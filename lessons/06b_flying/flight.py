"""Lesson 6B: power budget and an offboard velocity command.

Run:  pytest tests/test_06b_flying.py
"""
import math


def thrust_to_weight(max_thrust_per_motor_g, weight_g, motors=4):
    """Total maximum thrust divided by takeoff weight. Aim for 2.0 or more."""
    # TODO: your code here
    raise NotImplementedError("fill me in")


def hover_time_min(weight_g, cells, capacity_mah, efficiency_g_per_w,
                   payload_w=0.0, usable=0.8):
    """Estimated hover time in minutes.

    battery energy (Wh) = capacity_mah / 1000 * cells * 3.7 * usable
    hover power (W)     = weight_g / efficiency_g_per_w
    time                = energy / (hover power + payload_w), converted to minutes
    """
    # TODO: your code here
    raise NotImplementedError("fill me in")


def velocity_setpoint(target, position, max_speed, gain=1.0):
    """Velocity command (vx, vy, vz) that moves the drone toward a target point.

    This is what a companion computer sends in offboard mode.
    velocity = gain * (target - position), per axis.
    If its length exceeds max_speed, scale the whole vector down to max_speed
    so the direction is kept.
    """
    # TODO: your code here
    raise NotImplementedError("fill me in")
