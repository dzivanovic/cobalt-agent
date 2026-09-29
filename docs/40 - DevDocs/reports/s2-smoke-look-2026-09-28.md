# S2 smoke look — MON 2026-09-28 (after the 21:10 replay)

## §0 Headline
- Replay fix: **REPLAY FIX PROVEN**. The 09-28 21:10 replay ended `DONE` at 21:24:56 ET (deadline 21:35:00), and the miss line has no `PARTIAL` clause.
- Smoke: **AMBER, 1 real red** — K8.1 (`last_result.input_stale = 1`, expected 0), UNPLACED. K7, K10.1 and K10.2 are green.
- Smoke green: **no** (clause c).
- Deploy `3349466f` / tag `deploy-2026-09-27` is on production's tree (both greps = 1).
- H1 dry-run: UNPROVEN in the deploy report; stale-score census `<np0>` 190 → `<np1>` 190.

Authorization, each verified in its own call at 21:41 ET:
- R43 row present in `cto-2026-09-21.md`, string count 1; `git log -S` → `f5c5bf0f35ff2786b8fea70983bd250b35bf0918`.
- 09-27 R32 row prints and quotes "yes A".
- Placeholder gate: no output (clean).
- R168 row in `cto-2026-09-28.md` names this file; `git log -S` → `0f15ada75128529129af4b79a7ea9e28a5eaba74`.

## THE DEPLOY (step 2 — a record)
- `date`: `Mon Sep 28 21:41:37 EDT 2026` (inside the window).
- Last non-blank line of `deploy-2026-09-27.md`: `STACKED DEPLOY DONE 3349466f · tag deploy-2026-09-27 · branches: 4 · migrations: 0014 0015 0017 · residents down 220 s · /radar 200 · rollback: not used · ESCALATE: 14`
- `git log --oneline -1 deploy-2026-09-27`: `3349466f Merge branch 'main' into deploy/stacked-0925`
- `grep -c "def prepare_member"` → 1, so the replay fix is on the tree.
- `grep -c 'EVALUATOR_VERSION = "s2p2.3"'` → 1, so the stale score is on the tree.
- Record: `deploy: 3349466f`.

## THE REPLAY ROW (step 3, 2026-09-28 run only)
- Start line (`replay.err`): `2026-09-28 21:10:00.693 | INFO | cobalt.jobs.wrapper:job_run:173 - F17: com.cobalt.replay RUNNING (timeout 1800s, heartbeat every 600s)`
- Formations summary line (`replay.log` last line): `replay 2026-09-28: movers 40 · archived 39 · partial 1 · card misses 27 · mover misses 30 · input_stale 1 · formations s2p2.3 (125 misses, 90 suppressed) · line updated`
  - It is not in the `scans=… formations=…` shape the prompt expected. It carries no ` · CUT before` suffix.
- CUT warning: none. The only WARNINGs in the 09-28 run are the movers blank-Change rows and `GETY PARTIAL — bars end 2026-09-28T18:31:00+00:00, before 2026-09-28T16:00:00-04:00`.
- ERROR in the 09-28 run: `2026-09-28 21:10:46.907 | ERROR | cobalt.replay.runner:cards_step:422 - replay card 433 <ticker>: input_stale: bars end 2026-09-28T15:03:00+00:00, before 2026-09-28T16:00:00-04:00`
- Last line, `replay.err`: `2026-09-28 21:24:56.633 | INFO | cobalt.jobs.wrapper:job_run:199 - F17: com.cobalt.replay DONE`
- `grep -c -F "DeadlineExceeded" replay.err` → 6, all from earlier nights. In the tail, the 09-25 21:39:59 lines (`step line FAILED — DeadlineExceeded: line: past the deadline 21:35:00 ET`, and the F17 FAILED line). None is dated 2026-09-28.

## THE MISS LINE (step 4)
- `ls -la`: `-rw------- 1 cobalt staff 26896 Sep 28 21:24 …/DRC-2026-09-28.md`
- Marker lines: 676 `<!-- cobalt:section drc-misses -->`, 680 `<!-- /cobalt:section drc-misses -->`.
- Unit, whole (read with the Read tool, lines 676–680; the log's MISS lines are not quoted here because they carry tickers):
```
<!-- cobalt:section drc-misses -->
<!-- cobalt:unit miss_line -->
Misses 2026-09-28: cards 27 (unarmed 1 · passed 0 · not_filled 0 · window 0 · rule_10 26) · input_stale 1 · cf-R Σ +7.2R, n=27 · avg: insufficient data (n<30) · movers ≥ 10%: 30 not in play — <ticker> −83.8% not_in_any_source · <ticker> +77.6% not_in_any_source · <ticker> −61.2% not_in_any_source (+27 more) · formations: 125 not taken (no_card) · cf-R Σ −31.2R, n=125 · suppressed 90 · input_stale 12
<!-- /cobalt:unit miss_line -->
<!-- /cobalt:section drc-misses -->
```
- No `PARTIAL: cut before` clause.

## REPLAY VERDICT (step 5)
**REPLAY FIX PROVEN**
- Fix on production's tree: yes (`prepare_member` count 1, tag `deploy-2026-09-27` = `3349466f`).
- The 09-28 run ended `DONE` at 21:24:56 ET, before 21:35:00 (`F17: com.cobalt.replay DONE`). It ran about 14m56s from 21:10:00.
- Step 4 quotes a `drc-misses` unit with no `PARTIAL` clause.
- Not CUT: no `CUT before` suffix, no "formations cut at the deadline" line.

## THE SMOKE (step 6)
- Cutoff: `git -C … log -1 --format=%cI deploy-2026-09-19b` → `2026-09-19T15:11:42-04:00`, the same as the INDEX CARD value.
- Command: `COBALT_ENV=production uv run cobalt smoke s2 --prod --cutoff 2026-09-19T15:11:42-04:00`. Exit 1; it wrote `reports/s2-smoke-2026-09-28.md`.
- Output verbatim (no tickers in it):

```
wrote /Users/cobalt/cobalt/docs/40 - DevDocs/reports/s2-smoke-2026-09-28.md

| # | check | verdict | evidence |
|---|---|---|---|
| K1 | com.cobalt.radar launchctl | PASS | state=running, pid=11993, last exit code=(never exited) |
| K2 | radar_pool primary | PASS | state_valid ok; within_cap ok; failed_stage ok |
| K3 | membership value column (post-deploy admissions and re-scans) | PASS | metric_missing ok; rescanned_metric_missing ok |
| K4.1 | sheet /api/health | PASS | HTTP 200 |
| K4.2 | sheet GET / | PASS | HTTP 200 |
| K4.3 | sheet GET /radar with value column | PASS | HTTP 200 |
| K4.4 | sheet /api/radar/pool | PASS | HTTP 200 |
| K5.1 | P2 seam — latest radar_score_run | PASS | latest_status ok; failed_stage ok |
| K5.2 | P2 seam — radar.cards_enabled reported | PASS | cards_enabled ok |
| K6 | picks — one row per post-deploy FILLED transition | PASS | missing ok |
| K7 | replay job — last run | PASS | com.cobalt.replay: state=done, exit=0, finished_at=2026-09-29 01:24:56.614448+00:00 |
| K8.1 | missed — the replay job's own counters (system side) | FAIL | last_result.input_stale = 1 (expected '0') |
| K8.2 | missed — card rows complete (user side) | PASS | incomplete ok |
| K8.3 | missed — the corpus and the job agree on the card count | PASS | K8.1 = 27, K8.2 = 27 (op eq) |
| K9.1 | movers_daily — gainers stored (user side) | PASS | top_n ok |
| K9.2 | movers — what the gainers export allowed (system side) | PASS | com.cobalt.replay: state=done, exit=0, finished_at=2026-09-29 01:24:56.614448+00:00 |
| K9.3 | movers — gainers stored = what the export allowed | PASS | K9.1 = 20, K9.2 = 20 (op eq) |
| K9.4 | movers_daily — losers stored (user side) | PASS | top_n ok |
| K9.5 | movers — what the losers export allowed (system side) | PASS | com.cobalt.replay: state=done, exit=0, finished_at=2026-09-29 01:24:56.614448+00:00 |
| K9.6 | movers — losers stored = what the export allowed | PASS | K9.4 = 20, K9.5 = 20 (op eq) |
| K9.7 | movers_daily — gainers not archived (user side) | PASS | not_archived ok |
| K9.8 | movers — gainers the replay named partial (system side) | PASS | com.cobalt.replay: state=done, exit=0, finished_at=2026-09-29 01:24:56.614448+00:00 |
| K9.9 | movers — every gainers row not archived is named partial | PASS | K9.7 = 0, K9.8 = 0 (op eq) |
| K9.10 | movers_daily — losers not archived (user side) | PASS | not_archived ok |
| K9.11 | movers — losers the replay named partial (system side) | PASS | com.cobalt.replay: state=done, exit=0, finished_at=2026-09-29 01:24:56.614448+00:00 |
| K9.12 | movers — every losers row not archived is named partial | PASS | K9.10 = 1, K9.11 = 1 (op eq) |
| K10.1 | miss line unit in the DRC note | PASS | unit drc-misses/miss_line present in /Users/cobalt/Vault/Think/1 - Trading/5 - Review/DRC-2026-09-28.md |
| K10.2 | miss line vault_writes row | PASS | writes ok |
| K11.1 | heartbeat — last beat age | PASS | com.cobalt.heartbeat: state=done, exit=0, finished_at=2026-09-29 01:39:31.675650+00:00 |
| K11.2 | heartbeat — database probe OK | PASS | 1 line(s) match '^OK +database ' |
| K11.3 | heartbeat — sheet HTTP probe OK | PASS | 1 line(s) match '^OK +sheet HTTP ' |
| K12.1 | prefill-daily last run | PASS | com.cobalt.prefill-daily: state=done, exit=0, finished_at=2026-09-28 09:15:01.247485+00:00 |
| K12.2 | prefill-drc last run | PASS | com.cobalt.prefill-drc: state=done, exit=0, finished_at=2026-09-28 19:40:00.755527+00:00 |
| K13 | archiver freshness (cadence-aware) | PASS | com.cobalt.archiver: state=done, exit=0, finished_at=2026-09-29 00:55:05.660402+00:00 |
| K14 | backup last run | PASS | com.cobalt.backup: state=done, exit=0, finished_at=2026-09-29 01:40:22.565045+00:00 |
| K15 | heartbeat summary sent at the last slot | PASS | com.cobalt.heartbeat: state=done, exit=0, finished_at=2026-09-29 01:39:31.675650+00:00 |
| K16.1 | cards-expire last run | PASS | com.cobalt.cards-expire: state=done, exit=0, finished_at=2026-09-28 20:05:00.838623+00:00 |
| K16.2 | daymode-propose last run | PASS | com.cobalt.daymode-propose: state=done, exit=0, finished_at=2026-09-28 13:00:00.954560+00:00 |
| K18 | jobs registry vs launchd | PASS | 16 registry label(s) match launchd |

OVERALL: AMBER
```

## THE TABLE (step 7)
Only the red and the replay-fix rows are tabled; every other row is PASS.

| K | result | expected tonight? | last look (09-24) | evidence |
|---|---|---|---|---|
| K3 | PASS | n/a, not red. R32's HOLD reading not needed. | (not among the 09-24 reds) | `metric_missing ok; rescanned_metric_missing ok` |
| K7 | PASS | yes, green on REPLAY FIX PROVEN | RED | `state=done, exit=0, finished_at=2026-09-29 01:24:56.614448+00:00` (= 21:24:56 ET) |
| K8.1 | **FAIL** | **NO — a real red. UNPLACED.** No named ruling covers it, and it is not `fix not live` or CUT. | not among the 09-24 reds | `last_result.input_stale = 1 (expected '0')`. The same count is in the replay's own lines: the card 433 ERROR (`input_stale: bars end 2026-09-28T15:03:00+00:00, before 2026-09-28T16:00:00-04:00`) and the miss line's `input_stale 1`. It is the card step's input, not a deadline. |
| K10.1 | PASS | yes, green on REPLAY FIX PROVEN | RED | unit `drc-misses/miss_line` present |
| K10.2 | PASS | yes, green on REPLAY FIX PROVEN | RED | `writes ok` |

I place nothing on K8.1 beyond the evidence above: no ruling is named for it, so it stays UNPLACED.

## INFORMATION (step 8)
All three items: information — the first RTH data lands tomorrow; the desk reads it (X24-style: his, not a verdict).
- (a) H1 production dry-run: `grep "stored membership"` printed nothing. `deploy-2026-09-27.md:304`: `H1 dry-run UNPROVEN (no 2026-09-27 cache, Sunday); replay-fix live proof owed at 21:10 (`34`). Rollback: not used.`
- (b) Stale-score census (`deploy-2026-09-27.md` lines 276 / 380 / 486): `<np0>` = `190` before. Line 486: `(h) census <np1> | 20:10:00 | … aset_sizings WHERE proximity IS NULL | 190 (<np0> 190) | recorded`. `<s3_1>` (`s2p2.3` score runs) was not in my grep (`proximity IS NULL` only) and is NOT RECORDED in what I read.
- (c) Voice: line 473 `(j) voice | 18:47:15 | curl … http://127.0.0.1:5010/voice/status | 200 | GREEN`; line 500 `V1 STT: model not fetched (V4 step) — text-only until then (ls /Users/cobalt/.cobalt/voice-models → No such file). /voice/* loopback-only (his "B", 09-25 R86); the device session is a later sitting.`

## SMOKE GREEN (step 9)
**smoke green: no.** The first failing clause is (c): real reds = 1 (K8.1, UNPLACED). Clauses (a) (REPLAY FIX PROVEN) and (b) (step 6 ran) hold.

## ESCALATE
1. **K8.1 real red, UNPLACED.** `last_result.input_stale = 1 (expected '0')`.
   - One card (id 433) failed on `input_stale`: its bars end at 15:03 UTC (11:03 ET) against a 16:00 ET requirement. The same line's card misses (27) are otherwise consistent (K8.3 27 = 27).
   - The formations side also shows `input_stale 12`, not smoke-graded.
   - I ruled nothing and did not rerun anything.
2. **Wording note for the desk.** The `replay.log` summary line has a different shape from the one step 3 expected (`movers … · formations s2p2.3 (125 misses, 90 suppressed) · line updated`, not `scans=… formations=…`). The verdict rests on the DONE time and the `drc-misses` unit, not on that line's shape.

No `CUT` or `NOT PROVEN` verdict, so there is no DESK ITEM for the replay.

## DIGEST FOR THE DESK
- Deploy `3349466f` is live: `prepare_member` 1, `s2p2.3` 1.
- 09-28 21:10 replay: RUNNING 21:10:00.693, `F17 DONE` at 21:24:56 ET, about 10 minutes before the 21:35 deadline. No `DeadlineExceeded` on 09-28 (the count of 6 is earlier nights).
- The `drc-misses` unit is in `DRC-2026-09-28.md` (lines 676–680), with no `PARTIAL` clause.
- Replay verdict: **REPLAY FIX PROVEN** (R47's rule applied, not judged).
- Smoke: 40 checks, 39 PASS, 1 FAIL (K8.1), OVERALL AMBER. K7, K10.1 and K10.2, red on 09-24, are green tonight. K3 is PASS.
- K8.1 (`input_stale = 1`) is UNPLACED, so smoke green: no (clause c).
- H1 dry-run UNPROVEN (Sunday, no cache). `<np0>` 190 → `<np1>` 190.
- Voice `/voice/status` 200; STT model not fetched.
- I wrote only this report. I committed nothing and launched nothing.

S2 SMOKE LOOK DONE · replay: PROVEN · smoke: RED · ESCALATE: 1
