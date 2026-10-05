# Roadmap

This roadmap describes direction rather than a promise of dates.

## Phase 0 — Repository foundation

- [x] `src/` package layout
- [x] reusable visual theme and base scenes
- [x] contributor documentation
- [x] automated scene discovery
- [x] issue / PR templates
- [x] CI and documentation workflows
- [x] licensing and attribution boundaries

## Phase 1 — Chapter 1 complete

- [x] 1.1 Systems of Linear Equations
- [x] 1.2 Row Reduction and Echelon Forms
- [x] 1.3 Vector Equations
- [x] 1.4 The Matrix Equation `Ax=b`
- [x] 1.5 Solution Sets of Linear Systems
- [x] 1.7 Linear Independence
- [x] 1.8 An Introduction to Linear Transformations
- [ ] render-review every scene at 1080p
- [ ] collect student / TA feedback
- [ ] add captions or companion narration notes for every scene
- [ ] add thumbnail stills to the docs gallery

## Phase 2 — Remaining MATH 1554 content

Build subsequent chapters section-by-section using the same pattern:

1. map course objectives;
2. identify visualization opportunities;
3. implement small scenes;
4. refactor repeated visuals into `common/`;
5. test with students;
6. document the conceptual bridge to computation.

High-value future concepts include:

- subspaces and bases;
- determinants as area / volume scaling;
- eigenvectors and invariant directions;
- diagonalization;
- orthogonality and projections;
- Gram-Schmidt;
- least squares;
- symmetric matrices and quadratic forms;
- singular value decomposition.

## Phase 3 — Reusable visualization library

Extract stable visual components that are not specific to MATH 1554:

- vector-space panels;
- span visualizers;
- row-operation animations;
- pivot / free-variable overlays;
- transformation grids;
- eigendirection visualizers;
- projection and least-squares diagrams;
- matrix factorization compositions.

## Phase 4 — Course adapters

Separate concept assets from curriculum order so other courses can define mappings such as:

```text
courses/
├── gatech-math-1554/
├── gatech-math-1553/
├── mit-18-06/
└── community-linear-algebra/
```

A course adapter should describe ordering, terminology, and recommended scenes without forking the core animation code.

## Phase 5 — Public gallery

A lightweight website could eventually provide:

- concept search;
- section-by-section browsing;
- embedded rendered clips;
- source-code links;
- educator notes;
- accessibility metadata;
- course mappings;
- contributor credits.

## Research / evaluation opportunities

Potential future evaluation work:

- pre/post concept questions around selected visualizations;
- student confidence surveys;
- comparison of visual + symbolic versus symbolic-only review;
- misconception tagging for scenes;
- usability studies for course-synchronous navigation.
