-- 0010: system.archive_progress — the Bar Archiver's OWN watermark, per
-- (ticker, interval). Append-only redesign, FINAL design
-- `docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §4 and §11,
-- derived by the four-house tribunal (L67) from the owner's R14/R15:
-- "i want to know where the watermark is for each ticker and I want to
-- only add the new [bars] in the database that don't exist."
--
-- WHY THIS IS NOT `max(ts)`. `BarStore.watermark()` reads `max(ts)` over
-- `system.bars`, and the RADAR POLLER writes that table too — every 100 s,
-- i1, with a five-bar overlap. So `max(ts)` advances past bars the
-- ARCHIVER never saw, and using it as the archiver's progress loses every
-- bar the vendor adds late (round-2 sequences, `TRIBUNAL-R3.md`). This
-- table is the archiver's own record and nothing else writes it.
--
-- WHAT `archived_through` MEANS, EXACTLY (§4): the `ts` — the bar OPEN, in
-- UTC — of the newest COMPLETE bar of an ACCEPTED export. A BAR
-- timestamp, never a clock time, never a bar-close time, never
-- `fetch_started_at`. It records that the AVAILABLE export was processed
-- through that key; it does not claim the vendor supplied every bar.
-- Monotonic across accepted runs (the writer uses `GREATEST`), frozen on a
-- failed, withheld, empty or regressed target.
--
-- A ROW IS NEVER DELETED — not when a ticker leaves the trader's Lists
-- note. A returning target meets its old `archived_through`, which is what
-- makes the dropped-and-re-added sequence open a `gap` incident (round-2
-- sequence #8) instead of silently skipping the missing days.
--
-- SYSTEM SIDE (L32): market-data bookkeeping, nothing of one trader's
-- choice. `cobalt_user` is granted NOTHING here — a wrong-side query must
-- fail loud, and the user side has no business reading it.
--
-- ADDITIVE. `system.bars` is not touched (columns, PK, indexes are
-- explicitly out of scope, §1 non-goals), and the rollback is a plain
-- `DROP TABLE` of this table alone. IDEMPOTENT: a second
-- `cobalt db migrate` is a no-op.

CREATE TABLE IF NOT EXISTS system.archive_progress (
    -- The key. One row per (ticker, interval) target, for the life of the
    -- install.
    ticker            TEXT        NOT NULL,
    interval          TEXT        NOT NULL,

    -- The watermark itself, and the bounds of the export that set it.
    -- `export_oldest`/`export_newest` are ELIGIBLE-bar bounds (complete
    -- bars only, §7); `raw_export_newest` keeps the unfiltered bound as a
    -- diagnostic and is deliberately NULLABLE — an export whose raw bound
    -- cannot be read must still be able to record progress.
    archived_through  TIMESTAMPTZ NOT NULL,
    export_oldest     TIMESTAMPTZ NOT NULL,
    export_newest     TIMESTAMPTZ NOT NULL,
    raw_export_newest TIMESTAMPTZ,

    -- When the run that set this row started its fetch (V2-3's
    -- completeness instant), when this target was first bootstrapped, and
    -- which run last wrote the row. `run_id` is
    -- `<label or command>@<run started_at, UTC ISO>` (§9): `system.cobalt_jobs`
    -- has one row per LABEL and no per-run id, so the report and this row
    -- share a TEXT rather than a new run table.
    fetch_started_at  TIMESTAMPTZ NOT NULL,
    bootstrap_at      TIMESTAMPTZ NOT NULL,
    run_id            TEXT        NOT NULL,
    updated_at        TIMESTAMPTZ NOT NULL,

    PRIMARY KEY (ticker, interval),

    -- The invariant that makes the watermark auditable: progress can
    -- never be newer than the export it was derived from. If this ever
    -- fires, the writer computed `archived_through` from something other
    -- than the accepted export's newest eligible bar (L1: crash, do not
    -- store a number nobody can replay — L57).
    CONSTRAINT archive_progress_through_within_export
        CHECK (archived_through <= export_newest)
);

ALTER TABLE system.archive_progress OWNER TO cobalt_system;
