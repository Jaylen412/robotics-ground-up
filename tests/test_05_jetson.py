import pytest
from budget import (blind_distance_m, max_fps, memory_headroom_gb,
                    parse_tegrastats, total_latency_ms)

STAGES = {"capture": 15, "preprocess": 6, "inference": 22, "postprocess": 5}


def test_total_latency():
    assert total_latency_ms(STAGES) == 48


def test_max_fps():
    assert max_fps(50) == pytest.approx(20.0)


def test_blind_distance():
    assert blind_distance_m(1.0, 48) == pytest.approx(0.048)
    assert blind_distance_m(8.0, 48) == pytest.approx(0.384)


def test_memory_headroom():
    parts = {"linux": 1.6, "ros2": 0.8, "models": 2.0, "buffers": 0.6}
    assert memory_headroom_gb(parts) == pytest.approx(3.0)
    assert memory_headroom_gb({"models": 9.0}) < 0


def test_parse_tegrastats():
    line = "RAM 2448/7620MB (lfb 4x4MB) SWAP 0/3810MB CPU [5%@729] GR3D_FREQ 45% VDD_IN 6120mW/5890mW"
    assert parse_tegrastats(line) == {"ram_used_mb": 2448, "ram_total_mb": 7620, "gpu_pct": 45}
