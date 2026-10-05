#!/usr/bin/env python3
"""Validate public-repository invariants without rendering Manim scenes."""

from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PUBLIC_FILES = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "GOVERNANCE.md",
    "PROJECT_CHARTER.md",
    "ROADMAP.md",
    "ATTRIBUTION.md",
    "CITATION.cff",
    "CHANGELOG.md",
    "pyproject.toml",
    "course_map.yaml",
    "mkdocs.yml",
]


def fail(message: str) -> None:
    raise SystemExit(f"repository validation failed: {message}")


def main() -> int:
    for rel in REQUIRED_PUBLIC_FILES:
        if not (ROOT / rel).is_file():
            fail(f"missing {rel}")

    if (ROOT / "src/pyproject.toml").exists():
        fail("pyproject.toml must live at repository root, not src/")

    scene_names: set[str] = set()
    scene_files = sorted((ROOT / "src/math1554_visuals/chapter01").glob("section_*/scenes.py"))
    if len(scene_files) != 7:
        fail(f"expected 7 Chapter 1 scene files, found {len(scene_files)}")

    total = 0
    for source in scene_files:
        tree = ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
        local = 0
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            bases = {getattr(base, "id", None) for base in node.bases}
            if not bases.intersection({"CourseScene", "CourseThreeDScene"}):
                continue
            local += 1
            total += 1
            if node.name in scene_names:
                fail(f"duplicate scene class name: {node.name}")
            scene_names.add(node.name)
            if not ast.get_docstring(node):
                fail(f"scene {node.name} is missing a class docstring")
        if local == 0:
            fail(f"no CourseScene classes found in {source}")

    if total < 42:
        fail(f"expected at least 42 Chapter 1 scenes, found {total}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for phrase in ("not affiliated", "MIT", "Manim", "course-synchronous"):
        if phrase.lower() not in readme.lower():
            fail(f"README should communicate {phrase!r}")

    print(f"Repository validation passed: {total} scenes, {len(REQUIRED_PUBLIC_FILES)} public files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
