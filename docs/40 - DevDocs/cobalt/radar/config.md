# `src/cobalt/radar/config.py`

Loads strict engine-only `configs/cobalt/radar.yaml` and cross-checks all radar tunables and units. Unknown keys, missing headers, missing tunables, and wrong units fail naming their source file or row.

`ContextConfig` (S2-P2) declares the context tickers — market and sector ETFs polled beside the pool for the alignment shadow dots. The `context` block is REQUIRED, so the total-demand check always has a number to count; an explicit empty `tickers: []` is a declared zero, and the alignment dots then render `CHECKPOINT_MISSING`. Tickers must be unique uppercase symbols. The list ships empty: STEP-0 found 11 of 14 context tickers without current bars, so no ticker is added until coverage is verified.
