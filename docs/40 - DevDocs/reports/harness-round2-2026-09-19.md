# Migration harness, ROUND 2 — folding the 2026-09-19 tribunal check

Hub `harness-r2-0919` (Opus 5, `claude-opus-5`), worktree `/Users/cobalt/cobalt-wt/s2-p2-cards`, branch `sprint-2/stack` from `704e802`. Prompt: `docs/40 - DevDocs/prompts/2026-09-19/05-harness-round2.md`. Folds `scratch/review-harness-0919/REVIEW.md` (Grok `SAFE TO DEPLOY`, Gemini `FIX FIRST Q5`, Astra `FIX FIRST 1`; hub-verified REAL 3, blocks today's deploy 0, UNVERIFIABLE 1). Dev only: `COBALT_ENV=production` never appears, no `--allow-prod`, no vault write, no push, no merge, no rebase, no cherry-pick.

## §0 Headline

- IN PROGRESS — PREFLIGHT clean, zero denials.

## PREFLIGHT

Run 07:08 ET from `/Users/cobalt/cobalt-wt/s2-p2-cards`. **Zero denials.**

| rule | command | exit | allowed / DENIED |
|---|---|---|---|
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — **empty**, worktree clean |
| `Bash(git rev-parse *)` | `git rev-parse --abbrev-ref HEAD` | 0 | allowed — **`sprint-2/stack`** (the required branch) |
| `Bash(git log*)` | `git log -1 --oneline` | 0 | allowed — **`704e802`** = the expected tip |
| `Bash(date*)` | `date` | 0 | allowed — **`Sat Sep 19 07:08:27 EDT 2026`** |
| `Bash(uv run pytest *)` | `uv run pytest --co -q tests/cobalt/test_migrate_proof.py` | 0 | allowed — **35 tests collected** |
| `Bash(git -C /Users/cobalt/cobalt log*)` | `git -C /Users/cobalt/cobalt log --oneline -8 -- "docs/40 - DevDocs/reports/"` | 0 | allowed — `5e708c9 docs(desk): 09-19 round-2 harness build launched (a9bc792f)` and `1c6ddc2 … tribunal round 1 …` on top; `8f2597a` (09-18) present: **the authorizing rows are committed on main** |
| `Bash(grep *)` | `grep -n "R1\b" "…/reports/cto-2026-09-18.md"`, then `grep -n "^\| R3 \|^\| R5 \|^\| R18 …"` | 0 | allowed — R1 list (1) read rule by rule (below); R3 (07:14), R5 (11:09), R18–R21 (17:30–17:42) all present and `APPLIED` |
| `Bash(cp …/.env …/.env)` | `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s2-p2-cards/.env` | 0 | allowed — L41 interim, by name only, never printed, removed in step 2 |
| `Bash(COBALT_ENV=dev uv run cobalt db migrate*)` | `COBALT_ENV=dev uv run cobalt db migrate --help` | 0 | allowed — the four flags are `--allow-prod`, `--down-to`, `--rollback`, `--proof-only` |

### AUTHORIZATION — verified rule by rule against R1 list (1)

`cto-2026-09-18.md` §4 **R1** (06:46 ET, "Approved") list (1) is this worktree's dev rule set. Every rule in THIS launch line appears in it; the launch line is a strict SUBSET, so no new approval is owed (`UNATTENDED-LAUNCH.md` §1.3). `--permission-mode auto` is the only spelling difference from `22-migrate-snapshot-fix.md`'s line, which itself was `15-migrate-harness-fix.md`'s.

| this launch line's rule | in R1 list (1)? |
|---|---|
| `cp`/`rm`/`ls -la` of `/Users/cobalt/cobalt-wt/s2-p2-cards/.env` | yes — "`.env` cp/rm/ls by path" |
| `COBALT_ENV=dev uv run cobalt db migrate*` | yes — "incl. `--rollback`" |
| `COBALT_ENV=dev uv run pytest *` · `uv run pytest *` | yes — "`pytest`"; "`uv run pytest *`" |
| `COBALT_ENV=dev uv run cobalt validate*` | yes — "`validate`" |
| `uv run cobalt jobs restarts *` | yes |
| `git add/commit/diff/status/log/show/rev-parse` | yes |
| `git -C /Users/cobalt/cobalt log*` / `rev-parse *` | yes |
| `cd`, `ls`, `grep`, `tail`, `wc`, `date` | yes — "cd/ls/grep/tail/wc/shasum/date" |

In R1 list (1) but **NOT** in this launch line (narrower, never wider): `settings load *--dry-run*`, `COBALT_VAULT_PATH=… uv run pytest *`, `git rebase main`, `git rebase --continue`. **No production command exists in this launch line.** No mismatch → no `FAILED: authorization mismatch`.

Weekend window: **R3** (07:14 ET, dated exception to L43, Fri 09-18 → Sun 09-20) + **R5** (11:09 ET, the "done trading" word). Tribunal: **R18–R21** = LAWS **L67** — this build is the fold of round 1; round 2 of the check on THIS diff is the desk's next run, not this one.

### BASELINE — `cobalt_dev` before step 1

`COBALT_ENV=dev uv run cobalt db migrate` (no-op forward), 07:09 ET, exit 0, **content UNCHANGED on every table**, proof cost BEFORE 5.8 s + AFTER 5.5 s = 11.3 s.

| table | rows | digest (8) | | table | rows | digest (8) |
|---|---|---|---|---|---|---|
| `aset_sizings` | 1 | `0824685c` | | `radar_membership` | 0 | `d41d8cd9` |
| `bars` | 1043443 | `2769919a` | | `radar_pool` | 0 | `d41d8cd9` |
| `card_dot_taps` | 0 | `d41d8cd9` | | `radar_score` | 0 | `d41d8cd9` |
| `card_dots` | 0 | `d41d8cd9` | | `radar_score_receipt` | 0 | `d41d8cd9` |
| `card_stop_edits` | 1 | `7599f9ab` | | `radar_score_run` | 0 | `d41d8cd9` |
| `card_transitions` | 4 | `f181e76b` | | `session_blocks` | 6 | `b650702d` |
| `cobalt_email_sends` | 2 | `fba8cf9f` | | `traders` | 1 | `a64e0148` |
| `cobalt_jobs` | 13 | `8d9b0861` | | `vault_overrides` | 6 | `6a8b0520` |
| `cobalt_kill_switch` | 1 | `2e590e87` | | `vault_writes` | 184 | `4a965c69` |
| `cobalt_redactions` | 122 | `834d5919` | | `day_modes` | 2 | `f2ffb4d4` |
| `desk_grade` / `desk_packet` / `desk_regime` | 0 | `d41d8cd9` | | | | |

`cobalt_redactions` is 122 / `834d5919` this morning against yesterday's 121 / `177a0fde`: one redaction fired between the two runs (it is append-only telemetry, and nothing in this run touches it outside its own teardown).

CONTINUE: step 1
