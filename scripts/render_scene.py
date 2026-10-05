#!/usr/bin/env python3
"""Render one scene using a section number and scene class name."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from math1554_visuals.cli import render_main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(render_main())
