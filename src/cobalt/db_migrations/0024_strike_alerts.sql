-- 0024: "user".strike_alerts — S4-P2 S3 (F9 delivery, DECISION E4): one row
-- per strike seam transition (a `card_transitions` row with actor 'cobalt'
-- and evidence via 'strike.detector' or 'strike.missed', S4-P1's CONTRACT):
-- when it was pushed over the stream, shown on the pinned tab (the SERVER's
-- clock at the ack) and DM'd by the phone fallback, with the DM's result.
-- USER side (ADR-0008 D2 / L32): one trader's alerts. user_id NOT NULL + FK +
-- the tenant GUC default, owned by cobalt_user, like every user table.
-- Idempotent. Additive: touches no existing object.
--
-- ONE UPSERT ON transition_id fills only a NULL column (aset/strike.py
-- StrikeAlertStore.upsert): whichever comes first — the sheet's fallback
-- tail, the stream's send or the ack — creates the row. The DM is claimed by
-- UPDATE … SET dm_at WHERE dm_at IS NULL AND shown_at IS NULL RETURNING, so
-- one transition is never DM'd twice. NOT session-gated: a delivery record,
-- not trading record.
CREATE TABLE IF NOT EXISTS "user".strike_alerts (
    id               BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id          INTEGER NOT NULL
                         DEFAULT (current_setting('cobalt.trader_id')::int)
                         REFERENCES "user".traders(id),
    transition_id    BIGINT NOT NULL UNIQUE REFERENCES "user".card_transitions(id),
    seam_at          TIMESTAMPTZ NOT NULL,
    pushed_at        TIMESTAMPTZ,
    shown_at         TIMESTAMPTZ,
    dm_at            TIMESTAMPTZ,
    dm_result        TEXT,
    created_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (dm_result IS NULL OR dm_at IS NOT NULL)
);

ALTER TABLE "user".strike_alerts OWNER TO cobalt_user;
CREATE INDEX IF NOT EXISTS strike_alerts_seam_at ON "user".strike_alerts (seam_at);
