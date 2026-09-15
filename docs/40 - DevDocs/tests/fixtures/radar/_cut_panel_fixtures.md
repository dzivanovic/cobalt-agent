# `tests/fixtures/radar/_cut_panel_fixtures.py`

Hub-owned deterministic cutter for the three S2-P3 radar-panel fixtures. It reads raw production-query JSON only from explicitly named environment paths and never opens a database.

`cut_pool_and_membership()` shifts all pool and membership dates/timestamps to the fixed synthetic anchor while preserving intra-day offsets, rebases scan identifiers by the same day delta, and recursively zeroes 12-hex source suffixes. `cut_pool_block()` applies the same recursive transform and zeroes note/block hashes. `cut_cards_contract()` keeps the real `aset_sizings` column shape while synthesizing one row per lifecycle state plus the manual-owner and degraded cases, with full card-spec §6 presentation fields (`setup`/`trade`/`why`/`dots`/`health`/`trails`/`default_trail`/`trail_why`/`attempt`/`attempt_max`/`news`/`notes`) attached per card.

`cut_pool_and_membership()` optionally merges a second, real, already-completed trading day (`RADAR_FIXTURE_RAW_MEMBERSHIP_PRIOR`) into the membership array, appended after the primary day and filtered to tickers absent from the primary day (no group may mix a still-open primary-day episode with a closed prior-day one). This exists because a single partial trading day at cut time has too little churn to contain a real same-ticker exclude→promote→depart→re-enter sequence; the primary day alone stays the one `RadarStore.members_for_day`-scoped, pool.members-consistent day — the merged slice is additional real-shape texture for fixture-level (not builder-level) assertions.

The script is fixture-generation evidence owned by the hub. The Sol build consumed its (first-cut) outputs but did not run or modify the cutter or generated fixtures; the hub re-ran the cutter post-build to fix two self-consistency gaps Sol's own test run surfaced (see `reports/s2-p3-2026-09-15.md` §Fixtures v2).

