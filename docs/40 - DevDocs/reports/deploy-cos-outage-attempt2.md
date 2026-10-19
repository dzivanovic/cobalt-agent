# deploy cos-outage-attempt2 — set: cos-outage — migrations: none

## §0 Headline
Deploy green: `main` moved `44d3b598` → `a5e07866` (tag `deploy-2026-10-19-cos-outage-attempt2`), shipping `ops/cos-outage-1018` (deploy-outage.sh / deploy-step0.sh learn `com.cobalt.cos`).
Gate green on `2f8a899b`: offline 8667/0 · with-DB 5610/0 · live-note 147/0. The 798 attempt's G (c) red did not recur.
`RESTARTS: none` and `migrations: none`, so no resident went down (downtime none). Smoke GREEN.
1 decision (closed by proof), 0 for Dejan.

## L74
A system reminder asked for a `Claude-Session:` line in commits. This is recorded once and was not acted on, so commits carry `Co-Authored-By` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/806-deploy-cos-outage-attempt2-card.md"`, output quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/806-deploy-cos-outage-attempt2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/806-deploy-cos-outage-attempt2-card.md" · 0 · b6523f3170aff7f90da89ed08e40563152f6991b
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/806-deploy-cos-outage-attempt2-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la ".../reports/deploy-cos-outage-attempt2.md"` → `No such file or directory`.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 date | `date` | 0 | `Mon Oct 19 02:01:43 EDT 2026` — outside 21:30-22:30 |
| P2 tail | `tail -n 3 ".../cos-outage-1018-check-2026-10-18.md"` | 0 | `CHECK DONE · job: cos-outage-1018 · pass: 1 · tip: de3e15c8 · … · held unfixed: 0 · open: 0 · … · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165134` (tip = row's code tip) |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/cos-outage-1018-check-2026-10-18.md"` | 0 | `e7ef198a06256a5b862da217e331ac9cb2dc69d4` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/cos-outage-1018-check-2026-10-18.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 de3e15c8` | 0 | `de3e15c8` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-outage-1018` | 0 | `b5d62f17` (= TIP) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor de3e15c8 b5d62f17` | 0 | — |
| P3 docs-only | `git -C /Users/cobalt/cobalt diff --stat de3e15c8 b5d62f17 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no holder) |
| P5 status | `git -C /Users/cobalt/cobalt-wt/deploy-cos-outage-attempt2 status --short --branch` | 0 | `## deploy/cos-outage-attempt2` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-cos-outage-attempt2 rev-parse --short=8 HEAD` | 0 | `b6523f31` = `<m0>` (main's tip at launch, `git` recent commits) |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/cos-outage-attempt2` | 0 | empty |
| P6 marker 1 | `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/ops/desk/deploy-outage.sh` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` | 1 | `0` = before |
| P7 stat | `git -C /Users/cobalt/cobalt diff --stat main b5d62f17 -- src/cobalt/db_migrations` | 0 | `0025_dml_roles.rollback.sql \| 33 ---`, `0025_dml_roles.sql \| 77 ---`, `__init__.py \| 8 ---` (deletions only: main's 0025, landed by dml-roles after the branch was cut) |
| P7 registry | `git -C /Users/cobalt/cobalt diff main b5d62f17 -- src/cobalt/db_migrations/__init__.py` | 0 | only `-` lines for 0025 in docstring, `FORWARD` and `REVERSE`; no `+` line |
| P7 head's own | `git -C /Users/cobalt/cobalt diff --stat main...b5d62f17 -- src/cobalt/db_migrations` | 0 | nothing: the head adds no migration, so `MIGRATIONS: none` holds. See DECISIONS 1 |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 89330` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 86221` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 89351).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-cos-outage-attempt2 merge --no-edit b5d62f17` → `Merge made by the 'ort' strategy.` (6 files, 416 insertions, 7 deletions: `ops/desk/deploy-outage.sh`, `ops/desk/deploy-step0.sh`, `tests/ops/test_deploy_outage.py`, `tests/ops/test_deploy_step0.py`, two docs).
- `rev-parse --short=8 HEAD` → `<m1>` = `2f8a899b`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent b6523f31..deploy/cos-outage-attempt2` → `2f8a899b Merge commit 'b5d62f17' into deploy/cos-outage-attempt2`.
- `merge-base --is-ancestor de3e15c8 deploy/cos-outage-attempt2` → exit 0; `merge-base --is-ancestor b5d62f17 deploy/cos-outage-attempt2` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat b6523f31 deploy/cos-outage-attempt2 -- src/cobalt/db_migrations` → nothing: there is no migration path, so `MIGRATIONS: none` holds, 0025 is untouched by the merge, and DECISIONS 1 is closed by this proof.
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat b6523f31 deploy/cos-outage-attempt2 -- configs ops` → `ops/desk/deploy-outage.sh | 11 ++++++-----` · `ops/desk/deploy-step0.sh | 4 ++--` · `2 files changed, 8 insertions(+), 7 deletions(-)`. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" b6523f31 deploy/cos-outage-attempt2` → `STEP-C: ADMITTED 0`. `<launchd set>` is empty, and so is `<deferred set>`.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after a `uv` venv creation: `Creating virtual environment at: .venv` · `Installed 256 packages in 761ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/cos-outage-1018-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-outage-1018-build-2026-10-18.result	A	DOCS	-
ops/desk/deploy-outage.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_outage.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` is EMPTY, `<deferred set>` is empty and `<launchd set>` is empty. There is no `UNCLASSIFIED` row. With `MIGRATIONS: none`, an empty set is allowed.

## L68 GATE
- THE EQUAL-TREE CLAUSE does not hold: the check's stop line carries `with-DB 0/0`, so the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 listed files>` → `264 passed, 163 skipped in 19.69s` (0 failed; every skip is a with-DB `Postgres env settings not available` / `requires_db` skip).
- Deselects: none. The set's build report (`cos-outage-1018-build-2026-10-18.md`) names no with-DB deselect; its `deselected` lines are `-k` selections. `TICKERS: none` and no `--migration` were passed.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-cos-outage-attempt2 all --deploy --deploy-gate` (background) → exit 0. Its verdict lines, whole:
```
tests/ops: run (deploy gate)
offline 8667/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5610/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-cos-outage-attempt2-all-20261019-020352.log
```
- (a) offline `8667/0`; the W line is `tests/ops: run (deploy gate)`.
- (c) pass 1 skips: all eight are inside the allowed set. That covers `test_cards_picks.py:388` and `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365` and `test_predicate.py:262`. It also covers the `test_playbook_live.py` live-vault skip, the `test_replay_line.py` `COBALT_TEST_LIVE_DRC` skip and the `test_s3_c4_experiments.py` live-template skip, each with its listed reason.
- (c2) `grep -n -F "dev forward" <log>` → `1247:dev forward: APPLIED 02:44:28`. `grep -n -F "CHANGED" <log>` → only `nothing CHANGED` and `content UNCHANGED on every table` lines, so there is no `CHANGED` row.
- (c3) with-DB `5610/0`.
- (f) `cobalt_dev: 0013 — F2 = F0` (log 2289).
- THE RELEASE: log `2290: $ sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh deploy-cos-outage-attempt2` → `lock released` → `.env: removed`. `ls -la <GATE>/.env` → No such file. `grep -c -x -F "deploy-cos-outage-attempt2" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent). `.env: removed (L76 lock released; the log carries no timestamp, gate end read by `date` at 02:49:46 ET)`.
- (e) live-note `147/0`; the only skip naming `COBALT_TEST_LIVE_DRC` is inside the set.
- The 798 attempt's G (c) red (`test_db_credentials.py::…::test_it_is_a_member_of_all_three_side_roles`) did not recur: pass 1 has 0 failed.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 2f8a899b

## Deploy table
STEP-D0 (02:49 ET):
- `git -C /Users/cobalt/cobalt status --short --branch` → first line `## main...origin/main [ahead 22]`. `status --porcelain` → only ` M` / `??` under `docs/40 - DevDocs/`, ` M .claude/settings.json`, and `?? .claude/settings.json.bak`. There is no staged line and no dirty `src/`, `tests/`, `ops/` or `configs/` path. The `.bak` is untracked outside both lists and is recorded under `## RECORDS`.
- `git -C /Users/cobalt/cobalt diff --stat b6523f31 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- Allowlist probe: `tag scratch-allow-probe-cos-outage-attempt2` → ok · `tag -d …` → `Deleted tag 'scratch-allow-probe-cos-outage-attempt2' (was b6523f31)` · `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 7364e588] …` · `reset --soft HEAD~1` → ok · `log --oneline -1` → `b6523f31 docs(desk): card 806 cos-outage-attempt2 recut` (HEAD back).
- `rev-parse --verify --quiet refs/tags/deploy-2026-10-19-cos-outage-attempt2` → exit 1 · `refs/tags/pre-cos-outage-attempt2` → exit 1.

STEP-D1 (`date` → `Mon Oct 19 02:50:16 EDT 2026`):
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT GREEN — 17 job(s), 12 probe(s), nothing red  (2026-10-19 02:50:17 EDT)`. That includes `OK radar idle (overnight)`, `OK com.cobalt.aset running loaded, pid 89330`, `OK com.cobalt.agent running pid 89351 alive` and `OK com.cobalt.radar running running 59 min, heartbeat fresh`. `AMB com.cobalt.herdr unmanaged` is the declared interim. `com.cobalt.prefill-refresh` and `com.cobalt.playbook` read `OWED (deferred bootstrap)` (OK). There is no RED.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`. `<jobs0>` = `Jobs (F17): 17 registered — 6 resident, 11 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 1.2 h old` (ssd ARMED; b2 off).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = `89330`. `…/com.cobalt.radar` → `state = running`, `<radar pid>` = `86221`. `cobalt.sh status` → `Cobalt is ONLINE (PID: 89351).`, and `ps -p 89351` → listed (`uv run src/cobalt_agent/main.py`).
- `tail -n 8 radar.err` → `radar cycle: idle:overnight scan_id=None` every ~100 s, last `02:49:10.501`, with no traceback.
- Log baselines: `<a0>` 283 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. Markers again: `deploy-outage.sh` `0`, `deploy-step0.sh` `0` (before).
- THE LAUNCHD SET: empty, so there is nothing to read. There is no migration either, so no `<RB>`, census or proof-only.

STEP-D2:
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved b6523f31 "<card>"` → nothing. Report committed: `[main 44d3b598] docs(report): deploy cos-outage-attempt2 — gate green on 2f8a899b` (1 file, 145 insertions). `show --stat HEAD` lists that one file. `<pre-merge>` = `44d3b598`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `a5e07866`; `rev-parse --short=8 a5e07866^2` → `44d3b598` = `<pre-merge>`; `merge-base --is-ancestor 2f8a899b a5e07866` → exit 0.
- D2.3 `diff --stat 2f8a899b a5e07866 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs only).
- D2.4 `backup status` → `newest snapshot: 1.2 h old`. `backup run` (foreground) → `backup: cobalt_brain dumped, 8899.3 MB` · `ssd: snapshot eeb4daad — 0 new / 2 changed, 9.8 MB added, 1 pruned`. `backup status` → `newest snapshot: 0.0 h old`. Snapshot id: `eeb4daad`.
- D2.5 `date` → `02:52:09`, `heartbeat show` → `HEARTBEAT GREEN — 17 job(s), 12 probe(s), nothing red  (2026-10-19 02:52:09 EDT)`, 112 s after D1's 02:50:17. There is no new RED.
- D2.6 `date` → `Mon Oct 19 02:52:14 EDT 2026`. `git -C /Users/cobalt/cobalt tag pre-cos-outage-attempt2` → ok; `rev-parse --short=8 pre-cos-outage-attempt2` → `44d3b598`.

STEP-4 (`<restart set>` EMPTY):
- 4.1 `date` → `Mon Oct 19 02:52:27 EDT 2026` = `<t down>`. No resident goes down, so `<t up>` is 4.3's date, `02:52:27`.
- 4.2: nothing (empty set; aset not in it, so no orphan-clean; agent not in it).
- 4.3 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `44d3b598` = `<pre-merge>`. `git -C /Users/cobalt/cobalt merge --ff-only deploy/cos-outage-attempt2` → `Updating 44d3b598..a5e07866` / `Fast-forward` (6 files, 416 insertions(+), 7 deletions(-)).
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 17 registered — 6 resident, 11 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6: nothing to bootstrap. Downtime: none.
- 4.6L: `<launchd set>` empty, so nothing.

STEP-7:
| item | value |
|---|---|
| `<pre-merge>` → `<stack-final>` | `44d3b598` → `a5e07866` (`git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `a5e07866`) |
| tags | `pre-cos-outage-attempt2` → `44d3b598`; `deploy-2026-10-19-cos-outage-attempt2` → `a5e07866` (set after green smoke) |
| `<t down>` / `<t up>` / seconds | none (empty `<restart set>`; merge at 02:52:27) |
| uv sync line | none at 4.3/4.4 (no migration). The gate worktree's first `uv run` created its `.venv` (`Installed 256 packages in 761ms`) |
| proof cost | n/a (no migration) |
| migrations applied | none |
| `<RB>` before / after | n/a |
| snapshot | `eeb4daad` (ssd) |
| RESTARTS done | none |
| LAUNCHD done | none; BOOTSTRAP OWED: none |

THE ROLLBACK STRING (the desk's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 a5e07866`. That is ONE revert of the main-into-gate merge. `<restart set>` and `<launchd set>` are empty, so no resident goes down and no label is touched.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
`<t up>` = 02:52:27 (empty set; 4.3's date).
- FIRST CALLS: `grep -c "radar panel FAILED" aset.err` → `18` = `<rp_up>`, `radar pool refresh FAILED` → `60` = `<rpr_up>`, `radar S5 evaluate FAILED` → `43` = `<re_up>`, `lifecycle card read failed` → `39` = `<lc_up>`. All four equal D1.
- (a) `date` 02:52:43 · aset `state = running`, `pid = 89330` (SAME as D1; outside the set) · radar `state = running`, `pid = 86221` (SAME) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 89351).` (SAME). GREEN.
- (b) `date` 02:52:47 · `Started server process` → `283` = `<a0>` (aset outside the set). `tail -n 30 aset.err` shows the last start is `Started server process [89330]` then `Uvicorn running on http://127.0.0.1:5010`, with no new lines since. Traceback aset `217` = `<ta0>`, radar `0` = `<tr0>`, TaxonomyConfigError `0` = `<tc0>`. Radar tails are below.
- (c) `date` 02:52:51 · `/` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200`. GREEN.
- (d) `date` 02:52:54 · `grep -c -F "com.cobalt.cos" …/deploy-outage.sh` → `5` (after `5`) · `…/deploy-step0.sh` → `1` (after `1`). GREEN.
- (f) `date` 02:53:00 · 4.5's `validate` → exit 0, `<jobs0>` unchanged. `COBALT_ENV=production uv run cobalt jobs restarts 44d3b598..a5e07866` → exit 0, the same six rows, `RESTARTS: none` = STEP-R's `<restart set>`, no `UNCLASSIFIED`. GREEN.
- (g) no migration.
- (s) Both card reads quote the gate's run (the card's rule; no test runs in production). Gate log line 939 `$ uv run pytest -q -rs -p no:cacheprovider tests/ops` (this covers `tests/ops/test_deploy_outage.py` and `tests/ops/test_deploy_step0.py`) → line 1008 `4013 passed, 1 xfailed, 16 warnings in 876.04s (0:14:36)`, `[exit 0]`. That is `0 failed` for both reads. GREEN. `<launchd set>` empty, so there is no dry run.
- (e) read 1: `date` 02:53:11 · `HEARTBEAT GREEN — 17 job(s), 12 probe(s), nothing red  (2026-10-19 02:53:12 EDT)`; `com.cobalt.radar running running 62 min, heartbeat fresh`. Read 2: `date` 02:55:03 · `HEARTBEAT GREEN — 17 job(s), 12 probe(s), nothing red  (2026-10-19 02:55:06 EDT)`, 114 s after read 1; `com.cobalt.radar running running 64 min, heartbeat fresh`. There is no RED and nothing new versus `<hb0>`. The clock between reads was filled with `date` + `heartbeat show` pairs, all GREEN. GREEN.
- (b) radar tails: `date` 02:54:02 (t_up + 95 s) · `tail -n 12 radar.err` → last line `2026-10-19 02:52:30.546 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`. That cycle line is stamped after `<t up>` 02:52:27, with no `radar S5 evaluate FAILED`, no `lifecycle card read failed` and no traceback, so (b) is settled GREEN. The tail at `date` 02:55:29 (t_up + 182 s) adds `02:54:10.562 … radar cycle: idle:overnight scan_id=None`.
- (h) REVERT-READBACK at `date` 02:55:29 (≥ t_up + 180 s): `radar panel FAILED` `18` · `radar pool refresh FAILED` `60` · `radar S5 evaluate FAILED` `43` · `lifecycle card read failed` `39`. All equal `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, with no growth. `/radar` curl → `200`. No census reads on the card. GREEN.

THE CHAIN: every check committed (P2, `e7ef198a`); the tips re-read (P3 `de3e15c8` / `b5d62f17`); the merged tree (T, `2f8a899b`, no migration path); RESTARTS derived (R, none); three suites green on `2f8a899b` (G: offline 8667/0 · with-DB 5610/0 · live-note 147/0); `<stack-final>` `a5e07866` = `<m1>` + docs (D2.3); the landed code (4.3 fast-forward `44d3b598..a5e07866`); markers `5`/`1` (d); no migration (g); residents unchanged and running after the merge (a); radar cycling (b, e); the set's reads from the gate (s); no new failure (h). The card surface is not readable here, so the desk confirms it with him (L70).

## CONTINUE
next: STEP-D0 (gate green at 02:49:46 ET)
D0 and D1 passed. D2.0: `deploy-shipped.sh --moved b6523f31 "<card>"` printed nothing, and the report commit follows. next: D2.1
OUTAGE STARTING 02:52:14 ET — residents of <restart set> (EMPTY: none) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
4.6 ended at 02:52:27 (nothing down). Smoke GREEN at 02:55:29. Tagged; the run closes at STEP-7.

## DECISIONS
1. ASK DESK: P7's two-dot `diff main <head>` lists `0025_dml_roles*` and `__init__.py` as removals, because `main` gained 0025 (the dml-roles deploy) after `ops/cos-outage-1018` was cut. The head itself changes nothing under `db_migrations` (`main...b5d62f17` is empty). Safe default taken: P7 passes with `MIGRATIONS: none`, and STEP-T's `<m0>..<BRANCH>` migration check, which reads the merged tree, is the binding proof that 0025 survives the merge. [02:01 ET] — CLOSED by proof at STEP-T: `diff --stat b6523f31 deploy/cos-outage-attempt2 -- src/cobalt/db_migrations` printed nothing. For the desk: P7's two-dot form reads a `main` that moved after the cut as a removal, and a hub amendment to the three-dot form would stop this repeating; that is a tool question, not a stop (R1863).

## RECORDS
- Downtime: none (`<restart set>` empty; no resident went down).
- `cobalt_dev: 0013 (F2 = F0)`, lock released by `gate.sh`. `<GATE>/.env` is absent and so is the lock dir.
- REFUSED, not needed: none. Messages not followed: none.
- RETIRE OWED: none. BOOTSTRAP OWED (this run): none. Standing OWED in `<hb0>`, untouched by this run: `com.cobalt.prefill-refresh` and `com.cobalt.playbook` (`data/deploy/bootstrap-owed.json`).
- Carried RED: none (`<hb0>` GREEN, radar `idle (overnight)`).
- `main` at D0 carried an untracked `.claude/settings.json.bak`, outside the hub's ACCEPTED and REFUSED lists. It was not touched by this run, and that is noted for the desk.
- The 798 attempt's G (c) red (`test_db_credentials.py::TestTheLiveFactoryAuthenticatesAsCobaltApp::test_it_is_a_member_of_all_three_side_roles`) did not recur on this gate. Pass 1 was 0 failed after dml-roles (0025) landed on `main`.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-cos-outage-attempt2` and branch `deploy/cos-outage-attempt2`; the set's branch `ops/cos-outage-1018`; the failed 798 gate `deploy/cos-outage` and its worktree, if the desk has not yet removed them.
- L74: the `Claude-Session:` reminder is recorded once under `## L74` and was not acted on.
- Card `## RECORDS` (desk's), copied:
  - cos-outage-1018: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-outage-1018-check-2026-10-18.md` last line: CHECK DONE · job: cos-outage-1018 · pass: 1 · tip: de3e15c8 · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8612/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165134
  - cos-outage-1018: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-outage-1018` → `b5d62f17`; code tip `de3e15c8`
  - written by deploy-card.sh at 2026-10-19 02:01 ET (`date`); trial merge of the heads onto main in order: clean
- PRE-STOP SELF-CHECK:
  1. Every smoke row's evidence is quoted verbatim above with its `date` (02:52:43 … 02:55:29).
  2. P3 re-read `de3e15c8` and `b5d62f17`. `merge-base --is-ancestor b5d62f17 a5e07866` → exit 0 and `merge-base --is-ancestor de3e15c8 a5e07866` → exit 0.
  3. REVERT-READBACK (h) is shown: four counts equal, no growth. Every count, sha and line number in this report was read from this run's tool output.
  4. STEP-T merged clean (`Merge made by the 'ort' strategy.`) and D2.1 did too, so no conflict marker exists.
- THE RELEASE: the lock was released by `gate.sh` at the gate's end. `<GATE>/.env` is absent and the lock dir is absent (verified after STEP-G), so nothing is held.

DEPLOYED deploy-2026-10-19-cos-outage-attempt2 a5e07866 | set: cos-outage | migrations: none | gate: offline 8667/0 · with-DB 5610/0 · live-note 147/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 221956
