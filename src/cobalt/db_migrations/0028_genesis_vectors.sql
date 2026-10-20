-- 0028: genesis_chunk's vector column — F21 chunk 2 (F21 FINAL F-02, X6, X10;
-- card 2026-10-13 469 V4). `embedding vector(768)` carries its dimension in
-- the DDL (768 = the `local.embed` route's `dim`, X2 / X8); the genesis store
-- reads it back from pg_attribute.atttypmod at load and crashes when it is not
-- the route's `dim`, before any write (L1). Every embedded row records the
-- model as returned by the server and the dimension; the CHECK keeps the three
-- NULL together or set together, so no row is half-stamped. A NULL vector is a
-- chunk not yet embedded (or whose embed failed): its FTS body still serves.
--
-- `vector` is created here, first, by the migration harness's bootstrap role
-- (`db.connect_migration`, search_path `public`): X6 found cobalt_dev with
-- `plpgsql` only and `vector` 0.8.1 available, and `cobalt_user` cannot create
-- it. The extension lands in `public`; the user side never names the type (it
-- writes a text literal into a typed column).
-- Idempotent. Additive: three nullable columns and one CHECK on one table.
CREATE EXTENSION IF NOT EXISTS vector;

ALTER TABLE "user".genesis_chunk ADD COLUMN IF NOT EXISTS embedding vector(768);
ALTER TABLE "user".genesis_chunk ADD COLUMN IF NOT EXISTS embed_model TEXT;
ALTER TABLE "user".genesis_chunk ADD COLUMN IF NOT EXISTS embed_dim INTEGER;

ALTER TABLE "user".genesis_chunk DROP CONSTRAINT IF EXISTS genesis_chunk_embedding_stamped;
ALTER TABLE "user".genesis_chunk ADD CONSTRAINT genesis_chunk_embedding_stamped
    CHECK ((embedding IS NULL) = (embed_model IS NULL) AND (embedding IS NULL) = (embed_dim IS NULL));
