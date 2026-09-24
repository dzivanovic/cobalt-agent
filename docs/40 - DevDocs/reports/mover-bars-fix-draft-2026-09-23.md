# Mover bars fix — drafter report (2026-09-23)

Seat `mover-bars-fix-draft-0923` · Opus 5.5 · prompt `prompts/2026-09-23/77-draft-mover-bars-fix.md` + the desk's relay of his R114 (22:08 ET) · written 2026-09-23 22:1x ET (`date` 22:15:10).

## §0
- **What broke.** The one K9.4 loser was fetched cleanly (`archive_failures 0`) and its bars were stored. But those bars did not cover 09:30 → 16:00, so R1-12's `coverage()` rejected them. `archive_movers` then filed the ticker `incomplete`. It was never marked archived, and no log line named it. A halt or a late open fits. Which ticker it was, and whether it had 0 bars or a partial day, is UNPROVEN: that takes a DB read (ESCALATE 1).
- **FIX 1 (R113, design).** A clean fetch with bars short of the session becomes **`partial`**. The bars are kept, the ticker is named in a log line, and it is counted by side in the job row (`archive_partial`, `archive_partial_by_side`). `bars_archived` keeps its R1-12 meaning (a full session), so a partial row never looks complete. The S2 smoke's K9 passes a not-archived row only when the job row's partial count for that side covers it (new rows K9.7–K9.12, the K8 pattern). Zero bars and fetch failures stay red. No migration.
- **FIX 2 (R114, his "yes A").** K17 (`cobalt validate`) is deleted from `configs/cobalt/smoke/s2.yaml`. The `cli` check kind and its test stay.
- **Prompts.** `2026-09-24/07` is the build: Opus 5.5, `acceptEdits`, own worktree, red first, GATE EARLY. It needs 2 new `.env` strings. `08` is the check: Opus 5.5 + Grok, fail closed below two, `04`'s line with no new string. Tribunal needed: **no**.
- **Timing.** The fix makes the 09-24 deploy only if `07` launches tonight: build ≈1 h, `08` ≈1 h, then the `05` stacked re-issue and its `06` re-read ≈2 h, all before 15:00. Otherwise it rides 2026-09-25. ESCALATE: 3.

## FORENSICS
Read only; no DB command was run.

| # | Evidence | Source | Reads as |
|---|---|---|---|
| F1 | `K9.4 … FAIL · not_archived eq 0 (actual 1)`; K9.1 gainers PASS; K9.6 losers stored 20 = allowed 20 | `reports/s2-smoke-look-2026-09-23.md:58, :60` | one active loser row has `bars_archived = false` |
| F2 | `replay 2026-09-23: movers 40 · archived 39 · … · line updated` | `logs/replay.log:108` | 39 of 40 archived |
| F3 | job row `archive_incomplete: 1, archive_failures: 0` | `s2-smoke-look` §0 / K7 | the fetch **did not fail**. The one not archived is counted `incomplete` |
| F4 | `replay.err` 09-23 21:10–21:12: only blank-Change warnings (28 rows per side, unranked) and `cards.expire` INFO lines, then `DONE` | `logs/replay.err` tail | **no line names the incomplete ticker.** The code logs failures (`runner.py:358–359`) but never incomplete ones |
| F5 | archiver 09-23 run: `210 tickers … 0 failures`, `DONE` at 20:54:54; nothing after 21:00 | `logs/archiver.err` tail; `logs/archiver.log` is empty | the archiver played no part. The replay fetches mover bars itself (`MoversCollector.bars`, `movers.py:384`) |
| F6 | `archive_movers`: fetch → `upsert_bars(fetched[ticker])` → `if covered(ticker)` archived, `else outcome.incomplete.append(ticker)` | `src/cobalt/replay/movers.py:593–602` | **the bars are stored before the coverage test.** "Incomplete" means the stored bars do not span the session |
| F7 | `coverage()`: `first > start` → "bars begin …"; `last + 1 min < end` → "bars end …"; no bars → "no i1 bars" | `src/cobalt/replay/cards.py:145–163` | a halt that never reopens, or a late open, fails this rule while the fetch itself succeeds |
| F8 | `runner.py:356` `archive_incomplete = len(outcome.incomplete) + …`; `mark_bars_archived(outcome.archived_ids)` only | `runner.py:353–356`, `movers.py:676–680` | an incomplete row stays `bars_archived = false`, so K9.4 goes red |

**Cause:** the source's i1 bars for one loser did not span the RTH session. The fetch was clean and the bars were stored, but R1-12's coverage gate filed the ticker `incomplete`, and nothing named it. This matches his reading ("halted … has no bars"). **Not yet proven** (L70): whether it held **some** bars (a partial day) or **zero** bars on the day. Both give `incomplete` today. The ticker is `<ticker>` (L32).

## DESIGN

### Where it sits
The fix sits inside ADR-0010 §4 "Movers" (`docs/10 - Decisions/ADR-0010-missed-corpus-counterfactual-r-picks.md:86–92`) and the R1-12 coverage rule (Astra, S2-P4 plan). Both are quoted in `archive_movers`'s docstring (`movers.py:553–558`). R1-12 says "a fetch that still leaves a gap is counted `incomplete`, never archived". The fix keeps "never archived" as written: `bars_archived` still means a full session, and `coverage()` is untouched. It changes only the COUNT class, `incomplete` → `partial`, for a clean fetch that has bars. It also adds smoke rows that accept that class only with its marker. The change is ordered by his R113 words, a direct instruction (L73, 09-21 R5). `07` D3 adds one amendment bullet to ADR-0010 §4.

### Tribunal needed: NO
- This is a fix round inside a ruled design. It adds no new table, migration, component or interface.
- It does not reach scoring, ranking or the card, so L52 does not apply. `movers_daily.bars_archived` is read only by the S2 smoke (`grep bars_archived src/cobalt`: `movers.py`, `cards.py` docstrings, `s2.yaml`).
- L67's build bar applies: `08` seats Opus 5.5 + Grok per his R95.

### FIX 1: the mover with a short source day (R113)

| Case, after a successful fetch + `upsert_bars` | Today | After `07` | Smoke K9 |
|---|---|---|---|
| bars span 09:30 → 16:00 | archived | archived (unchanged) | green |
| ≥ 1 i1 bar on the day, short of the session (halt, late open) | `incomplete`, unnamed | **`partial`**, kept, `bars_archived = false`, WARNING log with `<n> i1 bars, first → last`, job row `archive_partial[]` (code `source_bars_short` + the `coverage()` detail, L57) and `archive_partial_by_side` | **green only when** the side's not-archived count = the job row's partial count for that side (K9.7–K9.12) |
| 0 i1 bars on the day | `incomplete`, unnamed | `incomplete`, **ERROR log naming it** | red |
| fetch raised | failure, job FAILS | unchanged | red (K7) |

Rejected alternatives:
- (a) A `bars_partial` column on `movers_daily`. This needs migration 0018. The migration-tail tests pinned per branch (setups `0013`, bars-chunk-2 `0012`, drc `0016`, voice `0017`) are the 09-23 cross-branch-pin stop class, and the column would add a migrate step to the deploy.
- (b) Setting `bars_archived = true` for a partial. The row would look complete (L1).

The smoke half follows s2.yaml's own K8 pattern: a user-side count, a system-side job-row number, then a `compare`. The two sides share no role, so the count cannot be taken in one SQL statement. Each side is a partition: a not-archived row is partial, incomplete or failed. So "not_archived = partial count" holds exactly when that side has no incomplete and no failed row.

### FIX 2: K17 out of the S2 smoke (R114)
- Delete the `- id: K17` block (`configs/cobalt/smoke/s2.yaml:507–512`).
- Keep the `cli` kind and `test_kind_cli_exit_code_through_the_allowlist` (synthetic, `test_smoke.py:693`).
- Red first: T7 asserts that no committed check is K17 or `cobalt validate`.
- Docs placement stays with the nightly close's `validate`.

### Build shape (`07`)
- **Red:** T1–T7 across 3 test files. T1 AMENDS the existing pin `incomplete == ["QNME"]` (the 30-bar short day). The ruled behaviour changes on his R113 words, so the checkers see it named.
- **Fix:** `movers.py`, `models.py`, `runner.py`, `cli.py`, `s2.yaml`.
- **Docs:** the DevDocs that exist, plus the ADR-0010 bullet.
- **Gates:** live-note, offline, with-DB (one-owner lock, `.env` removed), `RESTARTS` (expected `com.cobalt.replay` one-shot only).
- **Seam:** `test_replay_runner.py` is also edited by `setups/seven-0921` and `cards/stale-score-0922` at ~:418 / ~:472. `07` appends at the end only, and the L68 stacked gate proves it.

### Why `acceptEdits` for `07`
`archive_movers` holds `upsert_bars` and feeds `mark_bars_archived`, which is a DB write path (L29). The mode is `acceptEdits` plus the full list, the `65` precedent and L63's interim practice. The strings are `03`'s 20 with the `.env` pair re-pathed.

### Riding 09-24 (L43)
The fix rides 09-24 only if it is BUILT + CHECKED before 15:00 ET and the desk re-issues `05` as a stacked set with the setups branch, and that re-issue gets its `06` house read. The branch has no migration and no resident restart, so it adds no deploy step beyond the stacked gate. The smoke that closes it must read a post-deploy replay night. Realistic: **09-24 if `07` launches tonight** (the dev-DB lock is free, `ls -la ~/cobalt-wt/*/.env` → `no matches found` at 22:1x). Otherwise **09-25**.

## FOR DEJAN
1. **Two new rule strings for `07`**: `"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/mover-bars/.env)"` and `"Bash(rm /Users/cobalt/cobalt-wt/mover-bars/.env)"`. They are your R41 pair (2026-09-21, `setups-c1` only) with only the worktree path changed, and are used only for the with-DB gate on `cobalt_dev`. Approve? (fills `07`'s second `R__`)
2. **Ruling: a clean fetch with ZERO bars on the day.** A (built by default): red, named in an ERROR log. A top mover with a printed change must have traded, so zero bars is a source defect (L9). B: green, as `no_source_bars` with the same marker. B is a one-list change in `07` if you rule it.
3. **Grok for `08`**: a row of yours extending `Bash(grok *)` through the check's date and naming `08-mover-bars-fix-check.md` (the date gate, same shape as `04`'s; fills `08`'s `R__`).

## ESCALATE
1. **ASK DESK** [22:15]: the ticker and its bar count are UNPROVEN from logs (F4). This only decides which row of the FIX 1 table 09-23 was; the fix covers both. Read-only SQL, desk-run if wanted:
   - production `system` side: `SELECT side, rank, ticker, change_pct, volume, fetched_at FROM system.movers_daily WHERE trade_date = DATE '2026-09-23' AND active AND NOT bars_archived;`
   - then, on the archiver's `bars` table (`src/cobalt/archiver/migrations/0001_bars.sql`): `SELECT count(*), min(ts) AT TIME ZONE 'America/New_York', max(ts) AT TIME ZONE 'America/New_York' FROM bars WHERE ticker = '<ticker>' AND interval = 'i1' AND ts >= TIMESTAMPTZ '2026-09-23 00:00 America/New_York' AND ts < TIMESTAMPTZ '2026-09-24 00:00 America/New_York';`
2. **L1 finding, fixed by `07`**: today the replay names an `incomplete` mover in no log and no row. That gap is why F4 could not name the case.
3. **Deploy carry**: a job row written before the deploy has no `archive_partial_by_side`, so K9.8 / K9.11 would ERROR on a pre-deploy night. The first post-deploy S2 smoke must read a post-deploy replay night. This is stated in `07` CLOSE and in `08`'s standing lines.

MOVER BARS FIX DRAFTED · cause: a loser's source i1 bars were short of the RTH session (clean fetch, bars stored) → R1-12 coverage filed it incomplete, unnamed · tribunal needed: no · prompts: 2 · new rule strings: 2 · ESCALATE: 3
