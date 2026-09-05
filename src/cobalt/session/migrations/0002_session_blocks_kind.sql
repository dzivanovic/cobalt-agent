-- 0002: session_blocks.kind — RULED 2026-09-04 (S1-P3, decided-with-veto).
--
-- MIGRATION AND REPAIR TOOLING STAYS UNGATED inside the market_reset
-- hard block. The reasoning is the one already written into
-- `VaultWriter.restore` and `CardStore.backfill`: locking recovery out
-- for 20:00-21:00 would mean the one hour you most need to repair state
-- is the hour you cannot. Card CREATION stays refused; that is trading
-- record and the block exists for it.
--
-- The price of the carve-out is that it can never happen QUIETLY. Every
-- ungated run inside the window logs one loud line AND lands here, in
-- the same counter F18 displays — so "how many writes happened inside
-- the block tonight" has one answer covering both the writes that were
-- REFUSED and the ones that were let through by name.
--
-- 'refused'     — the guard turned a write away (every row before this).
-- 'ungated_run' — migration/repair tooling ran inside the window under
--                 its carve-out, and said so.
ALTER TABLE session_blocks ADD COLUMN IF NOT EXISTS kind TEXT NOT NULL DEFAULT 'refused';

ALTER TABLE session_blocks DROP CONSTRAINT IF EXISTS session_blocks_kind_check;

ALTER TABLE session_blocks ADD CONSTRAINT session_blocks_kind_check
    CHECK (kind IN ('refused', 'ungated_run'));
