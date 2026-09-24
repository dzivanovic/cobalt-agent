# `src/cobalt/radar/handicap.py`

The float / market-cap handicap's pure functions (FLOAT-HANDICAP-v3, H1). Nothing in this module sorts the pool and nothing in it holds a value of the trader's: the thresholds, the factor, the combinator and the missing rule are read from his `HandicapBlock` each call.

## The group verdict (STEP-3, v3 §3 [F-10])

`handicap_group(metrics_row, block)` is the one place a name's group membership is decided, shaped like `config.is_not_equity`. It reads the `float_m` and `market_cap_m` the radar's `_collect` put into the name's `SourceSet.metrics` row (parsed by `runner._number` from `export.handicap_headers`), converts them to `Decimal` through their text so the stored digits are the export's, and compares them with the block's thresholds by strict `<`. Under `combinator: any` a name is `yes` when one known value meets its threshold, `no` when both are known and neither does, and `unknown` when a blank could still change the answer; under `all` it is `yes` only when both are known and both meet, and `unknown` whenever either is blank. Blank, `-` and unparseable are always `unknown`, never a silent `no` (L1). The verdict carries both cells and a plain-words reason (`float`, `cap`, `float and cap`, `neither`, `blank …`) — never a threshold.
