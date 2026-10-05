"""Visual scenes for MATH 1554 Section 1.1: Systems of Linear Equations.

All worked examples are original examples chosen to match the section objectives.
"""

from manim import (
    Create,
    Dot,
    DOWN,
    FadeIn,
    FadeOut,
    Indicate,
    LEFT,
    MathTex,
    ORIGIN,
    RIGHT,
    Surface,
    Text,
    ThreeDAxes,
    Transform,
    UP,
    VGroup,
    Write,
)

from math1554_visuals.common.base_scene import CourseScene, CourseThreeDScene
from math1554_visuals.common.theme import MUTED, PRIMARY, SECONDARY, SOLUTION, TEXT, WARNING
from math1554_visuals.common.visuals import augmented_matrix_tex, caption, make_plane


class LinearEquationAsLine(CourseScene):
    """A single linear equation in two variables is a line of solutions."""

    def construct(self) -> None:
        header = self.section_header("1.1", "Systems of Linear Equations")
        prompt = Text("A linear equation describes a whole set of points", font_size=30)
        prompt.to_edge(UP, buff=0.42)
        plane = make_plane(x_length=7.6, y_length=4.8).shift(DOWN * 0.45)
        equation = MathTex(r"x+2y=4", color=PRIMARY, font_size=44).to_corner(UP + RIGHT)
        line = plane.plot(lambda x: 2 - x / 2, x_range=[-4, 6], color=PRIMARY)
        label = MathTex(r"\{(x,y):x+2y=4\}", color=TEXT, font_size=34).next_to(plane, DOWN, buff=0.2)

        self.play(FadeIn(header), Write(prompt))
        self.play(Create(plane), Write(equation))
        self.play(Create(line), FadeIn(label))
        self.wait(1)


class SolutionCountCases(CourseScene):
    """Two linear equations can have zero, one, or infinitely many solutions."""

    def _panel(self, title: str, subtitle: str) -> VGroup:
        plane = make_plane(
            x_range=(-4, 4, 1),
            y_range=(-4, 4, 1),
            x_length=3.1,
            y_length=3.1,
            include_numbers=False,
        )
        title_mob = Text(title, font_size=25, color=TEXT)
        subtitle_mob = Text(subtitle, font_size=19, color=MUTED)
        return VGroup(title_mob, plane, subtitle_mob).arrange(DOWN, buff=0.14)

    def construct(self) -> None:
        header = self.section_header("1.1", "Zero, One, or Infinitely Many")
        one = self._panel("One solution", "the lines intersect once")
        zero = self._panel("No solution", "parallel distinct lines")
        infinite = self._panel("Infinitely many", "the same line")
        panels = VGroup(one, zero, infinite).arrange(RIGHT, buff=0.42).scale(0.92).shift(DOWN * 0.45)

        one_plane = one[1]
        zero_plane = zero[1]
        inf_plane = infinite[1]

        one_l1 = one_plane.plot(lambda x: 0.6 * x + 0.4, x_range=[-4, 4], color=PRIMARY)
        one_l2 = one_plane.plot(lambda x: -0.8 * x + 1.8, x_range=[-3, 4], color=SECONDARY)
        intersection_x = 1.0
        intersection_y = 1.0
        point = Dot(one_plane.c2p(intersection_x, intersection_y), color=SOLUTION)

        zero_l1 = zero_plane.plot(lambda x: 0.55 * x + 1.0, x_range=[-4, 4], color=PRIMARY)
        zero_l2 = zero_plane.plot(lambda x: 0.55 * x - 1.0, x_range=[-4, 4], color=SECONDARY)

        inf_l1 = inf_plane.plot(lambda x: -0.5 * x + 0.6, x_range=[-4, 4], color=PRIMARY)
        inf_l2 = inf_plane.plot(lambda x: -0.5 * x + 0.6, x_range=[-4, 4], color=SECONDARY)

        self.play(FadeIn(header), FadeIn(panels))
        self.play(Create(one_l1), Create(one_l2), FadeIn(point))
        self.play(Create(zero_l1), Create(zero_l2))
        self.play(Create(inf_l1), Create(inf_l2))
        self.wait(1)


class PlaneIntersectionCases(CourseThreeDScene):
    """Show that two nonparallel planes in R^3 intersect in a line."""

    def construct(self) -> None:
        self.set_camera_orientation(phi=65 * 3.14159 / 180, theta=-45 * 3.14159 / 180)
        title = Text("Two equations in three variables describe two planes", font_size=30, color=TEXT)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)

        axes = ThreeDAxes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1])
        plane1 = Surface(
            lambda u, v: axes.c2p(u, v, 0.6 * u - 0.4),
            u_range=[-2.5, 2.5],
            v_range=[-2.5, 2.5],
            resolution=(12, 12),
            fill_opacity=0.45,
            checkerboard_colors=[PRIMARY, PRIMARY],
        )
        plane2 = Surface(
            lambda u, v: axes.c2p(u, v, -0.45 * u + 0.8),
            u_range=[-2.5, 2.5],
            v_range=[-2.5, 2.5],
            resolution=(12, 12),
            fill_opacity=0.45,
            checkerboard_colors=[SECONDARY, SECONDARY],
        )
        note = Text("nonparallel planes intersect in a line", font_size=24, color=SOLUTION).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(note)

        self.play(Create(axes))
        self.play(FadeIn(plane1), FadeIn(plane2), FadeIn(note))
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(2)
        self.stop_ambient_camera_rotation()


class EquationsToAugmentedMatrix(CourseScene):
    """Morph the information in equations into augmented-matrix notation."""

    def construct(self) -> None:
        header = self.section_header("1.1", "Equations to an Augmented Matrix")
        equations = MathTex(
            r"\begin{aligned}"
            r"x_1+2x_2-x_3&=4\\"
            r"2x_1-x_2+3x_3&=1\\"
            r"-x_1+4x_2+x_3&=7"
            r"\end{aligned}",
            font_size=42,
        )
        equations.shift(LEFT * 3.1)
        matrix = augmented_matrix_tex([[1, 2, -1, 4], [2, -1, 3, 1], [-1, 4, 1, 7]], font_size=42)
        matrix.shift(RIGHT * 3.0)
        arrow = MathTex(r"\Longrightarrow", font_size=48, color=MUTED)
        labels = VGroup(
            Text("coefficients", font_size=22, color=PRIMARY),
            Text("constants", font_size=22, color=SECONDARY),
        ).arrange(RIGHT, buff=1.7).next_to(matrix, DOWN, buff=0.35)

        self.play(FadeIn(header))
        self.play(Write(equations))
        self.play(Write(arrow), FadeIn(matrix))
        self.play(FadeIn(labels))
        self.wait(1)


class ElementaryRowOperations(CourseScene):
    """Show the three legal elementary row operations."""

    def construct(self) -> None:
        header = self.section_header("1.1", "Elementary Row Operations")
        original = augmented_matrix_tex([[1, 2, 5], [3, -1, 4]], font_size=45).shift(UP * 1.2)
        operation = Text("start", font_size=28, color=SECONDARY).next_to(original, DOWN, buff=0.55)

        self.play(FadeIn(header), FadeIn(original))

        steps = [
            ("Row replacement:  R₂ ← R₂ − 3R₁", [[1, 2, 5], [0, -7, -11]]),
            ("Row interchange:  R₁ ↔ R₂", [[0, -7, -11], [1, 2, 5]]),
            ("Row scaling:  R₁ ← −(1/7)R₁", [[0, 1, "11/7"], [1, 2, 5]]),
        ]

        current = original.copy()
        self.add(current)
        self.remove(original)
        for text, rows in steps:
            next_matrix = augmented_matrix_tex(rows, font_size=45).move_to(current)
            new_operation = Text(text, font_size=26, color=SECONDARY).next_to(current, DOWN, buff=0.55)
            self.play(Transform(operation, new_operation), Transform(current, next_matrix))
            self.wait(0.6)

        takeaway = Text("Each operation preserves the solution set", font_size=28, color=SOLUTION).to_edge(DOWN)
        self.play(FadeIn(takeaway))
        self.wait(1)


class RowOperationsPreserveSolutionSet(CourseScene):
    """Geometrically show why replacing an equation can preserve the common solution."""

    def construct(self) -> None:
        header = self.section_header("1.1", "Why Row Replacement Works")
        plane = make_plane(x_range=(-1, 5, 1), y_range=(-2, 5, 1), x_length=7.2, y_length=5.0)
        plane.shift(LEFT * 1.4 + DOWN * 0.5)

        line1 = plane.plot(lambda x: 3 - x, x_range=[-1, 5], color=PRIMARY)
        line2 = plane.plot(lambda x: 2 * x - 3, x_range=[0.5, 4], color=SECONDARY)
        replacement = plane.plot(lambda x: x / 2, x_range=[-1, 5], color=SECONDARY)
        solution = Dot(plane.c2p(2, 1), color=SOLUTION, radius=0.08)

        eq1 = MathTex(r"R_1:\;x+y=3", color=PRIMARY, font_size=34)
        eq2 = MathTex(r"R_2:\;2x-y=3", color=SECONDARY, font_size=34)
        op = MathTex(r"R_2-R_1\to R_2", color=TEXT, font_size=34)
        eq2_new = MathTex(r"R_2:\;x-2y=0", color=SECONDARY, font_size=34)
        algebra = VGroup(eq1, eq2, op).arrange(DOWN, aligned_edge=LEFT, buff=0.28).to_edge(RIGHT, buff=0.45)
        eq2_new.move_to(eq2)

        self.play(FadeIn(header), Create(plane), Write(eq1), Write(eq2))
        self.play(Create(line1), Create(line2), FadeIn(solution))
        self.play(Write(op))
        self.play(Transform(line2, replacement), Transform(eq2, eq2_new))
        note = Text("The individual line changes; the shared solution does not", font_size=24, color=SOLUTION)
        note.to_edge(DOWN)
        self.play(FadeIn(note), Indicate(solution, color=SOLUTION))
        self.wait(1)


class ConsistencyAndUniqueness(CourseScene):
    """Read no/unique/infinite solutions directly from reduced augmented matrices."""

    def construct(self) -> None:
        header = self.section_header("1.1", "The Two Fundamental Questions")
        question = VGroup(
            Text("1. Does a solution exist?", font_size=30),
            Text("2. If it exists, is it unique?", font_size=30),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(header, DOWN, buff=0.45).align_to(header, LEFT)

        inconsistent = augmented_matrix_tex([[1, 0, 2], [0, 0, 1]], font_size=34)
        unique = augmented_matrix_tex([[1, 0, 2], [0, 1, -1]], font_size=34)
        infinite = augmented_matrix_tex([[1, 2, 3], [0, 0, 0]], font_size=34)
        cards = VGroup(
            VGroup(inconsistent, Text("inconsistent", font_size=24, color=WARNING)).arrange(DOWN, buff=0.25),
            VGroup(unique, Text("one solution", font_size=24, color=SOLUTION)).arrange(DOWN, buff=0.25),
            VGroup(infinite, Text("infinitely many", font_size=24, color=SECONDARY)).arrange(DOWN, buff=0.25),
        ).arrange(RIGHT, buff=0.65).scale(0.92).shift(DOWN * 1.25)

        notes = VGroup(
            caption(r"a row 0 = nonzero"),
            caption("pivot in every variable column"),
            caption("at least one free variable"),
        )
        for note, card in zip(notes, cards):
            note.next_to(card, DOWN, buff=0.18)

        self.play(FadeIn(header), FadeIn(question))
        self.play(FadeIn(cards), FadeIn(notes))
        self.wait(1)
