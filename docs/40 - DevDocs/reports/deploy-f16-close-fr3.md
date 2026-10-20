# Deploy f16-close-fr3 · set: f16-close · migrations: none

## §0 Headline
- Deploy of `ops/f16-close-fr3` (code tip `1aea7418`, head `e7688a8f`) via gate `deploy/f16-close-fr3`. Card 895. In progress.

## L74
- none so far.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/895-deploy-f16-close-fr3-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/895-deploy-f16-close-fr3-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/895-deploy-f16-close-fr3-card.md" · 0 · 7810c14cba729237e9e9494ee3d985ba20b6f03d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/895-deploy-f16-close-fr3-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
AUTHORIZED
```
RULINGS: none.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la ".../reports/deploy-f16-close-fr3.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Tue Oct 20 03:37:54 EDT 2026` (outside 21:30-22:30) |
| P2 | `tail -n 3 ".../f16-close-fr3-check-2026-10-20.md"` | 0 | `CHECK DONE · job: f16-close-fr3 · pass: 1 · tip: 1aea7418 · house A: Grok FINDINGS: 1 · findings: 1 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8863/0 · with-DB 5758/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 16 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 195502` — carries `held unfixed: 0`, `ready: YES`, `tip: 1aea7418` = code tip |
| P2 | `git log -1 --format=%H -- "docs/40 - DevDocs/reports/f16-close-fr3-check-2026-10-20.md"` | 0 | `4a16fa191631ef54ee96dada5428a3c7176f277b` |
| P2 | `git diff --stat -- <check report>` | 0 | nothing |
| P3 | `git rev-parse --short=8 1aea7418` | 0 | `1aea7418` |
| P3 | `git rev-parse --short=8 ops/f16-close-fr3` | 0 | `e7688a8f` = row and `TIP` |
| P3 | `git merge-base --is-ancestor 1aea7418 e7688a8f` | 0 | — |
| P3 | `git diff --stat 1aea7418 e7688a8f -- . ":(exclude)docs"` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — lock free |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/f16-close-fr3` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `7810c14c` = `<m0>` |
| P5 | `git merge-base --is-ancestor 7810c14c main` | 0 | — |
| P5 | `git log --oneline main..deploy/f16-close-fr3` | 0 | empty |
| P6 | `grep -c -F "Playbook (F23): " .../src/cobalt/cli.py` | 1 | `0` = before |
| P6 | `grep -c -F "Daily refresh (F4): " .../src/cobalt/cli.py` | 1 | `0` = before |
| P6 | `grep -c -F "with no consumer (F16)" .../src/cobalt/taxonomy/loader.py` | 1 | `0` = before |
| P7 | `git diff --stat main e7688a8f -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 38353` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 38364` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
- `git -C <GATE> merge --no-edit e7688a8f` → `Merge made by the 'ort' strategy.` (7 files, 326 insertions, 1 deletion: `src/cobalt/cli.py`, `src/cobalt/taxonomy/loader.py`, `tests/cobalt/test_f16_close_1018.py`, 4 docs).
- `git -C <GATE> rev-parse --short=8 HEAD` → `29c12f7b` = `<m1>`.
- `git log --oneline --merges --first-parent 7810c14c..deploy/f16-close-fr3` → `29c12f7b Merge commit 'e7688a8f' into deploy/f16-close-fr3` (one line, one head).
- `merge-base --is-ancestor 1aea7418 deploy/f16-close-fr3` → exit 0; `merge-base --is-ancestor e7688a8f deploy/f16-close-fr3` → exit 0.
- `git diff --stat 7810c14c deploy/f16-close-fr3 -- src/cobalt/db_migrations` → nothing (no migration path; MIGRATIONS: none).
- STEP-C: `git diff --stat 7810c14c deploy/f16-close-fr3 -- configs ops` → nothing. `sh ops/desk/deploy-step-c.sh "<card>" 7810c14c deploy/f16-close-fr3` → exit 0, whole: `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the gate `.venv`: `Installed 257 packages in 851ms`), table whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/taxonomy/loader.md	M	DOCS	-
docs/40 - DevDocs/reports/f16-close-fr3-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/f16-close-fr3-build-2026-10-20.result	A	DOCS	-
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/taxonomy/loader.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_f16_close_1018.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No UNCLASSIFIED row. NOT LOADED: `launchctl print gui/501/com.cobalt.cos` → exit 113, `Could not find service "com.cobalt.cos" in domain for user gui: 501`.
- com.cobalt.cos: not loaded — skipped
- `<restart set>`: `com.cobalt.aset com.cobalt.radar`
- `<deferred set>`: empty · `<launchd set>`: empty

## L68 GATE
THE EQUAL-TREE CLAUSE holds: ONE branch in `TIP`; `git diff --stat 1aea7418 29c12f7b -- . ":(exclude)docs"` → nothing; the check's stop line carries `with-DB 5758/0` (> 0). The check's suite lines are the gate's, quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f16-close-fr3-check-2026-10-20.md` lines 145-164 (its `gate.sh f16-close-fr3 all --deploy --deploy-gate`, exit 0, on tip `1aea7418`):
```
tests/ops: run (deploy gate)
offline 8863/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5758/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f16-close-fr3-all-20261020-024650.log
```
SKIPPED read against the allowed set: all eight inside it (`test_cards_picks.py:388`, `:401`; the `test_playbook_live.py` skip naming `COBALT_LIVE_VAULT_ROOT not set`; `test_radar_evaluate.py:695`; the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`; the `test_s3_c4_experiments.py` live-template skip; `test_catalyst.py:365`; `test_predicate.py:262`). The check reports `grep -n -F "OUTSIDE" <log>` → nothing. (a)–(f) skipped by the clause.
- (a0) THE EARLY READ, run anyway: `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `264 passed, 163 skipped in 18.79s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db`).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.
- cobalt_dev: not taken by this run (the clause ran no with-DB leg); the check's `cobalt_dev: 0013 — F2 = F0` stands.

GATE GREEN on 29c12f7b

## Deploy table
STEP-D0 (03:39-03:40 EDT):
- `git status --short --branch` → `## main...origin/main [ahead 64]`; `status --porcelain` → only ` M` / `??` under `docs/40 - DevDocs/`, ` M .claude/settings.json`, and `?? .claude/settings.json.bak` (untracked, not under src/ tests/ ops/ configs/; recorded). No staged line.
- `git diff --stat 7810c14c main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-f16-close-fr3` → ok · `tag -d` → `Deleted tag 'scratch-allow-probe-f16-close-fr3' (was 7810c14c)` · `commit --allow-empty` → `[main f29b9d04] scratch: allowlist probe (reverted next line)` · `reset --soft HEAD~1` → ok · `log --oneline -1` → `7810c14c docs(prompts): F16 fr3 deploy card 895 (deploy-card.sh, bare validate smoke)`.
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-20-f16-close-fr3` → exit 1; `refs/tags/pre-f16-close-fr3` → exit 1.

STEP-D1 (`date` → `Tue Oct 20 03:40:23 EDT 2026`):
- `<hb0>` (`heartbeat show`, 03:40:25 EDT): `HEARTBEAT RED — 3 job(s) and 1 probe(s)`. Aset/sheet probes: `OK sheet HTTP http://127.0.0.1:5010/ -> 200`, `OK sheet daymode …`; radar: `OK radar idle (overnight)`, `OK com.cobalt.radar running running 106 min, heartbeat fresh`, `OK com.cobalt.aset running loaded, pid 38353`. REDs named, none on aset/sheet/radar: `RED archiver last run FAILED — last run 2026-10-20 00:54 UTC (6.8 h ago), rows written 3369418, exit 1`; `RED com.cobalt.archiver failed RuntimeError: 5 archiver failure(s): WBD/i1: … Finviz HTTP failed: Client error '400 Bad Request' …`; `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`; `RED com.cobalt.generated failed GeneratedCommitRefused: … pre-commit: a deploy hub is live — no desk commit on main until its stop line: 79a459de deploy-hub-hub-cos-restart-fr1 …`. OWED: `com.cobalt.prefill-refresh`, `com.cobalt.playbook` (deferred bootstrap). AMB: `com.cobalt.herdr` unmanaged.
- `<val0>` (`validate`): exit 0, last line `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 18 registered — 7 resident, 11 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 1.9 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = `38353`; `…/com.cobalt.radar` → `state = running`, `<radar pid>` = `38364`; `…/com.cobalt.cos` → exit 113 `Could not find service` (still not loaded); `cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).`; `ps -p 35845` → `35845 ?? 0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 logs/radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, last `2026-10-20 03:39:19.129`; no traceback.
- LOG BASELINES: `<a0>` 287 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS again → `0`, `0`, `0` (before).
- THE LAUNCHD SET: empty, nothing read. No migration: `<RB>`, census and D1-M not run.

## Smoke

## CONTINUE
next: STEP-D0 (gate green at 03:39:43 EDT)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
