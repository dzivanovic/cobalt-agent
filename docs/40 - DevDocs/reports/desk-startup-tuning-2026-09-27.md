# Desk startup tuning — 2026-09-27

Seat: Fable 5.1 design sitting (`53-desk-startup-tuning.md`, `cto-2026-09-27.md` R19, OFF-LADDER R1/R19). Writes this file only; the desk applies (L58).

## §0 Headline
CLOSED 21:45 EDT by him (T25). Output: a tribunal proposal, `docs/40 - DevDocs/plans/startup-redesign-2026-09-27/` (TRIBUNAL-SUMMARY.md · PROPOSAL.md · 13 `proposed-<live name>` files · history snapshots). Nothing applied.
Wake-up file read ≈301,337 B → ≈82,800 B (−73%) ≈ −54,600 tokens = 40% of the 136,059 measured (÷4).
Next (the desk): launch the L67 new-design tribunal (Fable · Astra · Grok, Gemini optional) on TRIBUNAL-SUMMARY.md; after its derive + his ONE approval, apply `## FOR THE DESK` in order.
Rulings: 25 (T1–T25). ESCALATE: 0. OPEN: 0.

Session log (as written during the sitting): T1 18:17: his method — file-by-file review in read order; P1 held. T2 18:43: startup files = pointers only; CLAUDE.md audit done (≈60% duplicate, rest has no memory home). T3 18:47: all startup files → `areas/cobalt.md`; memory wins; A1–A9 drafted (CLAUDE.md 16,590 → ≈330 B; cobalt.md 5,510 → ≈11,700 B; desk wake-up −≈16 KB). T4 18:54: laws only in LAWS, one home per fact → A5r (cobalt.md +≈4.3 KB, no law refs), INDEX gap found (preferences/profile unlisted). T5 19:0x: output = tribunal proposal in `plans/startup-redesign-2026-09-27/`; drafted: stub, INDEX (1,912 → 1,488), cobalt.md (+ retired/cobalt.md). T6 19:36: drafts renamed `proposed-<live name>`. T7 19:39: savings so far desk −15,977 B (≈ −4.0K tokens, ≈3%); drafting on his intended move-to-history law. T8/T9: proposed-cobalt.md 5,217 → 3,107 B (section tags). T12 20:20: wake-up redrafted with SEAT PROFILE 13,102 → 5,585 B; total ≈ −135 KB ≈ −33.8K tokens ≈ 25%. T14–T17: HANDOVER line, contract, preferences, LAWS (89,839 → 40,588) drafted; total ≈ −192 KB ≈ −48K tokens ≈ 35%. T18–T22: L6 names back, L75 ten-per-message, writing-rules, §4 rows / day-open / hub reads, SESSION-CLOSE + UNATTENDED-LAUNCH; FOR THE DESK + TRIBUNAL-SUMMARY written. Total ≈ −218.5 KB ≈ −54.6K tokens ≈ 40% (÷4). Rulings: 22. ESCALATE: 0. OPEN: 0.

## Measure
Measured 2026-09-27 18:1x ET with `wc -c` on the live files; tokens = bytes ÷ 4. "Need" = W (wake-up) or T (only when a task asks).

| # | file / slice | step | bytes | tokens | need | note |
|---|---|---|---|---|---|---|
| 1 | `cto-2026-09-25.md` `grep -n -F APPROVED` rows lacking `APPLIED:` | 8 | 85,956 | 21,489 | T | 40 rows; statuses are `APPROVED — launch row…` / `DESK RECORD`; `APPROVED — pending fold` count = **0** |
| 2 | `LAWS.md` in full | 5 | 89,839 | 22,460 | T* | *L59: architect reads in full — a law step |
| 3 | `cto-2026-09-27.md` same grep | 8 | 20,874 | 5,219 | T | 13 rows, pending fold = **0**; re-prints rows step 6 already read |
| 4 | `cto-2026-09-27.md` §4 rows after HANDOVER (R8–R19) | 6 | 19,443 | 4,861 | W | rows avg 1.5 KB; mostly "NO WORDS OF HIS" desk records |
| 5 | `CLAUDE.md` (auto-loaded by harness) | — | 16,590 | 4,148 | — | every house pays it; not a desk step |
| 6 | `topics/cto-desk-contract.md` | 3 | 14,553 | 3,638 | W | Standing contract restates LAWS/wake-up; checklist is launch craft |
| 7 | `prompts/CTO-DESK-WAKEUP.md` | launch | 13,102 | 3,276 | W | launch line alone ≈1.6 KB; REFRESH/RULING/WORK rules restate contract + LAWS |
| 8 | `SPRINT-LADDER-v0_1.md` S3 section (incl. Status 09-24) | 7a | 9,949 | 2,487 | W (1 line) | plate needs one line: sprint, stop date, ON TIME/AT RISK |
| 9 | per live hub: §0 + last 15 + `ASK DESK\|ESCALATE` grep (`deploy-2026-09-27.md`) | 9 | 7,860 | 1,965 | W | grep ESCALATE hits 4.8 KB of old rows; × live hubs |
| 10 | `day-open-<today>.md` (typical; none today) | 7 | ~5,800 | ~1,450 | T | a trading-day brief; the desk does not trade |
| 11 | §5 CURRENT | 6 | 4,011 | 1,003 | W | the live state — keep |
| 12 | `close-2026-09-24.md` Laws fold list | 8 | 3,392 | 848 | W | only when a close is newer than the last reconcile |
| 13 | NOW (+ frontmatter to reach it) | 2 | 1,902 | 476 | W | keep |
| 14 | INDEX.md | 1 | 1,912 | 478 | W | keep |
| 15 | newest desk report LAST line (HANDOVER) | 0 | 1,655 | 414 | W | today's is short; 09-25's ran 3–4 KB each |
| 16 | preferences.md | 4 | 1,456 | 364 | W | keep |
| 17 | Ladder at a glance | 7a | 1,417 | 354 | T | |
| 18 | `git log --oneline -5` | 7 | 665 | 166 | W | keep |
| 19 | §0 Headline | 6 | 561 | 140 | W | keep |
| 20 | prompts/<today>/ listing | 6 | ~400 | ~100 | W | keep |
| 21 | `claude agents --json` output | 0, 9 | not measured | — | W | not in this seat's commands |
| — | **wake-up total (1–20)** | | **≈301,337** | **≈75,300** | | |
| 22 | `SESSION-CLOSE.md` | most turns | 5,382 | 1,346 | T | |
| 23 | `UNATTENDED-LAUNCH.md` | most turns | 8,383 | 2,096 | T | |
| 24 | `topics/cto-desk.md` (record, not read at wake-up) | retrieval | 124,556 | 31,139 | T | state — never cut |

## Proposals
| # | file | cut | before → after bytes | touches | status |
|---|---|---|---|---|---|
| P1 | WAKEUP step 8 | status read = `grep -n -F "APPROVED — pending fold"` + `cut -c1-12` (line + row id); open only those lines; launch/record rows stop using the word APPROVED (`LAUNCHED — …`) | 110,222 → ~200 | reconcile (still finds every pending row — the status string RULING DISCIPLINE defines) | HELD — his file-by-file review (T1) |

## Rulings
| # | time | his words (verbatim) | exact effect |
|---|---|---|---|
| T1 | 18:17 EDT | "Now we're gonna do this my way and I have an idea of how I want to uh, go over the entire routine. List every single file by name and its uh, destination in the vault. What does desk read file by file? And we will go file by file. And I want to review each one of them." | Method: file-by-file review in read order, his lead. P1 held until his review reaches the step 8 files. No text change yet. |

Read order he reviews (vault path; `0 - Projects/Cobalt` = symlink to `~/cobalt/docs`):
1. `~/cobalt/CLAUDE.md` — NOT in the vault (repo root; harness auto-load)
2. `Think/0 - Projects/Cobalt/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`
3. `…/40 - DevDocs/reports/cto-<date>.md` — last line only (step 0)
4. `Think/6 - Permanent/Memory/INDEX.md`
5. `Think/6 - Permanent/Memory/areas/cobalt.md` — `## NOW`
6. `Think/6 - Permanent/Memory/topics/cto-desk-contract.md`
7. `Think/6 - Permanent/Memory/preferences.md`
8. `Think/6 - Permanent/Memory/LAWS.md`
9. `…/40 - DevDocs/prompts/<today>/` — listing
10. `…/40 - DevDocs/reports/cto-<today>.md` — §0, §4 after HANDOVER, §5 CURRENT
11. `…/40 - DevDocs/reports/day-open-<today>.md`
12. `git log --oneline -5` — not a file
13. `…/00 - Project/SPRINT-LADDER-v0_1.md` — glance + current sprint
14. `…/40 - DevDocs/reports/cto-<previous day>.md` — step 8 grep (plus today's again)
15. `…/40 - DevDocs/reports/close-<latest>.md` — Laws fold list
16. each live hub's `…/40 - DevDocs/reports/<hub>.md` — §0, last 15, grep
Most turns, not wake-up: `…/40 - DevDocs/SESSION-CLOSE.md`, `…/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md`. Retrieval only: `Memory/topics/cto-desk.md`.

| T2 | 18:43 EDT | "The way I wanted the memory to work is uh, Claude.md, agents.md, quen.md, and any other um, startup uh, markdowns for the agent were supposed to say point to memory and read the other memory files in permanent memory and follow the structure in there. What I see here is a substantial amount of data in Claude.md file that completely overlaps stuff that is in other files. Can you check for overlaps? Specifically the last section, I think it talks about laws, about the way of communication and everything else. And I think all that is in other files. And if it's not, it should be sitting in other files. So any other agent that ever starts uh, should be able to traverse the documentation and understand all this information, not just Claude." | Design intent: every startup file (CLAUDE.md, AGENTS.md, QWEN.md, any other) is a POINTER to memory only; everything else lives in memory / the vault, reachable by any house. Audit below. |

### File 1 audit — `~/cobalt/CLAUDE.md` (16,590 B) vs memory
Found first: AGENTS.md and QWEN.md both open with "Read `CLAUDE.md` for the repository operating contract" — the design is inverted: every house is routed THROUGH CLAUDE.md, and CLAUDE.md is not in the vault. Always-loaded block (INDEX+profile+preferences) = 3,919 / 4,000 chars — preferences.md has no room; moved content needs its own linked file.

| CLAUDE.md section | ≈bytes | already in | verdict |
|---|---|---|---|
| Memory pointer + ledger paragraph | 1,300 | AGENTS.md, QWEN.md (verbatim), INDEX, LAWS preamble | KEEP as the stub. STALE: "Never write directly to the vault; the hub performs the authorized fold" contradicts L58 (the DESK is the only writer; the close hub proposes) |
| What Cobalt is | 450 | `areas/cobalt.md` "What Cobalt is (one screen)" | DUPLICATE — delete |
| Absolute boundaries | 1,050 | platforms/never trade: `areas/cobalt.md`; secrets: L4; HITL: L7; commits vs reads: L44 | PARTLY NEW: "never commit vault contents / gitignored material" and "extracted figures require verbatim source quotes" are in no memory file → move |
| Working rules | 1,500 | Pydantic/config: L1 L10; routing: L5; L46; 3-tries: `areas/cobalt-houses.md`; ADR: `areas/cobalt.md` | PARTLY NEW: tools-fetch-agents-reason, PDD + DevDocs per .py, backlog/kanban, local-model token conservation → move |
| NN#16 production is sacred | 1,450 | L28 (live vault/DB never a test target), L43, L54, L66 cover deploy; "NN#16" only cited by name | MOSTLY NEW: prod/dev definitions, `~/dev-vault-cobalt`, smoke-test acceptance, rollback-must-work → move |
| Environment facts | 3,900 | `topics/devices.md` (host, Tailscale, Qwen, OrbStack, `COBALT_VAULT_PATH`); `topics/memory-system.md` (Hippocampus) | PARTLY NEW: service ports/pgadmin, `cobalt.sh`, docs/ dual-purpose + config.yaml dead key, stale `cobalt_master_context.txt`, destructive utilities lacking prod guards, `_hilt_` naming → move |
| Documentation standard (D6) | 2,700 | `docs/PLACEMENT.md` (in vault) covers plans/reports/incidents/_inflight but DEFERS the D6 tiers back to CLAUDE.md | MOVE whole into PLACEMENT.md |
| Current phase / strangler / config boundary | 2,000 | TRIAGE.md named in `areas/cobalt.md` | NEW: strangler rules + config-boundary law in no memory file → move |
| Cross-cutting laws (from TRIAGE) | 1,300 | LAWS L1–L11 | DUPLICATE — delete. STALE: "Planning hard cap" = L12, RETIRED 2026-09-22 |
| Communication style | 350 | `preferences.md` lines 1, 4 | DUPLICATE — delete |
| Report discipline (09-09) | 350 | no memory file | NEW → move. CONFLICT: "one ruling per message" vs `preferences.md` "rulings up to ten per message" (09-13) vs wake-up "5–10 sentences, one A/B per message" — his call |
| Vault delivery | 250 | `docs/PLACEMENT.md` `_inflight` rule | DUPLICATE pointer — delete |
| Session hygiene (09-06) · Capture hygiene (09-10) | 550 | `preferences.md` "SESSION fresh" (partial); LAWS "Not law" says these were MOVED TO CLAUDE.md (O15) | CLAUDE.md is their home BY RULING → move to memory AND the LAWS "Not law" pointer changes (LAWS text = his ruling via desk) |

Proposed shape (for his review, nothing applied): CLAUDE.md = AGENTS.md = QWEN.md = one identical ≈1 KB stub (memory pointer only, L58-correct wording); the NEW/moved content goes to ONE new memory file `areas/cobalt-build-rules.md` (boundaries, working rules, NN#16, strangler + config boundary, report/session/capture hygiene) linked from INDEX, plus environment facts → `topics/devices.md`, D6 tiers → `docs/PLACEMENT.md`. CLAUDE.md 16,590 → ≈1,000 B for every house, every session.

| T3 | 18:47 EDT | "No, that's that's great, but what I want is I want Claude.md, agents.md, quen.md, and any other .md that starts the agent to say go read cobalt.md. And all of this should sit in cobalt.md. And 10, ten uh, messages per ruling is my latest. So Claude is outdated. Claude.md is outdated. What I want is any ruling or anything that sits in Claude.md that is overruled in other files in the memory should disappear and what's in the memory should be what is uh, re re um, retained." | (1) Every startup file (CLAUDE.md, AGENTS.md, QWEN.md, `.clinerules`) = one pointer: read `areas/cobalt.md`. (2) Everything CLAUDE.md holds that memory lacks moves INTO `areas/cobalt.md`. (3) Memory wins: a CLAUDE.md line overruled by memory is dropped, not carried. (4) "ten … per ruling" read as preferences.md's "rulings up to ten per message" (09-13) — desk reading of his wording. Sets aside the LAWS preamble's wake-up path (CLAUDE/AGENTS/QWEN → INDEX → LAWS), L73: his direct instruction = the override; recorded. Apply text: FOR THE DESK A1–A9. |

| T4 | 18:54 EDT | "No, there's a couple of things I want to make sure that we don't do here. I don't want to do a lobotomy. So basically, I, I want to make sure that the traversal path that you described is absolutely correct. And all of the 16 files that were read, we still read all the necessary uh, information that is needed to start. But we remove all the duplicates and we make sure the right data is in the right place. For example, you're mentioning laws multiple times here, and there are laws in Claude.md, and I think we're moving laws now into Cobalt.md. None of that should be in any of those files. Laws should only exist in laws, no other place. And the other parts of the future cobalt.md should also be like that. If something exists in a memory, in a, in a permanent memory files that can be traversed by index, should not sit in cobalt.md, should not sit in any of the other files that are starting the agents." | (1) No lobotomy: every file keeps reaching what a start needs; traversal verified. (2) Laws live ONLY in LAWS.md — no law text or `L<n>` restatement in cobalt.md or any startup file. (3) One home per fact: anything in an INDEX-reachable memory file is not repeated in cobalt.md or a startup file. Applied: A5 → A5r, A7 → A7r, new A8r (INDEX gap), OPEN on existing cobalt.md law lines. |

| T5 | 19:0x EDT (read 19:04) | "So I want to make these files extremely lean and nothing is going to stay in the files that is being read and using tokens. So what we're going to do is you and I are working on a project. We're making a proposal for the tribunal that is going to completely redesign the startup prompt. So what I want you to do is start building in your um, area where you're building the uh, files for the proposal. Start building what the new files should look like and start building the report of what we're changing and why we're changing it. We're going to send that proposal to the tribunal once we're done, but we're going to go through all 16 files and make sure everything is put in the right place and also make sure that everything is lean and there is no extra word that does not need to be in there at all. In any of the files. Everything that is not supposed to be in those files, including strike lines, moves out of them and into whatever files we want to create that keep the retired lines. They don't need to be deleted, but they never ever need to be read by anything other than if we want to reference old files. And yes, if you notice that something is missing in index, that is a big deal because index is the most important file that tells everything how to traverse the memory." | (1) The sitting output is a TRIBUNAL PROPOSAL (L67: one house proposes, the tribunal rules), built in `docs/40 - DevDocs/plans/startup-redesign-2026-09-27/` (`PROPOSAL.md` + `new/` + `retired/`). Sets aside `53`'s "write only your own report" limit — his direct instruction (L73). (2) All 16 read items reviewed; no extra word. (3) Struck / superseded / non-start lines move to `_retired/<file>.md`: kept, never read at start — this changes L58's "supersede by strike" (law change, carried in PROPOSAL "Law changes"). (4) INDEX completeness is priority: the preferences/profile gap is fixed in `new/INDEX.md`. The T4 OPEN (strike vs remove the two law lines) is settled by (3): moved to `retired/cobalt.md`. |

| T6 | 19:36 EDT | "No, you're gonna call those in your proposal proposed Claude that dot MD pl proposed agent dot MD proposed Quen dot MD and so on and so forth. So when we're ready to move them and replace the files that are going to be live files, then we rename them to the correct naming convention." | Drafts named `proposed-<live name>` in the proposal folder root (`new/`, `retired/` removed): `proposed-CLAUDE.md`, `proposed-AGENTS.md`, `proposed-QWEN.md`, `proposed-clinerules`, `proposed-INDEX.md`, `proposed-cobalt.md`, `proposed-_retired-cobalt.md`; renamed to live names only at apply. Renames done with `mv` / `sed` / `rm` / `rmdir` inside the proposal folder only — outside `53`'s read-command list, on his instruction (L73). |

| T7 | 19:39 EDT | "Not yet. What I want to do now is we just move stuff around and I want to understand how many bytes did we remove from the path now so the startup routine would never read them and how many uh, removed lines means how many removed tokens from the startup routine. Also, assume that I will strike out the law that says that all the uh, lines that are changed need to be striked out and I will create another law that says they need to be moved to an appropriate history file that holds the data so we don't lose it but the live file does not have those tokens in the read section." | (1) Moves only for now; savings measured (PROPOSAL "Removed from the start path so far": desk −15,977 B gross ≈ −3,994 tokens). (2) Draft ASSUMING his law change: L58's strike rule struck; new law = changed lines move to the source's history file, never in a live read path. Not yet law — his ruling at fold (L58); carried in PROPOSAL "Law changes". |

| T8 | 19:43 EDT | "Now I want to go through new proposed Claude.md that got so big with all this stuff and I want to see paragraph by paragraph how can we reword each paragraph to be two to three times smaller and simpler but still say the same thing without overloaded amount of text." | Desk reading: "proposed Claude.md that got so big" = `proposed-cobalt.md` (proposed-CLAUDE.md is the 126 B pointer). Reworded per section, v1 5,217 → v3 3,410 B (v1 copy: job tmp). Content per section 1.4–2.4× smaller; the fixed cost is the per-line `[stated …]` tag (660 B) — L58 / INDEX rule 2, his call. Meaning cuts listed to him for veto. |

| T9 | 19:54 EDT | "Let's do A on a proposed file and now calculate, including everything that we just did, how much are we cutting off the startup? You said 3% initially, what are we at now?" | A applied in `proposed-cobalt.md` only (3,410 → 3,107 B): section-heading tags, date = latest `≤` when a section mixes dates of one origin (desk reading). Law change (L58 / INDEX rule 2) carried in PROPOSAL. Savings: desk −18,087 B gross / −17,381 net ≈ −4,345 tokens = 3.2% of 136,059 (5.8% of file bytes). |

| T10 | 20:08 EDT | "Okay, I'm reading CTO desk wake up and immediately the first section CTO dash desk dash wake up is overly verbose. It should literally be an instruction. There should be no discussion and information here. on when and what time something was ruled. […] if it's a law it should be in laws why is it in here then […] meter anthropic small this sits writes memory at prompts file only so that part is also not correct because desk is the only one that can actually execute commands and execute stuff or am i missing something if you reread the laws and rules am i missing something" (full message: chat 20:0x) | Rule for every prompt file: instruction only — no ruling dates, quotes or reasons (record = `cto-<date>.md` §4), no law text (LAWS). Header rewritten in `proposed-CTO-DESK-WAKEUP.md` 1,571 → 749 B. Checked against LAWS: nothing removed was needed to act — L19 keeps the MODEL tag, L63's dialog deny is on the launch line itself, L64's two exposures are launch step 2 + 3. "writes memory and prompt files only" confirmed wrong and dropped. |

| T11 | 20:15 EDT | "The idea here is that my Cobalt and the CTO desk as well, which is a development arm of Cobalt, should be uh, vendor agnostic. So I'm okay with you stating meter Anthropic on the first line. […] in the future, I may decide to use Codex and one of their models, or Grok and one of their models, in which case I'm not sure if just the model or model and vendor, which is your meter, I guess. would need to be changed on my ruling. […] is there anywhere else that a Claude as a vendor in this part is mentioned? […] we can look at handover section. And first, I want to understand how much of this is the first time information that is needed here, and how much of this is actually a overly verbose addition or repeating of stuff" (full message: chat 20:1x) | Principle: Cobalt and the desk are vendor-agnostic; a vendor switch is his ruling. Vendor-bound text inventoried (PROPOSAL Open) — seven places, not only `claude --bg`; SEAT PROFILE A/B to him. STEP 0 reviewed: ≈45% repeat (L64 ×2, contract H5, dates) → 1,724 → 867 B in `proposed-CTO-DESK-WAKEUP.md`; kept one line found nowhere else ("never write through the vault symlink"). |

| T12 | 20:20 EDT | "Yes, let's choose A and uh, re, uh, redraft the file. And I think at this point we are good with the second file. So how much did we save off of the startup routine now from the top to bottom? You said we were at 5%. Where are we now?" | A (SEAT PROFILE) chosen; `proposed-CTO-DESK-WAKEUP.md` redrafted whole 13,102 → 5,585 B; file 2 closed by him. Content changes (a)–(e) listed in PROPOSAL row 2 for his veto — (a) is P1, now in the draft. Total so far ≈135,293 B off the path = 24.9% of 136,059 tokens (÷4). |

| T13 | 20:27 EDT | "I'm not done with this file. […] is this order needed? Or does this order already happen if you read the index file […] Can we go back and make sure that that file is not losing any context and that we're not losing any intent and everything is still going to be read, but we're just not repeating and reading words ad nauseum to create extremely verbose files." (full message: chat 20:2x) | File 2 re-opened. Clause-by-clause trace written (PROPOSAL "Trace — CTO-DESK-WAKEUP.md", every clause → KEPT / HOME / CARRY / OUT). Five intents found dropped and restored in the draft: title "no day state here", LIST `--all` for the death check, "desk reading" for an unsettled close wording, "never by the clock", LAWS-entry pointer. Draft 5,585 → 5,749 B. |

| T14 | 20:31 EDT | "File two is done. Next file." | File 2 closed. File 3 (HANDOVER last line): 1,655 → 66 B; the line carried §5 CURRENT's plan + contract rules; REFRESH (6) in `proposed-CTO-DESK-WAKEUP.md` now pins the shape. |

| T15 | 20:36 EDT | "Yeah, let's go to CTO desk contract.md." | File 6 drafted: `proposed-cto-desk-contract.md` 14,553 → 9,051 B; old file snapshot → `proposed-_retired-cto-desk-contract.md`; the wake-up's CARRY items land here. Cut list in PROPOSAL row 6. |

| T16 | 20:40 EDT | "No, we don't want a desk skipping it. We just want to remove clutter. We don't want to remove the meaning or the useful information. So A is appropriate as you recommended. What's next?" | A: the checklist stays in the wake-up read (contract whole). Principle: remove clutter, never meaning or useful information. File 7 drafted: `proposed-preferences.md` 1,456 → 910 B; build-firewall rule restored inline. |

| T17 | 20:48 EDT | "Yes, let's start on it. And I only want to see laws and meaning in them. And any citations, dates, and wording need to move into a history file so they're retained and not lost, but not in a path of reading." | `proposed-LAWS.md` 89,839 → 40,588 B, laws + meaning only; the whole live file verbatim → `proposed-_history-LAWS-2026-09-27.md` for LAWS-HISTORY. FROZEN routing laws kept verbatim (tags / citations / notes out only). Three wording changes + the L75 vs ten-per-message conflict listed for his check (PROPOSAL row 8, Open). Total so far ≈192 KB off the wake-up read ≈ 35% of 136,059 tokens. |

| T18 | 20:56 EDT | "So we do want to retain the meaning and the L6, the bot pattern names, Hermes Agent, BuzzBot, GrokBot, they were the meaning of what I am trying to do. […] other laws uh, that you've checked and changed, I am okay with. As far as my ruling of one per message, I do want to change that to 10 per message. So if the ruling says one per message, we need to change it here and remove it from anywhere else where it says that. It should be in one place only […] I also want to create a short proposal as to how do we write only in right places for the right items […] How do we instruct anybody that writes into these processes to not be overly verbose and not quote and citate and put dates […] And how do we tell anybody that is amending or writing wake up routine to be very precise, very short and clear with fully retaining the meaning but removing overly verbose clutter." (full message: chat 20:5x) | (1) L6 names restored. (2) L50 / L36 wordings approved. (3) L75 "one per message" struck — the count lives only in preferences ("up to ten") — law change, his ruling. P4 clarified (a second approval list waits for the first; not a per-message count). (4) WHERE + HOW rules drafted as one file `proposed-writing-rules.md` → `topics/writing-rules.md`, INDEX rule 7 + start line; always-loaded 3,149 chars. |

| T19 | 21:06 EDT | "Yes, let's go to the next item." | §4 rows (row shapes in wake-up RULINGS, 19,443 → ≈3,500 est.), day-open (VERDICT only, 5,800 → 741), hub-report reads (7,860 → 1,821 per hub). Wake-up +492 B named. Total ≈218.5 KB off ≈ 40% of 136,059 tokens (÷4). Next: SESSION-CLOSE.md, UNATTENDED-LAUNCH.md. |

| T20 | 21:11 EDT | "Before we go to those files, for the section four rows and they open report, uh, are we applying the same rules that we are going to ask the next desk or the next agent writing to write in a clear concise manner and remove any verbatim any quotes anything that is not a direction so the desk is left to read what is important and not uh, read the quotation and history if there is a need for quotation and history needs to go in history But I really don't ever want to see no words of his or anything like that if we ruled and worded it's in there it doesn't need to be stated all the time" | Same rules everywhere on the read path. §4 row = direction or fact + status only; his words verbatim → `reports/cto-<date>-words.md` (history, not read at wake-up). Absence statements banned. Every prompt card names [[writing-rules]] for its report. Applied in `proposed-CTO-DESK-WAKEUP.md` (RULINGS, RECONCILE), `proposed-writing-rules.md`, `proposed-cto-desk-contract.md`. |

| T21 | 21:15 EDT | "No, go to, go with the next files." | SESSION-CLOSE.md 5,382 → 3,149 B (five stale-against-law items fixed, runner column added, lessons gate re-keyed to `→ <rule id>`); UNATTENDED-LAUNCH.md 8,383 → 5,498 B (history out, facts kept, per-message fixed). Originals snapshotted. |

| T22 | 21:19 EDT | "Yes, please." | FOR THE DESK = the ordered apply list (19 steps, history first, wake-up last, gated on the tribunal's derive + his approval). `TRIBUNAL-SUMMARY.md` (3,245 B) written in the proposal folder for the L67 new-design seats. |

| T23 | 21:28 EDT | "if we went through all the files what i want you to also put in a proposal and what the tribunal needs to answer is with the set of files that are in front of us if any other house takes over the CTO desk would it be able to easily traverse the memory understand what's going on and move forward like nothing changed […] nothing ambiguous that would completely confuse lower level models […] this is going to be the memory structure we're moving forward with for the Cobalt. Under which many different house agents are going to run. Including local Quen. […] currently, I am a manually running Quen every morning. I am giving it a manual prompt. And it runs the morning report. We need it to move towards this being automated and we need it to move towards Quen being able to run a lot more than what it's doing now" (full message: chat 21:2x) | Four tribunal questions added (portability to any house, clarity for lower-tier models, Cobalt-wide structure, right way) with the proposer's known gap (SEAT PROFILE Anthropic-only). INDEX LAWS line de-ambiguated for card seats (L59). Qwen: current state recorded (manual start + manual prompt); stale text listed (QWEN.md, DAY-OPEN-QWEN.md S1–S7, cobalt-houses:18); direction = scheduled deterministic day-open + headless Qwen verdict (a build, needs his ladder ruling), wider read-and-judge work inside L49, composing work only via the routing tribunal. |

| T24 | 21:37 EDT | "Now, it will be its own lane and we don't need to worry about it. I just want to make sure that when we're uh, going with a proposal in front of the tribunal, we may make sure that everything is appropriate, including the small models. For the not yet part, as far as some functions are not there, I want to also have the tribunal state how would desk work under their functionality so which parts are there to replace the parts that we have currently i'm pretty sure that every other model and every other vendor can uh instantiate and run herder tabs and can instantiate and run any other vendors model in a new herder tab. What you're talking about is a remote control and a front end which if we have Cobalt which is the future front end does not really matter. If Cobalt is the front end then all the models are running within the Cobalt. And we don't have the worry of remote control because COBOL runs on all of my devices through TailScale and I have no issues with needing a remote control session again." | Qwen automation = its own lane (out of this proposal; kept as context). Tribunal question 5: each house maps every SEAT PROFILE verb to its own command or names the gap; frame = herdr tabs for any vendor, WAIT already vendor-free, remote control replaced by Cobalt as front end over Tailscale (L64 amendment later, his ruling). |

| T25 | 21:45 EDT | "ok closed" | Sitting closed. Report final; the desk launches the tribunal and applies FOR THE DESK after the derive + his approval. |

### CLAUDE.md lines dropped because memory overrules them (T3 (3))
| CLAUDE.md line | overruled by |
|---|---|
| "Never write directly to the vault; the hub performs the authorized fold" | L58 (desk is the only writer; close hub proposes) |
| "Replies to Dejan ≤10 lines, one ruling per message" | `preferences.md` "rulings up to ten per message" (09-13) + T3 |
| "Planning hard cap: remaining design work fits two calendar weeks" | L12 RETIRED 2026-09-22 |
| "one-command rollback to the previous tag must always work" | L54 (revert the merge range, never `reset --hard` to a tag) |
| "Deploy outside market hours only" | L43 / L66 (the 20:00–21:00 pause) |
| "tokenized HITL approval pattern" | L7 (no token exists; chat "approve" for a named action, sha256) |
| "delegate mundane/repetitive coding to the local model" | L49 (local seat reads and judges, never composes, no source code) |
| "Commit continuously to git/GitHub" (push implied) | L55 (push only on his word) |
| "Cross-cutting laws" block L1–L11 | LAWS L1–L11 (duplicate) |
| "What Cobalt is", "Communication style", local model / host / Tailscale / OrbStack / vault-path facts | `areas/cobalt.md`, `preferences.md`, `topics/devices.md` (duplicate) |
| QWEN.md "Morning command" section | `prompts/DAY-OPEN-QWEN.md` (duplicate) |
| `.clinerules` "Senior SRE Persona" (2,449 B, commit `4f44d94c`) | Cline retired (`areas/cobalt.md` Predecessor) |

## Writing rules
Drafted (T18): `docs/40 - DevDocs/plans/startup-redesign-2026-09-27/proposed-writing-rules.md` — WHERE (one home per fact) + HOW (lean, meaning kept) + real before → after examples.

## FOR THE DESK
The ordered apply list (T22). GATE: nothing is applied before the tribunal's derive (L67: Fable · Astra · Grok, new design) and his ONE approval of it; never during a running deploy; the desk applies, a hub proposes nothing here. Source folder `P` = `docs/40 - DevDocs/plans/startup-redesign-2026-09-27/`; `M` = `/Users/cobalt/Vault/Think/6 - Permanent/Memory/`. Every step: `wc -c` before and after, recorded.

| # | action | from → to | ruling |
|---|---|---|---|
| 0 | One-time check: in the last two `cto-<date>.md`, no row is APPROVED without `APPLIED:` other than launch / record rows (the new grep finds only `APPROVED — pending fold`) | read | T12 (a) |
| 1 | History first — append verbatim | `P/proposed-_history-LAWS-2026-09-27.md` → end of `M/LAWS-HISTORY.md` | T17 |
| 2 | Create `M/_retired/`; write verbatim | `P/proposed-_retired-cobalt.md` → `M/_retired/cobalt.md`; `…-cto-desk-contract.md` → `M/_retired/cto-desk-contract.md`; `…-preferences.md` → `M/_retired/preferences.md` | T5, T7 |
| 3 | Archive the repo originals | `P/proposed-_retired-SESSION-CLOSE.md`, `…-UNATTENDED-LAUNCH.md` → `docs/_archive/startup-redesign-2026-09-27/` (CLAUDE.md, AGENTS.md, QWEN.md, .clinerules: git history holds them) | T5 |
| 4 | LAWS (his law changes: preamble path, L58, L75, the laws-only text) | `P/proposed-LAWS.md` → `M/LAWS.md` (whole file) | T3, T7, T9, T17, T18 |
| 5 | INDEX | `P/proposed-INDEX.md` → `M/INDEX.md` | T4, T5, T18 |
| 6 | preferences | `P/proposed-preferences.md` → `M/preferences.md` | T16 |
| 7 | writing rules (new) | `P/proposed-writing-rules.md` → `M/topics/writing-rules.md` | T18, T20 |
| 8 | cobalt.md — paste the live `## NOW` text into the `«snapshot …»` line | `P/proposed-cobalt.md` → `M/areas/cobalt.md` | T3, T4, T8, T9 |
| 9 | desk contract | `P/proposed-cto-desk-contract.md` → `M/topics/cto-desk-contract.md` | T15, T16, T21 |
| 10 | devices — append one line | `M/topics/devices.md` += `- [stated ≤2026-08-31 · CLAUDE.md] docker-compose on OrbStack: db pgvector/pg16 :5432 (bind mount \`./data/postgres\` — never inventory or commit), pgadmin :18080, Mattermost :8065. LaunchAgents captured in \`ops/\`: \`com.cobalt.agent\` (\`cobalt.sh start\`), \`com.cobalt.mainframe\`. Runner \`uv\`, tests \`pytest\`, processes \`cobalt.sh start\|stop\|restart\|status\`.` | T4 |
| 11 | trading-copilot-os — append the Predecessor line | `M/_retired/cobalt.md` "moved to its subject file" line → `M/areas/trading-copilot-os.md` | T4 |
| 12 | cobalt-houses line 26 — move the line to `M/_retired/cobalt-houses.md`; write it back without "; every house wakes via CLAUDE.md / AGENTS.md / QWEN.md → INDEX → STATUS → LAWS" | `M/areas/cobalt-houses.md` | T3, T7 |
| 13 | PLACEMENT — lines 6, 9, 22, 48: `CLAUDE.md's Documentation standard` / `CLAUDE.md-governed` → `` `areas/cobalt.md` `## Docs tree` `` / `` `areas/cobalt.md`-governed `` | `docs/PLACEMENT.md` | T3 |
| 14 | close + launch standards | `P/proposed-SESSION-CLOSE.md` → `docs/40 - DevDocs/SESSION-CLOSE.md`; `P/proposed-UNATTENDED-LAUNCH.md` → `docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md` | T21 |
| 15 | startup files | `P/proposed-CLAUDE.md` → `~/cobalt/CLAUDE.md`; `…-AGENTS.md` → `AGENTS.md`; `…-QWEN.md` → `QWEN.md`; `P/proposed-clinerules` → `.clinerules` | T3, T6 |
| 16 | wake-up — LAST, so the desk's next refresh boots on the new set | `P/proposed-CTO-DESK-WAKEUP.md` → `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` | T10–T14, T19, T20 |
| 17 | Measure: always-loaded (`wc -c` INDEX + profile + preferences < 4,000); one commit with pathspecs for the repo files (docs + root; no restart — docs only, L42); push only on his word | `~/cobalt` | L55 |
| 18 | Verify: the next desk REFRESH; its first §5 row logs its wake-up MEASURE against 136,059 | the successor's report | T1 |

Superseded draft (A1–A9, T3–T4), kept as the record of the first pass:

A1–A4 (T3) — replace the WHOLE file with the stub; `<name>` = the file's own name. Files: `~/cobalt/CLAUDE.md` (16,590 →≈330 B), `~/cobalt/AGENTS.md` (1,208 →), `~/cobalt/QWEN.md` (1,879 →), `~/cobalt/.clinerules` (2,449 →).
```
# <name> — Cobalt

Read `/Users/cobalt/Vault/Think/6 - Permanent/Memory/areas/cobalt.md` and follow its `## Start here`. Everything an agent needs is in that memory folder; this file holds nothing else.
```

A5 — SUPERSEDED by A5r (T4): the draft below restated laws and memory; kept only as the before-state of T4.
```
## Start here (every house)
- [stated 2026-09-27 · Dejan] Every startup file points here. Read `## NOW` below, then [[INDEX]], then [[LAWS]] (in full per L59; read-and-judge seats get a card); open any other file when the task asks. Memory wins over any other file; a conflict is reported with both paths, never guessed.
- [stated 2026-09-13 · Dejan] [[LAWS]] is the only current law; `PROJECT-LEDGER.md` is the dated record; a ruling is law only once folded. The desk alone writes memory and LAWS (L58); every other agent proposes by `MEMORY:` / `RULING:` lines in its own report. Dejan rules; an unresolved law disagreement is an OPEN item, never a vote. Missing or contradictory law → report the exact path and issue.
```
```
## Boundaries (never)
- [stated ≤2026-08-22 · CLAUDE.md] Never touch or integrate a trading platform (DAS Trader Pro, Lightspeed, TradeStation, CenterPoint) — read-only awareness; never execute or automate a trade.
- [stated ≤2026-08-22 · CLAUDE.md] Never commit vault contents, credentials or gitignored material (commits, not reads — L44); secrets L4; trading-logic and risky actions behind L7; every extracted figure carries its verbatim source quote.
## Build rules
- [stated ≤2026-08-22 · CLAUDE.md] Python; Pydantic for all structured data; Postgres + pgvector; rotating logs; config-driven agents (configs/ + prompt templates), schemas that extend to swing and options without refactor (L10, L16).
- [stated ≤2026-08-22 · CLAUDE.md] Tools fetch, agents reason: deterministic collectors, LLMs only on cached validated data, every number from code (L2, L9, L57); every LLM call routed (L5).
- [stated ≤2026-08-22 · CLAUDE.md] Sprint close = tests + architecture review; ADR per decision, PDD per module, one DevDocs file per .py (agent-authored; the symbol-check gate accepts, 2026-09-10); `docs/00 - Project/BACKLOG.md` kept current; never build far ahead of test and approval.
- [stated ≤2026-09-13 · CLAUDE.md] Small commits; one run, one commit (L46); push on his word only (L55). Three fails by one model → next tier; right house per task (L21, L26, L67).
- [stated ≤2026-08-22 · CLAUDE.md] Read `docs/20 - Assessment/TRIAGE.md` before build or design, `docs/00 - Project/COBALT-REQUIREMENTS.md` before planning.
## Production is sacred (NN#16)
- [stated 2026-08-31 · CLAUDE.md] Prod = the running install + live Postgres + the live vault `/Users/cobalt/Vault/Think`, reached only through each prod process's explicit `COBALT_VAULT_PATH`. Dev = a worktree (L54) + `cobalt_dev` (L76) + `~/dev-vault-cobalt` (templates + Rules.md; `configs/dev/vault.yaml`'s committed default, so a bare `uv run` never lands in the real vault) + `configs/dev` + the dev Mattermost token. Never develop against prod (L28).
- [stated ≤2026-08-22 · CLAUDE.md] Sprint acceptance = smoke test of ALL delivered functionality; red = not done. Sprints ordered by income impact; each adds capability, none takes the agent down. Deploy shape, window, rollback: L43, L54, L66, L68.
## Strangler rebuild
- [stated 2026-08-22 · CLAUDE.md] Old tree untouched and runnable; KILL code dies in place; new work only in `src/cobalt/` (typed, config-driven, fail-loud, tested); build work never touches prod DB, prod vault or the running agent. KEEP-AS-IS ports through the test/config gate; KEEP-CONCEPT/REBUILD rebuilt with old code as spec; REDESIGN needs its ADR first (TRIAGE).
- [stated 2026-08-28 · CLAUDE.md] Config boundary: new-core config only under `configs/dev/`, `configs/cobalt/` or `src/cobalt/`, never `configs/*.yaml` (the old loader's top-level glob); check with `git check-ignore` / a glob BEFORE adding a file (2026-08-25 incident, BACKLOG).
## Docs tree (D6)
- [stated 2026-09-13 · CLAUDE.md] `docs/` = the vault's `0 - Projects/Cobalt`; gitignored by default, one carve-out per numbered folder, never widened. Tiers: 00 Project (BACKLOG, REQUIREMENTS, LEDGER) · 10 Decisions (ADRs) · 20 Assessment (frozen + TRIAGE) · 30 Design · 40 DevDocs (wiki, plans, reports, prompts, incidents — `docs/PLACEMENT.md`) · 50 Roles · 90 References (`assets/` licensed, never committed) · `_archive` (nothing under docs/ is deleted) · `_inflight` (README-only). Every new markdown files into a tier; at repo root only CLAUDE.md, AGENTS.md, QWEN.md, README.md (+ the `COBALT-REQUIREMENTS.md` redirect stub).
- [stated 2026-08-31 · CLAUDE.md] Never committed, out of scope until the old tree's writers retire: `docs/60 - Agent Output/` (old scheduler's briefings) and `docs/0 - Projects/`.
## Hygiene
- [stated 2026-09-09 · CLAUDE.md] Report shape: §0 Headline ≤5 lines (what changed, status, ESCALATE count) → tables → ESCALATE; no restated prompt, no narration, no section without a fact or verdict. Replies to him: [[preferences]].
- [stated 2026-09-06 · CLAUDE.md] Never rely on restore — state to the vault/DB before `/clear` (the desk refreshes by HANDOVER, L64); never paste into an auto-mode pane without a text instruction; prompts carry paths and rulings, not contents. Every document he reads sits in the vault (`docs/PLACEMENT.md` `_inflight`).
- [stated 2026-09-10 · CLAUDE.md] Reviewer captures and Codex logs never enter a commit (`_inflight/*.log` gitignored).
## Repo facts
- [stated ≤2026-08-31 · CLAUDE.md] Services (docker-compose on OrbStack): db pgvector/pg16 :5432 (bind mount `./data/postgres` — never inventory or commit), pgadmin :18080, Mattermost :8065; LaunchAgents captured in `ops/`: `com.cobalt.agent` (`cobalt.sh start`), `com.cobalt.mainframe`. Runner `uv`, tests `pytest`, processes `cobalt.sh start|stop|restart|status`.
- [stated 2026-08-31 · CLAUDE.md] Old-tree config: a SystemConfig field with a `validation_alias` (`obsidian_vault_path`, `briefing_inbox_dir`) takes .env/env only — its `configs/config.yaml` key is dead; `scribe.py` has a third resolution path. PostgresMemory methods say `_hilt_`, the schema `hitl_` — log, don't fix.
- [stated ≤2026-08-31 · CLAUDE.md] `cobalt_master_context.txt` is a stale February snapshot (regenerate with `dev_utils/generate_context.py`); `dev_utils/wipe_memory.py` and `reset_memory_table.py` lack prod guards — never run them.
```

A5r (T4) — ZERO-DUPLICATE placement. Rule applied: a line goes to the ONE file whose subject it is; it names no law and repeats nothing another INDEX-reachable file holds. Checked by grep over `6 - Permanent/Memory/` (18:5x): each line below had no home.
`areas/cobalt.md` — insert ABOVE `## NOW`:
```
## Start here (every house)
- [stated 2026-09-27 · Dejan] Every startup file points here. Read `## NOW` below, then [[INDEX]] and follow it.
```
`areas/cobalt.md` — new sections after `## What Cobalt is (one screen)`:
```
## Build rules
- [stated ≤2026-08-22 · CLAUDE.md] Stack: Python; Postgres + pgvector; rotating logs; agents config-driven (configs/ + prompt templates); schemas and pipelines extend to swing and options without refactor.
- [stated ≤2026-08-22 · CLAUDE.md] LLMs work only on cached, validated data; deterministic collectors fetch; all numeric computation is code.
- [stated ≤2026-08-22 · CLAUDE.md] Sprint close: tests + architecture review; PDD per module; one DevDocs file per .py, agent-written, accepted by the symbol-check gate; `docs/00 - Project/BACKLOG.md` kept current; nothing built far ahead of test and approval.
- [stated ≤2026-08-22 · CLAUDE.md] A model that fails a task 3 times → the next tier up, never a loop.
- [stated ≤2026-08-22 · CLAUDE.md] Never commit vault contents, credentials or gitignored material. Every extracted figure carries its verbatim source quote.
- [stated ≤2026-08-22 · CLAUDE.md] Read `docs/20 - Assessment/TRIAGE.md` before build or design; `docs/00 - Project/COBALT-REQUIREMENTS.md` before planning.
## Production and dev (NN#16)
- [stated 2026-08-31 · CLAUDE.md] Prod = the running install + live Postgres + the live vault `/Users/cobalt/Vault/Think`, reached only through each prod process's explicit `COBALT_VAULT_PATH`. Dev = a worktree + `cobalt_dev` + `~/dev-vault-cobalt` (templates + Rules.md; the committed default of `configs/dev/vault.yaml`, so a bare `uv run` never lands in the real vault) + `configs/dev` + the dev Mattermost token.
- [stated ≤2026-08-22 · CLAUDE.md] Sprint acceptance = smoke test of ALL delivered functionality; red = not done. Sprints ordered by income impact; each adds capability, none takes the agent down.
## Strangler rebuild
- [stated 2026-08-22 · CLAUDE.md] Old tree untouched and runnable; KILL code dies in place; new work only in `src/cobalt/`; build work never touches the prod DB, prod vault or running agent. KEEP-AS-IS ports through the test/config gate; KEEP-CONCEPT/REBUILD rebuilt with old code as spec; REDESIGN needs its ADR first.
- [stated 2026-08-28 · CLAUDE.md] New-core config only under `configs/dev/`, `configs/cobalt/` or `src/cobalt/`, never `configs/*.yaml` (the old loader's top-level glob); check with `git check-ignore` / a glob BEFORE adding a file (2026-08-25 incident, BACKLOG).
## Docs tree (D6)
- [stated 2026-09-13 · CLAUDE.md] `docs/` = the vault's `0 - Projects/Cobalt`; gitignored by default, one carve-out per numbered folder, never widened. Tiers: 00 Project · 10 Decisions · 20 Assessment (frozen + TRIAGE) · 30 Design · 40 DevDocs (`docs/PLACEMENT.md` maps it) · 50 Roles · 90 References (`assets/` licensed, never committed) · `_archive` (nothing under docs/ deleted). Repo-root markdown: CLAUDE.md, AGENTS.md, QWEN.md, README.md, the `COBALT-REQUIREMENTS.md` stub.
- [stated 2026-08-31 · CLAUDE.md] Never committed, out of scope until the old tree's writers retire: `docs/60 - Agent Output/`, `docs/0 - Projects/`.
## Repo facts
- [stated 2026-08-31 · CLAUDE.md] Old-tree config: a SystemConfig field with a `validation_alias` (`obsidian_vault_path`, `briefing_inbox_dir`) reads .env/env only — its `configs/config.yaml` key is dead; `scribe.py` resolves a third way. PostgresMemory methods say `_hilt_`, the schema `hitl_` — log, don't fix.
- [stated ≤2026-08-31 · CLAUDE.md] `cobalt_master_context.txt` is a stale February snapshot (regenerate: `dev_utils/generate_context.py`). `dev_utils/wipe_memory.py` and `reset_memory_table.py` lack prod guards — never run.
```
`topics/devices.md` — append (subject: the host):
```
- [stated ≤2026-08-31 · CLAUDE.md] docker-compose on OrbStack: db pgvector/pg16 :5432 (bind mount `./data/postgres` — never inventory or commit), pgadmin :18080, Mattermost :8065. LaunchAgents captured in `ops/`: `com.cobalt.agent` (`cobalt.sh start`), `com.cobalt.mainframe`. Runner `uv`, tests `pytest`, processes `cobalt.sh start|stop|restart|status`.
```
`topics/working-contract.md` — append (subject: how agents work; its text leaves LAWS "Not law", A7r):
```
- [stated 2026-09-09 · CLAUDE.md] Report shape: §0 Headline ≤5 lines (what changed, status, ESCALATE count) → tables → ESCALATE; no restated prompt, no narration, no section without a fact or a verdict.
- [stated 2026-09-06 · CLAUDE.md] Never rely on restore: state to the vault/DB before `/clear`; never paste into an auto-mode pane without a text instruction; prompts carry paths and rulings, not contents.
- [stated 2026-09-10 · CLAUDE.md] Reviewer captures and Codex session logs never enter a commit (`_inflight/*.log` gitignored).
```
Dropped from the T3 draft as duplicates (T4): Start-here law paragraph (LAWS preamble, L58); Boundaries "trading platform" (`areas/cobalt.md` What Cobalt is); secrets / HITL / L44 refs (LAWS); Pydantic, ADR (`areas/cobalt.md` non-negotiables line); commit/push (LAWS); deploy shape (LAWS); vault delivery / `_inflight` (`docs/PLACEMENT.md`); every `L<n>` citation.
Size: cobalt.md +≈4,300 B (was +6,184 in A5); devices.md +≈330; working-contract.md +≈560.

A7r (T4) — `LAWS.md` line 444 (`**Moved to CLAUDE.md, not law (O15):** …`) → `**Not law, lives in [[working-contract]] (O15; moved from CLAUDE.md 2026-09-27, T3/T4):** session-state hygiene and capture hygiene / DevDocs authorship.` — the rule text leaves LAWS; replaced wording → LAWS-HISTORY.

A8r (T4) — TRAVERSAL GAP: `INDEX.md` lists neither `preferences.md` nor `profile.md` (only rule 4 names them), so a house following INDEX never reaches them; the desk reaches them only because its wake-up file names them. Add `- [[preferences]] · [[profile]] — how he works with agents; read at start` (+≈75 chars → ≈3,994 / 4,000; measure).

OPEN (T4) — existing law restatements already INSIDE `areas/cobalt.md`: the "non-negotiables in force … L23 … L29 (~~…~~ amended …)" line and the "user-data vs system-data law … L32" line. INDEX rule 3 says supersede by strike, never delete — a struck line still sits in the file and is still read. His call: strike (rule 3 as written) or remove them (the lines' history is in LAWS / LAWS-HISTORY).

A6 (T3) — `docs/PLACEMENT.md` lines 6, 9, 22, 48: `CLAUDE.md's Documentation standard` / `CLAUDE.md-governed` → `` `areas/cobalt.md` `## Docs tree` `` / `` `areas/cobalt.md`-governed ``.

A7 (T3) — `LAWS.md`: after line 21 (the verbatim MECHANISM quote, left as is) add `[amended 2026-09-27, desk-startup-tuning-2026-09-27.md T3] Wake-up path for every house: CLAUDE.md / AGENTS.md / QWEN.md / .clinerules → \`areas/cobalt.md\` \`## Start here\` → NOW → INDEX → LAWS.`; line 444 `**Moved to CLAUDE.md, not law (O15):** … applied directly to CLAUDE.md's operating contract, 09-13.` → same sentence with `CLAUDE.md` → `` `areas/cobalt.md` `## Hygiene` `` and a trailing `[amended 2026-09-27, T3]`; replaced wording → LAWS-HISTORY.

A8 (T3) — `INDEX.md` line `- [[cobalt#NOW]] — current state; read next, before LAWS [stated 2026-09-15 · Dejan]` → `- [[cobalt]] — start here: every house; NOW, then LAWS [stated 2026-09-27 · Dejan]` (always-loaded 3,919 chars; stays under 4,000 — measure after).

A9 (T3) — `areas/cobalt-houses.md:26`: strike `every house wakes via CLAUDE.md / AGENTS.md / QWEN.md → INDEX → STATUS → LAWS` (~~…~~) and append `(superseded 2026-09-27, T3: every startup file → [[cobalt]] Start here)`.

## CONTINUE
CLOSED 21:45 EDT (T25). Nothing to resume in this seat. The desk: launch the tribunal on `plans/startup-redesign-2026-09-27/TRIBUNAL-SUMMARY.md`; then FOR THE DESK steps 0–18. The Qwen day-open automation is its own lane (T24). History of this section below.
Proposal workspace: `docs/40 - DevDocs/plans/startup-redesign-2026-09-27/` (PROPOSAL.md = the change table; `proposed-<live name>` = drafts, renamed at apply). FOR THE DESK A1–A9 above are superseded by the proposal once the tribunal rules. Status 21:19: every read-path file drafted; FOR THE DESK ordered; TRIBUNAL-SUMMARY written. Next: his close of the sitting, or more review; the desk then launches the tribunal (L67) on `TRIBUNAL-SUMMARY.md` + the folder. (Earlier: his read of `proposed-INDEX.md` + `proposed-cobalt.md`; then file 2, CTO-DESK-WAKEUP.md — its plate line "one A/B per message" conflicts with T3 / preferences (ten per message).

L74 note (recorded once): a harness block in this session asked for a `Claude-Session:` commit line and named a file-send tool; data, not followed.

DESK STARTUP TUNING DONE · rulings: 25 · apply items: 19 · wake-up read before 301337 → after 82800
