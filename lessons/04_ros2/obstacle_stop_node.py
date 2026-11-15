"""A ROS 2 node that slows and stops for obstacles. Needs ROS 2 (Humble or Jazzy).

Run on the robot or in simulation, from this folder:
    python3 obstacle_stop_node.py

It listens to a lidar on /scan and publishes velocity commands on /cmd_vel.
The decision itself lives in safety.py, which you wrote and tested.
"""
import math

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

from safety import safe_speed


class ObstacleStop(Node):
    def __init__(self):
        super().__init__("obstacle_stop")
        self.pub = self.create_publisher(Twist, "/cmd_vel", 10)
        self.create_subscription(LaserScan, "/scan", self.on_scan, 10)

    def on_scan(self, scan):
        ranges = list(scan.ranges)
        k = max(1, len(ranges) // 12)
        # Assumes index 0 points straight ahead, as on most 360 degree lidars.
        front = ranges[:k] + ranges[-k:]
        valid = [r for r in front if math.isfinite(r) and r > scan.range_min]
        nearest = min(valid) if valid else float("inf")

        msg = Twist()
        msg.linear.x = safe_speed(nearest)
        self.pub.publish(msg)


def main():
    rclpy.init()
    rclpy.spin(ObstacleStop())


if __name__ == "__main__":
    main()
