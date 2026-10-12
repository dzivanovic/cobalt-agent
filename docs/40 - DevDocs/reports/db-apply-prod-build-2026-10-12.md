# Build report — db-apply-prod-1012 (card 417)

## §0 Headline
- BUILT: all 12 rows (A1–A7, K1–K4, R1) on tip `dfcf2097`. The gate is green: offline 4307/0, with-DB 5210/0 and live-note 146/0. `cobalt_dev` is back at 0013 with F2 = F0, and `.env` is removed.
- The A7 hang came from the test, not the verb. The suite's autouse `dev_db_tx` replaces `db.connect` with a proxy over one open transaction. The scratch fixture's `DROP TABLE` then waited on that transaction forever. All with-DB connections in the file now use the real factory, so T5, T6 and T9 now prove the rollback across sessions as their rows say.
- RESTARTS: `com.cobalt.agent com.cobalt.aset com.cobalt.radar` (R1's expectation).
- Three decisions, none for Dejan. The first: `cobalt_user` owns schema `"user"`, so the parse-tree allowlist is the only fence against DDL on that side.

## L74
- 15:10 EDT: a system reminder asked commits to end with a `Claude-Session:` line. Recorded once; not acted on (commits carry `Co-Authored-By` only).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/417-db-apply-prod-card.md"` · exit 0 · 15:10 EDT
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/417-db-apply-prod-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/417-db-apply-prod-card.md" · 0 · 8ff2d1a376e55ab12c948e7d2352cd7031d23051
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/417-db-apply-prod-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 113:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · exit 0
```
clock · date · 0 · Mon Oct 12 15:11:11 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/db-apply-prod-1012
    ?? "docs/40 - DevDocs/reports/db-apply-prod-build-2026-10-12.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 8f1d11ed docs(desk): R1245 card 417 preflight round 3 ready YES
diff · git diff --stat 8f1d11ed · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/db-apply-prod-1012 · 0 · 8f1d11ed docs(desk): R1245 card 417 preflight round 3 ready YES
env here · ls /Users/cobalt/cobalt-wt/db-apply-prod-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/archiver-429-grok/.env
PREFLIGHT OK
```
`git show --stat 8f1d11ed` · 0
```
commit 8f1d11ed4fae7196dbc914d57198e597989dc41e
    docs(desk): R1245 card 417 preflight round 3 ready YES
 docs/40 - DevDocs/reports/cto-2026-10-12.md        |  5 +-
 .../db-apply-prod-preflight-r3-2026-10-12.md       | 61 ++++++++++++++++++++++
 2 files changed, 64 insertions(+), 2 deletions(-)
```
`uv run cobalt jobs restarts 8f1d11ed..HEAD` · 0 (the venv was created at this first `uv run`)
```
path	change	rule	restart
docs/40 - DevDocs/reports/db-apply-prod-build-2026-10-12.md	A	DOCS	-
RESTARTS: none
```
(the one path is this report, untracked; no commit in the range.)

THE CARD'S SYMBOLS (rule · command · exit · hits):
- pyproject · `grep pyproject.toml` (Grep tool, `psycopg\[binary\]|pglast|requires-python`) · 0 · `6:requires-python = ">=3.11"`, `53:    "psycopg[binary]>=3.3.2",`
- no parser locked · Grep `pglast|pg_query|sqlglot|sqlparse` in `uv.lock` · 1 · no match
- server image · Grep `image:` in `docker-compose.yml` · 0 · `4:    image: pgvector/pgvector:pg16`
- read path · Read `src/cobalt/db_query.py:145-216` · `163: conn.execute("BEGIN READ ONLY")`, `164-166` `SET LOCAL statement_timeout`, `167-169` `current_user` check, `195-198` the cobalt_brain refusal, `209 def add_query_parser(sub)`
- callers · `grep -rn -F "add_query_parser(" src` · 0 · `src/cobalt/db_query.py:209:def add_query_parser(sub) -> None:`, `src/cobalt/db_migrations/cli.py:1132:    add_query_parser(gsub)`
- factory · Read `src/cobalt/db.py:85-300` · `160 def _open`, `199 return psycopg.connect(dsn, autocommit=True)`, `227 def connect(`, `269 def connect_migration(`
- env · Read `src/cobalt/env.py:44-95` · `73 def is_production()`, `78 def resolve_db_name()`
- migrate cli · Read `db_migrations/cli.py` · `152 DEFAULT_LOCK_TIMEOUT_S = 30`, `163 CODE_ROOT = Path(__file__).resolve().parents[3]`, `972 def _refuse`, `977 def cmd_dev_rebuild(` (grep), `1028-1066` one transaction, `1130-1132` the query parser import
- top cli · Grep `def main|db_cli|build_parser|parse_args` in `src/cobalt/cli.py` · `65:from cobalt.db_migrations import cli as db_cli`, `500:def main() -> None:`, `523:    db_cli.add_parser(sub)`, `556:    args = parser.parse_args()`; Read `:17` `    cobalt db migrate [--allow-prod] [--rollback]`
- backup · `grep -rn -F "def load_backup_config(" src` · 0 · `src/cobalt/backup/config.py:161`; `grep -rn -F "def latest_snapshot_age(" src` · 0 · `src/cobalt/backup/restic.py:240`; Read `backup/cli.py:58-72` (`62` database OFF line, `66-69` NO DESTINATION ARMED, `70-71` age); `restic.py:51-52` `BackupError`, `254` `require_mounted(dest)`
- the function list's use · `grep -n -F "updated_at = now()" src/cobalt/jobs/store.py src/cobalt/drc/store.py` · 0 · hits include `jobs/store.py:120`, `:135`, `drc/store.py:501`
- RESTARTS reads · `grep -n -F "pyproject.toml" configs/cobalt/jobs.yaml` · 0 · `88`, `157`, `201`; `grep -n -F "imports:" configs/cobalt/jobs.yaml` · `99: imports: [cobalt.aset.__main__, cobalt.aset.web]`, `159: [cobalt_agent.main]`, `203: [cobalt.cli]`
- `grep -rn -F "from .cli import" src/cobalt/db_migrations` · 0 · `dev_rebuild.py:46:from .cli import _content_digest`; `grep -rn -F "import cobalt.cli" src` · 1 · nothing
- launcher · Read `ops/desk/desk-launch.sh` `:158-169` (IT REFUSES prodwrite), `:199` `REPO=`, `:201` `PROMPTS=`, `:1669-1805` the prodwrite arm (`:1732-1734` characters, `:1738-1749` verbs, `:1804` `prodw=`), `:1910` the fill
- authorize · Read `ops/desk/authorize.sh` whole: `:7-30` header, `:77-87` `row`, `:243-254` the prodwrite block
- tests · Read `tests/ops/test_desk_launch_prodwrite.py` (`:134` fixture, `:160` P1), `tests/ops/test_authorize.py:320-407` (`:325` `prodwrite_card`, `:343` r1, `:386` r3), `tests/ops/test_prodwrite_hub.py` (`:90`, `:133`, `:160`), `tests/cobalt/test_db_query.py:33-35`, `tests/cobalt/test_dev_rebuild_db.py:29-32`, `tests/cobalt/test_backup.py:197`
- hub · Read `PRODWRITE-HUB.md`: `:10` the line, `:16` NEVER, `:26` step (0), `:29` SHAPE, `:42-43` WRITE; `CARD.md:141-147`
- gitignore · Read `.gitignore:1-100`: `:22` `!docs/40 - DevDocs/**`, `:83` `*.sql`, `:92` `!src/cobalt/db_migrations/*.sql`

`wc -l` of the files the rows edit · 0
```
     101 pyproject.toml
    1147 src/cobalt/db_migrations/cli.py
     581 src/cobalt/cli.py
    1982 ops/desk/desk-launch.sh
     261 ops/desk/authorize.sh
     100 .gitignore
      54 docs/40 - DevDocs/prompts/PRODWRITE-HUB.md
     147 docs/40 - DevDocs/prompts/CARD.md
     321 tests/ops/test_desk_launch_prodwrite.py
     407 tests/ops/test_authorize.py
     166 tests/ops/test_prodwrite_hub.py
```
`tail -n 3` of the reports `## READ` names:
- `prodwrite-card-decisions-2026-10-12.md` → `` `prodwrite 392 2026-10-12 brain: D1-D7 KEEP; follow-up card cobalt db apply --prod <file.sql> (one transaction, backup checked, statements quoted in the approving row, DDL only if named) under K3/K5; a stopped write is a new card the desk launches itself` ``
- `db-apply-prod-decisions-2026-10-12.md` → `` `card 417 2026-10-12 brain: 1 2 3 6 7 KEEP (no --ddl flag); 4 CHANGE apply refuses all DDL, schema only by db migrate; 5 CHANGE constant BACKUP_MAX_AGE_S=900 in the verb, no tunable, no restart` ``

THE CARD'S RECORDS, copied and re-read where the list reaches: `db_query.py:163` `BEGIN READ ONLY` (re-read); `desk-launch.sh:1740`, `:1743`, `:1804` (re-read); `.gitignore:83` `*.sql` after `:22` (re-read); `jobs.yaml:88`, `:157`, `:201` read `pyproject.toml`, `:203` radar imports `cobalt.cli` (re-read); `cli.py:65` imports `db_migrations.cli` (re-read); `db.py:193-199` the one DSN (re-read); `dev_rebuild.py:46` (re-read); `jobs/store.py:120`, `:135`, `drc/store.py:501` (re-read); R1138 HIS RULING · APPROVED (AUTHORIZATION row). Not re-read: the `ls -l` link `/Users/cobalt/.claude/ops/desk-launch.sh` (no listed read of it needed) and the pglast/libpg_query facts (pinned by D-cases).

PROVEN BY FIRST REAL USE: `sh /Users/cobalt/cobalt/ops/desk/*` → used at AUTHORIZATION and here (exit 0 both). `uv run cobalt jobs restarts *` → used above (exit 0). The rest per BUILD-HUB's table.

## E0 BASELINE
On `8f1d11ed`.
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` · exit 0 → `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 683.84s (0:11:23)`
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` · exit 0 → `146 passed, 1 skipped, 15 warnings in 30.70s`; the one skip `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (no skip names `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Test files written (no `src/` edit): NEW `tests/cobalt/test_db_apply.py` (A1-A5), NEW `tests/cobalt/test_db_apply_db.py` (A4 T5, T6, T9), NEW `tests/ops/test_gitignore_apply_sql.py` (K4), and in `tests/ops/test_desk_launch_prodwrite.py` (K1: `write_card` gains `tail`; P4, P5, P6), `tests/ops/test_authorize.py` (K2: `prodwrite_card` gains `rows`, `tail` with defaults that keep its text byte-equal; R4, R5), `tests/ops/test_prodwrite_hub.py` (K3: S1-S4).

Rewritten once: `test_db_apply.py` first imported `from cobalt import db_apply`, whose red read `ImportError: cannot import name 'db_apply' from 'cobalt'`; changed to `import cobalt.db_apply as db_apply` so the red is the row's named one.

- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_db_apply.py tests/cobalt/test_db_apply_db.py` · exit 2 → `2 errors in 0.12s`; first lines:
  - `tests/cobalt/test_db_apply.py:22: in <module>` · `E   ModuleNotFoundError: No module named 'cobalt.db_apply'` (A1-A5 red, as named)
  - `tests/cobalt/test_db_apply_db.py:18: in <module>` · `E   ModuleNotFoundError: No module named 'cobalt.db_apply'` (A4 with-DB red, as named; raised at import, before any connection)
- `uv run pytest -q -p no:cacheprovider --color=no --tb=no -rf tests/ops/test_desk_launch_prodwrite.py tests/ops/test_authorize.py tests/ops/test_prodwrite_hub.py tests/ops/test_gitignore_apply_sql.py` · exit 1 → `16 failed, 93 passed, 15 warnings in 16.36s`; the 16:
  - P5 ×8 (`one byte off`, `absent`, `uncommitted`, `changed after commit`, `another hash`, `no prod`, `two blocks`, `no last newline`): each `assert 0 == 1` at `test_desk_launch_prodwrite.py:153`, the stderr holding `RUN: claude --bg …"Bash(COBALT_ENV=production uv run cobalt db apply --side user --prod --sha256 aef873b4… 2026-01-02/1-x-apply.sql)"…` (it launches: the row's red)
  - R4: `assert ['RULING 2026...2 R2 at HEAD'] == ['SQL FILE co...L CARD BLOCK']` (no SQL row printed)
  - R5 ×3: `assert 0 == 1` at `test_authorize.py:442`, stdout ending `AUTHORIZED`
  - S1: `AssertionError: SQL FILE committed` (absent from step (0)); S2: `assert '--sha256' in " — before any production call…`; S4: `assert '## SQL' in ' (the values `PRODWRITE-HUB.md` reads…`
  - G1: `assert 0 == 1` · `where 0 = check_ignore('docs/40 - DevDocs/prompts/2026-01-02/1-x-apply.sql')`
- Green on BASE as the card says (two-sided / negative controls): P4, P6, `test_r1_…` and `test_r3_…` (R6), S3, G2 ×5, and every existing test of the four files.

THE WITH-DB RED, one lock take (the lock was held by another worktree at 15:21; the take waited):
- `sh /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh db-apply-prod-1012 90` (background) · exit 0 → `lock taken: db-apply-prod-1012` · 15:38 EDT
- `ls -la /Users/cobalt/cobalt-wt/*/.env` · 0 → one line, `/Users/cobalt/cobalt-wt/db-apply-prod-1012/.env`
- `<FP>` · 0 → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` · 0 → `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`, `TABLES 0011`, `NOTHING WAS APPLIED` (= `## LEVEL 0013` of `gate-lists.md`); no forward
- `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_db_apply_db.py` · 2 → `tests/cobalt/test_db_apply_db.py:18: in <module>` · `E   ModuleNotFoundError: No module named 'cobalt.db_apply'` · `1 error in 0.08s`
- `<FP>` again · 0 → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = `<F0>`
- `sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh db-apply-prod-1012` · 0 → `lock released`; `ls /Users/cobalt/cobalt-wt/db-apply-prod-1012/.env` → `No such file or directory` · 15:39 EDT

## E3 THE ROWS
A1, first edit: `pyproject.toml:54` gained `    "pglast>=6,<7",` after `"psycopg[binary]>=3.3.2",`. The first `uv run` after it:
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_gitignore_apply_sql.py` · exit 1 → (verbatim, head and tail; the tool cut 4279 characters from the middle of the compiler log)
```
   Building cobalt-agent @ file:///Users/cobalt/cobalt-wt/db-apply-prod-1012
   Building pglast==6.16
      Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/db-apply-prod-1012
  × Failed to build `pglast==6.16`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit
      status: 1)
      …
      running build_ext
      compiling src/pg_query_deparse.c
      …
      subprocess.CalledProcessError: Command '['make', '-s', 'build']'
      returned non-zero exit status 2.

      hint: This usually indicates a problem with the package or the build
      environment.
  help: `pglast` (v6.16) was included because `cobalt-agent` (v0.1.0) depends
        on `pglast`
```
- `git diff uv.lock` (read 15:40 EDT): uv locked `pglast` `6.16` (sdist `pglast-6.16.tar.gz`, upload 2025-03-17) with ONE dependency, `setuptools` (`84.0.0`, also added), and wheels for `cp311`, `cp312` and `cp313` only: no `cp314` wheel.
- `ls /Users/cobalt/cobalt-wt/db-apply-prod-1012/.venv/lib` → `python3.14` (the first `uv run` at PREFLIGHT printed `Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14`).
- Undone with the Edit tool (the `pyproject.toml` line and the three `uv.lock` hunks): `git diff --stat` → nothing; `git status --short --branch` → `## ops/db-apply-prod-1012` and the untracked report only. Proof that the tree runs again: the same `uv run pytest … tests/ops/test_gitignore_apply_sql.py` · exit 1 → `1 failed, 5 passed` (G1, its BASE red; uv re-synced `Uninstalled 1 package … Installed 1 package`).

(The stop at 15:41 EDT; the run CONTINUED at 15:44 EDT on the re-pointed card `c3da69a1`, below.)

### E3 after CONTINUE (card `c3da69a1`)
Tests first, for the card's changed A1/A4 text: D7 now checks `PARSER_PG_MAJOR == 17`, the parser's `"version" // 10000 == 17` and `SERVER_PG_MAJOR == 16`. D8 is new: `test_each_admitted_kind_parses_to_its_top_node`, six kinds through `db_apply.parse`. T8's message is now `FAILED: server is Postgres 17, apply is proved for 16 — ROLLED BACK`. These reds are the file's import red, `ModuleNotFoundError: No module named 'cobalt.db_apply'` (`uv run pytest … tests/cobalt/test_db_apply.py` · exit 2 · `1 error in 0.10s`, 15:46 EDT).

A1: `pyproject.toml:54` `    "pglast>=7.11,<8",`. The first `uv run` (the run above) printed `Downloading pglast (1.4MiB)` · `Installed 2 packages in 2ms`, a wheel with no source build. `uv.lock:3642-3643` `name = "pglast"` · `version = "7.20"`, sdist `pglast-7.20.tar.gz` (upload `2026-10-02`), wheel `pglast-7.20-cp314-cp314-macosx_11_0_arm64` present (`uv.lock:3675`). The entry lists no `dependencies`. The installed `pglast/parser.pyi` gives `parse_sql_json(query: str) -> str` (`:41`) and `class ParseError(Error)` (`:17`).

New `src/cobalt/db_apply.py` (A1-A5); `src/cobalt/db_migrations/cli.py` `add_parser` registers `add_apply_parser(gsub)` beside `add_query_parser` (function-local import); `src/cobalt/cli.py:18` the usage line.
- `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/cobalt/test_db_apply.py` · 0 → `106 passed in 0.63s` (first run after the module)

THE MUTATIONS, A rows (each made with Edit, the row's tests alone, undone with Edit):
| row / rule | mutation | run | result, first failing line |
|---|---|---|---|
| A1 r1 | `if not writes:` → `if False:` | `-k test_d1` | `25 failed, 81 deselected`; `Failed: DID NOT RAISE <class 'cobalt.db_apply.ApplyRefused'>` (`SELECT set_config(…)` instead fails r4: `assert 'statement 1 refused: SelectStmt' in 'statement 1 refused: function set_config is not on the apply list'`) |
| A1 r4 | `name not in` → `name[-1:] not in` (last part only) | `-k pg_catalog.now` | `1 failed`; `Failed: DID NOT RAISE` |
| A1 r3 | `key == "intoClause"` → `"intoClause_"` | `-k "d5-0 or d5-1"` | `2 failed, 5 passed`; `Failed: DID NOT RAISE` |
| A1 re-parse | the equality check → `if False:` | whole file | `106 passed`: STAYED GREEN, so I wrote `test_d6_a_piece_that_does_not_reparse_to_its_checked_statement_is_refused` (a tree swapped for `DELETE FROM t`'s, through `_pieces`) → under the mutation `1 failed`, `Failed: DID NOT RAISE` at `test_db_apply.py:198` |
| A1 r2 | the nested-`…Stmt` check → `if False:` | whole file | `107 passed`: STAYED GREEN (the grammar nests no DDL under DML), so I wrote `test_r2_a_nested_statement_that_is_not_dml_is_refused` (a CTE's query swapped for `DROP TABLE t`, through `check_statement`) → `1 failed`, `Failed: DID NOT RAISE` at `test_db_apply.py:79` |
| A2 | `if got != sha256:` → `if False:` | `-k test_h1` | `1 failed`; `AssertionError: connected` (the stub: it reached the connection) |
| A3 | `age.total_seconds() > BACKUP_MAX_AGE_S` → `False` | `-k test_b3` | `1 failed`; `AssertionError: connected`, stdout `backup: newest snapshot 901 s old (bound 900 s)` |
| A4 prepare | `conn.execute(piece, prepare=True)` → `conn.execute(piece)` | `-k test_t` | `1 failed, 5 passed`; T7 `assert [] == ['UPDATE t SE... t SET a = 3']` |
| A4 rollback | the failure's `return 1` → `continue` | `-k test_t1` | `1 failed`; `assert 0 == 1`, stdout `… STATEMENT 3/3 … COMMITTED · statements: 3 · rows: 4` |
| A5 | `add_apply_parser(gsub)` removed | `-k test_v1` | `1 failed`; `argparse.ArgumentError: argument command: invalid choice: 'apply' (choose from migrate, dev-rebuild, query)` |
After the undo: `uv run pytest … tests/cobalt/test_db_apply.py tests/cobalt/test_db_query.py tests/cobalt/test_backup.py` · 0 → `140 passed in 0.52s`.

K rows:
- K4 `.gitignore` carve-out after `:92` (comment + `!docs/40 - DevDocs/prompts/20*/*-apply.sql`) → `tests/ops/test_gitignore_apply_sql.py` `6 passed`.
- K1 `ops/desk/desk-launch.sh`: the `db apply` block after the `--rollback`/`--down-to` loop, and the IT REFUSES comment. First run `3 failed, 42 passed`: `awk: syntax error … else close >>>  = <<<  $0` (`close` is an awk builtin). Renamed to `opener`/`closer` → `tests/ops/test_desk_launch_prodwrite.py` `45 passed`.
- K2 `ops/desk/authorize.sh`: the four `SQL` rows after `WRITE RULING`, and the header comment → `tests/ops/test_authorize.py` `41 passed`.
- K3 `PRODWRITE-HUB.md` step (0) and (1) SHAPE, `CARD.md` prodwrite section → `tests/ops/test_prodwrite_hub.py` `17 passed`. The launch line `:10` and the NEVER line `:16` are untouched.
- `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops` (background) · 0 → `3444 passed, 1 xfailed, 16 warnings in 666.80s (0:11:06)`.

THE MUTATIONS, K rows:
| row | mutation | run | result, first failing line |
|---|---|---|---|
| K1 | `"$v1 $v2" = "db apply"` → `"db applyX"` (the block never runs) | `-k "p4 or p5 or p6"` | `8 failed, 2 passed`: every P5 case; P4, P6 green |
| K2 | `= "db apply"` → `= "db applyX"` in `authorize.sh` | `-k "r4 or r5 or r1 or r3"` | `4 failed, 5 passed`: R4, R5 ×3; r1, r3 green |
| K3 | step (0) `SQL FILE committed` → `SQL FILE kommitted` | whole file | `1 failed, 16 passed`; `AssertionError: SQL FILE committed`. My first try, `committedX`, kept the substring and stayed green (`17 passed`), so it proved nothing; I redid it. |
| K4 | carve-out commented out | whole file | `1 failed, 5 passed`; `assert 0 == 1 … check_ignore('docs/40 - DevDocs/prompts/2026-01-02/1-x-apply.sql')` |
| K4 negative control | carve-out widened to `!*-apply.sql` | whole file | `2 failed, 4 passed`; G2 `assert 1 == 0 … check_ignore('docs/40 - DevDocs/reports/1-x-apply.sql')` and `'docs/00 - Project/x-apply.sql'` |
After every undo: `uv run pytest … tests/ops/test_prodwrite_hub.py tests/ops/test_gitignore_apply_sql.py tests/ops/test_authorize.py tests/ops/test_desk_launch_prodwrite.py tests/cobalt/test_db_apply.py` · 0 → `217 passed, 15 warnings in 15.13s`. `git diff --stat` shows the fix only.
- DevDocs: `cobalt/db_apply.md` (new page), `cobalt/cli.md` and `cobalt/db_migrations/cli.md`, one `## 2026-10-12 — db-apply-prod-1012` entry each.

(Superseded by the CONTINUE.) At the stop, no row was built. Rows A1–A5 all need the parser (A1 `check_file`, and A2–A5 call it or sit in the same module). K1–K4 do not need it, but the card orders A1 first, and building K alone would ship a launcher arm for a verb that does not exist.

## RESTARTS
E3 commit `81452495`. `uv run cobalt jobs restarts 8f1d11ed..HEAD` · 0:
```
path	change	rule	restart
.gitignore	M	META	-
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_apply.md	A	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/cli.md	M	DOCS	-
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/PRODWRITE-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/db-apply-prod-build-2026-10-12.md	M	DOCS	-
ops/desk/authorize.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
pyproject.toml	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/db_apply.py	A	static import reach	com.cobalt.radar
src/cobalt/db_migrations/cli.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_db_apply.py	A	test/documentation; no resident	-
tests/cobalt/test_db_apply_db.py	A	test/documentation; no resident	-
tests/ops/test_authorize.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prodwrite.py	M	test/documentation; no resident	-
tests/ops/test_gitignore_apply_sql.py	A	test/documentation; no resident	-
tests/ops/test_prodwrite_hub.py	M	test/documentation; no resident	-
uv.lock	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. This is R1's expected table: agent, aset and radar from `pyproject.toml`/`uv.lock`, and radar alone from the three `src/` modules.

## W THE THREE SUITES
`<tip>` = `81452495`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh db-apply-prod-1012 all --deploy` (background) · exit 1 · 16:00–16:11 EDT. Its verdict line: `RED (exit 1): 1 failed, 4306 passed, 803 skipped, 1 xfailed, 36 warnings in 634.92s (0:10:34)`, then `log: /Users/cobalt/cobalt-wt/.gate-logs/db-apply-prod-1012-all-20261012-160054.log`. The gate stopped at (a) OFFLINE; it took no lock (`ls …/db-apply-prod-1012/.env` → `No such file or directory`), so (b)–(f) and (e) did not run. `cobalt_dev` was not touched.

The one red (log `:117-126`): `tests/cobalt/test_jobs_restarts.py:473` · `test_backup_yaml_readers_are_pinned_and_derive_the_aset_restart` · `assert readers == EXPECTED_BACKUP_YAML_READERS` · `Extra items in the left set: 'cobalt.db_apply.command'`, `'cobalt.db_apply.backup_line'`. The test pins every function whose calls reach `load_backup_config` (L42; `EXPECTED_BACKUP_YAML_READERS` `:240-271`, entrypoints `:484-497`, referrers `:498-506`). Row A3 calls the loader by the card's own text (`load_backup_config()` as `backup/cli.py:59`), so the verb is a new reader. My E3 test runs never ran this file, so E2 and E3 did not show the red.

Not fixed. BUILD-HUB W says a red "fix it inside the rows' files only", and the card says "A red outside these rows: a `## DECISIONS` item … never fixed here". `tests/cobalt/test_jobs_restarts.py` is in no row's `files`. (Answered later by the card's row A6, built in `2de9afa9`.)

### W, second gate call (after rows A6 and A7), `<tip>` = `dfcf2097`
`sh /Users/cobalt/cobalt/ops/desk/gate.sh db-apply-prod-1012 all --deploy` (background) · exit 0 · 16:33–about 17:20 EDT. No `--deselect` (this build's with-DB tests run at 0013), no `--tickers` (they write no ticker), no `--migration`. The verdict lines, whole:
```
offline 4307/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5210/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/db-apply-prod-1012-all-20261012-163356.log
```
- (a) OFFLINE: log `:885` `4307 passed, 806 skipped, 1 xfailed, 36 warnings in 632.89s`. The tests this build adds: `tests/cobalt/test_db_apply.py` (108 offline, A1–A5) and the K-row tests in `tests/ops`; the six with-DB tests skip offline (log `:256-259`).
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:902`); `TABLES 0011` · `LEVEL 0013` (log `:952`, `:955`).
- (c) PASS 1, the executed command (log `:958`), whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py` → log `:1115` `5005 passed, 7 skipped, 99 deselected, 3 xfailed, 43 warnings in 774.55s` = `<d1>` 5005. The seven skips are quoted above; none is marked `OUTSIDE the allowed set`, and none is in `test_db_apply_db.py`. Pass 1 runs `-rs`, so it prints no PASSED lines: this build's six with-DB tests ran in it at 0013 (not deselected, not skipped, `0 failed`).
- (c2) `dev forward: APPLIED 16:57:49` (log `:1117`); `F1: 908 45 126f2d6983fa59f9d0eaaff7da7dd29c` (log `:1195`).
- (c3) PASS 2: log `:1969` `205 passed, 1 deselected, 5 warnings in 228.10s` = `<d2>` 205. `<d>` = 5005 + 205 = 5210 = the gate's `with-DB 5210/0`. This build deselected nothing.
- (c3r) `stray rows: not read (no --tickers given)`: this build's tests write no ticker. The scratch table is dropped in the fixture's `finally`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:2037`) = `<F0>` → **`cobalt_dev: 0013 — F2 = F0`**; `.env: removed`; `ls /Users/cobalt/cobalt-wt/db-apply-prod-1012/.env` → `No such file or directory`.
- (e) LIVE-NOTE: log `:2160` `146 passed, 1 skipped, 15 warnings in 25.84s` → `live-note 146/0`; the skip is `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`), not `COBALT_LIVE_VAULT_ROOT`.
- The log's code line reads `code: dfcf2097 (DIRTY: 1 path(s))` (log `:950`): the one path is this report, uncommitted until CLOSE.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED for its named reason against BASE or a mutation, and the two that stayed green were rewritten:
- E2 reds: A1–A5 `ModuleNotFoundError: No module named 'cobalt.db_apply'` (offline and with-DB); P5 ×8 launched (`assert 0 == 1`); R4 `assert ['RULING 2026...2 R2 at HEAD'] == ['SQL FILE co...L CARD BLOCK']`; R5 ×3 `AUTHORIZED`; S1, S2, S4 text absent; G1 `assert 0 == 1`.
- D7 and D8 (the card's re-point): red by the file's import, `ModuleNotFoundError: No module named 'cobalt.db_apply'` (15:46 EDT).
- E3 mutation reds: A1 r1, r2, r3, r4 and the re-parse fence; A2, A3, A4 prepare, A4 rollback, A5; K1, K2, K3, K4 and K4's negative control (the tables under `## E3 THE ROWS`). The two tests that stayed green under a mutation (r2 and the re-parse) were written and shown red.
- T5, T6, T9 (with-DB) were red at E2 by import. Their greens are the by-hand run at 16:32 (`PASSED` lines quoted under `## RECORDS`) and pass 1 (`0 failed`, `## W`). No mutation was run on them on `cobalt_dev`; T1 and T7 are their offline twins under the A4 mutations.
- A6: red is the first gate's `:473` line (`Extra items in the left set: 'cobalt.db_apply.command' 'cobalt.db_apply.backup_line'`), green `22 passed` (`## RECORDS`).
- A7: red under the no-allowlist mutation, `[a]` and `[b]` `assert 0 == 2` with `COMMITTED` in stdout, `[c]` green as its control. Green `6 passed` after the undo (`## RECORDS`).

(2) Entry paths pinned, callers by `grep` at the tip:
- `grep -rn -F "add_apply_parser(" src` → `db_migrations/cli.py:1134`, pinned by V1–V3.
- `grep -rn -F "check_file(" src` → `db_apply.py:281` (`command`), pinned by `test_a_refused_statement_is_refused_before_connecting` and H0.
- `grep -rn -F "apply_statements(" src tests` → `db_apply.py:290` (`command`), plus `test_db_apply.py:445` and `test_db_apply_db.py:53`.
- `command` → `db.connect` → `apply_statements` as one run is pinned by A7 (`test_command_end_to_end_…[a|b|c]`, with-DB on the real factory). At the tip, `grep -rn -F "check_file(" src` → `db_apply.py:172` (def), `:281` (`command`).
- The flags: `--prod` with and without (B1–B6, H0), `--side` and `--sha256` absent (V2), `--ddl` (V3).

(3) Every `file:line` re-read at the tip `81452495`: `grep -n -F "pglast" pyproject.toml` → `54`; `grep -n -F "cobalt db apply" src/cobalt/cli.py` → `18`; `grep -n -F -e "-apply.sql" .gitignore` → `94`, `95`; `grep -n -F "add_apply_parser" src/cobalt/db_migrations/cli.py` → `1131`, `1134`; `grep -n -F "db apply" ops/desk/desk-launch.sh ops/desk/authorize.sh` → launcher `169`, `1754-1784`, authorize `26`, `261`, `280`; `uv.lock:3642-3643`, `:3675` (Read/Grep after the sync). At `dfcf2097`: `grep -n -F "REAL_CONNECT" tests/cobalt/test_db_apply_db.py` → `30`, `63`, `71`, `117`; `grep -n -F "cobalt.db_apply" tests/cobalt/test_jobs_restarts.py` → `273`, `274`, `501`, `511`; the gate log's lines by `grep -n -F` (`:885`, `:902`, `:958`, `:1115`, `:1117`, `:1195`, `:1969`, `:2037`, `:2160`).

## FOR THE CHECK
- Range `8f1d11ed..dfcf2097`: `df558cb7` wip red (tests only); `870f94ca` wip E3 (pglast 6.16); `81452495` feat A1–A5, K1–K4; `2e0e7c82` wip W offline red; `2de9afa9` wip A6 + A7 written; `dfcf2097` fix A7 on the real factory (A6, A7).
- Per row: the reds, mutations and greens are under `## E2 RED`, `## E3 THE ROWS`, `## RECORDS` (A6, A7) and `## PRE-STOP SELF-CHECK` (1).
- RUN row R1: the table under `## RESTARTS` (and the A6/A7 path `tests/cobalt/test_jobs_restarts.py`, `test/documentation; no resident`), `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`.
- Suites: under `## W`, second gate call. F0/F1/F2 per take: E2 take `664 · 35 · 272c95bb…` = after. A7 take (16:32–16:33): F0 = after = `664 · 35 · 272c95bb…`. Gate: F0 `664 35 272c95bb…`, F1 `908 45 126f2d69…`, F2 = F0. Lock times: E2 15:38–15:39; A7 red attempt (prior session) 16:17–16:28; A7 16:32–16:33; gate 16:34 to its exit (`lock: waited 0 min`).
- For X1: with the allowlist removed, `cobalt_user` committed `DROP TABLE "user".zz_db_apply_scratch` on `cobalt_dev`. The cause is `0001_schemas.sql:103` `ALTER SCHEMA "user" OWNER TO cobalt_user`. So for the user side, A1 is the only DDL fence (`## DECISIONS` 1).
- Worth reading: T5, T6 and T9 as first committed (`81452495`) ran on the suite's savepoint proxy (`tests/cobalt/conftest.py:304-339`). Their "second connection" was the same session, and `commit` was a `RELEASE SAVEPOINT`. They now use `REAL_CONNECT`.

## CONTINUE
next: none. The build is closed; the desk verifies it and launches CHECK-HUB on card 417. (Prior session's note, done at 16:31–16:34:) A6 is done and A7's test is written (wip commit). The new session: (1) under one lock take, run `tests/cobalt/test_db_apply_db.py` with the mutation OFF and a `timeout`, to learn whether T5/T6/T9 hang (an in-process lock wait: a migration-connection DROP with no `lock_timeout` behind a `cobalt_app` connection); (2) A7's red under the `split_statements` mutation, then green; (3) a `fix(db-apply-prod-1012):` commit of A6 + A7, RESTARTS, the gate.

## DECISIONS
- DECISION 1 (ASK DESK, 17:20 EDT; not for Dejan): on the user side, A1's parse-tree allowlist is the ONLY fence against DDL. `src/cobalt/db_migrations/0001_schemas.sql:103` `ALTER SCHEMA "user" OWNER TO cobalt_user` makes the side role the schema's owner. As owner it may drop any table in `"user"`. The A7 mutation showed this: with the allowlist removed, `STATEMENT 1/1: DROP TABLE "user".zz_db_apply_scratch` · `ROWS 1: -1` · `COMMITTED`. The card's X1 asks whether any shape reaches the database as DDL, and the server would not refuse one. Safe default: nothing changed, since it is outside the rows (a schema/grant change is a migration card). The check should weigh A1 knowing there is no second fence. Whether `"user"`'s ownership should move off `cobalt_user` is a question for the brain.
- DECISION 2 (ASK DESK): A7's text says both "carries `@pytest.mark.timeout(120)`" and "`pytest-timeout` is no dependency … none is added: the 120 s fence … `command` run in a daemon `threading.Thread` joined for 120 s". Without the plugin, the mark does nothing (`pyproject.toml:99` registers only `integration`). Safe default: the thread fence only (`HANG_S = 120`, `test_db_apply_db.py`), and no mark that looks like a fence but does nothing.
- DECISION 3 (ASK DESK): A7 names (b)'s red as "a per-statement allowlist (check, run, check, run) leaves `qty` raised". In this verb a check inside `apply_statements` would raise inside the one transaction, and its `finally` would roll back. So `qty` would NOT stay raised, and the test would go red on a different line (the thread's carried `ApplyRefused`). The red I ran removes the allowlist from `command` (`check_file` → `split_statements`): (b) commits the UPDATE and the DROP and goes red at `assert 0 == 2`. Safe default: that mutation, quoted. (b) is red under both shapes.
- ANSWERED: DECISION W and DECISION A4/A5 below, by the card's rows A6 and A7 (`91986b0c`), built in `2de9afa9` and `dfcf2097`.
- DECISION W (ASK DESK, 16:12 EDT): the offline suite is red on one L42 pin, `tests/cobalt/test_jobs_restarts.py:473`. `cobalt.db_apply.command` and `cobalt.db_apply.backup_line` now reach `load_backup_config`. The fix is test-side only and changes no behaviour, but that file is in no row. It would add the two names to `EXPECTED_BACKUP_YAML_READERS` (`:240`), `cobalt.db_apply.command` to the expected entrypoints (`:484`, an operator command with no job, as `_status`), and `cobalt.db_apply.add_apply_parser` to the referrers (`:498`). A change to `configs/cobalt/backup.yaml` would still derive `com.cobalt.aset` alone: the verb is no resident. Safe default: not fixed. Asked: may this build add the three names to `tests/cobalt/test_jobs_restarts.py`, then rerun W?
- DECISION A4/A5 (ASK DESK): `command`'s path `db.connect` → `apply_statements` is not pinned as one run. Each half is pinned: the refusals before the connection by H/B, the transaction by T1–T9. Safe default: left as it is, named here. Pinning it means a test with `db.connect` returning the fake connection, plus one more gate call.
- ANSWERED: DECISION A1 below. The desk re-pointed the card (`c3da69a1`, brain R1251, desk R1255) to `pglast>=7.11,<8`; uv locked 7.20.
- DECISION A1 (ASK DESK, 15:41 EDT): the card's one dependency, `pglast>=6,<7`, cannot be installed into this repo's venv. Its newest 6.x, 6.16, has no CPython 3.14 wheel, and its source build fails (`make -s build` exit 2). The venv runs CPython 3.14.3. Every path forward lies outside the card, so the desk or brain must pick one: (a) run the venv on CPython 3.13, for which 6.16 has a wheel; (b) allow `pglast` 7, whose Postgres 17 grammar A4 refuses against the pg16 server unless `PARSER_PG_MAJOR` and A4 change; (c) find and fix the source-build failure (the cause is in the cut middle of the log, unread); (d) another parser (the card fences that out). Safe default taken: no row built, `pyproject.toml` and `uv.lock` back at BASE, the red tests committed, the run stopped here.

## RECORDS
- `.env: removed, proven gone (E2)` 15:39 EDT.
- One lock take at E2, 15:38–15:39 EDT (the A4 with-DB red); `<F0>` = `<F>` after = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`.
- L74: one system reminder asked for a `Claude-Session:` commit line; not acted on.
- The card's RECORDS as re-read at PREFLIGHT (see `## PREFLIGHT`). The card's RECORDS call the pglast facts UNPROVEN by a read. This build read the first of them, that the package installs: it does not install on this venv.
- tokens at stop: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh a44616ba` → `context 266702 of 400000 — ok`.
- CONTINUED at E3 15:44 EDT: the message from `cto-desk` read `CONTINUE: A1. Card 417 is re-pointed and committed on main (c3da69a1): pin pglast>=7.11,<8 …, PARSER_PG_MAJOR 17 beside SERVER_PG_MAJOR 16, new test D8 per statement kind.` I verified it myself. `authorize.sh build "<card>"` → `CARD COMMITTED … c3da69a17ed6fbcbe1bddd2246c19794e10d1e4a`, `CARD UNCHANGED … nothing`, `AUTHORIZED`. `git -C /Users/cobalt/cobalt log --oneline -3` → `c3da69a1 docs(desk): R1255 card 417 pglast 7.11 pin, build continues at A1`. I re-read the card whole: A1 (pin, the two majors, D7, D8), A4 (`SERVER_PG_MAJOR`, its message), NOT IN THIS JOB, X5 and RECORDS `:82-84` changed; every other row stands. The rows come from the committed card, not from the message.
- CONTINUED at W 16:16 EDT: `cto-desk` sent `CONTINUE: W. Card 417 now has rows A6 … and A7 …, committed on main as 91986b0c`. Verified: `authorize.sh build "<card>"` → `CARD COMMITTED … 91986b0c8d8084ee91c5e0e0b61bc64e262bcc2a`, `AUTHORIZED`; `git -C /Users/cobalt/cobalt diff --stat c3da69a1 91986b0c` → the card `3 ++` (rows A6 `:27`, A7 `:28`, read whole by `grep -n -F "| A6 |"` / `"| A7 |"`). DECISION W and DECISION A4/A5 are answered by those rows.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

- tokens at the W stop: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh a44616ba` → `context 386248 of 400000 — ok`. This is above the desk's 250,000 line (UNATTENDED RULES (c)).
- One gate call (16:00–16:11 EDT), red at offline, no lock taken.

- A6 (16:18 EDT): the three names added to `tests/cobalt/test_jobs_restarts.py` (`EXPECTED_BACKUP_YAML_READERS`, entrypoints, referrers) → `uv run pytest … tests/cobalt/test_jobs_restarts.py` · 0 → `22 passed in 12.83s`. Its red is the gate's `:473` line under `## W` (`Extra items in the left set: 'cobalt.db_apply.command' 'cobalt.db_apply.backup_line'`).
- A7 (16:19 EDT): `test_command_end_to_end_checks_the_whole_file_before_any_statement_runs` (a, b, c) added to `tests/cobalt/test_db_apply_db.py`. For its red, I mutated `command`'s `check_file(text)` to `split_statements(text)` (no allowlist). Lock taken 16:17 EDT (`lock taken: db-apply-prod-1012`). `COBALT_ENV=dev uv run pytest -q -rA … tests/cobalt/test_db_apply_db.py` printed `.` (one test passed) and then HUNG past 600 s (moved to the background). `pg_stat_activity` showed two other sessions on `cobalt_dev`, one `cobalt_app` and one `cobalt`, their queries `<insufficient privilege>` to my role. I stopped the run with TaskStop at about 16:28 EDT. Afterwards: `to_regclass('"user".zz_db_apply_scratch')` → empty, and `sessions` → `1` (mine). The fingerprint → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = `<F0>`. I undid the mutation with Edit (`git diff --stat` shows no `src/` path). `release-devdb-lock.sh` → `lock released`; `ls …/.env` → `No such file or directory` (16:28 EDT). So the hang held two connections of the test process itself: the superuser fixture and one `cobalt_app`. UNPROVEN which one waited on which: the run printed no traceback, and its first test is T5 or T6, written before A7. A7 has neither a red nor a green yet, and T5/T6/T9 must be re-run to learn whether they hang without the mutation.
- `.env: removed, proven gone (A7 red attempt)` 16:28 EDT; one extra lock take (16:17–16:28 EDT).
- tokens: `context 386248 of 400000` at 16:12 EDT, and more since. This is above the desk's 250,000 line: RECOVERY (c), a new session continues.

- CONTINUED at W 16:31 EDT (new session, RECOVERY (c)): `git status --short --branch` → `## ops/db-apply-prod-1012`; `git log --oneline -3` → `2de9afa9 wip(db-apply-prod-1012): W — A6 pin green, A7 test written; with-DB run hung, handed to a new session` first; `ls -la …/.env` → `No such file or directory`. The card's A7 CONTINUE asks a wip commit of A6/A7 first: it is `2de9afa9`, `git show --stat` → `db-apply-prod-build-2026-10-12.md | 10`, `tests/cobalt/test_db_apply_db.py | 46`, `tests/cobalt/test_jobs_restarts.py | 6`, `3 files changed, 60 insertions(+), 2 deletions(-)`.
- THE HANG, read from the code (16:35 EDT): `tests/cobalt/conftest.py:262-344` `dev_db_tx` is autouse and replaces `db.connect` with `fake_connect` (`:304`, `:338`), a `_SavepointConnection` over ONE real connection with `autocommit = False` (`:301`) whose `commit`/`close` are a `RELEASE SAVEPOINT`/no-op (`:249-259`) and which is rolled back only at the fixture's end (`:343`). The with-DB file's `rows()` and `apply()` called that patched `db.connect`, so their reads took locks on `"user".zz_db_apply_scratch` inside the suite's open transaction (one `cobalt_app` session); the `scratch` fixture's teardown `DROP TABLE` on the superuser connection (`connect_migration`, no `lock_timeout`) waited for that transaction, which ends only in `dev_db_tx`'s own teardown, after it: an in-process wait with no end. That matches the two sessions the prior run saw (one `cobalt_app`, one `cobalt`). The fix is in the test file only: every connection is the unpatched factory, `REAL_CONNECT = db.connect` bound at import (the `tests/cobalt/test_fill_transaction_db.py:27-30` precedent), A7 patches `db.connect` back to it for `command`, the fixture sets `lock_timeout = '30s'`, and A7 runs `command` in a daemon thread joined for 120 s. No `src/` change. `uv run pytest … tests/cobalt/test_db_apply_db.py tests/cobalt/test_db_apply.py` · 0 → `108 passed, 6 skipped in 0.44s` (offline: the six with-DB tests skip).
- LOCK TAKE (A7 red/green and T5/T6/T9 re-run), 16:32–16:33 EDT: `take-devdb-lock.sh db-apply-prod-1012 90` · 0 → `lock taken: db-apply-prod-1012`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, this worktree's. `<FP>` → `<F0>` `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` · 0 → `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`, `TABLES 0011`, `NOTHING WAS APPLIED` (the same level the E2 take read). No forward.
  - `COBALT_ENV=dev uv run pytest -q -rA … tests/cobalt/test_db_apply_db.py` (mutation off) · 0 → `6 passed in 0.26s`: `PASSED …::test_t5_…`, `…::test_t6_…`, `…::test_command_end_to_end_…[a]`, `[b]`, `[c]`, `…::test_t9_…`. No hang.
  - A7 MUTATION: `command`'s `statements = check_file(text)` → `split_statements(text)` (no allowlist) · `-k test_command_end_to_end` · 1 → `2 failed, 1 passed, 3 deselected in 0.15s`: `[a]` `test_db_apply_db.py:138: assert 0 == 2`, stdout `STATEMENT 1/1: DROP TABLE "user".zz_db_apply_scratch` · `ROWS 1: -1` · `COMMITTED · statements: 1 · rows: 0`; `[b]` the same line, stdout `STATEMENT 1/2: UPDATE … SET qty = qty + 1` · `ROWS 1: 3` · `STATEMENT 2/2: DROP TABLE …` · `ROWS 2: -1` · `COMMITTED · statements: 2 · rows: 3`; `[c]` PASSED (its negative control). Undone with Edit; `git diff --stat` → the report and `tests/cobalt/test_db_apply_db.py` only (no `src/` path). Re-run · 0 → `6 passed in 0.26s`.
  - `<FP>` again → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = `<F0>`. `release-devdb-lock.sh db-apply-prod-1012` · 0 → `lock released`; `ls …/.env` → `No such file or directory` (16:33 EDT).
- Commit `dfcf2097` `fix(db-apply-prod-1012): A7 end-to-end with-DB test on the real factory, 120 s thread fence; T5/T6/T9 off the suite proxy; A6 reader pin (A6, A7; L42, L45)`. RESTARTS re-run on `8f1d11ed..HEAD` · 0 → the table under `## RESTARTS` plus `tests/cobalt/test_jobs_restarts.py M test/documentation; no resident -`; last line `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`; no `UNCLASSIFIED`.
- W stop (prior session): A7's with-DB run hung on cobalt_dev (two in-process sessions; stopped, F = F0, lock released); context over the desk's line; handed to a new session at W.

- One extra lock take by hand, 16:32–16:33 EDT (A7 red and green, T5/T6/T9 re-run); `.env: removed, proven gone (W, A7)` 16:33 EDT. The gate's take: `lock: waited 0 min`, `.env: removed`.
- L74 (this session, 16:31 EDT): a system reminder asked commits to end with a `Claude-Session:` line. Not acted on: `dfcf2097` carries `Co-Authored-By` only.
- One more gate call (the second), green; `log: /Users/cobalt/cobalt-wt/.gate-logs/db-apply-prod-1012-all-20261012-163356.log`.
- No `src/` change in this session; the A7 mutation in `src/cobalt/db_apply.py` was made and undone with Edit and never committed.
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 56c65689` → `context 164307 of 400000 — ok`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: db-apply-prod-1012 · tip: dfcf2097 | on 8f1d11ed | migration: none | offline 4307/0 | with-DB 5210/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar | rows: 12 of 12 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 164307
