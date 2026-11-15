import math

import pytest
from comp_filter import fuse, run_filter
from diff_drive import body_velocity, drive, step_pose


def test_straight_line():
    v, w = body_velocity(0.5, 0.5, 0.3)
    assert v == pytest.approx(0.5) and w == pytest.approx(0.0)


def test_spin_in_place():
    v, w = body_velocity(-0.3, 0.3, 0.3)
    assert v == pytest.approx(0.0) and w == pytest.approx(2.0)


def test_step_pose_forward():
    x, y, th = step_pose(0, 0, math.pi / 2, 1.0, 0.0, 0.1)
    assert x == pytest.approx(0.0, abs=1e-9) and y == pytest.approx(0.1) and th == pytest.approx(math.pi / 2)


def test_drive_straight_six_meters():
    x, y, th = drive(1.0, 1.0)
    assert x == pytest.approx(6.0, abs=1e-6) and y == pytest.approx(0.0, abs=1e-6)


def test_full_circle_returns_to_start():
    # w = 0.3 / 0.3 = 1 rad/s, so one full circle takes 2*pi seconds
    x, y, th = drive(0.35, 0.65, wheelbase=0.3, seconds=2 * math.pi)
    assert abs(x) < 0.01 and abs(y) < 0.01


def test_fuse_weights():
    assert fuse(10.0, 0.0, 0.0, 0.01, alpha=1.0) == pytest.approx(10.0)   # gyro only
    assert fuse(10.0, 0.0, 0.0, 0.01, alpha=0.0) == pytest.approx(0.0)    # accel only
    assert fuse(0.0, 100.0, 0.0, 0.01, alpha=0.5) == pytest.approx(0.5)


def test_filter_beats_drifting_gyro():
    dt, n = 0.02, 1000
    gyro = [2.0] * n       # the robot is still; this is pure bias, deg/s
    accel = [0.0] * n      # true angle is 0
    gyro_only = sum(g * dt for g in gyro)
    fused = run_filter(gyro, accel, dt, alpha=0.96)[-1]
    assert abs(gyro_only) > 30
    assert abs(fused) < 2
