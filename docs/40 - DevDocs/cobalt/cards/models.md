# `src/cobalt/cards/models.py`

## What it does
The **F7 card state machine's edge table**, as data, in one place:
`CardState` (eight states), `Actor` (`cobalt` | `you`), `ALLOWED`
(`from -> {legal to}`), and the refusal (`IllegalTransition`) that
names any edge outside it.

## The edge table
Charter §3 F7 / SPRINT-LADDER §S1. **Generated from `ALLOWED` by
`edge_table_markdown()`** — `cobalt cards edges` prints this exact
table, so this page cannot drift from what the store enforces.

| From | Legal `to` states | Terminal |
|---|---|---|
| `WATCH` | `ARMED`, `EXPIRED`, `MISSED`, `PASSED` | no |
| `ARMED` | `EXPIRED`, `TRIGGERED`, `WATCH` | no |
| `TRIGGERED` | `EXPIRED`, `FILLED`, `PASSED` | no |
| `FILLED` | `CLOSED` | no |
| `CLOSED` | — (none) | yes |
| `PASSED` | — (none) | yes |
| `EXPIRED` | — (none) | yes |
| `MISSED` | — (none) | yes |

11 legal edges out of 64 ordered
pairs; the other 53 are refused
by name. `TERMINAL` is **derived** (`no outgoing edge`), not listed a
second time — one-path rule applied to a constant.

## The two laws it encodes
1. **No card exists without a state.** A card row is created together
   with its genesis transition (`from_state` NULL -> `WATCH`), and
   `aset_sizings.state` is `NOT NULL` (migration 0007). The state is set
   *in the INSERT*, so there is not even a sub-transaction window in
   which a state-less card exists.
2. **No state changes without a transition row.** `state` on the card is
   a cache of the last `card_transitions` row; `store.transition()`
   writes both or neither.

## Why `ARMED -> WATCH` walks backwards
It is `disarm`, and it is the only backwards edge. Card-spec §2.2:
while armed there is nothing to decide *except* disarm, so the way out
has to exist. It requires a reason (see `store.py`).

## Why illegal edges are refused, never coerced
There is no "nearest legal state" fallback and no silent no-op. A card
that reached a wrong state quietly is a card whose DRC count is wrong,
and F7's acceptance test is precisely that those counts match Postgres.
`IllegalTransition` names both ends, lists what *was* legal, and says
explicitly when the source state is terminal.

## Editability constants (mock decision 11)
- `STOP_EDITABLE` = {`WATCH`, `FILLED`} — stops move with structure,
  in the pre-trade read and in-trade. 
- `KEY_EDITABLE` = {`WATCH`} — the key is a **risk commitment**, frozen
  from `ARMED` onward.

## Key functions
- `is_legal(from, to)` / `assert_edge(from, to, card_id=...)` — the gate.
- `edge_table_markdown()` — renders the table above (CLI + this page).

## Who uses it
`cards/store.py` (enforcement), `cards/expire.py` (`EXPIRABLE` is
asserted against it), `aset/web.py` (every button on the sheet is
rendered *from* `ALLOWED`, so no illegal button can be drawn),
`cobalt validate` (reachability check), and the tests.

## Related
`docs/30 - Design/TRADE-RADAR-CARD-MOCK-v0_1/card-spec.md` §2 (lifecycle),
`decisions.md` #1 / #7 / #11.
