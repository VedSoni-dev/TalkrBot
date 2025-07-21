import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AACNode(Node):
    def __init__(self):
        super().__init__('aac_node')
        self.subscription = self.create_subscription(
            String,
            '/aac_input',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Received AAC Input: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = AACNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main() 