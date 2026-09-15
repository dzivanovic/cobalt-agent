# `src/cobalt/radar/poller.py`

Polls admitted members in rank order through the shared bucket and bar transport. It writes closed overlapping i1 bars through `BarStore.upsert_bars`, preserves failure onset, clears recovery, and applies the stale rule only during RTH.

Carried failure records (`existing_failures`) whose ticker is not in this poll's `members` are dropped before the loop and logged once per ticker at INFO with each record's reason and `since`. A record is otherwise popped only by a fetch of its own ticker, so a name that left the pool kept its record forever (IMCC, 09-14 → 09-15, `reports/cto-2026-09-15.md` §1.2). Records for current members are unchanged: kept with their original onset until that member's fetch clears them.
