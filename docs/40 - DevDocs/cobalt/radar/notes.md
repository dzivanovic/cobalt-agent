# `src/cobalt/radar/notes.py`

Reads each source note once as bytes, hashes the note and every YAML fence, dispatches strict block kinds, checks pool overrides and the ruled request budget, and mirrors status through `TraderSettingsStore.put`. `parse_note_bytes` gives prospective validation the identical parser without temporary files. An invalid pool freezes membership decisions.

## The budget is total demand (L53)
`plan_transport_demand` is the ONE demand computation. `load_sources`, `configured_sources` and `radar screens validate` all go through it, and it returns a `TransportDemand`, which `ParsedSources.demand` keeps. A budget that measures one consumer is not a budget, so it counts every consumer of the shared Finviz transport together:

- steady, every scan cycle: pool bar-polling, one request per screen, one per list ticker-chunk, one per context ticker (`planned_context_rpm`);
- once per ET day: the daily-bar cold burst, one request per pool name (`daily_names = pool.cap`);
- every consumer is multiplied by (1 + `retries_per_request`).

It REFUSES in two cases: steady demand above the ceiling, or daily names with no headroom left after steady demand (the burst would never drain). Otherwise it REPORTS actual pacing: `cold_drain_minutes` at the remaining headroom, `cycle_requests`, `cold_cycle_seconds` (the first cold cycle paced by the bucket at the ceiling) and `cold_cycle_overruns_scan_interval`. These are reported, not refused, because the ceiling and cadence are Dejan's to set (L53) and the bucket waits rather than exceeds (Astra R1-13).

`planned_total_rpm` stays as the steady-demand sum and now requires `context_tickers`.

## Lifecycle polling (S2-P2, Astra R1-15)
`lifecycle_poll_demand(planned_rpm, names, *, scan_interval, ceiling_rpm)` returns `LifecycleDemand`. It decides whether S4 may also poll `names` departed-member tickers whose radar cards are still open. The count is conservative: those names go on top of the whole planned steady demand, which already budgets the full pool cap, at one request per name per cycle times the same retry factor. Above the ceiling it refuses with the named total. With no planned demand (a frozen or failed note) it refuses rather than assumes.

## Gotchas
`load_sources` takes `context_tickers` as a required argument, so no caller can leave the context consumer out. The refusal text names every consumer's share (`context=`, `daily_names=`), so a frozen pool says why.

Out-of-process Finviz callers (the 05:15 and 15:40 ET prefill jobs) are not in this plan; they do not share the resident's bucket. The scheduled one-shots that DO consume the same Finviz transport (the 20:30 archiver, the 21:10 replay) are counted by the total-demand gate below, over their own windows.

---

## 2026-09-17 — S2-P4: ONE total Finviz demand gate (L53, Astra R1-13/R2-5)

- `DemandWindow` is `[start_min, end_min)` in ET minutes, and `end` may pass
  24:00. `DemandConsumer {name, rpm, window | None, basis}`, where `None`
  means unbounded and so counts everywhere. `TotalDemand` holds the peak
  and the names counted.
- `total_demand(consumers, subject, ceiling)` is the peak concurrent rpm
  over the subject's window. A consumer counts wherever its window overlaps
  the subject's; one proved disjoint contributes zero.
- **`check_total_demand`** is THE shared gate. It raises
  `TotalDemandExceeded` (a `RadarNoteError`) when the peak is above the
  ceiling, or when the ceiling is unmeasured.
- `scheduled_consumers(ceiling=, radar_rpm=, replay_top_n=)` builds its
  list from the job registry and tunables:
  - radar: planned total or the bucket bound, 04:00–20:00.
  - archiver: pacing bound `60 / GENTLE_SLEEP_SECONDS` = 50 rpm, from `at`
    to `at + timeout_s`. It is never omitted because a precondition
    serializes it.
  - replay: `min(2 + 2×top_n, ceiling)`, or the bucket bound, from `at` to
    the deadline.
- `radar_window()`, `replay_window()` (deadline = backup `at` −
  `replay.backup_margin_s`), and `check_scheduled_demand(subject, …,
  extra=)` as the call sites use it.
- Call sites, each before any request: `load_sources` (new
  `radar_window=` / `other_consumers=` kwargs; `configured_sources` passes
  the registry's consumers; an overlap sets `pool_error` to "pool budget
  exceeded: …; REFUSED: total Finviz demand …"), `propose.py`,
  `archiver.runner._run_targets`, and `replay.movers.MoversCollector.exports`
  / `.bars`.
- The radar never computes its demand twice (L3): `load_sources` and
  `propose.py` build the radar `DemandConsumer` from the SAME
  `plan_transport_demand` result (`rpm=demand.steady_rpm`), so the gate
  and the plan share one number. Either refusal — the plan's own
  (`demand.refusal`: steady over the ceiling, or no headroom to drain the
  daily burst) or the gate's (`TotalDemandExceeded`) — freezes the pool
  with the same "pool budget exceeded: …" text, and the gate's refusal is
  appended verbatim after it.
- **Deployment gate (plan ESCALATE 4, still open):** the archiver's pacing
  bound alone (50 rpm) exceeds `radar.finviz_max_rpm` (45, ruled
  2026-09-16). Radar is disjoint and unaffected, but the archiver and
  replay sites refuse until Dejan rules the number.
