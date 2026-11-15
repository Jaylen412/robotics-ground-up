"""Lesson 2: write a PID controller.

Fill in PID.update, then run:  pytest tests/test_02_control.py
Afterwards, run this file to print a step response:  python lessons/02_control/pid.py
"""


def clamp(value, low, high):
    return max(low, min(high, value))


class PID:
    def __init__(self, kp, ki=0.0, kd=0.0, out_limit=30.0, i_limit=3.0):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.out_limit = out_limit   # output is clamped to +/- this
        self.i_limit = i_limit       # integral is clamped to +/- this (anti-windup)
        self.integral = 0.0
        self.last_error = None       # None until the first update

    def update(self, target, measured, dt):
        """Return the control output for one time step.

        1. error = target - measured
        2. Add error * dt to self.integral, then clamp it to +/- i_limit
        3. derivative = change in error / dt (use 0.0 on the first call)
        4. Remember the error in self.last_error
        5. Return kp*error + ki*integral + kd*derivative, clamped to +/- out_limit
        """
        error = target - measured
        self.integral = clamp(self.integral + error * dt, -self.i_limit, self.i_limit)
        derivative = 0.0 if self.last_error is None else (error - self.last_error) / dt
        self.last_error = error
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        return clamp(output, -self.out_limit, self.out_limit)


def simulate(pid, target=1.0, load=0.0, seconds=6.0, dt=0.002):
    """Provided for you. The same motor model the site's PID tuner uses.

    Returns the list of positions over time.
    """
    x, v, history = 0.0, 0.0, []
    for _ in range(int(seconds / dt)):
        u = pid.update(target, x, dt)
        a = u + load - 1.5 * v
        v += a * dt
        x += v * dt
        history.append(x)
    return history


if __name__ == "__main__":
    xs = simulate(PID(kp=12, ki=0, kd=1))
    print("peak %.3f  final %.3f" % (max(xs), xs[-1]))
