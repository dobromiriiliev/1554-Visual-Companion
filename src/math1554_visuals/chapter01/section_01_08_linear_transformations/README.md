# 1.8 An Introduction to Linear Transformations

Course reference: <https://cwarnockgt.github.io/MATH-1554---Course-Notes/sec-1-8.html>

This package contains short, independent scenes for the section. Each class has one primary conceptual job so scenes can be reused in lecture, review material, or future course adapters.

## Scenes

| Scene | Purpose |
|---|---|
| `DomainCodomainImageRange` | Distinguish domain, codomain, image, and range for a matrix transformation. |
| `ExistenceAndUniquenessUnderT` | Interpret existence and uniqueness of T(x)=b using earlier Ax=b ideas. |
| `ShearTransformation` | Animate a shear transformation on the entire coordinate grid. |
| `ProjectionAndRange` | Projection onto the x-axis shows that range can be smaller than codomain. |
| `LinearitySuperposition` | Visualize T(u+v)=T(u)+T(v) for a shear. |
| `BasisVectorsDetermineTransformation` | Knowing the images of the standard basis vectors determines the matrix. |

## Render

```bash
math1554-render --section 1.8 --scene DomainCodomainImageRange --quality low --preview
```

Direct Manim invocation is also supported.
