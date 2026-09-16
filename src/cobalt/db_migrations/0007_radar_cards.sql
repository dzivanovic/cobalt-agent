-- 0007: radar cards, USER side (S2-P2 STEP-1).
--
-- A radar card is an "user".aset_sizings row with origin = 'radar'. It is
-- born UNSIZED (WATCH, no key tapped), so the four sizing columns lose
-- NOT NULL and a CHECK keeps manual cards exactly as sized as before.
-- `trigger_price` / `structural_stop` are the immutable formation
-- evidence; the pre-existing `entry` / `stop` stay the live sizing input
-- (Astra R1-7).
--
-- STORED INPUTS, NOT HASHES (L57, Astra R1-10). `radar_score_receipt`
-- retains the actual consumed pool unit, tunable rows, settings,
-- definitions, tap versions and every observation's value next to its
-- hash. Every run writes one, dark runs included; a later scan or tap
-- writes a new one; immutable once written (a trigger refuses UPDATE). `card_dot_taps` is append-only the same way.
--
-- TENANCY (L32, ADR-0008): every new table carries user_id NOT NULL + FK
-- + the tenant GUC default, is owned by cobalt_user, and has its identity
-- sequence granted explicitly (Astra R1-2). Cross-side references are
-- schema-qualified; 0006 granted REFERENCES on the two system tables.
--
-- IDEMPOTENT (Astra R1-3): ADD COLUMN IF NOT EXISTS, guarded constraints,
-- CREATE ... IF NOT EXISTS, CREATE OR REPLACE for views and functions.

-- ---------------------------------------------------------------------
-- 1. aset_sizings: nullable sizing + card columns.
-- ---------------------------------------------------------------------
ALTER TABLE "user".aset_sizings
    ALTER COLUMN grade DROP NOT NULL,
    ALTER COLUMN risk_budget DROP NOT NULL,
    ALTER COLUMN shares DROP NOT NULL,
    ALTER COLUMN used_risk DROP NOT NULL,
    ADD COLUMN IF NOT EXISTS trade_def_slug TEXT,
    ADD COLUMN IF NOT EXISTS trade_def_md5 TEXT,
    ADD COLUMN IF NOT EXISTS setup_ref TEXT,
    ADD COLUMN IF NOT EXISTS trigger_type TEXT,
    ADD COLUMN IF NOT EXISTS trigger_price NUMERIC(14, 4),
    ADD COLUMN IF NOT EXISTS stop_ref TEXT,
    ADD COLUMN IF NOT EXISTS structural_stop NUMERIC(14, 4),
    ADD COLUMN IF NOT EXISTS formed_at TIMESTAMPTZ,
    ADD COLUMN IF NOT EXISTS expires_at TIMESTAMPTZ,
    ADD COLUMN IF NOT EXISTS why TEXT,
    ADD COLUMN IF NOT EXISTS proposed_key TEXT,
    ADD COLUMN IF NOT EXISTS tapped_grade TEXT,
    ADD COLUMN IF NOT EXISTS sized_grade TEXT,
    ADD COLUMN IF NOT EXISTS snap_notice TEXT,
    ADD COLUMN IF NOT EXISTS conviction NUMERIC(8, 6),
    ADD COLUMN IF NOT EXISTS proximity NUMERIC(8, 6),
    ADD COLUMN IF NOT EXISTS card_score INTEGER,
    ADD COLUMN IF NOT EXISTS score_suppressed TEXT,
    ADD COLUMN IF NOT EXISTS radar_score_id BIGINT REFERENCES system.radar_score(id),
    ADD COLUMN IF NOT EXISTS scan_id BIGINT,
    ADD COLUMN IF NOT EXISTS formula_sha256 TEXT,
    ADD COLUMN IF NOT EXISTS tunables_sha256 TEXT,
    ADD COLUMN IF NOT EXISTS settings_sha256 TEXT,
    ADD COLUMN IF NOT EXISTS health JSONB,
    ADD COLUMN IF NOT EXISTS promoted_at TIMESTAMPTZ;

DO $migration$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
         WHERE conname = 'aset_sizings_manual_sized'
           AND conrelid = '"user".aset_sizings'::regclass
    ) THEN
        ALTER TABLE "user".aset_sizings ADD CONSTRAINT aset_sizings_manual_sized
            CHECK (origin = 'radar' OR (grade IS NOT NULL AND risk_budget IS NOT NULL
                   AND shares IS NOT NULL AND used_risk IS NOT NULL));
    END IF;
    -- trade_def_slug joins the drafted provenance list: it is the def's
    -- identity (ADR-0008 D3 ruling a) and the open-card index below keys
    -- on it; a NULL would silently exempt a card from that uniqueness.
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
         WHERE conname = 'aset_sizings_radar_provenance'
           AND conrelid = '"user".aset_sizings'::regclass
    ) THEN
        ALTER TABLE "user".aset_sizings ADD CONSTRAINT aset_sizings_radar_provenance
            CHECK (origin <> 'radar' OR (trade_def_slug IS NOT NULL AND trade_def_md5 IS NOT NULL
                   AND trigger_price IS NOT NULL AND structural_stop IS NOT NULL
                   AND radar_score_id IS NOT NULL AND scan_id IS NOT NULL
                   AND formula_sha256 IS NOT NULL AND tunables_sha256 IS NOT NULL
                   AND settings_sha256 IS NOT NULL AND pool_member_id IS NOT NULL));
    END IF;
END
$migration$;

-- One OPEN radar card per (member, def, direction), enforced by the
-- database rather than a check-then-insert that races (Astra R1-14).
-- Open = every state with an outgoing edge in cards/models.py ALLOWED.
CREATE UNIQUE INDEX IF NOT EXISTS aset_sizings_one_open_radar_card
    ON "user".aset_sizings (pool_member_id, trade_def_slug, direction)
    WHERE origin = 'radar' AND state IN ('WATCH', 'ARMED', 'TRIGGERED', 'FILLED');

-- One PROMOTED radar card per trader (STEP-6 promote pins one card to
-- #2). Two concurrent promotes lock two different rows, so the "clear the
-- others, set mine" transaction alone cannot hold it; the index can.
-- Added S2-P2 chunk B.
CREATE UNIQUE INDEX IF NOT EXISTS aset_sizings_one_promoted_radar_card
    ON "user".aset_sizings (user_id)
    WHERE origin = 'radar' AND promoted_at IS NOT NULL;

-- ---------------------------------------------------------------------
-- 2. Immutability guard shared by the append-only tables.
-- ---------------------------------------------------------------------
CREATE OR REPLACE FUNCTION "user".refuse_row_update() RETURNS trigger
LANGUAGE plpgsql AS $fn$
BEGIN
    RAISE EXCEPTION '%.% is immutable: a later scan or tap writes a new row, never edits this one',
        TG_TABLE_SCHEMA, TG_TABLE_NAME;
END
$fn$;

ALTER FUNCTION "user".refuse_row_update() OWNER TO cobalt_user;

-- ---------------------------------------------------------------------
-- 3. Dots and taps.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS "user".card_dots (
    id             BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id        INTEGER NOT NULL DEFAULT (current_setting('cobalt.trader_id')::int) REFERENCES "user".traders(id),
    card_id        BIGINT NOT NULL REFERENCES "user".aset_sizings(id) ON DELETE CASCADE,
    factor         TEXT NOT NULL,
    position       SMALLINT NOT NULL,
    source         TEXT NOT NULL CHECK (source IN ('cobalt', 'cobalt-degraded', 'human')),
    tier           TEXT NOT NULL CHECK (tier IN ('deterministic', 'judgment')),
    role           TEXT NOT NULL CHECK (role IN ('shadow', 'live', 'human')),
    engine_value   NUMERIC(18, 6),
    engine_grade   SMALLINT CHECK (engine_grade BETWEEN 1 AND 10),
    engine_why     TEXT,
    engine_inputs  JSONB,
    engine_formula TEXT,
    na_reason      TEXT,
    history        JSONB NOT NULL DEFAULT '[]',
    trader_grade   SMALLINT CHECK (trader_grade BETWEEN 1 AND 10),
    tapped_at      TIMESTAMPTZ,
    UNIQUE (card_id, factor)
);

ALTER TABLE "user".card_dots OWNER TO cobalt_user;

CREATE TABLE IF NOT EXISTS "user".card_dot_taps (
    id                  BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id             INTEGER NOT NULL DEFAULT (current_setting('cobalt.trader_id')::int) REFERENCES "user".traders(id),
    card_id             BIGINT NOT NULL REFERENCES "user".aset_sizings(id) ON DELETE CASCADE,
    factor              TEXT NOT NULL,
    grade               SMALLINT NOT NULL CHECK (grade BETWEEN 1 AND 10),
    engine_grade_at_tap SMALLINT,
    at                  TIMESTAMPTZ NOT NULL DEFAULT now(),
    session             TEXT NOT NULL
);

ALTER TABLE "user".card_dot_taps OWNER TO cobalt_user;

-- ---------------------------------------------------------------------
-- 4. The run receipt: the stored inputs behind every seam number.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS "user".radar_score_receipt (
    id                   BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id              INTEGER NOT NULL DEFAULT (current_setting('cobalt.trader_id')::int) REFERENCES "user".traders(id),
    run_id               BIGINT NOT NULL REFERENCES system.radar_score_run(id),
    pool_key             TEXT NOT NULL,
    scan_id              BIGINT NOT NULL,
    evaluated_at         TIMESTAMPTZ NOT NULL,
    ordered_cohort       JSONB NOT NULL,
    tie_policy           TEXT NOT NULL,
    pool_unit            JSONB NOT NULL,
    pool_unit_sha256     TEXT NOT NULL,
    tunables_snapshot    JSONB NOT NULL,
    settings_snapshot    JSONB NOT NULL,
    definitions_snapshot JSONB NOT NULL,
    tap_versions         JSONB NOT NULL,
    observations         JSONB NOT NULL,
    created_at           TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS radar_score_receipt_run
    ON "user".radar_score_receipt (run_id);

ALTER TABLE "user".radar_score_receipt OWNER TO cobalt_user;

DO $migration$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
         WHERE tgname = 'radar_score_receipt_immutable'
           AND tgrelid = '"user".radar_score_receipt'::regclass
    ) THEN
        CREATE TRIGGER radar_score_receipt_immutable
            BEFORE UPDATE ON "user".radar_score_receipt
            FOR EACH ROW EXECUTE FUNCTION "user".refuse_row_update();
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
         WHERE tgname = 'card_dot_taps_append_only'
           AND tgrelid = '"user".card_dot_taps'::regclass
    ) THEN
        CREATE TRIGGER card_dot_taps_append_only
            BEFORE UPDATE ON "user".card_dot_taps
            FOR EACH ROW EXECUTE FUNCTION "user".refuse_row_update();
    END IF;
END
$migration$;

GRANT USAGE, SELECT ON SEQUENCE "user".card_dots_id_seq TO cobalt_user;
GRANT USAGE, SELECT ON SEQUENCE "user".card_dot_taps_id_seq TO cobalt_user;
GRANT USAGE, SELECT ON SEQUENCE "user".radar_score_receipt_id_seq TO cobalt_user;

-- ---------------------------------------------------------------------
-- 5. Views. The card-joined board lives user-side because system cannot
--    read user data (ADR-0008); it joins each radar card to its row in
--    the latest complete run and says whether the member left the pool
--    (Astra R1-15: pinned cards stay visible, labelled).
-- ---------------------------------------------------------------------
CREATE OR REPLACE VIEW "user".radar_cards_v AS
    SELECT c.id AS card_id, c.user_id, c.created_at, c.ticker, c.direction, c.state, c.state_at,
           c.session, c.account_mode, c.pool_member_id,
           c.trade_def_slug, c.trade_def_md5, c.setup_ref, c.trigger_type, c.trigger_price,
           c.stop_ref, c.structural_stop, c.entry, c.stop, c.formed_at, c.expires_at, c.why,
           c.proposed_key, c.tapped_grade, c.sized_grade, c.snap_notice,
           c.grade, c.risk_budget, c.shares, c.used_risk,
           c.conviction, c.proximity, c.card_score, c.score_suppressed,
           c.radar_score_id, c.scan_id, c.formula_sha256, c.tunables_sha256, c.settings_sha256,
           c.health, c.promoted_at,
           b.id AS board_score_id, b.run_id AS board_run_id, b.evaluation AS board_evaluation,
           b.started_at AS board_started_at,
           (m.left_at IS NOT NULL) AS outside_pool,
           c.last_price, m.last_rank AS pool_position
      FROM "user".aset_sizings AS c
      LEFT JOIN system.radar_board_v AS b
        ON b.id = c.radar_score_id  -- the score row of the card's own latest refresh; not the md5,
                                    -- which stays the formation md5 after a note edit (R2-4)
      LEFT JOIN system.radar_membership AS m ON m.id = c.pool_member_id
     WHERE c.origin = 'radar';

ALTER VIEW "user".radar_cards_v OWNER TO cobalt_user;

-- Per factor x trading session (the ET date of the tap — the promotion
-- bar counts SESSIONS, i.e. trading days, S2-P2 STEP-10): tap vs the
-- engine/desk shadow grade shown at tap time. A tap with no shadow grade
-- is not a pair. `deltas` keeps every |delta| so a report over many days
-- takes the median over all pairs, never a median of daily medians.
-- DROP first: chunk C changed the column list, which OR REPLACE alone
-- refuses on a database that already holds the earlier shape. Nothing
-- depends on this view, and the pair is still idempotent.
DROP VIEW IF EXISTS "user".shadow_agreement_v;
CREATE OR REPLACE VIEW "user".shadow_agreement_v AS
    SELECT t.user_id, t.factor, (t.at AT TIME ZONE 'America/New_York')::date AS trade_date,
           count(*) AS pairs,
           percentile_cont(0.5) WITHIN GROUP (
               ORDER BY abs(t.grade - t.engine_grade_at_tap)) AS median_abs_delta,
           avg(CASE WHEN abs(t.grade - t.engine_grade_at_tap) <= 2 THEN 1.0 ELSE 0.0 END)
               AS within2_share,
           array_agg(abs(t.grade - t.engine_grade_at_tap) ORDER BY t.id) AS deltas
      FROM "user".card_dot_taps AS t
     WHERE t.engine_grade_at_tap IS NOT NULL
     GROUP BY t.user_id, t.factor, (t.at AT TIME ZONE 'America/New_York')::date;

ALTER VIEW "user".shadow_agreement_v OWNER TO cobalt_user;
