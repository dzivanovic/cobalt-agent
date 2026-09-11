# `src/cobalt/archiver/aggregate.py`

Pure OHLCV aggregation for radar replay comparisons. Bars are grouped by ticker and ET wall-clock buckets floored from midnight; open/high/low/close/volume are explicit. It never persists derived bars.

