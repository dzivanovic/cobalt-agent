-- 0009: F3 picks and the F12/F13 missed corpus. S2-P4 STEP-1 (R2, R4, R5).
-- USER side only (ADR-0008 D2): a pick and a miss are one trader's record.
-- Both tables carry user_id NOT NULL + FK + the tenant GUC default, owned
-- by cobalt_user. Idempotent when applied repeatedly. Nothing here depends
-- on S2-P2's 0006/0007, so either merge order applies.

-- picks: one row per card that reached FILLED, written inside the
-- CardStore.fill transaction under SAVEPOINT pick (R2). It snapshots the
-- pool rank/metric/value and the card-score rank AT PICK TIME, with the
-- inputs that replay both ranks (L57, Astra R1-6):
--   pool_basis   'pool' | 'unavailable: <reason>' — why a pool field is null
--   score_basis  'card_score' | 'unavailable: <reason>'
--   score_inputs the ordered cohort and tie policy the rank came from
CREATE TABLE IF NOT EXISTS "user".picks (
    id                   BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id              INTEGER NOT NULL
                             DEFAULT (current_setting('cobalt.trader_id')::int)
                             REFERENCES "user".traders(id),
    card_id              BIGINT NOT NULL UNIQUE REFERENCES "user".aset_sizings(id),
    transition_id        BIGINT NOT NULL REFERENCES "user".card_transitions(id),
    ticker               TEXT NOT NULL,
    picked_at            TIMESTAMPTZ NOT NULL,
    session              TEXT NOT NULL,
    origin               TEXT NOT NULL,
    account_mode         TEXT,
    pool_member_id       BIGINT REFERENCES system.radar_membership(id),
    not_in_pool          BOOLEAN NOT NULL,
    pool_basis           TEXT NOT NULL,
    pool_rank            INTEGER,
    pool_size            INTEGER,
    rank_metric          TEXT,
    rank_value           NUMERIC(20,6),
    pool_scan_id         BIGINT,
    pool_scan_at         TIMESTAMPTZ,
    card_score           INTEGER,
    card_score_rank      INTEGER,
    focus_top4           BOOLEAN,
    score_basis          TEXT NOT NULL,
    score_inputs         JSONB NOT NULL,
    created_at           TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (not_in_pool = (pool_member_id IS NULL))
);

ALTER TABLE "user".picks OWNER TO cobalt_user;
CREATE INDEX IF NOT EXISTS picks_picked_at ON "user".picks (picked_at);

-- missed: every miss the nightly replay finds, with the gate that excluded
-- it and, for cards/formations, one counterfactual R.
--
-- IMMUTABLE RECEIPT (Astra R1-8). system.bars is mutable and a hash cannot
-- recover a source that has since changed, so `receipt` retains the actual
-- consumed bars, entry/stop as evaluated, the window and horizon, the state
-- history behind each gate and the benchmark/settings inputs;
-- `inputs_sha256` hashes it. `replay_run_id` is the receipt-owned run
-- identity (never cobalt_jobs' per-label id, which each run overwrites).
--
-- VERSIONED, NEVER OVERWRITTEN (Astra R2-1, corrected R3-1). A rerun that
-- recomputes a subject runs, in one USER transaction: (1) UPDATE the prior
-- row is_current = false, retired_by_run_id = <run> — freeing the partial
-- unique slot; (2) INSERT the replacement; (3) UPDATE the prior row's
-- superseded_by = <new id>. A subject whose miss disappears stops at (1).
CREATE TABLE IF NOT EXISTS "user".missed (
    id                   BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id              INTEGER NOT NULL
                             DEFAULT (current_setting('cobalt.trader_id')::int)
                             REFERENCES "user".traders(id),
    trade_date           DATE NOT NULL,
    kind                 TEXT NOT NULL CHECK (kind IN ('card','formation','mover')),
    ticker               TEXT NOT NULL,
    direction            TEXT CHECK (direction IN ('long','short')),
    card_id              BIGINT REFERENCES "user".aset_sizings(id),
    trade_def_md5        TEXT,
    formation_at         TIMESTAMPTZ,
    pool_member_id       BIGINT REFERENCES system.radar_membership(id),
    mover_id             BIGINT REFERENCES system.movers_daily(id),
    excluded_by          TEXT NOT NULL CHECK (excluded_by IN (
                             'unarmed','passed','not_filled','no_card','window','rule_10',
                             'not_in_any_source','config_cap','not_equity',
                             'screen_inactive','manual')),
    gate_detail          JSONB NOT NULL,
    entry                NUMERIC(14,4),
    stop                 NUMERIC(14,4),
    trigger_ts           TIMESTAMPTZ,
    fill_price           NUMERIC(14,4),
    horizon_end          TIMESTAMPTZ,
    exit_ts              TIMESTAMPTZ,
    exit_price           NUMERIC(14,4),
    exit_reason          TEXT CHECK (exit_reason IN ('stop','horizon_end')),
    cf_r                 NUMERIC(10,4),
    mfe_r                NUMERIC(10,4),
    bars_watermark       TIMESTAMPTZ,
    formula_version      TEXT,
    receipt              JSONB NOT NULL,
    inputs_sha256        TEXT NOT NULL,
    replay_run_id        TEXT NOT NULL,
    run_seq              INTEGER NOT NULL DEFAULT 1,
    is_current           BOOLEAN NOT NULL DEFAULT true,
    superseded_by        BIGINT REFERENCES "user".missed(id),
    retired_by_run_id    TEXT,
    created_at           TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (kind <> 'card' OR (card_id IS NOT NULL AND entry IS NOT NULL AND stop IS NOT NULL)),
    CHECK (kind <> 'mover' OR mover_id IS NOT NULL),
    CHECK (kind <> 'formation' OR (trade_def_md5 IS NOT NULL AND formation_at IS NOT NULL
                                   AND pool_member_id IS NOT NULL)),
    CHECK (is_current OR retired_by_run_id IS NOT NULL),
    CHECK (superseded_by IS NULL OR NOT is_current)
);

ALTER TABLE "user".missed OWNER TO cobalt_user;

-- One CURRENT row per subject. A formation's subject includes its trigger
-- time and member (Astra R1-21) so two same-day formations of one
-- (ticker, trade_def) never collapse into one row.
CREATE UNIQUE INDEX IF NOT EXISTS missed_one_current_per_subject
    ON "user".missed (
        user_id, trade_date, kind, ticker,
        COALESCE(card_id, 0), COALESCE(trade_def_md5, ''),
        COALESCE(formation_at, '-infinity'::timestamptz),
        COALESCE(CASE WHEN kind = 'formation' THEN pool_member_id END, 0))
    WHERE is_current;
CREATE INDEX IF NOT EXISTS missed_trade_date ON "user".missed (trade_date, kind);
