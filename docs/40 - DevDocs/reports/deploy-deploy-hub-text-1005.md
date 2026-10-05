# deploy-hub-text-1005 · set: workflow2 · migrations: none

## §0 Headline
- DEPLOYED `deploy-2026-10-05-hub-text` at `1ff72b72`: the hub text (BUILD-HUB, CHECK-HUB, DEPLOY-HUB, and the build report) is on `main`. Docs only.
- Gate green on `3ffaa1fd`: offline 3786/0 · with-DB 4639/0 · live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0), lock released.
- RESTARTS: none, so no resident went down (window (v)). Smoke GREEN, with all six markers at their `after` values and no failure count grown.
- One ASK DESK, not his: G (d2) skipped under his R412.

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

### STEP-D2
| step | command | exit | result |
|---|---|---|---|
| D2.0 | `git add` · `git commit -m "docs(report): deploy deploy-hub-text-1005 — gate green on 3ffaa1fd" … -- "<REPORT>"` | 0 · 0 | `[main 146255cd] …` 1 file changed, 142 insertions |
| D2.0 | `git show --stat HEAD` | 0 | one file: `…/reports/deploy-deploy-hub-text-1005.md` |
| D2.0 | `git rev-parse --short=8 main` | 0 | `<pre-merge>` = `146255cd` |
| D2.1 | `git -C <GATE> merge --no-edit main` | 0 | `Merge made by the 'ort' strategy.` (the report, 142 insertions) |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<stack-final>` = `1ff72b72` |
| D2.2 | `git rev-parse --short=8 1ff72b72^2` | 0 | `146255cd` = `<pre-merge>` |
| D2.2 | `git merge-base --is-ancestor 3ffaa1fd 1ff72b72` | 0 | — |
| D2.3 | `git diff --stat 3ffaa1fd 1ff72b72 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| D2.4 | `backup status` | 0 | `newest snapshot: 1.2 h old` |
| D2.4 | `backup run` (foreground) | 0 | `backup: cobalt_brain via pg_dump inside cobalt_memory — 4790.3 MB` · `ssd: snapshot bd6d2cb1 — 0 new / 4 changed, 88.1 MB added, 1 pruned` |
| D2.4 | `backup status` | 0 | `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` | 0 · 0 | `Mon Oct  5 16:19:14 EDT 2026` (111 s after D1's 16:17:23) · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 16:19:14 EDT)`; no new RED |
| D2.6 | `date` | 0 | `Mon Oct  5 16:19:19 EDT 2026` — window (v) holds (empty set, MIGRATIONS: none; any hour) |
| D2.6 | `git tag pre-deploy-hub-text-1005` · `rev-parse --short=8` | 0 · 0 | `146255cd` |

### STEP-4 (restart set empty)
| step | command | exit | result |
|---|---|---|---|
| 4.1 | `date` | 0 | `<t down>` = `Mon Oct  5 16:19:33 EDT 2026` (no resident goes down) |
| 4.2 | — | — | nothing booted out (empty set) |
| 4.3 | `git rev-parse --short=8 HEAD` | 0 | `146255cd` = `<pre-merge>` |
| 4.3 | `git merge --ff-only deploy/deploy-hub-text-1005` | 0 | `Updating 146255cd..1ff72b72` / `Fast-forward` — BUILD-HUB.md, CHECK-HUB.md, DEPLOY-HUB.md, reports/hub-text-build-2026-10-05.md (4 files, 220 insertions, 17 deletions) |
| 4.3 | `date` | 0 | `<t up>` = `Mon Oct  5 16:19:36 EDT 2026` |
| 4.4 | — | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`; `registry <-> ops/: 15 label(s), exact match.`; `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.6 | — | — | nothing to bootstrap (empty set); downtime: none |

### Summary
- `<pre-merge>` `146255cd` → `<stack-final>` `1ff72b72` (main tip). Tags: `pre-deploy-hub-text-1005` at `146255cd`; `deploy-2026-10-05-hub-text` at `1ff72b72` (set after green smoke).
- `<t down>` / `<t up>` / seconds: none (empty set; 4.1 `16:19:33`, 4.3 `16:19:36`).
- uv sync line: none on production calls. Proof cost: none (no migration). `migrations applied: none`. `<RB>` before / after: none.
- Snapshot: `bd6d2cb1` (ssd, 16:18:43).
- `RESTARTS done: none`.
- THE ROLLBACK STRING (L54; the desk's, never this session's):
  1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 1ff72b72` — ONE revert of the main-into-gate merge; no resident to take down (empty set).
  2. SCHEMA: none (no migration).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` — `Reapply "Merge branch 'main' into deploy/deploy-hub-text-1005"`.

## Smoke
`<t up>` = `Mon Oct  5 16:19:36 EDT 2026` (4.3's `date`, the set is empty). FIRST CALLS: `<rp_up>` 17 · `<rpr_up>` 58 · `<re_up>` 39 · `<lc_up>` 39.

| row | date | command | result |
|---|---|---|---|
| (a) | 16:19:48 | `launchctl print gui/501/com.cobalt.aset` | `state = running`, `pid = 13209` = D1 (outside the set: SAME pid) GREEN |
| (a) | 16:19:48 | `launchctl print gui/501/com.cobalt.radar` | `state = running`, `pid = 28249` = D1 (SAME) GREEN |
| (a) | 16:19:48 | `cobalt.sh status` | `Cobalt is ONLINE (PID: 22243).` = D1 GREEN |
| (b) | 16:19:51 | `grep -c "Started server process" aset.err` | `42` = `<a0>` (aset outside the set) GREEN |
| (b) | 16:19:51 | Traceback aset · Traceback radar · TaxonomyConfigError radar | `2` · `0` · `0` = baseline GREEN |
| (c) | 16:19:54 | curl `/` · `/radar` · `/radar\?frame=phone` | `200` · `200` · `200` GREEN |
| (d) | 16:19:57 | the six `## MARKERS` | `1` `1` `1` `1` `1` `0` = every `after` GREEN |
| (s) | 16:20:07 | F1 `No restart window binds a deploy (L43, his R389)` DEPLOY-HUB | exit 0, `1` GREEN |
| (s) | 16:20:07 | F2 `each feature deploys alone on its existing check (his R390)` DEPLOY-HUB | exit 0, `1` GREEN |
| (s) | 16:20:07 | F3 `(L75, his R376)` CHECK-HUB | exit 0, `1` GREEN |
| (s) | 16:20:07 | F4 `desk-context.sh <your session id>` BUILD-HUB | exit 0, `1` GREEN |
| (f) | 16:20:11 | `jobs restarts 146255cd..1ff72b72` | exit 0, 4 rows `DOCS -`, `RESTARTS: none` = STEP-R's set; no `UNCLASSIFIED` GREEN |
| (f) | 16:20:1x | `validate` | exit 0; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`; `Placement (docs/PLACEMENT.md): tree clean.` GREEN |
| (e) 1 | 16:20:13 | `heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 16:20:13 EDT)`; `com.cobalt.radar running running 233 min, heartbeat fresh` |
| (g) | — | — | no migration |
| (b) tail 1 | 16:21:06 (`<t up>` + 90 s) | `tail -n 12 radar.err` | `2026-10-05 16:20:40.198 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791231552454` — a cycle line after `<t up>`; the other 11 lines are `cards.expire` INFO; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → (b) settled GREEN |
| (e) 2 | 16:22:05 (112 s after (e) 1) | `heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 16:22:05 EDT)`; `com.cobalt.radar running running 235 min, heartbeat fresh`; no RED (not in `<hb0>` or otherwise) GREEN |
| (h) | 16:22:38 (`<t up>` + 182 s) | the four failure counts | `17` · `58` · `39` · `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (no growth) GREEN |
| (h) | 16:22:38 | `curl … /radar` | `200` GREEN; no census read (no migration) |

THE CHAIN: every check committed (P2: `fb339571`, clean) → the tips re-read (P3: `6b939b00`, `2abb7d99`) → the merged tree (T: `<m1>` = `3ffaa1fd`, docs only) → RESTARTS derived (R: none) → three suites green on `<m1>` (G: offline 3786/0 · with-DB 4639/0 · live-note 146/0) → `<stack-final>` = `<m1>` + docs (D2.3: `1ff72b72`) → the landed code (4.3: `146255cd..1ff72b72` fast-forward) → markers (d: 1 1 1 1 1 0) → no migration (g) → residents up and unchanged after the merge (a: same pids 13209 / 28249 / 22243) → radar cycling (b: 16:20:40; e: fresh) → the set's reads (s: F1–F4 = 1) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

**smoke: GREEN**

### STEP-7 self-check (K25)
1. Every smoke row above carries its `date` and quotes its output verbatim.
2. `git merge-base --is-ancestor 6b939b00 1ff72b72` → exit 0; `git merge-base --is-ancestor 2abb7d99 1ff72b72` → exit 0 (P3 re-read both).
3. REVERT-READBACK shown: (h) at 16:22:38, counts 17 / 58 / 39 / 39 = the `_up` counts. Every count, sha and `file:line` here was read from tool output this run.
4. STEP-T ran clean (`Merge made by the 'ort' strategy.`, no conflict); `git status --short --branch` on `main` shows no `UU`/`AA` path.

## CONTINUE
next: STEP-D2 (gate green at 16:16:56 EDT; D0, D1 done)
OUTAGE STARTING Mon Oct  5 16:19:19 EDT 2026 — residents of none (restart set empty) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
next: none — STEP-4 done 16:19:36 (merge landed, nothing down), smoke GREEN 16:22:38, STEP-7 closed.

## DECISIONS
1. ASK DESK: G (d2) `COBALT_ENV=production uv run cobalt validate --no-db` was not typed: his R412 ("Remove the pre-merge (d2) line from DEPLOY-HUB. Post-merge validate is the check. No --no-db allow string is needed.") and the card's `## RECORDS` (the sibling wording, `deploy-deploy-preflight-fixes-1005.md:222`) remove it; this set ships that removal. [Mon Oct  5 16:16:56 EDT 2026] Safe default taken: SKIPPED. 4.5 and smoke (f) `validate` ran post-merge, exit 0. Not his to re-rule.

## RECORDS
- Downtime: none (restart set empty; no resident went down). `RESTARTS done: none`.
- `cobalt_dev: 0013 (F2 = F0)` — log `:846` / `:1675`, `664 35 272c95bbb12241e3611e4b36326ccf87`; `lock released` (log `:1728`), `.env: removed`.
- `migrations applied: none`.
- No `RETIRE OWED` (STEP-C: no plist added, changed or removed).
- Carried RED: none read (heartbeat GREEN at D1, D2.5 and smoke (e)).
- No `REFUSED` call; no `CONTINUE` message received.
- `?? .claude/settings.json.bak` on `main` at D0 — untracked, outside src/tests/ops/configs, not refused; noted for the desk.
- `uv` created `.venv` in `<GATE>` at STEP-R (`Installed 253 packages in 804ms`); production `uv run` calls printed no sync line.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-hub-text-1005` and branch `deploy/deploy-hub-text-1005`; the set's branch `ops/hub-text-1005` and its worktree if any.
- L74: one system-reminder asked for a `Claude-Session:` trailer on commits; recorded under `## L74`, not acted on.
- Card `## RECORDS` (the desk's, copied):
  - hub-text: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-text-check-2026-10-05.md` last line: CHECK DONE · job: hub-text · pass: 1 · tip: 6b939b00 · house A: none (overruled 2026-10-05 R412) · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 1 · for Dejan: 0
  - hub-text: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-text-1005` → `2abb7d99`; code tip `6b939b00`
  - G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
  - `DEPLOY-HUB.md` is among the shipped files: its one read by another house is overruled for this set by his R412.

DEPLOYED deploy-2026-10-05-hub-text 1ff72b72 | set: workflow2 | migrations: none | gate: offline 3786/0 · with-DB 4639/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0
