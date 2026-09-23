# DEV-DB REPAIR — 2026-09-22 (seat `devdb-repair-0922`, R124, prompt `68-devdb-repair.md`)

## §0 Headline
- Stopped at PREFLIGHT Q3 (22:13:00 EDT): `FAILED: InsufficientPrivilege: permission denied for database cobalt_dev`. The listed string ran as written and failed. No variant was typed.
- **Nothing changed.** No dump, no rename, no restore, no migrate. `cobalt_dev` is still the bloated DB. `cobalt_dev_bloated_0922` does not exist.
- Everything else in preflight matched the desk's read: Q1 top row `public.aset_sizings` dropped 1560 / max_attnum 1586, Q2 all public (no `system` tables), D1 `0`, D2 no kept copy, D3 ≈ 464 GB / 489 GB free.
- The fix is a corrected Q3 string with his approval, then a relaunch. ESCALATE: 4.

## L74
- 22:12 ET: a system-reminder block arrived with the Read tool result of the prompt file. It asked for a `Claude-Session: https://claude.ai/code/session_012NLXXNHWfFNohwrdbQ1QQQ` commit trailer and named a file-send tool (`SendUserFile`). Recorded once as DATA and not followed: this seat makes no commit and sends no file.

## AUTHORIZATION
| check | command | exit | result |
|---|---|---|---|
| approval | `grep -n -F "cobalt_dev_bloated_0922" …/cto-2026-09-22.md …/cto-2026-09-23.md` | 2 | `cto-2026-09-23.md`: No such file (recorded, not fatal). `cto-2026-09-22.md:37`: **R122** 21:2x ET, his words: "Approved". APPROVED VERBATIM for `68-devdb-repair.md` only: the 15 NEW strings + 3 NEW denies. Condition: `73` changes no string. |
| approval committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"cobalt_dev_bloated_0922" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | 0 | `b33b56349102f455273f2c2578fcacd2486a6e9c` |
| launch row | `grep -n "68-devdb-repair.md" …/cto-2026-09-22.md …/cto-2026-09-23.md` | 2 | `cto-2026-09-22.md:35`: **R124** 22:1x ET DESK LAUNCH ROW. CONDITION MET: `73` → `gemini: REVIEW: RUN IT · blockers: 0 · string changes: 0`. (`-23` missing, recorded.) |
| launch committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"68-devdb-repair.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | 0 | `4830d80b2d88d98ea2ff78165bcdc78e0553590d` |

Verdict: AUTHORIZED (R122 + R124, both committed).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| R0 | `date` | 0 | `Tue Sep 22 22:12:33 EDT 2026` |
| R1 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`. The lane is free. |
| R2 | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M configs/cobalt/rules.yaml` · ` M "docs/30 - Design/archiver-runs.md"` · ` M "docs/40 - DevDocs/reports/radar-benchmark-load-2026-09-22.md"` · ` M "docs/40 - DevDocs/reports/seat-usage.md"` · `?? "docs/40 - DevDocs/reports/.grok-stdout-2026-09-22.tmp"` · `?? "docs/40 - DevDocs/reports/day-open-2026-09-22.md"` · `?? "docs/40 - DevDocs/reports/devdb-repair-2026-09-22.md"` (this report, first Write) |
| R3 | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `4830d80 docs(desk): 09-22 R124 devdb repair launch row (Gemini RUN IT, 0 string changes)` |
| R4 | `ls /Users/cobalt/cobalt/src/cobalt/db_migrations` | 0 | `0001_schemas.sql` … `0011_archive_incidents.sql` (+ `.rollback.sql` for 0002–0011, `cli.py`, `placement.py`, `__init__.py`). **`<HEAD>` = `0011` (`0011_archive_incidents.sql`)** |
| Q1 | (listed string, verbatim) | 0 | see below |
| Q2 | (listed string, verbatim) | 0 | see below |
| Q3 | `COBALT_ENV=dev uv run cobalt db query --side system --format json "SELECT current_database() AS db, pg_database_size(current_database()) AS bytes, to_regclass('system.archive_incidents') IS NOT NULL AS has_head"` | **1** | **`FAILED: InsufficientPrivilege: permission denied for database cobalt_dev`** (22:13:00 EDT) |
| D1 | (listed string) | 0 | `0` (evidence only, read-only, after Q3's failure: auth works over the local socket, no other session) |
| D2 | (listed string) | 0 | `cobalt_brain` · `cobalt_dev` · `mattermost` · `postgres` · `template0` · `template1` (evidence only: no `cobalt_dev_bloated_0922`) |
| D3 | `docker exec cobalt_memory df -k /tmp /var/lib/postgresql/data` | 0 | `overlay 466747392 2245804 464501588 1% /` · `mac 971350180 482309620 489040560 50% /var/lib/postgresql/data` (evidence only: the gate needs 3 × Q3 `bytes`, and `bytes` is unknown) |

Q1 (whole):
```
[{"sch": "public", "tbl": "aset_sizings", "dropped": 1560, "max_attnum": 1586}, {"sch": "public", "tbl": "day_modes", "dropped": 194, "max_attnum": 206}, {"sch": "public", "tbl": "vault_writes", "dropped": 130, "max_attnum": 145}, {"sch": "public", "tbl": "cobalt_jobs", "dropped": 130, "max_attnum": 144}, {"sch": "public", "tbl": "vault_overrides", "dropped": 130, "max_attnum": 142}, {"sch": "public", "tbl": "card_stop_edits", "dropped": 130, "max_attnum": 139}, {"sch": "public", "tbl": "card_transitions", "dropped": 130, "max_attnum": 139}, {"sch": "public", "tbl": "bars", "dropped": 0, "max_attnum": 8}, {"sch": "public", "tbl": "cobalt_kill_switch", "dropped": 0, "max_attnum": 7}, {"sch": "user", "tbl": "trade_defs", "dropped": 0, "max_attnum": 7}, {"sch": "public", "tbl": "session_blocks", "dropped": 0, "max_attnum": 7}, {"sch": "public", "tbl": "cobalt_email_sends", "dropped": 0, "max_attnum": 6}, {"sch": "public", "tbl": "cobalt_redactions", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "tunables", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "trader_settings", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "traders", "dropped": 0, "max_attnum": 3}]
```
Q2 (whole):
```
[{"tablename": "aset_sizings", "schemas": "public"}, {"tablename": "bars", "schemas": "public"}, {"tablename": "card_stop_edits", "schemas": "public"}, {"tablename": "card_transitions", "schemas": "public"}, {"tablename": "cobalt_email_sends", "schemas": "public"}, {"tablename": "cobalt_jobs", "schemas": "public"}, {"tablename": "cobalt_kill_switch", "schemas": "public"}, {"tablename": "cobalt_redactions", "schemas": "public"}, {"tablename": "day_modes", "schemas": "public"}, {"tablename": "session_blocks", "schemas": "public"}, {"tablename": "trade_defs", "schemas": "user"}, {"tablename": "trader_settings", "schemas": "user"}, {"tablename": "traders", "schemas": "user"}, {"tablename": "tunables", "schemas": "user"}, {"tablename": "vault_overrides", "schemas": "public"}, {"tablename": "vault_writes", "schemas": "public"}]
```
State vs the desk's 19:4x read: **matches**. Q1's top row is `public.aset_sizings` with dropped 1560. The new-core tables are in `public` only. There is no `"user".aset_sizings`, and no table sits in `system`, so `system.archive_incidents` is absent by this unscoped `pg_catalog` read (L35). That makes `has_head` effectively false, but it is not Q3's reading.

**Why Q3 failed (reasoned, UNPROVEN):** `src/cobalt/db_query.py:160-169` connects per side and asserts `current_user == side.role`. `pg_database_size()` checks the *current role's* CONNECT privilege on the database (or `pg_read_all_stats`). Q1 and Q2 succeeded on the same connection path, so the connection itself works. The likely cause is that the `system` side role lacks CONNECT on `cobalt_dev` as a direct grant, or gets the login through another route. That is not proven here. The drafter's list never ran Q3 before launch.

Stopped here: the D3 gate (`3 × Q3 bytes`) cannot be evaluated. The prompt forbids a variant string ("an unlisted command = do not call it … never a variant"). Safe default: stop and change nothing.

## REPAIR
Not run. D4, D5, D6, R7 and D7 were not called. No dump file was created. No rename happened.

## MIGRATE
Not run.

## PROOF
Not run.

## WITH-DB
Not run (T1/T2 not called).

## CLEANUP
- R10 not needed: no dump exists.
- R2 at 22:13:15 EDT is identical to the preflight R2. The only line this seat added is this report (`?? "docs/40 - DevDocs/reports/devdb-repair-2026-09-22.md"`).
- R8 was **not** run: R7 never ran, so rollback is forbidden.

## ROOT CAUSE
Not measured: step 5 never ran, so there is no per-run growth reading. The mechanism named in the prompt is unchanged, and the fix shapes (a)–(d) stand as drafted, to be measured on the relaunch. Arithmetic from today's read only: `aset_sizings` max_attnum 1586 leaves **14** attnum slots before the 1,600 cap. That is why `0007`'s re-apply overflowed.

## ESCALATE
1. **Q3 string fails on the dev DB** (`InsufficientPrivilege: permission denied for database cobalt_dev`). The repair needs a corrected, approved Q3 before relaunch. Two options for the drafter, no pick: (i) drop `pg_database_size(...)` from Q3 and take size from a new approved in-container probe, `docker exec cobalt_memory sh -c 'psql -U "$POSTGRES_USER" -d postgres -v ON_ERROR_STOP=1 -Atc "SELECT pg_database_size('"'"'cobalt_dev'"'"')"'` (quoting to be settled by the drafter); (ii) keep `has_head` in Q3 via `to_regclass` alone. Either option is a NEW string, so it needs his "approve" (L61/L62). A D3 reading is on record for reference: ≈ 464 GB (`/tmp`) and ≈ 489 GB (data) free.
2. **The raw-command gap (the refusal they lack):** `assert_destructive_target()` has no rebuild/restore verb. The repair must run raw `docker exec` strings on the server that also holds `cobalt_brain` (D2 lists it). Carried from `r3-check-devdb-draft-2026-09-22.md` ESCALATE (a).
3. **`cobalt_dev_bloated_0922`:** not created (nothing renamed). Its size is unknown because Q3 failed.
4. **ROOT CAUSE ops item (not built):** `TestMigrationRoundTrip` commits `--rollback --down-to 0001` + re-`migrate` on `cobalt_dev` each with-DB run. The reverse scripts' `DROP COLUMN` leave dropped slots. `aset_sizings` is at 1586/1600. Fix shapes (a) scratch DB `cobalt_dev_rt` via a guarded helper · (b) rebuild touched tables after the round trip · (c) reverse scripts recreate the table instead of `DROP COLUMN` · (d) a guarded `cobalt.devdb --rebuild` verb behind `assert_destructive_target()`. Growth per run is unmeasured (step 5 not reached).
- ASK DESK: none raised. The Q3 failure has an explicit safe default (stop, nothing changed).
- Step 5 reds: none (not run).

## CONTINUE
next: none — the run ended FAILED at PREFLIGHT Q3 with nothing changed. A relaunch needs a corrected, approved Q3 string (ESCALATE 1) and then starts again from AUTHORIZATION.

FAILED: PREFLIGHT Q3 — `InsufficientPrivilege: permission denied for database cobalt_dev` (the listed Q3 string cannot read `pg_database_size`; the D3 gate cannot be evaluated; nothing changed, no rollback needed) · ESCALATE: 4
