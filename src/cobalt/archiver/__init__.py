"""Bar Archiver — pre-beta component.

Nightly job: archives Finviz intraday bars (i1/i2/i5/i15/i30) before
they roll off Finviz's rolling window, so a minute-bar corpus accrues
for backtesting. Daily/weekly/monthly are NEVER archived here — Finviz
serves 10y+ of those on demand (DATA-SOURCE-MEMO.md), no need to store
a local copy.

Standalone: does not touch or import the old tree's scheduler.
"""
