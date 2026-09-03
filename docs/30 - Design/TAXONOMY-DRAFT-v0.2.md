# Trading Taxonomy — Draft v0.2
Sitting 2026-08-31 → 09-01 (closed). Supersedes v0.1. Covers spine, categories, structure objects, market/sector/theme layers, trigger lifecycle, the card variable registry, grade ladder. Deferred: gap-family + Changing Fundamentals definitions (setups session), Trades column (trades pass).
Legend: **RULED** = Dejan confirmed · **PROPOSED** = Claude's draft awaiting his call · **SPIKE** = empirical check before ruling · **DEFERRED** = parked to a named session.

---

## 1. Spine (RULED)

```
Market regime        market-level state, tracked continuously by Cobalt
  └ Sector state     analysis layer (not a trade layer): RS vs market, sector catalyst
      └ Category     Momentum | Trend | Mean Reversion  (SMB's three)
          └ Setup    higher-TF filter, per ticker, directional: "worth watching?"
              └ Trade  intraday execution: trigger, stop, R:R
```
- Setup vs Trade per SMB doctrine: setup = why/when, trade = how.
- Regime and sector never select trades; they enter the card as scored variables (§7).
- Theme (§5) cuts across layers as a context object.
- SMB AI chatbot answers are the doctrine channel for SMB terms (RULED).

## 2. Category → Setup mapping (RULED)

| Category | Setups |
|---|---|
| Momentum | Gap & Go, Range Break |
| Trend | Day 2 Continuation, Day 3 Continuation (separate setups) |
| Mean Reversion | VIR, Overextension, GUIR, GDIS |

Also named by Dejan, not yet placed: **Changing Fundamentals** (appeared as a setup in his MRNA example). DEFERRED → setups session.

Definitions confirmed:
- **VIR** — fast movement between defined range high and low, never breaking out → mean-reversion trading at the edges.
- **Range Break** — price leaves a defined range on either side; arises from ANY in-range movement. Post-break character decides momentum vs trend.
- **Momentum** — explosive, high-volume, one-directional; leg → consolidation → leg → consolidation → (third leg).
- **Trend** — steady directional sequence of swing highs/lows.
- **Day 2** — continuation of day-1 trend. **Day 3** — day 1 momentum (fundamental change) → day 2 flat/compression → day 3 continuation.
- **Overextension** — see Extension gates (§3).
- **Gaps** — a function of premarket: the window between prior close and today's open; price either fills it or continues. Gap & Go / GUIR / GDIS definitions DEFERRED → setups session.
- **High-Volume S/R** — NOT a setup: a Level type + trade trigger.
- Every setup carries `direction` (RULED).

## 3. Structure objects (RULED: shared across setups; every object carries `timeframe`)

**Range** — VIR, Range Break
- range_high, range_low · bars/days held · tests of each edge · in-range character (volatile / compressing / drifting) · width (tight = "balancing") · edge volume profile

**Gap** — Gap & Go, GUIR, GDIS, Overextension (initiation)
- direction, size (% and ATR-multiple) · fill status · premarket volume · catalyst present · prior close, prior-day range

**Prior-day sequence** — Day 2, Day 3
- day-1 character (momentum / trend), range, close location · day-2 behavior (continued / compressed) · days since catalyst

**Level** — all setups (level-significance 1–10)
- price · type (S/R, VWAP, MA, prior-day H/L, HV node) · significance · times tested · volume at level

**Extension** — Overextension (daily), Rubberband precondition (intraday)
- initiation: gap + 1 HV bar / gap + 2–3 HV bars / standalone significant HV bar
- consecutive directional bars · bar-size expansion · culmination bar (longest + highest volume, same direction) · supplementary: RSI, distance from MA/VWAP in ATR
- **Daily gates:** ≥5 ATR within ≥5 days; 5+ bars minimum; 7–9 expanding bars = prime
- **Intraday:** no ATR gate, no bar minimum; qualification DEFERRED → trades pass
- Daily trade trigger: **snapback bar** — engulfs prior 1–2 bars on high volume in the reversion direction. Entry timing DEFERRED → trades pass.

Detection tier: Range, Gap, Extension, prior-day sequence = **cobalt**. Level significance = cobalt-computed + human override-with-reason.

## 4. Market layer

### 4.1 Regime record (structure PROPOSED, continuous tracking RULED)
```
regime: {state, direction, confidence, volatility, breadth, divergence_flag, ts}
```
- **States:** Range (with width attr: tight = balancing) · Trend up · Trend down · Momentum up · Momentum down
- **Modifier:** volatility high / normal / low
- **Events** (transitions): Breakout (range → momentum/trend) · Reversal (→ opposite or → range)
- **Not a state:** Rotational → sector layer. **Trend day** = Trend at full confidence.
- **Confidence** (PROPOSED): count of core internals confirming at threshold (0–4).

### 4.2 Internals (RULED set)

| Internal | Dimension | Dejan's threshold | Source |
|---|---|---|---|
| TICK | instantaneous pressure; swing amplitude → volatility | one-directional | ingest |
| Cumulative TICK | direction + persistence | ±10K | computed |
| VOLD | strength; divergence → reversal warning | ±3 | ingest |
| ADL | breadth count; divergence → turning point | ±20K | ingest |
| VIX | volatility modifier | — | ingest (gap) |
| Put/Call | sentiment; extremes → reversal | research (Dejan) | ingest |
| High-Low Index | breadth quality | — | ingest |
| SPY/QQQ/IWM price action | momentum vs trend (legs vs swings) | — | computed |

Skipped as restatements: TRIN, breadth-thrust variants, OBV/VPT.
Read on SPY, QQQ, IWM + ALL sector ETFs. Principle: track what widens Dejan's view, not what he reads today; calibrate against outcomes. Whatever can be calculated, Cobalt calculates.

### 4.3 Data source (SPIKE)
Live environment = DAS Trader Pro. Internals target = TradingView. Whether a TradingView MCP returns internals as **numbers** is unverified — Finviz-style spike (enumerate returns, confirm data not charts, ToS). Fallbacks: DAS feed, direct provider.

### 4.4 Sector layer (RULED)
Analysis/support layer. Inputs: sector RS vs market (Finviz Groups), sector fundamentals/catalyst (LLM narrative). Rotation lives here.

## 5. Cross-asset context + Theme

**Reference instruments (current):** USO, BTCUSD, DXY — rolling correlation of SPY / sector / ticker vs each = computed. BTC = prefill gap.

**Theme object (structure PROPOSED, concept RULED):**
```
theme: {name, active_since, status, driver_instruments, affected_sectors,
        members[], leaders[], laggards[], correlation_direction,
        catalyst_sources, narrative}
```
- Watchlist of reference instruments is **derived from active themes** in config.
- Cobalt computes correlations, membership, leader/laggard RS ranking; council supplies name/narrative/why — never a figure.
- Thematic move (RULED): members move with theme leaders (AI: NVDA/AMD/MU/MRVL/INTC together) → leaders and laggards are exploitable. Laggard-follows-leader uses **existing trade vocabulary**, no new trade type.

## 6. Trigger lifecycle (RULED)

A trigger is a transient event, not a setup state:
```
trigger: {trade_type, ticker, time, direction, state: forming → fired → expired/missed, window}
```
- One ticker holds **one live trigger at a time**; a different one may appear minutes later.
- Triggers have windows: miss Fashionably Late and a later Second Chance is a *different* trade.
- SMB Scalp Radar stops at "forming" (Dejan: does not work well). Cobalt's detector carries the full lifecycle and surfaces the next valid trigger after a miss.
- Radar vocabulary (trade types): Hitchhiker, Back$ide, Rubberband, Second Chance, Fashionably Late → trades pass.

## 7. Card variable registry (RULED shape: 11 variables, each 1–10 with a stated WHY, weighted → total → grade)

The SMB ten contain the three object grades (catalyst / setup / trade); the rest are context. No separate combination rule and **no penalty matrix** — regime fit's weight IS the penalty.

| # | Variable | Tier | Source |
|---|---|---|---|
| 1 | Catalyst (fundamental + news) | human; council proposes with WHY | council + Cobalt facts (RVOL, gap, news) |
| 2 | Setup quality (technical) | cobalt-scored, override-with-reason | structure objects |
| 3 | Trade R:R | cobalt | card entry/stop/target |
| 4 | Market regime fit | cobalt | regime record × trade category |
| 5 | Market internals support direction | cobalt | regime direction/confidence |
| 6 | Level importance | cobalt + override | Level object |
| 7 | Volume / liquidity / participation | cobalt | RVOL, float, spread |
| 8 | Sentiment | cobalt-degraded | put/call + council narrative |
| 9 | Correlation (market / sector / theme) | cobalt | correlations, theme membership |
| 10 | Plan alignment | human | rules card = Rules Engine gate, not a score |
| 11 | Tape / price-action behavior | human placeholder | Dejan grades with WHY |

- Weights = config; v0 weights are a guess, tuned from card-vs-outcome data.
- Score overrides recorded WITH REASON; a reason must resolve to a variable (existing, mis-weighted, or new).
- `divergence_flag` from the regime record is an **event**, not a variable — surfaces loudly on every open card.

## 8. Grade ladder (RULED)

| Total | Grade | Keys (full / half) |
|---|---|---|
| 10 | A+ | 345 / 170 |
| 8–9 | A | 135 / 70 |
| 6–7 | B | 60 / 30 |
| 4–5 | C | 21 / 11 |
| < 4 | D | pass |

`enabled_grades` = phase dial (reduced-live now: A, B only). Decimal boundary: `>= 4` is C unless Dejan prefers rounding. "Stars align" (A+/A+/A+ on the three object grades) = max risk.

## 9. Deferred
- **Setups session:** Gap & Go / GUIR / GDIS / Changing Fundamentals definitions; single-session vs multi-day for GUIR/GDIS; premarket fields on the Gap object.
- **Trades pass:** Trades column per setup (trigger, stop, exit trigger per setup — 09-01 rule); snapback entry timing; intraday extension qualification; leg-count as variable; radar trade types; adds/scale-ins (parked).
- **Cross-reference pass:** Dejan's additional SMB vocabulary + rules upload, checked against this draft for gaps and architectural corners.

## 10. Spikes / research
- TradingView MCP internals-as-data + ToS
- Put/call usage at regime / sector / stock level (Dejan)
- BTC / VIX ingestion ownership (prefill gaps)
