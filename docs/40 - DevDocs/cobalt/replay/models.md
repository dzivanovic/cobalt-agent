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
  `reason` and `cause` (2026-09-18, chunk FY) are the row's OWN recorded
  words and its structured cause (`evidence->>'cause'`), both optional and
  both carried verbatim — `replay_card` puts them in `gate_detail` for an
  EXPIRED state, where one `excluded_by` value stands for three causes.
- `StopEdit`: one `card_stop_edits` row.
- `CardCandidate`: a card created that ET day whose history never reached
  FILLED, with its transitions and stop edits.
- `PositionSpan`: a FILLED card, open over `[filled_at, closed_at)`.
  `open_at(t)` is false at the exact close instant.
- `WindowResolution`: the public resolver's window end as an aware instant,
  plus its source and detail.
- `CardReplay`: `miss | no_trigger | input_stale`, a reason, and the
  `MissRow` for a miss.

## The shared counterfactual (2026-09-18, chunk E2)
- `Counterfactual`: what `cards.counterfactual()` computed — the searched
  and eligible bars, the trigger bar, the stop in force, the risk unit,
  window and horizon, the walked bars, fill, exit and `cf_r`/`mfe_r`. It
  holds `Bar`s, so `arbitrary_types_allowed` is on.
- `CfOutcome`: `ok | no_trigger | input_stale`, a reason, and the walk.

## Formation side (F12, R1-21)
- `RadarCardRef`: a radar card that already exists for a (member, def,
  direction). Its presence suppresses the formation miss.
- `FormationCandidate`: one S2-P2 `ReplayFormation` in replay's
  vocabulary — `entry`/`stop` take the live card path's own mapping
  (`trigger_price`/`structural_stop`), and `subject_key()` is the
  (member, def slug, direction) triple `aset_sizings_one_open_radar_card`
  enforces.
- `FormationReplay`: `miss | suppressed | no_trigger | input_stale`.
- `FormationCounts`: candidates, misses, suppressed, no_trigger,
  input_stale — every formation the day produced, none silently dropped.
- `FormationOutcome`: the formation step's whole answer — the capability
  marker it bound to (or `unavailable`), its rows and its counts.

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
  archive_incomplete`, `no_trigger`), the formation counts
  (`formation_candidates, formation_misses, formation_suppressed,
  formation_no_trigger, formation_input_stale`, added 2026-09-18),
  `line_diff`, `steps_done`, `failed_step`, `precondition`, and per-kind
  `reconcile` counts.
