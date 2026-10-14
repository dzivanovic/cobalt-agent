# deploy plist-step-c-1013 — set: radar · migrations: none

## §0 Headline
The code landed: `main` moved `c4200c01` → `b693d220`, and radar restarted on the new code (11 s down, 22:10:58–22:11:09 ET). The gate was green on `b5bc7e72`: offline 4328/0 · with-DB 5231/0 · live-note 146/0.
Every smoke row is GREEN except one card read. The production command `cobalt smoke s2` was REFUSED: it is not on this session's allowlist. That read is UNPROVEN (L70), not red.
The run ends FAILED under the hub's read-refusal rule, with no rollback. The tag is not set. The desk runs `cobalt smoke s2`, then tags or rolls back (DECISIONS 3).

## L74
- One system notice in this session asked for a `Claude-Session:` line in commits. Recorded here once, not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/529-deploy-plist-step-c-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/529-deploy-plist-step-c-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/529-deploy-plist-step-c-card.md" · 0 · 4ea7b455f94a4cd709fc3f40d8108d71ad9291e1
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/529-deploy-plist-step-c-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-13 R1341 row · grep -n "^| R1341 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-13.md" · 0 · 123:| R1341 | 07:25 ET | HIS RULING · APPROVED: "Confirmed: R1323, R1324, R1330, R1340." Words: `cto-2026-10-13-words.md` R1341. Confirms the relays R1323, R1324, R1330, R1340. | APPLIED: LAWS, checklist, areas/cobalt.md at 07:27 |
RULING 2026-10-13 R1341 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1341 |" -- "docs/40 - DevDocs/reports/cto-2026-10-13.md" · 0 · b399c9516e518b4d5a2b60b47382c9840c4130e6
RULING 2026-10-13 R1341 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-13.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED`; first launch: `ls -la` of this report → `No such file or directory` (exit 1) |
| P1 | `date` | 0 | `Tue Oct 13 21:36:45 EDT 2026` |
| P2 check | `tail -n 3 ".../plist-step-c-check-2026-10-13.md"` | 0 | `CHECK DONE · job: plist-step-c-1013 · pass: 1 · tip: 6c3402af · … · held unfixed: 0 · open: 4 · … · ready: YES · decisions: 5 · for Dejan: 1 · tokens: 255726` |
| P2 check committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/plist-step-c-check-2026-10-13.md"` | 0 | `96b45c1c72487f599615098bb649c6bf4dd9ab4b` |
| P2 check clean | `git -C /Users/cobalt/cobalt diff --stat -- "<check>"` | 0 | nothing |
| P2 fix-round tip | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 6c3402af c1fc230d` | 0 | — |
| P2 fix report | `git -C /Users/cobalt/cobalt show "6b2dabd5:docs/40 - DevDocs/reports/plist-step-c-build-2026-10-13.md"` last line | 0 | `BUILT · job: plist-step-c-1013 · tip: c1fc230d | on 5214e50b | migration: none | offline 4328/0 | with-DB 5231/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 14 of 14 | self-check: 3 of 3 | decisions: 6 · for Dejan: 0 · tokens: 179297` |
| P2 fix report committed | `git -C /Users/cobalt/cobalt log -1 --format=%H 6b2dabd5 -- "<fix report>"` | 0 | `6b2dabd5be75d4ce6be9727bac50aa79416ff7a8` (on the branch; not in the `main` tree, so `diff --stat` on main prints nothing) |
| P2 held ids | — | — | `held unfixed: 0`: no FIXED / CARRIED line is needed |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 c1fc230d` | 0 | `c1fc230d` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/plist-step-c-1013` | 0 | `6b2dabd5` = TIP |
| P3 ancestry | `git -C /Users/cobalt/cobalt merge-base --is-ancestor c1fc230d 6b2dabd5` | 0 | — |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat c1fc230d 6b2dabd5 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-plist-step-c-1013 status --short --branch` | 0 | `## deploy/plist-step-c-1013` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `53d8fe17` = `<m0>` |
| P5 m0 in main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 53d8fe17 main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/plist-step-c-1013` | 0 | empty |
| P6 marker 1 | `ls /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh` | 1 | `No such file or directory` = before |
| P6 marker 2 | `grep -c -F "bootstrap-owed.json" /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh` | 2 | `No such file or directory` = before |
| P6 marker 3 | `grep -c -F "bootstrap-owed.json" /Users/cobalt/cobalt/src/cobalt/smoke/checks.py` | 1 | `0` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 6b2dabd5 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 40377` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 22724` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 14763).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-plist-step-c-1013 merge --no-edit 6b2dabd5` → `Merge made by the 'ort' strategy.` (15 files changed, 1819 insertions(+), 19 deletions(-); no conflict)
- `git -C <GATE> rev-parse --short=8 HEAD` → `b5bc7e72` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 53d8fe17..deploy/plist-step-c-1013` → `b5bc7e72 Merge commit '6b2dabd5' into deploy/plist-step-c-1013` (one line, one head)
- `merge-base --is-ancestor c1fc230d deploy/plist-step-c-1013` → exit 0 · `merge-base --is-ancestor 6b2dabd5 deploy/plist-step-c-1013` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 53d8fe17 deploy/plist-step-c-1013 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 53d8fe17 deploy/plist-step-c-1013 -- configs ops` → whole:
```
 configs/cobalt/smoke/s2.yaml |   3 +-
 ops/desk/deploy-step-c.sh    | 325 +++++++++++++++++++++++++++++++++++++++++++
 ops/desk/desk-launch.sh      |  89 ++++++++++++
 3 files changed, 416 insertions(+), 1 deletion(-)
```
  No plist was added, modified or removed. STEP-C is clean.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0, whole (after uv's venv creation lines: `Creating virtual environment at: .venv`, `Installed 254 packages in 841ms`):
```
path	change	rule	restart
configs/cobalt/smoke/s2.yaml	M	operator command (cobalt smoke); no job reads	-
docs/40 - DevDocs/cobalt/jobs/watchdog.md	M	DOCS	-
docs/40 - DevDocs/cobalt/smoke/checks.md	M	DOCS	-
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/plist-step-c-build-2026-10-13.md	A	DOCS	-
ops/desk/deploy-step-c.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
src/cobalt/jobs/watchdog.py	M	static import reach	com.cobalt.radar
src/cobalt/smoke/checks.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_jobs.py	M	test/documentation; no resident	-
tests/cobalt/test_smoke.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step_c.py	A	test/documentation; no resident	-
tests/ops/test_desk_launch_launchd.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.radar`.

## L68 GATE
EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat c1fc230d b5bc7e72 -- . ":(exclude)docs"` → `configs/cobalt/rules.yaml | 2 +-`, `tests/ops/test_the_rule_sweep.py | 3 ---` (`main` moved since the build's base). The trees are not equal, so the gate runs whole (`--deploy`). The build report names no `--deselect`; TICKERS none; no migration.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 16.92s` (0 failed; every skip is a with-DB test: `Postgres env settings not available` / `requires_db: needs cobalt_dev`).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-plist-step-c-1013 all --deploy` started in the background at about 21:45 ET → exit 0. Verdict lines, whole:
```
offline 4328/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5231/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-plist-step-c-1013-all-20261013-213854.log
```
- (a) `offline 4328/0` · (c) PASS 1: the seven SKIPPED lines above are pass 1's. Each is in the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip whose reason names `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95`, the skip of `test_x14_live_his_template_strips_to_the_committed_fixture` (`def` at `:96` per Grep). (c2) `dev forward: APPLIED 22:03:19` (log `:1118`; no migration above `0013` in the set, nothing CHANGED). (c3) PASS 2: `with-DB 5231/0` · (f) `cobalt_dev: 0013 — F2 = F0` (log `:902` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`) · (e) `live-note 146/0`.
- THE RELEASE: `.env: removed (L76 lock released, log :2093 "lock released")`. `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-plist-step-c-1013" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (no lock dir).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on b5bc7e72 — offline 4328/0 · with-DB 5231/0 · live-note 146/0 (22:08 ET)

## Deploy table
STEP-D0:
- `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 3]`. `status --porcelain`: ` M .claude/settings.json`; ` M` and `??` under `docs/40 - DevDocs/` only; plus `?? .claude/settings.json.bak` (outside both lists: DECISIONS 1). No staged line. No dirty `src/`, `tests/`, `ops/` or `configs/` path.
- `git -C /Users/cobalt/cobalt diff --stat 53d8fe17 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing
- ALLOWLIST PROBE: `tag scratch-allow-probe-plist-step-c-1013` → ok; `tag -d` → `Deleted tag 'scratch-allow-probe-plist-step-c-1013' (was 53d8fe17)`; `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 0048f23f] …`; `reset --soft HEAD~1` → ok; `log --oneline -1` → `53d8fe17 docs(desk): section 5 state, 365 check done` (HEAD back)
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-13-plist-step-c` → exit 1; `refs/tags/pre-plist-step-c-1013` → exit 1

STEP-D1 (baseline, 22:08:48 EDT):
- `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-13 22:08:49 EDT)`; `OK   radar                    idle (overnight)`; `OK   com.cobalt.radar             running   running 1341 min, heartbeat fresh`; `OK   com.cobalt.aset              running   loaded, pid 40377 [launchd probe]`; `AMB  com.cobalt.herdr             unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0)` (named, not a stop)
- `<val0>`: `cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 0.5 h old` (ssd ARMED)
- aset `state = running`, `<aset pid>` = 40377 · radar `state = running`, `<radar pid>` = 22724 · `Cobalt is ONLINE (PID: 14763).` · `ps -p 14763` → `14763 ??         0:00.03 uv run src/cobalt_agent/main.py`
- `tail -n 8 radar.err` → last `2026-10-13 22:08:22.078 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (a cycle every ~100 s, no traceback)
- LOG BASELINES: `<a0>` 279 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39
- `curl … /radar` → `200` · MARKERS again → `No such file or directory` · `No such file or directory` · `0` (all before)
- MIGRATIONS: none, so no `<RB>`, no census and no D1-M

STEP-D2:
- D2.0 `commit … -- "docs/40 - DevDocs/reports/deploy-plist-step-c-1013.md"` → `[main c4200c01] docs(report): deploy plist-step-c-1013 — gate green on b5bc7e72`; `show --stat HEAD` → that one file (151 insertions). `rev-parse --short=8 main` → `c4200c01` = `<pre-merge>`
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only)
- D2.2 `<stack-final>` = `b693d220`; `b693d220^2` → `c4200c01` = `<pre-merge>`; `merge-base --is-ancestor b5bc7e72 b693d220` → exit 0
- D2.3 `diff --stat b5bc7e72 b693d220 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs only)
- D2.4 `backup status` → `newest snapshot: 0.5 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 7554.5 MB`, `ssd: snapshot 939fabea — 0 new / 2 changed, 30.9 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`
- D2.5 reads at 22:10:31, 22:10:37 (102 s and 108 s after D1's 22:08:49, both under 110 s, so both were repeated) and 22:10:42 (113 s) → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-13 22:10:42 EDT)`; radar `running 1343 min, heartbeat fresh`. No new RED.
- D2.6 `date` → `Tue Oct 13 22:10:46 EDT 2026`; `tag pre-plist-step-c-1013` → at `c4200c01`

STEP-4 (restart set: `com.cobalt.radar`):
- 4.1 `<t down>` = `Tue Oct 13 22:10:58 EDT 2026`
- 4.2 `launchctl bootout gui/501/com.cobalt.radar` → no output; `launchctl print gui/501/com.cobalt.radar` → exit 113, `Could not find service "com.cobalt.radar" in domain for user gui: 501`. aset and agent are not in the set, so there was no orphan-clean and no `cobalt.sh stop`.
- 4.3 `rev-parse --short=8 HEAD` → `c4200c01` = `<pre-merge>`; `merge --ff-only deploy/plist-step-c-1013` → `Updating c4200c01..b693d220` / `Fast-forward` (15 files, 1819 insertions(+), 19 deletions(-))
- 4.4 `migrations applied: none` (MIGRATIONS: none)
- 4.5 `cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`
- 4.6 `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` → no output; `launchctl print` → `state = running`, `pid = 8646` (≠ 22724); `<t up>` = `Tue Oct 13 22:11:09 EDT 2026`. Downtime: 11 s.

SUMMARY: `<pre-merge>` `c4200c01` → `<stack-final>` `b693d220` · rollback tag `pre-plist-step-c-1013` at `c4200c01` · `TAG` `deploy-2026-10-13-plist-step-c` NOT set (smoke (s) unproven, DECISIONS 3) · `<t down>` 22:10:58 / `<t up>` 22:11:09 / 11 s · uv sync: none at production (the gate worktree's venv creation at STEP-R is outside production) · proof cost: none (no migration) · `migrations applied: none` · `<RB>`: none · snapshot `939fabea` (ssd) · `RESTARTS done: com.cobalt.radar`
THE ROLLBACK STRING (the desk's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 b693d220` — ONE revert of the main-into-gate merge; `com.cobalt.radar` down first, up after.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
- FIRST CALLS after `<t up>`: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (each = D1)
- (a) 22:11:20: aset `state = running`, `pid = 40377` (SAME as D1; outside the set); radar `state = running`, `pid = 8646` (NEW; in the set); `Cobalt is ONLINE (PID: 14763).` (same; outside the set). GREEN
- (b) `Started server process` 279 = `<a0>` (aset outside the set) · aset Traceback 217 = `<ta0>` · radar Traceback 0 = `<tr0>` · TaxonomyConfigError 0 = `<tc0>` · `tail -n 30 aset.err` → the last lines are the 11:02:39 INTC fill-update write; no new start and no traceback. Radar tails: below.
- (c) `/` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200`. GREEN
- (d) MARKERS: `ls …/deploy-step-c.sh` → `/Users/cobalt/cobalt/ops/desk/deploy-step-c.sh` · `grep -c -F "bootstrap-owed.json" …/deploy-step-c.sh` → `3` · `grep -c -F "bootstrap-owed.json" …/checks.py` → `1`. All three are at their after values. GREEN
- (e) read 1 at 22:12:06 → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-13 22:12:07 EDT)`, `OK   com.cobalt.radar             running   running 1 min, heartbeat fresh`
- (f) `cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = 4.5 · `jobs restarts c4200c01..b693d220` → exit 0, `RESTARTS: com.cobalt.radar` = STEP-R, no `UNCLASSIFIED`. GREEN
- (g) no migration
- (s) 22:11:37 `COBALT_ENV=production uv run cobalt smoke s2` → REFUSED, verbatim: `Permission to use Bash has been denied because Claude Code is running in don't ask mode.` The string is not on this session's launch allowlist. Not retried. UNPROVEN (L70). · `launchctl print gui/501/com.cobalt.radar` → `state = running` (`pid = 8646`). GREEN
- (b) radar tails: 22:12:39 (`<t up>` + 90 s) → last line `2026-10-13 22:11:09.075 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (the same second as `<t up>`, so not settled). 22:12:59 → adds `2026-10-13 22:12:49.098 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`, a cycle stamped after `<t up>` with no `radar S5 evaluate FAILED`, no `lifecycle card read failed` and no traceback: SETTLED GREEN. 22:14:10 (+ 181 s) → the same two cycle lines; still clean.
- (e) read 2 at 22:13:56 (111 s after read 1's 22:12:07) → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-13 22:13:58 EDT)`, `OK   com.cobalt.radar             running   running 3 min, heartbeat fresh`. No new RED. GREEN
- (h) REVERT-READBACK at 22:14:10 (`<t up>` + 181 s): `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39, each = `<…_up>` (none growing) · `/radar` → `200`. No census read (no migration). GREEN

THE CHAIN: every check committed (P2: check `96b45c1c`, fix report `6b2dabd5`) → tips re-read (P3: `c1fc230d`, `6b2dabd5`) → merged tree (T: `<m1>` `b5bc7e72`) → RESTARTS derived (R: `com.cobalt.radar`) → three suites green on `<m1>` (G: offline 4328/0 · with-DB 5231/0 · live-note 146/0) → `<stack-final>` `b693d220` = `<m1>` + docs (D2.3) → landed code (4.3: `c4200c01..b693d220`) → markers at their after values (d) → no migration (g) → radar up on a new pid after the merge, aset and agent unchanged (a) → radar cycling (b, e) → the set's reads: `launchctl print` radar GREEN; `cobalt smoke s2` REFUSED, UNPROVEN (s) → no growing failure count (h). The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK:
1. Every smoke row's evidence is quoted verbatim above, with its `date` (22:11:20, 22:11:37, 22:12:06, 22:12:39, 22:12:59, 22:13:56, 22:14:10). The (s) refusal is quoted verbatim.
2. Every code tip and head was re-read (P3), and each is an ancestor of `<stack-final>`: `merge-base --is-ancestor c1fc230d b693d220` → exit 0; `merge-base --is-ancestor 6b2dabd5 b693d220` → exit 0. `rev-parse --short=8 HEAD` on main → `b693d220`.
3. REVERT-READBACK is shown as (h) (no rollback ran). Every count, sha and `file:line` in this report was read from tool output this run.
4. No conflict marker exists: STEP-T and D2.1 were both `Merge made by the 'ort' strategy.`, and 4.3 was a fast-forward.

## CONTINUE
next: STEP-D2 (gate green at 22:08:22 EDT; D0 and D1 done)
OUTAGE STARTING 22:10:46 EDT — residents of com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
OUTAGE ENDED 22:11:09 EDT — radar up (pid 8646). Smoke done at 22:14:10; the run stopped at 4.7 (s), the refused read. next: the desk's (DECISIONS 3). No resume of this hub.

## DECISIONS
1. ASK DESK: `main` has `?? .claude/settings.json.bak`, an untracked path outside D0's accepted list but in no refused class (not staged, not under `src/`, `tests/`, `ops/` or `configs/`). Is it accepted? [22:08 ET] Safe default taken: not a refusal; the deploy went on, and the file was left untouched.
2. ASK DESK: L68 says a set that changes `DEPLOY-HUB.md` or `gate.sh` first runs the gate on the merged hub text before that deploy. This set changes `DEPLOY-HUB.md` (the `:13` line, per `hub-text-preflight-2026-10-13.md` row 16) and does not change `gate.sh`. This run is on the INSTALLED hub at `main`, and its gate ran `gate.sh` whole on the merged tree. [22:08 ET] Safe default taken: STEP-G on `<m1>`, which carries the merged hub text, is that gate run. The new hub text governs the NEXT deploy, not this one.
3. ASK DESK: at 4.7 (s), the card's smoke read `COBALT_ENV=production uv run cobalt smoke s2` was REFUSED: the launch allowlist carries no `cobalt smoke` string. The refusal came after 4.6, outside the outage, with the merge landed and radar up. [22:11 ET] Safe default taken: the hub's read-refusal rule (`A refusal of a read → FAILED: <step> — <read> refused — <message>`). The run ends FAILED, without STEP-5. A command denial is UNPROVEN and not a defect (L70), so it is not an `(s) read failing` RED. Every other smoke row is GREEN. Rolling back on a permission gap would take radar down a second time with no defect read. NOT taken: the `TAG`, because it is set only after a green smoke. FOR THE DESK: (i) run `COBALT_ENV=production uv run cobalt smoke s2` and read K18 PASS with no `OWED` line; if it is green, set `deploy-2026-10-13-plist-step-c` at `b693d220`; if it is red, use the ROLLBACK STRING in `## Deploy table`. (ii) Either add the card's smoke-read strings to the deploy launch list (through STANDING-LIST; a string change returns to him per R60) or keep `## SMOKE READS` to strings already on the line. Not FOR DEJAN unless the desk takes route (ii) through a STANDING-LIST string change.

## RECORDS
- Downtime: radar down 22:10:58 → up 22:11:09 EDT, 11 s (under 300 s).
- REFUSED: `COBALT_ENV=production uv run cobalt smoke s2` (the card's `## SMOKE READS` line 1, at 4.7 (s), after 4.6) — `Permission to use Bash has been denied because Claude Code is running in don't ask mode.` Not retried in any spelling.
- `cobalt_dev: 0013 (F2 = F0)` — the gate's log `:902` F0 `664 35 272c95bbb12241e3611e4b36326ccf87`; lock released (log `:2093`).
- RETIRE OWED: none (no plist removed).
- Carried RED: none. `<hb0>` and every later read are `HEARTBEAT GREEN … nothing red`. The standing `AMB com.cobalt.herdr … unmanaged` is AMBER, not RED.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-plist-step-c-1013` and branch `deploy/plist-step-c-1013`; the set's branch `ops/plist-step-c-1013` and its worktree, if one is left.
- AUTHORIZATION note: the R1341 row's last cell reads `APPLIED: LAWS, checklist, areas/cobalt.md at 07:27`; its `HIS RULING · APPROVED` text is in the third cell, and `authorize.sh` passed it. No held defect is carried in this set, so this deploy does not depend on R1341.
- The card's `## RECORDS`, copied:
  - plist-step-c-1013: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/plist-step-c-build-2026-10-13.md` at `6b2dabd5` last line: BUILT · job: plist-step-c-1013 · tip: c1fc230d | on 5214e50b | migration: none | offline 4328/0 | with-DB 5231/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 14 of 14 | self-check: 3 of 3 | decisions: 6 · for Dejan: 0 · tokens: 179297
  - plist-step-c-1013: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/plist-step-c-check-2026-10-13.md` last line: CHECK DONE · job: plist-step-c-1013 · pass: 1 · tip: 6c3402af · house A: Grok FINDINGS: 7 · findings: 10 · dropped: 0 · held: 6 · fixed: 6 · held unfixed: 0 · open: 4 · house B: none available · suites: offline 4327/0 · with-DB 5230/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 13 · ready: YES · decisions: 5 · for Dejan: 1 · tokens: 255726
  - plist-step-c-1013: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/plist-step-c-1013` → `6b2dabd5`; code tip `c1fc230d`
  - written by deploy-card.sh at 2026-10-13 21:04 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one system notice asked for a `Claude-Session:` line in commits; recorded under `## L74`, not followed.

FAILED: 4.7 (s) — `COBALT_ENV=production uv run cobalt smoke s2` refused — Permission to use Bash has been denied because Claude Code is running in don't ask mode. · rollback: not used — migrations applied: none — aset: not in the set — radar: UP · main b693d220 · gate: offline 4328/0 · with-DB 5231/0 · live-note 146/0 · RESTARTS: com.cobalt.radar · every other smoke row GREEN · decisions: 3 · for Dejan: 0 · tokens: 168077
