# `src/cobalt/aset/engine.py`

## What it does
The deterministic sizing math. **Pure functions — no I/O, no LLMs, no
config reads.** Everything here is a straight port of
`docs/references/aset_daily_position_sizer.html`'s arithmetic and
`docs/references/Daily_Stop_Model_Card.pdf`'s rules, in `Decimal` (never
float) so money math never drifts.

## Key functions/classes
- `SizingError(ValueError)` — invalid input; the sheet turns this into a
  visible FAILED banner, never a guess.
- `enforce_broker_cap(daily_stop, cap) -> list[str]` — the broker hard
  cap: raises `SizingError` above the cap (refused), returns a one-line
  warning exactly at the cap, returns `[]` below it. Called from
  `web.py` before `compute_sizing`, server-side, in addition to the
  client-side JS clamp — the server never trusts the browser.
- `daily_stop_from_account(account_size) -> Decimal` — **the ruled
  Daily-Stop Model law: account ÷ 50.** Explicitly commented not to
  change; it's what `test_reference_worked_example_short_grade_a` in
  the test suite validates against the reference sizer's own worked
  example. Not currently called by `web.py` (see next function) but
  kept as the canonical implementation and the thing any future "revert
  the temp override" change would restore.
- `TEMP_PREFILL_DIVISOR = Decimal("100")` /
  `temp_prefill_daily_stop(account_size) -> Decimal` — a **labeled
  temporary override** (Dejan, 2026-08-25, "for now"): when
  `daily_stop_default` isn't configured, the sheet's auto-fill uses
  account ÷ 100, not the ruled ÷ 50. Deliberately kept as a separate
  function rather than changing `DAILY_STOP_DIVISOR`, so the ruled law
  and its test stay intact and this override is one grep away from
  being reverted.
- `compute_sizing(inp: SizingInput) -> SizingResult` — the actual sizing
  computation: `risk_budget = daily_stop × grade_pct / 100`,
  `shares = floor(risk_budget / |entry - stop|)`, `used_risk = shares ×
  per_share_risk`, `target_1r`/`target_2r` projected from direction.
  Raises `SizingError` if entry == stop. Appends non-fatal warnings for:
  D-SAW grade (no trade), stop on the wrong side of entry for the given
  direction, and shares rounding to zero.

## Data flow in/out
**In:** a validated `SizingInput` (from `models.py`).
**Out:** a `SizingResult`, or a raised `SizingError`. No side effects —
callers (`web.py`) own persistence and rendering.

## Config it reads
None — by design. All parameters (grade %, cap, daily stop) arrive as
function arguments; the caller is responsible for sourcing them from
`config.py`.
