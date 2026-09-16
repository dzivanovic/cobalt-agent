# Alignment benchmarks — proposal for Dejan's ruling (2026-09-16, CTO desk)

Ruling that triggered this (Dejan, 2026-09-16 08:5x ET): "Against QQQ not SPY for all technology, and SPY and its ETF (and we need to define those per sector). I need proposals for which are appropriate."

Scope: the two desk dots `market_alignment` and `sector_alignment` (P2 STEP-5). Today they render N/A (`DEFAULT_UNRULED`) because no dated ruling authorizes a benchmark map. This note proposes the map; the grade semantics (with / flat / against → 1–10) stay with the curve tribunal (item 1 of the same ruling set). Nothing here is applied until Dejan rules; the values then land in `"user".trader_settings` (user data, L32), never in committed config.

## Proposed benchmark map (Finviz `Sector` column → market benchmark, sector benchmark)

| Finviz sector (exact string) | market benchmark | sector benchmark | note |
|---|---|---|---|
| Technology | **QQQ** | XLK | Dejan's ruling: tech aligns against QQQ, not SPY. Semis: see override below |
| Communication Services | QQQ | XLC | Nasdaq-heavy (GOOGL, META, NFLX); QQQ is the honest market read |
| Consumer Cyclical | SPY | XLY | |
| Consumer Defensive | SPY | XLP | |
| Healthcare | SPY | XLV | Biotech override below — most of the low-float pool lives there |
| Financial | SPY | XLF | |
| Industrials | SPY | XLI | |
| Energy | SPY | XLE | |
| Basic Materials | SPY | XLB | |
| Utilities | SPY | XLU | |
| Real Estate | SPY | XLRE | |
| (sector missing / unknown) | SPY | — | sector dot renders `CHECKPOINT_MISSING`, never a guessed ETF |

## Proposed industry overrides (Finviz `Industry` column, checked before the sector row)

| Finviz industry | sector benchmark | why |
|---|---|---|
| Semiconductors, Semiconductor Equipment & Materials | SMH | XLK is Apple/Microsoft-weighted; semis move with SMH |
| Biotechnology | XBI | XLV is big-pharma-weighted; small-cap biotech (the in-play pool) moves with XBI |
| Gold, Silver, Other Precious Metals & Mining | GDX | XLB does not track miners |
| Oil & Gas E&P, Oil & Gas Drilling, Oil & Gas Equipment & Services | XOP | XLE is XOM/CVX-weighted; E&P small caps move with XOP |
| Software — Application, Software — Infrastructure | IGV | optional; XLK acceptable if one fewer ETF is preferred |

## Small-cap market read (open question for Dejan)
The in-play pool is mostly small and micro caps. A third read, `IWM`, would say whether small caps as a class are bid that day. Proposal: keep two dots as ruled (market, sector) and record IWM's sign in `radar_score.desk_shadow` only, no dot, for the curve tribunal to judge in S3. Alternative: replace SPY by IWM for names under $2B market cap. Recommendation: the first (no new dot, data captured).

## What this needs before it can run
1. Bars for every benchmark above at i1 and daily: SPY, QQQ, IWM, XLK, XLC, XLY, XLP, XLV, XLF, XLI, XLE, XLB, XLU, XLRE, SMH, XBI, GDX, XOP (IGV optional). Today `tier_b` archives the 14 SPDR names at i5/i30 only; the i1 add is approved (Dejan 09-16, ops item 5 tomorrow) — the four industry ETFs are NEW names for that tier. Demand: +4 names × 5 intervals ≈ +20 requests nightly, inside the 45 rpm ceiling.
2. The map as a `trader_settings` key (proposal: `card.alignment_benchmarks`, one JSON document: sector rows + industry overrides + the missing-sector rule), loaded by `settings load --apply --sha256` (P2's five-key loader must gain this sixth key — a P2 follow-up, one small build item, or part of the D2 values session).
3. The "with / flat / against" definition and the 1–10 grades = the curve tribunal's output, not this note.

## Ruling requested
A) Adopt the map + overrides as proposed (IWM captured as shadow, no dot). B) Adopt the sector map only, no industry overrides (fewer ETFs, coarser reads). C) Edits — name them.
Recommendation: A.
