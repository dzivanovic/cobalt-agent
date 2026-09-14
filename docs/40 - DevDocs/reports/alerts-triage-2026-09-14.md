# Heartbeat alert triage — 2026-09-14

READ-ONLY diagnosis. No code/config changed. Repo: /Users/cobalt/cobalt @ main
(clean except unrelated pre-existing `configs/cobalt/rules.yaml` / seat-usage.md diffs).

## 1. Alert path

One beat = `run_beat()` in `src/cobalt/heartbeat/runner.py:438-492`, stages in order
PROBES → COMPOSE → ALERTS → PERSIST → VAULT → FINALIZE.

- ALERTS stage: `_run_alerts()` (`runner.py:322-344`).
  - `beat.green` → `should_send_green()` (`runner.py:200-212`) — the ONLY
    existing dedup, gated on `heartbeat.green_summary_at` and a `green_summary_date`
    string stored in the job row.
  - `not beat.green` (i.e. ANY red, every single beat) → unconditionally calls
    `_attempt_alert(beat, "out-of-band", out_of_band)` then
    `_attempt_alert(beat, "red-dm", send_dm)` (`runner.py:339-344`). No condition,
    no counter, no prior-state read.
- `out_of_band()` = email over Layer-B OAuth (`runner.py:229-280`), runs FIRST.
- `send_dm()` = Mattermost DM (`runner.py:215-226`), runs second, carries the
  email outcome in its body.
- **Nothing today compares this beat to the previous one.** Confirmed by
  reading `_run_alerts`, `should_send_green`, and grepping
  `notify/*.py` + `heartbeat/*.py` for "previous/last_beat/dedup/diff" — the
  only hit is the green-summary dedup above. Every RED beat re-sends both
  channels regardless of whether the prior beat was also RED.

## 2. Persistence

Table `cobalt_jobs` (`src/cobalt/jobs/store.py`), one row per `label`, primary
key `label`. The heartbeat's own row is `label = 'com.cobalt.heartbeat'`.

- `record_heartbeat_result()` (`store.py:218-238`) does
  `last_result = COALESCE(last_result,'{}'::jsonb) || %s::jsonb` — a **merge
  overwrite of the SAME row**, called twice per beat (PERSIST at
  `runner.py:463-468`, FINALIZE at `runner.py:412-433`). `_beat_result()`
  (`runner.py:347-358`) already builds `{green, red_jobs, red_probes,
  stage_failures, kill_switch, green_summary_date}` every beat.
- **No per-beat history is retained** — each beat's `last_result` replaces the
  prior beat's. There is no beat-log table, only this always-current row.
- **A previous-beat comparison IS possible without a migration**: `store.get(
  JOB_LABEL)` read at the top of the ALERTS stage, BEFORE `_persist_beat()`
  overwrites it, returns the prior beat's `red_jobs`/`red_probes` — exactly
  the pattern `should_send_green` already uses for its own dedup. Job-level
  red/idle state for individual jobs (herdr, radar, archiver) also lives as
  their own `cobalt_jobs` rows, read fresh every beat by the probes.

## 3. Current RED sources — last 48h (line 31927 → EOF, `logs/heartbeat.log`, 193/193 beats RED, 0 GREEN)

| Source | Count (48h) | Cause class | Detail |
|---|---|---|---|
| `com.cobalt.herdr` (launchd job probe) | 193/193 | **known-idle** | `RED com.cobalt.herdr failed loaded, not running (last exit 0) [launchd probe]` — herdr is hand-started outside launchd per the 2026-09-08 handover carve-out (`configs/cobalt/jobs.yaml:131-141`, `enabled: true`, `supervisor: launchd`, not yet bootstrapped). The `herdr` PROBE itself (`probes.py:577-669`, socket+`agent list`) is green all 193 beats — it's reachable. Only the job-row launchd-liveness check rates it RED. |
| `radar` (probe) | 66/193 | 64 = **known-idle bug**, 2 = **probe-threshold** | 64× `"no radar_pool row for primary"` — `probes.py:82-84` checks `row is None` and returns RED **before** the session-idle check at `probes.py:86-90` ever runs. During windows with no pool row yet (session not started), this should fall through to the idle-session green but never reaches that code. 2× `"last_scan_at stale"` at 2026-09-14 10:03:49 UTC and **11:19:25 UTC (= 07:19:25 EDT, the named event)** — beat fired at 07:22:27 EDT, gap ≈182s vs threshold `heartbeat.radar_max_age_s = 180s` (`configs/cobalt/taxonomy/tunables.yaml:436-438`, beat cadence 15 min). A 2-second overshoot on a 180s threshold with a 15-min beat is exactly "probe staleness under 3 cycles" — self-recovered next beat. |
| `vault unit` | 17/193 | **real failure (resolved)** | `"failed — daily-note writer returned no result"` (`runner.py:397-398`, `_run_vault_stage`), continuous 2026-09-12 08:00–12:16 EDT (~4h15m), then clean. Not idle, not threshold — a genuine incident, already self-resolved; last 48h's tail (2026-09-14) is vault-clean. |
| `com.cobalt.archiver` | 0/193 | n/a in window | No archiver RED in the 48h window — `is_missed()` cadence logic (`probes.py:257-324`, reusing `jobs/watchdog.py`'s `is_missed`) is correctly treating the archiver's Mon–Fri, evening-run cadence as idle outside due windows. Named in the ruling as a class, not currently firing. |

Every RED beat in the window is `herdr` alone, or `herdr` + `radar`, or
`herdr` + `vault` — never a clean GREEN, confirming the 09-08 blackout
mechanism: standing REDs (mostly known-idle) never let a beat go green, so
every 15-minute cycle re-alerts.

## 4. Volume — last 24h (line 35496 → EOF)

- 97/97 beats RED (0 green summaries — none due at `17:30`).
- **97 email sends + 97 Mattermost DMs = 194 alert messages in 24h.**
- This is the before-number the fix is measured against.

## 5. Fix shape — 16:00 window

Smallest change = read-before-overwrite transition diff in `_run_alerts`,
plus a known-idle filter and two scheduled summaries. **No migration** — see
§2, `cobalt_jobs.last_result` already carries `red_jobs`/`red_probes`.

- `runner.py` (`_run_alerts`, `runner.py:322-344`): before calling
  `_persist_beat`, read `store.get(JOB_LABEL)`'s prior `red_jobs ∪ red_probes`
  set (available pre-overwrite, per §2); compute `newly_red = current - prior`,
  `recovered = prior - current`. Send out-of-band+DM only when `newly_red or
  recovered` is non-empty, or when the scheduled-summary predicate below is true.
- Known-idle filter, applied before the transition diff: (a) fix the radar
  probe-order bug — move the session-idle check (`probes.py:86-90`) above the
  `row is None` check (`probes.py:82-84`), 3-line reorder; (b) widen
  `heartbeat.radar_max_age_s` in `tunables.yaml` from 180s to ≈2 beat
  cycles (e.g. 1800s) — config, not code, per L53; (c) herdr launchd-probe
  known-idle needs a config flag (new `jobs.yaml` key, e.g.
  `launchd_probe_informational: true` on `com.cobalt.herdr`) read by the
  transition filter, not by `sweep()` itself — it must stay in the row as
  data, only excluded from the alert decision.
- Two summaries: replace `should_send_green`'s single `green_summary_at` gate
  with two tunables `heartbeat.summary_at_am` (07:00) / `heartbeat.summary_at_pm`
  (16:30) in `tunables.yaml` (config, L53), reusing the same
  `last_result.green_summary_date`-style dedup keyed per slot; summary fires
  regardless of green/red and lists standing REDs.
- Files touched: `src/cobalt/heartbeat/runner.py`, `src/cobalt/heartbeat/probes.py`,
  `configs/cobalt/taxonomy/tunables.yaml`, `configs/cobalt/jobs.yaml` (herdr flag),
  `tests/cobalt/test_heartbeat_runner.py` (new cases).
- **RESTARTS: none.** `com.cobalt.heartbeat` is one-shot under launchd
  (`StartInterval`, not a resident) and reads new code every invocation —
  same conclusion as `docs/40 - DevDocs/reports/heartbeat-fix-2026-09-10.md`.
  Config changes (tunables/jobs.yaml) are read live, no bounce needed either.
- Test oracle: a replay harness that feeds the last 48h of `heartbeat.log`
  beats (or the underlying `cobalt_jobs` reconstructed red/green sets per
  beat) through the new `_run_alerts` decision function and asserts the
  alert count drops from 194/24h to a small number — 1 transition-in
  (herdr/radar/vault noise suppressed as known-idle or non-transition), 1
  transition-out per real recovery (the 09-12 vault incident → exactly 2:
  RED at 08:00, recovered ~12:16), plus exactly 2 scheduled summaries/day.

ESCALATE: none
