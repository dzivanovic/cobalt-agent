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

**Config-completion follow-up (2026-08-28, ruled by Dejan):** which
grades are allowed to compute is no longer a hardcoded constant in this
module — `TRADEABLE_GRADES` is gone. `configs/cobalt/aset.yaml` now
carries the FULL grade ladder's dollar truth (every `Grade`, including
`D_SAW` at a config-enforced $0) plus a separate `enabled_grades` field
governing UI/compute availability. `engine.compute_sizing` takes
`enabled_grades` as an explicit argument instead.

## Key functions/classes
- `Grade(str, Enum)` — `A_PLUS, A, B, C, D_SAW`. `D_SAW` is deliberately
  named for the Daily-Stop Model card's framing: "too risky to feel like
  a C? It's not a C — it's a SAW trade." Every member has a real dollar
  figure in `configs/cobalt/aset.yaml` now (D's is always exactly 0);
  which ones are actually usable is `SheetModesConfig.enabled_grades`'
  job, not anything in this enum.
- `SheetMode(str, Enum)` — `FULL, HALF`. Selects which column of
  `configs/cobalt/aset.yaml`'s dollar table applies.
- `Direction(str, Enum)` — `LONG, SHORT`.
- `SizingInput` — `ticker` (normalized to stripped-upper by a
  `field_validator`, blank rejected), `grade`, `direction`,
  `sheet_mode`, `risk_dollars` (`Decimal >= 0` — `ge=0`, not `gt=0`,
  because D's real configured figure is exactly 0 and is still a
  legitimate value to carry through here; resolved by the caller from
  `SheetModesConfig.dollars_for(mode, grade)` in `config.py`, `engine.py`
  stays config-agnostic and just consumes this number), `entry`, `stop`
  (`Decimal > 0`), optional `last_price` / `price_source` (prefill
  metadata, never required). `extra="forbid"` — an unexpected field is a
  validation error, not a silently dropped one. No `daily_stop` field
  anymore.
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
None — pure data models. The enums are compile-time constants, not
config; the actual dollar figures per grade/mode, and which grades are
enabled, live in `configs/cobalt/aset.yaml`, read by `config.py`.
