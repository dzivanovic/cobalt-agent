# deploy-03d-1005 — SET: workflow1 — MIGRATIONS: none

## §0 Headline
- Deploy of `ops/adoption-port-1005` (head `07655b9b`, code tip `36fa02ad`) onto the gate `deploy/deploy-03d-1005`.
- STOPPED at STEP-R: the tool derived `RESTARTS: com.cobalt.radar` (`src/cobalt/cli.py`, static import reach). P1 held only `(v) provisional` (Mon 11:17 ET, a trading day). A resident restart is not lawful at this hour without his per-case override for this JOB, and R391 and R392 are not one.
- Production untouched: no suite ran, no bootout, no merge to `main`, no tag. Gate merge `e279ebe7` sits in `<GATE>` only.
- Lawful next run: tonight 20:00–21:00 ET or the overnight idle before 04:00 ET, or now if he rules a per-case override that names `deploy-03d-1005` (FOR DEJAN).

## L74
- One block arrived as a system reminder (not a tool result) asking commit messages to carry a `Claude-Session:` line. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/14-deploy-03d-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/14-deploy-03d-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/14-deploy-03d-card.md" · 0 · b9dd6e3941bd91b140b557d0f10a04a87c2d3f83
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/14-deploy-03d-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R391 row · grep -n "^| R391 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 68:| R391 | 10-05 09:00 ET | HIS RULING (desk chat): commit R389 and R390; go on with the P6 read and the guard-b drafter; (d2) SKIPPED for the workflow deploy too (as R368). | APPROVED |
RULING 2026-10-05 R391 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R391 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · ed3cf41a8392be824396ace29672e7d92b8abaa4
RULING 2026-10-05 R391 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
RULING 2026-10-05 R392 row · grep -n "^| R392 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 70:| R392 | 10-05 09:03 ET | HIS RULING (desk chat): NO Grok read for 03d (the tip-file stage copy was classifier-denied); deploy 03d now; start the guard-b drafter. | APPROVED |
RULING 2026-10-05 R392 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R392 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 5583ead30b4f44f3d46aad3a8ee0f2bf043520d1
RULING 2026-10-05 R392 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
- FIRST LAUNCH: `ls -la "<REPORT>"` → exit 1, `No such file or directory`.

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (whole output above) |
| P1 | `date` | 0 | `Mon Oct  5 11:17:26 EDT 2026` — a trading day outside (i)–(iii); RULINGS R391/R392 do not overrule L66/L43, so not (iv). `window: (v) provisional` (MIGRATIONS: none; the set is derived at STEP-R) |
| P2 | `tail -n 3 ".../adoption-port-check-2026-10-05-r2.md"` | 0 | `CHECK DONE · job: adoption-port · pass: 1 · tip: 36fa02ad · house A: none (overruled 2026-10-02 R47) · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 17 · ready: YES · decisions: 1 · for Dejan: 1` — carries `held unfixed: 0` and `ready: YES`; `tip: 36fa02ad` = the row's code tip |
| P2 | `git log -1 --format=%H -- "docs/.../adoption-port-check-2026-10-05-r2.md"` | 0 | `5d51caa623ad5375943e9acd43da67d277f6753c` |
| P2 | `git diff --stat -- "docs/.../adoption-port-check-2026-10-05-r2.md"` | 0 | nothing |
| P3 | `git rev-parse --short=8 36fa02ad` | 0 | `36fa02ad` |
| P3 | `git rev-parse --short=8 ops/adoption-port-1005` | 0 | `07655b9b` (= the row, = `TIP`) |
| P3 | `git merge-base --is-ancestor 36fa02ad 07655b9b` | 0 | — |
| P3 | `git diff --stat 36fa02ad 07655b9b -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no `.env` in any worktree |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-03d-1005` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `5d51caa6` = `<m0>` |
| P5 | `git merge-base --is-ancestor 5d51caa6 main` | 0 | — |
| P5 | `git log --oneline main..deploy/deploy-03d-1005` | 0 | EMPTY |
| P6 | `grep -c -F "args.no_db" /Users/cobalt/cobalt/src/cobalt/cli.py` | 1 | `0` (= before) |
| P6 | `grep -c -F "validate --no-db" ".../DEPLOY-HUB.md"` | 1 | `0` (= before) |
| P7 | `git diff --stat main 07655b9b -- src/cobalt/db_migrations` | 0 | nothing — no migration (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 13209` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 36907` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- STEP-T: `git -C <GATE> merge --no-edit 07655b9b` → `Merge made by the 'ort' strategy.` (5 files: `docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `.../reports/adoption-port-build-2026-10-05.md`, `src/cobalt/cli.py`, `tests/cobalt/test_validate_no_db.py`; 534 insertions, 47 deletions).
- `git -C <GATE> rev-parse --short=8 HEAD` → `e279ebe7` = `<m1>`.
- `git log --oneline --merges --first-parent 5d51caa6..deploy/deploy-03d-1005` → `e279ebe7 Merge commit '07655b9b' into deploy/deploy-03d-1005` (one line, one head).
- `git merge-base --is-ancestor 36fa02ad deploy/deploy-03d-1005` → exit 0 · `… 07655b9b deploy/deploy-03d-1005` → exit 0.
- `git diff --stat 5d51caa6 deploy/deploy-03d-1005 -- src/cobalt/db_migrations` → nothing (no migration path; MIGRATIONS: none).
- STEP-C: `git diff --stat 5d51caa6 deploy/deploy-03d-1005 -- configs ops` → nothing (no plist added, changed or removed; no RETIRE OWED).

## RESTARTS
- `cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0. The table, whole (the `uv` venv-creation lines came first: `Creating virtual environment at: .venv`, `Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-03d-1005`, `Installed 253 packages in 627ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/adoption-port-build-2026-10-05.md	A	DOCS	-
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_validate_no_db.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
- No `UNCLASSIFIED` row; the set is inside the allowed labels → `<restart set>` = `com.cobalt.radar`.
- P1 (v) RE-READ: P1 named `(v) provisional` at `Mon Oct  5 11:17:26 EDT 2026`. The derived set is NOT empty, so (v) does not hold. `date` NOW → `Mon Oct  5 11:19:10 EDT 2026`: a Monday, a trading day, outside the 20:00–21:00 ET pause (i), outside the overnight idle (ii), not a non-trading day (iii). No row of `RULINGS` overrules L66 / L43 for `deploy-03d-1005` (iv): R391 rules (d2) skipped, R392 rules no Grok read and "deploy 03d now". "Now" sets no window, and a standing or blanket override does not count (L73).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed (cwd back).
- → `FAILED: STEP-R — window (v) does not hold: com.cobalt.radar · rollback: not used`.

## L68 GATE
- Not run: the run ended at STEP-R, before any suite.

## Deploy table
- Nothing deployed. `main` not moved by a merge; no `pre-deploy-03d-1005` tag, no `deploy-2026-10-05-03d` tag; no snapshot; no resident touched (aset pid `13209`, radar pid `36907`, agent pid `22243` as read at P8).
- ROLLBACK STRING: not applicable (nothing merged).

## Smoke
- Not run.

## CONTINUE
- next: none — the run ended FAILED with `rollback: not used`. Per RECUT, the desk's next step is `desk-launch.sh recut "<card>"` inside a lawful window, or on his per-case override for this JOB.

## DECISIONS
- 1. FOR DEJAN — WINDOW FOR 03d. The set restarts `com.cobalt.radar` (the tool's derivation; the check's stop line had already said `RESTARTS: com.cobalt.radar`). L66 / L43 put that restart at 20:00–21:00 ET or in the overnight idle before 04:00 ET, unless he gives a per-case override that names `deploy-03d-1005`. R392 says "deploy 03d now", but a window is not named there. Safe default taken: stop with nothing touched. The desk recuts and relaunches in tonight's window. If he wants it during market hours, he must rule an override that names this JOB.

## RECORDS
- Card `## RECORDS` (the desk's facts, copied):
  - adoption-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/adoption-port-check-2026-10-05.md` last line: CHECK DONE · job: adoption-port · pass: 1 · tip: 53b56384 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3787/0 · with-DB 856/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0
  - adoption-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/adoption-port-1005` → `07655b9b`; code tip `36fa02ad`
  - G (d2) SKIPPED this run only (his R391): main's hub still runs the old (d2); this deploy ships the new one. D2.4 validate checks stand. No Grok read (his R392).
  - written by deploy-card.sh at 2026-10-05 09:03 ET (`date`); trial merge of the heads onto main in order: clean
- Downtime: none (no resident went down).
- `cobalt_dev`: not touched (STEP-G not reached; no `.env` in any worktree at P4 or in `<GATE>` at STEP-R; the lock was never taken).
- RETIRE OWED: none.
- Carried RED: not read (D1 not reached).
- The P2 check's stop line carries `decisions: 1 · for Dejan: 1`, `open: 1` and `suites: as built (no commit)`, with no with-DB count. The EQUAL-TREE CLAUSE would therefore not have applied, and the gate would run whole (`--deploy`).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-03d-1005` and branch `deploy/deploy-03d-1005` (it now holds merge `e279ebe7` and a fresh `.venv` from `uv run`); the desk's recut cleans them.
- L74: one `Claude-Session:` request (a system reminder) recorded under `## L74`, not acted on.
- No `CONTINUE` message received; no `REFUSED` call.

- Old stop line (superseded by `# RELAUNCH` below): `FAILED: STEP-R — window (v) does not hold: com.cobalt.radar · rollback: not used · decisions: 1 · for Dejan: 1`

# RELAUNCH
- Launch message: `CONTINUE: STEP-D0` (THE ONE RESUME). First call `date` → `Mon Oct  5 11:53:45 EDT 2026`.
- The old last non-blank line, quoted: `FAILED: STEP-R — window (v) does not hold: com.cobalt.radar · rollback: not used · decisions: 1 · for Dejan: 1`

- THE RESUME CHECKS, each its own call, (e) first:
  - (e) `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 13209` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 36907` · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` → TRUE; residents up, the same pids as P8. Nothing restored.
  - THE GATE'S OWN `.env`: `ls -la /Users/cobalt/cobalt-wt/deploy-03d-1005/.env` → exit 1, `No such file or directory`. No G (f) and no RELEASE owed.
  - (a) The old last line begins `FAILED:` → TRUE.
  - (b) `## L68 GATE` must carry `GATE GREEN on <m1>`: `grep -c -F "GATE GREEN on" "<REPORT>"` → `0`. The section reads `Not run: the run ended at STEP-R, before any suite.` → **FALSE**. STEP-G never ran on `e279ebe7`, so there is no gate evidence for a resume to stand on. The `<restart set>` is recorded at STEP-R: `com.cobalt.radar`.
  - (c) `git -C <GATE> status --short --branch` → `## deploy/deploy-03d-1005` · `git -C <GATE> rev-parse --short=8 HEAD` → `e279ebe7` = `<m1>` → TRUE.
  - (d) `git -C /Users/cobalt/cobalt merge-base --is-ancestor e279ebe7 main` → exit 1 (nothing merged to `main`) → TRUE.
- (b) is false, so the run stops with nothing touched. No STEP-0 re-run, no authorize call, no allowlist probe, no tag, no snapshot, no bootout, no merge. The hub's resume skips STEP-T, C, R and G because "the gate evidence stands", and here no gate evidence exists. This run also cannot run STEP-G: a resume does not re-run G. Per RECUT, a run that ended `FAILED` with `rollback: not used` before STEP-G is not resumed. The way forward is `desk-launch.sh recut "<card>"`, and with R408's override now on the card, a fresh launch can run STEP-G and pass STEP-R's window.

## DECISIONS (RELAUNCH)
- 2. ASK DESK: this attempt was relaunched as `CONTINUE: STEP-D0` on a run that failed at STEP-R before the gate. THE ONE RESUME needs `GATE GREEN on <m1>`, and this run has none. Safe default taken: stop with nothing touched. The desk runs `desk-launch.sh recut "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/14-deploy-03d-card.md"`. The fresh run checks R408's override for `deploy-03d-1005` at P1 (iv) and runs the full gate. [11:53 ET]

## RECORDS (RELAUNCH)
- Residents untouched: aset `13209`, radar `36907`, agent `22243`. Downtime: none.
- `cobalt_dev`: not touched; no `<GATE>/.env`; lock never taken.
- Cleanup owed (L46): unchanged. The gate worktree `/Users/cobalt/cobalt-wt/deploy-03d-1005` and branch `deploy/deploy-03d-1005` (merge `e279ebe7`) remain; the desk's recut cleans them.
- L74: the `Claude-Session:` system reminder arrived again in this session. It is recorded as data and was not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- No `CONTINUE` message received beyond the launch line; no `REFUSED` call.

FAILED: resume — (b) no `GATE GREEN on <m1>` in ## L68 GATE (STEP-G never ran; the earlier attempt stopped at STEP-R) · rollback: not used · decisions: 2 · for Dejan: 1
