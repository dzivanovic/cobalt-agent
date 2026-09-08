-- 0001: the loaded copies of the vault's trade_def units (ADR-0008 D3).
--
-- WHY THIS LIVES IN A FEATURE MODULE AND NOT IN db_migrations/.
-- `src/cobalt/db_migrations/` holds the DATABASE-WIDE migrations — the
-- schemas, the roles, the grants, the table-to-side moves — because none
-- of those belongs to a feature. These three objects DO belong to one:
-- the taxonomy owns them, `TradeDefStore.ensure_schema()` executes this
-- file the way every other store executes its own, and the suite's
-- store-side lint reads `<module>/migrations/*.sql`. Putting them in the
-- database-wide directory would have been the exception, not the rule.
--
-- THE VAULT IS THE TRUTH; THESE ARE COPIES. `"user".trade_defs` is what
-- the radar, the detector and the DRC join against — a row per validated
-- def, loaded from `1 - Trading/4 - Strategies/<note>.md` by
-- `taxonomy/vault_loader.py`. Nothing writes a def here except that
-- loader, and `TradeDefStore.sync()` DELETES rows whose slug is no longer
-- in the vault: a def deleted from a note is a def gone from the system,
-- not one that lingers in a table nobody reads any more.
--
-- UNQUALIFIED NAMES, ON PURPOSE. The factory pins a user-side connection
-- to `search_path = "user"` and nothing else, so these create in the
-- right schema without naming it — the same way every other module's
-- migrations work. (`user` is reserved; not writing it is also not
-- having to quote it.)
--
-- `user_id` carries the same GUC default as every other user-side table:
-- `current_setting('cobalt.trader_id')::int`, never a literal, so a
-- connection that skipped the factory cannot insert here at all.

CREATE TABLE IF NOT EXISTS trade_defs (
    -- The frontmatter `trade_def:` slug. It IS the id (D3 ruling a), so
    -- it is the primary key: there is no surrogate to disagree with it.
    slug       TEXT PRIMARY KEY,
    -- The frontmatter `name:` (D3 ruling e). Denormalised out of `def`
    -- so a listing does not have to open the JSON.
    name       TEXT NOT NULL,
    -- The validated TradeDef, as the loader built it (id and name
    -- injected). JSONB, not a blob: `setup_trade_matrix` unnests
    -- `valid_setups` straight out of it.
    def        JSONB NOT NULL,
    -- md5 of the unit's YAML text as authored. The change detector — a
    -- reload whose md5 matches wrote the same bytes.
    md5        TEXT NOT NULL,
    -- Vault-relative, so the row means the same thing on any machine.
    note_path  TEXT NOT NULL,
    loaded_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    user_id    INTEGER NOT NULL REFERENCES traders(id)
                   DEFAULT (current_setting('cobalt.trader_id')::int)
);

-- This trader's own per-trade tunable rows, from each note's second
-- unit. Engine rows stay in configs/cobalt/taxonomy/tunables.yaml and are
-- NOT copied here: two homes for the same key is the collision
-- `merge_tunables` refuses.
CREATE TABLE IF NOT EXISTS tunables (
    key        TEXT PRIMARY KEY,
    -- The whole §13.1 row (value, unit, scope, dynamic, status, source,
    -- consumers, replay). Replay writes `status` into the NOTE, and the
    -- next load brings it here — never the other way round.
    row        JSONB NOT NULL,
    -- The def whose note authored it. CASCADE because a per-trade row
    -- without its trade is a key nothing can resolve.
    slug       TEXT NOT NULL REFERENCES trade_defs(slug) ON DELETE CASCADE,
    loaded_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    user_id    INTEGER NOT NULL REFERENCES traders(id)
                   DEFAULT (current_setting('cobalt.trader_id')::int)
);

CREATE INDEX IF NOT EXISTS tunables_slug_idx ON tunables (slug);

-- The setup x trade matrix (D3 ruling b.1). It used to be a SECOND YAML
-- file listing each trade's (setup_ref, relation) rows, which the loader
-- asserted equal to the def's own `valid_setups[]`. The def is the truth
-- now and that file is gone — so the matrix is a VIEW over those rows and
-- CANNOT disagree with them. S2's radar keeps the artifact by
-- name; a duplicate pair is refused by the schema, one level up.
CREATE OR REPLACE VIEW setup_trade_matrix AS
SELECT d.slug                    AS trade_def,
       setup->>'setup_ref'       AS setup_ref,
       setup->>'relation'        AS relation
  FROM trade_defs d,
       LATERAL jsonb_array_elements(d.def -> 'valid_setups') AS setup;

ALTER VIEW setup_trade_matrix OWNER TO cobalt_user;
