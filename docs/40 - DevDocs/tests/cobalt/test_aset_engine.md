# `tests/cobalt/test_aset_engine.py`

## What it does
Unit tests for `engine.py`'s pure math — no DB, no network, no config
file. **Iteration 4 (2026-08-28):** rewritten for the fixed-dollar
sheet-mode model; the old percentage-model reference-sizer worked
example is gone (that math no longer exists). Worked examples here are
built from scratch, keyed to `configs/cobalt/aset.yaml`'s real full/half
A/B dollar figures (135/60, 70/30) so a config drift would be caught by
`test_grade_dollar_map_full_mode` even though the test doesn't read the
config file directly (values are inlined — a genuine future config
change would need this test updated too, deliberately, not silently
passing).

## Key functions/classes (what's covered, not defined)
- `test_full_mode_b_worked_example` — the load-bearing worked example:
  full-mode B ($60), entry 49, stop 50.09, short — asserts every output
  field (55 shares, $59.95 used risk, both targets, no warnings).
- `test_grade_dollar_map_full_mode` — A ($135) and B ($60) both check
  out against `configs/cobalt/aset.yaml`'s real full-mode values.
- `test_non_tradeable_grades_refuse_to_compute` /
  `test_a_plus_is_reserved_and_not_tradeable` — C, D_SAW, and A_PLUS all
  raise `SizingError` ("not tradeable") rather than computing a
  meaningless size — the sheet-mode-model replacement for the old
  D-SAW-"no trade"-warning behavior.
- `test_equal_entry_and_stop_fails_loud`, `test_long_targets_project_upward`,
  `test_long_with_stop_above_entry_warns`,
  `test_short_with_stop_below_entry_warns`,
  `test_size_rounding_to_zero_warns`, `test_ticker_normalized_and_blank_rejected`
  — unchanged in substance from the percentage model, re-expressed
  against `risk_dollars` instead of `daily_stop × pct`.
- `test_half_mode_dollars_differ_from_full` — same grade, different mode
  → different budget → fewer shares in half mode.
- `TestFillRecompute` — `compute_fill_recompute`: shares/used-risk
  recomputed at the actual fill (same `risk_dollars`, same stop); no
  warning under 25% distance change; the exact warning text at/above
  25%; `actual_fill` must be positive; `actual_fill` can't equal the
  stop.

## Data flow in/out
None — pure function tests, all inputs constructed in-memory via the
`make_input()` helper.

## Config it reads
None — but worked-example dollar figures are hand-matched to
`configs/cobalt/aset.yaml`'s committed values; see `test_aset_config.md`
for the test that actually reads that file.
