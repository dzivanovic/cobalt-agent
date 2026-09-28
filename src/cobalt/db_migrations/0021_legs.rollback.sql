-- 0021 rollback: removes exactly what 0021_legs.sql adds — the view, the
-- table (its indexes, trigger and sequence go with it), card_stop_edits.kind
-- and the three aset_sizings columns. `"user".refuse_row_update()` is 0007's
-- and stays. Destructive by design: every leg row and every recorded drift
-- P goes with its column. Idempotent.
DROP VIEW IF EXISTS "user".legs_current_v;
DROP TABLE IF EXISTS "user".legs;

ALTER TABLE "user".card_stop_edits
    DROP COLUMN IF EXISTS kind;

ALTER TABLE "user".aset_sizings
    DROP COLUMN IF EXISTS trade_note_path,
    DROP COLUMN IF EXISTS drift_warning_pct,
    DROP COLUMN IF EXISTS drift_warned;
