# deploy-preflight-fixes-1005 — SET: workflow2 — MIGRATIONS: none

## §0 Headline
- DEPLOYED `deploy-2026-10-05-preflight-fixes`: `ops/preflight-fixes-1005` @ `0af97be7` (preflight.sh card 20 F1 + F2, with tests) is on `main` at `c4e12797`.
- Gate green on `2ecd5fce`: offline 3786/0 · with-DB 4639/0 · live-note 146/0; `cobalt_dev: 0013 — F2 = F0`; lock released.
- RESTARTS: none. No resident went down; aset, radar and agent kept the same pids. No migration.
- Smoke GREEN: markers 0 → 2 ×3; curls 200; heartbeat GREEN twice; radar cycling; failure counts flat.
- One decision (ASK DESK, not his): G (d2) `validate --no-db` was refused, so it was SKIPPED under his R412.

## L74
- A system reminder in this session asked for a `Claude-Session:` trailer line on commits. Recorded once as data (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/39-deploy-preflight-fixes-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/39-deploy-preflight-fixes-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/39-deploy-preflight-fixes-card.md" · 0 · 9d49f133593085c9a9a2b465ea2711881f621891
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/39-deploy-preflight-fixes-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
- R412's "production HOLD" read in full (`cto-2026-10-05-words.md:27`): "Go on with the workflow set one at a time … guard-b, then preflight.sh's two fixes, then the hub text … Production stays on hold until the workflow set is deployed." This deploy IS the workflow set's second item (preflight.sh's two fixes), so the hold does not bar it.

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| FIRST LAUNCH | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct  5 14:35:53 EDT 2026` — a trading day outside (i)–(iv); `MIGRATIONS: none` → `window: (v) provisional` (STEP-R re-reads it) |
| P2 | `tail -n 3 "…/preflight-fixes-check-2026-10-05.md"` | 0 | `CHECK DONE · job: preflight-fixes · pass: 1 · tip: 0af97be7 · house A: none (overruled 2026-10-05 R412) · findings: 6 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3786/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 0 · for Dejan: 0` — carries `held unfixed: 0`, `ready: YES`, `tip: 0af97be7` = row |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/preflight-fixes-check-2026-10-05.md"` | 0 | `4f586d6e6cd1e9af989f6e0bce70643cc7853e75` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/preflight-fixes-check-2026-10-05.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 0af97be7` | 0 | `0af97be7` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/preflight-fixes-1005` | 0 | `0af97be7` = row head = `TIP` |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 0af97be7 ops/preflight-fixes-1005` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 0af97be7 ops/preflight-fixes-1005 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no session holds the lock |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-preflight-fixes-1005` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `9d49f133` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 9d49f133 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-preflight-fixes-1005` | 0 | EMPTY |
| P6 | `grep -c -F "card 20 F2" /Users/cobalt/cobalt/ops/desk/preflight.sh` | 1 | `0` = before |
| P6 | `grep -c -F "card 20 F1" /Users/cobalt/cobalt/ops/desk/preflight.sh` | 1 | `0` = before |
| P6 | `grep -c -F "(recorded)" /Users/cobalt/cobalt/ops/desk/preflight.sh` | 1 | `0` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 0af97be7 -- src/cobalt/db_migrations` | 0 | nothing — no migration, matches `MIGRATIONS: none` |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` (equals the bootstrap string) · `pid = 13209` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` (equals) · `pid = 28249` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 0af97be7` → `Merge made by the 'ort' strategy.` (4 files: `.../reports/preflight-fixes-build-2026-10-05.md` +167, `ops/desk/preflight.sh` 54, `tests/ops/test_desk_launch_brain.py` 2, `tests/ops/test_preflight.py` 78; 291 insertions, 10 deletions)
- `git -C <GATE> rev-parse --short=8 HEAD` → `2ecd5fce` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 9d49f133..deploy/deploy-preflight-fixes-1005` → `2ecd5fce Merge commit '0af97be7' into deploy/deploy-preflight-fixes-1005` (one line, one head)
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 0af97be7 deploy/deploy-preflight-fixes-1005` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 9d49f133 deploy/deploy-preflight-fixes-1005 -- src/cobalt/db_migrations` → nothing (no migration path; `MIGRATIONS: none`)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 9d49f133 deploy/deploy-preflight-fixes-1005 -- configs ops` → ` ops/desk/preflight.sh | 54 +++++++++++++++++++++++++++++++++++++++++++--------` / ` 1 file changed, 46 insertions(+), 8 deletions(-)`. No plist added, modified or removed.

## RESTARTS
- `cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the gate's `.venv`: `Installed 253 packages in 742ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/preflight-fixes-build-2026-10-05.md	A	DOCS	-
ops/desk/preflight.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_brain.py	M	test/documentation; no resident	-
tests/ops/test_preflight.py	M	test/documentation; no resident	-
RESTARTS: none
```
- `<restart set>` = none (empty). No `UNCLASSIFIED` row. `window: (v) holds` (P1 `(v) provisional`, the set is empty, `MIGRATIONS: none`).

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold — the check's stop line carries `with-DB 0/0` (a with-DB count of 0) → the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 157 skipped in 16.25s` — `0 failed` (the skips are with-DB tests: `Postgres env settings not available` / `requires_db: needs cobalt_dev`).
- (d2) `COBALT_ENV=production uv run cobalt validate --no-db` → REFUSED (no dialog): `Permission to use Bash has been denied because Claude Code is running in don't ask mode.` Not retried in any spelling. `G (d2) — SKIPPED (his R412)`: R412 (in `RULINGS`, AUTHORIZED) reads "Remove the pre-merge (d2) line from DEPLOY-HUB. Post-merge validate is the check. No --no-db allow string is needed." The card's `## RECORDS` points to the sibling cards' wording (`G (d2) SKIPPED this run only`). The checks are 4.5's `validate` and smoke (f). See `## DECISIONS` 1.
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-preflight-fixes-1005 all --deploy` (no `--deselect`: the build report names none; no `--tickers` / `--migration` on the card) — launched in the background. Exit 0. Verdict lines whole:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-preflight-fixes-1005-all-20261005-143803.log
```
- (a) offline `3786/0`. (c)+(c3) with-DB `4639/0`. (e) live-note `146/0`.
- SKIPS: every one is inside the allowed set: `test_cards_picks.py:388`, `:401`; `test_radar_evaluate.py:695`; `test_catalyst.py:365`; `test_predicate.py:262`; the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`; `test_s3_c4_experiments.py:95` = the `@requires_live` decorator line of `test_x14_live_his_template_strips_to_the_committed_fixture` (`:96`, read from `<GATE>`). The live-note pass printed no skip naming `COBALT_LIVE_VAULT_ROOT`.
- (c2) `dev forward: APPLIED 15:00:19` (log:1053). (f) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log:846) = `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log:1675) → `cobalt_dev: 0013 — F2 = F0` (log:1726).
- THE RELEASE: log:1727–1732 `release-devdb-lock.sh deploy-preflight-fixes-1005` → `lock released` · `.env: removed` (L76 lock released after the 15:00:19 forward; the log carries no stamp on the release line). `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 2ecd5fce (`date` → `Mon Oct  5 15:05:18 EDT 2026`)

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 130]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M` under `docs/40 - DevDocs/` (5 reports incl. `cto-2026-10-05.md`), ` M .claude/settings.json`, `??` under `docs/40 - DevDocs/` (incl. this report), and `?? .claude/settings.json.bak` (not under `src/` `tests/` `ops/` `configs/`: not refused; recorded) |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat 9d49f133 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-deploy-preflight-fixes-1005` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-deploy-preflight-fixes-1005' (was 9d49f133)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` / `reset --soft HEAD~1` / `log --oneline -1` | 0 / 0 / 0 | `[main 92617085] scratch: …` / — / `9d49f133 docs(desk): card 39 RULINGS header = R412 (HIS RULING + APPROVED; L7a)` (HEAD back) |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-05-preflight-fixes` | 1 | free |
| TAGS | `rev-parse --verify --quiet refs/tags/pre-deploy-preflight-fixes-1005` | 1 | free |

### STEP-D1 (baseline, read-only)
| read | exit | result |
|---|---|---|
| `date` | 0 | `Mon Oct  5 15:05:44 EDT 2026` |
| `heartbeat show` = `<hb0>` | 0 | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 15:05:46 EDT)`; `OK sheet HTTP http://127.0.0.1:5010/ -> 200`; `OK radar scanning (rth), members 50`; `OK com.cobalt.aset running loaded, pid 13209`; `OK com.cobalt.agent running pid 22243 alive`; `OK com.cobalt.radar running running 159 min, heartbeat fresh`; `AMB com.cobalt.herdr unmanaged … by declared interim` — no RED |
| `validate` = `<val0>` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.` |
| `Jobs (F17):` = `<jobs0>` | — | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 15 label(s), exact match.` · `registry <-> plists: schedules and COBALT_ENV agree on every job.` |
| `backup status` | 0 | `newest snapshot: 2.7 h old` (ssd ARMED) |
| `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `pid = 13209` = `<aset pid>` |
| `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `pid = 28249` = `<radar pid>` |
| `cobalt.sh status` / `ps -p 22243` | 0 / 0 | `Cobalt is ONLINE (PID: 22243).` / `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py` |
| `tail -n 8 logs/radar.err` | 0 | last: `2026-10-05 15:05:45.902 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791227060029` (7 `cards.expire … falling back to the session close` INFO lines before it; no traceback) |
| `<a0>` Started server process (aset.err) | 0 | `42` |
| `<ta0>` Traceback (aset.err) | 0 | `2` |
| `<tr0>` Traceback (radar.err) | 1 | `0` |
| `<tc0>` TaxonomyConfigError (radar.err) | 1 | `0` |
| `<rp0>` radar panel FAILED (aset.err) | 0 | `17` |
| `<rpr0>` radar pool refresh FAILED (aset.err) | 0 | `58` |
| `<re0>` radar S5 evaluate FAILED (radar.err) | 0 | `39` |
| `<lc0>` lifecycle card read failed (radar.err) | 0 | `39` |
| `curl … /radar` | 0 | `200` |
| MARKERS F2 / F1 / (recorded) | 1 / 1 / 1 | `0` / `0` / `0` = before |
| `<RB>`, census, D1-M | — | not run: `MIGRATIONS: none` |

### STEP-D2
| step | command | exit | result |
|---|---|---|---|
| D2.0 | `add` + `commit -m "docs(report): deploy deploy-preflight-fixes-1005 — gate green on 2ecd5fce" …` | 0 | `[main 213e4f39] …` `1 file changed, 153 insertions(+)`; `show --stat HEAD` → that one file |
| D2.0 | `git -C /Users/cobalt/cobalt rev-parse --short=8 main` | 0 | `213e4f39` = `<pre-merge>` |
| D2.1 | `git -C <GATE> merge --no-edit main` | 0 | `Merge made by the 'ort' strategy.` (the report only) |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `c4e12797` = `<stack-final>` |
| D2.2 | `git -C /Users/cobalt/cobalt rev-parse --short=8 c4e12797^2` | 0 | `213e4f39` = `<pre-merge>` |
| D2.2 | `merge-base --is-ancestor 2ecd5fce c4e12797` | 0 | — |
| D2.3 | `git -C /Users/cobalt/cobalt diff --stat 2ecd5fce c4e12797 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | NOTHING (docs only) |
| D2.4 | `backup status` | 0 | `newest snapshot: 2.7 h old` |
| D2.4 | `backup run` | 0 | `backup: cobalt_brain via pg_dump inside cobalt_memory — 4758.2 MB` · `ssd: snapshot a7e1e78c — 0 new / 4 changed, 137.2 MB added, 1 pruned` |
| D2.4 | `backup status` | 0 | `newest snapshot: 0.0 h old` (a7e1e78c newest) |
| D2.5 | `date` · `heartbeat show` | 0 · 0 | `Mon Oct  5 15:07:35 EDT 2026` · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 15:07:37 EDT)` — 111 s after D1's 15:05:46; no new RED; `com.cobalt.radar running running 160 min, heartbeat fresh` (four filler `date` + `heartbeat show` pairs at 15:07:12–15:07:32, all GREEN) |
| D2.6 | `date` | 0 | `Mon Oct  5 15:07:42 EDT 2026` — window (v) holds (empty set, no migration: any hour) |
| D2.6 | `git -C /Users/cobalt/cobalt tag pre-deploy-preflight-fixes-1005` → `rev-parse --short=8` | 0 | `213e4f39` = `<pre-merge>` |

### STEP-4 (empty restart set: nothing went down)
| step | command | exit | result |
|---|---|---|---|
| 4.1 | `date` | 0 | `Mon Oct  5 15:07:56 EDT 2026` = `<t down>` = `<t up>` (empty set) |
| 4.2 | — | — | no label in `<restart set>`: no bootout, no stop |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | 0 | `213e4f39` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/deploy-preflight-fixes-1005` | 0 | `Updating 213e4f39..c4e12797` / `Fast-forward` (4 files, 291 insertions, 10 deletions) |
| 4.4 | — | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.` · `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`; `registry <-> ops/: 15 label(s), exact match.`; `registry <-> plists: schedules and COBALT_ENV agree on every job.` |
| 4.6 | — | — | nothing to bring up; downtime `none` |

### CLOSE (STEP-7)
- `<pre-merge>` `213e4f39` → `<stack-final>` `c4e12797` (main tip `c4e12797`).
- Tags: `pre-deploy-preflight-fixes-1005` at `213e4f39`; `deploy-2026-10-05-preflight-fixes` at `c4e12797` (set after the green smoke).
- `<t down>` / `<t up>` / seconds: `none` (empty set).
- uv sync line: none in production. The gate's `.venv` was created on the first `uv run` in `<GATE>` (`Installed 253 packages in 742ms`).
- Proof cost: not run (`MIGRATIONS: none`). `migrations applied: none`. `<RB>` before / after: not applicable.
- Snapshot: `a7e1e78c` (ssd, 4758.2 MB dump, 137.2 MB added).
- `RESTARTS done: none`.
- THE ROLLBACK STRING (the desk's):
  1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 c4e12797` — ONE revert of the main-into-gate merge (it carries the set's merge with it). No resident to take down: the restart set is empty.
  2. SCHEMA: none (no migration).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` — git titles it `Reapply "Merge branch 'main' into deploy/deploy-preflight-fixes-1005"`.

## Smoke
`<t up>` = `Mon Oct  5 15:07:56 EDT 2026` (empty set). FIRST CALLS: `<rp_up>` `17` · `<rpr_up>` `58` · `<re_up>` `39` · `<lc_up>` `39`.

| row | `date` | command | result |
|---|---|---|---|
| (a) | 15:08:13 | `launchctl print gui/501/com.cobalt.aset` | `state = running`, `pid = 13209` = D1 (outside the set: same pid) |
| (a) | 15:08:13 | `launchctl print gui/501/com.cobalt.radar` | `state = running`, `pid = 28249` = D1 (same pid) |
| (a) | 15:08:13 | `/Users/cobalt/cobalt/cobalt.sh status` | `Cobalt is ONLINE (PID: 22243).` (same pid) |
| (b) | 15:08:17 | `grep -c "Started server process" logs/aset.err` | `42` = `<a0>` (aset outside the set) |
| (b) | 15:08:17 | Traceback aset / Traceback radar / TaxonomyConfigError radar | `2` / `0` / `0` = `<ta0>` / `<tr0>` / `<tc0>` |
| (b) | 15:08:17 | `tail -n 30 logs/aset.err` | last lines a 09:44:31 `cobalt.aset.daily_note:_write_unit:189 - [WRITE] updated: … section=aset-cards · unit=card-20261005T094431 · write_id=4506` diff; no new start (aset not restarted), no traceback |
| (c) | 15:08:17 | `curl … http://127.0.0.1:5010/` · `/radar` · `/radar\?frame=phone` | `200` · `200` · `200` |
| (d) | 15:08:17 | MARKERS `card 20 F2` / `card 20 F1` / `(recorded)` | `2` / `2` / `2` = after |
| (s) | 15:08:17 | pass-2 head reference (F2) `grep -c -F "card 20 F2" …/preflight.sh` | exit 0, `2` (≥1: green) |
| (s) | 15:08:17 | self-check count recorded (F1) `grep -c -F "(recorded)" …/preflight.sh` | exit 0, `2` (≥1: green) |
| (f) | 15:08:28 | `COBALT_ENV=production uv run cobalt jobs restarts 213e4f39..c4e12797` | exit 0; same 4 rows as STEP-R; `RESTARTS: none` = `<restart set>`; no `UNCLASSIFIED` |
| (f) | 15:08:28 | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>` |
| (e) 1 | 15:08:33 | `heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 15:08:35 EDT)`; `com.cobalt.radar running running 161 min, heartbeat fresh` |
| (g) | — | — | no migration |
| (b) tail 1 | 15:09:29 (`<t up>` + 93 s) | `tail -n 12 logs/radar.err` | `2026-10-05 15:08:51.759 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791227245932` — a cycle line stamped after `<t up>`; the 11 lines before it are `cards.expire … falling back to the session close` INFO; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → GREEN, settled |
| (e) 2 | 15:10:26 | `heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 15:10:28 EDT)` — 113 s after (e) 1; no RED; `com.cobalt.radar running running 163 min, heartbeat fresh` (filler `date` + `heartbeat show` pairs 15:08:49–15:10:22, all GREEN) |
| (h) | 15:10:56 (`<t up>` + 180 s) | the four failure counts | `17` / `58` / `39` / `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (= D1 baselines; none grew) |
| (h) | 15:10:56 | `curl … /radar` | `200` |
| (h) | — | census | none on the card |

THE CHAIN: every check committed (P2: `4f586d6e`, `held unfixed: 0`, `ready: YES`, tip `0af97be7`) → the tip re-read (P3: `0af97be7` = head) → the merged tree (T: `<m1>` `2ecd5fce`, one merge, no migration) → RESTARTS derived (R: none) → three suites green on `<m1>` (G: offline 3786/0, with-DB 4639/0, live-note 146/0, F2 = F0) → `<stack-final>` `c4e12797` = `<m1>` + docs (D2.3: nothing outside docs) → landed code (4.3: `Updating 213e4f39..c4e12797` Fast-forward) → markers 0 → 2 / 2 / 2 (d) → no migration (g) → residents up after the merge, same pids (a) → radar cycling at 15:08:51, heartbeat GREEN twice (b, e) → the set's reads green (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

SMOKE: GREEN.

## CONTINUE
next: STEP-D2 (gate green at Mon Oct  5 15:05:18 EDT 2026; D0, D1 done)
OUTAGE STARTING Mon Oct  5 15:07:42 EDT 2026 — residents of none (empty restart set) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
4.6 ended at 15:07:56 with nothing down; smoke GREEN at 15:10:56; STEP-7 closed. Nothing comes next in this run.

## DECISIONS
1. ASK DESK: G (d2) `validate --no-db` was refused (no allow string, as his R412 says). Is skipping it under R412 and the card's sibling wording right? [Mon Oct  5 14:35:53 EDT 2026 + run] Safe default taken: SKIPPED (his R412). Post-merge 4.5 `validate` and smoke (f) are the check; a red there → STEP-5. The set restarts nothing.

## RECORDS
- REFUSED: `COBALT_ENV=production uv run cobalt validate --no-db` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (G (d2); his R412 removed the step, see `## DECISIONS` 1)
- Downtime: none (empty restart set). No `CONTINUE` message arrived; no message was followed.
- `cobalt_dev: 0013 (F2 = F0)` — `F0` = `F2` = `664 35 272c95bbb12241e3611e4b36326ccf87`; lock released (gate log:1727–1732).
- RETIRE OWED: none (no plist removed).
- Carried RED: none. Every heartbeat read this run was GREEN (`AMB com.cobalt.herdr … declared interim` is an amber, not a RED).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-preflight-fixes-1005` and branch `deploy/deploy-preflight-fixes-1005` (`.venv` created in it by this run); the set's branch `ops/preflight-fixes-1005` and its worktree, if any.
- Tags pushed: none. Push is his (L55): `main` at `c4e12797`, tags `pre-deploy-preflight-fixes-1005`, `deploy-2026-10-05-preflight-fixes`.
- `?? .claude/settings.json.bak` on `main` at D0: untracked, outside `src/` `tests/` `ops/` `configs/`. Not refused; noted for the desk.
- Card RECORDS (the desk's, copied):
  - preflight-fixes: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/preflight-fixes-check-2026-10-05.md` last line: CHECK DONE · job: preflight-fixes · pass: 1 · tip: 0af97be7 · house A: none (overruled 2026-10-05 R412) · findings: 6 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3786/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 0 · for Dejan: 0
  - preflight-fixes: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/preflight-fixes-1005` → `0af97be7`; code tip `0af97be7`
  - G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
- L74: one system reminder asked for a `Claude-Session:` commit trailer; recorded under `## L74`, not acted on.

### PRE-STOP SELF-CHECK
1. Every smoke row is quoted with its `date` (`## Smoke`: 15:08:13 – 15:10:56).
2. The tip was re-read at P3 (`0af97be7`), and `git -C /Users/cobalt/cobalt merge-base --is-ancestor 0af97be7 c4e12797` → exit 0.
3. REVERT-READBACK shown at (h): `17` / `58` / `39` / `39` at 15:10:56. Every count, sha and line was read from tool output this run.
4. No conflict marker: STEP-T merged clean (`Merge made by the 'ort' strategy.`); `git -C <GATE> status --short --branch` → `## deploy/deploy-preflight-fixes-1005` alone.
- THE RELEASE: `ls -la <GATE>/.env` → No such file; the lock dir is absent (G).

DEPLOYED deploy-2026-10-05-preflight-fixes c4e12797 | set: workflow2 | migrations: none | gate: offline 3786/0 · with-DB 4639/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0
