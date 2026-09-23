-- 0016: DRC D1 — his two daily files, imported, parsed and paired
-- (DRC-AUTOMATION-v2-2026-09-22 §9 D1, [F-35]). USER side only (L32):
-- every row is one trader's own record. Three tables, no fourth (v2 §3):
-- the input event's state lives on the import row. It creates neither the
-- declared-but-unbuilt `fills` nor anything of the old tree's.
-- Idempotent when applied repeatedly. Written ONLY by `DrcStore` (L40).
--
-- NUMBER 0016: 0012 = bars chunk-2 (unmerged), 0013 = setups, 0014 =
-- handicap H1 (reserved), 0015 = stale score (reserved, conditional);
-- `reports/devdb-builds-reissue-2026-09-23.md`. The desk renumbers at
-- the L68 gate if the siblings change.

-- drc_imports: one row per dropped file (trading log, stats log or a
-- screenshot bound to a trade key). `reason` is empty on a clean parse,
-- the loud `PARTIAL — missing: <columns>` text on a partial one
-- (R17 (5)), and the failure with its line on a failed one (L1).
-- `supersedes` points at the newer file's predecessor of the same day
-- and kind; nothing is ever overwritten. `event_state` is D2's
-- `DrcInputsPlaced` state (L18: pending → running → done | failed).
CREATE TABLE IF NOT EXISTS "user".drc_imports (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id         INTEGER NOT NULL
                        DEFAULT (current_setting('cobalt.trader_id')::int)
                        REFERENCES "user".traders(id),
    import_date     DATE NOT NULL,
    kind            TEXT NOT NULL CHECK (kind IN ('trading_log', 'stats_log', 'screenshot')),
    name            TEXT NOT NULL,
    sha256          TEXT NOT NULL CHECK (sha256 ~ '^[0-9a-f]{64}$'),
    trade_key       TEXT,
    parse_status    TEXT NOT NULL CHECK (parse_status IN ('parsed', 'partial', 'failed')),
    reason          TEXT NOT NULL DEFAULT '',
    failed_line     INTEGER,
    degraded        TEXT,
    supersedes      BIGINT REFERENCES "user".drc_imports(id),
    event_state     TEXT CHECK (event_state IN ('pending', 'running', 'done', 'failed')),
    event_updated_at TIMESTAMPTZ,
    event_error     TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (kind <> 'screenshot' OR trade_key IS NOT NULL),
    CHECK (parse_status <> 'partial' OR reason LIKE 'PARTIAL%'),
    CHECK (parse_status <> 'failed' OR reason <> ''),
    CHECK (event_state IS NULL OR event_updated_at IS NOT NULL)
);

ALTER TABLE "user".drc_imports OWNER TO cobalt_user;
CREATE INDEX IF NOT EXISTS drc_imports_day_kind ON "user".drc_imports (user_id, import_date, kind);

-- drc_fills: one row per trading-log execution (the parse's inputs, L57).
-- Every column but the line is nullable: a `partial` file stores what it
-- has and nothing else (R17 (5)). The execution's date is the import
-- date (R17 (3)); the account is stored, never a gate (R94).
CREATE TABLE IF NOT EXISTS "user".drc_fills (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id         INTEGER NOT NULL
                        DEFAULT (current_setting('cobalt.trader_id')::int)
                        REFERENCES "user".traders(id),
    import_id       BIGINT NOT NULL REFERENCES "user".drc_imports(id),
    line            INTEGER NOT NULL CHECK (line >= 2),
    executed_at     TIMESTAMPTZ,
    symbol          TEXT,
    side            TEXT CHECK (side IN ('B', 'S', 'SS')),
    price           NUMERIC CHECK (price > 0),
    qty             INTEGER CHECK (qty > 0),
    route           TEXT,
    broker          TEXT,
    account         TEXT,
    order_type      TEXT,
    order_id        TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (import_id, line)
);

ALTER TABLE "user".drc_fills OWNER TO cobalt_user;

-- drc_rows: the declared table (placement.py), now built. One row per
-- trade, per open position (R67 — the next day's seed), per stats row
-- (matched or `unmatched`, shown) and one per day. Every derived value
-- is stored WITH its inputs and the function version that made it
-- (L57). `ref` names the subject: a trade_id, `line <n>`, or `day`.
CREATE TABLE IF NOT EXISTS "user".drc_rows (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id         INTEGER NOT NULL
                        DEFAULT (current_setting('cobalt.trader_id')::int)
                        REFERENCES "user".traders(id),
    day             DATE NOT NULL,
    kind            TEXT NOT NULL CHECK (kind IN ('trade', 'open_position', 'stats_row', 'day')),
    ref             TEXT NOT NULL,
    inputs          JSONB NOT NULL CHECK (jsonb_typeof(inputs) = 'object'),
    derived         JSONB NOT NULL CHECK (jsonb_typeof(derived) = 'object'),
    fn_version      TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

ALTER TABLE "user".drc_rows OWNER TO cobalt_user;
CREATE UNIQUE INDEX IF NOT EXISTS drc_rows_one_per_subject ON "user".drc_rows (user_id, day, kind, ref);
