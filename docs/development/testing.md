# Testing

The repository separates tests that require Manim rendering from tests that only inspect source structure.

## Fast checks

```bash
ruff check src tests scripts
python -m pytest
python scripts/validate_repository.py
```

These checks should run without rendering all scenes.

## Why AST-based tests?

Importing a scene module imports Manim and therefore requires native rendering dependencies. Structural tests parse Python source with `ast` so CI can verify scene names, docstrings, uniqueness, and repository completeness cheaply.

## Render review

Before merging a visual change, render the changed scene locally at low quality, then at high quality for final review.

Check:

- clipping;
- overlapping labels;
- mathematical correctness;
- sufficient dwell time;
- color-independent meaning;
- readable final frame.
