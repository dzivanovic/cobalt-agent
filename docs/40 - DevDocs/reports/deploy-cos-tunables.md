# deploy-cos-tunables — JOB cos-tunables · SET cos-tunables · MIGRATIONS none

Card: `docs/40 - DevDocs/prompts/2026-10-20/967-deploy-cos-tunables-card.md` · hub: `DEPLOY-HUB.md` · seat: deploy-hub-cos-tunables · model claude-opus-5-5 · started Wed Oct 21 02:34:49 EDT 2026.

## §0 Headline
(filled at the stop)

## L74
- A system notice in this session asked commits to carry a `Claude-Session:` line. It is recorded here as data and not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/967-deploy-cos-tunables-card.md"`, exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/967-deploy-cos-tunables-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/967-deploy-cos-tunables-card.md" · 0 · ddf5a6d35a0aae94f9bba78c34e4e92729f2e425
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/967-deploy-cos-tunables-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 first launch | `ls -la ".../reports/deploy-cos-tunables.md"` | 1 | `No such file or directory` |
| P0 authorization | `authorize.sh deploy "<card>"` | 0 | `AUTHORIZED` (above) |
| P1 date | `date` | 0 | `Wed Oct 21 02:34:49 EDT 2026`: outside the 21:30–22:30 ET backup window |
| P2 check line | `tail -n 3 ".../cos-tunables-check-fr1-2026-10-21.md"` | 0 | `CHECK DONE · job: cos-tunables · pass: 1 · tip: 0b8bf093 · … · held unfixed: 0 · open: 1 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 181651`: carries `held unfixed: 0` and `ready: YES`; `tip: 0b8bf093` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/cos-tunables-check-fr1-2026-10-21.md"` | 0 | `36b474f6fcb4208b6d433f3b692fb79bbe27b293` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 0b8bf093` | 0 | `0b8bf093` |
| P3 branch head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-tunables` | 0 | `0b8bf093` (= `TIP`) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 0b8bf093 0b8bf093` | 0 | — |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 0b8bf093 0b8bf093 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`: no session holds the lock |
| P5 gate status | `git -C /Users/cobalt/cobalt-wt/deploy-cos-tunables status --short --branch` | 0 | `## deploy/cos-tunables` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-cos-tunables rev-parse --short=8 HEAD` | 0 | `ddf5a6d3` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor ddf5a6d3 main` | 0 | — |
| P5 nothing ahead | `git -C /Users/cobalt/cobalt log --oneline main..deploy/cos-tunables` | 0 | empty |
| P6 marker 1 | `grep -c -F "enabled: false" ".../configs/cobalt/jobs.yaml"` | 0 | `1` (before `1`) |
| P6 marker 2 | `grep -c -F "DEFAULT (brain; his word may change it)" ".../taxonomy/tunables.yaml"` | 1 | `0` (before `0`) |
| P6 marker 3 GET | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/hitl` | 0 | `200` (an HTTP status from aset) |
| P6 marker 3 grep | `grep -c -F "https://cobalt.taild24291.ts.net" ".../taxonomy/tunables.yaml"` | 1 | `0` (before `0`) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 0b8bf093 -- src/cobalt/db_migrations` | 0 | nothing: no migration, `MIGRATIONS: none` holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 41813` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 22089` |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |
| P8 agent retired? | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 2 | `No such file or directory`: not retired; every agent read stands as written |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-cos-tunables merge --no-edit 0b8bf093` → `Merge made by the 'ort' strategy.` (17 files changed, 887 insertions(+), 32 deletions(-)): configs/cobalt/jobs.yaml, configs/cobalt/taxonomy/tunables.yaml, src/cobalt/heartbeat/probes.py, src/cobalt/heartbeat/runner.py, four tests/cobalt test files, docs.
- `rev-parse --short=8 HEAD` → `cda5b61f` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent ddf5a6d3..deploy/cos-tunables` → `cda5b61f Merge commit '0b8bf093' into deploy/cos-tunables` (one line, one head).
- `merge-base --is-ancestor 0b8bf093 deploy/cos-tunables` → exit 0.
- `diff --stat ddf5a6d3 deploy/cos-tunables -- src/cobalt/db_migrations` → nothing: no migration path (`MIGRATIONS: none`).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat ddf5a6d3 deploy/cos-tunables -- configs ops` →
```
 configs/cobalt/jobs.yaml              | 16 ++++++++--------
 configs/cobalt/taxonomy/tunables.yaml | 10 +++++-----
 2 files changed, 13 insertions(+), 13 deletions(-)
```
- `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" ddf5a6d3 deploy/cos-tunables` → exit 0, whole: `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-cos-tunables` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD`, exit 0, whole (after the uv venv creation lines `Using CPython 3.14.3 … Installed 257 packages in 841ms`):
```
path	change	rule	restart
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
docs/40 - DevDocs/cobalt/heartbeat/probes.md	M	DOCS	-
docs/40 - DevDocs/cobalt/heartbeat/runner.md	M	DOCS	-
docs/40 - DevDocs/cobalt/hitl/README.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-2026-10-20.result	A	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-fr1-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-fr1-2026-10-20.result	A	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-fr3-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-fr3-2026-10-20.result	A	DOCS	-
src/cobalt/heartbeat/probes.py	M	static import reach	com.cobalt.radar
src/cobalt/heartbeat/runner.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_cos_offline.py	M	test/documentation; no resident	-
tests/cobalt/test_cos_probes.py	M	test/documentation; no resident	-
tests/cobalt/test_cos_registry.py	M	test/documentation; no resident	-
tests/cobalt/test_sheet_daymode_probe.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row.
- NOT LOADED: `launchctl print gui/501/com.cobalt.cos` → exit 113, `Could not find service "com.cobalt.cos" in domain for user gui: 501`.
- com.cobalt.cos: not loaded — skipped
- `<deferred set>`: empty. `com.cobalt.agent`: not recorded retired (P8), not in the derived set.
- **`<restart set>` = `com.cobalt.aset com.cobalt.radar`** · `<launchd set>` = empty.

## L68 GATE
- EQUAL-TREE CLAUSE: one branch, but `git -C /Users/cobalt/cobalt diff --stat 0b8bf093 cda5b61f -- . ":(exclude)docs"` prints 8 files (configs/cobalt/rules.yaml, ops/desk/deploy-outage.sh, ops/desk/deploy-step0.sh, ops/desk/desk-launch.sh, four tests/ops files; 630 insertions, 13 deletions: `main` moved since the check's base) → the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `265 passed, 163 skipped in 20.80s`: 0 failed (the with-DB tests skip offline).
- Deselects: the set's build reports name no deselection of their own (`grep -c -F "deselect"` → fr1 `0`, fr3 `0`; the base build's one hit, `:148`, quotes the gate's own pass-1 command built from `ops/desk/gate-lists.md`, which carries `test_tenancy.py::TestMigrationRoundTrip`: `grep -c` → `2`). No `--deselect`, `--tickers` or `--migration` is added.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-cos-tunables all --deploy --deploy-gate` (background) → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 9029/0
lock: waited 1 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5875/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-cos-tunables-all-20261021-023651.log
```
- (a) offline `9029/0`; W line `tests/ops: run (deploy gate)`.
- (b) lock taken (`lock: waited 1 min`); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:1048`); proof-only at `0013`, nothing CHANGED.
- (c) pass 1, every SKIPPED line inside the allowed set, matched by test and reason: test_cards_picks.py `:388` and `:401`; test_radar_evaluate.py `:695`; test_catalyst.py `:365`; test_predicate.py `:262`; the `COBALT_LIVE_VAULT_ROOT not set` skips of test_playbook_live.py (`test_live_vault_renders_six_decks`), test_checkpoints_live.py (`test_dry_run_finds_the_heading_in_real_notes`) and test_s3_c4_experiments.py (`test_x14_…`); the `COBALT_TEST_LIVE_DRC` skip of test_replay_line.py.
- (c2) forward: none (`MIGRATIONS: none`, no migration above `0013` in the tree). (c3) with-DB total `5875/0`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:2330`) = F0 → `cobalt_dev: 0013 — F2 = F0` (log `:2384`).
- THE RELEASE: `.env: removed (L76 lock released at the gate's end, log :2386 "lock released"; the log carries no clock for it)`. `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-cos-tunables" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) live-note `148/0`: only the `COBALT_TEST_LIVE_DRC` skip, no skip naming `COBALT_LIVE_VAULT_ROOT` (log tail: `148 passed, 1 skipped`).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on cda5b61f (03:26:07 EDT)

## Deploy table
### STEP-D0 (03:26 EDT)
- `git -C /Users/cobalt/cobalt status --short --branch` → first line `## main...origin/main [ahead 31]`.
- `status --porcelain`: every line is ` M` / `??` under `docs/40 - DevDocs/` or ` M .claude/settings.json`, plus one `?? .claude/settings.json.bak` (an untracked file outside src/tests/ops/configs; it is in the status before this session; see `## DECISIONS` 1). No staged line, no dirty src/tests/ops/configs path.
- `git -C /Users/cobalt/cobalt diff --stat ddf5a6d3 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-cos-tunables` → ok; `tag -d` → `Deleted tag 'scratch-allow-probe-cos-tunables' (was dfd0ae61)`; `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 8ea67e90] …`; `reset --soft HEAD~1` → ok; `log --oneline -1` → `dfd0ae61 docs(desk): card 968 deploy f5-x3-values-port` (HEAD back).
- TAGS: `rev-parse --verify --quiet refs/tags/deploy-2026-10-21-cos-tunables` → exit 1; `refs/tags/pre-cos-tunables` → exit 1.

### STEP-D1 baseline (`date` → Wed Oct 21 03:26:39 EDT 2026)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-21 03:26:40 EDT)`. RED lines, whole:
  - `RED  archiver                 last run FAILED — last run 2026-10-21 00:54 UTC (6.5 h ago), rows written 3373447, exit 1`
  - `RED  com.cobalt.archiver          failed    RuntimeError: 5 archiver failure(s): WBD/i1: Fetch failed for WBD/i1: Finviz HTTP failed: Client error '400 Bad Request' for url 'https://elite.finviz.com/export/stock?t=WBD&p=i1&auth=[REDACTED:url_query_secret]'`
  - `RED  com.cobalt.replay            failed    ReplayError: archiver not done: state 'failed'` (+ traceback head)
  - These are not the aset / sheet / radar probe: named, not a stop. aset-side: `OK sheet HTTP … -> 200`, `OK sheet daymode`, `OK com.cobalt.aset running loaded, pid 41813`; `OK radar idle (overnight)`; `OK com.cobalt.radar running running 606 min, heartbeat fresh`; `OK com.cobalt.agent running pid 35845`; `OK cos unknown — NOT PROBED, registry enabled: false`; `OK hitl unknown — NOT PROBED, registry enabled: false (com.cobalt.cos)`; `OK com.cobalt.cos disabled registered but NOT LOADED BY DESIGN`. AMB `com.cobalt.herdr` (declared interim). Five OWED labels (prefill-refresh, checkpoint-0715/0745/0815/0845, playbook) read OK as OWED.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` with `NOT LOADED BY DESIGN (1): com.cobalt.cos`.
- `backup status` → `newest snapshot: 2.4 h old` (ssd ARMED; b2 off).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 41813` = `<aset pid>`; `…/com.cobalt.radar` → `state = running`, `pid = 22089` = `<radar pid>`; `…/com.cobalt.cos` → exit 113, still `Could not find service`.
- `cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).`; `ps -p 35845` → `35845 ?? 0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, the last `2026-10-21 03:26:23.503`; no traceback.
- LOG BASELINES: `<a0>` 291 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS: `enabled: false` → `1`; `DEFAULT (brain; …)` → `0`; `/hitl` → `200`; `https://cobalt.taild24291.ts.net` in tunables → `0`. All their `before` values.
- THE LAUNCHD SET: empty, nothing read. No migration: no `<RB>`, no D1-M, no census.

## Smoke

## CONTINUE
next: STEP-D2 (D0 and D1 done 03:27 EDT; `deploy-shipped.sh --moved ddf5a6d3 "<card>"` printed nothing; this commit is D2.0)

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` is on `main`'s porcelain, outside D0's ACCEPTED list (docs/40 untracked/modified, `configs/cobalt/rules.yaml`, `.claude/settings.json`) and outside its REFUSED list (a staged line; a dirty src/, tests/, ops/, configs/ path). Is it a refusal? [03:26 EDT] Safe default taken: not a refusal. It is untracked, outside every shipped path, in the session's opening git status, and the merge is `--ff-only` of committed trees, so the file never enters a commit. The desk may want to name it in D0's list.

## RECORDS

(run in progress — next step under ## CONTINUE)
