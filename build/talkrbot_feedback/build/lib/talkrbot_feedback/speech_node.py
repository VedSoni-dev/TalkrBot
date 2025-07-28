#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from talkrbot_msgs.msg import AACInput
import time
import threading

class SpeechNode(Node):
    def __init__(self):
        super().__init__('speech_node')
        
        # Subscribe to speech commands
        self.speech_subscription = self.create_subscription(
            String,
            '/speak_command',
            self.speak_command_callback,
            10
        )
        
        # Subscribe to AAC input for user responses
        self.aac_subscription = self.create_subscription(
            AACInput,
            '/aac_input',
            self.aac_input_callback,
            10
        )
        
        # Publisher for user responses to speech
        self.response_publisher = self.create_publisher(
            String,
            '/speech_response',
            10
        )
        
        # State tracking
        self.waiting_for_response = False
        self.current_question = ""
        self.response_timeout = 30.0  # seconds
        self.response_timer = None
        
        self.get_logger().info('SpeechNode initialized and subscribed to /speak_command and /aac_input')
    
    def speak_command_callback(self, msg):
        """Handle speech commands from failure handler"""
        try:
            text = msg.data
            self.get_logger().info(f'🗣️ [SPEECH] Speaking: "{text}"')
            
            # Check if this is a question that needs a response
            if self.is_question(text):
                self.wait_for_user_response(text)
            else:
                # Just informational speech, no response needed
                self.speak_text(text)
                
        except Exception as e:
            self.get_logger().error(f'Error processing speech command: {e}')
    
    def is_question(self, text):
        """Check if the text is a question that needs a response"""
        question_indicators = [
            "?", "should", "would", "could", "can", "will", "do you want",
            "would you like", "should i", "could i", "instead", "alternative"
        ]
        
        text_lower = text.lower()
        return any(indicator in text_lower for indicator in question_indicators)
    
    def speak_text(self, text):
        """Simulate speaking the text (in real implementation, this would use TTS)"""
        self.get_logger().info(f'🗣️ [TTS] "{text}"')
        
        # In a real implementation, this would:
        # 1. Convert text to speech using TTS engine
        # 2. Play the audio through speakers
        # 3. Wait for completion
        
        # For now, just simulate the delay
        time.sleep(2.0)
        self.get_logger().info('🗣️ [TTS] Speech completed')
    
    def wait_for_user_response(self, question):
        """Wait for user response to a question"""
        if self.waiting_for_response:
            self.get_logger().warn('Already waiting for response, ignoring new question')
            return
        
        self.waiting_for_response = True
        self.current_question = question
        
        # Speak the question
        self.speak_text(question)
        
        # Set up response timeout
        self.response_timer = self.create_timer(self.response_timeout, self.handle_response_timeout)
        
        self.get_logger().info(f'👂 [LISTENING] Waiting for user response to: "{question}"')
    
    def aac_input_callback(self, msg):
        """Handle AAC input from user"""
        if not self.waiting_for_response:
            # Not waiting for response, just log it
            self.get_logger().debug(f'Received AAC input (not waiting): {msg.text}')
            return
        
        try:
            response = msg.text
            self.get_logger().info(f'👤 [RESPONSE] User said: "{response}"')
            
            # Cancel the timeout timer
            if self.response_timer:
                self.response_timer.cancel()
                self.response_timer = None
            
            # Publish the response
            response_msg = String()
            response_msg.data = response
            self.response_publisher.publish(response_msg)
            
            # Reset waiting state
            self.waiting_for_response = False
            self.current_question = ""
            
            self.get_logger().info(f'✅ [RESPONSE] Processed user response: "{response}"')
            
        except Exception as e:
            self.get_logger().error(f'Error processing user response: {e}')
    
    def handle_response_timeout(self):
        """Handle timeout when no response is received"""
        if not self.waiting_for_response:
            return
        
        self.get_logger().warn(f'⏰ [TIMEOUT] No response received for: "{self.current_question}"')
        
        # Publish a timeout response
        timeout_msg = String()
        timeout_msg.data = "timeout_no_response"
        self.response_publisher.publish(timeout_msg)
        
        # Reset waiting state
        self.waiting_for_response = False
        self.current_question = ""
        self.response_timer = None

def main(args=None):
    rclpy.init(args=args)
    node = SpeechNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main() 