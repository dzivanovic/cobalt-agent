# Startup redesign — tribunal summary

Proposer: Fable 5.1 with Dejan, 2026-09-27. Seats (L67, new design): Fable · Astra · Grok; Gemini optional fourth. Full record: `PROPOSAL.md` (file table, clause trace, measurements) in this folder; his rulings T1–T21: `docs/40 - DevDocs/reports/desk-startup-tuning-2026-09-27.md`.

## Problem
A desk wake-up measured 136,059 tokens before any work; 12 wake-ups on 09-25. The read path carried duplicates, law restatements, struck lines, ruling history and quotes.

## Result
Wake-up file reads ≈301 KB → ≈83 KB (−73%); ≈−54,600 tokens (÷4), 40% of the measured wake-up; the rest is harness and the desk's own turns. Every house's start: CLAUDE.md 16,590 → 126 B.

## Principles (his rulings)
1. A startup file only points to `areas/cobalt.md`.
2. Laws live only in LAWS.md; no restatement elsewhere.
3. One home per fact; everywhere else links.
4. No lobotomy: every start still reaches everything it needs.
5. History (dates, quotes, citations, struck text) moves to history files, kept, never on a read path.
6. INDEX is the traversal map; every memory file is listed.
7. Keep all meaning; cut every word that changes nothing.
8. The desk is vendor-agnostic: vendor commands live in one SEAT PROFILE.

## Law changes to rule on (his intent stated; law only through the desk, L58)
1. Preamble: every house starts at its startup file → `areas/cobalt.md` → INDEX → LAWS.
2. L58: a superseded line moves to its source's history file (`_retired/<file>.md`; LAWS-HISTORY for LAWS) instead of being struck; one `[stated]` tag per section when lines share an origin; the Fold-at-close section merged into L58.
3. L75: "one per message" struck; the per-message count lives only in `preferences.md` (up to ten).
4. LAWS text: citations, tags, quotes, status notes and the "Not law" section move to LAWS-HISTORY; FROZEN routing laws (L5, L21–L27, L29, L49) keep their text verbatim; L6, L36, L50 reworded, meaning unchanged (approved).

## Answer these (his questions)
1. Can any other house — OpenAI, xAI, Google, the local Qwen — take over the CTO desk from these files alone, traverse memory, understand the state and continue as if nothing changed?
2. Is every start-path line a direction or description with one correct reading, unambiguous for a lower-tier model?
3. Is this the memory structure for all of Cobalt — many houses' agents, local Qwen included — and will it survive and thrive there?
4. Is this the right way to do it? If not, what instead.
5. How would the desk run on YOUR house's tooling? For each SEAT PROFILE verb — LAUNCH, VIEW, LIST, STOP, MESSAGE, WAIT, MEASURE — name your replacing command, or the gap. Frame: every house can run herdr tabs and start any vendor's model in one; WAIT is already vendor-free (the report's stop line); remote control is replaced by Cobalt as the front end over Tailscale (an L64 amendment, his ruling, later).
Local seat: current state and stale text in `PROPOSAL.md` "Local seat (Qwen)"; its automation is a separate lane.

## Check for (the proposer's own risk list)
- Traversal: startup file → cobalt.md → INDEX start set (preferences, profile, LAWS, desk contract, writing-rules) reaches everything the old path did (`PROPOSAL.md` Trace).
- RECONCILE: `grep -F "APPROVED — pending fold"` + launch rows marked `LAUNCHED` — finds every unfolded ruling, from the apply date on.
- His words moved from §4 rows to `reports/cto-<date>-words.md`: L7 (approval + time in §4), L58, L67, L73 (his words recorded) hold without text change.
- Lessons gate re-keyed: a lesson line ends `→ <rule id>` (contract no longer cites lesson lines).
- Distilled LAWS text: meaning of every law unchanged against `proposed-_history-LAWS-2026-09-27.md`.
- Fixed stale-against-law text in SESSION-CLOSE.md (step 2 hub-applies, no runner column, "Dejan pushes", old wake path, strike rule).

## Files (all drafts `proposed-<live name>` in this folder)
CLAUDE.md · AGENTS.md · QWEN.md · .clinerules · INDEX.md · areas/cobalt.md · preferences.md · LAWS.md · topics/cto-desk-contract.md · topics/writing-rules.md (new) · prompts/CTO-DESK-WAKEUP.md · SESSION-CLOSE.md · prompts/UNATTENDED-LAUNCH.md; history: `proposed-_history-LAWS-2026-09-27.md`, `proposed-_retired-*.md`.
