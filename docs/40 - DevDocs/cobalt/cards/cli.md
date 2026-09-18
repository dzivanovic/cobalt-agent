# `src/cobalt/cards/cli.py`

## What it does
`cobalt cards` — the state machine's command surface, mounted by
`cobalt.cli`.

| Command | Purpose |
|---|---|
| `state <id>` | the card's current state |
| `history <id>` | every transition, oldest first, with evidence |
| `move <id> --to STATE [--actor] [--reason]` | one transition through the gates |
| `backfill [--dry-run]` | give every state-less card a state + genesis row |
| `expire [--at ISO] [--dry-run]` | what `com.cobalt.cards-expire` runs at 16:05 ET |
| `edges` | print the edge table (the source of the DevDoc page) |

## Notes
- `--at` exists for the same reason `session now --at` does: the tests
  freeze the clock rather than sleeping until 16:05. It refuses a naive
  datetime — sessions are ET, storage is UTC (ADR-0007).
- `backfill` applies migration 0007's `NOT NULL` only **after** the
  backfill commits — the same two-step the F1 `session` backfill uses.
- `edges` is what `docs/40 - DevDocs/cobalt/cards/models.md` renders, so
  the wiki cannot disagree with what the store enforces.
