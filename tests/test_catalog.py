from math1554_visuals.catalog import discover_scenes, find_scene, scenes_for_section


def test_chapter_one_has_42_scenes() -> None:
    scenes = discover_scenes()
    assert len(scenes) == 42
    assert len({scene.class_name for scene in scenes}) == 42


def test_each_scene_has_description() -> None:
    assert all(scene.description for scene in discover_scenes())


def test_find_scene() -> None:
    scene = find_scene("1.1", "SolutionCountCases")
    assert scene.section_title == "Systems of Linear Equations"


def test_section_filter() -> None:
    assert len(scenes_for_section("1.8")) == 6
