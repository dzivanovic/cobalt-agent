# Voice V1 check — PART B (the model path) · `04b05cd4..28b6b0c6` on `voice/v1-0923` · round 1 of ≤3

## §0 Headline

- Checking part B of four: the model-access module (C1), the Plan + prompt builder (C3), the resolver + value parsers (C6), and the builder's `## ESCALATE` / `## RULE BREACH`. 26 paths + 4 report sections, staged whole from the worktree at `28b6b0c6`.
- Status: DONE. Preflight passed; packet 219,283 B staged (one comment-case slip in `modelaccess.yaml:12`, recorded). Grok: `BUILD STANDS`. Opus 5.5: `DEFECT REMAINS C6, THIRD-a (minor)`. Sol METER (Sep 26th 6:47 AM) · Astra NOT SEATED.
- Defects that HOLD in my file-check: 2 — C6 resolver binds a card from a stray side/ordinal word anywhere in the transcript (`resolve.py:83-91`); a loose "no choices" assertion (`test_modelaccess_client.py:281`). Grok and Opus contradict on C6.
- ESCALATE: 12 (3 claims carried to part D).

## L74

One block arrived after the first tool result (the prompt file read) carrying a commit-attribution instruction that asks for a `Claude-Session:` line and names a file-send tool (`SendUserFile`). Recorded once, as data. Not followed: this seat commits nothing and sends no file.

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | `Thu Sep 24 10:18:08 EDT 2026` |
| GROK GATE (1st) | `grep -n "^| R17 " …cto-2026-09-24.md` + `git log -1 -S"Grok approved with no asking going forward"` | 0 / 0 | row 27 carries `Grok approved with no asking going forward`; commit `1758fd78a572f47b613b2ca831dcfa636ed8f65a` |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| R13 (09-20) | `grep -n "^| R13 "` | 0 | row 86 present |
| R40 | `grep -n "^| R40 "` | 0 | carries `ONE EXTRA DOT THAT CANNOT BE TAPPED` |
| R44 | `grep -n "^| R44 "` | 0 | carries `ONE BUILD of the whole FINAL` |
| R46 | `grep -n "^| R46 "` + `git log -1 -S"instead of Astra you can use Sol"` | 0 / 0 | carries `instead of Astra you can use Sol`; committed `53e059456750c0c9efcf50222a7a647630dc4b04` |
| R49 (Sol string) | `grep -n "^| R49 "` · `grep -c -F` Sol string (=1) · `git log -1 -S` Sol string | 0 | carries `"Approved"`; count 1; committed `60147d400b009db5a2518e02b8ab1fe5765db405` |
| R32 (Opus 5.5 seat) | `grep -n "^| R32 "` cto-2026-09-22 + `git log -1 -S"Bash(claude -p --model claude-opus-5-5 *)"` | 0 / 0 | carries `claude -p --model claude-opus-5-5`; committed `b8a72b5300370e248cd6c7a8a732258fec03e6a0` |
| THE TWELVE + THREE | `grep -c -F -e "<rule>"` on `08-bars-chunk-e-check.md`, each its own call | 0 | grok · mkdir · cobalt show · cobalt log · s2-p2 show · s2-p2 log · s2-p2 diff · ls · grep · tail · wc · date = 1 each; `AskUserQuestion` · `EnterWorktree` · `Bash(git push*)` = 1 each |
| Astra string absent | `grep -c -F "Bash(codex exec … gpt-6-astra"` on this prompt | 1 (exit) | 0 |
| agy string absent | `grep -c -F "\"Bash(agy *)\" \"Bash(mkdir"` on this prompt | 1 (exit) | 0 |
| R57 | `grep -n "^| R57 "` cto-2026-09-23 + `git log -1 -S"approved design"` | 0 / 0 | row 60 carries `approved design`; committed `ffee37ad5e41ab5eb451406a9e11a9e03b26afdb` |
| build launch + stop record | `grep -n "43-voice-v1-build.md"` cto-2026-09-23 · `grep -n "VOICE V1 BUILT"` · `git log -1 -S"VOICE V1 BUILT"` | 0 | launch rows R60 (line 63) / R63 (line 66); the LATER record row R71 (line 74) carries `VOICE V1 BUILT 566d1848 | on 04b05cd4 | migration 0017 …`; R108 (line 116) the tip amendment; committed `9cc68741bc8cd656d4d2e3f9d7189ad8fabba2d8` |
| re-cut committed | `git log -1 -S"VOICE V1 CHECK RECUT" -- …voice-v1-check-recut-2026-09-24.md` | 0 | `80b208c5d1304bd99ec44fe1b6dfd84fc3c91b3c` |
| THIS launch R36 | `grep -n -F "17-voice-v1-check-b.md" …cto-2026-09-24.md` + `git log -1 -S"17-voice-v1-check-b.md" -- …cto-2026-09-2*.md` | 0 / 0 | row 46 `| R36 |` names this file (row filled, no `R__`); committed `2750a8b54cdb93ecaa73c4d51ea8707649d1b794` |
| PART A HAS STOPPED | `tail -n 3 …voice-v1-check-a-2026-09-24.md` | 0 | last non-blank line: `VOICE V1 CHECK DONE · part: A (the ordered act) · grok: CHECK VOICE V1 A: BUILD STANDS EXCEPT C7, C10 · ready for a deploy prompt: NO · … · opus: CHECK VOICE V1 A: DEFECT REMAINS A1 A2 · ready for a deploy prompt: NO · … · sol: METER — retry after Sep 26th, 2026 6:47 AM · astra: NOT SEATED (…) · defects that HOLD: 3 · ESCALATE: 11` (verdict not a gate, L72) |
| worktree | `ls /Users/cobalt/cobalt-wt/voice-v1` | 0 | present |
| THE BUILT LINE | `tail -n 3` build report | 0 | `VOICE V1 BUILT 566d1848 | on 04b05cd4 | migration 0017 | offline 2422/0 | with-DB 2774/0 | experiments run: 12 of 12 | design-changing results: 3 | stt: faster-whisper/tiny.en | plan route: local.plan (mainframe) | device session: OWED (E1 E3 E5 E8 X3) | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar (6 UNCLASSIFIED) | tests added: 471 | ESCALATE: 14` → `<base>` = `04b05cd4` (= measured) |
| `<tip>` | `git log --oneline -1 28b6b0c6` | 0 | `28b6b0c6 feat(voice-v1): build report` (desk amendment R108) |
| THE RANGE | `git log --oneline 04b05cd4..28b6b0c6` | 0 | 15 commits (as the re-cut) |
| branch tip / moved | `git log --oneline -1 voice/v1-0923` · `git log --oneline 28b6b0c6..voice/v1-0923 -- tests src configs ops pyproject.toml uv.lock "docs/40 - DevDocs/cobalt" "docs/40 - DevDocs/tests"` | 0 | tip `28b6b0c6`; second call EMPTY |
| THE BOUNDARY | `git log --stat --oneline 04b05cd4..28b6b0c6` | 0 | 84 distinct paths; every one in the re-cut's `## Split` (A 25 · B 26 · C 19 · D 13 + the build report) — read against the table, no path in no part |
| NEW vs CHANGED | `git log --diff-filter=A --name-only --format= 04b05cd4..28b6b0c6` | 0 | 67 paths counted; all 26 part-B paths are printed (all NEW) |
| `.env` | `ls /Users/cobalt/cobalt-wt/voice-v1/.env` | 1 | `No such file or directory` (as required) |
| recovery | `ls scratch/tribunal-bars-0920/voice-v1-check-b` | 1 | `No such file or directory` = fresh run |
| context source | `ls scratch/tribunal-bars-0920/voice-v1-check/A` | 0 | holds `final-v1.part1/2`, `seam-s1`, `rows.part1/2`, `rulings`, `l28`, `build-report-A.part2` (+ others) — all present |
| STAGGER | `grep -n -F "no other house hub is running" …cto-2026-09-24.md` | 0 | R36 (line 46) carries the literal AND names `17-voice-v1-check-b.md` |
| CODEX SHAPE | `grep -c -F "Experiment field: **reads started**" …setups-tribunal-r2-2026-09-21.md` | 0 | `1` → a Sol launch would append ` < /dev/null` (Sol not launched) |
| SOL probe | `codex exec … -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` | 1 | `ERROR: You've hit your usage limit. … try again at Sep 26th, 2026 6:47 AM.` → **`sol: METER — retry after Sep 26th, 2026 6:47 AM`**; SKIPPED, not relaunched; **`astra: NOT SEATED — Sol's Codex meter (Sep 26th, 2026 6:47 AM)`** |
| OPUS probe | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` | 0 | `OK` → UP |
| FLOOR | Opus 5.5 UP + Grok UP | — | met (two seated) |

MEASUREMENT gate (L35): every whole-file original `wc -c` = the re-cut's table, byte for byte (26 files; the 7 context files sum 96,187; `build-report-A.part2.md` 8,519); the saved `git show 8bed61d3 -- tests/cobalt/test_voice_plan.py` = 1,391 B, `grep -c "^diff --git"` = 1. Trailing-whitespace count `grep -c -E "[[:space:]]$"` = 0 on every original. Build report headings: `## C1` 214, `## C2` 226, `## C3` 239, `## C4` 254, `## C6` 278, `## C7` 293, `## RULE BREACH` 462, `## CONTINUE` 465 — the staged ranges 214–225 / 239–253 / 278–292 / 462–464 hold.

## Packet

Folder `scratch/tribunal-bars-0920/voice-v1-check-b/` (created by the Write tool; no `mkdir`). Method: Read the original → Write the copy (the Write tool takes text, not a path), then measured. Every piece is headed by one line `### <path or command> @ 28b6b0c6 · <whole|lines a–b|git output> · <n> B` (≤ 117 B). The saved `git show` output was taken `run_in_background`; the harness saved it to `/private/tmp/claude-501/-Users-cobalt-cobalt-wt-agy-trial/e32ba7a8-028b-4909-8cc3-89ede34323a2/tasks/b8cs3p2b8.output` (1,391 B, `grep -c "^diff --git"` = 1).

| staged file | bytes | lines | holds | size proof |
|---|---|---|---|---|
| `b-code-1.md` | 25,980 | 647 | the 6 `modelaccess/*.py` + `modelaccess.yaml`, whole | = 25,504 originals + 476 B of 7 headers, exactly |
| `b-code-2.md` | 20,638 | 543 | `voice/agent.py` · `models.py` · `resolve.py`, whole | = 20,452 + 186, exactly |
| `b-tests-1.md` | 21,953 | 586 | the 3 `test_modelaccess_*.py`, whole | = 21,726 + 227, exactly |
| `b-tests-2.md` | 20,069 | 500 | `test_voice_plan.py` · the `git show 8bed61d3` diff · `test_voice_resolve.py` · `plan-replies.constructed.yaml` | = 19,729 + 340, exactly |
| `b-devdocs.md` | 12,002 | 235 | the 10 DevDocs, whole | = 11,192 + 810, exactly |
| `build-report-b.md` | 7,383 | 49 | build report lines 214–225 (C1) · 239–253 (C3) · 278–292 (C6) · 462–464 (RULE BREACH) | `grep -b` heading offsets of original vs copy: C1 3,378 · C3 1,697 · C6 1,249 · RULE BREACH 661 B (measured on the staged copy; the re-cut's "≈ 700"); + 398 B of 4 headers |
| `build-report-escalate.md` | 8,519 | 34 | copied from `voice-v1-check/A/build-report-A.part2.md` (`## ESCALATE` (i)–(xiv); header line says "packet A") | size and line count equal |
| `final-v1.part1.md` · `final-v1.part2.md` | 15,586 · 21,457 | 74 · 105 | context, copied | sizes and line counts equal |
| `seam-s1.md` | 14,433 | 120 | context, copied | equal |
| `rows.part1.md` · `rows.part2.md` | 13,946 · 21,984 | 106 · 29 | context, copied | equal (`rows.part1.md` line 25 has one trailing space, in the original too) |
| `rulings.md` · `l28.md` | 4,080 · 4,701 | 10 · 9 | context, copied | equal |
| `QUESTIONS-VOICE-V1-B.md` | 6,552 | — | the verbatim question text (5,035 B; the re-cut measured 5,033) + the appended "Files in this folder:" paragraph | each of the 5 paragraphs found verbatim on lines 76–80 of this prompt (`grep -c -F -f` = 5) |

MEASUREMENT gate (before staging): every whole-file original `wc -c` equalled the re-cut's table (see PREFLIGHT). Trailing-whitespace count of each original = 0 (the context originals: `rows.part1.md` 1, the saved diff 5 lines, all reproduced).

FIDELITY (line-set, two ways, `grep -v -x -F -f`; `-x` leaves blank lines unmatched, so each count was compared with the file's own blank-line count): for `b-code-1`, `b-code-2`, `b-tests-1`, `b-tests-2`, `b-devdocs`, the 8 copied context/escalate files and `build-report-b`, the lines of the originals absent from the copy = the blank lines only, and the lines of the copy absent from the originals = its piece headers + blank lines only — **with ONE exception: PACKET MISMATCH (mine, typed):** `configs/cobalt/modelaccess.yaml:12` reads `# routing tribunal rules — FINAL [F-23]). The routing build extends THIS` in the original; my copy (`b-code-1.md:617`) reads `… The routing build EXTENDS THIS`. A one-word case slip in a YAML COMMENT; the byte count is the same (25,980 is exact). Found by my line-set check, which ran AFTER both checkers had been launched (10:33; Opus returned 10:36, Grok 10:51) — not before. Not fixed in place: editing the folder while two checkers read it would give them different packets (L44). It is recorded here and under `## ESCALATE`; nothing in a check turns on the case of that word.

HONEST SIZE: checked files 116,544 B (25,980 + 20,638 + 21,953 + 20,069 + 12,002 + 7,383 + 8,519) + context 96,187 B + QUESTIONS 6,552 B = **219,283 B** — under the 230,000 B ceiling with 10,717 B spare (the re-cut projected 222,826 B; headers came in smaller). ≈ **54,821 tokens per checker** (÷ 4). Largest staged file 25,980 B (≤ 38,000 B).

Launches (both `run_in_background`, independent, ONE attempt each; cwd `/Users/cobalt/cobalt-wt/agy-trial`; `date` before launch **Thu Sep 24 10:32:50 EDT 2026**, the Grok gate's second row re-run then: R17 row and `git log -S` = `1758fd78a572f47b613b2ca831dcfa636ed8f65a`):
- GROK: `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "You are GROK. The folder is scratch/tribunal-bars-0920/voice-v1-check-b/ (absolute path /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v1-check-b/). Start with QUESTIONS-VOICE-V1-B.md and follow it exactly. final-v1.part1.md / final-v1.part2.md and rows.part1.md / rows.part2.md are split into ordered parts: read each pair in order as one file. Do not open any *-check-*.md file. Write your complete check to /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v1-check-b/grok-check-b.md and reply with only that path."` (no `--always-approve`).
- OPUS: `claude -p --model claude-opus-5-5 "You are OPUS. The folder is scratch/tribunal-bars-0920/voice-v1-check-b/ (absolute path …). Start with QUESTIONS-VOICE-V1-B.md and follow it exactly. <the same parts sentence> Do not open any *-check-*.md file. Read files with the Read, Grep and Glob tools only. Write no file. Print your complete check as your answer." --permission-mode plan --add-dir /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v1-check-b --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"`.
- SOL: not launched (METER, retry after Sep 26th, 2026 6:47 AM). ASTRA: NOT SEATED (Sol's Codex meter; no string on this line).

WRITTEN-NOTHING PROOF — before launch (10:32): packet folder = the 15 staged files (newest mtime 10:32); `/Users/cobalt/cobalt-wt/voice-v1` newest mtime Sep 23 15:08 (top level; `scratch` 13:47, `src` 13:44, `tests` 13:45, `ops` 14:08).

CHECKER RUNS: OPUS launched 10:33, returned 10:36:02 (≈ 3 min); stdout written by me to `opus-check-b.md` (6,928 B, without the harness's `[exited with code 0]` line). GROK launched 10:33, returned 10:51:19 (≈ 18 min, under the 45-minute clock); its stdout ended with the path of `grok-check-b.md`, written by Grok itself through its approved `--allow` (6,450 B). Neither timed out. `grep -c -i "denied\|not allowed\|permission"` = 0 on both check files.
WRITTEN-NOTHING PROOF — after Opus (10:36) and after Grok (10:51): packet folder = the 15 staged files unchanged (same sizes and mtimes) + `opus-check-b.md` (mine, 10:36) + `grok-check-b.md` (Grok's own, 10:51); no other new or changed entry. `/Users/cobalt/cobalt-wt/voice-v1` listing identical to the pre-launch listing in every entry (newest mtime Sep 23 15:08). No entry marked `WROTE:`.

## CONTINUE

next: none — collated; report closed.

## Per chunk

| chunk | what it builds | grok | opus | sol | checkers answering CLOSED |
|---|---|---|---|---|---|
| C1 | the one model-access module: loopback-only registry, guard first, think policy, off-loop call | CLOSED (`client.py:62-75`, `:116-134`, `:160-162`; `config.py:58-72`, `:94-127`; tests `test_modelaccess_client.py:173-179`, `:194`, `:200`) | CLOSED (same rows; whole-tree grep half "NOT CHECKABLE FROM READS") | not seated (METER) | 2 of 2 |
| C3 | Plan + whitelisted prompt builder; spans and allowlist checked by code | CLOSED (`agent.py:85-114`, `:130-131`, `:145-148`, `:163`) | CLOSED (`agent.py:85-115`, `:130-131`, `:144-146`) | not seated | 2 of 2 |
| C6 | resolver + value parsers; never a guessed card or value | CLOSED (`resolve.py:71-72`, `:85-92`, `:134`, `:141`, `:150-152`) | NOT CLOSED — `resolve.py:83-91`: side word and ordinal taken from every word of the transcript, so "first, move the stop on XYZ to 4.50" binds card 11 (never named); tests stay green | not seated | 1 of 2 |

## Build ESCALATE

| item | checker | answer (verbatim, ≤60 words) |
|---|---|---|
| (iv) seam §3 JEV re-point | grok | "NOT CHECKABLE FROM READS — list `src/cobalt/classify` at `28b6b0c6`. This part has no re-point. The seam's "second merger re-points" reading is not itself in dispute." |
| (iv) | opus | "AGREE. Seam §3 puts the re-point on `jev/trial-0923` when it merges second. The `guard.py` docstring names the duplicate. That `classify/` is absent on main is the builder's PREFLIGHT claim." |
| (v) R56 reading | grok | "AGREE — R56 and L28's voice paragraph bind vault-note edits, not the card stop. FINAL [F-09] still refuses a changed card target and reads the new before-after back." |
| (v) | opus | "AGREE. The L28 VOICE-ORDERED EDIT clause covers vault fields only. The card stop is a database write through `CardStore`, so `[F-09]` refuse-and-re-confirm stands." |
| (viii) RESTARTS | grok | "NOT CHECKABLE FROM READS — run `uv run cobalt jobs restarts <base>..28b6b0c6` and compare the tail." |
| (viii) | opus | "NOT CHECKABLE FROM READS. It needs a re-run of `uv run cobalt jobs restarts <base>..HEAD` and a check of which jobs import `cobalt.cli`, which would confirm the `com.cobalt.radar` restart. The 6 UNCLASSIFIED paths must be ruled before the deploy." |
| every other item | grok · opus | NOTED (both; Opus also lists (i)–(iii), (vi), (vii), (ix)–(xiv) incl. (xii) as NOTED) |

## Laws and boundary

| checker | (a) weaker assertions | (b) outside the files | (c) silent failure | (d) vault bytes |
|---|---|---|---|---|
| grok | "NONE. The later diff (`8bed61d3`, `tests/cobalt/test_voice_plan.py:147` and `:178`) retargets `PLAN_SCHEMA` to `plan_schema(AGENT)`. The assert is still equality with the registry-built schema, and the enum assert is still the allowlist. No assert removed, no parametrize narrowed, no skip, no expected value fitted to output." | "NONE. This part's new files and that diff sit on the WHAT YOU BUILD list …" | "NO PATH. `think_leak`, `prompt_refused`, `plan_parse` / `plan_tool` / `plan_span` / `plan_candidate`, and `Unparseable` all raise. A card that is not exactly one match returns `bound=False` with a clarify string. Nothing here turns those into an empty success or an execution." | "NONE. No vault path, no `VaultWriter`, no vault byte written." |
| opus | "the later diff (`test_voice_plan.py:147`, `:179`) is equally strong … One new assertion is looser than the seam's rule: `test_modelaccess_client.py:281` accepts `kind in ("empty","bad_response")` for "no choices". Seam §2.4 (6) says `empty`. The code does return `empty`, but a regression to `bad_response` would stay green. This is minor." | "NONE among part B's files. Confirming that the named protected paths … are untouched needs `git diff <base> -- <those paths>`, so that is NOT CHECKABLE FROM READS." | "NO PATH in part B. `plan_turn` either returns a validated Plan or raises `PlanFailed`, keeping the error kind. A config error or budget `ValueError` escapes loud and untyped; part D should map it to `voice_plan`." | "NONE." |

**Contradictions, quoted, not smoothed:** (1) C6 — Grok "CLOSED … Two ticker matches clarify (`:94`) unless one side word or one in-range ordinal in the transcript narrows to exactly one (`:85-92`). An ordinal is the design's named narrow, not an unbound earliest pick." against Opus "NOT CLOSED, at `voice/resolve.py:83-91` … the side word and the ordinal are taken from *every* word of the transcript, not from spans in the Plan." (2) (a) — Grok "NONE" against Opus's `test_modelaccess_client.py:281` looseness (Grok did not mention that line).

## Checked against the branch

Files: originals under `/Users/cobalt/cobalt-wt/voice-v1/` (Read tool / grep); commits from the shared store.

| # | claim · who | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| 1 | C6 NOT CLOSED: side word and ordinal come from every transcript word; "first, move the stop on XYZ to 4.50" binds card 11 · opus | `src/cobalt/voice/resolve.py:83-91` | **HOLDS** | Traced on the test rows (11 XYZ long, 13 XYZ short): words = all lowercase letter-runs; `first` → ordinal 0 → `sorted(...)[0]` = card 11, `bound=True`. Both spans are verbatim in the transcript, so the Plan validates. |
| 1a | "…to 4.50, give me a second" binds card 13; "…4.50 before long" binds card 11 · opus | `resolve.py:83-91` | **HOLDS** | `second` → index 1 → card 13; lone `long` in `words` → `matches` filtered to direction `long` → card 11. |
| 1b | the tests stay green: the only ambiguity test has no such word · opus | `tests/cobalt/test_voice_resolve.py:51-54` (also `:57-65`) | **HOLDS** | `:51-54` uses "move the stop on XYZ to 4.50"; the side (`:57`) and ordinal (`:62`) tests assert binding only WITH a side/ordinal word. No test has a filler `first`/`second`/`long`/`short` and expects a clarify. |
| 1c | design says the Plan's spans (ticker text, side, ordinal) are matched · opus | `final-v1.part1.md` §4 item 2; `rows.part2.md` C6 | consistent with the files | Both texts say "The Plan's spans (ticker text, side, ordinal …) are matched by code". `resolve_card` reads only `args.get("card")` and the transcript's words (`resolve.py:70`, `:83`). Which reading the design permits is not this hub's. |
| 2 | grok's C6 reading: ordinal/side narrowing is the design's named narrow · grok | `resolve.py:85-92`; `final-v1.part1.md` §4 item 2 | HOLDS as a description of the code; contradiction with #1 stands | The narrowing exists at `:83-92`; the disagreement is whether transcript-wide words are the "Plan's spans" — quoted above, not judged. |
| 3 | new assertion looser than the seam rule: `kind in ("empty","bad_response")` · opus (THIRD-a, minor) | `tests/cobalt/test_modelaccess_client.py:281` | **HOLDS** | Line 281 is that assertion. Only `test_empty` (`:269-273`, content `""`, `"   "`, `None`) pins `== "empty"`; nothing pins the no-choices body. Seam §2.4 (6): "no choices / no content → `empty`". Code returns `empty` (`adapters.py:105-106` → `client.py:76-77`). |
| 4 | `plan_turn` uses blocking `call_sync`, not `call`; the loop stays free only if part D runs it through `to_thread` · opus | `voice/agent.py:28`, `:163` | fact HOLDS; the `to_thread` half is **PART D — carried to 19** | `agent.py:28` imports `call_sync`, `:163` calls it. C3's row text says `cobalt.modelaccess.call`. What `turn.py` does is part D's file. |
| 5 | `validate_plan` accepts `refuse`/`clarify`/`unsupported` that still carry a tool and args · opus | `voice/agent.py:130-143` | fact HOLDS; dispatch on `kind` is **PART D — carried to 19** | Lines 130-143 reject only an off-allowlist tool, answer/act without a tool or of the wrong tool kind, unknown arg names, and args with no tool. |
| 6 | a config error or budget `ValueError` escapes untyped; part D should map it · opus | `modelaccess/client.py:89-96`; `voice/agent.py:162-165` | fact HOLDS; the mapping is **PART D — carried to 19** | `ValueError` is raised at `client.py:90`/`:94`, outside `except ModelCallError`; `plan_turn` catches only `ModelCallError`. |
| 7 | substring span check accepts a truncated span ("…14.50" / span "4.50") · opus (not a defect) | `voice/agent.py:145` | fact HOLDS (opus itself files it as not a defect) | `value.span not in transcript` is the whole check. Not counted. |
| 8 | build report's C3 section says `PLAN_SCHEMA`; the tip has `plan_schema(agent)` · opus | `build-report-b.md` C3 `### C`; `agent.py:78`, `:175` | HOLDS (fact) | The report section predates commit `8bed61d3`; the tip exports `plan_schema`. A stale record, not a class; recorded, not counted. |
| 9 | (iv) `src/cobalt/classify` absent on main · builder / opus; grok "not checkable" | `git show <rev>:src/cobalt/classify` | HOLDS (fact) | `fatal: path 'src/cobalt/classify' does not exist` at BOTH `28b6b0c6` and `04b05cd4`. |
| 10 | C1 guard runs before the adapter; zero requests on a hit · grok, opus | `client.py:116-134`; `test_modelaccess_client.py:173-188` | consistent with the files | Guard at `:117-123` precedes `adapter.complete` at `:133`; tests assert `server.requests == []`. |
| 11 | non-empty `<think>` is `think_leak`; only whitespace-only removed · grok, opus | `client.py:62-78`; `test_modelaccess_client.py:194-218` | consistent with the files | `:70-71` raises on a non-empty body, `:72-73` removes an empty one. |

Facts the prompt names, checked by me:
- **(ii) PROTECTED PATHS**, both calls: `git log --oneline 04b05cd4..28b6b0c6 -- src/cobalt/radar src/cobalt/cards src/cobalt/vaultwrite src/cobalt/heartbeat src/cobalt_agent configs/config.yaml` → EMPTY · `… -- ops/com.cobalt.aset.plist ops/com.cobalt.heartbeat.plist ops/com.cobalt.radar.plist` → EMPTY.
- **(iii)** The staged later-commit diff (`git show 8bed61d3`): two `-` lines — `-    assert calls[0].response_schema == ag.PLAN_SCHEMA` (replaced by `+ … == ag.plan_schema(AGENT)` in the same hunk) and `-    tools = ag.PLAN_SCHEMA["properties"]["tool"]["enum"]` (an assignment, replaced by `+    tools = ag.plan_schema(AGENT)["properties"]["tool"]["enum"]`; the assert after it is a context line). No assert removed without an equal replacement. `grep -n "skip\|xfail"` on `test_modelaccess_client.py`, `test_modelaccess_config.py`, `test_modelaccess_silence.py`, `test_voice_plan.py`, `test_voice_resolve.py` and `plan-replies.constructed.yaml`, each its own call → no output.
- **(iv) ONE MODEL CALLER:** `grep -rln "litellm" /Users/cobalt/cobalt-wt/voice-v1/src/cobalt` → `src/cobalt/modelaccess/adapters.py`, `src/cobalt/modelaccess/__init__.py`; `grep -rln "chat/completions" …` → `src/cobalt/modelaccess/adapters.py`. All under `modelaccess/`; no path outside it. Supplemental: `grep -rn "import litellm\|from litellm" src/cobalt` → one line, `adapters.py:6`, inside the module docstring ("`import litellm` IS silent …") — no executable import.
- **(viii) L32:** I read this report once before the last line: no ticker, price or spoken word of his written (`XYZ`, `QRS`, `4.50`, card ids and the sentence "first, move the stop on XYZ to 4.50" are the tests' and the checker's constructed values).
- **(ix) RESTARTS (L42):** the build report's field, verbatim: `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar (6 UNCLASSIFIED)` (ESCALATE (viii): `configs/cobalt/agents/voice.yaml`, `configs/cobalt/modelaccess.yaml`, `configs/cobalt/voice.yaml`, `ops/start_aset.sh`, `pyproject.toml`, `uv.lock`). `NOT CHECKABLE FROM READS — uv run cobalt jobs restarts 04b05cd4..28b6b0c6`; no checker's claim is settled by the report's own classifier table.
- **Claims handed from part A (`PART B — carried to 17`):** none — the desk's launch row R36 hands none, and part A's `## ESCALATE` carries only part-D claims.

## Ready for a deploy

| checker | check line | ready | reason (verbatim) |
|---|---|---|---|
| grok | `CHECK VOICE V1 B: BUILD STANDS · ready for a deploy prompt: YES` | YES | — |
| opus | `CHECK VOICE V1 B: DEFECT REMAINS C6, THIRD-a (minor) · ready for a deploy prompt: NO · resolver binds an ambiguous card from incidental side/ordinal words` | NO | resolver binds an ambiguous card from incidental side/ordinal words |
| sol | not seated (METER — retry after Sep 26th, 2026 6:47 AM) | — | — |

## FOR THE CLASSIFIER

1. **Claim (verbatim, opus, part B):** "**C6: NOT CLOSED, at `voice/resolve.py:83-91`.** … the side word and the ordinal are taken from *every* word of the transcript, not from spans in the Plan. … Transcript: "first, move the stop on XYZ to 4.50". … Result: `bound=True, card_id=11`. That is the earliest card by id, and it was never named." — my file:line `src/cobalt/voice/resolve.py:83-91` (tests `test_voice_resolve.py:51-65`) — HOLDS. (Grok's contrary "C6 — CLOSED" reading is quoted under `## Laws and boundary`.)
2. **Claim (verbatim, opus, part B, THIRD-a "minor"):** "One new assertion is looser than the seam's rule: `test_modelaccess_client.py:281` accepts `kind in ("empty","bad_response")` for "no choices". … a regression to `bad_response` would stay green." — my file:line `tests/cobalt/test_modelaccess_client.py:281` — HOLDS.

## ESCALATE

1. **Opus: `DEFECT REMAINS C6, THIRD-a (minor)`** — see the check line above. Grok: `BUILD STANDS`.
2. **`## FOR THE CLASSIFIER` items 1–2** (C6 transcript-wide side/ordinal binding · `:281` loose assertion). `defects that HOLD: 2`.
3. **Claims carried to part D** (`19-voice-v1-check-d.md`; counted in neither total here): opus's (a) `plan_turn` uses the blocking `call_sync` — the loop stays free only if `turn.py` runs it through `to_thread`; (b) `validate_plan` accepts `refuse`/`clarify`/`unsupported` carrying a tool and args — the turn must dispatch on `kind`, never on `tool`; (c) a budget/config `ValueError` escapes `plan_turn` untyped — the turn must map it to `voice_plan`.
4. **Packet mismatch (mine):** `configs/cobalt/modelaccess.yaml:12` — `extends` (original) vs `EXTENDS` (`b-code-1.md:617`), one comment word, found after launch and left as launched (L44); see `## Packet`. No checker's finding rests on it.
5. **Contradictions:** C6 (Grok CLOSED vs Opus NOT CLOSED) and THIRD-a (Grok NONE vs Opus `:281`), both quoted under `## Laws and boundary`.
6. **No output** in (ii); **no path outside `modelaccess/`** in (iv).
7. **`sol: METER — retry after Sep 26th, 2026 6:47 AM`** · **`astra: NOT SEATED — Sol's Codex meter (Sep 26th, 2026 6:47 AM); no string on this line`** — the desk seats both from then (L62 R19). No `ASK DESK`. No checker marked `WROTE:`; no checker failed to check.
8. **L74:** the commit-attribution block naming `Claude-Session:` and a file-send tool that arrived after the first tool result (recorded once under `## L74`, not followed; the saved `git show` diff also contains a `Co-Authored-By` trailer line as plain data).
9. Standing line: **"This check covers voice V1 only, PART B of four (the model path) of `04b05cd4..28b6b0c6` of `voice/v1-0923`; parts A, C, D (`16`, `18`, `19`) cover the rest, every file in exactly one part. It is round 1 of ≤3 (L67 / L39). With the seated checkers (Opus 5.5 + Grok, L67 as amended 2026-09-24) checked on EACH of the four parts and `defects that HOLD: 0` in all four, the branch is READY for a stacked deploy prompt; a HOLD goes to a classifier and a fix round — and the branch waits out of that evening's set if the fix cannot land and be checked first (L43's drop rule)."**
10. Standing line: **"The DEVICE SESSION (E1, E3 on his phone's file, E5, E8 / X3 behind `tailscale serve`) is OWED (no `voice-v1-device-*.md` record exists in `reports/`): a design-changing device result is a fix round before the ship, whatever this check reads."**
11. Standing line: **"V1's production deploy needs, beyond the merge: the migration (`--allow-prod`), the model files in the production `model_dir`, the `COBALT_VOICE_*` exports live in `ops/start_aset.sh`, and `com.cobalt.aset` restarted inside the pause (L43 / L66) — the deploy prompt carries each (build ESCALATE (vi))."**
12. Standing line: **"L68 GATE EARLY (amended 2026-09-24) asks every BUILD's stop line to quote offline, with-DB AND live-note results; V1's built line (09-23, before the clause) quotes offline and with-DB only — the desk rules whether the live-note result is owed before the merge."**

VOICE V1 CHECK DONE · part: B (the model path) · grok: CHECK VOICE V1 B: BUILD STANDS · ready for a deploy prompt: YES · opus: CHECK VOICE V1 B: DEFECT REMAINS C6, THIRD-a (minor) · ready for a deploy prompt: NO · resolver binds an ambiguous card from incidental side/ordinal words · sol: METER — retry after Sep 26th, 2026 6:47 AM · astra: NOT SEATED (Sol's Codex meter, Sep 26th, 2026 6:47 AM; no string on this line) · defects that HOLD: 2 · ESCALATE: 12
