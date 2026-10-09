# `src/cobalt/strike/detector.py`

One `StrikeDetector.tick()`, only in PREMARKET or RTH (else `idle:<session>`, no read, no GET):

1. `CardStore.strike_cards()` — radar cards in WATCH or ARMED with `created_at` and the `at` of the latest ARMED transition (manual cards are not watched, D6).
2. Every `strike.missed_sweep_interval` s: the MISSED sweep over the WATCH cards on the i1 bars the radar poller already stored (`BarStore.bars_in_range`, no GET), from `created_at`; then the radar's plan is read again (it is also read at the first tick).
3. The first `strike.max_armed` ARMED cards by ARMED `at` are kept (D4); every card left out is logged by id and ticker.
4. `poll_interval(names, headroom_rpm, floor_s) = max(floor_s, ⌈names × 60 / headroom_rpm⌉)`, headroom = `radar.finviz_max_rpm` − the radar's planned rpm (`configured_sources().demand.headroom_rpm`); the strike demand is counted as consumer `strike` by `check_scheduled_demand("strike", …)` (`check_strike_demand`). A refusal, an unreadable plan or headroom ≤ 0 → logged, no GET this tick (D2).
5. One `fetch(ticker, Interval.I1, token)` per kept card through the detector's own `TokenBucket` at names × 60 / interval rpm (D8); `crossed(policy, …, since = ARMED at)`; a cross → `transition(card, TRIGGERED, actor=cobalt, evidence=CONTRACT, now=<tick>)`. A refused move (`IllegalTransition`, `CardStateError`, `SessionBlocked`) is logged and skipped; a fetch failure is logged scrubbed and fetched again next tick.

The policy is the one of the def now loaded for the card's slug (`TradeDefStore.get`); a changed md5 still uses it, and both md5s are in the evidence. A sequence trigger or no policy is logged `unwatchable` once per card (D5). `build_detector()` wires the real store, defs, bars, transport and clock for the radar resident.

## CONTRACT

The evidence of every transition this module writes; S4-P2 reads it. Keys, in order, byte-for-byte (`CONTRACT_KEYS`):

```
{"via": "strike.detector", "policy": <type>, "entry": "<decimal>", "cross_price": "<decimal>", "bar_ts": "<iso utc>", "bar_close_at": "<iso utc>", "seen_at": "<iso utc, the poll's wall clock>", "cadence_s": <int>, "def_md5": "<md5 used>", "card_def_md5": "<card's md5>"}
```

- `via`: `strike.detector` (ARMED → TRIGGERED) or `strike.missed` (WATCH → MISSED).
- `cadence_s`: the derived interval for `strike.detector`; `strike.missed_sweep_interval` for `strike.missed`.
- Edges written: ARMED → TRIGGERED and WATCH → MISSED only (`models.ALLOWED`; MISSED carries the reason `trigger crossed while WATCH (<policy>, bar <bar_ts>)`).
- Actor: `cobalt`, always.

## 2026-10-09 — s4-p1-1009
New module (S4-P1 C2, C3).
