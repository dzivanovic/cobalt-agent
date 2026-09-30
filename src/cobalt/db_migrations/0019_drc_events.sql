-- 0019: DRC D2 fix r1 — ONE home for the `DrcInputsPlaced` event state,
-- both day types (DRC-D2-SEAM-2026-09-25 §1, option (B); cto-2026-09-25
-- R64 (1)). USER side only (L32): one trader's own runs.
-- Idempotent when applied repeatedly. Written ONLY by `DrcStore` (L40).
--
-- WHY: the file-less no-trade day's event had no row to carry L18's
-- state (X-NT): the event lived on the trading-log import row
-- (`0016_drc.sql:35`–`:37`, `:42`), and a no-trade day with no file has
-- none. One `drc_events` row per SOURCE — the day's current trading-log
-- import, or its current `drc_stated_books` `no_trade` statement (v3
-- `[F-05]`) — holds pending → running → done | failed for both. The
-- columns on `drc_imports` are dropped (never shipped: `0016` is absent
-- from `cobalt_dev` and production), so the state has ONE home (L3).
--
-- A NEW NUMBERED FILE, never a fold into 0016 (v3 `[F-02]`). NUMBER 0019:
-- the desk's (R64 (5)); DRC D3's `drc_build_kinds` is 0020.

-- drc_events: one row per source row. `failed` names its reason; `done`
-- names the note path the build returned (the seam's ESCALATE 11). Not a
-- `drc_rows` kind, so a re-pair never deletes it (`_commit`).
CREATE TABLE IF NOT EXISTS "user".drc_events (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id         INTEGER NOT NULL DEFAULT (current_setting('cobalt.trader_id')::int)
                        REFERENCES "user".traders(id),
    day             DATE NOT NULL,
    source          TEXT NOT NULL CHECK (source IN ('import', 'stated_book')),
    import_id       BIGINT REFERENCES "user".drc_imports(id),
    stated_book_id  BIGINT REFERENCES "user".drc_stated_books(id),
    state           TEXT NOT NULL CHECK (state IN ('pending', 'running', 'done', 'failed')),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    error           TEXT,
    note_path       TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK ((source = 'import') = (import_id IS NOT NULL)),
    CHECK ((source = 'stated_book') = (stated_book_id IS NOT NULL)),
    CHECK ((state = 'failed') = (coalesce(error, '') <> '')),
    CHECK ((state = 'done') = (note_path IS NOT NULL)),
    UNIQUE (user_id, import_id),
    UNIQUE (user_id, stated_book_id)
);
ALTER TABLE "user".drc_events OWNER TO cobalt_user;
CREATE INDEX IF NOT EXISTS drc_events_day ON "user".drc_events (user_id, day);
-- the retired home (never shipped): the multi-column CHECK (0016:42) goes with its columns
ALTER TABLE "user".drc_imports DROP COLUMN IF EXISTS event_state,
                               DROP COLUMN IF EXISTS event_updated_at,
                               DROP COLUMN IF EXISTS event_error;
