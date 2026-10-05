# 1.1 Systems of Linear Equations

**Course reference:** <https://cwarnockgt.github.io/MATH-1554---Course-Notes/Section-1-1.html>

## Visual question

**How can simultaneous equations be seen as geometry?**

Treat each equation as a solution set and the system as their intersection.

## Implemented scenes

| Scene | Purpose |
|---|---|
| `LinearEquationAsLine` | A single linear equation in two variables is a line of solutions. |
| `SolutionCountCases` | Two linear equations can have zero, one, or infinitely many solutions. |
| `PlaneIntersectionCases` | In R^3, two planes can miss, coincide, or meet in a line. |
| `EquationsToAugmentedMatrix` | Morph the information in equations into augmented-matrix notation. |
| `ElementaryRowOperations` | Show the three legal elementary row operations. |
| `RowOperationsPreserveSolutionSet` | Geometrically show why replacing an equation can preserve the common solution. |
| `ConsistencyAndUniqueness` | Read no/unique/infinite solutions directly from reduced augmented matrices. |

## Render one scene

```bash
math1554-render --section 1.1 --scene LinearEquationAsLine --quality low --preview
```

## Teaching suggestion

Ask students to predict the geometric outcome before the final transformation appears. After the scene, reconnect the visual state to the notation in the course notes and solve a fresh example.

## Source-code location

```text
src/math1554_visuals/chapter01/section_01_01_systems_of_linear_equations/scenes.py
```
