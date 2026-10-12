# Preflight round 2 — card 417 `db-apply-prod-1012` (read-only) — 2026-10-12

## §0 Headline
- Card 417 is committed (`779d6d55`), unchanged, with one `«FILL` left (`BASE`). `CLASS: K3, K5`. No `--ddl`, `DDL:` or tunable. The NEVER line is unchanged. No allow string is added.
- Round 1's FAIL 1-3 and the stale cite are fixed in the rows, and each has a named test.
- 2 FAILS: (a) my own attack finds a statement the rule PASSES: dynamic SQL through `query_to_xml('select set_config(…)')`, because the function name sits in a literal; (b) "backslash in a comment" has no test.
- Ready: NO.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git log -1 --format=%H -- <card>`; `git diff HEAD --stat -- <card>`; `rev-parse HEAD` | `779d6d55b2d3…`; diff empty; HEAD is the same commit: card committed, unchanged | OK |
| 2 | `grep -n "«FILL" <card>` | `7:BASE: «FILL: main HEAD at the build launch, 8 hex»` only | OK |
| 3 | header read | `CLASS: K3, K5` (line 3); `RULINGS: 2026-10-12 R1138` | OK |
| 4 | `grep -o -i` for `--ddl`, `DDL:`, `tunables`, `BACKUP_MAX_AGE`, `load_tunables` | hits only at lines 20, 22, 27, 32, 34, 60, 63, 65. Each forbids or records: V3 `--ddl yes` → exit 2; NOT IN THIS JOB; B7 pins no `load_tunables`. No flag, header line or tunable added | OK |
| 5 | A3 read | `BACKUP_MAX_AGE_S = 900`, a module constant; compared with `latest_snapshot_age(cfg).total_seconds()`; B7 pins 900 | OK |
| 6 | K3 / S3 read; brain `db-apply-prod-decisions` ask 4 | NEVER line (`PRODWRITE-HUB.md:16`) unchanged, pinned by S3 (`a production schema change`, no `DDL`, no `db apply`) | OK |
| 7 | K1 read | "NO string is added to any line"; the fill is today's `"Bash(<command>)"`. K2, K3 add rows and text only. No new seat command | OK |
| 8 | `git diff HEAD --stat -- src ops tests .gitignore configs/cobalt/jobs.yaml`; `git diff --stat f7bea558 HEAD -- src ops tests .gitignore configs` | both print nothing: every `file:line` cited at the amend still holds at HEAD | OK |
| 9 | `src/cobalt/db_query.py` read `:18-126`, `:160-199` | `REFUSED_FUNCTIONS` `:25-28`; `tokenize` `:41-95` (`--` to `\n` `:52-55`, `/*` to first `*/` `:56-61`, quotes with doubling only `:62-75`, ASCII tag `:77`, ASCII word `:89`); function rule `:118-125`; `BEGIN READ ONLY` `:163`; `current_user` `:167-169`; `:195-198`. All as cited | OK |
| 10 | `.gitignore` read; `grep` of `cli.py` | `*.sql` `:83` after `!docs/40 - DevDocs/**` `:22`; `:92` is the last carve-out; the new `!docs/40 - DevDocs/prompts/20*/*-apply.sql` goes after it. `src/cobalt/cli.py:17` is the `db migrate` line, `:65` imports `db_migrations.cli` | OK |
| 11 | K4 G1/G2 read | G1 exit 1 for `…/2026-01-02/1-x-apply.sql`, RED on `BASE` (exit 0); G2 five paths stay ignored (`1-x.sql`, `cobalt_brain.sql`, `reports/…-apply.sql`, `docs/00 - Project/x-apply.sql`, `bars-dump-1.sql`) | OK |
| 12 | `grep -rn` of `src/` for imports of `db_migrations.cli`, `cobalt.cli`, `dev_rebuild`; `jobs.yaml` `grep` | `dev_rebuild.py:46 from .cli import _content_digest`; `dev_rebuild` imported only at `cli.py:619`, `:996` (function-local). Nothing imports `cobalt.cli`. aset `imports: [cobalt.aset.__main__, cobalt.aset.web]` (`jobs.yaml:99`); radar `imports: [cobalt.cli]` (`:203`) | OK |
| 13 | RESTARTS classes: `grep` of `restarts.py` | `.gitignore` → `REPO_META` `:28`, `:235-239`; `ops/desk/` → operator script `:230-234`; `docs/` → `DOCS` `:225-229`; `tests/` → test/documentation `:245-246`. All are named in the card's `## RECORDS` (line 73). New `src/` modules reach only `cobalt.cli`: `com.cobalt.radar`, not the aset | OK |
| 14 | `grep -o` of the card for `cto-2026-10-12.md` and `R1138` (stale cite, round 1 check 13) | `cto-2026-10-12.md` appears once, line 62: "R1138 is the row `R1138` of `cto-2026-10-12.md` (cited by id…)". No line number. R1138 is at `cto-2026-10-12.md:108` now | OK |
| 15 | FAIL 1 rows: D4 | `WITH d AS (DELETE … RETURNING a) SELECT a INTO u FROM d`, `WITH … INSERT INTO u SELECT …`, `WITH … RETURNING 1 AS insert) SELECT insert INTO u FROM d`, each named. Old rule (`WITH` + a DML word = `dml`) passes all three, so each is RED. The INTO rule needs INTO as the SECOND word after a first `INSERT`/`MERGE`: it refuses all three and passes `MERGE INTO` (D3). A plain `SELECT insert INTO u` is refused by the first-word rule | OK |
| 16 | FAIL 2 rows: D4 | `"set_config"('role', …)`, `"pg_terminate_backend"(1)`, `pg_catalog."SET_CONFIG"(…)`, `"pg_advisory_lock"(1)`, and `'"' AND "set_config"(…) = '"'`. The old tokenizer skips `"…"`, so each is RED. The raw lower-case substring test refuses all five | OK |
| 17 | FAIL 3 rows: D4 | `UPDATE t SET a = E'\''; DROP TABLE t; -- '` and `UPDATE t SET a = 'C:\x'`; t2 refuses any backslash before the split | OK |
| 18 | t2 text: "a backslash anywhere … comments included" vs D4 cases | the only backslash cases are inside a string literal (`E'\''`, `'C:\x'`). No case puts a backslash in a `--` or `/* */` comment. A build that skips comments in t2 passes every named test | FAIL |
| 19 | RECORDS line 70 and each hole's test | names: comment marks in strings (D3 pass), `--` in a quoted identifier (D3 pass), `$$…$$` and `$tag$…$tag$` (D3 pass), `$é$` (D4), `aé$b$` (D4), `\r` (D4), nested `/* /* */` (D4), `U&"…"` and `U&"!…" UESCAPE` (D4), `E'…'` (D4). Every hole found has a test. `U&'…'` (t3's `'` half) has no case: NOTE 1 | OK |
| 20 | amend's 3 decisions vs rows | 1: INTO rule, default as drafted, rows agree (D3 `MERGE INTO`, D4 `WITH … INSERT INTO`). 2: text rule t2, default as drafted, rows agree. 3: whole-ASCII fail-closed, default stated; t1 matches (NOTE 2, a narrowing) | OK |
| 21 | A4 vs `db_query.py:164-166` | apply sets `lock_timeout` only; the read path also sets `statement_timeout`. NOTE 3 | OK |
| 22 | ATTACK on the rule text, 8 statements | see below; 1 PASSES | FAIL |
| 23 | drafter's A2-A5, K1-K4 untouched | amend report lists changes to A1, D3-D5, A5 usage line, R1 cites, RECORDS only; K1-K4 text matches round 1's reads | OK |

### Attack (check 22): statements Postgres runs, read against A1's rules
| # | statement | verdict |
|---|---|---|
| 1 | `UPDATE t SET a = query_to_xml('select set_config(''role'', ''cobalt_system'', false)', true, true, '')::text` | PASSES. First word `UPDATE` is `dml`; no `INTO`; the words `QUERY_TO_XML`, `TRUE`, … match no refused function; the name `set_config` is inside a literal, which `tokenize` skips; `"set_config"` is not quoted. Postgres runs the inner SELECT through SPI (read-only mode still allows a volatile function), so a role or session setting changes, after the `current_user` check. `pg_terminate_backend(1)`, `pg_advisory_lock(1)` and `lo_import(…)` pass the same way |
| 2 | `WITH x AS (SELECT 1) SELECT * INTO u FROM x` | REFUSED (`WITH` holds no DML word: "writes nothing"; also the INTO rule) |
| 3 | `INSERT INTO t SELECT a INTO u FROM s` | REFUSED (INTO rule: the second INTO is not the second word) |
| 4 | `UPDATE t SET a = 1; COMMIT` | REFUSED (statement 2, first word `COMMIT` is `other`) |
| 5 | `UPDATE t SET a = 1 /* x */ ; /* y */ SET ROLE postgres` | REFUSED (statement 2 is `other`; comments hide nothing) |
| 6 | `UPDATE t SET a = pg_catalog.set_config('role', 'x', false)` | REFUSED (function rule: word `SET_CONFIG`) |
| 7 | `DELETE FROM t WHERE a = 1 \; DROP TABLE t` | REFUSED (t2, backslash) |
| 8 | `EXPLAIN ANALYZE DELETE FROM t` | REFUSED (`other`). Outside the four categories: `UPDATE t SET a = pg_sleep_for('1 hour')::text` PASSES (only `pg_sleep` is in `REFUSED_FUNCTIONS`); a stall, not DDL, a role change, a second command or a commit: NOTE 3 |

## ISSUES
1. FAIL (check 22, attack 1): the function rule reads tokenized words and the raw `"name"` form; a function that runs SQL held in a string (`query_to_xml`, `query_to_xml_and_xmlschema`, `query_to_xmlschema`, `cursor_to_xml`, `table_to_xml*`, `database_to_xml*`, `schema_to_xml*`) hides `set_config`, `pg_terminate_backend`, `pg_advisory_*`, `lo_*` in a literal. Fix: refuse those words (any word ending `_to_xml`, `_to_xml_and_xmlschema` or `_to_xmlschema`) in A1, and add the `query_to_xml('select set_config(…)')` case to D4. Postgres's read-only SPI run of a volatile function is from its documented behavior, UNPROVEN here (no database run).
2. FAIL (check 18): t2 says a backslash in a comment is refused, and no D4 case has one. Add `UPDATE t SET a = 1 -- \` and `UPDATE t SET a = 1 /* \ */`.
3. NOTE 1: t3's `'` half (`U&'…'`) has no D4 case; add `UPDATE t SET a = U&'x'`.
4. NOTE 2 (decision 3): t1 narrows apply to printable ASCII, tab and newline: a write carrying accented or other non-ASCII data is refused. Stated as a narrowing, default whole-ASCII fail-closed.
5. NOTE 3: A4 sets no `statement_timeout` (`db_query.py:164-166` does on the read path); `pg_sleep_for` or a long UPDATE holds the transaction and its locks until it ends. Consider `SET LOCAL statement_timeout` in A4, or add `pg_sleep_for`/`pg_sleep_until` to the refused names.
6. NOTE 4: round 1 NOTE 5 stands (K1/K2 shell re-reads plus the seat's Read re-proof); accepted by precedent.

PREFLIGHT DONE · card: db-apply-prod-1012 · checks: 23 · fails: 2 · ready: NO
