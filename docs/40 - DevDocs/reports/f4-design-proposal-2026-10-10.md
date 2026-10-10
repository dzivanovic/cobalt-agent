# F4 design proposal · prefill all day, ownership flags · 2026-10-10

Proposer: Opus 5.5 drafter `f4-design` (S5 Lane A, `s5-weekend-and-parked-answer-2026-10-10.md` §Lanes 1). Next: the L67 tribunal, then the card.
Code base: main's code commit `d0a5fbb8`; `src/`, `configs/`, `tests/`, `docs/00 - Project`, `docs/90 - References` in the working tree are identical to it (`git diff --stat d0a5fbb8` on those paths: empty).
Seam with F5: `f4-f5-seam-2026-10-10.md` (LAWS:363). Both cards cite it.

## 1. What F4 must do
- Charter:82-87 (his text, unchanged): the note exists at 05:15 with Cobalt blocks stamped "as of HH:MM"; refreshes on config cadence and on manual trigger; his text is never touched (L28 units, markers, diff); VIX/BTC show loud "n/a (manual)" until owned. Test: he writes in the game plan at 06:00, prefill re-runs at 08:45, his text is byte-identical; diff row in `vault_writes`.
- LADDER:932 delivers: config cadence + manual trigger; per-field flag cobalt / cobalt-degraded / human; "as of HH:MM" stamps; VIX/BTC loud "n/a (manual)".
- Prebell (`docs/90 - References/INDEX.md:84-86`, the spec of "what good looks like" per `areas/cobalt-sprints.md:42`): the day's view shows each number with its age and its owner. F4 takes that rule only; the prebell tiles (regime, expected ranges, sector heatmap, ranked watchlist) are not F4 (§6).
- `docs/30 - Design/PREBELL-MAP.md` (named at `cobalt-sprints.md:42`) does not exist in the tree; nothing here rests on it.

## 2. What exists today (`d0a5fbb8`)
- One job, `com.cobalt.prefill-daily`, 05:15 weekdays (`configs/cobalt/jobs.yaml:207-212`), entry `uv run prefill daily` (`src/cobalt/prefill/cli.py:30-45`).
- Four slots: rules, daymode, trading, market_calendar (`daily.py:463-473`). A slot already written is skipped (`daily.py:412-435`, `:574-577`), so a second run is a zero-diff no-op. Nothing refreshes after 05:15.
- Every existing-note write is `upsert_unit`, a three-way merge where a human edit wins and is recorded as an override (`vaultwrite/writer.py:673-690`, `merge.py:23-26`).
- The market table fills only blank SPY/QQQ/IWM cells (`daily.py:328-353`). VIX/BTC are blank by a 08-31 SLICE 2.1 note, "no n/a (manual) annotation" (`market.py:7-11`); the Charter (ratified 09-04) supersedes it.
- No stamp exists on any unit. The note header carries the create time only (`templates/daily.md.j2` `#### {{ date_str }} T {{ time_str }}`).

## 3. The defect a refresh would expose (designed out below)
- After any write, the unit's baseline becomes the MERGED body, his lines included (`writer.py:774-795` `unit_after = merged_body`; `writer.py:800-802`).
- The next merge takes that baseline as `base` (`writer.py:886-890`). A line of his that sits in the baseline now reads base == human; if Cobalt's proposal differs, Cobalt wins (`merge.py:15`).
- So a naive refresh keeps his edit on the first refresh and erases it on the second: an edited SPY cell, or a line he inserted inside a Cobalt unit. Today this never fires because each slot is written once. F4 is the first job to rewrite a daily-note unit he may have typed into, so the Charter test fails on the 2nd refresh unless F4 decides ownership itself (§4.4).

## 4. Design

### 4.1 Entry points
- `uv run prefill daily` — unchanged in behaviour: 05:15 create-if-absent, fills every absent slot once. New: stamps and VIX/BTC flags in the template (§4.5, §4.6).
- `uv run prefill refresh [--dry-run]` — NEW. Re-renders the refreshable units of today's note. It is both the scheduled refresh and the manual trigger. If today's note does not exist, it runs the `daily` path first (create, then return).
- F17: refresh runs under `as_job("com.cobalt.prefill-refresh", skip=dry_run)` like `cli.py:34`; the kill phrase stops it.

### 4.2 Cadence
- New job row `com.cobalt.prefill-refresh`: one-shot, supervisor `self`, `timeout_s: 300`, schedule `{every_min_tunable: prefill.refresh_interval_min, window_tunable: prefill.refresh_window, weekdays: [1,2,3,4,5]}` — the seat-usage shape (`jobs.yaml:284-296`, `jobs/config.py:63-117`).
- Tunables rows (`configs/cobalt/taxonomy/tunables.yaml`): `prefill.refresh_interval_min: 30` (unit min), `prefill.refresh_window: "05:45-15:45"` (unit window), `source: dwv`, `status: proposed`. Firings 05:45 … 08:45 … 15:45; 08:45 is a firing, which is the Charter test's re-run.
- Plist `ops/com.cobalt.prefill-refresh.plist`, StartCalendarInterval expanded per `Schedule.calendar_entries()`; `cobalt validate` proves parity.

### 4.3 What refresh rewrites, and what it never touches
- Refreshes: `trading/market_table`, `market_calendar/market_calendar`. The set lives in config (`daily_refresh.units`), validated against exactly these two; any other value refuses the load.
- Never touches: `rules` (his ticked checkboxes; written once at 05:15), `daymode` (owned by `daymode.note.write`, `daymode/note.py:53-54,128`), F5's `market_context` section, the heartbeat, cards, DRC stub and every unmarked line.
- Refresh does NOT call `regenerate_rules_config()` (`daily.py:482`): that writes `configs/cobalt/rules.yaml` in production (`prefill/config.py:37-48`) and would put a committed-file write in a 30-minute job.

### 4.4 Ownership: who owns each line (the per-field flag)
Refresh builds Cobalt's proposed body FROM what is on disk (the `daily.py:328-335` rule, extended), so the merge never sees Cobalt asking to change a line of his.
- **Market table, per row.** For each of SPY/QQQ/IWM whose config owner is `cobalt`, the row is HUMAN when any holds: (a) it differs from `store.last_after(note, "trading", "market_table")`'s row for that ticker and matches no row in `store.recent_afters(...)` (a sync revert is Cobalt's, `writer.py:870-877`); (b) `store.overrides_for(note)` holds an override in `trading/market_table` whose `human_text` carries that ticker's row. A HUMAN row is carried verbatim; a COBALT row is replaced with fresh values. (b) is what keeps his edit after the baseline absorbs it (§3).
- Every other line in the unit (VIX/BTC rows, the separator, lines he inserted) is carried verbatim, in position. The one exception: a VIX/BTC cell that is blank gets `n/a (manual)` (§4.6).
- **Calendar, whole unit.** Refresh rewrites the calendar only while the on-disk body equals `last_after` or one of `recent_afters`. Any other body is his: the unit is left alone (no write, so the baseline never absorbs it and the freeze holds all day) and flagged `human`. An absent unit with his text under the heading stays skipped, as today (`daily.py:578-582`).
- Store reads use the existing public methods (`vaultwrite/store.py:91`, `:111`, `:232`); `writer.py` is not changed.

### 4.5 Stamp and flag line
- First line of each refreshable unit, then a blank line, then the body. Above the table, never below it: a text line directly under a GFM table renders as a table row.
- Shape: `as of 08:45 ET · SPY cobalt · QQQ cobalt · IWM human · VIX n/a (manual) · BTC n/a (manual)`; calendar: `as of 08:45 ET · calendar cobalt` (or `human`, or `cobalt-degraded`).
- Time: ET through `SessionClock.to_et` (`session/clock.py:262`), not the host zone (`daily.py:479` today).
- A line matching `^as of \d\d:\d\d ET` inside the unit is Cobalt's and is replaced; nothing else is.
- The rules unit gets no stamp: it renders his `Rules.md`, which has no data age. The daymode unit keeps its own stage line.

### 4.6 VIX/BTC and the frontier flag
- `prefill.yaml` gains a top-level `daily_refresh:` block (its own Pydantic model, `extra="forbid"`, loaded with `_load_yaml_mapping(PREFILL_CONFIG_PATH, "daily_refresh")`, `prefill/config.py:121-127`). The `prefill:` mapping and `PrefillPathsConfig` (`config.py:107-118`, `extra="forbid"`) are not touched.
  ```yaml
  daily_refresh:
    units: [trading/market_table, market_calendar/market_calendar]
    fields: {SPY: cobalt, QQQ: cobalt, IWM: cobalt, VIX: manual, BTC: manual}
  ```
- `manual` renders `n/a (manual)` into a blank value cell; a cell he has typed is carried and flagged `human`. Flipping a field to `cobalt` is the Charter's frontier move by config (Charter §1); the loader refuses `cobalt` for a ticker `fetch_market_table` cannot serve (VIX/BTC are not Finviz screener tickers, `market.py:7-8`).
- The template's VIX and BTC rows (`daily.md.j2:41`, `:46`) render `n/a (manual)` on create.

### 4.7 Degraded, never blank
- 05:15 create with a dead source: `FAILED` text, as today (`daily.py:107-116`, `:119-125`).
- Refresh with a dead source: the COBALT rows keep their last values, and the flag reads `SPY cobalt-degraded (finviz fetch failed; values as of 08:15)`; the time comes from the previous stamp line on disk. The flag avoids the uppercase word `FAILED`, which `slot_state` reads as "retry" (`daily.py:435`).
- The run report lists every degraded field; the job result carries them.

### 4.8 Audit
- Every refresh write is an `upsert_unit`: a `vault_writes` row with before/after and hashes, the unified diff in the run report (`cli.py:42-45`), `--dry-run` writes nothing (no file, no row).
- Volume: ≤21 firings × 2 units ≈ 42 rows a weekday; existing retention purge applies (`store.py:247`).
- Concurrency: the heartbeat, cards and daymode already write this note (`heartbeat/runner.py:205`, `aset/daily_note.py:185`, `daymode/note.py:159`); F5 will too. Writes go through `_write_with_retry` (`writer.py:559`), which re-reads on `NoteChangedOnDisk`.

## 5. Files touched (F4 only)
| File | Change |
|---|---|
| `src/cobalt/prefill/daily.py` | `run_daily_refresh()`; ownership (§4.4); stamp/flag line; degraded carry; public helpers for F5 (`daily_note_path`, `ensure_daily_note`, `format_stamp`) — seam doc §2 |
| `src/cobalt/prefill/cli.py` | `refresh` subcommand, `REFRESH_JOB` |
| `src/cobalt/prefill/config.py` | `DailyRefreshConfig` + loader |
| `src/cobalt/prefill/market.py` | docstring only: SLICE 2.1 VIX/BTC note superseded by Charter F4 |
| `configs/cobalt/prefill.yaml` | top-level `daily_refresh:` |
| `configs/cobalt/jobs.yaml` | row `com.cobalt.prefill-refresh` after `com.cobalt.prefill-daily`; add it to the `daily.md.j2` readers (`jobs.yaml:330-335`) |
| `configs/cobalt/taxonomy/tunables.yaml` | `prefill.refresh_interval_min`, `prefill.refresh_window` |
| `configs/cobalt/templates/daily.md.j2` | stamp lines in the two units; VIX/BTC `n/a (manual)` |
| `ops/com.cobalt.prefill-refresh.plist` | new |
| `tests/cobalt/test_prefill_refresh.py` | new (§7) |
| `tests/cobalt/test_prefill_daily.py` | template shape (stamp, VIX/BTC) |
| `tests/cobalt/test_finviz_consumers.py` | inventory strings for `prefill/market.py`, `prefill/calendar.py` (`:47-48`) name both jobs |
| DevDocs per changed `.py`, PDD for F4 | per `areas/cobalt.md:38` |

## 6. NOT in F4
- F5: the four checkpoints, Finviz context numbers, the narrative and its delta (Charter:89-93).
- Prebell tiles: regime, VIX3M/VIX, expected ranges, sector heatmap, ranked watchlist, archive tab (`INDEX.md:84-86`).
- Owning VIX/BTC (needs a source; stays `manual`).
- The rules, daymode, heartbeat, cards and DRC stub units; the Trade Ideas table.
- A sheet or voice button for the manual trigger (CLI only).
- Adding prefill to the L53 shared gate (§8 R4).
- Holiday awareness (the job fires on weekdays; a closed market shows stale-but-stamped numbers).

## 7. Tests (each shown red first where it guards new behaviour)
| # | Proves | Suite |
|---|---|---|
| T1 | Charter test: create 05:15; he writes in Game Plan and the VIX cell at 06:00; refresh at 08:45 with new prices → every byte outside the two units identical, VIX row identical, SPY/QQQ/IWM updated, a `vault_writes` row with the diff | with-DB (`cobalt_dev`) |
| T2 | He edits the SPY row at 06:00; refreshes at 06:15, 06:45, 08:45 → his row survives all three (red against a naive refresh on the 2nd) | with-DB |
| T3 | He inserts a line inside the trading unit → survives three refreshes | with-DB |
| T4 | He edits the calendar → unit byte-identical over three refreshes, flag `calendar human` | with-DB |
| T5 | Finviz down at refresh → previous values kept, `cobalt-degraded … values as of HH:MM`, no blank | offline |
| T6 | VIX/BTC blank → `n/a (manual)`; config `VIX: cobalt` refuses load | offline |
| T7 | Rules (ticked), daymode, a fixture `market_context` section, heartbeat unit → byte-identical after refresh | with-DB |
| T8 | Note absent → refresh creates it via the daily path | with-DB |
| T9 | On-disk SPY row equals an earlier Cobalt write (sync revert) → treated as Cobalt's, refreshed, no override | with-DB |
| T10 | Registry/plist parity; firings 05:45…15:45 every 30 include 08:45 | offline |
| T11 | `--dry-run` → no file change, no `vault_writes` row | with-DB |
| T12 | Refresh never calls `regenerate_rules_config` | offline |
| T13 | Stamp time is ET from `SessionClock` under a non-ET host zone | offline |
| T14 | `test_every_finviz_consumer_is_in_the_total_demand_inventory` stays green | offline |
| Live | `prefill refresh --dry-run` against his real notes, read-only (L68 GATE EARLY) | live-note |

## 8. Risks
- R1 · His edit erased on the 2nd refresh (§3). Designed out by §4.4; T2, T3, T4 guard it.
- R2 · Same-minute writes with F5 at 07:15/07:45/08:15/08:45 and with the heartbeat. Different units; `_write_with_retry` re-reads. T7 plus one concurrent-write test in F5's card.
- R3 · `prefill.yaml` is in `com.cobalt.aset`'s `reads` (`jobs.yaml:81`): the F4 deploy (and F5's) restarts the sheet he trades beside. Lawful at any hour (L43, LAWS:255, R389); the restart is derived (L42) and the deploy card names it.
- R4 · L53 total demand: refresh adds ~3 Finviz requests per 30 min outside the shared gate, the known gap (`test_finviz_consumers.py:69-75`, strict xfail). Adding a `prefill` consumer to `scheduled_consumers` would sum with radar's ceiling-bound rpm (`radar/notes.py:358-363`) and refuse the radar; it is left out and the inventory strings name the new job.
- R5 · He edits the stamp line: Cobalt replaces it next refresh (one override row). Accepted.
- R6 · Notes created before deploy: their units get the stamp line at the first refresh, inside the markers only.
- R7 · `market.py:7-11` (08-31) says no `n/a (manual)`; the Charter (09-04, ratified) says loud `n/a (manual)`. The Charter governs; the docstring is updated.

## 9. Open choices — each takes its default
| # | Choice | Default | Reason |
|---|---|---|---|
| C1 | Refresh as new job + `refresh` subcommand, or reuse `daily` on an interval | New job + subcommand | A schedule is one form (`jobs/config.py:92-96`); 05:15 keeps its zero-diff idempotency |
| C2 | Cadence | 30 min, 05:45-15:45 ET, weekdays, tunables `source: dwv` | Hits 08:45 (the Charter test) and the M3 times; "all day" through RTH; ~0.1 rpm |
| C3 | Units refreshed | trading + market_calendar | Rules are his ticked boxes; daymode has its own writer; F5 owns market_context |
| C4 | Human detection | baseline + recent_afters + overrides_for; per row (table), whole unit (calendar) | §3 makes the merge alone unsafe for a repeating writer; existing public store reads, no `writer.py` change |
| C5 | VIX/BTC | `n/a (manual)` in blank cells; owner map in `prefill.yaml` | Charter F4 and the frontier law (Charter §1) |
| C6 | Stamp place and zone | First line of each refreshable unit, ET via SessionClock | GFM table rendering; F1 forbids wall-clock keys |
| C7 | Refresh on a dead source | Keep last values, flag `cobalt-degraded` with their age | A FAILED cell over a good number is less true |
| C8 | Refresh with no note | Create via the daily path | M1 says the note exists; a failed 05:15 should not leave the day blank |
| C9 | L53 shared gate | Not extended; inventory text updated | R4 |
| C10 | Manual trigger surface | CLI `uv run prefill refresh` | Charter asks "manual trigger"; a button is new surface |
| C11 | Rules unit stamp | None | No data age |
| C12 | Build seat | Opus 5.5 | Vault write path (L29, BUILD-HUB:3); house B mandatory at check (L67, his notes) |

## 10. L52 / owner items
- L52: not triggered; F4 scores and ranks nothing.
- Owner items: none. No field he owns changes; his Charter text is untouched; the cadence is a dwv value he may veto.
