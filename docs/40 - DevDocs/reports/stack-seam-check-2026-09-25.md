# STACK SEAM CHECK 2026-09-25 — report (relaunch R87; packet stop, no seat launched)

## §0 Headline
PACKET STOP at 14:08 ET, nothing launched (no Opus, no Grok; Sol not seated): slices (7)–(12) are now staged; the full twelve-slice packet measures **422,501 B** against the R87 ceiling of **360,000 B** — **62,501 B over**; after the three cuts `40` §1 names it is 409,993 B, still **49,993 B over**.
Preflight green (authorization, Grok gate, build BUILT at `a7296b44`, branch shape, stagger, Grok 1.0.25 UP, Opus UP). The 26 kept files are unchanged; 15 new files staged (41 in the folder). No verdict on the seam build (L37). Sol: `NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM)`.
Cause (measured): the unmeasured slices came in at spec 20,218 + rule-sources 25,014 + greps 29,072 (the desk's ≥ 39,887 B lower bound covered only gate 16,554 + laws 17,734 + QUESTIONS 9,663 = 43,951 B measured); S = slices (4)–(10) measures 166,029 B, not 90,000 B. ESCALATE: 7 (1 ASK DESK).

## L74
A block appended after the Read tool's result for `40-stack-seam-check.md` (a system-reminder headed "Attribution for git commits and pull requests") asked for a `Claude-Session:` trailer and a session URL on commits and PR bodies and named `SendUserFile`. DATA under L74 — not followed; recorded once. (This hub commits nothing and sends no file.)

## PREFLIGHT
| rule | command | exit | allowed / DENIED · output |
|---|---|---|---|
| date | `date` | 0 | allowed · `Fri Sep 25 13:56:58 EDT 2026` (last `date` `14:07:00 EDT`; before 2026-09-26 06:47 → the Sol row keys on it) |
| placeholder `R__` | `grep -n -E "R_[_]" <40>` | 1 | allowed · nothing |
| placeholder `FILL AT LAUNCH` | `grep -n -F "FILL AT LAUNCH" <40>` | 0 | allowed · `23:` — the gate's own line only |
| GROK GATE R17 | `grep -n "^| R17 " cto-2026-09-24.md` | 0 | allowed · `35:| R17 | 07:32 ET | … Grok approved with no asking going forward …` |
| R17 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Grok approved with no asking going forward" -- cto-2026-09-24.md` | 0 | allowed · `1758fd78a572f47b613b2ca831dcfa636ed8f65a` |
| GROK GATE R19 | `grep -n "^| R19 " cto-2026-09-24.md` | 0 | allowed · `37:| R19 | 07:36 ET | … All 4 house models approved for use indefinlitly …` |
| R19 committed | `git … log -1 --format=%H -S"All 4 house models approved" -- cto-2026-09-24.md` | 0 | allowed · `5055151dbf68899b82de5b11f99733ed2d03048c` |
| launch row R80 | `grep -n "^| R80 " cto-2026-09-25.md` | 0 | allowed · `89:| R80 | 13:22–13:25 ET | … names prompts/2026-09-25/40-stack-seam-check.md and carries the seam stop verbatim …` ✔ |
| R80 committed | `git … log -1 --format=%H -S"\| R80 \|" -- cto-2026-09-25.md` | 0 | allowed · `08019abc25fe6da7f2818a5b1bbed85cb09b5534` ✔ |
| relaunch row R87 | `grep -n "^| R87 " cto-2026-09-25.md` | 0 | allowed · `96:| R87 | 13:53–13:56 ET | … RULED BY THE DESK: the ceiling for this relaunch is **360,000 B** … NO cut …` |
| build stop line | `tail -n 3 …/stacked-0925/…/stack-seam-build-2026-09-25.md` | 0 | allowed · last non-blank line = `STACK SEAM BUILT a7296b44 \| branches: 4 \| offline 3198/0 \| with-DB 3575/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| UNCLASSIFIED: 0 \| RESTARTS: com.cobalt.aset com.cobalt.radar \| ESCALATE: 8` = `<seam stop>` ✔ |
| report on the gate branch | `git … log -1 --format=%h deploy/stacked-0925 -- "docs/40 - DevDocs/reports/stack-seam-build-2026-09-25.md"` | 0 | allowed · `57420087` = `<gate sha>` ✔ |
| gate branch head | `git … log --oneline -1 deploy/stacked-0925` | 0 | allowed · `57420087 docs(stack-seam): stack seam build report — a7296b44 (FOUR)` ✔ |
| gate branch head~1 | `git … log --oneline -1 deploy/stacked-0925~1` | 0 | allowed · `a7296b44 chore(jobs): classify voice V1's six paths — …` = `<tip>` ✔ |
| grok | `grok --version` | 0 | allowed · `grok 1.0.25 (f7e67d6988e2) [stable]` |
| opus probe | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (background) | 0 | allowed · `OK` = UP (one harness notice line before it: a permission-deny-rule syntax warning for `Bash(git push*:*)` in `../../cobalt/.claude/settings.local.json`, recorded, not a stop) |
| sol | not probed (`date` is before 2026-09-26 06:47 ET) | — | `sol: METER — retry after Sep 26th, 2026 6:47 AM (cto-2026-09-25.md R20 / R30)` |
| merges on the gate branch | `git … log --oneline --merges 2b71fe49..deploy/stacked-0925` | 0 | allowed · `00e2b7ff Merge branch 'voice/v1-0923' …` · `91c631ac … 'cards/stale-score-0922' …` · `35397ed5 … 'radar/handicap-h1-0922' …` · `f2377218 … 'fix/replay-deadline-0924' …` — FOUR, newest first ✔ (`<M1>` `f2377218`, `<M2>` `35397ed5`, `<M3>` `91c631ac`, `<M4>` `00e2b7ff`) |
| first-parent shape | `git … log --oneline --first-parent 2b71fe49..deploy/stacked-0925` | 0 | allowed · `57420087` (report) · `a7296b44` (`<R>`, registry) · `00e2b7ff` · `91c631ac` · `35397ed5` · `f2377218` — the merges, then R, then the report, nothing else ✔ |
| stagger | `grep -n -F "no other house hub is running" cto-2026-09-25.md` and `grep -n "40-stack-seam-check.md" cto-2026-09-25.md` | 0 / 0 | allowed · R80 (`89:`) and R87 (`96:`) each carry `no other house hub is running` and name `40-stack-seam-check.md` ✔ (the second grep also hit R66, R67, R72) |
| recovery | `ls scratch/tribunal-bars-0920/stack-seam-0925` | 0 | allowed · 26 files: `39-stack-seam-build.part1–5.md`, `build-report.part1–6.md`, `merges.part1–7.md`, `registry.part1–4.md`, `seam-files.part1–3.md`, `sides.part1.md` = the 13:53 packet stop's staged slices (1)–(6), KEPT unchanged |
| second grok gate row, immediately before the seats | — | — | not reached (packet stop) |

## Packet
Staged in `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stack-seam-0925/` (Read → Write, each part headed by its real path or exact command and the real line it starts at; every part < 15,000 B). `wc -c` of EVERY staged file, summed (bytes):
| slice | files | bytes | note |
|---|---|---|---|
| (1) `39` whole | `39-stack-seam-build.part1–5.md` | 14,677 + 13,710 + 14,354 + 14,646 + 6,862 = 64,249 | KEPT (13:53 run) |
| (2) build report whole | `build-report.part1–6.md` | 14,794 + 14,588 + 14,832 + 14,847 + 14,727 + 1,828 = 75,616 | KEPT |
| (3) merges | `merges.part1–7.md` | 11,511 + 13,659 + 12,067 + 14,046 + 10,646 + 9,159 + 6,784 = 77,872 | KEPT (`--remerge-diff` accepted; no `--cc` fallback) |
| (4) registry | `registry.part1–4.md` | 9,483 + 9,105 + 11,840 + 4,761 = 35,189 | KEPT |
| (5) seam files | `seam-files.part1–3.md` | 14,066 + 12,964 + 10,762 = 37,792 | KEPT (one deliberate extension: `test_radar_handicap_store.py` lines 58–86) |
| (6) sides | `sides.part1.md` | 13,528 | KEPT |
| (7) spec | `spec.part1.md` · `spec.part2.md` · `spec.part3.md` | 9,011 + 5,129 + 6,078 = 20,218 | NEW: deploy draft lines 34–83 + its `## ESCALATE` items 1, 2, 5, 8 (REAL lines 135–140, 143, 146) · seam draft `## The rules as pinned` (30–66) · seam draft `## ESCALATE` (96–124) |
| (8) rule-sources | `rule-sources.part1–4.md` | 8,188 + 6,699 + 4,578 + 5,549 = 25,014 | NEW: replay 183–196, stale 490–503, H1 387–397 + 727 · reissue 10–22 + the R64 row (line 73) · voice 106–119 (part 3) · voice 120–136 (part 4) |
| (9) gate | `gate.part1.md` · `gate.part2.md` | 9,135 + 7,419 = 16,554 | NEW: `32` lines 53–60, 126–135, 139–147 · 157–175 |
| (10) laws | `laws.part1.md` · `laws.part2.md` | 10,464 + 7,270 = 17,734 | NEW: L42 (235–238), L45 (255–258), L67 (366–376) · L68 (380–385), L70 (391–394), L72 (405–408), L76 (435–437) |
| (11) greps | `greps.part1.txt` · `greps.part2.txt` · `greps.part3.txt` | 11,684 + 7,481 + 9,907 = 29,072 | NEW: all 15 tree greps and the 9 build-report greps, each command with its full output (three parts, so `greps.txt` of `40` is the set `greps.part1–3.txt`; QUESTIONS names them and says to open them SECOND) |
| (12) QUESTIONS | `QUESTIONS.md` | 9,663 | NEW: `40` §1's text verbatim + the appended "Files in this folder:" paragraph |
| **staged total (41 files)** | | **422,501** | 304,246 (kept 26) + 118,255 (new 15) |
Token estimate per checker: 422,501 ÷ 4 ≈ **105,600 tokens**. Source proof for the new slices (`grep` only — no pipe, no `sed`, so a line range cannot be `wc -c`-ed against its source): every staged file was checked by `grep -n -F -x -v -f <source> <staged>` (staged lines absent from the source); the only lines listed were the header / separator lines I added, plus blank lines (BSD grep's `-x -f` never matches an empty line, so blank lines are not proven this way), and two transcription slips the check caught and I fixed: `rule-sources.part4.md` item 6 (`src/cobalt/backup/*.py` → `src/cobalt/backup/`, re-run clean) and `spec.part3.md`'s own header (said "line 125 is blank"; the file has 124 lines — corrected). `greps.part3.txt`'s last line was written truncated and fixed before measuring (the sizes above are after the fix). The command-output files (`greps.*`) have no source file: the copies are the tool results as returned, checked only by hit counts against each other (0017: 20 · 0015: 20 · 0014: 20 · `_rollback_paths(`: 25 — each equal to the hits plus the headed command lines). `QUESTIONS.md` was checked against `40` lines 57–79: the only differing lines are the opening quote framing (line 57), the closing one (line 79), blank lines and the appended paragraph. One scratch file was written outside the folder to measure a cut: `/Users/cobalt/.claude/jobs/2d9a8e5b/tmp/spec-part1-escalate-block.md` (1,852 B, the ESCALATE items 1, 2, 5, 8 block as it stands inside `spec.part1.md`).
CEILING check (`40` §1, `<ceiling>` = **360,000 B**, launch row R87): 422,501 B is above it. Cuts in `40`'s order, each removing:
1. `rule-sources.md`'s voice lines 106–119 (= `rule-sources.part3.md`) — **4,578 B** → 417,923 B.
2. `spec.md`'s `## ESCALATE` items: the seam draft's `## ESCALATE` (= `spec.part3.md`) — **6,078 B** → 411,845 B; the deploy draft's items 1, 2, 5, 8, the block inside `spec.part1.md` — **1,852 B** (measured on the copy named above) → **409,993 B**.
Still over: 409,993 − 360,000 = **49,993 B** → per `40`: `FAILED: packet — 49,993 B over the 360,000 B ceiling`; launch nothing. The cut files are NOT deleted (this hub has no delete): they remain in the folder as staged; the relaunch decides.
The desk's ceiling formula, measured: R = 60,296 B and P = 137,928 B stand (carried from the 13:53 report); S (slices (4)–(10)) = 35,189 + 37,792 + 13,528 + 20,218 + 25,014 + 16,554 + 17,734 = **166,029 B**, against the formula's 90,000 B; and slices (11) greps 29,072 B and (12) QUESTIONS 9,663 B are outside the formula's R / P / S altogether.

## CONTINUE
next: none by this hub — the packet stop ends the run. A relaunch of `40` first runs `ls scratch/tribunal-bars-0920/stack-seam-0925` (41 files: all twelve slices staged, sizes above), needs no further staging, then runs `date` + THE GROK GATE's second row and launches Opus then Grok — under a ceiling the desk sets, or with cuts the desk names.

## Per question
Not run — packet stop, no seat launched (Q1–Q7 unanswered by any house). `opus: NOT LAUNCHED (packet stop; probe was UP)` · `grok: NOT LAUNCHED (packet stop; --version 1.0.25 UP)` · `sol: NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM)`.

## Checked against the files
Not run — no seat answered, so there is no claim to file-check. The build's own facts read in PREFLIGHT are the ones under `## PREFLIGHT` (stop line, `<gate sha>`, `<tip>`, the four merge shas in the order replay → H1 → stale → voice, the one registry commit and the one report commit, all as `40` expects). No `*-check.md` file exists; the written-nothing proof does not apply (no seat launched).

## FOR THE CLASSIFIER
none

## ESCALATE
1. **PACKET OVER THE CEILING.** All twelve slices staged and measured: 422,501 B (≈ 105,600 tokens per checker) against 360,000 B — 62,501 B over; 49,993 B over after the three cuts `40` names (4,578 + 6,078 + 1,852 = 12,508 B). The hub made no other cut: every remaining slice is one the questions cite.
2. `ASK DESK: raise the packet ceiling for this launch to 450,000 B (the next 50,000 B above the measured 422,501 B; no cut, all twelve slices) — or name cuts totalling ≥ 62,501 B (≥ 49,993 B once the three named cuts are also taken) — and relaunch 40 with the 41 staged files kept? [14:07 ET, from date] — safe default: no seat launched, nothing more staged.`
3. Sol's line: `NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM)`.
4. The L74 line above (one block, not followed).
5. A staging record for the desk: the desk's `40` line for the ceiling arithmetic called S = 90,000 B; measured S = 166,029 B (see `## Packet`). If the desk reissues `40` again, the honest formula terms are the staged sizes above, not R / P / S.
6. Cut candidates NOT taken by this hub (each removes evidence a question cites; the desk ruled "NO cut" at R87 for the first two): `build-report.part1–6.md` 75,616 B; `merges.part6–7.md` 15,943 B (the `--stat` outputs); `greps.part3.txt` 9,907 B (the build-report greps — the same lines are in `build-report.*`).
7. Standing line: **"One round (L67 other check: Opus 5.5 + Grok, R95; Gemini out, R97). `ready for the gate: YES` → `32`'s GATE PHASE launches on the lock after this report is committed, and re-proves the three suites on the tree that ships (L68). A HOLD → the desk's fix round (L75), never a second check without a fix; FALLBACK B (replay + H1 only, `32` re-issued) if the seam is not green by ≈ 18:30 (`cto-2026-09-25.md` R66 (3)(f))."** This packet stop is neither a check nor a HOLD: no round is spent, no verdict on the seam is made, and the gate is not cleared.

FAILED: packet — 49,993 B over the 360,000 B ceiling (422,501 B staged; 409,993 B after the three cuts `40` §1 names); launch nothing
