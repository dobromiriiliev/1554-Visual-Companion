from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def _collect_nav_paths(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from _collect_nav_paths(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from _collect_nav_paths(item)


def test_mkdocs_navigation_targets_exist() -> None:
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    for rel in _collect_nav_paths(config["nav"]):
        assert (ROOT / "docs" / rel).is_file(), rel
