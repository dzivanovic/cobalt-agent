# S4-P1 card 72 preflight round 2 — 2026-10-06 (seat s4-p1-preflight-r2, read-only)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git rev-parse --short=8 HEAD`; `git diff --stat 2812c2ef HEAD -- src configs tests ops` | `ce49adaf`; diff empty: code the card cites is unchanged since `2812c2ef` | OK |
| 2 | `git diff 192f5abe HEAD -- <card>` | hunks only in M1, T1, C1, W1 and one RECORDS line. Header, C2, C3, C4, D1, DEPLOY GATE, RESTARTS, DECISIONS, NOT IN THIS JOB, READ and CHECK ASKS did not move | OK |
| 3 | header: `grep -c "«FILL"` → `1`; `BASE: «FILL: main HEAD at launch, 8 hex»`; `TIP:`, `CHECK REPORT:`, `HOUSE B:` empty; `BRANCH: ops/s4-p1-1007`, `WORKTREE: s4-p1-1007`; `RULINGS: 2026-10-06 R598` | unchanged by the diff; round 1 #2, #3, #5 (R598 HIS RULING + APPROVED, committed) stand | OK |
| 4 | card committed: `git log -- <card>` | `ce49adaf` (amend), `192f5abe`; no working-tree change to it | OK |
| 5 | round-1 FAIL #11 (C1 floor). Card C1: "the first bar whose start ts ≥ `since` (no floor: a bar that started before `since` never counts) … THE SAME RULE as the F12 replay's trigger (`src/cobalt/replay/cards.py:15-16`, `:242` `b.ts >= start_at`)"; red-first: "including `since` = 10:00:30 with the 10:00 bar touching (first cross the 10:01 bar or later)"; AGREEMENT "both on the minute and off it (10:00:30)". `grep replay/cards.py` | `:15` "Trigger = the first i1 bar starting at or after `created_at`"; `:242` `searched = [b for b in todays if b.ts >= start_at and …]`; `:319` `start_at=card.created_at`. Floor gone, the card's rule equals the replay's, the off-minute AGREEMENT control is present | OK (fixed) |
| 6 | round-1 FAIL #18 (validate wiring). Card T1: "`strike/config.py` holds `STRIKE_TUNABLE_UNITS`, `check()` … and `validate_command_lines()` shaped like the archiver's (`archiver/settings.py:252-273`); `cobalt validate` calls it in a new block right after the archiver's (`src/cobalt/cli.py:466-469`)"; red-first: "`_cmd_validate` driven as `tests/cobalt/test_validate_no_db.py` drives it, with the strike check made to raise naming `strike.poll_interval` → validate fails and the output names that key"; files add `src/cobalt/cli.py` (the validate block); control "every existing `test_validate_no_db.py` test unchanged and green" | `cli.py:466-469` is the archiver block (`validate_command_lines as archiver_lines`, loop prints); `settings.py:252-273` is `validate_command_lines() -> list[str]`; `test_validate_no_db.py` drives `cli._cmd_validate(...)` (`:40`, `:57`, `:77`, `:128`, `:139`). Wiring, file and test now exist | OK (fixed) |
| 7 | round-1 FAIL #19 (`--max-gets`). `grep -c -e "max-gets" -e "max_gets" <card>` → `0`; M1 verb is `--names --cadence --minutes --out`; cap "names × ⌈minutes × 60 / cadence⌉, computed, no argument" | no argument beyond the draft's decisions (R411, R412) | OK (fixed) |
| 8 | NOTE W1. Card W1: "makes its card through `create_radar_card`, which writes the card's F15 `create` record into `"user".prediction_records` (`store.py:1116`, `cards/predictions.py:214`), a table `0022` creates (`0022_prediction_records.sql:32`), above `0013`" | `store.py:1116` `from .predictions import write_record` inside `create_radar_card`; `predictions.py:214` `INSERT INTO prediction_records`; `0022_prediction_records.sql:32` `CREATE TABLE IF NOT EXISTS "user".prediction_records`. `grep -c -F test_strike_detector_db.py ops/desk/gate-lists.md` on BASE → `0` (card expects `2`) | OK (fixed) |
| 9 | NOTE M1 X4, test (f). Card cites `archiver/collector.py:78-83`, `finviz_api.py:93-101`, `:181` | `collector.py:78-83` `resolve_token` builds `FinvizApiClient()` and awaits `_resolve_vault_credentials`; `finviz_api.py:93-101` `__init__(vault_path="data/.cobalt_vault")` builds `VaultManager`; `:181` `_resolve_vault_credentials`. `data/.cobalt_vault` exists on this host, so (f) would run, with its skip reason named for hosts without it | OK (fixed) |
| 10 | new cites: `cli.py:466-469`, `:518`; `settings.py:252-273` | match (see 6) | OK |
| 11 | rows M1, T1, C1-C4, W1, D1 vs ladder `## S4` P1 (re-measure, detector, TRIGGERED, MISSED); round-1 #17 | unchanged; the fixes add a validate wiring, a test and a cap formula, no new scope | OK |
| 12 | trading platform; D2 gate | `## NOT IN THIS JOB` unchanged ("Any trading platform … never touched"); no row touches one. `strike.finviz_max_rpm` still "per DECISION D2"; M1 names no rpm | OK |
| 13 | reds on BASE: `ls src/cobalt/strike` → no such directory | M1/T1/C1-C3 reds hold (`ModuleNotFoundError`); T1's new `_cmd_validate` test and C1's off-minute tests sit in the same new files, red the same way | OK |
| 14 | RESTARTS paragraph and the added `src/cobalt/cli.py` (validate block) | `src/cobalt/cli.py` was already in the `static import reach` row; expected `RESTARTS: com.cobalt.aset com.cobalt.radar` unchanged | OK |

## ISSUES
- NOTE (round 1 #16, not claimed fixed): the NEGATIVE CONTROLS sit in the new files that import the missing module, so on BASE they ERROR rather than pass; they go green with the build.
- NOTE (round 1): `strike.alert_criterion_s` has no P1 reader (M1's verdict hard-codes the Charter's 5 s via D1); P2 reads it.
- NOTE: D2 (Finviz rate) and E1 stay open and his; the D1 live run string stays his to approve, behind D2.
- NOTE: the amend report's RECORDS cite `test_validate_no_db.py` `:39`, `:65`, `:101`; the `_cmd_validate` calls are at `:40`, `:57`, `:77`, `:128`, `:139`. The card cites no such lines; no card change needed.

PREFLIGHT DONE · card: s4-p1-72 · checks: 14 · fails: 0 · ready: YES
