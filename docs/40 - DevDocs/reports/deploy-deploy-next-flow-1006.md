# deploy-next-flow-1006 · set: workflow2 · migrations: none

## §0 Headline
- Deploy of `ops/next-flow-1006` (tip `987ab80d`, docs only: CHECK-HUB.md, BUILD-HUB.md, build report) per `DEPLOY-HUB.md`.
- In progress.

## L74
- A session context block asked for a `Claude-Session:` line in commits. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/09-deploy-next-flow-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/09-deploy-next-flow-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/09-deploy-next-flow-card.md" · 0 · 388159996c4a580863609efbf6d0820ac6818e92
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/09-deploy-next-flow-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R438 row · grep -n "^| R438 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 173:| R438 | 10-05 15:42 ET | HIS RULING: next flow (`next-flow-answer-2026-10-05.md`) only for features drafted after K3, P2, D5 DEPLOYED; after D5 a drafter writes changes 1-4 into the hubs (applied: contract, NOW 15:42; [words](cto-2026-10-05-words.md#r438)). | HIS RULING · APPROVED |
RULING 2026-10-05 R438 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R438 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 8e5b72b05c0c2566b49eb4b46d42969b4c4e5453
RULING 2026-10-05 R438 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above); report absent: `ls -la "<REPORT>"` | 0 · 1 | `AUTHORIZED` · `No such file or directory` (first launch) |
| P1 | `date` | 0 | `Tue Oct  6 02:50:46 EDT 2026` |
| P2 | `tail -n 3 ".../reports/next-flow-check-2026-10-06.md"` | 0 | `CHECK DONE · job: next-flow · pass: 1 · tip: 987ab80d · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 3932/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 8 · ready: YES · decisions: 1 · for Dejan: 1 · tokens: 144225` — carries `held unfixed: 0` and `ready: YES`; `tip: 987ab80d` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/next-flow-check-2026-10-06.md"` | 0 | `e782ae9f18790707d4b41066510dec77b9e83ff9` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/next-flow-check-2026-10-06.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 987ab80d` | 0 | `987ab80d` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/next-flow-1006` | 0 | `987ab80d` (= row, = `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 987ab80d ops/next-flow-1006` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 987ab80d ops/next-flow-1006 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-next-flow-1006 status --short --branch` | 0 | `## deploy/deploy-next-flow-1006` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-next-flow-1006 rev-parse --short=8 HEAD` | 0 | `39cebb60` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 39cebb60 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-next-flow-1006` | 0 | EMPTY |
| P6 | 12 `## MARKERS` greps | 0/1 | `0` `0` `1` `0` `0` `0` `0` `0` `0` `1` `1` `0` — each = its `before` |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main ops/next-flow-1006 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 79583` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 79594` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-next-flow-1006 merge --no-edit 987ab80d` → `Merge made by the 'ort' strategy.` (BUILD-HUB.md 12 +-, CHECK-HUB.md 76 +-, next-flow-build-2026-10-06.md 140 +; 3 files, 180 insertions, 48 deletions)
- `git -C /Users/cobalt/cobalt-wt/deploy-next-flow-1006 rev-parse --short=8 HEAD` → `e925caf9` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 39cebb60..deploy/deploy-next-flow-1006` → `e925caf9 Merge commit '987ab80d' into deploy/deploy-next-flow-1006` (one line, one head)
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 987ab80d deploy/deploy-next-flow-1006` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 39cebb60 deploy/deploy-next-flow-1006 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 39cebb60 deploy/deploy-next-flow-1006 -- configs ops` → nothing. No plist added, modified or removed.

## RESTARTS
- `cd /Users/cobalt/cobalt-wt/deploy-next-flow-1006` · `ls -la /Users/cobalt/cobalt-wt/deploy-next-flow-1006/.env` → `No such file or directory`
- `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created `.venv`, `Installed 253 packages in 612ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/next-flow-build-2026-10-06.md	A	DOCS	-
RESTARTS: none
```
- No `UNCLASSIFIED` row. `<restart set>` = EMPTY (none): no resident goes down; the merge lands with residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold — the check's stop line carries `with-DB 0/0` (no with-DB count above 0). The gate runs whole (`--deploy`).
- (a0) `ls -la .../deploy-next-flow-1006/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 162 skipped in 15.78s`; 0 failed (every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- Deselects: none (build report `next-flow-build-2026-10-06.md` names no `--deselect`; docs-only set). No `--tickers`, no `--migration` on the card.
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-next-flow-1006 all --deploy` → exit 0, verdict lines whole:
```
offline 3932/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4814/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-next-flow-1006-all-20261006-025244.log
```
- (a) offline `3932/0`. (c)/(c3) with-DB `4814/0`. (e) live-note `146/0`.
- SKIPPED lines, each inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py` (reason names `COBALT_TEST_LIVE_DRC`), `test_s3_c4_experiments.py:95` = `test_x14_live_his_template_strips_to_the_committed_fixture` (Grep: line 95 `@requires_live`, line 96 the def), `test_catalyst.py:365`, `test_predicate.py:262`. No other skip. Live-note leg: no skip naming `COBALT_LIVE_VAULT_ROOT` in its output.
- (b) log `877: F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; log 928 proof-only nothing CHANGED; `CHANGED` grep otherwise only the `content UNCHANGED` lines 1151 / 1825.
- (c2) log `1086: dev forward: APPLIED 03:15:30`.
- (f) log `1835: F2: 664 35 272c95bbb12241e3611e4b36326ccf87` = F0 field for field; `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log 1887–1892 `release-devdb-lock.sh deploy-next-flow-1006` → `lock released`, `.env: removed` (L76 lock released after F2, before the live-note leg; log line not time-stamped, run ended before 03:20:37). `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-next-flow-1006" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent). Log line 1882: `code: e925caf9 (clean)` = `<m1>`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on e925caf9

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 79]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; ` M` ×6 under `docs/40 - DevDocs/reports/` (brain-direction-2026-10-02, cto-2026-10-06, harness-mods-review-2026-10-03, lock-relief-decisions-2026-10-03, next-flow-answer-2026-10-05, seat-usage); `??` ×11 under `docs/40 - DevDocs/` (this report among them); `?? .claude/settings.json.bak` (see DECISIONS 1). No staged line; no dirty `src/` `tests/` `ops/` `configs/` path. |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat 39cebb60 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-deploy-next-flow-1006` · `tag -d …` | 0 · 0 | — · `Deleted tag 'scratch-allow-probe-deploy-next-flow-1006' (was 39cebb60)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 9ed8a6f2] scratch: …` · — · `39cebb60 docs(desk): flake-fix DEPLOYED 433e1c7e; R497 R498` (HEAD back) |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-06-next-flow` · `… refs/tags/pre-deploy-next-flow-1006` | 1 · 1 | free · free |

### STEP-D1 (baseline, 03:21:07)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 1 job(s)  (2026-10-06 03:21:08 EDT)`. aset / sheet probes OK (`sheet HTTP http://127.0.0.1:5010/ -> 200`, `com.cobalt.aset running loaded, pid 79583`); `radar idle (overnight)`, `com.cobalt.radar running running 162 min, heartbeat fresh`; `AMB com.cobalt.herdr unmanaged …`; the one RED, named (not aset, sheet or radar; not a stop): `RED  com.cobalt.generated  failed  GeneratedCommitRefused: \`git commit -m\` failed (exit 1): pre-commit: a deploy hub is live — no desk commit on main until its stop line: 9f093747 deploy-hub-deploy-p2-1005 Write by Edit / Write only; commit after DEPLOYED or FAILED, once the hub is stopped and removed. Traceback (most recent call las` (output ends there).
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0; `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.` `<jobs0>`: `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 0.6 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 79583`; `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 79594`; `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 8 × `radar cycle: idle:overnight scan_id=None`, 03:08:47 … 03:20:27; no traceback.
- LOG BASELINES: `<a0>` 45 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 58 · `<re0>` 40 · `<lc0>` 39.
- `curl … http://127.0.0.1:5010/radar` → `200`. `## MARKERS` again → `0 0 1 0 0 0 0 0 0 1 1 0`, each its `before`.
- No migration: `<RB>`, census and D1-M not run.

## CONTINUE
next: STEP-D2 (D2.0 commit)

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` is on `main`'s porcelain. D0's ACCEPTED list does not name it, and its REFUSED list (a staged line, or a dirty `src/` `tests/` `ops/` `configs/` path) does not either. Is it a stop? [03:20:54] Safe default taken: not a stop. It is untracked, outside every refused path and absent from the gate tree, so the ff-only merge cannot touch it. Its cleanup is the desk's.

## RECORDS
- 02:52:51 filler `COBALT_ENV=production uv run cobalt heartbeat show` typed with cwd = `<GATE>` (no `.env`) → exit 1 `FAILED: DbConfigError: Missing Postgres settings for the APP credential: POSTGRES_HOST, COBALT_DB_USER, COBALT_DB_PASSWORD. …` Not a refusal; nothing changed; production reads run from `/Users/cobalt/cobalt` (D1).

(run in progress — next step under ## CONTINUE)
