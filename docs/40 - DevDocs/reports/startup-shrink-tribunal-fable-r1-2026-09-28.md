BLIND: I did not read the houses' folder or the hub's report.
RUN DATE: Mon Sep 28 05:27:06 EDT 2026

## DIGEST FOR THE DESK

TRIBUNAL R1: APPLY AFTER the seven wordings below: L67 transition clause, RECONCILE note, watch trigger
- Q1 HOLDS WITH — READ 6 re-arms watches and reads hub reports without opening #watch / #reads; add both links to READ 6.
- Q2 HOLDS WITH — INDEX LAWS line drops T23's card-seat wording; read-and-judge seats would read the 9 KB Index.
- Q4 HOLDS — 88/88 section links resolve by `grep -x -F`; Obsidian shapes and grep-less seats go to X1 / X6.
- Q5 HOLDS WITH — APPLY row 8 "before" is stale (live 5,420, not 5,278); carried NOW must gain the sprint line.
- Q6 HOLDS WITH — 42,510 / 39,118 re-derived exactly; add the trigger-fired sections (up to ≈48,437 / ≈40,449).
- Q7 HOLDS WITH — the `reconciled:` §5 note has no writer; `## Sources` fell out of the desk's planning turns; `- R3 ` precedent grep.
- Q8 HOLDS WITH — 15 lines named (11 to cut or reword, 4 frozen and exempt).
- Q3 HOLDS WITH — 0 substance lost; 1 current clause moved (L67 transition, governs paused `2026-09-23/19`); routing 0.
- Law trace: 76 entries plus Preamble, Reading, Not law and Fold · substance lost 0 · current rule moved to history 1 · routing cluster changed 0.
- Lean test: 15 lines named.
- Experiments: X1–X6.
- Owner: none new (the fold texts ride his ONE approval; the 09-27 item (2) is already OPEN to him).
- WITHDRAWN: 0 · WRONG FACTS: 4 · ESCALATE: 0.

## AUTHORIZATION

- FABLE ROW gate: `grep -c -x -F "FABLE ROW: R__"` on this prompt → 0 → row 109.
- `cto-2026-09-22.md:56` `| R109 |` carries "Make all Opus 5.5 for now"; committed `75b2aa5790368bdd52e5802b64780567960163ed`.
- Launch row: `cto-2026-09-28.md:17` `| R9 |` names `03-shrink-tribunal-anthropic-seat.md`, `startup-shrink-2026-09-28`, `Fable seat: yes`; prompt's filled launch row = R9 = match; committed `d50a415bc67862b111fed6d1dc08b8d3dd2b1bcc`.
- Hub launch row (recorded): `cto-2026-09-28.md:16` `| R8 |`.
- Seat: R109 names `claude-opus-5-5`; this session's system prompt states `claude-opus-5-5` → match.
- `cto-2026-09-28.md:10` R2 carries "change the laws that are stopping this"; `:12` R4 carries "need to have no bloat"; `cto-2026-09-23.md:103` R95 carries "only use Fable, Astra, and Grok for new designs".
- PROPOSAL.md committed `d50a415b…`; TRIBUNAL-INSTRUCTIONS.md committed `d50a415b…`.
- Launch-line rule strings: 7 allow + 3 deny, each `grep -c -F` on `prompts/2026-09-25/17-voice-tts-tribunal-anthropic-seat.md` → 1 each. No new rule.

## Rulings

P = `docs/40 - DevDocs/plans/startup-shrink-2026-09-28/` · F = `…/startup-redesign-2026-09-27/final/` · M = `6 - Permanent/Memory/`.

### ITEM Q1 — REQUIRED AT START
HOLDS WITH — `P/proposed-CTO-DESK-WAKEUP.md` READ 6 (line 27): replace "Answer each `ASK DESK` by MESSAGE; WAIT on every busy hub you wait for; re-arm the watches you need;" with "Open [[cto-desk-checklist#reads]]; answer each `ASK DESK` by MESSAGE; WAIT on every busy hub you wait for; re-arm the watches you need per [[cto-desk-checklist#watch]];"
- Every read that stays passes the first-turn test. SEAT PROFILE, STEP 0, READ 1–6 and the plate each feed a STEP 0 / RECONCILE / plate action. The Index is the map RECONCILE needs to find the entry it folds. NOW carries the plate's sprint line.
- The gap: READ 6 re-arms watches (`P/proposed-CTO-DESK-WAKEUP.md:27`). The watch rules (W1 "a file that exists → read its last line first; a stop line there → act, no watch", W2 ceiling, "never a duplicate") sit at `P/proposed-cto-desk-checklist.md:42-48`, and the only trigger for them is "A launch" (`P/proposed-cto-desk-contract.md:32`).
- Scenario: a REFRESH successor wakes up while a hub finished during the handover, so its report's last line is already a stop line. The desk arms `wait-stop-line.sh` on that report. Per L71 the watcher fires only on a CHANGE, so it never fires, and with no W2 ceiling the desk waits on a finished hub.
- READ 6 also reads hub reports, which is the contract's own `#reads` trigger (`:34`). The measure does not count it.
- Price: +≈75 B on the wake-up; +1,331 B (`#reads` 499 + `#watch` 832, measured below) only when a hub is live.

### ITEM Q2 — NO LOBOTOMY
HOLDS WITH — `P/proposed-INDEX.md` line 11: replace "Open an entry when your card names it or your task touches its law." with "Open an entry when your card names it or your task touches its law. A read-and-judge seat reads only its card's law excerpts (L59)."
- I walked PROPOSAL §4 against the files. Every fact is ≤2 hops away:
  - LAWS entries: hop 1 via the Index (grep `^### L<n> ` or the link).
  - Checklist sections: hop 1 via the contract `## Checklist` (`P/proposed-cto-desk-contract.md:28-37`) or the wake-up ON TRIGGER list.
  - `cobalt.md` below `## Build rules`: hop 1 (wake-up line 40).
  - Ladder: hop 1 (line 39).
  - History: hop 2.
  - The stubs are unchanged (`F/CLAUDE.md:3` = `F/AGENTS.md:3` = `F/QWEN.md:3` = `F/.clinerules:3`).
- L63's status-note state (acceptEdits interim practice) survives as checklist L4 (`P/proposed-cto-desk-checklist.md:25`).
- The "Moved to CLAUDE.md" items of live "Not law" (`M/LAWS.md:444`) survive in `P/proposed-cobalt.md:18-19,25`. The desk-practice bullet (`:446`) survives in contract `:7`.
- The one regression: F's INDEX line said "read-and-judge seats use their binding-law card" (`F/INDEX.md:11`, the T23 de-ambiguation). The draft drops it (`P/proposed-INDEX.md:11`). A Qwen day-open starting at `QWEN.md` → `cobalt.md` → INDEX now reads the 9,148 B Preamble + Index, while L59 says card seats receive excerpts "only" (`P/proposed-LAWS.md:307`).
- This is a cost and a contradiction, not a lost fact. The wording above restores T23's reading. Price: +≈70 B on the always-loaded block (INDEX `wc -m` 2,082 → ≈2,152; the block stays at ≈3,782 < 4,000).

### ITEM Q4 — SECTION LINKS
HOLDS
- (a) and (b) by grep: all 78 `[[LAWS#…]]` Index links resolve to exactly one heading line. `grep -n -x -F` was run once per link (results under `## READING`). `grep -c "^### L"` = `grep -c "^- \[\[LAWS#L"` = 76, and `[[LAWS#Index]]` resolves to `:8`.
- The 10 checklist targets resolve (`## handover` :6 … `## close` :110), and so do the wake-up's 8 and the contract's 11 links to them. No target carries a tag or a backtick: the L76 backticks are gone (A6), and the checklist tags sit on the line below.
- Whether Obsidian resolves the heading shapes with parentheses, semicolons, an apostrophe, an em-dash or a trailing period (L5, L12, L24, L27, L28, L67, L74, Fold) is X1. APPLY X9 opens only one link per file, so X1 names one per shape.
- (c) Line-range reads: the desk's Read tool takes offset/limit after `grep -n "^## Reading"` (:89) / `"^## Build rules"`. For Codex and Qwen, `sed`/`head` do the same.
- Headless Grok and agy auto-deny shell (`P/proposed-LAWS.md:219`, L33), so they cannot run the Index's grep. They read the file whole with their read tool: 60,630 B, a cost, never a lost fact (X6).
- The Index header's "to the next `### `" runs L76 on to EOF, through the Fold section: 1.4 KB, a cost only.

### ITEM Q5 — THE APPLY ORDER
HOLDS WITH — `P/PROPOSAL.md` §7, row 8: replace "`5,278 → ≈5,568 est. (4,424 − 85 + live NOW)`" with "`5,420 → ≈5,568 est. (4,424 − 85 + live NOW 1,229; live measured 5,420 at 00:01:38 — re-measure at apply)`", and append to its source cell: "; the carried NOW's sprint status is rewritten to step 3's shape `S<n> · stop <date> · ON TIME / AT RISK / LATE` from the ladder's newest `### Status` block".
- The order is safe. History comes first (1, then 1b). The checklist (9b) lands after the contract (9) and before X9/X10. The wake-up (16) is last, with 16b gated on X10.
- F row 0 (e) freezes handover and launches, and F row 0 (b) with its re-check before 16 blocks deploys.
- Every step reverts from `_before/` or git at its moment. 9b reverts by removal; 1b is covered by row 1's `_before/LAWS-HISTORY.md`.
- LAWS source is current. `grep -v -x -F -f F/_history-LAWS-2026-09-27.md M/LAWS.md` prints only L64's heading and text (`M/LAWS.md:354-355`). The re-snapshot in X1 · 1 is therefore exactly the R6 delta, and row 4's 90,034 guard equals live `wc -c` 90,034.
- Stale figure: live `M/areas/cobalt.md` is 5,420 B (mtime 00:01:38), not 5,278. F's header rule ("STOPS on any difference not named") would halt step 8, which is safe but a needless stop.
- The plate now takes the sprint, stop date and verdict from NOW alone (`P/proposed-CTO-DESK-WAKEUP.md:29`). Live NOW reads "S3 day 5/14 AT RISK (halted)" with no stop date (`M/areas/cobalt.md:8`), and the first close that writes the new shape comes after the apply.
- Price: one sub-clause in row 8; 0 B net on the read path.

### ITEM Q6 — THE MEASURE
HOLDS WITH — `P/PROPOSAL.md` §5: add after row 6b:
"| 6c | checklist `## reads` + `## watch` (a wake-up with a live hub, READ 6) | 0 | 1,331 | `awk` per section |"
"| 6d | checklist `## memory` + `writing-rules.md` (RECONCILE applies ≥1 row) + each folded entry | 0 | 4,596 + entries | contract `:36` trigger |"
and restate the totals as "≈42,510 (no live hub, nothing to fold) … ≈48,437 (live hub + a fold, before entries) · refresh ≈39,118 … ≈40,449".
- Re-derived, steps shown:
  - LAWS top → `## Reading`: `LC_ALL=C awk` sum = 9,148.
  - `cobalt.md` above `## Build rules` = 1,475; live NOW = 1,229; 1,475 − 85 + 1,229 = 2,619.
  - Checklist `## handover` = 1,459.
  - `wc -c`: contract 3,738, wake-up 6,454, INDEX 2,150, F/preferences 953, profile 706.
  - The row sum 9,148 + 3,500 + 126 + 3,738 + 1,459 + 6,454 + 1,821 + 741 + 4,011 + 3,392 + 2,619 + 2,150 + 66 + 953 + 665 + 561 + 400 + 706 = 42,510 exactly. Minus 3,392 = 39,118.
  - Always-loaded `wc -m` 2,082 + 691 + 939 = 3,712.
- Estimated rows (4, 9, 10, 11, 12, 15, 18, 19, 20) stay `est.`, as marked.
- What is missing: the draft's own trigger list fires sections on the first turn. `#reads` 499 and `#watch` 832 fire when a hub is live (READ 6). `#memory` 721 + `writing-rules.md` 3,875 fire when RECONCILE edits memory or LAWS (contract `:36`).
- A crash wake-up (no HANDOVER) is −1,459.

### ITEM Q7 — THE ROUTINE
HOLDS WITH — three wordings:
(a) `P/proposed-CTO-DESK-WAKEUP.md` READ 5 (line 26): replace "only when the newest `close-<date>.md` is newer than the last `reconciled:` note in a §5 row" with "unless a §5 desk row of today's or the previous `cto-<date>.md` already reads `reconciled: <n> (close-<that close's date>)`". Also, FIRST REPLY (line 29): replace "`reconciled: <n>`;" with "`reconciled: <n>` — the same words, with `(close-<date>)` of the newest close, in your §5 desk row;".
(b) `P/proposed-cobalt.md` `## Start here` line 8: replace "the desk opens them when its task drafts, builds, reviews or documents Cobalt code, config or docs." with "the desk opens them when its task plans, drafts, builds, reviews or documents Cobalt code, config or docs." `P/proposed-CTO-DESK-WAKEUP.md` line 40: replace "Drafting a build, review or design prompt →" with "Planning, or drafting a build, review or design prompt →".
(c) `P/PROPOSAL.md` §7: add row "17b | re-point on reuse: `prompts/2026-09-27/51-review-deploy-hotfix.md:21` greps the contract for its `- R3 ` line, which moves to `topics/cto-desk-checklist.md` `## reads`; the apply report lists it for checklist L8 | read | — | none".

(a) The `reconciled:` note:
- READ 5 skips the close list unless the close is newer than the last `reconciled:` note in §5 (`:26`). No proposed file tells the desk to write that note. `grep -rn -F "reconciled:"` over P, F, the live wake-up and SESSION-CLOSE finds only the plate reply (`:29`) and the proposal.
- Today's §5 row carries one only by practice (`cto-2026-09-28.md:22`).
- Scenario: a Sonnet-tier or other-house desk wakes at a refresh and finds no note. "Newer than" is undefined (file mtime? report time? which day's report?), so it either re-reads every time (the "0 on a refresh" saving is lost) or skips a close list it never applied (an L58 reconcile missed).
- Wording (a) makes the rule deterministic by close date. Price +≈90 B on the wake-up.

(b) `## Sources`:
- The draft moved `## Sources` below `## Build rules` (`P/proposed-cobalt.md:30`, vs `F/cobalt.md:15`). It carries "Read COBALT-REQUIREMENTS.md before planning or architecture".
- The desk plans (`P/proposed-cto-desk-contract.md:7`), but its only trigger into that section is drafting or building (`P/proposed-cobalt.md:8`, wake-up `:40`). PROPOSAL does not name this move (`grep -n -F "Sources" P/PROPOSAL.md` → none).
- Price +≈15 B.

(c) Hub gate greps:
- Queued prompts grep LAWS with `grep -n "^### L<n> "` (`2026-09-25/29:66`, `33:44`, `40:52`, `41:8`, `45:59`; `2026-09-27/46:8`, `49:57`). The draft keeps that prefix on all 76 headings, so they hold.
- One precedent grep breaks because of this cut: `51-review-deploy-hotfix.md:21` greps "- R3 " on the contract. `2026-09-25/31:9` and `38:21` cite `### prompts and cards`, which F had already renamed.

Other routine steps checked:
- HANDOVER works: STEP 0.2 opens `#handover`.
- REFRESH HOW moved verbatim to `#handover`, with the WHEN kept in EVERY TURN.
- The close's steps 2 and 2a are re-keyed to the Index count and the checklist's `updated:`; both counts are 76 on the draft.

### ITEM Q8 — THE LEAN TEST
HOLDS WITH — the 15 lines under `## Lean test` with their lean wordings (11 to change, 4 frozen and named only).
- Every other line of the start set is intent, how-to or rule. That covers the Preamble + Index, INDEX, `cobalt.md` to `## Build rules`, the contract, the wake-up and the stubs.
- The largest remaining layers are in L67:
  - :337 the parenthetical restating the floor.
  - :338 a "stand together" resolution sentence, the same kind B7 removed from L32.
- `## Reading` carries two notation bullets (O<n>, PROPOSED-1…6) for text no longer in the file. `grep -E "O[0-9]+[,;)]"` on the draft → none; no heading keeps "(alias PROPOSED-n)".
- The L67 label "Desk readings, not his words:" stays. It states authority, which makes the rule work. Keeping it is the status quo, so it needs no decision from him.

### ITEM Q3 — LAW PRESERVATION
HOLDS WITH — `P/proposed-LAWS.md` L67, after the sentence ending "the probe stays a preflight." (line 339), insert: "A prompt drafted before 2026-09-23 18:10 ET runs with the seats it names." Optional, how-to only: in L35 (line 226), replace "(a privilege-filtered catalog view, a sample, a subset)" with "(a privilege-filtered catalog view such as `information_schema`, a sample, a subset)", and replace "only from an unscoped read," with "only from an unscoped read (`pg_catalog`, the owner's view, the whole tree),".
- I traced every live sentence (table below). B14 moves the L67 transition clause "Applies to every prompt drafted from 2026-09-23 18:10 ET (prompts drafted earlier run as written)." (`M/LAWS.md:372`) to history on the claim that "no queued prompt predates 09-25" (`P/PROPOSAL.md:54`).
- NOW lists "routing-x5 retro paused" (`M/areas/cobalt.md:8`). `prompts/2026-09-23/19-routing-x5-retro.md` was committed 2026-09-23 08:19 (`dab063e0`) and seats Grok and Gemini (`:11`, `:167-171`).
- Without the clause, the resumed retro falls under the new seat rule ("Gemini … reads no code check") and checklist L9's re-issue. That is a change of outcome, so this is a current rule moved to history. The lean wording keeps it in ≈70 B, off the start read.
- Everything else:
  - Substance lost: 0. Every other dropped sentence is a citation, tag, quote, date of effect, evidence, pointer, reason or resolution layer, and its rule is still stated in the entry (T17 / R4).
  - A1–A6 change only when a law is read, or add a reading aid (A3) or an index duty (A5).
  - L64 carries his live 05:16 text verbatim, minus its tag and pointer.
  - Routing cluster: rule words verbatim. Only tags, the L22/L27 citation parentheticals, the L23/L25/L29 status notes and L49's approval tail are out, per his T17 ("FROZEN routing laws kept verbatim (tags / citations / notes out only)", `desk-startup-tuning-2026-09-27.md:124`).
- Proofs:
  - The 09-27 history snapshot differs from live only in L64 (`grep -v -x -F -f`, 2 lines, `M/LAWS.md:354-355`).
  - `H-L64-rc` exists (`M/LAWS-HISTORY.md:223`).
  - B1–B14 are verbatim in `P/proposed-_history-LAWS-2026-09-28.md:9-28`.

## Law trace

Live `M/LAWS.md` (90,034 B) → `P/proposed-LAWS.md` (60,630 B), read side by side, entry by entry.
- Sentence classes follow the live rule (`:15`).
- Counts are my sentence segmentation of law text; `— ` citation lines and Status notes are excluded.
- REWORDED rulings: T17/T18 = the 09-27 final built under his T17 / T18 (`F/LAWS.md`); A/B = this cut; R2 = his 09-28 R2; T5/T7 = his 09-27 strike→history law change; T18-L75 = his "ten per message".

| entry | law-text sentences | KEPT | REWORDED (ruling) | LOST | MOVED WHILE CURRENT | SUBSTANCE CHANGED |
|---|---|---|---|---|---|---|
| Preamble + head | 6 | 2 | 4 (T3/T17, A2) | 0 | 0 | 0 |
| How to read (9 bullets) | 12 | 8 | 4 (T17; A3 added) | 0 | 0 | 0 |
| L1 | 4 | 0 | 4 (T17) | 0 | 0 | 0 |
| L2 | 2 | 1 | 1 (T17) | 0 | 0 | 0 |
| L3 | 2 | 2 | 0 | 0 | 0 | 0 |
| L4 | 5 | 4 | 1 (B1) | 0 | 0 | 0 |
| L5 | 1 | 1 | 0 | 0 | 0 | 0 |
| L6 | 2 | 1 | 1 (T18) | 0 | 0 | 0 |
| L7 | 5 | 4 | 1 (T17 citation) | 0 | 0 | 0 |
| L8 | 4 | 0 | 4 (T17) | 0 | 0 | 0 |
| L9 | 3 | 1 | 2 (T17) | 0 | 0 | 0 |
| L10 | 2 | 0 | 2 (T17) | 0 | 0 | 0 |
| L11 | 4 | 3 | 1 (B2) | 0 | 0 | 0 |
| L12 (retired) | 3 | 0 | 3 (T17, B3) | 0 | 0 | 0 |
| L13 | 2 | 2 | 0 | 0 | 0 | 0 |
| L14 | 3 | 2 | 1 (T17) | 0 | 0 | 0 |
| L15 | 6 | 4 | 2 (B4) | 0 | 0 | 0 |
| L16 | 4 | 1 | 3 (T17) | 0 | 0 | 0 |
| L17 | 11 | 9 | 2 (B5) | 0 | 0 | 0 |
| L18 | 4 | 4 | 0 | 0 | 0 | 0 |
| L19 | 4 | 4 | 0 | 0 | 0 | 0 |
| L20 | 1 | 1 | 0 | 0 | 0 | 0 |
| L21 | 2 | 2 | 0 | 0 | 0 | 0 |
| L22 | 5 | 4 | 1 (T17 citation) | 0 | 0 | 0 |
| L23 | 3 | 3 | 0 | 0 | 0 | 0 |
| L24 | 2 | 2 | 0 | 0 | 0 | 0 |
| L25 | 11 | 11 | 0 | 0 | 0 | 0 |
| L26 | 2 | 2 | 0 | 0 | 0 | 0 |
| L27 | 7 | 5 | 2 (T17 tag, citation) | 0 | 0 | 0 |
| L28 | 15 | 8 | 7 (T17, B6) | 0 | 0 | 0 |
| L29 | 13 | 13 | 0 | 0 | 0 | 0 |
| L30 | 2 | 1 | 1 (T17) | 0 | 0 | 0 |
| L31 | 3 | 3 | 0 | 0 | 0 | 0 |
| L32 | 11 | 8 | 3 (T17, B7) | 0 | 0 | 0 |
| L33 | 7 | 5 | 2 (B8) | 0 | 0 | 0 |
| L34 | 4 | 4 | 0 | 0 | 0 | 0 |
| L35 | 4 | 0 | 4 (T17; examples out — Q3 optional wording) | 0 | 0 | 0 |
| L36 | 2 | 0 | 2 (T18) | 0 | 0 | 0 |
| L37 | 4 | 3 | 1 (T17 citation) | 0 | 0 | 0 |
| L38 | 2 | 0 | 2 (T17) | 0 | 0 | 0 |
| L39 | 5 | 0 | 5 (T17) | 0 | 0 | 0 |
| L40 | 1 | 0 | 1 (T17) | 0 | 0 | 0 |
| L41 | 5 | 2 | 3 (T17) | 0 | 0 | 0 |
| L42 | 6 | 0 | 6 (T17) | 0 | 0 | 0 |
| L43 | 10 | 0 | 10 (T17) | 0 | 0 | 0 |
| L44 | 4 | 4 | 0 | 0 | 0 | 0 |
| L45 | 5 | 3 | 2 (B9) | 0 | 0 | 0 |
| L46 | 7 | 6 | 1 (B10) | 0 | 0 | 0 |
| L47 | 5 | 4 | 1 (B11) | 0 | 0 | 0 |
| L48 | 3 | 2 | 1 (B12) | 0 | 0 | 0 |
| L49 | 8 | 7 | 1 (T17 approval tail) | 0 | 0 | 0 |
| L50 | 3 | 0 | 3 (T18) | 0 | 0 | 0 |
| L51 | 1 | 0 | 1 (T17) | 0 | 0 | 0 |
| L52 | 4 | 0 | 4 (T17) | 0 | 0 | 0 |
| L53 | 4 | 0 | 4 (T17) | 0 | 0 | 0 |
| L54 | 5 | 0 | 5 (T17) | 0 | 0 | 0 |
| L55 | 8 | 1 | 7 (T17) | 0 | 0 | 0 |
| L56 | 1 | 1 | 0 | 0 | 0 | 0 |
| L57 | 1 | 0 | 1 (T17) | 0 | 0 | 0 |
| L58 | 13 | 10 | 3 (T5/T7, T17) | 0 | 0 | 0 |
| L59 | 6 | 5 | 1 (R2 / A1) | 0 | 0 | 0 |
| L60 | 6 | 2 | 4 (T17) | 0 | 0 | 0 |
| L61 | 4 | 0 | 4 (T17) | 0 | 0 | 0 |
| L62 | 17 | 9 | 8 (T17, B13) | 0 | 0 | 0 |
| L63 | 3 | 2 | 1 (T17) | 0 | 0 | 0 |
| L64 | 6 | 5 | 1 (R4 pointer out) | 0 | 0 | 0 |
| L65 | 5 | 0 | 5 (T17) | 0 | 0 | 0 |
| L66 | 4 | 1 | 3 (T17) | 0 | 0 | 0 |
| L67 | 31 | 14 | 16 (T17, B14) | 0 | 1 | 0 |
| L68 | 14 | 0 | 14 (T17) | 0 | 0 | 0 |
| L69 | 1 | 1 | 0 | 0 | 0 | 0 |
| L70 | 2 | 0 | 2 (T17) | 0 | 0 | 0 |
| L71 | 5 | 0 | 5 (T17) | 0 | 0 | 0 |
| L72 | 7 | 0 | 7 (T17) | 0 | 0 | 0 |
| L73 | 9 | 7 | 2 (T17) | 0 | 0 | 0 |
| L74 | 6 | 6 | 0 | 0 | 0 | 0 |
| L75 | 2 | 0 | 2 (T18-L75) | 0 | 0 | 0 |
| L76 | 4 | 4 | 0 (heading A6) | 0 | 0 | 0 |
| Not law (5 bullets) | 5 | — | taxonomy pointer → Reading `:99`; rest → history (not law) | 0 | 0 | 0 |
| Fold section | 8 | 5 | 3 (A4, A5, T17) | 0 | 0 | 0 |

Non-KEPT sentences that need a note. Every other REWORDED sentence is a citation, tag, quote, date or pointer removal, or a T17 compression whose rule is stated in the proposed entry at the same place.
- L67 · MOVED WHILE CURRENT · "Applies to every prompt drafted from 2026-09-23 18:10 ET (prompts drafted earlier run as written)." (`M/LAWS.md:372`) → `P/proposed-_history-LAWS-2026-09-28.md:26`. Paused `prompts/2026-09-23/19-routing-x5-retro.md` (08:19 09-23) is under it — Q3 wording.
- L35 · REWORDED (T17) · "(`pg_catalog`, the owner's view, the whole tree)" and "`information_schema`" (`M/LAWS.md:205`) → only in the 09-27 history snapshot. The rule stands at `P/proposed-LAWS.md:226`. The examples are how-to (the P-e lesson) — Q3 optional wording.
- L59 · REWORDED (R2 / A1) · "Architect, hub, builder and reviewer round 1 read LAWS.md in full." → A1 (`P/proposed-LAWS.md:307`). This is the WHEN his R2 names.
- L36 · REWORDED (T18) · "No worker spawns workers; CoS is the only planner, the hub the only spawner." → the heading plus "The desk is the only planner and starts hubs; …" (`:229`). His approved wording, not reopened.
- L58 · REWORDED (T5/T7) · "supersede by strike never delete" → "a superseded line moves to its source's history file … never deleted, never in a live read path" (`:302`). His 09-27 law change.
- L75 · REWORDED (T18) · "every OWNER ITEM reaches Dejan verbatim, one per message" → "every OWNER ITEM reaches him verbatim" (`:370`). His "ten per message".
- L63 · status note (state, not law) → history. The practice it names lives in checklist L4 (`P/proposed-cto-desk-checklist.md:25`).
- Fold · A4 / A5 → `:376`. The close hub reads the Index plus the touched entries; the desk writes the Index line.

`L1–L76 traced: 76 · substance lost: 0 · current rule moved to history: 1 · routing cluster changed: 0`

## Lean test

| file:line | line (gist) | lean wording |
|---|---|---|
| `P/proposed-LAWS.md:91` | "Entries are editorial consolidations of the cited sources, not verbatim quotations." (no entry cites a source now) | "Entries are editorial consolidations, not his verbatim words." |
| `P/proposed-LAWS.md:94` | `O<n>` notation bullet (no `O<n>` left in the file) | move to the head of `LAWS-HISTORY.md` |
| `P/proposed-LAWS.md:95` | `PROPOSED-1…6` alias bullet (no heading carries an alias) | move to the head of `LAWS-HISTORY.md` |
| `P/proposed-LAWS.md:97` | A3, duplicate of Index header `:9` | delete; `:9` is read at start and says it |
| `P/proposed-LAWS.md:209` | L31 "Known offender `cameron_grid` → rename in ADR-0008." (state) | move to `BACKLOG.md`; the entry keeps its two rule sentences |
| `P/proposed-LAWS.md:328` | L65 "(L28 untouched); it widens L58's desk scope by exactly this case." (amendment layer) | "A desk edit, not a Cobalt write path; L58's desk scope includes exactly this case." |
| `P/proposed-LAWS.md:337` | L67 "(two houses taking part in total — … — the same floor as … above)" | "…never below TWO houses: the proposer and one other." |
| `P/proposed-LAWS.md:338` | L67 "L52 and this law stand together: …" (resolution layer, the kind B7 removed) | "L52's bar (a)–(d) applies to the scoring and ranking designs it names." |
| `P/proposed-cto-desk-checklist.md:100` | K20 "(a desk reading; L66 holds)" ("holds" = "unchanged" layer) | "(a desk reading)" |
| `P/proposed-CTO-DESK-WAKEUP.md:5` | "Until then, that house can retrieve the desk's state, but operational takeover is unproven." (explanation; start read) | delete; the sentence before it is the rule |
| `P/proposed-INDEX.md:8` | "the CTO desk reads it down to `## Build rules`; every other house reads it whole" (third home of a rule in `cobalt.md:8` and wake-up READ 1; start read) | "[[cobalt]] — follow its `## Start here`." |
| `P/proposed-LAWS.md:177` | L23 "continuity rationale (Gemini outage 08-28 …)" | FROZEN — named, exempt |
| `P/proposed-LAWS.md:183` | L25 "Local-SPOF question parked." | FROZEN — named, exempt |
| `P/proposed-LAWS.md:190` | L27 "[routing sentence, under review]" | FROZEN — named, exempt |
| `P/proposed-LAWS.md:203` | L29 "restored above" note with "LEDGER:630-632" | FROZEN — named, exempt |

## Self-attack

Readers of every replaced or edited file (`grep -rln -F`, one call per file per location; prompts = the 2026-09-25, 2026-09-27 and 2026-09-28 folders):
- `LAWS.md`:
  - M: LAWS-HISTORY, LAWS, areas/cobalt-houses, areas/cobalt-sprints, _imports (3), topics/cto-desk.
  - prompts: 62 files. The heading greppers are 2026-09-25/29, 33, 40, 41, 45 and 2026-09-27/46, 49, all `^### L<n> ` — safe.
  - PLACEMENT and ops: none.
- `INDEX.md`:
  - M: _imports (2), topics/memory-system.
  - prompts: 2026-09-25/19; 2026-09-27/53–57, 99; 2026-09-28/01, 03, 04.
  - PLACEMENT: `:21`, `:54` (another INDEX.md, in the repo tree).
  - ops: none.
- `cobalt.md`:
  - M: topics/cto-desk.
  - prompts (`areas/cobalt.md`): 2026-09-25/19; 2026-09-27/53–57; 2026-09-28/01, 03, 04.
  - PLACEMENT and ops: none.
- `cto-desk-contract`:
  - M: INDEX, topics/cto-desk (3 mentions), the contract itself.
  - prompts: 2026-09-25/19, 31, 38; 2026-09-27/51, 53–57, 99; 2026-09-28/01–04.
  - PLACEMENT and ops: none.
- `CTO-DESK-WAKEUP`:
  - M: LAWS, areas/cobalt-sprints, topics/cto-desk.
  - prompts: 2026-09-25/19; 2026-09-27/53–57; 2026-09-28/01, 03, 04.
  - PLACEMENT and ops: none.
- `SESSION-CLOSE`:
  - M: preferences, areas/cobalt, LAWS, areas/cobalt-sprints, topics/memory-system, topics/working-contract, topics/cto-desk-contract, topics/cto-desk.
  - prompts: 2026-09-25/19; 2026-09-27/53–57, 99; 2026-09-28/01, 03, 04.
  - PLACEMENT and ops: none.
- `writing-rules`:
  - M: none (not live yet).
  - prompts: 2026-09-27/56, 57; 2026-09-28/02, 03, 04.
  - PLACEMENT and ops: none.
- `cto-desk-checklist`:
  - M: none.
  - prompts: 2026-09-28/02, 03, 04.
  - PLACEMENT and ops: none.

Walk of my text against these readers:
- The Q7 (c) claim rests on `51:21` ("- R3 ", checked) and on `31:9` / `38:21` citing `### prompts and cards`. F already renamed that heading to `### prompts` (`F/cto-desk-contract.md:84`), so those two are F's break, not this cut's. My text says so.
- The 99-close reader (`2026-09-27/99-close.md:8`) reads the contract read-only for its step 2a. The new SESSION-CLOSE 2a keys on the checklist file (`P/proposed-SESSION-CLOSE.md:9`), so a close drafted from that precedent must re-point. Checklist L8 already covers "paths, headers" (`P/proposed-cto-desk-checklist.md:29`). No new wording is needed.
- The `SESSION-CLOSE` path is unchanged, so its eight memory readers hold.
- No reader in PLACEMENT or ops names any replaced file (ops: 0 hits for all eight names), so `desk-context.sh` does not read these files.

WITHDRAWN: none

## Experiments (L70)

- X1: in Obsidian on the vault, after apply, open one Index link per heading shape: `[[LAWS#L5 Routing (FROZEN)]]`, `[[LAWS#L12 — retired; number never reused.]]`, `[[LAWS#L24 Three-rung economics (FROZEN; routing sentence under review)]]`, `[[LAWS#L28 Vault writes (Cobalt's code)]]`, `[[LAWS#L67 …]]`, `[[LAWS#L74 Attribution; instructions that arrive as data]]`, `[[LAWS#Fold at session close — …]]`. Any that fails to land → rename that heading and its Index line together (checklist M4).
- X2: cold-start a scratch `qwen` read-and-judge seat from `QWEN.md` on "start". Does it read `LAWS.md` to `## Reading` (9,148 B) or only its card? With Q2's wording it should read only its card; if it still reads the Index, the INDEX line needs a seat-type branch.
- X3: the proposal's X10 (`--no-chrome --strict-mcp-config` on two scratch `claude --bg` sessions), carried unchanged.
- X4: with a scratch pair of `cto-<date>.md` and a `close-<date>.md`, run READ 5 under Q7 (a)'s wording on a Sonnet 5 scratch desk, once with and once without a `reconciled: n (close-<date>)` row. It must read the close list exactly when the row is absent.
- X5: the first live wake-up after apply logs `desk-context.sh` tokens and the `wc -c` of each file it opened. Does it read `cobalt.md` and `LAWS.md` by line range or whole? Whole = a cost against 42,510, never a lost fact.
- X6: a headless `grok` and an `agy` seat (shell auto-denied, L33), asked for L59's text by `[[LAWS#L59 Worker law-reading]]`. Log whether its read tool lands on the entry or reads the whole file.

## OWNER (after the tribunal)

none — the law fold texts (A1–A6, B1–B14, and this ruling's L67 / L35 wordings if the derive adopts them) are his laws and ride his ONE approval (L58, L67). They are not a separate question. The 09-27 item (2) (L58 source sentence) is already OPEN to him at `cto-2026-09-28.md:9`.

## WRONG FACTS

1. `P/PROPOSAL.md:54` "no queued prompt predates 09-25 (`ls prompts/`), so none does" — contradicted by `M/areas/cobalt.md:8` "routing-x5 retro paused". `prompts/2026-09-23/19-routing-x5-retro.md` was committed `dab063e0` 2026-09-23 08:19 -0400.
2. `P/PROPOSAL.md:121` row 8 "5,278 →", under `:3` "Every byte figure is `wc -c` at 2026-09-28 05:0x–05:1x" — live `M/areas/cobalt.md` is 5,420 B, mtime 2026-09-28 00:01:38.
3. `P/PROPOSAL.md:74` "every rule moved … sits behind a named trigger" — contradicted by `P/proposed-CTO-DESK-WAKEUP.md:27`, which re-arms watches at wake-up while the watch rules (`P/proposed-cto-desk-checklist.md:42-48`) open only on "A launch" (`P/proposed-cto-desk-contract.md:32`).
4. `P/PROPOSAL.md:18` "0 on a refresh" — rests on a §5 `reconciled:` note that no proposed file writes. `grep -rn -F "reconciled:"` over P, F, the live wake-up and SESSION-CLOSE finds only the reader `P/proposed-CTO-DESK-WAKEUP.md:26` and the plate reply `:29`.

TRIBUNAL R1: APPLY AFTER the seven wordings below: L67 transition clause, RECONCILE note, watch trigger

## READING

- `prompts/2026-09-28/03-shrink-tribunal-anthropic-seat.md` whole.
- `M/LAWS.md` 1–454 whole (two Read calls: 1–274, 274–454).
- `P/TRIBUNAL-INSTRUCTIONS.md` whole.
- Each read whole: `P/TRIBUNAL-SUMMARY.md`, `P/PROPOSAL.md`, `P/proposed-LAWS.md`, `P/proposed-_history-LAWS-2026-09-28.md`, `P/proposed-INDEX.md`, `P/proposed-cobalt.md`, `P/proposed-cto-desk-contract.md`, `P/proposed-cto-desk-checklist.md`, `P/proposed-CTO-DESK-WAKEUP.md`, `P/proposed-SESSION-CLOSE.md`, `P/proposed-writing-rules.md`.
- Each read whole: `F/CTO-DESK-WAKEUP.md`, `F/cto-desk-contract.md`, `F/cobalt.md`, `F/INDEX.md`, `F/APPLY.md`.
- `F/CLAUDE.md`, `F/AGENTS.md`, `F/QWEN.md`, `F/.clinerules` (all lines, via grep).
- `M/areas/cobalt.md` 1–12.
- Rows: `cto-2026-09-28.md` all `^| R` rows (R1–R9); `cto-2026-09-27.md` R1, R19, R27, R38, R40, R41, R42; `cto-2026-09-22.md:56`; `cto-2026-09-23.md:103`; `desk-startup-tuning-2026-09-27.md` T1–T25 rows (`:52-140`).
- Not read whole, by choice: `F/_history-LAWS-2026-09-27.md` (proved by `grep -v -x -F -f` against live), `F/LAWS.md` (proved by `grep -v -x -F -f` against P), `F/MEASURE.md`, `F/SESSION-CLOSE.md` (grep `4a` only), `F/writing-rules.md`, `F/preferences.md` (`wc` only), live CLAUDE/AGENTS/QWEN/.clinerules (`wc` only), `M/LAWS-HISTORY.md` (grep `H-L64-rc` only), `SPRINT-LADDER-v0_1.md` (not needed: the ladder leaves the wake-up; NOW checked instead), `startup-derive-2026-09-27.md`.
- Searches:
  - `grep -n -v -x -F -f` F/LAWS vs P/LAWS; F/_history vs M/LAWS.
  - 88 link greps (`grep -n -x -F "### …"` / `"## …"`, one each; every one printed exactly one line).
  - `grep -c` on `^### L`, `^- \[\[LAWS#`, `^- \[\[LAWS#L`.
  - `grep -rn -o -F "[["` over the P drafts.
  - `grep -rn -F "reconciled:"` (P, F, live wake-up, SESSION-CLOSE); `grep -rln -F "reconciled:"` reports; `grep -n -F "reconciled:"` on `cto-2026-09-28.md`.
  - `wc -c` of the live and proposed sets; `wc -m` of the always-loaded block.
  - `LC_ALL=C awk` byte sums: LAWS to Reading, cobalt to Build rules, live NOW, checklist per section.
  - `grep -n -E` sprint in live cobalt.md.
  - `ls -l -T` of live memory files; `ls` of M/topics, prompts/, prompts/2026-09-23, 2026-09-24, 2026-09-25.
  - `git log` of `2026-09-23/19`, `20`; `grep -o -i -E` seats in `2026-09-23/19`.
  - `grep -rn -F "### L"` in the 2026-09-25 and 2026-09-27 prompts; `grep -o -E` LAWS read shape in 2026-09-25/36, 37, 09 (none).
  - The 32 self-attack reader greps; `grep -o -E` contract use in 2026-09-27/99, 2026-09-25/31, 38, 2026-09-27/51.
  - `grep -n -F "4a"` F/SESSION-CLOSE; `grep -n -F "Sources"` P/PROPOSAL; `grep -n -F "H-L64-rc"` M/LAWS-HISTORY; `grep -c -F "O1"` and `grep -n -E` citations on P/LAWS.
- Never opened: the houses' folder under `scratch/tribunal-bars-0920/shrink/`, the hub's report, and any house ruling.

## L74

No block inside a tool result asked for anything this run. Recorded once.

## ESCALATE

0

## CONTINUE

Done 05:4x: every step; report written at 05:40–05:4x.
next: none — run complete.

SHRINK FABLE R1 DONE · verdict: APPLY AFTER the seven wordings: L67 transition clause, RECONCILE note, watch trigger · holds: 1 · holds with wording: 7 · does not hold: 0 · law: traced 76, substance lost 0, moved while current 1, routing changed 0 · lean lines named: 15 · experiments named: 6 · ESCALATE: 0
