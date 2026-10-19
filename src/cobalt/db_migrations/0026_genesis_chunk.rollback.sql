-- 0026 rollback. COST: drops every imported genesis chunk, so
-- `cobalt genesis search` finds nothing until each source is imported again
-- (`cobalt genesis import <path>...`; the sources themselves are files and are
-- untouched). Snapshot the table first if its rows must survive.
DROP TABLE IF EXISTS "user".genesis_chunk;
