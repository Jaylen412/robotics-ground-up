# Robotics from the Ground Up

An interactive course from robotics fundamentals to edge AI on an NVIDIA Jetson Orin Nano, with two build paths: a rover (Rolling) and a quadcopter (Flying).

- `index.html` is the course site: lessons, simulations and quizzes. Open it in a browser.
- `lessons/` holds one coding lesson per module. Each file has functions to fill in.
- `tests/` checks your work.
- `solutions/` holds reference answers. Try first.

## Setup

Needs Python 3.9 or newer. Lessons 1 to 6 use only the standard library, so they run on a laptop or on the Jetson.

```bash
git clone <your fork's URL>
cd robotics-ground-up
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Use it in VS Code

1. Open the folder in VS Code and install the recommended extensions when prompted.
2. Pick the `.venv` interpreter (Command Palette, "Python: Select Interpreter").
3. Open the Testing panel (the flask icon). Every test starts red.
4. Open a lesson file, replace each `raise NotImplementedError` with your code, and rerun its tests until they pass.
5. To read the site next to your code, run the task "Serve course site" (Terminal, Run Task) and open http://localhost:8000.

From a terminal:

```bash
pytest                               # everything
pytest tests/test_02_control.py      # one lesson
LESSON_SRC=solutions pytest          # confirm the reference answers pass
```

## Lessons

| Module | Site section | File to edit | What you write |
|---|---|---|---|
| 1 Fundamentals | `#fundamentals` | `lessons/01_fundamentals/pwm.py` | PWM voltage, servo pulses, battery runtime |
| 2 Control | `#control` | `lessons/02_control/pid.py` | A PID controller with anti-windup |
| 3 Motion | `#motion` | `lessons/03_motion/diff_drive.py`, `comp_filter.py` | Wheel kinematics and a complementary filter |
| 4 ROS 2 | `#ros2` | `lessons/04_ros2/safety.py` | Obstacle speed logic, wrapped by a real ROS 2 node |
| 5 Jetson Orin Nano | `#jetson` | `lessons/05_jetson/budget.py` | Latency and memory budgets, a tegrastats parser |
| 6A Rolling | `#rolling` | `lessons/06a_rolling/odometry.py` | Encoder odometry |
| 6B Flying | `#flying` | `lessons/06b_flying/flight.py` | Thrust margin, hover time, an offboard velocity command |

## Files that need the robot

These are complete examples, not exercises, and are not covered by the tests:

- `lessons/04_ros2/forward_node.py` and `obstacle_stop_node.py` need ROS 2 (Humble on Ubuntu 22.04, Jazzy on 24.04).
- `lessons/05_jetson/export_onnx.py` needs PyTorch. `build_engine.sh` must run on the Jetson itself.

## Adding your own lesson

1. Add a folder under `lessons/` with a Python file. Give the file a name no other lesson uses.
2. Add `tests/test_<name>.py` that imports from it.
3. Put your answer in the matching folder under `solutions/`.
4. Add a "Code lab" block to the module in `index.html` (search for `class="lab code"`).
