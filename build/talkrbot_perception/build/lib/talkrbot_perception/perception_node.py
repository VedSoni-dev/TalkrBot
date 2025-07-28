import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from talkrbot_msgs.msg import DetectedObject
from cv_bridge import CvBridge
import cv2
import numpy as np
import torch
from ultralytics import YOLO
from geometry_msgs.msg import PoseStamped
from builtin_interfaces.msg import Time
import uuid
import json

class PerceptionNode(Node):
    def __init__(self):
        super().__init__('perception_node')
        self.bridge = CvBridge()
        self.rgb_image = None
        self.depth_image = None
        self.scene_memory = {}  # object_id -> latest pose
        self.model = YOLO('yolov8n.pt')
        self.rgb_sub = self.create_subscription(
            Image,
            '/camera/color/image_raw',
            self.rgb_callback,
            10
        )
        self.depth_sub = self.create_subscription(
            Image,
            '/camera/depth/image_raw',
            self.depth_callback,
            10
        )
        self.obj_pub = self.create_publisher(DetectedObject, '/detected_objects', 10)
        self.get_logger().info('PerceptionNode initialized and subscribed to camera topics.')

    def rgb_callback(self, msg):
        try:
            self.rgb_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            self.process()
        except Exception as e:
            self.get_logger().error(f'RGB image conversion failed: {e}')

    def depth_callback(self, msg):
        try:
            self.depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        except Exception as e:
            self.get_logger().error(f'Depth image conversion failed: {e}')

    def process(self):
        if self.rgb_image is None:
            return
        # Run YOLOv8 detection
        results = self.model(self.rgb_image)
        for det in results[0].boxes:
            class_id = int(det.cls[0])
            class_name = self.model.names[class_id]
            confidence = float(det.conf[0])
            bbox = det.xyxy[0].cpu().numpy().astype(int)
            bbox_x, bbox_y, bbox_x2, bbox_y2 = bbox
            bbox_width = bbox_x2 - bbox_x
            bbox_height = bbox_y2 - bbox_y
            # Estimate 3D pose using depth
            pose, depth_val = self.estimate_pose(bbox_x, bbox_y, bbox_width, bbox_height)
            # Generate unique object_id
            object_id = str(uuid.uuid4())
            # Scene memory update
            self.scene_memory[object_id] = pose
            # Prepare DetectedObject message
            msg = DetectedObject()
            msg.class_name = class_name
            msg.confidence = confidence
            msg.bbox_x = int(bbox_x)
            msg.bbox_y = int(bbox_y)
            msg.bbox_width = int(bbox_width)
            msg.bbox_height = int(bbox_height)
            msg.pose = pose
            msg.properties = json.dumps({"depth": float(depth_val)})
            msg.object_id = object_id
            msg.timestamp = self.get_clock().now().to_msg()
            self.obj_pub.publish(msg)
            self.get_logger().info(f"Detected: {class_name} ({confidence:.2f}) at {pose.pose.position}")

    def estimate_pose(self, x, y, w, h):
        # Default pose
        pose = PoseStamped()
        pose.header.frame_id = 'camera_link'
        pose.header.stamp = self.get_clock().now().to_msg()
        # If no depth image, return default
        if self.depth_image is None:
            return pose, 0.0
        # Get center of bbox
        cx = int(x + w / 2)
        cy = int(y + h / 2)
        try:
            depth_val = float(self.depth_image[cy, cx])
            if np.isnan(depth_val) or depth_val <= 0.01:
                raise ValueError('Invalid depth')
        except Exception:
            depth_val = 0.0
        # Simple pinhole camera model (replace with real intrinsics as needed)
        fx = fy = 525.0  # Focal length in pixels
        cx_cam = 319.5   # Principal point x
        cy_cam = 239.5   # Principal point y
        if depth_val > 0.0:
            z = depth_val
            x3d = (cx - cx_cam) * z / fx
            y3d = (cy - cy_cam) * z / fy
            pose.pose.position.x = float(x3d)
            pose.pose.position.y = float(y3d)
            pose.pose.position.z = float(z)
        else:
            pose.pose.position.x = 0.0
            pose.pose.position.y = 0.0
            pose.pose.position.z = 0.0
        return pose, depth_val

def main(args=None):
    rclpy.init(args=args)
    node = PerceptionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main() 