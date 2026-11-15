import math

import pytest
from flight import hover_time_min, thrust_to_weight, velocity_setpoint


def test_thrust_to_weight():
    assert thrust_to_weight(900, 1500) == pytest.approx(2.4)
    assert thrust_to_weight(500, 1500, motors=6) == pytest.approx(2.0)


def test_hover_time_without_payload():
    # 5 Ah * 4S * 3.7 V * 0.8 = 59.2 Wh; 1500 g / 7.5 g/W = 200 W
    assert hover_time_min(1500, 4, 5000, 7.5) == pytest.approx(17.76)


def test_payload_power_costs_flight_time():
    without = hover_time_min(1500, 4, 5000, 7.5)
    with_jetson = hover_time_min(1500, 4, 5000, 7.5, payload_w=20)
    assert with_jetson == pytest.approx(59.2 / 220 * 60)
    assert with_jetson < without


def test_setpoint_near_target_is_proportional():
    assert velocity_setpoint((1, 0, 0), (0.5, 0, 0), max_speed=2.0) == pytest.approx((0.5, 0, 0))


def test_setpoint_far_target_is_capped():
    v = velocity_setpoint((30, 40, 0), (0, 0, 0), max_speed=5.0)
    assert math.sqrt(sum(c * c for c in v)) == pytest.approx(5.0)
    assert v == pytest.approx((3.0, 4.0, 0.0))   # direction kept
