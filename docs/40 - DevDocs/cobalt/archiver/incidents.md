# `src/cobalt/archiver/incidents.py`

New 2026-09-19 with the append-only redesign (chunk P). Spec:
`docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §6, §7,
§11. Table: `src/cobalt/db_migrations/0011_archive_incidents.sql`.

## What it does
Writes and reads `system.archive_incidents` — what a night REFUSED to
do, and why, kept until a person resolves it. The five kinds live in
`reconcile.IncidentKind`, beside the decisions that raise them, and are
imported here rather than re-spelled (L3): `gap`, `restated`,
`stored_only`, `empty_export`, `regression`.

## Key functions/classes
- `open_or_refresh(conn, draft, *, run_id, now) -> int` — `ON CONFLICT
  (kind, ticker, interval, range_start) WHERE resolved_at IS NULL DO
  UPDATE`. A condition that recurs every night for a fortnight is ONE
  row whose `last_seen_at` moves, not fourteen. `first_seen_at` is
  written once and never touched again — it is how long a target has
  been withheld, which is the number an operator actually needs, and a
  test asserts it is absent from the `DO UPDATE SET` clause.
- `unresolved(conn, ticker=None) -> list[IncidentRow]` — read-only, what
  `cobalt archiver incidents` prints and what the heartbeat counts.
- `resolve(conn, id, *, by, note, now)` — explicit and audited.
- `counts_by_kind(rows)` — pure; the heartbeat's detail line built from
  rows it already holds.

## Data flow in/out
**In:** a `reconcile.IncidentDraft` (pure data — no id, no clock), the
run id and `now`.
**Out:** one row, inside the caller's transaction. `detail` is a closed
JSONB payload: the observed bounds, the differing keys with both values
after normalisation, the session dates, the operator's `--reason` on a
repair (L57 — the stored inputs behind every number).

## Gotchas
- **Which transaction is the RUNNER's decision, not this module's.**
  Normally the incident is written inside the target's one transaction
  (§4). The exception matters: a failed or withheld target's
  transaction is ROLLED BACK, so its incident is persisted afterwards in
  a second small transaction (Astra, V3-2 — "persist failure evidence
  separately after rollback"), because evidence written inside the
  doomed transaction dies with it.
- **Resolution never happens by itself.** No run closes a row, and
  `resolve` refuses an empty `by`. The heartbeat is not green while a
  row is unresolved (§11, O-7), and a self-closing incident would be a
  dashboard that goes green on its own.
- **`NULLS NOT DISTINCT` on the index is what makes `empty_export`
  work.** That kind has no span, so its `range_start` is NULL; under the
  default NULL rule a target failing empty for a month would open thirty
  rows for one condition. See the migration's own comment.
- An open `restated` incident does NOT stop the poller writing — that is
  Known limit 1 (spec §12), it goes to the owner WITH the switch ruling,
  and `test_archiver_quiet.py` demonstrates it executably rather than in
  prose.
