# Trading Taxonomy — Draft v0.3
Cross-reference pass 2026-09-01 (closed). Supersedes v0.2. Inputs cross-referenced: SMB Glossary (~130 terms), SMB Market Context, SMB Game Plan, TOS scripts doc. All v0.2 RULED content carries forward unless amended here.
Legend: **RULED** = Dejan confirmed · **PROPOSED** = Claude's draft awaiting his call · **SPIKE** = empirical check before ruling · **DEFERRED** = parked to a named session.

---

## 1. Spine (RULED, unchanged)

```
Market regime → Sector state → Category (Momentum | Trend | Mean Reversion) → Setup → Trade
```
- PENDING setups session: In-Play ticker layer insertion between Sector and Category.
- SMB AI chatbot = doctrine channel for SMB terms (RULED).

## 2. Category → Setup mapping (RULED, unchanged from v0.2)

Momentum: Gap & Go, Range Break · Trend: Day 2, Day 3 · Mean Reversion: VIR, Overextension, GUIR, GDIS. Changing Fundamentals unplaced → setups session.

## 3. Structure objects (amendments to v0.2 §3)

**Swing primitive (RULED 09-01):** swing high/low = structural peak/valley on the object's timeframe — a pivot bar with N confirming bars on each flank (N = config per timeframe). Higher-TF swings are multiday peaks/valleys; intraday the same on the lower timeframe. NO ATR component — SMB's ATR-displacement method REJECTED. Shared by Trend sequencing, Momentum legs, VIR edge tests, VWAP auto-anchor points.

**HV bar (RULED 09-01, per SMB Study 2):** bar volume ≥ MA(volume, lookback) + k·σ(volume, lookback). v0 config: k = 2.0, lookback ≈ 10 days of bars on the working timeframe (1950 on 2-min). Used by Extension initiation, volume-confirmation bar, breakout validity. Tune from outcomes.

**Extension band (RULED 09-01, per SMB Study 3):** upper/lower band = 5-day low/high ± factor·ATR(len); v0 config factor = 5, ATR len = 20, daily basis. The v0.2 "≥5 ATR within ≥5 days" gate is implemented as price beyond band. Extension object gains `distance_from_band` (ATR units, signed).

**Level.type enum extended (RULED 09-01):** S/R, VWAP, MA, prior-day H/L, HV node **+ PMH/PML, opening-range H/L, HOD/LOD, 52-week H/L, round number, multi-day VWAP, anchored VWAP, trendline.**

**Object lifecycle states** — DEFERRED → setups session (Range Break accepted/failed-trap; Extension extending → culminating → reverting → backside | resuming; Gap open → filling → filled). Naming rule already RULED: Backside-the-phase and Back$ide-the-trade are distinct identifiers.

Range `bound_type`, Gap `prior_context`, prior-day enum additions, ticker `volatility_state`, Change-in-Character / ticker-divergence events — DEFERRED → setups session.

## 4. Market layer (amendments to v0.2 §4)

**Breadth axes (RULED 09-01, adopt SMB and evolve):** regime record scores **strength and weakness as separate axes**; SMB 2×2 label derived on the record: High-S/High-W (volatile two-sided) · High-S/Low-W · High-W/Low-S · Low-S/Low-W. High/High maps to Range + volatility-high but carries its own label.

**VOLD (RULED 09-01):** read per exchange — NYSE ($UVOL/$DVOL) and NASDAQ ($UVOL/Q, $DVOL/Q). Two config bands: |VOLD| ≥ 2.618 = "leaning" (SMB default) · ≥ 3 = trend-day input to confidence (Dejan's threshold, the trend-day call).

**Regime events gain `cause`** (e.g. market-wide catalyst) (RULED 09-01). Dispersion attribute + headline-driven modifier — DEFERRED → setups session.

**TRIN (RULED 09-01):** computed free from ADL + VOLD components; never a card variable.

Desk-cadence calibration note: Cobalt logs regime snapshots at SMB's canonical checkpoints (post-open, midday, post-close) alongside continuous tracking — calibration data, not a tracking change.

## 5. Cross-asset context + Theme (amendments)

**Theme gains `head`** (RULED 09-01): the single leader driving the theme; head failure → theme status invalid. Laggard-follows-leader is termed **sympathy** (SMB vocabulary), still expressed in existing trade types.

## 6. Trigger lifecycle (amendment)

One-live-trigger constraint DEMOTED to config policy, keyed (ticker, direction) — not schema (RULED 09-01). Coexists with the 09-01 rules ruling: second trade on same name = two cards, two stops.

## 7. Card registry (RULED 09-01: container restructured)

Registry shape = `{gates[], variables[]}`. **Gates are binary; any failed gate = no card.** Variables remain 1–10 × weight → total → grade, each score with a stated WHY.

**Gates v0:**
| Gate | Content | Tier |
|---|---|---|
| Rules / plan alignment | printed rules card + IF/Then branch match (§8) | cobalt-checked, human-owned rules |
| Tradability | spread, polka-dot tape, active halt, locate available (shorts) | cobalt |

**Variables:** v0.2 vars 1–9 and 11 unchanged, except:
- Var 10 (plan alignment) MOVED to gates.
- Var 11 tape/price-action stays **human by law**; computable volume metrics (volume SD bars, volume-confirmation bar, block-trade counts if a T&S source ever exists) belong under var 7 (cobalt).
- **Var 12 reserved (RULED 09-01):** "setup expectancy (own data)" — inactive until n ≥ 30 per sample-size law.
- Window-fit variable + `dynamic` flag per variable — DEFERRED → setups session.

## 8. IF/Then plan branches (NEW, concept RULED 09-01)

Per-ticker pre-registered conditionals: `{condition, action, invalidation}`. Authored **premarket AND intraday** as game planning; ~3 branches per name premarket typical; in-play watchlist cap 3–5 names (config). A trade matching a registered branch = plan-aligned (feeds the rules gate).

Grammar requirements observed from Dejan's examples (DEFERRED → trades pass for formal grammar): time-of-day anchors ("at 1PM"), duration windows ("holds above PMH for 10 min", "consolidation 30–60 min"), level interactions (break / reject / retest of PMH, VWAP, 9/20 EMA, round numbers), multi-step sequences (waterfall → wait for retest → enter), branch-specific stops and trails (stop at PML, stop above rejection high, 2-min bar trail), and inverted branches (out-of-window consolidation → look for failed breakout).

## 9. Grade ladder (RULED, unchanged from v0.2)

## 10. Deferred

**Setups session (NEXT):**
1. Gap family definitions (Gap & Go / GUIR / GDIS) + Gap `prior_context: fresh | continuation | exhaustion`; premarket fields on the Gap object; single- vs multi-session for GUIR/GDIS.
2. Changing Fundamentals — defined by price response (gap through multi-month level, price discovery, volume), not by the news (anti-double-count with catalyst grade).
3. Object lifecycle states (Range Break, Extension, Gap) + transitions detected by Cobalt.
4. Range `bound_type: flat | converging | channel` (Bouncy Ball wedge).
5. In-Play ticker layer in the spine: `in_play {catalyst, RVOL, ATR, liquidity, tradability}` — precondition, not a variable.
6. Prior-day enum gains inside / reset / rest; "Day 3 liquidity trap" candidate setup.
7. Ticker `volatility_state` (contraction ↔ expansion; Momentum↔MR shift driver).
8. Change-in-Character + ticker-level divergence as Level/Extension events.
9. Dispersion on regime record (resolution: var 4 score goes neutral when high, weights untouched) + headline-driven modifier.
10. Time-of-day: window as gate input + window-fit variable; `dynamic` flag per registry variable.

**Trades pass (after setups):** Trades column per setup (trigger, stop, exit trigger — 09-01 rule) · snapback entry timing · intraday extension qualification · leg count · radar trade types mapped onto object states (Rubberband / Back$ide = Extension phases) · exit/stop type enum (time stop, two-bar rule, 2-min bar trail, passive, trailing variants) · confirmation policy per trigger (close-through / two-bar / acceptance) · entry mode front-side vs backside + sizing interaction · IF/Then condition grammar · intraday swing pivot N · adds/scale-ins (parked).

**Cross-reference pass:** DONE 09-01 (this document).

## 11. Spikes / research
- TradingView MCP: internals-as-numbers + ToS **+ $UVOL/$DVOL per-exchange ingestability** (RULED addition 09-01).
- Put/call usage at regime/sector/stock level (Dejan).
- BTC/VIX ingestion ownership (prefill gaps).

## 12. Script dispositions (RULED 09-01)
Default: Cobalt computes; Pine only where eyes-on-chart needed.
- Study 1 (volume data): SKIP — Finviz covers.
- Study 2 (bar threshold): Cobalt HV-bar detector on archiver bars; Pine display optional.
- Study 3 (extension bands): Cobalt daily calc + ONE Pine display for the daily chart.
- Study 4 (anchored VWAP): TradingView native; auto-anchoring Cobalt-side via §3 swing primitive.
- Study 5 (VOLD): Cobalt computes if $UVOL/$DVOL ingestable (spike above).
