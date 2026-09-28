# Startup tribunal — round 1 hub report (2026-09-27)

## §0 Headline
Round 1: 3 of 4 houses ruled (astra, grok, anthropic seat); gemini HARNESS (headless `command` permission auto-denied, no ruling, not retried). All three ruled APPLY AFTER (fixes named per seat); 1 of 10 questions settled (Q4 HOLDS on all three); 10 DOES NOT HOLD verdicts stand.
Q7 counts disagree across seats (moved 11/10/19, changed 23/5/9); every listed case HOLDS as a text difference; grok's count line does not reproduce from its own list.
File-check: 3 Anthropic sub-claims DO NOT HOLD (FC19, FC21, FC24); astra 8 + grok 7 wrong-fact claims HOLD, 1 astra claim UNVERIFIABLE.
Owner items: astra 3, anthropic 1, grok none. New strings: none. Day report rows R45/R46 exposed the Anthropic verdict line to whole-file readers (caveat, ESCALATE 10).
ESCALATE: 12 (item 1: relaunch gemini or derive without it).

## AUTHORIZATION
Launch row: `R44` (22:25 ET, `cto-2026-09-27.md:52`) — the grep on `55-startup-tribunal.md` prints it; the prompt's filled number `R44` = the printed row. It names `startup-redesign-2026-09-27`, `Fable seat: yes`, `derive seat: claude-opus-5-5` and `no other house hub is running` (all four literals present). Rows R9 / R15 / R17 also contain "no other house hub is running" but name other prompts (`49`, `51`, `52`), so only R44 is the stagger statement for `55`.

| check | result |
|---|---|
| R13 `cto-2026-09-20.md:86` | printed (rule list) |
| R109 `cto-2026-09-22.md:56` | carries `Make all Opus 5.5 for now` |
| R95 `cto-2026-09-23.md:103` | carries `only use Fable, Astra, and Grok for new designs` |
| R97 `cto-2026-09-23.md:105` | carries `unless it's a fourth` (row text: "unless it's a fourth in the new design sessions") |
| R17 `cto-2026-09-24.md:35` (GROK GATE, row 2) | carries `Grok approved with no asking going forward` |
| R19 `cto-2026-09-24.md:37` (AGY / ASTRA GATE, row 3) | carries `All 4 house models approved` |
| R27 `cto-2026-09-27.md:35` | carries `we can't continue development` |
| R38 `cto-2026-09-27.md:46` | carries `you need to start the tribunal` |
| R40 `cto-2026-09-27.md:48` | carries `exposed to all the houses` |
| git log -S "you need to start the tribunal" | `5e716cab089ed9b468ba033b289577055495d80a` (non-empty) |
| git log -S "exposed to all the houses" | `21c77f747a0b8900fca87cf3033120b32192f2e5` (non-empty) |
| git log -S "Grok approved with no asking going forward" | `1758fd78a572f47b613b2ca831dcfa636ed8f65a` (non-empty) |
| git log -S "All 4 house models approved" | `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty) |
| git log -1 PROPOSAL.md | `5e716cab089ed9b468ba033b289577055495d80a` (committed) |
| git log -S "DESK STARTUP TUNING DONE" (sitting report) | `5e716cab089ed9b468ba033b289577055495d80a` (committed) |
| grep -F "55-startup-tribunal.md" `cto-2026-09-27.md` | R44 (`:52`) — names 55 + the four literals |
| git log -S "55-startup-tribunal.md" (desk files only) | `7a31d4679c7f05b845a5136104776961a9f9025b` (launch row committed) |
| 14 allow + 3 deny strings, each `grep -c -F` (quotes included) on `16-voice-tts-tribunal.md` | all 17 = **1** (≥1): Bash(grok *), Bash(agy *), the astra `codex exec` string, mkdir, git show, git log, 3 × s2-p2-cards, ls, grep, tail, wc, date; denies AskUserQuestion, EnterWorktree, Bash(git push*). NO NEW RULE. |
| Sol / Opus checker string in my launch line | none (the launch line carried in `55` has none) |

R41 (`cto-2026-09-27.md:49`, RECORD): "SPOON-FEED, NEVER CUT … SUPERSEDED by R42 (spoon-feed only after a shown failure)". R42 (`:50`, RECORD): "NO PACKETS: INSTRUCTIONS FILE + THE FILES, EACH HOUSE READS … a workspace-scoped seat gets an unchanged copy; ordered parts only after a shown read failure (L70)". Both on disk; run continues as written.

## PREFLIGHT
| row | rule · command | exit | allowed / result |
|---|---|---|---|
| 1 | `date` | 0 | allowed — Sun Sep 27 22:26:18 EDT 2026 (launch day 2026-09-27; desk file `cto-2026-09-27.md`) |
| 2 | R17 grep (GROK GATE) | 0 | allowed — row carries the literal |
| 3 | R19 grep (AGY / ASTRA GATE) | 0 | allowed — row carries the literal |
| 4 | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| 5 | `agy --version` | 0 | allowed — `1.2.11` |
| 6 | `ls scratch/tribunal-bars-0920` | 0 | allowed — folder exists (many subfolders) |
| 7 | `ls scratch/tribunal-bars-0920/startup/r1` | 1 | "No such file or directory" = FRESH RUN |
| 8 | STAGGER — `grep -n -F "no other house hub is running"` on `cto-2026-09-27.md` | 0 | allowed — R44 (`:52`) names `55-startup-tribunal.md` and says the literal |
| 9 | ASTRA PROBE `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background) | 0 | `OK`, exit 0, no usage-limit text → **astra: UP** (verbatim output: `OK`, `tokens used 2,265`) |
| 10 | Gemini METER | — | no probe shape exists; `agy --version` (row 5) is its preflight → **gemini: seat, launch** |

## Files copied
Root: `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/startup/r1/files/` — `repo/<path under /Users/cobalt/cobalt/>` and `vault/<path under /Users/cobalt/Vault/Think/>`. Method: Read → Write, no cut, no excerpt; `wc -c` of each copy against its original (below). EXTRA check (not required by `55`, disclosed): for every file, `grep -c -v -x -F -f <original> <copy>` (lines of the copy that equal no line of the original) equals the copy's blank-line count — i.e. every non-blank line of every copy is a line of its original; run because a hub-side typo of equal length (one `R87` typed `R82` in `proposed-_history-LAWS-2026-09-27.md.part1`) passed `wc -c`, was found by this check and fixed before any house launched. Trailing-whitespace lines (`grep -c -E '[[:space:]]$'` on the originals): 0 for every file except `.clinerules` = 2.
Sizes recorded at copy time (`wc -c` original · copy, or the parts' SUM). `cto-2026-09-27.md` was 61,446 B at the drafter's measure and 62,165 B when copied (the desk appended rows R45 / R46 after; the file is copied as it is now; original re-measured after the copy = 62,165).

| # | original path | wc original | copy | wc copy | trailing-ws | match |
|---|---|---|---|---|---|---|
| 1 | `repo docs/40 - DevDocs/plans/startup-redesign-2026-09-27/TRIBUNAL-INSTRUCTIONS.md` | 12,171 | same path under `files/repo/` | 12,171 | 0 | yes |
| 2 | `docs/40 - DevDocs/reports/desk-startup-tuning-2026-09-27.md` | 51,972 | same | 51,972 | 0 | yes |
| 3 | `docs/40 - DevDocs/reports/cto-2026-09-27.md` | 62,165 (61,446 at drafting) | same | 62,165 | 0 | yes |
| 4 | `…/startup-redesign-2026-09-27/TRIBUNAL-SUMMARY.md` | 4,304 | same | 4,304 | 0 | yes |
| 5 | `…/PROPOSAL.md` | 25,761 | same | 25,761 | 0 | yes |
| 6–9 | `…/proposed-CLAUDE.md` · `-AGENTS.md` · `-QWEN.md` · `-clinerules` | 126 · 126 · 124 · 128 | same | 126 · 126 · 124 · 128 | 0 | yes |
| 10 | `…/proposed-cobalt.md` | 3,107 | same | 3,107 | 0 | yes |
| 11 | `…/proposed-INDEX.md` | 1,679 | same | 1,679 | 0 | yes |
| 12 | `…/proposed-preferences.md` | 910 | same | 910 | 0 | yes |
| 13 | `…/proposed-writing-rules.md` | 3,209 | same | 3,209 | 0 | yes |
| 14 | `…/proposed-cto-desk-contract.md` | 9,167 | same | 9,167 | 0 | yes |
| 15 | `…/proposed-CTO-DESK-WAKEUP.md` | 6,293 | same | 6,293 | 0 | yes |
| 16 | `…/proposed-SESSION-CLOSE.md` | 3,149 | same | 3,149 | 0 | yes |
| 17 | `…/proposed-UNATTENDED-LAUNCH.md` | 5,498 | same | 5,498 | 0 | yes |
| 18 | `…/proposed-LAWS.md` | 40,617 | same | 40,617 | 0 | yes |
| 19 | `…/proposed-_history-LAWS-2026-09-27.md` | 90,209 | `.part1` 36,264 (lines 1–242, cut at `### L43`) + `.part2` 36,158 (lines 243–380, cut at `## Part IX`) + `.part3` 17,787 (lines 381–end) — ordered parts, each ≤38,000 B, cut at a heading; concatenation = the file | 90,209 (SUM) | 0 | yes |
| 20–24 | `…/proposed-_retired-cobalt.md` · `-cto-desk-contract.md` · `-preferences.md` · `-SESSION-CLOSE.md` · `-UNATTENDED-LAUNCH.md` | 3,403 · 14,731 · 1,613 · 5,382 · 8,383 | same | same | 0 | yes |
| 25–28 | `repo/CLAUDE.md` · `AGENTS.md` · `QWEN.md` | 16,590 · 1,208 · 1,879 | same | same | 0 | yes |
| 29 | `repo/.clinerules` | 2,449 | same | **2,447** | **2** | **GAP 2 B = the 2 trailing-whitespace lines (32, 33: a space after "sentences." and "process."), stripped by the Write tool; disclosed, not a stop** |
| 30–32 | `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` · `docs/40 - DevDocs/SESSION-CLOSE.md` · `docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md` | 13,102 · 5,382 · 8,383 | same | same | 0 | yes |
| 33–37 | `vault/6 - Permanent/Memory/INDEX.md` · `areas/cobalt.md` · `preferences.md` · `profile.md` · `topics/cto-desk-contract.md` | 1,912 · 5,278 · 1,456 · 706 · 16,153 | same | same | 0 | yes |
| 38 | `vault/6 - Permanent/Memory/LAWS.md` | 89,839 | `.part1` 35,894 (lines 1–239, cut at `### L43`) + `.part2` 36,158 (lines 240–377, cut at `## Part IX`) + `.part3` 17,787 (lines 378–454) | 89,839 (SUM) | 0 | yes |
| 39 | `vault/6 - Permanent/Memory/LAWS-HISTORY.md` | 32,029 | same | 32,029 | 0 | yes |
| 40–42 | `vault/…/topics/devices.md` · `areas/trading-copilot-os.md` · `areas/cobalt-houses.md` | 12,715 · 733 · 26,305 | same | same | 0 | yes |
| 43 | `repo/docs/PLACEMENT.md` | 3,522 | same | 3,522 | 0 | yes |
| 44 | `repo/docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md` | 3,576 | same | 3,576 | 0 | yes |

Every original of `## FILES` 1–4 is copied (44 files: 42 whole in one call, 2 in three ordered parts each). Total originals 585,273 B + TRIBUNAL-INSTRUCTIONS.md 12,171 B. SECRETS (L4 / L41): `grep -r -c -i -e "password=" -e "api_key" -e "secret_key" -e "BEGIN PRIVATE KEY"` over the whole `files/` tree (one recursive call listing every file, not one call per file) → 0 in every file (47 files incl. the 6 part files). No credential in any copy.
`SEARCHES.txt` (the one aid): written at `scratch/tribunal-bars-0920/startup/r1/SEARCHES.txt` — s1–s15 with full outputs and full paths; the two `git log` / `grep` outputs are copied verbatim from the tool results.

## CONTINUE
next: wait for the three houses; at each completion notice / desk message run `date`, read the finished house's output, write its `<house>-ruling.md` (Astra: final message only → `astra-ruling.md`, else `.partial.md`; Gemini: printed answer byte for byte → `gemini-ruling.md`; Grok writes its own), add a `## Clock` row; then §3 collate + file-check, then the Anthropic-seat step, then §4 close.
Launched together in ONE message 22:55 EDT (date 22:55:24 before, 22:55:42 after; conservative launch = 22:55:24), all `run_in_background`:
- ASTRA — task `b1w1ubmzr`; 30-minute deadline **23:25:24 EDT** (TIMEOUT if unfinished).
- GROK — task `bbw6tb1s1`; deadline **23:25:24 EDT**; writes `scratch/tribunal-bars-0920/startup/r1/grok-ruling.md` itself.
- GEMINI — task `bd6klt7jn`; deadline **23:25:24 EDT** (`--print-timeout 20m` in its own line).
Files: all 44 copied and checked (`## Files copied`); `SEARCHES.txt` written. The Anthropic seat `56` already finished (desk row R46 at 22:44: `STARTUP FABLE R1 DONE …`); I read nothing of it until the collate step.

## Clock
| time | trigger | minutes since launch | action |
|---|---|---|---|
| 22:26:18 | preflight row 1 | — | — |
| 22:27:10 | astra probe completed | — | astra UP |
| 22:48:23 | copy step, before the big cto-2026-09-27 copy | — | file measured 62,165 B, copied |
| 22:52:18 | SEARCHES run | — | s1–s15 |
| 22:55:24 | `date` + R17 + R19 (gates' second rows) before the launches | 0 | gates print their literals (R17 `Grok approved with no asking going forward`, R19 `All 4 house models approved`) — launch |
| 22:58:24 | completion notice: GEMINI (exit 0) | gemini 3 (finished) · astra 3 · grok 3 | **gemini: HARNESS** — its whole output, verbatim: `jetski: no output produced — a tool required the "command" permission that headless mode cannot prompt for, so it was auto-denied. Add an allow-rule under permissions.allow in settings.json (e.g. command(<target>)). Alternatively, re-run with --dangerously-skip-permissions to auto-approve all tools.` then `[exited with code 0]`. No ruling, no round spent (L67); NOT re-run by me (one attempt). No file-read failure is shown (the denial is a shell command). |
| 23:08:07 | completion notice: ASTRA (exit 0) | astra ≈12.7 min · grok ≈12.7 min (still running; ruling file 10,336 B at 23:06) | Astra's output read (final message printed twice; ITEM messages printed as it ruled; `tokens used 230,214`); final message written once to `astra-ruling.md` (34,692 B). `TRIBUNAL R1: APPLY AFTER restoring law meaning, refreshing snapshots, fixing traversal and report gates, and proving reversible apply`. All 10 items + EXPERIMENTS + OWNER + WRONG FACTS present. |
| 23:31 | close: `date` before writing the stop line | ≈36 min from 22:55 (astra and grok finished inside the 30-min clock; no TIMEOUT) | report closed; §0 filled; stop line written |
| 22:55:42 | `date` after the launches | ≈0 | astra `b1w1ubmzr` · grok `bbw6tb1s1` · gemini `bd6klt7jn` running; deadline 23:25:24 |

## Rulings table
Seats: astra = `astra-ruling.md`; grok = `grok-ruling.md`; gemini = HARNESS (no ruling); anthropic = its report (filled at the Anthropic-seat step; verdict word only). HW = HOLDS WITH · DNH = DOES NOT HOLD. Grok's Q5 and Q7 carry no verdict word (a verb table; a count line) — recorded `no verdict word`. "Agreement" counts only seats that ruled the item; a count is never a vote (L39).

| item | astra | grok | gemini | anthropic | agreement | wording offered / reason (≤25 words per seat) |
|---|---|---|---|---|---|---|
| Q1 | HW | HW | HARNESS | DNH | 2 HW · 1 DNH · 3 of 4 ruled (the seats answer different hops: astra/anthropic the SEAT PROFILE, grok the INDEX hop) | astra: profile serves Anthropic desk; other house must scratch-prove its seven verbs · grok: absolute INDEX path in cobalt.md; INDEX bullet "ignore Start here" · anthropic: per-house SEAT PROFILE blocks from Q5 tables |
| Q2 | DNH | HW | HARNESS | HW | 2 HW · 1 DNH · 3 of 4 | astra: INDEX cobalt bullet "already read"; writing-rules history/absence bullets · grok: six replacements (rules clause 2, contract "desk only", decided-with-veto, COBALT_VAULT_PATH, splints, refresh number) · anthropic: path rule for bare `[[x]]`; writing-rules to retrieve |
| Q3 | HW | HW | HARNESS | HW | 3 HW · 3 of 4; grok's TRIBUNAL line names Q3 | astra: INDEX resolves within M, LAWS bullet card rule · grok: apply step 12b (working-contract wake clause) · anthropic: UNATTENDED-LAUNCH BOUNDARIES card line |
| Q4 | HW | HOLDS | HARNESS | HOLDS | 2 HOLDS · 1 HW · 3 of 4 | astra: writing-rules:8 keeps unique meaning before deleting duplicates · grok/anthropic: shape right, defects are lines/sources |
| Q5 | HW | no verdict word (table) | HARNESS | HW | 2 HW · grok table only · 3 of 4 | astra: WAIT line via wait-stop-line.sh; OpenAI table · grok: Grok table (5 GAP rows) · anthropic: add `herdr tab list` to VIEW; profile matches live |
| Q6 | DNH | HW | HARNESS | DNH | 2 DNH · 1 HW · 3 of 4 | astra: restore CLAUDE.md obligations in cobalt.md; carry live contract additions · grok: five cobalt.md/devices/contract additions · anthropic: six contract rules + five CLAUDE.md/cobalt.md facts |
| Q7 | DNH (76·0·11·23) | no verdict word (76·0·10·5) | HARNESS | DNH (76·0·19·9) | 2 DNH · grok count only · counts differ 11/10/19 moved, 23/5/9 changed | astra: restore live sentences except approved changes · grok: paste live sentences back · anthropic: restore lines under `## Law trace` |
| Q8 | DNH | HW | HARNESS | DNH | 2 DNH · 1 HW · 3 of 4 | astra: freeze + preimage capture before apply · grok: item 3b byte-copy of LAWS/INDEX/cobalt/contract · anthropic: snapshots from live at apply; steps 12a/12b; no LAUNCH during apply |
| Q9 | DNH | HW | HARNESS | HW | 2 HW · 1 DNH · 3 of 4 | astra: rewrite summary paragraph as estimate · grok: item 18 logs two numbers · anthropic: item 18 logs prediction ≈81,500 + day's conditions |
| Q10 | DNH | HW | HARNESS | HW | 2 HW · 1 DNH · 3 of 4 | astra: words-file linked from §4; RECONCILE, lessons gate, HANDOVER, authorization rewrites · grok: L67/L73 sentences, READ 6, SESSION-CLOSE step 4 · anthropic: words file = part of day's report; close carries words |
| closing line | `TRIBUNAL R1: APPLY AFTER restoring law meaning, refreshing snapshots, fixing traversal and report gates, and proving reversible apply` | `TRIBUNAL R1: APPLY AFTER the fixes named in Q1 Q2 Q3 Q6 Q7 Q8 Q9 Q10` | HARNESS | `TRIBUNAL R1: APPLY AFTER the derive restores 28 law sentences, six contract rules, live snapshots, house profiles` | 3 of 3 that ruled: APPLY AFTER | — |

Round-2 sets: no seat wrote `DO NOT APPLY`. Items that a TRIBUNAL line names: grok names Q1 Q2 Q3 Q6 Q7 Q8 Q9 Q10; astra and anthropic name none by number.

## Wording offered, verbatim
(astra and grok only; the Anthropic seat's wordings are read by the derive from its report. Only the replacement wordings and the DOES NOT HOLD heading lines are copied; each item's reasoning is in the ruling file. Copied from `astra-ruling.md` / `grok-ruling.md`.)

### ASTRA
**Q1 HOLDS WITH** — replace the SEAT PROFILE introduction at `P/proposed-CTO-DESK-WAKEUP.md:5` with:
> SEAT PROFILE — the active vendor’s commands; changes only on his ruling. The profile below serves the Anthropic desk. Before another house takes the desk, supply and scratch-prove its LAUNCH, VIEW, LIST, STOP, MESSAGE, WAIT and MEASURE commands. Until then, that house can retrieve the desk’s state, but operational takeover is unproven. Steps below name the verbs.

**Q2 DOES NOT HOLD** — `P/proposed-INDEX.md:8` and `P/proposed-writing-rules.md:10`, `:20` permit conflicting readings.
Replace INDEX’s first start bullet:
> - `areas/cobalt.md` — already read; continue below without restarting its instructions.

Replace writing-rules’ history bullet:
> - Move historical explanation and superseded wording to the source’s history file. Keep operational identifiers, approval times, authorization literals, evidence references and current state where their readers require them. Store his words in the day’s linked words appendix; read them when verifying a ruling.

Replace its absence bullet:
> - Omit empty narration. Preserve required negative results, failure states, zero counts, no-change close outcomes and stop-line fields.

**Q3 HOLDS WITH** — insert before `## start` in `P/proposed-INDEX.md`:
> Resolve links within `/Users/cobalt/Vault/Think/6 - Permanent/Memory/`. Every active memory file has an explicit relative-path entry here; archives are indexed by directory and source. Read the start set once, then retrieve by subject. A task card selects relevant laws and files; it does not restrict access. Missing or ambiguous targets are reported with their paths.

Replace its LAWS bullet:
> - `LAWS.md` — architect, hub, builder and reviewer round 1 read in full; read-and-judge seats use their binding-law card; reviewer rounds 2–3 re-read cited sections.

**Q4 HOLDS WITH** — replace `P/proposed-writing-rules.md:8`:
> Change a rule in its canonical home. Replace duplicate instructions with a link; preserve any unique current meaning and archive superseded text before removing it. Do not edit frozen records to remove their historical copies.

**Q5 HOLDS WITH** — replace `P/proposed-CTO-DESK-WAKEUP.md:10`:
> - STOP: `claude stop <id>` · MESSAGE: `SendMessage` · WAIT: the report’s changed last non-blank stop line via `wait-stop-line.sh`; `notify_when_idle` is a session notification, not completion evidence.

(its OpenAI verb table is under `## SEAT PROFILE answers (Q5)`)

**Q6 DOES NOT HOLD** — `P/proposed-cobalt.md:16`, `:21` omit active obligations from `R/CLAUDE.md:5`, `:48`, `:51`, `:194`, `:212`, `:274`; the proposed contract also predates live additions.
Replace the Sources bullet in `P/proposed-cobalt.md`:
> - Read `docs/00 - Project/COBALT-REQUIREMENTS.md` before planning or architecture, and `docs/20 - Assessment/TRIAGE.md` before build or design. Project record: `docs/00 - Project/PROJECT-LEDGER.md`; scope: `MVP-CHARTER.md`; sequence: `SPRINT-LADDER-v0_1.md`; queue: `BACKLOG.md`. Designs: `docs/30 - Design/`; ADRs: `docs/10 - Decisions/`.

Replace its sprint-close bullet:
> - Sprint close: tests and architecture review; ADR per decision, PDD per module or feature, agent-authored DevDocs per .py accepted by the symbol-check gate. Keep backlog and kanban current; never build ahead of testing and approval.

Append to its config-boundary bullet:
> Check the loader’s glob and git-ignore placement before adding a new-core config file.

Carry these live additions into the corresponding sections of `P/proposed-cto-desk-contract.md`:
> - A drafter copying an established precedent runs on Sonnet; use Opus only for judgment the precedent does not cover, named in the launch row. Tribunal seats receive the same complete files and instructions; each reads them itself. Stage unchanged copies only where access requires it; ordered parts follow a demonstrated read failure.
> - L17 Every helper, including a read-only survey, runs as an independent background session with remote control, a herdr tab and its launch registry row; never use the in-process Agent tool for work. Mechanical and survey helpers use Sonnet.
> - C5 Push is the bare `git push origin main` or `git push origin deploy-<tag>`, alone in its call, from `~/cobalt`.
> - K20 On a non-trading day with no scanning session, the deploy phase may run after its gate is green; this remains a desk reading subject to his word. Residents-down never crosses 20:20:00–20:34:59.
> - K21 Before choosing a day for a smoke look or live proof, read the job’s `StartCalendarInterval`.

Append to K19:
> Every path a smoke row reads must be inside the launch line’s `--add-dir` set.

Add to INDEX’s retrieval set:
> - Local day-open prompt: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md`.

**Q8 DOES NOT HOLD** — apply items 2, 5 and 8–12 lack complete current preimages; item 9 overwrites live additions absent from its draft.
Insert before apply item 0 in the sitting report’s `## FOR THE DESK`:
> Freeze this apply set: no deploy, other memory writer or desk handover until verification completes. Capture each target’s exact current bytes, relative path and existence in a dated rollback directory outside every startup read path, including LAWS-HISTORY and INDEX. Compare each final draft with that captured source; reconcile all changes since proposal drafting before approval. Before each write, refuse if the target differs from its captured preimage. Record completion per item. On failure, restore completed targets in reverse order from those preimages; preserve the apply report and evidence. Keep the old wake-up active until all earlier steps and their traversal checks pass.

(its revert-per-item table: `astra-ruling.md`, Q8)

**Q9 DOES NOT HOLD** — `P/TRIBUNAL-SUMMARY.md:9` presents an estimated byte budget and unvalidated token conversion as a measured reduction.
Replace that result paragraph:
> Estimated read-output budget: 301,337 → approximately 82,800 bytes. The baseline includes estimated and conditional reads; the proposed total includes estimated row sizes and is not a measured successor wake-up. Bytes divided by four is a planning estimate, not token accounting. Measure a successor using the same house, meter definition and wake-up boundary as the recorded 136,059 baseline; report input, cached input, output, tool-output bytes and scenario separately.

**Q10 DOES NOT HOLD** — reconcile, authorization evidence, lessons migration and close ownership remain inconsistent (`P/proposed-CTO-DESK-WAKEUP.md:27`, `:32`; `P/proposed-SESSION-CLOSE.md:9`, `:13`).
Replace the wake-up RULINGS words-file sentence:
> His words go verbatim, in the same turn, to `reports/cto-<today>-words.md`, explicitly linked from §4 as the day’s report appendix, with a stable heading for each R-number. Every approval row retains its time, exact approved action and required file/hash and authorization literals. Preserve existing rows consumed by queued prompts. Read the linked words when verifying authority; routine wake-up omits already-folded quotations.

Replace RECONCILE’s last two sentences:
> Verify each candidate against its source ruling and linked words; apply only the approved meaning. An absent source, contested classification or unsettled law wording stays OPEN with the exact row and clause. A close proposal is not approval by itself.

Replace the lessons-gate step:
> Check every lesson since the last completed lessons audit, including every numbered item, against a contract rule that preserves its instruction. During migration accept existing contract citations; add `→ <rule id>` links without dropping unmapped lessons. Record all misses under `Checklist — OWED` and advance the audit boundary only after the desk applies them.

In close step 5, replace “trim preferences into …, re-measure”:
> the hub proposes the exact move to `topics/working-contract.md`; the desk applies it; the hub re-measures.

Replace HANDOVER’s identity/wait instructions:
> Identify your actual session ID through the active SEAT PROFILE. A HANDOVER applies only when its successor ID matches yours. If the predecessor is still busy, write nothing and re-read the final line after its idle notification. End it only after the profile’s liveness check establishes the safe state. A missing process-list row alone does not establish death.

In unattended AUTHORIZATION, append:
> Verify the cited §4 row and its linked words appendix together; both must be committed before launch.

Replace contract Retrieval’s words pointer:
> His words and times: the cited §4 row and its linked `reports/cto-<date>-words.md` appendix.

**Q7 DOES NOT HOLD** — the law draft removes current qualifications and changes operative meaning beyond the approved T-rulings.
Replacement instruction for the affected entries of `P/proposed-LAWS.md`:
> Restore the live sentences identified below in their original entries, removing only authorized citation/date/quotation scaffolding. Preserve operative conditions, exceptions, scope and the distinction between his rulings and desk readings. Apply only the expressly approved preamble, L6, L36, L50, L58 and L75 changes. Keep frozen routing text verbatim apart from the expressly authorized metadata removal.

### GROK
**Q1 HOLDS WITH** this replacement of the bullet under `## Start here` in `proposed-cobalt.md` (the line that now reads `Read ## NOW, then [[INDEX]].`):
```
- Read `## NOW` below. Then read `/Users/cobalt/Vault/Think/6 - Permanent/Memory/INDEX.md` once and obey its `## start`, skipping [[cobalt]] (this file). A `[[name]]` is the file in that folder — root, `areas/` or `topics/` — whose frontmatter `name:` matches.
```
and this replacement of the first bullet under `## start` in `proposed-INDEX.md` (the line that now reads `[[cobalt]] — start here, NOW, build rules`):
```
- [[cobalt]] — read `## NOW` and the sections under it. Ignore its `## Start here` line.
```

**Q2 HOLDS WITH** the following replacements. Q1's two bullets stay; where this item touches the same INDEX bullet, this text is the one to paste.
1. `proposed-INDEX.md` frontmatter `rules:` clause 2 (now `every line [stated DATE · origin], ≤DATE = bound`) becomes: `2 tag a section [stated DATE · origin] when its lines share an origin; a line of another origin keeps its own tag; ≤DATE means true at or before that date, not expired`.
2. `proposed-INDEX.md` `## start` list: replace the `[[cto-desk-contract]]` bullet with `- [[cto-desk-contract]] — read only if you are the CTO desk; every other house skips it`. Move the `[[writing-rules]]` bullet out of `## start` into a new section under it: `## before writing` / `- [[writing-rules]] — open this before you write or edit a read-path file; do not open it at start`.
3. `proposed-cobalt.md` line 24, replace `Engineering choices: decided-with-veto.` with `Engineering choices: you decide, and he may veto.`
4. `proposed-cobalt.md` line 32, replace `Prod = live install, Postgres, vault (via `COBALT_VAULT_PATH` only).` with `Prod = the running install, its Postgres, and the vault at /Users/cobalt/Vault/Think. A production process opens that vault only when its own environment sets COBALT_VAULT_PATH.`
5. `proposed-preferences.md` line 12, replace the bullet body with `In a build session he is the CTO. SMB doctrine is the standard. A guardrail supports that method; it does not replace it, and you do not drop it.`
6. `proposed-CTO-DESK-WAKEUP.md` REFRESH paragraph, replace `or on the first turn after an hour's quiet while the context is heavier than a fresh wake-up` with `or on the first turn after an hour's quiet if this session is larger than the wake-up size you logged in your first §5 MEASURE row`.

**Q3 HOLDS WITH** one added apply step, and only together with the Q1 and Q2 wording. Insert after FOR THE DESK item 12:
```
12b. `M/topics/working-contract.md` — the line that ends `every house wakes via CLAUDE.md / AGENTS.md / QWEN.md → INDEX → ## NOW → LAWS`: move that clause only to `M/_retired/working-contract.md`. Do not write a new wake path here. The path's home is the LAWS preamble and `areas/cobalt.md` `## Start here`.
```

**Q4 HOLDS.**

**Q5** (no verdict word; verb table under `## SEAT PROFILE answers (Q5)`).

**Q6 HOLDS WITH** the additions below.
1. `proposed-cobalt.md:21`, replace the sprint-close bullet with: `- Sprint close: tests, review, ADR, PDD, one DevDocs file per .py written by the agent. The symbol-check gate accepts it; it is not a generator. Test before building more.`
2. `proposed-cobalt.md:37`, append to the config bullet: ` Before adding one, run git check-ignore and a top-level configs/*.yaml glob; a hit means the old loader would read it — do not add it.`
3. Extend FOR THE DESK item 10 with a second devices line: `- [stated ≤2026-08-31 · CLAUDE.md] Interfaces include a 3-tier local voice stack. A production process sets COBALT_VAULT_PATH in ops/start_aset.sh and both ops/com.cobalt.prefill-*.plist. configs/dev/vault.yaml's committed default is ~/dev-vault-cobalt.`
4. In `proposed-cto-desk-contract.md`, add:
```
- L17 Every helper, including a read-only survey, is its own background session with remote control, a herdr tab, and an L34 row. Never use the in-process Agent tool for that work.
- C5 A push is the bare `git push origin main` (or `git push origin deploy-<tag>`), alone in its call, from `~/cobalt`. A compound call misses the allow.
- K20 On a non-trading day with no scanning session, deploy any time after the gate is green. Residents-down never crosses 20:20:00–20:34:59.
- K21 Before a smoke look or a live proof, read the job plist StartCalendarInterval. The replay fires on weekdays only.
```
5. New apply step 12c: in `areas/cobalt-houses.md` line 18, move `; --yolo only for the day-open until then` to `M/_retired/cobalt-houses.md`, and add `Morning command: docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md.`

**Q8 HOLDS WITH** one added action in front of items 4, 5, 8 and 9, and a re-copy inside item 2 for the contract. Paste into `## FOR THE DESK`, before item 4:
```
3b. Byte-copy, before any vault overwrite: `M/LAWS.md`, `M/INDEX.md`, `M/areas/cobalt.md` and `M/topics/cto-desk-contract.md` to `M/_retired/<file>.pre-apply.md`. Item 2's cobalt and contract files are not this copy. Revert of 4, 5, 8 and 9 is copying that pre-apply file back.
```
And replace item 2's contract source with: copy the live `M/topics/cto-desk-contract.md` at apply time, then fold Q6's L17, C5, K20 and K21 into `proposed-cto-desk-contract.md` before item 9. Do not freeze the sitting's snapshot.
(its revert table: `grok-ruling.md`, Q8)

**Q9 HOLDS WITH** this replacement of FOR THE DESK item 18's verify sentence:
```
18. The successor's first §5 row logs two numbers: `desk-context.sh` tokens against 136,059, and `wc -c` of each file that wake-up opened against the table in PROPOSAL.md. The byte figure is not proven by the token figure. Do not expect ≈82,800 on that first wake-up: §4 rows already in the report stay long until a later HANDOVER.
```

**Q10 HOLDS WITH** three replacements.
1. `proposed-LAWS.md` L67 (the OVERRIDE sentence, now "the desk records his words and time") becomes: `the desk records the override in reports/cto-<date>.md §4 with the time, copies his words the same turn to reports/cto-<date>-words.md, states once what is set aside, and proceeds.` L73's "each override is recorded (his words, the time)" becomes: `each override is recorded in reports/cto-<date>.md §4 with the time, his words copied the same turn to reports/cto-<date>-words.md, and bound by his condition.`
2. `proposed-CTO-DESK-WAKEUP.md` READ 6, replace `A row you cannot verify from its own words → OPEN` with `A row you cannot verify from the row plus its R<n> lines in that day's -words.md → OPEN`. After `Plus the Laws fold — PROPOSED, NOT APPLIED list`, add `His words for each R<n> on that list are in that day's -words.md.`
3. `proposed-SESSION-CLOSE.md` step 4, after `Bump updated: of every file touched`, add `and that file's line in INDEX.`

**Q7** (no verdict word): "The ten moved sentences and the five changed ones are restored by pasting the live sentence back, except the preamble quote (paste `LAWS.md.part1:21`'s quoted MECHANISM paragraph above the new wake-path sentence) and L75 (leave "one per message" out). Q10's L67 and L73 sentences are that restoration plus his T20 words file."

## SEAT PROFILE answers (Q5)
### ASTRA (OpenAI) — verbatim
| verb | your command | GAP or not | UNPROVEN? (L70) |
|---|---|---|---|
| LAUNCH | `herdr tab create …`; `herdr pane run <pane> "codex -m <model> -a on-request -s <profile>"`; worker: `codex exec -m <model> -s <profile> "<prompt>"` | Persistent desk supervision and permitted memory-write profile remain gaps | Yes: lifecycle and gates |
| VIEW | The herdr pane containing Codex | No terminal-view gap in T24’s frame; attach-by-session-ID equivalent not established | Yes: reconnect |
| LIST | No cross-process Codex session-list command established here | GAP | Yes |
| STOP | No ID-targeted Codex stop command established here | GAP | Yes |
| MESSAGE | No cross-process Codex message command established here | GAP; eventual Cobalt controller | Yes |
| WAIT | `sh /Users/cobalt/.claude/ops/wait-stop-line.sh "<report>" "<stop-pattern>" <ceiling>` | Vendor-independent report mechanism | Codex wake delivery unproven |
| MEASURE | No Codex equivalent of `desk-context.sh` established here | GAP; establish equivalent metric before adopting 500,000 | Yes |

### GROK (xAI) — verbatim
Intro: "Grok (xAI), the `grok` CLI. Remote control is omitted on purpose: his later L64 amendment, not a gap I am opening. A Claude hub is still started with the profile's own `claude --bg` string, inside a herdr tab — that is his frame, not a new command."

| verb | command | GAP or not | UNPROVEN? |
|---|---|---|---|
| LAUNCH | `herdr pane run <pane> 'cd ~/cobalt && grok --sandbox workspace -p "Read '"'"'docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md'"'"' and follow it exactly."'` | GAP. No background id, so HANDOVER has nothing to put in `<s>`. No `--remote-control` (later, his ruling). | UNPROVEN. `-p` and `--sandbox workspace` are in `areas/cobalt-houses.md:17` and `:60`. No `grok --bg` is in the files. |
| VIEW | `herdr tab create --workspace w2 --cwd /Users/cobalt/cobalt --label "CTO" --no-focus`, then the LAUNCH pane run | GAP. Nothing in the files re-attaches a viewer to a live grok session (`claude attach` has no grok twin). | herdr itself is his frame. The missing attach is a gap, not an unrun claim. |
| LIST | Claude hubs: `claude agents --json` (the profile string, from the shell). This grok desk: none | GAP for the desk's own id. Claude rows are not a gap. | UNPROVEN that the grok sandbox will exec `claude`. His frame says the house can start another vendor; it does not say the sandbox allows that binary. |
| STOP | Claude hubs: `claude stop <id>` from the shell. This grok desk: none | GAP for stopping the grok desk. | Same sandbox question for `claude stop`. No `grok stop` in the files. |
| MESSAGE | none | GAP. No `SendMessage`. A line written into the hub report is a different channel; a hub waiting on a chat message will not see it. | UNPROVEN whether any current hub polls its report for an answer. |
| WAIT | `wait-stop-line.sh` on the report path, as contract W1 (`proposed-cto-desk-contract.md:47`). The file is on disk (`SEARCHES.txt` s12). | not a gap. His frame: WAIT is the stop line, vendor-free. The profile's `notify_when_idle` is the Claude tool, not this verb, once the desk is Grok. | UNPROVEN only inside the grok sandbox. |
| MEASURE | none | GAP. `desk-context.sh <id>` (`proposed-CTO-DESK-WAKEUP.md:11`) reads a Claude transcript. A grok id has no reading there, so REFRESH never fires on a number. | No grok context command in the files. Do not invent one. |

### GEMINI: HARNESS — no table.

## Law trace claims (Q7)
### ASTRA — count line verbatim
`L1–L76 traced: 76 entries · sentences lost: 0 · current law moved to history: 11 · meaning changed: 23.` — "“Lost” means absent from both destinations. “Moved” means an operative sentence has no counterpart in its proposed entry. “Changed” means its replacement drops or changes an operative qualification. Counts are distinct source-sentence findings, not word differences."
Every non-zero case, verbatim (`H:L<n>` = that entry in `P/proposed-_history-LAWS-2026-09-27.md`; `D:L<n>` = that entry in `P/proposed-LAWS.md`):

| ID | Law · live sentence verbatim | Where it went; finding |
|---|---|---|
| M1 | L12 · “Design-phase time is now bounded by L67's three-round cap and L73 (no law step is ever skipped for speed) rather than by a planning-cap law of its own.” | H:L12 only; D:L12 retains only retirement, not the replacement rule. |
| M2 | L15 · “The clause "vault/.env/personal layer excluded" that previously qualified the carve-out's scope is removed: L44 (09-12) gives every house equal read access to the vault, and a build-time tool carve-out may not narrow that.” | H:L15 only; D:L15 keeps “repo code only” without the access clarification. |
| M3 | L17 · “Epistemic diversity > role diversity for high-stakes judgment.” | H:L17 only; lens diversity does not preserve this comparative priority. |
| M4 | L29 · “"Never auto mode on a write path" (present in the 09-03/04 wording, LEDGER:630-632) was silently absent from the 09-10 fold wording.” | H:L29 only; frozen-entry sentence removed beyond stripping its amendment tag. |
| M5 | L29 · “Not a deliberate drop — restored above.” | H:L29 only; same frozen-text issue. Preserve or obtain his explicit classification as removable history. |
| M6 | L34 · “The day `cobalt_jobs` records agent sessions, this clause is amended, not silently bypassed.” | H:L34 only; explicit amendment requirement missing. |
| M7 | L45 · “The 09-10 R2 rule restricting the repo to a single synthetic example screen is REVOKED as the root cause of the 09-12 production failure; the revocation stands (exact revoked wording: LAWS-HISTORY H-R2).” | H:L45 only; a current revocation is not merely a historical citation. |
| M8 | L58 · “`SESSION-CLOSE.md` names the runner of every step.” | H:L58 only; the draft procedure complies today but loses the standing requirement. |
| M9 | L58 · “A status line written between closes goes to the desk report, not to NOW.” | H:L58 only; destination constraint disappears. |
| M10 | L67 · “The counts, the floor, the round cap, the shrink-to-two clause and "the meter is a precondition" (L47) are unchanged; Sol and Astra draw on the same Codex allowance — the probe stays a preflight.” | H:L67 only; other clauses preserve counts, but not the shared allowance and required probe. |
| M11 | L67 · “Applies to every prompt drafted from 2026-09-23 18:10 ET (prompts drafted earlier run as written).” | H:L67 only; grandfathering is an operative condition. |
| C1 | L4 · “A named `.env` bootstrap tier is permitted, scoped exactly to: the Postgres docker-compose credential, the app DB login (`COBALT_DB_USER`/`COBALT_DB_PASSWORD`), and the Mattermost DB role — nothing else.” | H:L4; D:L4’s “`.env` holds only a bootstrap tier” widens a secret restriction into a restriction on all contents. |
| C2 | L7 · “No variable, grader, or detector ever flips from human-fed to engine-fed without a shadow run (engine computes silently alongside Dejan's hand input for N sessions), agreement stats reviewed, and HITL-token approval (NN#12 — it IS a trading-logic change).” | H:L7; D:L7 changes the enduring requirement to generic approval. Keep token approval plus the bounded interim exception. |
| C3 | L17 · “Privacy default flipped: vault and personal layer are exposable to any vendor or local model at Dejan's choice (opt-out, not opt-in); secrets excluded on every channel (F19).” | H:L17; D:L17 omits the opt-out default. |
| C4 | L18 · “Every process registered w/ maxTurns + timeout + heartbeat; watchdog surfaces zombies; kill phrase stops all.” | H:L18; D:L18 requires attributes but drops registration. |
| C5 | L19 · “A CONTINUE relaunch is a full re-issue when the prompt file is unchanged and the only addition is ONE `CONTINUE:` prefix line naming the resume point (L47, L60).” | H:L19; D:L19 drops the requirement to name the resume point. |
| C6 | L28 · “Sync-revert carve-out to human-wins: when the on-disk unit text differs from the baseline but equals any of Cobalt's last 10 `unit_after` values for that unit, the change is a SYNC REVERT (Obsidian Sync putting an older Cobalt write back), not a human edit: Cobalt's new text wins, no override rows, the write row records `sync_revert_of = <matched write id>`, one loud log line.” | H:L28; D:L28 names the field but not its required matched-write-ID value. |
| C7 | L28 · “The CTO desk's hand edits under L58 (the memory folder) and L65 (his own notes, on his ruling) are not Cobalt writes; they carry their own trace (before/after in the desk report) and close into a Cobalt command the day one ships (L58).” | H:L28; D:L28 drops migration of hand edits to the shipped command. D:L58 alone covers memory, not the whole L65 scope. |
| C8 | L31 · “Known offender `cameron_grid` → rename in ADR-0008.” | H:L31; D:L31 says it “is renamed,” turning an obligation into apparent completed state. |
| C9 | L32 · “Finviz `f=` filter strings carry the same classification and protection as the rest of user data under this law — needing no separate secret-style protection — but classification and protection remain distinct rules and must not be conflated.” | H:L32; D:L32 omits no-separate-secret-protection. |
| C10 | L32 · “"User data" governs what leaves this install for OTHER Cobalt users.” | H:L32; D:L32 drops “for OTHER Cobalt users,” broadening scope. |
| C11 | L33 · “CoS calls ROLES, never flags or binaries; roles are fixed launcher profiles (reviewer = read-only for verification runs, network disabled; writer = workspace-write in a worktree, on-request; researcher = read-only + web).” | H:L33; D:L33 drops the writer’s `on-request` mode. |
| C12 | L46 · “SCOPE: this law governs ONE agent's own branch — wip-committed, a clean tree at run end, never outliving its own deploy.” | H:L46; D:L46 drops the explicit wip-commit condition. |
| C13 | L47 · “But the switch is PER-BUILD, not sticky: every build starts from the assessment of the task itself, the meter is a precondition checked BEFORE launch, and if the right model is unreachable and the alternative is a poor fit, say so rather than proceed.” | H:L47; D:L47 keeps “say so” but drops “rather than proceed.” |
| C14 | L56 · “The Obsidian + Postgres memory layer in `6 - Permanent/Memory/` is THE memory for every agent; no house keeps a private store.” | H:L56; D:L56 drops the Obsidian + Postgres layer. |
| C15 | L58 · “This file changes only from the close prompt's list of that day's approved rulings, each carrying his words, the time and the exact fold text, applied by the desk.” | H:L58; D:L58 drops the close-list source constraint. |
| C16 | L58 · “`## NOW` is a SNAPSHOT: rewritten whole at every close and every desk refresh, at most 1,500 characters, measured like the always-loaded block.” | H:L58; D:L58 drops the measurement obligation. |
| C17 | L62 · “A permission string Dejan has ruled standing is on every later launch line's pre-approved pool and is never asked again; the launch row cites the ruling instead of a dated grant.” | H:L62; D:L62 drops the required ruling citation. |
| C18 | L67 · “The exception is an EMERGENCY design or development while more than one house is unavailable; then fewer checkers are allowed.” | H:L67; D:L67 drops “more than one.” |
| C19 | L67 · “Desk readings, not his words (`close-2026-09-23.md` (c) OPEN 1–2): a "new build" is the first check of a new feature's build, everything after it is "other"; the Anthropic seat named "Fable" runs as 09-22 R109 pins it (Opus 5.5) until his word.” | H:L67; D:L67 presents these readings as unqualified law. |
| C20 | L67 · “The desk records the override with his words and the time in the day's desk report, states once what is being set aside, and proceeds.” | H:L67; D:L67 drops the reporting destination. Reconcile explicitly with T20. |
| C21 | L73 · “The desk does not ask whether he wants to overrule: it says in ONE line which laws his instruction set aside, records the override with his words and the time in the day's desk report, and proceeds; his "do it now" also stands as the approval of that action's command list (L62) — no second approval is asked.” | H:L73; D:L73 drops the reporting destination and compresses the no-second-approval instruction. |
| C22 | L74 · “No hub re-asks, no close re-proposes it, and no reply to him mentions it unless he asks.” | H:L74; D:L74 drops the exception for his asking. |
| C23 | L76 · “A production deploy's with-DB gate takes the lock alone; the desk launches no build that can touch `cobalt_dev` between the gate's cut and its stop line.” | H:L76; D:L76 expands “the desk launches no build” into “nothing … launches.” |

### GROK — count line verbatim
`L1–L76 traced: 76 entries · sentences lost: 0 · current law moved to history: 10 · meaning changed: 5`
Every non-zero case, verbatim (`LAWS.md.part<k>:<n>` = the copied part files the house read):
- `L17 · Epistemic diversity > role diversity for high-stakes judgment. · history only (`LAWS.md.part1:106`) · not in `proposed-LAWS.md:62-63``
- `L33 · writer = workspace-write in a worktree, on-request · history only (`LAWS.md.part1:193`) · proposed writer has no on-request (`proposed-LAWS.md:118`)`
- `L34 · The day `cobalt_jobs` records agent sessions, this clause is amended, not silently bypassed. · history only (`LAWS.md.part1:199`) · not in `proposed-LAWS.md:121-122``
- `Reading · The hub's fold job refuses a bare `R<n>` or `§<n>` reference in either direction. · history only (`LAWS.md.part1:12`) · not in `proposed-LAWS.md` Reading`
- `Reading · `O<n>` is never used for a new ruling. `PROPOSED-1…6` are read, never written in new text. · history only (`LAWS.md.part1:13-14`) · not in proposed Reading`
- `Reading · a line beginning `— ` is a citation, never law; a paragraph labelled `Status note` or `State (not law)` is state, never law · history only (`LAWS.md.part1:15`) · not in proposed Reading`
- `L58 · the record NOW summarises lives in the desk report and the ledger. A status line written between closes goes to the desk report, not to NOW. · history only (`LAWS.md.part2:86`) · proposed says only "replaced NOW text is not kept" (`proposed-LAWS.md:196`)`
- `L67 · Sol and Astra draw on the same Codex allowance — the probe stays a preflight. · history only (`LAWS.md.part2:133`) · not in `proposed-LAWS.md:230``
- `Preamble · the 09-13 MECHANISM quote, which the proposal says stays verbatim · paraphrased (`proposed-LAWS.md:12-13`); the quote is history (`LAWS.md.part1:21`) · `PROPOSAL.md:155` required the quote verbatim. The new wake path in that paraphrase is his T3 and is right.`
- `L58 · This file changes only from the close prompt's list of that day's approved rulings, each carrying his words, the time and the exact fold text. · generalized to "his approved rulings (his words, the time, the exact fold text)" (`proposed-LAWS.md:194`) · his L58 change was move-to-history, section tags, and merging the close. It was not dropping the close list as the carrier of his words.`
- `L67 · The desk records the override with his words and the time in the day's desk report · "records his words and time" with no place (`proposed-LAWS.md:229`) · the place is the law (`LAWS.md.part2:130`)`
- `L73 · records the override with his words and the time in the day's desk report · "recorded (his words, the time)" with no place (`proposed-LAWS.md:250`) · the place is the law (`LAWS.md.part3:36`)`
- `L59 · Read-and-judge seats receive index-card excerpts of the binding laws only · "get index-card excerpts" (`proposed-LAWS.md:200`) · "only" is gone (`LAWS.md.part2:90`)`

### GEMINI: HARNESS — no trace.
### ANTHROPIC — its count line and cases are file-checked under `## Anthropic-seat round-1 claims, file-checked` (FC rows); the derive reads its report.

Counts side by side (quoted, not smoothed; a count is never a vote): astra 76 · 0 · 11 · 23 — grok 76 · 0 · 10 · 5 — anthropic 76 · 0 · 19 · 9. ARITHMETIC: astra's 11 = M1–M11 and 23 = C1–C23 (rows listed = counts); anthropic's 19 = its 20 MOVED items minus item 6 "(not counted — KEPT)" and its table column sums to 19 / 9 (OK); grok's count line says 10 + 5 = 15 but it lists 13 lines (14 if line 146's two sentences count separately) — WRONG AT the count line (2 cases stated, not listed). The three seats classify differently (astra calls L33 `on-request` "changed", grok calls it "moved").

## Checked against the files
Verdict words: HOLDS · DOES NOT HOLD · UNVERIFIABLE FROM READS · ARITHMETIC OK. `Pn` = `P/proposed-<name>` line n in the ORIGINAL proposal folder; `Mn` = live memory file; `LAWS.md:n` = live line. Each row was opened by me in the real file (Read, or `grep -n -F` / `-c -F` on the original path; commands are in `## Clock` order, nothing wrapped). A claim about how a CLI, harness or model BEHAVES that nobody ran is UNVERIFIABLE with the run that settles it (L70). "Meaning changed" / "current law vs history" classifications are the seats' readings; what I verify is the TEXT (live sentence present at the live line; proposed entry lacks it).

| # | claim | who | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|---|
| CK1 | the SEAT PROFILE intro is `proposed-CTO-DESK-WAKEUP.md:5` and its commands are Anthropic tools (`claude --bg/stop/agents`, `ListAgents`, `SendMessage`, `notify_when_idle`, `desk-context.sh`) | astra Q1, anthropic Q1 | P-WAKEUP:5–11; PROPOSAL.md:130 "The SEAT PROFILE exists only for Anthropic" | HOLDS | profile block lines 5–11 all name Claude tools; PROPOSAL:130 says so itself |
| CK2 | startup pointers and map are house-neutral: AGENTS:3, cobalt:7, INDEX:7 | astra Q1 | P-AGENTS:3; P-cobalt:7; P-INDEX:7 | HOLDS | each is a path/link to cobalt.md / INDEX / the start list |
| CK3 | INDEX:8 lists `[[cobalt]]` (already open) while cobalt:7 says "Read `## NOW`, then [[INDEX]]" — a cycle for a literal reader | astra Q2, grok Q1/Q2, anthropic Q2 | P-INDEX:8; P-cobalt:7 | HOLDS | both lines read as stated; whether a Qwen session loops is UNVERIFIABLE (X: cold Qwen traversal) |
| CK4 | writing-rules:10 moves ruling dates/times/R-numbers off the read path while the wake-up row shape carries `R<n>` and a time | astra Q2 | P-writing-rules:10; P-WAKEUP:32 | HOLDS | :10 "ruling dates, times, R-numbers … goes to its history file"; :32 requires `| R<n> | <time> | …` rows |
| CK5 | writing-rules:20 "Never state an absence" vs required zero/none evidence | astra Q2 | P-writing-rules:20; P-SESSION-CLOSE:9 | HOLDS | SESSION-CLOSE:9 requires the line `Checklist — OWED: none`; a literal reader meets both |
| CK6 | links are bare names; only the stub/READ 1 carry an absolute path; `_imports/` holds two more `preferences.md` | astra Q3, grok Q1, anthropic Q2 | P-CLAUDE:3; P-cobalt:7; P-INDEX (all `[[x]]`); `ls M/_imports/anthropic-2026-09-05`, `…-15` | HOLDS | both import folders list `preferences.md`; with M/preferences.md that is three files of that name (a fourth after apply step 2) |
| CK7 | INDEX:11 "in full unless your prompt gives you a card (L59)" vs L59 "Architect, hub, builder and reviewer round 1 read LAWS.md in full" | astra Q3 | P-INDEX:11; P-LAWS:200 | HOLDS | L59 text names builders as full readers; the INDEX exception can be read as skipping |
| CK8 | writing-rules:8 "deleted on sight" vs :13 "Keep all the meaning" | astra Q4 | P-writing-rules:8, :13 | HOLDS | both lines present as quoted |
| CK9 | the proposal calls WAIT vendor-free; the profile's WAIT names `notify_when_idle` | astra Q5, grok Q5, anthropic Q5 | PROPOSAL.md:131; P-WAKEUP:10 | HOLDS | :131 "WAIT is already vendor-free (… `wait-stop-line.sh`)"; :10 "WAIT: `notify_when_idle`" |
| CK10 | launcher syntax `-a on-request -s …` is recorded at `cobalt-houses.md:19`; grok `-p` / `workspace` at :17 and :60 | astra Q5, grok Q5 | M/areas/cobalt-houses.md:17, :19, :60 | HOLDS | :19 "`-a on-request` with `-s read-only` or `-s workspace-write`"; :17 workspace profile; `-p` is at :60 (not :17) |
| CK11 | `desk-context.sh` and `wait-stop-line.sh` exist; the first reads a Claude transcript | grok Q5 | SEARCHES s12; live WAKEUP:28 "the context size from the last recorded usage in the desk's own transcript" | HOLDS | both scripts listed in `~/.claude/ops`; transcript sentence is in the live wake-up |
| CK12 | no cross-process Codex list / stop / message / meter command exists (astra), no `grok --bg`, no grok context command (grok) | astra Q5, grok Q5 | copied files only | UNVERIFIABLE FROM READS | absence claimed from a scoped read (L35); run: `codex`, `grok` CLI help in a scratch session (astra X3/X8, grok X2) |
| CK13 | proposed-cobalt omits CLAUDE.md obligations: REQUIREMENTS read-before-planning, symbol-check gate + agent-authored DevDocs, kanban, `git check-ignore` | astra Q6, grok Q6, anthropic Q6 | R/CLAUDE.md:5, :51, :194, :212, :274; P-cobalt:16, :21, :37 | HOLDS | `grep` of P-cobalt: `symbol`, `kanban`, `check-ignore` = 0; TRIBUNAL/TRIAGE "read before building" is present at :16 (the "or design" half is not) |
| CK14 | the live contract has six rules the proposed contract and its snapshot lack: line 41 (drafters/packets), :61 L17, :72 C5, :119 K19 tail, :120 K20, :121 K21 | astra Q6/Q8, grok Q6/Q8, anthropic Q6 | M/topics/cto-desk-contract.md:41, :61, :72, :119–121; `grep -c` of "L17 Every helper", "C5 Push", "K20", "K21", "every path a smoke row" on P-cto-desk-contract = 0 | HOLDS | all six present live; count 0 in the proposed contract; the retired snapshot (125 lines) ends at L16 / no such lines |
| CK15 | the retired contract is stale: 125 lines vs live 130 | astra WF, grok Q8, anthropic Q8 | SEARCHES s13; P-_retired-cto-desk-contract.md | HOLDS | s13: 125 vs 130 lines; 14,731 B vs 16,153 B (the proposal's "before 14,553" is a third number) |
| CK16 | `working-contract.md:40` still states the old wake path and no apply item touches it | grok Q3/Q6, anthropic Q6 | M/topics/working-contract.md:40 (SEARCHES s8); sitting FOR THE DESK 0–18 | HOLDS | :40 "every house wakes via CLAUDE.md / AGENTS.md / QWEN.md → INDEX → `## NOW` → LAWS"; item 12 only touches cobalt-houses:26 |
| CK17 | `cobalt-houses.md:18` carries stale `--yolo`; the full Qwen morning command is `DAY-OPEN-QWEN.md:7–9`, whose card says read nothing else | grok Q6 | M/areas/cobalt-houses.md:18; R/docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md:5, :7–9 | HOLDS | :18 "`--yolo` only for the day-open until then"; DAY-OPEN-QWEN:5 "INDEX CARD (read nothing else)" |
| CK18 | `devices.md:31` says "(CLAUDE.md boundary unchanged)" while step 15 moves the boundary out | anthropic Q8 | M/topics/devices.md:31 | HOLDS | line present as quoted |
| CK19 | FOR THE DESK gives no pre-apply copy of INDEX / LAWS / cobalt.md / contract / devices / trading-copilot-os / cobalt-houses; retired-cobalt is a 3,403 B extract of a 5,278 B file | astra Q8, grok Q8, anthropic Q8 | sitting report FOR THE DESK items 1–12 (:165–184); P-_retired-cobalt.md; live cobalt.md 5,278 B | HOLDS | items 2–3 write only retired extracts / repo originals; "What Cobalt is (one screen)" live line is in neither retired-cobalt nor proposed-cobalt |
| CK20 | retired-preferences differs from live only in frontmatter; SESSION-CLOSE and UNATTENDED snapshots equal their live files | astra Q8, grok Q8 | P-_retired-preferences.md:2–5; P-_retired-SESSION-CLOSE / -UNATTENDED vs live | HOLDS | `grep -c -v -x -F -f live snapshot` = 2 (preferences frontmatter), 4 and 7 (= their blank-line counts); byte order not compared (cmp not run) |
| CK21 | the history file is the live LAWS body plus a 3-line wrapper (90,209 − 89,839 = 370 B; 456 = 453 + 3 lines) | astra Q7, grok Q7/Q8/X3, anthropic Q7/Q8 | P-_history-LAWS…:1–3; `grep -c ""` LAWS 453, history 456 | HOLDS | line-set both ways: 113 history lines not in LAWS = 111 blank + 2 header lines; 110 LAWS lines not in history = its 110 blank lines |
| CK22 | byte identity / order of the history body vs live LAWS | astra, grok X3 | — | UNVERIFIABLE FROM READS | line-set and line count equal; `cmp` of the body after the 3-line wrapper is the run that settles it |
| CK23 | items 0's new grep is safe today: `APPROVED — pending fold` absent; `cto-2026-09-27.md` carries `APPROVED — launch at 21:41` (R26), `— smoke Mon 21:41` (R32), `— overnight run` (R43) with no `APPLIED:` | grok Q8 | SEARCHES s4, s5; cto-2026-09-27.md:34, :40, :51 | HOLDS | s4 prints nothing; the three statuses are as quoted (directions, not folds) |
| CK24 | nothing forbids a hub LAUNCH between apply step 4 (new LAWS) and step 15 (stubs); the gate line forbids only "during a running deploy" | anthropic Q8 | sitting report:162 | HOLDS | :162 "never during a running deploy; the desk applies, a hub proposes nothing here" |
| CK25 | the sitting's 20 measure rows sum to 301,337 | astra Q9, grok Q9, anthropic Q9 | sitting report:18–37 | ARITHMETIC OK | 85,956 + 89,839 + 20,874 + 19,443 + 16,590 + 14,553 + 13,102 + 9,949 + 7,860 + 5,800 + 4,011 + 3,392 + 1,902 + 1,912 + 1,655 + 1,456 + 1,417 + 665 + 561 + 400 = 301,337 (steps re-added) |
| CK26 | 109,156 − 15,943 − 5,059 − 6,039 + 492 + 180 = 82,787 ≈ 82,800; and 15,943+5,059+6,039 = 27,041 − 672 = 26,369; 192,181 + 26,369 = 218,550; 301,337 − 218,550 = 82,787 | astra, grok, anthropic Q9 | PROPOSAL.md:75, :78 | ARITHMETIC OK | each step re-computed; 1,589 + 5,502 + 546 + 49,251 = 56,888; 135,293 + 56,888 = 192,181 |
| CK27 | §4 after-size is ≈1,600 at PROPOSAL:38 but 3,500 implied at :78 (19,443 − 15,943) | astra Q9/WF, anthropic WF 8 | PROPOSAL.md:38, :78; sitting:128 | HOLDS | :38 "≈1,600 est."; 19,443 − 15,943 = 3,500 |
| CK28 | drafts on disk differ from the proposal's after-figures: LAWS 40,617 vs 40,588, contract 9,167 vs 9,051, wake-up 6,293 vs 6,241, INDEX 1,679 vs 1,488, writing-rules 3,209 vs 2,782 | grok Q9, anthropic Q9/WF 7 | SEARCHES s1; PROPOSAL.md:29, :34, :37, :44, :74 | HOLDS | s1 sizes vs the table cells |
| CK29 | rows 1–20 minus the two tilded rows = 295,137; +5,800 +400 = 301,337 | grok Q9 | sitting report:18–37 | ARITHMETIC OK | 301,337 − 5,800 − 400 = 295,137 |
| CK30 | the summary line "wake-up file reads ≈301 KB → ≈83 KB" vs the wake-up file itself 13,102 → 6,293 B | grok WF | TRIBUNAL-SUMMARY.md:9; SEARCHES s1 | HOLDS | :9 as quoted; 301,337 is the slice sum (sitting:39) |
| CK31 | live L67 OVERRIDE (LAWS.md:369) and L73 (:413) say "in the day's desk report"; proposed L67:229 and L73:250 drop the place; PROPOSAL/SUMMARY say L58/L67/L73 hold without text change | astra Q10/Q7, grok Q10/Q7, anthropic Q10 | LAWS.md:369, :413; P-LAWS:229, :250; PROPOSAL.md:38; TRIBUNAL-SUMMARY.md:38 | HOLDS | `grep` of P-LAWS: "in the day's desk report" absent; PROPOSAL:38 row 10 says they "hold without text change" |
| CK32 | live L58 requires the close list to carry his words, time and fold text; proposed SESSION-CLOSE step 2 asks only for the fold text and `R<n>` | grok Q10, anthropic Q10 | LAWS.md:323; P-SESSION-CLOSE:8 | HOLDS | :323 "each carrying his words, the time and the exact fold text"; :8 "the exact fold text and its `R<n>`" |
| CK33 | the AUTHORIZATION block of the proposed UNATTENDED-LAUNCH no longer names his words; prompts (55, 56, 57, 50) gate on literals (`must carry`) in §4 rows | anthropic Q10, astra Q10 | P-UNATTENDED-LAUNCH:11; SEARCHES s15; prompt 55's R109/R95/R97 gates | HOLDS | :11 lists "row numbers, the time" only; s15 lists four prompts with `must carry`; whether a literal is a quotation is X5 (unrun) |
| CK34 | R11 records an authorization-literal mismatch found at a launch read | astra Q10 | cto-2026-09-27.md:19 (R11 (4)(a)) | HOLDS | R74 named `THE THREE PRODUCTION MIGRATIONS`, not the literal the gate greps; the desk corrected the gate |
| CK35 | proposed SESSION-CLOSE step 4 drops the live step 4's "and the INDEX line of every file touched" | grok Q10 | D/SESSION-CLOSE.md:17; P-SESSION-CLOSE:11 | HOLDS | live :17 "Bump `updated:` and the INDEX line of every file touched"; proposed :11 "Bump `updated:` of every file touched" |
| CK36 | HANDOVER lines today begin `HANDOVER: predecessor <p> → successor <s> at <time>` and REFRESH (6) still writes that shape | grok Q10 | cto-2026-09-27.md:82, :84; P-WAKEUP:36 | HOLDS | both lines start as quoted; proposed (6) "append `HANDOVER: predecessor <own id> → successor <s> at <time>`" |
| CK37 | STEP 0 "When LIST shows `<p>` idle or absent: STOP it" vs L60 "liveness verified by asking, never inferred from process or transcript signals" | astra Q10 | P-WAKEUP:15; P-LAWS:203 | HOLDS | textual tension as quoted; L60 itself is unchanged |
| CK38 | FOR THE DESK step 17/proposal say push only on his word; item 17 commits repo files (no restart, docs only) | (context for astra Q8) | sitting:183 | HOLDS | as stated |
| CK39 | build-firewall rule not fully restored: proposed preferences:12 omits "nothing from coaching / DRC / trading sessions enters code without asking him how" | astra WF | P-preferences:12; M/topics/working-contract.md:39; PROPOSAL.md:35 | HOLDS | :12 "In build sessions he is the CTO; SMB doctrine is the standard; guardrails are splints"; working-contract:39 carries the ask-how rule |
| CK40 | Grok and agy have no dedicated startup file in the repo root | astra Q6, grok Q6/X1 | SEARCHES s11 | HOLDS | root has CLAUDE.md, AGENTS.md, QWEN.md, .clinerules only; auto-discovery is UNVERIFIABLE (experiment) |
| CK41 | Qwen's path ≈10k tokens of LAWS inside a 262,144 context | grok Q3, anthropic Q3 | P-LAWS 40,617 B; CLAUDE.md:91 "context 262144" | ARITHMETIC OK | 40,617 ÷ 4 = 10,154 |
| CK42 | behaviour claims: a cold Qwen/Sonnet/Sol session "will" loop, skip LAWS, resolve `[[x]]` in the wrong folder, delete a unique condition, use the wrong writer profile | astra Q2/Q3/Q4/Q7, grok Q1/Q2 | — | UNVERIFIABLE FROM READS | model / CLI behaviour, not in any file; runs: astra X1, X2, X12; grok X1; anthropic X2, X4, X9 (scratch cold-start per house) |

### Q7 — the cases, file-checked one by one
For each: the live sentence is at the live line (verbatim as the seat quotes it; checked by reading `LAWS.md` at that line), and the proposed entry lacks it (`grep -c -F` of a fixed phrase on the ORIGINAL `proposed-LAWS.md`, or a read of the entry). Verdict HOLDS = the text difference exists as stated. Where a sentence sits: `H` = present in the history file (line-set proven, CK21).

| ID | live line | proposed check | verdict |
|---|---|---|---|
| astra M1 (L12) | LAWS.md:79 | "planning-cap" = 0; P-LAWS:48 "retired; number never reused." | HOLDS |
| M2 (L15) | :97 | no "may not narrow"; P-LAWS:57 carve-out "for repo code only" | HOLDS |
| M3 (L17) | :106 | "epistemic" = 0 | HOLDS |
| M4 (L29 note) | :173 | note absent; the rule itself is kept at P-LAWS:104 ("never auto mode on a write path") | HOLDS (note sentence only) |
| M5 (L29) | :173 | "deliberate drop" = 0 | HOLDS |
| M6 (L34) | :199 | "silently bypassed" = 0 (P-LAWS:121–122) | HOLDS |
| M7 (L45) | :256 | "REVOKED" = 0 (P-LAWS:154) | HOLDS |
| M8 (L58) | :324 | "names the runner" = 0 | HOLDS |
| M9 (L58) | :325 | "between closes" = 0 | HOLDS |
| M10 (L67) | :372 | "same Codex allowance" = 0 (P-LAWS:230) | HOLDS |
| M11 (L67) | :372 | "drafted earlier" = 0 | HOLDS |
| C1 (L4) | :44 | P-LAWS:25 "`.env` holds only a bootstrap tier" | HOLDS |
| C2 (L7) | :56 | P-LAWS:34 "HITL approval" (no "-token"); interim clause kept | HOLDS |
| C3 (L17) | :107 | "opt-out" = 0 (P-LAWS:63) | HOLDS |
| C4 (L18) | :112 | P-LAWS:65–66 "Every process has maxTurns, timeout and heartbeat" (no "registered") | HOLDS |
| C5 (L19) | :117 | P-LAWS:69 no "naming the resume point" | HOLDS |
| C6 (L28) | :162 | "matched write" = 0 (P-LAWS:98 "records `sync_revert_of`") | HOLDS |
| C7 (L28) | :165 | "the day one ships" = 0 (P-LAWS:100) | HOLDS |
| C8 (L31) | :182 | "renamed by ADR-0008" = 1 (P-LAWS:112) | HOLDS |
| C9 (L32) | :187 | "secret-style" = 0 | HOLDS |
| C10 (L32) | :189 | "OTHER Cobalt users" = 0 (P-LAWS:115) | HOLDS |
| C11 (L33) | :193 | "on-request" = 0 (P-LAWS:118) | HOLDS |
| C12 (L46) | :262 | P-LAWS:157 no "wip" (the only "wip-committed" is L60, :203) | HOLDS |
| C13 (L47) | :266 | "rather than proceed" = 0 (P-LAWS:160) | HOLDS |
| C14 (L56) | :311 | "Obsidian + Postgres" = 0 (P-LAWS:188) | HOLDS |
| C15 (L58) | :323 | "close prompt" = 0 (P-LAWS:194) | HOLDS |
| C16 (L58) | :325 | "measured like" = 0 (P-LAWS:196) | HOLDS |
| C17 (L62) | :344 | "cites the ruling" = 0 (P-LAWS:210) | HOLDS |
| C18 (L67) | :367 | "more than one" = 0 (P-LAWS:229) | HOLDS |
| C19 (L67) | :372 | "desk readings" = 0 (P-LAWS:230) | HOLDS |
| C20 (L67) | :369 | P-LAWS:229 "records his words and time" (no place) | HOLDS |
| C21 (L73) | :413 | P-LAWS:250 "recorded (his words, the time)" (no place) | HOLDS |
| C22 (L74) | :420 | "unless he asks" = 0 (P-LAWS:253) | HOLDS |
| C23 (L76) | :436 | P-LAWS:259 "nothing that can touch `cobalt_dev` launches" | HOLDS |
| grok L17 / L33 / L34 | :106 / :193 / :199 | as M3 / C11 / M6 | HOLDS ×3 |
| grok Reading ×3 | :12, :13–14, :15 | "refuses a bare" = 0; "never used for a new" = 0 / "PROPOSED-" = 0; "citation, never" = 0 (P-LAWS:5–10 Reading) | HOLDS ×3 |
| grok L58 NOW / status line; L67 Codex allowance | :325; :372 | as M9 / M10 | HOLDS ×2 |
| grok Preamble quote paraphrased | :21 (part1:21) | "MECHANISM" = 0 (P-LAWS:12–13); PROPOSAL.md:155 says the quote stays verbatim | HOLDS |
| grok L58 close-list carrier; L67 override; L73; L59 "only" | :323; :369; :413; :329 | as C15 / C20 / C21; P-LAWS:200 "get index-card excerpts" (no "only") | HOLDS ×4 |
| FROZEN (astra, grok, anthropic): L5 L21–L27 L29 L49 verbatim apart from tags/citations | — | `grep -n -x -F -f LAWS.md P-LAWS` prints P-LAWS:28, :75, :81, :84, :87, :91, :104, :166 byte-identical; L22 :78, L25 ¶2 :88, L27 :94, L29 ¶2–3, L49 ¶2 are the live text with tags/citations removed (read) | HOLDS |

Anthropic's MOVED 1–20 and MEANING 1–9 are checked below (FC rows); the sentences in the two seats overlap: L33 `on-request` (all three), L34 (all three), L67 Codex allowance (all three), L67/L73 place of record (grok, anthropic; astra C20/C21), L58 status line / runner (astra, anthropic), L17 (astra M3/C3, grok, anthropic MEANING 2), L45 (astra, anthropic), L56 (astra, anthropic), L31, L19, L62, L28 (astra, anthropic).

## Anthropic-seat round-1 claims, file-checked
Run at 23:27 EDT (`date`), then `tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/startup-tribunal-fable-r1-2026-09-27.md"` → its LAST NON-BLANK line = `STARTUP FABLE R1 DONE · verdict: APPLY AFTER the derive restores 28 law sentences, six contract rules, live snapshots, house profiles · holds: 1 · holds with wording: 5 · does not hold: 4 · law: traced 76, lost 0, moved while current 19, meaning changed 9 · experiments named: 9 · ESCALATE: 0` (starts `STARTUP FABLE R1 DONE `). Read: `## DIGEST`, `## Rulings`, `## Law trace`, `## Self-attack`, `## WRONG FACTS`, `## OWNER`. Its verdicts: Q1 DNH · Q2 HW · Q3 HW · Q4 HOLDS · Q5 HW · Q6 DNH · Q7 DNH · Q8 DNH · Q9 HW · Q10 HW; its `TRIBUNAL R1:` line: `TRIBUNAL R1: APPLY AFTER the derive restores 28 law sentences, six contract rules, live snapshots, house profiles`. Its report line numbers below are found with `grep -n` on its report (Q1 :27, Q2 :42, Q3 :44, Q5 :63, Q6 :67–71, Q8 :75–76, Q9 :80, Q10 :84–86, Q7 :89, MOVED :183–202, MEANING :205–213, WRONG FACTS :252–260, OWNER :248). WITHDRAWN by the seat, not checked: (a) "Only the stub carries an absolute path" (:230); (b) "the desk's reconcile … marks them OPEN" (:231); (c) "PLACEMENT carries D6 + the `_inflight` rule" (:232).

| # | claim (seat report line) | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| FC1 | Q1 (:27): the SEAT PROFILE is Anthropic-only; PROPOSAL:130 says so | P-WAKEUP:5–11; PROPOSAL.md:130 | HOLDS | as CK1 |
| FC2 | Q1 (:27): STEP 0.2 `:15` "When LIST shows `<p>` idle or absent: STOP it"; 0.3 `:16` "Your id = LIST's background row with cwd `~/cobalt`" | P-WAKEUP:15, :16 | HOLDS | both lines as quoted |
| FC3 | Q1 (:27): REFRESH MEASURE reads a Claude transcript (`:35`, `desk-context.sh`) | P-WAKEUP:11, :35 | HOLDS | :11 names the script; the transcript reading is the live wake-up's own sentence (CK11) |
| FC4 | Q1 (:28): L49 (FROZEN) forbids composing, so a Qwen desk cannot write prompts, rows or NOW | LAWS.md:280 / P-LAWS:166 | HOLDS | L49 text "READS AND JUDGES, never COMPOSES … no report authoring"; that a desk row is "composing" is the seat's reading |
| FC5 | Q2 (:42): M holds three `preferences.md` (M/, two `_imports/`); fourth after apply step 2 | `ls M/_imports/anthropic-2026-09-05`, `…-15`; sitting:168 | HOLDS | both import folders list `preferences.md` (CK6) |
| FC6 | Q2 (:42): INDEX:7 lists `[[cobalt]]`; :13 lists `[[writing-rules]]` under "start" while PROPOSAL:37 says not read at every start | P-INDEX:7–8, :13; PROPOSAL.md:37 | HOLDS | line cited :7 is the `## start` heading; the `[[cobalt]]` bullet is :8 (off by one) |
| FC7 | Q2 (:42): WAKEUP:27 names LAWS "How to read this file"; proposed LAWS renames it `## Reading` (:5) | P-WAKEUP:27; P-LAWS:5 | HOLDS | `grep -c "How to read this file"` on P-LAWS = 0 |
| FC8 | Q2 (:42): SESSION-CLOSE:13 "Over = the close FAILS: trim preferences" with runner "hub measures" | P-SESSION-CLOSE:13 | HOLDS | row 5 as quoted; L58 makes memory writes desk-only |
| FC9 | Q2 (:42): WAKEUP:32 gives no status for a ruling of his that folds nothing and launches nothing | P-WAKEUP:32 | UNVERIFIABLE FROM READS | statuses listed: pending-fold→APPLIED, LAUNCHED, RECORD (+ report path); whether RECORD fits is a reading |
| FC10 | Q3 (:44): the AUTHORIZATION paragraph is at UNATTENDED-LAUNCH:11 (the BOUNDARIES card line anchors there) | P-UNATTENDED-LAUNCH:11 | HOLDS | :11 is the "AUTHORIZATION — VERIFY IT YOURSELF" paragraph |
| FC11 | Q3 (:44): a card seat is not told to open cobalt.md; whether it follows the stub unprompted | — | UNVERIFIABLE FROM READS | run: anthropic X3 (card-driven `claude -p` with the stub and a card omitting cobalt.md) |
| FC12 | Q3 (:44): Qwen path ≈10k tokens of LAWS inside 262,144 | P-LAWS 40,617 B | ARITHMETIC OK | 40,617 ÷ 4 = 10,154 |
| FC13 | Q5 (:51,:63): the profile LAUNCH string is byte-identical to the live wake-up's | R/…/CTO-DESK-WAKEUP.md:1; P-WAKEUP:7 | HOLDS | the `cd ~/cobalt` + `claude --bg …` string in both lines reads identically (both files open) |
| FC14 | Q5 (:63): `herdr tab list` is in live :5 and missing from the profile VIEW | live WAKEUP:5; P-WAKEUP:8 | HOLDS | live STEP 0 paragraph names it; P-WAKEUP:8 VIEW lacks it |
| FC15 | Q5 (:63): the wake-up's WATCHES line (:39) never names `wait-stop-line.sh` | P-WAKEUP:39 | HOLDS | :39 "WATCHES: every notice is a full-context turn …" no script name |
| FC16 | Q5 (:63): vendor literals outside the profile: UNATTENDED-LAUNCH:7 (`claude --bg`), :25 (`claude -p`, `pgrep`), contract:62 (`Bash(claude stop *)`), against writing-rules:16 | P-UNATTENDED-LAUNCH:7, :25; P-cto-desk-contract:62; P-writing-rules:16 | HOLDS | each line carries the literal; :16 says "Vendor commands live only in a SEAT PROFILE" |
| FC17 | Q5 (:63) X5: `notify_when_idle` is the tool name the harness exposes | — | UNVERIFIABLE FROM READS | run: scratch Claude session, call it on an idle hub (anthropic X5) |
| FC18 | Q6-1 (:67): six live contract rules missing from draft and snapshot at live :41, :61, :72, :119, :120, :121 | M-contract:41, :61, :72, :119–121 | HOLDS | as CK14 |
| FC19 | Q6-1 (:67): the live contract is "131 lines" | `grep -c ""` = 130 (SEARCHES s13) | DOES NOT HOLD | s13 prints 130 for the live file (125 for the snapshot); 16,153 B matches |
| FC20 | Q6-2 (:68): CLAUDE.md:10 / AGENTS.md:7 "do not substitute a stale copy or invent a resolution" is in no draft | R/CLAUDE.md:10; R/AGENTS.md:7; P (all) | HOLDS | `grep -rl -F "stale copy"` over the proposal folder prints nothing |
| FC21 | Q6-2 (:68): the phrase appears in P "only [in] the history file" | P-_history-LAWS… | DOES NOT HOLD | the same grep prints no file at all, history included (that file holds LAWS, not CLAUDE.md) |
| FC22 | Q6-3 (:69): CLAUDE.md :276 (agent-authored DevDocs, symbol-check), :51 (kanban), :212 (`git check-ignore`) dropped at P-cobalt:21/:16/:37 | R/CLAUDE.md:51, :212, :276; P-cobalt:16, :21, :37 | HOLDS | as CK13 |
| FC23 | Q6-3 (:69): prompt `36-drc-d2-fix-r1-build.md:111` cites "the CLAUDE.md rule" on DevDocs | D/prompts/2026-09-25/36-drc-d2-fix-r1-build.md:111 | HOLDS | "DevDocs (agent-authored, the CLAUDE.md rule; …" |
| FC24 | Q6-3 (:69): prompt `39-stack-seam-build.md:137` cites "the CLAUDE.md rule" | D/prompts/2026-09-25/39-stack-seam-build.md | DOES NOT HOLD | `grep -n -F "CLAUDE.md rule"` on that file prints nothing |
| FC25 | Q6-4 (:70): `M/areas/cobalt.md:12` "the two import files …" is in neither proposed-cobalt nor retired-cobalt | M/areas/cobalt.md:12; P-cobalt; P-_retired-cobalt | HOLDS | `grep -c -F "import files"`: live 1, proposed 0, retired 0 |
| FC26 | Q6-5 (:71): `working-contract.md:40` keeps the old wake path; no apply item touches it | M/topics/working-contract.md:40 | HOLDS | as CK16 |
| FC27 | Q8(i) (:75): step 1's snapshot is proven identical to live LAWS; 456 = 453 + 3 | `grep -c ""`; line-set | HOLDS | as CK21 |
| FC28 | Q8(ii) (:75): no step keeps a copy of INDEX; cobalt.md's retired file holds only moved lines | sitting:167–184 | HOLDS | as CK19 |
| FC29 | Q8(ii) (:75) X6: restic restores `M/` files (contract:123 "restic restores") | M-contract:123 | UNVERIFIABLE FROM READS | the sentence exists at :123 (M1 rule); that a repository holds `Memory/` and restores one file is the run (anthropic X6) |
| FC30 | Q8(iii) (:75): `devices.md:31` "(CLAUDE.md boundary unchanged)" becomes stale after step 15 | M/topics/devices.md:31 | HOLDS | as CK18 |
| FC31 | Q8(iv) (:75): nothing forbids a LAUNCH between step 4 and step 15 | sitting:162 | HOLDS | as CK24 |
| FC32 | Q9 (:80): 301,337 re-sums exactly | sitting:18–37 | ARITHMETIC OK | as CK25 |
| FC33 | Q9 (:80): 82,787 ≈ 82,800 | PROPOSAL.md:75, :78 | ARITHMETIC OK | as CK26 |
| FC34 | Q9 (:80): the drafts' sizes differ from the after-table (6,293 / 9,167 / 40,617 / 1,679 / 3,209) | SEARCHES s1; PROPOSAL.md | HOLDS | as CK28 |
| FC35 | Q9 (:79): 136,059 − 54,600 = ≈81,500 | PROPOSAL.md:78 | ARITHMETIC OK | 136,059 − 54,600 = 81,459 |
| FC36 | Q10-1 (:84): live L67/L73 place-of-record text at LAWS.md:369, :412, :413; proposed drops it (:229, :250); SUMMARY:38 says no text change | LAWS.md:369, :412, :413; P-LAWS:229, :250; TRIBUNAL-SUMMARY.md:38 | HOLDS | as CK31 (:412 is the L73 "his clause" line "recorded with his words and the time") |
| FC37 | Q10-2 (:85): L58 needs his words + time; SESSION-CLOSE:8 asks for fold text + `R<n>` | LAWS.md:323; P-SESSION-CLOSE:8 | HOLDS | as CK32 |
| FC38 | Q10-3 (:86): prompt 55 gates on words in a §4 row (`R109` "Make all Opus 5.5 for now"); UNATTENDED-LAUNCH:11 drops "his words" | `55-startup-tribunal.md` AUTHORIZATION; P-UNATTENDED-LAUNCH:11 | HOLDS | both as quoted (I ran the R109 gate myself: the row carries the literal) |
| FC39 | OWNER 1 (:248): live L58 says LAWS changes only from the close list; the live wake-up folds LAWS entries from any `APPROVED` row (`WAKEUP:17`); the draft widens to "his approved rulings" (:194) | LAWS.md:323; R/…/CTO-DESK-WAKEUP.md:17; P-LAWS:194 | HOLDS | three lines as quoted; whether B or A is his law choice (L39) — quoted under OWNER |
| FC40 | Q7 table sums (:97–177): MOVED column 19, MEANING column 9 | seat report :97–177 | ARITHMETIC OK | moved: 5+1+1+2+1+1+5+1+2 = 19; meaning: 1+1+1+1+1+1+2+1 = 9 |
| FC41 | Q7 (:95): FROZEN lines :28 :75 :81 :84 :87 :91 :104 :166 byte-identical; :78 :88 :94 :105–106 :167 live text minus tags | P-LAWS; `grep -n -x -F -f` | HOLDS | the eight line numbers are exactly the lines my run printed as identical |

Q7 MOVED 1–20 (19 counted; #6 "(not counted — KEPT)"), each: live sentence at the cited `LAWS.md` line and absent from `proposed-LAWS.md` (greps run: "editorial", "cited by filename", "refuses a bare", "never used for a new", "PROPOSED-", "never bare", "no-change", "Uncertain classification", "newly dated", "settles", plus M-greps above; FC42.n):
| FC42.1 | How to read :10 "editorial consolidations" | absent ("editorial" = 0) | HOLDS |
| FC42.2 | :12 "External documents are cited by filename" | absent | HOLDS |
| FC42.3 | :12 "fold job refuses a bare R<n> or §<n>" | absent | HOLDS |
| FC42.4 | :13 "never used for a new ruling" (O<n>) | absent | HOLDS |
| FC42.5 | :14 PROPOSED-1…6 "read, never written" | absent | HOLDS |
| FC42.6 | L19 :117 "naming the resume point" | absent (C5) | HOLDS |
| FC42.7 | L28 :165 "…the day one ships" | absent (C7) | HOLDS |
| FC42.8 | L33 :193 "on-request" | absent (C11) | HOLDS |
| FC42.9 | L33 :194 "never bare … means the sandbox flag" | absent ("never bare" = 0; P-LAWS:118 has "`exec` takes no `-a`") | HOLDS |
| FC42.10 | L34 :199 "amended, not silently bypassed" | absent (M6) | HOLDS |
| FC42.11 | L45 :256 revocation | absent (M7) | HOLDS |
| FC42.12 | L58 :324 "names the runner" | absent (M8) | HOLDS |
| FC42.13 | L58 :325 "between closes" | absent (M9) | HOLDS |
| FC42.14 | Fold :453 "no-change close records that outcome" | absent ("no-change" = 0) | HOLDS |
| FC42.15 | Fold :453 "Uncertain classification stays OPEN" | absent | HOLDS |
| FC42.16 | Fold :453 the close hub's inputs | absent ("newly dated" = 0) | HOLDS |
| FC42.17 | L62 :344 "cites the ruling instead of a dated grant" | absent (C17) | HOLDS |
| FC42.18 | L67 :370 "This settles what L29's 'two parties, ≤3 rounds' becomes … four houses" | connecting sentence absent ("settles" only in L72); L29's "two parties, ≤3 rounds" kept at P-LAWS:105 | HOLDS |
| FC42.19 | L67 :372 "Sol and Astra draw on the same Codex allowance" | absent (M10) | HOLDS |
MEANING 1–9 (FC43.n): each live→draft text difference as the seat quotes: 1 L13 `:87`→`P-LAWS:51` ("Claude protects Dejan's time, including from the project itself" → "Protect his time, including from the project") HOLDS · 2 L17 opt-out → "may go … at his choice" (P-LAWS:63) HOLDS · 3 L20 `:121`→`:72` (subject Claude dropped) HOLDS · 4 L31 `:182`→`:112` "is renamed" HOLDS · 5 L56 `:311`→`:188` (Postgres half dropped) HOLDS · 6 L58 `:323`→`:194` HOLDS · 7 L67 `:369`→`:229` HOLDS · 8 L67 `:372`→`:230` (labels dropped) HOLDS · 9 L73 `:413`→`:250` HOLDS — nine rows, nine HOLDS (FC43.1–9).
Anthropic WRONG FACTS 1–9 (FC44.n): 1 SUMMARY:3 "T1–T21" vs sitting:9 "25" HOLDS · 2 PROPOSAL:3 "T1–T5 … DRAFT" vs sitting:6 "CLOSED 21:45 EDT" HOLDS · 3 SUMMARY:38 / PROPOSAL:38 "hold without text change" vs P-LAWS:229/:250 HOLDS (CK31) · 4 PROPOSAL:155 quote stays verbatim vs P-LAWS:12–13 (no quote) HOLDS · 5 PROPOSAL:159 names a LAWS "Not law" line; P-LAWS has no such section HOLDS · 6 PROPOSAL:34 "before 14,553 … snapshot" vs 14,731 / 16,153 B HOLDS (its "131 lines" sub-claim = FC19, DOES NOT HOLD) · 7 PROPOSAL:32 "13,102 → 5,585", :44 "5,749 → 6,241", :29 INDEX "1,488" vs 6,293 / 1,679 B HOLDS · 8 PROPOSAL:38 "≈1,600" vs :78 / sitting:128 3,500 HOLDS · 9 PROPOSAL:46 "3,014 chars" vs drafts 1,679 + 706 + 910 = 3,295 B (ARITHMETIC OK; chars UNVERIFIED — `wc -m`) HOLDS as the text difference — nine rows, nine HOLDS.

Anthropic-seat R1 claims checked: 66 HOLD of 78 checked (FC1–FC41 = 41 rows: 29 HOLDS · 3 DOES NOT HOLD [FC19, FC21, FC24] · 4 UNVERIFIABLE [FC9, FC11, FC17, FC29] · 5 ARITHMETIC OK [FC12, FC32, FC33, FC35, FC40]; FC42.1–19 = 19 HOLDS; FC43.1–9 = 9 HOLDS; FC44.1–9 = 9 HOLDS; 29 + 19 + 9 + 9 = 66; 41 + 19 + 9 + 9 = 78).

## Experiments named (L70)
Deduplicated by what each runs; `named by` seat + its own `X<n>`. None is run by me. The result that would change the design is the seat's claim.

| experiment | named by | gates (the seat's claim) | result that would change the design |
|---|---|---|---|
| cold start of each house's CLI in a scratch checkout: which startup file it opens, whether it finds NOW, preferences, LAWS, task files and the stop instruction | astra X1; anthropic X2; grok X1 (agy) | Q1, Q3, Q6 (INDEX / launch instruction; an agy stub) | a missed or ambiguous target → INDEX wording or the launch instruction; agy opens none → an agy stub |
| Qwen Code cold traversal / read-and-judge task on the corrected path | astra X2; anthropic X9 | Q2, Q3 (traversal wording, card rule) | loop or missing context → wording, not law |
| Codex CLI as the desk: launch, view/reconnect, list, message, stop, hand over | astra X3; anthropic X1 | Q1, Q5 (SEAT PROFILE per house) | a missing operation → an adapter before takeover; verbs it cannot run stay `GAP` |
| every proposed writer profile: file-tool and command-write denial, unlisted-command handling | astra X4 | Q7/L33 writer profile | a denial is evidence about that shape; unrun = unproven |
| watch semantics: absent / in-progress / stopped / changed report; notification delivery after handover; `notify_when_idle` on an idle hub | astra X5; anthropic X5 | Q5 WAIT, Q10 | a watch completing on anything but the changed last non-blank line → WAIT wording |
| Anthropic scratch successor started before / after HANDOVER lands, stale HANDOVER present | astra X6 | Q10 STEP 0 | wrong-ID adoption, concurrent write, premature stop → STEP 0 |
| same-house before/after wake-up on a frozen scenario (read manifest, meter components, bytes ÷ 4 vs the 136,059 baseline) | astra X7; anthropic X7 | Q9 | the ≈82,800 B / token relation and comparability of 136,059 |
| Codex usage counters and refresh boundary | astra X8 | Q5 MEASURE | no equivalent → no 500,000 threshold for that house |
| apply interrupted after every mutation and restored in reverse order; a restic repository holds `Memory/` and restores a file | astra X9; anthropic X6 | Q8 | a failed restore → the apply procedure; restic ok → steps 5 and 8 reversible without extra copies |
| scratch day report with concise §4 rows and linked words: run every queued prompt's authorization greps; RECONCILE grep finds exactly the pending row | astra X10; grok X5; anthropic X8 | Q10 | a failed literal / unverifiable approval → the row migration or the reader |
| scratch close with old-style, new-style and unmapped lessons | astra X11 | Q10 lessons gate | an omission not found → the gate |
| re-prove inherited harness assertions (startup auto-loading, busy/idle, orphan-child survival, allow-rule matching) under the actual CLI/version | astra X12 | Q5, Q6 | file records are precedent, not cross-vendor behaviour |
| grok sandbox: `herdr tab list`, `claude agents --json`, a background-launch flag, a context-size command | grok X2 | Q5 | a found flag replaces a GAP |
| `cmp` of the history file body (after the 3-line wrapper) against live LAWS.md | grok X3 | Q7 "lost 0" | any diff → sentences lost is not 0 |
| read `topics/memory-system.md` for the 5-pillar schema, 1536-dim, 0.3 floor, FastPathCache | grok X4 | Q6 (Hippocampus facts) | absent → a devices / memory-system line |
| card-driven `claude -p` seat with the stub CLAUDE.md, card omitting cobalt.md, asked a boundary question | anthropic X3 | Q3 BOUNDARIES card line | it opens cobalt.md unprompted → the card line is unnecessary |
| Obsidian: with `areas/cobalt.md` and `_retired/cobalt.md` both present, which file `[[cobalt]]` opens | anthropic X4 | Q2 | picks `_retired/` → rename retired files |

## OWNER ITEMS (after the tribunal)
| seat | line (verbatim) | why-no-house-can-decide named? |
|---|---|---|
| astra 1 | "Confirm that T20’s linked words appendix is part of “the day’s desk report” for L67/L73; this is interpretation of his laws, not a house-owned layout decision." | NAMED (his laws) |
| astra 2 | "Any Q7 meaning change the derive proposes to retain instead of restoring must reach him explicitly; houses cannot amend his laws by compression." | NAMED (his laws) |
| astra 3 | "The later replacement of L64’s remote-control requirement by Cobalt’s front end remains his law amendment; it is not required to apply a corrected Anthropic startup set." | NAMED (his laws; T24 says "later") |
| grok | `none` | — |
| anthropic 1 | "L58's source of law changes — his laws, and no house can pick. Live L58 (`M/LAWS.md:323`) says LAWS changes "only from the close prompt's list of that day's approved rulings". The live wake-up folds LAWS entries from any `APPROVED` §4 row at reconcile (`R/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md:17`), and the draft (`P/proposed-LAWS.md:194`) widens the law to "his approved rulings". A = keep the close-list-only clause (the desk then stops folding LAWS at wake-up); B = the draft's wording. This seat recommends B, because it matches how the desk already works." | NAMED (his laws); the tension itself is FC39 HOLDS |
Each owner line names the owner test's category (his laws) — no owner item is unnamed; none is written as a precondition to build.
RE-OPENS A RULING: none found by text. Candidate quoted for the desk (a reading, not mine): astra Q2 replaces writing-rules:20 (T20's "absence statements banned") with "Omit empty narration. Preserve required negative results, failure states, zero counts, no-change close outcomes and stop-line fields." → see ESCALATE 9.

## WRONG FACTS claimed
Each seat's WRONG FACTS with my file-check verdict (Anthropic's nine are FC44.1–9 above).
| # | seat | claim | files | verdict |
|---|---|---|---|---|
| WF-A1 | astra | "Every house pays CLAUDE.md" not established: live `.clinerules` has its own persona and no pointer | PROPOSAL.md:6; R/.clinerules:1 | HOLDS (both lines as quoted; harness auto-load is UNVERIFIABLE — astra X12) |
| WF-A2 | astra | the retired contract lacks later live additions | P-_retired-cto-desk-contract.md:40; M-contract:41, :61, :72, :120 | HOLDS (CK14/CK15) |
| WF-A3 | astra | "the build-firewall rule itself" not fully restored | PROPOSAL.md:35; P-preferences:12; working-contract:39 | HOLDS (CK39) |
| WF-A4 | astra | WAIT called vendor-free while the profile names `notify_when_idle` | PROPOSAL.md:131; P-WAKEUP:10 | HOLDS (CK9) |
| WF-A5 | astra | §4 after-size 1,600 vs 3,500 | PROPOSAL.md:38, :78 | HOLDS (CK27) |
| WF-A6 | astra | the remainder of 136,059 tokens cannot be split harness vs turns by byte division | PROPOSAL.md:78; sitting:14, :38 | UNVERIFIABLE FROM READS (PROPOSAL:78 asserts the split; a token-level run settles it: astra X7) |
| WF-A7 | astra | "every law's meaning unchanged" contradicted (writer `on-request`) | TRIBUNAL-SUMMARY.md:40; LAWS.md:193; P-LAWS:118 | HOLDS (Q7 C11) |
| WF-A8 | astra | summary says T1–T21, sitting has T1–T25 | TRIBUNAL-SUMMARY.md:3; sitting:9 | HOLDS |
| WF-A9 | astra | PROPOSAL still says the vendor A/B awaits him; T12 chose A | PROPOSAL.md:162; sitting T12 row (:114) | HOLDS |
| WF-G1 | grok | SUMMARY:3 T1–T21 vs T25 (`sitting:141`) | TRIBUNAL-SUMMARY.md:3; sitting:140 | HOLDS (the T25 row is :140 in my copy; grok cites :141) |
| WF-G2 | grok | SUMMARY:9 "wake-up file ≈301 KB → ≈83 KB" vs the wake-up file 13,102 → 6,293 B | TRIBUNAL-SUMMARY.md:9; sitting:39; SEARCHES s1 | HOLDS (CK30) |
| WF-G3 | grok | PROPOSAL:155 says the MECHANISM quote stays verbatim; P-LAWS:12–13 paraphrases it | PROPOSAL.md:155; P-LAWS:12–13 | HOLDS |
| WF-G4 | grok | PROPOSAL:37 says writing-rules is not read at every start; INDEX:13 puts it in `## start` | PROPOSAL.md:37; P-INDEX:13 | HOLDS |
| WF-G5 | grok | PROPOSAL:162 says the vendor A/B awaits him; T12 chose A (`sitting:114`) | PROPOSAL.md:162; sitting:114 | HOLDS |
| WF-G6 | grok | PROPOSAL:38 says L58/L67/L73 hold without text change; live L67/L73 say "in the day's desk report"; the draft does not | PROPOSAL.md:38; LAWS.md:369, :413; P-LAWS:229, :250 | HOLDS (CK31) |
| WF-G7 | grok | PROPOSAL:34 "14,553 → 9,051"; live 16,153, draft 9,167; INDEX given as 1,488, draft 1,679 | PROPOSAL.md:29, :34; SEARCHES s1 | HOLDS (CK28) |
Tally: astra 8 HOLDS + 1 UNVERIFIABLE; grok 7 HOLDS. Anthropic: FC44.1–9 (9 HOLDS, one sub-claim DOES NOT HOLD = FC19).

## Independence
- `grep -c -F -e "-ruling" -e "astra-ruling" -e "gemini-ruling"` on `grok-ruling.md` → 0. On `astra-ruling.md`: `grep -c -F -e "grok-ruling" -e "gemini-ruling"` → 0; `grep -c -F -e "-ruling"` → 2, both the phrase "pending-ruling verification" in its own text (not a file name) — no breach. Astra's background output (the list of everything it opened) and Grok's background output: `grep -c -F -e "astra-ruling" -e "startup-tribunal-fable"` → 0 for grok; for astra, the only hits are its own launch sentence, the instructions file text, and the day report's rows R45 (names the Anthropic report path) — it opened no ruling file and no `startup-tribunal-fable-r1-…` file. Grok wrote `grok-ruling.md` at 23:06–23:2x, before `astra-ruling.md` existed (23:09).
- CAVEAT for the desk (not a breach by the seat rule): `cto-2026-09-27.md` is a whole-file read (R40 / R42) and it carried rows R45 and R46 when copied and when Astra read the original. R46 quotes the Anthropic seat's closing line (`STARTUP FABLE R1 DONE · verdict: APPLY AFTER the derive restores 28 law sentences … law: traced 76, lost 0, moved while current 19, meaning changed 9 …`). Astra says it saw "an incidental summary of another seat’s result" and did not use it as evidence. Grok's copy contained the same rows; its ruling does not mention them.
- Gemini: no ruling, nothing to check.

## For the derive
Paths the derive reads (nothing here is a recommendation):
- this report: `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/startup-tribunal-2026-09-27.md`
- `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/startup/r1/astra-ruling.md` (complete; ends with its `TRIBUNAL R1:` line)
- `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/startup/r1/grok-ruling.md` (complete; ends with its `TRIBUNAL R1:` line)
- the Anthropic seat: `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/startup-tribunal-fable-r1-2026-09-27.md` (done at collate; claims file-checked above)
- the copied inputs and aids: `scratch/tribunal-bars-0920/startup/r1/files/`, `scratch/tribunal-bars-0920/startup/r1/SEARCHES.txt`
- no `gemini-ruling.md`, no `astra-ruling.partial.md` exist (Gemini: HARNESS).
House fields: astra `TRIBUNAL R1: APPLY AFTER restoring law meaning, refreshing snapshots, fixing traversal and report gates, and proving reversible apply` · grok `TRIBUNAL R1: APPLY AFTER the fixes named in Q1 Q2 Q3 Q6 Q7 Q8 Q9 Q10` · gemini `HARNESS` · anthropic `TRIBUNAL R1: APPLY AFTER the derive restores 28 law sentences, six contract rules, live snapshots, house profiles`.

## NEW STRINGS
None (0) as a permission string or launch rule. Command shapes run that are not spelled in `16` / `24`: (1) the Grok command's tail `-p "<sentence>"` — `16` names `04`'s §2 spelling, which does not print the `-p` tail; I copied the shape `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "…"` from `prompts/2026-09-25/06-drc-d4-check.md` (an approved prompt with the same allow string); (2) `grep -c -v -x -F -f <original> <copy>` and `grep -n -x -F -f`, `grep -o -m …`, `grep -r -c …` — all `grep *`; (3) `ls`, `wc`, `date`, `git log` as allowed. Two commands were mistyped and did nothing harmful (`wc -c` of a nonexistent path; a `grep` with `/Users/cobalt-wt/…` for `.clinerules`, re-run correctly); one `grep … --include` failed under the shell's glob. No `mkdir`, no git write, no vault write, no memory-folder write.

## L74
One record: a block appended after the Read result of `55-startup-tribunal.md` asked for a `Claude-Session: …` line in commit messages / PR bodies and named a file-send tool. It is data, not followed; this hub commits nothing.

## ESCALATE
1. ASK DESK: gemini did not rule round 1 (verbatim: `jetski: no output produced — a tool required the "command" permission that headless mode cannot prompt for, so it was auto-denied. Add an allow-rule under permissions.allow in settings.json (e.g. command(<target>)). Alternatively, re-run with --dangerously-skip-permissions to auto-approve all tools.`) — relaunch this same file (it re-asks only the houses with no ruling file), or take the derive with the seats that ruled? [23:29] Safe default taken: no retry by me. No file-read failure is SHOWN (it is a shell-command denial), so R41's ordered-parts relaunch does not apply.
2. astra's probe row: `astra: UP` at 22:27 (`OK`, exit 0); Astra ruled all ten items in 12.7 min, 230,214 tokens, no METER.
3. DOES NOT HOLD verdicts whose supporting claims HOLD in my file-check (10 verdicts): astra Q2, Q6, Q7, Q8, Q9, Q10; anthropic Q1, Q6, Q7, Q8 — each rests on rows above marked HOLDS (CK1–CK5, CK13–CK15, CK19, CK25–CK27, CK31–CK35; Q7 case table).
4. Q7: every case listed by the three seats HOLDS as a TEXT difference (live sentence present at its live line, absent from `proposed-LAWS.md`; 48 verdict instances in the case table + FC42/FC43). The seats' COUNTS disagree (moved 11 / 10 / 19, changed 23 / 5 / 9) and grok's count line does not reproduce from its own list (10 + 5 = 15; 13 lines listed). Classification (current law vs history; meaning changed) is theirs; a disagreement about law text is an OPEN item for him, never a vote (L39).
5. Anthropic-seat claims that DOES NOT HOLD: FC19 ("131 lines" — 130), FC21 ("only the history file" — no file holds the phrase), FC24 (prompt `39-stack-seam-build.md:137` does not contain "the CLAUDE.md rule"). Its other claims HOLD or are UNVERIFIABLE (FC9, FC11, FC17, FC29) or arithmetic (5).
6. Numbers a seat proposed without a measurement, quoted: anthropic Q9 "the prediction ≈81,500 tokens (136,059 − 54,600) … more than 10% over → ESCALATE" (the 10% threshold has no measurement; grok Q9's item 18 sets none); grok Q2(6) "if this session is larger than the wake-up size you logged in your first §5 MEASURE row" (no number; a comparison to a logged one).
7. Owner items: none unnamed; none a precondition. (Table above.)
8. No `RE-OPENS A RULING` by text; see 9.
9. ASK DESK: astra Q2 would replace writing-rules:20 ("Never state an absence …") with "Omit empty narration. Preserve required negative results, failure states, zero counts, no-change close outcomes and stop-line fields." — T20 (sitting:130) banned "absence statements". Does the desk read that as RE-OPENING T20, or as a wording that keeps T20 while preserving required evidence (astra CK5)? [23:29] Safe default: quoted, not folded.
10. Independence caveat (Independence section): R45 / R46 in the day report exposed the Anthropic seat's closing verdict to any house reading the whole file (R40 / R42); astra disclosed it; grok's copy carried it. ASK DESK: does the derive treat astra / grok as independent for round 1? [23:29] Safe default: yes (no ruling file opened), caveat recorded.
11. Deviations from `55` disclosed: (a) the secrets grep ran as ONE recursive `grep -r -c` listing every file instead of one call per file (same command shape, same counts); (b) an extra line-set check on every copy (`grep -c -v -x -F -f`), which found and fixed one equal-length typo before launch; (c) `.clinerules` copy is 2 B short (two trailing-whitespace lines stripped by the Write tool); (d) SEARCHES.txt was rewritten once to spell paths in full after a first draft abbreviated them (the launched houses read the final version — it was final at 22:54, before the 22:55 launches); (e) the desk report `cto-2026-09-27.md` was 61,446 B at the drafter's measure and 62,165 B when copied.
12. No seat was SHOWN to fail on reading (astra: "truncated outputs recovered through subsequent ranges"); no R41 / R42 ordered-parts relaunch is asked.

STARTUP TRIBUNAL DONE · round: 1 · astra: TRIBUNAL R1: APPLY AFTER restoring law meaning, refreshing snapshots, fixing traversal and report gates, and proving reversible apply · grok: TRIBUNAL R1: APPLY AFTER the fixes named in Q1 Q2 Q3 Q6 Q7 Q8 Q9 Q10 · gemini: HARNESS · anthropic: TRIBUNAL R1: APPLY AFTER the derive restores 28 law sentences, six contract rules, live snapshots, house profiles · houses that ruled: 3 · questions settled: 1 of 10 · findings that HOLD: 164 · dissents: 10 · ESCALATE: 12
