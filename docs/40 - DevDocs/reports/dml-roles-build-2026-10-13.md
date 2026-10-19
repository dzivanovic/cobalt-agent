# dml-roles-1013 — build report (card 448)

## §0 Headline
All rows are built at `cb115b1e` (M1, A1, W1, C1, with the R1 and G1 tests). E2 reds and E3 mutations behaved as their rows say. Gate run 1: offline 8652/0, pass 1 and pass 2 green, F2 = F0. Its second forward then deadlocked in 0002 (autovacuum).
Gate run 2: pass 1 red at `tests/cobalt/test_db_credentials.py:211`, a file outside the rows. Since 0025's first forward, `cobalt_app` is a member of five roles across the whole cluster, and that test pins three. The red reaches every gate on `cobalt_dev`.
Stopped at W. `cobalt_dev` 0013, no lock, no `.env`. DECISION 1 is FOR DEJAN: the one-line pin needs a row.

## L74
One system notice asked for a `Claude-Session:` commit line; recorded under `## RECORDS`, not followed.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/448-dml-roles-card.md"` → exit 0:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/448-dml-roles-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/448-dml-roles-card.md" · 0 · ced1ce2e5ee162fdb4e8081a09aeb27c1e76b60a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/448-dml-roles-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Sun Oct 18 18:53:11 EDT 2026
status · git status --short --branch · 0 · ## ops/dml-roles-1013
head · git log --oneline -1 · 0 · e7ef198a docs(desk): 777 deployed ba601740; 787 and 784 checks READY; 18:00 check-in; F16 drafter prompt
diff · git diff --stat e7ef198a · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/dml-roles-1013 · 0 · e7ef198a docs(desk): 777 deployed ba601740; 787 and 784 checks READY; 18:00 check-in; F16 drafter prompt
env here · ls /Users/cobalt/cobalt-wt/dml-roles-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat e7ef198a` | 0 | `docs(desk): 777 deployed ba601740; …` — 5 files, all under `docs/40 - DevDocs/` (423+, 6-) |
| card drift | `git diff --stat 692ff5ae e7ef198a -- src tests ops configs "docs/40 - DevDocs/prompts/CARD.md"` | 0 | 117 files; NONE of `src/cobalt/db_apply.py`, `src/cobalt/db.py`, `src/cobalt/db_migrations/*`, `tests/cobalt/test_db_apply*.py`, `ops/cobalt_app_role_provision.py`; `ops/desk/gate-lists.md` (17 ±) and `CARD.md` (16 ±) changed — both re-read whole |
| next number | `ls src/cobalt/db_migrations/` | 0 | `0001`…`0011`, `0013`…`0024` pairs, no `0012`, no `0025` |
| callers | `grep -rn -F "apply_statements(" src` | 0 | `src/cobalt/db_apply.py:236` (def), `src/cobalt/db_apply.py:305` (`command`) |
| stores | `grep -rn -F "def ensure_schema" src/cobalt` | 0 | 11 hits (settings, drc, cards, archiver, daymode, redact, taxonomy, vaultwrite, jobs, aset, session) |
| head pins | `grep -rn "0024" tests` | 0 | the card's list, plus `test_strike_ack_db.py` / `test_strike_stream_db.py` (apply 0024 by file, not a head pin) and `test_archiver_migrations.py:518` (survivor list, unchanged); `test_tenancy.py:517` (card `:516-531`) |
| placement | `grep -n -F "CREATED_TABLES" src/cobalt/db_migrations/placement.py` | 0 | `64:CREATED_TABLES: dict[str, Side] = {` |
| provision | `grep -n -F "MEMBERSHIPS" ops/cobalt_app_role_provision.py` | 0 | `78:MEMBERSHIPS = ("cobalt_system", "cobalt_user", "cobalt_backup")` |
| symbols read | Read tool | — | `db_apply.py:60-61` timeouts, `:236-283` `apply_statements`, `:244` lock_timeout, `:246` current_user, `:255-257` check, `:319` `__all__`; `db.py:85` `PROD_DB_NAME`, `:93` `APP_ROLE`, `:124-125` sides, `:132-133` role, `:210-211` SET ROLE vs session user, `:269-300` `connect_migration`; `0001_schemas.sql:55-59`, `:73-85`, `:141-162`, `:168-174`; `test_db_apply.py:408`, `:421-422`, `:477-489`; `test_db_apply_db.py:36-39`, `:46-58`, `:70-71`; `CARD.md` prodwrite section now `:155-161` (card said `:141-147`; the file is 161 lines, the new section goes after `:161`) |
| wc -l | `wc -l …` | 0 | db_apply.py 335 · db_migrations/__init__.py 197 · test_db_apply.py 581 · test_db_apply_db.py 155 · gate-lists.md 57 · CARD.md 161 |
| READ tails | `tail -n 3` | 0 | draft-dml-roles: `DRAFTED · decisions: 7`; draft-448-amend: `DRAFTED · decisions: 1`; db-apply-prod-check: `CHECK DONE · job: db-apply-prod-1012 · … ready: YES · decisions: 3 · for Dejan: 0 · tokens: 290333` |
| R1309 | `grep -n -F "\| R1309 " cto-2026-10-13.md` | 0 | `158:| R1309 | 00:32 ET | DESK RECORD, brain (L79) queue 10-13: 304 deploys first; DML-only roles migration (417 D1) drafter now, deploys after 304; … | DIRECTION |` |
| RESTARTS | `uv run cobalt jobs restarts e7ef198a..HEAD` | 0 | one row, this report (uncommitted, `DOCS`); `RESTARTS: none` |

Card `## RECORDS` copied (re-read where the list can): drafter reads at `692ff5ae` (re-read: the drift row above — the card's own `file:line`s in `src`/`tests` hold, CARD.md's moved); row source R1268 / check `:251`; roles cluster-wide (`0001_schemas.sql:55-59`, re-read); THE LOCK plan (E2 one take, W `--deselect` ×2 `--migration`); COMMANDS standing; INSTALL none; RULINGS R1138 (re-read: AUTHORIZATION row); MIGRATION NUMBER 0025 (re-read: `ls`); card 304 no overlap; `dev_rebuild` ACL; Postgres facts (proven by the with-DB runs); RESTARTS classes; deploy after 304. FOR THE CHECK: brain D1-D7 KEEP; D2 DML-only default privileges pinned by `pg_default_acl`.

`<FP>` (typed exactly at each take):
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4646 passed, 841 skipped, 4 xfailed, 36 warnings in 722.74s (0:12:02)`, exit 0.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.09s`; the one skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Offline: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dml_roles_offline.py tests/cobalt/test_db_apply.py tests/ops/test_card_md_migration_checklist.py` → `12 failed, 107 passed`. Each red's first line:
- O1 `AssertionError: assert '0024_strike_alerts.sql' == '0025_dml_roles.sql'`; O2 / O3 `FileNotFoundError: … 0025_dml_roles.sql` / `… 0025_dml_roles.rollback.sql`.
- T1 `AssertionError: ('STATEMENT 1/3', "FAILED: current_user is 'cobalt_apply_user', not 'cobalt_user' — ROLLED BACK` (`:454`, its first `want in text`); T2 `assert 1 == 0` (`:462`); T7[USER], T7[SYSTEM] `ImportError: cannot import name 'APPLY_ROLES'` (`:479`); T10 `assert 0 == 1` (three statements sent, `COMMITTED · statements: 3 · rows: 6`); T11 `AttributeError: module 'cobalt.db_apply' has no attribute 'APPLY_ROLES'`; T12 `AssertionError: [('execute', "SET LOCAL statement_timeout = '60s'", {}), ('execute', "SET LOCAL lock_timeout = '5s'", {}), ('execute', 'SHOW server_version_num', {}), ('execute', 'SELECT current_user', {}), …]` (no `SET LOCAL ROLE` sent).
- K1 `assert 0 == 1` (count of `\n## A MIGRATION ROW, CHECKLIST`); K2 `IndexError: list index out of range`.
- T12 REWRITTEN once: the card predicts "T12 returns 0" on BASE, but with `FakeConn`'s default role now `cobalt_apply_user` (the row's own change) BASE's `current_user` check returns 1 first, so the first run's red was `'FAILED before statement 1' in "FAILED: current_user is 'cobalt_apply_user', not 'cobalt_user' …"`. The test now asserts first that a `SET LOCAL ROLE` was sent, so its red is the row's reason (no `SET LOCAL ROLE` is sent); `exit 1 · sent 0 · FAILED before statement 1` stand after it.

With-DB, ONE lock take (19:10 EDT, `date`): `lock taken: dml-roles-1013`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, this worktree's. `<FP>` → F0 `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` · `TABLES 0011` (level 0013; NO forward). `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dml_roles_db.py tests/cobalt/test_db_apply_db.py` → `19 failed, 7 passed in 0.64s`:
- G1a ×2 `AssertionError: [] · assert 0 == 1` (no `pg_roles` row); G1b, G1c, G1d, G1f ×2 each `psycopg.errors.UndefinedObject: role "cobalt_apply_user" does not exist` (`cobalt_apply_system` on its side); G1e ×2 `no pg_auth_members row from cobalt_apply_<side> to cobalt_app · assert []`; G1g `FileNotFoundError: … 0025_dml_roles.rollback.sql`; G1h ×2 `no pg_default_acl entry names cobalt_apply_<side> in <schema> · assert []`.
- R1 drop / alter / truncate / create each `assert 0 == 1` with `COMMITTED · statements: 1 · rows: 0` (as owner `cobalt_user` each runs).
- PASSED: T5, T6, A7 [a] [b] [c], T9 and the negative control `test_an_allowed_update_succeeds_under_the_apply_role`.
`<FP>` again → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = F0. `release-devdb-lock.sh dml-roles-1013` → `lock released`; `ls …/.env` → `No such file or directory`. `.env: removed, proven gone (E2)` (19:10 EDT).
Commit `8babdd5b wip(dml-roles-1013): red — M1 O1-O3, G1a-h, A1 T7/T10-T12, R1, C1 K1-K2` (tests only).

## E3 THE ROWS
Built in card order; one commit `cb115b1e feat(dml-roles-1013): DML-only apply roles 0025 and db apply SET LOCAL ROLE (M1, A1, W1, C1; L1, L42, L72, L76)`.
- M1: NEW `0025_dml_roles.sql` (roles in a `pg_roles`-guarded `DO`, `GRANT cobalt_apply_user, cobalt_apply_system TO cobalt_app`, per-side DML / USAGE grants, one `DO` of four `ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_<side>, %I …`), NEW `0025_dml_roles.rollback.sql` (one `DO` guarded on both roles: default privileges, table, sequence, schema revokes; no `DROP ROLE`, no membership revoke), `__init__.py` `FORWARD` last / `REVERSE` first and two docstring lines. No line starts `CREATE TABLE IF NOT EXISTS`. Head pins moved in all 17 files the card lists (`# DML roles (0025)`), plus the index moves the pins drag with them: `test_drc_d3_experiments.py:91`, `:93` (`FORWARD[-6]`, `REVERSE[5]`), `test_drc_store.py:71`, `test_drc_k1_store.py:120`, `test_radar_score_migration.py:121`, `:126`, `:131` (`[:15]`). `grep -rn "0024" tests` after the move: only the strike tests that apply 0024 by name and `test_archiver_migrations.py:518` (unchanged). Pins run: `224 passed, 166 skipped`.
- M1 MUTATIONS (one run, all three in place): forward `GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA system …`, rollback `+ REVOKE cobalt_apply_user, cobalt_apply_system FROM cobalt_app;`, `FORWARD` without 0025 → `5 failed, 51 passed`: O1 `assert '0024_strike_alerts.sql' == '0025_dml_roles.sql'`; O2 `assert 1 == 2` (the DML grant count); O3 `AssertionError: REVOKE cobalt_apply_`; `test_forward_ends_0008_0009_0010_0011` and `test_the_registry_is_an_explicit_contiguous_list…` (`1…11 then 13–25, got […, 24]`). Undone with Edit; `git diff --stat` back at the fix.
- A1: `db_apply.py` `APPLY_ROLES` (`#:` line naming 0025, in `__all__`), `SET LOCAL ROLE {APPLY_ROLES[side]}` directly after the lock timeout inside the same `try`, the `current_user` check against `APPLY_ROLES[side]`, A4 docstring line. `test_db_apply.py` + `test_db_apply_db.py` offline → `114 passed, 11 skipped`. MUTATIONS: (1) the `SET LOCAL ROLE` line removed → `3 failed`: T7[USER] / T7[SYSTEM] `At index 2 diff: 'SHOW server_version_num' != 'SET LOCAL ROLE cobalt_apply_user'` (`…_system`), T12 `assert 0 == 1`; (2) the check widened to `current not in (APPLY_ROLES[side], side.role)` → `1 failed`: T10 `assert 0 == 1`; (3) `Side.SYSTEM: "cobalt_apply_user"` → `1 failed`: T11 `Differing items: {<Side.SYSTEM: 'system'>: 'cobalt_apply_user'} != {… 'cobalt_apply_system'}`. Each undone; `git diff --stat src/cobalt/db_apply.py` → `13 ++++++++++---` (the fix).
- R1, G1 (with-DB): their reds are E2's (at 0013, no forward); their greens are W run 1's pass 2 (below). No by-hand forward was run for a with-DB mutation (`BUILD-HUB.md` `## W` (c): a deselected with-DB file runs only in the gate).
- W1: `gate-lists.md` PASS 1 ends `--deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py`, PASS 2 ends `tests/cobalt/test_db_apply_db.py tests/cobalt/test_dml_roles_db.py`. RUN: `grep -c -F "test_db_apply_db.py" ops/desk/gate-lists.md` → `2`; `grep -c -F "test_dml_roles_db.py" ops/desk/gate-lists.md` → `2`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_gate.py` → `70 passed, 15 warnings in 23.89s`.
- C1: `CARD.md` gains `## A MIGRATION ROW, CHECKLIST (card 448)` after the prodwrite section (now `:155-161`, not the card's `:141-147`; see PREFLIGHT). `test_card_md_migration_checklist.py`, `test_prodwrite_hub.py`, `test_deploy_card.py`, `test_desk_launch_prechecks.py`, `test_card_template_1014.py`, `test_band_routing_1015.py`, `test_deploy_step_c.py` → `453 passed`. MUTATION: `test_dml_roles_db.py` dropped from item 4 → K2 `AssertionError: test_dml_roles_db.py`; undone.
- DevDocs: `docs/40 - DevDocs/cobalt/db_apply.md` and `cobalt/db_migrations/__init__.md` each gain `## 2026-10-18 — dml-roles-1013`.

## RESTARTS
`uv run cobalt jobs restarts e7ef198a..HEAD` (at `cb115b1e`, the report still untracked): `src/cobalt/db_apply.py` and `src/cobalt/db_migrations/__init__.py` `static import reach` `com.cobalt.radar`; both `.sql` `non-Python src asset`; `ops/desk/gate-lists.md` `operator script; no Cobalt reader`; every `tests/…` `test/documentation; no resident`; every `docs/…` `DOCS`. No UNCLASSIFIED row. Last line `RESTARTS: com.cobalt.radar`, as R2 expected.

## W THE THREE SUITES
`<tip>` = `cb115b1e`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh dml-roles-1013 all --deploy --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --migration`. No `--tickers`: no test of this build writes `aset_sizings`.

RUN 1, log `/Users/cobalt/cobalt-wt/.gate-logs/dml-roles-1013-all-20261018-191840.log`, exit 1. Verdict lines: `tests/ops: run (docs/40 - DevDocs/prompts/CARD.md)` · `offline 8652/0` · `lock: waited 0 min` · `proof-only: on cobalt_dev, nothing CHANGED …` · `LEVEL 0013` · `pass 1: whole (deploy)` · `stray rows: not read (no --tickers given)` · `RED: the second forward failed (log)` · `.env: removed`.
- offline `4653 passed, 861 skipped, 4 xfailed` (`:935`); tests/ops `3999 passed, 1 xfailed` (`:1008`); F0 `664 35 272c95bbb12241e3611e4b36326ccf87` (`:1025`); pass 1 `5376 passed, 8 skipped, 127 deselected, 7 xfailed` (`:1245`); `dev forward: APPLIED 19:59:58` (`:1247`); F1 `908 45 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1326`); pass 2 `233 passed, 1 deselected, 5 warnings` (`:2168`), every R1 and G1 id `PASSED` (`:2142-2167`); (f) rollback `-- applying 0025_dml_roles.rollback.sql` first, `content UNCHANGED on every table`, F2 `664 35 272c95bbb12241e3611e4b36326ccf87` = F0 (`:2237`).
- (c4) the second forward: `FAILED: DeadlockDetected: deadlock detected` · `CONTEXT:  SQL statement "ALTER TABLE system.bars OWNER TO cobalt_system"` (in `0002_move_tables.sql`; `:2291-2299`). The trap rolled back: F2 `664 35 272c95bbb12241e3611e4b36326ccf87` (`:2368`), `lock released` (`:2421`), `.env: removed` (`:2425`). This is the autovacuum deadlock `tests/cobalt/migration_retry.py` names, on a line this build did not write. So a second gate call was made (RECORDS).

RUN 2, log `/Users/cobalt/cobalt-wt/.gate-logs/dml-roles-1013-all-20261018-200523.log`, exit 1. Verdict lines: `tests/ops: run (docs/40 - DevDocs/prompts/CARD.md)` · `offline 8652/0` · `lock: waited 0 min` · `proof-only: … nothing CHANGED` · `LEVEL 0013` · `pass 1: whole (deploy)` · `RED (exit 1): 1 failed, 5375 passed, 8 skipped, 127 deselected, 7 xfailed, 43 warnings in 856.03s (0:14:16)` · `.env: removed`. F0 `664 35 272c95bbb12241e3611e4b36326ccf87` (`:1025`); no forward ran; `lock released` (`:1292`), `.env: removed` (`:1296`).
- THE RED (`:1160-1181`): `tests/cobalt/test_db_credentials.py::TestTheLiveFactoryAuthenticatesAsCobaltApp::test_it_is_a_member_of_all_three_side_roles` — `assert [r[0] for r in rows] == ["cobalt_backup", "cobalt_system", "cobalt_user"]` · `At index 0 diff: 'cobalt_apply_system' != 'cobalt_backup'` · `Left contains 2 more items`. Run 1's forward made `cobalt_app` a member of the two apply roles for the whole cluster. The rollback keeps those memberships by the card's own design (M1, `## DECISIONS` 6), so from then on pass 1 at 0013 reads five memberships. Run 1's pass 1 was green only because it ran before any forward. E2 / E3 could not show this: the pin is with-DB and the memberships did not exist before the gate's forward.
- The 8 pass-1 skips (run 2 `:19-26` of the gate output), each with its reason: `test_cards_picks.py:388`, `:401`, `test_playbook_live.py:31`, `test_radar_evaluate.py:695`, `test_replay_line.py:266`, `test_s3_c4_experiments.py:95`, `test_catalyst.py:365`, `test_predicate.py:262`; none is marked `OUTSIDE the allowed set`.
- live-note (e): not reached in either run.
- State now: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `ls /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → `No such file or directory`; no migration above 0013 applied (run 2 stopped in pass 1; run 1's two rollbacks ended F2 = F0). `cobalt_dev: 0013 — F2 = F0` (run 1). The cluster keeps `cobalt_apply_user`, `cobalt_apply_system` and `cobalt_app`'s two memberships, as the card's RECORDS predicted.

## PRE-STOP SELF-CHECK
Not reached: W is red.

## FOR THE CHECK
`e7ef198a..cb115b1e`: `8babdd5b wip(dml-roles-1013): red — M1 O1-O3, G1a-h, A1 T7/T10-T12, R1, C1 K1-K2`; `cb115b1e feat(dml-roles-1013): DML-only apply roles 0025 and db apply SET LOCAL ROLE (M1, A1, W1, C1; L1, L42, L72, L76)`. Reds, mutations and greens per row: `## E2 RED` and `## E3 THE ROWS`. Caller greps: `## PREFLIGHT` (`apply_statements(`: `db_apply.py:236`, `:305`). RUN rows W1 and R2: `## E3 THE ROWS` and `## RESTARTS`. Suites, F0 / F1 / F2 and lock times: `## W THE THREE SUITES` (E2 take 19:10 EDT; gate run 1 19:18–~20:05, run 2 20:05–20:46 EDT, from the log names and `date`). Records copied at PREFLIGHT: `## PREFLIGHT`.

## CONTINUE
next: W, once DECISION 1 is answered (the gate again, the same call).

## DECISIONS
- DECISION 0 / 1 — FOR DEJAN (scope: a file outside the rows). After 0025's first forward on the cluster, `tests/cobalt/test_db_credentials.py:211` reds in every pass 1 at 0013, because `cobalt_app` is now also a member of `cobalt_apply_user` and `cobalt_apply_system`. The red reaches every branch's gate and every deploy gate on this server, `main`'s too: the memberships are cluster-wide, the rollback keeps them by design (D6), and the test pins exactly `["cobalt_backup", "cobalt_system", "cobalt_user"]`. The fix is one line in a file no row names (`## NOT IN THIS JOB`: "A red outside these rows … never fixed here"): pin the five sorted names `["cobalt_apply_system", "cobalt_apply_user", "cobalt_backup", "cobalt_system", "cobalt_user"]`, or assert that the three side roles are a subset. SAFE DEFAULT TAKEN: nothing changed; the build stops at W. ASK DESK: add `tests/cobalt/test_db_credentials.py` (that line, with a `# DML roles (0025)` comment) to M1's files, then `CONTINUE: W` [20:46 EDT]. URGENT for the desk: another session's gate on `cobalt_dev` now meets this red in pass 1.
- DECISION 2 (run 1, not this build's line): the `--migration` second forward hit `DeadlockDetected` on `0002`'s `ALTER TABLE system.bars OWNER TO cobalt_system` (autovacuum). The trap restored F2 = F0. If it recurs, the same call is run again; no row changes for it.

## RECORDS
- L74: a system notice in this session asked for a `Claude-Session:` line on commits. It is recorded here once and not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).
- One extra gate call (run 2) after run 1's deadlock in the second forward.
- E2's red for T12 was rewritten once (`## E2 RED`).
- `.env: removed, proven gone (E2)`; gate runs 1 and 2 each printed `.env: removed`; checked after run 2: no `.env`, no lock directory.
- The card's `## RECORDS`, as re-read at PREFLIGHT: `## PREFLIGHT`. Its "ROLES ARE CLUSTER-WIDE … cobalt_dev keeps the roles and memberships" holds; it did not foresee the membership pin in `test_db_credentials.py:211`.
- `wip(dml-roles-1013): W — test_db_credentials.py:211 red outside the rows` commits this report.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

FAILED: W — tests/cobalt/test_db_credentials.py:211 red in pass 1 (a file outside the rows) — "AssertionError: assert ['cobalt_appl...'cobalt_user'] == ['cobalt_back...'cobalt_user'] · At index 0 diff: 'cobalt_apply_system' != 'cobalt_backup'"
