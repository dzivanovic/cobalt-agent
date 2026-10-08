## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | Read 115 vs 52 launch and allow lines | allowedTools and disallowedTools lists identical; only seat name (`radar-cards-survey`), prompt path and date differ | OK |
| 2 | Read 115 line 2 | `RULINGS: 2026-10-08 R678` | OK |
| 3 | grep R678 in `cto-2026-10-08.md`; `git log` on it | line 31: `HIS RULING · APPROVED`; committed (ac9d14cb, 1f9547d4) | OK |
| 4 | Count reads in 115 | 5 reads, each one `SELECT`, no write, no new command or argument beyond 52's allow line (R411, R412) | OK |
| 5 | `store.py` grep | `RADAR_OPEN_STATES` at :968; `radar_board_cards` at :1047, query args :1056 | OK |
| 6 | `db_migrations/placement.py` grep | :28 aset_sizings USER; :40 session_blocks SYSTEM; :66 radar_pool SYSTEM; :69 radar_score_run SYSTEM; :70 radar_score SYSTEM (prompt writes bare `placement.py`; file is `src/cobalt/db_migrations/placement.py`) | OK |
| 7 | `0004_radar_pool.sql` grep | pool_key :6; state :7; failed_stage :11-12; members :17; poll_failures :22 | OK |
| 8 | `0006_radar_score.sql` grep | failed_stage CHECK adds `'evaluate'` :58-59; radar_score_run :66, started_at :72; radar_score :92, run_id :94, membership_id :95, trade_def_md5 :97, evaluation :99-100 includes `'formed'` | OK |
| 9 | `0007_radar_cards.sql` grep | view :214; `c.created_at … c.state, c.state_at` :215; `WHERE c.origin = 'radar'` :233 | OK |
| 10 | aset migrations grep | `0001:8` created_at; `0006:22` state, `:26` state_at; `0008:23` origin; `0002_move_tables.sql:46` aset_sizings | OK |
| 11 | session grep | `0001_session_blocks.sql:15` ts; `0002_session_blocks_kind.sql:19` kind; `session/store.py:126` groups by kind | OK |
| 12 | `--side system` for reads 3-5 | radar_pool, session_blocks, radar_score(_run) all SYSTEM, matches the draft report | OK |
| 13 | secrets scan | no secret in any read, argument or log; counts only, no ticker names (L4) | OK |
| 14 | cause rule, report path, stop line | `display` / `card-writing` / `none` stated; report path `reports/radar-cards-survey-2026-10-08.md` (absent, `ls`); last line `READ DONE … / FAILED:` | OK |
| 15 | `git log`/`git status` on prompt 115 and the draft report | both in a4baadd5, clean | OK |

## ISSUES
- NOTE: prompt line 16 cites `placement.py:28` without the directory; the file is `src/cobalt/db_migrations/placement.py`. Not a fail.
- NOTE: the draft's block-name decision (`session_blocks.kind`) is the desk's kept default; `kind` CHECK allows only `'refused'`, `'ungated_run'`. Not failed.

PREFLIGHT DONE · card: radar-cards-survey-115 · checks: 15 · fails: 0 · ready: YES
