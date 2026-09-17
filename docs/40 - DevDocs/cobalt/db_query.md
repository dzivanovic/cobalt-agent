# `src/cobalt/db_query.py`

Implements `cobalt db query`: a quote/comment-aware SELECT-only guard plus a server-side read-only transaction, timeout, role assertion, row limit, and unconditional rollback. All connections use `cobalt.db.connect`.

---

## 2026-09-17 — S2-P4: the read path, shared with `cobalt smoke`

The body of `command` moved into two functions. `cobalt smoke` (STEP-9) reads through them, so there is still one read path (L3).

- `read_rows(statement, *, side, prod, limit=1000) -> QueryRows`:
  - Runs the guard, then a `BEGIN READ ONLY` transaction with `SET LOCAL statement_timeout` (`db.query.timeout_s`).
  - Asserts `current_user` equals the side role, wraps the statement as `SELECT * FROM (…) AS q LIMIT %s`, and always rolls back and closes.
  - Before any connection opens, it raises `QueryRefused` for a statement off the allowlist and for `cobalt_brain` without `prod=True`.
- `QueryRows` is a frozen Pydantic value: `columns` (tuple) and `rows` (list of tuples).
- `hand_command(statement, *, side, prod)` returns the shell line that runs the same statement by hand: `uv run cobalt db query --side <side> [--prod] --format json '<statement>'`, shell-quoted. A smoke report prints it per check, and `shlex.split(line)[-1]` is the exact statement that ran.
- `command` keeps its behaviour and messages. A refused token or `cobalt_brain` without `--prod` exits 2 before connecting. Output is unchanged, as table or JSON.

Because the statement is wrapped with a `%s` limit parameter, a statement must not contain a literal `%`. The committed smoke SQL uses none.

