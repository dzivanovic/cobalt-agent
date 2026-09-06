# `ops/pending/` — plists that are deliberately NOT loaded

`cobalt validate` cross-checks `configs/cobalt/jobs.yaml` against
`ops/com.cobalt.*.plist` and fails on a job in one and not the other —
a registry that has drifted from launchd reports green for a job that
no longer exists. That check globs `ops/` only, never this directory.

A plist lives here when the job is **written and tested but must not
run yet**. It is not a draft folder: what is here is finished, and the
thing missing is an input from outside the repo.

| plist | why it is not loaded | what unblocks it |
|---|---|---|
| _(empty)_ | — | — |

**Nothing is pending today.** `com.cobalt.backup.plist` was the only
occupant; it was armed on 2026-09-05 when the backup SSD was mounted,
and moved to `ops/`. Its own header now records what the five steps
were and which leg (B2) is still missing.

This directory stays, empty, because the shape it enforces is worth
keeping: a finished job whose only blocker is an input from outside the
repo waits HERE, out of `cobalt validate`'s glob, rather than being
loaded early to fail nightly.

**Arming is never just `launchctl load`.** Every job here needs its
`configs/cobalt/jobs.yaml` row, its heartbeat probe wiring, and its
config switched on in the same commit, or `cobalt validate` will fail —
which is the check doing its job.
