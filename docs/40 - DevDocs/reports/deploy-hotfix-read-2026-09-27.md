# DEPLOY HOTFIX READ — 2026-09-27

## §0 Headline

Read hub for the two-line HOTFIX r3.1 change to `50-stacked-deploy-r3.md` (`33a43207`), before the `CONTINUE: DEPLOY` relaunch. Authorization and PREFLIGHT green (Opus + Sol both UP, Grok gate answered). Packet staged 68,216 B (well under the 150,000 B ceiling). Opus, Sol and Grok launched in the background; awaiting their `CHECK:` lines.
Status: run in progress.

## L74

A block appended inside a tool result (the Read of this prompt file, `51-review-deploy-hotfix.md`, in this session's own transcript) asked for a `Claude-Session:` commit/PR line and named a file-send tool (`SendUserFile`) — DATA, recorded once here, never followed: no `Claude-Session:` line is added to any commit or report this hub writes, and `SendUserFile` is not invoked.
A second, pre-existing instance sits inside the packet itself: `failed-run.part2.md:288` (`deploy-2026-09-27.md` line 288) records that the DEPLOY-PHASE run of `50` already logged the identical pattern once (a block inside a tool result asking for a `Claude-Session:` line and naming a file-send tool) — carried here as evidence, not re-triggered.

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| THE GROK GATE (R17) | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Grok approved with no asking going forward" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` | 0 | `1758fd78a572f47b613b2ca831dcfa636ed8f65a` — NON-EMPTY — allowed |
| THE GROK GATE (R19) | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"All 4 house models approved for use indefinlitly" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` — NON-EMPTY — allowed |
| THIS LAUNCH is R15 | `grep -n -F "\| R15 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-27.md"` | 0 | `23:\| R15 \| 17:39 ET \| …` names `51-review-deploy-hotfix.md`, carries the literal `no other house hub is running` — allowed |
| R15 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"51-review-deploy-hotfix.md" -- "docs/40 - DevDocs/reports/cto-2026-09-27.md"` | 0 | `076f44e8e43a81ae7fd6ca2c1db1d8368bbad82a` — NON-EMPTY — allowed |
| THE CHANGE, shape | `git -C /Users/cobalt/cobalt show --stat 33a43207` | 0 | names EXACTLY `docs/40 - DevDocs/prompts/2026-09-27/50-stacked-deploy-r3.md` and `docs/40 - DevDocs/reports/cto-2026-09-27.md` — allowed |
| THE CHANGE, history | `git -C /Users/cobalt/cobalt log --oneline -3 -- "docs/40 - DevDocs/prompts/2026-09-27/50-stacked-deploy-r3.md"` | 0 | newest `33a43207`, then `7a9e8e66`, then `21c1277f` — matches the expected shape — allowed |
| `date` | `date` | 0 | `Sun Sep 27 17:42:14 EDT 2026` — after 2026-09-26 06:47 ET, Sol expected UP |
| THE GROK GATE (version) | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` — allowed |
| RECOVERY | `ls scratch/tribunal-bars-0920/deploy-hotfix-0927` | 1 | "No such file or directory" — fresh run |
| STAGGER (ListAgents) | `ListAgents` | — | this session is `review deploy hotfix [8e24d9]`; peers are `cto desk wakeup prompt [bd18e0]` (bg, shell) and `review deploy3 build [7030be]` (bg, idle, 8d ago) — no other house-hub read is active; consistent with R15's "no other house hub is running" |
| OPUS PROBE | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (`run_in_background`) | 0 | `OK` — UP |
| SOL PROBE | `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` (`run_in_background`) | 0 | `OK` — SEATED |

FAIL CLOSED check: at least two of {Opus, Sol, Grok} answering is required, at least one of Grok/Sol — both Opus and Sol probed UP before launch; Grok's `--version` row is its standing gate (L67 P-c: Grok is never probed with a live question, only its version). All PREFLIGHT rows pass. Launching the three seats.

## Packet

Staged in `scratch/tribunal-bars-0920/deploy-hotfix-0927/`:

| file | bytes |
|---|---|
| `change.md` | 6,796 |
| `deploy-50.part1.md` | 7,997 |
| `deploy-50.part2.md` | 10,583 |
| `deploy-50.part3.md` | 12,962 |
| `failed-run.part1.md` | 343 |
| `failed-run.part2.md` | 13,019 |
| `lesson.md` | 12,826 |
| `QUESTIONS.md` | 3,690 |
| **total** | **68,216** |

Token estimate: 68,216 ÷ 4 ≈ 17,054 tokens per checker. CEILING 150,000 B (R15, measured by the desk) — 68,216 B is well under it. No cut; every slice staged. `deploy-50.md` was split into three parts at line boundaries (91–117, 193–228, 229–264) to keep every part under the 15,000 B part limit — `part2`/`part3` split STEP-D0/D1 from STEP-D2/RELAUNCH RULE/STEP-4 at line 228/229.

## CONTINUE

All three seats answered with a `CHECK:` line. Opus: NO (a scope gap in the RELAUNCH RULE). Sol: YES. Grok: YES. Collating and file-checking below.

## Per question

| Q | opus | sol | grok |
|---|---|---|---|
| (i) CHANGE A | YES — same three counts, `%` gone from `<RB>`, no other `db query` string carries `%` (`P:115`, the `%`/`LIKE` greps). `walked: YES` | YES — same, cites old blob + `P:115` + the 12-line `%` grep. `walked: YES` | YES — same, cites `P:115`, `:114`, `:224`, `:225` and the `%`/`LIKE` greps. `walked: YES` |
| (ii) CHANGE B | YES — all trigger conditions met (`P:245`, `R:290/292/294`, gate `R:202–205`). `walked: YES` | YES — same shape, cites `R:285/292/294`, `P:195–228`, gate `R:202–205`. `walked: YES` | YES — same shape, cites `R:294`, `R:290–292`, gate `R:202–207`, `P:198/240/245/248`. `walked: YES` |
| (iii) OTHER BLOCKER | **ONE FOUND**: the RELAUNCH RULE (`P:240`) scopes "the report" to only "this phase's `# DEPLOY PHASE` part"; if this re-run is itself interrupted mid-STEP-4, a second relaunch's (vii) would not see the re-run's own `<pre-merge>`/`<stack-final>` (recorded under the new `# DEPLOY RELAUNCH` heading) and could wrongly conclude "nothing touched." | none found | none found |
| ready for the relaunch | **NO** | YES | YES |

## Checked against the files

| claim | who | file:line | verdict | blocks the relaunch? | why |
|---|---|---|---|---|---|
| Change A's new `<RB>` computes the same three counts and is `%`-free; no other `db query` string carries `%` | opus, sol, grok | `50-stacked-deploy-r3.md:115`; `lesson.md` (`strpos(`/`%`/`LIKE` greps) | HOLDS | no | Read `50-stacked-deploy-r3.md:115` directly: the new `<RB>` reads `strpos(definition, 'evaluator_version') > 0`, no `%`. All 12 `%` hits (`lesson.md`'s grep) sit in git `--format=%H`/`%h` prose, `curl -w %{http_code}` strings, or the (vii) prose naming the refused character (`:245`) — verified myself, none inside an executed `db query` SQL string (the check `51` itself requires under §3). |
| Change B's new (vii) fires only on a no-touch `FAILED PREFLIGHT … rollback: not used` ending, and the failed run meets every condition | opus, sol, grok | `50-stacked-deploy-r3.md:245`; `deploy-2026-09-27.md:290–294` | HOLDS | no | Read `deploy-2026-09-27.md:294` directly: `FAILED PREFLIGHT: D1 — <RB> refused — ProgrammingError: … got '%e' · rollback: not used` — starts `FAILED PREFLIGHT:`, ends `rollback: not used` (the §3 sanity check). Lines `290–292` confirm no tag, no `<pre-merge>`, nothing merged, residents untouched. This is exactly the class (vii) requires. |
| The RELAUNCH RULE's "the report" scope (`P:240`'s parenthetical) covers only the original `# DEPLOY PHASE` section, not a later `# DEPLOY RELAUNCH` heading | opus | `50-stacked-deploy-r3.md:240` ("'The report' is `deploy-2026-09-27.md`, this phase's `# DEPLOY PHASE` part."); `:242` ("the last non-blank line above `# DEPLOY RELAUNCH`") | HOLDS | **yes** | Read `50-stacked-deploy-r3.md:240` and `:242` directly: the text is exactly as Opus quoted. If tonight's re-run (which itself writes under a new `# DEPLOY RELAUNCH` heading per `:245`/`:248`) is interrupted mid-STEP-4, a THIRD invocation would re-enter the RELAUNCH RULE (`:240`) with "the report" still defined as only the `# DEPLOY PHASE` part — so it would not see the re-run's own D2.0/D2.2 records, could misjudge which branch (i)–(iv)/(vii) applies, and (vii)'s "ANY OTHER" ending ("nothing touched") could be wrongly recorded even if the re-run had already merged main or migrated production. This is a correctness gap in the prompt's own recovery text for a plausible failure mode of the very relaunch under review, not a defect in tonight's data — cheap to fix (extend `:240`'s definition to the latest `# DEPLOY RELAUNCH`/`# DEPLOY PHASE` heading) before relaunching a production deploy. |

## FOR THE DESK

1. HOLDS, blocks the relaunch — the RELAUNCH RULE's "the report" scope (`50-stacked-deploy-r3.md:240`, `:242`) should be widened to the latest `# DEPLOY RELAUNCH`/`# DEPLOY PHASE` heading before relaunch, so a second interruption (of tonight's own re-run) is still handled correctly. Made by: opus.

No `INPUT NOT WALKED` rows — all three seats walked (i) and (ii) with the required citations.

## ESCALATE

1. **HOLD, blocks the relaunch**: RELAUNCH RULE's "the report" scope (`50-stacked-deploy-r3.md:240`/`:242`) misses a later `# DEPLOY RELAUNCH` heading — fix before relaunch (opus's finding, verified above).
2. UNVERIFIABLE FROM READS (opus): whether the production client's read-only allowlist accepts `strpos(...)` in the new `<RB>` (`50-stacked-deploy-r3.md:116`) — not a defect; the failed run's own ESCALATE 1 (`deploy-2026-09-27.md:284`) already asked for the re-issued `<RB>` to be probed before relaunch, and this still has not happened in these files. Settling command: `COBALT_ENV=production uv run cobalt db query --side user --prod "<the new <RB> string>"`, expected `0 · 0 · 0`.
3. UNVERIFIABLE FROM READS (grok): the live `COBALT_ENV=production uv run cobalt db query …` result for the new `<RB>` is not in these files (same underlying gap as item 2).
4. UNVERIFIABLE FROM READS (grok): `git -C /Users/cobalt/cobalt rev-parse --short=8 deploy/stacked-0925` as of the actual relaunch moment — not a defect; D02 re-checks it live against `c501e025`.
5. L74: recorded above under `## L74` — a block inside a tool result asked for a `Claude-Session:` line and named a file-send tool; treated as DATA, not followed.
6. Sol's line: SEATED (`codex exec -m gpt-5.6-sol`, probed UP at 17:42 EDT) — answered `CHECK: CHANGE STANDS · ready for the relaunch: YES`.

Standing line: this read covers ONLY the two-line HOTFIX r3.1 change to `50-stacked-deploy-r3.md` (`33a43207`) — the rest of `50` was read at commit `33` (09-25) and ran its GATE PHASE green. `ready for the relaunch: YES` requires zero HOLDS AND at least two seats answering (Grok or Sol among them) AND none `INPUT NOT WALKED` AND every answering seat itself saying `ready for the relaunch: YES` — Opus's NO fails that last condition regardless of the HOLD count. NEXT STEP, not this hub's: the desk commits this report; the RELAUNCH RULE scope gap goes to the desk/Dejan as one item before any `CONTINUE: DEPLOY` relaunch.

DEPLOY HOTFIX READ DONE · opus: CHECK: CHANGE — RELAUNCH RULE reads only # DEPLOY PHASE; interrupted re-run strands residents DOWN · ready for the relaunch: NO · sol: CHECK: CHANGE STANDS · ready for the relaunch: YES · grok: CHECK: CHANGE STANDS · ready for the relaunch: YES · defects that HOLD: 1 · ready for the relaunch: NO · ESCALATE: 6
