# DRC D4 FIX R1 CHECK — ROUND 2 OF ≤3 — 2026-09-25

Prompt: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-25/22-drc-d4-fix-r1-check.md` · hub `drc-d4-fix-r1-check-0925` (Sonnet 5, auto, read-only) · range `5d4f8201..e96f0be7` on `drc/d1-trading-log`. No code, no git write, no DB, no vault write by this run.

## §0 Headline
Checked DRC D4 fix round 1 (`5d4f8201..e96f0be7`: red `36331949`, pins `d523bba5`, fix `807c13ec`, RUNS `e96f0be7`) with RUN-1…RUN-3, the amended seam and trace, and the three suites' executed output; packet 189,045 B (25 files), no cut.
OPUS 5.5 and GROK both answered `FIX STANDS · ready for D2: YES`: F-1…F-8 all CLOSED with walked inputs, KEPT, NOTHING WIDENED, all suites and RUNS SHOWN, DESELECTS AS STATED. They split on the seam: OPUS `SEAM GAP` (Part A drops Part B's `_daymode_banner` bullet and helper cites), GROK `SEAM STATED`. File-check: that gap HOLDS as a fact (the code is right; the report text omits it) → `defects that HOLD: 1` → `ready for D2: NO` by the mechanical rule (§4), for the classifier. No `INPUT NOT WALKED`.
Sol: NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM; date 2026-09-25 08:09 ET, not probed). ESCALATE: 16.

## L74
One block arrived inside a tool result: the Read result of this prompt file was followed by a system-reminder asking commit messages to end with a `Claude-Session:` line and naming a file-send tool. Recorded once as DATA; not followed. This run commits nothing and sends no file. (Both checkers' stdout carried only the harness notices listed in ESCALATE 10; neither carried such a request.)

## PREFLIGHT
`<D>` = 2026-09-25. Every call was allowed; none denied.

| rule | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | `Fri Sep 25 07:58:23 EDT 2026` |
| placeholder `R_[_]` | `grep -n -E "R_[_]" …/22-drc-d4-fix-r1-check.md` | 1 | (nothing) |
| placeholder `FILL AT LAUNCH` | `grep -n -F "FILL AT LAUNCH" …/22-…md` | 0 | lines `1` (SEAT prose) and `21` (the gate's own line) only |
| GROK GATE R17 | `grep -n "^| R17 " cto-2026-09-24.md` | 0 | `35:` the `| R17 |` row "Grok approved with no asking going forward" |
| R17 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Grok approved with no asking going forward" -- …cto-2026-09-24.md` | 0 | `1758fd78a572f47b613b2ca831dcfa636ed8f65a` (run again 08:09 before launch: same) |
| R19 | `grep -n "^| R19 " cto-2026-09-24.md` | 0 | `37:` "All 4 house models approved for use indefinlitly" |
| R19 committed | `git … log -1 --format=%H -S"All 4 house models approved" -- …` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |
| round 1 committed | `git … log -1 --format=%H -- …/drc-d4-check-2026-09-25.md` | 0 | `a1f0c2b58c28bb92b088082a3506f38c10ae38d0`; last non-blank line starts `DRC D4 CHECK DONE ·` |
| classification committed | `git … log -1 --format=%H -- …/drc-d4-fix-r1-draft-2026-09-25.md` | 0 | `5c1eaed8cee28c27bdf37ebe07ea65b18fd6d6b7`; last non-blank line starts `DRC D4 FIX R1 DRAFTED ·` |
| THIS launch | `grep -n "22-drc-d4-fix-r1-check.md" cto-2026-09-25.md` | 0 | `39:` (`| R31 |`, `20`'s row — not counted), `56:` `| R48 | 07:58 ET |` (this launch), `76:` (`21`'s builder row) |
| launch row committed | `git … log -1 --format=%H -S"22-drc-d4-fix-r1-check.md" -- "…cto-2026-09-2*.md"` | 0 | `adf0ee1ba0b4e4ed659cdc29644d4f3442990ec7` |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| worktree | `ls /Users/cobalt/cobalt-wt/drc-d1` | 0 | listed |
| THE BUILT LINE | `tail -n 3 …/drc-d4-fix-r1-build-2026-09-25.md` | 0 | last non-blank: `DRC D4 FIX R1 BUILT e96f0be7 \| on 5d4f8201 \| red 36331949 \| offline 2520/0 \| with-DB 2980/0 \| live-note 142/0 \| .env: removed \| 0018: rolled back \| FIX: 8 \| RUNS: 3 \| ESCALATE: 15` — every required token present; no `0018: UNPROVEN` |
| tip subject | `git … log --oneline -1 e96f0be7` | 0 | `e96f0be7 test(drc): D4 fix r1 RUNS — the store joins the suite rollback, a refused field logs no typed value (L70)` |
| range | `git … log --oneline 5d4f8201..e96f0be7` | 0 | EXACTLY the six lines expected (RUNS `e96f0be7`, fix `807c13ec`, pins `d523bba5`, red `36331949`, then docs-only `8b6518a8`, `facdfc93`); non-docs commits = 4; no resume commit |
| nothing above tip | `git … log --oneline e96f0be7..drc/d1-trading-log -- src tests configs` | 0 | (empty) |
| path union | `git … log --stat --format=%h 5d4f8201..e96f0be7` | 0 | 11 paths, EXACTLY the expected set: `src/cobalt/{aset/web,settings/card,settings/cli}.py`; `tests/cobalt/{test_drc_d4_fix_r1,test_drc_d4_fix_r1_runs,test_card_settings,test_drc_settings,test_drc_settings_db}.py`; DevDocs `settings/card.md`, `settings/cli.md`; the D4 build report. No migration, `configs/`, `src/cobalt/cli.py`, `drc/`, `store.py`, `models.py`, `settings/drc.py`, `prefill/`, `radar/`, `cards/`, `aset/engine.py`, and `aset/web.md` not in range. |
| report headers | `grep -n "^## " …/drc-d4-fix-r1-build-2026-09-25.md` | 0 | the 18 headers in the prompt's order at lines 3, 9, 12, 28, 56, 66, 77, 83, 155, 162, 165, 169, 176, 195, 200, 212, 221, 224; no `(run 2)` section |
| L3 / L32 sweep | `grep -rn -F ".put(" …/src/cobalt/settings` · `grep -n -F "store.put(" …/card.py` · `grep -n "sha256 {}" …/cli.py` · `grep -rn "VaultWriter" …/src/cobalt/settings` | 0 / 1 / 1 / 1 | ONE hit `settings/cli.py:104` (`outcome = store.put(rows, source=source, **extra)`, inside `apply_settings`); then none; none; none — as expected |
| `.env` | `ls /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `No such file or directory` |
| recovery | `ls scratch/tribunal-bars-0920/drc-check/d4-fix-r1` | 1 | `No such file or directory` — fresh run |
| stagger | `grep -n -F "no other house hub is running" cto-2026-09-25.md` | 0 | the R48 row (line `56`) carries the literal AND names `22-drc-d4-fix-r1-check.md` |
| probe OPUS | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (background) | 0 | `OK` |
| Sol | keyed on `date` (2026-09-25 07:58 ET, before 2026-09-26 06:47) | — | `sol: METER — retry after Sep 26th, 2026 6:47 AM (15 / 37's record)` — not probed, not launched |

## Packet
`/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/drc-check/d4-fix-r1/` — 25 files staged by Write from Read of the real files (git outputs taken `run_in_background` and Read from the saved stdout); no `mkdir`; no part over 15,000 B.

| file set | parts | bytes (measured `wc -c`) | proof |
|---|---|---|---|
| `fix-diff.part1…3.md` | 3 | 31,386 (max part 12,918) | `grep -c "^commit "` over the parts = 2 + 1 + 1 = 4 = the non-docs commit count; `grep -c "^diff --git"` = 5 + 1 + 2 = 8 = the non-docs path-touches `--stat` shows (1+4+1+2); trailing-whitespace lines 10 + 9 + 16 = 35 = the original's 35. The saved original was 30,530 B; the 856 B difference is the three one-line headers plus the harness trailer — header bytes not separately measured. |
| `devdocs-diff.md` | 1 | 3,800 | trailing-whitespace lines 6 = the original's 6; the saved original was 3,557 B (header + harness trailer make the rest) |
| `code-at-tip.part1…5.md` | 5 | 54,174 (max 12,740) | REAL-line slices from `/Users/cobalt/cobalt-wt/drc-d1/` (`cli.py` 1–35, 66–118; `card.py` 279–336; `store.py` 60–117; `web.py` 745–746, 1258–1295; `test_card_settings.py` 1–56, 129–192; `test_drc_settings.py` 1–123, 136–166, 247–307, 374–562; `test_drc_settings_db.py` 1–323 whole; `conftest.py` 81–131, 133–253); trailing whitespace 0 in every source file and every slice. One transcription slip of mine (the `SessionBlocked` return at `web.py:1286` written without `f"{exc}\nNothing written."`) was found on re-read and corrected before any checker launched. |
| `build-proof.part1…4.md` | 4 | 21,848 | F2, F3, F4 whole, RESTARTS, CORRECTIONS, ESCALATE + the stop line verbatim (the report has no trailing whitespace: 0 = 0) |
| `runs.md` | 1 | 3,117 | `## F5 THE RUNS` whole; every RUN carries its executed result; RUN-3 carries a hit count and a path only, no value |
| `suites.md` | 1 | 6,011 | F1, F6, F7, F8 whole, each with its summary line; the four deselect ids listed with my own greps: `test_tenancy.py:697`, `:710`, `:263`, `test_migrate_proof.py:306` |
| `seam.md` | 1 | 8,995 | Part A (the fix report's `## SEAM FOR D2` + `## FOR D3`), Part B (the D4 report's, marked SUPERSEDED) |
| `round-1.part1…5.md` | 5 | 33,635 | round 1's `## Per row`, `## Checked against the branch`, `## FOR THE CLASSIFIER`, `## ESCALATE`; the classification's table (2 parts) and `## SEAM` |
| `rules.part1…3.md` | 3 | 17,348 | `05`'s SEAM paragraph + `## THE ROWS` + `NOT IN D4`; `21`'s AMENDED D4-4 TRACE under its replacement header; v2 REAL lines 176–178, 181, 200, 204; the R95 / R96 / R101 / R102 rows |
| `QUESTIONS-DRC-D4-FIX-R1.md` | 1 | 8,731 | verbatim + the one "Files in this folder:" paragraph |

**HONEST SIZE:** measured sum of the 25 staged files = **189,045 B** → ÷ 4 ≈ **47,261 tokens** per checker; ceiling 300,000 B not reached; no cut (no `rules.md` part cut). Same folder for both checkers (L44); the checkers' own `opus-check.md` (9,061 B) and `grok-check.md` (9,193 B) came after.

## CONTINUE
DONE. Launched OPUS 08:09:5x ET and GROK 08:10:00 ET (each inside the 45-minute clock: OPUS answered before 08:17, GROK wrote its file by 08:21); collated; no relaunch; Sol not seated.
Written-nothing proof: `ls -la` of the packet folder before the launches (25 staged files) and after each checker — the only new files are `opus-check.md` (written by this hub from OPUS's stdout) and `grok-check.md` (written by GROK, as its launch line told it to); `ls -la /Users/cobalt/cobalt-wt/drc-d1` before and after — the directory's mtime stayed `Sep 25 07:34`. No checker wrote any other file.
Harness lines recorded, not copied into `opus-check.md`: the deny-rule syntax notice and the `no stdin data received in 3s` warning on OPUS's stdout; `[exited with code 0]`. GROK's stdout carried only its progress sentences and the path.

## Rows
`F · opus · grok · sol` (FIRST, verbatim ≤30 words, walked input included). Sol: NOT SEATED.

| row | opus | grok | sol |
|---|---|---|---|
| F-1 | "CLOSED — `tests/cobalt/test_drc_d4_fix_r1.py:21` (spy, asserts `:46`–`:52`) exercises `src/cobalt/settings/card.py:322` → `src/cobalt/settings/cli.py:76` (the `put` at `:104`)." | "CLOSED — `tests/cobalt/test_drc_d4_fix_r1.py:46` exercises `src/cobalt/settings/card.py:322` (the call is `…:44`; `apply_settings` then `store.put` at `src/cobalt/settings/cli.py:104`)." | — |
| F-2 | "CLOSED — `tests/cobalt/test_drc_settings_db.py:74` writes the constructed set … reads it back through the **unpatched** `web_module.load_sheet_modes_config()` (`:99`–`:101` …), then posts `/size` (`:134`)." | "CLOSED — `tests/cobalt/test_drc_settings_db.py:100` exercises `src/cobalt/aset/web.py` `load_sheet_modes_config` (unpatched), then `tests/cobalt/test_drc_settings_db.py:134` posts `/size`." | — |
| F-3 | "CLOSED — `tests/cobalt/test_drc_settings_db.py:284` sends a valid two-key payload through `web.py:1280` → `cli.py:104` → `store.py:109`–`:110`. The raise fires after the upsert loop." | "CLOSED — `tests/cobalt/test_drc_settings_db.py:315` exercises `src/cobalt/settings/store.py:110`. … `constructed failure` can appear only if `before_commit` ran; that hook is after both upserts." | — |
| F-4 | "CLOSED — `tests/cobalt/test_drc_settings.py:280` walks `src/cobalt` with `_second_readers` (`:258`–`:276`) … Negative control: `:293`–`:303`. Residual routes …: ESCALATE 2." | "CLOSED — `tests/cobalt/test_drc_settings.py:280` exercises `tests/cobalt/test_drc_settings.py:258` (`_second_readers`), and the negative control `…:293` fails unless the walk names …" | — |
| F-5 | "CLOSED — `tests/cobalt/test_drc_settings.py:153` (`:160`–`:166`) exercises `src/cobalt/settings/models.py:199` (`DrcKey.validate` …). Whether each typed value is the model's *declared* type is NOT CHECKABLE FROM READS" | "CLOSED — `tests/cobalt/test_drc_settings.py:162` exercises `src/cobalt/settings/models.py:199` (`DrcKey.validate` …). Expected types are literals in the table … not `type(got)`." | — |
| F-6 | "CLOSED — `tests/cobalt/test_drc_settings.py:512` (`:518`) exercises `src/cobalt/settings/cli.py:109`–`:110`, rendered through `web.py:1287`–`:1288` / `:745`–`:746`. A generic FAILED … fails `:518`." | "CLOSED — `tests/cobalt/test_drc_settings.py:518` exercises `src/cobalt/settings/cli.py:110` (the read-back `TraderSettingsError`) via `src/cobalt/aset/web.py:1287` and `…:745`." | — |
| F-7 | "CLOSED — `drc-d4-fix-r1-build-2026-09-25.md:197`–`:198` against `drc-d4-build-2026-09-25.md:85` (12 items …, sum 49 = `:130`) and `:217` / `:219`, superseded by `:153`, `:166`, `:172`, `:185`." | "CLOSED — report only … the correction against round 1's HOLD 6 / HOLD 7 and the base `tests/cobalt/test_drc_settings.py` items at `5d4f8201` (`:366` … `:472` = 12). `26+3+3+4+12+1 = 49`" | — |
| F-8 | "CLOSED — `tests/cobalt/test_drc_settings.py:538` exercises `src/cobalt/settings/cli.py:113`–`:117`: keys, deletes, source kind (`:115`), time. Negative controls: `:544`–`:545`. The reversal is at `:560` … a tightening." | "CLOSED — `tests/cobalt/test_drc_settings.py:560` exercises `src/cobalt/settings/cli.py:113`–`:115`. Red on `36331949` was `:560` … The log names keys, deleted keys, the source kind up to `@sha256:`, and the time." | — |

Every answer of both houses names a walked input (test `real path:real line` and the code line it exercises): 0 × `INPUT NOT WALKED`.

## Intent
| checker | SECOND answer |
|---|---|
| opus | "KEPT. Only one assertion changed direction, the named reversal (`test_drc_settings.py:560`), and it tightens. Every other assertion edit is additive or stricter (F-4, F-5, F-8 loop)." |
| grok | "KEPT. No D4 assertion removed or loosened beyond that one reversal (`tests/cobalt/test_drc_settings.py:560`) and the one setup change (`tests/cobalt/test_card_settings.py:173`, `:189`). No new skip and no `xfail`" |

## Scope
| checker | THIRD answer |
|---|---|
| opus | "NOTHING WIDENED. The source edits are `web.py` (one docstring line, `:1268`), `settings/card.py` and `settings/cli.py`; the rest is tests and the two DevDocs. The diff over migrations, `configs` … is empty." |
| grok | "NOTHING WIDENED. Source diff is `src/cobalt/settings/card.py`, `src/cobalt/settings/cli.py`, and one docstring line in `src/cobalt/aset/web.py:1268`. … No D2 route and no D3 build." |

My PREFLIGHT path-union facts agree: 11 paths, exactly the expected set; `git log --oneline 5d4f8201..e96f0be7 -- <the empty-list paths>` printed nothing (see `## Checked against the branch` (ii)).

## Seam
| checker | SIXTH answer |
|---|---|
| opus | "SEAM GAP. … Part A (`drc-d4-fix-r1-build-2026-09-25.md:200`–`:219`) supersedes Part B but silently drops Part B's bullet (`drc-d4-build-2026-09-25.md:194`) … `_daymode_banner`'s call to `_settings_daily_form()`" |
| grok | "SEAM STATED. Amended caller list matches the slices … `## FOR D3` is the same four bullets plus the one line that the reader diff is empty. AMENDED D4-4 TRACE matches the log … NOT CHECKABLE FROM READS — `cmd_load_optional` `cli.py:237` and `cmd_load` `cli.py:317`" |

## Suites
| suite | opus | grok | sol |
|---|---|---|---|
| offline | "SHOWN — `2520 passed, 470 skipped, 1 xfailed, 15 warnings in 70.27s`; `.env` absent; 2516+4 / 467+3 reconcile." | "SHOWN — `2520 passed, 470 skipped, 1 xfailed, 15 warnings in 70.27s (0:01:10)`; 0 failed; `.env` absent before the run." | — |
| with-DB | "SHOWN — `2980 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 149.25s`; `.env` removed and shown gone; 0016/0018 absence probe `assert 28 == 32`, short by 4." | "SHOWN — `2980 passed, 6 skipped, 4 deselected, 1 xfailed …`; 0 failed; `.env` removed and proven gone; absence probe … short by 4; `0016` + `0018` rolled back" | — |
| live-note | "SHOWN — `142 passed, 1 skipped, 15 warnings in 10.02s`; the only skip is the known `test_replay_line.py:256`." | "SHOWN — `142 passed, 1 skipped, 15 warnings in 10.02s`; 0 failed; the one skip is the known vault skip, none naming `COBALT_LIVE_VAULT_ROOT`." | — |
| deselects | "DESELECTS AS STATED: `test_tenancy.py:697` and `:710` (the class), `:263`, `test_migrate_proof.py:306` = 4." | "DESELECTS AS STATED — three deselects, four tests: `…test_tenancy.py:697`, `:710`, `:263`, `tests/cobalt/test_migrate_proof.py:306`." | — |

Myself, from the build report `/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-d4-fix-r1-build-2026-09-25.md` (not the packet copy):
- offline (F7, line 166): `2520 passed, 470 skipped, 1 xfailed, 15 warnings in 70.27s (0:01:10)` — `<f>` = 0, "0 errors" written; the `.env` line before it reads `No such file or directory`. Baseline (F1, line 61): `2516 passed, 467 skipped, 1 xfailed, 15 warnings in 69.49s (0:01:09)`; 2520 = 2516 + 4 (F-1 ×2, the F-4 control, RUN-2) and 470 = 467 + 3 (F-3, RUN-1 ×2), as line 167 states.
- with-DB (F8 (c), line 172): `2980 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 149.25s (0:02:29)` — `<df>` = 0, "0 errors" written, deselected 4 (expected 4); the 6 SKIPPED lines name `test_cards_picks.py:383`, `:396`, `test_radar_evaluate.py:691`, `test_replay_line.py:256`, `test_catalyst.py:365`, `test_predicate.py:262` only.
- live-note (F6, line 163): `142 passed, 1 skipped, 15 warnings in 10.02s` — 0 failed, 0 errors; SKIPPED lines 1 (`grep -c "SKIPPED"` → 1), `tests/cobalt/test_replay_line.py:256 … COBALT_TEST_LIVE_DRC … not set`; NONE names `COBALT_LIVE_VAULT_ROOT` (expected none).
- deselected ids as the build names them (F8, line 170) = the four at `:697`, `:710`, `:263`, `:306`; my own greps in `/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/` read the same four lines (`test_tenancy.py:697`, `:710`, `:263`; `test_migrate_proof.py:306`).
- absence probe (F8 (c2), line 173): `1 failed in 5.65s`, `E       assert 28 == 32` — short by exactly 4, the KNOWN shape → `0016 + 0018: rolled back`.
- `.env: removed, proven gone` is written for F3 (line 80), F5 (line 157) AND F8 (line 174).
- the stop line carries `0018: rolled back`; `grep -n -F "0018: UNPROVEN"` on the report printed nothing.

## Runs
| run | opus | grok | sol |
|---|---|---|---|
| RUN-1 | "RESULT SHOWN — green (`3 passed in 0.24s`, none skipped). It depends on definition order (`test_drc_d4_fix_r1_runs.py:33`, `:45`)." | "RUN-1 RESULT SHOWN — green (with-DB `3 passed`: the row is read back inside the writing test and absent in the next)." | — |
| RUN-2 | "RESULT SHOWN — green; 0 messages captured, so it holds trivially (`:59`–`:76`)." | "RUN-2 RESULT SHOWN — green (0 captured messages; offline `1 passed, 2 skipped`; with-DB passed)." | — |
| RUN-3 | "RESULT SHOWN — **1 hit**, one tracked file under `docs/00 - Project/`, left for the desk's redaction." | "RUN-3 RESULT SHOWN — 1 hit, as stated (`docs/00 - Project/INCIDENT-2026-09-03-notes.md`); not a pytest red; not edited." | — |

Myself, from the build report (`## F5 THE RUNS`, lines 155–160):
- RUN-1 (line 157): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_d4_fix_r1_runs.py` → `3 passed in 0.24s` (none skipped) — GREEN, no `xfail` (line 156: "No test was red → NO `xfail` mark added").
- RUN-2 (line 158): offline `1 passed, 2 skipped in 0.18s`, captured stdout `RUN-2 captured messages: 0`; with-DB PASSED — GREEN; the build's own note: 0 captured means the refusal path logs nothing, so the assertion "holds trivially on this path".
- RUN-3 (line 159): "**old literal outside configs/src/tests: 1 hits**" — path `docs/00 - Project/INCIDENT-2026-09-03-notes.md` (tracked, last commit `b0fd2e41`); the figure-alone search names the same one path. Hit count 1, paths 1. A RESULT for the desk's redaction (ESCALATE 7); no value written by the build or by me.

## Reds and pins
From the build report:
- F2 (line 69): `3 failed, 68 passed, 1 skipped in 0.38s`. The three failures (lines 70–72): `test_the_card_apply_writes_through_the_one_apply_function` — `the card apply bypassed apply_settings: []` / `assert 0 == 1` (`test_drc_d4_fix_r1.py:46`); `test_the_settings_package_has_one_caller_of_put` — `a second caller of .put( in settings/: ['card.py']` (`:68`); `test_no_log_line_carries_a_value` — `assert '2538de05a8b...6cda5399524b' not in 'settings ap...6:28+00:00\n'` (`test_drc_settings.py:560`, the named reversal). Facts: the reds are EXACTLY the three named tests (F-1 ×2, F-8); I read the real lines `test_drc_d4_fix_r1.py:46` (`assert len(calls) == 1 …`) and `:68` (`assert set(callers) == {"cli.py"} …`) in the tree.
- PINS (F2 line 74 and F3 line 80): F-4 `test_one_reader_of_the_daily_stop_and_the_grade_dollars` + control `test_the_one_reader_walk_flags_a_second_reader`; F-5 the 12 rows; F-6 `test_saved_only_after_the_read_back_equals_the_payload` — all "GREEN on the base (in the 68 passed)"; F-2 and F-3 in the with-DB `7 passed in 0.43s`, every test PASSED, none SKIPPED. No PIN went red (build ESCALATE 14: "PINS red on the base: NONE").
- Negative controls, as the tree shows them: F-2 the `!=` assertion against the offline `full.B` (`test_drc_settings_db.py:101`); F-3 the flag-cleared second post (`:318`–`:323`); F-4 `test_the_one_reader_walk_flags_a_second_reader` (`test_drc_settings.py:293`); F-8 the two `_leaks` asserts (`:544`–`:545`). For F-5 and F-6 the tree holds no separate control test (`test_drc_settings.py:136`–`:166`, `:512`–`:519`) although build ESCALATE 14 says "each with its negative control" — a fact carried to ESCALATE 5.

## Checked against the branch
Files read under `/Users/cobalt/cobalt-wt/drc-d1/` at tip `e96f0be7` (Read tool / greps); `git -C /Users/cobalt/cobalt show`/`log` for the range. No `NOT CLOSED`, `WEAKENED`, `WIDENED`, `NOT SHOWN`, `DESELECTS OPEN` or `INPUT NOT WALKED` came from either house; the one verdict-bearing claim is the SEAM GAP.

| # | claim · who · file:line | verdict | ≤30 words |
|---|---|---|---|
| 1 | SEAM GAP: "Part A … silently drops Part B's bullet (`drc-d4-build-2026-09-25.md:194`) … `_daymode_banner`'s call to `_settings_daily_form()` … Part A also drops the inner-helper cites `:1192` / `:1219`" · opus · `drc-d4-fix-r1-build-2026-09-25.md:200`–`:210` vs `drc-d4-build-2026-09-25.md:191`–`:199` | HOLDS | D4 report `:193` names `_settings_daily_form` `:1192` / `_settings_daily_review` `:1219`, `:194` the `_daymode_banner` call; fix report's `## SEAM FOR D2` lists neither. Code bears it: `web.py:565`, `:622` call it, def `:1192`. |

Contradiction, quoted, smoothed neither way: opus "SEAM GAP" vs grok "SEAM STATED. Amended caller list matches the slices … `## FOR D3` is the same four bullets plus the one line …". Both are consistent with the code; the difference is what each counts as the seam (the prompt's SEAM STATED conditions — the amended caller list's `file:line`s, `## FOR D3` unchanged, the amended trace — all hold: I read `cli.py:76`, `:237` (the `cmd_load_optional` call), `:317` (the `cmd_load` call), `card.py:279` / `:322`, `web.py:1258` / `:1280`, `:1298`, `:1507`, `:1141` in the tree and they match; the omitted bullet is one the prompt's conditions do not list).

Checker observations under a CLOSED / KEPT verdict (no NOT CLOSED attached; each walked, listed in ESCALATE 3–6, not counted in `defects that HOLD`):
- F-2 residual (opus): `test_drc_settings_db.py:99`–`:101` (the loader assertions) precede the `monkeypatch` calls (`:119`–`:133`); the `/size` assertions (`:135`–`:137`) test `<div class="shares">` and `shares</span>` only, no dollar figure. As a fact it holds; `/size` reads the loader from `aset/web.py:974`.
- F-4 residual (opus): `test_drc_settings.py:275` restricts the `sheet_modes` check to `rel.startswith("drc/")`; `prefill/drc.py` carries `load_sheet_modes_config` at `:49`, `:380` and `sheet_modes_cfg` at `:248`–`:257`, `:405`, `:408` (grep in the tree). Those are the OLD DRC prefill's reads, unchanged by the range (`git diff` over `src/cobalt/prefill` empty) and not flagged by the walk. The walk is `*.py` only (`_py_files`, `:247`–`:248`).
- F-5 / F-6 negative controls (opus ESCALATE 4): see `## Reds and pins`; no separate control exists for either in the tree.
- `settings/card.py:10`–`:16` docstring (opus ESCALATE 5 / build ESCALATE 12): still reads "its trace is the command, hash and time" and does not name `apply_settings` — read in the tree, true; the build listed it as not a named F-1 line.
- opus / grok NOT CHECKABLE items, my reads: `cli.py:237` and `:317` are `apply_settings(` call lines (read); the `--card` dispatch sits at `cli.py:250`–`:258`; `radar/notes.py` has exactly one `.put(` at `:747` (grep); `TraderSettingsStore` is referenced in 14 `src/cobalt` files (grep -l), of which only `settings/cli.py` and `radar/notes.py` call `.put(`; whether `assert_writable` logs on a refusal, and whether each typed value is the model's declared type, are NOT CHECKABLE FROM READS (I did not read `session/guard.py` or `models.py`).

Own calls:
- (i) SWEEP hits (PREFLIGHT): exactly ONE `.put(` under `settings/` (`cli.py:104`, inside `apply_settings`); none in `card.py`; none for `sha256 {}`; none for `VaultWriter` under `settings/`.
- (ii) `git -C /Users/cobalt/cobalt log --oneline 5d4f8201..e96f0be7 -- src/cobalt/db_migrations src/cobalt/cli.py configs src/cobalt/drc src/cobalt/settings/store.py src/cobalt/settings/models.py src/cobalt/settings/drc.py src/cobalt/prefill src/cobalt/radar src/cobalt/cards src/cobalt/aset/engine.py` → EMPTY.
- (iii) `grep -rn "apply_settings" …/src/cobalt` → `settings/card.py:322` (`cmd_load_card`'s call); `settings/cli.py:11` (module docstring), `:76` (the definition), `:237` (`cmd_load_optional`), `:317` (`cmd_load`), `:402` (`__all__`); `aset/web.py:1262` (docstring), `:1280` (the change line's call). Placed: the definition, the two CLI callers, `cmd_load_card`, the change line, two docstrings, `__all__`.
- (iv) `grep -rn "settings applied" …/src/cobalt` → ONE call, `settings/cli.py:114`; its argument list read whole (`:113`–`:117`): `"settings applied: keys {} · deleted {} · source {} · at {}", sorted(rows), delete, source.split("@sha256:", 1)[0], datetime.now(timezone.utc).isoformat(timespec="seconds")` — keys, deleted keys, source kind, time; no digest, no value.
- (v) L32: this report was re-read once before the last line — no ticker, no real date of his, no file name of his and no value written. (The one repo docs path RUN-3 names, `docs/00 - Project/INCIDENT-2026-09-03-notes.md`, is quoted because the prompt requires RUN-3's paths; the tests' constructed figures are not quoted; run timestamps are not his dates.)

## Ready for D2
| checker | CHECK DRC D4 FIX R1 line | ready | reason verbatim |
|---|---|---|---|
| opus | `CHECK DRC D4 FIX R1: FIX STANDS · ready for D2: YES` | YES | (no reason line; the SEAM GAP is in its body, `ESCALATE 6`: "the seam gap above, for the D2 drafter: cite Part B's `_daymode_banner` bullet") |
| grok | `CHECK DRC D4 FIX R1: FIX STANDS · ready for D2: YES` | YES | (no reason line) |
| sol | NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM) | — | — |

Both seated houses say YES; `defects that HOLD` = 1 (not 0), so by §4 the hub's own field reads `ready for D2: NO` — the classifier's input, not a hub verdict (L37). No row of any seated house is `INPUT NOT WALKED`.

## FOR THE CLASSIFIER
Round 2 of ≤3 (a HOLD goes to round 3, the last, L75). One item per claim that HOLDS in my file-check; I add no class and no recommendation.
1. "Part A (`drc-d4-fix-r1-build-2026-09-25.md:200`–`:219`) supersedes Part B but silently drops Part B's bullet (`drc-d4-build-2026-09-25.md:194`). That bullet recorded `_daymode_banner`'s call to `_settings_daily_form()`, the only reference into D4's block from outside it. Part A also drops the inner-helper cites `:1192` / `:1219`." — opus — the seam (`## SEAM FOR D2`, L72) — `drc-d4-fix-r1-build-2026-09-25.md:200`–`:210` vs `drc-d4-build-2026-09-25.md:193`–`:194`; code `src/cobalt/aset/web.py:565`, `:622`, `:1192` — HOLDS.
No `INPUT NOT WALKED` question.

## ESCALATE
1. Checker lines — opus `CHECK DRC D4 FIX R1: FIX STANDS · ready for D2: YES` and grok `CHECK DRC D4 FIX R1: FIX STANDS · ready for D2: YES`: no `DEFECT REMAINS`. My file-check beside them: opus's SEAM GAP HOLDS (item 2); grok's `SEAM STATED` is consistent with the code (the prompt's three SEAM STATED conditions all hold) and differs from opus only on the omitted bullet.
2. Every item under `## FOR THE CLASSIFIER` restated: (1) the seam text of the fix report omits the D4 report's `_daymode_banner` bullet and the `:1192` / `:1219` helper cites (the code is correct; the D2 drafter reading only Part A would lack that fact).
3. Opus residual (F-2), under a CLOSED verdict, walked — holds as a fact: the loader precondition runs before the patches and the `/size` assertions carry no dollar figure, so a loader patch re-added inside `test_drc_settings_db.py:119`–`:133` would not fail this test. Not counted in `defects that HOLD` (no NOT CLOSED carried it).
4. Opus residual (F-4), under a CLOSED verdict, walked — holds as a fact: the `sheet_modes` check covers only `drc/`; the old DRC prefill's reads (`prefill/drc.py:49`, `:380`, `:408`) are outside the walk and were untouched by this range. Not counted.
5. Opus ESCALATE 4, walked — holds as a fact: build ESCALATE 14 says F-5 and F-6 each carry a negative control; the tree holds none as a separate test (`test_drc_settings.py:136`–`:166`, `:512`–`:519`). Both are CLOSED by both houses on reasoning from the assertions. Not counted.
6. Opus ESCALATE 5 = build ESCALATE 12, walked — holds: `settings/card.py:10`–`:16` still describes the trace as "the command, hash and time" without naming `apply_settings`. Not counted; the build left it as not a named F-1 line.
7. RUN-3 result, non-zero: `old literal outside configs/src/tests: 1 hits` — `docs/00 - Project/INCIDENT-2026-09-03-notes.md` (tracked, last commit `b0fd2e41`); a committed docs file carrying his old daily-stop value — the desk's redaction (L45 companion ruling, build ESCALATE 4); not edited by the build or by this run; no value written here.
8. Build-carried, quoted: LINE MOVED — `grep -n "the one log line (keys + hash + time" src/cobalt/aset/web.py` expected 1270, read 1268 (build ESCALATE 1); RUN-2 "holds trivially today and goes red the day that path logs the form" (build ESCALATE 7, its NOTE for `22`); PINS red: none; RUNS red: none; `0018: rolled back` (no `0018: UNPROVEN`).
9. NOT CHECKABLE FROM READS, with my reads: `cli.py:237` / `:317` are `apply_settings(` call lines (read in the tree); `radar/notes.py:747` is the one `.put(` in `notes.py` (grep) — that it is the only other writer of `trader_settings` rows in the whole tree was walked as far as a `TraderSettingsStore` reference grep (14 files; only `settings/cli.py` and `radar/notes.py` call `.put(`), not a SQL-level search; whether `assert_writable` logs on a refusal, whether each F-5 typed value is the model's declared type, and whether `_render` puts the key name on the page (opus F-6 `:519`) were not read.
10. Harness notices, recorded not followed: on OPUS's stdout `Permission deny rule (../../cobalt/.claude/settings.local.json): Bash(git push*:*) mixes * with the trailing :* prefix syntax … Use Bash(git push*) for wildcard matching.` (as in round 1) and `Warning: no stdin data received in 3s …`; on the OPUS probe the same deny-rule notice. Settings-syntax / stdin notices, not instructions.
11. Packet: no mismatch and no cut; one hub transcription slip corrected before any launch (`## Packet`); saved-original byte differences explained, header bytes not separately measured; no checker wrote a file it was not told to (GROK wrote only `grok-check.md`); no checker failed to check; no `ASK DESK`. I count one cite-form note: both houses cite real lines of the tree (I read `test_drc_d4_fix_r1.py:21`, `:44`, `:46`, `:55`, `:68`, `test_drc_settings_db.py:99`–`:101`, `:134`, `:315` and they match).
12. Sol: `NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM)` — not probed (2026-09-25 08:09 ET is before it); the desk seats Sol from that time.
13. Astra: the D4 NEW BUILD's Astra read is owed from Sep 26th, 2026 6:47 AM (06 ESCALATE 10) — the desk's seat, not this round's.
14. Stagger / meter: OPUS answered in under 8 minutes and GROK in about 11; no TIMEOUT, no relaunch.
15. Standing line: **"Round 2 covers DRC D4 fix r1 only (`5d4f8201..<tip>`), with RUN-1…RUN-3, the amended seam, AMENDED D4-4 TRACE, the report corrections and its three suites' executed output, checked by Opus 5.5 + Grok (+ Sol when seated) under his R95 (a fix round = other check; Gemini out, R96/R97). With every seated house `ready for D2: YES`, `defects that HOLD: 0` and no `INPUT NOT WALKED`, D4 is checked (L67) and `07` (D2) stacks on this tip, citing the fix report's `## SEAM FOR D2`; a HOLD goes to round 3, the last (L39, L75); a NO with `defects that HOLD: 0` leaves round 3 or his per-case override (L67 OVERRIDE / L73)."** — this round: both houses YES, `defects that HOLD: 1`, `INPUT NOT WALKED: 0`.
16. Standing line: **"The deploy's L68 gate re-proves offline, with-DB and the live-note suite on the stacked tree that ships (D1 + K1 + K2 + D4 + D2 + D3); the deploy prompt gets its own house read (L67, R95 seats)."**

DRC D4 FIX R1 CHECK DONE · round: 2 · opus: CHECK DRC D4 FIX R1: FIX STANDS · ready for D2: YES · grok: CHECK DRC D4 FIX R1: FIX STANDS · ready for D2: YES · defects that HOLD: 1 · ready for D2: NO · ESCALATE: 16
