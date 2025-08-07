#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import time

class ArmTestNode(Node):
    def __init__(self):
        super().__init__('arm_test_node')
        
        # Publisher to send test skill plans
        self.skill_publisher = self.create_publisher(String, '/skill_plan', 10)
        
        # Subscriber to listen for execution feedback
        self.feedback_subscription = self.create_subscription(
            String, '/execution_feedback', self.feedback_callback, 10
        )
        
        self.get_logger().info('🧪 Arm Test Node initialized')
        
        # Test skill plans for arm control
        self.test_plans = [
            ["grasp('water')"],
            ["grasp('blanket')", "place('blanket')"],
            ["grasp('keys')", "go_to('user')", "place('keys')"],
            ["grasp('phone')", "go_to('table')", "place('phone')"],
            ["grasp('unknown_object')"]  # This should use default pose
        ]
        
        self.current_test = 0
        
        # Start testing after a delay
        self.timer = self.create_timer(3.0, self.run_test)
        
    def feedback_callback(self, msg):
        """Handle execution feedback"""
        self.get_logger().info(f'📥 [FEEDBACK] {msg.data}')
        
    def run_test(self):
        """Run arm control tests"""
        if self.current_test >= len(self.test_plans):
            self.get_logger().info('🏁 All arm tests completed')
            return
            
        test_plan = self.test_plans[self.current_test]
        self.get_logger().info(f'🧪 Arm Test {self.current_test + 1}: {test_plan}')
        
        # Send skill plan
        plan_msg = String()
        plan_msg.data = json.dumps(test_plan)
        self.skill_publisher.publish(plan_msg)
        
        self.current_test += 1
        
        # Schedule next test
        if self.current_test < len(self.test_plans):
            self.timer = self.create_timer(15.0, self.run_test)  # Longer delay for arm movements

def main(args=None):
    rclpy.init(args=args)
    node = ArmTestNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main() 