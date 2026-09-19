-- 0011: system.archive_incidents — what the append-only night REFUSED to
-- do, and why, kept until a person resolves it. FINAL design
-- `docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §6, §7, §11.
--
-- THE FIVE KINDS (§11 — `regression` is v3's addition to v2's four):
--
--   gap           progress exists and the export's oldest eligible bar is
--                 NEWER than `archived_through` — the window between them
--                 is "unavailable from the tested export interface", not
--                 proven missing. The usable range is still appended; the
--                 target is DEGRADED.
--   restated      a key present in BOTH storage and the download differs
--                 in any of O/H/L/C/V after normalisation. NOTHING is
--                 inserted for that target tonight, nothing stored is
--                 touched, progress is unchanged, the target counts
--                 FAILED. There is no automatic repair, by constant
--                 factor or otherwise — the remedy is
--                 `cobalt archiver restate`, previewed, then `--apply`
--                 inside a quiet window (§8).
--   stored_only   a key in storage that the download does not carry.
--                 FLAGGED, never deleted.
--   empty_export  the export had no rows, or rows but no eligible
--                 COMPLETE bar. Progress unchanged, target FAILED.
--   regression    `export_newest < archived_through`, strictly. EQUAL is
--                 fine: an illiquid name whose newest bar has not moved
--                 succeeds with zero inserts, and a half-day's newest bar
--                 is newer than last night's. Only an ACCEPTED export
--                 ever updates the baseline.
--
-- ONE UNRESOLVED ROW PER (kind, ticker, interval, range_start), enforced
-- by a PARTIAL unique index `WHERE resolved_at IS NULL`. A recurring
-- night refreshes `last_seen_at`; it never duplicates. Once a row is
-- resolved the index no longer covers it, so the same condition can open
-- again and the history of both is kept.
--
-- THE HEARTBEAT READS THIS TABLE. `cobalt.heartbeat.probes.archiver_freshness`
-- is not green while any row is unresolved (§11, O-7) — that is the alarm
-- behind Known limit 3 (a withheld target whose new bars age out of the
-- vendor window if nobody repairs it).
--
-- Resolution is EXPLICIT and audited on the row (`resolved_by`, and the
-- operator's `--reason` in `detail`): nothing resolves itself, and a
-- `restate --apply` leaves its audit trail here (spec O-4).
--
-- SYSTEM SIDE (L32). `cobalt_user` is granted NOTHING. ADDITIVE and
-- IDEMPOTENT; the rollback drops this table alone.

CREATE TABLE IF NOT EXISTS system.archive_incidents (
    id            BIGSERIAL   PRIMARY KEY,

    kind          TEXT        NOT NULL CHECK (kind IN (
                      'gap', 'restated', 'stored_only', 'empty_export', 'regression')),
    ticker        TEXT        NOT NULL,
    interval      TEXT        NOT NULL,

    -- The affected span of BAR timestamps, when the kind has one. A
    -- `gap` carries (archived_through, export_oldest); an `empty_export`
    -- has no span at all, so both are NULLABLE.
    range_start   TIMESTAMPTZ,
    range_end     TIMESTAMPTZ,

    first_seen_at TIMESTAMPTZ NOT NULL,
    last_seen_at  TIMESTAMPTZ NOT NULL,

    -- The evidence, closed payload, validated by the writer before it
    -- gets here: observed bounds, the differing keys and which of
    -- O/H/L/C/V differed with both values after normalisation, the
    -- session dates involved, the operator's --reason on a repair. The
    -- database only insists it is an object (L57: the stored inputs
    -- behind every number).
    detail        JSONB       NOT NULL CHECK (jsonb_typeof(detail) = 'object'),

    resolved_at   TIMESTAMPTZ,
    resolved_by   TEXT,

    run_id        TEXT        NOT NULL
);

ALTER TABLE system.archive_incidents OWNER TO cobalt_system;

-- ONE open row per condition. PARTIAL, on purpose: resolved rows are
-- history and must not block the same condition recurring later.
--
-- `NULLS NOT DISTINCT` (Postgres 15+; this install is pg16) is
-- load-bearing, not tidiness: an `empty_export` incident has no span, so
-- its `range_start` is NULL, and under the DEFAULT rule every NULL is
-- distinct from every other — a target failing empty for a month would
-- open thirty rows for one condition and the heartbeat's "oldest kind"
-- detail would be meaningless.
CREATE UNIQUE INDEX IF NOT EXISTS archive_incidents_one_open
    ON system.archive_incidents (kind, ticker, interval, range_start)
    NULLS NOT DISTINCT
    WHERE resolved_at IS NULL;

CREATE INDEX IF NOT EXISTS archive_incidents_unresolved
    ON system.archive_incidents (resolved_at, kind, first_seen_at)
    WHERE resolved_at IS NULL;

-- Granted explicitly rather than assumed from 0001's default privileges
-- (0006's pattern, Astra R1-2). NOTHING is granted to `cobalt_user`.
GRANT USAGE, SELECT ON SEQUENCE system.archive_incidents_id_seq TO cobalt_system;

-- And "NOTHING" is now enforced rather than assumed (`cto-2026-09-19.md`
-- §4 R25 "B", from the DB run's finding DB-1). `0001_schemas.sql:124`
-- grants SELECT on ALL tables in schema `system` to `cobalt_user` and
-- `:149-151` makes it a DEFAULT PRIVILEGE for every table created later;
-- `:125` and `:152-154` do the same for SEQUENCES. `id BIGSERIAL` above
-- creates `archive_incidents_id_seq` as part of the CREATE TABLE, so the
-- sequence inherits that default read exactly as the table does — the
-- comment two lines up was true of neither until these two statements.
--
-- REVOKE ALL rather than REVOKE SELECT: §11's word is "nothing". Both
-- statements are no-ops on a database where they already applied (a
-- REVOKE of a privilege not held does not error), so the file stays
-- idempotent.
--
-- DELIBERATE DIVERGENCE from `0006_radar_score.sql:198-200`, which grants
-- `cobalt_user` explicit read on the radar tables because those feed
-- ASET sizing user-side. Incidents are the archiver's own bookkeeping
-- (L32) — opposite tenancy answer, not an inconsistency to fix.
REVOKE ALL ON system.archive_incidents FROM cobalt_user;
REVOKE ALL ON SEQUENCE system.archive_incidents_id_seq FROM cobalt_user;
