# Radar drought survey r3 — 2026-10-06 (R508)

## §0 Headline
- Cause: not found. There is no drought in production: radar-origin card rows exist on every trading day in the window (read 2, P): 09-29 31, 09-30 31, 10-01 19, 10-02 23, 10-05 24.
- `radar.cards_enabled` = True (read 1, P); every run row has `cards_enabled` True (read 5, P). Dev holds no rows on any read (D).
- 10-06 has no card yet: read at 09:21 ET, before the 09:30 open. Membership 391 and 109 complete runs, no formed rows (reads 3a, 5, 4a, P).
- 09-30 RED `bars: poll failures`: read 6a returns `abandoned: the run never published (crash or market_reset drop)` for one run at 12:43Z; the poll-failure cause itself is `not recorded`.

## TABLE
Weekend 10-03 and 10-04: no row in any read, P or D.

| date | membership rows | session_blocks rows | run rows | formed rows | radar-origin card rows | last stage reached | read ids |
|---|---|---|---|---|---|---|---|
| 09-29 | 611 (P) | 0 (P) | 314 complete (P) | 2783 (P) | 31 (P) | card | 3a, 3b, 5, 4a, 2 |
| 09-30 | 531 (P) | 0 (P) | 308 complete + 1 failed (P) | 3710 (P) | 31 (P) | card | 3a, 3b, 5, 4a, 2 |
| 10-01 | 594 (P) | 0 (P) | 316 complete (P) | 2368 (P) | 19 (P) | card | 3a, 3b, 5, 4a, 2 |
| 10-02 | 615 (P) | 0 (P) | 315 complete (P) | 3113 (P) | 23 (P) | card | 3a, 3b, 5, 4a, 2 |
| 10-05 | 547 (P) | 0 (P) | 315 complete + 1 failed (P) | 2696 (P) | 24 (P) | card | 3a, 3b, 5, 4a, 2 |
| 10-06 | 391 (P) | 2 (P) | 109 complete (P) | 0 (P) | 0 (P) | in-play (runs complete, none formed; read 09:21 ET, pre-open) | 3a, 3b, 5, 4a, 2 |

Stop check (read 4b, P): formed rows with a suppressed reason (required computed dot N/A and untapped) per day: 09-29 697, 09-30 759, 10-01 390, 10-02 416, 10-05 240. Unsuppressed (blank reason): 2086, 2951, 1978, 2697, 2456.
Read 4c (P), latest 5 formed rows, run 10-05 23:55Z: LEN `event(stop_hit)` false, last_close bar 23:53Z; CTVA and NVAX `event(stop_hit)` true, last_close bar 23:54Z; TWLO and NVAX (extension) carry no stop atom. No row is blocked on a missing stop or a stale last bar.
Failed runs (read 6b, P): 09-30 1, 10-05 1.
Dev (D): reads 1, 2, 3a, 3b, 4a, 4b, 4c, 5, 6a, 6b all return zero rows.

## DECISIONS
- ASK DESK: the premise "no card for a week" does not hold in production; confirm what the radar view showed (a UI or read-path fault, not a missing card) — default taken: none, no fix proposed [09:30 ET].

## RECORDS
All run from `/Users/cobalt/cobalt`; every command exit 0, no error, no hook refusal. Production strings (P) and dev strings (D) as in the prompt:
- P reads 1, 2, 3a, 3b, 4a, 4b, 4c, 5, 6a, 6b: ran, results above.
- D reads 1, 2, 3a, 3b, 4a, 4b, 4c, 5, 6a, 6b: ran, header only, zero rows.
- `date`: Tue Oct 6 09:21:42 EDT 2026.

SURVEY DONE · days: 6 · cause: not found
