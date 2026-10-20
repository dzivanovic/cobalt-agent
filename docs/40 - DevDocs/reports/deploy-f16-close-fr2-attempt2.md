# deploy f16-close-fr2-attempt2 · SET: f16-close · MIGRATIONS: none

## §0 Headline
Stopped at smoke (s), rollback USED. Gate green on `3eb11d1f` (offline 8829/0 · with-DB 5722/0 · live-note 147/0). It landed `06ac5a16` at 00:40:00: validate green, markers 1/1/1, residents up.
The card's smoke read `COBALT_ENV=production uv run cobalt validate --no-db` was REFUSED by `dontAsk` (only the bare `… validate` string is on the line), so → STEP-5: one revert `f7c03d0c`, `<pre-merge>` code proven restored, aset/radar UP on the old code, no new RED, no growing count.
Next (the desk's): fix the card's smoke string (DECISION 1), then re-land with `revert --no-edit f7c03d0c` on a new deploy, or recut.

## L74
- One block arrived as a system reminder mid-session asking that commits carry a `Claude-Session: https://claude.ai/code/session_01WewWYdF19oRUPGGBSqxrsv` line. Recorded here as DATA; none acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/886-deploy-f16-close-attempt2-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/886-deploy-f16-close-attempt2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/886-deploy-f16-close-attempt2-card.md" · 0 · 8df17f21ba1fa05c0e5105156ee2a4e8326143e1
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/886-deploy-f16-close-attempt2-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
AUTHORIZED
```
RULINGS: none.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 first launch | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Mon Oct 19 23:47:32 EDT 2026` (outside 21:30-22:30) |
| P2 check line | `tail -n 3 ".../f16-close-fr2-check-2026-10-19.md"` | 0 | `CHECK DONE · job: f16-close-fr2 · pass: 1 · tip: 6fb73789 · … · held unfixed: 0 · open: 2 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 188453` — carries `held unfixed: 0`, `ready: YES`, `tip: 6fb73789` = code tip |
| P2 committed | `git log -1 --format=%H -- "<check>"` | 0 | `421dab090d2411a4c93c60b937679901ee4afb7b` |
| P2 clean | `git diff --stat -- "<check>"` | 0 | (nothing) |
| P3 code tip | `rev-parse --short=8 6fb73789` | 0 | `6fb73789` |
| P3 head | `rev-parse --short=8 ops/f16-close-fr2` | 0 | `7c5f76a3` = TIP |
| P3 ancestor | `merge-base --is-ancestor 6fb73789 7c5f76a3` | 0 | — |
| P3 docs only | `diff --stat 6fb73789 7c5f76a3 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` (lock free) |
| P5 gate | `git -C <GATE> status --short --branch` | 0 | `## deploy/f16-close-fr2-attempt2` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `8df17f21` = `<m0>` |
| P5 m0 on main | `merge-base --is-ancestor 8df17f21 main` | 0 | — |
| P5 empty | `log --oneline main..deploy/f16-close-fr2-attempt2` | 0 | (empty) |
| P6 marker 1 | `grep -c -F "Playbook (F23): " .../cli.py` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "Daily refresh (F4): " .../cli.py` | 1 | `0` = before |
| P6 marker 3 | `grep -c -F "with no consumer (F16)" .../loader.py` | 1 | `0` = before |
| P7 | `diff --stat main 7c5f76a3 -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 35793` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 57565` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
- `git -C <GATE> merge --no-edit 7c5f76a3` → `Merge made by the 'ort' strategy.` (7 files, 323 insertions, 1 deletion: cli.md, loader.md, build report + .result, `src/cobalt/cli.py`, `src/cobalt/taxonomy/loader.py`, `tests/cobalt/test_f16_close_1018.py`)
- `git -C <GATE> rev-parse --short=8 HEAD` → `3eb11d1f` = `<m1>`
- `log --oneline --merges --first-parent 8df17f21..deploy/f16-close-fr2-attempt2` → `3eb11d1f Merge commit '7c5f76a3' into deploy/f16-close-fr2-attempt2` (one line, one head)
- `merge-base --is-ancestor 6fb73789 deploy/f16-close-fr2-attempt2` → exit 0; `… 7c5f76a3 …` → exit 0
- `diff --stat 8df17f21 deploy/f16-close-fr2-attempt2 -- src/cobalt/db_migrations` → (nothing): no migration, MIGRATIONS: none holds
- STEP-C: `diff --stat 8df17f21 deploy/f16-close-fr2-attempt2 -- configs ops` → (nothing). `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 8df17f21 deploy/f16-close-fr2-attempt2` → exit 0, `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` (from `<GATE>`, `.env` absent) → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/taxonomy/loader.md	M	DOCS	-
docs/40 - DevDocs/prompts/2026-10-18/731-f5-card.md	M	DOCS	-
docs/40 - DevDocs/reports/cto-2026-10-19.md	M	DOCS	-
docs/40 - DevDocs/reports/f16-close-fr2-build-2026-10-19.md	A	DOCS	-
docs/40 - DevDocs/reports/f16-close-fr2-build-2026-10-19.result	A	DOCS	-
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/taxonomy/loader.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_f16_close_1018.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
(preceded by uv's venv creation lines in the fresh gate: `Creating virtual environment at: .venv` · `Installed 257 packages in 993ms`). No `UNCLASSIFIED` row.
- NOT LOADED: `launchctl print gui/501/com.cobalt.cos` → exit 113, `Could not find service "com.cobalt.cos" in domain for user gui: 501`.
- com.cobalt.cos: not loaded — skipped
- `<restart set>` = `com.cobalt.aset com.cobalt.radar`
- `<deferred set>` = (empty) · `<launchd set>` = (empty)

## L68 GATE
- THE EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 6fb73789 3eb11d1f -- . ":(exclude)docs"` → `configs/cobalt/rules.yaml | 2 +-` · `tests/ops/test_hub_cos_restart_1019.py | 93 ++++` · `tests/ops/test_hub_deferred_1018.py | 4 +-` — not empty: the gate runs whole (`--deploy`).
- Deselects: the set's build report names none (`grep -i deselect` on `f16-close-fr2-build-2026-10-19.md` → no match).
- (a0) `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` (`.env` absent) → `264 passed, 163 skipped in 18.95s` — 0 failed (every skip a with-DB `Postgres env settings not available` / `requires_db`).
- THE GATE: `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-f16-close-fr2-attempt2 all --deploy --deploy-gate` (no `--deselect`, no `--tickers`, no `--migration`) → exit 0. Verdict lines WHOLE:
```
tests/ops: run (deploy gate)
offline 8829/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5722/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-f16-close-fr2-attempt2-all-20261019-234927.log
```
- (a) offline `8829/0`; W line `tests/ops: run (deploy gate)`.
- (c) every SKIPPED line inside the allowed set: `test_playbook_live.py:31` is the skip of `test_live_vault_renders_six_decks` (def at :32), reason `COBALT_LIVE_VAULT_ROOT not set`; `test_s3_c4_experiments.py:95` is `test_x14_live_his_template_strips_to_the_committed_fixture` (def at :96); the `test_replay_line.py` skip names `COBALT_TEST_LIVE_DRC`; the rest are the listed `file:line`s.
- (c2) log line 1262: `dev forward: APPLIED 00:31:21` (no migration above `0013` on this set). F0 (log line 1038): `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; final FINGERPRINT (log line 2330) `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
- (f) `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log `lock released` (line 2335), `.env: removed`. `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file (lock not this worktree's). The log line carries no time; the release lies between 00:31:21 and the gate's completion before 00:36:56.
- (e) live-note `147/0`, no skip naming `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 3eb11d1f

## Deploy table
### STEP-D0
- `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 34]`; `status --porcelain` → only ` M .claude/settings.json`, ` M`/`??` under `docs/40 - DevDocs/`, `?? .claude/settings.json.bak` — nothing staged, no dirty `src/` `tests/` `ops/` `configs/` path. (`.claude/settings.json.bak` is untracked outside the ACCEPTED list; not under src/tests/ops/configs, not staged: recorded, not a stop.)
- `diff --stat 8df17f21 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing).
- ALLOWLIST PROBE: `tag scratch-allow-probe-f16-close-fr2-attempt2` → ok; `tag -d …` → `Deleted tag 'scratch-allow-probe-f16-close-fr2-attempt2' (was 4f5680ff)`; `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main fb85cb0d] …`; `reset --soft HEAD~1` → ok; `log --oneline -1` → `4f5680ff docs(desk): R2128 F5 preflight r2 ready YES` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-19-f16-close-fr2-attempt2` → exit 1; `… refs/tags/pre-f16-close-fr2-attempt2` → exit 1.
### STEP-D1 (baseline, 00:37:27 ET)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-20 00:37:28 EDT)`. aset / sheet probes OK (`sheet HTTP http://127.0.0.1:5010/ -> 200`, `com.cobalt.aset running loaded, pid 35793`); radar OK (`radar idle (overnight)`, `com.cobalt.radar running running 805 min, heartbeat fresh`). REDs named, not a stop (none on aset / sheet / radar): `RED archiver last run FAILED — last run 2026-10-20 00:54 UTC (3.7 h ago), rows written 3369418, exit 1` · `RED com.cobalt.archiver failed RuntimeError: 5 archiver failure(s): WBD/i1: Fetch failed for WBD/i1: Finviz HTTP failed: Client error '400 Bad Request' …` · `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'` · `RED com.cobalt.generated failed GeneratedCommitRefused: … pre-commit: a deploy hub is live — no desk commit on main until its stop line: 79a459de deploy-hub-hub-cos-restart-fr1 …`. AMB `com.cobalt.herdr` unmanaged. OWED: `com.cobalt.prefill-refresh`, `com.cobalt.playbook` (deferred bootstrap).
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, last line `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 18 registered — 7 resident, 11 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 1.8 h old` (ssd local ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = `35793`; `launchctl print gui/501/com.cobalt.radar` → `state = running`, `<radar pid>` = `57565`; `launchctl print gui/501/com.cobalt.cos` → exit 113 `Could not find service` (still not loaded); `cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).`; `ps -p 35845` → `35845 ?? 0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → `radar cycle: idle:overnight scan_id=None` every ~100 s, last `2026-10-20 00:36:21.708`; no traceback.
- LOG BASELINES: `<a0>` = 284 · `<ta0>` = 217 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 18 · `<rpr0>` = 60 · `<re0>` = 43 · `<lc0>` = 39.
- `curl … /radar` → `200`. MARKERS → `0`, `0`, `0` (before).
- THE LAUNCHD SET: empty — nothing. No migration: `<RB>`, census and D1-M not run.
### STEP-D2
- D2.0: `deploy-shipped.sh --moved 8df17f21 "<card>"` → (nothing). Report committed `74b48b37 docs(report): deploy f16-close-fr2-attempt2 — gate green on 3eb11d1f`; `show --stat HEAD` → that one file (141 insertions). `<pre-merge>` = `74b48b37`.
- D2.1: `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (14 files, all under `docs/40 - DevDocs/`).
- D2.2: `<stack-final>` = `06ac5a16`; `rev-parse --short=8 06ac5a16^2` → `74b48b37` = `<pre-merge>`; `merge-base --is-ancestor 3eb11d1f 06ac5a16` → exit 0.
- D2.3: `diff --stat 3eb11d1f 06ac5a16 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing).
- D2.4: `backup status` → `newest snapshot: 1.8 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 9336.8 MB` · `ssd: snapshot 91539956 — 0 new / 3 changed, 18.8 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5: `date` → `Tue Oct 20 00:39:27 EDT 2026` (119 s after D1's 00:37:28 read); heartbeat `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-20 00:39:29 EDT)` — the same four RED lines as `<hb0>` (archiver probe, com.cobalt.archiver, com.cobalt.replay, com.cobalt.generated); aset `running loaded, pid 35793`, radar `running 807 min, heartbeat fresh`. No new RED.
- D2.6: `date` → `Tue Oct 20 00:39:33 EDT 2026`; `tag pre-f16-close-fr2-attempt2` at `74b48b37`.
### STEP-4 (the outage)
- 4.1 `<t down>` = `Tue Oct 20 00:39:43 EDT 2026`.
- 4.2 `launchctl bootout gui/501/com.cobalt.aset` → ok; print → exit 113 `Could not find service "com.cobalt.aset"`. `launchctl bootout gui/501/com.cobalt.radar` → ok; print → exit 113 `Could not find service "com.cobalt.radar"`. ORPHAN-CLEAN dry run `sh …/orphan-clean.sh aset` → `orphan-clean: aset · none found` — no kill. Agent not in the set: not stopped.
- 4.3 `rev-parse --short=8 HEAD` → `74b48b37` = `<pre-merge>`; `merge --ff-only deploy/f16-close-fr2-attempt2` → `Updating 74b48b37..06ac5a16` · `Fast-forward` (7 files, 323 insertions, 1 deletion).
- 4.4 migrations applied: none.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, last line `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 18 registered — 7 resident, 11 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`; new lines `Playbook (F23): latest_per_family None, rows_per_slide 8, why_max_chars 120, out_dir data/playbook.` and `Daily refresh (F4): units ['trading/market_table', 'market_calendar/market_calendar']; fields {'SPY': 'cobalt', 'QQQ': 'cobalt', 'IWM': 'cobalt', 'VIX': 'manual', 'BTC': 'manual'}.`
- 4.6 `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` → ok; `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` → ok. Print aset → `state = running`, `pid = 3222` (≠ 35793); print radar → `state = running`, `pid = 3232` (≠ 57565). `<t up>` = `Tue Oct 20 00:40:00 EDT 2026`. Downtime 17 s.
- 4.6L: `<launchd set>` empty — nothing.

### STEP-5 (rollback)
- (0) `date` → `Tue Oct 20 00:40:42 EDT 2026`.
- (1) `launchctl bootout gui/501/com.cobalt.aset` → ok; print → exit 113 `Could not find service "com.cobalt.aset"`. `launchctl bootout gui/501/com.cobalt.radar` → ok; print → exit 113 `Could not find service "com.cobalt.radar"`. Agent not in the set. Counts `<rp5>` 18 · `<rpr5>` 60 · `<re5>` 43 · `<lc5>` 39.
- (1L) `<launchd set>` empty — nothing.
- (2) `log --oneline -1` → `06ac5a16 Merge branch 'main' into deploy/f16-close-fr2-attempt2`. `git -C /Users/cobalt/cobalt revert --no-edit -m 2 06ac5a16` → `[main f7c03d0c] Revert "Merge branch 'main' into deploy/f16-close-fr2-attempt2"` · `7 files changed, 1 insertion(+), 323 deletions(-)`. PROOF: `diff --stat 74b48b37 HEAD -- . ':(exclude)docs'` → (nothing): `<pre-merge>` code restored.
- (2L) nothing. (2a)/(2b) no migration.
- (3) (residents restored; see below) `sh …/orphan-clean.sh aset` (dry run) → `orphan-clean: aset · none found`. `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` → ok; `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` → ok. Print aset → `state = running`, `pid = 3518`; radar → `state = running`, `pid = 3536`. Restored `Tue Oct 20 00:40:58 EDT 2026`. Second downtime 16 s (00:40:42 → 00:40:58).
### Summary row
| item | value |
|---|---|
| `<pre-merge>` → `<stack-final>` | `74b48b37` → `06ac5a16`; reverted by `f7c03d0c` |
| tags | `pre-f16-close-fr2-attempt2` at `74b48b37`; `deploy-2026-10-19-f16-close-fr2-attempt2` not set (no green smoke) |
| outage | `<t down>` 00:39:43 / `<t up>` 00:40:00 / 17 s; rollback 00:40:42 → 00:40:58 / 16 s |
| uv sync | none in production calls (`Resolved 267 packages` · `Audited 257 packages` in aset.err at each start); the gate's fresh venv: `Installed 257 packages in 993ms` |
| proof cost | no migration (gate's dev proof-only: `Proof cost: total 5.6 s`) |
| migrations applied | none |
| `<RB>` | none on this card |
| snapshot | `91539956` (ssd) |
| RESTARTS done | com.cobalt.aset com.cobalt.radar (twice: forward and rollback) |
| LAUNCHD done | none · BOOTSTRAP OWED: none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 06ac5a16` — USED this run → `f7c03d0c`. 2. SCHEMA: none (no migration). 3. RE-LAND (the desk's): `git -C /Users/cobalt/cobalt revert --no-edit f7c03d0c` — git titles it `Reapply "Merge branch 'main' into deploy/f16-close-fr2-attempt2"`; residents com.cobalt.aset com.cobalt.radar down first, up after |

## Smoke
### 4.7 on the landed tree 06ac5a16 (stopped at (s))
- FIRST CALLS after `<t up>` 00:40:00: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1).
- (a) `date` 00:40:12 · aset `pid = 3222`, radar `pid = 3232` (new, ≠ D1's) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).`
- (b) `Started server process` count 285 (= `<a0>` 284 + 1) · aset.err tail: `INFO:     Started server process [3222]` … `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)` · Traceback aset 217 (= `<ta0>`), radar 0 (= `<tr0>`), TaxonomyConfigError 0 (= `<tc0>`). Radar tails not reached (STEP-5 entered first).
- (c) `/` `200` · `/radar` `200` · `/radar\?frame=phone` `200`.
- (d) MARKERS → `1`, `1`, `1` (after values).
- (e) first read 00:40:22: `HEARTBEAT RED — 3 job(s) and 1 probe(s)` — the same four REDs as `<hb0>`; aset `running loaded, pid 3222`; radar `running 0 min, heartbeat fresh`. Second read not reached.
- (f) `jobs restarts 74b48b37..06ac5a16` → exit 0, `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`, no `UNCLASSIFIED`; minus `com.cobalt.cos: not loaded — skipped` = `<restart set>`. (validate at 4.5: exit 0.)
- (s) `COBALT_ENV=production uv run cobalt validate --no-db` → REFUSED: `Permission to use Bash has been denied because Claude Code is running in don't ask mode.` — RED → STEP-5.
### STEP-5 (4) on the reverted tree f7c03d0c
- (a) aset `state = running` `pid = 3518`, radar `state = running` `pid = 3536`; `cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).`
- (b) `Started server process` 286; aset.err tail: `INFO:     Finished server process [3222]` … `INFO:     Started server process [3518]` … `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)`; Traceback aset 217, radar 0; TaxonomyConfigError 0.
- (c) `/` `200` · `/radar` `200` · `/radar\?frame=phone` `200`.
- (e) first read `date` 00:41:14 → `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-20 00:41:15 EDT)`, the same four REDs as `<hb0>`, aset `pid 3518`, radar `running 0 min, heartbeat fresh`.
- (f) `COBALT_ENV=production uv run cobalt validate` → exit 0, last line `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 18 registered — 7 resident, 11 one-shot.` = `<jobs0>`; no `Playbook (F23)` / `Daily refresh (F4)` lines (old code). `jobs restarts 74b48b37..06ac5a16` → exit 0, `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`, no `UNCLASSIFIED`.
- (g) no migration.
- (e) second read `date` 00:43:06 (111 s after 00:41:15) → `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-20 00:43:09 EDT)` — the same four REDs as `<hb0>`; `com.cobalt.radar running running 2 min, heartbeat fresh`; aset `pid 3518`. No new RED.
- (b) radar tails: at 00:42:28 (+90 s) the last line `00:40:57.349 radar cycle: idle:overnight scan_id=None` (the restart's first cycle, 1 s before the `date` stamp); at 00:43:09 the tail adds `2026-10-20 00:42:37.371 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` — a cycle line stamped after `<t up>` 00:40:58, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, Traceback count 0 → GREEN.
- THE REVERT-READBACK (after the settled tail): `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39 = `<rp5>` `<rpr5>` `<re5>` `<lc5>` — no growing count. No census lines on this card.
- THE CHAIN: every check committed (P2) · tips re-read (P3) · merged tree `3eb11d1f` (T) · RESTARTS derived `com.cobalt.aset com.cobalt.radar` (R) · three suites green on `3eb11d1f` (G) · `06ac5a16` = `3eb11d1f` + docs (D2.3) · landed by ff (4.3) · markers 1/1/1 (d) · residents up with new pids (a) · validate green on the new tree (4.5) · BROKEN at (s): the card's read refused → STEP-5 → reverted `f7c03d0c`, residents UP on the old code, no new failure.

## CONTINUE
OUTAGE STARTING 00:39:33 — residents of com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- 4.6 ended 00:40:00, residents up on 06ac5a16. Smoke (s): the card's `COBALT_ENV=production uv run cobalt validate --no-db` REFUSED by the permission mode (`Permission to use Bash has been denied because Claude Code is running in don't ask mode.`) — a listed read a step names, refused (L62), and an (s) read failing = RED → STEP-5 now (rollback string, residents of com.cobalt.aset com.cobalt.radar down then up).
- STEP-5 done 00:43:09: reverted `f7c03d0c`, residents UP. This hub does nothing more after its stop line. The desk's next step: DECISION 1, then a re-land deploy or `desk-launch.sh recut "<card>"`.

## PRE-STOP SELF-CHECK
1. Every smoke row is quoted with its `date` (00:40:12 forward smoke; 00:41:14, 00:42:28, 00:43:06 rollback smoke), from this run's tool output.
2. P3 re-read `6fb73789` / `7c5f76a3`; `merge-base --is-ancestor` both into the gate branch exit 0; `3eb11d1f` ancestor of `06ac5a16` exit 0.
3. REVERT-READBACK shown (STEP-5 (4)): 18/60/43/39 = `<rp5>`…`<lc5>`. Every count, sha and `file:line` above was re-read from this run's tool output.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.`, D2.1 the same; the revert applied clean.

## DECISIONS
1. **The card's smoke read is not on this hub's launch line as typed** (blocks the next deploy of this set). The card's `## SMOKE READS` line is `COBALT_ENV=production uv run cobalt validate --no-db`; the line admits only `Bash(COBALT_ENV=production uv run cobalt validate)`, and `dontAsk` REFUSED the `--no-db` spelling (the hub's P8 note that an unstarred allow admits trailing arguments did not hold for this string). Every other proof was green on the landed tree (validate exit 0 with both `Playbook (F23): ` and `Daily refresh (F4): ` lines and `Placement (docs/PLACEMENT.md): tree clean.`; markers 1/1/1; residents new pids; curls 200; no new RED). Safe default taken: the hub's one path — STEP-5, ONE revert; no retry in another spelling (rule D, L62). The desk's fix before a recut: either the card's smoke read becomes `COBALT_ENV=production uv run cobalt validate` (already on the line; it carries the same three green lines), or `--no-db` is added as a listed string — a string change returns to him (R60). Not FOR DEJAN unless the desk takes the second route.

## RECORDS
- Downtime: outage 1 `00:39:43 → 00:40:00` (17 s); rollback `00:40:42 → 00:40:58` (16 s). Both under 300 s.
- REFUSED (listed, named by smoke (s)): `COBALT_ENV=production uv run cobalt validate --no-db` — `Permission to use Bash has been denied because Claude Code is running in don't ask mode.` → STEP-5.
- `cobalt_dev: 0013 (F2 = F0)` — from the gate log (`F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; final fingerprint equal).
- RETIRE OWED: none. BOOTSTRAP OWED (this run): none. `<launchd set>`: none.
- The carried RED as read (`<hb0>`, unchanged through every read): `archiver last run FAILED` · `com.cobalt.archiver failed RuntimeError: 5 archiver failure(s): WBD/i1 … Finviz HTTP failed: Client error '400 Bad Request'` · `com.cobalt.replay failed ReplayError: archiver not done` · `com.cobalt.generated failed GeneratedCommitRefused: … a deploy hub is live … 79a459de deploy-hub-hub-cos-restart-fr1` (that refusal names an earlier hub, `hub-cos-restart-fr1`, which K5 records as DEPLOYED — a stale guard read for the desk). No radar RED.
- `main` now: `f7c03d0c Revert "Merge branch 'main' into deploy/f16-close-fr2-attempt2"` above `06ac5a16`. RE-LAND, the desk's: `git -C /Users/cobalt/cobalt revert --no-edit f7c03d0c`. Tags: `pre-f16-close-fr2-attempt2` at `74b48b37`; `deploy-2026-10-19-f16-close-fr2-attempt2` NOT set.
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-f16-close-fr2-attempt2` and branch `deploy/f16-close-fr2-attempt2`; the set's branch `ops/f16-close-fr2` stays for the re-land / recut.
- `.claude/settings.json.bak` untracked on `main` at D0 (outside the ACCEPTED list, not src/tests/ops/configs, not staged): recorded.
- L74: the `Claude-Session:` request (see `## L74`) — not acted on.
- Card `## RECORDS`, copied:
  - f16-close-fr2: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f16-close-fr2-check-2026-10-19.md` last line: CHECK DONE · job: f16-close-fr2 · pass: 1 · tip: 6fb73789 · house A: Grok FINDINGS: 1 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 8825/0 · with-DB 5722/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 188453
  - f16-close-fr2: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f16-close-fr2` → `7c5f76a3`; code tip `6fb73789`
  - written by deploy-card.sh at 2026-10-19 23:47 ET (`date`); trial merge of the heads onto main in order: clean

FAILED: 4.7 (s) — the card's smoke read `COBALT_ENV=production uv run cobalt validate --no-db` refused by dontAsk (L62) · rollback: used — migrations applied: none — aset: UP — radar: UP — launchd: none · decisions: 1 · for Dejan: 0 · tokens: 207123
