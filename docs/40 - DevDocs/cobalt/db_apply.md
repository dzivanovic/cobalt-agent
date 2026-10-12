# `src/cobalt/db_apply.py`

Implements `cobalt db apply --side {user,system} [--prod] --sha256 <hex> <date>/<nn>-<name>-apply.sql`: one approved DML file, run in one transaction on the side's own role. All connections use `cobalt.db.connect`. Every refusal is `REFUSED: … — nothing opened` on stderr, exit 2.

---

## 2026-10-12 — db-apply-prod-1012 (card 417)

New module. The order is A2, A1, A3, A4:

- **A2, the file.** The argument matches `<date>/<nn>-<name>-apply.sql` and resolves under `PROMPTS_ROOT` (`CODE_ROOT/docs/40 - DevDocs/prompts`). The bytes are read once, their sha256 must equal `--sha256` (64 lower-case hex), and they must decode as strict UTF-8.
- **A1, the statements.** `check_file(text)` is the one entry. It parses with pglast (libpg_query, the Postgres 17 grammar, `PARSER_PG_MAJOR = 17`), splits on the parser's byte offsets, and re-parses each piece alone to the same tree. Each statement must pass every rule:
  - (r1) the top node is `InsertStmt`, `UpdateStmt`, `DeleteStmt` or `MergeStmt`, or a `SelectStmt` whose CTE writes;
  - (r2) every nested `…Stmt` node is one of those or a `SelectStmt`;
  - (r3) no `intoClause` appears;
  - (r4) every `FuncCall`, by its full name, is in `ALLOWED_FUNCTIONS = {("now",)}`.
- **A3, the backup.** Only with `--prod`: `COBALT_ENV=production`, a database dump armed, and the newest snapshot no older than `BACKUP_MAX_AGE_S = 900`. Without `--prod` it prints `backup: not checked (not --prod)`.
- **A4, the transaction.** `apply_statements(conn, statements, *, side)` sets `SET LOCAL statement_timeout = '60s'` and `lock_timeout = '5s'`. It requires the server major to equal `SERVER_PG_MAJOR = 16` and `current_user` to be the side role. It then sends each piece with `prepare=True` (the extended protocol, one command per piece), printing `STATEMENT i/n` before it and `ROWS i` after it. After the last piece it commits and prints `COMMITTED · statements · rows`. Any failure prints `FAILED at statement i: … — ROLLED BACK` and exits 1.

## 2026-10-12 — check of db-apply-prod-1012 (O1, O2)

- `parse` refuses a text holding a NUL byte (`does not parse: the text holds a NUL byte`). The parser reads a C string, so a NUL ended the checked text while the piece kept the bytes after it.
- `apply_statements` also ends a failure of the preamble (`FAILED before statement 1: … — ROLLED BACK`) or of the commit (`FAILED at commit: … — ROLLED BACK`, e.g. a deferred constraint) in one line and exit 1, never a traceback.
