# draft-dml-roles — 2026-10-13

## §0 Headline
- Card `prompts/2026-10-13/448-dml-roles-card.md` written (CLASS K3, K5), proved against main `692ff5ae`. It has seven rows: M1 migration `0025_dml_roles` plus 19 head pins, G1 catalog pin, A1 `SET LOCAL ROLE` after `db_apply.py:244`, R1 with-DB red, W1 gate lists, C1 CARD.md checklist, R2 RESTARTS (expected `com.cobalt.radar`).
- The second role is built as `cobalt_apply_system`, not `cobalt_apply_brain`: the sides are user and system, and `cobalt_brain` is the database name (DECISION 1).
- `RULINGS` carries R1138, not R1309: `authorize.sh:113-116` passes only a `HIS RULING · APPROVED` row (DECISION 4).
- Rollback revokes only this database's grants; roles and `cobalt_app`'s membership are cluster-wide and stay (DECISION 6).
- No new command; INSTALL none; deploy after 304, outside market hours (card RECORDS).

## DECISIONS
- ASK DESK: role name. Prompt 447 and the OWED line say `cobalt_apply_brain`; the brain's text (R1268; check report `:251`) says `cobalt_apply_<side>`, and `Side` is `user`/`system` (`db.py:124-125`). Default: `cobalt_apply_system`. [05:58]
- ASK DESK: default privileges. The row grants on existing tables, plus a checklist line for new migrations. Tables a store's `ensure_schema()` creates at runtime under its side role (11 stores) would miss the grant. Default: 0025 also runs `ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_<side>, <migration login>`, as `0001_schemas.sql:141-162` does; R1's fixture relies on it. If NO: drop M1 (4) and G1f, and R1's fixture gets an explicit `GRANT`. [05:58]
- ASK DESK: migration number. `0025` is next free on main; F5's tribunal design names `0025_market_checkpoints`, but no F5 card exists yet. Default: this card takes `0025`; F5 takes the next free number at its drafting. [05:58]
- ASK DESK: RULINGS. Prompt 447 sets `2026-10-13 R1309`, a `DIRECTION` row (`cto-2026-10-13.md:12`); `authorize.sh` fails any `RULINGS` row without `HIS RULING`…`APPROVED`. Default: `RULINGS: 2026-10-12 R1138`, with R1309 kept in `LADDER` (precedent: cards 441, 434, 397). [05:58]
- ASK DESK: `DB` key. Prompt 447 sets `DB cobalt_dev`; CARD.md allows only `none`, else the key is left out; card 417 left it out. Default: no `DB:` line; the job runs on `cobalt_dev` under the lock. [05:58]
- ASK DESK: L76 and the cluster-wide roles. After the gate's `--down-to 0013`, `cobalt_dev` keeps the two roles and `cobalt_app`'s membership in them, with no privilege; `F2 = F0` holds. Dropping either would cut `cobalt_brain`'s door once 0025 is deployed there. Default: the rollback revokes only per-database grants and default privileges, never `DROP ROLE` or a membership revoke (as 0001's roles are never reversed). [05:58]
- ASK DESK: CARD.md has no migration checklist (`grep -n -i checklist` prints nothing). Default: C1 appends `## A MIGRATION ROW, CHECKLIST (card 448)` with six lines of card 73's practice (number, registry and head pins, `CREATED_TABLES`, THE GRANT, gate lists, deploy `MIGRATIONS`/`READ-BACK`), pinned by `tests/ops/test_card_md_migration_checklist.py`. [05:58]

## RECORDS
- `grep -rn "D1 follow-up migration card" reports/` → `db-apply-prod-check-2026-10-12.md:251` and `cto-2026-10-13.md:17` only; `cto-2026-10-12.md` holds it as R1268 (`:45`); `grep -rln "DML-only"` → those two cto files and the check report.
- `cto-2026-10-13.md`: R1309 `:12` (`DIRECTION`), second OWED line `:17`, F5 drafter `:19`. `cto-2026-10-12.md`: R1138 `:173` (`HIS RULING · APPROVED`).
- `prompts/2026-10-12/417-db-apply-prod-card.md` read whole (92 lines); `reports/db-apply-prod-build-2026-10-12.md:205-228` (RESTARTS table, `db_apply.py` → `com.cobalt.radar` `:218`); `reports/deploy-db-apply-prod-1012.md:6`, `:206`.
- `src/cobalt/db_apply.py`: constants `:43-70`; `apply_statements` `:236-283` (autocommit `:240`, timeouts `:243-244`, `current_user` `:246`, check `:255-257`); `command` `:292-307`; `__all__` `:319`.
- `src/cobalt/db.py`: `APP_ROLE` `:93`, credentials `:35-70`, `Side` `:115-133`, `apply_side` `:202-224` (`SET ROLE` against the session user `:210-211`), `connect` `:227-266`, `connect_migration` `:269-300`.
- `src/cobalt/db_migrations/0001_schemas.sql` read whole: idempotent roles `:73-85`, grant to `current_user` `:93-97`, ownership `:29-32`, `:102-103`, `:174`, default privileges `:141-162`, cluster-wide `:55-59`.
- `src/cobalt/db_migrations/__init__.py` read whole (FORWARD ends 0024, REVERSE begins 0024); `ls` of the folder (0001–0024, no 0012); `cli.py:406-421` (`_table_creators`); `dev_rebuild.py` ACL restore `:407-431`, `:619`, `:734`.
- `ops/cobalt_app_role_provision.py:1-200` (`MEMBERSHIPS` `:78`, grant `:104-113`, refuses an existing role `:152-156`).
- `grep -n "def ensure_schema"` of `src/cobalt` → 11 stores.
- Tests: `test_db_apply.py:394-515` (FakeConn `:405-438`, T3 `:470-474`, T7 `:477-489`, T4 `:504-513`), `:55-56`, `:142`; `test_db_apply_db.py` read whole; `migration_retry.py:25`; `test_tenancy.py:362-396`, `:505-539`; `grep` of `0024` over `tests/` → 19 files (listed in M1).
- `ops/desk/gate-lists.md` read whole; `grep -c -F "test_db_apply_db.py"` → `0`; `ops/desk/gate.sh:2`, `:14-24`, `:475-500`; `ops/desk/authorize.sh:100-120`, `:141-165`.
- `BUILD-HUB.md:14`, `:35`, `:39`, `:68`, `:75-81`, `:92`; `CARD.md` read whole (ends `:147`); `test_prodwrite_hub.py:145-150`, `:165-166`, `:187-191`; `test_deploy_card.py:426`; `test_desk_launch_prechecks.py:826`.
- LAWS L1, L4, L41, L51, L62, L76, L81 read (`LAWS.md:107`, `:116`, `:249`, `:285`, `:320`, `:385`, `:403`); R411 `cto-2026-10-05.md:107`, R412 `:109`.
- Card 73 rows S3, W1 and its RESTARTS line; `deploy-s4-p2-1009.md:91-94`; cards 441, 434, 397 headers (`CLASS: K5`, `INSTALL: none`, `RULINGS: 2026-10-12 R1138`).
- `ls -l /Users/cobalt/.claude/ops/desk-launch.sh` → link to `/Users/cobalt/cobalt/ops/desk/desk-launch.sh`.
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `ffd5e7a8`, later `692ff5ae`; `git -C /Users/cobalt/cobalt diff --stat ffd5e7a8 692ff5ae -- src tests ops configs "docs/40 - DevDocs/prompts/CARD.md" "docs/40 - DevDocs/prompts/BUILD-HUB.md"` → nothing.
- One read outside the listed git prefix: `git -C /Users/cobalt/cobalt-wt/f4-refresh-1010 diff --stat main...HEAD -- <this card's files>` → nothing (card 304 overlaps no file).
- Files written: the card and this report. No commit, no launch, no database.
DRAFTED · decisions: 7
