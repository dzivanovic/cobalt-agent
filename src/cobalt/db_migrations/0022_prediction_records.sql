-- 0022: "user".prediction_records + aset_sizings.last_price_bar_ts — F15 P1
-- (F15-PREDICTION-RECORDS-FINAL-2026-09-29 §3, the `[F-40]` DDL verbatim;
-- his R145: the decision-grade column R2-1 (c) B and the trigger set R2-2 B;
-- R146: the desk settled the DDL text on the Anthropic seat's).
--
-- USER side (ADR-0008 D2 / L32): a record is one trader's card grade.
-- user_id NOT NULL + FK + the tenant GUC default, owned by cobalt_user,
-- identity sequence granted — the 0007 tenancy shape.
--
-- ONE APPEND-ONLY TABLE, ONE WRITER (L3): `cards/predictions.py`
-- `write_record` inserts every row, inside the card-row transaction it
-- describes (`[F-32]`). Order is `seq` per card, never `at` (`[F-33]`).
-- `transition_id` is the card's max(card_transitions.id) read under the
-- row lock (R2-1 (c); no FK). The card FK has NO `ON DELETE` (the legs
-- shape, 0021): a corpus row cannot dangle and a card delete is refused.
--
-- IMMUTABLE (R2-2 B): BEFORE UPDATE OR DELETE calls 0007's
-- "user".refuse_row_update(). A re-score is the next record, a correction
-- a new record; nothing thins the corpus unnoticed. Clearing a stray
-- cobalt_dev card that carries records needs this trigger disabled by the
-- table owner — a desk-approved write, never a test or a step.
--
-- last_price_bar_ts (R2-3, `[F-37]`): the i1 bar START of `last_price`,
-- written beside it in the same COALESCE pair. `db_migrations/cli.py`
-- excludes it from the aset_sizings digest (`[F-38]`).
--
-- IDEMPOTENT (the 0015 / 0017 / 0021 style): IF NOT EXISTS, guarded trigger.

-- ---------------------------------------------------------------------
-- 1. "user".prediction_records
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS "user".prediction_records (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id         INTEGER NOT NULL
                        DEFAULT (current_setting('cobalt.trader_id')::int)
                        REFERENCES "user".traders(id),
    card_id         BIGINT NOT NULL REFERENCES "user".aset_sizings(id),
    seq             INTEGER NOT NULL CHECK (seq >= 1),
    transition_id   BIGINT NOT NULL,
    kind            TEXT NOT NULL CHECK (kind IN ('create', 'refresh', 'tap')),
    at              TIMESTAMPTZ NOT NULL,
    scorer_id       TEXT NOT NULL CHECK (scorer_id IN ('card_grade')),
    scorer_version  TEXT NOT NULL,
    formula_sha256  TEXT NOT NULL,
    settings_sha256 TEXT NOT NULL,
    run_id          BIGINT REFERENCES system.radar_score_run(id),
    inputs          JSONB NOT NULL,
    output          JSONB NOT NULL,
    why             TEXT NOT NULL,
    UNIQUE (card_id, seq),
    CHECK ((kind = 'tap') = (run_id IS NULL))
);

ALTER TABLE "user".prediction_records OWNER TO cobalt_user;
GRANT USAGE, SELECT ON SEQUENCE "user".prediction_records_id_seq TO cobalt_user;

DO $migration$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
         WHERE tgname = 'prediction_records_immutable'
           AND tgrelid = '"user".prediction_records'::regclass
    ) THEN
        CREATE TRIGGER prediction_records_immutable
            BEFORE UPDATE OR DELETE ON "user".prediction_records
            FOR EACH ROW EXECUTE FUNCTION "user".refuse_row_update();
    END IF;
END
$migration$;

-- ---------------------------------------------------------------------
-- 2. aset_sizings.last_price_bar_ts (R2-3)
-- ---------------------------------------------------------------------
ALTER TABLE "user".aset_sizings ADD COLUMN IF NOT EXISTS last_price_bar_ts TIMESTAMPTZ;
