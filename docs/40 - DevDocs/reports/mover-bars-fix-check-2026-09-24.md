# MOVER BARS FIX CHECK — 2026-09-24 (round 1 of ≤3)

Seat `mover-bars-fix-check-0924` · Sonnet 5 hub · checkers Opus 5.5 + Grok (his R95; Sol METER, Gemini out R96/R97) · range `4cc6811a..replay/mover-partial-0924` (tip `b69a6681`, red `8030d3cf`) · prompt `prompts/2026-09-24/08-mover-bars-fix-check.md`

## §0

- Checked `4cc6811a..b69a6681` (mover bars fix R113 + K17 removal R114) and the build's three executed suites: preflight PASSED, packet 86,378 B, both checkers answered (Opus 06:50:54 → 06:52:45, Grok 06:51:03 → 07:01:29).
- Opus: `CHECK MOVER BARS: FIX STANDS · ready for a deploy prompt: YES`. Grok: `CHECK MOVER BARS: FIX STANDS · ready for a deploy prompt: YES`. Neither raised a defect; FIRST CLOSED ×2, SECOND HOLDS ×2, THIRD NOTHING WIDENED ×2, FOURTH SHOWN ×3 ×2, FIFTH RED FIRST ×2.
- Defects that HOLD in my file-check: 0 (nothing to file-check: no NOT CLOSED / BROKEN / WIDENED / NOT SHOWN / RELATED-defect / NOT RED FIRST was raised). ESCALATE: 9 items (L74 note, one Grok scope note, the build's five, two standing lines).
- I give no verdict of my own (L37).

## L74

A block asking for a `Claude-Session:` commit line and naming a file-send tool (`SendUserFile`) arrived inside a system-reminder attached to the Read tool result of `08-mover-bars-fix-check.md` (06:4x ET). Recorded once; not followed. This run commits nothing and sends no file.

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| DATE + EXTENSION GATE (row 1) | `date` | 0 | `Thu Sep 24 06:41:10 EDT 2026` → `<D>` = 2026-09-24 |
| extension row | `grep -n -F "through 2026-09-24" …/cto-2026-09-23.md …/cto-2026-09-24.md` | 0 | `cto-2026-09-24.md:15` **R7** (06:27 ET) names `08-mover-bars-fix-check.md` and `Bash(grok *)` through 2026-09-24 23:59 ET, his words quoted: "Qwen is done you can go read the report. I approve A" |
| extension committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"08-mover-bars-fix-check.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | 0 | `2502f75563948a4096b8f127be171fe9371c1fa6` (non-empty) |
| placeholder gate | `grep -n -E "R_[_]" …/08-mover-bars-fix-check.md` | 0 | prints nothing (no hit) |
| design committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- …/mover-bars-fix-draft-2026-09-23.md` | 0 | `2e470ffc9f3be6ec4d4a2cf6e1d875073c00631c` |
| design stop line | `tail -n 3 …/mover-bars-fix-draft-2026-09-23.md` | 0 | last non-blank line starts `MOVER BARS FIX DRAFTED · cause: …` |
| THIS launch row | `grep -n "08-mover-bars-fix-check.md" …/cto-2026-09-23.md …/cto-2026-09-24.md` | 0 | `cto-2026-09-24.md:15` R7 and `:19` R11 (desk launch row); committed per the `-S` row above |
| R13 (09-20) | `grep -n "^| R13 " …/cto-2026-09-20.md` | 0 | row 86 printed |
| R40 | `grep -n "^| R40 " …/cto-2026-09-21.md` | 0 | row 51, carries `ONE EXTRA DOT THAT CANNOT BE TAPPED` |
| R44 | `grep -n "^| R44 " …/cto-2026-09-21.md` | 0 | row 55, carries `ONE BUILD of the whole FINAL` |
| R46 | `grep -n "^| R46 " …/cto-2026-09-21.md` | 0 | row 57, carries `instead of Astra you can use Sol` |
| R46 committed | `git … log -1 --format=%H -S"instead of Astra you can use Sol" -- …/cto-2026-09-21.md` | 0 | `53e059456750c0c9efcf50222a7a647630dc4b04` |
| R49 | `grep -n "^| R49 " …/cto-2026-09-21.md` | 0 | row 60, carries `"Approved"` |
| R49 Sol string present | `grep -c -F "Bash(codex exec … -s read-only *)" …/cto-2026-09-21.md` | 0 | `1` |
| Sol string committed | `git … log -1 --format=%H -S"Bash(codex exec … -s read-only *)" -- …/cto-2026-09-21.md` | 0 | `60147d400b009db5a2518e02b8ab1fe5765db405` |
| R32 (Opus 5.5 string) | `grep -n "^| R32 " …/cto-2026-09-22.md` | 0 | row 131, carries `claude -p --model claude-opus-5-5` |
| R32 committed | `git … log -1 --format=%H -S"Bash(claude -p --model claude-opus-5-5 *)" -- …/cto-2026-09-22.md` | 0 | `b8a72b5300370e248cd6c7a8a732258fec03e6a0` |
| the 12 allow + 3 deny strings | `grep -c -F -e '"<rule>"' …/2026-09-20/08-bars-chunk-e-check.md` ×15 (grok, mkdir, show, log, s2-p2-cards ×3, ls, grep, tail, wc, date, AskUserQuestion, EnterWorktree, git push) | 0 each | each counts `1` |
| Astra string | not in this launch line | — | absent (R46) |
| clock | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| worktree | `ls /Users/cobalt/cobalt-wt/mover-bars` | 0 | present (AGENTS.md … uv.lock) |
| THE BUILT LINE | `tail -n 3 …/mover-bars-fix-build-2026-09-24.md` | 0 | last non-blank: `MOVER BARS FIX BUILT b69a6681 \| on 4cc6811a \| red 8030d3cf \| offline 2258/0 \| with-DB 2603/0 \| live-note 142/0 \| .env: removed \| FIX: 2 \| ESCALATE: 5` — carries `\| .env: removed \|` and `FIX: 2`. **`<tip>` = b69a6681 · `<base>` = 4cc6811a · `<red>` = 8030d3cf** |
| range log | `git -C /Users/cobalt/cobalt log --oneline 4cc6811a..replay/mover-partial-0924` | 0 | **5 commits:** `59532385 docs(mover-bars): build report — b69a6681` · `b69a6681 docs(replay): archived-partial movers — DevDocs + ADR-0010 amendment (R113, R114)` · `2d49f6ef test(smoke): the committed suite's K-family pin drops K17 (R114)` · `38e54342 fix(replay,smoke): a mover whose source bars are short of the session is archived-partial, named, counted by side; K9 green only with that marker; K17 out of the S2 smoke (R113, R114)` · `8030d3cf test(replay,smoke): red — a short-source mover is partial not incomplete; K9 needs the job row's marker; K17 leaves the S2 smoke (R113, R114)` |
| red commit | `git … show --stat --format=%H 8030d3cf` | 0 | ONLY `tests/cobalt/test_replay_movers.py` (51), `tests/cobalt/test_replay_runner.py` (107), `tests/cobalt/test_smoke.py` (79/…) — 3 files, 228 insertions, 9 deletions |
| migrations / fixtures | `git … log --oneline 4cc6811a..replay/mover-partial-0924 -- src/cobalt/db_migrations tests/fixtures` | 0 | EMPTY |
| `.env` | `ls /Users/cobalt/cobalt-wt/mover-bars/.env` | 1 | `No such file or directory` (expected; never read) |
| recovery | `ls scratch/tribunal-bars-0920/mover-bars-fix-check` | 1 | `No such file or directory` → fresh run |
| STAGGER | `grep -n -F "no other house hub is running" …/cto-2026-09-24.md` | 0 | line 19 (R11) carries it and names `08-mover-bars-fix-check.md` (line 13 R5 names `06`, not this file) |
| Opus probe | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (background) | 0 | `OK` → **OPUS UP** |
| Grok probe | `grok --version` row above | 0 | **GROK UP** |
| checker count | | | 2 of 2 UP (fail-closed floor met) |

The build's D-sections were read from `/Users/cobalt/cobalt-wt/mover-bars/docs/40 - DevDocs/reports/mover-bars-fix-build-2026-09-24.md` (176 lines).

## Packet

Folder `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/mover-bars-fix-check/` (no `mkdir`; the Write tool created it). Every file went Read → Write below a one-line header naming the real path, range and `<tip>`. Not staged: `.env`, `logs/`, any vault note, any DB output.

| file | bytes (`wc -c`) | what | check I ran |
|---|---|---|---|
| `diff.md` | 39,116 | PART 1 `git show 8030d3cf` (16,351 B saved stdout) + PART 2 `git log -p --format="commit %H %s" 8030d3cf..b69a6681` (22,236 B saved stdout) | `grep -c "^diff --git"` = 14 = 3 (red) + 11 (fix, K17 pin, docs); 3 commits in part 2 = 3 (`grep -c "^commit "` on the saved stdout); trailing-whitespace lines 42 = 15 + 27 (same counts as the two originals); line-by-line `grep -v -x -F -f <saved stdout>` found ONE retyping error of mine (`"FormationCounts"` dropped from the `__all__` line in the `models.py` hunk), fixed with Edit and not re-found; every path the build report's D1–D3 name appears (3 tests + `movers.py` `models.py` `runner.py` `cli.py` `s2.yaml` + `test_smoke.py` pin + 5 docs) |
| `code-at-tip.md` | 10,451 | `movers.py` 530–614, `cards.py` 135–164, `runner.py` 318–395 | source files have 0 trailing-whitespace lines (`grep -c`); every non-blank line matches the source file (`grep -v -x -F -f`); only headings and blank lines unmatched |
| `smoke-at-tip.md` | 12,909 | `s2.yaml` 223–488 and 593–608 | `s2.yaml` has 0 trailing-whitespace lines; same line-match check, only headings/blank unmatched; 288 lines = 4 + 266 + 2 + 16 |
| `suites.md` | 12,002 | build report D1 RED, D3 GREEN + DOCS, D4 LIVE-NOTE, D5 SUITE, D5b WITH-DB, RESTARTS, ESCALATE, the stop line, each whole | build report has 0 trailing-whitespace lines; line-match check found ONE retyping error of mine (ESCALATE item 5 truncated), fixed with Edit; after it only my section headings and blank lines are unmatched. Every suite section holds its summary line (`9 failed, 106 passed` red; `142 passed, 1 skipped`; `2258 passed, 351 skipped, 1 xfailed`; `2603 passed, 6 skipped, 1 xfailed`), so no `FAILED: packet — … carries no executed result` |
| `design.md` | 7,346 | drafter's `## FORENSICS` + `## DESIGN`, lines 12–71 | drafter report has 0 trailing-whitespace lines; line-match check, only heading/blank unmatched |
| `QUESTIONS-MOVER-BARS.md` | 4,554 | the prompt's questions verbatim (lines 2–7 match the prompt byte for byte; line 1 and the last line differ only by the prompt's opening/closing quote mark) + the "Files in this folder:" paragraph | `grep -v -x -F -f` against the prompt |
| **total** | **86,378** | | ÷ 4 = **≈ 21,595 tokens per checker** (drafter's estimate 60–110 KB, 15–28k tokens). **Under the 150,000 B ceiling by 63,622 B.** |

Deviation, named: the prompt asks for `wc -c` against the original for whole-file copies naming the header's bytes. These files are excerpts or composites (no single original to compare), so the content check is the line-by-line match above plus the line counts; the header lines are mine.

Written-nothing proof, launch lines and clock: see `## CONTINUE`, filled as each seat is launched.

## CONTINUE

DATE + EXTENSION GATE, second row (immediately before the launches): `date` → `Thu Sep 24 06:50:36 EDT 2026` (`<D>` = 2026-09-24); `grep -n -F "through 2026-09-24" …/cto-2026-09-23.md …/cto-2026-09-24.md` → R7 (`cto-2026-09-24.md:15`, 06:27 ET, names `08-mover-bars-fix-check.md` and `Bash(grok *)`, his words quoted); `git … log -1 --format=%H -S"08-mover-bars-fix-check.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` → `2502f75563948a4096b8f127be171fe9371c1fa6`. PASS.

Written-nothing proof, BEFORE the launches (both listings taken twice, once before each launch, identical): packet folder = the six files above (`code-at-tip.md 10451`, `design.md 7346`, `diff.md 39116`, `QUESTIONS-MOVER-BARS.md 4554`, `smoke-at-tip.md 12909`, `suites.md 12002`); `/Users/cobalt/cobalt-wt/mover-bars` = 27 entries, newest mtime `tests 06:32`, `.venv 06:31`, `src 06:31`, root dir `06:39`, no `.env`.

Launch lines AS RUN (each `run_in_background`, one attempt per house, independent, neither pointed at the other's check; no `--always-approve`, no `--dangerously-skip-permissions`):
- **OPUS**, `06:50:54 EDT`, task `bs9pzqbz3`: `claude -p --model claude-opus-5-5 "You are OPUS. The folder is scratch/tribunal-bars-0920/mover-bars-fix-check/ (absolute path /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/mover-bars-fix-check/). Start with QUESTIONS-MOVER-BARS.md and follow it exactly. Do not open any *-check.md file. Read files with the Read, Grep and Glob tools only. Write no file. Print your complete check as your answer." --permission-mode plan --add-dir /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/mover-bars-fix-check --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"`
- **GROK**, `06:51:03 EDT`, task `bff6a4n63`: `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "You are GROK. The folder is scratch/tribunal-bars-0920/mover-bars-fix-check/. Start with QUESTIONS-MOVER-BARS.md and follow it exactly. Do not open any *-check.md file. Write your complete check to /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/mover-bars-fix-check/grok-check.md and reply with only that path."`
- Sol NOT SEATED (METER, retry after Sep 26th, 2026 6:47 AM); Gemini NOT SEATED (R96/R97); no Astra. Not probed, not launched.

45-minute clock: OPUS would stop at 07:35:54, GROK at 07:36:03. Neither ran past it: no TIMEOUT, no TaskStop, no relaunch.

Completions (each `date` run at the notice): **OPUS** completed, exit 0, `Thu Sep 24 06:52:45 EDT 2026` (≈ 1 min 51 s), harness/monitor line `OPUS finished 06:52:48`; its answer ends with the `CHECK MOVER BARS:` line. **GROK** completed, exit 0, `Thu Sep 24 07:01:29 EDT 2026` (≈ 10 min 26 s); it printed the path `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/mover-bars-fix-check/grok-check.md` and had **written that file itself** (6,855 B, mtime 07:01, the one file its `--allow` covers); its file ends with the `CHECK MOVER BARS:` line. I wrote `opus-check.md` (4,415 B) from Opus's stdout, byte for byte without the harness's `[exited with code 0]` footer, and I held it back until Grok had finished, so Grok could not see it (independence, L44).

Written-nothing proof, AFTER (`ls -la` pairs after each checker returned):
- After OPUS: packet folder identical to BEFORE (six files, same sizes and mtimes); `/Users/cobalt/cobalt-wt/mover-bars` identical (27 entries, same mtimes, no `.env`). Denial-line count in Opus's answer (`grep -c -i "denied\|not allowed\|permission"`) = `0`.
- After GROK: packet folder = the six BEFORE files + `grok-check.md` (6,855 B, 07:01: Grok's own file, as asked) + `opus-check.md` (4,415 B, 07:01: mine, written after Grok returned); `/Users/cobalt/cobalt-wt/mover-bars` identical to BEFORE. Denial-line count in `grok-check.md` = `0`. Nothing else new or changed; no checker `WROTE:` mark.

next: none. Both seats answered with a `CHECK MOVER BARS:` line; the collation below is complete.

## The 09-23 case

| checker | FIRST, verbatim (≤30 words) |
|---|---|
| opus | "**CLOSED** … The ticker goes into `outcome.partial` with `code source_bars_short` … neither `incomplete` … nor `archived_ids` … counts it on each of those sides … K9 for that side passes with the marker" |
| grok | "CLOSED … is `partial`, is not filed incomplete, is not archived, is named in a warning, and is counted on every side it is stored on. K9 for that side passes when that count equals the side's not-archived rows." |

## Stays red

| checker | SECOND, verbatim (≤30 words) |
|---|---|
| opus | "**HOLDS** … marker is 0 and one row is not archived, the compare FAILs while K9.7 and K9.8 both PASS … zero bars … stays `incomplete` … ERROR log … `mark_bars_archived` receives only `archived_ids`" |
| grok | "HOLDS … Unequal numbers are FAIL; an errored operand is ERROR … Zero bars after a clean fetch: `count == 0` appends `incomplete` … `bars_archived` is never set true for a partial" |

## Scope

| checker | THIRD, verbatim (≤30 words) |
|---|---|
| opus | "**NOTHING WIDENED** … None of these are in the diff: a migration, a fixture, a new SQL statement … The three amended pins (T6a, T6b, T7a) each pinned only the shape that R113/R114 remove." |
| grok | "NOTHING WIDENED … No migration. No fixture file. No new SQL text … K-row edits are K9.1 / K9.4's `expect` … the six rows K9.7–K9.12, and the K17 block deleted … T7a only subtracts `K17`" |

## Suites

| suite | opus | grok |
|---|---|---|
| offline | "**SHOWN** `2258 passed, 351 skipped, 1 xfailed, 15 warnings in 70.01s (0:01:10)`, 0 failed, `.env` absent" | "SHOWN — offline: `2258 passed, 351 skipped, 1 xfailed, 15 warnings in 70.01s (0:01:10)` · 0 failed, 0 errors · `.env` absent before the run" |
| with-DB | "**SHOWN** `2603 passed, 6 skipped, 1 xfailed, 15 warnings in 206.17s (0:03:26)`, 0 failed; `.env` removed and proven gone" | "SHOWN — with-DB: `2603 passed, 6 skipped, 1 xfailed, 15 warnings in 206.17s (0:03:26)` · 0 failed, 0 errors · `.env` removed and proven gone" |
| live-note | "**SHOWN** `142 passed, 1 skipped, 15 warnings in 11.83s`, 0 failed; the skip names `COBALT_TEST_LIVE_DRC`" | "SHOWN — live-note: `142 passed, 1 skipped, 15 warnings in 11.83s` · `<lf> = 0`. The one skip names `COBALT_TEST_LIVE_DRC`" |
| RED NOT IN THIS DIFF | "none — No such line appears in suites.md." | "No `RED NOT IN THIS DIFF` line in `suites.md` … D3 iteration 1 … RELATED — K17's deletion in `38e54342` made the old K1–K18 pin red; `2d49f6ef` … subtracts K17 only … Not a leftover red." |

Myself, from the build report `/Users/cobalt/cobalt-wt/mover-bars/docs/40 - DevDocs/reports/mover-bars-fix-build-2026-09-24.md` (not the packet copy), facts only:
- **offline (D5, line 129):** `2258 passed, 351 skipped, 1 xfailed, 15 warnings in 70.01s (0:01:10)` — shows `0 failed` (no `failed` token in the summary; report says "**0 failed, 0 errors.**"); no `error` token in the summary line.
- **with-DB (D5b (c), line 135):** `2603 passed, 6 skipped, 1 xfailed, 15 warnings in 206.17s (0:03:26)` — same: no `failed` or `error` token; report says "**0 failed, 0 errors.**"
- **live-note (D4, line 119):** `142 passed, 1 skipped, 15 warnings in 11.83s` — no `failed` or `error` token; the report gives `<lf>` = 0. It has one SKIPPED line: `SKIPPED [1] tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`).
- `.env: removed, proven gone`: written in D5b (d), line 136: "**`.env`: removed, proven gone** (06:39:43 ET, `date`)", after `ls` → `No such file or directory`; I re-proved it at 06:4x (`ls /Users/cobalt/cobalt-wt/mover-bars/.env` → No such file).
- Other executed runs in the report: D1 RED `9 failed, 106 passed, 3 skipped in 9.76s`; D3 iteration 1 `1 failed, 114 passed, 3 skipped in 8.94s`; iteration 2 `115 passed, 3 skipped in 8.83s` (0 failed, 0 errors).
- `RED NOT IN THIS DIFF` lines: `grep -n -i "RED NOT IN THIS DIFF"` on the build report → **none**. The only red outside D1 is D3 iteration 1's `test_smoke_checks_load_through_schema_bad_file_crashes_with_line` (`Extra items in the right set: 'K17'`), recorded by the report as caused by R114 and amended in the range (`2d49f6ef`); Grok quotes it and marks it `RELATED` (the diff caused it, and the same diff fixed it, per its words "Not a leftover red"); Opus says none.

## Red first

| checker | FIFTH, verbatim (≤30 words) |
|---|---|
| opus | "**RED FIRST** … The red commit `8030d3cf` touches three test files only. Each red line number matches the red diff: T1 :631, T2 :653, T3 :672, T6 :1316, T7 :1355 and T6a :1239." |
| grok | "RED FIRST … `8030d3cf` is tests only … No src, no yaml. D1: `9 failed, 106 passed, 3 skipped`. T1–T7 each failed on the base for the gap this fix closes" |

## Checked against the branch

Both checkers ruled `CLOSED` / `HOLDS` / `NOTHING WIDENED` / `SHOWN` ×3 / `RED FIRST`. No `NOT CLOSED`, `BROKEN`, `WIDENED`, `NOT SHOWN`, `NOT RED FIRST` or defect-`RELATED` claim exists, so no claim is open for file-check, and the two checkers do not contradict each other. Rows:

| claim | who | file:line | result | note |
|---|---|---|---|---|
| (none raised) | — | — | — | nothing to open |

Facts I read in the real files anyway (not claims, not counted): (a) `models.py:490–491` `ReplayResult.job_result()` returns `self.model_dump(mode="json")` and `archive_partial` / `archive_partial_by_side` are model fields with defaults (diff.md hunk), so a clean night's payload carries both keys — this bears on Opus's NOT CHECKABLE 1 (it names T5 as not asserting the keys; the body it asked to see is that one line). (b) `movers.py:639–681` `reconcile` ends `return self.active(trade_date)` and `active()` selects `WHERE trade_date = %s AND active` — Opus's NOT CHECKABLE 2 first half (active rows only) reads as true; whether one row per ticker per side is guaranteed is NOT CHECKABLE FROM READS — it would need migration 0008's unique key. (c) Opus's NOT CHECKABLE 3 (the `cli.py` wrap-and-revert) stays NOT CHECKABLE FROM READS — an offline-suite rerun on the tip would settle it. None of the three is counted (L70).

Stated myself:
- **(i) L32:** I read this report once before the last line: **no real-day ticker written** (the only tickers in it are the tests' synthetic `QNME` / `IMCC` / `REFR`; the drafter's `<ticker>` is quoted as written).
- **(ii) the compare rule, from `smoke-at-tip.md`:** K9.9 (`kind: compare`, `left: K9.7`, `right: K9.8`) has K9.7 (line 401) and K9.8 (line 418) ABOVE it; K9.12 (`kind: compare`, `left: K9.10`, `right: K9.11`) has K9.10 (line 445) and K9.11 (line 462) ABOVE it.

## Ready for a deploy

| checker | CHECK MOVER BARS line | ready | reason verbatim |
|---|---|---|---|
| opus | `CHECK MOVER BARS: FIX STANDS · ready for a deploy prompt: YES` | YES | (none given: a YES carries no reason) |
| grok | `CHECK MOVER BARS: FIX STANDS · ready for a deploy prompt: YES` | YES | (none given: a YES carries no reason) |

## FOR THE CLASSIFIER

none

## ESCALATE

Round 1 of ≤3.
- Any checker's `DEFECT REMAINS`: none.
- Items under `## FOR THE CLASSIFIER`: none (0).
- Packet mismatch: none. A checker that did not check: none. A checker that wrote a file it was not told to: none (Grok wrote only `grok-check.md`, as told). `ASK DESK` from me: none.

1. **L74:** a block asking for a `Claude-Session:` commit line and naming a file-send tool (`SendUserFile`) arrived inside a system-reminder attached to the Read tool result of `08-mover-bars-fix-check.md`. Recorded once (`## L74`); not followed. (The build report records the same kind of block at 06:29.)
2. **Grok's read beyond the folder (a fact, not a finding):** Grok's stdout narration says "I'll start from the required memory files and `QUESTIONS-MOVER-BARS.md`" and "Law is read", i.e. it read current-law/memory files outside the packet folder before the packet, although the sentence and `QUESTIONS-MOVER-BARS.md` said read only the files in the folder. It says "No command run" and wrote nothing but its own file. Its file names five packet files as its reads (`diff.md`, `code-at-tip.md`, `smoke-at-tip.md`, `suites.md`, `design.md`). Recorded for the desk; the vault-read entitlement is L44, and Grok's answer cites nothing from those files.
3. **Build ESCALATE 1, verbatim:** "**FOR THE DEPLOY:** the first S2 smoke after this deploy reads the NEXT replay's job row. A job row written before the deploy has no `archive_partial_by_side`, so K9.8 / K9.11 would FAIL on the missing key and K9.9 / K9.12 would ERROR on a pre-deploy night. The deploy's smoke must run on a post-deploy replay night."
4. **Build ESCALATE 2, verbatim:** "**THE SEAM:** `tests/cobalt/test_replay_runner.py` is also edited by `setups/seven-0921` and `cards/stale-score-0922` (lines ~418 / ~472). This build appended at the end of the file only. The deploy's L68 stacked gate proves it."
5. **Build ESCALATE 3, verbatim:** "**ASK DESK [06:32 / 06:34]: three pre-existing test pins were amended beyond T1–T7.** Each pinned exactly the shape R113 / R114 remove, so no code could satisfy them. T6a `test_the_shipped_k9_…`: expect `[top_n, not_archived eq 0]` → `[top_n]`. T6b `test_k9_passes_a_short_side_…`: `not_archived=1` → stored row PASS; the grading moved to K9.9 / K9.12. T7a `test_smoke_checks_load_through_schema_bad_file_crashes_with_line`: the family set is `K1…K18` minus `K17`. Safe default taken: amended and named. `08` should confirm that no test's intent was widened." — The desk's answer is in `cto-2026-09-24.md` R11 ("the safe default stands; `08`'s file-check reads those three pins as part of the range"). Both checkers had the three pins in the range: Opus THIRD "The three amended pins (T6a, T6b, T7a) each pinned only the shape that R113/R114 remove"; Grok THIRD "T7a only subtracts `K17` from the K1–K18 family pin" and FIFTH "T6a … and T6b … failed in the same red run for the same K9 gate. They are outside T1–T7 and do not make the red commit anything but tests."
6. **Build ESCALATE 4, verbatim:** "**Cosmetic, left untouched (the prompt says nothing else changes):** `s2.yaml:15`'s header list of compare rows `(K8.3, K9.3, K9.6)` does not name K9.9 / K9.12, and `cli.py`'s summary f-string line is ≈160 chars (repo `line-length = 100`)."
7. **Build ESCALATE 5, verbatim:** "**RESTARTS differs from EXPECTED:** the derivation names the residents `com.cobalt.aset` and `com.cobalt.radar` (static import reach of `cobalt.replay.models` / `movers` / `cli` / `runner`), not "no resident". The stacked deploy plan must carry them, restarted inside the 20:00–21:00 pause (L43 / L66)."
8. **"Round 1 covers the mover bars fix + K17 removal only (`<base>..<tip>`) and its three suites' executed output, checked by Opus 5.5 + Grok under his R95 (Sol METER; Gemini out, R96/R97). With both `ready … YES` and `defects that HOLD: 0`, the branch is checked (L67 as he ruled it in R95) and rides the next deploy: 2026-09-24 only if this line is written before 15:00 ET and the desk re-issues `05` as a stacked set (L43 / L68), else 2026-09-25."** (Written 2026-09-24 ≈ 07:0x ET.)
9. **"The deploy's L68 gate re-proves offline, with-DB and live-note on the stacked tree (seam: `tests/cobalt/test_replay_runner.py` with `setups/seven-0921`); the first S2 smoke after the deploy must read a post-deploy replay night (a pre-deploy job row has no `archive_partial_by_side`)."**

MOVER BARS FIX CHECK DONE · round: 1 · opus: CHECK MOVER BARS: FIX STANDS · ready for a deploy prompt: YES · grok: CHECK MOVER BARS: FIX STANDS · ready for a deploy prompt: YES · sol: NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM) · gemini: NOT SEATED (R96/R97) · defects that HOLD: 0 · ESCALATE: 9
