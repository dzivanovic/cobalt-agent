-- 0014: the float handicap's shadow record on membership (FLOAT-HANDICAP-v3
-- §6, H1; his R26 "B": pool-wide). SYSTEM side, like the table. Additive and
-- all nullable, so every row scanned before the deploy stays valid as NULL
-- and nothing is backfilled (L57). No CHECK ([R2F-03]). Idempotent when
-- applied repeatedly.
--
-- raw_rank:        the `_ranked()` index of the scan, no factor applied.
-- handicap_factor: the factor the name would carry (1 when not in the group
--                  or on an inoperative scan, R54); NULL when the block is
--                  absent or the handicap step failed.
-- handicap:        the Pydantic-validated `HandicapRecord` (v3 §6's ten keys).
ALTER TABLE system.radar_membership
  ADD COLUMN IF NOT EXISTS raw_rank        INTEGER,
  ADD COLUMN IF NOT EXISTS handicap_factor NUMERIC(6,4),
  ADD COLUMN IF NOT EXISTS handicap        JSONB;
