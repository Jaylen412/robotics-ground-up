"""The smallest useful ROS 2 node: drive forward slowly. Needs ROS 2.

    python3 forward_node.py
"""
import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class Forward(Node):
    def __init__(self):
        super().__init__("forward")
        self.pub = self.create_publisher(Twist, "/cmd_vel", 10)
        self.create_timer(0.1, self.tick)   # 10 Hz

    def tick(self):
        msg = Twist()
        msg.linear.x = 0.2                  # m/s
        self.pub.publish(msg)


def main():
    rclpy.init()
    rclpy.spin(Forward())


if __name__ == "__main__":
    main()
