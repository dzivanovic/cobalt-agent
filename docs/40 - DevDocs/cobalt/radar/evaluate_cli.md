# `src/cobalt/radar/evaluate_cli.py`

## What it does
`cobalt radar evaluate` has two deliberately separate paths (S2-P2 STEP-4, R3/R9, Astra R1-11):

- `--replay <date> [--trade-def <slug>]` **writes nothing**. It reads the day's admitted membership episodes, stored i1 bars, the loaded trade_defs and daily bars from the radar cache only (a fetch would write the cache). It steps a virtual clock through RTH at `radar.scan_interval` and evaluates every admitted member against every def through the same `evaluate_member` the resident runs. It prints:
  - each formation once: ticker, def, direction, trigger, stop, formation bar;
  - each path-B-only formation (not evaluable in S2);
  - each def's `not evaluable: missing atoms […]` line.
  This is the list Dejan reviews before enable.
- `--candidate <date> --settings-file <d2.yaml> --sha256 <hash> [--taps <file>] [--trade-def <slug>]` is the **dev-persistence harness**, and it writes to cobalt_dev only. It runs the real `EvaluateStage` over a captured day:
  - the frozen, reviewed D2 card settings override the live card keys in memory (trader_settings is never written);
  - RVOL comes from that day's receipts;
  - simulated taps are applied to every card it creates.
  The output is non-null candidate scores, every numeric dot and every N/A path, for the L52-d audit bundle.

## Key functions/classes
- `replay_formations(day, *, pool_key, slug_filter, radar_store, defs_source, daily_source, tunables, defaults, clock, out)` returns a `ReplayReport` (scans, formations, path-B-only lines, not-evaluable map, evaluation counts).
- `admitted_at(rows, instant)` returns the episodes admitted at an instant. `scan_instants(day, clock, interval, first)` returns the RTH scan grid.
- `CachedDailyBars` is the read-only half of the daily collector (same `<root>/<ET date>/daily/<T>.csv` path). A missing file is an error, never a fetch.
- `assert_dev_database()` raises `CandidateRefused` unless `COBALT_ENV` resolves cobalt_dev.
- `curve_coverage_gaps(defs, frozen)` lists each evaluable def's computed factors (those with a computer) that have no curve.
- `candidate_run(...)` refuses non-enabled settings, a coverage gap, or a malformed tap, then runs the stage per scan instant. It returns a `CandidateReport` (run ids, receipt ids, cards, taps applied, frozen settings sha256).
- `receipt_rvol` and `rvol_as_of` return the RVOL observations the day's receipts retained, and the latest one per ticker at an instant.
- `evaluate_command(args)` is the CLI entry, registered in `radar/cli.py`.

## Gotchas
- The replay has no screener snapshot, so its RVOL dot is `input_unavailable`. That changes no formation, only the dot. The candidate harness takes RVOL from receipts instead, so it needs the day's receipts present in cobalt_dev.
- The parameter is `slug_filter`, not `trade_def`: the names-rule lint reads `trade_def: <word>` as a slug.
