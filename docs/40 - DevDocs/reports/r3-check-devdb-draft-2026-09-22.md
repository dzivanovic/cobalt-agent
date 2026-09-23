# R3 check + dev-DB repair: prompts drafted, 2026-09-22

## §0 Headline
- Two prompts written, both unlaunched: `prompts/2026-09-22/67-setups-check-r3.md` (`16` re-pointed to round 3; launch line byte-identical to `16` except the path and `setups-check-r3-0922`) and `prompts/2026-09-22/68-devdb-repair.md` (Opus 5.5, `acceptEdits`, dev only).
- 68: no guarded path can recreate a table or a database, so the repair is a raw dump → rename aside → restore of `cobalt_dev` inside `cobalt_memory`, then `db migrate`. It adds 15 new strings (12 allow, 3 deny). ESCALATE (a).
- ESCALATE: 7. The biggest is (b): round 2's fix range `60ddac4..826d284` has never been checked, because `16` never ran.
- Seat `r3-check-devdb-draft-0922`, 19:50–20:0x ET (`date`). Everything was read-only, and this seat wrote only these three files.

## DIGEST FOR THE DESK
- **Launch order:** `68` first, because nothing else in the dev-DB lane is running. `67` needs nothing from `68` (it is offline), so it can go into the house lane NOW, ahead of `59` and `63` (R110). `31` launches after `68`'s stop line, then `27`.
- **Stagger:** `59` and `63` do not name `67` in their own STAGGER gates. When `67` is running, the desk holds them. When `59` / `63` launch after `67`'s stop, nothing more is needed.
- **`67` (round 3 of 3, THE LAST):**
  - Range `65c08a0..<tip>`. The tip comes from r3's stop line (`be44eb4`); the report commit is `8da261a`.
  - The boundary is `33`'s rows' files plus r3 ESC (ix)/(x): `evaluate.py`, `anatomy/extension.py`, `anatomy/frame.py`, `formation/atoms.py`, `test_setups_d4.py`, `test_assumed_store.py`, `test_setups_registries.py`, `test_setups_d1.py`.
  - Questions: F1–F6, each read against his R47–R51 and R61. Then the proposal KEYS and grades, then Q1 (r2 ESC (viii) stop resolvers) and Q2 (r3 ESC (v) engine dial not per-setup).
  - The proposal file is read by the hub, and only keys and grades are staged (L32). The hub greps the values as counts only.
  - A defect that HOLDS goes to `## FOR DEJAN` with the override question; there is no round 4. The date gate is R30 (through 09-23 23:59 ET).
  - Placeholder the desk fills: launch row `R__`. That row must contain `59 is not running` / `63 is not running` and name `67-setups-check-r3.md` if either report is absent.
- **`68`:**
  - AUTHORIZATION checks his approval with `-S"cobalt_dev_bloated_0922"` on the desk files, plus launch row `R__`.
  - The steps: PREFLIGHT reads, then D1 (auth probe, and no other session may be open on `cobalt_dev`), then a disk check, a dump with `--create`, and a check that the dump is complete. Then RENAME `cobalt_dev` → `cobalt_dev_bloated_0922` (kept), RESTORE, `db migrate`, and the PROOF. T1 is the tenancy suite and T2 the three r3 reds. Last, cleanup of the dump file.
  - Rollback (R8) is only allowed after the rename has been proven.
  - The ROOT CAUSE is measured as the dropped-column growth per test run.
  - Placeholder the desk fills: `R__`.
- **Before `68` launches:** one read by another house (ESCALATE (c)), then his ONE approval of the list below.

## RULE PROOF
Each check was one `grep -c -F -e "<span>"` call.

| check | file | count |
|---|---|---|
| `16`'s span `--model claude-sonnet-5 … --remote-control setups-check-r2-0922 --allowedTools …15… --disallowedTools …3… --add-dir …3…` | `16-setups-check-r2.md` | 1 |
| the SAME span with only `setups-check-r2-0922` → `setups-check-r3-0922` | `67-setups-check-r3.md` | 1 |
| `` `cd /Users/cobalt/cobalt-wt/agy-trial` then `claude --bg "Read '…/67-setups-check-r3.md' and follow it exactly." --model claude-sonnet-5`` | `67` | 1 |

The only differences between the two launch lines are the prompt path and the remote-control name, as expected. `67` adds no new string (0).

## NEW strings:
These are `68`'s launch strings, verbatim as they appear in the launch line. The `\"` and `\$` escapes are the zsh spelling; the hub types plain `"` and `$`. They go to Dejan as ONE approval list. Each "= file" mark was checked with one `grep -c -F` = 1. For the NEW ones, `grep -rl -F` across `prompts/` found only `68`.
```
"Bash(date*)"                                         = 33-setups-fix-r3.md
"Bash(ls *)"                                          = 33-setups-fix-r3.md
"Bash(grep *)"                                        = 33-setups-fix-r3.md
"Bash(tail *)"                                        = 33-setups-fix-r3.md
"Bash(git -C /Users/cobalt/cobalt log*)"              = 33-setups-fix-r3.md
"Bash(git -C /Users/cobalt/cobalt show*)"             = 16-setups-check-r2.md
"Bash(git -C /Users/cobalt/cobalt status --porcelain)"  NEW
"Bash(COBALT_ENV=dev uv run cobalt db query --side system --format json *)"  NEW
"Bash(docker exec cobalt_memory sh -c 'psql -U \"\$POSTGRES_USER\" -d cobalt_dev -v ON_ERROR_STOP=1 -Atc \"SELECT count(*) - 1 FROM pg_stat_activity WHERE datname = current_database()\"')"  NEW
"Bash(docker exec cobalt_memory sh -c 'psql -U \"\$POSTGRES_USER\" -d postgres -v ON_ERROR_STOP=1 -Atc \"SELECT datname FROM pg_database ORDER BY 1\"')"  NEW
"Bash(docker exec cobalt_memory df -k /tmp /var/lib/postgresql/data)"  NEW
"Bash(docker exec cobalt_memory sh -c 'pg_dump -U \"\$POSTGRES_USER\" --create -f /tmp/cobalt_dev-0922.sql cobalt_dev')"  NEW
"Bash(docker exec cobalt_memory ls -la /tmp/cobalt_dev-0922.sql)"  NEW
"Bash(docker exec cobalt_memory tail -n 3 /tmp/cobalt_dev-0922.sql)"  NEW
"Bash(docker exec cobalt_memory sh -c 'psql -U \"\$POSTGRES_USER\" -d postgres -v ON_ERROR_STOP=1 -c \"ALTER DATABASE cobalt_dev RENAME TO cobalt_dev_bloated_0922\"')"  NEW
"Bash(docker exec cobalt_memory sh -c 'psql -U \"\$POSTGRES_USER\" -d postgres -v ON_ERROR_STOP=1 -q -f /tmp/cobalt_dev-0922.sql')"  NEW
"Bash(docker exec cobalt_memory sh -c 'psql -U \"\$POSTGRES_USER\" -d postgres -v ON_ERROR_STOP=1 -c \"DROP DATABASE IF EXISTS cobalt_dev\" -c \"ALTER DATABASE cobalt_dev_bloated_0922 RENAME TO cobalt_dev\"')"  NEW (rollback only)
"Bash(docker exec cobalt_memory rm /tmp/cobalt_dev-0922.sql)"  NEW
"Bash(COBALT_ENV=dev uv run cobalt db migrate)"       = 27-handicap-h1-build.md
"Bash(COBALT_ENV=dev uv run pytest *)"                = 33-setups-fix-r3.md
--disallowedTools:
"AskUserQuestion"                                     = 33-setups-fix-r3.md
"EnterWorktree"                                       = 33-setups-fix-r3.md
"Bash(git push*)"                                     = 33-setups-fix-r3.md
"Bash(*cobalt_brain*)"                                NEW (deny)
"Bash(*--allow-prod*)"                                NEW (deny)
"Bash(*--prod*)"                                      NEW (deny)
```
The mode is `--permission-mode acceptEdits`, the cwd is `/Users/cobalt/cobalt`, and `--add-dir` is the standard triplet.

## READING:
1. **Why dump and restore, not a per-table rebuild.** At the 0001 state, `aset_sizings` carries sequences, FKs, triggers and grants. A `CREATE TABLE … LIKE` swap would need all of them rebuilt by hand, and dropping the old table drops its owned sequence. A logical dump with `--create` recreates every table with live columns only, and it brings back the database-level owner, grants and settings. The bloated copy is renamed aside rather than dropped, so rollback is one rename.
2. **The migration head.** `cobalt_dev` has no migration-version table (`FORWARD` re-applies every file and `cli.py` records no state). Head = the last `-- applying` line of `db migrate` plus the existence of `system.archive_incidents` (from `0011`). Main's highest is `0011_archive_incidents.sql` (`ls src/cobalt/db_migrations`).
3. **`0013`.** The setups branch adds `0013_tunables_slug_nullable` (`61a283f`). `68` migrates to MAIN's head `0011`, as the desk asked. The setups CLOSE re-run migrates `0013` forward itself.
4. **The PostgreSQL mechanism is UNPROVEN (L70).** I could not quote the manual from this seat, so I did not assert that VACUUM FULL doesn't reclaim the slots. The repair works either way, because restored tables are new. PROOF measures `dropped` / `max_attnum`, and no FORWARD file contains `DROP COLUMN` (`grep -l` over `0001`–`0011` found none), so PROOF requires `dropped = 0`.
5. **Local-socket trust inside `cobalt_memory` is UNPROVEN.** I believe the official postgres image trusts local connections, but that is not verified. D1 is the probe: an auth error there is `FAILED` before anything changes. `"$POSTGRES_USER"` is expanded by the container's `sh`, so no credential appears on a host command line (L4).
6. **The dev read uses a wildcard.** The `db query` rule is `--side system --format json *` rather than three verbatim SQL strings, because nested double quotes cannot survive the double-quoted launch line. The command is SELECT-only in a READ ONLY transaction, and it refuses `cobalt_brain` without `--prod` (`db_query.py:98-178`). It is also narrower than the approved `COBALT_ENV=production … db query --side system --prod *`. The three exact queries are written in `68`'s body.
7. **`~/cobalt` as cwd.** It is L54's production checkout, and the desk named it. The hub writes only its report there. `pytest -p no:cacheprovider` avoids the cache dir, but gitignored `__pycache__` may still be written. R2 (`git status --porcelain`) before and after proves that nothing tracked changed.
8. **`67`'s scope.** I kept `16`'s 38 and 17 stagger rows, since both have stop lines as of 19:55 and pass. HOLD 1 is staged as context and is NOT re-asked: r3 moved no pin, and check (iii) proves it. `16`'s stop line had `houses that checked` and `ready`; I used the desk's shape instead and moved the houses count into the §4 text. The ORDER list's `:64–:67` (the file-check ranges) was re-pointed too, although the desk's parenthesis left it out. `## ORDER` names it.
9. **Deny strings with a leading `*`.** Whether they match mid-command is UNPROVEN. They back up the fixed strings and are not the guard.

## ESCALATE
(a) **The raw-command gap.**
- The four destructive `docker exec` strings (dump, rename, restore, rollback) lack `assert_destructive_target()`'s refusal. They run inside the container that also holds `cobalt_brain`.
- What stands in for the guard: fixed strings naming `cobalt_dev` / `cobalt_dev_bloated_0922` literally, the deny strings, and his approval.
- The desk brings this to him with the list. The ops item: a guarded `cobalt.devdb --rebuild` verb, so the next repair is not raw.

(b) **Round 2 has never been checked.**
- `16` never ran: there is no `reports/setups-check-r2-2026-09-22.md` and no `scratch/…/setups-check/` folder. As the desk scoped it, `67` checks `65c08a0..be44eb4` only.
- Round 2's fix `60ddac4..826d284` and `12`'s fixture cut `74eefd8..65c08a0` have had no house check. L67 says every build is checked by three.
- `ASK DESK: widen 67's packet to 60ddac4..<tip> with r2's F1–F5 + P1 questions, or cover r2 / 12 separately? [20:03]`. Safe default as drafted: the desk's range, with a standing line in `67`'s ESCALATE.

(c) **L67 floor on `68`.** A desk prompt with a DB-recovery step goes to at least one other house before it runs (09-18 R8, `topics/cto-desk.md` 2026-09-18). `ASK DESK: one Grok or Gemini read of 68 before his approval? [20:03]`

(d) **`cobalt_dev_bloated_0922` is kept on success.** It takes as much disk as `cobalt_dev` (Q3 `bytes`). Dropping it needs his word and a new string.

(e) **The root cause will recur.**
- `tests/cobalt/test_tenancy.py:685-705` `TestMigrationRoundTrip` commits `--rollback --down-to 0001` and a re-`migrate` on `cobalt_dev`, in a subprocess, on every with-DB run of every worktree. Each reverse `DROP COLUMN` leaves one slot per run.
- `68` measures the growth per run and how many runs are left.
- Fix shapes for an ops item, with no pick: a scratch database; a rebuild after the round trip; reverse scripts that recreate instead of dropping; a guarded rebuild verb.

(f) **`68`'s own with-DB proof grows the counts again.** T1 and T2 each re-run the round trip. The stop line's `max dropped` is PROOF's figure, taken before T1. The growth is reported separately.

(g) **`67`'s stagger vs `59` / `63`.** Their own gates do not name `67`. With `67` running, the desk must hold them (R110 already orders that).

## CONTINUE
next: none — `67`, `68` and this report are written. The desk commits all three, fills `R__` in both prompts, and brings the ONE approval list for `68`.

R3 CHECK + DEVDB REPAIR DRAFTED · prompts: 2 · 67 new strings: 0 · 68 new strings: 15 · ESCALATE: 7
