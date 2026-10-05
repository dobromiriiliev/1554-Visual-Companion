# Governance

The project uses lightweight maintainer governance while it is small.

## Roles

### Contributors

Anyone who submits code, documentation, mathematical review, design feedback, issue reports, or educational evaluation.

### Reviewers

Regular contributors trusted to review specific areas such as mathematics, Manim code, documentation, or accessibility.

### Maintainers

Contributors responsible for merging changes, releases, repository policy, and resolving disputes.

## Decision making

Most decisions should be made through ordinary issue and pull-request discussion.

When there is disagreement, maintainers should optimize for:

1. mathematical correctness;
2. student understanding;
3. open accessibility;
4. maintainability;
5. consistency with the project charter.

Large architectural changes should be proposed in an issue before implementation.

## Public API

Scene class names, section identifiers, CLI commands, and reusable helpers may be referenced by external users. Renaming them should therefore be treated as a compatibility change and documented in `CHANGELOG.md`.

## Conflicts of interest

Reviewers should disclose conflicts that could materially affect a decision, including reviewing their own major proposal as the sole approver.

## Becoming a maintainer

Maintainer status may be offered to contributors who demonstrate sustained constructive participation, sound technical or mathematical judgment, and respectful collaboration.

## Removing maintainer access

Maintainer access may be removed for prolonged inactivity, repeated policy violations, or misuse of repository privileges. The goal is project health, not punishment.
