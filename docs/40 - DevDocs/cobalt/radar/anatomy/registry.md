# `src/cobalt/radar/anatomy/registry.py`

## What it does
`evaluability(td) -> Evaluability` answers whether S2 can evaluate a def end-to-end, and if not, exactly what is missing (R2). The rule is data-driven, never slug-driven, and names no trade (L31/L32). A def is evaluable when every atom its preconditions and avoids require (`Predicate.required_atoms`), its trigger and its stop placement are all served by an S2 detector.

## Key functions/classes
- `SUPPORTED_ATOMS`: `Extension.state`, `Extension.instantiated`, `Extension.leg_count`, `RangeBreak(HTF).day_count`.
- `SUPPORTED_TRIGGERS`: `bar_break` with a `bars_cleared` param.
- `SUPPORTED_STOP_REFS`: `structural_extreme` on `snapback_candle` / `turn_low`.
- `Evaluability {evaluable, missing_atoms, human_predicates}`. Missing entries read on their own: atoms verbatim, relation words, `trigger:<type>`, `stop:<type>[:<ref>]`.

## Gotchas
`text` predicates are human (L11), never block evaluability, and are counted. `radar_watch[]` is not a card gate and is out of scope. A `sequence` trigger has no params and is reported as `trigger:sequence`, not a crash. The live-note proof (all 13 defined notes parse; Rubberband evaluable; the rest name what they miss) is the hub-run `requires_vault` test in `tests/taxonomy/test_predicate.py`.
