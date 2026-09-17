-- 0009 rollback. COST: drops every pick row and the whole missed corpus,
-- receipts included. A D1 dump cannot restore rows created after D1 —
-- snapshot both tables first (plan §6 rollback, Astra R1-23).

DROP TABLE IF EXISTS "user".missed;
DROP TABLE IF EXISTS "user".picks;
