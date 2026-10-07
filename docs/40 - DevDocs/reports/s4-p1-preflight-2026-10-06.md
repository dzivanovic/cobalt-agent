# S4-P1 card 72 preflight — 2026-10-06 (seat s4-p1-preflight, read-only)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git rev-parse --short=8 HEAD`; `git diff --stat 2812c2ef HEAD -- src configs tests ops` | `192f5abe`; diff empty: every code line the card cites (proven at `2812c2ef`) is unchanged at HEAD | OK |
| 2 | header of `72-s4-p1-card.md` | `BASE: «FILL: main HEAD at launch, 8 hex»` is the only `«FILL` (grep); `TIP:`, `CHECK REPORT:`, `HOUSE B:` empty; no `DB:` key (rows touch `src/`) | OK |
| 3 | `git log ops/s4-p1-1007` → unknown revision; `ls /Users/cobalt/cobalt-wt` → no `s4-p1-1007` | branch and worktree are new | OK |
| 4 | `grep -n "section \|DECISION" desk-launch.sh`; `CARD.md` | build kind needs only `section ROWS` (`:885`, `:906`); `## DECISIONS` is neither required nor refused; `CARD.md` names it only as a report section / RECORDS item. Both accept it | OK |
| 5 | `cto-2026-10-06.md:86` | `R598 … HIS RULING … HIS RULING · APPROVED`; words `## R598` at `cto-2026-10-06-words.md:3`; both files unmodified vs HEAD (committed) | OK |
| 6 | `git log -- card draft`; `git diff HEAD --stat` | both in `192f5abe`, no working-tree change | OK |
| 7 | `models.py:76-85` (Actor), `:92-110` (ALLOWED; ARMED→TRIGGERED `:100`, WATCH→MISSED `:94`, MISSED terminal `:109`), `:136` (MISSED_EDGE); `store.py:248` (`transition`), `:387-400` (MISSED reason), `:1017-1030` (`open_radar_cards`, columns id…entry, no ARMED `at`), `:1101` (`create_radar_card`); `cards/__init__.py:28-31`; `cli.py:518` | each quote matches the card | OK |
| 8 | `archiver/collector.py:78` (`resolve_token`), `:219-238` (`fetch_bars`), `:19-31`; `radar/collector.py:42` (`TokenBucket`); `session/models.py:22-23` | match. `:19-31` is the TIMEZONE docstring (bars tz-aware UTC), it does not say ts = bar start; that is stated at `replay/cards.py:32` | OK |
| 9 | `tunables.yaml:666-710` (`:684-692` poll_interval 100, `:702-709` finviz_max_rpm 50, R17 2026-09-17 in consumers); `radar/config.py:192-199`, `:202-215`; `jobs.yaml:184-195`, `:194` `imports: [cobalt.cli]`, `:69` and `:191` read tunables | match | OK |
| 10 | `trade_def.py:192-196`, `:379-396`, `:632-640`, `:643-654` (`SimpleTrigger.confirmation_policy`), `:657` (`SequenceTrigger`); `taxonomy/store.py:91-101` | match | OK |
| 11 | `replay/cards.py:14-16`, `:99-101`, `:242` (`b.ts >= start_at`) | `:14-16` and `:99-101` cite correctly, but C1 says `intrabar` floors `since` to the minute and is "THE SAME RULE" as the replay trigger. The replay does not floor: a bar starting before `created_at` is excluded (`:15` "at or after `created_at`", `:242`). A card armed 10:00:30 with a 10:00 bar whose high ≥ entry: the detector crosses, the replay does not. C1's AGREEMENT control (since = card start) cannot hold for a non-minute `since`, so X1 fails | FAIL |
| 12 | `radar/poller.py:11`, `:48`, `:98-100`; `radar/runner.py:461-472` (`:465`), `:475-486`; `aset/web.py:1799-1815` (manual TRIGGERED, `actor=YOU`) | match. `BarStore.bars_in_range` exists (`archiver/store.py:283`) for C3 | OK |
| 13 | Charter `:54`, `:102-105`, `:114-126` (`:121-124`, `:125-126`), `:269`, `:273`; ladder `:804-817` (F9 row `:812`); `LIVE-FEED-SPIKE.md:3-16`, `:8-9`, `:22-36`, `:190-192` | match; M1's lag definition equals the spike's (`:33-36`) and the VERDICT rule equals the Charter's (`:121-124`) | OK |
| 14 | `BUILD-HUB.md:12`, `:14` (no `uv run python`, no strike verb); `DEPLOY-HUB.md:92`; `gate-lists.md:5-7`; `placement/check.py:80`; `restarts.py:38`, `:207-210`, `:216-220`, `:225-229`, `:230-234`, `:245-246` | match | OK |
| 15 | `ls src/cobalt/strike` and the five new test files → none exist; `grep strike tunables.yaml` → none | M1/T1/C1-C3 reds (`ModuleNotFoundError`) hold on BASE. C4's red (no strike thread in `run_command`, `:461-472`) holds | OK |
| 16 | each row's NEGATIVE CONTROL | the controls sit in the same new files that import the missing module, so on BASE they ERROR too (not green); they go green with the build. Existing `test_radar_runner.py` tests are green on BASE | NOTE |
| 17 | rows M1, T1, C1-C4, W1, D1 vs ladder `## S4` P1 (`:812`: re-measure, detector, TRIGGERED, MISSED) | M1 = re-measure, C1/C2 = detector + TRIGGERED, C3 = MISSED; T1/C4/W1/D1 are config, the loop, gate lists and docs the three need. Nothing else; the SSE/notification/DM/week report sit in P2 and `## NOT IN THIS JOB` | OK |
| 18 | T1: "so `cobalt validate` fails on a missing or mis-united row" | `radar/config.py:202` `check()` is run by `cobalt radar check` (`radar/cli.py:17`, `config.py:218`), not by `cobalt validate`; validate's tunable checks hang off `cli.py:466`. T1's files are `tunables.yaml`, `strike/config.py`, `test_strike_config.py`: no row wires the strike check into `cobalt validate` or any caller, and no test asserts it. The stated effect has no row | FAIL |
| 19 | arguments against D1 (`--names --cadence --minutes --out`) | M1 adds `--max-gets <n>`, named in no decision (his R411, R412: no argument beyond the draft's decisions) | FAIL |
| 20 | RESTARTS paragraph vs `restarts.py` and `jobs.yaml` | classes and homes match; `com.cobalt.agent` imports `cobalt_agent.main` and nothing under `src/cobalt_agent` imports `cobalt.cards`/`radar`/`cli`, so no agent restart; expected `RESTARTS: com.cobalt.aset com.cobalt.radar`. The build proves it with `jobs restarts` | OK |
| 21 | D2 gate: T1 `strike.finviz_max_rpm` "per DECISION D2", C2 fetches through that bucket | the only Finviz-rate numbers in the rows stay behind D2. M1 names no bucket rpm; its D1 run (5 names × 3 s = 100 GET/min vs R17's 50) is his to approve and the desk's build-after-D2 note covers it | OK |
| 22 | trading platform | no row touches DAS or TradeStation; `## NOT IN THIS JOB` forbids it; M1 contacts none | OK |
| 23 | `grep -c -F "test_strike_detector_db.py" ops/desk/gate-lists.md` on BASE | `0` (card expects `2` after: one `--deselect` in PASS 1, one id in PASS 2); `test_radar_cards_db.py` already sits in PASS 2 | OK |

## ISSUES
- FAIL #11 (X1): C1's `intrabar` floors `since` to the minute; the replay's trigger (`replay/cards.py:15`, `:242`) does not. Drop the floor, or say the detector is intentionally wider and drop "THE SAME RULE" and the AGREEMENT control for non-minute `since`.
- FAIL #18: T1 promises `cobalt validate` fails on a missing or mis-united `strike.*` row, but no row wires `strike/config.py` into `validate` (`cli.py:466` area) or tests it. Add the wiring and its file to T1, or state that the check is `cobalt strike check`-style and named by a decision.
- FAIL #19: `--max-gets` is an argument no decision names. Name it under a decision, or cut it and keep the cadence × minutes cap.
- NOTE #16: controls are red-by-import on BASE, green after the build.
- NOTE W1: the card says the DB test needs "the radar card columns (`0007`)"; `create_radar_card` writes `card_score`/F15 records (migration `0022`), above the gate's `0013` level, so the PASS 1/PASS 2 listing is right but the stated reason is not.
- NOTE: `strike.alert_criterion_s` (T1) has no reader in P1 (the M1 verdict hard-codes the Charter's 5 s via D1); P2 reads it.
- NOTE M1 X4: the no-DB test (d) uses a fake fetch; the real `resolve_token` builds `FinvizApiClient` (agent config + VaultManager, `finviz_api.py:181`). Not shown to touch the database, but test (d) does not cover it.
- NOTE D1/D2: the live run string stays his to approve; keep it behind D2.

PREFLIGHT DONE · card: s4-p1-72 · checks: 23 · fails: 3 · ready: NO
