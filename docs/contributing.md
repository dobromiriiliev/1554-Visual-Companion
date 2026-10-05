# Contributing

Contributions are welcome from students, educators, animators, and software developers.

The canonical contributor guide is [`CONTRIBUTING.md`](../CONTRIBUTING.md) at the repository root. It covers setup, scene design, mathematical-example policy, testing, documentation, and pull-request review.

## Fast path

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev,docs]"
pre-commit install
python scripts/doctor.py
make check
```

Then choose one focused improvement: a clearer visual, a correctness fix, documentation, accessibility, or reusable tooling.

## Before writing a new scene

Read:

- [Scene authoring](scene-authoring.md)
- [Visual style](visual-style.md)
- [Accessibility](accessibility.md)
- [Architecture](architecture.md)

A strong scene has one primary learning objective and reconnects its visual explanation to the algebra students must perform.
