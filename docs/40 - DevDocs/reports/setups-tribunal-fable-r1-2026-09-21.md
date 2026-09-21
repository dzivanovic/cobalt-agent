BLIND: I did not read the houses' folder or the hub's report.

# Setups tribunal — Fable seat, round 1 (2026-09-21)

Seat `setups-tribunal-fable-0921` · Fable 5.1 · read-only, one file written (this one). Design ruled on: `docs/30 - Design/SETUPS-AT-DEFAULTS-PROPOSAL-2026-09-21.md` (Opus 5). Authorization verified before any reading: R20 row `cto-2026-09-21.md:31` carries both required strings; R20 wording committed at `30ae6c9`; proposal committed at `652434e`; all seven allow strings and three deny strings count 1 in `22-draft-setups-tribunal.md`. L32: this file cites his notes by `note:line`, the companion by KEY, and carries no value, quote or wording from them.

## DIGEST FOR THE DESK

TRIBUNAL R1: BUILD AFTER the derive folds the O4, O5, (d) and seam-reason replacements; C1 unblocked

Every objection below came from opening the file the proposal cites; none is a preference. Six proposal statements are contradicted by the code (## WRONG FACTS).

| item | verdict | gist |
|---|---|---|
| O1 direction from anatomy | ADOPT WITH | Right for all seven. Drop the "unbound" refusal (it would refuse hitchhiker and second-chance); hold the Extension's direction from its culminating bar in D4. |
| O2 mirrored frame | ADOPT WITH | Sound. Every observation type declares how it un-mirrors; `why` text is rendered after un-mirroring; daily series and levels are mirrored too. |
| O3 `unclassified` token | ADOPT WITH | Keep the token, as a constant outside the `SetupRef` enum. The "nullable needs a migration" reason is wrong. |
| O4 score suppressed when assumed | ADOPT WITH | Replace permanent suppression with one tappable `assumed_formation` dot: no new column, no migration, no `score_card` change. |
| O5 one vault note + hole-fill | ADOPT WITH | The note as described is REFUSED by the real loader. Move it out of the Strategies folder, give it its own small reader. |
| O6 seeded EMA/ATR beside RTH ATR | ADOPT WITH | `atr_working` is already a published name for the RTH ATR. New one is `atr_seeded`. One EMA9, and say `health` moves. |
| O7 drive ends by consolidation (`A-07`) | ADOPT WITH | Adopt the rule; `legs()` stays byte-identical so Rubberband's `leg_count` does not move. |
| O8 9-EMA catalyst via admission (`A-13`) | ADOPT WITH | Adopt; scope it to the def's precondition, leave Extension path B alone, add no field to `AtomOutcome`. |
| (a) direction root cause | ADOPT | The reading is right; no card lands on a side its def does not list. |
| (b) mirror non-equivalences | ADOPT WITH | No arithmetic break found; the breaks are labels, positive-price validators and strings. Property test must be registry-driven. |
| (c) L52 (a)–(d) | ADOPT WITH | The seam schema DOES change (closed `UnavailableReason`); (b) holds only with the O4 dot. |
| (d) assumed visibility | ADOPT WITH | A recorder on `cfg()` misses every detector-consumed row and all 12 conventions. Use a static declared-key closure. |
| (e) the store | ADOPT WITH | Desk writes the note under R15 (L73 record), AFTER the reader ships. Hole-fill guarded on `value is None` and `source: assumed`. |
| (f) acceptance | ADOPT WITH | Gates 1–4 catch the miss. Expected values written by a checker house, skipped = red, no known day = red, guard also checks last price. |
| (g) warm-up | ADOPT WITH | Two numbers move that the proposal says do not: the `atr_working` name and the card's `health`. |
| (h) chunks and experiments | ADOPT WITH | C1 is S logic + M gates and needs nothing from C2. Split C3. X5 re-run at every chunk. Latency UNVERIFIED. |
| (i) not checkable from reads | ADOPT WITH | X1–X5 kept and sharpened; X6–X9 added. |

Experiments named: 9 (X1–X9). Owner items (after cards): 6. ESCALATE: 2 — (1) the desk must NOT write `Assumed Defaults.md` into the Strategies folder before C2's reader deploys: it breaks every vault→DB definition load; (2) ASK DESK on the R15 reading.

Counts: adopt 1 · adopt with wording 16 · reject 0.

## Rulings

### O1 — direction from anatomy (`A-01`), not a setup classifier
**ADOPT WITH:** "Direction comes from the trade's own anatomy; `relation` is never read for direction. C1: `trade_direction = against ext.direction` for a def whose precondition anchor is an unqualified Extension; any other def stays `not_evaluable` as today. From C2 on, every long-written def is bound by the frame it forms on (§2.1); there is NO separate `Direction(unbound)` refusal. In D4 the Extension's direction is stamped at its culminating bar and held through `reverting` / `backside`; it is never recomputed from `last_close − session_open`."
- The root-cause reading holds: `evaluate.py:635-645` is the only reader of `relation`; taxonomy `:136` puts `relation` on the setup entry and `:137`, `:124`, `:75` compute instance direction separately.
- No wrong-side card: all three reversion defs list an intraday-overextension countertrend entry (`Rubberband.md:40`, `Backside Scalp.md:93`, `Fashionably Late.md:35`), and a culminating Extension IS that setup, so every against-the-Extension trade is covered by a listed pair whatever the day context.
- Failing scenario 1 (the unbound refusal): `Hitchhiker.md:33-38` and `Second Chance Scalp.md:106-108` name neither an Extension nor `trade_direction`. §1's rule ("names neither an oriented object nor `trade_direction`" → refused) makes both `not_evaluable: Direction(unbound)` after C3 / C7 — two of the seven never form. §2.1 already binds them by frame; the two mechanisms contradict.
- Failing scenario 2 (D4): name opens, flushes, culminates down, reverts and closes back above its open at a later scan. `extension.py:96-103` then reports direction `up`; the down-Extension the backside def trades against no longer exists at exactly the moment its state should read `backside`. Cost of the fix: none beyond D4 itself (one stored field).

### O2 — mirrored frame for side binding
**ADOPT WITH:** "Each observation, trigger outcome and stop outcome type declares `unmirror()`: prices and signed deltas are negated, magnitudes kept, `up↔down`, `high↔low`, `top↔base` and the level-label pairs swapped, `trade_direction` re-labelled. The Frame mirrors the daily series and the level set as well as the intraday bars. Resolvers return TYPED fields only; every human-readable `why` fragment is rendered after `unmirror()`, outside the frame. Factor observations and seam observations are computed ONCE on the real bars, never per frame. One evaluation is published per (member, def): the better of the two frames by `formed > avoided > input_stale > not_formed > not_evaluable`, ties to the long frame; the other frame's evaluation is kept in the receipt."
- The mirror is the smaller mechanism and I keep it: a long/short branch per detector is what today's defect looked like.
- Failing scenario (card field `why`): `structure.py:49-67` outcomes carry `trade_direction` plus four Decimal prices, and `evaluate.py:674-680` builds `why` from them. A resolver that composes its `why` inside the mirrored frame writes a negative trigger and stop and the word `long` onto a short card. `cards/radar.py:86,88` (`gt=0`) catches only the two typed prices, not the string, `extreme`, `raw`, `rounded` or `inputs`.
- Failing scenario (board row): hitchhiker, down drive into a lower-third consolidation at an early scan — long frame `not_formed`, mirrored frame `formed`. §2 never says which of the two the single seam row (`evaluate.py:593-596`) publishes when neither forms.
- `htf_range_break` (`daily.py:171-195`) is symmetric only if the daily series is mirrored with it; the proposal mirrors "the stored bars" only.
- Cost: the `unmirror()` declarations are what the proposal's property test needs anyway (mirror(detector(bars)) must be defined per type). No extra file.

### O3 — `setup_ref = unclassified` token
**ADOPT WITH:** "`UNCLASSIFIED_SETUP = "unclassified"` is a module constant in `evaluate.py`; it is NOT a member of the `SetupRef` enum, so no definition can list it in `valid_setups`."
- The token is more honest on the card face than a blank: the panel renders a null as an empty string (`radar_panel.py:735`).
- The proposal's stated reason is wrong (## WRONG FACTS 3): the column is already nullable (`0007_radar_cards.sql:34`) and the row model already `str | None` (`radar_panel.py:216`). The choice rests on honesty, not on cost.
- Failing scenario the wording closes: "validated" read as "add it to `SetupRef`" lets a note declare a setup named `unclassified`, and the card can no longer tell a detection from its absence.

### O4 — score suppressed on any assumed formation
**ADOPT WITH:** "A card whose definition's declared-key closure ((d)) contains any assumed key carries ONE extra dot: `factor: assumed_formation`, `source: cobalt-degraded`, `tier: deterministic`, `role: shadow`, `na_reason: ASSUMED`, `engine_inputs: {assumed_keys: [...]}`, appended by the evaluator after `compute_dots`. `NaReason` (`scoring.py:72`) gains `ASSUMED`. While untapped, the existing `suppression()` (`scoring.py:247-251`) suppresses the score; his tap lifts it and his grade enters conviction like any other tap. No `assumed_keys` view column, no migration, no change to `score_card`, no `FIELD_OWNERS` row. The panel may style that dot as the `ASSUMED · n` chip."
- Walked through the code: `Dot.computed` (`scoring.py:109-111`) is True for that dot, so `suppression()` lists it with "(tap to grade)"; `card_dots.na_reason` is free `TEXT` (`0007_radar_cards.sql:132`); `refresh_dots` (`scoring.py:201-224`) adds an unseen factor once.
- The proposal's path does not exist as described (## WRONG FACTS 2): `suppression()` is a function of dots only. `assumed_formation` needs a new `score_card` input, which contradicts "changes nothing in `card_score`".
- Failing scenario (ladder order): every one of the seven carries ≥1 assumed key (companion, per-setup table; rubberband carries `A-01` alone). As written the suppression never lifts, so every card is scoreless for life and WATCH orders by `pool_position` (`evaluate.py:134-138`). Two WATCH cards at one scan: one a cent from its trigger with all his dots tapped high, pool position low; one far from its trigger, tapped low, pool position high. The second ranks first. That contradicts ADR-0009 D4 ("pool `last_rank` only admits").
- L52(a) "degrades the score accordingly": suppressed until he has looked, then weighted by his own grade of the assumed formation. No invented penalty number. A per-card tap is a hand input, not a ruling on a setup (R17 intact).
- Smaller than the proposal: removes the view column, its migration, the badge row and the `score_card` change from C2.

### O5 — one vault note for assumed values, hole-fill merge rule
**ADOPT WITH:** "The assumed rows live in ONE vault note OUTSIDE `1 - Trading/4 - Strategies/` — `1 - Trading/Assumed Defaults.md`, beside the existing list-config note — in one marker-bounded unit `tunables:assumed`. A dedicated reader, `load_assumed_tunables(vault_root)`, validates the unit through `TunableRegistry`, accepts `global` and `per_trade(<slug>)` scopes, and requires `source ∈ {assumed, ruling}` on every row. `merge_tunables` gains hole-fill: a row from THAT reader may supply `value` and `source` for an engine row iff the engine row's committed `value is None` and the units match; key, unit and scope stay the engine's. Every other collision stays loud, including an assumed row meeting an engine row whose value is no longer null."
- The note as §8 describes it is refused by the loader (## WRONG FACTS 1): `load_vault_trade_defs` reads every `*.md` in the Strategies folder (`vault_loader.py:476`) and RAISES on a note without `trade_def:` frontmatter, `name:`, the definition section or its `trade_def:<slug>` unit (`:327-365`). A draft is an EMPTY def unit, not a missing one (`:380-392`). `_read_tunables_unit` refuses every row whose scope is not `per_trade(<that note's slug>)` (`:271-280`) — so every `global` row and every row for another setup is refused.
- Failing scenario: the desk writes the note as described "before the deploy" (C2 row). The next `cobalt taxonomy load` / `validate` (`taxonomy/cli.py:78`, `:304`; `validate.py:93`) raises for the whole folder. The running radar survives on its DB copy (`radar/runner.py:428`), but no definition edit reaches production until the note is removed.
- Widening: the two guards (`value is None`, rows only from the assumed reader) are what keep `loader.py:93-111`'s "never shadow an engine key" intact. A per-trade unit in a strategy note can never hole-fill.
- Cost, priced: one reader (~40 lines) + tests in `taxonomy/vault_loader.py`, the hole-fill branch in `taxonomy/loader.py`, `TunableSource.ASSUMED` (`tunables.py:63-66`). Adds S to C2 — paid back by O4 removing the column and migration.

### O6 — premarket-seeded EMA/ATR beside the Extension's RTH ATR
**ADOPT WITH:** "The Extension's RTH-run ATR KEEPS the name `atr_working` (it is already published under that name). The premarket-seeded ATR is a new quantity named `atr_seeded`. Both are `wilder_atr` over different series: one function, two named inputs. EMA9 and EMA21 have ONE definition each — seeded, falling back to RTH-only when the seed is short — and `MemberEvaluation.ema9` takes that value. The chunk that lands this states in its deploy notes that the `health` of open cards moves, and bumps `EVALUATOR_VERSION`."
- ## WRONG FACTS 4: `evaluate.py:568` already emits a seam observation named `atr_working` whose value is `ext.atr`, the RTH-run ATR. §5 gives that name to the seeded ATR and renames the old one `atr_run`: the same published name would change meaning between two evaluator versions, and an audit bundle diff across the deploy reads as a moved ATR.
- "Two quantities, not two paths" is true for ATR once the names do not collide. It is NOT true for EMA9 unless there is one: `evaluate.py:560-564` computes an RTH-only EMA9 that feeds `card_health` (`:791-794`). Keeping it beside a seeded EMA9 is two implementations of one indicator (L3).
- Whether the seed helps or hurts early tolerances is X6, not argued here.

### O7 — opening-drive termination by consolidation (`A-07`)
**ADOPT WITH:** "`leg.legs()` (`leg.py:42-67`) is unchanged, byte-identical. Roles and `terminated_by` are a separate function over its output plus the Range(micro) observation."
- Taxonomy `:94` names two terminators, so SOME rule must classify; read literally (first opposing bar) the precondition at `Hitchhiker.md:35` is almost never true and the avoid at `:68` almost always is. A marked assumption is the right home; the owner sees it after cards.
- Failing scenario the wording closes: D3 implemented by teaching `legs()` to absorb opposing bars inside a consolidation changes `Extension.leg_count` (`extension.py:120`, `evaluate.py:458-462`) — a Rubberband dot input moves with no shadow run.

### O8 — 9-EMA catalyst via in-play admission (`A-13`)
**ADOPT WITH:** "`A-13` serves `catalyst_ref` ONLY as a precondition atom of a definition. Extension path B keeps `catalyst_ref_unknown` (`extension.py:140-144`, `evaluate.py:620-622`) and is untouched. `AtomOutcome` gains no field: the resolver declares key `A-13` in its declared-key closure ((d)) and the mark reaches the card through the `assumed_formation` dot."
- A tap gate contradicts R17; with no catalyst data this is the only reading that lets the card show. It makes the precondition at `9 EMA Scalp.md:44` a tautology of the one at `:43` — honest only because it is marked, and with O4 the card is scoreless until he has looked at it.
- ## WRONG FACTS 5: §6 stores the outcome with `assumed=A-13`; `AtomOutcome` is a closed model (`seam.py:99-117`, `extra="forbid"`) and the L52 table says the seam schema is unchanged.
- Failing scenario the scoping closes: one ticker, one scan — the Rubberband board row says catalyst unknown (path B only) while the 9-EMA row says catalyst present. Left unscoped, a builder "unifies" the two readings and changes path B behaviour inside a chunk that was only meant to unlock 9-EMA.

### (a) DIRECTION
**ADOPT**
- Root cause confirmed against the code, not the report: the gate at `evaluate.py:635-645` reads a setup-context field as the trade's relation to the intraday Extension; the label at `:646-647` depends on list order. The proof test pins it (`test_rubberband_card_proof.py:179-217`: 71 of 71).
- Every one of the seven: the four continuation/opening defs list only with-trend entries (`Hitchhiker.md:28-30`, `Second Chance Scalp.md:101-103`, `9 EMA Scalp.md:37-39`, `VWAP Continuation.md:34-36`) and bind their side from their own legs; the three reversion defs resolve to one side per Extension (O1). No note carries setups that resolve to two sides for one instance.
- `against ext.direction`: no wrong-side card today because the detector has exactly one direction per scan (`extension.py:96-103`). The D4 hold in O1 keeps that true when lifecycle states arrive.
- `unclassified` is honest on the face: nothing in `src/cobalt/radar` detects a setup, and his `setup_relation` tap (`Rubberband.md:101`) carries the read.
- One thing C1 makes live for the first time, as an experiment not a defect (L70): `culminating` is sticky — the latest qualifying bar stays the culmination for the rest of the day (`extension.py:123-139`). X3 must report the age of the culminating bar at each formation.

### (b) THE MIRRORED FRAME
**ADOPT WITH:** "The property test is REGISTRY-DRIVEN: it iterates every registered detector, trigger resolver, stop resolver and level source and asserts `unmirror(f(mirror(x))) == f(x)` on the committed real-shape days; a registered item with no `unmirror()` fails the suite. It includes `structural_stop` swept across the cent grid (round dollars, x.x0, sub-cent extremes) on both sides."
Where price → −price is not a plain equivalence, with what happens:
- `cards/radar.py:86,88` (`trigger_price`, `structural_stop` `gt=0`) and `:106-111`: an un-negated price is refused loudly at card creation. A backstop, not a break — but it crashes the card path rather than refusing the formation, so un-mirroring belongs before `Formation`.
- `structure.py:100-116`: the stop law is already side-aware. Called as `long` on a negated extreme it floors a negative, which is the ceiling the real short wants; the ten-cent test (`:96-97`) and the toward/away branch (`:108-112`) are sign-symmetric by the same algebra. That last step rests on Python `Decimal` remainder and negative-zero behaviour — X4, not argued.
- Labels, not arithmetic: `TrackedExtreme.side` (`structure.py:44`), `HtfProximity.reference` (`daily.py:147-149`), `HtfRangeBreak.direction` (`daily.py:161`), `ExtensionObservation.direction`, every PMH/PML and PDH/PDL pair, `top`/`base`. Each needs its swap (O2).
- Symmetric, checked: true range and ATR (`indicators.py:86-94`, absolute values), the Extension's distance (`extension.py:115`, `abs`) and body test (`bars.py:57-59`), VWAP (linear in price), the day-range third (linear), wick share (a magnitude), volume-with-direction (`extension.py:126-130`, both flip together), Decimal context rounding (half-even is sign-symmetric). `A-11`'s normaliser is a magnitude per its companion row, so a normalised slope flips sign correctly.
- No validator requires a positive price on `WorkingBar`, `Bar` or `DailyBar` (grep: only `volume` and `minutes` carry bounds, `bars.py:43-50`, `daily.py:53`).
- Is the property test enough? For arithmetic, yes. It cannot see strings (O2) or a detector nobody registered — hence registry-driven.

### (c) L52 (a)–(d)
**ADOPT WITH:** in the L52 table — "(b) `card_score` remains the one ranking authority because the assumed mark is a tappable dot (O4), never a permanent suppression. (c) the seam schema CHANGES and is versioned: `seam.UnavailableReason` gains every reason a new resolver can emit, in the chunk that introduces it; each resolver declares its reasons beside its value domain; a committed test constructs an `AtomOutcome` for every (registered atom name, declared reason) pair and asserts none collapses to `unspecified_atom`."
- (a) Numbers reaching a card unmarked as the proposal stands: every value produced under one of the 12 convention keys, and every detector-consumed row ((d)). Trigger, stop, `proximity` and — after his key tap — `shares` derive from assumed values and are marked only at card level; with the dot that is visible where he grades, which I accept.
- (b) As written, fails in effect: all cards scoreless → `pool_position` orders WATCH (O4's scenario). With the dot, holds. Formation, side binding and the both-sides refusal add no rank.
- (c) Failing scenario: `UnavailableReason` is a closed Literal (`seam.py:48-55`). §5's new reason `insufficient_seed` — or any new detector reason — reaches `AtomOutcome(... unavailable=...)` at `evaluate.py:588` and raises a validation error inside `detail()`: the evaluate run fails for the whole pool, every scan, until the indicator warms. The table's "unchanged schema" is wrong on its face.
- (d) Holds once (c) holds: an atom that collapsed to `unspecified_atom` would leave the audit bundle unable to say which atom held which value. The committed test above closes it.

### (d) ASSUMED VISIBILITY
**ADOPT WITH:** "`assumed_keys` is a STATIC closure, not a runtime recorder. Every atom resolver, detector, trigger resolver, stop resolver and relation resolver declares `tunable_keys` — the existing pattern at `extension.py:40-44`. A definition's closure is the union over everything its preconditions, avoids, trigger and stop name. `assumed_keys` = the keys in that closure whose resolved row has `source: assumed`. Every CONVENTION (`A-01`, `A-05`, `A-06`, `A-12`, `A-13`, `A-14`, `A-15`, `A-17`, `A-18`, `A-21`, `A-22`, `A-23`) is also a row: unit `label`, value = the name of the rule the code implements; the resolver reads it through the same rows and refuses (`not_evaluable`, named) a label it does not implement. One mechanism marks all 23."
- Failing scenario (the recorder): detectors do not read through the interpreter's `cfg` callable. `evaluate.py:528` builds `ExtensionParams.from_tunables(tunables)` straight from the rows; the recorder sits on `:601-602`. A Range detector built the same way consumes `A-03` and `A-04` unseen. A hitchhiker card then forms whose only `cfg()` call in a precondition is the note's own duration band (`Hitchhiker.md:37`, not assumed): its `assumed_keys` omits `A-03`, `A-04`, `A-07` — the chip under-reports on exactly the values with the lowest confidence.
- Derivation of "12 conventions": the companion's name column marks 12 keys as conventions and 11 as rows (`A-02`, `A-03`, `A-04`, `A-07`, `A-08`, `A-09`, `A-10`, `A-11`, `A-16`, `A-19`, `A-20`); 12 + 11 = 23. §7–§8 give a convention no row, so nothing can ever change its `source` to `ruling`: "how a value stops being assumed" has no answer for more than half the keys.
- A static closure over-reports (a short-circuited branch still counts). That is the safe direction, and it is the same set the `--assumed` dry-run needs for its consumers column. Smaller than the recorder: no threading a recorder through every detector call.
- Size / refresh: `shares` follow the stop distance after his key tap; `proposed_key` is computed regardless of suppression (`scoring.py:332`). The dot sits on the same card he sizes from. It is recomputed each scan like every other dot; the creation receipt holds the keys the card formed with (L57).

### (e) THE STORE
**ADOPT WITH:** the O5 wording, plus — "The note is written by the CTO desk, once, under R15, AFTER C2's reader is deployed, never before. The desk records in the day's report one line: L65's 'never a value he has not ruled' is set aside for this note by R15 (L73 as amended 2026-09-21, `09-21 R5`), with his words and the time. A row stops being assumed only when its `source` reads `ruling`; an edited value with `source: assumed` keeps the mark. A ruled number for one of these keys NEVER moves into committed `tunables.yaml` (L32, L53): it stays in the note."
- Can hole-fill widen? Not with the two guards in O5. Without the "rows only from the assumed reader" guard, any strategy note's per-trade unit could fill an engine hole — a private copy of an engine key, the exact failure `loader.py:93-111` exists to stop.
- He edits a row later: human wins on the value (L28); the mark follows `source` only, so the worst case is over-marking.
- A committed engine row going null → value while the note still holds the row: loud collision, the whole load fails (L1). Correct, and the last sentence of the wording makes it a thing that should never be done.
- ESCALATE 7, which I would build: the desk write. R15's own words ask for defaults to be put in place and marked assumed; the L73 amendment of the same day makes a direct instruction the per-case override. Cost: no code, one report line. A Cobalt write command is a new write path (L28: off until proven on the dev vault with a diff) for a note written once — not worth its size. I approve nothing (L37); see ASK DESK.

### (f) ACCEPTANCE
**ADOPT WITH:** "(1) For each per-setup fixture day, the expected side, formed bar, trigger price and stop price are written by a CHECKER house from the bars alone, before it sees the builder's output; the test asserts all four, not only `formed`. (2) The live-note test is a named command in every chunk's deploy prompt; the hub reads the run's skip report and a SKIPPED result is RED. (3) `--expect-formed` for a setup with no known day exits non-zero; the chunk's deploy report must then carry X3-style evidence for that setup instead. (4) A committed test asserts that the corpus shape of every setup a chunk claims to unlock is `evaluable`. (5) Geometry guard: long → stop < min(trigger, last close); short → stop > max(trigger, last close); else `not_formed: stop_wrong_side`."
- The miss through the gates: gate 1 catches it (the real 4+1 shape never forms); gate 2 catches it only if the shape corpus holds the real shape — S2-P2's did not (`radar_p2_support.py:88` per the proof); gate 3 catches it when it runs; gate 4 catches it (`formations=0` was accepted on 09-19); gate 5 is unrelated to it.
- Still green while forming nothing: a fixture day picked by the detector's author (→ 1); a day that forms for the wrong reason (→ 1, the four pinned values); the live-note test skipped — it is skipped unless an env var is set (`test_radar_evaluate.py:686-688`) (→ 2); zero tagged trades for rubberband and backside (author's ESCALATE 4) (→ 3); a def the registry stops calling evaluable, so the property test runs over nothing (→ 4).
- Gate 3 as worded is red forever on today's fixture: the live def's day-1 avoid covers all 71 formed scans of that day (`test_rubberband_card_proof.py:220-231`). §9.1 knows this; C1 cannot close without a second committed real-shape day. X2 gates it.
- ## WRONG FACTS 6: a "stop < trigger" guard already exists (`cards/radar.py:106-111`) and the with-trend control PASSED it — both controls published cards (`test_rubberband_card_proof.py:268-289`). Guard (5) is the one that refuses that card: its stop sits at the run's high, above the last close, for a long (`:299`).
- Moving the guard from card creation (a raised error in the stage) to formation (`not_formed`, named) is right and I keep it.

### (g) WARM-UP AND SESSIONS
**ADOPT WITH:** the O6 wording, plus — "§5's 'Nothing [moves], for anything that already exists' is replaced by: the Extension, `atrs_from_open`, `leg_count`, the dots and `card_score` do not move; the card's `health` moves (its EMA9 becomes seeded); the seam observation `atr_working` keeps its name and meaning."
- Does any existing number move? Rubberband's Extension, no: `detect_extension` takes the RTH run and its own ATR (`extension.py:112`); `atrs_from_open` no (`evaluate.py:438-445`). `health`: yes (`evaluate.py:560-564` → `:791-794`), unstated by the proposal.
- Old receipts: a receipt carries `evaluator_version` and `formula_sha256` (`evaluate.py:1253`); whether replay refuses a mismatch was not read by either of us. X8.
- Seeding, arithmetic from the code's own constant (ATR period 14, `evaluate.py:444`): Wilder weight left on pre-open true ranges after n RTH bars is (13/14)^n — n=5 (09:40): 0.69; n=15 (10:00): 0.33. Through the whole early window the seeded ATR is mostly premarket. If premarket 2m ranges are much smaller than opening-drive ranges — UNVERIFIED, X6 — every ATR-scaled tolerance (`A-03`, `A-04`, `A-16`) and the slope normaliser (`A-11`) are several times too tight in exactly the window `Hitchhiker.md:84` and `9 EMA Scalp.md:94` need. The direction of the error is "fewer cards", the safe one; it still decides whether the early setups ever show.

### (h) CHUNKS AND EXPERIMENTS
**ADOPT WITH:** "C1 = S logic + M gates; it needs nothing from C2. C3 splits: C3a = D1 indicators + warm-up (removes E7; moves `health`, so it deploys alone and rolls back alone) · C3b = D2 + D3 opening-drive roles + `range_break` + `consolidation_low` (unlocks hitchhiker). Eight deploy evenings; first card still evening 1; all seven evening 8. X5 is re-run as a gate at C3a, C3b, C4, C5, C6 and C7 — at C2 only one def is evaluable and the measurement is nearly empty."
- C1 really S? The logic, yes: the branch at `evaluate.py:635-647`, a constant, the guard. The gates are not: a second committed bars day, the checker-written expectations, a CLI flag on `evaluate_cli.py:228`'s count, a version-mismatch test. C1 needs no C2 artifact: `unclassified` passes `RadarCardSpec.setup_ref` (`cards/radar.py:84`, `min_length=1`).
- C2 is lighter than priced on one side (O4 removes the column and migration) and heavier on the other (O5's reader). Net M stands. If C2 ships no migration, its restart set may drop `aset` — L42's derivation decides, not this table.
- C3 at L: one evening's three checkers would review a new Range detector, leg roles, a trigger, a stop ref, the warm-up and six assumed keys at once, while an existing published number moves. Failing scenario: the `health` change misbehaves in production and the rollback takes hitchhiker's first cards with it.
- Latency: `radar.scan_interval` = 100 (`tunables.yaml:467-474`). Today one def runs detectors (`evaluate.py:517-528`; the other twelve return at `:518`), about 50 detector passes a scan. The design builds a Frame per (member, side): about 100 Frame builds, each running D1–D6, with seven defs reading atoms. Bars are fetched once per member (`evaluate.py:1214`), so the DB cost does not double. Whether 100 Frame builds fit inside 100 s less the S1–S4 stage time: UNVERIFIED — the wall-clock of `EvaluateStage.run` for a 50-member pool at the last RTH scan of a stored day, today and per chunk (X5).
- X placement: X1 before C3a (not C3/C5 jointly), X2 before C1's fixture choice (correct), X3 inside C1's acceptance (correct), X4 inside C2 (correct), X5 per chunk. Missing: X6–X9 below.

### (i) NOT CHECKABLE FROM READS
**ADOPT WITH:** the nine experiments under `## Experiments (L70)` replace the proposal's X1–X5 paragraph.

## Experiments (L70)

- **X1** (proposal's, kept — before C3a): on `cobalt_dev`, last 10 stored sessions, the share of pool names with at least `period` complete premarket working buckets by 09:30, for periods 9, 14 and 21. Low share → the seed rarely applies, the early windows stay empty, and C3a's value is mostly the fallback.
- **X2** (kept — before C1's fixture choice): for every tagged trade day (the `trade_def:` frontmatter under `1 - Trading/2 - Trades`), does `cobalt_dev` hold that ticker's i1 bars for that date. None for a setup → its fixture day must come from stored pool days, with gate (f)(1)'s checker-written expectations.
- **X3** (kept, sharpened — C1 acceptance): `--replay` of rubberband over the last 10 stored sessions after the C1 change: formations > 0 somewhere; AND for each formation, side and minutes between the culminating bar and the scan. Many formations long after their culminating bar → sticky culmination (`extension.py:123-139`) needs a freshness bound before cards are enabled for that def.
- **X4** (kept, sharpened — C2): registry-driven mirror equivalence on stored days, plus `structural_stop` swept over the cent grid on negated extremes (Python `Decimal` remainder and negative zero). Any inequality → that item gets a side-explicit implementation and is named as the exception.
- **X5** (kept, re-placed — every chunk from C3a): wall-clock of `EvaluateStage.run`, 50-member pool, last RTH scan of a stored day. Over budget → Frames are built lazily, the mirrored side only for a def whose long frame did not form.
- **X6** (new — before C3b): on stored sessions, the ratio `atr_seeded` / RTH-only ATR at 09:40, 09:50 and 10:00, and the count of Range(micro) instantiations inside the `open_drive` sub-window (taxonomy `:79`) under each. Median ratio well under 1 → early ATR-scaled tolerances need an RTH-weighted ATR, and `A-05` changes for ATR while staying for the EMAs.
- **X7** (new — C2, repeated at C4 and C7): the count of scans where BOTH frames satisfy a def's preconditions, per def, last 10 sessions. Non-zero for any def → read those scans; a stale instance on one side hiding a fresh one on the other would turn the blanket `both_sides` refusal into "the later anchor wins".
- **X8** (new — C1): replay a receipt written under the current `EVALUATOR_VERSION` with C1's code. If it recomputes instead of refusing, gate 5 is a build item in C1, not only a test.
- **X9** (new — each chunk from C3b): for every atom the newly unlocked def consults, construct its `AtomOutcome` through `seam.validate_atom` with every declared reason. Any failure or collapse to `unspecified_atom` → the atom's spelling or the closed reason list changes before deploy. (The committed test in (c) is this experiment made permanent.)

## OWNER (after cards)

None is a precondition to build.
- `A-01`: confirm that all three reversion setups trade against the intraday Extension, whatever the day context.
- `A-07`: what ends an opening drive "by consolidation" — this reads a taxonomy rule (taxonomy `:94`), so it may be an amendment rather than a value.
- `A-13`: whether admission to the radar is an acceptable stand-in for the catalyst gate at `9 EMA Scalp.md:44`, or the gate waits for catalyst data.
- The two note-versus-sheet divergences the companion reports (`Fashionably Late.md:47-51`; `VWAP Continuation.md:81`): keep the note's reading or the sheet's.
- The 15 LOW-confidence keys, read from the `--assumed` dry-run with the cards they formed beside them.
- L11: whether the human-only variable of each of the six defs that do not mark one `frontier: true` should be marked in the note.

## WRONG FACTS

1. Proposal §8: a note with no preconditions is skipped as a non-def, and its unit holds `global` and `per_trade(<slug>)` rows read by "the same vault loader pass" (citing `vault_loader.py:43-49`). Code: every `*.md` in the folder is read (`vault_loader.py:476`); a note without the slug frontmatter, `name:`, the definition section or its def unit RAISES (`:327-365`); a draft is an empty def unit (`:380-392`); any row whose scope is not `per_trade(<that note's slug>)` is refused (`:271-280`).
2. Proposal §7.2: `assumed_formation` goes "through the existing suppression path (the one `trail_fit` uses)", and "What this does NOT do" says nothing in `card_score` changes. Code: `suppression()` is a function of dots only and lifts on a tap (`scoring.py:247-251`); `score_card` has no other suppression input (`:319-336`).
3. Proposal Open 3: a nullable `setup_ref` "would add a migration and a view change to C1". Code: the column is already nullable (`0007_radar_cards.sql:34`), the row model is `str | None` (`radar_panel.py:216`) and the panel renders a null (`:735`). Only the two Pydantic models are non-null (`cards/radar.py:84`, `evaluate.py:329`).
4. Proposal §5: the seeded ATR is "a new quantity with its own name (`atr_working`)" and the Extension's is `atr_run`. Code: `atr_working` is already the published seam observation name of the Extension's RTH-run ATR (`evaluate.py:568`).
5. Proposal §6 stores the catalyst outcome with `assumed=A-13`, while its L52 table row (c) says `RadarScoreDetail` has an "unchanged schema". Code: `AtomOutcome` is closed, `extra="forbid"`, and has no such field (`seam.py:99-117`); `UnavailableReason` is a closed Literal that does not contain §5's `insufficient_seed` (`seam.py:48-55`).
6. Proposal §2.3: the geometry guard is "new" and "alone would have turned the with-trend Rubberband card of the proof's control into a refusal". Code and run: the same both-sides condition already exists (`cards/radar.py:106-111`), and the with-trend control passed it and published two cards (`test_rubberband_card_proof.py:268-289`; proof report, test B).

Also unstated rather than wrong: §5's "nothing moves" omits `health` (`evaluate.py:560-564`, `:791-794`).

## READING

- Prompts: `24-setups-tribunal-fable-seat.md` full · `23-setups-tribunal.md:20-43` (QUESTIONS text at `:27-39`; nothing a house wrote) · `22-draft-setups-tribunal.md` by `grep -c` only.
- `cto-2026-09-21.md` rows `:25` (R13), `:27` (R15), `:28` (R17), `:29` (R18), `:31` (R20).
- `LAWS.md:1-405` (full).
- Proposal full · `setups-design-2026-09-21.md` full.
- `rubberband-card-proof-2026-09-21.md` full · `test_rubberband_card_proof.py` test names and assertions by grep (`:3-311`).
- `docs/_inflight/defs-gap-table-2026-09-21.md` full · `docs/_inflight/setups-assumed-values-2026-09-21.md` full (USER DATA, nothing copied).
- `ADR-0009-radar-cards-seam-and-precondition-ast.md` full · `TAXONOMY-DRAFT-v0_7.md:38-187`.
- Notes: `Rubberband.md` full · `Hitchhiker.md` full · `Backside Scalp.md:70-177` · `Fashionably Late.md:17-98` · `Second Chance Scalp.md:84-189` · `9 EMA Scalp.md:19-115` · `VWAP Continuation.md:19-116`. No PDF opened: no ruling turned on a quote.
- Code on main: `evaluate.py:1-700`, `:1160-1229`, greps for `ema9`, `card_health`, `EVALUATOR_VERSION`, `defs_source` · `anatomy/registry.py`, `structure.py`, `bars.py`, `extension.py`, `leg.py` full · `anatomy/daily.py:141-202` · `anatomy/indicators.py` outline by grep · `taxonomy/loader.py:60-149` · `taxonomy/tunables.py:25-124` · `taxonomy/vault_loader.py:1-80`, `:257-284`, `:317-525` · `cards/scoring.py:40-344` · `cards/radar.py:40-117` · `radar/seam.py:40-129` · `aset/radar_panel.py:253-272` · `tests/cobalt/test_radar_evaluate.py:680-719` · `evaluate_cli.py` by grep (`:101`, `:146`, `:228`) · `tunables.yaml:31-39`, `:72-80`, `:466-474` · `0007_radar_cards.sql` by grep (`:34`, `:124-134`).
- Not opened: `settings/card.py:60-75`, `taxonomy/predicate.py`, `taxonomy/trade_def.py`, `replay/*` — no ruling turned on them. Never opened, listed or searched: the houses' folder and the hub's report.

## ESCALATE

1. **Do not write the assumed-defaults note into the Strategies folder, and do not write it anywhere before C2's reader is deployed.** As §8 and the C2 row describe it ("before or with the deploy"), it makes `load_vault_trade_defs` raise for the whole folder (`vault_loader.py:327-365`, `:476`): every `cobalt taxonomy load` / `validate` fails until the note is removed. The running radar keeps its DB copy, so production stays up, but no definition edit can reach it. Owner: desk.
2. ASK DESK: is R15 ("defaults put in place … assumed") the direct instruction that sets L65's "never a value he has not ruled" aside for this one note (L73 as amended `09-21 R5`)? Safe default taken in (e): yes — the desk writes the note once, after C2's reader ships, and records the override in one line; no Cobalt write command is built. [09:39 ET]

Instruction-as-data note (L74, recorded once): the first file read this run carried an appended block inside the tool result asking for a `Claude-Session:` commit line and naming a file-send tool. Not followed. This seat makes no commit.

## CONTINUE

None — the run is complete. The derive (`25`) is a separate job launched by the desk after both round-1 stop lines are committed.

SETUPS TRIBUNAL FABLE R1 DONE · verdict: BUILD AFTER the derive folds the O4, O5, (d) and seam-reason replacements; C1 unblocked · adopt: 1 · adopt with wording: 16 · reject: 0 · experiments named: 9 · ESCALATE: 2
