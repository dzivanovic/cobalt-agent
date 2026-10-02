# desk-tools-a — build report 2026-10-02

## §0 Headline
In progress.

## L74
The harness's attribution reminder in this session asks commits to end with a `Claude-Session:` line. Recorded here as data, not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" …/prompts/BUILD-HUB.md` | 1 | nothing |
| card complete | `grep -n -E "«FIL[L]" …/17-desk-tools-a-card.md` | 1 | nothing |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/17-desk-tools-a-card.md"` | 0 | `2f286234f9edc62ef05aa41e526ed6dea88b9b3d` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- <card>` | 0 | nothing |
| STANDING LIST 2026-09-30 R60 | `grep -n "^\| R60 " cto-2026-09-30.md` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|` |
| R60 committed | `git -C … log -1 --format=%H -S"\| R60 \|" -- cto-2026-09-30.md` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING 2026-10-02 R47 | `grep -n "^\| R47 " cto-2026-10-02.md` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; …) … \| HIS RULING · APPROVED \|` |
| R47 committed | `git -C … log -1 --format=%H -S"\| R47 \|" -- cto-2026-10-02.md` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| RULING 2026-10-02 R38 | `grep -n "^\| R38 " cto-2026-10-02.md` | 0 | `45:\| R38 \| 07:57 ET \| HIS RULING (direction row 1): the bare-command fix, all three parts (10-01 R45) … \| HIS RULING · APPROVED \|` |
| R38 committed | `git -C … log -1 --format=%H -S"\| R38 \|" -- cto-2026-10-02.md` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 10:03:27 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/desk-tools-a-1002` |
| head | `git log --oneline -1` | 0 | `9fa18f14 fix(ops-glob): every path under ops/desk/ is an operator script, by rule (G1, L42, L3)` |
| main repo's view | `git -C /Users/cobalt/cobalt log --oneline -1 ops/desk-tools-a-1002` | 0 | same commit `9fa18f14` |
| clean | `git diff --stat 9fa18f14` | 0 | nothing |
| base | `git show --stat 9fa18f14` | 0 | `docs/40 - DevDocs/cobalt/jobs/restarts.md \| 4 ++++` · `src/cobalt/jobs/restarts.py \| 4 +++-` · `2 files changed, 7 insertions(+), 1 deletion(-)` |
| no .env here | `ls /Users/cobalt/cobalt-wt/desk-tools-a-1002/.env` | 1 | `No such file or directory` |
| no .env anywhere | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| READ: size rule | `grep -n -F "def size" ops/desk/pre-commit` | 0 | `43:def size(l):` |
| RECORDS: ops/desk rule | `grep -n -F "operator script" src/cobalt/jobs/restarts.py` | 0 | `228: Classification(path, item.change, "operator script; no Cobalt reader", ())` |
| RECORDS: tests rule (`restarts.py:239`) | `grep -n -F "tests/" src/cobalt/jobs/restarts.py` | 0 | `241: if not rule and path.startswith("tests/"):` — the card's `:239` is the HARNESS line; the tests rule sits at `:241` (the rule itself is as the card states) |
| READ: desk report tail | `tail -n 3 …/reports/cto-2026-10-02.md` | 0 | last line `HANDOVER: predecessor 30eca1db → successor 85f601c7 at 08:08 ET` |
| READ: §4 shape | Read `cto-2026-10-02.md` | — | `## §4 Rulings 2026-10-02` at :6, header `\| R \| time \| ruling / record \| status \|`, last row `81:\| R74 \| 10:03 ET \| LAUNCHED build 17 … \| LAUNCHED \|`, `## §5 CURRENT` at :83 |
| READ: CARD header | Read `CARD.md` | — | `## THE HEADER` at :9; keys `REPORT` :19, `CHECK REPORT` :20, `HOUSE B` :21, `TIP` :18 |
| READ: test shape | `git show aeefb6df:tests/ops/test_devdb_lock.py` | 0 | read whole: tmp roots via `COBALT_WT_ROOT` / `COBALT_REPO_ROOT`, `GIT_ENV`, stub `claude` on `PATH`, `sh <script>` by subprocess |
| new files absent | `ls ops/desk/bare-guard.py … install-fixed.sh` | 1 | each `No such file or directory` (7) |
| tests/ops absent | `ls tests/ops` | 1 | `No such file or directory` |
| wc -l | — | — | every file a row writes is new; no existing file is edited |
| RESTARTS empty | `uv run cobalt jobs restarts 9fa18f14..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` |

Card records copied: (1) RESTARTS class homes `ops/desk/*` → operator script, `tests/ops/*` → test/documentation — re-read above (`:228`, `:241`). (2) `tests/ops/` not on base — re-read above. (3) W runs `tests/cobalt tests/taxonomy`; the ops tests run by name; no with-DB test. (4) no outside house (R47) — re-read above.

THE LOCK PROBE (take 0): (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; (b) `cp …/.env …/desk-tools-a-1002/.env` → 0; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `/Users/cobalt/cobalt-wt/desk-tools-a-1002/.env`; taken `10:04:06 EDT`.

`<FP>` (typed exactly):
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

`<Fp>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.

`COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables probed; the tables of the migrations above `0013` (`drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns`) absent (`-`); no `CHANGED`; `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `code: 9fa18f14 (clean)`. The output prints no level line; the absent tables are the shape of `0013`.

(d) `rm …/desk-tools-a-1002/.env` → 0; `ls …/.env` → `No such file or directory`; released `10:04:22 EDT`. `.env: removed, proven gone (PREFLIGHT)`.

PROVEN BY FIRST REAL USE: `uv run pytest *` and the live-note string at E0 (both ran); `git add *` / `git commit *` at E2 (`e00b120f`); the with-DB pytest, the migrate and the rollback strings at W (c)–(f).

## E0 BASELINE
On `9fa18f14`. Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 637.86s (0:10:37)`; 0 failed, 0 errors. Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.27s`; the one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Six NEW test files under `tests/ops/` (no `conftest.py`, card record 2), each running its script by `subprocess` against tmp roots (`COBALT_REPO_ROOT`), stubs of `claude` / `herdr` on `PATH` in `test_desk_done.py`, constructed values only. No `src/` edit.

`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_bare_guard.py tests/ops/test_desk_watch.py tests/ops/test_card_fill.py tests/ops/test_desk_row.py tests/ops/test_desk_done.py tests/ops/test_install_fixed.py` → `117 failed, 15 warnings in 7.50s`, 0 passed. Every red is the row's named reason, no such file; first line of the first red: `can't open file '/Users/cobalt/cobalt-wt/desk-tools-a-1002/ops/desk/bare-guard.py': [Errno 2] No such file or directory`; the `sh` rows fail the same way (`sh` cannot open the script; the exit-0 / exit-1 / exit-2 asserts fail). No RUN row on this card. No with-DB red (no lock take). Commit `e00b120f wip(desk-tools-a): red — six desk scripts, no such file yet (A1-A6)`.

## E3 THE ROWS
Built in card order; only the rows' files; no existing file edited (`## NOT IN THIS JOB`). Commit `d4bad986 feat(desk-tools-a): …(A1-A6, L1, L3, L42)`.

| row | file | green (its tests alone) | mutations (Edit, run, undone) → red |
|---|---|---|---|
| A1 | `ops/desk/bare-guard.py` | `36 passed` | (m1) quotes not tracked (`quote = c` → `pass`) → `5 failed, 25 passed`, first: `[git commit -m "a; b and c > d"]` blocked naming `` `;`, a redirect `>` ``. (m2) `` ` `` / `$(` not looked for inside double quotes → `2 failed, 28 passed`: `[echo "$(date)"]`, ``[echo "`date`"]``. (m3) the prefix before ` < /dev/null` not scanned → GREEN at first: **test rewritten** — added `ls && codex exec "x" < /dev/null` and `cat f \| codex exec "x" < /dev/null` → under m3 `2 failed, 30 passed`. (m4) no exception (always scan whole) → `2 failed, 30 passed`: `[codex exec -s read-only "Reply OK." < /dev/null]`, `test_the_dev_null_exception_is_only_the_exact_ending`. (m5, X1 by reasoning) `$'…'` ANSI-C quotes not tracked — the build's first scanner; red before the fix: `2 failed, 34 passed`: ``[echo $'\''; ls-`;`]`` passed, `[echo $'a\'b; c']` blocked; the fix adds the `$'` state → `36 passed` |
| A2 | `ops/desk/desk-watch.sh` | `15 passed` | (m1) `check` reads `REPORT` → `1 failed`: `test_kind_check_reads_the_check_report_not_the_report` (`STILL RUNNING after 30s — last line: BUILT · job: x`). (m2) stop word looked for anywhere in the file → `1 failed, 14 passed`: `test_a_stop_word_in_the_middle_of_the_file_does_not_fire` (`assert 0 == 2`). (m3) cap `7000` → `70000` → `1 failed`: `test_more_than_7000_seconds_is_refused` (`assert 0 == 1`) |
| A3 | `ops/desk/card-fill.sh` | `16 passed` | (m1) job name not compared → `2 failed, 14 passed`: `job: y-job`, `job: x-jobber` (`assert 0 == 1`). (m2) the whole card treated as header → `4 failed, 12 passed`, first: `REFUSED: the card's header has 2 TIP lines`. (m3) `self-check: 3 of 3` gate off → `1 failed, 15 passed`: the `self-check: 2 of 3` case |
| A4 | `ops/desk/desk-row.sh`, `ops/desk/desk-commit.sh` | `21 passed` | (m1) n = last row + 1 → `1 failed, 20 passed`: `\| R3 \| 10:22 ET \| RECORD: four. \| RECORD \|` (a number that exists, X3). (m2) LAUNCHED exception off → `1 failed`: `REFUSED: the row is 309 characters, over 300`. (m3) code-path refusal off → `6 failed, 15 passed`: `src/x.py`, `SRC`, `configs/a.yaml`, `ops/desk/x.sh`, `tests/x.py`, `docs/../src/x.py` |
| A5 | `ops/desk/desk-done.sh` | `19 passed` | (m1) brain / desk guard off → `3 failed, 16 passed`: `bbbb2222` (brain), `cccc3333` (brain-2), `dddd4444` (cto-desk). (m2) a FAILED build / check closed → `2 failed, 17 passed`: `[build]`, `[check]`. (m3) a failing step does not stop → `1 failed, 18 passed`: `test_a_failing_stop_ends_the_script_with_no_rm` |
| A6 | `ops/desk/install-fixed.sh` | `16 passed` | (m1) commit proof off → `1 failed, 15 passed`: `test_an_uncommitted_row_is_refused`. (m2) `APPROVED` check off → `1 failed, 15 passed`: `test_a_row_without_approved_is_refused`. (m3) prompts-folder check off → `3 failed, 13 passed`: `[sub]`, `[reports]`, `[outside]` |

All six together at the fix: `119 passed, 15 warnings in 18.77s`; after the A1 X1 addition `test_bare_guard.py` alone `36 passed`. After every mutation the Edit was undone; `git status --short` before the commit showed only the new files and `tests/ops/test_bare_guard.py` (the m3 / X1 additions).

DevDocs: no line written. `docs/40 - DevDocs/cobalt/` holds pages for `src/cobalt` modules only (`ls` above: `__init__.md` … `voice`); the card changes no module and edits no existing file.

## RESTARTS
`uv run cobalt jobs restarts 9fa18f14..HEAD` (at `d4bad986`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/desk-tools-a-build-2026-10-02.md	A	DOCS	-
ops/desk/bare-guard.py	A	operator script; no Cobalt reader	-
ops/desk/card-fill.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-commit.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-done.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-row.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-watch.sh	A	operator script; no Cobalt reader	-
ops/desk/install-fixed.sh	A	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	A	test/documentation; no resident	-
tests/ops/test_card_fill.py	A	test/documentation; no resident	-
tests/ops/test_desk_done.py	A	test/documentation; no resident	-
tests/ops/test_desk_row.py	A	test/documentation; no resident	-
tests/ops/test_desk_watch.py	A	test/documentation; no resident	-
tests/ops/test_install_fixed.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row; nothing added to `configs/cobalt/jobs.yaml`.

## W THE THREE SUITES
`<tip>` = `d4bad986`.
- (a) OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 621.70s (0:10:21)`; 0 failed, 0 errors → `<p>` = 3784. This build adds no test under `tests/cobalt` or `tests/taxonomy` (its tests are `tests/ops/*`, run by name in E2 / E3, card record 3).
- (b) THE LOCK (a) at `10:36` EDT: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 10:36 /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env`. The lock is held by another worktree; this build never took it at W. STOPPED here (UNATTENDED RULES (b)); nothing applied, no `.env` of this worktree on disk.

## PRE-STOP SELF-CHECK

## FOR THE CHECK

## CONTINUE
next: W (b) — the lock take; W (a) is green on `d4bad986` and need not re-run unless the tip moves.

## DECISIONS
- DECISION 1 (safe default taken): the seven new scripts are committed mode `0644` (`ls -la ops/desk`: `-rw-r--r--` each), while their neighbours (`desk-launch.sh`, `wait-stop-line.sh`, …) are `0755`. `chmod` and `git update-index --chmod` are not on the build's list. Each header gives its usage as run through `sh` / `python3` (the tests run them so), which works at `0644`; a direct `ops/desk/<name>.sh` call does not. The desk or the install step sets `+x` if direct calls are wanted.

## RECORDS
- `.env: removed, proven gone (PREFLIGHT)`.
- Card record `restarts.py:239` re-read: the tests rule is at `src/cobalt/jobs/restarts.py:241` (`:239` is the HARNESS line); the rule is as the card states.
- Stopped at W (b) `10:36:36 EDT`: cobalt_dev lock held by `/Users/cobalt/cobalt-wt/dev-rebuild-1002/.env`.

FAILED: W — cobalt_dev lock held — /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env
