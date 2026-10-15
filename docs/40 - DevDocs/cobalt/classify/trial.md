# `src/cobalt/classify/trial.py`

## What it does
The trial runner behind `cobalt classify trial` (plan §3, M1–M8).

- `plan(cfg, clf, set, reps=, mode=, questions=, reverse=)` → `Plan`:
  the set's questions (the first n with `questions`, plan M2; the map
  reversed with `reverse` and nothing else, M6), the call SHAPES for the
  mode, and the items. Every rendered body passes `_guard_outbound` here.
  A REAL item (`real:` provenance, T9's day-open reports) that fails is
  SKIPPED loud (`logger.error`) and counted in `Plan.skipped`, never sent.
  A constructed item that fails raises, because it means the config is
  broken. `Plan.calls` = items × reps × shapes.
- Modes: `single` sends one call per item with every question.
  `parallel` sends one call per question, up to `max_parallel` threads
  per item (M3). `sequential` sends one call per question, in order.
  `gated` sends a layered set's levels (`TrialConfig.level_keys`, L20 =
  S1 · S2 · S3 · the ten gates) as one call each, in order (M4). Gated
  means ORDERED only: no level is skipped on an earlier answer, because
  no gate rule is ruled. A set with no levels is refused.
- `dry_run(plan, clf)` → one `DRY …` line: calls, the projected input
  tokens (the rendered body bytes ÷ 4, stated as an estimate), the
  projected USD from the listed entry pricing, the ledger total and the
  cap. It makes ZERO network calls and creates no ledger file.
- `run(plan, clf, tag=)` asks `ledger.check` about the WHOLE run's
  projection and call count FIRST: if refused, zero calls are made and no
  file is written (TOTAL demand, L53). Each call is then checked again
  inside `classify()`, and `ledger.stop_if()` runs after every item. Each
  call writes one `CallRecord` JSON line to
  `results_dir/classify-results-<set>-<tag>-<UTC stamp>.jsonl` (inside
  `scratch/`), and the file is created on the first record. The closing
  `RUN …` line gives the counts by status, the latency p50 / p95 / p99,
  the per-item wall-time percentiles when a mode makes several calls per
  item (B2's comparison), the spend of this run and the ledger total.
  Invalid responses are counted and logged loud (plan B3). A
  `ClassifyAuthError` or an overrun stops the run, and the lines already
  written stay.
- `percentile(xs, p)` is nearest-rank, computed by code (L35).

## What it never does
Holds a key (the collector reads it per request); sends a body the guard
refused; talks to any host but `openrouter.ai`; writes outside
`scratch/`; opens a database; writes the vault; retries a call.

## Laws
L1 (an all-skipped set, a missing price → FAILED), L10 (sets from config),
L35 (counts and percentiles by code), L53 (total-demand ledger), L57
(one full record per call), L41 (the guard before any send).
