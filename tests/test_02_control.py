import pytest
from pid import PID, simulate


def test_proportional_only():
    assert PID(kp=2).update(1.0, 0.0, 0.01) == pytest.approx(2.0)


def test_output_is_clamped():
    assert PID(kp=100).update(1.0, 0.0, 0.01) == pytest.approx(30.0)
    assert PID(kp=100).update(-1.0, 0.0, 0.01) == pytest.approx(-30.0)


def test_integral_accumulates():
    pid = PID(kp=0, ki=1)
    assert pid.update(1.0, 0.0, 0.5) == pytest.approx(0.5)
    assert pid.update(1.0, 0.0, 0.5) == pytest.approx(1.0)


def test_integral_is_limited():
    pid = PID(kp=0, ki=1, i_limit=3.0)
    for _ in range(100):
        out = pid.update(1.0, 0.0, 1.0)
    assert out == pytest.approx(3.0)


def test_derivative():
    pid = PID(kp=0, kd=1)
    assert pid.update(1.0, 0.0, 0.1) == pytest.approx(0.0)   # first call: no history
    assert pid.update(1.0, 0.5, 0.1) == pytest.approx(-5.0)  # error fell from 1.0 to 0.5


def test_step_response_settles():
    xs = simulate(PID(kp=12, ki=0, kd=1))
    assert abs(1.0 - xs[-1]) < 0.02


def test_load_leaves_error_without_integral():
    xs = simulate(PID(kp=12, ki=0, kd=1), load=-4.0)
    assert 1.0 - xs[-1] > 0.2


def test_integral_removes_load_error():
    xs = simulate(PID(kp=12, ki=8, kd=2), load=-4.0)
    assert abs(1.0 - xs[-1]) < 0.02
