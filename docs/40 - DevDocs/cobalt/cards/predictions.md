# `src/cobalt/cards/predictions.py`

## What it does
The prediction record's shapes and its ONE writer (F15 P1; FINAL
`F15-PREDICTION-RECORDS-FINAL-2026-09-29.md` §3, `[F-32]`, `[F-33]`,
`[F-40]`; R2-1 (c) B and R2-2 B, his R145). `"user".prediction_records`
(`db_migrations/0022_prediction_records.sql`) holds one append-only row per
grade write on a radar card: `create`, every scan's `refresh`, every dot
`tap`. Records observe `card_score`; nothing here ranks (L7, L52 (b)).

## Key functions/classes
- `RecordInputs` — `{kind, inputs}`, the inputs validated against the ONE
  shape of the kind: `ScanInputs` (`create` / `refresh`:
  `{taps_moved, locked}`, `locked` = `LockedNumbers`
  `{conviction, score_suppressed, proposed_key}` or null) or `TapInputs`
  (`{tap_id, dots: [TapDot], proximity, score_suppressed_before, bands,
  enabled}`). Every model is `extra="forbid"`; every key is required (a
  nullable one included).
- `RecordOutput` — `published_numbers(...)`'s keys + `proposed_key_reason`.
- `PredictionRecord` — every `[F-40]` column but `id` / `user_id`; validates
  `formula_sha256` / `settings_sha256` as 64 lowercase hex and
  `(kind == 'tap') == (run_id is None)`. The seam P2 reads (L72).
- `write_record(conn, *, card_id, kind, at, run_id, scorer_version,
  formula_sha256, settings_sha256, inputs, output) -> int` — the only
  `INSERT INTO prediction_records` in `src/`. Runs on the caller's open
  transaction (never opens, commits or rolls back); validates everything
  before the INSERT; reads `seq = COALESCE(MAX(seq), 0) + 1` and
  `transition_id = max(card_transitions.id)` for the card inside the
  caller's row lock; `why = scoring.grade_why(output)`. Returns the row id.

## Who calls it
`cards/store.py`: `create_radar_card`, `refresh_radar_card`, `tap_dot`
(each inside its `work`, under the card's lock).

## Gotchas
The table is immutable (`BEFORE UPDATE OR DELETE`, R2-2 B), and its card FK
has no `ON DELETE`: a card that carries records cannot be deleted. Clearing
a stray `cobalt_dev` card needs the trigger disabled by the owner — a
desk-approved write, never a test (FINAL `:195`). Tests apply `0022` only
inside the suite's rollback (`tests/cobalt/predictions_db_support.py`).

## 2026-09-30 — f15-p1
Created (card 61 rows W1, H1–H3).

## 2026-10-04 — F15 P2
The read half (card 2026-10-04/02 rows P2-1, P2-2, P2-3; FINAL §5, §6). Pure
reads through `CardReads` (USER side, SELECTs only, no lock, no current
settings, no market data):
- `replay(card_id) -> ReplayReport` — every record by `seq`: a record of
  another `scorer_version` is NOT REPLAYABLE; a `tap` is recomputed from its
  own inputs (`recompute_tap`); a `create` / `refresh` through
  `replay_receipt` on its run's receipt chain (`scan_recompute`; taps-moved
  per `[F-08]` / `[F-44]`), with the receipt's settings for
  `proposed_key_reason`; `ReplayError`, a missing receipt or a receipt with
  no slice of the card → NOT REPLAYABLE with its reason. `output_diff`
  compares as `Decimal` values (X7) and re-derives `why` with `grade_why`.
  The decision grade (`decision_seq`, R2-1 (c) B) and the ROW check (the
  card row vs the last record by `seq`) are derived, never stored. Exit
  0 / 1 / 2 as §5; a manual card and a radar card with no records (the
  audit-export line, `--run` = `system.radar_score.run_id` of its
  `radar_score_id`) exit 2. `ReplayReport.as_json()` is the ONE `[F-44]`
  object; a card with no records has `row = {verdict: null, record_seq:
  null, diff: []}`. A tap's recomputed dots carry the fields its inputs
  hold (no `engine_value`), and the dot compare covers those fields.
- `corpus(since, *, card_id=None) -> list[CorpusRow]` — one row per card
  with records (created on or after `since`, ET), or the one card asked:
  decision / final record, count, state, `legs.realized_r` on
  `legs_current_v` with its provisional flag as returned, the current
  `missed` row (two refuse loud), the `picks` row, `outcome_status` per
  `[F-09]` (`awaiting nightly replay` until a current `missed` row exists).
  `render_corpus` prints n per status first; no EV, no aggregate.
`replay`'s OUTCOME line is `corpus(None, card_id=…)` for its card.
