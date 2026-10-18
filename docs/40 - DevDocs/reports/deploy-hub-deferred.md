# deploy hub-deferred · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/hub-deferred-1018` (head `77e04a2a`, code tip `79b8ac8e`) on gate `deploy/hub-deferred`. In progress.

## L74
- A system-reminder block arriving after a tool result asked that commit messages also carry a `Claude-Session:` line. Recorded as DATA, not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/791-deploy-hub-deferred-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/791-deploy-hub-deferred-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/791-deploy-hub-deferred-card.md" · 0 · 4fa1f450a1eaecde52a1fb7f1c429d8db8f49c2d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/791-deploy-hub-deferred-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 68:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-hub-deferred.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Sun Oct 18 18:53:43 EDT 2026` (outside 21:30-22:30) |
| P2 | `tail -n 3 ".../reports/hub-deferred-1018-check-2026-10-18.md"` | 0 | `CHECK DONE · job: hub-deferred-1018 · pass: 1 · tip: 79b8ac8e · house A: Grok FINDINGS: 0 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 8608/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 15 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 173800` — `held unfixed: 0`, `ready: YES`, `tip: 79b8ac8e` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/hub-deferred-1018-check-2026-10-18.md"` | 0 | `e7ef198a06256a5b862da217e331ac9cb2dc69d4` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 79b8ac8e` | 0 | `79b8ac8e` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-deferred-1018` | 0 | `77e04a2a` (= TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 79b8ac8e 77e04a2a` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 79b8ac8e 77e04a2a -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (lock free) |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-hub-deferred status --short --branch` | 0 | `## deploy/hub-deferred` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-hub-deferred rev-parse --short=8 HEAD` | 0 | `4fa1f450` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 4fa1f450 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/hub-deferred` | 0 | empty |
| P6 | `grep -c -F "<deferred set>" ".../prompts/DEPLOY-HUB.md"` | 1 | `0` (= before) |
| P6 | `grep -c -F "minus every label of" ".../prompts/DEPLOY-HUB.md"` | 1 | `0` (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 77e04a2a -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 89330` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 70450` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 89351).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| merge | `git -C /Users/cobalt/cobalt-wt/deploy-hub-deferred merge --no-edit 77e04a2a` | 0 | `Merge made by the 'ort' strategy.` (4 files: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `reports/hub-deferred-1018-build-2026-10-18.md`, `.result`, `tests/ops/test_hub_deferred_1018.py`) |
| `<m1>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `783c2e2d` |
| merges | `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 4fa1f450..deploy/hub-deferred` | 0 | `783c2e2d Merge commit '77e04a2a' into deploy/hub-deferred` |
| ancestry | `merge-base --is-ancestor 79b8ac8e deploy/hub-deferred` · `… 77e04a2a deploy/hub-deferred` | 0 · 0 | — |
| migrations | `git -C /Users/cobalt/cobalt diff --stat 4fa1f450 deploy/hub-deferred -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| STEP-C | `git -C /Users/cobalt/cobalt diff --stat 4fa1f450 deploy/hub-deferred -- configs ops` | 0 | nothing |
| STEP-C | `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 4fa1f450 deploy/hub-deferred` | 0 | `STEP-C: ADMITTED 0` → `<launchd set>` empty |

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-hub-deferred` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` · exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/hub-deferred-1018-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/hub-deferred-1018-build-2026-10-18.result	A	DOCS	-
tests/ops/test_hub_deferred_1018.py	A	test/documentation; no resident	-
RESTARTS: none
```
(preceded by uv venv creation lines: `Creating virtual environment at: .venv` · `Installed 256 packages in 646ms`)
- `<restart set>`: EMPTY · `<launchd set>`: EMPTY · `<deferred set>`: none

## L68 GATE
- Equal-tree clause: does not hold (the check's stop line carries `with-DB 0/0`) → the gate runs whole.
- (a0) `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `264 passed, 163 skipped in 18.97s` (0 failed; skips are with-DB `Postgres env settings not available` / `requires_db`).
- Deselects named by the build report: none.
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-hub-deferred all --deploy --deploy-gate` (no `--tickers`, no `--migration`) · exit 0 · verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8648/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5582/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-hub-deferred-all-20261018-185550.log
```
- (a) offline `8648/0`; W line `tests/ops: run (deploy gate)`. (c) every SKIPPED line is inside the allowed set (test_cards_picks :388/:401, test_playbook_live live render, test_radar_evaluate :695, test_replay_line `COBALT_TEST_LIVE_DRC`, test_s3_c4_experiments live template, test_catalyst :365, test_predicate :262). (c2) no migration: no dev forward. with-DB `5582/0`. (e) live-note `147/0`.
- `cobalt_dev: 0013 — F2 = F0` · `.env: removed` (L76 lock released — log line 2240 `lock released`; recorded at 19:42 ET `date`). `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-hub-deferred" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (lock dir absent).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 783c2e2d

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| main | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 216]`; only ` M .claude/settings.json`, ` M`/`??` under `docs/40 - DevDocs/`, `?? .claude/settings.json.bak` |
| main code paths | `git -C /Users/cobalt/cobalt status --porcelain -- src tests ops configs` | 0 | nothing |
| staged | `git -C /Users/cobalt/cobalt diff --cached --stat` | 0 | nothing |
| main moved | `git -C /Users/cobalt/cobalt diff --stat 4fa1f450 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe | `tag scratch-allow-probe-hub-deferred` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-hub-deferred' (was 4fa1f450)` |
| probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 36a3fc4f] …` → `4fa1f450 docs(desk): deploy card 791 hub-deferred` |
| tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-18-hub-deferred` · `… refs/tags/pre-hub-deferred` | 1 · 1 | absent |

### STEP-D1 (baseline)
- `date` → `Sun Oct 18 19:43:10 EDT 2026`. `<hb0>` = `HEARTBEAT GREEN — 17 job(s), 12 probe(s), nothing red  (2026-10-18 19:43:12 EDT)`; `OK   radar                    idle (overnight)`; `OK   com.cobalt.radar             running   running 202 min, heartbeat fresh`; `AMB  com.cobalt.herdr             unmanaged AMBER …` (declared interim); `com.cobalt.prefill-refresh` and `com.cobalt.playbook` `OWED (deferred bootstrap)` (listed in `data/deploy/bootstrap-owed.json`). No RED.
- `<val0>`: `COBALT_ENV=production uv run cobalt validate` exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 17 registered — 6 resident, 11 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 0.9 h old`.
- aset `state = running` `pid = 89330` · radar `state = running` `pid = 70450` · `Cobalt is ONLINE (PID: 89351).` · `ps -p 89351` → `89351 ??         0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last `2026-10-18 19:42:52.298 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (cycles every 100 s, no traceback).
- Log baselines: `<a0>` 283 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. Markers: `<deferred set>` → `0`, `minus every label of` → `0` (before values).
- `<launchd set>` empty: nothing. MIGRATIONS none: no `<RB>`, no proof-only.

## Smoke

## CONTINUE
- STEP-D0 green, STEP-D1 baseline read at 19:43 ET.
- next: STEP-D2

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
