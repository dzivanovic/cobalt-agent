# devdb-rebuild 2026-10-02 — rebuild `"user".aset_sizings` on `cobalt_dev`

## §0 Headline
- `cobalt_dev` `"user".aset_sizings` rebuilt in one committed transaction: `max_attnum 1581 → 54`, dropped `1527 → 0`, live `54 = 54`, rows `1 = 1`. The catalog digest is identical BEFORE and AFTER (`8e8bee07f5fb11891ef757b16e891299`).
- FP F1 = F0 = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`; `cobalt_dev` is still at `0013`.
- Proof: `test_card_checks_index_and_receipt_immutability_on_cobalt_dev` PASSED (43 of 43 passed in the file).
- Lock released at 06:34 EDT; `.env` is gone.

## STEPS

### FP (typed exactly, from BUILD-HUB.md THE LOCK)
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

### 1. READ (no lock), 06:26 EDT
- `src/cobalt/aset/migrations/0001_aset_sizings.sql`: identity `id` PK plus 15 columns. aset 0002–0009 add and drop columns and set NOT NULLs.
- Registry migrations up to 0013 that touch the table:
  - 0002 moves it to `"user"` and adds `user_id` with the GUC default.
  - 0004 adds `account_mode` with a CHECK, and `pool_member_id` as an FK to `system.radar_membership`.
  - 0006 and 0007 add the radar card columns, the CHECKs `aset_sizings_manual_sized` and `aset_sizings_radar_provenance`, two partial unique indexes, inbound FKs from `card_dot_*`, and the view `"user".radar_cards_v`.
  - 0009 adds inbound FKs from `picks` and `missed`.
- Connection: `cobalt.db` is the one factory. The script loads `<repo>/.env` the way `cobalt/cli.py` does, then opens `db.connect_migration(env.DEV_DB_NAME)`. It reads, prints and passes no secret.
- Script: `/Users/cobalt/cobalt-wt/devdb-rebuild-1002/rebuild_aset_sizings.py`.
  - Exits 2 without opening anything unless `COBALT_ENV=dev`, `env.resolve_db_name()` is `cobalt_dev` and `assert_destructive_target` passes.
  - Exits 2 right after connecting unless `current_database()` is `cobalt_dev`.
  - In one transaction it runs `lock_timeout 15s`, `LOCK … ACCESS EXCLUSIVE`, then takes the BEFORE digest.
  - It captures columns, constraints, indexes, triggers, policies, ACLs (table, column, sequence), comments, inbound FKs, the identity sequence (options, last_value, is_called) and the dependent views (recursive).
  - It drops the views and inbound FKs, parks the old table's index and sequence names, renames the old table, creates the new table with live columns in attnum order, sets the owner, copies rows `OVERRIDING SYSTEM VALUE`, runs `setval`, drops the old table, then re-adds constraints, indexes, grants, comments, inbound FKs and views (owner and grants), and runs `ANALYZE`.
  - It takes the AFTER digest and compares. It refuses (rolls back, exits 1) on shapes it does not handle: inheritance, publications, ext stats, rules, matviews, serial sequences.
- Proof test located: `tests/cobalt/test_radar_score_migration.py:412`.

### 2. Lock + FP + level
- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`.
- (b) `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/deploy-1001-1/.env` → no output. `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 06:31 /Users/cobalt/cobalt-wt/deploy-1001-1/.env` (exactly one line).
- `<FP>` → **F0** = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `36 table(s) probed on cobalt_dev`.
  - The tables of migrations above 0013 (`drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns`) read `-`, so the level is **0013**. This is read the same way as `deploy-2026-10-01-1.md`.
  - `aset_sizings user user 1 0824685c130da3c7cb7f0e76191a6819` · `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` · `code: 8cf44088 (clean) · /Users/cobalt/cobalt-wt/deploy-1001-1`.

### 3. Dry run (3 tries, the limit)
- Try 1 → exit 1, `psycopg.errors.AmbiguousFunction: operator is not unique: text || "char"`. The error was in the BEFORE digest's view-trigger subquery, before any DDL, and the transaction rolled back. Fix: `t.tgenabled::text`.
- Try 2 → exit 1, `psycopg.errors.SyntaxError: conflicting or redundant options` at `SEQUENCE NAME "user".aset_sizings_id_seq AS bigint`. The error was at `CREATE TABLE`, inside the transaction, and the transaction rolled back. Fix: drop `AS <type>` from the identity options, because the column type sets it. A guard was also tightened: compression is applied only for `p` or `l`.
- Try 3 → exit 0:
  - `BEFORE max_attnum=1581 dropped=1527 live=54 rows=1 digest=8e8bee07f5fb11891ef757b16e891299`
  - `CAPTURED columns=54 constraints=7 indexes=3 triggers=0 policies=0 fks_in=6 sequences=1 views=1 col_acls=0 pg=16`
  - `AFTER  max_attnum=54 dropped=0 live=54 rows=1 digest=8e8bee07f5fb11891ef757b16e891299`
  - Every section md5 equal: rows_md5 `ced48fb5…`, table `13de2c69…`, columns `98ab574b…`, constraints `2f2633a2…`, indexes `0ebf3f31…`, triggers/policies `d41d8cd9…` (none), fks_in `c42fc39c…`, fks_out `7a16c17e…`, sequences `1df21302…`, views `6a28e5c6…`.
  - `ROLLED BACK (dry run): every check equal`

### 4. Rebuild
- `COBALT_ENV=dev uv run python /Users/cobalt/cobalt-wt/devdb-rebuild-1002/rebuild_aset_sizings.py` → exit 0:
  - `BEFORE max_attnum=1581 dropped=1527 live=54 rows=1 digest=8e8bee07f5fb11891ef757b16e891299`
  - `AFTER  max_attnum=54 dropped=0 live=54 rows=1 digest=8e8bee07f5fb11891ef757b16e891299`, with every section md5 identical to try 3 above.
  - `COMMITTED: every check equal`
  - `POST-COMMIT max_attnum=54 dropped=0 live=54 rows=1`
- BEFORE digest content, from the run:
  - Owner `cobalt_user`, with owner-only ACLs on the table, the view and the sequence.
  - 54 columns, starting `1|id|bigint||True||a` and ending `54|promoted_at|timestamp with time zone`.
  - Constraints: `aset_sizings_account_mode_check`, `_manual_sized`, `_pkey`, `_pool_member_id_fkey`, `_radar_provenance`, `_radar_score_id_fkey`, `_user_id_fkey`.
  - Indexes: `aset_sizings_one_open_radar_card`, `aset_sizings_one_promoted_radar_card`, `aset_sizings_pkey`.
  - Inbound FKs: `card_dots`, `card_dot_taps`, `card_stop_edits`, `card_transitions` (ON DELETE CASCADE), `missed`, `picks`.
  - Sequence: `"user".aset_sizings_id_seq|i|id|…|18444|True`.
  - View: `"user".radar_cards_v`.
- `<FP>` → **F1** = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`, which equals F0 field for field.

### 5. Proof
- `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_radar_score_migration.py` → `43 passed in 1.10s`, including `PASSED tests/cobalt/test_radar_score_migration.py::test_card_checks_index_and_receipt_immutability_on_cobalt_dev` and `test_migrate_twice_is_idempotent_on_cobalt_dev`.
- `<FP>` → `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = F0.
- `migrate --proof-only` → the same 36-table output. The tables above 0013 still read `-`, so the level is **0013**. `aset_sizings` digest is unchanged at `0824685c130da3c7cb7f0e76191a6819`. `NOTHING WAS APPLIED` · `code: 8cf44088 (clean)`.
- (d) `rm /Users/cobalt/cobalt-wt/deploy-1001-1/.env` → no output. `ls /Users/cobalt/cobalt-wt/deploy-1001-1/.env` → `ls: /Users/cobalt/cobalt-wt/deploy-1001-1/.env: No such file or directory`. `date` → `Fri Oct  2 06:34:30 EDT 2026`.

## DECISIONS

## RECORDS
- `.env: removed, proven gone (step 5)` at 06:34:30 EDT. The lock was taken once (06:31) and covered steps 2–5.
- The script authenticates as `Credential.BOOTSTRAP` through `db.connect_migration`, the factory's migration path. The rebuild needs `CREATE TABLE`, `ALTER … OWNER`, ACL re-grants and FK changes on other `"user"` tables, which are migration acts. The `cobalt_dev`-only guards apply before and after connecting.
- All 3 allowed dry-run tries were used. Both failures were script errors that rolled back inside the transaction. The BEFORE digest of try 3 and of the commit run matches try 2's BEFORE, so the failed tries left nothing behind.
- Script path `/Users/cobalt/cobalt-wt/devdb-rebuild-1002/rebuild_aset_sizings.py`: not in git, kept for reuse. The same shape of rebuild applies to any other table that hits `TooManyColumns`.
- No git write and no production command were run. Under `/Users/cobalt/cobalt`, only this report was written.

REBUILT · aset_sizings max_attnum 1581 → 54 · rows 1 = 1 · FP F1 = F0 · proof test: PASSED · cobalt_dev: 0013 · .env: removed · decisions: 0 · for Dejan: 0
