JOB: f15-e1-0930
LADDER: S3-P4 · F15
BRANCH: deploy/f15-e1-0930b
WORKTREE: deploy-0930-5
BASE: main
TIP: 1d70cf72 fb48997e
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-2026-09-30-4b.md
RULINGS: 2026-10-01 R1
TAG: deploy-2026-09-30-4
MIGRATIONS: 0022 · production at 0021 · creates: table "user".prediction_records (with its trigger prediction_records_immutable and its identity sequence) and column "user".aset_sizings.last_price_bar_ts · old code on the new schema: main's src names neither object except placement.py:135, which already places prediction_records on Side.USER; it reads aset_sizings by column name (aset/models.py:135 from_card, aset/store.py:276) and inserts with a column list (aset/store.py:129, cards/store.py:1097); and no DELETE of aset_sizings exists in src, ops or dev_utils, so the new FK and trigger are never hit — a code revert alone runs on 0022
SET: f15e1

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `f15/p1-records` | `1d70cf72` | `1d70cf72` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f15-p1-check-2026-09-30.md` | `held unfixed: 0` and `ready: YES` |
| 2 | `s3/e1-inline-0930` | `fb48997e` | `fb48997e` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/e1-inline-check-2026-09-30.md` | `held unfixed: 0` and `ready: YES` |

## RECORDS
- THE WINDOW (desk, 05:59 ET Thursday 2026-10-01): the overnight idle (`DEPLOY-HUB.md` P1 (ii)) closed at 04:00 ET. Thursday is a trading day. His per-case override of the window for THIS deploy is `cto-2026-10-01.md` R1 (`HIS RULING`, `APPROVED`), cited in `RULINGS`; P1 records it as the window.
- THE RESTART SET, as both checks' stop lines give it: `RESTARTS: com.cobalt.aset com.cobalt.radar` (`f15-p1-check-2026-09-30.md:335`, `e1-inline-check-2026-09-30.md` last line). The hub derives its own at STEP-R (L42).
- THE CHECKS: f15-p1 pass 1 `CHECK DONE · job: f15-p1 · pass: 1 · tip: 1d70cf72 … held unfixed: 0 … ready: YES · decisions: 2 · for Dejan: 0`. Its 2 decisions were answered by `f15-p1-check-decisions-2026-09-30.md:13` (`answered: 2 of 2 · for Dejan: 0`). e1-inline pass 2 `CHECK DONE · job: e1-inline · pass: 2 · tip: fb48997e … held unfixed: 0 … ready: YES · decisions: 0 · for Dejan: 0`. Each head equals its code tip: `git -C /Users/cobalt/cobalt log -1` (short hash) of `f15/p1-records` → `1d70cf72`, and of `s3/e1-inline-0930` → `fb48997e` (the drafter, 22:41 ET). f15's head `1d70cf72` (`wip(f15-p1): check red — O4 …`) is the check's FIX commit, a test only: `tests/cobalt/test_f15_p1_records_db.py | 20 +` (`f15-p1-check-2026-09-30.md:223`, `:230`, `:271`). It is green on the tip: W (c3) `171 passed` (`:250`).
- MERGE ORDER `1d70cf72` then `fb48997e`. The two branches share no file. `git -C /Users/cobalt/cobalt log --oneline main..s3/e1-inline-0930 --` over F15's eleven `src/` paths, `tests/cobalt/test_f15_p1_records_db.py` and the two hub files → EMPTY. `git -C /Users/cobalt/cobalt log --oneline main..f15/p1-records -- src/cobalt/prefill tests/cobalt/test_s3_c4_trade_note_offline.py "docs/40 - DevDocs/cobalt/prefill"` → EMPTY. Since either branch, `main` moved in reports and dated prompts only: `git -C /Users/cobalt/cobalt log --oneline <branch>..main -- . ":(exclude)docs/40 - DevDocs/reports" ":(exclude)docs/40 - DevDocs/prompts/2026-09-30"` → EMPTY for both. The `merge-tree` half is the hub's own gate, at STEP-T (L68) (the drafter, 22:41 ET).
- THE MIGRATION FILES: on `f15/p1-records`, commit `8747dc75` touches under `src/cobalt/db_migrations` the pair `0022_prediction_records.sql` / `.rollback.sql` and the registry files `__init__.py`, `cli.py`, `placement.py` (`git -C /Users/cobalt/cobalt log --oneline --stat main..f15/p1-records`). At the head, `FORWARD` ends `0021_legs.sql`, `0022_prediction_records.sql`, and `REVERSE` begins `0022_prediction_records.rollback.sql`, `0021_legs.rollback.sql` (`/Users/cobalt/cobalt-wt/f15-p1-0930/src/cobalt/db_migrations/__init__.py:155-156`, `:161-162`). e1-inline touches no migration path.
- P7 (desk reading, 22:46 ET): the `db_migrations` diff stat of head `1d70cf72` prints exactly the five paths above — they ARE the files of this card's `MIGRATIONS` (the pair plus the three registry files the migration edits, as STEP-T admits); any other path under `src/cobalt/db_migrations` is a refusal.
- PRODUCTION AT 0021: deploy 2 applied it (`deploy-2026-09-30-2.md` stop line `migrations: 0021`; `<RB>` after `5 · 1 · 2 · 4`, `:235`). Deploy 3 applied none (`deploy-2026-09-30-3.md:108`, `migrations applied: none`). `0022` is free on `main`: `ls /Users/cobalt/cobalt/src/cobalt/db_migrations/0022_prediction_records.sql` → No such file.
- THE TREE STATE ROW: F15's row T1 edits `DEPLOY-HUB.md` STEP-G on its branch. It adds `tests/cobalt/test_f15_p1_records_offline.py` to (a0), and adds the four 0022 files and one `--deselect` to (c3), in commits `8747dc75` and `28d9364f`. That edit reaches `main` only with this deploy, so the hub runs STEP-G's lines as `main` has them (`DEPLOY-HUB.md:98`).
- ATTEMPT 2 (desk, 06:05 ET): attempt 1 (`deploy-2026-09-30-4.md`, branch `deploy/f15-e1-0930`, gate `deploy-0930-4`) ended `FAILED PREFLIGHT P2` before any step touched anything: the two check reports were untracked on `main`; they are committed now (`git log -1 -- <each>` non-empty). Its gate worktree is clean and unused; this launch uses fresh names (`deploy/f15-e1-0930b`, `deploy-0930-5`, report `-4b`). Tag names `deploy-2026-09-30-4` and `pre-f15-e1-0930` are still free.
- NAMES ARE FREE (attempt 1; attempt 2 re-checks them): `ls -d /Users/cobalt/cobalt-wt/deploy-0930-4` → No such file. `git -C /Users/cobalt/cobalt log -1 deploy/f15-e1-0930 --` → `bad revision`. The same for `refs/tags/deploy-2026-09-30-4` and `refs/tags/pre-f15-e1-0930` → `bad revision` (the drafter, 22:42 ET).

## MARKERS
- `ls /Users/cobalt/cobalt/src/cobalt/db_migrations/0022_prediction_records.sql` · before `No such file or directory` · after listed
- `ls /Users/cobalt/cobalt/src/cobalt/cards/predictions.py` · before `No such file or directory` · after listed
- `grep -c -F "0022_prediction_records" /Users/cobalt/cobalt/src/cobalt/db_migrations/__init__.py` · before `0` · after `5`
- `grep -c -F "def inline_comment(" /Users/cobalt/cobalt/src/cobalt/prefill/trade_note.py` · before `0` · after `1`

## READ-BACK
`COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname = 'user' AND c.relname IN ('legs', 'legs_current_v')) AS m0021, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname = 'user' AND c.relname = 'prediction_records' AND c.relkind = 'r') AS m0022t, (SELECT count(*) FROM pg_catalog.pg_trigger t JOIN pg_catalog.pg_class c ON c.oid = t.tgrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname = 'user' AND c.relname = 'prediction_records' AND t.tgname = 'prediction_records_immutable') AS m0022g, (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname = 'user' AND c.relname = 'aset_sizings' AND a.attname = 'last_price_bar_ts' AND NOT a.attisdropped) AS m0022c"`
- BEFORE `2 · 0 · 0 · 0` (`legs` and `legs_current_v` present, the 0021 level; no table, trigger or column of 0022)
- AFTER `2 · 1 · 1 · 1`

## SMOKE READS
- F15 table · `COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT count(*) FROM \"user\".prediction_records"` · exit 0, one integer
- F15 column · `COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT count(*) FROM \"user\".aset_sizings WHERE last_price_bar_ts IS NOT NULL"` · exit 0, one integer
- census · `COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT count(*) FROM \"user\".aset_sizings"` · exit 0, one integer before the outage and one after, recorded
- E1 inline · `grep -c -F "def inline_comment(" /Users/cobalt/cobalt/src/cobalt/prefill/trade_note.py` · exit 0, `1`; the E1 tests' PASSED lines in `tests/cobalt/test_s3_c4_trade_note_offline.py` are quoted from G (a)
