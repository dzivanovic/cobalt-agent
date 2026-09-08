-- 0001: "user".trader_settings — the trader's own settings (ADR-0008 D3.4).
--
-- WHAT MOVED IN HERE, AND WHY IT COULD NOT STAY IN CONFIG. The sheet
-- dollars, the enabled grades, the reduced rung, the `.htk` template and
-- the step-down table were `configs/cobalt/aset.yaml` and
-- `configs/cobalt/daymode.yaml`. Every one of them is ONE TRADER'S
-- CHOICE: how much he risks on a B, which grades he takes, what makes
-- today a smaller day. Cobalt is a product for many traders (L32), and a
-- committed file cannot hold a different answer per trader — so these are
-- rows, on the user side, and the repo installs with none of them.
--
-- ONE ROW PER TOP-LEVEL SETTING, keyed by its dotted path
-- (`aset.sheet_modes`, `daymode.stepdowns`, ...). Not one row for the
-- whole blob and not a row per leaf:
--   * per-blob would make every diff read "aset changed" — useless in a
--     `settings load --dry-run` when what you need to know is WHICH knob
--     moved;
--   * per-leaf would split a Pydantic-validated object across rows, and a
--     half-applied update would then be a config that validates nowhere.
-- A top-level setting is exactly the unit that is validated as a whole
-- and ruled as a whole, so it is the unit that is stored and dated as a
-- whole: `source` and `updated_at` are per-setting facts ("the sheet
-- dollars were re-typed from the .htk on the 28th" is different
-- provenance from "the step-down table was ruled on the 4th").
--
-- PK (user_id, key): two traders on one install hold different answers to
-- the same key, which is the entire point of the tenancy split.

CREATE TABLE IF NOT EXISTS trader_settings (
    -- The GUC default, like every other user-side table: a connection
    -- that skipped the factory cannot write a setting for nobody.
    user_id    INTEGER NOT NULL REFERENCES traders(id)
                   DEFAULT (current_setting('cobalt.trader_id')::int),
    -- Dotted path: `aset.sheet_modes`, `aset.enabled_grades`,
    -- `daymode.reduced_sheet`, ... The Pydantic model owns the list.
    key        TEXT NOT NULL,
    -- The setting's whole value, as it appears in the model. JSONB so a
    -- reader can look at it without a Python process.
    value      JSONB NOT NULL,
    -- Where it came from: `yaml:<file>` for a seed, and later `sheet`,
    -- `ruling`, `coach`. A number nobody can source is a number nobody
    -- can re-derive.
    source     TEXT NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (user_id, key)
);
