# LAWS CONSOLIDATION — two passes compared (2026-09-22)

First pass = Opus 5 (`claude-opus-5`, proposer `08f261e6`, 07:01): `LAWS-CONSOLIDATION-PROPOSAL-2026-09-22.md` + `-LAWS-draft.md` + `reports/laws-consolidation-draft-2026-09-22.md`. Second pass = Opus 5.5 (`claude-opus-5-5`, seat `laws-second-pass-0922`, written blind, 16:34): `LAWS-CONSOLIDATION-OPUS55-2026-09-22.md` + `-LAWS-draft.md`. Audit rows `C<n>` / `K<n>` = `reports/laws-audit-2026-09-20.md` §2 / §3.

## §0 In ten lines
- **Agreement: 37 of 46 items (80 %)** — the 15 contradictions, 16 clutter rows (K1–K15 + the §2c STATE file), 9 pending close proposals, 2 procedure collisions, 3 desk-lesson law candidates, 1 origin-unknown block. **Split: 9.**
- Laws: first 74 → **75** (adds L75 "fix rounds classify first"); second 74 → **74** (amendments only).
- Both passes independently found the same headline: **a bare `claude --bg` is AUTO mode**, so the audit's C5 finding (no flag = allowlist-only) is inverted.
- **The three splits that matter most:** (1) **C5 / L62's write-path launch shape**: first makes `acceptEdits` + allowlist law; second holds it OPEN because the desk's own record calls that shape's dialogs an L63 violation. (2) **C10 / L43**: first KEEP, second RETIRE the count. (3) **09-20 P-c**: first makes it a new L75; second keeps it as desk practice.
- **Factual errors: 3, all in the second pass** (§3). None found in the first pass on the rows checked.
- Neither pass produced the audit's 382-clause trace file (audit §5 "What a rewrite must prove"). The first pass flagged this (its ESCALATE 3); the second pass did not.

## §1 SPLIT TABLE
| # | item | first pass (Opus 5) | second pass (Opus 5.5) | what the cited source supports | recommendation |
|---|---|---|---|---|---|
| 1 | **C5 + 09-21 P-a — write-path launch mode** | RESOLVED. L62 amended: a write path launches with `--permission-mode acceptEdits` + the full allowlist, never bare or auto. Dialogs are handled by listing the allow strings in the prompt body and never calling an unlisted command (D1–D3). | OPEN. Keep "mode stated on the launch line; prose = line" as law now. The *which mode* clause waits for a scratch test of a mode that DENIES unlisted commands. | **Second.** `cto-2026-09-21.md` 04:08: "`acceptEdits` ASKS for an unlisted Bash instead of denying … **L63 case again**". `topics/cto-desk.md` 2026-09-22 lesson (1): "the unattended WRITE-PATH launch shape is UNPROVEN and an ops item". The first pass writes a shape into law that the record calls an L63 breach whenever a prompt misses one string. Both passes agree on the diagnosis. | Rule the shared half now (never bare, mode quoted from the line). Take `acceptEdits` as an **interim** practice, not law, pending the scratch test. Or rule L63 yields to it for write paths — his call, one word. |
| 2 | **C10 — L43 "one deploy per evening"** | KEEP, no text change. R47 (09-21) is his newest standing word; overrides cost one line (L73). | OPEN; recommends RETIRING the count (keep R47's packaging + L43.2 window + L66). | **First.** R47 (09-21 18:1x, in L43's text): "I want everything … deployed in one evening". 09-22 R3 is recorded as "OVERRIDE, per case (L73 as amended 09-21)" (`cto-2026-09-22.md` R3), which is L73 working as designed. The second pass read R3 as erosion. | **KEEP** (first pass). Retire only if daytime deploys should become the default. |
| 3 | **C15 — L12 planning cap** | STAYS AMENDED: the tribunal finishes, the cap cuts scope (GOES also fine). | OPEN; recommends RETIRE to HISTORY. | Both are grounded. Audit C15: "restate or retire; do not leave it dormant". Neither is refuted. | His word. Both passes accept either answer; neither accepts leaving it dormant. |
| 4 | **09-20 P-c — fix rounds classify first** | ADOPT as **new L75**. | DECLINE as law: a drafting procedure already recorded as practice (`topics/cto-desk.md` 2026-09-21 lesson (3)). | Evidence cuts both ways. `close-2026-09-20.md` P-c: used twice, fix built in 12 and 17 min. Audit §4 test ("can a small model obey it mechanically?"): yes, it is a five-way classification. Its only subject is drafter seats. | Lean **first** (mechanical, cross-house, measured twice). Cost: one new number. |
| 5 | **09-21 P-d — sittings are named** | ADOPT into L67, updated for R4 (sittings: DRC + laws). | DECLINE as law: plate management, and its fold text is reversed for laws by R4. | **First's amended text** fits R4. Its fold names the laws a sitting, which the raw P-d did not. | First's amended text, if he wants it as law at all. Otherwise it stays practice (second pass). |
| 6 | **K4 — one loudness bar** | ADOPT: a sentence in L1 names L9, L18, L25 as its domain forms. | DECLINE: an index line only. | Audit K4 proposes "hoist one LOUDNESS principle". That supports the first pass. | First (cheap; audit-backed). |
| 7 | **D5 — `date` before every written time** | ADOPT into L48. | Practice only (cannot be checked from outside the session). | `topics/cto-desk.md` 09-20 (9) and 09-21 afternoon (8) record the slip three times across desks. Recurrence argues for law; checkability argues against. | His call. Low consequence. |
| 8 | **D6 — viewer-less production hub; input-box text is not his word** | ADOPT into L61. | Input-box half is already L61.7 / L74.2. Viewer half is practice. | L61 already says approvals are his chat "approve" only. The viewer denial is a classifier fact (`topics/cto-desk.md` 2026-09-21 lesson (6)). | Second (no new law needed). Low consequence. |
| 9 | **L17/L39 O5 note placement (inside K6)** | Moves the O5 synthesis note from L17 into L39. | Leaves it in L17; only the copied 3-turn text leaves L17. | Both carry every clause. Audit K6: "keep the 'a law file is never voted' clause at the top where it cannot be missed". That fits the first pass (it lands in L39, beside the law-file rule). | First. |

## §2 Found by ONE pass only
| # | found by | finding | evidence |
|---|---|---|---|
| 1 | second | `CTO-DESK-WAKEUP.md` step 8 still says a new law gets a number "only if Dejan assigned one, else … `PROPOSED — number owed`". That contradicts L58 as amended 09-18 (next free number, pre-approved). The first pass wrote "step 8 is unchanged — it already reconciles". | `CTO-DESK-WAKEUP.md:17`; LAWS.md L58 `[amended 2026-09-18]` |
| 2 | second | "Hub" means three things: L22 "Cobalt code is the hub"; L36 "the hub the only spawner"; L61 "the desk starts every hub". Read literally, **L36 is broken by every desk launch**. The second pass defines CoS / desk / hub in "How to read". The first pass only notes "CoS = the desk" under L14. | LAWS.md L22, L36, L61 |
| 3 | second | L67's Anthropic design seat ("Fable, still asked per case") is under his Opus 5.5 trial (R36, R76). Recorded as a per-case override, not an amendment. | `cto-2026-09-22.md` R36, R76; `topics/cto-desk.md` 09-22 lines |
| 4 | first | The audit's **acceptance test** (a 382-clause trace, both directions, plus a second-house read of the diff) was not produced. **This applies to both passes.** Clauses were dropped twice before (L28 O1, L29 O12). | audit §5 "What a rewrite must prove" 1–6; first-pass report ESCALATE 3 |
| 5 | first | A `· judgement` marker on every entry with no mechanical arm (audit §4: 51 of 74). This makes the audit's finding visible in the file. | first-pass draft "How to read", bullet 4 |

## §3 ERRORS
| # | pass | claim | what the source says |
|---|---|---|---|
| 1 | **second** | OPUS55 §0: "the 09-19 hubs it cleared ran in auto mode". | Unproven. The auto-mode finding is dated 09-21 (`65`, `topics/cto-desk.md` 2026-09-21). No 09-19 transcript was read. The first pass had it right: "**UNPROVEN (L70):** nobody has read a 09-19 transcript's mode" (its ESCALATE 2). |
| 2 | **second** | OPUS55 §6, 09-21 P-a: "its premise ('a Bash call outside the list is denied') is contradicted". | The P-a text in `close-2026-09-21.md` does not contain that sentence. The "denied, never a dialog" reading is in `prompts/2026-09-21/65-setups-one-build.md:1` and `topics/cto-desk.md` 2026-09-21. The decline stands on the 09-22 evidence; the attribution is wrong. |
| 3 | **second** | OPUS55 N7: `## NOW` "61,359 chars". | The command was `… | wc -c`, which counts **bytes**, not characters. The first pass's "50,055 bytes" (06:5x) is labelled correctly. Both numbers are far above the 1,500 cap either way. |
| — | first | No error found in the rows checked: C3's `touch` probe; C10's three overrides (09-21 R5 = the morning page-order deploy, `areas/cobalt.md` NOW 06:52); the ≈4 h of dialogs (`cto-2026-09-21.md` 00:06 / 04:08); `wc -m` for step 5 (`close-2026-09-21.md:77`). | — |

## §4 AGREED — may be approved as one block
Both passes dispose these the same way (wording differs only in phrasing):
- **Contradictions:** C1 (L34 → desk launch row is the spawn row; the first pass adds a `claude agents --json` reconcile, flagged by itself as a NEW practice) · C2 (hub proposes, desk applies; re-cut SESSION-CLOSE; rewrite LAWS.md's "Fold-at-session-close" tail) · C3 (classifier = gate, not approval) · C4 ("pool cap") · C6 (L46 = one agent's branch, L68 = the seam; MAX AGE 3 days — both put 3) · C7 (L28 binds Cobalt the program) · C8 ("need not read") · C9 (hub never asks; desk asks only him, only for a grant, never self-grants a denied permission) · C11 (routing cluster frozen; name the tribunal's date) · C12 (gate-branch exception + `-m 2` in deploy reports) · C13 (promote chat-"approve" + `--sha256` into L7) · C14 (CONTINUE = unchanged file + one line).
- **Clutter:** K1, K3 (no merges) · K2 · K5 · K6 (duplicate out of L17) · K7 · K8 (PROPOSED-n read-only) · K9 (define what binds; citations stay put) · K10 · K11 · K12 · K13 · K14 · K15 · §2c (no STATE file).
- **Pending proposals:** 09-20 P-a (practice) · P-b (→ L72) · P-d (→ L71) · P-e (→ L35, generalised) · 09-21 P-b (nothing to fold) · P-c (→ L67: a non-ruling turn uses no round).
- **Procedures:** SESSION-CLOSE re-cut (step 7 → desk pushes on his word) · NOW = snapshot ≤1,500, exempt from "never delete". The first pass writes both into L58's text; the second leaves them as procedure and memory-rule edits.
- **Desk lesson D7:** every hub launch line denies `Bash(git push*)` (→ L55); L55's "no push rule exists" note is retired.
- **Origin-unknown laws:** keep all.

## §5 THE SITTING AGENDA (deduplicated, by consequence)
1. **Write-path launch mode (C5 / L62 / 09-21 P-a).** First: law = `acceptEdits` + allowlist. Second: law = mode stated on the line, never bare; the mode itself waits for a deny-unlisted scratch test (the record calls `acceptEdits` dialogs L63 breaches). *Both:* never bare `--bg` on a write path.
2. **Routing tribunal date (C11).** Agreed: frozen until then; name the date.
3. **L34 (C1)** → the desk launch row is the spawn row until sessions-as-jobs ships. Agreed: YES.
4. **L58 / SESSION-CLOSE / NOW (C2, §8)** → hub proposes and desk applies; NOW is a ≤1,500 snapshot. Agreed: YES. Also fix `CTO-DESK-WAKEUP.md` step 8's numbering line (§2 #1).
5. **L37 (C3)** → classifier is a gate, not an approval. Agreed: YES.
6. **L7 (C13)** → promote chat-"approve" + `--sha256`. Agreed: YES.
7. **L43 (C10).** First: KEEP. Second: RETIRE the count. *This comparison favours KEEP* (§1 #2).
8. **L46 max age (C6)** → 3 days. Agreed: YES.
9. **L54 / L68 (C12)** → the gate-branch exception. Agreed: YES.
10. **L12 (C15).** First: restate (the tribunal finishes, scope is cut). Second: retire.
11. **One-sentence fixes, as a block:** L28, L32, L53, L59, L19, L62 (C9), L55 (push-deny), L35/L67/L71/L72 amendments, the hub/CoS definitions (§2 #2). Agreed: YES.
12. **New L75 "fix rounds classify first" (09-20 P-c).** First: ADD. Second: practice.
13. **09-21 P-d sittings, D5 (`date`), D6 (viewer), K4 (loudness line).** First: law. Second: practice / index. Low consequence.
14. **The 382-clause trace before the desk applies anything** (audit §5; neither pass made one). *Both passes' evidence:* needed — clauses have been dropped twice. Recommend a Sonnet trace hub against whichever draft he rules, or his explicit waiver.
