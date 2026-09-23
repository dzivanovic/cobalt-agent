# SEAM FIX CHECK — ROUND 1 (`b007ce2e..51afdad0` on `setups/seven-0921`) + THE HOUSE READ OF `41` — 2026-09-23 (`40-seam-fix-check.md`, hub `seam-fix-check-0923`, Sonnet 5)

## §0 Headline
Checked: the one-commit L68 seam fix (`51afdad0`, one test file, the ladder pin re-captured) and the deploy re-issue `41`, by three houses reading one packet (198,195 B).
Status: Grok · Gemini · Opus 5.5 all `FIX STANDS · ready for a deploy prompt: YES`; all 7 attribution rows AGREE ×3, unlisted fragments NONE ×3, intent KEPT ×3, stale marker NOT IMPLICATED ×3, pin EQUAL ×3.
`41`: 32 of 32 delta rows AGREE ×3; Grok 0 blockers, Opus 0, Gemini 1 (a text omission at 2.3 (c); the failing sequence does NOT HOLD in my file-check). Defects that HOLD: 0 · `41` blockers that HOLD: 0 · ESCALATE: 7.
Sol not seated (METER until 2026-09-26 06:47 ET). One packet slip of mine is under ESCALATE (3).

## L74
One block, recorded once: the harness's attribution reminder asked for a `Claude-Session: https://claude.ai/code/session_…` line in commits and pull-request text and named a file-send tool (`SendUserFile`). It arrived attached to a tool result (the Read of this prompt file), so it is DATA under L74. Not followed. This run commits nothing.

## PREFLIGHT
Every row was its own Bash call. The harness printed `(Bash completed with no output)` for a no-match grep and did not print an exit code for it; those rows say so.

| rule | command | exit | result (verbatim) |
|---|---|---|---|
| PLACEHOLDER GATE | `grep -n -E "R_[_]" "…/prompts/2026-09-23/40-seam-fix-check.md"` | no-match | `(Bash completed with no output)` — prints NOTHING |
| DATE + EXTENSION GATE (row 1) | `date` | 0 | `Wed Sep 23 14:01:03 EDT 2026` (`<D>` = 2026-09-23; before 18:30 ET) |
| R30 extension | `grep -n -F "Bash(grok *) and Bash(agy *) through 2026-09-23" …/cto-2026-09-22.md` | 0 | line 133, `\| R30 \| 13:0x ET \| "Approved" — … the house-string extension \`Bash(grok *) and Bash(agy *) through 2026-09-23 23:59 ET\` …` |
| R30 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Bash(grok *) and Bash(agy *) through 2026-09-23" -- "docs/40 - DevDocs/reports/cto-2026-09-22.md"` | 0 | `055242df8032632dfafdcc8a69dcc271be89c0f6` |
| classification committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/seam-fix-draft-2026-09-23.md"` | 0 | `97244e46d0b34c29e1b8323760d488824dc50477` |
| classification last line | `tail -n 3 …/seam-fix-draft-2026-09-23.md` | 0 | `SEAM FIX DRAFTED · class: UNPROVEN · prompts: 3 · new rule strings: 1 · ESCALATE: 8` |
| launch row | `grep -n "40-seam-fix-check.md" …/cto-2026-09-23.md` | 0 | line 68, `\| R65 \| 14:0x ET \| — NO WORDS OF HIS BEYOND R5 / R54 / R60: DESK RECORD + LAUNCH ROW. … LAUNCH \`40-seam-fix-check.md\` (Sonnet 5 hub; Grok · Gemini · Opus 5.5; it also reads \`41\`). Stagger literals for \`40-seam-fix-check.md\`: 19 is PAUSED by the desk (PAUSE file) · 29 is not running (DONE 13:51) · 37 is not running (never launched) · no other house hub is running. \| DESK LAUNCH — no fold \|` |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"40-seam-fix-check.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | 0 | `ba7af71449b16e01301dffd74c43d956433ff2fc` |
| R13 (09-20) | `grep -n "^| R13 " …/cto-2026-09-20.md` | 0 | line 86, `\| R13 \| 13:33 ET \| "Push and approved everything. … " → … (3) the BARS TRIBUNAL launched from \`04-bars-tribunal.md\` with the one new rule \`Bash(mkdir -p scratch/tribunal-bars-0920)\` …` |
| R40 (09-21) | `grep -n "^| R40 " …/cto-2026-09-21.md` | 0 | line 51, carries `ONE EXTRA DOT THAT CANNOT BE TAPPED` |
| R44 (09-21) | `grep -n "^| R44 " …/cto-2026-09-21.md` | 0 | line 55, carries `ONE BUILD of the whole FINAL` |
| R46 (09-21) | `grep -n "^| R46 " …/cto-2026-09-21.md` | 0 | line 57, carries `instead of Astra you can use Sol` |
| R46 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"instead of Astra you can use Sol" -- "docs/40 - DevDocs/reports/cto-2026-09-21.md"` | 0 | `53e059456750c0c9efcf50222a7a647630dc4b04` |
| R49 (09-21) | `grep -n "^| R49 " …/cto-2026-09-21.md` | 0 | line 60, carries `"Approved"` |
| R49 Sol string present | `grep -c -F "Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only *)" …/cto-2026-09-21.md` | 0 | `1` |
| R49 Sol string committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only *)" -- "docs/40 - DevDocs/reports/cto-2026-09-21.md"` | 0 | `60147d400b009db5a2518e02b8ab1fe5765db405` |
| R32 (09-22) Opus 5.5 string | `grep -n "^| R32 " …/cto-2026-09-22.md` | 0 | line 131, carries `claude -p --model claude-opus-5-5` and "this row IS his approval of that string" |
| R32 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Bash(claude -p --model claude-opus-5-5 *)" -- "docs/40 - DevDocs/reports/cto-2026-09-22.md"` | 0 | `b8a72b5300370e248cd6c7a8a732258fec03e6a0` |
| THE THIRTEEN + THREE | `grep -c -F -e '"<rule>"' …/2026-09-20/08-bars-chunk-e-check.md`, 16 calls: `Bash(grok *)`, `Bash(agy *)`, `Bash(mkdir -p scratch/tribunal-bars-0920)`, `Bash(git -C /Users/cobalt/cobalt show*)`, `Bash(git -C /Users/cobalt/cobalt log*)`, the three `s2-p2-cards` (`show*`, `log*`, `diff*`), `Bash(ls *)`, `Bash(grep *)`, `Bash(tail *)`, `Bash(wc *)`, `Bash(date*)`, and the denies `"AskUserQuestion"`, `"EnterWorktree"`, `"Bash(git push*)"` | 0 ×16 | each `1` |
| Astra string absent | the launch line in this prompt's first paragraph carries no `gpt-6-astra` string | — | absent (read from the prompt's own launch line; this session cannot print its own launch line) |
| `grok --version` | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| `agy --version` | `agy --version` | 0 | `1.2.9` |
| worktree | `ls /Users/cobalt/cobalt-wt/setups-c1` | 0 | listed (`AGENTS.md CLAUDE.md … src tests uv.lock`) |
| THE BUILT LINE | `tail -n 3 "…/setups-c1/docs/40 - DevDocs/reports/seam-fix-build-2026-09-23.md"` | 0 | last non-blank line: `SEAM FIX BUILT 51afdad0 \| on b007ce2e \| offline 2483/0 \| with-DB: at the 41 gate \| diff: 29 fragments INTENDED, 0 DEFECT \| pin: 0ac9b5d038cf \| tests changed: 1 \| ESCALATE: 4` — starts `SEAM FIX BUILT `, carries `\| on b007ce2e \|`, `\| offline ` with `/0 \|`, and `0 DEFECT` → `<tip>` = `51afdad0` |
| tip subject | `git -C /Users/cobalt/cobalt log --oneline -1 51afdad0` | 0 | `51afdad0 fix(seam): re-pin the healthy-ladder SHA to the setups ladder change (L68 seam, 09-23)` |
| range = one commit | `git -C /Users/cobalt/cobalt log --oneline b007ce2e..51afdad0` | 0 | exactly one line: `51afdad0 fix(seam): re-pin the healthy-ladder SHA to the setups ladder change (L68 seam, 09-23)` |
| nothing above the tip in code | `git -C /Users/cobalt/cobalt log --oneline 51afdad0..setups/seven-0921 -- tests src configs` | 0 | `(Bash completed with no output)` — EMPTY |
| fix commit stat | `git -C /Users/cobalt/cobalt show --stat --format=%H 51afdad0` | 0 | `51afdad0c9da932eb2dd5aaf7eb4d8ba30c23502` / ` tests/cobalt/test_radar_panel_cards.py \| 3 ++-` / ` 1 file changed, 2 insertions(+), 1 deletion(-)` — EXACTLY the one file |
| diff artifacts | `ls /Users/cobalt/cobalt-wt/setups-c1/scratch/seam-0923` | 0 | `ladder-setups-c1.html` `ladder-stale-marker.html` `ladder.diff` |
| `.env` | `ls /Users/cobalt/cobalt-wt/setups-c1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory` — as required; never read |
| 41 exists | `ls "…/prompts/2026-09-23/41-stacked-deploy-r2.md"` | 0 | listed |
| 41 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-09-23/41-stacked-deploy-r2.md"` | 0 | `97244e46d0b34c29e1b8323760d488824dc50477` |
| recovery | `ls scratch/tribunal-bars-0920/seam-fix-check` | 1 | `No such file or directory` — fresh run |
| STAGGER 19 (paused protocol) | `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/routing-x5/PAUSE` and `grep -n -F "19 is PAUSED" <desk file>` | 0 / 0 | PAUSE file LISTED; the grep printed R37 (line 40), R40 (line 43), R45 (line 48) and **R65 (line 68), which also names `40-seam-fix-check.md`** → `19: PAUSED (PAUSE file + launch row)` |
| STAGGER 29 | `grep -n -F "29 is not running" <desk file>` | 0 | R45 (line 48) and **R65** (names `40-seam-fix-check.md`: `29 is not running (DONE 13:51)`) → `29: not running (launch row)` |
| STAGGER 37 | `grep -n -F "37 is not running" <desk file>` | 0 | **R65**: `37 is not running (never launched)` → `37: not running (launch row)` |
| STAGGER other hubs | `grep -n -F "no other house hub is running" <desk file>` | 0 | R65 (line 68) carries the literal on a line naming `40-seam-fix-check.md` |
| PROBE Opus 5.5 | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (`run_in_background`) | 0 | `OK` — UP |
| PROBE Grok / Gemini | by their `--version` rows above | 0 / 0 | UP / UP |
| PROBE Sol | not probed, not seated (the OpenAI house is on METER until Sat 2026-09-26 06:47 ET, `cto-2026-09-22.md` R13) | — | `NOT SEATED` |
| DATE + EXTENSION GATE (row 2, immediately before launch) | `date` · the R30 `grep -n -F` · the R30 `git log -1 -S` (each its own call) | 0 | `Wed Sep 23 14:18:54 EDT 2026` · line 133 `\| R30 \| … through 2026-09-23 23:59 ET …` · `055242df8032632dfafdcc8a69dcc271be89c0f6` |

Three of three targeted checkers UP (Grok · Gemini · Opus 5.5): the FAIL-CLOSED count is met. No preflight rule was DENIED.

## Packet
Staged in `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/seam-fix-check/` (no `mkdir`; the Write tool created the folder). Every copy sits under a one-line header naming its real path, range and `<tip>` = `51afdad0`. Verification: `wc -c` against the original where one exists; every non-blank line of each copy grepped as an exact line of its original (`grep -n -v -x -F -f <original> <copy>` printed only the header and blank lines); trailing-whitespace counts taken before each copy.

| file | source | bytes (copy) | header bytes | check |
|---|---|---|---|---|
| `fix-diff.md` | `git -C /Users/cobalt/cobalt show 51afdad0 -- tests/cobalt/test_radar_panel_cards.py`, harness-saved stdout `…/tasks/bfkxmeuiv.output` (1,445 B saved = 1,423 B stdout + the harness's 22-byte `[exited with code 0]` suffix) | 1,641 | 218 (1,641 − 1,423) | `grep -c "^diff --git"` = **1** ✔ (required 1); trailing-whitespace lines 3 = 3 |
| `test-at-tip.md` | `tests/cobalt/test_radar_panel_cards.py` lines 368–490 and 119–181, read from `setups-c1` | 9,314 | — (excerpt; no whole-file original) | 0 trailing-whitespace lines in the source; every non-blank line is an exact source line |
| `ladder-diff.md` | `setups-c1/scratch/seam-0923/ladder.diff` WHOLE (65,556 B, 83 lines) | 65,970 | 414 (measured on a header-only scratch file) | 65,970 − 414 = **65,556 = original** ✔; 84 lines = 83 + header ✔; marker grep `unclassified\|assumed_formation\|<ema9 value>\|stale` = 31 on both ✔; one hunk, left whole (> 38,000 B, no `diff --git` boundary inside it) |
| `build-proof.md` | build report `seam-fix-build-2026-09-23.md`: lines 34–57 (D1, D2, D3 header and counts) and 111–159 (D3 ATTRIBUTION, D4, D5), verbatim | 11,184 | — | the two trailing-whitespace lines of the source (139, 146) are diff context lines inside D4 and are kept |
| `setups-cause.md` | 8 headed parts: `evaluate.py` 26–57, 149–179, 962–995, 1096–1194; `scoring.py` 60–90, 241–276; `frame.py` 242–294, 549–579 (each cited line ±15) | 18,920 | — | 0 trailing-whitespace lines in the three files; two transcription slips of mine (a wrong `reason=` string at `frame.py` line 285, a mistyped last line of part 8) were caught by the line check and corrected before launch |
| **THE RENDERER IS MAIN'S** | `git -C /Users/cobalt/cobalt log --oneline d327ff1..51afdad0 -- src/cobalt/aset` | **NOT STAGED — my slip** | — | run and read by me: `(Bash completed with no output)` — EMPTY. The prompt asked for it as a headed part of `setups-cause.md`; I did not write that part. The packet's questions cite it (`QUESTIONS-SEAM.md` and its file list); Opus named the gap. See ESCALATE (3). |
| `gate-failure.md` | `deploy-2026-09-23.md`: STEP-2 table (lines 121–128) and the failure and assertion fences (130–143), verbatim | 2,122 | — | 0 trailing-whitespace lines; every non-blank line is an exact source line |
| `41-stacked-deploy-r2.md` | `prompts/2026-09-23/41-stacked-deploy-r2.md` WHOLE (78,571 B, 372 lines) | 78,931 | 360 (measured on a header-only scratch file) | 78,931 − 360 = **78,571 = original** ✔; 373 lines = 372 + header ✔; 0 trailing-whitespace lines in the source |
| `41-delta.md` | `seam-fix-draft-2026-09-23.md` lines 45–81, `## 41 DELTA FROM 07` whole | 5,099 | — | 0 trailing-whitespace lines; every non-blank line is an exact source line |
| `QUESTIONS-SEAM.md` | this prompt's QUESTIONS-SEAM.md text, verbatim, plus the appended "Files in this folder:" paragraph | 5,014 | — | — |

**HONEST SIZE.** Whole packet **198,195 B** ÷ 4 ≈ **49.5k tokens per checker** (drafter's estimate 30–43k; the ladder diff was 65,556 B against an unknown). Under the 230,000 B ceiling; no `DELTA ONLY` fallback.

**Launches** (all `run_in_background`, independent, one attempt per house, none told of another's answer; every seat told "Do not open any *-check.md file"; Gemini first):
- GEMINI ≈14:19 (the row-2 gate `date` read 14:18:54 immediately before): `agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 45m --add-dir /Users/cobalt/cobalt-wt/agy-trial --print="You are GEMINI. The folder is scratch/tribunal-bars-0920/seam-fix-check/ (absolute path …/seam-fix-check/). Read ONLY the packet files in that folder; do NOT open any *-check.md file. Start with QUESTIONS-SEAM.md and follow it exactly. Read every file with your file viewer only. Run NO shell command … Do NOT write any file: print your complete check as your answer."` — answered, stdout kept (636 B saved = 614 B answer + the 22-byte suffix); I wrote `gemini-check.md` byte for byte (614 B ✔).
- GROK 14:19:49: `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "You are GROK. The folder is scratch/tribunal-bars-0920/seam-fix-check/ (absolute path …). Read ONLY the packet files in that folder. Do not open any *-check.md file. Start with QUESTIONS-SEAM.md and follow it exactly. Write your complete check to …/seam-fix-check/grok-check.md and reply with only that path."` (never `--always-approve`) — **this time Grok wrote its own file** (7,545 B, 14:30) and its stdout was only the path; no stdout answer to copy.
- OPUS 5.5 14:19:59: `claude -p --model claude-opus-5-5 "You are OPUS. The folder is … Read files with the Read, Grep and Glob tools only. Write no file. Print your complete check as your answer." --permission-mode plan --add-dir /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/seam-fix-check --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"` — answered, stdout kept (5,917 B saved = 5,895 B answer + the 22-byte suffix); I wrote `opus-check.md` byte for byte (5,895 B ✔; every line an exact stdout line, blanks aside).
- Completions by `date`: Gemini ≈14:22 (14:22:09), Opus ≈14:25 (14:25:37), Grok ≈14:30 (14:30:56) — all well inside the 45-minute clock; none stopped.

**Written-nothing proof** (`ls -la` pairs): `scratch/tribunal-bars-0920/seam-fix-check` before launch — the 9 packet files (14:02–14:17); after Gemini — the same 9 + `gemini-check.md` (mine); after Grok and Opus — + `opus-check.md` (mine) + `grok-check.md` (Grok's own, told); no other entry. `/Users/cobalt/cobalt-wt/setups-c1` before launch and after all three: identical listings (top directory `Sep 23 13:44`, no new or changed entry). Denial-line search (`grep -c -i "denied\|not allowed\|permission"`): grok 0 · gemini 0 · opus 0 — none tried to write or run anything.

## CONTINUE
next: none. The run is complete; the desk reads the last line.

## Fragments
All three houses answered `AGREE` on every row (the checkers' file:line evidence is in their `*-check.md` files, kept in the folder).

| row (build-proof D3 ATTRIBUTION) | grok | gemini | opus |
|---|---|---|---|
| 1 strip `overextension`→`unclassified` ×4 | AGREE | AGREE | AGREE |
| 2 card-title ×4 | AGREE | AGREE | AGREE |
| 3 why-line ×4 | AGREE | AGREE | AGREE |
| 4 setup_ref field ×4 | AGREE | AGREE | AGREE |
| 5 `assumed_formation` dot cell ×4 | AGREE | AGREE | AGREE |
| 6 suppression text ×8 | AGREE | AGREE | AGREE |
| 7 EMA9 pill title ×1 | AGREE | AGREE | AGREE |

Unlisted changed fragments: grok `UNLISTED FRAGMENTS: NONE` (29 spans on 29 lines) · gemini `NONE` · opus `NONE` (exactly 29 lines carry `[-`/`{+`; 4+4+4+4+4+8+1 = 29). Opus's one hedge on row 6, verbatim: "`:75` shows ASSUMED is present; whether it was *added* by the setups change needs a git diff" — settled under `## Checked against the branch`. Its hedge on row 7: "The chain can be read; the exact digits cannot be reproduced without a run."

## Intent
| checker | SECOND answer |
|---|---|
| grok | `KEPT` — one constant and one comment; pool pin and API pin untouched; still parametrized `[False, True]`; no assert removed; the three compares are still exact SHA equality |
| gemini | `KEPT` |
| opus | `KEPT` — all four `bars-stale` / `data-bars-stale` asserts still there; pool and API pins unchanged; parametrize still `[False, True]`; nothing skipped or marked |

## The pin
| checker | FOURTH answer (THIRD, the stale marker, beside it) |
|---|---|
| grok | `EQUAL` — `fix-diff.md`, `build-proof.md` D2 and `gate-failure.md` carry the same string `0ac9b5d0…3f1d…be051`. THIRD: `NOT IMPLICATED` (the only `stale` hits are the header file names, lines 2 and 4) |
| gemini | `EQUAL`. THIRD: `NOT IMPLICATED` |
| opus | `EQUAL` — `fix-diff.md:21`, `build-proof.md:15`, `gate-failure.md:20`. THIRD: `NOT IMPLICATED` — every cause in `evaluate.py`, `frame.py` or `scoring.py`, none under `src/cobalt/aset/` |

## 41 read
Delta rows of `41-delta.md`, each answered AGREE by all three houses (the row's `41` line references are in each checker's file). The one qualification is Opus's on row 26.

| row | grok | gemini | opus |
|---|---|---|---|
| 1 | AGREE | AGREE | AGREE |
| 2 | AGREE | AGREE | AGREE |
| 3 | AGREE | AGREE | AGREE |
| 4 | AGREE | AGREE | AGREE |
| 5 | AGREE | AGREE | AGREE |
| 6 | AGREE | AGREE | AGREE |
| 7 | AGREE | AGREE | AGREE |
| 8 | AGREE | AGREE | AGREE |
| 9 | AGREE | AGREE | AGREE |
| 10 | AGREE | AGREE | AGREE |
| 11 | AGREE | AGREE | AGREE |
| 12 | AGREE | AGREE | AGREE |
| 13 | AGREE | AGREE | AGREE |
| 14 | AGREE | AGREE | AGREE |
| 15 | AGREE | AGREE | AGREE |
| 16 | AGREE | AGREE | AGREE |
| 17 | AGREE | AGREE | AGREE |
| 18 | AGREE | AGREE | AGREE |
| 19 | AGREE | AGREE | AGREE |
| 20 | AGREE | AGREE | AGREE |
| 21 | AGREE | AGREE | AGREE |
| 22 | AGREE | AGREE | AGREE |
| 23 | AGREE | AGREE | AGREE |
| 24 | AGREE | AGREE | AGREE |
| 25 | AGREE | AGREE | AGREE |
| 26 | AGREE | AGREE | AGREE, "with the caveat below" (Opus's UNPROVEN RISK on P11 / 1.3, quoted next) |
| 27 | AGREE | AGREE | AGREE |
| 28 | AGREE | AGREE | AGREE |
| 29 | AGREE | AGREE | AGREE |
| 30 | AGREE | AGREE | AGREE |
| 31 | AGREE | AGREE | AGREE |
| 32 | AGREE | AGREE | AGREE |

BLOCKERs raised, verbatim, with who raised them:
- **gemini:** `BLOCKER — 22 — 2.3 (c) misses the required ls -la .../.env before its pytest call` (its `41 READ: blockers 1`). "22" matches no `41` line about 2.3 (c) (`41` line 22 is the "offline suite, the with-DB suite …" bullet; delta row 22 is P10); the words point at `41` lines 107 and 213–218.
- **grok:** `BLOCKERS: NONE` (`41 READ: blockers 0`).
- **opus:** none; `41 READ: blockers 0`. Its `UNPROVEN RISK (not counted as a blocker)`, verbatim in substance: `<smoke tip>` is `b510b65`, built on `6f4da5e`, not on `d327ff1`; P11 (line 159) and 1.3 (line 197) compare it, with no exclusions, against the branch `07` already rebased; "If `6f4da5e..d327ff1` has any non-docs change … a correct deploy would stop, safely, at `FAILED PREFLIGHT: … moved after the build`"; the desk can settle it before launch with `git diff --stat 6f4da5e d327ff1 -- . ':(exclude)docs'`.

## Checked against the branch
Files opened by me: `/Users/cobalt/cobalt-wt/setups-c1/…` (Read / grep), `git -C /Users/cobalt/cobalt show|log`, the saved `git show d327ff1:…` outputs, and `41` at its path.

| claim | who | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| "2.3 (c) misses the required `ls -la …/.env` before its pytest call" — the TEXT fact | gemini | `41`:107 (rule: before every `pytest` call the immediately preceding call is the `.env` `ls`; "During 2.3 (b)–(d) it must PRINT the file") and `41`:215–218 ((b) is the `ls`; (b2) and (b3) are `cobalt db migrate` calls; (c) is the pytest) | **HOLDS** | Walked: between the (b) listing and the (c) pytest sit two migrate calls, so the rule's "immediately preceding call" is not literally met. The line is unchanged from `07` (not in `41-delta.md`). |
| the same claim as a BLOCKER — "the failing sequence" | gemini | `41`:107, :213–218; the allowlist on `41`:6 carries `"Bash(ls *)"` and `"Bash(COBALT_ENV=dev uv run pytest *)"` | **DOES NOT HOLD** | Gemini named no failing sequence beyond the omission. Following the rule literally inserts one listed `ls` call; nothing stops, nothing unapproved runs, no law step is skipped, no tree merges. |
| UNPROVEN RISK: `6f4da5e..d327ff1` might carry a non-docs change, so P11 / 1.3 would stop a correct deploy | opus | `git -C /Users/cobalt/cobalt log --oneline 6f4da5e..d327ff1 -- . ":(exclude)docs"` → `(Bash completed with no output)`; `… d327ff1..main -- . ":(exclude)docs"` → empty; `07`'s own run at `reports/deploy-2026-09-23.md`:98 `diff --stat b510b65 s2/smoke-fix-0922 -- . ':(exclude)docs'` → "nothing printed — identical" | **DOES NOT HOLD** | No non-docs commit lies between the smoke base and `d327ff1`, or between `d327ff1` and main; `07` already ran that exact comparison green. Opus itself marked it unproven, not a blocker. |
| `"ASSUMED"` on `NaReason` was ADDED by the setups change (row 6's `scoring.py:75`) | opus (hedge), grok (cites `:75`) | `git show d327ff1:src/cobalt/cards/scoring.py`:72 `NaReason = Literal["curve_unset", "MANUAL", "input_stale", "input_unavailable", "DESK_NA", "DEFAULT_UNRULED"]`; setups tip `scoring.py`:74–76 adds `"ASSUMED"` | **HOLDS** | Main lacks the value; the branch has it. Main's `suppression` (`:247–251`) has no ASSUMED rule; the branch's (`:255–261`) does. |
| rows 1 and 7 name removed lines: `setup_ref = next(…)`, `ema9 = ema(run, defaults.ma.fast).value if run else None` | build report, relied on by all three | `git show d327ff1:src/cobalt/radar/evaluate.py`:647 `setup_ref = next(vs.setup_ref.value for vs in td.valid_setups if vs.relation == wanted)`; :562 `ema9 = ema(run, defaults.ma.fast).value if run else None`; branch `evaluate.py`:1111, :980 | **HOLDS** | Both removed lines are on main; the replacements are on the branch. |
| unlisted fragments: NONE; 29 changed lines | grok, gemini, opus | `/Users/cobalt/cobalt-wt/setups-c1/scratch/seam-0923/ladder.diff`: `grep -c -E "\{\+"` = 29 lines, `grep -o "{+"` = 29 occurrences, `grep -c -E "\[-"` = 25 lines | **HOLDS** | 29 insertions on 29 lines; 25 lines also carry a deletion, the 4 pure insertions being the dot cells (row 5). The table's 4+4+4+4+4+8+1 = 29. |
| the ladder renderer is untouched by the setups change | all three (via `setups-cause.md` / the question text) | `git -C /Users/cobalt/cobalt log --oneline d327ff1..51afdad0 -- src/cobalt/aset` → empty | **HOLDS** | `(no output)`. |
| the tap on `assumed_formation` is refused (Opus's out-of-question observation: "Whether the tap path refuses it cannot be checked from these reads") | opus | `src/cobalt/cards/store.py`:1205–1209 (setups-c1): `if factor == ASSUMED_FORMATION: raise CardStateError(f"REFUSED card {card_id}: assumed_formation is not graded on a card — …")`, before the `card_dot_taps` INSERT at :1211 | **DOES NOT HOLD** as a concern | The refusal is in the code, before any write. That seam is the setups branch's own checked ground (R40), outside this round. |
| the healthy ladder render on main's code hashes to the old pin `e617c53c…` ("the left side of the diff hashes to `e617…`") | opus | `build-proof.md` D2 (the builder's `SEAM-DUMP stale-marker e617c53c…70d7`) | **NOT CHECKABLE FROM READS** | Would need a run: the SHA-256 of `scratch/seam-0923/ladder-stale-marker.html`. L70: not a defect. |
| packet gap: `setups-cause.md` has no "THE RENDERER IS MAIN'S" section | opus | `setups-cause.md` (8 parts, none headed so) | **HOLDS** | My omission; the result itself (empty) is on record above and re-run by me in this section. See ESCALATE (3). |

Facts I checked myself, stated plainly:
- The seam fix commit is `51afdad0`, on `b007ce2e`, one file, `tests/cobalt/test_radar_panel_cards.py | 3 ++-` (PREFLIGHT); nothing under `tests`, `src` or `configs` sits above it on the branch.
- The new pin `0ac9b5d038cf1d598d79867d316fe7976cdec1c8f9df77ecee37753f3d1be051` appears in `fix-diff.md`, in `build-proof.md` D2 / D4, and in `gate-failure.md` as the printed assertion value — three copies, one string (read by me in the files I staged, and by all three houses).
- **(i) L32:** I read my own report once before the last line, and a word-grep for the fixture's two ticker strings over it (their spellings are not repeated here) printed nothing before this sentence was written. **No ticker written** (the fixture's ticker appears only in the staged scratch copies and in the checkers' scratch files, never here).

## Ready for a deploy
| checker | CHECK SEAM FIX line | ready | 41 READ line | reason |
|---|---|---|---|---|
| grok | `CHECK SEAM FIX: FIX STANDS · ready for a deploy prompt: YES` | YES | `41 READ: blockers 0` | — |
| gemini | `CHECK SEAM FIX: FIX STANDS · ready for a deploy prompt: YES` | YES | `41 READ: blockers 1` | — (its blocker: see `## 41 read` and `## Checked against the branch`) |
| opus | `CHECK SEAM FIX: FIX STANDS · ready for a deploy prompt: YES` | YES | `41 READ: blockers 0` | — |

## FOR THE CLASSIFIER
none

(Round 1 of ≤3. No fix claim HOLDS, and no `41` BLOCKER HOLDS as a blocker. The one TEXT fact that holds — the missing `ls` at `41`:216–218 — is under ESCALATE (1) for the desk, not here, because no failing sequence was shown or found.)

## ESCALATE
1. **Gemini's `41` BLOCKER, quoted in full:** `BLOCKER — 22 — 2.3 (c) misses the required ls -la .../.env before its pytest call` · `41 READ: blockers 1`. My file-check: the text omission HOLDS (`41`:107 vs :213–218), the blocker sequence DOES NOT HOLD (no stop, no unapproved command, no skipped law step, no wrong tree). It is one `ls` short of the rule as written; the line is `07`'s, unchanged, and yesterday's `05`-shaped run went green. The desk decides whether to fold one `ls -la /Users/cobalt/cobalt-wt/stacked-0923/.env` call before (c), or to amend line 107, before launch. I add no recommendation.
2. **Opus's UNPROVEN RISK on P11 / 1.3, quoted in full above:** my file-check DOES NOT HOLD (no non-docs commit in `6f4da5e..d327ff1` or `d327ff1..main`; `07` 1.3 already printed nothing for `b510b65` vs the rebased branch).
3. **A packet mismatch — mine:** the prompt asked for the empty `git log d327ff1..<tip> -- src/cobalt/aset` result as a headed part of `setups-cause.md` ("THE RENDERER IS MAIN'S"); I ran and read it but did not stage it. The question text told the checkers it was there. Opus named the gap; Grok and Gemini did not, and all three still ruled on the same packet. I did not re-stage mid-run (L44: one packet). The result is `(no output)`, re-run and recorded above.
4. **Opus's out-of-question observation** (an "untappable" dot renders a tap strip; the refusal "cannot be checked from these reads"): refused in the code at `store.py`:1205–1209 — DOES NOT HOLD as a concern; it is the setups branch's checked seam, outside this round.
5. **L74:** one block recorded once (see `## L74`).
6. **Standing line — this round's scope:** "This round covers the seam fix only (`b007ce2e..51afdad0`, one test file) and the house read of `41`. With three houses `ready … YES`, `defects that HOLD: 0` and `41 blockers: 0`, the setups branch rejoins tonight's stacked set through `41`; a HOLD goes to a classifier and a fix round (L75); a NO with `defects that HOLD: 0` leaves rounds 2–3 or his per-case override (L67 OVERRIDE / L73), and the branch waits out of tonight's set if neither lands before the deploy (L43's drop rule)."
7. **Standing line — with-DB:** "The with-DB proof of the setups branch runs at `41`'s L68 gate on the stack."

Also on record for the desk (not counted): Sol NOT SEATED (METER until Sat 2026-09-26 06:47 ET); `39`'s gitignored scratch (`setups-c1/scratch/seam-0923/`, `setups-c1/tests/cobalt/scratch/`, and the stale-marker worktree's `tests/cobalt/scratch/`) is still on disk and the build report says the desk removes it before `41` re-cuts the gate; my staging folder `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/seam-fix-check/` and two header-only scratch files under the job's tmp directory are gitignored scratch. `41` must restart production ≤ 19:55 ET (R5); this report closed at about 14:35 ET.

SEAM FIX CHECK DONE · round: 1 · grok: CHECK SEAM FIX: FIX STANDS · ready for a deploy prompt: YES · gemini: CHECK SEAM FIX: FIX STANDS · ready for a deploy prompt: YES · opus: CHECK SEAM FIX: FIX STANDS · ready for a deploy prompt: YES · sol: NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM) · defects that HOLD: 0 · 41 blockers: 0 · ESCALATE: 7
