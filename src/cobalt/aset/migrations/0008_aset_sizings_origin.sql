-- 0008: aset_sizings.origin — who put the card on the board.
--
-- S1-P3 (CTO review of S1-P2, 2026-09-04). F7's one-click fill is
-- allowed on cards Dejan wrote himself and refused on cards the S2 radar
-- proposed, so the state machine needs to know which is which. It is a
-- property of the CARD (where it came from), not of a transition, so it
-- lives on the card row.
--
-- 'manual' = written by hand on the ASET sheet (every card that exists
-- today, by construction: the radar does not exist until S2).
-- 'radar'  = proposed by the S2 detector. Nothing writes this yet; the
--            column exists now so the shortcut can refuse it by name
--            from the day the radar lands, rather than being retrofitted
--            into a live write path later.
--
-- Backfilled to 'manual' in the same statement that adds the column
-- (DEFAULT applies to existing rows on ALTER), then the default is kept
-- so the sheet's INSERT can stay explicit without every future caller
-- having to remember. NOT NULL is a SEPARATE migration (0009) so
-- `cobalt cards backfill` can create the column before populating it —
-- the S1-P2 lesson, where a NOT NULL applied before its own backfill
-- could run.
ALTER TABLE aset_sizings ADD COLUMN IF NOT EXISTS origin TEXT DEFAULT 'manual';

UPDATE aset_sizings SET origin = 'manual' WHERE origin IS NULL;
