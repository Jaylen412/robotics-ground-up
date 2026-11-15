"""Lesson 6A: wheel odometry.

Run:  pytest tests/test_06a_rolling.py
"""
import math


def ticks_to_distance(ticks, ticks_per_rev, gear_ratio, wheel_diameter_m):
    """Meters a wheel rolled for a number of encoder ticks.

    ticks_per_rev is per motor turn. gear_ratio is motor turns per wheel turn.
    """
    wheel_turns = ticks / (ticks_per_rev * gear_ratio)
    return wheel_turns * math.pi * wheel_diameter_m


def update_pose(pose, d_left, d_right, wheelbase_m):
    """Return the new (x, y, theta) after each wheel rolled d_left and d_right meters.

    distance = average of the two wheels
    d_theta  = (d_right - d_left) / wheelbase_m
    Move `distance` along the heading theta + d_theta / 2 (the midpoint heading),
    then add d_theta to theta.
    """
    x, y, theta = pose
    distance = (d_left + d_right) / 2.0
    d_theta = (d_right - d_left) / wheelbase_m
    x += distance * math.cos(theta + d_theta / 2.0)
    y += distance * math.sin(theta + d_theta / 2.0)
    return x, y, theta + d_theta
