# `src/cobalt/prefill/cli.py`

## What it does
The `prefill` console script (`uv run prefill daily` / `uv run prefill
drc [--date YYYY-MM-DD]`), registered in `pyproject.toml`
`[project.scripts]`. Same `LOGURU_LEVEL=INFO` guard as
`aset/__main__.py` and `archiver/runner.py` (this import chain also
transitively pulls in `FinvizApiClient`). Any exception is caught at
the top level, logged, printed to stderr as `FAILED: ...`, and exits
non-zero — the two scheduled launchd jobs (`ops/com.cobalt.prefill-
daily.plist`, `ops/com.cobalt.prefill-drc.plist`) surface failures in
their log files rather than dying silently.

## Key functions/classes
- `main()` — argparse subcommands `daily` / `drc`.
- `_run_daily()` — Slice 2.1: also prints `filled`/`skipped` slot lists
  from `DailyPrefillResult` (the "a non-empty slot is skipped and
  reported" requirement — reported here, on stdout/log, not written
  into the note itself).

## Data flow in/out
**In:** CLI args. **Out:** stdout summary line (+ filled/skipped slot
lines for `daily`), or a `FAILED:` stderr line + exit code 1.

## Config it reads
None directly — delegates entirely to `daily.run_daily_prefill` /
`drc.run_drc_prefill`.

## 2026-09-29 — DRC D3: `prefill drc` retired
The `drc` subcommand, `_run_drc` and `DRC_JOB` (`com.cobalt.prefill-drc`)
are removed (F39; v2 §8 `[F-22]`): the DRC is built by `cobalt drc build`
(K1's `drc` group) and the `/drc` drop's event. `uv run prefill drc` now
exits 2, `invalid choice: 'drc'`. The `prefill` script entry in
`pyproject.toml` stays — it runs `prefill daily`.
