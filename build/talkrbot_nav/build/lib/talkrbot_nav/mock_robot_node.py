#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseWithCovarianceStamped, TransformStamped
from sensor_msgs.msg import JointState
from nav_msgs.msg import Odometry
from std_msgs.msg import Header
import tf2_ros
import math
import time

class MockRobotNode(Node):
    def __init__(self):
        super().__init__('mock_robot_node')
        
        # Publishers
        self.odom_pub = self.create_publisher(Odometry, '/odom', 10)
        self.joint_states_pub = self.create_publisher(JointState, '/joint_states', 10)
        self.pose_pub = self.create_publisher(PoseWithCovarianceStamped, '/amcl_pose', 10)
        
        # Subscribers
        self.cmd_vel_sub = self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)
        
        # TF broadcaster
        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)
        
        # Robot state
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.linear_vel = 0.0
        self.angular_vel = 0.0
        
        # Joint states (simulating a simple robot)
        self.joint_positions = {
            'left_wheel_joint': 0.0,
            'right_wheel_joint': 0.0,
            'base_link_joint': 0.0
        }
        
        # Timer for publishing
        self.timer = self.create_timer(0.1, self.publish_robot_state)  # 10Hz
        
        self.get_logger().info('🤖 Mock Robot Node initialized')
        self.get_logger().info('📡 Publishing: /odom, /joint_states, /amcl_pose')
        self.get_logger().info('📥 Subscribing: /cmd_vel')
        self.get_logger().info('🔗 TF: base_link -> odom')
        
    def cmd_vel_callback(self, msg):
        """Handle velocity commands"""
        self.linear_vel = msg.linear.x
        self.angular_vel = msg.angular.z
        
        # Log received commands
        if abs(self.linear_vel) > 0.01 or abs(self.angular_vel) > 0.01:
            self.get_logger().info(f'🎮 CMD_VEL: linear={self.linear_vel:.2f}, angular={self.angular_vel:.2f}')
    
    def publish_robot_state(self):
        """Update and publish robot state"""
        # Update position based on velocity
        dt = 0.1  # 10Hz timer
        self.x += self.linear_vel * math.cos(self.theta) * dt
        self.y += self.linear_vel * math.sin(self.theta) * dt
        self.theta += self.angular_vel * dt
        
        # Normalize angle
        self.theta = math.atan2(math.sin(self.theta), math.cos(self.theta))
        
        # Update joint positions
        wheel_radius = 0.1  # 10cm wheel radius
        self.joint_positions['left_wheel_joint'] += (self.linear_vel - self.angular_vel * 0.2) / wheel_radius * dt
        self.joint_positions['right_wheel_joint'] += (self.linear_vel + self.angular_vel * 0.2) / wheel_radius * dt
        self.joint_positions['base_link_joint'] = self.theta
        
        # Publish odometry
        self.publish_odometry()
        
        # Publish joint states
        self.publish_joint_states()
        
        # Publish pose
        self.publish_pose()
        
        # Publish TF
        self.publish_tf()
    
    def publish_odometry(self):
        """Publish odometry message"""
        msg = Odometry()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'odom'
        msg.child_frame_id = 'base_link'
        
        # Position
        msg.pose.pose.position.x = self.x
        msg.pose.pose.position.y = self.y
        msg.pose.pose.position.z = 0.0
        
        # Orientation (quaternion from yaw)
        msg.pose.pose.orientation.x = 0.0
        msg.pose.pose.orientation.y = 0.0
        msg.pose.pose.orientation.z = math.sin(self.theta / 2.0)
        msg.pose.pose.orientation.w = math.cos(self.theta / 2.0)
        
        # Velocity
        msg.twist.twist.linear.x = self.linear_vel
        msg.twist.twist.linear.y = 0.0
        msg.twist.twist.linear.z = 0.0
        msg.twist.twist.angular.x = 0.0
        msg.twist.twist.angular.y = 0.0
        msg.twist.twist.angular.z = self.angular_vel
        
        # Covariance (simplified)
        msg.pose.covariance = [0.1] * 36
        msg.twist.covariance = [0.1] * 36
        
        self.odom_pub.publish(msg)
    
    def publish_joint_states(self):
        """Publish joint states"""
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = list(self.joint_positions.keys())
        msg.position = list(self.joint_positions.values())
        msg.velocity = [0.0] * len(self.joint_positions)
        msg.effort = [0.0] * len(self.joint_positions)
        
        self.joint_states_pub.publish(msg)
    
    def publish_pose(self):
        """Publish pose estimate"""
        msg = PoseWithCovarianceStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'map'
        
        msg.pose.pose.position.x = self.x
        msg.pose.pose.position.y = self.y
        msg.pose.pose.position.z = 0.0
        
        msg.pose.pose.orientation.x = 0.0
        msg.pose.pose.orientation.y = 0.0
        msg.pose.pose.orientation.z = math.sin(self.theta / 2.0)
        msg.pose.pose.orientation.w = math.cos(self.theta / 2.0)
        
        # Covariance
        msg.pose.covariance = [0.1] * 36
        
        self.pose_pub.publish(msg)
    
    def publish_tf(self):
        """Publish transform from odom to base_link"""
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'
        
        t.transform.translation.x = self.x
        t.transform.translation.y = self.y
        t.transform.translation.z = 0.0
        
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = math.sin(self.theta / 2.0)
        t.transform.rotation.w = math.cos(self.theta / 2.0)
        
        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = MockRobotNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main() 