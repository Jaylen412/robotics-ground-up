"""Puts every lesson folder on the import path so tests can `import pid`.

By default tests run against lessons/. To check the reference answers instead:
    LESSON_SRC=solutions pytest
"""
import os
import sys
from pathlib import Path

root = Path(__file__).parent / os.environ.get("LESSON_SRC", "lessons")
for folder in sorted(p for p in root.iterdir() if p.is_dir()):
    sys.path.insert(0, str(folder))
