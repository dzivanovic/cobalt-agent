# `src/cobalt/radar/throttle.py`

Implements the stop-first Finviz throttle measurement. It refuses trading/reset windows, uses only synthetic fixture inputs, records transport metrics, stops on the first bad status/redirect/body/header, and derives the tunable as half the highest achieved clean rate.

