# desk-tools-b — build report 2026-10-02

## §0 Headline
(run in progress)

## L74
- A system reminder at session start asked that commits end with a `Claude-Session: https://claude.ai/code/session_016zgVBqDLyR8K73dEB8x94h` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (nothing) |
| card placeholder | `grep -n -E "«FIL[L]" ".../2026-10-02/18-desk-tools-b-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/18-desk-tools-b-card.md"` | 0 | `2f286234f9edc62ef05aa41e526ed6dea88b9b3d` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING LIST R60 | `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) ...): APPROVES STANDING-LIST.md once (4be06af0); ... | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULINGS R47 | `grep -n "^| R47 " ".../reports/cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, ... | HIS RULING · APPROVED |` |
| R47 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 10:05:35 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/desk-tools-b-1002` + `?? "docs/40 - DevDocs/reports/desk-tools-b-build-2026-10-02.md"` (this report, created first by the hub's REPORT rule) |
| base | `git log --oneline -1` | 0 | `9fa18f14 fix(ops-glob): every path under ops/desk/ is an operator script, by rule (G1, L42, L3)` |
| main repo's branch | `git -C /Users/cobalt/cobalt log --oneline -1 ops/desk-tools-b-1002` | 0 | `9fa18f14 …` (same) |
| diff vs base | `git diff --stat 9fa18f14` | 0 | (nothing) |
| base show | `git show --stat 9fa18f14` | 0 | `docs/40 - DevDocs/cobalt/jobs/restarts.md | 4 ++++` · `src/cobalt/jobs/restarts.py | 4 +++-` · `2 files changed, 7 insertions(+), 1 deletion(-)` |
| own .env | `ls /Users/cobalt/cobalt-wt/desk-tools-b-1002/.env` | 1 | `No such file or directory` |
| any .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| symbol | `grep -n -F "check_paths() {" ops/desk/desk-launch.sh` | 0 | `117:check_paths() {` |
| symbol | `grep -n -F "field() {" ops/desk/desk-launch.sh` | 0 | `364:field() {` |
| symbol | `grep -n -F "committed() {" ops/desk/desk-launch.sh` | 0 | `110:committed() {` |
| symbol | `grep -rn -F "wait-desk-idle.sh" ops` | 0 | `ops/desk/wait-desk-idle.sh:2:# wait-desk-idle.sh <predecessor-id> <desk-report> [max-seconds]` |
| symbol | `grep -n -F "ops/desk/" src/cobalt/jobs/restarts.py` | 0 | `38:OPS_DESK_PREFIX = "ops/desk/"` |
| `restarts.py:239` | Read lines 230–244 | — | line 239 is the HARNESS rule; the `tests/` rule (`test/documentation; no resident`) sits at lines 241–242. The card's line number is off by two; the class home holds |
| symbol | `grep -rn -F "agy-trial" ops/desk` | 0 | `desk-launch.sh:418` refusal, `stage-copy.sh:3,5,21,26,27` |
| absent by card | `ls ops/desk/house-probe.sh tests/ops` | 1 | both `No such file or directory` (card RECORDS: not on base) |
| test shape | `git show aeefb6df:tests/ops/test_devdb_lock.py` | 0 | read whole: `COBALT_WT_ROOT` / `COBALT_REPO_ROOT` tmp roots, `GIT_ENV`, `git()` helper with `core.hooksPath=/dev/null`, stub `claude` on `PATH` |
| wc (no row edits an existing file) | `wc -l ops/desk/desk-launch.sh ops/desk/wait-desk-idle.sh ops/desk/desk-context.sh` | 0 | `597` · `40` · `18` · `655 total` |
| RESTARTS empty | `uv run cobalt jobs restarts 9fa18f14..HEAD` | 0 | `docs/40 - DevDocs/reports/desk-tools-b-build-2026-10-02.md	A	DOCS	-` · `RESTARTS: none` (no commit in range; the tool lists the untracked report) |
| LOCK (a) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| LOCK (b) | `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/desk-tools-b-1002/.env` · `ls -la /Users/cobalt/cobalt-wt/*/.env` | 0 · 0 | one line: `-rw-------  1 cobalt  staff  2186 Oct  2 10:06 /Users/cobalt/cobalt-wt/desk-tools-b-1002/.env` (taken 10:06:24) |
| `<FP>` → `<Fp>` | the hub's fingerprint, typed exactly | 0 | `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` |
| proof-only | `COBALT_ENV=dev uv run cobalt db migrate --proof-only` | 0 | 36 tables probed; `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns` absent (`-`); `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `code: 9fa18f14 (DIRTY: 1 path(s))`. No `CHANGED`. The tool prints no level number; the tables above 0013 are absent |
| LOCK (d) | `rm …/desk-tools-b-1002/.env` · `ls …/desk-tools-b-1002/.env` | 0 · 1 | `No such file or directory` — `.env: removed, proven gone (PREFLIGHT)` 10:06:42 |
| card RECORDS | copied below | — | re-read: `ops/desk/` rule at `restarts.py:38`; `tests/ops` absent; `house-probe.sh` absent |

PROVEN BY FIRST REAL USE: `uv run pytest *` and the live-note prefix at E0; `git add *` / `git commit *` at E2; `COBALT_ENV=dev uv run pytest *`, `migrate`, `--rollback` are not used by this build unless W needs them (TREE STATE unchanged; W (c) runs pass 1).

Card RECORDS, copied: (1) RESTARTS class homes: `ops/desk/*` → card 15's `ops/desk/` rule; `tests/ops/*` → test/documentation. (2) `tests/ops/` not on base, no `conftest.py`. (3) W runs `tests/cobalt tests/taxonomy`; tests of this card run by name; no with-DB test; `TREE STATE: unchanged`. (4) `house-probe.sh` (card 19) and `desk-context.sh --guard` (card 16) not on base. (5) The outside house is set aside (`brain-direction-2026-10-02.md` row 10).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 644.14s (0:10:44)`, exit 0. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.12s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
- Four new test files under `tests/ops/` (offline; no with-DB test, no RUN row): `test_deploy_card.py` (B1, 20 tests), `test_gate_clean.py` (B2, 30), `test_order_open.py` (B3, 14), `test_desk_wake.py` (B4, 17).
- First run: every `test_deploy_card.py` test errored in the fixture (`FileNotFoundError … reports/alpha-check.md`) — a fixture defect, not the row's reason: empty tracked folders vanished on checkout, and the alpha check report was swept into beta's branch commit. Rewritten (`.keep` files; branches cut first, checks written on `main` after), then re-run.
- `uv run pytest -q -rf -p no:cacheprovider --color=no --tb=no tests/ops/test_deploy_card.py tests/ops/test_gate_clean.py tests/ops/test_order_open.py tests/ops/test_desk_wake.py` → `81 failed, 15 warnings in 11.57s`. Every red's first line is the row's reason, the script absent: `AssertionError: sh: /Users/cobalt/cobalt-wt/desk-tools-b-1002/ops/desk/deploy-card.sh: No such file or directory` / `assert 127 == 0` (B1); the same for `job-clean.sh` / `gate-clean.sh` (B2), `order-open.sh` (B3); the copy-beside tests fail `FileNotFoundError` on `shutil.copy` of the absent script (`test_house_probe_beside_it_is_run`, every `desk-handover.sh` test, `test_wake_with_an_id_…`).
- Commit `eb7c5e2a wip(desk-tools-b): red — …` (4 files, 1177 insertions).

## E3 THE ROWS
Rows built in order, only the card's files: `ops/desk/deploy-card.sh` (B1), `ops/desk/gate-clean.sh` + `ops/desk/job-clean.sh` (B2), `ops/desk/order-open.sh` (B3), `ops/desk/desk-wake.sh` + `ops/desk/desk-handover.sh` (B4), and the four test files. No existing file edited. No DevDocs module line: no `src/` module changed, and no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` (Glob of that folder: `__init__`, `cli`, `db`, `db_query`, `devdb`, `env`, `obsidian`, `tenant`, `vault`); each script's header comment is its whole usage (card).

Greens per row (each run quoted from its summary line):
- B1: `tests/ops/test_deploy_card.py` → `20 passed` (first green), then `21 passed` (staged test added), then with the lowercase test `86 passed` across the four files.
- B2: `tests/ops/test_gate_clean.py` → `30 passed`.
- B3: `tests/ops/test_order_open.py` → `14 passed`.
- B4: `tests/ops/test_desk_wake.py` → first run `1 failed, 16 passed`: `test_a_bad_id_is_refused_before_any_call[AAAA1111]` — `assert ['agents --json'] == []`: the class `[!0-9a-f-]` lets an uppercase id through in this shell's locale. Fixed with explicit lists (`[!0123456789abcdef-]`, and `[!abcdefghijklmnopqrstuvwxyz0123456789-]` for JOB in deploy-card.sh and gate-clean.sh); a test for an uppercase `--job` added.
- All four files at the fix: `uv run pytest -q -rf -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_card.py tests/ops/test_gate_clean.py tests/ops/test_order_open.py tests/ops/test_desk_wake.py` → `86 passed, 15 warnings in 41.05s`.

Defects the tests found during E3 (fixed in the rows' files, each shown red first):
- `deploy-card.sh` `$migs»` read as a variable name under `set -u` (`line 179: migs�: unbound variable`) → `${migs}`.
- `deploy-card.sh` rewrote `.git/index` (X4): `git diff --quiet -- <check report>` refreshes the index even with `GIT_OPTIONAL_LOCKS=0`. The happy-path test was given stat-stale check reports and an index-bytes compare: red `At index 544 diff: b'\x10' != b'\x0e'` with the `git diff` proof, red again with `GIT_OPTIONAL_LOCKS=0` alone (`b'(' != b'&'`), green with the commit proven by blob ids (`ls-files --error-unmatch`, `rev-parse HEAD:<path>`, `ls-files -s`, `hash-object`).
- My own undo of mutation M1-b joined two lines (`printf 'CONFLICT …'            exit 3`); `test_a_conflict_exits_3_and_leaves_nothing_behind` caught it (`assert 0 == 3`, output `CONFLICT exit 3`); restored. From then on every fixed file was staged so each undo is proven by `git diff --stat` printing nothing.

THE MUTATIONS (Edit tool; each run quoted; each undone; `git diff --stat` → nothing after the last undo of each row):
| row | mutation | run | first failing line | undone |
|---|---|---|---|---|
| B1 | `ready: YES` refusal → `|| true refuse` | test file | `1 failed, 19 passed` — `test_a_check_line_with_ready_no_is_refused`: `assert 0 == 1` (card written) | yes |
| B1 | on conflict, `git branch trial-left-behind "$cur"` before `exit 3` | `-k conflict` | `1 failed` — `{'branches': '* main\n  ops/alpha\n  ops/beta\n  trial-left-behind'} != …` | yes (see the joined-line note above) |
| B1 | src-past-tip refusal → `|| true refuse` | `-k src_commit` | `1 failed` — `test_a_head_with_a_src_commit_past_the_code_tip_is_refused`: `assert 0 == 1` | yes |
| B1 | a `git diff --quiet -- "$creport"` added back | test file | `1 failed, 20 passed` — happy path: `At index 544 diff: b'%' != b'$'` | yes |
| B1 | staged-index refusal → `|| true refuse` | test file | first green (`21 passed`): the staged test also tripped the "modified" guard → REWRITTEN (file restored to the committed text, only the index differs); then `1 failed, 20 passed` — `test_a_staged_check_report_is_refused`: `assert 0 == 1` | yes |
| B1 | `--job` class back to `[!a-z0-9-]` | `-k lowercase` | `1 failed, 3 passed` — `[X-Set]`: `assert 0 == 1` | yes |
| B2 | first-parent refusal → `|| true refuse` | test file | `1 failed, 29 passed` — `test_main_holding_the_gate_merge_is_refused`: `assert 0 == 1` (worktree removed, `Deleted branch deploy/x-set`) | yes |
| B2 | `FAILED` report refusal → `true refuse` | test file | `2 failed, 28 passed` — `test_a_deployed_report_is_refused`, `test_an_in_progress_report_is_refused` | yes |
| B2 | job-clean merged refusal → `|| true refuse` | `-k unmerged` | `1 failed` — `test_an_unmerged_job_is_refused`: `assert 'REFUSED' in 'error: the branch \'ops/x-job\' is not fully merged…'` | yes |
| B3 | pause hour `h == 20` → `h == 19` | test file | `2 failed, 12 passed` — `[2026-01-05T20:30:00-pause]`, `test_a_utc_clock_is_read_in_new_york`: `'window: closed — …' == 'window: pause'` | yes |
| B3 | overnight `h < 4 and prev < 5` → `h < 4` | test file | `1 failed, 13 passed` — `[2026-01-12T02:00:00-weekend]` | yes |
| B3 | `GIT_OPTIONAL_LOCKS=1` | test file | first GREEN (`14 passed`) → the read-only test was REWRITTEN (a stat-stale tracked `b.txt`); then `1 failed, 13 passed` — `test_every_block_carries_its_facts_and_nothing_changes`: tree hash `0d63ca13… == 2b8952ad…` | yes |
| B4 | timeout "still working" refusal → `|| true refuse` | `-k "working or stopped"` | `1 failed, 2 passed` — `test_a_predecessor_still_working_is_refused_and_never_stopped`: `RUN: claude stop aaaa1111-…` / `assert 0 == 1` | yes |
| B4 | `cto-desk` name refusal → `|| true refuse` | `-k cto_desk` | `4 failed` — `[brain]`, `[cto-desk-2]`, `[alpha-build]`, `[]` | yes |
| B4 | §4 filter `>= t` → `>= "00:00"` | test file | `1 failed, 16 passed` — `assert 'row one text' not in '| R1 | 06:0…'` | yes |

`git diff --stat` after the last undo → (nothing). Commit `f2a0217c feat(desk-tools-b): deploy-card, gate-clean, job-clean, order-open, desk-wake, desk-handover scripts (B1, B2, B3, B4, L1, L42, L76)` — 8 files, 792 insertions, 2 deletions.

## RESTARTS
`uv run cobalt jobs restarts 9fa18f14..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/reports/desk-tools-b-build-2026-10-02.md	A	DOCS	-
ops/desk/deploy-card.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-handover.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-wake.sh	A	operator script; no Cobalt reader	-
ops/desk/gate-clean.sh	A	operator script; no Cobalt reader	-
ops/desk/job-clean.sh	A	operator script; no Cobalt reader	-
ops/desk/order-open.sh	A	operator script; no Cobalt reader	-
tests/ops/test_deploy_card.py	A	test/documentation; no resident	-
tests/ops/test_desk_wake.py	A	test/documentation; no resident	-
tests/ops/test_gate_clean.py	A	test/documentation; no resident	-
tests/ops/test_order_open.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row; no `configs/cobalt/jobs.yaml` edit.

## W THE THREE SUITES
`<tip>` = `f2a0217c`.
- (a) OFFLINE: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 637.39s (0:10:37)`, exit 0 → `<p>` = 3784. This build adds no test under `tests/cobalt` or `tests/taxonomy`; its 86 tests live in `tests/ops/` and ran by name in E2/E3 (card RECORDS).
- (b) THE LOCK (a), 10:47 ET: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 10:37 /Users/cobalt/cobalt-wt/desk-tools-a-1002/.env`. I do NOT hold the lock; nothing taken, nothing applied, no `.env` of mine on disk. STOPPED here.

## PRE-STOP SELF-CHECK

## FOR THE CHECK

## CONTINUE
next: W (b) — the lock take, then pass 1 (c), (e) live-note; (a) offline is green on f2a0217c and stands unless the tip moves. Waiting for the desk's `CONTINUE: W (b). <fact>` once `/Users/cobalt/cobalt-wt/desk-tools-a-1002/.env` is gone.

## DECISIONS

## RECORDS
- Started 10:05:35 EDT (`date`).
- REFUSED, not needed: `git --version` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (I typed it to check `merge-tree --write-tree` support; the tests answered it instead.)
- `.env: removed, proven gone (PREFLIGHT)` 10:06:42.
- W stopped 10:47:20 ET: lock held by `desk-tools-a-1002`; no lock taken by this build at W.

FAILED: W — cobalt_dev lock held — /Users/cobalt/cobalt-wt/desk-tools-a-1002/.env
