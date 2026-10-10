BLIND: I did not read the houses' round-3 folder or the hub's round-3 report.
RUN DATE: Sat Oct 10 17:00:14 EDT 2026

## DIGEST FOR THE DESK
- Closing line: `TRIBUNAL R3: ADOPT AFTER R2-4 per-run gate without derived interval; R2-7 template-body baseline-guarded stub fill`
- R2-4 · ADOPT WITH. Strike-loop gating stands. Two clauses are replaced. (1) There is no derived interval: launchd fixes the schedule at install, and `poll_interval` never refuses a 3-request burst. (2) rpm = the run's 3 unpaced requests, never 3/30.
- R2-4 (i) headroom = `radar.finviz_max_rpm` (50) − the radar's planned rpm (`notes.py:634-635`). It is a plan figure, not a measurement (X8). (ii) `prefill.refresh_interval_min` IS the schedule; nothing is derived. (iii) Unreadable plan → radar counted at the ceiling → refused, no request, degraded, exit 1.
- R2-7 · ADOPT WITH. Settled scope, two units only. Bodies come from the template unit (stamp, separator, VIX/BTC `n/a (manual)`), not the three bare rows at `daily.py:336-340`. A unit is filled only when it has no baseline. His unmarked table is skipped.
- R2-7 narrows one folded sentence of [F-26]: `baseline_missing` applies to a unit present on disk.
- Experiments: keep X1–X13. X6 and X13 change. New: X14 (strike + refresh in one minute), X15 (stub fill shape and baseline).
- Owner items: none.
- WITHDRAWN: none. ESCALATE: 1 (the rules input for [F-08]'s absent-note create is unnamed; R2-F26 latent).
- Conflict (L26): my round-2 R2-7 wording filled all four `SLOT_SPECS` units. R931's settled scope is two units; I take it and keep only my baseline guard. My round-2 R2-4 form stands on the files, with the interval clause of the round-3 form replaced.

## Rulings

### R2-4 · C9: the FORM of the refresh's place in the shared Finviz gate
**ADOPT WITH** the wording below. It replaces §6's bullet "Adding prefill to the L53 shared gate", §8 R4, SEAM §7, the `demand-model / admission call sites` row of §5, §9 row C9, the L53 line of `## The bar`, and the clause "(X13 if R2-4 closes on inclusion)" in `## CHUNKS` (X13 now gates unconditionally):
> "Refresh is counted in the ONE shared gate before any Finviz request, the way the strike loop is (`strike/detector.py:111-117`, `:273-279`). It is never listed in `scheduled_consumers` (`radar/notes.py:329-381`), because that list also feeds the radar's own admission (`radar/notes.py:440-449`, `:682`): refresh's demand never refuses the radar. Every run calls the gate first: scheduled, manual, `--dry-run`, the [F-08] absent-note create and the §4.1 stub fill. The call is `check_scheduled_demand("prefill-refresh", radar_rpm=configured_sources().planned_rpm, extra=[DemandConsumer(name="prefill-refresh", rpm=3.0, window=DemandWindow.from_at(<run start, ET HH:MM>, 300), basis="3 unpaced requests in one run (1 screener + 2 calendar)")])` (`radar/notes.py:384-391`, `:192-194`, `:203-215`). 300 is the job's `timeout_s` (§4.2).
> The rpm is the run's whole request count (`daily.py:509`, `:517-518`), because `prefill/market.py:66-67` and `prefill/calendar.py:52` send with no bucket (`test_finviz_consumers.py:47-48`): all three requests can fall in one minute. It is never `3 / prefill.refresh_interval_min`, which understates that minute by a factor of thirty.
> Refresh derives no interval and does not call `poll_interval` or catch `IntervalRefused`. The schedule is the plist's `StartCalendarInterval` list, expanded from `prefill.refresh_interval_min` at install and parity-tested (`jobs/config.py:198-222`). A one-shot cannot re-time itself; the per-run gate is the headroom test.
> The run makes no request when the gate raises `TotalDemandExceeded` or `RadarNoteError`, or when `configured_sources()` raises anything (caught as `strike/detector.py:167-172` catches the plan read). It then takes the [F-28] degraded path with reason `demand refused` or `radar plan unreadable`, keeps the last good values, and exits 1. An unreadable plan (`planned_rpm` None, `radar/notes.py:411-422`) counts the radar at the ceiling (`radar/notes.py:357-362`), so the gate refuses. An unmeasured ceiling refuses too (`radar/notes.py:279-280`).
> `radar.finviz_max_rpm` and the scan cadence are not edited.
> Named residual, not fixed by F4: refresh and the strike loop are each passed as `extra`, so neither counts the other. The strike loop sizes itself to up to the whole headroom (`strike/detector.py:103-108`, `:115`), so a minute with ARMED cards can exceed the ceiling by refresh's 3 requests. That gap is the owed cross-process gate (`test_finviz_consumers.py:5-6`). Its strict xfail (`:69-75`) stays, because `prefill/market.py` is still unbucketed. X14 measures it.
> Tests (offline):
> - Radar planned 48, fixture ceiling 50, refresh rpm 3 → `TotalDemandExceeded`; with radar planned 0, refresh passes (L53's refusal test).
> - A refused run sends no request (the fetchers are faked to fail if called) and records `exit_code=1`.
> - `planned_rpm` None → refused, no request.
> - `test_finviz_consumers.py:47-48` name `com.cobalt.prefill-refresh` and its gate.
> Price: ~20 lines in `daily.py`, 3 tests, 2 strings. No change to `radar/notes.py` or `strike/`."

- (i) The headroom is `radar.finviz_max_rpm` (50, `tunables.yaml:702-703`, a ruled value per R2-F9) minus the radar's planned steady rpm. That rpm is `plan_transport_demand`'s `steady` (`radar/notes.py:634-635`, set at `:436`), the same `headroom_rpm` the strike loop reads (`strike/detector.py:319`). The archiver window (20:30–21:10) and replay (from 21:10) (`jobs.yaml:214-233`) overlap no refresh window (05:45–15:50). So the gate's peak at a refresh is planned + 3, admitted only when headroom ≥ 3. It is a plan computed from his radar notes, not a measured rate: X8 measures the real per-minute demand.
- (ii) `prefill.refresh_interval_min` (engine tunable, proposed 30, `status: proposed`) IS the schedule. It is neither a floor nor replaced, because no interval is derived. Its value is set by X8.
- (iii) Unreadable plan: the radar is counted at the ceiling (`radar/notes.py:357-362`, FC30) → `TotalDemandExceeded` → no request, `cobalt-degraded (radar plan unreadable; values as of <last success>)`, exit 1, on every run until the plan reads.
- Defect in the form's "interval derived from the measured headroom" (failing sequence): radar planned 49.0, ceiling 50, headroom 1.0. `poll_interval(3, 1.0, 1800)` = max(1800, ⌈180/1.0⌉) = 1800 → no `IntervalRefused`. Refresh sends 3 requests at 08:45, and that minute carries 49 + 3 = 52 > 50. The gate with rpm 3 refuses: 52 > 50.
- Defect in rpm = `3/30` (Grok's round-2 conversion, derive `:41`): radar planned 47.5. 47.5 + 0.1 = 47.6 is admitted, but the 08:45 minute carries 47.5 + 3 = 50.5 > 50.
- `poll_interval` with a floor of `interval×60` returns the floor whenever headroom > 0.1 (3×60/1800), so it decides nothing that the gate does not.
- Reading of the code: the plist is fixed at install (`jobs/config.py:202-206`, "the test suite compares this list against the plist's own array"). An interval derived per run cannot reach launchd.
- Scenario for (iii) from the files: his radar lists note fails to parse. The radar still runs on a valid pool (`radar/notes.py:417-419`), but `planned_rpm` stays None, so every refresh that day is refused and degraded, exit 1. That is loud (L1, L9), not silent. Whether that day is acceptable is measured by X13's variant, not argued.

### R2-7 · C8: a clean wording of the stub-note scope
**ADOPT WITH** the wording below. It replaces §4.1's `OPEN AFTER ROUND 2 (R2-7)` paragraph (both quoted positions included), SEAM §6's "what refresh adds to a stub is **OPEN (R2-7)**", and T8's "the stub case **OPEN (R2-7)**":
> "Stub note. Today's ET note may exist with a refreshable unit absent from it: `trading/market_table` or `market_calendar/market_calendar` with `slot_state(...) == "absent"` (`daily.py:412-435`). The sheet's stub has neither (`aset/daily_note.py:103-104`, `:184`). In that case refresh fills that unit once and writes nothing else. It calls neither `run_daily_prefill` nor `regenerate_rules_config`, writes no `rules` or `daymode` unit (§4.3), and renders no template over the file: the stub-upgrade branch is deleted (`daily.py:14-24`), and `create_if_absent` on an existing file writes nothing (`writer.py:597-607`).
> A unit is filled only when the store holds no baseline for it in this note (`VaultWriteStore.last_after(note, section, unit) is None`, `store.py:91-97`). An absent unit WITH a baseline was removed by him. It is not recreated, neither by this fill nor by `upsert_unit`'s section append (`writer.py:722-741`), and the run report names it.
> The two bodies need no rules read, and they do not go through `build_slot_contents` (`daily.py:207-234`, which takes `rules_cfg`). Their only inputs:
> - this run's gated fetches (R2-4): `fetch_market_table` (`daily.py:509`), `fetch_economic_events` and `fetch_earnings_events` (`daily.py:517-518`);
> - the formatting of those results by `format_market_row` (`daily.py:107-116`) and `format_calendar_block` (`daily.py:119-144`);
> - `format_stamp(when)` ([F-31]).
> Each body is the unit body the [F-08] create renders: `_render_template` (`daily.py:237-240`) runs on a context holding only those values, and the unit is taken from the rendered text with `find_section` (`vaultwrite/markers.py:114`). So the filled unit carries the §4.5 stamp line, the separator, and the VIX/BTC rows with `n/a (manual)` (§4.6). `build_market_table_body`'s no-table branch is not used: it renders three bare rows, with no separator and no VIX/BTC rows (`daily.py:336-340`).
> Each fill is one `upsert_unit` at the slot's placement (`TRADING_PLACEMENT` `daily.py:297`, `MARKET_CALENDAR_PLACEMENT` `daily.py:313-315`). The sheet's stub has neither heading, so both sections append at the end of the note and nothing above them is touched (`writer.py:722-741`).
> Content already under a heading is his and is never wrapped:
> - A pipe table under `### Trading` that carries no markers (`_trading_table_span`, `daily.py:276-294`, not None) skips the trading fill.
> - Text of his under `### Market Calendar:` skips the calendar fill (`calendar_body_is_available`, `daily.py:318-325`; the rule of `daily.py:578-582`), and the trading stamp line then reads `calendar human`.
> Each skip is named in the run report and is not a degradation.
> A fetch that is refused or fails writes nothing to the unit it feeds; the run exits 1 ([F-28]), and the next run fills it.
> A unit already present is not filled; it takes §4.4 in the same run. A filled unit is not refreshed again in that run.
> The fill's write stores its body as the unit's baseline (`writer.py:774-795`, `unit_after = merged_body`), so the next scheduled refresh finds `last_after` and takes the §4.4 path.
> Price: ~25 lines in `daily.py`; 0 new files; 0 migrations."
>
> Consequent narrowing of [F-26] (its sentence "If `last_after` is None, write nothing and exit 1, `FAILED: baseline_missing`."). Replace that sentence with: "If `last_after` is None for a unit present on disk, write nothing to it and exit 1, `FAILED: baseline_missing`. A unit absent from disk takes §4.1's stub fill." Read literally, the folded sentence exits 1 on every stub, because a stub's units have no baseline. That contradicts the settled scope.
>
> T8 (replacing its stub clause): "the sheet's stub (banner plus a cards unit) → after one refresh, both units are appended at the end with the stamp line, the separator and VIX/BTC `n/a (manual)`; the stub and cards bytes are unchanged; there is no `rules` or `daymode` unit; `regenerate_rules_config` is not called; the next refresh takes §4.4. The trading unit deleted with a baseline on record → not recreated. A hand-typed table under `### Trading` in a stub → not wrapped; his bytes are unchanged."

- (a) The scope is as R931 settled it: two units, `upsert_unit` at their placements, the stub untouched. (b) Inputs: the three gated fetches and their formatters (cited above); no rules read. (c) `daily.py:14-24`. (d) A present unit takes §4.4; his content under a heading is skipped (`daily.py:578-582`'s rule, extended to `### Trading`). (e) The fill seeds the baseline (`writer.py:795`), so the next run takes §4.4.
- Defect in the round-2 wording's body (failing scenario): the 05:15 run fails. At 06:00 he grades a card and the sheet writes the stub plus the cards unit. A 06:15 fill through `build_market_table_body` (`daily.py:566`) finds no table and writes three bare rows `| SPY | $500.12 | +0.34% |` … with no separator and no VIX/BTC rows (`daily.py:337-340`). That unit becomes the baseline. §4.4 never re-emits a ticker line absent from `last_after` ([F-26]), so VIX/BTC `n/a (manual)` never appear that day, against Charter:82-87 ("VIX/BTC show a loud n/a (manual)").
- Defect in "upsert at their placements" with no guard, for an unmarked table: he types `### Trading` and `| SPY | 500 | |` into the stub at 06:00. At 06:15 `TRADING_PLACEMENT` wraps his lines (`daily.py:297`) as `seed`, and `merge3(seed, seed, cobalt)` (`writer.py:733-735`) has base == human, so Cobalt's body wins and his 500 is gone in one write (`merge.py:15`, folded §3). The skip prevents it.
- Defect with no baseline guard: at 10:00 he deletes the trading unit, markers included. At 10:15 it is absent, and the round-2 wording re-adds it every 30 minutes, against L28 human-wins.

## Self-attack
Greps run over `/Users/cobalt/cobalt/src/cobalt` plus `tests`, `configs` and `ops` where named. W = writer, R = reader / caller.
- `poll_interval` (strike): def `strike/detector.py:103`; R `detector.py:274`; tests `test_strike_detector.py:32`, `:129-134`, `:155`. `radar.poll_interval` is a different key (`radar/notes.py:399`, `:677`). `strike.poll_interval_min`: `strike/config.py:17`, `:30`, `:59`; `measure.py:163-164`, `:178`; `tunables.yaml:735` (value 2). F4 calls none of them.
- `IntervalRefused`: def `detector.py:99`; raised `:105`; caught `:276`; test `test_strike_detector.py:133`. F4 does not use it.
- `check_strike_demand`: `detector.py:111`, `:275`; tests `test_strike_detector.py:138`, `:142`. Untouched.
- `check_scheduled_demand`: def `radar/notes.py:384`; R `archiver/runner.py:119`, `:135`; `replay/movers.py:356`, `:387`; `strike/measure.py:175`; `strike/detector.py:117`; tests `test_replay_demand.py:152-154`, `test_replay_movers.py:593`. F4 adds one caller (`prefill-refresh`).
- `check_total_demand`: def `notes.py:276`; R `notes.py:391`, `:446`; `radar/propose.py:632`; tests `test_replay_demand.py`. Unchanged.
- `scheduled_consumers`: def `notes.py:329`; R `notes.py:390`, `:682` (the radar's own admission), `radar/propose.py:638`; tests `test_replay_demand.py:54`, `:114-210`. F4 adds no entry. That is why refresh never reaches `:446`.
- `DemandConsumer`: def `notes.py:203`; built at `archiver/runner.py:131`, `radar/propose.py:634`, `notes.py:359`, `:367`, `:380`, `:440`, `strike/measure.py:172`, `strike/detector.py:115`. F4 builds one as `extra`.
- `radar_window`: `notes.py:294`, `:360`, `:681`; `propose.py:635`; `strike/measure.py:172`; `strike/detector.py:115`. Refresh does not use it: its window is `DemandWindow.from_at` (`notes.py:192`).
- `headroom_rpm`: `notes.py:604`, `:656`; `propose.py:701`; `strike/detector.py:85`, `:104`, `:274`, `:319`; tests. F4 reads none of them; the gate computes the same quantity.
- `planned_rpm`: `notes.py:60`, `:436`; `radar/runner.py:359`, `:485`; `radar/sources.py:133`, `:147`; `strike/measure.py:133-137`; `strike/detector.py:84`, `:319`. F4 reads `configured_sources().planned_rpm`.
- `refresh_interval_min`, `daily_refresh`, `prefill-refresh`, `prefill_refresh` (src, configs, ops, tests): no committed file carries them.
- `upsert_unit(` W: `drc/build.py:905`, `prefill/trade_note.py:474`, `:522`, `prefill/daily.py:583`, `daymode/note.py:159`, `heartbeat/runner.py:205`, `taxonomy/cli.py:225`, `:516`, `taxonomy/catalyst.py:404`, `taxonomy/note_migration.py:872`, `:880`, `replay/line.py:223`, `radar/propose.py:756`, `aset/daily_note.py:185`, `seatusage/runner.py:126`. Only `daily.py:583` writes `trading` or `market_calendar`.
- `create_if_absent(` W: `drc/build.py:899`, `prefill/trade_note.py:265`, `prefill/daily.py:548`, `taxonomy/cli.py:515`, `radar/propose.py:753`, `aset/daily_note.py:184` (the stub), `seatusage/runner.py:107`; def `writer.py:588`.
- `slot_state`: `daily.py:412`, `:496`, `:574` only.
- `SLOT_SPECS`: `daily.py:463`, `:496`, `:502`, `:552`, `:573` only. The stub fill does not iterate it (two units only).
- `TRADING_PLACEMENT` / `MARKET_CALENDAR_PLACEMENT`: `daily.py:297`, `:313`, `:471-472` only.
- `load_rules_config`: def `prefill/config.py:130`; no src caller (`rules_gen.py:7` is a docstring); tests `test_prefill_config.py`, `test_prefill_rules_gen.py:139-153`. The stub fill does not use it.
- `RULES_CONFIG_PATH`: `config.py:17`, `:48`, `:131-139`; `rules_gen.py:155` (comment); tests `test_prefill_rules_gen.py:150-185`.
- `stub_template`: `aset/daily_note.py:103`, `:184` only.
- `regenerate_rules_config`: def `rules_gen.py:128`; R `daily.py:71`, `:482`, `prefill/drc.py:79-82`; tests `test_prefill_daily.py:172`, `test_drc_d3_fix_r1.py:30-40`, `test_prefill_rules_gen.py`, `test_jobs_restarts.py:222-225`. Refresh never calls it.
- `run_daily_prefill`: `daily.py:476`, `prefill/cli.py:25`, `:35`; tests `test_prefill_daily.py:234-425`. Refresh never calls it.
- `prefill.yaml`: `prefill/config.py:29`; `jobs.yaml:81` (aset reads); docstrings `smoke/checks.py:124`, `drc/template.py`, `replay/line.py:207`, `taxonomy/trade_note_migration.py:55`. Neither ruling here touches it.
- Also: `build_market_table_body` (`daily.py:328`, `:566`; no test of its no-table branch), `calendar_body_is_available` (`daily.py:318`, `:578`), `format_market_row` / `format_calendar_block` (`daily.py:107`, `:119`, `:220-233`; tests `test_prefill_daily.py:60-83`), `_render_template` (`daily.py:237`, `:548`; `test_drc_settings.py:334`), `last_after` (`store.py:91`).

Walking my text against this list:
- "refresh's demand never refuses the radar": refresh is absent from `scheduled_consumers` and the radar's admission reads only that list (`notes.py:682`, `:443-446`). Holds.
- "the strike loop sizes itself to up to the whole headroom": interval = max(2, ⌈names×60/h⌉) (`detector.py:108`), so rpm = names×60/interval ≤ h. Holds as "up to".
- "archiver and replay overlap no refresh window": `jobs.yaml:219-233` gives 20:30–21:10 and from 21:10; refresh runs 05:45–15:50. Holds.
- "the fill's body becomes the baseline": `writer.py:795` stores `merged_body`. That `merge3([], [], body)` returns exactly `body` at an end-of-note append is merge behaviour I did not read in `merge.py` → X15, not a fact.
- "`_render_template` on a partial context renders the missing keys empty" is jinja behaviour → X6 (already the draft's), not a fact.
- My round-2 R2-7 wording ("fills each `SLOT_SPECS` unit that is absent AND has no baseline") reaches `rules` and `daymode` (`daily.py:463-473`). R931 excludes them. This report does not repeat it.
- WITHDRAWN: none.

## Experiments (L70)
- Keep X1–X5, X7, X9–X12 as drafted.
- X6 (change): add the stub fixture's assertions from T8 above. Also record whether `_render_template` with a context holding only the market, calendar and stamp keys renders a trading unit byte-equal to the 05:15 create's for the same values. If it is not byte-equal, the stub body source changes (it then becomes the create's own rendering).
- X8 (keep): add per-minute counts at the transport for 05:45–15:50 with the radar at its planned rate, and the redirects of `follow_redirects=True` (`prefill/market.py:66`, `calendar.py:52`). If a run sends more than 3 requests, rpm 3 changes to the measured count.
- X13 (change: it now gates unconditionally): dev tunables with `radar.finviz_max_rpm` 50 and a radar plan at 47.5 planned rpm → refresh is refused with no HTTP request, and `configured_sources()` shows the radar NOT refused (`pool_error` None). Variant: the lists note unparseable → `planned_rpm` None → refresh refused and degraded, exit 1. Either the radar refused, or refresh admitted at planned 47.5 → R2-4's wording is wrong.
- X14 (new): dev, 5 synthetic ARMED cards, radar planned 40, ceiling 50, a refresh fired at the strike loop's steady state. Count requests per wall-clock minute at the transport and record any 429. Any minute above 50, or a 429 → the named strike/refresh residual cannot ship as named, and the derive puts a strike-side reservation row on the F4 card (L75) before the scheduled writer loads.
- X15 (new): dev vault copy, the synthetic stub (`stub_template` plus one cards unit). Run refresh twice. Pass: after run 1, both units are appended with the stamp, separator and VIX/BTC `n/a (manual)`, and `last_after` equals the written body; run 2 takes §4.4 (no second append, no `baseline_missing`). Then delete the trading unit and refresh: not recreated. Then a stub with a hand-typed `### Trading` table: its bytes are unchanged. Any failure → R2-7's wording returns to the derive.

## OWNER (after the tribunal)
none. R2-4 leaves his ceiling and scan cadence unedited (L53); `prefill.refresh_interval_min` is an engine tunable set by X8. R2-7 is a write-path mechanism the houses settle. Neither is his money, his data, his laws or his trading judgement in a way no house can decide.

## WRONG FACTS
- FINAL SEAM §7 (`F4-FINAL-2026-10-10.md:271`): "Whether either is counted in the shared gate (`radar/notes.py:357-363`)". Lines `:357-362` are `scheduled_consumers`' ceiling fallback for the radar's rpm. The shared gate is `check_total_demand` (`radar/notes.py:276-284`), called through `check_scheduled_demand` (`:384-391`).
- FINAL §4.4 [F-26] (`F4-FINAL-2026-10-10.md:66`): "If `last_after` is None, write nothing and exit 1". Read literally, it fires on every stub unit, against the settled R2-7 scope: a stub unit has no baseline (`store.py:91-97`; `aset/daily_note.py:103-104` writes no unit). Narrowed above.
- Derive `## FOR DEJAN` (`f4-tribunal-r2-derive-2026-10-10.md:76`): "In Grok's form, refresh fetches nothing at all until a measurement (X8) shows room". That is Grok's round-2 form, now superseded by R931's strike-loop form, under which refresh fetches whenever the plan leaves ≥3 rpm (`radar/notes.py:276-284`). This is not a file contradiction, only a stale description for the derive to drop.

## READING
- `279-f4-tribunal-r3-opus-seat.md` (whole). `278-f4-tribunal-r3.md` lines 16-18, 26-31, 35-53 (question set and §1 staging only).
- LAWS.md 1-140, 190-399.
- `F4-FINAL-2026-10-10.md` 1-304.
- `f4-tribunal-r2-derive-2026-10-10.md` 38-85 (`## OPEN AFTER ROUND 2`, `## OWNER ITEMS`, `## FOR DEJAN`).
- `f4-tribunal-r2-2026-10-10.md` rows R2-F7–R2-F10, R2-F22–R2-F26, FC27–FC30 (lines 168-171, 183-187, 205-208).
- `f4-tribunal-r2-opus-2026-10-10.md` 63-128.
- `cto-2026-10-10.md` rows R849, R860, R903, R917, R920, R931, R949. `cto-2026-09-22.md` R109. `cto-2026-09-23.md` R95, R97.
- Code (all unchanged since `d0a5fbb8`: `git log d0a5fbb8..HEAD` over the paths printed nothing):
  - `strike/detector.py` 1-40, 80-129, 150-179, 250-329.
  - `radar/notes.py` 180-459, 596-690.
  - `tests/cobalt/test_finviz_consumers.py` 1-175.
  - `jobs/config.py` 55-139, 196-230.
  - `prefill/market.py` 53-74.
  - `prefill/daily.py` 1-40, 100-147, 205-364, 400-595.
  - `aset/daily_note.py` 60-199.
  - `templates/daily.md.j2` (whole).
  - `vaultwrite/writer.py` 586-800.
  - `prefill/config.py` 25-144.
  - `tests/cobalt/test_prefill_daily.py` 345-384.
- Searches:
  - the authorization greps and git logs;
  - the 23 self-attack greps above;
  - tunables keys (`premarket_open`, `aftermarket_close`, `finviz_max_rpm`, `strike.*`);
  - `jobs.yaml` archiver/replay rows;
  - `calendar_entries`;
  - the prefill fetch sites;
  - `STUB_BANNER`;
  - `markers.py` defs;
  - `store.py` `last_after`;
  - `git -C /Users/cobalt/cobalt log --oneline -3 main` (`0f1e76e9`).

## L74
No tool result in this run carried an instruction block. A session-level reminder asked for commit attribution lines. This seat makes no commit, so nothing was acted on. Recorded once.

## ESCALATE
1. For the derive, not an owner item: [F-08] and [F-31] create an absent note through "the shared create-if-absent rendering with validated read-only inputs", but no file names the read-only rules input. The only read-only loader, `load_rules_config()`, is env-blind (`prefill/config.py:130-139` against `:37-48`, R2-F26 HOLDS), so a builder reaching for it reads production `rules.yaml` in a dev run. The derive should name the input (a read-only parse of `Rules.md` split from `regenerate_rules_config`, `rules_gen.py:128`, or another), within the folded paragraph's scope.

## CONTINUE
next: none. Run complete 17:08 ET (`date`). MEASURE: tokens UNMEASURED; the session counter fell from 15,000,000 to ≈14,763,000 (≈237k cumulative across turns).

F4 TRIBUNAL R3 OPUS DONE · verdict: ADOPT AFTER R2-4 per-run gate without derived interval; R2-7 template-body baseline-guarded stub fill · adopt: 0 · adopt with wording: 2 · reject: 0 · ESCALATE: 1 · tokens: ≈237k (session counter, unmeasured)
