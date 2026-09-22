# S3 exits tribunal — derive v2 — 2026-09-22

Seat `s3-exits-tribunal-derive-0922` · model `claude-opus-5-5` (row R36, `cto-2026-09-22.md`:54, committed `67bc19ba`) · not the Fable seat (the Fable seat ruled round 1 on `claude-fable-5-1`); this seat held no side in round 1.

## §0 Headline
- v2 written: `docs/30 - Design/S3-EXITS-v2-2026-09-22.md` — the proposal whole, 41 fold rows tagged `[F-nn]` in place + 1 verdict row; 26 house wordings taken verbatim; no user data (5 spans redacted).
- Folded: one-transaction fill through `mark_filled` (grok), pct-only drift warning with missing P recording the fill (grok; AND gate dropped by all three), trade-note path column (grok), Fable's fact rows F34–F36 and corrections to F29/F30/F32/F33, Fable's F14 seam list.
- **Round 2 owed on 3 items**: gemini's DO NOT BUILD vs v2 (R2-1); the legs correction/running-share mechanism, incl. the live stop-edit defect's fix form (R2-2); which migration set carries M1 (R2-3). The tribunal does not close.
- Seats: grok, gemini, Fable in full; Astra METER under 09-22 R13 — reads v2 Sat 09-26. Owner items: 20 (O1–O8 first). ESCALATE: 8.

## Preconditions (verified 14:22 ET)

| Check | Result |
|---|---|
| DERIVE ROW unfilled? (`R__` count) | 0 → filled: R36 |
| R36 rows in `cto-2026-09-21.md` / `cto-2026-09-22.md` | 2 rows named R36; ONE carries `S3-EXITS-PROPOSAL-2026-09-21.md` (`cto-2026-09-22.md`:54) with `Fable seat: yes` and `derive seat: claude-opus-5-5`; the 09-21 R36 (`cto-2026-09-21.md`:47) is the stale-marker ruling and names no proposal |
| R36 committed | `67bc19ba43b94f01dff3be2ecc87f9944e9891aa` |
| Seat = row | row names `claude-opus-5-5`; this session runs `claude-opus-5-5` |
| Hub report | only `s3-exits-tribunal-2026-09-22.md` exists (`-09-21` absent); last line starts `S3 EXITS TRIBUNAL R1 DONE`; committed `9a4b01a7` |
| Fable R1 report | only `s3-exits-tribunal-fable-r1-2026-09-22.md` exists; last line starts `S3 EXITS TRIBUNAL FABLE R1 DONE`; committed `acf9a6a3` |
| Astra | `astra: METER — proceed on three` → RECORDED under 09-22 R13 (`cto-2026-09-22.md`:74), not a refusal; `01-QUESTIONS.md` names no Astra-only question |
| Launch line adds no rule | all 7 allow + 3 deny strings count 1 in `22-draft-setups-tribunal.md` |

## DIGEST FOR THE DESK

**What v2 changed from the proposal, item by item:**
- Q1 realized R on the ACTUAL unit `|fill − stop at fill|` (grok verbatim; all three). Planned-unit second output → O15.
- Q2 one `legs` table; `fills` stays declared (grok). Strike → O16.
- Q3 correction index / current row / running chain → **R2-2** (grok+gemini: partial unique index impossible; Fable offers one).
- Q4 fill columns kept as cache, written in the SAME transaction (grok). Cache after an entry-leg correction → R2-2.
- Q5/(i) fill never refused on a sheet mismatch; entry leg stores `day_mode_id`, `attested_sheet`, `sheet_mismatch` (grok). Comparison basis → O18.
- Q6, Q7, Q8, Q10, (k) — proposal kept (unanimous).
- Q9 note synchronous after commit; retry = `upsert_trade_note` + `upsert_unit` per leg (grok). Same-second collision → X16.
- Q11 ↺ = `kind=reset` to `structural_stop`; not rendered on a manual card (Fable); typed-equal stop stays `edit` (grok).
- Q12 REST poll; interval his, resident refuses to start without it (grok).
- (a) F34/F35/F36 added; F29/F30/F33 corrected (Fable verbatim); stale citations fixed; `create_state` writer → X9.
- (b) ONE fill path: `fill(conn=)`, `mark_filled` one transaction, `/move` stops filling, FILLED without price refused, CLI via `mark_filled` (grok). Orchestrator alternative → O17.
- (c) numbering: next free 0014/0015 only after 0012+0013 land (grok; desk lane). Migration SET → **R2-3**.
- (e) AND gate dropped; `distance_change_pct > P`; no ATR term; missing P records the fill + banner (grok). ATR display alternative → O3 B.
- (f) `cobalt_stop` per leg struck, gap computed at render (Fable). FILLED stop-edit share count fix → **R2-2** (form); live defect on main → ESCALATE 2.
- (g) panel first; kill phrase checked first; one listener (grok). O8 costs from grok + Fable + gemini's coupling, verbatim.
- (h) `trade_note_path` column; F14 reads it, never the nearest-timestamp search (grok). Body is a code copy — keep it (grok); X14.
- (j) #16 reading = one entry fill, many exit legs (Fable verbatim); his confirmation → O13.
- (l) C3 → C4 sequential; hours 30/42 h (38/53 with DM) (grok); order after bars 0012 + setups 0013 (grok).
- (m) Fable's seven F14/F15 seams, verbatim.
- (n) 17 experiments placed before their chunks; grok's test-plan changes folded.

**Seats that ruled round 1:** grok in full · gemini in full · Fable in full (approved, 09-21 R57) · Astra NOT (METER, 09-22 R13).
**Fable claims:** hub-checked 8 (7 HOLD, 1 UNVERIFIABLE — FC8 → X9). Fable wordings folded that the hub did not check: 7 rows, each read by this derive at the cited file (all borne out); counted under no "HOLDS" figure.
**Round 2 (3):** R2-1 gemini's DO NOT BUILD vs v2; R2-2 legs corrections / running shares / current row / cache / `direction` source / double-tap outcome; R2-3 migration set for `card_stop_edits.kind` and the `aset_sizings` columns. Why: a DO NOT BUILD (R2-1) and houses disagreeing on whether a mechanism is correct (R2-2, R2-3).
**Owner items (20):** O1 ⅓/½ rounding · O2 drift P + comparator · O3 ATR in the warning · O4 manual notes at sizing · O5 his blank keys · O6 `trade_def` on radar notes · O7 one tap from ARMED · O8 DM in S3 · O9 poll interval · O10 listener RED rule · O11 radar FILL UPDATE block · O12 dataview `strategy` column · O13 #16 reading · O14 preset set · O15 planned-unit R · O16 `fills` name · O17 build shape · O18 mismatch basis · O19 ↺ on manual · O20 Cobalt stop per leg.
**Chunks under v2:** C1 8 h → C2 6 h → C3 7 h → C4 5 h (after C3) · C5 8 h only if O8 = A (parallel after C2) · C6 4 h. Write paths 5 (4 if O8 = B), Opus 5 floor; Anthropic seats `claude-opus-5-5` while 09-22 R36 stands. RESTARTS: GUESS — `com.cobalt.aset` + `com.cobalt.radar` in the pause, C5 bootstraps `com.cobalt.dmlisten`; X12 measures.
**Hours (GUESS):** 42 h without the DM, 53 h with it (grok's re-derivation) + round 2 + unpriced S3-P3, against S3's 09-24 → 10-07 (10 trading days). Build cannot start before the FINAL, i.e. after round 2.

## Fold table

`F-nn · item · seats that ruled it · whose wording · adopted verbatim? · why`

| F | item | seats that ruled it | whose wording | verbatim? | why |
|---|---|---|---|---|---|
| F-01 | Q1 R_unit | 3 of 4 (grok, gemini, Fable) | grok | yes | actual unit unanimous; grok's single output is the smaller mechanism (Fable's `r_planned` → O15); `direction` clause tagged R2-2 |
| F-02 | Q2 `fills` | 3 of 4 | grok | yes | split on striking: keeping is no change, the smaller one; strike (gemini, Fable) → O16; not a correctness split |
| F-03 | Q3 index, current row, correction rule | 3 of 4 | none | not taken | → R2-2: grok, gemini say a partial unique index cannot work; Fable's `WHERE corrects IS NULL` says it can |
| F-04 | Q4 cache | 3 of 4 | grok | yes | Checked row 1 (two transactions) HOLDS; grok's "No other path writes them" vs Fable's correction rewrite → R2-2(e) |
| F-05 | Q5 + (i) attestation at fill | 3 of 4 | grok | yes | record+flag unanimous; grok's compares to today's day mode (existing check); Fable's sizing-sheet basis (UNCHECKED) → O18 |
| F-06 | Q6 "27 %" | 3 of 4 | proposal kept | n/a | all ADOPT; Fable derives both readings = 27 (X15) |
| F-07 | Q7 DM ambiguity | 3 of 4 | proposal kept | n/a | all ADOPT refuse-with-candidates |
| F-08 | Q8 note edit | 3 of 4 | proposal kept | n/a | all ADOPT override only, no reverse parse |
| F-09 | Q9 note timing, retry | 3 of 4 | grok | yes | retry must upsert units, not only `create_if_absent`; Fable's wording (collision clause, UNCHECKED `trade_note.py:154-169`) not taken → X16 |
| F-10 | Q10 TRIGGERED expiry | 3 of 4 | proposal kept | n/a | all ADOPT; caller unproven → X5 (L70) |
| F-11 | Q11 reset target, manual card | 3 of 4 | Fable | yes | UNCHECKED by a hub — read by the derive at `cards/store.py:980-996` (only `structural_stop` writer) and `aset/web.py:701`; grok's refuse-with-reason → O19 |
| F-12 | Q11 typed-equal stop stays `edit` | 3 of 4 | grok | yes | separate point; Fable (f) says the same in substance |
| F-13 | Q12 transport, interval | 3 of 4 | grok | yes | REST unanimous; Fable's key name not taken (name at build, value his, L53) |
| F-14 | (a) F34, F35, F36 rows | 3 of 4 | Fable | yes | F35: Checked rows F8/F16 HOLD; F36: FC1 HOLDS; F34: UNCHECKED by a hub — read by the derive at `aset/web.py:1006`, `:1103`, `:1336` |
| F-15 | (a) F29 corrected | 3 of 4 | Fable | yes | UNCHECKED by a hub — read by the derive: `git log main..setups/seven-0921` → `61a283f` adds 0013; bars `02d67a6` adds 0012 |
| F-16 | (a) F30 corrected | 3 of 4 | Fable | yes | Checked row 4 / FC3 HOLDS (count now 18, noted beside it) |
| F-17 | (a) F33 corrected | 3 of 4 | Fable | yes | hub WRONG FACTS "F33" HOLDS; FC6 (ladder `:606-623`) |
| F-18 | stale citations (`:3` pin, ladder `:590`/`:596-599`, `radar_panel.py` commits) | 3 of 4 | hub-checked lines | no | citation fixes only: Checked rows 3, 7, 9; FC5, FC6 |
| F-19 | (a) `create_state` writer | 3 of 4 | none | not taken | FC8 UNVERIFIABLE FROM READS → X9 before C1 |
| F-20 | (a) `last_price` writer `:1032` | 3 of 4 | none | not taken | gemini gives no wording; `last_price` is stale-score's lane (§9); derive read: writer exists at `cards/store.py:1032` |
| F-21 | (a) O7 B needs no new edge | 3 of 4 | Fable | yes | into O7 as its price; UNCHECKED by a hub — read by the derive at `cards/store.py:469-486`; grok agrees; gemini's `IllegalTransition` is today's behaviour, not a contrary mechanism |
| F-22 | (b) one fill path | 3 of 4 | grok | yes | Checked row 1 HOLDS; `mark_filled` with `fill(conn=)` is smaller than Fable's new orchestrator (→ O17) |
| F-23 | (c) running shares, corrections | 3 of 4 | none | not taken | → R2-2: stored chain + neighbour checks (grok) vs derived running (Fable); gemini: UNIQUE impossible |
| F-24 | (c) migration sets | 3 of 4 | none | not taken | → R2-3: grok cards/ for `kind`; gemini cards/ + aset/; Fable all in db_migrations (derive read: `0007:27` ALTERs `"user".aset_sizings`) |
| F-25 | (c) numbering | 3 of 4 | grok | yes | 0012/0013 on unmerged branches (derive read); the number is the desk's at the L68 gate |
| F-26 | (d) realized-R inputs | 3 of 4 | none | not taken | covered by F-01; grok's (d) names `cobalt_stop` (struck F-28) and `direction` (R2-2); Fable's names `r_planned` (O15) |
| F-27 | (e) drift warning | 3 of 4 | grok | yes | hub ESCALATE 4 three-way; WRONG FACTS "§4 contradiction" HOLDS; grok's pct-only is smaller than Fable's ATR store+display (→ O3 B) |
| F-28 | (f) `cobalt_stop` per leg | 3 of 4 | Fable | yes | smaller (no column); rests on proposal F13 (PROVEN, `0007:3-8`); grok's keep → O20 |
| F-29 | (f) FILLED stop-edit share count | 3 of 4 | none | not taken | defect HOLDS (Checked row 2, FC2); its form depends on R2-2 (tail `running_after` vs derived) |
| F-30 | (f) his stop is the plan; structural visible; STOP_EDITABLE | 3 of 4 | proposal kept | n/a | grok, Fable ADOPT these parts |
| F-31 | (g) DM listener mechanics | 3 of 4 | grok | yes | kill-first unanimous; Fable's RED rule N → O10; gemini's coupling carried under O8 |
| F-32 | O8 costs | 3 of 4 | grok + Fable + gemini (costs, side by side) | yes | "with the cost each house named"; Fable's UNCHECKED claims read by the derive: Charter `:144-145`, `matches_kill_phrase` has no caller (`jobs/killswitch.py:106`, `:128`) |
| F-33 | (h) note path column | 3 of 4 | grok | yes | hub (h) 2-0 defect; column only is smaller than Fable's reuse-the-sizing-note (→ O4 B) |
| F-34 | (h) body is a code copy | 3 of 4 | grok | yes | hub WRONG FACTS "§7/F21" HOLDS; X14 |
| F-35 | (j) Charter #16 reading | 3 of 4 | Fable | yes | UNCHECKED by a hub — read by the derive at `MVP-CHARTER-v0_2.md:253-254`; confirmation → O13 |
| F-36 | (k) platform boundary | 3 of 4 | proposal kept | n/a | NONE, unanimous, hub-confirmed |
| F-37 | (l) chunks, parallel, hours | 3 of 4 | grok | yes | hub ESCALATE 5; all three: C3 ∥ C4 false as written; grok's is the only re-derivation of hours |
| F-38 | (l) order | 3 of 4 | grok | yes | Checked row 4; desk lane (L68) stated as fact |
| F-39 | (m) F14/F15 seams | 3 of 4 | Fable | yes | UNCHECKED by a hub — read by the derive at `prefill/drc.py:67`, `:70`, `:123-130`; seam (7) matches grok (m) and gemini (m) |
| F-40 | (n) test plan changes | 3 of 4 | grok | yes | keeps proposal cases, adds crash/race/correction/vault-fail; ATR fixture struck (all three) |
| F-41 | §9 L52 finding | 3 of 4 | proposal kept | n/a | Checked row 10 / FC7 HOLD; re-answered in v2 `## L52 and the bar` |
| F-42 | closing verdicts | 3 of 4 | none | not taken | grok BUILD AFTER, Fable BUILD AFTER, gemini DO NOT BUILD → R2-1; gemini's text in `## Dissents, verbatim` |

## NEEDS ROUND 2

**R2-1 — gemini's DO NOT BUILD against v2.**
- Gemini: "TRIBUNAL R1: DO NOT BUILD 5 write paths with a broken risk recompute and two-transaction seam."
- Grok: "TRIBUNAL R1: BUILD AFTER one fill transaction, running-share risk, correction chain checks". Fable: "BUILD AFTER derive folds same-transaction fill, leg lock, pct-only warning, 0014 numbering".
- Question: v2 §2 folds grok's one-transaction fill (`fill(conn=)`, `mark_filled` one connection); §5 names the share-count fix with its form in R2-2. Against v2's text, does the DO NOT BUILD stand? If yes, name the defect in v2's text with `file:line`.

**R2-2 — the legs correction and running-share mechanism (Q3, Q4, (c), (d), (f)).**
- (a) Index. Grok: "There is no UNIQUE `(card_id, seq)` constraint." / "A partial unique index needs an `is_current` flip, which `refuse_row_update()` forbids." Gemini: "A correction row makes `UNIQUE (card_id, seq)` impossible to enforce on the base table if old rows are never updated (you cannot use a partial index without a marker on the old row)." Fable: "`UNIQUE (card_id, seq) WHERE corrects IS NULL` (one ORIGINAL row per seq; corrections are excluded from the index)."
- (b) Current row. Grok: "The head is the row of that seq that is not the target of another row's `corrects`." Fable: "`legs_current_v` = for each (card_id, seq) the row with the greatest id."
- (c) Running shares. Grok: stored `running_before`/`running_after`; "refuses the insert unless `running_before` and `running_after` still meet the neighboring current legs. A share change on a non-tail leg is refused." Fable: "No `running_after` column: running = entry-leg shares − Σ current exit-leg shares, computed in the store under the card row lock, never chained row to row."
- (d) FILLED stop-edit share count (the live defect's fix). Grok: "`in_trade_shares` = the tail current leg's `running_after` when an entry leg exists, otherwise the `shares` column (legacy cards with no legs)." Fable: "recomputes open risk from the RUNNING share count read from `legs_current_v` (entry shares − Σ exits) under the card row lock".
- (e) Cache after an entry-leg correction. Grok: "No other path writes them." Fable: "A correction of the entry leg updates the cache in that correction's transaction."
- (f) `direction`. Grok: "`sign` comes from `direction` stored on the entry leg." / "Without it, replay reads `aset_sizings.direction`, which is not the append-only record." Fable: "`direction` and `entry` have no UPDATE writer (grep `UPDATE aset_sizings SET` → none sets them), so they are as immutable as the leg rows." (Derive read: no `UPDATE aset_sizings` statement sets `direction` or `entry` — `cards/store.py:339`, `:622`, `:708`, `:730`, `:1032`, `:1040`, `:1169`, `:1222`, `:1246-1252`; `aset/store.py:233`.)
- (g) Two concurrent ½ taps. Grok: "two concurrent ½ taps, one refused, running consistent." Fable (X6): "the second computes running 50 and writes 25, never 50."
- Question: which mechanism is correct for (a)–(g) under L57 and `refuse_row_update()`, and does it make grok (c) scenarios 1–4 / Fable (c) scenarios 1–4 impossible or refused? X4 and X7 settle (a)–(c), (g) on `cobalt_dev`.

**R2-3 — which migration set carries M1.**
- Grok: "`legs`, `legs_current_v`, the `aset_sizings` columns (`trade_note_path` and the drift fields), and M2's `dm_inbound` go in `db_migrations` FORWARD … `card_stop_edits.kind` goes in `cards/migrations/` (the set that created the table …)."
- Gemini: "`card_stop_edits` belongs in `cards/migrations/`, while `aset_sizings` belongs in `aset/migrations/`."
- Fable: "the precedent is that a numbered `db_migrations` file alters them. M1 = `db_migrations/0014_legs.sql` + `.rollback.sql`, carrying `legs`, `legs_current_v`, `card_stop_edits.kind`, `aset_sizings.trade_note_path` and the drift fields".
- Derive read (fact, not a ruling): `db_migrations/0007_radar_cards.sql:27` ALTERs `"user".aset_sizings`; `db_migrations/0002_move_tables.sql:64` moves tables by `SET SCHEMA`; `aset/migrations/` holds 0001–0009, `cards/migrations/` 0001–0002.
- Question: after `0002_move_tables`, which runner correctly applies an ALTER to `"user".card_stop_edits` and `"user".aset_sizings`, in what order relative to `db_migrations`, and with what rollback?

## OWNER ITEMS (after the tribunal)

None is a precondition to building C1–C4 or C6. C5's existence follows O8 (ESCALATE 3).

| O | item | raised by |
|---|---|---|
| O1 | ⅓ / ½ rounding | proposal; grok, Fable as framed |
| O2 | drift pct threshold P + comparator at equality | proposal; Fable (comparator); grok (B reopens >20 %) |
| O3 | ATR in the drift warning (none until the 09-03 text, or store+display in ATRs; which ATR) | proposal O3; grok O9; Fable (e); hub O9 |
| O4 | manual sheet notes at sizing (two files at fill) vs one note per card | proposal; Fable reframe; gemini (h) |
| O5 | exit_price / times / P&L filled while blank, or never | proposal |
| O6 | `trade_def` on a radar note from the card while blank, or never | proposal |
| O7 | radar fill before S4: two taps vs one from ARMED (priced ~10 lines, no new edge) | proposal; Fable, grok (a) |
| O8 | DM line in S3 or after (costs: grok, Fable; coupling: gemini) | proposal; all three |
| O9 | DM poll interval value | grok O10; Fable O10 |
| O10 | listener heartbeat RED rule (N missed polls) | Fable O11 |
| O11 | radar fill writes the daily note's FILL UPDATE block or not | Fable O12 |
| O12 | dataview `strategy` column vs `trade_def` notes (his template) | Fable O13; gemini, grok (h); author ESCALATE 5 |
| O13 | confirm the #16 reading (one entry, many exits) | gemini O9; Fable (j); author ESCALATE 6 |
| O14 | the preset SET (mock #2) | Fable O9 |
| O15 | realized R also on the planned unit | Fable Q1 (smaller mechanism taken) |
| O16 | `fills` declared name: keep or strike | Q2 split (grok vs gemini, Fable) |
| O17 | build shape: `mark_filled` + sequential C3 → C4 vs orchestrator + parallel | Fable (b), (l) vs grok (b), (l) |
| O18 | `sheet_mismatch` basis: today's day mode vs the card's sizing sheet | grok Q5 vs Fable Q5 |
| O19 | ↺ on a manual card: hidden vs shown and refused | Fable Q11 vs grok (f) |
| O20 | Cobalt's stop per leg: computed at render vs stored per leg | Fable (f) vs grok (f) |

## FOR DEJAN

Each: A = what v2 builds by default · B = the alternative a seat named. No seat that holds a side recommends (L37); this derive seat recommends nothing.

- **O1 · ½ / ⅓ taps (IN-TRADE card, mid-trade).** 101 shares, you tap ½: A = 50 shares logged (round down) · B = 51 (round to nearest). Proposal; grok and Fable took no side.
- **O2 · drift warning line (IN-TRADE card, at the fill).** A = one threshold for radar and the manual sheet (proposal suggests 20) · B = 20 on radar, 25 on the sheet. Also: does exactly 20 % warn? Proposal; Fable (equality); grok (B reopens the Charter's >20 %).
- **O3 · ATR on the drift line (IN-TRADE card, at the fill).** A = % only, no ATR, until you give the 09-03 note (grok) · B = % plus "drift 0.05 ATR" shown and stored, not gating until you give a floor K (Fable).
- **O4 · trade notes for manual-sheet trades (your `2 - Trades` folder).** A = today's note at sizing stays, and a second note appears at the fill; the card points at the fill note (grok) · B = one note per trade — created at the fill only (proposal) or created at sizing and refreshed at the fill (Fable).
- **O5 · exit_price / entry_time / exit_time / profit_loss in your trade note.** A = Cobalt fills each only while blank · B = yours, never written. Proposal.
- **O6 · `trade_def` in a radar trade note.** A = Cobalt fills it from the card while blank · B = yours. Proposal.
- **O7 · radar card before the S4 detector (`/radar`, ARMED).** A = two taps: TRIGGERED, then FILLED · B = one FILLED tap writes both steps as yours (~10 lines, no new edge — Fable, grok).
- **O8 · DM fill line (your phone, Mattermost).** A = "[TICKER] filled [PRICE] 10" works in S3: +8 h, a new always-on listener that also hears the kill phrase · B = panel only in S3, DM later: the Charter's fallback sentence waits; the kill phrase stays unheard as today. Gemini: kill phrase tied to a feature listener.
- **O9 · how often the DM listener checks (with O8 A).** Your number; no default. Grok, Fable.
- **O10 · when the listener turns RED on the heartbeat (with O8 A).** Your N missed checks; no default. Fable.
- **O11 · radar fills in your daily note.** A = the trade note only · B = also the FILL UPDATE block the manual sheet writes today. Fable.
- **O12 · the Strategy column in your daily trades table (Obsidian).** New notes carry `trade_def`, so the column shows blank. A = leave your template · B = you change the column. Outside S3; all three seats.
- **O13 · "single fill at MVP" (Charter #16).** A = one entry fill, many exit taps (all three seats' reading) · B = you read #16 otherwise.
- **O14 · which exit taps exist on the card.** A = ½ · ⅓ · flat · typed (as in F11) · B = your set. Fable (mock #2 open).
- **O15 · R on your trade (DRC).** A = R on the risk you actually took at the fill (all three) · B = also R on the planned risk beside it, for comparison with the replay (Fable).
- **O16 · an unused `fills` table name in the schema.** A = keep it for later partial entries (grok) · B = remove it (gemini, Fable). Nothing you see changes.
- **O17 · how S3's panel and note get built.** A = one after the other on the existing fill path (grok; ~42 h) · B = a new fill function so panel, note and DM build in parallel (Fable). What you see is the same.
- **O18 · the red "sheet mismatch" flag on a fill (card, DRC).** A = flagged when your attested sheet ≠ today's day mode (grok) · B = flagged when it ≠ the sheet the card was sized on (Fable).
- **O19 · ↺ on a manual-sheet card (no Cobalt stop exists).** A = no ↺ shown (Fable) · B = ↺ shown, tapping it says why it cannot reset (grok).
- **O20 · Cobalt's stop beside your stop on each exit (DRC gap).** A = computed from the card's structural stop when shown (Fable) · B = also stored on every exit row (grok). What you see is the same.

## Redactions

5 spans, all in v2, none in this report: `S3-EXITS-PROPOSAL-2026-09-21.md:139` — his traded ticker ×2 and two prices (4 spans) → `[TICKER]` / `[PRICE]`; `:151` — one price (1 span) → `[PRICE]`. Final check: `grep -c -E` for the three literals on v2 → 0. The houses' texts taken verbatim already used `[TICKER]` / `[PRICE]`. No house proposed a value for one of his keys.

## READING

- `LAWS.md` in full (`:1-407`) · hub `s3-exits-tribunal-2026-09-22.md` whole · `r1/grok-ruling.md` whole · `r1/gemini-ruling.md` whole · `s3-exits-tribunal-fable-r1-2026-09-22.md` whole (incl. `## Self-attack`, 2 WITHDRAWN) · proposal whole · `s3-exits-design-2026-09-21.md` whole · `cto-2026-09-20.md:275` (R38) · `cto-2026-09-22.md:54` (R36), `:74` (R13) · `cto-2026-09-21.md:47` · `MVP-CHARTER-v0_2.md` `:133-148`, `:205-207`, `:245-256` · `SPRINT-LADDER-v0_1.md` `:604-625` · `r1/01-QUESTIONS.md` (grep astra → none).
- Code, only where a fold turned on it: `cards/store.py` grep `structural_stop` (`:902`, `:919`, `:980`, `:996`), `:466-487`, `:728-734`, `:1167-1173` · grep `UPDATE aset_sizings` over `src/cobalt` · `aset/web.py` grep `save_fill_update|save_card(` (`:66`, `:1006`, `:1103`, `:1336`), `:699-703` · `prefill/drc.py` grep (`:67`, `:70`, `:101`, `:123`, `:129`), `:123-131` · grep `matches_kill_phrase` (`jobs/killswitch.py:106`, `:128`) · `ls` of `db_migrations/`, `cards/migrations/`, `aset/migrations/` · grep `ALTER TABLE|SET SCHEMA` in `0007_radar_cards.sql`, `0002_move_tables.sql`.
- Git: `log -1 -S` for R36, the hub and Fable stop lines · `log --oneline -3 main` (`ff63e95`) · `log --oneline --stat main..setups/seven-0921 -- src/cobalt/db_migrations` (`61a283f`, 0013) · same for `bars/chunk-2-0920` (`02d67a6`, 0012).
- Not read: his templates, any note of his, the card mock, ADR-0008/0009.

## ESCALATE

1. **The tribunal does not close: round 2 is owed on R2-1, R2-2, R2-3.** 09-21 R39's `grok`/`agy` extension ends 2026-09-22 23:59 ET; a round-2 run after that needs his word (the prompt's own note). Astra's meter returns Sat 09-26 06:47 ET.
2. **Live defect on main, independent of S3** (Fable ESCALATE 3; hub ESCALATE 2; Checked row 2 HOLDS by read): a FILLED stop edit on the manual sheet recomputes open risk on the planned `shares` column. v2 puts the fix in C2 with its form in R2-2; whether it is fixed before S3 is the desk's call. Unproven by a run until X19 (L70).
3. **C5 depends on one of his choices**: grok and the proposal gate C5 on O8 = A ("only if O8 is A"). Named per the derive rules; C1–C4 and C6 depend on none.
4. **L67's four-house count set aside for this tribunal by 09-22 R13**: three seats ruled; Astra reads v2 when its meter returns.
5. **Order and numbering (desk lane, L68)**: `0012` (`bars/chunk-2-0920`, `02d67a6`) and `0013` (`setups/seven-0921`, `61a283f`, wip) are unmerged; M1/M2 are numbered at the gate; S3-P1 is cut after the setups one-build lands.
6. **Hours (GUESS)**: 42 h without the DM, 53 h with it, plus round 2 and an unpriced S3-P3, inside 09-24 → 10-07; build starts only after the FINAL.
7. **`create_state` (`cards/store.py:560-629`) is unsettled** (FC8, grok X8): X9 must run before C1 (L3).
8. **Grok's verbatim texts cite packet files** (`02-greps.txt:<n>`, `12-scope-and-rulings.md`, `33-migrations.excerpt.sql`, `22-trade_note.py`) that live only in the gitignored scratch folder; a reader of the committed v2 cannot open them. v2 keeps the text verbatim (rule); the desk may keep that folder until the FINAL.

## CONTINUE

Done. Both files written. Next is the desk's: commit v2 and this report; draft the round-2 hub for R2-1 … R2-3 only, with the same approved strings (a run after 2026-09-22 23:59 ET needs his word for `grok` / `agy`); bring `## FOR DEJAN` to him after the tribunal closes.

S3 EXITS DERIVED v2 · folds: 42 · verbatim: 26 · needs round 2: 3 · owner items: 20 · ESCALATE: 8
