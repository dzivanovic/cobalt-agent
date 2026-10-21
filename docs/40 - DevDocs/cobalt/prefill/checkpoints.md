# `src/cobalt/prefill/checkpoints.py`

F5 (FINAL `docs/30 - Design/F5-FINAL-2026-10-11.md`, card 731): the four market-context checkpoints at 07:15, 07:45, 08:15 and 08:45 ET. Each run writes one unit of Finviz numbers, the delta since the previous checkpoint and a short narrative into today's daily note, directly under `### Market Context:` (split A, R1055 + R1056).

## The command

```
uv run cobalt checkpoint run --slot HHMM [--dry-run]
```

It is the plist command (`ops/com.cobalt.checkpoint-HHMM.plist`) and the manual trigger. `--slot` must be `HHMM` (argparse refuses anything else) and one of `prefill.yaml` `checkpoints.slots` (`CheckpointError`, exit 1). The run sits under `as_job("com.cobalt.checkpoint-HHMM", skip=dry_run)`. A dirty run raises `CheckpointNotClean` inside the job, so the job row records exit 1. A run outside its slot window prints the `REFUSED:` line and exits 2 BEFORE `as_job`. So a late launchd fire leaves no job row, and the watchdog's MISSED stands.

`--dry-run` ignores the window and writes nothing: no note bytes, no `market_checkpoints` row, no `vault_writes` row, no DM. It still reads the stores (the base row, today's slots) and calls the model.

## The config block

`configs/cobalt/prefill.yaml` top-level `checkpoints:`, loaded only by `CheckpointsConfig` / `load_checkpoints_config()` (`prefill/config.py`). It sets `extra="forbid"` and requires every key: `slots` (with `source: ruling`, Charter:50), `indices`, `groups` (`{g: sector, v: 140}`), `route` (`checkpoint.narrative`), `narrative_max_lines` (3), `section` (`market_context`) and `heading` (`### Market Context:`). There is no `grace_min` and no tunables row. `prefill:` is untouched.

The route `checkpoint.narrative` is in `configs/cobalt/modelaccess.yaml`. It uses the local lane, `mainframe`, `json_schema` and no key. `timeout_s: 60` and `max_output_tokens: 512` are UNMEASURED and provisional; X3 is owed before the plists load (card DECISION 2).

## The table

`system.market_checkpoints` (`db_migrations/0029_market_checkpoints.sql`, rollback drops it). SYSTEM side: public market figures, no `user_id`. It holds one row per `(trade_date, slot)`, UNIQUE, and `CheckpointStore.upsert` updates the row in place on a re-run. The columns are `figures`, `source_status`, `base_slot`, `base_at`, `base_figures` (a COPY of the figures the delta used, so a later re-run of 07:45 never changes what 08:15 replays), `delta`, `narrative_input`, `prompt_sha256`, `narrative`, `narrative_status`, `model_returned`, `write_status`, `vault_write_id`, `fetched_at`, `created_at` and `updated_at`. `vault_write_id` has no foreign key, because `vault_writes` is purged at 30 days.

## The unit body

Unit `checkpoint_HHMM` in section `market_context`, written by `VaultWriter("prefill.checkpoint")`:

```
as of 07:45 ET cobalt                 ← format_stamp(slot instant) + cobalt | cobalt-degraded
SPY 500.00 +0.10% · QQQ … · IWM …     ← or: degraded: finviz-screener — <reason>
Sectors: Utilities +1.00% · …         ← competition-rank order; or: degraded: finviz-groups — <reason>
Δ since 07:15:                        ← or: Δ since prior close: (the day's first run)
- <one delta line each>
narrative: pending                    ← then: Narrative: + lines, or narrative: degraded (<kind>)
```

A gate refusal replaces the two source lines with `degraded: finviz — demand ceiling`. A body never has a markdown heading line. A slot with no row when a later slot runs gets the one line `MISSED HH:MM — no run recorded`.

## The order of a run

1. config and route (crash before any fetch);
2. `TradingCalendar.is_trading_day`: on a closed day, nothing is fetched or written, exit 0;
3. the slot window, from the slot's time to the next slot's (08:45 to `FULL_VIEW_BY` 09:00): REFUSED, exit 2;
4. one `check_scheduled_demand("checkpoint", radar_rpm=radar_planned_rpm(), extra=[2 rpm over the slot minute])`. A refusal or an unreadable plan sends no GET;
5. the fetch: `fetch_market_table` (F4's, unchanged) and one Groups GET `g=sector&v=140` (`fetch_groups`, the token and scrub from `aset.prefill`). Each source fails alone. A body that is not exactly the eleven `SECTORS`, or a row with no Change, is a failed groups source;
6. `compute_delta(figures, base)`, a pure function. The base is the latest earlier slot of today with stored figures; with none, the base is the prior close. Lines are `prior_close`, `index_move`, `rank_move` (only when the integer rank changes), `leader` and `laggard` (the tied sets). There is no crossing field. A sector name set that differs from the base fails the groups source;
7. upsert the row (`vault_write_id` null);
8. F4's `ensure_daily_note(writer, when)`;
9. a MISSED unit for every earlier slot with no row, and ONE `send_dm` naming the newly written ones;
10. the unit with the numbers and `narrative: pending`. It is skipped when the unit on disk already holds the same numbers, so a re-run with the same figures is a zero diff;
11. ONE `call_sync` on the route. The input is the delta list only. `validate_reply` accepts `{lines: [{phrase_id, refs}]}` only: a digit in any string, a phrase outside `PHRASES`, a ref out of range or to a line of another phrase, a schema failure, or more than `narrative_max_lines` gives `narrative: degraded (unsourced figure)`. A modelaccess error gives `narrative: degraded (<kind>)`. There is no retry and no second lane;
12. the same unit with the narrative, then the row's narrative fields, `write_status` and `vault_write_id`.

A refused or failed write (the writer's `VaultWriteError`, a second `NoteChangedOnDisk`, a market-reset refusal) sets `write_status` FAILED, sends a DM and exits 1, with no model call after a failed numbers write.

## Exit codes

0: every Finviz source is ok (the narrative may be ok or degraded), or the day is closed. 1: a Finviz source is degraded (fetch error, the eleven-row rule, the gate, a changed sector set), or the write FAILED. 2: the slot window. A config error crashes before any fetch.

## The laws on the job

L1 (fail loud: every refusal is a line, an exit code and, for writes, a DM). L3 (one screener function, one groups fetch, one note creator, one model path). L9 (each source degrades alone). L10 (the config block). L25 (one lane, no fallback). L28 (marker-bounded units only; his text under the heading stays outside the section and byte-identical; dev vault in tests). L42 (restarts derived: `com.cobalt.aset`, `com.cobalt.radar`; the four plists are new one-shots, BOOTSTRAP deferred). L53 (the one gate with the planned radar rpm).

Tests: `tests/cobalt/test_checkpoints_offline.py`, `test_checkpoints_registry.py`, `test_checkpoints_db.py` (with-DB, PASS 2), `test_checkpoints_live.py` (live-note, read only).

## 2026-10-19 — f5-checkpoints-1018
Created (card 731 K2–K8): the module, its store and its command.

## 2026-10-20 — f5-checkpoints-fr1
Check O1: `run_checkpoint` now refuses a `checkpoints.route` that names an embeddings route (card 469's `EmbedRoute`) with `PrefillConfigError`, before any fetch.
