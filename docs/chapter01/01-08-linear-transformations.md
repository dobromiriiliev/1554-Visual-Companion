# 1.8 An Introduction to Linear Transformations

**Course reference:** <https://cwarnockgt.github.io/MATH-1554---Course-Notes/sec-1-8.html>

## Visual question

**How does a matrix become a function?**

The matrix maps every input vector to an output while preserving linear combination structure.

## Implemented scenes

| Scene | Purpose |
|---|---|
| `DomainCodomainImageRange` | Distinguish domain, codomain, image, and range for a matrix transformation. |
| `ExistenceAndUniquenessUnderT` | Interpret existence and uniqueness of T(x)=b using earlier Ax=b ideas. |
| `ShearTransformation` | Animate a shear transformation on the entire coordinate grid. |
| `ProjectionAndRange` | Projection onto the x-axis shows that range can be smaller than codomain. |
| `LinearitySuperposition` | Visualize T(u+v)=T(u)+T(v) for a shear. |
| `BasisVectorsDetermineTransformation` | Knowing the images of the standard basis vectors determines the matrix. |

## Render one scene

```bash
math1554-render --section 1.8 --scene DomainCodomainImageRange --quality low --preview
```

## Teaching suggestion

Ask students to predict the geometric outcome before the final transformation appears. After the scene, reconnect the visual state to the notation in the course notes and solve a fresh example.

## Source-code location

```text
src/math1554_visuals/chapter01/section_01_08_linear_transformations/scenes.py
```
