# Card 731 `f5-checkpoints-1018` — preflight round 4 (2026-10-19)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read card header vs `CARD.md` build column | JOB, LADDER, BRANCH, WORKTREE, BASE `40e646ed`, TIP empty (the desk's), REPORT, CHECK REPORT, HOUSE B `mandatory — vault notes`, BAND HIGH, RULINGS, RESTARTS, BOOTSTRAP, all column 0 (`CLASS`, `INSTALL` not CARD.md keys, NOTE) | OK |
| 2 | `git rev-parse HEAD 40e646ed` | HEAD `1bd7766bb9a71c2738bebcd7f0ca883a7eb6d9d9`; BASE `40e646edf7264b21191b2b63f5fbbb2dede793c7` | OK |
| 3 | `git log --oneline -3 -- <card>` | `1bd7766b` (migration-number amend), `86483cd0`, `319a99d5`: card committed | OK |
| 4 | `git diff HEAD --stat -- <card>` | empty | OK |
| 5 | `grep -n -e "ASK DESK" -e "«FILL" -e TBD -e TODO` on card | no hit (r3's `ASK DESK` definition is gone) | OK |
| 6 | read DECISION 2, K2, K4, B0, `## CHECK ASKS` | unchanged from r3: synthetic fixture marker; `timeout_s: 60`, `max_output_tokens: 512` each with the UNMEASURED comment; X2, X3 owed before load; brain 2026-10-19 CHECK ASK present; mutually consistent (r3 checks 6-11) | OK |
| 7 | placeholder scan `grep -o -n -E "<[A-Za-z]...>\|«...»"` | `<BASE>`, `<NNNN>`, `<tip>`, `<reason>`, `<kind>`; no `«FILL`. `<NNNN>` is K0's resolved number (`0026`); `<reason>`, `<kind>` sit inside runtime message strings; TIP empty is the desk's | OK (NOTE) |
| 8 | `grep -n -e launchctl -e --add-dir -e --allowedTools -e "claude --bg" -e desk-launch` on card (R411, R412) | one hit, line 48 `## NOT IN THIS JOB`: a prohibition; no command string added | OK |
| 9 | K0 at BASE: `git grep -n -e "def ensure_daily_note" -e "def format_stamp" -e "daily_refresh" 40e646ed -- src/cobalt/prefill configs/cobalt/prefill.yaml` | `daily.py:856 ensure_daily_note`, `:705 format_stamp`, `prefill.yaml:24 daily_refresh:` (plus other `daily_refresh` lines) | OK |
| 10 | K0 at BASE: `git grep -n "label: com.cobalt.prefill-refresh" 40e646ed -- configs/cobalt/jobs.yaml` | `jobs.yaml:214` | OK |
| 11 | `ls src/cobalt/db_migrations` | ends `0024_strike_alerts.*`, `0025_dml_roles.rollback.sql`, `0025_dml_roles.sql`; no `0026` file | OK |
| 12 | `grep -n FORWARD/REVERSE/0025/0026 db_migrations/__init__.py` | `FORWARD` last `0025_dml_roles.sql` :175; `REVERSE` first `0025_dml_roles.rollback.sql` :180; no `0026` | OK |
| 13 | FAIL 21 fixed: `grep -n -e 0024 -e 0025 -e 0026` on card | K6 :29 `0026` on BASE, RED `FORWARD[-1].name == "0025_dml_roles.sql"`, head-pin `grep -rn "0025" tests`, "now they move to `0026`"; DECISION 3 :88 `0025_dml_roles` on main, no `0026` file, F5 takes `0026`; RECORDS :99, :102 agree; no `0024` left | OK |
| 14 | head-pin tests exist for the `0025` grep: `grep -rn "0025_dml_roles" tests` | hits in `test_dml_roles_offline.py:21`, `test_f15_p1_records_offline.py:28`, `test_assumed_store.py:271`, `test_archiver_migrations.py` and a dozen rollback-list tests: the grep finds the pins K6 moves | OK |
| 15 | `## RECORDS` no longer says BASE `279c99ce` as BASE | :93 keeps `279c99ce…` only as the drafter's `rev-parse` result, labelled "the drafted BASE; the header BASE is now `40e646ed`"; the old "F4 is NOT on main at BASE" line is gone, :94 says F4 is on main at `40e646ed` | OK (NOTE) |
| 16 | `git diff HEAD -- <card>` (check 4) | empty | OK |
| 17 | `grep -c -i GRANT` on card, vs `CARD.md` migration checklist item 4 | `0`: K6 names no `GRANT ... TO cobalt_apply_system`, though `0025_dml_roles` is on main and `test_dml_roles_db.py` (G1b) fails a side table without a grant | OK (NOTE) |

## ISSUES
- NOTE · check 15 · `## RECORDS` :93 still prints `279c99ce…`, as the drafter's historical `rev-parse` and labelled as superseded; it no longer claims BASE.
- NOTE · check 17 · K6 does not mention the new table's `GRANT SELECT, INSERT, UPDATE, DELETE ON system.market_checkpoints TO cobalt_apply_system` and sequence `GRANT USAGE` (`CARD.md` migration checklist item 4, card 448). Not a round-3 check and not in this round's list; the builder or check should catch it via `test_dml_roles_db.py` G1b. The desk may add it to K6 before launch.
- NOTE · line cites drifted at BASE (`daily_note_path` :250, `validate` :550, `K16.1` :623, `no_resident_reads` :356, `AT_END` default :732); the card says re-find by content.
- NOTE · `## CHECK ASKS` X2/X3 share labels with the owed-before-load X2/X3 (Groups capture, 30 calls); the FOR THE CHECK line spells out each.
- NOTE · Header `CLASS`, `INSTALL` are not CARD.md keys (as r1-r3).
- NOTE · `<reason>` and `<kind>` in K2/K4 are runtime message templates, not unfilled tokens.

PREFLIGHT DONE · card: f5-checkpoints-1018 · checks: 17 · fails: 0 · ready: YES
