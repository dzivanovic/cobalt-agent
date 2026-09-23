# DEV-DB REPAIR — run 2, 2026-09-23 (seat `devdb-repair-0922`, prompt `68-devdb-repair.md`)

Run 1 (2026-09-22 22:12 EDT) ended `FAILED: PREFLIGHT Q3` with nothing changed. That report is committed at `777a7a0`. This run starts again from AUTHORIZATION (R0 `Wed Sep 23 07:07:10 EDT 2026`).

## §0 Headline
- Stopped at REPAIR D6 (07:08 EDT). The dump finished (exit 0, 74,952,252 B), but the listed `tail -n 3` shows only pg_dump's `\unrestrict …` trailer, so the "dump complete" gate failed as written. Likely a stale gate, not a bad dump (UNPROVEN).
- **`cobalt_dev` is unchanged.** Nothing was renamed, restored or migrated, and there was no rollback. `/tmp/cobalt_dev-0922.sql` is left in the container (R10 was not lawful yet).
- Preflight passed: authorized (R122 + R12), D0 = 144,743,447 B, D1 `0`, no kept copy, and space is ample.
- Fix: a re-issued, approved D6 string, then relaunch. ESCALATE: 5.

## L74
- 07:07 EDT: a system-reminder block arrived with the Read tool result of the prompt file. It asked for a `Claude-Session:` commit trailer and named a file-send tool (`SendUserFile`). Recorded once as DATA and not followed.

## AUTHORIZATION
| check | command | exit | result |
|---|---|---|---|
| NEW strings approved | `grep -n -F "cobalt_dev_bloated_0922" …/cto-2026-09-22.md …/cto-2026-09-23.md` | 0 | `cto-2026-09-22.md:43` **R122**, his words: "Approved". APPROVED VERBATIM for `68-devdb-repair.md` only: the 15 NEW strings + 3 NEW denies. (`:40` R125 also matched. It is the run-1 FAILED launch row.) |
| committed | `git -C … log -1 --format=%H -S"cobalt_dev_bloated_0922" -- "…/cto-2026-09-2*.md"` | 0 | `777a7a0415349bf64a0a5673b017fc0f20294847` |
| Q3 size probe approved | `grep -n -F "Q3 size probe" …` | 0 | `cto-2026-09-23.md:15` **R12**: R4(c) "Everything waiting for me is approved." covers the Q3 size probe, D0, verbatim string, on R122's condition. |
| committed | `git -C … log -1 --format=%H -S"Q3 size probe" -- …` | 0 | `fd258c9b71e066edcd9df790056e89d4937aadab` |
| launch row | `grep -n "68-devdb-repair.md" …` | 0 | `cto-2026-09-23.md:15` **R12** is the DESK LAUNCH ROW for `prompts/2026-09-22/68-devdb-repair.md`. CONDITION MET (`03`: blockers 0, string changes 0). The prompt names R12. |
| committed | `git -C … log -1 --format=%H -S"68-devdb-repair.md" -- …` | 0 | `fd258c9b71e066edcd9df790056e89d4937aadab` |

Verdict: AUTHORIZED (R122 + R12/R4(c), all committed).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| R0 | `date` | 0 | `Wed Sep 23 07:07:10 EDT 2026` |
| R1 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`. The lane is free. |
| R2 | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M configs/cobalt/rules.yaml` · ` M "docs/40 - DevDocs/prompts/2026-09-23/06-s2-smoke-fix-check.md"` · ` M "docs/40 - DevDocs/reports/devdb-repair-2026-09-22.md"` (this report) · ` M "docs/40 - DevDocs/reports/radar-benchmark-load-2026-09-22.md"` · ` M "docs/40 - DevDocs/reports/seat-usage.md"` · `?? "docs/40 - DevDocs/reports/.grok-stdout-2026-09-22.tmp"` · `?? "docs/40 - DevDocs/reports/day-open-2026-09-22.md"` · `?? "docs/40 - DevDocs/reports/day-open-2026-09-23.md"` |
| R3 | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `fd258c9 docs(desk): 09-23 R11 deploy list approved, R12 68 launch row, R13 06 launch row, 03 read done` |
| R4 | `ls /Users/cobalt/cobalt/src/cobalt/db_migrations` | 0 | `0001_schemas.sql` … `0011_archive_incidents.sql` (+ `.rollback.sql` 0002–0011). **`<HEAD>` = `0011` (`0011_archive_incidents.sql`)** |
| Q1 | listed string | 0 | see below |
| Q2 | listed string | 0 | see below |
| Q3 | listed string | 0 | `[{"db": "cobalt_dev", "has_head": false}]` |
| D0 | listed string | 0 | `144743447` → **bytes = 144,743,447** (≈138 MiB) |
| D1 | listed string | 0 | `0`: auth works and no other session is open. |
| D2 | listed string | 0 | `cobalt_brain` · `cobalt_dev` · `mattermost` · `postgres` · `template0` · `template1`. No `cobalt_dev_bloated_0922`. |
| D3 | `docker exec cobalt_memory df -k /tmp /var/lib/postgresql/data` | 0 | `overlay 466878464 2245864 464632600 1% /` · `mac 971350180 482189604 489160576 50% /var/lib/postgresql/data`. Gate: 3 × 144,743,447 B = 434,230,341 B ≈ 424,054 KB. Both free values are far above it → PASS. |

Q1 (whole):
```
[{"sch": "public", "tbl": "aset_sizings", "dropped": 1560, "max_attnum": 1586}, {"sch": "public", "tbl": "day_modes", "dropped": 194, "max_attnum": 206}, {"sch": "public", "tbl": "vault_writes", "dropped": 130, "max_attnum": 145}, {"sch": "public", "tbl": "cobalt_jobs", "dropped": 130, "max_attnum": 144}, {"sch": "public", "tbl": "vault_overrides", "dropped": 130, "max_attnum": 142}, {"sch": "public", "tbl": "card_stop_edits", "dropped": 130, "max_attnum": 139}, {"sch": "public", "tbl": "card_transitions", "dropped": 130, "max_attnum": 139}, {"sch": "public", "tbl": "bars", "dropped": 0, "max_attnum": 8}, {"sch": "public", "tbl": "cobalt_kill_switch", "dropped": 0, "max_attnum": 7}, {"sch": "user", "tbl": "trade_defs", "dropped": 0, "max_attnum": 7}, {"sch": "public", "tbl": "session_blocks", "dropped": 0, "max_attnum": 7}, {"sch": "public", "tbl": "cobalt_email_sends", "dropped": 0, "max_attnum": 6}, {"sch": "public", "tbl": "cobalt_redactions", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "tunables", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "trader_settings", "dropped": 0, "max_attnum": 5}, {"sch": "user", "tbl": "traders", "dropped": 0, "max_attnum": 3}]
```
Q2 (whole):
```
[{"tablename": "aset_sizings", "schemas": "public"}, {"tablename": "bars", "schemas": "public"}, {"tablename": "card_stop_edits", "schemas": "public"}, {"tablename": "card_transitions", "schemas": "public"}, {"tablename": "cobalt_email_sends", "schemas": "public"}, {"tablename": "cobalt_jobs", "schemas": "public"}, {"tablename": "cobalt_kill_switch", "schemas": "public"}, {"tablename": "cobalt_redactions", "schemas": "public"}, {"tablename": "day_modes", "schemas": "public"}, {"tablename": "session_blocks", "schemas": "public"}, {"tablename": "trade_defs", "schemas": "user"}, {"tablename": "trader_settings", "schemas": "user"}, {"tablename": "traders", "schemas": "user"}, {"tablename": "tunables", "schemas": "user"}, {"tablename": "vault_overrides", "schemas": "public"}, {"tablename": "vault_writes", "schemas": "public"}]
```
State vs the desk's read: **matches** (identical to run 1). Q1's top row is `public.aset_sizings`, dropped 1560 / max_attnum 1586. The new-core tables are in `public` only, and there is no `"user".aset_sizings`. Q3 `has_head` is false. → proceed to REPAIR.

## REPAIR
| rule | command | exit | result |
|---|---|---|---|
| D4 | `docker exec cobalt_memory sh -c 'pg_dump -U "$POSTGRES_USER" --create -f /tmp/cobalt_dev-0922.sql cobalt_dev'` (background) | 0 | no output |
| D5 | `docker exec cobalt_memory ls -la /tmp/cobalt_dev-0922.sql` | 0 | `-rw-r--r-- 1 root root 74952252 Sep 23 11:08 /tmp/cobalt_dev-0922.sql` (74,952,252 B; container clock is UTC) |
| D6 | `docker exec cobalt_memory tail -n 3 /tmp/cobalt_dev-0922.sql` | 0 | **`\unrestrict Y0OMDCwzmAM0u0eLdZ7VrptAuOvqnpUE5UzMQWGZncOvpODztqVLdEnz8JYvhk2`** (the only non-blank line). `-- PostgreSQL database dump complete` is **NOT** in the output → gate FAILED. |

**Stopped at D6** (07:08:14 EDT), as the prompt says: "else `FAILED: D6 — the dump is incomplete`, stop (nothing renamed yet)". R7, D7 and R8 were not called.

**Why D6 failed (reasoned, UNPROVEN, L70):** the likely cause is a stale gate, not a truncated dump. Newer `pg_dump` builds (the 2025 security releases, 16.10 / 17.6 and later) wrap a plain-format dump in `\restrict <key>` … `\unrestrict <key>`. The `\unrestrict` line is written AFTER the `-- PostgreSQL database dump complete` comment block, so `tail -n 3` reaches only the trailer. Three facts point this way: pg_dump exited 0 with no output; the file is 74.9 MB against a 144.7 MB database; and the last line is the trailer pg_dump writes at the very end. This is not verified: no listed command reads further back in the file, and the server version was not read. A variant was not typed (L62).

## MIGRATE
Not run.

## PROOF
Not run.

## WITH-DB
Not run (T1/T2 not called).

## CLEANUP
- **R10 not run.** The prompt allows the `rm` "ONLY after PROOF passed and T1 / T2 ran". So **`/tmp/cobalt_dev-0922.sql` (74,952,252 B) is LEFT inside `cobalt_memory`**. It holds a full copy of the dev DB. A relaunch's D4 overwrites it (`-f`).
- R8 was **not** run. R7 never ran, so rollback is forbidden.
- R2 at 07:08 EDT: no line added by this seat beyond this report (` M …/devdb-repair-2026-09-22.md`). The `06-s2-smoke-fix-check.md` line from the first R2 is gone. The desk committed it; this seat did not touch it.
- **`cobalt_dev` is unchanged**: it is still the bloated DB (1560 dropped on `aset_sizings`). `cobalt_dev_bloated_0922` does not exist.

## ROOT CAUSE
Not measured: step 5 was not reached. The mechanism and fix shapes (a)–(d) stand as drafted (see ESCALATE 4). From today's read only: `aset_sizings` max_attnum 1586 leaves **14** attnum slots before the 1,600 cap.

## ESCALATE
1. **D6 gate string vs the pg_dump trailer.** D6's `tail -n 3` cannot reach `-- PostgreSQL database dump complete` when pg_dump appends `\unrestrict <key>` (reasoned, UNPROVEN). The drafter needs to re-issue D6 before a relaunch. Two options, no pick, and either one is a NEW string that needs his approval: (i) `docker exec cobalt_memory grep -c -F -- "-- PostgreSQL database dump complete" /tmp/cobalt_dev-0922.sql` → MUST print `1`; or (ii) `docker exec cobalt_memory tail -n 8 /tmp/cobalt_dev-0922.sql`, with the gate unchanged. Also worth checking: D7's `psql -f` restore needs a `psql` that understands `\restrict` (a psql from the same container/version does). The drafter should confirm this with a version read, e.g. a new string `docker exec cobalt_memory psql --version`.
2. **Dump file left in the container**: `/tmp/cobalt_dev-0922.sql`, 74,952,252 B, full dev-DB content. R10 could not run lawfully. Options: the relaunch overwrites and then removes it at R10, or the desk approves R10 on its own now.
3. **The raw-command gap (the refusal they lack):** `assert_destructive_target()` has no rebuild/restore verb. The repair runs raw `docker exec` strings on the server that also holds `cobalt_brain` (D2 lists it). Carried from `r3-check-devdb-draft-2026-09-22.md` ESCALATE (a).
4. **ROOT CAUSE ops item (not built):** `TestMigrationRoundTrip` commits `--rollback --down-to 0001` + re-`migrate` on `cobalt_dev` on every with-DB run. The reverse scripts' `DROP COLUMN` leave dropped slots, and `aset_sizings` is at 1586/1600. Fix shapes: (a) scratch DB `cobalt_dev_rt` via a guarded helper · (b) rebuild the touched tables after the round trip · (c) reverse scripts recreate the table instead of `DROP COLUMN` · (d) a guarded `cobalt.devdb --rebuild` verb behind `assert_destructive_target()`. NAMED GAP: `assert_destructive_target()` has no rebuild/restore verb. Growth per run is unmeasured.
5. **`cobalt_dev_bloated_0922`:** not created. For the record, D0 `bytes` = 144,743,447 (the size the kept copy will have).
- ASK DESK: none raised. D6 has an explicit safe default (stop, nothing renamed).
- Step 5 reds: none (not run).

## CONTINUE
next: none — the run ended FAILED at D6 with the dev DB unchanged (only the dump file was created, ESCALATE 2). A relaunch needs a corrected, approved D6 string (ESCALATE 1) and then starts again from AUTHORIZATION.

FAILED: D6 — the dump is incomplete (the listed `tail -n 3` shows only pg_dump's `\unrestrict` trailer, no `-- PostgreSQL database dump complete` line; likely a stale gate, UNPROVEN; nothing renamed, no rollback needed; dump file left in the container) · ESCALATE: 5
