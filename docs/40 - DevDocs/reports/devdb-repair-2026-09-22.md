# DEV-DB REPAIR — run 3, 2026-09-23 (seat `devdb-repair-0922`, prompt `68-devdb-repair.md`)

Run 1 (2026-09-22 22:12 EDT) ended `FAILED: PREFLIGHT Q3`, nothing changed (committed `777a7a0`). Run 2 (2026-09-23 07:07 EDT) ended `FAILED: D6` (stale `tail -n 3` gate), nothing changed, dump file left in the container (committed `53102ea`). This run starts again from AUTHORIZATION (R0 `Wed Sep 23 07:13:36 EDT 2026`).

## §0 Headline
- **`cobalt_dev` repaired** (07:13–07:18 EDT). Steps: dump, rename aside, restore, migrate to `0011`. PROOF: every table has `dropped` 0, and `aset_sizings` max_attnum went from 1586 to 54. Each table is in exactly one schema, and `has_head` is true.
- With-DB tests on `f567eeb`: tenancy **34/0**, and the three r3 CLOSE tests that went red **3/0**. The dev-DB lane is open for `31`, `27` and the setups CLOSE re-run.
- The root cause is measured: each `TestMigrationRoundTrip` run adds **28** dropped slots to `aset_sizings`, so about **53 runs** are left before the 1,600 cap.
- `cobalt_dev_bloated_0922` is KEPT (144,743,447 B). The dump file has been removed. ESCALATE: 3.

## L74
- 07:13 EDT: a system-reminder block arrived with the Read tool result of the prompt file. It asked for a `Claude-Session:` commit trailer and named a file-send tool (`SendUserFile`). Recorded once as DATA and not followed.

## AUTHORIZATION
| check | command | exit | result |
|---|---|---|---|
| NEW strings approved | `grep -n -F "cobalt_dev_bloated_0922" …/cto-2026-09-22.md …/cto-2026-09-23.md` | 0 | `cto-2026-09-22.md:43` **R122**, his words: "Approved". APPROVED VERBATIM for `68-devdb-repair.md` only: the 15 NEW strings + 3 NEW denies. (`:40` R125 also matched, the run-1 FAILED launch row.) |
| committed | `git -C … log -1 --format=%H -S"cobalt_dev_bloated_0922" -- "…/cto-2026-09-2*.md"` | 0 | `777a7a0415349bf64a0a5673b017fc0f20294847` |
| Q3 size probe approved | `grep -n -F "Q3 size probe" …` | 0 | `cto-2026-09-23.md:15` **R12** (his R4(c) "Everything waiting for me is approved." covering D0's string) · `:19` **R16** |
| committed | `git -C … log -1 --format=%H -S"Q3 size probe" -- …` | 0 | `f567eebbda9a2088900c42c725f2a58d1b9970bb` |
| launch row | `grep -n "68-devdb-repair.md" …` | 0 | `cto-2026-09-23.md:19` **R16**: DESK LAUNCH ROW for `68-devdb-repair.md` (relaunch after R14). D6 string per **R15** (`:18`, his words "Approved": `tail -n 8`). Also matched: R12, R124, R122. |
| committed | `git -C … log -1 --format=%H -S"68-devdb-repair.md" -- …` | 0 | `f567eebbda9a2088900c42c725f2a58d1b9970bb` |

Verdict: AUTHORIZED (R122 + R12/R4(c) + R15 + R16, all committed).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| R0 | `date` | 0 | `Wed Sep 23 07:13:36 EDT 2026` |
| R1 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`. The lane is free. |
| R2 | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M configs/cobalt/rules.yaml` · ` M "docs/40 - DevDocs/reports/devdb-repair-2026-09-22.md"` (this report) · ` M "docs/40 - DevDocs/reports/radar-benchmark-load-2026-09-22.md"` · ` M "docs/40 - DevDocs/reports/seat-usage.md"` · `?? "docs/40 - DevDocs/reports/.grok-stdout-2026-09-22.tmp"` · `?? "docs/40 - DevDocs/reports/day-open-2026-09-22.md"` · `?? "docs/40 - DevDocs/reports/day-open-2026-09-23.md"` · `?? "docs/40 - DevDocs/reports/s2-smoke-fix-check-2026-09-23.md"` |
| R3 | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `f567eeb docs(desk): 09-23 R15 D6 tail -n 8 (his word, L67 override), R16 68 relaunch row` |
| R4 | `ls /Users/cobalt/cobalt/src/cobalt/db_migrations` | 0 | `0001_schemas.sql` … `0011_archive_incidents.sql` (+ `.rollback.sql` 0002–0011). **`<HEAD>` = `0011` (`0011_archive_incidents.sql`)** |
| Q1 | listed string | 0 | see below |
| Q2 | listed string | 0 | see below |
| Q3 | listed string | 0 | `[{"db": "cobalt_dev", "has_head": false}]` |
| D0 | listed string | 0 | `144743447` → **bytes = 144,743,447** |
| D1 | listed string (run after the Q reads finished) | 0 | `0` |
| D2 | listed string | 0 | `cobalt_brain` · `cobalt_dev` · `mattermost` · `postgres` · `template0` · `template1`. No `cobalt_dev_bloated_0922`. |
| D3 | `docker exec cobalt_memory df -k /tmp /var/lib/postgresql/data` | 0 | `overlay 466681856 2319060 464362796 1% /` · `mac 971350180 482465124 488885056 50% /var/lib/postgresql/data`. Gate 3 × 144,743,447 B ≈ 424,054 KB; both far above → PASS. |

Q1 (whole):
```
[{"sch": "public", "tbl": "aset_sizings", "dropped": 1560, "max_attnum": 1586}, {"sch": "public", "tbl": "day_modes", "dropped": 194, "max_attnum": 206}, {"sch": "public", "tbl": "vault_writes", "dropped": 130, "max_attnum": 145}, {"sch": "public", "tbl": "cobalt_jobs", "dropped": 130, "max_attnum": 144}, {"sch": "public", "tbl": "vault_overrides", "dropped": 130, "max_attnum": 142}, {"sch": "public", "tbl": "card_stop_edits", "dropped": 130, "max_attnum": 139}, {"sch": "public", "tbl": "card_transitions", "dropped": 130, "max_attnum": 139}, {"sch": "public", "tbl": "bars", "dropped": 0, "max_attnum": 8}, {"sch": "public", "tbl": "cobalt_kill_switch", "dropped": 0, "max_attnum": 7}, {"sch": "user", "tbl": "trade_defs", "dropped": 0, "max_attnum": 7}, {"sch": "public", "tbl": "session_blocks", "dropped": 0, "max_attnum": 7}, {"sch": "public", "tbl": "cobalt_email_sends", "dropped": 0, "max_attnum": 6}, {"sch": "public", "tbl": "cobalt_redactions", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "tunables", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "trader_settings", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "traders", "dropped": 0, "max_attnum": 3}]
```
Q2 (whole):
```
[{"tablename": "aset_sizings", "schemas": "public"}, {"tablename": "bars", "schemas": "public"}, {"tablename": "card_stop_edits", "schemas": "public"}, {"tablename": "card_transitions", "schemas": "public"}, {"tablename": "cobalt_email_sends", "schemas": "public"}, {"tablename": "cobalt_jobs", "schemas": "public"}, {"tablename": "cobalt_kill_switch", "schemas": "public"}, {"tablename": "cobalt_redactions", "schemas": "public"}, {"tablename": "day_modes", "schemas": "public"}, {"tablename": "session_blocks", "schemas": "public"}, {"tablename": "trade_defs", "schemas": "user"}, {"tablename": "trader_settings", "schemas": "user"}, {"tablename": "traders", "schemas": "user"}, {"tablename": "tunables", "schemas": "user"}, {"tablename": "vault_overrides", "schemas": "public"}, {"tablename": "vault_writes", "schemas": "public"}]
```
State vs the desk's read: **matches** (identical to runs 1 and 2). → REPAIR. Preflight done 07:14:02 EDT.

## REPAIR
| rule | command | exit | result |
|---|---|---|---|
| D4 | `docker exec cobalt_memory sh -c 'pg_dump -U "$POSTGRES_USER" --create -f /tmp/cobalt_dev-0922.sql cobalt_dev'` (background) | 0 | no output |
| D5 | `docker exec cobalt_memory ls -la /tmp/cobalt_dev-0922.sql` | 0 | `-rw-r--r-- 1 root root 74952252 Sep 23 11:14 /tmp/cobalt_dev-0922.sql` (overwrote run 2's file; container clock UTC) |
| D6 | `docker exec cobalt_memory tail -n 8 /tmp/cobalt_dev-0922.sql` | 0 | `--` · `-- PostgreSQL database dump complete` · `--` · (blank) · `\unrestrict <key>` → gate PASS. (Confirms run 2's reasoned cause: the `\unrestrict` trailer follows the complete marker.) |

| R7 | `docker exec cobalt_memory sh -c 'psql -U "$POSTGRES_USER" -d postgres -v ON_ERROR_STOP=1 -c "ALTER DATABASE cobalt_dev RENAME TO cobalt_dev_bloated_0922"'` | 0 | `ALTER DATABASE` |

| D7 | `docker exec cobalt_memory sh -c 'psql -U "$POSTGRES_USER" -d postgres -v ON_ERROR_STOP=1 -q -f /tmp/cobalt_dev-0922.sql'` (background) | 0 | no error; stdout only the dump's `SELECT` result sets: 2 × `set_config` (empty) and 9 × `setval` (7625, 767, 14503, 88, 978, 1213, 287, 29061, 1) |
| D2 again | listed string | 0 | `cobalt_brain` · `cobalt_dev` · `cobalt_dev_bloated_0922` · `mattermost` · `postgres` · `template0` · `template1` → both listed ✓ |

## MIGRATE
R9 `COBALT_ENV=dev uv run cobalt db migrate` (background) → exit 0. Verbatim:
```
cobalt db migrate — FORWARD on cobalt_dev
-- applying 0001_schemas.sql
-- applying 0002_move_tables.sql
-- applying 0003_heartbeat_vault_outcome.sql
-- applying 0004_radar_pool.sql
-- applying 0005_heartbeat_note_absent.sql
-- applying 0006_radar_score.sql
-- applying 0007_radar_cards.sql
-- applying 0008_radar_value_movers.sql
-- applying 0009_picks_missed.sql
-- applying 0010_archive_progress.sql
-- applying 0011_archive_incidents.sql

table                side    schema before -> after     rows            probe secs      digest before -> after verdict
----------------------------------------------------------------------------------------------------------------------
archive_incidents    system  - -> system                - -> 0          0.01 -> 0.00    - -> d41d8cd9         CREATED
archive_progress     system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
aset_sizings         user    public -> user             1 -> 1          0.01 -> 0.00    0824685c -> 0824685c  OK
bars                 system  public -> system           1043443 -> 1043443 5.53 -> 5.44    2769919a -> 2769919a  OK
card_dot_taps        user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
card_dots            user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
card_stop_edits      user    public -> user             1 -> 1          0.00 -> 0.00    7599f9ab -> 7599f9ab  OK
card_transitions     user    public -> user             4 -> 4          0.00 -> 0.00    f181e76b -> f181e76b  OK
cobalt_email_sends   system  public -> system           2 -> 2          0.00 -> 0.00    fba8cf9f -> fba8cf9f  OK
cobalt_jobs          system  public -> system           13 -> 13        0.00 -> 0.00    8d9b0861 -> 8d9b0861  OK
cobalt_kill_switch   system  public -> system           1 -> 1          0.00 -> 0.00    2e590e87 -> 2e590e87  OK
cobalt_redactions    system  public -> system           137 -> 137      0.00 -> 0.00    094847ab -> 094847ab  OK
day_modes            user    public -> user             2 -> 2          0.00 -> 0.00    f2ffb4d4 -> f2ffb4d4  OK
desk_grade           system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
desk_packet          system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
desk_regime          system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
missed               user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
movers_daily         system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
picks                user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
radar_membership     system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
radar_pool           system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
radar_score          system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
radar_score_receipt  user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
radar_score_run      system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
session_blocks       system  public -> system           6 -> 6          0.00 -> 0.00    b650702d -> b650702d  OK
traders              user    user -> user               1 -> 1          0.00 -> 0.00    a64e0148 -> a64e0148  OK
vault_overrides      user    public -> user             6 -> 6          0.00 -> 0.00    6a8b0520 -> 6a8b0520  OK
vault_writes         user    public -> user             184 -> 184      0.01 -> 0.01    4a965c69 -> 4a965c69  OK
----------------------------------------------------------------------------------------------------------------------
28 table(s) proven; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 25 card column(s) added by 0007. content UNCHANGED on every table.
proof cost: BEFORE 5.6 s + AFTER 5.5 s = total 11.0 s; slowest table bars (5.5 s before).
code: f567eeb (DIRTY: 8 path(s)) · /Users/cobalt/cobalt
```
Gate: last `-- applying` = `0011_archive_incidents.sql` = `<HEAD>` ✓ · summary `content UNCHANGED on every table.` ✓. (`DIRTY: 8 path(s)` = the R2 lines, none under `src/`.)

## PROOF
| rule | exit | result |
|---|---|---|
| Q1 | 0 | 31 tables, **every `dropped` = 0**. **max dropped: 0**; max `max_attnum` = 54 (`user.aset_sizings`, down from 1586) |
| Q2 | 0 | 31 tables, each in exactly ONE schema (`system` or `user`); none in `public`, none in two |
| Q3 | 0 | `[{"db": "cobalt_dev", "has_head": true}]` |

Q1 (whole):
```
[{"sch": "user", "tbl": "aset_sizings", "dropped": 0, "max_attnum": 54}, {"sch": "user", "tbl": "missed", "dropped": 0, "max_attnum": 33}, {"sch": "user", "tbl": "picks", "dropped": 0, "max_attnum": 24}, {"sch": "system", "tbl": "radar_membership", "dropped": 0, "max_attnum": 19}, {"sch": "system", "tbl": "desk_grade", "dropped": 0, "max_attnum": 18}, {"sch": "system", "tbl": "radar_pool", "dropped": 0, "max_attnum": 17}, {"sch": "user", "tbl": "card_dots", "dropped": 0, "max_attnum": 17}, {"sch": "user", "tbl": "vault_writes", "dropped": 0, "max_attnum": 16}, {"sch": "system", "tbl": "cobalt_jobs", "dropped": 0, "max_attnum": 16}, {"sch": "user", "tbl": "radar_score_receipt", "dropped": 0, "max_attnum": 16}, {"sch": "system", "tbl": "radar_score_run", "dropped": 0, "max_attnum": 15}, {"sch": "system", "tbl": "radar_score", "dropped": 0, "max_attnum": 14}, {"sch": "system", "tbl": "movers_daily", "dropped": 0, "max_attnum": 14}, {"sch": "user", "tbl": "day_modes", "dropped": 0, "max_attnum": 14}, {"sch": "user", "tbl": "vault_overrides", "dropped": 0, "max_attnum": 13}, {"sch": "system", "tbl": "desk_packet", "dropped": 0, "max_attnum": 13}, {"sch": "system", "tbl": "archive_incidents", "dropped": 0, "max_attnum": 12}, {"sch": "user", "tbl": "card_transitions", "dropped": 0, "max_attnum": 10}, {"sch": "system", "tbl": "archive_progress", "dropped": 0, "max_attnum": 10}, {"sch": "user", "tbl": "card_stop_edits", "dropped": 0, "max_attnum": 10}, {"sch": "system", "tbl": "bars", "dropped": 0, "max_attnum": 8}, {"sch": "user", "tbl": "card_dot_taps", "dropped": 0, "max_attnum": 8}, {"sch": "system", "tbl": "cobalt_kill_switch", "dropped": 0, "max_attnum": 7}, {"sch": "system", "tbl": "session_blocks", "dropped": 0, "max_attnum": 7}, {"sch": "user", "tbl": "trade_defs", "dropped": 0, "max_attnum": 7}, {"sch": "system", "tbl": "cobalt_email_sends", "dropped": 0, "max_attnum": 6}, {"sch": "system", "tbl": "desk_regime", "dropped": 0, "max_attnum": 6}, {"sch": "user", "tbl": "trader_settings", "dropped": 0, "max_attnum": 5}, {"sch": "system", "tbl": "cobalt_redactions", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "tunables", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "traders", "dropped": 0, "max_attnum": 3}]
```
Q2 (whole):
```
[{"tablename": "archive_incidents", "schemas": "system"}, {"tablename": "archive_progress", "schemas": "system"}, {"tablename": "aset_sizings", "schemas": "user"}, {"tablename": "bars", "schemas": "system"}, {"tablename": "card_dot_taps", "schemas": "user"}, {"tablename": "card_dots", "schemas": "user"}, {"tablename": "card_stop_edits", "schemas": "user"}, {"tablename": "card_transitions", "schemas": "user"}, {"tablename": "cobalt_email_sends", "schemas": "system"}, {"tablename": "cobalt_jobs", "schemas": "system"}, {"tablename": "cobalt_kill_switch", "schemas": "system"}, {"tablename": "cobalt_redactions", "schemas": "system"}, {"tablename": "day_modes", "schemas": "user"}, {"tablename": "desk_grade", "schemas": "system"}, {"tablename": "desk_packet", "schemas": "system"}, {"tablename": "desk_regime", "schemas": "system"}, {"tablename": "missed", "schemas": "user"}, {"tablename": "movers_daily", "schemas": "system"}, {"tablename": "picks", "schemas": "user"}, {"tablename": "radar_membership", "schemas": "system"}, {"tablename": "radar_pool", "schemas": "system"}, {"tablename": "radar_score", "schemas": "system"}, {"tablename": "radar_score_receipt", "schemas": "user"}, {"tablename": "radar_score_run", "schemas": "system"}, {"tablename": "session_blocks", "schemas": "system"}, {"tablename": "trade_defs", "schemas": "user"}, {"tablename": "trader_settings", "schemas": "user"}, {"tablename": "traders", "schemas": "user"}, {"tablename": "tunables", "schemas": "user"}, {"tablename": "vault_overrides", "schemas": "user"}, {"tablename": "vault_writes", "schemas": "user"}]
```
**PROOF PASS** · head: 0011 · max dropped: 0. R8 no longer applies.

## WITH-DB
| rule | command | exit | summary (verbatim) |
|---|---|---|---|
| T1 | `COBALT_ENV=dev uv run pytest -q -p no:cacheprovider tests/cobalt/test_tenancy.py` (background) | 0 | `34 passed in 58.57s` → **34/0** |

Q1 after T1 (whole):
```
[{"sch": "user", "tbl": "aset_sizings", "dropped": 28, "max_attnum": 82}, {"sch": "user", "tbl": "missed", "dropped": 0, "max_attnum": 33}, {"sch": "user", "tbl": "picks", "dropped": 0, "max_attnum": 24}, {"sch": "system", "tbl": "radar_membership", "dropped": 0, "max_attnum": 19}, {"sch": "system", "tbl": "desk_grade", "dropped": 0, "max_attnum": 18}, {"sch": "system", "tbl": "cobalt_jobs", "dropped": 2, "max_attnum": 18}, {"sch": "system", "tbl": "radar_pool", "dropped": 0, "max_attnum": 17}, {"sch": "user", "tbl": "vault_writes", "dropped": 1, "max_attnum": 17}, {"sch": "user", "tbl": "card_dots", "dropped": 0, "max_attnum": 17}, {"sch": "user", "tbl": "day_modes", "dropped": 2, "max_attnum": 16}, {"sch": "user", "tbl": "radar_score_receipt", "dropped": 0, "max_attnum": 16}, {"sch": "system", "tbl": "radar_score_run", "dropped": 0, "max_attnum": 15}, {"sch": "system", "tbl": "radar_score", "dropped": 0, "max_attnum": 14}, {"sch": "user", "tbl": "vault_overrides", "dropped": 1, "max_attnum": 14}, {"sch": "system", "tbl": "movers_daily", "dropped": 0, "max_attnum": 14}, {"sch": "system", "tbl": "desk_packet", "dropped": 0, "max_attnum": 13}, {"sch": "system", "tbl": "archive_incidents", "dropped": 0, "max_attnum": 12}, {"sch": "user", "tbl": "card_transitions", "dropped": 1, "max_attnum": 11}, {"sch": "user", "tbl": "card_stop_edits", "dropped": 1, "max_attnum": 11}, {"sch": "system", "tbl": "archive_progress", "dropped": 0, "max_attnum": 10}, {"sch": "system", "tbl": "bars", "dropped": 0, "max_attnum": 8}, {"sch": "user", "tbl": "card_dot_taps", "dropped": 0, "max_attnum": 8}, {"sch": "system", "tbl": "cobalt_kill_switch", "dropped": 0, "max_attnum": 7}, {"sch": "system", "tbl": "session_blocks", "dropped": 0, "max_attnum": 7}, {"sch": "user", "tbl": "trade_defs", "dropped": 0, "max_attnum": 7}, {"sch": "system", "tbl": "cobalt_email_sends", "dropped": 0, "max_attnum": 6}, {"sch": "system", "tbl": "desk_regime", "dropped": 0, "max_attnum": 6}, {"sch": "user", "tbl": "trader_settings", "dropped": 0, "max_attnum": 5}, {"sch": "system", "tbl": "cobalt_redactions", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "tunables", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "traders", "dropped": 0, "max_attnum": 3}]
```

| T2 | `COBALT_ENV=dev uv run pytest -q -p no:cacheprovider tests/cobalt/test_radar_score_migration.py::test_card_checks_index_and_receipt_immutability_on_cobalt_dev tests/cobalt/test_tenancy.py::TestMigrationRoundTrip::test_twice_is_idempotent_and_the_rollback_round_trips tests/cobalt/test_tenancy.py::TestMigrationRoundTrip::test_the_proof_table_names_every_ruled_table` (background) | 0 | `3 passed in 58.22s` → **3/0** |

Q1 after T2 (whole):
```
[{"sch": "user", "tbl": "aset_sizings", "dropped": 56, "max_attnum": 110}, {"sch": "user", "tbl": "missed", "dropped": 0, "max_attnum": 33}, {"sch": "user", "tbl": "picks", "dropped": 0, "max_attnum": 24}, {"sch": "system", "tbl": "cobalt_jobs", "dropped": 4, "max_attnum": 20}, {"sch": "system", "tbl": "radar_membership", "dropped": 0, "max_attnum": 19}, {"sch": "system", "tbl": "desk_grade", "dropped": 0, "max_attnum": 18}, {"sch": "user", "tbl": "day_modes", "dropped": 4, "max_attnum": 18}, {"sch": "user", "tbl": "vault_writes", "dropped": 2, "max_attnum": 18}, {"sch": "user", "tbl": "card_dots", "dropped": 0, "max_attnum": 17}, {"sch": "system", "tbl": "radar_pool", "dropped": 0, "max_attnum": 17}, {"sch": "user", "tbl": "radar_score_receipt", "dropped": 0, "max_attnum": 16}, {"sch": "user", "tbl": "vault_overrides", "dropped": 2, "max_attnum": 15}, {"sch": "system", "tbl": "radar_score_run", "dropped": 0, "max_attnum": 15}, {"sch": "system", "tbl": "radar_score", "dropped": 0, "max_attnum": 14}, {"sch": "system", "tbl": "movers_daily", "dropped": 0, "max_attnum": 14}, {"sch": "system", "tbl": "desk_packet", "dropped": 0, "max_attnum": 13}, {"sch": "user", "tbl": "card_stop_edits", "dropped": 2, "max_attnum": 12}, {"sch": "user", "tbl": "card_transitions", "dropped": 2, "max_attnum": 12}, {"sch": "system", "tbl": "archive_incidents", "dropped": 0, "max_attnum": 12}, {"sch": "system", "tbl": "archive_progress", "dropped": 0, "max_attnum": 10}, {"sch": "system", "tbl": "bars", "dropped": 0, "max_attnum": 8}, {"sch": "user", "tbl": "card_dot_taps", "dropped": 0, "max_attnum": 8}, {"sch": "system", "tbl": "cobalt_kill_switch", "dropped": 0, "max_attnum": 7}, {"sch": "system", "tbl": "session_blocks", "dropped": 0, "max_attnum": 7}, {"sch": "user", "tbl": "trade_defs", "dropped": 0, "max_attnum": 7}, {"sch": "system", "tbl": "cobalt_email_sends", "dropped": 0, "max_attnum": 6}, {"sch": "system", "tbl": "desk_regime", "dropped": 0, "max_attnum": 6}, {"sch": "user", "tbl": "trader_settings", "dropped": 0, "max_attnum": 5}, {"sch": "system", "tbl": "cobalt_redactions", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "tunables", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "traders", "dropped": 0, "max_attnum": 3}]
```

Per-run growth (`dropped`: PROOF → after T1 → after T2). Tables not listed stayed at 0.
| table | PROOF | after T1 | after T2 | per run |
|---|---|---|---|---|
| user.aset_sizings | 0 | 28 | 56 | +28 |
| system.cobalt_jobs | 0 | 2 | 4 | +2 |
| user.day_modes | 0 | 2 | 4 | +2 |
| user.vault_writes | 0 | 1 | 2 | +1 |
| user.vault_overrides | 0 | 1 | 2 | +1 |
| user.card_stop_edits | 0 | 1 | 2 | +1 |
| user.card_transitions | 0 | 1 | 2 | +1 |

Reds: none.

## CLEANUP
| rule | command | exit | result |
|---|---|---|---|
| R10 | `docker exec cobalt_memory rm /tmp/cobalt_dev-0922.sql` | 0 | no output |
| D5 | `docker exec cobalt_memory ls -la /tmp/cobalt_dev-0922.sql` | 2 | `ls: cannot access '/tmp/cobalt_dev-0922.sql': No such file or directory` ✓ |
| R2 | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | identical to the first R2 (8 lines). The only line that is this seat's is ` M …/devdb-repair-2026-09-22.md` (this report) ✓ |
| — | `date` | 0 | `Wed Sep 23 07:18:14 EDT 2026` |

`cobalt_dev_bloated_0922` is KEPT as the rollback copy. Dropping it is the desk's call, with his word.

## ROOT CAUSE (ops item — NOT built here)
- **The test that grows the counts:** `tests/cobalt/test_tenancy.py` `TestMigrationRoundTrip`. It runs the real CLI in a subprocess, so `--rollback --down-to 0001` and the re-`migrate` both COMMIT on `cobalt_dev`. Every reverse script's `ALTER TABLE … DROP COLUMN` leaves one dropped `attnum` slot, and the forward re-apply takes a new slot. T1 (the whole file) and T2 (the round-trip tests plus the radar test) each added exactly one round trip's worth, which shows that one with-DB run = one round trip.
- **Growth per run (measured):** `aset_sizings` +28 (the 25 radar-card columns of `0007`, plus `user_id` and 2 more from the reverse chain) · `cobalt_jobs` +2 · `day_modes` +2 · `vault_writes`, `vault_overrides`, `card_stop_edits` and `card_transitions` +1 each.
- **Runs left:** (1600 − 110) ÷ 28 = **53** with-DB runs of any worktree before `aset_sizings` hits 1,600 again (counted from after T2). Each future FORWARD migration that adds columns to `aset_sizings` shortens this.
- **Fix shapes (one line each, no pick):**
  - (a) Run the round trip against a scratch DATABASE that the test creates and drops (e.g. `cobalt_dev_rt`), through a guarded helper. `assert_destructive_target` would have to learn that name.
  - (b) Keep the round trip, but rebuild the touched tables afterwards (dump/restore or `CREATE TABLE … AS`).
  - (c) Make the reverse scripts recreate the table instead of using `ALTER … DROP COLUMN`.
  - (d) A guarded `cobalt.devdb --rebuild` verb that runs THIS repair behind `assert_destructive_target()`, so the next repair is not raw.
- **NAMED GAP:** `assert_destructive_target()` has no rebuild or restore verb at all.

## ESCALATE
1. **The raw-command gap (the refusal they lack):** this repair ran raw `docker exec` psql and pg_dump strings on the server that also holds `cobalt_brain` (D2 lists it). No `assert_destructive_target()` guarded them. Only the fixed strings, the deny list and his approval stood in. Carried from `r3-check-devdb-draft-2026-09-22.md` ESCALATE (a).
2. **`cobalt_dev_bloated_0922` is KEPT.** Its size before the repair was 144,743,447 B (D0). It is the rollback copy and still holds 1,560 dropped slots on `aset_sizings`. Dropping it needs the desk and his word.
3. **ROOT CAUSE ops item:** see `## ROOT CAUSE`. At +28 per with-DB run, about 53 runs are left before `cobalt_dev` hits the 1,600 cap again. Fix shapes (a)–(d) are listed with no pick. NAMED GAP: `assert_destructive_target()` has no rebuild/restore verb.
- Step-5 reds: none (T1 34/0, T2 3/0).
- ASK DESK: none raised.
- Note (no action): D6 `tail -n 8` confirmed run 2's reasoned cause. `-- PostgreSQL database dump complete` sits 4 lines above pg_dump's `\unrestrict` trailer.

## CONTINUE
next: none — run complete.

DEVDB REPAIRED · head: 0011 · max dropped: 0 · tenancy: 34/0 · r3 reds: 3/0 · ESCALATE: 3
