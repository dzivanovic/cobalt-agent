# `src/cobalt/dayopen/report.py`

Renders `docs/40 - DevDocs/reports/day-open-<date>.md`: a header, one
fenced raw block per check, a VERDICT table, and the OVERALL line.
`write_report` NEVER replaces a file: the first run of a date writes
`day-open-<date>.md`; a later run the same date writes
`day-open-<date>-<HHMMSS>.md` beside it (ET, from `generated_at`), and a
stamped name that already exists raises `ReportPathError`. Opened with
exclusive create (`"x"`). Fixed 2026-09-16 after the 09-15 deploy smoke
overwrote the seat's report and its verdict. `append_verdict`
is the local seat's one write path (`cobalt day-open verdict "..."`):
it refuses if the day's report does not exist yet. Both refuse any path
whose parent is not `REPORTS_DIR` itself (`_assert_under_reports_dir`).
Touches no vault, no database — L48's evidence lands in this file in the
same turn the checks run.
