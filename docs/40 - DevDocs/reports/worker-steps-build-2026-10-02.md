# worker-steps — build report 2026-10-02

## §0 Headline
(run in progress)

## L74
A system reminder at session start asked that commits carry a `Claude-Session: https://claude.ai/code/session_016FKCUva3Y7hZSHKpjCG6W1` line. Recorded here once, and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
Started 10:08 ET (`date` → `Fri Oct  2 10:08:06 EDT 2026`).

| rule | command | exit | result |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | nothing |
| card has no placeholder | `grep -n -E "«FIL[L]" ".../2026-10-02/19-worker-steps-card.md"` | 1 | nothing |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/19-worker-steps-card.md"` | 0 | `2f286234f9edc62ef05aa41e526ed6dea88b9b3d` |
| card unchanged | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | nothing |
| STANDING LIST R60 | `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** (...) APPROVES STANDING-LIST.md once (4be06af0) ... | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULINGS R47 (also HOUSE A's `overruled 2026-10-02 R47`) | `grep -n "^| R47 " ".../reports/cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house ... | HIS RULING · APPROVED |` |
| R47 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |

Result: authorized.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 10:08:06 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/worker-steps-1002` |
| at BASE | `git log --oneline -1` | 0 | `9fa18f14 fix(ops-glob): every path under ops/desk/ is an operator script, by rule (G1, L42, L3)` |
| main repo sees branch | `git -C /Users/cobalt/cobalt log --oneline -1 ops/worker-steps-1002` | 0 | `9fa18f14 …` (same commit) |
| first launch | `git diff --stat 9fa18f14` | 0 | nothing |
| BASE | `git show --stat 9fa18f14` | 0 | `docs/40 - DevDocs/cobalt/jobs/restarts.md | 4 ++++`, `src/cobalt/jobs/restarts.py | 4 +++-`, 2 files changed, 7 insertions(+), 1 deletion(-) |
| no own .env | `ls /Users/cobalt/cobalt-wt/worker-steps-1002/.env` | 1 | `No such file or directory` |
| no .env anywhere | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| symbol `committed` | `grep -n -F "committed() {" ops/desk/desk-launch.sh` | 0 | `110:committed() {` |
| symbol `field` | `grep -n -F "field() {" ops/desk/desk-launch.sh` | 0 | `364:field() {` |
| symbol `cmd_migrate` | `grep -n "def cmd_migrate" src/cobalt/db_migrations/cli.py` | 0 | `575:def cmd_migrate(args: argparse.Namespace) -> None:` |
| proof-only printer | `grep -n -A 40 "def _print_probe" src/cobalt/db_migrations/cli.py` | 0 | `449:def _print_probe(…)`: a table of `table side schema rows digest secs`, then `NOTHING WAS APPLIED …`, then `_code_line()`. No level line. |
| ledger table | Grep `schema_migrations|applied_migrations|migration_level` in `src/cobalt` | — | `No files found` |
| ops/desk rule (RECORDS) | `grep -n -F "ops/desk/" src/cobalt/jobs/restarts.py` | 0 | `38:OPS_DESK_PREFIX = "ops/desk/"` |
| lock scripts (READ) | `git show aeefb6df:ops/desk/take-devdb-lock.sh`, `…release-devdb-lock.sh`, `…:tests/ops/test_devdb_lock.py` | 0 | read whole; usage `take-devdb-lock.sh <worktree> <minutes>` (exits 0/1/2/4), `release-devdb-lock.sh <worktree>` (exits 0/1/2/3) |
| tests/ops on base (RECORDS) | `ls tests/ops` | 1 | `No such file or directory` |
| agy-trial scratch | `ls /Users/cobalt/cobalt-wt/agy-trial/scratch` | 0 | exists (tribunal-bars-0920 among others) |
| RECORDS report | `tail -n 3 ".../reports/brain-direction-2026-10-02.md"` | 0 | last line: `DIRECTION WRITTEN, REVISED 08:25 ET — cards 15–19, 21 and the cut 13 are in prompts/2026-10-02/ as the brain names them` |
| RESTARTS empty | `uv run cobalt jobs restarts 9fa18f14..HEAD` | 0 | one row, this report (uncommitted, `DOCS -`); `RESTARTS: none` |
| wc -l | none: every file the rows name is NEW (the card: "No existing file is edited") | — | — |

Files read per `## READ`: BUILD-HUB.md whole; CHECK-HUB.md whole; DEPLOY-HUB.md lines 1–36 (title `INSTALL: 2026-09-30 R60 (+ R62 string changes)`, `## AUTHORIZATION`); `ops/desk/stage-copy.sh`, `ops/desk/desk-launch.sh` whole; `cli.py` 575–694 and 350–483.

THE LOCK PROBE (take 0), 10:09 ET:
- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → exit 1, `no matches found`.
- (b) `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/worker-steps-1002/.env` → exit 0; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 10:09 /Users/cobalt/cobalt-wt/worker-steps-1002/.env` (one line).
- `<FP>` (typed exactly as BUILD-HUB THE LOCK) → `<Fp>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → exit 0, WHOLE:
```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
archive_incidents    system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.01
archive_progress     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.00
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.51
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   226          8ac36f0333cc551ef34de32abf13a912   0.00
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
36 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 29 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007; card_stop_edits: 1 card column(s) added by 0007. Proof cost: total 5.6 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
code: 9fa18f14 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/worker-steps-1002
```
  Read as W (b) tells a worker: no `CHANGED`; every table of 0016 and later (`drc_*`, `voice_turns`, `legs`, `prediction_records`) shows schema `-`. The output states no level number; consistent with `0013`.
- (d) `rm /Users/cobalt/cobalt-wt/worker-steps-1002/.env` → exit 0; `ls /Users/cobalt/cobalt-wt/worker-steps-1002/.env` → `No such file or directory`. `.env: removed, proven gone (PREFLIGHT)` 10:09 ET.

Card `## RECORDS`, copied and re-read:
- RESTARTS class homes: `ops/desk/*` → the `ops/desk/` rule (`restarts.py:38 OPS_DESK_PREFIX = "ops/desk/"` re-read); `tests/ops/*` → test/documentation (read at RESTARTS).
- `tests/ops/` is not on the base: `ls tests/ops` → `No such file or directory` (re-read).
- The suites run `tests/cobalt` and `tests/taxonomy`; no with-DB test is added: `TREE STATE: unchanged`.
- The lock scripts are not on the base: `ls ops/desk` → `desk-context.sh desk-launch.sh pre-commit stage-copy.sh wait-desk-idle.sh wait-stop-line.sh` (re-read).
- His order sets aside the outside house: `tail -n 3` of `brain-direction-2026-10-02.md` quoted above; R47 quoted in AUTHORIZATION.

PROVEN BY FIRST REAL USE: as BUILD-HUB's table (pytest strings at E0; git add/commit at E2's red commit; `COBALT_ENV=dev uv run pytest` and the migrate forward and rollback at W).

## E0 BASELINE
- Offline, `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, on `9fa18f14`) → exit 0; summary line 749: `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 645.49s (0:10:45)`. 0 failed, 0 errors.
- Live-note, `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.81s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.
- Seen in the offline output: pytest writes ANSI colour codes even into a file. `gate.sh` strips them before it reads a summary.

## E2 RED
Five NEW test files under `tests/ops/` (no `conftest.py`); no with-DB test, no RUN row.
`uv run pytest -q -rf -p no:cacheprovider --color=no --tb=no tests/ops/test_authorize.py tests/ops/test_preflight.py tests/ops/test_gate.py tests/ops/test_stage_set.py tests/ops/test_house_probe.py` → `75 failed, 15 warnings in 69.07s (0:01:09)`. Every red's first line is the row's named reason, no such file, e.g.:
- S1: `AssertionError: sh: /Users/cobalt/cobalt-wt/worker-steps-1002/ops/desk/authorize.sh: No such file or directory` (`assert 127 == 0`), 17 tests.
- S2: `… ops/desk/preflight.sh: No such file or directory` (`assert 127 == 1`), 15 tests.
- S3: `… ops/desk/gate.sh: No such file or directory` (`assert 127 == 1`), and in the two lock-script tests `FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-wt/worker-steps-1002/ops/desk/gate.sh'` (the copy beside the stub lock scripts), 26 tests.
- S4: `… ops/desk/stage-set.sh: No such file or directory`, 8 tests.
- S5: `… ops/desk/house-probe.sh: No such file or directory`, 9 tests.
Commit `7e4ecee2 wip(worker-steps): red — the five step scripts do not exist (S1-S5)`.

## E3 THE ROWS
Built in card order, each a NEW file under `ops/desk/` (POSIX `sh`, inline `python3` only in `gate.sh` to read the hub file). No existing file edited. Commit `8f3c4876 feat(worker-steps): authorize, preflight, gate, stage-set and house-probe — a worker step in one call (S1-S5, L3, L76, L35)`.

**S1 `authorize.sh`.** `tests/ops/test_authorize.py` → `17 passed, 15 warnings in 2.91s`.
- Mutation 1, the row's `APPROVED` requirement dropped (`*"HIS RULING"*APPROVED*) ok=0` → `*) ok=0`): `1 failed, 16 passed` — `FAILED tests/ops/test_authorize.py::test_a_ruling_row_without_approved_fails_naming_it`, `assert 0 == 1`. Undone.
- Mutation 2, the at-HEAD proof dropped (`if [ -n "$line" ] && git -C "$REPO" show "HEAD:$rel" … | grep -q -x -F -e "$line"` → `if [ -n "$line" ]`): `1 failed, 16 passed` — `FAILED …::test_approved_only_in_the_working_tree_over_a_committed_unapproved_row_fails`, `assert 0 == 1`. Undone.

**S2 `preflight.sh`.** `tests/ops/test_preflight.py` → `15 passed, 15 warnings in 3.09s`.
- Mutation, the docs-only rule above TIP dropped (`others=$(git log --format= --name-only …| grep -v '^docs/')` → `others=""`): `1 failed, 14 passed` — `FAILED tests/ops/test_preflight.py::test_a_check_with_a_src_commit_above_tip_fails`, `assert 0 == 1` (the output ended `PREFLIGHT OK`). Undone. Negative control `test_a_check_on_a_built_branch_passes_with_a_docs_only_commit_above_tip` stayed green.

**S3 `gate.sh`.** `tests/ops/test_gate.py` → `26 passed, 15 warnings in 9.31s` on the first write. Reading it before the mutations, I found a defect of my own: `fp0=$(fingerprint)` ran the fingerprint in a subshell, so a failed query's `exit 1` did not stop the run and its message would have landed in `<F0>`. Fixed (the fingerprint sets `FPV` in the main shell and returns its exit; the rollback path never exits from inside the trap), and two tests added for it: `test_a_failed_fingerprint_at_the_start_stops_and_releases`, `test_a_failed_fingerprint_after_the_forward_still_rolls_back` → `28 passed, 15 warnings in 9.97s`.
- Mutation 1 (X1), the trap's rollback removed (`rollback_and_prove || st=6` → `:`): `3 failed, 25 passed` — `test_pass_2_red_still_rolls_back_and_releases` (`Right contains 2 more items, first extra item: 'rollback'`), `test_a_failed_fingerprint_after_the_forward_still_rolls_back` (same), `test_a_term_mid_pass_2_still_rolls_back_and_releases` (`assert ['fp', 'pytest'] == ['rollback', 'fp']`). Undone.
- Mutation 2, the fingerprint fix undone (`fingerprint || { say …; exit 1; }` → `fingerprint || true`, at F0 and at F1): `2 failed, 26 passed` — `test_a_failed_fingerprint_at_the_start_stops_and_releases` (`assert 6 == 1`), `test_a_failed_fingerprint_after_the_forward_still_rolls_back` (`assert 0 == 1`). Undone. These two tests were written after the script, so this mutation is their red.
- Mutation 3 (X2), pass 1 no longer the hub's line (`PASS1=$(cat "$tmp/pass1")` → `PASS1="$(cat "$tmp/pass1") -x"`): `2 failed, 26 passed` — `test_withdb_green_runs_the_hub_commands_byte_for_byte_in_order` (`Left contains one more item: '-x'`), `test_a_deselect_goes_into_pass_1_and_its_id_at_the_end_of_pass_2` (`At index 36 diff: '-x' != '--deselect'`). Undone.

**S4 `stage-set.sh`.** `tests/ops/test_stage_set.py` → `8 passed, 15 warnings in 2.65s`.
- Mutation 1 (X4), the copy taken from the working file (`git -C "$1" show "$2" > "$3"` → `cp "$1/${2#*:}" "$3"`): `1 failed, 7 passed` — `test_the_whole_set_is_staged_byte_equal_to_git_at_tip`: `FAILED: …/files/wt/src/a dir/with space.py differs from 9802dd57:src/a dir/with space.py (230f0bb9…, not b40139d3…)`, `assert 1 == 0`. Undone.
- Mutation 2, the `.env` refusal dropped: `1 failed, 7 passed` — `test_an_env_path_in_the_diff_is_refused_with_the_dest_left_empty`, `assert 0 == 1` (it staged `STAGED 10 files · 2162 bytes · commits 3`). Undone.

**S5 `house-probe.sh`.** `tests/ops/test_house_probe.py` → `9 passed, 15 warnings in 9.22s`.
- Mutation 1, the limit never fires (`"$waited" -lt "$LIMIT"` → `-lt 100000`): `2 failed, 7 passed in 65.87s` — `test_all_three_by_default_up_out_and_timeout` (`assert (… - …) < 25`, it waited ~30 s), `test_gemini_is_spelled_as_the_hub_launch_with_a_three_minute_print_timeout` (`assert ['gemini: UP'] == ['gemini: OUT — TIMEOUT']`). Undone.
- Mutation 2, the Sol spelling (`-c model_reasoning_effort="high"` dropped): `1 failed, 8 passed` — `test_the_sol_stub_sees_the_hub_files_probe_exactly` (`At index 6 diff: 'Reply with only the word OK.' != '-c'`). Undone.

After every undo: `grep -n -E "100000|env-mutated|\) -x|\|\| true|^ +:$"` over the five scripts → exit 1, nothing. All five files together: `77 passed, 15 warnings in 24.93s`. `git diff --stat` before the commit → `tests/ops/test_gate.py | 23 +++` only (the scripts were untracked).

DevDocs line: none written. No page under `docs/40 - DevDocs/cobalt/` documents `ops/desk/`, and the card fences every existing file ("No existing file is edited"). Recorded under `## RECORDS`.

## RESTARTS
`uv run cobalt jobs restarts 9fa18f14..HEAD` (HEAD `8f3c4876`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/worker-steps-build-2026-10-02.md	A	DOCS	-
ops/desk/authorize.sh	A	operator script; no Cobalt reader	-
ops/desk/gate.sh	A	operator script; no Cobalt reader	-
ops/desk/house-probe.sh	A	operator script; no Cobalt reader	-
ops/desk/preflight.sh	A	operator script; no Cobalt reader	-
ops/desk/stage-set.sh	A	operator script; no Cobalt reader	-
tests/ops/test_authorize.py	A	test/documentation; no resident	-
tests/ops/test_gate.py	A	test/documentation; no resident	-
tests/ops/test_house_probe.py	A	test/documentation; no resident	-
tests/ops/test_preflight.py	A	test/documentation; no resident	-
tests/ops/test_stage_set.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row; nothing added to `configs/cobalt/jobs.yaml`.

## W THE THREE SUITES
`<tip>` = `8f3c4876`.
- (a) OFFLINE, `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → exit 0, line 749: `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 633.67s (0:10:33)`. 0 failed, 0 errors → `<p>` = 3784. This build adds no test under `tests/cobalt` or `tests/taxonomy`; its 77 tests are in `tests/ops/` and ran by name at E2 and E3.
- (b) THE LOCK (a), 10:49 ET: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 10:37 /Users/cobalt/cobalt-wt/desk-tools-a-1002/.env`. Another worktree holds the lock. I did not take it: no `.env` copied, nothing run on `cobalt_dev`, no migration applied.

## PRE-STOP SELF-CHECK

## FOR THE CHECK

## CONTINUE
next: W (b) (tip 8f3c4876; W (a) is green and stands). Stopped 10:49 ET: the cobalt_dev lock is held by desk-tools-a-1002.

## DECISIONS

## RECORDS
- `.env: removed, proven gone (PREFLIGHT)` 10:09 ET.
- No DevDocs page line: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/`, and the card fences every existing file.
- The card's RECORDS cite `restarts.py:239` for `tests/*`; at the base, line 239 is the HARNESS rule and the `tests/` rule is at line 241 (`if not rule and path.startswith("tests/"):`). The class itself is as the card says (the RESTARTS table shows `test/documentation; no resident`).
- The L74 line (a `Claude-Session:` request at session start): recorded under `## L74`, not acted on.
- W stopped at (b), 10:49 ET: lock held by `/Users/cobalt/cobalt-wt/desk-tools-a-1002/.env` (10:37). Nothing taken, nothing to roll back.

FAILED: W (b) — cobalt_dev lock held — /Users/cobalt/cobalt-wt/desk-tools-a-1002/.env
