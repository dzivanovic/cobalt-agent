-- 0001: redactions — F19's counter, and the F18 heartbeat's number.
--
-- ONE ROW PER (event, pattern). There is deliberately NO column that
-- could hold a secret value: this table is read by whoever is debugging
-- an alert, and a schema with nowhere to put the material cannot leak it
-- by accident. `pattern` is a NAME from configs/cobalt/redact.yaml (or
-- `literal:<vault key name>`); `channel` is where the text was headed
-- (mattermost / email / heartbeat / log).
CREATE TABLE IF NOT EXISTS redactions (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ts TIMESTAMPTZ NOT NULL DEFAULT now(),
    channel TEXT NOT NULL,
    pattern TEXT NOT NULL,
    hits INTEGER NOT NULL CHECK (hits > 0)
);

CREATE INDEX IF NOT EXISTS redactions_ts_idx ON redactions (ts);
