# `tests/cobalt/test_archiver_config.py`

## What it does
Tests `archiver/config.py`'s fail-loud loading and the archive/backfill
target-derivation logic. Two tests run against the real, committed
`configs/cobalt/watchlists.yaml`; the rest isolate via `monkeypatch` +
`tmp_path` or construct a `WatchlistsConfig` directly in memory.

## Key functions/classes (what's covered, not defined)
- `test_committed_watchlists_config_is_valid` — the real config loads;
  tier_a's intervals are exactly the 5-interval set, tier_b's exactly
  `[i5, i30]`, tier_c's empty (no archiving).
- `test_no_ticker_appears_in_more_than_one_tier` — a sanity check on
  the real, hand-derived tier lists: no symbol is double-classified.
- `test_vix_excluded_from_every_tier` — the named data-layer gap never
  silently ends up in a tier.
- Missing file, non-mapping YAML, unknown `Interval` value, unknown
  top-level key — all crash with `ConfigError`.
- `test_archive_targets_covers_tier_a_and_b_not_c` — the cross-product
  logic, and that tier_c is genuinely excluded.
- `test_backfill_targets_uses_tier_a_intervals_for_any_ticker` — the
  on-demand path applies tier_a's interval set regardless of which
  tier (or no tier) the ticker actually belongs to.

## Data flow in/out
Two tests read the real `configs/cobalt/watchlists.yaml`; the rest
write throwaway YAML under pytest's `tmp_path`.

## Config it reads
`configs/cobalt/watchlists.yaml` (only in the two ambient tests).
