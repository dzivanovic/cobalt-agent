# `src/cobalt/strike/__init__.py`

The F9 strike path (Charter §3 F9, ladder S4): `measure` (the live-feed re-measure), `config` (the four `strike.*` rows), `policy` (the confirmation policy over i1 bars), `detector` (ARMED → TRIGGERED and WATCH → MISSED through `CardStore.transition()`), `cli` (the `strike` verb group). The loop runs inside `com.cobalt.radar` in its own thread (`radar/runner.py`); there is no strike resident.

## 2026-10-09 — s4-p1-1009
New package (S4-P1 rows M1, T1, C1–C4).
