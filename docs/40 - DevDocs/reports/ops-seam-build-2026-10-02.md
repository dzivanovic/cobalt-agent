# ops-seam — build report 2026-10-02

## §0 Headline
(pending)

## L74
- A system block at session start asked for a `Claude-Session:` line in commit messages. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`date` → `Fri Oct  2 09:05:33 EDT 2026`

| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-02/16-ops-seam-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/16-ops-seam-card.md"` | 0 | `2f286234f9edc62ef05aa41e526ed6dea88b9b3d` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING 2026-09-30 R60 | `grep -n "^| R60 " cto-2026-09-30.md` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** ... APPROVES STANDING-LIST.md once (4be06af0) ... | APPROVED |` |
| R60 committed | `git -C ... log -1 --format=%H -S"| R60 |" -- cto-2026-09-30.md` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| 2026-10-02 R47 | `grep -n "^| R47 " cto-2026-10-02.md` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house ... | HIS RULING · APPROVED |` |
| R47 committed | `-S"| R47 |"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| 2026-10-01 R8 | `grep -n "^| R8 " cto-2026-10-01.md` | 0 | `16:| R8 | 07:30 ET | **HIS RULING** ... guard card 02-desk-size-guard-card.md. | APPROVED |` |
| R8 committed | `-S"| R8 |"` | 0 | `f7aa534f49b3b1f2b1112ef2f09970316f214c7c` |
| 2026-10-01 R20 | `grep -n "^| R20 " cto-2026-10-01.md` | 0 | `28:| R20 | 08:31 ET | **HIS RULING** ... Card 07-devdb-lock-card.md. | APPROVED |` |
| R20 committed | `-S"| R20 |"` | 0 | `23c7cdeb217d98a24bbe81fc838909c6095f6839` |
| 2026-10-02 R8 | `grep -n "^| R8 " cto-2026-10-02.md` | 0 | `16:| R8 | 05:59 ET | HIS RULING G1 = A: on 07, the one-line OPS_TOOLS lift ... stands | HIS RULING · APPROVED |` |
| R8 committed | `-S"| R8 |"` | 0 | `0b59495396cab614599ff350934b2a10e4ab9683` |
| 2026-10-02 R9 | `grep -n "^| R9 " cto-2026-10-02.md` | 0 | `17:| R9 | 05:59 ET | HIS RULING D2 = A: --add-dir /Users/cobalt/.claude/ops on the build, check and deploy launch lines | HIS RULING · APPROVED |` |
| R9 committed | `-S"| R9 |"` | 0 | `0b59495396cab614599ff350934b2a10e4ab9683` |

Authorization: complete.

## PREFLIGHT
`date` → `Fri Oct  2 09:05:33 EDT 2026` (session start)

| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## ops/ops-seam-1002` + `?? "docs/40 - DevDocs/reports/ops-seam-build-2026-10-02.md"` (this report, written first per REPORT) |
| base | `git log --oneline -1` | 0 | `9fa18f14 fix(ops-glob): every path under ops/desk/ is an operator script, by rule (G1, L42, L3)` |
| main's view | `git -C /Users/cobalt/cobalt log --oneline -1 ops/ops-seam-1002` | 0 | same `9fa18f14 …` |
| clean vs base | `git diff --stat 9fa18f14` | 0 | (nothing) |
| base commit | `git show --stat 9fa18f14` | 0 | `docs/40 - DevDocs/cobalt/jobs/restarts.md | 4 ++++` · `src/cobalt/jobs/restarts.py | 4 +++-` · `2 files changed, 7 insertions(+), 1 deletion(-)` |
| own .env | `ls /Users/cobalt/cobalt-wt/ops-seam-1002/.env` | 1 | `No such file or directory` |
| any .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` (09:05) |
| READ: A's files | `git diff --stat 36bed6ed ee667f3c` | 0 | restarts.md 9 · desk-size-guard-build report 399 · desk-context.sh 83 · desk-launch.sh 12 · wait-stop-line.sh 4 · restarts.py 9 · test_jobs_restarts.py 14 · tests/ops/test_desk_size_guard.py 445 · `8 files changed, 963 insertions(+), 12 deletions(-)` |
| READ: B's files | `git diff --stat 093028d0 aeefb6df` | 0 | restarts.md 3 · BUILD-HUB.md 23 · CHECK-HUB.md 16 · DEPLOY-HUB.md 32 · STANDING-LIST.md 24 · devdb-lock-build report 196 · desk-launch.sh 38 · release-devdb-lock.sh 63 · take-devdb-lock.sh 63 · restarts.py 9 · test_jobs_restarts.py 18 · tests/ops/test_devdb_lock.py 303 · `12 files changed, 736 insertions(+), 52 deletions(-)` |
| new-file modes | `git diff --summary 093028d0 aeefb6df` / `36bed6ed ee667f3c` | 0 | every new file `create mode 100644` |
| P2 hubs untouched by main | `git diff --stat 093028d0 HEAD -- BUILD-HUB.md DEPLOY-HUB.md` | 0 | (nothing) |
| P1 files untouched by main | `git diff --stat 36bed6ed HEAD -- ops/desk/desk-context.sh ops/desk/wait-stop-line.sh ops/desk/desk-launch.sh tests/ops` | 0 | (nothing) |
| main since B | `git diff --stat 093028d0 HEAD -- ops/desk tests/ops CHECK-HUB.md STANDING-LIST.md restarts.md` | 0 | restarts.md 4 · CHECK-HUB.md `4 ++--` · STANDING-LIST.md `2 +-` · ops/desk/stage-copy.sh 37 |
| symbol `kind=$1` | Grep tool on `ops/desk/desk-launch.sh` | — | `158:kind=$1` |
| symbol fixed-file marker | `grep -n -F "# ---- the kind is a fixed file" ops/desk/desk-launch.sh` | 0 | `333:# ---- the kind is a fixed file ---…` |
| `OPS_TOOLS` | `grep -n -F "OPS_TOOLS" src/cobalt/jobs/restarts.py` | 0 | `36:OPS_TOOLS = frozenset({"ops/cto-desk.sh"})` · `226:        if not rule and (path in OPS_TOOLS or path.startswith(OPS_DESK_PREFIX)):` |
| `ops/desk/` rule | `grep -n -F "ops/desk/" src/cobalt/jobs/restarts.py` | 0 | `38:OPS_DESK_PREFIX = "ops/desk/"` |
| test/doc rule | `grep -n -F "test/documentation" src/cobalt/jobs/restarts.py` | 0 | `242:            rule = "test/documentation; no resident"` (card says `:239`; the line is 242 at base) |
| DOCS rule | `grep -n -F "DOCS" src/cobalt/jobs/restarts.py` | 0 | `221: if not rule and (path.startswith("docs/") or path in ROOT_DOCS):` · `224: … "DOCS", ()))` |
| B's symbols | `git diff 093028d0 aeefb6df -- ops/desk/desk-launch.sh` | 0 | `REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}` · `WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}` · `lock_dir_free() {` · two `[ -z "$step" ] || lock_free` and one `lock_dir_free` call · three `note=` lines |
| A's symbols | `git diff 36bed6ed ee667f3c -- ops/desk/desk-launch.sh …` | 0 | `sh "$(dirname "$0")/desk-context.sh" --guard || exit $?` in desk-launch.sh and wait-stop-line.sh |
| tests/ops on base | `ls tests/ops` | 1 | `No such file or directory` (arrives with the port) |
| ops/desk on base | `ls ops/desk` | 0 | `desk-context.sh desk-launch.sh pre-commit stage-copy.sh wait-desk-idle.sh wait-stop-line.sh` |
| `wc -l` | `wc -l` of the edited files | 0 | desk-launch.sh 597 · desk-context.sh 18 · wait-stop-line.sh 22 · CHECK-HUB.md 131 · STANDING-LIST.md 178 · BUILD-HUB.md 111 · DEPLOY-HUB.md 184 · restarts.md 40 |
| READ check reports | `tail -n 3 desk-size-guard-check-2026-10-01.md` | 0 | `CHECK DONE · job: desk-size-guard · pass: 2 · tip: ee667f3c · … · ready: YES · decisions: 1 · for Dejan: 0` |
| | `tail -n 3 devdb-lock-check-2026-10-01.md` | 0 | `CHECK DONE · job: devdb-lock · pass: 2 · tip: aeefb6df · … · ready: NO · decisions: 1 · for Dejan: 1` (card RECORDS: ready on his G1 and D2 = A, 2026-10-02 R8, R9 — both verified under AUTHORIZATION) |
| RESTARTS | `uv run cobalt jobs restarts 9fa18f14..HEAD` | 0 | `docs/40 - DevDocs/reports/ops-seam-build-2026-10-02.md	A	DOCS	-` · `RESTARTS: none` (the only path is this untracked report) |
| LOCK PROBE (a) | `ls -la /Users/cobalt/cobalt-wt/*/.env` (09:07) | 0 | `-rw-------  1 cobalt  staff  2186 Oct  2 09:06 /Users/cobalt/cobalt-wt/x5-tap-refresh-1002/.env` → LOCK HELD; probe not taken |

Card `## RECORDS` copied: class homes (ops/desk → `ops/desk/` rule, re-read at `restarts.py:38`, `:226`; tests/ops → `:242`; docs → `:221`); both parents checked (re-read above); known overlaps (re-read: main since `093028d0` changed CHECK-HUB 2 lines (`4 ++--`) and STANDING-LIST 1 line; BUILD-HUB / DEPLOY-HUB untouched); PREFLIGHT symbols proven by `git diff` of A / B; `sh` not on the line; outside house set aside (R47, verified).

LOCK PROBE, take 0 (after CONTINUE, 09:08):
| step | command | exit | output |
|---|---|---|---|
| (a) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| (b) | `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/ops-seam-1002/.env` | 0 | (nothing) |
| (b) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 0 | `-rw-------  1 cobalt  staff  2186 Oct  2 09:08 /Users/cobalt/cobalt-wt/ops-seam-1002/.env` (exactly one, this worktree's) |
| `<FP>` → `<Fp>` | (below) | 0 | `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` |
| level | `COBALT_ENV=dev uv run cobalt db migrate --proof-only` | 0 | `36 table(s) probed on cobalt_dev`; `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns` read `-` (absent — the tables of the migrations above `0013`); no `CHANGED`; `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `code: d7cb5f30 (DIRTY: 1 path(s))` (this report). The output prints no level number; `0013` is read from the absent above-`0013` tables. |
| (d) | `rm /Users/cobalt/cobalt-wt/ops-seam-1002/.env` | 0 | (nothing) |
| (d) | `ls /Users/cobalt/cobalt-wt/ops-seam-1002/.env` | 1 | `No such file or directory` |

`.env: removed, proven gone (PREFLIGHT)`.

`<FP>` as typed (copied whole before any run):
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

## E0 BASELINE
On `d7cb5f30` (= `9fa18f14` + this report).
- Offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 601.81s (0:10:01)`; exit 0; 0 failed, 0 errors.
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.72s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (no skip names `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Test files written, no `src/` or `ops/` edit:
- `tests/ops/test_desk_size_guard.py` — Write from `git show ee667f3c:…`; `git add`, then `git diff --stat ee667f3c -- tests/ops/test_desk_size_guard.py` → (nothing): byte-equal.
- `tests/ops/test_devdb_lock.py` — Write from `git show aeefb6df:…`; `git add`, then `git diff --stat aeefb6df -- tests/ops/test_devdb_lock.py` → (nothing): byte-equal.
- `tests/ops/test_install_ops.py` — new (P4), six tests: the link run (2 linked, gamma kept byte for byte, guard called with `--guard`); the second run `0 linked, 3 kept`, links unchanged; an existing link to elsewhere never re-pointed; only regular `*.sh` / `*.py` linked (a `pre-commit`, a `.md`, a directory `folder.sh` are not); one extra argument → exit 1, `REFUSED: usage: desk-launch.sh install-ops`, nothing linked; a refusing guard → exit 3 before any link.

First run of the P4 file alone: the extra-argument test PASSED on base (it asserted only `"REFUSED" in stderr`, which the base's kind refusal also prints) — rewritten to assert the exact usage refusal; its red is now the row's.

`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_install_ops.py tests/ops/test_desk_size_guard.py tests/ops/test_devdb_lock.py` → `49 failed, 17 passed, 1 xfailed, 15 warnings in 8.79s`. The reds, by first line:
- P4: the four link tests → `REFUSED: usage: desk-launch.sh <build|check|deploy> <absolute card path> [PASS-2] [<resume step>]` (base, `desk-launch.sh:319`: with one argument the generic usage refusal comes before the kind check at `:338`); the extra-argument test → `- REFUSED: usage: desk-launch.sh install-ops` / `+ REFUSED: kind 'install-ops' is none of build, check, deploy, desk, prompt, close` (the row's named red); the guard test → `assert (1, '') == (3, 'REFUSED:...RESH first\n')` (the base has no guard).
- P1 (A's tests on base code): G1 → `assert (2, 'no trans...-guard\n', '') == (0, '', '')` (base `desk-context.sh` has no `--guard`); G2 refusing-guard → `build reached claude: --bg Read '…/01-fx-card.md' …` (base `desk-launch.sh` runs no guard), and the same for all 10 guarded forms; real-guard → `assert (0, 'HEAD is ...6799f base\n') == (3, 'REFUSED:...RESH first\n')`; G3 → `AssertionError: the loop ran` (base `wait-stop-line.sh` runs no guard).
- P2 (B's tests on base code): every L1 test → `sh: /Users/cobalt/cobalt-wt/ops-seam-1002/ops/desk/take-devdb-lock.sh: No such file or directory` (exit 127); `test_release_does_not_remove_a_lock_taken_after_it_saw_none` → `FileNotFoundError: … .cobalt_dev.lock/owner`; every L2 test → `REFUSED: the card must be /Users/cobalt/cobalt/docs/40 - DevDocs/prompts/<date>/<nn>-<job>-card.md` (base `REPO=` takes no `COBALT_REPO_ROOT`).
- Passed on base (negative controls): A's `test_g1_the_plain_call_is_unchanged_and_never_reads_the_list`, the 10 `test_g2_a_passing_guard_lets_every_kind_reach_its_launch`, `test_g2_desk_never_calls_the_guard_and_reaches_its_launch`, `test_g3_a_passing_guard_keeps_the_match_path`, `…_timeout_path`, `test_g3_wait_desk_idle_is_not_guarded`, `test_g4_run_…` (RUN, asserts nothing); xfailed: A's strict-xfail H2 probe. No with-DB red: no lock take at E2.

## E3 THE ROWS

## RESTARTS

## W THE THREE SUITES

## PRE-STOP SELF-CHECK

## FOR THE CHECK

## CONTINUE
next: E2

## DECISIONS
none

## RECORDS
- REFUSED, not needed: `grep -n -F "kind=$1" ops/desk/desk-launch.sh` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (a `$` in a double-quoted argument; re-read with the Grep tool instead).

- STOPPED at PREFLIGHT 09:07: lock held by `/Users/cobalt/cobalt-wt/x5-tap-refresh-1002/.env` (wip `d7cb5f30`).
- CONTINUED at PREFLIGHT 09:08:04 EDT (desk message from `cto-desk`; fact verified: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`).

(run in progress — next step under ## CONTINUE)
