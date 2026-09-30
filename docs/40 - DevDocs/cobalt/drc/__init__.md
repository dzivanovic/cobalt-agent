# `src/cobalt/drc/__init__.py`

## What it is
The package for DRC automation, chunk D1 (`DRC-AUTOMATION-v2-2026-09-22.md`
§9 D1, as changed by his rulings of 09-22 R91–R117 and 09-23 R17 / R59).
It holds a docstring and no code. It covers his two daily files, parsed
and paired, and their store.

| module | job |
|---|---|
| `detect` | the ONE header classifier (R114) — what a file is, from its first line only |
| `trading_log` | the daily execution export → `Execution`s (`ExecutionSource`, L9) |
| `stats_log` | the journal's daily log → `StatsRow`s (`TradeStatsSource`, L9) |
| `pairing` | FIFO trades + exit legs, open positions carried (R67), the exact stats match |
| `models` | the typed records |
| `store` | `DrcStore`, the one writer of `drc_imports` / `drc_fills` / `drc_rows` (L40) |

## Names (L31)
No vendor or person name enters an identifier, an enum value or a schema
name. The kinds are `trading_log` and `stats_log`, and the flags are
`trading_log_shape` and `stats_log_shape`. His files are cited only in
docstrings.

## Not in D1
These belong to later chunks:
- the import page, the bytes writer and the input event (D2)
- the note and its build (D3)
- settings (D4)
- leg corrections (D5)

D1 also has no folder reader. `detect.import_folders` is only the
listing rule that D2's reader applies.
