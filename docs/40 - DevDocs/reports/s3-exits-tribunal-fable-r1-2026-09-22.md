BLIND: I did not read the houses' folder or the hub's report.
REPORT NAMED FROM date: 2026-09-22

Seat `s3-exits-tribunal-fable-0922` · Fable 5.1 (`claude-fable-5-1`) · round 1 of ≤3 · authorization: FABLE ROW `R57` (`cto-2026-09-21.md:68`, "Fable seat: yes", names `S3-EXITS-PROPOSAL-2026-09-21.md`; row committed `b2b454f`, proposal name in a desk file `000b46e`, proposal committed `b72b204`; R38 carries "B with your addition", R46 carries "For the designs and creations we need the higher level models"; the ten launch-line strings each count 1 in `22-draft-setups-tribunal.md`). Main at read time: `1698c99` (the proposal cites `be58530`). L32: every price and ticker below is hypothetical or `[TICKER]` / `[PRICE]`; his templates were read by headings and key names only.

## DIGEST FOR THE DESK

**Closing line: `TRIBUNAL R1: BUILD AFTER derive folds same-transaction fill, leg lock, pct-only warning, 0014 numbering`.**

- Q1 R_unit — ADOPT WITH: realized R on the ACTUAL unit `|fill − stop in force at fill|`; the planned unit is a second output of the same function, for F12 comparison.
- Q2 one `legs` table, `fills` struck — ADOPT.
- Q3 append-only + current view — ADOPT WITH: the index is `UNIQUE (card_id, seq) WHERE corrects IS NULL`; every leg write under the card row lock; running DERIVED, not chained.
- Q4 `actual_fill…` cache — ADOPT WITH: kept, but written in the SAME transaction as the entry leg (today it is a second transaction).
- Q5 attestation at fill — ADOPT WITH: record + flag; the flag is a named column on the entry leg; compared against the card's own `sheet_mode`.
- Q6 "27 % past plan" — ADOPT: both readings give `distance_change_pct = 27` (derived below).
- Q7 DM ambiguity — ADOPT (refuse with candidates).
- Q8 note edit — ADOPT (override only, no reverse parse).
- Q9 synchronous note — ADOPT WITH: banner says FILLED first; a same-path collision refuses instead of merging two trades into one note.
- Q10 TRIGGERED expiry — ADOPT (covered by `EXPIRABLE`, no new timer).
- Q11 ↺ target — ADOPT WITH: `structural_stop` on radar cards; a manual card has no ↺ (no Cobalt stop exists).
- Q12 REST poll — ADOPT WITH: the interval is his, a `"user".trader_settings` key, refused at resident start when missing.
- (a) fact base — ADOPT WITH: three missed writers/callers added (`save_fill_update`, `save_card` at the key tap, `cobalt cards move`); F29/F30/F33 corrected; O7 B needs no edge, it changes `fill()`'s strict rule.
- (b) one fill path — ADOPT WITH: one orchestrator function called by panel, sheet, CLI and DM; `mark_filled` is TWO transactions today and C1 must move the fill columns inside `fill()`'s.
- (c) `legs` — ADOPT WITH: running derived; CLOSED-card corrections that reopen the position refused; M1 = `db_migrations/0014` by the 0007 precedent; 0013 is TAKEN.
- (d) realized R — ADOPT WITH: the function reads the card's direction and entry too; its version string is rendered beside every R.
- (e) drift — REJECT the AND gate: a 27 % fill on a wide-ATR card would not warn; pct alone fires; ATR is displayed and stored; a missing setting never refuses a fill that already happened.
- (f) stop override — ADOPT WITH: in-trade open risk from RUNNING shares (today it reads the planned `shares` column); `cobalt_stop` per leg dropped (it is on the card).
- (g) DM — ADOPT WITH: kill phrase checked FIRST on every post; O8's costs priced; the Charter names the DM line in F11's acceptance.
- (h) F22 — ADOPT WITH: a card that already has a note (manual, from `/size`) gets THAT note refreshed at fill, never a second file.
- (i) attestation — ADOPT WITH (as Q5).
- (j) Charter #16 — ADOPT WITH: one entry fill, many exit legs; the preset SET is mock #2, still open, his.
- (k) boundary — ADOPT: NONE.
- (l) chunks — ADOPT WITH: C3 ∥ C4 ∥ C5 is true only with the (b) orchestrator; migration sets named; hours UNVERIFIED.
- (m) seams — ADOPT WITH: `_read_strategy` reads `strategy` and the DRC parses the daily note's FILL UPDATE block, both miss radar trades; the "R had Cobalt's stop held" figure is a 21:10 figure, never a 15:41 one.
- (n) experiments — ADOPT WITH: X1–X12 below.
- Experiments named: 12. Owner items: O1–O8 as framed (O4 reframed), plus O9–O13.
- WITHDRAWN sentences: 2. ESCALATE: 5.

## Rulings

### Q1 — R_unit: planned vs actual
**ADOPT WITH** — replace §3 "Realized R" unit sentence with: "R_unit = |entry-leg price − stop_in_force on the entry leg| (the risk he actually took: the fill recompute sized him on `|fill − stop|`, `aset/engine.py:287-293`). The same function also returns `r_planned` on `|card.entry − stop_in_force|`, the unit F12's counterfactual uses (`replay/cards.py:22-25`, `:258-259`), so the DRC can set realized R beside `cf_r` without a second formula. One function, two named outputs, one version string."
- The stop is the same in both options: `STOP_EDITABLE` is WATCH and FILLED only (`cards/models.py:120`, refused in the store `cards/store.py:661`), so no edit can land between ARMED and FILLED; stop at trigger = stop at fill. The choice is entry vs fill, nothing else.
- Failing scenario if only the planned unit were used: card 41 long, entry 10.00, stop 9.90 (planned 0.10); filled at 10.05 (actual 0.15), 66 shares; exits flat at 10.20. Actual: (0.15 × 66) / (66 × 0.15) = +1.00 R on the risk taken. Planned: (0.15 × 66) / (66 × 0.10) = +1.50 R. The DRC adherence question is "did the trade pay for the risk taken"; 1.50 R overstates it by the drift he was warned about.
- Comparability with F12 is real (the replay's denominator is the planned risk by design, `replay/cards.py:23-25`), which is why the planned figure stays as a second output rather than being dropped.
- No aggregate is rendered in S3 (§3), so L8 is not reached here.

### Q2 — one `legs` table with `kind`; `fills` struck
**ADOPT.**
- `fills` exists only as a declared name (`db_migrations/placement.py:110`; grep `"fills"` → that line alone). Striking it costs one dict entry. One table with `kind ∈ {entry, exit}` and a partial UNIQUE on the entry keeps "single fill at MVP" (Charter :253) as a constraint.
- If partial entries arrive post-MVP, the partial UNIQUE is dropped and `seq` already orders them; no second table is needed then either.

### Q3 — append-only corrections + a current view vs UPDATE in place
**ADOPT WITH** — replace §3's index and correction sentences with: "`UNIQUE (card_id, seq) WHERE corrects IS NULL` (one ORIGINAL row per seq; corrections are excluded from the index). `legs_current_v` = for each (card_id, seq) the row with the greatest id. A correction row copies `seq` and `kind` from the row it corrects; the store checks that under the card row lock (`SELECT … FROM aset_sizings WHERE id = %s FOR UPDATE`, the same lock `transition()` takes, `cards/store.py:275-278`) because a cross-row CHECK cannot. `"user".refuse_row_update()` (`0007_radar_cards.sql:105-111`) is attached, as on `card_dots`."
- "UNIQUE (card_id, seq) among current rows" is not a DDL: currency depends on OTHER rows, and a plain UNIQUE breaks on the first correction (the correction row shares the seq). The partial form above survives: original rows are unique per seq; a correction of a correction is also excluded; the view picks the latest.
- UPDATE in place is refused by `refuse_row_update()` on every append-only user table already (`0007:190`, `:199`); the proposal's shape matches the house style.
- The running-share consequences of corrections are ruled under (c).

### Q4 — `aset_sizings.actual_fill…` kept as a cache or retired
**ADOPT WITH** — replace §12 Q4's premise with: "Kept as a cache of the entry leg — like `state` caches `card_transitions` — on one condition: the fill columns are written INSIDE `fill()`'s transaction, by the same function that inserts the entry leg, so `actual_fill` equals the entry leg's price by construction. A correction of the entry leg updates the cache in that correction's transaction. Today `mark_filled` is two transactions (`aset/store.py:217` — `fill()` commits at `cards/store.py:519` — then a second `with self._connect()` at `:230`)."
- Readers of the columns today: `aset/store.py:312` (the day's rows for the DRC), `aset/daily_note.py:136` (the FILL UPDATE block from the in-memory `FillRecompute`, not the DB), `prefill/drc.py:196` (parsed from the daily note, not the DB). Retiring them means rewriting the `:312` SELECT and the DRC's fill source; keeping them is the smaller change.
- Failing scenario under today's two transactions: card 41, `fill()` commits FILLED at 10:12:07; the UPDATE at `:231` matches 0 rows (a row deleted by a concurrent backfill, or a connection drop) → `RuntimeError` at `:252` → the sheet shows FAILED, the card is FILLED, the fill columns are NULL, and no retry path exists. Under the same-transaction rule the card stays TRIGGERED and he taps again.

### Q5 — attestation mismatch at fill: record + flag vs refuse
**ADOPT WITH** — replace §8 bullet 3 with: "A fill is never refused for a sheet mismatch. The entry leg stores `day_mode_id`, `attested_sheet` (the `day_modes` value at fill time, `daymode/store.py:155-158`) and `sheet_mismatch boolean NOT NULL`, true when the attested sheet at fill differs from the sheet the card was SIZED on (`aset_sizings.sheet_mode`, written by the key tap `cards/store.py:1169-1173`) or when nothing is attested. The panel and the DRC render it red."
- Failing scenario for REFUSE: 09:47, card 41 TRIGGERED, he is filled in his broker, he taps FILLED; the day mode changed at 09:45 and he has not re-attested → `SheetMismatch` → the card sits TRIGGERED; `EXPIRABLE` includes TRIGGERED (`cards/expire.py:71`) → at the window end the radar EXPIRES it (`:305-308`) → a trade he took is recorded as never taken and the DRC's "trades taken (FILLED only)" (ladder `:612`) is wrong.
- Failing scenario for RECORD without the column: a fill recorded against `attested_sheet = NULL` with nothing flagging it → the DRC's adherence question has no signal. The column is the honest record.
- The ladder refuses CREATION only (`:610`); comparing against the card's `sheet_mode` rather than only today's mode is what "a fill is recorded against that stated sheet" means when the sheet changed between the tap and the fill.

### Q6 — "27 % past plan"
**ADOPT** — `drift_pct = 27` under the code's formula, and the alternative reading gives the same number.
- Derivation from `aset/engine.py:295-298`: `planned_distance = per_share_risk = |entry − stop|`; `new_distance = |fill − stop|` (`:287`); `distance_change_pct = |new − planned| / planned × 100`.
- Reading A ("27 % drift"): by definition 27.
- Reading B ("a fill 27 % of the planned distance beyond the trigger"): long, fill = entry + 0.27 × planned → new = planned + 0.27 × planned = 1.27 × planned → pct = 0.27 × 100 = 27. Short: fill = entry − 0.27 × planned, same algebra. A fill 27 % of the distance TOWARD the stop gives new = 0.73 × planned → pct = 27 as well (abs). The two readings coincide; the fixture is entry E, stop S, fill = E ± 0.27·|E − S|.
- The comparator (`>=` today at `:301`, ">" in the Charter `:138`) matters only at equality; it is part of O2.

### Q7 — DM ambiguity: refuse with candidates vs latest card wins
**ADOPT.**
- Two open cards on one ticker are possible today: the one-open-card index is per (member, def, direction) (`0007:90-92`), so a long and a short, or two defs, can both be TRIGGERED. "Latest wins" would write a fill on the wrong card with actor YOU; a refusal with `TICKER#id` candidates costs him one more line.

### Q8 — a human edit to a `cobalt-legs` line
**ADOPT.**
- `upsert_unit` already records the override and keeps his text (`vaultwrite/writer.py:654-660`); a reverse parse would be a second writer of `legs` (L3) and an LLM-free parser of free text is a second grammar to maintain. The DRC's "estimated legs to confirm" (ladder `:612`) is the place he corrects, and a correction row is the record.

### Q9 — note synchronous in the fill request vs a queued job
**ADOPT WITH** — add to §7 bullet 1: "The banner's first words are `FILLED · card <id> · legs row <id>`; the note failure follows, never precedes. Before `create_if_absent`, if the computed path already exists AND another card's `trade_note_path` equals it, the write is refused with both card ids named — `upsert_trade_note` would otherwise MERGE the second card's five keys into the first card's note (`prefill/trade_note.py:154-169`) and report `updated`."
- Synchronous meets "fill at 10:12 → note by 10:13" without a queue, a worker or a job row; the retry CLI covers the failure arm; `create_if_absent` is idempotent (`writer.py:568-578` returns `skipped_exists`).
- Failing scenario for the collision clause: cards 41 and 42, both `[TICKER]`, filled in one DM poll cycle at 10:12:07 → one filename from the pattern (`prefill.yaml:14`, seconds resolution) → without the clause, one note for two trades and the daily dataview shows one row.
- A second fill request on the same card cannot write a second note: `fill()` refuses a FILLED card (`cards/store.py:479-480`) before the note step runs.

### Q10 — does the existing radar expiry cover TRIGGERED
**ADOPT.**
- `EXPIRABLE = (WATCH, ARMED, TRIGGERED)` (`cards/expire.py:71`); `radar_expiry` applies `avoid` and `deadline` to every EXPIRABLE state and stop-touch to WATCH only (`:285-310`); the manual `expire_due` walks the same tuple (`:182`). "No tap by expiry → EXPIRED" (Charter `:138`) is the `deadline` cause. No TRIGGERED-specific timer is owed.

### Q11 — ↺ reset target
**ADOPT WITH** — replace §5 bullet 1's reset definition with: "Reset = a stop edit with `kind = reset` whose `to_stop` is the card's `structural_stop`. A manual card has no `structural_stop` (the column is added by `0007:38` and written only by `create_radar_card`, `cards/store.py:980-996`); on a manual card the ↺ control is not rendered and the sheet's existing wording stands (`aset/web.py:701`: reset = re-enter the card stop)."
- A Cobalt in-trade trail does not exist (`grep trail` → `cards/trail_fit_draft.py` only, a draft); M8's trail selection is not in S3's scope.

### Q12 — DM resident: REST poll vs websocket; the interval
**ADOPT WITH** — replace §6's resident bullet's interval clause with: "The poll interval is HIS (L53): key `dm.poll_interval_s` in `"user".trader_settings` (name to be confirmed at the derive), read at start by the same `CardSettingsReader` pattern (`settings/card.py:178`: a missing row refuses to start, loud). It is never a committed config value."
- REST is right: the outbound module deliberately carries no websocket (`notify/mattermost.py:6-11`); a poller is the deterministic watcher L2 names; `_api` already speaks `/api/v4` (`:105`).

### (a) THE FACT BASE
**ADOPT WITH** — §1 gains three rows and three corrections, pasteable:
- "F34 — `aset/daily_note.py:229-248` `save_fill_update`: the manual `/fill` writes a FILL UPDATE unit into the DAILY note (`aset/web.py:1103`), keyed on the original card timestamp. The radar key tap writes the card block into the daily note (`save_card`, `aset/web.py:1336`). Neither is a trade-note writer, both are vault writers of the fill/card. PROVEN."
- "F35 — `cards/cli.py:83` `cobalt cards move <id> FILLED` calls `fill()` with no price, evidence `{"via": "cobalt cards move"}`: a third caller of the one fill path, and a second way (with the sheet button, `aset/web.py:640`) to reach TRIGGERED. PROVEN."
- "F36 — `mark_filled` is TWO transactions: `fill()` commits (`cards/store.py:519`), then a second connection UPDATEs the fill columns (`aset/store.py:230-250`). PROVEN."
- F29 corrected: "`0013` is TAKEN by `setups/seven-0921` (`61a283f`, `0013_tunables_slug_nullable.sql`). The next free number is `0014`."
- F30 corrected: "At 13:4x ET 2026-09-22 both branches exist: `setups/seven-0921` is 17 commits ahead of main; `s2/stale-marker-0921` (`cddf32c`) is 0 commits ahead — already in main."
- F33 corrected: "The ladder carries the ATR text (`SPRINT-LADDER-v0_1.md:610` 'drift warning scaled to ATR (his 09-03 defect)', `:621` 'ATR-scaled drift'); what has no source is the '09-03 defect' origin only."
- Every other row I could open holds (F1, F2, F3 by its docstring `:254`, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15 by `expire.py:71` and `store.py:989`, F16 with F35 added, F17, F18, F19, F20 by `writer.py:559` and `:644`, F21 with the body caveat under (h), F22, F23, F24, F25 keys, F27, F28, F32). F25's dataview and F26 are UNVERIFIED by me — L32 bars the body line; F31 (the mock) was not in my read set.
- Writers of `state`: `cards/store.py:339` (`transition`), `:622` (`create_state`, genesis) — §1 names the first only; the genesis writer is not a fill path, so no ruling turns on it. Writers of `stop`: `:708`, `:730` (`record_stop_edit`) — named (F12). Writers of the fill columns: `aset/store.py:233` only — named (F6). No writer was missed that changes a ruling; F34/F35 are missed callers, not missed writers of the card row.
- §2 edge walk: ARMED→TRIGGERED, TRIGGERED→FILLED, TRIGGERED→PASSED, {WATCH, ARMED, TRIGGERED}→EXPIRED, FILLED→CLOSED — every row is an edge in `ALLOWED` (`cards/models.py:92-110`); the exit leg writes no transition (§2 row 5), consistent with the stop-edit precedent (`0002_card_stop_edits.sql:3-6`). **No row needs a new edge.** O7 B (one tap from ARMED, both rows actor YOU): `fill()` computes `route = [TRIGGERED, FILLED]` and `strict = origin is not MANUAL or len(route) <= 1` → True for a radar card → `transition(ARMED→FILLED)` → `IllegalTransition` (`cards/store.py:482-486`, `:512-517`). O7 B is a change to the `strict` rule at `:486` (walk the route for a radar card too, actor YOU on both rows, evidence naming "pre-S4 tap"), not a new edge; the docstring's reason for the refusal (`:469-473`, the detector's record) has no force until S4's detector exists (F16). Priced: ~10 lines in C1, one test. His A/B stands.

### (b) L3 — ONE FILL PATH
**ADOPT WITH** — replace §2's "The one fill path" paragraph with: "One orchestrator `aset.fill_card(card_id, *, price, shares, price_source, price_asof, source, now)` (C1) does, in order: `SizingResult.from_card(row)` → `compute_fill_recompute` (the existing typo guard `max_fill_distance_pct` and its config, `engine.py:279-285`, unchanged) → ONE transaction: `fill()`'s hops, the entry `legs` row, the `aset_sizings` fill columns, the drift receipt fields → commit → the trade note (C4) → the return value the caller renders. Its callers are the panel fill route (C3), `/fill` (which today rebuilds from the form, `aset/web.py:1057-1062`, and switches to `from_card` + the posted price), `cobalt cards move … FILLED` (F35) and the DM line (C5). `from_card` reads exactly the columns `compute_sizing` wrote (`entry, stop, grade, risk_budget, direction, sheet_mode, ticker`); it carries NO default that the form path does not — a NULL in any of them refuses, because a card that reached TRIGGERED was sized (`cards/store.py:299-309`)."
- Where a second path would appear without this: the panel route calling `store.fill()` directly (as `/card/{id}/move` does at `aset/web.py:1203-1208`) would be a fill with no price, no leg and no recompute — exactly ESCALATE 1's hole, reproduced on the panel.
- The seam §10 C1 needs: `fill()` exposes its open transaction to the leg insert. `transition()` already has `before_commit` (`cards/store.py:250`, `:360-361`) and `_write_tx` (`:849`) has one; `fill()` (`:429`) has neither. C1 adds a `within=` callback to `fill()` that runs after the FILLED hop and the pick savepoint (`:518`), before `conn.commit()` (`:519`). ~15 lines, no new edge, one test.
- `mark_filled`'s second transaction (`aset/store.py:230`) is retired into the orchestrator's one transaction (Q4); the sheet's `save_fill_update` daily-note block stays the manual sheet's (owner item O12 says whether the panel writes one).

### (c) THE `legs` TABLE
**ADOPT WITH** — replace §3's "running_before, running_after" row and the compounding paragraph with: "`running_before int NOT NULL` — the running count the preset was computed from, a STORED INPUT (L57). No `running_after` column: running = entry-leg shares − Σ current exit-leg shares, computed in the store under the card row lock, never chained row to row. CHECK on an exit row: `shares > 0`; the store refuses a leg whose shares exceed the running count it just computed. CLOSED is written in the same transaction as the leg that brings running to 0." And add: "Corrections: a correction may change price, time, flag, source; it may change shares only while Σ current exits ≤ entry shares AND (on a CLOSED card) the running count stays 0 — otherwise it is refused naming the rows, because CLOSED has no outgoing edge (`cards/models.py:106`) and a correction that reopens a position would make the card's state lie."
- Disagreement scenarios with the proposal's stored `running_after` chain: (1) entry 100 sh, exit 50 (before 100, after 50); he corrects the entry to 80 → the exit row still says after 50, running is now 30 by arithmetic and 50 by the row; nothing recomputes. Derived running has no such row to go stale. (2) A correction lifting an exit from 50 to 120 on a 100-share entry → Σ exits > entry → refused. (3) Two taps racing: both read running 100, both write 50 → derived running −0 by rows but the chain shows two `before 100` rows; under the row lock the second tap reads 50. (4) A correction to the closing leg of a CLOSED card from 50 to 40 → running 10, state CLOSED, no edge back → refused by the rule above; the fix path is a correction that keeps running at 0 (price, time, flag) or the DRC correction pass.
- The index and view: ruled at Q3.
- Placement: `"user"` side, `user_id INTEGER NOT NULL DEFAULT (current_setting('cobalt.trader_id')::int) REFERENCES "user".traders(id)` as `0007:120`; `card_id … REFERENCES "user".aset_sizings(id) ON DELETE CASCADE` as `:121`; identity PK; `refuse_row_update()` trigger; sequence grant as `0007`'s header says (`:16-19`). `placement.py:109` already declares `legs` USER; `"fills"` (`:110`) is struck.
- Migration sets: `card_stop_edits` was created by `cards/migrations/0002` and `aset_sizings` by `aset/migrations/0001`, but `db_migrations/0007` already ALTERs `aset_sizings` (`0007:27-40`) and `0002_move_tables` moved both tables to `"user"` (`0002_move_tables.sql:48`) — the precedent is that a numbered `db_migrations` file alters them. M1 = `db_migrations/0014_legs.sql` + `.rollback.sql`, carrying `legs`, `legs_current_v`, `card_stop_edits.kind`, `aset_sizings.trade_note_path` and the drift fields; M2 = `0015_dm_inbound.sql`. The proposal does NOT say which set (§3: "the next free migration number is taken at build") — the derive says it. `0012` (bars) and `0013` (setups) both exist unmerged/merged as (a) records; L68 stacks them and the number is re-derived at the gate.

### (d) REALIZED R
**ADOPT WITH** — add to §3 "Realized R": "The function reads: the current legs view (price, shares, flag, kind, seq), the entry leg's `stop_in_force`, and from the card row `direction` and `entry` (for `r_planned`). `direction` and `entry` have no UPDATE writer (grep `UPDATE aset_sizings SET` → none sets them), so they are as immutable as the leg rows. The function carries a version string in the `FORMULA_VERSION` pattern (`replay/models.py:23`); every rendered R shows it, and F14's DRC row stores it beside the figure it quotes."
- Which stop after his R38 edit: the entry leg's `stop_in_force` = the stop at fill = the stop at trigger (Q1). A stop edit in FILLED changes OPEN risk (`engine.py:143-158`), not the R unit of a trade already sized; the DRC's "gap" reads the stop path from `card_stop_edits` (`replay/cards.py:547` walks it) and each leg's `stop_in_force`.
- `provisional = any current leg estimated` — ADOPT as written; a correction row with a typed price flips the current row to `confirmed` and the flag clears by the same read.
- L8: §3 says no statistic is rendered in S3 and F14 renders exit efficiency with n; ADOPT. A single trade's R is not an aggregate.

### (e) THE DRIFT WARNING
**REJECT** the AND gate of §4 bullet 3 (`drift_pct > P` AND `drift_atr ≥ K`) — `aset/engine.py:295-302` with `SPRINT-LADDER-v0_1.md:610` and the Charter test `MVP-CHARTER-v0_2.md:146`. Replacement wording for §4: "The warning fires on `drift_pct` alone, against his threshold (O2, key `card.fill_drift_warn_pct` in `"user".trader_settings`, comparator per O2); it is the Charter's '>20 % distance drift warns' (`:138`). `drift_atr = |new_dist − planned_dist| ÷ atr_working` is COMPUTED, STORED on the fill (receipt id, `atr_working` value, its bar ts, `evaluate.py:568`) and DISPLAYED beside the pct as `drift 0.05 ATR`; whether it gates or scales anything is O3, and until he rules it, it gates nothing. A manual card (no receipt) stores `drift_atr = NULL, drift_atr_unavailable = 'no radar receipt'` and shows 'ATR n/a — pct only'. A missing threshold row NEVER refuses the fill: the fill is recorded, `drift_warning = 'UNAVAILABLE: card.fill_drift_warn_pct missing'` is stored and rendered red, and the heartbeat carries it; the row is also checked at `com.cobalt.aset` start so it is loud before the first fill."
- Failing scenario for the AND: card 41, planned distance 0.10, `atr_working` 0.50 (a wide-ATR name on a tight stop). Fill 27 % past plan: |new − planned| = 0.027; `drift_atr` = 0.027 / 0.50 = 0.054 ATR. With any K ≥ 0.1 the AND is false → no warning → the Charter acceptance "fill 27 % past plan → warning" is RED. The proposal concedes this by choosing the fixture's ATR to pass (`§4` last bullet before the display sentence) — a fixture fitted to the design, the L45 failure shape.
- Failing scenario for "missing setting → refuse the fill": 09:47, TRIGGERED, filled in his broker, the settings row was never loaded → refused → TRIGGERED → expired at the window (Q5's sequence). L1's "loud" is satisfied by the red UNAVAILABLE field and the start-time check; a refusal of a fact that already happened is not fail-loud, it is fail-wrong.
- Smuggled values, named: P (his, O2), K (his, O3), `>` vs `≥` (O2), `atr_working` vs daily ATR — a unit choice, not a threshold; working-TF is the TF the stop lives on and the receipt already stores it (`evaluate.py:568`) while the daily ATR is only an input of `htf_level_proximity` (`:475`) — ADOPT the unit and NAME it in O3's text ("K in working-TF ATRs"); "latest receipt" — the last `radar_score_receipt` before the fill instant, its id stored (replayable, L57) — ADOPT.
- The two §4 sentences ("refused loudly" and "never blocks the fill") do contradict each other; the replacement resolves it toward the second.

### (f) STOP OVERRIDE PER R38
**ADOPT WITH** — replace §5 bullet 2 with: "In FILLED, `record_stop_edit` recomputes open risk from the RUNNING share count read from `legs_current_v` (entry shares − Σ exits) under the card row lock — today it passes the `shares` column (`cards/store.py:720`), which the fill never updates (`aset/store.py:233-240` writes `recomputed_shares`, not `shares`) and which no exit leg reduces. C2 changes that one argument." And strike `cobalt_stop` from the per-leg columns: "Cobalt's stop is the card's `structural_stop` (immutable, `0007:6-8`); the gap per leg is `stop_in_force − structural_stop`, computed at render. `stop_in_force` stays on every leg as the stored input."
- Failing scenario today, no S3 needed: manual card, planned 100 sh at entry 10.00 / stop 9.90; filled at 10.05 → `recomputed_shares` = ⌊10.00 / 0.15⌋ = 66 (`engine.py:291-292`), `shares` still 100; he moves the stop to 9.95 in FILLED → `used_risk` = 0.10 × 100 = 10.00 rendered; his real open risk on 66 shares is 6.60. After a ½ leg (running 33) the same edit still reads 100. ESCALATE 3 below — it is live on the manual sheet now.
- What R38 needs and gets: the stop path (`card_stop_edits`, every row kept, folded by id `cards/store.py:348-359`), the stop at fill on the entry leg, the stop in force on each leg, `structural_stop` always rendered (`radar_panel.py:1038` already shows it in LEVELS), the gap derivable per leg and per edit. A typed stop equal to `structural_stop` is still YOURS by the derived owner (last row actor YOU, kind edit) with gap 0 — correct: it was his decision.
- A manual card with no `structural_stop`: owner derivation still works (rows exist or not); the ↺ is absent (Q11); the gap is `NULL — no Cobalt stop`, rendered as such, never 0.
- `STOP_EDITABLE` unchanged: no F11 flow edits a stop in ARMED or TRIGGERED — a "re-read stop" after the drift warning happens in FILLED, which is editable.

### (g) THE DM LINE
**ADOPT WITH** — add to §6's resident bullet: "On every new post the listener checks `matches_kill_phrase` / `matches_resume_phrase` FIRST (`jobs/killswitch.py:106-120`), before the exits grammar; a kill match is acted on and logged even if the exits parser is broken. Its heartbeat probe is RED when the listener has not polled within N intervals (N his, with the interval key)." And under O8: the costs, pasteable: "O8 A (build in S3) costs C5 = 8 h + a plist + a heartbeat probe + M2 (`dm_inbound`) + a RESTARTS row for a new resident + the bot token's first READ use (the same VaultManager credential `notify/mattermost.py:19-21`, no new secret). O8 B (after S3) sets aside the Charter's own F11 acceptance sentence 'Fallback capture: a DM/voice line … writes the same rows' (`MVP-CHARTER-v0_2.md:144-145`) and the ladder's S3 row (`:610`); the panel tap path is complete without it (§6 bullet 1), and the kill phrase stays unlistened, as it is today (`matches_kill_phrase` has no caller: grep → its definition and `__all__` only)."
- Coupling a safety path to a feature path: today NO path carries the kill phrase, so the listener does not degrade a working safety path; it creates the first. One listener is L3's shape (`killswitch.py:109`: "the moment one lands"). The risk is the reverse — an exits bug taking the listener down takes the kill phrase with it — hence "kill check first" and the RED probe.
- REST vs websocket, the interval: Q12. Ambiguity: Q7. `dm_inbound` dedupe by post id — ADOPT; the poll must also skip the bot's own posts (X8).
- Whether the DM line is in S3 is O8, his; the tribunal prices, it does not choose.

### (h) F22 — THE NOTE
**ADOPT WITH** — replace §7's "Path" bullet with: "If the card already carries `trade_note_path` (a manual card written at `/size`, `aset/web.py:1019-1021`, or a retry), the fill event upserts THAT note: the existing merge refreshes Cobalt's five keys (`prefill/trade_note.py:160-168`) so `entry_price` becomes the fill price; no second file is created. If the column is NULL, the path is his pattern (`prefill.yaml:14`) with `when` = the FILLED transition time (ET), then stored on the card. `/size` stores the path it wrote in the same column (one UPDATE, C4). F14 reads the column; `find_trade_note_for_card` (`prefill/drc.py:101-120`, tolerance 30 s `:67`) is retired when F14 lands."
- The manual card at 09:40 / 10:12 under the proposal as written: O4 A → TWO files, `Trade-<day> 09-40-ss -[TICKER].md` (from `/size`) and `Trade-<day> 10-12-ss -[TICKER].md` (from the fill); `find_trade_note_for_card` returns the 09:40 one (within 30 s of `created_at`), the new column points at the 10:12 one; the dataview shows two rows for one trade. O4 B → ONE file at 10:12; `find_trade_note_for_card` returns None (delta 32 min > 30 s) and only the column finds it. Under the replacement: A → one file (09:40, refreshed at fill), B → one file (10:12); both found by the column.
- Vault write fails after the DB commit: FILLED first in the banner (Q9); retry `cobalt cards trade-note <id>` idempotent by `create_if_absent` (`writer.py:568-578`) then `upsert_unit` per leg; a retry racing a leg's `upsert_unit` on the same file is a writer-guard question I cannot read the outcome of → X1.
- `_render_body` (`trade_note.py:93-104`) is a CODE COPY of his template body, not a read of `5 - Templates/Individual Trade Template.md` at write time; §7 "his template body, verbatim" is verbatim as of the copy. I may not diff it (L32) → X2. If it has drifted, the derive decides between reading the template at write time (his template is his, R48) and keeping the copy.
- `strategy` vs `trade_def` (ESCALATE 5): the code side is settled by ADR-0008 D4 (`trade_note.py:30-37`; 69 notes migrated); the dataview column is HIS template (R48) → O13; nothing in S3 changes it. Cobalt's own reader `_read_strategy` (`drc.py:123-130`) still reads `strategy` → an F14 seam, (m).

### (i) ATTESTATION AT FILL
**ADOPT WITH** — as Q5: record + flag; the flag is `legs.sheet_mismatch boolean NOT NULL` on the entry row; the comparison is attested-at-fill vs the card's `sheet_mode` (and NULL attested → true).
- Nothing other than the entry leg writes `day_mode_id` / `attested_sheet`: today only `attest_sheet` writes the `day_modes` columns (`daymode/store.py:152-169`, from the sheet at `aset/web.py:486`, `:1168` and the CLI `daymode/cli.py:193`); the proposal names no reader on exit legs — correct, exits do not re-attest.
- `sheet_mismatch` had no home in the proposal (§8 bullet 3 says "on the card"); the entry leg is the row that records the fill, so it lives there.

### (j) CHARTER §5 #16
**ADOPT WITH** — state the reading in §1 F32 as: "Charter :253 '#16 single fill at MVP, partials post-MVP' answers the mock's question about partial ENTRIES; F11 :139-142 specifies scale-out EXIT legs and 'running shares 0 → CLOSED'. Reading: ONE entry fill (the partial UNIQUE on `kind = entry`), MANY exit legs. Charter :254 keeps '#2 scale-out presets' OPEN: the preset SET (which fractions exist) is his — O9."
- The reading reconciles two of his lines; he confirms it after the tribunal (an owner line, not a precondition — the constraint is one column to drop if he reads it otherwise).

### (k) CLAUDE.md'S ABSOLUTE BOUNDARY
**ADOPT — NONE.**
- `.htk`: attested, never read (`daymode/match.py:86-92`, `:101`; `daymode/store.py:140-141`). Fill price: typed, or the last polled price from the bars poll (`evaluate.py:567`, Finviz-lite/bars, not a platform). DM line: Mattermost, his own words. Prefill: `last_price` on the card. The "DAS log" for the DRC's correction pass (Charter `:143-144`): he reads it; "evening DAS execution-log reconcile = post-MVP" is the one future line that would touch the boundary and it is not in S3. Grep `-w DAS|Lightspeed|TradeStation|CenterPoint` over the six core dirs → docstrings and refusal messages only (`aset/models.py:5`, `aset/web.py:592`, `:1142`, `aset/engine.py:4`, `cards/models.py:61`, `daymode/*`).

### (l) CHUNKS, SEATS, ORDER, HOURS
**ADOPT WITH** — replace §10's parallel sentence with: "C3 ∥ C4 ∥ C5 holds only because all three call the (b) orchestrator: C3 owns `aset/web.py` (routes) + `aset/radar_panel.py` (render); C4 owns `prefill/trade_note.py` + the orchestrator's note step; C5 owns a new `dmlisten/` package + `notify/` (a `GET /posts` helper beside `_api`) + `jobs/` + M2 + its plist. C1 and C2 own `cards/store.py`, `aset/store.py`, `aset/engine.py`, `aset/models.py`, M1 — nothing in C3–C5 edits those files. The three land as ONE stacked set under L68's one gate; 'parallel' is a build-seat claim, not a merge claim."
- Seats by L29: C1, C2, C3 (routes), C5 — user-table write paths → Opus 5 floor, Fable at his call; C4 — a vault write path → the same floor; C6 — no write path → any seat (Sonnet permitted, non-write). Never auto mode on a write path (L29 restored clause).
- RESTARTS (a GUESS until `cobalt jobs restarts`, L42 — I cannot run it): `com.cobalt.aset` (`start_aset.sh` → `aset/web.py`, which imports `cards`, `prefill`, `vaultwrite`); `com.cobalt.radar` (`radar/runner.py:409` imports `cards.store`; `radar/evaluate.py` imports `cards`); one-shots that import `cards` / `prefill` / `aset` and pick up code at their next launch: `cards-expire`, `prefill-daily`, `prefill-drc`, `replay` (`replay/cards.py`, `replay/line.py`), `daymode-propose` (`daymode/drc.py`, `daymode/note.py`), `heartbeat` (`heartbeat/runner.py`), `seat-usage` (`seatusage/runner.py`); C5 bootstraps `com.cobalt.dmlisten` new. Both residents restart inside the 20:00–21:00 pause with residents down before the merge (L43/L66).
- Order: `setups/seven-0921` exists, 17 commits ahead, touches `cards/store.py` (`58aa823`, +7 −?) and `radar/evaluate.py`; `s2/stale-marker-0921` is already in main (0 ahead). S3-P1 is cut AFTER the setups build lands (or rebased over it) — ADOPT. §10's "`radar_panel.py` was touched twice today on main (`a660a7c`, `04b0dbd`)" — now four times (`490c231`, `71a8368` too); C3 rebases over all four.
- Hours: 35 h / 50 h — UNVERIFIED (no file re-derives a seat-hour; the setups one-build's report was not in my read set). Only the shape is checkable: C5 (8 h) is the one chunk O8 can defer; C6 (3 h) cannot be parallel. Window 09-24 → 10-07 = 10 trading days, also carrying S3-P3.

### (m) THE F14 / F15 SEAMS
**ADOPT WITH** — add to §7/§9 a "Seams left for F14/F15" list: "(1) `aset_sizings.trade_note_path` replaces `find_trade_note_for_card` (`prefill/drc.py:101-120`). (2) `_read_strategy` (`drc.py:123-130`) reads `strategy`; new notes carry `trade_def` (`trade_note.py:38-41`) — F14 reads `trade_def` from the note or `trade_def_slug` from the card (`0007:32`). (3) The DRC's fill data comes from the daily note's FILL UPDATE block (`drc.py:70` `parse_fill_updates`, written only by the manual `/fill`, `aset/web.py:1103`); a radar fill writes no such block — F14 reads `legs` and the fill columns (`aset/store.py:312`) instead. (4) Realized R + `provisional` + the estimated-legs list: the pure function of (d). (5) The stop path: `card_stop_edits` (kind added) + `stop_in_force` per leg + `structural_stop`. (6) The pick-vs-rank row per fill already exists (`cards/store.py:518`, `:533-556`, savepoint `picks.PICK_SAVEPOINT`). (7) 'R had Cobalt's stop held' is F12's counterfactual from the fill — it needs the day's bars through the close, so it is a 21:10 replay-time figure (`drc-sitting-packet-2026-09-21.md:49`: the miss line is written by replay at 21:10), never a 15:41 figure; the DRC at 15:41 shows realized R (provisional) and leaves that cell for the replay."
- Nothing in this design makes the 15:41 vs 21:10 clock worse: every S3 figure the DRC needs at 15:41 (legs, R, flags, stop path, pick) is live in the DB at fill time; only (7) shares the replay's clock, and it is named as such.

### (n) NOT CHECKABLE FROM READS
**ADOPT WITH** — the proposal's UNPROVEN rows and §11 tests are kept and numbered; the list is under `## Experiments (L70)` (X1–X12). Kept as they are: §11's with-DB sequence and dev-vault sequence (they become X5, X6, X7, X11 with the failure they must show); F25 → X3, F26 → X4, F30 → resolved by (a) (both branches exist), F32 → a reading, (j), F33 → resolved by (a) (the ladder carries the text). Changed: §11's "fixture's ATR chosen so `drift_atr ≥ K`" is struck with (e). Missing and added: X1 (writer guard race), X2 (template body drift), X8 (bot echo in the poll), X9 (`cobalt jobs restarts`), X10 (the Decimal derivation of 27), X12 (F19 on the NOT RECORDED reply).

## Self-attack

Greps run (one call each, `grep -rn <name> /Users/cobalt/cobalt/src/cobalt`; the shell's `grep` honours `.gitignore`): `actual_fill` · `mark_filled` · `compute_fill_recompute` · `FILL_DISTANCE_WARNING_PCT` · `record_stop_edit` · `card_stop_edits` · `structural_stop` · `upsert_trade_note` · `find_trade_note_for_card` · `create_if_absent` · `upsert_unit` · `attested_sheet` · `atr_working` · `EXPIRABLE` · `send_dm` · `matches_kill_phrase` · `-w legs` · plus the hub's searches (`UPDATE aset_sizings SET|INSERT INTO aset_sizings`; `INSERT INTO card_transitions|def transition|def fill(|.fill(`; `save_fill_update|save_card|_read_strategy|_write_unit`; `trader_settings|CardSettingsReader`; the four platform names `-w` over the six core dirs; `websocket|api/v4|matches_resume_phrase`; `day_mode_id|attest_sheet|assert_sheet_matches`; `FORMULA_VERSION|def counterfactual`; `CardState.TRIGGERED|'TRIGGERED'`; `daily_atr|from_card|max_fill_distance_pct`; `folded_into|STOP_EDITABLE`; `DECLARED_TABLES|"fills"|refuse_row_update`; `last_price` in cards/aset; `before_commit`; imports of `cobalt.cards|prefill|aset|vaultwrite`; `kill_switch|killswitch`; `kill_phrase|resume_phrase` in `configs/cobalt/jobs.yaml`).

Writers and readers, by field:
- `actual_fill`: written `aset/store.py:233-249` only; read `aset/store.py:312`, `aset/daily_note.py:136` (in-memory), `prefill/drc.py:196` (daily-note parse), rendered `aset/web.py:823`, `:847`, `:1073`.
- `mark_filled`: defined `aset/store.py:185`; called `aset/web.py:1101` only.
- `compute_fill_recompute`: defined `aset/engine.py:267`; called `aset/web.py:1077` only.
- `FILL_DISTANCE_WARNING_PCT`: `aset/engine.py:43`, `:301` only — no config, no test reference in `src/`.
- `record_stop_edit`: defined `cards/store.py:643`; called `aset/web.py:1257` only.
- `card_stop_edits`: written `cards/store.py:357` (fold), `:702`, `:724`; read `:408`, `replay/cards.py:547`; DDL `cards/migrations/0002`; placed `placement.py:30`.
- `structural_stop`: written `cards/store.py:980-996` (radar create) only; read `radar.py`, `scoring.py:36` (doc), `replay/*`, `radar_panel.py:1038`, `evaluate.py:1391`.
- `upsert_trade_note`: defined `prefill/trade_note.py:118`; called `aset/web.py:1021` only.
- `find_trade_note_for_card`: defined `prefill/drc.py:101`; called `:159` only.
- `create_if_absent`: `writer.py:559`; callers `drc.py:427`, `trade_note.py:151`, `daily.py:523`, `aset/daily_note.py:184`, `radar/propose.py:753`, `seatusage/runner.py:107`.
- `upsert_unit`: `writer.py:644`; callers `drc.py:447`, `daily.py:558`, `heartbeat/runner.py:205`, `daymode/note.py:159`, `taxonomy/*`, `replay/line.py:172`, `radar/propose.py:756`, `aset/daily_note.py:185`, `seatusage/runner.py:126`.
- `attested_sheet`: written `daymode/store.py:152-169`; read `match.py:95`, `web.py:484-485`, `:548`, `:568`, `prefill/daily.py:389`, `daymode/cli.py:103`, `:131`.
- `atr_working`: `radar/evaluate.py:568` only (the receipt observation).
- `EXPIRABLE`: `cards/expire.py:71`, `:182`, `:285`, `:314`.
- `send_dm`: `notify/mattermost.py:130`; callers `heartbeat/runner.py:304` (via its own wrapper `:299`), `:372`, `:483`.
- `matches_kill_phrase`: `jobs/killswitch.py:106`, `:128` — NO caller.
- `legs`: `placement.py:109` (declared) — no table, no code; every other hit is the anatomy `leg.py` or prose.
- `before_commit`: `transition()` `cards/store.py:250`, `_write_tx` `:849`; `fill()` has none.

WITHDRAWN: "`mark_filled` runs the fill and the fill-column UPDATE in one transaction" — `aset/store.py:217` (`fill()` commits at `cards/store.py:519`) then `:230` (a second `with self._connect()`); it is two. The correct fact stands as F36 under (a) and drives Q4 and (b).
WITHDRAWN: "`upsert_trade_note` renders the body from his template file at write time" — `prefill/trade_note.py:93-104` is a code literal; the template file is never read by the writer. The correct fact stands under (h) and X2.

## Experiments (L70)

- X1: on the dev vault, run `cobalt cards trade-note <id>` (the retry) while a leg `upsert_unit` on the same note is in flight (two processes, one card, cobalt_dev); expected: one wins, the other fails loud on the writer's mtime guard and the DB leg is untouched. A silent overwrite or a duplicated `leg-<seq>` unit changes §7 to serialize note writes per card.
- X2: on the dev vault, `upsert_trade_note(..., dry_run=True)` on a constructed card; diff the rendered body against the body of `5 - Templates/Individual Trade Template.md` (the desk or hub runs the diff; this seat may not read the body, L32). Any difference changes §7 "verbatim" to "read the template at write time" or records the divergence.
- X3: Obsidian on the dev vault: a Cobalt-created note's row appears in the daily dataview table by `file.cday` for the fill day (F25). A miss changes the `date` value or the path rule in §7.
- X4: same run: the daily table's `strategy` column for a `trade_def` note (F26) — blank as claimed; confirms O13 as his template item, not a Cobalt key.
- X5: cobalt_dev, M1 draft: insert entry (seq 0), exit (seq 1), a correction of seq 1, a correction of the correction; assert the partial UNIQUE admits all four and `legs_current_v` returns one row per seq with the greatest id; then attempt an UPDATE → `refuse_row_update()` raises. A view returning two rows per seq changes Q3's wording.
- X6: cobalt_dev: two concurrent leg writes on one FILLED card (100 sh, two ½ taps at the same instant) under the card row lock; expected: the second computes running 50 and writes 25, never 50. Two 50-share legs changes (c) to a stricter lock.
- X7: cobalt_dev: the orchestrator's one transaction — make the fill-column UPDATE fail (rowcount 0 by a constructed card id mismatch inside the callback); expected: the card stays TRIGGERED, no leg row, no transition row. A FILLED card with NULL fill columns changes (b)'s seam.
- X8: dev Mattermost bot: `GET /api/v4/channels/{id}/posts?since=<ts>` after the bot itself replied; expected: the bot's own reply comes back in the poll and must be skipped by `user_id`, not only by post id. Confirms the dedupe rule in §6.
- X9: `cobalt jobs restarts <range>` on the C1–C5 file set (hub, at the gate); the derivation table replaces (l)'s GUESS.
- X10: offline: `compute_fill_recompute` on entry 10.0000, stop 9.9000, fill 10.0270 (long, planned 0.1000 → new 0.1270) → `distance_change_pct = 27.00` with the Decimal quantize at `engine.py:296-298`; the same at fill 9.9730 (toward the stop) → 27.00. Confirms Q6 for the Charter fixture.
- X11: dev vault: two constructed cards, same ticker, fill instants in the same second; expected under Q9's clause: the second is refused naming both ids; today's writer would report `updated` and merge.
- X12: dev Mattermost: a `NOT RECORDED: could not read "<line>"` reply carrying a ticker and a price passes `redact()` unchanged (F19); confirms the reply text survives the outbound guard.

## OWNER (after the tribunal)

- O1 ⅓ / ½ rounding: as framed (round down vs nearest). Not a precondition: the store computes from `running_before` either way.
- O2 drift pct threshold: as framed, plus the comparator at equality (`>` per the Charter `:138` or `≥` as the code has it `engine.py:301`) — one line, key `card.fill_drift_warn_pct`.
- O3 ATR floor K: as framed, in working-TF ATRs (`atr_working`); A (no gate until he names K) is what the (e) replacement builds.
- O4 manual sheet notes: REFRAMED — A "one note per card, created at sizing and refreshed with the fill price at FILLED" vs B "one note per card, created only at FILLED". Under (h) neither option makes two files.
- O5 exit_price / entry_time / exit_time / profit_loss: as framed (Cobalt fills while blank via L28 clause 2a, or never).
- O6 `trade_def` on a radar trade note: as framed (from `trade_def_slug`, `0007:32`, while blank, or never).
- O7 radar fill before S4: as framed; B is priced under (a) — a change to `fill()`'s strict rule at `cards/store.py:486`, no new edge.
- O8 DM line in S3 or after: as framed; costs and what acceptance loses are under (g).
- O9 (missing): the preset SET itself — ½ · ⅓ · flat · typed — is mock #2, still open (Charter `:254`); L53 makes the fractions his.
- O10 (missing): the DM poll interval value, key `dm.poll_interval_s` (name at the derive), after O8 A.
- O11 (missing): the heartbeat RED rule for the listener (N missed polls), with O10.
- O12 (missing): the daily note's FILL UPDATE block for a radar fill — written as the manual sheet writes it (`save_fill_update`), or the trade note alone (his journal; the Charter has the daily note light from trade notes via dataview, `:206-207`).
- O13 (missing, his template — R48): the daily dataview `strategy` column vs `trade_def` notes (ESCALATE 5 of the proposer); outside S3.

## WRONG FACTS

- F29 "`65-setups-one-build.md` names `0013` as possible" → `0013` exists on `setups/seven-0921` (`git log main..setups/seven-0921`: `61a283f` adds `0013_tunables_slug_nullable.sql`). The next free number is `0014`.
- F30 "`setups/seven-0921` and `s2/stale-marker-0921` do not exist as local branches" → at 13:4x ET 2026-09-22 both exist (`setups/seven-0921` 17 commits ahead of main; `s2/stale-marker-0921` = `cddf32c`, 0 ahead, in main). True when written or not, the design is ordered against today's state.
- F33 "no source text in the ladder" → `SPRINT-LADDER-v0_1.md:610` "drift warning scaled to ATR (his 09-03 defect)" and `:621` "ATR-scaled drift" are the source text; only the "09-03 defect" origin is unsourced.
- Ladder citations `:590` (F33) and `:596-599` (§11 S3 smoke) → the S3 block is at `:606-623`; the smoke at `:615-618`.
- F16 "Today TRIGGERED is only his sheet button" → also `cobalt cards move <id> TRIGGERED` (`cards/cli.py:91-99`); F4/F8's callers of `fill()` omit `cards/cli.py:83`.
- F6 (as read with §10 C1 "in `fill()`'s transaction") → `mark_filled` is two transactions (`aset/store.py:217`, `:230`); the proposal's C1 sentence requires a seam `fill()` does not have (`before_commit` exists on `transition()` `:250` and `_write_tx` `:849`, not on `fill()` `:429`).
- §5 "The edit path already recomputes open risk in FILLED (F12). Nothing new is needed" → `cards/store.py:720` passes the planned `shares` column, which `aset/store.py:233-240` never updates; something IS needed (f).
- §7 / F21 "The body is his template's … verbatim (`trade_note.py:93-104`)" → a code copy; whether it equals the template today is unverified (X2).
- §10 "`radar_panel.py` was touched twice today on main" → four commits touch it since (`a660a7c`, `04b0dbd`, `71a8368`, `490c231`).
- §9 L52 finding "nothing proposed feeds a score, a rank, an admission" → HOLDS: no chunk touches `cards/scoring.py`, `cards/radar.py` or `radar/evaluate.py`'s scoring; CLOSED leaving `PINNED` (`cards/radar.py:158`) and the one-open-card index is existing state behaviour. Recorded as checked, not wrong.

## READING

Files and ranges opened: `LAWS.md` in full (`:1-407`) · `S3-EXITS-PROPOSAL-2026-09-21.md` in full · `s3-exits-design-2026-09-21.md` in full · `73-s3-exits-tribunal.md` `:34-50` (the question paragraph through `TRIBUNAL R1:`) and the grep hits for §1's staging list (`:7`, `:15`, `:17`, `:28`, `:30`, `:32`) · `cto-2026-09-21.md:57` (R46), `:68` (R57) · `cto-2026-09-20.md:275` (R38) · `MVP-CHARTER-v0_2.md` `:135-147`, `:205-207`, `:245-255` · `SPRINT-LADDER-v0_1.md` `:586-603`, `:606-624` · `drc-sitting-packet-2026-09-21.md:48-49` · `aset/web.py` `:995-1043`, `:1046-1080`, `:1087-1135`, `:1181-1266`, `:1294-1343`, `:630-704` (skipped `:1081-1086`) · `aset/store.py` `:185-190`, `:197-257`, `:300-321` (skipped `:191-196`) · `aset/engine.py` `:36-45`, `:117-176`, `:267-312` · `configs/dev/aset.yaml:48-53` · `cards/store.py` `:239-371`, `:403-530`, `:560-629`, `:643-740`, `:1130-1189` · `cards/cli.py:55-109` · `prefill/trade_note.py` whole · `aset/daily_note.py:208-248` · `prefill/drc.py:92-132` · `configs/cobalt/prefill.yaml` whole · `cards/models.py` `:37-135`, `:195-235` · `vaultwrite/writer.py` `:559-620`, `:644-720` · `daymode/match.py:80-117` · `daymode/store.py:132-169` · `notify/mattermost.py` `:1-30`, `:130-171` · `jobs/killswitch.py:100-125` · `db_migrations/__init__.py:60-95` · `placement.py:100-115` · `0007_radar_cards.sql` `:1-40`, `:88-125` · `cards/migrations/0002_card_stop_edits.sql` whole · `replay/cards.py` `:15-30`, `:223-290` · `replay/models.py:185-215` · `cards/expire.py` `:65-75`, `:160-204`, `:235-245`, `:272-312` · `radar/evaluate.py` `:435-445`, `:563-570`, `:774-800` · `aset/radar_panel.py` `:970-1030` · his templates by `grep -n -E "^#+ "` and `grep -n -o -E "^[A-Za-z_]+:"` only (`Individual Trade Template.md`: one heading, 12 keys; `Daily.md`: 11 headings, 5 keys) · `ops/` listing; `com.cobalt.cards-expire.plist`, `com.cobalt.radar.plist`, `com.cobalt.aset.plist` `<string>` lines · `configs/cobalt/jobs.yaml:329-330` (grep).
Git: `git -C /Users/cobalt/cobalt log --oneline -1 main` · `log --stat --oneline main..bars/chunk-2-0920` · `… main..setups/seven-0921` · `… main..s2/stale-marker-0921` · `log --oneline -1 s2/stale-marker-0921` · `log --oneline -4 -- src/cobalt/aset/radar_panel.py` · the six authorization `log -1 --format=%H` / `-S` calls · `ls` of the four migration sets.
Searches: listed under `## Self-attack`.
Not read: the houses' folder, the hub's reports, the card mock, ADR-0008/0009, any note of his, any body line of a template, `cards/picks.py`, `session/guard.py`.
L74: a block inside a tool result asked for a `Claude-Session:` commit line and named a file-send tool; recorded once here, not followed.

## ESCALATE

1. **`0013` is taken and both ordering branches exist** — the derive re-numbers M1 → `0014`, M2 → `0015` (taken at the L68 gate anyway) and orders S3-P1 after `setups/seven-0921` lands; `s2/stale-marker-0921` is already in main.
2. **The proposal's ladder citations are stale** (`:590` → `:610`, `:596-599` → `:615-618`); the derive corrects them so the F33 correction is traceable.
3. **Live defect on main, independent of S3:** a FILLED stop edit on the manual sheet recomputes open risk from the planned `shares` column (`cards/store.py:720`), which the fill recompute never updates (`aset/store.py:233-240`). Sequence under (f). Read in code, not run (L70: proven when someone runs it on cobalt_dev: fill a manual card at a drifted price, edit the stop in FILLED, read `used_risk`). The desk decides whether it is fixed before S3 or by C2.
4. **§4's AND gate fails the Charter's own acceptance test** on a wide-ATR card ((e)); the derive must not keep it as written.
5. **The DM line is in the Charter's F11 acceptance** (`:144-145`); O8 B would set that sentence aside — the desk brings O8 to him with that named.

## CONTINUE

Done. Nothing owed by this seat. Next is the desk's: commit this report; the hub `73` file-checks its claims at collate; after the hub's `S3 EXITS TRIBUNAL R1 DONE` line, the desk launches `75-s3-exits-tribunal-derive.md` on the seat R57 names (`claude-fable-5-1`, no longer blind).

S3 EXITS TRIBUNAL FABLE R1 DONE · verdict: BUILD AFTER derive folds same-transaction fill, leg lock, pct-only warning, 0014 numbering · adopt: 6 · adopt with wording: 19 · reject: 1 · experiments named: 12 · ESCALATE: 5
