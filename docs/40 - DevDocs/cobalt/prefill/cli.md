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

## Data flow in/out
**In:** CLI args. **Out:** stdout summary line, or a `FAILED:` stderr
line + exit code 1.

## Config it reads
None directly — delegates entirely to `daily.run_daily_prefill` /
`drc.run_drc_prefill`.
