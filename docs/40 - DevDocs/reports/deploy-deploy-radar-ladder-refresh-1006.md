# deploy-radar-ladder-refresh-1006 · SET: none · MIGRATIONS: none

## §0 Headline
(in progress)

## L74
none so far.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/60-deploy-ladder-refresh-card.md"` at Tue Oct  6 18:40:28 EDT 2026 → exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/60-deploy-ladder-refresh-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/60-deploy-ladder-refresh-card.md" · 0 · bb9c010cae1521879b53cc4efc8f39c47752b3e4
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/60-deploy-ladder-refresh-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-06 R556 row · grep -n "^| R556 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 110:| R556 | 14:20 ET | HIS RULING ([words](cto-2026-10-06-words.md) `## R556`): fix the empty radar screen if the brain says GO (bandwidth, no blocker); desk asked the brain 14:20; on GO the desk launches the fix flow, no further ask to him. | HIS RULING · APPROVED |
RULING 2026-10-06 R556 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R556 |" -- "docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 8bceed0a20d4157786a85a2f0e44a76a1ff2bf30
RULING 2026-10-06 R556 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · the row as grepped
AUTHORIZED
```

First launch: `ls -la` of this report → `No such file or directory` (exit 1).

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (## AUTHORIZATION) |
| P1 DATE | `date` | 0 | `Tue Oct  6 18:40:28 EDT 2026` (no window binds, L43) |
| P2 tail | `tail -n 3 ".../radar-ladder-refresh-check-2026-10-06.md"` | 0 | `CHECK DONE · job: radar-ladder-refresh · pass: 1 · tip: ed19060f · … · held unfixed: 0 · open: 0 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 181164` — both literals present, `tip: ed19060f` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "<check report>"` | 0 | `02b15e1f07a9f44bb7885b680db0f3e91abc5fda` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "<check report>"` | 0 | (nothing) |
| P3 code tip | `rev-parse --short=8 ed19060f` | 0 | `ed19060f` |
| P3 head | `rev-parse --short=8 ops/radar-ladder-refresh-1006` | 0 | `ed19060f` (= TIP) |
| P3 ancestor | `merge-base --is-ancestor ed19060f ed19060f` | 0 | — |
| P3 diff | `diff --stat ed19060f ed19060f -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` (no session holds the lock) |
| P5 status | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-radar-ladder-refresh-1006` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `e177280b` = `<m0>` |
| P5 ancestor | `merge-base --is-ancestor e177280b main` | 0 | — |
| P5 empty | `log --oneline main..deploy/deploy-radar-ladder-refresh-1006` | 0 | (empty) |
| P6 marker 1 | `grep -c -F "tickLadder" .../radar_panel.py` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "window.setInterval(tickLadder,interval)" ...` | 1 | `0` = before |
| P6 marker 3 | `grep -c -F "window.setInterval(refreshPool,interval)" ...` | 0 | `1` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main ed19060f -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 83925` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 83936` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit ed19060f` → `Merge made by the 'ort' strategy.` (4 files, 483 insertions, 2 deletions; no conflict).
- `git -C <GATE> rev-parse --short=8 HEAD` → `46a587c9` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent e177280b..deploy/deploy-radar-ladder-refresh-1006` → `46a587c9 Merge commit 'ed19060f' into deploy/deploy-radar-ladder-refresh-1006` (one line, one head).
- `merge-base --is-ancestor ed19060f deploy/deploy-radar-ladder-refresh-1006` → exit 0.
- `diff --stat e177280b deploy/deploy-radar-ladder-refresh-1006 -- src/cobalt/db_migrations` → (nothing): no migration path, MIGRATIONS: none.
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat e177280b deploy/deploy-radar-ladder-refresh-1006 -- configs ops` → (nothing): no plist added, modified or removed; no RETIRE OWED.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after a first-run `uv` venv build in the gate: `Installed 253 packages in 815ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-ladder-refresh-build-2026-10-06.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar` (matches the card).

## L68 GATE
THE EQUAL-TREE CLAUSE holds: ONE branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat ed19060f 46a587c9 -- . ":(exclude)docs"` → (nothing); the check's stop line carries `with-DB 4847/0` (> 0). The check's suite lines are the gate's; (a)–(f) skipped, no `cobalt_dev` lock taken by this run. Quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-ladder-refresh-check-2026-10-06.md` lines 191–208 (its `gate.sh radar-ladder-refresh-1006 all --deploy` on tip `ed19060f`, exit 0):
```
offline 3963/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4847/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-ladder-refresh-1006-all-20261006-180724.log
```
Skips read against the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262` — each in the set; `test_replay_line.py` skip names `COBALT_TEST_LIVE_DRC` — in the set; `test_s3_c4_experiments.py:95` — read in `<GATE>`: line 95 `@requires_live`, line 96 `def test_x14_live_his_template_strips_to_the_committed_fixture():` — in the set. None outside.
`cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed. `cobalt_dev: 0013 — F2 = F0` (the check's gate).

GATE GREEN on 46a587c9 (Tue Oct  6 18:41:50 EDT 2026) — offline 3963/0 · with-DB 4847/0 · live-note 146/0

## Deploy table
### STEP-D0
- `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 222]`; `status --porcelain` → only ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` under `docs/40 - DevDocs/`, plus `?? .claude/settings.json.bak` (see ## DECISIONS 1); no staged line, no dirty `src/` `tests/` `ops/` `configs/` path other than `rules.yaml`.
- `git -C /Users/cobalt/cobalt diff --stat e177280b main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing).
- ALLOWLIST PROBE: `tag scratch-allow-probe-deploy-radar-ladder-refresh-1006` → ok; `tag -d …` → `Deleted tag 'scratch-allow-probe-deploy-radar-ladder-refresh-1006' (was e177280b)`; `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 474dc9a6] scratch: allowlist probe (reverted next line)`; `reset --soft HEAD~1` → ok; `log --oneline -1` → `e177280b docs(desk): card 54 deploy preflight ready YES, deploy launching; R581` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-06-radar-ladder-refresh` → exit 1; `… refs/tags/pre-deploy-radar-ladder-refresh-1006` → exit 1.

### STEP-D1 baseline (Tue Oct  6 18:42:24 EDT 2026)
- `<hb0>` (`heartbeat show`, 18:42:25 EDT): `HEARTBEAT RED — 1 job(s)`. Every probe OK (database, sheet HTTP 200, sheet daymode, radar `scanning (aftermarket), members 50`, `com.cobalt.aset running loaded, pid 83925`, `com.cobalt.agent running pid 22243`, `com.cobalt.radar running running 277 min, heartbeat fresh`, …) except `AMB com.cobalt.herdr unmanaged` (declared interim) and `RED com.cobalt.generated failed GeneratedCommitRefused: \`git commit -m\` failed (exit 1): pre-commit: a deploy hub is live — no desk commit on main until its stop line: 9f093747 deploy-hub-deploy-p2-1005 …`. Not an aset / sheet / radar probe: named, not a stop (## RECORDS).
- `<val0>` (`validate`): exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 4.6 h old` (ssd local ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = `83925`; `…/com.cobalt.radar` → `state = running`, `<radar pid>` = `83936`; `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 logs/radar.err` → last line `2026-10-06 18:41:20.480 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791326392928`; no traceback.
- Log baselines: `<a0>` = 46 · `<ta0>` = 2 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 17 · `<rpr0>` = 58 · `<re0>` = 40 · `<lc0>` = 39.
- `curl … /radar` → `200`. MARKERS again → `0` / `0` / `1` (each its before).
- No migration: `<RB>`, census and D1-M not run.

## Smoke

## CONTINUE
next: STEP-D2 (D0, D1 green; gate green at 18:41:50 EDT)

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` is untracked on `main` (present at session start). D0's ACCEPTED list does not name it and its REFUSED classes (staged; dirty `src/` `tests/` `ops/` `configs/`) do not cover it. Safe default taken: not a refusal, the run goes on; the file is not touched. [18:42 EDT]

## RECORDS

(run in progress — next step under ## CONTINUE)
