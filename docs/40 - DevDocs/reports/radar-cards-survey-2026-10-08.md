## §0 Headline
- cards: `not recorded` · view: `not recorded` · poll failures: `not recorded` · formations: `not recorded`.
- Cause: `not recorded`. The first production read was refused by a guard; per the prompt no other production string was run.

## COUNTS
| read id | key | count |
|---|---|---|
| 1 | cards created today by state | not recorded (refused) |
| 2 | ladder view | not recorded (not run) |
| 3 | poll failures, failed stage | not recorded (not run) |
| 4 | session blocks | not recorded (not run) |
| 5 | formations | not recorded (not run) |

## DECISIONS
- ASK DESK: the guard `ops/desk/bare-guard.py` refuses the production string the prompt prescribes. Either the hook needs to allow `COBALT_ENV=production uv run cobalt db query --side <user|system> --prod "<sql>"` for this seat, or the deploy hub runs the five reads. Default taken: stopped, no other production string run. [2026-10-08]

## RECORDS
- Prompt 115 read; `reports/radar-page-read-2026-10-06.md` and `reports/cards-origin-survey-2026-10-06-r2.md` read.
- `ls` of the report path: exit 1, absent, as required.
- Column greps on main, all confirmed: `aset/migrations/0001_aset_sizings.sql:8` created_at; `0006_aset_sizings_state.sql:22` state, `:26` state_at; `0008_aset_sizings_origin.sql:23` origin; `db_migrations/0007_radar_cards.sql:215` view columns, `:233` `origin = 'radar'`; `db_migrations/0004_radar_pool.sql:6` pool_key, `:7` state, `:11-12` failed_stage, `:17` members, `:22` poll_failures; `session/migrations/0001_session_blocks.sql:15` ts, `0002_session_blocks_kind.sql:19` kind; `db_migrations/0006_radar_score.sql:72` started_at, `:94` run_id, `:95` membership_id, `:97` trade_def_md5, `:99` evaluation.
- Production read 1 (the exact string in the prompt, `--side user --prod`): refused by the PreToolUse hook `python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py`. Hook text, whole: `route: production is the deploy hub's; a dev read uses COBALT_ENV=dev`. No output from the database.
- Reads 2 to 5: not run. No other production string run. No database write, no code, no git write.

## MEASURE
`wc -c` of this report: not measured (no `wc` run on it; about 2300 bytes by count).

FAILED: production read 1 refused by bare-guard.py hook ("route: production is the deploy hub's; a dev read uses COBALT_ENV=dev")
