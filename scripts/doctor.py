#!/usr/bin/env python3
"""Run the project environment doctor directly from a source checkout."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from math1554_visuals.cli import doctor_main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(doctor_main())
