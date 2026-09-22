# `cobalt.radar.formation.atoms` — ATOMS, RELATIONS and the one shape walk

Added 2026-09-21 in STEP-2 of the setups one build (FINAL §2.5, §4, §7 R2-2.2 B).

- **`AtomValue`** is the value of one atom as the Frame measured it. It moved here from `evaluate.py`, which still re-exports it.
- **`ATOMS`** holds one `AtomResolver` per served atom. A resolver declares:
  - the value kind;
  - for a symbol, its **producible domain** (`Extension.state` is `{culminating, none}` today);
  - `price`: its number is a price, negated back before publication (X12);
  - `tunable_keys`: its detector's `TUNABLE_KEYS` (term (2) of the closure);
  - `conventions`: the conventions it implements (term (3)).
- **`RELATIONS`** has no entries yet. A word it does not serve is named missing.
- **`predicate_gaps(node)`** is the one walk of a predicate's shape. The registry uses it, and it mirrors what `evaluate_node` can evaluate, so the two agree (E9, proved over the corpus). It names:
  - an unserved atom, verbatim;
  - an unserved relation word;
  - `Unsupported(<kind>)` for a shape the interpreter cannot evaluate, such as Arith, a Quantity, or `IN` against something that is not a set;
  - `<atom>∌<value>` for a symbol compared to a value outside its atom's domain (E8).

The atom values themselves are computed by `anatomy/frame.py`. This table only says what is served.

## 2026-09-21 — the D1 rows (setups one build STEP-3; FINAL §3 D1)

Sixteen new rows:

- `price`
- `EMA9`, `EMA21`, `ATR(working_tf)`: convention `frame.warmup_source`, `A-05`
- `EMA9.slope`, `slope_norm(EMA9)`, `slope_norm(VWAP)`: `tunable_keys = slope.TUNABLE_KEYS`
- `VWAP`: convention `vwap.anchor`, `A-12`
- `DayRange.high|low|upper_third`: convention `dayrange.session`, `A-06`
- `PMH`, `PML`, `PDH`, `PDL`
- `InPlay.state`: domain `{active, departed}`

The `price` flag now reads "flips sign with the mirror". Prices carry it, and so do the three slopes. `ATR(working_tf)` does not: a mirrored range has the same width.

A new field, `reasons`, lists every unavailability reason an atom can give. X11 constructs an `AtomOutcome` for each one; before the change it made `seam.UnavailableReason` gain `insufficient_seed` and `slope_norm.bars_unset`. `InPlay.state` is always known and declares none.

The existing four rows now declare their reasons too. Nothing else about them changed: the Lego (ii) pins hold under STEP-3's named normalisation.

`flat(x, window)` is not a row yet. Its detector exists (`anatomy/slope.flat`); the atom arrives with `between` at STEP-5.

## 2026-09-22 — the D2 / D3 rows and the band shape (setups one build STEP-4)

Ten new rows:

- `Range(micro).instantiated|duration|low|top|base|bound|height|wick_ratio`
- `Leg(opening_drive).direction`, domain `{up, down}`
- `Leg(opening_drive).terminated_by`, domain `{pullback, consolidation}`

What they declare:

- The Range rows declare `micro_range.TUNABLE_KEYS` and the warm-up convention: their tolerances scale with the seeded ATR.
- `terminated_by` also declares `leg_roles.TUNABLE_KEYS`.
- `low|top|base|bound` flip with the mirror; `height`, `duration` and `wick_ratio` do not.
- `reasons` include each detector key's `_unset`, and X11 adds those four to the seam's closed list.

`AtomResolver.unit` is new: `Range(micro).duration` is in `min`. `predicate_gaps` now accepts the FINAL §4 row-1 shape `<atom> IN cfg(band) <unit>` when the atom's unit is the Quantity's. Otherwise it names `Unsupported(unit:<q>)` (the atom has no unit) or `Unsupported(unit:<q>≠<atom unit>)`. `unit_mismatch` is the one spelling of that name, shared with the interpreter's runtime check of the band row's own unit.

## 2026-09-22 — D4, `between` + `flat`, Arith (setups one build STEP-5)

- **`Extension.state`.**
  - The domain is `{culminating, reverting, backside, none}`.
  - `tunable_keys` add `extension.LIFECYCLE_KEYS` and `slope_norm.bars`.
  - The reasons add `slope_norm.bars_unset` and `insufficient_seed`.
  - The warm-up convention is NOT declared on it: while `A-08` is null the lifecycle never runs. That is an ESCALATE in the build report.
- **`RELATIONS["between"]`** is served.
  - `_between_gaps` accepts exactly `flat(<EMA9|VWAP>, window: <n> min / working_tf | <n> bars) between <turn|cross> and <turn|cross>`, and names anything else `Unsupported(between:<operand>)`.
  - `window_bars` converts minutes to working bars, rounding up so the window covers the minutes.
  - `flat_between` is the pure test: some `window` consecutive bars inside the span with every |normalised slope| ≤ the threshold.
  - `relation_operand_names` tells the registry which raw names a served relation consumes.
- **Arith `*` / `/`** (FINAL §4 row 2) is an operand shape: `predicate_gaps` walks both sides. `+` / `-` stay `Unsupported(arith)`.

## 2026-09-22 — roles, `touched`, `on`, bound symbols, `A-13` (setups one build STEP-6)

- **The role rows:** `Leg(pullback).direction|end|index`, `Leg(impulse).direction` and `Leg(opening_drive OR impulse).direction`; directions have domain `{up, down}`.
- **`catalyst_ref`** is THE ONE NAMED SPECIAL CASE (FINAL §6, R2-2.4 B). A boolean atom whose resolver stands in for data the radar does not have: the def's "or setup" branch, read as met by the pool admission. Its conventions are `(CATALYST_CONVENTION,)`, the row `catalyst_ref.resolver` (`A-13`), so the formation's closure carries the key and the mark reaches the card through the `assumed_formation` dot. `AtomOutcome` gains nothing: X26 shows `assumed=` is a `ValidationError`. Extension path B keeps `catalyst_ref_unknown`.
- **Relations.**
  - `RELATIONS["touched"]` serves `Leg(pullback|impulse) touched EMA9|EMA21|VWAP`.
  - `RELATIONS["on"]` serves `Extension.instantiated on Leg(pre_test)` and declares the conventions `leg.pre_test` (A-14) and `extension.on_leg.form` (A-15).
  - `RelationResolver.conventions` is new, and `evaluate._conventions` reads it.
  - Any other operand is `Unsupported(touched:…)` / `Unsupported(on:…)`.
- **Bound symbols (FINAL §4).** `BOUND_SYMBOLS = {trade_direction: up}` and `opposite(x)` / `against(x)` through `bound_direction`. A bound form is a value, never an atom (`relation_operand_names`), and never an E8 domain miss. `null` is an operand.

## 2026-09-22 — `dist`, the level set, `rejected` (setups one build STEP-7)

- **`dist(a, b)`** (`dist_operands`) is a served function: `|a − b|` in price, with its operands' gaps walked. The vwap-continuation shape compares it to `cfg(dist.k.vwap) × ATR(working_tf)`. `dist.k.vwap` is a `per_indicator` hole (F1, never widened), so at production defaults it reads `dist.k.vwap_unset`.
- **`Level_ref(resistance).rejected`** is a boolean row with conventions `levels.set` (`A-17`, the set = {PMH, PDH}) and `level.rejected.rule` (`A-18`: a wick through the level, a close back below, and the last close still below). The frame computes it.

## 2026-09-22 — the RangeBreak lifecycle and its events (setups one build STEP-8)

- **Rows.**
  - `RangeBreak(level).state` and its alias `RangeBreak.state`, with domain `{forming, break_attempt, accepted, failed_trap}`.
  - `event(retest)` and `event(stop_hit)`: booleans. `stop_hit` also declares `event.stop_hit.source` (A-22) and `turn_candle.rule` (A-23).
  - All of them declare `range_break.TUNABLE_KEYS`, the level set and the warm-up.
- **Shapes.** `predicate_gaps` serves an `EventAtom` whose render is a row, and three new relation shapes:
  - `event(retest) on that RangeBreak`: the anaphora;
  - `<RangeBreak state> after event(retest)`;
  - `price inside Range(prior)`: `RELATIONS["inside"]`, convention `range_prior.rule` (A-21).
- `relation_operand_names` lists each shape's consumed operands.

**2026-09-22 (fix round 2, F2) — `sequence` steps.** FINAL §4: `close_through` and `close_above(prior_bar)` inside `sequence` steps are "relation resolvers over working-TF closes". `STEP_SHAPES` maps each served step shape to its bar-indexed resolution `(frame, i) -> bool`: `price close_through Level_ref` (bar i closes above the level), `event(retest)` (bar i is the RangeBreak observation's retest bar, as before), `close_above(prior_bar)` (bar i closes above the prior bar's high). `Level_ref` is the level of the frame's RangeBreak(level) observation (`range_break_observation`), the existing binding. `step_gaps` names what keeps a step from being walked: `Unsupported(close_through:…)` / `Unsupported(close_above:…)` outside the served shape; otherwise `predicate_gaps`, and `Unsupported(step:<predicate>)` for a predicate the interpreter serves but that has no bar-indexed resolution. These shapes are served in steps only; `close_through` is still not a precondition relation (not in `RELATIONS`).
