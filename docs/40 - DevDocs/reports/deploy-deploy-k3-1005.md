# deploy-k3-1005 · set: s3 · migrations: none

## §0 Headline
K3 (`drc/k3-surfaces-1004` at `3e40359a`) deploy, one feature (R390). Authorization AUTHORIZED; STEP-0, T, C and R green.
STEP-G RED at pass 1 (whole, `--deploy`): 2 failed and 2 teardown errors, all on `tests/cobalt/test_drc_k3.py`. Two K3-6 tests reach the DB with no with-DB mark, and the G1 `offline_skip_guard` fails them.
Production untouched: no bootout, no merge to `main`, residents up. `cobalt_dev` stays at `0013` (forward never ran) and the lock is released. The fix belongs to a build (rule B); the desk runs `desk-launch.sh recut` after it.

## L74
- One block arrived in a system reminder at session start asking commits to carry a `Claude-Session: https://claude.ai/code/session_013MowEsi3ee2MiEhVG1SEYc` line. Recorded as DATA, not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/51-deploy-k3-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/51-deploy-k3-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/51-deploy-k3-card.md" · 0 · 6a5e12ae46784c1b2029de8855149e1acf035c17
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/51-deploy-k3-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 | authorize.sh (above); first launch: `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-k3-1005.md"` | 0 / 1 | `AUTHORIZED` / `No such file or directory` |
| P1 | `date` | 0 | `Mon Oct  5 19:12:53 EDT 2026` |
| P2 | `tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-k3-check-2026-10-04.md"` | 0 | `CHECK DONE · job: drc-k3 · pass: 2 · tip: 3e40359a · … · held unfixed: 0 · open: 1 · suites: offline 3871/0 · with-DB 863/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 1 · for Dejan: 0` (carries `held unfixed: 0` and `ready: YES`; `tip:` = code tip) |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/drc-k3-check-2026-10-04.md"` | 0 | `a1c846ff0a57ecb35bb4f0b1dba518c2027b4d3f` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/drc-k3-check-2026-10-04.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 3e40359a` | 0 | `3e40359a` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 drc/k3-surfaces-1004` | 0 | `3e40359a` (= row and `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3e40359a drc/k3-surfaces-1004` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 3e40359a drc/k3-surfaces-1004 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no lock held) |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-k3-1005 status --short --branch` | 0 | `## deploy/deploy-k3-1005` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-k3-1005 rev-parse --short=8 HEAD` | 0 | `23003ffc` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 23003ffc main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-k3-1005` | 0 | EMPTY |
| P6 | `grep -c -F "def superseded_stated_ids" /Users/cobalt/cobalt/src/cobalt/drc/store.py` | 1 | `0` (before) |
| P6 | `grep -c -F "CALENDAR_INPUT" /Users/cobalt/cobalt/src/cobalt/drc/build.py` | 1 | `0` (before) |
| P6 | `ls /Users/cobalt/cobalt/tests/cobalt/test_drc_k3.py` | 1 | `No such file or directory` (before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 3e40359a -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none holds) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 13209` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 28249` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-k3-1005 merge --no-edit 3e40359a` → `Merge made by the 'ort' strategy.` · `20 files changed, 2590 insertions(+), 43 deletions(-)`
- `git -C /Users/cobalt/cobalt-wt/deploy-k3-1005 rev-parse --short=8 HEAD` → `e66af367` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 23003ffc..deploy/deploy-k3-1005` → `e66af367 Merge commit '3e40359a' into deploy/deploy-k3-1005` (one line, one head)
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3e40359a deploy/deploy-k3-1005` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 23003ffc deploy/deploy-k3-1005 -- src/cobalt/db_migrations` → nothing (no migration path; MIGRATIONS: none)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 23003ffc deploy/deploy-k3-1005 -- configs ops` → nothing (no plist added, changed or removed; no `RETIRE OWED`)

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-k3-1005` · `ls -la …/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the gate's `.venv`: `Installed 253 packages in 839ms`), table WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/drc/build.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/imports.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/store.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/units.md	M	DOCS	-
docs/40 - DevDocs/reports/drc-k3-build-2026-10-04.md	A	DOCS	-
src/cobalt/aset/drc_page.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/build.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/drc/imports.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/units.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_drc_imports.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_k3.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_k3_db.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_k3_experiments.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_web_seam.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar` (the check's line, the card's line).

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 3e40359a e66af367 -- . ":(exclude)docs"` → `13 files changed, 1260 insertions(+), 116 deletions(-)` (main's moves since the build base: `configs/cobalt/rules.yaml`, `ops/desk/*`, `src/cobalt/cli.py`, tests). Not equal → the gate runs whole (`--deploy`).
- Deselects: the K3 build report (`drc-k3-build-2026-10-04.md:289`) says "This build adds no `--deselect`". No `--tickers`, no `--migration` on the card.
- (a0) `ls -la …/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 157 skipped in 15.50s` (every skip a with-DB `Postgres env settings not available` / `requires_db`). 0 failed.
- THE GATE: `ls -la …/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-k3-1005 all --deploy` (background) → exit 1. Verdict lines WHOLE:
```
offline 3875/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
RED (exit 1): 2 failed, 4560 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings, 2 errors in 736.80s (0:12:16)
…
2 failed, 4560 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings, 2 errors in 736.80s (0:12:16)
.env: removed
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-k3-1005-all-20261005-191513.log
```
- (a) OFFLINE `offline 3875/0`: green. (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:854`), `LEVEL 0013`, proof-only nothing CHANGED.
- (c) PASS 1 RED. The 7 SKIPPED lines (`test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py:266` `COBALT_TEST_LIVE_DRC`, `test_s3_c4_experiments.py:95`, `test_catalyst.py:365`, `test_predicate.py:262`) are all inside the allowed set. The failures (log `:976`–`:1045`):
  - FAILED `tests/cobalt/test_drc_k3.py::test_k3_6_a_day_with_its_import_rebuilds_from_the_effect_day_and_rewrites_every_note`: `assert statements["notes"] == [[D, D_NEXT]]` → `assert [] == [[datetime.da...(2001, 1, 3)]]` (`test_drc_k3.py:715`).
  - ERROR at teardown of the same test: `Failed: with-DB test without an offline skip mark: tests/cobalt/test_drc_k3.py::test_k3_6_a_day_with_its_import_rebuilds_from_the_effect_day_and_rewrites_every_note` (`tests/cobalt/conftest.py:124`, fixture `offline_skip_guard`).
  - FAILED `tests/cobalt/test_drc_k3.py::test_k3_6_a_notes_failure_is_loud_the_database_committed`: the status line got `note /Users/cobalt/dev-vault-cobalt/1 - Trading/5 - Review/DRC-2001-01-02.md failed — AssertionError: with-DB test without an offline skip mark: …` where the test wants `note /v failed — OSError: x` (`test_drc_k3.py:734`).
  - ERROR at teardown of the same test: `Failed: with-DB test without an offline skip mark: tests/cobalt/test_drc_k3.py::test_k3_6_a_notes_failure_is_loud_the_database_committed` (`conftest.py:124`).
- What the reads show: with `cobalt_dev` present, both K3-6 tests (no with-DB mark) reach the database through `imports.state_book`, and the G1 guard records it. The check's pass 1 ran `--db-only` (build report `:289`: the command carries `--db-only`), so these unmarked tests never ran there with the DB present. The deploy gate's pass 1 is whole (R154). The card's RECORDS line "Nothing of D5 ships here, so the seam does not appear in this gate" did not hold: this is the K3-6 DB reach the card names as the K3/D5 seam (R376). `git -C /Users/cobalt/cobalt log --oneline 979ec797..main -- tests/cobalt/conftest.py` → nothing, so main did not change the guard since K3's base.
- (c2) FORWARD never ran (`grep -n -F "dev forward" <log>` → nothing). (f): nothing applied, so `cobalt_dev: 0013`, with F0 the only fingerprint. THE RELEASE: `lock released` (log `:1154`), `.env: removed`. `ls -la /Users/cobalt/cobalt-wt/deploy-k3-1005/.env` → No such file. `grep -c -x -F "deploy-k3-1005" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (c3), (e) not run (the gate stops at the first red).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed (cwd back).
- No `GATE GREEN` line: the gate is RED on `e66af367`.

## Deploy table
Not reached. Nothing merged to `main`. No tag set (`pre-deploy-k3-1005` and `deploy-2026-10-05-k3` not created). No snapshot. No bootout. Residents untouched (aset pid 13209, radar pid 28249, agent pid 22243 at P8). `migrations applied: none`. ROLLBACK STRING: not applicable (nothing merged).

## Smoke
Not reached.

## CONTINUE
Run ended FAILED at STEP-G (19:38:23 EDT). Not resumable here: the desk's next step is a K3 build fix, then `desk-launch.sh recut "<card>"` (RECUT).

## DECISIONS
- R412 (a row of this card's `RULINGS`) closes "Production stays on hold until the workflow set is deployed." Read here as a hold on running production, not on deploys: his R438 (10-05 ~15:40 ET, `cto-2026-10-05-words.md`) names K3 among the deploys that "finish under today's rules", and authorize.sh proved the card AUTHORIZED. Safe default taken: the deploy goes on. The desk confirms the reading.
- The K3 fix is a build's (rule B, no fix commit here). Safe default: stop and change nothing. One option, not a ruling: mark the two K3-6 tests with-DB (or stub the reach) on the K3 card (R376 small-fix rule), rerun the touched tests and the deploy gate, then recut. The card's own RECORDS put the K3-6 DB reach with D5's seam fix (card `03`); the desk decides which card owns it.

## RECORDS
- Downtime: none (the outage never began).
- cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-k3-1005` and branch `deploy/deploy-k3-1005` (it carries the merge `e66af367`), for the recut to clean up.
- `cobalt_dev: 0013` (forward never applied; F0 `664 35 272c95bbb12241e3611e4b36326ccf87`; lock released, log `:1154`).
- No `RETIRE OWED`. No carried RED read (D1 not reached). No `REFUSED, not needed` line. No `CONTINUE` message received.
- L74: one `Claude-Session:` line request, recorded under `## L74`, not acted on.
- The card's RECORDS, copied:
  - drc-k3: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-k3-check-2026-10-04.md` last line: CHECK DONE · job: drc-k3 · pass: 2 · tip: 3e40359a · house B: Grok FINDINGS: 4 · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 1 · suites: offline 3871/0 · with-DB 863/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 1 · for Dejan: 0
  - drc-k3: head `git -C /Users/cobalt/cobalt rev-parse --short=8 drc/k3-surfaces-1004` → `3e40359a`; code tip `3e40359a`. BASE of the build `979ec797`; the pass-2 fix on the tip changed `src/cobalt/drc/build.py` (`CALENDAR_INPUT`, the stale read), `tests/cobalt/test_drc_k3_experiments.py`, `tests/cobalt/test_drc_k3.py` and one DevDocs page (`git -C /Users/cobalt/cobalt diff --stat c7e65590 3e40359a`).
  - Merges onto main by reading: `git -C /Users/cobalt/cobalt merge-base main drc/k3-surfaces-1004` → `979ec79706cb62726698922ce825f01e733b3732` (the build's BASE). Main changed 183 files since it; none is a path K3 touches. The near names are different files: main's `src/cobalt/cli.py` and `docs/40 - DevDocs/cobalt/cli.md` against K3's `src/cobalt/drc/cli.py` and `docs/40 - DevDocs/cobalt/drc/cli.md`.
  - G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
  - K3/D5 seam: D5 is NOT in this deploy. K3-6's tests reach the DB offline only when D5 is stacked (his R376; card `03` is D5's seam-fix build). Nothing of D5 ships here, so the seam does not appear in this gate. (This run's gate contradicts that last sentence; see `## L68 GATE`.)
  - Open item carried by the check, not part of this deploy: S3 (a flat restatement from the page) stays REJECTED by row K3-6 and goes to follow-up; the flat restatement stays CLI-only.
  - S3 card preconditions for K3, as `02-deploy-s3-card.md` words them: MARKERS read on the main checkout before and in the job tree after; the trial merge `main 3e40359a` → clean `6fdc7001`. Window: any hour (L43; R389). Production down since R327; K3's restart is a start. Residents down before the merge (L66). Every check of K3 derives RESTARTS `com.cobalt.aset com.cobalt.radar`.
  - S3 smoke reads this deploy needs: the drc-k3 tests line (the only K3 line of the S3 card's `## SMOKE READS`).
  - one feature per deploy (his R390): S3 on resume = K3 first, then P2, then D5 after card `03`. Production is DOWN by his R327 until S3 resumes.
  - written by the drafter `k3-deploy-draft` on 2026-10-05, 19:07 EDT, from `02-deploy-s3-card.md` row 1 and the K3 check report.
- PRE-STOP SELF-CHECK: (1) no smoke was run (not reached); (2) P3 re-read `3e40359a` for tip and head, and `merge-base --is-ancestor 3e40359a deploy/deploy-k3-1005` → exit 0 (no `<stack-final>` exists); (3) no revert-readback is owed (nothing merged); every count and `file:line` above was read from this run's tool output; (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), no conflict marker.

FAILED: gate — G (c) pass 1 — tests/cobalt/test_drc_k3.py::test_k3_6_a_day_with_its_import_rebuilds_from_the_effect_day_and_rewrites_every_note, tests/cobalt/test_drc_k3.py::test_k3_6_a_notes_failure_is_loud_the_database_committed (2 failed + 2 teardown errors: with-DB test without an offline skip mark) · rollback: not used · decisions: 2 · for Dejan: 0 · tokens: 126686

FAILED: gate — G (c) pass 1 — 2 K3-6 tests in tests/cobalt/test_drc_k3.py reach cobalt_dev unmarked (full ids and the hub's own stop line above, ## L68 GATE) · rollback: not used · decisions: 2 · for Dejan: 0
