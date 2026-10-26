# draft-f4-reserve-amend · 2026-10-26 · STOPPED: radar yield impossible

## §0 Headline
- STOPPED before redrafting. Card 1049 is left as it was, and its first revision (strike 30 s → 43 s) stands. Lines were read at main `2d033ddc`.
- The radar has no per-minute budget. Its single pacer is `process_bucket(50)`, a token bucket set at the CEILING, not at its planned 40. Inside a 100 s scan the radar can make 50 requests in a minute.
- The strike loop runs its own bucket in addition to that. Radar + strike can therefore reach 60 in a burst minute without refresh, and a radar that is "yielding 3" still does not bound the refresh minute at 50.
- "Refresh waits" cannot be built: the one-shot sees only the plan, which is the same in every minute.
- One question for him: the 13 s cost (D1).

## DECISIONS
- ASK DESK: radar yield impossible: the radar has no per-minute budget hook. To yield 3 in one minute, a wall-clock, schedule-aware cap would have to be added to the radar's shared bucket at ceiling − live strike rpm − 3. That changes the radar's pacing, which FINAL `:174` leaves untouched, and the X15 probe's radar stand-in as well [11:37]. Default: card 1049 as its first revision drafted it (S1/S2 strike reservation at 43 s, S4 burst refusal), sent to the brain as D1.
  - The radar's one pacer: `bucket = process_bucket(int(rpm))` with rpm = `radar.finviz_max_rpm` = 50 (`radar/runner.py:522`; tunables `:702-703`). It is shared by the daily collector `:547`, the screener `:559` and the poller `:564`. Every request goes through `bucket.acquire()` (`radar/collector.py:174`, `:274`; `radar/poller.py:87`).
  - `TokenBucket` (`radar/collector.py:42`): fixed `rate = rpm / 60` (`:54`) and `capacity = 1.0` (`:55`). It runs on a monotonic clock only, with no wall-clock minute, no schedule and no hook. `process_bucket` caches one bucket per rpm (`:78-81`).
  - Planned is an average, not a pace. Planned = cycle requests × 60 / `radar.scan_interval` (`radar/notes.py:467`, `:634`, `:436`), with scan_interval = 100 s (tunables `:675-676`). The cold-cycle math assumes the cycle runs at the ceiling (`:640`). The resident runs a cycle, then sleeps 100 s (`radar/runner.py:637-639`). At planned 40, a cycle is about 67 requests made at up to 50 rpm.
  - The strike loop has its own bucket at its counted share (`strike/detector.py:282-287`), separate from the radar's 50. In a radar burst minute with 5 ARMED names at 30 s that is 50 + 10 = 60, before refresh. UNPROVEN (L70): the real radar's per-minute peak, because fetch latency and DB work may hold it below 50. It may bear on the 06:48 429 (D3 of the card).
  - The probe does not see the radar's bucket. X15's radar is a stand-in at a flat `radar_rpm` 40 that calls `finviz_get` directly (`prefill/refresh_probe.py:23`, `:77`, `:321-329`, `:407`). A yield in the radar's bucket cannot change the X15 count unless the stand-in is rewritten to go through it, and a flat 40 does not reproduce the real burst.
  - A deferral lands in the next minute. With steady demand, 3 requests deferred from minute M make M+1 = 43 + 10 = 53 in the probe's model, unless the cap continues past M.
  - Refresh cannot wait for headroom. The one-shot reads only `read_plan()` (`prefill/daily.py:788`) and compares the plan (`:791`, `:794`). The plan is the same in every minute and the one-shot cannot see the live counts of `com.cobalt.radar`. With the strike loop at its full headroom (40 + 10 = 50), no minute ever shows 3 free.
  - For his one question (the 13 s cost): (a) strike 30 s → 43 s inside 05:45–15:45 ET, 5 names at radar 40, so every alert is up to 13 s later. This is card 1049 as drafted, and it passes X15's arithmetic: 40 + 6.98 + 3 = 49.98. (b) Strike stays at 30 s and the refresh plist stays unloaded until a radar pacing card budgets the radar's bucket per minute; that card is wider and changes the radar's pacing. Under (b), radar + strike above 50 in burst minutes is a separate open finding either way.

## RECORDS
- 11:35:00 EDT `date`; `git rev-parse --short=8 main` → `2d033ddc`.
- Read: prompt 1061; card 1049 (left unchanged); `reports/draft-f4-reserve-fix-2026-10-26.md`; `reports/cto-2026-10-26.md:13` (R2492); `docs/30 - Design/F4-FINAL-2026-10-10.md:160-225` (`:174` "Neither edits … the scan cadence", `:214` X8 R2-4 yield, `:219` X13, `:221` X15); `topics/writing-rules.md`.
- Read whole with `git show main:`: `src/cobalt/radar/collector.py`, `src/cobalt/radar/poller.py`, `src/cobalt/radar/runner.py`, `src/cobalt/radar/notes.py`, `src/cobalt/strike/detector.py`, `src/cobalt/prefill/daily.py`, `src/cobalt/prefill/refresh_probe.py`.
- Proved with `git grep -n main`: collector `:42`, `:54`, `:55`, `:78`, `:81`, `:174`, `:274`; poller `:87`; runner `:522`, `:547`, `:559`, `:564`, `:635`, `:637`, `:639`; detector `:144`, `:274`, `:282`, `:284`, `:287`; refresh_probe `:23`, `:58`, `:77`, `:119`, `:321`, `:325`, `:329`, `:407`; notes `:436`, `:467`, `:634`, `:635`, `:640`; daily `:682`, `:759`, `:780`, `:788`, `:791`, `:794`, `:800`; tunables `:675-676` (100), `:702-703` (50), `:1148-1149`, `:1160-1161`.
- ARITHMETIC: 40 rpm × 100 s / 60 ≈ 67 requests a cycle, which takes ≈ 80 s at 50 rpm. Burst minute 50 + 10 = 60. Deferral M+1 43 + 10 = 53. The 43 s option: ⌈300/7⌉ = 43, 6.98 rpm, 49.98.
- 11:37:50 EDT `date`. Reads only; no file edited except this report; no git write; nothing launched.

FAILED: radar yield impossible — ASK DESK under ## DECISIONS
