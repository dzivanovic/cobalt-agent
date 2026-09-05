# `src/cobalt/jobs/models.py`

## The five states
`pending` · `running` · `done` · `failed` · `zombie`.

Two are **derived by the watchdog** rather than written by the job
itself, and that is the point of the feature: a job that fails loudly is
easy, a job that stops existing is the one that goes unnoticed for a
week.

`RED_STATES` = {`failed`, `zombie`}. `pending` is not red on its own — a
job registered this morning that has not reached its schedule yet is
fine; the MISSED probe is what catches one that should have run.

## `missed` is deliberately not a state
There is no row to move. It is a fact about the **absence** of a run,
computed at probe time from the schedule; writing it as a state would
mean inventing a run to attach it to.

## `Supervisor`
`self` (the wrapper — the strongest signal: alive, running our code, and
past our gates) · `launchd` (a live PID) · `pidfile` (spawned detached;
see `com.cobalt.agent`).
