"""Lesson 3a: differential drive kinematics.

Run:  pytest tests/test_03_motion.py
"""
import math


def body_velocity(v_left, v_right, wheelbase):
    """Return (v, w): forward speed in m/s and turn rate in rad/s."""
    return (v_right + v_left) / 2.0, (v_right - v_left) / wheelbase


def step_pose(x, y, theta, v, w, dt):
    """Advance the pose by one small time step and return (x, y, theta).

    Move along the current heading, then update the heading.
    """
    x += v * math.cos(theta) * dt
    y += v * math.sin(theta) * dt
    theta += w * dt
    return x, y, theta


def drive(v_left, v_right, wheelbase=0.3, seconds=6.0, dt=0.001):
    """Provided for you. Final pose after driving at constant wheel speeds."""
    v, w = body_velocity(v_left, v_right, wheelbase)
    x = y = theta = 0.0
    for _ in range(int(round(seconds / dt))):
        x, y, theta = step_pose(x, y, theta, v, w, dt)
    return x, y, theta
