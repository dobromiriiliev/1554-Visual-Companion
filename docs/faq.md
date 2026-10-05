# FAQ

## Is this an official Georgia Tech project?

No. It is an independent open-source project that uses the public course sequence as a curriculum reference.

## Is this trying to recreate 3Blue1Brown?

No. The project values visual mathematical intuition, but it creates original scenes and is organized around course synchronization rather than reproducing existing videos.

## Why Manim?

Manim makes mathematical objects programmable. That supports precise transformations, version-controlled source, reusable components, and reproducible rendering.

## Why many small scenes instead of one video per lecture?

Small scenes are easier to remix into lectures, review pages, web galleries, and other curricula. They are also easier to test and maintain.

## Why is there no Section 1.6 folder?

The repository follows the published Chapter 1 section numbering of the referenced MATH 1554 notes.

## Can I use these scenes in my own class?

Yes, subject to the MIT License for project code. If you publish modified versions, clearly distinguish your modifications and preserve applicable license notices.

## Why does installation fail when I run pip from `src/`?

This repository uses a `src` layout. Run editable installation from the project root, where `pyproject.toml` and `README.md` live.
