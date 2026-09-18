# `src/cobalt/replay/cli.py`

`cobalt replay nightly [--date YYYY-MM-DD] [--dry-run]` is the entry point
of `com.cobalt.replay` (`ops/com.cobalt.replay.plist`, Mon–Fri 21:10, with
`COBALT_ENV=production` and `COBALT_VAULT_PATH`, like the prefill plists).

## `cmd_nightly`
- `--date` defaults to today in ET (`now_et()`).
- The command runs inside `as_job("com.cobalt.replay", skip=args.dry_run)`.
  A dry run is not a run: no jobs row is registered, stamped or finished,
  and it does not satisfy the MISSED probe.
- It builds `default_deps(dry_run=…)` and calls `runner.run_nightly`.
  `job.result = ReplayResult.job_result()` on success. On a `ReplayError`
  the partial result is attached first, so a failed row still says which
  step failed and what ran.
- It prints one summary line: movers, archived, card and mover misses,
  input_stale, formations, line action.

## `default_deps(dry_run=)` — the production wiring
- Stores: `JobStore`, `MissedStore` (USER), `MoversStore`, `BarStore` and
  `RadarStore` (SYSTEM). Also `TraderSettingsStore.values` and the job
  registry and tunables.
- `session_bounds(day)`: RTH open and close from the session clock. A
  non-trading day refuses.
- `collector_factory`: resolves the Finviz token, then builds a
  `MoversCollector` on `process_bucket(radar.finviz_max_rpm)` with the
  `radar.yaml` cache dir. An unmeasured ceiling refuses.
- `writer_factory(dry)`: `VaultWriter("replay.nightly", VaultWriteStore())`.
  It calls `ensure_schema()` only for a real run, so a dry run performs no
  DDL (R1-17).
- `drc_path = line.drc_note_path`.

Constructing the deps writes nothing. Every write lives behind a runner
call that a dry run never makes.

`build_parser()` is a standalone parser for tests. `add_parser(sub)` mounts
the group in `cobalt.cli`.
