# `tests/cobalt/test_radar_panel.py`

Offline contract suite for the S2-P3 radar read layer, typed builder, pure renderers, and GET-only FastAPI routes. It uses the hub-cut real-shape pool/settings/card fixtures without editing them, then creates isolated in-memory snapshots for boundary cases.

The suite covers episode identity and admission categories, pool/member consistency, rank ordering, churn cursor equality/retry behavior, ET trading-day selection, retained prior-day data, all five current clock sessions, stored-session metric labels, configured freshness, every fail-loud source, HTML escaping, ladder ordering and lifecycle rendering, health/owner/detail contracts, responsive rules, disabled P2 controls, refresh failure behavior, exact GET-only routes, and sentinel proof that radar requests bypass write-capable sheet helpers.

The `requires_db` integration test is skipped without Postgres variables. Under the hub's `cobalt_dev` transaction fixture it inserts a uniquely named pool plus open/left/other-day episodes, proves `RadarStore.members_for_day()` returns open and left rows for exactly one pool/day, and relies on the outer transaction rollback for cleanup.

