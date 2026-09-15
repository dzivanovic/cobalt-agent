# `src/cobalt/jobs/config.py`

Resident specifications now carry optional static import roots; missing declarations trigger conservative restart selection.

## What it does
Loads `configs/cobalt/jobs.yaml` into `JobRegistry` / `JobSpec` /
`Schedule`. Pydantic-validated; a bad row crashes with its label.

## `Schedule` — exactly one shape
`at` + `weekdays` (a `StartCalendarInterval` plist), `every_min`, or
`every_min_tunable`. Weekday numbering is **launchd's** (1 = Monday),
matching the plists it mirrors.

`every_min_tunable` exists for F16: the heartbeat's own cadence is a
threshold, so it reads `heartbeat.interval_min` rather than carrying a
literal. It is the number every *"red within one interval"* claim is
measured against.

## Refusals worth knowing
- a **one-shot with no schedule** — the MISSED probe asks "should this
  have run by now", and without a schedule there is no answer, only
  silence;
- `supervisor: pidfile` with no `pidfile`, or a `pidfile` on any other
  supervisor (nothing would read it);
- `launchd_unmanaged` on anything but a launchd-supervised resident —
  nothing else has a launchd liveness probe to soften;
- duplicate labels; a kill phrase equal to the resume phrase.

## `launchd_unmanaged` (INTERIM, 2026-09-14)
Plist loaded, process deliberately running outside launchd: the watchdog
rates "not running" AMBER instead of RED (see `watchdog.md`). Set on
`com.cobalt.herdr` only; removed as the last step of its launchd handover.

## The mirror problem
launchd cannot read this file and this file cannot read launchd, so the
schedule is written twice. `cobalt validate` compares them — a mirror
nobody compares is a mirror that drifts.

## `no_resident_reads` (ruled 2026-09-15)
A top-level list of repo files that only **one-shots** read at runtime —
`path`, `readers` (job labels), `because` (the derivation, file:line).
A one-shot re-reads everything every run, so such a file derives no
restart; declaring it is what separates "no resident reads this" from
"nobody has worked out who reads this". The schema refuses an
unregistered label, a RESIDENT as reader (that belongs in its `reads`),
a path some resident already `reads`, and absolute or `..` paths.
`JobRegistry.no_resident_read(path)` returns the declaration or None.
First row: `configs/cobalt/notify.yaml`, reader `com.cobalt.heartbeat`.
