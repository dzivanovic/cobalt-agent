# `src/cobalt/radar/throttle.py`

Implements the stop-first Finviz throttle measurement. It refuses trading/reset windows, uses only synthetic fixture inputs, records transport metrics, stops on the first bad status/redirect/body/header, and derives the tunable as half the highest achieved clean rate.

## Where its column set comes from (AT-1 2.3)

The probe measures the radar's request, so its screener request has to be the radar's shape — a probe of a narrower export measures a different request. The module holds no config of its own and does not open one: `run_probe(..., columns=...)` is a required argument, and `command()` (the `cobalt radar throttle-probe` entry point) reads `export.columns` from the radar config once and hands it down. `run_probe` renders it through `config.screener_columns_param`, so a malformed declaration crashes before the first request rather than after the measurement. Tests that exercise the stop-first behaviour pass the smallest valid declaration; `tests/cobalt/test_finviz_consumers.py` drives `command()` itself to pin that the probe sends the shipped set.

