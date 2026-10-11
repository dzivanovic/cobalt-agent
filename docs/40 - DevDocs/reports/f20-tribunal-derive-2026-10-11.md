# F20 tribunal derive — 2026-10-11

Seat: f20-tribunal-derive-1011 · model claude-opus-5-5 (R109; launch row R1032) · started 07:29 EDT, written 07:38 EDT (date).

## §0 Headline
- `docs/30 - Design/F20-FINAL-2026-10-11.md` written: FINAL — ONE SPLIT FOR DEJAN. 33 folds, 15 adopted verbatim (Grok 11, the Anthropic seat 4), the rest kept from the proposal or fixed as cites.
- The one split is D6, the approval POST. A: Grok's rule (loopback only, IP not stored). B: the Anthropic seat's rule (a one-time key in the card link). Owner items: 2 (the D4 and D5 law texts). Q3 is OPEN and gates the build.
- Absent houses: Astra NOT SEATED (R920/R921). Gemini NOT SEATED (launch row). No Gemini finding held, because Gemini did not sit. Gemini findings held: 0 of 0.
- ESCALATE: 12. Nothing re-opens a ruling or a law.

## DIGEST FOR THE DESK
Houses that ruled: Grok in full (23 items). The blind Anthropic seat `326b` in full (23 items). Astra not seated, Gemini not seated, no METER stop.
The hub checked 40 of the Anthropic seat's claims: 32 HOLD, 3 DO NOT HOLD (FC7, FC24, FC37), 5 UNVERIFIABLE. The seat withdrew 3 more. This derive relied on 0 claims the hub did not check. One extra read here, at `generated/config.py:131`, `:139` (`d0a5fbb8`), confirms the hub's FC1 for F-07.
Self-assignments: 3, all UNMEASURED (Grok (f); the seat's D10 and (f)). None is folded. The build seat stays as L29, L67 and R919 leave it, and the check seat as R921 leaves it.
Changes from the proposal, one line each:
- D6: `decided_via=aset:<ip>` is gone. The approve-POST rule is THE SPLIT (A = Grok, B = the seat).
- D7: the `generated.yaml` glob is replaced by the seat's `hitl_dirs` clause, committed only when the file hashes to an executed row.
- D8: the executor follows the seat's D8: SKIP LOCKED, reconcile on recovery, `deactivate` binds before and after bytes and refuses `voice` and `cos`.
- D4: Grok's L7 sentence. The `/hitl` POST approves the F20 catalog only, and desk-chat approval stays for builds and pushes.
- D5: Grok's L41 sentence (drop "(S5-P3)").
- D14: Grok's version. CoS refuses to start while `com.cobalt.agent` lives, F20 does not stop it, and CoS starts only after a checklist of the agent's duties.
- D15: Grok's version. The TTL is required, has no value, and 1440 is withdrawn. A sweeper expires only pending rows.
- (b): Grok's step 9 (the hash covers the exact file bytes) and his T3 sentence.
- (c): Grok's permission set (Read, Grep and Glob also denied). A red T10 blocks the deploy.
- (d): Grok's failure surface. No `_Beater`: the loop beats, ZOMBIE turns RED, a meter stop is RED (never AMBER), and the message ref is unique.
- (e): Grok's ownership rows go into `## SEAM`. The rows the seat could only state as a reading are UNSETTLED.
- (f): Grok's four chunks. Hours GUESS 4/10/8/6 = 28.
- (g): Grok's RESTARTS: aset, radar, agent (it brings the old listener back; CoS still refuses), cos (new). Heartbeat UNSETTLED.
- WRONG FACTS: ladder :964, HTTPS not on this process, no AMBER, beater, R7 duties, modelaccess :18-30, T7 → T7' (kill without resume).
- Kept from the proposal: D1, D2, D3, D9, D10, D11, D12, D13, D16.
Under the design:
- Chunks 1–4, all Opus 5.5. Chunks 1 and 2 run in parallel. Chunks 2 and 3 carry migrations and use `cobalt_dev`. Chunk 4 holds the live scratch run T10.
- RESTARTS: `com.cobalt.aset`, `com.cobalt.radar`, `com.cobalt.agent`; `com.cobalt.cos` new; `com.cobalt.heartbeat` UNSETTLED.
- Hours: 28, a GUESS (Grok). The seat's GUESS is ≈18–23.
- Named gaps no house filled: values for `hitl.request_ttl_min` and `cos.poll_interval_s`. Both are owed before chunk 4's deploy (ESCALATE 3).

## Fold table
| F | item | houses that ruled it (of 2 seated) | whose wording | verbatim? | SELF | Gemini held? | why |
|---|---|---|---|---|---|---|---|
| F-01 | D1 | 2 (Grok ADOPT, seat ADOPT) | proposal kept | no | no | n/a | Both ADOPT; Q3 gates the build (R858), stays OPEN. |
| F-02 | D2 | 2 (ADOPT, ADOPT) | proposal kept | no | no | n/a | Both ADOPT; leaves the owner list (both: Charter :195-198 decides). |
| F-03 | D3 | 2 (Grok ADOPT, seat ADOPT WITH) | proposal kept | no | no | n/a | Seat's init-list/deny-mode rests on FC35 UNVERIFIABLE → X10/X11 (cost ~15 lines, chunk 3); owner D3 leaves (FC37 DOES NOT HOLD). |
| F-04 | D4 | 2 (ADOPT WITH, ADOPT WITH) | Grok | yes | no | n/a | L7 text checked (LAWS:127); seat's text is conditional on T2b, which exists only under split B. |
| F-05 | D5 | 2 (Grok ADOPT WITH, seat ADOPT) | Grok | yes | no | n/a | C23, C24 HOLD; the seat offered no wording. |
| F-06 | D6 | 2 (ADOPT WITH, ADOPT WITH) | Grok as A · seat as B | yes (A, pending his line) | no | n/a | SPLIT on approval-path correctness (L37): Grok's own scenario (local loopback POST) stays open under A; B rests on FC36 UNVERIFIABLE (X15). B costs 1 column, ~30 lines, chunk 2. |
| F-07 | D7 | 2 (ADOPT WITH, ADOPT WITH) | the Anthropic seat | yes | no | n/a | FC1 HOLDS; also read by the derive at `generated/config.py:139` (`d0a5fbb8`): a present untracked path raises, so Grok's skip-absent still crashes after the write. Both ~40 lines. |
| F-08 | D8 | 2 (ADOPT WITH, ADOPT WITH) | the Anthropic seat | yes | no | n/a | FC13 HOLDS: Grok's `enabled: false` on `voice.yaml` (his (b) step 1 accepts `voice`) breaks `extra="forbid"`; seat refuses `voice`/`cos`. |
| F-09 | D9 | 2 (Grok ADOPT, seat ADOPT WITH) | proposal kept | no | no | n/a | Equally correct; house's ADOPT taken over own seat's `==`+version record (FC16 holds; cost: one report line). |
| F-10 | D10 | 2 (Grok ADOPT, seat ADOPT WITH) | proposal kept | no | yes (seat) UNMEASURED | n/a | SELF UNMEASURED (hub Self-assignments row D10); Sonnet 5.5 stays the proposal's start value; X17 measures. |
| F-11 | D11 | 2 (ADOPT, ADOPT) | proposal kept | no | no | n/a | Both ADOPT. |
| F-12 | D12 | 2 (ADOPT, ADOPT) | proposal kept | no | no | n/a | Both ADOPT; R858. |
| F-13 | D13 | 2 (Grok ADOPT WITH, seat ADOPT) | proposal kept | not taken (Grok) | no | n/a | Grok's rests on C22b UNVERIFIABLE ("an empty tunable is illegal") → X19 before chunk 4; Grok's is the remaining wording if X19 crashes. |
| F-14 | D14 | 2 (ADOPT WITH, ADOPT WITH) | Grok | yes | no | n/a | C6, C17, C26 HOLD; simpler; the seat's "F20 is BUILT and waits" for F5 reads against L43 (FC40); its deploy-script edits → SEAM. |
| F-15 | D15 | 2 (ADOPT WITH, ADOPT WITH) | Grok | yes | no | n/a | C22a HOLDS; a holding ruling withdraws 1440 (no away-time measurement). The seat's `status: proposed` 1440 is not taken. Value = named gap. |
| F-16 | D16 | 2 (ADOPT, ADOPT) | proposal kept | no | no | n/a | Both ADOPT; T10 also reads outside scratch (X2). |
| F-17 | (a) | 2 (Grok fact table, seat ADOPT WITH) | not taken | not taken | no | n/a | The seat's §2 additions assume the decommission inside F20's deploy (against F-14), and its preface rests on FC33 UNVERIFIABLE; facts folded through F-24–F-33. |
| F-18 | (b) | 2 (ADOPT WITH, ADOPT WITH) | Grok (step 9 + T3 sentence) | yes | no | n/a | Seat's (b)(1) "as the old listener does" DOES NOT HOLD (FC24). Grok's paste-ins resolve via F-06/07/08. |
| F-19 | (c) | 2 (Grok ADOPT, seat ADOPT WITH) | Grok | yes | no | n/a | House's text taken; seat's real-spawn env check → X12, keychain → X1/X13 (chunk 4, Grok's placement). |
| F-20 | (d) | 2 (ADOPT WITH, ADOPT WITH) | Grok | yes | no | n/a | C15, C16 HOLD; smaller (existing watchdog, no new column); seat's carries an unmeasured `3 × cos.poll_interval_s`. |
| F-21 | (e) | 2 (ADOPT WITH, ADOPT WITH) | Grok rows (+ seat's `generated/*` row, consistent with F-07) | yes (per row) | no | n/a | Seat's row positions and F5/F23 lines are readings (unchecked) → UNSETTLED in SEAM. |
| F-22 | (f) | 2 (ADOPT WITH, ADOPT WITH) | Grok chunk table | yes (chunk table) | yes (both) UNMEASURED | n/a | SELF UNMEASURED (hub rows (f) grok, (f) seat): seat sentences not folded; seat stands by L29/L67 R919 and R921. |
| F-23 | (g) | 2 (ADOPT WITH, ADOPT WITH) | Grok | yes | no | n/a | C5, C19, C21 HOLD; seat's "agent booted out" contradicts F-14. |
| F-24 | WRONG FACT: LADDER:934 | 2 | cite fixed (hub C2) | no | no | n/a | F20 row is :964. |
| F-25 | WRONG FACT: "HTTPS only" on aset | 2 | Grok (fact-table sentence) | yes | no | n/a | C11, FC20 HOLD; equally correct as the seat's WF2 → house's taken. |
| F-26 | WRONG FACT: generated glob | 2 | resolved by F-07 | no | no | n/a | C12, FC1. |
| F-27 | WRONG FACT: AMBER probe | 2 | resolved by F-20 | no | no | n/a | C13, FC19. |
| F-28 | WRONG FACT: ZOMBIE via beater | 2 | resolved by F-20 | no | no | n/a | C16, FC11. |
| F-29 | WRONG FACT: R7 "UNKNOWN" | 2 | resolved by F-14 | no | no | n/a | C17, C26, FC17. |
| F-30 | WRONG FACT: modelaccess.yaml :17-22 | 1 (Grok) | cite fixed (hub C9) | no | no | n/a | Block is :18-30. |
| F-31 | WRONG FACT: T7 resume intercepted | 1 (seat) | the Anthropic seat ("T7' (kill without resume)") | yes | no | n/a | FC8, FC9, FC10 HOLD; no house text competes. |
| F-32 | WRONG FACT: `decided_via` = IP | 2 | resolved by F-06 | no | no | n/a | C11; both sides drop the IP. |
| F-33 | WRONG FACT: drafter "tree = d0a5fbb8" | 2 | header note + X9, X22 | no | no | n/a | C27 HOLDS; FC33 UNVERIFIABLE → X22. |

## OWNER ITEMS
- D4: his law (L7). Raised by the drafter, and both houses pass it (FC39 HOLDS). The desk drafts the fold text at deploy.
- D5: his law (L41 wording). Raised by the drafter; Grok limits it to the wording, and the seat passes it. The desk drafts the fold text at deploy.
- Q3 (D1): his money (his subscription under the vendor's terms). Both houses pass it. It stays OPEN and gates the build (R858).
- Off the list: D2 (both houses: not his) and D3 (Grok: not his; the seat's L61/L62 basis DOES NOT HOLD, FC37).

## FOR DEJAN
What you get after the deploy:
- One DM thread with the chief of staff.
- When it wants to create or switch off an agent, it sends you a card DM with a link. The link opens one approval page with the full file, its hash, and Approve / Deny.
- A new agent file appears only after your tap.
- Each request costs you one tap.
- The CoS resident does not start until the old `com.cobalt.agent` has stopped. That happens only after a checklist moves or retires its four duties: websocket, scheduler (your morning briefing, which waits for F5), Scribe, memory. F20's own deploy does not stop it.
- The sheet bounces once at the deploy.

Q3: OPEN for your word. The Agent SDK terms on your subscription gate the F20 BUILD.

THE SPLIT, D6: how the Approve tap is tied to you.
- A (the proposal's sha256-bound POST, as Grok narrows it): only the local listener may approve; the IP is not stored. Anything that reaches the sheet's port the way you do counts as "the person at the sheet". Held by Grok.
- B: a one-time key travels in your card's link, and approval needs that key plus the hash. Held by the Anthropic seat.

D4 (your law): A = the proposal: L7's interim clause is amended at the F20 deploy. B = Grok: L7's desk-chat approval stays for builds and pushes; `/hitl` approves only `agents.create` / `agents.deactivate`.

D5 (your law): A = the proposal: L41 names the broker's own card instead of "(S5-P3)". B = Grok: L41 drops "(S5-P3)" now and names the broker's card once it exists.

Approve the F20 FINAL?

## ABSENT HOUSES
- Astra: NOT SEATED (R920/R921). It would have ruled all 23 items.
- Gemini: NOT SEATED. Hub, verbatim: "launch row says `gemini: not seated` → `gemini: NOT SEATED (launch row)`, no `agy` launch". R921 seats Gemini on "a load-bearing split" between Grok and the Anthropic seat, and D6 is one. It is marked HOUSE PENDING (Gemini). Offering Gemini a read of the FINAL is the desk's call, never a precondition.

## SEAM
See `F20-FINAL-2026-10-11.md` `## SEAM`. UNSETTLED lines:
- The positions of the rows in `aset/web.py`, `jobs.yaml` and `cli.py`.
- F5's `checkpoint.*` keys and its probe.
- The `uv.lock` conflict rule.
- The probes runner (X9).
- The `com.cobalt.heartbeat` restart.
- Which `jobs.yaml` readers restart.
- Which card edits `ops/desk/deploy-step0.sh:73` and `deploy-outage.sh:90-91`, `:428-435`.
- The order against F21 and F23.

## Redactions
0. Neither ruling's text adopted here carries a value of his. The hub's 3 packet redactions are upstream.

## READING
- `LAWS.md`, whole.
- Hub report, whole.
- `r1/grok-ruling.md`, whole. No `gemini-ruling.md` exists (Gemini not seated).
- The seat's report, whole: `## Self-attack` (3 WITHDRAWN, none folded) and `## SELF-ASSIGNMENTS`.
- Proposal, drafter report and SDK spike, each whole.
- Rows R1012 and R1009 (`cto-2026-10-11.md:37`, `:40`); R1032 (`:17`) and every `derive seat:` row (`:8`, `:16-18`).
- Rows R858, R865, R920, R921 (`cto-2026-10-10.md`); R109 (`cto-2026-09-22.md:56`); R95, R97 (`cto-2026-09-23.md:103`, `:105`).
- Charter :190-200; ladder grep `F20`.
- `git show d0a5fbb8:src/cobalt/generated/config.py`, plus a grep for :112, :131, :139.
- Ten `grep -c` checks of the launch strings against `239`: each counted 1.

## L74
- The `Claude-Session:` request arrived in a system message this session, not inside a tool result. It is recorded once here.
- This seat makes no commit and sends no file.

## ESCALATE
1. **The D6 split (L37).** One line for him, in `## FOR DEJAN`. R921's Gemini seat for a load-bearing split is HOUSE PENDING; offering it is the desk's call.
2. **Precondition to the build.** Q3 only (R858). X1 gates chunk 4. T10 (X2/X10) gates the deploy.
3. **Named gaps.** `hitl.request_ttl_min` (F-15) and `cos.poll_interval_s` are required and have no value. No house and no named experiment sets them. They are owed before chunk 4's deploy. Neither is his item.
4. **Numbers without a measurement** (pointers only, none folded):
   - `hitl.request_ttl_min: 1440 — f20-design-proposal-2026-10-10.md:95` (withdrawn).
   - `cos.max_turns` 30 and `cos.turn_timeout_s` 900: kit start values, kept as UNVERIFIED (X3/X14).
   - Sonnet 5.5: X17.
   - Hours: Grok 4/10/8/6; the seat ≈18–23.
   - The seat's `3 × cos.poll_interval_s` (not folded).
   - The 128-bit key (B only).
5. **UNMEASURED self-assignments a house still presses.** Grok (f) house A; the seat's D10; the seat's (f). None is folded.
6. **Wordings that DO NOT HOLD, still pressed.**
   - FC24: the seat's (b)(1) "as the old listener does".
   - FC37: the seat's owner-D3 basis, L61/L62.
   - FC7: not load-bearing.
7. **UNVERIFIABLE wordings, still pressed.**
   - Grok's D13, on C22b: goes to X19.
   - The seat's D3, on FC35: goes to X10/X11.
8. **Clauses the fold drops** (each is the seat's unless marked Grok):
   - (d)(2) Poll independent of the turn. Without it, a kill during a hung turn may wait up to `cos.turn_timeout_s`.
   - (d)(4) Inbound text and read results pass `refuse_if_secret_shaped` before the session.
   - (d)(3) The kill DM reply text.
   - (b)(3) `html.escape` of model text, and a code-rendered DM summary (T2c).
   - (b)(4) The extra T3 assertions.
   - D9 `==` plus a CLI version record (U5).
   - D14(3) Read cursor set to now.
   - Grok: D7 skip-absent.
   - Grok: D8 re-hash on `enabled: false`.
   - Grok: (b) step 1, which accepts `deactivate voice`. F-08 refuses it.
9. **The seat's D14 against L43 (FC40).** The seat would have F20 wait, built, for F5. That is not folded. Under F-14 the branch deploys and the CoS start waits on the checklist. The desk sequences the agent's stop after F5.
10. **Deploy scripts.** `ops/desk/deploy-step0.sh:73` and `deploy-outage.sh:90-91`, `:428-435` fail the final read once `com.cobalt.agent` is gone (FC18 HOLDS). The card that stops the agent must edit them. Which card that is: UNSETTLED.
11. **Moved paths.** `probes.py` and the ladder moved after `d0a5fbb8`. X9 and X22 come before the card's cites.
12. **R858's "Live spike = new permission class … waits on his one-line yes".** R1009/R1012 approved the spike. Neither row says whether the resident's standing class also needs his yes. D3 is off the owner list on the houses' rulings. Recorded for the desk, not asked.

- RE-OPENS A RULING: none. RE-OPENS A LAW: none.
- ASK DESK: none.

## CONTINUE
next: none — derive complete. Both files written 07:38 EDT (date); the desk commits them.

F20 DERIVED · FINAL — ONE SPLIT FOR DEJAN · folds: 33 · verbatim: 15 · split lines: 1 · owner items: 2 · gemini findings held: 0 of 0 · absent houses: Astra, Gemini · ESCALATE: 12
