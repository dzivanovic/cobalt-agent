-- 0001: cobalt_jobs — F17's persisted row per scheduled job (Charter §3, L18).
--
-- WHY THE `cobalt_` PREFIX, when no other new-core table has one.
-- `cobalt_brain` is the SAME Postgres database Mattermost uses: 129
-- tables, of which 116 are Mattermost's — and one of them is called
-- `jobs`, with 164,320 rows of `expiry_notify` / `delete_expired_posts`
-- work items in it. `CREATE TABLE IF NOT EXISTS jobs` therefore did
-- NOTHING, silently, and the first query failed with `column "label"
-- does not exist` (found 2026-09-04 by the first production dry run —
-- the fail-loud discipline is what surfaced it in seconds rather than
-- in a week of green heartbeats reporting on Mattermost's table).
--
-- `jobs` and `kill_switch` are generic enough that a collision was
-- always going to happen; the existing new-core tables (aset_sizings,
-- vault_writes, card_transitions, day_modes, bars) are specific enough
-- that none has one, and they are NOT renamed here — they hold live
-- trading record and a rename is a migration, not a naming preference.
-- New tables from this prompt take the prefix.
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
CREATE TABLE IF NOT EXISTS cobalt_jobs (
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
CREATE TABLE IF NOT EXISTS cobalt_kill_switch (
    id BOOLEAN PRIMARY KEY DEFAULT TRUE CHECK (id),
    active BOOLEAN NOT NULL DEFAULT FALSE,
    phrase TEXT,
    set_by TEXT,
    set_at TIMESTAMPTZ,
    cleared_by TEXT,
    cleared_at TIMESTAMPTZ
);

INSERT INTO cobalt_kill_switch (id, active) VALUES (TRUE, FALSE) ON CONFLICT (id) DO NOTHING;
