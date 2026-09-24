# SITTING — VWAP CONTINUATION · 2026-09-24 · second sitting (after Second Chance)

## §0 ONE SCREEN
**What it is (cheat sheet p.1):** "An in-play stock will often make a strong move in the morning that will attract profit taking from momentum traders" · "This selling can drop the stock into VWAP where institutional participants will be looking to buy" · "Enter near VWAP after a trendline break or a range break".
**Cobalt today:** it waits for an in-play stock's morning up-move, then for the pullback after it. It needs the pullback's low to end "near" VWAP — but "near" has no number yet, so today it never fires. Once it has one, it fires when price breaks the pullback's falling trendline, or the top of a tight range built at VWAP. Stop = VWAP at entry, less 2¢; half out at the high of the day.
**Where they differ:** SHEET says "into VWAP" / "near VWAP", no distance / Cobalt needs a number for "near" and has none. · SHEET puts the stop "just below VWAP", so price should hold VWAP / Cobalt measures distance either side — a pullback that sinks the same distance UNDER VWAP still counts. · SHEET lists "a rejection of an important resistance level" as a factor that lowers the odds / Cobalt treats it as a hard no. · PLAYBOOK "could be re-entered if the setup reset" / your note allows 1 try.
**Decisions for you:**
1. How close to VWAP must the pullback's low get? Recommend: **within half of an average 2-minute candle** (your 09-22 value) — it scales with how much the stock moves; tuned live.
2. May the pullback close under VWAP? Recommend: **a wick under is fine; a 2-minute close under VWAP cancels it** — the stop sits "just below VWAP", so a close there means the trade is already wrong.
3. How many tries per stock per day? Recommend: **2** — the playbook re-entered "if the setup reset"; the sheet says nothing.

## §0b SETTLED BY THE HOUSES (not asked — the sources already answer them)
| # | Item | Settled as | Why |
|---|---|---|---|
| V1 | Resistance rejection | a factor that lowers the grade, not a hard no | sheet p.1 lists it under "Factors that decrease the probability", not under "avoid" |
| V2 | Trail | your 20 EMA stays | `configs/cobalt/taxonomy/defaults.yaml:11` "sheet value 21; Dejan trades 20" — your number |
| V3 | "Strong move" size | the minimum-move rule you ruled, tuned live | your 09-22 R49 "A and we tune in live" |
| V4 | "Choppy / not definitive" opening | your eye, shown as text on the card — never computed | sheet p.2; human-only read (L11) |
| V5 | Trendline OR range break | both built: a falling line through 2+ lower highs, or the top of a tight range at VWAP | sheet p.1; playbook p.7 "Entry plan: VWAP consolidation" |
| V6 | Short side | the mirror image | sheet p.1 "inverted rules for the short side"; the playbook trade is a short |
| V7 | "Just below VWAP" | 2¢ under VWAP at entry, the same 2¢ as every stop | sheet p.1; `stop.buffer` 0.02 |

## §1 HIS WORDS (verbatim, dated)
- **R118, 2026-09-23 22:3x ET:** "Let's go with B and I will pull up the cheat sheet tomorrow and revew with you as I do not understand what you are saying at all"
- **R107, 2026-09-23 20:58 ET (superseded by R118):** his word "A": write all three rows, `dist.k.vwap` included.
- **R119, 2026-09-22 21:18–21:2x ET:** the three word-only values enter Assumed Defaults as ASSUMED / LOW and are tuned live — A-16 = 0.5 × ATR (then held by R118).
- **R48, 2026-09-22 14:14 ET:** "A" — `dist.k.vwap` gets a cheat-sheet-derived value, marked ASSUMED.
- **R13, 2026-09-24 06:5x ET:** "The wvap continuation and second chance need a sitting and redesign between you and me."

## §2 THE CHEAT SHEETS (verbatim)
`docs/90 - References/VWAP Continuation.pdf`
- p.1 why: "An in-play stock will often make a strong move in the morning that will attract profit taking from momentum traders" · "This selling can drop the stock into VWAP where institutional participants will be looking to buy" · "We will wait for this buying to overwhelm the selling and look to get long for a continuation of the morning strength".
- p.1 entry: "Enter near VWAP after a trendline break or a range break" · stop: "The stop should be placed just below VWAP".
- p.1 exit: "This is a trending trade so we will sell half into the high of the day and trail the rest with the 21 EMA on the 1-minute chart".
- p.1 better: "A strong market" · "A breakout of a technical level" · "A changing fundamentals catalyst"; worse: "A weak market" · "A rejection of an important resistance level" · "A weak or uneventful catalyst".
- p.1 times: "Late morning (10 AM - 11 AM)" · "Mid-day (11 AM - 2 PM)"; p.2 avoid: "We will avoid this trade entirely if the opening auction was choppy and/or not definitive".

`docs/90 - References/SMB PlayBook — 2026-08-17 — $NU — NU DAY 2 + VWAP CONTINUATION.pdf` (ticker → `<ticker>`)
- p.6: "Daily: gap up into resistance." · "Intraday: VWAP continuation." · p.7: "Direction: short continuation, not long" · "Entry plan: VWAP consolidation" · "Setup criteria: strong sellers and one-direction trend".
- p.8: "The trade used a tight stop and could be re-entered if the setup reset." · p.9: "A tight stop allowed re-entry if the VWAP continuation setup reset instead of fighting the move."
- p.10: "Let opening drive reveal the stock's nature".

## §3 THE ENGINE TODAY (branch `setups-c1` @ `c60a7f00`, not yet on main)
| Cheat-sheet clause | Code | What it does | Match / gap |
|---|---|---|---|
| "strong move in the morning" | note `VWAP Continuation.md:40`; `anatomy/leg_roles.py:108-116` | the up-leg right before the pullback, in the trade's direction; no size rule while A-24 is null | MATCH (size tuned live, V3) |
| "drop the stock into VWAP" | note `:41`; `radar/evaluate.py:229-244`; `formation/atoms.py:349-356` | pullback low within `dist.k.vwap` × ATR of VWAP, measured either side | GAP: no number (Q1); either side (Q2) |
| "trendline break or a range break" | note `:42-48`; `formation/triggers.py:181-231` | line through 2+ falling pivot highs; flat case = a tight range's top | MATCH |
| "just below VWAP" | note `:49-56`; `formation/stops.py:197-235` | VWAP at the entry bar, less 2¢ | MATCH |
| "sell half into the high of the day" / trail | note `:65-75`; `defaults.yaml:11` | half at HOD; trail on the 20 EMA | MATCH (V2) |
| "rejection of an important resistance level" | note `:81`; `anatomy/frame.py:472-493` | HARD AVOID when PMH or PDH was wicked and closed back under | GAP (V1) |
| "opening auction was choppy" | note `:80` | text only, never computed | MATCH (V4) |
| Times 10 AM – 2 PM | note `:94-95`; `evaluate.py:1882` | window end is the radar deadline | MATCH |
| Held off | `tests/cobalt/test_setups_lego.py:69-70`; `tunables.yaml:411-418` | pinned "AWAITING ITS ENGINE FILL" while `dist.k.vwap` is null | R118 hold |

## §3b WHERE THE DESIGN CAME FROM (`30 - Design/SETUPS-AT-DEFAULTS-FINAL-2026-09-21.md`)
| Design clause (FINAL line) | Cheat-sheet source |
|---|---|
| Morning leg `Leg(opening_drive OR impulse)` (`:208`) | p.1 "a strong move in the morning" |
| `dist(pullback end, VWAP)` in working-TF ATR (`:190`) | p.1 "drop the stock into VWAP" / "Enter near VWAP" — the MEASURE is sourced |
| A-16 `dist.k.vwap` = 0.5 × ATR (R119, LOW) | **NO CHEAT-SHEET SOURCE — design invention** (the sheet gives no distance) → Q1 |
| Distance measured either side of VWAP (`:190`, `\|a − b\|`) | **NO CHEAT-SHEET SOURCE — design invention** (the sheet's stop "just below VWAP" implies holding above) → Q2 |
| `trendline_break`, flat case = micro-Range top (`:147`) | p.1 "after a trendline break or a range break"; playbook p.7 "VWAP consolidation" |
| `trendline.min_pivots` = 2 (`tunables.yaml:60`) | **NO CHEAT-SHEET SOURCE** (a ruled engine value, `source: ruling`) |
| Stop `indicator` VWAP at entry (`:161`) | p.1 "The stop should be placed just below VWAP" |
| `rejected` avoid on level set A-17 = PMH, PDH; A-18 rule (`:191`, `:370`) | p.1 has the words, but as a **factor that decreases**, not an avoid; the PMH/PDH set is **design invention** → V1 |
| Flat thresholds A-09 / A-10 (`:186`) | not read by this setup's definition (they serve other setups' `flat(...)`) — no clause here |
| `max_attempts` 1 (note `:77`, "sheet silent") | **NO CHEAT-SHEET SOURCE**; the playbook p.8 re-enters → Q3 |

## §4 THE ROLE OF `dist.k.vwap`, AND THE SMALLEST CHANGE
`dist.k.vwap` is the one number that says how near VWAP the pullback's low must end — "near" in the sheet's words, measured in average 2-minute candles. Held null (R118), the rule reads "unknown", never true or false (`evaluate.py:242-243`), so the setup forms nowhere and stays `AWAITING ITS ENGINE FILL` (`test_setups_lego.py:69-70`). The smallest change that lets it run: (1) his Q1 value written as ONE row in `1 - Trading/Assumed Defaults.md` (desk edit on his word, L65) and a `cobalt taxonomy load` — the pin lifts and the live-note gate asserts it forms on the committed day (L68 GATE EARLY); (2) Q2 as a "yes" adds one clause to the note's pullback rule and one engine check ("no pullback bar closes under VWAP") — a fix round, checked by Opus · Sol · Grok (L67); (3) V1 moves note `:81` out of `avoid` (it is already in `quality_factors`, `:88`); (4) Q3 changes note `:77`, but the radar does not count tries yet — a backlog item.

## HIS EXAMPLES
5–10 chart examples and other traders' playbooks, brought by Dejan to the sitting; reviewed against §0's decisions and §3b's inventions.

## §5 APPENDIX — engine terms (for the desk)
- Precondition: `Leg(pullback).direction == opposite(trade_direction) AND dist(Leg(pullback).end, VWAP) <= cfg(dist.k.vwap) * ATR(working_tf)` (note `:41`); unit `atr`, scope `per_indicator(vwap)`, status `proposed` (`tunables.yaml:411-418`).
- Dials: A-16 `dist.k.vwap`; A-17 `levels.set`; A-18 `level.rejected.rule`; A-24 `leg.min_size_atr`; `trendline.min_pivots`; `stop.buffer`; `ma.slow` (`defaults.yaml:11`).
- Seam: the Second Chance redesign replaces A-17's fixed set; `rejected` here reads that same set (`frame.py:472-493`) — settle in one document before either build (L72 seam clause).
- `Assumed Defaults.md` is not in the vault yet (the deploy's STEP-6 writes it) — nothing to read for this packet.
