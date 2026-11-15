"""Lesson 1: PWM, servos and batteries.

Fill in each function, then run:  pytest tests/test_01_fundamentals.py
"""


def duty_to_voltage(duty_pct, supply_v):
    """Average voltage a motor sees at a given PWM duty cycle.

    duty_pct is 0 to 100. Values outside that range are clamped.
    Example: 25% of a 12 V supply is 3.0 V.
    """
    # TODO: your code here
    raise NotImplementedError("fill me in")


def servo_pulse_ms(angle_deg):
    """Pulse width in milliseconds for a hobby servo angle.

    0 degrees is 1.0 ms, 180 degrees is 2.0 ms, linear in between.
    Angles outside 0 to 180 are clamped.
    """
    # TODO: your code here
    raise NotImplementedError("fill me in")


def battery_runtime_min(capacity_ah, current_a):
    """Minutes a battery lasts at a constant current draw.

    A 5 Ah pack at 20 A lasts 15 minutes.
    Raise ValueError if current_a is zero or negative.
    """
    # TODO: your code here
    raise NotImplementedError("fill me in")
