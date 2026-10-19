-- 0026: "user".genesis_chunk — F21 chunk 1, the FTS floor (F21 FINAL F-01,
-- F-02, F-15; card 2026-10-13 468 G1): one row per structural chunk of one
-- imported markdown source, with its 1-based inclusive line range and the
-- source file's sha256. `tsv` is generated from `body`; the one recall entry
-- (`cobalt.genesis.search`) ranks it with ts_rank_cd. No vector column: that
-- is chunk 2's own migration.
-- USER side (ADR-0008 D2 / L32): one trader's ledger and vault history.
-- user_id NOT NULL + FK + the tenant GUC default, owned by cobalt_user, like
-- every user table. Idempotent. Additive: touches no existing object.
--
-- A re-import of one source deletes that (user_id, source)'s rows and writes
-- the new ones in ONE transaction (genesis/store.py GenesisStore.replace).
CREATE TABLE IF NOT EXISTS "user".genesis_chunk (
    id               BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id          INTEGER NOT NULL
                         DEFAULT (current_setting('cobalt.trader_id')::int)
                         REFERENCES "user".traders(id),
    source           TEXT NOT NULL,
    source_sha256    TEXT NOT NULL,
    seq              INTEGER NOT NULL,
    line_start       INTEGER NOT NULL,
    line_end         INTEGER NOT NULL,
    body             TEXT NOT NULL CHECK (body <> ''),
    tsv              tsvector GENERATED ALWAYS AS (to_tsvector('english', body)) STORED,
    imported_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (user_id, source, seq)
);

ALTER TABLE "user".genesis_chunk OWNER TO cobalt_user;
CREATE INDEX IF NOT EXISTS genesis_chunk_tsv ON "user".genesis_chunk USING gin (tsv);
