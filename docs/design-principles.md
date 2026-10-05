# Design principles

## 1. Visualize a relationship, not decoration

Every animation should answer a mathematical question. Motion should communicate structure rather than simply make the screen more active.

## 2. Keep the course synchronized

The project earns its value by appearing where the learner needs it. A beautiful eigenvector scene does not help a student currently trying to understand pivot variables unless the course mapping makes that transition explicit.

## 3. Reconnect geometry to symbols

A scene should usually finish by reconnecting the visual to notation, an equation, a matrix, or a computation.

## 4. One primary concept per scene

Small scenes are easier to teach with, render, test, remix, and maintain.

## 5. Use semantic visual language

A color should mean something consistently. Pivot highlights, warnings, solutions, and recurring vector roles should not change arbitrarily from section to section.

## 6. Do not rely on color alone

Use labels, spatial organization, line styles, or shapes as redundant cues.

## 7. Prefer transformations over cuts

When teaching equivalence—system to matrix, vector equation to `Ax=b`, input to output—morphing or aligned layouts can preserve conceptual continuity.

## 8. Preserve invariants visibly

When the mathematical point is that something stays the same, show the invariant explicitly. Row operations are a canonical example: the equation representation changes while the common solution stays fixed.

## 9. Use original examples

The project maps concepts, not copyrighted prose. Examples should be created for the visualization itself and chosen to make the intended structure easy to see.

## 10. Optimize for explanation before abstraction

Do not build a giant framework before repeated needs emerge. Implement a clear scene first; promote stable patterns to `common/` after genuine reuse.
