# `src/cobalt/replay/models.py`

Every structured value the nightly replay reads, computes or publishes, as a
Pydantic model. Prices and R stay `Decimal` end to end. A counterfactual R
that passed through a float would not replay to the same four decimals
(L57).

## Constants
- `FORMULA_VERSION = "s2p4.cf_r.1"`: stored in every receipt. A formula
  change is a new version, never a silent recompute.
- `FORMATION_UNAVAILABLE = "unavailable"` and `FORMATION_UNAVAILABLE_LINE =
  "trade_def replay: not available until S2-P2"`: the exact R4 line.
- `ExcludedBy`, `Direction`, `MissKind`, `Side`: literals that mirror the
  CHECK constraints in migrations 0008/0009.

## Errors
- `ReplayError`: the replay refused. The runner attaches `.result` (the
  partial `ReplayResult`) before re-raising, so the job row still records
  what ran.
- `ReplayInputError`: an input is missing, ambiguous or contradictory, for
  example tied transitions with no id, entry equal to stop, or a stop on the
  wrong side of entry.
- `StepFailed(step, error)`: one step failed. The message is `step <name>
  failed — <class>: <msg>`.

## Hashing
`canonical_json` sorts keys, drops whitespace and stringifies Decimals and
datetimes. `sha256_json` hashes that text. Every `inputs_sha256` is
`sha256_json(receipt["inputs"])`.

## Card side (F12)
- `TransitionRow`: one `card_transitions` row. `id` is optional only so the
  hub-cut fixture (which has no ids) can load. `(at, id)` is the order.
- `StopEdit`: one `card_stop_edits` row.
- `CardCandidate`: a card created that ET day whose history never reached
  FILLED, with its transitions and stop edits.
- `PositionSpan`: a FILLED card, open over `[filled_at, closed_at)`.
  `open_at(t)` is false at the exact close instant.
- `WindowResolution`: the public resolver's window end as an aware instant,
  plus its source and detail.
- `CardReplay`: `miss | no_trigger | input_stale`, a reason, and the
  `MissRow` for a miss.

## Mover side (F13)
- `MoverRow`: one ranked export row.
- `MoversExport`: one side's top rows, the sha256 of the raw bytes, the
  header, and `live | retained`.
- `StoredMover`: an active `system.movers_daily` row. `id` is None in a dry
  run.
- `Episode`: a `radar_membership` episode. It ignores extra columns.

## The row and the run
- `MissRow`: one `"user".missed` row before insert. `subject()` returns the
  Python form of the `missed_one_current_per_subject` key: trade_date,
  kind, ticker, card_id or 0, md5 or '', formation_at, and member for
  formations.
- `ReconcileCounts`: `inserted / superseded / retired / unchanged`.
- `ReplayResult`: `job.result`. It carries `movers, archived,
  card_misses, mover_misses, formation_replay, line_action` (STEP-4), the
  R1-12 coverage counts (`input_stale, archive_failures,
  archive_incomplete`, `no_trigger`), `line_diff`, `steps_done`,
  `failed_step`, `precondition`, and per-kind `reconcile` counts.
