# Updating an Existing Checkout

If you already created a Git repository for an earlier version of this project, you do **not** need to replace the `.git` directory.

## Safest approach

1. Commit or back up your current work.
2. Extract the new project bundle beside your existing repository.
3. Copy the bundle's contents into the existing repository root while preserving the existing `.git/` directory.
4. Confirm that these files are at the root:

```text
README.md
pyproject.toml
Makefile
src/
docs/
tests/
```

5. Remove any accidental `src/pyproject.toml` or `src/Makefile` left from the earlier layout.
6. Recreate or reactivate your virtual environment.
7. Run:

```bash
python -m pip install -e ".[dev,docs]"
python scripts/doctor.py
python scripts/validate_repository.py
python -m pytest
```

## macOS / Linux merge example

From the parent directory of both folders:

```bash
rsync -av --exclude='.git' \
  1554-Visual-Companion-Open-Source/ \
  1554-Visual-Companion/
```

Then enter the existing repository and inspect `git status` before committing.

## Do not copy generated caches

The supplied bundle excludes Python caches and Manim render output. Keep `.venv/`, `media/`, and `site/` local; they are ignored by Git.
