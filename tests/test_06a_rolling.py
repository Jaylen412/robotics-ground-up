import math

import pytest
from odometry import ticks_to_distance, update_pose


def test_one_wheel_turn():
    # 48 ticks per motor turn, 34:1 gearbox -> 1632 ticks per wheel turn
    d = ticks_to_distance(1632, 48, 34, 0.065)
    assert d == pytest.approx(math.pi * 0.065)


def test_straight():
    x, y, th = update_pose((0, 0, 0), 0.5, 0.5, 0.3)
    assert (x, y, th) == pytest.approx((0.5, 0.0, 0.0))


def test_spin_in_place():
    x, y, th = update_pose((1, 2, 0), -0.1, 0.1, 0.2)
    assert (x, y) == pytest.approx((1, 2))
    assert th == pytest.approx(1.0)


def test_many_small_steps_trace_a_circle():
    pose = (0.0, 0.0, 0.0)
    steps = 1000
    # right wheel travels further: a left-hand circle of radius 1 m at the center
    for _ in range(steps):
        pose = update_pose(pose, 2 * math.pi * 0.85 / steps, 2 * math.pi * 1.15 / steps, 0.3)
    assert abs(pose[0]) < 0.01 and abs(pose[1]) < 0.01
    assert pose[2] == pytest.approx(2 * math.pi)
