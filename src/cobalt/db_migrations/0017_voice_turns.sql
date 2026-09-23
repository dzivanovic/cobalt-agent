-- 0017: "user".voice_turns — voice V1's turn rows (voice v3 FINAL §2, §5,
-- §7, W10). USER side (ADR-0008 D2 / L32): a turn is one trader's words and
-- the command it ran. Carries user_id NOT NULL + FK + the tenant GUC
-- default, owned by cobalt_user, like every user table. Idempotent.
-- Additive: touches no existing object.
--
-- THE ROW IS THE TASK ROW (L18): the FINAL §7 state machine, moved by
-- single-flight UPDATE … WHERE state = ANY(<expected>) RETURNING, reaped,
-- never fire-and-forget. NOT session-gated (FINAL [F-16]): a turn row is
-- the voice module's own state, not trading record.
--
-- NO AUDIO, EVER (R18 (b)): no bytes column of any kind — only the clip's
-- sha256, byte length and duration (dedupe + audit, not a recording). The
-- stored inputs of every executed command are transcript + Plan +
-- resolution + confirm + the expert's write id (L57 as set aside by R18).
-- Rows are kept, no pruning (W10).
--
-- Number 0017 is the desk's (L68): 0012 bars, 0013 setups, 0014 H1,
-- 0015 DRC D1, 0016 reserved for stale-score — all on unmerged branches.
CREATE TABLE IF NOT EXISTS "user".voice_turns (
    id                   BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id              INTEGER NOT NULL
                             DEFAULT (current_setting('cobalt.trader_id')::int)
                             REFERENCES "user".traders(id),
    turn_id              TEXT NOT NULL UNIQUE,
    session_id           TEXT NOT NULL,
    source               TEXT NOT NULL CHECK (source IN ('widget', 'cli', 'test')),
    state                TEXT NOT NULL CHECK (state IN ('received', 'transcribing', 'planned', 'answered', 'awaiting_confirm', 'executing', 'done', 'failed', 'cancelled', 'expired', 'unsupported')),
    input_kind           TEXT NOT NULL CHECK (input_kind IN ('audio', 'text')),
    audio_sha256         TEXT,
    audio_bytes          INTEGER,
    audio_duration_ms    INTEGER,
    audio_deleted_at     TIMESTAMPTZ,
    transcript           TEXT,
    stt_engine           TEXT,
    stt_model            TEXT,
    stt_revision         TEXT,
    stt_ms               INTEGER,
    plan                 JSONB,
    plan_route           TEXT,
    model_returned       TEXT,
    plan_latency_ms      INTEGER,
    plan_usage           JSONB,
    resolution           JSONB,
    reply                TEXT,
    pending_action       JSONB,
    confirm_of           TEXT REFERENCES "user".voice_turns(turn_id),
    expert_write_kind    TEXT,
    expert_write_id      BIGINT,
    failure_class        TEXT,
    failure_detail       TEXT,
    received_at          TIMESTAMPTZ NOT NULL,
    transcribing_at      TIMESTAMPTZ,
    planned_at           TIMESTAMPTZ,
    answered_at          TIMESTAMPTZ,
    awaiting_confirm_at  TIMESTAMPTZ,
    executing_at         TIMESTAMPTZ,
    done_at              TIMESTAMPTZ,
    failed_at            TIMESTAMPTZ,
    cancelled_at         TIMESTAMPTZ,
    expired_at           TIMESTAMPTZ,
    unsupported_at       TIMESTAMPTZ,
    updated_at           TIMESTAMPTZ NOT NULL,
    CHECK (audio_bytes IS NULL OR audio_bytes > 0),
    CHECK (input_kind = 'audio' OR audio_sha256 IS NULL),
    CHECK ((expert_write_kind IS NULL) = (expert_write_id IS NULL))
);

ALTER TABLE "user".voice_turns OWNER TO cobalt_user;
CREATE INDEX IF NOT EXISTS voice_turns_session ON "user".voice_turns (session_id, received_at);
CREATE INDEX IF NOT EXISTS voice_turns_live ON "user".voice_turns (state)
    WHERE state IN ('received', 'transcribing', 'planned', 'awaiting_confirm', 'executing');
