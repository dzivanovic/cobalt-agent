# deploy-03d-1005 (attempt 3) · SET: workflow1 · MIGRATIONS: none

## §0 Headline
- Run in progress.

## L74
- none

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/14-deploy-03d-card.md"` → exit 0, whole output:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/14-deploy-03d-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/14-deploy-03d-card.md" · 0 · 0ab64eb00c4d8d836d51884fe41b674986675a14
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/14-deploy-03d-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R391 row · grep -n "^| R391 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 68:| R391 | 10-05 09:00 ET | HIS RULING (desk chat): commit R389 and R390; go on with the P6 read and the guard-b drafter; (d2) SKIPPED for the workflow deploy too (as R368). | APPROVED |
RULING 2026-10-05 R391 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R391 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · ed3cf41a8392be824396ace29672e7d92b8abaa4
RULING 2026-10-05 R391 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
RULING 2026-10-05 R392 row · grep -n "^| R392 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 70:| R392 | 10-05 09:03 ET | HIS RULING (desk chat): NO Grok read for 03d (the tip-file stage copy was classifier-denied); deploy 03d now; start the guard-b drafter. | APPROVED |
RULING 2026-10-05 R392 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R392 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 5583ead30b4f44f3d46aad3a8ee0f2bf043520d1
RULING 2026-10-05 R392 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
RULING 2026-10-05 R408 row · grep -n "^| R408 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 102:| R408 | 10-05 11:53 ET | HIS RULING (A): per-case window override naming `deploy-03d-1005`; deploy it now ([words](cto-2026-10-05-words.md#r408--his-window-override-for-deploy-03d-1005-10-05-1153-et-desk-chat)). | APPROVED |
RULING 2026-10-05 R408 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R408 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · be1114d4c53f768b00750daf96274a4d08f41455
RULING 2026-10-05 R408 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
First launch: `ls -la "<REPORT>"` → exit 1, `No such file or directory`.

| rule | command | exit | result |
|---|---|---|---|
| P0 | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (above) |
| P1 | `date` | 0 | `Mon Oct  5 11:55:01 EDT 2026` — window: (iv) R408, his per-case override naming `deploy-03d-1005` (this card's JOB) |
| P2 | `tail -n 3 ".../adoption-port-check-2026-10-05-r2.md"` | 0 | `CHECK DONE · job: adoption-port · pass: 1 · tip: 36fa02ad · house A: none (overruled 2026-10-02 R47) · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 17 · ready: YES · decisions: 1 · for Dejan: 1` — `held unfixed: 0`, `ready: YES`, tip `36fa02ad` = row |
| P2 | `git log -1 --format=%H -- "docs/.../adoption-port-check-2026-10-05-r2.md"` | 0 | `5d51caa623ad5375943e9acd43da67d277f6753c` |
| P2 | `git diff --stat -- "docs/.../adoption-port-check-2026-10-05-r2.md"` | 0 | nothing |
| P3 | `rev-parse --short=8 36fa02ad` | 0 | `36fa02ad` |
| P3 | `rev-parse --short=8 ops/adoption-port-1005` | 0 | `07655b9b` (= row, = TIP) |
| P3 | `merge-base --is-ancestor 36fa02ad 07655b9b` | 0 | — |
| P3 | `diff --stat 36fa02ad 07655b9b -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-03d-1005-attempt3` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `0ab64eb0` = `<m0>` |
| P5 | `merge-base --is-ancestor 0ab64eb0 main` | 0 | — |
| P5 | `log --oneline main..deploy/deploy-03d-1005-attempt3` | 0 | empty |
| P6 | `grep -c -F "args.no_db" .../src/cobalt/cli.py` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "validate --no-db" ".../DEPLOY-HUB.md"` | 1 | `0` (before `0`) |
| P7 | `diff --stat main 07655b9b -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 13209` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 36907` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| T merge | `git -C <GATE> merge --no-edit 07655b9b` | 0 | `Merge made by the 'ort' strategy.` — 5 files: `docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/reports/adoption-port-build-2026-10-05.md`, `src/cobalt/cli.py`, `tests/cobalt/test_validate_no_db.py` (534+, 47−) |
| `<m1>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `dbd295fd` |
| merges | `log --oneline --merges --first-parent 0ab64eb0..deploy/deploy-03d-1005-attempt3` | 0 | `dbd295fd Merge commit '07655b9b' into deploy/deploy-03d-1005-attempt3` |
| tip in | `merge-base --is-ancestor 36fa02ad deploy/deploy-03d-1005-attempt3` | 0 | — |
| head in | `merge-base --is-ancestor 07655b9b deploy/deploy-03d-1005-attempt3` | 0 | — |
| migrations | `diff --stat 0ab64eb0 deploy/deploy-03d-1005-attempt3 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| STEP-C | `diff --stat 0ab64eb0 deploy/deploy-03d-1005-attempt3 -- configs ops` | 0 | nothing — no plist added, changed or removed |

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created `.venv`, `Installed 253 packages in 629ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/adoption-port-build-2026-10-05.md	A	DOCS	-
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_validate_no_db.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
- `<restart set>` = `com.cobalt.radar`. No UNCLASSIFIED row.
- window: (iv) R408 at `Mon Oct  5 11:56:08 EDT 2026` (P1 named (iv), not (v); the set is non-empty and (iv) holds).

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold — the check's stop line carries no with-DB count (`suites: as built (no commit)`); the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 157 skipped in 15.36s` — 0 failed.
- (d2) SKIPPED this run only (his R391, card `## RECORDS`).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-03d-1005-attempt3 all --deploy` (no `--deselect`: the build report `adoption-port-build-2026-10-05.md:179` adds no with-DB test; no `--tickers`; no `--migration`) → exit 0. Verdict lines, whole:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-03d-1005-attempt3-all-20261005-115651.log
```
- (a) offline `3786 passed, 756 skipped, 1 xfailed` (log `:829`) → `offline 3786/0`.
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:846`); LEVEL 0013; proof-only nothing CHANGED.
- (c) PASS 1 whole: `4466 passed, 7 skipped, 67 deselected, 3 xfailed` (`:1051`) → `<d1>` = 4466. The 7 SKIPPED lines are all inside the allowed set (`test_s3_c4_experiments.py:95` is `test_x14_live_his_template_strips_to_the_committed_fixture`, def at `:96`).
- (c2) `dev forward: APPLIED 12:19:11` (`:1053`).
- (c3) PASS 2: `173 passed, 1 deselected` (`:1610`) → `<d2>` = 173; `with-DB 4639/0`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:1675`) = F0 → `cobalt_dev: 0013 — F2 = F0` (`:1726`).
- THE RELEASE: `lock released` (`:1728`), `.env: removed` (`:1732`); `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-03d-1005-attempt3" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) live-note `146 passed, 1 skipped` (`:1797`); the one skip is `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`, allowed) → `live-note 146/0`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on dbd295fd

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `status --short --branch` | 0 | `## main...origin/main [ahead 84]` |
| MAIN | `status --porcelain` | 0 | ` M .claude/settings.json`; ` M` ×5 and `??` ×11 under `docs/40 - DevDocs/` (this report among them); `?? .claude/settings.json.bak` (see `## DECISIONS`); nothing staged; no dirty `src/`, `tests/`, `ops/`, `configs/` path |
| MAIN | `diff --stat 0ab64eb0 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-deploy-03d-1005` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-deploy-03d-1005' (was 0ab64eb0)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main f1736515] …` · — · `0ab64eb0 docs(desk): RECUT deploy-03d-1005 attempt 3` |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-05-03d-attempt3` | 1 | absent |
| TAGS | `rev-parse --verify --quiet refs/tags/pre-deploy-03d-1005` | 1 | absent |

### STEP-D1 (baseline, `Mon Oct  5 12:24:49 EDT 2026`)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 1 probe(s)  (2026-10-05 12:24:50 EDT)`; the one RED: `RED  radar                    failed_stage bars: poll failures: 1` — THE CARRIED FAMILY: `com.cobalt.radar running … running 1186 min, heartbeat fresh`; `radar.err` last line `2026-10-05 12:22:57.141 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791217293863` (inside 5 min); radar Traceback count 0. Every other probe OK; `com.cobalt.herdr` AMB (declared interim, unmanaged). `sheet HTTP … -> 200`, `backup newest snapshot 2.3 h old across ssd`.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, `13 trade_def(s) validated OK`, `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` (`registry <-> ops/: 15 label(s), exact match.`; `registry <-> plists: schedules and COBALT_ENV agree on every job.`)
- `backup status` → `newest snapshot: 2.3 h old` (ssd ARMED; b2 off).
- aset `state = running`, `<aset pid>` = 13209 · radar `state = running`, `<radar pid>` = 36907 · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- LOG BASELINES: `<a0>` 42 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 58 · `<re0>` 39 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS again: `args.no_db` → `0`; `validate --no-db` → `0` (both before values).
- MIGRATIONS: none → no `<RB>`, no census, no D1-M.

## Smoke

## CONTINUE
- next: STEP-D2 (D0, D1 done)

## DECISIONS
- ASK DESK: D0 `status --porcelain` shows `?? .claude/settings.json.bak` — not on the accepted list, not in the refused classes (`src/`, `tests/`, `ops/`, `configs/`, staged). Safe default taken: go on (an untracked file outside the code tree; the ff-only merge does not touch it). [12:24 EDT]

## RECORDS

(run in progress — next step under ## CONTINUE)
