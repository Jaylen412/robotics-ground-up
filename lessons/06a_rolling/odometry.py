"""Lesson 6A: wheel odometry.

Run:  pytest tests/test_06a_rolling.py
"""
import math


def ticks_to_distance(ticks, ticks_per_rev, gear_ratio, wheel_diameter_m):
    """Meters a wheel rolled for a number of encoder ticks.

    ticks_per_rev is per motor turn. gear_ratio is motor turns per wheel turn.
    """
    # TODO: your code here
    raise NotImplementedError("fill me in")


def update_pose(pose, d_left, d_right, wheelbase_m):
    """Return the new (x, y, theta) after each wheel rolled d_left and d_right meters.

    distance = average of the two wheels
    d_theta  = (d_right - d_left) / wheelbase_m
    Move `distance` along the heading theta + d_theta / 2 (the midpoint heading),
    then add d_theta to theta.
    """
    # TODO: your code here
    raise NotImplementedError("fill me in")
