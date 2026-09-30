# `src/cobalt/replay/runner.py`

The nightly replay run in its ruled order (S2-P4 STEP-4, R3 as amended by
R1-15/R1-16/R1-17/R2-3).

## `run_nightly(trade_date, *, dry_run, deps, live=None)`
`live` defaults to "trade_date is today in ET". A live run fetches; a
historical run reads what was retained.

| Step | What | Commit side |
|---|---|---|
| (0) precondition | `archiver_precondition` on the `com.cobalt.archiver` row | read only |
| `movers` | benchmark settings (USER read) → exports → `export_counts` → `movers_store.reconcile` → `archive_movers` → `mark_bars_archived` → membership read → `benchmark_misses` → `missed.reconcile(kind="mover")` | SYSTEM, then USER |
| `cards` | candidates + positions (USER) → bars (SYSTEM read) → `replay_card` each → `missed.reconcile(kind="card")` | USER |
| `formations` | `missed.radar_cards` (USER read) + bars (SYSTEM read) → `deps.formation_source` (default `formation_replay`) → `missed.reconcile(kind="formation")` when it returns rows | USER |
| `line` | `render_line` from the current rows → `drc_path` → deadline check → `write_miss_line` | vault (L28) |

- No connection spans both schemas (R2-3). Recovery is a rerun:
  reconciliation is idempotent and keyed to `replay_run_id`, so a retry
  after any commit boundary resumes. This is tested with a crash after the
  SYSTEM commit.
- A failing step raises `StepFailed(step, error)` with `.result`
  (`failed_step`, `steps_done`). Earlier commits stand and later steps do
  not run.
- Per-ticker archive failures are counted and raise `ReplayError("N movers
  archive failure(s)…")` **after** the line (archiver semantics).
  Incomplete coverage is counted, not failed.
- **Archived-partial movers (2026-09-24, R113).** `movers_step` turns
  `outcome.partial` into `result.archive_partial` (one `ArchivePartial` per
  ticker, `sides` read from the stored movers) and counts
  `result.archive_partial_by_side` per side. Each partial is logged as one
  WARNING (`… PARTIAL — <reason> (<n> i1 bars, <first> → <last>)`), and
  each incomplete ticker — a clean fetch with zero bars — as one ERROR
  naming it. `archive_incomplete` no longer counts partial tickers.
- **What the export really had (2026-09-19).** Between the exports and the
  first write, `movers_step` records `result.movers_by_side =
  export_counts(exports, top_n=settings.top_n)` — per side, the export's
  own row count and `min(top_n, exported)`. One pure statement over
  values already in memory: it selects, orders and drops nothing, and the
  movers stored, benchmarked and archived below it are unchanged. Every
  path records it, because all three (live, dry run, retained `--date`)
  reach the same `exports` list. It is what lets the S2 smoke's K9 pass a
  short side and fail a side holding fewer rows than its export allowed,
  without a hand count of the cached CSV.
- Every miss is printed as `MISS card <id> <ticker> <dir> excluded_by=<gate>
  cf_r=…`, `MISS mover <ticker> excluded_by=<gate> change=…%` or
  `MISS formation <ticker> <dir> member=<id> formed=<ts>
  excluded_by=no_card cf_r=…`. That is the report listing each miss with
  its gate.

## `archiver_precondition(row, *, trade_date, now, registry)` (R1-15)
It refuses (`archiver not done: …`) on: an absent row, state not `done`, a
nonzero exit, missing or inverted `started_at`/`finished_at`, a finish in
the future, a start before that date's scheduled `at` (20:30 ET), or a
future trade date. For tonight it also requires the start's ET date to be
tonight; the ET date is what counts, so a 20:35 ET start stamped 01:35 UTC
passes. For a past date, a clean run started at or after that night's
occurrence is the only evidence `cobalt_jobs` keeps (one row per label).

## `replay_deadline(now, *, registry, tunables)` (R1-16)
`deadline = com.cobalt.backup at − replay.backup_margin_s` (21:40 − 300 s =
21:35 ET).
- A start before the deadline enforces it.
- A start inside `[deadline, backup)` raises `DeadlineExceeded`.
- A start after the backup has no deadline.

It is enforced before every step, per card, before the vault write, and on
async collector work through `asyncio.wait_for`. A slow collector that is
still heartbeating is cut at the deadline. A dry run has no deadline
because it writes nothing.

**2026-09-25 — the formations cut (`cto-2026-09-24.md` R95).**
- **The reserve.** With a deadline, the run also reads `replay.formations_reserve_s` at start. If it is missing or null the run raises `ReplayError` naming it (L1), before any step.
- **The cut.** The formations step hands the formation source `cut_at = now >= deadline − reserve`, which is asked between scans (`evaluate_cli.replay_formations`). With no deadline (dry run, or a start after the backup) `cut_at` is None.
- **A cut run:**
  - sets `ReplayResult.formation_cut` (`FormationCut`);
  - reconciles its rows as usual;
  - writes the line with the PARTIAL clause (the pre-write deadline check still guards it);
  - then FAILS AT THE END with `ReplayError("formations cut at the deadline — k of n scans")`, in the archive failures' place. Both together make one error, archive failures first. `failed_step` stays None.

## `formation_replay(trade_date, *, out, sources=None, context=None)` (R4, R1-21)

**2026-09-18 — S2-P4 chunk E2.** The adapter is now BOUND. It returns a
`FormationOutcome` (status, rows, counts), not a tuple.

| S2-P2 in the tree | What happens |
|---|---|
| absent | logs and prints exactly `trade_def replay: not available until S2-P2`, status `unavailable`, no rows |
| present, model missing any of `FORMATION_REQUIRED_FIELDS` | `ReplayError`, "present but incompatible: missing […]" |
| present, `EVALUATOR_VERSION` outside `SUPPORTED_EVALUATORS` | `ReplayError`, "incompatible: evaluator version …" |
| present and compatible, no `sources`/`context` | `ReplayError`, "no formation sources" — a half-wired binding never runs |
| present, compatible, wired | calls P2's OWN `replay_formations` for the day and hands its report to `formations.formation_misses` |

TWO S2-P2 MODULES, BOTH IMPORTED STATICALLY: the entrypoint and its model
are in `cobalt.radar.evaluate_cli`, the capability marker
`EVALUATOR_VERSION` is in `cobalt.radar.evaluate`. The plan named one
module (`cobalt.radar.evaluate`); the code follows the shipped layout and
never accepts one name in two spellings (L3). The imports are static
because a string-named dynamic import would make the L42 restart
classifier restart every resident.

A `ModuleNotFoundError` naming anything OTHER than those two modules is
re-raised: a broken dependency inside S2-P2 is not "S2-P2 is not deployed".

## `ReplayDeps`
A dataclass of everything the run touches: stores, registry, tunables,
clock, session bounds, settings reader, collector factory, writer factory,
DRC path, output and ceiling. Tests record every call on it.
`cli.default_deps` is the production wiring.

`formation_source` (default `formation_replay`) and `formation_sources`
(the factory that builds S2-P2's own replay arguments) are the two
formation seams. The `formations` step builds its `FormationContext` from
the deps it already holds — the SYSTEM bar read it uses for cards and the
USER `missed.radar_cards(trade_date)` read — and both are callables, so
nothing is read when S2-P2 is absent.

## 2026-09-29 — DRC D3-3: no DRC note at 21:10
The `line` step no longer fails when the day's DRC note is absent (R66:
no DRC is his lawful choice; `[F-24]`). `deps.drc_path` raising
`DrcNoteAbsent`, or returning a path that is not a file, now: creates
nothing and writes nothing; stores the EXACT `render_line` arguments on the
result (`ReplayResult.line_inputs`, via `line.stored_line_inputs` —
`card_rows`, `mover_rows`, `settings`, `formation_replay`, `input_stale`,
`formation_rows`, `formation_suppressed`, `formation_input_stale`,
`formation_cut`), which the CLI stores in `job.result` (the existing
`cobalt_jobs.last_result` JSON — no migration); sets `line_action` to
`pending (no DRC)`; prints `line: pending (no DRC) — <the line>`; and the
step ends green. The DRC build, once `drc-rules` exists, is the only later
writer of that line, from the stored blob (`line.render_stored`); E6
proves the re-render is byte-identical. A note present at 21:10 is written
exactly as before.
