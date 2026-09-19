# The APPROVAL LIST — every rule string in `38-deploy-p4.md`'s launch line that differs from `02-deploy-stack-3.md`'s approved line

`02-deploy-stack-3.md`'s launch line was approved by Dejan this morning (R7, 07:49 ET) and ran to `STACK DEPLOY DONE 2893a7f`. `38-deploy-p4.md` reuses it. The desk verified with `grep -c -F` that **36 strings are byte-identical in both files** (all `git -C * …` reads, the `add`/`commit`/`reset --soft`/`tag`/`revert` rules, the production `validate`/`jobs`/`backup`/`db query`/`heartbeat` rules, the bare `db migrate --allow-prod`, the four aset/radar `launchctl` rules plus `print` and both `kickstart`s, `curl`, `shasum`, `grep`, `tail`, `ls`, `wc`, `date`, `--disallowedTools "AskUserQuestion" "EnterWorktree"`, `--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt-wt`).

**14 strings differ. Each was checked `grep -c -F` = 0 in `02-deploy-stack-3.md` and = 1 in `38-deploy-p4.md`.** These are what Dejan approves.

| # | string (verbatim) | class | why it is there | which step uses it |
|---|---|---|---|---|
| 1 | `Bash(git -C /Users/cobalt/cobalt merge --ff-only sprint-2/p4)` | RENAME | the branch that lands changed from `sprint-2/stack` | §4.3 |
| 2 | `Bash(git -C /Users/cobalt/cobalt-wt/s2-p4 rebase main)` | RENAME | P4's worktree replaces `s2-p2-cards` | §4.1 |
| 3 | `Bash(git -C /Users/cobalt/cobalt-wt/s2-p4 rebase --abort)` | RENAME | same, the abort half | §4.1 |
| 4 | `Bash(git -C /Users/cobalt/cobalt worktree add *)` | NEW | L68's gate needs a throwaway worktree for the stacked branch | §1.2 |
| 5 | `Bash(git -C /Users/cobalt/cobalt-wt/stack-deploy2-0919 merge --no-edit *)` | NEW | the three ordinary merges that build the stacked tree | §1.2 |
| 6 | `Bash(git -C /Users/cobalt/cobalt-wt/stack-deploy2-0919 merge --abort)` | NEW | the abort half of the same | §1.2 |
| 7 | `Bash(cd *)` | NEW HERE | pytest needs a cwd; already approved in `13-p4-verify.md` / `24b` / `25` / `35` launch lines | §1.3, §1.4, §1.5 |
| 8 | `Bash(uv run pytest *)` | NEW HERE | the gate's OFFLINE suite, run only inside a worktree; approved in `13` / `24b` / `35` | §1.3 |
| 9 | `Bash(COBALT_ENV=dev uv run pytest *)` | NEW HERE | the gate's with-DB suite; R18 (11:33 ET) disclosed this string as REUSED from `13`'s approved line | §1.4 (d) |
| 10 | `Bash(COBALT_ENV=dev uv run cobalt db migrate*)` | NEW HERE | the gate's `--proof-only` state reads, its forward apply and its `--rollback --down-to 0009` restore, all on `cobalt_dev`; same R18 disclosure | §1.4 (b)(c)(f) |
| 11 | `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stack-deploy2-0919/.env)` | NEW PATH | R18 approved this exact SHAPE for two other worktrees (`ops-2026-09-19`, `archiver-append`); this path is new and therefore needs its own word | §1.4 (a) |
| 12 | `Bash(rm /Users/cobalt/cobalt-wt/stack-deploy2-0919/.env)` | NEW PATH | the cleanup half of the same | §1.4 (g) |
| 13 | `Bash(COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only)` | NEW HERE | the read-only production preflight probe; this is the EXACT line R7 part (1) approved this morning for `03-prod-proof-only-3.md`, which ran three times read-only | §0 P13 |
| 14 | `Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.replay.plist)` | NEW | P4 ships a new scheduled job; L55 requires Code to install and prove every scheduled job it ships | §5.3 |

## DROPPED from `02`'s approved line (verified `grep -c -F` = 0 in `38`)

| string(s) | why dropped |
|---|---|
| the SIX `Bash(COBALT_ENV=production uv run cobalt settings load …)` strings (`--from …daymode-settings-0918` ×2, `--from …pre-stack-0919/daymode-settings-rollback` ×2, `--card …p2-dark-settings.yaml` ×2) | this deploy writes NO `trader_settings` row. Cards went LIVE at 12:30:01 ET today (R20) and the dark file must never be reachable from a P4 deploy session — dropping the strings makes "the rollback cannot turn cards dark" a property of the allowlist, not of the prose. |
| `Bash(mkdir -p /Users/cobalt/cobalt/data/backups/pre-stack-0919/daymode-settings-rollback)` | no settings file is loaded, so no rollback DIRECTORY is built. The rollback point is the tag `pre-p4-0919`. |
| `Bash(COBALT_ENV=production uv run cobalt radar evaluate --replay *)` | `02` used it as P2's DARK proof. With `radar.cards_enabled = true` the desk could not establish from reads that a replay stays read-only, so the command is not typed at all rather than typed hopefully. |

## Not added, deliberately — name it if you think the prompt needs it

`git branch -D` / `git worktree remove` (the gate branch and worktree are left on disk for the desk to clean), any `push`, any `--force`/`-f`, `git reset` in any spelling, `COBALT_ENV=production … --allow-prod --rollback`/`--down-to` (so a production schema rollback cannot be typed), `pytest` with `/Users/cobalt/cobalt` as cwd (WHY 2: `~/cobalt/.env` points it at `cobalt_dev`), `cat`/`less`/anything that could print `.env`.
