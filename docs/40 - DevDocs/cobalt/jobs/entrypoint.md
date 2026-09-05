# `src/cobalt/jobs/entrypoint.py`

## What it does
The one line each scheduled entry point adds:

```python
with as_job("com.cobalt.prefill-daily", skip=args.dry_run) as job:
    ...
    job.result = {...}
```

## Three things it adds over `job_run` directly
1. **`skip=` — a dry run is not a run.** `prefill daily --dry-run`
   writes nothing and must not satisfy the MISSED probe, or *"I checked
   what it would do"* would silence the alarm that says it never did it.
2. **F19's log guard, installed once, here.** Every scheduled job writes
   to `logs/*.log`; those files are read over Tailscale and pasted into
   reports. A new job gets the guard by using this wrapper.
3. The **stopped** case prints a line and exits 0 rather than raising a
   traceback.

## Ad-hoc runs count
`uv run prefill daily` by hand goes through this too, and that is
correct: a manual catch-up run *is* a run of that job, it belongs in the
row, and it should stop the MISSED probe firing an hour later.

## Where it is wired
`prefill/cli.py` (daily, drc) · `archiver/runner.py` (the nightly full
run only — a `--backfill TICKER` is an operator fetching one symbol, and
recording it as the nightly run would mark the night satisfied) ·
`cards/cli.py` (expire) · `daymode/cli.py` (propose).
