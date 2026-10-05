"""Small reusable visual helpers.

The goal is to keep section scene files focused on mathematics rather than repeated
Manim boilerplate.  Helpers here intentionally stay simple and composable.
"""

from __future__ import annotations

from collections.abc import Sequence

from manim import (
    Arrow,
    MathTex,
    Matrix,
    NumberPlane,
    Text,
    VGroup,
)

from math1554_visuals.common.theme import MUTED, PRIMARY, TEXT


def make_plane(
    *,
    x_range: tuple[float, float, float] = (-6, 6, 1),
    y_range: tuple[float, float, float] = (-4, 4, 1),
    x_length: float = 8.0,
    y_length: float = 5.2,
    include_numbers: bool = True,
) -> NumberPlane:
    """Return the standard 2D coordinate plane used throughout Chapter 1."""
    return NumberPlane(
        x_range=list(x_range),
        y_range=list(y_range),
        x_length=x_length,
        y_length=y_length,
        background_line_style={"stroke_opacity": 0.28},
        axis_config={"include_numbers": include_numbers},
    )


def vector_arrow(
    plane: NumberPlane,
    end: Sequence[float],
    *,
    start: Sequence[float] = (0, 0),
    color=PRIMARY,
    stroke_width: float = 6,
) -> Arrow:
    """Create an arrow whose endpoints are specified in plane coordinates."""
    return Arrow(
        plane.c2p(*start),
        plane.c2p(*end),
        buff=0,
        color=color,
        stroke_width=stroke_width,
        max_tip_length_to_length_ratio=0.18,
    )


def labeled_vector(
    plane: NumberPlane,
    end: Sequence[float],
    label: str,
    *,
    color=PRIMARY,
) -> VGroup:
    arrow = vector_arrow(plane, end, color=color)
    tex = MathTex(label, color=color, font_size=32).next_to(arrow.get_end(), direction=(0.25, 0.25, 0))
    return VGroup(arrow, tex)


def matrix(rows: Sequence[Sequence[object]], *, scale: float = 0.82) -> Matrix:
    """A consistently sized Manim Matrix."""
    mob = Matrix([[str(value) for value in row] for row in rows], h_buff=0.9, v_buff=0.65)
    mob.scale(scale)
    return mob


def augmented_matrix_tex(rows: Sequence[Sequence[object]], *, font_size: int = 40) -> MathTex:
    """Create an augmented matrix from rows whose final entry is the RHS."""
    body_rows: list[str] = []
    for row in rows:
        values = [str(value) for value in row]
        left = " & ".join(values[:-1])
        body_rows.append(f"{left} & {values[-1]}")
    cols = "r" * (len(rows[0]) - 1) + "|r"
    latex = r"\left[\begin{array}{" + cols + "}" + r"\\".join(body_rows) + r"\end{array}\right]"
    return MathTex(latex, font_size=font_size)


def caption(text: str, *, font_size: int = 25) -> Text:
    return Text(text, font_size=font_size, color=MUTED)


def equation_chain(*items: str, font_size: int = 38) -> VGroup:
    """Stack MathTex expressions with uniform spacing."""
    mobs = [MathTex(item, font_size=font_size, color=TEXT) for item in items]
    return VGroup(*mobs).arrange(direction=(0, -1, 0), buff=0.28)
