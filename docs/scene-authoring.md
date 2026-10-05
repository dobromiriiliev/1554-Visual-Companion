# Scene authoring

## Start with the learning objective

Write one sentence:

> After watching this scene, a student should be able to explain ______ visually and connect it to ______ symbolically.

If that sentence contains several unrelated verbs, split the scene.

## Choose an example for visibility

A good animation example is not always the most general example. Prefer values that:

- fit cleanly on the coordinate plane;
- produce visible intersections;
- avoid distracting fractions unless fractions are the point;
- reveal the structure immediately;
- still represent the general idea honestly.

## Recommended scene anatomy

```python
class ExampleScene(CourseScene):
    """One-sentence catalog description."""

    def construct(self) -> None:
        header = self.section_header("1.x", "Concept")
        # 1. establish objects
        # 2. animate the conceptual change
        # 3. reconnect to notation
        # 4. leave a stable final frame
```

## Keep the final frame useful

The final frame should make sense as a screenshot. Avoid ending with everything faded out unless the transition itself requires it.

## Pacing

Use motion to separate logical steps. If three facts appear simultaneously, students may not know which relationship matters.

## Text

Prefer short labels. Put extended explanation in documentation or narration notes rather than filling the frame with prose.

## MathTex

When possible, preserve object correspondence between algebraic states. Align matrices and equations so that a transformation reads as a transformation rather than a replacement.

## Reusability

Do not immediately generalize every helper. When a pattern appears in two or more scenes, consider moving it into `common/`.
