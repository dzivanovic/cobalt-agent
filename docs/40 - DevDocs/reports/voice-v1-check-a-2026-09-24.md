# Voice V1 check — PART A (the ordered act) · round 1 of ≤3 · 2026-09-24

## §0 Headline

- Checked: part A of four of `04b05cd4..28b6b0c6` on `voice/v1-0923` — C7 tools · C8 `set_card_stop` · C9 `voice_turns` + store · C10 confirm. PREFLIGHT green; packet 221,682 B.
- Opus 5.5 answered: `DEFECT REMAINS A1 A2` (C7 and C10 NOT CLOSED, C8 and C9 CLOSED). **Grok did NOT check** — its Write into the packet folder was refused and it produced no check file (HARNESS). Sol METER until Sep 26th, 2026 6:47 AM; Astra NOT SEATED. One seated house checked, so the two-house floor is NOT met.
- File-check: **3 defects HOLD** (A1 order/platform refusal regex gap · A2 `target_sha256` re-check unpinned by any test · A5 `EXECUTING → DONE` return ignored). ESCALATE: 12.

## L74

After this session's first tool result (the Read of this prompt file), one block asked that commits end with a `Claude-Session:` line and named a file-send tool (`SendUserFile`). Recorded once, as data. Not followed: this seat commits nothing and sent no file.

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | Thu Sep 24 08:43:25 EDT 2026 (again 09:00:11 before launch) |
| GROK GATE (row 1) | `grep -n "^| R17 " …cto-2026-09-24.md` · `git log -1 --format=%H -S"Grok approved with no asking going forward" -- …cto-2026-09-24.md` | 0 | allowed: R17 row carries `Grok approved with no asking going forward`; commit `1758fd78a572f47b613b2ca831dcfa636ed8f65a` |
| GROK GATE (row 2, immediately before launch, ~09:01) | same `git log -S` · `grep -c -F "Grok approved with no asking going forward"` on the desk file | 0 | commit `1758fd78…` again; phrase count 1 (the R17 row had moved from line 26 to 27 — the desk file changed on disk between the two reads; row unchanged) |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` — UP |
| launch row | `grep -n -F "16-voice-v1-check-a.md" …cto-2026-09-24.md` · `git log -1 --format=%H -S"16-voice-v1-check-a.md" -- …cto-2026-09-2*.md` | 0 | R31 (line 40) names this file; committed `c5305b403f4b77b0a342e8c6bf7008a43ff3add4` |
| 66 gate R13 (09-20) | `grep -n "^| R13 "` | 0 | allowed (line 86) |
| 66 gate R40 | `grep -n "^| R40 "` | 0 | allowed: `ONE EXTRA DOT THAT CANNOT BE TAPPED` |
| 66 gate R44 | `grep -n "^| R44 "` | 0 | allowed: `ONE BUILD of the whole FINAL` |
| 66 gate R46 + committed | `grep -n "^| R46 "` · `git log -1 -S"instead of Astra you can use Sol"` | 0 | allowed; `53e059456750c0c9efcf50222a7a647630dc4b04` |
| 66 gate R49 (Sol string) | `grep -n "^| R49 "` · `grep -c -F "Bash(codex exec …gpt-5.6-sol -s read-only *)"` · `git log -1 -S…` | 0 | allowed: `"Approved"`; count 1; `60147d400b009db5a2518e02b8ab1fe5765db405` |
| Opus string R32 | `grep -n "^| R32 " …cto-2026-09-22.md` · `git log -1 -S"Bash(claude -p --model claude-opus-5-5 *)"` | 0 | allowed (line 131); `b8b5a7300370e248cd6c7a8a732258fec03e6a0` |
| THE TWELVE + THREE | `grep -c -F -e "<rule>" …/2026-09-20/08-bars-chunk-e-check.md` ×15 (grok, mkdir, git show, git log, s2 show/log/diff, ls, grep, tail, wc, date; the 3 denies) | 0 | each **1** |
| Astra / agy absent | read of this prompt's launch line (line 1): 14 allow strings, no `gpt-6-astra`, no `Bash(agy *)` | — | allowed |
| design approval R57 | `grep -n "^| R57 "` · `git log -1 -S"approved design"` | 0 | allowed (line 60); `ffee37ad5e41ab5eb451406a9e11a9e03b26afdb` |
| build launch + stop record | `grep -n "43-voice-v1-build.md" …cto-2026-09-23.md` · `git log -1 -S"VOICE V1 BUILT" -- …cto-2026-09-2*.md` | 0 | launch rows R60, R63; stop recorded on R71 (line 74) and R108 (line 116), each carrying `VOICE V1 BUILT 566d1848`; commit `9cc68741bc8cd656d4d2e3f9d7189ad8fabba2d8` |
| re-cut committed | `git log -1 -S"VOICE V1 CHECK RECUT" -- …voice-v1-check-recut-2026-09-24.md` | 0 | `80b208c5d1304bd99ec44fe1b6dfd84fc3c91b3c` |
| worktree | `ls /Users/cobalt/cobalt-wt/voice-v1` | 0 | present |
| THE BUILT LINE | `tail -n 3 …/voice-v1-build-2026-09-23.md` | 0 | see below |
| tip | `git log --oneline -1 28b6b0c6` | 0 | `28b6b0c6 feat(voice-v1): build report` |
| range | `git log --oneline 04b05cd4..28b6b0c6` | 0 | 15 commits (recorded) |
| branch tip | `git log --oneline -1 voice/v1-0923` · `git log --oneline 28b6b0c6..voice/v1-0923 -- tests src configs ops pyproject.toml uv.lock "docs/40 - DevDocs/cobalt"` | 0 | `28b6b0c6 feat(voice-v1): build report`; second call EMPTY |
| THE BOUNDARY / SPLIT | `git log --stat --oneline 04b05cd4..28b6b0c6` | 0 | 84 distinct paths (67 NEW + 17 CHANGED, counted by hand) = A 25 (14 NEW + 11 CHANGED) · B 26 · C 19 (16 + 3) · D 13 (10 + 3) + the build report; every path is in exactly one row of the re-cut's `## Split` |
| NEW vs CHANGED | `git log --diff-filter=A --name-only --format= 04b05cd4..28b6b0c6` | 0 | 67 paths; every part-A row staged WHOLE is printed (14 of 14); no part-A row staged as a DIFF is printed (11 of 11 absent) |
| `.env` | `ls /Users/cobalt/cobalt-wt/voice-v1/.env` | 1 | "No such file or directory" — as required |
| recovery | `ls …/scratch/tribunal-bars-0920/voice-v1-check-a` | 1 | "No such file" — fresh run. This session's cwd was `/Users/cobalt/cobalt`, not `agy-trial` (a relative-path `ls` first missed for that reason), so every scratch path in this run is ABSOLUTE |
| context source | `ls …/scratch/tribunal-bars-0920/voice-v1-check/A` | 0 | all 12 files present |
| STAGGER | `grep -n -F "no other house hub is running" …cto-2026-09-24.md` | 0 | R31 (line 40) carries the literal and names `16-voice-v1-check-a.md` |
| CODEX LAUNCH SHAPE | `grep -c -F "Experiment field: **reads started**" …setups-tribunal-r2-2026-09-21.md` | 0 | `1` → a Sol launch appends ` < /dev/null` (Sol not launched) |
| PROBE Sol | `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` | 1 | `You've hit your usage limit. … try again at Sep 26th, 2026 6:47 AM.` → `sol: METER — retry after Sep 26th, 2026 6:47 AM` — SKIPPED, not relaunched |
| PROBE Opus | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` | 0 | `OK` — UP |
| Astra | — | — | `astra: NOT SEATED — Sol's Codex meter (Sep 26th, 2026 6:47 AM); no string on this line, never launched (R46)` |

THE BUILT LINE (last non-blank line of `voice-v1-build-2026-09-23.md`, whole): `VOICE V1 BUILT 566d1848 | on 04b05cd4 | migration 0017 | offline 2422/0 | with-DB 2774/0 | experiments run: 12 of 12 | design-changing results: 3 | stt: faster-whisper/tiny.en | plan route: local.plan (mainframe) | device session: OWED (E1 E3 E5 E8 X3) | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar (6 UNCLASSIFIED) | tests added: 471 | ESCALATE: 14`. `<tip>` on the line `566d1848` → desk amendment R108 = `28b6b0c6` (checked above); `<base>` = `04b05cd4` = the measured base, so no re-measure is owed.

Device session record: `ls -d …/reports/voice-v1-device-*.md` → no match → `device session: NOT RUN`.

## Packet

Staged in `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v1-check-a/` (16 files, no `mkdir`, Read → Write). MEASUREMENT gate (before the first Write): all ten whole code/test originals and the four DevDoc originals equal the table byte for byte (10,240 · 2,027 · 9,189 · 5,427 · 3,569 · 297 · 8,985 · 7,715 · 8,508 · 12,317 · 2,160 · 1,169 · 1,616 · 1,446); the five saved git outputs are 4,529 · 2,804 · 9,126 · 3,053 · 2,797 B (no drift) with `grep -c "^diff --git"` = 2 · 2 · 6 · 2 · 2 (the table's counts); the build report is 75,781 B and `grep -n "^## "` puts `## C7` at 293 and `## C11` at 344; the context sources measure 15,586 · 21,457 · 14,433 · 13,946 · 21,984 · 4,080 · 4,701 (+ `stop-route-before-after` 5,870, `store-stop` 4,986). Trailing-whitespace counts before copying: 0 for every original; `rows.part1.md` has 1 (the source's own line, reproduced).

| staged file | bytes | what | copy check |
|---|---|---|---|
| `QUESTIONS-VOICE-V1-A.md` | 7,884 | the prompt's four paragraphs verbatim (they equal prompt lines 73–76: 1,399 · 1,898 · 815 · 595 B) + the file-list paragraph | line-for-line match against the prompt file |
| `a-code.md` | 31,168 | 6 new code/SQL files, whole | = 30,749 originals + 419 header bytes exactly; every non-blank line present in its original |
| `a-tests-1.md` | 25,418 | `test_voice_tools` / `test_voice_card_stop` / `test_voice_confirm`, whole | = 25,208 + 210 exactly; line-set check clean |
| `a-tests-2.md` | 12,386 | `test_voice_store`, whole | = 12,317 + 69 exactly; line-set check clean |
| `a-diff.md` | 16,830 | saved diffs: `aset/web.py` (2 commits), `db_migrations/__init__.py` + `placement.py`, five registry-pin tests | = 16,459 + 371 exactly; two-way line-set check clean (a first pass had 4 typing errors in the pin-test piece — a garbled line, two `@@` context names, a missing block header — found by that check and corrected before any checker launched) |
| `stop-route-before-after.md` | 5,870 | copied from `voice-v1-check/A/` | size and line sets equal |
| `store-stop.md` | 4,986 | copied from `voice-v1-check/A/` | size and line sets equal |
| `a-devdocs.md` | 12,794 | 4 new DevDocs whole + 2 saved DevDoc diffs | = 12,241 + 553 exactly; two-way line-set check clean (a first pass had 3 errors — two missing trailing tabs and one word — corrected) |
| `build-report-a.md` | 8,159 | build report lines 293–343 | body 8,059 B + 100 B header; line sets equal |
| `final-v1.part1.md` · `final-v1.part2.md` | 15,586 · 21,457 | context | sizes equal; line sets equal |
| `seam-s1.md` | 14,433 | context | size and line sets equal |
| `rows.part1.md` · `rows.part2.md` | 13,946 · 21,984 | context | sizes equal; line sets equal |
| `rulings.md` · `l28.md` | 4,080 · 4,701 | context | sizes equal; line sets equal |

Piece headers are `### <path or command> @ 28b6b0c6 · <whole|lines a–b|git output> · <n> B`, ≤160 B; two headers abbreviate their command (the five pin tests; the two DevDoc diffs) to stay under 160 B — the QUESTIONS file says so. The copies were made by retyping from Read output (the Write tool takes text, not a file path); the line-set and size checks above are the fidelity proof.

HONEST SIZE: **221,682 B** total (≤ 230,000 B ceiling; ≈ 8,300 B spare) ≈ **55,420 tokens per checker** (÷ 4). Largest staged file 31,168 B (≤ 38,000 B).

Launches (both `run_in_background`, independent, one attempt each; hub cwd `/Users/cobalt/cobalt`, so the sentences add the absolute folder path):
- GROK, launched ≈ 09:02:19, returned by 09:14:52 (≤ 12 min): `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "You are GROK. The folder is scratch/tribunal-bars-0920/voice-v1-check-a/ (absolute path /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v1-check-a/). Start with QUESTIONS-VOICE-V1-A.md and follow it exactly. final-v1.part1.md / final-v1.part2.md and rows.part1.md / rows.part2.md are split into ordered parts: read each pair in order as one file. Do not open any *-check-*.md file. Write your complete check to /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v1-check-a/grok-check-a.md and reply with only that path."` (no `--always-approve`).
- OPUS, launched ≈ 09:02:19, returned 09:05:39 (≈ 3 min): `claude -p --model claude-opus-5-5 "<same sentence with OPUS> Read files with the Read, Grep and Glob tools only. Write no file. Print your complete check as your answer." --permission-mode plan --add-dir /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v1-check-a --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"`. I wrote `opus-check-a.md` from its stdout (without the harness's closing `[exited with code 0]` line).
- SOL: not launched (METER). ASTRA: not launched.

WRITTEN-NOTHING PROOF: `ls -la` of the packet folder and of `/Users/cobalt/cobalt-wt/voice-v1` before launch (08:59 / 09:01) and after each return (09:05, 09:14). Worktree listing identical to the last byte of every entry in all three (newest mtime Sep 23 15:08). Packet folder: the only new entry after the launches is `opus-check-a.md` (mine, 09:05); **no `grok-check-a.md` exists**. No other new or changed entry in either folder; `ls -lat` of the repo root shows nothing modified after 08:54 except `.git` and `logs`. `grep -c -i "denied\|not allowed\|permission"` on `opus-check-a.md` = 0.

## CONTINUE

next: none — collated; report closed.

## Per chunk

| chunk | what it builds | grok | opus | sol | checkers answering CLOSED |
|---|---|---|---|---|---|
| C7 | read tools, code templates, figures check, hard refusals | did not check | NOT CLOSED — `tools.py:50-53`: `_ORDER` has no platform term and misses `short N`-type verbs; tests only use `short QRS at market` | not seated | 0 of 1 |
| C8 | `set_card_stop` extraction; route output pinned; dry-run writes nothing | did not check | CLOSED | not seated | 1 of 1 |
| C9 | migration 0017 `voice_turns` + single-flight store, reaper, no bytes | did not check | CLOSED (notes a vacuous assertion at `test_voice_store.py:143-144`) | not seated | 1 of 1 |
| C10 | confirm: exact-word match, single-flight, re-hash before write | did not check | NOT CLOSED — `tools.py:233`: no test changes only the card state, so the `target_sha256` clause can be deleted with every test green | not seated | 0 of 1 |

## Laws and boundary

| checker | (a) weaker assertions | (b) outside the files | (c) silent failure | (d) vault bytes |
|---|---|---|---|---|
| grok | — (no check) | — | — | — |
| opus | "NONE. `test_archiver_migrations.py`: `range(1,12)` → `[*range(1,12),17]`, `[-2:]` → `[-3:-1]`, and `voice_turns` excluded from the rollback survivors. Each follows the stated L68 numbering (0017 sits above both rollback bounds), not observed output. The pins only grew, `[:4]` → `[:5]`." | "`src/cobalt/db_migrations/__init__.py` (FORWARD/REVERSE registration) and the five pin tests … The builder named all of these. Nothing under radar, cards, vaultwrite, heartbeat, cobalt_agent, `configs/config.yaml` or `ops/*.plist`. DevDoc slip: `db_migrations/__init__.md` says "four registry pins"; five changed (a-devdocs.md:219-221)." | "`confirm.py:99` [a-code:599] DOES (A5). The `EXECUTING → DONE` return value is ignored. If a turn reaps the row at the 60 s `executing` limit (`store.py:65`) while `record_stop_edit` is still waiting on `FOR UPDATE`, the stop is written and the reply says "Done". The row stays `failed: reaped_executing` with no `expert_write_id`, and nothing logs it." | "NONE." |

## Checked against the branch

Files: originals under `/Users/cobalt/cobalt-wt/voice-v1/` (Read tool / grep), commits from the shared store.

| # | claim · who | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| 1 | C7 NOT CLOSED (A1): `_ORDER` has no platform term and misses order verbs (`short N`, `go long`, `exit`, `close my position`, …) · opus | `src/cobalt/voice/tools.py:50-53` | **HOLDS** | The regex's alternation holds buy/sell/cover/flatten/execute/market/limit/stop/place/cancel-type words only; no `DAS`/`Lightspeed`/`platform`/`short`/`exit`/`close`. Order tests (`test_voice_tools.py:133-141`) name none of them. |
| 1a | example `open DAS and flatten nothing` gets no `refuse` · opus | `tools.py:51` | **DOES NOT HOLD** for that input | `flatten` is in `_ORDER`, so it is refused. `log into Lightspeed` and `short 100 QRS` match no pattern in `_ORDER` or `_LOGIC` (`tools.py:50-58`): no code refusal for either; `short 100 QRS` vs stop 12.60 is ratio 7.94, under the 10× guard (`tools.py:192`). Whether a Plan then plans an act: NOT CHECKABLE FROM READS (live model). |
| 2 | C10 NOT CLOSED (A2): only the stop-changed case is tested; the `target_sha256` clause can be deleted with tests green · opus | `tools.py:233`; `test_voice_card_stop.py:148-160`; `test_voice_tools.py:188,196-197` | **HOLDS** | `grep -rn target_sha256 tests` names only `test_voice_tools.py:188/196/197`; the execute test moves the stop, which changes `diff_sha256` too, so `TargetChanged` still raises without the `target` clause. No test varies only `card_state`. |
| 3 | silent failure (A5): `EXECUTING → DONE` return ignored; reply says "Done" · opus | `src/cobalt/voice/confirm.py:99-101`; `store.py:65,116-126,140-156` | **HOLDS** as a code path | `store.transition(...DONE...)`'s bool is discarded and `PendingOutcome("done", …)` is returned at 101; the reaper fails `executing` rows past 60 s (called from `turn.py:371`, `web.py:177` — part D files). That the timing occurs: NOT CHECKABLE FROM READS. |
| 4 | vacuous assertion `test_voice_store.py:143-144` · opus (inside C9 CLOSED) | `tests/cobalt/test_voice_store.py:143-144` | HOLDS (fact) | The set holds names starting `audio_`, minus the four allowed; `"audio"` can never be in it. The `ValueError` line 146 is real. Not a class under the prompt; recorded, not counted. |
| 5 | DevDoc says "four registry pins"; five changed · opus | `docs/40 - DevDocs/cobalt/db_migrations/__init__.md` (a-devdocs `:219-221`) | HOLDS (fact) | The doc names four tests; `test_radar_score_migration.py` is the fifth. Prose slip, not a class; recorded, not counted. |
| 6 | (A3) normalization is wider than the FINAL's "casefold, strip" · opus, ASK DESK | `confirm.py:40-41`; `test_voice_confirm.py:47` | HOLDS (fact) — a desk question, not a defect claim | Code does NFKC + casefold + strip + strip `. , ! ?`; test pins `Yes.` `yes!` `Yes?` and fullwidth. The build report `## C10` states the same rule. Whether it stands is not for this hub. |
| 7 | (A4) card read at `tools.py:228` then again at `card_stop.py:43`: a sheet edit between is overwritten · opus, PLAUSIBLE | `tools.py:228`; `card_stop.py:43` | NOT CHECKABLE FROM READS | Two reads exist as stated; a concurrent edit landing between them needs two live requests. Not restated as a defect (L70). |
| 8 | C8: route output byte-identical; only path to the card is `set_card_stop` · opus | `stop-route-before-after.md:29 vs :59`; `test_voice_card_stop.py:183-204` | consistent with the files | Only `current["stop"]`/`new_stop` → `edit.from_stop`/`edit.to_stop`; that the pins were captured on base `04b05cd4` is the builder's claim — NOT CHECKABLE FROM READS. |
| 9 | (a) NONE for weaker assertions · opus | `a-diff.md` | see (iii) | Nine `-` lines carry an `assert`; each has a `+` replacement in its hunk (list below). |

Facts the prompt names, checked by me:
- **(i) BOUNDARY.** `git log --stat` names paths outside `43`'s WHAT YOU BUILD list: `src/cobalt/db_migrations/__init__.py`, `tests/cobalt/test_archiver_migrations.py`, `test_p4_migrations.py`, `test_radar_migration.py`, `test_radar_score_migration.py`, `test_tenancy.py` (all part A) — the build report `## C9 ### C` names them: "**Outside the WHAT-YOU-BUILD list, named (ESCALATE):** `src/cobalt/db_migrations/__init__.py` … and five existing registry pins, each gaining exactly the one `0017` entry (the setups branch did the same for 0013)". Also `tests/cobalt/test_radar_panel_cards.py` (part D) and `docs/40 - DevDocs/cobalt/db_migrations/__init__.md` (`## C9 ### D` names it). Quoted, not judged.
- **(ii) PROTECTED PATHS**, both calls: `git log --oneline 04b05cd4..28b6b0c6 -- src/cobalt/radar src/cobalt/cards src/cobalt/vaultwrite src/cobalt/heartbeat src/cobalt_agent configs/config.yaml` → EMPTY · `… -- ops/com.cobalt.aset.plist ops/com.cobalt.heartbeat.plist ops/com.cobalt.radar.plist` → EMPTY.
- **(iii) assertions / skips.** `-` lines with `assert` in `a-diff.md` (9): `FORWARD[-4:]` → `[-5:]` · `REVERSE[:4]` → `[:5]` · `numbers == list(range(1, 12))` → `[*range(1, 12), 17]` · `numbers[-2:] == [10, 11]` → `numbers[-3:-1] == [10, 11]` · `selected[:4]` → `[:5]` (radar_migration) · `reverse_names[:4]` → `[:5]` · two `_rollback_paths(...)[:4]` → `[:5]` (radar_score) · `selected[:4]` → `[:5]` (tenancy) — each with a `+` replacement in the same hunk. The `numbers[-2:]` → `[-3:-1]` line changes what the tail assertion selects (0017 now last); recorded as such. `skip`/`xfail` on `+` lines of `a-diff.md`: none. In the new part-A test files, `grep -n "skip\|xfail"`: `test_voice_tools.py` none · `test_voice_card_stop.py` none · `test_voice_confirm.py:35 requires_db = pytest.mark.skipif(` · `test_voice_store.py:38 requires_db = pytest.mark.skipif(` (both skip only without Postgres env).
- **(v) NO BYTES.** `grep -rn "bytea\|large object\|lo_import" src/cobalt/db_migrations src/cobalt/voice` → no output.
- **(viii) L32.** I read this report once before the last line: no ticker, price or spoken word of his written (the tickers and prices quoted are the tests' constructed values).

## Ready for a deploy

| checker | check line | ready | reason (verbatim) |
|---|---|---|---|
| grok | none (HARNESS) | — | — |
| opus | `CHECK VOICE V1 A: DEFECT REMAINS A1 A2 · ready for a deploy prompt: NO · platform refusal gap; target_sha256 re-check has no test` | NO | platform refusal gap; target_sha256 re-check has no test |
| sol | not seated (METER) | — | — |

**Grok, whole output (its stdout — no check, no file):** "I'll start from the questions file and follow it exactly.The refusal and confirm paths don’t match the rows. I’ll write the check from the code, tests, and design.The check file couldn’t be written in the scratch folder directly. I’ll write it through the shell." — recorded `grok: HARNESS — could not write the check file; no CHECK VOICE V1 A line`, kept whole, not relaunched (one attempt per house). Cause not established: the hub's cwd was `/Users/cobalt/cobalt`, not the intended `agy-trial`; the `--allow` path was absolute and correct.

## FOR THE CLASSIFIER

1. **Claim (verbatim, opus, part A):** "C7 — NOT CLOSED (A1): `tools.py:50-53` `_ORDER` has no platform term (DAS, Lightspeed, TradeStation, CenterPoint, "platform"). It also misses order verbs like `short N`, `go long`, `exit`, `close my position`, `get me out of`, `take profits`, `scale out.`" — my file:line `src/cobalt/voice/tools.py:50-53` (and the order tests `test_voice_tools.py:133-141`) — HOLDS. (Its first example input, `open DAS and flatten nothing`, is refused through `flatten`: that example DOES NOT HOLD; the class HOLDS on `log into Lightspeed` and `short 100 QRS`.)
2. **Claim (verbatim, opus, part A):** "C10 — NOT CLOSED (A2): `tools.py:233` re-checks both hashes, but no test changes only the card state." — my file:line `src/cobalt/voice/tools.py:233` with `tests/cobalt/test_voice_card_stop.py:148-160` and `test_voice_tools.py:188,196-197` — HOLDS.
3. **Claim (verbatim, opus, part A):** "`confirm.py:99` DOES (A5). The `EXECUTING → DONE` return value is ignored." — my file:line `src/cobalt/voice/confirm.py:99-101` — HOLDS (code path; the timing that triggers it is NOT CHECKABLE FROM READS).

## ESCALATE

1. **Opus: `DEFECT REMAINS A1 A2`** — see the check line above.
2. **`## FOR THE CLASSIFIER` items 1–3** (A1 order/platform refusal gap · A2 `target_sha256` re-check unpinned · A5 ignored `EXECUTING → DONE` return). `defects that HOLD: 3`.
3. **A claim carried to another part:** opus's "the no-model-call routing while `awaiting_confirm`, the rule that another transcript is not planned in the same turn, and CLI `--confirm` in production are all in `turn.py`/`cli.py`" — PART D — carried to `19-voice-v1-check-d.md` (counted in neither total here).
4. **A checker that did not check:** `ASK DESK: grok did not check part A (HARNESS — its Write into the packet folder was refused and it wrote no check file; stdout quoted above) — relaunch it alone before the merge? [09:15 ET]`. Safe default taken: no retry by this run; the seated floor (Opus 5.5 + Grok) is NOT met on this report.
5. **`ASK DESK` (opus A3): the confirm-word normalization** (`confirm.py:40-41` NFKC + casefold + strip + strip `. , ! ?`) is wider than the FINAL's "Unicode casefold, strip"; `Yes.` / `Yes?` execute. The builder's report states the rule and says X-X1 / X-E2 were counted with it. Which rule stands is not this hub's. [09:15 ET]
6. **Seats:** `sol: METER — retry after Sep 26th, 2026 6:47 AM` · `astra: NOT SEATED — Sol's Codex meter, same return time; no string on this line` — the desk seats both from then (L62 R19).
7. **Hub environment:** this run's cwd was `/Users/cobalt/cobalt`, not `agy-trial` as the launch's first bare command intends; paths were absolute. The desk may want to confirm the launch shape (it is the only difference from prior hubs seen here, and Grok's Write failure is the only observed effect).
8. **L74:** the block quoted under `## L74` (recorded once, not followed).
9. Standing line: **"This check covers voice V1 only, PART A of four (the ordered act) of `04b05cd4..28b6b0c6` of `voice/v1-0923`; parts B, C, D (`17`, `18`, `19`) cover the rest, every file in exactly one part. It is round 1 of ≤3 (L67 / L39). With the seated checkers (Opus 5.5 + Grok, L67 as amended 2026-09-24) checked on EACH of the four parts and `defects that HOLD: 0` in all four, the branch is READY for a stacked deploy prompt; a HOLD goes to a classifier and a fix round — and the branch waits out of that evening's set if the fix cannot land and be checked first (L43's drop rule)."**
10. Standing line: **"The DEVICE SESSION (E1, E3 on his phone's file, E5, E8 / X3 behind `tailscale serve`) is OWED (no `voice-v1-device-*.md` record exists): a design-changing device result is a fix round before the ship, whatever this check reads."**
11. Standing line: **"V1's production deploy needs, beyond the merge: the migration (`--allow-prod`), the model files in the production `model_dir`, the `COBALT_VOICE_*` exports live in `ops/start_aset.sh`, and `com.cobalt.aset` restarted inside the pause (L43 / L66) — the deploy prompt carries each (build ESCALATE (vi))."**
12. Standing line: **"L68 GATE EARLY (amended 2026-09-24) asks every BUILD's stop line to quote offline, with-DB AND live-note results; V1's built line (09-23, before the clause) quotes offline and with-DB only — the desk rules whether the live-note result is owed before the merge."**

VOICE V1 CHECK DONE · part: A (the ordered act) · grok: HARNESS — check file could not be written, no CHECK VOICE V1 A line · opus: CHECK VOICE V1 A: DEFECT REMAINS A1 A2 · ready for a deploy prompt: NO · platform refusal gap; target_sha256 re-check has no test · sol: METER — retry after Sep 26th, 2026 6:47 AM · astra: NOT SEATED (Sol's Codex meter, Sep 26th, 2026 6:47 AM; no string on this line) · defects that HOLD: 3 · ESCALATE: 12
