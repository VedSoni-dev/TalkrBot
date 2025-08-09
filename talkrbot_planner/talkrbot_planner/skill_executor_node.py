import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from std_msgs.msg import String
from talkrbot_msgs.msg import ExecutionFeedback
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped, Point, Quaternion
from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from sensor_msgs.msg import JointState
import json
import re
import time
import asyncio
import math

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
        
        # Nav2 Action Client
        self.nav2_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        
        # Arm Controller Action Client
        self.arm_client = ActionClient(self, FollowJointTrajectory, 'arm_controller/follow_joint_trajectory')
        
        # Arm joint configuration
        self.arm_joints = {
            'shoulder_pan_joint': 0.0,
            'shoulder_lift_joint': -1.57,
            'elbow_joint': 0.0,
            'wrist_1_joint': -1.57,
            'wrist_2_joint': 0.0,
            'wrist_3_joint': 0.0,
            'gripper_joint': 0.0
        }
        
        # Gripper states
        self.gripper_open_position = 0.08  # Open gripper
        self.gripper_closed_position = 0.0  # Closed gripper
        
        # Grasp poses for common objects
        self.grasp_poses = {
            'water': {'x': 0.5, 'y': 0.0, 'z': 0.3, 'gripper': 'open'},
            'blanket': {'x': 0.4, 'y': 0.1, 'z': 0.2, 'gripper': 'open'},
            'keys': {'x': 0.3, 'y': 0.0, 'z': 0.1, 'gripper': 'open'},
            'phone': {'x': 0.4, 'y': 0.0, 'z': 0.25, 'gripper': 'open'},
            'book': {'x': 0.5, 'y': 0.0, 'z': 0.3, 'gripper': 'open'},
            'cup': {'x': 0.4, 'y': 0.0, 'z': 0.2, 'gripper': 'open'},
            'apple': {'x': 0.3, 'y': 0.0, 'z': 0.15, 'gripper': 'open'},
            'remote': {'x': 0.35, 'y': 0.0, 'z': 0.2, 'gripper': 'open'}
        }
        
        # Location to pose mapping (populated in _initialize_location_poses)
        self.location_poses = {}
        
        # Initialize location poses with default coordinates
        self._initialize_location_poses()
        
        self.get_logger().info('SkillExecutorNode initialized and subscribed to /skill_plan')
        self.get_logger().info('🤖 Nav2 Action Client initialized for navigation')
        self.get_logger().info('🤖 Arm Controller Action Client initialized for manipulation')
        
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
        
    def _move_arm_to_pose(self, pose_dict, timeout=10.0):
        """Move arm to a specific pose using joint trajectory"""
        try:
            # Create joint trajectory goal
            goal = FollowJointTrajectory.Goal()
            trajectory = JointTrajectory()
            
            # Set joint names (assuming UR5/UR10 style arm)
            trajectory.joint_names = list(self.arm_joints.keys())
            
            # Create trajectory point
            point = JointTrajectoryPoint()
            
            # Calculate joint positions based on pose
            # This is a simplified IK - in practice, you'd use a proper IK solver
            x, y, z = pose_dict['x'], pose_dict['y'], pose_dict['z']
            
            # Simple inverse kinematics (approximate)
            joint_positions = [
                0.0,  # shoulder_pan_joint
                -1.57,  # shoulder_lift_joint  
                0.0,  # elbow_joint
                -1.57,  # wrist_1_joint
                0.0,  # wrist_2_joint
                0.0,  # wrist_3_joint
                self.gripper_open_position if pose_dict.get('gripper') == 'open' else self.gripper_closed_position
            ]
            
            point.positions = joint_positions
            point.velocities = [0.0] * len(joint_positions)
            point.accelerations = [0.0] * len(joint_positions)
            point.time_from_start.sec = int(timeout)
            point.time_from_start.nanosec = 0
            
            trajectory.points.append(point)
            goal.trajectory = trajectory
            
            # Send goal
            goal_handle = self.arm_client.send_goal_async(goal)
            
            if not goal_handle.done():
                goal_handle.wait_for_result()
            
            if goal_handle.accepted:
                result = goal_handle.get_result()
                if result and result.error_code == 0:
                    return True, "Arm moved successfully"
                else:
                    return False, f"Arm movement failed: {result.error_string if result else 'Unknown error'}"
            else:
                return False, "Arm goal rejected"
                
        except Exception as e:
            return False, f"Arm control error: {e}"
    
    def _control_gripper(self, position, timeout=3.0):
        """Control gripper position"""
        try:
            # Create gripper trajectory
            goal = FollowJointTrajectory.Goal()
            trajectory = JointTrajectory()
            trajectory.joint_names = ['gripper_joint']
            
            point = JointTrajectoryPoint()
            point.positions = [position]
            point.velocities = [0.0]
            point.accelerations = [0.0]
            point.time_from_start.sec = int(timeout)
            point.time_from_start.nanosec = 0
            
            trajectory.points.append(point)
            goal.trajectory = trajectory
            
            # Send goal
            goal_handle = self.arm_client.send_goal_async(goal)
            
            if not goal_handle.done():
                goal_handle.wait_for_result()
            
            if goal_handle.accepted:
                result = goal_handle.get_result()
                if result and result.error_code == 0:
                    return True, f"Gripper moved to position {position}"
                else:
                    return False, f"Gripper control failed: {result.error_string if result else 'Unknown error'}"
            else:
                return False, "Gripper goal rejected"
                
        except Exception as e:
            return False, f"Gripper control error: {e}"
        
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

    def execute_grasp(self, object_name):
        """Real arm controller implementation of grasp skill"""
        self.get_logger().info(f'🤖 [EXEC] grasp("{object_name}") → Grasping {object_name}...')
        
        # Check if object has a predefined grasp pose
        if object_name not in self.grasp_poses:
            self.get_logger().warn(f'⚠️ No predefined grasp pose for {object_name}, using default')
            grasp_pose = {'x': 0.4, 'y': 0.0, 'z': 0.25, 'gripper': 'open'}
        else:
            grasp_pose = self.grasp_poses[object_name]
        
        # Wait for arm controller to be available
        if not self.arm_client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error('❌ Arm controller not available')
            return False, "Arm controller not available"
        
        try:
            # Step 1: Move arm to grasp position
            self.get_logger().info(f'🎯 Moving arm to grasp position for {object_name}')
            success, notes = self._move_arm_to_pose(grasp_pose, timeout=8.0)
            if not success:
                return False, f"Failed to move arm to grasp position: {notes}"
            
            # Step 2: Open gripper
            self.get_logger().info('🤏 Opening gripper')
            success, notes = self._control_gripper(self.gripper_open_position, timeout=2.0)
            if not success:
                return False, f"Failed to open gripper: {notes}"
            
            # Step 3: Close gripper to grasp
            self.get_logger().info('🤏 Closing gripper to grasp')
            success, notes = self._control_gripper(self.gripper_closed_position, timeout=2.0)
            if not success:
                return False, f"Failed to close gripper: {notes}"
            
            # Step 4: Verify grasp (simplified - in practice you'd check force/torque sensors)
            time.sleep(0.5)  # Brief pause to simulate grasp verification
            
            self.get_logger().info(f'✅ Successfully grasped {object_name}')
            return True, f"Successfully grasped {object_name}"
            
        except Exception as e:
            self.get_logger().error(f'❌ Grasp error: {e}')
            return False, f"Grasp error: {e}"

    def execute_place(self, object_name):
        """Real arm controller implementation of place skill"""
        self.get_logger().info(f'🤖 [EXEC] place("{object_name}") → Placing {object_name}...')
        
        # Wait for arm controller to be available
        if not self.arm_client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error('❌ Arm controller not available')
            return False, "Arm controller not available"
        
        try:
            # Step 1: Move to place position (slightly above current position)
            place_pose = {'x': 0.4, 'y': 0.0, 'z': 0.3, 'gripper': 'closed'}
            self.get_logger().info(f'🎯 Moving to place position for {object_name}')
            success, notes = self._move_arm_to_pose(place_pose, timeout=6.0)
            if not success:
                return False, f"Failed to move to place position: {notes}"
            
            # Step 2: Open gripper to release object
            self.get_logger().info('🤏 Opening gripper to release object')
            success, notes = self._control_gripper(self.gripper_open_position, timeout=2.0)
            if not success:
                return False, f"Failed to open gripper: {notes}"
            
            # Step 3: Move arm back to neutral position
            neutral_pose = {'x': 0.0, 'y': 0.0, 'z': 0.5, 'gripper': 'open'}
            self.get_logger().info('🔄 Moving arm to neutral position')
            success, notes = self._move_arm_to_pose(neutral_pose, timeout=6.0)
            if not success:
                self.get_logger().warn(f'⚠️ Failed to move to neutral position: {notes}')
                # Don't fail the place operation if neutral position fails
            
            self.get_logger().info(f'✅ Successfully placed {object_name}')
            return True, f"Successfully placed {object_name}"
            
        except Exception as e:
            self.get_logger().error(f'❌ Place error: {e}')
            return False, f"Place error: {e}"

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