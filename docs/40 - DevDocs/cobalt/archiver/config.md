# `src/cobalt/archiver/config.py`

## What it does
Loads and validates `configs/cobalt/watchlists.yaml` — the three-tier
watchlist (config-as-code, TRIAGE cross-cutting law). `configs/cobalt/`
is a second sanctioned new-core config location alongside
`configs/dev/` (CLAUDE.md's config boundary law) — safe for the same
reason: the old loader's glob (`configs/*.yaml`) is top-level only and
never reaches either subdirectory.

## Key functions/classes
- `Tier` — `description`, `intervals: list[Interval]`, `tickers:
  list[str]`. `extra="forbid"`.
- `WatchlistsConfig` — exactly `tier_a`, `tier_b`, `tier_c`, each a
  `Tier`.
  - `.archive_targets() -> list[(ticker, interval)]` — every pair to
    archive nightly: the cross product of each of tier_a and tier_b's
    tickers × that tier's intervals. **tier_c is deliberately excluded**
    — it's a browse list, no archiving, present for future use only.
  - `.backfill_targets(ticker) -> list[(ticker, interval)]` — tier_a's
    interval set applied to one arbitrary ticker (the on-demand
    backfill path — used regardless of which tier that ticker is
    actually in).
- `ConfigError(RuntimeError)` — the one error type.
- `load_config() -> WatchlistsConfig` — reads, validates, raises
  `ConfigError` with the file path and detail on any failure. No
  local/private override file exists for this config (unlike
  `aset.local.yaml`) — ticker lists aren't sensitive.

## Data flow in/out
**In:** `configs/cobalt/watchlists.yaml`.
**Out:** a validated `WatchlistsConfig`, or a raised `ConfigError`.
Called fresh by `runner.py` at the start of every run — no caching.

## Config it reads
Itself — this **is** the config loader.
