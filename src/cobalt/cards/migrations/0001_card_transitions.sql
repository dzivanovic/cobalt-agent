-- 0001: card_transitions — F7's ledger (S1-P2).
--
-- "No state changes without a transition row." This table is the record;
-- `aset_sizings.state` is a cache of its last row, written in the same
-- database transaction. If the two ever disagree, THIS is the truth —
-- which is why the DRC counts (Charter §3 F7's acceptance test) are
-- asked of this table and not of the card's own column.
CREATE TABLE IF NOT EXISTS card_transitions (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    -- The aset_sizings row. FK with ON DELETE CASCADE: a card and its
    -- history are one object, and an orphan transition is a count with
    -- no card behind it.
    card_id     BIGINT NOT NULL REFERENCES aset_sizings(id) ON DELETE CASCADE,
    -- NULL only on the GENESIS row (card created -> its first state).
    -- That is the "no card exists without a state" law in table form:
    -- every card has exactly one row here with from_state IS NULL.
    from_state  TEXT,
    to_state    TEXT NOT NULL,
    at          TIMESTAMPTZ NOT NULL DEFAULT now(),
    -- F1: every card, alert and note carries the session it happened in.
    -- Resolved in Python through the NYSE calendar, never derived in SQL.
    session     TEXT NOT NULL,
    -- 'cobalt' | 'you'. His taps are the calibration set and must never
    -- be summed with Cobalt's own moves (Charter §1).
    actor       TEXT NOT NULL,
    -- What justified the move: the trigger print, the backfill marker,
    -- the stop edits made since the previous transition (decision 11 —
    -- a stop edit is not a state change, so it rides here), the expiry
    -- window that elapsed. JSONB so it is queryable, not a blob.
    evidence    JSONB NOT NULL DEFAULT '{}'::jsonb,
    -- Free text. REQUIRED for MISSED and for an overrule; optional
    -- elsewhere. Enforced in the store, where the rule can say why.
    reason      TEXT
);
-- The history of one card, in order — the store's read path and the
-- sheet's terminal strip both walk this.
CREATE INDEX IF NOT EXISTS card_transitions_card_idx ON card_transitions (card_id, id);
-- "How many cards were MISSED today" without a sequential scan.
CREATE INDEX IF NOT EXISTS card_transitions_to_state_at_idx ON card_transitions (to_state, at);
-- Exactly one genesis row per card. A second one would mean a card was
-- created twice, and every count downstream would double it.
CREATE UNIQUE INDEX IF NOT EXISTS card_transitions_genesis_idx
    ON card_transitions (card_id) WHERE from_state IS NULL;
