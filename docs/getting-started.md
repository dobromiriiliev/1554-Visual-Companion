# Getting started

## Prerequisites

- Python 3.11 or newer;
- FFmpeg;
- a TeX installation for `MathTex` scenes;
- a supported local Manim environment.

For platform-specific native dependencies, use the official Manim installation documentation.

## Create an environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

On Windows PowerShell, activate with the appropriate `.venv\Scripts\Activate.ps1` command instead.

## Install

From the directory containing `pyproject.toml`:

```bash
python -m pip install -e ".[dev]"
```

If pip says it is obtaining `.../src`, stop and check your working directory. It should obtain the repository root, not the `src` directory.

## Diagnose the environment

```bash
python scripts/doctor.py
```

The doctor checks:

- Python version;
- `ffmpeg` availability;
- `latex` availability;
- whether Manim imports;
- whether you are running from a valid repository layout.

## List scenes

```bash
python scripts/list_scenes.py
```

## Render

```bash
python scripts/render_scene.py   --section 1.1   --scene SolutionCountCases   --quality low   --preview
```

Quality choices are `low`, `medium`, `high`, and `4k`.

## Next steps

- browse the [scene catalog](reference/scene-catalog.md);
- read [scene authoring](scene-authoring.md) before adding a new animation;
- use [Chapter 1](chapter01/index.md) to understand the conceptual sequence.
