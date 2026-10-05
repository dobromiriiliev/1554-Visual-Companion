#!/usr/bin/env python3
"""Create a new section package without modifying the curriculum map automatically."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "src/math1554_visuals/chapter01"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a new visual-companion section.")
    parser.add_argument("--number", required=True, help="Section number, e.g. 1.9")
    parser.add_argument("--title", required=True, help="Human-readable section title")
    args = parser.parse_args()

    chapter, section = args.number.split(".", maxsplit=1)
    if chapter != "1":
        raise SystemExit(
            "This scaffold currently targets chapter01. Extend the script before adding another chapter."
        )

    directory = CHAPTER / f"section_{int(chapter):02d}_{int(section):02d}_{slugify(args.title)}"
    if directory.exists():
        raise SystemExit(f"Refusing to overwrite existing directory: {directory}")
    directory.mkdir(parents=True)
    (directory / "__init__.py").write_text("", encoding="utf-8")
    (directory / "README.md").write_text(
        f"# {args.number} {args.title}\n\n"
        "## Learning objective\n\nTODO\n\n"
        "## Planned scenes\n\n- TODO\n",
        encoding="utf-8",
    )
    (directory / "scenes.py").write_text(
        "from math1554_visuals.common.base_scene import CourseScene\n\n\n"
        "class ConceptOverview(CourseScene):\n"
        '    """TODO: describe the single visual idea this scene communicates."""\n\n'
        "    def construct(self) -> None:\n"
        '        raise NotImplementedError("Replace the scaffold with an implemented scene.")\n',
        encoding="utf-8",
    )
    print(f"Created {directory}")
    print("Next: update course_map.yaml and public docs manually.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
