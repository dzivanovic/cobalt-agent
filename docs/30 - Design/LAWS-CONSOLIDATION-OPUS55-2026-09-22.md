# LAWS CONSOLIDATION — SECOND PASS (Opus 5.5) · 2026-09-22

Seat `laws-second-pass-0922` (`claude-opus-5-5`), prompt `prompts/2026-09-22/43-laws-consolidation-second-pass.md`. PHASE 1: written BLIND — the first pass (`LAWS-CONSOLIDATION-PROPOSAL-2026-09-22.md`, its `-LAWS-draft.md`, `reports/laws-consolidation-draft-2026-09-22.md`) was not opened before this file and its draft were written. A PROPOSAL (L39, L58): nothing here is law until he rules and the desk applies it. Full proposed file: `LAWS-CONSOLIDATION-OPUS55-2026-09-22-LAWS-draft.md`.

Sources read in full: `LAWS.md` (407 lines), `LAWS-HISTORY.md` (173), `reports/laws-audit-2026-09-20.md` (687), `close-2026-09-20.md` + `close-2026-09-21.md` "Laws fold — PROPOSED, NOT APPLIED", `topics/cto-desk.md` lines dated 09-19…09-22 (lines 69–106), `SESSION-CLOSE.md`, `CTO-DESK-WAKEUP.md` step 8. Spot reads: `cto-2026-09-22.md` §4 R3/R4/R77, `prompts/2026-09-21/65-setups-one-build.md` line 1, `INDEX.md`, `areas/cobalt.md` `## NOW` (measured).

## §0 What changes

| count | value |
|---|---|
| laws before → after | **74 → 74** (no new number; 4 pending proposals adopted as AMENDMENTS of L35, L67, L71, L72) |
| audit §2 contradictions | **15: 11 RESOLVED (wording below) · 4 OPEN FOR DEJAN** (C5, C10, C11, C15) |
| audit §3 clutter | 15: 10 adopt (6 as amended) · 3 decline/defer · 1 leave (routing) · 1 = C8 |
| clauses retired from law | **0** (none proven dead; L12 is OPEN, not struck) |
| replaced wordings moved to LAWS-HISTORY | **8** (L7 status note, L34, L41 heading word, L53.2, L59.5, L17's 09-07 duplicate, "Fold-at-session-close" text, staging header) |
| new laws | **0** — 3 proposals declined as law and kept as desk practice (P-a/P-c of 09-20, P-d of 09-21) |
| found beyond the audit (dated after it, or missed) | **9** (§2 rows N1–N9) |

Headline finding: **audit C5 is inverted by later evidence.** A bare `claude --bg` with no `--permission-mode` comes up in AUTO mode (`topics/cto-desk.md` 2026-09-21, "A BARE `claude --bg` … COMES UP IN AUTO MODE"; `prompts/2026-09-21/65-setups-one-build.md:1`, first launch `FAILED PREFLIGHT`). The audit's recommended standard ("no flag, allowlist only", laws-audit §2 C5 "Practice follows A, by accident") is therefore the auto mode L29.6 forbids, and the 09-19 hubs it cleared ran in auto mode. And the working alternative, `acceptEdits` + allowlist, ASKS on an unlisted Bash instead of denying (`topics/cto-desk.md` 2026-09-22 lesson (1)), which L63 forbids. No proven unattended write-path shape exists today → C5 is OPEN.

## §1 Principles

1. **His mechanism ruling stands** (LAWS.md Preamble, verbatim 09-13): one entry per law, amended in place with a date, replaced wording verbatim to LAWS-HISTORY. Its sentence "the fold is a hub job at every session close" is superseded in practice by L58 (09-16) — the Preamble stays verbatim (it is a quotation); the "Fold-at-session-close" section below it is rewritten (row N1).
2. **Numbers are never reused, and none is retired here.** Merging laws (audit K1/K3/K6) is declined: `PROPOSED-n` aliases were still being written days after renumbering (laws-audit §3 K8: PROPOSED-5 ×23), so renumbering costs more confusion than it removes. A **subject index** at the top of the file gives "one place to look" without moving a number.
3. **Nothing is struck without the audit row proving it dead.** No audit row proves any clause dead; L34 is proven *unobeyed* (§2 C1), which argues for amending, not striking.
4. **Routing-tribunal clauses listed and left, text unchanged:** L5 (whole), L24's rung sentence, L26 (whole), L27.7–.8 (the Codex routing sentence), L29 (whole, "carried as written") and L49's heading marker (LAWS.md L5, L24, L26, L27, L29, L49; fold rule, LAWS.md "Fold-at-session-close": refuse a fold touching "L29's routing substance"). L29.6 ("never auto mode on a write path") is a permission rule, not routing — still, this pass does not edit L29; the C5 fix lands in L62.
5. **Every clause of the current file is carried** (audit §5 "What a rewrite must prove" 1–5); the draft adds text and moves replaced wording to HISTORY, it deletes no clause. The five restored clauses (L28.7, .8, .12, .13, L29.6) are unchanged in the draft.

## §2 Contradiction register (audit §2 C1–C15, plus N1–N9 found by this pass)

| row | disposition |
|---|---|
| **C1** L34 vs L61.1 | **RESOLVED — amend to today's mechanism** (§4). Proposed L34: "Every spawn is recorded as a row BEFORE it starts: house, role, model, worktree (or cwd), required artifact (report path + stop-line shape). A Cobalt pipeline job's row is its `cobalt_jobs` row; an agent session's row is its launch row in the day's desk report (`cto-<date>.md`), written by the desk before `claude --bg`. No row, no launch. The day agent sessions get a `cobalt_jobs` row (BACKLOG sessions-as-jobs gap, `cto-2026-09-16.md` §4 row 10), that row replaces the desk-report row." Evidence the desk row already exists: `cto-2026-09-22.md` R5, R77 ("DESK LAUNCH" rows). |
| **C2** L58 vs SESSION-CLOSE 3–4 | **RESOLVED — keep L58; the procedure is re-cut** (§8). Practice already follows L58 on 3 of 3 closes (laws-audit §2 C2). No law text changes; SESSION-CLOSE steps 2-apply, 3, 4 become the desk's. |
| **C3** L37 vs the classifier | **RESOLVED** — add to L37: "The harness permission classifier is a gate, not an approval: it may refuse; what it lets through stays bound by every approval this file requires, and no approval this file requires (HITL, push, deploy, settings) is ever satisfied by it." Grounds: L55.3 (09-03) and L37 (09-07) target different things (laws-audit §2 C3 fields 1, 3); the classifier's own-judgement behaviour is measured (`cto-2026-09-19.md` §61–§62, cited by the audit). |
| **C4** L53.2 "cap" | **RESOLVED** — L53.2's "never a cap" → "never the pool cap". Its origin sentence names only the 50-name pool cap (LEDGER:1140 per laws-audit §2 C4 field 1); L53.1 already governs the rpm ceiling and cadence (ruled, never silent) and `TotalDemandExceeded` enforces the total. Old wording → HISTORY. |
| **C5** L29.6 vs the launch shapes | **OPEN FOR DEJAN.** Reading A: keep "never auto mode on a write path" for every write path, dev included — unattended write-path hubs then need a mode that DENIES unlisted commands; `acceptEdits` ASKS (cto-desk 09-22 lesson (1)) and breaks L63; no-flag = auto (cto-desk 09-21). Reading B: narrow L29.6 to production write paths (dev migrations/tests may run in auto, classifier-gated). **Recommendation: A**, and an ops scratch test this week of a deny-unlisted shape (UNCITED — verify whether the harness offers a `dontAsk`-style mode); meanwhile the 09-22 interim stands (allow strings in the prompt body, "unlisted = do not call it", 2 h look). Wording that lands either way, in L62: "A launch line states `--permission-mode` explicitly; a bare `claude --bg` is auto mode. The prompt's SEAT prose quotes the mode from its own launch line; prose and line never disagree." (laws-audit §5 ESCALATE 4). |
| **C6** L46 vs L68 | **RESOLVED boundary** — add to L46: "L46 governs one agent's own branch (committed, clean tree at run end, never outliving its deploy); several agents' parallel branches are lawful and their seam is governed by L68." The branch MAX AGE the audit asks for is new policy → §9 item 7. |
| **C7** L28 vs L58/L65 | **RESOLVED** — add to L28: "This law binds Cobalt the program's writes. The CTO desk's hand edits under L58 (memory folder, LAWS) and L65 (his notes, on his ruling) are not a Cobalt write path; they carry their own trace (desk report before/after) and end when a Cobalt memory command ships (L58)." Already stated in L65's own text (laws-audit §2 C7 "Practice follows"). |
| **C8** L44 vs L59.5 | **RESOLVED** — L59.5 "workers never read the whole memory folder" → "workers need not read the whole memory folder; the card is the working set, never a fence, and a worker opens any memory file it needs." His origin words: "so it can retrieve anything else itself" (laws-audit §2 C8 field 3). Old wording → HISTORY. |
| **C9** L62 vs L61.2 | **RESOLVED boundary** — add to L62: "L62 binds every session the desk starts. The desk itself may ask Dejan, and only him, for a permission grant it lacks — never for a ruling already in force (L73) — and may never grant itself a permission it was just denied." Last clause = `topics/cto-desk.md` 2026-09-19 ("THE DESK MAY NOT GRANT ITSELF A PERMISSION IT WAS JUST DENIED"). |
| **C10** L43.1 | **OPEN FOR DEJAN.** Reading A: keep "one production deploy per evening"; every extra deploy is his per-case override (L73). Reading B: retire the count; keep R47's packaging (everything ready lands as one set) as the default and L43.2's radar window + L66 as the safety. Evidence: overridden 09-19 (R32, three deploys) and again **09-22 R3** ("continue building and deploying through the day", `cto-2026-09-22.md` R3, after the audit). **Recommendation: B** — the count now fails more often than it holds, and the restart window is where the production risk lives. |
| **C11** routing cluster | **OPEN FOR DEJAN — left.** Not consolidated (§1.4). Recommendation: rule the routing tribunal's date; it has been open 9 days (since 09-13). |
| **C12** L54.5 vs L68.5–.7 | **RESOLVED boundary** — add to L54: "Exception, L68: a gate branch combining sibling branches merges `main` into itself and is fast-forwarded as a whole; its rollback is one `git revert -m 2` of that merge. Every other merge is rebase-then-ff." Deploy report template updated with the second rollback shape (ops, same ruling). |
| **C13** L7 token | **RESOLVED** — promote the interim clause from the status note into L7's law text and name `--sha256` as its mechanical half (LEDGER:1288 per laws-audit §2 C13 "Practice follows"). Status note reduced to the fact that no token mechanism exists. |
| **C14** L19 vs CONTINUE | **RESOLVED boundary** — add to L19: "A CONTINUE relaunch re-issues the unchanged prompt file with one resume line; it never edits the file. Any change to the file is a full re-issue." |
| **C15** L12 | **OPEN FOR DEJAN.** Reading A: restate — "each design phase is capped by ruling at its start; when hit, the tribunal round in progress completes and the design ships with what is decided". Reading B: retire L12 to HISTORY — dormant since 09-04 (L12's own 09-13 amendment), and L67's three-round cap now bounds design time. **Recommendation: B.** |
| **N1** LAWS.md "Fold-at-session-close — hub job" section vs L58.7 | **RESOLVED** — the section tells the HUB to "rewrite the entry in place" (LAWS.md line 406); L58.7 says "A hub never writes the memory folder or this file". Rewrite: "The close hub PROPOSES (report section `Laws fold — PROPOSED, NOT APPLIED`, exact fold text per item); the CTO desk APPLIES what he approved (L58)." Refusal triggers unchanged. Old text → HISTORY. Not in the audit. |
| **N2** `CTO-DESK-WAKEUP.md` step 8 vs L58's 09-18 numbering | Procedure fix, no law change: step 8 says "number only if Dejan assigned one, else listed as `PROPOSED — number owed`"; L58 [amended 2026-09-18] gives the next free number in advance. Step 8 should say "next free number (L58)". Not in the audit. |
| **N3** `SESSION-CLOSE.md` step 7 vs L55 (09-19) | Procedure fix: step 7 "Dejan pushes — `git push` is his" predates L55's push clause (desk pushes on his word). Re-cut with §8. Not in the audit. |
| **N4** audit C5 factual inversion | See §0. The audit's "no flag = allowlist is the gate" (from `cto-2026-09-19.md` §63) is contradicted by the 09-21 finding that no flag = auto. Not a law edit; it changes C5's disposition. |
| **N5** L43 overridden after the audit | 09-22 R3 (see C10). |
| **N6** L67's Anthropic design seat vs 09-22 R36/R76 | L67 [09-21]: design keeps "Fable (Anthropic, still asked per case, 09-20 R18)"; R76 (09-22): the desk asks "Opus 5.5 or Fable?" per Fable seat during his trial. A per-case override during a trial (L73) — **no law edit**; the trial's end is his. |
| **N7** `## NOW` size | measured 61,359 chars (`awk '/^## NOW/…' areas/cobalt.md | wc -c`, this pass) against SESSION-CLOSE step 3's ≤1,500. §8 collision 2. |
| **N8** "hub" and "CoS" used for different things | L22.6 "Cobalt code is the hub" (the model-access hub) · L36.3 "the hub the only spawner" · L61.1 the DESK starts every hub. Read literally, L36 is broken by every desk launch. **RESOLVED** — define in "How to read this file": "CoS = the CTO desk; hub = a session the desk starts to run one job; in L22 'hub' means Cobalt's model-access layer." L36 then reads "the desk the only spawner of hubs; a hub launches only the house seats its prompt names". |
| **N9** close-2026-09-21 P-d overtaken | His 09-22 R4 ("Laws are all mine") re-made the laws a sitting, reversing P-d's fold text for the laws. See §6. |

## §3 Clutter register (audit §3 K1–K15)

| K | disposition |
|---|---|
| K1 launch cluster | **ADOPT AS AMENDED** — no merge (§1.2). Subject index line "Launch & permissions: L55 L61 L62 L63 L64"; L61's duplicate "never `bypassPermissions`" becomes "(L55)". |
| K2 L35/L70 | **ADOPT AS AMENDED** — no merge; L35 gains "Companion: L70 (a claimed failure is not a failure either)". |
| K3 merge cluster | **ADOPT AS AMENDED** — no merge; index line "Merge & deploy: L43 L46 L54 L66 L68"; C6 and C12 boundaries carry the substance. |
| K4 loudness | **DECLINE** — four domain rules, each correct where it sits; index line "Loud failure: L1 L9 L18 L25". |
| K5 L7/L8 | **ADOPT** — one line each: L7 = promotion rule, L8 = render rule. |
| K6 L17/L39 | **ADOPT AS AMENDED** — L17's `[amended 09-07, L39]` sentence (a copy of L39.1–.5) → HISTORY; L17 keeps a pointer "Turn limit and termination: L39". L17's O5 synthesis sentence stays. |
| K7 routing | **LEAVE** (§1.4). |
| K8 PROPOSED-n aliases | **ADOPT** — drop "(alias PROPOSED-n)" from L62–L67 headings; H-PartVIII-PROPOSED keeps the map; a prompt writing `PROPOSED-` is corrected at dispatch. |
| K9 source lines | **DEFER** — moving every citation (a full rewrite) is exactly the operation that dropped clauses twice (laws-audit §5 "What a rewrite must prove"); cheaper later, with the trace file. |
| K10 `O<n>` | **ADOPT** — define in "How to read this file": "`O<n>` = objection n of the 09-13 ledger tribunal, ruled by him that day". |
| K11 L41 "REPLACED" | **ADOPT** — heading reads "(ruled 09-10; corrected 09-11; replaced 09-13)" in lower case, prior text in H-L41-v2. |
| K12 L15.5 | **ADOPT** — the struck clause shown in place as `~~vault/.env/personal layer excluded~~` (INDEX rule 3). |
| K13 L32 vs L44 | **ADOPT** — add to L32: "'User data' governs what leaves this install for other Cobalt users; it never restricts a house working on this install (L44)." |
| K14 staging header | **ADOPT** — both files' "Status: FINAL, staged here pending placement" → HISTORY. |
| K15 | = C8. |
| §2c status notes → STATE file | **DECLINE** — one more file for a small model to find. Instead: L7's imperatives promoted (C13); the other four notes relabelled `State (not law):` one line each, kept beside their law. |

## §4 Never-obeyed laws

| law | one recommendation | cost |
|---|---|---|
| **L34** (never obeyed, laws-audit §2 C1; §4b) | **AMEND to today's mechanism** (C1 wording): the desk launch row IS the spawn row until sessions-as-jobs ships. Not BUILD now (blocks every launch until a DB registry exists); not STRIKE (its purpose — an auditable spawn — is live and the row exists in practice). | ≈0: the desk already writes launch rows (`cto-2026-09-22.md` R5, R77); one added field set (house, role, model, cwd, artifact). |
| L25.8 reason-class column | keep; state line "owed" (LAWS.md L25 status note, LEDGER:1177). | build item, already on record |
| L55 push gate | settled since the audit: `settings.local.json` allow + nine denies exist (`topics/cto-desk.md` 2026-09-20 R12). Status note updated. | 0 |
| L36 (literal reading) | resolved by the N8 definitions. | 0 |

## §5 Origin-unknown laws (laws-audit §5, 10 + 2 partial)

L2, L14, L16, L18, L19, L20, L21, L24, L26, L57; partial L54 (O17), L34/L37. **Recommendation: KEEP ALL, no edit beyond C1/C14.** Unknown origin is not proof of death (§1.3); L2/L14/L16/L18 are Cobalt's product architecture (TRIAGE/08-28 register), L57 has 11 test references (laws-audit §4a), L24/L26 are frozen (§1.4). One-line `State (not law): origin not recorded beyond LEDGER:<n>` is NOT added — it would invite the argument L37/L39 forbid.

## §6 Pending proposals

| proposal | disposition | fold text |
|---|---|---|
| 09-20 P-a desk delegates | **DECLINE as law** — a desk-seat behaviour rule, already practice (`topics/cto-desk.md` 2026-09-20 R16–R18) and now bent by R36/R76 (Opus 5.5 trial). Keep as practice. | — |
| 09-20 P-b sibling seam | **ADOPT as L72 amendment** (evidence close-2026-09-20 §35) | "[amended <date>] Where two sibling builders share a name, shape or interface, that seam is settled in one document both prompts cite BEFORE either launches; a shared seam a builder can only record as a READING is a real dependency (this law). L68's stacked gate proves the seam; it does not decide it." |
| 09-20 P-c fix rounds classify | **DECLINE as law** — a drafting procedure; practice already (`topics/cto-desk.md` 2026-09-21 lesson (3)); UNCLASSIFIED/UNPROVEN leg is L70. | — |
| 09-20 P-d breadcrumb | **ADOPT as L71 amendment** | "[amended <date>] A run's resume breadcrumb or progress marker is never in a stop-line shape and never its report's last non-blank line while the run is unfinished; it lives under `## CONTINUE`, and the prompt pins the in-progress last line." |
| 09-20 P-e catalog view | **ADOPT AS AMENDED, as L35 corollary, generalised** (the same scoped-read error class as 09-19 P4, per close-2026-09-20 P-e) | "[amended <date>] A read scoped by privilege, filter or sample is never evidence that something does not exist: absence is claimed only from a read that could have seen it (for Postgres, `pg_catalog`, not `information_schema`), or stated as 'not visible to this reader'." |
| 09-21 P-a acceptEdits shape | **DECLINE as written** — its premise ("a Bash call outside the list is denied") is contradicted the next morning (cto-desk 09-22 lesson (1): `acceptEdits` ASKS; a prompt reached him, `cto-2026-09-22.md` 07:0x). UNPROVEN (L70). The part that holds (state the mode on the line) lands in L62 via C5. | — |
| 09-21 P-b pacing | **AGREE: nothing to fold** (already L43 [09-21]). | — |
| 09-21 P-c non-ruling rounds | **ADOPT as L67 amendment** | "[amended <date>] A turn that ends in METER, HARNESS, TIMEOUT or another stop without a ruling does not use one of that house's three rounds; only a turn that produces a ruling counts. Floor, shrink-to-two and the cap's number unchanged." |
| 09-21 P-d sittings named | **DECLINE as law** — plate management (desk practice, 09-20 PENDING SITTINGS line), and its fold text sends the laws to a tribunal, which R4 (09-22) reversed. Practice line amended: "a sitting = an item he names himself the output authority of (today: LAWS, DRC)". | — |

## §7 Desk-practice candidates (cto-desk.md 09-19…09-22), test: can a small model obey it mechanically?

| line | verdict |
|---|---|
| 09-19 "never ask him to re-decide a law" / "minimum idle time" | already law (L73) — no action |
| 09-19 R21 desk seat = Fable / 09-22 R36, R76 | seat choice, trial running — practice, not law (N6) |
| 09-19 "desk may not grant itself a permission it was denied" | **LAW** — mechanical, cross-house; folded into L62 (C9) |
| 09-20 R12 push rule exists / "every hub line carries `--disallowedTools "Bash(git push*)"`" | **LAW** — mechanical, grep-checkable; add to L55's push clause as one sentence |
| 09-21 bare `claude --bg` = auto | **LAW (fact-bearing clause)** — folded into L62 (C5 wording) |
| 09-21 (9)/(8) `date` before every time written | practice (cannot be checked from outside the session) |
| 09-21 afternoon (1) watch ceiling = expected + 15 min | practice (desk tooling) |
| 09-21 afternoon (5) text in a hub's input box is never his word | already L61.7/L74.2 — no action |
| 09-22 lesson (1) acceptEdits asks | state, feeding C5 — ops scratch test |
| 09-22 midday (6) approval lists one at a time | practice |

## §8 The two procedure collisions

1. **L58 vs SESSION-CLOSE steps 2–4 (and 7).** Keep L58 (3 of 3 closes already obey it, laws-audit §2 C2). Re-cut `SESSION-CLOSE.md` (repo procedure, the desk edits it under L65's spirit only if he approves; it is not a vault note): HUB steps = 1 ledger appendix · 2 **proposals only** (`Laws fold — PROPOSED, NOT APPLIED`, exact fold text) · 4a ladder/backlog · 5 measure · 6 commit; DESK steps = 2-apply (L58), 3 NOW, 4 areas/topics, 7 push on his word (L55). The desk's step 8 reconcile (WAKEUP) already catches a close the desk missed. Fix N2 (numbering) in the same edit.
2. **NOW's "never delete" vs its size cap.** INDEX rule 3 ("supersede by ~~mark~~, never delete") has been applied to NOW's mid-day lines ("kept per rule 3", `areas/cobalt.md` NOW), turning a ≤1,500-char snapshot (SESSION-CLOSE step 3, "rewrite in full, never append") into a 61,359-char log (N7). **Recommendation:** NOW is a SNAPSHOT, exempt from rule 3: the previous NOW is preserved by the close report and the ledger (git), not inline; mid-day desk updates REPLACE the top block and copy the superseded block into `cto-<date>.md` §5. A memory-rule change → his (§9 item 9); applied by the desk (L58).

## §9 What only he can rule (one per message; recommendation first)

1. **C11** — date the routing tribunal (open 9 days); this sitting leaves L5/L24/L26/L27.7–.8/L29/L49's marker untouched. *Rec: this week, parallel lane (L72).*
2. **C5** — L29.6 for every write path (A) or production only (B)? *Rec: A, plus an ops scratch test of a deny-unlisted launch mode this week.*
3. **C1 / L34** — amend to "the desk launch row is the spawn row until sessions-as-jobs ships". *Rec: yes.*
4. **C10 / L43.1** — keep the one-deploy count or retire it (keep R47 packaging + radar window + L66)? *Rec: retire the count.*
5. **§8.1** — SESSION-CLOSE re-cut into hub half / desk half (steps 2-apply, 3, 4, 7 = desk). *Rec: yes.*
6. **§8.2** — NOW is a snapshot exempt from "never delete". *Rec: yes.*
7. **C6 add-on** — a branch MAX AGE (unmerged, not shipping) → ESCALATE at dispatch after N days. *Rec: yes, N = 3 (`sprint-2/radar-pool` stopped a deploy at 4 days, LEDGER:1283).*
8. **C15 / L12** — restate or retire. *Rec: retire to HISTORY.*
9. **The block** — approve as one: C2, C3, C4, C7, C8, C9, C12, C13, C14, N1, N8, K1–K6, K8, K10–K14, the four amendments (L35, L67, L71, L72), L62's mode-on-the-line sentence (C5, lands either way) and L55's hub push-deny sentence (§7). *Rec: yes.*
10. **Declined as law** — 09-20 P-a, P-c; 09-21 P-a, P-d stay practice. *Rec: confirm.*
