# `src/cobalt/dayopen/report.py`

Renders `docs/40 - DevDocs/reports/day-open-<date>.md`: a header, one
fenced raw block per check, a VERDICT table, and the OVERALL line.
`write_report` overwrites its own day's file outright — this is a repo
file day-open owns, not a marker-bounded vault unit, so there is nothing
here for a human to have edited (unlike `VaultWriter`). `append_verdict`
is the local seat's one write path (`cobalt day-open verdict "..."`):
it refuses if the day's report does not exist yet. Both refuse any path
whose parent is not `REPORTS_DIR` itself (`_assert_under_reports_dir`).
Touches no vault, no database — L48's evidence lands in this file in the
same turn the checks run.
