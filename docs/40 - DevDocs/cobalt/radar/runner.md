# `src/cobalt/radar/runner.py`

Runs the resident cycle in membership, pool-row, mirror, then per-ticker bar transactions. It checks the session before work and again through each store's `before_commit` hook, stamps partial failures, uses monotonic scan IDs, and makes idle/reset cycles perform no Finviz calls.

A transaction that reaches `market_reset` rolls back and records its stage on the resident runner without attempting another write in the blocked window. The next active cycle includes that pending stage and scrubbed detail in its pool-row transaction, keeps the stamp visible through that cycle's poll-status transaction, and then clears the in-process pending marker. A later cycle can clear a recovered bars failure normally.

`_pool_row` (S2) carries the previous row's `poll_failures` forward and, when that list is non-empty, writes `failed_stage='bars'` and `failed_detail='poll failures: N'` — the same strings `RadarStore.stamp_poll` writes at S4. Before 2026-09-15 S2 wrote the row clean and S4 re-stamped it about 70 s later; a heartbeat beat that sampled the gap read OK, so the radar probe flapped (27/27 beats fit that phase rule, `reports/cto-2026-09-15.md` §1.2). Membership, pending-drop and mirror failure stages still override the carried `bars` stage exactly as before, and S4's `stamp_poll` remains the one place a bars failure clears.

## S5 evaluate (S2-P2 R1)
`RadarRunner` takes `evaluator` (an `evaluate.EvaluateStage`) and `ceiling_rpm`. `build_runner` always wires both. `None` is the S1–S4-only shape, used by the pre-S5 tests and by the membership replay tool (`scan --replay`), and that choice is written at their call sites. Supplying an evaluator without a ceiling raises.

- **Lifecycle polling (Astra R1-15).** Before S4 the runner asks the stage for the tickers of open radar cards whose member left the pool. `notes.lifecycle_poll_demand` then decides against the total planned demand:
  - inside the ceiling: they join the S4 poll list;
  - otherwise they are not polled, and the refusal is stamped `failed_stage='bars'` with the named total.
- **S5 order.** S5 runs after S4's status stamp, behind the same `gate` hook with `evaluate:*` labels, and gets the scan's RVOL observations (`anatomy.freshness.rvol_observations`) and the pool unit (pool block, frozen flag, source sets).
- **Failure handling.**
  - A `StageDropped` returns `dropped` with stage `evaluate`; the run row stays `running` and the next cycle abandons it.
  - Any other failure stamps `failed_stage='evaluate'` with the scrubbed detail and returns `scanning`; S1–S4 results stand.
  - Card refusals collected by a published run are stamped the same way.
- **Settings freshness.** The resident's stage reads trader settings every cycle and resolves today's rung from `DayModeStore` + `decided_or_stage1`.
