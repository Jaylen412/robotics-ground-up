"""Lesson 5: memory and latency budgets for the Orin Nano.

Run:  pytest tests/test_05_jetson.py
"""
import re


def total_latency_ms(stages):
    """Sum a dict of stage name -> milliseconds."""
    # TODO: your code here
    raise NotImplementedError("fill me in")


def max_fps(latency_ms):
    """Highest frame rate a pipeline with this total latency can sustain."""
    # TODO: your code here
    raise NotImplementedError("fill me in")


def blind_distance_m(speed_m_s, latency_ms):
    """Distance the robot covers while one frame is being processed."""
    # TODO: your code here
    raise NotImplementedError("fill me in")


def memory_headroom_gb(parts, total_gb=8.0):
    """Free memory left after a dict of component name -> GB. May be negative."""
    # TODO: your code here
    raise NotImplementedError("fill me in")


def parse_tegrastats(line):
    """Pull RAM and GPU load out of one line of tegrastats output.

    Example line (yours will have more fields):
      "RAM 2448/7620MB (lfb 4x4MB) SWAP 0/3810MB CPU [5%@729] GR3D_FREQ 45% VDD_IN 6120mW/5890mW"

    Return {"ram_used_mb": 2448, "ram_total_mb": 7620, "gpu_pct": 45}.
    Hint: re.search(r"RAM (\\d+)/(\\d+)MB", line) and r"GR3D_FREQ (\\d+)%".
    """
    # TODO: your code here
    raise NotImplementedError("fill me in")
