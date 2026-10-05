"""Visual scenes for MATH 1554 Section 1.8: An Introduction to Linear Transformations."""

from manim import (
    Arrow,
    Create,
    DOWN,
    FadeIn,
    FadeOut,
    LEFT,
    MathTex,
    NumberPlane,
    Rectangle,
    RIGHT,
    Text,
    Transform,
    UP,
    VGroup,
    Write,
)

from math1554_visuals.common.base_scene import CourseScene
from math1554_visuals.common.theme import ACCENT, MUTED, PRIMARY, SECONDARY, SOLUTION, TEXT, WARNING
from math1554_visuals.common.visuals import make_plane, vector_arrow


class DomainCodomainImageRange(CourseScene):
    """Distinguish domain, codomain, image, and range for a matrix transformation."""

    def construct(self) -> None:
        header = self.section_header("1.8", "Domain, Codomain, Image, and Range")
        domain_box = Rectangle(width=4.4, height=4.2, color=PRIMARY).shift(LEFT * 3.2 + DOWN * 0.25)
        codomain_box = Rectangle(width=4.4, height=4.2, color=SECONDARY).shift(RIGHT * 3.2 + DOWN * 0.25)
        domain_label = MathTex(r"\mathbb R^n\;\text{ domain}", color=PRIMARY, font_size=34).next_to(domain_box, UP)
        codomain_label = MathTex(r"\mathbb R^m\;\text{ codomain}", color=SECONDARY, font_size=34).next_to(codomain_box, UP)
        x = MathTex(r"\vec x", color=PRIMARY, font_size=42).move_to(domain_box)
        tx = MathTex(r"T(\vec x)", color=SOLUTION, font_size=42).move_to(codomain_box)
        arrow = Arrow(domain_box.get_right(), codomain_box.get_left(), buff=0.25, color=TEXT)
        t_label = MathTex(r"T(\vec v)=A\vec v", font_size=34).next_to(arrow, UP, buff=0.15)
        range = Text("range = all outputs that actually occur", font_size=25, color=SOLUTION).next_to(codomain_box, DOWN, buff=0.3)

        self.play(FadeIn(header), Create(domain_box), Create(codomain_box))
        self.play(FadeIn(domain_label), FadeIn(codomain_label), FadeIn(x))
        self.play(Create(arrow), Write(t_label), FadeIn(tx))
        self.play(FadeIn(range))
        self.wait(1)


class ExistenceAndUniquenessUnderT(CourseScene):
    """Interpret existence and uniqueness of T(x)=b using earlier Ax=b ideas."""

    def construct(self) -> None:
        header = self.section_header("1.8", "Existence and Uniqueness for T(x)=b")
        equation = MathTex(r"T(\vec x)=\vec b\quad\Longleftrightarrow\quad A\vec x=\vec b", font_size=45).shift(UP * 1.5)
        existence = VGroup(
            Text("Existence", font_size=30, color=PRIMARY),
            MathTex(r"\vec b\in\operatorname{Range}(T)", color=SOLUTION, font_size=36),
            Text("equivalently: b is in the span of A's columns", font_size=23, color=MUTED),
        ).arrange(DOWN, buff=0.22)
        uniqueness = VGroup(
            Text("Uniqueness", font_size=30, color=SECONDARY),
            MathTex(r"A\vec x=\vec0\text{ has only }\vec x=\vec0", color=SOLUTION, font_size=33),
            Text("equivalently: A has a pivot in every column", font_size=23, color=MUTED),
        ).arrange(DOWN, buff=0.22)
        panels = VGroup(existence, uniqueness).arrange(RIGHT, buff=1.2).next_to(equation, DOWN, buff=0.7)

        self.play(FadeIn(header), Write(equation))
        self.play(FadeIn(existence), FadeIn(uniqueness))
        self.wait(1)


class ShearTransformation(CourseScene):
    """Animate a shear transformation on the entire coordinate grid."""

    def construct(self) -> None:
        header = self.section_header("1.8", "A Matrix Can Move the Whole Plane")
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=8.0,
            y_length=6.4,
            background_line_style={"stroke_opacity": 0.35},
        ).shift(DOWN * 0.3)
        formula = MathTex(r"A=\begin{bmatrix}1&1\\0&1\end{bmatrix}", font_size=38).to_corner(RIGHT + UP, buff=0.45)
        label = Text("shear: horizontal position changes with y", font_size=25, color=MUTED).to_edge(DOWN)

        transformed = grid.copy()
        transformed.apply_matrix([[1, 1], [0, 1]])

        self.play(FadeIn(header), Create(grid), Write(formula))
        self.play(Transform(grid, transformed), run_time=2.0)
        self.play(FadeIn(label))
        self.wait(1)


class ProjectionAndRange(CourseScene):
    """Projection onto the x-axis shows that range can be smaller than codomain."""

    def construct(self) -> None:
        header = self.section_header("1.8", "Projection and the Range")
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=8.0,
            y_length=6.4,
            background_line_style={"stroke_opacity": 0.35},
        ).shift(DOWN * 0.3)
        formula = MathTex(r"A=\begin{bmatrix}1&0\\0&0\end{bmatrix}", font_size=38).to_corner(RIGHT + UP, buff=0.45)
        transformed = grid.copy()
        transformed.apply_matrix([[1, 0], [0, 0]])
        range_tex = MathTex(r"\operatorname{Range}(T)=\operatorname{Span}\left\{\begin{bmatrix}1\\0\end{bmatrix}\right\}", color=SOLUTION, font_size=35).to_edge(DOWN)

        self.play(FadeIn(header), Create(grid), Write(formula))
        self.play(Transform(grid, transformed), run_time=2.0)
        self.play(Write(range_tex))
        self.wait(1)


class LinearitySuperposition(CourseScene):
    """Visualize T(u+v)=T(u)+T(v) for a shear."""

    def construct(self) -> None:
        header = self.section_header("1.8", "Linearity = Superposition")
        plane = make_plane(x_range=(-1, 5, 1), y_range=(-1, 4, 1), x_length=7.1, y_length=4.9)
        plane.shift(LEFT * 1.4 + DOWN * 0.5)

        u = (2, 0)
        v = (0, 1)
        uv = (2, 1)
        tu = (2, 0)
        tv = (1, 1)
        tuv = (3, 1)

        input_group = VGroup(
            vector_arrow(plane, u, color=PRIMARY),
            vector_arrow(plane, v, color=SECONDARY),
            vector_arrow(plane, uv, color=ACCENT),
        )
        output_group = VGroup(
            vector_arrow(plane, tu, color=PRIMARY),
            vector_arrow(plane, tv, color=SECONDARY),
            vector_arrow(plane, tuv, color=SOLUTION),
        )

        algebra = VGroup(
            MathTex(r"T(x,y)=(x+y,y)", font_size=33),
            MathTex(r"\vec u=\begin{bmatrix}2\\0\end{bmatrix},\quad\vec v=\begin{bmatrix}0\\1\end{bmatrix}", font_size=31),
            MathTex(r"T(\vec u+\vec v)=\begin{bmatrix}3\\1\end{bmatrix}", color=SOLUTION, font_size=31),
            MathTex(r"T(\vec u)+T(\vec v)=\begin{bmatrix}3\\1\end{bmatrix}", color=SOLUTION, font_size=31),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32).to_edge(RIGHT, buff=0.35)

        self.play(FadeIn(header), Create(plane), FadeIn(algebra[0]), FadeIn(algebra[1]))
        self.play(Create(input_group))
        self.play(Transform(input_group, output_group))
        self.play(FadeIn(algebra[2]), FadeIn(algebra[3]))
        self.wait(1)


class BasisVectorsDetermineTransformation(CourseScene):
    """Knowing the images of the standard basis vectors determines the matrix."""

    def construct(self) -> None:
        header = self.section_header("1.8", "The Basis Vectors Determine Everything")
        statement = MathTex(
            r"\vec x=x_1\vec e_1+x_2\vec e_2",
            font_size=42,
        ).shift(UP * 1.7)
        linearity = MathTex(
            r"T(\vec x)=x_1T(\vec e_1)+x_2T(\vec e_2)",
            color=SOLUTION,
            font_size=42,
        ).next_to(statement, DOWN, buff=0.45)
        images = MathTex(
            r"T(\vec e_1)=\begin{bmatrix}1\\1\end{bmatrix},\qquad"
            r"T(\vec e_2)=\begin{bmatrix}-1\\2\end{bmatrix}",
            font_size=38,
        ).next_to(linearity, DOWN, buff=0.55)
        matrix = MathTex(
            r"A=\begin{bmatrix}\vert&\vert\\T(\vec e_1)&T(\vec e_2)\\\vert&\vert\end{bmatrix}="
            r"\begin{bmatrix}1&-1\\1&2\end{bmatrix}",
            color=PRIMARY,
            font_size=39,
        ).next_to(images, DOWN, buff=0.55)
        note = Text("The columns of A are the images of the standard basis vectors.", font_size=26, color=MUTED).to_edge(DOWN)

        self.play(FadeIn(header), Write(statement))
        self.play(Write(linearity))
        self.play(FadeIn(images))
        self.play(Write(matrix), FadeIn(note))
        self.wait(1)
