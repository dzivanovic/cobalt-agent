# `src/cobalt/radar/poller.py`

Polls admitted members in rank order through the shared bucket and bar transport. It writes closed overlapping i1 bars through `BarStore.upsert_bars`, preserves failure onset, clears recovery, and applies the stale rule only during RTH.

