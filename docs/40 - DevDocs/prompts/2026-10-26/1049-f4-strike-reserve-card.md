JOB: f4-strike-reserve
LADDER: S5-P2 · F4
CLASS: K2
INSTALL: none
BRANCH: ops/f4-strike-reserve
WORKTREE: f4-strike-reserve
BASE: 05366873
TIP:
REPORT: /Users/cobalt/cobalt-wt/f4-strike-reserve/docs/40 - DevDocs/reports/f4-strike-reserve-build-2026-10-26.md
CHECK REPORT:
HOUSE B:
BAND: HIGH
RULINGS: 2026-10-18 R1863

## ROWS

WHY: FINAL `docs/30 - Design/F4-FINAL-2026-10-10.md:221` (X15): a minute above 50 or a 429 when the strike loop and a refresh share a minute → "a strike-side reservation row on the F4 card before the scheduled writer loads". Today each is `extra` to the gate and neither counts the other (`:315`): the strike loop derives its interval from the radar's whole headroom (`src/cobalt/strike/detector.py:274`, `poll_interval` `:103-108`), and refresh is shown to the gate at its average, `3 / prefill.refresh_interval_min` (form B, `:286`; `prefill/daily.py:759-777`), while its 3 GETs fall in one minute. This job makes the strike loop reserve refresh's one-minute burst inside `prefill.refresh_window`. LAUNCH GATE (brain R2465 of `reports/cto-2026-10-26.md`): launched only on `PROBE X15 FAIL` from `prompts/2026-10-26/1045-f4-gate-run.md` SECOND PASS; dropped if X15 is `OK`. Every `file:line` is `main` at BASE; re-find each place by content before the edit (BUILD-HUB E3). Test rule (brain R1472). Constructed values only (L32).

| row | what | red first | files |
|---|---|---|---|
| S1 | THE RESERVATION. `strike/detector.py` gains `REFRESH_BURST_RPM = 3.0` (refresh's GETs in its one minute; pinned equal to `cobalt.prefill.daily.REFRESH_GETS`, `prefill/daily.py:682`, by a test, never by an import in `strike/`: `strike/` imports no `cobalt.prefill` module today) and `refresh_reservation(now) -> Optional[DemandConsumer]`: reads `prefill.refresh_window` from `load_tunables()` and parses it with `parse_window` (`jobs/config.py:34`); `now` in ET inside the window (both ends included) → `DemandConsumer(name="prefill-refresh-burst", rpm=REFRESH_BURST_RPM, window=DemandWindow.between(<opens>, <closes>), basis="refresh's 3 GETs in one minute, reserved by the strike loop (F4-FINAL :221)")` (`radar/notes.py:173-190`); outside → `None`. The tunable missing or `None` → `RadarNoteError` naming it (an unreadable reservation is no GET, as an unreadable plan is, `:167-172`) | OFFLINE NEW `tests/cobalt/test_strike_detector.py::test_the_refresh_reservation_is_three_rpm_inside_the_refresh_window_only` (05:44 ET → `None`, 05:45 → 3.0, 10:00 → 3.0, 15:45 → 3.0, 15:46 → `None`, on constructed EST and EDT days); `::test_the_reservation_equals_refreshs_gets` (`REFRESH_BURST_RPM == cobalt.prefill.daily.REFRESH_GETS`); `::test_a_missing_refresh_window_tunable_makes_no_fetch`. RED on BASE: `AttributeError: module 'cobalt.strike.detector' has no attribute 'refresh_reservation'` | `src/cobalt/strike/detector.py`, `tests/cobalt/test_strike_detector.py` |
| S2 | THE INTERVAL AND THE GATE. In `tick` (`:238-310`), before `poll_interval` (`:274`): `reserve = refresh_reservation(now)`; the interval is `poll_interval(len(watched), headroom_rpm - (reserve.rpm if reserve else 0), floor)`, and `check_strike_demand` (`:111-117`) gains keyword `extra=()` passed on to `check_scheduled_demand` after the strike consumer, called with `(reserve,)` when `reserve` is not `None`. `RadarNoteError` from S1 joins the existing refusal (`:276-279`: `report.refused`, no GET). Outside the window the interval is today's | OFFLINE NEW `::test_inside_the_refresh_window_five_names_with_radar_40_poll_every_43_s` (plan `DemandPlan(40.0, 10.0)`, 10:00 ET: `interval_s == 43`, the gate's counted consumers hold `prefill-refresh-burst`, peak ≤ 50); `::test_outside_the_refresh_window_the_interval_is_unchanged` (17:00 ET, same plan: `interval_s == 30`, no `prefill-refresh-burst`); `::test_a_reservation_that_leaves_no_headroom_makes_no_fetch` (plan `DemandPlan(47.5, 2.5)` at 10:00 ET: `report.refused`, no fetch). EDIT `::test_with_the_radar_at_30_rpm_five_names_poll_every_15_s` (`:145-151`): its clock is 10:05 ET (`:36`, `:107`), inside the window, so headroom 20 − 3 = 17 gives 18 s; renamed `…_poll_every_18_s_inside_the_refresh_window` with `18`, and a twin at 17:00 ET keeps `15`. RED on BASE: `interval_s == 30`, not 43 | `src/cobalt/strike/detector.py`, `tests/cobalt/test_strike_detector.py` |
| S3 | THE INVENTORY. `tests/cobalt/test_finviz_consumers.py::test_every_finviz_consumer_is_in_the_total_demand_inventory` (`:66`) still green; if it lists consumer names, `prefill-refresh-burst` is named as the strike loop's reservation, not a new transport consumer | the existing test, quoted | `tests/cobalt/test_finviz_consumers.py` (only if it lists names) |
| R1 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`, the table WHOLE; the tool's last line is the record | — (tool output quoted in the report) | none |
| D0 | THE MODULE DOCS. One dated section `## 2026-10-26 — f4-strike-reserve` in `docs/40 - DevDocs/cobalt/strike/detector.md` (the reservation, its window, the interval it gives), appended after the file's last section, found by content | the symbol-check gate, if it asks | `docs/40 - DevDocs/cobalt/strike/detector.md` |

ORDER: S1, S2 (each red, then green), S3, the card's offline suite `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_strike_detector.py tests/cobalt/test_radar_runner.py tests/cobalt/test_finviz_consumers.py tests/cobalt/test_prefill_refresh.py` (whole, quoted, `0 failed`), D0, the commit, R1, the `## DEPLOY PROOF` reads on the tree, the three suites (BUILD-HUB `## W`), the stop line.

## NOT IN THIS JOB
- Launching before `PROBE X15 FAIL` is recorded in `reports/f4-gate-run-2026-10-26.md` (brain R2465).
- The refresh side: `prefill/daily.py` and its form-B gate call (`:780-797`) unchanged (R771); `prefill.refresh_interval_min`, `prefill.refresh_window` and the plist unchanged.
- `radar/notes.py`, the radar's own admission, `strike/measure.py`, `strike/config.py`, `configs/cobalt/taxonomy/tunables.yaml`.
- A new tunable for the reservation: the 3 is refresh's GET count, pinned by test (S1).
- Loading `com.cobalt.prefill-refresh`; any `launchctl`; any production command or database; a live Finviz GET.
- A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with its output; never fixed here.

## READ
- `docs/30 - Design/F4-FINAL-2026-10-10.md:221` (X15), `:285-286` (form B), `:315`.
- `src/cobalt/strike/detector.py` whole; `src/cobalt/radar/notes.py:173-190` (`DemandWindow`), `:276-391` (the gate); `src/cobalt/jobs/config.py:34` (`parse_window`); `src/cobalt/prefill/daily.py:680-797`.
- `tests/cobalt/test_strike_detector.py:1-170`; `tests/cobalt/test_radar_runner.py:609-660` (the strike thread's interval).
- The X15 probe line and its clause in `reports/f4-gate-run-2026-10-26.md` (pass 2).

## CHECK ASKS
- X1 Is the reservation applied only inside `prefill.refresh_window` in ET, both ends included, and is the interval outside it byte-for-byte today's?
- X2 With radar planned 40, ceiling 50 and 5 names, is the worst minute radar + strike + 3 ≤ 50 (43 s → 6.98 rpm)?
- X3 Does an unreadable `prefill.refresh_window` make no GET, as an unreadable plan does?
- X4 Does `strike/` import any `cobalt.prefill` module (it must not)?
- X5 RESTARTS re-derived: `com.cobalt.radar` (the strike loop runs in the radar resident)?

## DEPLOY PROOF
- `grep -c -F "def refresh_reservation(" /Users/cobalt/cobalt/src/cobalt/strike/detector.py` · before `0` · after `1`
- `grep -c -F "REFRESH_BURST_RPM = 3.0" /Users/cobalt/cobalt/src/cobalt/strike/detector.py` · before `0` · after `1`
- the strike detector is on the restarted tree · `grep -c -F "prefill-refresh-burst" /Users/cobalt/cobalt/src/cobalt/strike/detector.py` · prints 1 or more
- the refresh plist stays on disk, unloaded · `ls /Users/cobalt/cobalt/ops/com.cobalt.prefill-refresh.plist` · exit 0, listed

## RECORDS
- F4 reservation 1049 — drafted in parallel with f4-probe; launched only on PROBE X15 FAIL, dropped on OK — brain 9b07db5a 2026-10-26 (R2465)
- ARITHMETIC (drafter): radar 40, ceiling 50, 5 names. Today 5 × 60 / 10 = 30 s = 10 rpm, and the refresh minute holds 40 + 10 + 3 = 53. With the reservation, headroom 7 → ⌈300 / 7⌉ = 43 s = 6.98 rpm, and the refresh minute holds 49.98.
- COST (drafter): inside 05:45–15:45 ET the strike loop polls slower (5 names at radar 40: 30 s → 43 s), against `strike.alert_criterion_s` (`strike/config.py`). The brain weighs it at launch.
- After this deploys, 1045's X15 is re-run (its SECOND PASS string) before the bootstrap card 1048 writes an X15 line.
- Drafter `draft-f4-gate-run` (prompt 1043, R2465), 2026-10-26 (`date`). Reads only; nothing run, no git write. BASE `05366873` = `git -C /Users/cobalt/cobalt rev-parse --short=8 main` at drafting; the desk resets it at launch.
