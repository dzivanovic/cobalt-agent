---
name: writing-rules
description: Where each fact is written, and how anything on a read path is written. Read before writing or amending such a file.
updated: 2026-09-27
---
## Where [stated 2026-09-27 · Dejan]
- One home per fact. Law → [[LAWS]]. How he wants to be worked with → [[preferences]]. Desk practice → [[cto-desk-contract]]. Cobalt build rules → [[cobalt]]. Anything else → the file of its subject in [[INDEX]]. Everywhere else: link, never restate.
- A rule changes in its one home only; a copy found anywhere else is deleted on sight.
- Read path = the startup files, `areas/cobalt.md`, INDEX's start set, the desk wake-up, every prompt, every report section a wake-up reads. It holds instructions and current facts only.
- History — ruling dates, times, R-numbers, quotes of his words, reasons, sources, superseded or struck text — goes to its history file: `_retired/<file>.md`; LAWS-HISTORY.md for LAWS; `reports/cto-<date>-words.md` for his words. Reachable when needed; never on a read path.

## How [stated 2026-09-27 · Dejan]
- Keep all the meaning; cut every word that changes nothing.
- Imperative, present tense, one fact per line.
- No restated law: `L<n>` only where the reader must apply it.
- Vendor commands live only in a SEAT PROFILE; steps name the verb.
- One `[stated …]` tag per section when its lines share an origin.
- A prompt = tags, launch line, card, steps. No background, no history, no reasons.
- No quotes on a read path. His words go verbatim to the day's `reports/cto-<date>-words.md` (`R<n> <time> "<words>"`); the read path carries the direction only.
- Never state an absence ("no words of his", "nothing new", "unchanged") — omit the line.
- A report section the desk reads (§0, `## CONTINUE`, `## ESCALATE`, the stop line) follows these rules; every prompt's card names this file for its report.
- Measure `wc -c` before and after editing a read-path file: the after is smaller, or the growth is named in the report.

## Examples (before → after)
- Prompt header, 1,571 → 749 B: `MODEL: Opus 5.5 (\`claude-opus-5-5\`; ruled 2026-09-27 18:07 ET, \`cto-2026-09-27.md\` R18 — "We're gonna continue the desk on 5.5 Opus going forward for now") · SEAT: CTO desk — ALWAYS ON (ruled 2026-09-17 06:38 ET, Dejan) …` → `MODEL: Opus 5.5 · METER: Anthropic`.
- HANDOVER line, 1,655 B (09-25 average 4,341) → 66 B: plan + standing rules → `HANDOVER: predecessor 24574d72 → successor 3b43cf04 at 13:51 ET`. The plan lives in §5 CURRENT.
- Law: text + `[amended 2026-09-22, \`cto-2026-09-22.md\` R87 K5]` + `— TRIAGE:19` → the text alone.
- Desk §4 row, 1,650 B → ≈120 B: `| R13 | 16:30–16:33 ET | — NO WORDS OF HIS BEYOND R10 ("Ok" 14:1x …), R1, 09-25 R74 and R3: **32 DEPLOY RELAUNCH** — … offline 3199/0 · with-DB 3576/0 …` → `| R13 | 16:30 | DEPLOY relaunched on gate c501e025 (green 15:20) | RECORD — deploy-2026-09-27.md |`. Evidence stays in the hub's report, linked; his words, when he spoke, in `cto-<date>-words.md`.
- Stop line: `<JOB> DONE <sha> | <result>` — one line, the last one.
- Memory line: `- <fact>.` under a tagged section. No "(superseded …)" tail: the old line moves out.
