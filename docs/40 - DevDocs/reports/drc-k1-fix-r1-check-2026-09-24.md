# DRC K1 FIX R1 — BUILD CHECK, ROUND 2 (`9a0fc900..40cf173e` on `drc/d1-trading-log`)

Hub `drc-k1-fix-r1-check-0924`, Sonnet 5, started Thu Sep 24 22:10:00 EDT 2026 (from `date`), re-issued launch row R101 (R97's first launch stopped `FAILED PREFLIGHT` on the range; this run reads the re-pointed prompt). Prompt `prompts/2026-09-24/49-drc-k1-fix-r1-check.md`.

## §0 Headline
- Round 2 of the house check of DRC K1 fix round 1 (`9a0fc900..40cf173e`: two red commits, the fix, RUN-1, the second fix, DevDocs, and the executed output of all three suites): Opus 5.5 and Grok both checked, both `FIX STANDS · ready for K2: YES`; H1, H2, H3 `CLOSED` from both; intent `KEPT`, `NOTHING WIDENED`, three suites `SHOWN`, `DESELECTS AS STATED`, RUN-1 `RESULT SHOWN` (green), Opus `SEAM STATED`.
- Grok answered `SEAM GAP`: amended seam point (7) names no `file:line`. In my file-check that claim HOLDS as a fact about the text (`## SEAM FOR D2` (7) carries no citation); Grok itself calls it "the missing citation, not a false rule". `defects that HOLD: 1` → `ready for K2: NO` under §4 (YES needs every checker YES **and** 0 HOLD). ESCALATE: 10.
- Sol: `NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM)` (not probed, 22:10 ET is before that time). No Gemini, no Astra.

## L74
- One block arrived as a system-reminder appended to the Read result of this prompt file (a `Claude-Session:` commit line request and a file-send tool). Recorded once; not followed. This hub commits nothing and sends no file. The build report's own L74 section and round 1's L74 line are data, carried as read.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| placeholder gate | `grep -n -E "R_[_]" …/49-drc-k1-fix-r1-check.md` | 1 | no output — allowed |
| clock | `date` | 0 | `Thu Sep 24 22:10:00 EDT 2026` → `<D>` = 2026-09-24, 22:10 ET |
| GROK GATE (R17) | `grep -n "^| R17 " …/cto-2026-09-24.md` | 0 | `:32` row carries `Grok approved with no asking going forward` — allowed |
| GROK GATE (R17 committed) | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Grok approved with no asking going forward" -- …/cto-2026-09-24.md` | 0 | `1758fd78a572f47b613b2ca831dcfa636ed8f65a` |
| GROK GATE (R19) | `grep -n "^| R19 " …/cto-2026-09-24.md` | 0 | `:34` row carries `All 4 house models approved for use indefinlitly` — allowed |
| GROK GATE (R19 committed) | `git … log -1 --format=%H -S"All 4 house models approved" -- …/cto-2026-09-24.md` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |
| round 1 committed | `git … log -1 --format=%H -- …/drc-k1-check-2026-09-24.md`; `tail -n 3` | 0 | `3aff0134f024826de22c2b580d8abe3c91a3b1eb`; last non-blank line starts `DRC K1 CHECK DONE ·` |
| classification committed | `git … log -1 --format=%H -- …/drc-k1-fix-r1-draft-2026-09-24.md`; `tail -n 3` | 0 | `712e753b60f8e37715c554abe30815351ded4537`; last non-blank line starts `DRC K1 FIX R1 DRAFTED ·` |
| THIS launch | `grep -n "49-drc-k1-fix-r1-check.md" …/cto-2026-09-24.md` | 0 | `:91` R76 (`47`'s row, does not count), `:118` R97 and `:121` R101 (both DESK LAUNCH ROWS naming this file — count) |
| launch row committed | `git … log -1 --format=%H -S"49-drc-k1-fix-r1-check.md" -- …/cto-2026-09-24.md` | 0 | `16fcf04d45484e52fa110033e7b24b8d89676a0d` |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` → UP |
| worktree | `ls /Users/cobalt/cobalt-wt/drc-d1` | 0 | present |
| THE BUILT LINE | `tail -n 3` of the fix build report | 0 | last non-blank line: `DRC K1 FIX R1 BUILT 40cf173e \| on 9a0fc900 \| red d158a8a3 \| offline 2441/0 \| with-DB 2848/0 \| live-note 142/0 \| .env: removed \| 0018: rolled back \| FIX: 3 \| RUNS: 1 \| ESCALATE: 10` — carries every required field; `<tip>` = `40cf173e`, `<red>` = `d158a8a3`; `0018: rolled back`, not UNPROVEN |
| tip subject | `git … log --oneline -1 40cf173e` | 0 | `40cf173e fix(drc): K1 fix r1 — _reason asks the calendar only after an earlier day row (D8 red)` — the second fix commit |
| range | `git … log --oneline 9a0fc900..40cf173e` | 0 | exactly seven lines, oldest last: `40cf173e` · `ecdf4a4d` (docs) · `67a4624b` · `ae4388df` · `0009e9c1` · `d158a8a3` · `a50e5515` (docs) — as the prompt names |
| above the tip | `git … log --oneline 40cf173e..drc/d1-trading-log -- src tests configs` | 0 | EMPTY |
| path union | `git … log --stat --format=%h 9a0fc900..40cf173e` | 0 | `src/cobalt/drc/{models,pairing,store}.py`, `tests/cobalt/test_drc_k1.py`, `test_drc_k1_store.py`, new `test_drc_k1_fix_r1_runs.py`, `docs/40 - DevDocs/cobalt/drc/{models,pairing,store}.md`, the two build reports (`a50e5515`, `ecdf4a4d`); `40cf173e` = `src/cobalt/drc/store.py` only (`8 insertions(+), 5 deletions(-)`); `test_drc_k1_experiments.py` not touched; no `db_migrations`, no `drc/cli.py`, no `configs/` |
| L28 sweep | `grep -rn "VaultWriter" …/src/cobalt/drc` | 1 | no hit |
| L3 sweep | `grep -rn "INSERT INTO" …/src/cobalt/drc/cli.py` | 1 | no hit |
| `.env` | `ls /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `No such file or directory` (never read) |
| recovery | `ls scratch/tribunal-bars-0920/drc-check/k1-fix-r1` | 1 | `No such file or directory` → fresh run |
| STAGGER | `grep -n -F "no other house hub is running" …/cto-2026-09-24.md` | 0 | output large (every launch row carries the literal; saved to a file); the rows that also name `49-drc-k1-fix-r1-check.md` are R97 (`:118`) and R101 (`:121`), each carrying `no other house hub is running` (seen in the `grep -n "49-drc-k1-fix-r1-check.md"` output) |
| PROBE Opus | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (background) | 0 | `OK` → UP; the saved output carried one harness notice line first (the `Bash(git push*:*)` deny-rule syntax notice; a notice, no call denied) |
| PROBE Grok | its `--version` row | — | UP |
| SOL | keyed on `date` (2026-09-24 22:10 ET, before 2026-09-26 06:47 ET) | — | `sol: METER — retry after Sep 26th, 2026 6:47 AM (15 / 37's record)` — not probed, not launched |
| FAIL CLOSED | Opus UP and Grok UP | — | two UP → checkers launched |
| GROK GATE, second row (before launch) | R17 and R19 rows and both `git -S` commits, re-run at 22:21:47 | 0 | same rows (`:33`, `:35` as the file then stood), same hashes `1758fd78…` and `5055151d…` |

## Packet
Staged in `scratch/tribunal-bars-0920/drc-check/k1-fix-r1/` (no `mkdir`; the Write tool created the folder). Sources read from `/Users/cobalt/cobalt-wt/drc-d1/` (code, build report) and `/Users/cobalt/cobalt/` (design, desk file, reports).
| file | bytes | what |
|---|---|---|
| `fix-diff.part1.md` | 18,557 | `git log -p 9a0fc900..40cf173e -- . ":(exclude)docs"`; one part (≤ 38,000 B); header 317 B + 18,240 B (saved stdout 18,262 − 22 B harness trailer) |
| `devdocs-diff.md` | 3,699 | `git log -p 9a0fc900..40cf173e -- "docs/40 - DevDocs/cobalt/drc"`; header 339 B + 3,360 B (3,382 − 22) |
| `code-at-tip.md` | 30,102 | pairing.py 96–311, store.py 199–597, models.py 123–135, cli.py 51–55 and 121–147 (both `except` sites) |
| `build-proof.md` | 16,715 | build report D2 RED, D3 RED, D4 THE EDITS, D4 (run 2), RESTARTS, ESCALATE, the stop line |
| `run.md` | 1,510 | D5 THE RUN + D5 THE RUN (run 2) |
| `suites.md` | 10,194 | D1 BASELINE, D6 (run 1, run 2), D7 (run 1, run 2), D8 (run 1 RED, run 2 GREEN) + the four deselected ids with `file:line` |
| `seam.md` | 8,381 | Part A the amended `## SEAM FOR D2` / `## FOR K2`; Part B the superseded K1 seam |
| `round-1.md` | 21,587 | `40`'s `## Seam`, `## Checked against the branch`, `## FOR THE CLASSIFIER`, `## ESCALATE` + the classification table and `## FOR K2` |
| `design.md` | 10,106 | v3 lines 71, 76, 89–90, 108–118, 126, 133–139, 212–215, 226, 313 + his R51 row |
| `QUESTIONS-DRC-K1-FIX-R1.md` | 5,971 | the questions verbatim + the "Files in this folder:" paragraph |
| **total** | **126,822** | ÷ 4 = **≈ 31,705 tokens per checker**; under the 200,000 B ceiling (drafter's estimate 90–150 KB) |

Written after the checks: `opus-check.md` 5,801 B (by this hub from stdout), `grok-check.md` 8,361 B (by Grok, as told).

Staging checks (each from a tool result):
- `grep -c "^commit "` over the fix diff = **5**; `grep -c "^diff --git"` = **7** = the distinct non-docs path-touches (`40cf173e` 1, `67a4624b` 1, `ae4388df` 3, `0009e9c1` 1, `d158a8a3` 1). `grep -n -F -x -v -f` of the saved output against my copy lists only the one header line and blank lines (grep quirk, same offsets in both directions); trailing-space lines: 27 in the saved output and 27 in the copy, every one at the same line + 1 (the header). Line count 416 = 415 + header.
- `devdocs-diff.md`: 8 whitespace-ending lines in the saved output (6 trailing tab, 2 trailing space), 8 in the copy; only header and blank lines unmatched.
- `code-at-tip.md`: `grep -n -F -x -v -f` against the four sources lists only its own headers, `===` lines and blank lines; 0 whitespace-ending lines.
- `build-proof.md`, `run.md`, `suites.md`: against the build report, only their own headers, `===` lines and blanks unmatched; `build-proof.md` 6 whitespace-ending lines (the diff quote's blank context lines) = the report's 6.
- `seam.md`: against both reports, only its headers, `===` lines and blanks. `round-1.md`: against `40` and the classification, only headers and blanks. `design.md`: against v3 and the desk file, only headers and blanks.
- `QUESTIONS-DRC-K1-FIX-R1.md`: every line but the two that carry the prompt's opening / closing quote mark is present exactly in the prompt; the appended paragraph follows.
- The four deselected ids in `suites.md` were each confirmed by my own `grep -rn` of the name in `tests/cobalt/`: `test_tenancy.py:697`, `test_tenancy.py:710`, `test_tenancy.py:263`, `test_migrate_proof.py:306` (classes at `test_tenancy.py:688` and `:239`). No line moved.
- Not staged: `.env`, `logs/`, any vault file, `_imports/`, round 1's own packet.

Launches (both `run_in_background`, independent, one attempt per house, told "Do not open any *-check.md file"; Opus first):
- OPUS at 22:21:5x (bg `blbefkulq`), `claude -p --model claude-opus-5-5 "You are OPUS. The folder is scratch/tribunal-bars-0920/drc-check/k1-fix-r1/ (absolute path …). Start with QUESTIONS-DRC-K1-FIX-R1.md and follow it exactly. Files named <name>.part<k>.md are one file read in order. Do not open any *-check.md file. Read files with the Read, Grep and Glob tools only. Write no file. Print your complete check as your answer." --permission-mode plan --add-dir /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/drc-check/k1-fix-r1 --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"`. Answered by 22:24:29 (≈ 3 min). Its stdout carried two harness notice lines before the check (the `Bash(git push*:*)` deny-rule syntax notice and a `no stdin data received in 3s` warning) and the 22-byte trailer; `opus-check.md` written by this hub from stdout without those (notice lines and trailer), otherwise byte for byte.
- GROK at 22:22:0x (bg `bg105ule1`), `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "You are GROK. … Write your complete check to /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/drc-check/k1-fix-r1/grok-check.md and reply with only that path."` (never `--always-approve`). Its stdout was progress text and the path; its own file was on disk at 22:32. Grok's file is recorded as Grok wrote it.
- Clock: 45-minute deadline ≈ 23:07; both inside it; no HARNESS / METER / TIMEOUT.
- Written-nothing proof: `ls -la` of the packet folder (10 files, folder mtime 22:21) and of `/Users/cobalt/cobalt-wt/drc-d1` (mtime 21:24, no `.env`) before and after launch were identical; after both finished the packet folder holds the 10 staged files + `opus-check.md` (this hub's) + `grok-check.md` (told to Grok), and `drc-d1` is unchanged (same entries and mtimes).

## CONTINUE
done — packet staged, both checkers answered, every claim walked; report closed below.

## Rows
`row · opus · grok · sol` (FIRST). Sol: NOT SEATED (METER).
| row | opus | grok | sol |
|---|---|---|---|
| H1 | `CLOSED` — "`stated_open_positions` sets `opened_on=None` (`pairing.py:122`)… `pair_day` sets `opened_on=book.carried_from if book.seeded else day` (`:302`), so a stated position and every carry of it keep `None`." | `CLOSED` — "The stated position no longer receives a date, and a carry of it does not invent one. A position opened by an execution still keeps the day it opened." | — |
| H2 | `CLOSED` — "`first import` is returned only when there is no `day < D` row. … none of the three callers can store or print a false reason. A true `chain broken` is still stored" | `CLOSED` — "No caller can store or print an `opening` whose `reason` is `chain broken at <P>` while P is recorded, or `first import` while an earlier day is recorded." | — |
| H3 | `CLOSED` — "Seam point (2) now says the route records the unpaired day with `record_day(pairing, import_ids, None)`: a `day` row, no `seed`, no `book_close`. … the next day raises until D is stated" | `CLOSED` — "`seam.md` point (2) says what the store does, and a test pins the next day failing." | — |

## Intent
- opus · SECOND: `KEPT` — "Only the two named H1 assertions were reversed: `test_drc_k1.py:132` and `test_drc_k1_store.py:420`. The case (iv) change moves `_day1_carrying_ddd()` after `_state(D_NEXT)`…"
- grok · SECOND: `INTENT — KEPT` — "The only assertion lines removed are the two named H1 reversals… Case (iv) adds a docstring and swaps setup order… No `skip`, no `xfail`."

## Scope
- opus · THIRD: `NOTHING WIDENED` — "The non-docs diff touches `drc/models.py`, `drc/pairing.py`, `drc/store.py` and three test files. No migration, `configs/` or `drc/cli.py` path appears"
- grok · THIRD: `SCOPE — NOTHING WIDENED` — "Non-docs diff is five commits… No migration, no `configs/`, no `drc/cli.py`, no vault-write path."

## Seam
`checker · SIXTH answer` (≤40 words each):
- opus · `SEAM STATED` — "Each citation checked against the code at tip: `seed_for` is at `:323`, `record_day` at `:199`… `## FOR K2` names what moved: H1, H2, H3, the calendar order, and RUN-1." (three items `NOT CHECKABLE FROM READS`: `build_day` `:394`, `cli.py:150`, "the stats rows unmatched" — walked below)
- grok · `SEAM GAP` — "(7) names no `file:line` for the stated `opened_on` rule. The rule's prose is what the code does… The gap is the missing citation, not a false rule."

## Suites
`suite · opus · grok · sol` (FOURTH):
| suite | opus | grok | sol |
|---|---|---|---|
| offline | `SHOWN`: "exit 0, `<value> passed, <value> skipped, <value> xfailed`, 0 failed; `.env` absence shown by `ls`." | `SHOWN` — "`2441 passed, 417 skipped, 1 xfailed, 15 warnings in 70.26s`, exit 0, `<f> 0`, 0 errors; `.env` already absent" | — |
| with-DB | `SHOWN`: "exit 0, … 4 deselected …, 0 failed. `.env` was removed and proven gone. The 0016 / 0018 absence probe came up short by exactly the four `drc_*` tables." | `SHOWN` — "`2848 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 145.98s`, exit 0, `<df> 0`, 0 errors… `28 == 32`, short by exactly 4" | — |
| live-note | `SHOWN`: "exit 0, … 0 failed; only the known `test_replay_line.py:256` skip." | `SHOWN` — "`142 passed, 1 skipped, 15 warnings in 10.39s`, exit 0, `<lf> 0`, 0 errors. … none names `COBALT_LIVE_VAULT_ROOT`." | — |
| deselects | `DESELECTS AS STATED` — "2 + 1 + 1 = 4 = the summary's `4 deselected`." | `DESELECTS AS STATED` — "Executed result `4 deselected` matches those four ids." | — |
| second fix | "exactly the one-order change the red named, with nothing more in behaviour… `+7 / -4`, `store.py` only" | "exactly the one-order change the red named and nothing more… (`+7 / -4` inside `_reason`)" | — |

Myself, from the build report (`/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-k1-fix-r1-build-2026-09-24.md`), facts only:
- offline (D7 run 2, `:207`): `2441 passed, 417 skipped, 1 xfailed, 15 warnings in 70.26s (0:01:10)` — no `failed` and no `error` token; `<f>` 0. (D7 run 1, `:204`: `2441 passed, 417 skipped, 1 xfailed, 15 warnings in 70.40s (0:01:10)`.)
- with-DB (D8 run 2, `:224`): `2848 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 145.98s (0:02:25)` — no `failed` / `error` token; `<df>` 0; deselected 4. D8 run 1 (`:212`), staged as the red: `13 failed, 2835 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 145.17s (0:02:25)`, all 13 `CalendarError` (`:213`).
- live-note (D6 run 2, `:201`): `142 passed, 1 skipped, 15 warnings in 10.39s` — no `failed` / `error` token. SKIPPED lines naming `COBALT_LIVE_VAULT_ROOT` in the live-note leg: none (the one skip is `test_replay_line.py:256`, `COBALT_TEST_LIVE_DRC`). The with-DB run 2's six skips include four live-vault skips (`test_radar_evaluate.py:691`, `test_replay_line.py:256`, `test_catalyst.py:365`, `test_predicate.py:262`) and two `test_cards_picks.py` skips, none in the DRC store test files (`:224`).
- deselected count 4, ids as the build report names them (`:210`): `test_tenancy.py:697`, `:710` (class `TestMigrationRoundTrip`, `:688`), `test_tenancy.py:263`, `test_migrate_proof.py:306` — the same four as `suites.md`'s list and my own `grep -rn`.
- absence probe (D8 run 2 (c2), `:225`): `1 failed in 5.69s`, `E       assert 28 == 32` — "short by EXACTLY 4"; `0016 + 0018: rolled back — applied only inside the suite's transaction; absent on cobalt_dev (probe short by 4)`. Run 1's probe was not run (`:218`, "UNPROVEN by this run"); run 2's proved it. The stop line carries `0018: rolled back`, not `0018: UNPROVEN`.
- `.env: removed, proven gone` is written for D3 (`:62` `(D3)`), D8 run 1 (`:219` `(D8)`) and D8 run 2 (`:226` `(D8)`).

## Run
`run · opus · grok · sol` (FIFTH):
| run | opus | grok | sol |
|---|---|---|---|
| RUN-1 | `RESULT SHOWN` — "Green on `ae4388df` and `40cf173e`. The quoted reason line is `unmatched — 0 trades match`, and the stated `GGG` trade has `stats is None`." | `RESULT SHOWN` — "Green, on `ae4388df` and again on `40cf173e`: exit 0, `1 passed`. The reason line the passing assertion quotes is `unmatched — 0 trades match`. No `xfail` added." | — |

Myself, from the build report: RUN-1 D5 (`:192`): "RUN-1 GREEN on `ae4388df`: no exception; the `GGG` trade's `stats is None`; the one stats row (line 2, `GGG`) is in `unmatched`, attached to no other trade; its `reason` — asserted equal, so quoted by the passing assertion — is `unmatched — 0 trades match`. Kept as a plain pin (no mark)." D5 run 2 (`:195`): `1 passed in 0.02s`, "the reason is still `unmatched — 0 trades match`". It is green, not a strict `xfail` (no mark in `fix-diff.part1.md`; the test asserts `u.reason == "unmatched — 0 trades match"`). The code path: `pairing.py:370` compares `t.entry_time == row.open_time`; `:373` `unmatched — {len(hits)} trades match` (walked in the real file).

## Reds
Myself, from the build report:
- D2 (`:48-53`, offline, on `d158a8a3`): `2 failed, 53 passed in 0.11s` — `test_a_stated_position_is_one_lot_with_no_time_and_a_stable_id` at `test_drc_k1.py:136` `E       AssertionError: assert (datetime.date(2001, 1, 3) is None)`; `test_a_stated_positions_open_day_stays_not_stated_through_the_carry` at `test_drc_k1.py:174` `E       AssertionError: assert datetime.date(2001, 1, 3) is None`. Both are the rows the build named (the reversed `:132` assertion, now `:136`, and the NEW carry test). `test_a_carried_positions_open_day_is_kept` (GREEN-as-pin) passed.
- D3 (`:55-63`, with-DB, on `0009e9c1`): `2 failed, 56 passed in 3.13s` — `test_an_opening_is_refused_while_its_prior_trading_day_is_recorded` at `test_drc_k1_store.py:320` `E       Failed: DID NOT RAISE <class 'ValueError'>`; `test_seed_vi_a_stated_book_seeds_a_first_import` at `test_drc_k1_store.py:444` `E       AssertionError: assert (datetime.date(2001, 1, 2) is None)`. Both are named rows (H2's NEW test; H1's reversed `:420` assertion, now `:444`). I read `test_drc_k1_store.py:320` and `:444` in the real file: `:320` is the `pytest.raises(ValueError, match="is recorded")` block, `:444` the reversed assertion.
- No GREEN-as-pin test was red: `test_a_carried_positions_open_day_is_kept` passed at D2; the reordered case (iv) test and the H3 pin passed on the base at D3 (`:61`; build ESCALATE 3).
- The with-DB run 1 red on `67a4624b` (13 `CalendarError`, `:212-213`) is not a named red; it is the one the second fix `40cf173e` answers (build ESCALATE 6).

## Checked against the branch
`claim · who · file:line · HOLDS / DOES NOT HOLD / NOT CHECKABLE FROM READS · ≤30 words`:
| # | claim | who | file:line | verdict | note |
|---|---|---|---|---|---|
| 1 | `SEAM GAP` — amended point (7) (a stated position's `opened_on` is `None`) names no `file:line` | grok | build report `## SEAM FOR D2` (7) `:256` (text carries no citation); the code it describes: `models.py:134`, `pairing.py:122`, `:302` | **HOLDS** | The text of (7) has no `file:line` (verified in the build report); the rule is what the code does. Grok: "the missing citation, not a false rule". Opus: `SEAM STATED`. Quoted both, smoothed neither. |
| 2 | Opus `NOT CHECKABLE FROM READS`: seam (2) cites `build_day` at `pairing.py:394`, not in `code-at-tip.md` | opus | `pairing.py:394` `def build_day(` | walked — bears out | Real file line 394 is `def build_day(`. Not a defect. |
| 3 | Opus `NOT CHECKABLE FROM READS`: seam (6) cites `drc/cli.py:150` | opus | `cli.py:150` | walked — bears out | Real file line 150 is `def add_parser(sub)`. Not a defect. |
| 4 | Opus `NOT CHECKABLE FROM READS`: seam (2) "the stats rows unmatched" for a not-computed day; `build_day` body not staged | opus | `pairing.py:407-416` | walked — bears out | `build_day` with `seed=None` returns a not-computed pairing whose `unmatched` holds every stats row, reason `unmatched — no trades were paired` (`:412`). Not a defect. |
| 5 | Grok's H3 citations `store.py:299` (`seed` only when `seed is not None`), `:312` (`book_close` only when computed), `:422-429` (`_carried`'s raise) | grok | packet `code-at-tip.md:299`, `:312`, `:428`; real `store.py:272`, `:285`, `:401` | claims true; line numbers are packet-relative | Opus cites the real lines (`:272`, `:285`). Not one of the claim kinds; not counted. |
| 6 | Both checkers repeat the build's "`+7 / -4`" for the second fix | opus, grok | `git -C … show --stat 40cf173e`: `src/cobalt/drc/store.py | 13 ++++++++-----`, `8 insertions(+), 5 deletions(-)` | build prose off by one each way | The diff itself (`fix-diff.part1.md`, first commit) is the reorder + one comment line; the numbers are the build's prose (`:186`). Not counted; carried to ESCALATE. |

(i) L28 / L3 SWEEP: `grep -rn "VaultWriter" …/src/cobalt/drc` → no hit; `grep -rn "INSERT INTO" …/src/cobalt/drc/cli.py` → no hit.
(ii) `grep -rn "opened_on" /Users/cobalt/cobalt-wt/drc-d1/src/cobalt` → four hits, all placed: `drc/models.py:134` (the field, `Optional[date]`), `drc/pairing.py:122` (`opened_on=None`, `stated_open_positions`), `:217` (`carried_from=position.opened_on`, `_seeded`), `:302` (`opened_on=book.carried_from if book.seeded else day`, `pair_day`). No hit outside `drc/models.py` and `drc/pairing.py`.
(iii) `git -C /Users/cobalt/cobalt log --oneline 9a0fc900..40cf173e -- src/cobalt/db_migrations src/cobalt/drc/cli.py configs` → EMPTY.
(iv) L32: this report was read once before the last line: no ticker beyond the constructed `GGG` / `HHH` / `DDD`, no real date of his, no file name of his and no value written.

## Ready for K2
`checker · CHECK DRC K1 FIX R1 line · ready: YES|NO · reason verbatim`:
- opus · `CHECK DRC K1 FIX R1: FIX STANDS · ready for K2: YES` · ready: YES · (no reason line)
- grok · `CHECK DRC K1 FIX R1: FIX STANDS · ready for K2: YES` · ready: YES · (no reason line)
- Hub: `defects that HOLD` = 1 (Grok's `SEAM GAP` on point (7), Checked-against-the-branch row 1), so `ready for K2: NO` under §4 (YES needs every checker YES **and** 0 HOLD).

## FOR THE CLASSIFIER
Round 2 of ≤3 — a HOLD goes to round 3, the last (L75). One item per claim that HOLDS in my file-check; no class, no recommendation:
1. Claim: "(7) names no `file:line` for the stated `opened_on` rule. The rule's prose is what the code does (`models.py:133`, `pairing.py:122`, `pairing.py:302`), and `## FOR K2` says what moved… The gap is the missing citation, not a false rule." — Grok — the seam (SIXTH; build report `## SEAM FOR D2` (7) `:256`; code `models.py:134`, `pairing.py:122`, `:302`) — HOLDS.

## ESCALATE
1. FOR THE CLASSIFIER item 1 (Grok, `SEAM GAP`, amended seam point (7) carries no `file:line`; Opus `SEAM STATED`) — HOLDS at the build report `## SEAM FOR D2` (7), `:256`.
2. Any checker's `DEFECT REMAINS`: none — both answered `FIX STANDS · ready for K2: YES`.
3. Build prose vs git: the build report's D4 (run 2) says the second fix is `+7 / -4` inside `_reason` (`:186`); `git show --stat 40cf173e` reads `8 insertions(+), 5 deletions(-)`. The diff is the one-order change the red named; only the count in the prose differs. Both checkers repeated the prose count.
4. Grok's H3 line citations (`store.py:299`, `:312`, `:422-429`) are line numbers of `code-at-tip.md`, not of `store.py` (real: `:272`, `:285`, `:401`); its claims are true. Recorded, not counted.
5. Packet mismatch: none. A checker that did not check: none. A checker that wrote a file it was not told to: none. `ASK DESK`: none. Opus's stdout carried two harness notices (deny-rule syntax; `no stdin data`), no denial of any call.
6. L74: one block arrived as a system-reminder beside the Read of this prompt (a `Claude-Session:` commit line request naming a file-send tool); recorded once, not followed.
7. Sol: `NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM)` — not probed (22:10 ET is before it); the desk seats Sol from that time (L62 R19).
8. Astra: the K1 NEW BUILD's Astra read is owed from Sep 26th, 2026 6:47 AM (40 ESCALATE 11) — the desk's seat, not this round's.
9. The build's OWNER ITEM line, verbatim (carried for the desk; his, not this check's): "**OWNER ITEM carried, not built (the residue of H1): whether his opening-book statement also takes each swing's open day. Until he rules, a stated position's `opened_on` is `None` — not stated, never a date known false (L1). His ruling is on the drafter's `## OWNER ITEMS`.** (Desk row R90 records his R80 "B" — "not stated" is enough; `None` as written.)"
10. Standing lines: **"Round 2 covers DRC K1 fix r1 only (`9a0fc900..40cf173e`), with RUN-1, the amended seam and its three suites' executed output, checked by Opus 5.5 + Grok (+ Sol when seated) under his R95 (a fix round = other check; Gemini out, R96/R97). With every seated house `ready for K2: YES` and `defects that HOLD: 0`, K1 is checked (L67) and the K2 build may launch on this tip, citing the fix report's `## SEAM FOR D2` / `## FOR K2`; a HOLD goes to round 3, the last (L39, L75); a NO with `defects that HOLD: 0` leaves round 3 or his per-case override (L67 OVERRIDE / L73). The opening-book open day is his owner item, not this check's."** and **"The deploy's L68 gate re-proves offline, with-DB and the live-note suite on the stacked tree that ships (D1 + K1 + K2 + D4 + D2 + D3); the deploy prompt gets its own house read (L67, R95 seats)."** This round: both seated houses `YES`, `defects that HOLD: 1` → the round-3 branch of the first line applies.

DRC K1 FIX R1 CHECK DONE · round: 2 · opus: CHECK DRC K1 FIX R1: FIX STANDS · ready for K2: YES · grok: CHECK DRC K1 FIX R1: FIX STANDS · ready for K2: YES · defects that HOLD: 1 · ready for K2: NO · ESCALATE: 10
