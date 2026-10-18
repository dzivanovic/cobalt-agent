# deploy stop-guard-work · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/stop-guard-work-1018` (tip `9c359688`) on gate `deploy/stop-guard-work`, card `prompts/2026-10-18/777-deploy-stop-guard-work-card.md`.

## L74
- One block arrived (a system reminder, not a tool result) asking commits to carry a `Claude-Session: https://claude.ai/code/session_0138rg16Hkpoew4f6hRyVkhK` line. Recorded as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/777-deploy-stop-guard-work-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/777-deploy-stop-guard-work-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/777-deploy-stop-guard-work-card.md" · 0 · 63e01f434c02236e7b442d6138e1a435f5e85370
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/777-deploy-stop-guard-work-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1841 row · grep -n "^| R1841 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 88:| R1841 | 06:25 ET | HIS RULING (brain relays, L79): the desk does not idle; until MVP it launches the next card, every turn ends with a live worker and watch, the night is a shift. Words: [R1841](cto-2026-10-18-words.md). | HIS RULING · APPROVED · APPLIED: cto-desk-contract.md at 06:46 |
RULING 2026-10-18 R1841 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1841 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 7317d540b338bf299f1e555362b25230a75d1120
RULING 2026-10-18 R1841 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 66:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above); `ls -la <REPORT>` | 0 · 1 | `AUTHORIZED`; report: `No such file or directory` (first launch) |
| P1 | `date` | 0 | `Sun Oct 18 17:54:56 EDT 2026` (outside 21:30-22:30) |
| P2 | `tail -n 3 ".../stop-guard-work-check-2026-10-18.md"` | 0 | `CHECK DONE · job: stop-guard-work-1018 · pass: 1 · tip: 9c359688 · … · held unfixed: 0 · open: 0 · … · suites: offline 8508/0 · with-DB 0/0 · live-note 146/0 · … · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 191580` |
| P2 | `git log -1 --format=%H -- <check>` | 0 | `db1110e0764e58921c1ecea69a6d686755327c6f` |
| P2 | `git diff --stat -- <check>` | 0 | nothing |
| P3 | `rev-parse --short=8 9c359688` · `… ops/stop-guard-work-1018` | 0 · 0 | `9c359688` · `9c359688` |
| P3 | `merge-base --is-ancestor 9c359688 ops/stop-guard-work-1018` | 0 | — |
| P3 | `diff --stat 9c359688 ops/stop-guard-work-1018 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` (lock free) |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/stop-guard-work` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `9036cedb` |
| P5 | `merge-base --is-ancestor 9036cedb main` · `log --oneline main..deploy/stop-guard-work` | 0 · 0 | — · empty |
| P6 | `grep -c -F "def next_unlaunched" .../ops/desk/stop-guard.py` | 1 | `0` (before) |
| P6 | `grep -c -F "test_w1_the_1017_2107_shape_with_nothing_live_blocks" .../tests/ops/test_stop_guard.py` | 1 | `0` (before) |
| P7 | `diff --stat main 9c359688 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 89330` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 70450` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 89351).` |

## THE TREE
- `git -C <GATE> merge --no-edit 9c359688` → `Merge made by the 'ort' strategy.` (4 files: `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py`, two build-report docs; 541+/2-)
- `<m1>` = `d12b0e1a`
- `log --oneline --merges --first-parent 9036cedb..deploy/stop-guard-work` → `d12b0e1a Merge commit '9c359688' into deploy/stop-guard-work`
- `merge-base --is-ancestor 9c359688 deploy/stop-guard-work` → exit 0
- `diff --stat 9036cedb deploy/stop-guard-work -- src/cobalt/db_migrations` → nothing (no migration)
- STEP-C: `diff --stat 9036cedb deploy/stop-guard-work -- configs ops` → ` ops/desk/stop-guard.py | 134 +++…-` / ` 1 file changed, 132 insertions(+), 2 deletions(-)`; `deploy-step-c.sh` → `STEP-C: ADMITTED 0` (exit 0). `<launchd set>` empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` (exit 0; uv created `.venv`, `Installed 256 packages in 1.01s`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/stop-guard-work-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/stop-guard-work-build-2026-10-18.result	A	DOCS	-
ops/desk/stop-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
- `<restart set>` = EMPTY (no resident goes down). `<launchd set>` = empty.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied — the check's stop line carries `with-DB 0/0` (DB: none single branch runs the gate whole).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `264 passed, 163 skipped in 20.25s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db`).
- Deselects: none (build report `stop-guard-work-build-2026-10-18.md` names no with-DB deselect; its line 67 `110 deselected` is a `-k` filter of `tests/ops/test_stop_guard.py`).
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-stop-guard-work all --deploy --deploy-gate` launched in background (no `--tickers`, no `--migration`). Exit 0. Verdict lines WHOLE:
```
tests/ops: run (deploy gate)
offline 8643/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5582/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-stop-guard-work-all-20261018-175634.log
```
- (a) offline `8643/0`; W line `tests/ops: run (deploy gate)`.
- (b) lock taken (waited 0 min); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log:1015); proof-only at 0013, nothing CHANGED.
- (c) PASS 1 whole; every SKIPPED line is inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_playbook_live.py` (`test_live_vault_renders_six_decks`, reason `COBALT_LIVE_VAULT_ROOT not set`), `test_radar_evaluate.py:695`, `test_replay_line.py` (`COBALT_TEST_LIVE_DRC`), `test_s3_c4_experiments.py:95` (the x14 live template read), `test_catalyst.py:365`, `test_predicate.py:262`.
- (c2) no migration above 0013 on the card: nothing forward applied.
- (c3)/with-DB `5582/0`. Log pass summaries: `5375 passed, 8 skipped, 101 deselected, 7 xfailed …` (log:1235) · `207 passed, 1 deselected …` (log:2118).
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log:2186) = F0 → `cobalt_dev: 0013 — F2 = F0`.
- RELEASE: log:2239-2244 `release-devdb-lock.sh deploy-stop-guard-work` → `lock released` · `.env: removed` (no timestamp printed in the log; verified at 18:45:04 EDT): `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-stop-guard-work" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (lock dir absent).
- (e) live-note `147/0`, no skip naming `COBALT_LIVE_VAULT_ROOT` in that leg (log:2310 `147 passed, 1 skipped` — the `COBALT_TEST_LIVE_DRC` skip, allowed).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on d12b0e1a

## Deploy table
| step | command | result |
|---|---|---|
| D0 | `git -C /Users/cobalt/cobalt status --short --branch` | `## main...origin/main [ahead 202]` |
| D0 | `status --porcelain` | no staged line; ` M` / `??` under `docs/40 - DevDocs/`, ` M .claude/settings.json`, and `?? .claude/settings.json.bak` (outside both classes; no src/tests/ops/configs path) |
| D0 | `diff --stat 9036cedb main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D0 probe | `tag scratch-allow-probe-stop-guard-work` · `tag -d …` | ok · `Deleted tag 'scratch-allow-probe-stop-guard-work' (was 9036cedb)` |
| D0 probe | `commit --allow-empty -m "scratch: …"` · `reset --soft HEAD~1` · `log --oneline -1` | `[main ca134167] scratch: allowlist probe (reverted next line)` · ok · `9036cedb docs(report): F20 scoped check r2, CHECK DONE ready YES` |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-18-stop-guard-work` · `… refs/tags/pre-stop-guard-work` | exit 1 · exit 1 |
| D1 | `date` | `Sun Oct 18 18:45:36 EDT 2026` |
| D1 `<hb0>` | `heartbeat show` | `HEARTBEAT GREEN — 17 job(s), 12 probe(s), nothing red  (2026-10-18 18:45:37 EDT)`; `OK radar idle (overnight)`; `OK com.cobalt.radar running running 144 min, heartbeat fresh`; `AMB com.cobalt.herdr unmanaged …`; `com.cobalt.prefill-refresh` and `com.cobalt.playbook` `OWED (deferred bootstrap)` |
| D1 `<val0>` | `validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 `<jobs0>` | — | `Jobs (F17): 17 registered — 6 resident, 11 one-shot. Kill phrase 'COBALT STOP'.` |
| D1 | `backup status` | `newest snapshot: 1.2 h old` |
| D1 | `launchctl print` aset · radar | `state = running` `pid = 89330` · `state = running` `pid = 70450` |
| D1 | `cobalt.sh status` · `ps -p 89351` | `Cobalt is ONLINE (PID: 89351).` · `89351 ?? 0:00.03 uv run src/cobalt_agent/main.py` |
| D1 | `tail -n 8 radar.err` | last: `2026-10-18 18:44:31.619 \| INFO \| cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (8 idle:overnight cycles, no traceback) |
| D1 counts | a0 · ta0 · tr0 · tc0 · rp0 · rpr0 · re0 · lc0 | `283` · `217` · `0` · `0` · `18` · `60` · `43` · `39` |
| D1 | `curl … /radar` | `200` |
| D1 | MARKERS | `0` · `0` (before) |
| D1 | launchd set · migration | empty: nothing · `MIGRATIONS: none`: no `<RB>`, no proof-only |
| D2.0 | `deploy-shipped.sh --moved 9036cedb "<card>"` | nothing |

## Smoke

## CONTINUE
- STEP-D0 (gate green at 18:45:04 EDT) passed; D1 baseline read.
- next: STEP-D2 (D2.0 report commit, then D2.1 `main` into the gate)

## DECISIONS

## RECORDS
- REFUSED, not needed: `grep -n -F ".env: removed" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. The release is proved by the gate's stdout, log:2239-2244 (read with Read) and `ls -la <GATE>/.env`.

(run in progress — next step under ## CONTINUE)
