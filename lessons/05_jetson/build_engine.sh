#!/usr/bin/env bash
# Run this ON THE JETSON. Engines only work on the device and TensorRT version that built them.
# The output ends with measured latency. Put that number into the site's latency planner.
set -euo pipefail

/usr/src/tensorrt/bin/trtexec \
  --onnx=detector.onnx \
  --saveEngine=detector.engine \
  --fp16
