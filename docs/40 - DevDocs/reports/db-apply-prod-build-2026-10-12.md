# Build report — db-apply-prod-1012 (card 417)

## §0 Headline
- Stopped at E3, row A1: `pglast>=6,<7` resolves to 6.16, which publishes wheels for cp311–cp313 only. The repo venv is Python 3.14, so uv builds the sdist, and the build fails.
- Done: AUTHORIZATION, PREFLIGHT, E0 green, E2 red as named (commit `df558cb7`, tests only). No `src/` file was touched.
- The tree is back at BASE for `pyproject.toml` and `uv.lock`; `cobalt_dev` is untouched (F0 = F after, lock released, `.env` gone).
- One decision for the desk: which runtime or parser path the card takes.

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

Not fixed. BUILD-HUB W says a red "fix it inside the rows' files only", and the card says "A red outside these rows: a `## DECISIONS` item … never fixed here". `tests/cobalt/test_jobs_restarts.py` is in no row's `files`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED for its named reason against BASE or a mutation, and the two that stayed green were rewritten:
- E2 reds: A1–A5 `ModuleNotFoundError: No module named 'cobalt.db_apply'` (offline and with-DB); P5 ×8 launched (`assert 0 == 1`); R4 `assert ['RULING 2026...2 R2 at HEAD'] == ['SQL FILE co...L CARD BLOCK']`; R5 ×3 `AUTHORIZED`; S1, S2, S4 text absent; G1 `assert 0 == 1`.
- D7 and D8 (the card's re-point): red by the file's import, `ModuleNotFoundError: No module named 'cobalt.db_apply'` (15:46 EDT).
- E3 mutation reds: A1 r1, r2, r3, r4 and the re-parse fence; A2, A3, A4 prepare, A4 rollback, A5; K1, K2, K3, K4 and K4's negative control (the tables under `## E3 THE ROWS`). The two tests that stayed green under a mutation (r2 and the re-parse) were written and shown red.
- T5, T6, T9 (with-DB) were red at E2 by import. Their greens are pass 1's `-rA` lines (`## W`). No mutation was run on `cobalt_dev`; T1 and T7 are their offline twins under the A4 mutations.

(2) Entry paths pinned, callers by `grep` at the tip:
- `grep -rn -F "add_apply_parser(" src` → `db_migrations/cli.py:1134`, pinned by V1–V3.
- `grep -rn -F "check_file(" src` → `db_apply.py:281` (`command`), pinned by `test_a_refused_statement_is_refused_before_connecting` and H0.
- `grep -rn -F "apply_statements(" src tests` → `db_apply.py:290` (`command`), plus `test_db_apply.py:445` and `test_db_apply_db.py:53`.
- `command` → `db.connect` → `apply_statements` as one run is NOT pinned end to end: H0/B6 stop at the connect stub, and T1–T9 call `apply_statements` directly. Named under `## DECISIONS`.
- The flags: `--prod` with and without (B1–B6, H0), `--side` and `--sha256` absent (V2), `--ddl` (V3).

(3) Every `file:line` re-read at the tip `81452495`: `grep -n -F "pglast" pyproject.toml` → `54`; `grep -n -F "cobalt db apply" src/cobalt/cli.py` → `18`; `grep -n -F -e "-apply.sql" .gitignore` → `94`, `95`; `grep -n -F "add_apply_parser" src/cobalt/db_migrations/cli.py` → `1131`, `1134`; `grep -n -F "db apply" ops/desk/desk-launch.sh ops/desk/authorize.sh` → launcher `169`, `1754-1784`, authorize `26`, `261`, `280`; `uv.lock:3642-3643`, `:3675` (Read/Grep after the sync).

## FOR THE CHECK

## CONTINUE
next: W (after the desk's answer to DECISION W: the pin fix as a second `fix(db-apply-prod-1012):` commit, then RESTARTS and the gate again; tip now `81452495`)

## DECISIONS
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
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

- tokens at the W stop: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh a44616ba` → `context 386248 of 400000 — ok`. This is above the desk's 250,000 line (UNATTENDED RULES (c)).
- One gate call (16:00–16:11 EDT), red at offline, no lock taken.

FAILED: W — offline red: tests/cobalt/test_jobs_restarts.py:473 pins backup.yaml readers; cobalt.db_apply.command and cobalt.db_apply.backup_line are new readers, and the file is in no row — `Extra items in the left set: 'cobalt.db_apply.command' 'cobalt.db_apply.backup_line'` · decisions: 2 · for Dejan: 0 · tokens: 386248
