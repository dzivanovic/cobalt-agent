# launcher-checks — build report (2026-10-02)

CARD: `docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md` (committed `b19e85c8`) · BRANCH `ops/launcher-checks-1002` · BASE `63649058`

## §0 Headline
Built, 6 of 6 rows, tip `a2dd9400` on `63649058`. `desk-launch.sh` now refuses before a session starts on a missing, unapproved or uncommitted ruling row (L1), a check whose build report does not end in its `BUILT` line (L2), and a deploy whose check is uncommitted, not clean, or whose head moved (L3). It prints the `WATCH:` line, and its header says installed (L4).
The three older launcher tests gained fixture lines only, still 108 tests (L5). `STANDING-LIST.md` carries `## CLASSES` (L6).
Suites: offline 3784/0 · with-DB 4383 + 171 / 0 · live-note 146/0 · `tests/ops` 160/0. `cobalt_dev` back at `0013`, `F2 = F0`; `.env` removed. RESTARTS: none.
The W gate stopped once at 12:43 on a lock `worker-steps-1002` held, and resumed on the desk's CONTINUE at 12:46.
Three decisions for the desk: the dry-run WATCH line goes on stderr (L4 vs L5); the L1 commit proof is stricter than the card's `-S`; two entry paths are unpinned (self-check 2 of 3).

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
- (b)–(c3r) and (f): NOT RUN at 12:43 — the lock was held by `worker-steps-1002`. Resumed at W (b), `## RECORDS` `CONTINUED`.
- (b) after the resume: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/launcher-checks-1002/.env`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `-rw-------  1 cobalt  staff  2186 Oct  2 12:46 /Users/cobalt/cobalt-wt/launcher-checks-1002/.env`. Taken `Fri Oct  2 12:46:53 EDT 2026`. `<FP>` → `<F0>`: `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `NOTHING WAS APPLIED`, no `CHANGED`, the tables above `0013` (`drc_*`, `legs`, `prediction_records`, `voice_turns`) absent: `cobalt_dev` at `0013` (the table matches PREFLIGHT's but for `cobalt_redactions 233 · 4619ce5f…`, rows written by the earlier holder's run; `code: 4f60f644`, the wip commit, the same code tree as `a2dd9400`).
- (c) PASS 1, executed WHOLE, the pass-1 command byte for byte with no deselect added (this build has no with-DB test):
`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk`
  → exit 0, `4383 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 710.12s (0:11:50)` → `<d1>` = 4383. Every SKIPPED line: `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` · `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged` · `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` · `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` · `tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read` · `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft` · `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`.
- (c2) FORWARD: `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → exit 0; applied in order `0001` … `0011`, `0013`, `0014`, `0015`, `0016`, `0017`, `0018`, `0019`, `0020`, `0021`, `0022` (no migration of this build); `CREATED`: `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns`; every other table `OK`, `content UNCHANGED on every table.`; no `CHANGED`. **`dev forward: APPLIED Fri Oct  2 12:59:31 EDT 2026`**. `<FP>` → `<F1>`: `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2, executed WHOLE, the pass-2 command byte for byte (pass 1 deselected nothing for this build):
`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones`
  → exit 0, `171 passed, 1 deselected, 5 warnings in 220.00s (0:03:40)`; no SKIPPED, no FAILED, no ERROR line (Grep of the output). This build's with-DB test ids: none. `<d2>` = 171; `<d>` = 4383 + 171 = 4554.
- (c3r) NOTHING LEFT BEHIND: `ls -la /Users/cobalt/cobalt-wt/launcher-checks-1002/.env` → listed (`… 2186 Oct  2 12:46 …`). The `aset_sizings` read takes "every constructed ticker your with-DB tests write"; this build has no with-DB test and writes no ticker, so no `IN (…)` list exists and the query was not typed. The forward and rollback tables both show `aset_sizings 1 -> 1`, digest `0824685c -> 0824685c` (the row PREFLIGHT read).
- (c4): no migration in this build; not run.
- (f) ROLLBACK: `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → exit 0; reversed newest first `0022`, `0021`, `0020`, `0019`, `0018`, `0017`, `0016`, `0015`, `0014`; the eight tables `DROPPED`; every other table `OK`; `content UNCHANGED on every table.` `<FP>` → `<F2>`: `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field. **`cobalt_dev: 0013 — F2 = F0`**. The lock's (d): `rm /Users/cobalt/cobalt-wt/launcher-checks-1002/.env` → exit 0; `ls /Users/cobalt/cobalt-wt/launcher-checks-1002/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`. Released `Fri Oct  2 13:04:11 EDT 2026`. `.env: removed, proven gone (W)`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown RED for its named reason — YES. Every refusal test of L1, L2 and L3 was red on BASE with `assert 0 == 1` in `refused()` (the launch went through). L4's tests were red with `IndexError` (no stdout line) and the header assertion. The controls passed (E2). Each row's mutation turned its tests red: L1 13 and then 1, L2 7 and then 1, L3 9 and then 1, L4 3 and then 4 (E3 table, quoted). The three older files gained fixture lines only; their assertions are unchanged, and the E3 mutation (2) of L4 turned two of them red (`test_a_good_card_prints_…`, `test_build_still_prints_…`). No test stayed green under its mutation, and none was rewritten for that reason. One control, `test_l1_a_deploy_with_rulings_none_needs_no_rulings_file`, was rewritten for a fixture fault (E2).
(2) Every entry path of each rule pinned by a test — NOT FULLY. The launcher has no caller in `src/`. Its one caller is the desk's `sh … desk-launch.sh <kind>` (PREFLIGHT symbols; card `## READ`). Pinned: L1 on build (8 tests), check, deploy and devfix (`test_l1_every_kind_refuses_an_absent_row[…]`); HOUSE A and HOUSE B `overruled`; a deploy `RULINGS: none` with no rulings file; a malformed item; two rows for one number; a build resume on its own `.env` (`test_devdb_lock.py::test_a_resume_skips_its_own_env`, green). L2 pinned on a first check, a resume (`E3`) and PASS-2 left alone. L3 pinned on a first deploy, a STEP-D0 resume left alone, a docs-only head (both tips), an old-shape literal and the nine breaks, each leaving no gate. L4 pinned on build, check, deploy, devfix, close, the dry run, a refusal and a failed `claude`. NOT PINNED: that `desk` and `prompt` print no `WATCH:` line on a real launch (no test runs either kind non-dry and reads its stdout); and a deploy whose `## SHIPS` has no row (it launches untouched, `## RECORDS`). Both are under `## DECISIONS` (3).
(3) Every `file:line`, count and quote re-read at the tip — YES. `git diff --stat a2dd9400 HEAD` → only this report (`204 +`). Grep at the tip → `2:# The installed launcher …`, `176:here=…`, `199:watch_line() {`, `509:ruling_row() {`, `537:ruling_rows() {`, `558:ruling_rows`, `583:ships_checked() {`, `697:` / `701:` the `not built — ` refusals, `750:        ships_checked`. `grep -c "NOT INSTALLED" ops/desk/desk-launch.sh` → `0`. `grep -n -F "## CLASSES" …` → `31:`. `git log --oneline 63649058..HEAD` → `4f60f644`, `a2dd9400`, `b4d38eda`.

## FOR THE CHECK
- Range `63649058..a2dd9400` (tip). Commits: `b4d38eda wip(launcher-checks): red — the pre-check tests (L1, L2, L3, L4)` · `a2dd9400 feat(launcher-checks): desk-launch.sh refuses before a session starts — ruling rows, the BUILT line, every check committed and clean; the WATCH line and the installed header; the CLASSES section (L1, L2, L3, L4, L5, L6, L1 law, L3 law, L72)` · `4f60f644 wip(launcher-checks): W (b) — cobalt_dev lock held by worker-steps-1002` (report only) · and the report commit at CLOSE.
- Per row, its reds, mutations and greens: `## E2 RED` and the `## E3 THE ROWS` table. RUN rows WHOLE: L5 at E2 `35 failed, 125 passed, 1 xfailed` (the new file's reds) and at E3 `160 passed, 1 xfailed, 15 warnings in 103.08s (0:01:43)`, with the three files at 22 · 47 · 39 = 108 before and after. L6 at E2 nothing, at E3 `31:## CLASSES — approved once, 2026-10-02 R39`, with the section quoted in E3.
- Suites: offline `3784 passed, 673 skipped, 1 xfailed`; pass 1 `4383 passed, 7 skipped, 65 deselected, 3 xfailed`; pass 2 `171 passed, 1 deselected`; live-note `146 passed, 1 skipped`. The executed commands are quoted in `## W`.
- Fingerprints: take 0 (PREFLIGHT) `<Fp>` 664 · 35 · `272c95bb…`. W take: `<F0>` 664 · 35 · `272c95bb…`, `<F1>` 893 · 44 · `126f2d69…`, `<F2>` 664 · 35 · `272c95bb…`. Lock: take 0 12:06:36 → 12:06:52; W take 12:46:53 → 13:04:11.
- RESTARTS: the table in `## RESTARTS`, `RESTARTS: none`.
- Where to look (CHECK ASKS): X1 → `ruling_row` (`desk-launch.sh:509`), the `not built` block (`:697`), `ships_checked` (`:583`, called `:750`). X2 → the controls `test_l1_a_deploy_with_rulings_none_needs_no_rulings_file`, `test_l3_an_old_shape_check_line_with_its_own_literals_launches`, `test_l3_a_step_d0_resume_is_not_re_checked`, `test_l2_a_pass_2_launch_keeps_the_test_it_has`. X3 → `gate_left()` asserted after every L3 break, and `test_l1_every_kind_refuses_an_absent_row` asserts no `x-gate` and no `x-fix`. X4 → `git diff 63649058 -- tests/ops/test_devdb_lock.py tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_size_guard.py`: the only line changed is the data line `"BUILT · fixture\n"` → `f"BUILT · job: fy · tip: {base}\n"`; every other change is an added line.
- The card's records as copied at PREFLIGHT: see `## PREFLIGHT`.

## CONTINUE
next: none — W done (`cobalt_dev: 0013 — F2 = F0`, `.env` removed); the report is committed at CLOSE. The desk verifies, then CHECK-HUB.

## DECISIONS
1. ASK DESK: rows L4 and L5 conflict. L4 says the `WATCH:` line is also printed under `DESK_LAUNCH_DRY=1` "after the dry lines". L5 says no assertion of `test_desk_launch_devfix.py` changes, and four of them assert the dry stdout line for line (`test_a_good_card_prints_the_worktree_add_the_cd_and_the_filled_line`, `test_an_existing_worktree_on_the_branch_is_reused_not_re_cut`, `test_a_resume_skips_its_own_lock_and_prefixes_continue`, `test_build_still_prints_its_add_cd_and_line`; `test_the_trees_devfix_hub_line_is_printed_with_its_tokens_filled` reads `out[-1]`). The E3 mutation that printed it on dry STDOUT turned red both of the two run under it. Default taken: under the dry run the WATCH line follows the dry lines on STDERR; a real launch that exits 0 prints it as its last STDOUT line, as L4 states. [12:43 ET]
2. ASK DESK: L1's commit proof. The card's command (`git -C $REPO log -1 --format=%H -S"| R<n> |"`) is non-empty whenever the row was ever committed, so on its own it lets through a row that is `APPROVED` only in the working tree, the very case the card names. E3 mutation (2) shows it: with the `-S` alone, `test_l1_a_row_approved_only_in_the_working_tree_refuses` passes the launch. Default taken: both the `-S` proof and the same line standing in `HEAD:<cto file>`. Other uncommitted rows in that file do not block a launch. [12:43 ET]
3. SELF-CHECK GAP (`self-check: 2 of 3`): two entry paths are not pinned by a test. (a) `desk` and `prompt` print no `WATCH:` line on a real launch. Their `run_launch` calls pass no fourth argument (`desk-launch.sh`, the `desk` and `prompt` blocks), but no test reads their non-dry stdout. (b) A deploy card whose `## SHIPS` table has no row launches untouched: the fixtures of `test_devdb_lock.py` and `test_desk_size_guard.py` have such cards, and the card names no refusal for them. Default taken: both are left as built and named here. Pinning (a) adds a test, which moves the tip and re-runs W; making (b) a refusal widens L3 past the card. The check decides. [13:05 ET]

## RECORDS
- `.env: removed, proven gone (PREFLIGHT)`. Lock take 0 at `12:06:36`, released at `12:06:52`.
- W (b) found the lock held by `/Users/cobalt/cobalt-wt/worker-steps-1002/.env` (12:26) — not this build's; nothing of this build's on `cobalt_dev`.
- REFUSED, not needed: `grep -n -F "case \"$kind\" in" ops/desk/desk-launch.sh` and `grep -n -F "run_launch \"$dir\" \"$line\" \"$note\"" ops/desk/desk-launch.sh` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (a `$` inside a double-quoted argument); the same lines read with the Grep tool (PREFLIGHT).
- No DevDocs page exists for `ops/desk/desk-launch.sh` under `docs/40 - DevDocs/cobalt/`; no page invented.
- A deploy card whose `## SHIPS` table has no row passes L3 untouched (as the fixtures of `test_devdb_lock.py` and `test_desk_size_guard.py` need it to); the card names no such refusal.
- Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74). A harness reminder of this session asked for a `Claude-Session:` line; it is not added. Not a tool result, so `## L74` stays `none`.
- The card's `## RECORDS`, re-read: see `## PREFLIGHT`.
- STOPPED `Fri Oct  2 12:43:39 EDT 2026`: `FAILED: W (b) — cobalt_dev lock held — /Users/cobalt/cobalt-wt/worker-steps-1002/.env` (wip `4f60f644`).
- CONTINUED at W (b) Fri Oct  2 12:46:45 EDT 2026 — the message from `cto-desk`: "CONTINUE: W (b). The cobalt_dev lock is free now (no worktree .env held; cobalt_dev at 0013)." Verified: `ls -la /Users/cobalt/cobalt-wt/*/.env` → exit 1, `no matches found`; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → `No such file or directory`. The level `0013` is read by `--proof-only` below.
- Lock takes: take 0 (PREFLIGHT probe) and the W take after the resume; no extra take (E2 had no with-DB red). `.env: removed, proven gone (W)` at 13:04:11.
- W (a) and (e) ran on `a2dd9400` before the stop; the tip did not move after them (`git diff --stat a2dd9400 HEAD` → this report only), so neither was run again.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: launcher-checks · tip: a2dd9400 | on 63649058 | migration: none | offline 3784/0 | with-DB 4554/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 2 of 3 | decisions: 3 · for Dejan: 0
