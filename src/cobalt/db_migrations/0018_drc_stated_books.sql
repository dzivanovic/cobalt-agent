-- 0018: DRC K1 — the overnight-position lane's book records
-- (DRC-OVERNIGHT-POSITION-v3-2026-09-24 §3, §6 K1; R51, R52). USER side
-- only (L32): his statements and his day's derived rows.
-- Idempotent when applied repeatedly. Written ONLY by `DrcStore` (L40).
--
-- A NEW NUMBERED FILE, never a fold into 0016 (`[F-02]`; X5: an edited
-- 0016 applied over the old one leaves the CHECK unchanged). NUMBER 0018:
-- 0017 is the voice branch's `0017_voice_turns` (left free here); the
-- desk renumbers at the L68 gate if the siblings change.

-- drc_stated_books: his word as an INPUT, beside `drc_imports` — never a
-- `drc_rows` kind, which `record_day` deletes and replaces per day
-- (`[F-01]`). Append-only: a restatement is a NEW row whose `supersedes`
-- names the one it replaces; the current row of a day and kind is the
-- one no other row supersedes. `opening` = the book a day opens with
-- (`[]` = flat); `resolve` = one carried trade_id closed outside the
-- export (`[F-06]`); `no_trade` = the no-trade DRC's input (`[F-05]`).
-- `via` names the caller (R52 (a): `cli` is the `cobalt drc state-book`
-- command); `turn_id` / `readback_sha256` belong to the voice caller only.
CREATE TABLE IF NOT EXISTS "user".drc_stated_books (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id         INTEGER NOT NULL
                        DEFAULT (current_setting('cobalt.trader_id')::int)
                        REFERENCES "user".traders(id),
    day             DATE NOT NULL,
    kind            TEXT NOT NULL CHECK (kind IN ('opening', 'resolve', 'no_trade')),
    positions       JSONB NOT NULL CHECK (jsonb_typeof(positions) = 'array'),
    book_sha256     TEXT NOT NULL CHECK (book_sha256 ~ '^[0-9a-f]{64}$'),
    via             TEXT NOT NULL CHECK (via IN ('drc_page', 'voice_widget', 'cli')),
    turn_id         TEXT,
    readback_sha256 TEXT,
    reason          TEXT NOT NULL,
    supersedes      BIGINT REFERENCES "user".drc_stated_books(id),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    -- a resolve names exactly one trade_id (v3 `:143`)
    CHECK (kind <> 'resolve' OR (jsonb_typeof(positions) = 'array' AND jsonb_array_length(positions) = 1))
);

ALTER TABLE "user".drc_stated_books OWNER TO cobalt_user;
CREATE INDEX IF NOT EXISTS drc_stated_books_day_kind ON "user".drc_stated_books (user_id, day, kind);

DO $migration$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
         WHERE tgname = 'drc_stated_books_append_only'
           AND tgrelid = '"user".drc_stated_books'::regclass
    ) THEN
        CREATE TRIGGER drc_stated_books_append_only
            BEFORE UPDATE OR DELETE ON "user".drc_stated_books
            FOR EACH ROW EXECUTE FUNCTION "user".refuse_row_update();
    END IF;
END
$migration$;

-- drc_rows widened (v3 §3): `seed` = the book a day started from, with
-- its source and hash; `book_close` = the book it left, `count = 0`
-- included, so "flat" is a stored fact. The constraint's name is the one
-- Postgres gave 0016's column CHECK, proven from `pg_constraint` by the
-- suite (`test_drc_k1_store.py`).
ALTER TABLE "user".drc_rows DROP CONSTRAINT IF EXISTS drc_rows_kind_check;
ALTER TABLE "user".drc_rows ADD CONSTRAINT drc_rows_kind_check
    CHECK (kind IN ('trade', 'open_position', 'stats_row', 'day', 'seed', 'book_close'));
