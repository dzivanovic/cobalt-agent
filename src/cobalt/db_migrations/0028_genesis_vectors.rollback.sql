-- 0028 rollback. COST: drops every stored genesis vector, its model and its
-- dimension; the chunks and their FTS stay, so `cobalt genesis search` is
-- unchanged and a later `cobalt genesis embed` (after 0028 again) re-embeds
-- every chunk. Snapshot the three columns first if they must survive.
-- The `vector` EXTENSION IS NOT DROPPED: on cobalt_brain the old tree's
-- 1536-dim tables use the type (FINAL: "the four 1536-dim tables are
-- untouched"), and DROP EXTENSION would take them with it.
ALTER TABLE IF EXISTS "user".genesis_chunk DROP CONSTRAINT IF EXISTS genesis_chunk_embedding_stamped;
ALTER TABLE IF EXISTS "user".genesis_chunk DROP COLUMN IF EXISTS embedding;
ALTER TABLE IF EXISTS "user".genesis_chunk DROP COLUMN IF EXISTS embed_model;
ALTER TABLE IF EXISTS "user".genesis_chunk DROP COLUMN IF EXISTS embed_dim;
