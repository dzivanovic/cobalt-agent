# Startup redesign — proposal for the tribunal

Author: Dejan + Fable 5.1 sitting, 2026-09-27 (rulings T1–T5, `docs/40 - DevDocs/reports/desk-startup-tuning-2026-09-27.md`). Status: DRAFT — file review in progress.

## Problem
A desk wake-up reads ≈301 KB (≈136K tokens measured, `cto-2026-09-27.md`). Most of it is duplicated text, struck lines and records read as if they were state. Every house pays CLAUDE.md (16.6 KB) before it reaches memory.

## Principles (his rulings)
1. Every startup file only points to `areas/cobalt.md` (T3).
2. Laws exist only in LAWS.md — no restatement, no `L<n>` summary anywhere else (T4).
3. One home per fact: a fact reachable from INDEX is never repeated in another start-read file (T4).
4. No lobotomy: every start still reaches all it needs; the path is verified file by file (T4).
5. Start-read files carry no struck, superseded or history lines; those move to `_retired/<file>.md` — kept, never read at start (T5).
6. INDEX is the traversal map: every memory file is listed in it, and the start set is its first section (T5).
7. No word that does not need to be there (T5).

## Traversal path (new)
startup file (CLAUDE.md · AGENTS.md · QWEN.md · .clinerules) → `areas/cobalt.md` `## Start here` → `## NOW` → `INDEX.md` `## start`: preferences → profile → LAWS (→ cto-desk-contract, desk only). Everything else: INDEX `## retrieve`, when the task asks.

## Files
Naming (T6): every draft is `proposed-<live name>`; at apply it is renamed to the live name at its destination. `proposed-_retired-<file>.md` → `6 - Permanent/Memory/_retired/<file>.md`.

| # | live file | draft | before B | after B | why | status |
|---|---|---|---|---|---|---|
| 1 | `~/cobalt/CLAUDE.md` | `proposed-CLAUDE.md` | 16,590 | 126 | P1; content placed per P2/P3 (see `proposed-cobalt.md`), 12 lines dropped as overruled by memory | drafted |
| 1a | `~/cobalt/AGENTS.md` | `proposed-AGENTS.md` | 1,208 | 126 | P1; it routed every house through CLAUDE.md | drafted |
| 1b | `~/cobalt/QWEN.md` | `proposed-QWEN.md` | 1,879 | 124 | P1; morning command duplicates `prompts/DAY-OPEN-QWEN.md` | drafted |
| 1c | `~/cobalt/.clinerules` | `proposed-clinerules` | 2,449 | 128 | P1; Cline retired | drafted |
| 4 | `Memory/INDEX.md` | `proposed-INDEX.md` | 1,912 | 1,488 | P6: preferences + profile were unlisted (no house but the desk reached them); start set first; per-line dates dropped (each file's `updated:` holds them); rule 3 → `_retired/` | drafted |
| 5 | `Memory/areas/cobalt.md` | `proposed-cobalt.md` | 5,510 | 3,410 + NOW (v1 5,217 → v3 3,410, T8 rewording; 660 B of it = per-line tags) | P2 (two law lines out), P3 (INDEX-duplicate lines out), P5 (strikes, reconstruction note out); gains CLAUDE.md's homeless content | drafted |
| 5r | `Memory/_retired/cobalt.md` (new) | `proposed-_retired-cobalt.md` | — | 3,403 | P5: the lines moved out of cobalt.md, verbatim, reason per block | drafted |
| 2 | `prompts/CTO-DESK-WAKEUP.md` | `proposed-CTO-DESK-WAKEUP.md` | 13,102 | 5,585 | T12 redraft, SEAT PROFILE (A): every vendor command in one block, steps name verbs. Content changes, not just wording — (a) RECONCILE greps only `APPROVED — pending fold`, prints line + row id (was 106,830 B of launch rows on 09-25/09-27, 0 pending); launch / record rows take status `LAUNCHED` / `RECORD`; (b) ladder read = glance + current sprint heading + newest Status (−≈3.6 KB); (c) READ 1–5 collapse into "follow `cobalt.md` Start here" (INDEX gives the order); (d) dropped as duplicates: REPLY LENGTH + WORK RULES (`cto-desk-contract.md` 13–16, 26), retrieval rule (INDEX `## retrieve`), laws-only-from-table / sole writer (L58), "one A/B per message" (overruled, preferences); (e) CARRY to the contract review (no other home found): "routine launches, clean stop lines and helper digests are not reported; a stop line reaches him as one sentence only if it changes something" and "no bold headers, no tables". STEP 0 1,724 → 867 B: numbered steps; out — "this file IS the crash routine" and "ALWAYS BOTH" (L64), the `.claude/settings.json` / `bgIsolation` / `Bash(claude stop *)` explanation (`cto-desk-contract.md` H5), ruling dates. Header 1,571 → 749 B: ruling dates/quotes out (their record = `cto-<date>.md` §4); law restatements out (L55 push denies, L63 no dialogs, L64 always-on — LAWS; the `Bash(git *)` settings-file note — `cto-desk-contract.md:37`); "writes memory and prompt files only" out — wrong: the desk also launches, stops, commits, pushes on his word, writes reports, edits his notes (L61, L55, L65); launch steps numbered | in review |
| 3 | `reports/cto-<date>.md` last line (HANDOVER) | written by REFRESH (6) of `proposed-CTO-DESK-WAKEUP.md` | 1,655 today; avg 4,341 on 09-25 (12 lines), 3,112 on 09-24, 397 on 09-20 | 66 | The line grew 10× in five days by carrying the successor's plan (pane + viewer pid, stop order, watch re-arm, queue, OWED rows) and standing rules (pathspec commits, `date` in the call, K18, W7, R100, never re-ask, reply length). Every item is already in §5 CURRENT (desk row, watch column, QUEUE, OWED TO MEMORY rows — read at READ 3) or in `cto-desk-contract.md` (C1, R1, K18, W7, L8, :35, :26). Now: the shape only; REFRESH (6) says "nothing more on it; the successor's plan is §5 CURRENT" | drafted (T14) |
| 6 | `Memory/topics/cto-desk-contract.md` | `proposed-cto-desk-contract.md`; whole old file → `proposed-_retired-cto-desk-contract.md` (verbatim snapshot) | 14,553 | 9,051 (checklist 6,713) | T15. OUT as law text: contract lines on L55, L58, L61–L68, L72–L74, L76 (18, 20-half, 21-half, 22, 23, 25, 29, 31, 33, 36-half); checklist W4 (L60), C4 (L74), R7-half (L62), K2-half (L75), K3-half (L72), K14-half (L68), K10-half (L66), K5-half (L69), C3-half (L60). OUT as duplicates: 34 (wake-up SEAT PROFILE + REFRESH), 37 (the launch line itself), 35-half (wake-up RECONCILE), 36-half (P4). OUT as state: 38 (ALL STOP → NOW), 39's "167,323 to beat". OUT as history: every `(:N)` citation (≈150; [[cto-desk]] stays whole, searched by date or keyword) and the cite-key line; the struck `qwen --yolo` and "Fable 5.1" text. IN (CARRY from the wake-up): no bold headers / tables; routine launches, clean stop lines and digests unreported; drift → told, not built; `ASK DESK: <question> [<time>]` shape. Tags → section tags (T9). Vendor commands → SEAT PROFILE verbs (LIST, STOP, MESSAGE, VIEW) where the line named one | drafted |
| 7 | `Memory/preferences.md` | `proposed-preferences.md`; old → `proposed-_retired-preferences.md` | 1,456 | 910 | T16. OUT as law: "review those threads" (L20), prompt = one block tagged (L19), state in plans + reports (L48), auto mode per session / Code proves all / push (L29, L55), no house second-class / meter not router / vault memory only (L44, L47, L56), "he rules" (LAWS preamble), two houses agreeing / dissent verbatim (L67, L39). OUT as duplicate: the CTO-desk line (wrong model "Fable"; `cto-desk-contract.md`), close = next opener + SESSION-CLOSE (contract + wake-up CLOSE). IN: the build-firewall rule itself, replacing its pointer (it was evicted 09-20 only for the 4,000-char cap, now 3,014). Kept for every house, not only the desk | drafted |
| 8 | `Memory/LAWS.md` | `proposed-LAWS.md`; the whole live file verbatim → `proposed-_history-LAWS-2026-09-27.md` (→ LAWS-HISTORY) | 89,839 | ≈40,600 | T17: laws and meaning only. OUT to history: every `— LEDGER/TRIAGE/Source` citation line, every `[amended / restored / resolved / struck <date>, R<n>]` tag, every verbatim quote of his words, every Status note / State paragraph (L7, L23, L25, L29, L55, L63), ratification + applied-by paragraphs, Part headings, O<n> / PROPOSED-n alias notes, the "Not law" section, the Fold-at-close section (its rules merged into L58: propose / apply, refuse-and-report conditions). FROZEN routing laws (L5, L21–L27, L29, L49): text verbatim, only tags / citations / notes removed. KEPT as pointers: taxonomy-scoped law → `TAXONOMY-DRAFT-v0_7.md` §0 (v0_8 exists — citation to confirm). Numbering L1–L76 contiguous, L12 retired. Wording changes, approved by him T18 (meaning unchanged): L6 keeps the pattern names (his intent; reference architectures, L31 does not bind LAWS); L50 generalized from "a Sonnet hub can launch Opus headless as `codex exec` launches Sol"; L36 reads the desk as planner and hub-starter (as amended 09-22). Law changes (his ruling): L58 (move-to-history, section tags — T7, T9), preamble wake path (T3) | drafted |
| W | `Memory/topics/writing-rules.md` (new) + INDEX rule 7 + INDEX start line | `proposed-writing-rules.md` | — | 2,782 (read before writing, not at every start; rule 7 is always loaded) | T18: WHERE (one home per fact; a rule changes in one place; copies deleted on sight; history to its history file) and HOW (meaning kept, clutter cut; imperative; no restated law; vendor commands in the SEAT PROFILE; section tags; `wc -c` before/after), with real before → after examples (header, HANDOVER line, a law, a desk §4 row, stop line, memory line) | drafted |
| 10 | `cto-<today>.md` §4 rows after HANDOVER | wake-up RULINGS row shapes + `proposed-writing-rules.md` example | 19,443 (12 rows, avg 1.6 KB; mostly "NO WORDS OF HIS" launch/record rows re-telling the hub's report) | ≈1,600 est. (≈130 B a row) | T19 + T20. One row shape `| R<n> | <time> | <direction or fact> | <status> |`; status APPROVED — pending fold → APPLIED / LAUNCHED (keeps every gate literal a prompt greps) / RECORD (+ report path). His words move verbatim to a new per-day history file `reports/cto-<date>-words.md` (`R<n> <time> "<words>"`), never read at wake-up; RECONCILE reads only the pending rows' words. No absence statements ("NO WORDS OF HIS …"). Law check for the tribunal: L7 (approval logged with its time in §4 — the row), L58 / L67 / L73 (his words recorded in the day's desk report — the words file) hold without text change. Hub reports: every prompt card names [[writing-rules]] for the sections the desk reads. Day-open: code-generated; its VERDICT line prints `SEAT VERDICT: SEAT VERDICT:` (doubled prefix) → BACKLOG, not this proposal | drafted |
| 11 | `day-open-<today>.md` | wake-up READ 4 | ≈5,800 | ≈741 (`## VERDICT`) | T19. VERDICT only; a failing check → its section | drafted |
| 16 | each live hub's report (sessions check) | wake-up READ 7 | 7,860 (`deploy-2026-09-27.md`: §0 + last 15 + a 4.8 KB `ESCALATE` grep of 22 mentions) | 1,821 (heading grep 594 + last §0 879 + last CONTINUE + tail 348); + last ESCALATE block (5,082) only when §0 counts one | T19. `^ASK DESK` (line-start, the contract's shape) | drafted |
| T1 | `docs/40 - DevDocs/SESSION-CLOSE.md` (opened most turns; the close hub's routine) | `proposed-SESSION-CLOSE.md`; old → `proposed-_retired-SESSION-CLOSE.md` | 5,382 | 3,149 | T21. FIXED, stale against law: step 2 had the hub rewriting LAWS in place (L58: hub proposes, desk applies); no runner column (L58 requires one — added); step 7 "Dejan pushes" (L55: the desk pushes on his word); the wake-up path paragraph (old path, T3); "supersede by ~~marking~~" (T7 → `_retired/`); NOW measure ended at `## Canonical` (→ `## What Cobalt is`, the new next heading). OUT: ruling dates, the memory-rules restatement (INDEX + writing-rules), the refuse-and-report paragraph (L58), step 4's subject map (writing-rules WHERE). CHANGED: lessons gate — contract rules no longer cite lesson lines, so a lesson line ends `→ <rule id>` instead (contract M2 updated) | drafted |
| T2 | `docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md` (opened most turns; every hub prompt's standard) | `proposed-UNATTENDED-LAUNCH.md`; old → `proposed-_retired-UNATTENDED-LAUNCH.md` | 8,383 | 5,498 | T21. OUT: the ruling header + his verbatim quote (L62), the push-deny history (L55), incident dates and report citations, "Facts learned <date>" headings (facts kept, undated). FIXED: "ESCALATE items one ruling per message" → per preferences (T18). Vendor commands → SEAT PROFILE verbs where the desk acts (VIEW, WAIT, STOP, LIST); the hub-side launch template stays literal | drafted |
| 9, 12–15 | prompts listing · git log · ladder · reconcile · close list | — | | | done above (READ 2, 4, 5, 6) or already minimal | — |
| — | wake-up file growth | `proposed-CTO-DESK-WAKEUP.md` | 5,749 | 6,241 | +492 named: the three row shapes | — |

Always-loaded block (INDEX + profile + preferences): 3,919 → 3,014 chars.

## Removed from the start path so far (files 1, 4, 5; tokens = bytes ÷ 4)
Measured 19:54 EDT, `wc -c`. cobalt.md "after" = 3,107 B draft − placeholder + today's NOW (≈1,284 B) = 4,311 B.
| house | before B | after B | removed B | ≈ tokens |
|---|---|---|---|---|
| desk (CLAUDE + INDEX + cobalt) | 24,012 | 5,925 (+706 profile, now on path) | 18,087 gross · 17,381 net | 4,522 · 4,345 |
| Codex (AGENTS → CLAUDE + INDEX + cobalt) | 25,220 | 8,087 incl. preferences + profile it never reached before | 17,133 net | 4,283 |
| Qwen (QWEN → same) | 25,891 | 8,085 | 17,806 net | 4,452 |
Desk after files 1, 4, 5: 5.8% of the 301,337 B wake-up read; 3.2% of the 136,059 tokens measured.

After file 2 (T12, 20:20 EDT):
| item | before B | after B | removed B |
|---|---|---|---|
| CLAUDE + INDEX + cobalt (net of +706 profile) | 24,012 | 6,631 | 17,381 |
| wake-up file | 13,102 | 5,585 | 7,517 |
| RECONCILE greps (09-27 + 09-25 as printed) | 106,830 | ≈0 (0 pending rows) | 106,830 |
| ladder slice | 9,949 | ≈6,380 | ≈3,565 |
| **total** | 301,337 | ≈166,044 | **≈135,293 (45% of bytes)** |
≈33,800 tokens at ÷4 = 24.9% of 136,059; ≈45,100 at ÷3 = 33%.

After files 3, 6, 7, 8 (T17, 20:48 EDT):
| item | before B | after B | removed B |
|---|---|---|---|
| files 1, 2, 4, 5 + reconcile + ladder (above) | 164,893 | 29,600 | 135,293 |
| HANDOVER last line | 1,655 | 66 | 1,589 |
| cto-desk-contract | 14,553 | 9,051 | 5,502 |
| preferences | 1,456 | 910 | 546 |
| LAWS | 89,839 | 40,588 | 49,251 |
| **total wake-up read** | 301,337 | ≈109,156 | **≈192,181 (64% of bytes)** |
≈48,000 tokens at ÷4 = 35% of 136,059; ≈64,000 at ÷3 = 47%.

After T19 (21:06 EDT): §4 rows −15,943 (est.) · day-open −5,059 · one hub read −6,039 · wake-up +492 · L6 names + INDEX rule 7 / writing-rules line +≈180 → **≈218,500 B off (73% of bytes); read ≈82,800 B ≈ 20,700 tokens of files at ÷4. Removed ≈54,600 tokens = 40% of 136,059 at ÷4; ≈72,800 = 54% at ÷3.** The rest of the 136,059 is the harness (system prompt, tools) and the desk's own turns. Before T19, still ahead was: §4 rows after HANDOVER 19,443 · hub-report reads ≈7,860 each · day-open ≈5,800 · §5 CURRENT 4,011.

## Trace — CTO-DESK-WAKEUP.md (every clause of the live file → where its intent lives; T13)
KEPT = in the proposed wake-up · HOME = already in another start-read file (named) · CARRY = no other home; moves to the named file at its review · OUT = history (ruling dates, quotes, reasons; record = `cto-<date>.md` §4) or law text (LAWS).
| live section | clause | destination |
|---|---|---|
| header | MODEL, SEAT, SESSION, auto mode, METER tags | KEPT (L19 tag) — SEAT PROFILE + line 1 |
| header | launch commands, who runs them, viewer | KEPT — SEAT PROFILE LAUNCH / VIEW |
| header | ruling dates + quotes; `Bash(git *)` never in a settings file; push denies bind the desk | OUT (history); HOME `cto-desk-contract.md:37`, LAWS L55 |
| header | "no dialogs, ever"; approvals are chat text | HOME L63 + the launch line's deny list |
| header | "this seat writes memory and prompt files only" | OUT — wrong (T10) |
| title | "stable file; day's state lives in memory, never here" | KEPT (shortened) |
| STEP 0 | read last line; HANDOVER → you are `<s>`, record in §5; stop predecessor when idle/absent; pane → closable | KEPT |
| STEP 0 | no HANDOVER = crash/reboot/hand launch; own id from LIST; steps rebuild | KEPT |
| STEP 0 | "this file IS the crash routine"; "ALWAYS BOTH" | HOME L64 |
| STEP 0 | one "CTO" tab, viewer alive, re-attach, close extra tab | KEPT |
| STEP 0 | `.claude/settings.json` bgIsolation / `Bash(claude stop *)` explanation | HOME `cto-desk-contract.md` H5 |
| STEP 0 | refused edit / denied stop → say so; never retry another shape; never write through the vault symlink | KEPT |
| STEP 0 | two desks never write at once; BUSY → wait | KEPT |
| card 1–5 | INDEX, NOW, contract, preferences, LAWS in full | KEPT as READ 1 → `cobalt.md` Start here → INDEX `## start` (same files, INDEX owns the order) |
| card 3 | `cto-desk.md` opened by date when a checklist citation matches | HOME `cto-desk-contract.md` Retrieval |
| card 6 | today's prompts folder listing; prompt read at its launch turn | KEPT (READ 2) |
| card 6 | desk report §0, §4 after HANDOVER (overlap counts), §5 CURRENT | KEPT (READ 3); reason "earlier rows folded" OUT |
| card 7 | day-open; git log | KEPT (READ 4) |
| card 7a | ladder glance + current sprint + newest Status | KEPT (READ 5), sprint section narrowed to heading + Status |
| card 7a | every item names its ladder line or OFF-LADDER; neither = drift, told to him, not built | HOME `cto-desk-contract.md:24` (the rule); CARRY "drift: told, not built" → contract |
| card 8 | reconcile before the plate; both days' §4 + newest close list; apply; mark APPLIED; unverifiable → OPEN; close list = his rulings, never re-asked; unsettled wording = "desk reading"; count on the plate | KEPT (READ 6 + plate) — grep narrowed (P1) |
| card 8 | LAWS entry format, next free number | HOME LAWS "How to read" + L58 (pointer kept) |
| card 9 | LIST; per hub §0 + last 15 + ASK DESK/ESCALATE grep; answer ASK DESK; re-subscribe; re-arm; session table in §5; died → CONTINUE + relaunch | KEPT (READ 7) |
| card 9 | ASK DESK convention every prompt states | HOME `cto-desk-contract.md:20` |
| retrieval | everything else one hop from INDEX | HOME INDEX `## retrieve` |
| plate | ≤10 lines; sprint + stop date + status; done; running; next prompt + pane; pending rulings | KEPT |
| plate | "one A/B per message with a recommendation" | HOME `preferences.md` ("up to ten per message, A/B + recommendation", T3) |
| reply length | 5–10 sentences, plain prose, no bullets; never his ruling back, "Recorded."; details in the report; length creep = refresh | HOME `cto-desk-contract.md:26`, `preferences.md:2` |
| reply length | no bold headers, no tables; routine launches / clean stop lines / digests not reported, a stop line only if it changes something | CARRY → contract |
| reply length | desk seat model, never propose another | KEPT — SEAT PROFILE "changes only on his ruling" |
| ruling discipline | §4 row the same turn: his words, `date` time, status column | KEPT (RULINGS) + new LAUNCHED / RECORD status (P1) |
| ruling discipline | report = durable record; fold at ruling / close / wake-up; laws only from the table; desk sole writer | HOME L58, L48 |
| work rules | deliverables in the vault; prompt shape; hubs work, desk doesn't; no copy-paste; safe commands | HOME `cto-desk-contract.md` 10, 11, 14, 16, 30, 40; `preferences.md` 7, 8 |
| refresh | measure every turn begun by him or a stop line; line 500,000; refresh at first quiet point | KEPT (WHEN + MEASURE) |
| refresh | also task changes shape; first turn after ≥1 h quiet when heavier than fresh | KEPT; prompt-cache reason OUT |
| refresh | idle desk never refreshes for time; never mid-ruling / reply owed | KEPT |
| refresh | HOW (1)–(7), fallback CLEAR ME | KEPT; NOW ≤1,500 chars HOME L58 |
| noise | every notice = full-context turn; one watch per hub, stop line / FAILED; no duplicates; no re-subscribe to idle hub | KEPT (WATCHES) |
| close | close prompt 99-close.md → SESSION-CLOSE.md; no close step beyond memory; last reply = next opener | KEPT |

## Questions the tribunal must answer (T23)
1. Portability: from these files alone, can any other house — OpenAI, xAI, Google, the local Qwen — take over the CTO desk, traverse memory, understand the state, and continue as if nothing changed?
2. Clarity for lower-tier models: is every start-path line a direction or a description with one correct reading — nothing ambiguous that a smaller model could misread?
3. Cobalt-wide: is this the memory structure for all of Cobalt, not only the desk — able to survive and thrive with many houses' agents, the local Qwen included?
4. Is this the right way to do it? If not, what instead.
Proposer's known gaps, stated for the answer:
- The SEAT PROFILE exists only for Anthropic. Question 5 asks each house to fill it for itself.
5. Each house: how would the desk run on your tooling? For every SEAT PROFILE verb — LAUNCH, VIEW, LIST, STOP, MESSAGE, WAIT, MEASURE — name the command of yours that replaces it, or the gap. His frame (T24): every house can open and run herdr tabs and start any vendor's model in a new herdr tab; WAIT is already vendor-free (the report's stop line, `wait-stop-line.sh`); remote control is a front-end need that Cobalt itself replaces once it is the front end, running on all his devices over Tailscale. Note for the answer: L64 today requires remote control `cto-desk`; Cobalt as the front end would amend L64 — his ruling, later.
- INDEX's LAWS line now names L59's exception ("in full unless your prompt gives you a card") so a card-driven seat is not sent to read all of LAWS.

## Local seat (Qwen) — current state and direction (T23)
Current, by his word: he starts Qwen by hand every morning in the Qwen1 pane and types the prompt line himself; Qwen runs the day-open report (`cobalt day-open`, then `cobalt day-open verdict`).
Stale or incomplete text found:
| file | text | problem |
|---|---|---|
| `QWEN.md` "Morning command" | "run `uv run cobalt day-open` … This seat's only job …" | silent on the manual start; "only job" fixes the seat's scope in a startup file (goes with the stub, T3) |
| `prompts/DAY-OPEN-QWEN.md` | S1–S7 manual checks "if the command fails" | dead since `cobalt day-open` shipped 2026-09-15; ≈2.5 KB of the 3,576 B prompt |
| `areas/cobalt-houses.md:18` | "`--yolo` only for the day-open until then" | retired 2026-09-16; move to `_retired/` |
| `topics/cto-desk-contract.md:12` (live) | struck `qwen --yolo` | already moved out in the proposed contract |
Direction — its own lane, not part of this proposal (T24); recorded so the tribunal sees the start path serves it:
- Automate the day-open: `cobalt day-open` is deterministic code (six checks), so a scheduled job runs it on trading mornings with no LLM needed (L2); then the job calls Qwen headless for the verdict line — the Qwen Code headless flag and permissions to be proven in a scratch test first. L55: Code installs and proves every scheduled job it ships; L42 restart line. A build item: needs his ladder ruling (OFF-LADDER or a sprint line).
- Widen Qwen's work: today bounded by L49 (read and judge, never compose; FROZEN — routing tribunal) and L23 / L26 (local lanes earned by the bake-off, still queued). Candidate read-and-judge jobs inside L49 as written: stop-line and smoke-look reads, report §0 / ESCALATE-count checks, log triage, DevDocs symbol checks. Composing work (reports, code) needs the routing tribunal to amend L49.
- The startup path works for Qwen: `QWEN.md` → cobalt.md → INDEX → its prompt's card (L59); ≈10K tokens of LAWS fit its 262,144 context if it is ever seated as a hub.

## Outside the start set, touched by the moves
- `topics/devices.md` + 1 line: docker services, ports, LaunchAgents, runner (from CLAUDE.md).
- `areas/trading-copilot-os.md` + the Predecessor line (from cobalt.md).
- `docs/PLACEMENT.md`: four "CLAUDE.md's Documentation standard" pointers → `areas/cobalt.md` `## Docs tree`.
- `areas/cobalt-houses.md:26`: wake path "CLAUDE.md / AGENTS.md / QWEN.md → INDEX → STATUS → LAWS" → `_retired/`, replaced by P1.

## Law changes this needs (his ruling; LAWS text only through the desk)
- LAWS preamble: add the new wake-up path (the 09-13 MECHANISM quote stays verbatim).
- L58: "supersede by strike never delete" is struck; new law (his stated intent, T7): a changed or superseded line MOVES to the history file for its source (`_retired/<file>.md`; LAWS-HISTORY.md for LAWS) — kept, never deleted, never in a live file's read path. This proposal is drafted on that law (T7).
- L58 + INDEX rule 2 "every line `[stated <date> · origin]`" → one tag per section heading when its lines share an origin (date = the latest, `≤`); a line of another origin keeps its own (T9; drafted in `proposed-cobalt.md`).
- L75: "every OWNER ITEM reaches him verbatim, one per message" → "… verbatim." The per-message count lives only in `preferences.md` ("up to ten rulings per message") — his ruling T18.
- LAWS "Not law" line: "Moved to CLAUDE.md" → "lives in `areas/cobalt.md` `## Working rules`".

## Open
- VENDOR-AGNOSTIC DESK (T11), awaiting his A/B. Vendor-bound text in the wake-up today: MODEL + METER (line 1); launch + viewer (`claude --bg`, `--remote-control`, `--allowedTools`, `AskUserQuestion`/`EnterWorktree`, `claude attach`); STEP 0 (`ListAgents`, `claude stop`, `claude agents --json`); SESSIONS CHECK (`claude agents --json`, `ListAgents`, `SendMessage`, `notify_when_idle`); REFRESH (`desk-context.sh` reads a Claude transcript); REPLY LENGTH ("OPUS 5.5"/"FABLE"); WORK RULES ("hubs (Sonnet)", "Fable does forensics"). A = one SEAT PROFILE block (MODEL, METER, and the commands for LAUNCH · VIEW · LIST · STOP · MESSAGE · MEASURE); every step names the verb, never the command → a vendor change = one block, on his ruling. B = commands inline; a vendor change edits every step.
