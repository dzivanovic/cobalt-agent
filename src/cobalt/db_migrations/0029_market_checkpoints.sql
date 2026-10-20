-- 0029: system.market_checkpoints — F5 (FINAL §4 Table, [F-04]; card 731 K6):
-- one row per (trade_date, slot) of the four market-context checkpoints, the
-- stored input every delta and narrative replays from (F15 explainability,
-- Charter:173-175). The run upserts it by (trade_date, slot): a re-run of a
-- slot inside its window updates the row in place.
--
-- `base_figures` is a COPY of the figures the delta was computed against, so a
-- later re-run of 07:45 never changes what 08:15 replays (L57, X9).
-- `vault_write_id` points at `"user".vault_writes` with NO foreign key: that
-- table is purged at 30 days (vaultwrite/store.py purge_expired), the rule
-- `vault_writes.sync_revert_of` already follows
-- (vaultwrite/migrations/0004_vault_writes_sync_revert.sql:28-38).
--
-- SYSTEM SIDE (ADR-0008 D2, L32): public market figures, nothing of one
-- trader's, no user_id. Idempotent. Additive: touches no existing object.
CREATE TABLE IF NOT EXISTS system.market_checkpoints (
    id                BIGSERIAL PRIMARY KEY,
    trade_date        DATE        NOT NULL,
    slot              TEXT        NOT NULL,
    figures           JSONB,
    source_status     JSONB,
    base_slot         TEXT,
    base_at           TIMESTAMPTZ,
    base_figures      JSONB,
    delta             JSONB,
    narrative_input   JSONB,
    prompt_sha256     TEXT,
    narrative         JSONB,
    narrative_status  TEXT,
    model_returned    TEXT,
    write_status      TEXT,
    vault_write_id    BIGINT,
    fetched_at        TIMESTAMPTZ,
    created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (trade_date, slot)
);

ALTER TABLE system.market_checkpoints OWNER TO cobalt_system;

-- CARD.md migration checklist item 4 (card 448's apply roles, 0025): DML and
-- sequence USAGE for the system side's apply role — never ownership, never
-- CREATE. The rollback's DROP takes both grants with the table.
GRANT SELECT, INSERT, UPDATE, DELETE ON system.market_checkpoints TO cobalt_apply_system;
GRANT USAGE ON SEQUENCE system.market_checkpoints_id_seq TO cobalt_apply_system;
