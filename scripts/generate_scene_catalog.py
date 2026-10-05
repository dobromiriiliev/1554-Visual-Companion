#!/usr/bin/env python3
"""Regenerate the public Markdown scene catalog from source docstrings."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from math1554_visuals.catalog import discover_scenes  # noqa: E402

OUT = ROOT / "docs/reference/scene-catalog.md"


def main() -> int:
    scenes = discover_scenes()
    lines = [
        "# Scene catalog",
        "",
        f"This page is generated from scene class names and docstrings. **{len(scenes)} scenes** are currently discoverable.",
        "",
        "> Regenerate with `python scripts/generate_scene_catalog.py`.",
        "",
    ]
    section = None
    for scene in scenes:
        if scene.section != section:
            section = scene.section
            lines.extend([f"## {scene.section} — {scene.section_title}", ""])
        rel = scene.source_file.relative_to(ROOT)
        lines.extend(
            [
                f"### `{scene.class_name}`",
                "",
                scene.description or "No description provided.",
                "",
                "```bash",
                f"math1554-render --section {scene.section} --scene {scene.class_name} --quality low --preview",
                "```",
                "",
                f"Source: `{rel}`",
                "",
            ]
        )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
