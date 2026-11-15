"""Lesson 4: the logic inside a ROS 2 node.

Keep decision logic in plain functions like this one. You can test it on a
laptop with no robot and no ROS installed. obstacle_stop_node.py wraps it.

Run:  pytest tests/test_04_ros2.py
"""
import math


def safe_speed(distance_m, max_speed=0.5, stop_dist=0.3, slow_dist=1.0):
    """Forward speed in m/s given the nearest obstacle ahead.

    - At or inside stop_dist: 0.0
    - At or beyond slow_dist: max_speed
    - In between: scale linearly from 0.0 up to max_speed
    - If distance_m is NaN, return 0.0 (a bad reading is not a clear path)
    """
    if math.isnan(distance_m) or distance_m <= stop_dist:
        return 0.0
    if distance_m >= slow_dist:
        return max_speed
    return max_speed * (distance_m - stop_dist) / (slow_dist - stop_dist)
