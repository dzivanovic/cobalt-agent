# `src/cobalt/radar/anatomy/__init__.py`

Package marker for the S2-P2 anatomy detectors. These are pure functions over bars, with no database, network, clock read or trade_def content. They turn stored bars into the typed observations the §10.5 atoms name. Taxonomy anatomy is system data (L32). The S5 evaluate stage (STEP-4, chunk B) feeds them bars and tunables and stores every observation it consumed (L57).

Modules: `bars` (completeness-flagged working-TF buckets), `indicators` (true range, Wilder ATR, volume band), `leg`, `extension` (path A / B-only), `structure` (tracked extreme, bar_break trigger, structural stop), `daily` (prior session, daily ATR, HTF refs), `registry` (what S2 can evaluate), `freshness` (RVOL observations, staleness per dependency).
