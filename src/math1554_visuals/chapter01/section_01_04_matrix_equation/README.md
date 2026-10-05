# 1.4 The Matrix Equation Ax = b

Course reference: <https://cwarnockgt.github.io/MATH-1554---Course-Notes/sec-1-4.html>

This package contains short, independent scenes for the section. Each class has one primary conceptual job so scenes can be reused in lecture, review material, or future course adapters.

## Scenes

| Scene | Purpose |
|---|---|
| `DimensionsOfAx` | Show how the dimensions of A, x, and b must fit together. |
| `MatrixVectorAsColumnCombination` | Matrix-vector multiplication is a linear combination of the columns of A. |
| `FourEquivalentRepresentations` | Cycle through the four equivalent ways to encode the same linear system. |
| `ColumnSpanAndExistence` | A x = b is solvable exactly when b lies in the span of A's columns. |
| `ConsistentForEveryB` | In R², compare a one-dimensional column span with a full two-dimensional span. |

## Render

```bash
math1554-render --section 1.4 --scene DimensionsOfAx --quality low --preview
```

Direct Manim invocation is also supported.
