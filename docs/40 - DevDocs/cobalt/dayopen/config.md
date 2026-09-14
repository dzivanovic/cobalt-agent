# `src/cobalt/dayopen/config.py`

Two ruled tunables (L53): `dayopen.c4_expected_session_blocks` (8,
`proposed` — a moving baseline) and `dayopen.c6_max_gap_min` (20,
`solidified`), both in `configs/cobalt/taxonomy/tunables.yaml`.

Every other day-open threshold REUSES an existing tunable rather than
duplicating it (L3): `session.premarket_open` (C2/C3's "has the scan
started" line) and `session.aftermarket_close` (C6's "previous evening"
anchor), both read through `cobalt.session.clock`, never re-declared
here.
