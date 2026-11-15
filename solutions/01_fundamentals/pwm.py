"""Lesson 1: PWM, servos and batteries.

Fill in each function, then run:  pytest tests/test_01_fundamentals.py
"""


def duty_to_voltage(duty_pct, supply_v):
    """Average voltage a motor sees at a given PWM duty cycle.

    duty_pct is 0 to 100. Values outside that range are clamped.
    Example: 25% of a 12 V supply is 3.0 V.
    """
    duty = min(100.0, max(0.0, duty_pct))
    return supply_v * duty / 100.0


def servo_pulse_ms(angle_deg):
    """Pulse width in milliseconds for a hobby servo angle.

    0 degrees is 1.0 ms, 180 degrees is 2.0 ms, linear in between.
    Angles outside 0 to 180 are clamped.
    """
    angle = min(180.0, max(0.0, angle_deg))
    return 1.0 + angle / 180.0


def battery_runtime_min(capacity_ah, current_a):
    """Minutes a battery lasts at a constant current draw.

    A 5 Ah pack at 20 A lasts 15 minutes.
    Raise ValueError if current_a is zero or negative.
    """
    if current_a <= 0:
        raise ValueError("current must be positive")
    return capacity_ah / current_a * 60.0
