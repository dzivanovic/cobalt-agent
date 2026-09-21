# Setups tribunal — derive v2 (Fable seat, second job) — 2026-09-21

Seat `setups-tribunal-derive-0921` · Fable 5.1 · prompt `docs/40 - DevDocs/prompts/2026-09-21/25-setups-tribunal-derive.md` · 15:00–15:3x EDT · two files written, nothing built, launched or committed.

## §0 Headline

- v2 written: `docs/30 - Design/SETUPS-AT-DEFAULTS-v2-2026-09-21.md` (the proposal whole, 21 folds tagged `[F-nn]`, no user data). Derived on three seats — Grok, Gemini, Fable; **astra did not rule, derived without it on R32.**
- 9 folds take a house's (or R24's) wording word for word; 17 first-gate experiments; 0 `REJECT` / `DO NOT BUILD` from any house.
- **The tribunal does NOT close: 4 items need round 2.** One of them (R2-2, how an assumed value is marked and degrades the score — `A-01` on the Rubberband card included) **gates C1** under L52 (a). My own round-1 "C1 unblocked" does not survive Grok's file-checked claims.
- Owner items 12, none a precondition (R15 / R17 held). ESCALATE 5 (two ASK DESK, safe defaults taken).

## DIGEST FOR THE DESK

**Seats, round 1:** Grok in full · Gemini in full (9 of its claims DO NOT HOLD, R1B hub) · Fable in full (blind; NO hub file-checked its claims) · astra NOT (METER, TIMEOUT). Counts are out of three.

**What v2 changed from the proposal, item by item:**
- O1 / (a): root cause and the C1 rule kept (3 seats). Unbound refusal → R2-1. `A-01` beyond rubberband → X10 before C4.
- O2 / (b): frame kept; the proposal's property test replaced by Grok's, word for word. Fable's additions → R2-4, X12.
- O3: token kept as a constant OUTSIDE `SetupRef` (Fable's words; Grok rules the same).
- O4 / (d) / (c)(a)(b): §7 not buildable — two seats show its recorder and its suppression path do not work as written; they offer opposite fixes → R2-2.
- O5 / (e): §8 not buildable — the real loader refuses the note as described (hub-noted + Fable); two different stores offered → R2-3.
- O6 / (g): seeded ATR is `atr_seeded`; `atr_working` keeps its meaning; one EMA9, `health` moves and the deploy says so (Fable's words; Grok names the same quantity).
- O7: rule kept (3 seats); "never forms under the literal reading" is unrun → X15; `legs()` untouched → X16.
- O8: `A-13` kept (3 seats); how it is marked → R2-2.
- (c): L52 re-answered — (a) NOT MET until R2-2, (c) partly, (b) and (d) hold. Closed `UnavailableReason` → X11.
- (f) + R24: Fable's five acceptance points taken whole; gates 1 and 4 re-worded by R24 — no fixture, gate day or lookalike from his log; expected values written by a checker house from the definition on the bars; his tagged ticker-days replay-and-look only.
- §2.3: the sentence "this guard alone would have turned … into a refusal" removed — wrong fact, two seats + hub.
- (h): C3 splits into C3a / C3b (Fable's words; Grok rules the same split). 8 chunks.
- (i): X1–X5 kept (X2 re-scoped by R24), X6–X17 added, each before the chunk it gates.

**Round 2 (why):** R2-1 Grok keeps / Fable removes the unbound refusal · R2-2 persisted suppression + recorder (Grok) vs tappable dot + static closure (Fable) — each says the other's fails · R2-3 two stores, each leaves the hole the other names · R2-4 a spec gap only one seat saw (what two frames publish).

**Owner items (after cards), one line each:** (1) the `A-01`…`A-23` values, read from the `--assumed` dry-run · (2) `A-01` orientation confirm · (3) `A-07`: value or taxonomy amendment · (4) `A-13`: proxy acceptable, or a tap later · (5) `A-05` seeding confirm · (6) the two note-versus-sheet divergences · (7) setup identity later as an engine dot under L7 shadow · (8) one ATR or two · (9) agreement stats from replay-and-look on his tagged ticker-days · (10) L11 `frontier` marks on six defs · (11) WATCH tie policy for score-less cards · (12) frame-property trade-off (Fable's `unmirror()` registry vs Grok's single property).

**Evenings under v2:** first card evening **1**; all seven evening **8** (was 7 — C3 split) — counted from the first evening after round 2 has answered R2-2 and C1 has passed its three checkers.

**Grok's four `BUILD AFTER` items:** atr name → settled (F-10) · hole-fill → R2-3 · assumed persist → R2-2 · scoped `A-01` → X10 + R2-1.

## How the single-seat clause (R32) was applied

R32: an item where only ONE seat's claim HOLDS against the hubs' file-check tables is never settled by the derive. The hubs checked Grok and Gemini only; no hub checked the Fable seat. Reading taken (stricter, ASK DESK 2): a fold is SETTLED only when its deciding FACT is a hub `HOLDS` row AND a second seat states the same fact (a Fable claim counts only when it is the same fact as a hub `HOLDS` row). A Grok-only `HOLDS` fact, or a Fable-only claim, goes to an experiment when a run can settle it and to round 2 when only reads can. My own check-reads this run (`vault_loader.py:318-366`, `:462-485`; `seam.py:44-55`, `:100`; `evaluate.py:584-596`; a `grep -c` of two notes) are marked "derive read" and are NOT hub checks (L35).

## Fold table

| F-nn | item | seats that ruled it | whose wording | adopted verbatim? | why (≤25 words) |
|---|---|---|---|---|---|
| F-01 | O1, (a) — root cause; C1 direction rule | 3 of 4 (Grok, Gemini, Fable) | proposal kept | not taken (Grok O1, Fable O1) | R1 rows 1, 2 and R1B row 1 HOLD; C1 effect identical under both pastes; each paste embeds what the other contests. |
| F-02 | O1 — `Direction(unbound)` refusal | 2 of 4 (Grok, Fable); Gemini silent | none | not taken | Grok keeps, Fable removes: a mechanism-correctness disagreement → R2-1. |
| F-03 | O1, (a), WRONG FACTS — `A-01` beyond rubberband; D4 direction | 3 of 4 | none | not taken | R1 row 30 HOLDS as a reading, row 7b UNVERIFIABLE; R1B row 2 DOES NOT HOLD; Fable's hold is single-seat → X10. |
| F-04 | O2, (b) — frame and acceptance property | 3 of 4 | Grok O2 | yes | R1 rows 8b, 9, 10 HOLD; R1B row 4 DOES NOT HOLD; Fable's property also maps long↔short; smaller mechanism. |
| F-05 | O2 — per-type `unmirror()`, published evaluation, observations once | 1 of 4 (Fable) | none | not taken | Single seat, no hub check → R2-4 and X12; its trade-off listed as owner item 12. |
| F-06 | (b) — non-equivalences | 3 of 4 | proposal kept + X4, X6 | not taken | R1 rows 8b–12 HOLD; rows 15 (R1), 5 (R1B) UNVERIFIABLE → experiments, never text. |
| F-07 | O3 — `unclassified` token | 3 of 4 | Fable O3 | yes | R1 row 16, R1B row 26 HOLD; Grok states the same rule ("must not" join `SetupRef`). |
| F-08 | O4, (d), (c)(a)(b) — assumed mark and score; `A-01` on the C1 card | 3 of 4 | none | not taken (Grok O4, Fable O4, Fable (d)) | Facts HOLD for two seats (R1 rows 17, 26; R1B rows 8, 9 DO NOT HOLD for Gemini); fixes conflict → R2-2. |
| F-09 | O5, (e) — the assumed store | 3 of 4 | none | not taken (Grok O5, Fable O5, Fable (e)) | R1 hub note `vault_loader.py:271-280` and row 18 HOLD; R1B row 17b DOES NOT HOLD; two stores, neither closes both holes → R2-3. |
| F-10 | O6 — ATR names, one EMA9 | 3 of 4 | Fable O6 | yes | R1 rows 20, 22 HOLD for Grok and Fable alike; Grok's paste rests on row 21 (DOES NOT HOLD); R1B row 6 DOES NOT HOLD. |
| F-11 | (g) — what moves | 3 of 4 | Fable (g) | yes | R1 row 22 and R1B row 7a HOLD; R1B row 7b UNVERIFIABLE → X14; X13, X16 beside it. |
| F-12 | O7 — `A-07` consolidation rule | 3 of 4 | Gemini O7 (= the proposal's own sentence) | yes | All three adopt; R1 row 32a HOLDS; rows 32b (R1), 18 (R1B) UNVERIFIABLE → X15; Fable's `legs()` clause single-seat → X16. |
| F-13 | O8 — `A-13` catalyst default | 3 of 4 | proposal kept | not taken (Fable O8) | R1 row 33, R1B rows 19, 20 HOLD; the marking mechanism is contested (atom field vs none) → R2-2. |
| F-14 | (c) L52 (c) — seams as artifacts | 3 of 4 | none | not taken (Grok (c) list, Fable (c)) | R1B row 10 DOES NOT HOLD; Grok's list names contested artifacts; Fable's closed-Literal claim single-seat → X11. |
| F-15 | (c) L52 (b), (d) | 3 of 4 | proposal kept | not taken (none offered) | R1B rows 11, 12, 13 HOLD; Grok (b), (d) ADOPT; the (b)-in-effect dispute rides with R2-2. |
| F-16 | (f) — acceptance points (1)–(5) | 3 of 4 | Fable (f) | yes | R1 rows 27, 28, 29 and R1B rows 21, 22 HOLD; R24 names this wording; point (5)'s effect single-seat → X17. |
| F-17 | WRONG FACTS — §2.3 "guard alone would have … refusal" | 2 of 4 (Grok WF1, Fable WF6); Gemini "None found" | sentence removed | no (a removal; no wording taken) | R1 rows 29, 10 HOLD; R1B row 25a: Gemini's "None found" DOES NOT HOLD. |
| F-18 | (h) — chunks | 3 of 4 | Fable (h) | yes | Grok rules the same C3a / C3b split; R1 row 34 HOLDS; Gemini claims nothing against it. |
| F-19 | (i) — experiments | 3 of 4 | each source's own text | yes | X1–X5 proposal; Grok X6, X8; Gemini X6; Fable X6–X9; hubs' unrun rows; Grok's "X7 settled" not taken (R1 row 25). |
| F-20 | WRONG FACTS — the rest | 2 of 4 claim any (Grok 3, Fable 6) | routed, none settled here | not taken | `atr_working` → F-10; same-side → F-03; loader → F-09; suppression path → F-08; closed models → F-13, F-14; nullable column: single-seat, decision unaffected. |
| F-21 | §9, §10, §11, X2 — OWNER RULING R24 | — (his) | R24 (`cto-2026-09-21.md:35`) | yes | Binding: no gate, test, `--expect-formed` day or lookalike from his log; checker-written values; replay-and-look only. |

Rows: 21. Marked `yes`: 9 — F-04, F-07, F-10, F-11, F-12, F-16, F-18, F-19, F-21.

## NEEDS ROUND 2

Four items. None is a `DO NOT BUILD`; R2-1, R2-2, R2-3 are two houses disagreeing on whether a mechanism is correct; R2-4 is a single-seat mechanism (R32 clause). Round 2 is asked only these.

### R2-1 — O1: is a `Direction(unbound)` refusal built? (gates: the registry check — proposal C1 row, C2's registry)

- **Grok (O1 paste):** "A def with no oriented object and no bindable `trade_direction` → `not_evaluable: Direction(unbound)`."
- **Fable (O1 paste):** "From C2 on, every long-written def is bound by the frame it forms on (§2.1); there is NO separate `Direction(unbound)` refusal." Its failing scenario: "`Hitchhiker.md:33-38` and `Second Chance Scalp.md:106-108` name neither an Extension nor `trade_direction`. §1's rule … makes both `not_evaluable: Direction(unbound)` after C3 / C7 — two of the seven never form. §2.1 already binds them by frame; the two mechanisms contradict."
- **Gemini:** silent. **Derive read (not a hub check):** `grep -c "trade_direction"` = 0 in both of those notes; R1 row 6's note says the three with-trend defs carry no unqualified Extension.
- **Question for round 2:** with the frame binding `trade_direction` on both sides, does any of the seven stay unbound — and if a refusal is kept, under which exact wording do `hitchhiker` and `second-chance` remain evaluable?

### R2-2 — O4 / (d) / (c)(a)(b) / O8: how an assumed value is marked on the card and degrades the score (gates: **C1** and C2)

Facts both seats hold, file-checked: the `cfg` recorder misses `_cfg_value` and `from_tunables` reads (R1 row 26); `suppression()` is dots-only and `refresh_card` recomputes it (R1 row 17); `A-01` is neither a `cfg` key nor a resolver (R1 hub ESCALATE 3).

- **Grok (O4 paste, whole):** "A formation that consulted any assumed `cfg` key or assumed resolver (A-01, A-05, A-13 included) sets `score_suppressed = assumed_formation` at create. That string is stored on the card row and is not overwritten by `refresh_card` from live tunables or from `suppression(dots)` (`cards-scoring.py:247-251`; `evaluate.py.part2:60-81`). `card_score` remains the only ranking authority (ADR-0009 D4). Null scores sink by the existing WATCH tie policy (`evaluate.py.part1:134-138`). Proximity stays computed from live entry/stop (same path as `trail_fit` N/A). C1 has no `assumed_keys` column yet: rubberband still sets `score_suppressed = assumed_formation` because A-01 is assumed. The chip and view column land in C2." — and (c)(a): "recorder that wraps every `resolve_cfg` / `_cfg_value` / `from_tunables` read, not only the interpreter `cfg`". — and O8: "Mark A-13 on the atom, chip on the card".
- **Fable (O4 paste, whole):** "A card whose definition's declared-key closure ((d)) contains any assumed key carries ONE extra dot: `factor: assumed_formation`, `source: cobalt-degraded`, `tier: deterministic`, `role: shadow`, `na_reason: ASSUMED`, `engine_inputs: {assumed_keys: [...]}`, appended by the evaluator after `compute_dots`. `NaReason` (`scoring.py:72`) gains `ASSUMED`. While untapped, the existing `suppression()` (`scoring.py:247-251`) suppresses the score; his tap lifts it and his grade enters conviction like any other tap. No `assumed_keys` view column, no migration, no change to `score_card`, no `FIELD_OWNERS` row. The panel may style that dot as the `ASSUMED · n` chip." — and (d): "`assumed_keys` is a STATIC closure, not a runtime recorder. Every atom resolver, detector, trigger resolver, stop resolver and relation resolver declares `tunable_keys` — the existing pattern at `extension.py:40-44`. A definition's closure is the union over everything its preconditions, avoids, trigger and stop name. `assumed_keys` = the keys in that closure whose resolved row has `source: assumed`. Every CONVENTION (`A-01`, `A-05`, `A-06`, `A-12`, `A-13`, `A-14`, `A-15`, `A-17`, `A-18`, `A-21`, `A-22`, `A-23`) is also a row: unit `label`, value = the name of the rule the code implements; the resolver reads it through the same rows and refuses (`not_evaluable`, named) a label it does not implement. One mechanism marks all 23." — and O8: "`A-13` serves `catalyst_ref` ONLY as a precondition atom of a definition. Extension path B keeps `catalyst_ref_unknown` (`extension.py:140-144`, `evaluate.py:620-622`) and is untouched. `AtomOutcome` gains no field: the resolver declares key `A-13` in its declared-key closure ((d)) and the mark reaches the card through the `assumed_formation` dot."
- **Each says the other's fails.** Grok, of a mark that can lift: "a hitchhiker card that formed on assumed A-02 would show a score. L52(a)/L57 hole." Fable, of a mark that never lifts: "every card is scoreless for life and WATCH orders by `pool_position` … That contradicts ADR-0009 D4". Gemini adopts the proposal; its two supporting claims DO NOT HOLD (R1B rows 8, 9).
- **Questions for round 2:** (1) permanent persisted suppression, or a tappable dot? (2) a runtime recorder around every read, or a static declared-key closure with the conventions stored as rows? (3) which chunk marks `A-01` on the Rubberband card, and with what — C1 has neither the column nor the closure; (4) can `A-13` be marked on the atom at all (`AtomOutcome` is `extra="forbid"`, `seam.py:100` — Fable WF5, derive read, no hub check)? (5) does the winner pass X8, and does WATCH stay ordered by `card_score`?

### R2-3 — O5 / (e): the assumed store (gates: C2)

Facts: the vault loader refuses a tunables row whose scope is not `per_trade(<slug>)` of its own note (`vault_loader.py:271-280`, R1 hub note; Fable WF1); hole-fill as proposed widens by scope (R1 row 18). Derive read, not a hub check: every `*.md` in the Strategies folder is read (`:476`) and a note without def frontmatter, `name:`, the definition section or its def unit raises (`:327-365`).

- **Grok (O5 paste, whole):** "Store: one vault note `1 - Trading/4 - Strategies/Assumed Defaults.md`, marker unit `tunables:assumed`, rows `source: assumed` (`TunableSource.ASSUMED`). Cobalt writes that unit with a new L28 command (create-if-absent, deterministic, versioned `vault_writes`, dry-run `cobalt taxonomy tunables --assumed`, proven on the dev vault first). The desk does not write unruled numbers (L65). R15 is the what (defaults assumed and marked), not a L73 override of L65. `merge_tunables` hole-fill: a user row may fill an engine row only when engine `value is null` AND user `source == assumed` AND user `scope ==` engine `scope` AND keys equal. Any other collision stays loud (`taxonomy-loader.py:90-112`). Engine null → non-null in the same load as dropping the assumed row, or the merge fails loud. Owner edit of the unit: human wins (L28). Open cards keep the `assumed_keys` they formed with."
- **Fable (O5 paste, whole):** "The assumed rows live in ONE vault note OUTSIDE `1 - Trading/4 - Strategies/` — `1 - Trading/Assumed Defaults.md`, beside the existing list-config note — in one marker-bounded unit `tunables:assumed`. A dedicated reader, `load_assumed_tunables(vault_root)`, validates the unit through `TunableRegistry`, accepts `global` and `per_trade(<slug>)` scopes, and requires `source ∈ {assumed, ruling}` on every row. `merge_tunables` gains hole-fill: a row from THAT reader may supply `value` and `source` for an engine row iff the engine row's committed `value is None` and the units match; key, unit and scope stay the engine's. Every other collision stays loud, including an assumed row meeting an engine row whose value is no longer null." — and (e): "A row stops being assumed only when its `source` reads `ruling`; an edited value with `source: assumed` keeps the mark. A ruled number for one of these keys NEVER moves into committed `tunables.yaml` (L32, L53): it stays in the note."
- **Gemini:** adopts the proposal's note and a desk write; "obeys L65 strictly" DOES NOT HOLD (R1B row 17b).
- **Why neither is taken:** Grok's note sits where the real loader refuses it; Fable's predicate keeps the engine's scope, which is the widening Grok's row 18 names.
- **Questions for round 2:** (1) where does the note live and which reader loads it, given `vault_loader.py:271-280`, `:327-365`? (2) one hole-fill predicate that closes BOTH holes — a strategy note's unit filling an engine hole (Fable) and a per-trade row filling a global key (Grok)? (3) is "assumed follows `source` only" (Fable (e)) the rule? — WHO writes the note is NOT asked of round 2: it is a law reading (ESCALATE 3).

### R2-4 — O2: what a two-frame evaluation publishes (gates: C2) — single seat

- **Fable (O2 paste, whole):** "Each observation, trigger outcome and stop outcome type declares `unmirror()`: prices and signed deltas are negated, magnitudes kept, `up↔down`, `high↔low`, `top↔base` and the level-label pairs swapped, `trade_direction` re-labelled. The Frame mirrors the daily series and the level set as well as the intraday bars. Resolvers return TYPED fields only; every human-readable `why` fragment is rendered after `unmirror()`, outside the frame. Factor observations and seam observations are computed ONCE on the real bars, never per frame. One evaluation is published per (member, def): the better of the two frames by `formed > avoided > input_stale > not_formed > not_evaluable`, ties to the long frame; the other frame's evaluation is kept in the receipt."
- **Grok:** its O2 paste (taken, F-04) negates PRICES before `Formation` / `RadarCardSpec` and says of labels only "the label is frame-local". **Gemini:** silent. No hub checked Fable's claims (`evaluate.py:593-596` — derive read: one `RadarScoreDetail` per evaluation).
- **Question for round 2:** when neither frame forms, which frame's evaluation does the one seam row publish; are factor and seam observations computed once on the real bars; is the daily series and level set mirrored with the bars? (The strings-and-labels half is X12, a run, not a round.)

## OWNER ITEMS (after cards)

Deduplicated. None is a precondition to any chunk; no house wrote one as a precondition.

| # | item | raised by |
|---|---|---|
| 1 | The `A-01`…`A-23` values, the LOW-confidence ones first, read from the `--assumed` dry-run with the cards they formed | Grok, Fable |
| 2 | `A-01`: confirm the orientation rule. (Gemini's wording of this item carries "all 7 setups trade against immediate Extension" — DOES NOT HOLD, R1B row 2; Fable's: the three reversion setups) | Gemini, Fable |
| 3 | `A-07`: an assumed value, or an amendment of `TAXONOMY-DRAFT-v0_7.md:94` | Grok, Gemini, Fable, proposal ESCALATE 2 |
| 4 | `A-13`: is radar admission an acceptable stand-in for the catalyst gate, or a tap later | Grok, Gemini, Fable |
| 5 | `A-05`: confirm premarket seeding for the early-window indicators | Gemini |
| 6 | The two note-versus-sheet divergences (`Fashionably Late.md:47-51`; `VWAP Continuation.md:81`): keep the note's reading or the sheet's | Grok, Fable, proposal ESCALATE 3 |
| 7 | Whether setup identity later becomes an engine `setup_relation` dot under L7 shadow | Grok |
| 8 | One ATR or two; whether to collapse to one after a Rubberband shadow | Grok |
| 9 | His tagged ticker-days: replay-and-look, agreement stats read by him after cards show — never a fixture or a gate (re-scoped by R24 from Grok's "fixture/replay days from his tagged trades") | Grok, R24 |
| 10 | L11: explicit `frontier` marks on the six defs that do not carry one (a note edit, L65) | Grok, Fable |
| 11 | The tie policy that orders WATCH cards whose score is suppressed | Gemini |
| 12 | Frame-property trade-off (prefer-simpler rule): Fable's per-type `unmirror()` + registry-driven property costs one declaration per observation type and buys label / string un-mirroring and a suite that fails on an unregistered detector; v2 took Grok's single pipeline property | derive, from Fable (b) vs Grok O2 |

## Redactions

Count: **0** spans redacted by the derive. No house proposed a VALUE for an assumed key in round 1, so there is no `A-nn: value change proposed by …` pointer. The spans the hubs redacted (7 in R1 — Grok's (a) table cells and one scenario clause; 2 in R1B — the hub's own rows) are not re-quoted in either file; where Grok's backside scenario is needed (X10) the hub's own words are used ("a backside fixture with last > open"). Both files cite his notes by `file:line` and assumed values by KEY only. `grep` of v2 for every ticker and money figure in `docs/_inflight/trading-stats-2026-09-21.md`: 0 hits.

## READING

- Prompt `25-setups-tribunal-derive.md` full · `22-draft-setups-tribunal.md` by `grep -c` only (10 strings, each 1).
- `cto-2026-09-21.md` rows `:31` (R20), `:35` (R24), `:43` (R32).
- `LAWS.md:1-405` (full).
- Hub reports, full: `setups-tribunal-2026-09-21.md`, `setups-tribunal-r1b-2026-09-21.md`.
- Raw rulings, full: `r1/grok-ruling.md`, `r1/gemini-ruling.md` (no `astra-ruling*.md` exists) · own round 1: `setups-tribunal-fable-r1-2026-09-21.md` full.
- The proposal full · `setups-design-2026-09-21.md` full.
- `docs/_inflight/trading-stats-2026-09-21.md` full (USER DATA, read for R24, nothing copied).
- Check-reads (index card 4): `taxonomy/vault_loader.py:318-366`, `:462-485` + a grep of its raise sites · `radar/seam.py:44-55` + grep (`:100`, `:117`) · `radar/evaluate.py:584-599` · `grep -c "trade_direction"` on four strategy notes (counts only).
- Not opened: the companion `setups-assumed-values-2026-09-21.md`, the gap table, the cheat-sheet PDFs, `0007_radar_cards.sql` — no fold turned on them.

## ESCALATE

1. **C1 is not unblocked by this derive.** R2-2 gates it: as the proposal stands the Rubberband card's direction, trigger and stop rest on `A-01`, an assumed convention, unmarked and scored — L52 (a), raised by both hubs (R1 ESCALATE 3, R1B ESCALATE 3) and by two seats. Everything else in C1 is settled (direction rule, token, §9 gates under R24). Owner: desk — whether round 2 runs on R2-2 alone first (L72) is its call; `grok` / `agy` approval ends 2026-09-21 23:59 ET.
2. **Production (NN#16): nobody writes `Assumed Defaults.md` into `1 - Trading/4 - Strategies/` before a reader that accepts it is deployed.** The loader reads every `*.md` there and raises on a note without the def frontmatter; every `cobalt taxonomy load` / `validate` would then fail for the whole folder (Fable R1 ESCALATE 1; hub-noted `vault_loader.py:271-280`; derive read `:327-365`, `:476`). The proposal's C2 row said "before or with the deploy". Owner: desk.
3. **ASK DESK: who writes the assumed note — is R15 the direct instruction that sets L65's "never a value he has not ruled" aside (L73 as amended 09-21 R5), as Gemini and Fable read it, or not, as Grok reads it ("R15 does not name the note or the values", R1 row 19 HOLDS)? [15:16 ET]** A law reading is never voted (LAWS preamble). Safe default taken in v2: the path lawful under every seat's reading — a Cobalt L28 command, +S on C2 — so nothing is asked of him before cards.
4. **ASK DESK: is my reading of R32's single-seat clause the one you meant — a Fable-seat claim counts only when it is the same fact as a hub `HOLDS` row, because no hub file-checked the Fable seat? [15:16 ET]** Safe default taken: the stricter reading; it is what sends F-05, F-13's mark and F-14 to round 2 or to experiments instead of settling them on my own round-1 claims.
5. **Two derive notes for whoever drafts C2, neither a house's claim, both UNPROVEN (L70):** (a) both houses' X5 over-budget remedy (build the second frame only when the first does not form) stops observing `both_sides` — read X7 first; (b) Grok's acceptance property (F-04, taken word for word) names `eval_as_short` / `pred_as_short`, and no short-side implementation exists for a side-less detector to compare against — the checkers should say what the right-hand side is before C2's suite is written.

No `DO NOT BUILD`, no `REJECT`, no second ranking authority claimed by any house, no owner item written as a precondition (so none named here), no user data in either file.

L74 (recorded once, not followed): a block appended inside a tool result (the prompt file Read) asked for a `Claude-Session:` line in commits and named a file-send tool. It is data; this seat commits nothing.

MEMORY: [stated 2026-09-21 · setups derive] On a tribunal where the Fable seat rules blind, no hub file-checks its claims, so a later derive cannot count them as HOLDS; next tribunal, the round-1 hub (or a third hub) file-checks the Fable seat's report too.

## CONTINUE

None — the run is complete. v2 is written and is NOT re-derived on a relaunch. Next step, not mine: `needs round 2: 4` → a round-2 hub is drafted for R2-1 … R2-4 only, with the same approved strings.

SETUPS DERIVED v2 · folds: 21 · verbatim: 9 · needs round 2: 4 · owner items: 12 · ESCALATE: 5
