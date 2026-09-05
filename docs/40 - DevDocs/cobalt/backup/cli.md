# `src/cobalt/backup/cli.py`

## What it does
`cobalt backup run` · `status` · `restore <dest> <id> --into DIR`.

## `run` goes through `as_job`
A manual catch-up run IS a run of `com.cobalt.backup`: it lands in
`cobalt_jobs` and it stops the MISSED probe firing an hour later.
`--dry-run` deliberately does NOT touch the row — a dry run is not a run.

## `status` exits 1 when nothing is armed
So a human check and a scripted one give the same answer. Today that is
the honest exit code: there is no backup.

## The job is not registered yet
`com.cobalt.backup` is deliberately absent from `configs/cobalt/
jobs.yaml`, and its plist waits in `ops/pending/` — see that directory's
README. `cobalt backup run` therefore fails with "unknown job label"
until the job is armed, which is correct: the arming steps are one
commit, together, or `cobalt validate` fails.
