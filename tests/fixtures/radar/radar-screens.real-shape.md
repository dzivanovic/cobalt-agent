---
name: Radar Screens
description: Production-shaped parser fixture; personal attribution, dates, and preset IDs removed.
fixture_substitutions: Personal attribution, dates, and saved-preset IDs only.
---
# Radar Screens (F2 dynamic sources)

Each screen = the Finviz Elite saved-screener URL as pasted, its decoded filters, and the
export call Cobalt derives from it. The field text and punctuation below retain production shape.

## Screen 1 — Up Gappers
- **Pasted:** `https://elite.finviz.com/screener?v=150&f=sh_avgvol_o2000%2Csh_curvol_o100%2Csh_price_o1%2Cta_averagetruerange_o0.5%2Cta_gap_u3&ft=4&o=-volume&ar=10&c=0%2C1%2C4%2C5%2C129%2C6%2C7%2C25%2C26%2C28%2C30%2C84%2C93%2C49%2C83%2C61%2C63%2C64%2C67%2C65%2C66`
- **Filters (`f=`):** `sh_avgvol_o2000` avg volume > 2M · `sh_curvol_o100` current volume > 100K · `sh_price_o1` price > $1 · `ta_averagetruerange_o0.5` ATR > 0.5 · `ta_gap_u3` gap up > 3%
- **Sort:** `-volume` (volume desc) · **columns (`c=`):** 0,1,4,5,129,6,7,25,26,28,30,84,93,49,83,61,63,64,67,65,66 · preset [removed]
- **Export call (derived):** `/export/screener?v=152&f=sh_avgvol_o2000,sh_curvol_o100,sh_price_o1,ta_averagetruerange_o0.5,ta_gap_u3&c=<same columns>`
- **Intent:** premarket / open gap-up scan

## Screen 2 — Down Gappers
- **Pasted:** `https://elite.finviz.com/screener?v=150&f=sh_avgvol_o2000,sh_curvol_o100,sh_price_o1,ta_averagetruerange_o0.5,ta_gap_d3&ft=4&o=-relativevolume&ar=60&c=0,1,4,5,129,6,7,25,26,28,30,84,93,49,83,61,63,64,67,65,66`
- **Filters (`f=`):** `sh_avgvol_o2000` avg volume > 2M · `sh_curvol_o100` current volume > 100K · `sh_price_o1` price > $1 · `ta_averagetruerange_o0.5` ATR > 0.5 · `ta_gap_d3` gap DOWN > 3%
- **Sort:** `-relativevolume` (RVOL desc) · **columns:** 0,1,4,5,129,6,7,25,26,28,30,84,93,49,83,61,63,64,67,65,66 · no preset id (`ar=60`)
- **Export call (derived):** `/export/screener?v=152&f=sh_avgvol_o2000,sh_curvol_o100,sh_price_o1,ta_averagetruerange_o0.5,ta_gap_d3&c=0,1,4,5,129,6,7,25,26,28,30,84,93,49,83,61,63,64,67,65,66`
- **Intent:** premarket / open gap-down scan (the short side of Screen 1)

## Screen 3 — Day Scan (after 10:00)
- **Pasted:** `https://elite.finviz.com/screener?v=150&f=sh_curvol_o10000%2Csh_price_o1%2Csh_relvol_o3&o=-volume&ar=10&c=0%2C1%2C4%2C5%2C129%2C6%2C7%2C25%2C26%2C28%2C30%2C84%2C93%2C49%2C83%2C61%2C63%2C64%2C67%2C65%2C66`
- **Filters (`f=`):** `sh_curvol_o10000` current volume > 10M · `sh_price_o1` price > $1 · `sh_relvol_o3` RVOL > 3
- **Sort:** `-volume` · **columns:** 0,1,4,5,129,6,7,25,26,28,30,84,93,49,83,61,63,64,67,65,66 · preset [removed]
- **Export call (derived):** `/export/screener?v=152&f=sh_curvol_o10000,sh_price_o1,sh_relvol_o3&c=0,1,4,5,129,6,7,25,26,28,30,84,93,49,83,61,63,64,67,65,66`
- **Intent:** in-session in-play scan, used after 10:00 ET — pool source only from 10:00 (window per F1 session clock)

## Screen 4 — Morning Low Float
- **Pasted:** `https://elite.finviz.com/screener?v=150&f=sh_float_u10%2Csh_price_u10%2Cta_gap_u10&ft=4&o=-volume&ar=10&c=0%2C1%2C4%2C5%2C129%2C6%2C7%2C25%2C26%2C28%2C30%2C84%2C93%2C49%2C83%2C61%2C63%2C64%2C67%2C65%2C66`
- **Filters (`f=`):** `sh_float_u10` float < 10M · `sh_price_u10` price < $10 · `ta_gap_u10` gap up > 10%
- **Sort:** `-volume` · **columns:** 0,1,4,5,129,6,7,25,26,28,30,84,93,49,83,61,63,64,67,65,66 · preset [removed]
- **Export call (derived):** `/export/screener?v=152&f=sh_float_u10,sh_price_u10,ta_gap_u10&c=0,1,4,5,129,6,7,25,26,28,30,84,93,49,83,61,63,64,67,65,66`
- **Intent:** morning low-float gapper scan (premarket / open)
