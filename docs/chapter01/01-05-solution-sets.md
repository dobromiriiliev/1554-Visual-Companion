# 1.5 Solution Sets of Linear Systems

**Course reference:** <https://cwarnockgt.github.io/MATH-1554---Course-Notes/sec-1-5.html>

## Visual question

**What do free variables mean geometrically?**

They parameterize directions along an entire family of solutions.

## Implemented scenes

| Scene | Purpose |
|---|---|
| `HomogeneousAlwaysContainsZero` | Every homogeneous system A x = 0 has the trivial solution x = 0. |
| `FreeVariableCreatesDirection` | One free parameter traces a line of homogeneous solutions through the origin. |
| `ParametricVectorForm` | Convert a reduced system with one free variable into parametric vector form. |
| `HomogeneousVsInhomogeneousGeometry` | Compare a homogeneous solution line with a translated inhomogeneous solution line. |
| `TrivialVsNontrivialSolutions` | A homogeneous system has nontrivial solutions exactly when a free variable exists. |

## Render one scene

```bash
math1554-render --section 1.5 --scene HomogeneousAlwaysContainsZero --quality low --preview
```

## Teaching suggestion

Ask students to predict the geometric outcome before the final transformation appears. After the scene, reconnect the visual state to the notation in the course notes and solve a fresh example.

## Source-code location

```text
src/math1554_visuals/chapter01/section_01_05_solution_sets/scenes.py
```
