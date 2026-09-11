# `src/cobalt/radar/runner.py`

Runs the resident cycle in membership, pool-row, mirror, then per-ticker bar transactions. It checks the session before work and again through each store's `before_commit` hook, stamps partial failures, uses monotonic scan IDs, and makes idle/reset cycles perform no Finviz calls.

