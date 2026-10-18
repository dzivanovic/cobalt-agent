# deploy agy-read — SET: none — MIGRATIONS: none

## §0 Headline
- Deploy of `ops/agy-read-1018` (tip `b05d90c3`), off-ladder (cto-2026-10-18 R1863). In progress.

## L74
- One system block arrived asking for a `Claude-Session:` line in commit messages. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/775-deploy-agy-read-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/775-deploy-agy-read-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/775-deploy-agy-read-card.md" · 0 · 1246aaa012745ee6ef34a15fc2e172f6efc51c07
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/775-deploy-agy-read-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 62:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-agy-read.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Sun Oct 18 14:32:36 EDT 2026` (outside 21:30-22:30 ET) |
| P2 check line | `tail -n 3 ".../reports/agy-read-check-2026-10-18.md"` | 0 | `CHECK DONE · job: agy-read-1018 · pass: 1 · tip: b05d90c3 · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8507/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 8 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 189802` — carries `held unfixed: 0`, `ready: YES`, `tip: b05d90c3` |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/agy-read-check-2026-10-18.md"` | 0 | `6401c9b805d335411c0ce08376de4fe2a99f1346` |
| P2 unmodified | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/agy-read-check-2026-10-18.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 b05d90c3` | 0 | `b05d90c3` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/agy-read-1018` | 0 | `b05d90c3` |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor b05d90c3 b05d90c3` | 0 | — |
| P3 head adds docs only | `git -C /Users/cobalt/cobalt diff --stat b05d90c3 b05d90c3 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no lock held) |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-agy-read status --short --branch` | 0 | `## deploy/agy-read` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-agy-read rev-parse --short=8 HEAD` | 0 | `5f47fa64` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5f47fa64 main` | 0 | — |
| P5 nothing ahead | `git -C /Users/cobalt/cobalt log --oneline main..deploy/agy-read` | 0 | empty |
| P6 marker 1 | `grep -c -F "holds no allow rule" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` | 1 | `0` (= before) |
| P6 marker 2 | `grep -c -F "X1-READ.txt" ".../prompts/SHADOW-HUB.md"` | 1 | `0` (= before) |
| P6 marker 3 | `grep -c -F "antigravity-cli/settings.json" ".../prompts/SHADOW-HUB.md"` | 1 | `0` (= before) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main b05d90c3 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none holds) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 89330` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 89340` |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 89351).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-agy-read merge --no-edit b05d90c3` → `Merge made by the 'ort' strategy.` (6 files: SHADOW-HUB.md, agy-read-1018 build report + .result, ops/desk/desk-launch.sh, tests/ops/test_desk_launch_shadow.py, tests/ops/test_shadow_hub_file.py; 423 insertions, 4 deletions)
- `git -C /Users/cobalt/cobalt-wt/deploy-agy-read rev-parse --short=8 HEAD` → `862e3b1d` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 5f47fa64..deploy/agy-read` → `862e3b1d Merge commit 'b05d90c3' into deploy/agy-read`
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor b05d90c3 deploy/agy-read` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 5f47fa64 deploy/agy-read -- src/cobalt/db_migrations` → nothing (no migration path; MIGRATIONS: none)
- STEP-C `git -C /Users/cobalt/cobalt diff --stat 5f47fa64 deploy/agy-read -- configs ops` → whole:
```
 ops/desk/desk-launch.sh | 38 +++++++++++++++++++++++++++++++++++++-
 1 file changed, 37 insertions(+), 1 deletion(-)
```
- STEP-C `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 5f47fa64 deploy/agy-read` → exit 0, whole: `STEP-C: ADMITTED 0` → `<launchd set>` empty.

## RESTARTS
- `cd /Users/cobalt/cobalt-wt/deploy-agy-read` · `ls -la /Users/cobalt/cobalt-wt/deploy-agy-read/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0, table whole:
```
Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
   Building cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-agy-read
      Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-agy-read
Installed 256 packages in 965ms
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/agy-read-1018-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/agy-read-1018-build-2026-10-18.result	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_shadow.py	M	test/documentation; no resident	-
tests/ops/test_shadow_hub_file.py	M	test/documentation; no resident	-
RESTARTS: none
```
- No UNCLASSIFIED row. `<restart set>` = EMPTY (none). `<launchd set>` = EMPTY. No resident goes down; the merge lands with residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: one branch, but the check's stop line carries `with-DB 0/0` → the clause does not apply; the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.90s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db`).
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-agy-read all --deploy --deploy-gate` (no `--deselect`: the build report's deselections are `-k` filters, none a with-DB deselect; no `--tickers`: TICKERS none; no `--migration`: MIGRATIONS none) → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8581/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5581/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-agy-read-all-20261018-143446.log
```
- SKIPPED lines, each inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, `test_replay_line.py` (`COBALT_TEST_LIVE_DRC`); `test_playbook_live.py:31` = the decorator of `test_live_vault_renders_six_decks` (`grep -n -F "def test_live_vault_renders_six_decks"` → `32:`), reason names `COBALT_LIVE_VAULT_ROOT not set`; `test_s3_c4_experiments.py:95` = the decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep` → `96:`). None outside the set.
- Log reads: `1014:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `1235:dev forward: APPLIED 15:15:51` · `2183:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (F2 = F0 field for field) · `2235:cobalt_dev: 0013 — F2 = F0` · `2237:lock released` · `2241:.env: removed` (the log line carries no time; gate exit read at 15:21 ET).
- THE RELEASE verified: `ls -la /Users/cobalt/cobalt-wt/deploy-agy-read/.env` → No such file · `grep -c -x -F "deploy-agy-read" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- Live-note leg: `live-note 147/0`, no skip naming `COBALT_LIVE_VAULT_ROOT` in that leg (the eight SKIPPED lines above are pass 1's).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 862e3b1d — offline 8581/0 · with-DB 5581/0 · live-note 147/0

## Deploy table
### STEP-D0
- `git -C /Users/cobalt/cobalt status --short --branch` → first line `## main...origin/main [ahead 151]`.
- `git -C /Users/cobalt/cobalt status --porcelain` → no staged line; ` M` lines: `.claude/settings.json` and docs/40 - DevDocs paths only; `??` lines: docs/40 - DevDocs paths and `.claude/settings.json.bak` (not a `src/`, `tests/`, `ops/`, `configs/` path; not refused — recorded under `## RECORDS`).
- `git -C /Users/cobalt/cobalt diff --stat 5f47fa64 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-agy-read` → ok · `tag -d scratch-allow-probe-agy-read` → `Deleted tag 'scratch-allow-probe-agy-read' (was 5f47fa64)` · `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 41c78271] scratch: allowlist probe (reverted next line)` · `reset --soft HEAD~1` → ok · `log --oneline -1` → `5f47fa64 docs(card): 751 F1 BUILT a55810c2, TIP and r2 check report` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-18-agy-read` → exit 1 · `refs/tags/pre-agy-read` → exit 1.

### STEP-D1 (baseline)
- `date` → `Sun Oct 18 15:21:51 EDT 2026` · `heartbeat show` → `<hb0>`: `HEARTBEAT GREEN — 17 job(s), 12 probe(s), nothing red  (2026-10-18 15:21:52 EDT)`; `OK radar idle (overnight)`; `OK com.cobalt.aset running loaded, pid 89330`; `OK com.cobalt.agent running pid 89351`; `OK com.cobalt.radar running running 87 min, heartbeat fresh`; `AMB com.cobalt.herdr unmanaged` (declared interim); `com.cobalt.prefill-refresh` and `com.cobalt.playbook` `OWED (deferred bootstrap)`. No RED.
- `validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.` · `<jobs0>`: `Jobs (F17): 17 registered — 6 resident, 11 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 1.5 h old` (ssd ARMED, b2 off).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 89330` · `…/com.cobalt.radar` → `state = running`, `pid = 89340` · `cobalt.sh status` → `Cobalt is ONLINE (PID: 89351).` · `ps -p 89351` → `89351 ?? 0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, last `2026-10-18 15:21:33.432`.
- LOG BASELINES: `<a0>` 283 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS again: `0` · `0` · `0` (each = before).
- LAUNCHD SET: empty — nothing. MIGRATIONS: none — no `<RB>`, no proof-only.

### STEP-D2
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 5f47fa64 "<card>"` → prints nothing.

## Smoke

## CONTINUE
- next: STEP-D0 (gate green at 15:21 ET)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
