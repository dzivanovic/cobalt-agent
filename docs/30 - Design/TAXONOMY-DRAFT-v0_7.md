# Trading Taxonomy — Draft v0.7
Batch 2 fold 2026-09-02. Supersedes v0.6 in full. Amendment layer: **all v0.4 RULED content not amended in v0.5, v0.6 or here carries forward** (v0.4 remains the base for §6–9 and everything not restated); v0.6 sections not restated here carry forward unchanged. Schema **v0.4** (DwV bump: v0.3 + Batch 2 §A). Status: **FINAL** — §14 collisions 1–2 RULED 09-02.
Legend: **RULED** = Dejan confirmed · **DwV** = decided with veto (fold consequence, stands unless vetoed) · **PROPOSED** · **PLACEHOLDER** · **SPIKE** · **DEFERRED** · `config` = editable value, default shown · `dynamic` = must survive archiver-corpus replay (§0). Source tags `[A.n]` = TRADE-DEFS-BATCH2-v0_1 §A item n (all RULED 09-02 unless marked DwV there); `[B1 A.n]` = Batch 1 item; `[Code]` = item reported by the Batch 1 Code commit (ledger 09-02).

---

## Change log v0.6 → v0.7

| # | Change | Source | Status |
|---|---|---|---|
| 1 | `reentry_window: duration \| null` trade_def field; rules gate intersects with the 08-27 re-entry rule, stricter wins | A.1 | RULED |
| 2 | Stop placement gains `indicator {indicator, buffer, snapshot: at_entry \| live, floor}`; default `snapshot: at_entry` | A.2 | RULED |
| 3 | Trigger `trendline_break {ref: Level_ref(trendline, anchor_leg), pivots, confirmation_policy}`; flat case = far-bound break; a touch of VWAP / the base never triggers | A.3 | RULED |
| 4 | Trigger `indicator_rejection {indicator, contact: touch \| penetrate}`, confirmation `close_through` — rejection bar = trigger + entry; replaces any tape proxy | A.4 | RULED |
| 5 | `Level.type` gains `open`; `bar_break` carries a second param shape `{ref: Level_ref}` (no new trigger type) | A.5 | RULED |
| 6 | Stop buffer `fixed 0.02` for **every** trade; sheet deviations = PROPOSAL, applied only on ruling — supersedes v0.6 row 17 and §14 collision 3 | A.6 | RULED |
| 7 | Structural refs gain `recent_lower_high`; both `recent_*` refs = the micro-Range's latest counter-pivot | A.7 | RULED |
| 8 | Trail `{conditions[], mode: select, on: event}`, evaluation `close_through`; condition enum `prior_bar_break {n:1} · ma_close {ma} · vwap_close · level {level_ref}`; MA periods = config keys (`ma.slow = 20`, sheet 21). **`mode: select` supersedes A.8's `any`** — one capability picked at trade start from price action, followed to the end (§14 c.1) | A.8 + 09-02 ruling | RULED (`level` condition DwV) |
| 9 | **1-bar trail law** — trailing = one working-TF bar, always; move2move double-bar exits untouched | A.8 | RULED |
| 10 | **Stop-movement rule** — `stop_management` default `fixed`; only permitted move = `raise_to` below the latest swing low, on Dejan's call; Batch 1 ladders stand | A.8 | RULED |
| 11 | **One stop at a time** — the trail IS the stop once its `on:` event fires; one `trail` slot per trade_def; `trail_ma_close` / `trail_bar` removed from stop_management (duplicate spellings). Second Chance: hard stop → trail selected on exit_leg(1) → leg 2 exits on it | §14 c.1 | RULED (spelling DwV) |
| 12 | `working_timeframe` global default `2m` in `defaults.yaml`, per-trade override; sheets' "1-min" = template note | A.9 | DwV |
| 13 | **Class definitions rewritten** — trailing and legs-out count define no class; scalp / move2move / swing defined by trade shape and horizon (§0). Strikes v0.6 row 2 "one leg out" and A.10 "trailing exit ⇒ move2move" | §14 c.2 | RULED |
| 14 | Parameter denomination: bar-denominated params follow the working TF; minute-denominated are TF-independent | A.11 | DwV |
| 15 | **Tape = frontier, not nature** — tape reads are registry variables `source: human (frontier)`; triggers stay bar-defined | A.12 | RULED |
| 16 | Grammar atoms / fields: `dist(a,b)`, `Catalyst.grade`, `Catalyst.polarity`, `Regime.label`, `Range.counter_pivot_count`, `gap_retrace_pct`, `Leg(pullback).index` | A.13–18 | DwV |
| 17 | `Leg.role` gains `pullback` (with `index`); predicate `touched(Leg, indicator)`; Range fields `top / base / bound` named once | fold | DwV |
| 18 | Standalone `ma_close` exit target DEPRECATED → expressed as a `trail` condition; `{ma, tf}` → `{ma}` (tf = working by law) | fold | DwV |
| 19 | **Tunable slot** — every `config, dynamic` quantity is a registry row (§13.1); grammar atom `cfg(key)` replaces inline "(config)" | Code fold item | DwV |
| 20 | Taxonomy data path `configs/cobalt/taxonomy/` (ADR-0001; corrects `config/taxonomy/`); Batch 1 commit mismatches folded (`breakeven` = `level {entry}`; sequence event-steps carry no confirmation_policy; FL `entry_price` → `entry`) | Code | DwV |
| 21 | §12 status 13/21; Batch 2 CLOSED; Batch 3 = the 8 sheet-less trades | session | RULED |
| 22 | §13 replay additions (GGG duration band, trendline pivots, dist() k, counter_pivot_count, gap_retrace_pct, trail-condition sets, time_stop 2-bar) | B2 §A | RULED |
| 23 | Schema version v0.3 → v0.4 | fold | DwV |
| 24 | §14 collisions 1–2 | session | RULED |

---

## 0. Cross-cutting laws

**Anatomy-only law (RULED 09-02, unchanged):** the taxonomy carries no personal trading rules — no entry cutoffs, no "no-trade windows", no risk dollars. Windows describe market anatomy; trading is moving to 24×5. Dejan's live rules live in the printed card / rules-gate config / future Guardian (advisory), never here. Only structural exception: `market_reset 20:00–21:00`.

**Timeframe-agnostic trigger law (RULED 09-02; amended [A.9–A.11]):** a trade triggers on a bar of its own `working_timeframe`. Objects on timeframes above the working timeframe are preconditions and context, never triggers. No fixed timeframe anywhere in the taxonomy. `working_timeframe` is a config value: global default `configs/cobalt/taxonomy/defaults.yaml: working_timeframe: 2m`, per-trade override (DwV [A.9]) — a config default is a trader preference, not a taxonomy timeframe. The sheets' "1-min bar" is a template note only [B1 A.18a].
- **Class definitions (RULED 09-02, §14 c.2 — supersede v0.6 row 2 and A.10):** `class` describes the trade's shape and horizon, not its exit mechanics — **trailing vs hard exit defines no class (any class may trail), and legs-out count defines no class (scalps may scale out: Hitchhiker 2 legs, Rubberband 3).** `scalp` = usually below the 15-min timeframe, lasting seconds to ~45 minutes; `tf_ceiling: 15-min` stays the only hard constraint. `move2move` = defined entry, stop and target capitalising on a momentum move that can survive consolidation and continue in the same direction to a target usually further away (e.g. two measured moves, high/low of day, or session end) — usually longer, tradeable on 5-min and up; an intraday swing. `swing` / `options` = defined when taken up. Durations are anatomy descriptors, never gates. All 13 populated classes stand as ruled, incl. 9 EMA Scalp = scalp, BTO / Bouncy Ball = move2move.
- **Parameter denomination (DwV [A.11]):** nothing in v0.6 / Batch 1 / Batch 2 is pinned to 1-min. Bar-denominated params follow the working TF (`bar_break_reverse 2`, `time_stop 2 bars`, `bars_cleared 2`, pivot N=2, `two_bar` confirmation, 2-touch Range, MA trails, `ATR(working_tf, 14)`) — on 2-min a double-bar break = 4 minutes. Minute-denominated params are TF-independent (`Range.duration` bands 3–7 / 5–20 / ≥45, `flat()` windows, `reentry_window`). Both kept as-is: SMB counts bars; Dejan trades bars on i2. Every Tunable carries its `unit` (§13.1) so the denomination is explicit.

**Branch-vs-taxonomy boundary (RULED, unchanged):** an IF/Then branch is Dejan's authored plan for one name on one day — his data; personal timing inside a branch is legitimate.

**Dynamic definitions (RULED; registry form DwV [Code]):** consolidation rule, leg=wave alias, Extension instantiation thresholds, pivot N, trendline min-pivots, Range.duration bands, flat_threshold per indicator, Range.wick_ratio threshold, break_volume_sigma_bars, dist() k per indicator, counter_pivot_count minimum, gap_retrace_pct threshold, time_stop bar counts, trail capability sets per trade — all `config, dynamic`: must stand archiver-corpus replay before counted as solidified (§13). **Every `config, dynamic` quantity is a row in the Tunable registry (§13.1) and is referenced from predicates by key via `cfg(key)` — a dynamic value never lives only inside a predicate string.** Replay status is a field on the row, so §13's backlog is a query, not a list.

**Advisory-exit law [B1 A.15] (unchanged):** every `on_cic`, `stop_management`, exit and time-stop field is a warning to the human, never an order — Cobalt never executes (non-negotiable: no platform integration). Revise from real trades.

**Per-trade stop rules [B1 A.16; buffer RULED 09-02, reworded A.6]:** no uniform stop *placement* across trades — refs per sheet, carried in each `trade_def.stop`. **Buffer = `fixed 0.02` for every trade.** A sheet stating a different value is flagged as a PROPOSAL and applied only on Dejan's ruling (BTO and Bella Fade sheets say 0.01 → RULED 0.02). Supersedes v0.6 "unless its sheet says otherwise". `spread` is not a buffer (spread is a tradability gate). The 08-27 minimum stop-distance floor lives in the rules gate; `floor: config` in a trade_def points there.

**Stop-nudge law [B1 A.17] (rules gate, card stage; unchanged):** a stop is never exactly on the structural price, a round dollar, or a x.x0 cent level — 1–2¢ beyond. The sheets' "$0.02" is this rule (order-cluster avoidance, not a noise buffer). DwV clarification stands: the gate nudge is check-and-move, not additive.

**1-bar trail law (RULED [A.8]):** the bar-trail capability = one working-TF bar (`prior_bar_break {n: 1}`), always; `n` is pinned to 1 wherever a bar trail is expressed (trail condition, `on_cic: trail_bar`). move2move **exits** on a double-bar break (`bar_break_reverse {bars: 2}`, GGG / Big Dog) are targets, not trails — untouched.

**One-stop law (RULED 09-02, §14 c.1):** a trade has exactly one stop at any moment. Hard stop from entry; the stop may be moved (per the stop-movement rule and the trade's ruled ladder — e.g. to break-even after a scale-out) and, from the trail's `on:` event onward, **the trail IS the stop** — never a second object. Share count on the stop is card/sizing state (fill-recompute), not taxonomy. **Trail = selected capability (RULED):** a trade_def lists its trail capabilities (`conditions[]`: 2-min bar, 9 EMA, 20 EMA…); at trade start Dejan — or Cobalt, from price action — picks ONE and it is followed to the end of the trade (`mode: select`); the selection and its WHY persist on the card as calibration data for the day Cobalt picks. A.8's "first condition to fire" is superseded. Which capability the stock "cleanly follows" = registry variable `trail_fit` (cobalt-computable from bars).

**Stop-movement rule (RULED [A.8]):** `stop_management` default = `fixed`. The only generally permitted move = `raise_to {structural_extreme, ref: recent_higher_low}` (below the latest swing low), on Dejan's call. Per-sheet ladders already ruled in Batch 1 stand as ruled: Rubberband (B/E after 1R, trail after leg 2), Big Dog (50%-hold), Back$ide `time_stop`; Second Chance's trail after leg 1 (previously spelled `trail_ma_close`) is the same shape. `time_stop` entries (BTO, Bouncy Ball, Back$ide) are exits-by-time, not stop moves — permitted.

**Sheet reading laws [B1 A.18] (unchanged):** (a) every SMB scalp sheet is TF-templated — "1-min bar" = working TF; (b) "low of the day" = the current tracked low of the move (`turn_low` / `snapback_candle`), not necessarily the session LOD, unless the image shows otherwise; (c) `preferred_windows[]` populated from the sheet's "ideal times", mapped to the RTH sub-window enum; sheet wording kept in `preferred_windows_ref` — window-fit variable only.

**Attempts [B1 A.19; amended A.1]:** `max_attempts` editable per trade; sheet value is the default; doctrine (anatomy), not Dejan's rule. **`reentry_window: duration | null`** (default null): attempt n+1 is valid only if the trigger re-fires within the window (GGG 3 min). The rules gate intersects both with the personal re-entry rule (08-27: #2 needs written new info, #3 = stand-down + ticker closed); the stricter governs the card.

**Standard quality factors [B1 A.20] (unchanged):** every card carries `setup_relation`, `market_alignment`, `sector_alignment` (§1 misalignment = penalty variable, never a forbidden cell).

**Tape law (Laws Register: human-only tape dot) — frontier note (RULED [A.12]):** the human-only tape dot is a capability-frontier flag under the 08-31 per-field ownership model (cobalt / cobalt-degraded / human), not a permanent law. Every tape-class read is a registry variable with `source: human (frontier)` — `bids_hold`, `tape_flip`, `tape_read`, `buyers_defending_zone` — and flips to Cobalt when an L2 / time-&-sales feed is ingested, with no schema change. Triggers stay bar-defined; a tape-defined trigger enters only as an amendment backed by data.

## 1. Spine (COMPLETE, unchanged)

```
Market regime → Sector state → In-Play ticker → Category → Setup → Trade
```
Category computed per instance (v0.4). Instance direction computed from setup-instance state (§5). One card per trade instance; card cites `trade_def` + setup instance + matched IF/Then branch. Misalignment = penalty variable.

## 2. v0.4 §13 open items — resolved (RULED 09-02, unchanged)

1. RTH sub-windows (anatomy only, config): `open_drive 9:30–10:00 · morning 10:00–11:30 · midday 11:30–14:00 · afternoon 14:00–15:30 · close 15:30–16:00`; `market_reset` structural.
2. Unexplained-RVOL in-play admission: yes — `reason: unexplained`, resolver's chase list.
3. Consolidation: daily = inside-day body rule, daily-only. Intraday consolidation = a Range instance at micro scale — instantiation **2 touches per side** (`cfg(range.micro.touches_per_side)`). No bar count. Dynamic.

## 3. Structure primitives

### 3.0 Range — fields (amended)
Instantiation per §2.3 (micro) or level-defined (HTF). Fields:
- `duration` (start → now) [B1 A.6] — precondition band per trade (Hitchhiker 5–20 min · Big Dog ≥ 45 min · **GGG 3–7 min** [B2]) and quality factor. Config, dynamic.
- `bound_type: flat | converging | channel` (v0.4) — the only shape field; **diverging bounds = no Range** (v0.6 Ruling 1). Bouncy Ball requires `converging`.
- **`top` / `base`** — the two bounds (`base` alias `range_base` / `consolidation_low`). **`bound`** = the trade-side bound (long → `top`, short → `base`); trade_defs written long-side may cite either spelling. DwV — one spelling for the registry.
- **`counter_pivot_count`** [A.16] — number of successively shallower counter-pivots against the flat bound (Bouncy Ball ≥ `cfg(range.counter_pivot_min)`, default 2). Config, dynamic.
- `wick_ratio` [B1 A.8], `height`, `volume_contraction`, `position` (incl. `position_vs_vwap_ema9`) — data fields consumed by quality factors; named here for one spelling.

### 3.1 Leg = wave (RULED alias; role enum amended)
`leg {direction, start, end, terminated_by: pullback | consolidation, range, volume_profile, role, index}` — one directional move terminated by the first pullback (≥1 opposing bar) or consolidation (micro-Range). `wave` = alias.
**`role: opening_drive | impulse | pullback`** — `impulse` = any directional leg preceding a range; `opening_drive` = the impulse leg starting at the RTH open; **`pullback`** (DwV, fold) = the counter-directional leg that terminates an impulse / opening drive; **`index`** [A.18] = ordinal of pullback legs since the RTH open (First VWAP Pullback requires `Leg(pullback).index == 1`). Predicate **`touched(Leg, indicator)`** (DwV) = the leg's extreme reached the indicator price (contact, not proximity) — FVP (VWAP), 9 EMA Scalp (EMA9). Consumers: Extension `leg_count`; exit targets `leg_end(n)`; `raise_to` events; trendline anchors (§3.7); `gap_retrace_pct` (§3.8).

### 3.2 Extension — intraday instantiation (RULED, unchanged)
Paths (A) culminating bar character (HV bar ≥ MA+2σ that is also the run's widest body) or (B) ≥ `cfg(extension.path_b_atr)` (1.25) ATR from the open with `catalyst_ref: null`. Snapback watched only once instantiated. Distance from VWAP / ATRs from open = card quality factors, never gates. `leg_count` = legs since base. `backside`: ≥1 HH and ≥1 HL above rising 9 EMA (config). Batch 2 consumes `Extension.instantiated on Leg(x)` as an avoid (FVP, 9 EMA Scalp, Bouncy Ball).

### 3.3 Swing pivot N (RULED, unchanged)
N = 2 bars each side, `cfg(pivot.n)`, per-TF override off by default. Pivots serve structure, never triggers. **Distinct key from the trendline's minimum pivot count** (`cfg(trendline.min_pivots)`, §3.7) — same default, different meaning (DwV spelling).

### 3.4 Range Break (unchanged)
Lifecycle `forming → break_attempt → accepted | failed_trap`; `retest` event; promotion default `close_through`; `failed_trap` = close back inside within `cfg(range_break.failed_trap_bars)`. `RangeBreak(HTF).day_count` [B1 A.10] as v0.6. Batch 2 consumes `RangeBreak(Level_ref(HTF)).state == accepted against trade_direction` as a Bella Fade avoid.

### 3.5 Indicator-slope predicates [B1 A.9] (unchanged)
`slope_norm(indicator)`, `flat(indicator, window)`, thresholds `cfg(flat_threshold.ema9)` / `cfg(flat_threshold.vwap)`. Working-TF ATR, never daily.

### 3.6 Structural references (consolidated; consumed by stops, anchors, exits)
`snapback_candle` / `turn_low` (aliases — the **current tracked extreme of the move**, [B1 A.5, A.18b]) · `low_of_day` / `high_of_day` (session extreme, distinct from the above) · `consolidation_low` / `range_base` (= `Range.base`) · `turn_candle` · **`recent_higher_low` / `recent_lower_high`** [A.7] (side-mirrors — the micro-Range's latest counter-pivot on the trade-opposite side; v0.6 "micro-Range base pivot" = the same object for a long; Back$ide / Bouncy Ball stops; the stop-movement rule's `raise_to` ref) · `cross_point {a, b}` [B1 A.4] · `entry` (fill price; alias `breakeven` — resolves to `level {level_ref: entry, buffer: 0}` [Code]) · `leg_end(n)` · **`Range(micro).top` / `.base`** as parametrised refs (encoded `level {level_ref: "Range(micro).top"}` in YAML — Rubberband/GGG precedent, [Code] DwV) · any `Level_ref`, now including `Level_ref(open)` and `Level_ref(trendline, anchor_leg)` (§3.7).

### 3.7 Level.type additions (amended)
- **`open`** [A.5] — the RTH opening print. Consumer: Back-Through Open, `bar_break {ref: Level_ref(open)}`.
- **`trendline`** (09-01) gains `anchor_leg: Leg(...)`: the line through the named leg's pivots, ≥ `cfg(trendline.min_pivots)` (default 2), sloped by nature [A.3]. The flat case (pullback consolidated into a micro-Range) is the same object with slope 0 — the break must be through the **far bound** (`Range(micro).top` for a long). Consumers: VWAP Continuation (anchor = `Leg(pullback)`), Bella Fade (anchor = `Leg(opening_drive)`).

### 3.8 Derived quantities (new, DwV [A.13, A.17])
- `dist(a, b)` — distance in working-TF ATR units: "near VWAP" = `dist(price, VWAP) <= cfg(dist.k.vwap) · ATR(working_tf, 14)`. k per indicator, config, dynamic.
- `gap_retrace_pct = Leg(opening_drive).range ÷ Gap.size` — GGG avoid `> cfg(gap_retrace_pct_max)` (0.5) + quality factor. Config, dynamic.

## 4. Radar trades → object states (RULED, unchanged from v0.6)
Table as v0.6 (Rubberband · Back$ide · Fashionably Late · Hitchhiker · Second Chance · Big Dog). Batch 2 trades are not radar trades; their object-state preconditions live in their trade_defs (TRADE-DEFS-BATCH2-v0_1 §B). Radar reads object states, not trade detectors.

## 5. VIR resolution (RULED, unchanged)
VIR unlocks countertrend trades in either direction; `two_way` removed; every trade_def side-symmetric; instance direction computed from setup-instance state.

## 10. Trade layer — schema v0.4

### 10.1 `trade_def` registry (data)
```
trade_def {
  id, name, aliases[],
  family[]: opening_drive | continuation | range_break | reversion | time_window,   # extensible [B1 A.1]
  class: scalp | move2move | swing | options,          # trade shape + horizon (§0 class definitions, RULED 09-02): scalp = sub-15-min TF, seconds–~45 min (tf_ceiling 15-min);
                                                        # move2move = intraday swing surviving consolidation to a further target, 5-min+; neither trailing nor legs-out count defines class
  sides: long+short (inverted),
  valid_setups[]: {setup_ref, relation: with_trend | countertrend},   # Cameron H grid as data (Batch 1 §C)
  instance_direction: computed from setup-instance state,
  working_timeframe: cfg(working_timeframe) (global default 2m) | per-trade value,  tf_ceiling: 15-min (scalp only)   # [A.9]
  entry_mode: front_side | backside,
  preconditions[]: predicates (§10.5) | {text} fallback,
  radar_watch[]: predicates → watch/checkpoint state, never entry,
  trigger: {type: bar_break | range_break | indicator_cross | trendline_break | indicator_rejection, params, confirmation_policy}   # [A.3–A.5]
         | {type: sequence, steps[]: {name, predicate, confirmation_policy?}},   # event steps carry no policy [Code]
  stop: {type: structural_extreme | measured_fraction | level | indicator, params: {ref | indicator, buffer, snapshot?, floor}, evaluation},   # [A.2]
  stop_management[]: {type, params, on: event},          # ladder of moves of THE stop; default fixed (stop-movement rule) — advisory
  trail: {conditions[], mode: select, on: event} | null, # ONE per trade_def (one-stop law); from on: the trail is the stop; default on: entry
  exit[]: {fraction, target_type, params, evaluation, computable: cobalt | human},   # advisory; target_type: trail = the leg exits when the trail fires
  on_cic: {triggers[], action},                          # advisory
  max_attempts: config (sheet default),
  reentry_window: duration | null,                       # [A.1]; rules gate takes the stricter of this and 08-27
  add_policy: {type, params},                            # reserved, default none (§10.6)
  avoid[]: predicates | {text},
  quality_factors[]: → card variables; always includes setup_relation, market_alignment, sector_alignment;
                     tape-class factors carry source: human (frontier) [A.12],
  preferred_windows[]: RTH sub-window enum → window-fit variable only,
  preferred_windows_ref: text (sheet wording),
  reference_stats: external metadata (SMB win rate / R:R), never EV
}
```
One trigger per trade_def (v0.6 Ruling 2 stands; A.3 reaffirms — no variants). Every `config` value in a trade_def is either an inline literal the loader hoists into the Tunable registry or a `cfg(key)` reference (§13.1, DwV).

### 10.2 Enums (extensible)
**Trigger types:** `bar_break` — two param shapes: `{bars_cleared: n, direction: any}` (Rubberband) or `{ref: Level_ref}` (Back-Through Open, `Level_ref(open)`) [A.5] · `range_break {ref: Range.top | Range.base | Range.bound}` · `indicator_cross {a, b, direction}` (stamps `cross_point`) · **`trendline_break {ref: Level_ref(trendline, anchor_leg), pivots: cfg(trendline.min_pivots)}`** [A.3] · **`indicator_rejection {indicator, contact: touch | penetrate}`** [A.4] — the bar that touches/penetrates the indicator and closes on the trade side IS trigger and entry; next-bar continuation = tape read = human · `sequence {steps[]}`.
**Stop placement:** `structural_extreme {ref: §3.6 ref, buffer: fixed <¢> (default 0.02), floor: config → rules gate}` · `measured_fraction {anchor_a, anchor_b, fraction}` · `level {level_ref, buffer}` · **`indicator {indicator: VWAP | EMA9 | ma.slow, buffer: fixed <¢> (default 0.02), snapshot: at_entry | live, floor: config}`** [A.2] — default `at_entry`: the hard stop is the indicator price at fill; `live` (Cobalt re-warns as the indicator drifts) exists, not default. Consumers: VWAP Continuation, First VWAP Pullback (VWAP), 9 EMA Scalp (ma.slow).
**Stop management** (moves of the one stop; each entry `on: event`, default `entry`; default ladder = `fixed`): `fixed` · `raise_to {placement: <any stop-placement>, on: event}` — the only generally permitted move is `raise_to {structural_extreme, ref: recent_higher_low}` (stop-movement rule); Batch 1 ladders stand (Rubberband B/E after 1R, Big Dog 50%-hold) · `time_stop {duration: bars, condition}` · `passive`. **`trail_ma_close` / `trail_bar` REMOVED** — duplicate spellings of the `trail` slot (one-stop law). `breakeven` placement = `level {level_ref: entry, buffer: 0}` [Code].
**Trail** (one slot per trade_def, RULED 09-02): `trail {conditions[]: prior_bar_break {n: 1} · ma_close {ma} · vwap_close · level {level_ref} (exit-into-strength, DwV), mode: select, on: event (default entry)}`, evaluation `close_through`. `conditions[]` = the trade's trail capabilities from the sheet; `mode: select` = one picked at trade start by Dejan / Cobalt from price action and followed to the end; selection + WHY persist on the card. Batch 1/2 spellings resolve: Second Chance `on: exit_leg(1)`, conditions `[ma_close {ma.fast}, ma_close {ma.slow}, prior_bar_break {1}]`; Rubberband `on: exit_leg(2)`, `[ma_close {ma.fast}]` (leg 3 keeps its VWAP target, the trail is its stop); VWAP Continuation `on: exit_leg(1)`, `[ma_close {ma.slow}]`; 9 EMA Scalp / BTO / Bouncy Ball `on: entry` with their listed sets.
**Exit targets:** `rr_multiple {r}` · `vwap` · `level {level_ref}` · `measured_move {anchor_a, anchor_b, projected_from, multiple}` · `leg_end {leg_index | break_leg}` · `bar_break_reverse {bars: 2, after?: event}` (move2move exit; untouched by the 1-bar trail law) · **`trail`** — the leg exits when the trade's trail (the stop) fires; no params here, the trail is defined once in the `trail` slot · `window_end {window}` (move2move session-end exits) · `cic_event`. **`ma_close` as a standalone target is DEPRECATED** (DwV) — it is a trail capability; `{ma, tf}` → `{ma}` (tf = working TF by law).
**MA keys** [A.8]: `cfg(ma.fast) = 9` · `cfg(ma.slow) = 20` (sheet value 21 recorded on the row). Sheets' "21 EMA" → `ma.slow`.
**Events:** `entry` · `exit_leg(n)` · `leg_end(n)` · `retest` · `stop_hit` · `cic(n)` · `consolidation` · `divergence`.
**Evaluation:** `touch | close_through`. Hard stops = touch; invalidation law = close_through on working TF; `trail` = close_through.
**CiC as exit input:** `on_cic {triggers: [1..4], action: exit_all | exit_leg | tighten_to: breakeven | trail_bar}` (`trail_bar` = switch the stop to the 1-bar trail capability).

### 10.3 Confirmation policy (RULED; amended)
Per trigger: `intrabar · close_through · two_bar · acceptance {bars | time}`. Entries mostly `intrabar` (`range_break`, `trendline_break`, `bar_break`); **`indicator_rejection` = `close_through` by definition** — entry at the close of the rejection bar [A.4]; Second Chance steps 1 and 3 `close_through`, step 2 = event, no policy [Code]. Invalidations `close_through`. Headline-driven regime flag → one-notch step-up, one config table.

### 10.4 Entry mode + sizing (RULED, unchanged)
`front_side` = entry at the turn / break bar; `backside` = entry after structure confirms. No entry-mode → size coupling; one sizing path: grade → risk key → shares = risk ÷ stop distance.

### 10.5 IF/Then condition grammar (RULED; atoms extended)
Branch = `{condition, action, invalidation}`. Atoms as v0.6 plus (DwV [A.13–A.18], fold): `dist(a, b) {<=,>} k·ATR` · `touched(Leg, indicator)` · `Catalyst.grade` (1–10, the LLM catalyst call) and `Catalyst.polarity` as predicate fields (BTO ≥ 8, Bella Fade ≤ 8, config) · `Regime.label` (09-01 SMB 2×2 label; BTO avoids `range_bound | fading`) · `Range.counter_pivot_count` · `gap_retrace_pct` · `Leg.role` incl. `pullback`, `Leg.index` · `Level_ref(open)`, `Level_ref(trendline, anchor_leg)` · **`cfg(key)`** — reference to a Tunable row (§13.1). `Object.field` for every §3.0/3.4 field; `event(name)` over the §10.2 enum. Combinators, actions, invalidation, `mirror` unchanged.

### 10.6 Adds / scale-ins — PARKED (unchanged)

## 11. Day 3 liquidity trap (RULED criteria; PLACEHOLDER definition — unchanged)
Graduation criteria 1–5 and the placeholder definition carry forward from v0.5; placeholder stop buffer = `fixed 0.02` (A.6).

## 12. Population plan (RULED process; status updated)
Offline batches: Dejan pastes full 2-page sheet → Claude drafts filled `trade_def` → Dejan rules conflicts only. **Repo home: `configs/cobalt/taxonomy/`** (ADR-0001; corrects the v0.6 prompt's `config/taxonomy/` per the CLAUDE.md boundary law) — `trade_defs/*.yaml`, `cameron_grid.yaml`, `defaults.yaml`, `tunables.yaml` (§13.1), per-trade variable-registry stubs; Pydantic on load, `extra=forbid`, fail-loud loader, validate CLI. No engine code, no predicate parsing until the setups engine.
- **Batch 1 — CLOSED 09-02, COMMITTED** (branch `taxonomy/trade-defs-v0_3`, 4 commits, 207 tests green, unpushed at fold): Hitchhiker, Big Dog, Second Chance, Back$ide, Fashionably Late, Rubberband → TRADE-DEFS-BATCH1-v0_1.md. Commit-reported mismatches folded (change log #20). Rubberband source of truth: Rev1 deck + 09-02 rulings; Rev2 note pending.
- **Batch 2 — CLOSED 09-02, COMMITTED** (commits 00ff853 + 2b96611 on the same branch, 223 tests green, unpushed): Gap Give and Go, VWAP Continuation, First VWAP Pullback, 9 EMA Scalp, Back-Through Open, Bella Fade, Bouncy Ball → TRADE-DEFS-BATCH2-v0_1.md. Committed at schema v0.3 + §A (trail as exit target, `mode: any`); the v0.7 commit migrates to v0.4 (trail slot, `mode: select`). Commit-reported items folded: GGG `raise_to` ref encoded as `level {Range(micro).top}` (§3.6); `buyers_defending_zone` has no consumer among the 13 — no registry entry until a trade cites it.
- **Population status: 13 of 21 grid trades.** Not populated (sheets not in hand): `opening_drive_pmh, opening_range_break, first_move_down, first_move_up, spencer_scalp, off_sides, the_330_trade, ema9_reclaim` — `valid_setups[]` only. **Batch 3** = these 8 as sheets are found (same one-at-a-time process). Day 3 liquidity trap PLACEHOLDER (§11). Gap & Go = setup sheet, excluded (setup-level metadata for `gap_and_go` only).
- Trade classes swing / options: defined when Dejan takes them up.

## 13. Spikes / research (carried + added)
- Carried: TradingView MCP internals; put/call; BTC/VIX ownership; dispersion measure; $UVOL/$DVOL via TradingView MCP; Day 3 liquidity trap sheet (SMB chatbot pull acceptable).
- **Replay validation** over the archiver corpus = every §13.1 row with `status != solidified`. Carried: consolidation 2-touch rule · leg=wave alias (first consumer = Hitchhiker wave exits) · Extension paths A/B thresholds · pivot N=2 · `failed_trap` N · Range.duration bands (5–20 / ≥45) · flat_threshold per indicator · Range.wick_ratio threshold · break_volume_sigma_bars. **Added [B2 §A]:** Range.duration 3–7 band (GGG) · trendline min-pivots · dist() k per indicator · counter_pivot_count minimum · gap_retrace_pct threshold · trail capability sets per trade + `trail_fit` selection variable (outcome-tuned) · time_stop 2-bar no-progress (BTO, Bouncy Ball; Back$ide carried).
- **Backlog (post-MVP, after grading engine):** visual-similarity conviction variable — as v0.6.

### 13.1 Tunable registry (DwV, Code fold item) — `configs/cobalt/taxonomy/tunables.yaml`
Row shape:
```
tunable {
  key,                                  # dotted, unique; the cfg(key) target
  value,                                # current default
  unit: bars | min | atr | cents | count | pct | ratio | label | duration,
  scope: global | per_trade(<id>) | per_indicator(<ind>),
  dynamic: bool,                        # true ⇒ §0 dynamic-definitions law applies
  status: proposed | replay_pending | solidified | overridden,
  source: ruling | sheet | dwv,
  sheet_value?,                         # when the sheet differs (ma.slow 21; BTO/Bella buffer 0.01)
  consumers[],                          # trade_def ids / primitives
  replay?: {corpus_ref, result, date}
}
```
Rules: the loader hoists every inline `(config)` literal in a trade_def into a row (key derived `<trade_id>.<field>`) and rejects a `cfg(key)` with no row (fail-loud); `sheet_value` ≠ `value` is a visible PROPOSAL record (A.6); replay writes `status`, never `value` — value changes stay a ruling. Seed rows (status `replay_pending` unless noted):

| key | value | unit | scope | dyn | consumers |
|---|---|---|---|---|---|
| `working_timeframe` | 2m | duration | global | no (solidified by ruling) | all |
| `stop.buffer` | 0.02 | cents | global | no | all stops; BTO/Bella `sheet_value 0.01` |
| `ma.fast` / `ma.slow` | 9 / 20 (sheet 21) | count | global | no | trails, stops, 9 EMA Scalp |
| `range.micro.touches_per_side` | 2 | count | global | yes | micro-Range instantiation |
| `pivot.n` | 2 | bars | global | yes | swing pivots |
| `trendline.min_pivots` | 2 | count | global | yes | VWAP Cont, Bella Fade |
| `range.duration_band` | [5,20] / ≥45 / [3,7] | min | per_trade hitchhiker / big_dog / ggg | yes | preconditions |
| `flat_threshold.ema9` / `.vwap` | — | ratio | per_indicator | yes | Fashionably Late |
| `range.wick_ratio_max` | — | ratio | global | yes | Hitchhiker avoid |
| `break_volume_sigma_bars` | — | count | global | yes | Big Dog |
| `extension.path_b_atr` | 1.25 | atr | global | yes | Extension |
| `extension.backside_hh_min` / `_hl_min` | 1 / 1 | count | global | yes | Back$ide |
| `range_break.failed_trap_bars` | — | bars | global | yes | Range Break, Second Chance |
| `dist.k.vwap` | — | atr | per_indicator | yes | VWAP Continuation |
| `range.counter_pivot_min` | 2 | count | global | yes | Bouncy Ball |
| `gap_retrace_pct_max` | 0.5 | pct | global | yes | GGG |
| `time_stop.bars` | 2 | bars | per_trade backside / bto / bouncy_ball | yes | stop_management |
| `bar_break_reverse.bars` | 2 | bars | per_trade ggg / big_dog | yes | exits |
| `rubberband.bars_cleared` | 2 | bars | per_trade | yes | trigger |
| `catalyst.grade_min` / `_max` | 8 / 8 | count | per_trade bto / bella_fade | no (config) | preconditions |
| `bella_fade.near_low_duration_max` | — | min | per_trade | yes | avoid |
| `<trade>.max_attempts`, `<trade>.reentry_window` | sheet | count / min | per_trade | no (doctrine) | rules gate |
| `<trade>.trail_conditions` | sheet capability set | label[] | per_trade | yes (outcome-tuned) | trail slot; per-instance selection is card data, not a tunable |

## 14. Fold collisions — RULED 09-02
1. **Second Chance stop ladder vs A.8 retro-fit — NOT a collision.** Two spellings of one object (`stop_management: trail_ma_close` and exit `trail`), misread as two stops. RULED: **one stop at any moment; the trail is the stop** once active; a trade_def lists trail *capabilities* and ONE is selected at trade start from price action and followed to the end (`mode: select` — supersedes A.8's first-to-fire `any`). Spelling consolidated into the single `trail` slot (§10.1/10.2); nothing dropped or grandfathered.
2. **9 EMA Scalp class vs A.10 — A.10 struck.** RULED: trailing vs hard exit defines no class; legs-out count defines no class (v0.6 "scalp = one leg out" was wrong from the start — Hitchhiker and Rubberband scale out and are scalps). Classes redefined in §0 by shape and horizon; all 13 populated classes stand.
No other collisions. Batch 2 A.6 explicitly supersedes v0.6 Ruling 3 — folded. DwV items stand unless vetoed.
