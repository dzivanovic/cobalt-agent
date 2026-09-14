# `src/cobalt/dayopen/launchd.py`

C1's collector: `launchctl print gui/<uid>/<label>`, parsed for `state`,
`pid`, `runs` and `last exit code`. A deliberate second parser next to
`cobalt.jobs.watchdog.launchctl_status` (which shells `launchctl list`,
tab-separated, no `runs` counter) — different command surface, nothing
shared to duplicate.

`launchctl_print()` raises `LaunchdPrintError` on a missing binary, a
non-zero exit or a timeout; `parse_launchctl_print()` is the pure half,
tested directly against the real `state`/`pid`/`runs`/`last exit code`
values captured in `docs/40 - DevDocs/reports/day-open-2026-09-14.md` S1.
`running_with_pid` is C1's whole PASS condition.
