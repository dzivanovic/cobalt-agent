# `src/cobalt/radar/store.py`

System-side `RadarStore` for membership episodes and the pool status row. Membership, pool, and failure stamps are separate idempotent transactions; each checks `assert_writable` and calls the supplied commit gate immediately before commit.

`stamp_poll(..., preserve_failure=True)` updates S4 freshness without clearing the pending reset-crossing failure that S2 first made observable in the same recovery cycle. The default remains `False`, so ordinary successful polling still clears a recovered `bars` failure.
