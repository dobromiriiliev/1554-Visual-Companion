"""Command-line tools for discovering, checking, and rendering scenes."""

from __future__ import annotations

import argparse
import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path

from math1554_visuals.catalog import discover_scenes, find_scene

QUALITY_FLAGS = {
    "low": "-ql",
    "medium": "-qm",
    "high": "-qh",
    "4k": "-qk",
}


def _repo_root_from_source(source_file: Path) -> Path:
    """Find the editable-checkout root containing a scene source file."""
    current = source_file.resolve()
    for parent in current.parents:
        if (parent / "pyproject.toml").exists() and (parent / "src").exists():
            return parent
    return Path.cwd()


def list_scenes_main(argv: list[str] | None = None) -> int:
    """CLI entry point for scene discovery."""
    parser = argparse.ArgumentParser(description="List MATH 1554 Visual Companion scenes.")
    parser.add_argument("--section", help="Filter by section number, e.g. 1.3")
    args = parser.parse_args(argv)

    scenes = discover_scenes()
    if args.section:
        scenes = [scene for scene in scenes if scene.section == args.section]

    if not scenes:
        print("No scenes found.")
        return 1

    current = None
    for scene in scenes:
        if scene.section != current:
            current = scene.section
            print(f"\n{scene.section} — {scene.section_title}")
        suffix = f" — {scene.description}" if scene.description else ""
        print(f"  {scene.class_name}{suffix}")
    print(f"\n{len(scenes)} scene(s)")
    return 0


def render_main(argv: list[str] | None = None) -> int:
    """CLI entry point for rendering one named scene."""
    parser = argparse.ArgumentParser(description="Render a named MATH 1554 scene with Manim.")
    parser.add_argument("--section", required=True, help="Section number, e.g. 1.1")
    parser.add_argument("--scene", required=True, help="Scene class name")
    parser.add_argument("--quality", choices=QUALITY_FLAGS, default="low")
    parser.add_argument("--preview", action="store_true", help="Open the render after completion")
    parser.add_argument("--write-to-movie", action="store_true", help="Explicitly request movie output")
    args = parser.parse_args(argv)

    scene = find_scene(args.section, args.scene)
    command = ["manim", QUALITY_FLAGS[args.quality]]
    if args.preview:
        command.append("-p")
    if args.write_to_movie:
        command.append("--write_to_movie")
    command.extend([str(scene.source_file), scene.class_name])

    print("Running:", " ".join(command))
    return subprocess.call(command, cwd=_repo_root_from_source(scene.source_file))


def doctor_main(argv: list[str] | None = None) -> int:
    """CLI entry point for local-environment checks."""
    del argv
    checks: list[tuple[str, bool, str]] = []
    py_ok = sys.version_info >= (3, 11)
    checks.append(("Python >= 3.11", py_ok, sys.version.split()[0]))

    for executable in ("ffmpeg", "latex"):
        path = shutil.which(executable)
        checks.append((executable, path is not None, path or "not found"))

    manim_spec = importlib.util.find_spec("manim")
    checks.append(
        ("Manim import", manim_spec is not None, "available" if manim_spec else "not installed")
    )

    root_layout = (Path.cwd() / "pyproject.toml").exists() and (Path.cwd() / "src").is_dir()
    checks.append(("Repository-root working directory", root_layout, str(Path.cwd())))

    print("MATH 1554 Visual Companion — environment doctor\n")
    failed = False
    for label, ok, detail in checks:
        status = "OK" if ok else "FAIL"
        print(f"[{status:4}] {label}: {detail}")
        failed = failed or not ok

    if failed:
        print("\nOne or more checks failed. See docs/getting-started.md for setup guidance.")
        return 1
    print("\nEnvironment looks ready for rendering.")
    return 0


if __name__ == "__main__":
    raise SystemExit(list_scenes_main())
