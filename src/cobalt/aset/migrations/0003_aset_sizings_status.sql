-- 0003: card lifecycle status + the actual-fill columns (2026-09-03).
--
-- WHY: the fill-recompute was note-only. The 09-03 forensics found the
-- 10:02:36 TSLA FILL UPDATE had NO DB ROW AT ALL, so Postgres could not
-- answer "which cards became trades" and any note rebuild from the DB
-- would have silently dropped it. The recompute now UPDATEs the card row
-- it belongs to: status FILLED plus the actual-fill figures.
--
-- status is deliberately minimal — 'CARD' (a written plan) and 'FILLED'
-- (a taken trade). The full lifecycle ruled on 09-02 (WATCH / ARMED /
-- TRIGGERED / FILLED / CLOSED / PASSED / EXPIRED) is OUT OF SCOPE here;
-- the sheet is beta and only these two are observable from it today.
-- Historical rows take 'CARD': they are written plans, and whether they
-- were taken is exactly what the DRC's card-reconcile block asks Dejan.
ALTER TABLE aset_sizings ADD COLUMN IF NOT EXISTS status TEXT NOT NULL DEFAULT 'CARD';
ALTER TABLE aset_sizings ADD COLUMN IF NOT EXISTS filled_at TIMESTAMPTZ;
ALTER TABLE aset_sizings ADD COLUMN IF NOT EXISTS actual_fill NUMERIC(14, 4);
ALTER TABLE aset_sizings ADD COLUMN IF NOT EXISTS recomputed_shares INTEGER;
ALTER TABLE aset_sizings ADD COLUMN IF NOT EXISTS recomputed_used_risk NUMERIC(14, 2);
ALTER TABLE aset_sizings ADD COLUMN IF NOT EXISTS share_delta INTEGER;
ALTER TABLE aset_sizings ADD COLUMN IF NOT EXISTS distance_change_pct NUMERIC(14, 4);
