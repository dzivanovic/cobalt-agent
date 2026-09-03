# Trading Taxonomy — Draft v0.4
Setups session 2026-09-01 (closed). Supersedes v0.3. All v0.3 RULED content carries forward unless amended here.
Legend: **RULED** = Dejan confirmed · **PROPOSED** = Claude's draft awaiting his call · **SPIKE** = empirical check before ruling · **DEFERRED** = parked to a named session.

---

## 0. Cross-cutting laws (RULED 09-01, setups session)

**Modularity / shift-on-the-fly:** trading changes; what is true today may not be true tomorrow. Every threshold in this document (ATR gap threshold, RVOL cutoffs, significance thresholds, VOLD bands, 5-ATR/5-day, window boundaries, in-play cap) is **config, never code**. Enums are extensible without schema migration. Setup definitions live as data — a definition change is an edit, not a rebuild.

**Calibration loop (generalizes var 12):** every scored object — catalyst grade, setup grade, trade grade, per-variable scores — persists as a **prediction record**: score + WHY at scoring time, outcome joined later. The corpus answers "when we score a catalyst 9, what fraction behave like a 9" and drives re-scoring proposals. Cobalt **proposes** re-scores from this data; Dejan approves; scoring rules never self-modify (non-negotiable 12). n ≥ 30 before any proposal carries weight. Schema requirement on every graded object, not a new engine today.

## 1. Spine (AMENDED)

```
Market regime → Sector state → In-Play ticker → Category → Setup → Trade
```

**Category is computed per instance from bar character, not hard-wired to setup name (RULED):** continuous same-direction bars, high AND expanding volume, bars same size or larger = **Momentum** — whatever day of the move (Day 2/3 can be Momentum on the daily). Steady swing-high/low sequencing on ordinary volume = Trend. Each setup keeps a *default* category; observed character overrides it. Category = computed attribute.

## 2. Category → Setup mapping (defaults)

Momentum: Gap & Go, Range Break · Trend: Day 2, Day 3 · Mean Reversion: VIR, Overextension, GUIR, GDIS, **Day 3 liquidity trap (candidate — no card until graduation, RULED)** · Changing Fundamentals: placed (§3.4), Momentum default on day 1, feeds Trend.

## 3. Structure objects (amendments to v0.3 §3)

### 3.1 Consolidation primitive (NEW, RULED)
Daily consolidation = an **inside day measured open-to-close**: `min(O,C) ≥ prior min(O,C) AND max(O,C) ≤ prior max(O,C)` — wicks excluded on both sides. One such day = consolidation. Consecutive inside days extend it; exit anchors the new base. Intraday (Momentum legs): same body-inside rule on the working timeframe — PROPOSED, confirm at trades pass. Consumers: Extension reset, Momentum leg sequencing, Big Dog compression.

### 3.2 Extension (AMENDED, RULED)
Consolidation **resets the day count AND re-anchors the 5-ATR distance** — both restart from the post-consolidation base. The 5-in-5 run must be consecutive directional days.
Lifecycle: `building → extending → culminating → reverting → backside | resuming`; consolidation event → back to `building` with re-anchored base. `culminating` = very long HV bar in trend direction; `reverting` starts at the snapback bar.

### 3.3 Gap object + family (RULED)
Single-session event. Threshold to instantiate: **ATR units** (config).
`{direction, size_pct, size_atr, prior_close, premarket: {PMH, PML, pm_volume, pm_rvol, pm_behavior: holding | fading | extending}, catalyst_ref, gap_into: Level_ref | null, prior_context, state}`
Lifecycle: `open → filling → filled` + continuous `fill_pct` (partial fills carried by `fill_pct`, no "held" state).

**Family — discriminator is `gap_into`:**
- **Gap & Go (Momentum):** gap in catalyst direction into clear air (no significant opposing level in path, significance threshold config); premarket holds/extends the gap.
- **GUIR (MR):** gap up landing at a significant level **without breaking it, or rejecting the break attempt**. A sustained break through the level = breakout (momentum territory), not gap-into. **GDIS** = mirror into support.
- One gap can be both candidates premarket — resolved by IF/Then branches at the open interaction, not by premarket classification.
- The level gapped into may be any timeframe; multi-session weight lives in Level significance, no multi-session gap logic needed.

**`prior_context` (RULED):** `fresh` = new move · `continuation` = the Day 2/3 setups themselves (ties to spine, no double duty) · `exhaustion` = gap in trend direction after extended run (proxy: Extension `distance_from_band` positive), raises reversion probability.

### 3.4 Changing Fundamentals (RULED)
**A fundamental-analysis concept — defined by the news, not by levels.** Level breaks are a byproduct of the move; level size irrelevant (a 3-week level can still be significant). Gap **optional** — news and move can happen mid-day.

**Split (RULED):**
- **Instantiation (news side):** a catalyst of fundamental-repricing class hits — news forcing the market to revalue the company. Binary classification, any time of day.
- **Confirmation + setup grade (price side only):** extreme RVOL, HV bars, directional repricing; levels broken + price discovery recorded as byproduct evidence. News quality scored once, in the catalyst grade — anti-double-count preserved (class membership is binary, not a score).

Fields: `{catalyst_ref (required), event_time, gap_ref (optional), rvol, hv_bars, levels_broken[], price_discovery, state}`
Lifecycle: `pending → confirmed → active → exhausted | dead`; `pending → dead` if price never confirms — **failed-to-confirm cases kept as calibration data**. `active` feeds Day 2/3 continuation; CF is a Theme-head candidate.
Detection note: instantiation needs news classification (research engine / "why is it moving" resolver); until then, price anomaly prompts a human CF call.

### 3.5 Range (AMENDED, RULED)
`bound_type: flat | converging | channel` + `convergence_shape: symmetric | descending | ascending` (Bouncy Ball = `descending` onto flat support). Bounds fitted from §3 swing primitives; ≥ 2 touches per side to instantiate (config); bound slopes classify the type. **Big Dog / Small Dog breakouts fire from `flat` or `channel` (sloping up or down), break direction independent of slope.**
Range Break lifecycle: `forming → break_attempt → accepted | failed_trap`; promotion policy (close-through / two-bar / acceptance) → trades pass.

### 3.6 Ticker `volatility_state` (RULED)
`contraction | neutral | expansion`, daily + intraday update. Measure (config): short vs baseline realized range, e.g. ATR(5)/ATR(20) ratio with bands; bar-character volume progression can accelerate the intraday flip.
**Role: filter-flag, not score.** Neither gate nor variable — context metadata. Off-state setups (e.g. VIR on `expansion`) flagged degraded but still cardable; colors radar and WHY. Feeds in-play entry test and the auto-adapting ATR-denominated thresholds.
`contraction` → Big Dog/Small Dog stalking; `expansion` → momentum/extension live, range fades dangerous.

### 3.7 Events: Change-in-Character + ticker divergence (RULED)
Both are **events** — timestamped, attached to existing objects, feeding radar and WHY.

**CiC — bar-level detection only; tape/sub-minute excluded from system scope (tape is human by law).** Triggers (config-armed per context):
1. first opposing HV bar after a directional run
2. bar-progression break: expanding same-direction bars → first larger opposing body
3. first close beyond a structure that had held (e.g. 2-min trail / rising 9-EMA structure)
4. volume regime flip: expanding volume with price → expanding against price

Payload: `{ticker, timeframe, evidence[], attached_to: Extension | Trend-sequence | Range}`. Consumers: Extension transitions, exit logic (trades pass), radar highlight.

**Ticker divergence:** `{ticker, reference: sector | market | theme_head, direction: stronger | weaker, measure}` — fires on material decoupling (RS delta over window ≥ threshold, config). Divergence vs `head` = sympathy-break detector → sympathy thesis invalid.

## 4. Market layer (amendments)

**Dispersion (RULED):** regime record gains `dispersion: low | normal | high` — uniformity of the market's move. `high` = index masking offsetting sector moves; stock-picking tape. Compute (config): sector-direction spread weighted by size, or breadth-vs-index disagreement. **Resolution: dispersion `high` → var 4 (market alignment) scores neutral, weights untouched**; WHY records "dispersion high, market read unreliable."

**Headline-driven modifier (RULED):** regime flag — tape trading on macro headlines rather than internals. Sources: calendar density (merged Finviz + ForexFactory) + clustering of regime events with `cause: market-wide catalyst`. **Context flag, not a score input.** Any hard-gating of setup families around events runs through the §9 windowing machinery (calendar-event windows) — one gating system, not two.

## 5. In-Play layer (RULED, upgraded)

**Two tiers:**
- **In-play set** — Cobalt's radar, **cap 50** (config), out of the 5,000–8,000 universe. Grows and shrinks intraday.
- **Focus list** — human conviction, ~4 names; the IF/Then watchlist (cap 3–5, config).

**Sources:** 4 static TradingView watchlists + 4 dynamic Finviz watchlists + future specialized watchlists (Finviz or Cobalt-native) stalking Dejan's trade types.

**Object:** `in_play {ticker, catalyst_ref | null, rvol, atr, atr_state, liquidity, tradability_snapshot, source: premarket_scan | intraday_alert | carryover, reason, first_flagged, expires}`
Lifecycle: `candidate → in_play → fading → expired`; `carryover` re-qualifies multi-day names (CF `active`, Day 2/3) without the fresh-catalyst test.
Entry test (all config): RVOL ≥ threshold, ATR/price ≥ threshold, liquidity floor, catalyst OR technical qualification.
**PROPOSED (default yes):** pure RVOL anomaly with no catalyst and no technical qualifier admitted as `reason: unexplained` — the resolver's chase list.

**Continuous re-scoring radar:** Cobalt recalculates conviction across the full set on the fly (setup grades, object states, regime/sector context) and surfaces what's breaking out right now — ranking is a query over live object state, not a new engine. **Honesty note:** true EV ranking requires var 12 (own outcomes, n ≥ 30 per setup); until that corpus exists the radar ranks on setup grade + object state — conviction proxy, upgrading to EV as the calibration loop matures.

**Role: precondition, not a variable** — no setup instantiates on a name outside the set.

## 6. Prior-day enum (RULED)

Gains `inside | reset` only — `rest` cut (not in Dejan's read; folds into `inside` with the relaxed-body case).
- `inside` — the §3.1 consolidation day (incl. near-inside drift days).
- `reset` — countertrend day deep enough to unwind the extension (retrace ≥ x% of prior leg or tag of a re-anchor level, config) without breaking structure.

## 7. Card registry (amendments)

- **Window-fit variable ADDED** (see §9): 1–10 × weight with WHY — how well the trigger's window matches the setup's best window. Judgment-scored until per-setup window expectancy validates from outcomes (n ≥ 30).
- **`dynamic` flag per variable (RULED):** marks variables legitimately re-scorable intraday while a card is open (window-fit, market alignment) vs frozen-at-card (catalyst quality, level significance at entry). Dynamic vars re-scored by Cobalt on state change; card shows original vs current; **original grade immutable** (prediction record scores the entry decision; drift is context). **Display-only until Guardian exists (RULED)**; score-decay card retirement = config-off.

## 8. IF/Then plan branches

Unchanged from v0.3, plus: window membership (§9) is an input to the rules gate — a trigger firing in a setup's blocked window fails the gate, no card.

## 9. Time layer (NEW, RULED)

**Session clock — 24×5 (RULED; prep for the 24-hour trading move):**
```
premarket 04:00–09:30 → RTH 09:30–16:00 → aftermarket 16:00–20:00
→ market_reset 20:00–21:00 (no-trading window, hard-blocked) → overnight 21:00–04:00
```

**RTH intraday windows (PROPOSED v0 defaults, boundaries config):**
`open_drive 9:30–10:00 · morning 10:00–11:30 · midday 11:30–14:00 · afternoon 14:00–15:30 · close 15:30–16:00`

**Window primitive:** `{name, start, end, source: clock | calendar_event}`. Calendar-event windows (FOMC, Fed speaker ± buffer, data drops) come from the merged calendar — same object; this is where headline-driven hard-gating lives (§4).

**Two roles (RULED):**
1. **Gate input:** per-setup `allowed_windows[]` / `blocked_windows[]` (config). Blocked-window trigger fails the rules gate. Empty = unrestricted. `market_reset` blocked for everything.
2. **Window-fit variable:** §7.

## 10. Deferred → Trades pass (NEXT)

Carried from v0.3 plus session additions:
1. Trades column per setup (trigger, stop, exit trigger — 09-01 rule) · snapback entry timing · intraday extension qualification · leg count.
2. Radar trade types mapped onto object states (Rubberband / Back$ide = Extension phases).
3. Exit/stop type enum (time stop, two-bar rule, 2-min bar trail, passive, trailing variants); CiC events as exit inputs.
4. Confirmation policy per trigger (close-through / two-bar / acceptance) — incl. Range Break `break_attempt → accepted` promotion; stricter policy under headline-driven flag.
5. Entry mode front-side vs backside + sizing interaction.
6. IF/Then condition grammar (time-of-day anchors, duration windows, level interactions, multi-step sequences, branch-specific stops, inverted branches) — now with §9 window objects available as grammar terms.
7. Intraday swing pivot N; intraday consolidation rule confirmation (§3.1).
8. Adds/scale-ins (parked).
9. Day 3 liquidity trap graduation criteria (candidate → cardable).

## 11. Spikes / research
- TradingView MCP: internals-as-numbers + ToS + $UVOL/$DVOL per-exchange ingestability.
- Put/call usage at regime/sector/stock level (Dejan).
- BTC/VIX ingestion ownership.
- Dispersion measure selection (sector-spread vs breadth-vs-index disagreement) — pick after regime snapshots accumulate.

## 12. Script dispositions (unchanged from v0.3)

## 13. Open PROPOSED items awaiting ruling
1. RTH intraday window v0 boundaries (§9) — defaults stand unless re-cut.
2. `reason: unexplained` in-play admission (§5) — default yes.
3. Intraday consolidation = body-inside on working timeframe (§3.1) — confirm at trades pass.
