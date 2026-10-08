# deploy desk-ops-fixes-1008 (attempt 2) · SET: none · MIGRATIONS: none

## §0 Headline
Green deploy: `ops/desk-ops-fixes-1008` (code tip `2413dbec`, head `9aca7680`) landed on `main`: `4b0aa106..c2bda2a4` (fast-forward), tag `deploy-2026-10-08-desk-ops-fixes-attempt2`, rollback tag `pre-desk-ops-fixes-1008`.
Gate GREEN on `4366bab8`: offline 3991/0 · with-DB 4875/0 · live-note 146/0; `cobalt_dev: 0013 — F2 = F0`, lock released.
RESTARTS: none — no resident went down; aset 37788, radar 37799, agent 22243 unchanged. No migration.
Smoke GREEN: markers 0→4 / 0→3 / 0→2, curls 200, radar cycled at 10:47:51, failure counts flat, heartbeat GREEN.
One ASK DESK (an untracked `.claude/settings.json.bak` on `main`), nothing for Dejan.

## L74
The session's harness context (a system reminder, not a tool result) asked for a `Claude-Session: https://claude.ai/code/session_01DSimJUYbzuMQYvhchdHYjp` trailer on commits. Recorded once here as data; not acted on — this run's commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/113-deploy-desk-ops-fixes-card.md"` → exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/113-deploy-desk-ops-fixes-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/113-deploy-desk-ops-fixes-card.md" · 0 · 5facc838aa968914337ddcdabb6df99dce76daf5
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/113-deploy-desk-ops-fixes-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R657 row · grep -n "^| R657 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 10:| R657 | 07:13 ET | HIS RULING (words: `cto-2026-10-08-words.md` R657, "approved"): one ops card, rows G1-G4 from the brain's relay, no DB. LAUNCHING drafter `desk-ops-fixes-draft`, prompt `105`, card `106` to follow. | HIS RULING · APPROVED |
RULING 2026-10-08 R657 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R657 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · c6b4a04d639c181b21ff0af0b849c3bf938dcc4d
RULING 2026-10-08 R657 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

First launch: `ls -la "<REPORT>"` → exit 1, `No such file or directory` (before this write).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Thu Oct  8 10:12:17 EDT 2026` (no restart window binds, L43) |
| P2 | `tail -n 3 "<check report>"` | 0 | last line: `CHECK DONE · job: desk-ops-fixes · pass: 1 · tip: 2413dbec · house A: Sol FINDINGS: 6 · findings: 11 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 6 · house B: Grok FINDINGS: 0 · suites: offline 3991/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 20 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 101004` — carries `held unfixed: 0` and `ready: YES`, `tip: 2413dbec` = the row's code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/desk-ops-fixes-check-2026-10-08.md"` | 0 | `12cee3244794d242be57e5de2e8a57c03d9a5eef` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/desk-ops-fixes-check-2026-10-08.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 2413dbec` | 0 | `2413dbec` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/desk-ops-fixes-1008` | 0 | `9aca7680` (= row, = TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 2413dbec 9aca7680` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 2413dbec 9aca7680 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no lock held |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/desk-ops-fixes-1008-attempt2` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `5facc838` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5facc838 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/desk-ops-fixes-1008-attempt2` | 0 | empty |
| P6 | `grep -c -F "NOTIFY FAILED" /Users/cobalt/cobalt/ops/desk/close-timer.sh` | 1 | `0` (= before) |
| P6 | `grep -c -F "session list unreadable" /Users/cobalt/cobalt/ops/desk/stop-guard.py` | 1 | `0` (= before) |
| P6 | `grep -c -F "REPLACED:" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` | 1 | `0` (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 9aca7680 -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 37788` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 37799` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 9aca7680` → `Merge made by the 'ort' strategy.` (10 files, 802 insertions, 61 deletions: `ops/desk/close-timer.sh`, `ops/desk/desk-launch.sh`, `ops/desk/stop-guard.py`, six `tests/ops/` files, two docs files).
- `<m1>` = `4366bab8`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 5facc838..deploy/desk-ops-fixes-1008-attempt2` → `4366bab8 Merge commit '9aca7680' into deploy/desk-ops-fixes-1008-attempt2` (one line, one head).
- `merge-base --is-ancestor 2413dbec <BRANCH>` → exit 0; `merge-base --is-ancestor 9aca7680 <BRANCH>` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 5facc838 <BRANCH> -- src/cobalt/db_migrations` → nothing (no migration, as `MIGRATIONS: none`).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 5facc838 <BRANCH> -- configs ops` →
```
 ops/desk/close-timer.sh | 73 ++++++++++++++++++++++++++++++++++++++++-----
 ops/desk/desk-launch.sh | 29 +++++++++++++-----
 ops/desk/stop-guard.py  | 79 ++++++++++++++++++++++++++++++++++---------------
 3 files changed, 141 insertions(+), 40 deletions(-)
```
  No plist added, modified or removed. No RETIRE OWED.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
docs/40 - DevDocs/reports/desk-ops-fixes-build-2026-10-08.md	A	DOCS	-
ops/desk/close-timer.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/stop-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_close_timer.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_devfix.py	M	test/documentation; no resident	-
tests/ops/test_desk_wakeup_rule.py	A	test/documentation; no resident	-
tests/ops/test_install_ops.py	M	test/documentation; no resident	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
(preceded by uv's venv creation lines: `Creating virtual environment at: .venv` · `Installed 253 packages in 789ms`.) No UNCLASSIFIED row. `<restart set>` = EMPTY (none): no resident goes down; the merge lands with residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold — the check's stop line carries `with-DB 0/0` (no with-DB count above 0); the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 163 skipped in 16.02s` — 0 failed (every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- Deselects: the build report `desk-ops-fixes-build-2026-10-08.md` names none (`grep deselect` → no match). TICKERS none, no `--migration`.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-desk-ops-fixes-1008-attempt2 all --deploy` launched in background (`date` right after: `Thu Oct  8 10:14:07 EDT 2026`). Exit 0. Verdict lines WHOLE:
```
offline 3991/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4875/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-desk-ops-fixes-1008-attempt2-all-20261008-101359.log
```
- (a) OFFLINE → `offline 3991/0`.
- (b) lock taken (waited 0 min); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log line 880); proof-only at `0013`, nothing CHANGED (log line 931).
- (c) PASS 1 whole; every SKIPPED line is inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = the `@requires_live` decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (def at line 96, read from `<GATE>`).
- (c2) FORWARD: `dev forward: APPLIED 10:37:00` (log line 1090); the post-forward proof: `content UNCHANGED on every table` (log lines 1155, 1855); no `CHANGED` line other than line 931's `nothing CHANGED`.
- (c3) → `with-DB 4875/0`.
- (f) `cobalt_dev: 0013 — F2 = F0` (log line 1916; final FINGERPRINT `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`, log line 1913 = F0).
- THE RELEASE: `release-devdb-lock.sh` → `lock released` (log line 1918), `.env: removed` (line 1922); the log carries no time stamp for the release (it lies between `dev forward: APPLIED 10:37:00` and my `date` of 10:42:13). Verified by me: `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.
- (e) LIVE-NOTE, `.env` absent → `146 passed, 1 skipped` — the one skip is `test_replay_line.py:266` naming `COBALT_TEST_LIVE_DRC` (allowed); no skip names `COBALT_LIVE_VAULT_ROOT` → `live-note 146/0`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 4366bab8

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 35]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M .claude/settings.json`; ` M` ×6 and `??` ×14 under `docs/40 - DevDocs/` (this report among them); `?? .claude/settings.json.bak` (see `## DECISIONS` 1); no dirty `src/`, `tests/`, `ops/`, `configs/` path |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat 5facc838 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-desk-ops-fixes-1008` | 0 | — |
| PROBE | `git -C /Users/cobalt/cobalt tag -d scratch-allow-probe-desk-ops-fixes-1008` | 0 | `Deleted tag 'scratch-allow-probe-desk-ops-fixes-1008' (was 5facc838)` |
| PROBE | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` | 0 | `[main 54d1196d] scratch: allowlist probe (reverted next line)` |
| PROBE | `git -C /Users/cobalt/cobalt reset --soft HEAD~1` | 0 | — |
| PROBE | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `5facc838 docs(desk): RECUT desk-ops-fixes-1008 attempt 2` (HEAD back) |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-08-desk-ops-fixes-attempt2` | 1 | absent |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-desk-ops-fixes-1008` | 1 | absent (first launch) |

### STEP-D1 (production baseline, read-only)
- `date` → `Thu Oct  8 10:42:43 EDT 2026`.
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 10:42:44 EDT)`; every probe `OK` (database, sheet HTTP, sheet daymode, obsidian, mainframe, herdr, archiver, seat usage, backup `newest snapshot 13.0 h old across ssd`, vault blocks, redactions, radar `scanning (rth), members 50`); `com.cobalt.aset running pid 37788`, `com.cobalt.radar running running 1123 min, heartbeat fresh`, `com.cobalt.agent running pid 22243`; one `AMB com.cobalt.herdr unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) [launchd probe]; runs outside launchd by declared interim`. No RED; no carried-family line.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0: `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.` (no `docs/_inflight/` line).
- `<jobs0>` `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 15 label(s), exact match.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 13.0 h old` (ssd `local ARMED /Volumes/COBALT-BACKUP/restic`).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = `37788`; `launchctl print gui/501/com.cobalt.radar` → `state = running`, `<radar pid>` = `37799`; `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ??         0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → seven `cards.expire: falling back to the session close` INFO lines and `2026-10-08 10:41:47.936 | INFO     | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791470426404`; no traceback.
- LOG BASELINES: `<a0>` Started server process (aset.err) = `49` · `<ta0>` Traceback (aset.err) = `2` · `<tr0>` Traceback (radar.err) = `0` · `<tc0>` TaxonomyConfigError (radar.err) = `0` · `<rp0>` radar panel FAILED (aset.err) = `17` · `<rpr0>` radar pool refresh FAILED (aset.err) = `59` · `<re0>` radar S5 evaluate FAILED (radar.err) = `41` · `<lc0>` lifecycle card read failed (radar.err) = `39`.
- `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` → `200`.
- MARKERS again: `NOTIFY FAILED` → `0` · `session list unreadable` → `0` · `REPLACED:` → `0` (each = before).
- MIGRATIONS: none → no `<RB>`, no census read, no D1-M proof-only.

### STEP-D2
- D2.0 `git -C /Users/cobalt/cobalt add "docs/40 - DevDocs/reports/deploy-desk-ops-fixes-1008-attempt2.md"` → exit 0 · `git -C /Users/cobalt/cobalt commit -m "docs(report): deploy desk-ops-fixes-1008 — gate green on 4366bab8" …` → `[main 4b0aa106] docs(report): deploy desk-ops-fixes-1008 — gate green on 4366bab8` · `show --stat HEAD` → that one file (`161 insertions(+)`). `<pre-merge>` = `4b0aa106`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `c2bda2a4`; `rev-parse --short=8 c2bda2a4^2` → `4b0aa106` = `<pre-merge>`; `merge-base --is-ancestor 4366bab8 c2bda2a4` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 4366bab8 c2bda2a4 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs only).
- D2.4 `backup status` → `newest snapshot: 13.1 h old` · `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 5946.4 MB` · `ssd: snapshot 89f71689 — 9 new / 11 changed, 377.3 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `Thu Oct  8 10:44:28 EDT 2026` · heartbeat `HEARTBEAT GREEN … (2026-10-08 10:44:30 EDT)` (106 s after D1's — short of 110 s) · `date` → `Thu Oct  8 10:44:34 EDT 2026` · heartbeat `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 10:44:36 EDT)` = 112 s after D1's; no RED; aset pid 37788, radar `running 1125 min, heartbeat fresh`, agent pid 22243; the same herdr AMB line as `<hb0>`.
- D2.6 `date` → `Thu Oct  8 10:44:40 EDT 2026` · `git -C /Users/cobalt/cobalt tag pre-desk-ops-fixes-1008` → exit 0 (at `4b0aa106`).

### STEP-4 (empty `<restart set>`)
- 4.1 `date` → `Thu Oct  8 10:44:54 EDT 2026` = `<t down>` (no resident goes down).
- 4.2 nothing (set empty): no bootout, no `cobalt.sh stop`.
- 4.3 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `4b0aa106` = `<pre-merge>` · `git -C /Users/cobalt/cobalt merge --ff-only deploy/desk-ops-fixes-1008-attempt2` → `Updating 4b0aa106..c2bda2a4` / `Fast-forward` (10 files, 802 insertions, 61 deletions).
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, identical to `<val0>` (`13 trade_def(s) validated OK` … `Placement (docs/PLACEMENT.md): tree clean.`); `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`.
- 4.6 nothing (set empty). `<t up>` = `<t down>` = `Thu Oct  8 10:44:54 EDT 2026` (the set is empty; the hub's 4.3 `date`). Downtime: none.

## Smoke
- FIRST CALLS after `<t up>`: `<rp_up>` = `17` · `<rpr_up>` = `59` · `<re_up>` = `41` · `<lc_up>` = `39` (each = D1 baseline).
- (a) `date` → `Thu Oct  8 10:45:13 EDT 2026` · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 37788` (SAME pid as D1: outside the empty set — correct) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 37799` (SAME) · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (same) → GREEN.
- (b) `date` → `Thu Oct  8 10:45:16 EDT 2026` · `grep -c "Started server process" aset.err` → `49` = `<a0>` (aset outside the set — correct) · Traceback aset.err `2` = `<ta0>` · Traceback radar.err `0` = `<tr0>` · TaxonomyConfigError radar.err `0` = `<tc0>`.
- (c) same `date` · `curl … http://127.0.0.1:5010/` → `200` · `curl … /radar` → `200` · `curl … /radar\?frame=phone` → `200` → GREEN.
- (d) MARKERS, same `date`: `grep -c -F "NOTIFY FAILED" /Users/cobalt/cobalt/ops/desk/close-timer.sh` → `4` (after `4`) · `grep -c -F "session list unreadable" /Users/cobalt/cobalt/ops/desk/stop-guard.py` → `3` (after `3`) · `grep -c -F "REPLACED:" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` → `2` (after `2`) → GREEN.
- (s) THE SET'S SMOKE READS (the same three reads, same `date`): close-timer notify present → exit 0, `4` (≥1) GREEN · stop-guard fail-closed text present → exit 0, `3` (≥1) GREEN · install-ops replace line present → exit 0, `2` (≥1) GREEN. The tests behind them are the gate's (`offline 3991/0`, `tests/ops/` inside it); no test runs in production.
- (f) validate = 4.5 (exit 0, = `<val0>`) · `COBALT_ENV=production uv run cobalt jobs restarts 4b0aa106..c2bda2a4` → exit 0, the same ten rows as STEP-R, `RESTARTS: none` = `<restart set>`, no UNCLASSIFIED → GREEN.
- (g) no migration.
- (e) read 1: `date` → `Thu Oct  8 10:45:29 EDT 2026` · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 10:45:30 EDT)`; `com.cobalt.radar running running 1126 min, heartbeat fresh`; only the herdr AMB line already in `<hb0>`. The clock to the next reads was filled with `date` + heartbeat pairs only (10:45:45 → 10:47:54), every one `HEARTBEAT GREEN … nothing red`. Read 2: `date` → `Thu Oct  8 10:47:19 EDT 2026` · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 10:47:22 EDT)` = 112 s after read 1; `com.cobalt.radar running running 1128 min, heartbeat fresh`; no RED; herdr AMB as in `<hb0>` → GREEN.
- (b) radar tails (`<t up>` = 10:44:54): tail 1 `date` → `Thu Oct  8 10:46:25 EDT 2026` (+91 s) · `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` → last line `2026-10-08 10:44:49.387 | INFO     | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791470607971` (before `<t up>`; not settling), the rest `cards.expire: falling back to the session close` INFO lines. Tail 2 `date` → `Thu Oct  8 10:47:57 EDT 2026` (+183 s) · `tail -n 12 …/radar.err` → `2026-10-08 10:47:51.081 | INFO     | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791470789421` (after `<t up>`), the other eleven lines `cards.expire` INFO, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → GREEN (settled; tail 3 not needed).
- (h) REVERT-READBACK: `date` → `Thu Oct  8 10:48:01 EDT 2026` (`<t up>` + 187 s) · `radar panel FAILED` `17` = `<rp_up>` · `radar pool refresh FAILED` `59` = `<rpr_up>` · `radar S5 evaluate FAILED` `41` = `<re_up>` · `lifecycle card read failed` `39` = `<lc_up>` · Traceback radar.err `0` · `curl … /radar` → `200`. No census read (no migration) → GREEN.

THE CHAIN: every check committed (P2: `12cee324…`, clean, `held unfixed: 0`, `ready: YES`) → tips re-read (P3: `2413dbec`, `9aca7680`) → the merged tree (T: `4366bab8`, no migration, no plist) → RESTARTS derived (R: none) → three suites green on `4366bab8` (G: offline 3991/0 · with-DB 4875/0 · live-note 146/0) → `c2bda2a4` = `4366bab8` + docs (D2.3: nothing outside docs) → the landed code (4.3: `Updating 4b0aa106..c2bda2a4`, fast-forward) → markers (d: 4 / 3 / 2) → no migration (g) → residents up, unchanged pids (a) → radar cycling (b: 10:47:51; e: two GREEN reads 112 s apart) → the set's reads (s: GREEN) → no new failure (h: counts flat). The card surface is not readable here; the desk confirms it with him (L70).

### STEP-7 close
- `git -C /Users/cobalt/cobalt tag deploy-2026-10-08-desk-ops-fixes-attempt2` → exit 0 (after the green smoke, at `c2bda2a4`).
- `<pre-merge>` `4b0aa106` → `<stack-final>` `c2bda2a4` · tags `pre-desk-ops-fixes-1008` (at `4b0aa106`), `deploy-2026-10-08-desk-ops-fixes-attempt2` (at `c2bda2a4`) · `<t down>` / `<t up>` `none` (empty set; both stamped 10:44:54), 0 s · uv sync: none on production (the gate worktree's first `uv run` created its own `.venv`: `Installed 253 packages in 789ms`) · proof cost: none (no migration) · `migrations applied: none` · `<RB>` none · snapshot `89f71689` (ssd) · `RESTARTS done: none`.
- THE ROLLBACK STRING: 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 c2bda2a4` — no resident to take down or bring up (restart set empty). 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.
- PRE-STOP SELF-CHECK: (1) every smoke row above is quoted verbatim with its `date`. (2) `git -C /Users/cobalt/cobalt merge-base --is-ancestor 2413dbec c2bda2a4` → exit 0; `… 9aca7680 c2bda2a4` → exit 0; `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `c2bda2a4`. (3) REVERT-READBACK (h) shown above; every count, sha and `file:line` in this report was read from tool output this run. (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), and D2.1 too; no conflict marker exists.
- THE RELEASE: the gate released the lock (log line 1918 `lock released`); `ls -la <GATE>/.env` → No such file at close.
- `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 0eb1fd25-3168-4787-bc89-b0474d95ef06` → `context 208828 of 400000 — ok`.

## CONTINUE
OUTAGE STARTING Thu Oct  8 10:44:40 EDT 2026 — residents of <restart set> = none going down (empty set: no resident goes down; the merge lands with residents up); if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
next: none — the run ended green (stop line below). Residents were never down.

## DECISIONS
1. ASK DESK: `git status --porcelain` on `main` shows `?? .claude/settings.json.bak`, a path neither in D0's ACCEPTED list nor in its REFUSED classes (`src/`, `tests/`, `ops/`, `configs/`, staged). Default taken: go on — it is untracked, not staged, outside every code path, and neither the merge nor any commit of this run touches it. [Thu Oct  8 10:42:43 EDT 2026]

## RECORDS
- Downtime: none (empty restart set; no resident went down).
- `REFUSED, not needed` lines: none. Messages not followed: none received.
- `cobalt_dev: 0013 (F2 = F0)` — gate log line 1916; `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`.
- RETIRE OWED: none (no plist removed).
- Carried RED: none read — `<hb0>` and every later heartbeat `nothing red`; the only non-OK line is `AMB com.cobalt.herdr … runs outside launchd by declared interim`, unchanged throughout.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-desk-ops-fixes-1008-attempt2` and branch `deploy/desk-ops-fixes-1008-attempt2`; the set's branch `ops/desk-ops-fixes-1008` and its build worktree; the gate log `/Users/cobalt/cobalt-wt/.gate-logs/deploy-desk-ops-fixes-1008-attempt2-all-20261008-101359.log` (desk's call).
- Push is his, through the desk (L55): `main` is local at `c2bda2a4` plus this report commit.
- Card `## RECORDS` (the desk's, copied):
  - desk-ops-fixes: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-ops-fixes-check-2026-10-08.md` last line: CHECK DONE · job: desk-ops-fixes · pass: 1 · tip: 2413dbec · house A: Sol FINDINGS: 6 · findings: 11 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 6 · house B: Grok FINDINGS: 0 · suites: offline 3991/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 20 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 101004
  - desk-ops-fixes: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/desk-ops-fixes-1008` → `9aca7680`; code tip `2413dbec`
  - written by deploy-card.sh at 2026-10-08 09:37 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one block (the `Claude-Session:` trailer request) recorded under `## L74`, not acted on.

DEPLOYED deploy-2026-10-08-desk-ops-fixes-attempt2 c2bda2a4 | set: none | migrations: none | gate: offline 3991/0 · with-DB 4875/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 208828
