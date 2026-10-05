# Contributing

Thank you for helping make linear algebra easier to see.

This repository welcomes contributions from students, educators, animators, designers, and software developers. You do not need to be an expert in every part of the stack.

## Ways to contribute

### Mathematics

- check an example for correctness;
- suggest a misconception that deserves a visualization;
- connect a scene more explicitly to a theorem or computation;
- identify a case the animation currently hides.

### Animation

- improve pacing or composition;
- add a visual transition that clarifies an equivalence;
- make 3D scenes easier to read;
- create reusable visual primitives.

### Software

- improve test coverage;
- simplify duplicated scene code;
- improve rendering utilities;
- fix packaging or platform issues;
- improve CI.

### Documentation

- clarify setup instructions;
- add instructor notes;
- document a scene's intended learning objective;
- improve accessibility guidance;
- add troubleshooting information.

## Development setup

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev,docs]"
pre-commit install
python scripts/doctor.py
```

Manim has operating-system dependencies. Follow the official Manim installation documentation if `doctor.py` reports that FFmpeg, LaTeX, or Manim is unavailable.

## Important: run commands from the repository root

The correct working directory contains:

```text
README.md
pyproject.toml
src/
tests/
```

Do not run `pip install -e ".[dev]"` from inside `src/`.

## Find a scene

```bash
python scripts/list_scenes.py
```

Filter by section:

```bash
python scripts/list_scenes.py --section 1.3
```

## Render a scene

```bash
python scripts/render_scene.py   --section 1.3   --scene SpanOfTwoVectors   --quality low   --preview
```

Use low quality while iterating. Render high quality only when reviewing a finished scene.

## Scene design checklist

Before coding, be able to answer:

1. **What exact idea should become visible?**
2. **What student misconception does this address?**
3. **What symbolic expression should the animation reconnect to?**
4. **Can the scene communicate without narration?**
5. **Does color carry meaning that also needs a label, shape, or position cue?**

## Code conventions

### One primary idea per class

Prefer:

```python
class SpanOfTwoVectors(CourseScene):
    ...
```

over one giant scene that teaches an entire section.

### Descriptive class names

Class names become public API: they appear in commands, documentation, and scene catalogs.

Use `RowOperationsPreserveSolutionSet`, not `Scene4`.

### Add a class docstring

The first sentence becomes the generated scene-catalog description.

```python
class PivotAndFreeVariables(CourseScene):
    """Distinguish pivot variables from free variables in an echelon system."""
```

### Prefer semantic theme colors

Use names from `common/theme.py` such as `PRIMARY`, `SOLUTION`, `WARNING`, `PIVOT`, and `FREE` instead of hard-coded colors.

### Promote repetition carefully

Start concrete. Move an object or helper into `common/` when it is genuinely reused by multiple sections.

## Mathematical examples

Examples must be original to this repository unless their license clearly permits reuse and attribution is documented.

When matching the course:

- preserve the concept and terminology;
- do not copy substantial prose from the course notes;
- do not reproduce entire worked examples verbatim;
- link to the original section instead.

## 3Blue1Brown / Manim boundary

Using Manim is encouraged. Copying 3Blue1Brown video assets, scripts, Pi creatures, or scene compositions is not part of this project.

Build original visual explanations inspired by the broader idea of visual mathematics.

## Testing

Run:

```bash
make check
```

At minimum, a pull request changing scenes should pass:

```bash
ruff check src tests scripts
python -m pytest
python scripts/validate_repository.py
```

When practical, also render the changed scene and include a still or short clip in the pull request description.

## Documentation

If you add a concept or scene, update at least one of:

- the section README;
- the section page under `docs/chapter01/`;
- `course_map.yaml` if the curriculum mapping changes.

Then regenerate the catalog:

```bash
make catalog
```

## Pull requests

A strong pull request explains:

- the learning objective;
- what changed visually;
- why the change improves understanding;
- how it was tested;
- whether it changes public scene names.

Small focused PRs are easier to review than large mixed changes.

## Review priorities

Reviewers should prioritize, in this order:

1. mathematical correctness;
2. pedagogical clarity;
3. accessibility and legibility;
4. maintainability;
5. visual polish.

A beautiful but misleading animation should not merge.

## New sections

Use:

```bash
python scripts/new_section.py --help
```

The generated section is only a scaffold. A section is not considered complete until it has learning goals, scene documentation, tests, and render-reviewed scenes.

## Credit

Contributors are encouraged to add their name to `CONTRIBUTORS.md` in the same pull request as their first substantive contribution.
