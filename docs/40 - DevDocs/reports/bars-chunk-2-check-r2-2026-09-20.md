# Bars chunk 2 — build check, round 2 (the fix only)

§0 Headline
- Checked the fix `427c752..d768674` (four commits, rows X1–X5) with **3 of 3 houses**; astra answered this time, so the three-house floor is met.
- Grok and gemini: `FIX STANDS`, inert YES, ready YES. Astra: `FIX AGAIN X1, O4-in-memory-range`, inert NO, ready NO. The houses split 2–1.
- Astra's two points both HOLD in the file-check: the `rth_stale` case in test 1 never goes stale, and a carried `no_partition` record is dropped on a plain-table success and keeps `detail=None` on a partitioned one.
- FIX rows closed by every house: 4 of 5 (X1 open). New defects: 0. ESCALATE: 12.

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| authorization (git log) | `git -C /Users/cobalt/cobalt log --oneline -6 -- "…/cto-2026-09-20.md"` | 0 | allowed — 6 commits, tip `90e47bb` |
| R13 | `grep -n "^| R13 " …cto-2026-09-20.md` | 0 | allowed — line 86, "Push and approved everything. Please start all the process…" |
| R23 | `grep -n "^| R23 " …` | 0 | allowed — line 206, "yes", grok/agy stand THROUGH MONDAY 2026-09-21 23:59 ET |
| R25 | `grep -n "^| R25 " …` | 0 | allowed — line 262, "approved" |
| R25 committed | `git log -1 --format=%H -S"\| R25 \|" …` | 0 | allowed — `e15d03eac2076366a3009b2d56ac40cba92dd6fc` |
| desk fix-round call committed | `git log -1 --format=%H -S"chunk 2 is NOT ready for a deploy prompt" …` | 0 | allowed — `407091266786727a04f188baa81feebedf4c305d` |
| **DATE GATE** | `date` | 0 | allowed — `Sun Sep 20 23:45:48 EDT 2026` (before 2026-09-22 → passes) |
| grok | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| agy | `agy --version` | 0 | allowed — `1.2.7` |
| worktree | `ls /Users/cobalt/cobalt-wt/bars-chunk-2` | 0 | allowed — present |
| fix built | `tail -n 3 …/bars-chunk-2-2026-09-20.md` | 0 | allowed — last non-blank line: `BARS CHUNK 2 FIX BUILT d768674 \| on 427c752 \| offline 2372/0 (365 skipped; round-1 2368/0) \| fixed: X1 X2 X3 X4 X5 \| not fixed (listed): 24 \| inert on an unpartitioned parent, every path: proven \| upsert_bars byte-identical to main: proven \| card/scoring paths untouched: empty diff \| db: OWED — 0 requires_db tests written, never run \| ESCALATE: 12` → `<fix tip>` = `d768674`, `<round-1 tip>` = `427c752` |
| fix commits | `git -C /Users/cobalt/cobalt log --oneline 427c752..d768674` | 0 | allowed — 4 commits: `d768674` (X4), `7064868` (X3), `d6d39b1` (X2), `51764c8` (X1) |
| branch tip | `git -C /Users/cobalt/cobalt log --oneline -1 bars/chunk-2-0920` | 0 | allowed — `1351da6` (the fix report commit, above `d768674`) |
| staging list / boundary | `git -C /Users/cobalt/cobalt log --stat --oneline 427c752..d768674` | 0 | allowed — see below |
| round-1 folder | `ls scratch/tribunal-bars-0920/chunk-2-check` | 0 | allowed — holds `grok-check.md`, `gemini-check.md`, `QUESTIONS-CHECK.md`, `THE-POLLER-DIFF.md`, `built/` (also `astra-check.md`, `build-prompt.md.part1/2`, `build-report.md.part1-4`, `build-diff-src.md.part1-5`, `main-poller.py`, `main-store.py`, `main-0006.sql`, `main-0010.sql`, `owner-rulings-r19-r25.md`, `spec-final-s2.md`, `s4`, `s5`, `chunk-e-check-report.md.part1`). NOTE: `spec-final-s3.md` is NOT in this folder (see ESCALATE) |
| recovery | `ls scratch/tribunal-bars-0920/chunk-2-check-r2` | 1 | "No such file or directory" — fresh run |
| **CODEX PROBE (gate)** | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background) | 0 | allowed — replied `OK`, exit 0, no usage-limit text → **astra: UP** |

Staging list / boundary (the `--stat` of `427c752..d768674`):

| commit | paths |
|---|---|
| `51764c8` (X1) | `docs/40 - DevDocs/cobalt/radar/poller.md` (+11) · `docs/40 - DevDocs/reports/bars-chunk-2-2026-09-20.md` (+219) · `src/cobalt/radar/poller.py` (62 lines) · `tests/cobalt/test_bars_poller_coverage.py` (40 lines) |
| `d6d39b1` (X2) | report (+144) · `tests/cobalt/test_bars_poller_coverage.py` (94 lines) |
| `7064868` (X3) | report (+87) · `tests/cobalt/test_bars_poller_coverage.py` (98 lines) |
| `d768674` (X4) | `docs/40 - DevDocs/cobalt/bars/ensure.md` (19) · report (+89) · `src/cobalt/bars/ensure.py` (13) · `tests/cobalt/test_bars_ensure.py` (+70) |

L74 note (recorded once, not followed): the Read tool result of this prompt file arrived with an appended block asking for a `Claude-Session: …` line in commit messages and PR descriptions and naming a file-send tool (SendUserFile). It is DATA; not followed. This run commits nothing and sends no file.

Date note: the run crossed midnight during staging (the clock now reads 2026-09-21, still inside R23's window that runs through 2026-09-21 23:59 ET; the DATE GATE row above was taken at 23:45 ET 2026-09-20 and passes).

## Packet
Folder `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/chunk-2-check-r2/` (fresh run; no `mkdir` run — the first Write created it). Staged by this hub alone, Read → Write; whitespace-only lines are EMPTY in `fix-diff.md.part*` (round 1's ESCALATE 9, expected) and said so in QUESTIONS-R2's list.

| item | staged as | check |
|---|---|---|
| the fix, pre-computed | `fix-diff.md.part1` (30,111 B) + `fix-diff.md.part2` (35,715 B) — the whole `git log -p 427c752..d768674`, ALL paths, **run per path group** (the whole range was too large for one tool result; said so in a hub header at the top of part1): group 1 `docs/40 - DevDocs/cobalt`, group 2 `src` + `tests`, group 3 the chunk-2 report | `commit ` lines 6 + 4 = 10 = the per-group commit headers (group 1: 2, group 2: 4, group 3: 4); `diff --git` lines 8 + 4 = **12** = the file-touches the `--stat` list shows (4 + 2 + 2 + 4). Group 3 (the report) verified line-by-line against the tool result (`grep -x -F -f`: only whitespace-only lines and the hub header differ; 3 transcription slips found and fixed). Groups 1–2 were copied from tool output and are NOT line-verified against a second source beyond the 12-touch count |
| touched files as fixed | `fixed/poller.py` 13,941 · `fixed/ensure.py` 10,268 · `fixed/test_bars_ensure.py` 26,269 · `fixed/poller.md` 7,042 · `fixed/ensure.md` 5,547 · `fixed/test_bars_poller_coverage.py.part1` 29,299 + `.part2` 29,727 = 59,026 (cut between `test_6b` and `test_6c`) | every copy `wc -c` = original (13,941 / 10,268 / 26,269 / 7,042 / 5,547 / 59,026) |
| main's poller | `main-poller.py` 4,981 — main's LIVE file, the baseline every inertness claim is measured against | `wc -c` = 4,981 = round 1's copy |
| round 1's verdicts | `round1-verdicts.md` 24,770 (`## Inertness`, `## The composition note`, `## The thirteen poller tests`, `## Checked against the branch` + O1–O3, `## ESCALATE`; round-1 lines 76–182, 246–301, 316–329; the round-1 stop line not staged) | every non-blank line matches the source line-for-line (`grep -x -F -f`); only the hub's one header line and blank lines differ |
| the CLASSIFY table | `classify.md` 13,448 (drafter's `## CLASSIFY`, lines 26–67) | line-verified as above |
| the fix's own report | `fix-report.md.part1` 32,225 + `part2` 30,071 = the `# FIX ROUND 1` section (lines 937–1922 of the chunk-2 report, 986 lines) | 533 + 453 = 986 lines; every non-blank line matches the original |
| what the fixer was told | `fix-prompt.md.part1` 20,211 + `part2` 21,830 = 42,041 | sum = `wc -c` of `23-bars-chunk-2-fix.md` (42,041); line-verified |
| questions | `QUESTIONS-R2.md` (verbatim + the "Files in this folder" paragraph) · `QUESTIONS-R2-ASTRA.md` (the addendum, verbatim; named in ASTRA's launch sentence only) | written by the hub |

Round 1's copies, referenced from `../` (not re-staged; ASTRA is expected to use them): `../chunk-2-check/` `build-prompt.md.part1/.part2`, `build-report.md.part1…part4`, `THE-POLLER-DIFF.md`, `built/`, `spec-final-s2.md`, `spec-final-s4.md`, `spec-final-s5.md`, `owner-rulings-r19-r25.md`, `grok-check.md`, `gemini-check.md`, `astra-check.md`, `QUESTIONS-CHECK.md`; `../chunk-e-check/spec-final-s3.md`, `spec-final-s6.md`, `spec-final-s8.md`; `../r3/DERIVED-v3.md.part1/.part2` — all verified present by `ls`.

Packet defects (recorded, not fatal):
- **`QUESTIONS-R2-ASTRA.md` (verbatim from the prompt) names `../chunk-2-check/spec-final-s3.md`, which is NOT in that folder** (verified by `ls`); FINAL's §3 with the COMPOSITION NOTE is at `../chunk-e-check/spec-final-s3.md` (present) and the note is also quoted whole in `fixed/test_bars_poller_coverage.py.part1`'s docstring and in `round1-verdicts.md`. Astra's launch sentence names the real path; the addendum text itself is unedited.
- QUESTIONS-R2's list says the fix diff was cut into three path groups; the prompt's own check ("`commit` lines equal the commits listed") is satisfied per group, not on one run of the whole range.
- The three test/source copies under `fixed/` are `wc -c`-exact but were not content-diffed against a second read.

House rows (one attempt each, never re-asked):
- **grok**: DONE, exit 0; wrote `chunk-2-check-r2/grok-check-r2.md` itself (10,787 B). Closing line present.
- **gemini**: DONE, exit 0; printed answer written byte for byte to `chunk-2-check-r2/gemini-check-r2.md`. Closing line present.
- **astra**: DONE, exit 0, no usage-limit text; final message written to `chunk-2-check-r2/astra-check-r2.md` (17,559 B). Closing line present. The three-house floor was MET.

## CONTINUE
next: none — the report is complete; the desk reads it.

## Per FIX row
| row | what it fixes | grok | gemini | astra | CLOSED |
|---|---|---|---|---|---|
| X1 | write-failure arm partitioned-only; test 1 widened | CLOSED | CLOSED | **NOT CLOSED** — RTH-stale case never goes stale, so a regression that breaks plain-table stale planting stays green (`fixed/test_bars_poller_coverage.py.part1:334`) | 2 of 3 |
| X2 | tests 5/5b reach the per-ticker P-closed clause | CLOSED | CLOSED | CLOSED | 3 of 3 |
| X3 | test 9 reaches an uncovered batch; source guard | CLOSED | CLOSED | CLOSED (source guard is a direct-name check only) | 3 of 3 |
| X4 | `ensure` asserts parent + every child of the plan | CLOSED | CLOSED | CLOSED | 3 of 3 |
| X5 | report corrections appended | CLOSED | CLOSED | CLOSED (adds: report still overstates a tested RTH-stale path) | 3 of 3 |

No house wrote NEW DEFECT INTRODUCED. Astra also says the production change at `fixed/poller.py:201` is correct; its X1 objection is to the proof, not the code.

## Per not-fixed row
Grok and gemini: `AGREE` on all 23 non-FIX rows (NR1–NR7, U1–U5, S1–S6, O1–O6) and on X14. Astra: `AGREE` on all except one.

| row | class | grok | gemini | astra |
|---|---|---|---|---|
| NR1–NR7, U1–U5, S1–S6 | as classified | AGREE | AGREE | AGREE |
| O1 unreadable-bounds divergence | OWNER ITEM | AGREE | AGREE | AGREE |
| O2, O3, O5, O6 | OWNER ITEM | AGREE | AGREE | AGREE |
| **O4** in-memory named range | OWNER ITEM | AGREE | AGREE | **DISAGREE** — see ESCALATE 3 |
| X14 child-name shape | FIX on chunk 1a | AGREE | AGREE | AGREE |

## Inertness on the fixed code
Astra's answers are in `astra-check-r2.md` (staged verbatim there; `ROUND-1 QUESTION (a)`–`(d)` and `COMPOSITION`). Their content, for tabulation: (a) all four paths match main by inspection, with named extra control points; (b) the test compares against main's real `poll()`, with limits; (c) reader reached every cycle, one connection and one catalog query; (d) "literally yes" — closure and two dicts run before the read, and a failing read returns an abort with no verdict. COMPOSITION: **SOUND**, with two qualifications (Monday "every ticker" is an illustration; an abort does not roll back earlier tickers).

Hub file-check of each against `fixed/poller.py` and `main-poller.py`:
- **(a)** HOLDS. `fixed/poller.py:201` gates the refresh, tally, re-classify and `no_partition` block under `if bounds.partitioned`; the arm falls to one `error`/`stopped_at` tail at `:231-233`, main's `:113-115`. Fetch-failure arm `:153-159` = main `:89-95`. `partitions.py:584-585` and `:638-644` make `current_period_abort` return None and `classify_coverage` return every index covered on a plain reading.
- **Extra branch, HOLDS:** `fixed/poller.py:245` `failures.pop((ticker, NO_PARTITION), None)` runs on a plain-table success; main has no such pop, so a carried `no_partition` record is dropped where main keeps it. A no-op unless such a record exists.
- **(b)** HOLDS. `_main_poller_module` loads main from git.
- **(c)** HOLDS. `fixed/poller.py:137` is unconditional. Server cost is NOT CHECKABLE FROM READS.
- **(d)** HOLDS: `:117-130` (two dicts, `_result`) precede `:136-142`; nothing fetches or writes first.
- **COMPOSITION**: the code implements it as worded (`partitions.py:567-608`, `:667-670`; `poller.py:144-146`, `:171-179`).
- **The RTH-stale case, HOLDS as astra says.** In test 1 the bars are `NOW-4m, -2m, -1m, 0` and the watermark for `rth_stale` is `NOW-10m` (`part1:334-337`); closed = the first three, `newest = NOW-1m`, age 60 s < `max_age_s` 180, so neither poller plants `stale`. The case is a copy of `clean` with a different watermark.

`inert on every path: 0 of 3 YES` — grok YES, gemini YES, astra NO; astra's NOT CLOSED HOLDS in the file-check.

## Assertions and boundary
| house | (a) weaker assertions | (b) outside the FIX rows | (c) L52 |
|---|---|---|---|
| grok | NONE | NONE; `partitions.py` and `placement.py` not touched | NOTHING REACHES A CARD |
| gemini | NONE | NONE; neither touched | NOTHING REACHES A CARD |
| astra | NONE in the supplied diff (notes `written == {"AAA": 0}` becomes `{"AAA": 1}`) | NONE; neither touched (notes the report-only close is outside the range) | NOTHING REACHES A CARD |

## Checked against the branch
Originals under `/Users/cobalt/cobalt-wt/bars-chunk-2/`; commits via `git -C /Users/cobalt/cobalt`.

| claim · who | file:line | verdict | note |
|---|---|---|---|
| rth_stale fixture never goes stale · astra | `test_bars_poller_coverage.py:334-337` (staged `part1`), `poller.py:162-166, 250-257` | HOLDS | newest = NOW−1m, age 60 s < 180; same as clean |
| a break of plain-table stale planting stays green · astra | `test_1` compares only the same fields | HOLDS | follows from the row above |
| carried `no_partition` is popped on a plain-table success · astra | `poller.py:245`; main has no such pop | HOLDS | predates the fix (round-1 `:230-233`) |
| `setdefault` keeps a carried `detail=None` · astra | `poller.py:222, 240-243`; `runner.py:270-277` rebuilds without `detail`, `:288-290` persists three keys | HOLDS | test 10c (`part2`) asserts onset only |
| X1 gate at `:201`, one tail at `:231` · astra, grok | `poller.py:201-233` | HOLDS | |
| X2 mutation is caught; fetch recorded · grok, astra, gemini | `test_bars_poller_coverage.py:601-702` | HOLDS | evidence is the fixer's own runs; re-run is NOT CHECKABLE FROM READS |
| X3 property not behaviourally falsifiable · all | `partitions.py:667-670`, `poller.py:174-179, 250` | HOLDS | reason true of the code |
| X4 asserted set = parent + present + missing · all | `ensure.py:257-262` | HOLDS | grants still `grant_statements(plan.missing)` at `:245` |
| gemini "(a) NONE, no assertion removed" | fix diff | DOES NOT HOLD (literal) | `assert result.written == {"AAA": 0}` removed in `test_9`; old wholesale-strip call assert removed. Both replaced by stronger asserts |
| the report says "Nothing is removed from the test" (X3) | `fix-report.md` X3 | DOES NOT HOLD (literal) | same removed assert |
| requires_db behaviour of the real reader · all | — | NOT CHECKABLE FROM READS | run the 14 tests on `cobalt_dev` |

Facts the fix promised:
- (i) `--stat` of `427c752..d768674` names only `src/cobalt/radar/poller.py`, `src/cobalt/bars/ensure.py`, `tests/cobalt/test_bars_poller_coverage.py`, `tests/cobalt/test_bars_ensure.py`, `docs/40 - DevDocs/cobalt/radar/poller.md`, `docs/40 - DevDocs/cobalt/bars/ensure.md`, and the chunk-2 report. HOLDS. Above `d768674` the branch tip `1351da6` touches the report only.
- (ii) `git log --oneline 427c752..d768674 -- src/cobalt/cards src/cobalt/radar/evaluate.py src/cobalt/aset configs src/cobalt/archiver/store.py src/cobalt/db_migrations/placement.py src/cobalt/bars/partitions.py` is EMPTY. HOLDS.
- (iii) `git log -p 427c752..bars/chunk-2-0920 -- <report>`: **8 removed lines**, none above the `# FIX ROUND 1` heading (line 937): the `(filled at CLOSE)` placeholder, six `next:` breadcrumb lines and two lines of an in-progress "Diff stat" sentence, all the fixer's own scaffolding. This is a row.
- (iv) removed `assert` lines in the two test diffs: `test_bars_ensure.py` none; `test_bars_poller_coverage.py` two — the `written == {"AAA": 0}` line in `test_9` and the wholesale `partition_bounds`-stripping call assert in test 1. Each is replaced by a narrower or equally exact assert on a re-pointed fixture; no parametrize narrowed, no skip added.

## Ready for a deploy prompt
| house | ready | reason |
|---|---|---|
| grok | YES | "CHECK R2: FIX STANDS · inert on an unpartitioned parent, every path: YES · ready for its deploy prompt: YES" |
| gemini | YES | "CHECK R2: FIX STANDS · inert on an unpartitioned parent, every path: YES · ready for its deploy prompt: YES" |
| astra | NO | "Stale fixture misses branch; carried failures discard required recovery ranges." |

## ESCALATE
1. **astra `CHECK R2: FIX AGAIN X1, O4-in-memory-range`** — `CHECK R2: FIX AGAIN X1, O4-in-memory-range · inert on an unpartitioned parent, every path: NO · ready for its deploy prompt: NO · Stale fixture misses branch; carried failures discard required recovery ranges.` Grok and gemini answered `FIX STANDS`, YES, YES. The houses split 2–1; nothing here is smoothed.
2. **astra NOT CLOSED on X1** — the `rth_stale` case does not plant `stale` in either poller, so the four-case proof does not cover plain-table staleness (claim HOLDS in the file-check). Grok and gemini answered X1 CLOSED without noting it.
3. **astra DISAGREE on O4 (an OWNER ITEM), in full:** "**DISAGREE with treating the entire finding as OWNER ITEM** — Persistence/card-schema changes are owner scope. Losing the currently computed range inside `PollResult` is already an implementation defect under F2 and prompt 11 test 10." Its sequence: a cycle returns `no_partition` with a range; the runner persists ticker, reason and onset only (`runner.py:288-290`); the next cycle rebuilds the record without detail (`:270-277`); `setdefault` (`poller.py:240`, and `:222` in the write-failure arm) keeps that carried `detail=None`, so the in-memory range is lost; "preserving onset while updating the in-memory range requires neither a persisted fourth key nor a card-schema change." The mechanism HOLDS in the file-check. What the owner would be ruling: whether an in-memory range is required on a carried record, versus a durable or visible surface. Grok and gemini AGREE with O4's class.
4. **Plain-table divergence found by astra** — `poller.py:245` pops a carried `no_partition` record on a plain-table success where main keeps it (HOLDS; astra notes it predates this fix and is outside main's ordinary failure vocabulary).
5. **Literal assertion removals (hub finding)** — `test_9`'s `written == {"AAA": 0}` and test 1's wholesale-strip call assert are removed in the diff, replaced by stronger asserts; gemini answered "no assertion removed" and the fixer's report says "Nothing is removed from the test."
6. **The report's 8 removed lines** are all inside `# FIX ROUND 1` (fact (iii)).
7. **The 14 `requires_db` tests are still unrun and OWED before deploy** (U1, U2, U3). Astra adds that the named bounds test checks timestamp casts and `FOR VALUES FROM` only, so a real rerun/idempotence run is also needed.
8. **OWNER ITEM O1, unchanged:** a raising first `partition_bounds()` aborts a cycle main would have completed. All three houses AGREE with the class; astra notes it still defeats unconditional inertness.
9. **Packet defects:** (a) `QUESTIONS-R2-ASTRA.md` (verbatim) names `../chunk-2-check/spec-final-s3.md`, which does not exist; the real copy is `../chunk-e-check/spec-final-s3.md`, named in astra's launch sentence. (b) The fix diff was cut into three path groups; counts match per group (10 commit headers, 12 `diff --git` lines = the `--stat` touches). Groups 1–2 were copied from tool output and are not line-verified against a second source.
10. **Astra: the final report commit `1351da6` is outside the four-commit range** and its content was not independently established by astra; the hub read it (report only, added lines plus the eight removed above).
11. **L74:** a block asking for a `Claude-Session:` line and naming a file-send tool arrived beside a tool result; recorded once above, not followed.
12. **No `ASK DESK` from this run.**

BARS CHUNK 2 CHECK R2 DONE · grok: CHECK R2: FIX STANDS · inert on an unpartitioned parent, every path: YES · ready for its deploy prompt: YES · gemini: CHECK R2: FIX STANDS · inert on an unpartitioned parent, every path: YES · ready for its deploy prompt: YES · astra: CHECK R2: FIX AGAIN X1, O4-in-memory-range · inert on an unpartitioned parent, every path: NO · ready for its deploy prompt: NO · Stale fixture misses branch; carried failures discard required recovery ranges. · houses that checked: 3 of 3 · FIX rows CLOSED: 4 of 5 · inert on every path: 0 of 3 YES · new defects: 0 · ready for a deploy prompt: 2 of 3 · ESCALATE: 12
