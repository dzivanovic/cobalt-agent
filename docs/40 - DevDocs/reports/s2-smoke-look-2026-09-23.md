# S2 SMOKE LOOK 2026-09-23

Seat `s2-smoke-look-0923` (Sonnet 5), read-only, launched by the CTO desk (row R111, `cto-2026-09-23.md`) after tonight's 21:10 ET replay. Prompt: `docs/40 - DevDocs/prompts/2026-09-23/09-s2-smoke-look.md`. Run at 21:40–21:42 ET (`date`: `Wed Sep 23 21:40:46 EDT 2026` at start, `Wed Sep 23 21:41:53 EDT 2026` at write).

Authorization verified: `grep -c -F` of the R43 string in `cto-2026-09-21.md` = 1 (on the `| R43` row that quotes his words); `git log -1 --format=%H -S"cobalt smoke s2 --prod"` = `f5c5bf0f35ff2786b8fea70983bd250b35bf0918`; R111 row of `cto-2026-09-23.md` names `09-s2-smoke-look.md`.

## §0 Headline

- **Replay ran and DONE tonight** — 21:10:00 → 21:12:19 ET, exit 0, first success since the fix; the blank-`Change` rows are now counted (28 unranked per side), not fatal.
- **Smoke OVERALL: AMBER** — 32 green / 2 red (both FAIL, no ERROR): **K9.4** (one stored loser has no bars) and **K17** (5 stray files in `docs/_inflight/`). Neither is placed by a named ruling → 2 real reds.
- K3, K4.4, K7, K8.1, K9.2/.3/.5/.6, K10.1/.2 — last night's reds — are all PASS tonight.
- **Deploy record conflict:** `deploy-2026-09-23.md` ends `FAILED: 2.2` (no tag, "Production UNTOUCHED"), yet the tag `deploy-2026-09-23` exists and the fix is on the tree and in tonight's replay behavior. Recorded as `none (FAILED: 2.2)` by the rule; flagged in ESCALATE.
- **S2 DOES NOT CLOSE** (clause c: 2 real reds). ESCALATE: 3.

## Deploy row (step 2)

- Last non-blank line of `reports/deploy-2026-09-23.md` (verbatim): `FAILED: 2.2 — offline suite red on the stack — tests/cobalt/test_radar_panel_cards.py::test_bars_stale_badge_absent_and_output_unchanged_when_healthy[False], [True] (ladder SHA pin 0ac9b5d0… ≠ e617c53c…) · rollback: not used`
- The report's own state block (`deploy-2026-09-23.md:7`, `:156`): "Production UNTOUCHED: nothing down, nothing merged, no migration, no tag, no vault write." · "No `pre-stacked-0923` tag, no `deploy-2026-09-23` tag."
- `git log --oneline -1 deploy-2026-09-23` → `4e4577c3 fix(s2-smoke): report` (the ref exists). `git show --no-patch --format="%H %D" deploy-2026-09-23` → `4e4577c39d55e4591ebe0192a66a51b1badff8cf tag: deploy-2026-09-23, s2/smoke-fix-0922, deploy/stacked-0923`; commit time `2026-09-23T16:56:18-04:00`. `HEAD` = `e10f95f6` on `main`.
- `grep -c -F "unranked_rows" src/cobalt/replay/models.py` → `5` (≥1: the smoke fix is on this tree).
- Tonight's `replay.err` shows the fix's behavior: `movers-gainers: 28 of 11666 rows have a blank Change — unranked, not stored, not benchmarked` (and the same for losers) — the exact input that failed 09-22.
- **Record: `deploy: none (FAILED: 2.2)`** (the stop line of the report is FAILED). The tag/tree/behavior above contradict "nothing tagged" — not explained here; see ESCALATE 3.

## Replay row (step 3)

- Start (`replay.err`): `2026-09-23 21:10:00.563 | INFO | cobalt.jobs.wrapper:job_run:173 - F17: com.cobalt.replay RUNNING (timeout 1800s, heartbeat every 600s)`
- DONE (`replay.err`): `2026-09-23 21:12:19.759 | INFO | cobalt.jobs.wrapper:job_run:199 - F17: com.cobalt.replay DONE`
- `replay.log` tail: `replay 2026-09-23: scans=235 formations=0 path_b_only=48 counts={'avoided': 294, 'input_stale': 291, 'not_evaluable': 7182, 'not_formed': 3983} writes: none` and `replay 2026-09-23: movers 40 · archived 39 · card misses 7 · mover misses 24 · input_stale 0 · formations s2p2.1 (0 misses, 0 suppressed) · line updated` (log line 108). `archive_incomplete: 1` in the job row (see K9.4).
- Earlier nights in the same file (text, not tonight): 09-21 FAILED (`no 'radar.benchmark' row`), 09-22 FAILED (`Change '' is not a percentage`).

## Smoke output (step 4, verbatim)

Cutoff: `git -C /Users/cobalt/cobalt log -1 --format=%cI deploy-2026-09-19b` → `2026-09-19T15:11:42-04:00` (same as 09-22's look).
Command: `COBALT_ENV=production uv run cobalt smoke s2 --prod --cutoff 2026-09-19T15:11:42-04:00` (from `/Users/cobalt/cobalt`; exit code 1, i.e. not GREEN).

```
wrote /Users/cobalt/cobalt/docs/40 - DevDocs/reports/s2-smoke-2026-09-23.md

| # | check | verdict | evidence |
|---|---|---|---|
| K1 | com.cobalt.radar launchctl | PASS | state=running, pid=79755, last exit code=(never exited) |
| K2 | radar_pool primary | PASS | state_valid ok; within_cap ok; failed_stage ok |
| K3 | membership value column (post-deploy admissions and re-scans) | PASS | metric_missing ok; rescanned_metric_missing ok |
| K4.1 | sheet /api/health | PASS | HTTP 200 |
| K4.2 | sheet GET / | PASS | HTTP 200 |
| K4.3 | sheet GET /radar with value column | PASS | HTTP 200 |
| K4.4 | sheet /api/radar/pool | PASS | HTTP 200 |
| K5.1 | P2 seam — latest radar_score_run | PASS | latest_status ok; failed_stage ok |
| K5.2 | P2 seam — radar.cards_enabled reported | PASS | cards_enabled ok |
| K6 | picks — one row per post-deploy FILLED transition | PASS | missing ok |
| K7 | replay job — last run | PASS | com.cobalt.replay: state=done, exit=0, finished_at=2026-09-24 01:12:19.745012+00:00 |
| K8.1 | missed — the replay job's own counters (system side) | PASS | com.cobalt.replay: state=done, exit=0, finished_at=2026-09-24 01:12:19.745012+00:00 |
| K8.2 | missed — card rows complete (user side) | PASS | incomplete ok |
| K8.3 | missed — the corpus and the job agree on the card count | PASS | K8.1 = 7, K8.2 = 7 (op eq) |
| K9.1 | movers_daily — gainers stored (user side) | PASS | top_n ok; not_archived ok |
| K9.2 | movers — what the gainers export allowed (system side) | PASS | com.cobalt.replay: state=done, exit=0, finished_at=2026-09-24 01:12:19.745012+00:00 |
| K9.3 | movers — gainers stored = what the export allowed | PASS | K9.1 = 20, K9.2 = 20 (op eq) |
| K9.4 | movers_daily — losers stored (user side) | FAIL | not_archived eq 0 (actual 1) |
| K9.5 | movers — what the losers export allowed (system side) | PASS | com.cobalt.replay: state=done, exit=0, finished_at=2026-09-24 01:12:19.745012+00:00 |
| K9.6 | movers — losers stored = what the export allowed | PASS | K9.4 = 20, K9.5 = 20 (op eq) |
| K10.1 | miss line unit in the DRC note | PASS | unit drc-misses/miss_line present in /Users/cobalt/Vault/Think/1 - Trading/5 - Review/DRC-2026-09-23.md |
| K10.2 | miss line vault_writes row | PASS | writes ok |
| K11.1 | heartbeat — last beat age | PASS | com.cobalt.heartbeat: state=done, exit=0, finished_at=2026-09-24 01:35:41.626826+00:00 |
| K11.2 | heartbeat — database probe OK | PASS | 1 line(s) match '^OK +database ' |
| K11.3 | heartbeat — sheet HTTP probe OK | PASS | 1 line(s) match '^OK +sheet HTTP ' |
| K12.1 | prefill-daily last run | PASS | com.cobalt.prefill-daily: state=done, exit=0, finished_at=2026-09-23 09:15:05.591317+00:00 |
| K12.2 | prefill-drc last run | PASS | com.cobalt.prefill-drc: state=done, exit=0, finished_at=2026-09-23 19:40:04.349782+00:00 |
| K13 | archiver freshness (cadence-aware) | PASS | com.cobalt.archiver: state=done, exit=0, finished_at=2026-09-24 00:54:54.762090+00:00 |
| K14 | backup last run | PASS | com.cobalt.backup: state=done, exit=0, finished_at=2026-09-24 01:40:15.097503+00:00 |
| K15 | heartbeat summary sent at the last slot | PASS | com.cobalt.heartbeat: state=done, exit=0, finished_at=2026-09-24 01:35:41.626826+00:00 |
| K16.1 | cards-expire last run | PASS | com.cobalt.cards-expire: state=done, exit=0, finished_at=2026-09-23 20:05:05.449676+00:00 |
| K16.2 | daymode-propose last run | PASS | com.cobalt.daymode-propose: state=done, exit=0, finished_at=2026-09-23 13:00:04.392532+00:00 |
| K17 | cobalt validate | FAIL | exit 1 (expected 0) |
| K18 | jobs registry vs launchd | PASS | 16 registry label(s) match launchd |

OVERALL: AMBER
```

The command's own full per-check artifact: `docs/40 - DevDocs/reports/s2-smoke-2026-09-23.md` (written by the command, not by this seat).

## Table (step 5)

Last-night column = `s2-smoke-look-2026-09-22.md` Table 2. "Formed card?" = does the check structurally need a formed card (from the 09-22 look's Table 1; only K6 does, guarded by `known_if` fills=0).

| K | result | expected tonight? | last night (09-22) | formed card? | evidence |
|---|---|---|---|---|---|
| K1 | PASS | — | PASS | no | state=running, pid=79755 |
| K2 | PASS | — | PASS | no | pool `primary` scanning→aftermarket, cap 50, members 50, failed_stage empty |
| K3 | PASS | — (no R32 reading needed: not red) | FAIL (metric_missing 66) | no | `post_deploy_admitted=451, metric_missing=0, value_null=102, unranked_retained=102, rescanned_admitted=50, rescanned_metric_missing=0`. The 102 NULL values = the 102 unranked_retained (designed NULL). Neither HOLD nor RETAIN defect: both counters 0 |
| K4.1–K4.3 | PASS | — | PASS | no | HTTP 200 each |
| K4.4 | PASS | — | FAIL (422) | no | HTTP 200 with `?since=2026-09-19T15%3A11%3A42-04%3A00` |
| K5.1–K5.2 | PASS | — | PASS | no | latest_status=complete; cards_enabled=True |
| K6 | PASS | — | PASS (fills 9) | **yes** (`known_if` fills=0 → KNOWN; not needed tonight) | fills=13, missing=0 |
| K7 | PASS | — | FAIL | no | state=done, exit=0, finished 2026-09-24 01:12:19 UTC |
| K8.1–K8.3 | PASS | — | FAIL/PASS/PASS | no | K8.1 = 7 = K8.2 (card_misses=7, incomplete=0) |
| K9.1 | PASS | — | PASS | no | top_n=20, stored=20, not_archived=0 |
| K9.2–K9.3 | PASS | — | FAIL / ERROR | no | gainers exported 11666, unranked 28, expected 20 = stored 20 |
| **K9.4** | **FAIL** | **NO — real red, UNPLACED** | PASS (stored 0) | no | `top_n=20, stored=20, not_archived=1`. Job row: `archived: 39` of `movers: 40`, `archive_incomplete: 1`, `archive_failures: 0`. Which loser is unarchived: not readable with this seat's commands (no DB query) |
| K9.5–K9.6 | PASS | — | FAIL / ERROR | no | losers exported 11666, unranked 28, expected 20; K9.4 stored = 20 = K9.5 expected (K9.6's own FAIL line in the artifact only carries K9.4's verdict) |
| K10.1–K10.2 | PASS | — | FAIL | no | `drc-misses/miss_line` unit present in `DRC-2026-09-23.md`; vault_writes writes=1 |
| K11.1–K11.3 | PASS | — | PASS | no | heartbeat GREEN 21:35:38 EDT, database and sheet probes OK |
| K12.1–K12.2 | PASS | — | PASS | no | exit 0 |
| K13 | PASS | — | PASS | no | archiver finished 2026-09-24 00:54:54 UTC |
| K14 | PASS | — | PASS | no | backup finished 2026-09-24 01:40:15 UTC |
| K15 | PASS | — | PASS | no | `summary_sent` `{'07:00': '2026-09-23', '16:30': '2026-09-23'}` |
| K16.1–K16.2 | PASS | — | PASS | no | exit 0 |
| **K17** | **FAIL** | **NO — real red, UNPLACED** (no ruling names it) | FAIL (same 5 files) | no | `FAILED: docs/PLACEMENT.md violations:` — `docs/_inflight/DRC-automation-spec-2026-09-22.md` · `docs/_inflight/defs-gap-table-2026-09-21.md` · `docs/_inflight/drc-automation-values-2026-09-22.md` · `docs/_inflight/setups-assumed-values-2026-09-21.md` · `docs/_inflight/trading-stats-2026-09-21.md`, each "docs/_inflight/ may hold only README.md (set COBALT_INFLIGHT_OK=1 for a deliberate in-flight window)". `ls docs/_inflight/` tonight: those five + `README.md`. All other `cobalt validate` lines OK |
| K18 | PASS | — | PASS | no | 16 registry labels match launchd |

Tonight's checks needing a formed card: K6 only. The seven setups are live only if the deploy landed (step 2 record: none (FAILED: 2.2), conflicting evidence) — UNPROVEN either way; no check tonight depends on it.

## S2 CLOSE VERDICT

Rule: `S2 CLOSES` only if (a), (b) and (c) all hold.

- (a) A 2026-09-23 replay run ended DONE — **HOLDS.** `2026-09-23 21:12:19.759 … com.cobalt.replay DONE` (`logs/replay.err`); job row `state=done, exit=0`.
- (b) Step 4 ran — **HOLDS.** Output quoted above.
- (c) `real or UNPLACED reds` = 0 — **FAILS.** 2: K9.4 and K17. Neither is placed `expected` by a named ruling (09-20 R32 covers K3's frozen HOLD only, and K3 is PASS).

**S2 DOES NOT CLOSE** — first failing clause: (c). The live day is banked (R46); this rule reads the green night only. The desk and he decide what follows (L37).

## ESCALATE

1. **K9.4 — real red, UNPLACED, new tonight.** One of the 20 stored `losers` rows for 2026-09-23 has `bars_archived = false` (`not_archived eq 0 (actual 1)`). Same night's job row: `movers: 40, archived: 39, archive_incomplete: 1, archive_failures: 0`. Gainers side is clean. Which ticker and why is not knowable from this seat's read-only commands; needs a DB read (`system.movers_daily`, side `losers`, `NOT bars_archived`) by whoever holds that path.
2. **K17 — real red, UNPLACED, unchanged since 09-22.** Five non-README files in `docs/_inflight/` (named above) fail `cobalt validate` / `docs/PLACEMENT.md`. Needs the desk's call: move/delete them, or a deliberate `COBALT_INFLIGHT_OK=1` window (a setting this seat does not touch).
3. **Deploy record conflict (not a smoke red; an unresolved fact).** `reports/deploy-2026-09-23.md` says the deploy FAILED at 2.2 with "no `deploy-2026-09-23` tag" and production untouched. Tonight: the tag `deploy-2026-09-23` exists on `4e4577c3` (commit time 16:56:18 EDT, also carrying `s2/smoke-fix-0922` and `deploy/stacked-0923`), `unranked_rows` is in `src/cobalt/replay/models.py` on this tree, and the replay ran with the fix's behavior. What landed, when, and by whom is not established by this seat. The smoke's K3/K4.4/K7/K8/K9.x greens are consistent with the smoke fix being live.

## DIGEST FOR THE DESK

- Replay ran and succeeded tonight (21:10:00 → 21:12:19 ET, exit 0): the blank-`Change` fix is live in behavior (28 unranked rows/side, counted not fatal).
- Smoke AMBER, 32/34 green. Last night's reds (K3, K4.4, K7, K8.1, K9.2/.3/.5/.6, K10.1/.2) all cleared.
- Two reds remain, neither placed by a named ruling: **K9.4** (1 of 20 stored losers has no bars; job row `archive_incomplete: 1`, `archived 39/40`; ticker not readable here) and **K17** (same 5 stray `docs/_inflight/` files as 09-22).
- Deploy record conflict: `deploy-2026-09-23.md` = FAILED 2.2, no tag; the tag exists (4e4577c3, 16:56 EDT) and the fix is live. Recorded as `none (FAILED: 2.2)`; the desk should reconcile.
- S2 close verdict by the one rule: (a) yes, (b) yes, (c) no (2 real reds) → **S2 DOES NOT CLOSE**.
- Both reds are small and specific: K17 is a housekeeping move; K9.4 needs one DB read to name the ticker.
- The command's own artifact is `reports/s2-smoke-2026-09-23.md`; this report is `reports/s2-smoke-look-2026-09-23.md`; the desk commits both.

S2 SMOKE LOOK DONE · deploy: none · replay ran: yes 21:10 DONE · checks: 32 green / 2 red · reds expected tonight: 0 · real or UNPLACED reds: 2 · smoke green for S2: no · S2: DOES NOT CLOSE · ESCALATE: 3
