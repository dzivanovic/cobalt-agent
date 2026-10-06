# deploy-p2-1005 · set: s3 · migrations: none

## §0 Headline
- Deploy of `f15/p2-replay-1004` (code tip `437c7299`, head `6269f05e`) onto `main`, card `prompts/2026-10-05/61-deploy-p2-card.md`.
- STEP-0, T, C, R green; GATE GREEN on `0d80e076` (offline 3932/0 · with-DB 4809/0 · live-note 146/0; `cobalt_dev: 0013 — F2 = F0`; lock released).
- STEP-D0 FAILED: a STAGED line on `main` (`M  "docs/40 - DevDocs/reports/seat-usage.md"`), unstaged at this session's start. Production untouched; nothing merged to `main`; no tag set.

## L74
- A system block in this session's context asked commits to end with a `Claude-Session: https://claude.ai/code/session_01Nwt9epo4bgFB8rgmTtNJ5s` line. Recorded as DATA (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/61-deploy-p2-card.md"` → exit 0, output WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/61-deploy-p2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/61-deploy-p2-card.md" · 0 · 4c58a87901b49c491ef79c835238029cced71004
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/61-deploy-p2-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-03 R326 row · grep -n "^| R326 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · 332:| R326 | 10-05 06:19 ET | HIS RULING: A on all three — D5 ships at `c96b5118` with O1 pinned (follow-up card: items' store + B2 wording); second-writer survey gets its 5 read strings, this seat only; F15 P2 X11 → follow-up card. Words: `cto-2026-10-05-words.md` R326–R327. | HIS RULING · APPROVED |
RULING 2026-10-03 R326 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R326 |" -- "docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · b133743171ec855e164c445ceef03e657eb50eeb
RULING 2026-10-03 R326 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-p2-1005.md"` → exit 1, `No such file or directory`.

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct  5 23:34:21 EDT 2026` |
| P2 | `tail -n 3 ".../reports/f15-p2-check-2026-10-05.md"` | 0 | `CHECK DONE · job: f15-p2 · pass: 1 · tip: 437c7299 · house A: Grok FINDINGS: 0 (Sol METER) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 20 · ready: YES · decisions: 0 · for Dejan: 0` — carries `held unfixed: 0`, `ready: YES`, `tip: 437c7299` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/f15-p2-check-2026-10-05.md"` | 0 | `4e8795dc5d93751a628be63bcce5b445e71957f9` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/f15-p2-check-2026-10-05.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 437c7299` | 0 | `437c7299` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 f15/p2-replay-1004` | 0 | `6269f05e` (= row, = `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 437c7299 6269f05e` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 437c7299 6269f05e -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no lock held) |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-p2-1005 status --short --branch` | 0 | `## deploy/deploy-p2-1005` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-p2-1005 rev-parse --short=8 HEAD` | 0 | `1757a53c` = `<m0>` (= `main`) |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 1757a53c main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-p2-1005` | 0 | EMPTY |
| P6 | `grep -c -F "def corpus(" .../cards/predictions.py` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "def replay(" .../cards/predictions.py` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "def cmd_replay" .../cards/cli.py` | 1 | `0` (before `0`) |
| P6 | `ls /Users/cobalt/cobalt/tests/cobalt/test_f15_p2_replay.py` | 1 | `No such file or directory` |
| P6 | `ls /Users/cobalt/cobalt/tests/experiments/f15_p2/conftest.py` | 1 | `No such file or directory` |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main f15/p2-replay-1004 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 47333` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 47343` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-p2-1005 merge --no-edit 6269f05e` → `Merge made by the 'ort' strategy.` (10 files changed, 1822 insertions(+), 4 deletions(-); `docs/.../cards/cli.md`, `docs/.../cards/predictions.md`, `reports/f15-p2-build-2026-10-04.md`, `ops/desk/gate-lists.md`, `src/cobalt/cards/cli.py`, `src/cobalt/cards/predictions.py`, `tests/cobalt/test_f15_p2_replay.py`, `tests/cobalt/test_f15_p2_replay_db.py`, `tests/experiments/f15_p2/conftest.py`, `tests/experiments/f15_p2/test_x7_x10_x11_db.py`).
- `git -C /Users/cobalt/cobalt-wt/deploy-p2-1005 rev-parse --short=8 HEAD` → `0d80e076` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 1757a53c..deploy/deploy-p2-1005` → `0d80e076 Merge commit '6269f05e' into deploy/deploy-p2-1005` (one line, one head).
- `merge-base --is-ancestor 437c7299 deploy/deploy-p2-1005` → exit 0; `merge-base --is-ancestor 6269f05e deploy/deploy-p2-1005` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 1757a53c deploy/deploy-p2-1005 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 1757a53c deploy/deploy-p2-1005 -- configs ops` → ` ops/desk/gate-lists.md | 4 ++--` / ` 1 file changed, 2 insertions(+), 2 deletions(-)`. No plist added, modified or removed.

## RESTARTS
- `cd /Users/cobalt/cobalt-wt/deploy-p2-1005` · `ls -la /Users/cobalt/cobalt-wt/deploy-p2-1005/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the gate's `.venv`: `Using CPython 3.14.3 … Installed 253 packages in 551ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cards/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cards/predictions.md	M	DOCS	-
docs/40 - DevDocs/reports/f15-p2-build-2026-10-04.md	A	DOCS	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
src/cobalt/cards/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/cards/predictions.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_f15_p2_replay.py	A	test/documentation; no resident	-
tests/cobalt/test_f15_p2_replay_db.py	A	test/documentation; no resident	-
tests/experiments/f15_p2/conftest.py	A	test/documentation; no resident	-
tests/experiments/f15_p2/test_x7_x10_x11_db.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
- No `UNCLASSIFIED`. `<restart set>` = `com.cobalt.aset com.cobalt.radar`.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold. `git -C /Users/cobalt/cobalt diff --stat 437c7299 0d80e076 -- . ":(exclude)docs"` → 18 files, 1680 insertions(+), 206 deletions(-) (main's D5/K3/desk changes since the check), and the check's stop line carries no with-DB count (`suites: as built (no commit)`). The gate runs whole (`--deploy`).
- Deselects: the build report `reports/f15-p2-build-2026-10-04.md` line 155 ran pass 1 with `--deselect tests/cobalt/test_f15_p2_replay_db.py` → passed here too. `--tickers`: the card gives none → not passed (see DECISIONS). `--migration`: none.
- G (a0): `ls -la …/deploy-p2-1005/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 157 skipped in 15.82s` (every skip a with-DB `Postgres env settings not available` / `requires_db: needs cobalt_dev`). 0 failed.
- THE GATE: `ls -la …/deploy-p2-1005/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-p2-1005 all --deploy --deselect tests/cobalt/test_f15_p2_replay_db.py` (background) → exit 0, verdict lines WHOLE:
```
offline 3932/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4809/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-p2-1005-all-20261005-233610.log
```
- (a) `offline 3932/0`. (c)+(c3) `with-DB 4809/0`. (e) `live-note 146/0`.
- SKIPPED lines: all seven inside the allowed set. `test_s3_c4_experiments.py:95` is `@requires_live` on `def test_x14_live_his_template_strips_to_the_committed_fixture()` (Grep of the gate tree, lines 95–96). `test_replay_line.py:266` names `COBALT_TEST_LIVE_DRC`.
- (c2) log line 1081: `dev forward: APPLIED 23:58:53`. (f) log line 872 `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`, line 1830 `F2: 664 35 272c95bbb12241e3611e4b36326ccf87`, line 1881 `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log lines 1882–1887 `sh …/release-devdb-lock.sh deploy-p2-1005` → `lock released` · `.env: removed` (the log carries no clock on this line; between `23:58:53` and my `date` `Tue Oct  6 00:03:50 EDT 2026`). `ls -la …/deploy-p2-1005/.env` → No such file; `grep -c -x -F "deploy-p2-1005" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (no lock dir).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 0d80e076

## Deploy table
STEP-D0 (MAIN), each its own call:
- `git -C /Users/cobalt/cobalt status --short --branch` → first line `## main...origin/main [ahead 33]`.
- `git -C /Users/cobalt/cobalt status --porcelain` → among the lines: `M  "docs/40 - DevDocs/reports/seat-usage.md"` — first column `M` = STAGED. (This session's start snapshot showed ` M "docs/40 - DevDocs/reports/seat-usage.md"`, unstaged; this session ran no `git add`.) Every other line is ` M` / `??` under `docs/40 - DevDocs/`, ` M .claude/settings.json`, or `?? .claude/settings.json.bak`.
- `git -C /Users/cobalt/cobalt diff --stat 1757a53c main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- Rule: a STAGED line → `FAILED PREFLIGHT: staged change on main`. The run stops here: no allowlist probe, no D1, no D2.0 commit, no main-into-gate merge, no snapshot, no `pre-deploy-p2-1005` tag, no bootout. `<pre-merge>` / `<stack-final>`: not reached. migrations applied: none. ROLLBACK STRING: not applicable (nothing merged).

## Smoke
Not reached.

## CONTINUE
STOPPED at STEP-D0 (MAIN) 00:04:19 EDT 2026-10-06. The gate evidence (`GATE GREEN on 0d80e076`, restart set `com.cobalt.aset com.cobalt.radar`) stands; the gate worktree `deploy-p2-1005` holds `<m1>` `0d80e076`, unchanged, no `.env`.

## DECISIONS
1. ASK DESK: `main` carries a staged `docs/40 - DevDocs/reports/seat-usage.md` that this session did not stage (the hub says no desk staging on `main` from launch to the stop line). Who staged it, and is it unstaged before the next launch? Safe default taken: stop with `FAILED PREFLIGHT` and touch nothing on `main` but this report. [00:04:19 EDT 2026-10-06]
2. ASK DESK: the card gives no `--tickers`, so the gate's stray-row read did not run (`stray rows: not read (no --tickers given)`). The P2 build ran `--tickers ZZPB,TEST` (build report line 155). Safe default taken: the card's value (none). Should the recut card name `ZZPB,TEST`? [00:04:19 EDT 2026-10-06]
3. ASK DESK: R412 (one of `RULINGS`, `AUTHORIZED`) contains the words "production HOLD". The card's `## RECORDS` say production is DOWN by R327 until S3 resumes, and that K3 started the residents. This run reached no production write, so it did not depend on reading that phrase. Before the next launch, confirm the HOLD does not bind this deploy. [00:04:19 EDT 2026-10-06]

## RECORDS
- downtime: none (no resident touched). Residents at P8: aset pid 47333, radar pid 47343, agent PID 22243, all running / ONLINE.
- `cobalt_dev: 0013 (F2 = F0)`; lock released by `gate.sh`, `.env: removed`.
- RETIRE OWED: none. Carried RED: not read (D1 not reached). REFUSED, not needed: none. CONTINUE messages: none received.
- cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-p2-1005` and branch `deploy/deploy-p2-1005` (at `0d80e076`, with a `.venv` that uv built at STEP-R); the gate log `/Users/cobalt/cobalt-wt/.gate-logs/deploy-p2-1005-all-20261005-233610.log`. Per RECUT, the desk's next step is `desk-launch.sh recut "<card>"`.
- L74: one block, recorded under `## L74`, not acted on.
- Card `## RECORDS`, copied:
  - f15-p2: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f15-p2-check-2026-10-05.md` last line: CHECK DONE · job: f15-p2 · pass: 1 · tip: 437c7299 · house A: Grok FINDINGS: 0 (Sol METER) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 20 · ready: YES · decisions: 0 · for Dejan: 0
  - f15-p2: head `6269f05e`; code tip `437c7299`. Build report last line: `BUILT · job: f15-p2 · tip: 437c7299 | on 3c1f75b8 | migration: none | offline 3926/0 | with-DB 878/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 6 of 6 | self-check: 3 of 3 | decisions: 5 · for Dejan: 0`.
  - G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
  - Merges onto main by reading: merge-base `3c1f75b8…`; main changed none of P2's ten files since; no overlap.
  - P2 ships alone: D5 DEPLOYED `c8503415`, K3 `07a4b8fe`; `c96b5118`, `3c1f75b8`, `07a4b8fe`, `c8503415` ancestors of main.
  - Production state: DOWN by his R327 until S3 resumes; K3 (`07a4b8fe`) started `com.cobalt.aset` and `com.cobalt.radar`. They are running now.
  - Markers dropped: `drc/reconcile.py` (D5's file).
  - K3-F1 mark record: P2's DB tests carry module-level `requires_db`; no unmarked database test.
  - S3 smoke reads: the f15-p2 replay-tests line only.
  - S3 card preconditions: MARKERS before/after; MIGRATIONS `none`; window: any hour (L43).
  - FOLLOW-UP OWED, NOT PART OF THIS DEPLOY (R326): F15 P2 X11, the `no_trigger` row (`replay/runner.py:431-432`; build report DECISION 3).
  - Written by the drafter `p2-deploy-draft` 2026-10-05 22:40 EDT; re-pointed by `p2-repoint` 23:31 EDT.

FAILED PREFLIGHT: staged change on main — M  "docs/40 - DevDocs/reports/seat-usage.md" · rollback: not used · decisions: 3 · for Dejan: 0 · tokens: 111745
