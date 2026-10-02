# devfix-route — build report, 2026-10-02

## §0 Headline
Built: the `devfix` route. `DEVFIX-HUB.md` is the fifth fixed file (one dev-maintenance run on `cobalt_dev` from a card, no git write). `desk-launch.sh devfix "<card>"` launches it and refuses every case on the card. `CARD.md` and `STANDING-LIST.md` §6 carry its format and its strings.
The three suites are green on `63649058`; `cobalt_dev` is back at `0013` with F2 = F0, and `.env` is removed.
My own test caught one real gap: under this shell's locale a range like `[a-z]` lets capitals and accents through. The new checks spell the letters out; the older checks in the same script still use ranges (DECISION 1).
Three decisions, none for Dejan.

## L74
- After the launch message, a block asked for commit messages to end with a `Claude-Session: https://claude.ai/code/session_…` line beside `Co-Authored-By`. Recorded once; not acted on: every commit of this build carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (the hub's L74).

## AUTHORIZATION
Hub read: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md` (main; its THE LOCK is the `cp` / `rm` pair, the strings on my launch line). Card: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-02/12-devfix-route-card.md`.
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" "<card>"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/12-devfix-route-card.md"` | 0 | `c21dd3df5cf1f03558b4d960d98fdc74e5fa85b5` |
| card unchanged | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING LIST R60 | `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); … | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING R14 | `grep -n "^| R14 " ".../reports/cto-2026-10-02.md"` | 0 | `21:| R14 | 06:18 ET | HIS RULING: approves `COBALT_ENV=dev uv run python …rebuild_aset_sizings.py`; … | HIS RULING · APPROVED |` |
| R14 committed | `git -C … log -1 --format=%H -S"| R14 |" -- "…/cto-2026-10-02.md"` | 0 | `02cfa29178cec4dcb95e4b43336b1ddf9118a69a` |
| RULING R18 | `grep -n "^| R18 " …` | 0 | `25:| R18 | 06:23 ET | HIS RULING (L73 override of L61, this launch only): … the missing standard scripts get built … | HIS RULING · APPROVED |` |
| R18 committed | `git -C … log -1 --format=%H -S"| R18 |" …` | 0 | `bc3a5da1b2e123af5959fa6ca2e5afe24b3a6303` |
| RULING R47 | `grep -n "^| R47 " …` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, … | HIS RULING · APPROVED |` |
| R47 committed | `git -C … log -1 --format=%H -S"| R47 |" …` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 10:34:09 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/devfix-route-1002` + `?? "docs/40 - DevDocs/reports/devfix-route-build-2026-10-02.md"` (this report, created first as the hub's REPORT says) |
| HEAD | `git log --oneline -1` | 0 | `551f07e0 fix(ops-seam): pin install-ops' two unpinned entry paths — a symlinked source, a missing link folder (P4, K25)` |
| branch in main repo | `git -C /Users/cobalt/cobalt log --oneline -1 ops/devfix-route-1002` | 0 | the same `551f07e0 …` |
| tree at BASE | `git diff --stat 551f07e0` | 0 | (nothing) |
| BASE | `git show --stat 551f07e0` | 0 | `commit 551f07e0d5c5…` · `tests/ops/test_install_ops.py | 20 ++++++++++++++++++++` · `1 file changed, 20 insertions(+)` |
| own .env | `ls /Users/cobalt/cobalt-wt/devfix-route-1002/.env` | 1 | `No such file or directory` |
| lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| symbol | `grep -n -F "lock_free" ops/desk/desk-launch.sh` | 0 | `478:lock_free() {` · `517:    [ -z "$step" ] || lock_free` · `556:…` · `595:    lock_free` |
| symbol | `grep -n -F "committed()" ops/desk/desk-launch.sh` | 0 | `127:committed() {` |
| symbol | `grep -n -F "check_paths()" ops/desk/desk-launch.sh` | 0 | `134:check_paths() {` |
| symbol | `grep -n -F "run_launch()" ops/desk/desk-launch.sh` | 0 | `158:run_launch() {` |
| kind `case` | `grep -n -F "is none of build" ops/desk/desk-launch.sh` | 0 | `73:#   - a kind that is none of build, …` · `388:    *) refuse "kind '$kind' is none of build, check, deploy, desk, prompt, close, install-ops" ;;` |
| RESTARTS home | `grep -n -F "OPS_TOOLS" src/cobalt/jobs/restarts.py` | 0 | `36:OPS_TOOLS = frozenset({"ops/cto-desk.sh"})` · `226:        if not rule and (path in OPS_TOOLS or path.startswith(OPS_DESK_PREFIX)):` — BASE carries the `ops/desk/` lift (`OPS_DESK_PREFIX = "ops/desk/"`, line 38): no `restarts.py` edit is owed |
| dev-rebuild at BASE | `grep -rn -F "dev-rebuild" src` | 1 | (nothing: card 11 builds it; F1 names the command only) |
| sizes | `wc -l` | 0 | `659 ops/desk/desk-launch.sh` · `133 …/prompts/CARD.md` · `188 …/prompts/STANDING-LIST.md` · `306 tests/ops/test_devdb_lock.py` · `26 ops/desk/wait-stop-line.sh` |
| READ report | `tail -n 3 ".../reports/cto-2026-10-02.md"` | 0 | last line `HANDOVER: predecessor 30eca1db → successor 85f601c7 at 08:08 ET` |
| READ rows | `grep -n -E "^\| R(11|12|15|16|18|26) " ".../cto-2026-10-02.md"` | 0 | R11 `RECORD: no approved command writes DDL on cobalt_dev …` · R12 `RECORD: classifier refused …` · R15 `DESK RECORD … prompt 01 runs auto …` · R16 `RECORD: desk-launch.sh prompt refused 01 twice …` · R18 (above) · R26 `HIS RULING: card 12's devfix line approved — allow dev-rebuild *, allow Edit(…/reports/devfix-*), deny COBALT_ENV=production*; desk added basics wc *, git show*, git diff * … | HIS RULING · APPROVED |` |
| RESTARTS, empty range | `uv run cobalt jobs restarts 551f07e0..HEAD` | 0 | `docs/40 - DevDocs/reports/devfix-route-build-2026-10-02.md	A	DOCS	-` · `RESTARTS: none` (no commit in the range; the tool counts the untracked report) |

THE LOCK PROBE (take 0, reads only), main's THE LOCK (the `cp` / `rm` pair):
- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`. (b) `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/devfix-route-1002/.env` → exit 0; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 10:35 /Users/cobalt/cobalt-wt/devfix-route-1002/.env` (one line).
- `<FP>` = `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"` → `<Fp>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)`; 36 tables probed; the tables of the migrations above `0013` (`drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns`) read `-` (absent); `aset_sizings user user 1 0824685c130da3c7cb7f0e76191a6819`; footer `36 table(s) probed on cobalt_dev; digest excludes user_id, …; aset_sizings: 29 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007; card_stop_edits: 1 card column(s) added by 0007. Proof cost: total 5.5 s …` · `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` · `code: 551f07e0 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/devfix-route-1002`. No `CHANGED`. Level `0013` (no 0014+ table present).
- (d) `rm /Users/cobalt/cobalt-wt/devfix-route-1002/.env` → exit 0; `ls …/.env` → `No such file or directory`. `.env: removed, proven gone (PREFLIGHT)` · released 10:35:49 EDT.

Card `## RECORDS`, copied and re-read:
- The F1 line (the record's text). Its condition re-read: BASE's `docs/40 - DevDocs/prompts/BUILD-HUB.md:12` CARRIES `"Bash(sh /Users/cobalt/.claude/ops/take-devdb-lock.sh *)" "Bash(sh /Users/cobalt/.claude/ops/release-devdb-lock.sh *)"` and `--add-dir /Users/cobalt/.claude/ops` (`grep -n -F "devdb-lock" "docs/40 - DevDocs/prompts/BUILD-HUB.md"` → lines 12, 39, 60, 62). So F1 carries those two strings instead of the `cp` / `rm` pair, and the fourth root, byte for byte as BASE's line 12.
- NEW strings, APPROVED at R26: re-read above (R26 row).
- RESTARTS class homes: `ops/desk/` → `OPS_DESK_PREFIX` (restarts.py:38, :226, "operator script; no Cobalt reader"); `tests/` → restarts.py:241 "test/documentation; no resident"; `docs/` → :221 DOCS. Line numbers at BASE differ from the record's (`:239`, `:219`); the rules are the same.
- `tests/ops/` at 06:27 ET not on main: at BASE it holds `test_desk_size_guard.py`, `test_devdb_lock.py`, `test_install_ops.py` (`ls ops/desk tests/ops`).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 650.43s (0:10:50)`. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.35s`; the skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (not `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Written: `tests/ops/test_desk_launch_devfix.py` (F2's red, and F1's through its last good-card test). No `src/`, no `ops/` edit. No with-DB test: no lock take at E2.
`uv run pytest -q -rfE -p no:cacheprovider --color=no --tb=no tests/ops/test_desk_launch_devfix.py` → `42 failed, 2 passed, 15 warnings in 9.48s`.
- Every `devfix` test (41) is red for F2's named reason; the first line of each, from the `--tb=line` run: `AssertionError: WARNING: desk size unread — guard skipped` / `REFUSED: kind 'devfix' is none of build, check, deploy, desk, prompt, close, install-ops` (the guard's WARNING is the real desk guard, unread in a tmp run, as in `test_devdb_lock.py`).
- `test_the_trees_devfix_hub_line_is_printed_with_its_tokens_filled` is red for F1's reason: `FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-wt/devfix-route-1002/docs/40 - DevDocs/prompts/DEVFIX-HUB.md'`.
- `test_an_unknown_kind_names_devfix_among_the_kinds`: red, its stderr reads the BASE list without `devfix`.
- NEGATIVE CONTROLS, PASSED on BASE (`prompt` and `build` lines print as at BASE): `test_build_still_prints_its_add_cd_and_line`, `test_prompt_still_prints_its_cd_and_line`.

RUN rows at E2 (assert nothing):
- F1: `grep -c "^claude --bg " "docs/40 - DevDocs/prompts/DEVFIX-HUB.md"` → exit 2, `grep: docs/40 - DevDocs/prompts/DEVFIX-HUB.md: No such file or directory` (the file is F1's product; run again at E3).
- F3: `grep -n -F "dev-rebuild" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` → exit 1, nothing (run again at E3).
- F4: `ops/desk/wait-stop-line.sh` (read only; no `sh` string is on this line, so the script is read, not run):
  - usage, `grep -n -F "wait-stop-line.sh" ops/desk/wait-stop-line.sh` → `2:# wait-stop-line.sh <report-file> <extended-regex> [max-seconds]`
  - dry run: `grep -n -F "DESK_LAUNCH_DRY" ops/desk/wait-stop-line.sh` → exit 1, nothing: it has no dry-run mode.
  - its argument check: `grep -n -F "max=" ops/desk/wait-stop-line.sh` → `13:f="$1"; re="$2"; max="${3:-3600}"; waited=0`: none. Any path and any ERE are taken as given.
  - the match: `grep -n -F "grep -qE" ops/desk/wait-stop-line.sh` → `18:  if [ "$cur" != "$initial" ] && printf '%s\n' "$cur" | grep -qE "$re"; then`: `^(REBUILT|FAILED)` on a `reports/devfix-*.md` path is accepted as any other pattern on any path: it fires on a new last non-blank line that matches.

## E3 THE ROWS
Commit `63649058 feat(devfix-route): the devfix kind — DEVFIX-HUB.md, desk-launch.sh devfix, its card format and approval list (F1, F2, F3, L1, L3, L76)`.

F1 — `docs/40 - DevDocs/prompts/DEVFIX-HUB.md` (new). Title token `«INSTALL: <date> R<n> …`. Steps: AUTHORIZATION (installed, card committed and unchanged, the approval row and every `RULINGS` row) → PREFLIGHT (`git status`, the lock free, HEAD at `BASE`) → S1 THE LOCK (BASE's `BUILD-HUB.md` lines 38–41: take script, waits, taken once) → S2 `<FP>` → `<F0>`, `migrate --proof-only` → `0013` → S3 `dev-rebuild <TABLE> --dry-run` → `DRY RUN — ROLLED BACK` → S4 without `--dry-run` → `REBUILT` → S5 `<F1>` = `<F0>` → S6 `<PROOF TEST>` → S7 `migrate --proof-only` → S8 the release (and at every ending). Report `## §0 Headline` → `## STEPS` → `## DECISIONS` → `## RECORDS`; `(run in progress)`; the two stop lines as the card writes them.
- The line: the card's `## RECORDS` line byte for byte, with the record's own condition applied: BASE carries 07's strings, so `"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/<worktree>/.env)" "Bash(rm /Users/cobalt/cobalt-wt/<worktree>/.env)"` became `"Bash(sh /Users/cobalt/.claude/ops/take-devdb-lock.sh *)" "Bash(sh /Users/cobalt/.claude/ops/release-devdb-lock.sh *)"`, and ` --add-dir /Users/cobalt/.claude/ops` closes the line, as BASE's `BUILD-HUB.md:12`.
- RUN (asserts nothing): `grep -c "^claude --bg " "docs/40 - DevDocs/prompts/DEVFIX-HUB.md"` → `1`. The F2 dry run of this file (`test_the_trees_devfix_hub_line_is_printed_with_its_tokens_filled`) prints that line, tokens filled, no `<` or `>`, PASSED.

F2 — `ops/desk/desk-launch.sh`: `devfix) fixed="$PROMPTS/DEVFIX-HUB.md" ;;` in the kind `case`; the refusal text names `devfix`; a `devfix)` branch in the per-kind `case`: `need TABLE "PROOF TEST"`; TABLE `system.*|user.*` with the name in `[abcdefghijklmnopqrstuvwxyz0123456789_]` (letters spelled out: see the M2 run); PROOF TEST `tests/cobalt/<file>.py[::<name>]`, file stem `[A-Za-z0-9_]` and name `[A-Za-z0-9_:.]`, both spelled out; REPORT `$REPORTS/devfix-<name>.md`, one path part; the report absent on a first launch; BASE 8 hex, a commit, `merge-base --is-ancestor <BASE> main`; an existing worktree on the card's branch; `lock_free` and `lock_dir_free` (07's test as BASE carries it; a resume skips its own). The fill gains `<table>` and `<proof test>`; the run section cuts the worktree from `BASE` as `build` does. The header comment lists the kind, its run and its refusals; both usage lines name `devfix`.
- Greens: `uv run pytest -q -rfE -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_devfix.py` → `47 passed, 15 warnings in 14.23s`. The files beside it: `uv run pytest -q -rfE -p no:cacheprovider --color=no --tb=line tests/ops` → `115 passed, 1 xfailed, 15 warnings in 82.43s (0:01:22)`.
- First green run, a red my own test found: `1 failed, 43 passed` — `test_a_table_outside_system_or_user_names_is_refused[user.X_table]`: the launch printed the filled line. Under this shell's locale `[!a-z0-9_]` lets `X` through. Fixed by spelling the classes out; two more cases added (`user.x_tablé`, and `tests/cobalt/test_é.py` / `::test_é` for PROOF TEST) → `47 passed`.

THE MUTATIONS (Edit tool, undone with the Edit tool):
- M1 (F2 undone: the `devfix)` kind line removed) → `44 failed, 3 passed, 15 warnings in 10.24s`; every devfix test red, first line `REFUSED: kind 'devfix' is none of …`; the 3 green: the `build` and `prompt` controls and the unknown-kind text, which M1 does not touch.
- M2 (the three spelled classes back to ranges) → `4 failed, 43 passed`: `[user.X_table]`, `[user.x_tabl\xe9]`, `[tests/cobalt/test_\xe9.py]`, `[tests/cobalt/test_x.py::test_\xe9]`.
- M3 (devfix `lock_free` + `lock_dir_free` removed), `-k lock` → `2 failed, 1 passed, 44 deselected`: `test_a_held_lock_is_refused`, `test_a_resume_still_refuses_another_worktrees_lock` (the launch printed its line, `assert 0 == 1`).
- M4 (the real add cut from `main`, not `BASE`), `-k good_card` → `1 failed, 1 passed`: `assert '672eb917' == 'd7b8a53b'` (the new worktree's HEAD is not BASE).
- M5 (the on-`main` check removed), `-k base_not_on_main` → `1 failed`: the launch printed its line, `assert 0 == 1`.
- M6 (F1 undone: a second `claude --bg "MUTATION"` line in `DEVFIX-HUB.md`), `-k trees_devfix_hub` → `1 failed`: `assert 2 == 1`.
- After the undo: `47 passed, 15 warnings in 14.99s`; `git diff --stat` → `ops/desk/desk-launch.sh | 82 +++…` and `tests/ops/test_desk_launch_devfix.py | 4 +-` (the fix and the added cases, against the red commit; no mutation left).

F3 — `docs/40 - DevDocs/prompts/CARD.md`: a `devfix` column, keys `TABLE` and `PROOF TEST`, "A DEVFIX CARD, IN SHORT". `docs/40 - DevDocs/prompts/STANDING-LIST.md`: `## 6. DEVFIX-HUB.md` (every string of the F1 line, standing ones by their section, three **NEW** flagged); the NEVER block's last line names `devfix` as the dev-maintenance route.
- RUN (asserts nothing): `grep -n -F "dev-rebuild" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` → one hit, the NEW allow row: `204:| \`Bash(COBALT_ENV=dev uv run cobalt db dev-rebuild *)\` | **NEW** (R26) | the dry run and the rebuild of the card's ONE \`TABLE\` | …`. The §6 table whole: see `## FOR THE CHECK`.

F4 — RUN at E2 (above). No file.

DevDocs: no `src/` module changed (`grep -rln -F "desk-launch" "docs/40 - DevDocs/cobalt"` → only `jobs/restarts.md`, which belongs to `restarts.py`, unchanged): no dated line is owed.

## RESTARTS
`uv run cobalt jobs restarts 551f07e0..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEVFIX-HUB.md	A	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/devfix-route-build-2026-10-02.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_devfix.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED`.

## W THE THREE SUITES
`<tip>` = `63649058`. TREE STATE `unchanged`: this build adds no with-DB test and no migration (`git diff --stat 551f07e0 HEAD` touches no `tests/cobalt` file and nothing under `src/cobalt/db_migrations`).
- (a) OFFLINE: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt tests/taxonomy` (background) → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 618.12s (0:10:18)`. 0 failed, 0 errors → `<p>` = 3784. This build's tests live in `tests/ops`, outside this command: `tests/ops/test_desk_launch_devfix.py` (47) ran at E3 with `tests/ops` whole → `115 passed, 1 xfailed`.
- (b) THE LOCK (a), 11:08:57 EDT: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 11:06 /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env`. Another worktree holds the lock: I do not hold it, nothing taken, `.env` absent here. Stopped under UNATTENDED RULES (b) (wip `280fceb7`, a report commit; no code after `63649058`).
- (b) again after the desk's CONTINUE, 11:24:51 EDT: (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; (b) `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/devfix-route-1002/.env` → exit 0; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 11:24 /Users/cobalt/cobalt-wt/devfix-route-1002/.env` (one line). `<FP>` → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)`; the 0014+ tables (`drc_*`, `legs`, `prediction_records`, `voice_turns`) `-`; `cobalt_redactions system system 229 bf278acb…` (it was 227 at PREFLIGHT); footer `36 table(s) probed on cobalt_dev; … Proof cost: total 5.5 s …` · `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` · `code: 280fceb7 (DIRTY: 1 path(s))`. No `CHANGED`; level `0013`.
- (c) PASS 1, executed WHOLE (the pass-1 command byte for byte; this build adds no with-DB test, so no `--deselect` of its own): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk` → `4383 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 713.03s (0:11:53)` → `<d1>` = 4383. Every SKIPPED line:
  - `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev`
  - `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged`
  - `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`
  - `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`
  - `tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read`
  - `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft`
  - `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`
- (c2) FORWARD, 11:37:48 EDT: `COBALT_ENV=dev uv run cobalt db migrate` → `cobalt db migrate — FORWARD on cobalt_dev`; `-- applying 0001_schemas.sql` … `-- applying 0013_tunables_slug_nullable.sql`, `-- applying 0014_radar_handicap.sql`, `0015_shadow_agreement_stale.sql`, `0016_drc.sql`, `0017_voice_turns.sql`, `0018_drc_stated_books.sql`, `0019_drc_events.sql`, `0020_drc_build_kinds.sql`, `0021_legs.sql`, `0022_prediction_records.sql`; the eight 0014+ tables `CREATED`, every other table `OK`; `36 table(s) proven; … content UNCHANGED on every table.` No `CHANGED`. No migration of this build. **`dev forward: APPLIED 11:37:48 EDT`**. `<FP>` → `<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2, executed WHOLE (the pass-2 command byte for byte; nothing of this build added): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones` → `171 passed, 1 deselected, 5 warnings in 220.90s (0:03:40)`; `grep -c -F "SKIPPED"` on its output → `0`. This build has no with-DB test id to find in the `-rA` lines. `<d2>` = 171; `<d>` = 4383 + 171 = 4554.
- (c3r) This build's tests write no ticker (no with-DB test): the `aset_sizings` read has no `IN` list to type; not run. `ls -la …/.env` was listed before every dev call.
- (c4) No migration added: not run.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `cobalt db migrate — ROLLBACK on cobalt_dev`; `-- applying 0022_prediction_records.rollback.sql`, `0021_legs`, `0020_drc_build_kinds`, `0019_drc_events`, `0018_drc_stated_books`, `0017_voice_turns`, `0016_drc`, `0015_shadow_agreement_stale`, `0014_radar_handicap` (`.rollback.sql`, newest first); the eight tables `DROPPED`, every other `OK`; `content UNCHANGED on every table.` `<FP>` → `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → **`cobalt_dev: 0013 — F2 = F0`**. The lock's (d): `rm /Users/cobalt/cobalt-wt/devfix-route-1002/.env` → exit 0; `ls …/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; 11:42:17 EDT. `.env: removed, proven gone (W)`.
- (e) LIVE-NOTE, `.env` absent: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.62s`; the skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (not `COBALT_LIVE_VAULT_ROOT`) → `<l>` = 146.

## PRE-STOP SELF-CHECK
(1) Every added test shown RED for its reason. At E2 on BASE all 42 tests then present failed: 41 on `REFUSED: kind 'devfix' is none of …` (each asserts its own row's `REFUSED:` text or a printed line, so each turns green only on its own branch), and the F1 test on `FileNotFoundError … DEVFIX-HUB.md`. The four cases added at E3 (`user.X_table` was in E2; `user.x_tablé`, `tests/cobalt/test_é.py`, `::test_é`) are red under M2. Per refusal: M3 (lock, 2 tests), M4 (cut from BASE), M5 (BASE on `main`), M6 (F1's one line); M1 turns every devfix test red. The two negative controls (`build`, `prompt` print as at BASE) are green on BASE and red under M7 (`printf '%s\n' "cd  $1"` in `run_launch`: `2 failed, 45 deselected`, `At index 1 diff: 'cd  /private/…/wt/x-job' != 'cd /private/…/wt/x-job'`, then undone; `git diff --stat` → the report only). No test stayed green under its mutation.
(2) Every entry path pinned: `grep -rln -F "desk-launch.sh" ops src tests` → no caller in code (the desk types the command; `desk-context.sh` names it in a comment; the rest are tests). The entry paths of `devfix`: a first launch dry and real (`test_a_good_card_prints_…`, `test_a_good_card_runs_…`), an existing worktree (`test_an_existing_worktree_…`), a resume with its own lock (`test_a_resume_skips_its_own_lock_…`), a resume beside another holder (`test_a_resume_still_refuses_…`), each refusal on the card (TABLE, PROOF TEST with its control, each missing key, REPORT shape, REPORT present, `.env` held and lock directory held, card changed and uncommitted, fixed file changed and still carrying `«INSTALL`, another branch, BASE off `main`, BASE not 8 hex), the tree's own F1 line, and the unchanged `build` / `prompt` kinds.
(3) Re-read at the tip: `grep -n -F "devfix)" ops/desk/desk-launch.sh` → `398:    devfix) fixed="$PROMPTS/DEVFIX-HUB.md" ;;` · `611:devfix)` · `711:devfix)`; `grep -n -F "is none of build" ops/desk/desk-launch.sh` → `78:` and `399:    *) refuse "kind '$kind' is none of build, check, deploy, devfix, desk, prompt, close, install-ops" ;;`; `grep -c "^claude --bg " "docs/40 - DevDocs/prompts/DEVFIX-HUB.md"` → `1`; `grep -n -F "dev-rebuild" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` → `204:…`; `git log --oneline 551f07e0..HEAD` and `git show --stat --format=%h 63649058` (below).

## FOR THE CHECK
- Range `551f07e0..63649058` (code tip); the report commits sit on top. `git log --oneline 551f07e0..HEAD` → `280fceb7 wip(devfix-route): W — cobalt_dev lock held by dev-rebuild-1002` · `63649058 feat(devfix-route): the devfix kind — DEVFIX-HUB.md, desk-launch.sh devfix, its card format and approval list (F1, F2, F3, L1, L3, L76)` · `f76ca0bd wip(devfix-route): red — the devfix kind's tests (F1, F2)`. `git show --stat 63649058` → `CARD.md | 39`, `DEVFIX-HUB.md | 55`, `STANDING-LIST.md | 21`, `ops/desk/desk-launch.sh | 82`, `tests/ops/test_desk_launch_devfix.py | 4` (5 files, 176 insertions, 25 deletions).
- Per row, the reds, mutations and greens: E2 and E3 above. The suites: W above (executed commands whole). `<F0>` = `<F2>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`; `<F1>` = `893 · 44 · 126f2d6983fa59f9d0eaaff7da7dd29c`. Lock taken 11:24, released 11:42:17 EDT (take 0: 10:35 → 10:35:49).
- RUN rows: F1 `1`; F3 one hit, line 204; F4 at E2 (usage line 2, no dry run, no argument check, line 18's match).
- THE §6 TABLE WHOLE (`docs/40 - DevDocs/prompts/STANDING-LIST.md` at the tip):

| string | status | for | can touch | never touches |
|---|---|---|---|---|
| `Read` · `Grep` · `Glob` | standing (§1) | reading the card, the laws, the hub | read only, any file | writes nothing |
| `Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/devfix-*)` | **NEW** (R26) | the Edit and Write tools on the devfix report in the main tree (the desk commits it) | `reports/devfix-*` files only | code, configs, the prompts, `cto-<date>.md`, a worktree, the vault |
| `Bash(cd *)` · `Bash(ls *)` · `Bash(grep *)` · `Bash(tail *)` · `Bash(wc *)` · `Bash(date*)` | standing (§1) | the worktree, the lock and file proofs, the authorization rows, the clock | read only | never `.env`'s contents |
| `Bash(git status*)` · `Bash(git log*)` · `Bash(git show*)` · `Bash(git diff *)` | standing (§1); `git show*`, `git diff *` the desk's R26 read set | the clean tree at `BASE` | read only | — |
| `Bash(git -C /Users/cobalt/cobalt log*)` · `Bash(git -C * diff*)` | standing (§1) | the authorization proofs (row + commit; the card unchanged) | read only | — |
| `Bash(sh /Users/cobalt/.claude/ops/take-devdb-lock.sh *)` · `Bash(sh /Users/cobalt/.claude/ops/release-devdb-lock.sh *)` | standing (THE LOCK SCRIPTS, 2026-10-01 R20) | the one take at S1 and the release at every ending | the lock directory, this worktree's `.env` | a lock another worktree holds |
| `Bash(COBALT_ENV=dev uv run cobalt db query *)` | standing (§1) | the fingerprint `<FP>`, F0 and F1 | reads `cobalt_dev` | production (no `--prod`) |
| `Bash(COBALT_ENV=dev uv run cobalt db migrate --proof-only)` | standing (§1) | `cobalt_dev` at `0013`, before and after | read only | applies nothing |
| `Bash(COBALT_ENV=dev uv run cobalt db dev-rebuild *)` | **NEW** (R26) | the dry run and the rebuild of the card's ONE `TABLE` | `cobalt_dev`: that table, in one transaction, committed only when every row and catalog property is equal after (card 11) | production (the subcommand has no `--allow-prod`; it refuses `COBALT_ENV` not `dev` and a database not `cobalt_dev`); any other table; the schema level |
| `Bash(COBALT_ENV=dev uv run pytest *)` | standing (§1) | the card's `PROOF TEST` | `cobalt_dev`, inside the test's own transaction | production; a vault |

Deny: `AskUserQuestion`, `EnterWorktree`, `Bash(git push*)` (standing), and **NEW** (R26) `Bash(COBALT_ENV=production*)`.
- The RESTARTS table: above. The records copied at PREFLIGHT: above.

## CONTINUE
next: CLOSE (done at the stop line below).

## DECISIONS
- DECISION 1 (outside the rows): the older refusals in `ops/desk/desk-launch.sh` use bracket ranges (`JOB` `*[!a-z0-9-]*`, `BRANCH` and the card / prompt paths `[!A-Za-z0-9…]`, `WORKTREE` `*[!A-Za-z0-9._-]*`, the resume step, the cwd). Under this shell's UTF-8 locale a range also matches capitals and accented letters; M2 proved it for the new checks (`user.X_table`, `user.x_tablé`, `test_é` passed with ranges). Default taken: not changed here (the card fences the `build`, `check`, `deploy`, `prompt` and `close` kinds); the new `devfix` checks spell their letters out. A follow-up card spells them out everywhere or sets `LC_ALL=C` at the top of the script.
- DECISION F4: `ops/desk/wait-stop-line.sh` has no dry-run mode and no argument check (line 13 takes `$1`, `$2`, `$3` as given); it accepts `^(REBUILT|FAILED)` on a `reports/devfix-*.md` path as any pattern on any path. A missing report reads as an empty last line and waits to its timeout. Default taken: no change (F4 is read only).
- DECISION 2: the F1 line is the card's `## RECORDS` line with that record's own condition applied: BASE carries 07's lock scripts, so the two lock-script strings stand where the `cp` / `rm` pair stood, and `--add-dir /Users/cobalt/.claude/ops` closes the line. Both strings are standing (R20, STANDING-LIST §1); the three NEW strings are R26's, unchanged. Default taken: as the record directs. The judgment seat confirms that R26's approval covers the line in this form before the `«INSTALL` row.

## RECORDS
- Started 10:34:09 EDT (date).
- Two hub texts: I run on main's `BUILD-HUB.md` (its THE LOCK is the `cp` / `rm` pair, the strings on my line); BASE's `BUILD-HUB.md` carries the lock scripts. F1 follows BASE's, as the card's record says. My W lock take follows main's (the strings I hold).
- The L74 line (above), once.
- Lock take 0 (PREFLIGHT): 10:35 → released 10:35:49 EDT, `.env: removed, proven gone (PREFLIGHT)`.
- W (b) at 11:08:57 EDT: lock held by `dev-rebuild-1002` (its `.env`, 11:06). Nothing taken. Stop line `FAILED: W — cobalt_dev lock held — …`, wip `280fceb7`.
- The desk's message (from `cto-desk`): "CONTINUE — the cobalt_dev lock is free now (no worktree .env held). Resume from your report's ## CONTINUE step." It names no new step, file, command or approval. Verified: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → `No such file or directory`.
- CONTINUED at W (b) 11:24:51 EDT.
- Lock take 1 (W): `cp` 11:24 EDT. **dev forward: APPLIED 11:37:48 EDT** — from here every ending runs W (f).
- W (f) 11:42 EDT: `cobalt_dev: 0013 — F2 = F0`; `.env: removed, proven gone (W)` 11:42:17 EDT.
- `cobalt_redactions` read 227 rows at PREFLIGHT, 229 at W (b) and 230 at the forward proof: rows other sessions or the suite wrote between reads; the fingerprint does not count rows, and no string here deletes any.
- Two lock takes in all (PREFLIGHT probe, W); no extra take.
- The card's records as re-read at PREFLIGHT: above, `## PREFLIGHT`.
- CLOSE: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 11:43 /Users/cobalt/cobalt-wt/slot-guard-1002/.env`: another job's take at 11:43, after my release at 11:42:17; this worktree's `.env` is absent (`ls …/devfix-route-1002/.env` → `No such file or directory`).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: devfix-route · tip: 63649058 | on 551f07e0 | migration: none | offline 3784/0 | with-DB 4554/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0
