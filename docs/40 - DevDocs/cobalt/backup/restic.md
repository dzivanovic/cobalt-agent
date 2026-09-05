# `src/cobalt/backup/restic.py`

## What it does
`snapshot()` (dump → back up → forget), `latest_snapshot_age()` for the
heartbeat, `restore()` for the drill.

## The dump is taken INTO the run, not read off disk
A `.sql` sitting in `~/cobalt-backups` from some earlier night backs up
whatever age it happens to be. `pg_dump` runs at the start of every
snapshot and the file is deleted in a `finally`, so "the database at
snapshot time" is the only thing a snapshot can contain.

## `STAGING` is a fixed path, and the first restore drill is why
The first version staged into `tempfile.mkdtemp()`. The snapshot was
perfect and the restore was unusable: inside the repository the database
lived at
`/var/folders/4b/…/cobalt-backup-egp09dbp/cobalt_brain.sql`, a new
random path every night. `restic restore --include` needs a path a human
can type, and the day it is needed is not the day to go listing
snapshots to find where the database went. It now stages at
`~/cobalt-backups/staging/cobalt_brain.sql`, always.

This is the whole argument for "proven restore" as a gate: the backup
half was already green.

## The password never touches a command line
It goes into the child's environment (`RESTIC_PASSWORD`, and the two
`B2_*` keys) and nowhere else — not a file, not `ps` output, not a log
line. `_run()` folds restic's stderr into the exception rather than
logging it raw.

## `forget` filters on the same tag the write used
`--tag cobalt-nightly`. A snapshot a human took by hand into the same
repository can never be pruned by the nightly job.

## Nothing is dumped for a run that cannot store it
`snapshot()` raises on zero armed destinations **before** the dump. A
360 MB dump written and thrown away is a real cost, and the refusal is
the point: a nightly job that runs, writes nothing and reports success
is the exact failure this design exists to prevent.
