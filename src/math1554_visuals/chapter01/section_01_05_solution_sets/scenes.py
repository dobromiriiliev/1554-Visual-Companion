"""Visual scenes for MATH 1554 Section 1.5: Solution Sets of Linear Systems."""

from manim import (
    Create,
    Dot,
    DOWN,
    FadeIn,
    LEFT,
    MathTex,
    RIGHT,
    Text,
    UP,
    VGroup,
    Write,
)

from math1554_visuals.common.base_scene import CourseScene
from math1554_visuals.common.theme import FREE, MUTED, PRIMARY, SECONDARY, SOLUTION, TEXT, WARNING
from math1554_visuals.common.visuals import augmented_matrix_tex, make_plane, vector_arrow


class HomogeneousAlwaysContainsZero(CourseScene):
    """Every homogeneous system A x = 0 has the trivial solution x = 0."""

    def construct(self) -> None:
        header = self.section_header("1.5", "Homogeneous Systems")
        equation = MathTex(r"A\vec x=\vec 0", font_size=52).shift(UP * 1.2)
        substitution = MathTex(r"A\vec 0=\vec 0", font_size=46, color=SOLUTION)
        conclusion = Text("So every homogeneous system is consistent.", font_size=30, color=SOLUTION)
        question = Text("The interesting question: are there nonzero solutions too?", font_size=27, color=MUTED)
        group = VGroup(substitution, conclusion, question).arrange(DOWN, buff=0.45).next_to(equation, DOWN, buff=0.6)

        self.play(FadeIn(header), Write(equation))
        self.play(Write(substitution), FadeIn(conclusion))
        self.play(FadeIn(question))
        self.wait(1)


class FreeVariableCreatesDirection(CourseScene):
    """One free parameter traces a line of homogeneous solutions through the origin."""

    def construct(self) -> None:
        header = self.section_header("1.5", "A Free Variable Creates a Direction")
        plane = make_plane(x_range=(-6, 6, 1), y_range=(-4, 4, 1), x_length=7.5, y_length=5.0)
        plane.shift(LEFT * 1.45 + DOWN * 0.5)
        line = plane.plot(lambda x: x / 2, x_range=[-6, 6], color=PRIMARY)
        arrow = vector_arrow(plane, (2, 1), color=PRIMARY)
        origin = Dot(plane.c2p(0, 0), color=SOLUTION)

        equations = VGroup(
            MathTex(r"x_1-2x_2=0", font_size=36),
            MathTex(r"x_2=t", color=FREE, font_size=36),
            MathTex(r"x_1=2t", font_size=36),
            MathTex(r"\vec x=t\begin{bmatrix}2\\1\end{bmatrix}", color=SOLUTION, font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT, buff=0.4)

        samples = VGroup(*[Dot(plane.c2p(2 * t, t), color=SECONDARY, radius=0.055) for t in [-2, -1, 0, 1, 2]])

        self.play(FadeIn(header), Create(plane), Write(equations[0]))
        self.play(FadeIn(equations[1]), FadeIn(equations[2]))
        self.play(Create(arrow), FadeIn(origin), FadeIn(equations[3]))
        self.play(FadeIn(samples), Create(line))
        self.wait(1)


class ParametricVectorForm(CourseScene):
    """Convert a reduced system with one free variable into parametric vector form."""

    def construct(self) -> None:
        header = self.section_header("1.5", "Parametric Vector Form")
        rref = augmented_matrix_tex([[1, 0, 2, 3], [0, 1, -1, -1]], font_size=44).shift(UP * 1.35)
        equations = MathTex(
            r"x_1+2x_3=3,\qquad x_2-x_3=-1",
            font_size=38,
        ).next_to(rref, DOWN, buff=0.55)
        parameter = MathTex(r"x_3=t", color=FREE, font_size=38).next_to(equations, DOWN, buff=0.35)
        vector_form = MathTex(
            r"\vec x="
            r"\begin{bmatrix}3\\-1\\0\end{bmatrix}"
            r"+t\begin{bmatrix}-2\\1\\1\end{bmatrix}",
            color=SOLUTION,
            font_size=43,
        ).next_to(parameter, DOWN, buff=0.45)
        labels = VGroup(
            Text("particular solution", font_size=23, color=PRIMARY),
            Text("free direction", font_size=23, color=SECONDARY),
        ).arrange(RIGHT, buff=1.7).next_to(vector_form, DOWN, buff=0.35)

        self.play(FadeIn(header), FadeIn(rref))
        self.play(Write(equations), Write(parameter))
        self.play(Write(vector_form), FadeIn(labels))
        self.wait(1)


class HomogeneousVsInhomogeneousGeometry(CourseScene):
    """Compare a homogeneous solution line with a translated inhomogeneous solution line."""

    def _panel(self, homogeneous: bool) -> VGroup:
        plane = make_plane(
            x_range=(-5, 5, 1),
            y_range=(-4, 4, 1),
            x_length=4.4,
            y_length=4.0,
            include_numbers=False,
        )
        if homogeneous:
            line = plane.plot(lambda x: 0.5 * x, x_range=[-5, 5], color=PRIMARY)
            equation = MathTex(r"x_1-2x_2=0", font_size=31)
            form = MathTex(r"\vec x=t\begin{bmatrix}2\\1\end{bmatrix}", color=SOLUTION, font_size=30)
            label = Text("through the origin", font_size=22, color=SOLUTION)
        else:
            line = plane.plot(lambda x: 0.5 * x + 1.5, x_range=[-5, 5], color=SECONDARY)
            equation = MathTex(r"x_1-2x_2=-3", font_size=31)
            form = MathTex(
                r"\vec x=\begin{bmatrix}-3\\0\end{bmatrix}+t\begin{bmatrix}2\\1\end{bmatrix}",
                color=SOLUTION,
                font_size=28,
            )
            label = Text("translated affine line", font_size=22, color=SECONDARY)
        geometry = VGroup(plane, line)
        return VGroup(equation, geometry, form, label).arrange(DOWN, buff=0.14)

    def construct(self) -> None:
        header = self.section_header("1.5", "Homogeneous vs. Inhomogeneous Solution Sets")
        homogeneous = self._panel(True)
        inhomogeneous = self._panel(False)
        panels = VGroup(homogeneous, inhomogeneous).arrange(RIGHT, buff=0.7).scale(0.88).shift(DOWN * 0.45)
        note = Text("Same direction vector; the inhomogeneous set is shifted.", font_size=26, color=MUTED).to_edge(DOWN)

        self.play(FadeIn(header), FadeIn(panels))
        self.play(FadeIn(note))
        self.wait(1)


class TrivialVsNontrivialSolutions(CourseScene):
    """A homogeneous system has nontrivial solutions exactly when a free variable exists."""

    def construct(self) -> None:
        header = self.section_header("1.5", "Trivial or Nontrivial?")
        unique = augmented_matrix_tex([[1, 0, 0], [0, 1, 0]], font_size=40)
        free = augmented_matrix_tex([[1, -2, 0], [0, 0, 0]], font_size=40)
        left = VGroup(
            Text("no free variables", font_size=27, color=PRIMARY),
            unique,
            MathTex(r"\vec x=\vec0\text{ only}", color=SOLUTION, font_size=32),
        ).arrange(DOWN, buff=0.35)
        right = VGroup(
            Text("a free variable exists", font_size=27, color=FREE),
            free,
            MathTex(r"\vec x=t\begin{bmatrix}2\\1\end{bmatrix}", color=SOLUTION, font_size=32),
        ).arrange(DOWN, buff=0.35)
        panels = VGroup(left, right).arrange(RIGHT, buff=1.4).shift(DOWN * 0.25)
        theorem = Text("free variable ⇔ infinitely many solutions ⇔ nontrivial homogeneous solutions", font_size=24, color=MUTED)
        theorem.to_edge(DOWN)

        self.play(FadeIn(header), FadeIn(panels))
        self.play(FadeIn(theorem))
        self.wait(1)
