# Scene catalog

This page is generated from scene class names and docstrings. **42 scenes** are currently discoverable.

> Regenerate with `python scripts/generate_scene_catalog.py`.

## 1.1 — Systems of Linear Equations

### `LinearEquationAsLine`

A single linear equation in two variables is a line of solutions.

```bash
math1554-render --section 1.1 --scene LinearEquationAsLine --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_01_systems_of_linear_equations/scenes.py`

### `SolutionCountCases`

Two linear equations can have zero, one, or infinitely many solutions.

```bash
math1554-render --section 1.1 --scene SolutionCountCases --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_01_systems_of_linear_equations/scenes.py`

### `PlaneIntersectionCases`

Show that two nonparallel planes in R^3 intersect in a line.

```bash
math1554-render --section 1.1 --scene PlaneIntersectionCases --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_01_systems_of_linear_equations/scenes.py`

### `EquationsToAugmentedMatrix`

Morph the information in equations into augmented-matrix notation.

```bash
math1554-render --section 1.1 --scene EquationsToAugmentedMatrix --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_01_systems_of_linear_equations/scenes.py`

### `ElementaryRowOperations`

Show the three legal elementary row operations.

```bash
math1554-render --section 1.1 --scene ElementaryRowOperations --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_01_systems_of_linear_equations/scenes.py`

### `RowOperationsPreserveSolutionSet`

Geometrically show why replacing an equation can preserve the common solution.

```bash
math1554-render --section 1.1 --scene RowOperationsPreserveSolutionSet --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_01_systems_of_linear_equations/scenes.py`

### `ConsistencyAndUniqueness`

Read no/unique/infinite solutions directly from reduced augmented matrices.

```bash
math1554-render --section 1.1 --scene ConsistencyAndUniqueness --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_01_systems_of_linear_equations/scenes.py`

## 1.2 — Row Reduction and Echelon Forms

### `REFvsRREF`

Build the visual checklist that distinguishes REF from RREF.

```bash
math1554-render --section 1.2 --scene REFvsRREF --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_02_row_reduction_and_echelon_forms/scenes.py`

### `PivotPositionsAndColumns`

Identify pivot positions and distinguish pivot columns from free columns.

```bash
math1554-render --section 1.2 --scene PivotPositionsAndColumns --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_02_row_reduction_and_echelon_forms/scenes.py`

### `RowReductionAlgorithm`

Animate a complete row-reduction sequence to RREF.

```bash
math1554-render --section 1.2 --scene RowReductionAlgorithm --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_02_row_reduction_and_echelon_forms/scenes.py`

### `PivotAndFreeVariables`

Connect pivot columns to pivot variables and the remaining columns to free variables.

```bash
math1554-render --section 1.2 --scene PivotAndFreeVariables --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_02_row_reduction_and_echelon_forms/scenes.py`

### `ExistenceAndUniquenessFlowchart`

Turn Theorem 1.20 into a compact decision tree.

```bash
math1554-render --section 1.2 --scene ExistenceAndUniquenessFlowchart --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_02_row_reduction_and_echelon_forms/scenes.py`

### `PolynomialInterpolation`

Use a linear system to recover the coefficients of a polynomial.

```bash
math1554-render --section 1.2 --scene PolynomialInterpolation --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_02_row_reduction_and_echelon_forms/scenes.py`

## 1.3 — Vector Equations

### `PointVsVector`

The ordered pair (3,2) can be viewed as a point or as a vector from the origin.

```bash
math1554-render --section 1.3 --scene PointVsVector --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_03_vector_equations/scenes.py`

### `ScalarMultiplication`

Positive scalars stretch/compress; negative scalars also reverse direction.

```bash
math1554-render --section 1.3 --scene ScalarMultiplication --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_03_vector_equations/scenes.py`

### `VectorAdditionParallelogram`

Visualize vector addition using head-to-tail and parallelogram constructions.

```bash
math1554-render --section 1.3 --scene VectorAdditionParallelogram --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_03_vector_equations/scenes.py`

### `LinearCombinationBuildsTarget`

Build a target vector from weighted copies of two source vectors.

```bash
math1554-render --section 1.3 --scene LinearCombinationBuildsTarget --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_03_vector_equations/scenes.py`

### `SpanOfOneVector`

All scalar multiples of one nonzero vector form a line through the origin.

```bash
math1554-render --section 1.3 --scene SpanOfOneVector --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_03_vector_equations/scenes.py`

### `SpanOfTwoVectors`

Two nonparallel vectors in R² can generate the whole plane.

```bash
math1554-render --section 1.3 --scene SpanOfTwoVectors --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_03_vector_equations/scenes.py`

### `SpanMembershipAsSystem`

Membership in a span is equivalent to solvability of a linear system.

```bash
math1554-render --section 1.3 --scene SpanMembershipAsSystem --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_03_vector_equations/scenes.py`

## 1.4 — The Matrix Equation Ax = b

### `DimensionsOfAx`

Show how the dimensions of A, x, and b must fit together.

```bash
math1554-render --section 1.4 --scene DimensionsOfAx --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_04_matrix_equation/scenes.py`

### `MatrixVectorAsColumnCombination`

Matrix-vector multiplication is a linear combination of the columns of A.

```bash
math1554-render --section 1.4 --scene MatrixVectorAsColumnCombination --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_04_matrix_equation/scenes.py`

### `FourEquivalentRepresentations`

Cycle through the four equivalent ways to encode the same linear system.

```bash
math1554-render --section 1.4 --scene FourEquivalentRepresentations --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_04_matrix_equation/scenes.py`

### `ColumnSpanAndExistence`

A x = b is solvable exactly when b lies in the span of A's columns.

```bash
math1554-render --section 1.4 --scene ColumnSpanAndExistence --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_04_matrix_equation/scenes.py`

### `ConsistentForEveryB`

In R², compare a one-dimensional column span with a full two-dimensional span.

```bash
math1554-render --section 1.4 --scene ConsistentForEveryB --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_04_matrix_equation/scenes.py`

## 1.5 — Solution Sets of Linear Systems

### `HomogeneousAlwaysContainsZero`

Every homogeneous system A x = 0 has the trivial solution x = 0.

```bash
math1554-render --section 1.5 --scene HomogeneousAlwaysContainsZero --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_05_solution_sets/scenes.py`

### `FreeVariableCreatesDirection`

One free parameter traces a line of homogeneous solutions through the origin.

```bash
math1554-render --section 1.5 --scene FreeVariableCreatesDirection --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_05_solution_sets/scenes.py`

### `ParametricVectorForm`

Convert a reduced system with one free variable into parametric vector form.

```bash
math1554-render --section 1.5 --scene ParametricVectorForm --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_05_solution_sets/scenes.py`

### `HomogeneousVsInhomogeneousGeometry`

Compare a homogeneous solution line with a translated inhomogeneous solution line.

```bash
math1554-render --section 1.5 --scene HomogeneousVsInhomogeneousGeometry --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_05_solution_sets/scenes.py`

### `TrivialVsNontrivialSolutions`

A homogeneous system has nontrivial solutions exactly when a free variable exists.

```bash
math1554-render --section 1.5 --scene TrivialVsNontrivialSolutions --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_05_solution_sets/scenes.py`

## 1.7 — Linear Independence

### `IndependentVsDependent2D`

Nonparallel vectors are independent in R²; scalar multiples are dependent.

```bash
math1554-render --section 1.7 --scene IndependentVsDependent2D --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_07_linear_independence/scenes.py`

### `OnlyTrivialCombination`

Linear independence means zero can be produced only by zero coefficients.

```bash
math1554-render --section 1.7 --scene OnlyTrivialCombination --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_07_linear_independence/scenes.py`

### `DependenceRelation`

Construct a concrete nontrivial dependence relation among three vectors.

```bash
math1554-render --section 1.7 --scene DependenceRelation --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_07_linear_independence/scenes.py`

### `PivotTestForIndependence`

A set of columns is independent iff A x = 0 has no free variables.

```bash
math1554-render --section 1.7 --scene PivotTestForIndependence --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_07_linear_independence/scenes.py`

### `TooManyVectorsInR2`

Three vectors in R² must be linearly dependent.

```bash
math1554-render --section 1.7 --scene TooManyVectorsInR2 --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_07_linear_independence/scenes.py`

### `ZeroVectorForcesDependence`

Any set containing the zero vector is linearly dependent.

```bash
math1554-render --section 1.7 --scene ZeroVectorForcesDependence --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_07_linear_independence/scenes.py`

## 1.8 — An Introduction to Linear Transformations

### `DomainCodomainImageRange`

Distinguish domain, codomain, image, and range for a matrix transformation.

```bash
math1554-render --section 1.8 --scene DomainCodomainImageRange --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_08_linear_transformations/scenes.py`

### `ExistenceAndUniquenessUnderT`

Interpret existence and uniqueness of T(x)=b using earlier Ax=b ideas.

```bash
math1554-render --section 1.8 --scene ExistenceAndUniquenessUnderT --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_08_linear_transformations/scenes.py`

### `ShearTransformation`

Animate a shear transformation on the entire coordinate grid.

```bash
math1554-render --section 1.8 --scene ShearTransformation --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_08_linear_transformations/scenes.py`

### `ProjectionAndRange`

Projection onto the x-axis shows that range can be smaller than codomain.

```bash
math1554-render --section 1.8 --scene ProjectionAndRange --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_08_linear_transformations/scenes.py`

### `LinearitySuperposition`

Visualize T(u+v)=T(u)+T(v) for a shear.

```bash
math1554-render --section 1.8 --scene LinearitySuperposition --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_08_linear_transformations/scenes.py`

### `BasisVectorsDetermineTransformation`

Knowing the images of the standard basis vectors determines the matrix.

```bash
math1554-render --section 1.8 --scene BasisVectorsDetermineTransformation --quality low --preview
```

Source: `src/math1554_visuals/chapter01/section_01_08_linear_transformations/scenes.py`
