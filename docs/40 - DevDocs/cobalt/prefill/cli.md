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

## 2026-10-10 — f4-refresh-1010
F4: `prefill refresh [--dry-run]` added — its own handler `_run_refresh`,
constant `REFRESH_JOB = "com.cobalt.prefill-refresh"` and parser
registration. It runs under `as_job(REFRESH_JOB, skip=dry_run)`, prints the
run report (every unified diff) and then raises `RefreshNotClean` inside the
block when a field degraded or a write failed, so `job_run` records
`exit_code=1`.

## 2026-10-26 — f4-probe
`prefill probe X15` added (card 1047; F4 FINAL `:221`): the parser takes one
positional `item` (`choices=refresh_probe.PROBE_ITEMS`, today `X15`); the
handler imports `refresh_probe` and exits with `main(item)`'s code, outside
`as_job` (a probe is not a run of a job). `daily` and `refresh` are unchanged.
The probe (`src/cobalt/prefill/refresh_probe.py`) prints one line, `PROBE X15
OK|FAIL <clause>` (exit 0 / 1) or `PROBE X15 NOT RUN — <reason>` (exit 3).
Boundary: `COBALT_ENV=dev` or a `FAIL refused:` line before anything is built;
every `httpx.AsyncClient` gets the probe's `httpx.MockTransport` and a real
transport is stopped (`FAIL error network`); the constructed token, no store,
no vault write, no DM, no `launchctl`; loguru off for `cobalt` during the run; a
crash is `FAIL error <ExceptionName>`. Virtual clock: one `monotonic` / `sleep`
/ `now` from 08:40:00 to 08:46:00 ET on a constructed weekday drives the radar
stand-in (40 rpm through `finviz_get`), the real `StrikeDetector.tick` over 5
constructed ARMED cards (`fetch_bars`, a `TokenBucket` on the clock) and, at
08:43:00, the real `_gated_fetch` (its gate, then its 3 GETs). The count: the
mock records (virtual minute, consumer, path, status) per request, redirects
included, never the query, and answers 429 past the 50th in a minute; OK iff
no minute holds more than 50 and no 429 was answered, else FAIL naming the
FINAL `:221` consequence; a gate refusal is NOT RUN; a ceiling other than 50 is
NOT RUN.

2026-10-26 (f4-probe check O1, O2): the pass rule's two halves are pinned on `_clause` — a minute of exactly 50 is OK (`test_check_o1_…`), and a 429 within the ceiling is FAIL with the consequence (`test_check_o2_…`).
