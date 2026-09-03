# Trading Taxonomy — Draft v0.6
Batch 1 fold 2026-09-02 (closed). Supersedes v0.5 in full. v0.5 was an amendment layer on v0.4; so is this document — **all v0.4 RULED content not amended in v0.5 or here carries forward** (v0.4 remains the base for §6–9 and everything not restated). Schema **v0.3**.
Legend: **RULED** = Dejan confirmed · **DwV** = decided with veto (Claude's fold consequence, stands unless vetoed) · **PLACEHOLDER** · **SPIKE** · **DEFERRED**. Fold collisions 1–3 (§14) RULED 09-02. Source tags `[A.n]` = TRADE-DEFS-BATCH1-v0_1 §A item n (all RULED 09-02).

---

## Change log v0.5 → v0.6

| # | Change | Source | Status |
|---|---|---|---|
| 1 | `family` → `family[]`, enum `opening_drive · continuation · range_break · reversion · time_window` | A.1 | RULED |
| 2 | `class` = management shape (scalp = one leg out, tf_ceiling 15-min; move2move = hold for leg 2, no ceiling) | A.2 | RULED |
| 3 | `stop_management` gains `raise_to {placement, on: event}` | A.3 | RULED |
| 4 | Structural refs gain `cross_point {a,b}`, `turn_low` / `snapback_candle` = current tracked extreme | A.4, A.5 | RULED |
| 5 | Range gains `duration`, `wick_ratio`; `shape` DROPPED — diverging bounds = no Range at all; `bound_type` unchanged | A.6–8 + Ruling 1 | RULED |
| 6 | `flat(indicator, window)` / `slope_norm` predicate | A.9 | RULED |
| 7 | `RangeBreak(HTF).day_count` | A.10 | RULED |
| 8 | `Leg(impulse)`; Leg gains `role` | A.11 | RULED (role field DwV) |
| 9 | §4 Big Dog / Hitchhiker / Rubberband rows rewritten | A.12–14 | RULED |
| 10 | Trigger-variants slot DROPPED (re-add only with real-world data) | Ruling 2 | RULED |
| 11 | Laws: advisory-exit, per-trade stops, stop-nudge, sheet reading, attempts, standard quality factors | A.15–20 | RULED |
| 12 | Stop-nudge = check-and-move, not additive to a trade's `fixed` buffer | fold | DwV |
| 13 | `stop_management` becomes a ladder `[]`, each entry with `on: event` | populated defs | DwV |
| 14 | Structural refs gain `entry` (alias `breakeven`) and `leg_end(n)` as anchors | populated defs | DwV |
| 15 | Schema gains `radar_watch[]` and `preferred_windows_ref` | populated defs, A.18c | DwV |
| 16 | Exit-target and event params defined per type | populated defs | DwV |
| 17 | Stop buffer default = **fixed 0.02** for every trade unless its sheet says otherwise; `spread` not used | Ruling 3 | RULED |
| 18 | `max_attempts` = doctrine default; rules gate intersects with personal re-entry rule, stricter wins | A.19 + 08-27 rule | DwV |
| 19 | §12 population plan: Batch 1 closed, Batch 2 defined, Gap & Go = setup sheet | session | RULED |
| 20 | §13 replay backlog additions; visual-similarity backlog | §A backlog | RULED |

---

## 0. Cross-cutting laws

**Anatomy-only law (RULED 09-02):** the taxonomy carries no personal trading rules — no entry cutoffs, no "no-trade windows", no risk dollars. Windows describe market anatomy; trading is moving to 24×5. Dejan's live rules live in the printed card / rules-gate config / future Guardian (advisory), never here. Only structural exception: `market_reset 20:00–21:00`.

**Timeframe-agnostic trigger law (RULED 09-02, wording amended [A.2]):** a trade triggers on a bar of its own `working_timeframe` (trader preference per trade). Objects on timeframes above the working timeframe are preconditions and context, never triggers. No fixed timeframe anywhere. `class` is **not** a timeframe: it is the management shape (§10.1); the only timeframe constraint a class carries is the scalp `tf_ceiling: 15-min` on the working timeframe (a working TF above 15-min is not a scalp). Hold duration is unconstrained by class.

**Branch-vs-taxonomy boundary (RULED):** an IF/Then branch is Dejan's authored plan for one name on one day — his data; personal timing inside a branch is legitimate.

**Dynamic definitions (RULED):** consolidation rule, leg=wave alias, Extension instantiation thresholds, pivot N, Range.duration bands, flat_threshold per indicator, Range.wick_ratio threshold, break_volume_sigma_bars — all `config, dynamic`: must stand archiver-corpus replay before counted as solidified (§13).

**Advisory-exit law [A.15]:** every `on_cic`, `stop_management`, exit and time-stop field is a warning to the human, never an order — Cobalt never executes (non-negotiable: no platform integration). Revise from real trades.

**Per-trade stop rules [A.16; buffer default RULED 09-02]:** no uniform stop *placement* across trades — refs per sheet, carried in each `trade_def.stop`. Buffer default = `fixed 0.02` for every trade unless its sheet states a different buffer; `spread` is not a buffer (spread is a tradability gate). The 08-27 minimum stop-distance floor lives in the rules gate; `floor: config` in a trade_def points there.

**Stop-nudge law [A.17] (rules gate, card stage):** a stop is never exactly on the structural price, a round dollar, or a x.x0 cent level — 1–2¢ beyond. The sheets' "$0.02" is this rule (order-cluster avoidance, not a noise buffer). **DwV clarification:** the gate nudge is check-and-move, not additive — it moves a card's stop only when the trade_def-computed stop (structural ref ± its `buffer`) lands on a forbidden price; a `buffer: fixed 0.02` already satisfies "not on the structural price", so the gate touches it only for round-dollar / x.x0 collisions.

**Sheet reading laws [A.18]:** (a) every SMB scalp sheet is TF-templated — structure fixed, "1-min bar" = working TF; (b) "low of the day" = the current tracked low of the move (`turn_low` / `snapback_candle`), not necessarily the session LOD, unless the image shows otherwise; (c) `preferred_windows[]` populated from the sheet's "ideal times", mapped to the RTH sub-window enum; sheet wording kept in `preferred_windows_ref` — window-fit variable only.

**Attempts [A.19]:** `max_attempts` editable per trade; sheet value is the default. **DwV:** it is doctrine (anatomy), not Dejan's rule — the rules gate intersects it with his personal re-entry rule (08-27: #2 needs written new info, #3 = stand-down + ticker closed); the stricter of the two governs the card.

**Standard quality factors [A.20]:** every card carries `setup_relation`, `market_alignment`, `sector_alignment` (§1 misalignment = penalty variable, never a forbidden cell).

## 1. Spine (COMPLETE)

```
Market regime → Sector state → In-Play ticker → Category → Setup → Trade
```
Category computed per instance (v0.4). Instance **direction** computed from setup-instance state (§5). One card per trade instance; card cites `trade_def` + setup instance + matched IF/Then branch. Misalignment = penalty variable.

## 2. v0.4 §13 open items — resolved (RULED 09-02, unchanged)

1. RTH sub-windows (anatomy only, config): `open_drive 9:30–10:00 · morning 10:00–11:30 · midday 11:30–14:00 · afternoon 14:00–15:30 · close 15:30–16:00`; `market_reset` structural.
2. Unexplained-RVOL in-play admission: yes — `reason: unexplained`, resolver's chase list.
3. Consolidation: daily = inside-day body rule, daily-only, sole consumer Overextension day-count/5-ATR reset. Intraday consolidation = a Range instance at micro scale — instantiation **2 touches per side** (single config value). No bar count. Dynamic.

## 3. Structure primitives

### 3.0 Range — fields (amended)
Instantiation per §2.3 (micro) or level-defined (HTF). Fields added/amended:
- `duration` (start → now) [A.6] — data field. Consumed as a **precondition band per trade** (Hitchhiker 5–20 min; Big Dog ≥ 45 min default) and as a quality factor. Config, dynamic.
- **`shape` DROPPED (Ruling 1, 09-02).** v0.4 `bound_type: flat | converging | channel` stands as the only shape field; slope is irrelevant to instantiation and to Big Dog (converging with or without slope, parallel channel with or without slope all qualify). **Diverging bounds (support and resistance moving apart) are not a consolidation — no Range instantiates.** Consequence: Big Dog carries no shape clause; any instantiated micro-Range qualifies.
- `wick_ratio` (avg wick ÷ avg body over the range) [A.8] — data field; "choppy consolidation" avoid threshold = config, dynamic.
- `height` (bound distance), `volume_contraction` (range avg vol ÷ prior avg), `position` (range location within day range / LOD→VWAP) — data fields already consumed by Batch 1 quality factors; named here so the registry has one spelling. DwV.

### 3.1 Leg = wave (RULED, data-level alias)
`leg {direction, start, end, terminated_by: pullback | consolidation, range, volume_profile, role}` — one directional move terminated by the first pullback (≥1 opposing bar) or consolidation (micro-Range) event. `wave` = alias on the same record (changeable). **`role: opening_drive | impulse` [A.11, field DwV]:** `impulse` = any directional leg preceding a range; `opening_drive` = the impulse leg that starts at the RTH open (a subset). Hitchhiker requires `Leg(opening_drive)`; Big Dog accepts `Leg(impulse)`. Consumers: Extension `leg_count`; exit targets `leg_end(n)`; `raise_to` events.

### 3.2 Extension — intraday instantiation (RULED, unchanged)
Paths (A) culminating bar character (HV bar ≥ MA+2σ that is also the run's widest body) or (B) ≥ 1.25 ATR from the open with `catalyst_ref: null`. Snapback watched only once instantiated. Distance from VWAP / ATRs from open = card quality factors, never gates. `leg_count` = legs since base.
`backside` phase: HH+HL swing sequence above rising 9 EMA — **≥1 HH and ≥1 HL (config)**; plus micro-Range above the 9 EMA for Back$ide.

### 3.3 Swing pivot N (RULED, unchanged)
N = 2 bars each side, single config, per-TF override off by default. Pivots serve structure, never triggers.

### 3.4 Range Break (amended)
Lifecycle `forming → break_attempt → accepted | failed_trap`; timestamped `retest` event on an accepted break (may recur). Promotion default `close_through`; `failed_trap` = close back inside within N bars (config).
**`RangeBreak(HTF).day_count` [A.10]:** for a Range Break instance on a daily / HTF level, `day_count` = sessions since acceptance, the break session = 1 (same day-count machinery as Overextension). Predicate `RangeBreak(HTF).day_count == 1` = "day-1 HTF breakout" — avoid for Back$ide and Rubberband.

### 3.5 Indicator-slope predicates [A.9]
`slope_norm(indicator) = regression slope per bar ÷ ATR(working_tf, 14)` — working-TF ATR, never daily.
`flat(indicator, window)` ⇔ `abs(slope_norm) < flat_threshold[indicator]` over `window` bars. Separate threshold keys for EMA9 and VWAP; window per consumer (EMA9 avoid = 15 min ÷ working TF; VWAP at trigger = 5 bars). Config, dynamic. Both are §10.5 grammar atoms.

### 3.6 Structural references (consolidated; consumed by stops, anchors, exits)
`snapback_candle` / `turn_low` (aliases — the **current tracked extreme of the move**, [A.5, A.18b]) · `low_of_day` / `high_of_day` (session extreme, distinct from the above) · `consolidation_low` / `range_base` · `turn_candle` · `recent_higher_low` (micro-Range base pivot) · `cross_point {a, b}` (price at an indicator cross; also the `indicator_cross` trigger's price stamp, [A.4]) · `entry` (fill price; alias `breakeven`, DwV) · `leg_end(n)` (DwV) · any `Level_ref`.

## 4. Radar trades → object states (RULED, rows amended per A.12–14)

| Trade | Precondition (object state) | Trigger |
|---|---|---|
| Rubberband | Extension `culminating` (intraday; daily as context). `radar_watch`: culminating near `Level_ref(HTF)` → watch/checkpoint state, **never a trigger** — the leg may blow through it [A.14] | **one trigger:** snapback bar_break — both preceding candles cleared (2, config), any colour, doji in the cleared set = plus; the event *is* the `culminating → reverting` transition. Former Variant B lives on as quality factors (ATRs from open, HTF-level proximity/significance, prior-session rehearsal) and a branch-level target override |
| Back$ide | Extension `backside` + micro-Range with `low > EMA9` and `EMA9.slope > 0` | range_break |
| Fashionably Late | Extension `reverting \| backside`; `slope_norm(EMA9) > threshold` AND `slope_norm(VWAP) ≤ threshold`; avoid `flat(EMA9, 15 min ÷ working TF)` between turn and cross | indicator_cross (EMA9 × VWAP), stamps `cross_point` |
| Hitchhiker | `Leg(opening_drive)` terminated by consolidation (not pullback) + micro-Range in upper ⅓ of day range + **`Range.duration ∈ [5, 20] min` (config)** — the Hitchhiker/Big Dog discriminator [A.13] | range_break |
| Second Chance | Range Break `accepted` + `retest` event | sequence (break close_through → retest → turn-candle close-through) |
| Big Dog | `Leg(impulse)` terminated by consolidation + micro-Range instantiated (any `bound_type`, Ruling 1) + `volatility_state: contraction` + `Range.height ≤ 50% day range` + `Range.duration ≥ config` (45 min default). **`above PDH` and `> 75% of day above open` DEMOTED to quality factors** (DELL 2026-09-02 exemplar fails both and worked) [A.12] | range_break |

Radar reads object states, not trade detectors.

## 5. VIR resolution (RULED, unchanged)
VIR is a setup unlocking countertrend trades in either direction; `two_way` removed from the relation enum; every trade_def side-symmetric; instance direction computed from setup-instance state.

## 10. Trade layer — schema v0.3

### 10.1 `trade_def` registry (data)
```
trade_def {
  id, name, aliases[],
  family[]: opening_drive | continuation | range_break | reversion | time_window,   # extensible; a trade may carry several [A.1]
  class: scalp | move2move | swing | options,          # management shape [A.2]: scalp = one leg out (tf_ceiling 15-min);
                                                        # move2move = hold through a pullback for leg 2, no ceiling; swing/options defined when taken up
  sides: long+short (inverted),
  valid_setups[]: {setup_ref, relation: with_trend | countertrend},   # Cameron H grid as data (Batch 1 §C)
  instance_direction: computed from setup-instance state,
  working_timeframe: config (trader preference), tf_ceiling: 15-min (scalp class only),
  entry_mode: front_side | backside,
  preconditions[]: predicates (§10.5) | {text} fallback,
  radar_watch[]: predicates → watch/checkpoint state, never entry,     # v0.3 (DwV)
  trigger: {type: bar_break | range_break | indicator_cross, params, confirmation_policy}
         | {type: sequence, steps[]: {name, predicate, confirmation_policy}},
  stop: {type, params: {ref, buffer, floor}, evaluation},
  stop_management[]: {type, params, on: event},          # ladder; default on: entry (DwV) — advisory
  exit[]: {fraction, target_type, params, evaluation, computable: cobalt | human},   # advisory
  on_cic: {triggers[], action},                          # advisory
  max_attempts: config (sheet default),
  add_policy: {type, params},                            # reserved, default none (§10.6)
  avoid[]: predicates | {text},
  quality_factors[]: → card variables; always includes setup_relation, market_alignment, sector_alignment,
  preferred_windows[]: RTH sub-window enum → window-fit variable only,
  preferred_windows_ref: text (sheet wording),           # [A.18c]
  reference_stats: external metadata (SMB win rate / R:R), never EV
}
```
**Trigger variants: DROPPED (Ruling 2, 09-02).** v0.5's reserved slot had Rubberband A/B as its sole example; A.14 collapsed that to one trigger. One trigger per trade_def; a variants mechanism returns only as an amendment backed by real-world data.

### 10.2 Enums (extensible)
**Stop placement:** `structural_extreme {ref: §3.6 ref, buffer: fixed <¢> (default 0.02), floor: config → rules gate}` · `measured_fraction {anchor_a, anchor_b, fraction}` · `level {level_ref, buffer}`
**Stop management** (each entry `on: event`, default `entry`): `fixed` · `breakeven_at {R}` · `raise_to {placement: <any stop-placement>, on: event}` [A.3] · `trail_ma_close {ma, tf}` · `trail_bar {n}` · `time_stop {duration, condition}` · `passive`
**Exit targets** (params, DwV): `rr_multiple {r}` · `vwap` · `level {level_ref}` · `measured_move {anchor_a, anchor_b, projected_from, multiple}` · `leg_end {leg_index | break_leg}` · `bar_break_reverse {bars, after?: event}` · `ma_close {ma, tf}` · `window_end {window}` · `cic_event`
**Events** (for `on:`, `after:`, `event()` atoms): `entry` · `exit_leg(n)` · `leg_end(n)` · `retest` · `stop_hit` · `cic(n)` · `consolidation` · `divergence`
**Evaluation:** `touch | close_through`. Hard stops = touch; invalidation law = close_through on working TF.
**CiC as exit input:** `on_cic {triggers: [1..4], action: exit_all | exit_leg | tighten_to: breakeven | trail_bar}`.

### 10.3 Confirmation policy (RULED, unchanged)
Per trigger: `intrabar · close_through · two_bar · acceptance {bars | time}`. Entries mostly `intrabar` (Second Chance steps 1 and 3 `close_through`); invalidations `close_through`. Headline-driven regime flag → one-notch step-up, one config table.

### 10.4 Entry mode + sizing (RULED, unchanged)
`front_side` = entry at the turn / break bar; `backside` = entry after structure confirms. No direct entry-mode → size coupling; one sizing path: grade → risk key → shares = risk ÷ stop distance.

### 10.5 IF/Then condition grammar (RULED; atoms extended)
Branch = `{condition, action, invalidation}`. Atoms as v0.5 plus: `slope_norm(indicator) {>,<,≤,≥} x` · `flat(indicator, window)` · `Object.field` for every §3.0/3.4 field (`Range.duration`, `Range.wick_ratio`, `RangeBreak(HTF).day_count`, `Leg.role`, `Leg.terminated_by`) · `event(name)` over the §10.2 event enum. Combinators, actions, invalidation, `mirror` unchanged.

### 10.6 Adds / scale-ins — PARKED (unchanged)

## 11. Day 3 liquidity trap (RULED criteria; PLACEHOLDER definition — unchanged)
Graduation criteria 1–5 and the placeholder definition carry forward from v0.5, with the placeholder stop buffer re-pointed to the default `fixed 0.02` (Ruling 3).

## 12. Population plan (RULED process; status updated)
Offline batches: Dejan pastes full 2-page sheet → Claude drafts filled `trade_def` → Dejan rules conflicts only.
- **Batch 1 — CLOSED 09-02:** Hitchhiker, Big Dog, Second Chance, Back$ide, Fashionably Late, Rubberband → TRADE-DEFS-BATCH1-v0_1.md (schema v0.2 + §A; re-validated against v0.3 at the Code commit). Cameron H grid as `valid_setups[]` for all 21 trades.
- **Rubberband source of truth:** Rubber Band Playbook Rev1 deck + 09-02 rulings over the raw SMB sheet; stop = extreme candle + fixed 0.02 + floor (RULED 09-02; overwrites v0.5's "spread buffer"). Rev2 note to the deck pending.
- **Batch 2 — next session (sheets in hand, 7):** 9 EMA Scalp, Back-Through Open, Bella Fade, Bouncy Ball, First VWAP Pullback, Gap Give and Go, VWAP Continuation. One at a time, same (a)(b)(c) process.
- **Gap & Go = a setup sheet, not a trade** (one page, no entry/stop/exit rules) — excluded from trades; its content ("best trade types: momentum, trend continuation") is setup-level metadata for `gap_and_go` (v0.4 setups) — fold there if wanted, otherwise reference only.
- Trade classes swing / options: defined when Dejan takes them up.

## 13. Spikes / research (carried + added)
- Carried: TradingView MCP internals; put/call; BTC/VIX ownership; dispersion measure; $UVOL/$DVOL via TradingView MCP; Day 3 liquidity trap sheet (SMB chatbot pull acceptable).
- **Replay validation** of dynamic definitions over the archiver corpus: consolidation 2-touch rule · leg=wave alias (first consumer = Hitchhiker wave exits) · Extension paths A/B thresholds · pivot N=2 · `failed_trap` N · **Range.duration bands (5–20 / ≥45)** · **flat_threshold per indicator (EMA9, VWAP)** · **Range.wick_ratio threshold** · **break_volume_sigma_bars**.
- **Backlog (post-MVP, after grading engine):** visual-similarity conviction variable — rendered working-TF chart → local vision model or image-embedding nearest-neighbour vs exemplar library → one semaphore dot with WHY; never a trigger; n ≥ 30 hand-graded before it lights; blind mixed-deck validation; shadow mode first.

## 14. Fold collisions — RULED 09-02
1. Range `shape` dropped; `bound_type` unchanged; diverging bounds = no Range; Big Dog shape-free.
2. Trigger-variants slot dropped; re-add only with real-world data.
3. Stop buffer default fixed 0.02 for all trades unless a sheet says otherwise; no spread buffers.
No open PROPOSED items. DwV items stand unless vetoed.
