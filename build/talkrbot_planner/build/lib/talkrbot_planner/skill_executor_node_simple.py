#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from std_msgs.msg import String
from talkrbot_msgs.msg import ExecutionFeedback
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped, Point, Quaternion
import json
import re
import time
import asyncio
import math

class SkillExecutorNodeSimple(Node):
    def __init__(self):
        super().__init__('skill_executor_node_simple')
        
        # Subscribe to skill plan (for now, we'll use a string topic)
        self.subscription = self.create_subscription(
            String,
            '/skill_plan',
            self.skill_plan_callback,
            10
        )
        self.feedback_publisher = self.create_publisher(ExecutionFeedback, '/execution_feedback', 10)
        
        # Nav2 Action Client
        self.nav2_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        
        # Location to pose mapping
        self.location_poses = {
            'kitchen': PoseStamped(
                header=None,
                pose=PoseStamped().pose
            ),
            'closet': PoseStamped(
                header=None,
                pose=PoseStamped().pose
            ),
            'living_room': PoseStamped(
                header=None,
                pose=PoseStamped().pose
            ),
            'bedroom': PoseStamped(
                header=None,
                pose=PoseStamped().pose
            ),
            'bathroom': PoseStamped(
                header=None,
                pose=PoseStamped().pose
            ),
            'fridge': PoseStamped(
                header=None,
                pose=PoseStamped().pose
            ),
            'user': PoseStamped(
                header=None,
                pose=PoseStamped().pose
            ),
            'table': PoseStamped(
                header=None,
                pose=PoseStamped().pose
            ),
            'couch': PoseStamped(
                header=None,
                pose=PoseStamped().pose
            ),
            'desk': PoseStamped(
                header=None,
                pose=PoseStamped().pose
            )
        }
        
        # Initialize location poses with default coordinates
        self._initialize_location_poses()
        
        self.get_logger().info('SkillExecutorNodeSimple initialized and subscribed to /skill_plan')
        self.get_logger().info('🤖 Nav2 Action Client initialized for navigation')
        
        # Track execution state
        self.is_executing = False
        self.current_plan = []
        
    def _initialize_location_poses(self):
        """Initialize location poses with default coordinates"""
        # Default poses for common locations
        poses = {
            'kitchen': {'x': 5.0, 'y': 0.0, 'z': 0.0, 'yaw': 0.0},
            'closet': {'x': 2.0, 'y': 3.0, 'z': 0.0, 'yaw': 1.57},
            'living_room': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'yaw': 0.0},
            'bedroom': {'x': -3.0, 'y': 2.0, 'z': 0.0, 'yaw': -0.785},
            'bathroom': {'x': -5.0, 'y': 0.0, 'z': 0.0, 'yaw': 3.14},
            'fridge': {'x': 4.5, 'y': 0.5, 'z': 0.0, 'yaw': 0.0},
            'user': {'x': 1.0, 'y': 1.0, 'z': 0.0, 'yaw': 0.0},
            'table': {'x': 2.0, 'y': 1.5, 'z': 0.0, 'yaw': 0.785},
            'couch': {'x': -1.0, 'y': 2.0, 'z': 0.0, 'yaw': 1.57},
            'desk': {'x': 3.0, 'y': -2.0, 'z': 0.0, 'yaw': -1.57}
        }
        
        for location, coords in poses.items():
            pose = PoseStamped()
            pose.header.frame_id = 'map'
            pose.pose.position.x = coords['x']
            pose.pose.position.y = coords['y']
            pose.pose.position.z = coords['z']
            
            # Convert yaw to quaternion
            yaw = coords['yaw']
            pose.pose.orientation.x = 0.0
            pose.pose.orientation.y = 0.0
            pose.pose.orientation.z = math.sin(yaw / 2.0)
            pose.pose.orientation.w = math.cos(yaw / 2.0)
            
            self.location_poses[location] = pose
            
        self.get_logger().info(f'🗺️ Initialized {len(self.location_poses)} location poses')
        
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
                return self.execute_grasp_mock(skill_args)
            elif skill_name == 'place':
                return self.execute_place_mock(skill_args)
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
        """Real Nav2 implementation of go_to skill"""
        self.get_logger().info(f'🤖 [EXEC] go_to("{location}") → Navigating to {location}...')
        
        # Check if location exists in our map
        if location not in self.location_poses:
            self.get_logger().error(f'❌ Unknown location: {location}')
            return False, f"Unknown location: {location}"
        
        # Get the target pose
        target_pose = self.location_poses[location]
        target_pose.header.stamp = self.get_clock().now().to_msg()
        
        # Wait for Nav2 action server to be available
        if not self.nav2_client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error('❌ Nav2 action server not available')
            return False, "Nav2 action server not available"
        
        # Create navigation goal
        goal = NavigateToPose.Goal()
        goal.pose = target_pose
        
        # Send goal and wait for result
        max_retries = 3
        for attempt in range(max_retries):
            try:
                self.get_logger().info(f'🎯 Sending navigation goal to {location} (attempt {attempt + 1}/{max_retries})')
                
                # Send goal
                goal_handle = self.nav2_client.send_goal_async(goal)
                
                # Wait for goal to be accepted
                if not goal_handle.done():
                    self.get_logger().info('⏳ Waiting for goal to be accepted...')
                    goal_handle.wait_for_result()
                
                if not goal_handle.accepted:
                    self.get_logger().error('❌ Navigation goal rejected')
                    if attempt < max_retries - 1:
                        self.get_logger().info(f'🔄 Retrying navigation to {location}...')
                        time.sleep(2.0)
                        continue
                    return False, f"Navigation goal rejected after {max_retries} attempts"
                
                # Wait for navigation to complete
                self.get_logger().info('🚶 Navigation in progress...')
                result = goal_handle.get_result()
                
                if result and result.result == NavigateToPose.Result.SUCCEEDED:
                    self.get_logger().info(f'✅ Successfully navigated to {location}')
                    return True, f"Successfully navigated to {location}"
                else:
                    self.get_logger().warn(f'⚠️ Navigation to {location} failed')
                    if attempt < max_retries - 1:
                        self.get_logger().info(f'🔄 Retrying navigation to {location}...')
                        time.sleep(2.0)
                        continue
                    return False, f"Navigation to {location} failed after {max_retries} attempts"
                    
            except Exception as e:
                self.get_logger().error(f'❌ Navigation error: {e}')
                if attempt < max_retries - 1:
                    self.get_logger().info(f'🔄 Retrying navigation to {location}...')
                    time.sleep(2.0)
                    continue
                return False, f"Navigation error: {e}"
        
        return False, f"Failed to navigate to {location} after {max_retries} attempts"

    def execute_grasp_mock(self, object_name):
        """Mock implementation of grasp skill (for testing)"""
        self.get_logger().info(f'🤖 [EXEC] grasp("{object_name}") → Grasping {object_name}...')
        
        # Simulate grasping time
        time.sleep(1.5)
        
        self.get_logger().info(f'✅ Successfully grasped {object_name}')
        return True, f"Successfully grasped {object_name}"

    def execute_place_mock(self, object_name):
        """Mock implementation of place skill (for testing)"""
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
    node = SkillExecutorNodeSimple()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main() 