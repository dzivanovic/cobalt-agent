# `src/cobalt/radar/runner.py`

Runs the resident cycle in membership, pool-row, mirror, then per-ticker bar transactions. It checks the session before work and again through each store's `before_commit` hook, stamps partial failures, uses monotonic scan IDs, and makes idle/reset cycles perform no Finviz calls.

A transaction that reaches `market_reset` rolls back and records its stage on the resident runner without attempting another write in the blocked window. The next active cycle includes that pending stage and scrubbed detail in its pool-row transaction, keeps the stamp visible through that cycle's poll-status transaction, and then clears the in-process pending marker. A later cycle can clear a recovered bars failure normally.

`_pool_row` (S2) carries the previous row's `poll_failures` forward and, when that list is non-empty, writes `failed_stage='bars'` and `failed_detail='poll failures: N'` — the same strings `RadarStore.stamp_poll` writes at S4. Before 2026-09-15 S2 wrote the row clean and S4 re-stamped it about 70 s later; a heartbeat beat that sampled the gap read OK, so the radar probe flapped (27/27 beats fit that phase rule, `reports/cto-2026-09-15.md` §1.2). Membership, pending-drop and mirror failure stages still override the carried `bars` stage exactly as before, and S4's `stamp_poll` remains the one place a bars failure clears.
