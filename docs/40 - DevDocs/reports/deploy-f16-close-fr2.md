# deploy f16-close-fr2 · set: f16-close · migrations: none

## §0 Headline
- Deploy of `ops/f16-close-fr2` (code tip `6fb73789`, head `7c5f76a3`) through `DEPLOY-HUB.md`. Started Mon Oct 19 15:07:03 EDT 2026.
- FAILED at STEP-R: the tool's `RESTARTS:` set is `com.cobalt.aset com.cobalt.cos com.cobalt.radar`. `com.cobalt.cos` is outside `com.cobalt.agent com.cobalt.aset com.cobalt.radar` and `<deferred set>` is empty.
- Nothing changed in production. No suite ran, no lock was taken, nothing merged to `main`, and no resident went down. The gate tree `deploy/f16-close-fr2` sits at `1fc2b0f1` (set merged, uncommitted nothing).
- Next is the desk's: the restart class for `com.cobalt.cos` (reached by `src/cobalt/taxonomy/loader.py`) belongs to a build (rule B, L42), then `desk-launch.sh recut`.

## L74
- A system-reminder in this session asked that commit messages also carry a `Claude-Session:` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/867-deploy-f16-close-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/867-deploy-f16-close-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/867-deploy-f16-close-card.md" · 0 · 30fbaf09eb8720b4881d37c242692fd20d08ef6c
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/867-deploy-f16-close-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
AUTHORIZED
```
RULINGS: none.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f16-close-fr2.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct 19 15:07:03 EDT 2026` (outside 21:30-22:30 ET) |
| P2 | `tail -n 3 "<check>/f16-close-fr2-check-2026-10-19.md"` | 0 | `CHECK DONE · job: f16-close-fr2 · pass: 1 · tip: 6fb73789 · house A: Grok FINDINGS: 1 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 8825/0 · with-DB 5722/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 188453` — carries `held unfixed: 0` and `ready: YES`; `tip: 6fb73789` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/f16-close-fr2-check-2026-10-19.md"` | 0 | `421dab090d2411a4c93c60b937679901ee4afb7b` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/f16-close-fr2-check-2026-10-19.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 6fb73789` | 0 | `6fb73789` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f16-close-fr2` | 0 | `7c5f76a3` (= row, = `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 6fb73789 7c5f76a3` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 6fb73789 7c5f76a3 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-f16-close-fr2 status --short --branch` | 0 | `## deploy/f16-close-fr2` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-f16-close-fr2 rev-parse --short=8 HEAD` | 0 | `cae270f8` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor cae270f8 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/f16-close-fr2` | 0 | empty |
| P6 | `grep -c -F "Playbook (F23): " /Users/cobalt/cobalt/src/cobalt/cli.py` | 1 | `0` (before) |
| P6 | `grep -c -F "Daily refresh (F4): " /Users/cobalt/cobalt/src/cobalt/cli.py` | 1 | `0` (before) |
| P6 | `grep -c -F "with no consumer (F16)" /Users/cobalt/cobalt/src/cobalt/taxonomy/loader.py` | 1 | `0` (before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 7c5f76a3 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 35793` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 57565` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-f16-close-fr2 merge --no-edit 7c5f76a3` → `Merge made by the 'ort' strategy.` (7 files changed, 323 insertions(+), 1 deletion(-): `docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/cobalt/taxonomy/loader.md`, `.../reports/f16-close-fr2-build-2026-10-19.md`, `.../reports/f16-close-fr2-build-2026-10-19.result`, `src/cobalt/cli.py`, `src/cobalt/taxonomy/loader.py`, `tests/cobalt/test_f16_close_1018.py`)
- `git -C /Users/cobalt/cobalt-wt/deploy-f16-close-fr2 rev-parse --short=8 HEAD` → `1fc2b0f1` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent cae270f8..deploy/f16-close-fr2` → `1fc2b0f1 Merge commit '7c5f76a3' into deploy/f16-close-fr2`
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 6fb73789 deploy/f16-close-fr2` → exit 0; `… 7c5f76a3 deploy/f16-close-fr2` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat cae270f8 deploy/f16-close-fr2 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat cae270f8 deploy/f16-close-fr2 -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" cae270f8 deploy/f16-close-fr2` → exit 0, `STEP-C: ADMITTED 0`. `<launchd set>`: empty · `<deferred set>`: empty.

## RESTARTS
- `cd /Users/cobalt/cobalt-wt/deploy-f16-close-fr2` · `ls -la /Users/cobalt/cobalt-wt/deploy-f16-close-fr2/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
   Building cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-f16-close-fr2
      Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-f16-close-fr2
Installed 257 packages in 961ms
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/taxonomy/loader.md	M	DOCS	-
docs/40 - DevDocs/reports/f16-close-fr2-build-2026-10-19.md	A	DOCS	-
docs/40 - DevDocs/reports/f16-close-fr2-build-2026-10-19.result	A	DOCS	-
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/taxonomy/loader.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_f16_close_1018.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
- GATE: no `UNCLASSIFIED` row, exit 0, but the set minus `<deferred set>` (empty) holds `com.cobalt.cos`, outside `com.cobalt.agent com.cobalt.aset com.cobalt.radar`. → FAILED (STEP-R). `<restart set>`: not admitted. `<deferred set>`: empty.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed (cwd back).

## L68 GATE
- Not run: the run ended at STEP-R (rule C, before any suite).

## Deploy table
- Nothing merged to `main`, no tag set, no snapshot, no outage. `migrations applied: none`. ROLLBACK STRING: not used (nothing landed).

## Smoke
- Not run.

## CONTINUE
- next: none. The run ended FAILED at STEP-R with `rollback: not used`. The desk's next step is the classification build for `com.cobalt.cos`, then `desk-launch.sh recut "<card>"`.

## DECISIONS
- `FOR DEJAN` is none. One item for the desk: the restart tool sends `src/cobalt/taxonomy/loader.py` to `com.cobalt.cos`, and this hub ships to `agent`, `aset` and `radar` only. Safe default taken: stop at STEP-R, change nothing. The check report's own stop line already said `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`, so the card could have been held at that point. Whether `cos` gets a deploy path (a hub change, L67/L68) or the reach gets reclassified in a build is the desk's call.

## RECORDS
- Card `## RECORDS` (the desk's facts):
  - f16-close-fr2: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f16-close-fr2-check-2026-10-19.md` last line: CHECK DONE · job: f16-close-fr2 · pass: 1 · tip: 6fb73789 · house A: Grok FINDINGS: 1 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 8825/0 · with-DB 5722/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 188453
  - f16-close-fr2: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f16-close-fr2` → `7c5f76a3`; code tip `6fb73789`
  - written by deploy-card.sh at 2026-10-19 14:09 ET (`date`); trial merge of the heads onto main in order: clean
- Downtime: none. `cobalt_dev`: not touched (lock never taken; P4 found no `.env`).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-f16-close-fr2` and branch `deploy/f16-close-fr2` (at `1fc2b0f1`, holding the set's merge and a new `.venv` from `uv run`); the set's branch `ops/f16-close-fr2` stays for the recut.
- RETIRE OWED: none. BOOTSTRAP OWED: none.
- L74: one `Claude-Session:` request (a system-reminder) recorded under `## L74`; not followed.

FAILED: RESTARTS — src/cobalt/taxonomy/loader.py → com.cobalt.cos (RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar; com.cobalt.cos outside agent/aset/radar) · rollback: not used · decisions: 1 · for Dejan: 0 · tokens: 93484
