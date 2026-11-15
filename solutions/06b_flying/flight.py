"""Lesson 6B: power budget and an offboard velocity command.

Run:  pytest tests/test_06b_flying.py
"""
import math


def thrust_to_weight(max_thrust_per_motor_g, weight_g, motors=4):
    """Total maximum thrust divided by takeoff weight. Aim for 2.0 or more."""
    return motors * max_thrust_per_motor_g / weight_g


def hover_time_min(weight_g, cells, capacity_mah, efficiency_g_per_w,
                   payload_w=0.0, usable=0.8):
    """Estimated hover time in minutes.

    battery energy (Wh) = capacity_mah / 1000 * cells * 3.7 * usable
    hover power (W)     = weight_g / efficiency_g_per_w
    time                = energy / (hover power + payload_w), converted to minutes
    """
    energy_wh = capacity_mah / 1000.0 * cells * 3.7 * usable
    power_w = weight_g / efficiency_g_per_w + payload_w
    return energy_wh / power_w * 60.0


def velocity_setpoint(target, position, max_speed, gain=1.0):
    """Velocity command (vx, vy, vz) that moves the drone toward a target point.

    This is what a companion computer sends in offboard mode.
    velocity = gain * (target - position), per axis.
    If its length exceeds max_speed, scale the whole vector down to max_speed
    so the direction is kept.
    """
    v = [gain * (t - p) for t, p in zip(target, position)]
    speed = math.sqrt(sum(c * c for c in v))
    if speed > max_speed:
        v = [c * max_speed / speed for c in v]
    return tuple(v)
