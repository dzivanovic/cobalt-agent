# deploy radar-top50-1009 · SET: none · MIGRATIONS: none

## §0 Headline
- The radar top-50 over-cap change (`ops/radar-top50-1009`, code tip `109bcfc0`) is live in production: `main` `0d187b31` → `e4586978`, tag `deploy-2026-10-09-radar-top50`.
- Gate green on `2d580f26`: offline 4054/0 · with-DB 4941/0 · live-note 146/0. No migration.
- aset and radar restarted 18:26:30 → 18:26:44 (14 s); smoke GREEN, failure counts flat.
- One decision (an untracked `.claude/settings.json.bak` on `main`), safe default taken; nothing for Dejan. Push is his.

## L74
- The session's harness attribution reminder asked commits to carry a `Claude-Session:` line. Recorded here as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/184-deploy-radar-top50-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/184-deploy-radar-top50-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/184-deploy-radar-top50-card.md" · 0 · b97d8ae87cf5ea4c87a21c436ae1baec3d70d288
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/184-deploy-radar-top50-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above); report absent: `ls -la "<REPORT>"` | 0 · 1 | `AUTHORIZED` · `No such file or directory` (first launch) |
| P1 | `date` | 0 | `Fri Oct  9 17:54:17 EDT 2026` |
| P2 | `tail -n 3 "…/radar-top50-check-2026-10-09.md"` | 0 | last line `CHECK DONE · job: radar-top50-1009 · pass: 1 · tip: 109bcfc0 · … · held unfixed: 0 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 153816` — carries `held unfixed: 0` and `ready: YES`; `tip: 109bcfc0` = row code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/radar-top50-check-2026-10-09.md"` | 0 | `92b08e65c7cc121490d5be316c706c95f9752e96` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/radar-top50-check-2026-10-09.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 109bcfc0` | 0 | `109bcfc0` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-top50-1009` | 0 | `b5b61eb0` (= row, = `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 109bcfc0 b5b61eb0` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 109bcfc0 b5b61eb0 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` (lock free) |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/radar-top50-1009` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `b97d8ae8` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor b97d8ae8 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/radar-top50-1009` | 0 | empty |
| P6 | `grep -c -F "over_cap" …/radar_panel.py` | 1 | `0` (= before) |
| P6 | `grep -c -F "Over cap" …/radar_panel.py` | 1 | `0` (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main b5b61eb0 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none holds) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 93108` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 93120` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit b5b61eb0` → `Auto-merging docs/40 - DevDocs/cobalt/aset/radar_panel.md` / `Auto-merging src/cobalt/aset/radar_panel.py` / `Merge made by the 'ort' strategy.` (4 files changed, 308 insertions(+), 2 deletions(-)).
- `git -C <GATE> rev-parse --short=8 HEAD` → `2d580f26` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent b97d8ae8..deploy/radar-top50-1009` → `2d580f26 Merge commit 'b5b61eb0' into deploy/radar-top50-1009` (one line, one head).
- `merge-base --is-ancestor 109bcfc0 deploy/radar-top50-1009` → exit 0; `merge-base --is-ancestor b5b61eb0 deploy/radar-top50-1009` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat b97d8ae8 deploy/radar-top50-1009 -- src/cobalt/db_migrations` → nothing (no migration path; `MIGRATIONS: none` holds).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat b97d8ae8 deploy/radar-top50-1009 -- configs ops` → nothing (no plist added, modified or removed).

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the gate's `.venv`: `Installed 253 packages in 821ms`), whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-top50-build-2026-10-09.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar` (= the check's RESTARTS).

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 109bcfc0 2d580f26 -- . ":(exclude)docs"` → 8 files (`ops/desk/bare-guard.py`, `ops/desk/stop-guard.py`, `src/cobalt/aset/radar_panel.py`, `src/cobalt/aset/web.py`, `tests/cobalt/test_radar_panel_cards.py`, `tests/cobalt/test_s3_c3_panel_offline.py`, `tests/ops/test_bare_guard.py`, `tests/ops/test_stop_guard.py`; 768+/71-: `main` moved since the branch's base) → the clause does NOT hold; the gate runs whole (`--deploy`).
- Deselects: the build report `radar-top50-build-2026-10-09.md:126` — "No `--deselect`, `--tickers` or `--migration`: this build adds no with-DB test and no migration." → none.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `262 passed, 163 skipped in 16.46s` (0 failed; every skip is a with-DB `Postgres env settings not available` / `requires_db` skip).
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-radar-top50-1009 all --deploy` (background) → exit 0. Verdict lines WHOLE:
```
offline 4054/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4941/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-radar-top50-1009-all-20261009-175556.log
```
- (c) SKIPPED lines: all seven inside the allowed set; `test_s3_c4_experiments.py:95` is the decorator line of `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F "def test_x14_…" …/test_s3_c4_experiments.py` → `96:`), the allowed skip.
- (c2) `dev forward: APPLIED 18:18:57` (log `:1095`). (f) `cobalt_dev: 0013 — F2 = F0` (log `:2016`).
- THE RELEASE: log `:2017–2022` `release-devdb-lock.sh deploy-radar-top50-1009` → `lock released`, `.env: removed` (the log stamps no time; released before 18:23:58 ET, my `date` after the completion notice). Verified: `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-radar-top50-1009" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) live-note `146/0`; no skip naming `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 2d580f26 — offline 4054/0 · with-DB 4941/0 · live-note 146/0 (18:23:58 ET)

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 106]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M` / `??` under `docs/40 - DevDocs/` only, plus `?? .claude/settings.json.bak` (see `## DECISIONS` 1); no staged line; no dirty `src/` `tests/` `ops/` `configs/` path but `rules.yaml` |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat b97d8ae8 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-radar-top50-1009` · `tag -d …` | 0 · 0 | — · `Deleted tag 'scratch-allow-probe-radar-top50-1009' (was b97d8ae8)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 0addceb8] scratch: …` · — · `b97d8ae8 docs(desk): deploy card 184 radar top-50` (HEAD back) |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-09-radar-top50` · `… refs/tags/pre-radar-top50-1009` | 1 · 1 | both free |

### STEP-D1 (18:24:24 ET)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 18:24:25 EDT)`; `OK   radar                    scanning (aftermarket), members 50`; `OK   com.cobalt.aset              running   loaded, pid 93108 [launchd probe]`; `OK   com.cobalt.radar             running   running 68 min, heartbeat fresh`; `OK   com.cobalt.agent             running   pid 22243 alive …`; the one non-OK row `AMB  com.cobalt.herdr             unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) [launchd probe]; runs outside launchd by declared interim …` (not RED; outside the set). No RED.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0; `13 trade_def(s) validated OK from the vault.`; `Placement (docs/PLACEMENT.md): tree clean.` `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 1.2 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = `93108`; `launchctl print gui/501/com.cobalt.radar` → `state = running`, `<radar pid>` = `93120`; `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ??         0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → seven `cards.expire: falling back to the session close (16:00:00)` INFO lines, last `2026-10-09 18:23:50.622 | INFO     | cobalt.radar.runner:resident:576 - radar cycle: scanning scan_id=1791584541783`.
- LOG BASELINES: `<a0>` `Started server process` aset.err = `53` · `<ta0>` Traceback aset.err = `2` · `<tr0>` Traceback radar.err = `0` · `<tc0>` TaxonomyConfigError = `0` · `<rp0>` `radar panel FAILED` = `18` · `<rpr0>` `radar pool refresh FAILED` = `60` · `<re0>` `radar S5 evaluate FAILED` = `42` · `<lc0>` `lifecycle card read failed` = `39`.
- `curl … http://127.0.0.1:5010/radar` → `200`. MARKERS again: `over_cap` → `0`, `Over cap` → `0` (= before).
- MIGRATIONS: none → `<RB>`, census and D1-M not run.

### STEP-D2
- D2.0 `git -C /Users/cobalt/cobalt add "…/deploy-radar-top50-1009.md"` · `commit -m "docs(report): deploy radar-top50-1009 — gate green on 2d580f26" …` → `[main 0d187b31] …  1 file changed, 137 insertions(+)`; `show --stat HEAD` → that one file. `rev-parse --short=8 main` → `0d187b31` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `rev-parse --short=8 HEAD` → `e4586978` = `<stack-final>`; `rev-parse --short=8 e4586978^2` → `0d187b31` = `<pre-merge>`; `merge-base --is-ancestor 2d580f26 e4586978` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 2d580f26 e4586978 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 1.2 h old` · `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 6632.8 MB` · `ssd: snapshot c655c69b — 0 new / 2 changed, 308.8 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `18:26:14` · `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 18:26:15 EDT)` (110 s after D1's 18:24:25; two earlier pairs at 18:26:05 and 18:26:11 were under 110 s, both GREEN); no RED.
- D2.6 `date` → `Fri Oct  9 18:26:19 EDT 2026`; `git -C /Users/cobalt/cobalt tag pre-radar-top50-1009` at `0d187b31` → exit 0.

### STEP-4 — the outage
| step | command | result |
|---|---|---|
| 4.1 | `date` | `Fri Oct  9 18:26:30 EDT 2026` = `<t down>` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.aset` · `launchctl print gui/501/com.cobalt.aset` | exit 0 · exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print gui/501/com.cobalt.radar` | exit 0 · exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | `0d187b31` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/radar-top50-1009` | `Updating 0d187b31..e4586978` / `Fast-forward` (4 files, 308+/2-) |
| 4.4 | — | `migrations applied: none` (MIGRATIONS: none) |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` (= `<jobs0>`); `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `launchctl print …aset` | exit 0 · `state = running`, `pid = 14669` (≠ 93108) |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `launchctl print …radar` | exit 0 · `state = running`, `pid = 14679` (≠ 93120) |
| 4.6 | `date` | `Fri Oct  9 18:26:44 EDT 2026` = `<t up>`; downtime 14 s |

### STEP-7 summary
- `<pre-merge>` `0d187b31` → `<stack-final>` `e4586978` (`<m0>` `b97d8ae8`, `<m1>` `2d580f26`).
- Tags: `pre-radar-top50-1009` at `0d187b31`; `deploy-2026-10-09-radar-top50` at `e4586978` (set after the green smoke).
- `<t down>` 18:26:30 · `<t up>` 18:26:44 · 14 s.
- uv sync line: none at 4.3–4.6 (the only uv build line this run was the gate worktree's first `.venv` at STEP-R).
- Proof cost: none in production (no migration); the gate's cobalt_dev proof `Proof cost: total 5.7 s` (log `:2009`).
- `migrations applied: none`. `<RB>`: none (no migration).
- Snapshot: `ssd: snapshot c655c69b`.
- `RESTARTS done: com.cobalt.aset com.cobalt.radar`.
- THE ROLLBACK STRING (the desk's): 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 e4586978` — `com.cobalt.aset` and `com.cobalt.radar` down first, up after. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
FIRST CALLS after `<t up>` 18:26:44: `<rp_up>` `radar panel FAILED` = `18` · `<rpr_up>` `radar pool refresh FAILED` = `60` · `<re_up>` `radar S5 evaluate FAILED` = `42` · `<lc_up>` `lifecycle card read failed` = `39` (all = D1).
- (a) [18:26:57] `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 14669` (NEW, ≠ 93108) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 14679` (NEW, ≠ 93120) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (agent outside the set: SAME pid). GREEN.
- (b) [18:27:00] `grep -c "Started server process" aset.err` → `54` (`<a0>` 53 + 1) · `tail -n 30 aset.err` → `INFO:     Started server process [14675]` … `2026-10-09 18:26:42.555 | INFO … voice_startup …` · `INFO:     Application startup complete.` · `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)` · Traceback aset.err `2` (= `<ta0>`) · Traceback radar.err `0` (= `<tr0>`) · TaxonomyConfigError `0` (= `<tc0>`). Radar tails: below.
- (c) [18:27:06] `curl … http://127.0.0.1:5010/` → `200` · `…/radar` → `200` · `…/radar\?frame=phone` → `200`. GREEN.
- (d) MARKERS [18:27:06] `grep -c -F "over_cap" …/radar_panel.py` → `7` (after `7`) · `grep -c -F "Over cap" …/radar_panel.py` → `1` (after `1`). GREEN.
- (s) SMOKE READS (same calls) → `over_cap` exit 0, `7` (≥1 green) · `Over cap` exit 0, `1` (≥1 green). GREEN.
- (f) [18:27:11] `COBALT_ENV=production uv run cobalt jobs restarts 0d187b31..e4586978` → exit 0, `RESTARTS: com.cobalt.aset com.cobalt.radar` (= STEP-R), no `UNCLASSIFIED` · `validate` → exit 0, `13 trade_def(s) validated OK from the vault.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`, `Placement (docs/PLACEMENT.md): tree clean.` GREEN.
- (e) read 1 [18:27:11] `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 18:27:14 EDT)`; `OK   com.cobalt.radar             running   running 1 min, heartbeat fresh`; `OK   com.cobalt.aset              running   loaded, pid 14669`; `OK   radar                    scanning (aftermarket), members 50`.
- (e) read 2 [18:29:07] `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 18:29:08 EDT)` (114 s after read 1); `OK   com.cobalt.radar             running   running 2 min, heartbeat fresh`. No RED not in `<hb0>`. GREEN.
- (b) radar tail 1 [18:28:15, `<t up>` + 91 s] `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` → eleven `cards.expire: falling back to the session close (16:00:00)` INFO lines stamped 18:28:11, then `2026-10-09 18:28:12.358 | INFO     | cobalt.radar.runner:resident:576 - radar cycle: scanning scan_id=1791584803210` — a cycle line after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → settled GREEN.
- (g) no migration: not run.
- (b) radar tail 2 [18:29:43, `<t up>` + 179–181 s] `tail -n 12 radar.err` → unchanged; last line `2026-10-09 18:28:12.358 | INFO … radar cycle: scanning scan_id=1791584803210`; no failure line (already settled at tail 1).
- (h) REVERT-READBACK [18:29:45, `<t up>` + 181 s] → `radar panel FAILED` `18` · `radar pool refresh FAILED` `60` · `radar S5 evaluate FAILED` `42` · `lifecycle card read failed` `39` (all = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`; none grew) · `/radar` curl `200` · Traceback radar.err `0`, aset.err `2` (= baseline). No census read (no migration). GREEN.

SMOKE: GREEN.

THE CHAIN: every check committed (P2: `92b08e65`) · the tips re-read (P3: `109bcfc0`, `b5b61eb0`) · the merged tree (T: `2d580f26`, clean, no migration) · RESTARTS derived (R: `com.cobalt.aset com.cobalt.radar`) · three suites green on `<m1>` `2d580f26` (G: offline 4054/0 · with-DB 4941/0 · live-note 146/0) · `<stack-final>` `e4586978` = `<m1>` + docs (D2.3: nothing) · the landed code (4.3: `Updating 0d187b31..e4586978` / `Fast-forward`) · markers (d: `7`, `1`) · no migration (g) · residents up on NEW pids after the merge (a: 14669, 14679) · radar cycling (b: 18:28:12; e: two GREEN reads) · the set's reads (s: `7`, `1`) · no new failure (h). The card surface (the `/radar` over-cap table as he sees it) is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK:
1. Every smoke row above carries its `date` and its output verbatim.
2. `merge-base --is-ancestor 109bcfc0 e4586978` → exit 0; `merge-base --is-ancestor b5b61eb0 e4586978` → exit 0; `rev-parse --short=8 main` → `e4586978`.
3. REVERT-READBACK shown at (h); every count, sha and `file:line` here was read from tool output this run.
4. STEP-T ran clean (`Merge made by the 'ort' strategy.`); `grep -c -F "<<<<<<<" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` → `0`.
- STEP-7.1 `git -C /Users/cobalt/cobalt tag deploy-2026-10-09-radar-top50` → exit 0 (after the green smoke).
- THE RELEASE: the lock was released by `gate.sh` at STEP-G; nothing held now.

## CONTINUE
next: STEP-D0 (gate green at 18:23:58 ET) — D0, D1, D2 done
OUTAGE STARTING 18:26:19 ET — residents of com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
next: none — outage ended 18:26:44 (residents up), smoke GREEN, STEP-7 closed.

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` (untracked) on `main` is not in D0's ACCEPTED list and not in its REFUSED list (not staged; not under `src/` `tests/` `ops/` `configs/`). Safe default taken: go on — it is untracked, outside the merge's paths, and `diff --stat <m0> main` outside docs printed nothing. [18:24 ET]

## RECORDS
- Downtime: `<t down>` 18:26:30 → `<t up>` 18:26:44 = 14 s (under 300 s).
- `cobalt_dev: 0013 (F2 = F0)` (gate log `:2016`); lock released by `gate.sh` (`lock released`, `.env: removed`).
- RETIRE OWED: none (STEP-C: no plist changed).
- Carried RED: none — every heartbeat read this run was `HEARTBEAT GREEN … nothing red`; the one non-OK row is `AMB com.cobalt.herdr … unmanaged` (amber, outside the set).
- REFUSED, not needed: none. Messages not followed: none.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-radar-top50-1009` and branch `deploy/radar-top50-1009`; the set's branch `ops/radar-top50-1009` and its worktree if any.
- Equal-tree clause did not hold (main moved since the branch base: `bare-guard.py`, `stop-guard.py`, `radar_panel.py`, `web.py` and tests), so the gate ran whole: offline 4054 / with-DB 4941 vs the check's 4039 / 4926.
- L74: the harness attribution reminder asking for a `Claude-Session:` commit line — recorded under `## L74`, not acted on.
- (card) radar-top50-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-top50-check-2026-10-09.md` last line: CHECK DONE · job: radar-top50-1009 · pass: 1 · tip: 109bcfc0 · house A: Sol FINDINGS: 2 · findings: 9 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 4 · suites: offline 4039/0 · with-DB 4926/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 153816
- (card) radar-top50-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-top50-1009` → `b5b61eb0`; code tip `109bcfc0`
- (card) written by deploy-card.sh at 2026-10-09 17:53 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-09-radar-top50 e4586978 | set: none | migrations: none | gate: offline 4054/0 · with-DB 4941/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 193331
