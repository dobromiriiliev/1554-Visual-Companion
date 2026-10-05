# 1.4 The Matrix Equation Ax = b

**Course reference:** <https://cwarnockgt.github.io/MATH-1554---Course-Notes/sec-1-4.html>

## Visual question

**What is matrix-vector multiplication really doing?**

It forms a weighted sum of the columns of the matrix.

## Implemented scenes

| Scene | Purpose |
|---|---|
| `DimensionsOfAx` | Show how the dimensions of A, x, and b must fit together. |
| `MatrixVectorAsColumnCombination` | Matrix-vector multiplication is a linear combination of the columns of A. |
| `FourEquivalentRepresentations` | Cycle through the four equivalent ways to encode the same linear system. |
| `ColumnSpanAndExistence` | A x = b is solvable exactly when b lies in the span of A's columns. |
| `ConsistentForEveryB` | In R², compare a one-dimensional column span with a full two-dimensional span. |

## Render one scene

```bash
math1554-render --section 1.4 --scene DimensionsOfAx --quality low --preview
```

## Teaching suggestion

Ask students to predict the geometric outcome before the final transformation appears. After the scene, reconnect the visual state to the notation in the course notes and solve a fresh example.

## Source-code location

```text
src/math1554_visuals/chapter01/section_01_04_matrix_equation/scenes.py
```
