# `tests/cobalt/test_aset_engine.py`

## What it does
Unit tests for `engine.py`'s pure math — no DB, no network, no config
file. The load-bearing test is
`test_reference_worked_example_short_grade_a`: it reproduces the
reference sizer's own worked example (daily stop 1000, grade A/short,
entry 49, stop 50.09) and asserts every output field, so any future
change to the math has to consciously break a documented, sourced
example rather than an arbitrary assertion.

## Key functions/classes (what's covered, not defined)
- `daily_stop_from_account` — account÷50 law + non-positive rejection.
- `temp_prefill_daily_stop` — account÷100 temp override + non-positive
  rejection (kept as a separate test from the ÷50 law's test, on
  purpose — they must never accidentally converge).
- `compute_sizing` — the full worked example; the grade→shares map
  parametrized across all five grades (`test_grade_risk_map`); D-SAW's
  "no trade" warning; entry==stop failing loud; long/short target
  projection; long/short stop-on-wrong-side warnings; shares-rounds-to-
  zero warning.
- `enforce_broker_cap` — refuses above, warns exactly at, silent below.
- `SizingInput` ticker normalization (strip/upper) and blank rejection.

## Data flow in/out
None — pure function tests, all inputs constructed in-memory via the
`make_input()` helper.

## Config it reads
None.
