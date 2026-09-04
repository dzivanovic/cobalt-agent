-- 0001: the LAW L28 audit trail for every Cobalt write into the vault.
--
-- vault_writes    every touched section, before + after, plus full-file
--                 hashes. 30-day retention, purged by the writer itself
--                 (VaultWriteStore.purge_expired, called on every run).
-- vault_overrides every place a human's text beat Cobalt's. NEVER
--                 purged — an override is a calibration signal about
--                 Dejan's real preferences, not an operational log.
--
-- `section`/`unit` are nullable: a whole-file create (create_if_absent)
-- records one file-level row with both NULL, then one baseline row per
-- unit the rendered template contains.
--
-- before/after hold the touched SECTION (what the law asks to persist,
-- and what `cobalt vault restore` puts back). unit_before/unit_after
-- hold just that unit's BODY — the `base` leg of the next run's
-- three-way merge. Both are needed and they are not the same text: a
-- section carries its markers and any human lines between its units.
CREATE TABLE IF NOT EXISTS vault_writes (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ts TIMESTAMPTZ NOT NULL DEFAULT now(),
    note TEXT NOT NULL,
    section TEXT,
    unit TEXT,
    before TEXT,
    after TEXT,
    unit_before TEXT,
    unit_after TEXT,
    hash_before TEXT,
    hash_after TEXT NOT NULL,
    writer TEXT NOT NULL,
    run_id TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS vault_writes_lookup_idx
    ON vault_writes (note, section, unit, id DESC);
ALTER TABLE vault_writes ADD COLUMN IF NOT EXISTS unit_before TEXT;
ALTER TABLE vault_writes ADD COLUMN IF NOT EXISTS unit_after TEXT;
CREATE INDEX IF NOT EXISTS vault_writes_ts_idx ON vault_writes (ts);

CREATE TABLE IF NOT EXISTS vault_overrides (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ts TIMESTAMPTZ NOT NULL DEFAULT now(),
    note TEXT NOT NULL,
    section TEXT NOT NULL,
    unit TEXT NOT NULL,
    write_id BIGINT,
    cobalt_text TEXT NOT NULL,
    human_text TEXT NOT NULL,
    attempted_text TEXT NOT NULL,
    conflict BOOLEAN NOT NULL,
    writer TEXT NOT NULL,
    run_id TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS vault_overrides_note_idx ON vault_overrides (note, section, unit);
