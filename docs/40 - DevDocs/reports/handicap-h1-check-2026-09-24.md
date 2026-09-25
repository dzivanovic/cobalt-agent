# HANDICAP H1 CHECK — round 1 — 2026-09-24

## §0 Headline
Round 1 check of the H1 build `f6643d41..27df13f1` (branch `radar/handicap-h1-0922`) and its three suites' executed output. Seats: Opus 5.5 `CHECK: FIX` (two items), Grok `CHECK: BUILD STANDS`; Sol NOT SEATED (METER until Sep 26th, 2026 6:47 AM), Gemini out (R96/R97), Astra out (R46).
Both defect claims HOLD in my file-check as facts (five XL76 callers keep `dev_db_tx` beside `migrated_radar`; `_cut_tier`'s docstring names X2's rule but implements another); nothing sorts on the factor, `_ranked` / `_metric_position` hunk-free, ONE new `try`, migration order and L76 harness as built.
Ready for a deploy prompt: 1 of 2 (`CHECK: BUILD STANDS` lines out of the houses that answered; the floor is 2, R95). ESCALATE: 14.

## L74
Recorded ONCE: a system-reminder block attached to the result of my first tool call (the `Read` of the prompt file `45-handicap-h1-check-r2.md`) asked for a `Claude-Session: https://claude.ai/code/session_…` line in every commit message and named a file-send tool (`SendUserFile`). It is DATA, never followed. This run makes no commit and sent no file.

## PREFLIGHT
| # | rule · command | exit | result |
|---|---|---|---|
| 1 | PLACEHOLDER GATE · `grep -n -E "R_[_]" <this prompt>` | 1 | printed nothing — allowed |
| 2 | `date` | 0 | `Thu Sep 24 21:07:54 EDT 2026` → `<D>` = 2026-09-24, 21:07 ET — allowed |
| 3 | THE GROK GATE (first row) · `grep -n "^| R17 " cto-2026-09-24.md` | 0 | line 32, carries `Grok approved with no asking going forward` — allowed |
| 3b | `git log -1 --format=%H -S"Grok approved with no asking going forward" -- cto-2026-09-24.md` | 0 | `1758fd78a572f47b613b2ca831dcfa636ed8f65a` (non-empty) — allowed |
| 3c | `grep -n "^| R19 " cto-2026-09-24.md` | 0 | line 34, carries `All 4 house models approved for use indefinlitly` — allowed |
| 3d | `git log -1 --format=%H -S"All 4 house models approved" -- cto-2026-09-24.md` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty) — allowed |
| 4 | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` — allowed |
| 5 | R26 · `grep -n "^| R26 " cto-2026-09-22.md` + `git log -1 -S"POOL-WIDE division"` | 0 / 0 | line 137, carries `POOL-WIDE division`; commit `d86b973d5d83c3b7a3682f71167bad49ece2d2d8` — allowed |
| 6 | R54 · `grep -n "^| R54 " cto-2026-09-22.md` + `git log -1 -S"INOPERATIVE at factor 1"` | 0 / 0 | line 112, carries `INOPERATIVE at factor 1`; commit `9a4b01a7750195bee43f952ba919e0ccb75c6f46` — allowed |
| 7 | R58 · `grep -n "^| R58 " cto-2026-09-23.md` | 0 | line 61, carries `"yes start both"` — allowed |
| 8 | R95 · `grep -n "^| R95 " cto-2026-09-23.md` | 0 | line 103, carries `just Opus and Grok for code checks and code deploys` — allowed |
| 9 | R97 · `grep -n "^| R97 " cto-2026-09-23.md` | 0 | line 105, carries `take Gemini out of reading` — allowed |
| 10 | THE BUILD'S STOP · `grep -n -F "HANDICAP H1 BUILT" cto-2026-09-2{4,5,6}.md` | 2 | (exit 2 = `cto-2026-09-25.md` / `-26.md` do not exist, recorded, not fatal) rows R85 (line 105), **R89** (line 110, quotes the stop line), lines 118 / 130 — allowed |
| 11 | THIS launch · `grep -n "45-handicap-h1-check-r2.md" cto-2026-09-2{4,5,6}.md` | 2 | line 110 = row **R89** (21:06 ET) names this file — allowed |
| 11b | `git log -1 --format=%H -S"45-handicap-h1-check-r2.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | 0 | `7c21fe86f9efae6363739ec32b752cacf4ce6925` (non-empty) — allowed |
| 12 | THE LINE IS `15`'s · `grep -c -F -e "<rule>" 15-drc-d1-fix-r1-check.md` ×14 allow + 3 deny | 0 | every one counts 1 (Bash(grok *), mkdir, the two main git strings, three `s2-p2-cards`, ls, grep, tail, wc, date, Sol `codex exec`, Opus `claude -p`; deny AskUserQuestion, EnterWorktree, git push) — allowed. No Astra string, no `Bash(agy *)` in the launch line |
| 13 | `ls /Users/cobalt/cobalt-wt/handicap-h1` | 0 | worktree present (AGENTS.md … uv.lock) — allowed |
| 14 | THE BUILT LINE · `tail -n 3 <build report>` | 0 | last non-blank: `HANDICAP H1 BUILT 27df13f1 \| on f6643d41 \| experiments 14/12/2 \| offline 2619/0 \| with-DB 2976/0 \| live-note 131/0 \| migration: 0014 rolled back \| cobalt_dev: 0013 \| h=1 identity: proven \| .env: removed \| ESCALATE: 12` — starts `HANDICAP H1 BUILT `, carries every required field; NOT `cobalt_dev: UNPROVEN`. **`<tip>` = `27df13f1`, `<main tip>` = `f6643d41`** |
| 15 | `git show f6643d41:src/cobalt/db_migrations/0013_tunables_slug_nullable.sql` | 0 | prints the file — `0013` is under the build |
| 15b | `git log --oneline f6643d41..a2d320b8` | 0 | EMPTY — `deploy-2026-09-24` is under the base |
| 16 | THE RANGE · `git log --oneline f6643d41..27df13f1` | 0 | ten commits: `4c1c92f2` S0 · `0598c6ac` S1 · `8f178af2` S2 · `5693fe41` S3 · `a7928964` S4 · `f11836b8` S4A · `a16c97ff` S5 · `71e0da42` S6 · `9fb8a8e2` S7 · `27df13f1` CLOSE probe test (nine steps + one CLOSE test commit — a different count is recorded, not fatal) |
| 17 | `git log --oneline -1 radar/handicap-h1-0922` | 0 | `026c99b8` (the report commit above `<tip>`) |
| 17b | `git log --oneline 27df13f1..radar/handicap-h1-0922 -- tests src configs` | 0 | EMPTY — the branch did not move above `<tip>` in code |
| 18 | `git log --stat --oneline f6643d41..27df13f1` | 0 | staging list + boundary: see `## Checked against the branch` (i). `tests/cobalt/conftest.py` and `src/cobalt/db_migrations/placement.py` do NOT appear |
| 19 | `ls /Users/cobalt/cobalt-wt/handicap-h1/.env` | 1 | `No such file or directory` — as required |
| 20 | `ls scratch/tribunal-bars-0920` | 0 | present — allowed |
| 20b | `ls scratch/tribunal-bars-0920/handicap-h1-check` | 1 | `No such file or directory` — fresh run |
| 21 | THE STAGGER · `grep -n -F "no other house hub is running" cto-2026-09-24.md` | 0 | line 110 (R89) carries `no other house hub is running` AND names `45-handicap-h1-check-r2.md` (`44` stopped 19:22, R88) — allowed |
| 22 | OPUS probe · `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (`run_in_background`) | 0 | `OK` (stdout also carried a harness warning about the `Bash(git push*:*)` deny-rule syntax in `cobalt/.claude/settings.local.json`; noise) — `opus: UP` |
| 23 | SOL — keyed on `date` (2026-09-24 21:07 ET < 2026-09-26 06:47) | — | NOT probed. `sol: METER — retry after Sep 26th, 2026 6:47 AM (54's probe)` |
| 24 | Grok probe | 0 | by its `--version` row (4) — `grok: UP` |
| 25 | FAIL CLOSED · count UP | — | Opus + Grok = 2 UP (Sol METER; Gemini and Astra not seated) — floor of TWO met |

## Packet
Folder `scratch/tribunal-bars-0920/handicap-h1-check/` (created by the first Write; no `mkdir`). Range `f6643d41..27df13f1`. Every original was taken from a saved `run_in_background` git output or the file itself, Read → Write; each copy `wc -c`-checked against its original, and every non-blank line of each copy checked to be a line of the original (`grep -v -x -F -f <original> <copy>` prints only my own empty lines / headers).

| file | bytes | status | check |
|---|---|---|---|
| `00-READING-ORDER.md` | 26,516 | guide | mine; its 18 step-list lines (`43`'s headings and `Files:` lines) each an exact line of `43` (`grep -c -x -F -f 43 00` = 18) |
| `01-QUESTIONS-CHECK.md` | 9,531 | MANDATORY | both paragraphs found verbatim in this prompt (`grep -c -F -f 01 <prompt>` = 2, lines 49 and 50) |
| `10-rulings.md` | 7,202 | MANDATORY | R26, R13, R54 (09-22), R58, R95, R97 (09-23), R9, R10 (09-24): each row an exact line of its desk file (`grep -c -x -F -f` = 3 / 3 / 2) |
| `11-design-v3.part1` + `part2` | 37,053 + 36,929 = 73,982 | MANDATORY | = the saved `git show 27df13f1:"docs/30 - Design/FLOAT-HANDICAP-v3-2026-09-21.md"` output (73,982 B, incl. the shell's `[exited with code 0]` trailer, kept as the last line of part2) |
| `12-facts-packet.md` | 18,431 | MANDATORY | = original `29-handicap-h1-facts.md` (18,431 B), byte for byte |
| `13-b-text-source.md` | 5,640 | MANDATORY | header + lines 37–57 of the derive-r2 report; body lines exact |
| `20-diff-src.part1`–`part5` | 28,383 + 32,733 + 37,207 + 36,236 + 23,070 = 157,629 | MANDATORY | = the saved `git log -p -W f6643d41..27df13f1 -- src/cobalt configs` (157,629 B); `diff --git` 2+5+3+3+4 = **17** = the `--stat` src+configs touches; `commit ` 2+1+2+1+1 = **7** |
| `21-diff-migration.md` | 3,375 | MANDATORY | the `0014` pair and `FORWARD`/`REVERSE` lines; body lines exact |
| `30-diff-tests.part1`–`part5` | 37,881 + 33,061 + 31,964 + 32,810 + 30,503 = 166,219 | MANDATORY (all five: each holds a named test, see `00`) | = the saved `git log -p f6643d41..27df13f1 -- tests` (166,219 B); `diff --git` 8+11+3+6+7 = **35** = the `--stat` test touches (1+2+3+11+1+2+2+1+12); `commit ` 4+2+1+2+0 = **9** |
| `40-diff-docs.part1` + `part2` | 25,916 + 21,049 = 46,965 | part1 OPEN, part2 MANDATORY (the STEP-0 commit) | = the saved `git log -p f6643d41..27df13f1 -- docs` (46,965 B); `diff --git` 14+2 = **16**; `commit ` 7+1 = **8** |
| `50-build-report.md` | 28,116 | MANDATORY | 7 excerpts (lines 1–10, 15–53, 54–129, 515–542, 729–758, 759–818, 823), 244 body lines, every one an exact line of the build report |
| `51-build-report-steps.part1` / `part2` / `part3` | 17,345 / 13,543 / 17,893 | part1 + part3 MANDATORY, part2 OPEN | bodies = report lines 138–279 / 280–372 / 373–514 (17,105 / 13,279 / 17,643 B, byte counts equal) |
| `52-suites.md` | 7,510 | MANDATORY | `## BASELINE` (lines 130–137) and `## CLOSE`'s suite rows (543–602); each carries an executed summary line — no `FAILED: packet` |

**Honest size** (bytes as staged; tokens = bytes ÷ 4): MANDATORY set without `00` = 533,922 B ≈ 133,481 tokens; whole packet without `00` = 573,381 B ≈ 143,345 tokens; with `00` (26,516 B ≈ 6,629 tokens): MANDATORY 560,438 B ≈ 140,110 tokens; whole 599,897 B ≈ 149,974 tokens. Under 1,200,000 B: one read for every seat, no two-run split.

**Trailing-whitespace disclosure:** the originals carry lines ending in whitespace — the source diff 174 lines, the test diff 29, the docs diff 59 (single-space context blanks, commit-body indents, the tab after a name with spaces); the copies carry the same counts (45+5+61+35+28 = 174; 9+17+1+2+0 = 29; 40+19 = 59). The v3 file, facts packet and build report have 0. The four saved `git` outputs end with the shell tool's `[exited with code 0]` line, kept as the last line of the last part of each (disclosed in `00`).

**Corrected while staging (caught by `wc -c` / the line-set check, fixed before launch):** `20-diff-src.part5` (two mistyped context lines of the `__all__` hunk, +3 B) and `40-diff-docs.part1` (one line of a docs hunk mistyped, and a dropped trailing blank line) — both re-checked to the original size.

**Launches.** `date` at launch `Thu Sep 24 21:43:24 EDT 2026`; THE GROK GATE re-read then: R17 line 32 (`1758fd78…`) and R19 line 34 (`5055151d…`), both committed. Before-launch `ls -la`: the packet folder = the 26 packet files `00`…`52` (no `*-check.md`; latest mtime 21:43 = my own `00`); `/Users/cobalt/cobalt-wt/handicap-h1` = the 27-entry worktree root, no `.env` (mtimes ≤ 20:57). Same listings taken before the Grok launch (seconds apart).
- OPUS 5.5, launched 21:43 (bg `brw3g6zj0`): `claude -p --model claude-opus-5-5 "You are OPUS. The folder is scratch/tribunal-bars-0920/handicap-h1-check/. Start with 00-READING-ORDER.md and follow 01-QUESTIONS-CHECK.md exactly. Files split into ordered parts name.part1.md … are read in order as one file. Do not open any *-check.md file. Read files with the Read, Grep and Glob tools only. Write no file. Print your complete check as your answer." --permission-mode plan --add-dir /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/handicap-h1-check --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"`.
- GROK, launched 21:43 (bg `bjf94z8zk`): `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "You are GROK. The folder is scratch/tribunal-bars-0920/handicap-h1-check/. Start with 00-READING-ORDER.md and follow 01-QUESTIONS-CHECK.md exactly. Files split into ordered parts name.part1.md … are read in order as one file. Do not open any *-check.md file. Write your complete check to /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/handicap-h1-check/grok-check.md and reply with only that path."` (never `--always-approve`).
- The 45-minute clock: deadline 22:28 ET for both. SOL not launched (METER, retry Sep 26th, 2026 6:47 AM). Gemini not seated (R96/R97). Astra not seated (R46).

**Results and the written-nothing proof.** OPUS returned at 21:49 (≈ 6 min; stdout 17,580 B; `opus-check.md` written by me from stdout, first line — a harness warning about the `Bash(git push*:*)` deny-rule syntax — and the `[exited with code 0]` trailer dropped; every non-blank line of the copy is a line of the stdout file). GROK returned at 21:57 (≈ 14 min); it wrote `grok-check.md` itself (25,777 B) and printed only the path. Both inside the 45-minute clock; no HARNESS / METER / TIMEOUT; one attempt per house. After both returned: the packet folder = the 26 packet files unchanged (same sizes and mtimes) plus `opus-check.md` (mine) and `grok-check.md` (Grok's own); `/Users/cobalt/cobalt-wt/handicap-h1` = the same 27 entries, no `.env`, every mtime ≤ 20:57; `git log -1 radar/handicap-h1-0922` still `026c99b8`. `grep -c -i "denied\|not allowed\|permission"` on `opus-check.md` and `grok-check.md` = 0 each.

## CONTINUE
next: none — collation is complete; the report ends on the stop line.

## Per question
Cells ≤ 20 words. "challenging" counts checkers who raised a qualification or challenge on that question.

| # | question | builder's claim | opus | grok | challenging |
|---|---|---|---|---|---|
| 1 | B as built | B computed after `_ranked`, Decimal, tie to the unhandicapped name | YES on all six points; constructed pool: S stores 3 → 5, L stores 4 → 3 | Yes; computed after `_ranked`, `Decimal`, `applied` flag sorts False first | 0 |
| 2 | shadow never sorts | no consumer reads the would-be rank | seven consumers listed, none reads it; test covers every main field + `raw_rank` | same list; test compares H1-absent vs H1-shadow, "does not execute main" | 0 |
| 3 | `h = 1` identity | proven on committed scan and 6 days / 1923 scans / 0 | holds; "weaker than the prompt's wording": both sides are H1 code | yes, "as absent versus factor 1 under this code, not a second execution of main" | 2 (qualification) |
| 4 | loud refusal, no default | six keys required, no default, pool freezes | model refuses each key; reader path proven for `combinator` only | same; other five keys not each run through `parse_note_bytes` | 2 (qualification) |
| 5 | fail-soft | ONE catch in `decide()`, NULL not 1, one ERROR | one place; "resident loop has no `except` — NOT SHOWN in this packet" | one catch; the no-`except` half "is the facts packet's claim, not re-shown" | 2 (packet gap) |
| 6 | `FORMULA_FILES` | `evaluate.py` untouched, no card number reads the factor | true; wording loose: `pool_unit` carries the factor's inputs, not the factor | reason holds; `pool_unit` carries metrics and block | 1 (wording) |
| 7 | storage + harness | additive 0014, only in rollback txns, XL76 (A), conftest untouched | migration fine; five callers keep `dev_db_tx` beside `migrated_radar` → defect 1; ranked LEAVE writes none | migration fine; notes the same stacking, no defect | 1 (defect) |
| 8 | rollback order | block removed FIRST | yes; X4 freeze not crash | yes | 0 |
| 9 | L32 | no value of his committed | lists the builder's literals for the hub to grep | no suspect line in production code, config, migration, commit message | 0 |
| 10 | experiments | 14 / 12 as expected / 2 not | all follow; X4 load path and X5 stored half UNPROVEN | all follow; no §4 stop | 1 (partial) |
| 11 | L52 (a)–(d) | met | (d) "only partly": a row alone cannot give the index; ranked LEAVEs store no record | (c): v3's own L52 (c) paragraph still says OPEN FOR DEJAN; (d) same limit | 2 |
| 12 | outside H1 / missing | nothing outside H1 | nothing outside; missing: "not replayable from bars" line, [F-16] top-ten ladder | nothing outside; missing: [F-16] top-ten ladder; identity/shadow tests are H1-vs-H1 | 2 |
| 13 | R54 dead column | inoperative at factor 1, degraded, panel line | as ruled; 6 of 11 RED first, 5 green by construction (disclosed) | same, plus: on a blank column each row also shows `unknown → not applied` | 1 (note) |
| 14 | suites | three summaries, deselect 2, absence `=0` | offline, with-DB, live-note all SHOWN | all SHOWN, baseline and close | 0 |

### Question 1 — B as built (every checker's answer, unedited)
**OPUS:**

| point | verdict | evidence |
|---|---|---|
| Computed after the raw ranking | YES | `20-diff-src.part4.md:180` `_ranked(...)`, then the one call at `:191-197` |
| Dividend is the raw rank, divisor is the name's factor | YES | `20-diff-src.part3.md:598` `Decimal(ranks[ticker]) / factors[ticker]`. The factor is `block.factor` when the verdict is `yes`, or `unknown` under `apply`; otherwise it is 1 (`:591-593`) |
| Decimal, never float | YES | The factor is a `Decimal` field (`part5.md:436`). The float case is pinned by a test (`30-diff-tests.part3.md:89-100`) |
| Sort key `(eff, in_group, raw_rank)` | YES | `part3.md:599`. `applied[t]` is the boolean "handicapped" flag, so False sorts first |
| Exact tie goes to the unhandicapped name | YES | Test at `30…part3.md:82-86` |
| `_ranked` and `_metric_position` untouched | YES | The `-U0` hunk headers (`51.part2.md:61`) start at `-220` in `decide`, with none in 94-106 or 109-212. The `-W` header `@@ -215,191 +230,236 @@ def _ranked(` (`part4.md:62`) is only git's function-name label: the hunk body starts at `def decide(` |

**Constructed pool.** Factor 0.5 (my literal). Raw ranks: U1=1 and U2=2 (unhandicapped), S=3 (a handicapped screen name), L=4 (an unhandicapped list name), U5=5.
- The quotients are 1, 2, 6, 4, 5, so the would-be order is U1, U2, L, U5, S.
- For S the code stores `raw_rank` 3, `handicap_factor` 0.5000, `handicap.position` 3 and `handicap.effective_position` 5.
- For L it stores 4, 1.0000, 4 and 3.
- `rank` and `last_rank` stay 3 and 4.

**GROK:**
Yes, for the would-be rank H1 stores. It is computed after `_ranked` returns, not inside it (`20-diff-src.part4.md:180-197`). `eff = Decimal(ranks[ticker]) / factors[ticker]` (`20-diff-src.part3.md:598`). The dividend is the raw rank. The divisor is the block's factor when the verdict applies it (`yes`, or `unknown` with `missing: apply`), else `Decimal(1)` (`20-diff-src.part3.md:591-592`, `:733`). Both operands are `Decimal`; there is no `float` division. The would-be order is `sorted(..., key=(eff, applied, raw_rank))` (`20-diff-src.part3.md:599`). `applied` is that same boolean, not the verdict string `yes|no|unknown`. `False < True`, so on an exact `eff` tie the unhandicapped name is first. `effective_position` is the 1-based index in that order; `HandicapRecord.position` is the raw rank (`20-diff-src.part3.md:600-610`). In shadow, `ordered` and `ranks` are not rebuilt (`20-diff-src.part4.md:182-185`, `:217`). That is R26's "computed, stored, not used", not the live sentence "ranks is rebuilt".

`_ranked` and `_metric_position` are untouched. The `-W` hunk header `@@ -215,191 +230,236 @@ def _ranked(` (`20-diff-src.part4.md:62`) opens on `def decide(` (`:63`); no added or removed line is inside `_ranked`. `_metric_position` does not appear in the source diff. STEP-4's `-U0` headers, recorded at `51-build-report-steps.part2.md:61`, are all `Transition`, `Decision`, or `def decide(` — none inside `_metric_position` (94–106) or `_ranked` (109–212).

Constructed pool, same shape as the pinned homogeneous case (`30-diff-tests.part3.md:66-79`, `:483-515`): one screen, every name in the group; one other source, none in the group; same tier; raw order interleaves. With the test's factor below 1, the code writes `handicap_factor` = that factor on each in-group name and `1` on each other name; `position` = `raw_rank` = `Transition.rank`; `effective_position` for raw places 1..6 is 2, 1, 5, 3, 6, 4 (in-group, other, in-group, other, in-group, other). A two-name case (screen name raw rank 1 in group, list name raw rank 2 not) ties when the factor is one half (`eff` 2 and 2): the list name sorts first, so the screen name stores `position` 1, `effective_position` 2, `handicap_factor` = the block factor, and the list name stores `position` 2, `effective_position` 1, `handicap_factor` 1. Admission order stays the raw order.

### Question 2 — shadow never sorts (every checker's answer, unedited)
**OPUS:**

| consumer | reads | file:line |
|---|---|---|
| `winners` | `ordered[:seats]` (raw) | `part4.md:217-219` |
| `Transition.rank` | `ranks[...]` / `ranks.get` | `:230`, `:238-239`, `:256-257`, `:277`, `:284` |
| `last_rank`, `rank_at_entry` | `item.rank` | `part3.md:94-104`, `:171` |
| stickiness and `below_cap_streak` | raw ranks; the loser is chosen by `max(..., ranks[t])` | `part4.md:234-265` |
| held eviction | `last_rank` | `:166-175` |
| poller | `PollMember(item.ticker, item.rank)` sorted by `(rank, ticker)` | `:496-499`; X7 (`51.part1.md:95`) |
| `/radar` row order | `last_rank` | `part1.md:284-289` |

- Nothing in this list reads the would-be rank or the factor. They reach only the Transition, the store, the panel's display cell (`part1.md:404-422`) and the dry-run.
- **Test coverage:** the shadow tests compare `model_dump(exclude={handicap_factor, handicap})`. That is every field that exists on main, plus `raw_rank`, plus action order, with a sticky member in play (`30…part3.md:108-124`). The same check runs on a dead-column scan (`part2.md:617-625`), and the panel test shows a handicapped row does not move (`part1.md:187-191`).
- **`mode: live`:** it stores exactly what shadow stores and ranks raw. It adds `handicap` with the reason `mode live needs H2 — ranking raw`, and the panel shows `degraded` (`part3.md:617`; `30…part3.md:217-229`; `part1.md:140-141`).

**GROK:**
None of these read `effective_position` or `handicap_factor`:

| Consumer | What it reads | Where |
|---|---|---|
| `winners` | `ordered[:seats]` from `_ranked`, after the comment that `ordered` / `ranks` are untouched | `20-diff-src.part4.md:184-185`, `:217` |
| `Transition.rank` | `ranks[ticker]` (raw) on RETAIN, ADMIT, EXCLUDE, ranked LEAVE | `:230`, `:239`, `:257`, `:277`, `:284` |
| `last_rank` | `item.rank` on RETAIN and on the INSERT | `20-diff-src.part3.md:94-103`, `:171` |
| `rank_at_entry` | `item.rank if entered else None` | `:171` |
| stickiness / `below_cap_streak` | membership in `provisional` (the raw `winners`); the evicted newcomer is `max(..., key=ranks[ticker])` | `20-diff-src.part4.md:217-218`, `:234`, `:251-260` |
| poller order | `PollMember(item.ticker, item.rank or 10**9)`; frozen path uses stored `last_rank`. `poller.py` is not in the diff. The recorded read is `for member in sorted(members, key=lambda item: (item.rank, item.ticker))` | `20-diff-src.part4.md:496-503`; `51-build-report-steps.part1.md:95` |
| `/radar` row order | `sorted(..., key=(last_rank is None, last_rank, id))` | `20-diff-src.part1.md:284-286` |

The badge prints `effective_position`; it does not sort (`20-diff-src.part1.md:404-422`).

`test_shadow_changes_nothing_but_the_new_fields` dumps every field except `handicap_factor` and `handicap` (`30-diff-tests.part3.md:31`, `:108-120`), so every field that exists on main, plus `raw_rank`, between a shadow decision and an absent-block decision under this code. It does not execute main. `raw_rank` matches because both paths set it from `ranks`.

`mode: live` stores the same factors and the same record fields as shadow (except `mode` and `block_sha256`), keeps the raw order, and sets `degraded_sources` to include `handicap` with reason `mode live needs H2 — ranking raw` (`20-diff-src.part3.md:519`, `:617`; `30-diff-tests.part3.md:217-229`). The pool-level `degraded` flag stays false. The panel never renders `live`: a `handicap` degradation, or `mode == live` with no such entry, is `degraded` (`20-diff-src.part1.md:128-142`; `30-diff-tests.part1.md:182-184`).

### Question 3 — the `h = 1` identity (every checker's answer, unedited)
**OPUS:**
- **Committed fixture:** for block absent against a factor-1 block, under both `missing` values and both `combinator` values, every core field matches and the order matches. `raw_rank == rank` holds, and `effective_position == position` (`30…part1.md:288-301`). `CORE_FIELDS` is pinned to main's Transition fields (`:304-305`).
- **Weaker than the prompt's wording:** both sides of that test are H1 code; nothing compares against a stored main output. That the absent block equals main rests on reading the diff (the absent path only adds `raw_rank`) and on `test_radar_pool.py` staying green unchanged (`51.part2.md:65`).
- **X12:** all six days PREFLIGHT listed, 1923 scans, 0 mismatches, both at STEP-6 and again on the tip (`51.part3.md:62-71`; `52:61-69`). The run also checks `raw_rank == rank` (`part2.md:302-305`).
- **Left to the deploy:** the production stored-membership comparison. The function is proven with-DB only on rows the test inserts (`30…part1.md:406-426`), because `cobalt_dev` holds no production day. The report says so (`50:186`). This is honest.

**GROK:**
Yes on the committed real-shape scan, as absent versus factor 1 under this code, not as a second execution of main. `CORE_FIELDS` is exactly the pre-H1 set (`ticker`, `action`, `sources`, `source`, `rank`, `below_cap_streak`, `excluded_by`, `rollover`, `left_at`, `rank_metric`, `rank_value`) (`20-diff-src.part2.md:229-234`). `test_core_fields_are_exactly_the_pre_h1_transition` pins that those plus the three new fields are all of `Transition` (`30-diff-tests.part1.md:304-305`). `test_block_absent_and_factor_one_are_byte_identical_on_the_committed_scan` runs `decide` on `_scan()` (the committed screen export and `pool-metrics`) with the block absent and with factor 1, for every `missing` × `combinator`, and asserts the core tuples and their order match, `raw_rank == rank`, `effective_position == position`, and `handicap_factor == 1` (`30-diff-tests.part1.md:288-301`). The absent path does not call `shadow_rank` (`20-diff-src.part4.md:191`). Together with `_ranked` untouched, that is main's ranking on those fields.

X12's recorded output is every retained day and zero mismatches. STEP-6 (`51-build-report-steps.part3.md:63-71`): 2026-09-17 scans 306, 09-18 318, 09-21 327, 09-22 326, 09-23 327, 09-24 319; mismatches 0; summed days 6, scans 1923. CLOSE re-run matches (`52-suites.md:62-69`). `identity_mismatches` appends a mismatch when `raw_rank` is set and `raw_rank != rank` (`20-diff-src.part2.md:302-305`), and it forces the compared block's factor to 1 (`:286`). The committed-scan test asserts `raw_rank == rank` directly (`30-diff-tests.part1.md:298-299`).

Left to the deploy, and honest: the production-day comparison of the `h = 1` pass with stored `radar_membership`. `cobalt_dev` holds no production day. The with-DB proof inserts its own rows inside `migrated_radar` (`30-diff-tests.part1.md:407-426`). `## FOR THE DEPLOY` names the read-only `handicap-dry-run --day` against production membership (`50-build-report.md:186`). The command prints `stored membership: matched … mismatches …` and does not write (`20-diff-src.part2.md:497-523`).

### Question 5 — fail-soft (every checker's answer, unedited)
**OPUS:**
- **One place:** the only `try` added in the diff (`part4.md:191-202`). Its body is the header-None check, `shadow_rank(...)` and `handicap_reason = shadow.degraded`.
- **On an exception:** the pool ranks raw, and `raw_rank` is still stored (`:204-210`). The two handicap fields are NULL, not 1. `handicap` is added with `"handicap step failed: <Class>: …"`, and there is one ERROR record (test at `30…part3.md:176-198`).
- **A parse-time `ValidationError` can't reach it:** the frozen path returns before `decide()` gets there (`part4.md:88-94`; test at `30…part3.md:201-209`). The catch covers only the handicap step.
- **The reason `decide()` needs its own catch:**
  - `decide()` runs outside S1's `try` in `runner.py` — TRUE (`part4.md:439-448`).
  - The resident loop has no `except` — NOT SHOWN in this packet (it is only cited in PREFLIGHT, `50:120`). I cannot prove it from these files.

**GROK:**
One catch, only around the handicap step (`20-diff-src.part4.md:191-202`). The `try` body is: if `handicap_headers` is `None`, raise `ValueError`; else `shadow = shadow_rank(...)`; `handicap_reason = shadow.degraded`. On `Exception`: `shadow = None` (so `handicap_factor` and `handicap` stay `None`, not 1), `raw_rank` still comes from `ranks`, `ordered` / `ranks` are the raw ones, `handicap` is appended to `degraded_sources` with `handicap step failed: {class}: {error}`, and one `logger.opt(exception=error).error(...)` line is written (`:199-202`, `:293-297`). The test captures one ERROR line and `ZeroDivisionError` in the reason (`30-diff-tests.part3.md:176-198`). `decision.degraded` stays the sources' flag.

The catch cannot see a parse-time `ValidationError`. Parse is `PoolBlock` in the note reader, before `decide`. The test shows a missing `combinator` raises at `PoolBlock` and that `decide(..., None, ...)` returns frozen with `pool_block` (`30-diff-tests.part3.md:201-209`). It does not raise `ValidationError` inside the `try`. A `ValidationError` raised inside `shadow_rank` would be caught; that is inside the step.

`decide()` is called in `cycle()` before the S1 `try` (`20-diff-src.part4.md:439-448`). `resident` / `run_command` are not in the diff (not edited). The "no except around `cycle()`" half is the facts packet's claim (`12-facts-packet.md:88`), not re-shown.

### Question 7 — storage and the L76 harness (every checker's answer, unedited)
**OPUS:**
- **The migration:** additive, nullable, idempotent (`IF NOT EXISTS`), no CHECK. It sits after `0013` in `FORWARD` and before it in `REVERSE`. The rollback drops exactly the three columns (`21:16-19`, `:29-32`, `:49-55`).
- **`HandicapRecord`:** exactly ten keys, no `decisive`, `extra="forbid"` (`part3.md:682-702`; test at `30…part3.md:132-137`). It is re-validated before every write (`part3.md:15-20`).
- **Store writes:**
  - The three columns are written on INSERT, RETAIN and never-admitted EXCLUDE; a HOLD leaves them untouched (`part3.md:92-178`).
  - **Ranked LEAVEs** (stickiness evictions and the cap LEAVE) arrive with `raw_rank` and the record attached (`part4.md:239`, `:257`), but the LEAVE update writes none of them (`part3.md:122-130`). A test pins that (`30…part2.md:194-215`). This follows the precedent for `rank_metric`/`rank_value` (`40.part1.md:144`), so it is ESCALATE 1, not a defect.
- **Only inside rolled-back transactions:** the `0014` pair is applied only inside a test's own rolled-back transaction, proven by `test_forward_twice…` (`30…part2.md:261-286`), by `migrated_radar` (`30…part1.md:773-796`) and by the probe reading `=0`. `tests/cobalt/conftest.py` is not in the diff.
- **One harness:**
  - Assertions are unchanged.
  - Only `test_radar_store` swapped `dev_db_tx` for `migrated_radar` (`30…part2.md:412-414`).
  - The four `test_cards_picks` methods and `test_radar_panel` add `migrated_radar` next to a still-present `dev_db_tx` (`:33-61`, `:357-360`). Their green depends on how the two fixtures interact, which this packet doesn't show. → **defect 1**.

**GROK:**
`0014` is `ADD COLUMN IF NOT EXISTS` of `raw_rank INTEGER`, `handicap_factor NUMERIC(6,4)`, `handicap JSONB`, all nullable, no `CHECK`, no `NOT NULL` (`21-diff-migration.md:16-19`; `30-diff-tests.part2.md:163-168`). `FORWARD` places `0014` immediately after `0013`; `REVERSE` places its rollback immediately before `0013`'s (`21-diff-migration.md:49-55`). Rollback drops exactly those three, `IF EXISTS`, nothing else (`21-diff-migration.md:29-31`; `30-diff-tests.part2.md:171-174`). `placement.py` is not in the diff; the test asserts membership stays `Side.SYSTEM` and no new table (`30-diff-tests.part2.md:181-183`).

`HandicapRecord` has exactly the ten keys, `extra="forbid"`, no `decisive` (`20-diff-src.part3.md:682-702`; `30-diff-tests.part3.md:132-137`). The store re-validates with `HandicapRecord.model_validate` before `model_dump_json` (`20-diff-src.part3.md:15-20`). INSERT writes the three (`:164-176`). RETAIN and the never-admitted EXCLUDE update write them (`:94-103`, `:145-155`). HOLD's UPDATE does not (`:106-120`). LEAVE's UPDATE does not (`:122-129`). The store test pins insert, retain, and exclude write, and hold and leave do not (`30-diff-tests.part2.md:194-215`). A HOLD round-trip leaves the three as the prior RETAIN wrote them (`:295-314`).

`0014` is applied only inside a test transaction: `test_forward_twice_on_a_populated_table_then_bounded_rollback_then_reapply` rolls the connection back in `finally` (`30-diff-tests.part2.md:262-286`); `migrated_radar` applies `FORWARD` and rolls back (`30-diff-tests.part1.md:774-796`). CLOSE prints `0014_columns_on_cobalt_dev=0` (`52-suites.md:49`).

XL76 (A): the six callers are the four fill tests, `test_members_for_day_db_returns_both_open_and_left_and_scopes_pool_and_day`, and `test_membership_values_round_trip_retain_and_hold_on_cobalt_dev` (`51-build-report-steps.part1.md:129-134`). Each gained `migrated_radar`; the assertion lines are unchanged (`30-diff-tests.part2.md:33-61`, `:358-361`, `:412-415`). The store test replaced `dev_db_tx`; the pick tests and the panel test still also wear `dev_db_tx`. `tests/cobalt/conftest.py` is not in the diff. The harness is the new `tests/cobalt/radar_migrated_support.py` only.

`open_members` does not select the three columns; `members_for_day` does (`20-diff-src.part3.md:36-38`, `:63-64`; `30-diff-tests.part2.md:218-225`). The panel and the dry-run read `members_for_day`. `OpenMember` is not given the new fields.

### Question 13 — R54, the dead column (every checker's answer, unedited)
**OPUS:**
- **Definition:** as ruled. A column is dead when the header is absent (every cell parses to None) or when every ranked equity row has a blank, `-` or unparseable cell (`part3.md:525-547`).
- **Deviation:** a source with no ranked equity row is neither dead nor live (ESCALATE 1, raised by the builder).
- **On a dead scan:** every name stores factor 1, never NULL; `effective_position == position`; `handicap` is added with the header and source; each record carries the same reason; `skip` changes nothing (`part3.md:587-590`, `:617`; tests at `30…part2.md:541-587`).
- **A single blank cell on a live column** still follows `missing`, with no degraded entry (`:590-600`).
- **Kept apart from fail-soft:** no exception, no ERROR line, factor 1 (`:603-613`).
- **RED before code:** 6 of the 11 tests went RED against STEP-4's commit, for example `AssertionError: assert Decimal('0.8') == Decimal('1')`, and the `skip` case `assert 'dead column: Shares Float (screen:blanked@00000000000a)' in 'blank float and cap — unknown → not applied'` (`51.part2.md:79`). The other 5 are invariance guards that were green by construction; disclosed.
- **Panel:** shows `handicap: degraded — inoperative (dead column: …)` (`30…part1.md:174-179`).

**GROK:**
Yes. `dead_columns` marks `<header> (<source>)` when every equity row of an active healthy source that is in `ranked` has that metric `None` (`20-diff-src.part3.md:525-547`). A missing header becomes `None` for every name in `_collect` (`row.get`), and the test drops the header (`30-diff-tests.part2.md:574-576`). Blank, `-`, and unparseable are `None` via `_number`. One parseable cell leaves the column off the dead list. A source with no equity row reaching ranking is skipped (`:541-543`; `30-diff-tests.part2.md:628-639`).

On a dead column, every ranked name of the scan, including names from a live source, stores `handicap_factor` 1, not `None`; `effective_position == position == raw_rank`; `degraded_sources` contains `handicap` with `handicap inoperative — dead column: <header> (<source>)`; each row's `handicap.reason` is that same string (`20-diff-src.part3.md:587-589`, `:617`; `30-diff-tests.part2.md:541-564`). This runs before `missing` (`:575-589`). `missing: skip` does not change it (`:585-587`).

One blank cell on a live column follows `missing` and does not add `handicap` to `degraded_sources` (`30-diff-tests.part2.md:591-600`).

Inoperative is not the fail-soft path. No exception, no ERROR line, factor 1 not `None` (`30-diff-tests.part2.md:603-613`). The `try` in `decide` is not entered as a failure; `shadow.degraded` is the reason string.

RED before the code, from `51-build-report-steps.part2.md:79`, against `a7928964`: six tests. (i) both parametrized cases, (ii), (iii), and the unparseable case: `AssertionError: assert Decimal('0.8') == Decimal('1')`. (iv) `skip`: `AssertionError: assert 'dead column: Shares Float (screen:blanked@00000000000a)' in 'blank float and cap — unknown → not applied'`. Five did not go red: (v) one blank on a live column, (vi) no ERROR and factor not `None`, (vii) shadow never sorts, and the vacuous-source guard. The report says they were already green because they pin behavior STEP-4 already had. The six that change under R54 did go red, then green.

The panel header renders `handicap: degraded — inoperative (dead column: <header> (<source>))` (`20-diff-src.part1.md:137-138`, `:454-457`; `30-diff-tests.part1.md:174-179`). Rows at factor 1 get no badge (`20-diff-src.part1.md:415-422`). A row whose stored verdict is still `unknown` also gets the `unknown → not applied` line; on a wholly blank column that is every ranked row. The header carries the inoperative reason. The prompt allows that line and forbids the badge.

The other questions' answers (4, 6, 8, 9, 10, 11, 12, 14) are in `opus-check.md` and `grok-check.md`, whole, in the packet folder `scratch/tribunal-bars-0920/handicap-h1-check/`.

## Suites
From the build report itself (`/Users/cobalt/cobalt-wt/handicap-h1/docs/40 - DevDocs/reports/handicap-h1-build-2026-09-24.md`), not the packet copy:
- **Offline** — BASELINE (line 134): `2501 passed, 361 skipped, 1 xfailed, 15 warnings in 515.19s (0:08:35)`, "0 failed". CLOSE (line 548): `2619 passed, 365 skipped, 1 xfailed, 15 warnings in 506.48s (0:08:26)` — "0 failed, 0 errors". CLOSE shows `0 failed` and `0 errors`: yes.
- **With-DB** — BASELINE (line 136): `2854 passed, 6 skipped, 2 deselected, 1 xfailed, 15 warnings in 588.78s (0:09:48)`, "0 failed", deselected 2. CLOSE (line 557): `2976 passed, 6 skipped, 2 deselected, 1 xfailed, 15 warnings in 586.95s (0:09:46)`, "0 failed, 0 errors", deselected 2. Deselected count at both: 2 (`tests/cobalt/test_tenancy.py::TestMigrationRoundTrip`).
- **Table-set probe** — BASELINE (line 136): `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` "in the run, not among the skips, 0 failed → GREEN"; CLOSE (line 559): "GREEN in it: `-q` names no passing test, and no test failed or errored".
- **XL76 absence line** (line 571): `XL76: 0014_columns_on_cobalt_dev=0` (`3 passed in 0.17s`); the same block prints `XL76: callers=9`, `harness_applies=True`, `apply_ms=33`.
- **Live-note** — BASELINE (line 135): `131 passed, 15 warnings in 27.32s`; CLOSE (line 594): `131 passed, 15 warnings in 24.48s`. `SKIPPED` lines naming `COBALT_LIVE_VAULT_ROOT` in the live-note legs: none at either (expected none). `AWAITING` set at both: `AWAITING A RULING: backside` · `AWAITING A RULING: fashionably-late` · `AWAITING A DAY: hitchhiker` · `AWAITING ITS ENGINE FILL: vwap-continuation (dist.k.vwap null)` — identical.
- **`.env: removed, proven gone`** is written after every with-DB call: the `## LANE` table (lines 746–757) has nine with-DB rows (BASELINE, STEP-1 XL76, STEP-1 X5, STEP-5 files, STEP-5 suite, STEP-6 a, STEP-6 b, STEP-7, CLOSE), each with column (d) `.env: removed, proven gone (<point>)`; at the time of this check `ls /Users/cobalt/cobalt-wt/handicap-h1/.env` → `No such file or directory`.
- **LANE rows:** all nine `pass`; the first row (PREFLIGHT) `free`; no LANE STOP recorded (ESCALATE ALWAYS (x): "none").

## Checked against the branch
`<main tip>` = `f6643d41`, `<tip>` = `27df13f1`; originals under `/Users/cobalt/cobalt-wt/handicap-h1/` (Read / grep), main via `git -C /Users/cobalt/cobalt show f6643d41:<path>` (saved, then grep).

| claim | who | file:line | verdict | note |
|---|---|---|---|---|
| Five XL76 callers keep `dev_db_tx` beside `migrated_radar` (`test_cards_picks` ×4 via the class, `test_radar_panel` ×1); only `test_radar_store` replaced it | opus (defect 1), grok (noted) | `tests/cobalt/test_cards_picks.py:330` (class `usefixtures("dev_db_tx","pick_pool")`), `:332,343,353,363`; `test_radar_panel.py:1223,1225`; `test_radar_store.py:166` | HOLDS | The stacking is as stated. The with-DB suite ran GREEN in this state (2976/0); that the stacking is harmless or harmful is NOT CHECKABLE FROM READS — settled by the deploy's with-DB run. |
| `_cut_tier`'s docstring says "the rule X2 tallies" but implements a different order | opus (defect 2) | `src/cobalt/radar/handicap_dry_run.py:335-337` vs `tests/experiments/handicap_h1/test_h1_x2_marginal_seat.py` `_tier` | HOLDS | `_cut_tier`: seats → stickiness, then held, priority, first_from/position, per cut; X2 `_tier`: held first, one tier per scan, first match wins. |
| Ranked LEAVEs write none of the three columns; the departed row keeps the previous scan's record | opus (ESCALATE 1), grok | branch `radar/store.py` LEAVE update (unchanged); packet `20-diff-src.part3.md:122-130`; store test `30-diff-tests.part2.md:194-215` | HOLDS | Code path as stated; the test pins it. |
| The panel renders a stale badge on departed rows | opus | `src/cobalt/aset/radar_panel.py:590` (`_row(item, "departed", …)`), `:877` `_handicap_cell` — no category guard | HOLDS | By reading: `_handicap_cell` keys on `row.handicap_factor < 1`, not on category. What a departed row shows at run time: NOT CHECKABLE FROM READS. |
| The resident loop has no `except` | opus ("NOT SHOWN"), grok ("facts packet's claim, not re-shown") | branch `radar/runner.py:461-472` (`run_command` → `resident()`: `while … result = await runner.cycle()`, no `try`) | HOLDS | Verified in the file; the packet did not carry it. |
| `decide()` runs outside S1's `try` | opus, grok | branch `radar/runner.py:190` (`decision = decide(`), S1 `try` after it | HOLDS | — |
| One `try` added in `decide()`; main has none in `pool.py` | opus, grok, builder | branch `pool.py:358`; main `f6643d41:pool.py` `grep -c "try:"` = 0 | HOLDS | Exactly one new `try:` in `pool.py`. |
| `_ranked` / `_metric_position` untouched | all | branch `pool.py:109` / `:124` (shifted +15 by earlier hunks); packet `20-diff-src.part4.md:62` hunk `@@ -215,191 +230,236 @@ def _ranked(` starts at main `:215` = `def decide(` | HOLDS | Main: `_metric_position` :94, `_ranked` :109-212; no hunk in either. |
| Other `decide(` callers without `handicap_headers` (possible `radar/replay.py`) | opus (ESCALATE 2) | `grep -rn "decide(" src/cobalt`: `radar/runner.py:190`, `radar/handicap_dry_run.py:256` (both pass `handicap_headers`); `daymode/*` is another `decide` | DOES NOT HOLD | No other caller of `pool.decide` exists in `src/cobalt`. |
| v3 §3 "not replayable from bars" line is not built | opus, grok | `grep -rn "not replayable" src/cobalt` → empty | HOLDS | Not in v3 §9's H1 row (grok); v3 §3 states it. |
| The facts packet's "in `pool_unit`" wording covers only inputs | opus (ESCALATE 3) | `radar/runner.py:319-323` (main): `pool_block` + `source_sets` dumps | HOLDS | `pool_unit` = pool block + source sets (metrics); the factor is on the row. |
| v3's L52 (c) paragraph still says OPEN FOR DEJAN | grok | `11-design-v3.part2.md` (`## L52`, row (c)): "NOT MET until he answers R2-1" | HOLDS | Text as the branch left it (STEP-0 edits did not touch that row: the STEP-0 diff, `40-diff-docs.part2.md`, has no hunk there). |
| The identity test is H1 vs H1, not a second execution of main | opus, grok | `tests/cobalt/test_radar_handicap_dry_run.py::test_block_absent_and_factor_one_…` | HOLDS | Both sides call `decide()` on branch code. The retained-day identity is also branch-vs-branch. The stored-membership comparison is the deploy's. |
| On a dead column each row shows the `unknown → not applied` line where the verdict is `unknown` | grok | `radar_panel.py:877` `_handicap_cell` (verdict `unknown` at factor 1 renders the line) | HOLDS | By reading only. |

**Facts-packet `file:line` claims (`12-facts-packet.md`), read on main `f6643d41`:**

| cite (packet) | main line now | verdict |
|---|---|---|
| `pool.py:326` re-sort point | `:326` `ordered, ranks, source_for, values = _ranked(…)` | HOLDS |
| `pool.py:208` `source_for[ticker]` | `:208` | HOLDS |
| `pool.py:332-333` seats / winners | `:332-333` | HOLDS |
| `pool.py:94-106`, `:109-…` `_metric_position`, `_ranked` | `:94`, `:109` | HOLDS |
| `runner.py:186` `decide(` call | `:186` | HOLDS |
| `runner.py:189-206` S1 `try` | S1 comment `:190` | DOES NOT HOLD at the cited line (off by one; builder re-located to 190–207; HOLDS there) |
| `runner.py:245` frozen poll hand-off | `:245` | HOLDS |
| `runner.py:319-323` `pool_unit` | `:319`, `:322` | HOLDS |
| `runner.py:391-398` `_number` | `:391` | HOLDS |
| `runner.py:453-460` resident | `resident` at `:454`, `cycle()` at `:458` | DOES NOT HOLD at the cited start (off by one; builder re-located to 453–464) |
| `evaluate.py:143-152` `FORMULA_FILES` | `:174` comment, `:175` tuple | DOES NOT HOLD at the cited line (drift; builder re-located to 175; HOLDS there) |
| `evaluate.py:155-158`, `:161-166` `canonical_sha256` / hash | `:187` | DOES NOT HOLD at the cited line (builder re-located to 187) |
| `notes.py:108` `PoolBlock(**raw)` | `:108` | HOLDS |
| `notes.py:64-65` `frozen` | `:64-65` | HOLDS |
| `notes.py:408-415` `pool_error` | `:412`, `:415` | HOLDS |
| `models.py:99-100` `PoolBlock` `extra="forbid"` | `:99-100` | HOLDS |
| `poller.py:84` | `:84` `sorted(members, key=lambda item: (item.rank, item.ticker))` | HOLDS |
| `radar_panel.py:586-588` degraded joiner | `:588` | HOLDS |
| `radar_panel.py:542-545` pool-row sort | `:545` | HOLDS |

The packet's cites were taken on `d2d82e7`; at the builder's re-located lines (`50-build-report.md`, `27 cite → main line`) every one holds. No cited symbol vanished.

**Stated checks (i)–(xi):**
- **(i) boundary.** `git log --stat --oneline f6643d41..27df13f1` (17 src/config, 35 test, 16 docs touches). Paths not named in `43`'s STEP `Files:` lines: `src/cobalt/radar/runner.py` in STEP-4 (the `decide()` call passes `handicap_headers`; `_pool_row` writes `Decision.reasons`) and `src/cobalt/db_migrations/cli.py` in STEP-5 (`TABLE_DIGEST_EXCLUDED_COLUMNS`) — both named by the builder in ESCALATE 3; A1 test re-points beyond the two `43` names for STEP-5: `test_p4_migrations.py`, `test_radar_migration.py`, `test_radar_score_migration.py`, `test_tenancy.py` (registry pins; builder's A1 table, `51.part3`), `test_radar_panel.py` / `test_cards_picks.py` / `test_radar_store.py` (XL76 callers, named in `43`); STEP-7's `test_radar_panel.py` re-points; the DevDocs under `docs/40 - DevDocs/cobalt/`; the CLOSE `test_xl76_membership_harness.py` edit. `tests/cobalt/conftest.py` and `src/cobalt/db_migrations/placement.py` do NOT appear.
- **(ii)** `git log --oneline f6643d41..27df13f1 -- src/cobalt/radar/evaluate.py src/cobalt/cards src/cobalt/replay src/cobalt/radar/poller.py src/cobalt/aset/web.py src/cobalt/settings tests/cobalt/test_radar_panel_cards.py tests/cobalt/conftest.py src/cobalt/db_migrations/placement.py` → EMPTY.
- **(iii)** `grep -n "def _metric_position\|def _ranked"` on the branch `pool.py` → `:109`, `:124`; the source diff's hunk headers (`-9,10` / `-39,20` / `-64,9` / `-215,191` (label `_ranked`, body starts at `def decide(`) …): no hunk inside either function.
- **(iv)** `grep -rn "try:"` branch `pool.py` → one, `:358`; main's `pool.py` → 0. Exactly ONE new.
- **(v)** `grep -rn "decisive" src/cobalt` → ONE hit, `radar/handicap.py:119`, a docstring line (`exactly v3's ten keys. \`decisive\` is H2's and is NOT a key here.`). Not EMPTY as the prompt expected: the hit is a comment, no code.
- **(vi) L32, numbers.** Read the `| R28 |` row (`cto-2026-09-21.md:39`): two threshold values. `R28 value 1`: 0 hits — added lines of every `20-diff-src` part (covers `src/cobalt/radar`, `configs/cobalt/radar.yaml`) and every `30-diff-tests` part (covers `tests/experiments/handicap_h1/` and each new test file). `R28 value 2`: 0 hits in `20-diff-src`; 5 matching lines in `30-diff-tests.part3.md` (523, 524, 528, 529, 530) — the redacted real-shape fixture `tests/fixtures/radar/screen-handicap.real-shape.csv` (header line's `50-Day…` column labels and export data cells copied from a retained export); not in a test/code assertion. Judged by the desk, not me.
- **(vii)** In the test diffs every `-` line that removes an `assert` has a `+` replacement in the same hunk (`30-diff-tests.part1.md:209`→`:210-212`; `:805`,`:819`,`:843-844` and `part2.md:9-10`, `:338`, `:380`, `:386`, `:392`, `:426`: registry pins re-pointed, each replaced by an `assert` of equal or greater extent). `+` lines matching `skip|xfail`: 18, all either `missing: skip` (a value of the key), `pytest.mark.skipif` / `pytest.skip` on this build's own with-DB modules (`radar_migrated_support.py`, the experiment `requires_db`), or the word "skipped" in a docstring/print — no `xfail`, no skip on an existing test.
- **(viii)** `## FOR THE DEPLOY` (build report lines 729–738): `ROLLBACK, IN THIS ORDER (L65): (1) the desk removes the handicap: block from his note FIRST, parser proof; (2) the code revert (L54 / L68); (3) 0014's rollback; (4) residents inside the pause (L43 / L66).` — precedes the code revert and the migration rollback.
- **(ix) R54.** `grep -n "inoperative"` on `handicap.py`, `pool.py`, `radar_panel.py`: `handicap.py` (`INOPERATIVE = "handicap inoperative — "`, `dead_columns`, `inoperative_reason`), `radar_panel.py` (`INOPERATIVE` import, `_handicap_state`). `dead_columns` (`handicap.py:88-…`): a column is dead only if `all(row.get(key) is None for row in rows)` over the ranked equity rows of a healthy active source — one parseable cell makes it live; a source with no ranked equity row is skipped (`if not rows: continue`). The factor-1 result sits inside `shadow_rank` (`handicap.py`), called from the ONE `try` of (iv) but raising nothing: it is NOT a second `try` and not an exception path.
- **(x)** `grep -n "00[0-9][0-9]_" src/cobalt/db_migrations/__init__.py`: `FORWARD` `:91` `0013`, `:92` `0014`; `REVERSE` `:97` `0014_…rollback`, `:98` `0013_…rollback` — `0014` directly after `0013` in `FORWARD` and directly before `0013`'s rollback in `REVERSE`.
- **(xi) L76.** `grep -rn "db migrate"` in the build report: 3 hits, all sentences ABOUT the rule (line 50: the removed allow string is absent; line 733: `cobalt db migrate --allow-prod` "is the deploy hub's (L61)"; line 765: the digest exclusion "would … roll the production migrate back"), none a command the build ran. Harness: `tests/cobalt/radar_migrated_support.py:77` `db.connect_migration`, `:81` `_apply(conn, FORWARD)`, `:93` `conn.rollback()` in `finally`; `test_radar_handicap_store.py:139` `db.connect_migration`, `:170-187` `_apply(conn, …)`, `:190` `conn.rollback()`. `grep -rln "migrated_radar" tests/cobalt` → `radar_migrated_support.py`, `test_radar_handicap_store.py`, `test_radar_panel.py`, `test_radar_handicap_dry_run.py`, `test_radar_store.py`, `test_cards_picks.py`: the six XL76-listed callers (cards_picks ×4, radar_panel, radar_store) all moved, none missing; the two new files also use it.

Where the checkers contradict: none. Differences of emphasis — Opus: `CHECK: FIX` on two items; Grok: `CHECK: BUILD STANDS`, with the same stacking noted ("the pick tests and the panel test still also wear `dev_db_tx`") and not raised as a defect.

## Ready for a deploy
| checker | CHECK line | ready |
|---|---|---|
| Opus 5.5 | `CHECK: FIX — 1) remove dev_db_tx from the five XL76 callers that now also use migrated_radar (test_cards_picks ×4 via the class, and test_radar_panel::test_members_for_day_db…), or prove the two fixtures are ordered correctly, so every membership test runs on ONE harness as the prompt and report state; 2) correct _cut_tier's docstring claim ("the rule X2 tallies") and the render comment, or align the rule with X2's, so the dry-run's tier tally is not presented as X2's` | NO — the two items above |
| Grok | `CHECK: BUILD STANDS` | YES |
| Sol | not seated (METER, retry after Sep 26th, 2026 6:47 AM) | — |

## FOR THE CLASSIFIER
| claim | who | file:line | my HOLDS row |
|---|---|---|---|
| Five XL76 callers keep `dev_db_tx` beside `migrated_radar` (prompt and report say "moved") | opus (defect 1) | `tests/cobalt/test_cards_picks.py:330,332,343,353,363`; `tests/cobalt/test_radar_panel.py:1223,1225` | HOLDS (the stacking); harm NOT CHECKABLE FROM READS — with-DB suite ran green in this state |
| `_cut_tier`'s docstring ("the rule X2 tallies") does not describe its rule; the `render` comment repeats the X2 claim | opus (defect 2) | `src/cobalt/radar/handicap_dry_run.py:335-337`; `render` comment; `tests/experiments/handicap_h1/test_h1_x2_marginal_seat.py` `_tier` | HOLDS |

## ESCALATE
1. **Opus `CHECK: FIX`** (two items, `## FOR THE CLASSIFIER`); Grok `CHECK: BUILD STANDS`. Defects that HOLD in my file-check: 2. No weaker assertion that HOLDS (vii). No path where the factor or the would-be rank reaches an order or a card number that HOLDS (L7): both checkers and (ii), (iii), (iv) agree. No owner value in a committed line that HOLDS as an assertion; `R28 value 2` has 5 matching lines in the fixture CSV (data / column-label cells, `## Checked against the branch (vi)`) — the desk judges.
2. **Experiments carried as-is.** NOT AS EXPECTED (builder): X6 (only the name rendered → built at STEP-7) and X10 (cap cells differ across sources in 14,612 of 37,368 pairs → verdict follows `source_for`, the row stores `source`): Opus and Grok both read neither as a §4 stop. Builder marked none UNPROVEN; Opus reads two partial results as UNPROVEN: X4's load path under H1 (`pool_error` text not printed; the builder puts it down to the harness's `finviz_max_rpm=None`, main `notes.py:421` "radar.finviz_max_rpm is unmeasured") and X5's stored half (0 receipts on `cobalt_dev`, nothing to check).
3. **XL76's decision:** (A) — one fixture `migrated_radar` in the new `tests/cobalt/radar_migrated_support.py`, `tests/cobalt/conftest.py` untouched; six callers moved; `0014_columns_on_cobalt_dev=0` at CLOSE. Carried as-is; the `dev_db_tx` stacking is defect 1.
4. **The deploy's own acceptance carried as-is:** the production dry-run `cobalt radar handicap-dry-run --day <retained day>` against production `radar_membership` (0 mismatches) and the read-only parser proof after the block is written; the build ran neither.
5. **The builder's four ASK DESK items** (1 vacuous dead column · 2 X11 latch · 8 how loud a handicap-only degradation is · 11 healthy pins vs "not configured, shown") — carried; the desk's records in R89 (cto-2026-09-24) stand; both checkers carry them as raised, neither holds them as a defect.
6. **Opus's ESCALATE 1 (ranked LEAVEs store no record; the departed row keeps the previous scan's record and the panel can render it):** the claim HOLDS in my file-check. Carried as Opus's question to the desk: keep the `rank_metric` precedent, or write / clear the three columns on ranked LEAVEs.
7. **Opus's ESCALATE 2 (other `decide(` callers without `handicap_headers`):** DOES NOT HOLD in `src/cobalt` — only `runner.py:190` and `handicap_dry_run.py:256`, both pass it. Opus's related item — v3 §3's "replay-from-bars reports `handicap: not replayable from bars`" is not built — HOLDS (no such string in `src`); v3 §9's H1 row does not list it.
8. **Packet-gap notes:** (a) the "resident loop has no `except`" half of question 5 was not in the packet; verified by me in `runner.py:461-472`. (b) `12-facts-packet.md`'s `file:line` cites drift on main `f6643d41` at four lines (`runner.py:189-206`, `:453-460`, `evaluate.py:143-152`, `:155-158`/`:161-166`); at the builder's re-located lines every cite holds. None DOES NOT HOLD at its re-located line.
9. **Grok's note on v3's own L52 (c) paragraph** ("NOT MET until he answers R2-1") still stands in the file the branch shipped, beside the status table that says RULED B — a stale sentence, not a second seam.
10. **Both checkers' limit on the identity / shadow tests:** they compare H1-absent with H1-present on branch code; main is not executed (the retained-day identity is likewise branch vs branch). The deploy's production dry-run is the comparison with stored membership.
11. **LANE STOPs recorded by the build:** none. **Live-note:** identical to R56's known state at baseline and close. **`cobalt_dev: UNPROVEN`:** not in the stop line (it reads `cobalt_dev: 0013`). **Packet mismatch:** none (two typing slips, caught by `wc -c` / the line-set check, fixed before launch). **A checker that did not check:** none. **ASK DESK from this run:** none.
12. **L74:** one block arrived — see `## L74`.
13. **Sol:** `METER — retry after Sep 26th, 2026 6:47 AM` (54's probe); not probed (`date` 2026-09-24 21:07 ET). Gemini not seated (R96/R97); Astra not seated (R46).
14. **Standing line:** Round 1 covers the H1 build (`f6643d41..27df13f1`) and its three suites' executed output, checked by Opus 5.5 + Grok (+ Sol when seated) under his R95 (Gemini out, R96/R97). With every seated house `CHECK: BUILD STANDS` and `defects that HOLD: 0`, the build is checked (L67) and the desk drafts its deploy prompt; a HOLD goes to a fix round (L75) and round 2 (L39); the deploy's L68 gate re-proves offline, with-DB (running `TestMigrationRoundTrip`, which this build deselected under L76) and live-note on the tree that ships.

HANDICAP H1 CHECK DONE · round: 1 · opus: CHECK: FIX — 1) remove dev_db_tx from the five XL76 callers that now also use migrated_radar … or prove the two fixtures are ordered correctly; 2) correct _cut_tier's docstring claim ("the rule X2 tallies") and the render comment, or align the rule with X2's · grok: CHECK: BUILD STANDS · sol: NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM) · gemini: NOT SEATED (R96/R97) · defects that HOLD: 2 · ready for a deploy prompt: 1 of 2 · ESCALATE: 14
