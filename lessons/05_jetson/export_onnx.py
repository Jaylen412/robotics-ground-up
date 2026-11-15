"""Export a small PyTorch model to ONNX. Needs torch installed.

    python3 export_onnx.py

Swap TinyNet for your own model. Then build the engine on the Jetson with
build_engine.sh.
"""
import torch
import torch.nn as nn


class TinyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 16, 3, stride=2, padding=1), nn.ReLU(),
            nn.Conv2d(16, 32, 3, stride=2, padding=1), nn.ReLU(),
            nn.AdaptiveAvgPool2d(1), nn.Flatten(), nn.Linear(32, 10),
        )

    def forward(self, x):
        return self.net(x)


model = TinyNet().eval()
dummy = torch.randn(1, 3, 224, 224)   # fixed input size keeps the engine simple
torch.onnx.export(model, dummy, "detector.onnx",
                  input_names=["image"], output_names=["scores"], opset_version=17)
print("wrote detector.onnx")
