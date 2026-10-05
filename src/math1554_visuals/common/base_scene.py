"""Base scene utilities used throughout the visual companion."""

from manim import DOWN, LEFT, UP, Scene, Text, ThreeDScene, VGroup

from math1554_visuals.common.theme import BACKGROUND, MUTED, TEXT


class _CourseSceneMixin:
    """Shared layout helpers for 2D and 3D scenes."""

    def section_header(self, section: str, title: str) -> VGroup:
        number = Text(section, font_size=26, color=MUTED)
        heading = Text(title, font_size=32, color=TEXT)
        group = VGroup(number, heading).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
        group.to_corner(LEFT + UP, buff=0.35)
        return group

    def concept_title(self, text: str) -> Text:
        title = Text(text, font_size=30, color=TEXT)
        title.to_edge(UP, buff=0.45)
        return title


class CourseScene(_CourseSceneMixin, Scene):
    """Base class for ordinary course scenes."""

    def setup(self) -> None:
        super().setup()
        self.camera.background_color = BACKGROUND


class CourseThreeDScene(_CourseSceneMixin, ThreeDScene):
    """Base class for 3D course scenes."""

    def setup(self) -> None:
        super().setup()
        self.camera.background_color = BACKGROUND
