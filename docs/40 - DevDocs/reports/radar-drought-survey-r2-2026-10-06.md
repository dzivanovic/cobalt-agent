## §0 Headline
- Cause: not found. `radar.cards_enabled` = not recorded (dev: table `trader_settings` absent on `--side system`; prod: read blocked).
- Radar-origin card counts per day: not recorded (dev: `aset_sizings` absent on `--side system`; prod: blocked).
- Dev `radar_membership`: 0 rows 09-29 to 10-06 (read 3a), so no dev day passed membership.
- Production: every `--prod` read was refused by hook `bare-guard.py`; no prod number exists.

## TABLE
Dev unless named. Prod = not recorded on every cell (hook refusal).

| date | membership rows | session_blocks rows | formed rows | radar-origin card rows | last stage reached | query |
|---|---|---|---|---|---|---|
| 2026-09-29 | 0 | not recorded | not recorded | not recorded | none (dev) | 3a |
| 2026-09-30 | 0 | not recorded | not recorded | not recorded | none (dev) | 3a |
| 2026-10-01 | 0 | not recorded | not recorded | not recorded | none (dev) | 3a |
| 2026-10-02 | 0 | not recorded | not recorded | not recorded | none (dev) | 3a |
| 2026-10-03 | 0 | not recorded | not recorded | not recorded | none (dev) | 3a |
| 2026-10-04 | 0 | not recorded | not recorded | not recorded | none (dev) | 3a |
| 2026-10-05 | 0 | not recorded | not recorded | not recorded | none (dev) | 3a |
| 2026-10-06 | 0 | not recorded | not recorded | not recorded | none (dev) | 3a |

Stop and last-bar fields of `detail`: not recorded (read 4 errored).

## DECISIONS
- ASK DESK: the prod reads are refused by `bare-guard.py` (production is the deploy hub's); re-run the four reads from a seat the hook admits, or lift the guard for these SELECTs. [now] Default taken: report cause not found.
- ASK DESK: dev `--side system` lacks `trader_settings` and `aset_sizings`, and `session_blocks` and `radar_score` have no `created_at`; supply the side or day column for reads 1, 2, 3b, 4. [now] Default taken: no schema probing, cells not recorded.

## RECORDS
Dev = `COBALT_ENV=dev uv run cobalt db query --side system "<sql>"`; prod = same with `--prod` after `--side system`.
- 1 dev `SELECT value FROM trader_settings WHERE key = 'radar.cards_enabled'` · exit 1 · `UndefinedTable: relation "trader_settings" does not exist`
- 1 prod same · blocked · `PreToolUse:Bash hook error: [bare-guard.py]: route: production is the deploy hub's; a dev read uses COBALT_ENV=dev`
- 2 dev `SELECT created_at::date, count(*) FROM aset_sizings WHERE origin = 'radar' …` · exit 1 · `UndefinedTable: relation "aset_sizings" does not exist`
- 3a dev `SELECT trade_date, count(*) FROM radar_membership WHERE trade_date between 2026-09-29 and 2026-10-06 GROUP BY 1` · exit 0 · header only, 0 rows
- 3a prod same · blocked · same hook error
- 3b dev `SELECT created_at::date, count(*) FROM session_blocks …` · exit 1 · `UndefinedColumn: column "created_at" does not exist`
- 4 dev `SELECT created_at::date, count(*) FROM radar_score WHERE evaluation = 'formed' …` · exit 1 · `UndefinedColumn: column "created_at" does not exist`
- Reads 2, 3b, 4 prod: not run (guard refused every prod command tried).

SURVEY DONE · days: 8 · cause: not found
