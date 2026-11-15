"""Lesson 5: memory and latency budgets for the Orin Nano.

Run:  pytest tests/test_05_jetson.py
"""
import re


def total_latency_ms(stages):
    """Sum a dict of stage name -> milliseconds."""
    return sum(stages.values())


def max_fps(latency_ms):
    """Highest frame rate a pipeline with this total latency can sustain."""
    return 1000.0 / latency_ms


def blind_distance_m(speed_m_s, latency_ms):
    """Distance the robot covers while one frame is being processed."""
    return speed_m_s * latency_ms / 1000.0


def memory_headroom_gb(parts, total_gb=8.0):
    """Free memory left after a dict of component name -> GB. May be negative."""
    return total_gb - sum(parts.values())


def parse_tegrastats(line):
    """Pull RAM and GPU load out of one line of tegrastats output.

    Example line (yours will have more fields):
      "RAM 2448/7620MB (lfb 4x4MB) SWAP 0/3810MB CPU [5%@729] GR3D_FREQ 45% VDD_IN 6120mW/5890mW"

    Return {"ram_used_mb": 2448, "ram_total_mb": 7620, "gpu_pct": 45}.
    Hint: re.search(r"RAM (\\d+)/(\\d+)MB", line) and r"GR3D_FREQ (\\d+)%".
    """
    ram = re.search(r"RAM (\d+)/(\d+)MB", line)
    gpu = re.search(r"GR3D_FREQ (\d+)%", line)
    return {
        "ram_used_mb": int(ram.group(1)),
        "ram_total_mb": int(ram.group(2)),
        "gpu_pct": int(gpu.group(1)),
    }
