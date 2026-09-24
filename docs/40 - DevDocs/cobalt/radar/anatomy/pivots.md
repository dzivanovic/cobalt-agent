# `cobalt.radar.anatomy.pivots` — swing pivots

Added 2026-09-22 in STEP-4 of the setups one build (FINAL §3 D2; taxonomy §3.3).

`pivots(bars, n)` returns the pivot highs and lows of the bars:

- A pivot high has a high STRICTLY above each of the `n` bars on either side; a pivot low, a low strictly below them.
- The last `n` bars cannot be pivots yet.
- `n` is `cfg(pivot.n)`, read through `pivot_n(rows)`: `TUNABLE_KEYS = ("pivot.n",)`.

Pivots serve structure, never triggers. Their consumers are the micro-Range's counter-pivots (`recent_higher_low`, whose stop is registered at STEP-5) and the trendline of STEP-7. No atom reads them at this step. The function is pure.
