import os
import rclpy
from rclpy.node import Node
from talkrbot_msgs.msg import AACInput, TaskCommand
from std_msgs.msg import String
import uuid
import json
from datetime import datetime
from rclpy.time import Time

# Gemini API
import google.generativeai as genai

def get_gemini_api_key():
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise RuntimeError('GEMINI_API_KEY environment variable not set')
    return api_key

class LLMNode(Node):
    def __init__(self):
        super().__init__('llm_node')
        self.subscription = self.create_subscription(
            AACInput,
            '/aac_input',
            self.aac_input_callback,
            10
        )
        self.publisher = self.create_publisher(TaskCommand, '/task_command', 10)
        self.get_logger().info('LLMNode initialized and subscribed to /aac_input')
        # Set up Gemini API
        try:
            genai.configure(api_key=get_gemini_api_key())
            self.model = genai.GenerativeModel('gemini-pro')
        except Exception as e:
            self.get_logger().error(f'Failed to initialize Gemini API: {e}')
            self.model = None

    def aac_input_callback(self, msg):
        if not self.model:
            self.get_logger().error('Gemini model not initialized. Skipping input.')
            return
        prompt = self.build_prompt(msg)
        try:
            response = self.model.generate_content(prompt)
            command = self.parse_response(response)
            if command:
                self.publish_task_command(command, msg)
            else:
                self.get_logger().error('Gemini response could not be parsed into a command.')
        except Exception as e:
            self.get_logger().error(f'Gemini API error: {e}')

    def build_prompt(self, msg):
        # Prompt engineering for structured robot command
        prompt = (
            f"AAC input: '{msg.text}'\n"
            "Interpret this as a robot command. Respond ONLY in JSON with these fields: "
            "task, object, location, parameters (as JSON string), confidence (0.0-1.0), command_id (UUID), timestamp (ISO8601)."
        )
        return prompt

    def parse_response(self, response):
        # Try to extract JSON from Gemini response
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
            return data
        except Exception as e:
            self.get_logger().error(f'Error parsing Gemini response: {e}')
            return None

    def publish_task_command(self, data, aac_msg):
        try:
            msg = TaskCommand()
            msg.task = data.get('task', '')
            msg.object = data.get('object', '')
            msg.location = data.get('location', '')
            msg.parameters = data.get('parameters', '{}')
            msg.confidence = float(data.get('confidence', 0.0))
            msg.command_id = data.get('command_id', str(uuid.uuid4()))
            # Use current time if not provided
            if 'timestamp' in data:
                try:
                    dt = datetime.fromisoformat(data['timestamp'])
                    msg.timestamp = Time(seconds=int(dt.timestamp())).to_msg()
                except Exception:
                    msg.timestamp = self.get_clock().now().to_msg()
            else:
                msg.timestamp = self.get_clock().now().to_msg()
            self.publisher.publish(msg)
            self.get_logger().info(f'Published TaskCommand: {msg}')
        except Exception as e:
            self.get_logger().error(f'Error publishing TaskCommand: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = LLMNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main() 