# 1.2 Row Reduction and Echelon Forms

**Course reference:** <https://cwarnockgt.github.io/MATH-1554---Course-Notes/sec-1-2.html>

## Visual question

**What information survives row reduction?**

The representation changes, but the solution set does not; pivots expose structure.

## Implemented scenes

| Scene | Purpose |
|---|---|
| `REFvsRREF` | Build the visual checklist that distinguishes REF from RREF. |
| `PivotPositionsAndColumns` | Identify pivot positions and distinguish pivot columns from free columns. |
| `RowReductionAlgorithm` | Animate a complete row-reduction sequence to RREF. |
| `PivotAndFreeVariables` | Connect pivot columns to pivot variables and the remaining columns to free variables. |
| `ExistenceAndUniquenessFlowchart` | Turn Theorem 1.20 into a compact decision tree. |
| `PolynomialInterpolation` | Use a linear system to recover the coefficients of a polynomial. |

## Render one scene

```bash
math1554-render --section 1.2 --scene REFvsRREF --quality low --preview
```

## Teaching suggestion

Ask students to predict the geometric outcome before the final transformation appears. After the scene, reconnect the visual state to the notation in the course notes and solve a fresh example.

## Source-code location

```text
src/math1554_visuals/chapter01/section_01_02_row_reduction_and_echelon_forms/scenes.py
```
