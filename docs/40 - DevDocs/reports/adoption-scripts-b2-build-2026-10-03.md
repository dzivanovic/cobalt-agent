# adoption-scripts-b — build report (b2, 2026-10-03)

## §0 Headline
- All six rows are built on `02`'s checked tip `6251baeb`. The tip is `b7eeb80c`. DB: none, so no lock was taken.
- M5 port: `gate.sh`, `desk-launch.sh` and `test_desk_launch_prechecks.py` are byte-equal to `44d3f246`. `preflight.sh` carries both A9 and M1. `test_gate.py` and `test_preflight.py` carry both sides. `test_pass1_db_only.py` is `44d3f246`'s with the xfail mark dropped.
- M6: STANDING-LIST §3 PATHS now names the repo path and CLASS (a) for the lock scripts, the sentence O2 named.
- Suites: offline 3749/0, ops 603/0 (1 xfailed), live-note 146/0. RESTARTS: none.
- Two decisions, neither his: PREFLIGHT's status row met this report (M1's own defect), and the card's whole-file M6 count cannot reach 0.

## L74
- A system notice in this session asked commits to carry a `Claude-Session:` line. Recorded once here as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
Started `Sat Oct  3 15:38:25 EDT 2026` (date).
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | nothing |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-03/03c-adoption-scripts-b-card.md"` | 1 | nothing |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/03c-adoption-scripts-b-card.md"` | 0 | `38dd76ae8409deaea98abb87b8a2f064cde167ea` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | nothing |
| STANDING LIST 2026-09-30 R60 | `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** (… APPROVES STANDING-LIST.md once (4be06af0) …) | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| 2026-10-02 R47 | `grep -n "^| R47 " ".../reports/cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only … | HIS RULING · APPROVED |` |
| R47 committed | `git -C … log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| 2026-10-02 R154 | `grep -n "^| R154 " …` | 0 | `161:| R154 | 17:29 ET | HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock at build + check …; pass 1 under the lock = with-DB tests only … | HIS RULING · APPROVED |` |
| R154 committed | `git -C … log -1 --format=%H -S"| R154 |" …` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| 2026-10-02 R157 | `grep -n "^| R157 " …` | 0 | `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week, adoption card included … | HIS RULING · APPROVED |` |
| R157 committed | `git -C … log -1 --format=%H -S"| R157 |" …` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 15:38:25 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/adoption-scripts-b2-1003` · `?? "docs/40 - DevDocs/reports/adoption-scripts-b2-build-2026-10-03.md"`: the second line is this report, which the hub's first Write made. That is the defect row M1 fixes (DECISION 1) |
| head | `git log --oneline -1` | 0 | `6251baeb fix(adoption-hubs): preflight lists a sibling's .env as information and fails only on this worktree's; THE LOCK SCRIPTS names class (a) (A9, A10; L1 L76 L77)` |
| main repo | `git -C /Users/cobalt/cobalt log --oneline -1 ops/adoption-scripts-b2-1003` | 0 | the same line |
| diff | `git diff --stat 6251baeb` | 0 | nothing |
| base | `git show --stat 6251baeb` | 0 | `docs/40 - DevDocs/prompts/STANDING-LIST.md | 6 +++---` · `ops/desk/preflight.sh | 14 ++++++++------` · `2 files changed, 11 insertions(+), 9 deletions(-)` |
| env here | `ls /Users/cobalt/cobalt-wt/adoption-scripts-b2-1003/.env` | 1 | `No such file or directory` |
| env anywhere | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| symbol M4 | `grep -n -F "TREE STATE" ops/desk/desk-launch.sh` | 0 | `507:    case "$(field "TREE STATE")" in` · `509:        *) refuse "incomplete card: TREE STATE must be 'unchanged' or 'row <id>'" ;;` |
| callers M4 | `grep -n -F "tree_state" ops/desk/desk-launch.sh` | 0 | `506:tree_state() {` · `678:    tree_state` · `699:    tree_state` |
| symbol M1 | `grep -n -F "git status --short --branch" ops/desk/preflight.sh` | 0 | `8:#   status        …` · `94:out=$(git status --short --branch 2>&1)` · `98:row status "git status --short --branch" "$rc" "$out" "$ok"` |
| symbol M2 | `grep -n -F "held_env" ops/desk/gate.sh` | 0 | `234:held_env() {` · `247:    held_env` · `273:    held_env` |
| symbol M2 | `grep -n -F "take-devdb-lock.sh" ops/desk/gate.sh` | 0 | `27:` (header) · `254:` · `259:` · `260:        sh "$HERE/take-devdb-lock.sh" "$name" 90 >> "$log" 2>&1` · `264:` (exit 4) · `265:` |
| symbol M3 | `grep -n -F " --db-only" ops/desk/gate-lists.md` | 0 | `24:` — the `## PASS 1` line, ` --db-only` once after `tests/cobalt tests/taxonomy` |
| M3 caller | `grep -n -F "gate.sh" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | 0 | `13:` (CLASS (a) text) · `72:` (table) · `98:` · `102:- THE GATE, ONE CALL: … sh /Users/cobalt/cobalt/ops/desk/gate.sh <WORKTREE> all --deploy (--deploy runs pass 1 whole, without --db-only: his 2026-10-02 R154) …` |
| symbol M6 | `grep -n -F ".claude/ops" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` | 0 | 8 lines: `36:` (class (a) installed spelling) · `49:` (02's A10: "the `--add-dir /Users/cobalt/.claude/ops` root stays on each line") · `54:` (§1 `--add-dir`) · `107:` (§2 `desk-context.sh`) · `109:` (§3 header `--add-dir`) · `156:` (§3 PATHS: "(`/Users/cobalt/.claude/ops` for the two lock scripts)") · `172:` (§4 `desk-launch.sh`) · `192:` (§6 `--add-dir`) |
| M6 source | Read `reports/adoption-hubs-check-2026-10-03-r2.md:65-69,117,124` | — | FINDING O2: `STANDING-LIST.md:156` … "Settled by a row that names the sentence: (`/Users/cobalt/cobalt` for the scripts), then `grep -c -F "for the two lock scripts"` → `0`" |
| M5 sources | `git diff --stat 0a4a7743 6251baeb -- ops/desk/gate.sh ops/desk/desk-launch.sh tests/ops/test_desk_launch_prechecks.py` | 0 | nothing: `02` left these three files alone, so they port from `44d3f246` byte-equal |
| M5 shared | `git diff --stat 0a4a7743 6251baeb -- ops tests/ops` | 0 | `ops/desk/preflight.sh 14` · `tests/ops/test_gate.py 47` · `tests/ops/test_hub_lines.py 238` · `tests/ops/test_pass1_db_only.py 47` · `tests/ops/test_preflight.py 32` |
| M5 port source | `git show --stat 5c96db68` / `44d3f246` | 0 | red: `test_desk_launch_prechecks.py +40` · `test_gate.py +137` · `test_pass1_db_only.py` · `test_preflight.py +97`; fix: `desk-launch.sh` · `gate.sh` · `preflight.sh` |
| wc -l | `wc -l <the rows' files>` | 0 | preflight.sh 194 · gate.sh 499 · desk-launch.sh 989 · test_preflight.py 250 · test_gate.py 632 · test_pass1_db_only.py 51 · test_desk_launch_prechecks.py 635 · STANDING-LIST.md 207 |
| READ tail | `tail -n 3 "docs/40 - DevDocs/reports/adoption-hubs-build-2026-10-03.md"` | 0 | last line `RESUMED: E3 15:12 ET` |
| READ tail | `tail -n 3 ".../reports/adoption-hubs-decisions-2026-10-03.md"` (main tree; not in this worktree) | 0 | last line `FOR THE CHECK (card 02 ## RECORDS): Build decisions 1–11 answered … 7 is not his.` |
| RESTARTS | `uv run cobalt jobs restarts 6251baeb..HEAD` | 0 | `path	change	rule	restart` · `docs/40 - DevDocs/reports/adoption-scripts-b2-build-2026-10-03.md	A	DOCS	-` · `RESTARTS: none` (it created `.venv` on first use) |
| DB | card header `DB: none` | — | no lock probe; with-DB not run |

Card `## RECORDS`, copied: (1) RE-ISSUE 10-03: stacked on `02`'s checked tip `6251baeb`; M1–M4 ported from `44d3f246` by M5; M6 added. Re-read: `git log --oneline -1` → `6251baeb`; `git log --oneline -4 44d3f246` holds `44d3f246` and `5c96db68`. (2) `DB: none`: every file under `ops/`, `tests/ops/`, plus M6's `STANDING-LIST.md`. Re-read at W (a0). (3) FOR THE CHECK (judge R113): carried to `## FOR THE CHECK`.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3749 passed, 746 skipped, 1 xfailed, 36 warnings in 585.54s (0:09:45)`, exit 0.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.72s`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.
- The rows' own suite: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `574 passed, 1 xfailed, 15 warnings in 197.73s (0:03:17)`.

## E2 RED
The tests are ported from the first build's red commit `5c96db68` (as it stands at `44d3f246`), with no `ops/` edit:
- `tests/ops/test_preflight.py`: the 7 `test_m1_*` tests, the tracked-reports fixture lines and `write_card(check_report=…)`, added on top of `02`'s A9 tests.
- `tests/ops/test_gate.py`: `waiting_lock_scripts`, the 3 `test_m2_*` tests and the 5 `test_m3_*` tests, inserted after `test_a_lock_script_that_says_not_free_exits_4`, on top of `02`'s `hub_commands` and hub-reference test.
- `tests/ops/test_pass1_db_only.py`: `44d3f246`'s file, with the `xfail(strict=True)` mark and its `import pytest` dropped (M5).
- `tests/ops/test_desk_launch_prechecks.py`: `set_tree_state` and the 3 `test_m4_*` tests, parametrized over build and check.

Port proof:
- `git diff --stat 44d3f246 -- <the four files>` → `test_gate.py | 47`, `test_pass1_db_only.py | 7 ------`, `test_preflight.py | 32`. `test_desk_launch_prechecks.py` is byte-equal.
- The 47 and 32 lines equal `02`'s own diff of those files (`git diff --stat 0a4a7743 6251baeb`: `test_gate.py 47`, `test_preflight.py 32`). The 7 lines are the mark and the import.

`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_preflight.py tests/ops/test_gate.py tests/ops/test_pass1_db_only.py tests/ops/test_desk_launch_prechecks.py` on BASE code → `9 failed, 136 passed, 15 warnings in 46.59s`. The reds:
- M1 build: `?? "docs/40 - DevDocs/reports/x-job-build.md"` … `FAILED PREFLIGHT: status` / `assert 1 == 0` (test_preflight.py:250). The report alone fails.
- M1 check: `?? "docs/40 - DevDocs/reports/x-job-check.md"` … `FAILED PREFLIGHT: status` / `assert 1 == 0` (:306).
- M2 wait: `AssertionError: cobalt_dev lock held — …/wt/beta/.env` / `assert 4 == 0` (test_gate.py:598). Exit 4 at once.
- M2 never-free: `assert [] == ['take x-job ... 'try 3 held']` (:615). The gate exited 4 before it called the take.
- M2 no lock scripts: `with-DB 10/0` … `assert 0 == 1` (:631). BASE took the `cp .env` way and ran every pass.
- M3 deploy, `all` and `withdb --deselect`: `REFUSED: unknown argument '--deploy'` / `assert 1 == 0` (:648, :671).
- M4 build and check: `REFUSED: incomplete card: TREE STATE must be 'unchanged' or 'row <id>'` / `assert 1 == 0` (test_desk_launch_prechecks.py:640).

Negative controls that PASSED on BASE:
- M1: the report plus another untracked file; a modified tracked report; another untracked file alone; a build given a CHECK REPORT; a check with its report plus another file.
- M3: no `--deploy` keeps `--db-only`; `--deploy` is refused in offline, livenote and probe; a PASS 1 without the token.
- M4: `unchanged` and `row A3` launch; `nonsense`, empty and `row` are refused.

M5: `test_pass1_db_only.py` passes on BASE (2 passed), because `02`'s STEP-G text is already below it. Its red-before-settle is `44d3f246`'s xfail-strict mark put back, shown as an E3 mutation.

M6 (a grep, no test file):
- `grep -c -F "for the two lock scripts" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` → `1`. That is the sentence O2 names.
- The card's own `grep -c -F ".claude/ops" …` → `8` (DECISION 2).

Commit `289c7a0f wip(adoption-scripts-b): red — M1 M2 M3 M4 tests ported from 5c96db68 onto 6251baeb (M5)`.

## E3 THE ROWS
Built in the card's order. Every mutation was made and undone with Edit; each undo was proven by `git diff 44d3f246 -- <file>` (empty for `gate.sh` and `desk-launch.sh`; for `preflight.sh`, exactly `02`'s A9, `14 ++++++++------`) and `git diff --stat 289c7a0f -- tests` (empty).
- **M1** `ops/desk/preflight.sh`: `44d3f246`'s status block and header lines, applied on top of `02`'s A9.
  - `git diff 44d3f246 -- ops/desk/preflight.sh` → only `02`'s A9 hunks (the `env anywhere` header and the sibling loop), so both edits stand.
  - Green: `test_preflight.py` → `25 passed`.
  - Mutation 1 (`if false && …`, the fix off) → `2 failed, 23 passed`: the M1 build test (`?? "docs/40 - DevDocs/reports/x-job-build.md"` … `FAILED PREFLIGHT: status`, :250) and the M1 check test (:306).
  - Mutation 2 (`if true; then`, any lone line accepted) → `4 failed, 21 passed`:
    - `test_an_uncommitted_file_fails` (`assert 0 == 1`, :139).
    - The modified tracked report (` M "docs/40 - DevDocs/reports/x-job-build.md"` → `PREFLIGHT OK`, :275).
    - Another untracked file alone (`?? "…x-other-build.md"` → `PREFLIGHT OK`, :286).
    - A build given the check report (:296).
  - Mutation 3 (`-eq 2` → `-ge 2`, the one-line guard off) → `2 failed, 23 passed`: the report plus `?? src/b.py` → `PREFLIGHT OK`, for the build (:262) and for the check (:318).
- **M2** `ops/desk/gate.sh`: `44d3f246`'s hunks. `git diff 44d3f246 -- ops/desk/gate.sh` → nothing (byte-equal).
  - Mutation a (the at-once held-`.env` pre-check put back in `take()`) → `2 failed, 48 passed`: the wait test (`cobalt_dev lock held — …/wt/beta/.env` / `assert 4 == 0`, :598) and the never-free test (`assert [] == ['take x-job ... 'try 3 held']`, :615).
  - Mutation b, first form (`true || [ -f take ] && [ -f release ] || refuse`) → `50 passed`. That form was not a mutation: by `&&`/`||` precedence the release check still refused. I rewrote the mutation, not the test.
  - Mutation b (`|| refuse` → `|| true`, the guard off) → `1 failed, 49 passed`: `''.startswith('REFUSED: ')` is False (:632).
- **M3** `ops/desk/gate.sh` (the same byte-equal port).
  - Mutation a (`--deploy` keeps `$PASS1`) → `2 failed, 50 passed`: `At index 8 diff: '--db-only' != '--deselect'` (:651, :673).
  - Mutation b (`p1cmd=$PASS1_DEPLOY` always, which breaks the negative control) → `4 failed, 46 passed`, each `At index 8 diff: '--deselect' != '--db-only'`:
    - `test_withdb_green_runs_the_lists_commands_byte_for_byte_in_order` (:245).
    - `test_the_hub_file_is_no_longer_read_a_moved_pass_1_is_what_runs` (:288).
    - `test_a_deselect_goes_into_pass_1…` (:340).
    - `test_m3_without_deploy_pass_1_keeps_db_only` (:663).
  - Mutation c (`n == 1` → `n <= 1`) → `1 failed, 49 passed`: the gate ran a PASS 1 that has no token (`pass 1: whole (deploy)` … `with-DB 10/0`, `assert 0 == 1`, :692).
- **M4** `ops/desk/desk-launch.sh` `tree_state()`. `git diff 44d3f246 -- ops/desk/desk-launch.sh` → nothing (byte-equal).
  - Mutation a (the absence clause removed) → `2 failed, 10 passed`: `REFUSED: incomplete card: TREE STATE must be 'unchanged' or 'row <id>'`, for build and for check (:640).
  - Mutation b (`return 0` first) → `6 failed, 6 passed`: `nonsense`, empty and `row` launch, for build and for check (`assert 0 == 1`, :222).
- **M5** the settle:
  - `test_pass1_db_only.py`: `44d3f246`'s xfail-strict mark put back → `1 failed, 1 passed`, `[XPASS(strict)] card 02 A3 (amended 10-03) writes STEP-G's …`. Dropped → `2 passed`.
  - `test_gate.py` before the settle (`44d3f246`'s byte-for-byte hub test in place of `02`'s) → `1 failed, 49 passed`, `KeyError: 'offline'` (:264). Both sides → `50 passed`.
- **M6** `STANDING-LIST.md:156`. §3 PATHS now reads "(`/Users/cobalt/cobalt` for the scripts: the two lock scripts are CLASS (a), `ops/desk/` at the repo path)".
  - `grep -c -F "for the two lock scripts"` → `0` (red `1`).
  - The card's `grep -c -F ".claude/ops"` → `7` (red `8`). See DECISION 2.
- Greens together: `test_preflight.py test_gate.py test_pass1_db_only.py test_desk_launch_prechecks.py test_desk_launch_devfix.py test_devdb_lock.py test_hub_lines.py test_install_fixed.py test_authorize.py` → `269 passed, 15 warnings in 129.78s`. Before that, `test_gate.py test_pass1_db_only.py test_desk_launch_prechecks.py test_desk_launch_devfix.py` → `168 passed`.
- DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers an `ops/desk` script. The Grep hits `jobs/restarts.md` and `db_migrations/cli.md` are `src/cobalt` module pages that only mention them. The scripts' header comments carry the change.

Commit `b7eeb80c fix(adoption-scripts-b): M1-M4 ported from 44d3f246 onto 6251baeb (gate waits, deploy's whole pass 1, TREE STATE optional; preflight carries A9 and M1); STANDING-LIST §3 PATHS names the repo path (M1 M2 M3 M4 M5 M6; L1 L3 L76)`.

## RESTARTS
`uv run cobalt jobs restarts 6251baeb..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/adoption-scripts-b2-build-2026-10-03.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/gate.sh	M	operator script; no Cobalt reader	-
ops/desk/preflight.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
tests/ops/test_gate.py	M	test/documentation; no resident	-
tests/ops/test_pass1_db_only.py	M	test/documentation; no resident	-
tests/ops/test_preflight.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `b7eeb80c`.
- (a0) `git diff --name-only --no-renames 6251baeb` → `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `ops/desk/desk-launch.sh` · `ops/desk/gate.sh` · `ops/desk/preflight.sh` · `tests/ops/test_desk_launch_prechecks.py` · `tests/ops/test_gate.py` · `tests/ops/test_pass1_db_only.py` · `tests/ops/test_preflight.py`. Every path starts with `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 8 paths)`**.
- (a) `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3749 passed, 746 skipped, 1 xfailed, 36 warnings in 570.29s (0:09:30)`, exit 0. This build adds no test there.
- ops: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `603 passed, 1 xfailed, 15 warnings in 205.38s (0:03:25)`. That is the E0 574 plus 29 new tests: 7 `test_m1_*` (test_preflight.py), 3 `test_m2_*` and 7 `test_m3_*` (one parametrized ×3; test_gate.py), and 12 `test_m4_*` (test_desk_launch_prechecks.py). `test_pass1_db_only.py` holds 2 tests before and after: `test_the_gate_lists_pass1_holds_db_only_once_after_the_two_suites` and `test_the_deploy_hub_step_g_calls_the_gate_with_deploy` replace `02`'s two.
- (e) `ls /Users/cobalt/cobalt-wt/adoption-scripts-b2-1003/.env` → `No such file or directory`. Then `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.83s`. The one skip is `test_replay_line.py:266` `COBALT_TEST_LIVE_DRC`, which does not name `COBALT_LIVE_VAULT_ROOT`.
- with-DB: not run (DB: none).

## PRE-STOP SELF-CHECK
1. "Every added or changed test shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten."
   - E2 reds: M1 build and check; M2 wait, never-free and no-scripts; M3 ×2; M4 build and check.
   - Every negative control went red under an E3 mutation: M1 mutations 2 and 3; M3 b and c; M4 b. The M5 settle red is the XPASS(strict) and `KeyError: 'offline'`.
   - One mutation (M2 b, first form) was itself wrong and was rewritten. The test was not changed.
   - The three `--deploy`-refused-in-offline/livenote/probe tests go red on no mutation of their own. BASE already refused `--deploy` as unknown, and the fix keeps that refusal. Named, as the first build named it.
   - M6 has no test file. Its red and green are the grep counts (`1` → `0`).
2. "Every entry path of each rule pinned by a test."
   - `tree_state` callers `680` (build) and `701` (check), from the grep at the tip, are both pinned by the parametrized `test_m4_*`.
   - The `gate.sh` lock guard is pinned for `withdb`, `all` and `probe`. `--deploy` is pinned under `withdb` and `all`, and refused in the other three modes.
   - `preflight.sh build` and `check` are both pinned for M1. `02`'s A9 tests still pass beside them.
   - The STEP-G caller (`DEPLOY-HUB.md:102`) is pinned by `test_the_deploy_hub_step_g_calls_the_gate_with_deploy`.
3. "Every `file:line`, count and quote in the report re-read from tool output at the tip." Re-run at `b7eeb80c`:
   - `grep -n -F "tree_state" ops/desk/desk-launch.sh` → `507`, `680`, `701`.
   - `grep -n -F "held_env" ops/desk/gate.sh` → `255`, `286` (the after-take proof only).
   - `grep -n -F "expected" ops/desk/preflight.sh` → `11, 100, 119, 126`.
   - `grep -n -F "siblings holding" ops/desk/preflight.sh` → `18, 194, 196` (A9 stands).
   - `grep -n -F "for the scripts" STANDING-LIST.md` → `156:`.
   - `git log --oneline 6251baeb..HEAD` → the two commits.
   - `git diff 44d3f246 -- ops/desk/gate.sh` and `-- ops/desk/desk-launch.sh` → nothing.

## FOR THE CHECK
- `6251baeb..b7eeb80c`:
  - `289c7a0f wip(adoption-scripts-b): red — M1 M2 M3 M4 tests ported from 5c96db68 onto 6251baeb (M5)`
  - `b7eeb80c fix(adoption-scripts-b): M1-M4 ported from 44d3f246 onto 6251baeb (gate waits, deploy's whole pass 1, TREE STATE optional; preflight carries A9 and M1); STANDING-LIST §3 PATHS names the repo path (M1 M2 M3 M4 M5 M6; L1 L3 L76)`
- Per row: reds in E2; mutations, greens and port diffs in E3, all quoted. There are no RUN rows.
- Port proof (M5):
  - `git diff 44d3f246 --` `gate.sh`, `desk-launch.sh` and `test_desk_launch_prechecks.py` → nothing.
  - `preflight.sh` differs by `02`'s A9 alone.
  - `test_gate.py` (47 lines) and `test_preflight.py` (32 lines) differ by `02`'s own diffs alone.
  - `test_pass1_db_only.py` differs by the 7 lines of the mark and the import.
  - The judge's R113 record is met: the gate waits through `take-devdb-lock.sh` (02 r2 O1); §3 names class (a) (02 r2 O2); `test_pass1_db_only.py` is `44d3f246`'s with the mark dropped; `test_gate.py` carries both sides; `preflight.sh` carries A9 and M1.
- X1, can `gate.sh` run a `uv` command while another worktree holds the lock?
  - `probe`, `withdb` and `all` refuse before anything runs unless both lock scripts sit beside gate.sh (M2 b).
  - The `cp` way is gone. The first `COBALT_ENV=dev` call comes only after the take exits 0 and `$WT/*/.env` shows this worktree's alone.
  - `all` runs OFFLINE (no `COBALT_ENV`) before the take, by design.
  - `test_m2_a_lock_never_free…` asserts no uv call, and `test_a_sibling_env_is_a_held_lock_and_no_uv_runs` (`02`'s side) still passes: the real take succeeds, the after-take proof sees two `.env`, and the gate exits 4.
- X1, can `--deploy` leak? It is set only by its own argument and refused outside `withdb` and `all`. Without it, `p1cmd=$PASS1` byte for byte (M3 b turns 4 tests red).
- X2 (M1): exactly two status lines are needed, `## <BRANCH>` and `??` plus the report's own path. A second untracked path fails (mutation 3). A modified tracked report fails (mutation 2). A build does not accept CHECK REPORT.
- Three suites: offline `3749 passed` (W (a)), live-note `146 passed` (W (e)), with-DB not run (DB: none). The ops suite: `603 passed, 1 xfailed`.
- `<F0>`, `<F1>`, `<F2>` and the lock take and release times: not run (DB: none).
- RESTARTS table: above. Records copied at PREFLIGHT: above.

## CONTINUE
next: CLOSE (done)

## DECISIONS
1. ASK DESK: PREFLIGHT's `status` row (BUILD-HUB: EXACTLY `## <BRANCH>`) read `## ops/adoption-scripts-b2-1003` plus `?? "docs/40 - DevDocs/reports/adoption-scripts-b2-build-2026-10-03.md"`. That second line is this report, which the hub's own `## REPORT` rule makes the first Write. This is adoption-hubs DECISION 2, the defect M1 fixes in `preflight.sh`. Safe default taken: went on, because the one extra line is the shape M1 accepts. Not his. [16:12 ET]
2. DECISION M6: the card's red-first proof `grep -c -F ".claude/ops" "docs/40 - DevDocs/prompts/STANDING-LIST.md" → 0` cannot reach 0 inside the row.
   - After the fix it reads `7`.
   - The remaining lines are not about the lock scripts' path. They are `--add-dir /Users/cobalt/.claude/ops` roots that stand on the real launch lines (`:54` §1, `:109` §3, `:192` §6). `02`'s A10 `:49` says that root "stays on each line". The other lines are the installed class-(a) spelling (`:36`), `02`'s own `:49`, and the desk's `desk-context.sh` and `desk-launch.sh` commands (`:107`, `:172`).
   - Changing those would edit launch-line strings and other sections, which the card's NOT IN THIS JOB fences out.
   - Safe default taken: built the row's "what" (§3, the lock scripts' sentence) exactly as O2 names it. The proof used is O2's own: `grep -c -F "for the two lock scripts"` → `0`.
   - Not his: the desk words the proof.

## RECORDS
- `test_pass1_db_only.py` taken as `44d3f246`'s (card M5). `02`'s `test_neither_hub_types_a_pass1_command` is not in it. Its two assertions are still pinned elsewhere: `test_the_hub_holds_no_gate_command_and_points_at_the_lists_file` in `test_gate.py` (BUILD-HUB `## W` holds no pass command and calls `gate.sh … all`), and the new STEP-G `all --deploy` test.
- M2 mutation b was first typed in a form that did not disable the guard (`&&`/`||` precedence; `50 passed`). It was redone as `|| true`, which went red. The test was not changed.
- `uv run cobalt jobs restarts` created `.venv` in this worktree on first use (gitignored).
- No lock take (DB: none). `.env` was never present in this worktree (PREFLIGHT, W (e)).
- The card's records, as re-read at PREFLIGHT: (1) the re-issue stacking on `6251baeb` holds (`git log --oneline -1`). (2) `DB: none` holds: 8 paths, all under `ops/`, `tests/ops/` or `docs/` (W (a0)). (3) the R113 FOR THE CHECK items are met (see `## FOR THE CHECK`).
- The L74 line: see `## L74`.
- **The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.**

BUILT · job: adoption-scripts-b · tip: b7eeb80c | on 6251baeb | migration: none | offline 3749/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0
