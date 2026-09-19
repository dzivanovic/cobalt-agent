# `src/cobalt/radar/collector.py`

Strict Finviz screener collector using the shared transport and one process token bucket. It parses CSV by header name, refuses redirects/HTML/missing headers, chunks ticker lists, and caches raw responses only under gitignored `data/radar-cache`.

`_params()` builds the screener request's `v` and `c` from the loaded config: `c` comes from `config.screener_columns_param(config.export.columns)`, never from a literal of its own (AT-1 2.3, L3).

## Daily bars (S2-P2, R5)
`DailyBarsSource` is the collector interface (L9) for daily bars; `FinvizDailyBarsCollector` is its Finviz implementation. It makes one request per name per ET day. The cache is what makes that true: `<cache_root>/<ET date>/daily/<TICKER>.csv`. A cache hit, whether in this process or after a restart, reads the file and takes no token. A miss takes one token from the SAME bucket every other radar consumer uses (`process_bucket`, `radar.finviz_max_rpm`), fetches, parses through `anatomy.daily.parse_daily_csv`, and only then writes the cache, so a refused body is never cached. A redirect, a transport error or a bad body raises `SourceFailure`, and that name's HTF atoms are unavailable. The day comes from the ET date, so the cache does not roll over at 19:00/20:00 ET when the UTC date changes.

`DAILY_RETRIES_PER_REQUEST = 0`: the daily path makes no retries. `notes.plan_transport_demand` multiplies demand by (1 + this), so a retry path added without changing the constant would undercount demand. A test pins it.

## Retention
`prune_cache` is shared by both collectors and deletes recursively. The screener's old files-then-`rmdir` sweep failed on a date directory holding a nested `daily/` (Astra R1-13). Anything not named as a date is left alone.

## Gotchas
The `TokenBucket` WAITS and never refuses. The only refusal is the demand plan in `notes.py`, checked before a scan starts. At runtime, too much demand shows up as slower cycles, never as traffic above the ceiling.
