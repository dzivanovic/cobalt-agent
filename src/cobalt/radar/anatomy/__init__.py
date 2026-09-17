"""Anatomy detectors — pure functions over bars (S2-P2 STEP-3).

Taxonomy anatomy is system data (L32): Range, Leg, Extension, the session
clock. These modules turn stored bars into the typed observations the §10.5
atoms name, and nothing else — no database, no network, no clock read, no
trade_def content. The S5 evaluate stage (STEP-4) feeds them bars and
tunables and records every observation it consumed (L57).

    bars.py        working-TF buckets, completeness-flagged (Astra R1-8)
    indicators.py  true range, Wilder ATR, volume MA + sigma band (R1-9)
    leg.py         legs terminated by one opposing bar
    extension.py   Extension path A (lands cards) / path B-only (R4)
    structure.py   tracked extreme, bar_break trigger, structural stop
    daily.py       daily bars: prior session, daily ATR, HTF refs (R5)
    registry.py    which atoms/triggers/stops S2 can evaluate (R2)
"""
