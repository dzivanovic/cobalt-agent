# deploy f5-probe-x4-fix — set: f5-probe-x4-fix — migrations: none

## §0 Headline
- DEPLOYED `ops/f5-probe-x4-fix` (code tip `8525c6f7`, head `820a8f21`): `main` `c0ba6c7c` → `985b7740`, tag `deploy-2026-10-21-f5-probe-x4-fix`, rollback tag `pre-f5-probe-x4-fix`.
- Gate green on `3aae511e`: offline 9084/0 · with-DB 5930/0 · live-note 148/0; `cobalt_dev: 0013 — F2 = F0`.
- RESTARTS: com.cobalt.radar — down 22:45:19, up 22:45:30 (11 s); migrations: none; smoke GREEN.
- Held 22:37–22:43 off the nightly backup window (gate went green at 21:36, inside 21:30–22:30); two ASK DESK items, neither his.

## L74
- No block inside a tool result asked for a `Claude-Session:` line or any instruction. A harness system note (not a tool result) offered a `Claude-Session:` commit trailer; per L74 commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only, and none was added.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1009-deploy-f5-probe-x4-fix-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1009-deploy-f5-probe-x4-fix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/1009-deploy-f5-probe-x4-fix-card.md" · 0 · 9e83bf2ca01531c61311ea36e18b7190d98624d9
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/1009-deploy-f5-probe-x4-fix-card.md" · 0 · nothing
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
| FIRST LAUNCH | `ls -la ".../reports/deploy-f5-probe-x4-fix.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Wed Oct 21 20:46:32 EDT 2026` — outside 21:30-22:30 |
| P2 check last line | `tail -n 3 ".../reports/f5-probe-x4-fix-check-2026-10-21.md"` | 0 | `CHECK DONE · job: f5-probe-x4-fix · pass: 1 · tip: 8525c6f7 · house A: Grok FINDINGS: 0 · findings: 5 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9078/0 · with-DB 5924/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 11 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 177591` — carries `held unfixed: 0`, `ready: YES`, `tip: 8525c6f7` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/f5-probe-x4-fix-check-2026-10-21.md"` | 0 | `c7fde2906b7e7d5d56f59cf8359f2c8ded647643` |
| P2 unmodified | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 8525c6f7` | 0 | `8525c6f7` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f5-probe-x4-fix` | 0 | `820a8f21` = TIP |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 8525c6f7 820a8f21` | 0 | — |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 8525c6f7 820a8f21 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate status | `git -C /Users/cobalt/cobalt-wt/deploy-f5-probe-x4-fix status --short --branch` | 0 | `## deploy/f5-probe-x4-fix` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-f5-probe-x4-fix rev-parse --short=8 HEAD` | 0 | `9e83bf2c` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 9e83bf2c main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/f5-probe-x4-fix` | 0 | empty |
| P6 marker 1 | `grep -c -F "def _at_repo" /Users/cobalt/cobalt/src/cobalt/prefill/checkpoint_probe.py` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "X4_GROUPS_KEPT = " /Users/cobalt/cobalt/src/cobalt/prefill/checkpoint_probe.py` | 1 | `0` = before |
| P6 marker 3 | `grep -c -F "def test_fr3_x4_reaches_no_finviz" /Users/cobalt/cobalt/tests/cobalt/test_checkpoint_probe.py` | 1 | `0` = before |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 820a8f21 -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 6720` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 31938` |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` |
| P8 agent retired | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1` — `com.cobalt.agent recorded retired` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-f5-probe-x4-fix merge --no-edit 820a8f21` → `Merge made by the 'ort' strategy.` (5 files: `docs/40 - DevDocs/cobalt/prefill/checkpoints.md`, the build report and `.result`, `src/cobalt/prefill/checkpoint_probe.py`, `tests/cobalt/test_checkpoint_probe.py`; 455 insertions, 17 deletions).
- `git -C /Users/cobalt/cobalt-wt/deploy-f5-probe-x4-fix rev-parse --short=8 HEAD` → `3aae511e` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 9e83bf2c..deploy/f5-probe-x4-fix` → `3aae511e Merge commit '820a8f21' into deploy/f5-probe-x4-fix` (one line, one head).
- `merge-base --is-ancestor 8525c6f7 deploy/f5-probe-x4-fix` → exit 0; `merge-base --is-ancestor 820a8f21 deploy/f5-probe-x4-fix` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 9e83bf2c deploy/f5-probe-x4-fix -- src/cobalt/db_migrations` → nothing (no migration path; MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 9e83bf2c deploy/f5-probe-x4-fix -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 9e83bf2c deploy/f5-probe-x4-fix` → exit 0, whole output: `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
- `cd /Users/cobalt/cobalt-wt/deploy-f5-probe-x4-fix` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after uv created the gate venv: `Installed 257 packages in 651ms`), table whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/prefill/checkpoints.md	M	DOCS	-
docs/40 - DevDocs/reports/f5-probe-x4-fix-build-2026-10-21.md	A	DOCS	-
docs/40 - DevDocs/reports/f5-probe-x4-fix-build-2026-10-21.result	A	DOCS	-
src/cobalt/prefill/checkpoint_probe.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_checkpoint_probe.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
- No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.radar`. `<deferred set>` = none. `<launchd set>` = none. `com.cobalt.cos` not in the set (no NOT LOADED read needed). `com.cobalt.agent: recorded retired — not restarted` (not derived here either).

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 8525c6f7 3aae511e -- . ":(exclude)docs"` → `ops/desk/retired-labels | 1 +`, `src/cobalt/cos/run.py | 10 +++`, `tests/cobalt/test_cos_env_load.py | 177 +++…`, `3 files changed, 188 insertions(+)` — not equal; the gate runs whole (`--deploy`).
- Deselects: the build report (`f5-probe-x4-fix-build-2026-10-21.md:119`) names none (`no --deselect`); `TICKERS: none`; no `--migration`.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `265 passed, 163 skipped in 19.85s` — `0 failed` (every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-f5-probe-x4-fix all --deploy --deploy-gate` (background) → exit 0. Verdict lines WHOLE:
```
tests/ops: run (deploy gate)
offline 9084/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5930/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-f5-probe-x4-fix-all-20261021-204823.log
```
- (a) `offline 9084/0`; W line `tests/ops: run (deploy gate)`.
- (c) every SKIPPED line is inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_checkpoints_live.py` (`test_dry_run_finds_the_heading_in_real_notes`, `COBALT_LIVE_VAULT_ROOT not set`), `test_playbook_live.py` (`COBALT_LIVE_VAULT_ROOT not set`), `test_radar_evaluate.py:695`, `test_replay_line.py` (`COBALT_TEST_LIVE_DRC`), `test_s3_c4_experiments.py` (`COBALT_LIVE_VAULT_ROOT not set`), `test_catalyst.py:365`, `test_predicate.py:262`.
- (c2) `grep -n -F "dev forward" <log>` → `1278:dev forward: APPLIED 21:31:06`. Proof tables (`:1352`, `:2322`): `content UNCHANGED on every table`; no `CHANGED` row.
- (c3) `with-DB 5930/0`.
- (f) `F0:` `:1049` `664 35 272c95bbb12241e3611e4b36326ccf87`; `F2:` `:2332` `664 35 272c95bbb12241e3611e4b36326ccf87` → `cobalt_dev: 0013 — F2 = F0` (`:2386`).
- THE RELEASE: `:2387-2392` `release-devdb-lock.sh deploy-f5-probe-x4-fix` → `lock released`; `.env: removed`. `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-f5-probe-x4-fix" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) `live-note 148/0`, no skip naming `COBALT_LIVE_VAULT_ROOT` in that leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.
- GATE GREEN on 3aae511e (`date` → `Wed Oct 21 21:36:43 EDT 2026`)

## STEP-D0
- `git -C /Users/cobalt/cobalt status --short --branch` → first line `## main...origin/main [ahead 180]`. `status --porcelain` → no staged line; ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` under `docs/40 - DevDocs/` — and one ` M "docs/30 - Design/archiver-runs.md"` (see `## DECISIONS` 1). No dirty `src/`, `tests/`, `ops/`, other `configs/` path.
- `git -C /Users/cobalt/cobalt diff --stat 9e83bf2c main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-f5-probe-x4-fix` → ok · `tag -d …` → `Deleted tag 'scratch-allow-probe-f5-probe-x4-fix' (was 9e83bf2c)` · `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 73a9f90f] scratch: allowlist probe (reverted next line)` · `reset --soft HEAD~1` → ok · `log --oneline -1` → `9e83bf2c docs(desk): deploy card 1009 f5-probe-x4-fix, TIP 820a8f21` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-21-f5-probe-x4-fix` → exit 1; `… refs/tags/pre-f5-probe-x4-fix` → exit 1.
- `date` → `Wed Oct 21 21:37:19 EDT 2026` — inside the nightly backup window 21:30-22:30; D2.4's `backup run` stays off it → HOLD before D1 until 22:30 (`## DECISIONS` 2).
- Heartbeat at the hold (information, not D1's baseline): `HEARTBEAT RED — 2 job(s)  (2026-10-21 21:37:20 EDT)`; REDs: `com.cobalt.agent not loaded` (recorded retired) and `com.cobalt.replay failed StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings …`; aset / sheet / radar probes OK (`radar idle (overnight)`, `com.cobalt.radar running 86 min, heartbeat fresh`).

## STEP-D1 (after the hold; `date` → `Wed Oct 21 22:43:00 EDT 2026`)
- `<hb0>`: `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s)  (2026-10-21 22:43:02 EDT)`; REDs: `RED  com.cobalt.agent             not loaded NOT LOADED in launchd …` (recorded retired) and `RED  com.cobalt.replay            failed    StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings top_n Field required …` — named, not a stop (neither aset / sheet nor radar). `OK sheet HTTP http://127.0.0.1:5010/ -> 200`; `OK radar idle (overnight)`; `OK com.cobalt.aset running loaded, pid 6720`; `OK com.cobalt.radar running running 151 min, heartbeat fresh`; `OK com.cobalt.cos running running 125 min, heartbeat fresh`; `OK com.cobalt.backup done last finish 2026-10-21 21:41 ET, exit 0`. No radar RED (carried family not present).
- `<val0>`: `COBALT_ENV=production uv run cobalt validate` → exit 0, `13 trade_def(s) validated OK from the vault.`, `Placement (docs/PLACEMENT.md): tree clean.`, no `docs/_inflight/` line. `<jobs0>`: `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 1.0 h old` (ssd ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 6720` = `<aset pid>` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 31938` = `<radar pid>` · `/Users/cobalt/cobalt/cobalt.sh status` → `  Cobalt is OFFLINE.` (recorded retired; no `ps -p`).
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, last `2026-10-21 22:41:36.172`.
- LOG BASELINES: `<a0>` = 293 · `<ta0>` = 217 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 18 · `<rpr0>` = 60 · `<re0>` = 80 · `<lc0>` = 39.
- `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` → `200`. MARKERS → `0`, `0`, `0` (each its `before`).
- THE LAUNCHD SET: empty — nothing. MIGRATIONS: none — no `<RB>`, no D1-M.

## Deploy table
| step | command | result |
|---|---|---|
| D2.0 | `deploy-shipped.sh --moved 9e83bf2c "<card>"` | nothing |
| D2.0 | report commit | `[main c0ba6c7c] docs(report): deploy f5-probe-x4-fix — gate green on 3aae511e`; `show --stat HEAD` → the one report file |
| D2.0 | `rev-parse --short=8 main` | `c0ba6c7c` = `<pre-merge>` |
| D2.1 | `git -C <GATE> merge --no-edit main` | `Merge made by the 'ort' strategy.` (the report file only) |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` | `985b7740` = `<stack-final>`; `985b7740^2` → `c0ba6c7c` = `<pre-merge>`; `merge-base --is-ancestor 3aae511e 985b7740` → exit 0 |
| D2.3 | `diff --stat 3aae511e 985b7740 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D2.4 | `backup status` | `newest snapshot: 1.1 h old` |
| D2.4 | `date` · `backup run` | `22:43:53` · `backup: cobalt_brain dumped, 10193.7 MB` · `ssd: snapshot 4538e86f — 0 new / 2 changed, 25.0 MB added, 1 pruned` |
| D2.4 | `backup status` | `newest snapshot: 0.0 h old` (4538e86f newest) |
| D2.5 | `date` · `heartbeat show` | `22:45:03` · `HEARTBEAT RED — 2 job(s)  (2026-10-21 22:45:04 EDT)` — the same two REDs as `<hb0>` (agent, replay), 122 s after D1's read; aset / sheet / radar OK; no new RED |
| D2.6 | `date` · `tag pre-f5-probe-x4-fix` | `Wed Oct 21 22:45:08 EDT 2026` · tag at `c0ba6c7c` |
| 4.1 | `date` | `Wed Oct 21 22:45:19 EDT 2026` = `<t down>` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print gui/501/com.cobalt.radar` | ok · exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501`. aset not in the set (no bootout, no orphan-clean); agent recorded retired (no stop) |
| 4.3 | `rev-parse --short=8 HEAD` · `merge --ff-only deploy/f5-probe-x4-fix` | `c0ba6c7c` = `<pre-merge>` · `Updating c0ba6c7c..985b7740` / `Fast-forward` (5 files, 455+/17−) |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0, as `<val0>` (`13 trade_def(s) validated OK`, `Placement … tree clean`); `Jobs (F17): 22 registered — 7 resident, 15 one-shot.` = `<jobs0>`; no uv sync line |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · print | ok · `state = running`, `pid = 26270` ≠ 31938 |
| 4.6 | `date` | `Wed Oct 21 22:45:30 EDT 2026` = `<t up>` — downtime 11 s |
| 4.6L | — | `<launchd set>` empty — nothing |
| 7.1 | `git -C /Users/cobalt/cobalt tag deploy-2026-10-21-f5-probe-x4-fix` | after the green smoke; at `985b7740` |

- `<pre-merge>` `c0ba6c7c` → `<stack-final>` `985b7740` (main tip). Tags: `pre-f5-probe-x4-fix` (at `c0ba6c7c`), `deploy-2026-10-21-f5-probe-x4-fix` (at `985b7740`).
- `<t down>` 22:45:19 / `<t up>` 22:45:30 / 11 s. uv sync line: none at 4.5 (the gate venv's `Installed 257 packages` was at STEP-R, in `<GATE>`). Proof cost: none (no migration). `migrations applied: none`. `<RB>`: none. Snapshot: `4538e86f` (ssd).
- RESTARTS done: com.cobalt.radar. LAUNCHD done: none. BOOTSTRAP OWED: none from this run.
- THE ROLLBACK STRING: 1. CODE: `launchctl bootout gui/501/com.cobalt.radar` · `git -C /Users/cobalt/cobalt revert --no-edit -m 2 985b7740` · `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` (`Reapply "Merge branch 'main' into deploy/f5-probe-x4-fix"`).

## Smoke
- FIRST CALLS after `<t up>` 22:45:30: `<rp_up>` = 18 · `<rpr_up>` = 60 · `<re_up>` = 80 · `<lc_up>` = 39 (each = D1).
- (a) `date` 22:45:40 · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 6720` (outside the set: SAME pid) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 26270` (in the set: NEW, ≠ 31938) · `/Users/cobalt/cobalt/cobalt.sh status` → `  Cobalt is OFFLINE.` (recorded retired: OFFLINE is green). GREEN.
- (b) `grep -c "Started server process" …/aset.err` → `293` = `<a0>` (aset outside the set) · aset Traceback `217` = `<ta0>` · radar Traceback `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`. Radar tails below.
- (c) `curl … https://cobalt.taild24291.ts.net/` → `200` · `…/radar` → `200` · `…/radar\?frame=phone` → `200`. GREEN.
- (d) MARKERS → `1`, `1`, `1` (each its `after`). GREEN.
- (e) first read: `date` 22:45:56 · `heartbeat show` → `HEARTBEAT RED — 2 job(s)  (2026-10-21 22:45:57 EDT)`; REDs `com.cobalt.agent` and `com.cobalt.replay`, both in `<hb0>`; `OK com.cobalt.radar running running 0 min, heartbeat fresh`.
- (f) `COBALT_ENV=production uv run cobalt validate` → exit 0, as 4.5 (`13 trade_def(s) validated OK`, `Jobs (F17): 22 registered — 7 resident, 15 one-shot.`, `Placement … tree clean`) · `COBALT_ENV=production uv run cobalt jobs restarts c0ba6c7c..985b7740` → exit 0, `RESTARTS: com.cobalt.radar` = STEP-R's `<restart set>`, no `UNCLASSIFIED`. GREEN.
- (g) no migration — not applicable.
- (s) `ls /Users/cobalt/cobalt/src/cobalt/prefill/checkpoint_probe.py` → exit 0, listed · `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` → exit 0, listed (heartbeat still shows `com.cobalt.checkpoint-0715 OWED (deferred bootstrap) NOT LOADED` — on disk, unloaded). No `<launchd set>` dry run. Tests: quoted from the gate (`offline 9084/0`, `with-DB 5930/0`, `live-note 148/0`). GREEN.
- (b) radar tails: `date` 22:47:00 (+90 s) · `tail -n 12 …/radar.err` → last line `2026-10-21 22:45:29.645 … radar cycle: idle:overnight scan_id=None` (the new process's first cycle, 0.4 s before `<t up>` — not counted) · `date` 22:48:31 (+181 s) · `tail -n 12 …/radar.err` → `2026-10-21 22:47:09.664 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` — a cycle line after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → GREEN (settled; the +300 s tail not needed). `tail -n 30 …/aset.err` → last lines from 11:14 (aset outside the set, not restarted; no new `Started server process`).
- (e) second read: `date` 22:47:48 · `heartbeat show` → `HEARTBEAT RED — 2 job(s)  (2026-10-21 22:47:50 EDT)` (113 s after the first); REDs `com.cobalt.agent`, `com.cobalt.replay` only, both in `<hb0>`; `OK com.cobalt.radar running running 2 min, heartbeat fresh`. GREEN.
- (h) REVERT-READBACK, `date` 22:48:33 (`<t up>` + 183 s): `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 80 · `lifecycle card read failed` 39 — each = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, none growing; `curl … /radar` → `200`; radar Traceback `0`. No `census` reads on the card. GREEN.
- THE CHAIN: every check committed (P2: `c7fde290…`) → the tips re-read (P3: `8525c6f7`, `820a8f21`) → the merged tree (T: `3aae511e`, one merge, no migration) → RESTARTS derived (R: com.cobalt.radar) → three suites green on `<m1>` (G: 9084/0 · 5930/0 · 148/0) → `<stack-final>` `985b7740` = `<m1>` + docs (D2.3: nothing) → the landed code (4.3: `Updating c0ba6c7c..985b7740`) → markers 1/1/1 (d) → no migration (g) → radar up on a new pid after the merge (a) → radar cycling (b, e) → the set's reads (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).
- PRE-STOP SELF-CHECK: (1) every smoke row above quotes its output with its `date`; (2) `merge-base --is-ancestor 8525c6f7 985b7740` → exit 0, `merge-base --is-ancestor 820a8f21 985b7740` → exit 0, P3 re-read both; (3) (h) shown above; counts, shas and lines re-read from this run's tool output; (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), D2.1 clean — no conflict marker.

## CONTINUE
next: STEP-D2.1 (gate green at 21:36:43; D0, D1 done; D2.0 `deploy-shipped.sh --moved 9e83bf2c "<card>"` → nothing; this report committed at D2.0)
OUTAGE STARTING 22:45:08 — residents of com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
Outage ended 22:45:30 (radar up, pid 26270); smoke GREEN; tagged; closed at STEP-7. No next step for this session.

## DECISIONS
1. ASK DESK: `main` carries ` M "docs/30 - Design/archiver-runs.md"`, a dirty path outside the accepted `docs/40 - DevDocs/` set but not in D0's refused classes (staged, or dirty `src/` `tests/` `ops/` `configs/`) — is it accepted? Safe default taken: accepted (docs only, unstaged, not a shipped path, never committed by this run). [21:37:19]
2. ASK DESK: the gate went green at 21:36:43, inside the nightly backup window 21:30-22:30 that D2.4's `backup run` stays off (P1, brain R1295). Hold, or stop? Safe default taken: hold before D1 (so the baseline is fresh at the outage) until 22:30 or later; the hold is filled with background offline-suite runs on the gate tree (`.env` absent; the same leg as G (a)), then `date` + `heartbeat show` pairs. [21:37:19]

## RECORDS
- HOLD RUN (not a gate leg, not evidence): 21:37 `uv run pytest -q -p no:cacheprovider tests` (my own spelling, wider than the gate's) → `ERROR tests/test_finviz_extractor.py` / `Interrupted: 1 error during collection` — the old-tree `tests/` root, which the gate never collects (`ops/desk/gate-lists.md:24` runs `tests/cobalt tests/taxonomy`). Re-run at 21:38 with the gate's offline line.
- REFUSED, not needed: none. Messages not followed: none.
- Downtime: 11 s (com.cobalt.radar), under 300 s.
- `cobalt_dev: 0013 (F2 = F0)` — `664 35 272c95bbb12241e3611e4b36326ccf87` both.
- RETIRE OWED: none. BOOTSTRAP OWED: none from this run (heartbeat lists the earlier deferred labels prefill-refresh, checkpoint-0715/0745/0815/0845, playbook as OWED).
- Carried RED as read: no radar RED of the carried family. Standing REDs outside this set, named not stopped: `com.cobalt.agent` (recorded retired) and `com.cobalt.replay` (`TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings top_n Field required`) — the same at D1, D2.5 and both smoke reads.
- Clock filler between smoke reads: besides `date` + `heartbeat show` pairs I used `backup status`, `validate` and one `desk-context.sh` read (all read-only listed strings) — a wider filler than the rule's `date` + `heartbeat show`; recorded, nothing changed.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-f5-probe-x4-fix` and branch `deploy/f5-probe-x4-fix`; the set's branch `ops/f5-probe-x4-fix` and its worktree, if any.
- Card `## RECORDS` (the desk's), copied: f5-probe-x4-fix: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-probe-x4-fix-check-2026-10-21.md` last line: CHECK DONE · job: f5-probe-x4-fix · pass: 1 · tip: 8525c6f7 · house A: Grok FINDINGS: 0 · findings: 5 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9078/0 · with-DB 5924/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 11 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 177591 / f5-probe-x4-fix: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f5-probe-x4-fix` → `820a8f21`; code tip `8525c6f7` / written by deploy-card.sh at 2026-10-21 20:46 ET (`date`); trial merge of the heads onto main in order: clean.
- L74: no tool-result block arrived; see `## L74`.
- HOLD RUNS on the gate tree (`.env` absent each time): `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` ×4 → `4958 passed, 878 skipped, 4 xfailed` each (done 21:50, 22:02, 22:15, 22:27); `uv run pytest -q -rs -p no:cacheprovider tests/ops` → `4126 passed, 1 xfailed` (done 22:42). Window closed; D1 at 22:43:00. The nightly backup finished 21:41 ET (heartbeat `com.cobalt.backup`).

DEPLOYED deploy-2026-10-21-f5-probe-x4-fix 985b7740 | set: f5-probe-x4-fix | migrations: none | gate: offline 9084/0 · with-DB 5930/0 · live-note 148/0 | RESTARTS: com.cobalt.radar | smoke: GREEN | decisions: 2 · for Dejan: 0 · tokens: 223725
