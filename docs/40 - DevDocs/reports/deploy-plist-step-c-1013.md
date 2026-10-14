# deploy plist-step-c-1013 — set: radar · migrations: none

## §0 Headline
Deploy of `ops/plist-step-c-1013` (code tip `c1fc230d`, head `6b2dabd5`) onto `main`. Started 2026-10-13 21:36 ET. AUTHORIZED, STEP-0 green.

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

## Smoke

## CONTINUE
next: STEP-D2 (gate green at 22:08:22 EDT; D0 and D1 done)

## DECISIONS
1. ASK DESK: `main` has `?? .claude/settings.json.bak`, an untracked path outside D0's accepted list but in no refused class (not staged, not under `src/`, `tests/`, `ops/` or `configs/`). Is it accepted? [22:08 ET] Safe default taken: not a refusal; the deploy went on, and the file was left untouched.
2. ASK DESK: L68 says a set that changes `DEPLOY-HUB.md` or `gate.sh` first runs the gate on the merged hub text before that deploy. This set changes `DEPLOY-HUB.md` (the `:13` line, per `hub-text-preflight-2026-10-13.md` row 16) and does not change `gate.sh`. This run is on the INSTALLED hub at `main`, and its gate ran `gate.sh` whole on the merged tree. [22:08 ET] Safe default taken: STEP-G on `<m1>`, which carries the merged hub text, is that gate run. The new hub text governs the NEXT deploy, not this one.

## RECORDS

(run in progress — next step under ## CONTINUE)
