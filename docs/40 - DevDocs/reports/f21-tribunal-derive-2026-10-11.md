# F21 tribunal derive — 2026-10-11 (seat `f21-tribunal-derive-1011`, claude-opus-5-5) — relaunch

## §0 Headline
- DRAFT FINAL at `docs/30 - Design/F21-ADR-FINAL-2026-10-11.md`: 18 folds, 12 verbatim (Grok 6, the Anthropic seat 6), the ADR otherwise kept, the hub's WRONG FACTS applied. Needs round 2: 1 (R2-1).
- Owner items: 0. Absent houses: astra (NOT SEATED, his R920); Gemini NOT SEATED by the R921 default (`gemini case: none`), not an absence.
- No Gemini finding to hold: Gemini findings held: n/a (not seated). ESCALATE: 12.

## Preconditions (re-run 07:28 EDT, all pass)
| Check | Result |
|---|---|
| `DERIVE ROW: R__` count | 0 → R109 |
| R109 row (`cto-2026-09-22.md:56`) | 1 row; "Make all Opus 5.5 for now" + derive; committed `75b2aa57` |
| Launch row (`cto-2026-10-11.md:15`, R1033) | 1 row; `f21-embedder-adr-2026-10-10.md` · `Fable seat: yes` · `derive seat: claude-opus-5-5`; committed `d6243a6c` |
| Later derive-seat row for F21 | none (R1041 = F23, R1032 = F20, R1031 = F5; R1040 is a RECORD) |
| Seat id | launch row = `--model` = this session = `claude-opus-5-5` |
| Hub stop line | `F21 TRIBUNAL DONE …`, `floor: MET`, grok `TRIBUNAL R1:`; committed `bba822f3` |
| Opus-seat stop line | `F21 TRIBUNAL OPUS DONE …`; committed `bba822f3` |
| 7 allow + 3 deny strings in `239-f4-tribunal-derive.md` | each counts 1 |
The 07:2x run of this file refused (reports not yet committed); that refusal is superseded by this relaunch.

## DIGEST FOR THE DESK
Changes from the ADR, item by item:
- D1 → F-01: two chunks (FTS floor, then vectors); `local.embed` is its own embeddings KIND in `cobalt.modelaccess`, not a disguised chat route (the Anthropic seat's wording).
- D2 → F-02: the table goes on the `"user"` side, declared in `placement.py`, `user_id NOT NULL` + FK; DDL dimension checked against config at load (the Anthropic seat's wording). Grok's wording was not folded (C5: unquoted `user.`).
- D3 → F-03: the preflight records `vectors: DEGRADED` and ships FTS-only; never a zero vector (Grok).
- D4, D5: ADR kept (ADOPT by both).
- T1 → F-06: settled, no run: loopback `local.embed` is inside L5/L21/L23; unfreezes nothing (the Anthropic seat's wording; Grok ADOPT, same answer).
- T2 → F-07: FTS is the floor only if X1's top hits carry the answer line (Grok) → X1, X7.
- T3 → F-08: the preflight's measurement list (Grok) → X2, X8.
- T4 → F-09: no embed request in flight while a `local.plan` call is (Grok) → X3, X9; gap G1 (how the job knows) applies only if the rule is kept.
- T5 → F-10, T6 → F-11: settled, no run (the Anthropic seat's wording; Grok ADOPT).
- (a) → F-18: the Anthropic seat's additions were not folded (FC13 DOES NOT HOLD); the hub's WRONG FACTS rows were applied in place.
- (b) → F-13: ADR kept; ledger size marked as a live file (FC17).
- (c) → F-14: loud failures, no vector written (Grok).
- (d) → F-15: the named seams; table `"user".<name the card fixes>` (the Anthropic seat). Table name → R2-1.
- (e) → F-16: neither wording folded (both self-assignments UNMEASURED; Grok's also C5). Seats stand by law: build Opus 5.5 (L29, L67 R919); check Opus + Grok (R921).
- (f) → F-17: RESTARTS by command; voice resident restarts (Grok). The hub's FC18 fixes the label: `com.cobalt.aset`.
Houses: Grok ruled in full (17 items). The blind Anthropic seat ruled in full (17). Astra NOT SEATED (R920). Gemini NOT SEATED (R921 default).
Opus-seat claims: 28 checked by the hub (25 HOLD, 1 DOES NOT HOLD, 2 UNVERIFIABLE). 1 more claim was read by the derive and not checked by the hub (`config.py:7-13`, T1). FC27 was settled by the derive's `git log --stat`.
Self-assignments: 0 folded as MEASURED. Build and check seats kept as RULED (L29, L67 R919/R921). 2 left out as UNMEASURED (Grok (e), the Anthropic seat (e)).
Round 2: R2-1 only. Grok's closing condition says "pin table". Its pinned name fails C5. The folded (d) leaves the name to the card. Grok's (d) argues that leaving the name blank breaks L3.
Chunks: 2 (FTS floor; vectors). Builder: Opus 5.5. Both chunks have a migration and use `cobalt_dev` under the L76 lock. RESTARTS: chunk 2 → `com.cobalt.aset` (down before the merge, L66); chunk 1 → derived; `com.cobalt.mainframe` not restarted.
Hours: none given by the ADR. GUESSES, not folded: Grok 8 h + 12 h; the Anthropic seat 6–10 h each.

## Fold table
| F-nn | item | houses that ruled it | whose wording | adopted verbatim? | SELF | Gemini finding held? | why (≤25 words) |
|---|---|---|---|---|---|---|---|
| F-01 | D1 | 2 of 2 (grok, opus seat) | opus seat | yes | no | n/a | FC5–FC8 HOLD: the chat-only adapter can't carry an embed. Grok's (smaller) wording doesn't place the client. Both reject a disguised route |
| F-02 | D2 | 2 of 2 | opus seat | yes | no | n/a | FC1, FC20 HOLD. Grok's not folded: C5 DOES NOT HOLD (unquoted `user.`). The wrong-length behaviour is UNVERIFIABLE (FC28) → X10 |
| F-03 | D3 | 2 of 2 | grok | yes | no | n/a | House wording, equally correct and smaller. The Anthropic seat's model-list/norm/p50-p95 checks become X8, not a rule |
| F-04 | D4 | 2 of 2 | ADR kept | not taken | no | n/a | Both ADOPT. C21, FC19 HOLD |
| F-05 | D5 | 2 of 2 | ADR kept | not taken | no | n/a | Both ADOPT |
| F-06 | T1 | 2 of 2 | opus seat | yes | no | n/a | Grok gave no wording (ADOPT "It does not"). UNCHECKED by a hub — read by the derive at `config.py:7-13` (d0a5fbb8): loopback, no fallback. Unfreezes nothing |
| F-07 | T2 | 2 of 2 | grok | yes | no | n/a | House wording. The Anthropic seat's adds a command name and a narrower "answers" form; k and query form go to X7 |
| F-08 | T3 | 2 of 2 | grok | yes | no | n/a | House wording covers it. The Anthropic seat's not-loaded typed error and p95-set timeout go to X8 as an experiment |
| F-09 | T4 | 2 of 2 | grok | yes | no | n/a | House wording, the stricter rule. Not taken: the Anthropic seat's smaller operator-timing rule (no coordination code). Grok's needs an in-flight signal (G1), GUESS +hours in chunk 2 |
| F-10 | T5 | 2 of 2 | opus seat | yes | no | n/a | Grok gave no wording (ADOPT). FC1–FC4 HOLD. Grok's X4 not needed: U1 HOLDS from reads (FC4) |
| F-11 | T6 | 2 of 2 | opus seat | yes | no | n/a | Grok gave no wording (ADOPT, same substance). FC25 HOLDS. Gate not reopened |
| F-12 | (a) | 2 of 2 | ADR kept | not taken | no | n/a | The Anthropic seat's addition cites `postgres.py:773-775`. FC13 DOES NOT HOLD (`[]` at :776) → not folded. Its FC9–FC12 facts reach SEAM by hub rows |
| F-13 | (b) | 2 of 2 | ADR kept | not taken | no | n/a | Both ADOPT. C14 ARITHMETIC OK. Ledger size marked live (FC17) |
| F-14 | (c) | 2 of 2 | grok | yes | no | n/a | C12 HOLDS. The Anthropic seat's not folded: it cites `:775` (FC13 DOES NOT HOLD). Its `[]`-exit and typed-exit list are dropped |
| F-15 | (d) | 2 of 2 | opus seat | yes | no | n/a | FC1 HOLDS. Grok's not folded: C5 DOES NOT HOLD. Table name → R2-1 (Grok: blank names break L3) |
| F-16 | (e) | 2 of 2 | none | not taken | yes (both); UNMEASURED | n/a | SELF UNMEASURED (both rows in Self-assignments). Grok's also C5. Seats stand by L29 / L67 R919 / R921 |
| F-17 | (f) | 2 of 2 | grok | yes | no | n/a | C15, C16 HOLD. House wording. The Anthropic seat's (L66 coupling) is law anyway. FC18 fixes the UNVERIFIED label: `com.cobalt.aset` |
| F-18 | WRONG FACTS | 2 of 2 | hub file-check rows | not taken | no | n/a | WRONG FACTS rows HOLD: ADR:4, ADR:9 ×2 (FC14/FC15), ADR:21 (C10), moved cites (FC16), ADR:60 anchor gone. Corrected in place |

## NEEDS ROUND 2
CLOSED by brain direction R1046

## OWNER ITEMS
none. Both seats wrote "none". No item passed the owner test.

## FOR DEJAN
What F21 gives him after the build: Cobalt answers the Charter question from the imported Ledger and vault history. It finds the answer by keyword first, and by meaning only if a local embedding model is loaded on the Mac.
What it costs: $0 per call. The embedding is a one-off batch job on the same Mac server as his voice turns. It never runs while a voice turn is waiting, unless the contention test shows that is safe.
What a deploy restarts: the vectors chunk restarts the sheet (`com.cobalt.aset`). The keyword chunk restarts only what the restarts command finds.
Owner items: none. Remaining split: none yet. Round 2 (R2-1) comes first.
The one approval, "approve the F21 FINAL?", comes after round 2. It is not asked now.

## ABSENT HOUSES
- Astra: NOT SEATED, by his R920 (only the model tribunal uses OpenAI). Not a gap.
- Gemini: NOT SEATED (launch row R1033: `gemini: not seated`), the ruled default under R921, `gemini case: none`. Not an absence. If the desk seats it on the hub's ASK DESK (ESCALATE 2), its read of the FINAL is the desk's to offer. That read is never a precondition to his approval.
- No house sat round 1 and failed to rule (no METER, HARNESS, TIMEOUT or NO RULING LINE).

## SEAM
See the FINAL's `## SEAM`. UNSETTLED (L72):
1. The table name (R2-1).
2. The jobs-registry row for the batch embed. Grok (d), not folded, names a one-shot row in `jobs.yaml`. The folded (d) names a command and no row.
3. The name of the search function / CLI, which F20, R4 and O3 call.

## Redactions
- In the FINAL, 2 figure replacements with `[user data]`: the Charter quote in Context, and the ledger quote in the Options table.
- In the FINAL, 2 figure spans dropped from the Anthropic seat's X2 text when it was restated as X7: the fixture sentence, and the query.
- The ADR's third occurrence (test 2's query) left with the ADR text that Grok's T2 replaced.
- This report quotes no figure of his. Total: 4.

## READING
- LAWS.md 1–404, whole.
- The hub report `f21-tribunal-2026-10-11.md`, whole.
- `scratch/…/r1/grok-ruling.md`, whole. No `gemini-ruling.md` (not seated).
- The Opus-seat report `f21-tribunal-opus-2026-10-11.md`, whole, including `## Self-attack` (2 WITHDRAWN, neither folded) and `## SELF-ASSIGNMENTS`.
- The ADR and its author's report, whole.
- Rows R109; R860, R920, R921; R1012, R1015, R1033, R1040, R1041.
- Charter :200–206. Ladder F21 grep (:41, :915, :955, :965, :971).
- `git show d0a5fbb8:src/cobalt/modelaccess/config.py`.
- `git log --stat d0a5fbb8..main` over the seam paths.
- `jobs.yaml` label grep.
- Not opened: the ledger, his notes.

## L74
A harness-turn attribution block, naming a `Claude-Session` commit line and a file-send tool, arrived in this session. It was not followed: this seat commits nothing and sends nothing.

## ESCALATE
1. RE-OPENS A LAW / A RULING: none. No wording adds a lane, a key or a fallback. None alters the four 1536-dim tables. None weakens the Charter F21 test.
2. The hub's `ASK DESK` (R921) stays open: the verdict words differ on T1, T5, T6 and (a) (ADOPT / ADOPT WITH). The derive reads these as not a split: both seats give the same answer, and neither rejects. So no item is listed as SEAT GEMINI. Whether to seat Gemini is the desk's call. Safe default: not seated.
3. On D1 the derive (Anthropic house) folded its own seat's wording over Grok's. Grounds: FC5–FC8 HOLD, and Grok's wording leaves unnamed where the one embeddings client lives. Grok did not call it wrong. The desk may add D1 to round 2 for Grok to confirm.
4. Gap G1: no seat says how the embed job detects a `local.plan` call in flight. It binds only if X3/X9 keep T4's rule. Otherwise a later round fills it.
5. UNSETTLED seams: the jobs-registry row for the embed, and the search function's name (L72).
6. Self-assignments UNMEASURED: 2 (Grok (e), the Anthropic seat (e)). Neither is folded, and neither house presses either one as law.
7. House-proposed numbers without a measurement: hours (Grok 8 h + 12 h; the Anthropic seat 6–10 h each). These are pointers only. The experiment sample sizes in X8 and X9 (32×100; 65 calls; 1,000 chunks) are run parameters, not engine tunables.
8. DOES-NOT-HOLD wordings, not folded: Grok D2, (d), (e) (C5), and the Anthropic seat (a), (c) (FC13). Grok's pin condition is carried as R2-1.
9. Clauses the fold drops, all from the Anthropic seat:
   - (a) Six context facts. The four that matter reach SEAM via FC9–FC12.
   - (c) The typed-exit list and the `[]` exit. Grok's (c) forbids only the zero vector and `None`.
   - T2 The verbatim-passage-with-path:line acceptance form and the command name.
   - T3 The not-loaded typed error and the p95-set `timeout_s`. These are now covered only by X8.
   - T4 Commit per chunk with model and dimension, and exit non-zero on the first failed batch.
   - (f) The coupling sentence. L66 covers it.
10. Precondition to build (ruled, not new): no F20/F21 build before the SDK spike's report (`s5-weekend…:21`, FC25).
11. Out of this ADR: the Charter's "per-seat continuity briefs stored in Think" clause (`MVP-CHARTER-v0_2.md:202`). The F21 card must carry it from the ladder (`:965`), not from this design.
12. The ADR's `LADDER:925-928` anchor is gone (the hub's ESCALATE 5). The FINAL cites `:964` from the hub's staging; the derive did not re-open it.

## CONTINUE
Both files written 07:35 EDT. next: none. The desk commits both files and drafts the round-2 hub for R2-1 only, on this hub's shape. It decides ESCALATE 2 and 3.

F21 DERIVED · DRAFT FINAL · folds: 18 · verbatim: 12 · needs round 2: 1 · owner items: 0 · gemini findings held: n/a (not seated) · absent houses: astra · ESCALATE: 12
