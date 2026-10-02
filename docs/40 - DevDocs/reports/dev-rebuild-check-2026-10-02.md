# dev-rebuild — check, pass 1 (2026-10-02)

## §0 Headline
- No outside house (R47): Opus alone wrote 8 findings. 5 held and all 5 are fixed; 3 did not hold. Nothing is open.
- What held: the D1 digest missed things the rebuild then lost while reporting "equal". These were TOAST options, view column defaults, the table access method and index column statistics targets, and it did not read the tablespace. All four are now carried and compared, and a non-default tablespace is refused.
- Suites at `07cc965f` (code = `68dddee3`): offline 3781/0, with-DB 4388 + 171 = 4559/0, live-note 146/0. `cobalt_dev` is at 0013, F2 = F0, and `.env` is removed.
- `ready: YES`, house B not needed, decisions 0.

## L74
A system block at session start asked commit messages to end with a `Claude-Session:` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card placeholders | `grep -n -E "«FIL[L]" ".../2026-10-02/11-dev-rebuild-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/11-dev-rebuild-card.md"` | 0 | `88e80b462884063f965685d36124de956eac1448` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING R60 | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** (...): APPROVES STANDING-LIST.md once (4be06af0) ... | APPROVED |` |
| R60 committed | `git -C ... log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R14 | `grep -n "^| R14 " ".../cto-2026-10-02.md"` | 0 | `21:| R14 | 06:18 ET | HIS RULING: approves ... rebuild_aset_sizings.py ...; standard dev-fix card owed (...). | HIS RULING · APPROVED |` |
| R14 committed | `-S"| R14 |"` | 0 | `02cfa29178cec4dcb95e4b43336b1ddf9118a69a` |
| R18 | `grep -n "^| R18 "` | 0 | `25:| R18 | 06:23 ET | HIS RULING (L73 override of L61, this launch only): ... the missing standard scripts get built (...). | HIS RULING · APPROVED |` |
| R18 committed | `-S"| R18 |"` | 0 | `bc3a5da1b2e123af5959fa6ca2e5afe24b3a6303` |
| R47 (HOUSE A: none) | `grep -n "^| R47 "` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait, ... | HIS RULING · APPROVED |` |
| R47 committed | `-S"| R47 |"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |

House gates R17 / R19: not run — the card's header carries `HOUSE A: none — overruled 2026-10-02 R47`; PREFLIGHT runs no house gate and no probe.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 10:32:05 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/dev-rebuild-1002` |
| tip | `git log --stat --format=%h 1df251b9..HEAD` | 0 | `f7e93d66` and `d7574799`, each only `.../reports/dev-rebuild-build-2026-10-02.md` (docs-only above TIP) |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: dev-rebuild · tip: 1df251b9 | on 6ae3f133 | migration: none | offline 3781/0 | with-DB 4555/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 4 of 4 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0` |
| range | `git log --oneline 6ae3f133..1df251b9` | 0 | `1df251b9 feat(dev-rebuild): cobalt db dev-rebuild frees a dev table's dropped column slots, kept only on an equal compare (D1, D2, D3; L1, L3, L4, L76)` · `fe638d17 wip(dev-rebuild): red — D1 D2 D3 tests before any src edit` |
| range stat | `git log --stat --format=%h 6ae3f133..1df251b9` | 0 | path union: `docs/40 - DevDocs/cobalt/db_migrations/cli.md`, `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md`, `src/cobalt/db_migrations/cli.py`, `src/cobalt/db_migrations/dev_rebuild.py`, `tests/cobalt/test_dev_rebuild_cli.py`, `tests/cobalt/test_dev_rebuild_db.py` |
| lock (own) | `ls /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env` | 1 | `No such file or directory` |
| lock (all) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| houses | — | — | house A: none (overruled 2026-10-02 R47) · house B: as needed |

## Files copied
none — no house (R47).

## OWN FINDINGS
Read set: the card; `BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`); the diff `6ae3f133..1df251b9` (`git diff` of `cli.py` and the DevDocs pages, and the full files `dev_rebuild.py`, `test_dev_rebuild_db.py` and `test_dev_rebuild_cli.py` at the tip); `db.py` `connect_migration` (:269); the build report's `## E3`–`## RECORDS` and its last line; `areas/cobalt.md` `## What Cobalt is` and `## Build rules` down.

The D1 rule is only as strong as the digest. Anything that is neither in `read_state` nor re-made by `_rebuild` is lost silently, because the compare cannot see it (X2). The digest covers the card's list. The tests below are for what it misses.

FINDING O1
ROW: D1 / X2
CLAIM: TOAST reloptions (`toast.*`) are stored on the TOAST relation, not in `c.reloptions`. `read_state` reads only `c.reloptions` (`src/cobalt/db_migrations/dev_rebuild.py:202`), and `_rebuild` re-makes only `cap['reloptions']` (`:624`). So `toast.autovacuum_enabled=false` is dropped and the compare stays equal.
RUN: TEST, `tests/cobalt/test_dev_rebuild_db.py`
```python
@requires_db
def test_check_o1_toast_reloptions_survive_the_rebuild(conn):
    _build_scratch(conn)
    conn.execute(f'ALTER TABLE "user".{SCRATCH} SET (toast.autovacuum_enabled = false)')
    q = ("SELECT t.reloptions FROM pg_class c JOIN pg_class t ON t.oid = c.reltoastrelid"
         " WHERE c.oid = %s::regclass")
    rel = f'"user".{SCRATCH}'
    assert conn.execute(q, (rel,)).fetchone()[0] == ["autovacuum_enabled=false"]
    assert any("autovacuum_enabled=false" in line for line in read_state(conn, "user", SCRATCH).sections["table"])
    rebuild_table(conn, "user", SCRATCH, dry_run=False)
    assert conn.execute(q, (rel,)).fetchone()[0] == ["autovacuum_enabled=false"]
```
EXPECT: the second `assert any(...)` fails on the tip (the digest does not see the option). Without that line, the last assert fails with `None == ['autovacuum_enabled=false']`.

FINDING O2
ROW: D1 / X2
CLAIM: A dependent view's column default (`ALTER VIEW … ALTER COLUMN … SET DEFAULT`, held in `pg_attrdef`) is neither captured by `_capture_view` (`dev_rebuild.py:421`) nor read by the `views` section (`:304`–`:311`). The recreated view loses it and the compare stays equal.
RUN: TEST, `tests/cobalt/test_dev_rebuild_db.py`
```python
@requires_db
def test_check_o2_a_view_column_default_survives_the_rebuild(conn):
    _build_scratch(conn)
    v = f'"user".{VIEW}'
    conn.execute(f"ALTER VIEW {v} ALTER COLUMN qty SET DEFAULT 5")
    q = ("SELECT pg_get_expr(d.adbin, d.adrelid) FROM pg_attrdef d"
         " JOIN pg_attribute a ON a.attrelid = d.adrelid AND a.attnum = d.adnum"
         " WHERE d.adrelid = %s::regclass AND a.attname = 'qty'")
    assert conn.execute(q, (v,)).fetchone()[0] == "5"
    rebuild_table(conn, "user", SCRATCH, dry_run=False)
    row = conn.execute(q, (v,)).fetchone()
    assert row is not None and row[0] == "5"
```
EXPECT: the last assert fails on the tip (`row` is `None`).

FINDING O3
ROW: D1 / X2
CLAIM: The table access method (`pg_class.relam`) is not in the `table` section (`dev_rebuild.py:200`–`:207`), and `CREATE TABLE` at `:624` has no `USING`. A table on a non-default access method comes back on `heap`, and the compare stays equal.
RUN: TEST, `tests/cobalt/test_dev_rebuild_db.py`
```python
@requires_db
def test_check_o3_the_table_access_method_survives_the_rebuild(conn):
    t = '"user".zz_dev_rebuild_am_t'
    conn.execute("CREATE ACCESS METHOD zz_dev_rebuild_am TYPE TABLE HANDLER heap_tableam_handler")
    conn.execute(f"CREATE TABLE {t} (id bigint PRIMARY KEY, note text) USING zz_dev_rebuild_am")
    conn.execute(f"INSERT INTO {t} VALUES (1, 'a')")
    conn.execute(f"ALTER TABLE {t} ADD COLUMN zz_extra text")
    conn.execute(f"ALTER TABLE {t} DROP COLUMN zz_extra")
    q = "SELECT am.amname FROM pg_class c JOIN pg_am am ON am.oid = c.relam WHERE c.oid = %s::regclass"
    assert conn.execute(q, (t,)).fetchone()[0] == "zz_dev_rebuild_am"
    rebuild_table(conn, "user", "zz_dev_rebuild_am_t", dry_run=False)
    assert conn.execute(q, (t,)).fetchone()[0] == "zz_dev_rebuild_am"
```
EXPECT: the last assert fails on the tip with `'heap' == 'zz_dev_rebuild_am'`.

FINDING O4
ROW: D1 / X2
CLAIM: An index column's statistics target (`ALTER INDEX … ALTER COLUMN 1 SET STATISTICS`) is not part of `pg_get_indexdef`. The `indexes` section (`dev_rebuild.py:251`) does not read it, and the index re-made at `:657` drops it.
RUN: TEST, `tests/cobalt/test_dev_rebuild_db.py`
```python
@requires_db
def test_check_o4_an_index_column_statistics_target_survives_the_rebuild(conn):
    _build_scratch(conn)
    idx = f'"user".{SCRATCH}_lower_idx'
    conn.execute(f'CREATE INDEX {SCRATCH}_lower_idx ON "user".{SCRATCH} (lower(label))')
    conn.execute(f"ALTER INDEX {idx} ALTER COLUMN 1 SET STATISTICS 321")
    q = "SELECT attstattarget FROM pg_attribute WHERE attrelid = %s::regclass AND attnum = 1"
    assert conn.execute(q, (idx,)).fetchone()[0] == 321
    rebuild_table(conn, "user", SCRATCH, dry_run=False)
    assert conn.execute(q, (idx,)).fetchone()[0] == 321
```
EXPECT: the last assert fails on the tip (the target is back at the default).

FINDING O5
ROW: D1 / X2
CLAIM: Neither the digest nor the rebuild reads `reltablespace`, so a table or index in a non-default tablespace moves to the default and the compare stays equal. `CREATE TABLESPACE` cannot run inside a transaction, so no rolled-back test can construct this.
RUN: COMMAND `grep -n -F "reltablespace" src/cobalt/db_migrations/dev_rebuild.py`
EXPECT: no output (exit 1).

FINDING O6
ROW: D1 (entry path: a table whose ACL is NULL)
CLAIM: `_restore_acl` returns early for a NULL ACL (`dev_rebuild.py:387`). A fresh table in a schema with `ALTER DEFAULT PRIVILEGES` for the creating role gets those grants, so the AFTER `grants` line reads explicit entries where BEFORE read `<default>`. Every such table is refused with `RebuildMismatch: grants`.
RUN: TEST, `tests/cobalt/test_dev_rebuild_db.py`
```python
@requires_db
def test_check_o6_a_default_acl_table_rebuilds_under_schema_default_privileges(conn):
    t = '"user".zz_dev_rebuild_acl_t'
    conn.execute(f"CREATE TABLE {t} (id bigint PRIMARY KEY, note text)")
    conn.execute(f"INSERT INTO {t} VALUES (1, 'a')")
    conn.execute(f"ALTER TABLE {t} ADD COLUMN zz_extra text")
    conn.execute(f"ALTER TABLE {t} DROP COLUMN zz_extra")
    assert conn.execute("SELECT relacl IS NULL FROM pg_class WHERE oid = %s::regclass", (t,)).fetchone()[0] is True
    conn.execute('ALTER DEFAULT PRIVILEGES IN SCHEMA "user" GRANT SELECT ON TABLES TO cobalt_system')
    result = rebuild_table(conn, "user", "zz_dev_rebuild_acl_t", dry_run=False)
    assert result.after.dropped == 0
```
EXPECT: on the tip, `RebuildMismatch: AFTER differs from BEFORE in: grants`.

FINDING O7
ROW: X1
CLAIM (to be disproved): some argument or fallback opens the dev-rebuild connection on a name other than `env.DEV_DB_NAME`, or with `allow_prod` true.
RUN: COMMAND `grep -n -F "_open(" src/cobalt/db_migrations/cli.py`
EXPECT if the claim holds: a `dev-rebuild` call whose arguments are not the literals `env.DEV_DB_NAME, allow_prod=False`.

FINDING O8
ROW: X3
CLAIM (to be disproved): a refused compare leaves the table changed.
RUN: TEST, the existing `tests/cobalt/test_dev_rebuild_db.py::test_d1_negative_control_a_skipped_grant_is_refused_and_nothing_is_kept` (asserts `read_state(...) == before` after the refusal), plus `grep -n -F "LOCK TABLE" src/cobalt/db_migrations/dev_rebuild.py`. The lock is taken before `with conn.transaction()`, so it is held until the caller's transaction ends.
EXPECT if the claim holds: the test is red.

## Findings
none — no house.

## Dropped
none.

## RUNS
Lock take 1 (step 4): `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` · `cp …/.env` · `ls -la` → `-rw-------  1 cobalt  staff  2186 Oct  2 10:36 /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env` (10:36:28) · `<FP>` → `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` · `--proof-only` → 36 tables, the eight above `0013` read `-`, `NOTHING WAS APPLIED`, so `cobalt_dev` is at `0013` · runs below · `<FP>` again → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` (equal) · `rm …/.env`; `ls …/.env` → `No such file or directory` (10:37:04). `.env: removed, proven gone (step 4)`.

`COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_db.py` → `5 failed, 4 passed in 0.67s` (the builder's four PASSED).

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | TEST `test_check_o1_toast_reloptions_survive_the_rebuild` | `E   assert False` / `where False = any(<generator …>)` at `test_dev_rebuild_db.py:183`: the digest does not see `toast.autovacuum_enabled` | HELD |
| O2 | own | TEST `test_check_o2_a_view_column_default_survives_the_rebuild` | `E   assert (None is not None)` at `:199`: the view's column default is gone after the rebuild | HELD |
| O3 | own | TEST `test_check_o3_the_table_access_method_survives_the_rebuild` | `E   AssertionError: assert 'heap' == 'zz_dev_rebuild_am'` at `:213` | HELD |
| O4 | own | TEST `test_check_o4_an_index_column_statistics_target_survives_the_rebuild` | `E   assert -1 == 321` at `:225` | HELD |
| O5 | own | COMMAND `grep -n -F "reltablespace" src/cobalt/db_migrations/dev_rebuild.py` | no output (exit 1) | HELD: the digest and the rebuild never read the tablespace |
| O6 | own | TEST `test_check_o6_a_default_acl_table_rebuilds_under_schema_default_privileges` | `E   assert False is True` at `:235`: the precondition `relacl IS NULL` fails, because a new `"user"` table already carries an explicit ACL. An added read on `cobalt_dev` (`ls -la …/.env` listed first): `system null_acl 0 rels 17` · `user null_acl 0 rels 18` | NOT HELD: red for another reason. No table in `system` / `"user"` has a NULL ACL, so the path is not reached, and if it were, the result would be a loud refusal, not a loss. The test was removed again |
| O7 | own (X1) | COMMAND `grep -n -F "_open(" src/cobalt/db_migrations/cli.py` | `530:def _open(dbname: str, *, allow_prod: bool):` · `578:    conn = _open(dbname, allow_prod=allow_prod)` (`_connect`, migrate only) · `885:    conn = _open(env.DEV_DB_NAME, allow_prod=False)` (dev-rebuild) | NOT HELD: the only dev-rebuild connection is the literal `env.DEV_DB_NAME` with `allow_prod=False`, behind the `COBALT_ENV == dev` refusal and `db._prod_gate` |
| O8 | own (X3) | TEST `test_d1_negative_control_a_skipped_grant_is_refused_and_nothing_is_kept` (in the same run) · COMMAND `grep -n -F "LOCK TABLE" src/cobalt/db_migrations/dev_rebuild.py` | `PASSED …test_d1_negative_control…` (`read_state` after the refusal equals BEFORE) · `749:    conn.execute(sql.SQL("LOCK TABLE {} IN ACCESS EXCLUSIVE MODE")…` (before `with conn.transaction():` at :750) | NOT HELD: one transaction holds the lock, and a refusal leaves BEFORE |

HELD tests committed before any fix: `c9960106 wip(dev-rebuild): check red — O1 O2 O3 O4`.

## FIXES
| fix | ids | commits |
|---|---|---|
| The digest and the rebuild now carry the access method, the TOAST options, index column statistics targets and view column defaults. A table or index outside the default tablespace is refused. | O1 O2 O3 O4 O5 | code `68dddee3` (`wip(dev-rebuild): check — fix …`, made at the lock stop) · DevDocs line and the `fix(dev-rebuild):` subject `07cc965f` |

The fix for O1–O5 is in `src/cobalt/db_migrations/dev_rebuild.py`, committed as wip `68dddee3` before its with-DB green:
- the `table` section reads the access method and the TOAST reloptions, and `_rebuild` re-makes both (`USING <am>`, then `ALTER TABLE … SET (toast.…)`).
- the `indexes` section reads each index column's statistics target, and `_rebuild` re-sets it.
- the `views` section reads each view column's default, and `_rebuild` re-sets it.
- `_TABLE_SHAPE` reads `reltablespace` and the number of indexes outside the default tablespace, and `_capture` refuses any non-zero value (L1).

Offline neighbours after the edit: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_dev_rebuild_cli.py tests/cobalt/test_dev_rebuild_db.py tests/cobalt/test_tenancy.py tests/cobalt/test_migrate_proof.py` → `63 passed, 52 skipped in 2.07s` (every skip is `Postgres env settings not available`).

With-DB green, lock take 2 (extra, step 5, 10:55–10:56:02): `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` · `cp` · `ls -la` → only `…/dev-rebuild-1002/.env` (10:55) · `<FP>` → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` · `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_db.py` → `8 passed in 0.57s`: the four builder tests (D3 on `aset_sizings` included) and `test_check_o1`…`test_check_o4` PASSED · `<FP>` → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` · `rm`; `ls …/.env` → `No such file or directory`. `.env: removed, proven gone (step 5)`.
O5 after the fix: `grep -n -F "reltablespace" src/cobalt/db_migrations/dev_rebuild.py` → `192:           c.reltablespace,` · `194:             WHERE x.indrelid = c.oid AND i.reltablespace <> 0)`.

## Suites
The suites ran at HEAD `07cc965f` (clean). Its code tree is that of `68dddee3`, the newest code commit; `07cc965f` adds only the DevDocs line.
- RESTARTS: `uv run cobalt jobs restarts 6ae3f133..HEAD` → `cli.md` / `dev_rebuild.md` / build report `DOCS -` · `cli.py` and `dev_rebuild.py` `static import reach com.cobalt.radar` · both test files `test/documentation; no resident -` · `RESTARTS: com.cobalt.radar`. No UNCLASSIFIED row.
- (a) OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, exit 0) → `3781 passed, 681 skipped, 1 xfailed, 25 warnings in 613.52s (0:10:13)`; `grep -c -F "FAILED"` → `0`. That is the build's 677 skips plus the four new with-DB tests `test_check_o1`–`o4`, which skip without Postgres settings.
- (b) THE LOCK at 11:06:49: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` · `cp` · `ls -la` → only `-rw-------  1 cobalt  staff  2186 Oct  2 11:06 /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env` · `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` · `--proof-only` → 36 tables, the eight above `0013` read `-`, `NOTHING WAS APPLIED`, `code: 07cc965f (clean)`, so `cobalt_dev` is at `0013`.
- (c) PASS 1: the hub's PASS-1 COMMAND byte for byte, nothing added (`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip …` through `--deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk`) → `4388 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 736.26s (0:12:16)`, exit 0. That is the build's 4384 plus the four check tests. The SKIPPED lines are `test_cards_picks.py:388` (S2-P2's card_score column is present on cobalt_dev), `test_cards_picks.py:401` (real S2-P2 0007 applied …), `test_radar_evaluate.py:695`, `test_s3_c4_experiments.py:95`, `test_catalyst.py:365` and `test_predicate.py:262` (each COBALT_LIVE_VAULT_ROOT not set), and `test_replay_line.py:266` (COBALT_TEST_LIVE_DRC). These are the build's seven; none names `test_dev_rebuild`. `<d1>` = 4388. Row T: `grep -n -F "test_dev_rebuild"` on `BUILD-HUB.md` and `DEPLOY-HUB.md` (in this worktree) → no hit; no deselect was owed.
- (c2) FORWARD `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `0001` … `0022` applied; every pre-existing table `OK`; the eight tables above `0013` `CREATED`; `content UNCHANGED on every table.` **dev forward: APPLIED 11:19** (`date` → `Fri Oct  2 11:19:54 EDT 2026`). `<F1>` = `893 · 44 · 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2: the hub's PASS-2 COMMAND byte for byte, nothing added → `171 passed, 1 deselected, 5 warnings in 222.35s (0:03:42)`, exit 0; `grep -c -F "SKIPPED"` → `0`. The 11 `FAILED` text hits are captured log and page text under `-rA` (`radar panel FAILED: …`, `<div class="failed">FAILED`), not test results. `<d2>` = 171; `<d>` = 4388 + 171 = **4559**.
- (c3r) NOTHING LEFT BEHIND (`ls -la …/.env` listed first): `COBALT_ENV=dev uv run cobalt db query --side user "SELECT 'rel' …"` over relations prefixed `zz_dev_rebuild` / `zz_rebuild_old`, access methods and functions prefixed `zz_dev_rebuild` → header only, **no rows**.
- (f) ROLLBACK `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0022` … `0014` rollback, newest first; the eight tables `DROPPED`, every other table `OK`; `content UNCHANGED on every table.` `<F2>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field. **cobalt_dev: 0013 — F2 = F0.** `rm …/.env`; `ls …/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` (11:24:28). `.env: removed, proven gone (W)`.
- (e) LIVE-NOTE `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.75s`. The one skip is `test_replay_line.py:266` (COBALT_TEST_LIVE_DRC); none names `COBALT_LIVE_VAULT_ROOT`. `<l>` = 146.

## Scope
PREFLIGHT path union (`6ae3f133..1df251b9`): `src/cobalt/db_migrations/cli.py`, `src/cobalt/db_migrations/dev_rebuild.py`, `tests/cobalt/test_dev_rebuild_cli.py`, `tests/cobalt/test_dev_rebuild_db.py`, `docs/40 - DevDocs/cobalt/db_migrations/cli.md`, `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md`. Every one is in the `files` of D1, D2 or D3. My commits touch `tests/cobalt/test_dev_rebuild_db.py` (D1 / D3), `src/cobalt/db_migrations/dev_rebuild.py` (D1) and `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md` (D1), all inside the rows. Nothing touches a score, rank, grade or size: the module rebuilds catalog shape on `cobalt_dev` only and copies rows unchanged (the row digest is the proof).

## Checked against the branch
- (i) `git log --oneline 1df251b9..HEAD -- . ":(exclude)docs"` → `68dddee3 wip(dev-rebuild): check — fix for O1 O2 O3 O4 O5 before its with-DB green; cobalt_dev lock held by desk-tools-a-1002` · `c9960106 wip(dev-rebuild): check red — O1 O2 O3 O4`. `<tip now>` = `68dddee3`.
- (ii) `git log --stat --format=%h 1df251b9..HEAD` → `07cc965f` `docs/…/dev_rebuild.md` · `68dddee3` `src/cobalt/db_migrations/dev_rebuild.py` · `c9960106` `tests/cobalt/test_dev_rebuild_db.py` · `f7e93d66` / `d7574799` the build report. Every non-docs path is a row's file or a test file. No WIDENED.
- (iii) fence: `git log --oneline 6ae3f133..HEAD -- src/cobalt/aset/migrations` → empty. The full stat of `6ae3f133..HEAD` (PREFLIGHT plus (ii)) names no registry migration, no `STANDING-LIST.md`, no `desk-launch.sh` and no launch line.
- (iv) `grep -n -F "def test_check_o" tests/cobalt/test_dev_rebuild_db.py` → `176:…o1…`, `189:…o2…`, `203:…o3…`, `217:…o4…`, one line each. `c9960106` (red) sits below `68dddee3` (the code fix) and `07cc965f` (`fix(dev-rebuild):`) in (i) / `git log --oneline 1df251b9..HEAD`. O5 is a COMMAND finding; its after-fix grep is under `## FIXES`.
- (v) `ls …/dev-rebuild-1002/.env` → `No such file or directory` · `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` · `git status --short --branch` → `## ops/dev-rebuild-1002`.
- (vi) TREE STATE row T: `git log --stat --format=%h 6ae3f133..HEAD -- src/cobalt/db_migrations tests/cobalt` → `68dddee3` (`dev_rebuild.py`), `c9960106` (`test_dev_rebuild_db.py`), `1df251b9`, `fe638d17`. There is no new migration and no new with-DB test FILE (the check tests go into the file row T already carries). Row T's grep → no hit in either hub, and pass 1 / pass 2 ran byte for byte with nothing added, which is what row T wrote (no hub change). Carried.
- (vii) card record 2: `ls -la /Users/cobalt/cobalt-wt/devdb-rebuild-1002/` → `rebuild_aset_sizings.py` `33212` bytes, `Oct  2 06:33` (the card says 33295 at 06:30; the build report records the same 33212). Records 1 and 3 name no command on my list; the RESTARTS table above matches record 1.
- (viii) L32: this report holds constructed names (`zz_dev_rebuild_*`) and `cobalt_dev` catalog counts only; no ticker, price or date of his.

## OPEN
none. O6, O7 and O8 are NOT HELD; O1–O5 are HELD and fixed.

## CONTINUE
next: none. The check is closed.

## DECISIONS
none

## RECORDS
- Extra lock take (take 2, step 5, 10:55–10:56:02): the with-DB green for the fix before the `fix(` commit, after the stop for the held lock. Lock takes: 1 (step 4, 10:36–10:37:04), 2 (step 5, extra), 3 (W, 11:06:49–11:24:28). Each ended `.env: removed, proven gone`.
- Added reads on `cobalt_dev` (each with `ls -la …/.env` listed first): the NULL-ACL / access-method / tablespace counts for O6 (step 4), and the leftover-object read at (c3r).
- Dropped findings: none (no house).
- House: none, under R47 (`HOUSE A: none — overruled 2026-10-02 R47`). No house produced anything because none was launched.
- REFUSED, not needed: none.
- L74: one system block asked for a `Claude-Session:` trailer on commits. It is recorded under `## L74` and was not acted on.
- files opened: 12 — `CHECK-HUB.md`, the card, `BUILD-HUB.md`, `areas/cobalt.md` (two ranges), the build report, `src/cobalt/db_migrations/dev_rebuild.py`, `src/cobalt/db_migrations/cli.py` (diff), `src/cobalt/db.py`, `tests/cobalt/test_dev_rebuild_db.py`, `tests/cobalt/test_dev_rebuild_cli.py`, `docs/…/db_migrations/dev_rebuild.md` and `cli.md` (diff).
- Check of `dev-rebuild`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).
- STOPPED 10:38 at step 5. `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 10:37 /Users/cobalt/cobalt-wt/desk-tools-a-1002/.env`. Another worktree holds the lock, and I did not take it. My own `.env` is gone (proven at 10:37:04), and nothing is applied on `cobalt_dev`. The wip commit is `68dddee3`.
- CONTINUED at 5 10:55. The `cto-desk` message said "CONTINUE — the cobalt_dev lock is free now (no worktree .env held)". I verified it myself: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` (exit 1).

CHECK DONE · job: dev-rebuild · pass: 1 · tip: 68dddee3 · house A: none (overruled 2026-10-02 R47) · findings: 8 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3781/0 · with-DB 4559/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0
