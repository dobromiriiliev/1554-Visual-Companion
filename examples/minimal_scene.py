"""Minimal example"""

from manim import Create, FadeIn, MathTex

from math1554_visuals.common.base_scene import CourseScene
from math1554_visuals.common.theme import PRIMARY
from math1554_visuals.common.visuals import make_plane


class MinimalCompanionScene(CourseScene):
    def construct(self) -> None:
        header = self.section_header("Example", "Minimal Companion Scene")
        plane = make_plane()
        equation = MathTex(r"y=x", color=PRIMARY)
        line = plane.plot(lambda x: x, x_range=[-3, 3], color=PRIMARY)

        self.play(FadeIn(header), Create(plane))
        self.play(FadeIn(equation), Create(line))
        self.wait(1)
