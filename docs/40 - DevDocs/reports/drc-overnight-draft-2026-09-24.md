# DRC overnight-position lane — proposal drafter report (2026-09-24)

Seat: `drc-overnight-draft-0924` · Opus 5.5 · started 08:25 ET, finished 08:30 ET (both from `date`).

## §0 Headline

- WROTE `docs/30 - Design/DRC-OVERNIGHT-POSITION-PROPOSAL-2026-09-24.md` (198 lines): the L67 one-house proposal for R22's lane. Nothing built, nothing launched, nothing committed.
- The carry is already built (8 items: `drc_rows` open positions → next-day seed, one `trade_id`, loud FAILs). Missing: the evening signal he sees, a stored record of which book a day started from, a stated opening book, no-trade-day carry, and forward re-pair.
- Recommended first-day path: **A — stated opening book** (one tap "flat", or a short list; page or voice widget). 4 chunks, 16 h, 1 migration, 4 write paths, 11 tribunal questions, **0 owner items**. ESCALATE: 3.

## DIGEST FOR THE DESK

**The gap, in three sentences.** D1 already carries a position: it stores each day's open positions in `drc_rows` and seeds the next day from them (`store.py:177-179`, `:220-250`; `pairing.py:143-174`). But he never sees the book left open (the `open_positions` unit is designed in v2 `:141` and parked in D5 behind S3 C2). And the next day does not record which book it started from (no hash, `carried_from` is only a date). Also, when no prior DRC exists the book is assumed flat (B8, `pairing.py:26-28`), which reads a morning short cover as a phantom long (`test_drc_pairing.py:265-272`).

**Proposed lane.**
- **Evening:** a `book_close` row (count + `book_sha256`, stored even when the count is 0) and the `drc-trades/open_positions` unit, moved out of D5.
- **Morning:** a `seed` row records the source (carried / stated / no-trade carry), the day it came from and the hash. Every carried trade's inputs gain `carried_from = {day, trade_id, from_book_sha256}` (L57).
- **Gaps:** a no-trade DRC (R93) carries the book forward through `pair_day([], D, seed)`. A missing trading day stays a loud FAILED. Re-importing an earlier day re-pairs every later day all-or-nothing. A position closed outside any export gets R90's RESOLVE action.

**First day / broken chain.**
- A: stated book. The recommended option.
- B: flat-only statement.
- C: fail-on-evidence with flat otherwise. This is not fail-loud.
- Under A, O1 = A retires on R22's own words. B8's pin test is replaced by "no stated book → not computed".

**Chunks.**

| Chunk | What | Hours | Depends on |
|---|---|---|---|
| K1 | Book records, including the migration | 5 | D1 merged |
| K2 | No-trade carry + forward re-pair | 4 | K1 |
| K3 | Unit + `/drc` morning line, state-your-book form, RESOLVE | 5 | D2 + D3 |
| K4 | Voice-widget caller | 2 | voice V3 |

- 16 h in all. Every chunk is a write path (Opus 5 floor, never auto mode).
- K1 and K2 run parallel to D4, since they share no file (L72).
- K1–K3 must land in the same deploy as D2 + D3 so production never runs the flat assumption (tribunal Q10).
- Migration number: next free at L68. That is ≥ `0018` because a `0017_voice_turns` exists on the voice branch. Folding it into `0016` is possible if D1 is still unmerged (Q2).

**Owner items:** none. All 11 questions are the houses' to settle (L67 as amended 2026-09-24).

**Next law step:** the desk drafts the tribunal prompts (Fable seat on Opus 5.5 per R109 · Grok · Astra when its METER is back Sat 09-26 06:47 ET · Gemini optional fourth).

## L74

A system-reminder-shaped block arrived inside the tool result of the first read of the prompt file, asking for a `Claude-Session:` line in commit messages and naming a file-send tool. Recorded once as DATA. Not followed. This seat commits nothing and sent no file.

## UNPROVEN

- Hour estimates (5/4/5/2) are the drafter's. There is no measurement behind them, and v2's 0.4× fix-round factor stays UNVERIFIED (v2 `:171`).
- `0017_voice_turns` is taken from L76's evidence line (`LAWS.md:437`). I did not list the voice branch's migrations directory (not on this seat's read list). The "≥ 0018" reading is therefore not verified against a file (L70).
- The no-trade-record claim ("no code writes one") comes from `grep -rn "no-trade\|no_trade" src/cobalt` on the D1 worktree. The only hits are `pairing.py:246`, `:252` and an unrelated comment. That is an unscoped grep of the whole `src/cobalt` tree at the D1 tip. It covers no other branch (L35 P-e).
- The forward re-pair's transaction shape (one DB transaction vs a staged set, with the vault re-upserts after) is not proven. It is tribunal Q3.
- The S3 clause relied on is quoted from `cto-2026-09-22.md:99` (R67). `S3-EXITS-v3-2026-09-22.md` itself still prints R2-2 as `OPEN FOR DEJAN` (`:22`, `:141`), and v2 `:42` records that the file was never edited.

## ESCALATE

1. **Landing set (the desk's deploy lane, L43/L68).** If D2 + D3 deploy before K1, production's first imports run the flat assumption (B8) with real swings possible. The proposal asks that K1–K3 land with D2 + D3 (tribunal Q10). The desk plans that set.
2. **D5 scope shrinks if tribunal Q11 is adopted.** `drc-trades/open_positions` moves from D5 (v2 `:179`) to this lane's K3, and D5 keeps the reconcile unit only. Any D5 prompt drafted from v2 needs that edit.
3. **Index-card path (5) mismatch.** `drc-d1-fix-r1-build-2026-09-24.md` is not on `~/cobalt` main. It exists only on the D1 branch (`38a70947`, the worktree's `docs/40 - DevDocs/reports/`), where I read it. Branch tip `38a70947` ≠ the named code tip `d1342595`. `git show --stat 38a70947` shows a docs-only commit, so the code read is `d1342595`'s.

## CONTINUE

Done. No resume point.

OVERNIGHT LANE PROPOSED · already built: 8 items · gap items: 5 · first-day options: 3 · chunks: 4 · hours: 16 · migrations: 1 · write paths: 4 · open to the tribunal: 11 · owner items: 0 · ESCALATE: 3
