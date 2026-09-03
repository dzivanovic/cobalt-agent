# Trading Taxonomy — Draft v0.5
Trades pass 2026-09-02 (closed). Supersedes v0.4. All v0.4 RULED content carries forward unless amended here.
Legend: **RULED** = Dejan confirmed · **PROPOSED** = Claude's draft awaiting his call · **PLACEHOLDER** = default rules to be replaced · **SPIKE** = empirical check before ruling · **DEFERRED** = parked to a named session.

---

## 0. Cross-cutting laws (additions, RULED 09-02)

**Anatomy-only law:** the taxonomy carries no personal trading rules — no entry cutoffs, no "no-trade windows", no risk dollars. Windows describe market anatomy; trading is moving to 24×5 with premarket, aftermarket and overnight included. Dejan's live rules live in the printed card / rules-gate config / future Guardian (advisory), never in this document. (Only structural exception: `market_reset 20:00–21:00` = venue anatomy, ruled 09-01.)

**Timeframe-agnostic trigger law:** a trade triggers on a bar of its own `working_timeframe` — trader preference per trade class (intraday scalp: Dejan's 2-min today, any TF ≤ 15-min; swing and options: their own classes, own rules, own timeframes). Objects on timeframes above the working timeframe are preconditions and context, never triggers. No fixed timeframe anywhere in the taxonomy.

**Branch-vs-taxonomy boundary:** an IF/Then branch is Dejan's authored plan for one name on one day — his data. Personal timing inside a branch is legitimate; the taxonomy itself stays anatomy-only.

**Dynamic definitions:** consolidation rule, leg=wave alias, Extension instantiation thresholds, pivot N — all tagged dynamic: config, must stand the test of historical usage (archiver-corpus replay) before counted as solidified.

## 1. Spine (COMPLETE)

```
Market regime → Sector state → In-Play ticker → Category → Setup → Trade
```
Category computed per instance (v0.4). Instance **direction** computed from setup-instance state (§10.1). One card per trade instance; card cites `trade_def` + setup instance + matched IF/Then branch. Misalignment (countertrend cell, wrong regime) = penalty variable, never a forbidden cell.

## 2. v0.4 §13 open items — resolved (RULED)

1. **RTH sub-windows (anatomy only, config):** `open_drive 9:30–10:00 · morning 10:00–11:30 · midday 11:30–14:00 · afternoon 14:00–15:30 · close 15:30–16:00`. `market_reset` stays structural.
2. **Unexplained-RVOL in-play admission:** yes as drafted — `reason: unexplained`, resolver's chase list.
3. **Consolidation:** daily = inside-day body rule, **daily-only**, sole consumer Overextension day-count/5-ATR reset. **Intraday consolidation = a Range instance at micro scale** — instantiation rule reused everywhere: **2 touches per side** (single config value). No bar count (rejected as wrong design). Dynamic.

## 3. Structure primitives (amendments)

### 3.1 Leg = wave (RULED, data-level alias — changeable)
`leg {direction, start, end, terminated_by: pullback | consolidation, range, volume_profile}` — one directional move terminated by the first pullback (≥1 opposing bar) or consolidation (micro-Range) event. `wave` is an alias on the same definition record; if the equivalence proves wrong, `wave` gets its own record and consumers re-point. Consumers: Extension `leg_count`; exit targets `leg_end`.

### 3.2 Extension — intraday instantiation (RULED)
Two paths, both config:
- **(A) culminating** — bar character: accelerating run of expanding same-direction bodies on expanding volume; `culminating` = the run's HV bar (vol ≥ MA+2σ) that is also its widest body.
- **(B) distance** — ≥ **1.25 ATR from the open** (config) with **no catalyst** (`catalyst_ref: null`).
Only once instantiated does Cobalt watch for the snapback. Distance from VWAP / ATRs from open are card quality factors, never gates. Extension gains `leg_count` (legs since base) — rising count = reversion-probability quality factor.
`backside` phase definition: HH+HL swing sequence above rising 9 EMA (+ micro-Range above the 9 EMA for Back$ide).

### 3.3 Swing pivot N (RULED)
**N = 2** bars each side, single config, fully configurable (per-TF override available, off by default). Pivots serve structure (HH/HL, Range bounds, leg boundaries), never triggers — lag affects recognition, not entry.

### 3.4 Range Break — retest event (RULED)
Lifecycle unchanged (`forming → break_attempt → accepted | failed_trap`). Gains a timestamped **`retest` event** attached to an accepted break (may recur). Promotion default `close_through`; `failed_trap` = close back inside within N bars (config) of the attempt. Second Chance's failed-retest avoid rule = same predicate after the retest event.

## 4. Radar trades → object states (RULED)

| Trade | Precondition (object state) | Trigger |
|---|---|---|
| Rubberband | Extension `culminating` (intraday, or daily as context) | snapback bar_break — the event *is* the `culminating → reverting` transition |
| Back$ide | Extension `backside` + micro-Range above rising 9 EMA | range_break |
| Fashionably Late | Extension `reverting → backside` on the indicator plane; avoid predicate: 9 EMA flat > 15 min | indicator_cross (9 EMA × VWAP) |
| Hitchhiker | opening-drive leg terminated by consolidation (not pullback) + micro-Range in upper ⅓ of day range | range_break |
| Second Chance | Range Break `accepted` + `retest` event | sequence (retest → turn-candle close-through) |
| Big Dog | micro-Range `converging` after opening-drive leg, above PDH, `volatility_state: contraction`; predicates: pattern ≤ 50% day range, > 75% of day above open | range_break |

Radar reads object states, not trade detectors: "Extension entered culminating" = Rubberband stalking.

## 5. VIR resolution (RULED)
VIR is a **setup** that unlocks multiple countertrend trades in either direction. Two-way-ness lives in the setup, not in any trade. `two_way` removed from the relation enum. Every `trade_def` is side-symmetric by construction (rules identical, inverted for shorts). Instance direction computed from setup-instance state: directional setup → the one opposing direction; VIR → toward range midpoint from whichever bound is being tested.

## 10. Trade layer (NEW — schema v0.2, RULED and LOCKED)

### 10.1 `trade_def` registry (data, per modularity law)
```
trade_def {
  id, name, aliases[], family, class: scalp | move2move | swing | options,
  sides: long+short (inverted),
  valid_setups[]: {setup_ref, relation: with_trend | countertrend},   # Cameron H grid as data
  instance_direction: computed from setup-instance state,
  working_timeframe: config (trader preference), tf_ceiling: 15-min (scalp class),
  entry_mode: front_side | backside,
  preconditions[]: object-state predicates,
  trigger: {type: bar_break | range_break | indicator_cross | sequence[], params, confirmation_policy},
  stop: {type, params, evaluation},
  stop_management: {type, params},
  exit: ladder[] {fraction, target_type, params, evaluation, computable: cobalt (default) | human},
  on_cic: {triggers[], action},
  max_attempts: config,
  add_policy: {type, params}  # reserved, default none (item 8 PARKED)
  avoid[]: predicates + text fallback,
  quality_factors[]: → card variables,
  preferred_windows[]: doctrine → window-fit variable only,
  reference_stats: external metadata (SMB win rate / R:R), never EV
}
```
Trigger variants: one trade_def may carry named trigger variants (Rubberband: A = snapback bar-break, B = level-fail reclaim).

### 10.2 Enums (RULED, extensible)
**Stop placement:** `structural_extreme {ref: snapback_candle | low_of_day | consolidation_low | range_base | turn_candle | recent_higher_low, buffer: fixed | spread, floor}` · `measured_fraction {anchor_a, anchor_b, fraction}` · `level {level_ref, buffer}`
**Stop management:** `fixed` · `breakeven_at {R}` · `trail_ma_close {ma, tf}` · `trail_bar {n}` · `time_stop {duration, condition}` · `passive`
**Exit targets:** `rr_multiple` · `vwap` · `level` · `measured_move` · `leg_end` · `bar_break_reverse` · `ma_close` · `window_end` · `cic_event`
**Evaluation** (every stop and exit target): `touch | close_through`. Hard stops = touch; Dejan's invalidation law = close_through on working TF.
**CiC as exit input:** `on_cic {triggers: [1..4], action: exit_all | exit_leg | tighten_to: breakeven | trail_bar}` — the four ruled CiC triggers become exit vocabulary, no second detector.

### 10.3 Confirmation policy (RULED)
Per trigger, config: `intrabar` · `close_through` · `two_bar` · `acceptance {bars | time}`. Sheet doctrine: entries mostly `intrabar` (Second Chance step 1 `close_through`); invalidations `close_through`. Sequence triggers carry a policy per step. **Headline-driven regime flag → each trigger's policy steps up one notch** (`intrabar → close_through → two_bar`), one config table.

### 10.4 Entry mode + sizing (RULED)
`front_side` = entry at the turn / break bar (Rubberband, Hitchhiker, Big Dog); `backside` = entry after structure confirms (Back$ide, Second Chance, Fashionably Late). **No direct entry-mode → size coupling.** Sizing has one path: grade → risk key → shares = risk ÷ stop distance. Entry mode influences size only through the grade (as a variable) and the stop distance. Risk dollars per grade stay in Dejan's rules/config, outside the taxonomy.

### 10.5 IF/Then condition grammar (RULED)
Branch = `{condition, action, invalidation}` (v0.3). Grammar = predicates over taxonomy objects.
- **Atoms:** `price {above|below|at|tests|holds|fails} Level_ref [buffer]` · `Object.state == X` / `Object.field ≥ x` · `event(type)` (CiC, retest, divergence, leg_end, consolidation) · `in_window(name)` / `after(window.start)` / `before(window.end)` · `at(HH:MM)` · `holds_for {bars|minutes}` · indicator relations (`EMA9 {above|below|crosses} VWAP`, slope) · context (`regime`, `dispersion`, `market_alignment`, `rvol`, `volatility_state`).
- **Combinators:** `AND` · `OR` · `NOT` · `THEN` (ordered, optional `within {duration}`) · `WITHIN {duration}`.
- **Action:** `enter {trade_def, entry_mode?}` · `watch` · `alert` · `pass`; optional branch-specific stop override (defaults to trade_def stop).
- **Invalidation:** same grammar; true → branch dead, logged as a prediction record (calibration).
- **`mirror: true`** auto-generates the opposite-side branch.
Example — Second Chance long on a PDH Range Break:
```
IF   RangeBreak(PDH).accepted AND event(retest) AND price holds PDH
     THEN close_above(prior_bar) within 3 bars
ACTION enter second_chance, entry_mode: backside
INVALIDATE price closes below PDH AND NOT recovers within 1 bar
```

### 10.6 Adds / scale-ins — PARKED (RULED)
`add_policy` slot reserved, default `none`, enum empty. Revisit when own-data or doctrine exists; fills already captured by card + prediction record.

## 11. Day 3 liquidity trap (RULED criteria; PLACEHOLDER definition)

**Registry status flag:** `status: candidate | cardable` — flip on Dejan's ruling. While candidate: radar may flag, no card, no grade; every candidate instance logged as a prediction record.

**Graduation requires all five (RULED):**
1. Definition in taxonomy terms — preconditions as predicates over existing primitives only (new object → setups-session amendment first).
2. Replay-detectable — loose candidate detector produces instances over the archiver corpus.
3. n ≥ 30 ruled instances (fired / trap / didn't fire) — recognition rulings, not trades.
4. Discriminable from nearest neighbours (Day 2/Day 3 continuation, Overextension): confusion rate ≤ threshold (config).
5. ≥ 1 trade_def mapped, stop/exit from §10.2 enums, nothing bespoke.

**PLACEHOLDER definition (default rules — edit/extend at trade-details population; no cheat sheet found yet):**
- Precondition: directional move on day count = 3 (Day 2 continuation held); open extends beyond the Day-2 extreme or gaps in trend direction with `prior_context: exhaustion`.
- Trap event: price fails to hold beyond the prior-day extreme — `close_through` back inside on working TF (late participants trapped).
- Category default: Mean Reversion. Mapped trade candidates: Rubberband (countertrend), Bella Fade.
- Stop: `structural_extreme {ref: trap-day extreme, buffer: spread, floor}`; exit: ladder → VWAP / prior-day level.

## 12. Population plan (RULED process)
Session ruled schema + enums; per-trade population is offline data entry: Dejan pastes cheat sheet → Claude drafts filled `trade_def` → Dejan rules conflicts/ambiguities only. **Batch 1 = the six sheets in hand** (Hitchhiker, Back$ide, Rubberband, Second Chance, Fashionably Late, Big Dog) + Cameron H grid as `valid_setups[]` data for all 21 trades. Rubberband source of truth = Rubber Band Playbook Rev1 deck (trainer chat rulings) over the raw SMB sheet where they conflict (stop = extreme candle + spread buffer + floor). Further batches in Dejan's order. Trade classes swing / options: defined when Dejan takes them up.

## 13. Spikes / research (carried + added)
- Carried from v0.4 §11: TradingView MCP internals; put/call; BTC/VIX ownership; dispersion measure.
- **Replay validation** of dynamic definitions: consolidation 2-touch rule, leg=wave alias, Extension paths A/B thresholds, pivot N=2, `failed_trap` N — tune from archiver corpus.
- Day 3 liquidity trap cheat sheet — Dejan to locate (SMB chatbot pull acceptable).

## 14. Open PROPOSED items awaiting ruling
None. All defaults marked config or PLACEHOLDER are editable at population.
