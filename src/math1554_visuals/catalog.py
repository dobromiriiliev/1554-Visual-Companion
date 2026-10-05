"""Source-level scene discovery utilities.

This module intentionally uses :mod:`ast` instead of importing scene modules. That
keeps scene discovery usable even when native Manim rendering dependencies are
unavailable.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class SceneInfo:
    section: str
    section_title: str
    class_name: str
    description: str
    source_file: Path


SECTION_INFO = {
    "section_01_01_systems_of_linear_equations": ("1.1", "Systems of Linear Equations"),
    "section_01_02_row_reduction_and_echelon_forms": ("1.2", "Row Reduction and Echelon Forms"),
    "section_01_03_vector_equations": ("1.3", "Vector Equations"),
    "section_01_04_matrix_equation": ("1.4", "The Matrix Equation Ax = b"),
    "section_01_05_solution_sets": ("1.5", "Solution Sets of Linear Systems"),
    "section_01_07_linear_independence": ("1.7", "Linear Independence"),
    "section_01_08_linear_transformations": ("1.8", "An Introduction to Linear Transformations"),
}


def package_root() -> Path:
    """Return the installed package directory."""
    return Path(__file__).resolve().parent


def discover_scenes() -> list[SceneInfo]:
    """Discover public scene classes by parsing section source files."""
    scenes: list[SceneInfo] = []
    chapter = package_root() / "chapter01"
    for directory_name, (section, title) in SECTION_INFO.items():
        source = chapter / directory_name / "scenes.py"
        tree = ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            bases = {getattr(base, "id", None) for base in node.bases}
            if not bases.intersection({"CourseScene", "CourseThreeDScene"}):
                continue
            description = (ast.get_docstring(node) or "").strip().split("\n")[0]
            scenes.append(
                SceneInfo(
                    section=section,
                    section_title=title,
                    class_name=node.name,
                    description=description,
                    source_file=source,
                )
            )
    return scenes


def scenes_for_section(section: str) -> list[SceneInfo]:
    """Return scenes for one course section."""
    return [scene for scene in discover_scenes() if scene.section == section]


def find_scene(section: str, class_name: str) -> SceneInfo:
    """Find one scene by section and class name, raising a helpful error if absent."""
    matches = [
        scene
        for scene in discover_scenes()
        if scene.section == section and scene.class_name == class_name
    ]
    if not matches:
        available = ", ".join(scene.class_name for scene in scenes_for_section(section)) or "none"
        raise ValueError(
            f"Unknown scene {class_name!r} in section {section}. Available scenes: {available}"
        )
    return matches[0]
