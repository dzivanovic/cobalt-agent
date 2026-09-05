-- 0001: day_modes — F6's two-stage day-mode record (S1-P2).
--
-- ONE ROW PER TRADING DAY. The date is the primary key, so the 09:00
-- job is idempotent by construction: a second run on the same day
-- UPDATEs the proposal instead of stacking a second one that the sheet
-- would then have to choose between.
--
-- A row exists ONLY for a day that had a stage-2 proposal. There is no
-- row for a Sunday, a holiday, or any day before 09:00 — stage 1 is a
-- SYSTEM RULE ("the lowest enabled mode"), computed from config and
-- asking him nothing, so persisting it would be storing a constant and
-- inviting someone to edit the stored copy instead of the config.
CREATE TABLE IF NOT EXISTS day_modes (
    trade_date      DATE PRIMARY KEY,
    -- 'stage2' from the moment the row exists — stage 1 has no row.
    stage           TEXT NOT NULL,
    -- What Cobalt proposed, and the assembled sentence behind it. The
    -- reason is stored, not recomputed: it cites the prior day's fills
    -- and the prior DRC, and those change underneath.
    proposed        TEXT NOT NULL,
    reason          TEXT NOT NULL,
    -- What was actually decided. NULL until he approves or overrules —
    -- and while it is NULL the sheet stays on the stage-1 mode.
    decided         TEXT,
    decided_by      TEXT,
    decided_at      TIMESTAMPTZ,
    -- Required when `decided` <> `proposed` (enforced in the store,
    -- where the rule can explain itself).
    overrule_reason TEXT,
    -- F6 match check. The .htk file he STATES he loaded — attested, not
    -- read: Cobalt never touches DAS (absolute boundary). Card creation
    -- refuses while this disagrees with the decided mode.
    attested_sheet  TEXT,
    attested_at     TIMESTAMPTZ,
    -- F1: every row Cobalt writes carries the session it was written in.
    session         TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);
