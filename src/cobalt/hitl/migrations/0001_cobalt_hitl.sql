-- 0001: "user".cobalt_hitl_requests — one row per requested action (F20 FINAL §2, §3).
--
-- USER SIDE: his approvals and what the chief of staff asked of him (L32,
-- card 730 DECISION 4). Created by `HitlStore.ensure_schema`, directly on
-- its side, the way every module table is (placement.py MODULE_TABLES).
--
-- THE BYTES. `rendered` holds the exact file bytes B the page shows and the
-- executor writes; `sha256` is sha256(B) (F-18). For `agents.deactivate`
-- `before_bytes` / `before_sha256` bind the file as it was when he looked
-- (F-08): the executor refuses unless the bytes on disk still equal them.
--
-- THE KEY (F-06 = B). Only `approve_key_sha256` is stored; the 128-bit key
-- itself travels in the card DM's link fragment and nowhere else.
--
-- THE ONLY pending -> approved / denied WRITE is the two `/hitl` routes in
-- aset/web.py (L37, T3). The executor writes executed / failed; the sweeper
-- writes expired. `reported_at` marks the outcome DM + the session line as
-- sent, so each terminal outcome is reported exactly once (L18).

CREATE TABLE IF NOT EXISTS cobalt_hitl_requests (
    id                  BIGSERIAL PRIMARY KEY,
    user_id             INTEGER NOT NULL REFERENCES traders(id)
                            DEFAULT (current_setting('cobalt.trader_id')::int),
    short_id            TEXT NOT NULL UNIQUE,
    agent_id            TEXT NOT NULL,
    action              TEXT NOT NULL,
    payload             JSONB NOT NULL,
    sha256              TEXT NOT NULL,
    rendered            BYTEA NOT NULL,
    before_sha256       TEXT,
    before_bytes        BYTEA,
    reason              TEXT NOT NULL,
    status              TEXT NOT NULL DEFAULT 'pending'
                            CHECK (status IN ('pending', 'approved', 'denied', 'expired',
                                              'executed', 'failed')),
    created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
    expires_at          TIMESTAMPTZ NOT NULL,
    decided_at          TIMESTAMPTZ,
    decided_via         TEXT,
    deny_reason         TEXT,
    result              JSONB,
    error               TEXT,
    approve_key_sha256  TEXT NOT NULL,
    reported_at         TIMESTAMPTZ
);

CREATE INDEX IF NOT EXISTS cobalt_hitl_requests_status ON cobalt_hitl_requests (status, id);
