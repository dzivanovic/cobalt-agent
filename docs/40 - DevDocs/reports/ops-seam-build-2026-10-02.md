# ops-seam — build report 2026-10-02

## §0 Headline
desk-size-guard (`ee667f3c`) and devdb-lock (`aeefb6df`) are ported onto `9fa18f14` by Edit and Write, and `desk-launch.sh` gains `install-ops`. Rows P1–P4 are built. Every ported script and hub file is byte-equal to its side. `desk-launch.sh`, `CHECK-HUB.md` and `STANDING-LIST.md` carry every hunk of both sides, and the counts match their lines.
Two seams the card did not state forced a 2-line edit in each ported test file. Both are under `## DECISIONS` for the judgment seat; no script was changed for them.
Three suites green on `551f07e0`: offline 3784, with-DB 4383 + 171, live-note 146. `tests/ops`: 68 passed. `cobalt_dev` at 0013 (F2 = F0); `.env` removed; RESTARTS: none.

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
Commit `dd3dc7ed` — `feat(ops-seam): port desk-size-guard and devdb-lock onto one base; desk-launch install-ops (P1, P2, P3, P4, L3, L42, L72)`. Every change made by Edit (changed files, hunk by hunk) or Write (new files, from `git show`).

**P1** — `desk-context.sh` (A's one hunk), `wait-stop-line.sh` (A's one hunk), `tests/ops/test_desk_size_guard.py` (written at E2).
- Proof: `git diff --stat ee667f3c HEAD -- ops/desk/desk-context.sh ops/desk/wait-stop-line.sh` → (nothing). `git diff --stat ee667f3c HEAD -- ops/desk/desk-context.sh ops/desk/wait-stop-line.sh tests/ops/test_desk_size_guard.py` → `tests/ops/test_desk_size_guard.py | 4 ++--` · `1 file changed, 2 insertions(+), 2 deletions(-)`. The test file is NOT byte-equal: DECISION P1 below, diff quoted there.
- Mutation: `desk-context.sh` `if [ "${1:-}" = "--guard" ]` → `"--guard-MUTATED"`; `uv run pytest … tests/ops/test_desk_size_guard.py` → `11 failed, 27 passed, 1 xfailed`; first red `test_desk_size_guard.py:121: AssertionError: assert (2, 'no trans...-guard\n', '') == (0, '', '')`; every G1 test and `test_g2_the_real_guard_refuses_a_build_and_lets_the_desk_launch` red. Undone with Edit.

**P2** — `take-devdb-lock.sh`, `release-devdb-lock.sh` (Write from `git show aeefb6df:`), `BUILD-HUB.md` (B's 11 hunks), `DEPLOY-HUB.md` (B's hunks), `tests/ops/test_devdb_lock.py` (E2).
- Pre-proof (on BASE): `git diff --stat 093028d0 HEAD -- BUILD-HUB.md DEPLOY-HUB.md` → (nothing).
- Proof: `git diff --stat aeefb6df HEAD -- ops/desk/take-devdb-lock.sh ops/desk/release-devdb-lock.sh BUILD-HUB.md DEPLOY-HUB.md` → (nothing). With `tests/ops/test_devdb_lock.py` added → `tests/ops/test_devdb_lock.py | 5 ++++-` · `1 file changed, 4 insertions(+), 1 deletion(-)`. The test file is NOT byte-equal: DECISION P2 below.
- Mutation: `take-devdb-lock.sh` `mkdir "$LOCK"` → `mkdir -p "$LOCK"` (not atomic); `uv run pytest … tests/ops/test_devdb_lock.py` → `2 failed, 20 passed`; first red `test_devdb_lock.py:87: AssertionError: {'alpha': 0, 'beta': 0}` (`test_two_takes_at_once_exactly_one_wins`), then `test_the_loser_waits_then_exits_4_naming_the_holder` (`assert 0 == 4`). Undone.

**P3** — `desk-launch.sh`, `CHECK-HUB.md`, `STANDING-LIST.md`, `restarts.md`.
- `git diff ee667f3c -- ops/desk/desk-launch.sh` (before P4) → exactly B's hunks: the header lock paragraph, `COBALT_REPO_ROOT` / `COBALT_WT_ROOT`, `lock_dir_free()`, `[ -z "$step" ] || lock_free` (build, check), `lock_dir_free` (deploy), the three `note=` lines. `git diff aeefb6df -- ops/desk/desk-launch.sh` (before P4) → exactly A's two hunks (the FIRST-guard header paragraph, the guard block after `kind=$1`). After P4, `git diff aeefb6df -- ops/desk/desk-launch.sh` → A's two hunks plus P4's (the header usage line and WHAT IT DOES entry, the `install-ops` refusal-list words, the usage string, the `install-ops` block, the kind refusal message).
- `CHECK-HUB.md`: `git diff aeefb6df -- CHECK-HUB.md` → only the launch line (+ `"Bash(sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh *)"`, main's R37) and THE LIST line (35 allow, the 30 strings of BUILD-HUB, plus the staging string). `git diff 9fa18f14 -- CHECK-HUB.md` → B's hunks (LAUNCH paragraph, launch line + 2 lock strings + `--add-dir /Users/cobalt/.claude/ops`, THE LIST, (b), RECOVERY, PREFLIGHT THE LOCK, 7 (v), 8 CLOSE).
- Counts, line 10 of `CHECK-HUB.md`: `grep -n -o -F "\"Bash("` → 31 hits on line 10, one of them the deny `"Bash(git push*)"` (`grep … "\"Bash(git push*)\""` → `10:`), so 30 Bash allow; `grep -n -o -F "\"Edit("` → 2 on line 10; plus `"Read" "Grep" "Glob"` = 35 allow. Each lock string once: `take-devdb-lock.sh *)` → `10:` only; `release-devdb-lock.sh *)` → `10:` only; `stage-copy.sh *)` → `10:` and `12:` (the line and its prose); `--add-dir /Users/cobalt/.claude/ops` → `10:`. `BUILD-HUB.md` line 12: `"Bash(` → 27 hits, one the push deny → 26 Bash + 4 file = 30 (prose: `30 allow … 26 Bash strings`).
- `STANDING-LIST.md`: `git diff aeefb6df -- STANDING-LIST.md` → only the §2 title: `35 allow, 3 deny (+1 staging string …, his 2026-10-01 R37, R39 …) · … · the same four --add-dir roots`. Every other hunk of B is in.
- `restarts.md`: `git diff 9fa18f14 -- restarts.md` → + `## 2026-10-01 — desk-size-guard`, the three `ops/desk/` paths, `They are classified `operator script; no Cobalt reader` and derive no restart.` A's `OPS_TOOLS now also holds…` line and the sentence naming the unported `test_the_desk_ops_scripts_…` are dropped; B's section (all `OPS_TOOLS`) is not ported.
- NOT ported, as the card says: both `OPS_TOOLS` hunks of `src/cobalt/jobs/restarts.py`, their tests in `tests/cobalt/test_jobs_restarts.py`, the two build reports. `git diff --stat 9fa18f14 HEAD -- src` → (nothing).
- Mutations: (A side) `desk-launch.sh` `if [ "$kind" != "desk" ]` → `= "MUTATED"`; `tests/ops/test_desk_size_guard.py tests/ops/test_install_ops.py` → `13 failed, 31 passed, 1 xfailed`; all 10 `test_g2_a_refusing_guard_stops_every_kind_but_desk_before_any_launch[…]`, `test_g2_the_real_guard_…`, `test_install_ops_links_the_missing_names_and_keeps_the_existing_one`, `test_a_refusing_guard_stops_install_ops_before_any_link` red. (B side) build's `[ -z "$step" ] || lock_free` → `lock_free`; `test_devdb_lock.py -k "launch or resume or deploy"` → `1 failed, 5 passed`; red `test_devdb_lock.py:254: AssertionError: WARNING: desk size unread — guard skipped` / `REFUSED: with-DB launch refused: the cobalt_dev lock is held (…/wt/beta/.env) (L76)`. Both undone.
- RUN (asserts nothing): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `66 passed, 1 xfailed, 15 warnings in 69.09s (0:01:09)` (no skip). `uv run cobalt jobs restarts 9fa18f14..HEAD` (tree before the commit) → every `ops/desk/` path `operator script; no Cobalt reader	-`; no `UNCLASSIFIED`; `src/cobalt/jobs/restarts.py` absent; `RESTARTS: none` (whole table under `## RESTARTS`).

**P4** — `desk-launch.sh` kind `install-ops`; `tests/ops/test_install_ops.py`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=short tests/ops/test_install_ops.py` → `6 passed, 15 warnings in 0.91s`.
- Mutation 1 (undo the fix): `if [ "$kind" = "install-ops" ]` → `"install-ops-MUTATED"` → `5 failed, 1 passed`; first red `test_install_ops.py:66: AssertionError: REFUSED: usage: desk-launch.sh <build|check|deploy> <absolute card path> [PASS-2] [<resume step>]`; the extra-argument test red on `+ REFUSED: kind 'install-ops' is none of build, check, deploy, desk, prompt, close, install-ops`. The guard test stays green under it (the guard refuses before any kind); it is red under P3's A-side mutation above.
- Mutation 2 (X4, re-point): `ln -s` → `ln -sfh` and the KEPT test without `|| [ -L "$links/$name" ]` → `1 failed, 5 passed`; red `test_install_ops.py:102: AssertionError: assert 'KEPT alpha.sh' in ['LINKED alpha.sh', 'KEPT gamma.sh', 'LINKED beta.py', 'install-ops: 2 linked, 1 kept']` (`test_an_existing_link_to_elsewhere_is_never_re_pointed`). Undone.

After every undo: `git diff --stat` (before the commit) → the ten fix files only, as committed; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` on the restored tree → `66 passed, 1 xfailed, 15 warnings in 69.06s (0:01:09)`.

DevDocs: `ops/desk/*` has no page under `docs/40 - DevDocs/cobalt/` (Grep `desk-launch` there → no files); the one page the card names, `restarts.md`, carries A's surviving lines. No new page written (it would widen the job).

## RESTARTS
`uv run cobalt jobs restarts 9fa18f14..HEAD` (HEAD `dd3dc7ed`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/jobs/restarts.md	M	DOCS	-
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/ops-seam-build-2026-10-02.md	M	DOCS	-
ops/desk/desk-context.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/release-devdb-lock.sh	A	operator script; no Cobalt reader	-
ops/desk/take-devdb-lock.sh	A	operator script; no Cobalt reader	-
ops/desk/wait-stop-line.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_size_guard.py	A	test/documentation; no resident	-
tests/ops/test_devdb_lock.py	A	test/documentation; no resident	-
tests/ops/test_install_ops.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row; `src/cobalt/jobs/restarts.py` not in the table; nothing classified in `configs/cobalt/jobs.yaml`.

## W THE THREE SUITES
TREE STATE: `unchanged` — this build adds no with-DB test and no migration (`git diff --stat 9fa18f14 HEAD -- src` → nothing; the new tests are all under `tests/ops/`, offline). Pass 1 and pass 2 run byte for byte with no added `--deselect`.

### W, first run — on `dd3dc7ed`
- (a) `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 573.46s (0:09:33)`. This build adds no test under `tests/cobalt` / `tests/taxonomy`; its tests are `tests/ops/` (run in E3).
- (b) lock taken 09:43:55: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/ops-seam-1002/.env`; `ls -la …/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 09:43 /Users/cobalt/cobalt-wt/ops-seam-1002/.env` (one line). `<F0>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`. `--proof-only` → `36 table(s) probed on cobalt_dev`; the eight above-`0013` tables read `-`; no `CHANGED`; `NOTHING WAS APPLIED`.
- (c) PASS 1, executed byte for byte as the hub's pass-1 command, no addition → `4383 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 704.28s (0:11:44)`. SKIPPED, each quoted: `test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` · `test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged` · `test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` · `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` · `test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read` · `taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — …` · `taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — …`.
- (c2) `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → applied `0001`…`0011`, `0013`…`0022` in order (`0014_radar_handicap` … `0022_prediction_records`); 8 tables `CREATED`; `content UNCHANGED on every table`; no `CHANGED`. **`dev forward: APPLIED 09:56:18`**. `<F1>` = `893 · 44 · 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2, executed byte for byte as the hub's pass-2 command (no addition) → `171 passed, 1 deselected, 5 warnings in 218.59s (0:03:38)`. This build has no with-DB test id.
- (c3r) no constructed ticker: this build writes no with-DB test; the query has nothing to name, not run.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` → `0022` … `0014` reversed newest first; 8 tables `DROPPED`; `content UNCHANGED on every table`. `<F2>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → **`cobalt_dev: 0013 — F2 = F0`** (10:00:34). Lock (d): `rm …/ops-seam-1002/.env`; `ls …/ops-seam-1002/.env` → `No such file or directory`; `ls -la …/*/.env` → `no matches found`. `.env: removed, proven gone (W)`.
- (e) live-note → `146 passed, 1 skipped, 15 warnings in 25.92s`; skip `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …` (no skip names `COBALT_LIVE_VAULT_ROOT`).
- Then PRE-STOP SELF-CHECK (2) found two `install-ops` entry paths no test pinned (a symlink under `ops/desk/`, a missing link folder). Pinned in `tests/ops/test_install_ops.py` (`test_a_symlink_under_ops_desk_is_not_linked`, `test_a_missing_link_folder_is_refused_and_never_made`); green on the fix (`8 passed`); RED under their mutations — `[ -f "$src" ] && [ ! -L "$src" ]` → `[ -f "$src" ]` and the `-d` refusal → `mkdir -p "$links"` → `2 failed, 6 passed`; reds `test_install_ops.py:124: … At index 2 diff: 'delta.sh' != 'gamma.sh'` and `test_install_ops.py:133: AssertionError: assert 0 == 1` (stdout `LINKED alpha.sh / LINKED gamma.sh / LINKED beta.py / install-ops: 3 linked, 0 kept`); undone, `git diff --stat` → the test file and this report only. Commit `551f07e0` `fix(ops-seam): pin install-ops' two unpinned entry paths — a symlinked source, a missing link folder (P4, K25)`. RESTARTS again → the same table, `RESTARTS: none`. W again from (a) on `551f07e0`, one more lock take (`## RECORDS`).

### W, second run — on `551f07e0` = `<tip>`
- (a) `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 606.60s (0:10:06)` → `<p>` = 3784.
- (b) lock taken 10:12:11: `ls -la …/*/.env` → `no matches found`; `cp …`; `ls -la …/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 10:12 /Users/cobalt/cobalt-wt/ops-seam-1002/.env`. `<F0>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`. `--proof-only` → the same 36 tables, the eight above-`0013` tables `-`, no `CHANGED`, `NOTHING WAS APPLIED`, `code: 551f07e0 (DIRTY: 1 path(s))` (this report).
- (c) PASS 1, executed WHOLE (the hub's pass-1 command, nothing added):
  `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk`
  → `4383 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 748.70s (0:12:28)` → `<d1>` = 4383. The seven SKIPPED lines are the same seven quoted under the first run (`test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py:266`, `test_s3_c4_experiments.py:95`, `taxonomy/test_catalyst.py:365`, `taxonomy/test_predicate.py:262`), each with the reason quoted there.
- (c2) `COBALT_ENV=dev uv run cobalt db migrate` → `0001`…`0011`, `0013`…`0022` applied in order; 8 `CREATED`; `content UNCHANGED on every table`; no `CHANGED`. **`dev forward: APPLIED 10:25:20`**. `<F1>` = `893 · 44 · 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2, executed WHOLE (the hub's pass-2 command, nothing added):
  `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones`
  → `171 passed, 1 deselected, 5 warnings in 226.95s (0:03:46)` → `<d2>` = 171; `<d>` = 4383 + 171 = 4554. This build has no with-DB test id.
- (c3r) no constructed ticker (no with-DB test in this build); not run.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` → `0022` … `0014` reversed newest first; 8 `DROPPED`; `content UNCHANGED on every table`. `<F2>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = `<F0>` → **`cobalt_dev: 0013 — F2 = F0`** (10:29:38). Lock (d): `rm …/ops-seam-1002/.env`; `ls …/ops-seam-1002/.env` → `No such file or directory`; `ls -la …/*/.env` → `no matches found`. `.env: removed, proven gone (W, second take)`.
- (e) `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.62s` → `<l>` = 146; the skip `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`; none names `COBALT_LIVE_VAULT_ROOT`.
- The row tests on `<tip>`: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `68 passed, 1 xfailed, 15 warnings in 69.33s (0:01:09)`.

## PRE-STOP SELF-CHECK
(1) "Every added or changed test shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten." Each ported test was red on BASE code at E2 (`49 failed`, first lines quoted), except the negative controls named there. Under the P1 mutation `11 failed`, under P2 `2 failed`, under P3 (A side) `13 failed` and (B side) `1 failed`, under P4 (1) `5 failed` and (2) `1 failed`. The two pins added at the self-check went red under their mutations (`2 failed`). Rewritten: the extra-argument test, which was green on base at first (E2). Three tests are not killed by a mutation of this build: P2's `test_a_bad_name_exits_2_and_touches_nothing`, `test_bad_minutes_exit_2` and `test_release_leaves_the_env_when_no_lock_names_this_worktree`. Each was red on BASE (exit 127, quoted at E2), and each is byte-for-byte B's, checked on B's branch.
(2) "Every entry path of each rule pinned by a test." `install-ops`: no argument (`…links_the_missing_names…`), one extra (`test_one_extra_argument…`), the guard refusing (`test_a_refusing_guard_stops_install_ops…`), an existing plain file (gamma.sh in `…keeps_the_existing_one`), an existing link to elsewhere (`…never_re_pointed`), a second run (`…keeps_all_three`), non-`.sh`/`.py` names and a directory (`…only_regular_sh_and_py…`), a symlink under `ops/desk/` (`test_a_symlink_under_ops_desk_is_not_linked`) and a missing link folder (`test_a_missing_link_folder_is_refused_and_never_made`). The last two were found by this check and pinned in `551f07e0`. The guard and the lock paths are pinned by A's and B's own tests, all run green on `<tip>`. Callers: `desk-launch.sh` is typed by the desk only (`grep -n -F "install-ops" ops/desk/desk-launch.sh` → lines 33, 56, 62, 73, 174, 344, 347, 348, 350, 360, 365, 388); no `src/` reader of any `ops/desk/` file (RESTARTS: `operator script; no Cobalt reader`).
(3) "Every file:line, count and quote re-read at the tip": re-ran at `551f07e0` `grep -n -F "install-ops"` (above), `grep -n -F "desk-context.sh\" --guard"` → `desk-launch.sh:182`, `wait-stop-line.sh:12`, `grep -n -F "lock_dir_free"` → `487`, `596`, `grep -n -F "test/documentation" src/cobalt/jobs/restarts.py` → `242`, the CHECK-HUB / BUILD-HUB counts (E3), the P1 / P2 `git diff --stat` proofs (below), `git show --stat 551f07e0`.

## FOR THE CHECK
- Range `9fa18f14..551f07e0`: `d7cb5f30 wip(ops-seam): PREFLIGHT — cobalt_dev lock held by x5-tap-refresh-1002` · `5165cabd wip(ops-seam): red — the two ported test files and install-ops (P1, P2, P4)` · `dd3dc7ed feat(ops-seam): port desk-size-guard and devdb-lock onto one base; desk-launch install-ops (P1, P2, P3, P4, L3, L42, L72)` · `551f07e0 fix(ops-seam): pin install-ops' two unpinned entry paths — a symlinked source, a missing link folder (P4, K25)`.
- X1 at `<tip>`: `git diff --stat ee667f3c HEAD -- ops/desk/desk-context.sh ops/desk/wait-stop-line.sh tests/ops/test_desk_size_guard.py` → `tests/ops/test_desk_size_guard.py | 4 ++--` only (DECISION 1). `git diff --stat aeefb6df HEAD -- ops/desk/take-devdb-lock.sh ops/desk/release-devdb-lock.sh tests/ops/test_devdb_lock.py BUILD-HUB.md DEPLOY-HUB.md` → `tests/ops/test_devdb_lock.py | 5 ++++-` only (DECISION 2). Every other ported path prints nothing.
- X2: the commands are `git diff ee667f3c HEAD -- ops/desk/desk-launch.sh` (expected: B's hunks + P4's), `git diff aeefb6df HEAD -- ops/desk/desk-launch.sh` (A's + P4's, quoted under E3), `git diff aeefb6df HEAD -- CHECK-HUB.md STANDING-LIST.md` (only main's staging string, the merged LIST line, the §2 title), `git diff 36bed6ed ee667f3c --stat` / `git diff 093028d0 aeefb6df --stat` against `git diff --stat 9fa18f14 HEAD`. Not ported, by the card: `git log --oneline 9fa18f14..HEAD -- src/cobalt/jobs/restarts.py tests/cobalt/test_jobs_restarts.py <the two build reports>` → (nothing).
- X3: CHECK-HUB line 10 holds every string of the base's line, B's two lock strings once each, and `--add-dir /Users/cobalt/.claude/ops` once (greps under E3). Prose: CHECK-HUB `35 allow … the 30 strings of BUILD-HUB.md's line … four --add-dir roots`; STANDING-LIST §1 `30 allow`, §2 `35 allow, 3 deny (+1 staging string …) · … four --add-dir roots`, §2 BUILD LIST `30 strings`, §3 `60 allow … (57 without a migration …)` (B's).
- X4: `install-ops` uses `ln -s` without `-f`/`-h`. Any existing name, a dangling link included (`[ -e ] || [ -L ]`), is KEPT and untouched. Nothing is removed. A missing link folder is refused, never created. Pinned and mutation-proven (E3 P4 mutation 2; the self-check pins).
- Per-row reds, mutations and greens: under `## E2 RED` and `## E3 THE ROWS`. RUN row P3 output under E3. The three suites, `<F0>`/`<F1>`/`<F2>` and the lock times are under W. Lock taken 09:08 (PREFLIGHT probe, released the same minute), 09:43:55 → released after 10:00:34, and 10:12:11 → released after 10:29:38. The RESTARTS table is under `## RESTARTS` (the second run on `551f07e0` printed the same 14 rows and `RESTARTS: none`). The card's records were copied at PREFLIGHT.

## CONTINUE
next: none — built; the desk verifies the artifact and launches `CHECK-HUB.md` on the same card

## DECISIONS
1. **ASK DESK — DECISION P1: `tests/ops/test_desk_size_guard.py` is not byte-equal to `ee667f3c`** [10:05]. A seam the card does not state. A's `World` stages `desk-launch.sh` by replacing the literal lines `REPO=/Users/cobalt/cobalt\n` and `WT=/Users/cobalt/cobalt-wt\n`, and B rewrote those two lines (`REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}`). With both sides ported and the test byte-equal, the replacement matches nothing, the staged copy points at the real repo, and 10 G2 tests fail: `REFUSED: the card must be /Users/cobalt/cobalt/docs/40 - DevDocs/prompts/<date>/<nn>-<job>-card.md` (also `REFUSED: a prompt lives under …` and `REFUSED: a close resume needs its report: …`), with `15 failed, 45 passed` across the two files. SAFE DEFAULT TAKEN, modelled on the card's own rule for the `OPS_TOOLS` literal: the two substitution keys point at B's lines, and no script changes. `git diff ee667f3c HEAD -- tests/ops/test_desk_size_guard.py`:
   ```
   -            "REPO=/Users/cobalt/cobalt\n": f"REPO={self.repo}\n",
   -            "WT=/Users/cobalt/cobalt-wt\n": f"WT={self.wt}\n",
   +            "REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}\n": f"REPO={self.repo}\n",
   +            "WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}\n": f"WT={self.wt}\n",
   ```
   The other choice would be FAILED at E3 for the card to name the seam. The judgment seat keeps the edit or orders that.
2. **ASK DESK — DECISION P2: `tests/ops/test_devdb_lock.py` is not byte-equal to `aeefb6df`** [10:05]. A seam the card does not state. B's launch tests run the real `ops/desk/desk-launch.sh`, which now runs A's guard first. The guard runs the real `/Users/cobalt/.claude/ops/desk-list.sh` (read only), which calls `claude agents --json`, and that reaches B's logging `claude` stub. The stub logs one extra cwd line, so 6 L2 tests fail (`At index 0 diff: '/Users/cobalt/cobalt-wt/ops-seam-1002' != '…/wt/x-job'`; `assert not True` on `claude-calls`). SAFE DEFAULT TAKEN: the stub answers `agents` with `[]` (the shape of A's own `World` stub), and no script changes. The guard then finds no `cto-desk` row and fails open (`WARNING: desk size unread — guard skipped`), so the tests no longer depend on the real desk's size. They do still execute `/Users/cobalt/.claude/ops/desk-list.sh`, which sits outside `tmp_path`, reads only, and goes through the stub. `git diff aeefb6df HEAD -- tests/ops/test_devdb_lock.py`:
   ```
   -    (stub / "claude").write_text(f'#!/bin/sh\nprintf "%s\\n" "$PWD" >> "{calls}"\nexit 0\n')
   +    (stub / "claude").write_text(
   +        '#!/bin/sh\nif [ "$1" = "agents" ]; then echo "[]"; exit 0; fi\n'
   +        f'printf "%s\\n" "$PWD" >> "{calls}"\nexit 0\n'
   +    )
   ```
   As in item 1, keep the edit or order the stop.
3. **DECISION P4 (for the record, not a gap):** the card's predicted red for P4 (`REFUSED: kind 'install-ops' is none of …`) is the red of the one-extra-argument test. With no argument, the base refuses first on its generic usage line (`desk-launch.sh:319` at base). `install-ops` also refuses a missing link folder (`REFUSED: install-ops: no link folder <path>`, exit 1) instead of creating it. The card is silent on that case; L1 says refuse loud, and the test pins it. The kind refusal message and the header's kind list also name `install-ops`.

## RECORDS
- REFUSED, not needed: `grep -n -F "kind=$1" ops/desk/desk-launch.sh` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (a `$` in a double-quoted argument; re-read with the Grep tool instead).
- A `grep -n -o -F "--add-dir …"` call exited 2 (`grep: unrecognized option`, the pattern read as an option); re-run as `grep -n -o -F -e "--add-dir /Users/cobalt/.claude/ops" …` → `10:--add-dir /Users/cobalt/.claude/ops`.
- One extra lock take: W ran twice (on `dd3dc7ed`, then on `551f07e0` after the self-check pins).
- `cobalt_redactions` (system) read 224 rows at PREFLIGHT (09:08), 225 at W (b) (09:43), and 226 during the forward. That is another writer, outside this job. The fingerprint does not see rows; `<F2>` = `<F0>`.
- B's `desk-launch.sh` comment `# COBALT_REPO_ROOT and COBALT_WT_ROOT stand in for these two in tests/ops/test_devdb_lock.py only` is kept byte for byte (fence: no wording of B changed). `tests/ops/test_install_ops.py` also sets `COBALT_REPO_ROOT`, and the `install-ops` header names `$COBALT_OPS_LINK_DIR`.
- The card's `restarts.py:239` is `:242` at base (`rule = "test/documentation; no resident"`).
- The P1 card text "RED on BASE (no such file)": once the test file was written at E2, the red is the base code's (no `--guard`), quoted under `## E2 RED`.
- Cleanup owed (L46): none by this build. No link was made under `/Users/cobalt/.claude/` (the desk runs `install-ops` after the deploy).
- STOPPED at PREFLIGHT 09:07: lock held by `/Users/cobalt/cobalt-wt/x5-tap-refresh-1002/.env` (wip `d7cb5f30`).
- CONTINUED at PREFLIGHT 09:08:04 EDT (desk message from `cto-desk`; fact verified: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`).
- The card's records as re-read at PREFLIGHT: see `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: ops-seam · tip: 551f07e0 | on 9fa18f14 | migration: none | offline 3784/0 | with-DB 4554/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0
