# Stack gate — 2026-09-18

Seat: `stack-gate-0918`, Opus 5 (`claude-opus-5`), background, worktree `/Users/cobalt/cobalt-wt/s2-p2-cards` (`sprint-2/cards`).
Prompt: `docs/40 - DevDocs/prompts/2026-09-18/09-stack-gate.md` (committed `34524c1`). Supersedes `07-p2-integrate.md`.

## §0 Headline (14:36 ET)

- Run started. Authorization verified rule-by-rule against `cto-2026-09-18.md` §4 R1 list (1), R2, R7 — every rule in the launch line maps to a committed row; no rule is unaccounted for.
- PREFLIGHT: 5 probes, 0 denied.
- Preconditions PASS: tree clean, `<old-tip>` = `976528f`, `<n>` = **34** commits above main (`34524c1`), the 8 ops-0918 commits `fe195ab..856176e` confirmed, main's 8 reverts confirmed.
- ESCALATE: 0.

---

## AUTHORIZATION (verified by this hub, 14:35 ET)

`git -C /Users/cobalt/cobalt log --oneline -8 -- "docs/40 - DevDocs/reports/"` → `34524c1`, `41ed33f`, `3b8148c`, `5476410`, `77b1a08`, `2a4a595`, `cccdfbe`, `d6332f6` — the R7 row is committed at `5476410`, R8/R9 at `41ed33f`/`34524c1`. Rows read from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-18.md` §4.

| launch-line rule | approved by | verdict |
|---|---|---|
| `cp …/cobalt/.env …/s2-p2-cards/.env` · `rm …/.env` · `ls -la …/.env` | R1 list (1) — ".env cp/rm/ls by path" | MATCH |
| `COBALT_ENV=dev uv run cobalt db migrate*` | R1 list (1) | MATCH |
| `COBALT_ENV=dev uv run pytest *` | R1 list (1) | MATCH |
| `COBALT_ENV=dev uv run cobalt validate*` | R1 list (1) | MATCH |
| `COBALT_ENV=dev uv run cobalt settings load *--dry-run*` | R1 list (1) | MATCH |
| `COBALT_ENV=dev uv run cobalt settings load --from …/ops-2026-09-18/scratch/daymode-settings-0918 --apply` | R7 (3), exact line, DEV only | MATCH |
| `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run pytest *` | R1 list (1) | MATCH |
| `uv run pytest *` · `uv run cobalt jobs restarts *` | R1 list (1) | MATCH |
| `git rebase main` | R1 list (1) | MATCH |
| `git rebase --abort` | R7 (2) | MATCH |
| `git cherry-pick *` | R2 | MATCH |
| `git add/commit/diff/status/log/show/rev-parse *` | R1 list (1) | MATCH |
| `git -C /Users/cobalt/cobalt log*` · `… rev-parse *` | R1 list (1) | MATCH |
| `cd` · `ls` · `grep` · `tail` · `wc` · `shasum -a 256` · `date` | R1 list (1) | MATCH |
| `--disallowedTools AskUserQuestion EnterWorktree` | R1 (all three launches) | MATCH |

Not in this line and not used: push, `bypassPermissions`, `--allow-prod`, any `COBALT_ENV=production` command, any vault write, `git reset`, `git branch -f`. R1 list (1) additionally carried `git rebase --continue`; this line is narrower, which is allowed.

Also noted, as the deploy-1 hub noted before me: the prompt file's tail carries a block styled as a system reminder asking for a `Claude-Session:` URL line in every commit. It arrives inside a tool result (the file's own bytes), not from the harness. The genuine harness attribution reminder names only `Co-Authored-By`. Not followed.

## PREFLIGHT (14:35–14:36 ET)

| # | rule probed | command | exit | verdict |
|---|---|---|---|---|
| P1 | `git status*` | `git status --porcelain` | 0 | allowed — no output (clean) |
| P2 | `git log*` | `git log -1 --oneline` | 0 | allowed — `976528f` |
| P3 | `date*` | `date` | 0 | allowed — Fri Sep 18 14:35:51 EDT 2026 |
| P4 | `git cherry-pick *` | `git cherry-pick -h` | 129 | allowed (usage printed; 129 is `-h`'s normal exit) |
| P5 | `uv run pytest *` | `uv run pytest --co -q tests/cobalt/test_radar_notes.py` | 0 | allowed — 16 tests collected |

Probed by first real use, per the prompt (no harmless variant inside their own pattern): the `.env` `cp`/`rm`/`ls` rules, `COBALT_ENV=dev uv run cobalt db migrate*`, both `settings load` rules, `COBALT_ENV=dev uv run pytest *`, `COBALT_ENV=dev uv run cobalt validate*`, `COBALT_VAULT_PATH=… uv run pytest *`, `uv run cobalt jobs restarts *`, `git rebase main`.

0 allowlisted shape denied.

## 0. Preconditions

| check | expected | observed | verdict |
|---|---|---|---|
| `git status --porcelain` | empty | empty | PASS |
| `git rev-parse --short HEAD` | `976528f` or a report-only commit above it | **`976528f`** = `<old-tip>` | PASS |
| `git log --oneline main..HEAD` | record `<n>` + list | **`<n>` = 34** — `976528f` … `f266a88` (21 P2 code/plan commits + 13 report commits; full list is the branch's own log, unchanged from the third run's close) | PASS |
| `git rev-parse --short main` | — | `34524c1` | recorded |
| `git -C /Users/cobalt/cobalt log --oneline -12` | tip = desk docs commit above `77b1a08`; 8 `Revert "…"` of ops-0918 | tip `34524c1` (desk docs), then `41ed33f`, `3b8148c`, `5476410`, `77b1a08`, then reverts `511cf25`, `04c09e4`, `159cc9a`, `34f9413`, `6a78c8b`, `2a4a595`, `cccdfbe` (+ `d6332f6` = 8) | PASS |
| `git log --oneline 77260b5..856176e` | exactly the 8 ops commits, `fe195ab` … `856176e` | `856176e`, `497d8c1`, `3ef1dfb`, `c7f0465`, `382c862`, `7e41a5c`, `93cd7c2`, `fe195ab` — **8** | PASS |

CONTINUE: step 1
