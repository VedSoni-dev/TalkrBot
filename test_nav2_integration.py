#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import time

class Nav2TestNode(Node):
    def __init__(self):
        super().__init__('nav2_test_node')
        
        # Publisher to send test skill plans
        self.skill_publisher = self.create_publisher(String, '/skill_plan', 10)
        
        # Subscriber to listen for execution feedback
        self.feedback_subscription = self.create_subscription(
            String, '/execution_feedback', self.feedback_callback, 10
        )
        
        self.get_logger().info('🧪 Nav2 Test Node initialized')
        
        # Test skill plans
        self.test_plans = [
            ["go_to('kitchen')"],
            ["go_to('closet')", "wait(2)", "go_to('user')"],
            ["go_to('fridge')", "go_to('table')"],
            ["go_to('unknown_location')"]  # This should fail
        ]
        
        self.current_test = 0
        
        # Start testing after a delay
        self.timer = self.create_timer(3.0, self.run_test)
        
    def feedback_callback(self, msg):
        """Handle execution feedback"""
        self.get_logger().info(f'📥 [FEEDBACK] {msg.data}')
        
    def run_test(self):
        """Run navigation tests"""
        if self.current_test >= len(self.test_plans):
            self.get_logger().info('🏁 All tests completed')
            return
            
        test_plan = self.test_plans[self.current_test]
        self.get_logger().info(f'🧪 Test {self.current_test + 1}: {test_plan}')
        
        # Send skill plan
        plan_msg = String()
        plan_msg.data = json.dumps(test_plan)
        self.skill_publisher.publish(plan_msg)
        
        self.current_test += 1
        
        # Schedule next test
        if self.current_test < len(self.test_plans):
            self.timer = self.create_timer(10.0, self.run_test)

def main(args=None):
    rclpy.init(args=args)
    node = Nav2TestNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main() 