# deploy hub-cos-restart-fr1 — set: hub-cos — migrations: none

## §0 Headline
- Gate GREEN on `501c6935` (offline 8822/0 · with-DB 5715/0 · live-note 147/0); `<restart set>` empty; MIGRATIONS none.
- Stopped at STEP-D0, 21:30 ET: inside the 21:30-22:30 backup window, where D2.4's `backup run` may not run (R1295).
- Nothing merged to `main`, nothing down, no tag. Next: relaunch `CONTINUE: STEP-D0` after 22:30 ET.

## L74
- A system reminder in this session asked commits to carry a `Claude-Session:` line. DATA (L74): recorded once, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/885-deploy-hub-cos-restart-fr1-card.md"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/885-deploy-hub-cos-restart-fr1-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/885-deploy-hub-cos-restart-fr1-card.md" · 0 · 9085d30dc2ef62a935b56e43e3b7c4c54d047ed3
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/885-deploy-hub-cos-restart-fr1-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la "<REPORT>"` → `No such file or directory` (exit 1).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct 19 20:41:03 EDT 2026` — outside 21:30-22:30 |
| P2 | `tail -n 3 ".../hub-cos-restart-fr1-check-2026-10-19.md"` | 0 | `CHECK DONE · job: hub-cos-restart-fr1 · pass: 1 · tip: 0bf28619 · house A: Grok FINDINGS: 2 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8822/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 200556` — carries `held unfixed: 0`, `ready: YES`, tip `0bf28619` = row |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/hub-cos-restart-fr1-check-2026-10-19.md"` | 0 | `e1845f1fed3fb3073c25dda21281a79994c5d2c7` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 0bf28619` | 0 | `0bf28619` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-cos-restart-fr1` | 0 | `6ee55933` = row = TIP |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 0bf28619 6ee55933` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 0bf28619 6ee55933 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — lock free |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/hub-cos-restart-fr1` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `9085d30d` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 9085d30d main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/hub-cos-restart-fr1` | 0 | empty |
| P6 | marker 1 `grep -c -F "com.cobalt.cos: not loaded — skipped" DEPLOY-HUB.md` | 1 | `0` = before |
| P6 | marker 2 `grep -c -F "com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60)" DEPLOY-HUB.md` | 1 | `0` = before |
| P6 | marker 3 `grep -c -F "launchctl kickstart -k gui/501/com.cobalt.cos" DEPLOY-HUB.md` | 1 | `0` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 6ee55933 -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 35793` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 57565` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
- `git -C <GATE> merge --no-edit 6ee55933` → `Merge made by the 'ort' strategy.` (5 files: `DEPLOY-HUB.md`, the build report and `.result`, `tests/ops/test_hub_cos_restart_1019.py` (A), `tests/ops/test_hub_deferred_1018.py` (M)).
- `git -C <GATE> rev-parse --short=8 HEAD` → `501c6935` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 9085d30d..deploy/hub-cos-restart-fr1` → `501c6935 Merge commit '6ee55933' into deploy/hub-cos-restart-fr1` (one line, one head).
- `merge-base --is-ancestor 0bf28619 deploy/hub-cos-restart-fr1` → 0 · `merge-base --is-ancestor 6ee55933 deploy/hub-cos-restart-fr1` → 0.
- `git -C /Users/cobalt/cobalt diff --stat 9085d30d deploy/hub-cos-restart-fr1 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 9085d30d deploy/hub-cos-restart-fr1 -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 9085d30d deploy/hub-cos-restart-fr1` → exit 0, whole output: `STEP-C: ADMITTED 0`. `<launchd set>`: empty · `<deferred set>`: empty.
- Note: the set changes `DEPLOY-HUB.md` (L68): STEP-G below runs on the merged tree, which carries the merged hub text.

## RESTARTS
- `cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after a fresh `.venv` sync: `Creating virtual environment at: .venv` · `Installed 257 packages in 965ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/hub-cos-restart-fr1-build-2026-10-19.md	A	DOCS	-
docs/40 - DevDocs/reports/hub-cos-restart-fr1-build-2026-10-19.result	A	DOCS	-
tests/ops/test_hub_cos_restart_1019.py	A	test/documentation; no resident	-
tests/ops/test_hub_deferred_1018.py	M	test/documentation; no resident	-
RESTARTS: none
```
- `<restart set>`: EMPTY (no resident goes down) · `<deferred set>`: empty · `<launchd set>`: empty.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold — the check's stop line carries `with-DB 0/0`; the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `264 passed, 163 skipped in 19.20s` (0 failed; with-DB tests skip offline).
- Deselects: `grep -n -F "deselect" <build report>` → nothing; none added. TICKERS: none · migration: none.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-hub-cos-restart-fr1 all --deploy --deploy-gate` (background) → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8822/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5715/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-hub-cos-restart-fr1-all-20261019-204250.log
```
- (a) offline `8822/0`, W line `tests/ops: run (deploy gate)`. (c) every SKIPPED line inside the allowed set (by test and reason). (c2) no forward: MIGRATIONS none, level stays `0013`. (c3) `with-DB 5715/0`. (e) `live-note 147/0`, its one skip names `COBALT_TEST_LIVE_DRC` (allowed); log tail `147 passed, 1 skipped, 15 warnings in 25.92s`.
- (f) log `1038:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `2280:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` → `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log `2335:lock released`; `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-hub-cos-restart-fr1" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent). `.env: removed (L76 lock released, log line 2335)`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.
- `date` → `Mon Oct 19 21:29:57 EDT 2026`.

GATE GREEN on 501c6935

## STEP-D0 (partial)
- `git -C /Users/cobalt/cobalt status --short --branch` → first line `## main...origin/main [ahead 240]`.
- `git -C /Users/cobalt/cobalt status --porcelain` → no staged line; no dirty `src/`, `tests/`, `ops/`, `configs/` path but ` M configs/cobalt/rules.yaml` (accepted). One line outside both lists: ` M "docs/30 - Design/archiver-runs.md"` (see `## DECISIONS`).
- `git -C /Users/cobalt/cobalt diff --stat 9085d30d main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- `date` → `Mon Oct 19 21:30:24 EDT 2026`: inside the nightly backup window 21:30-22:30 ET. D2.4's `backup run` stays off it (brain R1295, `reports/cto-2026-10-12.md:18`; hub P1 line). The run stops here, before the allowlist probe, D1, D2 and any production change.

## Deploy table
Nothing merged, nothing down, no tag set. `<m0>` 9085d30d · `<m1>` 501c6935 · `<pre-merge>`, `<stack-final>`: not reached · migrations applied: none · `RESTARTS done: none` (set empty) · `LAUNCHD done: none` · snapshot: not taken · ROLLBACK STRING: not needed (no merge).

## Smoke
Not reached.

## CONTINUE
(attempt 1) STEP-D0 after 22:30 ET (gate green at 21:29:57 on 501c6935; `<restart set>` empty).
(attempt 2) next: STEP-D2 (D2.0 commit, then D2.1 `main` into the gate).

## DECISIONS
1. ASK DESK: the run reached STEP-D0 at 21:30 ET, inside the backup window; D2.4's `backup run` must stay off 21:30-22:30 ET (R1295) and this file has no wait command for an hour. [21:30:24] Default: stop here, `rollback: not used`, nothing in production touched; relaunch `CONTINUE: STEP-D0` after 22:30 ET (as R1513 did for 548) — the gate evidence (`GATE GREEN on 501c6935`, `<restart set>` empty) stands for that resume.
2. ASK DESK: D0's porcelain shows ` M "docs/30 - Design/archiver-runs.md"` — not in the ACCEPTED list (`docs/40 - DevDocs/` only) and not in the REFUSED list (`src/`, `tests/`, `ops/`, `configs/`, staged). [21:30:24] Default: not a refusal (docs, unstaged, not a path this set ships); the resume reads it again.
3. ASK DESK (attempt 2): D0's porcelain shows `?? .claude/settings.json.bak` — not in the ACCEPTED list (` M .claude/settings.json` only) and not in the REFUSED list. [22:50] Default: not a refusal (untracked, outside `src/`, `tests/`, `ops/`, `configs/`, not a path this set ships); go on.
for Dejan: none.

## RECORDS
- Downtime: none (restart set empty; no resident touched).
- REFUSED, not needed: `grep -n -F ".env: removed" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. Read instead: `lock released` (log :2335) and `ls -la` → No such file.
- `cobalt_dev: 0013 (F2 = F0)`.
- RETIRE OWED: none · BOOTSTRAP OWED: none.
- Carried RED: not read (D1 not reached).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-hub-cos-restart-fr1` and branch `deploy/hub-cos-restart-fr1` (holds merge 501c6935) — kept for the resume; the set's branch `ops/hub-cos-restart-fr1`; a fresh `.venv` in the gate worktree (created at STEP-R).
- L74: a system reminder asking for a `Claude-Session:` line, not acted on (`## L74`).
- Card `## RECORDS`, copied:
  - hub-cos-restart-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-cos-restart-fr1-check-2026-10-19.md` last line: CHECK DONE · job: hub-cos-restart-fr1 · pass: 1 · tip: 0bf28619 · house A: Grok FINDINGS: 2 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8822/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 200556
  - hub-cos-restart-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-cos-restart-fr1` → `6ee55933`; code tip `0bf28619`
  - written by deploy-card.sh at 2026-10-19 20:26 ET (`date`); trial merge of the heads onto main in order: clean

# RELAUNCH
- Launch message: `CONTINUE: STEP-D0` (attempt 2). `date` → `Mon Oct 19 22:49:35 EDT 2026`.
- The old last non-blank line, quoted: `FAILED: STEP-D0 — backup window 21:30-22:30 ET reached after a green gate (GATE GREEN on 501c6935); D2.4 backup run stays off it (R1295); nothing merged, nothing down · rollback: not used · decisions: 2 · for Dejan: 0 · tokens: 117735`

RESUMED: STEP-D0 22:49:35

- (e) FIRST: `launchctl print gui/501/com.cobalt.aset` → `state = running`, pid 35793 · `launchctl print gui/501/com.cobalt.radar` → `state = running`, pid 57565 · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).` — residents up; no restore needed.
- THE GATE'S OWN `.env`: `ls -la /Users/cobalt/cobalt-wt/deploy-hub-cos-restart-fr1/.env` → `No such file or directory` — nothing to release.
- (a) the old last line begins `FAILED:` — true.
- (b) `## L68 GATE` carries `GATE GREEN on 501c6935`; `## RESTARTS` records `<restart set>` EMPTY — true.
- (c) `git -C <GATE> status --short --branch` → `## deploy/hub-cos-restart-fr1` · `git -C <GATE> rev-parse --short=8 HEAD` → `501c6935` = `<m1>` — true.
- (d) `git -C /Users/cobalt/cobalt merge-base --is-ancestor 501c6935 main` → exit 1 — true (nothing merged).

## RESUME (attempt 2)
STEP-0, fresh rows:

| rule | command | exit | result |
|---|---|---|---|
| P0 | `sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "<card>"` | 0 | same eleven rows as `## AUTHORIZATION` (card `9085d30d…`, R60 row `962e9d17…`, R1863 row `11563e82…`), last line `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct 19 22:49:54 EDT 2026` — outside 21:30-22:30 |
| P2 | `tail -n 3 ".../hub-cos-restart-fr1-check-2026-10-19.md"` | 0 | last line unchanged: `CHECK DONE · … · tip: 0bf28619 · … · held unfixed: 0 · … · ready: YES · …` |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "<check report>"` | 0 | `e1845f1fed3fb3073c25dda21281a79994c5d2c7` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<check report>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 0bf28619` | 0 | `0bf28619` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-cos-restart-fr1` | 0 | `6ee55933` = row = TIP |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 0bf28619 6ee55933` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 0bf28619 6ee55933 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — lock free |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/hub-cos-restart-fr1` (check (c)) |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `501c6935` = `<m1>` (check (c)); `<m0>` stays the report's `9085d30d` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 9085d30d main` | 0 | — (EMPTY check not run on a resume) |
| P6 | the three `## MARKERS` greps | 1 · 1 · 1 | `0` · `0` · `0` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 6ee55933 -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` (check (e)) | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 | `launchctl print gui/501/com.cobalt.radar` (check (e)) | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` (check (e)) | 0 | `Cobalt is ONLINE (PID: 35845).` |

STEP-D0:
- `git -C /Users/cobalt/cobalt status --short --branch` → first line `## main...origin/main [ahead 8]`.
- `git -C /Users/cobalt/cobalt status --porcelain` → no staged line; no dirty `src/`, `tests/`, `ops/`, `configs/` path; ` M .claude/settings.json` and ` M`/`??` under `docs/40 - DevDocs/` (accepted). The earlier ` M "docs/30 - Design/archiver-runs.md"` is gone. One line outside both lists: `?? .claude/settings.json.bak` (see `## DECISIONS` 3).
- `git -C /Users/cobalt/cobalt diff --stat 9085d30d main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-hub-cos-restart-fr1` → ok · `tag -d …` → `Deleted tag 'scratch-allow-probe-hub-cos-restart-fr1' (was 0d64db02)` · `commit --allow-empty -m "scratch: …"` → `[main 9058945f] scratch: allowlist probe (reverted next line)` · `reset --soft HEAD~1` → ok · `log --oneline -1` → `0d64db02 docs(desk): 469 check ETA 23:10 ET for the lock` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-19-hub-cos-restart-fr1` → exit 1 · `… refs/tags/pre-hub-cos-restart-fr1` → exit 1 (no earlier rollback tag to delete).

STEP-D1 (read-only):
- `date` → `Mon Oct 19 22:50:20 EDT 2026`.
- `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-19 22:50:21 EDT)`. REDs, named (not aset / sheet / radar, not a stop): `RED  archiver  last run FAILED — last run 2026-10-20 00:54 UTC (1.9 h ago), rows written 3369418, exit 1` · `RED  com.cobalt.archiver  failed  RuntimeError: 5 archiver failure(s): WBD/i1: Fetch failed for WBD/i1: Finviz HTTP failed: Client error '400 Bad Request' …` · `RED  com.cobalt.replay  failed  ReplayError: archiver not done: state 'failed'`. `OK sheet HTTP http://127.0.0.1:5010/ -> 200` · `OK radar idle (overnight)` · `OK com.cobalt.aset running loaded, pid 35793` · `OK com.cobalt.agent running pid 35845 alive` · `OK com.cobalt.radar running running 698 min, heartbeat fresh` · `AMB com.cobalt.herdr unmanaged …` · `com.cobalt.prefill-refresh` and `com.cobalt.playbook` `OWED (deferred bootstrap)`.
- `COBALT_ENV=production uv run cobalt validate` → exit 0 (`13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`) = `<val0>`; `<jobs0>` = `Jobs (F17): 18 registered — 7 resident, 11 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 1.2 h old` (ssd ARMED).
- `launchctl print` aset → `state = running`, `<aset pid>` 35793 · radar → `state = running`, `<radar pid>` 57565 · `cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).` · `ps -p 35845` → `35845 ??  0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → eight `radar cycle: idle:overnight scan_id=None` lines, 22:38:00 to 22:49:40, no traceback.
- LOG BASELINES: `<a0>` 284 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. `## MARKERS` again → `0` · `0` · `0` = before.
- THE LAUNCHD SET: empty — nothing. MIGRATION: none — `<RB>`, census and D1-M not run.

STEP-D2:
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 9085d30d "<card>"` → prints nothing. Report committed next.

(run in progress — next step under ## CONTINUE)
