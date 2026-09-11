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
- duplicate labels; a kill phrase equal to the resume phrase.

## The mirror problem
launchd cannot read this file and this file cannot read launchd, so the
schedule is written twice. `cobalt validate` compares them — a mirror
nobody compares is a mirror that drifts.
