# deploy-launcher-fixround-1005 · SET: workflow2 · MIGRATIONS: none

## §0 Headline
(filled at close)

## L74
none

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/47-deploy-launcher-fixround-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/47-deploy-launcher-fixround-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/47-deploy-launcher-fixround-card.md" · 0 · ea8906451c597946ccf2704bd1d85e6e78b96ab0
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/47-deploy-launcher-fixround-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
R412's "production HOLD", read in `cto-2026-10-05-words.md:27`: "Production stays on hold until the workflow set is deployed." This card is part of the workflow set (LADDER: R387), so the hold does not bar it.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| P1 | `date` | 0 | Mon Oct  5 18:29:30 EDT 2026 |
| first launch | `ls -la "<REPORT>"` | 1 | No such file or directory |
| P2 | `tail -n 3 ".../launcher-checks-check-2026-10-05-r2.md"` | 0 | `CHECK DONE · job: launcher-checks · pass: 1 · tip: a545a4d8 · … · held unfixed: 0 · open: 0 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 152813` |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "<check>"` | 0 | 6bf0b815c86ac3ae11567bf32f890efea7dc37bd |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<check>"` | 0 | nothing |
| P3 | `rev-parse --short=8 a545a4d8` | 0 | a545a4d8 |
| P3 | `rev-parse --short=8 ops/launcher-fixround-1005` | 0 | a545a4d8 |
| P3 | `merge-base --is-ancestor a545a4d8 ops/launcher-fixround-1005` | 0 | — |
| P3 | `diff --stat a545a4d8 ops/launcher-fixround-1005 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` (lock free) |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-launcher-fixround-1005` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = 59d271c9 |
| P5 | `merge-base --is-ancestor 59d271c9 main` | 0 | — |
| P5 | `log --oneline main..deploy/deploy-launcher-fixround-1005` | 0 | empty |
| P6 | marker 1 `grep -c -F "is not committed and unmodified" …/deploy-step0.sh` | 1 | 0 (before 0) |
| P6 | marker 2 `grep -c -F "Fix-round row" …/DEPLOY-HUB.md` | 1 | 0 (before 0) |
| P6 | marker 3 `grep -c -F "On a fix-round row (a small fix after the check, his R376, L75)" …/CARD.md` | 1 | 0 (before 0) |
| P6 | marker 4 `grep -c -F "\| fix report \|" …/deploy-card.sh` | 1 | 0 (before 0) |
| P7 | `diff --stat main a545a4d8 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 13209 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 28249 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit a545a4d8` → `Auto-merging docs/40 - DevDocs/prompts/DEPLOY-HUB.md` / `Merge made by the 'ort' strategy.` (8 files, 586 insertions, 11 deletions)
- `<m1>` = `git -C <GATE> rev-parse --short=8 HEAD` → 1ee33bcf
- `log --oneline --merges --first-parent 59d271c9..deploy/deploy-launcher-fixround-1005` → `1ee33bcf Merge commit 'a545a4d8' into deploy/deploy-launcher-fixround-1005`
- `merge-base --is-ancestor a545a4d8 deploy/deploy-launcher-fixround-1005` → exit 0
- `diff --stat 59d271c9 deploy/deploy-launcher-fixround-1005 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C `diff --stat 59d271c9 deploy/deploy-launcher-fixround-1005 -- configs ops` → `ops/desk/deploy-card.sh | 6 +++---` · `ops/desk/deploy-step0.sh | 22 ++++` · `ops/desk/desk-launch.sh | 22 +++-` · `3 files changed, 46 insertions(+), 4 deletions(-)`. No plist added, modified or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after a fresh `.venv` create, `Installed 253 packages in 919ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = none (EMPTY: no resident goes down; the merge lands with residents up).

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat a545a4d8 1ee33bcf -- . ":(exclude)docs"` → `ops/desk/preflight.sh | 54`, `tests/ops/test_desk_launch_brain.py | 2`, `tests/ops/test_preflight.py | 78` (main moved since the check's base) → the clause does not hold; the gate runs whole (`--deploy`).
- Deselects: none (build report line 216: "no `--deselect`: this build adds no with-DB test"); no `--tickers`, no `--migration`.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 157 skipped in 15.47s` (0 failed; every skip is a with-DB skip: "Postgres env settings not available" / "requires_db").
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-launcher-fixround-1005 all --deploy` (background) → exit 0. Verdict lines, whole:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-launcher-fixround-1005-all-20261005-183114.log
```
- (a) offline: log :829 `3786 passed, 756 skipped, 1 xfailed` → `<p>` = 3786.
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :846); proof-only at 0013, nothing CHANGED.
- (c) PASS 1 whole: log :1051 `4466 passed, 7 skipped, 67 deselected, 3 xfailed` → `<d1>` = 4466. The 7 SKIPPED lines above are each inside the allowed set: test_cards_picks.py:388, :401; test_radar_evaluate.py:695; test_replay_line.py (reason names `COBALT_TEST_LIVE_DRC`); test_s3_c4_experiments.py:95 = `test_x14_live_his_template_strips_to_the_committed_fixture` (read at `<GATE>/tests/cobalt/test_s3_c4_experiments.py:95-96`); test_catalyst.py:365; test_predicate.py:262.
- (c2) `dev forward: APPLIED 18:53:20` (log :1053).
- (c3) PASS 2: log :1610 `173 passed, 1 deselected` → `<d2>` = 173; `with-DB 4639/0` = 4466 + 173.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :1675) = F0 · `cobalt_dev: 0013 — F2 = F0` (log :1726).
- THE RELEASE: log :1727–1731 `release-devdb-lock.sh deploy-launcher-fixround-1005` → `lock released`, `.env` No such file. `.env: removed (L76 lock released, log :1728; gate ended before 18:58:18)`. Verified: `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-launcher-fixround-1005" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (lock dir absent).
- (e) LIVE-NOTE: log :1797 `146 passed, 1 skipped` → `<l>` = 146; the one skip is the `COBALT_TEST_LIVE_DRC` replay_line skip (allowed); none names `COBALT_LIVE_VAULT_ROOT`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 1ee33bcf

## Deploy table
| step | command | result |
|---|---|---|
| D0 | `git -C /Users/cobalt/cobalt status --short --branch` | `## main...origin/main [ahead 169]`; ` M` lines: `.claude/settings.json` and five under `docs/40 - DevDocs/reports/`; `??` lines under `docs/40 - DevDocs/` plus `.claude/settings.json.bak` (see RECORDS); no staged line; no dirty `src/` `tests/` `ops/` `configs/` |
| D0 | `diff --stat 59d271c9 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D0 probe | `tag scratch-allow-probe-deploy-launcher-fixround-1005` · `tag -d …` | `Deleted tag 'scratch-allow-probe-deploy-launcher-fixround-1005' (was 59d271c9)` |
| D0 probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | `[main aa6c8e11] scratch: …` → `59d271c9 docs(desk): R452 deploy card 47 preflight r2 READY YES` |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-05-launcher-fixround` · `…/pre-deploy-launcher-fixround-1005` | exit 1 · exit 1 |
| D1 | `date` | Mon Oct  5 18:58:47 EDT 2026 |
| D1 `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 18:58:48 EDT)`; `OK radar scanning (aftermarket), members 50`; `OK com.cobalt.radar running 392 min, heartbeat fresh`; one `AMB com.cobalt.herdr unmanaged` (declared interim). No RED. |
| D1 `<val0>` | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK`; `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 `<jobs0>` | (validate) | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` |
| D1 | `COBALT_ENV=production uv run cobalt backup status` | `newest snapshot: 2.7 h old` |
| D1 | `launchctl print gui/501/com.cobalt.aset` | `state = running`, `<aset pid>` 13209 |
| D1 | `launchctl print gui/501/com.cobalt.radar` | `state = running`, `<radar pid>` 28249 |
| D1 | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 22243` | `Cobalt is ONLINE (PID: 22243).` · listed (`uv run src/cobalt_agent/main.py`) |
| D1 | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | last line `2026-10-05 18:57:21.254 \| INFO \| cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791240952793`; no traceback |
| D1 counts | `grep -c` × 8 | `<a0>` 42 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 58 · `<re0>` 39 · `<lc0>` 39 |
| D1 | `curl … http://127.0.0.1:5010/radar` | 200 |
| D1 markers | the four `## MARKERS` greps | 0 · 0 · 0 · 0 (each its `before`) |
| D1 migration | — | MIGRATIONS: none; no `<RB>`, no census, no proof-only |

## Smoke

## CONTINUE
next: STEP-D2 (gate green at 18:58:18; D0, D1 done)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
