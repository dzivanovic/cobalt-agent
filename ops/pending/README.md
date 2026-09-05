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
| `com.cobalt.backup.plist` | Neither destination the backup ruling names exists on this host (2026-09-04): no external SSD is mounted, and the vault holds no B2 credential. Loading it would fail every night at 21:40 and — since S1-P3 made the heartbeat ask launchd about every registered job — paint the beat red and DM every 15 minutes for a gap already written down in the ledger. | An SSD mounted or a B2 bucket, plus the secrets listed in that plist's own header. The header carries the full five-step arming procedure. |

**Arming is never just `launchctl load`.** Every job here needs its
`configs/cobalt/jobs.yaml` row, its heartbeat probe wiring, and its
config switched on in the same commit, or `cobalt validate` will fail —
which is the check doing its job.
