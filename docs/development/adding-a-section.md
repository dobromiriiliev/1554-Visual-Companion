# Adding a section

## 1. Map the curriculum

Add the section to `course_map.yaml` with:

- number;
- title;
- source URL;
- learning goals;
- planned conceptual bridges.

## 2. Scaffold the package

Use:

```bash
python scripts/new_section.py --help
```

## 3. Plan scenes

Prefer several short scenes, each with one primary learning objective.

## 4. Implement

Use `CourseScene` or `CourseThreeDScene` and shared semantic theme values.

## 5. Document

Update both the local section README and the public docs page.

## 6. Test

Run `make check`, render every new scene, and regenerate the scene catalog.
