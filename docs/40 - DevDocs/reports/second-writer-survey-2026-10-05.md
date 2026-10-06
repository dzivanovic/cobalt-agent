# Second writer on `cobalt_dev` — survey 2026-10-05

## §0 Headline
- Writer: **not found**. At 4 lock-free ticks (22:41, 22:52, 23:22, 23:29 ET) no backend on `cobalt_dev`, no locks, no host connection on 5432.
- The four deadlocks have no second writer: every blocker is a Postgres **autovacuum worker** (`autovacuum: VACUUM <table>`), a server-side process, not a client.
- Each waiter (migration `0002` ALTER … OWNER TO, or `0007` once) held a lock the vacuum wanted while it waited on the vacuum's lock.
- Coverage gap: the survey started at 22:41 ET, not 18:00, so 6 of the 34 ticks ran (4 lock free, 2 held).
- Q2: `mattermost`/`jwt` is the only redaction channel; all 12 rows of 10-04 evening fall inside gate-run windows.

## Q1
| time (ET) | lock | backends | host processes | max_id |
|---|---|---|---|---|
| 22:41 | free | none | none | 2912 (301 rows) |
| 22:52 | free | none | none | 2912 (301) |
| 23:02 | held by `deploy-d5-1005` (`.env` mtime 23:00) | pid 2045232, query `<insufficient privilege>` (`sees_all_queries` = False) | pytest pid 38378, started 23:00:29, cwd `/Users/cobalt/cobalt-wt/deploy-d5-1005` | not read (held) |
| 23:12 | held by `deploy-d5-1005` | pid 2047395, query `<insufficient privilege>` | same pid 38378 | not read (held) |
| 23:22 | free | none | none | 2925 (302) |
| 23:29 | free | none | none | 2925 (302) |

- Sightings: 0. `max_id` grew 2912 → 2925 between 22:52 and 23:22, across the `deploy-d5-1005` lock hold, so the lock holder explains it.
- The `/Users/cobalt/cobalt` lead (`COBALT_ENV=dev` process with that cwd): never seen. The only host process ever on 5432 was the lock owner's pytest.
- Held-lock `pg_locks` sample at 23:02 returned no rows (pytest uses short transactions).

## Q2
- Rows since 09-28: `mattermost` / `jwt`: 124 rows, 124 hits, first 2026-09-28 14:03 UTC, last 2026-10-06 02:16 UTC (22:16 ET today).
- Channel → caller (`grep -rn "channel="`): `mattermost` ← `src/cobalt/redact/guard.py:8`, `redact/__init__.py:4`, `notify/mattermost.py:123,126,140` (`CHANNEL`); `modelaccess` ← `modelaccess/guard.py:42`, `client.py:34`; `log` ← `redact/guard.py:211` (`record=False`); `heartbeat.stage` ← `heartbeat/runner.py:328`; `jobs.last_error` ← `jobs/store.py:159,205,248,270`. Recording goes through `guard.py:186`.
- 10-04 minutes (UTC): 23:21, 23:35, 00:09, 00:25, 01:13, 02:02, 03:02, 03:43, 03:53, 04:01, 04:11, 04:31, one row each. In ET each falls inside a gate log's span (by log name and mtime): k3 191010, 192326, 195726, 201354, 210130, 215047; d5 225058, 232844; f15 234155; d5 234415 / f15 000008; f15 000008; d5 001939.
- Settle: `channel mattermost · writer pytest runs of the gate (Mattermost notify path, jwt pattern) · during gate runs`. The 10-05 evening rows (last 22:16 ET) fall inside `deploy-launcher-f5-1005-all-20261005-220231` (22:02–22:29). Writer process inferred from timing, not observed.

## Q3
Server log: container `cobalt_memory` stderr (`logging_collector` = off, `log_destination` = stderr, `log_line_prefix` = `%m [%p] `, `log_timezone` = UTC, `log_lock_waits` = off, `deadlock_timeout` = 1000). Read once with `docker logs` (saved under the session tool-results; line numbers below are in that file).

| # | gate log | server-log lines | settle |
|---|---|---|---|
| K3-1 | `drc-k3-1004-all-20261004-195726.log:1092-1094` | `:520-546`: `[1863164] ERROR: deadlock detected`; `Process 1863162: autovacuum: VACUUM system.bars`; CONTEXT `ALTER TABLE system.bars OWNER TO cobalt_system` | `blocker = autovacuum: VACUUM system.bars · other process (Postgres autovacuum)` |
| K3-2 | `drc-k3-1004-all-20261004-201354.log:963-965` | `:1192-1214`: `[1864558] deadlock detected`; `Process 1864552: autovacuum: VACUUM system.bars` | `blocker = autovacuum: VACUUM system.bars · other process (Postgres autovacuum)` |
| D5-1 | `drc-d5-1004-all-20261004-232844.log:976-981` (lock taken `:846`) | `:3422-3444`: `[1872014] deadlock detected`; `Process 1872009: autovacuum: VACUUM user.card_transitions`; CONTEXT `ALTER TABLE "user".card_transitions OWNER TO cobalt_user` | `blocker = autovacuum: VACUUM user.card_transitions · other process (Postgres autovacuum)` |
| D5-2 | `drc-d5-1004-all-20261004-234415.log:965-967` | `:4995-5021`: `[1875138] deadlock detected`; `Process 1875126: autovacuum: VACUUM user.vault_writes`; CONTEXT `ALTER TABLE "user".vault_writes OWNER TO cobalt_user`. Same minute, `:4969-4973`: `[1875126]` autovacuum on `user.card_dots` deadlocked with `[1875136]` migration 0007 (`radar cards, USER side`) | `blocker = autovacuum: VACUUM user.vault_writes · other process (Postgres autovacuum)` |

- Server-log lines are quoted from the `docker logs` output; the K3-1 `0002` statement text is cut by the server at the log's statement-length limit.
- Waiter/blocker pid gaps of 2–12 are consecutive pids from one Postgres cluster (autovacuum workers spawn near the migration's connection); the blocker is a different kind of backend, not a second connection of the run.
- Not checked: the `connect_migration` / `subprocess` grep of the test files (the settle needs no test-side connection, the blocker being autovacuum).
- Mechanism: migration `0002` runs many ALTERs in one transaction; autovacuum takes `ShareUpdateExclusiveLock` plus a `pg_class` tuple update, and the two wait on each other. Not a write outside the lock.
- Fix directions (not applied; read-only seat): disable autovacuum on the touched tables during migration, or retry on `DeadlockDetected`, or order lock acquisition.

## DECISIONS
- ASK DESK: window 18:00–23:30 had passed when the seat was launched (first command 22:41 ET), so ticks 1–28 were not taken; say whether to re-run with a seat launched at 18:00. [22:41] Default: ran the 6 ticks that fit.
- ASK DESK: should the held-lock samples record backend queries? `pg_read_all_stats` is not granted to the seat's role, so queries read `<insufficient privilege>`. [23:02] Default: recorded pid and the host process instead.

## RECORDS
All exit 0 unless noted; every DB read preceded by `ls -d` of the lock; no refusals except the one noted.
- `date` ×6; `ls -d /Users/cobalt/cobalt-wt/.cobalt_dev.lock` ×14 (exit 1 = free, exit 0 = held); Read of `…/.cobalt_dev.lock/owner` ×2.
- DB reads via `cobalt db query --side system --format table`: `pg_database`; `pg_class`; `pg_settings`; `pg_has_role`; Q2 rows; Q2 by minute; Q1 `pg_stat_activity` ×6; `pg_locks` ×4; `max(id)` ×3.
- `docker logs --timestamps --since … --until … cobalt_memory` once; `grep` on its saved output ×2; Read of its lines 518-547 and 4968-4976.
- `grep -n …` on gate logs ×4, `grep -rn "channel="` ×1, `ls -la …/.gate-logs/`, `ls -la …/*/.env` ×2.
- `lsof -nP -iTCP:5432 -sTCP:ESTABLISHED` ×6 (exit 1 = no connections at the 4 free ticks); `ps -o … -p 38378`; `lsof -a -p 38378 -d cwd`.
- `sleep 600` ×3 and `sleep 420` ×1 in the background. Refused: a foreground `sleep 560` (tool block); no other refusals.
- Not run: `ls -la /Users/cobalt/cobalt-wt/*/.env` at the free ticks (no owner to record); the test-file `grep` of Q3.

SURVEY DONE · writer: not found · — · ticks: 6 (4 lock free) · sightings: 0 · redactions: mattermost by gate pytest runs (inferred) · deadlocks settled: 4/4 · decisions: 2
