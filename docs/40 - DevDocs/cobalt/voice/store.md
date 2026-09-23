# `src/cobalt/voice/store.py`

## What it does
`VoiceTurnStore` — the voice module's one table, `"user".voice_turns`
(migration `0017`). USER side (`SIDE = Side.USER`): a turn is one trader's
words and the command they ran.

## The row is the task row (L18)
- `create` inserts a row in `received`.
- `transition(turn_id, expected, new, at=…, **fields)` is ONE single-flight
  statement — `UPDATE … WHERE turn_id = %s AND state = ANY(<expected>)
  RETURNING` — returning True only for the call that moved the row. It
  stamps `<new>_at` from the caller's clock. This is what makes a confirm
  and a cancel racing on one pending action end with exactly one winner.
- `update` sets non-state fields from a CLOSED list (`UPDATABLE`) that has
  no audio column; an unknown column is a `ValueError`.
- `expire_pending` ends `awaiting_confirm` rows whose pending action's
  `expires_at` has passed (`expired`).
- `reap(now, limits)` fails rows stuck in `received` / `transcribing` /
  `planned` / `executing` past `reap_limits(...)` as
  `failed: reaped_<state>`. It only MARKS: a reaped `executing` row is
  never retried.

## Not session-gated
Like `cobalt_jobs` (FINAL [F-16]): a turn row is the voice module's own
state, not trading record. Every ACT is refused inside `market_reset` by
its owning expert's own gate.

## Reads
`get`, `pending_for_session` (the newest `awaiting_confirm` of one widget
session) and `history(session, limit)` — the agent's only memory (L2).
`delete_test_rows` exists for with-DB tests that commit through REAL
connections, and refuses any session id not shaped like a test's.
