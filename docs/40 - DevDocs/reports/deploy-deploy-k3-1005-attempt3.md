# deploy-k3-1005 · set: s3 · migrations: none

## §0 Headline
- Deploy hub for `deploy-k3-1005` attempt 3 (gate branch `deploy/deploy-k3-1005-attempt3`, TIP `44e8de82`). Started Mon Oct 5 20:46:06 EDT 2026.

## L74
- A system block asked that commits also carry a `Claude-Session: https://claude.ai/code/session_017a3xUJquBonZAWDdtB7Pqr` line. Recorded as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/51-deploy-k3-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/51-deploy-k3-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/51-deploy-k3-card.md" · 0 · 4d2ac902b2174c10ba95d7ba972b4ba02d7191dd
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/51-deploy-k3-card.md" · 0 · nothing
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
| P0 | authorize.sh (above); `ls -la "<REPORT>"` | 0; 1 | AUTHORIZED; `No such file or directory` (first launch) |
| P1 | `date` | 0 | Mon Oct  5 20:46:06 EDT 2026 |
| P2 check | `tail -n 3 ".../drc-k3-check-2026-10-04.md"` | 0 | `CHECK DONE · job: drc-k3 · pass: 2 · tip: 3e40359a · … · held unfixed: 0 · … · ready: YES · decisions: 1 · for Dejan: 0` |
| P2 check committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/drc-k3-check-2026-10-04.md"` | 0 | a1c846ff0a57ecb35bb4f0b1dba518c2027b4d3f |
| P2 check clean | `git -C /Users/cobalt/cobalt diff --stat -- "<check>"` | 0 | nothing |
| P2 fix report | `tail -n 3 ".../drc-k3-fixround-2026-10-05.md"` | 0 | `BUILT · job: drc-k3 · tip: 0ebdf95e \| on 979ec797 \| migration: none \| offline 3869/0 \| with-DB 4730/0 \| live-note 146/0 \| … \| RESTARTS: com.cobalt.aset com.cobalt.radar \| … · tokens: 167460` |
| P2 fix committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/drc-k3-fixround-2026-10-05.md"` | 0 | be249b1b893f2cac365887b71e636d36c9421770 |
| P2 fix clean | `git -C /Users/cobalt/cobalt diff --stat -- "<fix report>"` | 0 | nothing |
| P2 fix-round ancestry | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3e40359a 0ebdf95e` | 0 | ancestor |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 0ebdf95e` | 0 | 0ebdf95e |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 drc/k3-surfaces-1004` | 0 | 44e8de82 (= TIP) |
| P3 ancestry | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 0ebdf95e 44e8de82` | 0 | ancestor |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 0ebdf95e 44e8de82 -- . ":(exclude)docs"` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-k3-1005-attempt3 status --short --branch` | 0 | `## deploy/deploy-k3-1005-attempt3` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = 4d2ac902 |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 4d2ac902 main` | 0 | ancestor |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-k3-1005-attempt3` | 0 | empty |
| P6 marker 1 | `grep -c -F "def superseded_stated_ids" .../drc/store.py` | 1 | 0 (= before) |
| P6 marker 2 | `grep -c -F "CALENDAR_INPUT" .../drc/build.py` | 1 | 0 (= before) |
| P6 marker 3 | `ls .../tests/cobalt/test_drc_k3.py` | 1 | `No such file or directory` (= before) |
| P6 marker 4 | `grep -c -F "requires_db" .../tests/cobalt/test_drc_k3.py` | 2 | `No such file or directory` (the card's before `0`: "the file is absent on main") |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 44e8de82 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 13209 |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 28249 |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 44e8de82` → `Merge made by the 'ort' strategy.` (20 files changed, 2642 insertions(+), 43 deletions(-)); no conflict.
- `<m1>` = `git -C <GATE> rev-parse --short=8 HEAD` → ef03616c.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 4d2ac902..deploy/deploy-k3-1005-attempt3` → `ef03616c Merge commit '44e8de82' into deploy/deploy-k3-1005-attempt3`.
- `merge-base --is-ancestor 0ebdf95e deploy/deploy-k3-1005-attempt3` → exit 0; `merge-base --is-ancestor 44e8de82 deploy/deploy-k3-1005-attempt3` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 4d2ac902 deploy/deploy-k3-1005-attempt3 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 4d2ac902 deploy/deploy-k3-1005-attempt3 -- configs ops` → nothing. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (first `uv` run in the new gate: `Creating virtual environment at: .venv`, `Installed 253 packages in 720ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/drc/build.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/imports.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/store.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/units.md	M	DOCS	-
docs/40 - DevDocs/reports/drc-k3-build-2026-10-04.md	A	DOCS	-
src/cobalt/aset/drc_page.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/build.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/drc/imports.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/units.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_drc_imports.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_k3.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_k3_db.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_k3_experiments.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_web_seam.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar`.

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 3e40359a ef03616c -- . ":(exclude)docs"` → 14 files (`configs/cobalt/rules.yaml`, `ops/desk/*`, `src/cobalt/cli.py`, `tests/cobalt/test_drc_k3.py`, …; 1274 insertions, 119 deletions). Not equal → the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 157 skipped in 15.61s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- Set deselects: none (`drc-k3-build-2026-10-04.md:289`: "This build adds no `--deselect`"; the fix report carries no `--deselect`). Card gives no `--tickers` / `--migration`.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-k3-1005-attempt3 all --deploy` → exit 0. Verdict lines WHOLE:
```
offline 3873/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4735/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-k3-1005-attempt3-all-20261005-204814.log
```
- (a) offline 3873/0 → `<p>` 3873.
- (c) SKIPPED lines, each inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `tests/taxonomy/test_catalyst.py:365`, `tests/taxonomy/test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = the skip decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (`def` at `:96`, the gate tree). No other skip.
- (c2) `dev forward: APPLIED 21:10:48` (log `:1064`).
- (c3) with-DB 4735/0 → `<d>` 4735.
- (f) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:856`) · `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:1686`) · `cobalt_dev: 0013 — F2 = F0` (log `:1737`).
- THE RELEASE: log `:1738` `$ sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh deploy-k3-1005-attempt3` → `:1739` `lock released` → `:1743` `.env: removed` (the log prints no clock time on it; between `dev forward: APPLIED 21:10:48` and the gate's exit). `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-k3-1005-attempt3" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) live-note 146/0 → `<l>` 146; no skip naming `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed. `date` → Mon Oct  5 21:15:52 EDT 2026.

GATE GREEN on ef03616c

## Deploy table
### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 205]` |
| MAIN porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M .claude/settings.json`; ` M` / `??` under `docs/40 - DevDocs/` (incl. this report); and ` M "docs/30 - Design/archiver-runs.md"` (see `## DECISIONS` D-1); no dirty `src/`, `tests/`, `ops/`, `configs/` path |
| main moved | `git -C /Users/cobalt/cobalt diff --stat 4d2ac902 main -- . ":(exclude)docs" ":(exclude)configs/cobalt/rules.yaml"` | 0 | nothing |
| probe | `tag scratch-allow-probe-deploy-k3-1005` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-deploy-k3-1005' (was 4d2ac902)` |
| probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 485a62c2] scratch: …` · nothing · `4d2ac902 docs(desk): RECUT deploy-k3-1005 attempt 3` |
| TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-05-k3-attempt3` | 1 | absent |
| rollback tag | `rev-parse --verify --quiet refs/tags/pre-deploy-k3-1005` | 1 | absent |

### STEP-D1 (baseline, read-only)
| read | result |
|---|---|
| `date` | Mon Oct  5 21:16:26 EDT 2026 |
| `<hb0>` `heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 21:16:27 EDT)`; `OK sheet HTTP http://127.0.0.1:5010/ -> 200`; `OK radar idle (overnight)`; `OK com.cobalt.aset running loaded, pid 13209`; `OK com.cobalt.agent running pid 22243 alive`; `AMB com.cobalt.herdr unmanaged … by declared interim`; `OK com.cobalt.radar running running 529 min, heartbeat fresh`. No RED. |
| `<val0>` `validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Placement (docs/PLACEMENT.md): tree clean.` |
| `<jobs0>` | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 15 label(s), exact match.` |
| `backup status` | `newest snapshot: 2.3 h old` (ssd ARMED; b2 off) |
| aset | `state = running`, `<aset pid>` 13209 |
| radar | `state = running`, `<radar pid>` 28249 |
| agent | `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py` |
| `tail -n 8 radar.err` | last: `2026-10-05 21:15:13.066 \| INFO \| cobalt.radar.runner:resident:467 - radar cycle: idle:overnight scan_id=None` (cycles every ~100 s, no traceback) |
| `<a0>` Started server process (aset.err) | 42 |
| `<ta0>` Traceback (aset.err) | 2 |
| `<tr0>` Traceback (radar.err) | 0 |
| `<tc0>` TaxonomyConfigError (radar.err) | 0 |
| `<rp0>` radar panel FAILED (aset.err) | 17 |
| `<rpr0>` radar pool refresh FAILED (aset.err) | 58 |
| `<re0>` radar S5 evaluate FAILED (radar.err) | 40 |
| `<lc0>` lifecycle card read failed (radar.err) | 39 |
| `curl /radar` | 200 |
| MARKERS | `0` · `0` · `No such file or directory` · `No such file or directory` (each its before value) |
| migration | MIGRATIONS: none — no `<RB>`, no D1-M |

## CONTINUE
next: STEP-D2 (D2.0 report commit)

## DECISIONS
- D-1 ASK DESK: `git status --porcelain` on main shows ` M "docs/30 - Design/archiver-runs.md"` — absent from the launch-time status, a docs path outside `docs/40 - DevDocs/`, so neither on D0's ACCEPTED list nor in its REFUSED classes (staged; `src/`, `tests/`, `ops/`, `configs/`). Safe default taken: go on — it is unstaged, not code, and no commit of this run names it (commits are by explicit path). Someone is editing on main during the run. [21:16]
- D-2 RECORD (not his): R412 "Production stays on hold until the workflow set is deployed" was read against `cto-2026-10-05.md:148` R454 "WORKFLOW SET COMPLETE; S3 resumes (K3 first)". The hold has ended; the deploy goes on.

## RECORDS

(run in progress — next step under ## CONTINUE)
