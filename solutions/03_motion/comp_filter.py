"""Lesson 3b: complementary filter.

Run:  pytest tests/test_03_motion.py
"""


def fuse(angle, gyro_rate, accel_angle, dt, alpha=0.96):
    """One filter step. Return the new angle estimate.

    Trust the gyro for the short term: angle + gyro_rate * dt, weighted by alpha.
    Trust the accelerometer for the long term: accel_angle, weighted by 1 - alpha.
    """
    return alpha * (angle + gyro_rate * dt) + (1.0 - alpha) * accel_angle


def run_filter(gyro_rates, accel_angles, dt, alpha=0.96):
    """Provided for you. Run fuse over two equal-length lists of readings."""
    angle, out = 0.0, []
    for rate, acc in zip(gyro_rates, accel_angles):
        angle = fuse(angle, rate, acc, dt, alpha)
        out.append(angle)
    return out
