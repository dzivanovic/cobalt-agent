# Card 731 `f5-checkpoints-1018` — preflight round 3 (2026-10-19)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read card header vs `CARD.md` build column | JOB, LADDER, BRANCH, WORKTREE, BASE `40e646ed`, TIP empty (the desk's), REPORT, CHECK REPORT, HOUSE B, BAND, RULINGS, RESTARTS, BOOTSTRAP present, column 0 (as r2; `CLASS`, `INSTALL` not CARD.md keys, NOTE) | OK |
| 2 | `git rev-parse 40e646ed` | `40e646edf7264b21191b2b63f5fbbb2dede793c7` | OK |
| 3 | `git log --oneline -3 -- <card>` | `86483cd0` (DECISION 2 amend), `319a99d5`, `2831c8cc`: card committed | OK |
| 4 | `git diff HEAD --stat -- <card>` | empty | OK |
| 5 | `grep -c -e "ASK DESK" -e "«FILL" -e "TBD" -e "TODO"` on card; `grep -n -e "ASK DESK" -e stop` | `1`: line 83, the preamble definition of `ASK DESK`; none inside DECISION 2; "stop" only in K0 and DECISION 1 (F4 gate), none in DECISION 2 | OK |
| 6 | read DECISION 2 | X2: builder-committed synthetic fixture at `tests/cobalt/fixtures/checkpoints/`, marker `# synthetic shape — X2 real capture owed before load`; X3: `timeout_s: 60`, `max_output_tokens: 512`, each `# source: UNMEASURED, provisional — X3 owed before load` | OK |
| 7 | read K2 row | parser "built against the builder-committed synthetic-shape fixture (`DECISION` 2)"; tests on "the synthetic fixture"; files cell lists the fixture dir | OK |
| 8 | read K4 row | `timeout_s: 60`, `max_output_tokens: 512`, each with the UNMEASURED comment, "never the voice route's 15 s" | OK |
| 9 | read B0 row | owed list names X2 and X3 first, with X4–X7, X10, X12, X13 | OK |
| 10 | read `## CHECK ASKS` | FOR THE CHECK line for brain 2026-10-19 present (K2 synthetic, K4 provisional, X2/X3 owed, follow-up card) beside the 2026-10-18 line | OK |
| 11 | K2, K4, ORDER vs DECISION 2 and each other | K2 synthetic fixture = DECISION 2; K4 60/512 = DECISION 2; ORDER "X2 and X3 are owed before load (B0, DECISION 2)" = B0; DECISION 4 `300` s > 60 + 2×30 | OK |
| 12 | placeholder scan | only `<NNNN>`, `<BASE>`, `<tip>`, `HHMM`, TIP (the desk's); no BASE-less or other token | OK |
| 13 | `grep -n -e launchctl -e --add-dir -e --allowedTools -e "claude --bg" -e desk-launch` on card (R411, R412) | one hit, line 48 `## NOT IN THIS JOB`: a prohibition, no command string | OK |
| 14 | K0 at BASE: `git grep -n -e "def ensure_daily_note" -e "def format_stamp" -e "daily_refresh" 40e646ed -- src/cobalt/prefill configs/cobalt/prefill.yaml` | `daily.py:856 ensure_daily_note`, `:705 format_stamp`, `prefill.yaml:24 daily_refresh:` | OK |
| 15 | K0 at BASE: `git grep -n "label: com.cobalt.prefill-refresh" 40e646ed -- configs/cobalt/jobs.yaml` | `jobs.yaml:214` | OK |
| 16 | `git grep` BASE `prefill/market.py`, `prefill/config.py` | `import httpx` :25, `resolve_token, scrub` :27, `fetch_market_table` :55; `_load_yaml_mapping` :163, F4 `daily_refresh` loader :199, `"prefill"` loader :207 | OK (cites drifted, by content) |
| 17 | `git grep` BASE `vaultwrite/writer.py` | `AT_END` :156, `after_pattern` :159, `_write_with_retry` :559, `upsert_unit` :673, AT_END default :732 | OK |
| 18 | `git grep` BASE `radar/notes.py`, `strike/measure.py` | `DemandConsumer` :203, `scheduled_consumers` :329, `check_scheduled_demand` :384, `radar_planned_rpm` :133 | OK |
| 19 | `git grep` BASE calendar, note, notify, entrypoint, store | `is_trading_day` calendar.py:116, `daily_note_path` note.py:250 (card :238), `send_dm` mattermost.py:130, `as_job` entrypoint.py:36, `purge_expired` store.py:247 | OK (cite drift, by content) |
| 20 | `git grep` BASE `cli.py`, `s2.yaml`, `jobs.yaml`, `test_finviz_consumers.py` | `validate = sub.add_parser(` :550 (card :548); `id: K16.1` :623, `label: com.cobalt.cards-expire` :626; `no_resident_reads` :356, `daily.md.j2` :359; `CONSUMERS` :35, exact-set :66 | OK (cite drift, by content) |
| 21 | `git grep` BASE `db_migrations/__init__.py` for K6/DECISION 3 | `FORWARD` ends `0025_dml_roles.sql` :175 (rollback :180): card 448 has merged; K6 says "`0025` on BASE", RED "`FORWARD[-1].name == "0024_strike_alerts.sql"`", head-pin `grep -rn "0024" tests`; DECISION 3 says 448 has not merged | FAIL |
| 22 | `ls tests/cobalt/fixtures/checkpoints` | absent: the builder commits it (DECISION 2) | OK (NOTE) |

## ISSUES
- FAIL · check 21 · K6 and DECISION 3 are stale at BASE `40e646ed`: `0025_dml_roles` is on main, so the next free number is `0026`, K6's RED (`FORWARD[-1]` is `0025_dml_roles.sql`) and its head-pin grep (`0025`, not `0024`) are wrong, and DECISION 3's "neither has merged" is false. The drafter did not touch K6 or DECISION 3 (its report: DECISION 3 untouched). Fix K6 and DECISION 3 to `0026` before the launch.
- NOTE · `## RECORDS` still says BASE `279c99ce` and "F4 is NOT on `main` at BASE"; the header BASE is `40e646ed` and K0's two greps now print (checks 14, 15). DECISION 1 stands as the K0 gate only.
- NOTE · Line cites drifted at the new BASE (`daily_note_path` :250, `validate` :550, `K16.1` :623, `no_resident_reads` :356, `AT_END` default :732); the card says re-find by content.
- NOTE · `## CHECK ASKS` X2 (model output) and X3 (gate) share labels with the owed-before-load X2 (Groups capture) and X3 (30 calls); the FOR THE CHECK line spells out what each is.
- NOTE · Line 83 keeps the `ASK DESK` definition although no decision uses it now.
- NOTE · Header `CLASS`, `INSTALL` are not CARD.md keys (as r1, r2).

PREFLIGHT DONE · card: f5-checkpoints-1018 · checks: 22 · fails: 1 · ready: NO
