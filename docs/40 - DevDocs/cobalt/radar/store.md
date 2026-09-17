# `src/cobalt/radar/store.py`

System-side `RadarStore` for membership episodes and the pool status row. Membership, pool, and failure stamps are separate idempotent transactions; each checks `assert_writable` and calls the supplied commit gate immediately before commit.

## Reads

- `open_members(pool_key)` returns the open episode fields required by the radar decision engine.
- `pool_row(pool_key)` returns the complete status row or `None`.
- `members_for_day(pool_key, trade_date)` returns every membership column for every episode in exactly one pool/day, ordered by identity. It intentionally includes admitted open rows, departed admitted rows, and never-admitted exclusions. Callers distinguish admission through `entered_at`, not through `left_at` alone.

All three are plain SELECT paths. They do not initialize a schema or invoke a write guard.

## Writes

`apply_membership`, `put_pool`, `stamp_failure`, and `stamp_poll` remain the resident's guarded write transactions. `stamp_poll(..., preserve_failure=True)` updates S4 freshness without clearing the pending reset-crossing failure that S2 first made observable in the same recovery cycle. The default remains `False`, so ordinary successful polling still clears a recovered `bars` failure.

## S5 evaluate seam (S2-P2 STEP-4)
System payload only (L32, Astra R1-1).

Reads:
- `admitted_members(pool_key)`: open admitted episodes by id.
- `memberships(ids)`: raises when an id an open card references is missing.
- `i1_bars(ticker, start, end)`: stored bars as `Bar`, oldest first.
- `latest_run_id(pool_key)`.
- `board(pool_key)`: `radar_board_v`.
- `members_for_replay(pool_key, day)`.

Writes — each is one guarded transaction (`assert_writable('radar.evaluate')` + `before_commit`):
- `abandon_running_runs` marks a stale `running` run `failed`, named "abandoned".
- `open_score_run` inserts the run as `running`.
- `put_scores` re-validates every `detail`/`desk_shadow` through `seam.RadarScoreDetail`/`DeskShadow` at the write, and returns `{(membership_id, md5): score_id}`.
- `copy_card_values` puts the card's proximity/conviction/card_score/suppression onto its seam row.
- `finish_run` publishes `complete` or `failed`, and refuses a run that is not `running`, so a published run is never re-published.

## Audit export reads (S2-P2 STEP-11)
- `score_run(run_id)`: one `radar_score_run` row as a dict, or `None`.
- `scores_for_run(run_id)`: every `radar_score` row of that run, by id.

Both are plain SELECTs; `radar.audit_export.export_run` pairs them with the user-side receipt chain and refuses a run whose stored hashes or seam labels do not replay.

---

## 2026-09-17 — S2-P4: `rank_metric` / `rank_value` (ruling R1)

- `open_members` and `members_for_day` select both columns.
- `apply_membership` writes the pair on RETAIN, on the in-place UPDATE of
  a never-admitted EXCLUDE, and on INSERT.
- HOLD has its own UPDATE. A HOLD with no metric keeps the stored pair
  (`COALESCE`). A HOLD that carries a metric writes both together, so the
  metric and the value never come from different scans.
- LEAVE touches neither column: the departed episode keeps its last values.

No backfill (L57): rows written before 0008 stay NULL.
