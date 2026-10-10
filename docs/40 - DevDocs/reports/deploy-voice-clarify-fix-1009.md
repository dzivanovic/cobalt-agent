# deploy voice-clarify-fix-1009 · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/voice-clarify-fix-1009` (code tip `9feda305`, head `4465b758`) on `deploy/voice-clarify-fix-1009`. In progress.

## L74
- A system-reminder arriving mid-session asked that commits carry a `Claude-Session:` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/200-deploy-voice-clarify-fix-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/200-deploy-voice-clarify-fix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/200-deploy-voice-clarify-fix-card.md" · 0 · 4ab4e76035069e7e205653838a13ccd691b07088
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/200-deploy-voice-clarify-fix-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "<REPORT>"` | 1 | No such file or directory |
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| P1 DATE | `date` | 0 | Fri Oct  9 22:10:32 EDT 2026 |
| P2 check last line | `tail -n 3 ".../voice-clarify-fix-check-2026-10-09.md"` | 0 | `CHECK DONE · job: voice-clarify-fix-1009 · pass: 1 · tip: 9feda305 · … · held unfixed: 0 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 161041` — carries `held unfixed: 0` and `ready: YES`; `tip: 9feda305` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/voice-clarify-fix-check-2026-10-09.md"` | 0 | c6ef303f1bb813e11641708f3ea0bc8d665c1785 |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | (nothing) |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 9feda305` | 0 | 9feda305 |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/voice-clarify-fix-1009` | 0 | 4465b758 (= TIP) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 9feda305 4465b758` | 0 | — |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 9feda305 4465b758 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate status | `git -C /Users/cobalt/cobalt-wt/deploy-voice-clarify-fix-1009 status --short --branch` | 0 | `## deploy/voice-clarify-fix-1009` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `5fc1e9a4` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5fc1e9a4 main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/voice-clarify-fix-1009` | 0 | (empty) |
| P6 marker 1 | `grep -c -F "#cv-voice .cv-row[hidden]{display:none}" /Users/cobalt/cobalt/src/cobalt/voice/web.py` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "\"candidates\"" /Users/cobalt/cobalt/src/cobalt/voice/turn.py` | 1 | `0` = before |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 4465b758 -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 14669` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 14679` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 4465b758` → `Merge made by the 'ort' strategy.` (14 files, 287 insertions, 2 deletions: `src/cobalt/voice/{agent,tools,turn,web}.py`, four voice tests, one fixture, docs).
- `<m1>` = `13698c03` (`git -C <GATE> rev-parse --short=8 HEAD`).
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 5fc1e9a4..deploy/voice-clarify-fix-1009` → `13698c03 Merge commit '4465b758' into deploy/voice-clarify-fix-1009` (one line, one head).
- `merge-base --is-ancestor 9feda305 deploy/voice-clarify-fix-1009` → exit 0; `merge-base --is-ancestor 4465b758 deploy/voice-clarify-fix-1009` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 5fc1e9a4 deploy/voice-clarify-fix-1009 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 5fc1e9a4 deploy/voice-clarify-fix-1009 -- configs ops` → nothing. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the gate's `.venv`: `Installed 253 packages in 1.04s`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/voice/agent.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/tools.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/turn.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/web.md	M	DOCS	-
docs/40 - DevDocs/reports/voice-clarify-fix-build-2026-10-09.md	A	DOCS	-
src/cobalt/voice/agent.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/tools.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/turn.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_voice_plan.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_tools.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_turn.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_web.py	M	test/documentation; no resident	-
tests/fixtures/voice/plan-replies.constructed.yaml	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar` (agent not in the set).

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 9feda305 13698c03 -- . ":(exclude)docs"` → ` configs/cobalt/rules.yaml | 2 +-` — not empty, so the gate runs whole (`--deploy`).
- Deselects: the build report (`voice-clarify-fix-build-2026-10-09.md:125`) says `no --deselect: no with-DB test added`; none passed. TICKERS none, no `--migration`.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `262 passed, 163 skipped in 16.27s` (0 failed; the skips are the with-DB tests, absent `.env`).

- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-voice-clarify-fix-1009 all --deploy` (launched 22:12 ET, run_in_background) → exit 0. Verdict lines whole:
```
offline 4060/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4947/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-voice-clarify-fix-1009-all-20261009-221210.log
```
- (a) offline `<p>` = 4060, 0 failed.
- (c) the seven SKIPPED lines are all in the allowed set. `test_s3_c4_experiments.py:95` is the decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F` → `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`).
- (c2) log `:1096` `dev forward: APPLIED 22:35:03`. The proof tables at `:1162` and `:1957` read `content UNCHANGED on every table`. `grep -n -F "CHANGED"` shows no `CHANGED` verdict.
- (c3) with-DB `<d>` = 4947, 0 failed.
- (f) log `:2018` `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log `:2019–2023`, `release-devdb-lock.sh deploy-voice-clarify-fix-1009` → `lock released` → `.env` No such file. Re-checked by `ls -la <GATE>/.env` → No such file, and `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file. `.env: removed (L76 lock released, before 22:40:01 ET)`.
- (e) live-note `<l>` = 146, 0 failed. Its one skip names `COBALT_TEST_LIVE_DRC`, which is in the allowed set.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 13698c03

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| main branch | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 8]` |
| main dirty | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`, ` M` and `??` only under `docs/40 - DevDocs/`, plus `?? .claude/settings.json.bak` (not under `src/` `tests/` `ops/` `configs/`; recorded). No staged line. |
| main since cut | `git -C /Users/cobalt/cobalt diff --stat 5fc1e9a4 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | (nothing) |
| probe tag | `tag scratch-allow-probe-voice-clarify-fix-1009` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-voice-clarify-fix-1009' (was 5fc1e9a4)` |
| probe commit | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 7df81a88] scratch: …` → HEAD back at `5fc1e9a4 docs(desk): desk pane by id DEPLOYED, https and S4-P1 check reports (R795)` |
| TAG free | `rev-parse --verify --quiet refs/tags/deploy-2026-10-09-voice-clarify-fix` | 1 | — |
| rollback tag free | `rev-parse --verify --quiet refs/tags/pre-voice-clarify-fix-1009` | 1 | — |

### STEP-D1 (baseline, 22:40:28 EDT)
- `<hb0>` (`heartbeat show` 22:40:29): `HEARTBEAT RED — 2 job(s) and 1 probe(s)`. The REDs are `RED  archiver  last run FAILED — last run 2026-10-10 00:54 UTC (1.8 h ago), rows written 3308843, exit 1`, `RED  com.cobalt.archiver  failed  RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …` and `RED  com.cobalt.replay  failed  ReplayError: archiver not done: state 'failed'`. None is on the aset, sheet or radar probe: they are named here and do not stop the run. `OK sheet HTTP … -> 200` · `OK radar idle (overnight)` · `OK com.cobalt.aset running loaded, pid 14669` · `OK com.cobalt.radar running running 254 min, heartbeat fresh` · `OK com.cobalt.agent running pid 22243 alive`.
- `<val0>` (`validate`): exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 0.6 h old` (ssd local ARMED).
- aset `state = running`, `<aset pid>` = 14669 · radar `state = running`, `<radar pid>` = 14679 · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → `radar cycle: idle:overnight scan_id=None` every ~100 s, last at `2026-10-09 22:40:12.375`; no traceback.
- Log baselines: `<a0>` 54 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS: marker 1 → `0`, marker 2 → `0` (the before values).
- MIGRATIONS: none, so there is no `<RB>`, no census and no D1-M.

## CONTINUE
next: STEP-D2 (D2.0 commit)

(run in progress — next step under ## CONTINUE)
