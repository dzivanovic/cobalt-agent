# `src/cobalt/aset/engine.py`

## What it does
The deterministic sizing math. **Pure functions — no I/O, no LLMs, no
config reads.** In `Decimal` (never float) so money math never drifts.

**Iteration 4 (2026-08-28, ruled by Dejan):** the daily-stop x
grade-percentage model (`docs/90 - References/aset_daily_position_sizer.html`,
`docs/90 - References/Daily_Stop_Model_Card.pdf`) is retired — historical
reference only, no longer the math this module implements. Sizing is
now fixed-dollar-per-grade, mirroring Dejan's DAS Trader Pro hotkey
files exactly (sheet mode full/half — see `configs/cobalt/aset.yaml`).
`enforce_broker_cap`, `daily_stop_from_account`,
`TEMP_PREFILL_DIVISOR`/`temp_prefill_daily_stop`, and the old
percentage-based `compute_sizing` body were **deleted outright**, not
deprecated in place — one-path rule.

## Key functions/classes
- `SizingError(ValueError)` — invalid input; the sheet turns this into a
  visible FAILED banner, never a guess.
- `FILL_DISTANCE_WARNING_PCT = Decimal("25")` — the actual-fill distance
  change threshold: ≥25% between the planned and actual-fill entry means
  the stop was likely picked against a different price than what was
  actually paid.
- `compute_sizing(inp: SizingInput) -> SizingResult` — refuses up front
  (`SizingError`) if `inp.grade not in TRADEABLE_GRADES` ("not
  tradeable in sheet mode — no trade (SAW)"). Otherwise:
  `risk_budget = inp.risk_dollars` (flat, no percentage math at all —
  the config-driven number IS the budget), `shares = floor(risk_budget /
  |entry - stop|)`, `used_risk = shares × per_share_risk`,
  `target_1r`/`target_2r` projected from direction. Raises
  `SizingError` if entry == stop. Appends non-fatal warnings for: stop
  on the wrong side of entry for the given direction, and shares
  rounding to zero.
- `compute_fill_recompute(original: SizingResult, actual_fill: Decimal)
  -> FillRecompute` — recomputes shares at `actual_fill` using the
  **same** `risk_dollars` and the **same** stop as `original` (never a
  new distance-derived budget). Raises `SizingError` if `actual_fill`
  isn't positive or equals the stop. Sets `structural_warning` when
  `distance_change_pct >= FILL_DISTANCE_WARNING_PCT`. Note-only — never
  writes to Postgres; callers (`web.py`) pass the result straight to
  `daily_note.save_fill_update`.

## Data flow in/out
**In:** a validated `SizingInput` (from `models.py`) for `compute_sizing`;
a prior `SizingResult` + an actual fill price for `compute_fill_recompute`.
**Out:** a `SizingResult` / `FillRecompute`, or a raised `SizingError`. No
side effects — callers (`web.py`) own persistence and rendering.

## Config it reads
None — by design. `risk_dollars` arrives as a `SizingInput` field,
already resolved by the caller from `config.py`'s
`SheetModesConfig.dollars_for(mode, grade)`.
