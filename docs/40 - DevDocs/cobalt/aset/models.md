# `src/cobalt/aset/models.py`

## What it does
The Pydantic data contracts for a single sizing computation — the
vocabulary every other ASET module (`engine`, `store`, `web`,
`daily_note`) shares. No behavior beyond validation.

**Iteration 4 (2026-08-28, ruled by Dejan):** the daily-stop x
grade-percentage model is retired. Sizing is now fixed-dollar-per-grade,
selected by a `SheetMode` (FULL/HALF) mirroring Dejan's two DAS Trader
Pro hotkey files exactly — the actual dollar figures live in
`configs/cobalt/aset.yaml`, not here (this module stays pure data).

## Key functions/classes
- `Grade(str, Enum)` — `A_PLUS, A, B, C, D_SAW`. `D_SAW` is deliberately
  named for the Daily-Stop Model card's framing: "too risky to feel like
  a C? It's not a C — it's a SAW trade."
- `TRADEABLE_GRADES = (Grade.A, Grade.B)` — the only grades with a
  defined fixed-dollar risk in sheet mode. `A_PLUS` is reserved/hidden
  from the sheet for now; `C`/`D_SAW` are "no trade (SAW)" — selecting
  either makes `engine.compute_sizing` refuse with a `SizingError`
  rather than compute a meaningless size.
- `SheetMode(str, Enum)` — `FULL, HALF`. Selects which column of
  `configs/cobalt/aset.yaml`'s dollar table applies.
- `Direction(str, Enum)` — `LONG, SHORT`.
- `SizingInput` — `ticker` (normalized to stripped-upper by a
  `field_validator`, blank rejected), `grade`, `direction`,
  `sheet_mode`, `risk_dollars` (`Decimal > 0` — resolved by the caller
  from `SheetModesConfig.dollars_for(mode, grade)` in `config.py`;
  `engine.py` stays config-agnostic and just consumes this number),
  `entry`, `stop` (`Decimal > 0`), optional `last_price` / `price_source`
  (prefill metadata, never required). `extra="forbid"` — an unexpected
  field is a validation error, not a silently dropped one. No
  `daily_stop` field anymore.
- `SizingResult` — the computed output: `input` (echoes the
  `SizingInput`), `risk_budget`, `per_share_risk`, `shares`,
  `used_risk`, `target_1r`, `target_2r`, `warnings: list[str]`. No
  `risk_pct` field anymore (there's no longer a percentage in this
  model — `risk_budget` **is** `risk_dollars`, just quantized).
- `FillRecompute` — the actual-fill audit record: `original`
  (`SizingResult`), `actual_fill`, `recomputed_shares`,
  `recomputed_used_risk`, `share_delta`, `distance_change_pct`,
  `structural_warning` (optional — set when the fill moved the stop
  distance ≥25% from the plan). Never persisted to Postgres — it's a
  note-only audit trail entry (see `daily_note.py`), not a second
  `aset_sizings` row.

## Data flow in/out
**In:** raw form fields (strings) from `web.py`, coerced to `Decimal`/
enum by Pydantic on `SizingInput(**form)`; `risk_dollars` is resolved
by `web.py` from `config.load_sheet_modes_config()` before construction,
not read directly off the form.
**Out:** validated `SizingInput` consumed by `engine.compute_sizing`,
which returns a `SizingResult` consumed by `store.py` (persistence),
`daily_note.py` (card formatting), and `web.py` (rendering).
`engine.compute_fill_recompute` additionally returns a `FillRecompute`
consumed only by `daily_note.py`'s FILL UPDATE block and `web.py`'s
result-card rendering.

## Config it reads
None — pure data models. `TRADEABLE_GRADES` and the enums are
compile-time constants, not config; the actual dollar figures per
grade/mode live in `configs/cobalt/aset.yaml`, read by `config.py`.
