## 11. THE APPROVAL LIST — regenerated after round 1 of the house check (2026-09-19 13:30 ET)

`38`'s launch line now carries **55 `Bash(...)` rules**. **32 are byte-identical to `02-deploy-stack-3.md`'s line** (approved R7 07:49 ET, ran clean to `STACK DEPLOY DONE 2893a7f`), as are `--disallowedTools "AskUserQuestion" "EnterWorktree"` and `--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt-wt`. **23 strings differ** — each verified `grep -c -F` = 0 in `02`, = 1 in `38`. These are what Dejan approves, verbatim:

```
Bash(git -C /Users/cobalt/cobalt tag scratch-allow-probe-p4-0919)
Bash(git -C /Users/cobalt/cobalt tag -d scratch-allow-probe-p4-0919)
Bash(git -C /Users/cobalt/cobalt tag pre-p4-0919)
Bash(git -C /Users/cobalt/cobalt tag deploy-2026-09-19b)
Bash(git -C /Users/cobalt/cobalt merge --ff-only sprint-2/p4)
Bash(git -C /Users/cobalt/cobalt-wt/s2-p4 rebase main)
Bash(git -C /Users/cobalt/cobalt-wt/s2-p4 rebase --abort)
Bash(git -C /Users/cobalt/cobalt worktree add -b stack/deploy2-0919 /Users/cobalt/cobalt-wt/stack-deploy2-0919 main)
Bash(git -C /Users/cobalt/cobalt-wt/stack-deploy2-0919 merge --no-edit *)
Bash(git -C /Users/cobalt/cobalt-wt/stack-deploy2-0919 merge --abort)
Bash(cd *)
Bash(uv run pytest *)
Bash(COBALT_ENV=dev uv run pytest *)
Bash(COBALT_ENV=dev uv run cobalt db migrate --proof-only)
Bash(COBALT_ENV=dev uv run cobalt db migrate)
Bash(COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0009)
Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stack-deploy2-0919/.env)
Bash(rm /Users/cobalt/cobalt-wt/stack-deploy2-0919/.env)
Bash(COBALT_ENV=production uv run cobalt jobs register)
Bash(COBALT_ENV=production uv run cobalt jobs restarts *)
Bash(COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only)
Bash(launchctl bootout gui/501/com.cobalt.replay)
Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.replay.plist)
```

| string | class | why |
|---|---|---|
| the four `tag` rules | **NARROWED** (replaces `02`'s `Bash(git -C /Users/cobalt/cobalt tag *)`) | round-1 finding 5: the wildcard could tag or delete any ref; these are the only four tag commands this run types |
| `merge --ff-only sprint-2/p4` | RENAME | the branch that lands |
| the two `s2-p4 rebase` rules | RENAME | P4's worktree replaces `s2-p2-cards` |
| `worktree add -b stack/deploy2-0919 …` | **NARROWED NEW** | the L68 gate worktree; the exact command, no `*` |
| the two stack `merge` rules | NEW | the three merges that build the stacked tree, path-scoped to the gate worktree |
| `cd *` | NEW HERE | pytest needs a cwd; approved in `13` / `24b` / `25` / `35` |
| `uv run pytest *`, `COBALT_ENV=dev uv run pytest *` | NEW HERE | the gate's two suites; R18 disclosed the dev one as REUSED from `13` |
| the **three exact** `COBALT_ENV=dev … db migrate` rules | **NARROWED NEW — round-1 BLOCKER 1** | the wildcard `Bash(COBALT_ENV=dev uv run cobalt db migrate*)` also matched `… --allow-prod --rollback --down-to 0007`, and `--allow-prod` beats `COBALT_ENV`: `src/cobalt/db_migrations/cli.py:542` (main `:537`) `dbname = db.PROD_DB_NAME if args.allow_prod else env.resolve_db_name()`, with `src/cobalt/db.py:146` `_prod_gate` refusing ONLY when `allow_prod` is false. The three exact strings close it |
| the `cp` / `rm` `.env` pair | NEW PATH | R18 approved this shape for two other worktrees; this path is new |
| `jobs register`, `jobs restarts *` | **NARROWED** (replaces `02`'s `Bash(COBALT_ENV=production uv run cobalt jobs *)`) | round-1 finding 5: `cobalt jobs run <label> -- <cmd>` exists (`src/cobalt/jobs/cli.py:189`) and the wildcard would have wrapped any command under a production prefix |
| `db migrate --allow-prod --proof-only` | NEW HERE | the read-only production preflight; the EXACT line R7 part (1) approved for `03-prod-proof-only-3.md` |
| `launchctl bootout gui/501/com.cobalt.replay` | **NEW — round-1 finding 3** | §8 must be able to UNLOAD the new job: `src/cobalt/replay` arrives with P4 and is absent from main, so a job left armed after a revert fires against a tree with no `replay` module on Monday 21:10 ET |
| `launchctl bootstrap gui/501 …/com.cobalt.replay.plist` | NEW | the job's first install (L55) |

**REMOVED from `02`'s approved line** (each verified `grep -c -F` = 0 in `38`): the six `settings load` strings (no `trader_settings` write; cards live since 12:30 ET and the dark file must be unreachable), `mkdir -p …/pre-stack-0919/daymode-settings-rollback` (no rollback directory), `radar evaluate --replay *` (not established read-only with cards enabled), plus the two wildcards narrowed above (`tag *`, `jobs *`).

**Still open, the desk's to settle, NOT a rule change:** whether an UNSTARRED rule matches by prefix on this host — if `Bash(COBALT_ENV=production uv run cobalt db migrate --allow-prod)` did, it would admit the production rollback on its own. That string is byte-identical to the one approved and run this morning; round 1 marked the question `UNVERIFIABLE FROM READS` with a named experiment (a scratch session allowlisting `Bash(echo hi)`, then typing `echo hi there`; expect DENIED).

## 12. What this packet could NOT establish
