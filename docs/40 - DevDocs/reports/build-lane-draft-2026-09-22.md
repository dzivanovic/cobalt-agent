# Build lane: prompts drafted, 2026-09-22

Seat: Opus 5.5 prompt drafter `build-lane-draft-0922` (`30-draft-build-lane.md`). Run 14:39–14:59 ET (`date`). The seat worked from reads only. It wrote six prompt files and this report, the report last. No database, docker, pytest, git write, agent launch (L36), vault write or memory write (L58). One desk addition came in by peer message at about 14:47 (his R61, verified committed on main, `74fe5c8`). It is folded into `33` as row F6.

## DIGEST
- **`27` H1 build, re-issued.** Scope: v3 H1 as before. R54's dead column is a new **STEP-4A** with RED-first tests (i)–(vii); R54 is also written into v3 [F-10] at STEP-0. AUTHORIZATION now greps R52–R57 plus a `-S` check on R54.
  - Steps: 9 (STEP-0 … 4, 4A, 5 … 7). Experiments first: 12 (X2 first); X1 now also counts dead columns.
  - Model and mode: Opus 5.5, auto. Worktree `handicap-h1`, which already exists.
  - RESTARTS expected: radar, aset. Migration: `0014`.
  - Launch line unchanged byte for byte. New strings: 0.
- **`28` H1 check, re-issued.** Adds one question, Q13 on R54 and STEP-4A. The packet stages the R54 row. File-check (ix) is new.
  - Step count is now nine. The date gate names R30 for 2026-09-23. Launch line unchanged byte for byte.
- **`29` facts packet, re-issued.** §3 items 3, 4, 8, 9, 10, 11 and 12 carry R52–R57, one line each. §2 records that a dead column stores factor 1, not NULL. X1's row is updated.
- **`31` stale-score build, new.** Scope: v2 design C with R37–R45 folded in. R45 (the fresh-price tap race) has its own RED-first test, STEP-4 (iii).
  - Steps: 5. STEP-1 is the experiments before S1, with X10 first. STEP-2 is S1. STEP-3 is the experiments before S2 plus **X30**, the drafter's experiment that decides R40's mechanism. STEP-4 is S2. STEP-5 is X4, X17 and X29.
  - Model and mode: Opus 5.5, auto (stated as `27` states it). New worktree `/Users/cobalt/cobalt-wt/stale-score` on branch `cards/stale-score-0922`, cut by the desk from `__TIP__`.
  - RESTARTS expected: radar and aset, plus the replay one-shot.
  - Migration: only if X30 returns (A). It would be one view migration, `0015` expected.
  - New strings: 2 (the `.env` pair).
- **`32` stale-score check, new.** Launch line = `28`'s byte for byte apart from the path and the remote-control name. That is `66`'s line with R32's Opus string.
  - Q-set: 14 questions. L52 (a)–(d) is Q13. Each of R37–R45 is covered by Q6–Q10. The experiments' AS EXPECTED is re-read in Q12. The L32 grep is Q14 plus the file-check.
  - X9 / X25: the DESK runs them before launch (§1a); see ESCALATE 5. New strings: 0.
- **`33` setups fix r3, new.** Rows F1–F5 = R47, R48, R49, R50, R51, plus **F6 = R61**: (a) a `## DIALS` table per setup of every dial, marked per_trade or assumed/engine only; (b) one test that a per-trade override reaches the evaluator.
  - Base `__TIP__` comes from `12`'s stop line. Model and mode: Opus 5.5, auto. Worktree `setups-c1`.
  - The values for A-09, A-10, A-16 and the new A-24 are proposed ONLY in a gitignored file (ESCALATE 9).
  - Migration: none. New strings: 0.

## NEW STRINGS
| # | String, verbatim | Re-points |
|---|---|---|
| 1 | `"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stale-score/.env)"` | 09-22 R30's `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/handicap-h1/.env)` (09-21 R41 / 09-19 R18 shape), new worktree |
| 2 | `"Bash(rm /Users/cobalt/cobalt-wt/stale-score/.env)"` | 09-22 R30's `Bash(rm /Users/cobalt/cobalt-wt/handicap-h1/.env)` |

Both need his "approve" in the ONE list before `31` launches (L61 / L62). `31`'s AUTHORIZATION refuses without a committed row of his that carries them. No other file carries a new string.

## RULE PROOF
Each launch segment, from `claude --bg` through the last `--add-dir`, was compared token by token with its precedent using `diff`. Every `"Bash(…)"` and deny string was then counted with `grep -c -F` in the precedent file.

| Prompt | Against | Tokens | Diff | `grep -c -F` counts |
|---|---|---|---|---|
| `27` new | `27` at `HEAD` | — | **line 1 byte-identical** (`cmp` silent). Launch segment identical (922 chars); worktree-add line identical | — |
| `28` new | `28` at `HEAD` | — | launch segment identical (904 chars) | — |
| `31` | `27` | 30 vs 30 | `--remote-control stale-score-0922` · the 2 `.env` strings re-pointed · prompt path | 18 allow strings = 1 each · 2 `.env` strings = 0 (NEW) · 3 denies = 1 each |
| `32` | `28` | 25 vs 25 | `--remote-control stale-score-check-0922` · prompt path | 13 allow strings = 1 each · Sol string = 2 · Opus-5.5 string = 2 · 3 denies = 1 each |
| `32` | `66` | — | the remote-control name · `claude-opus-5-5` vs `claude-opus-5` (R32) · prompt path | — |
| `33` | `15` | 29 vs 29 | `--remote-control setups-fix-r3-0922` · **`--model claude-opus-5-5` vs `claude-opus-5`** (R32; ESCALATE 4) · prompt path | 18 allow strings = 1 each · `rm …setups-c1/.env` = 2 · 3 denies = 1 each |

The permission mode is `auto` on all three builders: `27` unchanged, and `31` / `33` as `27` / `15` have it. All 24 AUTHORIZATION phrases were checked against their `| R |` rows, and each count is 1: R30, R32, R37–R45, R47–R58 as used, and R61.

## ORDER
The dev-DB lane has ONE `.env` at a time. Every build prompt PREFLIGHTs `ls -la /Users/cobalt/cobalt-wt/*/.env`, and it must be empty.
1. **`12` fixture cut** (running in `setups-c1`, on `74eefd8`). Its stop line is `SETUPS FIXTURE CUT BUILT <tip> | on 74eefd8 | …`.
2. **`33` setups fix r3.** It PREFLIGHTs `12`'s last line and requires `<tip>` to equal the `__TIP__` the desk fills in.
3. **`31` stale-score.** It stacks on the setups tip. Recommended `__TIP__`: `33`'s report commit, because R42 needs `cards/health.py` left as the tip has it and R50 changes that file in `33`.
4. **`27` H1.** It is off-ladder and main-based, so it could run anywhere in the lane. It stays behind the setups and stale-score work (the R58 lane order).
- Checks run in the house lane after their builds: `16` (re-pointed), then `32`, then `28`. `32` and `28` both need grok/agy by date: R30 covers through 2026-09-23, and later needs his extension.
- **`16` after r3 (not edited; the lines to re-point):**
  - `:1`: the launch description and the range.
  - `:15`: the `tail` path `setups-fix-r2-2026-09-22.md` and the `| on 60ddac4 |` gate → the r3 report and `| on <base> |`.
  - `:16`, `:18`: the ranges `60ddac4..<tip>` and the boundary path list (`15`'s CLOSE → `33`'s CLOSE).
  - `:33–:35`: the packet diffs and the fix report path.
  - `:45`: the FIX-row question set, F1–F5 + P1 → r3's F1–F6. Add the r2 ESCALATE (viii) stop-resolver question and the gitignored proposal file (R48's "read by the check").
  - `:64–:67`: the file-check ranges, and the four `DEF_WRITTEN_*` files, which may now move under `33` F1's rule.
  - `33`'s `## NOTE FOR THE DESK` restates this.

## ESCALATE
1. **R54's scope.** R54 says "INOPERATIVE at factor 1 **for that scan**"; `30`'s test wording says "factor 1 for every name **of that source**".
   - Drafted SCAN-WIDE: STEP-4A (i) asserts both, because scan-wide satisfies both.
   - `ASK DESK: per-source instead? [14:59]`. Safe default as drafted: scan-wide.
2. **R54's definition is the drafter's reading of "whole float / cap column blank".**
   - ONE dead column is enough (float OR cap).
   - A missing header is dead.
   - Unparseable cells count as blank, as [F-10] treats them per cell.
   - Fable (d)'s separate "unparseable non-blank = degraded" rule is NOT built; R54 ruled only the dead column.
3. **The re-issues were made with the Edit tool, not one Write.** `27`, `28` and `29` are whole, complete files (L19). Edit kept every untouched line byte-identical, and the RULE PROOF's `cmp` of `27`'s line 1 depends on that. Disclosed because `30` says "Write tool".
4. **`33`'s `--model` differs from `15`.** `30` asks for the line byte for byte except the path and the remote-control name. R32 says every Opus launch the desk writes carries `claude-opus-5-5`, and `30`'s own L29 line says an Opus 5.5 builder. Drafted as 5.5, so there are three differences from `15`. The desk keeps it or reverts it.
5. **X9 / X25 are run by the DESK, not the check hub (`32` §1a).**
   - `30` asks for them "run by the HUB inside the check under the precedented read string".
   - `32`'s line, `66`/`28`'s byte for byte, carries no production string and no `cd`. Its cwd `agy-trial` has no `.env`, and `src/cobalt/cli.py` loads the `.env` of its own checkout.
   - The precedented strings are named: `Bash(COBALT_ENV=production uv run cobalt db query --side user --prod *)` (`01-radar-benchmark-load.md`'s approved line; the desk's own read at `cto-2026-09-20.md:497`) and `…--side system --prod *` (09-22 R23, `12`).
   - The desk runs them from `~/cobalt` and writes `60-production-x9-x25.md`. If absent, X9 / X25 are recorded UNPROVEN (L70), and that is not a stop.
   - `ASK DESK: or add the two strings plus a .env route to 32 and re-issue? [14:59]`
6. **R40 has no mechanism in v2.**
   - `31` adds the drafter's experiment **X30** (L70) with a decision table:
     - (A) a sound join plus an already-stored pre-fix discriminator → one view migration on `"user".shadow_agreement_v`, number `0015`. That is the next free number after 0012 (bars), 0013 (setups) and 0014 (H1) — an L68 seam.
     - (B) → not built, ASK DESK.
   - This goes beyond the tribunal's text because his ruling requires a mechanism. Under (A), daily-missing pre-fix rows would be over-excluded (W3's two meanings). That is named and accepted, because it only removes rows.
7. **`31`'s version rule is a SEPARATE bump on the setups string, not riding it.** Under [F-08], riding is correct in only one of the two packaging cases. This is the drafter's reading. X20 may refuse old nightly bindings, which is accepted per v2.
8. **`31` restates v2's `file:line` cites by symbol.** Cites are on main `3ceb469`, and the setups branch added about 1,000 lines to `evaluate.py`. The builder writes a `v2 cite → tip line` table at PREFLIGHT.
9. **Values in `33` (R48 / R49) and L32.**
   - `30` asks for each value "with its cited source quoted verbatim" in the prompt. L32 and the FINAL's own rule (`:29`) class cheat-sheet-derived values and quotes as user data, so they must not appear in any committed file.
   - Drafted: values and verbatim quotes go ONLY in the gitignored `setups-c1/docs/_inflight/setups-assumed-values-r3-2026-09-22.md` (`.gitignore:44` `docs/_inflight/*`). The hub proves the file is ignored. Committed files cite by key, companion row and PDF page.
   - The companion's A-09, A-10 and A-16 rows are marked `NO SOURCE NUMBER`, LOW. `33` proposes them under R44's standard only when the hub re-finds the quote on the cited page. Otherwise the hole stays null.
   - The drafter read the companion rows. No value from them appears in any file written here.
10. **`33` F3: `value: null` means today's roles, byte-identical.** This follows the build's Found 13 precedent for a null lifecycle key, not Found 14's "null reads unknown". Found 14's reading would stop every `Leg(impulse)` / `Leg(pullback)` def forming at committed config and move pins. This is the drafter's reading of R49's "in place before cards go live".
11. **`33` F5 (R51).** `TunableUnit` has no `dollars`, so the relabel needs `DOLLARS` added in `src/cobalt/taxonomy/tunables.py`. That is not conversion code, but it is a src change. It is also a rollback hazard (main's enum), named in the rollback doc line. The def-side `buffer: {…, cents: …}` spec key (`predicate.py` `UNITS`, his notes' shape) is left as it is (L45).
12. **`33` F6 comes from the desk's peer message (R61 at 14:46 ET), not from `30`.** R61 was verified committed. F6 (b) is a proof, not a fix: if the override does not reach the evaluator, it is ASK DESK and nothing is committed red.
13. **Placeholders the desk fills before launch (L19):**
    - `28`: `R__`, `<STAGGER REPORT>`.
    - `31`: `__TIP__` (6 occurrences, one fill), `R__`.
    - `32`: `R__`, `<STAGGER REPORT>`.
    - `33`: `__TIP__` (1), `R__`.
    - `27`: its line-1 desk sentence still reads `R__` while AUTHORIZATION names R31. It was kept byte-identical by rule.
14. **v2 step 8 and `[F-18]`'s scoping are superseded by R45** (Fable (i)'s wording). The derive report still shows step 8 alone; `31` names the replacement.
15. **The fix-r2 ESCALATE (viii) (stop resolvers' `tunable_keys`) is NOT built in `33`.** It is carried as a question for the re-pointed `16`.

BUILD LANE PROMPTS DRAFTED · prompts: 6 · re-issued: 3 · new rule strings: 2 · migrations: 2 · ESCALATE: 15
