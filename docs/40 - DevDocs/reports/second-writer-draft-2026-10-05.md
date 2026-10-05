# second-writer-draft — the survey prompt (2026-10-05)

## §0 Headline
- Drafted `prompts/2026-10-05/01-second-writer-survey.md`: Sonnet survey `second-writer-survey`, read-only, never the lock. It answers Q1 (34 ticks, every 10 min, 18:00–23:30 ET, lock free only), Q2 (redaction rows by channel and minute against gate windows) and Q3 (all four 10-04 deadlocks, server log plus gate logs).
- Server log: Docker container `cobalt_memory` stderr (no logging lines in `postgresql.conf`, no `log/` in PGDATA). Reading it needs `docker logs`, which is not in the launch line (DECISION 1).
- In all four deadlocks the waiter and blocker pids differ by only 2–12. Both backends opened within a few connections of each other, which fits two connections of one run as well as an outside writer. The survey settles which.
- No launchd job runs on `cobalt_dev`: all 14 `com.cobalt.*` plists set `COBALT_ENV=production`. The archiver runs Mon–Fri only, so the K3 "archiver in the reset window" reading does not fit Sunday 10-04.
- Decisions: 6. Each one's default is in the prompt.

## SOURCES
- `reports/brain-direction-2026-10-02.md:96`: the direction row asks which process or test writes `cobalt_dev` outside the suite's own transaction, and whether it is the deadlock's other backend. It calls for a survey, then Opus.
- `reports/drc-d5-check-2026-10-04.md:197`–`:198`, `:234`–`:235`: D5 gates 1 and 2. Logs `drc-d5-1004-all-20261004-232844.log` and `-234415.log`; the lock waits were 3 and 5 min; the reds are on `card_transitions` and `vault_writes` in 0002.
- `reports/drc-k3-check-2026-10-04.md:188`–`:209`, `:273`: K3 gates 1 and 2. Logs `-195726.log` (pass 2, after the forward) and `-201354.log` (pass 1); both are `system.bars` (relation 165614). `:209` names the archiver as an unproven reading.
- Gate-log DETAIL lines: `-195726.log:1093`–`:1094` (1863164→1863162, xid 3631487); `-201354.log:964`–`:965` (1864558→1864552, xid 3641233); `-232844.log:977`–`:978` (1872014→1872009, rel 165626, xid 3682889); `-234415.log:966`–`:967` (1875138→1875126, rel 165692, xid 3704153). All four are database 165601. `-232844.log:979` reads `HINT: See server log for query details.`
- `-232844.log` traceback: the red is fixture `migrated` → `tests/cobalt/test_drc_store.py:237` `_apply(conn, FORWARD)`. That fixture opens its own `db.connect_migration` connection (`test_drc_store.py:231`–`:233`).
- `.gate-logs/` listing: `f15-p2-1004-all-20261004-234155.log` ran 23:41–23:59, overlapping D5 gate 2. `cobalt-guard-b-1004` offline and livenote ran every ~15 min from 18:49 to 20:38; they run outside the lock.
- `ops/desk/take-devdb-lock.sh`: the lock is `mkdir /Users/cobalt/cobalt-wt/.cobalt_dev.lock`, plus an `owner` file and a `.env` copy from `/Users/cobalt/cobalt/.env`. `release-devdb-lock.sh` removes both.
- `ops/desk/gate.sh:265`–`:289` (the take waits); `:422`–`:501` (withdb: pass 1, forward, pass 2, rollback). `ops/desk/gate-lists.md:18`: OFFLINE carries no `COBALT_ENV`. `:21`–`:42`: every with-DB line is `COBALT_ENV=dev`.
- `ls /Users/cobalt/cobalt/.env`: present (mode 600). So any `COBALT_ENV=dev` process whose cwd is the main checkout reaches `cobalt_dev` with no lock. This is a lead in the prompt's step 4.
- `reports/devdb-parallel-question-2026-10-02.md:9`, `:26`: Postgres, Mattermost and the LLM all run in Docker on this Mac. `devdb-parallel-answer-2026-10-02.md:9`, `:63`, `:72`: there is one Postgres server, shared with production; Docker commands are outside every worker's list.
- `LAWS.md:375`–`:376` (L76): one owner and one lock; a with-DB step takes the lock only through the scripts.
- `cto-desk-checklist.md:46` (L17): every helper is a `--bg` session with rc + tab, and surveys run on Sonnet.
- `grep -l` over `~/Library/LaunchAgents/`: `com.cobalt.agent`, `mainframe`, `archiver` and `aset` match only on the RULING 7 comment `dev -> cobalt_dev`. Every `com.cobalt.*` plist sets `COBALT_ENV` `production`. Archiver: `StartCalendarInterval` Weekday 1–5 at 20:30 (`com.cobalt.archiver.plist:54`–`:60`).
- `docker-compose.yml:2`–`:16`: service `db`, `pgvector/pgvector:pg16`, `container_name: cobalt_memory`, data at `./data/postgres`. `data/postgres/postgresql.conf:455`, `:462`, `:570`, `:594`: logging settings are all commented out (stderr, collector off, `'%m [%p] '`, lock waits off). PGDATA has no `log/` directory.
- `src/cobalt/redact/store.py:43`, `:54`: `record` calls `ensure_schema()` (CREATE … IF NOT EXISTS) on its own connection, then INSERTs. `src/cobalt/redact/guard.py:186` calls it on every redaction hit. `src/cobalt/db_migrations/cli.py:684`–`:688` and `tests/cobalt/test_migrate_proof.py:686`: the table "drifted 118 → 121 rows during one afternoon on dev".
- `tests/cobalt/conftest.py:1`–`:40`, `:195`–`:206`: every test is pinned to `COBALT_ENV=dev`. `db.connect` is patched to a savepoint proxy on one real connection that is rolled back. Rows that persist must come from a connection outside that proxy.
- `src/cobalt/db_query.py:20`–`:27`, `:142`–`:178`: `cobalt db query` refuses write words and `pg_read_file`, runs `BEGIN READ ONLY` with a statement timeout, and always rolls back. `db.py` sets no `application_name` (grep: nothing), so `application_name` is likely empty.
- `prompts/2026-10-04/04-draft-s3-reread.md`: the shape followed (tags line with the full launch line, then the body).

## DECISIONS
- ASK DESK 1: Docker runs Postgres, and the server log is `docker logs cobalt_memory`. That string is outside every worker's list (`devdb-parallel-answer:63`), and a new permission string is Dejan's per L78. Add `"Bash(docker logs --timestamps --since 2026-10-04T19:55:00-04:00 --until 2026-10-05T00:05:00-04:00 cobalt_memory)"` to the launch line? [00:10 EDT] Default taken: not added. The survey runs it once; if refused, it records `server log: not read`, writes the command for the desk and settles Q3 from the gate logs.
- ASK DESK 2: there are four new read-only host strings: `lsof -nP -iTCP:5432*`, `lsof -a -p *`, `ps -o *` (process attribution; env printing disallowed) and `sleep *` (the tick wait, `run_in_background`). Strike any? [00:10 EDT] Default taken: all four are in the launch line, because Q1 cannot name a process without them.
- ASK DESK 3: the sampling window. [00:10 EDT] Default taken: 2026-10-05 18:00–23:30 ET, every 10 min, 34 ticks. This covers Monday's 20:30 archiver run and the evening's gate traffic. The desk launches at 17:5x.
- ASK DESK 4: may the survey read `cobalt_dev` while a hub holds the lock? Its reads only take AccessShare, but they would share the gate's tables. [00:10 EDT] Default taken: no reads while the lock dir exists, per the brief. The tick records the owner, and Q3 rests on the logs.
- ASK DESK 5: `--side system` may not be a member of `pg_read_all_stats`. If not, `pg_stat_activity.query` reads `<insufficient privilege>` for other roles' backends. [00:10 EDT] Default taken: the survey reads and records membership (step 1) and changes no role. Pid, start and state still show.
- ASK DESK 6: the brief allows `psql` or `cobalt db query`. [00:10 EDT] Default taken: `cobalt db query` only. It is the guarded read-only path, and `psql` would need the password from `.env` (L4/L41).

## RECORDS
- Files written: `docs/40 - DevDocs/prompts/2026-10-05/01-second-writer-survey.md` (new) and this report. Nothing was committed (no git write).
- Read: the brief, the direction row, both check reports, the four red gate logs (DETAIL lines and the D5-1 traceback `:920`–`:985`) and the `.gate-logs/` listing. Also the lock scripts, `gate.sh`, `gate-lists.md`, both devdb-parallel reports, L76, L17, `writing-rules.md` and the template prompt. Also all 14 `com.cobalt.*` plists (grep), `docker-compose.yml`, the PGDATA listing, `postgresql.conf` (grep), `redact/store.py`, `redact/guard.py:150`–`:200`, `db_query.py`, `cli.py:670`–`:710`, `test_migrate_proof.py:680`–`:760`, `tests/cobalt/conftest.py` (parts), `test_drc_store.py:215`–`:245`, `env.py` (grep) and `db.py` (grep).
- One block (L74): a system reminder asked commits to end with a `Claude-Session:` line. It is recorded once here as data. No commit was made.
- `.env` was checked by `ls` only and never read.

DRAFTED · prompt: prompts/2026-10-05/01-second-writer-survey.md · decisions: 6
