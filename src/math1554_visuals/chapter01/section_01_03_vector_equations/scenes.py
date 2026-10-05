"""Visual scenes for MATH 1554 Section 1.3: Vector Equations."""

from manim import (
    Arrow,
    Create,
    DashedLine,
    Dot,
    DOWN,
    FadeIn,
    FadeOut,
    LEFT,
    MathTex,
    ORIGIN,
    RIGHT,
    Text,
    Transform,
    UP,
    VGroup,
    Write,
)

from math1554_visuals.common.base_scene import CourseScene
from math1554_visuals.common.theme import ACCENT, MUTED, PRIMARY, SECONDARY, SOLUTION, TEXT
from math1554_visuals.common.visuals import make_plane, vector_arrow


class PointVsVector(CourseScene):
    """The ordered pair (3,2) can be viewed as a point or as a vector from the origin."""

    def construct(self) -> None:
        header = self.section_header("1.3", "Points and Vectors in R²")
        plane = make_plane(x_range=(-4, 5, 1), y_range=(-3, 4, 1), x_length=7.4, y_length=5.2)
        plane.shift(DOWN * 0.45)
        point = Dot(plane.c2p(3, 2), color=SOLUTION)
        arrow = vector_arrow(plane, (3, 2), color=PRIMARY)
        point_label = MathTex(r"(3,2)", color=SOLUTION, font_size=34).next_to(point, UP + RIGHT, buff=0.1)
        vector_label = MathTex(r"\vec v=\begin{bmatrix}3\\2\end{bmatrix}", color=PRIMARY, font_size=34)
        vector_label.to_corner(RIGHT + UP, buff=0.45)

        self.play(FadeIn(header), Create(plane))
        self.play(FadeIn(point), Write(point_label))
        self.play(Create(arrow), Write(vector_label))
        note = Text("same coordinates, different geometric viewpoint", font_size=25, color=MUTED).to_edge(DOWN)
        self.play(FadeIn(note))
        self.wait(1)


class ScalarMultiplication(CourseScene):
    """Positive scalars stretch/compress; negative scalars also reverse direction."""

    def construct(self) -> None:
        header = self.section_header("1.3", "Scalar Multiplication")
        plane = make_plane(x_range=(-6, 6, 1), y_range=(-4, 4, 1), x_length=8.0, y_length=5.2)
        plane.shift(DOWN * 0.45)
        base = (2, 1)
        arrow = vector_arrow(plane, base, color=PRIMARY)
        label = MathTex(r"1\vec v", color=PRIMARY, font_size=36).next_to(arrow.get_end(), UP)
        self.play(FadeIn(header), Create(plane), Create(arrow), Write(label))

        cases = [
            (2.0, r"2\vec v", "same direction, twice the length"),
            (0.5, r"\tfrac12\vec v", "same direction, half the length"),
            (-1.5, r"-\tfrac32\vec v", "negative scalar reverses direction"),
        ]
        current_arrow = arrow
        current_label = label
        note = Text("", font_size=24, color=MUTED).to_edge(DOWN)
        for scalar, tex, text in cases:
            next_arrow = vector_arrow(plane, (scalar * base[0], scalar * base[1]), color=PRIMARY)
            next_label = MathTex(tex, color=PRIMARY, font_size=36).next_to(next_arrow.get_end(), UP)
            next_note = Text(text, font_size=24, color=MUTED).to_edge(DOWN)
            self.play(Transform(current_arrow, next_arrow), Transform(current_label, next_label), Transform(note, next_note))
            self.wait(0.6)
        self.wait(0.5)


class VectorAdditionParallelogram(CourseScene):
    """Visualize vector addition using head-to-tail and parallelogram constructions."""

    def construct(self) -> None:
        header = self.section_header("1.3", "Vector Addition")
        plane = make_plane(x_range=(-4, 5, 1), y_range=(-3, 5, 1), x_length=7.4, y_length=5.2)
        plane.shift(DOWN * 0.45)
        u = (3, 1)
        v = (-1, 2)
        total = (2, 3)
        u_arrow = vector_arrow(plane, u, color=PRIMARY)
        v_arrow = vector_arrow(plane, v, color=SECONDARY)
        total_arrow = vector_arrow(plane, total, color=SOLUTION)
        translated_v = Arrow(plane.c2p(*u), plane.c2p(*total), buff=0, color=SECONDARY, stroke_width=6)
        translated_u = DashedLine(plane.c2p(*v), plane.c2p(*total), color=PRIMARY)
        labels = VGroup(
            MathTex(r"\vec u", color=PRIMARY, font_size=32).next_to(u_arrow.get_end(), RIGHT),
            MathTex(r"\vec v", color=SECONDARY, font_size=32).next_to(v_arrow.get_end(), LEFT),
            MathTex(r"\vec u+\vec v", color=SOLUTION, font_size=32).next_to(total_arrow.get_end(), UP),
        )

        self.play(FadeIn(header), Create(plane))
        self.play(Create(u_arrow), Create(v_arrow), FadeIn(labels[0]), FadeIn(labels[1]))
        self.play(Create(translated_v), Create(translated_u))
        self.play(Create(total_arrow), FadeIn(labels[2]))
        equation = MathTex(
            r"\begin{bmatrix}3\\1\end{bmatrix}+\begin{bmatrix}-1\\2\end{bmatrix}="
            r"\begin{bmatrix}2\\3\end{bmatrix}",
            font_size=36,
        ).to_edge(DOWN)
        self.play(Write(equation))
        self.wait(1)


class LinearCombinationBuildsTarget(CourseScene):
    """Build a target vector from weighted copies of two source vectors."""

    def construct(self) -> None:
        header = self.section_header("1.3", "Linear Combinations")
        plane = make_plane(x_range=(-4, 6, 1), y_range=(-3, 6, 1), x_length=7.3, y_length=5.3)
        plane.shift(LEFT * 1.25 + DOWN * 0.45)
        u = (2, 1)
        v = (-1, 2)
        two_u = (4, 2)
        target = (3, 4)

        u_arrow = vector_arrow(plane, u, color=PRIMARY)
        two_u_arrow = vector_arrow(plane, two_u, color=PRIMARY)
        v_shifted = Arrow(plane.c2p(*two_u), plane.c2p(*target), buff=0, color=SECONDARY, stroke_width=6)
        target_arrow = vector_arrow(plane, target, color=SOLUTION)

        algebra = VGroup(
            MathTex(r"\vec u=\begin{bmatrix}2\\1\end{bmatrix}", color=PRIMARY, font_size=32),
            MathTex(r"\vec v=\begin{bmatrix}-1\\2\end{bmatrix}", color=SECONDARY, font_size=32),
            MathTex(r"2\vec u+\vec v=\begin{bmatrix}3\\4\end{bmatrix}", color=SOLUTION, font_size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).to_edge(RIGHT, buff=0.35)

        self.play(FadeIn(header), Create(plane), Create(u_arrow), FadeIn(algebra[0]), FadeIn(algebra[1]))
        self.play(Transform(u_arrow, two_u_arrow))
        self.play(Create(v_shifted))
        self.play(Create(target_arrow), FadeIn(algebra[2]))
        self.wait(1)


class SpanOfOneVector(CourseScene):
    """All scalar multiples of one nonzero vector form a line through the origin."""

    def construct(self) -> None:
        header = self.section_header("1.3", "The Span of One Vector")
        plane = make_plane(x_range=(-6, 6, 1), y_range=(-4, 4, 1), x_length=8.0, y_length=5.1)
        plane.shift(DOWN * 0.45)
        v = (2, 1)
        span_line = plane.plot(lambda x: 0.5 * x, x_range=[-6, 6], color=PRIMARY)
        samples = VGroup(*[Dot(plane.c2p(2 * k, k), color=SECONDARY, radius=0.055) for k in range(-2, 3)])
        arrow = vector_arrow(plane, v, color=PRIMARY)
        equation = MathTex(r"\operatorname{Span}\{\vec v\}=\{c\vec v:c\in\mathbb R\}", font_size=36)
        equation.to_edge(DOWN)

        self.play(FadeIn(header), Create(plane), Create(arrow))
        self.play(FadeIn(samples))
        self.play(Create(span_line), Write(equation))
        self.wait(1)


class SpanOfTwoVectors(CourseScene):
    """Two nonparallel vectors in R² can generate the whole plane."""

    def construct(self) -> None:
        header = self.section_header("1.3", "The Span of Two Vectors")
        plane = make_plane(x_range=(-5, 5, 1), y_range=(-4, 4, 1), x_length=7.5, y_length=5.2, include_numbers=False)
        plane.shift(DOWN * 0.4)
        u = (2, 1)
        v = (-1, 2)
        u_arrow = vector_arrow(plane, u, color=PRIMARY)
        v_arrow = vector_arrow(plane, v, color=SECONDARY)

        sample_points = []
        for a in range(-2, 3):
            for b in range(-2, 3):
                x = a * u[0] + b * v[0]
                y = a * u[1] + b * v[1]
                if -5 <= x <= 5 and -4 <= y <= 4:
                    sample_points.append(Dot(plane.c2p(x, y), radius=0.045, color=ACCENT))
        samples = VGroup(*sample_points)
        statement = MathTex(r"\operatorname{Span}\{\vec u,\vec v\}=\mathbb R^2", color=SOLUTION, font_size=38)
        statement.to_edge(DOWN)

        self.play(FadeIn(header), Create(plane))
        self.play(Create(u_arrow), Create(v_arrow))
        self.play(FadeIn(samples))
        self.play(Write(statement))
        self.wait(1)


class SpanMembershipAsSystem(CourseScene):
    """Membership in a span is equivalent to solvability of a linear system."""

    def construct(self) -> None:
        header = self.section_header("1.3", "Is b in the Span?")
        vectors = VGroup(
            MathTex(r"\vec u=\begin{bmatrix}1\\2\end{bmatrix}", color=PRIMARY, font_size=36),
            MathTex(r"\vec v=\begin{bmatrix}2\\-1\end{bmatrix}", color=SECONDARY, font_size=36),
            MathTex(r"\vec b=\begin{bmatrix}5\\0\end{bmatrix}", color=SOLUTION, font_size=36),
        ).arrange(RIGHT, buff=0.7).shift(UP * 1.7)
        question = MathTex(r"c_1\vec u+c_2\vec v=\vec b\;?", font_size=42)
        system = MathTex(
            r"\begin{aligned}c_1+2c_2&=5\\2c_1-c_2&=0\end{aligned}",
            font_size=38,
        )
        answer = MathTex(r"c_1=1,\;c_2=2", color=SOLUTION, font_size=38)
        conclusion = MathTex(r"\vec b\in\operatorname{Span}\{\vec u,\vec v\}", color=SOLUTION, font_size=40)
        chain = VGroup(question, system, answer, conclusion).arrange(DOWN, buff=0.32).shift(DOWN * 0.6)

        self.play(FadeIn(header), FadeIn(vectors))
        self.play(Write(question))
        self.play(FadeIn(system))
        self.play(FadeIn(answer), FadeIn(conclusion))
        self.wait(1)
