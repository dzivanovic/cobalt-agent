# Cards origin survey — 2026-10-06 (R560)

## §0 Headline
- Read 1 refused by the hook; no number recorded. Today (2026-10-06 ET) count by origin and setup: `not recorded`.
- First zero day per setup: `not recorded`. Match to the hold day (2026-09-23 / 09-24): `not recorded`.
- Hold dates verified by grep: VWAP Continuation held 09-23 22:3x ET (R118); Second Chance off the radar 09-23 22:2x ET (R117); no later hold or release found.

## TABLE
Read 1 refused: no row. Date · origin · setup · count · total: `not recorded`.

## DECISIONS
- ASK DESK: the production route is refused for this seat (hook text in RECORDS). Run read 1 from the hub, or widen the seat's route — default taken: no other production string run, no estimate [15:20 ET].

## RECORDS
All from `/Users/cobalt/cobalt`.
- Read 1, production string as typed in the prompt: refused. Hook text, whole: `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: production is the deploy hub's; a dev read uses COBALT_ENV=dev`. No other production string run; no dev read run (dev holds no rows, r3 read).
- Read: prompt 50; `radar-drought-survey-r3-2026-10-06.md`; `radar-screen-trace-2026-10-06.md`; `Memory/areas/cobalt.md`; `topics/writing-rules.md`.
- Hold-date greps:
  - `reports/sitting-vwap-continuation-2026-09-24.md:24` — R118, 2026-09-23 22:3x ET, "Let's go with B…"; `:54` — `dist.k.vwap` "R118 hold" (confirmed). `docs/00 - Project/BACKLOG.md:608` — VWAP CONTINUATION REVIEW `PENDING — UNHELD` (confirmed).
  - `reports/sitting-second-chance-2026-09-24.md:25` — R117, 2026-09-23 22:2x ET, "This setup needs to be redesigned"; `:85` — "Second Chance stays off the radar (R117)" (confirmed). BACKLOG sitting row for Second Chance: lines 74, 75, 607 matched but are over-long lines; the `PENDING — UNHELD` wording was not read there: `not recorded`.
  - `reports/cto-2026-10-0*` for either setup: `cto-2026-10-06.md:100` (long line, content not read; not a hold or release found by pattern), `cto-2026-10-06-words.md:14` (his words: the empty screen began "around when we said I need a sitting for VWAP and Second Chance"). Later hold or release: none found.
- `wc -l cto-2026-10-06.md`: 115, exit 0. `date`: Tue Oct 6 15:20:10 EDT 2026.
- No database write, no code, no git write.

## MEASURE
`wc -c` of this report: 2525 (before this line was edited), exit 0.

FAILED: production read 1 refused by bare-guard hook (route: production is the deploy hub's)
