from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "src" / "math1554_visuals" / "chapter01"


def test_chapter_one_sections_exist():
    expected = {
        "section_01_01_systems_of_linear_equations",
        "section_01_02_row_reduction_and_echelon_forms",
        "section_01_03_vector_equations",
        "section_01_04_matrix_equation",
        "section_01_05_solution_sets",
        "section_01_07_linear_independence",
        "section_01_08_linear_transformations",
    }
    actual = {p.name for p in CHAPTER.iterdir() if p.is_dir()}
    assert expected <= actual


def test_first_section_has_starter_scenes():
    scenes = CHAPTER / "section_01_01_systems_of_linear_equations" / "scenes.py"
    text = scenes.read_text()
    assert "class LinearEquationAsLine" in text
    assert "class SolutionCountCases" in text
