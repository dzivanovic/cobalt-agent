# Preflight round 3 — card 417 `db-apply-prod-1012` (read-only) — 2026-10-12

## §0 Headline
- Card 417 is committed (`4a1f4a2e` = HEAD) and unchanged. `BASE` is the only `«FILL`. `CLASS: K3, K5`.
- The allowlist redesign matches the brain's three additions. Every old hole is a RED case on the new classifier, and each allowlist edge has a test.
- My attack on the rule text found no harmful PASS. Two harmless PASSES are NOTES.
- 0 FAILs. Ready: YES. Two UNPROVEN items (decisions 1 and 7) are NOTES.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git log -1 --format=%h -- <card>`; `git diff HEAD --stat -- <card>`; `rev-parse --short HEAD` | `4a1f4a2e`; diff empty; HEAD `4a1f4a2e`: committed, unchanged | OK |
| 2 | `grep -n "«FILL" <card>` | `7:BASE: «FILL: main HEAD at the build launch, 8 hex»` only | OK |
| 3 | header read | `CLASS: K3, K5` (line 3); `RULINGS: 2026-10-12 R1138` | OK |
| 4 | `grep -n -E "--ddl\|DDL:"` | hits only at line 22 (A5: "there is no `--ddl` flag", V3 `--ddl yes` → exit 2) and line 35 (NOT IN THIS JOB). No flag, header line or tunable | OK |
| 5 | A3 read; B7 | `BACKUP_MAX_AGE_S = 900` module constant, compared with `age.total_seconds()`; B7 pins 900 and no `load_tunables` | OK |
| 6 | K3 read; `PRODWRITE-HUB.md:16` | NEVER line unchanged and still holds `a production schema change`; S3 pins it | OK |
| 7 | K1 read | "NO string is added to any line"; the fill stays `"Bash(<command>)"`. No new seat command | OK |
| 8 | `.gitignore` carve-out K4 and tests | `!docs/40 - DevDocs/prompts/20*/*-apply.sql` after `:92`; `tests/ops/test_gitignore_apply_sql.py` G1 (tracked) and G2 (five paths ignored) | OK |
| 9 | rollback and hash tests | T1 (second statement raises: rollback, no commit), T5 (second connection reads `qty` unchanged); H1 (one byte off → `REFUSED: sha256`, never connected) | OK |
| 10 | `git diff --stat 4a1f4a2e HEAD -- src ops tests .gitignore configs/cobalt/jobs.yaml pyproject.toml uv.lock` | prints nothing: the cites still hold | OK |
| 11 | brain's three additions vs card A1/A4 (quoted below) | each matches; see "Brain additions" | OK |
| 12 | every round-1/round-2 hole as a RED test (D5) | `SELECT … INTO` (two cases, r3); quoted `"set_config"` (r4); `E'\''; DROP TABLE t; -- '` (r1, statement 2 `DropStmt`); `query_to_xml('select set_config(…)')` (r4); plus `$é$`, `aé$b$`, `\r`, nested `/* /* */`, `U&"…"`, `U&"!…" UESCAPE`, `; COMMIT` | OK |
| 13 | allowlist edges D4 | pass: `now()` in SET, `now()` in VALUES and RETURNING. Refused, each naming the function: `upper` in a sub-select, `lower` inside `COALESCE`, `set_config` in a CTE, `pg_terminate_backend` in RETURNING, `pg_catalog.now`, `pg_sleep`, `dblink` in FROM. Every edge named in the task has a case (see NOTE 3 on "nested call") | OK |
| 14 | removed rules and tests: `grep -o` of the card for `tokenize`, `REFUSED_WORDS`, `t1`-`t4`, `backslash`, `ASCII`, `word rule` | A1 and D-cases say they are gone ("DROPPED with the backslash rule (t2)", "the whole-ASCII rule is gone", "no word list, no `tokenize`"); NOT IN THIS JOB lines 33-34 forbid them. No row asks the build to implement or test them. Round-1/2 RECORDS bullets (lines 66-72) still describe them, and line 76 says they "no longer bind a row" (NOTE 4) | OK |
| 15 | `pglast` pin; `grep -n -i pglast pyproject.toml` | not in `pyproject.toml` yet; A1 adds `"pglast>=6,<7",` after `psycopg[binary]>=3.3.2` (`:53`) and `uv.lock` gains its pin at the first `uv run pytest`; NOT IN THIS JOB forbids any other version or dependency | OK |
| 16 | RESTARTS: `grep -n` of `jobs.yaml`, `restarts.py` | `pyproject.toml` and `uv.lock` in `reads:` at `:88-89` (aset, label `:39`), `:157-158` (agent, `:127`), `:201-202` (radar, `:193`); `restarts.py:210` "resident reads". All match the card's cites. The class home is named in `## RECORDS` line 80 (resident reads, `restarts.py:207-210`) beside line 75 (the `.gitignore`, `ops/desk/`, `docs/` and `tests/` classes) | OK |
| 17 | the card's RESTARTS statement | the card has no header `RESTARTS:` key. R1 states the expected `com.cobalt.agent`, `com.cobalt.aset`, `com.cobalt.radar` and tells the build to write the line. Same as rounds 1-2 | OK |
| 18 | drafter's 7 decisions vs rows | 1 pin → A1 pin. 2 three restarts → R1. 3 several statements → T1/T5/T6, A1 re-parse, A4 `prepare=True`, T9. 4 text rules removed → D3 `'é'`, DROPPED list. 5 one entry `now` → D7 and r4. 6 top `SELECT` passes only with a writing CTE → D1 `WITH x AS (SELECT 1) SELECT …` refused, D3 `WITH … INSERT` passes. 7 uv sync → A1 "re-locks and syncs". Each has a stated default. Rows agree | OK |
| 19 | decision 1: pglast 6 wheel for Python 3.14 | UNPROVEN (the venv is 3.14, `pyproject.toml:6` `>=3.11`; no lock entry yet). NOTE 1 | OK |
| 20 | decision 7: network in the build sandbox for the re-lock | UNPROVEN. NOTE 2 | OK |
| 21 | ATTACK on the rule text, 10 statements | see below; 8 REFUSED, 2 PASS harmless | OK |

### Brain additions, quoted against the card
- Brain (R1243): "allowlist on a Postgres parse tree: top node INSERT/UPDATE/DELETE/MERGE or a WITH of those". Card r1: "the node is `InsertStmt`, `UpdateStmt`, `DeleteStmt` or `MergeStmt`, or a `SelectStmt` with a `withClause` at least one of whose CTEs is one of those four; any other top → `ApplyRefused(…)`". Match.
- Brain: "every FuncCall on a named list; literals never parsed". Card r4: "every `FuncCall` node anywhere … in `ALLOWED_FUNCTIONS = frozenset({("now",)})`"; "A string literal is an `A_Const`, data, never parsed for calls". Match.
- Brain: "`SET LOCAL statement_timeout = '60s'` and `lock_timeout = '5s'`; side role only". Card A4: "first `SET LOCAL statement_timeout = '60s'` then `SET LOCAL lock_timeout = '5s'` (module constants `STATEMENT_TIMEOUT = "60s"`, `LOCK_TIMEOUT = "5s"`)"; "`SELECT current_user` must be `side.role` … never a superuser"; never `connect_migration`. Match. T7 pins the call order.

### Attack (check 21): statements Postgres runs, read against r1-r4
| # | statement | verdict |
|---|---|---|
| 1 | `DO $$ BEGIN … END $$` | REFUSED r1: top `DoStmt` |
| 2 | `COPY t TO PROGRAM 'x'` (and `COPY (UPDATE … RETURNING …) TO PROGRAM`) | REFUSED r1: top `CopyStmt`; the inner UPDATE sits under a refused top |
| 3 | `INSERT INTO t VALUES (1) ON CONFLICT (a) DO UPDATE SET a = nextval('s')` | REFUSED r4: `FuncCall` `nextval` (the walk is "anywhere", ON CONFLICT included) |
| 4 | `UPDATE t SET a = 1 FROM pg_sleep(1)` | REFUSED r4: `FuncCall` `pg_sleep` in FROM (a `RangeFunction`) |
| 5 | `DELETE FROM t USING generate_series(1, 3) g WHERE …` | REFUSED r4: `FuncCall` `generate_series` |
| 6 | `WITH x AS (SELECT * FROM t FOR UPDATE) UPDATE u SET a = 1 FROM x` | PASSES. r1 top `UpdateStmt`; r2 allows `SelectStmt`; no `FuncCall`. It takes row locks that end with the transaction, bounded by `lock_timeout` 5 s and `statement_timeout` 60 s: harmless. A top `SELECT … FOR UPDATE` with no writing CTE is REFUSED r1. NOTE 5 |
| 7 | `WITH x AS (TABLE t) DELETE FROM u USING x …`, `WITH x AS (VALUES (1)) INSERT INTO t SELECT * FROM x` | PASSES. `TABLE` and `VALUES` are `SelectStmt` nodes with no `FuncCall` and no `intoClause`: reads only, harmless |
| 8 | `EXECUTE p`, `PREPARE p AS DELETE FROM t` | REFUSED r1: top `ExecuteStmt` / `PrepareStmt` |
| 9 | `SET ROLE cobalt_system`, `LOCK TABLE t IN ACCESS EXCLUSIVE MODE` | REFUSED r1: `VariableSetStmt` / `LockStmt` (D1 holds `SET ROLE`, `RESET ROLE`, `BEGIN`, `COMMIT`; no test names `LOCK` or `PREPARE`: NOTE 6) |
| 10 | `UPDATE t SET a = 1 RETURNING (SELECT set_config('role', 'x', false))` and `SELECT … INTO` nested in a CTE | REFUSED r4 (`set_config`, in RETURNING through a sub-select) and r3 (`intoClause` anywhere) |

## ISSUES
1. NOTE 1 (decision 1, UNPROVEN): no check here shows a `pglast` 6.x wheel for Python 3.14. If the sync cannot install it, the build stops: `pglast` is the only pinned range, "no version outside `>=6,<7`" (NOT IN THIS JOB, line 34), so `uv run pytest` fails and the red is a `## DECISIONS` item, never a fallback to 7.x (line 36). Not a FAIL.
2. NOTE 2 (decision 7, UNPROVEN): the re-lock needs network access in the build sandbox. If it is absent, `uv run pytest` cannot sync and the build records a `## DECISIONS` item (UNPROVEN, L70) and ships nothing. The drafter's default (no seat allow line for `uv add`/`uv lock`) is as stated. Not a FAIL.
3. NOTE 3: D4's "nested call" cases are a call in a sub-select (`upper`) and a call inside an expression (`COALESCE(lower(…))`). No case puts a call inside the argument of another call, and none can add a case the allowlist reaches: the only allowed name, `now`, takes no argument, so an inner call is always checked on its own `FuncCall`. Optional case: `UPDATE t SET a = abs(pg_sleep(1))`.
4. NOTE 4: `## RECORDS` lines 66-72 and 67's "Result: `com.cobalt.radar` and not `com.cobalt.aset`" are round-1 text; lines 76 and 80 mark them superseded. They bind no row. Left as history.
5. NOTE 5: attack 6 (a `FOR UPDATE` in a CTE under a writing statement) passes; the locks last to the transaction's end and are bounded by the two timeouts. Triggers, rules and operators the side role did not create run only what a migration created (RECORDS line 82, UNPROVEN beyond the grammar's node names).
6. NOTE 6: D1 has no case for `LOCK TABLE`, `PREPARE` or `EXECUTE`; r1 refuses each as a top node other than the four. Optional cases.

PREFLIGHT DONE · card: db-apply-prod-1012 · checks: 21 · fails: 0 · ready: YES
