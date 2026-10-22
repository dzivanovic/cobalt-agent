# deploy cos-bootstrap-2 · set: cos · migrations: none

Card: `docs/40 - DevDocs/prompts/2026-10-21/1004-deploy-cos-bootstrap-2-card.md` (committed `5afae482`). A bootstrap-only deploy (4.6L-BO): no merge, no outage, no gate worktree.

## §0 Headline
(filled at the end)

## L74
(filled at the end)

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1004-deploy-cos-bootstrap-2-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1004-deploy-cos-bootstrap-2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/1004-deploy-cos-bootstrap-2-card.md" · 0 · 5afae48278a17fde330087c49b64093125e88e20
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/1004-deploy-cos-bootstrap-2-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la` of this report → `No such file or directory` (exit 1).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Wed Oct 21 20:34:58 EDT 2026` — outside 21:30-22:30 |
| P2 | — | — | no `## SHIPS` row: no card value (card `## RECORDS`, HUB STEPS WITH NO CARD VALUE) |
| P3 | — | — | no code tip: no card value |
| P4 LOCK | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no session holds the lock |
| P5 | — | — | `WORKTREE: none`: no card value |
| P6 marker 1 | `ls /Users/cobalt/cobalt/data/cos/scratch` | 1 | `ls: /Users/cobalt/cobalt/data/cos/scratch: No such file or directory` = before |
| P6 marker 2 | `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` | 0 | `1` = before |
| P7 | — | — | `MIGRATIONS: none`, no head: no card value |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 6720` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 31938` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` |
| P8 retired | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1` — `com.cobalt.agent recorded retired`; OFFLINE is the expected read |

### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 173]`; no staged line; every dirty line ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, plus `?? .claude/settings.json.bak` (untracked, not under `src/` `tests/` `ops/` `configs/`: not a refused line; recorded) |
| MAIN moved | `diff --stat <m0> main` | — | no `<m0>` (no gate worktree): no card value |
| PROBE tag | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-cos-bootstrap-2` | 0 | (no output) |
| PROBE tag -d | `git -C /Users/cobalt/cobalt tag -d scratch-allow-probe-cos-bootstrap-2` | 0 | `Deleted tag 'scratch-allow-probe-cos-bootstrap-2' (was f244b5a6)` |
| PROBE commit | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` | 0 | `[main 5c3d4f97] scratch: allowlist probe (reverted next line)` |
| PROBE reset | `git -C /Users/cobalt/cobalt reset --soft HEAD~1` | 0 | (no output) |
| PROBE log | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `f244b5a6 docs(desk): STATE 20:24` — HEAD back |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-21-cos-bootstrap-2` | 1 | free |
| TAG pre | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-cos-bootstrap-2` | 1 | free |

### STEP-D1 — baseline
| read | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | `Wed Oct 21 20:35:35 EDT 2026` |
| `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | `HEARTBEAT RED — 2 job(s)  (2026-10-21 20:35:36 EDT)`; `OK   sheet HTTP               http://127.0.0.1:5010/ -> 200`; `OK   radar                    paused (market_reset)`; `OK   com.cobalt.aset              running   loaded, pid 6720 [launchd probe]`; `OK   com.cobalt.radar             running   running 24 min, heartbeat fresh`; `OK   com.cobalt.cos               OWED (deferred bootstrap) NOT LOADED in launchd …`; `OK   cos                      unknown — NOT PROBED, OWED (deferred bootstrap)`; `OK   hitl                     unknown — NOT PROBED, OWED (deferred bootstrap) (com.cobalt.cos)`. The two REDs, named, neither the aset / sheet nor the radar probe: `RED  com.cobalt.agent             not loaded NOT LOADED in launchd …` (recorded retired) and `RED  com.cobalt.replay            failed    ReplayError: archiver not done: state 'failed'` |
| `<val0>` | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.` |
| `<jobs0>` | (same output) | 0 | `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 22 label(s), exact match.` |
| backup | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 0.4 h old` |
| aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `pid = 6720` |
| radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `pid = 31938` |
| agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` (recorded retired; no `ps -p`) |
| radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 0 | last: `2026-10-21 20:34:54.681 \| INFO     \| cobalt.radar.runner:resident:638 - radar cycle: paused_market_reset scan_id=None` (8 such lines, 100 s apart, no traceback) |
| `<a0>` | `grep -c "Started server process" /Users/cobalt/cobalt/logs/aset.err` | 0 | `293` |
| `<ta0>` | `grep -c "Traceback" /Users/cobalt/cobalt/logs/aset.err` | 0 | `217` |
| `<tr0>` | `grep -c "Traceback" /Users/cobalt/cobalt/logs/radar.err` | 1 | `0` |
| `<tc0>` | `grep -c "TaxonomyConfigError" /Users/cobalt/cobalt/logs/radar.err` | 1 | `0` |
| `<rp0>` | `grep -c "radar panel FAILED" /Users/cobalt/cobalt/logs/aset.err` | 0 | `18` |
| `<rpr0>` | `grep -c "radar pool refresh FAILED" /Users/cobalt/cobalt/logs/aset.err` | 0 | `60` |
| `<re0>` | `grep -c "radar S5 evaluate FAILED" /Users/cobalt/cobalt/logs/radar.err` | 0 | `80` |
| `<lc0>` | `grep -c "lifecycle card read failed" /Users/cobalt/cobalt/logs/radar.err` | 0 | `39` |
| curl | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | 0 | `200` |
| marker 1 | `ls /Users/cobalt/cobalt/data/cos/scratch` | 1 | `No such file or directory` = before |
| marker 2 | `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` | 0 | `1` = before |
| LAUNCHD SET (cos · add) | `launchctl print gui/501/com.cobalt.cos` | 113 | `Could not find service "com.cobalt.cos" in domain for user gui: 501` |
| cos.err | `ls -la /Users/cobalt/cobalt/logs/cos.err` | 0 | `-rw-r--r--  1 cobalt  staff  3040 Oct 21 17:23 /Users/cobalt/cobalt/logs/cos.err` |
| cos.err Traceback | `grep -c -F "Traceback" /Users/cobalt/cobalt/logs/cos.err` | 0 | `2` |
| cos.err DbConfigError | `grep -c -F "DbConfigError: Missing Postgres settings" /Users/cobalt/cobalt/logs/cos.err` | 0 | `2` |
| migration | — | — | `MIGRATIONS: none`: no `<RB>`, no D1-M |

## THE TREE
No merge: `TIP: none`, `BRANCH: none`. STEP-T has no card value.

## STEP-C (bootstrap-only, 4.6L-BO)
`sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh --bootstrap-only "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1004-deploy-cos-bootstrap-2-card.md" com.cobalt.cos` · exit 0:
```
ADMITTED: com.cobalt.cos · bootstrap-only
STEP-C: ADMITTED 1
```
`<launchd set>` = `com.cobalt.cos · add` (bootstrap-only). `launchctl print gui/501/com.cobalt.cos` → exit 113, `Could not find service "com.cobalt.cos" in domain for user gui: 501`.

## RESTARTS
`<restart set>`: EMPTY — nothing merges; STEP-R has no card value. `<deferred set>`: empty. `<launchd set>`: `com.cobalt.cos · add (bootstrap-only)`. com.cobalt.agent: recorded retired — not restarted.

## L68 GATE
No gate: no code merges (STEP-G has no card value). The cos gate items are the card's `## GATE RESULTS` (gate report `reports/cos-gate-run-2026-10-20.md` at `7de50210`), admitted by `--bootstrap-only` above.

## Deploy table

## Smoke

## CONTINUE
next: STEP-D2 (D2.0 report commit)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
