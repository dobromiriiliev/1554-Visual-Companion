"""Visual scenes for MATH 1554 Section 1.7: Linear Independence."""

from manim import (
    Create,
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
from math1554_visuals.common.theme import MUTED, PRIMARY, SECONDARY, SOLUTION, TEXT, WARNING
from math1554_visuals.common.visuals import make_plane, matrix, vector_arrow


class IndependentVsDependent2D(CourseScene):
    """Nonparallel vectors are independent in R²; scalar multiples are dependent."""

    def _panel(self, dependent: bool) -> VGroup:
        plane = make_plane(
            x_range=(-3, 3, 1),
            y_range=(-3, 3, 1),
            x_length=4.2,
            y_length=4.2,
            include_numbers=False,
        )
        u = vector_arrow(plane, (2, 1), color=PRIMARY)
        if dependent:
            v = vector_arrow(plane, (-2, -1), color=SECONDARY)
            label = Text("dependent", font_size=26, color=WARNING)
            relation = MathTex(r"\vec u+\vec v=\vec0", color=WARNING, font_size=30)
        else:
            v = vector_arrow(plane, (-1, 2), color=SECONDARY)
            label = Text("independent", font_size=26, color=SOLUTION)
            relation = MathTex(r"c_1\vec u+c_2\vec v=\vec0\Rightarrow c_1=c_2=0", color=SOLUTION, font_size=27)
        geometry = VGroup(plane, u, v)
        return VGroup(label, geometry, relation).arrange(DOWN, buff=0.13)

    def construct(self) -> None:
        header = self.section_header("1.7", "Independent vs. Dependent")
        independent = self._panel(False)
        dependent = self._panel(True)
        panels = VGroup(independent, dependent).arrange(RIGHT, buff=0.75).scale(0.91).shift(DOWN * 0.45)

        self.play(FadeIn(header), FadeIn(panels))
        self.wait(1)


class OnlyTrivialCombination(CourseScene):
    """Linear independence means zero can be produced only by zero coefficients."""

    def construct(self) -> None:
        header = self.section_header("1.7", "The Zero-Combination Test")
        definition = MathTex(
            r"c_1\vec v_1+\cdots+c_k\vec v_k=\vec0",
            font_size=46,
        ).shift(UP * 1.5)
        independent = MathTex(
            r"\text{independent}\iff c_1=\cdots=c_k=0\text{ is the only solution}",
            color=SOLUTION,
            font_size=34,
        )
        dependent = MathTex(
            r"\text{dependent}\iff \text{some nonzero coefficients also give }\vec0",
            color=WARNING,
            font_size=34,
        )
        examples = VGroup(independent, dependent).arrange(DOWN, buff=0.55).next_to(definition, DOWN, buff=0.7)
        note = Text("Independence asks whether any vector is redundant.", font_size=27, color=MUTED).to_edge(DOWN)

        self.play(FadeIn(header), Write(definition))
        self.play(FadeIn(independent))
        self.play(FadeIn(dependent), FadeIn(note))
        self.wait(1)


class DependenceRelation(CourseScene):
    """Construct a concrete nontrivial dependence relation among three vectors."""

    def construct(self) -> None:
        header = self.section_header("1.7", "A Dependence Relation")
        plane = make_plane(x_range=(-1, 4, 1), y_range=(-1, 4, 1), x_length=6.0, y_length=5.0)
        plane.shift(LEFT * 2.2 + DOWN * 0.5)
        v1 = vector_arrow(plane, (2, 0), color=PRIMARY)
        v2 = vector_arrow(plane, (0, 2), color=SECONDARY)
        v3 = vector_arrow(plane, (2, 2), color=SOLUTION)

        algebra = VGroup(
            MathTex(r"\vec v_1=\begin{bmatrix}2\\0\end{bmatrix}", color=PRIMARY, font_size=31),
            MathTex(r"\vec v_2=\begin{bmatrix}0\\2\end{bmatrix}", color=SECONDARY, font_size=31),
            MathTex(r"\vec v_3=\begin{bmatrix}2\\2\end{bmatrix}", color=SOLUTION, font_size=31),
            MathTex(r"\vec v_1+\vec v_2-\vec v_3=\vec0", color=WARNING, font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT, buff=0.4)
        conclusion = Text("not all coefficients are zero → dependent", font_size=24, color=WARNING).to_edge(DOWN)

        self.play(FadeIn(header), Create(plane))
        self.play(Create(v1), Create(v2), Create(v3), FadeIn(algebra[:3]))
        self.play(Write(algebra[3]), FadeIn(conclusion))
        self.wait(1)


class PivotTestForIndependence(CourseScene):
    """A set of columns is independent iff A x = 0 has no free variables."""

    def construct(self) -> None:
        header = self.section_header("1.7", "Pivots Test Linear Independence")

        independent_matrix = matrix([[1, 0], [0, 1]], scale=0.9)
        dependent_matrix = matrix([[1, 2], [2, 4]], scale=0.9)
        dependent_rref = matrix([[1, 2], [0, 0]], scale=0.9)

        left = VGroup(
            Text("pivot in every column", font_size=25, color=SOLUTION),
            independent_matrix,
            MathTex(r"A\vec x=\vec0\Rightarrow\vec x=\vec0", color=SOLUTION, font_size=30),
            Text("independent", font_size=26, color=SOLUTION),
        ).arrange(DOWN, buff=0.3)

        right = VGroup(
            Text("missing a column pivot", font_size=25, color=WARNING),
            dependent_matrix,
            MathTex(r"\sim", font_size=40),
            dependent_rref,
            Text("free variable → dependent", font_size=25, color=WARNING),
        ).arrange(DOWN, buff=0.2)

        panels = VGroup(left, right).arrange(RIGHT, buff=1.4).scale(0.92).shift(DOWN * 0.25)
        theorem = MathTex(
            r"\{\vec v_1,\ldots,\vec v_k\}\text{ independent}"
            r"\iff [\vec v_1\ \cdots\ \vec v_k]\text{ has a pivot in every column}",
            font_size=29,
        ).to_edge(DOWN)

        self.play(FadeIn(header), FadeIn(panels))
        self.play(Write(theorem))
        self.wait(1)


class TooManyVectorsInR2(CourseScene):
    """Three vectors in R² must be linearly dependent."""

    def construct(self) -> None:
        header = self.section_header("1.7", "Too Many Vectors for the Dimension")
        plane = make_plane(x_range=(-4, 4, 1), y_range=(-4, 4, 1), x_length=7.0, y_length=5.1)
        plane.shift(DOWN * 0.45)
        arrows = VGroup(
            vector_arrow(plane, (2, 0), color=PRIMARY),
            vector_arrow(plane, (0, 2), color=SECONDARY),
            vector_arrow(plane, (2, 2), color=SOLUTION),
        )
        relation = MathTex(r"\vec v_3=\vec v_1+\vec v_2", color=WARNING, font_size=38).to_corner(RIGHT + UP, buff=0.55)
        theorem = MathTex(r"k>n\text{ vectors in }\mathbb R^n\Rightarrow\text{dependent}", font_size=35).to_edge(DOWN)

        self.play(FadeIn(header), Create(plane))
        self.play(Create(arrows[0]), Create(arrows[1]))
        self.play(Create(arrows[2]), Write(relation))
        self.play(Write(theorem))
        self.wait(1)


class ZeroVectorForcesDependence(CourseScene):
    """Any set containing the zero vector is linearly dependent."""

    def construct(self) -> None:
        header = self.section_header("1.7", "Why the Zero Vector Forces Dependence")
        set_tex = MathTex(
            r"\left\{\vec v_1,\;\vec0,\;\vec v_3\right\}",
            font_size=50,
        ).shift(UP * 1.2)
        relation = MathTex(
            r"0\vec v_1+1\vec0+0\vec v_3=\vec0",
            color=WARNING,
            font_size=43,
        ).next_to(set_tex, DOWN, buff=0.7)
        note = Text("A nonzero coefficient (1) produces the zero vector.", font_size=28, color=WARNING).next_to(relation, DOWN, buff=0.55)
        conclusion = Text("Therefore the set is linearly dependent.", font_size=30, color=TEXT).to_edge(DOWN)

        self.play(FadeIn(header), Write(set_tex))
        self.play(Write(relation), FadeIn(note))
        self.play(FadeIn(conclusion))
        self.wait(1)
