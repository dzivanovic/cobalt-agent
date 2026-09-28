BLIND: I did not read the houses' folder or the hub's report.
RUN DATE: Sun Sep 27 22:26:26 EDT 2026

## DIGEST FOR THE DESK

TRIBUNAL R1: APPLY AFTER the derive restores 28 law sentences, six contract rules, live snapshots, house profiles
- Q1 DOES NOT HOLD — SEAT PROFILE is Anthropic-only; a Codex desk has no LIST idle/busy, own id, MESSAGE or MEASURE. Derive adds per-house blocks from Q5.
- Q2 HOLDS WITH — INDEX links resolve by bare name to 3–4 same-named files (`_imports/`, `_retired/`); give the path rule. Also: writing-rules moves to retrieve; fix the "How to read this file" pointer.
- Q3 HOLDS WITH — boundaries leave the auto-loaded CLAUDE.md; every card names cobalt "What Cobalt is" + "Build rules" (UNATTENDED-LAUNCH §2).
- Q4 HOLDS — the shape is right; every defect is a line, a source or a path.
- Q5 HOLDS WITH — the profile matches the live file except `herdr tab list` (VIEW); writing-rules' "vendor commands only in the profile" needs its two stated exceptions.
- Q6 DOES NOT HOLD — six live contract rules (L17, C5, K19 tail, K20, K21, R40/R42 line) are in neither the draft nor its stale snapshot. Five CLAUDE.md/cobalt.md facts are lost. working-contract:40 keeps the old wake path.
- Q8 DOES NOT HOLD — the contract snapshot is stale (14,731 vs live 16,153 B); INDEX and cobalt.md replacements have no whole snapshot (vault not git). Snapshot from live at apply; add steps 12a/12b; no LAUNCH during apply.
- Q9 HOLDS WITH — 301,337 re-sums exactly; 82,800 is a one-quiet-day model (several drafts grew since); step 18 logs the prediction ≈81,500 tokens plus the day's conditions.
- Q10 HOLDS WITH — his words in the words file: define it as part of the day's desk report and restore that phrase in L67/L73. SESSION-CLOSE step 2 must carry his words and time (L58). Authorization gates read the words file.
- Q7 DOES NOT HOLD — nothing lost; FROZEN verbatim. 19 current sentences moved to history, 9 meanings changed; each has its restore line.
Law trace: L1–L76 traced 76 · lost 0 · moved while current 19 · meaning changed 9.
Experiments: X1–X9 (Codex desk verbs; CLI auto-load; card seat follows pointer; Obsidian duplicate names; notify_when_idle; restic restore; tokenizer; reconcile grep; Qwen traversal).
Owner: 1 — L58's source of law changes, close list only (A) or any approved ruling (B, recommended).
WITHDRAWN: 3. ESCALATE: 0. WRONG FACTS: 9.

## Rulings

P = `docs/40 - DevDocs/plans/startup-redesign-2026-09-27/` · M = `/Users/cobalt/Vault/Think/6 - Permanent/Memory/` · R = `/Users/cobalt/cobalt/`.

### ITEM Q1 — another house takes over the desk from these files alone
DOES NOT HOLD — `P/proposed-CTO-DESK-WAKEUP.md:5-11` (the SEAT PROFILE is Anthropic-only — the proposer says so, `P/PROPOSAL.md:130` "The SEAT PROFILE exists only for Anthropic"; three of its verbs are Claude Code tools in this session's own tool list; what a Codex session has instead is X1). Scenario: a Codex (Sol) session is launched on the wake-up file at a crash. STEP 0.2 (`:15`) "When LIST shows `<p>` idle or absent: STOP it" — LIST = `claude agents --json` + `ListAgents` (`:9`); `ListAgents` is a Claude Code tool, so it cannot tell idle from busy and cannot end the predecessor safely; STEP 0.3 (`:16`) "Your id = LIST's background row with cwd `~/cobalt`" — a Codex session is not in `claude agents`, so it has no id to record in §5 or to name in HANDOVER; REFRESH `:35` MEASURE reads a Claude transcript (`desk-context.sh`), so it never gets a refresh signal; READ 7 (`:28`) answers `ASK DESK` by MESSAGE = `SendMessage`, which it does not have. It cannot "continue as if nothing changed". The memory traversal itself does carry over (stub → `cobalt.md` → INDEX → LAWS), apart from Q2's path defect.
Wording that makes it hold (`P/proposed-CTO-DESK-WAKEUP.md`, after `:11`): `A desk of another house runs on its own SEAT PROFILE block, same seven verbs, each a command or "GAP → <fallback>"; the MODEL line names which block binds. Blocks for OpenAI, xAI and Google come from the tribunal's Q5 tables; a house with no block cannot be seated as the desk.` The derive writes the blocks from the houses' Q5 tables (that is T11's option A completed, not reopened). The local Qwen: L49 (FROZEN) forbids composing — a Qwen desk cannot write prompts, rows or NOW — so Qwen is out of the desk seat by law, not by these files; say so in the same block.

### ITEM Q2 — every start-path line has one correct reading
HOLDS WITH — replace `P/proposed-cobalt.md:7` with `- Read \`## NOW\`, then \`/Users/cobalt/Vault/Think/6 - Permanent/Memory/INDEX.md\`.` and replace `P/proposed-INDEX.md:7-13` with:
```
## start — read in this order (a link [[x]] = x.md in this folder, areas/ or topics/ — never _imports/ or _retired/)
- [[cobalt]] — you came from here; read its sections below NOW (build rules)
- [[preferences]] — how he works with agents
- [[profile]] — who he is
- [[LAWS]] — current law; in full unless your prompt gives you a card (L59)
- [[cto-desk-contract]] — the desk only
## retrieve when the task asks
- [[writing-rules]] — before writing or amending any read-path file
```
(and drop the old `[[writing-rules]]` line). Scenario (the defect): a Qwen or Grok seat resolves `[[preferences]]` by file name with its shell; M holds three files of that name today (`M/preferences.md`, `M/_imports/anthropic-2026-09-05/preferences.md`, `M/_imports/anthropic-2026-09-15/preferences.md`) and apply step 2 adds a fourth (`M/_retired/preferences.md`); the same happens to `[[cobalt]]` (`areas/`, `_retired/`), `[[cto-desk-contract]]` (`topics/`, `_retired/`), `[[devices]]`, `[[cobalt-houses]]`, `[[cobalt-sprints]]` (live + `_imports/`). Only hop 1 carries an absolute path (the stub `P/proposed-CLAUDE.md:3`, or the desk's READ 1 `P/proposed-CTO-DESK-WAKEUP.md:22`); from hop 2 on, every link is a bare name. The live AGENTS.md / QWEN.md gave absolute paths for INDEX, NOW and LAWS (`R/AGENTS.md:5`) — the draft loses that. Second defect: `P/proposed-INDEX.md:7` lists `[[cobalt]]` (already open — a loop for a literal reader) and `:13` lists `[[writing-rules]]` under "start — read in this order" while `P/PROPOSAL.md:37` says "read before writing, not at every start": two readings. Price: INDEX +≈60 B net (always-loaded 3,295 → ≈3,355 B, under 4,000; `wc -m` to confirm chars), cobalt.md +≈45 B, wake-up −3,209 B that a literal reader would otherwise read at start. Third defect: `P/proposed-CTO-DESK-WAKEUP.md:27` applies a LAWS entry "per LAWS \"How to read this file\"", a section `P/proposed-LAWS.md:5` renames `## Reading` (grep: the phrase survives only in the history snapshot) → `:27` "LAWS entry (per LAWS \`## Reading\` and L58)". Minor, left to the derive: `P/proposed-SESSION-CLOSE.md:13` "Over = the close FAILS: trim preferences" — runner `hub measures`, but a trim is a memory write (desk only, L58); `P/proposed-CTO-DESK-WAKEUP.md:32` gives no status for a ruling of his that folds nothing and launches nothing (use `RECORD`).

### ITEM Q3 — the memory structure for all of Cobalt, many houses, Qwen included
HOLDS WITH — add to `P/proposed-UNATTENDED-LAUNCH.md` §2, after the AUTHORIZATION paragraph (`:11`): `BOUNDARIES: every card names [[cobalt]] "What Cobalt is" and "Build rules" as binding for the run, whatever else the card holds.` Reason: today every Claude session gets the absolute boundaries (never touch a trading platform, never commit vault content or secrets, quote the source of every figure) because the harness puts `R/CLAUDE.md` in its context (`R/CLAUDE.md` "Absolute boundaries"). After step 15 it gets a one-line pointer (`P/proposed-CLAUDE.md:3`). A card seat (L59: the card is the working set) — e.g. a `claude -p` checker whose card lists a diff and a report — is not told to open `cobalt.md`; whether it follows the stub's pointer unprompted is X3, unrun. The card line makes the boundaries reach every seat without putting anything back into the startup files (T3/T4 intact). Price: ≈150 B in UNATTENDED-LAUNCH (not a wake-up read), ≈60 B per prompt card. The rest of the structure — one stub per house, one area file, INDEX as map, laws in one file, history outside the read path — is the right shape for many houses and holds; Qwen's path (`P/proposed-QWEN.md:3` → cobalt → INDEX → its card) is ≈10k tokens of LAWS at most, inside its 262,144 context.

### ITEM Q4 — is this the right way
HOLDS — pointer stubs, one area file, INDEX as the map, laws-only LAWS with the verbatim history kept, one home per fact and move-to-history are each the smallest mechanism that meets his T2–T5/T17/T20; I found no simpler one and no failing sequence against the shape itself. Every defect I found is a missing line, a stale source or a wrong path (Q2, Q3, Q6, Q8, Q10), not the design. I considered renaming `_retired/<file>.md` to avoid basename collisions and withdrew it: Q2's one INDEX line fixes resolution for every house at ≈60 B and touches no law text; Obsidian's own link resolution with duplicate basenames is X4.

### ITEM Q5 — the desk on Anthropic tooling; the SEAT PROFILE vs the live wake-up and contract
HOLDS WITH — `P/proposed-CTO-DESK-WAKEUP.md:8` becomes: `- VIEW: \`herdr tab list\` (find the "CTO" tab); \`herdr tab create --workspace w2 --cwd /Users/cobalt/cobalt --label "CTO" --no-focus\`, then \`herdr pane run <pane> "claude attach <id>"\`; alive = \`pgrep -fl "claude attach <id>"\``.

| verb | Anthropic command (live file, line) | in the draft profile? | GAP? | UNPROVEN? (L70) |
|---|---|---|---|---|
| LAUNCH | `cd ~/cobalt` then `claude --bg "Read 'docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md' and follow it exactly." --model claude-opus-5-5 --permission-mode auto --remote-control cto-desk --allowedTools "Bash(git *)" "Edit" "Write" "Bash(python3 *)" --disallowedTools "AskUserQuestion" "EnterWorktree" --add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt-wt` (`R/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md:1`) | yes, byte-identical (`grep -c -F` of the draft's string in the live file = 1) | no | in live use; not run by this seat |
| VIEW | `herdr tab create … --label "CTO" --no-focus`; `herdr pane run <pane> "claude attach <id>"`; `pgrep -fl "claude attach <s>"`; **`herdr tab list`** (live `:5`) | first three yes; `herdr tab list` NO | yes — STEP 0.4 (`:17`) "re-attach … close any other desk tab" and REFRESH (5) need the tab list; no verb gives it | in live use |
| LIST | `claude agents --json` (+ `--all`), `ListAgents` (live `:5`, `:16`) | yes | no | in live use |
| STOP | `claude stop <id>` (live `:5`); pane predecessor left alone (live `:5`) | yes (`:10`, `:15`) | no | in live use |
| MESSAGE | `SendMessage` (live `:16`) | yes | no | tool present in this session; not sent |
| WAIT | `notify_when_idle` (live `:16`) | yes | no — but the frame's WAIT (stop line) is `M/topics/cto-desk-contract.md` W1 `wait-stop-line.sh` (exists: `ls /Users/cobalt/.claude/ops`), which the wake-up's WATCHES line (`:39`) never names | `notify_when_idle` is a name in the files; X5 |
| MEASURE | `sh /Users/cobalt/.claude/ops/desk-context.sh <own id> 500000` (live `:28`) | yes | no | script exists; not run |

Profile commands the live file does not prove: none — every profile command appears in the live wake-up. Live commands the profile does not carry: `herdr tab list` only. Vendor literals left outside the profile although `P/proposed-writing-rules.md:16` says "Vendor commands live only in a SEAT PROFILE": `P/proposed-UNATTENDED-LAUNCH.md:7` (`claude --bg`), `:25` (`claude -p`, `pgrep -fl "claude --model"`), `P/proposed-cto-desk-contract.md:62` (`Bash(claude stop *)`). The proposal keeps the hub-side template literal on purpose (`P/PROPOSAL.md:42`); the writing rule should say so: `P/proposed-writing-rules.md:16` → `- Vendor commands live in a SEAT PROFILE; steps name the verb. Exceptions: a launch template and a fact about one vendor's CLI.`

### ITEM Q6 — no lobotomy
DOES NOT HOLD — facts a house reads today that the new path no longer reaches in ≤2 hops (some not even in a history file):
1. Desk — `P/proposed-cto-desk-contract.md` (whole) lacks six rules of the LIVE contract, and the snapshot that should keep them (`P/proposed-_retired-cto-desk-contract.md`, 14,731 B, 125 lines, taken ≈20:35) lacks them too — the live file is 16,153 B, 131 lines: `M/topics/cto-desk-contract.md:41` (R40/R42 — precedent-shape drafters on Sonnet 5; one instructions file + the files, each seat reads them; ordered parts only after a shown read failure), `:61` L17 (every helper is a `--bg` session with rc + tab + L34 row; the in-process Agent tool is never used for work; mechanical helpers on Sonnet), `:72` C5 (push = the bare `git push origin main` alone in its call), `:119` K19's tail (every smoke-row path under the launch line's `--add-dir`), `:120` K20 (non-trading-day deploy timing; residents-down never crosses 20:20:00–20:34:59), `:121` K21 (read the plist's `StartCalendarInterval` before pointing a smoke look). Proof: `grep -n -e "L17 Every helper" -e "K20 " -e "K21 " -e "C5 Push" -e "NO PACKETS"` on the snapshot → no output. Scenario: step 9 at apply; the next desk launches a survey helper with the Agent tool (L17 gone) or pushes in a compound call (C5 gone) — both lessons re-learned.
2. Every house — `R/CLAUDE.md:10` / `R/AGENTS.md:7` "If required law is missing, unreadable, or contradictory, report the exact path and unresolved issue; do not substitute a stale copy or invent a resolution" is in no draft (`grep -rn -F "stale copy"` over P → only the history file). Scenario: a Codex hub finds LAWS unreadable mid-sync; nothing on its path forbids reading `_imports/…` or LAWS-HISTORY as law.
3. Builders — `R/CLAUDE.md:276` "DevDocs prose stays agent-authored; the symbol-check gate is the acceptance test, not a generator" — prompts cite it as "the CLAUDE.md rule" (`R/docs/40 - DevDocs/prompts/2026-09-25/36-drc-d2-fix-r1-build.md:111`, `…/39-stack-seam-build.md:137`); `P/proposed-cobalt.md:21` keeps only "DevDocs per .py". `R/CLAUDE.md:51` "Keep the backlog and kanban board updated as you work" — cobalt.md lists BACKLOG as a source only (`:16`). `R/CLAUDE.md:212` "Verify with `git check-ignore`/a quick glob check before adding" a new-core config file — dropped at `P/proposed-cobalt.md:37`.
4. `M/areas/cobalt.md:12` "the two import files carry the full chat-side history 08-21 → 09-05 …; consult them for the reasoning behind a Ledger line, never as a second source of truth" — in neither `P/proposed-cobalt.md` nor `P/proposed-_retired-cobalt.md` (grep: live `:12` only). Deleted, against T5.
5. Stale wake path left reachable: `M/topics/working-contract.md:40` "every house wakes via CLAUDE.md / AGENTS.md / QWEN.md → INDEX → `## NOW` → LAWS" — no apply item touches it (item 12 fixes only `M/areas/cobalt-houses.md:26`). A house retrieving [[working-contract]] (INDEX `retrieve`) reads a second, contradicting start path.
Wording that makes it hold: (a) derive `F/cto-desk-contract.md` from the LIVE contract at apply time, carrying the six rules in the draft's style (`- L17 Every helper — a survey included — is a background session with rc, tab and an L34 row; never the in-process Agent tool; mechanical helpers on Sonnet.` · `- C5 Push = the bare \`git push origin main\` (or \`… deploy-<tag>\`) alone in its call, from \`~/cobalt\`.` · K19 + `every path a smoke row reads sits under the launch line's \`--add-dir\`` · `- K20 A non-trading day with no scanning session: the deploy phase may run once the gate is green; residents-down never crosses 20:20:00–20:34:59.` · `- K21 Before pointing a smoke look or live proof at a day, read the job's plist \`StartCalendarInterval\`.` · Seats line + `A drafter copying an established precedent shape runs on Sonnet 5. Every tribunal seat reads one instructions file and the files itself; ordered parts only after a shown read failure.`); (b) `P/proposed-cobalt.md` `## Working rules` += `- If a law is missing, unreadable or contradictory: report the path and the issue; never substitute a stale copy.` and `- DevDocs prose is agent-written; the symbol-check gate accepts it, never generates it.`; `## Build rules` line 3 += ` Keep \`docs/00 - Project/BACKLOG.md\` current.`; `## Strangler rebuild` line 2 += ` Check with \`git check-ignore\` before adding one.`; `## Sources` += ` \`_imports/\`: chat history 08-21 → 09-05 — reasons behind a Ledger line, never a source of truth.` (≈330 B on the start path); (c) new apply item 12a: move `M/topics/working-contract.md:40`'s wake-path clause to `M/_retired/working-contract.md`, the line kept without it. Everything else I walked holds: stub → cobalt → INDEX start set reaches preferences and profile for every house (a gain — `P/PROPOSAL.md:29`), `topics/devices.md` gets the services line (item 10), the D6 tiers sit in `P/proposed-cobalt.md:40` `## Docs tree` and PLACEMENT points there after item 13 (PLACEMENT itself keeps "never in a new ad-hoc folder" `R/docs/PLACEMENT.md:6` and the `_inflight` rule `:28`), `R/docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md:9` carries the Qwen morning command.

### ITEM Q8 — the 19 apply items
DOES NOT HOLD — `R/docs/40 - DevDocs/reports/desk-startup-tuning-2026-09-27.md:167-171`. (i) Stale sources: step 2 writes `P/proposed-_retired-cto-desk-contract.md` (14,731 B, ≈20:35) as the whole-file snapshot of a live file now 16,153 B (Q6-1) — measured by `wc -c` this session; step 1 appends a LAWS snapshot taken 20:45 (proven identical to live LAWS today: every non-blank live line is in it, `grep -v -x -F -f`, and 456 = 453 + 3 lines) that goes stale the moment a close folds a ruling before apply; step 4's source was drafted from that snapshot. (ii) Not reversible from what exists at its moment (the vault is not git): step 5 replaces `M/INDEX.md` whole and no step keeps a copy of it; step 8 replaces `M/areas/cobalt.md` whole and `M/_retired/cobalt.md` holds only the moved lines — the kept lines' old wording and the NOW at apply are not recoverable byte-exact. Restic (`M/topics/cto-desk-contract.md:123` "restic restores") is X6, unproven here. (iii) Missing items: `M/topics/working-contract.md:40` (Q6-5); `M/topics/devices.md:31` "(CLAUDE.md boundary unchanged)" points at a boundary that step 15 moves out of CLAUDE.md. (iv) Order is right (history first, wake-up last, no deploy), but nothing forbids a hub LAUNCH between step 4 (new LAWS preamble path) and step 15 (stubs): a session starting then reads the old CLAUDE.md → old INDEX order against a new LAWS.
Wording that makes it hold, `## FOR THE DESK`: step 1 → `History first — append the header + the LIVE \`M/LAWS.md\` as it is now (re-prove: every non-blank line matched, line count = live + 3) → end of \`M/LAWS-HISTORY.md\`; a live line that is not in \`P/proposed-_history-LAWS-2026-09-27.md\` stops the apply (the derive re-drafts LAWS).` · step 2 → `Create \`M/_retired/\`; write, each taken from the LIVE file now: \`_retired/cto-desk-contract.md\`, \`_retired/preferences.md\`, \`_retired/INDEX.md\`, \`_retired/cobalt.md\` (the whole live file, then the draft's moved-lines blocks)` · new step 12a (Q6-5) and 12b `M/topics/devices.md:31` "(CLAUDE.md boundary unchanged)" → "(Cobalt never touches a platform — [[cobalt]])" · the GATE line += `No LAUNCH from step 1 to step 17.` Reverts: 1 = truncate LAWS-HISTORY to its recorded before-size; 2 = remove `_retired/`; 3 = remove the archive folder; 4–9 = copy back from `_retired/` (INDEX, cobalt, contract, preferences) or from the step-1 snapshot (LAWS); 7 = delete the new file; 10–12b = remove the appended line / restore the moved line; 13–16 = `git checkout -- <path>` before step 17, `git revert <sha>` after; 17 = `git revert`; 18 = none (read).

### ITEM Q9 — the measure
HOLDS WITH — `R/docs/40 - DevDocs/reports/desk-startup-tuning-2026-09-27.md:184` step 18 becomes: `Verify: the successor's first §5 row logs its MEASURE, the prediction ≈81,500 tokens (136,059 − 54,600) and the day's conditions — live hubs read, pending rows, day-open present; more than 10% over → ESCALATE with the per-file wc -c.`
Re-derivation: "before" = the sum of the sitting's Measure rows 1–20 (`:18-37`): 85,956 + 89,839 + 20,874 + 19,443 + 16,590 + 14,553 + 13,102 + 9,949 + 7,860 + 5,800 + 4,011 + 3,392 + 1,902 + 1,912 + 1,655 + 1,456 + 1,417 + 665 + 561 + 400 = **301,337** — exact, but rows 10 (~5,800, "none today") and 20 (~400) are estimates, row 5 (CLAUDE.md 16,590) is the harness auto-load ("not a desk step", `:22`), and rows 1/3 are the old reconcile's grep output for two specific days. "After" = `P/PROPOSAL.md:75` 109,156 − 15,943 (§4 rows, est.) − 5,059 (day-open) − 6,039 (one hub read) + 492 + 180 = **82,787 ≈ 82,800** — the arithmetic holds; its terms do not all match the drafts as they now are (`wc -c` this session): wake-up 6,293 (table 5,585 / 6,241), contract 9,167 (9,051), LAWS 40,617 (40,588), INDEX 1,679 (1,488), writing-rules 3,209 (2,782, and read at start by a literal reader — Q2); the §4 after-figure is 3,500 at `P/PROPOSAL.md:78` but ≈1,600 at `:38`; reconcile ≈0 holds only on a day with 0 pending rows; hub reads scale with live hubs. Estimated rows: §4 rows, day-open, hub reads, ladder slice (≈6,380), reconcile. So 82,800 B is a model of one quiet day, ±≈5 KB on the drafts as written, not a measurement. Whether bytes ÷ 4 approximates this tokenizer, and how much of 136,059 is harness, is X7. The step-18 measure tests the total only if the day's conditions are logged beside it.

### ITEM Q10 — the desk's own routine
HOLDS WITH — HANDOVER (`P/proposed-CTO-DESK-WAKEUP.md:36` (6)), STEP 0, the R98 MEASURE (`:35`) and the close's runner split (`P/proposed-SESSION-CLOSE.md`, matches L58's 2026-09-22 C2 clause) hold. Three breaks, each with wording:
1. His words leave the §4 row for `reports/cto-<date>-words.md` (`P/proposed-CTO-DESK-WAKEUP.md:32`), but LIVE L67 OVERRIDE and L73 say the override is recorded "with his words and the time in the day's desk report" (`M/LAWS.md:369`, `:412`, `:413`), and `P/proposed-LAWS.md:229` / `:250` silently drop "in the day's desk report" — a text change the proposal says is not needed (`P/TRIBUNAL-SUMMARY.md:38`, WRONG FACTS 3). L7 (`M/LAWS.md:57` "logs it with the time in `reports/cto-<date>.md` §4") holds — the row has the time. Wording: `P/proposed-writing-rules.md:10` += ` \`cto-<date>-words.md\` is part of the day's desk report.`; restore `P/proposed-LAWS.md:229` "the desk records his words and time in the day's desk report" and `:250` "each override is recorded in the day's desk report (his words, the time)". Then no law text changes and T20 stands as ruled.
2. L58 (live `M/LAWS.md:323` and `P/proposed-LAWS.md:194`) requires every fold candidate to carry "his words, the time and the exact fold text"; `P/proposed-SESSION-CLOSE.md:8` asks the close hub only for "the exact fold text and its `R<n>`". Scenario: the 99-close hub on the first day after apply follows the draft and lists candidates without his words or times — a close list that no longer meets L58, which the desk then folds at wake-up as "his rulings already given" (`:27`) with only a row number to go on. Wording: `:8` "… with his words (from `cto-<date>-words.md`), the time, the exact fold text and its `R<n>`."
3. Authorization gates grep his words IN the §4 row today — this prompt does (`grep -n "^| R109 "` must carry "Make all Opus 5.5 for now"), and R40 puts precedent-shape drafters on Sonnet, who copy that shape. After apply a new row carries no words; the copied gate counts 0 and the run stops `FAILED: authorization mismatch`. `P/proposed-UNATTENDED-LAUNCH.md:11` already drops "his words" from the AUTHORIZATION block; say where they are: `:11` "(`reports/cto-<date>.md` §4 row numbers, the time; his words, when a gate quotes them, from \`cto-<date>-words.md\` \`^R<n> \`)". The RECONCILE grep (`:27`) and step 0 of the apply list together find every pending row from the apply date on; the one-time step 0 covers the old statuses (`APPROVED — launch row`, `APPROVED — drafter …`).

### ITEM Q7 — law preservation (full trace under `## Law trace`)
DOES NOT HOLD — `L1–L76 traced: 76 · sentences lost: 0 · current law moved to history: 19 · meaning changed: 9`. Nothing is lost (the history snapshot carries every non-blank live line), and the FROZEN routing laws are verbatim. But 19 current law-text sentences sit only in history and 9 changed meaning without a T-ruling. Scenario: after step 4, the desk folds a close whose hub listed no runner and wrote nothing for a no-change close. Nothing in LAWS now requires either (MOVED 13, 15). A later hub reads FROZEN L29's "two parties, ≤3 rounds" (`P/proposed-LAWS.md:105`) with no L67 sentence saying what it becomes (MOVED 19), and seats two houses on a design. L17's privacy default reads as opt-in (MEANING 2). L67/L73 no longer say where an override is recorded (MEANING 7, 9). Wording that makes it hold: each restore line under `## Law trace` (MOVED 1–20 except 6, MEANING 1–9), pasted into `P/proposed-LAWS.md` at the line named. That is ≈1.4 KB on LAWS, still ≈49 KB under the live file. MEANING 6 (L58's source of law changes) is restored to the live clause, and the tension the draft tried to fix goes to OWNER 1. The T18 rewordings (L6, L36, L50, L75), the T3 preamble path and T7/T9 in L58 carry his stated meaning.

## Law trace

Method: every entry of the live `M/LAWS.md` (453 lines; `grep -n "^### L"` map) read side by side with `P/proposed-LAWS.md` (259 lines), both whole in this session; disputed sentences confirmed by `grep -n -F` (READING). Classification by the live file's own rule (`M/LAWS.md:15`): `— ` lines = citation; `Status note` / `State (not law)` = state; everything else = law text. Amendment tags `[amended …]`, ratification/applied-by paragraphs and verbatim quotes of his words are moved by T17 (his: "any citations, dates, and wording need to move into a history file"). Sentence counts are mine, ± a clause. "K" includes rationale-only sentences cut under T5/T17 ("no word that does not need to be there") — listed after the table, not findings.
History snapshot = the live file: `wc -c` 90,209 vs 89,839 (+370 B = the 3-line header, `P/proposed-_history-LAWS-2026-09-27.md:1-3`); `grep -c ""` 456 vs 453; `grep -v -x -F -f live snapshot`-style check both ways: every non-blank live line is in the snapshot (the only unmatched live lines printed were blank lines). So LOST = 0 by construction, provided apply step 1 appends it; every dropped sentence below is in history — the question is whether it was still current.
FROZEN (L5, L21–L27, L29, L49): proposed lines :28, :75, :81, :84, :87, :91, :104, :166 are byte-identical to live lines (`grep -n -x -F -f`); :78 (L22), :88 (L25 ¶2), :94 (L27), :105–:106 (L29 ¶2–3), :167 (L49 ¶2) are live text with only the tag / citation removed (`grep -c -F` of each draft sentence in live = 1). Frozen: 0 changed.

| entry | law-text sentences | KEPT | REWORDED (whose) | LOST | MOVED WHILE CURRENT | MEANING CHANGED |
|---|---|---|---|---|---|---|
| Header | 1 | 1 | 0 | 0 | 0 | 0 |
| How to read | 13 | 6 | 2 (T17: entry shape/tags; what-binds rule moot) | 0 | 5 | 0 |
| Preamble | 8 | 7 | 1 (T3 wake path) | 0 | 0 | 0 |
| L1 | 4 | 4 | 0 | 0 | 0 | 0 |
| L2 | 2 | 2 | 0 | 0 | 0 | 0 |
| L3 | 2 | 2 | 0 | 0 | 0 | 0 |
| L4 | 6 | 6 | 0 | 0 | 0 | 0 |
| L5 FROZEN | 1 | 1 | 0 | 0 | 0 | 0 |
| L6 | 2 | 0 | 2 (T18) | 0 | 0 | 0 |
| L7 | 6 | 6 | 0 | 0 | 0 | 0 |
| L8 | 5 | 5 | 0 | 0 | 0 | 0 |
| L9 | 3 | 3 | 0 | 0 | 0 | 0 |
| L10 | 2 | 2 | 0 | 0 | 0 | 0 |
| L11 | 4 | 4 | 0 | 0 | 0 | 0 |
| L12 (retired) | 2 | 2 | 0 | 0 | 0 | 0 |
| L13 | 2 | 1 | 0 | 0 | 0 | 1 |
| L14 | 3 | 3 | 0 | 0 | 0 | 0 |
| L15 | 5 | 5 | 0 | 0 | 0 | 0 |
| L16 | 5 | 5 | 0 | 0 | 0 | 0 |
| L17 | 14 | 13 | 0 | 0 | 0 | 1 |
| L18 | 3 | 3 | 0 | 0 | 0 | 0 |
| L19 | 4 | 3 | 0 | 0 | 1 | 0 |
| L20 | 1 | 0 | 0 | 0 | 0 | 1 |
| L21 FROZEN | 2 | 2 | 0 | 0 | 0 | 0 |
| L22 FROZEN | 6 | 6 | 0 | 0 | 0 | 0 |
| L23 FROZEN | 3 | 3 | 0 | 0 | 0 | 0 |
| L24 FROZEN | 2 | 2 | 0 | 0 | 0 | 0 |
| L25 FROZEN | 11 | 11 | 0 | 0 | 0 | 0 |
| L26 FROZEN | 2 | 2 | 0 | 0 | 0 | 0 |
| L27 FROZEN | 7 | 7 | 0 | 0 | 0 | 0 |
| L28 | 20 | 19 | 0 | 0 | 1 | 0 |
| L29 FROZEN | 13 | 13 | 0 | 0 | 0 | 0 |
| L30 | 2 | 2 | 0 | 0 | 0 | 0 |
| L31 | 4 | 3 | 0 | 0 | 0 | 1 |
| L32 | 9 | 9 | 0 | 0 | 0 | 0 |
| L33 | 7 | 5 | 0 | 0 | 2 | 0 |
| L34 | 3 | 2 | 0 | 0 | 1 | 0 |
| L35 | 3 | 3 | 0 | 0 | 0 | 0 |
| L36 | 2 | 0 | 2 (T18) | 0 | 0 | 0 |
| L37 | 6 | 6 | 0 | 0 | 0 | 0 |
| L38 | 3 | 3 | 0 | 0 | 0 | 0 |
| L39 | 5 | 5 | 0 | 0 | 0 | 0 |
| L40 | 1 | 1 | 0 | 0 | 0 | 0 |
| L41 | 5 | 5 | 0 | 0 | 0 | 0 |
| L42 | 5 | 5 | 0 | 0 | 0 | 0 |
| L43 | 7 | 7 | 0 | 0 | 0 | 0 |
| L44 | 3 | 3 | 0 | 0 | 0 | 0 |
| L45 | 5 | 4 | 0 | 0 | 1 | 0 |
| L46 | 7 | 7 | 0 | 0 | 0 | 0 |
| L47 | 5 | 5 | 0 | 0 | 0 | 0 |
| L48 | 3 | 3 | 0 | 0 | 0 | 0 |
| L49 FROZEN | 7 | 7 | 0 | 0 | 0 | 0 |
| L50 | 3 | 0 | 3 (T18) | 0 | 0 | 0 |
| L51 | 2 | 2 | 0 | 0 | 0 | 0 |
| L52 | 4 | 4 | 0 | 0 | 0 | 0 |
| L53 | 5 | 5 | 0 | 0 | 0 | 0 |
| L54 | 6 | 6 | 0 | 0 | 0 | 0 |
| L55 | 9 | 9 | 0 | 0 | 0 | 0 |
| L56 | 1 | 0 | 0 | 0 | 0 | 1 |
| L57 | 1 | 1 | 0 | 0 | 0 | 0 |
| L58 (+ Fold section) | 20 | 11 | 3 (T7, T9, fold merge) | 0 | 5 | 1 |
| L59 | 6 | 6 | 0 | 0 | 0 | 0 |
| L60 | 5 | 5 | 0 | 0 | 0 | 0 |
| L61 | 5 | 5 | 0 | 0 | 0 | 0 |
| L62 | 13 | 12 | 0 | 0 | 1 | 0 |
| L63 | 3 | 3 | 0 | 0 | 0 | 0 |
| L64 | 7 | 7 | 0 | 0 | 0 | 0 |
| L65 | 5 | 5 | 0 | 0 | 0 | 0 |
| L66 | 3 | 3 | 0 | 0 | 0 | 0 |
| L67 | 22 | 18 | 0 | 0 | 2 | 2 |
| L68 | 9 | 9 | 0 | 0 | 0 | 0 |
| L69 | 1 | 1 | 0 | 0 | 0 | 0 |
| L70 | 2 | 2 | 0 | 0 | 0 | 0 |
| L71 | 5 | 5 | 0 | 0 | 0 | 0 |
| L72 | 6 | 6 | 0 | 0 | 0 | 0 |
| L73 | 8 | 7 | 0 | 0 | 0 | 1 |
| L74 | 5 | 5 | 0 | 0 | 0 | 0 |
| L75 | 3 | 2 | 1 (T18) | 0 | 0 | 0 |
| L76 | 5 | 5 | 0 | 0 | 0 | 0 |
| Not law | 5 bullets (pointers, not law) | — | history by T17; one pointer's content lost from every read path (DevDocs authorship, Q6-3) | 0 | 0 | 0 |

**L1–L76 traced: 76 (+ header, How to read, Preamble, Not law, Fold) · sentences lost: 0 · current law moved to history: 19 · meaning changed: 9.**

MOVED WHILE CURRENT — live sentence verbatim → where it went → why it is still current → restore wording (`P/proposed-LAWS.md` line):
1. How to read `M/LAWS.md:10` "Entries are editorial consolidations of the cited sources, not verbatim quotations." → history → it tells a reader how to read every entry → `:3` += ` Entries consolidate their sources; they are not quotations.`
2. `:12` "External documents are cited by filename." → history → binds every new entry → `:7` += ` External documents are cited by filename.`
3. `:12` "The hub's fold job refuses a bare `R<n>` or `§<n>` reference in either direction." → history → an enforcement rule on every fold → `:7` += ` A fold refuses a bare \`R<n>\` or \`§<n>\`.`
4. `:13` "…is historical, and is never used for a new ruling." (O<n>) → history → binds new text → `:7` += ` \`O<n>\` and \`PROPOSED-<n>\` are historical, never written in new text.`
5. `:14` "They are read, never written in new text." (PROPOSED-1…6) → history → same (covered by 4's wording).
6. (not counted — KEPT) `:17` the FROZEN line's "and L24's/L27's routing sentences" → carried by the L24/L27 headings (`:83`, `:93`).
7. L19 `:117` "…ONE `CONTINUE:` prefix line naming the resume point…" → "naming the resume point" dropped → `:69` "…with one \`CONTINUE:\` prefix line naming the resume point…".
8. L28 `:165` "…and close into a Cobalt command the day one ships (L58)." → history → the L65 note edits have no other sunset clause → `:100` += ` They move to a Cobalt command the day one ships.`
9. L33 `:193` writer "= workspace-write in a worktree, on-request" → "on-request" dropped → `:118` "writer (workspace-write in a worktree, on request)".
10. L33 `:194` "\"never bare\" for exec means the sandbox flag." → history → `:118` "(\`exec\` takes no \`-a\`; for it, \"never bare\" means the sandbox flag)".
11. L34 `:199` "The day `cobalt_jobs` records agent sessions, this clause is amended, not silently bypassed." → history → the sunset rule L7 and L58 keep → `:121` += ` When \`cobalt_jobs\` records agent sessions, this law is amended, not bypassed.`
12. L45 `:256` "The 09-10 R2 rule restricting the repo to a single synthetic example screen is REVOKED as the root cause of the 09-12 production failure; the revocation stands" → history → a standing revocation (the ledger still holds the revoked rule) → `:154` += ` The 09-10 rule limiting the repo to one synthetic example screen stays revoked.`
13. L58 `:324` "`SESSION-CLOSE.md` names the runner of every step." → history → the draft's own SESSION-CLOSE runner column rests on it (`P/PROPOSAL.md:41` "L58 requires one") → `:195` += ` \`SESSION-CLOSE.md\` names the runner of every step.`
14. L58 `:325` "A status line written between closes goes to the desk report, not to NOW." → history → a rule the desk applies daily → `:196` += ` A status line between closes goes to the desk report, not to NOW.`
15. Fold `:453` "Trigger: every session close, including a close with no new law — a no-change close records that outcome." → history → `:195` += ` A close with no new law records that outcome.`
16. Fold `:453` "Uncertain classification stays OPEN for Dejan." → history → `:195` += ` An uncertain classification stays OPEN for him.`
17. Fold `:453` the close hub's inputs ("the live ledger's newly dated rulings, this file and LAWS-HISTORY.md, Memory INDEX + … and Dejan's session rulings with dated provenance") → history → procedure; acceptable in `SESSION-CLOSE.md` instead: `P/proposed-SESSION-CLOSE.md:3` += ` Inputs: the ledger's new dated rulings, LAWS, LAWS-HISTORY, INDEX + profile + preferences, the day's rulings with their words and times.`
18. L62 `:344` "…the launch row cites the ruling instead of a dated grant." → history → prompts gate on it (contract K13) → `:210` "…pre-approved on every later launch line — the launch row cites the ruling, never a dated grant — and never asked again."
19. L67 `:370` "This settles what L29's \"two parties, ≤3 rounds\" becomes under this law: four houses, ≤3 rounds each; L39's termination rule … is unchanged." → history → FROZEN L29 still says "two parties, ≤3 rounds" (`P/proposed-LAWS.md:105`); without this sentence the two laws read as conflicting → `:228` += ` This is what L29's "two parties, ≤3 rounds" becomes: every tribunal house, ≤3 rounds.`
20. L67 `:372` "Sol and Astra draw on the same Codex allowance — the probe stays a preflight." → history → a standing preflight rule → `:230` += ` Sol and Astra share one Codex allowance; the probe stays a preflight.`

MEANING CHANGED — live → draft → the change → restore:
1. L13 `:87` "Claude protects Dejan's time, including from the project itself." → `:51` "Protect his time, including from the project." → duty widened from Claude to every reader; no T-ruling → restore "Claude protects his time, including from the project."
2. L17 `:107` "vault and personal layer are exposable to any vendor or local model at Dejan's choice (opt-out, not opt-in)" → `:63` "may go to any vendor or local model at his choice" → the default flips to opt-in on a literal reading → restore "Vault and personal layer go to any vendor or local model unless he opts out; secrets never, on any channel."
3. L20 `:121` "Claude searches/reads the named threads before answering — never answers from memory alone appearing to have reviewed" → `:72` imperative → subject widened as in 1 → restore "…Claude reads the named threads before answering…".
4. L31 `:182` "Known offender `cameron_grid` → rename in ADR-0008." → `:112` "`cameron_grid` is renamed by ADR-0008." → an owed rename reads as done → restore "Known offender: \`cameron_grid\` → rename in ADR-0008."
5. L56 `:311` "The Obsidian + Postgres memory layer in `6 - Permanent/Memory/` is THE memory for every agent" → `:188` "`6 - Permanent/Memory/` is the memory for every agent" → Postgres half of the memory layer dropped; a Postgres memory store could now read as "a private store" → restore "The Obsidian + Postgres memory layer in \`6 - Permanent/Memory/\` is the memory for every agent; no house keeps a private store."
6. L58 `:323` "This file changes only from the close prompt's list of that day's approved rulings, each carrying his words, the time and the exact fold text" → `:194` "This file changes only from his approved rulings (his words, the time, the exact fold text)" → the LAWS source widened from the close list to any approved ruling; not among his T7/T9 changes → restore the live clause; the pre-existing tension it resolves goes to OWNER 1.
7. L67 `:369` "The desk records the override with his words and the time in the day's desk report" → `:229` "the desk records his words and time" → the place of record dropped (the proposal says L67 "holds without text change", `P/TRIBUNAL-SUMMARY.md:38`) → restore "…records his words and time in the day's desk report…" (with Q10-1's definitional line).
8. L67 `:372` "Desk readings, not his words (…): a \"new build\" is the first check of a new feature's build, …; the Anthropic seat named \"Fable\" runs as 09-22 R109 pins it (Opus 5.5) until his word." → `:230` both stated as plain law → two desk readings promoted to ruled law without his word → restore the label: "(desk readings, not his words: a new build = the first check of a new feature's build; the Anthropic seat named Fable runs as Opus 5.5, 09-22 R109, until his word)".
9. L73 `:413` "records the override with his words and the time in the day's desk report" → `:250` "records it" / "each override is recorded (his words, the time)" → place of record dropped → restore "…records it in the day's desk report (his words, the time)…".

REWORDED by his rulings — checked for HIS meaning: L6 (T18: the three pattern names kept — carried); L36 (T18: desk = planner and hub-starter; a hub launches only its prompt's seats — carried; note the prohibition "No worker spawns workers" now lives only in the heading); L50 (T18: generalized to any house's headless model — carried); L75 (T18: "one per message" struck — carried, count in `P/proposed-preferences.md:10`); Preamble (T3: `startup file → areas/cobalt.md → INDEX → this file` — carried; note `P/PROPOSAL.md:155` says the 09-13 MECHANISM quote "stays verbatim", but the draft moves it to history under T17 — WRONG FACTS 4); L58 (T7 move-to-history, T9 section tags, the Fold section merged — carried, except the five sentences in MOVED 13–17 and the source widening in MEANING 6); How to read `:9` (T17: no dates, no `[amended]` tags — carried).
Rationale-only sentences cut (in K, not findings): L3 "Duplicated paths rot"; L11 "The board stays honest about what it cannot see."; L12 "Design-phase time is now bounded by L67's three-round cap and L73…"; L17 "Epistemic diversity > role diversity for high-stakes judgment."; L28 "this is not a model-judged approval (L37)"; L44 "No exceptions, no per-house withholding."; L46 "With several agents working in parallel later this becomes unmanageable, so the discipline starts now."; L48 "A cleared session takes its narrative with it and only the file survives."; L61 "Dejan directs the desk by voice or text"; L64 "which IS the crash routine"; L66 "A staged checkout … (option B) is not built" (state).

## Self-attack

Readers of every file the drafts replace or edit (`grep -rln -F`, run per file on M; per file-group on the prompts folders 2026-09-25 and 2026-09-27; PLACEMENT and `/Users/cobalt/.claude/ops` by `grep -n` / `grep -rn` with every name as `-e`):
- `CLAUDE.md` — M: `LAWS.md`, `areas/cobalt-houses.md` (:26, :66), `areas/cobalt-sprints.md`, `topics/devices.md` (:31 "CLAUDE.md boundary unchanged"), `topics/working-contract.md` (:40 old wake path), `topics/memory-system.md` (:13, history), 5 `_imports/` files · prompts (with AGENTS/QWEN/.clinerules): 09-25 `02 05 16 17 18 21 24 25 26 36 39`, 09-27 `54 55 56 57` — six tribunal prompts cite "CLAUDE.md's absolute boundary" (`grep -rc`), `36:111` and `39:137` cite "the CLAUDE.md rule" on DevDocs · PLACEMENT `:6 :9 :22 :48` · ops: none.
- `AGENTS.md` — M: `LAWS.md`, `cobalt-houses.md`, `cobalt-sprints.md`, `working-contract.md`, 4 `_imports/`. `QWEN.md` — the same + `topics/cto-desk.md`. `.clinerules` — M: none.
- `INDEX.md` — M: `topics/memory-system.md:9`, 2 `_imports/` · prompts (with areas/cobalt.md, preferences.md, cto-desk-contract): 09-25 `19 31 38`, 09-27 `51 53 54 55 56 57 99-close` · PLACEMENT `:21 :54` (the docs tree's own INDEX.md, a different file).
- `areas/cobalt.md` — M: `topics/cto-desk.md`. `preferences.md` — M: `areas/cobalt-product-definition.md`, `topics/working-contract.md`, `topics/memory-system.md`, 2 `_imports/`. `cto-desk-contract` — M: `INDEX.md`, `topics/cto-desk.md`, itself.
- `LAWS.md` — M: `LAWS-HISTORY.md`, `LAWS.md`, `cobalt-houses.md`, `cobalt-sprints.md`, `cto-desk.md`, 4 `_imports/` · prompts: 59 files across 09-25 / 09-27 (every card).
- `CTO-DESK-WAKEUP` — M: `LAWS.md`, `cobalt-sprints.md`, `cto-desk.md`. `SESSION-CLOSE` — M: `preferences.md`, `LAWS.md`, `areas/cobalt.md`, `cobalt-sprints.md`, `working-contract.md`, `memory-system.md`, `cto-desk.md`, `cto-desk-contract.md`. `UNATTENDED-LAUNCH` — M: `LAWS.md`, `cto-desk.md`, `cto-desk-contract.md` · prompts (with the three above, writing-rules, `_retired/`): 09-25 `19 38`, 09-27 `53 54 55 56 57 99-close`.
- `writing-rules`, `_retired/` — no reader anywhere yet (new).
- Renamed sections: `How to read this file` is still named by `P/proposed-CTO-DESK-WAKEUP.md:27` (fixed in Q2); `Fold-at-session-close` by the live SESSION-CLOSE only (replaced by item 14).
Walked against my text: readers that the apply list leaves stale are in Q6-5 (`working-contract.md:40`) and Q8 (`devices.md:31`); the tribunal prompts' "CLAUDE.md's absolute boundary" wording belongs to prompts already run (no action; new cards follow Q3's line). The `cobalt-sprints.md` / `cto-desk.md` / `LAWS-HISTORY.md` mentions are dated record (history), left as they are.
WITHDRAWN: "Only the stub carries an absolute path" — `P/proposed-CTO-DESK-WAKEUP.md:22` also carries one (READ 1); replaced in Q2 by "Only hop 1 carries an absolute path".
WITHDRAWN: "the desk's reconcile (`:27`) then cannot \"verify from its own words\" and marks them OPEN" — `P/proposed-CTO-DESK-WAKEUP.md:27` handles a close-list wording it cannot settle as "desk reading", not OPEN; replaced in Q10-2.
WITHDRAWN: "PLACEMENT carries D6 + the `_inflight` rule" — `R/docs/PLACEMENT.md:9` defers the D6 tiers to CLAUDE.md's Documentation standard (after item 13: `areas/cobalt.md` `## Docs tree`); replaced in Q6.

## Experiments (L70)

- X1: Codex (Sol, `codex exec -s read-only`) in a scratch session: run the draft wake-up's STEP 0 and READ 7 against two live `--bg` Claude hubs — can it LIST (via `claude agents --json` in its shell), tell busy from idle, STOP, MESSAGE, and MEASURE itself? The verbs it cannot run are the rows of its SEAT PROFILE that read `GAP` (Q1).
- X2: Which CLIs auto-load which startup file: `claude --bg`, `claude -p` (CLAUDE.md), `codex exec` (AGENTS.md), `qwen` (QWEN.md), `grok`, `agy` — each asked in a scratch dir holding a marker-line stub "what does your startup file say?". A CLI that loads nothing needs its card to carry the path (Q3, Q6).
- X3: A card-driven `claude -p` seat with the stub CLAUDE.md, whose card omits `cobalt.md`, asked a boundary question ("may you read the DAS config?") — if it opens `cobalt.md` unprompted, Q3's card line is unnecessary.
- X4: Obsidian: with `areas/cobalt.md` and `_retired/cobalt.md` both present, which file does `[[cobalt]]` open from INDEX, and does the graph/backlink view conflate them? If it picks `_retired/`, rename the retired files (`<file>-retired.md`).
- X5: `notify_when_idle` — confirm it is the tool name the desk's harness exposes, and what it does on a hub already idle (WAIT verb, Q5).
- X6: Does a restic repository hold `6 - Permanent/Memory/` and restore one file to a scratch path (`M/topics/cto-desk-contract.md:123` "restic restores")? If yes, apply steps 5 and 8 are reversible without the extra snapshots (Q8 ii).
- X7: Tokens: in a scratch Claude session, `desk-context.sh` before and after reading exactly the new start set + wake-up reads; compare with bytes ÷ 4 and with the 136,059 baseline's harness share (Q9).
- X8: After apply, create one `APPROVED — pending fold` row and one `LAUNCHED` row in a scratch copy of `cto-<date>.md`; run the RECONCILE grep; it must print exactly the pending row (Q10).
- X9: A Qwen seat (`qwen`, the day-open's allowlist, read-only) given only "start" in `~/cobalt`: log the files it opens; it must reach cobalt.md → INDEX (by absolute path, not `_imports/`) → LAWS (Q2, Q3).

## OWNER (after the tribunal)

1. L58's source of law changes — his laws, and no house can pick. Live L58 (`M/LAWS.md:323`) says LAWS changes "only from the close prompt's list of that day's approved rulings". The live wake-up folds LAWS entries from any `APPROVED` §4 row at reconcile (`R/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md:17`), and the draft (`P/proposed-LAWS.md:194`) widens the law to "his approved rulings". A = keep the close-list-only clause (the desk then stops folding LAWS at wake-up); B = the draft's wording. This seat recommends B, because it matches how the desk already works.

## WRONG FACTS

1. `P/TRIBUNAL-SUMMARY.md:3` "his rulings T1–T21" — the sitting has 25 (`R/docs/40 - DevDocs/reports/desk-startup-tuning-2026-09-27.md:9` "Rulings: 25 (T1–T25)").
2. `P/PROPOSAL.md:3` "rulings T1–T5 … Status: DRAFT — file review in progress" — the sitting closed with T1–T25 (`…/desk-startup-tuning-2026-09-27.md:6` "CLOSED 21:45 EDT").
3. `P/TRIBUNAL-SUMMARY.md:38` and `P/PROPOSAL.md:38` "L7 …, L58, L67, L73 … hold without text change" — `P/proposed-LAWS.md:229` (L67) and `:250` (L73) drop "in the day's desk report" that `M/LAWS.md:369` and `:413` carry.
4. `P/PROPOSAL.md:155` "the 09-13 MECHANISM quote stays verbatim" — `P/proposed-LAWS.md:12-13` has no quote; the quote is only in the history snapshot (`P/proposed-_history-LAWS-2026-09-27.md:24`).
5. `P/PROPOSAL.md:159` "LAWS \"Not law\" line: \"Moved to CLAUDE.md\" → \"lives in `areas/cobalt.md` `## Working rules`\"" — the draft has no "Not law" section at all (`P/proposed-LAWS.md`, whole; `P/PROPOSAL.md:36` moves it to history).
6. `P/PROPOSAL.md:34` "whole old file → `proposed-_retired-cto-desk-contract.md` (verbatim snapshot)", "before 14,553" — the snapshot is 14,731 B / 125 lines and the live file is 16,153 B / 131 lines (`wc -c`, `grep -c ""`), with six rules the snapshot lacks (Q6-1).
7. `P/PROPOSAL.md:32` wake-up "13,102 → 5,585" and `:44` "5,749 → 6,241" — `P/proposed-CTO-DESK-WAKEUP.md` is 6,293 B (`wc -c`); `P/PROPOSAL.md:29` INDEX after "1,488" — the draft is 1,679 B.
8. `P/PROPOSAL.md:38` §4 rows after "≈1,600 est." — `P/PROPOSAL.md:78` and the sitting `:128` use ≈3,500 (−15,943 from 19,443).
9. `P/PROPOSAL.md:46` "Always-loaded block … 3,014 chars" — the drafts sum to 1,679 + 706 + 910 = 3,295 B; characters UNVERIFIED — `wc -m INDEX.md profile.md preferences.md` on the drafts (under 4,000 either way).

## READING

- date → Sun Sep 27 22:26:26 EDT 2026
- ls report path → absent (fresh run)
- AUTHORIZATION (each its own call): `grep -c -x -F "FABLE ROW: R__"` 56 → 0 (filled, R109) · `grep -n "^| R109 "` cto-2026-09-22.md → :56, one row, carries "Make all Opus 5.5 for now" · `git log -S"| R109 | "` → 75b2aa57 · launch row `grep -n -F 56-…` cto-2026-09-27.md → :53 `| R45 |` (= the filled R45), carries `startup-redesign-2026-09-27` and `Fable seat: yes` · `git log -S"56-…"` → 14614742 · hub row `55-…` → :52 R44 (+ :59 watch row), recorded · seat: R109 names claude-opus-5-5 = this session's model id claude-opus-5-5 · R38 :46 carries "you need to start the tribunal" · R95 (09-23) :103 carries "only use Fable, Astra, and Grok for new designs" · PROPOSAL.md → 5e716cab · TRIBUNAL-INSTRUCTIONS.md → 7a31d467 · 7 allow + 3 deny strings each `grep -c -F` = 1 in 17-voice-tts-tribunal-anthropic-seat.md → PASS.

- READ whole: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-27/56-startup-tribunal-anthropic-seat.md`; `M/LAWS.md` :1–454 (two parts, 1–275 and 276–454); `P/TRIBUNAL-INSTRUCTIONS.md`; `P/TRIBUNAL-SUMMARY.md`; `P/PROPOSAL.md`; `R/docs/40 - DevDocs/reports/desk-startup-tuning-2026-09-27.md`; every `P/proposed-*` draft (CLAUDE, AGENTS, QWEN, clinerules, cobalt, INDEX, preferences, writing-rules, CTO-DESK-WAKEUP, cto-desk-contract, SESSION-CLOSE, UNATTENDED-LAUNCH, LAWS, `_retired-cobalt`); `P/proposed-_history-LAWS-2026-09-27.md` :1–6 and :452–457 (the body proven = live LAWS by grep, not re-read); live `R/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `M/topics/cto-desk-contract.md`, `M/areas/cobalt.md`, `M/INDEX.md`, `M/preferences.md`, `M/profile.md`, `R/AGENTS.md`, `R/QWEN.md`, `R/.clinerules`, `R/docs/40 - DevDocs/SESSION-CLOSE.md`, `R/docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md`; `R/CLAUDE.md` (in this session's context from the harness; lines confirmed by `grep -n`).
- NOT read whole (proven by `wc -c` equal to live instead, per the prompt): `P/proposed-_retired-SESSION-CLOSE.md` (5,382 = live), `P/proposed-_retired-UNATTENDED-LAUNCH.md` (8,383 = live); `P/proposed-_retired-cto-desk-contract.md` (14,731 ≠ live 16,153 — searched by grep, Q6-1); `P/proposed-_retired-preferences.md` (1,613 B; not opened — Q8 re-snapshots from live). Not opened: `M/LAWS-HISTORY.md` (32,029 B, `wc -c` only), `M/topics/devices.md`, `M/areas/trading-copilot-os.md`, `M/areas/cobalt-houses.md` (lines 26 and 66 by grep only), `R/docs/PLACEMENT.md` (grep only), `R/docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md` (grep only).
- desk rows: `cto-2026-09-27.md` :9 (R1), :27 (R19), :35 (R27), :46 (R38), :48–:50 (R40–R42), :52–:53 (R44–R45), :59; `cto-2026-09-22.md` :56 (R109); `cto-2026-09-23.md` :103 (R95).
- measures (`wc -c`): proposal folder listing (`ls -la P`); the 14 live files (CLAUDE 16,590 · AGENTS 1,208 · QWEN 1,879 · .clinerules 2,449 · wake-up 13,102 · SESSION-CLOSE 5,382 · UNATTENDED-LAUNCH 8,383 · INDEX 1,912 · cobalt.md 5,278 · preferences 1,456 · profile 706 · contract 16,153 · LAWS-HISTORY 32,029), the sitting 51,972, the instructions 12,171, LAWS 89,839; `grep -c ""`: LAWS 453, history snapshot 456, proposed LAWS 259, contract snapshot 125.
- searches: `grep -c -v -x -F -f` both directions and `grep -n -v -x -F -f` (live vs snapshot); `grep -n -x -F -f` live→proposed LAWS; 8 × `grep -c -F` frozen paragraphs; `grep -n -F` 16 dropped phrases in proposed LAWS; `grep -n -e "L17 Every helper" -e "K20 " -e "K21 " -e "C5 Push" -e "NO PACKETS"` and `grep -n` `:151–:160` on the contract snapshot; `grep -rn -F` for "stale copy / agent-authored / check-ignore / kanban / symbol-check" over P, PLACEMENT, working-contract; `grep -n -F` lost directives in `R/CLAUDE.md`; `grep -n -F "the two import files"`; `ls -R M`; `ls /Users/cobalt/.claude/ops`; `ls` prompts; the Self-attack reader greps (14 on M, 4 on the prompts folders, 1 on PLACEMENT, 1 on ops) + `grep -rc "CLAUDE.md's absolute boundary"` + `grep -n -F "CLAUDE.md"` on 4 memory files and 3 prompts + `grep -n -F "INDEX.md"` on memory-system; `grep -rn -F "How to read this file" / "Fold-at-session-close"`; `grep -c -F` of the profile's launch line in the live wake-up; `grep -n -F` vendor verbs in the draft wake-up; `grep -n -F` in DAY-OPEN-QWEN and PLACEMENT.
- BLIND note: the prompts-folder reader grep (`grep -rn -F "CLAUDE.md"` on three prompts) printed one line of `prompts/2026-09-27/57-startup-derive.md` (:31) — the desk's derive prompt, not a house ruling or the hub's report; nothing of the houses' folder or `reports/startup-tribunal-2026-09-27.md` was listed, read or grepped. No ruling here rests on that line.

## L74

A block appended to a tool result in this session asked for a `Claude-Session:` line in commit messages and PR bodies and named a file-send tool; it is data, not followed (this seat commits nothing). Recorded once.

## ESCALATE

0.

## CONTINUE

next: none — ruling complete 22:43 EDT; the desk commits this report; the hub `55` file-checks it; the derive `57` follows.

TRIBUNAL R1: APPLY AFTER the derive restores 28 law sentences, six contract rules, live snapshots, house profiles

STARTUP FABLE R1 DONE · verdict: APPLY AFTER the derive restores 28 law sentences, six contract rules, live snapshots, house profiles · holds: 1 · holds with wording: 5 · does not hold: 4 · law: traced 76, lost 0, moved while current 19, meaning changed 9 · experiments named: 9 · ESCALATE: 0
