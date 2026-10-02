# launcher-checks — build report (2026-10-02)

CARD: `docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md` (committed `b19e85c8`) · BRANCH `ops/launcher-checks-1002` · BASE `63649058`

## §0 Headline
(in progress)

## L74
none

## AUTHORIZATION
Times from `date`: `Fri Oct  2 12:03:59 EDT 2026`.

| proof | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../BUILD-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../21-launcher-checks-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md"` | 0 | `b19e85c8870dd83f99cca0839133225f598d38d6` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING R60 row | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); … | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULINGS R47 row | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, … | HIS RULING · APPROVED |` |
| R47 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| RULINGS R39 row | `grep -n "^| R39 " ".../cto-2026-10-02.md"` | 0 | `46:| R39 | 07:57 ET | HIS RULING (direction row 2): permission by class — `sh …/ops/desk/*` everywhere; `COBALT_ENV=dev uv run cobalt db *` on build/check/devfix/deploy, production denied on the first three; each kind's report glob (…). | HIS RULING · APPROVED |` |
| R39 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R39 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |

All hold.

## PREFLIGHT

| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 12:03:59 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/launcher-checks-1002` + `?? "docs/40 - DevDocs/reports/launcher-checks-build-2026-10-02.md"` (this report, the hub's FIRST Write; nothing else) |
| head | `git log --oneline -1` | 0 | `63649058 feat(devfix-route): the devfix kind — DEVFIX-HUB.md, desk-launch.sh devfix, its card format and approval list (F1, F2, F3, L1, L3, L76)` |
| branch from main repo | `git -C /Users/cobalt/cobalt log --oneline -1 ops/launcher-checks-1002` | 0 | `63649058 feat(devfix-route): …` (same) |
| diff vs BASE | `git diff --stat 63649058` | 0 | (nothing) |
| BASE | `git show --stat 63649058` | 0 | `docs/40 - DevDocs/prompts/CARD.md | 39`, `DEVFIX-HUB.md | 55`, `STANDING-LIST.md | 21`, `ops/desk/desk-launch.sh | 82`, `tests/ops/test_desk_launch_devfix.py | 4` — `5 files changed, 176 insertions(+), 25 deletions(-)` |
| own .env | `ls /Users/cobalt/cobalt-wt/launcher-checks-1002/.env` | 1 | `No such file or directory` |
| any .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| symbol | `grep -n -F "refuse() {" ops/desk/desk-launch.sh` | 0 | `126:refuse() {` |
| symbol | `grep -n -F "committed() {" …` | 0 | `137:committed() {` |
| symbol | `grep -n -F "check_paths() {" …` | 0 | `144:check_paths() {` |
| symbol | `grep -n -F "run_launch() {" …` | 0 | `168:run_launch() {` |
| symbol | `grep -n -F "field() {" …` | 0 | `425:field() {` |
| symbol | `grep -n -F "need() {" …` | 0 | `428:need() {` |
| symbol | `grep -n -F "section() {" …` | 0 | `433:section() {` |
| symbol | `grep -n -F "commit_exists() {" …` | 0 | `442:commit_exists() {` |
| symbol | `grep -n -F "lock_free() {" …` | 0 | `489:lock_free() {` |
| per-kind case, last block | Grep tool, `case "\$kind" in\|run_launch "\$dir" "\$line" "\$note"` (the Bash form was refused, `## RECORDS`) | — | `394:case "$kind" in` · `511:case "$kind" in` · `696:case "$kind" in` · `720:    run_launch "$dir" "$line" "$note"` · `731:run_launch "$dir" "$line" "$note"` |
| fixture | `grep -n -F "def desk(" tests/ops/test_devdb_lock.py` | 0 | `185:def desk(roots, tmp_path):` |
| helper | `grep -n -F "def launch(" tests/ops/test_devdb_lock.py` | 0 | `244:def launch(env: dict, *args: str) -> subprocess.CompletedProcess:` |
| new file | `ls tests/ops/test_desk_launch_prechecks.py` | 1 | `No such file or directory` |
| wc | `wc -l ops/desk/desk-launch.sh tests/ops/test_devdb_lock.py tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_size_guard.py "docs/40 - DevDocs/prompts/STANDING-LIST.md"` | 0 | `731` · `306` · `372` · `445` · `207` |
| READ report | `tail -n 3 ".../reports/deploy-2026-10-01-1.md"` | 0 | last line `FAILED: gate — G (c) — tests/cobalt/test_radar_score_migration.py::test_card_checks_index_and_receipt_immutability_on_cobalt_dev (TooManyColumns: cobalt_dev "user".aset_sizings 1581/1600 column slots) · rollback: not used · decisions: 2 · for Dejan: 0` |
| RESTARTS empty | `uv run cobalt jobs restarts 63649058..HEAD` | 0 | `docs/40 - DevDocs/reports/launcher-checks-build-2026-10-02.md	A	DOCS	-` · `RESTARTS: none` (the one path is this untracked report; no commit in the range) |

Card `## RECORDS`, copied: (1) RESTARTS class homes: `ops/desk/desk-launch.sh` → the `ops/desk/` rule; `tests/ops/*` → test/documentation (`restarts.py:239`); `docs/…` → DOCS (`:219`). No `src/`, no `configs/`. (2) The three launches this card would have refused: 10-01 R9, 10-01 R6, `deploy-2026-10-01-1.md` DECISIONS 1. (3) The classes are his 2026-10-02 R39; `sh` is not on this line. (4) His order sets aside the outside house (`brain-direction-2026-10-02.md` row 10). Re-read: (2)'s third item — `deploy-2026-10-01-1.md` `## DECISIONS` 1 reads `the voice-peers check's stop line reads tip: 76f7f7d5 (the branch head), and the card's row gives the code tip de483933 … Default taken: proceed` (Grep, `-A 6`). (1) is re-read at RESTARTS by the tool.

THE LOCK PROBE (take 0, reads only), `<FP>` typed exactly:
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → exit 1, `no matches found`.
- (b) `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/launcher-checks-1002/.env` → exit 0; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `-rw-------  1 cobalt  staff  2186 Oct  2 12:06 /Users/cobalt/cobalt-wt/launcher-checks-1002/.env`. Taken `Fri Oct  2 12:06:36 EDT 2026`.
- `<FP>` → `<Fp>`: `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → exit 0. Quoted whole:

```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
archive_incidents    system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.01
archive_progress     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.00
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.23
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   231          92583e844337bea96e1d53c358cd4de5   0.00
day_modes            user    user     2            f2ffb4d41ed0a3bbc3dc2a1c7e6112b9   0.00
desk_grade           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_packet          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_regime          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
drc_events           user    -        -            -                                  0.00
drc_fills            user    -        -            -                                  0.00
drc_imports          user    -        -            -                                  0.00
drc_rows             user    -        -            -                                  0.00
drc_stated_books     user    -        -            -                                  0.00
legs                 user    -        -            -                                  0.00
missed               user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
movers_daily         system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
picks                user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
prediction_records   user    -        -            -                                  0.00
radar_membership     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_pool           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_receipt  user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_run      system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
session_blocks       system  system   6            b650702dd6fd624548e05ca940662f08   0.00
traders              user    user     1            a64e01480038484676fad3b14eb2489f   0.00
vault_overrides      user    user     6            6a8b05207f55b8e25c253ce990c7a65a   0.00
vault_writes         user    user     187          2c8181e1b1a4156609f49ce53c27a97f   0.01
voice_turns          user    -        -            -                                  0.00
------------------------------------------------------------------------------------------
36 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 29 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007; card_stop_edits: 1 card column(s) added by 0007. Proof cost: total 5.3 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
code: 63649058 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/launcher-checks-1002
```
  No `CHANGED`. The tables above `0013` (`drc_*`, `legs`, `prediction_records`, `voice_turns`) stand absent (`-`): `cobalt_dev` at `0013`. `DIRTY: 1 path` is this untracked report.
- (d) `rm /Users/cobalt/cobalt-wt/launcher-checks-1002/.env` → exit 0; `ls /Users/cobalt/cobalt-wt/launcher-checks-1002/.env` → `No such file or directory`. Released `Fri Oct  2 12:06:52 EDT 2026`. `.env: removed, proven gone (PREFLIGHT)`.

PROVEN BY FIRST REAL USE (the hub's table): `uv run pytest *` · `COBALT_LIVE_VAULT_ROOT=… uv run pytest *` at E0; `git add *` · `git commit *` at E2's red commit; `COBALT_ENV=dev uv run pytest *` and `COBALT_ENV=dev uv run cobalt db migrate` at W (c) / (c2); the rollback string at W (f).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → exit 0, `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 636.04s (0:10:36)`. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.80s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — it does not name `COBALT_LIVE_VAULT_ROOT`.
- L5's before-counts on BASE: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `115 passed, 1 xfailed, 15 warnings in 88.07s (0:01:28)`. `uv run pytest --co -q -p no:cacheprovider tests/ops/test_devdb_lock.py tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_size_guard.py` → `108 tests collected`: `test_devdb_lock.py` 22 · `test_desk_launch_devfix.py` 47 · `test_desk_size_guard.py` 39 (counted from the id list).

## E2 RED
Written: `tests/ops/test_desk_launch_prechecks.py` (45 tests; no with-DB test, no lock take). No `ops/` edit before the red commit.
- `uv run pytest -q -rfE -p no:cacheprovider --color=no --tb=no tests/ops/test_desk_launch_prechecks.py` → `36 failed, 9 passed`. One of the 36 (`test_l1_a_deploy_with_rulings_none_needs_no_rulings_file`, a negative control) failed for a fixture reason — `FileNotFoundError: … reports/x-job-check.md` (its `git rm` emptied the folder before `ship()` wrote the report); rewritten (`ship()` first, then the `git rm`), it PASSES on BASE as a control should.
- The reds, by reason (`--tb=line`, first lines quoted): every L1, L2 and L3 refusal test fails in `refused()` at `assert done.returncode == 1` with `assert 0 == 1` — the launch went through (`RUN: claude --bg …` in its stderr): the rows' named reason "RED on BASE: the launches go through". L4: `test_l4_a_build_launch_ends_its_stdout_with_the_watch_line` → `IndexError: list index out of range` (stdout empty: no `WATCH:` line); `test_l4_a_close_prints_the_watch_line_on_its_report` → the same `IndexError`; `test_l4_a_dry_run_prints_the_watch_line_after_the_dry_lines` → `assert 'WARNING: des...guard skipped' == 'WATCH: sh /U...-job-card.md"'`; `test_l4_the_header_says_installed_and_tested` → `assert 'NOT INSTALLED' not in '#!/bin/sh\n...'` (`# DRAFT — NOT INSTALLED — TESTED IN PART …`).
- Negative controls PASS on BASE: `test_l1_a_build_on_an_approved_committed_row_launches`, `test_l1_a_house_line_whose_overruled_row_is_approved_launches`, `test_l1_a_deploy_with_rulings_none_needs_no_rulings_file`, `test_l2_a_check_launches_on_the_built_line_for_its_job_and_tip`, `test_l2_a_pass_2_launch_keeps_the_test_it_has`, `test_l3_a_deploy_on_a_committed_clean_check_launches`, both `test_l3_a_docs_only_commit_past_the_code_tip_launches[...]`, `test_l3_an_old_shape_check_line_with_its_own_literals_launches`, `test_l3_a_step_d0_resume_is_not_re_checked`.
- RUN L5 at E2 (pre-build): `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=no tests/ops` → `35 failed, 125 passed, 1 xfailed, 15 warnings in 100.17s (0:01:40)` — the 35 are this file's reds; the older files pass. Run again after E3 (the run that answers the row).
- RUN L6 at E2: `grep -n -F "## CLASSES" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` → exit 1, nothing. Run again after E3.
- Commit: `b4d38eda wip(launcher-checks): red — the pre-check tests (L1, L2, L3, L4)`.

## E3 THE ROWS
Built in card order in `ops/desk/desk-launch.sh` (re-read whole at BASE before the first edit), the three older test files and `STANDING-LIST.md`. Commit `a2dd9400`.

| row | what was built | row tests after the row | mutation (Edit tool) → red | undone |
|---|---|---|---|---|
| L1 | `ruling_row` / `ruling_rows`, called once after the card-committed check (every kind reaching it is build, check, deploy or devfix). Each `RULINGS` item and each `overruled <date> R<n>` of `HOUSE A` / `HOUSE B` → `$REPORTS/cto-<date>.md`: exactly one line `^| R<n> |`; holds `HIS RULING` and `APPROVED`; committed = `git -C $REPO log -1 --format=%H -S"| R<n> |"` non-empty AND the same line stands in `HEAD:<file>` | `-k test_l1_` → `16 passed, 29 deselected` | (1) `ruling_rows` → `: ruling_rows` → `13 failed, 3 passed`; first: `FAILED …::test_l1_a_cited_row_that_is_absent_refuses`. (2) the `HEAD:` blob read → `true` (the card's `-S` alone) → `1 failed, 15 passed`: `FAILED …::test_l1_a_row_approved_only_in_the_working_tree_refuses` | yes |
| L2 | kind check, not PASS-2: `not built — no build report: <path>` / `not built — <last line>` unless the last non-blank line is `BUILT · job: <JOB> · tip: <TIP>` exactly or followed by a space | `-k test_l2_` → `9 passed, 36 deselected` | (1) `if [ -z "$pass2" ]` → `if false` → `7 failed, 2 passed`; first: `FAILED …::test_l2_a_report_not_ending_in_its_built_line_refuses[FAILED: W — x]`. (2) negative control → `if true` → `1 failed, 8 passed`: `FAILED …::test_l2_a_pass_2_launch_keeps_the_test_it_has` | yes |
| L3 | `ships_checked` (+ `ship_cell`), deploy, not STEP-D0, before the gate worktree add: per `## SHIPS` row the report exists; `log -1` non-empty, `diff --quiet`, `diff --cached --quiet`; every backticked literal of the last column in the last non-blank line (followed by a space or the end); its `tip:` = code tip or branch head; `rev-parse --short=8 <branch>` = row head; `merge-base --is-ancestor <code tip> <head>`; `diff --stat <code tip> <head> -- . ':(exclude)docs'` empty | `-k test_l3_` → `14 passed, 31 deselected` | (1) `ships_checked` → `: ships_checked` → `9 failed, 5 passed`; first: `FAILED …::test_l3_one_broken_fact_refuses_and_leaves_no_gate[uncommitted]`. (2) negative control: the `|| [ "$ltip" = "$shead" ]` dropped → `1 failed, 13 passed`: `FAILED …::test_l3_a_docs_only_commit_past_the_code_tip_launches[head]` | yes |
| L4 | `here` (the script's folder), `watch_line`, `run_launch <dir> <line> <note> [<watch>]`: the WATCH line is the last stdout line of a launch that exits 0 (build, check, deploy, devfix, close); under `DESK_LAUNCH_DRY=1` it follows the dry lines on STDERR (`## DECISIONS` 1). Header lines 2–5 → `# The installed launcher (installed 2026-09-30, his R63); its kinds are tested in tests/ops/.`; the WATCH line and the L1–L3 refusals added to the header's lists | all 45 → `45 passed`; `grep -c "NOT INSTALLED" ops/desk/desk-launch.sh` → `0` | (1) the WATCH `printf` in `run_launch` removed → `3 failed, 3 passed`; first: `FAILED …::test_l4_a_build_launch_ends_its_stdout_with_the_watch_line`. (2) WATCH printed ungated and on dry STDOUT → `4 failed, 4 passed`: `FAILED …::test_l4_a_dry_run_prints_the_watch_line_after_the_dry_lines`, `…::test_l4_a_refused_or_failed_launch_prints_no_watch_line`, and two older assertions `test_desk_launch_devfix.py::test_a_good_card_prints_the_worktree_add_the_cd_and_the_filled_line`, `…::test_build_still_prints_its_add_cd_and_line` (the L4/L5 conflict, shown) | yes |
| L5 | RUN. Fixture lines only: a committed `cto-2026-01-02.md` with an approved R1 in each of the three files' tmp repos; `test_devdb_lock.py` and `test_desk_size_guard.py` build reports end `BUILT · job: <job> · tip: <tip>`. `git diff 63649058 -- <the three files>` → `3 +++`, `5 ++++-`, `7 +++++++` — additions, and one changed fixture data line (`"BUILT · fixture\n"` → the BUILT line); no assertion line changed, none removed | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `160 passed, 1 xfailed, 15 warnings in 103.08s (0:01:43)`. Counts: `--co -q` of the three files → `108 tests collected` (22 · 47 · 39), equal to BASE | — (RUN) | — |
| L6 | `## CLASSES — approved once, 2026-10-02 R39` inserted after `## NEVER`, before `## THE .env PATTERN` | RUN: `grep -n -F "## CLASSES" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` → `31:## CLASSES — approved once, 2026-10-02 R39` (one line) | — (RUN) | — |

After undoing every mutation: `git diff --stat` → `STANDING-LIST.md | 9`, the report, `ops/desk/desk-launch.sh | 163`, the three test files `3`, `5`, `7` (the fix, nothing else); then `tests/ops` → `160 passed, 1 xfailed, 15 warnings in 102.77s (0:01:42)`.

The L6 section, quoted whole:

```
## CLASSES — approved once, 2026-10-02 R39
His permission by class. A string inside a class is used and recorded and is not brought to him; a string outside every class is NEW and is asked for by itself. NO launch line changes with this section: the lines take the classes in the adoption card.

| string | for | can touch | never touches |
|---|---|---|---|
| (a) `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` and its installed spelling `Bash(sh /Users/cobalt/.claude/ops/*)` | any script under `ops/desk/` that reached `main` through a build, a check and a deploy; on his settings and on every fixed file's line | what that script's own header and tests say it touches | a script that did not come through a build, a check and a deploy |
| (b) `Bash(COBALT_ENV=dev uv run cobalt db *)` | any dev-only `cobalt db` verb, on the build, check, devfix and deploy lines | `cobalt_dev`, as the verb allows | production: `Bash(COBALT_ENV=production*)` is DENIED on the build, check and devfix lines |
| (c) each kind's own report glob under `docs/40 - DevDocs/reports/` | the Edit and Write tools on that kind's own report | the files of that one glob | another kind's reports, `cto-<date>.md`, code, configs, the prompts |
```

DevDocs page: no page for `ops/desk/desk-launch.sh` exists under `docs/40 - DevDocs/cobalt/` (Grep `desk-launch` there → only `jobs/restarts.md`, the RESTARTS classifier's page); it is no `src/cobalt` module and the earlier ops builds (`git show --stat 63649058`) wrote none. None invented (`## RECORDS`).

## RESTARTS
`uv run cobalt jobs restarts 63649058..HEAD` (HEAD `a2dd9400`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/launcher-checks-build-2026-10-02.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_devfix.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	A	test/documentation; no resident	-
tests/ops/test_desk_size_guard.py	M	test/documentation; no resident	-
tests/ops/test_devdb_lock.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row; nothing classified here.

## W THE THREE SUITES
`<tip>` = `a2dd9400`. TREE STATE `unchanged`: this build adds no with-DB test and no migration (`git diff --stat 63649058 a2dd9400` touches `ops/`, `tests/ops/`, `docs/` only).
- (a) OFFLINE: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → exit 0, `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 603.32s (0:10:03)` → `<p>` = 3784. Tests this build adds: none in these two folders (the 45 new tests are `tests/ops/test_desk_launch_prechecks.py`, run at E3).
- (b) THE LOCK (a): `ls -la /Users/cobalt/cobalt-wt/*/.env` → exit 0, ONE line: `-rw-------  1 cobalt  staff  2186 Oct  2 12:26 /Users/cobalt/cobalt-wt/worker-steps-1002/.env`. Another worktree holds the lock: this build did NOT take it (no `cp`, no `<FP>`, no `migrate`). Stopped here (UNATTENDED RULES (b)) at `Fri Oct  2 12:43:39 EDT 2026`.
- (e) LIVE-NOTE (`.env` absent here; it needs no lock): `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.46s`; the skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` names no `COBALT_LIVE_VAULT_ROOT` → `<l>` = 146.
- (b)–(c3r) and (f): NOT RUN — the lock is held by `worker-steps-1002`. `dev forward: ` never recorded; nothing applied; `cobalt_dev` untouched by this build since PREFLIGHT's (d).

## PRE-STOP SELF-CHECK

## FOR THE CHECK

## CONTINUE
next: W (b) — THE LOCK (a)–(b) once no `/Users/cobalt/cobalt-wt/*/.env` exists; then `<F0>`, `--proof-only`, pass 1 (c), forward (c2), pass 2 (c3), (c3r), (f). W (a) `3784` and (e) `146` stand on `a2dd9400` unless the tip moves.

## DECISIONS
1. ASK DESK: rows L4 and L5 conflict. L4 says the `WATCH:` line is also printed under `DESK_LAUNCH_DRY=1` "after the dry lines". L5 says no assertion of `test_desk_launch_devfix.py` changes, and four of them assert the dry stdout line for line (`test_a_good_card_prints_the_worktree_add_the_cd_and_the_filled_line`, `test_an_existing_worktree_on_the_branch_is_reused_not_re_cut`, `test_a_resume_skips_its_own_lock_and_prefixes_continue`, `test_build_still_prints_its_add_cd_and_line`; `test_the_trees_devfix_hub_line_is_printed_with_its_tokens_filled` reads `out[-1]`). The E3 mutation that printed it on dry STDOUT turned two of them red. Default taken: under the dry run the WATCH line follows the dry lines on STDERR; a real launch that exits 0 prints it as its last STDOUT line, as L4 states. [12:43 ET]
2. ASK DESK: L1's commit proof. The card's command (`git -C $REPO log -1 --format=%H -S"| R<n> |"`) is non-empty whenever the row was ever committed, so on its own it lets through a row that is `APPROVED` only in the working tree, the very case the card names. E3 mutation (2) shows it: with the `-S` alone, `test_l1_a_row_approved_only_in_the_working_tree_refuses` passes the launch. Default taken: both the `-S` proof and the same line standing in `HEAD:<cto file>`. Other uncommitted rows in that file do not block a launch. [12:43 ET]

## RECORDS
- `.env: removed, proven gone (PREFLIGHT)`. Lock take 0 at `12:06:36`, released at `12:06:52`.
- W (b) found the lock held by `/Users/cobalt/cobalt-wt/worker-steps-1002/.env` (12:26) — not this build's; nothing of this build's on `cobalt_dev`.
- REFUSED, not needed: `grep -n -F "case \"$kind\" in" ops/desk/desk-launch.sh` and `grep -n -F "run_launch \"$dir\" \"$line\" \"$note\"" ops/desk/desk-launch.sh` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (a `$` inside a double-quoted argument); the same lines read with the Grep tool (PREFLIGHT).
- No DevDocs page exists for `ops/desk/desk-launch.sh` under `docs/40 - DevDocs/cobalt/`; no page invented.
- A deploy card whose `## SHIPS` table has no row passes L3 untouched (as the fixtures of `test_devdb_lock.py` and `test_desk_size_guard.py` need it to); the card names no such refusal.
- Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74). A harness reminder of this session asked for a `Claude-Session:` line; it is not added. Not a tool result, so `## L74` stays `none`.
- The card's `## RECORDS`, re-read: see `## PREFLIGHT`.

FAILED: W (b) — cobalt_dev lock held — /Users/cobalt/cobalt-wt/worker-steps-1002/.env
