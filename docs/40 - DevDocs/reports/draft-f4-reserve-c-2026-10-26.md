# draft-f4-reserve-c · 2026-10-26 · DRAFTED (round 2, brain R2513)

## §0 Headline
- Card 1049 is redrafted in place around his ruling C and brain R2513. The rows are R1 (radar cap `radar.finviz_rpm` = 37), R6 (strike headroom = ceiling − cap − 3 = 10, so 5 names poll at 30 s whatever the radar plans), R2 (refresh gate), R3 (X15 with the radar capped), R4 (FINAL X13 amendment), R5 (RUN) and D0.
- The cap is a real per-minute cap: `TokenBucket` capacity is 1.0 (`radar/collector.py:55`), so 37 grants fit in any half-open minute. Only the bucket's rpm source changes.
- Refresh under C: with R6 every readable plan is admitted, because the headroom equals the allowance, 10. Without R6, refresh would be admitted only at planned ≥ 37. No finding blocks the plist on this arithmetic.
- The one open item is D6. The strike gate counts the radar at min(planned, cap); otherwise every strike tick is refused once planned > 40.
- Decisions: 6 (5 ruled by R2513, 1 open).

## DECISIONS
- D1-D5: ruled by R2513 and recorded in the card's `## DECISIONS`. D1, D2 and D5 hold as the defaults. D3(b) is now R6, D3(a) is answered under R2, and D3(c) stays recorded. D4 is up to +16% (3 → 3.5 min), measured live.
- ASK DESK: R6 counts the radar at `min(planned_rpm, radar.finviz_rpm)` in `check_strike_demand`. At a fixed strike 10 rpm, a planned count refuses every tick above planned 40 (45 + 10 = 55), though the radar sends ≤ 37. The rule sits in `read_plan`, so the injected-plan tests `test_strike_detector.py:145` and `:191` stay unedited [18:04]. Default: as R6 writes it.

## RECORDS
- Round 1: 17:54 EDT `date`; main `e015c97b`. Reads were the prompt 1070 set: card 1049, the amend report, `cto-2026-10-26.md:69-72`, the words file `:1-4`, `f4-gate-run-2026-10-26.md:6`, `:14-21`, card 1068 `:17`, `:25`, writing-rules, `LAWS.md:136-137`, BUILD-HUB `:77-78`. Read with `git show main:` were the radar collector, runner, config, cli and notes; strike detector; prefill daily and refresh_probe; taxonomy tunables.py and tunables.yaml; F4-FINAL; and the tests radar_collector, radar_config, refresh_probe and prefill_refresh. The round-1 `git grep -n` proofs stand as recorded there. The new names were absent on main and the plist is listed.
- Round 2: the message from cto-desk (brain R2513) arrived after 18:00:35. Read: `git show main:tests/cobalt/test_strike_detector.py` whole. Proved with `git grep -n main`: detector `:50`, `:51`, `:80`, `:103`, `:111`, `:117`, `:274`, `:276`, `:313`, `:319`; test_strike_detector `:137`, `:145`, `:191`. Uses of `DemandPlan(`, `check_strike_demand` and `read_plan` in `src` and `tests`: `daily.py:100`, `:788`; `refresh_probe.py:260`, `:395`; `detector.py:111`, `:167`, `:172`, `:245`, `:252`, `:275`, `:313`, `:319`, `:349`; `test_prefill_refresh.py`; `test_strike_detector.py:118`, `:138`, `:142`, `:148`, `:163-164`; `test_strike_detector_db.py:55`. No other test reads `headroom_rpm` (`test_radar_runner.py`, `test_finviz_consumers.py`).
- ARITHMETIC: headroom 50 − 37 − 3 = 10. 5 × 60 / 10 = 30 s. Planned 20 on BASE: headroom 30 → 10 s. Planned 45: counted at min(45, 37) = 37 + 10 = 47 ≤ 50; at planned it would be 55, refused. X15: 37 + 10 + 3 = 50.
- Filter-string check: `grep -c` of `exch_` and `f=` in the card → `0`. Card `wc -c`: 14752 (HEAD) → 20371 (round 1) → 24365. The growth comes from rows R1-R6 replacing S1-S4.
- 18:04:22 EDT `date`. Only card 1049 and this report were written. Nothing was run; there was no git write and no launch.

DRAFTED · decisions: 6
