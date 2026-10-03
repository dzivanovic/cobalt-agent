# lock-relief — build report, 2026-10-03

## §0 Headline

All 7 rows built on `bb816d45`, tip `77d19438`. A G1 guard fails any test that reaches `cobalt_dev` without a `skipif` mark; `--db-only` keeps only marked tests in pass 1; `BUILD-HUB.md`, `CHECK-HUB.md` and `CARD.md` now carry the `DB: none` card. `DEPLOY-HUB.md` is untouched.
At W, the guard named 68 unmarked tests. They now carry the mark line, so pass 1 dropped from 704.70 s to 110.32 s (672 passed), and 672 + 3737 offline ≥ the 4405 the full pass 1 runs.
Suites on the tip: offline 3737/0 · with-DB 845/0 (672 + 173) · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · RESTARTS: none.
Six decisions, one for Dejan (R154's wording against the `tests/ops/` prefix). The others: a BASE red in `tests/ops` that would stop every `DB: none` build, 68 tests moved out of the offline run, a `cobalt_redactions` row committed by every pass 1, `connect_migration` not a door, and the CHECK-HUB stop-line literal.

## L74

None in a tool result. One system reminder at launch asked for a `Claude-Session:` commit trailer; it was not followed, and the commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (`## RECORDS`).

## AUTHORIZATION

Run at 06:03:04 EDT (`date`).

| check | command | exit / output |
|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | no output (no hit) |
| card placeholders | `grep -n -E "«FIL[L]" ".../2026-10-03/01-lock-relief-card.md"` | no output (no hit) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/01-lock-relief-card.md"` | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | no output |
| STANDING LIST R60 | `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` | `46:| R60 | 15:15 ET | **HIS RULING** (...) APPROVES \`STANDING-LIST.md\` once (\`4be06af0\`); ... | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md"` | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING R47 | `grep -n "^| R47 " ".../reports/cto-2026-10-02.md"` | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, ... | HIS RULING · APPROVED |` |
| R47 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md"` | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| RULING R154 | `grep -n "^| R154 " ".../reports/cto-2026-10-02.md"` | `161:| R154 | 17:29 ET | HIS RULING: a card with no \`src/\`, test, config or migration path takes no dev-DB lock at build + check (L68 narrowed there only); pass 1 under the lock = with-DB tests only; lands + measured 10-03; 2nd DB waits (...). | HIS RULING · APPROVED |` |
| R154 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R154 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md"` | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |

## PREFLIGHT

| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 06:03:04 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/lock-relief-1003` and `?? "docs/40 - DevDocs/reports/lock-relief-build-2026-10-03.md"` (this report, created first as REPORT says) |
| base | `git log --oneline -1` | 0 | `bb816d45 docs(report): deploy scripts-1002 — DEPLOYED deploy-2026-10-02-2, smoke GREEN` |
| branch on main checkout | `git -C /Users/cobalt/cobalt log --oneline -1 ops/lock-relief-1003` | 0 | `bb816d45 docs(report): deploy scripts-1002 — DEPLOYED deploy-2026-10-02-2, smoke GREEN` |
| no diff | `git diff --stat bb816d45` | 0 | (no output) |
| base stat | `git show --stat bb816d45` | 0 | `docs/40 - DevDocs/reports/deploy-2026-10-02-2.md | 89 ++++++++++++++++++++++--` / `1 file changed, 85 insertions(+), 4 deletions(-)` |
| no .env here | `ls /Users/cobalt/cobalt-wt/lock-relief-1003/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/lock-relief-1003/.env: No such file or directory` |
| .env anywhere | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no lock held) |
| hub files on main = base | `git -C /Users/cobalt/cobalt diff --stat bb816d45 -- BUILD-HUB.md CHECK-HUB.md CARD.md tests/cobalt/conftest.py` | 0 | (no output) |
| restarts | `uv run cobalt jobs restarts bb816d45..HEAD` | 0 | `docs/40 - DevDocs/reports/lock-relief-build-2026-10-03.md	A	DOCS	-` / `RESTARTS: none` (the untracked report only; no commit in range) |

THE CARD'S SYMBOLS:

| symbol | command | hit |
|---|---|---|
| `dev_db_tx` | `grep -n -F "def dev_db_tx" tests/cobalt/conftest.py` | `134:def dev_db_tx(monkeypatch):` |
| `fake_connect` | `grep -n -F "def fake_connect" tests/cobalt/conftest.py` | `162:    def fake_connect(dbname: str, *, side: db.Side, allow_prod: bool = False):` |
| `real_connect` | `grep -n -F "def real_connect" tests/cobalt/conftest.py` | `197:def real_connect():` |
| `_open` | `grep -n -F "def _open" tests/cobalt/conftest.py` | `209:    def _open(dbname: str = env.DEV_DB_NAME, *, side: db.Side):` |
| `REAL_CONNECT` | `grep -rln -F "REAL_CONNECT" tests/cobalt` | `conftest.py`, `test_s3_c2_experiments.py`, `test_legs_c2_db.py`, `test_fill_transaction_db.py`, `test_x5_tap_refresh_db.py` |
| `psycopg.connect` | `grep -rn -F "psycopg.connect" tests/cobalt` | text only: `conftest.py:7` (docstring), `test_db_credentials.py:11,48` (docstring; the test patches it), `test_tenancy.py:329,341` (message / comment) — no call |
| `migrated` fixtures | Grep `def \w*migrated\w*\(` in tests/cobalt | `radar_migrated_support.py:73:def migrated_radar(monkeypatch, dev_db_tx):`, `test_drc_store.py:232:def migrated(monkeypatch):` (and three test names containing the word) |
| `real_connect` users | `grep -rln -F "real_connect" tests/cobalt` | conftest, test_db_credentials, test_s3_c2_experiments, test_replay_runner, test_modelaccess_client, test_migrate_proof, test_env, test_archiver_append_store, test_voice_store, test_tenancy, test_archiver_migrations, test_radar_score_migration, test_radar_seam, test_cards_picks |
| `migrated` users | `grep -rln -F "migrated" tests/cobalt` | 26 files (test_drc_*_db / *_runs / *_store / *_experiments, test_radar_handicap_*, test_radar_panel, test_radar_store, test_tenancy, test_cards_picks, radar_migrated_support, test_radar_migrated_harness, test_drc_build_db) |
| `connect_migration` (not a card door) | `grep -rn -F "connect_migration" tests/cobalt` | real calls in test_p4_migrations:305, radar_migrated_support:78, test_radar_handicap_store:146, test_migrate_proof (many), test_stale_score_db:137, test_drc_store:233, test_voice_store:166, test_tenancy:546,573, test_archiver_migrations:447, test_radar_score_migration:300 → DECISION G1 |
| radar_panel mark | Read `tests/cobalt/test_radar_panel.py` 1216–1224 | `requires_db = pytest.mark.skipif(` … `@requires_db` / `@pytest.mark.usefixtures("migrated_radar")` on a function (no module mark) |
| session mark | Read `tests/cobalt/test_session.py` 410–416 | `requires_db = pytest.mark.skipif(` and `requires_dev_vault = pytest.mark.skipif(` |
| inline skips | Grep `pytest\.skip\(` in tests/cobalt, tests/taxonomy | test_cards_picks.py:388,401; radar_migrated_support.py:77; test_env.py:90; test_heartbeat_runner.py:712; test_voice_transcribe.py:43 |
| gate.sh reader | `grep -n -F "BUILD-HUB" ops/desk/gate.sh` | `104:hub="$dir/docs/40 - DevDocs/prompts/BUILD-HUB.md"`; Read 110–165: pass 1 = the one backticked line after the `- (c) ` item that begins `` `COBALT_ENV=dev uv run pytest `` |

`wc -l`: `tests/cobalt/conftest.py` 290 · `tests/conftest.py` 90 · `BUILD-HUB.md` 114 · `CHECK-HUB.md` 132 · `CARD.md` 138.
`tail -n 3 devdb-parallel-answer-2026-10-02.md` → last line `ANSWER WRITTEN — decisions: 4 · for Dejan: 3`.

THE CARD'S RECORDS, copied, with what was re-read:
- His ruling 2026-10-02 17:25 ET (R154): re-read above in AUTHORIZATION, row 161 of `cto-2026-10-02.md`, `HIS RULING · APPROVED`, commit `edd6f7aa`.
- Seams (1)–(5) settled by the brain (L72): not re-decided. (5) re-read: launch line in BUILD-HUB.md line 12 holds `"Bash(git -C * diff*)"` and `"Bash(git diff *)"`.
- This job is a with-DB job; it takes the lock as `main`'s hub says.
- Baseline for the gain measure (check `17`): offline `3784 passed, 673 skipped` 595.72 s; pass 1 `4383 passed, 7 skipped, 65 deselected, 3 xfailed` 709.60 s; pass 2 `171 passed` 220.14 s. Not re-read (another report); quoted beside mine at W.
- 57 files carry the skip: re-read with `grep -rlc -F "not (os.getenv(\"POSTGRES_HOST\") and os.getenv(\"POSTGRES_USER\"))," tests/cobalt tests/taxonomy` → 56 files with count 1 (54 test files + `stale_db_support.py` + `radar_migrated_support.py`); `test_vault_restore.py:38` carries the `COBALT_DB_USER` variant (57th); every `tests/taxonomy` file 0.
- Outside house set aside (R47): re-read above.
- After DEPLOYED, later cards carry `DB: none`: the desk's, not this build's.

## E0 BASELINE

On `bb816d45`, no file changed but this report.
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3792 passed, 675 skipped, 1 xfailed, 25 warnings in 578.68s (0:09:38)`; 0 failed, 0 errors.
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 24.96s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED

Red commit `0dcaeb12` `wip(lock-relief): red — G1, P1, P2 tests on bb816d45` (test files only, no `src/` or conftest edit).

OFFLINE `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_db_only_selection.py tests/ops/test_pass1_db_only.py` → `6 failed, 6 passed, 1 skipped, 23 warnings in 2.14s`. Each red and its first line:

| row | test | red's first line | the row's reason |
|---|---|---|---|
| G1 | `test_the_mark_finder_sees_a_skipif_on_the_function_the_class_and_the_module` | `AttributeError: module 'conftest' has no attribute 'offline_skip_marks'` | the helper does not exist |
| G1 | `test_the_mark_finder_sees_nothing_on_an_unmarked_test` | `AttributeError: module 'conftest' has no attribute 'offline_skip_marks'` | the helper does not exist |
| G1 | `test_the_guard_refuses_an_unmarked_item_and_passes_a_marked_one` | `AttributeError: module 'conftest' has no attribute 'require_offline_skip'` | the helper does not exist |
| P1 | `test_db_only_keeps_marked_three_ways_and_drops_unmarked` | `AttributeError: module 'conftest' has no attribute 'db_only_split'` | no such helper |
| P1 | `test_the_db_only_option_is_registered_and_off_by_default` | `ValueError: no option named '--db-only'` | no such option |
| P2 | `tests/ops/test_pass1_db_only.py::test_the_build_gate_pass1_holds_db_only_once_after_the_two_suites` | `AssertionError: assert 0 == 1` (`command.count(' --db-only')`) | the option is absent |

Green on BASE, as the card allows or as controls:
- `test_every_door_to_cobalt_dev_carries_an_offline_skip_mark` PASSED: the card's "RED on BASE only if a door is unmarked today" — no door is unmarked today, so no file gains a mark at E2. Its red is shown at E3 by mutation.
- `test_the_static_reader_finds_each_door_unmarked`, `test_the_static_reader_accepts_each_mark_form`, `test_the_autouse_open_of_dev_db_tx_is_not_a_door` PASSED: they test the static reader inside the new test file itself; red shown at E3 by mutation.
- `test_the_deploy_gate_pass1_runs_without_db_only` PASSED (negative control: DEPLOY-HUB STEP-G holds no `--db-only`); `test_the_two_pass1_commands_differ_by_the_option_alone` PASSED (on BASE both commands are identical; it pins seam (1)); red shown at E3 by mutation.

WITH-DB, ONE lock take:
- take `sh /Users/cobalt/.claude/ops/take-devdb-lock.sh lock-relief-1003 90` (started 06:19, `date` 06:19:27 EDT) → `lock taken: lock-relief-1003`, exit 0. `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  3 06:19 /Users/cobalt/cobalt-wt/lock-relief-1003/.env` (one line, ours).
- `<FP>` → `<F0>` = `664	35	272c95bbb12241e3611e4b36326ccf87`.
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables probed, the 0014+ tables (`drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns`) absent (`-`), no `CHANGED`, `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` — `cobalt_dev` at `0013`. NO forward.
- `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_db_only_selection.py` → `6 failed, 4 passed, 8 warnings in 1.48s`; the with-DB red: `FAILED tests/cobalt/test_db_only_selection.py::test_an_unmarked_reach_through_the_suite_factory_fails_with_the_guard_message` — `test_db_only_selection.py:568: AttributeError: module 'conftest' has no attribute 'require_offline_skip'` (the helper does not exist).
- `<FP>` again → `664	35	272c95bbb12241e3611e4b36326ccf87` = `<F0>`.
- release `sh /Users/cobalt/.claude/ops/release-devdb-lock.sh lock-relief-1003` → `lock released`; `ls /Users/cobalt/cobalt-wt/lock-relief-1003/.env` → `No such file or directory`; 06:20:02 EDT. `.env: removed, proven gone (E2)`.

RUN ROW R0 (read only; each a fixed string, quoted whole):
- `grep -rn -F "with-DB" ops/desk` →
  `ops/desk/gate.sh:38:# only: \`offline <p>/0\`, \`with-DB <d>/0\` (pass 1 + pass 2), \`live-note <l>/0\`, every SKIPPED line`
  `ops/desk/gate.sh:450:    say "with-DB $((p1 + p2))/0"`
  `ops/desk/desk-launch.sh:100:#     takes the lock at its with-DB steps through take-devdb-lock.sh, and waits for it there;`
  `ops/desk/desk-launch.sh:570:        [ ! -e "$f" ] || refuse "with-DB launch refused: the cobalt_dev lock is held ($f) (L76)"`
  `ops/desk/desk-launch.sh:580:    refuse "with-DB launch refused: the cobalt_dev lock is held by ${holder:-unknown} ($WT/.cobalt_dev.lock) (L76)"`
  `ops/desk/desk-launch.sh:866:    note="reminder: the build takes the cobalt_dev lock only at its with-DB steps and waits for it there (L76, R20); no deploy launch while it holds it"`
  `ops/desk/desk-launch.sh:870:    note="reminder: one Grok hub at a time (L15); no other house hub running; the check takes the cobalt_dev lock only at its with-DB steps and waits for it there (L76, R20); measure the session at its stop line (desk-context.sh)"`
  `ops/desk/desk-launch.sh:875:    note="reminder: no desk commit on main until the stop line; builds and checks may launch, their with-DB steps wait for the lock the gate holds to its stop line (L76, R20); a hub hung after its first bootout: stop it and at once run this script again with STEP-D0"`
  `ops/desk/take-devdb-lock.sh:3:# 2026-10-01 R20; card 07 devdb-lock). A with-DB step of a build, a check or a deploy gate runs it`
- `grep -rn -F "F2 = F0" ops/desk` →
  `ops/desk/gate.sh:39:# of pass 1, \`cobalt_dev: <level> — F2 = F0\`, \`.env: removed\`, \`log: <path>\`; on a red, the first`
  `ops/desk/gate.sh:319:        [ "$rrc" -eq 0 ] || say "the rollback exited $rrc; F2 = F0 (log)"`
  `ops/desk/gate.sh:448:    say "cobalt_dev: $level — F2 = F0"`
- `grep -rn -F "cobalt_dev: 0013" ops/desk` → no output.
- `grep -n -F "with-DB" ".../DEPLOY-HUB.md"` → lines 3, 15, 62, 99, 100, 107, 185 (text of the deploy's own with-DB gate: `MODEL:` line, `THE DESK WHILE YOU RUN`, P4, `WHO KEEPS THE TREE STATE CURRENT`, (a0), (c)'s `plus one --deselect for each with-DB test a build of this set deselected in its own pass 1 (its build report names them)`, the `DEPLOYED` stop-line shape `gate: offline <p>/0 · with-DB <d>/0 · live-note <l>/0`).
- `grep -n -F "F2 = F0" ".../DEPLOY-HUB.md"` → lines 55 (THE ONE RESUME: `the rollback to 0013 when dev forward: APPLIED has no F2 = F0 after it`), 112 (G (f) `Record cobalt_dev: 0013 — F2 = F0`), 180 (`## RECORDS`: `cobalt_dev: 0013 (F2 = F0)`) — all the deploy gate's own lock.
- `grep -n -F "cobalt_dev: 0013" ".../DEPLOY-HUB.md"` → lines 112 and 180 (the same two, the deploy's own).
- `grep -n -F "with-DB" ".../CHECK-HUB.md"` → lines 8, 66, 69, 106 (lock prose: the check takes the lock only at its with-DB steps; PREFLIGHT THE LOCK; PROVEN BY FIRST REAL USE; `## 4` a with-DB test inside ONE lock take).
- `grep -n -F "F2 = F0" ".../CHECK-HUB.md"` → line 112 (`## 6`: one commit or more → `## W` whole, `cobalt_dev: 0013 — F2 = F0`).
- `grep -n -F "cobalt_dev: 0013" ".../CHECK-HUB.md"` → lines 112 and 129 (the pass-1 stop-line shape `· cobalt_dev: 0013 · .env: removed ·`).
- Readers of a build stop line, `grep -rn -F "BUILT" ops/desk`: `desk-watch.sh:27` (`re='^(BUILT|FAILED)'`), `card-fill.sh:66` (`BUILT · job: (\S+) · tip: ([0-9a-f]{8})`) and `:70` (`self-check: 3 of 3`), `desk-launch.sh:714` (`"BUILT · job: $job · tip: $tip"`), `preflight.sh:173` (`"BUILT · job: $job · tip: $tip"*"self-check: 3 of 3"*`), `desk-done.sh:21` (`^BUILT`). None parses `with-DB`, `cobalt_dev:` or `.env:`.
- `desk-launch.sh` build/check `lock_free` runs only with a resume step (`grep -n -F "lock_free" ops/desk/desk-launch.sh` → `676:    [ -z "$step" ] || lock_free`, `733:    [ -z "$step" ] || lock_free`; 774 and 826 are the deploy and devfix branches).
→ No reader on this tree refuses or misreads a build stop line carrying `with-DB 0/0 | cobalt_dev: not taken`, or a report with no `cobalt_dev: 0013 — F2 = F0` line: `gate.sh` writes those strings, never reads them from a report; the DEPLOY-HUB and CHECK-HUB hits are each hub's own lock steps. DECISION R0: none (recorded under `## DECISIONS`, with the CHECK-HUB stop-line literal named for X4).

## E3 THE ROWS

Commit `377c83b2` `feat(lock-relief): offline-skip guard, --db-only pass 1, the DB: none card (G1, P1, P2, H1, H2, H3; L3, L68, L76)`: `tests/cobalt/conftest.py`, `tests/cobalt/test_db_only_selection.py`, `BUILD-HUB.md`, `CHECK-HUB.md`, `CARD.md` (151 insertions, 10 deletions). No `src/` file, no `ops/desk/` file, `DEPLOY-HUB.md` untouched. No DevDocs module line: no `src/cobalt` module changed, and `docs/40 - DevDocs/cobalt/` has no page for the test conftest (`grep -rln -F "conftest" "docs/40 - DevDocs/cobalt"` → `prefill/trade_note.md`, `env.md`, `session/__init__.md` only, none a page of it).

**G1 + P1** (`tests/cobalt/conftest.py`): `offline_skip_marks(item)` = `item.iter_markers(name="skipif")` (own, class, module, the ONE reading both rows use, L3); `require_offline_skip(item)` raises `with-DB test without an offline skip mark: <nodeid>`; `db_only_split(items)`; autouse `offline_skip_guard` records each refused reach and fails the test at teardown (a store may swallow the error); `fake_connect` (inside `dev_db_tx`) and `_open` (inside `real_connect`) call the guard first. `dev_db_tx`'s own open is not guarded.
- P1, WHERE: `pytest_addoption` and `pytest_collection_modifyitems` sit in `tests/cobalt/conftest.py`, beside the helper they share (L3: `tests/conftest.py` cannot import it; conftest modules are not importable by name). The pass-1 command names `tests/cobalt`, so this conftest is an initial conftest and the option is registered before parsing; `pytest_collection_modifyitems` is a session-wide hook and sees `tests/taxonomy` items too. Proof: `uv run pytest -q --collect-only -p no:cacheprovider tests/cobalt tests/taxonomy --db-only` → `680/4478 tests collected (3798 deselected) in 1.05s`, 2 of them `tests/taxonomy/` items (`grep -c -F "tests/taxonomy/"` → `2`). A run naming no `tests/cobalt` path refuses `--db-only` as an unknown argument (L1).
- Static doors (`test_db_only_selection.py`, an `ast` reader): a test module's test is a door user when it (or a helper / fixture it calls or requests, transitively) names `REAL_CONNECT`, calls `psycopg.connect`, defines a fixture `migrated` / `migrated_<x>`, requests one (argument, `usefixtures`, `getfixturevalue`), or requests a conftest fixture that is a door user (`real_connect`; `dev_db_tx` excluded). Helper modules and `conftest.py` are read through the modules that import them. Accepted marks: an inline `pytest.mark.skipif(...)`, a name bound to one in the module or imported from a helper module (also `alias.name`, star imports), on the test, its class (decorator or class `pytestmark`) or the module `pytestmark` (single or list). `migrated_<x>` read as `migrated` (the card's READ names `radar_migrated_support.py`'s `migrated_radar` as a `migrated` fixture).
- Static door test on the tree: PASSED with no edit → no `tests/cobalt/` file gained a mark line.
- Test-form repair (said, per E2): the constructed-items fixture first used `getmodulecol(...).collect()`, which returns class nodes; changed to `makepyfile` + `genitems`. The assertions did not change. Their E2 red (`AttributeError ... offline_skip_marks`) came before the fixture mattered; their red against the fix is the M-G1a mutation below.
- Added at E3 (each shown red by mutation below): `test_with_db_only_a_run_deselects_every_unmarked_item`, `test_without_db_only_a_run_keeps_every_item` (the hook, an inner run with THIS conftest as plugin), `test_a_reach_a_store_swallowed_still_fails_the_test_at_teardown`, `test_an_unmarked_open_through_real_connect_is_refused_before_any_connection` (the `_open` door, refused before `REAL_CONNECT`).

**P2** (`BUILD-HUB.md` `## W` (c)): pass-1 command `… tests/cobalt tests/taxonomy --db-only --deselect …`, nothing else changed (pinned by `test_the_two_pass1_commands_differ_by_the_option_alone`); label `PASS 1 at 0013, the with-DB tests only (--db-only; the rest ran in (a))`; sentence added to (c)'s GATE line. `DEPLOY-HUB.md` not edited.

**H1 / H2 / H3** proofs, one `grep -n -F` each, one hit each:
| row | string | hit |
|---|---|---|
| H1 (1) | `takes no lock at all: PREFLIGHT runs no lock probe` | `BUILD-HUB.md:42` (last line of `## THE LOCK`) |
| H1 (2) | `A "DB: none" CARD ONLY` | `BUILD-HUB.md:85` (first item of `## W`) |
| H1 (3) | `Not for a "DB: none" card. NO LOCK PROBE` | `BUILD-HUB.md:56` |
| H1 (4) | `with-DB 0/0 \| cobalt_dev: not taken \| .env: removed` | `BUILD-HUB.md:115` |
| H1 (5) | `not run (DB: none)` | `BUILD-HUB.md:108` (`## FOR THE CHECK` in CLOSE: the with-DB summary, `<F0>`/`<F1>`/`<F2>`, the lock times; PRE-STOP SELF-CHECK asks for none of the three) |
| P2 | `the with-DB tests only (--db-only; the rest ran in (a))` | `BUILD-HUB.md:88` |
| P2 | `runs without --db-only, on purpose; a TREE STATE row adds its deselects to both.` | `BUILD-HUB.md:90` |
| H2 (1) | `FAILED PREFLIGHT: the card says DB: none but the diff holds` | `CHECK-HUB.md:66` |
| H2 (2) | `is not made: it goes under` | `CHECK-HUB.md:112` |
| H3 | `the job takes no` | `CARD.md:23` (row after `TREE STATE`) |
H2 (3) ("a finding's with-DB test (`## 4`) still takes one lock, as written") is a statement, not a new sentence: `CHECK-HUB.md:106` already says it; no edit. H3: `grep -n -F "TREE STATE" ops/desk/desk-launch.sh` → `490:    case "$(field "TREE STATE")" in`, `492:        *) refuse "incomplete card: TREE STATE must be 'unchanged' or 'row <id>'" ;;`; `field()` (`desk-launch.sh:446-448`) reads named keys only and nothing refuses an unknown key → no DECISION H3.

THE MUTATIONS (each made and undone with Edit; first failing line quoted):
| id | change | tests run | result |
|---|---|---|---|
| M-G1a | `offline_skip_marks` reads `skipif_MUTATED` | the G1/P1 file | `5 failed, 6 passed, 1 skipped` — `assert set() == {'TestMarkedI...n_the_module'}` (mark finder ×2, `db_only_split`, the hook run, the guard: `with-DB test without an offline skip mark: test_module_mark.py::test_marked_on_the_module`) |
| M-P1a | the hook does not deselect (`pass`) | the G1/P1 file | `1 failed, 10 passed, 1 skipped` — `test_with_db_only_a_run_deselects_every_unmarked_item`: extra `'test_skip_is_not_skipif'`, `'test_another_mark_only'`, `'test_unmarked'` |
| M-P1b | the hook ignores the option (`if False:`) | the G1/P1 file | `1 skipped, 11 deselected in 0.02s` — the mutated hook deselects this file's own unmarked tests in the outer run, so `test_without_db_only_a_run_keeps_every_item` cannot run; any gate run would collect only the marked tests and show it |
| M-P1c | the option registered as `--db-only-MUTATED` | the G1/P1 file | `INTERNALERROR> ValueError: no option named '--db-only'`, exit 3 |
| M-G1c | `@requires_db` removed from `test_radar_migrated_harness.py:72` | static door test | `1 failed` — `Left contains one more item: 'test_radar_migrated_harness.py::test_a_migrated_radar_test_holds_one_transaction_on_cobalt_dev'` |
| M-G1c2 | `test_x5_tap_refresh_db.py` `pytestmark = [pytest.mark.integration]` | static door test | `1 failed` — `Left contains 2 more items, first extra item: 'test_x5_tap_refresh_db.py::test_x5_a_tap_committed_while_the_refresh_waits_keeps_its_numbers'` (a REAL_CONNECT door) |
| M-G1d | `_is_migrated` returns `False` | the G1/P1 file | `1 failed` — `test_the_static_reader_finds_each_door_unmarked`: `At index 4 diff: 'test_doors.py::test_requests_real_connect' != 'test_doors.py::test_requests_migrated'` |
| M-G1e + M-G1f | imported skipif names ignored; `NOT_A_DOOR = set()` | the G1/P1 file | `3 failed` — static door `Left contains 158 more items, first extra item: 'test_drc_build_db.py::test_a_placed_day_builds_the_note_and_its_build_rows'`; accept-form `'test_marked.py::test_uses_a_support_fixture'`; autouse `['test_plain.py::test_plain'] == []` |
| M-P2a | ` --db-only` removed from BUILD-HUB pass 1 | `tests/ops/test_pass1_db_only.py` | `1 failed, 2 passed` — `assert 0 == 1` |
| M-P2b | pass 1 `--db-only -x` | same | `1 failed, 2 passed` — `test_the_two_pass1_commands_differ_by_the_option_alone` |
| M-P2c (negative control) | DEPLOY-HUB STEP-G pass 1 gains `--db-only` | same | `2 failed, 1 passed` — `assert '--db-only' not in 'COBALT_ENV=...efresh_db.py'` |
| M-G1b (with-DB) | `fake_connect` no longer calls the guard | the with-DB test | `1 failed` — `Failed: DID NOT RAISE <class 'AssertionError'>` (line 602) |
| M-G1g (with-DB take) | the guard's teardown never fails | the teardown test | `1 failed` — `<TestReport 'test_swallowed.py::test_swallows_the_refusal' when='teardown' outcome='passed'>.failed` is False |
| M-G1h (with-DB take) | `_open` no longer calls the guard | the `_open` test | `1 failed` — `assert ['passed'] == ['failed']` |
After the undo: `git diff --stat` → only the five row files (`DEPLOY-HUB.md`, `test_radar_migrated_harness.py`, `test_x5_tap_refresh_db.py` absent: back as they were).

The with-DB mutations ran in ONE extra lock take (a `## RECORDS` line): taken 06:35:17 EDT (`lock taken: lock-relief-1003`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → ours alone); `<FP>` `664	35	272c95bbb12241e3611e4b36326ccf87` before and after; the file green inside it `COBALT_ENV=dev uv run pytest -q -rA … tests/cobalt/test_db_only_selection.py` → `12 passed`, then `13 passed`, then `14 passed` as the two tests were added (with-DB test PASSED); released 06:36:34 EDT `lock released`, `.env` → `No such file or directory`. `.env: removed, proven gone (E3)`.

GREENS after the undo, offline: `uv run pytest -q -rs -p no:cacheprovider --color=no --show-capture=no tests/cobalt/test_db_only_selection.py tests/ops/test_pass1_db_only.py tests/ops/test_gate.py` → `47 passed, 1 skipped, 27 warnings in 13.82s` (the skip: the with-DB test, `Postgres env settings not available`). Before the four E3 additions, all of `tests/ops` with the hub edits: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_db_only_selection.py tests/ops` → `1 failed, 479 passed, 1 skipped, 1 xfailed in 388.43s`; the one red, `tests/ops/test_order_open.py::test_every_block_carries_its_facts_and_nothing_changes` (`assert 'sol: OUT — R... or directory' == 'not probed'`), repeats alone (`1 failed, 13 passed in 199.73s`) and is the BASE's own: `git diff --stat bb816d45 -- ops tests/ops/test_order_open.py` → empty; `ops/desk/house-probe.sh` came with `8f3c4876` / `c1eab436` before BASE, and `order-open.sh` prints `not probed` (`:135`) only when no `house-probe.sh` sits beside it (`:15`: "the output of house-probe.sh beside this script when that file exists, else `not probed`") → DECISION 1.

## RESTARTS

`uv run cobalt jobs restarts bb816d45..HEAD` (HEAD `377c83b2`), the table WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/lock-relief-build-2026-10-03.md	A	DOCS	-
tests/cobalt/conftest.py	M	test/documentation; no resident	-
tests/cobalt/test_db_only_selection.py	A	test/documentation; no resident	-
tests/ops/test_pass1_db_only.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row; nothing added to `configs/cobalt/jobs.yaml`.

## W THE THREE SUITES

### W attempt 1 — on `377c83b2`, stopped at P2's PROOF (before (c2); nothing applied)
- (a) `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3805 passed, 676 skipped, 1 xfailed, 37 warnings in 567.74s (0:09:27)`.
- (e) (`.env` absent: `ls` → `No such file or directory`) `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.23s`; skip `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`.
- (b) take 06:48:17 EDT `lock taken: lock-relief-1003`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → ours alone; `<F0>` = `664	35	272c95bbb12241e3611e4b36326ccf87`; `--proof-only` → the same 36-table table as E2, 0014+ tables `-`, no `CHANGED`, `NOTHING WAS APPLIED` → `0013`.
- P2 PROOF, the BASE's pass-1 command byte for byte (no `--db-only`), G1 in the tree: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip … --deselect tests/cobalt/test_x5_tap_refresh_db.py` (the 15 deselects of `main`'s line) → `1 failed, 4404 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings, 68 errors in 705.52s (0:11:45)`. Every error is a teardown error `Failed: with-DB test without an offline skip mark: <nodeid>` (the guard's record: these tests reach `fake_connect` and catch the AssertionError), and the one failure `test_aset_web.py::TestDefect3TwoDistinctHandlers::test_entry_dirty_machinery_fully_removed` (`assert 'entry_dirty' not in '<!doctype h...'`, the page rendering the guard's message that holds the node id) carries the same teardown line. 68 node ids in 12 files (`grep -o -E "E +Failed: with-DB test without an offline skip mark: tests/[^ ]+"` over the run's output): `test_aset_web.py` 29 items (28 defs), `test_drc_settings.py` 12 items (8 defs), `test_s3_c3_panel_offline.py` 9, `test_voice_plan.py` 5 items (1 def), `test_fill_c1_offline.py` 4, `test_modelaccess_client.py` 2, `test_s3_c4_trade_note_offline.py` 2, `test_drc_d3_fix_r2.py` 1, `test_drc_d4_fix_r1_runs.py` 1, `test_radar_panel_cards.py` 1, `test_settings_optional.py` 1, `test_voice_web.py` 1. The 7 SKIPPED: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py:266`, `test_s3_c4_experiments.py:95`, `test_catalyst.py:365`, `test_predicate.py:262`.
- `<FP>` → `664	35	272c95bbb12241e3611e4b36326ccf87` = `<F0>`; (c2) not reached, nothing applied, so no (f). Released 07:01:27 EDT `lock released`; `.env` → `No such file or directory`. `.env: removed, proven gone (W attempt 1)`.
- THE FIX, as P2 says ("a red that is G1's message is fixed by the mark line (row G1's files)"): one decorator line above each of the 59 named defs, `@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")` (pytest's string condition; `os` is in its evaluation namespace, so no import line is added). `git diff --stat` → `12 files changed, 59 insertions(+)`, no deletion. Offline check of the 12 files + the G1 file → `304 passed, 71 skipped, 13 warnings in 20.55s`. Second fix commit `77d19438` `fix(lock-relief): the offline skip mark on the 68 tests G1's guard named at the W proof run (G1, P2; L68)`. These 68 items now run in pass 1 (marked) and no longer offline → DECISION 2. RESTARTS again (`bb816d45..HEAD` at `77d19438`) → the table above plus the 12 marked files, each `test/documentation; no resident	-`; `RESTARTS: none`. One more lock take follows (a `## RECORDS` line); W again from (a).

### W attempt 2 — on `<tip>` = `77d19438`
- (a) OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3737 passed, 744 skipped, 1 xfailed, 36 warnings in 564.47s (0:09:24)` → `<p>` = 3737 (3805 − 68 passed, 676 + 68 skipped). Tests this build adds: `tests/cobalt/test_db_only_selection.py` (14 offline + 1 with-DB) and `tests/ops/test_pass1_db_only.py` (3, run in `tests/ops`, not in (a)).
- (e) LIVE-NOTE (`.env` absent, `ls` → `No such file or directory`) → `146 passed, 1 skipped, 15 warnings in 26.19s` → `<l>` = 146; skip `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`, none naming `COBALT_LIVE_VAULT_ROOT`.
- (b) take 07:14:43 EDT `lock taken: lock-relief-1003`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  3 07:14 /Users/cobalt/cobalt-wt/lock-relief-1003/.env` alone. `<F0>` = `664	35	272c95bbb12241e3611e4b36326ccf87`. `--proof-only` → 36 tables, 0014+ tables `-`, no `CHANGED`, `NOTHING WAS APPLIED` → `0013` (`cobalt_redactions 244` there; 243 at attempt 1 → DECISION 3).
- (c) PASS 1, the command row P2 wrote, executed WHOLE (no deselect added: this build's one with-DB test needs no migration above `0013`):
  `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --db-only --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py`
  → `672 passed, 7 skipped, 3801 deselected, 2 xfailed, 12 warnings in 110.32s (0:01:50)` → `<d1>` = 672. The 7 SKIPPED: `test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev`; `test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged`; `test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`; `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`; `test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read`; `test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft`; `test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof` (the same 7 as the full pass 1).
- P2 PROOF on `77d19438`, the BASE's pass-1 command byte for byte (as in attempt 1) → `4405 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings in 704.70s (0:11:44)`; 0 failed, 0 errors: no test reaches the database unmarked. ORDER, as it happened: in this take (c) ran first, then the PROOF; the card orders the PROOF first. Neither run changes the database and both ran in the one take at `0013` (a `## RECORDS` line).
- THE COUNTS (P2): new pass-1 passed 672 + offline passed 3737 = 4409 ≥ full pass-1 passed 4405 → no shortfall, no DECISION P2. Seconds: full pass 1 704.70 s → `--db-only` pass 1 110.32 s. Beside the card's baseline (check `17`): offline `3784 passed, 673 skipped` 595.72 s / pass 1 `4383 passed, 7 skipped, 65 deselected, 3 xfailed` 709.60 s / pass 2 `171 passed` 220.14 s; this build: offline `3737 passed, 744 skipped` 564.47 s / pass 1 `672 passed, 7 skipped, 3801 deselected, 2 xfailed` 110.32 s / pass 2 `173 passed` 219.90 s.
- (c2) FORWARD `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `0001` … `0013`, then `0014_radar_handicap.sql`, `0015_shadow_agreement_stale.sql`, `0016_drc.sql`, `0017_voice_turns.sql`, `0018_drc_stated_books.sql`, `0019_drc_events.sql`, `0020_drc_build_kinds.sql`, `0021_legs.sql`, `0022_prediction_records.sql` applied in `FORWARD` order (no migration of this build); every pre-existing table `OK`, the nine 0014+ tables `CREATED`, `content UNCHANGED on every table`, no `CHANGED`. **dev forward: APPLIED 07:29:48 EDT.** `<F1>` = `893	44	126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2, byte for byte (nothing deselected for this build): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip … tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones` (the line at `BUILD-HUB.md` W (c3), unchanged) → `173 passed, 1 deselected, 5 warnings in 219.90s (0:03:39)` → `<d2>` = 173. `<d>` = 672 + 173 = 845. This build's one with-DB test sits in pass 1 (it needs no migration): 0 failed there, and PASSED by name in E3's extra take (`PASSED tests/cobalt/test_db_only_selection.py::test_an_unmarked_reach_through_the_suite_factory_fails_with_the_guard_message`).
- (c3r) the build's with-DB tests write no `aset_sizings` row and no constructed ticker (the one with-DB test calls `db.connect` and nothing else), so there is no ticker list to read; not run.
- (f) ROLLBACK `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0022` … `0014` `.rollback.sql`, newest first; the nine tables `DROPPED`, every other table `OK`, `content UNCHANGED on every table`. `<F2>` = `664	35	272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field. **cobalt_dev: 0013 — F2 = F0.** Release 07:34:14 EDT `lock released`; `ls /Users/cobalt/cobalt-wt/lock-relief-1003/.env` → `No such file or directory`. `.env: removed, proven gone (W attempt 2)`.
- (c4) not run: this build adds no migration.

## PRE-STOP SELF-CHECK

(1) "Every added or changed test shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten." — E2 reds: the five helper/option tests (`AttributeError … offline_skip_marks` / `require_offline_skip` / `db_only_split`, `ValueError: no option named '--db-only'`), the with-DB test (`AttributeError … require_offline_skip`, line 568), P2's build test (`assert 0 == 1`). E3 mutation reds: M-G1a (mark finder ×2, split, hook run, guard), M-P1a (hook-with-option), M-P1c (option), M-G1c / M-G1c2 (static door), M-G1d (finds-each-door), M-G1e/f (accepts-each-form, autouse-not-a-door), M-P2a/b/c (the three P2 tests), M-G1b (with-DB test `DID NOT RAISE`), M-G1g (teardown test), M-G1h (`_open` test). `test_without_db_only_a_run_keeps_every_item`: its mutation (M-P1b) deselects the test itself in the outer run (`1 skipped, 11 deselected`), so it cannot show a red. It stays as written, because any run under that mutation collects only marked tests and shows it at once (named here, not rewritten). The 59 mark lines change no assertion: each named test was red at the PROOF run (68 teardown errors, quoted) and green after (PROOF on `77d19438`: 0 failed).
(2) "Every entry path of each rule pinned by a test." — the guard's callers (`grep -n -F "_guarded_reach(request.node, offline_skip_guard)" tests/cobalt/conftest.py` → `241` in `fake_connect`, `289` in `_open`): `fake_connect` by the with-DB test, `_open` by the inner-run test; a swallowed reach by the teardown test; the mark forms (function, class decorator, class `pytestmark`, module `pytestmark`) by the mark-finder tests; the hook with and without `--db-only` by the two inner-run tests; `tests/taxonomy` items reaching the hook by the collect-only count (`2` taxonomy items kept). The static doors: `REAL_CONNECT`, `psycopg.connect`, `migrated` / `migrated_<x>` defined, requested by argument / `usefixtures` / `getfixturevalue`, a helper chain, a local fixture chain, a support-module fixture, conftest `real_connect`, a class method, by `test_the_static_reader_finds_each_door_unmarked`. NOT pinned: `db.connect_migration` called directly (PREFLIGHT's grep, ~10 files) — not a door the card names → DECISION 4. The hub sentences have no test (the card's rows say so); each has its one-hit grep.
(3) "Every `file:line`, count and quote in the report re-read from tool output at the tip." — re-run at `77d19438`: `git log --oneline bb816d45..HEAD` (three commits, quoted under FOR THE CHECK); `git diff --stat 377c83b2 77d19438 -- docs tests/cobalt/conftest.py tests/cobalt/test_db_only_selection.py tests/ops` → empty (the hub lines 42, 56, 85, 88, 90, 108, 115, `CHECK-HUB.md` 66, 112, `CARD.md` 23 stand as grepped at E3); `grep -n -F "tests/cobalt tests/taxonomy --db-only --deselect" BUILD-HUB.md` → line 89, the command executed at (c); the guard's two call sites (241, 289); `grep -c -F "reaches cobalt_dev (lock-relief G1)"` over the 12 marked files → 28, 8, 9, 4, 2, 2, 1, 1, 1, 1, 1, 1 = 59.

## FOR THE CHECK

- `bb816d45..77d19438`: `0dcaeb12 wip(lock-relief): red — G1, P1, P2 tests on bb816d45` · `377c83b2 feat(lock-relief): offline-skip guard, --db-only pass 1, the DB: none card (G1, P1, P2, H1, H2, H3; L3, L68, L76)` · `77d19438 fix(lock-relief): the offline skip mark on the 68 tests G1's guard named at the W proof run (G1, P2; L68)`. The report commit sits above them.
- Per row: reds under `## E2 RED`; mutations and greens under `## E3 THE ROWS`; the PROOF red and its fix under W attempt 1; R0's output WHOLE under `## E2 RED`.
- Executed commands and summaries: under `## W THE THREE SUITES` (both attempts).
- Fingerprints: E2 take `<F0>` = `<F>` after = `664	35	272c95bbb12241e3611e4b36326ccf87` (06:19:27 → 06:20:02); E3 extra take the same before and after (06:35:17 → 06:36:34); W attempt 1 `<F0>` = after (06:48:17 → 07:01:27, no forward); W attempt 2 `<F0>` `664	35	272c95bb…`, `<F1>` `893	44	126f2d6983fa59f9d0eaaff7da7dd29c`, `<F2>` `664	35	272c95bbb12241e3611e4b36326ccf87` (07:14:43 → 07:34:14).
- RESTARTS: the table under `## RESTARTS` and its re-run at `77d19438` (W attempt 1): `RESTARTS: none`.
- Records copied at PREFLIGHT: under `## PREFLIGHT`.
- The check's asks, from what this build ran: X1 — `db.connect_migration` is not a static door (DECISION 4); the runtime guard named 68 unmarked reaches that no static door saw (web stores reached through `fake_connect`). X2 — the PROOF's 4405 passed vs 672 + 3737 = 4409. X3 — not run by this build (no `DB: none` card exists yet); the check's. X4 — `CHECK-HUB.md:129`'s pass-1 stop-line shape still carries `cobalt_dev: 0013` for a `DB: none` check (DECISION 6). X5 — R0: no reader refuses (under `## E2 RED`).

## CONTINUE

next: none — the build is closed; the desk verifies the artifact and launches the check (`CHECK-HUB.md`, same card).

## DECISIONS

1. `tests/ops/test_order_open.py::test_every_block_carries_its_facts_and_nothing_changes` is red on BASE (`assert 'sol: OUT — R... or directory' == 'not probed'`): `ops/desk/house-probe.sh` now sits beside `order-open.sh`, which then probes instead of printing `not probed`. This job touches neither file. It matters now because H1's (a0) runs all of `tests/ops` for every `DB: none` build, so each such build would end `FAILED` at W until it is fixed. Safe default taken: not fixed (outside the rows, `ops/desk/` fenced). The desk cards the fix before the first `DB: none` card.
2. Following P2 ("a red that is G1's message is fixed by the mark line"), 68 test items (59 defs in 12 files) now carry an offline skip mark and run only with the database, in pass 1. That includes 15 defs in three files named `*_offline.py` (`test_fill_c1_offline.py` 4, `test_s3_c3_panel_offline.py` 9, `test_s3_c4_trade_note_offline.py` 2). The offline suite drops from 3805 to 3737 passed. Each of these tests reaches `cobalt_dev` through `fake_connect` in pass 1 and catches the refusal (the web routes swallow errors), so offline they pass on a code path that pass 1 does not take. Safe default taken: marked as the card says, no assertion touched. Whether those 68 should instead stop reaching the database (a store stub) is a new card's question.
3. Pass 1 commits rows to `system.cobalt_redactions` on `cobalt_dev` outside the suite's rollback: one `mattermost` / `jwt` row per full pass-1 run (`SELECT id, ts, channel, pattern, hits FROM cobalt_redactions ORDER BY id DESC LIMIT 3` → ids 2165 at 2026-10-03 10:52:04 UTC, inside W attempt 1's PROOF run; 2154 and 2141 on 2026-10-02, before this job). The count went 243 → 244 → 246 across this build's three pass-1 runs. `<FP>` and (c3r) do not see rows. Safe default taken: nothing deleted (no string allows it), not traced (outside the rows). The desk owns the leak.
4. G1's static doors are the card's three (REAL_CONNECT, `psycopg.connect`, the `migrated` fixtures). `db.connect_migration` is called directly in about ten test files (PREFLIGHT's grep) and no static door covers it; the runtime guard does not see it either. Today each of those calls sits in a marked test or a `migrated` fixture (the static door test is green, and so is the PROOF). Safe default taken: not widened (THE ROWS). This is CHECK ASK X1's.
5. FOR DEJAN — R154's text (`cto-2026-10-02.md:161`): "a card with no `src/`, test, config or migration path takes no dev-DB lock". The card's `DB: none` allow list, settled by the brain as seam (2), includes `tests/ops/`, which is a test path. Built as the card says (L72, not re-decided). Safe default taken: the card's three prefixes. Whether `tests/ops/` belongs in the class is his to confirm.
6. `CHECK-HUB.md:129`, the pass-1 `CHECK DONE` stop-line shape, still prints `cobalt_dev: 0013 · .env: removed` for every check, including a `DB: none` check that never takes the lock. H2 says "change no other sentence", so it was not edited. No script reads that field (R0). Safe default taken: unchanged. If the desk wants it, a `DB: none` sentence for the check's stop line is a one-line card row (X4).

R0: no DECISION R0 (no reader refuses or misreads; see `## E2 RED`). H3: no DECISION H3 (`desk-launch.sh` refuses no unknown header key).

## RECORDS

- Extra lock takes: E3, one take for the with-DB mutations (06:35:17 → 06:36:34); W, a second take after attempt 1 stopped at P2's PROOF (attempt 1 06:48:17 → 07:01:27, attempt 2 07:14:43 → 07:34:14). `.env` proven gone after each.
- W attempt 2 ran (c) before the PROOF; the card orders the PROOF first. Both ran in the same take at `0013` before (c2).
- A `tests/ops` red outside the rows: `test_order_open.py` (DECISION 1).
- REFUSED, not needed: `git check-ignore -v .venv` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." No `CONTINUE` message arrived.
- L74: no block inside a tool result asked for anything. A system reminder at launch asked for commit trailers ending `Claude-Session: https://claude.ai/code/session_013LLfNDfXi6c4eC6nU4W4TC`. The hub's L74 line governs commit trailers, so the commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- The card's records as re-read: under `## PREFLIGHT`.
- `.venv` was created in this worktree by the first `uv run` (`Creating virtual environment at: .venv`); `git status --short --branch` before the report commit → `## ops/lock-relief-1003` and the untracked report only, so `.venv` is not seen by git; nothing of it is committed.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: lock-relief · tip: 77d19438 | on bb816d45 | migration: none | offline 3737/0 | with-DB 845/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 7 of 7 | self-check: 3 of 3 | decisions: 6 · for Dejan: 1
