"""Visual scenes for MATH 1554 Section 1.4: The Matrix Equation A x = b."""

from manim import (
    Create,
    Dot,
    DOWN,
    FadeIn,
    FadeOut,
    LEFT,
    MathTex,
    Matrix,
    RIGHT,
    Text,
    Transform,
    UP,
    VGroup,
    Write,
)

from math1554_visuals.common.base_scene import CourseScene
from math1554_visuals.common.theme import ACCENT, MUTED, PRIMARY, SECONDARY, SOLUTION, TEXT, WARNING
from math1554_visuals.common.visuals import augmented_matrix_tex, make_plane, vector_arrow


class DimensionsOfAx(CourseScene):
    """Show how the dimensions of A, x, and b must fit together."""

    def construct(self) -> None:
        header = self.section_header("1.4", "The Shape of A x = b")
        equation = MathTex(r"A\vec x=\vec b", font_size=52).shift(UP * 1.1)
        dimensions = MathTex(
            r"\underbrace{A}_{m\times n}"
            r"\underbrace{\vec x}_{n\times 1}="
            r"\underbrace{\vec b}_{m\times 1}",
            font_size=48,
        )
        dimensions.next_to(equation, DOWN, buff=0.7)
        note = Text("n input coordinates → m output coordinates", font_size=28, color=MUTED).next_to(dimensions, DOWN, buff=0.55)

        self.play(FadeIn(header), Write(equation))
        self.play(Write(dimensions), FadeIn(note))
        self.wait(1)


class MatrixVectorAsColumnCombination(CourseScene):
    """Matrix-vector multiplication is a linear combination of the columns of A."""

    def construct(self) -> None:
        header = self.section_header("1.4", "A x is a Column Combination")
        product = MathTex(
            r"\begin{bmatrix}2&-1\\1&3\end{bmatrix}"
            r"\begin{bmatrix}x_1\\x_2\end{bmatrix}",
            font_size=47,
        ).shift(UP * 1.5)
        expansion = MathTex(
            r"=x_1\begin{bmatrix}2\\1\end{bmatrix}"
            r"+x_2\begin{bmatrix}-1\\3\end{bmatrix}",
            font_size=43,
        ).next_to(product, DOWN, buff=0.55)
        example = MathTex(
            r"\vec x=\begin{bmatrix}2\\1\end{bmatrix}"
            r"\Longrightarrow A\vec x="
            r"2\begin{bmatrix}2\\1\end{bmatrix}+"
            r"\begin{bmatrix}-1\\3\end{bmatrix}="
            r"\begin{bmatrix}3\\5\end{bmatrix}",
            color=SOLUTION,
            font_size=36,
        ).next_to(expansion, DOWN, buff=0.6)
        takeaway = Text("The entries of x are weights on the columns of A.", font_size=27, color=MUTED).to_edge(DOWN)

        self.play(FadeIn(header), Write(product))
        self.play(Write(expansion))
        self.play(FadeIn(example), FadeIn(takeaway))
        self.wait(1)


class FourEquivalentRepresentations(CourseScene):
    """Cycle through the four equivalent ways to encode the same linear system."""

    def construct(self) -> None:
        header = self.section_header("1.4", "One Problem, Four Representations")
        title = Text("The same solution set appears in every representation", font_size=27, color=MUTED)
        title.next_to(header, DOWN, buff=0.45).align_to(header, LEFT)

        forms = [
            (
                "system of equations",
                MathTex(r"\begin{aligned}x_1+2x_2&=5\\3x_1-x_2&=4\end{aligned}", font_size=46),
            ),
            (
                "augmented matrix",
                augmented_matrix_tex([[1, 2, 5], [3, -1, 4]], font_size=48),
            ),
            (
                "vector equation",
                MathTex(
                    r"x_1\begin{bmatrix}1\\3\end{bmatrix}+"
                    r"x_2\begin{bmatrix}2\\-1\end{bmatrix}="
                    r"\begin{bmatrix}5\\4\end{bmatrix}",
                    font_size=42,
                ),
            ),
            (
                "matrix equation",
                MathTex(
                    r"\begin{bmatrix}1&2\\3&-1\end{bmatrix}"
                    r"\begin{bmatrix}x_1\\x_2\end{bmatrix}="
                    r"\begin{bmatrix}5\\4\end{bmatrix}",
                    font_size=44,
                ),
            ),
        ]

        label = Text(forms[0][0], font_size=30, color=PRIMARY).shift(UP * 1.0)
        current = forms[0][1].shift(DOWN * 0.35)
        self.play(FadeIn(header), FadeIn(title), FadeIn(label), Write(current))
        for name, form in forms[1:]:
            form.move_to(current)
            next_label = Text(name, font_size=30, color=PRIMARY).move_to(label)
            self.play(Transform(current, form), Transform(label, next_label))
            self.wait(0.75)
        self.wait(0.5)


class ColumnSpanAndExistence(CourseScene):
    """A x = b is solvable exactly when b lies in the span of A's columns."""

    def construct(self) -> None:
        header = self.section_header("1.4", "Existence Means b is in the Column Span")
        plane = make_plane(x_range=(-5, 5, 1), y_range=(-4, 4, 1), x_length=7.2, y_length=5.0)
        plane.shift(LEFT * 1.4 + DOWN * 0.5)

        a1 = (2, 1)
        a2 = (4, 2)  # deliberately dependent; span is one line
        span_line = plane.plot(lambda x: 0.5 * x, x_range=[-5, 5], color=PRIMARY)
        a1_arrow = vector_arrow(plane, a1, color=PRIMARY)
        a2_arrow = vector_arrow(plane, a2, color=SECONDARY)
        b_good = vector_arrow(plane, (-2, -1), color=SOLUTION)
        b_bad = vector_arrow(plane, (1, 3), color=WARNING)

        good = MathTex(r"\vec b_1\in\operatorname{Span}\{\vec a_1,\vec a_2\}", color=SOLUTION, font_size=31)
        good_eq = MathTex(r"A\vec x=\vec b_1\;\text{ has a solution}", color=SOLUTION, font_size=31)
        bad = MathTex(r"\vec b_2\notin\operatorname{Span}\{\vec a_1,\vec a_2\}", color=WARNING, font_size=31)
        bad_eq = MathTex(r"A\vec x=\vec b_2\;\text{ has no solution}", color=WARNING, font_size=31)
        algebra = VGroup(good, good_eq, bad, bad_eq).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT, buff=0.35)

        self.play(FadeIn(header), Create(plane), Create(span_line))
        self.play(Create(a1_arrow), Create(a2_arrow))
        self.play(Create(b_good), FadeIn(good), FadeIn(good_eq))
        self.play(Create(b_bad), FadeIn(bad), FadeIn(bad_eq))
        self.wait(1)


class ConsistentForEveryB(CourseScene):
    """In R², compare a one-dimensional column span with a full two-dimensional span."""

    def _panel(self, full_span: bool) -> VGroup:
        plane = make_plane(
            x_range=(-3, 3, 1),
            y_range=(-3, 3, 1),
            x_length=4.0,
            y_length=4.0,
            include_numbers=False,
        )
        a1 = vector_arrow(plane, (2, 1), color=PRIMARY)
        if full_span:
            a2 = vector_arrow(plane, (-1, 2), color=SECONDARY)
            text = Text("pivot in every row\nspan = R²", font_size=23, color=SOLUTION)
        else:
            a2 = vector_arrow(plane, (-2, -1), color=SECONDARY)
            text = Text("missing row pivot\nspan is only a line", font_size=23, color=WARNING)
        geometry = VGroup(plane, a1, a2)
        return VGroup(geometry, text).arrange(DOWN, buff=0.18)

    def construct(self) -> None:
        header = self.section_header("1.4", "When is A x = b Solvable for Every b?")
        left = self._panel(False)
        right = self._panel(True)
        panels = VGroup(left, right).arrange(RIGHT, buff=1.0).scale(0.95).shift(DOWN * 0.55)
        theorem = MathTex(
            r"A\vec x=\vec b\text{ is consistent for every }\vec b"
            r"\iff A\text{ has a pivot in every row}",
            font_size=32,
            color=TEXT,
        ).to_edge(DOWN)

        self.play(FadeIn(header), FadeIn(panels))
        self.play(Write(theorem))
        self.wait(1)
