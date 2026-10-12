# Preflight — card 417 `db-apply-prod-1012` (read-only) — 2026-10-12

## §0 Headline
- Card 417 is committed (`15054887`), unchanged, one `«FILL` left (`BASE`), `CLASS: K3, K5`, R1138 is `HIS RULING · APPROVED`.
- Every brain direction is in the rows (no `--ddl`, no `DDL:`, no tunable, constant 900); no row touches the NEVER line; no allow line gains a string.
- 2 FAILS: the R1138 anchor is stale (`:103`, now `:106`); the statement rule (A1) lets DDL through three shapes the card does not test.
- Ready: NO. Fix A1 (X1 below) and the anchor, then BASE.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C … log -1 --format=%H -- <card>`; `git diff HEAD --stat -- <card>` | `15054887d27ba3877d7d0dc3b24c6d9072de1abb`; diff empty | OK |
| 2 | `grep -n "«FILL" <card>` | `7:BASE: «FILL: main HEAD at the build launch, 8 hex»` only. `TIP:` empty, `HOUSE B:` empty (build). `CHECK REPORT` filled: brain ask 7 KEEP, drafter decision 7 | OK |
| 3 | `grep -n "R1138" cto-2026-10-12.md` (HEAD = tree) | `106:\| R1138 \| 06:10 ET \| HIS RULING · APPROVED …`; card `RULINGS: 2026-10-12 R1138` | OK |
| 4 | `CLASS:` line | `CLASS: K3, K5` (card line 3) | OK |
| 5 | `grep -n -i -e "--ddl" -e "DDL:" -e "tunables.yaml" -e "backup_max_age_s"` | hits at lines 20 (A3: "no `tunables.yaml` row", the constant), 22 (A5: "there is no `--ddl` flag"; V3 `--ddl yes` → exit 2), 27 (R1: no tunable row), 32 (NOT IN THIS JOB), 34 (NOT IN THIS JOB: no `--ddl`, no `DDL:`), 60, 63, 65 (RECORDS). Every hit forbids or records; none adds a flag, header line or tunable. `db.apply.backup_max_age_s`: no hit | OK |
| 6 | A3 + B7 read | `BACKUP_MAX_AGE_S = 900` a module constant of `db_apply.py`; compared with `latest_snapshot_age(cfg).total_seconds()` (`restic.py:240-263`, the number `backup status` prints, `cli.py:70-71`); B7 pins 900 and no `load_tunables` | OK |
| 7 | A1 D1 read | named cases for CREATE, ALTER, DROP, TRUNCATE, GRANT, REVOKE, COMMENT, `FROBNICATE t` | OK |
| 8 | A1 D1 read | DDL hidden: after `--` comment, after `/* */` (lower case), after `;` (statement 2 named), `;/* x */drop table t` | OK |
| 9 | A4 T1, T5 read | T1 fake connection: 2nd of 3 raises → `FAILED at statement 2`, `ROLLED BACK`, no `STATEMENT 3/3`, no commit; T5 with-DB: second session sees every `qty` unchanged | OK |
| 10 | A2 H1 read | one byte changed after its hash → exit 2, `REFUSED: sha256`, never connected | OK |
| 11 | `git show`-equal reads (tree = HEAD: `git diff HEAD --stat -- src ops tests .gitignore configs/cobalt/jobs.yaml prompts` prints nothing) of every `file:line` of the code rows | hold: `db_query.py:20-28, 41-95, 118-125, 163, 195-198`; `db.py:160-199, 227-266, 272-275`; `env.py:73`; `db_migrations/cli.py:152, 163, 972, 1001, 1028-1066, 1130-1132`; `backup/cli.py:59, 62, 66-71`; `restic.py:51-52, 240-263, 254`; `src/cobalt/cli.py:65, 500` | OK |
| 12 | same, ops, docs, tests | hold: `desk-launch.sh:158-168, 1669-1805, 1732-1734, 1740, 1743, 1749, 1804, 1910`; `bare-guard.py:1099-1107`; `authorize.sh:7-30, 77-87, 243-254`; `PRODWRITE-HUB.md:10, 16, 25-26, 29, 34, 42-43`; `CARD.md:141-147`; `.gitignore:21-22, 73-82, 83, 92`; `jobs.yaml:67-99, 69, 193-204`; `restarts.py:133, 216-220, 225-246`; `BUILD-HUB.md:80`; test lines `test_db_query.py:33-35`, `test_backup.py:197`, `test_dev_rebuild_db.py:29-32`, `test_prodwrite_hub.py:90, 133, 160`, `test_authorize.py:325-340, 343, 386`, `test_desk_launch_prodwrite.py:134, 160` | OK |
| 13 | `cto-2026-10-12.md:103` (RECORDS last-but-two bullet) vs `grep -n` | R1138 is at `:106`; three rows (R1237-R1239) were added above it after the drafter's read | FAIL |
| 14 | counts pinned: `grep -rn` of `src/` for `cobalt.cli` | three docstring hits (`session/cli.py:166`, `cards/cli.py:280`, `archiver/store.py:46`): matches. `tunables.yaml` has only `:611 heartbeat.backup_max_age_min`: matches. Card's "no `src/` module imports `db_migrations.cli` but `cobalt.cli`" is wrong by one: `db_migrations/dev_rebuild.py:46 from .cli import _content_digest`; `dev_rebuild` is imported only by `cli.py` (function-local), so the RESTARTS conclusion stands | OK (NOTE 3) |
| 15 | NEVER line (`PRODWRITE-HUB.md:16`) vs rows | K3 leaves it unchanged; S3 pins `a production schema change`, no `DDL`, no `db apply` (read: line 16 holds neither) | OK |
| 16 | prodwrite arm `desk-launch.sh:1732-1749, 1804` | `COBALT_ENV=production uv run cobalt db apply --side user --prod --sha256 <hex> <date>/<nn>-<name>-apply.sql` holds no char of `:1733`, is none of `:1740`/`:1743`/`:1747`, is filled whole as `"Bash(<command>)"` at `:1804`, `:1910`; the hub's allow and deny lists name no `db apply`; no string added (R411/R412) | OK |
| 17 | `.gitignore` K4 + G1/G2 read | `*.sql` at `:83` after `!docs/40 - DevDocs/**` (`:22`); one negation `!docs/40 - DevDocs/prompts/20*/*-apply.sql` after `:92`; G1 exit 1, G2 five paths still ignored | OK |
| 18 | RESTARTS homes | `## RECORDS` `:65` and R1 row: `src/` three modules → radar via `cobalt.cli` (`jobs.yaml:203`), not aset (`:99`, nothing imports `cobalt.cli`); `.gitignore` META `:235-239`; `ops/desk/` `:230-234`; `docs/` `:225-229`; `tests/` `:245-246`. Result `com.cobalt.radar`, justified | OK (NOTE 4) |
| 19 | tests red on `BASE`, test text read | A1-A5, S, V: module absent / `invalid choice: 'apply'`; P5 each launches on `BASE`; R4/R5 print no `SQL` row and give `AUTHORIZED` on `BASE`; S1, S2, S4 text absent; G1 exit 0 on `BASE`. P4, P6, R6, S3, G2 are two-sided as stated | OK |
| 20 | drafters' decisions vs rows | draft 1-7 and re-point 1-3 each carry a default; rows agree (1 no `DB:` key, 2 required flags minus `--ddl`, 3 `## SQL` + sha, 4 no DDL, 5 constant, 6 carve-out, 7 `CHECK REPORT` filled; re-point 1 two refusal texts, 2 four `SQL` rows, 3 no aset restart) | OK |
| 21 | X1 on A1: `db_query.tokenize` (`:41-95`) read for what `apply` runs | DDL reaches the database in three shapes the card names no test for (ISSUES 1-3) | FAIL |

checks: 21 · fails: 2

## ISSUES
1. FAIL (X1, check 21): `WITH d AS (DELETE FROM t RETURNING a) SELECT a INTO u FROM d` is `dml` by A1 (`WITH` + a `DELETE` word) and creates table `u` (`SELECT … INTO` is CREATE TABLE AS). D3/D4 have no case. Fix: refuse the word `INTO` in any statement not led by `INSERT`, add the case to D4.
2. FAIL (X1, check 21): the function rule reads tokenized words and `tokenize` skips `"…"`, so `UPDATE t SET a = "set_config"('role', 'cobalt_system', false)` or `"pg_terminate_backend"(1)` carries no refused word (a quoted lower-case name is the same function). It can move the role after the `current_user` check. Fix: refuse a function name from a quoted identifier too (match the raw text of each `"…"`), add cases to D4.
3. FAIL (X1, check 21): `tokenize` treats `\'` as a closing quote, but an `E'…\'…'` string does not close there. `UPDATE t SET a = E'\''; DROP TABLE t; -- '` reads as ONE `dml` statement (the tokenizer's second quote spans `; DROP TABLE t; -- `), while Postgres runs the `UPDATE`, then `DROP TABLE t`. psycopg's no-parameter `execute` sends the simple protocol, which accepts several statements (the build must confirm). Fix: refuse an `E`/`e` string prefix or any `\` outside a comment, add the case to D4; or run each statement with `cursor.execute` and reject a result of more than one command.
4. FAIL (check 13): `cto-2026-10-12.md:103` is `:106`. Cite the row by id, or correct the line at the BASE fill.
5. NOTE 1: D5 says each statement is "byte-equal to its slice" without saying whether the slice holds the `;`; state it.
6. NOTE 2: `src/cobalt/cli.py:25` is the `backup` usage line; the `db` line to extend is `:17`.
7. NOTE 3: `deploy-2026-10-02-2.md:42` is the ops-glob check row; its src-derives-radar rows are `:121-122`. And `dev_rebuild.py:46` imports `db_migrations.cli` (check 14); neither changes `com.cobalt.radar`.
8. NOTE 4: the classes of `.gitignore`, `ops/desk/`, `docs/`, `tests/` sit in row R1, not in `## RECORDS`; `## RECORDS` names `src/` only.
9. NOTE 5: K1 and K2 each re-read the card's one command and the `## SQL` block in shell (two implementations, as card 392); the seat's own Read re-proof is the third. Accepted by precedent, not a fail.

PREFLIGHT DONE · card: db-apply-prod-1012 · checks: 21 · fails: 2 · ready: NO
