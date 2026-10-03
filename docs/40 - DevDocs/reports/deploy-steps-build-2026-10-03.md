# deploy-steps — build report 2026-10-03

## §0 Headline
- Built D1–D4: `ops/desk/deploy-step0.sh`, `deploy-outage.sh`, `deploy-smoke.sh`, each with `--dry-run`, tested by stubs in `tests/ops/` (62 tests, red first, one mutation per row).
- Tip `775aedfd`: offline 3737/0, `tests/ops` 534/0, live-note 146/0; DB: none; `RESTARTS: none`.
- A test once fell through to the real `/bin/launchctl` (print and a failed tmp-plist bootstrap); fixed; the desk confirms aset (`## DECISIONS` 1, FOR DEJAN).
- As built, the outage script does bootout and bootstrap with nothing between them: the hub's merge and migration cannot sit inside it (`## DECISIONS` 4).

## L74
- The session's attribution reminder asked for a `Claude-Session:` line on commits. Recorded once as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 11:30:18 EDT 2026` |
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../prompts/2026-10-03/20-deploy-steps-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/20-deploy-steps-card.md"` | 0 | `942180bed20f9a19cc5cf34fc10947ac02a704b6` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING LIST R60 (09-30) | `grep -n "^\| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** (...): APPROVES STANDING-LIST.md once (4be06af0) ... \| APPROVED \|` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R60 \|" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULINGS 2026-10-02 R47 | `grep -n "^\| R47 " ".../reports/cto-2026-10-02.md"` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, ... card 20 (deploy-outage.sh) keeps a Grok check (...). \| HIS RULING · APPROVED \|` |
| R47 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R47 \|" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| RULINGS 2026-10-02 R157 | `grep -n "^\| R157 " ".../reports/cto-2026-10-02.md"` | 0 | `164:\| R157 \| 17:40 ET \| HIS RULING (B): the brain's full process list for 10-03 runs this week, adoption card included; ... \| HIS RULING · APPROVED \|` |
| R157 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R157 \|" -- ".../cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |

AUTHORIZATION: PASS.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## ops/deploy-steps-1003` + `?? "docs/40 - DevDocs/reports/deploy-steps-build-2026-10-03.md"` (this report, written at AUTHORIZATION) |
| base | `git log --oneline -1` | 0 | `a09f0862 docs(desk): 10-03 R30-R34 set 1 deployed; refusals list; his rulings` |
| branch in repo | `git -C /Users/cobalt/cobalt log --oneline -1 ops/deploy-steps-1003` | 0 | `a09f0862 docs(desk): 10-03 R30-R34 set 1 deployed; refusals list; his rulings` |
| no diff | `git diff --stat a09f0862` | 0 | (nothing) |
| base stat | `git show --stat a09f0862` | 0 | `docs/40 - DevDocs/reports/cto-2026-10-03-words.md \| 6 ++++++` · `docs/40 - DevDocs/reports/cto-2026-10-03.md \| 19 +++++++++++++++++--` · `2 files changed, 23 insertions(+), 2 deletions(-)` |
| no .env here | `ls /Users/cobalt/cobalt-wt/deploy-steps-1003/.env` | 1 | `ls: …/deploy-steps-1003/.env: No such file or directory` |
| .env census | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| RESTARTS empty | `uv run cobalt jobs restarts a09f0862..HEAD` | 0 | (venv created) `docs/40 - DevDocs/reports/deploy-steps-build-2026-10-03.md	A	DOCS	-` · `RESTARTS: none` (the untracked report only) |
| symbol P1 | `grep -n -F "**P1 DATE AND WINDOW**" ".../prompts/DEPLOY-HUB.md"` | 0 | `59:- **P1 DATE AND WINDOW**: \`date\`. Lawful when ONE of these holds; …` |
| symbol STEP-4 | `grep -n -F "## STEP-4 — THE OUTAGE" ".../DEPLOY-HUB.md"` | 0 | `141:## STEP-4 — THE OUTAGE, on the labels of \`<restart set>\` only: …` |
| symbol STEP-5 | `grep -n -F "## STEP-5 — ROLLBACK" ".../DEPLOY-HUB.md"` | 0 | `163:## STEP-5 — ROLLBACK, ONE PATH (L54, L68): …` |
| cobalt.sh status | `grep -n -F "status)" /Users/cobalt/cobalt-wt/deploy-steps-1003/cobalt.sh` | 0 | `79:    status)` |
| the three new files | `ls …/ops/desk/deploy-step0.sh …/deploy-outage.sh …/deploy-smoke.sh` | 1 | `No such file or directory` × 3 (the rows' RED on BASE) |
| wc -l | (no row edits an existing file: the six files are new) | — | — |
| READ tail attempt1 | `tail -n 3 ".../reports/deploy-2026-09-30-1-attempt1.md"` | 0 | `FAILED: T — merges — \`--merges 8635cde1..deploy/drc-0930\` prints two lines (\`94067d63\`, \`5bb1f4b5\`), exactly one required — nothing touched · rollback: not used` |
| READ tail attempt2 | `tail -n 3 ".../deploy-2026-09-30-1-attempt2.md"` | 0 | `FAILED: gate — G (a) — \`tests/cobalt/test_drc_build.py::test_the_retired_files_are_gone\` (…) · rollback: not used` |
| READ tail attempt3 | `tail -n 3 ".../deploy-2026-09-30-1-attempt3.md"` | 0 | `FAILED: RESTARTS — \`configs/cobalt/templates/daily.md.j2	M	UNCLASSIFIED CONFIG\` (exit 1, …; set widened to six residents) · rollback: not used` |
| READ tail 10-01 | `tail -n 3 ".../deploy-2026-10-01-1.md"` | 0 | `FAILED: gate — G (c) — tests/cobalt/test_radar_score_migration.py::test_card_checks_index_and_receipt_immutability_on_cobalt_dev (TooManyColumns: …) · rollback: not used · decisions: 2 · for Dejan: 0` |
| READ tail brain | `tail -n 3 ".../brain-unattended-2026-10-02.md"` | 0 | `BRAIN DONE — report /Users/cobalt/cobalt/docs/40 - DevDocs/reports/brain-unattended-2026-10-02.md` |
| DevDocs pages | `grep -rln -F "deploy-card.sh" ".../docs/40 - DevDocs/cobalt"` | 1 | (nothing): no DevDocs module page exists for `ops/desk/` scripts; no `src/` module changes, so E3's dated line has no page to land on |

DB: none — no lock probe, no with-DB string used by this build.

Card `## RECORDS`, copied: (1) `DB: none`: every file is under `ops/` or `tests/ops/`. (2) House A = Grok by his word; one Grok hub at a time (L15). (3) The dry run before first use is the desk's step after DEPLOYED; the adoption of the three scripts into `DEPLOY-HUB.md` is a later card. Re-read: (1) is re-read at W (a0); (2), (3) are the desk's and not re-readable by this list.

## E0 BASELINE
- Offline on `a09f0862`: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → exit 0, `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 655.08s (0:10:55)`. 0 failed, 0 errors.
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.86s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — no skip names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
- Written: `tests/ops/test_deploy_step0.py` (D1, D4), `tests/ops/test_deploy_outage.py` (D2, D4), `tests/ops/test_deploy_smoke.py` (D3, D4). No `src/` or `ops/` edit.
- First run: every stub's recorder was built with `str.format` over a JSON literal → `KeyError: '"name"'` at setup (outage, smoke). Not the rows' reason: the recorder was rewritten with a plain placeholder, and the run repeated.
- `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_step0.py tests/ops/test_deploy_outage.py tests/ops/test_deploy_smoke.py` → exit 1, progress line `FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF [100%]` (62 F). Each red's first line is the row's named reason, RED on BASE: no such file, e.g. `AssertionError: sh: /Users/cobalt/cobalt-wt/deploy-steps-1003/ops/desk/deploy-step0.sh: No such file or directory` (`assert 127 == 0`), the same for `deploy-outage.sh` and `deploy-smoke.sh`; the row-lookup tests fail one step later on the empty stdout (`AssertionError: ('needle exact', '')`), same cause.
- No with-DB red (DB: none). Commit `7a9db92b` `wip(deploy-steps): red — D1-D4 tests before the scripts`.

## E3 THE ROWS
Files: `ops/desk/deploy-step0.sh`, `ops/desk/deploy-outage.sh`, `ops/desk/deploy-smoke.sh` (new, POSIX `sh`, `export LC_ALL=C` before `set -u`, header = usage and the desk's dry-run line), their three tests. No DevDocs module page exists for `ops/desk/` (PREFLIGHT); none written.

| row | built | greens | mutation (Edit, run, undone) |
|---|---|---|---|
| D1 | `deploy-step0.sh "<card>"`: KEYS, SHIPS, P0 (`authorize.sh deploy`, its rows prefixed `P0 `), P1 window, P2 check / committed per ship, P3 tip per ship, P7 listing per head and P7 migrations, P8 census ×3, disk, main status; last line `STEP-0 OK — window: <rule>` / `FAILED STEP-0: <rule> — <detail>`. `--window` (the P1 row alone, read by D2) | `tests/ops/test_deploy_step0.py` → `28 passed` | P2 literal check made a no-op (`*) ;;`) → `1 failed, 27 passed`: `test_deploy_step0.py:242: AssertionError: assert 0 == 1` (`test_a_ready_no_check_report_fails_naming_the_rule`, `STEP-0 OK — window: (iii)` printed). Undone |
| D2 | `deploy-outage.sh "<card>" <set> <MERGED\|NOT MERGED>`: arguments, NOT MERGED, window (`deploy-step0.sh --window`) and every label's `print` state/path checked before the first bootout; bootout all, bootstrap all (one retry on `Bootstrap failed: 5`, one `kickstart -k`), agent by `cobalt.sh stop` / `launchctl kickstart`; `cobalt.sh status`; trap on EXIT INT TERM HUP restores every label down | `tests/ops/test_deploy_outage.py` → `19 passed` | `trap on_exit EXIT` removed → `6 failed, 13 passed`: first lines `test_deploy_outage.py:187: IndexError: list index out of range` (no output at all) and `test_deploy_outage.py:248: AssertionError: assert 'RESIDENTS UP (trap)' in ''` (×3 signals). Undone |
| D3 | `deploy-smoke.sh "<card>"`: MARKERS then SMOKE READS, four mapped shapes (`ls`, `grep -c -F`, `curl` ×3 tries, `db query`), no shell eval; db rows SKIPPED on `MIGRATIONS: none` or a `%`; census recorded | `tests/ops/test_deploy_smoke.py` → `15 passed` | marker verdict forced green (`vr=0`) → `1 failed, 14 passed`: `test_deploy_smoke.py:141: AssertionError: assert 0 == 1` (`SMOKE GREEN` printed). Undone |
| D4 | `--dry-run` in each script: `WOULD RUN:` lines in order, nothing run, no log | the three `test_dry_run_*` and `test_d4_*` tests green | outage `--dry-run` made to run for real (`dry=""`) → `2 failed, 1 passed, 16 deselected`: `test_deploy_outage.py:332: … Left contains 15 more items, first extra item: {'argv': ['+%Y%m%d-%H%M%S'], 'name': 'date'}`. Undone |

- Tests changed during E3, each said: (a) `test_a_marker_whose_after_differs_is_smoke_red` expected ` · 0 · RED`; the script prints ` · 0 (still the before value) · RED` — the expectation was widened to that text. (b) `test_launchctl_gone_after_the_first_bootout_…`: the stub deleted itself, so the script fell through to the real `/bin/launchctl` (see `## DECISIONS` 1); the stub now turns into a `exit 127` stand-in and the test asserts `command not found` reached the log. (c) step0's `test_d4_…` dropped `COBALT_REPO_ROOT` so its dry run prints the real `/Users/cobalt/cobalt` paths.
- First D1 run: `10 failed, 18 passed` — `P0 FAILED: authorization mismatch — STANDING LIST`: `authorize.sh` inherited `LC_ALL=C` and its `[^«]*` title pattern no longer matched. Fixed in the script: `authorize.sh` runs in the caller's locale (`CALLER_LC_ALL`). Also the window failure text read `P1 window — window — …`; fixed to `window — <time>`.
- After the undo: `git diff --stat` → the three test edits only (the scripts were then untracked); the three files → `62 passed`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `534 passed, 1 xfailed, 15 warnings in 227.53s (0:03:47)`.
- Commit `775aedfd` `feat(deploy-steps): deploy-step0, deploy-outage, deploy-smoke scripts with --dry-run (D1-D4, L1 L3 L42 L66)`.

### D4 RUN — the three `--dry-run` outputs on `prompts/2026-10-02/25-deploy-scripts-card.md` (worktree copy), quoted whole
`uv run pytest -q -rP -p no:cacheprovider --color=no tests/ops/test_deploy_step0.py::test_d4_dry_run_on_the_10_02_deploy_card` (after the root fix) → `1 passed`:
```
KEYS · field JOB BRANCH WORKTREE TIP REPORT RULINGS TAG MIGRATIONS SET · 0 · all present
SHIPS · section SHIPS · 0 · 9 row(s), heads = TIP: 76f7f7d5 24001f82 0c2d9764 30452b64 8914827e e416589c 46712ab4 1ad4c546 dcdd170d
WOULD RUN: sh /Users/cobalt/cobalt-wt/deploy-steps-1003/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt-wt/deploy-steps-1003/docs/40 - DevDocs/prompts/2026-10-02/25-deploy-scripts-card.md"
WOULD RUN: TZ=America/New_York date '+%u %H %M %Y-%m-%d %a'
WOULD RUN: tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/voice-peers-check-2026-10-01.md"
WOULD RUN: git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/voice-peers-check-2026-10-01.md"
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/voice-peers-check-2026-10-01.md"
WOULD RUN: git -C /Users/cobalt/cobalt rev-parse --short=8 76f7f7d5 ops/voice-peers-1001
WOULD RUN: git -C /Users/cobalt/cobalt merge-base --is-ancestor 76f7f7d5 76f7f7d5
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat 76f7f7d5 76f7f7d5 -- . ':(exclude)docs'
WOULD RUN: git -C /Users/cobalt/cobalt show 76f7f7d5:src/cobalt/db_migrations/
WOULD RUN: tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/ops-glob-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/ops-glob-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/ops-glob-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt rev-parse --short=8 9fa18f14 ops/ops-glob-1002
WOULD RUN: git -C /Users/cobalt/cobalt merge-base --is-ancestor 9fa18f14 24001f82
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat 9fa18f14 24001f82 -- . ':(exclude)docs'
WOULD RUN: git -C /Users/cobalt/cobalt show 24001f82:src/cobalt/db_migrations/
WOULD RUN: tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/ops-seam-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/ops-seam-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/ops-seam-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt rev-parse --short=8 551f07e0 ops/ops-seam-1002
WOULD RUN: git -C /Users/cobalt/cobalt merge-base --is-ancestor 551f07e0 0c2d9764
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat 551f07e0 0c2d9764 -- . ':(exclude)docs'
WOULD RUN: git -C /Users/cobalt/cobalt show 0c2d9764:src/cobalt/db_migrations/
WOULD RUN: tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-tools-a-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/desk-tools-a-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/desk-tools-a-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt rev-parse --short=8 30452b64 ops/desk-tools-a-1002
WOULD RUN: git -C /Users/cobalt/cobalt merge-base --is-ancestor 30452b64 30452b64
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat 30452b64 30452b64 -- . ':(exclude)docs'
WOULD RUN: git -C /Users/cobalt/cobalt show 30452b64:src/cobalt/db_migrations/
WOULD RUN: tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-tools-b-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/desk-tools-b-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/desk-tools-b-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt rev-parse --short=8 8914827e ops/desk-tools-b-1002
WOULD RUN: git -C /Users/cobalt/cobalt merge-base --is-ancestor 8914827e 8914827e
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat 8914827e 8914827e -- . ':(exclude)docs'
WOULD RUN: git -C /Users/cobalt/cobalt show 8914827e:src/cobalt/db_migrations/
WOULD RUN: tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/worker-steps-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/worker-steps-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/worker-steps-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt rev-parse --short=8 e416589c ops/worker-steps-1002
WOULD RUN: git -C /Users/cobalt/cobalt merge-base --is-ancestor e416589c e416589c
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat e416589c e416589c -- . ':(exclude)docs'
WOULD RUN: git -C /Users/cobalt/cobalt show e416589c:src/cobalt/db_migrations/
WOULD RUN: tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/devfix-route-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/devfix-route-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/devfix-route-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt rev-parse --short=8 46712ab4 ops/devfix-route-1002
WOULD RUN: git -C /Users/cobalt/cobalt merge-base --is-ancestor 46712ab4 46712ab4
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat 46712ab4 46712ab4 -- . ':(exclude)docs'
WOULD RUN: git -C /Users/cobalt/cobalt show 46712ab4:src/cobalt/db_migrations/
WOULD RUN: tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-checks-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/launcher-checks-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/launcher-checks-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt rev-parse --short=8 1ad4c546 ops/launcher-checks-1002
WOULD RUN: git -C /Users/cobalt/cobalt merge-base --is-ancestor 1ad4c546 1ad4c546
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat 1ad4c546 1ad4c546 -- . ':(exclude)docs'
WOULD RUN: git -C /Users/cobalt/cobalt show 1ad4c546:src/cobalt/db_migrations/
WOULD RUN: tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/x5-tap-refresh-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/x5-tap-refresh-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/x5-tap-refresh-check-2026-10-02.md"
WOULD RUN: git -C /Users/cobalt/cobalt rev-parse --short=8 2a5fa102 s3/x5-tap-refresh-1002
WOULD RUN: git -C /Users/cobalt/cobalt merge-base --is-ancestor 2a5fa102 dcdd170d
WOULD RUN: git -C /Users/cobalt/cobalt diff --stat 2a5fa102 dcdd170d -- . ':(exclude)docs'
WOULD RUN: git -C /Users/cobalt/cobalt show dcdd170d:src/cobalt/db_migrations/
WOULD RUN: git -C /Users/cobalt/cobalt show main:src/cobalt/db_migrations/
WOULD RUN: launchctl print gui/501/com.cobalt.aset
WOULD RUN: launchctl print gui/501/com.cobalt.radar
WOULD RUN: launchctl print gui/501/com.cobalt.agent
WOULD RUN: df -k /Users/cobalt/cobalt
WOULD RUN: git -C /Users/cobalt/cobalt status --short --branch
DRY RUN — nothing run: 71 commands
```
`…test_deploy_outage.py::test_d4_dry_run_on_the_10_02_deploy_card` (`com.cobalt.aset,com.cobalt.radar MERGED`) → passed:
```
WOULD RUN: sh /Users/cobalt/cobalt-wt/deploy-steps-1003/ops/desk/deploy-step0.sh --window "/Users/cobalt/cobalt-wt/deploy-steps-1003/docs/40 - DevDocs/prompts/2026-10-02/25-deploy-scripts-card.md"
WOULD RUN: launchctl print gui/501/com.cobalt.aset
WOULD RUN: launchctl print gui/501/com.cobalt.radar
WOULD RUN: date +%s
WOULD RUN: launchctl bootout gui/501/com.cobalt.aset
WOULD RUN: launchctl print gui/501/com.cobalt.aset
WOULD RUN: launchctl bootout gui/501/com.cobalt.radar
WOULD RUN: launchctl print gui/501/com.cobalt.radar
WOULD RUN: launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist
WOULD RUN: launchctl print gui/501/com.cobalt.aset
WOULD RUN: launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist
WOULD RUN: launchctl print gui/501/com.cobalt.radar
WOULD RUN: date +%s
WOULD RUN: /Users/cobalt/cobalt/cobalt.sh status
DRY RUN — nothing run: 14 commands
```
`…test_deploy_smoke.py::test_d4_dry_run_on_the_10_02_deploy_card` → passed:
```
WOULD RUN: grep -c -F "100.82.85.27" /Users/cobalt/cobalt/configs/cobalt/voice.yaml
WOULD RUN: grep -c -F "OPS_DESK_PREFIX" /Users/cobalt/cobalt/src/cobalt/jobs/restarts.py
WOULD RUN: ls /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh
WOULD RUN: ls /Users/cobalt/cobalt/tests/ops/test_install_ops.py
WOULD RUN: ls /Users/cobalt/cobalt/ops/desk/bare-guard.py
WOULD RUN: ls /Users/cobalt/cobalt/ops/desk/deploy-card.sh
WOULD RUN: ls /Users/cobalt/cobalt/ops/desk/gate.sh
WOULD RUN: ls "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEVFIX-HUB.md"
WOULD RUN: grep -c -F "ships_checked() {" /Users/cobalt/cobalt/ops/desk/desk-launch.sh
WOULD RUN: grep -c -F "tap_version = conn.execute(" /Users/cobalt/cobalt/src/cobalt/cards/store.py
WOULD RUN: grep -c -F "100.104.48.21" /Users/cobalt/cobalt/configs/cobalt/voice.yaml
WOULD RUN: grep -c -F "127.0.0.1" /Users/cobalt/cobalt/configs/cobalt/voice.yaml
WOULD RUN: grep -c -F "path.startswith(OPS_DESK_PREFIX)" /Users/cobalt/cobalt/src/cobalt/jobs/restarts.py
WOULD RUN: ls /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh
WOULD RUN: grep -c -F "install-ops" /Users/cobalt/cobalt/ops/desk/desk-launch.sh
WOULD RUN: ls /Users/cobalt/cobalt/ops/desk/install-fixed.sh
WOULD RUN: ls /Users/cobalt/cobalt/ops/desk/gate-clean.sh
WOULD RUN: ls /Users/cobalt/cobalt/ops/desk/preflight.sh
WOULD RUN: grep -c -F "devfix)" /Users/cobalt/cobalt/ops/desk/desk-launch.sh
WOULD RUN: grep -c -F "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-" /Users/cobalt/cobalt/ops/desk/desk-launch.sh
WOULD RUN: grep -c -F "watch_line() {" /Users/cobalt/cobalt/ops/desk/desk-launch.sh
WOULD RUN: grep -c -F "taps_moved = int(tap_version) != update.tap_version" /Users/cobalt/cobalt/src/cobalt/cards/store.py
WOULD RUN: ls /Users/cobalt/cobalt/tests/cobalt/test_x5_tap_refresh_db.py
DRY RUN — nothing run: 23 commands
```
What the RUN shows (not fixed here) is under `## DECISIONS` 4.

## RESTARTS
`uv run cobalt jobs restarts a09f0862..HEAD` → exit 0, whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/deploy-steps-build-2026-10-03.md	A	DOCS	-
ops/desk/deploy-outage.sh	A	operator script; no Cobalt reader	-
ops/desk/deploy-smoke.sh	A	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	A	operator script; no Cobalt reader	-
tests/ops/test_deploy_outage.py	A	test/documentation; no resident	-
tests/ops/test_deploy_smoke.py	A	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row; nothing classified in this build.

## W THE THREE SUITES
`<tip>` = `775aedfd`.
- (a0) `git diff --name-only --no-renames a09f0862` → whole: `ops/desk/deploy-outage.sh`, `ops/desk/deploy-smoke.sh`, `ops/desk/deploy-step0.sh`, `tests/ops/test_deploy_outage.py`, `tests/ops/test_deploy_smoke.py`, `tests/ops/test_deploy_step0.py` — every path under `ops/` or `tests/ops/`. **cobalt_dev: not taken (DB: none — 6 paths)**.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `534 passed, 1 xfailed, 15 warnings in 233.79s (0:03:53)`. This build adds 62 tests there: 28 in `test_deploy_step0.py`, 19 in `test_deploy_outage.py`, 15 in `test_deploy_smoke.py`.
- (a) `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → exit 0, `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 640.47s (0:10:40)` → `<p>` = 3737. This build adds no test under `tests/cobalt` or `tests/taxonomy`.
- (b)–(d), (f): not run (DB: none).
- (e) `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (no `.env`) → `146 passed, 1 skipped, 15 warnings in 28.60s`; the skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT` → `<l>` = 146.

## PRE-STOP SELF-CHECK
(1) Every added test was RED at E2 for its row's reason (`No such file or directory`, 62 F at `7a9db92b`); each row's mutation turned its named test red (E3 table: D1 `:242`, D2 `:187` / `:248`, D3 `:141`, D4 `:332`). Two tests were rewritten and said (E3 (a), (b)).
(2) Entry paths: `grep -rn -F 'deploy-step0.sh" --window' ops/desk` → `ops/desk/deploy-outage.sh:162:wout=$(sh "$HERE/deploy-step0.sh" --window "$card" 2>&1)`, pinned by `test_a_closed_window_is_refused_before_anything_goes_down` and the window tests; `grep -rn -F 'authorize.sh" deploy' ops/desk/deploy-step0.sh` → `ops/desk/deploy-step0.sh:296:        sh "$HERE/authorize.sh" deploy "$card" 2>&1`, pinned by `test_a_rulings_row_without_approved_fails_naming_the_rule` and the happy path. Grep (tool) of `deploy-(step0|outage|smoke)\.sh` outside `tests/` → the three scripts and docs only (reports, cards); no fixed file or `desk-launch.sh` calls them. Flags: `--dry-run` / `--window` / none each pinned; states MERGED / NOT MERGED, labels in / out of the set, the agent, signals INT / TERM / HUP each pinned.
(3) Re-read at the tip: the two greps above ran after `775aedfd`; `git show 775aedfd:ops/desk/deploy-outage.sh` read whole; the RESTARTS table and the (a0) list ran on `775aedfd`.

## FOR THE CHECK
- `a09f0862..775aedfd`: `7a9db92b` `wip(deploy-steps): red — D1-D4 tests before the scripts` · `775aedfd` `feat(deploy-steps): deploy-step0, deploy-outage, deploy-smoke scripts with --dry-run (D1-D4, L1 L3 L42 L66)`.
- Per row reds, mutations and greens: `## E2 RED`, `## E3 THE ROWS`. The D4 RUN output, whole: `## E3 THE ROWS` / D4 RUN.
- Suites: `## W THE THREE SUITES` (commands and summaries); with-DB `not run (DB: none)`; `<F0>` / `<F1>` / `<F2>` `not run (DB: none)`; lock taken / released `not run (DB: none)`.
- RESTARTS: `## RESTARTS` (`RESTARTS: none`). Records copied at PREFLIGHT: `## PREFLIGHT` last paragraph.
- For CHECK ASK X1: the trap restores every label in `down`, which a label joins BEFORE its bootout call; the trap ignores INT / TERM / HUP while it restores; arguments, window and restorability are all checked before the first bootout. SIGKILL cannot be trapped (header). For X2: `--dry-run` exits before any call (`test_dry_run_calls_nothing…`, D4 mutation). For X3 / X4: `## DECISIONS` 2, 3, 5.

## CONTINUE
next: none — closed (the desk verifies and launches the check)

## DECISIONS
1. **FOR DEJAN — a test reached the real `/bin/launchctl` once (E3, first D2 run).** `test_launchctl_gone_after_the_first_bootout_reports_the_residents_down` deleted its `launchctl` stub after the stubbed bootout; the next `launchctl` calls fell through `PATH` to `/bin/launchctl`. The run's last line: `FAILED OUTAGE: com.cobalt.aset — still loaded after bootout · residents: up: com.cobalt.aset,com.cobalt.radar · down: none`, so the real `print gui/501/com.cobalt.aset` answered "loaded". By the script's code, the real launchd then received `print gui/501/com.cobalt.aset` (two or three reads) and, from the trap, `bootstrap gui/501 <pytest tmp>/repo/ops/com.cobalt.aset.plist` (a file holding `<plist/>`), possibly once more on `Bootstrap failed: 5`. No bootout reached the real launchd (the bootout was the stub's, before it removed itself). The log of that run sat in the pytest tmp folder and is not quoted. UNPROVEN what launchd did with the bootstrap; this seat has no `launchctl` string. Safe default taken: the test was fixed (the stub becomes an `exit 127` stand-in, never removed), and nothing else. The desk reads `launchctl print gui/501/com.cobalt.aset` (state, pid, `path =`) to confirm aset is as it was.
2. ASK DESK: the market holiday of P1 (iii). The hub says "a market holiday a line of the card's `## RECORDS` names with the desk's read" and fixes no form. Default taken: a `## RECORDS` line holding the word `holiday` (any case) and the day's `YYYY-MM-DD`. The small hours after a holiday are not (ii) (pinned by test).
3. ASK DESK: a carried held defect (P2: "a line that carries a held defect ships only when a row of `RULINGS` rules it carried"). Default taken: the script does not read a carry; such a line FAILS `P2 check <n>`, and the hub reads the carry itself. Said in the header.
4. DECISION D4 (what the RUN shows; nothing fixed here): (a) step0 on card `25` would run 71 commands; the `authorize.sh` it names is the copy beside the script, so at `/Users/cobalt/cobalt/ops/desk/` after adoption. (b) The outage dry run is 14 commands for `com.cobalt.aset,com.cobalt.radar`: bootout both, bootstrap both, nothing between. As the card's seam states it (the merge before the script, given as `MERGED`), the hub's 4.3 merge, 4.4 migration and 4.5 validate cannot sit between this script's bootout and bootstrap; `DEPLOY-HUB.md` today merges INSIDE the outage. The adoption card must place the call; a deploy with a migration needs its schema step before the bootout or a second shape. FOR the judge, not decided here (L72). (c) Smoke: all 23 rows of card `25` (10 markers, 13 smoke reads) map to a shape; none skipped, none refused.
5. ASK DESK (CHECK ASK X3): STEP-0 rules the script does not mirror, by the card's D1 list: P4 (the lock census), P5 (the gate worktree), P6 (markers' before values; `deploy-smoke.sh` reads markers after), P8's `path =` gate (the outage proves state and path before its first bootout). The census is recorded, never a gate, as the card says (the hub's P8 makes `state = running` a gate). Default taken: the card's list, the rest named in the header.
6. ASK DESK: a `db query` smoke row whose SQL carries `%` is SKIPPED and said (the card: it "runs only when … carries no `%`"), so on a migration card such a row does not make `SMOKE RED`. Default taken: the card's words. The agent in a restart set goes down by `cobalt.sh stop` and up by `launchctl kickstart gui/501/com.cobalt.agent` (the hub's 4.2 / 4.6), not by bootout / bootstrap; the card names bootout / bootstrap "of each label".

## RECORDS
- REFUSED, not needed: `grep -rln -F "deploy-outage.sh" ops docs/40\ -\ DevDocs/prompts/DEPLOY-HUB.md docs/40\ -\ DevDocs/prompts/BUILD-HUB.md` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." The same read was made with the Grep tool (`## PRE-STOP SELF-CHECK` (2)).
- L74: the session's attribution reminder asked for a `Claude-Session:` line; recorded under `## L74`, not acted on.
- `deploy-step0.sh` saves the caller's `LC_ALL` in two lines before `export LC_ALL=C`, to run `authorize.sh` in that locale (E3).
- No lock taken, no `.env` written (DB: none). No extra lock take.
- Card `## RECORDS` as re-read at PREFLIGHT: (1) `DB: none` — every path is under `ops/` or `tests/ops/` (W (a0) re-read it); (2) house A = Grok, one Grok hub at a time; (3) the dry run before first use and the adoption card are the desk's / the judge's.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: deploy-steps · tip: 775aedfd | on a09f0862 | migration: none | offline 3737/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 6 · for Dejan: 1
