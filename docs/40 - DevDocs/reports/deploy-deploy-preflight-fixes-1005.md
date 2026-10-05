# deploy-preflight-fixes-1005 — SET: workflow2 — MIGRATIONS: none

## §0 Headline
(run in progress)

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

## Smoke

## CONTINUE
next: STEP-D2 (gate green at Mon Oct  5 15:05:18 EDT 2026; D0, D1 done)

## DECISIONS
1. ASK DESK: G (d2) `validate --no-db` was refused (no allow string, as his R412 says). Is skipping it under R412 and the card's sibling wording right? [Mon Oct  5 14:35:53 EDT 2026 + run] Safe default taken: SKIPPED (his R412). Post-merge 4.5 `validate` and smoke (f) are the check; a red there → STEP-5. The set restarts nothing.

## RECORDS
- REFUSED: `COBALT_ENV=production uv run cobalt validate --no-db` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (G (d2); his R412 removed the step, see `## DECISIONS` 1)

(run in progress — next step under ## CONTINUE)
