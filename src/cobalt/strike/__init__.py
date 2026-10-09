"""F9 (19b, focus scale): the strike path — Charter §3 F9, ladder S4.

* `measure.py`  — `cobalt strike measure`: the live-feed re-measure (M1),
  measurement only, no database, no vault.
* `config.py`   — the four `strike.*` tunables rows, unit-checked (T1).
* `policy.py`   — the card's confirmation policy over i1 bars, pure (C1).
* `detector.py` — one tick: ARMED → TRIGGERED on a cross, the WATCH →
  MISSED sweep, through `CardStore.transition()` only (C2, C3).
* `cli.py`      — the `strike` verb group.

The loop runs inside `com.cobalt.radar` (`radar/runner.py`, C4) in its own
thread; there is no strike resident.
"""
