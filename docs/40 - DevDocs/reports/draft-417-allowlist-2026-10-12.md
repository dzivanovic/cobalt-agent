# Draft — card 417 allowlist redesign — 2026-10-12

## §0 Headline
- Card 417 is edited in place and uncommitted. `«FILL` is only at `BASE`. 34673 → 42834 bytes (`wc -c`): the A1 parse-tree rules and their test cases.
- A1 is now an allowlist on a pglast parse tree. Tops: INSERT, UPDATE, DELETE, MERGE, or a SELECT with a writing CTE. Every `FuncCall` must be in `ALLOWED_FUNCTIONS = {("now",)}`. `intoClause` is refused, and so is any other `*Stmt`. Every word and tokenizer rule is removed, and every old hole is a red D5 case.
- A4 opens with `statement_timeout '60s'` and `lock_timeout '5s'`, checks that the server major is 16, and sends each piece with `prepare=True` (one command per execute). New tests T7-T9.
- pglast is a NEW dependency (`>=6,<7`). Because of it, RESTARTS is not none: agent, aset and radar all read `uv.lock`.
- Next: the desk reads the decisions, commits the card, then preflight round 3.

## DECISIONS
1. ASK DESK: pin `pglast>=6,<7` (the Postgres 16 grammar, which matches `docker-compose.yml:4` pg16). The repo venv is Python 3.14. Whether a pglast 6 wheel exists for 3.14 is UNPROVEN here. Default: as pinned. If the sync cannot install it, the build stops `FAILED`, with no fallback to 7.x. [15:08]
2. ASK DESK: the new dependency changes `uv.lock` and `pyproject.toml`. `jobs.yaml:88-89`, `:157-158` and `:201-202` therefore derive `com.cobalt.agent`, `com.cobalt.aset` and `com.cobalt.radar`. Brain ask 5's "no aset restart" was about the tunable, and the constant still restarts nothing. Default: take the three restarts at deploy. [15:08]
3. ASK DESK: a file may still hold several statements, all in one transaction, so T1, T5 and T6 stand. I read "a second statement is refused" as a second command inside one executed piece. Two things close that: A1's re-parse of each piece alone, and A4's `prepare=True`, which T9 proves on `cobalt_dev`. Alternative: one statement per file. Default: several. [15:08]
4. ASK DESK: text rules t1-t4 are removed, including the whole-ASCII rule. Non-ASCII data now passes (D3 `'é'`). The round-2 backslash-in-comment cases and `'C:\x'` are dropped together with the backslash rule. `U&'x'` is now a D3 pass. Default: removed. [15:08]
5. ASK DESK: `ALLOWED_FUNCTIONS` has one entry, `now`, used by `updated_at = now()` (`jobs/store.py:120`). Names are matched by their full tuple, so `pg_catalog.now()` is REFUSED. Default: as drafted. [15:08]
6. ASK DESK: a top `SELECT` passes only when a CTE writes. `WITH x AS (SELECT 1) SELECT * FROM x` stays refused. `WITH … INSERT INTO u SELECT …` moves from refused to passing, because the tree reads it correctly. Default: as drafted. [15:08]
7. ASK DESK: no seat allow line carries `uv add` or `uv lock`. The build edits `pyproject.toml`, and its first `uv run pytest` re-locks and syncs. This needs network access in the build sandbox, which is UNPROVEN. Default: as drafted. [15:08]

## RECORDS
- Reads 14:58-15:07 EDT, `main` HEAD `38bca339`. `git status --short` of `src ops tests .gitignore configs pyproject.toml uv.lock` and the prompts folder shows only `configs/cobalt/rules.yaml`, which no row cites.
- Inputs read whole and left unchanged: card 417, `db-apply-prod-preflight-2026-10-12.md`, `db-apply-prod-preflight-r2-2026-10-12.md`, `draft-417-amend-2026-10-12.md`, `db-apply-prod-decisions-2026-10-12.md`.
- No parser in `pyproject.toml`/`uv.lock` (`grep`). Cites checked: `pyproject.toml:53`, `:6`; `.venv/lib/python3.14`; `docker-compose.yml:4`.
- psycopg 3.3.2: `_preparing.py:63-76`, `_cursor_base.py:283-290`, `:455-458`, `:564-576`, `_queries.py:69-71`; `db.py:199` (no `prepare_threshold`).
- `db_query.py:164-166` statement timeout; `db_migrations/cli.py:152` `DEFAULT_LOCK_TIMEOUT_S = 30`.
- RESTARTS: `jobs.yaml` labels `:39` aset, `:127` agent, `:193` radar, each with `pyproject.toml`/`uv.lock` in `reads:`; `restarts.py:207-210` resident reads, `:216-220`, `:225-246` classes.
- The card's `## RECORDS` (last bullets) carries every changed `file:line`, the UNPROVEN pglast/Postgres facts (each pinned by a RED-able test), and 8 hostile statements with the rule that refuses each: `query_to_xml(…)` r4; `E'\''; DROP` r1; `U&"\0073et_config"` r4; `SELECT … INTO` r3; nested `/* */` DROP r1; `pg_sleep` r4 plus the timeout; `; COMMIT` r1; `dblink` in FROM r4.
- Kept: the one-transaction rollback tests (T1, T5), sha256 mismatch (H1), the NEVER line unchanged (K3/S3), the `.gitignore` carve-out (K4), K1/K2. A2, A5 and K1-K4 are untouched.
- No commit, no launch, no database.

DRAFTED · decisions: 7
