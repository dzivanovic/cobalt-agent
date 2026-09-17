# `src/cobalt/replay/runner.py`

The nightly replay run in its ruled order (S2-P4 STEP-4, R3 as amended by
R1-15/R1-16/R1-17/R2-3).

## `run_nightly(trade_date, *, dry_run, deps, live=None)`
`live` defaults to "trade_date is today in ET". A live run fetches; a
historical run reads what was retained.

| Step | What | Commit side |
|---|---|---|
| (0) precondition | `archiver_precondition` on the `com.cobalt.archiver` row | read only |
| `movers` | benchmark settings (USER read) → exports → `movers_store.reconcile` → `archive_movers` → `mark_bars_archived` → membership read → `benchmark_misses` → `missed.reconcile(kind="mover")` | SYSTEM, then USER |
| `cards` | candidates + positions (USER) → bars (SYSTEM read) → `replay_card` each → `missed.reconcile(kind="card")` | USER |
| `formations` | `deps.formation_source` (default `formation_replay`) | none today |
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
- Every miss is printed as `MISS card <id> <ticker> <dir> excluded_by=<gate>
  cf_r=…` or `MISS mover <ticker> excluded_by=<gate> change=…%`. That is
  the report listing each miss with its gate.

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

## `formation_replay(trade_date, *, out)` (R4, R1-21)
- `cobalt.radar.evaluate_cli` absent: logs and prints exactly `trade_def
  replay: not available until S2-P2` and returns `("unavailable", [])`.
- Present but missing `replay_formations`/`ReplayFormation`, or any of
  `FORMATION_REQUIRED_FIELDS` (`membership_id, trade_def_md5, ticker,
  direction, trigger, stop, formed_bar_ts`): refuses as incompatible.
- Present and compatible: refuses too until the binding is written against
  the real contract. No second formation path is guessed.

The import is static (`import cobalt.radar.evaluate_cli`). A string-named
dynamic import would make the L42 restart classifier restart every resident.

## `ReplayDeps`
A dataclass of everything the run touches: stores, registry, tunables,
clock, session bounds, settings reader, collector factory, writer factory,
DRC path, output and ceiling. Tests record every call on it.
`cli.default_deps` is the production wiring.
