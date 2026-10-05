# Visual style

The style system is intentionally small. Consistency matters more than decorative complexity.

## Semantic palette

Defined in `src/math1554_visuals/common/theme.py`:

- `PRIMARY` — first/main mathematical object;
- `SECONDARY` — comparison or second object;
- `SOLUTION` — correct/shared/target state;
- `WARNING` — contradiction, inconsistency, or failure condition;
- `ACCENT` — third object or supporting emphasis;
- `MUTED` — explanatory secondary text.

Semantic aliases such as `PIVOT`, `FREE`, and `INCONSISTENT` should be preferred when the concept matches.

## Typography

- section headers should be stable across scenes;
- long prose belongs in documentation, not animation frames;
- equations should remain large enough to read in a classroom projection;
- avoid showing more simultaneous notation than the scene needs.

## Layout

Prefer clear spatial roles:

- geometry on the left / algebra on the right;
- input on the left / output on the right;
- before above / after below;
- consistent placement across a sequence when comparing cases.

## Motion

Use transformations when the mathematical object persists. Use fade transitions when the object is conceptually being replaced rather than changed.
