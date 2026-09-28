-- 0021: "user".legs + "user".legs_current_v, card_stop_edits.kind, the
-- aset_sizings trade-note / drift columns — S3 exits M1 (S3-EXITS-v3 §3,
-- §4, §5; his R67 and R38; the S-LEGS seam of the C1 build prompt).
--
-- USER side (ADR-0008 D2 / L32): a leg is one trader's fill or exit.
-- user_id NOT NULL + FK + the tenant GUC default, owned by cobalt_user,
-- identity sequence granted — the 0007 tenancy shape.
--
-- ONE TABLE, ENTRY AND EXITS. seq 0 is the entry leg (single fill at MVP,
-- Charter §5 #16), seq 1..n the exits. A correction is a NEW row that
-- names the current row of its seq in `corrects`; the old row is never
-- updated (`refuse_row_update()`, 0007). One ORIGINAL per seq and one
-- original entry per card are partial unique indexes on `corrects IS
-- NULL` — `corrects` is written at INSERT and never changed, so the
-- predicate needs no flag to flip.
--
-- NO running_after, NO direction, NO cobalt_stop (R67 = the Fable seat's
-- N): running = entry-leg shares − Σ current exit shares, computed by ONE
-- store function under the card lock; `running_before` is the count a tap
-- was computed from (a stored input, L57; the entry row stores 0).
-- `direction` and `entry` are read from the card row; Cobalt's stop is the
-- card's `structural_stop`, the gap computed at render.
--
-- held_stated (R67 (1), S-HELD): his "holding X" mid-trade is a correction
-- row of the entry leg — only there may it be set.
--
-- source_import_id carries NO foreign key: the trading-log import table is
-- the DRC lane's and not on main; that lane adds the FK in its own
-- migration.
--
-- IDEMPOTENT (the 0015 / 0017 style): IF NOT EXISTS, guarded trigger,
-- CREATE OR REPLACE for the view.

-- ---------------------------------------------------------------------
-- 1. "user".legs
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS "user".legs (
    id               BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id          INTEGER NOT NULL
                         DEFAULT (current_setting('cobalt.trader_id')::int)
                         REFERENCES "user".traders(id),
    card_id          BIGINT NOT NULL REFERENCES "user".aset_sizings(id),
    seq              SMALLINT NOT NULL,
    kind             TEXT NOT NULL CHECK (kind IN ('entry', 'exit')),
    shares           INTEGER NOT NULL CHECK (shares > 0),
    price            NUMERIC(14, 4) NOT NULL CHECK (price > 0),
    at               TIMESTAMPTZ NOT NULL,
    flag             TEXT NOT NULL CHECK (flag IN ('estimated', 'confirmed')),
    price_source     TEXT NOT NULL CHECK (price_source IN ('last_poll', 'typed', 'dm', 'trading_log')),
    price_asof       TIMESTAMPTZ,
    preset           TEXT CHECK (preset IS NULL OR preset IN ('half', 'third', 'flat', 'typed')),
    running_before   INTEGER NOT NULL CHECK (running_before >= 0),
    stop_in_force    NUMERIC(14, 4) NOT NULL,
    source           TEXT NOT NULL CHECK (source IN ('panel', 'sheet', 'dm', 'trading_log')),
    source_import_id BIGINT,
    held_stated      INTEGER CHECK (held_stated IS NULL OR held_stated >= 0),
    corrects         BIGINT REFERENCES "user".legs(id),
    session          TEXT NOT NULL,
    account_mode     TEXT NOT NULL,
    day_mode_id      DATE REFERENCES "user".day_modes(trade_date),
    attested_sheet   TEXT,
    sheet_mismatch   BOOLEAN,
    CHECK ((source = 'trading_log') = (source_import_id IS NOT NULL)),
    CHECK (held_stated IS NULL OR (kind = 'entry' AND corrects IS NOT NULL)),
    CHECK ((kind = 'entry' AND corrects IS NULL) = (sheet_mismatch IS NOT NULL))
);

ALTER TABLE "user".legs OWNER TO cobalt_user;
GRANT USAGE, SELECT ON SEQUENCE "user".legs_id_seq TO cobalt_user;

CREATE UNIQUE INDEX IF NOT EXISTS legs_one_original_per_seq
    ON "user".legs (card_id, seq) WHERE corrects IS NULL;
CREATE UNIQUE INDEX IF NOT EXISTS legs_one_original_entry
    ON "user".legs (card_id) WHERE kind = 'entry' AND corrects IS NULL;

DO $migration$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
         WHERE tgname = 'legs_append_only'
           AND tgrelid = '"user".legs'::regclass
    ) THEN
        CREATE TRIGGER legs_append_only
            BEFORE UPDATE ON "user".legs
            FOR EACH ROW EXECUTE FUNCTION "user".refuse_row_update();
    END IF;
END
$migration$;

-- ---------------------------------------------------------------------
-- 2. The current row per (card, seq): the greatest id.
-- ---------------------------------------------------------------------
CREATE OR REPLACE VIEW "user".legs_current_v AS
    SELECT DISTINCT ON (l.card_id, l.seq) l.*
      FROM "user".legs AS l
     ORDER BY l.card_id, l.seq, l.id DESC;

ALTER VIEW "user".legs_current_v OWNER TO cobalt_user;

-- ---------------------------------------------------------------------
-- 3. card_stop_edits.kind (R38): a reset is a stop edit of kind 'reset'.
-- ---------------------------------------------------------------------
ALTER TABLE "user".card_stop_edits
    ADD COLUMN IF NOT EXISTS kind TEXT NOT NULL DEFAULT 'edit'
        CONSTRAINT card_stop_edits_kind_check CHECK (kind IN ('edit', 'reset'));

-- ---------------------------------------------------------------------
-- 4. aset_sizings: the trade note's path (C4 writes it) and the drift P in
--    force at the fill + whether it warned (both NULL = not evaluated).
-- ---------------------------------------------------------------------
ALTER TABLE "user".aset_sizings
    ADD COLUMN IF NOT EXISTS trade_note_path TEXT,
    ADD COLUMN IF NOT EXISTS drift_warning_pct NUMERIC(6, 2),
    ADD COLUMN IF NOT EXISTS drift_warned BOOLEAN;
