import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from talkrbot_msgs.msg import AACInput
import threading
import asyncio
import websockets
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from datetime import datetime
from rclpy.time import Time

class AACNode(Node):
    def __init__(self):
        super().__init__('aac_node')
        # ROS publisher and subscriber
        self.aac_pub = self.create_publisher(AACInput, '/aac_input', 10)
        self.text_sub = self.create_subscription(
            String,
            '/aac_text_input',
            self.ros_text_callback,
            10
        )
        # User profiles: user_id -> set of common phrases
        self.user_profiles = {}
        # Start WebSocket and HTTP servers in threads
        self.ws_thread = threading.Thread(target=self.start_websocket_server, daemon=True)
        self.ws_thread.start()
        self.http_thread = threading.Thread(target=self.start_http_server, daemon=True)
        self.http_thread.start()
        self.get_logger().info('AACNode initialized with WebSocket (8765) and HTTP (8080) servers.')

    def normalize_input(self, text):
        return text.strip().lower()

    def update_user_profile(self, user_id, text):
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = set()
        self.user_profiles[user_id].add(text)

    def log_input(self, source, text, user_id):
        self.get_logger().info(f"Received input from {source}: user_id={user_id}, text='{text}'")

    def publish_aac_input(self, text, user_id, input_method, confidence=1.0, metadata=""):
        msg = AACInput()
        msg.text = text
        msg.user_id = user_id
        msg.timestamp = self.get_clock().now().to_msg()
        msg.input_method = input_method
        msg.confidence = float(confidence)
        msg.metadata = metadata
        self.aac_pub.publish(msg)
        self.update_user_profile(user_id, text)
        self.log_input(input_method, text, user_id)

    # --- ROS topic callback ---
    def ros_text_callback(self, msg):
        text = self.normalize_input(msg.data)
        user_id = "ros_user"
        self.publish_aac_input(text, user_id, "ros_topic")

    # --- WebSocket server ---
    async def ws_handler(self, websocket):
        async for message in websocket:
            try:
                data = json.loads(message)
                text = self.normalize_input(data.get('text', ''))
                user_id = data.get('user_id', 'unknown')
                metadata = data.get('metadata', '')
                confidence = float(data.get('confidence', 1.0))
                self.publish_aac_input(text, user_id, "websocket", confidence, metadata)
                await websocket.send(json.dumps({'status': 'ok'}))
            except Exception as e:
                await websocket.send(json.dumps({'status': 'error', 'reason': str(e)}))

    def start_websocket_server(self):
        import asyncio
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async def ws_main():
            async with websockets.serve(self.ws_handler, '0.0.0.0', 8765):
                print("WebSocket server running on port 8765")
                await asyncio.Future()  # Run forever

        try:
            loop.run_until_complete(ws_main())
        except Exception as e:
            self.get_logger().error(f"WebSocket server failed: {str(e)}")
        finally:
            loop.close()

    # --- HTTP REST API server ---
    class AACHTTPRequestHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            if self.path != '/aac_input':
                self.send_response(404)
                self.end_headers()
                return
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            try:
                data = json.loads(body)
                text = self.server.node.normalize_input(data.get('text', ''))
                user_id = data.get('user_id', 'unknown')
                metadata = data.get('metadata', '')
                confidence = float(data.get('confidence', 1.0))
                self.server.node.publish_aac_input(text, user_id, "http", confidence, metadata)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'ok'}).encode())
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'error', 'reason': str(e)}).encode())

    class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
        def __init__(self, server_address, RequestHandlerClass, node):
            super().__init__(server_address, RequestHandlerClass)
            self.node = node

    def start_http_server(self):
        server = self.ThreadedHTTPServer(('0.0.0.0', 8080), self.AACHTTPRequestHandler, self)
        server.serve_forever()

def main(args=None):
    rclpy.init(args=args)
    node = AACNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():  # Only shutdown if still running
            rclpy.shutdown()

if __name__ == '__main__':
    main() 