# Routing tribunal — derive v2 (seat `routing-tribunal-derive-0922`, claude-opus-5-5)

Started 2026-09-22 23:09 ET; v2 written 23:19 ET; report closed 23:21 ET (`date` at each step).

## §0 Headline
- **v2 written:** `docs/30 - Design/ROUTING-v2-2026-09-22.md`, derived from 25 fold rows. 17 wordings were taken verbatim: 7 from Grok, 8 from the proposal, 1 that combines the proposal with Grok's X5, and 1 from the Anthropic seat.
- **Round 2 is not needed:** no seat said DO NOT ADOPT or REJECT. The tribunal closes on Astra's Sat 09-26 read (R13). v2 is **ASTRA PENDING**.
- **Owner items: 18.** They include D1–D3, write-path scope, the n, and L31's reach. Nothing is decided here.
- **Re-test rows: 8.** Every UNMEASURED self-assignment went there, none into law: Grok 2, Gemini 1, the Anthropic seat 4, and the proposal's own row 2.
- **ESCALATE: 14.** They include the ASTRA line, RULES AN OWNER ITEM (D1; Gemini's T7), RE-OPENS A RULING (R46), and L26's bare § that the fold would refuse.

## DIGEST FOR THE DESK

**What v2 changed from the proposal, one line each:**
- L5: the proposal's text, adopted by all 3 seats [F-02].
- L21: unchanged.
- L22: **unchanged.** The proposal's phrase edit was not taken: its only ground was L31, which does not reach law text (hub check) [F-12].
- L23: the proposal's "first ASSESSED" sentence; the status note is replaced [F-09]. Grok's longer wording is O-18.
- L24: **Grok's T3.** It restores the async / CLI-bridge shapes the proposal dropped and removes the proposal's "cheapest rung" closer [F-03].
- L25: the bake-off pointer goes to "the seat table" [F-10]. The first-hop "Claude →" edit was not taken, on the L31 ground [F-11].
- L26: the proposal's text [F-13]. **Its bare "§4"/"§5" would be refused by the fold (LAWS.md:12)** — O-11.
- L27: every ceiling sentence unchanged. The routing sentence is OPEN (D2).
- L29: **Grok's T7.** The floor stays operative "until he rules D1". It restores "or higher", "never in session context", the Sonnet/Haiku clause, auto-per-session and the writer profile. .6 is kept BY NAME [F-07].
- L49: the marker is removed; the text is unchanged [F-14].
- Seat table: Grok's T4 (`seats.yaml` is the only home; `source pending <T4 build>`) and Grok's (g) precedence rule. Rows are corrected by the hub check: row 4 id, row 3 write path, row 7 → R109, row 13 id, row 14 adverse records; row 8a is added (RULED R46).
- Key: the proposal's §4, bound only after X5. Re-test: Grok's T8, which restores the "local models improve" trigger (e). Trials: Grok's T11.

**Seats that ruled round 1:**
- Grok: in full, 20 items.
- Gemini: in full. Its closing line is off-shape, and it wrote no SELF line on (a)–(h).
- Astra: METER, ASTRA PENDING (R13).
- The Anthropic seat (R109, `claude-opus-5-5`): in full, 20 items, 2 WITHDRAWN (neither folded).

**The Anthropic seat's claims:**
- The hub checked 11: 10 HOLD, 1 UNVERIFIABLE (FC11 → X12).
- Claims the hub did not check, which the derive read before using:
  - `areas/cobalt-houses.md:60`, `:66` (rows 13/14 adverse records);
  - `src/cobalt/seatusage/report.py:127` (T12 (2));
  - `bars-chunk-1a-check-2026-09-20.md:174-204` (O-6 B);
  - `LAWS.md:12` (bare §, O-11).
- Wordings taken from the Anthropic seat: one, T12 [F-16].

**Self-assignments:**
- Grok: 0 folded as MEASURED. Design and checker kept RULED (L67, row 13). 2 re-test rows (R-01, R-02).
- Gemini: 0 folded as MEASURED (a spot check, n = 1, recorded). Kept RULED ("A" + L67, row 14). 1 re-test row (R-03, UNMARKED).
- The Anthropic seat: 4 re-test rows (R-04 to R-07).
- The proposal's own Anthropic rows (1–8, plus 8a): 7 RULED, 1 MEASURED (row 3, n = 3), 1 UNMEASURED (row 2 → R-08).

**Round 2:** none. No DO NOT ADOPT, no REJECT, no REJECT-with-HOLDS against an ADOPT.

**Owner items (O-1 to O-18):**
- O-1 D1: production write-path floor.
- O-2 D2: L27 routing sentence.
- O-3 D3: local seat as hub.
- O-4: write-path scope, dev included.
- O-5: class-level n.
- O-6: PASS bar, HOLD vs FIX.
- O-7: who runs T6, and the match rate.
- O-8: trigger (c) baseline.
- O-9: L25 "not load-bearing" vs L67.
- O-10: L31's reach.
- O-11: L26 wording (bare §).
- O-12: the seat table's interim source.
- O-13: writer profile, L29 or L33.
- O-14: L67 ids (RE-OPENS R46).
- O-15: "blind code seat".
- O-16: T12 owners.
- O-17: T5 citation rule.
- O-18: L23 wording.

**First trials under v2** (each is its own lane; none holds a build; none promotes a row without his one message):
- X1: Sonnet shadow, a build lane plus L67's three checkers.
- X2: Terra shadow, when its meter is read.
- X3: Haiku hub, planted mismatch.
- X4: local checker beside a cloud checker.
- X5: retrospective (T6); who runs it is O-7.
- X9: write-path launch-shape scratch test, owed ops.
- X10: `claude-opus-5-5` shadow.
- X6–X8: T12 ops.

## Preconditions (23:09 ET)

| Check | Result |
|---|---|
| placeholder count in `65` | 0 |
| `DERIVE ROW:` lines | 1 (R109) |
| R109 row | `cto-2026-09-22.md:55` carries `ROUTING-PROPOSAL-2026-09-22.md` + `derive seat: claude-opus-5-5`, with his words "Make all Opus 5.5 for now". `cto-2026-09-23.md` is absent (recorded, not fatal) |
| R109 committed | `75b2aa5790368bdd52e5802b64780567960163ed` |
| later row changing this derive seat | none. The other `derive seat:` rows are R33 (stale-score), R108 (voice), R73 (DRC), R36 (S3 exits) |
| seat match | row, `--model` and this session: `claude-opus-5-5` ×3 |
| hub stop line | `ROUTING TRIBUNAL R1 DONE · grok: TRIBUNAL R1: … · gemini: TRIBUNAL R1: … · astra: METER — proceed on three · houses that ruled: 2 of 3 …`; committed `485c20c0d84b7480cb5adea6acf4122e000e9ba8` |
| Anthropic seat stop line | `ROUTING TRIBUNAL FABLE R1 DONE …`; committed `6f85a88f06aa1f0bd909f913dbbb3e3695217204` |
| Astra | `METER — proceed on three`: recorded, not a refusal |
| launch-line strings (7 allow + 3 deny) in `22-draft-setups-tribunal.md` | each count = 1 |

## Fold table

`F-nn · item · seats that ruled it (n of 4) · whose wording · verbatim? · SELF · why`

| F | item | seats ruled (of 4) | whose wording | verbatim? | SELF | why (≤25 words) |
|---|---|---|---|---|---|---|
| F-01 | T1 split | 3: Grok, Gemini, Anthropic seat | Grok | yes | no | Keeps L25's fallback / reason-class duty on seats; the proposal filed L25 under ENGINE. Changes frozen scope least. Hub `## Rulings table` T1 |
| F-02 | T2 L5 | 3 | proposal kept | yes | no | All three ADOPT. Hub T2: "Both take §1.1 verbatim" |
| F-03 | T3 L24 | 3 | Grok | yes | no | Restores the dropped rung-2 shapes (hub WRONG FACTS, Gemini row HOLDS). The Anthropic seat's wording drops them, so it is not taken |
| F-04 | T4 table form / home | 3 | Grok | yes | no | A house's wording is preferred over the Anthropic seat's; "no seat file exists" HOLDS. Source stated `pending <T4 build>`. Anthropic seat T4 → O-12 |
| F-05 | T5 / (e) key | 3 | proposal kept | yes | Grok T5: yes | Gemini ADOPT; changes nothing frozen. Grok T5: SELF UNMEASURED — re-test row R-01. Citation rule → O-17. Binds after X5 |
| F-06 | T6 retrospective | 3 | proposal kept + Grok X5 | yes | no | All require T6 before the key binds (hub Experiments row). Who runs it and the match rate → O-7 |
| F-07 | T7 / (b) / (d) L29 | 3 | Grok | yes | no | Keeps the floor operative until D1 (hub ESCALATE: Grok and the Anthropic seat found the OR risk). Restores dropped clauses (hub WRONG FACTS rows HOLD) |
| F-08 | T8 / (f) re-test | 3 | Grok | yes | yes: DOES NOT HOLD as measurement | Restores the "local models improve" trigger. Self element = L67's RULED checkers, no new seat; recorded re-test row R-02. PASS metric → O-6 |
| F-09 | T9 L23 | 3 | proposal kept | yes | no | Gemini and the Anthropic seat adopt the proposal's sentence; it changes the least frozen text. Grok's paragraph → O-18 (L39: the change-least wording is carried) |
| F-10 | T9 L25 pointer (proposer ESCALATE 1) | 3 | proposal kept (= Grok's phrase) | yes | no | Hub `Checked` row "ESCALATE 1 … HOLDS": ADR-0008 has no bake-off table |
| F-11 | T9 L25 first hop | 3 | not taken | not taken | no | Its only ground is L31; hub `Checked` row "L31 forbids … law text" HOLDS against the proposal. → O-10 |
| F-12 | T9 L22 phrase | 3 | not taken (unchanged) | not taken | no | Same L31 ground, which does not hold. The Anthropic seat also says unchanged. → O-10 |
| F-13 | (b) L26 text | 2: Grok (b), Anthropic seat (b) | proposal kept | yes | no | Grok accepts it, and F-08 restores the trigger. Bare §4 / §5 are refused by the fold, per LAWS.md:12 as read by the derive. Anthropic seat wording → O-11 |
| F-14 | T10 L49 marker | 3 | proposal kept | yes | no | All ADOPT. The token figure is corrected by FC2 (not the verdict lines) |
| F-15 | T11 trials | 3 | Grok | yes | no | A house's wording; converged with the Anthropic seat X5 on the planted-STOP bar (hub Experiments). Anthropic T11: SELF UNMEASURED — re-test row R-05 |
| F-16 | T12 gaps | 3 | Anthropic seat (additions) + proposal kept | yes | no | No house wording competes. (1) FC4 HOLDS; (2) UNCHECKED by a hub — read by the derive at `report.py:127`; (3)–(5) match Grok / the proposal |
| F-17 | (a) seat map | 3 | hub file-check + seats (facts) | no | row-level | Row 4 DOES NOT HOLD; row 3 "no write path" DOES NOT HOLD for 09-22; row 13 id; row 7 → R109; row 8a is the Anthropic seat's MISSED line |
| F-18 | (g) table vs L67 | 3 | Grok | yes | yes: RULED L67 | A precedence rule; assigns no seat. RE-OPENS A RULING (R46) for L67 ids → O-14. Re-test rows R-02, R-03, R-06 |
| F-19 | (h) meter exhaustion | 3 | not taken | not taken | Anthropic seat: yes | The fallback text belongs to D2 (his). Grok's (h) is carried with D2; Anthropic (h): SELF UNMEASURED — re-test row R-07 |
| F-20 | (c) local seat | 3 | proposal kept | yes | no | All KEPT: L49 doctrine, L25 floor, exception handler |
| F-21 | WRONG FACTS | 3 | hub file-check | no | no | 16 claims, all HOLD. Corrected in v2's seat table and trace (port-probe count, day-open citation, five deploys, LEDGER:1326, L33) |
| F-22 | D1 | 3 (none ruled it) | OPEN (proposal §7 kept) | not taken | no | RULES AN OWNER ITEM (D1): Gemini's T7 writes D1-A into the text; not folded |
| F-23 | D2 | 3 (none ruled it) | OPEN (proposal §7 kept) | not taken | no | His (R4). Grok: A conflicts with L47. The Anthropic seat: A adds "none idle". ASTRA PENDING |
| F-24 | D3 | 3 (none ruled it) | OPEN (proposal §7 kept) | not taken | no | His. The Anthropic seat: "what the hub seat requires" is missing (`PROJECT-LEDGER.md:1326`) |
| F-25 | L21; L27 ceiling | 3 | proposal kept | yes | no | No divergence found. The L27 ceiling is NOT OPEN, by rule |

Counts:
- folds: 25
- verbatim `yes`: 17
- `no` (fact corrections): 2
- `not taken`: 6

## NEEDS ROUND 2

EMPTY. No house said `DO NOT ADOPT`; the hub's rulings table shows no REJECT. The Anthropic seat recorded `reject: 0`. No two seats disagree on whether a clause is CORRECT in the REJECT-against-ADOPT sense. Every divergence is a difference in wording, carried as the change-least wording plus an A/B, or it is an owner item. **The tribunal closes. v2 goes to him after Astra's read (R13).**

## OWNER ITEMS (after the tribunal)

Deduplicated. The proposal's D1–D3 come first. None is decided here.

- **O-1 D1:** the production write-path floor. Raised by the proposal §7 ("Recommend A" is the Anthropic house's line).
  - Gemini recommends A (`gemini-ruling.md:101`).
  - Grok declines to rule it.
  - The Anthropic seat says D1 is MIS-FRAMED, and that its premise is a Sync race, not a model tier (`PROJECT-LEDGER.md:621-624`, hub HOLDS).
- **O-2 D2:** L27's routing sentence. Raised by the proposal §7.
  - Grok: A conflicts with L47.
  - The Anthropic seat: A adds "none idle".
  - Gemini recommends A (`:102`).
  - ASTRA PENDING.
- **O-3 D3:** the local seat as hub. Raised by the proposal §7.
  - The Anthropic seat: the "missing half" is what the seat requires and what the fallback is.
  - Grok: T10's trial is not the hub trial.
  - Gemini recommends A (`:103`).
- **O-4:** write-path scope for all three L29 conditions, dev migrations included. Raised by the Anthropic seat (audit C5). Live case: deploy `05`, confirmed by the hub. Builds `27` and `31` are unverified by the hub.
- **O-5:** the class-level n. Raised by all seats. value proposed by Gemini — `gemini-ruling.md:88`.
- **O-6:** PASS bar — HOLD count vs FIX rows (L75), and any severity threshold. Raised by Grok and the Anthropic seat.
- **O-7:** T6 — who runs it (a house other than the proposer; blind two-pass) and the match rate that means "predicts". Raised by the Anthropic seat; Grok says the owner is a hub.
- **O-8:** trigger (c)'s baseline. Raised by the Anthropic seat.
- **O-9:** L25 "Phase 1: cross-house seats NOT load-bearing" vs L67. Raised by Grok.
- **O-10:** L31's reach over law text. It decides the L22 phrase, L25's first hop, L26's "(L31)" and L22's chassis names. Raised by the Anthropic seat ESCALATE 1 and Grok (b); the hub check HOLDS.
- **O-11:** L26 wording — the proposal's (bare §, refused by the fold) vs the Anthropic seat's. Raised by the derive, from the Anthropic seat's (b).
- **O-12:** the seat table's interim source until `seats.yaml` loads. Raised by the Anthropic seat T4.
- **O-13:** the OpenAI writer profile — in L29 (v2) or L33. Raised by the Anthropic seat. ASTRA PENDING.
- **O-14:** RE-OPENS A RULING (R46), the model ids in L67 [amended 2026-09-21]. Raised by the Anthropic seat and Grok (g).
- **O-15:** does a "blind code seat" exist? Raised by Grok.
- **O-16:** owners of the T12 ops items. Raised by Grok; the hub check HOLDS: no owner is named.
- **O-17:** T5 — S by a pre-build citation rule. Raised by Grok (SELF) and the Anthropic seat.
- **O-18:** L23 wording — the proposal's or Grok's. Raised by Grok.

## FOR DEJAN

No recommendation: the Anthropic house proposed this design, ruled round 1, and derived v2 (L37). A = what v2 carries; B = the alternative a seat named.

1. **D1: production write paths.** When a build or deploy touches the live vault, the production DB, or an `--allow-prod` migration, does it always run on the house's top model?
   - A: yes, until you rule otherwise; no trial earns it down (v2's L29, Grok's wording).
   - B: a lower model that passed a dev shadow build may run it (the proposal's D1-B).
   - The proposal's own D1-A (production always top, dev earnable) is Gemini's wording.
2. **Write-path scope.** A deploy hub on Sonnet ran a `cobalt_dev` migration in auto mode on 09-22.
   - A: that is a write path, so today's launch shape is outside the law (v2 as written).
   - B: dev-only migrations and with-DB suites are scoped differently (the Anthropic seat, audit C5).
3. **D2: a spent meter.** When Codex runs out mid-week, what does the law say about that house?
   - A: every house's allowance is planned in the seat table, and a bound meter moves the seat to its row's fallback (the proposal).
   - B: keep "Codex is the overflow valve … most of it on Astra".
   - Grok's per-build alternative text for A is in v2 `## Dissents`. ASTRA PENDING.
4. **D3: the local model as Cobalt's hub.**
   - A: keep it as the plan, gated on a measured hub trial.
   - B: retire it; local stays on the morning check only (the proposal).
5. **n for a PASS.** How many shadow builds make a model "pass" a class?
   - A: unset — every trial reads "spot check, n = 1".
   - B: you set a number. Gemini offered 3 as a pointer.
6. **What counts against a candidate in a shadow build.**
   - A: the checkers' HOLD count (Grok).
   - B: FIX rows only, because some HOLDs confirm the build is right (the Anthropic seat; true of rows 5, 6 and 25 in the 09-20 chunk 1a check).
7. **Who grades the S/H key against past builds.**
   - A: "a hub job" (the proposal).
   - B: a house other than the proposer, classing blind from prompts first (the Anthropic seat).
8. **Trigger (c) baseline.**
   - A: unset.
   - B: you set the defect baseline per seat.
9. **Cross-house seats.**
   - A: L25's "cross-house seats NOT load-bearing" stays as written beside L67 (v2).
   - B: it is retired, since L67 made Grok, Gemini and OpenAI seats standing (raised by Grok).
10. **Vendor names in law text.**
    - A: L22 and L25 keep "Max", "Anthropic API" and "Claude →" (v2; L31 lists no law text).
    - B: substitute house-neutral words (the proposal; Grok and Gemini adopted it).
11. **L26 wording.**
    - A: the proposal's, which the desk cannot fold as written because of its bare §4 / §5.
    - B: the Anthropic seat's, which inlines the triggers and uses FIX rows (tied to item 6).
12. **Before `seats.yaml` exists, where does a launch read its seat?**
    - A: "source pending" (v2).
    - B: the desk-report §4 ruling cited in the launch prompt (the Anthropic seat).
13. **OpenAI writer profile** (workspace-write, network on, cannot commit).
    - A: it stays in L29 (v2).
    - B: it moves into L33 (the Anthropic seat named this option). ASTRA PENDING.
14. **L67's model ids** ("Sol", "Opus 5") — RE-OPENS R46.
    - A: L67 is untouched and the table records the ids.
    - B: you re-rule L67 without ids.
15. **"Blind code seat" for Grok.**
    - A: not in the table (v2).
    - B: you seat it by ruling.
16. **T12 ops owners.**
    - A: none named (v2).
    - B: you name them.
17. **What is class S** (the lower-tier-eligible work)?
    - A: the proposal's §4 description.
    - B: the prompt names an existing artifact and a test a wrong guess fails (Grok, the Anthropic seat).
18. **L23 wording.**
    - A: one sentence changes: "first candidate ASSESSED" (v2).
    - B: Grok's paragraph, which also says "local trumps cloud" is a reason, not a route.

## ASTRA READ OWED

On Sat 09-26, before his ruling, the OpenAI house reads:
- v2's header (ASTRA PENDING).
- Seat-table rows 9, 10 and 11, and "not seated" row 12 (Terra).
- The trace rows that move L29 [amended 09-10]'s OpenAI roles and writer profile.
- O-13.
- X2 (Terra shadow).
- R-02, R-06 and R-07: they touch the checker set that includes Sol, and the Opus stand-in for Sol / Astra.
- O-14 (L67's `gpt-5.6-sol` id).
- **D2 / O-2**: L27's routing sentence, which names that house's role.
- O-7, if the non-proposer T6 seat falls to that house.

## Redactions

0. The packet and the rulings carry no user data (hub redaction check: 0). v2 and this report quote no ticker, price, share count or rule value of his.

## READING

- `prompts/2026-09-22/65-routing-tribunal-derive.md` (whole)
- `LAWS.md` :1-442 (full)
- hub `reports/routing-tribunal-2026-09-22.md` :1-303
- `scratch/tribunal-bars-0920/routing-tribunal/r1/grok-ruling.md` :1-357; `gemini-ruling.md` :1-114
- `reports/routing-tribunal-fable-r1-2026-09-22.md` :1-263
- `30 - Design/ROUTING-PROPOSAL-2026-09-22.md` :1-246; `reports/routing-propose-2026-09-22.md` :1-41
- `cto-2026-09-22.md` R4 :15, R109 :55, R81 :84, R76 :89, R36 :129, R32 :130, R13 :149; R33, R108, R73 via the `derive seat:` grep. R46 and R49 are taken from the hub's AUTHORIZATION row and L67's text, not re-read.
- `LAWS-HISTORY.md` :27-72
- Opened where a fold turns on it:
  - `areas/cobalt-houses.md` :50-69
  - `src/cobalt/seatusage/report.py` grep "L29" (:127)
  - `bars-chunk-1a-check-2026-09-20.md` :172-204
- Launch-string greps in `prompts/2026-09-21/22-draft-setups-tribunal.md` (10 strings)
- `ls` of the r1 folder and of both output paths

## ESCALATE

1. **ASTRA:** the OpenAI house has not ruled on a routing design that assigns its own seats (seat-table rows 9–12) — R13, meter out until Sat 09-26 06:47 ET. The desk brings Astra's read of v2 to him BEFORE his ruling of the law text.
2. **RULES AN OWNER ITEM (D1):** Gemini's T7 wording writes D1-A ("OR (for dev write paths only) …") into L29's text (`gemini-ruling.md:32`). Not folded; carried in v2 `## Dissents`.
3. Gemini's `OWNER` section recommends A on D1, D2 and D3 (`gemini-ruling.md:101-103`). These are recommendations, not rulings: recorded, not folded. The hub counted RULES AN OWNER ITEM: none.
4. **RE-OPENS A RULING (R46):** the model ids inside L67 [amended 2026-09-21] ("Sol (`gpt-5.6-sol`)", "Opus 5") → O-14. Not folded.
5. **Self-assignment wordings folded as procedure, not as seats**, named for his eye:
   - Grok's T8 (SELF; its hub row says DOES NOT HOLD as measurement) is v2's re-test procedure.
   - Grok's (g) (SELF, RULED L67) is v2's table-vs-L67 rule.
   - Neither adds a seat. Their self elements are re-test rows R-02 and R-03.
   - No seat presses an UNMEASURED self-assignment as law.
6. **A ground that DOES NOT HOLD, still in folded text:**
   - The proposal's L26 closes "Model ids live in the table, never in law text (L31)". L31's text does not cover law text (hub check) → O-10 / O-11.
   - Grok's L24 removes "(Grok Bot etc.)" as "a vendor example" binding no duty; that removal is folded.
7. **Clauses the trace finds dropped or changed (named, not silent):**
   - L24 "rare" is absent from Grok's folded T3, though Grok's (b) says it is kept.
   - L23 "cheapest sufficient step up" is dropped.
   - L5 "were ruled accordingly" (provenance) is dropped.
   - L29 "Claude included" is dropped.
   - L26 "slice reviews" is not named.
   - L29's Sonnet/Haiku clause gains an exception ("unless a seat-table row cites his ruling or a measured trial").
   - L29's gate gains "outside the session's workspace".
8. **L31 against folded wordings:**
   - v2's L29 (Grok) names "Sonnet/Haiku" and "the OpenAI writer".
   - v2 keeps the vendor names already in L22, L23 ("Gemini outage"), L25 ("Claude →") and L27.
   - The hub check found L31 does not list law text. The derive prompt's index card reads it as covering law text. See item 13.
9. **Form defect:** the proposal's L26 carries bare "(§4)" and "§5", and LAWS.md:12 says the fold refuses a bare §-reference. The desk cannot fold O-11 A as written; his A/B, or a later wording, must settle it.
10. **L29.6 against today's launches** (the Anthropic seat ESCALATE 2): `05-stacked-deploy` (Sonnet 5, `--permission-mode auto`) ran `COBALT_ENV=dev uv run cobalt db migrate` (hub check HOLDS). Builds `27` and `31` are the same shape per the Anthropic seat, UNVERIFIED by the hub. This is a live law-vs-practice gap, independent of the fold; not a defect claim (L70) → O-4.
11. Gemini's X1 names a shadow build on a write-path deploy (`68-devdb-repair.md`). v2's L29 ("A trial does not earn a write path down") bars that as an earn-down until D1. It is carried in X1's row as a note, not as a trial.
12. Hub record discrepancies, for the desk's record:
    - The hub's rulings table shows Gemini T6 as "ADOPT WITH"; the raw file (`gemini-ruling.md:26-27`) says "ADOPT".
    - The hub attributes the Grok model-pin experiment to Grok; Grok's raw file has no such X (it is the Anthropic seat's X2).
    - The hub's self-assignment count line says "3" for the Anthropic seat while listing 4 rows.
13. `ASK DESK: L31's reach. The derive prompt's index card reads L31 as "no vendor or model name in law text"; LAWS.md:181 lists code identifiers, schema, config keys, enum values and system design docs, and the hub's check HOLDS that it does not reach law text. Safe default applied: a wording whose ONLY ground is L31 was not folded (F-11, F-12); v2's new sentences carry no model id except where a folded house wording already did (item 8). [23:19 ET]`
14. **One Anthropic-seat wording was folded:** T12's additions [F-16], where no house wording competes. Two claims in it were UNCHECKED by the hub and read by the derive (`report.py:127`; `seat-usage.md` keys via FC4). One seat-table row (8a, RULED R46) comes from the Anthropic seat's (a) MISSED line. Both are named, because this house holds a side.

## CONTINUE

next: none — run complete. v2 at `docs/30 - Design/ROUTING-v2-2026-09-22.md`; nothing committed (no git write in this seat).

ROUTING DERIVED v2 · folds: 25 · verbatim: 17 · needs round 2: 0 · owner items: 18 · ESCALATE: 14
