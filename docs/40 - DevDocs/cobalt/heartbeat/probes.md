# `src/cobalt/heartbeat/probes.py`

S2-P1 adds the radar probe's disabled, missing, paused, idle, stale, degraded, failed-stage, mirror, and poll-failure branches.

## What it does
One function per question, each returning a `Probe(name, ok, detail,
unknown)`.

`sheet_http` · `database` · `obsidian` · `mainframe` ·
`archiver_freshness` · `backup_freshness` · `vaultwrite_blocks` ·
`redactions`.

## `radar` asks the session before the pool row (2026-09-14)
Outside a scanning session (premarket, RTH, aftermarket) the probe
returns idle or paused green before it looks for the `radar_pool` row.
It used to return RED "no radar_pool row for primary" first, which
painted every weekend and pre-session gap red: 64 beats in the 09-14
triage. Same fix class as `archiver_freshness` below (b481bd5). Inside a
session a missing row is still RED. `last_scan_at` staleness and a
standing `poll_failures` entry are measured against
`heartbeat.radar_scan_max_age_s` = 320 s (ruled 09-14: 3 × the 100 s
cycle + jitter). That key is the heartbeat's alone: the poller's RTH
bar-staleness threshold is `radar.poll_bar_max_age_s` = 180 s (split
ruled 09-14).

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

---

## 2026-09-19 — the archiver probe sees unresolved archive incidents

Append-only FINAL design §11 and spec **O-7**: `archiver_freshness` is
NOT GREEN while any `system.archive_incidents` row is unresolved. The
desk's safe default for wording and colour is the one the spec named —
"not green = the probe's existing FAIL form, detail names the incident
count".

WHY THE HEARTBEAT CARRIES IT. Known limit 3 (spec §12): a withheld
target's new bars age out of the vendor window (i5 ≈ 21 days) if nobody
repairs it. The incident list and this probe ARE the alarm. A dashboard
that stayed green through a fortnight of withholding would make `append`
worse than the overlay it replaces.

The probe splits into two named pieces:

- `_archiver_run_probe(row, ts)` — today's verdict on the last RUN,
  unchanged: `is_missed` for the cadence, then exit code, then
  `rows_written`.
- `_with_archive_incidents(base, incidents)` — the fold. **Zero
  incidents returns `base` ITSELF**, not a rebuilt equal one, so "an
  upsert night's probe is byte-identical to today's" is true by
  construction rather than by careful copying — and a test asserts that
  identity, not just equality.
- `_read_archive_incidents()` — the production reader (read-only,
  `archiver.incidents.unresolved`). `archiver_freshness(incidents=…)` is
  the test seam that replaces exactly it.

An UNREADABLE table is RED, names the migration
(`0011_archive_incidents.sql`) and the command that applies it — the
alarm cannot be read, so nothing here can be called green — **and it
does not raise**: L1 says fail LOUD, not take the whole heartbeat run
down with it. The run's own detail is kept on the line either way, so an
operator sees both facts at once.

An unresolved incident's line names the COUNT, the OLDEST kind with its
target and first-seen date, the tally by kind, and
`cobalt archiver incidents`.

NOTE for `tests/cobalt/test_heartbeat.py`: that file is about run
freshness and has never had a database, so an autouse fixture pins
`_read_archive_incidents` to "no incidents" there. The incident
behaviour, including the unreadable case, lives in
`test_heartbeat_archiver_incidents.py`.

## 2026-10-18 — f20-cos-1018
F20 C4b (F-27): `cos(now)` — RED on a missing or stale `com.cobalt.cos` heartbeat (older than `timeout_s / jobs.heartbeat_fraction`) or a last turn `failed`; `hitl(now)` — RED on a `pending` request past its TTL or any `failed` execution. RED is `ok=False`; no AMBER. While the registry row is `enabled: false` both return ok with detail `unknown — NOT PROBED …`, never red, and read nothing. Tests: `test_cos_probes.py`.

## 2026-10-20 — cos-tunables
`cos` and `hitl`, once the row is enabled, return ok `unknown — NOT PROBED, OWED (deferred bootstrap)` when `bootstrap_owed()` lists `com.cobalt.cos`, before any store is built; `BootstrapOwedError` is not caught.

## 2026-10-20 — cos-tunables check
Two tests pin P1 (check O2, O4): `test_an_unreadable_owed_file_raises_through_both_probes` and `test_the_runner_path_reads_the_real_row_then_the_owed_file` (the `enabled=None` call the runner makes). No code change.

## 2026-10-20 — cos-tunables fr1
An unreadable or malformed owed file (`BootstrapOwedError`) now makes `cos` and `hitl` RED, `ok=False` with detail `bootstrap-owed.json unreadable: <error>`, never a raise out of `take_beat`, so the beat's other probes still land (check O1). This supersedes the "`BootstrapOwedError` is not caught" line of the cos-tunables section; `test_an_unreadable_owed_file_is_a_red_probe_never_a_raise` replaces the raise test.

## 2026-10-21 — cos-tunables fr1 check
`test_an_unreadable_owed_file_is_a_red_probe_never_a_raise` now also asserts the `BootstrapOwedError` reason (`not JSON` / `not a JSON object keyed by label`) in each red detail, so a detail without the error text fails (check A1). No code change.
