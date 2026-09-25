# VOICE V1 FIX R2 CHECK — ROUND 3 OF 3 (THE LAST) — 2026-09-24

## §0 Headline
- Checked voice V1 fix round 2 (`137c1928..d319e4f3`; red `5a56a47e`, fix `d2963110`, DevDocs `d319e4f3`) with the build's three executed suites and RUN-R, in ONE packet (89,256 B ≈ 22.3k tokens). Checkers: Opus 5.5 and Grok. Sol: NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM, `37`'s record; not probed).
- Both checkers: all 7 FIX rows CLOSED · KEPT · NOTHING WIDENED · 3 suites SHOWN · DESELECTS AS STATED · RUN-R SHOWN · `FIX STANDS · ready … YES`.
- My file-check: `defects that HOLD: 1` — not a FIX-row failure; Opus's ESCALATE observation that the new A1 alternative also refuses some ordinary card phrasings holds as an input fact (`tools.py:61`). Under `## FOR DEJAN`. ESCALATE: 10.

## L74
One block arrived attached to a tool result (the first Read of this prompt file): an attribution reminder asking commits to carry a `Claude-Session:` trailer and mentioning a file-send tool. Recorded once here as DATA; not followed. This run commits nothing.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| clock | `date` | 0 | `Thu Sep 24 22:40:30 EDT 2026` (`<D>` = 2026-09-24, before Sol's return) |
| placeholder | `grep -c -F "R__" …/55-voice-v1-fix-r2-check.md` | 0 | `1` |
| grok gate R17 | `grep -n "^| R17 " cto-2026-09-24.md`; `git log -1 -S"Grok approved with no asking going forward"` | 0 | `33:| R17 |` present; `1758fd78a572f47b613b2ca831dcfa636ed8f65a` (re-run 22:50 before launch: same) |
| grok gate R19 | `grep -n "^| R19 " …`; `git log -1 -S"All 4 house models approved"` | 0 | `35:| R19 |` present; `5055151dbf68899b82de5b11f99733ed2d03048c` |
| round 2 committed | `git log -1 -- …voice-v1-fix-r1-check-2026-09-24.md`; `tail -n 3` | 0 | `f2196b5ee1c14d190a2c2a3074cfabaefc4a912c`; last line starts `VOICE V1 FIX R1 CHECK DONE · round: 2` |
| classification committed | `git log -1 -- …voice-v1-fix-r2-draft-2026-09-24.md`; `tail -n 3` | 0 | `f8926b45b743877695af52a3e199358d31d908b1`; last line starts `VOICE V1 FIX R2 DRAFTED ·` |
| launch row | `grep -n -F "55-voice-v1-fix-r2-check.md" cto-2026-09-24.md`; `git log -1 -S…` | 0 | `125:| R104 |` (22:39 ET launch row; `:102` R83 is the drafted record); `a67f2a7dde849bf0db13d976a831d60ac2ae653a` |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| worktree | `ls /Users/cobalt/cobalt-wt/voice-v1` | 0 | present |
| BUILT line | `tail -n 3 …/voice-v1-fix-r2-build-2026-09-24.md` | 0 | `VOICE V1 FIX R2 BUILT d319e4f3 \| on 137c1928 \| red 5a56a47e \| offline 2786/0 \| with-DB 3129/0 \| live-note 142/0 \| .env: removed \| 0017: rolled back \| FIX: 7 of 7 \| RUNS: 1 \| deselects: <eight names> \| ESCALATE: 8` — every required field present; no `0017: UNPROVEN`; `<tip>` = `d319e4f3`, `<red>` = `5a56a47e` |
| tip subject | `git log --oneline -1 d319e4f3` | 0 | `d319e4f3 docs(voice-v1): fix r2 DevDocs (L75)` |
| range | `git log --oneline 137c1928..d319e4f3` | 0 | exactly 3: `d319e4f3 docs(voice-v1): fix r2 DevDocs (L75)` · `d2963110 fix(voice-v1): fix r2 — …` · `5a56a47e wip(fix-r2): voice V1 fix r2 red tests — …` |
| nothing after tip | `git log --oneline d319e4f3..voice/v1-0923 -- src tests configs` | 0 | EMPTY |
| path union | `git log --stat --format=%h 137c1928..d319e4f3` | 0 | 18 = 6 docs (`aset/card_stop.md`, `voice/{cli,config,tools,turn,web}.md`) + 7 src/config (`configs/cobalt/jobs.yaml`, `src/cobalt/aset/card_stop.py`, `src/cobalt/voice/{cli,config,tools,turn,web}.py`) + 5 tests (`test_jobs_restarts`, `test_voice_{config,fix_r1_runs,tools,web}`); no `db_migrations`, no other `configs/` |
| L28 sweep | `grep -rn -F "VaultWriter" …/src/cobalt/voice`; `… "vaultwrite" …` | 1 / 1 | no hits (both) |
| `.env` | `ls /Users/cobalt/cobalt-wt/voice-v1/.env` | 1 | `No such file or directory` |
| recovery | `ls scratch/tribunal-bars-0920/voice-v1-check/fix-r2` | 1 | `No such file or directory` = fresh run |
| stagger | `grep -n -F "no other house hub is running" cto-2026-09-24.md` | 0 | line `125` (R104) carries the literal and names `55-voice-v1-fix-r2-check.md` |
| Opus probe | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (background) | 0 | `OK` (plus one harness warning about a `Bash(git push*:*)` deny-rule syntax) → opus UP |
| Sol probe | keyed on `date` | — | 22:40 ET on 2026-09-24 is before 2026-09-26 06:47: NOT probed → `sol: METER — retry after Sep 26th, 2026 6:47 AM (37's record)` |
Floor: Opus AND Grok UP = two seats. No `mkdir`, no `s2-p2-cards` string, no `agy`, no `codex exec`, no Astra was run.

## Packet
`/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v1-check/fix-r2/` (the Write tool created the folder; every Write under 15,000 B, R79). Files (B): `fix-diff.part1..4.md` 5,186 · 10,534 · 9,132 · 6,219 · `devdocs-diff.md` 8,177 · `build-proof.part1..3.md` 6,142 · 6,325 · 4,595 · `suites.md` 6,472 · `round-2.part1..3.md` 5,695 · 7,325 · 3,955 · `design.md` 4,420 · `QUESTIONS-VOICE-V1-FIX-R2.md` 5,079. **Total 89,256 B ≈ 22,314 tokens per checker** (ceiling 230,000 B: met; drafter's estimate 70–120 KB: met). Each file has a one-line header naming its real path, range and tip.
Checks (counted by me): fix diff — `^commit ` lines = 2 (red, fix), `^diff --git` lines = 12 = the 7 src/config + 5 test path-touches `--stat` shows; DevDocs diff — 1 commit, 6 `diff --git`. Copies were verified by (a) line counts — fix-diff parts 86 + 171 + 175 + 105 lines = 529 source lines + 8 header lines; devdocs 130 = 128 + 2, (b) `grep -v -x -F -f <original> <copy>` printing only header and blank lines for every copy, and (c) trailing-whitespace counts equal to the original's (fix diff 8 + 10 + 14 + 10 = 42; devdocs 17; build report, round 2 and classification 0). A byte-sum against the saved git output was not done: that file carries the harness's trailing `[exited with code 0]` lines (29,909 B / 7,917 B on disk).
`build-proof` carries the executed RUN-R output (`## RESTARTS`); `suites.md` carries D1, D6, D7 and D8 each with a summary line — no `FAILED: packet`.
Written-nothing proof (Opus and Grok both read-only-launched; Grok may write only its own file): folder before, 14 packet files (listing at 22:50); after Opus 22:54, the folder held the same 14 plus `opus-check.md` (mine); after Grok 23:01, plus `grok-check.md` (its own file, told to it). `ls -la /Users/cobalt/cobalt-wt/voice-v1` at 22:50 and at 23:01: identical (the newest entry `.` dated Sep 24 21:40 in both). Denial search on Opus's output: 0 hits (`grep -c -i "denied\|not allowed\|permission"`); Grok's file read whole: none.
Launch lines as run: OPUS (22:50:57, finished 22:53) `claude -p --model claude-opus-5-5 "<sentence>" --permission-mode plan --add-dir /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v1-check/fix-r2 --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"`. GROK (22:51:06, finished 23:01) `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "<sentence + reasons for CLOSED on A1, D3, C2 + write to …/fix-r2/grok-check.md>"`. Both sentences named the folder (relative and absolute), `QUESTIONS-VOICE-V1-FIX-R2.md`, the `.part<k>` rule and "Do not open any *-check.md file". Grok wrote `grok-check.md` itself; I wrote `opus-check.md` from stdout (lines 3–45, without the two harness warning lines and the exit trailer; copy verified line by line). Both well inside the 45-minute clock.

## CONTINUE
next: none — collation done.

## Rows
`row · opus · grok · sol` (sol: NOT SEATED — METER).
| row | opus | grok |
|---|---|---|
| A1 | CLOSED — `_ORDER` alternative matches all four; test 4 × answer/act; red ×8 `assert (None is not None)`; readable set still reads (`my short XYZ card`, `close at`); observation below | CLOSED — "Named red at test_voice_tools.py:169; tools.py:61 now refuses `exit QRS`, `get out of QRS`, `close out QRS`, and `short QRS`, and the six side/price pins stay green." |
| D3 | CLOSED — `device` declared, drawn by `banner()`, no-mic line pushed to it; no status callback assigns `device`; static pin, red at (a) | CLOSED — "Refused and OK callbacks assign only `lines` (web.py:299); the no-microphone line stays on `device` (web.py:300) and banner always concats it (web.py:232)." |
| DESELECT IDS | CLOSED — all eight full ids verbatim in D8 (d) command and ESCALATE 1; stop line names all eight, each matching one id | CLOSED |
| C2 | CLOSED — no-arg load reads through `load_backup_config()`, `BackupConfigError` → `VoiceConfigError`; `jobs.yaml` reads/no_resident_reads; pin `("com.cobalt.aset",)`, rule `resident reads`, `readers_of == ["com.cobalt.aset"]` | CLOSED — "No-arg load refuses a path under a backup source (config.py:159); jobs.yaml:75 is on aset reads and not under no_resident_reads; the pin is com.cobalt.aset (test_jobs_restarts.py:391)." |
| RUN-2 | CLOSED — `expect_from_stop=pending.from_stop`; `StopMoved` before `record_stop_edit` → `TargetChanged`; route passes nothing | CLOSED |
| RUN-4c | CLOSED — `except Exception` after `PlanFailed` ends the turn as `voice_plan`; only non-`Exception` types get past it | CLOSED |
| RUN-7 | CLOSED — read once, `len(data) > cfg.max_upload_bytes` → `_fail` before `DirectoryLock` and any turn; no scratch path touched | CLOSED |
| sol | NOT SEATED | — |

## Intent
- opus · KEPT — "The only reversed assertion is C2's … xfailed went from 4 to 1 … No skip or mark was added. Confirm, the 10× guard … and the read-back are untouched."
- grok · KEPT
- sol · NOT SEATED

## Scope
- opus · NOTHING WIDENED — "18 paths: 7 src/config + 5 tests + 6 DevDocs … no migration … the VaultWriter/vaultwrite grep finds nothing."
- grok · NOTHING WIDENED
- sol · NOT SEATED

## Suites
`suite · opus · grok · sol`
| suite | opus | grok | sol |
|---|---|---|---|
| offline | SHOWN — `2786 passed, 358 skipped, 1 xfailed, 20 warnings in 92.41s` · exit 0, 0 failed | SHOWN — same line `(0:01:32)` · exit 0 · failed 0 · `.env` absent before the run | NOT SEATED |
| with-DB | SHOWN — `3129 passed, 6 skipped, 9 deselected, 1 xfailed, 20 warnings in 169.22s` · exit 0, 0 failed; probe `28 == 29` | SHOWN — same line `(0:02:49)` · failed 0 · probe short by 1 · `.env` removed at (f) | NOT SEATED |
| live-note | SHOWN — `142 passed, 1 skipped, 15 warnings in 9.74s` · exit 0, 0 failed | SHOWN — same line · failed 0 | NOT SEATED |
| deselects | DESELECTS AS STATED — all eight ids verbatim; five proven by their own run (`5 failed`, `UndefinedTable voice_turns`) | DESELECTS AS STATED | NOT SEATED |

Myself, from the build report `/Users/cobalt/cobalt-wt/voice-v1/docs/40 - DevDocs/reports/voice-v1-fix-r2-build-2026-09-24.md` (not the packet copy):
- offline (D7, line 104): `2786 passed, 358 skipped, 1 xfailed, 20 warnings in 92.41s (0:01:32)` · exit 0 → `<f>` = 0, 0 errors stated.
- with-DB (D8 (d), line 116): `3129 passed, 6 skipped, 9 deselected, 1 xfailed, 20 warnings in 169.22s (0:02:49)` · exit 0 → `<df>` = 0, 0 errors stated.
- live-note (D6, line 101): `142 passed, 1 skipped, 15 warnings in 9.74s` · exit 0 → `<lf>` = 0, 0 errors stated. The one SKIPPED line names `COBALT_TEST_LIVE_DRC`; no `SKIPPED` line names `COBALT_LIVE_VAULT_ROOT` in the live-note leg (expected none: met). With-DB's own SKIPPED list carries `test_radar_evaluate.py:691`, `test_catalyst.py:365`, `test_predicate.py:262` as `COBALT_LIVE_VAULT_ROOT not set` — the report states these run at D6.
- DESELECT PROOF (D8 (c), lines 109–115): `5 failed, 5 warnings in 32.17s` · exit 1; per id: `test_store_round_trip_and_single_flight_in_the_suite_transaction` FAILED `UndefinedTable: relation "voice_turns" does not exist`; `test_the_reaper_fails_stale_rows_and_never_retries` FAILED, same; `test_single_flight_under_two_real_connections` FAILED, same; `test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both` FAILED, same (cleanup `DELETE FROM voice_turns`); `test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped` FAILED (`the upload never reached the scratch dir`, then `UndefinedTable`); "None passed, none skipped → `voice_turns` does NOT exist on `cobalt_dev`."
- The eight ids as quoted in D8 (d) (full `--deselect` ids): `tests/cobalt/test_tenancy.py::TestMigrationRoundTrip`; `tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default`; `tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches`; `tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction`; `…::test_the_reaper_fails_stale_rows_and_never_retries`; `…::test_single_flight_under_two_real_connections`; `tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both`; `tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped`. In the stop line (line 139) the same eight appear by test name: `TestMigrationRoundTrip`, `test_every_user_table_carries_user_id_not_null_with_the_guc_default`, `test_rows_reach_the_probe_through_a_named_cursor_in_batches`, `test_store_round_trip_and_single_flight_in_the_suite_transaction`, `test_the_reaper_fails_stale_rows_and_never_retries`, `test_single_flight_under_two_real_connections`, `test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both`, `test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped` — same eight, same order. ESCALATE 1 (line 130) lists the eight full ids too.
- `0017` ABSENCE PROBE (D8 (e), line 117): `1 failed in 5.88s`, `assert 28 == 29` — "SHORT BY EXACTLY 1 … NO `cobalt_probe_voice_turns`" → `0017: rolled back — applied only inside the suite's transaction; absent on cobalt_dev (probe short by 1)`.
- `.env: removed, proven gone (D8)` is written (line 118), preceded by `.env` absent at D7 (line 104) and the lock reads at D8 (a) (line 107); the stop line carries `.env: removed`.

## Runs
`run · opus · grok · sol`
| run | opus | grok | sol |
|---|---|---|---|
| RUN-R | RESULT SHOWN — `RESTARTS: com.cobalt.aset com.cobalt.radar` | RESULT SHOWN — `RESTARTS: com.cobalt.aset com.cobalt.radar` | NOT SEATED |

Myself, build report `## RESTARTS` (lines 120–124): `uv run cobalt jobs restarts 137c1928..d319e4f3` → exit 0; last line `RESTARTS: com.cobalt.aset com.cobalt.radar` (`jobs.yaml` → `registry; register, no restart`; `card_stop.py` and `voice/{config,tools,turn,web}.py` → `static import reach` `com.cobalt.aset,com.cobalt.radar`; `voice/cli.py` → `com.cobalt.radar`; 6 docs and 5 tests → no restart). Whole-branch range `04b05cd4..d319e4f3` → exit 1, `RestartError`, six UNCLASSIFIED paths (`configs/cobalt/agents/voice.yaml`, `configs/cobalt/modelaccess.yaml`, `configs/cobalt/voice.yaml`, `ops/start_aset.sh`, `pyproject.toml`, `uv.lock`), `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`. Offline xfailed count: `1 xfailed` in D7 (line 104) — `54` D7 expects 1: as expected.

## Red
From the build report `## D2 RED (offline)` (lines 43–79): run of the eight voice / jobs test files on `137c1928` → `15 failed, 250 passed in 9.02s` · exit 1; "The 15: A1 8 · D3 1 · C2 3 · RUN-2 1 · RUN-4c 1 · RUN-7 oversize 1 — EXACTLY the named set; every other test passed".
- A1 ×8: `assert (None is not None)` (`test_voice_tools.py:169`). A1 not-refused set: green ×6.
- D3: `AssertionError:  let rec = null, chunks = [], pendingTurn = null, muted = false, downAt = 0, lines = [];` (`test_voice_web.py:255`); `:234`'s test green.
- C2 ×3: `AttributeError: <module 'cobalt.voice.config' …> has no attribute 'load_backup_config'` (`test_voice_config.py:235`); `assert 'load_backup_config' in '"""…'` (`:221`); `assert () == ('com.cobalt.aset',)` (`test_jobs_restarts.py:391`).
- RUN-2: `Failed: DID NOT RAISE <class 'cobalt.voice.tools.TargetChanged'>` (`test_voice_fix_r1_runs.py:83`). RUN-4c: `assert 'Something fa... was changed.' == "Cobalt can't...(ValueError)."` (`:124`). RUN-7: `Failed: DID NOT RAISE <class 'SystemExit'>` (`:175`), `[zero]` green.
Facts: every named red is one of the rows the build named (A1 ×8, D3, C2 ×3, RUN-2, RUN-4c, RUN-7 = 15); no other test was red. Green after the fix: same eight files → `265 passed in 10.13s` · exit 0, no `xfailed` (D3 proofs, line 91).

## Checked against the branch
Files: code under `/Users/cobalt/cobalt-wt/voice-v1/` (tip `d319e4f3`), the build report there, the staged packet. No checker answered NOT CLOSED, WEAKENED, WIDENED, NOT SHOWN or DESELECTS OPEN; no checkers contradict each other. Rows below are Opus's ESCALATE observation and the reasons Grok gave (round 2's Grok answered CLOSED with none; the file-check decided).
| claim · who | file:line | verdict | note (≤30 words) |
|---|---|---|---|
| A1 rule also refuses ordinary card phrasings: `the XYZ short I opened`, `move the stop on the XYZ short I have to <value>`, `the stop on this short XYZ card`, `what was the close I saw on XYZ` · opus (ESCALATE 1; ruled no FIX-row failure, `YES`) | `src/cobalt/voice/tools.py:61` (with `:55-62`) | **HOLDS** (input facts) | `re.I` + `(?-i:[A-Z]{1,5})\b`: `I` is a 1-letter upper token, so `short I` / `close I` match; the lookbehind exempts only `the ` / `my ` / `a ` before `short` (`this ` is not exempt); `code_refusal` returns the fixed sentence before any tool. |
| A1 CLOSED: `tools.py:61` refuses `exit QRS`, `get out of QRS`, `close out QRS`, `short QRS`; six side/price pins green · grok | `tools.py:61`; `test_voice_tools.py:169` | HOLDS (as a reason) | `:61` carries `short ` + upper ticker and `(exit\|close out\|close\|get out of) ` + upper ticker; test at `:169` is in `fix-diff.part4`; the readable set (six pins) stays in the same test file. |
| D3 CLOSED: callbacks assign only `lines` (`web.py:299`), no-mic line on `device` (`:300`), `banner` concats it (`:232`) · grok | `web.py:229`, `:232`, `:299`, `:300` | HOLDS (as a reason) | `:229` declares `device = []`; `:232` `lines.concat(device, extra \|\| [])`; `:299` assigns `lines` only; `:300` `device.push(…)`. Runtime on a real device is the owed device session. |
| C2 CLOSED: `config.py:159`; `jobs.yaml:75`; pin `test_jobs_restarts.py:391` · grok | `config.py:159-163`; `jobs.yaml:70-75, 307-315`; `test_jobs_restarts.py:391` | HOLDS (as a reason) | `:159` `if backup_sources is None` → `load_backup_config().sources`; `jobs.yaml:75` is in `com.cobalt.aset`'s `reads:`; `no_resident_reads` now holds only `notify.yaml` and `rules.yaml`; `:391` asserts `("com.cobalt.aset",)`. |
| RUN-4c: only non-`Exception` types get past `except Exception` · opus | `turn.py:293-304`; `:126` | HOLDS | The `try` at `:293` wraps only `deps.plan`; `_Fail(Exception)` raised in the `PlanFailed` handler is not caught by its sibling `except`. |
- (i) L28 SWEEP: `grep -rn -F "VaultWriter"` and `grep -rn -F "vaultwrite"` over `…/src/cobalt/voice` → no hits (both).
- (ii) L32: I read this report once before the last line: no ticker beyond the constructed `XYZ` / `QRS`, no price and no word of his written.

## Ready for a deploy prompt
| checker | CHECK VOICE V1 FIX R2 line | ready | reason verbatim |
|---|---|---|---|
| opus | `CHECK VOICE V1 FIX R2: FIX STANDS · ready for a deploy prompt: YES` | YES | — |
| grok | `CHECK VOICE V1 FIX R2: FIX STANDS · ready for a deploy prompt: YES` | YES | — |
| sol | NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM) | — | — |

## FOR DEJAN
ROUND 3 WAS THE LAST — L39 / L75: no round 4. One item; no class, no recommendation.
1. Claim (verbatim, opus, its ESCALATE 1): "The A1 rule refuses some ordinary card phrasings … `short` followed by the always-capital `I`, or by a ticker after any other word, matches: `what is the stop on the XYZ short I opened` → refused. `move the stop on the XYZ short I have to <value>` → refused. This is V1's one act. `the stop on this short XYZ card` → refused. `what was the close I saw on XYZ` → refused, via `close I`. Each gets the fixed refusal and nothing executes, so it breaks no law and no FIX row. The row's pinned readable set holds." — row A1 — my file:line `src/cobalt/voice/tools.py:61` — HOLDS (input facts). Opus itself ruled it no FIX-row failure and answered `YES`; it is listed here because the rule as built refuses those inputs.

## ESCALATE
1. **Opus's observation, quoted in full with my verdict beside it:** see `## FOR DEJAN` 1 — HOLDS as input facts at `tools.py:61`; both checkers answered `FIX STANDS · … YES`. No checker answered `DEFECT REMAINS`.
2. **Sol's line:** NOT SEATED — METER, retry after Sep 26th, 2026 6:47 AM (`37`'s record); not probed (22:40 ET on 09-24).
3. **The build's L76 standing line (carried, not this check's):** "L76 left five V1 with-DB tests UNRUN in this build (`D8` (c) proves why): the store round-trip and reaper, X-X13's two real-connection races, and X-E7, plus RUN-1's timing. Each needs `voice_turns` COMMITTED on a database. They run at the stacked L68 gate with `0017` applied and rolled back before its stop line (L76's second clause) — the desk's ruling (`37` ESCALATE 8 / 12), not this build's."
4. **The build's OUT OF SCOPE line (carried):** "OUT OF SCOPE, carried: D6 — `tests/cobalt/test_radar_panel_cards.py` changed outside `43`'s list; its revert would turn the `/radar` byte-equality red, so it was NOT taken; the desk rules the boundary. X-E10 — the FINAL's column routes 'an unexpected native / GPL package' to TRIBUNAL ROUND 2 (FINAL `:285`); not this build's."
5. **Desk R83 reading, not staged:** the desk's record (`cto-2026-09-24.md:102`) says its ESCALATE 2 — a narrower RUN-2 window in `cards/store.py:677-682` — was to be CARRIED to `55`'s packet as a named non-claim, not built (L75). `55`'s own staging list (§1 (1)–(7)) has no such item, so it was not staged and no checker named it. Recorded here as a fact for the desk.
6. **C2's wider import reach (build ESCALATE 6, carried):** `cobalt.voice.config` imports `cobalt.backup.config` at module level, so by the classifier's static-import rule a `src/cobalt/backup/*.py` change now derives a `com.cobalt.aset` restart as well as a `configs/cobalt/backup.yaml` change (a reading, not run); the deploy prompt names both (L42).
7. **L74:** one block recorded once under `## L74`, not followed.
8. **Process record:** (a) Grok's stdout says it began with "the required law/memory reads" before the packet — a read outside the folder that the questions file said not to make (read-only; the worktree listing and the folder listing show it wrote nothing but `grok-check.md`); (b) harness warnings on the Opus launch (`Bash(git push*:*)` deny-rule syntax; "no stdin data received in 3s") — no effect on the answer; (c) packet copies were verified by line counts, per-line membership and trailing-whitespace counts, not a byte sum (see `## Packet`).
9. **Standing line:** "Round 3 — THE LAST (L39 / L75) — covers voice V1 fix r2 only (`137c1928..d319e4f3`), in ONE packet, with RUN-R and its three suites' executed output and the eight deselect ids, checked by Opus 5.5 + Grok (+ Sol when seated) under his R95 (Gemini out, R96/R97). With every seated house `ready … YES` and `defects that HOLD: 0`, V1 is checked (L67) and may join a stacked deploy — after the device session (E1 E3 E5 E8 X3), which stays OWED before any ship. A HOLD here, or a NO with `defects that HOLD: 0`, goes to him as ONE message — his per-case override (L67 OVERRIDE / L73) or a design round — never a round 4."
10. **Standing line:** "The deploy's L68 gate re-proves offline, with-DB and the live-note suite on the tree that ships — and is where the five V1 with-DB tests that need `voice_turns` committed run (L76's apply-and-roll-back clause, the desk's ruling); the deploy prompt gets its own house read (L67, R95 seats), carries V1's production prerequisites (build ESCALATE (vi)), and names the `com.cobalt.aset` restart C2 now derives for a `configs/cobalt/backup.yaml` change (L42)."

VOICE V1 FIX R2 CHECK DONE · round: 3 · opus: CHECK VOICE V1 FIX R2: FIX STANDS · ready for a deploy prompt: YES · grok: CHECK VOICE V1 FIX R2: FIX STANDS · ready for a deploy prompt: YES · defects that HOLD: 1 · ESCALATE: 10
