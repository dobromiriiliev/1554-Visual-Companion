# 1.3 Vector Equations

**Course reference:** <https://cwarnockgt.github.io/MATH-1554---Course-Notes/sec-1-3.html>

## Visual question

**What does a linear combination physically build?**

Scalar multiples create directions and vector addition combines them into reachable points.

## Implemented scenes

| Scene | Purpose |
|---|---|
| `PointVsVector` | The ordered pair (3,2) can be viewed as a point or as a vector from the origin. |
| `ScalarMultiplication` | Positive scalars stretch/compress; negative scalars also reverse direction. |
| `VectorAdditionParallelogram` | Visualize vector addition using head-to-tail and parallelogram constructions. |
| `LinearCombinationBuildsTarget` | Build a target vector from weighted copies of two source vectors. |
| `SpanOfOneVector` | All scalar multiples of one nonzero vector form a line through the origin. |
| `SpanOfTwoVectors` | Two nonparallel vectors in R² can generate the whole plane. |
| `SpanMembershipAsSystem` | Membership in a span is equivalent to solvability of a linear system. |

## Render one scene

```bash
math1554-render --section 1.3 --scene PointVsVector --quality low --preview
```

## Teaching suggestion

Ask students to predict the geometric outcome before the final transformation appears. After the scene, reconnect the visual state to the notation in the course notes and solve a fresh example.

## Source-code location

```text
src/math1554_visuals/chapter01/section_01_03_vector_equations/scenes.py
```
