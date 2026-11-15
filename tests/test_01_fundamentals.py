import pytest
from pwm import battery_runtime_min, duty_to_voltage, servo_pulse_ms


def test_duty_to_voltage():
    assert duty_to_voltage(25, 12) == pytest.approx(3.0)
    assert duty_to_voltage(100, 12) == pytest.approx(12.0)


def test_duty_is_clamped():
    assert duty_to_voltage(150, 12) == pytest.approx(12.0)
    assert duty_to_voltage(-10, 12) == pytest.approx(0.0)


def test_servo_pulse():
    assert servo_pulse_ms(0) == pytest.approx(1.0)
    assert servo_pulse_ms(90) == pytest.approx(1.5)
    assert servo_pulse_ms(180) == pytest.approx(2.0)
    assert servo_pulse_ms(400) == pytest.approx(2.0)


def test_battery_runtime():
    assert battery_runtime_min(5, 20) == pytest.approx(15.0)
    with pytest.raises(ValueError):
        battery_runtime_min(5, 0)
