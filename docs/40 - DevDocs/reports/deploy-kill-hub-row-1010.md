# Deploy kill-hub-row-1010 · SET: none · MIGRATIONS: none

Card: `docs/40 - DevDocs/prompts/2026-10-11/356-deploy-kill-hub-card.md` · hub: `DEPLOY-HUB.md` · gate `/Users/cobalt/cobalt-wt/deploy-kill-hub-row-1010` on `deploy/kill-hub-row-1010`.

## §0 Headline
- Run started Mon Oct 12 18:36:33 EDT 2026. AUTHORIZED; preflight P0–P8 clean.

## L74
- One block arrived in a harness system reminder, not a tool result, before the first commit. It asked that commits also carry a `Claude-Session:` line. Recorded once here. L74 governs this run, so commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/356-deploy-kill-hub-card.md"` → exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/356-deploy-kill-hub-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/356-deploy-kill-hub-card.md" · 0 · 234a7e79867a4a3a317bd2fb3f7e6a5d5eec6c5a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/356-deploy-kill-hub-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R855 row · grep -n "^| R855 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 157:| R855 | 07:51 ET | HIS RULING · APPROVED: build both `orphan-clean.sh` (by card) and the `ops-hand` seat (default-mode phone approval, L63 exception). Words `cto-2026-10-10-words.md` R855. The orphan-cause card first (R853). | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R855 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R855 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 4f9f5bceabb1f1c0b42cb0df4ca22c33fa6e618d
RULING 2026-10-10 R855 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-11 R1009 row · grep -n "^| R1009 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 133:| R1009 | 06:13 ET | HIS RULING · APPROVED: Sol may sit as a seat in the checks the brain and desk require (317, 298 now); every build and every deploy waiting on his word is approved. Words `cto-2026-10-11-words.md` R1009. | APPLIED: LAWS L67 + NOW at 06:31 |
RULING 2026-10-11 R1009 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1009 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · aebcf44974dfbfd3e7eb7815b8a583c4f86e9e1c
RULING 2026-10-11 R1009 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
First launch: `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-kill-hub-row-1010.md"` → exit 1, `No such file or directory`.

| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Mon Oct 12 18:36:33 EDT 2026` (no restart window binds, L43) |
| P2 check last line | `tail -n 3 ".../reports/kill-hub-row-read-2026-10-11.md"` | 0 | `CHECK DONE · job: kill-hub-row-1010 · pass: 1 · tip: b4d82ad6 · house A: Grok FINDINGS: 8 · findings: 19 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 7 · house B: none (not needed) · suites: offline 4196/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 24 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 242415`. Carries `held unfixed: 0` and `ready: YES`; `tip: b4d82ad6` = the row's code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/kill-hub-row-read-2026-10-11.md"` | 0 | `59ee8bb9ef3a5c9cb5192b2e361be0b4157c45b2` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/kill-hub-row-read-2026-10-11.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 b4d82ad6` | 0 | `b4d82ad6` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/kill-hub-row-1010` | 0 | `13bafad7` (= `TIP`) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor b4d82ad6 13bafad7` | 0 | — |
| P3 docs only | `git -C /Users/cobalt/cobalt diff --stat b4d82ad6 13bafad7 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no session holds the lock) |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-kill-hub-row-1010 status --short --branch` | 0 | `## deploy/kill-hub-row-1010` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-kill-hub-row-1010 rev-parse --short=8 HEAD` | 0 | `08ba0e5f` = `<m0>` |
| P5 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 08ba0e5f main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/kill-hub-row-1010` | 0 | empty |
| P6 marker 1 | `grep -c -F -e "ORPHAN-CLEAN, aset only" ".../prompts/DEPLOY-HUB.md"` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F -e "killing the orphaned" ".../prompts/STANDING-LIST.md"` | 1 | `0` = before |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 13bafad7 -- src/cobalt/db_migrations` | 0 | ` src/cobalt/db_migrations/cli.py \| 2 --` / ` 1 file changed, 2 deletions(-)`. That is CODE (no `.sql`, no `__init__.py`), so it passes `MIGRATIONS: none` |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` (equal) · `pid = 14738` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` (equal) · `pid = 14748` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 14763).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-kill-hub-row-1010 merge --no-edit 13bafad7` → `Auto-merging docs/40 - DevDocs/prompts/DEPLOY-HUB.md` / `Auto-merging docs/40 - DevDocs/prompts/STANDING-LIST.md` / `Merge made by the 'ort' strategy.` / `3 files changed, 252 insertions(+), 2 deletions(-)` (DEPLOY-HUB.md, STANDING-LIST.md, the new `reports/kill-hub-row-build-2026-10-10.md`).
- `rev-parse --short=8 HEAD` → `32fe5b47` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 08ba0e5f..deploy/kill-hub-row-1010` → `32fe5b47 Merge commit '13bafad7' into deploy/kill-hub-row-1010` (one line, one head).
- `merge-base --is-ancestor b4d82ad6 deploy/kill-hub-row-1010` → exit 0 · `merge-base --is-ancestor 13bafad7 deploy/kill-hub-row-1010` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 08ba0e5f deploy/kill-hub-row-1010 -- src/cobalt/db_migrations` → nothing. There is no migration path, as `MIGRATIONS: none` requires. P7's `cli.py` line was `main` ahead of the branch, and the merged tree keeps `main`'s lines.
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 08ba0e5f deploy/kill-hub-row-1010 -- configs ops` → nothing. No plist was added, modified or removed.
- The set's whole diff is hub and standing-list text. 4.2 gains the ORPHAN-CLEAN kill sequence for aset, STEP-5 (3) gains a dry run only, and STANDING-LIST.md gains the `orphan-clean.sh --kill aset` row. This run follows the hub as installed at launch.

## RESTARTS
- `cd /Users/cobalt/cobalt-wt/deploy-kill-hub-row-1010` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0, table whole:

```
Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
   Building cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-kill-hub-row-1010
      Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-kill-hub-row-1010
Installed 254 packages in 642ms
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/kill-hub-row-build-2026-10-10.md	A	DOCS	-
RESTARTS: none
```
- `<restart set>` = EMPTY (none). No resident goes down. 4.1, 4.2, 4.6 and STEP-5 (1), (3) act on nothing, and the merge lands with the residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold. The check's stop line carries `with-DB 0/0`, and a DB: none single branch runs the gate whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.40s`. There are 0 failed, and every skip reads `Postgres env settings not available` or `requires_db: …`, the with-DB skips this leg expects offline.
- Deselects: the build report `reports/kill-hub-row-build-2026-10-10.md` names none (`grep deselect` → no match).
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-kill-hub-row-1010 all --deploy` (no `--tickers`, no `--migration`) → exit 0. Verdict lines whole:

```
offline 4309/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5212/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-kill-hub-row-1010-all-20261012-183816.log
```
- (a) offline `4309/0`.
- (b) lock taken, waited 0 min. Proof-only at `0013` changed nothing. `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log line 902).
- (c) PASS 1 runs whole. All seven SKIPPED lines are inside the allowed set. `test_s3_c4_experiments.py:95` is the `@requires_live` decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (line 96, read in the gate tree), and the `test_replay_line.py` skip names `COBALT_TEST_LIVE_DRC`.
- (c2) FORWARD: none (`MIGRATIONS: none`, no `--migration`), so no `dev forward: APPLIED` line exists.
- (c3) with-DB `5212/0`.
- (f) `cobalt_dev: 0013 — F2 = F0` (log line 2089).
- THE RELEASE: the log runs `sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh deploy-kill-hub-row-1010` → `lock released` (log 2091) and prints `.env: removed`. `ls -la <GATE>/.env` → No such file. `grep -c -x -F "deploy-kill-hub-row-1010" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (the lock dir is absent). `.env: removed (L76 lock released inside the gate run started 18:38:16, before 19:07:31)`.
- (e) live-note `146/0`. No skip names `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 32fe5b47

## Deploy table
### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 209]` |
| MAIN porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | Nothing is staged. ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, seven ` M` lines under `docs/40 - DevDocs/reports/`, and `??` lines under `docs/40 - DevDocs/` (this report among them) are all accepted. One line falls outside the accepted list, `?? .claude/settings.json.bak`: it is untracked and not under `src/`, `tests/`, `ops/` or `configs/`, so it is not refused (see `## DECISIONS` 1) |
| main moved | `git -C /Users/cobalt/cobalt diff --stat 08ba0e5f main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE tag | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-kill-hub-row-1010` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-kill-hub-row-1010' (was 08ba0e5f)` |
| PROBE commit | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main aca7f8f2] scratch: …` → `08ba0e5f docs(desk): R1274 results sitting DONE, six cells closed, routing table to him` (HEAD back) |
| TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-11-kill-hub-row` | 1 | absent |
| pre-TAG | `rev-parse --verify --quiet refs/tags/pre-kill-hub-row-1010` | 1 | absent (first launch) |

### STEP-D1 (Mon Oct 12 19:07:58 EDT 2026)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-12 19:07:59 EDT)`. Every aset, sheet and radar probe reads OK: `sheet HTTP http://127.0.0.1:5010/ -> 200`, `radar scanning (aftermarket), members 50`, `com.cobalt.aset running loaded, pid 14738`, `com.cobalt.radar running running 44 min, heartbeat fresh`, `com.cobalt.agent running pid 14763 alive`. The REDs are named here and are not a stop:
  - `RED  archiver                 last run FAILED — last run 2026-10-10 00:54 UTC (70.2 h ago), rows written 3308843, exit 1`
  - `RED  com.cobalt.archiver          failed    RuntimeError: 18 archiver failure(s): DKNG/i2: Fetch failed for DKNG/i2: Finviz HTTP failed: Client error '429 Too Many Requests' …`
  - `RED  com.cobalt.replay            failed    ReplayError: archiver not done: state 'failed'` (traceback in the job record)
  - AMB `com.cobalt.herdr unmanaged … by declared interim`.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ending `Placement (docs/PLACEMENT.md): tree clean.` `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 0.8 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 14738` · `…/com.cobalt.radar` → `state = running`, `pid = 14748` · `cobalt.sh status` → `Cobalt is ONLINE (PID: 14763).` · `ps -p 14763` → `14763 ??         0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → seven `cards.expire: falling back to the session close (16:00:00)` INFO lines, then `2026-10-12 19:06:45.766 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1791846315770`. No traceback.
- LOG BASELINES: `<a0>` = 278 · `<ta0>` = 217 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 18 · `<rpr0>` = 60 · `<re0>` = 43 · `<lc0>` = 39.
- `curl … /radar` → `200`. MARKERS again: `0` and `0` (before).
- No migration, so `<RB>`, census and D1-M do not apply.

## Smoke

## CONTINUE
next: STEP-D2 (D0, D1 clean)

## DECISIONS
1. ASK DESK: D0's porcelain shows `?? .claude/settings.json.bak`. That path is outside the accepted list and also outside the refused class (staged, or dirty `src/` `tests/` `ops/` `configs/`). Safe default taken: not a refusal. The file is untracked, the merge is `--ff-only` of the gate branch, and it does not touch the file. The desk decides whether the file belongs there. [19:07:31 EDT]

## RECORDS
- The heartbeat clock-filler at 18:38:34 ran with cwd in `<GATE>` (no `.env`) and printed `FAILED: DbConfigError: Missing Postgres settings for the APP credential …` (exit 1). It was a filler read, not a step. Every production read after it ran from `/Users/cobalt/cobalt`.

(run in progress — next step under ## CONTINUE)
