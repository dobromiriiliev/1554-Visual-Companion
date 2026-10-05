# MATH 1554 Visual Companion

> **A course-synchronous, open-source visual layer for linear algebra.**  
> 42 Manim scenes currently cover every published section in Chapter 1 of Georgia Tech's MATH 1554 notes.

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Manim](https://img.shields.io/badge/Manim-0.21.0-58C4DD)
![License](https://img.shields.io/badge/License-MIT-green)
![Chapter 1](https://img.shields.io/badge/Chapter%201-42%20scenes-success)

## The idea

Linear algebra is often taught through excellent symbolic notes and excellent visual intuition—but those two resources are not always synchronized. This project bridges that gap.

The **MATH 1554 Visual Companion** follows the order and learning goals of Georgia Tech's public MATH 1554 course notes while adding original, reusable Manim animations that make geometric structure visible at the exact moment it appears in the course.

The project is designed around a simple learning loop:

```text
course objective -> geometric intuition -> animation -> symbolic computation
```

The goal is **not** to replace lecture notes, instructors, textbooks, or 3Blue1Brown. The goal is to create a visual companion that a student can use *alongside* the course without having to translate between different topic orders or notation systems.

## Why this repository exists

Students can often perform row reduction before they understand why it preserves a solution set, compute a span before they can picture what is being spanned, or multiply a matrix by a vector before they see that the product is a weighted sum of columns.

This repository treats those moments as visualization opportunities.

Examples include:

- a system of equations becoming intersecting geometric constraints;
- row replacement changing one equation while preserving the common solution;
- free variables becoming directions of motion through a solution set;
- `Ax=b` assembling `b` from the columns of `A`;
- linear dependence appearing as a redundant direction;
- a matrix transformation moving an entire coordinate grid;
- the images of basis vectors determining the full transformation.

## Project status

**Chapter 1 is implemented as the first complete development milestone.**

| Section | Topic | Scenes | Status |
|---|---|---:|---|
| 1.1 | Systems of Linear Equations | 7 | Implemented |
| 1.2 | Row Reduction and Echelon Forms | 6 | Implemented |
| 1.3 | Vector Equations | 7 | Implemented |
| 1.4 | The Matrix Equation `Ax=b` | 5 | Implemented |
| 1.5 | Solution Sets of Linear Systems | 5 | Implemented |
| 1.7 | Linear Independence | 6 | Implemented |
| 1.8 | An Introduction to Linear Transformations | 6 | Implemented |

The numbering intentionally follows the published course-note sequence; Chapter 1 does not include a Section 1.6.

## Quick start

### 1. Clone and enter the repository

```bash
git clone <your-repository-url>
cd 1554-Visual-Companion
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 3. Install the project

```bash
python -m pip install -e ".[dev]"
```

> Run the install command from the **repository root**—the directory containing `pyproject.toml` and `README.md`—not from `src/`.

Manim also requires system dependencies such as FFmpeg and a TeX installation for `MathTex`. See the [official Manim installation guide](https://docs.manim.community/en/stable/installation.html) for your platform.

### 4. Check your environment

```bash
python scripts/doctor.py
```

### 5. Discover available scenes

```bash
python scripts/list_scenes.py
```

or, after installation:

```bash
math1554-scenes
```

### 6. Render a scene

```bash
math1554-render --section 1.1 --scene SolutionCountCases --quality low --preview
```

The direct Manim command also works:

```bash
manim -pql   src/math1554_visuals/chapter01/section_01_01_systems_of_linear_equations/scenes.py   SolutionCountCases
```

## Who this is for

### Students

Use the scenes as a visual companion while moving through MATH 1554. Each section has a dedicated README explaining what its scenes are intended to communicate.

### Instructors and TAs

Render individual scenes for lecture, recitation, review material, or office-hour explanations. Scenes are intentionally short and modular rather than being full lecture videos.

### Animators and developers

Reuse the common visual primitives, improve scene composition, add accessibility features, or build new course mappings.

### Other universities

The long-term architecture separates reusable visualization code from course-specific ordering. A future course adapter can map the same visual library to another linear algebra syllabus without duplicating every animation.

## Repository map

```text
1554-Visual-Companion/
├── .github/                 # issue forms, PR template, CI, docs workflows
├── docs/                    # public documentation site source
├── examples/                # small standalone examples
├── scripts/                 # contributor and rendering utilities
├── src/math1554_visuals/
│   ├── common/              # reusable visual language
│   └── chapter01/           # course-synchronous Chapter 1 scenes
├── tests/                   # repository and catalog checks
├── ATTRIBUTION.md
├── CHANGELOG.md
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── PROJECT_CHARTER.md
├── ROADMAP.md
├── SECURITY.md
├── SUPPORT.md
├── course_map.yaml
├── mkdocs.yml
├── pyproject.toml
└── README.md
```

## Design principles

1. **Course-synchronous** — visualization should appear where the course introduces the idea.
2. **Original explanations** — link to source material; do not republish course-note prose.
3. **Geometry before memorization** — make structure visible before adding rules.
4. **One concept per scene** — scenes should be composable and easy to reuse.
5. **Semantic color** — visual meaning should remain consistent across chapters.
6. **Symbolic connection** — animations should reconnect to the algebra students must perform.
7. **Accessible by default** — meaning should never depend on color alone.
8. **Course-independent primitives** — reusable ideas belong in `common/`, not copied across sections.

Read the full philosophy in [`docs/design-principles.md`](docs/design-principles.md).

## Chapter 1 scene catalog

The repository currently contains **42 scenes**. A generated catalog with descriptions and render commands lives at [`docs/reference/scene-catalog.md`](docs/reference/scene-catalog.md).

A few good entry points:

- `SolutionCountCases` — zero, one, or infinitely many solutions;
- `RowOperationsPreserveSolutionSet` — why row replacement preserves the shared solution;
- `SpanOfTwoVectors` — how two independent vectors fill the plane;
- `FourEquivalentRepresentations` — system / vector / matrix / augmented forms;
- `ParametricVectorForm` — free variables as geometric directions;
- `IndependentVsDependent2D` — redundancy as linear dependence;
- `ShearTransformation` — a matrix acting on the entire coordinate grid.

## Contributing

Contributions are welcome from students, educators, animators, and developers. You do **not** need to be an expert in all four areas.

Good contributions include:

- improving a scene's mathematical clarity;
- adding a missing visual explanation;
- fixing layout or rendering problems;
- writing tests or documentation;
- improving accessibility;
- creating reusable helpers;
- reviewing examples for correctness;
- proposing mappings for later chapters.

Start with [`CONTRIBUTING.md`](CONTRIBUTING.md). The fastest first contribution is usually to render one scene, identify one confusing visual choice, and improve it.

## Documentation website

The documentation is built with MkDocs Material.

```bash
python -m pip install -e ".[docs]"
mkdocs serve
```

Then open the local address printed by MkDocs.

## Project boundaries and attribution

This is an **unofficial** project and is **not affiliated with or endorsed by Georgia Tech, the authors of the MATH 1554 notes, 3Blue1Brown, Grant Sanderson, or the Manim Community**.

The repository:

- links to Georgia Tech's public course notes as a curriculum reference;
- creates original examples, prose, code, and animations;
- uses Manim Community Edition as the animation engine;
- does not redistribute Georgia Tech course-note text;
- does not copy 3Blue1Brown video footage, scripts, characters, or visual assets.

See [`ATTRIBUTION.md`](ATTRIBUTION.md) and [`docs/licensing-and-attribution.md`](docs/licensing-and-attribution.md).

## License

Project code and original project documentation are released under the [MIT License](LICENSE), unless a file states otherwise.

## Citation

If this repository becomes useful in teaching, research, or educational tooling, citation metadata is provided in [`CITATION.cff`](CITATION.cff).

## Roadmap

Chapter 1 is the foundation. The broader plan is to:

1. polish and classroom-test Chapter 1;
2. expand section-by-section through the rest of MATH 1554;
3. build a reusable linear-algebra visualization library;
4. add course mappings for other curricula;
5. publish a searchable web gallery of scenes and concepts.

See [`ROADMAP.md`](ROADMAP.md) for the full roadmap.
