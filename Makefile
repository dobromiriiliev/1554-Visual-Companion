PYTHON ?= python
MANIM ?= manim
SECTION ?= 1.1
SCENE ?= SolutionCountCases
QUALITY ?= low

.PHONY: help install install-dev install-docs doctor scenes preview render test lint format check docs docs-build catalog clean tree

help:
	@echo "MATH 1554 Visual Companion"
	@echo ""
	@echo "Setup"
	@echo "  make install        Install runtime dependencies"
	@echo "  make install-dev    Install contributor dependencies"
	@echo "  make install-docs   Install documentation dependencies"
	@echo "  make doctor         Check Python, FFmpeg, LaTeX, and Manim"
	@echo ""
	@echo "Scenes"
	@echo "  make scenes         List all discovered scenes"
	@echo "  make preview SECTION=1.3 SCENE=SpanOfTwoVectors"
	@echo "  make render  SECTION=1.8 SCENE=ShearTransformation QUALITY=high"
	@echo ""
	@echo "Quality"
	@echo "  make lint"
	@echo "  make test"
	@echo "  make check          Lint + tests + repository validation"
	@echo "  make catalog        Regenerate docs/reference/scene-catalog.md"
	@echo ""
	@echo "Docs"
	@echo "  make docs           Serve docs locally"
	@echo "  make docs-build     Build docs strictly"

install:
	$(PYTHON) -m pip install -e .

install-dev:
	$(PYTHON) -m pip install -e ".[dev]"

install-docs:
	$(PYTHON) -m pip install -e ".[docs]"

doctor:
	$(PYTHON) scripts/doctor.py

scenes:
	$(PYTHON) scripts/list_scenes.py

preview:
	$(PYTHON) scripts/render_scene.py --section $(SECTION) --scene $(SCENE) --quality $(QUALITY) --preview

render:
	$(PYTHON) scripts/render_scene.py --section $(SECTION) --scene $(SCENE) --quality $(QUALITY)

test:
	$(PYTHON) -m pytest

lint:
	ruff check src tests scripts

format:
	ruff format src tests scripts

check: lint test
	$(PYTHON) scripts/validate_repository.py

catalog:
	$(PYTHON) scripts/generate_scene_catalog.py

docs:
	mkdocs serve

docs-build:
	mkdocs build --strict

clean:
	rm -rf media site .pytest_cache .ruff_cache build dist *.egg-info src/*.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +

tree:
	find . -maxdepth 5 		-not -path './.git/*' 		-not -path './media/*' 		-not -path './.venv/*' 		-not -path './site/*' | sort
