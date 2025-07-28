import rclpy
from rclpy.node import Node
from talkrbot_msgs.msg import AACInput, RefinedIntent
import google.generativeai as genai
import json
import os
import uuid
from builtin_interfaces.msg import Time

class IntentRefinerNode(Node):
    def __init__(self):
        super().__init__('intent_refiner_node')
        
        # Subscribe to AAC input from user
        self.aac_subscription = self.create_subscription(
            AACInput,
            '/aac_input',
            self.aac_input_callback,
            10
        )
        
        # Subscribe to override intents from failure handler
        self.override_subscription = self.create_subscription(
            RefinedIntent,
            '/refined_intent',
            self.override_intent_callback,
            10
        )
        
        # Publisher for refined intents
        self.publisher = self.create_publisher(RefinedIntent, '/refined_intent', 10)
        
        # Track if we're currently processing an override
        self.processing_override = False
        
        self.get_logger().info('IntentRefinerNode initialized and subscribed to /aac_input and /refined_intent')
        
        # Set up Gemini API
        try:
            api_key = os.getenv('GEMINI_API_KEY')
            if not api_key:
                raise RuntimeError('GEMINI_API_KEY environment variable not set')
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
            self.get_logger().info('Gemini API configured successfully')
        except Exception as e:
            self.get_logger().error(f'Failed to initialize Gemini API: {e}')
            self.model = None

    def aac_input_callback(self, msg):
        """Process AAC input from user and refine intent"""
        if not self.model:
            self.get_logger().error('Gemini model not initialized. Skipping input.')
            return
        
        if self.processing_override:
            self.get_logger().info('Currently processing override, skipping AAC input')
            return
        
        try:
            # Build the prompt for intent refinement
            prompt = self.build_prompt(msg.text)
            self.get_logger().info(f'Processing AAC input: "{msg.text}"')
            
            # Get response from Gemini
            response = self.model.generate_content(prompt)
            refined_intent = self.parse_response(response, msg.text)
            
            if refined_intent:
                self.publish_refined_intent(refined_intent, msg, source="user")
            else:
                self.get_logger().warning(f'Failed to parse LLM response for input: "{msg.text}"')
                
        except Exception as e:
            self.get_logger().error(f'Error processing AAC input: {e}')
    
    def override_intent_callback(self, msg):
        """Process override intents from failure handler"""
        try:
            # Check if this is a high-priority override (from failure handler)
            if msg.priority == "high":
                self.processing_override = True
                self.get_logger().info(f'🔄 [OVERRIDE] Processing failure handler suggestion: {msg.intent}')
                
                # Publish the override intent directly
                self.publish_override_intent(msg)
                
                # Reset override flag after a short delay
                self.create_timer(2.0, self.reset_override_flag)
            else:
                # Normal intent, just log it
                self.get_logger().debug(f'Received normal intent: {msg.intent}')
                
        except Exception as e:
            self.get_logger().error(f'Error processing override intent: {e}')
    
    def reset_override_flag(self):
        """Reset the override processing flag"""
        self.processing_override = False
        self.get_logger().info('🔄 [OVERRIDE] Reset override flag, ready for new AAC input')

    def build_prompt(self, aac_text):
        prompt = f"""The user is using an AAC system and selected the phrase: '{aac_text}'. Please translate this into a clear, robot-actionable task.

Respond ONLY in JSON format with these fields:
- intent: The specific robot action (e.g., "bring blanket", "go to user", "turn on lights")
- user_location: Where the user is or wants the action (e.g., "couch", "bedroom", "kitchen") - use "unknown" if not specified
- priority: "high", "normal", or "low" based on urgency

Example response:
{{
  "intent": "bring blanket",
  "user_location": "couch", 
  "priority": "high"
}}"""
        return prompt

    def parse_response(self, response, original_text):
        try:
            if hasattr(response, 'text'):
                text = response.text
            elif hasattr(response, 'candidates') and response.candidates:
                text = response.candidates[0].text
            else:
                text = str(response)
            
            # Find JSON in text
            start = text.find('{')
            end = text.rfind('}') + 1
            if start == -1 or end == -1:
                self.get_logger().error(f'No JSON found in Gemini response: {text}')
                return None
            
            json_str = text[start:end]
            data = json.loads(json_str)
            
            # Validate required fields
            required_fields = ['intent', 'user_location', 'priority']
            for field in required_fields:
                if field not in data:
                    self.get_logger().error(f'Missing required field "{field}" in LLM response')
                    return None
            
            return data
            
        except json.JSONDecodeError as e:
            self.get_logger().error(f'Invalid JSON in LLM response: {e}')
            return None
        except Exception as e:
            self.get_logger().error(f'Error parsing LLM response: {e}')
            return None

    def publish_refined_intent(self, data, original_msg, source="user"):
        try:
            msg = RefinedIntent()
            msg.intent = str(data.get('intent', ''))
            msg.user_location = str(data.get('user_location', 'unknown'))
            msg.priority = str(data.get('priority', 'normal'))
            msg.original_text = original_msg.text
            msg.timestamp = self.get_clock().now().to_msg()
            
            self.publisher.publish(msg)
            self.get_logger().info(f'📋 [USER] Published refined intent: "{msg.intent}" (priority: {msg.priority}, location: {msg.user_location})')
            
        except Exception as e:
            self.get_logger().error(f'Error publishing refined intent: {e}')
    
    def publish_override_intent(self, override_msg):
        """Publish an override intent from failure handler"""
        try:
            # Create a new message to avoid circular publishing
            msg = RefinedIntent()
            msg.intent = override_msg.intent
            msg.user_location = override_msg.user_location
            msg.priority = override_msg.priority
            msg.original_text = f"override_from_failure_handler: {override_msg.intent}"
            msg.timestamp = self.get_clock().now().to_msg()
            
            self.publisher.publish(msg)
            self.get_logger().info(f'🔄 [OVERRIDE] Published override intent: "{msg.intent}" (priority: {msg.priority})')
            
        except Exception as e:
            self.get_logger().error(f'Error publishing override intent: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = IntentRefinerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main() 