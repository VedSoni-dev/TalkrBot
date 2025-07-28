import os
import rclpy
from rclpy.node import Node
from talkrbot_msgs.msg import AACInput, RefinedIntent
import google.generativeai as genai
import uuid
from rclpy.time import Time

def get_gemini_api_key():
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise RuntimeError('GEMINI_API_KEY environment variable not set')
    return api_key

class IntentRefinerNode(Node):
    def __init__(self):
        super().__init__('intent_refiner_node')
        self.subscription = self.create_subscription(
            AACInput,
            '/aac_input',
            self.aac_input_callback,
            10
        )
        self.publisher = self.create_publisher(RefinedIntent, '/refined_intent', 10)
        self.get_logger().info('IntentRefinerNode initialized and subscribed to /aac_input')
        
        # Set up Gemini API
        try:
            genai.configure(api_key=get_gemini_api_key())
            self.model = genai.GenerativeModel('gemini-2.5-flash')
        except Exception as e:
            self.get_logger().error(f'Failed to initialize Gemini API: {e}')
            self.model = None

    def aac_input_callback(self, msg):
        if not self.model:
            self.get_logger().error('Gemini model not initialized. Skipping input.')
            return
        
        try:
            # Build prompt for intent refinement
            prompt = self.build_refinement_prompt(msg)
            
            # Get Gemini response
            response = self.model.generate_content(prompt)
            refined_intent = self.parse_response(response, msg)
            
            if refined_intent:
                self.publish_refined_intent(refined_intent, msg)
            else:
                self.get_logger().error('Failed to parse Gemini response into refined intent.')
                
        except Exception as e:
            self.get_logger().error(f'Intent refinement failed: {e}')

    def build_refinement_prompt(self, msg):
        prompt = f"""
        You are an intent refiner for an assistive robot. Transform vague AAC input into clear, actionable robot tasks.
        
        AAC Input: "{msg.text}"
        User ID: {msg.user_id}
        Input Method: {msg.input_method}
        
        Respond with a JSON object containing:
        - "intent": The specific task the robot should perform (e.g., "bring blanket", "go to user", "bring water")
        - "user_location": Where the user is or wants the robot to go (e.g., "couch", "kitchen", "bedroom") - use "unknown" if not specified
        - "priority": "high", "normal", or "low" based on urgency
        - "reasoning": Brief explanation of the transformation
        
        Examples:
        - "I'm cold" → {{"intent": "bring blanket", "user_location": "unknown", "priority": "normal", "reasoning": "User is cold, needs warmth"}}
        - "Help" → {{"intent": "go to user", "user_location": "unknown", "priority": "high", "reasoning": "User needs immediate assistance"}}
        - "Water yummy more" → {{"intent": "bring water", "user_location": "unknown", "priority": "normal", "reasoning": "User enjoyed water and wants more"}}
        
        Respond ONLY with valid JSON.
        """
        return prompt

    def parse_response(self, response, original_msg):
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
            
            import json
            json_str = text[start:end]
            data = json.loads(json_str)
            
            return {
                'intent': data.get('intent', ''),
                'user_location': data.get('user_location', 'unknown'),
                'priority': data.get('priority', 'normal'),
                'reasoning': data.get('reasoning', '')
            }
            
        except Exception as e:
            self.get_logger().error(f'Error parsing Gemini response: {e}')
            return None

    def publish_refined_intent(self, refined_data, original_msg):
        try:
            msg = RefinedIntent()
            msg.intent = refined_data['intent']
            msg.user_location = refined_data['user_location']
            msg.priority = refined_data['priority']
            msg.original_text = original_msg.text
            msg.timestamp = self.get_clock().now().to_msg()
            
            self.publisher.publish(msg)
            self.get_logger().info(f'Refined intent: "{original_msg.text}" → "{refined_data["intent"]}" (priority: {refined_data["priority"]})')
            
        except Exception as e:
            self.get_logger().error(f'Error publishing refined intent: {e}')

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