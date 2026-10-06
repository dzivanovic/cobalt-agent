# deploy-launcher-f5-1005 — SET: workflow2 — MIGRATIONS: none

## §0 Headline
- DEPLOYED `deploy-2026-10-05-launcher-f5` at `5ec48566`. F5 is on main: `ops/desk/desk-launch.sh` and `tests/ops/test_desk_launch_prechecks.py`, from `ops/launcher-fixround-1005` `fb2d95a2`.
- Gate green on `68d3c749`: offline 3873/0 · with-DB 4735/0 · live-note 146/0. `cobalt_dev` is back at 0013, F2 = F0.
- RESTARTS: none, so no resident went down and there was no downtime. Smoke GREEN: markers 1/1/1/1, heartbeat GREEN, radar cycling, failure counts flat.
- Snapshot `7fa24f68`; rollback tag `pre-deploy-launcher-f5-1005` at `68811ed8`. Push is his, through the desk (L55).
- Decisions: 1 (the untracked `.claude/settings.json.bak` on main), not his.

## L74
- The session's harness reminder asked that commits also carry a `Claude-Session:` line. Recorded once as data. Not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/57-deploy-launcher-f5-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/57-deploy-launcher-f5-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/57-deploy-launcher-f5-card.md" · 0 · 44c22cfa2c320ad5ff4d4be2c833237188af7df6
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/57-deploy-launcher-f5-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
- R412's "production HOLD" was read in `cto-2026-10-05-words.md` `## R412`: "Production stays on hold until the workflow set is deployed." This card is that set (`SET: workflow2`, LADDER "workflow set … R387"), so the hold does not bar this deploy.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "<REPORT>"` | 1 | No such file or directory |
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| P1 | `date` | 0 | Mon Oct  5 22:00:51 EDT 2026 |
| P2 | `tail -n 3 ".../launcher-checks-check-2026-10-05-r2.md"` | 0 | `CHECK DONE · job: launcher-checks · pass: 1 · tip: a545a4d8 · … · held unfixed: 0 · open: 0 · … · suites: offline 3786/0 · with-DB 857/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 152813` |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/…/launcher-checks-check-2026-10-05-r2.md"` | 0 | 6bf0b815c86ac3ae11567bf32f890efea7dc37bd |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/launcher-checks-check-2026-10-05-r2.md"` | 0 | nothing |
| P2 fix round | `tail -n 3 ".../launcher-f5-fixround-2026-10-05.md"` | 0 | `BUILT · job: launcher-checks · tip: 8d79d7c9 \| on 5fb0ddf5 \| migration: none \| offline 3786/0 \| with-DB 857/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: none \| rows: 1 of 1 \| self-check: 3 of 3 \| decisions: 2 · for Dejan: 0 · tokens: 179659` |
| P2 fix round | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/…/launcher-f5-fixround-2026-10-05.md"` | 0 | 44c22cfa2c320ad5ff4d4be2c833237188af7df6 |
| P2 fix round | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/launcher-f5-fixround-2026-10-05.md"` | 0 | nothing |
| P2 fix round | `git -C /Users/cobalt/cobalt merge-base --is-ancestor a545a4d8 8d79d7c9` | 0 | ancestor |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 8d79d7c9` | 0 | 8d79d7c9 |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-fixround-1005` | 0 | fb2d95a2 (= TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 8d79d7c9 fb2d95a2` | 0 | ancestor |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 8d79d7c9 fb2d95a2 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — no lock held |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-launcher-f5-1005` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `ed62f960` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor ed62f960 main` | 0 | ancestor |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-launcher-f5-1005` | 0 | empty |
| P6 | marker 1 `grep -c -F "ruling_items() {" …/desk-launch.sh` | 1 | 0 (before 0) |
| P6 | marker 2 `grep -c -F "tool_list() {" …/desk-launch.sh` | 1 | 0 (before 0) |
| P6 | marker 3 `grep -c -F "card 21 F5: …" …/desk-launch.sh` | 1 | 0 (before 0) |
| P6 | marker 4 `grep -c -F "def test_f5_the_survey_prompt_launches_on_its_rulings_row" …/test_desk_launch_prechecks.py` | 1 | 0 (before 0) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main fb2d95a2 -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 17342 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 17353 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| merge | `git -C <GATE> merge --no-edit fb2d95a2` | 0 | `Merge made by the 'ort' strategy.` — 3 files: `docs/…/launcher-fixround-build-2026-10-05.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_prechecks.py` (270+, 49−) |
| `<m1>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `68d3c749` |
| merges | `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent ed62f960..deploy/deploy-launcher-f5-1005` | 0 | `68d3c749 Merge commit 'fb2d95a2' into deploy/deploy-launcher-f5-1005` |
| ancestry | `merge-base --is-ancestor 8d79d7c9 deploy/deploy-launcher-f5-1005` | 0 | ancestor |
| ancestry | `merge-base --is-ancestor fb2d95a2 deploy/deploy-launcher-f5-1005` | 0 | ancestor |
| migrations | `git -C /Users/cobalt/cobalt diff --stat ed62f960 deploy/deploy-launcher-f5-1005 -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none |
| STEP-C | `git -C /Users/cobalt/cobalt diff --stat ed62f960 deploy/deploy-launcher-f5-1005 -- configs ops` | 0 | ` ops/desk/desk-launch.sh \| 139 ++++…---- ` / ` 1 file changed, 94 insertions(+), 45 deletions(-)` — no plist added, modified or removed |

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after uv created `.venv` in the gate: `Installed 253 packages in 857ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md	M	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = none (EMPTY). There is no `UNCLASSIFIED` row and no migration. No resident goes down.

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat a545a4d8 68d3c749 -- . ":(exclude)docs"` → 19 files, `2540 insertions(+), 98 deletions(-)` (main moved since the check: drc, aset, preflight). Not equal, so the gate runs whole (`--deploy`).
- (a0): `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 157 skipped in 15.47s`, 0 failed. Every skip is a with-DB test (`Postgres env settings not available` / `requires_db`).
- Deselects: none. The build report :263 says "no `--deselect`: this build adds no with-DB test", and F5's test is in `tests/ops`, offline. No `--tickers`, no `--migration`.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-launcher-f5-1005 all --deploy` → exit 0. Verdict lines, whole:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-launcher-f5-1005-all-20261005-220231.log
```
- Skips: all 7 are inside the allowed set. `test_s3_c4_experiments.py:95` is the decorator line of `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F` → `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`). The `test_replay_line.py` skip names `COBALT_TEST_LIVE_DRC`. Live-note has no skip naming `COBALT_LIVE_VAULT_ROOT`.
- Log reads: `:1064 dev forward: APPLIED 22:24:59` · `:856 F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `:1686 F2: 664 35 272c95bbb12241e3611e4b36326ccf87` · `:1737 cobalt_dev: 0013 — F2 = F0` · `:1739 lock released` · `:1743 .env: removed`. The log prints no clock time on the release line. It falls between 22:24:59 and the gate's end, at or before 22:29:54.
- THE RELEASE verified: `ls -la <GATE>/.env` → No such file · `grep -c -x -F "deploy-launcher-f5-1005" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (the lock dir is absent).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.
- Suites: offline 3873/0 · with-DB 4735/0 · live-note 146/0.

GATE GREEN on 68d3c749

## Deploy table
| step | command | exit | result |
|---|---|---|---|
| D0 main | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 4]` |
| D0 main | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; ` M` ×5 and `??` ×11 under `docs/40 - DevDocs/`; `?? .claude/settings.json.bak` (see DECISIONS 1). No staged line, and no dirty `src/`, `tests/`, `ops/` or `configs/` path. |
| D0 main | `git -C /Users/cobalt/cobalt diff --stat ed62f960 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| D0 probe | `tag scratch-allow-probe-deploy-launcher-f5-1005` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-deploy-launcher-f5-1005' (was ed62f960)` |
| D0 probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 11f551a2] …` → `ed62f960 docs(report): launcher F5 deploy card preflight — 8 checks, 0 fails, ready YES` (HEAD back) |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-05-launcher-f5` · `… refs/tags/pre-deploy-launcher-f5-1005` | 1 · 1 | neither exists |
| D1 | `date` · `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | 22:30:23 · `<hb0>` = `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 22:30:24 EDT)`. `radar idle (overnight)`; `com.cobalt.radar running 72 min, heartbeat fresh`; `com.cobalt.herdr` AMB (unmanaged interim, declared). |
| D1 | `COBALT_ENV=production uv run cobalt validate` | 0 | `<val0>` OK, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` |
| D1 | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 0.8 h old` |
| D1 | `launchctl print gui/501/com.cobalt.aset` · `…/com.cobalt.radar` | 0 · 0 | `state = running` · `<aset pid>` 17342 · `<radar pid>` 17353 |
| D1 | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 22243` | 0 · 0 | `Cobalt is ONLINE (PID: 22243).` · `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py` |
| D1 | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 0 | 8 lines `radar cycle: idle:overnight scan_id=None`, 22:18:50 → 22:30:30, no traceback |
| D1 counts | `grep -c` ×8 | — | `<a0>` 43 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 58 · `<re0>` 40 · `<lc0>` 39 |
| D1 | `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` | 0 | `200` |
| D1 markers | the four `## MARKERS` greps | 1 ×4 | `0` `0` `0` `0` = before |
| D1-M | — | — | not run: MIGRATIONS none |
| D2.0 | `git -C /Users/cobalt/cobalt add "docs/…/deploy-deploy-launcher-f5-1005.md"` · `commit -m "docs(report): deploy deploy-launcher-f5-1005 — gate green on 68d3c749" …` | 0 · 0 | `[main 68811ed8] …` · `show --stat HEAD` → 1 file, `.../reports/deploy-deploy-launcher-f5-1005.md \| 144 +++` |
| D2.0 | `git -C /Users/cobalt/cobalt rev-parse --short=8 main` | 0 | `<pre-merge>` = `68811ed8` |
| D2.1 | `git -C <GATE> merge --no-edit main` | 0 | `Merge made by the 'ort' strategy.` (the report, 1 file) |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` · `rev-parse --short=8 5ec48566^2` · `merge-base --is-ancestor 68d3c749 5ec48566` | 0 · 0 · 0 | `<stack-final>` = `5ec48566` · `68811ed8` = `<pre-merge>` · ancestor |
| D2.3 | `git -C /Users/cobalt/cobalt diff --stat 68d3c749 5ec48566 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing — docs only |
| D2.4 | `backup status` | 0 | `newest snapshot: 0.8 h old` |
| D2.4 | `COBALT_ENV=production uv run cobalt backup run` | 0 | `backup: cobalt_brain dumped, 4889.4 MB` · `ssd: snapshot 7fa24f68 — 0 new / 3 changed, 12.8 MB added, 1 pruned` |
| D2.4 | `backup status` | 0 | `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` (pairs 22:31:53 → 22:32:14) | 0 | the read at `22:32:14 EDT` (110 s after D1's 22:30:24) is `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red`. No new RED; radar `running 73 min, heartbeat fresh`. |
| D2.6 | `date` · `git -C /Users/cobalt/cobalt tag pre-deploy-launcher-f5-1005` · `rev-parse --short=8 pre-deploy-launcher-f5-1005` | 0 · 0 · 0 | 22:32:18 · tag set · `68811ed8` |
| 4.1 | `date` | 0 | `<t down>` 22:32:33 (empty set: no resident goes down) |
| 4.2 | — | — | nothing: `<restart set>` empty |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | 0 | `68811ed8` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/deploy-launcher-f5-1005` | 0 | `Updating 68811ed8..5ec48566` / `Fast-forward` — 3 files, 270+ 49− |
| 4.3 | `date` | 0 | 22:32:37 = `<t up>` (empty set) |
| 4.4 | — | — | migrations applied: none |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | OK, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>` |
| 4.6 | — | — | nothing: no label taken down. Downtime: none |
| STEP-7 | `git -C /Users/cobalt/cobalt tag deploy-2026-10-05-launcher-f5` · `rev-parse --short=8 deploy-2026-10-05-launcher-f5` | 0 · 0 | `5ec48566` |

CLOSE:
- `<pre-merge>` `68811ed8` → `<stack-final>` `5ec48566` (main tip).
- Tags: `pre-deploy-launcher-f5-1005` at `68811ed8`; `deploy-2026-10-05-launcher-f5` at `5ec48566`.
- `<t down>` 22:32:33 / `<t up>` 22:32:37 / downtime: none (empty set; no resident stopped).
- uv sync line in production: none. Proof cost: n/a (no migration). Migrations applied: none. `<RB>` before / after: n/a.
- Snapshot: `7fa24f68` (ssd).
- RESTARTS done: none.

THE ROLLBACK STRING (the desk's, never this session's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 5ec48566` — ONE revert of the main-into-gate merge. `<restart set>` is empty, so no resident needs to go down or come back up.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
| row | date | command | result | verdict |
|---|---|---|---|---|
| first calls | after 22:32:37 | the four failure counts | `<rp_up>` 17 · `<rpr_up>` 58 · `<re_up>` 40 · `<lc_up>` 39 (= D1) | — |
| (a) | 22:32:44 | `launchctl print gui/501/com.cobalt.aset` · `…/com.cobalt.radar` · `cobalt.sh status` | aset `state = running` pid 17342 (same; outside the set) · radar `state = running` pid 17353 (same) · `Cobalt is ONLINE (PID: 22243).` (same) | GREEN |
| (b) | 22:32:48 | `grep -c "Started server process" …/aset.err` | 43 = `<a0>` (aset outside the set) | GREEN |
| (b) | 22:32:48 | `tail -n 30 …/aset.err` | last `INFO:     Started server process [17348]` (21:18:48 startup) then `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)`; no new start | GREEN |
| (b) | 22:32:48 | Traceback aset · Traceback radar · TaxonomyConfigError radar | 2 · 0 · 0 = baseline | GREEN |
| (c) | 22:32:48 | `curl … http://127.0.0.1:5010/` · `/radar` · `/radar\?frame=phone` | `200` · `200` · `200` (first attempt each) | GREEN |
| (d) | 22:32:48 | the four `## MARKERS` greps | `1` `1` `1` `1` = after | GREEN |
| (f) | 22:32:37 / 22:32:48 | 4.5 validate · `COBALT_ENV=production uv run cobalt jobs restarts 68811ed8..5ec48566` | validate exit 0 as 4.5 · exit 0, same 3 rows (DOCS / operator script / test), `RESTARTS: none` = STEP-R, no `UNCLASSIFIED` | GREEN |
| (e) 1 | 22:33:03 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 22:33:04 EDT)`; `com.cobalt.radar running 74 min, heartbeat fresh` | — |
| (g) | — | — | no migration | n/a |
| (s) | 22:33:09 | `ruling_items` helper · `tool_list` helper · F5 comment · F5 test (`grep -c -F` each, the card's strings) | `1` · `1` · `1` · `1`, exit 0 each | GREEN |
| (b) tail 1 | 22:34:07 (`<t up>` + 90 s) | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | last `2026-10-05 22:33:50.269 \| INFO \| cobalt.radar.runner:resident:467 - radar cycle: idle:overnight scan_id=None`, after `<t up>`. No `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback. | GREEN (settled) |
| (e) 2 | 22:34:56 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 22:34:58 EDT)`, 114 s after (e) 1; `com.cobalt.radar running 76 min, heartbeat fresh`. No RED anywhere. | GREEN |
| (h) | 22:35:37 (`<t up>` + 180 s) | the four failure counts · `curl … /radar` · `tail -n 12 …/radar.err` | 17 · 58 · 40 · 39 = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew) · `200` · newest `22:35:30.293 … radar cycle: idle:overnight scan_id=None`. No `census` read on the card. | GREEN |

THE CHAIN, each link tied to its evidence:
- (P2) every check is committed: `6bf0b815`, plus fix report `44c22cfa`.
- (P3) the tips: `8d79d7c9` / `fb2d95a2`.
- (T) the merged tree: `68d3c749`.
- (R) RESTARTS derived: none.
- (G) three suites green on `68d3c749`: offline 3873/0 · with-DB 4735/0 · live-note 146/0.
- (D2.3) `<stack-final>` `5ec48566` = `<m1>` + docs.
- (4.3) the code landed: `68811ed8..5ec48566` fast-forward.
- (d) the markers: 1/1/1/1.
- (g) migration read back: n/a.
- (a) residents up after the merge, same pids, set empty.
- (b, e) radar cycling: 22:33:50, 22:35:30.
- (s) the set's reads: 1/1/1/1.
- (h) no new failure: counts flat.

The card surface is not readable here; the desk confirms it with him (L70).

SMOKE: GREEN

PRE-STOP SELF-CHECK (K25):
1. Every smoke row above quotes its output verbatim with its `date`.
2. Every tip was re-read at P3: `8d79d7c9`, `fb2d95a2`. Both are ancestors of `<stack-final>`: `git -C /Users/cobalt/cobalt merge-base --is-ancestor fb2d95a2 5ec48566` → exit 0; `… 8d79d7c9 5ec48566` → exit 0.
3. REVERT-READBACK is shown at (h). Every count, sha and `file:line` in this report was read from tool output this run.
4. No conflict marker exists: STEP-T ran clean (`Merge made by the 'ort' strategy.`), and so did D2.1.

## CONTINUE
OUTAGE STARTING 22:32:18 — residents of none going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- 4.6 ended 22:32:37 with nothing down. Smoke GREEN at 22:35:37. STEP-7 closed: next: none — the run is complete.

## DECISIONS
1. `?? .claude/settings.json.bak` is on main at D0. It is not on the ACCEPTED list (that has ` M .claude/settings.json`, not the `.bak`), and it is not a REFUSED class (no staged line, not under `src/`, `tests/`, `ops/` or `configs/`). Default taken: go on. It is untracked, so it never enters a commit or the merge. ASK DESK: whether the `.bak` stays [22:30:23].

## RECORDS
- Downtime: none. `<restart set>` was empty, so no resident went down. `<t down>` 22:32:33, `<t up>` 22:32:37 (the merge only).
- `cobalt_dev: 0013 (F2 = F0)` — `F0`/`F2` `664 35 272c95bbb12241e3611e4b36326ccf87` (gate log :856, :1686). The lock was released by `gate.sh`; `<GATE>/.env` is absent and the lock dir is absent.
- No `REFUSED, not needed` line. No `CONTINUE` message arrived. No `RETIRE OWED`: STEP-C found no plist.
- Carried RED: none. Every heartbeat read was `HEARTBEAT GREEN … nothing red`, and radar was `idle (overnight)`.
- L74: one harness reminder asked for a `Claude-Session:` line in commits. It is recorded under `## L74` and was not acted on.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-launcher-f5-1005` and branch `deploy/deploy-launcher-f5-1005`, and the set's branch `ops/launcher-fixround-1005` with its worktree if one exists. Not touched here; they are the desk's.
- The gate's `uv` created a fresh `.venv` in `<GATE>` at STEP-R (`Installed 253 packages in 857ms`). There was no `uv` sync line in production.
- The card's `## RECORDS`, copied:
  - launcher-f5: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-checks-check-2026-10-05-r2.md` last line: CHECK DONE · job: launcher-checks · pass: 1 · tip: a545a4d8 · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3786/0 · with-DB 857/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 152813
  - launcher-f5: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-fixround-1005` → `fb2d95a2`; code tip `8d79d7c9` (F5, row committed `6fce2ccb`; BASE `5fb0ddf5`). The F1-F4 part of the branch is already on main (deploy `21a06ce3`); the ship is F5's two code files and the builder's report.
  - fix report: `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-f5-fixround-2026-10-05.md`, a pointer record whose last non-blank line is the branch report's `BUILT · … tip: 8d79d7c9` stop line. It must be committed on main and unmodified before the launch.
  - G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
  - The builder's DECISIONS item 1: `tests/ops/test_desk_launch_brain.py::test_the_trees_brain_hub_line_is_printed_with_its_handover_filled` is red on the old BASE `5fb0ddf5` only. The brain ruled 10-05: ignore; already fixed on main by `c4e12797`, 66 passed; the deploy merges main. A record, not a defect.
- This run's gate is consistent with that: offline 3873/0 on `68d3c749`, which carries main.

DEPLOYED deploy-2026-10-05-launcher-f5 5ec48566 | set: workflow2 | migrations: none | gate: offline 3873/0 · with-DB 4735/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 178075
