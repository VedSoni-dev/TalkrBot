import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from talkrbot_msgs.msg import ExecutionFeedback
import json
import re
import time
import asyncio

class SkillExecutorNode(Node):
    def __init__(self):
        super().__init__('skill_executor_node')
        
        # Subscribe to skill plan (for now, we'll use a string topic)
        self.subscription = self.create_subscription(
            String,
            '/skill_plan',
            self.skill_plan_callback,
            10
        )
        self.feedback_publisher = self.create_publisher(ExecutionFeedback, '/execution_feedback', 10)
        
        self.get_logger().info('SkillExecutorNode initialized and subscribed to /skill_plan')
        
        # Track execution state
        self.is_executing = False
        self.current_plan = []

    def skill_plan_callback(self, msg):
        """Handle incoming skill plan as JSON string"""
        if self.is_executing:
            self.get_logger().warn('Already executing a plan. Ignoring new plan.')
            return
            
        try:
            # Parse the skill plan from JSON string
            skill_plan = json.loads(msg.data)
            
            if not isinstance(skill_plan, list):
                self.get_logger().error('Skill plan must be a list of strings')
                return
                
            self.get_logger().info(f'Received skill plan with {len(skill_plan)} steps')
            self.execute_skill_plan(skill_plan)
            
        except json.JSONDecodeError as e:
            self.get_logger().error(f'Failed to parse skill plan JSON: {e}')
        except Exception as e:
            self.get_logger().error(f'Error processing skill plan: {e}')

    def execute_skill_plan(self, skill_plan):
        """Execute a list of skills sequentially"""
        self.is_executing = True
        self.current_plan = skill_plan
        
        self.get_logger().info(f'🚀 Starting execution of {len(skill_plan)} skills')
        
        for i, skill_str in enumerate(skill_plan, 1):
            try:
                self.get_logger().info(f'📋 Step {i}/{len(skill_plan)}: {skill_str}')
                
                # Parse and execute the skill
                success, notes = self.execute_skill(skill_str)
                
                # Publish execution feedback
                self.publish_execution_feedback(skill_str, success, notes)
                
                if success:
                    self.get_logger().info(f'✅ Step {i} completed successfully')
                else:
                    self.get_logger().error(f'❌ Step {i} failed. Stopping execution.')
                    break
                    
                # Small delay between skills
                time.sleep(0.5)
                
            except Exception as e:
                self.get_logger().error(f'❌ Error executing step {i}: {e}')
                break
        
        self.get_logger().info('🏁 Skill plan execution completed')
        self.is_executing = False
        self.current_plan = []

    def execute_skill(self, skill_str):
        """Execute a single skill command"""
        try:
            # Parse the skill command using regex
            # Match patterns like: go_to('location'), grasp('object'), etc.
            match = re.match(r'(\w+)\(([^)]*)\)', skill_str.strip())
            
            if not match:
                self.get_logger().error(f'Invalid skill format: {skill_str}')
                return False, f"Invalid skill format: {skill_str}"
                
            skill_name = match.group(1)
            skill_args = match.group(2).strip("'\"")  # Remove quotes
            
            # Execute the appropriate skill
            if skill_name == 'go_to':
                return self.execute_go_to(skill_args)
            elif skill_name == 'grasp':
                return self.execute_grasp(skill_args)
            elif skill_name == 'place':
                return self.execute_place(skill_args)
            elif skill_name == 'wait':
                return self.execute_wait(skill_args)
            elif skill_name == 'speak':
                return self.execute_speak(skill_args)
            else:
                self.get_logger().error(f'Unknown skill: {skill_name}')
                return False, f"Unknown skill: {skill_name}"
                
        except Exception as e:
            self.get_logger().error(f'Error parsing skill "{skill_str}": {e}')
            return False, f"Error parsing skill: {e}"

    def execute_go_to(self, location):
        """Mock implementation of go_to skill"""
        self.get_logger().info(f'🤖 [EXEC] go_to("{location}") → Navigating to {location}...')
        
        # Simulate navigation time
        time.sleep(2.0)
        
        self.get_logger().info(f'✅ Arrived at {location}')
        return True, f"Successfully navigated to {location}"

    def execute_grasp(self, object_name):
        """Mock implementation of grasp skill"""
        self.get_logger().info(f'🤖 [EXEC] grasp("{object_name}") → Grasping {object_name}...')
        
        # Simulate grasping time
        time.sleep(1.5)
        
        self.get_logger().info(f'✅ Successfully grasped {object_name}')
        return True, f"Successfully grasped {object_name}"

    def execute_place(self, object_name):
        """Mock implementation of place skill"""
        self.get_logger().info(f'🤖 [EXEC] place("{object_name}") → Placing {object_name}...')
        
        # Simulate placing time
        time.sleep(1.0)
        
        self.get_logger().info(f'✅ Successfully placed {object_name}')
        return True, f"Successfully placed {object_name}"

    def execute_wait(self, duration_str):
        """Mock implementation of wait skill"""
        try:
            duration = float(duration_str) if duration_str else 1.0
        except ValueError:
            duration = 1.0
            
        self.get_logger().info(f'🤖 [EXEC] wait({duration}) → Waiting for {duration} seconds...')
        
        # Simulate waiting
        time.sleep(duration)
        
        self.get_logger().info(f'✅ Wait completed')
        return True, f"Successfully waited for {duration} seconds"

    def execute_speak(self, text):
        """Mock implementation of speak skill"""
        self.get_logger().info(f'🤖 [EXEC] speak("{text}") → Speaking: "{text}"')
        
        # Simulate speech time
        time.sleep(len(text) * 0.1)  # Rough estimate based on text length
        
        self.get_logger().info(f'✅ Speech completed')
        return True, f"Successfully spoke: '{text}'"

    def publish_execution_feedback(self, step, success, notes):
        """Publish execution feedback to /execution_feedback topic"""
        try:
            msg = ExecutionFeedback()
            msg.step = step
            msg.status = "success" if success else "failure"
            msg.notes = notes
            msg.timestamp = self.get_clock().now().to_msg()
            
            self.feedback_publisher.publish(msg)
            
            status_emoji = "✅" if success else "❌"
            self.get_logger().info(f'{status_emoji} [FEEDBACK] {step} → {msg.status}: {notes}')
            
        except Exception as e:
            self.get_logger().error(f'Error publishing execution feedback: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = SkillExecutorNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main() 