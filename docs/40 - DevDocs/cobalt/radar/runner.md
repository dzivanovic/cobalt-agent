# `src/cobalt/radar/runner.py`

Runs the resident cycle in membership, pool-row, mirror, then per-ticker bar transactions. It checks the session before work and again through each store's `before_commit` hook, stamps partial failures, uses monotonic scan IDs, and makes idle/reset cycles perform no Finviz calls.

A transaction that reaches `market_reset` rolls back and records its stage on the resident runner without attempting another write in the blocked window. The next active cycle includes that pending stage and scrubbed detail in its pool-row transaction, keeps the stamp visible through that cycle's poll-status transaction, and then clears the in-process pending marker. A later cycle can clear a recovered bars failure normally.
