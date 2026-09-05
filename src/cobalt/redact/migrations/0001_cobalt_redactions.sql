-- 0001: cobalt_redactions — F19's counter, and the F18 heartbeat's number.
--
-- Prefixed for the reason recorded in jobs/migrations/0001_cobalt_jobs.sql:
-- `cobalt_brain` SHARED its database with Mattermost's 103 tables until
-- 2026-09-04 (ADR-0006, one database per product), and a
-- generic name is a collision waiting to happen. Mattermost has no
-- `redactions` table today; this does not rely on that staying true.
--
-- ONE ROW PER (event, pattern). There is deliberately NO column that
-- could hold a secret value: this table is read by whoever is debugging
-- an alert, and a schema with nowhere to put the material cannot leak it
-- by accident. `pattern` is a NAME from configs/cobalt/redact.yaml (or
-- `literal:<vault key name>`); `channel` is where the text was headed
-- (mattermost / email / heartbeat / log).
CREATE TABLE IF NOT EXISTS cobalt_redactions (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ts TIMESTAMPTZ NOT NULL DEFAULT now(),
    channel TEXT NOT NULL,
    pattern TEXT NOT NULL,
    hits INTEGER NOT NULL CHECK (hits > 0)
);

CREATE INDEX IF NOT EXISTS cobalt_redactions_ts_idx ON cobalt_redactions (ts);
