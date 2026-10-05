"""Central visual language for the MATH 1554 visual companion."""

from manim import BLUE_C, GOLD_C, GREEN_C, GREY_B, RED_C, TEAL_C, WHITE

BACKGROUND = "#0f111a"
TEXT = WHITE
MUTED = GREY_B
PRIMARY = BLUE_C
SECONDARY = GOLD_C
SOLUTION = GREEN_C
WARNING = RED_C
ACCENT = TEAL_C

# Semantic aliases. Keeping these names stable makes it easy to change the palette later.
VECTOR_U = PRIMARY
VECTOR_V = SECONDARY
VECTOR_W = ACCENT
PIVOT = SOLUTION
FREE = SECONDARY
INCONSISTENT = WARNING
