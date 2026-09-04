# `src/cobalt/session/guard.py`

## What it does
`assert_writable(actor, target=..., now=..., clock=..., store=...)` —
the `market_reset` hard block. Returns the `Session` when writing is
allowed; raises `SessionBlocked` when it is not.

## What it protects
20:00–21:00 ET is when the day's record closes out and
`com.cobalt.archiver` pulls the day's bars (20:30). A card or a note
landing in that window lands in a day whose books are being closed. The
answer is a refusal, not a warning.

## Three things happen on a refusal, in this order
1. `SessionBlocked` is raised with **one loud message** naming the
   window (`20:00-21:00`), the current ET clock, and when the block
   lifts (`21:00 ET (overnight)`).
2. A line goes to the log at `ERROR`.
3. A row goes to `session_blocks` — the heartbeat-visible counter.

**Step 3 cannot undo step 1.** The refusal is decided before anything is
recorded, and `SessionBlockStore.record()` logs-and-returns on a
database failure rather than raising. A Postgres outage loses the
counter row; it does not turn a hard block into a pass.

## Key functions/classes
- `SessionBlocked(RuntimeError)` — carries `.session` and `.actor`.
- `block_message(clock, ts, actor)` — the message, built once.
- `assert_writable(...)` — the gate. `now` is the test seam.

## Who calls it
| Caller | Actor string |
|---|---|
| `vaultwrite/writer.py` `create_if_absent` | `vaultwrite:<writer>:create_if_absent` |
| `vaultwrite/writer.py` `upsert_unit` | `vaultwrite:<writer>:upsert_unit` |
| `vaultwrite/writer.py` `upsert_region` | `vaultwrite:<writer>:upsert_region` |
| `aset/web.py` `POST /size` | `aset.card` |
| `aset/web.py` `POST /fill` | `aset.fill` |

## The two carve-outs, and why
- **`--dry-run`** is not gated. It writes nothing, and finding out what
  a job *would* have done is exactly what you want at 20:30 when a job
  just refused.
- **`VaultWriter.restore`** is not gated. It is the L28 rollback path
  and a human action; locking recovery out for an hour would mean the
  one hour you most want to undo a bad write is the one hour you cannot.
  The restore is still audited and still stamps its session.

`POST /fill` **is** gated, even though the instruction named card
creation: a fill is a DB `UPDATE` plus a note write, and the note write
would be refused downstream anyway — leaving the card marked `FILLED` in
Postgres with nothing in the journal. Refuse the whole thing up front
instead of half of it.

## Tests
`tests/cobalt/test_session.py` — the Charter refusal with its message
asserted clause by clause; every other session allowed; the counter row
captured with its actor/target/reason; a dead database losing the row
but not the block; and four wiring tests proving the gate is actually on
`create_if_absent` / `upsert_unit` (file byte-identical after the
refusal), that a dry run still works at 20:30, and that a real write
stamps `vault_writes.session`.
