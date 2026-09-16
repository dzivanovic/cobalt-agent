# `src/cobalt/radar/notes.py`

Reads each source note once as bytes, hashes the note and every YAML fence, dispatches strict block kinds, checks pool overrides and the ruled request budget, and mirrors status through `TraderSettingsStore.put`. `parse_note_bytes` gives prospective validation the identical parser without temporary files. An invalid pool freezes membership decisions.

## The budget is total demand (L53)
`plan_transport_demand` is the ONE demand computation. `load_sources`, `configured_sources` and `radar screens validate` all go through it, and it returns a `TransportDemand`, which `ParsedSources.demand` keeps. A budget that measures one consumer is not a budget, so it counts every consumer of the shared Finviz transport together:

- steady, every scan cycle: pool bar-polling, one request per screen, one per list ticker-chunk, one per context ticker (`planned_context_rpm`);
- once per ET day: the daily-bar cold burst, one request per pool name (`daily_names = pool.cap`);
- every consumer is multiplied by (1 + `retries_per_request`).

It REFUSES in two cases: steady demand above the ceiling, or daily names with no headroom left after steady demand (the burst would never drain). Otherwise it REPORTS actual pacing: `cold_drain_minutes` at the remaining headroom, `cycle_requests`, `cold_cycle_seconds` (the first cold cycle paced by the bucket at the ceiling) and `cold_cycle_overruns_scan_interval`. These are reported, not refused, because the ceiling and cadence are Dejan's to set (L53) and the bucket waits rather than exceeds (Astra R1-13).

`planned_total_rpm` stays as the steady-demand sum and now requires `context_tickers`.

## Gotchas
`load_sources` takes `context_tickers` as a required argument, so no caller can leave the context consumer out. The refusal text names every consumer's share (`context=`, `daily_names=`), so a frozen pool says why.

Out-of-process Finviz callers (the 05:15 and 15:40 ET prefill jobs, the 20:30 ET archiver) are not in this plan. They do not share the resident's bucket.
