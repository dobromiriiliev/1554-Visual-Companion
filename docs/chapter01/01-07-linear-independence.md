# 1.7 Linear Independence

**Course reference:** <https://cwarnockgt.github.io/MATH-1554---Course-Notes/sec-1-7.html>

## Visual question

**What does dependence look like?**

A dependent vector adds no genuinely new direction because it can be reconstructed from the others.

## Implemented scenes

| Scene | Purpose |
|---|---|
| `IndependentVsDependent2D` | Nonparallel vectors are independent in R²; scalar multiples are dependent. |
| `OnlyTrivialCombination` | Linear independence means zero can be produced only by zero coefficients. |
| `DependenceRelation` | Construct a concrete nontrivial dependence relation among three vectors. |
| `PivotTestForIndependence` | A set of columns is independent iff A x = 0 has no free variables. |
| `TooManyVectorsInR2` | Three vectors in R² must be linearly dependent. |
| `ZeroVectorForcesDependence` | Any set containing the zero vector is linearly dependent. |

## Render one scene

```bash
math1554-render --section 1.7 --scene IndependentVsDependent2D --quality low --preview
```

## Teaching suggestion

Ask students to predict the geometric outcome before the final transformation appears. After the scene, reconnect the visual state to the notation in the course notes and solve a fresh example.

## Source-code location

```text
src/math1554_visuals/chapter01/section_01_07_linear_independence/scenes.py
```
