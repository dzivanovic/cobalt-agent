# `src/cobalt/strike/config.py`

The four strike rows of `configs/cobalt/taxonomy/tunables.yaml`, unit-checked like `radar/config.py`: `strike.poll_interval_min` (duration 2, the floor under the derived interval and the measure's cadence floor), `strike.max_armed` (count 5), `strike.alert_criterion_s` (duration 5), `strike.missed_sweep_interval` (duration 100). `check(path)` returns `StrikeSettings` or raises `StrikeConfigError` naming the key or the unit; `validate_command_lines()` is what `cobalt validate` prints, in a block right after the archiver's, and a `StrikeConfigError` there fails validate (`FAILED: …`, exit 1).

There is no `strike.finviz_max_rpm` and no fixed poll interval (card DECISION D2): the one ceiling is `radar.finviz_max_rpm`, and the interval is derived (`detector.poll_interval`).

## 2026-10-09 — s4-p1-1009
New module (S4-P1 T1).
