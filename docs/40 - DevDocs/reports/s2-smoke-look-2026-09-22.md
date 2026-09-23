# S2 SMOKE LOOK 2026-09-22

Seat `s2-smoke-look-0922` (Sonnet 5), read-only, launched by the CTO desk on a timer after tonight's 21:10 ET replay. Prompt: `docs/40 - DevDocs/prompts/2026-09-22/03-s2-smoke-look.md`.

## §0 Headline

- **Replay ran and FAILED again tonight** — a SECOND, DIFFERENT bug from last night's: `SourceFailure: movers: Change '' is not a percentage`, 21:10:03.991 → 21:10:05.865 ET.
- **Smoke OVERALL: RED** — 23 green / 11 red (9 FAIL, 2 ERROR). Of the 11, **4 are the already-known "no successful replay row yet" gap** (K9.2/.3/.5/.6); **7 are real reds** needing attention (K3, K4.4, K7, K8.1, K10.1, K10.2, K17).
- **Only K6 structurally needs a formed card**, and it's `known_if`-guarded (would read KNOWN, not FAIL, at zero) — tonight it's not even an issue: 9 real fills, 0 missing. The "no card can form" premise did not drive tonight's reds; the replay's own repeated failure did.
- **Smoke green for S2: NO.** ESCALATE: 5.

## Table 1 — which checks need a formed card (`configs/cobalt/smoke/s2.yaml`)

No `--prod`-run card has formed since the 2026-09-19 deploy per the desk's own record (`cto-2026-09-21.md:287`, "no card can form before chunk C1 lands"); K6's own real data below shows fills already exist, so that premise did not block anything tonight — noted, not silently accepted.

| K | what it asserts | needs ≥1 formed card today? |
|---|---|---|
| K1 | `com.cobalt.radar` launchctl running | no |
| K2 | radar_pool scanning/cap/failed_stage healthy | no |
| K3 | post-deploy `radar_membership` admissions carry rank_metric/value (INSERT + RETAIN paths) | no — pool admission, not a card; `known_if` only guards zero-admission, s2.yaml:99-102 |
| K4.1–K4.3 | sheet health/root/`/radar` page 200 | no |
| K4.4 | `/api/radar/pool` 200 | no |
| K5.1 | P2 `radar_score_run` seam complete | no |
| K5.2 | `radar.cards_enabled` setting reported (existence of the flag, not a card) | no |
| K6 | ≥1 FILLED `card_transitions` row has a matching `picks` row | **yes** — `known_if` fills=0 → KNOWN, s2.yaml:184-186 |
| K7 | replay job's own last-run state/exit/result shape | no — job execution, not card-gated |
| K8.1 | replay job's own `card_misses` counter + `trade_date` | no — count can legitimately be 0 |
| K8.2 | `"user".missed` kind='card' rows complete | no — 0 rows passes vacuously, no `known_if` needed, s2.yaml:241-256 |
| K8.3 | K8.1 = K8.2 | no — compares two possibly-vacuous zeros |
| K9.1–K9.6 | `movers_daily` gainers/losers stored = what the export allowed | no — movers ranking, not cards |
| K10.1 | DRC note carries `drc-misses`/`miss_line` markers | no — needs a logged MISS, not a formed card |
| K10.2 | ≥1 `vault_writes` row for `drc-misses`/`miss_line` | no — same, needs a miss record not a formed card, s2.yaml:389-399, no `known_if` |
| K11–K18 | job rows / registry / launchctl / `cobalt validate` | no — infra checks, unrelated to cards |

## Table 2 — the smoke command, verbatim

Command: `COBALT_ENV=production uv run cobalt smoke s2 --prod --cutoff 2026-09-19T15:11:42-04:00` (cutoff source: `git -C /Users/cobalt/cobalt log -1 --format=%cI deploy-2026-09-19b` — `deploy-p4-2026-09-19.md`'s own merge line, 4.3, carries no clock instant of its own; the nearest report timestamp, the 4.2 baseline re-check "`Sat Sep 19 15:11:51 EDT 2026`," is 9s later than the tag's commit time, so the tag commit was used as the precise instant).

```
| # | check | verdict | evidence |
|---|---|---|---|
| K1 | com.cobalt.radar launchctl | PASS | state=running, pid=23081, last exit code=(never exited) |
| K2 | radar_pool primary | PASS | state_valid ok; within_cap ok; failed_stage ok |
| K3 | membership value column (post-deploy admissions and re-scans) | FAIL | metric_missing eq 0 (actual 66) |
| K4.1 | sheet /api/health | PASS | HTTP 200 |
| K4.2 | sheet GET / | PASS | HTTP 200 |
| K4.3 | sheet GET /radar with value column | PASS | HTTP 200 |
| K4.4 | sheet /api/radar/pool | FAIL | HTTP 422 (expected 200) |
| K5.1 | P2 seam — latest radar_score_run | PASS | latest_status ok; failed_stage ok |
| K5.2 | P2 seam — radar.cards_enabled reported | PASS | cards_enabled ok |
| K6 | picks — one row per post-deploy FILLED transition | PASS | missing ok |
| K7 | replay job — last run | FAIL | state 'failed' (expected 'done'); exit_code 1 (expected 0); last_result.trade_date = '2026-09-22' (expected '2026-09-21') |
| K8.1 | missed — the replay job's own counters (system side) | FAIL | last_result.trade_date = '2026-09-22' (expected '2026-09-21') |
| K8.2 | missed — card rows complete (user side) | PASS | incomplete ok |
| K8.3 | missed — the corpus and the job agree on the card count | PASS | K8.1 = 0, K8.2 = 0 (op eq) |
| K9.1 | movers_daily — gainers stored (user side) | PASS | top_n ok; not_archived ok |
| K9.2 | movers — what the gainers export allowed (system side) | FAIL | last_result.trade_date = '2026-09-22' (expected '2026-09-21') |
| K9.3 | movers — gainers stored = what the export allowed | ERROR | ERROR(non-numeric result) — K9.2 (job_row) produced no number to compare |
| K9.4 | movers_daily — losers stored (user side) | PASS | top_n ok; not_archived ok |
| K9.5 | movers — what the losers export allowed (system side) | FAIL | last_result.trade_date = '2026-09-22' (expected '2026-09-21') |
| K9.6 | movers — losers stored = what the export allowed | ERROR | ERROR(non-numeric result) — K9.5 (job_row) produced no number to compare |
| K10.1 | miss line unit in the DRC note | FAIL | section 'drc-misses' absent in /Users/cobalt/Vault/Think/1 - Trading/5 - Review/DRC-2026-09-21.md |
| K10.2 | miss line vault_writes row | FAIL | writes ge 1 (actual 0) |
| K11.1 | heartbeat — last beat age | PASS | com.cobalt.heartbeat: state=done, exit=0, finished_at=2026-09-23 01:14:18.550423+00:00 |
| K11.2 | heartbeat — database probe OK | PASS | 1 line(s) match '^OK +database ' |
| K11.3 | heartbeat — sheet HTTP probe OK | PASS | 1 line(s) match '^OK +sheet HTTP ' |
| K12.1 | prefill-daily last run | PASS | com.cobalt.prefill-daily: state=done, exit=0, finished_at=2026-09-22 09:15:00.982282+00:00 |
| K12.2 | prefill-drc last run | PASS | com.cobalt.prefill-drc: state=done, exit=0, finished_at=2026-09-22 19:40:00.712952+00:00 |
| K13 | archiver freshness (cadence-aware) | PASS | com.cobalt.archiver: state=done, exit=0, finished_at=2026-09-23 00:55:04.219531+00:00 |
| K14 | backup last run | PASS | com.cobalt.backup: state=done, exit=0, finished_at=2026-09-22 01:40:11.048289+00:00 |
| K15 | heartbeat summary sent at the last slot | PASS | com.cobalt.heartbeat: state=done, exit=0, finished_at=2026-09-23 01:14:18.550423+00:00 |
| K16.1 | cards-expire last run | PASS | com.cobalt.cards-expire: state=done, exit=0, finished_at=2026-09-22 20:05:00.667253+00:00 |
| K16.2 | daymode-propose last run | PASS | com.cobalt.daymode-propose: state=done, exit=0, finished_at=2026-09-22 13:00:00.788639+00:00 |
| K17 | cobalt validate | FAIL | exit 1 (expected 0) |
| K18 | jobs registry vs launchd | PASS | 16 registry label(s) match launchd |

OVERALL: RED
```

Full per-check detail written by the command to `docs/40 - DevDocs/reports/s2-smoke-2026-09-22.md`.

## Table 3 — reading it (K3 per `cto-2026-09-20.md` R32)

| K | result | expected tonight? | evidence |
|---|---|---|---|
| K1–K2 | PASS | — | pid 23081 never exited; state_valid/within_cap/failed_stage all ok |
| K3 | FAIL | **no — real red.** R32's HOLD/`degraded_sources` reading applies only to the RETAIN-path predicate (`rescanned_metric_missing`), which is clean (0). The FAIL is on the INSERT-path predicate, and the check's own text states the INSERT path "always writes rank_metric" with no documented exception. | `post_deploy_admitted=301, metric_missing=66, value_null=66, rescanned_admitted=50, rescanned_metric_missing=0` |
| K4.1–K4.3 | PASS | — | HTTP 200 each |
| K4.4 | FAIL | **no — real red.** `/api/radar/pool` now requires a `since` query param (`src/cobalt/aset/radar_panel.py:373`, landed 2026-09-21, after the deploy this smoke's cutoff is pinned to); K4.4's own config calls it bare. | `HTTP 422 {"status":"FAILED","error":"since is required"}` |
| K5.1–K5.2 | PASS | — | latest_status=complete; cards_enabled=True |
| K6 | PASS | — | fills=9, missing=0 |
| K7 | FAIL | **no — real red.** Tonight's 21:10:03.991→21:10:05.865 ET run failed on a NEW bug. | `state=failed, exit_code=1, trade_date='2026-09-22'` |
| K8.1 | FAIL | **no — same root cause as K7** (reads the same failed job row). | `trade_date` mismatch only; `card_misses=0` |
| K8.2–K8.3 | PASS | — | `card_rows=0, incomplete=0` — vacuous: no missed rows logged for 09-21 either |
| K9.1, K9.4 | PASS | — | `top_n=20, stored=0, not_archived=0` |
| K9.2, K9.5 | FAIL | **yes — expected.** `deploy-p4-2026-09-19.md` §6.5 named this red-by-design until "the first `com.cobalt.replay` run writes a job row carrying [`movers_by_side`]" — two nights running, that run still hasn't happened. | `last_result.movers_by_side={}` |
| K9.3, K9.6 | ERROR | **yes — same cause**, no number to compare. | `(no number)` |
| K10.1 | FAIL | **no — real red, but placed.** 09-21's own 21:10 run failed instantly (missing `radar.benchmark` row) before writing anything, so the DRC note never got a `drc-misses` section that night; today's 07:04 ET fix landed after that run had already failed and does not backfill it. | section absent in `DRC-2026-09-21.md` |
| K10.2 | FAIL | **no — same explanation as K10.1.** | `writes=0` |
| K11–K16, K18 | PASS | — | all job rows / registry green |
| K17 | FAIL | **no — real red, unrelated to replay/cards.** `docs/_inflight/` holds 5 non-README files, violating `docs/PLACEMENT.md` (no `COBALT_INFLIGHT_OK` window set). | 5 files named in the FAILED block (`DRC-automation-spec…`, `defs-gap-table…`, `drc-automation-values…`, `setups-assumed-values…`, `trading-stats…`, all 2026-09-21/22) |

## ESCALATE

1. **Replay failed a second night in a row, on a second, different bug.** `movers: Change '' is not a percentage` (`SourceFailure`), 21:10:05 ET. Blocks K7, K8.1, K9.2, K9.3, K9.5, K9.6 and pushes S2's "one green smoke night" out again. Needs a fix in the movers source parser and a rerun before this smoke can go green.
2. **K3 real red** — 66 of 301 post-deploy-admitted `radar_membership` rows are missing `rank_metric` on the INSERT path, which R32's HOLD exception does not cover (that exception is RETAIN-path only, and the RETAIN-path count is clean). Needs a read of `radar/store.py`'s insert path, or a ruling if this is itself a new class to accept.
3. **K4.4 real red** — `/api/radar/pool` started requiring a `since` param on 2026-09-21 (`radar_panel.py:373`); the smoke config (`s2.yaml` K4.4) is stale against that change. Needs either the check updated with a `since` value or a ruling that the endpoint's new requirement is wrong.
4. **K10.1/K10.2** — 2026-09-21's DRC miss-line was never written (that night's replay died before reaching it); no backfill mechanism exists. Desk call: backfill it, or accept the gap for S2's live-day count.
5. **K17** — 5 stray files in `docs/_inflight/` fail `cobalt validate`/PLACEMENT.md. Needs cleanup (move/delete/README-only) or a deliberate `COBALT_INFLIGHT_OK` window.

## DIGEST FOR THE DESK

Replay ran tonight (21:10:03–21:10:05 ET) and FAILED — a NEW bug (`movers: Change '' is not a percentage`), not last night's missing-benchmark-row one. Smoke ran anyway (per the seat's design) and came back RED: 23/34 green, 11 red. Of the 11: 4 are the known "no successful replay row yet" gap (K9.2/.3/.5/.6, expected per the P4 deploy report until a replay run finally succeeds). The other 7 are real and need attention — K3 (a genuine INSERT-path metric gap, not the accepted R32 HOLD case), K4.4 (a stale smoke check against a 09-21 API change requiring `since`), K7/K8.1 (tonight's failed run itself), K10.1/K10.2 (09-21's DRC miss-line was never written, no backfill exists), K17 (5 stray `docs/_inflight/` files). Only K6 structurally needed a formed card and it already has real fills (9), so the "no card can form" premise wasn't the story tonight — the replay's own back-to-back different failures were. Smoke is NOT green; S2 does not close on tonight's run.

S2 SMOKE LOOK DONE · replay ran: yes 21:10 FAILED · checks: 23 green / 11 red · reds expected tonight: 4 · real or UNPLACED reds: 7 · checks that need a formed card: 1 · smoke green for S2: no · ESCALATE: 5
