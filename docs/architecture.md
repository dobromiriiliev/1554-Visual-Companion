# Architecture

The repository separates **curriculum mapping**, **reusable visuals**, and **course-specific scenes**.

```text
course_map.yaml
      │
      ├── section order / objectives / source references
      │
      v
src/math1554_visuals/chapter01/
      │
      ├── course-specific scene composition
      │
      v
src/math1554_visuals/common/
      │
      └── reusable layout / theme / vector / matrix helpers
```

## `common/`

Contains stable visual language:

- base scene classes;
- semantic colors;
- coordinate-plane helpers;
- vector arrows;
- matrix helpers;
- shared captions and layouts.

## Section packages

Each section owns:

- `scenes.py` — Manim scene classes;
- `README.md` — learning intent and local render examples;
- `__init__.py` — package marker.

## Scene discovery

`math1554_visuals.catalog` parses section source files with Python's AST rather than importing them. This allows documentation and development tools to list scenes even on a machine that has not finished installing Manim's native dependencies.

## CLI

`math1554_visuals.cli` provides:

- `math1554-scenes` — discover scenes;
- `math1554-render` — resolve a section and render a named scene;
- `math1554-doctor` — check environment prerequisites.

## Future course adapters

The desired long-term boundary is:

```text
concept visual library
        ↑
course adapter / mapping
        ↑
course-specific documentation
```

That lets multiple curricula reuse the same visual concept without forcing them into the same sequence.
