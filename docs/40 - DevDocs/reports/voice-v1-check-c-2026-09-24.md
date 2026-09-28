# Voice V1 check — PART C of four (audio, model files, config, experiments) · 2026-09-24

## §0 Headline

- Part C (audio, model files, config, experiments) of `04b05cd4..28b6b0c6` on `voice/v1-0923`, round 1 of ≤3: PREFLIGHT green; packet 211,524 B staged and fidelity-checked; Opus 5.5 + Grok checked; Sol METER (back Sep 26th, 2026 6:47 AM), Astra NOT SEATED.
- Opus: `DEFECT REMAINS C4` · ready NO. Grok: `BUILD STANDS EXCEPT C2, C5` · ready NO. Floor (Opus 5.5 + Grok) met; the two contradict on C4 (Grok CLOSED, Opus NOT CLOSED) — the hub's file-check HOLDS the write-failure path.
- File-check: **defects that HOLD: 9** (C4 write leak · C2 resident skips backup refusal · empty-env fallback · already-gone line dropped · 4 loose assertions · dead `plan_route` with a false comment); Grok's C5 claim (empty transcript) DOES NOT HOLD — the path is in part D's `turn.py:383-384`. Protected paths EMPTY; no audio; side B (no age test, called at startup only).
- ESCALATE: 14. Device session: NOT RUN.

## L74

No block arrived inside a tool result asking for a `Claude-Session` line or naming a file-send tool so far. (The harness's own attribution reminder is not a tool result.)

## PREFLIGHT

date: `Thu Sep 24 10:57:47 EDT 2026`.

| rule | command | result |
|---|---|---|
| THE GROK GATE (first) | `grep -n "^| R17 " cto-2026-09-24.md` · `git log -1 -S"Grok approved with no asking going forward"` | row 27 carries `Grok approved with no asking going forward`; commit `1758fd78a572f47b613b2ca831dcfa636ed8f65a` — allowed |
| `grok --version` | `grok --version` | `grok 1.0.25 (f7e67d6988e2) [stable]` — allowed |
| R13 of 09-20 | `grep -n "^| R13 " cto-2026-09-20.md` | row 86 printed — allowed |
| R40 | `grep -n "^| R40 " cto-2026-09-21.md` | carries `ONE EXTRA DOT THAT CANNOT BE TAPPED` — allowed |
| R44 | `grep -n "^| R44 " cto-2026-09-21.md` | carries `ONE BUILD of the whole FINAL` — allowed |
| R46 + committed | `grep -n "^| R46 "` · `git log -1 -S"instead of Astra you can use Sol"` | carries the phrase; `53e059456750c0c9efcf50222a7a647630dc4b04` — allowed |
| R49 (Sol string) | `grep -n "^| R49 "` · `grep -c -F` Sol string (1) · `git log -1 -S` Sol string | carries `"Approved"`; count 1; `60147d400b009db5a2518e02b8ab1fe5765db405` — allowed |
| R32 (Opus 5.5 string) | `grep -n "^| R32 " cto-2026-09-22.md` · `git log -1 -S"Bash(claude -p --model claude-opus-5-5 *)"` | row 131 carries `claude -p --model claude-opus-5-5`; `b8a72b5300370e248cd6c7a8a732258fec03e6a0` — allowed |
| THE TWELVE + THREE (`08`) | `grep -c -F -e '<rule>'` on `08-bars-chunk-e-check.md`, each with quotes | `Bash(grok *)` 1 · mkdir 1 · git show 1 · git log 1 · s2-p2 show 1 · s2-p2 log 1 · s2-p2 diff 1 · ls 1 · grep 1 · tail 1 · wc 1 · date 1 · `AskUserQuestion` 1 · `EnterWorktree` 1 · `Bash(git push*)` 1 — all 1 |
| Astra / agy strings absent | read of this prompt's launch line | neither `gpt-6-astra` nor `Bash(agy *)` is in the launch line — allowed |
| R57 design approval | `grep -n "^| R57 " cto-2026-09-23.md` · `git log -1 -S"approved design"` | row 60 carries `approved design`; `ffee37ad5e41ab5eb451406a9e11a9e03b26afdb` — allowed |
| build launch + stop record | `grep -n "43-voice-v1-build.md" cto-2026-09-23.md` · `grep -n -o … VOICE V1 BUILT` · `git log -1 -S"VOICE V1 BUILT"` | launch row R63 (line 66, also R60 line 63); later row R71 (line 74) carries `VOICE V1 BUILT 566d1848`; `9cc68741bc8cd656d4d2e3f9d7189ad8fabba2d8` — allowed |
| re-cut committed | `git log -1 -S"VOICE V1 CHECK RECUT" -- reports/voice-v1-check-recut-2026-09-24.md` | `80b208c5d1304bd99ec44fe1b6dfd84fc3c91b3c` — allowed |
| THIS launch R37 | `grep -n -F "18-voice-v1-check-c.md" cto-2026-09-24.md` · `git log -1 -S"18-voice-v1-check-c.md" -- cto-2026-09-2*.md` | row 47 (`R37`) names this file; `e9652bdbcecfeebe988e8887fea5a08317ac84ba` — allowed |
| PART B HAS STOPPED | `tail -n 3 reports/voice-v1-check-b-2026-09-24.md` | last non-blank line: `VOICE V1 CHECK DONE · part: B (the model path) · grok: CHECK VOICE V1 B: BUILD STANDS · ready for a deploy prompt: YES · opus: CHECK VOICE V1 B: DEFECT REMAINS C6, THIRD-a (minor) · ready for a deploy prompt: NO · resolver binds an ambiguous card from incidental side/ordinal words · sol: METER — retry after Sep 26th, 2026 6:47 AM · astra: NOT SEATED (Sol's Codex meter, Sep 26th, 2026 6:47 AM; no string on this line) · defects that HOLD: 2 · ESCALATE: 12` — starts `VOICE V1 CHECK DONE · part: B`; its verdict is not a gate here (L72) |
| worktree | `ls /Users/cobalt/cobalt-wt/voice-v1` | present |
| THE BUILT LINE | `tail -n 3` build report | last non-blank line: `VOICE V1 BUILT 566d1848 \| on 04b05cd4 \| migration 0017 \| offline 2422/0 \| with-DB 2774/0 \| experiments run: 12 of 12 \| design-changing results: 3 \| stt: faster-whisper/tiny.en \| plan route: local.plan (mainframe) \| device session: OWED (E1 E3 E5 E8 X3) \| RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar (6 UNCLASSIFIED) \| tests added: 471 \| ESCALATE: 14` — `<base>` = `04b05cd4` = the measured base |
| `<tip>` | `git log --oneline -1 28b6b0c6` | `28b6b0c6 feat(voice-v1): build report` |
| THE RANGE | `git log --oneline 04b05cd4..28b6b0c6` | 15 commits (recorded) |
| branch tip | `git log --oneline -1 voice/v1-0923` | `28b6b0c6 feat(voice-v1): build report`; `git log --oneline 28b6b0c6..voice/v1-0923 -- tests src configs ops pyproject.toml uv.lock "docs/40 - DevDocs/cobalt" "docs/40 - DevDocs/tests"` → EMPTY |
| THE BOUNDARY | `git log --stat --oneline 04b05cd4..28b6b0c6` | every path is in `43`'s list per the re-cut report; no extra path row for part C |
| THE SPLIT IS TOTAL | stat list (84 unique paths) against the re-cut `## Split` | all 84 in exactly one row (A 25 · B 26 · C 19 · D 13 · build report 1) — nothing unassigned |
| NEW VS CHANGED | `git log --diff-filter=A --name-only --format=` | 67 paths; the 16 whole-staged part-C paths printed; `ops/start_aset.sh`, `pyproject.toml`, `uv.lock` NOT printed — as the re-cut staged them |
| `.env` | `ls /Users/cobalt/cobalt-wt/voice-v1/.env` | `No such file or directory` — expected |
| scratch C | `ls scratch/tribunal-bars-0920/voice-v1-check-c` | `No such file or directory` — fresh run |
| sources | `ls scratch/tribunal-bars-0920/voice-v1-check/A` · `…/B` | A: `final-v1.part1/2`, `seam-s1`, `rows.part1/2`, `rulings`, `l28` all present; B: `build-report-B.part1.md` present |
| THE STAGGER | `grep -n -F "no other house hub is running" cto-2026-09-24.md` | row R37 (line 47) carries the literal AND names `18-voice-v1-check-c.md` — allowed |
| THE CODEX LAUNCH SHAPE | `grep -c -F "Experiment field: **reads started**" setups-tribunal-r2-2026-09-21.md` | `1` → a Sol launch appends ` < /dev/null` |
| PROBE Sol | `codex exec … -m gpt-5.6-sol … "Reply with only the word OK." < /dev/null` | exit 1: `ERROR: You've hit your usage limit. … try again at Sep 26th, 2026 6:47 AM.` → `sol: METER — retry after Sep 26th, 2026 6:47 AM`; SKIPPED, not relaunched; `astra: NOT SEATED — Sol's Codex meter (Sep 26th, 2026 6:47 AM)` |
| PROBE Opus | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` | `OK`, exit 0 — UP |
| PROBE Grok | `grok --version` | UP |
| FLOOR | Opus 5.5 + Grok | both UP — floor met |

## Packet

Folder: `scratch/tribunal-bars-0920/voice-v1-check-c/` (14 files, staged 11:01–11:12 ET).

MEASUREMENT gate (before the first Write): every whole-file original `wc -c` equalled the re-cut's table — code 579 / 6,517 / 3,924 / 9,487 / 6,851 · yaml 2,227 / 2,728 · fixture 8,142 · tests 11,403 / 8,373 / 5,442 · DevDocs 620 / 1,993 / 871 / 1,636 / 1,372 · the seven context files and the experiments source (24,761) equalled their stated sizes. Saved git outputs (each `run_in_background`, harness saved file): `ops/start_aset.sh` diff 1,147 B, `pyproject.toml` diff 615 B, `uv.lock` full diff **26,366 B**, the `grep -n -v` excerpt **1,708 B** — each equal to the re-cut's number; `grep -c "^diff --git"` = 1 on each (table: 1 block each). No "packet — re-measure" stop.

| staged file | bytes | contents | fidelity |
|---|---|---|---|
| `c-code.md` | 27,671 | 5 new `.py` files, whole (579 · 6,517 · 3,924 · 9,487 · 6,851) | piece sizes from `grep -b` header offsets = the originals exactly; line-set check clean |
| `c-config.md` | 17,141 | `agents/voice.yaml` 2,227 · `voice.yaml` 2,728 · utterance set 8,142 · ops diff 1,147 · pyproject diff 615 · uv.lock EXCERPT 1,708 | piece sizes exact; line-set check: flagged 13 = 7 blank + 6 headers |
| `c-tests.md` | 25,428 | 3 test files, whole (11,403 · 8,373 · 5,442) | piece sizes exact; flagged 186 = 183 blank + 3 headers |
| `c-devdocs.md` | 6,874 | 5 DevDocs, whole | piece sizes exact; flagged 23 = 18 blank + 5 headers |
| `build-report-c.md` | 6,292 | report lines 226–238 (3,084) · 254–265 (1,876) · 266–277 (1,035) | piece sizes exact; flagged 6 = 3 blank + 3 headers |
| `build-report-experiments.md` | 24,761 | copy of `voice-v1-check/B/build-report-B.part1.md` (lines 62–213 of the report) | size equal; line-set: only blank lines flagged (one typing slip of mine — `configs/cobalt/strategies.yaml` written without `cobalt/` — found by that check BEFORE launch and fixed; re-measured 24,761) |
| `final-v1.part1.md` · `final-v1.part2.md` | 15,586 · 21,457 | context, copied | sizes equal; flagged = blank lines only (16 = 16 · 20 = 20) |
| `seam-s1.md` | 14,433 | context, copied | equal; flagged = blank (22 = 22) |
| `rows.part1.md` · `rows.part2.md` | 13,946 · 21,984 | context, copied (`rows.part1.md` line 25 keeps its one trailing space) | equal; flagged = blank (3 = 3 · 4 = 4) |
| `rulings.md` · `l28.md` | 4,080 · 4,701 | context, copied | equal; flagged = blank (3 = 3 · 0 = 0) |
| `QUESTIONS-VOICE-V1-C.md` | 7,170 | the verbatim question text + the appended "Files in this folder:" paragraph (CHECKED / CONTEXT per file) | typed from this prompt; one added clause ("read in order as one file `final-v1.md`") in the file list |

`uv.lock` EXCLUSION: the whole diff (26,366 B, 1 block, commit `cc2e95b6`) is NOT staged; the 1,708 B excerpt (added `av` 18.1.0, `ctranslate2` 4.8.2, `faster-whisper` 1.2.1, `flatbuffers` 25.12.19, `onnxruntime` 1.30.0, their dependency edges and hunk headers) is a piece of `c-config.md`.
Device-session record: `ls …/reports/voice-v1-device-*.md` → no match → **device session: NOT RUN** (not staged, not a defect). (One earlier attempt at that listing used a `| grep -c` pipe against the "no pipe" rule — count 0 — and was redone with a bare `ls` glob; recorded here as a rule slip of mine.)

HONEST SIZE: checked files 83,537 B (27,671 + 17,141 + 25,428 + 6,874 + 6,292) + experiments 24,761 + context 96,187 + QUESTIONS 7,170 = **211,524 B** (`wc -c` total of the 14 files) — under the 230,000 B ceiling with 18,476 B spare (the re-cut projected 213,549 B). ≈ **52,881 tokens per checker** (÷ 4). Largest staged file 27,671 B (≤ 38,000 B).

Launches (both `run_in_background`, independent, ONE attempt each; cwd `/Users/cobalt/cobalt-wt/agy-trial`; `date` before launch **Thu Sep 24 11:13:37 EDT 2026**; the Grok gate's second row re-run then: R17 row 27 and `git log -S` = `1758fd78a572f47b613b2ca831dcfa636ed8f65a`):
- GROK: `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "You are GROK. The folder is scratch/tribunal-bars-0920/voice-v1-check-c/ (absolute path /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v1-check-c/). Start with QUESTIONS-VOICE-V1-C.md and follow it exactly. final-v1.part1.md / final-v1.part2.md and rows.part1.md / rows.part2.md are split into ordered parts: read each pair in order as one file. Do not open any *-check-*.md file. Write your complete check to /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v1-check-c/grok-check-c.md and reply with only that path."` (no `--always-approve`; the spelling is part B's, as run at 10:32).
- OPUS: `claude -p --model claude-opus-5-5 "You are OPUS. The folder is scratch/tribunal-bars-0920/voice-v1-check-c/ (absolute path …). Start with QUESTIONS-VOICE-V1-C.md and follow it exactly. <the same parts sentence> Do not open any *-check-*.md file. Read files with the Read, Grep and Glob tools only. Write no file. Print your complete check as your answer." --permission-mode plan --add-dir /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v1-check-c --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"`.
- SOL: not launched (METER, retry after Sep 26th, 2026 6:47 AM). ASTRA: NOT SEATED (Sol's Codex meter; no string on this line).

WRITTEN-NOTHING PROOF — before launch (11:13): packet folder = the 14 staged files (newest mtime 11:12); `/Users/cobalt/cobalt-wt/voice-v1` newest top-level mtime Sep 23 15:08 (`ops` 14:08, `scratch` 13:47, `src` 13:44, `tests` 13:45, `pyproject.toml` / `uv.lock` 13:51).

CHECKER RUNS: OPUS launched 11:14, returned 11:18 (≈ 4 min); stdout written by me to `opus-check-c.md` (10,504 B, lines up to its `CHECK VOICE V1 C:` line; the harness's `[exited with code 0]` footer left out). GROK launched 11:14, returned 11:27 (≈ 13 min, under the 45-minute clock); its stdout was only the path of `grok-check-c.md`, which Grok wrote itself through its approved `--allow` (12,883 B). Neither timed out. `grep -c -i "denied\|not allowed\|permission"` = 0 on both check files. SOL: METER (not launched). ASTRA: not launched (R46).
WRITTEN-NOTHING PROOF — after Opus (11:18) and after Grok (11:27): packet folder = the 14 staged files unchanged (same sizes and mtimes) + `opus-check-c.md` (mine, 11:18) + `grok-check-c.md` (Grok's own, 11:27); no other new or changed entry. `/Users/cobalt/cobalt-wt/voice-v1` listing identical to the pre-launch listing in every entry (newest top-level mtime Sep 23 15:08). No entry marked `WROTE:`.

## CONTINUE

next: none — collated; report closed.

## Per chunk

| chunk | what it builds | grok | opus | sol | checkers answering CLOSED |
|---|---|---|---|---|---|
| C2 | voice config + agent registry; path refusals, missing key crashes, yes/no words | NOT CLOSED — `c-code.md:112-114`, `:118-129`: "The backup refusal does not run on the resident load … `load_voice_config()` with no `backup_sources`" and a path under a backup source outside repo and vaults still loads; tests pass | CLOSED — `c-code.md:96-115,151-157`; notes: backup refusal not enforced at runtime; `plan_route` "never checked"; `REPO_ROOT` from a worktree accepts a main-checkout path | not seated (METER) | 1 of 2 |
| C4 | scratch writer, one unlink, side-B start sweep, directory lock | CLOSED — `c-code.md:405-415`, `:438-446`, `:434`, `:497-518`, `:449-465` (its own (c) adds: "An `os.write` / `os.chmod` failure inside `write_scratch` happens before `turn_audio`'s `try` … that partial file is not unlinked") | NOT CLOSED — `c-code.md:387-395`, `:441-442`: `os.write` raises (disk full / I/O error) → partial file left, no unlink, no RED, until restart; `os.write` return ignored | not seated | 1 of 2 |
| C5 | local faster-whisper Transcriber, pinned, off the loop, missing model a named RED | NOT CLOSED — `c-code.md:674-684`: "No branch in this part says 'I heard nothing' … `test_voice_transcribe.py` has no empty-transcript test" | CLOSED — `c-code.md:609-611`, `:614-615`, `:708-710`; "empty transcript lands nothing" belongs to the turn function (part D), not checkable here | not seated | 1 of 2 |

## Per experiment

Build outcomes are quoted from `build-report-experiments.md`. Device rows have no `### X-<id>` section (the built line: `device session: OWED (E1 E3 E5 E8 X3)`).

| id | the build's outcome | grok | opus | sol |
|---|---|---|---|---|
| E1 | no section (device session) | OWED (device session) | OWED (device session) | not seated |
| E2 | "OUTCOME: NO CHANGE — a size meets the bar; CPU faster-whisper stands." | RUN — follows from the quoted output | RUN — follows; caveats: 14 distinct texts ×3 voices, container assumed (E1) | not seated |
| E3 | no section (device session) | OWED | OWED | not seated |
| E4 | "OUTCOME: DESIGN-CHANGING — while any other client holds `mainframe`, a voice Plan call queues behind that whole generation (60–72 s measured)." | RUN — follows (contended n = 12 of 65) | RUN — follows; "summary was recomputed by a parser that is not quoted" | not seated |
| E5 | no section (device session) | OWED | OWED | not seated |
| E6 | "OUTCOME: NO CHANGE — both the transcribe and the Plan call are off the loop" | RUN — follows | RUN — follows | not seated |
| E7 | not in this copy: report `## C13` line 363 and `## WITH-DB` line 383 ("X-E7 kill -9 / restart GREEN") | "NOT RUN — no `### X-E7` in the staged experiments … No stated reason." | "No `### X-E7` in the staged section … cannot check it from this folder" | not seated |
| E8 | no section (device session) | OWED | OWED | not seated |
| E10 | "OUTCOME: NO CHANGE by the letter … FLAGGED, not assumed away: the `av` wheel bundles `libx264` / `libx265`…" + `ASK DESK … safe default taken: continue the build (the letter of the gate is not met; the desk decides before ship)` | RUN — follows; notes the paragraph says both "NO CHANGE by the letter" and "the letter of the gate is not met" | RUN — "the output does not support the 'no GPL' conclusion"; FFmpeg lines show `--enable-libx264 --enable-libx265`; "the build took 'continue'" | not seated |
| X1 | "OUTCOME: NO CHANGE — 0 of 70" | RUN — follows | RUN — follows | not seated |
| X3 | no section (device session) | OWED | OWED | not seated |
| X5 | "OUTCOME: DESIGN-CHANGING — a NEW wrong-value path" (6 of 24 price clips); default: 10× clarify + read-back | RUN — follows | RUN — follows; carried as ASK DESK | not seated |
| X12 | "OUTCOME: NO CHANGE to the parser rule" | RUN — follows | RUN — follows | not seated |
| X13 | not in this copy: report `## C9` line 322, `## C10` line 334, `## WITH-DB` line 383 | "NOT RUN — no `### X-X13` in the staged experiments" | "Not in the staged section (placed in C10, with-DB)" | not seated |
| G2 / K5 | "OUTCOME: NO CHANGE (C2 test)" | NOT RUN — the build's stated reason (start-only sweep); the age check is a C2 test that exists | NOT RUN as a sweep-during-decode run — same reason | not seated |
| X20 | "OUTCOME: INFORMATIONAL (gates nothing)" | RUN — follows | RUN — follows | not seated |
| X22 | "OUTCOME: DESIGN-CHANGING — the old holder survives a `kill -9` of the job pid while launchd respawns …" (keep the lock) | RUN — launchd half follows; by-hand half not a by-hand conclusion (confounded, said so) | RUN — follows for the launchd half; by-hand half confounded | not seated |

Other experiment answers (verbatim, ≤ 30 words each): **design-changing carried?** grok — "Whether a later `## ESCALATE` repeats those four is not in this folder." · opus — "The build report's `## ESCALATE` section is not staged here, so I cannot confirm the carry. E10's safe default is not the FINAL's." **Tunables traceable?** grok — "match a quoted measurement or the allowed 'engine default — FINAL §11 W7' line" (the "four turns add a few hundred tokens" clause "is not a quoted measurement") · opus — measured: model / revision / compute type / `stt_timeout_s`; `history_turns` partly; four "engine default"; `modelaccess.yaml` "not in this folder". **Lock diff GPL / AGPL / unexpected native?** grok — "No GPL or AGPL line is quoted. No native package outside `av`, `ctranslate2`, and `onnxruntime`" · opus — "None is AGPL, and the native packages are the expected ones. The only GPL material is the x264/x265 bundled inside `av`".

## Laws and boundary

| | grok | opus |
|---|---|---|
| (a) weaker assertions | `c-tests.md:130` accepts `"docs"` or `"repo"` (a docs path that only hits the repo refusal still passes); `c-tests.md:264-268` asserts `AgentConfigError` only; `c-tests.md:195` uses `str.startswith`, not `_under` | 1. `c-tests.md:65-70` — the source-line test is vacuous ("any earlier `# source:` satisfies the check"); 2. `c-tests.md:626` — `t.revision` checked against the config the code copies in; 3. `c-tests.md:538-542` — counts only `os.unlink(` inside `scratch.py` |
| (b) outside WHAT YOU BUILD | NONE (`ops/start_aset.sh` two exports; `pyproject.toml` one line; no plist / heartbeat / vaultwrite / top-level `configs/*.yaml`) | NONE (same list) |
| (c) silent failure | "NO PATH that turns a dead engine into success"; but a subdirectory in scratch is RED-logged and skipped (logged, "not silent"); and an `os.write` / `os.chmod` failure inside `write_scratch` leaves the partial file (`c-code.md:387-396` vs `:441-446`) | 1. C4 write leak (`c-code.md:387-395`); 2. `c-code.md:143-146` — `COBALT_VOICE_*_DIR=""` is treated as unset → production silently falls back to the dev path; 3. `c-code.md:430-434` — a file "already gone" counts as a normal deletion and its AMBER line is dropped |
| (d) committed audio / a test reading a recording | NONE | NONE |

## Checked against the branch

Originals under `/Users/cobalt/cobalt-wt/voice-v1/` (Read tool / `grep`), which equal `28b6b0c6` (PREFLIGHT proves the branch has not moved). Line numbers are the ORIGINAL files'.

| # | claim · who | file:line | result | note |
|---|---|---|---|---|
| 1 | C4: `os.write` raising leaves a partial file; no unlink, no RED, until the restart sweep · opus (grok (c) same) | `scratch.py:113-121` (`os.open(O_EXCL)`, then `os.write` in a `try/finally` that only closes the fd); `:164-172` (`turn_audio`: `write_scratch` runs BEFORE its `try:`); `turn.py:183-201` (the only caller catches `ScratchRefused` / `ScratchUnlinkFailed`; an `OSError` propagates, `held` is never bound) | **HOLDS** | no test writes with a failing `os.write` (`grep ENOSPC` over `tests/` empty; `test_voice_scratch.py` has none) — the new tests stay green |
| 2 | `os.write`'s return value ignored (short write truncates the clip) · opus | `scratch.py:118` | **HOLDS** | the return value is not read; whether a regular-file write can return short is NOT CHECKABLE FROM READS |
| 3 | C2: resident load does not refuse a path under a backup source; only when `backup_sources=` is passed · grok (opus note) | `config.py:98-100` (loop over `backup_sources or ()`); `:104-116`, `:142-143` (the resident passes none); the docstring says so; `test_voice_config.py:151-157` passes the list, `:197-201` requires the resident not read `backup.yaml` | **HOLDS** | the build disclosed it: report C2 line 231 (`ASK DESK: C2 …` — safe default: the suite check); `backup.yaml`'s real sources are NOT CHECKABLE FROM READS (file not staged) |
| 4 | C2: no shape check — a route name that is a URL is accepted once registered · grok | `registry.py:57` (`route: str = Field(min_length=1)`), `:99-106` (membership in `load_routes().routes`) | HOLDS as stated | no failing input without editing `modelaccess.yaml`; rows.part2 C2 asks for "a validator [that] refuses anything that looks like a URL" — no such validator exists. Not counted (Grok gives no input that loads) |
| 5 | C5: no "I heard nothing" branch in this part; no empty-transcript test in `test_voice_transcribe.py` · grok | `transcribe.py:148-158` (`text=" ".join(...).strip()` may be `""`); `test_voice_transcribe.py` has no such test | facts HOLD; **the NOT CLOSED DOES NOT HOLD** | the path exists in part D: `turn.py:383-384` (`raise _Fail("empty_transcript", "I heard nothing.")`, both audio and text), tested at `test_voice_turn.py:240-244` |
| 6 | `COBALT_VOICE_*_DIR=""` treated as unset → falls back to the committed dev path · opus | `config.py:129-132` (`if os.getenv(SCRATCH_ENV):` — empty string is falsy) | **HOLDS** | the dev path passes every refusal; no test sets an empty value |
| 7 | a file "already gone" counts as a normal deletion and its AMBER line is dropped · opus | `scratch.py:135-136` (`FileNotFoundError` → `UnlinkResult(True, amber "already gone")`); `:153-160` (`unlink_now` appends a line only when `not r.ok`, then sets `deleted_at`) | **HOLDS** | in the sweep the line is kept (`:243`) |
| 8 | source-line test vacuous · opus | `test_voice_config.py:64-69` (`block = text.split(...)[0].rsplit("\n\n", 1)[-1]`); `grep -c "^$" configs/cobalt/voice.yaml` = 0 | **HOLDS** | with no blank line, `block` is the whole text before the key, which holds the `# source:` of `scratch_dir` (`voice.yaml:16`) for every tested key; the assertion `"# source:" in block` stays true if a key's own source line is deleted |
| 9 | `t.revision` checked against the config the code copies in · opus | `test_voice_transcribe.py:83`; `transcribe.py:154-156` (`revision=self.cfg.stt_revision`) | **HOLDS** | a load of a different snapshot would not change `t.revision`; the assertion stays true |
| 10 | one-unlink test counts `os.unlink(` only · opus | `test_voice_scratch.py:234-238` | **HOLDS** | a `Path.unlink()` / `os.remove` added in `scratch.py` leaves `src.count("os.unlink(") == 1` true |
| 11 | docs-or-repo assertion · grok | `test_voice_config.py:125-129` (`"docs" in str(e.value) or "repo" in str(e.value)`); refusal messages `config.py:86-89` | **HOLDS** | removing the docs refusal falls through to the repo refusal (message contains "repo"); the assertion stays true |
| 12 | `plan_route` in `voice.yaml` is never checked against the registry; the comment says it is · opus | `config.py:56-58` (comment "checked by the agent registry"); `grep -rn plan_route src/cobalt configs/cobalt` — readers: none (`turn.py:281,287` and `store.py:42` are DB record keys; `registry.py` never names it) | **HOLDS** | dead key; the turn's route comes from the registry (`web.py:176` `load_agent().route`); whether a mismatch matters is not a fact I judge |
| 13 | `REPO_ROOT` is the running checkout: from a worktree a main-checkout path is accepted · opus | `config.py:30` (`parents[3]`), `:88` | HOLDS as stated | dev only, opus itself rates it low and CLOSED; not counted |
| 14 | `audio/wav` in the content-type map but `max_upload_bytes` holds ≈ 20.8 s of 48 kHz 16-bit mono WAV, not 30 s · opus | `scratch.py:49-56`; `voice.yaml:29,31` | HOLDS as arithmetic (2,000,000 / 96,000 B/s) | the WAV rate is opus's assumption; not counted |
| 15 | E10: FFmpeg lines show `--enable-libx264 --enable-libx265`; `.dylibs` lists both; the build took "continue" · opus | `build-report-experiments.md` X-E10 section (report lines 71–102): the quoted probe line, the `.dylibs` sentence, `ASK DESK … safe default taken: continue the build` | quotes HOLD; "output does not support the 'no GPL' conclusion" DOES NOT HOLD | the report never concludes "no GPL": it says no new package's licence LINE is GPL/AGPL (supported by its quoted grep) and FLAGS x264/x265 itself. "Stock FFmpeg refuses those flags without `--enable-gpl`" = general knowledge, NOT CHECKABLE FROM READS. Carried as a desk item |
| 16 | scripts of E2 / E2b / X1 / X20 / E4 / E6 / X5 / E10 are described, not quoted whole (`rows.part1` X-A: "each script's text is quoted whole in its `### X-<id>` section") · opus | X-E10 "Script text (…): imports `av`, prints …" (a description); X-E2 "script: …" (a description); only X-X22 says "Script text written EXACTLY as the prompt block" | **HOLDS** (as a fact) | fits none of the listed classes; carried to ESCALATE as a fact |
| 17 | E7 / X13 not in the experiments section · both | report `## C13` line 363 and `## WITH-DB` line 383 (X-E7); `## C9` 322, `## C10` 334, 383 (X-X13) | **PART D — carried to 19** (X-E7) · **PART A — carried to 16** (X-X13) | counted in neither total |
| 18 | Grok NOT CHECKABLE: ASET startup calls `start_sweep` before the first request; the turn copies `deleted_at` onto the row · grok / opus | `aset/web.py:91` (`app.add_event_handler("startup", voice_web.voice_startup)`); `web.py:157-164` (lock, then `start_sweep`); `turn.py:202-206` (`audio_deleted_at=held.deleted_at` in a `finally`) | hub reading, **PART D — carried to 19** | a held lock raises `ScratchLocked` out of `voice_startup` (`web.py:161`); non-zero exit is NOT CHECKABLE FROM READS |
| 19 | Starlette's multipart spool may write uploads over 1 MiB outside `scratch_dir` · opus | — | NOT CHECKABLE FROM READS — PART D — carried to 19 | run an upload above the spool threshold and list the temp dir |
| 20 | grok: subdirectory in scratch survives the sweep (RED logged) | `scratch.py:231-236` | HOLDS as a fact; logged, not silent | not counted (Grok says so itself) |
| 21 | grok: `c-tests.md:264-268` asserts `AgentConfigError` only; `:195` uses `startswith` | `test_voice_config.py:263-267`, `:194` | HOLDS as facts | neither names a regression that stays green; not counted |

FACTS the check prompt promised, stated plainly:
- **(ii) PROTECTED PATHS**: `git -C /Users/cobalt/cobalt log --oneline 04b05cd4..28b6b0c6 -- src/cobalt/radar src/cobalt/cards src/cobalt/vaultwrite src/cobalt/heartbeat src/cobalt_agent configs/config.yaml` → EMPTY · `… -- ops/com.cobalt.aset.plist ops/com.cobalt.heartbeat.plist ops/com.cobalt.radar.plist` → EMPTY.
- **(iii) `skip` / `xfail`** in the new part-C tests: `test_voice_config.py` — no hit; `test_voice_scratch.py` — no hit; `test_voice_transcribe.py` — lines 5-6 (docstring "skip ONLY when the pinned model is absent … that skip is counted"), 41 (docstring "collection-time skipif"), 43 `pytest.skip("speech-to-text model absent from the dev model_dir")` (the EXPECTED `slow` skip-on-missing-model, counted in the build's C4 SUITE line: "8 passed, 3 warnings (0 skipped …)"), 46 `needs_say = pytest.mark.skipif(shutil.which("say") is None, reason="macOS `say` absent")` — a SECOND skip condition (`say` absent), not the model skip; recorded as a row.
- **(v) NO AUDIO**: `git log --stat --oneline 04b05cd4..28b6b0c6` read for `.webm .ogg .opus .mp4 .m4a .wav .aiff .aif .mp3 .flac .caf` → none (paths: `.md .py .yaml .sql .sh .toml .lock` only).
- **(vii) SIDE B, NOT SIDE A**: the tip's `scratch.py:223-244` `start_sweep(directory, lock)`: refuses without the lock (`:225-226`), then `for entry in sorted(Path(directory).iterdir())` skips `.lock`, RED-logs an unexpected directory, otherwise `unlink_scratch(entry, "start sweep — a turn died mid-way")`, AMBER per file, no time comparison. **age test present: no · called per turn: no** — `grep -rn "start_sweep" src/cobalt` → `voice/web.py:162` (inside `voice_startup`), `voice/scratch.py:223`, `:250`; `voice_startup` is registered once as the app's startup handler, `aset/web.py:91`. Letter B: `no` / `no`.
- **(viii) L32**: I read this report once before its last line: no ticker, price or spoken word of his written. (His ruling phrase for Grok in PREFLIGHT is a desk-row literal, not a spoken word of the product.)

Where two checkers contradict each other: C4 — grok "CLOSED — `c-code.md:405-415`, `:438-446`, `:434`, `:497-518`, `:449-465`" against opus "NOT CLOSED — `c-code.md:387-395` (`write_scratch`) and `c-code.md:441-442` (`turn_audio`)"; Grok's own (c) names the same write-failure gap. C5 — grok "NOT CLOSED — `c-code.md:674-684`" against opus "CLOSED … 'an empty transcript lands nothing' belongs to the turn function (part D)". C2 — grok NOT CLOSED, opus CLOSED with the same backup note. Smoothed: none.

## Ready for a deploy

| checker | check line | ready | reason verbatim |
|---|---|---|---|
| grok | `CHECK VOICE V1 C: BUILD STANDS EXCEPT C2, C5 · ready for a deploy prompt: NO · resident skips backup refusal; empty transcript ungated` | NO | resident skips backup refusal; empty transcript ungated |
| opus | `CHECK VOICE V1 C: DEFECT REMAINS C4 · ready for a deploy prompt: NO · C4 write leak open; X-E10 bundled x264/x265 awaits desk` | NO | C4 write leak open; X-E10 bundled x264/x265 awaits desk |
| sol | METER — retry after Sep 26th, 2026 6:47 AM | — | not seated |
| astra | NOT SEATED | — | Sol's Codex meter; no string on this line |

## FOR THE CLASSIFIER

Round 1 of ≤3 (a HOLD goes to a fix round, L75). Part C; my file:line are the ORIGINAL files'.

1. Claim: "C4 … NOT CLOSED — `write_scratch` … `os.write` then raises … A partial audio file stays in `scratch_dir` with no unlink and no RED line" — who: opus (grok (c) the same) — part C — `scratch.py:113-121`, `:164-172`; `turn.py:183-201` — HOLDS. (Includes `os.write`'s ignored return value, `scratch.py:118`.)
2. Claim: "C2 — NOT CLOSED … `load_voice_config()` with no `backup_sources`, `scratch_dir` or `model_dir` an absolute path under a `configs/cobalt/backup.yaml` source … outside the repo and outside both vault roots" still loads — who: grok (opus as a note) — part C — `config.py:98-100`, `:104-144` — HOLDS (disclosed by the build: report line 231).
3. Claim: "`COBALT_VOICE_*_DIR=""` is treated as unset, so production silently falls back to the dev path" — who: opus — part C — `config.py:129-132` — HOLDS.
4. Claim: "a file that was 'already gone' counts as a normal deletion, and its AMBER line is dropped" — who: opus — part C — `scratch.py:135-136`, `:153-160` — HOLDS.
5. Claim: "the test that checks every setting has a `# source:` line is vacuous" — who: opus — part C — `test_voice_config.py:64-69` with `configs/cobalt/voice.yaml` (0 blank lines) — HOLDS.
6. Claim: "`c-tests.md:626` checks `t.revision` against the config, which the code copies in … so it proves nothing about which model files loaded" — who: opus — part C — `test_voice_transcribe.py:83`, `transcribe.py:154-156` — HOLDS.
7. Claim: "`c-tests.md:538-542` counts only `os.unlink(` inside `scratch.py`; `Path.unlink`, `os.remove` and other voice modules are not covered" — who: opus — part C — `test_voice_scratch.py:234-238` — HOLDS.
8. Claim: "`c-tests.md:130` accepts `\"docs\"` or `\"repo\"`, so a docs path that only hits the repo refusal still passes" — who: grok — part C — `test_voice_config.py:125-129` — HOLDS.
9. Claim: "`plan_route` in `voice.yaml` is never checked against `modelaccess.yaml` or against the registry's `route`. The comment … claims 'checked by the agent registry', but no code does that" — who: opus — part C — `config.py:56-58`; no reader in `src/cobalt` or `configs/cobalt` — HOLDS.

## ESCALATE

1. **Opus: `CHECK VOICE V1 C: DEFECT REMAINS C4`** (ready NO). Grok: `BUILD STANDS EXCEPT C2, C5` (ready NO).
2. **The nine items under `## FOR THE CLASSIFIER`** (1 C4 write leak · 2 C2 resident backup refusal · 3 empty-env fallback · 4 already-gone line · 5 vacuous source test · 6 revision tautology · 7 unlink-count test · 8 docs-or-repo · 9 dead `plan_route`) — `defects that HOLD: 9`.
3. **Contradictions quoted**: C4 (grok CLOSED vs opus NOT CLOSED; the hub's file-check HOLDS the write-failure path, `## Checked against the branch` 1); C5 (grok NOT CLOSED vs opus CLOSED; the hub's file-check: DOES NOT HOLD, the path is `turn.py:383-384` in part D).
4. **`PART A — carried to 16`**: X-X13's section is in the report's C9 / C10 / WITH-DB (lines 322, 334, 383), not in the experiments copy (grok "NOT RUN — no `### X-X13`", opus "placed in C10, with-DB").
5. **`PART D — carried to 19`**: X-E7 is in the report's C13 / WITH-DB (lines 363, 383); the startup sweep / lock ordering (`web.py:157-164`, `aset/web.py:91`), `audio_deleted_at` on the row (`turn.py:202-206`), a held lock's non-zero exit, and Starlette's multipart spool (opus, NOT CHECKABLE FROM READS) belong to part D's files.
6. **Facts that hold and fit no class (desk items, no class added)**: (a) X-E10 — the quoted probe and `.dylibs` list show `libx264` / `libx265` bundled in the `av` wheel beside "OUTCOME: NO CHANGE by the letter", and the build's own ASK DESK ("the letter of the gate is not met; the desk decides before ship"); the FINAL's column reads "an unexpected native / GPL package → tribunal round 2" — the desk rules; (b) the experiment scripts (E2, E2b, X1, X20, E4, E6, X5, E10) are described, not quoted whole, against `rows.part1` X-A ("each script's text is quoted whole in its `### X-<id>` section"); (c) `audio/wav` vs `max_upload_bytes` (≈ 20.8 s of 48 kHz mono, opus's assumption) vs `max_clip_s` 30; (d) `REPO_ROOT` from a worktree accepts a main-checkout path (dev only); (e) the build's C2 `ASK DESK` (make `com.cobalt.aset` a declared `backup.yaml` reader, or keep the suite check) is still open on the desk; (f) the experiments file's header says "packet B" (copied unchanged, as the re-cut ruled).
7. **The `uv.lock` EXCLUSION**: its whole diff (26,366 B, 1 block, commit `cc2e95b6`) was not staged; the 1,708 B excerpt was. No checker made a claim about the unstaged lines.
8. **Packet notes**: no mismatch against the re-cut's measurements; one typing slip of mine in the copy of the experiments file (a path missing `cobalt/`) was found by the line-set check before launch and fixed (24,761 B re-measured); one earlier `| grep -c` pipe against the "no pipe" rule (device-session listing, count 0) was redone as a bare `ls` glob. No checker marked `WROTE:`. No `ASK DESK` of mine. No L74 block arrived inside a tool result.
9. **`sol: METER — retry after Sep 26th, 2026 6:47 AM`** (probe exit 1, "You've hit your usage limit … try again at Sep 26th, 2026 6:47 AM."); **`astra: NOT SEATED`** (Sol's Codex meter; no string on this line) — the desk seats both from Sat 2026-09-26 06:47 ET (L62 R19).
10. **Standing line**: This check covers voice V1 only, PART C of four (audio, model files, config, experiments) of `04b05cd4..28b6b0c6` of `voice/v1-0923`; parts A, B, D (`16`, `17`, `19`) cover the rest, every file in exactly one part. It is round 1 of ≤3 (L67 / L39). With the seated checkers (Opus 5.5 + Grok, L67 as amended 2026-09-24) checked on EACH of the four parts and `defects that HOLD: 0` in all four, the branch is READY for a stacked deploy prompt; a HOLD goes to a classifier and a fix round — and the branch waits out of that evening's set if the fix cannot land and be checked first (L43's drop rule).
11. **Standing line**: The DEVICE SESSION (E1, E3 on his phone's file, E5, E8 / X3 behind `tailscale serve`) is OWED (no `voice-v1-device-*.md` record exists): a design-changing device result is a fix round before the ship, whatever this check reads.
12. **Standing line**: V1's production deploy needs, beyond the merge: the migration (`--allow-prod`), the model files in the production `model_dir`, the `COBALT_VOICE_*` exports live in `ops/start_aset.sh`, and `com.cobalt.aset` restarted inside the pause (L43 / L66) — the deploy prompt carries each (build ESCALATE (vi)).
13. **Standing line**: L68 GATE EARLY (amended 2026-09-24) asks every BUILD's stop line to quote offline, with-DB AND live-note results; V1's built line (09-23, before the clause) quotes offline and with-DB only — the desk rules whether the live-note result is owed before the merge.
14. **Part B's verdict** (`DONE · part: B … defects that HOLD: 2`) was read as a stop only (L72); it holds nothing here.

VOICE V1 CHECK DONE · part: C (audio, model files, config, experiments) · grok: CHECK VOICE V1 C: BUILD STANDS EXCEPT C2, C5 · ready for a deploy prompt: NO · resident skips backup refusal; empty transcript ungated · opus: CHECK VOICE V1 C: DEFECT REMAINS C4 · ready for a deploy prompt: NO · C4 write leak open; X-E10 bundled x264/x265 awaits desk · sol: METER — retry after Sep 26th, 2026 6:47 AM · astra: NOT SEATED (Sol's Codex meter, Sep 26th, 2026 6:47 AM; no string on this line) · defects that HOLD: 9 · ESCALATE: 14
