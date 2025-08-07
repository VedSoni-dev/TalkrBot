#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import time

class Nav2FinalTestNode(Node):
    def __init__(self):
        super().__init__('nav2_final_test_node')
        
        # Publisher to send test skill plans
        self.skill_publisher = self.create_publisher(String, '/skill_plan', 10)
        
        # Subscriber to listen for execution feedback
        self.feedback_subscription = self.create_subscription(
            String, '/execution_feedback', self.feedback_callback, 10
        )
        
        self.get_logger().info('🧪 Nav2 Final Test Node initialized')
        
        # Test skill plans for complete Nav2 integration
        self.test_plans = [
            # Simple navigation tests
            ["go_to('kitchen')"],
            ["go_to('closet')"],
            ["go_to('living_room')"],
            
            # Combined navigation and manipulation
            ["go_to('fridge')", "grasp('water')", "go_to('user')", "place('water')"],
            ["go_to('closet')", "grasp('blanket')", "go_to('couch')", "place('blanket')"],
            
            # Error handling tests
            ["go_to('unknown_location')"],  # Should fail gracefully
            ["go_to('kitchen')", "grasp('unknown_object')"],  # Should use default pose
            
            # Complex multi-step tasks
            ["go_to('fridge')", "grasp('apple')", "go_to('table')", "place('apple')", "go_to('user')"],
            ["go_to('desk')", "grasp('keys')", "go_to('user')", "place('keys')", "speak('Here are your keys')"]
        ]
        
        self.current_test = 0
        
        # Start testing after a delay
        self.timer = self.create_timer(3.0, self.run_test)
        
    def feedback_callback(self, msg):
        """Handle execution feedback"""
        self.get_logger().info(f'📥 [FEEDBACK] {msg.data}')
        
    def run_test(self):
        """Run comprehensive Nav2 tests"""
        if self.current_test >= len(self.test_plans):
            self.get_logger().info('🏁 All Nav2 integration tests completed')
            return
            
        test_plan = self.test_plans[self.current_test]
        self.get_logger().info(f'🧪 Nav2 Test {self.current_test + 1}: {test_plan}')
        
        # Send skill plan
        plan_msg = String()
        plan_msg.data = json.dumps(test_plan)
        self.skill_publisher.publish(plan_msg)
        
        self.current_test += 1
        
        # Schedule next test
        if self.current_test < len(self.test_plans):
            self.timer = self.create_timer(20.0, self.run_test)  # Longer delay for complex tasks

def main(args=None):
    rclpy.init(args=args)
    node = Nav2FinalTestNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main() 