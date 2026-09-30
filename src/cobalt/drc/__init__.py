"""DRC automation, chunk D1 — his two daily files, parsed and paired.

`DRC-AUTOMATION-v2-2026-09-22.md` §9 D1, with his rulings of 09-22
(R91–R117) and 09-23 (R17, R59):

- `detect`      — the ONE header classifier (R114): every import path
                  asks it what a file is; it reads the first line only,
                  never the name or the extension.
- `trading_log` — his broker platform's daily execution export, read by
                  column NAME behind `ExecutionSource` (L9).
- `stats_log`   — his trade journal's daily log (entries, targets, R:R,
                  MAE/MFE, playbooks) behind `TradeStatsSource`.
- `pairing`     — FIFO executions → trades + exit legs; open positions
                  carried to the next day (R67); the stats match.
- `store`       — `DrcStore`, the one writer of every `drc_*` row (L40).

No vendor or person name enters an identifier here (L31); the files
are cited only in docstrings.
"""
