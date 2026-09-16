# DAY-OPEN 2026-09-15 — seat qwen-27b, read-only checks

Run: 08:15–08:18 EDT (12:17 UTC). All commands run verbatim from `docs/40 - DevDocs/prompts/2026-09-15/00-day-open-qwen.md`.

## S1 radar resident
```
         state = running
        pid = 91916
        last exit code = 143
```

## S2 radar pool row
```
state   session members cap     last_scan_at    failed_stage    failed_detail
scanning        premarket       50      50      2026-09-15 12:15:01.069849+00:00        bars    poll failures: 1

Tue Sep 15 12:17:31 UTC 2026
```

## S3 first membership rows today
```
ticker  session entered_et      source  rank_at_entry
THH     premarket       2026-09-15 04:00:46.071737      screen:morning_low_float@a834132de4fa   9
PMEC    premarket       2026-09-15 04:00:46.071737      screen:morning_low_float@a834132de4fa   8
DKI     premarket       2026-09-15 04:00:46.071737      screen:morning_low_float@a834132de4fa   12
VRAX    premarket       2026-09-15 04:00:46.071737      screen:morning_low_float@a834132de4fa   13
ALGS    premarket       2026-09-15 04:00:46.071737      screen:morning_low_float@a834132de4fa   7
```

## S4 heartbeat, last beat
```
HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-09-15 08:13:27 EDT)
OK   database                 cobalt_brain reachable
OK   sheet HTTP               http://127.0.0.1:5010/ -> 200
OK   archiver                 last run 2026-09-15 00:53 UTC (11.3 h ago), rows written 3165340, exit 0
RED  radar                    failed_stage bars: poll failures: 1; poll IMCC stale since 2026-09-14T13:38:07.287155+00:00
RED  com.cobalt.prefill-daily     failed    RulesSourceError: Rules.md line 14 (rule #11): needs exactly one trailing tag from ('process', 'sizing', 'time_window', 're_entry', 'circuit_breaker', 'hard_stop'), found none: "11. Exits and scaling follow the setup's sheet as written; no written exit = no trade. Exit structure read live — prior 2-
RED  com.cobalt.prefill-drc       failed    RulesSourceError: Rules.md line 14 (rule #11): needs exactly one trailing tag from ('process', 'sizing', 'time_window', 're_entry', 'circuit_breaker', 'hard_stop'), found none: "11. Exits and scaling follow the setup's sheet as written; no written exit = no trade. Exit structure read live — prior 2-
```

## S5 radar cycle gaps today
```
2026-09-15 06:13:39.612 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789467130625
2026-09-15 06:16:48.614 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789467319661
2026-09-15 06:19:57.568 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789467508650
2026-09-15 06:23:06.491 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789467697599
2026-09-15 06:26:15.487 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789467886521
2026-09-15 06:29:24.443 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789468075522
2026-09-15 06:32:33.451 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789468264473
2026-09-15 06:35:42.451 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789468453483
2026-09-15 06:38:51.476 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789468642491
2026-09-15 06:42:00.497 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789468831513
2026-09-15 06:45:09.504 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789469020529
2026-09-15 06:48:18.495 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789469209536
2026-09-15 06:51:27.500 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789469398524
2026-09-15 06:54:36.496 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789469587535
2026-09-15 06:57:45.512 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789469776531
2026-09-15 07:00:54.452 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789469965541
2026-09-15 07:04:03.408 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789470154489
2026-09-15 07:07:12.324 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789470343434
2026-09-15 07:10:21.280 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789470532350
2026-09-15 07:13:30.243 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789470721308
2026-09-15 07:16:39.202 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789470910267
2026-09-15 07:19:48.146 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789471099223
2026-09-15 07:22:57.105 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789471288171
2026-09-15 07:26:06.097 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789471477133
2026-09-15 07:29:15.104 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789471666127
2026-09-15 07:32:24.084 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789471855130
2026-09-15 07:35:33.099 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789472044117
2026-09-15 07:38:42.115 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789472233132
2026-09-15 07:41:51.145 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789472422150
2026-09-15 07:45:00.108 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789472611179
2026-09-15 07:48:09.053 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789472800136
2026-09-15 07:51:18.003 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789472989084
2026-09-15 07:54:27.003 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789473178034
2026-09-15 07:57:36.032 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789473367035
2026-09-15 08:00:44.989 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789473556056
2026-09-15 08:03:53.996 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789473745022
2026-09-15 08:07:03.012 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789473934027
2026-09-15 08:10:12.026 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789474123044
2026-09-15 08:13:21.033 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789474312058
2026-09-15 08:16:30.031 | INFO     | cobalt.radar.runner:resident:342 - radar cycle: scanning scan_id=1789474501069
```

## S6 daily note
```
ls: /Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-15.md: No such file or directory
label   state   exit_code       finished_at
com.cobalt.prefill-daily        failed  1       2026-09-15 09:15:05.795973+00:00
com.cobalt.prefill-drc  failed  1       2026-09-14 19:40:05.969780+00:00
```

## S7 archiver
```
OK   archiver                 last run 2026-09-15 00:53 UTC (11.3 h ago), rows written 3165340, exit 0
```

## VERDICT

| check | verdict | one-line evidence |
|---|---|---|
| S1 radar resident | PASS | `state = running`, pid 91916 |
| S2 radar pool row | KNOWN | scanning, members 50/50, last_scan_at 2.5 min before `date -u`; failed_stage bars "poll failures: 1" = known IMCC stale-bar ticket |
| S3 first membership rows today | PASS | premarket entries at 04:00:46 ET (after 04:00), screen:morning_low_float |
| S4 heartbeat, last beat | FAIL | beat 08:13:27 EDT (within 20 min), database + sheet HTTP OK; prefill-daily RED and the note does not exist (S6) |
| S5 radar cycle gaps today | PASS | 40 cycles, every gap ≈3 min 9 s; largest gap 06:13:39→06:16:48 (≈3 min 9 s) |
| S6 daily note | FAIL | `2026-09-15.md` does not exist; prefill-daily state failed, exit_code 1 (RulesSourceError: rule #11 lacks a trailing tag) |
| S7 archiver | PASS | OK, last run 2026-09-15 00:53 UTC (11.3 h ago), exit 0 |

**OVERALL: AMBER** — no ERROR; FAIL on S4/S6 (prefill-daily failed again with `RulesSourceError` on Rules.md rule #11 — the launch-line sed pattern `\.#process$` does not match a line with no trailing tag at all, and the note was never created). Known items (S2 radar bars poll, S4 prefill-drc RED until its 15:40 run) do not lower the verdict.

NEXT: the desk reads this report and states the plate.
