# `cobalt.radar.anatomy.frame` — the Frame (side binding by mirroring)

Added 2026-09-21 in STEP-2 of the setups one build (FINAL §2.1 [F-04], [R2F-12], §3).

Every def is evaluated twice per scan, once per side, on a `Frame` built once per (member, scan, side):

- **Long** is the stored working bars.
- **Short** is the same detectors run on mirrored bars. `mirror_bars` maps price to −price and swaps high and low; volume and time are unchanged. `mirror_daily` does the same to the daily series ([R2F-12]), so the HTF range break of a mirrored run is the real opposite break with the same day count.

`build_frame(side, run, daily=, daily_ok=, trade_date=, params=, last_close=)` takes the REAL series and mirrors them for `short`. It runs the detectors (`detect_extension`, `htf_range_break`) and fills `atoms` (moved here from `evaluate.py`). The stage asks the frame for atoms and never runs a detector itself. `Frame.real(price)` converts a frame price back to real-world coordinates.

The acceptance property is F-04's, proved over every scan of the committed day in `tests/cobalt/test_setups_registries.py`:

- for price outputs, `negate_prices(eval_as_long(mirror(bars))) == eval_as_short(bars)`;
- for predicates, `pred_as_long(mirror(bars)) == pred_as_short(bars)`.

The mirror wraps `WorkingBar` / `DailyBar` only. It never round-trips through the archiver's `Bar` (X6: a negative-price `Bar` constructs, so nothing would stop such a round trip).
