#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from talkrbot_msgs.msg import ExecutionFeedback, RefinedIntent
from std_msgs.msg import String
import google.generativeai as genai
import os
import json
import re
from datetime import datetime

class FailureHandlerNode(Node):
    def __init__(self):
        super().__init__('failure_handler_node')
        
        # Subscribe to execution feedback
        self.feedback_subscription = self.create_subscription(
            ExecutionFeedback,
            '/execution_feedback',
            self.feedback_callback,
            10
        )
        
        # Subscribe to refined intent to track current task
        self.intent_subscription = self.create_subscription(
            RefinedIntent,
            '/refined_intent',
            self.intent_callback,
            10
        )
        
        # Subscribe to speech responses
        self.speech_response_subscription = self.create_subscription(
            String,
            '/speech_response',
            self.speech_response_callback,
            10
        )
        
        # Publisher for new refined intent suggestions
        self.intent_publisher = self.create_publisher(
            RefinedIntent,
            '/refined_intent',
            10
        )
        
        # Publisher for speech commands
        self.speech_publisher = self.create_publisher(
            String,
            '/speak_command',
            10
        )
        
        # Initialize Gemini
        self.init_gemini()
        
        # Track current task context
        self.current_intent = None
        self.failed_steps = []
        self.waiting_for_speech_response = False
        self.pending_suggestion = None
        
        self.get_logger().info('FailureHandlerNode initialized and subscribed to /execution_feedback')
        
    def init_gemini(self):
        """Initialize Gemini API"""
        try:
            api_key = os.getenv('GEMINI_API_KEY')
            if not api_key:
                raise RuntimeError('GEMINI_API_KEY environment variable not set')
            
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
            
            self.get_logger().info('Gemini API initialized successfully')
            
        except Exception as e:
            self.get_logger().error(f'Failed to initialize Gemini: {e}')
            raise
    
    def intent_callback(self, msg):
        """Track the current refined intent"""
        self.current_intent = msg
        self.failed_steps = []  # Reset failed steps for new intent
        self.get_logger().info(f'📋 Tracking new intent: {msg.intent}')
    
    def speech_response_callback(self, msg):
        """Handle user response to speech question"""
        try:
            response = msg.data
            self.get_logger().info(f'👤 [SPEECH] User responded: "{response}"')
            
            if self.waiting_for_speech_response and self.pending_suggestion:
                self.waiting_for_speech_response = False
                
                # Process the user response
                if response.lower() in ['yes', 'okay', 'sure', 'juice', 'milk', 'water']:
                    # User agreed to the suggestion
                    self.get_logger().info('✅ [SPEECH] User agreed to suggestion, publishing alternative intent')
                    self.publish_alternative_intent(self.pending_suggestion, self.build_failure_context_from_pending())
                elif response.lower() in ['no', 'cancel', 'stop', 'timeout_no_response']:
                    # User declined or timeout
                    self.get_logger().info('❌ [SPEECH] User declined suggestion or timeout')
                else:
                    # User provided a different response, try to interpret it
                    self.handle_user_alternative_response(response)
                
                self.pending_suggestion = None
                
        except Exception as e:
            self.get_logger().error(f'Error processing speech response: {e}')
    
    def feedback_callback(self, msg):
        """Process execution feedback and handle failures"""
        try:
            if msg.status == "failure":
                self.get_logger().info(f'❌ [FAILURE] {msg.step}: {msg.notes}')
                self.failed_steps.append({
                    'step': msg.step,
                    'notes': msg.notes,
                    'timestamp': msg.timestamp
                })
                
                # Generate alternative suggestion
                self.handle_failure(msg)
            else:
                self.get_logger().debug(f'✅ [SUCCESS] {msg.step}')
                
        except Exception as e:
            self.get_logger().error(f'Error processing feedback: {e}')
    
    def handle_failure(self, failed_msg):
        """Handle a failure by generating alternative suggestions"""
        try:
            # Build context for Gemini
            context = self.build_failure_context(failed_msg)
            
            # Generate prompt
            prompt = self.build_gemini_prompt(context)
            
            # Get response from Gemini
            response = self.get_gemini_suggestion(prompt)
            
            # Handle the response with speech interaction
            if response:
                self.handle_suggestion_with_speech(response, context)
                
        except Exception as e:
            self.get_logger().error(f'Error handling failure: {e}')
    
    def handle_suggestion_with_speech(self, suggestion, context):
        """Handle suggestion with speech interaction"""
        try:
            message = suggestion.get('message', '')
            
            if message and self.is_question(message):
                # Speak the question and wait for response
                self.waiting_for_speech_response = True
                self.pending_suggestion = suggestion
                
                # Publish speech command
                speech_msg = String()
                speech_msg.data = message
                self.speech_publisher.publish(speech_msg)
                
                self.get_logger().info(f'🗣️ [SPEECH] Speaking question: "{message}"')
            else:
                # No question, just publish the alternative intent directly
                self.publish_alternative_intent(suggestion, context)
                
        except Exception as e:
            self.get_logger().error(f'Error handling suggestion with speech: {e}')
    
    def is_question(self, text):
        """Check if text contains a question"""
        question_indicators = ['?', 'should', 'would', 'could', 'instead', 'alternative']
        return any(indicator in text.lower() for indicator in question_indicators)
    
    def handle_user_alternative_response(self, response):
        """Handle when user provides a different response"""
        try:
            # Try to interpret the user's response as a new intent
            self.get_logger().info(f'🤔 [SPEECH] Interpreting user response: "{response}"')
            
            # For now, just log it. In a full implementation, this could use Gemini
            # to interpret the response and generate a new intent
            
        except Exception as e:
            self.get_logger().error(f'Error handling user alternative response: {e}')
    
    def build_failure_context_from_pending(self):
        """Build context from pending suggestion"""
        return {
            'failed_step': 'unknown',
            'failure_reason': 'user_response',
            'current_intent': self.current_intent.intent if self.current_intent else "unknown",
            'user_location': self.current_intent.user_location if self.current_intent else "unknown",
            'priority': "high",
            'failed_steps_count': len(self.failed_steps)
        }
    
    def build_failure_context(self, failed_msg):
        """Build context about the failure"""
        context = {
            'failed_step': failed_msg.step,
            'failure_reason': failed_msg.notes,
            'current_intent': self.current_intent.intent if self.current_intent else "unknown",
            'user_location': self.current_intent.user_location if self.current_intent else "unknown",
            'priority': self.current_intent.priority if self.current_intent else "medium",
            'failed_steps_count': len(self.failed_steps)
        }
        return context
    
    def build_gemini_prompt(self, context):
        """Build a prompt for Gemini to suggest alternatives"""
        prompt = f"""
You are a helpful robot assistant. The robot just failed to complete a task and needs to ask the user for clarification or suggest alternatives.

**Context:**
- Original user intent: "{context['current_intent']}"
- Failed step: {context['failed_step']}
- Failure reason: {context['failure_reason']}
- User location: {context['user_location']}
- Number of previous failures: {context['failed_steps_count']}

**Task:**
Generate a helpful response that either:
1. Asks the user for clarification
2. Suggests an alternative approach
3. Offers different options

**Response Format:**
Return a JSON object with these fields:
- "response_type": "clarification" | "alternative" | "options"
- "message": "The message to show the user"
- "suggested_intent": "New refined intent if suggesting alternative"
- "confidence": 0.0-1.0 (how confident in the suggestion)

**Examples:**
- If water bottle not found: suggest juice, milk, or ask what they prefer
- If location unreachable: suggest alternative locations or ask for help
- If object not found: suggest similar objects or ask for clarification

Generate a helpful, natural response that maintains the user's original goal.
"""
        return prompt
    
    def get_gemini_suggestion(self, prompt):
        """Get suggestion from Gemini"""
        try:
            response = self.model.generate_content(prompt)
            
            # Try to parse JSON response
            try:
                # Look for JSON in the response
                json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                if json_match:
                    suggestion = json.loads(json_match.group())
                    self.get_logger().info(f'🤖 [GEMINI] Generated suggestion: {suggestion}')
                    return suggestion
                else:
                    # Fallback: create a simple response
                    self.get_logger().warn('Could not parse JSON from Gemini response, using fallback')
                    return {
                        "response_type": "clarification",
                        "message": f"I couldn't complete {response.text[:100]}... What would you like me to do instead?",
                        "suggested_intent": "ask_user_for_alternative",
                        "confidence": 0.5
                    }
                    
            except json.JSONDecodeError as e:
                self.get_logger().error(f'Failed to parse Gemini response as JSON: {e}')
                return None
                
        except Exception as e:
            self.get_logger().error(f'Error getting Gemini suggestion: {e}')
            return None
    
    def publish_alternative_intent(self, suggestion, context):
        """Publish a new refined intent based on the suggestion"""
        try:
            msg = RefinedIntent()
            
            if suggestion.get('suggested_intent') and suggestion.get('suggested_intent') != "ask_user_for_alternative":
                msg.intent = suggestion['suggested_intent']
            else:
                # Generate a new intent based on the original
                msg.intent = f"alternative_approach_for_{context['current_intent']}"
            
            msg.user_location = context['user_location']
            msg.priority = "high"  # Failure handling is high priority
            msg.timestamp = self.get_clock().now().to_msg()
            
            self.intent_publisher.publish(msg)
            
            self.get_logger().info(f'🔄 [REPLAN] Published alternative intent: {msg.intent}')
            self.get_logger().info(f'💬 [USER] {suggestion.get("message", "No message provided")}')
            
        except Exception as e:
            self.get_logger().error(f'Error publishing alternative intent: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = FailureHandlerNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main() 