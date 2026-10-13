# deploy aset-orphan-1010 (attempt 2) · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED `ops/aset-orphan-1010` (code 1987849b, head f72dbb9a): `main` 182c35fc → 014fe4cf, tag `deploy-2026-10-10-aset-orphan-attempt2`.
- Gate GREEN on 14595934: offline 4317/0 · with-DB 5220/0 · live-note 146/0. No migration.
- RESTARTS com.cobalt.aset only: down 00:26:15, up 00:26:30 (15 s); pid 14738 → 40377, no orphan.
- Smoke GREEN. Start script now execs python itself: uvicorn `Started server process [40377]` = the launchd pid.

## L74
- One system block during this session asked for a `Claude-Session:` trailer on commits. Recorded as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/256-deploy-aset-orphan-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/256-deploy-aset-orphan-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/256-deploy-aset-orphan-card.md" · 0 · a6b10eeff63851f840793e6ef3bd05eabf60edb6
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/256-deploy-aset-orphan-card.md" · 0 · nothing
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
| FIRST LAUNCH | `ls -la ".../reports/deploy-aset-orphan-1010-attempt2.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Mon Oct 12 23:52:14 EDT 2026` |
| P2 check last line | `tail -n 3 ".../reports/aset-orphan-check-2026-10-10.md"` | 0 | `CHECK DONE · job: aset-orphan-1010 · pass: 1 · tip: 1987849b · … · held unfixed: 0 · open: 3 · … · suites: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset · files opened: 13 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 163668` — carries `held unfixed: 0` and `ready: YES`; `tip: 1987849b` = row's code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/aset-orphan-check-2026-10-10.md"` | 0 | `af0b107247fcba531187d2d4b8eec553a6187f4b` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/aset-orphan-check-2026-10-10.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 1987849b` | 0 | `1987849b` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/aset-orphan-1010` | 0 | `f72dbb9a` (= TIP) |
| P3 ancestry | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 1987849b f72dbb9a` | 0 | — |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 1987849b f72dbb9a -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate status | `git -C <GATE> status --short --branch` | 0 | `## deploy/aset-orphan-1010-attempt2` |
| P5 `<m0>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `a6b10eef` |
| P5 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor a6b10eef main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/aset-orphan-1010-attempt2` | 0 | empty |
| P6 marker | `grep -c -F 'exec "$REPO_ROOT/.venv/bin/python" -m cobalt.aset' /Users/cobalt/cobalt/ops/start_aset.sh` | 1 | `0` (= before) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main f72dbb9a -- src/cobalt/db_migrations` | 0 | ` src/cobalt/db_migrations/cli.py \| 2 --` — CODE, no migration file; passes `MIGRATIONS: none` |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 14738` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 22724` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 14763).` |

## THE TREE
- `git -C <GATE> merge --no-edit f72dbb9a` → `Merge made by the 'ort' strategy.` (5 files: aset-orphan-build report, `ops/README.md`, `ops/start_aset.sh`, `tests/cobalt/test_jobs_reads.py`, `tests/ops/test_launchd_orphan.py`).
- `<m1>`: `git -C <GATE> rev-parse --short=8 HEAD` → `14595934`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent a6b10eef..deploy/aset-orphan-1010-attempt2` → `14595934 Merge commit 'f72dbb9a' into deploy/aset-orphan-1010-attempt2`.
- `merge-base --is-ancestor 1987849b deploy/aset-orphan-1010-attempt2` → exit 0; `merge-base --is-ancestor f72dbb9a deploy/aset-orphan-1010-attempt2` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat a6b10eef deploy/aset-orphan-1010-attempt2 -- src/cobalt/db_migrations` → nothing (no migration; = `MIGRATIONS: none`).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat a6b10eef deploy/aset-orphan-1010-attempt2 -- configs ops` →
```
 ops/README.md     |  2 +-
 ops/start_aset.sh | 17 +++++++++++------
 2 files changed, 12 insertions(+), 7 deletions(-)
```
  No plist added, modified or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/reports/aset-orphan-build-2026-10-10.md	A	DOCS	-
ops/README.md	M	operations documentation; no resident	-
ops/start_aset.sh	M	resident reads	com.cobalt.aset
tests/cobalt/test_jobs_reads.py	M	test/documentation; no resident	-
tests/ops/test_launchd_orphan.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset
```
(preceded by uv lines: `Creating virtual environment at: .venv` … `Installed 254 packages in 664ms`). No UNCLASSIFIED row. `<restart set>` = `com.cobalt.aset`.

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 1987849b 14595934 -- . ":(exclude)docs"` → 59 files changed (main moved since the check: ops/desk, src/cobalt/db_apply.py, backup, tests …). Clause does not hold → the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 16.92s` (0 failed; skips all `Postgres env settings not available` / `requires_db`).
- Deselects: build report `aset-orphan-build-2026-10-10.md:155` — "no `--deselect`: this build adds no with-DB test". `TICKERS: none`, no `--migration`.
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-aset-orphan-1010-attempt2 all --deploy` (background) → exit 0. Verdict lines WHOLE:
```
offline 4317/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5220/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-aset-orphan-1010-attempt2-all-20261012-235408.log
```
- SKIPPED judgment: all seven inside the allowed set. `test_s3_c4_experiments.py:95` is the decorator of `def test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F` → line 96). `test_replay_line.py:266` names `COBALT_TEST_LIVE_DRC`. These skips are the pass-1 lines; the live-note leg (146/0) runs them with `COBALT_LIVE_VAULT_ROOT`.
- (b) log `902:F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; proof-only at 0013, `nothing CHANGED` (log 954).
- (c2) `dev forward: APPLIED 00:18:32` (log 1117); proof tables `content UNCHANGED on every table` (log 1185, 2027).
- (f) `cobalt_dev: 0013 — F2 = F0` (log 2089); final fingerprint `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` (log 2086) = F0.
- THE RELEASE: log 2090–2095 `release-devdb-lock.sh … → lock released [exit 0]`, `.env: removed` (L76 lock released; the log prints no time — read before 00:23:37). `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` listed.

GATE GREEN on 14595934 — offline 4317/0 · with-DB 5220/0 · live-note 146/0 (`date` → `Tue Oct 13 00:23:37 EDT 2026`)

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN branch | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 24]` |
| MAIN porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; ` M` ×6 and `??` under `docs/40 - DevDocs/`; `?? .claude/settings.json.bak` (see DECISIONS); no staged line; no dirty `src/` `tests/` `ops/` `configs/` |
| moved since cut | `git -C /Users/cobalt/cobalt diff --stat a6b10eef main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe tag | `tag scratch-allow-probe-aset-orphan-1010` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-aset-orphan-1010' (was a6b10eef)` |
| probe commit | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` | 0 | `[main 08437d7a] scratch: allowlist probe (reverted next line)` |
| probe reset | `reset --soft HEAD~1` then `log --oneline -1` | 0 / 0 | `a6b10eef docs(desk): RECUT aset-orphan-1010 attempt 2` |
| TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-10-aset-orphan-attempt2` | 1 | absent |
| pre-tag | `rev-parse --verify --quiet refs/tags/pre-aset-orphan-1010` | 1 | absent |

### STEP-D1 (baseline)
- `date` → `Tue Oct 13 00:24:05 EDT 2026`. `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-13 00:24:06 EDT)`; `OK   com.cobalt.aset              running   loaded, pid 14738`; `OK   com.cobalt.radar             running   running 37 min, heartbeat fresh`; `OK   radar                    idle (overnight)`; `AMB  com.cobalt.herdr             unmanaged AMBER …` (declared interim). No RED.
- `<val0>`: `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>`: `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 15 label(s), exact match.`
- `backup status` → `newest snapshot: 0.6 h old` (ssd ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = `14738`; `…com.cobalt.radar` → `state = running`, `<radar pid>` = `22724`; `cobalt.sh status` → `Cobalt is ONLINE (PID: 14763).`; `ps -p 14763` → `14763 ??         0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, last `2026-10-13 00:24:06.170`; no traceback.
- Counts: `<a0>` Started server process (aset.err) `278` · `<ta0>` Traceback (aset.err) `217` · `<tr0>` Traceback (radar.err) `0` · `<tc0>` TaxonomyConfigError `0` · `<rp0>` radar panel FAILED `18` · `<rpr0>` radar pool refresh FAILED `60` · `<re0>` radar S5 evaluate FAILED `43` · `<lc0>` lifecycle card read failed `39`.
- `curl … /radar` → `200`. MARKER `grep -c -F 'exec "$REPO_ROOT/.venv/bin/python" -m cobalt.aset' ops/start_aset.sh` → `0` (= before).
- `MIGRATIONS: none` → no `<RB>`, no census, no D1-M.

### STEP-D2
- D2.0 `add` + `commit … -- "docs/40 - DevDocs/reports/deploy-aset-orphan-1010-attempt2.md"` → `[main 182c35fc] docs(report): deploy aset-orphan-1010 — gate green on 14595934`; `show --stat HEAD` → that one file, `144 insertions(+)`. `<pre-merge>` = `182c35fc`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `014fe4cf`; `rev-parse --short=8 014fe4cf^2` → `182c35fc` = `<pre-merge>`; `merge-base --is-ancestor 14595934 014fe4cf` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 14595934 014fe4cf -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` before → `newest snapshot: 0.6 h old`. `backup run` → `backup: cobalt_brain dumped, 7133.8 MB` · `ssd: snapshot af4c120d — 0 new / 2 changed, 26.4 MB added, 1 pruned`; `backup status` after → `newest snapshot: 0.0 h old`.
- D2.5 `date` → 00:25:45 / 00:25:52 / 00:25:57 (clock filler reads 00:25:48, 00:25:54 all GREEN); read at `2026-10-13 00:25:59 EDT` (113 s after D1's 00:24:06) → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red`, aset pid 14738, radar `running 39 min, heartbeat fresh`. No new RED.
- D2.6 `date` → `Tue Oct 13 00:26:04 EDT 2026`; `git -C /Users/cobalt/cobalt tag pre-aset-orphan-1010` at `182c35fc` → exit 0.

### STEP-4 — the outage (`<restart set>` = com.cobalt.aset)
| step | command | exit | result |
|---|---|---|---|
| 4.1 | `date` | 0 | `<t down>` = `Tue Oct 13 00:26:15 EDT 2026` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.aset` | 0 | — |
| 4.2 | `launchctl print gui/501/com.cobalt.aset` | 113 | `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 ORPHAN-CLEAN (1) | `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh aset` | 0 | `orphan-clean: aset · none found` → clean, no kill |
| DEPLOY PROOF | `ps -p 14738` | 1 | `  PID TTY           TIME CMD` (header only) |
| 4.2 agent | not in the set | — | no call |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | 0 | `182c35fc` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/aset-orphan-1010-attempt2` | 0 | `Updating 182c35fc..014fe4cf` / `Fast-forward` (5 files, 362+/8−) |
| 4.4 | — | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>` |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | — |
| 4.6 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `pid = 40377` (≠ 14738) |
| 4.6 | `date` | 0 | `<t up>` = `Tue Oct 13 00:26:30 EDT 2026` — downtime 15 s |

### STEP-7 close
- `<pre-merge>` `182c35fc` → `<stack-final>` `014fe4cf` (`git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `014fe4cf`).
- Tags: `pre-aset-orphan-1010` at 182c35fc; `deploy-2026-10-10-aset-orphan-attempt2` at 014fe4cf (set after the green smoke, exit 0).
- `<t down>` 00:26:15 / `<t up>` 00:26:30 / 15 s. uv sync line (aset start, aset.err): `Resolved 264 packages in 2ms` · `Audited 254 packages in 4ms`. Proof cost: no production migration (gate's dev proof `total 5.5 s`, log 2082).
- `migrations applied: none` · `<RB>`: none (no migration) · snapshot `af4c120d` (ssd).
- `RESTARTS done: com.cobalt.aset`.
- THE ROLLBACK STRING: (1) CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 014fe4cf`, com.cobalt.aset down first, up after. (2) SCHEMA: none (no migration). (3) RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
- FIRST CALLS after `<t up>`: `<rp_up>` radar panel FAILED `18` · `<rpr_up>` radar pool refresh FAILED `60` · `<re_up>` radar S5 evaluate FAILED `43` · `<lc_up>` lifecycle card read failed `39` (= D1).
- (a) `date` 00:26:45 · `launchctl print gui/501/com.cobalt.aset` (4.6) → `state = running`, pid `40377` NEW (≠ 14738) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, pid `22724` SAME (outside the set) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 14763).` (same pid; agent outside the set).
- (b) `grep -c "Started server process" aset.err` → `279` (> 278, ≤ 280) · `tail -n 30 aset.err` → `INFO:     Started server process [40377]` then `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)` (the uvicorn pid = the launchd pid: the start script execs python itself) · Traceback aset.err `217` = `<ta0>` · Traceback radar.err `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`.
- (c) `curl … /` → `200` · `curl … /radar` → `200` · `curl … /radar\?frame=phone` → `200`.
- (d) MARKER `grep -c -F 'exec "$REPO_ROOT/.venv/bin/python" -m cobalt.aset' /Users/cobalt/cobalt/ops/start_aset.sh` → `1` (= after). DEPLOY PROOF: `ps -p 14738` after 4.2 → header only; 4.6 aset `state = running` pid 40377.
- (e) first: `date` 00:26:57 · heartbeat `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-13 00:26:58 EDT)`; `com.cobalt.aset running loaded, pid 40377`; `com.cobalt.radar running running 40 min, heartbeat fresh`.
- (f) `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` · `COBALT_ENV=production uv run cobalt jobs restarts 182c35fc..014fe4cf` → exit 0, `RESTARTS: com.cobalt.aset` = STEP-R, no UNCLASSIFIED.
- (g) no migration.
- (s) the start script's direct exec line → `1` (exit 0, ≥ 1): GREEN.
- (b) spaced radar tails: `date` 00:28:00 (+90 s) `tail -n 12 radar.err` → last `2026-10-13 00:27:26.206 … radar cycle: idle:overnight scan_id=None` (after `<t up>`, no S5 / lifecycle failure, no traceback) → GREEN settled. Second tail at 00:29:30 → last `2026-10-13 00:29:06.228 … radar cycle: idle:overnight scan_id=None`.
- (e) second: `date` 00:28:51 · heartbeat `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-13 00:28:53 EDT)` (115 s after the first); `com.cobalt.radar running running 41 min, heartbeat fresh`; aset pid 40377. No RED (clock-filler reads 00:27:19 to 00:29:26 also all GREEN).
- (h) REVERT-READBACK `date` 00:29:30 (`<t up>` + 180 s): radar panel FAILED `18` · pool refresh FAILED `60` · S5 evaluate FAILED `43` · lifecycle card read failed `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none growing) · `curl … /radar` → `200` · no census read (no migration).
- DEPLOY PROOF re-read after the smoke: `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 40377` (same pid).

THE CHAIN: check committed `af0b1072` with `held unfixed: 0 · ready: YES` (P2) → tips 1987849b / f72dbb9a re-read (P3) → merged clean at 14595934 (T) → RESTARTS `com.cobalt.aset` by the tool (R) → three suites green on 14595934 (G) → `014fe4cf` = 14595934 + docs (D2.3) → landed `Fast-forward 182c35fc..014fe4cf` (4.3) → marker 0 → 1 (d) → no migration (g) → aset up on a new pid, radar and agent unchanged (a) → radar cycling 00:27:26, 00:29:06; heartbeats GREEN (b, e) → direct exec line present (s) → no failure count grew (h). The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK: (1) every smoke row above is quoted with its `date`. (2) `merge-base --is-ancestor 1987849b 014fe4cf` → exit 0; `merge-base --is-ancestor f72dbb9a 014fe4cf` → exit 0. (3) (h) shown; every count, sha and line above was read from this run's tool output. (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), no conflict.

## CONTINUE
- next: STEP-D2 (gate green at 00:23:37; D0, D1 done)
- OUTAGE STARTING 00:26:04 — residents of com.cobalt.aset going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- OUTAGE ENDED 00:26:30 — aset up (pid 40377), merge landed 182c35fc..014fe4cf.
- Smoke GREEN 00:29:30; tagged; closed. next: none (stop line written).

## DECISIONS
- D0 porcelain: `?? .claude/settings.json.bak` is neither in the ACCEPTED list nor in the REFUSED paths (`src/` `tests/` `ops/` `configs/`). Safe default taken: not refused, not touched; the deploy goes on. Desk to clear the stray backup file.

## RECORDS
- Downtime: aset 15 s (00:26:15 → 00:26:30); under 300 s.
- No `REFUSED, not needed` line; no `CONTINUE` message arrived; no message from another session followed.
- `cobalt_dev: 0013 (F2 = F0)` — gate log line 2089; lock released, `.env: removed`.
- RETIRE OWED: none (no plist removed).
- Carried RED: none. `<hb0>` and every smoke heartbeat read `HEARTBEAT GREEN … nothing red`; radar `idle (overnight)`.
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-aset-orphan-1010-attempt2` and branch `deploy/aset-orphan-1010-attempt2`; the set's branch `ops/aset-orphan-1010` and its worktree; tag `pre-aset-orphan-1010` kept as the rollback point.
- The gate created `.venv` in the gate worktree (`uv` at STEP-R: `Creating virtual environment at: .venv`); it goes with the worktree cleanup.
- Card `## RECORDS`, copied:
  - aset-orphan-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/aset-orphan-check-2026-10-10.md` last line: CHECK DONE · job: aset-orphan-1010 · pass: 1 · tip: 1987849b · house A: Sol FINDINGS: 1 · findings: 10 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 3 · house B: Gemini FINDINGS: 5 · suites: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset · files opened: 13 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 163668
  - aset-orphan-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/aset-orphan-1010` → `f72dbb9a`; code tip `1987849b`
  - written by deploy-card.sh at 2026-10-10 11:29 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one system block asked for a `Claude-Session:` commit trailer; recorded under `## L74`, not acted on.
- Push is his (L55): `main` is local at 014fe4cf plus this report commit; tags `pre-aset-orphan-1010` and `deploy-2026-10-10-aset-orphan-attempt2` are local.

DEPLOYED deploy-2026-10-10-aset-orphan-attempt2 014fe4cf | set: none | migrations: none | gate: offline 4317/0 · with-DB 5220/0 · live-note 146/0 | RESTARTS: com.cobalt.aset | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 193777
