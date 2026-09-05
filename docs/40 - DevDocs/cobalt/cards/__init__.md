# `src/cobalt/cards/__init__.py`

## What it does
The F7 package's public surface: `CardState`, `Actor`, `ALLOWED`,
`TERMINAL`, `STOP_EDITABLE`, `KEY_EDITABLE`, `assert_edge`,
`edge_table_markdown`, `CardStore`, `CardStateError`,
`IllegalTransition`, `expire_due`, `window_end_for`.

## The four pieces, one law each
| Module | Law |
|---|---|
| `models.py` | the **edge table**, in one place, as data; illegal edges refused by name, never coerced |
| `store.py` | state + ledger row in **one transaction or neither**; the F1 guard runs **first** |
| `expire.py` | a closed window is an **act** with an actor and evidence, not a predicate on read |
| `cli.py` | `cobalt cards state/history/move/backfill/expire/edges` |

## S1 scope
The moves are **manual** — Dejan's buttons on the ASET sheet. The
TRIGGERED detector is S2/S4's, and it will call exactly the same
`store.transition()` these buttons call: the state machine does not
learn a second write path when the detector arrives.
