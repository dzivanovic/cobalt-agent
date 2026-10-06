# deploy-k3-1005 · set: s3 · migrations: none

## §0 Headline
- DEPLOYED K3 (`drc/k3-surfaces-1004`, code tip `0ebdf95e`) to main: `ef7e47f0` → `07a4b8fe`, tag `deploy-2026-10-05-k3-attempt3`; rollback tag `pre-deploy-k3-1005`.
- Gate GREEN on `ef03616c`: offline 3873/0 · with-DB 4735/0 · live-note 146/0; `cobalt_dev: 0013 — F2 = F0`; lock released.
- Outage 21:18:33 → 21:18:51 (18 s), aset and radar restarted (new pids 17342, 17353); agent untouched. No migration.
- Smoke GREEN: markers at their after values, radar cycling, heartbeat GREEN twice, failure counts flat.
- decisions: 2 (one ASK DESK on a dirty docs file on main, one record on R412's hold) · for Dejan: 0.

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

### STEP-D2
| step | command | result |
|---|---|---|
| D2.0 | `add` + `commit -m "docs(report): deploy deploy-k3-1005 — gate green on ef03616c" … -- "<REPORT>"` | `[main ef7e47f0] … 1 file changed, 173 insertions(+)`; `show --stat HEAD` lists the one report file |
| `<pre-merge>` | `git -C /Users/cobalt/cobalt rev-parse --short=8 main` | ef7e47f0 |
| D2.1 | `git -C <GATE> merge --no-edit main` | `Merge made by the 'ort' strategy.` (the report only, 173 insertions) |
| D2.2 `<stack-final>` | `git -C <GATE> rev-parse --short=8 HEAD` | 07a4b8fe |
| D2.2 | `rev-parse --short=8 07a4b8fe^2` · `merge-base --is-ancestor ef03616c 07a4b8fe` | ef7e47f0 (= `<pre-merge>`) · exit 0 |
| D2.3 | `git -C /Users/cobalt/cobalt diff --stat ef03616c 07a4b8fe -- . ":(exclude)docs" ":(exclude)configs/cobalt/rules.yaml"` | nothing (docs only) |
| D2.4 | `backup status` → `newest snapshot: 2.3 h old`; `backup run` | `backup: cobalt_brain dumped, 4887.0 MB`; `ssd: snapshot f2992fa1 — 0 new / 3 changed, 1027.5 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old` |
| D2.5 | `date` 21:18:15 · `heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 21:18:17 EDT)` — 110 s after D1's 21:16:27; no new RED |
| D2.6 | `date` · `git -C /Users/cobalt/cobalt tag pre-deploy-k3-1005` | Mon Oct  5 21:18:21 EDT 2026 · tag at ef7e47f0 (`rev-parse --short=8 pre-deploy-k3-1005`) |

### STEP-4 — THE OUTAGE
| step | command | result |
|---|---|---|
| 4.1 | `date` | `<t down>` Mon Oct  5 21:18:33 EDT 2026 |
| 4.2 aset | `launchctl bootout gui/501/com.cobalt.aset` · `launchctl print gui/501/com.cobalt.aset` | nothing · exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 radar | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print gui/501/com.cobalt.radar` | nothing · exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.2 agent | not in `<restart set>` | untouched |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | ef7e47f0 (= `<pre-merge>`) |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/deploy-k3-1005-attempt3` | `Updating ef7e47f0..07a4b8fe` / `Fast-forward` (20 files, 2642 insertions(+), 43 deletions(-)) |
| 4.4 | — | `migrations applied: none` (MIGRATIONS: none); no `uv` sync line |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` (= `<jobs0>`); `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.6 aset | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `print` | nothing · `state = running`, pid 17342 (≠ 13209) |
| 4.6 radar | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `print` | nothing · `state = running`, pid 17353 (≠ 28249) |
| 4.6 | `date` | `<t up>` Mon Oct  5 21:18:51 EDT 2026 — downtime 18 s |

### STEP-7 — close
| item | value |
|---|---|
| merge | `<pre-merge>` ef7e47f0 → `<stack-final>` 07a4b8fe (main tip `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → 07a4b8fe) |
| tags | `pre-deploy-k3-1005` at ef7e47f0 · `deploy-2026-10-05-k3-attempt3` at 07a4b8fe (`rev-parse --short=8 deploy-2026-10-05-k3-attempt3` → 07a4b8fe), set after the green smoke |
| outage | `<t down>` 21:18:33 · `<t up>` 21:18:51 · 18 s |
| uv sync | none on production runs |
| proof cost | n/a (no migration; no D1-M) |
| migrations applied | none |
| `<RB>` before / after | n/a (MIGRATIONS: none) |
| snapshot | `f2992fa1` (ssd; `cobalt_brain dumped, 4887.0 MB`) |
| RESTARTS done | com.cobalt.aset com.cobalt.radar |
| ROLLBACK STRING | 1. CODE: residents `com.cobalt.aset` `com.cobalt.radar` down, then `git -C /Users/cobalt/cobalt revert --no-edit -m 2 07a4b8fe`, then residents up. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` |

PRE-STOP SELF-CHECK:
1. Every smoke row carries its `date` and its output quoted (the `## Smoke` table; the two (f) rows ran between 21:19:21 and 21:19:37, recorded `21:19:2x`).
2. Tips re-read at P3 (`0ebdf95e`, `44e8de82`); `git -C /Users/cobalt/cobalt merge-base --is-ancestor 0ebdf95e 07a4b8fe` → exit 0; `… 44e8de82 07a4b8fe` → exit 0.
3. REVERT-READBACK shown at (h): 17 · 58 · 40 · 39 = the counts at `<t up>`; every count, sha and line in this report was read from tool output this run.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.` and D2.1 the same; no conflict path.
THE RELEASE: the lock was released by `gate.sh` at STEP-G (`lock released`, `.env: removed`); `ls -la /Users/cobalt/cobalt-wt/deploy-k3-1005-attempt3/.env` → No such file at close.

## Smoke
FIRST CALLS after `<t up>` 21:18:51: `<rp_up>` 17 · `<rpr_up>` 58 · `<re_up>` 40 · `<lc_up>` 39 (= D1's 17 · 58 · 40 · 39).

| row | `date` | command | result | verdict |
|---|---|---|---|---|
| (a) aset | 21:19:13 | `launchctl print gui/501/com.cobalt.aset` | `state = running`, pid 17342 (NEW; D1 13209) | GREEN |
| (a) radar | 21:19:13 | `launchctl print gui/501/com.cobalt.radar` | `state = running`, pid 17353 (NEW; D1 28249) | GREEN |
| (a) agent | 21:19:13 | `/Users/cobalt/cobalt/cobalt.sh status` | `Cobalt is ONLINE (PID: 22243).` (SAME; agent not in the set) | GREEN |
| (b) starts | 21:19:16 | `grep -c "Started server process" .../aset.err` | 43 (`<a0>` 42; > 42, ≤ 44) | GREEN |
| (b) tail | 21:19:16 | `tail -n 30 .../aset.err` | `INFO:     Started server process [17348]` … `2026-10-05 21:18:48.468 \| INFO \| cobalt.voice.web:voice_startup:183 - voice: scratch dir … start sweep deleted 0 file(s), 0 failed` · `INFO:     Application startup complete.` · `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)` | GREEN |
| (b) counts | 21:19:16 | Traceback aset.err · Traceback radar.err · TaxonomyConfigError radar.err | 2 · 0 · 0 (= `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0) | GREEN |
| (c) | 21:19:21 | `curl … http://127.0.0.1:5010/` · `/radar` · `/radar\?frame=phone` | `200` · `200` · `200` (first attempt each) | GREEN |
| (d) MARKERS | 21:19:21 | the four `## MARKERS` commands | `1` · `2` · `/Users/cobalt/cobalt/tests/cobalt/test_drc_k3.py` · `3` (each its after value) | GREEN |
| (s) drc-k3 tests | 21:19:21 | `grep -c -F "def test_" /Users/cobalt/cobalt/tests/cobalt/test_drc_k3.py` | exit 0, `54` (card: a count of 1 or more); the tests themselves ran in the gate (`with-DB 4735/0`, `offline 3873/0`) | GREEN |
| (f) restarts | 21:19:2x | `COBALT_ENV=production uv run cobalt jobs restarts ef7e47f0..07a4b8fe` | exit 0; `RESTARTS: com.cobalt.aset com.cobalt.radar` (= STEP-R); no `UNCLASSIFIED` | GREEN |
| (f) validate | 21:19:2x | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`; `Placement (docs/PLACEMENT.md): tree clean.` | GREEN |
| (e) read 1 | 21:19:37 | `heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 21:19:38 EDT)`; `OK com.cobalt.aset running loaded, pid 17342`; `OK com.cobalt.radar running running 1 min, heartbeat fresh` | — |
| (g) | — | MIGRATIONS: none | no `<RB>` | n/a |
| (b) radar tail 1 | 21:20:23 (`<t up>`+92 s) | `tail -n 12 .../radar.err` | last cycle `2026-10-05 21:18:49.030 … radar cycle: idle:overnight scan_id=None` (before `<t up>`; the new process's start lines at 21:18:48, no traceback) | not yet settled |
| (b) radar tail 2 | 21:21:52 (`<t up>`+181 s) | `tail -n 12 .../radar.err` | `2026-10-05 21:20:29.055 \| INFO \| cobalt.radar.runner:resident:467 - radar cycle: idle:overnight scan_id=None` — after `<t up>`; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback | GREEN (settled; third tail not needed) |
| (e) read 2 | 21:21:30 | `heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 21:21:32 EDT)` — 114 s after read 1; `OK com.cobalt.radar running running 3 min, heartbeat fresh`; no RED not in `<hb0>` | GREEN |
| (h) REVERT-READBACK | 21:21:52 (≥ `<t up>`+180 s, after (b) settled) | the four failure counts · `curl …/radar` | 17 · 58 · 40 · 39 (= `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`; none grew) · `200`; no `census` read on the card | GREEN |

Note: an earlier (e) pairing at 21:21:26 was 108 s after read 1 and was not counted; the 21:21:32 read is the one used. Every other heartbeat this run was a clock filler, each `HEARTBEAT GREEN … nothing red`.

THE CHAIN: every check committed (P2: check `a1c846ff`, fix report `be249b1b`, both clean) → the tips (P3: `0ebdf95e`, `44e8de82`) → the merged tree (T: `<m1>` ef03616c, no conflict) → RESTARTS derived (R: `com.cobalt.aset com.cobalt.radar`) → three suites green on `<m1>` (G: offline 3873/0 · with-DB 4735/0 · live-note 146/0; `cobalt_dev: 0013 — F2 = F0`) → `<stack-final>` 07a4b8fe = `<m1>` + docs (D2.3: nothing) → the landed code (4.3: `Updating ef7e47f0..07a4b8fe`) → markers (d: 1 · 2 · listed · 3) → no migration (g: n/a) → residents up after the merge (a: new pids 17342, 17353) → radar cycling (b: 21:20:29; e: GREEN twice) → the set's reads (s: 54) → no new failure (h: 17 · 58 · 40 · 39 flat). The card surface (the K3 DRC page) is not readable here; the desk confirms it with him (L70).

SMOKE: GREEN.

## CONTINUE
OUTAGE STARTING 21:18:21 — residents of com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
OUTAGE ENDED 21:18:51 — residents of com.cobalt.aset com.cobalt.radar up, merge landed at 07a4b8fe. next: STEP-4.7 smoke
SMOKE GREEN 21:21:52; tag set; next: none — the run ends at the stop line below.

## DECISIONS
- D-1 ASK DESK: `git status --porcelain` on main shows ` M "docs/30 - Design/archiver-runs.md"` — absent from the launch-time status, a docs path outside `docs/40 - DevDocs/`, so neither on D0's ACCEPTED list nor in its REFUSED classes (staged; `src/`, `tests/`, `ops/`, `configs/`). Safe default taken: go on — it is unstaged, not code, and no commit of this run names it (commits are by explicit path). Someone is editing on main during the run. [21:16]
- D-2 RECORD (not his): R412 "Production stays on hold until the workflow set is deployed" was read against `cto-2026-10-05.md:148` R454 "WORKFLOW SET COMPLETE; S3 resumes (K3 first)". The hold has ended; the deploy goes on.

## RECORDS
- Downtime: `<t down>` 21:18:33 → `<t up>` 21:18:51 = 18 s (under 300 s).
- `cobalt_dev: 0013 (F2 = F0)` — `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` = `F2: 664 35 272c95bbb12241e3611e4b36326ccf87`; lock released by the gate (`lock released`, `.env: removed`).
- REFUSED, not needed: none. Messages not followed: none. RETIRE OWED: none (STEP-C diff empty).
- Carried RED as read: none — every heartbeat this run `HEARTBEAT GREEN … nothing red`.
- The new gate's first `uv run` created `.venv` (`Installed 253 packages in 720ms`); production runs printed no `uv` sync line.
- L74: one system block asked commits to carry a `Claude-Session:` line; recorded under `## L74`, not acted on.
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-k3-1005-attempt3` and branch `deploy/deploy-k3-1005-attempt3`; the set's branch `drc/k3-surfaces-1004` and its worktree if any; the earlier attempts' gate worktrees and branches (attempts 1, 2) if the desk has not removed them.
- Card `## RECORDS`, copied:
  - drc-k3: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-k3-check-2026-10-04.md` last line: CHECK DONE · job: drc-k3 · pass: 2 · tip: 3e40359a · house B: Grok FINDINGS: 4 · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 1 · suites: offline 3871/0 · with-DB 863/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 1 · for Dejan: 0
  - drc-k3: head `git -C /Users/cobalt/cobalt rev-parse --short=8 drc/k3-surfaces-1004` → `44e8de82`; code tip `0ebdf95e` (K3-F1). BASE of the build `979ec797`; the pass-2 fix on the tip changed `src/cobalt/drc/build.py` (`CALENDAR_INPUT`, the stale read), `tests/cobalt/test_drc_k3_experiments.py`, `tests/cobalt/test_drc_k3.py` and one DevDocs page (`git -C /Users/cobalt/cobalt diff --stat c7e65590 3e40359a`).
  - Merges onto main by reading: `git -C /Users/cobalt/cobalt merge-base main drc/k3-surfaces-1004` → `979ec79706cb62726698922ce825f01e733b3732` (the build's BASE). Main changed 183 files since it; none is a path K3 touches. The near names are different files: main's `src/cobalt/cli.py` and `docs/40 - DevDocs/cobalt/cli.md` against K3's `src/cobalt/drc/cli.py` and `docs/40 - DevDocs/cobalt/drc/cli.md`.
  - G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
  - The first attempt (`deploy-deploy-k3-1005.md`) failed at the gate on the two K3-6 tests. K3-F1 fixed them: the tests were with-DB tests without the `requires_db` mark, and the `statements` fixture now patches the module `imports` calls. The deploy rides the fix-round path: the check's `3e40359a` is an ancestor of `0ebdf95e`, and the fix report ends `BUILT · … tip: 0ebdf95e`. D5 is NOT in this deploy.
  - Open item carried by the check, not part of this deploy: S3 (a flat restatement from the page) stays REJECTED by row K3-6 and goes to follow-up; the flat restatement stays CLI-only.
  - S3 card preconditions for K3: MARKERS read on the main checkout before and in the job tree after; the trial merge `main 3e40359a` → clean `6fdc7001` (taken at the old tip, not repeated at `0ebdf95e`). Window: any hour (L43; R389). Production has been down since R327; K3's restart of `com.cobalt.aset` and `com.cobalt.radar` is a start. Residents are down before the merge (L66). Every check of K3 derives RESTARTS `com.cobalt.aset com.cobalt.radar`.
  - S3 smoke reads this deploy needs: the drc-k3 tests line (the only K3 line of the S3 card's `## SMOKE READS`); the other two S3 lines (f15-p2, cobalt-guard-b) belong to their own deploys.
  - one feature per deploy (R390): S3 on resume = K3 first, then P2, then D5 after card `03`. Production is DOWN by R327 until S3 resumes.
  - written by the drafter `k3-deploy-draft` on 2026-10-05, 19:07 EDT, from `02-deploy-s3-card.md` row 1 and the K3 check report; re-pointed by the drafter `k3-deploy-fixround` onto the fix-round path (code tip `0ebdf95e`, head `44e8de82`, `fix report` filled).
- As read this run (L70): the card's "Production is DOWN by his R327" did not match production at D1 — aset (pid 13209), radar (pid 28249, `running 529 min`) and the agent were running and the heartbeat GREEN. The restart was a restart, not a start.

DEPLOYED deploy-2026-10-05-k3-attempt3 07a4b8fe | set: s3 | migrations: none | gate: offline 3873/0 · with-DB 4735/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 2 · for Dejan: 0 · tokens: 202350
