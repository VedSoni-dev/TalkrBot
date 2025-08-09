import os
import time
import xml.etree.ElementTree as ET

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
from builtin_interfaces.msg import Time as TimeMsg
from talkrbot_msgs.msg import ExecutionFeedback


class BTExecutorNode(Node):
    def __init__(self):
        super().__init__('bt_executor_node')

        self.declare_parameter('bt_xml_path', os.path.join(
            os.path.dirname(os.path.dirname(__file__)), '..', 'bring_object.xml'))
        self.bt_xml_path = self.get_parameter('bt_xml_path').get_parameter_value().string_value

        qos = QoSProfile(depth=10)
        self.feedback_pub = self.create_publisher(ExecutionFeedback, '/execution_feedback', qos)

        self.get_logger().info(f'Loading Behavior Tree XML from: {self.bt_xml_path}')
        if not os.path.isabs(self.bt_xml_path):
            self.bt_xml_path = os.path.abspath(self.bt_xml_path)
        if not os.path.exists(self.bt_xml_path):
            self.get_logger().error(f'BT XML not found: {self.bt_xml_path}')
            return

        try:
            tree = ET.parse(self.bt_xml_path)
            self.root = tree.getroot()
        except Exception as e:
            self.get_logger().error(f'Failed to parse BT XML: {e}')
            return

        # Immediate execution after startup
        self.create_timer(0.5, self.execute_bt_once)
        self.executed_once = False

    def now_time(self) -> TimeMsg:
        now = self.get_clock().now().to_msg()
        return now

    def publish_feedback(self, step: str, status: str, notes: str):
        msg = ExecutionFeedback()
        msg.step = step
        msg.status = status
        msg.notes = notes
        msg.timestamp = self.now_time()
        self.feedback_pub.publish(msg)
        self.get_logger().info(f'[BT] {step} -> {status}: {notes}')

    def execute_bt_once(self):
        if self.executed_once:
            return
        self.executed_once = True

        main_tree_id = self.root.attrib.get('main_tree_to_execute', 'MainTree')
        bt = None
        for child in self.root:
            if child.tag == 'BehaviorTree' and child.attrib.get('ID') == main_tree_id:
                bt = child
                break
        if bt is None:
            self.get_logger().error(f'BehaviorTree ID {main_tree_id} not found')
            return

        # Iterate simple sequence of leaf nodes: go_to, grasp, place, etc.
        for node in bt:
            tag = node.tag
            attrs = {k: v for k, v in node.attrib.items()}
            step_desc = f"{tag}({', '.join([f"{k}='{v}'" for k, v in attrs.items()])})"

            try:
                ok, notes = self.execute_skill(tag, attrs)
                self.publish_feedback(step_desc, 'success' if ok else 'failure', notes)
                if not ok:
                    break
            except Exception as e:
                self.publish_feedback(step_desc, 'failure', f'Exception: {e}')
                break

    def execute_skill(self, tag: str, attrs: dict):
        # Placeholder implementations. Replace with ROS 2 action clients as needed.
        if tag == 'go_to':
            location = attrs.get('location', '')
            time.sleep(0.5)
            return True, f"Navigated to {location} (mock)"
        if tag == 'grasp':
            obj = attrs.get('object', '')
            time.sleep(0.5)
            return True, f"Grasped {obj} (mock)"
        if tag == 'place':
            obj = attrs.get('object', '')
            time.sleep(0.5)
            return True, f"Placed {obj} (mock)"
        if tag == 'wait':
            dur = float(attrs.get('seconds', '1'))
            time.sleep(dur)
            return True, f"Waited {dur} seconds (mock)"
        if tag == 'speak':
            text = attrs.get('text', '')
            time.sleep(0.1)
            return True, f"Spoke: {text} (mock)"
        return False, f"Unknown skill '{tag}'"


def main(args=None):
    rclpy.init(args=args)
    node = BTExecutorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            rclpy.shutdown() 