# Release checklist

Before tagging a release:

- [ ] `ruff check src tests scripts` passes
- [ ] `python -m pytest` passes
- [ ] `python scripts/validate_repository.py` passes
- [ ] `mkdocs build --strict` passes
- [ ] changed scenes have been render-reviewed
- [ ] `CHANGELOG.md` is updated
- [ ] `CITATION.cff` version/date are updated
- [ ] `pyproject.toml` version is updated
- [ ] public documentation matches scene names
- [ ] licensing / attribution for any new assets is documented
- [ ] generated scene catalog is current

After release:

- create a GitHub release from the tag;
- include a concise list of new visualizations;
- link breaking scene-name changes prominently;
- invite educational feedback.
