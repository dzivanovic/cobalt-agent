-- 0001: cobalt_email_sends — what the F18 `email` probe reads back.
--
-- Charter §3 F18 asks the probe for "token present + last send result".
-- Presence is answered from the vault with no database at all; the
-- SECOND half needs memory across processes, because the sends happen in
-- three different ones (the heartbeat's 15-minute one-shot, `cobalt
-- notify email-test`, and any future alerting caller) and none of them
-- outlives its own beat.
--
-- WHY A TABLE RATHER THAN THE HEARTBEAT'S OWN JOB ROW. `cobalt_jobs.
-- last_result` is written by the heartbeat and only by the heartbeat, so
-- a send from `email-test` — the exact command used to prove the channel
-- works — would leave no trace the probe could read. A channel whose
-- proof is invisible to its own monitor is not proven.
--
-- NO COLUMN CAN HOLD A SECRET, same discipline as cobalt_redactions.
-- `detail` is written from an ALREADY-REDACTED string (EmailError's
-- contract) and carries a Gmail message id or a failure reason;
-- `message_id` is Google's opaque id, which is not a credential and is
-- exactly what an operator pastes into a support thread.
--
-- Prefixed for the reason recorded in jobs/migrations/0001_cobalt_jobs.sql.
CREATE TABLE IF NOT EXISTS cobalt_email_sends (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ts TIMESTAMPTZ NOT NULL DEFAULT now(),
    ok BOOLEAN NOT NULL,
    -- Who asked: 'heartbeat' | 'email-test' | any future caller. A red
    -- alert that failed to send matters differently from a manual test
    -- that failed, and one column keeps them apart forever.
    caller TEXT NOT NULL,
    message_id TEXT,
    detail TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS cobalt_email_sends_ts_idx ON cobalt_email_sends (ts);
