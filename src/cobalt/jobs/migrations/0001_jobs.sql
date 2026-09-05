-- 0001: jobs — F17's persisted row per scheduled job (Charter §3, L18).
--
-- ONE ROW PER LAUNCHD LABEL, and the label is the join key everywhere:
-- configs/cobalt/jobs.yaml, ops/*.plist, `launchctl list`, and the F18
-- heartbeat all name the same string.
--
-- WHY THE COLUMNS ARE THESE COLUMNS:
--   state/started_at/finished_at/exit_code/last_error  — what happened.
--   heartbeat_at  — the ONLY thing that distinguishes a long job from a
--                   hung one. Without it `running` means "started and did
--                   not finish", which is true of both.
--   expected_cadence — rendered from the schedule in jobs.yaml, so the
--                   MISSED probe reads one place and an operator reading
--                   this table sees when the job should have run.
--   heartbeat_source — `self` | `launchd` | `pidfile`. Cobalt cannot run
--                   a heartbeat thread inside Obsidian or LM Studio, so
--                   the watchdog stamps for them from a real probe. The
--                   column exists so that is VISIBLE rather than implied:
--                   a probe saying "the process exists" and a process
--                   saying "I am working" are different claims.
--   last_result   — the run's own numbers, JSON. The archiver's rows
--                   written land here, which is what makes F18's
--                   "archiver freshness (last run + rows written)"
--                   answerable without a second table.
CREATE TABLE IF NOT EXISTS jobs (
    label TEXT PRIMARY KEY,
    kind TEXT NOT NULL CHECK (kind IN ('resident', 'one-shot')),
    expected_cadence TEXT,
    timeout_s INTEGER NOT NULL CHECK (timeout_s > 0),
    state TEXT NOT NULL DEFAULT 'pending'
        CHECK (state IN ('pending', 'running', 'done', 'failed', 'zombie')),
    heartbeat_source TEXT NOT NULL DEFAULT 'self'
        CHECK (heartbeat_source IN ('self', 'launchd', 'pidfile')),
    started_at TIMESTAMPTZ,
    heartbeat_at TIMESTAMPTZ,
    finished_at TIMESTAMPTZ,
    exit_code INTEGER,
    last_error TEXT,
    last_result JSONB,
    registered_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- The kill switch (F17d). ONE row, id = TRUE, so there is exactly one
-- answer to "is Cobalt stopped" and no way to have two.
CREATE TABLE IF NOT EXISTS kill_switch (
    id BOOLEAN PRIMARY KEY DEFAULT TRUE CHECK (id),
    active BOOLEAN NOT NULL DEFAULT FALSE,
    phrase TEXT,
    set_by TEXT,
    set_at TIMESTAMPTZ,
    cleared_by TEXT,
    cleared_at TIMESTAMPTZ
);

INSERT INTO kill_switch (id, active) VALUES (TRUE, FALSE) ON CONFLICT (id) DO NOTHING;
