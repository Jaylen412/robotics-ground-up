import pytest
from safety import safe_speed


def test_clear_path_is_full_speed():
    assert safe_speed(5.0) == pytest.approx(0.5)
    assert safe_speed(float("inf")) == pytest.approx(0.5)


def test_stops_when_close():
    assert safe_speed(0.3) == 0.0
    assert safe_speed(0.05) == 0.0


def test_slows_in_between():
    assert safe_speed(0.65) == pytest.approx(0.25)


def test_bad_reading_stops():
    assert safe_speed(float("nan")) == 0.0


def test_custom_limits():
    assert safe_speed(1.0, max_speed=2.0, stop_dist=0.5, slow_dist=1.5) == pytest.approx(1.0)
