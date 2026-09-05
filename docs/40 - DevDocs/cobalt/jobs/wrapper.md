# `src/cobalt/jobs/wrapper.py`

## What it does
```python
with job_run("com.cobalt.archiver") as run:
    summary = do_the_work()
    run.result = {"rows_written": summary.rows_written}
```

## What it guarantees, in order
1. **The kill switch is checked first.** A stopped Cobalt does not start
   a one-shot at all — and the process exits **0**, not 1, because a
   deliberate stop is not a failure and must not paint F18 red for a
   state the operator caused.
2. `running` is marked before the work, with `started_at`.
3. A **beater thread** stamps `heartbeat_at` every
   `timeout_s / jobs.heartbeat_fraction` (5 min for the archiver's
   90-minute window).
4. `done` (exit 0) or `failed` (exit code + the exception, redacted
   through F19 on its way into the column).
5. The exception is **re-raised**. The wrapper reports; it never
   swallows.

## Why the beater thread is a daemon
If the job process dies hard, the thread dies with it, `heartbeat_at`
stops advancing, and the watchdog draws the right conclusion. A thread
that outlived its job would keep a dead job looking alive — the exact
failure this feature exists to catch.

A failed stamp does not kill the job; it logs at ERROR, because the
watchdog may conclude ZOMBIE from it and an operator needs the other
half of the story.

## `run.result`
Whatever the run wants F18 to be able to report. The archiver's
`rows_written` lands here, which is what makes *"archiver freshness
(last run + rows written)"* answerable without a second table.

## `should_keep_running(label)`
A resident's own loop check — `False` means exit cleanly now. Cobalt's
residents are launchd-supervised today, so this is for the first
new-core resident (the S2 radar poller).
