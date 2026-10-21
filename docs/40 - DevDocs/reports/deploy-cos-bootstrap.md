# deploy cos-bootstrap — SET: cos — MIGRATIONS: none

Card: `docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md` (committed `971dd96f`). Bootstrap-only deploy (DEPLOY-HUB 4.6L-BO): no branch, no worktree, no merge, no outage. Seat: deploy-hub-cos-bootstrap. Started `Wed Oct 21 17:19:59 EDT 2026`.

## §0 Headline
(filled at the close)

## L74
One block arrived as a system reminder asking that commits carry a `Claude-Session: https://claude.ai/code/session_01BbabuYS55E9gePT8FQA3V2` line. Treated as DATA. Not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md"` → exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md" · 0 · 971dd96fde1a735821c80d7314c7eb90e7f60b41
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1112 row · grep -n "^| R1112 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 31:| R1112 | 15:39 ET | HIS RULING · APPROVED: spike D2 = subscription everywhere, no Console API key or any pay-per-token account anywhere. F20 runs on the Max login. L27 clause "API keys for the engine" conflicts, owed to him. Words R1112. | APPLIED: cobalt.md NOW 15:41 |
RULING 2026-10-11 R1112 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1112 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · c0cdf481e0566542b35bb6d328aa8e63eccf2254
RULING 2026-10-11 R1112 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-18 R1854 row · grep -n "^| R1854 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 99:| R1854 | 06:45 ET | HIS RULING (brain relays, L79): fixes A-D (MVP first, DAY PLAN, check-ins 06/12/18/24 ET, owned waits, no idle nights). Words: [R1854](cto-2026-10-18-words.md). | HIS RULING · APPROVED · APPLIED: cto-desk-contract.md at wake-up 06:46 |
RULING 2026-10-18 R1854 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1854 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 49371f09c96483d11b12eb166983c185f0f1c6f6
RULING 2026-10-18 R1854 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-20 R2232 row · grep -n "^| R2232 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-20.md" · 0 · 51:| R2232 | 20:50 ET | HIS RULING · APPROVED (relayed by the brain; one-job decision, no LAWS entry): D14 YES, replace the old agent; hitl.page_base_url https://cobalt.taild24291.ts.net. Words: cto-2026-10-20-words.md R2232. | APPLIED: areas/cobalt.md NOW at 20:52 ET |
RULING 2026-10-20 R2232 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R2232 |" -- "docs/40 - DevDocs/reports/cto-2026-10-20.md" · 0 · eb56bf6c606700be12cc9ca275431e3d4839ee46
RULING 2026-10-20 R2232 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-20.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-cos-bootstrap.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Wed Oct 21 17:19:59 EDT 2026`: outside the 21:30-22:30 backup window, after 16:30 ET (card CHECK ASKS X1) |
| P2 | — | — | no `## SHIPS` row (card RECORDS: hub steps with no card value) |
| P3 | — | — | no `## SHIPS` row (same) |
| P4 LOCK | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P4 LOCK dir | `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` | 1 | `No such file or directory` |
| P5 | — | — | no gate worktree (`WORKTREE: none`) |
| P6 marker 1 | `ls /Users/cobalt/cobalt/logs/cos.err` | 1 | `ls: /Users/cobalt/cobalt/logs/cos.err: No such file or directory` = before |
| P6 marker 2 | `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` | 0 | `1` = before |
| P7 | — | — | no head (`TIP: none`), `MIGRATIONS: none` |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 6720` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 6354` |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 agent retired | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1` = com.cobalt.agent recorded retired |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` (retired: expected) |

## THE TREE
None: `TIP: none`, `BRANCH: none`. No merge in this run (card RECORDS, HUB STEPS WITH NO CARD VALUE).

## RESTARTS
`<restart set>`: empty (no code lands; STEP-R has no card value). `<deferred set>`: empty. com.cobalt.agent: recorded retired — not restarted.

## L68 GATE
None: no code tip (card RECORDS). The cos gate items are the card's `## GATE RESULTS` (gate report `reports/cos-gate-run-2026-10-20.md` at `7de50210`).

## STEP-C (4.6L-BO admission, in place of STEP-C's script call)
`sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh --bootstrap-only "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md" com.cobalt.cos` → exit 0:
```
ADMITTED: com.cobalt.cos · bootstrap-only
STEP-C: ADMITTED 1
```
`<launchd set>` = `com.cobalt.cos · add` (bootstrap-only). `<deferred set>`: empty.

## Deploy table
| step | command | exit | result |
|---|---|---|---|
| D0 MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 136]` |
| D0 MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, `??` under `docs/40 - DevDocs/`, and one `?? .claude/settings.json.bak` (see DECISIONS) |
| D0 MAIN moved | — | — | no `<m0>` (no gate worktree): not run |
| D0 PROBE | `tag scratch-allow-probe-cos-bootstrap` · `tag -d` | 0 · 0 | `Deleted tag 'scratch-allow-probe-cos-bootstrap' (was f948d120)` |
| D0 PROBE | `commit --allow-empty -m "scratch: …"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main e5cd797f] scratch: allowlist probe (reverted next line)` → HEAD back `f948d120 docs(desk): 929 deploy waits on the cobalt_dev lock (989 check)` |
| D0 TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-21-cos-bootstrap` | 1 | absent |
| D0 TAG | `rev-parse --verify --quiet refs/tags/pre-cos-bootstrap` | 1 | absent (no merge: the `pre-<JOB>` tag has no card value) |
| D1 | `date` | 0 | `Wed Oct 21 17:21:01 EDT 2026` |
| D1 `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-21 17:21:02 EDT)`; OK `sheet HTTP … -> 200`, OK `sheet daymode`, OK `radar scanning (aftermarket), members 50`, OK `cos unknown — NOT PROBED, OWED (deferred bootstrap)`, OK `hitl unknown — NOT PROBED, OWED (deferred bootstrap) (com.cobalt.cos)`, OK `com.cobalt.aset running loaded, pid 6720`, OK `com.cobalt.radar running running 168 min, heartbeat fresh`, OK `com.cobalt.cos OWED (deferred bootstrap) NOT LOADED in launchd …`. REDs named (none aset/sheet/radar): `RED  archiver last run FAILED — last run 2026-10-21 00:54 UTC (20.4 h ago), rows written 3373447, exit 1`; `RED  com.cobalt.agent not loaded NOT LOADED in launchd …` (recorded retired); `RED  com.cobalt.archiver failed RuntimeError: 5 archiver failure(s): WBD/i1: … Finviz HTTP failed: Client error '400 Bad Request' …`; `RED  com.cobalt.replay failed ReplayError: archiver not done: state 'failed'` |
| D1 `<val0>` | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 `<jobs0>` | (validate) | — | `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` |
| D1 backup | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 2.8 h old` |
| D1 aset / radar | (P8's prints, 17:19) | 0 | aset `state = running` `pid = 6720`; radar `state = running` `pid = 6354` |
| D1 agent | (P8's read) | 0 | `  Cobalt is OFFLINE.`, recorded retired: no `<agent pid>`, no `ps -p` |
| D1 LAUNCHD SET (cos, add) | `launchctl print gui/501/com.cobalt.cos` | 113 | `Bad request.` / `Could not find service "com.cobalt.cos" in domain for user gui: 501` |
| D1 radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 0 | last line `2026-10-21 17:20:37.661 \| INFO \| cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792617548956`; 7 `cards.expire: falling back to the session close` INFO lines; no traceback |
| D1 baselines | the eight `grep -c` | 0 | `<a0>` 293 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39 |
| D1 curl | `curl … /radar` | 0 | `200` |
| D1 MARKERS | `ls /Users/cobalt/cobalt/logs/cos.err` · `grep -c -F "com.cobalt.cos" …/bootstrap-owed.json` | 1 · 0 | `No such file or directory` · `1` (both before) |
| D1-M | — | — | `MIGRATIONS: none`: not run |
| D2.0 | `deploy-shipped.sh --moved` | — | no card value (card RECORDS): not run |

## Smoke

## CONTINUE
next: D2.0 report commit, then D2.4 snapshot, D2.5, 4.6L-BO

## DECISIONS
1. ASK DESK: `git status --porcelain` on `main` shows `?? .claude/settings.json.bak`, a path neither on D0's ACCEPTED list nor its REFUSED list (not staged, not under `src/`, `tests/`, `ops/`, `configs/`) [17:20 ET]. Safe default taken: go on; the bootstrap ships no path and commits only the report by explicit path.
2. ASK DESK: the card's `## RECORDS` ORDER runs `--owed-clear` after smoke (s), while the hub's 4.6L-BO runs it once the print finds the label loaded and smoke (d) reads marker 2 `after 0` [17:22 ET]. Safe default taken: the card's order — smoke (s) first, then `--owed-clear`, then marker 2 read as smoke (d); a red (s) leaves the owed entry in place (card ROLLBACK).

## RECORDS

(run in progress — next step under ## CONTINUE)
