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
