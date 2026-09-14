# Heartbeat alerts — transition-only (2026-09-14)

Branch `ops/alerts-transition` · worktree `~/cobalt-wt/ops-alerts-transition` · Opus 5 · input `alerts-triage-2026-09-14.md` (this folder).
Ruling (Dejan 09-14, option B): alert on RED entry and recovery only; known-idle never RED; summaries 07:00 + 16:30 ET always sent. Ruled values: `heartbeat.summary_at` = ["07:00", "16:30"]; staleness key SPLIT (Dejan 09-14, second pass): `heartbeat.radar_scan_max_age_s` = 320, `radar.poll_bar_max_age_s` = 180.

## §0 Headline

- Alerts now fire on a transition only: entered RED or recovered. Known-idle states never rate RED. Summaries go out at 07:00 and 16:30 ET whether or not anything is red.
- The shared `heartbeat.radar_max_age_s` is gone. The heartbeat now uses **`heartbeat.radar_scan_max_age_s` = 320 s**. The poller now uses **`radar.poll_bar_max_age_s` = 180 s**, the same value as before.
- Replay over the real log: **402 → 6** messages in 48 h and **192 → 2** in 24 h, unchanged. Offline suite: **900 passed** (899 plus the new split test), with the same single credential-less failure.
- **RESTARTS: com.cobalt.aset com.cobalt.radar** (re-derived over the amended diff, unchanged).
- **ESCALATE: 1.** The first beat at ~20:05 sends a late **16:30 summary DM** as well as the herdr RECOVERED alert. It is not followed by silence (see DEPLOY STEP-6).

## Commit

Single commit on `ops/alerts-transition` (L46), amended.
- Code/test/config content: `04a8cc0`.
- The amend that folds this report in produces the final sha. A file cannot contain the sha of the commit that contains it. The final sha is the one on this run's last line and `git log -1 ops/alerts-transition`, and its diff against `04a8cc0` is this report file only.

## Step log (L48 — written as each step lands)

1. Worktree created off main 9c47d6f; triage copied to `alerts-triage-2026-09-14.md`.
2. Baseline `uv run pytest -q tests/cobalt` (unchanged code): **891 passed, 239 skipped, 1 failed**. The failure is `test_sheet_daymode_probe.py::TestItIsWiredIntoTheBeat::test_the_runner_asks_it_right_after_sheet_http`: `DbConfigError: Missing Postgres settings for the APP credential`. It's environmental. The worktree has no DB credentials by design (L41 interim), and the failure is pre-existing and unrelated.
3. Failing-before, oracles written first and run against unchanged code:
   - (a) transition oracle RED,RED,RED,GREEN,GREEN → `assert 3 == 2` (`['out_of_band','dm'] × 3`: every red beat re-sent both channels).
   - (b) Saturday radar with no pool row → `Probe(ok=False, detail='no radar_pool row for primary')`.
4. Implementation (see Diff summary). One test-authoring bug fixed before the failing-before run counted: oracle (a) first raised `minute must be in 0..59`, not an assertion.
5. `cobalt validate` with `COBALT_ENV` unset refuses (`EnvConfigError: COBALT_ENV is unset`) — no default, by the 09-13 ruling. Rerun with `COBALT_ENV=dev` (worktree = dev; L51's production pre-approval does not apply here).
6. `COBALT_ENV=dev uv run cobalt validate` → **exit 1**, `DbConfigError: Missing Postgres settings for the APP credential`. Every section before the DB step passed on the branch: 13 trade_defs, engine tunables, calendar, session boundaries. **Untouched main in a credential-less detached worktree gives the same exit 1 and byte-identical output.** Exit 0 is not provable offline: the "Heartbeat (F18)" line (`cli.py`, now `summary_at()`) is past the DB step. It needs the hub's credentialed run (DEPLOY STEP-2).
7. Replay oracle, real `~/cobalt/logs/heartbeat.log`, read-only. Pinned window 2026-09-12 08:00 → 2026-09-14 08:00 ET:

| | 48 h | 24 h |
|---|---|---|
| beats (all RED as logged) | 192 | 96 |
| messages BEFORE (logged `Email sent`/`DM sent`/channel-failure lines) | 402 | 192 |
| transition alerts AFTER | 1 (`RECOVERED: vault unit` 09-12 12:24) | 0 |
| summaries AFTER | 4 (09-12 16:40, 09-13 07:14, 16:32, 09-14 07:07) | 2 |
| messages AFTER (transition = email+DM, summary = DM) | 6 | 2 |

   - Triage deltas, stated not smoothed: the triage counted 193 / 194 because its window edges differ (it began at 08:15 and ended at its own run time). **The 09-12 vault episode began 00:12:27 ET, not 08:00.** The triage saw it from its window edge. Replayed over its own span (09-12 00:00 → 13:00), the episode is exactly **2** transitions: `ENTERED RED` at 00:12, `RECOVERED` at 12:24. A separate episode, 09-11 00:13 → 05:29, falls outside the window.
   - Herdr (192 beats) rates AMBER: zero transitions. Radar's no-pool-row / 182 s beats rate green under the new probe order and the 320 s threshold: zero transitions.
8. First commit on the branch (5217acc); `cobalt jobs restarts main..HEAD` derived; report and DevDocs folded in by amend (L46).
9. **Key split (ruling 09-14, second pass).** The shared key `heartbeat.radar_max_age_s` was replaced by two keys:
   - `heartbeat.radar_scan_max_age_s` = 320, read only by `heartbeat/probes.py` `radar()`.
   - `radar.poll_bar_max_age_s` = 180, read only by `radar/runner.py` → `BarPoller(max_age_s=…)`, and unit-checked in `radar/config.py` `TUNABLE_UNITS`.

   Both carry a one-line comment in `tunables.yaml` naming the ruling and date (L53). Afterwards, `git grep radar_max_age_s -- src tests configs` finds only the two YAML comments and the new test's absence assert. Tunables loaded: 45 → **46**. Dev `cobalt validate` still exits 1 at the same DB step.
10. `_inflight` cleanup: `~/cobalt/docs/_inflight/alerts-transition-2026-09-14.md` and `alerts-triage-2026-09-14.md` were deleted (docs/PLACEMENT.md: README-only since 09-13). Proof: `ls -la ~/cobalt/docs/_inflight/` → `README.md` only.
11. Re-runs over the amended tree: see Tests. Replay numbers unchanged. `cobalt jobs restarts main..HEAD` re-derived: unchanged (table below). Code commit amended → `04a8cc0`.
12. First-beat summary check. `summary_due(2026-09-14 20:05 ET, prior summary_sent={}, ["07:00","16:30"])` → `16:30`. The production row has no `summary_sent` (main never writes it), so the 20:05 beat sends the 16:30 summary late. The next beat, with `{"16:30":"2026-09-14"}`, → `None`. On 09-15 at 07:00 → `07:00`.

## Diff summary

| file | change |
|---|---|
| `src/cobalt/heartbeat/runner.py` | `PriorBeat.from_row` reads the prior `red_jobs`/`red_probes`/early-stage failures before PERSIST; `alert_keys`, `transitions`, `transition_note`; email + DM only on a non-empty transition; vault transition decided in FINALIZE against the prior `vault_outcome`. Unreadable prior fails toward alerting. `summary_at()` (list, validated ascending/unique) + `summary_due()` + `send_summary` replace `green_summary_at`/`should_send_green`; dedup in `last_result.summary_sent` |
| `src/cobalt/heartbeat/probes.py` | `radar()`: session-idle/market_reset checks moved ahead of the `row is None` check (b481bd5 class); `last_scan_at` staleness and standing `poll_failures` read `heartbeat.radar_scan_max_age_s` |
| `src/cobalt/radar/runner.py` | `BarPoller(max_age_s=)` reads `radar.poll_bar_max_age_s` |
| `src/cobalt/radar/config.py` | `TUNABLE_UNITS`: `heartbeat.radar_max_age_s` → `radar.poll_bar_max_age_s` (duration) |
| `src/cobalt/heartbeat/render.py` | `Beat.amber_jobs`, 🟡 row icon, "Amber:" DM section, `summary_body()` (RED + AMBER or "all green") |
| `src/cobalt/jobs/watchdog.py` | `Finding.amber`; `supervised_finding()` — launchd "not running" + `launchd_unmanaged` → AMBER "launchd unmanaged", `ok=True` |
| `src/cobalt/jobs/config.py` | `JobSpec.launchd_unmanaged` (launchd resident only, validated) |
| `src/cobalt/cli.py` | validate's heartbeat line reads `summary_at()` |
| `configs/cobalt/taxonomy/tunables.yaml` | `heartbeat.radar_max_age_s` (180) removed → `heartbeat.radar_scan_max_age_s: 320` + `radar.poll_bar_max_age_s: 180`, each commented with ruling + date; `heartbeat.green_summary_at` → `heartbeat.summary_at: ["07:00","16:30"]` (L53) |
| `configs/cobalt/jobs.yaml` | `com.cobalt.herdr`: `launchd_unmanaged: true`, commented INTERIM until launchd handover |
| `tests/cobalt/test_heartbeat_runner.py` | 8 new tests (a)–(e) + herdr AMBER + flag validation + summary-on-standing-red; 3 existing tests moved from `should_send_green` to `send_summary` |
| `tests/cobalt/test_radar_config.py` | expected radar tunables set uses `radar.poll_bar_max_age_s`; new `test_staleness_key_is_split_poller_180_heartbeat_320` (poller 180, heartbeat 320, old key absent) |
| DevDocs | `heartbeat/runner.md`, `heartbeat/__init__.md`, `heartbeat/render.md`, `heartbeat/probes.md` (split key named), `jobs/watchdog.md`, `jobs/config.md` |

Not changed: the beat row shape (only `summary_sent` added, `green_summary_date` left in place as dead data), the note unit, the probe set, `BarPoller`'s signature, no migration.

## Tests

| run | passed | failed | skipped |
|---|---|---|---|
| baseline `tests/cobalt`, unchanged code | 891 | 1 (env: DB creds) | 239 |
| after, first commit (5217acc) | 899 | 1 (same test, same env cause) | 239 |
| after key split, `tests/cobalt` | **900** (899 + split test) | 1 (same test, same env cause) | 239 |
| targeted: `test_heartbeat_runner.py`, `test_heartbeat.py`, `test_radar_config.py`, `test_radar_poller.py`, L45 leak scan | 61 | 0 | 0 |

| oracle | before | after |
|---|---|---|
| (a) RED,RED,RED,GREEN,GREEN → exactly 2 alerts | FAIL `3 == 2` | PASS |
| (b) Saturday radar, no pool row → green | FAIL `no radar_pool row for primary` | PASS |
| (c) 182 s gap green at 320 s; 321 s RED | — | PASS (reads `heartbeat.radar_scan_max_age_s`) |
| (d) summaries at 07:00/16:30 only, two days of 15-min beats | — | PASS |
| (e) replay oracle, real log, pinned window: 402 → 6, 192 → 2 (not skipped on this host) | — | PASS, numbers unchanged |
| (f) key split: poller 180, heartbeat 320, shared key absent | — | PASS |

L45 leak scan `test_radar_notes.py::test_screen_filter_values_live_only_in_approved_radar_fixtures` (covers `docs/40 - DevDocs`, `src/cobalt`, `configs/cobalt`, `tests/cobalt`, `ops`): PASS on the amended tree. Credential-pattern grep over both reports: no match. No credential was copied into the worktree. A DevDocs symbol-check gate was searched for in `src/`, `dev_utils/` and `tests/` and was not found, so it did not run.

## RESTARTS

`uv run cobalt jobs restarts main..HEAD`, re-derived over the amended diff:

| path | rule | restart |
|---|---|---|
| `configs/cobalt/jobs.yaml` | registry; register, no restart | - |
| `configs/cobalt/taxonomy/tunables.yaml` | resident reads | com.cobalt.aset, com.cobalt.radar |
| `src/cobalt/{cli,heartbeat/probes,heartbeat/render,heartbeat/runner,jobs/config,jobs/watchdog,radar/config,radar/runner}.py` | static import reach | com.cobalt.radar |
| docs / tests | no resident | - |

**RESTARTS: com.cobalt.aset com.cobalt.radar**. Unchanged by the split. `radar/config.py` and `radar/runner.py` joined the table, and both reach only radar. The heartbeat itself is one-shot (launchd `StartInterval` 900), so it picks up new code on its next run.

## DEPLOY (hub; ~20:05 ET 2026-09-14, inside the 20:00–21:00 pause — ruled)

Radar's aftermarket scanning session ends at 20:00. The restarts land in the pause, never during a scanning session. L43: this is tonight's one production deploy.

- **STEP-1 — merge (Dejan).** From `~/cobalt`: `git merge --ff-only ops/alerts-transition` (rebase first if main moved, L54). `git push` is Dejan's (L55).
- **STEP-2 — credentialed validate (hub).** From `~/cobalt`: `COBALT_ENV=production uv run cobalt validate` (L51). Expect **exit 0**, `46 engine tunable(s) loaded`, and the "Heartbeat (F18)" line showing summaries 07:00/16:30.
  - Also run `uv run pytest -q tests/cobalt/test_sheet_daymode_probe.py` credentialed. Expect pass.
  - A non-zero exit stops the deploy: roll back with `git revert` of the merge range (L54). Residents have not been restarted yet, so nothing else to undo.
- **STEP-3 — register (hub).** `COBALT_ENV=production uv run cobalt jobs register` (jobs.yaml changed: `launchd_unmanaged` on herdr; register, no restart).
- **STEP-4 — restarts (hub), exactly the derived list:**
  - `launchctl kickstart -k gui/$(id -u)/com.cobalt.aset`, then confirm `GET http://127.0.0.1:5010/` → 200.
  - `launchctl kickstart -k gui/$(id -u)/com.cobalt.radar`, then confirm a new PID and that the radar log shows `radar cycle:` (idle session after 20:00 is expected).
- **STEP-5 — forced beat (hub).** `launchctl kickstart -k gui/$(id -u)/com.cobalt.heartbeat`. This runs under the plist's own env: `COBALT_ENV=production`, `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think`. Do not run a bare `uv run cobalt heartbeat beat`: without `COBALT_VAULT_PATH` it writes the dev vault.
- **STEP-6 — expected first messages on that beat:**
  1. **Exactly one transition alert: `RECOVERED: com.cobalt.herdr`.** The prior row lists herdr RED; it now rates AMBER. A transition goes on both channels: **one email + one DM**.
  2. **One `SUMMARY 16:30` DM** (ESCALATE 1). It lists every RED/AMBER item, or says "all green", with herdr AMBER. The production row has no `summary_sent` yet, and `summary_due` picks the latest passed slot not sent today (step log 12).
  3. **Then silence.** Every following beat tonight sends nothing unless something enters RED or recovers. Check: `~/cobalt/logs/heartbeat.log` shows no `Email sent`/`DM sent` line on the next beat (~20:20), and `last_result.summary_sent` = `{"16:30": "2026-09-14"}`.
  - Any other RED transition on the forced beat is a real finding, not noise. Report it.
- **STEP-7 — live proof tomorrow (Dejan's glance).** At **07:00 ET 2026-09-15**, exactly one summary DM and no email. Nothing between tonight's forced beat and 07:00 unless a real transition happened. A missing 07:00 DM means a dead heartbeat or Mattermost; the summary is DM-only (ruled).

## Decisions taken (veto open)

- **Key names.** "No reader can confuse them" was taken literally, so neither key keeps the old name:
  - `heartbeat.radar_scan_max_age_s` sits in the `heartbeat.` family and names what it measures: scan age.
  - `radar.poll_bar_max_age_s` joins the `radar.poll_*` family, with value 180, unchanged.
  - Keeping `heartbeat.radar_max_age_s` for the poller would have left a `heartbeat.`-prefixed key the heartbeat never reads, next to one it does.
- **The heartbeat's standing-`poll_failures` age uses the heartbeat key (320).** The probe compares two things against a threshold: the scan age and how long a poll failure has stood. Both are the heartbeat's judgement of radar, so both read `heartbeat.radar_scan_max_age_s`. The poller's own decision to open a `stale` entry stays at 180 s. Effect: a stale-bar entry the poller opens at 180 s turns the heartbeat RED once it has stood more than 320 s. On main that age was 180 s; 320 s is the ruled heartbeat value.
- **Summary is DM-only** — accepted 09-14.
- **One `RECOVERED: com.cobalt.herdr` on the first beat** — accepted 09-14.
- **A late beat sends only the latest missed slot.** A heartbeat dead at 07:00 does not send a stale 07:00 summary at 16:45; it sends 16:30's.
- **Late-stage failures are persisted but not compared.** Failures in `persist`, `vault`, `FINALIZE` and `alerts/*` stay in the row. Only `probes`/`compose` failures and every red job/probe enter the transition set, because only they are known at alert time. The vault unit is compared in FINALIZE.

## ESCALATE

1. **The first beat is not "one RECOVERED herdr DM, then silence".** By the code as ruled, the ~20:05 forced beat sends:
   - `RECOVERED: com.cobalt.herdr` as email + DM (a transition uses both channels);
   - a late `SUMMARY 16:30` DM (`summary_due` → `16:30`; step log 12).

   Silence follows after that. This is consistent with "a late beat sends the latest missed slot", but it is not the expectation stated in the dispatch. Options:
   - accept it (no change);
   - seed `summary_sent` with today's 16:30 before STEP-5 (a production DB write, so a gated job);
   - add a rule that no slot is sent more than N hours late (a code change, new run).

   Default if not ruled: accept it. STEP-6 already expects it.

## Verdict

READY FOR MERGE. The credentialed `cobalt validate` exit 0 is DEPLOY STEP-2, run from `~/cobalt` after the ff-merge; a red result reverts the merge before any restart.
RESTARTS: com.cobalt.aset com.cobalt.radar · ESCALATE: 1 (the first beat also sends a late 16:30 summary DM)
