import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloPublisher(Node):
    def __init__(self):
        super().__init__('hello_publisher')
        self.pub = self.create_publisher(String, 'hello_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World!'
        self.pub.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main():
    rclpy.init()
    node = HelloPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
