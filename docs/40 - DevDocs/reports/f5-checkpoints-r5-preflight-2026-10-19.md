# Card 731 `f5-checkpoints-1018` — preflight round 5 (2026-10-19)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read card header vs `CARD.md` build column | JOB, LADDER, BRANCH, WORKTREE, BASE `40e646ed`, TIP empty (the desk's), REPORT, CHECK REPORT, HOUSE B `mandatory — vault notes`, BAND HIGH, RULINGS, RESTARTS, BOOTSTRAP, all column 0 | OK |
| 2 | `git rev-parse HEAD 40e646ed` | HEAD `13e1c7e9923559e612515479db547190e091ab1b`; BASE `40e646edf7264b21191b2b63f5fbbb2dede793c7` | OK |
| 3 | `git log --oneline -3 -- <card>` | `13e1c7e9` (pin-lines amend), `1bd7766b`, `86483cd0`: card committed | OK |
| 4 | `git diff HEAD -- <card>` | empty | OK |
| 5 | `grep -n -e "ASK DESK" -e "«FILL" -e TBD -e TODO` on card | no hit | OK |
| 6 | placeholder scan `grep -o -n -E "<[A-Za-z]...>\|«...»"` on card | `<BASE>`, `<NNNN>`, `<reason>`, `<kind>`, `<tip>`; no `«FILL`. `<NNNN>` is K0's resolved number (`0026`); `<reason>`, `<kind>` sit inside runtime message strings; `<tip>` is a RECORDS command arg; TIP empty is the desk's | OK (NOTE) |
| 7 | `grep -n -e launchctl -e --add-dir -e --allowedTools -e "claude --bg" -e desk-launch` on card (R411, R412) | one hit, line 48 `## NOT IN THIS JOB`: a prohibition; no command string added to a launch line | OK |
| 8 | K0 at BASE: `git grep -n -e "def ensure_daily_note" -e "def format_stamp" -e "daily_refresh" 40e646ed -- src/cobalt/prefill configs/cobalt/prefill.yaml` | `daily.py:856 ensure_daily_note`, `:705 format_stamp`, `prefill.yaml:24 daily_refresh:` (and other `daily_refresh` lines) | OK |
| 9 | K0 at BASE: `git grep -n "label: com.cobalt.prefill-refresh" 40e646ed -- configs/cobalt/jobs.yaml` | `jobs.yaml:214` | OK |
| 10 | `ls src/cobalt/db_migrations` | ends `0024_strike_alerts.*`, `0025_dml_roles.rollback.sql`, `0025_dml_roles.sql`; no `0026` | OK |
| 11 | `grep -n FORWARD/REVERSE/0025/0026 db_migrations/__init__.py` | `FORWARD` last `0025_dml_roles.sql` :175; `REVERSE` first `0025_dml_roles.rollback.sql` :180; no `0026` | OK |
| 12 | K6/DECISION 3/RECORDS read for `0025`/`0026` | K6 `0026`, RED `FORWARD[-1].name == "0025_dml_roles.sql"`; DECISION 3 and RECORDS agree (r4 check 13 unchanged) | OK |
| 13 | r4 header/DECISION 2/K2/K4/B0/CHECK ASKS reread | DECISION 2 synthetic fixture marker; `timeout_s: 60`, `max_output_tokens: 512` each with the UNMEASURED comment; X2, X3 owed before load (B0); brain 2026-10-19 CHECK ASK present; consistent | OK |
| 14 | K4 files cell (card line 27) | names `tests/cobalt/test_modelaccess_config.py` | OK |
| 15 | K4 row text (card line 27) | "routes pin ... becomes the full list `["local.plan", "checkpoint.narrative"]`, never a subset"; "route is added after `local.plan` in the file (the loader keeps file order)" | OK |
| 16 | prove order: `grep -n routes src/cobalt/modelaccess/config.py` + read `:106-131` | `routes: dict[str, Route]` (:91); `load_routes` does `yaml.safe_load` then `ModelAccessConfig(**raw)`; a dict keeps insertion order, so a route placed after `local.plan` lists `["local.plan", "checkpoint.narrative"]` | OK |
| 17 | pin exists at HEAD: `grep -n "list(cfg.routes)" tests/cobalt/test_modelaccess_config.py` | `51:    assert list(cfg.routes) == ["local.plan"]` | OK |
| 18 | K9 files cell (card line 32) | names `tests/cobalt/test_prefill_refresh.py` | OK |
| 19 | K9 row text (card line 32) | "ONLY the readers-list pin ... gains the four checkpoint job labels ... after F4's, with the comment `# F5 card 731 K9`; nothing else in that F4-owned file changes" | OK |
| 20 | pin exists at HEAD: `grep -n -e "entry.readers ==" -e "LABEL =" tests/cobalt/test_prefill_refresh.py` | `351: LABEL = "com.cobalt.prefill-refresh"`, `391: assert entry.readers == ["com.cobalt.prefill-daily", self.LABEL]` | OK |
| 21 | NOT IN THIS JOB (card line 45) | "Any F4-owned line, except these two pin lines (K4, K9): ..." | OK |

## ISSUES
- NOTE · check 6 · `<reason>`, `<kind>` are runtime message templates in K2/K4; `<NNNN>` is K0's resolved `0026`; `<tip>` is a command argument; none is an unfilled token.
- NOTE · K6 does not name the `GRANT SELECT, INSERT, UPDATE, DELETE ON system.market_checkpoints TO cobalt_apply_system` and sequence `GRANT USAGE` (`CARD.md` migration checklist item 4); carried from r4, `test_dml_roles_db.py` G1b would catch it. The desk may add it before launch.
- NOTE · line cites drift at BASE (card says re-find by content); header `CLASS`, `INSTALL` are not CARD.md keys (as r1-r4).
- NOTE · the K9 pin test sits in F4-owned `test_prefill_refresh.py`; the fence admits exactly that one line and K4's, no more.

PREFLIGHT DONE · card: f5-checkpoints-1018 · checks: 21 · fails: 0 · ready: YES
