# `src/cobalt/heartbeat/probes.py`

## What it does
One function per question, each returning a `Probe(name, ok, detail,
unknown)`.

`sheet_http` · `database` · `obsidian` · `mainframe` ·
`archiver_freshness` · `backup_freshness` · `vaultwrite_blocks` ·
`redactions`.

## `unknown` is red, and separately marked
A probe that could not run renders `??` rather than `RED`, so an
operator knows they are looking at ignorance rather than at a diagnosis
— but it still fails the beat.

## `obsidian` reads the same call the writer reads
`cobalt.obsidian.sync_status()`. The heartbeat and the vault writer can
never disagree about the wording of "Obsidian is not running — will not
sync".

## `archiver_freshness`, and the day-one rule
Reads the job row's `finished_at` **and** `last_result.rows_written`.
Red on: MISSED against the archiver's own Mon-Fri cadence (via
`cobalt.jobs.watchdog.is_missed`, `jobs.missed_grace_min`), a non-zero
exit, or zero rows written.

**Changed 2026-09-06** (RED incident that morning): this used to check a
flat `now - finished_at > heartbeat.archiver_max_age_min` (26h) window
instead. A flat window cannot tell a genuine miss from an ordinary
Friday-to-Monday gap, and it bit for real: the F17 wrapper was
registered 22:19 ET Friday 2026-09-04, *after* that evening's 20:30 run
had already completed via the pre-wrapper code path, so `finished_at`
stayed NULL with nothing wrong — and the flat window expired just after
midnight Saturday, painting the whole weekend red for a job not due
again until Monday evening. `is_missed` already had the right,
cadence-aware arithmetic (and its own tests for "a due moment before
registration is not missed") — this probe now reuses it instead of a
second, flatter copy of the same question.

A row that has **never** completed a run and has had no due moment
since it was registered is **not** red — the same registration-cutoff
rule `is_missed` already enforces for the watchdog's MISSED finding.

## `backup_freshness` — three different reds, and they are not the same
Wired into the runner on 2026-09-05, when the SSD leg was armed (before
that it was written, tested, and deliberately not on the beat).

* **no destination armed** — red, `unknown=False`. The probe ran fine;
  the answer is simply "there is no backup". `??` would imply the
  question could not be asked.
* **armed but the disk is unplugged** — red, `unknown=True`, and the
  detail is `BackupError`'s own first sentence, which names the mount:
  `ssd: /Volumes/COBALT-BACKUP is NOT MOUNTED`. This is the one place a
  probe passes an exception's *message* through rather than its type,
  and it is deliberate: `BackupError`'s text is credential-free by
  contract, and a beat that said only `BackupError` would send someone
  to read a log to learn they need to plug a disk in. Any other
  exception type still degrades to the type name.
* **armed, reachable, stale** — red against
  `heartbeat.backup_max_age_min` (1560 min = 26 h, not 24: the job runs
  at 21:40 and a snapshot that starts late must not alarm the next
  night).

## `vaultwrite_blocks` reports two numbers, never summed
`refused` (the guard working) and `ungated_run` (the migration/repair
carve-out being used — RULED 2026-09-04). They share a counter because
both are "a write met the market_reset window tonight", but reading five
repairs as five refusals would send someone hunting a bug that is not
there.

## Thresholds are tunables rows (F16)
`heartbeat.probe_timeout_s`, `heartbeat.backup_max_age_min`,
`jobs.missed_grace_min` (shared with the F17 watchdog — see above). No
literal in a predicate.

---

## 2026-09-08 — ADR-0008 (two-layer data model)

The `database` probe names no table but still has to declare a side:
SYSTEM. A liveness probe must never be the thing that opens user data.
