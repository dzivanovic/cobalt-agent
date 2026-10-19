-- 0001: "user".cobalt_cos_sessions + "user".cobalt_cos_turns (F20 FINAL §2 `cos/store.py`, §5; F-20; L18).
--
-- USER SIDE: his conversation with the chief of staff (L32; card 730
-- DECISION 4, the `voice_turns` precedent). Created by
-- `CosStore.ensure_schema`, directly on its side.
--
-- ONE TURN ROW PER DM, inserted `pending` BEFORE the session is called, then
-- `running` -> `done` | `failed` (L18). `message_ref` is the Mattermost post
-- id and is UNIQUE: a post is never answered twice (F-20, T11).
--
-- A turn fails on `is_error` or `terminal_reason`, never on the vendor
-- `result_subtype` alone (spike D5); the subtype is recorded, not trusted.

CREATE TABLE IF NOT EXISTS cobalt_cos_sessions (
    id          BIGSERIAL PRIMARY KEY,
    user_id     INTEGER NOT NULL REFERENCES traders(id)
                    DEFAULT (current_setting('cobalt.trader_id')::int),
    channel     TEXT NOT NULL,
    agent_id    TEXT NOT NULL,
    session_id  TEXT NOT NULL,
    started_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    rotated_at  TIMESTAMPTZ,
    state       TEXT NOT NULL CHECK (state IN ('active', 'rotated', 'failed'))
);

CREATE INDEX IF NOT EXISTS cobalt_cos_sessions_current ON cobalt_cos_sessions (channel, agent_id, id);

CREATE TABLE IF NOT EXISTS cobalt_cos_turns (
    id               BIGSERIAL PRIMARY KEY,
    user_id          INTEGER NOT NULL REFERENCES traders(id)
                         DEFAULT (current_setting('cobalt.trader_id')::int),
    message_ref      TEXT NOT NULL UNIQUE,
    state            TEXT NOT NULL DEFAULT 'pending'
                         CHECK (state IN ('pending', 'running', 'done', 'failed')),
    created_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
    started_at       TIMESTAMPTZ,
    finished_at      TIMESTAMPTZ,
    num_turns        INTEGER,
    result_subtype   TEXT,
    is_error         BOOLEAN,
    terminal_reason  TEXT,
    error            TEXT
);
