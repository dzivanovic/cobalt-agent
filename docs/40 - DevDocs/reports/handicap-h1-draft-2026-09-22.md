# Handicap H1: prompts drafted, 2026-09-22

Seat: Opus 5 prompt drafter `handicap-h1-draft-0922`. Run 12:31–12:44 ET (`date`). The seat worked from reads only. It wrote exactly four files with the Write tool, this report last. No database, docker, pytest, git write or agent launch (L36). No vault write and no memory write (L58).

## DIGEST
- **Scope:** H1 of the float handicap, which is v3 §9's first chunk with R26 "B" built in:
  - float and cap are added to `SourceSet.metrics`
  - the `handicap` block (six keys, no default) is read from his pool note
  - B's pool-wide would-be rank is computed and stored on the membership row, `mode: shadow` only, and never sorts
  - one fail-soft catch
  - the dry-run, with the `h = 1` identity checked over every retained day
  - a `HANDICAP (shadow)` badge on the `/radar` pool row
  - nothing of H2 (live sort, `decisive`) or H3 (card).
- **Steps:** 8 (STEP-0 docs: R26 into v3 plus the ADR-0009 D4 amendment; STEP-1 experiments; STEP-2 … STEP-7 code), then CLOSE.
- **Experiments first:** 12 in STEP-1, **X2 first**, then X4, X1, X3, X9, X10, X5, X6, X7, X8, X11, X15. X15 is measure-only and gates H2. X12 (the identity) runs inside STEP-6.
- **Build seat:** MODEL Opus 5 · `--permission-mode auto` (today's dev-lane reading, stated in the MODEL line) · NEW worktree `/Users/cobalt/cobalt-wt/handicap-h1`, branch `radar/handicap-h1-0922` off main, created by the desk.
- **RESTARTS expected:** `com.cobalt.radar` and `com.cobalt.aset`. They are derived by `cobalt jobs restarts` at CLOSE (L42), not asserted.
- **Migration:** `0014_radar_handicap`. Main ends at `0011`; `0012` belongs to `bars/chunk-2-0920` and `0013` to `setups/seven-0921`.
- **New rule strings:** 2, the `.env` pair for the new worktree. One more string was added that is precedented, not new: `COBALT_ENV=dev uv run cobalt db migrate`. See ESCALATE 1.
- **Check (`28`):** Grok · Gemini · Opus 5, with Sol expected METER (R13). The launch line is `66`'s byte for byte apart from the path and the remote-control name.

## NEW STRINGS
| # | String, verbatim | Re-points |
|---|---|---|
| 1 | `"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/handicap-h1/.env)"` | 09-21 R41's `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/setups-c1/.env)`, same shape as 09-19 R18, new worktree path |
| 2 | `"Bash(rm /Users/cobalt/cobalt-wt/handicap-h1/.env)"` | 09-21 R41's `Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)` |

Precedented, NOT new: `"Bash(COBALT_ENV=dev uv run cobalt db migrate)"`. It is byte-identical in `prompts/2026-09-19/53-deploy-d3.md` (1 hit) and `prompts/2026-09-22/05-stacked-deploy.md` (1 hit), both `grep -c -F`.

## RULE PROOF
The quoted tokens were extracted from each launch line (`claude --bg …` through the last `--add-dir`) and compared with `comm`.

| Prompt | Against | Tokens (sentence + allow + deny) | Differences |
|---|---|---|---|
| `27` | `65` | 24 = 1 + 20 + 3 vs 23 = 1 + 19 + 3 | **17 allow strings identical** · 3 denies identical · `--add-dir` triplet identical · the two `setups-c1` `.env` strings are replaced by the two **NEW** `handicap-h1` strings · **+1 precedented** `COBALT_ENV=dev uv run cobalt db migrate` · the prompt sentence differs. `--permission-mode` is `auto`, not `65`'s `acceptEdits` (ordered by `26`). `--remote-control handicap-h1-0922`. |
| `28` | `66` | 19 = 1 + 15 + 3 vs 19 = 1 + 15 + 3 | `comm -3` shows only the prompt sentence. `diff` of the whole launch segment shows one line changed: the path `2026-09-22/28-handicap-h1-check.md` and `--remote-control handicap-h1-check-0922`. Everything else, including `cd /Users/cobalt/cobalt-wt/agy-trial`, `--model claude-sonnet-5` and `--permission-mode auto`, is byte-identical. |

## RULINGS TAKEN
- **FORMULA_FILES — the factor's module does NOT join the hash in H1.**
  - `src/cobalt/radar/evaluate.py:143` reads "The source files whose bytes ARE the formula (`formula_sha256`)". `:144-152` lists `evaluate.py`, `anatomy/*`, `cards/scoring.py`, `cards/health.py`, `cards/radar.py`, `cards/expire.py` and `aset/engine.py`: the card formula only. `pool.py` was never in it.
  - In H1 no card number reads `h`. The factor is stored on the row and in the receipt's `pool_unit` (`runner.py:319-323`), so it replays from stored inputs (L57).
  - Adding the file would split `formula_sha256` (`:161-166`) with no change to the card formula.
  - H3 re-asks the question when `card_score` gains `h`.
  - Written in `29` §5; CLOSE asserts `git diff main -- src/cobalt/radar/evaluate.py` is empty.
- **FAIL-SOFT — one catch, in `decide()`, around the single handicap call after `pool.py:326`.**
  - Why: `decide()` runs at `runner.py:186`, before S1's `try` (`:189-206`). The resident loop at `runner.py:453-460` calls `cycle()` with no `except`. A handicap exception would therefore kill the resident and launchd would respawn it into the same failure: a pool outage for a shadow feature that sorts nothing (L9).
  - On failure: ranks stay raw, `raw_rank` is kept, `handicap_factor` and `handicap` are stored NULL (not 1, because 1 would claim a verdict — L1), `handicap` goes into `degraded_sources` with a reason, and one `logger.exception` line is written.
  - Parse-time refusal stays loud and separate: `PoolBlock(**raw)` at `notes.py:108` sets `pool_error` and the pool freezes (`notes.py:64-65`). A test proves the catch does not swallow it.
- **The rollback hazard** is written into `27`'s `## FOR THE DEPLOY`: "the desk removes the `handicap:` block from his note FIRST", then the code revert, then `0014`'s rollback. X4 proves freeze versus crash on main's code.
- **`last_scan_ms`** (derive-r2 ESCALATE 6): an ops item, not handled in these prompts.

## ESCALATE
1. **A 20th allow string, beyond `26`'s "nothing else added".** The added string is `COBALT_ENV=dev uv run cobalt db migrate`, precedented in `53-deploy-d3` and `05`. `26` itself orders the BASELINE migrate and the `cobalt_dev` migrate for `0014`.
   - Without the string, both calls go to the auto-mode classifier, and a refusal FAILS the run (L62).
   - **ASK DESK: keep it, or strike it and accept the classifier risk? [12:43 ET]** Safe default as drafted: kept, and named precedented rather than new.
2. **Auto mode on a run that writes to a DB (dev only).** `65` used `acceptEdits` under L29's "never auto mode on a write path". `26` ordered `auto` per today's dev-lane reading (`05`, `12`, `15`). `27`'s MODEL line states that reading. The desk's reading governs; it is flagged because `cobalt_dev` migrate is a write.
3. **v3 §6 was followed over `26`'s paraphrase.** `26` says an absent block means every row stores `h = 1`. v3 §6 says `handicap_factor` is NULL when the block is absent. The build stores NULL (plus `raw_rank`), and the identity test covers both an absent block and a block whose factor is 1 everywhere (`29` §9).
4. **Three columns, not two.** `26` names "`handicap` JSONB + `raw_rank`". v3 §6's table also has `handicap_factor NUMERIC(6,4)`, so `0014` adds all three.
5. **The ADR-0009 D4 amendment has not landed on main.** `docs/10 - Decisions/ADR-0009-…md:28` still reads "pool `last_rank` only admits". v3 §9 puts it "Before H1 [F-08]". It is folded into `27` STEP-0(b), using v3's own text verbatim, and skipped if it has already landed. The desk may prefer to make that edit itself.
6. **`mode: live` under H1 code is a drafter guard, not text from v3.** H1 stores what shadow stores, sorts raw, and flags `handicap` as degraded (`29` §6). v3 does not say what H1 does with `live`; the Literal must accept it ([F-12]).
7. **The X11 stop threshold is the drafter's.** "More than a handful a day" is v3's wording. `27` stops the build only when a day's verdict flips exceed a tenth of that day's in-group names, and otherwise records an `ASK DESK`. This is an engine-side judgement, not a value of his; the desk may re-set it before launch (L19 re-issue).
8. **X12's production half runs at the deploy.** `cobalt_dev` holds no production day, so the `h = 1`-vs-stored-membership comparison is the deploy's read-only acceptance (`27` `## FOR THE DEPLOY`). The build proves identity on the committed fixture and on every retained cache day.
9. **The check's DATE gate.** `28` will most likely launch on 2026-09-23 or later, after the ≈4–8 h build. `grok` / `agy` stand through 2026-09-22 23:59 ET only (09-21 R39), so his extension belongs in tonight's ONE list.
10. **L68 seams, from main `d2d82e7`:**
    - `setups/seven-0921`: `src/cobalt/radar/cli.py`, `src/cobalt/db_migrations/__init__.py` (its `0013`), `tests/experiments/`
    - `bars/chunk-2-0920`: `src/cobalt/radar/runner.py`, `src/cobalt/db_migrations/__init__.py` (its `0012`)
    - `bars/chunk-e-0920`: `tests/experiments/`
    - `s2/stale-marker-0921` and `ops/2026-09-21`: already merged into main (`git branch --merged`)
    - `bars/chunk-1a-0920`: none of these paths.
11. **Placeholders the desk fills before launch (L19):** `R__` in `27` and `28`, and `<STAGGER REPORT>` in `28`. The desk also commits `27`, `28`, `29` and the approval row for the two NEW strings, then runs `git -C /Users/cobalt/cobalt worktree add -b radar/handicap-h1-0922 /Users/cobalt/cobalt-wt/handicap-h1 main`.

HANDICAP H1 PROMPTS DRAFTED · steps: 8 · experiments first: 12 · new rule strings: 2 · migration: yes · restarts: com.cobalt.radar, com.cobalt.aset · ESCALATE: 11
