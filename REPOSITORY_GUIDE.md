# Repository Guide

This file is a one-page orientation for someone encountering the repository for the first time.

## One-sentence pitch

**The MATH 1554 Visual Companion adds original Manim-based geometric explanations to the same topic order students encounter in Georgia Tech's linear algebra course.**

## Current scope

- Chapter 1 implemented;
- 7 published sections;
- 42 scene classes;
- reusable theme and visual helpers;
- CLI for discovery and rendering;
- MkDocs documentation;
- contributor / governance / CI infrastructure.

## Where to look

| You want to... | Start here |
|---|---|
| Understand the project | `README.md`, `PROJECT_CHARTER.md` |
| Render something | `docs/getting-started.md` |
| Browse animations | `docs/reference/scene-catalog.md` |
| Add a scene | `CONTRIBUTING.md`, `docs/scene-authoring.md` |
| Understand code layout | `docs/architecture.md` |
| Check curriculum alignment | `course_map.yaml` |
| Understand reuse / copyright boundaries | `ATTRIBUTION.md` |
| See long-term direction | `ROADMAP.md` |

## The most important architectural rule

Course-specific composition lives in a section package. Reusable visual ideas move to `common/` only after they are actually reused.

## The most important pedagogical rule

An animation should make one mathematical relationship easier to see and then reconnect that relationship to the notation students must use.
