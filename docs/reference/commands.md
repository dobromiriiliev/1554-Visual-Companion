# Command reference

## Environment

```bash
python scripts/doctor.py
```

## Scene discovery

```bash
python scripts/list_scenes.py
python scripts/list_scenes.py --section 1.7
```

Installed command:

```bash
math1554-scenes --section 1.7
```

## Rendering

```bash
python scripts/render_scene.py --section 1.8 --scene ShearTransformation --quality low --preview
```

Installed command:

```bash
math1554-render --section 1.8 --scene ShearTransformation --quality high
```

## Tests

```bash
python -m pytest
```

## Lint

```bash
ruff check src tests scripts
```

## Repository validation

```bash
python scripts/validate_repository.py
```

## Scene catalog

```bash
python scripts/generate_scene_catalog.py
```

## Documentation

```bash
mkdocs serve
mkdocs build --strict
```
