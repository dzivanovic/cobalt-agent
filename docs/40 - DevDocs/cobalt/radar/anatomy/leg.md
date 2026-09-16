# `src/cobalt/radar/anatomy/leg.py`

## What it does
`legs(bars) -> tuple[LegObservation, ...]` splits a run of working bars into legs (TAXONOMY v0.7 §3.1). A leg is one directional move, ended by the first opposing bar.

## Conventions (Astra R1-9)
- A bar's direction is the sign of close − open; equal is `flat`.
- A flat (doji) bar never starts or ends a leg. It extends the current one, and leading flats join the first directional leg.
- One opposing bar ends the current leg (`terminated=True`) and starts the next. The last leg is open.
- The base is the first bar handed in. The caller picks it (`extension.leg_base: session_open`, replay_pending).

## Gotchas
Consolidation-terminated legs (micro-Range) are an S3 detector. S2 uses legs only for `Extension.leg_count`.
