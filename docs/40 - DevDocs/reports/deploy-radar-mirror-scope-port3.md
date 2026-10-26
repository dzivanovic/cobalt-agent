# deploy radar-mirror-scope-port3 — set: radar-mirror-scope-port3 — migrations: none

## §0 Headline
- Deploy of `ops/radar-mirror-scope-port3` (code tip `671e0215`, head `304a0b03`) on gate `deploy/radar-mirror-scope-port3` at `<m1>` `fca82a78`, card 1065: FAILED at STEP-G (a) OFFLINE, 1 failed.
- Red test: `test_radar_notes.py::test_screen_filter_values_live_only_in_approved_radar_fixtures`. It flags `docs/40 - DevDocs/reports/survey-0648-429-2026-10-26.md` (desk commit `5d7e2f128` on `main`), not this set.
- Production untouched; nothing merged; `cobalt_dev` lock never taken. Next: fix that doc on `main`, then recut.

## L74
- none

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1065-deploy-radar-mirror-scope-port3-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1065-deploy-radar-mirror-scope-port3-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-26/1065-deploy-radar-mirror-scope-port3-card.md" · 0 · ccefd299c463df3243e9e30bdf641475512fca29
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-26/1065-deploy-radar-mirror-scope-port3-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
AUTHORIZED
```
RULINGS: none.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| first launch | `ls -la ".../reports/deploy-radar-mirror-scope-port3.md"` | 1 | `No such file or directory` |
| P1 | `date` | 0 | `Mon Oct 26 16:01:12 EDT 2026` — outside 21:30-22:30 |
| P2 | `tail -n 3 ".../radar-mirror-scope-port3-check-2026-10-24.md"` | 0 | `CHECK DONE · job: radar-mirror-scope-port3 · pass: 1 · tip: 671e0215 · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9120/0 · with-DB 5956/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 17 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165034` — `held unfixed: 0`, `ready: YES`, `tip: 671e0215` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/.../radar-mirror-scope-port3-check-2026-10-24.md"` | 0 | `ba9f463499a38337a90f4baf1f252ddd3297e17e` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../radar-mirror-scope-port3-check-2026-10-24.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 671e0215` | 0 | `671e0215` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-mirror-scope-port3` | 0 | `304a0b03` = row, = `TIP` |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 671e0215 304a0b03` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 671e0215 304a0b03 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — lock free |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/radar-mirror-scope-port3` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `ccefd299` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor ccefd299 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/radar-mirror-scope-port3` | 0 | EMPTY |
| P6 | `grep -c -F "MIRROR_SOURCE_PREFIX = " /Users/cobalt/cobalt/src/cobalt/radar/notes.py` | 1 | `0` = before |
| P6 | `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` | 2 | `grep: /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py: No such file or directory` — the file is new with this set; production does not carry the marker (see `## DECISIONS` 1) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 304a0b03 -- src/cobalt/db_migrations` | 0 | nothing — `MIGRATIONS: none` holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 36927` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 36944` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1` — `com.cobalt.agent recorded retired` |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` (retired: expected) |

## THE TREE
- `git -C <GATE> merge --no-edit 304a0b03` → `Merge made by the 'ort' strategy.` (9 files changed, 561 insertions(+), 16 deletions(-): `src/cobalt/radar/notes.py`, `tests/cobalt/test_radar_{evaluate,mirror_scope (new),notes,replay,runner}.py`, three docs)
- `git -C <GATE> rev-parse --short=8 HEAD` → `fca82a78` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent ccefd299..deploy/radar-mirror-scope-port3` → `fca82a78c Merge commit '304a0b03' into deploy/radar-mirror-scope-port3` (one line, one head)
- `merge-base --is-ancestor 671e0215 deploy/radar-mirror-scope-port3` → exit 0 · `merge-base --is-ancestor 304a0b03 deploy/radar-mirror-scope-port3` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat ccefd299 deploy/radar-mirror-scope-port3 -- src/cobalt/db_migrations` → nothing (no migration; `MIGRATIONS: none`)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat ccefd299 deploy/radar-mirror-scope-port3 -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" ccefd299 deploy/radar-mirror-scope-port3` → `STEP-C: ADMITTED 0` (exit 0). `<launchd set>`: empty · `<deferred set>`: empty.

## RESTARTS
- `cd /Users/cobalt/cobalt-wt/deploy-radar-mirror-scope-port3` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` (exit 0; uv created the gate `.venv`, `Installed 257 packages in 877ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/radar/notes.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-port3-build-2026-10-24.md	A	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-port3-build-2026-10-24.result	A	DOCS	-
src/cobalt/radar/notes.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_mirror_scope.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_notes.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
- No `UNCLASSIFIED` row. NOT LOADED read: `launchctl print gui/501/com.cobalt.cos` → exit 0, `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.cos.plist`, `pid = 36938` → kept.
- `<restart set>`: `com.cobalt.aset com.cobalt.cos com.cobalt.radar`
- `<deferred set>`: none · `<launchd set>`: none
- com.cobalt.agent: recorded retired — not restarted (not derived by this range either)

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 671e0215 fca82a78 -- . ":(exclude)docs"` → prints `src/cobalt/prefill/cli.py | 12 +`, `src/cobalt/prefill/refresh_probe.py | 458 +++`, `tests/cobalt/test_prefill_refresh.py | 46 ++++`, `tests/cobalt/test_refresh_probe.py | 253 +++` (4 files, 769 insertions; `main` moved since the check) → clause does not hold; the gate runs whole.
- Deselects: the build report (`radar-mirror-scope-port3-build-2026-10-24.md:166`) ran `gate.sh … all --deploy` with "no `--deselect`: this build adds no with-DB test" → none. `TICKERS: none` → no `--tickers`. No `--migration`.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `265 passed, 163 skipped in 19.59s` — 0 failed (every skip is a with-DB `Postgres env settings not available` / `requires_db` skip).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-radar-mirror-scope-port3 all --deploy --deploy-gate` → exit 1, verdict lines whole:
```
RED (exit 1): 1 failed, 5004 passed, 878 skipped, 4 xfailed, 36 warnings in 834.10s (0:13:54)
1 failed, 5004 passed, 878 skipped, 4 xfailed, 36 warnings in 834.10s (0:13:54)
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-radar-mirror-scope-port3-all-20261026-160256.log
```
- (a) OFFLINE — RED. The failing test, log `:88`–`:113`: `tests/cobalt/test_radar_notes.py::test_screen_filter_values_live_only_in_approved_radar_fixtures` (`tests/cobalt/test_radar_notes.py:43`), `AssertionError: assert ['docs/40 - D...026-10-26.md'] == []` · `Left contains one more item: 'docs/40 - DevDocs/reports/survey-0648-429-2026-10-26.md'`.
- The offender is not this set's file: `git -C /Users/cobalt/cobalt log --oneline -2 -- "docs/40 - DevDocs/reports/survey-0648-429-2026-10-26.md"` → `5d7e2f128 docs(desk): R2497 survey 0648 done` (a desk commit on `main`, inside `<m0>`). `grep -n -F "f=" ".../survey-0648-429-2026-10-26.md"` → `:16` (screen `down_gappers`) and `:17` (screen `morning_low_float`) each carry a screen URL query whose filter parameter holds real `sh_` / `ta_` filter values (not quoted here: this report sits under the same test's `docs/40 - DevDocs` root): the screen filter values the L32/L45 test allows only under `tests/fixtures/radar`. The `main` tree at `<m0>` fails the same test; this set's code is not implicated. Never "known" (L68, L70): the run ends here.
- The lock was never taken (the gate ended at (a), before (b)): `ls -la <GATE>/.env` → `No such file or directory`; `grep -c -x -F "deploy-radar-mirror-scope-port3" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory`. `cobalt_dev` untouched.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

## Deploy table
- Nothing merged to `main`, nothing in production changed: no bootout, no tag, no snapshot. `rollback: not used`.

## Smoke
- not reached.

## CONTINUE
- ended FAILED at STEP-G (a) `Mon Oct 26 16:17:34 EDT 2026`. The desk's next step: a docs fix on `main` for `survey-0648-429-2026-10-26.md` (`:16`, `:17`), then `desk-launch.sh recut "<card>"` (RECUT; not resumed here).

## DECISIONS
1. ASK DESK: card `## MARKERS` line 2 gives `before 0`, but the test file `tests/cobalt/test_radar_mirror_scope.py` is new with this set, so on production `grep -c -F` exits 2 `No such file or directory` rather than printing `0`. Production plainly does not carry the marker (the P6 failure is "production already carries"). Safe default taken: read as `before` (absent = not carried), continue; the `after 1` read at smoke (d) stands as written. [Mon Oct 26 16:01:12 EDT 2026]

## RECORDS
- radar-mirror-scope-port3: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-mirror-scope-port3-check-2026-10-24.md` last line: CHECK DONE · job: radar-mirror-scope-port3 · pass: 1 · tip: 671e0215 · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9120/0 · with-DB 5956/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 17 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165034 (card)
- radar-mirror-scope-port3: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-mirror-scope-port3` → `304a0b03`; code tip `671e0215` (card)
- written by deploy-card.sh at 2026-10-26 15:49 ET (`date`); trial merge of the heads onto main in order: clean (card)
- Gate red on a `main` docs file: `docs/40 - DevDocs/reports/survey-0648-429-2026-10-26.md:16-17` carries real screen filter values (the `sh_` / `ta_` families) that `tests/cobalt/test_radar_notes.py:43` refuses outside `tests/fixtures/radar`. Every gate cut from `main` at or after `5d7e2f128` fails offline until that doc is fixed: the next deploy of any set is blocked on it too.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-radar-mirror-scope-port3` and branch `deploy/radar-mirror-scope-port3` (holding merge `fca82a78`), and its `.venv` created by uv at STEP-R.
- No downtime. No `REFUSED` call. No message received. L74: none.

FAILED: gate — G (a) — tests/cobalt/test_radar_notes.py::test_screen_filter_values_live_only_in_approved_radar_fixtures (offender docs/40 - DevDocs/reports/survey-0648-429-2026-10-26.md, from main 5d7e2f128) · rollback: not used · decisions: 1 · for Dejan: 0 · tokens: 113218
