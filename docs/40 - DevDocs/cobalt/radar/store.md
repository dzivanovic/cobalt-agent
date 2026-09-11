# `src/cobalt/radar/store.py`

System-side `RadarStore` for membership episodes and the pool status row. Membership, pool, and failure stamps are separate idempotent transactions; each checks `assert_writable` and calls the supplied commit gate immediately before commit.

