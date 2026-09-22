# LAWS CONSOLIDATION — proposer report (2026-09-22)

Seat: `laws-consolidation-propose-0922` (Opus 5), launched by the desk from `prompts/2026-09-22/07-propose-laws-consolidation.md`. Started 06:50 ET, stopped 07:0x ET (`date`). Wrote three files and nothing under `6 - Permanent/Memory/` (L58). Re-aimed mid-run by the desk's message at 06:5x ET, relaying his R4 ("I don't need tribunal for the laws. Laws are all mine"). I verified R4 at `cto-2026-09-22.md` §4 line 14 before acting on it. File (a) is now HIS sitting packet, one block per law; §9 (tribunal questions) was dropped; §10 became packet §6, his ordered rulings.

## §0 DIGEST
- Files: `docs/30 - Design/LAWS-CONSOLIDATION-PROPOSAL-2026-09-22.md` (packet, 22.7 KB) · `…-LAWS-draft.md` (full proposed LAWS.md as it reads if he takes every recommendation; 80.9 KB; L1–L75 contiguous).
- Laws 74 → 75: none retired, one new (**L75 Fix rounds classify first**). 29 entries reworded (2 of them headings only). 12 pieces of text go to LAWS-HISTORY, each with its proof (packet §3).
- Contradictions 15: 13 get proposed wording; 2 are his with **no text change recommended** — C10 (L43: keep) and C11 (routing cluster: frozen, name the tribunal date). Under R4 all 15 are his to rule.
- Pending close proposals 8: 7 adopted into law text; 1 kept as desk practice (09-20 P-a).
- Most consequential: (1) **L34 amended to the real interim registry** (desk report §5 row + `claude agents --json`), because it has never once been obeyed. (2) **L62 gains the write-path launch shape**: `acceptEdits` plus the full allowlist listed in the prompt body, never bare `--bg` (which comes up in auto mode), no heredocs, plus the hub/desk ask boundary. (3) **L58 + SESSION-CLOSE + NOW**: the hub proposes and the desk applies; NOW becomes a ≤1,500-character snapshot (it is 50,055 bytes today).
- His rulings: 15, one word each (packet §6). Most important: #1, L34.
- ESCALATE: 5.

## ESCALATE
| # | item | why |
|---|---|---|
| 1 | **Law text changed since the audit.** The vault is not a git repo, so `git log` cannot diff LAWS.md. Judged from inline tags plus the file's mtime (2026-09-21 18:10): **L43** `[amended 2026-09-21 R47]`, **L67** `[amended 2026-09-21 R46]` and **L73** `[amended 2026-09-21 R5]` are newer than the 09-20 audit. All three are placed in the packet. The audit's "382 clauses" count is stale by these three. | The audit's clause counts no longer match the file. |
| 2 | **Audit C5 is contradicted by later evidence.** The audit called the 09-19 no-flag hubs (`02`, `38`, `48`–`50`, `53`) "allowlist-only, compliant by accident". On 09-21, `65`, launched bare, came up in AUTO mode and refused at preflight (`close-2026-09-21.md` P-a). If that held on 09-19, those write-path hubs ran in auto mode against L29. **UNPROVEN (L70):** nobody has read a 09-19 transcript's mode. | Decides whether 09-19 broke L29. A read-only check of one transcript settles it. |
| 3 | **The audit's acceptance test (§5: a 382-clause trace file, both directions, plus a second-house read of the diff) was not produced.** The packet and draft work per law, not per clause. R4 removes the tribunal. The trace would still be the mechanical proof that nothing was dropped, which has happened twice before (L28 O1, L29 O12). | Ask the desk: a Sonnet trace hub before the fold, or his waiver. |
| 4 | **Cited from partial search only.** "No routing tribunal on record since 09-13" was checked against `cto-/close-2026-09-20…22.md` and `BACKLOG.md`, not the ledger. The L34 "reconcile at every wake-up and refresh" is a NEW proposed practice, not an existing citation. "NOW = 50,055 bytes" is my own `awk … \| wc -c` at 06:5x. | Marked `UNCITED — verify` where used. |
| 5 | **LAWS-HISTORY entries are not drafted.** Packet §3 names the 12 moves and their proofs. The desk writes the verbatim entries from current LAWS.md at the fold. The same applies to the INDEX rule-3 and SESSION-CLOSE edits (packet §4). | L58: the desk alone writes those files. |

Audit placement: every §2 row (C1–C15), §2b, §2c (5 notes) and §3 row (K1–K15) has a disposition in the packet — 13 in law blocks, K1/K3/§2c-STATE as "not done, why". None unplaced.

L74: this session's tool results carried the injected `Claude-Session` block; treated as data and not followed. No commit was made.

LAWS CONSOLIDATION PROPOSED · laws: 74 → 75 · contradictions: 13 resolved / 2 open for Dejan · struck to history: 12 · new laws proposed: 1 · size: 22.7 KB · ESCALATE: 5
