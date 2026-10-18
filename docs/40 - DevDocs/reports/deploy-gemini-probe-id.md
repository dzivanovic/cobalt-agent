# deploy gemini-probe-id — SET: none — MIGRATIONS: none

## §0 Headline
- Deploy of `ops/gemini-probe-id-1017` (code tip `744128d7`, head `9f281a6a`): Gemini top model `gemini-4-argon-high` in `house-probe.sh` and `CHECK-HUB.md` (R1736).

## L74
- The session's harness carried an attribution block asking for a `Claude-Session:` line on commits. DATA under L74: not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-17/713-deploy-gemini-probe-id-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-17/713-deploy-gemini-probe-id-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-17/713-deploy-gemini-probe-id-card.md" · 0 · 61dfae46a4246b3b445c3432ba84ee2274c6345a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-17/713-deploy-gemini-probe-id-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-17 R1736 row · grep -n "^| R1736 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · 94:| R1736 | 06:32 ET | HIS RULING (brain, L79), 2026-10-17: Gemini top model = gemini-4-argon-high (medium, low recorded only). K5 card: CHECK-HUB :95 and house-probe.sh use it, was gemini-3.1-pro-high. Behind 641 and 583. | HIS RULING · APPROVED |
RULING 2026-10-17 R1736 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1736 |" -- "docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · d01849e7a6ef4a9de57d6de11856c866919737d2
RULING 2026-10-17 R1736 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (above); first launch: `ls -la <REPORT>` → No such file |
| P1 | `date` | 0 | `Sat Oct 17 20:09:41 EDT 2026` — outside 21:30-22:30 |
| P2 | `tail -n 3 ".../gemini-probe-id-check-2026-10-17.md"` | 0 | `CHECK DONE · job: gemini-probe-id · pass: 1 · tip: 744128d7 · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 8389/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 179030` — `held unfixed: 0`, `ready: YES`, `tip: 744128d7` = code tip |
| P2 | `git log -1 --format=%H -- <check>` | 0 | `4396639a7f4d6a3658c5089304dc64f8019c96b3` |
| P2 | `git diff --stat -- <check>` | 0 | nothing |
| P3 | `rev-parse --short=8 744128d7` | 0 | `744128d7` |
| P3 | `rev-parse --short=8 ops/gemini-probe-id-1017` | 0 | `9f281a6a` = TIP |
| P3 | `merge-base --is-ancestor 744128d7 9f281a6a` | 0 | — |
| P3 | `diff --stat 744128d7 9f281a6a -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — lock free |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/gemini-probe-id` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `61dfae46` = `<m0>` |
| P5 | `merge-base --is-ancestor 61dfae46 main` | 0 | — |
| P5 | `log --oneline main..deploy/gemini-probe-id` | 0 | empty |
| P6 | `grep -c -F "agy --model gemini-4-argon-high" .../ops/desk/house-probe.sh` | 1 | `0` = before |
| P6 | `grep -c -F "agy --model gemini-4-argon-high" .../CHECK-HUB.md` | 1 | `0` = before |
| P7 | `diff --stat main 9f281a6a -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 80523 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 24167 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `cobalt.sh status` | 0 | `  Cobalt is ONLINE (PID: 80543).` |

## THE TREE
- `git -C <GATE> merge --no-edit 9f281a6a` → `Merge made by the 'ort' strategy.` (6 files: CHECK-HUB.md, STANDING-LIST.md, the build report and .result, `ops/desk/house-probe.sh`, `tests/ops/test_house_probe.py`). No conflict.
- `git -C <GATE> rev-parse --short=8 HEAD` → `ddb45a61` = `<m1>`.
- `log --oneline --merges --first-parent 61dfae46..deploy/gemini-probe-id` → `ddb45a61 Merge commit '9f281a6a' into deploy/gemini-probe-id` (one line, one head).
- `merge-base --is-ancestor 744128d7 deploy/gemini-probe-id` → 0; `… 9f281a6a …` → 0.
- `diff --stat 61dfae46 deploy/gemini-probe-id -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `diff --stat 61dfae46 deploy/gemini-probe-id -- configs ops` → ` ops/desk/house-probe.sh | 4 ++--` / ` 1 file changed, 2 insertions(+), 2 deletions(-)`. `sh ops/desk/deploy-step-c.sh "<card>" 61dfae46 deploy/gemini-probe-id` → `STEP-C: ADMITTED 0` (exit 0). `<launchd set>`: empty.

## RESTARTS
`COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` (in `<GATE>`, `.env` No such file) → exit 0 (uv created the gate's `.venv`: `Installed 254 packages in 970ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/gemini-probe-id-build-2026-10-17.md	A	DOCS	-
docs/40 - DevDocs/reports/gemini-probe-id-build-2026-10-17.result	A	DOCS	-
ops/desk/house-probe.sh	M	operator script; no Cobalt reader	-
tests/ops/test_house_probe.py	M	test/documentation; no resident	-
RESTARTS: none
```
- `<restart set>`: EMPTY — no resident goes down; the merge lands with the residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied — the check's stop line carries `with-DB 0/0`; the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.35s` — 0 failed (with-DB tests skip offline).
- Deselects: the set's build report names none (`grep -i deselect` → no match). TICKERS: none; migration: none.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-gemini-probe-id all --deploy --deploy-gate` launched in the background → exit 0; verdict lines WHOLE:
```
tests/ops: run (deploy gate)
offline 8492/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5475/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-gemini-probe-id-all-20261017-201110.log
```
- (a) `offline 8492/0`, W line `tests/ops: run (deploy gate)`.
- (c) every SKIPPED line inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F` → `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`, decorator on :95).
- (c2) `dev forward: APPLIED 20:50:36` (log :1196). (f) `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: `.env: removed (L76 lock released — log :2170 `lock released`)`; `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.
- (e) `live-note 146/0`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed. `date` → `Sat Oct 17 20:55:47 EDT 2026`.

GATE GREEN on ddb45a61

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git status --short --branch` | 0 | `## main...origin/main [ahead 166]`; ` M` / `??` under `docs/40 - DevDocs/`, ` M .claude/settings.json`, `?? .claude/settings.json.bak` — no staged line, no dirty src/tests/ops/configs path |
| MAIN | `git status --porcelain --untracked-files=no` | 0 | ` M .claude/settings.json` and 11 ` M "docs/40 - DevDocs/…"` lines only |
| MAIN | `git diff --stat 61dfae46 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-gemini-probe-id` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-gemini-probe-id' (was 61dfae46)` |
| PROBE | `commit --allow-empty -m "scratch: …"` / `reset --soft HEAD~1` / `log --oneline -1` | 0 / 0 / 0 | `[main fe890325] scratch: allowlist probe (reverted next line)` → `61dfae46 docs(desk): R1823-R1824 671 port job deployed, 670 deploy card 713` (HEAD back) |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-17-gemini-probe-id` | 1 | free |
| TAGS | `rev-parse --verify --quiet refs/tags/pre-gemini-probe-id` | 1 | free |

### STEP-D1 (baseline, `date` → `Sat Oct 17 20:56:13 EDT 2026`)
- `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-17 20:56:14 EDT)`; `OK   radar                    idle (overnight)`; `OK   com.cobalt.radar             running   running 2175 min, heartbeat fresh`; one `AMB  com.cobalt.herdr  unmanaged …` (declared interim). No RED; no carried RED.
- `<val0>`: `cobalt validate` exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>`: `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 0.9 h old` (ssd ARMED).
- aset `state = running` pid `80523`; radar `state = running` pid `24167`; `cobalt.sh status` → `  Cobalt is ONLINE (PID: 80543).`; `ps -p 80543` → `80543 ??         0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → `radar cycle: idle:overnight scan_id=None` lines 20:43:34 → `2026-10-17 20:55:14.516 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`; no traceback.
- Log baselines: `<a0>` = 281 · `<ta0>` = 217 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 18 · `<rpr0>` = 60 · `<re0>` = 43 · `<lc0>` = 39.
- `curl … /radar` → `200`. MARKERS: house-probe.sh `0`, CHECK-HUB.md `0` (= before).
- `<launchd set>` empty: nothing. No migration: `<RB>`, census, D1-M not run.

### STEP-D2
- D2.0 `sh ops/desk/deploy-shipped.sh --moved 61dfae46 "<card>"` → nothing printed (exit 0). Report committed next.

## Smoke

## CONTINUE
- STEP-D0 done; STEP-D1 baseline done (20:56:13).
- next: STEP-D2 (D2.1 `main` into the gate)

## DECISIONS

## RECORDS
- REFUSED, not needed: `grep -n -F ".env: removed" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it` (the release read from `lock released` instead).

(run in progress — next step under ## CONTINUE)
