"""Visual scenes for MATH 1554 Section 1.2: Row Reduction and Echelon Forms."""

from manim import (
    Axes,
    Circumscribe,
    Create,
    Dot,
    DOWN,
    FadeIn,
    FadeOut,
    Indicate,
    LEFT,
    MathTex,
    Matrix,
    ORIGIN,
    RIGHT,
    SurroundingRectangle,
    Text,
    Transform,
    UP,
    VGroup,
    Write,
)

from math1554_visuals.common.base_scene import CourseScene
from math1554_visuals.common.theme import FREE, MUTED, PIVOT, PRIMARY, SECONDARY, SOLUTION, TEXT, WARNING
from math1554_visuals.common.visuals import augmented_matrix_tex, caption


class REFvsRREF(CourseScene):
    """Build the visual checklist that distinguishes REF from RREF."""

    def construct(self) -> None:
        header = self.section_header("1.2", "REF versus RREF")
        ref = Matrix([[1, 3, -2, 4], [0, 2, 5, -1], [0, 0, -3, 7], [0, 0, 0, 0]])
        rref = Matrix([[1, 0, 0, 2], [0, 1, 0, -1], [0, 0, 1, 3], [0, 0, 0, 0]])
        ref.scale(0.68).shift(LEFT * 3.2 + DOWN * 0.25)
        rref.scale(0.68).shift(RIGHT * 3.2 + DOWN * 0.25)

        ref_label = Text("REF", font_size=30, color=PRIMARY).next_to(ref, UP)
        rref_label = Text("RREF", font_size=30, color=SOLUTION).next_to(rref, UP)
        ref_rules = VGroup(
            Text("• zero rows at bottom", font_size=22),
            Text("• pivots move right", font_size=22),
            Text("• zeros below pivots", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).next_to(ref, DOWN, buff=0.3)
        rref_rules = VGroup(
            Text("• every pivot is 1", font_size=22),
            Text("• pivot is alone in its column", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).next_to(rref, DOWN, buff=0.3)

        self.play(FadeIn(header))
        self.play(FadeIn(ref), FadeIn(ref_label), FadeIn(ref_rules))
        self.play(FadeIn(rref), FadeIn(rref_label), FadeIn(rref_rules))

        # Highlight the staircase of leading entries.
        ref_entries = ref.get_entries()
        rref_entries = rref.get_entries()
        for entry in [ref_entries[0], ref_entries[5], ref_entries[10]]:
            self.play(Indicate(entry, color=PIVOT), run_time=0.35)
        for entry in [rref_entries[0], rref_entries[5], rref_entries[10]]:
            self.play(Indicate(entry, color=PIVOT), run_time=0.35)
        self.wait(1)


class PivotPositionsAndColumns(CourseScene):
    """Identify pivot positions and distinguish pivot columns from free columns."""

    def construct(self) -> None:
        header = self.section_header("1.2", "Pivot Positions and Pivot Columns")
        matrix = Matrix([[1, 2, 0, -1], [0, 0, 1, 4], [0, 0, 0, 0]], h_buff=1.0)
        matrix.scale(0.88).shift(UP * 0.25)
        entries = matrix.get_entries()

        pivot_boxes = VGroup(
            SurroundingRectangle(entries[0], color=PIVOT, buff=0.12),
            SurroundingRectangle(entries[6], color=PIVOT, buff=0.12),
        )
        pivot_text = MathTex(r"\text{pivot columns: }1,3", color=PIVOT, font_size=34)
        free_text = MathTex(r"\text{nonpivot columns: }2,4", color=FREE, font_size=34)
        labels = VGroup(pivot_text, free_text).arrange(DOWN, buff=0.2).next_to(matrix, DOWN, buff=0.45)

        self.play(FadeIn(header), FadeIn(matrix))
        self.play(Create(pivot_boxes), FadeIn(labels))
        self.wait(1)


class RowReductionAlgorithm(CourseScene):
    """Animate a complete row-reduction sequence to RREF."""

    def construct(self) -> None:
        header = self.section_header("1.2", "The Row-Reduction Algorithm")
        matrices = [
            [[1, 2, -1, 3], [2, 4, 1, 9], [0, 1, 2, 5]],
            [[1, 2, -1, 3], [0, 0, 3, 3], [0, 1, 2, 5]],
            [[1, 2, -1, 3], [0, 1, 2, 5], [0, 0, 3, 3]],
            [[1, 2, -1, 3], [0, 1, 2, 5], [0, 0, 1, 1]],
            [[1, 2, -1, 3], [0, 1, 0, 3], [0, 0, 1, 1]],
            [[1, 2, 0, 4], [0, 1, 0, 3], [0, 0, 1, 1]],
            [[1, 0, 0, -2], [0, 1, 0, 3], [0, 0, 1, 1]],
        ]
        operations = [
            r"R_2-2R_1\to R_2",
            r"R_2\leftrightarrow R_3",
            r"\frac13R_3\to R_3",
            r"R_2-2R_3\to R_2",
            r"R_1+R_3\to R_1",
            r"R_1-2R_2\to R_1",
        ]

        current = augmented_matrix_tex(matrices[0], font_size=43).shift(UP * 0.45)
        op = MathTex(r"\text{start}", color=SECONDARY, font_size=34).next_to(current, DOWN, buff=0.45)
        self.play(FadeIn(header), FadeIn(current), FadeIn(op))

        for rows, label in zip(matrices[1:], operations):
            next_matrix = augmented_matrix_tex(rows, font_size=43).move_to(current)
            next_op = MathTex(label, color=SECONDARY, font_size=34).move_to(op)
            self.play(Transform(current, next_matrix), Transform(op, next_op))
            self.wait(0.35)

        solution = MathTex(r"(x_1,x_2,x_3)=(-2,3,1)", color=SOLUTION, font_size=38).next_to(op, DOWN, buff=0.45)
        self.play(FadeIn(solution))
        self.wait(1)


class PivotAndFreeVariables(CourseScene):
    """Connect pivot columns to pivot variables and the remaining columns to free variables."""

    def construct(self) -> None:
        header = self.section_header("1.2", "Pivot Variables and Free Variables")
        matrix = augmented_matrix_tex([[1, 2, 0, -1, 3], [0, 0, 1, 4, 2]], font_size=43)
        matrix.shift(UP * 1.2)
        variables = MathTex(r"x_1\quad x_2\quad x_3\quad x_4", font_size=38).next_to(matrix, DOWN, buff=0.5)
        pivot = MathTex(r"x_1,x_3\;\text{ are pivot variables}", color=PIVOT, font_size=36)
        free = MathTex(r"x_2,x_4\;\text{ are free variables}", color=FREE, font_size=36)
        notes = VGroup(pivot, free).arrange(DOWN, buff=0.25).next_to(variables, DOWN, buff=0.45)
        meaning = Text("Free variables can be chosen; pivot variables respond to those choices.", font_size=24, color=MUTED)
        meaning.to_edge(DOWN)

        self.play(FadeIn(header), FadeIn(matrix), Write(variables))
        self.play(FadeIn(notes), FadeIn(meaning))
        self.wait(1)


class ExistenceAndUniquenessFlowchart(CourseScene):
    """Turn Theorem 1.20 into a compact decision tree."""

    def construct(self) -> None:
        header = self.section_header("1.2", "Existence and Uniqueness")
        start = Text("Look at the RREF of the augmented matrix", font_size=28, color=TEXT)
        start.next_to(header, DOWN, buff=0.5).align_to(header, LEFT)
        q1 = Text("Pivot in the last (augmented) column?", font_size=27, color=PRIMARY)
        q1.next_to(start, DOWN, buff=0.65)

        no_solution = Text("YES → inconsistent → no solution", font_size=27, color=WARNING)
        q2 = Text("NO → any free variables?", font_size=27, color=SECONDARY)
        no_solution.next_to(q1, DOWN, buff=0.45).shift(LEFT * 2.1)
        q2.next_to(q1, DOWN, buff=0.45).shift(RIGHT * 2.0)

        infinite = Text("YES → infinitely many solutions", font_size=25, color=FREE)
        unique = Text("NO → unique solution", font_size=25, color=SOLUTION)
        results = VGroup(infinite, unique).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(q2, DOWN, buff=0.45)

        self.play(FadeIn(header), Write(start))
        self.play(FadeIn(q1))
        self.play(FadeIn(no_solution), FadeIn(q2))
        self.play(FadeIn(results))
        self.wait(1)


class PolynomialInterpolation(CourseScene):
    """Use a linear system to recover the coefficients of a polynomial."""

    def construct(self) -> None:
        header = self.section_header("1.2", "Row Reduction Finds Polynomial Coefficients")
        axes = Axes(x_range=[-2, 3, 1], y_range=[0, 7, 1], x_length=5.2, y_length=4.0)
        axes.shift(LEFT * 3.2 + DOWN * 0.45)
        points = [(-1, 2), (0, 1), (2, 5)]
        dots = VGroup(*[Dot(axes.c2p(x, y), color=PRIMARY) for x, y in points])
        curve = axes.plot(lambda x: x * x + 1, x_range=[-1.7, 2.4], color=SOLUTION)

        model = MathTex(r"p(x)=ax^2+bx+c", font_size=38, color=TEXT)
        system = MathTex(
            r"\begin{aligned}a-b+c&=2\\c&=1\\4a+2b+c&=5\end{aligned}",
            font_size=34,
        )
        solution = MathTex(r"a=1,\;b=0,\;c=1", color=SOLUTION, font_size=36)
        formula = MathTex(r"p(x)=x^2+1", color=SOLUTION, font_size=40)
        algebra = VGroup(model, system, solution, formula).arrange(DOWN, buff=0.3).to_edge(RIGHT, buff=0.55)

        self.play(FadeIn(header), Create(axes), FadeIn(dots))
        self.play(Write(model), FadeIn(system))
        self.play(FadeIn(solution), Create(curve), Write(formula))
        self.wait(1)
