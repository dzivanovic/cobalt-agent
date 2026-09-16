# `src/cobalt/radar/anatomy/extension.py`

## What it does
`detect_extension(run, params) -> ExtensionObservation` detects an intraday Extension (TAXONOMY v0.7 §3.2) over the run from the session open to the last closed working bar. The run's direction is the sign of last close − session open.

## The two paths (R4)
- **Path A (lands cards):** a bar in the run direction whose volume is at least the volume band threshold of the `n` bars before it, AND whose body is strictly wider than every earlier body of the run. The latest such bar is the culmination, and the result is `instantiated=True, state="culminating", path="A"`.
- **Path B-only:** |last close − open| ≥ `path_b_atr` × ATR(14) with no path-A bar. The catalyst is unknown in S2, so this reports `path="B_only"`, `unavailable="catalyst_ref_unknown"`, with `instantiated` and `state` both None. It is logged by the dry-run and never produces a card, but it is not reported as "not instantiated" either.

## Key functions/classes
`ExtensionParams.from_tunables(rows)` reads `extension.path_a_volume_ma_bars` (n), `extension.path_a_volume_sigma` (k) and `extension.path_b_atr`. A missing or unmeasured row raises. The observation stores every intermediate: session open, last close, the culminating bar's ts, volume and body, the widest prior body, the band, the ATR, the distance in ATRs and the params.

## Gotchas
Any incomplete bucket in the run gives `unavailable="incomplete_bucket"`. Fewer than max(n+1, 14) bars gives `insufficient_bars`. The value is never computed from part of the run. A run that closes exactly at its open has no direction and is not instantiated.
