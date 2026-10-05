from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_public_community_files_exist() -> None:
    expected = [
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
    ]
    for rel in expected:
        assert (ROOT / rel).is_file(), rel


def test_packaging_files_are_at_repository_root() -> None:
    assert (ROOT / "pyproject.toml").is_file()
    assert not (ROOT / "src/pyproject.toml").exists()
    assert (ROOT / "README.md").is_file()
