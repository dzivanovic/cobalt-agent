# deploy-hub-text-1005 · set: workflow2 · migrations: none

## §0 Headline
(filled at close)

## L74
- A system-reminder of this session asked commits to end with a `Claude-Session: https://claude.ai/code/session_012Yaryci5UQrbLUGYUxwJxN` line. Recorded as DATA (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/41-deploy-hub-text-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/41-deploy-hub-text-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/41-deploy-hub-text-card.md" · 0 · f502c2df54b79915a423555a2822d7e8c2b20c91
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/41-deploy-hub-text-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "<REPORT>"` | 1 | No such file or directory |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct  5 15:48:04 EDT 2026` — trading day, outside (i)–(iv); `window: (v) provisional` (MIGRATIONS: none) |
| P2 | `tail -n 3 "…/hub-text-check-2026-10-05.md"` | 0 | `CHECK DONE · job: hub-text · pass: 1 · tip: 6b939b00 · … · held unfixed: 0 · open: 0 · … · RESTARTS: none · files opened: 9 · ready: YES · decisions: 1 · for Dejan: 0` — `held unfixed: 0`, `ready: YES`, tip = row |
| P2 | `git log -1 --format=%H -- "docs/…/hub-text-check-2026-10-05.md"` | 0 | `fb339571c6d6ba47b856ad115406ab67c2563c63` |
| P2 | `git diff --stat -- "docs/…/hub-text-check-2026-10-05.md"` | 0 | nothing |
| P3 | `git rev-parse --short=8 6b939b00` | 0 | `6b939b00` |
| P3 | `git rev-parse --short=8 ops/hub-text-1005` | 0 | `2abb7d99` (= row, = TIP) |
| P3 | `git merge-base --is-ancestor 6b939b00 2abb7d99` | 0 | — |
| P3 | `git diff --stat 6b939b00 2abb7d99 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-hub-text-1005` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `f502c2df` |
| P5 | `git merge-base --is-ancestor f502c2df main` | 0 | — |
| P5 | `git log --oneline main..deploy/deploy-hub-text-1005` | 0 | empty |
| P6 | marker 1 `No restart window binds a deploy (L43, his R389)` DEPLOY-HUB | 0 | `0` (before 0) |
| P6 | marker 2 `each feature deploys alone on its existing check (his R390)` DEPLOY-HUB | 0 | `0` (before 0) |
| P6 | marker 3 `first runs the gate on the merged hub text` DEPLOY-HUB | 0 | `0` (before 0) |
| P6 | marker 4 `(L75, his R376)` CHECK-HUB | 0 | `0` (before 0) |
| P6 | marker 5 `desk-context.sh <your session id>` BUILD-HUB | 0 | `0` (before 0) |
| P6 | marker 6 `(d2)` DEPLOY-HUB | 0 | `2` (before 2) |
| P7 | `git diff --stat main 2abb7d99 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 13209` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 28249` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| merge head 1 | `git -C <GATE> merge --no-edit 2abb7d99` | 0 | `Merge made by the 'ort' strategy.` — 4 files (BUILD-HUB.md, CHECK-HUB.md, DEPLOY-HUB.md, reports/hub-text-build-2026-10-05.md), 220 insertions, 17 deletions |
| `<m1>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `3ffaa1fd` |
| merges | `git log --oneline --merges --first-parent f502c2df..deploy/deploy-hub-text-1005` | 0 | `3ffaa1fd Merge commit '2abb7d99' into deploy/deploy-hub-text-1005` |
| code tip in | `git merge-base --is-ancestor 6b939b00 deploy/deploy-hub-text-1005` | 0 | — |
| head in | `git merge-base --is-ancestor 2abb7d99 deploy/deploy-hub-text-1005` | 0 | — |
| migrations | `git diff --stat f502c2df deploy/deploy-hub-text-1005 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| STEP-C | `git diff --stat f502c2df deploy/deploy-hub-text-1005 -- configs ops` | 0 | nothing — no plist added, changed or removed |

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created `.venv` in the gate: `Installed 253 packages in 804ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/hub-text-build-2026-10-05.md	A	DOCS	-
RESTARTS: none
```
`<restart set>` = none (empty). No `UNCLASSIFIED`. P1 re-read: `window: (v) holds` (MIGRATIONS: none, empty set).

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold — the check's stop line carries no with-DB count (`suites: as built (no commit) · cobalt_dev: not taken`); the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 157 skipped in 15.40s`, 0 failed (with-DB tests skip offline: `Postgres env settings not available` / `requires_db`).
- (d2) SKIPPED under his R412 (`cto-2026-10-05.md:109`, words `cto-2026-10-05-words.md:27`: "Remove the pre-merge (d2) line from DEPLOY-HUB. Post-merge validate is the check. No --no-db allow string is needed.") and the card's `## RECORDS` (sibling wording: `deploy-deploy-preflight-fixes-1005.md:222`). 4.5 / smoke (f) `validate` is the check. See `## DECISIONS` 1.
- deselects: none (the build report `hub-text-build-2026-10-05.md` names no `--deselect`, `--tickers` or `--migration`).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-hub-text-1005 all --deploy` → exit 0, verdict lines whole:
```
offline 3786/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4639/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-hub-text-1005-all-20261005-154946.log
```
- (a) offline `3786/0`. (c) pass 1 skips: all seven inside the allowed set (`test_s3_c4_experiments.py:95` = `test_x14_live_his_template_strips_to_the_committed_fixture`, read at `<GATE>/tests/cobalt/test_s3_c4_experiments.py:96`). (c2) no migration above `0013` on this set. (c3) `with-DB 4639/0`. (e) `live-note 146/0`; its one skip (log tail) is the `COBALT_TEST_LIVE_DRC` skip, inside the set; no skip naming `COBALT_LIVE_VAULT_ROOT`.
- (f) log `:846` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `:1675` `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` → `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log `:1728` `lock released`; `.env: removed`; `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-hub-text-1005" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (exit 2; the lock dir is absent).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 3ffaa1fd (Mon Oct  5 16:16:56 EDT 2026)

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git status --short --branch` | 0 | `## main...origin/main [ahead 150]` |
| MAIN | `git status --porcelain` | 0 | ` M .claude/settings.json`; ` M` / `??` under `docs/40 - DevDocs/` only; `?? .claude/settings.json.bak` (not staged, not under src/tests/ops/configs — not refused; `## RECORDS`). No staged line. |
| MAIN | `git diff --stat f502c2df main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe | `git tag scratch-allow-probe-deploy-hub-text-1005` · `tag -d` | 0 · 0 | `Deleted tag 'scratch-allow-probe-deploy-hub-text-1005' (was f502c2df)` |
| probe | `git commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main d97114fe] …` · — · `f502c2df docs(desk): R441 hub-text deploy card 41 TIP = head 2abb7d99; deploy launching` |
| TAG | `git rev-parse --verify --quiet refs/tags/deploy-2026-10-05-hub-text` | 1 | free |
| TAG | `git rev-parse --verify --quiet refs/tags/pre-deploy-hub-text-1005` | 1 | free |

### STEP-D1 baseline
- `date` → `Mon Oct  5 16:17:22 EDT 2026` · `heartbeat show` → `<hb0>` = `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 16:17:23 EDT)`; `com.cobalt.herdr` AMB (declared `launchd_unmanaged` interim, not RED); `OK radar scanning (aftermarket), members 50`; `com.cobalt.radar running 230 min, heartbeat fresh`. No RED.
- `validate` → exit 0; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`; `registry <-> ops/: 15 label(s), exact match.`; `Placement (docs/PLACEMENT.md): tree clean.`
- `backup status` → `newest snapshot: 1.2 h old` (ssd ARMED).
- aset `state = running`, `<aset pid>` = 13209 · radar `state = running`, `<radar pid>` = 28249 · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last line `2026-10-05 16:14:24.495 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791231176937`; no traceback.
- counts: `<a0>` 42 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 58 · `<re0>` 39 · `<lc0>` 39.
- `curl … /radar` → `200`. Markers: 0, 0, 0, 0, 0, 2 = every `before`.
- No migration: `<RB>`, census and D1-M not run.

## Smoke

## CONTINUE
next: STEP-D2 (gate green at 16:16:56 EDT; D0, D1 done)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
