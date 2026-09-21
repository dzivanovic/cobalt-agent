# Setups at defaults — design PROPOSAL — 2026-09-21

Proposing house: Opus 5, seat `setups-design-0921` (L67: one house proposes; the four-house tribunal rules on this and derives the final version — **nothing is built from this file**). Prompt: `docs/40 - DevDocs/prompts/2026-09-21/21-propose-setups-design.md`. His rulings: `docs/40 - DevDocs/reports/cto-2026-09-21.md` §4 R15, R17, R18.

**Scope.** The seven setups on his short list (R18), in the slugs his notes use: `rubberband`, `hitchhiker`, `backside`, `second-chance`, `fashionably-late`, `nine-ema-scalp`, `vwap-continuation`. The other six definitions are out of scope, but every mechanism here is a registry they plug into without a refactor (§2, §3).

**L32 rule for this file.** It carries no value, quote or wording from his notes or the cheat sheets. It cites his notes by `file:line` (all under `/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies/`), the cheat sheets by `docs/90 - References/<file>.pdf` page, and every assumed value by KEY (`A-01` … `A-23`). The values, sources, quotes and confidence levels are in the gitignored companion `docs/_inflight/setups-assumed-values-2026-09-21.md`.

**Fact base (read, not redone).** `docs/_inflight/defs-gap-table-2026-09-21.md` (gap table: G1–G13, D-1…D-16, E1–E11); `~/cobalt-wt/rubberband-proof/docs/40 - DevDocs/reports/rubberband-card-proof-2026-09-21.md` (the proof); ADR-0009; the code on `main` at `0cf4b82`.

---

## 1. DIRECTION — Rubberband first, its own deployable chunk

### What is wrong (proven)

`evaluate.py:635-645` reads a def's `valid_setups[].relation` as the relation between the trade and the **Extension**: all countertrend → trade against the run, all with_trend → trade with it, mixed → `not_evaluable: Setup(relation)`. `Rubberband.md:36-41` mixes both. The proof ran it: 71 of 71 scans where a single-relation control forms come back `not_evaluable` (proof report, test A). `setup_ref` is then the first listed entry with that relation (`evaluate.py:647`) — a label that depends on list order, not a detection.

### Why it is wrong (the root cause, not just the symptom)

`relation` is the relation between the trade and the **setup's** trend (the day or higher-timeframe context: a gap, a day-2 trend, an overextension). It is not the relation to the intraday Extension. Three facts, each readable:

1. The schema puts `relation` on the setup entry: `valid_setups[]: {setup_ref, relation}` (`TAXONOMY-DRAFT-v0_7.md:136`). The trade's direction is a separate field, `instance_direction: computed from setup-instance state` (`:137`; also `:124`, "every trade_def side-symmetric").
2. Rubberband's trigger and stop only make sense AGAINST the Extension. The stop ref is `snapback_candle` (`Rubberband.md:53`), which the taxonomy defines as the current tracked extreme of the move (`TAXONOMY-DRAFT-v0_7.md:110`; sheet reading law (b), `:62`). A stop just beyond the extreme of a move protects a trade against that move. With the move, the extreme is ahead of price, not behind it. The proof's own with-trend control shows this: a long on an up-run gets its stop placed from the run's high (proof report, "With-trend geometry"; `structure.py:70-79`, `:100-116`).
3. The cheat sheet describes one trade shape and its inverse only (`the_rubberband_scalp_cheat_sheet.pdf` p.1, entry and stop rules). The same holds for `backside` (`back$ide_cheat_sheet.pdf` p.1) and `fashionably-late` (`the_fashionably_late_scalp_cheat_sheet.pdf` p.1). In each case, every one of the def's five setup entries (`Rubberband.md:37-41`, `Backside Scalp.md:90-94`, `Fashionably Late.md:32-36`) resolves to the same side: against the Extension. The with_trend `day2_continuation` entry is with the *day-2* trend and still against the intraday Extension.

So S2-P2 made a category error: it read a setup-context field as a direction field. That is how a def "that will never show up" was built and shipped green. The proof explains why the suite never saw it (proof report, "Why the S2-P2 suite and the 09-19 replay were green").

### The mechanism (simplest correct)

**Direction comes from the trade's own anatomy. `relation` is never read for direction.**

- **Orientation rule (key `A-01`).** In a def written long-side (`TAXONOMY-DRAFT-v0_7.md:89`, "trade_defs written long-side"), an unqualified `Extension` is the Extension the long trade opposes, so its direction is down. `Extension … on Leg(x)` is the Extension of that leg, whatever its direction. For chunk 1 this reduces to one line, `trade_direction = against ext.direction`. That is today's countertrend branch (`evaluate.py:636-637`), applied to every def whose precondition anchor is an unqualified Extension. §2 generalises it with the mirrored frame.
- **Setup identity is NOT detected in this design.** No detector for gap / day-2 / overextension / volatility-in-range exists or is proposed. The card shows `setup_ref = unclassified`. The existing human quality factor `setup_relation` (`Rubberband.md:101`, a tap in `evaluate_cli.py:35`) carries his read. The order-dependent label (`evaluate.py:647`) is deleted, not replaced by another guess.
- **Neither side qualifies → `not_formed`** (unchanged). **Both sides qualify on the same scan → `not_formed`, note `both_sides`.** This is counted on the board and never a guess. For chunk 1 it cannot happen, because the Extension has exactly one direction (`extension.py:96-103`). In §2 it can, and it stays refused.
- **A def whose side cannot be bound is refused.** If a def names neither an oriented object nor `trade_direction`, the registry reports it `not_evaluable: Direction(unbound)`, named in the dry-run. It never forms.

**What the card shows.** `direction` (COBALT, unchanged). `setup_ref = unclassified` (COBALT, the literal token). `why` is unchanged in shape (`evaluate.py:674-680`) with the setup token first. The `setup_relation` dot stays YOURS.

**Files.** `src/cobalt/radar/evaluate.py` (`:34-37` docstring, `:635-647` gate + label). `EVALUATOR_VERSION` is bumped (`:132`). `src/cobalt/radar/anatomy/registry.py` gets the unbound-direction check. Tests: see §9. No schema, migration, card column, vault or config change.

**Cost, priced honestly.** Size S: about 20 lines of logic, plus the tests of §9, which are most of the work. Risk: the direction of every Rubberband card now rests on `A-01`, a reading of the taxonomy and sheets and not a ruling. Its confidence is HIGH in the companion, and it is Open point 1. The second gate (the def's own day-1 HTF avoid, `Rubberband.md:86`) stays and is correct. A fixed Rubberband still forms no card on a day that avoid covers (proof ESCALATE 2).

## 2. THE FORMATION STAGE, generalised (gap table E2)

Today formation is hard-wired to one shape: the Extension's culminating bar, a `bar_break{bars_cleared}` trigger and the tracked-extreme stop, enforced by `assert`s (`evaluate.py:633-671`, `:649-651`). The seven need 6 trigger shapes and 6 stop placements (the list below). The design turns formation into **three registries of resolvers, keyed by the def's own data**, plus one side-binding step. Nothing is keyed by trade name (L31/L32, as `registry.py:5-8` already requires).

### 2.1 Side binding — the mirrored frame

Every def is evaluated twice, once per side, on a **Frame** (§3):

- **long** = the frame built on the stored bars;
- **short** = the same frame built on the **mirrored** bars (price → −price, high ↔ low; volume and time unchanged).

Every detector runs unchanged on both frames. Every def is read as its long-side text (`TAXONOMY-DRAFT-v0_7.md:89`, `:124`; each of the seven sheets says the short side is the inverse). Examples: `EMA9.slope > 0`, `Range(micro).low > EMA9`, `Range(micro).bound`, `recent_higher_low` and `a_crosses_above_b` all mean the right thing on the short side with no side-specific code. `trade_direction` is bound to `long` in both frames: it means "the side this frame trades". `opposite(trade_direction)` and `Leg(…).direction == trade_direction` compare against the frame's own `up`. A def forms on side s only when its preconditions are True, no avoid is True, and trigger and stop both resolve on frame s. A price read from the mirrored frame is negated back before it reaches the Formation.

Why this and not side-aware detectors: one pure transform and one property test (detector(mirror(bars)) == mirror(detector(bars))) replace a long/short branch in every detector. The cost is CPU, not code: every def is evaluated twice. First-gate experiment X5 (§ L52 table) measures the latency.

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

**Geometry guard (new, fail-loud).** A resolved stop that is not on the protective side of the trigger (long: stop < trigger; short: stop > trigger) gives `not_formed`, note `stop_wrong_side`, never a card. This guard alone would have turned the with-trend Rubberband card of the proof's control into a refusal.

### 2.4 The Formation model

`Formation` (`evaluate.py:324-336`) is generalised. `extension_direction` becomes `anchor {object, direction, bar_ts}`. `trigger` becomes the `TriggerOutcome`. `extreme` becomes optional. `stop` gains `placement` and `inputs`. `setup_ref` is kept (the token `unclassified` in this design). New: `side_frame: long | mirrored` and `assumed_keys: tuple[str, ...]` (§7). `card_why` (`evaluate.py:674-680`) is assembled from the resolvers' `why` fragments. No resolver writes prose from his notes (L32).

### 2.5 One path for "what is served" (fixes E8 and E9)

`registry.evaluability` stops keeping its own constants (`registry.py:27-38`). It reads `TRIGGERS`, `STOPS`, `STRUCTURAL_REFS`, `ATOMS` and `RELATIONS` (§3, §4): the same tables formation dispatches through (L3). Each atom resolver also declares its **producible value domain**. A precondition that compares a symbol atom to a literal outside that domain is `not_evaluable: <atom>∌<value>`. Example: `Extension.state IN {reverting, backside}` while the detector produces only `culminating | none` (`extension.py:70`). So the registry can no longer report served-but-never-true (E8). Every AST shape the interpreter cannot evaluate is also named in `missing` (E9), because `evaluability` walks the AST through the same dispatch the interpreter uses.

**Extension without refactor.** A future trigger (`bar_break{ref: Level_ref(open)}` for the other six, a swing `daily_close_break`, an options `iv_cross`) is one resolver plus one registry row. It declares its own `serves()` and domain. The stage, the registry and the card are untouched.

## 3. THE DETECTOR GROUPS the seven need — build order by setups per unit of size

All inputs are stored today: i1 04:00→19:59 ET (`cto-2026-09-20.md:23-24`, gap table), the daily series (`daily.py`) and the pool row (`radar/runner.py:139-142`). No new data source. Each detector is PURE (bars in, typed observation out) and emits typed atoms with a declared domain.

**The Frame** (`src/cobalt/radar/anatomy/frame.py`, new) is built once per (member, scan, side). It holds the RTH run (as today), the warm series (§5), the indicators, and every detector's observation. `evaluate_member` asks the frame for atoms and never runs detectors itself.

| # | group (gap table) | atoms / refs (typed events) | inputs | unlocks (with earlier groups) | size |
|---|---|---|---|---|---|
| D0 | Direction (G1, §1) | `trade_direction`, `opposite(…)`, orientation `A-01` | the frame side | rubberband | S |
| D1 | Shared indicators + session levels (G3 part, G8) | `price`, `EMA9`, `EMA21`, `EMA9.slope`, `slope_norm(x)` (`A-11`), `flat(x, window)` (`A-09`, `A-10`), `VWAP` (`A-12`), `ATR(working_tf)` (seeded, `A-05`, §5), `DayRange`, `DayRange.upper_third` (`A-06`), `PMH/PML/PDH/PDL`, `InPlay.state` (pool admission, `evaluate.py:320`) | warm series + RTH run + daily | none alone (shared) | M |
| D2 | Range(micro) + pivots (G5) | `Range(micro).{instantiated, duration, low, top, base, bound, height, wick_ratio}`, `bound_type` (diverging = no Range), pivot highs/lows `cfg(pivot.n)`, refs `consolidation_low`, `recent_higher_low` | RTH run, `A-02`, `A-03`, `A-04` | hitchhiker (with D1, D3) | L |
| D3 | Leg roles (G4) | `Leg(opening_drive).{direction, terminated_by}`, `Leg(impulse)`, `Leg(pullback).{direction, end, index}`, `Leg(pre_test)` (`A-14`), relation `touched` | RTH run + D2 (for `terminated_by: consolidation`, `A-07`) | hitchhiker; nine-ema-scalp (with D1) | M |
| D4 | Extension lifecycle (G10, E8) | `Extension.state` domain grows to `building \| extending \| culminating \| reverting \| backside \| resuming \| none` (`TAXONOMY-DRAFT-v0_4.md:32`); `reverting` from the snapback rule `A-08`; `backside` from ≥`cfg(extension.backside_hh_min)` HH and ≥`cfg(extension.backside_hl_min)` HL above a rising EMA9 (`TAXONOMY-DRAFT-v0_7.md:98`); `Extension.instantiated on Leg(x)` (`A-15`); refs `turn_low`, `turn` | RTH run, D1 EMA9, D2 pivots | backside (with D2), fashionably-late (with D1) | M |
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
- **warm** = working bars from the premarket (04:00) through now. It is used ONLY to seed the rolling indicators `EMA9`, `EMA21` and `ATR(working_tf)`. The first RTH value of each is the continuation of its premarket-seeded series. Premarket buckets with no print are absent, and incomplete ones are flagged (`bars.py:13-17`). The seed uses only complete premarket buckets. With fewer than `period` of them, the indicator is `unavailable: insufficient_seed` and falls back to the RTH-only warm-up (later, never guessed).

**What it does to "RTH bars only".** Nothing, for anything that already exists. The Extension keeps its own RTH-run ATR (`extension.py:112`) as a distinct, named quantity (`atr_run`). So Rubberband's numbers, and the `atrs_from_open` factor (`evaluate.py:438-445`), do not move. The seeded ATR is a new quantity with its own name (`atr_working`) and its own consumers (tolerances, `dist`, slopes). They are two quantities, not two paths to one (L3). The tribunal may prefer one ATR (Open point 6).

**L57.** No receipt change is needed. The consumed set already holds every closed i1 bar of the trade date, premarket included (`evaluate.py:498-500`), so a seeded value replays from the stored receipt.

**First-gate experiment (L70), X1:** the share of pool names whose premarket has ≥ `period` complete 2m buckets by 09:30, measured on `cobalt_dev` over the last 10 stored sessions. If it is low, the seed rarely applies, and the earliest windows stay mostly empty. The design does not argue that point; it measures it.

## 6. 9 EMA's CATALYST (E3) — one default, no owner question

`9 EMA Scalp.md:44` requires `catalyst_ref != null`. Cobalt has no catalyst data (G12). The note's own inline comment and the sheet's avoid rule (`9 EMA.pdf` p.2) both allow **catalyst OR setup**.

**Default (key `A-13`, ASSUMED):** the `catalyst_ref` atom is served by an assumed resolver that reads the def's "or setup" branch as met by the name's **radar in-play admission**. The def already requires admission (`InPlay.state == active`, `9 EMA Scalp.md:43`). The atom's outcome is stored as `value_kind=boolean, assumed=A-13`. It is never shown as a detected catalyst. The existing `catalyst` quality dot stays `DESK_NA` / YOURS (`evaluate.py:683-692`). The card carries the ASSUMED chip (§7).

Rejected: a human tap field as the gate. No card could form before he tapped, which contradicts "I need to see the cards before I rule on anything" (R17). The tap stays where it is, on the dot.

## 7. ASSUMED, VISIBLE

Nothing new is invented where something exists. Three surfaces are used:

1. **Card face.** Formation records every `cfg(key)` and every assumed resolver it consulted (the interpreter's `cfg` callable, `evaluate.py:601-602`, gets a recorder). The keys whose row is `source: assumed` become `Formation.assumed_keys`. They reach the card as one new `"user".radar_cards_v` column, `assumed_keys` (owner badge **COBALT**, `cards/radar.py:51-68`; the panel's import check, `aset/radar_panel.py:261-263`, forces the badge to be declared). The panel renders it as an `ASSUMED · n` chip that expands to the key list. A card with no assumed key shows no chip. The precedent for an unruled default reaching the card is `DEFAULT_UNRULED` on the alignment dots (`evaluate.py:683-692`). The chip is the same idea, one level up.
2. **Score.** L52(a) wants a modelled number to degrade the score. A card whose formation consulted any ASSUMED key gets `score_suppressed` with the reason `assumed_formation`, through the existing suppression path (the one `trail_fit` uses, ADR-0009 Consequences). The card still appears in WATCH, ordered by the existing tie policy (`evaluate.py:134-138`). Open point 4.
3. **Settings surface.** `cobalt taxonomy tunables --assumed` is a read-only dry-run (L10). It lists every assumed row: key, value, consumers (defs), cards formed on it in the last N sessions, and source page. That is the one table he reads after cards show. The companion file is its first version.

**How a value stops being assumed.** Only by his ruling, through the normal load path (L28, L65). The row's `source` changes from `assumed` to `ruling` (with the value he ruled). The desk makes the edit on his ruling (L65), or he edits the row himself (human wins, L28). The next load clears the chip on new formations. Cards already open keep the `assumed_keys` they formed with (L57: the formation's inputs are immutable).

## 8. WHERE ASSUMED VALUES LIVE (L32 / L53; gap table digest item 12)

**Not in committed config.** Committed `tunables.yaml` keeps what it has: engine keys, and for the six sheet-derived holes `value: null` + `status: proposed` (`tunables.yaml:73-210`, convention `:26-27`). The key and unit are anatomy (system, L32). A number read from a cheat sheet or chosen for his setups is user data.

**The store.** A single vault note, `1 - Trading/4 - Strategies/Assumed Defaults.md`. It has no `preconditions:`, so the def loader skips it as a non-def (`vault_loader.py:43-49`). It carries one marker-bounded unit, `tunables:assumed`, in the existing per-trade tunables unit shape (`vault_loader.py:28-41`). Each row has: `key`, `value`, `unit`, `scope` (`global` or `per_trade(<slug>)`), `dynamic: true`, `status: proposed`, `source: assumed`, `sheet_value` (if the sheet has a number), and `consumers`.

**Schema change (system side, S).** `TunableSource` gains `ASSUMED` (`tunables.py:63-66`).

**Load path.** The same vault loader pass that loads per-trade units into `"user".tunables` reads this unit (one more unit id). `merge_tunables` (`loader.py:90-112`) gains exactly one rule, **hole-fill**: a user row may supply the value of an engine row whose committed `value` is `null`. Every other collision stays loud, as today. The resolved row carries `source: assumed`, which is what §7 reads.

**Who writes the note.** The CTO desk, once, on R15 ("defaults put in place … assumed"), under L65: smallest diff, before/after in the desk report, a read-only production-parser proof afterwards. The input is the companion file after the tribunal. Cobalt code never writes it. There is no new write path. L65 says the desk never writes "a value he has not ruled", and assumed values are unruled by definition. Whether R15 counts as his direct instruction (L73, a per-case override) is flagged in `reports/setups-design-2026-09-21.md` ESCALATE 7. The fallback is a Cobalt command that writes a Cobalt-owned marked unit under L28. That is a new write path, and it would add about an S to C2.

Rejected: (a) the rows in each def's own `tunables:` unit — seven of his notes edited for values he has not ruled, and assumed rows mixed with ruled ones in the same unit; (b) `"user".trader_settings` via `settings load` — it takes `card.*` keys only (`settings/card.py:72`) and needs his hand on every load; (c) committed `tunables.yaml` — L32/L53.

## 9. ACCEPTANCE THAT WOULD HAVE CAUGHT TODAY'S DEFECT

The defect survived for three reasons (proof report). The fixture was not the real def's shape. The live-note test never asserted `formed` (`test_radar_evaluate.py:692-714`). A replay with `formations=0` was accepted (`deploy-2026-09-19.md:177`). Each gets a gate:

1. **Real-shape formation test, per setup (L45).** Each setup gets a committed test. It writes a neutral note in the real layout with the real def's shape (the proof's pattern: `tests/cobalt/test_rubberband_card_proof.py`, value-free per L32/L45, O7), loads it through `load_vault_trade_defs`, and runs `evaluate_member` on a committed real-shape bars day (ticker and dates stripped) **chosen because the setup forms on it**. It asserts `evaluation == "formed"`, the side, and the geometry guard (§2.3). For Rubberband that is the 4+1 mixed shape on a day its HTF avoid does not cover. The fixture day comes from his own tagged trades where bars exist (X2 below). Otherwise it is a stored pool day that a checker house confirms by chart.
2. **Registry evaluable ⇒ forms (a property test).** For every def shape in the committed shape corpus, if `evaluability(td).evaluable` is True, that def's formation fixture must form. A def the registry calls evaluable that has no formation fixture fails the suite. So `evaluable` is proven by formation, not by atom presence.
3. **Live-note test fixed.** `test_live_defined_notes_…` asserts `formed` for every def the registry calls evaluable, on its fixture day. The desk runs it with `COBALT_LIVE_VAULT_ROOT` set as a deploy smoke step (proof report ASK DESK).
4. **Replay gate, RED on zero.** `cobalt radar evaluate --replay <day> --trade-def <slug> --expect-formed` exits non-zero when formations == 0 (the count at `evaluate_cli.py:228`). The known days per setup live in a user-side list: his tagged trades (`1 - Trading/2 - Trades`, `trade_def:` frontmatter) where `cobalt_dev` holds the bars. A chunk's deploy acceptance runs it for every setup that chunk unlocks, and for every setup already live (the smoke covers all delivered functionality, NN#16).
5. **Old receipts.** A receipt written under an older `EVALUATOR_VERSION` (`evaluate.py:132`) is refused loudly by replay, never recomputed with new code. New formation modules join `FORMULA_FILES` (`evaluate.py:144-152`). How replay treats a version mismatch today was not read here, so C1 needs a test for it either way.

## 10. CHUNKS

Every chunk is buildable offline in its own worktree, checked by ≥3 tribunal houses (L67), and deployed on its own evening inside the market_reset pause (L43, L66). Each one unlocks a named setup or removes a named defect. Builder seat by L29: evaluator code that reaches the card, and C2 touches the tunables load path (a DB write path), so the floor is **Opus 5 or GPT-5.6-Sol high** for every chunk. Restarts are derived with `cobalt jobs restarts <range>` (L42). Expected: `src/cobalt/radar/**` → `com.cobalt.radar`. `cards/radar.py` or `aset/**` → also `com.cobalt.aset`. Taxonomy loader → every resident that imports it (the static AST walk decides).

| # | chunk | unlocks / removes | size | builder (L29) | restarts (L42, expected) | needs from `cobalt_dev` |
|---|---|---|---|---|---|---|
| C1 | Direction from anatomy (§1); `unclassified` setup token; unbound-direction refusal; geometry guard (§2.3); gates 1–5 of §9 for rubberband | **rubberband can form** (removes E1 + the order-dependent `setup_ref` label) | S | Opus 5 / Sol-high | radar | stored days for X2/X3; replay only (no migration) |
| C2 | Formation registries (§2.2–2.5) with today's trigger and stop re-registered (byte-identical Rubberband output); mirrored frame (§2.1); interpreter shapes (§4); assumed store + hole-fill + `TunableSource.ASSUMED` (§8); `assumed_keys` column + chip + suppression reason (§7) | removes **E8** (served-but-never-true) and **E9** (under-reported shapes); ASSUMED visible | M | Opus 5 / Sol-high | radar + aset (view column) | migration for the view column; desk writes the vault note (L65) before or with the deploy |
| C3 | D1 indicators + warm-up (§5) + D2 Range(micro) + D3 opening-drive roles + `range_break` + `consolidation_low` | **hitchhiker** | L | Opus 5 / Sol-high | radar | replay on tagged hitchhiker days (X2); X1 |
| C4 | D4 Extension lifecycle (`reverting`, `backside`) + `indicator_cross` + `measured_fraction` + `recent_higher_low` + `flat`/`between` | **backside**, **fashionably-late** | M | Opus 5 / Sol-high | radar | replay on tagged fashionably-late days; a stored backside day (X2) |
| C5 | D3 pullback / impulse / `pre_test` roles + `touched` + `indicator_rejection` + `indicator` stop + catalyst resolver `A-13` + `Extension … on Leg(x)` | **nine-ema-scalp** | M | Opus 5 / Sol-high | radar | replay on the tagged 9-EMA day; X1 decides whether the def's early window is reachable |
| C6 | D5 trendline + `dist` + the level set and `rejected` (`A-17`, `A-18`) | **vwap-continuation** | M | Opus 5 / Sol-high | radar | replay on tagged vwap-continuation days |
| C7 | D6 RangeBreak lifecycle + `retest` / `failed_trap` / `stop_hit` events + `Range(prior)` + `sequence` + `turn_candle` | **second-chance** | M–L | Opus 5 / Sol-high | radar | replay on tagged second-chance days |

**Evenings, stated plainly.** 7 chunks = **7 deploy evenings** at one deploy per evening (L43). This is counted from the first evening after the tribunal has ruled this design and C1 has passed its three checkers. Builds and checks of later chunks run in parallel lanes while earlier ones deploy (L72). Code dependencies are strictly C1 → C2 → C3 → {C4, C5, C6} → C7 (C7 reuses C6's level set). The integrated pre-merge gate applies whenever two land together (L68). **First card possible: evening 1 (rubberband).** Then hitchhiker (evening 3), backside + fashionably-late (4), nine-ema-scalp (5), vwap-continuation (6), second-chance (**evening 7 — all seven**). "Possible" is the honest word: a card also needs the market to produce the setup, and proof ESCALATE 2 says a zero-card day is a likely outcome. Evenings are shared with every other deploy lane, so 7 deploy evenings is not 7 calendar days.

## 11. WHAT I WOULD USE FROM HIS TRADING STATS

The figures that would replace a LOW-confidence assumed value, per setup. They are phrased as one message he can send to his Claude chat, in the report's `## STATS TO ASK HIM FOR`. Summary by key:

| setup | the figure | replaces |
|---|---|---|
| all seven | date + ticker + entry time + side of every trade he tagged with the setup, last 90 days | the fixture and replay-gate days (§9), not a value, but the most useful ask |
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

| bar | answer |
|---|---|
| (a) every number traceable or marked modelled, degrading the score | Every input is a stored i1 bar, a daily bar or a pool row; the receipt already retains them (`evaluate.py:498-512`, ADR-0009 D3). Every threshold is a `cfg(key)` row. An assumed row is `source: assumed`, reaches the card as `assumed_keys`, and suppresses the score (`assumed_formation`, §7). The two modelled resolvers (`A-13` catalyst, `A-05` seed) are marked on the atom outcome. First-gate experiments X1–X5 below replace every argument about data behaviour (L70). |
| (b) exactly ONE ranking authority reaches the card | `card_score` (ADR-0009 D4), unchanged. Formation adds no rank, and the side binding adds none. Nothing here feeds conviction or proximity except the trigger price, and that is suppressed when assumed. |
| (c) the integration seam as a real artifact | `Formation` (§2.4), `TriggerOutcome`, `StopOutcome`, the atom domain declarations, the `assumed_keys` view column (`"user".radar_cards_v`, owner COBALT), and `RadarScoreDetail` (unchanged schema; new atom names pass `validate_atom` or collapse to `unspecified_atom`, `evaluate.py:379-399`). Each is pinned by a committed schema test in the chunk that adds it. |
| (d) auditable by another house | `cobalt radar audit-export` (ADR-0009 D7) bundles the assumed rows with the tunables it already exports. `replay_receipt` recomputes every formation from the receipt alone. Every chunk is checked by ≥3 houses other than the builder (L67). The mirrored-frame property test and the per-setup formation fixtures are readable by any house without a DB. |

**First-gate experiments (L70) — run on `cobalt_dev` before the chunk that depends on them, never argued:**
X1 premarket seed viability (§5, before C3/C5). X2 whether `cobalt_dev` holds i1 for his tagged trade days (the tags found are dated 2025 — bars coverage unknown; before C1's fixture choice). X3 C1's `--replay` over the last 10 stored sessions: rubberband formations > 0 somewhere in the pool. X4 mirrored-frame equivalence on stored days, detector by detector (C2). X5 scan latency with every def evaluated twice × 50 members, against `radar.scan_interval` (C2).

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

Only `nine-ema-scalp` marks its variable `frontier: true` (gap table E11). This design computes none of the others and renders them YOURS. Marking them explicitly is a note edit, so it is his (L65), not proposed here.

## What this does NOT do

- It edits none of his notes, and proposes no edit to them (L65). The divergences between notes and sheets are reported only (gap table E10, plus one more in the report's ESCALATE).
- It detects no Setup (gap / day-2 / overextension / volatility-in-range); the card says `unclassified`.
- It adds no catalyst, breadth or regime data, and builds no Gap, volatility_state or Regime detectors.
- It changes nothing in `card_score`, conviction, proximity, the curves or the dots. It promotes nothing: cards stay advisory beside his hand grade, in the L7 shadow.
- It writes nothing to `"user".trader_settings`, and makes no Finviz or pool change.
- It does not tune: every assumed value stays assumed until he rules (R15, R17).
- The other six definitions are out of scope, and nothing here must be torn up for them (§2.5).
- No build, no launch, no commit by this seat.

## Open to the tribunal

The points where this proposal is least sure, each with the alternative it rejected:

1. **Direction from anatomy (`A-01`), not from a setup classifier.** Rejected: detecting which of the five setups an instance is (gap, day-2, overextension, volatility-in-range) and deriving direction as setup trend × relation. It is size L, needs daily-context detectors, and for these defs every setup gives the same side, so it changes no direction. Setup detection may still earn its place as an engine-computed `setup_relation` dot under L7 shadow.
2. **Mirrored frame for side binding.** Rejected: side-aware detectors (a long and a short branch in each). That doubles the test surface, and a missed branch is exactly the kind of defect today's was. The cost of the mirror is 2× evaluation CPU (X5).
3. **`setup_ref = unclassified` token instead of a nullable column.** Rejected: a nullable `setup_ref` would add a migration and a view change to C1 and make it larger than S. The token is a reserved value, validated.
4. **Score suppressed on any assumed formation.** Rejected: score plus chip only. L52(a) says modelled numbers degrade the score. The cost is that most early cards show no score, only the chip. Cards still appear.
5. **One vault note for assumed values, with a hole-fill merge rule.** Rejected: rows in each def's own `tunables:` unit (seven notes edited, assumed mixed with ruled) and `trader_settings` (`card.*` only, his hand per load). The hole-fill rule is a narrow exception to "user rows never shadow engine rows" (`loader.py:93-111`). The tribunal should check that it cannot widen.
6. **Premarket-seeded EMA/ATR next to the Extension's own RTH ATR.** Rejected: RTH-only (9-EMA's window would be unreachable) and prior-session seeding (the overnight gap distorts the average). Named `atr_working` vs `atr_run` so that they are two quantities, not two paths. The tribunal may rule one ATR, but moving the Extension's ATR changes Rubberband's numbers and needs its own shadow.
7. **Opening-drive termination: consolidation before pullback (`A-07`).** Read literally, the taxonomy lets the first opposing bar end a leg as a pullback (`TAXONOMY-DRAFT-v0_7.md:94`). A micro-Range always contains opposing bars, so `terminated_by == consolidation` could almost never be true, and hitchhiker's avoid would almost always hold. Rejected: the literal reading. The proposed rule: when a micro-Range instantiates from the drive's extreme within a bounded retrace, the termination is consolidation. This reads a taxonomy rule, so it may be his to rule (ESCALATE).
8. **9-EMA catalyst via in-play admission (`A-13`).** Rejected: a human tap gate, because no card would form until he tapped, which contradicts R17. The risk is that the def's intent (a real news catalyst) is weakened. The chip and the YOURS catalyst dot keep that visible.
