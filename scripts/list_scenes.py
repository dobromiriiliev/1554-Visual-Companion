#!/usr/bin/env python3
"""List scene classes discovered from a source checkout."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from math1554_visuals.cli import list_scenes_main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(list_scenes_main())
