# Cards origin survey — 2026-10-06 (R560)

## §0 Headline
- Today 2026-10-06 ET (read 1, P, 15:21 ET): 31 rows. radar nine-ema-scalp 12, radar rubberband 6, radar second-chance 8, manual none 5.
- First zero day: none. No setup falls to zero or drops sharply (more than half, two days running) in 09-24 to 10-06 (read 1, P).
- Hold day 2026-09-23/24: no setup drops on it, so the answer is no for every setup.
- `vwap-continuation` has no row on any day (read 1, P): `not recorded`.
- Radar-origin rows start 09-24. 09-21 to 09-23 hold manual rows only (read 1, P).

## TABLE
Read 1 (P). Setup `none` = manual card. A day with no row is absent (weekends 09-20, 09-26, 09-27, 10-03, 10-04).

| date | origin | setup | count | total |
|---|---|---|---|---|
| 09-21 | manual | none | 7 | 7 |
| 09-22 | manual | none | 8 | 8 |
| 09-23 | manual | none | 12 | 12 |
| 09-24 | manual | none | 11 | 18 |
| 09-24 | radar | rubberband | 5 | 18 |
| 09-24 | radar | second-chance | 2 | 18 |
| 09-25 | manual | none | 6 | 32 |
| 09-25 | radar | nine-ema-scalp | 17 | 32 |
| 09-25 | radar | rubberband | 2 | 32 |
| 09-25 | radar | second-chance | 7 | 32 |
| 09-28 | manual | none | 7 | 36 |
| 09-28 | radar | nine-ema-scalp | 20 | 36 |
| 09-28 | radar | rubberband | 1 | 36 |
| 09-28 | radar | second-chance | 8 | 36 |
| 09-29 | manual | none | 15 | 46 |
| 09-29 | radar | nine-ema-scalp | 16 | 46 |
| 09-29 | radar | rubberband | 3 | 46 |
| 09-29 | radar | second-chance | 12 | 46 |
| 09-30 | manual | none | 3 | 34 |
| 09-30 | radar | nine-ema-scalp | 17 | 34 |
| 09-30 | radar | rubberband | 2 | 34 |
| 09-30 | radar | second-chance | 12 | 34 |
| 10-01 | manual | none | 10 | 29 |
| 10-01 | radar | nine-ema-scalp | 12 | 29 |
| 10-01 | radar | rubberband | 1 | 29 |
| 10-01 | radar | second-chance | 6 | 29 |
| 10-02 | manual | none | 7 | 30 |
| 10-02 | radar | nine-ema-scalp | 10 | 30 |
| 10-02 | radar | rubberband | 5 | 30 |
| 10-02 | radar | second-chance | 8 | 30 |
| 10-05 | manual | none | 6 | 30 |
| 10-05 | radar | nine-ema-scalp | 14 | 30 |
| 10-05 | radar | rubberband | 2 | 30 |
| 10-05 | radar | second-chance | 8 | 30 |
| 10-06 | manual | none | 5 | 31 |
| 10-06 | radar | nine-ema-scalp | 12 | 31 |
| 10-06 | radar | rubberband | 6 | 31 |
| 10-06 | radar | second-chance | 8 | 31 |

## ANSWER
Per setup (read 1, P). Drop = count below half the prior-day count, two days running.

| origin · setup | last day above zero | first zero or sharp drop | hold day match |
|---|---|---|---|
| radar · nine-ema-scalp | 10-06 | NO DROP: 17, 20, 16, 17, 12, 10, 14, 12 | no |
| radar · rubberband | 10-06 | NO DROP: 5, 2, 1, 3, 2, 1, 5, 2, 6 (one halving, 09-24 to 09-25, not two days running) | no |
| radar · second-chance | 10-06 | NO DROP: 2, 7, 8, 12, 12, 6, 8, 8, 8 | no |
| manual · none | 10-06 | NO DROP: 7, 8, 12, 11, 6, 7, 15, 3, 10, 7, 6, 5 (one halving, 09-29 to 09-30, then 10; not two days running) | no |
| radar · vwap-continuation | `not recorded` (no row on any day) | `not recorded` | `not recorded` |

Today (2026-10-06 ET, read 1, P): radar nine-ema-scalp 12, radar rubberband 6, radar second-chance 8, manual none 5; total 31.

Note: second-chance rows continue on every trading day after the 09-23 hold (read 1, P), 09-24 to 10-06.

## DECISIONS
- ASK DESK: the premise "no cards for about a week, only 9 EMA and VWAP cards at the start" does not match production: radar rows of three setups exist every trading day, and no `vwap-continuation` row exists on any day (read 1, P). Confirm which screen he looks at and what it showed at which ET time. Default taken: none, no fix proposed [15:25 ET].
- ASK DESK: second-chance rows are written on every day since 09-24 although the hold records say it stays off the radar (`reports/sitting-second-chance-2026-09-24.md:85`). Is that expected? Default taken: reported only [15:25 ET].

## RECORDS
All from `/Users/cobalt/cobalt`. `date`: Tue Oct 6 15:21:13 EDT 2026.
- First `ls` with a pipe: refused by `ops/desk/bare-guard.py` (hook text: "NOT A REFUSAL. Dejan's rule: one bare command per call, and this call contains a pipe `|` with `ls`, not a read-only filter. Resend the SAME commands now, one per call, in order. Do not report this to Dejan as a failure."). No production string was in that call.
- `ls` of this report: exit 1, absent.
- Read: prompt 50; `radar-drought-survey-r3-2026-10-06.md`; `radar-screen-trace-2026-10-06.md`; `Memory/topics/writing-rules.md`.
- P read 1 (the one production string, `--side user --prod`): exit 0, no error, no refusal.
- Hold-date greps:
  - `sitting-vwap-continuation-2026-09-24.md:24` R118, 2026-09-23 22:3x ET; `:54` "Held off … R118 hold". Verified.
  - `BACKLOG.md:608` VWAP CONTINUATION REVIEW: `PENDING — UNHELD`. Verified.
  - `sitting-second-chance-2026-09-24.md:25` R117, 2026-09-23 22:2x ET; `:85` "until then Second Chance stays off the radar (R117)". Verified.
  - `BACKLOG.md:607` SECOND CHANCE REDESIGN: `PENDING — UNHELD`. Verified.
  - `reports/cto-2026-10-0*` for a later hold or release of either: no hold or release. Hits only `cto-2026-10-06.md:101` (both sittings listed as held off, he holds them) and `cto-2026-10-06-words.md:14` (his words: unsure when the screen emptied, around the VWAP and Second Chance sitting). No later hold or release: `none`.
- No other database command, no production string, no code or git write.

## MEASURE
`wc -c` of this report: 5482 bytes (measured before this line was edited; exit 0).

SURVEY DONE · first zero day: none · decisions: 2
