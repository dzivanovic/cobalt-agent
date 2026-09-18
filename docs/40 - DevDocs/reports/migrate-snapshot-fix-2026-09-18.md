# Migration harness — the proof must be SNAPSHOT-CONSISTENT (REPEATABLE READ)

Hub `migrate-snapshot-0918` (Opus 5, `claude-opus-5`), worktree `/Users/cobalt/cobalt-wt/s2-p2-cards`, branch `sprint-2/stack` from `15ec09d`. Prompt: `docs/40 - DevDocs/prompts/2026-09-18/22-migrate-snapshot-fix.md`. Authorization: `cto-2026-09-18.md` §4 **R1 list (1)** (this worktree's dev rules) + **R3**/**R5** (the weekend push) + **R18** (three tribunal checkers — that check is the desk's next run, not this one). Dev only: `COBALT_ENV=production` never appears, no `--allow-prod`, no vault write, no push, no merge.

## §0 Headline

- IN PROGRESS — see the last line.

## PREFLIGHT

Run 17:36 ET from `/Users/cobalt/cobalt-wt/s2-p2-cards`. **Zero denials.**

| rule | command | exit | allowed / DENIED |
|---|---|---|---|
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — **empty**, worktree clean |
| `Bash(git rev-parse *)` | `git rev-parse --abbrev-ref HEAD` | 0 | allowed — **`sprint-2/stack`** (the required branch) |
| `Bash(git log*)` | `git log -1 --oneline` | 0 | allowed — **`15ec09d`** = the expected tip |
| `Bash(date*)` | `date` | 0 | allowed — **`Fri Sep 18 17:36:15 EDT 2026`** |
| `Bash(uv run pytest *)` | `uv run pytest --co -q tests/cobalt/test_migrate_proof.py` | 0 | allowed — **30 tests collected** |
| `Bash(cp …/.env …/.env)` | `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s2-p2-cards/.env` | 0 | allowed — L41 interim, by name only, never printed, removed in step 2 |
| `Bash(COBALT_ENV=dev uv run cobalt db migrate*)` | `COBALT_ENV=dev uv run cobalt db migrate --help` | 0 | allowed — the four flags are `--allow-prod`, `--down-to`, `--rollback`, `--proof-only` |
| `Bash(git -C /Users/cobalt/cobalt log*)` | `git -C /Users/cobalt/cobalt log --oneline -8 -- "docs/40 - DevDocs/reports/"` | 0 | allowed — top row `fb767ab docs(desk): 09-18 deploy moves to Saturday … the migrate proof is not snapshot-consistent …; snapshot-fix prompt`: **the authorizing rows are committed on main** |
| `Bash(grep *)` | `grep -n "R1\|§4\|list (1)" "…/reports/cto-2026-09-18.md"` | 0 | allowed — R1's list (1) read rule by rule; see AUTHORIZATION below |

### AUTHORIZATION — verified rule by rule against R1 list (1)

R1 (06:46 ET, "Approved") list (1) is this worktree's dev rule set. Every rule in THIS launch line appears in it; the launch line is a strict SUBSET, so no new approval is owed (UNATTENDED-LAUNCH §1.3).

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

### BASELINE — `cobalt_dev` before step 1

`COBALT_ENV=dev uv run cobalt db migrate` (no-op forward), 17:38 ET, exit 0, **content UNCHANGED on every table**, proof cost BEFORE 5.5 s + AFTER 5.5 s = 11.0 s.

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
| `cobalt_redactions` | 121 | `177a0fde` | | `day_modes` | 2 | `f2ffb4d4` |
| `desk_grade` / `desk_packet` / `desk_regime` | 0 | `d41d8cd9` | | | | |

## Step 1 — the tests, RED

`tests/cobalt/test_migrate_proof.py` group **8. SNAPSHOT CONSISTENCY**, five tests, each against `cobalt_dev` with a SECOND connection (`db.connect_migration`, autocommit — it IS another session) playing the other writer. Discovery IS a fixed list (`placement.MOVED_TABLES/SEEDED_TABLES/CREATED_TABLES` is a dict literal), so per the prompt's fallback the concurrency table is `cobalt_redactions`; every row inserted is deleted **by its own id** in teardown.

`COBALT_ENV=dev uv run pytest -q tests/cobalt/test_migrate_proof.py -k "snapshot or invisible or repeatable or own_write or concurrent" --tb=short -p no:randomly` → **4 failed, 1 passed** in 11.18 s.

| # | test | before the change | quoted failing line |
|---|---|---|---|
| (a) | `test_a_commit_by_another_session_between_the_probes_is_invisible` | **RED** | `AssertionError: another session committed one row between the BEFORE and the AFTER probe and the proof called it CHANGED: rows 121 -> 122, digest 177a0fde30d8c28fa57360b49382abb1 -> da4f5e64aa7c4526c31d1172c239fdde.` / `assert 'CHANGED' == 'OK'` |
| (b) | `test_the_migrate_transactions_own_write_is_still_seen_between_the_probes` | **PASSES, by design** | — it is a PRESERVATION guard: the property "the transaction sees its own writes" holds at READ COMMITTED too, and the change must not break it. A test that fails first is impossible for a property that is already true; it is the one test in this group that cannot be red, and it is the one that would catch a fix that hid the migration's own changes. |
| (c) | `test_the_proof_only_transaction_is_repeatable_read_and_read_only` | **RED** | `AssertionError: --proof-only's transaction runs at 'read committed'. …` / `assert 'read committed' == 'repeatable read'` |
| (d) | `test_the_migrate_transaction_is_repeatable_read_and_read_write` | **RED** | `AssertionError: the migrate transaction runs at 'read committed', so its BEFORE and AFTER probes read two different databases` / `assert 'read committed' == 'repeatable read'` |
| (e) | `test_a_concurrent_update_to_a_row_the_migration_updates_fails_loud` | **RED** | `AssertionError: the harness did not name the serialization failure; an operator reading this at 20:40 on a deploy gets: 1 table(s) changed content across the migration. The transaction was rolled back before commit; compare against the pg_dump.` |

**(e) IS deterministic** — the desk's prompt allowed for it not being. The row is committed by the other session BEFORE the migrate transaction opens (so it is inside the snapshot), the other session commits over it while the migration holds that snapshot, and the migration then updates the same row. Nothing races: plain `SELECT`s take only `ACCESS SHARE`, so the other session's `UPDATE` is never blocked. The red run above is the full `cmd_migrate` path, and its captured proof table shows the pre-fix behaviour exactly — `cobalt_redactions … 122 -> 122 … dc32ce10 -> 208c6b30 CHANGED`, i.e. at READ COMMITTED the migration's own update is simply allowed and the verdict is a content change, not a serialization failure.

CONTINUE: step 2
