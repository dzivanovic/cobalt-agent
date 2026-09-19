# `src/cobalt/smoke/report.py`

Renders and writes `docs/40 - DevDocs/reports/<suite>-smoke-<date>.md`
(`REPORTS_DIR` is day-open's). It follows the same file discipline as the
day-open report (L48):
- The report is written in the same turn the checks run.
- It is a plain repo file, with no `VaultWriter` and no markers.
- The hub commits it under L51(2).

- `build_report(suite, title, ctx, outcomes, generated_at=)` builds a `SmokeReport` with `overall = overall_verdict(outcomes)`.
- `render_table(rep)` prints `| # | check | verdict | evidence |`, one row per check, then `OVERALL: <GREEN|AMBER|RED>`. Pipes and newlines in cells are escaped.
- `render_markdown(rep)` renders, in order:
  1. The title and generation line.
  2. **Variables** (`SmokeContext.printable()`: now, report_date, session, cutoff, last_trading_day, last summary slot/date, database).
  3. **VERDICT** (the table), then the roll-up rule line.
  4. One section per check: kind, `command:`, `expected:`, verdict detail, then the raw evidence in a fence.

  The hand fallback runs from this file alone (R6 A).
- `render_json(rep)` carries the same content without `raw`, for `--json`. Each check also carries `number`: THE number of its result when it declared a `result_number`, rendered as **text** — a `Decimal` prints exactly and a float would not (L57) — and `null` otherwise.
- `write_report(rep, reports_dir=)`:
  - Never replaces a file. A second run the same day writes `…-<HHMMSS>.md` beside the first, stamped with the ET time of the write.
  - Refuses to write outside `reports_dir` and to overwrite a colliding stamp (`ReportPathError`).
