# The code behind round-1 BLOCKER 1 — `--allow-prod` decides the database, `COBALT_ENV` does not

Read by the CTO desk directly from the tree at 2026-09-19 13:4x ET. Quotes are verbatim; line numbers are given for both trees because the deploy runs from `/Users/cobalt/cobalt` (main) and the gate runs from a worktree carrying `sprint-2/p4`.

## 1. `cmd_migrate` picks the database from the FLAG

`src/cobalt/db_migrations/cli.py` — **line 542 on `sprint-2/p4`, line 537 on main**:

```python
dbname = db.PROD_DB_NAME if args.allow_prod else env.resolve_db_name()
```

`env.resolve_db_name()` is the only place `COBALT_ENV` is consulted, and it is on the ELSE branch. When `--allow-prod` is present the environment variable is never read for this decision. The connections that follow carry the same flag:

```
cli.py:548 (main :543)   conn = _connect(dbname, allow_prod=args.allow_prod, read_only=True)    # the --proof-only path
cli.py:559 (main :554)   conn = _connect(dbname, allow_prod=args.allow_prod, read_only=False)   # the read-write path
cli.py:486 (main :481)   conn = db.connect_migration(dbname, allow_prod=allow_prod)
```

## 2. The production gate only fires when the flag is ABSENT

`src/cobalt/db.py:144-157`, verbatim:

```python
def _prod_gate(dbname: str, allow_prod: bool) -> None:
    """RULING 7: `cobalt_brain` needs a production declaration."""
    if dbname == PROD_DB_NAME and not allow_prod:
        try:
            declared_production = env.is_production()
        except env.EnvConfigError:
            declared_production = False  # unset is definitively not production
        if not declared_production:
            raise DbConfigError(
                f"Refusing to connect to production database '{PROD_DB_NAME}': "
                f"this process has not declared {env.ENV_VAR}={env.PRODUCTION} "
                "(NN#16 / RULING 7). Pass allow_prod=True only from migration "
                "tooling that must reach prod deliberately."
            )
```

`_prod_gate` is called from both `connect` (`db.py:259`) and `connect_migration` (`db.py:289`). With `allow_prod=True` the `if` is false and the function returns immediately: **there is no `COBALT_ENV` check anywhere on the `--allow-prod` path.** The docstring is honest about it — the flag is the deliberate escape hatch for migration tooling.

## 3. Therefore

`COBALT_ENV=dev uv run cobalt db migrate --allow-prod --rollback --down-to 0007` connects to `cobalt_brain` — **production** — and reverses migrations there, despite the `dev` prefix. The previous launch line's rule `Bash(COBALT_ENV=dev uv run cobalt db migrate*)` matched that string, so the file's own claim that "a production schema rollback cannot be typed" was false.

**The fold:** that wildcard is removed. The dev lane is now three exact strings with no `*` —

```
Bash(COBALT_ENV=dev uv run cobalt db migrate --proof-only)
Bash(COBALT_ENV=dev uv run cobalt db migrate)
Bash(COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0009)
```

— which are exactly the three commands §1.4 (b), (c) and (f) type, and the only `--allow-prod` rules in the line are `Bash(COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only)` (read-only) and `Bash(COBALT_ENV=production uv run cobalt db migrate --allow-prod)` (the forward apply, bare).

## 4. The residual question this does NOT answer

Whether an UNSTARRED allowlist rule matches by PREFIX on this host. If `Bash(COBALT_ENV=production uv run cobalt db migrate --allow-prod)` matched `… --allow-prod --rollback --down-to 0007`, the hole would still be open through that rule. Round 1 marked this `UNVERIFIABLE FROM READS` and named the experiment: a scratch session allowlisting `Bash(echo hi)`, then typing `echo hi there` — expect DENIED. The string is byte-identical to the one Dejan approved for deploy 1 (R7) which ran clean this morning; the prompt forbids typing any longer spelling of it.
