# Setups at defaults — design v2 (DERIVED) — 2026-09-21

Derived by the Fable seat's second job (`setups-tribunal-derive-0921`; `cto-2026-09-21.md` §4 R20, "blind ruling (+ the derive step…)"), L67 step "derive". **Nothing is built from this file until `## Not settled` below is empty.**

| input | path | status |
|---|---|---|
| the proposal (Opus 5, `652434e`) | `docs/30 - Design/SETUPS-AT-DEFAULTS-PROPOSAL-2026-09-21.md` | whole, amended in place below |
| Grok ruling | `scratch/tribunal-bars-0920/setups-tribunal/r1/grok-ruling.md` · hub file-check `docs/40 - DevDocs/reports/setups-tribunal-2026-09-21.md` | ruled in full |
| Gemini ruling | `scratch/tribunal-bars-0920/setups-tribunal/r1/gemini-ruling.md` · hub file-check `docs/40 - DevDocs/reports/setups-tribunal-r1b-2026-09-21.md` | ruled in full; nine of its claims DO NOT HOLD (R1B rows 2, 4, 6, 8, 9, 10, 17b, 24, 25a) |
| Fable ruling (blind) | `docs/40 - DevDocs/reports/setups-tribunal-fable-r1-2026-09-21.md` | ruled in full; no hub file-checked its claims |
| astra | — | **astra: did not rule (METER round 1, TIMEOUT round 1B) — derived without it on his ruling R32** |
| fold table | `docs/40 - DevDocs/reports/setups-tribunal-derive-2026-09-21.md` `## Fold table` | F-01 … F-21 |
| owner ruling binding §9 | `cto-2026-09-21.md` §4 R24 (11:13 ET) | folded as F-21 |

**How to read this file.** It is the proposal, whole. Every amended paragraph carries a tag `[F-nn]` that is a row of the fold table. Three kinds of tag:
- `[F-nn]` — a house's wording taken WORD FOR WORD (in a blockquote, house named), or a wrong sentence removed (struck through).
- `[F-nn · NOT SETTLED → R2-n]` — the proposal's text is left standing ONLY so the file can be diffed; it is contested between houses and is not buildable until round 2 answers `R2-n`.
- `[F-nn · X<n>]` — a claim no read can settle; it is an experiment in `## First-gate experiments (L70)`, run before the chunk it gates.

Every per-item count is out of the three seats that ruled (Grok, Gemini, Fable). "R1 row n" / "R1B row n" = that hub report's `## Checked against the files` table. The derive invents no mechanism, number, rule or chunk.

**Scope.** The seven setups on his short list (R18), in the slugs his notes use: `rubberband`, `hitchhiker`, `backside`, `second-chance`, `fashionably-late`, `nine-ema-scalp`, `vwap-continuation`. The other six definitions are out of scope, but every mechanism here is a registry they plug into without a refactor (§2, §3).

**L32 rule for this file.** It carries no value, quote or wording from his notes or the cheat sheets. It cites his notes by `file:line` (all under `/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies/`), the cheat sheets by `docs/90 - References/<file>.pdf` page, and every assumed value by KEY (`A-01` … `A-23`). The values, sources, quotes and confidence levels are in the gitignored companion `docs/_inflight/setups-assumed-values-2026-09-21.md`. No house proposed a value for an assumed key in round 1.

**Fact base (read, not redone).** `docs/_inflight/defs-gap-table-2026-09-21.md` (gap table: G1–G13, D-1…D-16, E1–E11); `~/cobalt-wt/rubberband-proof/docs/40 - DevDocs/reports/rubberband-card-proof-2026-09-21.md` (the proof); ADR-0009; the code on `main` at `0cf4b82`.

---

## Not settled (→ round 2) — the four items, full text in the derive report `## NEEDS ROUND 2`

| # | item | gates |
|---|---|---|
| R2-1 | O1 — the `Direction(unbound)` refusal: kept (Grok) or removed (Fable) | the registry check (proposal C1 row; C2's generalised registry) |
| R2-2 | O4 / (d) / (c)(a)(b) / O8 — how an assumed value is marked on the card and degrades the score, `A-01` on the C1 card included | **C1** (L52 (a)) and C2 |
| R2-3 | O5 / (e) — the assumed store: note location, reader, hole-fill predicate | C2 |
| R2-4 | O2 — what a two-frame evaluation publishes, and where observations are computed | C2 |

---

## 1. DIRECTION — Rubberband first, its own deployable chunk

### What is wrong (proven)

`evaluate.py:635-645` reads a def's `valid_setups[].relation` as the relation between the trade and the **Extension**: all countertrend → trade against the run, all with_trend → trade with it, mixed → `not_evaluable: Setup(relation)`. `Rubberband.md:36-41` mixes both. The proof ran it: 71 of 71 scans where a single-relation control forms come back `not_evaluable` (proof report, test A). `setup_ref` is then the first listed entry with that relation (`evaluate.py:647`) — a label that depends on list order, not a detection.

> **[F-01]** Proposal kept. All three seats hold this root cause (R1 rows 1, 2 HOLD; R1B row 1 HOLDS; Fable (a) ADOPT).

### Why it is wrong (the root cause, not just the symptom)

`relation` is the relation between the trade and the **setup's** trend (the day or higher-timeframe context: a gap, a day-2 trend, an overextension). It is not the relation to the intraday Extension. Three facts, each readable:

1. The schema puts `relation` on the setup entry: `valid_setups[]: {setup_ref, relation}` (`TAXONOMY-DRAFT-v0_7.md:136`). The trade's direction is a separate field, `instance_direction: computed from setup-instance state` (`:137`; also `:124`, "every trade_def side-symmetric").
2. Rubberband's trigger and stop only make sense AGAINST the Extension. The stop ref is `snapback_candle` (`Rubberband.md:53`), which the taxonomy defines as the current tracked extreme of the move (`TAXONOMY-DRAFT-v0_7.md:110`; sheet reading law (b), `:62`). A stop just beyond the extreme of a move protects a trade against that move. With the move, the extreme is ahead of price, not behind it. The proof's own with-trend control shows this: a long on an up-run gets its stop placed from the run's high (proof report, "With-trend geometry"; `structure.py:70-79`, `:100-116`).
3. The cheat sheet describes one trade shape and its inverse only (`the_rubberband_scalp_cheat_sheet.pdf` p.1, entry and stop rules). The same holds for `backside` (`back$ide_cheat_sheet.pdf` p.1) and `fashionably-late` (`the_fashionably_late_scalp_cheat_sheet.pdf` p.1). In each case, every one of the def's five setup entries (`Rubberband.md:37-41`, `Backside Scalp.md:90-94`, `Fashionably Late.md:32-36`) resolves to the same side: against the Extension. The with_trend `day2_continuation` entry is with the *day-2* trend and still against the intraday Extension.

> **[F-03 · X10]** For `rubberband` fact 3 stands (three seats). For `backside` and `fashionably-late` it is NOT SETTLED: Grok lists it as a WRONG FACT ("used to justify `against ext.direction` beyond rubberband"; R1 row 30 HOLDS as a reading of §1, its consequence R1 row 7b is UNVERIFIABLE FROM READS — no backside detector exists); Fable (a) holds the same side per Extension, provided the Extension's direction is held from its culminating bar. Both seats rest on one fact that HOLDS: the detector's direction is sign(last close − session open) (`extension.py:96-103`, R1 row 7a). **X10 runs before C4.** Nothing in C1–C3b depends on it: no `backside` / `reverting` state is produced before D4.

So S2-P2 made a category error: it read a setup-context field as a direction field. That is how a def "that will never show up" was built and shipped green. The proof explains why the suite never saw it (proof report, "Why the S2-P2 suite and the 09-19 replay were green").

### The mechanism (simplest correct)

**Direction comes from the trade's own anatomy. `relation` is never read for direction.**

- **Orientation rule (key `A-01`).** In a def written long-side (`TAXONOMY-DRAFT-v0_7.md:89`, "trade_defs written long-side"), an unqualified `Extension` is the Extension the long trade opposes, so its direction is down. `Extension … on Leg(x)` is the Extension of that leg, whatever its direction. For chunk 1 this reduces to one line, `trade_direction = against ext.direction`. That is today's countertrend branch (`evaluate.py:636-637`), applied to every def whose precondition anchor is an unqualified Extension. §2 generalises it with the mirrored frame.

> **[F-01]** Proposal kept for C1: under Grok's O1 wording and under Fable's O1 wording alike, the only def this line can form in C1 is `rubberband`. Neither house's O1 replacement is taken: Grok's embeds the refusal that Fable contests (R2-1) and a sentence resting on R1 row 7b (UNVERIFIABLE); Fable's embeds the removal that Grok contests and a D4 mechanism only one seat offers (X10). The four with-trend defs carry no unqualified Extension anchor, so this line never applies to them (R1 rows 5, 6; R1B row 2).
>
> **[F-08 · NOT SETTLED → R2-2]** `A-01` is an assumed convention, neither a `cfg` key nor a resolver. As this section stands, the C1 card's direction, trigger and stop rest on it UNMARKED and the card is scored — L52 (a) is not met for C1 (R1 hub ESCALATE 3; R1B hub ESCALATE 3; Fable (c)(a)). Grok and Fable each offer a mechanism; they disagree. **R2-2 gates C1.**

- **Setup identity is NOT detected in this design.** No detector for gap / day-2 / overextension / volatility-in-range exists or is proposed. The card shows `setup_ref = unclassified`. The existing human quality factor `setup_relation` (`Rubberband.md:101`, a tap in `evaluate_cli.py:35`) carries his read. The order-dependent label (`evaluate.py:647`) is deleted, not replaced by another guess.

> **[F-07]** Fable, O3, word for word: "`UNCLASSIFIED_SETUP = "unclassified"` is a module constant in `evaluate.py`; it is NOT a member of the `SetupRef` enum, so no definition can list it in `valid_setups`." — Three seats ADOPT the token; Grok states the same rule ("`SetupRef` … has no `unclassified` and must not"); R1 row 16 and R1B row 26 HOLD.

- **Neither side qualifies → `not_formed`** (unchanged). **Both sides qualify on the same scan → `not_formed`, note `both_sides`.** This is counted on the board and never a guess. For chunk 1 it cannot happen, because the Extension has exactly one direction (`extension.py:96-103`). In §2 it can, and it stays refused.

> **[F-19 · X7]** Kept by all three seats. How often it happens is measured, not argued: X7.

- **A def whose side cannot be bound is refused.** If a def names neither an oriented object nor `trade_direction`, the registry reports it `not_evaluable: Direction(unbound)`, named in the dry-run. It never forms.

> **[F-02 · NOT SETTLED → R2-1]** Grok keeps a refusal ("A def with no oriented object and no bindable `trade_direction` → `not_evaluable: Direction(unbound)`"). Fable removes it ("there is NO separate `Direction(unbound)` refusal"): as worded here it would refuse `hitchhiker` and `second-chance`, which §2.1 already binds by frame. Two houses disagree on whether this mechanism is correct. Not built until R2-1 is answered.

**What the card shows.** `direction` (COBALT, unchanged). `setup_ref = unclassified` (COBALT, the literal token). `why` is unchanged in shape (`evaluate.py:674-680`) with the setup token first. The `setup_relation` dot stays YOURS.

**Files.** `src/cobalt/radar/evaluate.py` (`:34-37` docstring, `:635-647` gate + label). `EVALUATOR_VERSION` is bumped (`:132`). `src/cobalt/radar/anatomy/registry.py` gets the unbound-direction check **[F-02 → R2-1]**. Tests: see §9. No schema, migration, card column, vault or config change **[F-08 → R2-2: one of the two offered `A-01` marks stores a string on the card row]**.

**Cost, priced honestly.** Size S: about 20 lines of logic, plus the tests of §9, which are most of the work **[F-18: "C1 = S logic + M gates", §10]**. Risk: the direction of every Rubberband card now rests on `A-01`, a reading of the taxonomy and sheets and not a ruling. Its confidence is HIGH in the companion, and it is Open point 1. The second gate (the def's own day-1 HTF avoid, `Rubberband.md:86`) stays and is correct. A fixed Rubberband still forms no card on a day that avoid covers (proof ESCALATE 2).

## 2. THE FORMATION STAGE, generalised (gap table E2)

Today formation is hard-wired to one shape: the Extension's culminating bar, a `bar_break{bars_cleared}` trigger and the tracked-extreme stop, enforced by `assert`s (`evaluate.py:633-671`, `:649-651`). The seven need 6 trigger shapes and 6 stop placements (the list below). The design turns formation into **three registries of resolvers, keyed by the def's own data**, plus one side-binding step. Nothing is keyed by trade name (L31/L32, as `registry.py:5-8` already requires).

### 2.1 Side binding — the mirrored frame

> **[F-04]** Grok, O2, word for word — this replaces the proposal's frame definition, its "`trade_direction` is bound to `long` in both frames" sentence, its negation sentence and its property test:
>
> "Every def is evaluated twice, once per side, on a Frame. Long = stored bars. Short = the same detectors on mirrored bars (price → −price, high ↔ low; volume and time unchanged). `trade_direction` in a frame means that frame's side. A price from the mirrored frame is negated before it reaches `Formation` or `RadarCardSpec`. Acceptance property (not the proposal's): `negate_prices(eval_as_long(mirror(bars))) == eval_as_short(bars)` for price outputs, and `pred_as_long(mirror(bars)) == pred_as_short(bars)` for predicates. Do not ship `detector(mirror(bars)) == mirror(detector(bars))`."
>
> Why this wording: three seats keep the frame. The proposal's property is false for the stop as stated (R1 rows 8a ARITHMETIC OK, 8b HOLDS); Gemini's "No equivalence flaws exist" DOES NOT HOLD (R1B row 4); Fable's own property also maps long↔short. Of the two houses' properties this is the smaller mechanism; Fable's registry-driven `unmirror()` property is carried as an owner item (trade-off) and its single-seat additions as R2-4 and X12.

Every detector runs unchanged on both frames. Every def is read as its long-side text (`TAXONOMY-DRAFT-v0_7.md:89`, `:124`; each of the seven sheets says the short side is the inverse). Examples: `EMA9.slope > 0`, `Range(micro).low > EMA9`, `Range(micro).bound`, `recent_higher_low` and `a_crosses_above_b` all mean the right thing on the short side with no side-specific code. `opposite(trade_direction)` and `Leg(…).direction == trade_direction` compare against the frame's own `up`. A def forms on side s only when its preconditions are True, no avoid is True, and trigger and stop both resolve on frame s.

Why this and not side-aware detectors: one pure transform and one property test (**[F-04]** the property above) replace a long/short branch in every detector. The cost is CPU, not code: every def is evaluated twice. First-gate experiment X5 measures the latency.

> **[F-06 · X4, X6]** The places where price → −price is not a plain equivalence are an experiment list, not an argument: stop buffer + round-away + ten-cent nudge (`structure.py:96-116`), `DayRange.upper_third`, `RadarCardSpec` `gt=0` (`cards/radar.py:86-88`), the non-positive-buffer refusal (`structure.py:101-102`), the HTF-proximity tie label (`daily.py:147-149`), `htf_range_break` (`daily.py:182-196`) — R1 rows 8b, 9, 10, 11, 12 HOLD. `Decimal % 10` on negative cents is UNVERIFIABLE FROM READS (R1 row 15) → X4. A negative-price archiver `Bar` → X6 (R1 row 14, R1B row 5).
>
> **[F-05 · NOT SETTLED → R2-4 · X12]** Fable's O2 additions are single-seat and no hub checked them: per-type `unmirror()` (labels and `why` strings, not only prices), the daily series and level set mirrored with the bars, factor and seam observations computed once on the real bars, and ONE published evaluation per (member, def) with a stated order. Whether a mirrored-frame card carries a negative price or a long-side label anywhere but `trigger_price` / `structural_stop` is X12 (C2). What the single seam row (`evaluate.py:593-596`) publishes when neither frame forms is R2-4.

### 2.2 Trigger resolvers (data: `trigger.type` + params shape)

`src/cobalt/radar/formation/triggers.py`, `TRIGGERS: dict[TriggerType, TriggerResolver]`. Each resolver declares `serves(params) -> bool` (the param shape) and returns a `TriggerOutcome {state: armed | fired | unavailable, price, ref_bar_ts, kind, inputs, why}`.

| type (schema `trade_def.py:183`) | param shape | used by (of the seven) | resolves to |
|---|---|---|---|
| `bar_break` | `{bars_cleared}` | rubberband (`Rubberband.md:46-49`) | today's `bar_break_trigger` (`structure.py:82-93`), re-registered, byte-identical output |
| `range_break` | `{ref: Range(micro).bound \| .top}` | hitchhiker (`Hitchhiker.md:40-42`), backside (`Backside Scalp.md:101-103`) | the trade-side bound of the live micro-Range, intrabar |
| `indicator_cross` | `{a, b, direction}` | fashionably-late (`Fashionably Late.md:43-44`) | the bar where a crosses b in the stated direction; stamps `cross_point` |
| `indicator_rejection` | `{indicator, contact}` | nine-ema-scalp (`9 EMA Scalp.md:48-49`) | the bar that touches/penetrates the indicator and closes on the trade side; `close_through` by definition (`TAXONOMY-DRAFT-v0_7.md:163`, `:174`) |
| `trendline_break` | `{ref: Level_ref(trendline), anchor_leg}` | vwap-continuation (`VWAP Continuation.md:43-46`) | the line through the anchor leg's pivots (≥ `cfg(trendline.min_pivots)`); the flat case is the micro-Range far bound (`TAXONOMY-DRAFT-v0_7.md:114`) |
| `sequence` | `{steps[]}` | second-chance (`Second Chance Scalp.md:110-118`) | the steps in order; each step is a predicate evaluated by the same interpreter (§4); the last step's bar is the trigger bar |

### 2.3 Stop resolvers (data: `stop.placement.type` + ref)

`src/cobalt/radar/formation/stops.py`, `STOPS: dict[placement type, StopResolver]`, plus `STRUCTURAL_REFS: dict[StructuralRef, RefResolver]` for the §3.6 refs (`TAXONOMY-DRAFT-v0_7.md:110`). The buffer and the stop-nudge law are reused unchanged (`structure.py:100-116`).

| placement | ref / params | used by | resolves to |
|---|---|---|---|
| `structural_extreme` | `snapback_candle` / `turn_low` | rubberband | today's tracked extreme (`structure.py:70-79`), re-registered |
| `structural_extreme` | `consolidation_low` (= `Range.base`) | hitchhiker (`Hitchhiker.md:44-47`) | the micro-Range base |
| `structural_extreme` | `recent_higher_low` | backside (`Backside Scalp.md:105-108`) | the micro-Range's latest counter-pivot on the trade-opposite side |
| `structural_extreme` | `turn_candle` | second-chance (`Second Chance Scalp.md:121-124`) | the extreme of the retest bar that turned at the level (`A-23`) |
| `measured_fraction` | `anchor_a, anchor_b, fraction` | fashionably-late (`Fashionably Late.md:47-51`) | anchor_a − fraction × (anchor_a − anchor_b), anchors resolved through `STRUCTURAL_REFS` (`entry` = the trigger price) |
| `indicator` | `indicator, snapshot` | nine-ema-scalp (`9 EMA Scalp.md:52-55`), vwap-continuation (`VWAP Continuation.md:50-53`) | the indicator's value at the trigger bar (`snapshot: at_entry`, the ruled default, `TAXONOMY-DRAFT-v0_7.md:164`) |

**Geometry guard (~~new,~~ fail-loud).** A resolved stop that is not on the protective side of the trigger (long: stop < trigger; short: stop > trigger) gives `not_formed`, note `stop_wrong_side`, never a card. ~~This guard alone would have turned the with-trend Rubberband card of the proof's control into a refusal.~~

> **[F-17]** Sentence removed, and "new" struck: WRONG FACT held by two seats (Grok WF1, R1 row 29 HOLDS; Fable WF6). The same stop-below-trigger condition already exists at card creation (`cards/radar.py:106-114`, R1 row 10) and the proof's with-trend control PASSED it and published cards. Moving the check from card creation to formation is kept (Grok: "worth having"; Fable: "is right and I keep it"). The guard's condition in v2 is §9 point (5) **[F-16 · X17]**.

### 2.4 The Formation model

`Formation` (`evaluate.py:324-336`) is generalised. `extension_direction` becomes `anchor {object, direction, bar_ts}`. `trigger` becomes the `TriggerOutcome`. `extreme` becomes optional. `stop` gains `placement` and `inputs`. `setup_ref` is kept (the token `unclassified` in this design). New: `side_frame: long | mirrored` and `assumed_keys: tuple[str, ...]` (§7) **[F-08 → R2-2]**. `card_why` (`evaluate.py:674-680`) is assembled from the resolvers' `why` fragments **[F-05 · X12]**. No resolver writes prose from his notes (L32).

### 2.5 One path for "what is served" (fixes E8 and E9)

`registry.evaluability` stops keeping its own constants (`registry.py:27-38`). It reads `TRIGGERS`, `STOPS`, `STRUCTURAL_REFS`, `ATOMS` and `RELATIONS` (§3, §4): the same tables formation dispatches through (L3). Each atom resolver also declares its **producible value domain**. A precondition that compares a symbol atom to a literal outside that domain is `not_evaluable: <atom>∌<value>`. Example: `Extension.state IN {reverting, backside}` while the detector produces only `culminating | none` (`extension.py:70`). So the registry can no longer report served-but-never-true (E8). Every AST shape the interpreter cannot evaluate is also named in `missing` (E9), because `evaluability` walks the AST through the same dispatch the interpreter uses.

**Extension without refactor.** A future trigger (`bar_break{ref: Level_ref(open)}` for the other six, a swing `daily_close_break`, an options `iv_cross`) is one resolver plus one registry row. It declares its own `serves()` and domain. The stage, the registry and the card are untouched.

## 3. THE DETECTOR GROUPS the seven need — build order by setups per unit of size

All inputs are stored today: i1 04:00→19:59 ET (`cto-2026-09-20.md:23-24`, gap table), the daily series (`daily.py`) and the pool row (`radar/runner.py:139-142`). No new data source. Each detector is PURE (bars in, typed observation out) and emits typed atoms with a declared domain.

**The Frame** (`src/cobalt/radar/anatomy/frame.py`, new) is built once per (member, scan, side). It holds the RTH run (as today), the warm series (§5), the indicators, and every detector's observation. `evaluate_member` asks the frame for atoms and never runs detectors itself.

| # | group (gap table) | atoms / refs (typed events) | inputs | unlocks (with earlier groups) | size |
|---|---|---|---|---|---|
| D0 | Direction (G1, §1) | `trade_direction`, `opposite(…)`, orientation `A-01` | the frame side | rubberband | S |
| D1 | Shared indicators + session levels (G3 part, G8) | `price`, `EMA9`, `EMA21`, `EMA9.slope`, `slope_norm(x)` (`A-11`), `flat(x, window)` (`A-09`, `A-10`), `VWAP` (`A-12`), `ATR(working_tf)` (seeded, `A-05`, §5 — **[F-10]** published as `atr_seeded`), `DayRange`, `DayRange.upper_third` (`A-06`), `PMH/PML/PDH/PDL`, `InPlay.state` (pool admission, `evaluate.py:320`) | warm series + RTH run + daily | none alone (shared) | M |
| D2 | Range(micro) + pivots (G5) | `Range(micro).{instantiated, duration, low, top, base, bound, height, wick_ratio}`, `bound_type` (diverging = no Range), pivot highs/lows `cfg(pivot.n)`, refs `consolidation_low`, `recent_higher_low` | RTH run, `A-02`, `A-03`, `A-04` | hitchhiker (with D1, D3) | L |
| D3 | Leg roles (G4) | `Leg(opening_drive).{direction, terminated_by}`, `Leg(impulse)`, `Leg(pullback).{direction, end, index}`, `Leg(pre_test)` (`A-14`), relation `touched` | RTH run + D2 (for `terminated_by: consolidation`, `A-07`) **[F-12 · X15, X16]** | hitchhiker; nine-ema-scalp (with D1) | M |
| D4 | Extension lifecycle (G10, E8) | `Extension.state` domain grows to `building \| extending \| culminating \| reverting \| backside \| resuming \| none` (`TAXONOMY-DRAFT-v0_4.md:32`); `reverting` from the snapback rule `A-08`; `backside` from ≥`cfg(extension.backside_hh_min)` HH and ≥`cfg(extension.backside_hl_min)` HL above a rising EMA9 (`TAXONOMY-DRAFT-v0_7.md:98`); `Extension.instantiated on Leg(x)` (`A-15`); refs `turn_low`, `turn` **[F-03 · X10]** | RTH run, D1 EMA9, D2 pivots | backside (with D2), fashionably-late (with D1) | M |
| D5 | Trendline + distance (G11 part, G3 part) | `Level_ref(trendline, anchor_leg)`, trigger `trendline_break`, `dist(a, b)` in working-TF ATR with `cfg(dist.k.vwap)` (`A-16`) | D2 pivots, D3 legs | vwap-continuation (with D6 levels + `dist`) | M |
| D6 | Levels + RangeBreak lifecycle + events (G6) | the level set `A-17`; `RangeBreak(level).state ∈ {forming, break_attempt, accepted, failed_trap}` (`failed_trap` within `cfg(range_break.failed_trap_bars)`, `A-19`); `event(retest)` (`A-20`); `event(stop_hit)` (`A-22`); `Range(prior)` (`A-21`); `Level_ref(resistance).rejected` (`A-18`); ref `turn_candle` (`A-23`) | RTH run, premarket i1, daily | second-chance; the `rejected` avoid of vwap-continuation | M–L |
| — | Catalyst resolver (G12, only for `nine-ema-scalp`) | `catalyst_ref` resolved by `A-13` (§6) | pool admission | nine-ema-scalp | S |

Order by setups unlocked per unit of size, after D0: D1+D2+D3 together unlock hitchhiker, the first entry on his list (L, 1 setup, and they are the shared base for 5 of the 7). D4 then unlocks two (backside, fashionably-late) for M, which is the best ratio in the ladder. D3's pullback roles + `indicator_rejection` + the catalyst resolver unlock nine-ema-scalp for M. D5 + `dist` unlock vwap-continuation for M, and they need D6's level set only for the `rejected` avoid, so that part of D6 moves into D5's chunk. The rest of D6 unlocks second-chance for M–L. Chunks: §10.

**Not built:** Gap, volatility_state, Regime, Catalyst grade/polarity (G7, G9, G12, G13) — none of the seven needs them.

## 4. THE INTERPRETER GAPS (E9) — only what the seven need

Today the interpreter raises `Unsupported` for Relation, Qualified, Between, Arith, Quantity and `IN` against a non-set (`evaluate.py:215-235`, `:284-293`). The AST already parses them (`predicate.py:122`, `:156`, `:181-200`). The seven need:

| shape | where (note:line) | proposal |
|---|---|---|
| `IN cfg(band) min` (Quantity + band) | `Hitchhiker.md:37` | `InTest` with a `Cfg` that resolves to `[lo, hi]` → inclusive band test; `Quantity` carries a unit; minutes convert to working bars only through the unit table (`TunableUnit`, `tunables.py:32-53`). A unit mismatch is `Unsupported`, named |
| Arith `*`, `/` | `VWAP Continuation.md:41`; `Fashionably Late.md:66` | Decimal at the indicator module's precision (`indicators.py:26-27`); division by zero → unknown with a reason, never inf |
| `trade_direction`, `opposite(x)`, `against(x)` | `9 EMA Scalp.md:45`; `VWAP Continuation.md:40-41` | bound symbols from the frame (§2.1); direction values map `up ↔ long` in the frame's orientation |
| Relation words `touched`, `on`, `after`, `inside`, `between` | `9 EMA Scalp.md:46`, `:78`; `Second Chance Scalp.md:108`, `:152-153`; `Fashionably Late.md:66` | ONE `RELATIONS: dict[word, RelationResolver]` table (§2.5). Each resolver takes the operands' typed objects (a Leg, an indicator series, an event with a bar index) and returns three-valued truth. An unknown word → `not_evaluable: relation:<word>`, named |
| `Leg(opening_drive OR impulse)` | `9 EMA Scalp.md:45`; `VWAP Continuation.md:40` | the most recent leg of either role that precedes the pullback being evaluated (D3) |
| anaphora `that RangeBreak` | `Second Chance Scalp.md:108` | binds to the RangeBreak the previous precondition in the same def evaluated True; with no antecedent it is unknown, never "any" |
| `close_through`, `close_above(prior_bar)` inside `sequence` steps | `Second Chance Scalp.md:113-118` | relation resolvers over working-TF closes (`TAXONOMY-DRAFT-v0_7.md:170`) |

Kleene three-valued semantics are unchanged (`evaluate.py:244-293`). Every new shape keeps "unknown ≠ false".

## 5. WARM-UP (E7)

**Problem.** `evaluate.py:526-528` builds working bars and keeps RTH only. EMA21 on 2m therefore has no value before about 10:12 ET, EMA9 before about 09:48, and ATR(14) before about 09:58 (E7). `nine-ema-scalp`'s preferred window (`9 EMA Scalp.md:94`) opens before EMA21 can have an RTH-only value, and `hitchhiker`'s (`Hitchhiker.md:84`) closes before an RTH-only ATR has much history.

**Proposal (key `A-05`).** The Frame has two series:

- **run** = RTH only, exactly as today. Every **session-anchored** object uses it: the Extension (leg base = session open, `tunables.yaml` `extension.leg_base`), Legs and their roles, Range(micro), DayRange, RangeBreak, VWAP (`A-12`, RTH-anchored) and the open.
- **warm** = working bars from the premarket (04:00) through now. It is used ONLY to seed the rolling indicators `EMA9`, `EMA21` and `ATR(working_tf)`. The first RTH value of each is the continuation of its premarket-seeded series. Premarket buckets with no print are absent, and incomplete ones are flagged (`bars.py:13-17`). The seed uses only complete premarket buckets. With fewer than `period` of them, the indicator is `unavailable: insufficient_seed` **[F-14 · X11]** and falls back to the RTH-only warm-up (later, never guessed).

**What it does to "RTH bars only".**

> **[F-10]** Fable, O6, word for word — this replaces the proposal's `atr_run` / `atr_working` naming:
>
> "The Extension's RTH-run ATR KEEPS the name `atr_working` (it is already published under that name). The premarket-seeded ATR is a new quantity named `atr_seeded`. Both are `wilder_atr` over different series: one function, two named inputs. EMA9 and EMA21 have ONE definition each — seeded, falling back to RTH-only when the seed is short — and `MemberEvaluation.ema9` takes that value. The chunk that lands this states in its deploy notes that the `health` of open cards moves, and bumps `EVALUATOR_VERSION`."
>
> Why this wording: `atr_working` is today's seam observation of the Extension's RTH ATR (`evaluate.py:568`) — Grok WF2 and Fable WF4, R1 row 20 HOLDS; `ev.ema9` feeds FILLED-card health (R1 row 22 HOLDS, both seats). Grok names the same new quantity (`atr_seeded`). Grok's own O6 text is not taken: the reason beside it ("Renaming the live name moves Rubberband `atrs_from_open` inputs") DOES NOT HOLD (R1 row 21). Gemini's "keeping `atr_run` … introducing `atr_working`" DOES NOT HOLD (R1B row 6).
>
> **[F-11]** Fable, (g), word for word — this replaces "Nothing, for anything that already exists.":
>
> "§5's 'Nothing [moves], for anything that already exists' is replaced by: the Extension, `atrs_from_open`, `leg_count`, the dots and `card_score` do not move; the card's `health` moves (its EMA9 becomes seeded); the seam observation `atr_working` keeps its name and meaning."
>
> `atrs_from_open` unmoved: R1B row 7a HOLDS. The blanket "do not shift" is UNVERIFIABLE FROM READS (R1B row 7b) → **X14** at C3a. Whether a premarket-dominated seeded ATR makes the early ATR-scaled tolerances too tight → **X13** before C3b. `leg_count` unmoved → **X16**.

They are two quantities, not two paths to one (L3). The tribunal may prefer one ATR (Open point 6).

**L57.** No receipt change is needed. The consumed set already holds every closed i1 bar of the trade date, premarket included (`evaluate.py:498-500`), so a seeded value replays from the stored receipt.

**First-gate experiment (L70), X1:** see `## First-gate experiments (L70)`. If the share is low, the seed rarely applies, and the earliest windows stay mostly empty. The design does not argue that point; it measures it.

## 6. 9 EMA's CATALYST (E3) — one default, no owner question

`9 EMA Scalp.md:44` requires `catalyst_ref != null`. Cobalt has no catalyst data (G12). The note's own inline comment and the sheet's avoid rule (`9 EMA.pdf` p.2) both allow **catalyst OR setup**.

**Default (key `A-13`, ASSUMED):** the `catalyst_ref` atom is served by an assumed resolver that reads the def's "or setup" branch as met by the name's **radar in-play admission**. The def already requires admission (`InPlay.state == active`, `9 EMA Scalp.md:43`). The atom's outcome is stored as `value_kind=boolean, assumed=A-13`. It is never shown as a detected catalyst. The existing `catalyst` quality dot stays `DESK_NA` / YOURS (`evaluate.py:683-692`). The card carries the ASSUMED chip (§7).

> **[F-13]** The default is kept: three seats ADOPT `A-13` (R1 row 33 HOLDS — it is constant True on the evaluated set; R1B rows 19, 20 HOLD).
>
> **[F-13 · NOT SETTLED → R2-2]** HOW `A-13` is marked is contested: Grok marks it on the atom ("Mark A-13 on the atom, chip on the card"); Fable adds no field ("`AtomOutcome` gains no field") because `AtomOutcome` is a closed model (`seam.py:99-117`, `extra="forbid"` — Fable WF5; single seat, no hub check) and scopes `A-13` to the def's precondition atom, leaving Extension path B (`catalyst_ref_unknown`) untouched. Part of R2-2.

Rejected: a human tap field as the gate. No card could form before he tapped, which contradicts "I need to see the cards before I rule on anything" (R17). The tap stays where it is, on the dot.

## 7. ASSUMED, VISIBLE

> **[F-08 · NOT SETTLED → R2-2]** This whole section stands only for the diff. Two facts about it HOLD and are held by two seats each:
> - The recorder on the interpreter's `cfg` callable misses assumed reads: the trigger's `bars_cleared` and the stop buffer go through `_cfg_value`, the Extension's params through `from_tunables` (R1 row 26 HOLDS; Fable (d); Gemini's "every consulted assumed key is recorded" DOES NOT HOLD, R1B row 9). `A-01`, `A-05`, `A-13` and the other conventions are not `cfg` keys at all.
> - The "existing suppression path" does not carry `assumed_formation`: `suppression()` is a function of dots only and `refresh_card` recomputes `score_suppressed` from dots every scan (R1 row 17 HOLDS; Fable WF2; Gemini's "covers all paths" DOES NOT HOLD, R1B row 8).
>
> The two seats then offer DIFFERENT mechanisms and disagree on whether the other's is correct — Grok: a string persisted on the card row, never overwritten by `refresh_card`, a recorder that wraps every read, the `assumed_keys` column and chip in C2, `A-01` suppressed already in C1; Fable: one tappable `assumed_formation` dot fed by a STATIC declared-key closure, conventions stored as rows, no column, no migration, no `score_card` change — because permanent suppression leaves every card scoreless and WATCH ordered by `pool_position` (L52 (b) in effect). Round 2 answers R2-2. X8 binds whichever mechanism wins.

Nothing new is invented where something exists. Three surfaces are used:

1. **Card face.** Formation records every `cfg(key)` and every assumed resolver it consulted (the interpreter's `cfg` callable, `evaluate.py:601-602`, gets a recorder). The keys whose row is `source: assumed` become `Formation.assumed_keys`. They reach the card as one new `"user".radar_cards_v` column, `assumed_keys` (owner badge **COBALT**, `cards/radar.py:51-68`; the panel's import check, `aset/radar_panel.py:261-263`, forces the badge to be declared). The panel renders it as an `ASSUMED · n` chip that expands to the key list. A card with no assumed key shows no chip. The precedent for an unruled default reaching the card is `DEFAULT_UNRULED` on the alignment dots (`evaluate.py:683-692`). The chip is the same idea, one level up.
2. **Score.** L52(a) wants a modelled number to degrade the score. A card whose formation consulted any ASSUMED key gets `score_suppressed` with the reason `assumed_formation`, through the existing suppression path (the one `trail_fit` uses, ADR-0009 Consequences). The card still appears in WATCH, ordered by the existing tie policy (`evaluate.py:134-138`). Open point 4.
3. **Settings surface.** `cobalt taxonomy tunables --assumed` is a read-only dry-run (L10). It lists every assumed row: key, value, consumers (defs), cards formed on it in the last N sessions, and source page. That is the one table he reads after cards show. The companion file is its first version.

**How a value stops being assumed.** Only by his ruling, through the normal load path (L28, L65). The row's `source` changes from `assumed` to `ruling` (with the value he ruled). The desk makes the edit on his ruling (L65), or he edits the row himself (human wins, L28). The next load clears the chip on new formations. Cards already open keep the `assumed_keys` they formed with (L57: the formation's inputs are immutable).

## 8. WHERE ASSUMED VALUES LIVE (L32 / L53; gap table digest item 12)

> **[F-09 · NOT SETTLED → R2-3]** This section stands only for the diff. What HOLDS about it:
> - The load path as written does not work: the vault loader refuses a tunables row whose scope is not `per_trade(<slug>)` of the note it sits in (`vault_loader.py:271-280` — R1 hub note, claimed blind by Fable WF1), and this note carries `global` rows and rows for other setups. Fable adds (single seat; derive read of `vault_loader.py:327-365`, `:476` agrees, no hub check): every `*.md` in the Strategies folder is read and a note without the def frontmatter, `name:`, the definition section or its def unit RAISES — the note is not "skipped as a non-def".
> - Hole-fill as written widens by scope: `merge_tunables` is key-only, so a per-trade row would fill a global engine key for every def (R1 row 18 HOLDS; R1B row 14).
>
> The two seats offer DIFFERENT stores — Grok: the note stays in the Strategies folder, a new L28 Cobalt command writes the unit, hole-fill only when engine `value is null` AND user `source == assumed` AND scopes equal AND keys equal; Fable: the note moves OUT of the Strategies folder, a dedicated reader loads it, hole-fill only for rows from that reader when the engine `value is None` and units match, scope staying the engine's. Neither wording closes the hole the other names. Round 2 answers R2-3.
>
> WHO writes the note is a reading of law (L65 against R15 / L73), not a design question: Grok — a Cobalt L28 command, "Desk-write is cheaper and unlawful"; Gemini and Fable — the desk, once (Gemini's "obeys L65 strictly" DOES NOT HOLD, R1B row 17b). A law reading is never voted (LAWS preamble). v2's default is the path lawful under every seat's reading — the Cobalt command, +S on C2 — so that nothing is asked of him before cards; see the derive report `## ESCALATE`.
>
> **Production warning carried from Fable ESCALATE 1:** the note must NOT be written into the Strategies folder, by anyone, before a reader that accepts it is deployed.

**Not in committed config.** Committed `tunables.yaml` keeps what it has: engine keys, and for the six sheet-derived holes `value: null` + `status: proposed` (`tunables.yaml:73-210`, convention `:26-27`). The key and unit are anatomy (system, L32). A number read from a cheat sheet or chosen for his setups is user data.

**The store.** A single vault note, `1 - Trading/4 - Strategies/Assumed Defaults.md`. It has no `preconditions:`, so the def loader skips it as a non-def (`vault_loader.py:43-49`). It carries one marker-bounded unit, `tunables:assumed`, in the existing per-trade tunables unit shape (`vault_loader.py:28-41`). Each row has: `key`, `value`, `unit`, `scope` (`global` or `per_trade(<slug>)`), `dynamic: true`, `status: proposed`, `source: assumed`, `sheet_value` (if the sheet has a number), and `consumers`.

**Schema change (system side, S).** `TunableSource` gains `ASSUMED` (`tunables.py:63-66`). *(Common to both seats' stores.)*

**Load path.** The same vault loader pass that loads per-trade units into `"user".tunables` reads this unit (one more unit id). `merge_tunables` (`loader.py:90-112`) gains exactly one rule, **hole-fill**: a user row may supply the value of an engine row whose committed `value` is `null`. Every other collision stays loud, as today. The resolved row carries `source: assumed`, which is what §7 reads.

**Who writes the note.** The CTO desk, once, on R15 ("defaults put in place … assumed"), under L65: smallest diff, before/after in the desk report, a read-only production-parser proof afterwards. The input is the companion file after the tribunal. Cobalt code never writes it. There is no new write path. L65 says the desk never writes "a value he has not ruled", and assumed values are unruled by definition. Whether R15 counts as his direct instruction (L73, a per-case override) is flagged in `reports/setups-design-2026-09-21.md` ESCALATE 7. The fallback is a Cobalt command that writes a Cobalt-owned marked unit under L28. That is a new write path, and it would add about an S to C2.

Rejected: (a) the rows in each def's own `tunables:` unit — seven of his notes edited for values he has not ruled, and assumed rows mixed with ruled ones in the same unit; (b) `"user".trader_settings` via `settings load` — it takes `card.*` keys only (`settings/card.py:72`) and needs his hand on every load; (c) committed `tunables.yaml` — L32/L53.

## 9. ACCEPTANCE THAT WOULD HAVE CAUGHT TODAY'S DEFECT

The defect survived for three reasons (proof report). The fixture was not the real def's shape. The live-note test never asserted `formed` (`test_radar_evaluate.py:692-714`). A replay with `formations=0` was accepted (`deploy-2026-09-19.md:177`). Each gets a gate:

> **[F-21 — OWNER RULING R24, 11:13 ET: "Do not assume days and look alikes. This is not known at the time"]** His trade log is NEVER pass/fail truth — his tags, grades and retro labels are hindsight. In v2, no gate, test or `--expect-formed` day asserts "formed" / "not formed" from a day he traded or tagged, and no "negative / lookalike" fixture is built from his labels. Expected values are written from the DEFINITION evaluated on the bars, by a checker house. His tagged ticker-days may only be REPLAYED to look at the engine beside him (L7 shadow, agreement stats he reads after cards show).

1. **Real-shape formation test, per setup (L45).** Each setup gets a committed test. It writes a neutral note in the real layout with the real def's shape (the proof's pattern: `tests/cobalt/test_rubberband_card_proof.py`, value-free per L32/L45, O7), loads it through `load_vault_trade_defs`, and runs `evaluate_member` on a committed real-shape bars day (ticker and dates stripped) **chosen because the setup forms on it**. It asserts `evaluation == "formed"`, the side, and the geometry guard (§2.3). For Rubberband that is the 4+1 mixed shape on a day its HTF avoid does not cover. **[F-21]** The fixture day is a stored pool day on which the DEFINITION, evaluated on the bars, forms. ~~The fixture day comes from his own tagged trades where bars exist (X2 below). Otherwise it is a stored pool day that a checker house confirms by chart.~~ It is never chosen because he traded or tagged it; its expected values are written per point (1) below.
2. **Registry evaluable ⇒ forms (a property test).** For every def shape in the committed shape corpus, if `evaluability(td).evaluable` is True, that def's formation fixture must form. A def the registry calls evaluable that has no formation fixture fails the suite. So `evaluable` is proven by formation, not by atom presence.
3. **Live-note test fixed.** `test_live_defined_notes_…` asserts `formed` for every def the registry calls evaluable, on its fixture day. The desk runs it with `COBALT_LIVE_VAULT_ROOT` set as a deploy smoke step (proof report ASK DESK).
4. **Replay gate, RED on zero.** `cobalt radar evaluate --replay <day> --trade-def <slug> --expect-formed` exits non-zero when formations == 0 (the count at `evaluate_cli.py:228`). ~~The known days per setup live in a user-side list: his tagged trades (`1 - Trading/2 - Trades`, `trade_def:` frontmatter) where `cobalt_dev` holds the bars.~~ **[F-21]** A known day for a setup is a stored day whose expected values were written from the DEFINITION evaluated on the bars, by a checker house (point (1) below) — never a day he traded or tagged. A chunk's deploy acceptance runs it for every setup that chunk unlocks, and for every setup already live (the smoke covers all delivered functionality, NN#16).
5. **Old receipts.** A receipt written under an older `EVALUATOR_VERSION` (`evaluate.py:132`) is refused loudly by replay, never recomputed with new code. New formation modules join `FORMULA_FILES` (`evaluate.py:144-152`). How replay treats a version mismatch today was not read here, so C1 needs a test for it either way. **[F-19 · X9]** What the hubs read: `replay_receipt` reads no evaluator version (R1 row 24 HOLDS); the nightly formation replay refuses any version outside its allowed set (`replay/formations.py:81,145-148`, `replay/runner.py:219-224` — so Grok's "X7 settled" DOES NOT HOLD, R1 row 25; hub note: a C1 bump of `EVALUATOR_VERSION` meets that check).

> **[F-16]** Fable, (f), word for word — added to the five gates above:
>
> "(1) For each per-setup fixture day, the expected side, formed bar, trigger price and stop price are written by a CHECKER house from the bars alone, before it sees the builder's output; the test asserts all four, not only `formed`. (2) The live-note test is a named command in every chunk's deploy prompt; the hub reads the run's skip report and a SKIPPED result is RED. (3) `--expect-formed` for a setup with no known day exits non-zero; the chunk's deploy report must then carry X3-style evidence for that setup instead. (4) A committed test asserts that the corpus shape of every setup a chunk claims to unlock is `evaluable`. (5) Geometry guard: long → stop < min(trigger, last close); short → stop > max(trigger, last close); else `not_formed: stop_wrong_side`."
>
> Why this wording: it is the only replacement offered for §9 and R24 names it ("a checker house writes the expected values from the def, Fable seat (f)"). Every hole it closes is named by a second seat and HOLDS — the builder-chosen day and the wrong-reason day (Grok (f); Gemini (f), R1B row 21), the skipped live-note test (R1 row 27; R1B row 22), zero tagged days for two setups (R1 row 28), a def the registry stops calling evaluable (Grok (f)), the guard that passed the with-trend control (R1 row 29). That point (5) refuses the proof's with-trend control and none of the formed scans is a single seat's claim → **X17** before C1's guard is final.

## 10. CHUNKS

Every chunk is buildable offline in its own worktree, checked by ≥3 tribunal houses (L67), and deployed on its own evening inside the market_reset pause (L43, L66). Each one unlocks a named setup or removes a named defect. Builder seat by L29: evaluator code that reaches the card, and C2 touches the tunables load path (a DB write path), so the floor is **Opus 5 or GPT-5.6-Sol high** for every chunk. Restarts are derived with `cobalt jobs restarts <range>` (L42). Expected: `src/cobalt/radar/**` → `com.cobalt.radar`. `cards/radar.py` or `aset/**` → also `com.cobalt.aset`. Taxonomy loader → every resident that imports it (the static AST walk decides).

> **[F-18]** Fable, (h), word for word:
>
> "C1 = S logic + M gates; it needs nothing from C2. C3 splits: C3a = D1 indicators + warm-up (removes E7; moves `health`, so it deploys alone and rolls back alone) · C3b = D2 + D3 opening-drive roles + `range_break` + `consolidation_low` (unlocks hitchhiker). Eight deploy evenings; first card still evening 1; all seven evening 8. X5 is re-run as a gate at C3a, C3b, C4, C5, C6 and C7 — at C2 only one def is evaluable and the measurement is nearly empty."
>
> Why this wording: Grok rules the same split in its own words ("C3a D1+warmup (M, unlocks none alone) then C3b D2+D3 hitchhiker (L)") and the same C1 reading ("It does **not** need C2 registries", R1 row 34 HOLDS). Gemini keeps C3 whole ("large but required") and claims nothing against the split. Sizes of C3a / C3b in the table are Grok's.

| # | chunk | unlocks / removes | size | builder (L29) | restarts (L42, expected) | needs from `cobalt_dev` |
|---|---|---|---|---|---|---|
| C1 | Direction from anatomy (§1); `unclassified` setup token **[F-07]**; unbound-direction refusal **[F-02 → R2-1]**; geometry guard (§2.3, §9 (5)) **[F-16 · X17]**; gates 1–5 and points (1)–(5) of §9 for rubberband; the `A-01` mark **[F-08 → R2-2, gates this chunk]** | **rubberband can form** (removes E1 + the order-dependent `setup_ref` label) | S logic + M gates **[F-18]** | Opus 5 / Sol-high | radar | stored pool days for the definition-written fixture **[F-21]** and X3; X9; X17; replay only (a migration only if R2-2 rules a persisted column) |
| C2 | Formation registries (§2.2–2.5) with today's trigger and stop re-registered (byte-identical Rubberband output); mirrored frame (§2.1) **[F-04; F-05 → R2-4]**; interpreter shapes (§4); assumed store + hole-fill + `TunableSource.ASSUMED` (§8) **[F-09 → R2-3]**; the assumed mark on the card and the score (§7) **[F-08 → R2-2]** | removes **E8** (served-but-never-true) and **E9** (under-reported shapes); ASSUMED visible | M | Opus 5 / Sol-high | radar + aset (if R2-2 rules a view column) | X4, X5, X6, X7, X8, X12; the assumed note is written only AFTER its reader ships **[F-09]** |
| C3a **[F-18]** | D1 indicators + warm-up (§5) **[F-10, F-11]** | removes **E7**; moves `health` — deploys alone, rolls back alone | M (Grok) | Opus 5 / Sol-high | radar | X1 before it; X11; X14; X5 re-run |
| C3b **[F-18]** | D2 Range(micro) + D3 opening-drive roles + `range_break` + `consolidation_low` | **hitchhiker** | L (Grok) | Opus 5 / Sol-high | radar | X13, X15 before it; X16; X11; X5 re-run; replay-and-look on his tagged hitchhiker ticker-days **[F-21]** |
| C4 | D4 Extension lifecycle (`reverting`, `backside`) + `indicator_cross` + `measured_fraction` + `recent_higher_low` + `flat`/`between` | **backside**, **fashionably-late** | M | Opus 5 / Sol-high | radar | **X10 before it**; X7; X11; X5 re-run; replay-and-look on his tagged ticker-days **[F-21]** |
| C5 | D3 pullback / impulse / `pre_test` roles + `touched` + `indicator_rejection` + `indicator` stop + catalyst resolver `A-13` **[F-13 → R2-2 for its mark]** + `Extension … on Leg(x)` | **nine-ema-scalp** | M | Opus 5 / Sol-high | radar | X1 decides whether the def's early window is reachable; X11; X5 re-run; replay-and-look **[F-21]** |
| C6 | D5 trendline + `dist` + the level set and `rejected` (`A-17`, `A-18`) | **vwap-continuation** | M | Opus 5 / Sol-high | radar | X11; X5 re-run; replay-and-look **[F-21]** |
| C7 | D6 RangeBreak lifecycle + `retest` / `failed_trap` / `stop_hit` events + `Range(prior)` + `sequence` + `turn_candle` | **second-chance** | M–L | Opus 5 / Sol-high | radar | X7; X11; X5 re-run; replay-and-look **[F-21]** |

**Evenings, stated plainly. [F-18]** 8 chunks = **8 deploy evenings** at one deploy per evening (L43). This is counted from the first evening after the tribunal has closed (round 2 answered for the items that gate the chunk — R2-2 for C1) and C1 has passed its three checkers. Builds and checks of later chunks run in parallel lanes while earlier ones deploy (L72). Code dependencies are strictly C1 → C2 → C3a → C3b → {C4, C5, C6} → C7 (C7 reuses C6's level set). The integrated pre-merge gate applies whenever two land together (L68). **First card possible: evening 1 (rubberband).** Then hitchhiker (evening 4), backside + fashionably-late (5), nine-ema-scalp (6), vwap-continuation (7), second-chance (**evening 8 — all seven**). "Possible" is the honest word: a card also needs the market to produce the setup, and proof ESCALATE 2 says a zero-card day is a likely outcome. Evenings are shared with every other deploy lane, so 8 deploy evenings is not 8 calendar days.

## 11. WHAT I WOULD USE FROM HIS TRADING STATS

The figures that would replace a LOW-confidence assumed value, per setup. They are phrased as one message he can send to his Claude chat, in the report's `## STATS TO ASK HIM FOR`. Summary by key:

| setup | the figure | replaces |
|---|---|---|
| all seven | date + ticker + entry time + side of every trade he tagged with the setup, last 90 days | **[F-21]** ~~the fixture and replay-gate days (§9), not a value, but the most useful ask~~ the ticker-days that may be REPLAYED to look at the engine beside him (L7 shadow; R24) — never a fixture, never a gate day |
| hitchhiker | consolidation length in minutes, and how far price came back from the drive's high before going sideways (share of the drive), on his wins vs losses | `A-07` (and a sanity check of the duration band his note already carries) |
| hitchhiker | how many consolidations he skipped as "choppy", and what they looked like (wicks vs bodies) | `A-02` |
| backside, fashionably-late | minutes from the low of the move to his entry; how far price had come back (share of the move) at entry | `A-08`, `A-09`/`A-10` |
| fashionably-late | whether the 9 EMA was visibly sloping at the cross on his wins; minutes between turn and cross | `A-09`, `A-10`, `A-11` |
| nine-ema-scalp | the share of his 9-EMA trades that had a real news catalyst; entry times relative to the open | `A-13`, `A-05` |
| nine-ema-scalp | the size of the move before the 9-EMA test (in ATRs or %) on wins vs losses | `A-15` |
| vwap-continuation | how far from VWAP the pullback low was at his entries (cents or ATR share) | `A-16` |
| second-chance | bars between break and retest; how close to the level the retest got; which levels he used (PMH, PDH, range top, other) | `A-17`, `A-20` |
| all seven | n, win rate, average R by side (L8: shown only at n ≥ 30) | nothing assumed; it goes next to the cards as his own `reference_stats` |

## L52 (a)–(d)

> **[re-answered for v2]** v2 does not yet clear the bar: (a) and (c) wait on round 2. It is a stepping stone until `## Not settled` is empty (L52, last sentence).

| bar | answer for v2 |
|---|---|
| (a) every number traceable or marked modelled, degrading the score | **NOT MET until R2-2 closes.** Inputs are stored i1 bars, daily bars and pool rows, retained by the receipt (`evaluate.py:498-512`, ADR-0009 D3) — that half holds. The marking half does not: as the proposal stands, `A-01` and the other conventions, every assumed row read through `_cfg_value` / `from_tunables`, and the resolver outcomes `A-05` / `A-13` reach a trigger, stop and `proximity` unmarked, and an open card can regain a score on refresh (R1 rows 17, 26 HOLD; R1B rows 8, 9; Fable (c)(a), (d); both hubs' ESCALATE 3). Two mechanisms are offered and contested (R2-2); X8 binds the winner. Every argument about data behaviour is an experiment (X1–X17), never text. |
| (b) exactly ONE ranking authority reaches the card | `card_score` (ADR-0009 D4) — three seats (Grok (c)(b) ADOPT; R1B rows 12, 13 HOLD; Fable). Formation, side binding and the `both_sides` refusal add no rank. OPEN inside R2-2: Fable holds that a suppression that never lifts leaves WATCH ordered by `pool_position` for every card, a second authority in effect; Grok and Gemini hold the tie policy is enough. |
| (c) the integration seam as a real artifact | **PARTLY.** Specified in v2: the Frame and its acceptance property (F-04), `atr_seeded` beside the unchanged `atr_working` (F-10), the `UNCLASSIFIED_SETUP` constant outside `SetupRef` (F-07), the §9 gates (F-16, F-21). NOT yet artifacts: `TriggerOutcome`, `StopOutcome`, `assumed_keys`, `assumed_formation` exist nowhere in `src/` (R1B row 10), and their shape waits on R2-2 / R2-3. The proposal's "`RadarScoreDetail` (unchanged schema …)" is contested by one seat: `seam.UnavailableReason` is a closed Literal, so a new reason such as `insufficient_seed` fails validation (Fable (c); no hub check) → X11 before C3a. Grok's list of seams "named as artifacts in the chunk that adds them" is not taken whole because it names the contested ones. |
| (d) auditable by another house | HOLDS — three seats. `cobalt radar audit-export` and `replay_receipt` exist (R1B row 11 HOLDS); Grok's two conditions are already the proposal's (assumed rows in the tunables snapshot the receipt stores; new modules join `FORMULA_FILES`). Every chunk is checked by ≥3 houses other than the builder (L67). The frame property and the per-setup fixtures need no DB. |

## First-gate experiments (L70)

Run on `cobalt_dev` before the chunk each one gates; never argued. X1–X5 are the proposal's; the rest are the houses' or the hubs' unrun checks. Each text is its source's, word for word; only the numbering is v2's.

| # | source (its own label) | before / in | the run | result that would change the design |
|---|---|---|---|---|
| X1 | proposal X1; Fable X1 (text) | before C3a | "on `cobalt_dev`, last 10 stored sessions, the share of pool names with at least `period` complete premarket working buckets by 09:30, for periods 9, 14 and 21." | Fable: "Low share → the seed rarely applies, the early windows stay empty, and C3a's value is mostly the fallback." Grok: "do not drop the seed, report the rate." |
| X2 | proposal X2, re-scoped by R24 **[F-21]** | before any replay-and-look | whether `cobalt_dev` holds i1 for his tagged ticker-days | Coverage only. It no longer chooses a fixture or a gate day: none is chosen because he traded or tagged it (R24). |
| X3 | proposal X3; Fable X3 (text) | C1 acceptance | "`--replay` of rubberband over the last 10 stored sessions after the C1 change: formations > 0 somewhere; AND for each formation, side and minutes between the culminating bar and the scan." | Fable: "Many formations long after their culminating bar → sticky culmination (`extension.py:123-139`) needs a freshness bound before cards are enabled for that def." Grok: "Zero is allowed (proof ESCALATE 2) and is not a C1 defect." |
| X4 | proposal X4; Grok X4 (text); R1 row 15; Fable X4 (sweep) | C2 | Grok: "O2 property, detector by detector, on stored days. A fail that is only the old property test is not a defect." Hub: "`_on_ten_cent_grid` on `Decimal('-10.00')` and `Decimal('-10.04')`." Fable: "`structural_stop` swept over the cent grid on negated extremes (Python `Decimal` remainder and negative zero)." | Fable: "Any inequality → that item gets a side-explicit implementation and is named as the exception." |
| X5 | proposal X5; Grok X5; Fable X5 | C2, re-run at C3a, C3b, C4, C5, C6, C7 **[F-18]** | Grok: "time 7 defs × 2 frames × 50 members on `cobalt_dev` against a 100 s budget" (7×2×50 = 700, R1 row 31a ARITHMETIC OK; Gemini's `100T` is wrong at the evaluations-per-scan step, R1B row 23a). Fable: "wall-clock of `EvaluateStage.run`, 50-member pool, last RTH scan of a stored day." | Grok: "p95 over 100 s → sequential frames or a smaller pool during C2, never silent miss." Fable: "Over budget → Frames are built lazily, the mirrored side only for a def whose long frame did not form." *(Derive note, not a house's: a lazily built second frame cannot observe `both_sides` — read X7 first.)* |
| X6 | Grok X6; Gemini X6 | C2 Frame | Grok: "construct mirrored i1 as archiver `Bar`." Gemini: "Instantiate `cobalt.archiver.models.Bar` with a negative price on `cobalt_dev`." (Field level: OHLC unconstrained, R1 row 14; a DB-level CHECK is unread, R1B row 5.) | Grok: "Frame must wrap `WorkingBar` only, never round-trip through `Bar`." Gemini: "the mirrored frame will require a shadow model". |
| X7 | Fable X7 | C2, repeated at C4 and C7 | "the count of scans where BOTH frames satisfy a def's preconditions, per def, last 10 sessions." | "Non-zero for any def → read those scans; a stale instance on one side hiding a fresh one on the other would turn the blanket `both_sides` refusal into 'the later anchor wins'." |
| X8 | Grok X8 | C2 (binds the R2-2 winner) | "after C2, form a card on an assumed key, then change that row's `source` to `ruling`; assert the open card still has `score_suppressed=assumed_formation`." | The open card gains a score → the mark must survive a refresh (R1 row 17). |
| X9 | Fable X8 (Grok's "X7 … settled" not taken: R1 row 25 DOES NOT HOLD) | C1 | "replay a receipt written under the current `EVALUATOR_VERSION` with C1's code." | "If it recomputes instead of refusing, gate 5 is a build item in C1, not only a test." |
| X10 | R1 row 7b (hub's run); Grok (a); Fable O1 scenario 2 | **before C4** | Hub: "evaluate a backside fixture with last > open once D4 exists." | The card forms on the wrong side, or never forms → `A-01` is not applied to the D4 states as §1 words it. The two offered fixes: Grok — "they bind side only through the mirrored frame on their own long-side text"; Fable — "the Extension's direction is stamped at its culminating bar and held through `reverting` / `backside`; it is never recomputed from `last_close − session_open`." |
| X11 | Fable X9 | before C3a (its (c) scenario names C3a's `insufficient_seed`) and each later chunk (its own text: "each chunk from C3b") | "for every atom the newly unlocked def consults, construct its `AtomOutcome` through `seam.validate_atom` with every declared reason." | "Any failure or collapse to `unspecified_atom` → the atom's spelling or the closed reason list changes before deploy." |
| X12 | from Fable O2's failing scenario (card field `why`) | C2 | form a card from the mirrored frame on a stored day; read `why`, `extreme`, `raw`, `rounded`, `inputs` and every level label | A negative price or a long-side label on a short card → per-type un-mirroring before `Formation` (Fable O2), not only the two typed prices. |
| X13 | Fable X6 | before C3b | "on stored sessions, the ratio `atr_seeded` / RTH-only ATR at 09:40, 09:50 and 10:00, and the count of Range(micro) instantiations inside the `open_drive` sub-window (taxonomy `:79`) under each." | "Median ratio well under 1 → early ATR-scaled tolerances need an RTH-weighted ATR, and `A-05` changes for ATR while staying for the EMAs." |
| X14 | R1B row 7b (hub's run) | C3a | Hub: "C3 build + replay of a FILLED card." | A number other than `health` moves → C3a's deploy note (F-10) is wrong and the chunk does not deploy. |
| X15 | R1 row 32b / R1B row 18 (hubs' run) | before C3b | Hub: "evaluate hitchhiker on stored drive-then-range days under both readings." | The literal reading forms → `A-07` is not needed as worded (Grok "almost never", Gemini "impossible" are both unrun). |
| X16 | from Fable O7's failing scenario | C3b | replay stored Rubberband receipts after D3 lands; compare `Extension.leg_count` | Any difference → Fable O7: "`leg.legs()` (`leg.py:42-67`) is unchanged, byte-identical. Roles and `terminated_by` are a separate function over its output plus the Range(micro) observation." |
| X17 | from Fable (f)'s WRONG FACT 6 claim | C1, before the guard is final | run §9 point (5) against the proof's two controls (`test_rubberband_card_proof.py`) | It does not refuse the with-trend control, or it refuses a formed scan of the single-relation control → point (5) is not the guard; §2.3's stop-versus-trigger condition stands alone. |

## L11 — the human-only variable each setup keeps

| setup | human-only variable (name) | note:line |
|---|---|---|
| rubberband | text avoid (news against the trade) + `setup_relation` tap | `Rubberband.md:87`, `:101` |
| hitchhiker | text avoid (consolidation far beyond the band) | `Hitchhiker.md:70` |
| backside | factor `price_action_consistency` | `Backside Scalp.md:134` |
| second-chance | factor `level_significance` | `Second Chance Scalp.md:155` |
| fashionably-late | factor `volume_convergence_vs_divergence` | `Fashionably Late.md:68` |
| nine-ema-scalp | `bids_hold` (`frontier: true`) | `9 EMA Scalp.md:87` |
| vwap-continuation | text avoid (opening auction choppy) | `VWAP Continuation.md:80` |

Only `nine-ema-scalp` marks its variable `frontier: true` (gap table E11). This design computes none of the others and renders them YOURS. Marking them explicitly is a note edit, so it is his (L65), not proposed here. *(Owner item after cards — Grok, Fable.)*

## What this does NOT do

- It edits none of his notes, and proposes no edit to them (L65). The divergences between notes and sheets are reported only (gap table E10, plus one more in the report's ESCALATE).
- It detects no Setup (gap / day-2 / overextension / volatility-in-range); the card says `unclassified`.
- It adds no catalyst, breadth or regime data, and builds no Gap, volatility_state or Regime detectors.
- It changes nothing in `card_score`, conviction, proximity, the curves or the dots **[F-08 → R2-2: both offered `A-01` marks touch this sentence — one stores a suppression string `score_card` does not compute, the other adds a dot and a `NaReason`]**. It promotes nothing: cards stay advisory beside his hand grade, in the L7 shadow.
- It writes nothing to `"user".trader_settings`, and makes no Finviz or pool change.
- It does not tune: every assumed value stays assumed until he rules (R15, R17).
- **[F-21]** It asserts nothing from his trade log: no fixture, gate or lookalike comes from a day he traded, tagged, graded or labelled (R24).
- The other six definitions are out of scope, and nothing here must be torn up for them (§2.5).
- No build, no launch, no commit by this seat.

## Open to the tribunal — as round 1 left each point

1. **Direction from anatomy (`A-01`), not from a setup classifier.** Three seats keep it for `rubberband` (F-01). Beyond rubberband → X10 (F-03). The unbound refusal → R2-1 (F-02). "for these defs every setup gives the same side" is Grok's WRONG FACT 3 and Fable's (a) reading, unsettled → X10.
2. **Mirrored frame for side binding.** Kept by three seats, with Grok's acceptance property (F-04). Fable's additions → R2-4, X12 (F-05).
3. **`setup_ref = unclassified` token instead of a nullable column.** Kept by three seats as a constant outside `SetupRef` (F-07). The stated reason (a nullable column "would add a migration") is contested by Fable WF3 — the column is already nullable — single seat, not checked, and the decision does not turn on it.
4. **Score suppressed on any assumed formation.** → R2-2 (F-08).
5. **One vault note for assumed values, with a hole-fill merge rule.** → R2-3 (F-09). The tribunal did check that hole-fill can widen: it can, by scope (R1 row 18 HOLDS).
6. **Premarket-seeded EMA/ATR next to the Extension's own RTH ATR.** Kept, renamed: `atr_working` stays the Extension's, the seeded one is `atr_seeded` (F-10); `health` moves, stated at deploy (F-11). One ATR or two is an owner item after cards (Grok).
7. **Opening-drive termination: consolidation before pullback (`A-07`).** Kept by three seats; Gemini's replacement wording is this point's own sentence ("When a micro-Range instantiates from the drive's extreme within a bounded retrace, the termination is consolidation.") (F-12). Whether the literal reading really never forms → X15. Whether it amends the taxonomy is his, after cards.
8. **9-EMA catalyst via in-play admission (`A-13`).** Kept by three seats (F-13); how it is marked → R2-2.

## Dissents, verbatim

No house issued a `REJECT` or a `DO NOT BUILD` in round 1 (R1 hub: "No `DO NOT BUILD`, no `REJECT`"; R1B hub: the same; Fable: "reject 0"). Closing lines, for the record: Grok — `TRIBUNAL R1: BUILD AFTER scoped A-01, atr name, hole-fill, assumed persist`; Gemini — `TRIBUNAL R1: BUILD`; Fable — `BUILD AFTER the derive folds the O4, O5, (d) and seam-reason replacements; C1 unblocked`.

Where v2 does not follow a house's `ADOPT WITH` wording, that wording is quoted whole, beside the other house's, in the derive report `## NEEDS ROUND 2` (Grok O1, O4, O5; Fable O1, O2, O4, O5, O8, (c), (d), (e)) — carried, never settled by count (L37). Grok's O6 text and its (c) seam list are not taken for the reasons in the fold table (F-10, F-14). Fable's "C1 unblocked" is NOT followed by v2: R2-2 gates C1 (F-08).
