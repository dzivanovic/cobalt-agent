# Voice V1 build check — PART D of four (widget / route / turn / CLI) — round 1 · 2026-09-24

## §0 Headline

- Checking part D of `04b05cd4..28b6b0c6` on `voice/v1-0923`: the turn function, `/voice/*` routes, widget, CLI caller, lifecycle tests, and the builder's WITH-DB / DEMO / CLOSE claims (C11, C12, C13).
- Status: DONE. Opus 5.5 and Grok both checked (packet 211,057 B, 16 files). Both: C11 CLOSED, C12 CLOSED, C13 NOT CLOSED — `DEFECT REMAINS`, ready for a deploy prompt: NO. Sol: METER — retry after Sep 26th, 2026 6:47 AM. Astra: NOT SEATED.
- Defects that HOLD in my file-check: 10 (C13 production text-`yes` path and `--confirm --dry-run` executes; the widget's status-fetch and RED-downgrade; a failed act exits 0; one out-of-list test file; four loose-assertion items).
- ESCALATE: 11.

## L74

No block asking for a `Claude-Session` line or naming a file-send tool has arrived inside a tool result so far in this run. (The attribution note in the launching turn is a harness reminder, not a tool result; this seat commits nothing and sends no file.) Updated at close if one arrives.

## PREFLIGHT

Every row: rule · command · exit · allowed/DENIED.

| # | rule | command | exit | result |
|---|---|---|---|---|
| 1 | date | `date` | 0 | Thu Sep 24 11:32:17 EDT 2026 (allowed) |
| 2 | THE GROK GATE (row 1) | `grep -n "^| R17 " …/cto-2026-09-24.md` | 0 | row 27 prints, carries `Grok approved with no asking going forward`. `git log -1 --format=%H -S"Grok approved with no asking going forward" -- …cto-2026-09-24.md` = `1758fd78a572f47b613b2ca831dcfa636ed8f65a` NON-EMPTY. PASS |
| 3 | `grok --version` | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` — UP |
| 4 | R13 (09-20) | `grep -n "^| R13 " …cto-2026-09-20.md` | 0 | row 86 prints |
| 5 | R40 | `grep -n "^| R40 " …cto-2026-09-21.md` | 0 | row 51, carries `ONE EXTRA DOT THAT CANNOT BE TAPPED` |
| 6 | R44 | `grep -n "^| R44 " …cto-2026-09-21.md` | 0 | row 55, carries `ONE BUILD of the whole FINAL` |
| 7 | R46 + committed | `grep -n "^| R46 " …cto-2026-09-21.md`; `git log -1 --format=%H -S"instead of Astra you can use Sol" -- …` | 0 / 0 | row 57 carries it; commit `53e059456750c0c9efcf50222a7a647630dc4b04` |
| 8 | R49 (Sol string) | `grep -n "^| R49 " …`; `grep -c -F "Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only *)" …cto-2026-09-21.md`; `git log -1 --format=%H -S…` | 0 | row 60 carries `"Approved"`; count 1; commit `60147d400b009db5a2518e02b8ab1fe5765db405` |
| 9 | R32 (Opus 5.5 seat string) | `grep -n "^| R32 " …cto-2026-09-22.md`; `git log -1 --format=%H -S"Bash(claude -p --model claude-opus-5-5 *)" -- …cto-2026-09-22.md` | 0 | row 131 carries `claude -p --model claude-opus-5-5`; commit `b8a72b5300370e248cd6c7a8a732258fec03e6a0` |
| 10 | THE TWELVE + THREE | `grep -c -F -e "<rule>" …/08-bars-chunk-e-check.md`, 15 calls (grok · mkdir · git show · git log · s2 show · s2 log · s2 diff · ls · grep · tail · wc · date · AskUserQuestion · EnterWorktree · git push) | 0 each | each = **1** |
| 11 | Astra string absent from the launch line | `grep -c -F "gpt-6-astra" …/19-voice-v1-check-d.md` | 1 (count 0) | **0** — absent. `Bash(agy *)` appears in the prompt only as the "REMOVED" sentence, not in its launch line. (I cannot read my own launch argv; the prompt's launch line is the record.) |
| 12 | R57 design approval + committed | `grep -n "^| R57 " …cto-2026-09-23.md`; `git log -1 --format=%H -S"approved design" -- …` | 0 | row 60 carries `approved design`; commit `ffee37ad5e41ab5eb451406a9e11a9e03b26afdb` |
| 13 | Build launch + desk record of its stop | `grep -n "43-voice-v1-build.md" …cto-2026-09-23.md`; `grep -n "VOICE V1 BUILT" …`; `git log -1 --format=%H -S"VOICE V1 BUILT" -- …cto-2026-09-2*.md` | 0 | launch row R63 (line 66); later row R71 (line 74) carries `VOICE V1 BUILT 566d1848 | on 04b05cd4 | …`; commit `9cc68741bc8cd656d4d2e3f9d7189ad8fabba2d8` |
| 14 | Re-cut committed | `git log -1 --format=%H -S"VOICE V1 CHECK RECUT" -- …/voice-v1-check-recut-2026-09-24.md` | 0 | `80b208c5d1304bd99ec44fe1b6dfd84fc3c91b3c` NON-EMPTY |
| 15 | THIS launch row R41 | `grep -n -F "19-voice-v1-check-d.md" …cto-2026-09-24.md`; `git log -1 --format=%H -S"19-voice-v1-check-d.md" -- …cto-2026-09-2*.md` | 0 | grep prints R23 (line 33) and R41 (line 51). The commit query = `80b208c5d1304bd99ec44fe1b6dfd84fc3c91b3c` NON-EMPTY, so the gate as written PASSES. **But the R41 row states it was "written UNCOMMITTED under R39's hold; `19`'s gate on a committed row naming it is met by R23"**, and `git log -1 --format=%H -S"\| R41 \|" -- …cto-2026-09-24.md` printed NOTHING (the R41 row itself is not committed). Recorded; continued on the gate as the prompt words it. → `## ESCALATE`. |
| 16 | Part C has stopped (house lane) | `tail -n 3 …/voice-v1-check-c-2026-09-24.md` | 0 | LAST NON-BLANK line: `VOICE V1 CHECK DONE · part: C (audio, model files, config, experiments) · grok: CHECK VOICE V1 C: BUILD STANDS EXCEPT C2, C5 · … · opus: CHECK VOICE V1 C: DEFECT REMAINS C4 · … · sol: METER — retry after Sep 26th, 2026 6:47 AM · astra: NOT SEATED (…) · defects that HOLD: 9 · ESCALATE: 14`. Starts `VOICE V1 CHECK DONE · part: C` — PASS. Its verdict is not a gate (L72). |
| 17 | worktree | `ls /Users/cobalt/cobalt-wt/voice-v1` | 0 | present |
| 18 | THE BUILT LINE | `tail -n 3` on the build report | 0 | LAST NON-BLANK line: `VOICE V1 BUILT 566d1848 | on 04b05cd4 | migration 0017 | offline 2422/0 | with-DB 2774/0 | experiments run: 12 of 12 | design-changing results: 3 | stt: faster-whisper/tiny.en | plan route: local.plan (mainframe) | device session: OWED (E1 E3 E5 E8 X3) | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar (6 UNCLASSIFIED) | tests added: 471 | ESCALATE: 14`. Starts `VOICE V1 BUILT `, carries `| on ` and `| migration `. `<base>` = `04b05cd4` = the measured base. PASS |
| 19 | `<tip>` = `28b6b0c6` | `git log --oneline -1 28b6b0c6` | 0 | `28b6b0c6 feat(voice-v1): build report` (desk amendment `cto-2026-09-23.md` R108). PASS |
| 20 | THE RANGE | `git log --oneline 04b05cd4..28b6b0c6` | 0 | 15 commits (matches the re-cut) |
| 21 | branch tip / moved above | `git log --oneline -1 voice/v1-0923`; `git log --oneline 28b6b0c6..voice/v1-0923 -- tests src configs ops pyproject.toml uv.lock "docs/40 - DevDocs/cobalt" "docs/40 - DevDocs/tests"` | 0 | tip `28b6b0c6`; second command EMPTY. PASS |
| 22 | THE BOUNDARY + THE SPLIT IS TOTAL | `git log --stat --oneline 04b05cd4..28b6b0c6` read against the re-cut `## Split` | 0 | every path of the `--stat` list is in exactly one row of the table (A 25 · B 26 · C 19 · D 13 + the build report = 84). Paths outside `43`'s WHAT YOU BUILD list are read against the build report in `## Laws and boundary` (the CHANGED test files `test_p4_migrations.py`, `test_radar_migration.py`, `test_radar_score_migration.py`, `test_tenancy.py`, `test_archiver_migrations.py`, `test_radar_panel_cards.py` and the two DevDocs beside them). |
| 23 | NEW vs CHANGED | `git log --diff-filter=A --name-only --format= 04b05cd4..28b6b0c6` | 0 | 67 paths. The 10 part-D whole files (`voice/turn.py`, `voice/web.py`, `voice/cli.py`, the four tests, the three DevDocs) are printed. `src/cobalt/cli.py`, `tests/cobalt/test_radar_panel_cards.py`, `docs/40 - DevDocs/cobalt/cli.md` are NOT printed (staged as diffs). PASS |
| 24 | `.env` | `ls /Users/cobalt/cobalt-wt/voice-v1/.env` | 1 | "No such file or directory" — PASS (never read) |
| 25 | recovery | `ls scratch/tribunal-bars-0920/voice-v1-check-d` | 1 | "No such file or directory" = fresh run |
| 26 | sources of copied context | `ls scratch/tribunal-bars-0920/voice-v1-check/A`, `…/B` | 0 | A holds `final-v1.part1/2`, `seam-s1`, `rows.part1/2`, `rulings`, `l28` (+ others); B holds `build-report-B.part2.md`. All present. |
| 27 | THE STAGGER | `grep -n -F "no other house hub is running" …cto-2026-09-24.md` | 0 | R41's line prints AND names `19-voice-v1-check-d.md` ("STAGGER for `19-voice-v1-check-d.md`: `no other house hub is running`"). PASS |
| 28 | THE CODEX LAUNCH SHAPE | `grep -c -F "Experiment field: **reads started**" …/setups-tribunal-r2-2026-09-21.md` | 0 | **1** → a Sol launch would append ` < /dev/null` (recorded; Sol not launched) |
| 29 | PROBE — SOL | `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` (background) | 1 | `ERROR: You've hit your usage limit. … try again at Sep 26th, 2026 6:47 AM.` → **`sol: METER — retry after Sep 26th, 2026 6:47 AM`**. SKIPPED, not relaunched. **`astra: NOT SEATED — Sol's Codex meter (Sep 26th, 2026 6:47 AM); no string on this line`** |
| 30 | PROBE — OPUS 5.5 | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (background) | 0 | `OK` — **UP** |
| 31 | FAIL CLOSED ON THE COUNT | — | — | Opus 5.5 UP + Grok UP = the two seated. Proceed. |

### Measurement gate (before the first Write) — PASS

Whole-file originals at `/Users/cobalt/cobalt-wt/voice-v1/` (`wc -c` = table): `voice/turn.py` 19,606 · `voice/web.py` 14,802 · `voice/cli.py` 4,186 · `test_voice_turn.py` 16,615 · `test_voice_web.py` 10,076 · `test_voice_cli.py` 3,817 · `test_voice_lifecycle.py` 7,765 · DevDocs `turn.md` 2,104 · `web.md` 2,150 · `cli.md` 948. Trailing-whitespace lines (`grep -c -E "[[:space:]]$"`): **0** in each of the ten. Saved git outputs (`run_in_background`, harness-saved): `src/cobalt/cli.py` diff 1,236 (1 `diff --git`) · `test_radar_panel_cards.py` diff 1,561 (1) · `git show 28b6b0c6 -- test_voice_lifecycle.py` 1,574 (1) · DevDoc `cli.md` diff 1,189 (1) · `aset/web.py` diff 4,529 (2) — all equal the table to the byte. Context sources (`wc -c`): `final-v1.part1` 15,586 · `final-v1.part2` 21,457 · `seam-s1` 14,433 · `rows.part1` 13,946 · `rows.part2` 21,984 · `rulings` 4,080 · `l28` 4,701 · `build-report-B.part2` 8,754 — all equal. Build report headings: `## C11` line 344, `## C12` 353, `## C13` 361, `## WITH-DB` 374, so the lines 344–373 piece is the table's C11–C13 (+ SUITE, COMMIT).

## Packet

Folder: `scratch/tribunal-bars-0920/voice-v1-check-d/` (created by the Write tool; no `mkdir`). Every checked piece is headed by one `### <path or command> @ 28b6b0c6 · whole | lines a–b | git output · <bytes> B` line. Staged by Read → Write. `wc -c` after each Write; the whole-file originals and the saved git outputs were `wc -c`'d BEFORE the first Write (PREFLIGHT, Measurement gate). The `grep -c -v -x -F -f <original> <staged>` line-diff I tried first is NOT usable on this machine's `grep` (it reports 65 differing lines for `turn.py` against itself), so the byte check plus `wc -l` is the proof of fidelity; I did not verify contents any other way.

| staged file | pieces | measured | `wc -c` of the staged copy | expected (pieces + headers) |
|---|---|---|---|---|
| `d-code-1.md` | `voice/turn.py` whole 19,606 · `voice/web.py` whole 14,802 | 34,408 | 34,527 (731 lines) | 34,408 + 119 = 34,527 ✓ |
| `d-code-2.md` | `voice/cli.py` whole 4,186 · `git log -p` of `src/cobalt/cli.py` 1,236 · `git log -p` of `test_radar_panel_cards.py` 1,561 · `git show 28b6b0c6` of `test_voice_lifecycle.py` 1,574 | 8,557 | 8,985 | 8,557 + 428 = 8,985 ✓ (10 trailing-whitespace lines kept — the git outputs carry 3 + 4 + 3) |
| `d-tests-1.md` | `test_voice_turn.py` 16,615 · `test_voice_web.py` 10,076 | 26,691 | 26,824 (642 lines) | 26,691 + 133 = 26,824 ✓ |
| `d-tests-2.md` | `test_voice_cli.py` 3,817 · `test_voice_lifecycle.py` 7,765 | 11,582 | 11,718 (304 lines) | 11,582 + 136 = 11,718 ✓ |
| `d-devdocs.md` | DevDocs `turn.md` 2,104 · `web.md` 2,150 · `cli.md` 948 · `git log -p` of the DevDoc `cli.md` 1,189 | 6,391 | 6,737 | 6,391 + 346 = 6,737 ✓ (3 trailing-whitespace lines kept: 2 tab-terminated `---`/`+++` lines and the commit-message blank) |
| `build-report-d.md` | build report lines 344–373 (`## C11`, `## C12`, `## C13`, `### SUITE`, `### COMMIT`) | 6,740 | 6,839 | 6,740 + 99 = 6,839 ✓ |
| `build-report-close.md` | COPY of `scratch/tribunal-bars-0920/voice-v1-check/B/build-report-B.part2.md` (`## WITH-DB`, `## DEMO`, `## CLOSE`) | 8,754 | 8,754 | = source ✓ (58 lines, its own "packet B" header kept) |
| `context-aset-web-diff.md` | CONTEXT: `git log -p` of `src/cobalt/aset/web.py` (2 commit blocks) | 4,529 | 4,648 | 4,529 + 119 = 4,648 ✓ (13 trailing-whitespace lines kept) |
| `final-v1.part1.md` | COPY from `…/voice-v1-check/A/` | 15,586 | 15,586 | ✓ |
| `final-v1.part2.md` | COPY | 21,457 | 21,457 | ✓ |
| `seam-s1.md` | COPY | 14,433 | 14,433 | ✓ |
| `rows.part1.md` | COPY (1 trailing-whitespace line kept) | 13,946 | 13,946 | ✓ |
| `rows.part2.md` | COPY | 21,984 | 21,984 | ✓ |
| `rulings.md` | COPY | 4,080 | 4,080 | ✓ |
| `l28.md` | COPY | 4,701 | 4,701 | ✓ |
| `QUESTIONS-VOICE-V1-D.md` | the question text VERBATIM + the "Files in this folder:" paragraph | 3,635 (drafter; my copy of the text alone measured 3,633 — the drafter's number most likely counts the two delimiting quote marks) | 5,838 | — |

Context copies total **96,187 B** = the prompt's 96,187 ✓. Every staged file is ≤ 38,000 B; the largest is `d-code-1.md` at 34,527.

**HONEST SIZE:** whole packet = **211,057 B** (16 files) ≈ **52,764 tokens per checker** (÷ 4). Ceiling 230,000 B — under it, **18,943 B to spare**. The prompt's projection was ≈ 212,534 B.

Trailing-whitespace disclosure: the ten original whole files had **0** trailing-whitespace lines; the five saved git outputs carry 3 / 4 / 3 / 3 / 13 (commit-message blank lines, diff context blank lines, two tab-terminated `---`/`+++` header lines) and the Write tool kept them — counts equal in the staged copies. `rows.part1.md` carries 1 (source: 1).

## CONTINUE

- 11:49:04 ET `date`; THE GROK GATE second row: R17 row printed (line 27), commit `1758fd78a572f47b613b2ca831dcfa636ed8f65a` — PASS. Written-nothing proof, BEFORE: `ls -la /Users/cobalt/cobalt-wt/voice-v1` (27 entries, newest mtime Sep 23 15:08 `.`, `ops` Sep 23 14:08, `uv.lock` Sep 23 13:51, no `.env`) and `ls -la scratch/tribunal-bars-0920/voice-v1-check-d` (16 files, last write 11:47).
- LAUNCHED 11:49 ET, both `run_in_background`, independent, one attempt each:
  - GROK: `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "You are GROK. The folder is scratch/tribunal-bars-0920/voice-v1-check-d/. Start with QUESTIONS-VOICE-V1-D.md and follow it exactly. final-v1.part1.md then final-v1.part2.md are one file read in order (the text calls it final-v1.md); rows.part1.md then rows.part2.md are one file read in order (the text calls it rows.md). Do not open any *-check-*.md file. Write your complete check to /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v1-check-d/grok-check-d.md and reply with only that path."` (task `baal0ktjz`).
  - OPUS 5.5: `claude -p --model claude-opus-5-5 "You are OPUS. … Do not open any *-check-*.md file. Read files with the Read, Grep and Glob tools only. Write no file. Print your complete check as your answer." --permission-mode plan --add-dir /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v1-check-d --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"` (task `b4be3ynnu`).
  - SOL: not launched (METER, PREFLIGHT row 29). ASTRA: not launched (no string on this line).
- 45-minute clock: Grok and Opus started 11:49 ET → stop any still running at 12:34 ET.
- Facts checked while the checkers ran (they read no code): (ii) both PROTECTED-PATHS calls printed NOTHING; (vi) `grep -rn "str(v)" src/cobalt/voice` printed NOTHING; skip/xfail: the two `+`-line diffs (`test_radar_panel_cards.py`, the lifecycle later edit) carry none; the part-D test files: `test_voice_turn.py`, `test_voice_web.py`, `test_voice_cli.py` none; `test_voice_lifecycle.py` line 40 `requires_db = pytest.mark.skipif(` and line 125 `@pytest.mark.skipif(shutil.which("say") is None, reason="macOS `say` absent")` — both quoted, not judged.

- Returns: OPUS 5.5 back 11:52 ET (~3 min) — I wrote `opus-check-d.md` from its stdout (its closing `[exited with code 0]` harness line not included; 6,179 B); Grok back by 12:03 ET (~14 min), wrote `grok-check-d.md` itself (8,148 B); its stdout was only the path. Neither near the 45-minute clock. Written-nothing proof AFTER: `ls -la /Users/cobalt/cobalt-wt/voice-v1` is line-for-line identical to BEFORE (same 27 entries, same mtimes); `ls -la scratch/tribunal-bars-0920/voice-v1-check-d` gained exactly `opus-check-d.md` (mine, 11:53) and `grok-check-d.md` (Grok's own, 12:03); all other 16 files unchanged. `grep -c -i "denied\|not allowed\|permission"` = 0 on both check files. No entry marked `WROTE:`.

next: none — the run is complete; the report is closed on the stop line below.

## Per chunk

| chunk | builds (rows.md) | grok | opus | sol | CLOSED: n of 2 |
|---|---|---|---|---|---|
| C11 | turn function, `/voice/*` routes, peer gate, startup sweep | CLOSED — `web.py:105-111`, `turn.py:186-193`, `web.py:70-74` | CLOSED — `d-code-1.md:524-530`, `:489-494`, `:186-191` | METER — not launched | **2 of 2** |
| C12 | the widget partial on `/` and `/radar` | CLOSED — `web.py:238,244,245`; no card id | CLOSED — `d-code-1.md:655-665, 674-717`; no reply audio | METER — not launched | **2 of 2** |
| C13 | `cobalt voice turn` CLI; `--confirm` refused in production; `--dry-run` | NOT CLOSED — `cli.py:43` → `turn.py:369-370`: `--confirm <id> --dry-run` ignores dry-run and executes | NOT CLOSED — `d-code-2.md:60` + `d-code-1.md:388-400` text `yes` confirms in production; `d-code-2.md:40-45` `--confirm --dry-run` executes | METER — not launched | **0 of 2** |

## Laws and boundary

Verbatim, per checker.

**Grok — (a)** three loose-assertion groups: `test_voice_lifecycle.py:165` allows the pre-reap state to be `failed`; `:173` asserts only `state == failed`; `:174` checks a `reaped_` class only inside an `if`; `:168` is the test's own reap with real now + 10 min, "not the restarted server's startup reap. A row the restart left in `transcribing` still passes." · `:55-62` `CrashBeforeDone.reap` "ignores `now` and `limits` … It is not `VoiceTurnStore.reap`." · `test_voice_cli.py:57-62` fakes `run_turn`, checks only `dry_run is True` and the letters of `plan` / `change` ("The no-write proof is the turn test above") · `test_voice_cli.py:68` "does not assert the refusal text, only a non-zero exit and that `run_turn` was not called" · `test_voice_turn.py:394` and `test_voice_cli.py:48` are substring checks. **(b)** `tests/cobalt/test_radar_panel_cards.py:596-599` and `:669-670` "Not in the list. The builder named it as an escalate in the C11 claim"; no `ops/*.plist`, `heartbeat`, `vaultwrite`, top-level `configs/*.yaml`; `src/cobalt/cli.py` is the one allowed registration pair. **(c)** `web.py:299` `fetch('/voice/status')` does not check `r.ok` ("the banner is cleared … a LAN peer who can load the page (the page is not behind `peer_gate`) sees a healthy widget"); "`--dry-run` on `--confirm` is accepted and ignored, and the act runs, with no `dry run (nothing written)` line"; `web.py:244` no-local-voice `speak` calls `banner` with only the amber line and "red `degraded` lines `show` just painted (`web.py:251`) are dropped"; no scratch-file-survives path; no `SttDown`-as-empty path. **(d)** NONE.

**Opus — (a)** "Three soft spots; no real weakening found": the E7 row check accepts any of four states and asserts `failed_at` only if the failure class starts `reaped_`; the row is reaped by the test's own `store.reap` with the clock 10 minutes ahead, not by the restarted server; the "one turn function" tests are only `inspect.getsource` string checks (`d-tests-2.md:270, 275-280`; `d-tests-1.md:390-395`; `d-tests-2.md:48-49`). **(b)** `tests/cobalt/test_radar_panel_cards.py` changed — `POST_ALLOWLIST` gains three `/voice/*` routes; the `/radar` byte-equality check now expects the widget; "The builder named it as an ESCALATE"; no plist / heartbeat / vaultwrite / top-level configs change in part D's files. **(c)-1** "A 403 reads as all clear. The widget's `/voice/status` fetch never checks `r.ok`" (`d-code-1.md:718`). **(c)-2** "A RED line gets downgraded. `show()` draws the turn's RED `degraded` lines, then `speak()` redraws the banner with only the AMBER no-local-voice line" (`d-code-1.md:663, 670-671`). **(c)-3** "A failed act exits 0" (`d-code-1.md:238-240, 257-259`; `d-code-2.md:82-83`). **(d)** "NONE. Test bytes are constructed literals, and E7 synthesizes speech with `say` into `tmp_path` at test time."

**Sol** — METER, not launched. **Astra** — not seated.

## Checked against the branch

Originals under `/Users/cobalt/cobalt-wt/voice-v1/` (Read / grep). Line numbers are the ORIGINAL files' (the staged copies' line numbers, which Opus cites, are `d-code-1.md` = original line + 419 for `web.py` and + 1 for `turn.py`; a spot check of `web.py:105` = `d-code-1.md:524` matched).

| # | claim | who | file:line | verdict | note |
|---|---|---|---|---|---|
| 1 | `cobalt voice turn --text "<request>"` then `--text yes` confirms a pending act in production; `--confirm`'s production refusal is the only production check | opus | `voice/cli.py:59` (text turn: `source="cli"`, session default `cli-local`); `turn.py:386-399` (`pending_for_session` → `_answer_pending`, no `source` or environment test); `store.py:168-173` (`WHERE session_id = %s AND state = 'awaiting_confirm'`, no source filter); `grep is_production` in `src/cobalt/voice/` → `cli.py:40` only | **HOLDS** | The code path exists. Whether it breaches FINAL `[F-02]` / L37 is the desk's; I judge nothing. `test_voice_cli.py:64-68` covers only the `--confirm` flag. |
| 2 | `--confirm <id> --dry-run` is accepted and the act executes | opus, grok | `cli.py:39-44` (the confirm branch builds the tap without `dry_run`), `cli.py:90-94` (`--dry-run` is not in the mutually exclusive group), `turn.py:368-369` (a tap returns `_tap` before any dry-run test), `turn.py:242-258` (`_tap` never reads `inp.dry_run`); `cli.py:78` prints "dry run (nothing written)" only when `out.dry_run` is set, and `_tap`'s outcome carries none | **HOLDS** | No test combines the two flags (`test_voice_cli.py:57`, `:71`). Executes in dev under `COBALT_ALLOW_DEV_ENTRY=1` (Opus). |
| 3 | `--confirm` in production is refused, named, non-zero; text `--dry-run` writes no row or pending action | opus, grok | `cli.py:40-42, 32-34` (stderr `FAILED:` line, `sys.exit(2)`); `turn.py:139-157` (`_Rec` no-ops when `dry`), `:371`, `:354-358` | **HOLDS** (the narrow asks close) | Grok also read `env.is_production` as unread: `env.py:73-75` = `resolve_env() == PRODUCTION`, and `resolve_env` reads `COBALT_ENV` (`env.py:60-70`) — so the test's `COBALT_ENV=production` exercises the real function. |
| 4 | `/voice/status` fetch never checks `r.ok`; a 403 clears the banner | opus, grok | `web.py:299`: `fetch('/voice/status').then(r => r.json()).then(j => { lines = j.lines || []; banner(); })` | **HOLDS** | A 403 body `{detail: …}` has no `lines`. The turn POST path does check `r.ok` (`web.py:259`) — Grok's contrast holds. |
| 5 | The page carrying the widget is not behind `peer_gate` | grok | context diff `context-aset-web-diff.md`: hunks add the router include, the startup / shutdown handlers and the widget placement only; no gate on `/` or `/radar` | **HOLDS** (as far as this branch's diff shows) | Whether those routes carry an older gate is not in the staged files. |
| 6 | `speak()` with no local voice repaints the banner with only the amber line, dropping the turn's RED `degraded` lines | opus, grok | `web.py:231-235` (`banner` rebuilds from `lines` + `extra`), `:241-246` (`speak` → `banner([{level:'amber', …}])`), `:247-253` (`show`: `banner(j.degraded)` then `speak(j.reply)`) | **HOLDS** | The reply text itself stays in `#cv-reply` (`web.py:248`). |
| 7 | A failed act exits 0 | opus | `turn.py:231-239` (`res.kind == "failed"` → state `DONE` + a RED degraded line), `:256-258`; `cli.py:81-82` (exit 1 only when `out.state.value == "failed"`) | **HOLDS** | The RED line is printed (`cli.py:74-75`); the exit code is 0. |
| 8 | `tests/cobalt/test_radar_panel_cards.py` was changed and is not in `rows.md`'s WHAT YOU BUILD list | opus, grok | staged diff `d-code-2.md` (git output, 1 block: 6 added lines); `rows.part1.md` WHAT YOU BUILD lists `tests/cobalt/test_modelaccess_*.py`, `test_voice_*.py`, `tests/fixtures/voice/*` | **HOLDS** | The build report names it: `build-report-d.md` C11 `### C` "**Outside the list, named (ESCALATE):** `tests/cobalt/test_radar_panel_cards.py` — `POST_ALLOWLIST` gains … and the `/radar` byte-equality expectation gains the widget partial before `</body>`." The diff removes no line and no assert. |
| 9 | E7's pre-reap check accepts four states; `failed_at` asserted only if the class starts `reaped_`; the reap is the test's own call with real time + 10 min, not the restarted server's | opus, grok | `test_voice_lifecycle.py:165` (`in ("received", "transcribing", "planned", "failed")`), `:170-171` (`store.reap(now=datetime.now(timezone.utc) + timedelta(minutes=10), …)`), `:173` (`state == "failed"`), `:174-175` (`if … startswith("reaped_")`) | **HOLDS** | The assertion that stays true for a row left `transcribing`: `row["state"] == "failed"` after the test's own reap. (Grok cites `:168`; that line is the comment, the call is `:170`.) |
| 10 | `CrashBeforeDone.reap` ignores `now` and `limits` and fails every `executing` row; it is not `VoiceTurnStore.reap` | grok | `test_voice_lifecycle.py:55-61` | **HOLDS** | Whether the real reaper's `executing` handling is proven elsewhere is part A's file (`test_voice_store.py`) — not in this packet. |
| 11 | `test_confirm_is_refused_in_production` does not assert the refusal text | grok | `test_voice_cli.py:64-68`: `assert e.value.code != 0 and recorded == []` | **HOLDS** | The named sentence is `cli.py:41-42`; the stderr text is not asserted. |
| 12 | The "one turn function" tests are substring checks | opus, grok | `test_voice_turn.py:389-394` (`"run_turn" in inspect.getsource(web)`); `test_voice_cli.py:47-48` (`"run_turn(" in inspect.getsource(vcli)`) | **HOLDS** | Both are `inspect.getsource` string tests; the call sites are `web.py:91`, `cli.py:65`. |
| 13 | `test_voice_cli.py:57-62` fakes `run_turn` and checks only `dry_run is True` and two substrings; the no-write proof is the turn test | grok | `test_voice_cli.py:57-62`; `test_voice_turn.py:380-386` (`store.rows == {}`, `executed == []`) | **HOLDS as a description; not a gap** | Grok itself names the turn test as the proof; the two-flag combination in row 2 is not covered by either. Not counted below. |
| 14 | Proxy-header rewrite of `request.client.host` under uvicorn; model load on the event loop; CLI `--audio` zero-byte / oversize; a dry-run's Plan call writing a row in the model layer | opus, grok | — | **NOT CHECKABLE FROM READS** | Needs `ops/start_aset.sh` + a live LAN request with the spoofed header (part C's file) / an X-E6 run / a run of `--audio` on an empty file / a with-DB `--dry-run` with the tables diffed. |
| 15 | Builder WITH-DB, DEMO and CLOSE results (migrate, two pytest runs, deadlocks, live turns, `git ls-files` audio count, restarts, scratch listing) | opus, grok | `build-report-close.md` | **NOT CHECKABLE FROM READS** | Needs the with-DB suite, the live model and a dev server; the with-DB claim's own text calls three deadlocks UNPROVEN. |
| 16 | Part C's Grok "empty transcript ungated", carried to part D by the desk's R41 ("part D's `turn.py:383-384`") | part C, per desk | `turn.py:383-384`: `if not transcript or not transcript.strip(): raise _Fail("empty_transcript", "I heard nothing.")`; `test_voice_turn.py:240-244` | **DOES NOT HOLD** | The gate exists before any plan or pending step. No claim text was handed to me in a launch row beyond that pointer. |

Facts the prompt has me state plainly:

- **(ii) PROTECTED PATHS** — `git log --oneline 04b05cd4..28b6b0c6 -- src/cobalt/radar src/cobalt/cards src/cobalt/vaultwrite src/cobalt/heartbeat src/cobalt_agent configs/config.yaml` → EMPTY. `… -- ops/com.cobalt.aset.plist ops/com.cobalt.heartbeat.plist ops/com.cobalt.radar.plist` → EMPTY.
- **(iii)** In the staged diffs of `test_radar_panel_cards.py` and the `test_voice_lifecycle.py` later edit: no `-` line removes an `assert`. The radar diff has no `-` line at all; the lifecycle diff's two `-` lines are `from cobalt.session import clock as clock_mod` and `store.reap(now=clock_mod.now_utc() + timedelta(minutes=10),`, replaced in the same hunk by the real-time import and call — no assert removed. `skip` / `xfail` on the `+` lines of both diffs: none. `grep -n "skip\|xfail"` on the four part-D test files: `test_voice_turn.py` none · `test_voice_web.py` none · `test_voice_cli.py` none · `test_voice_lifecycle.py` line 40 `requires_db = pytest.mark.skipif(` and line 125 `@pytest.mark.skipif(shutil.which("say") is None, reason="macOS `say` absent")` — quoted, not judged.
- **(vi) THE UPLOAD IDIOM** — `grep -rn "str(v)" /Users/cobalt/cobalt-wt/voice-v1/src/cobalt/voice` → no output.
- **(viii) L32** — I read this report once before the last line: **no ticker, price or spoken word of his written.**

## Ready for a deploy

| checker | check line | ready | reason (verbatim) |
|---|---|---|---|
| grok | `CHECK VOICE V1 D: DEFECT REMAINS C13, (c) · ready for a deploy prompt: NO · dev confirm with dry-run still executes the act` | NO | dev confirm with dry-run still executes the act |
| opus | `CHECK VOICE V1 D: DEFECT REMAINS C13, (c)-1, (c)-2, (c)-3 · ready for a deploy prompt: NO · CLI --text yes confirms production act; dry-run executes with --confirm` | NO | CLI --text yes confirms production act; dry-run executes with --confirm |
| sol | METER — retry after Sep 26th, 2026 6:47 AM | — | not launched |

The two seated checkers agree on C11 and C12 (CLOSED) and on C13 (NOT CLOSED, the `--confirm --dry-run` path); Opus alone raises the production text-`yes` path (row 1) and the exit code (row 7). They do not contradict each other.

## FOR THE CLASSIFIER

Round 1 of ≤3. Ten items; each part D, `HOLDS`.

1. "under `COBALT_ENV=production`, running `cobalt voice turn --text "<stop request>"` leaves a pending act in session `cli-local`. Running `cobalt voice turn --text yes` next then confirms it through `confirm_pending`" — opus — `voice/cli.py:59`, `turn.py:386-399`, `store.py:168-173` — HOLDS.
2. "`--confirm <id> --dry-run` is accepted by argparse … The confirm branch ignores `args.dry_run`, so the act executes" — opus, grok — `voice/cli.py:39-44, 90-94`, `turn.py:368-369, 242-258` — HOLDS.
3. "A 403 reads as all clear. The widget's `/voice/status` fetch never checks `r.ok`" — opus, grok — `voice/web.py:299` — HOLDS.
4. "A RED line gets downgraded. `show()` draws the turn's RED `degraded` lines, then `speak()` redraws the banner with only the AMBER no-local-voice line" — opus, grok — `voice/web.py:231-253` — HOLDS.
5. "A failed act exits 0" — opus — `turn.py:231-239, 256-258`, `voice/cli.py:81-82` — HOLDS.
6. "`tests/cobalt/test_radar_panel_cards.py` was changed" (outside `rows.md`'s WHAT YOU BUILD list; the builder's own ESCALATE (x) names it) — opus, grok — staged diff, `rows.part1.md` — HOLDS.
7. "The row is reaped by the test's own `store.reap` call with the clock moved 10 minutes ahead, not by the restarted server" (E7 check accepts four states; `failed_at` only inside an `if`) — opus, grok — `tests/cobalt/test_voice_lifecycle.py:165, 170-175` — HOLDS.
8. "`CrashBeforeDone.reap` ignores `now` and `limits` … It is not `VoiceTurnStore.reap`" — grok — `tests/cobalt/test_voice_lifecycle.py:55-61` — HOLDS.
9. "`tests/cobalt/test_voice_cli.py:68` does not assert the refusal text, only a non-zero exit and that `run_turn` was not called" — grok — `tests/cobalt/test_voice_cli.py:64-68` — HOLDS.
10. "`tests/cobalt/test_voice_turn.py:394` and `tests/cobalt/test_voice_cli.py:48` are substring checks" (the "one turn function" pins) — opus, grok — `test_voice_turn.py:389-394`, `test_voice_cli.py:47-48` — HOLDS.

## ESCALATE

1. **Opus `DEFECT REMAINS`** — `CHECK VOICE V1 D: DEFECT REMAINS C13, (c)-1, (c)-2, (c)-3 · ready for a deploy prompt: NO · …`.
2. **Grok `DEFECT REMAINS`** — `CHECK VOICE V1 D: DEFECT REMAINS C13, (c) · ready for a deploy prompt: NO · …`.
3. **Every item under `## FOR THE CLASSIFIER`, 1–10** (restated by number). Item 6 is a hunk the builder itself named in its own ESCALATE (x), with its reason — quoted in `## Checked against the branch` row 8, not judged.
4. **`PART <A|B|C> — carried to …`: none.** The desk handed no carried claim's text in the launch row beyond the pointer to `turn.py:383-384`, which I checked (row 16: DOES NOT HOLD). Claims that depend on other parts' files sit under row 14 as NOT CHECKABLE FROM READS.
5. **The launch row R41 is uncommitted.** Its own text says "written UNCOMMITTED under R39's hold; `19`'s gate on a committed row naming it is met by R23"; `git log -1 --format=%H -S"| R41 |" -- cto-2026-09-24.md` printed nothing. The gate as this prompt words it (`-S"19-voice-v1-check-d.md"` on the desk files) printed commit `80b208c5d1304bd99ec44fe1b6dfd84fc3c91b3c` (R23's mention), so the run went ahead on the gate's letter. The desk decides whether that satisfies "the launch row is uncommitted".
6. **Grok's own narration** in its stdout ("I'll start with the questions file and the required memory") says it read something beyond the packet folder. It wrote only its own `grok-check-d.md`; its check file cites no file outside the folder. Recorded, not judged.
7. **`sol: METER — retry after Sep 26th, 2026 6:47 AM`** · **`astra: NOT SEATED (Sol's Codex meter, Sep 26th, 2026 6:47 AM; no string on this line)`** — the desk seats them from that time (L62 R19). No packet mismatch, no checker without a check line, no `WROTE:`, no `ASK DESK`, no L74 block arrived.
8. **Standing line:** This check covers voice V1 only, PART D of four (widget, route, turn, CLI) of `04b05cd4..28b6b0c6` of `voice/v1-0923`; parts A, B, C (`16`, `17`, `18`) cover the rest, every file in exactly one part. It is round 1 of ≤3 (L67 / L39). With the seated checkers (Opus 5.5 + Grok, L67 as amended 2026-09-24) checked on EACH of the four parts and `defects that HOLD: 0` in all four, the branch is READY for a stacked deploy prompt; a HOLD goes to a classifier and a fix round — and the branch waits out of that evening's set if the fix cannot land and be checked first (L43's drop rule).
9. **Standing line:** The DEVICE SESSION (E1, E3 on his phone's file, E5, E8 / X3 behind `tailscale serve`) is **OWED** (`ls` of `reports/` shows no `voice-v1-device-*.md`; device session: NOT RUN): a design-changing device result is a fix round before the ship, whatever this check reads.
10. **Standing line:** V1's production deploy needs, beyond the merge: the migration (`--allow-prod`), the model files in the production `model_dir`, the `COBALT_VOICE_*` exports live in `ops/start_aset.sh`, and `com.cobalt.aset` restarted inside the pause (L43 / L66) — the deploy prompt carries each (build ESCALATE (vi)).
11. **Standing line:** L68 GATE EARLY (amended 2026-09-24) asks every BUILD's stop line to quote offline, with-DB AND live-note results; V1's built line (09-23, before the clause) quotes offline and with-DB only — the desk rules whether the live-note result is owed before the merge. (The desk's R23 already reads it as OWED before the merge.)

VOICE V1 CHECK DONE · part: D (widget, route, turn, CLI) · grok: CHECK VOICE V1 D: DEFECT REMAINS C13, (c) · ready for a deploy prompt: NO · dev confirm with dry-run still executes the act · opus: CHECK VOICE V1 D: DEFECT REMAINS C13, (c)-1, (c)-2, (c)-3 · ready for a deploy prompt: NO · CLI --text yes confirms production act; dry-run executes with --confirm · sol: METER — retry after Sep 26th, 2026 6:47 AM · astra: NOT SEATED (Sol's Codex meter, Sep 26th, 2026 6:47 AM; no string on this line) · defects that HOLD: 10 · ESCALATE: 11
