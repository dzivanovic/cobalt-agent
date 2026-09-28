# SITTING — SECOND CHANCE SCALP (redesign) · 2026-09-24 · first sitting

## §0 ONE SCREEN
**What it is (cheat sheet p.1):** "Watch for price to break through an area of resistance with a strong and clear move." · "wait for the price to come back and 'retest' the broken level" · "seeing buyers come back in through a candle that closes above a prior candle and enter our position."
**Cobalt today:** it only watches the premarket high and yesterday's high — no other level. It waits for a 2-min bar to close above that line, then for any later bar that dips to within a hair of it (a tenth of a typical bar) and closes above. It fires on the first bar after that dip that closes above the prior bar's high. It calls the break failed only if a close back under comes in the very next bar; after that, closes under are not checked.
**Where they differ:** YOU say the level is any price touched several times today / Cobalt uses premarket and yesterday's high only. · YOU say no pullback bar may close under the level, however long / Cobalt checks one bar only. · YOU say the pullback must give back at least half the breakout move / Cobalt only needs one bar dipping near the line, however shallow the pullback. · YOU say no ATR / Cobalt measures "near" in ATR.
**Decisions for you:**
1. How many touches make a level? Recommend: **3 or more** — you said "several times, could be many"; two tops are only a double top.
2. How close do the highs have to be to count as the same line? Recommend: **within 0.1 % of price** (about 2¢ on a $20 stock), tuned live — "no ATR" rules out bar-size units, and a fixed cents value is too tight on a $200 stock.
3. May a pullback bar's wick go below the level if the bar closes back above? Recommend: **no — the wick may touch the level (within Q2's distance), never go through it** — you said "touch the level or come above the level … and not below resistance line".
4. What counts as the "curl"? Recommend: **the first bar that closes above the prior bar's high** — the sheet's "closes above a prior candle", read the strict way; this is what Cobalt does today.

## §0b SETTLED BY THE HOUSES (not asked — the sources already answer them)
| # | Item | Settled as | Why |
|---|---|---|---|
| S1 | The break | one 2-min bar closing above the level | your R116 "one bar breaks above" = sheet p.1 "candle to close above a key level" = engine today |
| S2 | Failed break | any pullback bar closing under the level ends it, at any bar count | your R116 overrides the sheet's p.2 "does not recover in the next candle" and dial A-19 |
| S3 | "Breakout range" | from the level up to the highest high after the break; the pullback low must reach ≤ halfway back | your R117 "at least 50% of a breakout range back towards the resistance line" |
| S4 | ATR | removed from the setup | your R117 "there is no ATR corelation here" → dial A-20 dies |
| S5 | Premarket / yesterday's high | count only when tested several times today, like any level | your R116 "it has to be a price level that stock is touching multiple times" |
| S6 | Stop, targets, strikes | unchanged: 2¢ under the curl bar's low; half at the breakout high; 2 strikes, never a 3rd | sheet p.1–2, no ruling of yours changes them |

## §1 HIS WORDS (verbatim, `cto-2026-09-23.md`)
- **R116, 2026-09-23 22:2x ET:** "second chance forms when stock troughout a day creates a level, by touching a price line several times, could be many, then one bar breaks above the resistance line. this is the level, and it doesnt have to be premarket, or prior day high, it has to be a price level that stock is touching multiple times and can not break, then one bar breaks it. that bar can be followed by another and another, but usualy one breaks. Than pullback happens, and it can be any number of bars, what is important is that it does not close below that resistance line again. No single of those bars pulling back close below.. It should create pullback and bounce off of or above the level."
- **R117, 2026-09-23 22:2x ET:** "The retest has to pull back to the level and either touch the level or come above the level. It has to pull back at least 50% of a breakout range back towards the resistance line and not below resistance line and then curl into direction of a breakout. there is no ATR corelation here. This setup needs to be redesigned. we deploy tomorrow and redesign."
- **R82, 2026-09-23 16:3x ET (now overridden by R116/R117):** his word "A" → A-19 = 1 bar, A-20 = 0.10 × ATR, as ASSUMED.
- **R13, 2026-09-24 06:5x ET:** "The wvap continuation and second chance need a sitting and redesign between you and me."

## §2 THE CHEAT SHEET (`docs/90 - References/the_second_chance_scalp_cheat_sheet.pdf`, verbatim)
- p.1 break: "Watch for price to break through an area of resistance with a strong and clear move. A common way is to wait for the candle to close above a key level."
- p.1 retest: "Once the level is broken, wait for the price to come back and "retest" the broken level allowing us to see if old resistance becomes new support."
- p.1 entry: "Allow the 2nd chance to confirm by seeing buyers come back in through a candle that closes above a prior candle and enter our position."
- p.1 stop: ".02 below the low of the turn candle" — "We place our stop here because this low should line up with our old resistance that is now new support."
- p.1 exit: "Sell ½ our position at our profit target: the high of the initial pullback that set up the 2nd Chance Scalp"; p.2: "waiting for a 1-minute bar close below the 9 EMA on a 1-minute chart."
- p.2 better: "Significance of the Level being broken" · "a visible increase in volume on the break of resistance combined with a low-volume retest of the prior resistance" · "Trade occurring in the direction of the market".
- p.2 worse: "If the size of the initial breakout move is more than the height of the prior range, it just may be too much for this scalp." · "This scalp fighting a bigger picture trend on the day".
- p.2 avoid: "If the action breaks back into range (back below resistance that should have become support) and does not recover in the next candle we avoid this trade entirely." · "NEVER take this trade a 3rd time, 2 strikes and we are out on this trade".
- p.2 times: "Morning (9:59-10:44 am ET)" · "Mid-Day(10:45-1:29 am ET)" · "Afternoon (1:30 – 4 am ET)".

## §3 THE ENGINE TODAY (branch `setups-c1` @ `c60a7f00`, not yet on main)
| Clause | Code | What it does | Match / gap |
|---|---|---|---|
| The level | `anatomy/frame.py:496-505`; `anatomy/range_break.py:104-118` | levels = {premarket high, prior-day high}; picks the latest-broken one; a gap above a level is not a break | GAP vs R116 (intraday multi-touch) |
| The break | `range_break.py:86`; `formation/atoms.py:486-490` | first 2-min bar with close > level | MATCH |
| Failed break | `range_break.py:91-92` | a close < level within `failed_trap_bars` (A-19) bars after the break | GAP vs R116 (every pullback bar, any length) |
| The retest | `range_break.py:93-95` | first later bar with low ≤ level + A-20 × ATR and close > level | GAP vs R117 (no 50 % rule; uses ATR) |
| The curl | `range_break.py:97-98`; `atoms.py:499-503` | first bar after the retest closing above the prior bar's high | MATCH (Q4) |
| Order of steps | `formation/triggers.py:234-280` | break → retest → curl, each after the previous | MATCH |
| Stop | `formation/stops.py:91-98`; `tunables.yaml` `stop.buffer` 0.02 | curl bar's low less 2¢ | MATCH |
| Held off | `tests/cobalt/test_setups_lego.py:69-72` | pinned "AWAITING ITS ENGINE FILL" until A-19 + A-20 have values | A-19 / A-20 die in the redesign |

## §3b WHERE THE DESIGN CAME FROM (`30 - Design/SETUPS-AT-DEFAULTS-FINAL-2026-09-21.md`)
| Design clause (FINAL line) | Cheat-sheet source | His R116/R117 |
|---|---|---|
| Level set A-17 = PMH, PDH (`:191`) | **NO CHEAT-SHEET SOURCE — design invention** (sheet says only "an area of resistance" / "a key level", p.1) | OVERRIDDEN (R116) |
| `accepted` = a close through the level (`:191`, `:148`) | p.1 "wait for the candle to close above a key level" | agrees |
| `failed_trap` within A-19 bars (`:191`); A-19 = 1 | p.2 "does not recover in the next candle" | OVERRIDDEN (R116: no close below, ever) |
| `event(retest)` within A-20 × ATR (`:191`); A-20 = 0.10 | **NO CHEAT-SHEET SOURCE — design invention** (sheet p.1 says "retest the broken level", no distance) | OVERRIDDEN (R117: 50 %, touch or above, no ATR) |
| Turn = close above prior bar (`:148`, `:210`) | p.1 "a candle that closes above a prior candle" (engine reads "prior bar's high" — a design reading) | agrees ("curl") — Q4 |
| Stop `turn_candle` A-23 (`:159`) | p.1 ".02 below the low of the turn candle" | agrees |
| `Range(prior)` A-21 = session low → level (`:191`) | p.2 "breaks back into range" / "height of the prior range" name a range; its span is **design invention** | range height still feeds the p.2 over-extension factor |
| `event(stop_hit)` A-22 from bars (`:191`) | **NO CHEAT-SHEET SOURCE — design invention** (mechanics for "2 strikes") | untouched |
| A-20's own record: "no number in the source, LOW" (R82) | — | the one the desk flagged; R117 confirms it |

## §4 THE REDESIGN SKETCH (bar conditions, long side; the short side mirrors — sheet p.1 "just inverted")
1. **Level L:** in today's session, ≥ N bars (Q1) put their high within the touch distance (Q2) of one price, with no close above it — R116 "touching a price line several times … can not break".
2. **Break:** the first bar that closes above L — R116 "one bar breaks above"; sheet p.1.
3. **Breakout high H:** the highest high from the break until the pullback starts; breakout range = H − L — R116 "that bar can be followed by another and another".
4. **Pullback:** any number of bars; the low reaches L + 0.5 × (H − L) or lower — R117 "at least 50% of a breakout range".
5. **Hold:** no pullback bar closes below L; a wick touches L at most (Q3) — R116 "No single of those bars pulling back close below"; R117 "not below resistance line".
6. **Curl (trigger):** the first bar after the pullback low that closes above the prior bar's high (Q4) — R117 "curl into direction of a breakout".
7. **Dead:** a pullback close below L ends it; 2 strikes per level, never a 3rd — sheet p.2.
- **Dials that die:** A-19 (`range_break.failed_trap_bars`), A-20 (`range_break.retest_tolerance_atr`). A-17 changes from a fixed set to the multi-touch detector.
- **New values:** touch count (Q1, his), touch distance as % of price (Q2, his; tuned live), retrace 0.5 (his R117 — fixed, not a dial).
- **Human-only (L11):** level significance and the volume read (sheet p.2) stay his eye on the card.
- **Fixture (L45):** 2-min bars of real `<ticker>` days he tags as Second Chance: one that forms (3+ touches, close-above break, ≥ 50 % pullback with no close below, curl bar) and one that dies (a pullback bar closing under L) — real shape, dates and attribution stripped.

## HIS EXAMPLES
5–10 chart examples and other traders' playbooks, brought by Dejan to the sitting; reviewed against §0's decisions and §3b's inventions.

## §5 APPENDIX — engine terms (for the desk)
- Files: `src/cobalt/radar/anatomy/range_break.py` (lifecycle, `choose`), `anatomy/frame.py:472-506` (level set, `rejected`), `formation/atoms.py:480-512` (step shapes), `formation/triggers.py:234` (`Sequence`), `formation/stops.py:91` (`turn_candle`); note def `Second Chance Scalp.md:106-118`.
- Dials: `range_break.failed_trap_bars` (A-19, `tunables.yaml:157`), `range_break.retest_tolerance_atr` (A-20, `:325`), `levels.set` (A-17), `range_prior.rule` (A-21), `event.stop_hit.source` (A-22), `turn_candle.rule` (A-23).
- Seam: A-17's level set also feeds vwap-continuation's `Level_ref(resistance).rejected` avoid (`frame.py:472-493`) — the redesign must keep or split it (one-path, L3).
- Path: redesign → four-house tribunal (L67; Fable · Astra · Grok) with this sitting's answers as his rulings → build → `taxonomy load`; until then Second Chance stays off the radar (R117).
