# S2 smoke look — 2026-09-24 night (after the 09-24 deploy)

## §0 Headline
- Replay 09-24 **FAILED** 21:40:06 ET (`StepFailed: step line failed — DeadlineExceeded: line: past the deadline 21:35:00 ET`). Smoke (21:40:52 ET) **AMBER, 36 green / 3 red** of 39 checks: K7, K10.1, K10.2.
- K9.4 fix **shows**: gainers not_archived 0 = named partial 0, losers not_archived 1 = named partial 1, K9.9 / K9.12 PASS, `archive_partial_by_side` present. K17 **gone** (no row printed; `grep "id: K17"` empty).
- `smoke green: no` — first failing clause (a): no 2026-09-24 replay run ended DONE. 3 real reds, none placed by a named ruling. ESCALATE: 5. S2 stays CLOSED (R113); this decides nothing.

## Authorization + window (all passed)
`date` = Thu Sep 24 21:40:52 EDT 2026 (in window). R43 row quotes the smoke string (cto-2026-09-21.md:54); `git log -S` → `f5c5bf0f35ff2786b8fea70983bd250b35bf0918`. Placeholder gate: no output. R67 row names this file (cto-2026-09-24.md:82); `git log -S` → `bbae298becdcae1f00f841a0316860bde0c81e5a`. R113 carries "I call this smoke test green" (cto-2026-09-23.md:121); R114 carries "yes A. Thank you." (:122).

## Step 2 — deploy row (a record)
- Last non-blank line of `reports/deploy-2026-09-24-reland.md`: `SETUPS DEPLOY RELAND DONE · reland: a2d320b8 · tag: deploy-2026-09-24 · rows: 0 (R119: NOT WRITTEN — dry run REFUSED: note absent, --dry-run cannot preview the create) · live-note: NOT RUN · S2 smoke: owed 21:10 · ESCALATE: 12`
- `git log --oneline -1 deploy-2026-09-24` → `a2d320b8 Reapply "Merge branch 'main' into deploy/stacked-0923"`.
- `grep -c -F archive_partial_by_side src/cobalt/replay/models.py` → `3` (mover-bars fix IS on the tree). `grep -n "id: K17" configs/cobalt/smoke/s2.yaml` → no output (K17 removed).
- Record: `deploy: a2d320b8` (tag deploy-2026-09-24).
- Cutoff: `git log -1 --format=%cI deploy-2026-09-19b` → `2026-09-19T15:11:42-04:00` (same as the 09-22 / 09-23 looks).

## Step 3 — replay row
- Start (replay.err): `2026-09-24 21:10:00.609 | INFO | cobalt.jobs.wrapper:job_run:173 - F17: com.cobalt.replay RUNNING (timeout 1800s, heartbeat every 600s)`
- End (replay.err, last lines): `2026-09-24 21:40:06.498 | ERROR | cobalt.replay.runner:run_nightly:484 - replay 2026-09-24 step line FAILED — DeadlineExceeded: line: past the deadline 21:35:00 ET` / `2026-09-24 21:40:06.630 | ERROR | cobalt.jobs.wrapper:job_run:192 - F17: com.cobalt.replay FAILED — StepFailed: step line failed — DeadlineExceeded: line: past the deadline 21:35:00 ET` / `FAILED: StepFailed: step line failed — DeadlineExceeded: line: past the deadline 21:35:00 ET`. → **replay ran: yes 21:40 FAILED.**
- Movers step ran before the failure: `2026-09-24 21:10:02.476 | WARNING | cobalt.replay.movers:parse_movers:216 - movers-gainers: 17 of 11673 rows have a blank Change — unranked, not stored, not benchmarked` (same for movers-losers, 21:10:04.100); one PARTIAL line (replay.err:52): `2026-09-24 21:10:37.658 | WARNING | cobalt.replay.runner:movers_step:376 - replay movers archive: <ticker> PARTIAL — bars begin 2026-09-24T13:33:00+00:00, after 2026-09-24T09:30:00-04:00 (84 i1 bars, 2026-09-24T13:33:00+00:00 → 2026-09-24T23:30:00+00:00)`. No `INCOMPLETE` line in replay.err (grep: only that one match for PARTIAL|INCOMPLETE|partial).
- Between 21:10:37.9 and 21:40:04 the last 40 lines of replay.err show no line (last card-expire INFO at 21:10:37.900, next at 21:40:04.138).
- **No `replay 2026-09-24: movers … archived … · partial <n>` summary line exists** in replay.log (grep `2026-09-24|movers`: the only 09-24 lines are line 109 and line 467 `replay 2026-09-24: scans=235 formations=197 path_b_only=115 counts={…} writes: none`, then MISS lines). The `· partial <n>` figure therefore comes only from the smoke (K9.8 / K9.11).
- replay.log:109 verbatim: `replay 2026-09-24 run replay-2026-09-24-20260924T211000-442467: tonight's 20:30 ET run: done, exit 0, finished 20:54:22 ET` — see ESCALATE 4.

## Step 4 — the smoke output (verbatim; command exit 1; it printed `wrote /Users/cobalt/cobalt/docs/40 - DevDocs/reports/s2-smoke-2026-09-24.md`)

```
| # | check | verdict | evidence |
|---|---|---|---|
| K1 | com.cobalt.radar launchctl | PASS | state=running, pid=53832, last exit code=(never exited) |
| K2 | radar_pool primary | PASS | state_valid ok; within_cap ok; failed_stage ok |
| K3 | membership value column (post-deploy admissions and re-scans) | PASS | metric_missing ok; rescanned_metric_missing ok |
| K4.1 | sheet /api/health | PASS | HTTP 200 |
| K4.2 | sheet GET / | PASS | HTTP 200 |
| K4.3 | sheet GET /radar with value column | PASS | HTTP 200 |
| K4.4 | sheet /api/radar/pool | PASS | HTTP 200 |
| K5.1 | P2 seam — latest radar_score_run | PASS | latest_status ok; failed_stage ok |
| K5.2 | P2 seam — radar.cards_enabled reported | PASS | cards_enabled ok |
| K6 | picks — one row per post-deploy FILLED transition | PASS | missing ok |
| K7 | replay job — last run | FAIL | state 'failed' (expected 'done'); exit_code 1 (expected 0) |
| K8.1 | missed — the replay job's own counters (system side) | PASS | com.cobalt.replay: state=failed, exit=1, finished_at=2026-09-25 01:40:06.609642+00:00 |
| K8.2 | missed — card rows complete (user side) | PASS | incomplete ok |
| K8.3 | missed — the corpus and the job agree on the card count | PASS | K8.1 = 13, K8.2 = 13 (op eq) |
| K9.1 | movers_daily — gainers stored (user side) | PASS | top_n ok |
| K9.2 | movers — what the gainers export allowed (system side) | PASS | com.cobalt.replay: state=failed, exit=1, finished_at=2026-09-25 01:40:06.609642+00:00 |
| K9.3 | movers — gainers stored = what the export allowed | PASS | K9.1 = 20, K9.2 = 20 (op eq) |
| K9.4 | movers_daily — losers stored (user side) | PASS | top_n ok |
| K9.5 | movers — what the losers export allowed (system side) | PASS | com.cobalt.replay: state=failed, exit=1, finished_at=2026-09-25 01:40:06.609642+00:00 |
| K9.6 | movers — losers stored = what the export allowed | PASS | K9.4 = 20, K9.5 = 20 (op eq) |
| K9.7 | movers_daily — gainers not archived (user side) | PASS | not_archived ok |
| K9.8 | movers — gainers the replay named partial (system side) | PASS | com.cobalt.replay: state=failed, exit=1, finished_at=2026-09-25 01:40:06.609642+00:00 |
| K9.9 | movers — every gainers row not archived is named partial | PASS | K9.7 = 0, K9.8 = 0 (op eq) |
| K9.10 | movers_daily — losers not archived (user side) | PASS | not_archived ok |
| K9.11 | movers — losers the replay named partial (system side) | PASS | com.cobalt.replay: state=failed, exit=1, finished_at=2026-09-25 01:40:06.609642+00:00 |
| K9.12 | movers — every losers row not archived is named partial | PASS | K9.10 = 1, K9.11 = 1 (op eq) |
| K10.1 | miss line unit in the DRC note | FAIL | section 'drc-misses' absent in /Users/cobalt/Vault/Think/1 - Trading/5 - Review/DRC-2026-09-24.md |
| K10.2 | miss line vault_writes row | FAIL | writes ge 1 (actual 0) |
| K11.1 | heartbeat — last beat age | PASS | com.cobalt.heartbeat: state=done, exit=0, finished_at=2026-09-25 01:27:08.129224+00:00 |
| K11.2 | heartbeat — database probe OK | PASS | 1 line(s) match '^OK +database ' |
| K11.3 | heartbeat — sheet HTTP probe OK | PASS | 1 line(s) match '^OK +sheet HTTP ' |
| K12.1 | prefill-daily last run | PASS | com.cobalt.prefill-daily: state=done, exit=0, finished_at=2026-09-24 09:15:01.037712+00:00 |
| K12.2 | prefill-drc last run | PASS | com.cobalt.prefill-drc: state=done, exit=0, finished_at=2026-09-24 19:40:00.713483+00:00 |
| K13 | archiver freshness (cadence-aware) | PASS | com.cobalt.archiver: state=done, exit=0, finished_at=2026-09-25 00:54:22.941066+00:00 |
| K14 | backup last run | PASS | com.cobalt.backup: state=done, exit=0, finished_at=2026-09-25 01:40:18.608230+00:00 |
| K15 | heartbeat summary sent at the last slot | PASS | com.cobalt.heartbeat: state=done, exit=0, finished_at=2026-09-25 01:27:08.129224+00:00 |
| K16.1 | cards-expire last run | PASS | com.cobalt.cards-expire: state=done, exit=0, finished_at=2026-09-24 20:05:00.748138+00:00 |
| K16.2 | daymode-propose last run | PASS | com.cobalt.daymode-propose: state=done, exit=0, finished_at=2026-09-24 13:00:00.805754+00:00 |
| K18 | jobs registry vs launchd | PASS | 16 registry label(s) match launchd |

OVERALL: AMBER
```

## Step 5 — the table
Last-night column = `s2-smoke-look-2026-09-23.md` table (32/34: K9.4 FAIL, K17 FAIL, all else PASS; K9.7–K9.12 did not exist). "Formed card?" = per that look's structure: K6 only (guarded by `known_if` fills=0); every other check no.

| K | result | expected tonight? | last night (09-23) | formed card? | evidence |
|---|---|---|---|---|---|
| K1 | PASS | — | PASS | no | state=running, pid=53832 |
| K2 | PASS | — | PASS | no | state_valid / within_cap / failed_stage ok |
| K3 | PASS | — (not red; no R32 reading needed) | PASS | no | metric_missing ok; rescanned_metric_missing ok |
| K4.1–K4.4 | PASS | — | PASS | no | HTTP 200 ×4 |
| K5.1–K5.2 | PASS | — | PASS | no | ok |
| K6 | PASS | — | PASS | yes (`known_if` fills=0; not consulted, PASS) | missing ok |
| **K7** | **FAIL** | **NO → real red** (no ruling) | PASS | no | state 'failed' (expected 'done'); exit_code 1 (expected 0) |
| K8.1 | PASS | — | PASS | no | state=failed, exit=1, finished 2026-09-25 01:40:06 UTC (counter read from a failed row) |
| K8.2 / K8.3 | PASS | — | PASS | no | incomplete ok; K8.1 = 13, K8.2 = 13 |
| K9.1 / K9.4 | PASS | — | K9.1 PASS / K9.4 FAIL (`not_archived eq 0 (actual 1)`) | no | `top_n ok` only — `not_archived` NOT printed in K9.1 / K9.4 evidence (ESCALATE 5); `stored` = 20 / 20 (K9.3 / K9.6) |
| K9.2 / K9.3 / K9.5 / K9.6 | PASS | — | PASS | no | K9.1 = 20, K9.2 = 20; K9.4 = 20, K9.5 = 20 |
| K9.7 | PASS | — | (new) | no | gainers `not_archived` ok; K9.9 prints 0 |
| K9.8 | PASS | — | (new) | no | `archive_partial_by_side.gainers` = 0 (via K9.9); `archive_partial` list size not printed |
| K9.9 | PASS | — | (new) | no | K9.7 = 0, K9.8 = 0 (op eq) |
| K9.10 | PASS | — | (new) | no | losers `not_archived` ok; K9.12 prints 1 |
| K9.11 | PASS | — | (new) | no | `archive_partial_by_side.losers` = 1 (via K9.12); list size not printed |
| K9.12 | PASS | — | (new) | no | K9.10 = 1, K9.11 = 1 (op eq) |
| **K10.1** | **FAIL** | **NO → real red** (no ruling) | PASS | no | section 'drc-misses' absent in `DRC-2026-09-24.md` |
| **K10.2** | **FAIL** | **NO → real red** (no ruling) | PASS | no | writes ge 1 (actual 0) |
| K11.1–K11.3 | PASS | — | PASS | no | heartbeat done exit 0 01:27:08 UTC; both probes OK |
| K12.1 / K12.2 | PASS | — | PASS | no | prefill-daily / prefill-drc done exit 0 |
| K13 | PASS | — | PASS | no | archiver finished 2026-09-25 00:54:22 UTC |
| K14 | PASS | — | PASS | no | backup finished 2026-09-25 01:40:18 UTC |
| K15 | PASS | — | PASS | no | heartbeat done exit 0 |
| K16.1 / K16.2 | PASS | — | PASS | no | cards-expire / daymode-propose done exit 0 |
| K17 | **absent** | expected (R114) | FAIL | — | no K17 row in the output; `grep "id: K17"` empty |
| K18 | PASS | — | PASS | no | 16 registry labels match launchd |

Checks: 39 printed, 36 PASS, 3 FAIL (K7, K10.1, K10.2). Last night's K9.4 and K17 reds cleared.
Placement note on K10.1 / K10.2: no ruling covers them, so they are real reds. Evidence only: the 09-23 replay's miss-line write appears in replay.log:96–108 immediately before `… · line updated`; tonight's run failed AT step `line` (log above), and `writes: 0`. I do not rule on the cause.

## K9.4 AFTER THE FIX
Proof (mover-bars build ESCALATE 1 / FIX 1, INDEX CARD 7), clause by clause:
1. **K9.4 PASS with `top_n` not null** — PASS: `K9.4 | PASS | top_n ok`; K9.6: `K9.4 = 20, K9.5 = 20`. The `not_archived` figure is not printed by K9.4 itself (printed by K9.7 / K9.10 instead, see 2).
2. **Per side, not-archived = the job row's `archive_partial_by_side`** — holds. Gainers: `K9.7 = 0, K9.8 = 0 (op eq)` → K9.9 PASS. Losers: `K9.10 = 1, K9.11 = 1 (op eq)` → K9.12 PASS. Log corroborates: exactly one PARTIAL WARNING for one mover (`<ticker>`), zero INCOMPLETE lines (replay.err:52).
3. **K9.8 / K9.11 read a present `archive_partial_by_side`, not a missing-key FAIL** — holds: both PASS with numeric values (0 and 1) → the job row is post-deploy. `archive_partial` list size: not printed by the smoke (not read; no DB command allowed).
4. **No not-archived row the marker does not cover** (no zero-bars / fetch-failure `archive_incomplete`) — consistent: counts equal on both sides; no INCOMPLETE log line.

Caveat, stated plainly: the job row read is `state=failed` (the run died later, at step `line`); the movers step itself completed before that.

`K9.4: not_archived 1 · named partial 1 (PASS)` (losers); gainers `not_archived 0 · named partial 0 (PASS)`.

## SMOKE GREEN — `smoke green: no`
- (a) a 2026-09-24 replay run that ended DONE — **NOT MET**: run `replay-2026-09-24-20260924T211000-442467` ended FAILED 21:40:06 ET (`step line failed — DeadlineExceeded: line: past the deadline 21:35:00 ET`); K7 FAIL agrees. **First failing clause.**
- (b) step 4 ran — MET (command ran from `~/cobalt`, exit 1, AMBER, 39 checks).
- (c) real reds = 0 — **NOT MET**: 3 real reds (K7, K10.1, K10.2); no named ruling places any (R32 not applicable: K3 PASS; R113 was 09-23 only, L73). 0 `fix not live`, 0 UNPLACED.

## ESCALATE
1. **K7 real red** — replay job `failed`, exit 1, DeadlineExceeded at step `line` (deadline 21:35:00 ET), job wrapper timeout 1800 s from a 21:10:00 start.
2. **K10.1 real red** — `drc-misses` section absent in `DRC-2026-09-24.md`.
3. **K10.2 real red** — vault_writes writes 0 (need ≥ 1).
4. **replay.log:109 contradicts the failed run** — `replay 2026-09-24 run replay-2026-09-24-20260924T211000-442467: tonight's 20:30 ET run: done, exit 0, finished 20:54:22 ET`; the run id is tonight's 21:10 run, which FAILED at 21:40:06; `20:54:22 ET` equals K13's archiver `finished_at` (2026-09-25 00:54:22 UTC). Not explained here (UNPLACED).
5. **K9.1 / K9.4 no longer print `not_archived`** — evidence reads `top_n ok` only (last night: `top_n ok; not_archived ok`); INDEX CARD (2) expected them to PRINT it. K9.7 / K9.10 / K9.9 / K9.12 supply the numbers, so the proof still reads, but the print differs from the card.

## DIGEST FOR THE DESK
- Replay 09-24 FAILED 21:40:06 ET, step `line`, DeadlineExceeded past 21:35 ET; started 21:10:00; no log line 21:10:38 → 21:40:04 in the tail.
- Smoke AMBER 36/39: reds K7, K10.1, K10.2 — all real (no ruling), the miss line was not written for 09-24.
- K9.4 fix shows: gainers 0/0, losers 1/1 (K9.9 / K9.12 PASS, `archive_partial_by_side` present, one PARTIAL log line, no INCOMPLETE). K17 gone (R114).
- K3 PASS (no HOLD/RETAIN reading needed). Deploy a2d320b8 on the tree (`archive_partial_by_side` in models.py: 3 hits).
- `smoke green: no` — clause (a). Decides nothing about S2 (closed R113).
- The smoke command itself wrote `reports/s2-smoke-2026-09-24.md` (uncommitted, its own behaviour); this report is my one Write.
- replay.log:109 anomaly (ESCALATE 4) and the K9.1 / K9.4 print change (ESCALATE 5) are unplaced.
- Nothing launched, no DB command other than the smoke, no git write.

S2 SMOKE LOOK DONE · deploy: deploy-2026-09-24 · replay ran: yes 21:40 FAILED · checks: 36 green / 3 red · K9.4: not_archived 1 · named partial 1 (PASS) · real reds: 3 · smoke green: no · ESCALATE: 5
