# STARTUP SHRINK — proposal (2026-09-28)

Proposer: `startup-shrink-draft-0928` (Opus 5.5), from his `cto-2026-09-28.md` R2, bound by his R4 (every line read at start or in a normal run is intent, how-to or rule — no amendment layers, citations, status or explanation; history holds the rest, recalled by link) and carrying the LIVE L64 of his R5 / R6 (applied 05:16; `M/LAWS.md` is now 90,034 B, `M/LAWS-HISTORY.md` 33,083 B). A DELTA on `plans/startup-redesign-2026-09-27/final/` (unapplied; built on side A of every 09-27 `## FOR DEJAN` item — kept). `F` = that `final/` folder · `P` = this folder · `M` = `/Users/cobalt/Vault/Think/6 - Permanent/Memory/` · `R` = `/Users/cobalt/cobalt/`. Every byte figure is `wc -c` at 2026-09-28 05:0x–05:1x EDT unless marked `est.`.

## 1. The rule this cut applies
Nothing is read at start unless the desk's FIRST turn (STEP 0, READ, RECONCILE, the plate) cannot act correctly without it. Everything else is one line with the trigger that opens it: a section link `[[file#heading]]` (Obsidian) that a plain-file house resolves with `grep -n` on the heading line. Every law keeps its text; only WHEN it is read changes.

## 2. Change table
| # | item | file | before (F) → after | required at start? (the first-turn test) | reach after |
|---|---|---|---|---|---|
| 1 | LAWS at start = Preamble + Index | `P/proposed-LAWS.md` | start read 53,168 → 9,148 (file 53,168 → 60,630) | Preamble: YES (he rules; OPEN items; the start path). Index: YES (the map the desk and every seat use to open the entry a turn needs). Entries: NO — no first-turn step applies a law it has not been pointed to; RECONCILE opens the entry it folds (READ 5 "LAWS entry per `## Reading` and L58") | entry = 1 hop (`[[LAWS#L<n> …]]`, or `grep -n "^### L<n> "`) |
| 2 | Where the index lives: TOP OF `LAWS.md`, between `## Preamble` and `## Reading` | `P/proposed-LAWS.md` | — | — | — |
| 3 | The laws that block it: L59, Preamble, Fold section (+ the Reading bullet and the fold's index duty) | `P/proposed-LAWS.md` · history `P/proposed-_history-LAWS-2026-09-28.md` | see §3 | — | — |
| 4 | Desk contract = standing lines; checklist → its own file, one section per trigger | `P/proposed-cto-desk-contract.md` · `P/proposed-cto-desk-checklist.md` (new) | 10,641 → 3,738 (+ `## handover` 1,459 on a HANDOVER wake-up) | Contract, Replies, Seats, Prompts: YES (every turn). Checklist: only `## handover` fires at start (STEP 0.2 ends the predecessor: H2–H4); the rest fire on launch, commit, reads, replies, prompts, memory, close | section = 1 hop (contract's trigger list, or wake-up ON TRIGGER) |
| 5 | `areas/cobalt.md`: the desk reads down to `## Build rules` | `P/proposed-cobalt.md` | desk read ≈5,275 est. → ≈2,619 est. (1,475 on the file with the 85 B placeholder − 85 + today's live NOW 1,229) | NOW: YES. What Cobalt is + Working rules: YES (report shape, law-missing rule). Build rules … Repo facts: NO for the desk's first turn — they bind whoever builds, reviews or drafts a build prompt; every other house still reads the file whole | same file, 1 hop (wake-up ON TRIGGER) |
| 6 | The ladder: NOW carries the sprint line; glance + section on demand | `P/proposed-CTO-DESK-WAKEUP.md` · `P/proposed-SESSION-CLOSE.md` step 3 | ladder read ≈6,380 est. + 1,417 → 0 | The plate needs sprint, stop date, verdict: NOW's sprint line (close step 3 now names it, from step 4a's block). Glance and status block: NO | 1 hop (ON TRIGGER → SPRINT-LADDER) |
| 7 | The wake-up file = a map of content | `P/proposed-CTO-DESK-WAKEUP.md` | 7,478 → 6,454 | SEAT PROFILE, STEP 0, READ, the plate, EVERY TURN: YES. REFRESH HOW, RULINGS row shape, WATCHES, CLOSE: NO → moved verbatim to checklist sections | 1 hop (ON TRIGGER) |
| 8 | RECONCILE reads the close list only when that close is newer than the last `reconciled:` note in §5 | `P/proposed-CTO-DESK-WAKEUP.md` READ 5 | 3,392 est. on every wake-up → 3,392 on the first wake-up after a close, 0 on a refresh | Only an unreconciled close carries rulings not yet applied (L58 "at the next desk wake-up for anything left unwritten") | unchanged |
| 9 | INDEX start set names the ranges | `P/proposed-INDEX.md` | 2,042 → 2,150 (+108 B, named: the two ranges and the checklist line) | YES (the map) | — |
| 10 | Section-link rule; link targets carry no tag/backtick | `P/proposed-writing-rules.md` (3,448 → 3,875, not on the start read) · checklist M4 · `proposed-cobalt.md` Start here | — | NO (writing only) | — |
| 11 | Link resolution for plain-file houses: `[[name]]` = `name.md` in root, `areas/`, `topics/` or `people/` | `P/proposed-cobalt.md` `## Start here` | — | YES (every house resolves links from here) | fixes 09-27 ESCALATE 6 (LAWS / LAWS-HISTORY carry no `name:`) and adds `people/` (`[[partner]]`) |
| 12 | The desk launch line drops unused connectors — UNPROVEN (L70) | `P/proposed-CTO-DESK-WAKEUP.md` SEAT PROFILE LAUNCH — NOT changed in the file; APPLY 16b after X10 | fixed tool-definition context per turn: not measurable from files | — | — |
| 13 | L76 heading loses its backticks (a link target) | `P/proposed-LAWS.md` | — | — | `[[LAWS#L76 One owner, one lock for cobalt_dev]]` |
Files NOT changed by this cut (the 09-27 finals stand): `CLAUDE.md`, `AGENTS.md`, `QWEN.md`, `.clinerules` (each still points to `areas/cobalt.md`; a non-desk house reads it whole, which it needs), `preferences.md`, `UNATTENDED-LAUNCH.md`, `_history-LAWS-2026-09-27.md`, `_retired/cobalt.md`.

Item 12 (connectors). `claude --help` (2.1.283) shows `--no-chrome` ("Disable Claude in Chrome integration") and `--strict-mcp-config` ("Only use MCP servers from --mcp-config, ignoring all other MCP configurations"). The repo has no `.mcp.json` and `R/.claude/settings.json` names no MCP server, so the desk uses none it would lose. Whether `--strict-mcp-config` also drops the claude.ai docs connector (an account connector, not a local MCP config) is NOT shown by `--help`: UNPROVEN; if X10 shows it stays, that half is a GAP (no flag shown). X10 = two scratch `claude --bg` sessions from `~/cobalt`, the desk's launch line with and without `--no-chrome --strict-mcp-config`, each asked to list its `mcp__` tools and stop; `desk-context.sh <id>` on each first turn. The flags go in (APPLY 16b) only when X10 shows the tools gone and the measured tokens lower.

## 3. Law amendments — HIS; folded only on his approval (L58). Each changes WHEN a law is read, never WHAT it says.
Before = `F/LAWS.md` (the 09-27 final); the live `M/LAWS.md` wording, where it differs, is given too. Replaced wording → `P/proposed-_history-LAWS-2026-09-28.md` (verbatim).
| # | entry | before (verbatim) | after (verbatim) | reason |
|---|---|---|---|---|
| A1 | L59 first sentence | F:226 and live M:329: "Architect, hub, builder and reviewer round 1 read LAWS.md in full." | "Every seat — the desk, architect, hub, builder and reviewer — reads this file's `## Preamble` and `## Index` at start, and the whole entry of every law its index card names or its task touches before it acts on that law; a seat unsure whether a law applies opens its entry." | His R2 names this sentence. The rest of L59 (read-and-judge excerpts, rounds 2–3, the card, "never a fence", L44 corollary) is unchanged. |
| A2 | Preamble, last sentence | F:18: "Every house starts at its startup file → `areas/cobalt.md` → INDEX → this file." (live M:21 is his 09-13 MECHANISM quote, "Wake-up path for every house: CLAUDE.md / AGENTS.md / QWEN.md → memory INDEX → LAWS.md." — history under 09-27 item 36, side A) | "Every house starts at its startup file → `areas/cobalt.md` → INDEX → this file's `## Preamble` and `## Index`; an entry is read when a task touches its law (L59)." | "→ this file" reads as the whole file. |
| A3 | `## Reading`, new bullet | — | "`## Index` is a map, never law: a line there binds nothing; its entry binds." | An index sentence is shorter than its law; without this a reader could act on the summary. Adds no rule to any law. |
| A4 | Fold section, inputs sentence | F:295: "The close hub's inputs: the live ledger's newly dated rulings, this file and LAWS-HISTORY.md, Memory INDEX + …" (live M:453 identical) | "The close hub's inputs: the live ledger's newly dated rulings, this file's `## Index` and the entries its candidates touch, LAWS-HISTORY.md's lines for those entries, Memory INDEX + …" (rest unchanged) | "this file and LAWS-HISTORY.md" forces the close hub to read ≈62 KB + ≈123 KB (LAWS-HISTORY after the 09-27 append) every night. |
| A5 | Fold section, desk's work sentence | F:295: "…for a new law, the next free number (L58)." | "…for a new law, the next free number (L58); in the same edit, write or rewrite that law's `## Index` line so every `### L<n>` heading has exactly one." | Keeps the index true; the close proves it by count (`P/proposed-SESSION-CLOSE.md` step 2). |
| A6 | L76 heading | F:291: "### L76 One owner, one lock for `cobalt_dev`" | "### L76 One owner, one lock for cobalt_dev" | A link target with backticks may not resolve (Q4). Body unchanged. Queued prompts cite L76 in prose only (`grep -rln -F "one lock for" prompts/2026-09-25`: 10 files, none greps the heading). |
LEAN (his R4) — one current text per entry; each sentence below moves VERBATIM to `P/proposed-_history-LAWS-2026-09-28.md` (B1–B14). Substance kept: every rule the moved words carried is still stated in the entry (the right column names where).
| # | entry | moved out (kind) | the rule it carried now lives in |
|---|---|---|---|
| B1 | L4 | "Gemini-era failure post-mortem: `.env` is static and cannot call the vault —" (evidence) | "Composition happens in application boot code, two-phase (…), never in dotenv." |
| B2 | L11 | "per the 09-02 taxonomy ruling ("tape = FRONTIER not nature")" (citation, quote) | the same sentence without it |
| B3 | L12 | "Design-phase time is now bounded by L67's three-round cap and L73 … rather than by a planning-cap law of its own." (explanation of a retirement) | the heading "retired; number never reused"; L67 / L73 themselves |
| B4 | L15 | "The clause "vault/.env/personal layer excluded" that previously qualified the carve-out's scope is removed: …" (amendment layer) | "A build-time tool carve-out never narrows L44's equal read access to the vault." |
| B5 | L17 | "flipped" (amendment layer) | "Privacy default: … (opt-out, not opt-in) …" |
| B6 | L28 | "Nothing else in this law changes." (amendment layer) | — (the entry is the whole law) |
| B7 | L32 | "does not revoke the … clause above" · "Both stand together —" (resolution layer) | "L45 governs what tests are specified against; this law governs what leaves the repo as user data: every test fixture follows L45's real-shape rule while the shipped repo carries no user data." |
| B8 | L33 | "The network settings (…) are unchanged by the access clause. The 09-07 profile wording is retained in H-L33-access; it cannot override L44." (amendment layer, history pointer) | the profile sentence (reviewer: network disabled; researcher: web) and L44 |
| B9 | L45 | "The 09-10 R2 rule … is REVOKED …; the revocation stands (…H-R2)." (history) · label "Companion rulings, current:" | "The real artifact's shape is committed as a test fixture …"; "Fixture policy = real-shape …" |
| B10 | L46 | "With several agents working in parallel later this becomes unmanageable, so the discipline starts now." (reason) | — (intent; the rule is the rest of the entry) |
| B11 | L47 | "The 09-10 rule (…) survives as the bounded form of this law's wait-exception: …" (amendment layer) | "When the wait-exception applies, at most one relaunch with a CONTINUE line is taken before a second stop hands the report + diff to the other house; waiting is never the default." |
| B12 | L48 | "A cleared session takes its narrative with it and only the file survives." (reason) | — |
| B13 | L62 | ", the 09-22 R30 shape" (citation) | the same sentence without it |
| B14 | L67 | "(This restates the preamble …)" · "defined by him" · "This settles what … becomes …; … is unchanged" · "from 2026-09-24" · "(his evidence for removing it)" · "The counts, the floor, … are unchanged;" · "Applies to every prompt drafted from 2026-09-23 18:10 ET (prompts drafted earlier run as written)." · "while we follow the new gate rule" (quote) · "L29's routing text is not rewritten here (routing tribunal)." · "The floor, the shrink-to-two clause and the cap's number are unchanged." (layers, dates, a transition clause, reasons) | "Under this law L29's "two parties, ≤3 rounds" means four houses, ≤3 rounds each; L39's termination rule … holds." · "The reduced seats … hold while L68's GATE EARLY clause stands." The transition clause (prompts drafted before 2026-09-23 18:10 ET run as written) is the one line whose removal could change an outcome: no queued prompt predates 09-25 (`ls prompts/`), so none does — Q8 checks it |
KEPT AS WRITTEN, named for Q8: FROZEN L5, L21–L27, L29, L49 keep their text verbatim (the routing tribunal; this prompt's rule) — L23 "continuity rationale (…)", L25 "Local-SPOF question parked", L27 "[routing sentence, under review]", L29's "restored above" note are layers R4 would move, left for the routing tribunal. L67's "Desk readings, not his words:" is a label that states authority (a desk reading is not his ruling): kept; removing it would turn two desk readings into his law — HIS call (Q8). `## Reading` bullets are how-to (notation, what binds); kept.
L64 — LIVE DRIFT: his R5 / R6 amended L64 at 05:16 (`H-L64-rc`); `F/LAWS.md` carries the pre-R6 text. `P/proposed-LAWS.md` carries the LIVE text (tag and "Prior wording →" pointer out, R4); the 09-27 final's L64 goes to history (never applied). Index line updated.
Also on the law file, not law text: `## Preamble` moves above `## Reading` so the start read is one range (top → `## Reading`); the `## Index` section (78 lines: 76 entries + Reading + Fold) is new. Every index link resolves to an exact heading (`grep -x -F "### <target>"` for all 78: 0 missing).
Unchanged, checked: L58 (its wake-up reconcile is a grep of pending rows — cheap, required), L64's crash clause ("the same wake-up file" = STEP 0 + READ stay in it), L29 and the routing cluster L5, L21–L27, L49 (verbatim; `grep -v -x -F -f` between `F/LAWS.md` and `P/proposed-LAWS.md` shows only the A, B and L64 lines changed — 24 lines; every other entry line byte-identical).
Checklist (R4): the five citation tails `(:153)` … `(:158)` leave K19, K20, K21, L17, C5; K20's "(desk reading, his word overrules; L66 unchanged)" → "(a desk reading; L66 holds)". The originals stay in `_retired/cto-desk-contract.md` (09-27 APPLY 2b, snapshotted from live).

HOW EVERY SEAT READS LAWS — one rule (A1), recommended: every seat reads Preamble + Index (≈9.1 KB) at start and the entries its card names or its task touches. Price: a seat that read 53,168 B (≈13,300 tokens ÷4) now reads ≈9,105 B + its entries (≈0.5–3 KB each), saving ≈10,000 tokens per launch of an architect, hub, builder or reviewer round 1. Risk: a seat acts under a law it never opened because its index line misled it. Guards: A3 (the index binds nothing), the card names the binding laws (L59 unchanged), reviewer round 1 and the tribunal/check houses (L67) see the same law, and a card can still say "LAWS.md in full" (queued prompts do — valid under A1). Alternative B: architect and reviewer round 1 keep the full read, hub and builder use the index — safer for judgment seats, ≈13,300 tokens each; not recommended: the architect and reviewer are exactly the seats whose cards name their laws most completely.

## 4. Reachability — NO LOBOTOMY (his T4), ≤2 hops per house
Hop 0 = read at start. Every fact in the 09-27 finals stays reachable; none moved out of a file a house reaches.
| house · start file | hop 0 | hop 1 | hop 2 |
|---|---|---|---|
| desk · `CTO-DESK-WAKEUP.md` (+ `CLAUDE.md` auto-load) | cobalt.md top → `## Build rules`; INDEX; preferences; profile; LAWS Preamble + Index; contract; checklist `## handover` (on a HANDOVER) | any LAWS entry; any checklist section; cobalt.md from `## Build rules`; writing-rules; SPRINT-LADDER; every INDEX retrieve file; UNATTENDED-LAUNCH; `cto-<date>-words.md` | LAWS-HISTORY lines (via an entry's number); files those link |
| builder / reviewer / architect (Claude) · `CLAUDE.md` → cobalt.md | cobalt.md whole; INDEX; preferences; profile; LAWS Preamble + Index; its prompt's card | any LAWS entry (was hop 0 — the only fact that moved deeper); INDEX retrieve files | files those link |
| Codex seat · `AGENTS.md` | same as the Claude builder | same | same |
| Qwen · `QWEN.md` / Cline · `.clinerules` | same as the Claude builder | same | same |
| hub (any house) · its prompt card | the card's files; LAWS Preamble + Index (A1) | named entries; any entry | — |
| read-and-judge seats (local day-open, agy, Grok probes) · their card | card excerpts (L59 unchanged) | — | — |
| Grok / agy tribunal seats · the instructions file | the files it lists, whole | — | — |
The desk loses nothing at hop 0 that its first turn uses: every rule moved (REFRESH HOW, RULINGS, WATCHES, CLOSE, the checklist groups) sits behind a named trigger in the wake-up's ON TRIGGER list or the contract's checklist list.

## 5. MEASURE — the desk's wake-up read (rows of `F/MEASURE.md`)
| # | item | F (09-27 final) | after | source |
|---|---|---|---|---|
| 1 | `cto-<prev>.md` RECONCILE grep | ≈0 est. | ≈0 est. | unchanged |
| 2 | `LAWS.md` | 53,168 | 9,148 | `awk '/^## Reading/{exit} {print}' P/proposed-LAWS.md \| wc -c` |
| 3 | `cto-<today>.md` RECONCILE grep | ≈0 est. | ≈0 est. | unchanged |
| 4 | §4 rows after HANDOVER | ≈3,500 est. | ≈3,500 est. | unchanged |
| 5 | `CLAUDE.md` | 126 | 126 | unchanged file |
| 6 | `cto-desk-contract.md` | 10,641 | 3,738 | `wc -c P/proposed-cto-desk-contract.md` |
| 6b | checklist `## handover` (a HANDOVER wake-up only) | 0 | 1,459 | `awk` on `P/proposed-cto-desk-checklist.md` |
| 7 | `CTO-DESK-WAKEUP.md` | 7,478 | 6,454 | `wc -c P/proposed-CTO-DESK-WAKEUP.md` |
| 8 | ladder S3 slice | ≈6,380 est. | 0 | NOW's sprint line |
| 9 | one live hub's report | ≈1,821 est. | ≈1,821 est. | unchanged (per hub) |
| 10 | `day-open` VERDICT | ≈741 est. | ≈741 est. | unchanged |
| 11 | §5 CURRENT | ≈4,011 est. | ≈4,011 est. | unchanged |
| 12 | newest close Laws-fold list | ≈3,392 est. | ≈3,392 est. (first wake-up after a close) · 0 (refresh) | READ 5 condition |
| 13 | `areas/cobalt.md` | ≈5,275 est. | ≈2,619 est. | 1,475 (`awk '/^## Build rules/{exit} {print}'` on the draft) − 85 (placeholder) + 1,229 (today's live NOW, `awk` on `M/areas/cobalt.md`) |
| 14 | `INDEX.md` | 2,042 | 2,150 | `wc -c P/proposed-INDEX.md` |
| 15 | HANDOVER last line | ≈66 est. | ≈66 est. | unchanged |
| 16 | `preferences.md` | 953 | 953 | unchanged |
| 17 | Ladder at a glance | 1,417 | 0 | on trigger |
| 18 | `git log --oneline -5` | ≈665 est. | ≈665 est. | unchanged |
| 19 | §0 Headline | ≈561 est. | ≈561 est. | unchanged |
| 20 | prompts listing | ≈400 est. | ≈400 est. | unchanged |
| 21 | `profile.md` | 706 | 706 | unchanged |
| — | **total, first wake-up after a close** | **≈103,343** | **≈42,510** | rows 1–21 + 6b |
| — | total, a REFRESH wake-up (no newer close) | ≈103,343 | ≈39,118 | − row 12 |
Tokens ≈42,510 ÷4 ≈ 10,600 · ÷3 ≈ 14,200 (planning estimates, not token accounting). Always-loaded block: `wc -m` INDEX 2,082 + profile 691 + preferences 939 = 3,712 characters < 4,000.
Against the desk's ≈30,000 B estimate: ≈12,500 B heavier. Named: the Index is ≈8,600 B (76 one-sentence lines, his item 1's shape — a title-and-link-only index would be ≈3,500 B, but drops the rule sentence he asked for); the wake-up keeps SEAT PROFILE + STEP 0 + READ (≈6,454, all first-turn); ≈13,100 B are day-state rows this cut does not own (rows 4, 9, 11, 12, 19).

## 6. His rulings this cut carries, and the ones it sets aside
- Carried: T1–T25 wordings (no line of a 09-27 final is reworded except the lines above; the checklist lines, REFRESH HOW, RULINGS, WATCHES and CLOSE move VERBATIM — `grep -v -x -F -f` shows only headings, tags and the prefixes `REFRESH HOW:` / `[stated …]` added).
- Set aside by R2 (his later, direct instruction — L73: recorded, not asked): T16 A ("the checklist stays in the wake-up read (contract whole)") — now read on trigger, meaning kept, 1 hop; T13 ("everything is still going to be read") for the wake-up's REFRESH / RULINGS / WATCHES / CLOSE — read on trigger. The desk records these in its §4 when it brings the approval.

## 7. APPLY — the delta on `F/APPLY.md` (32 rows)
The shrink derive (`prompts/2026-09-28/04-shrink-derive.md`) writes ONE combined `final/APPLY.md` that supersedes `F/APPLY.md`. Rows of `F/APPLY.md` not named here are carried unchanged. History first; the wake-up file last; never during a deploy (step 0 (b), re-checked before 16); every step reversible — the vault is not a git repository, so step 0a's `_before/` copy IS the vault revert.
| F row | change | kind | wc -c before → after | revert |
|---|---|---|---|---|
| 0 | + (g): the set applied is the combined `final/` of this cut; `F/` (09-27) is not applied on its own | gate | — | none |
| 0a | + record ABSENT `M/topics/cto-desk-checklist.md` | snapshot | — | as F |
| X1 · 1 | RE-SNAPSHOT: live `M/LAWS.md` changed at 05:16 (R6, L64) — 89,839 → 90,034. The combined derive re-takes `_history-LAWS-2026-09-27.md` from the live file as it is at derive time (header + live body); X1's `cmp` and step 1's line proof run on that; the desk re-proves at apply | append | 33,083 → ≈123,487 est. (33,083 + 370 + 90,034) | Write `_before/LAWS-HISTORY.md` back |
| **1b (added)** | append `P/proposed-_history-LAWS-2026-09-28.md` after the 09-27 block | append | → + ≈6,300 est. | as 1 |
| 4 | source = the combined `final/LAWS.md`; guard = live `M/LAWS.md` equals what the derive read (90,034 today; any later change = LIVE CARRY into the combined final first, never overwritten) | whole-file replace | 90,034 → 60,630 | Write `_before/LAWS.md` back |
| 5 | source = combined `final/INDEX.md` | whole-file replace | 1,912 → 2,150 | as F |
| 7 | source = combined `final/writing-rules.md` | whole-file write | absent → 3,875 | remove |
| 8 | source = combined `final/cobalt.md` + the live NOW over its placeholder | whole-file replace | 5,278 → ≈5,568 est. (4,424 − 85 + live NOW) | as F |
| 9 | source = combined `final/cto-desk-contract.md`; LIVE CARRY applies to the contract AND the checklist (a live line newer than the 09-27 snapshot goes to its section) | whole-file replace | 16,153 → 3,738 | as F |
| **9b (added)** | `M/topics/cto-desk-checklist.md` (new) ← combined `final/cto-desk-checklist.md` | whole-file write | absent → 10,517 | remove `M/topics/cto-desk-checklist.md` |
| 14 | `SESSION-CLOSE.md` source = combined final | whole-file replace | 5,382 → 3,476 | `git checkout <pre-apply sha> -- …` |
| **X9 (added, before 16)** | LINKS: every `[[…#…]]` in the applied files resolves — `grep -x -F "### <target>"` / `"## <target>"` per link (78 in LAWS, 11 in the wake-up, contract and INDEX); Obsidian opens one link per file; a scratch `claude -p` asked for L59 reads only LAWS down to `## Reading` plus that entry (its tool log) | read / scratch | — | none |
| **X10 (added, before 16)** | CONNECTORS: item 12's scratch pair | scratch | — | none |
| 16 | source = combined `final/CTO-DESK-WAKEUP.md` | whole-file replace | 13,102 → 6,454 | `git checkout <pre-apply sha> -- …` |
| **16b (added, same step)** | only if X10 passed: SEAT PROFILE LAUNCH — named edit `--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt-wt` → `--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt-wt --no-chrome --strict-mcp-config`; X10 failed → not applied, recorded GAP | named edit | 6,454 → 6,488 | as 16 |
| 17 | MEASURE against §5 of this file; + `grep -c "^### L" M/LAWS.md` = `grep -c "^- \[\[LAWS#L" M/LAWS.md` = 76 | read | — | none |
| 19 | VERIFY against the combined `final/MEASURE.md` | read | — | none |
| X4 | + a plain-file house (`codex exec`, `grok`) resolves `[[LAWS#L59 Worker law-reading]]` and `[[cto-desk-checklist#launch]]` by the rule in `cobalt.md` `## Start here` | scratch | — | none |
Rows after the cut: 32 + 5 added (1b, 9b, X9, X10, 16b) = 37. The 09-27 guards that name 89,839 (X1, 1, 4) are superseded by the rows above.

## 8. Carried from 09-27 (`cto-2026-09-28.md` R1) — each on its recommended side; `F/` was built on it
- (1) His override words in the linked `cto-<date>-words.md` count as part of the day's desk report (L67 / L73) — A.
- (2) L58's source of law changes: "only from his approved rulings" — B (the Anthropic seat) vs keep live — A: the 09-27 finals keep the live sentence (A); the derive recommended B. Carried as it stands.
- (3–35) The 33 LAW PRESERVATION entries keep his live wording — A (all three houses).
- (36) The 09-13 MECHANISM quote — history only (A, T17); its quoted wake path would contradict A2 if pasted back.
