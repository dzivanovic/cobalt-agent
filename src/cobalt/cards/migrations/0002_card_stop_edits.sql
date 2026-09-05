-- 0002: card_stop_edits — decision 11's other half (S1-P2).
--
-- "Stop is editable in WATCH and IN-TRADE; key is frozen once armed."
-- A stop edit is NOT a state change: the card stays exactly where it is,
-- so it must not produce a `card_transitions` row (that would break
-- "every row is a state change" and inflate every count keyed off it).
--
-- But it is not nothing either — it moves shares, risk and room, and the
-- 09-03 lesson is that an unrecorded number is an unrecoverable one. So
-- edits land here as they happen, and the NEXT transition folds every
-- edit made since the previous one into its `evidence` JSON (see
-- store.py's `_pending_stop_edits`). That is the ruling read literally:
-- "a stop edit is not a state change but is logged in evidence on the
-- next transition."
CREATE TABLE IF NOT EXISTS card_stop_edits (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    card_id     BIGINT NOT NULL REFERENCES aset_sizings(id) ON DELETE CASCADE,
    at          TIMESTAMPTZ NOT NULL DEFAULT now(),
    session     TEXT NOT NULL,
    -- The state the card was in when the edit was made. Kept so the
    -- evidence can show WHERE the stop moved (a WATCH re-read of the
    -- level is a different act from a FILLED trail), and so a later
    -- audit can re-check the edit against STOP_EDITABLE.
    in_state    TEXT NOT NULL,
    from_stop   NUMERIC(14, 4) NOT NULL,
    to_stop     NUMERIC(14, 4) NOT NULL,
    actor       TEXT NOT NULL,
    -- Set once the edit has been folded into a transition's evidence, so
    -- one edit is never counted twice.
    folded_into BIGINT REFERENCES card_transitions(id) ON DELETE SET NULL
);
CREATE INDEX IF NOT EXISTS card_stop_edits_pending_idx
    ON card_stop_edits (card_id) WHERE folded_into IS NULL;
