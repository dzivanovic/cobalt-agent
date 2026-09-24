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
- `ReplayFormation` is the per-formation row of that report: `seen_at, ticker, slug, direction, trigger, stop, formed_bar_ts, membership_id, trade_def_md5, score_inputs_sha256`. Frozen, `extra="forbid"`.

## The three subject fields (added 2026-09-18, S2-P4 chunk E2)
`membership_id`, `trade_def_md5` and `score_inputs_sha256` were added
ADDITIVELY for downstream consumers that must key a row on a formation —
S2-P4's `"user".missed` rows, whose `kind='formation'` CHECK needs the
member and the def, and whose unique index needs the formation bar so two
same-day formations of one (ticker, trade_def) do not collapse into one
row (Astra R1-21).

Every one of the three is a value `evaluate_member` already returned for
that formation (`ev.membership_id`, `ev.md5`, `ev.inputs_sha256`). Nothing
new is computed here, nothing is written, and no schema changed: the
`--replay` path is as read-only as it was.

`score_inputs_sha256` is the reference to the RETAINED SCORE RECEIPT. The
resident stores that same digest in `system.radar_score.inputs_sha256` on
its row for the same `(membership_id, trade_def_md5)`. Because this path
reads no receipt row, the reference is content-addressed — a natural key
plus a digest — not a score id. A consumer resolves it with a lookup; a
digest that does not match means the resident evaluated different inputs,
which is the point of keeping it (L57).
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
