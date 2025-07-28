import rclpy
from rclpy.node import Node
from talkrbot_msgs.msg import RefinedIntent
from std_msgs.msg import String
import google.generativeai as genai
import json
import os
import ast

class GROOTPlannerNode(Node):
    def __init__(self):
        super().__init__('groot_planner_node')
        self.subscription = self.create_subscription(
            RefinedIntent,
            '/refined_intent',
            self.refined_intent_callback,
            10
        )
        self.publisher = self.create_publisher(String, '/skill_plan', 10)
        self.get_logger().info('GROOTPlannerNode initialized and subscribed to /refined_intent')
        
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

    def refined_intent_callback(self, msg):
        if not self.model:
            self.get_logger().error('Gemini model not initialized. Skipping intent.')
            return
        
        try:
            # Build the prompt for skill planning
            prompt = self.build_prompt(msg.intent)
            self.get_logger().info(f'Planning for intent: "{msg.intent}" (priority: {msg.priority})')
            
            # Get response from Gemini
            response = self.model.generate_content(prompt)
            skill_plan = self.parse_response(response, msg.intent)
            
            if skill_plan:
                self.log_skill_plan(skill_plan, msg.intent)
                self.publish_skill_plan(skill_plan)
            else:
                self.get_logger().warning(f'Failed to parse skill plan for intent: "{msg.intent}"')
                
        except Exception as e:
            self.get_logger().error(f'Error planning for intent: {e}')

    def build_prompt(self, intent):
        prompt = f"""The robot has the following skills: go_to(location), grasp(object), place(object), wait(), speak(text).

The user intent is: {intent}.

Generate a list of steps (as Python function calls) the robot should execute to complete this task.

Respond ONLY with a JSON array of strings, where each string is a valid Python function call.

Example response:
[
  "go_to('closet')",
  "grasp('blanket')", 
  "go_to('user')",
  "place('blanket')"
]"""
        return prompt

    def parse_response(self, response, intent):
        try:
            if hasattr(response, 'text'):
                text = response.text
            elif hasattr(response, 'candidates') and response.candidates:
                text = response.candidates[0].text
            else:
                text = str(response)
            
            # Find JSON array in text
            start = text.find('[')
            end = text.rfind(']') + 1
            if start == -1 or end == -1:
                self.get_logger().error(f'No JSON array found in Gemini response: {text}')
                return None
            
            json_str = text[start:end]
            skill_list = json.loads(json_str)
            
            # Validate that it's a list of strings
            if not isinstance(skill_list, list):
                self.get_logger().error(f'Response is not a list: {skill_list}')
                return None
            
            # Validate each skill is a string and looks like a function call
            for i, skill in enumerate(skill_list):
                if not isinstance(skill, str):
                    self.get_logger().error(f'Skill {i} is not a string: {skill}')
                    return None
                
                # Basic validation that it looks like a function call
                if not (skill.startswith('go_to(') or skill.startswith('grasp(') or 
                       skill.startswith('place(') or skill.startswith('wait(') or 
                       skill.startswith('speak(')):
                    self.get_logger().warning(f'Skill {i} may not be a valid robot skill: {skill}')
            
            return skill_list
            
        except json.JSONDecodeError as e:
            self.get_logger().error(f'Invalid JSON in LLM response: {e}')
            return None
        except Exception as e:
            self.get_logger().error(f'Error parsing LLM response: {e}')
            return None

    def log_skill_plan(self, skill_plan, intent):
        try:
            self.get_logger().info(f'🎯 GROOT Plan for "{intent}":')
            self.get_logger().info(f'📋 Generated {len(skill_plan)} steps:')
            
            for i, skill in enumerate(skill_plan, 1):
                self.get_logger().info(f'  {i}. {skill}')
            
            self.get_logger().info(f'✅ Plan ready for execution (Ladder 6C)')
            
        except Exception as e:
            self.get_logger().error(f'Error logging skill plan: {e}')

    def publish_skill_plan(self, skill_plan):
        """Publish the skill plan to /skill_plan topic"""
        try:
            msg = String()
            msg.data = json.dumps(skill_plan)
            self.publisher.publish(msg)
            self.get_logger().info(f'📤 Published skill plan to /skill_plan')
        except Exception as e:
            self.get_logger().error(f'Error publishing skill plan: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = GROOTPlannerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main() 