# deploy f4-refresh — SET: none — MIGRATIONS: none

Card: `docs/40 - DevDocs/prompts/2026-10-18/778-deploy-f4-refresh-card.md` · gate `deploy/f4-refresh-attempt2` at `/Users/cobalt/cobalt-wt/deploy-f4-refresh-attempt2` · TIP `7b291371` · TAG `deploy-2026-10-18-f4-refresh-attempt2`

## §0 Headline
- f4-refresh (`ops/f4-refresh-1018`, code tip `51b03e00`) is on `main`: `5623c3ff` → `54feb833`, tag `deploy-2026-10-18-f4-refresh-attempt2`, rollback tag `pre-f4-refresh`.
- Gate green on `db62c4b5`: offline 8539/0 · with-DB 5552/0 · live-note 146/0. MIGRATIONS none.
- aset and radar were restarted, down 28 s (12:42:45 to 12:43:13 ET). Smoke GREEN.
- STEP-C let the plist in this time: `com.cobalt.prefill-refresh` was merged with its bootstrap deferred. It is `BOOTSTRAP OWED` (gate X7, X8, X9, X10, X15) and a later bootstrap-only deploy loads it.

## L74
- A harness reminder in this session asked commit messages to end with a `Claude-Session:` line. Recorded as data, not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/778-deploy-f4-refresh-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/778-deploy-f4-refresh-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/778-deploy-f4-refresh-card.md" · 0 · 707d437391fb5718891c492c91ce6ba617337bd0
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/778-deploy-f4-refresh-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1833 row · grep -n "^| R1833 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 88:| R1833 | 06:19 ET | HIS RULING (brain relays, L79): "do everything you need, and I want to run everything that is being blocked." Brain: X1 first, gate holds only till the X1 row; launch every K5 gap-filler and job-clean now. | HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46 |
RULING 2026-10-18 R1833 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1833 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · d001e0937ca3731225cee781090eaf30d8d7feb7
RULING 2026-10-18 R1833 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P0 | `authorize.sh deploy` | 0 | `AUTHORIZED` (above) |
| P1 | `date` | 0 | `Sun Oct 18 11:51:20 EDT 2026` — outside 21:30-22:30 |
| P2 | `tail -n 3 ".../f4-refresh-check-2026-10-18.md"` | 0 | `CHECK DONE · job: f4-refresh-1018 · pass: 1 · tip: 51b03e00 · house A: Grok FINDINGS: 1 · findings: 3 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8538/0 · with-DB 5552/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 15 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 160500` — carries `held unfixed: 0`, `ready: YES`, tip `51b03e00` = row |
| P2 | `git log -1 --format=%H -- "docs/.../f4-refresh-check-2026-10-18.md"` | 0 | `220f03a11d7462cb5cfc9f30153dc7d2e0d740b7` |
| P2 | `git diff --stat -- "docs/.../f4-refresh-check-2026-10-18.md"` | 0 | nothing |
| P3 | `rev-parse --short=8 51b03e00` | 0 | `51b03e00` |
| P3 | `rev-parse --short=8 ops/f4-refresh-1018` | 0 | `7b291371` = row = TIP |
| P3 | `merge-base --is-ancestor 51b03e00 7b291371` | 0 | — |
| P3 | `diff --stat 51b03e00 7b291371 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/f4-refresh-attempt2` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `707d4373` = `<m0>` |
| P5 | `merge-base --is-ancestor 707d4373 main` | 0 | — |
| P5 | `log --oneline main..deploy/f4-refresh-attempt2` | 0 | empty |
| P6 | `grep -c -F "label: com.cobalt.prefill-refresh" .../jobs.yaml` | 1 | `0` = before |
| P6 | `grep -c -F "key: prefill.refresh_interval_min" .../tunables.yaml` | 1 | `0` = before |
| P6 | `grep -c -F "key: prefill.refresh_window" .../tunables.yaml` | 1 | `0` = before |
| P6 | `grep -c -F "id: K12.3" .../smoke/s2.yaml` | 1 | `0` = before |
| P7 | `diff --stat main 7b291371 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 80523` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 24167` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 80543).` |

## THE TREE
- `git -C <GATE> merge --no-edit 7b291371` → `Merge made by the 'ort' strategy.` (28 files changed, 2934 insertions(+), 115 deletions(-)); no conflict.
- `git -C <GATE> rev-parse --short=8 HEAD` → `db62c4b5` = `<m1>`.
- `log --oneline --merges --first-parent 707d4373..deploy/f4-refresh-attempt2` → `db62c4b5 Merge commit '7b291371' into deploy/f4-refresh-attempt2` (one line, one head).
- `merge-base --is-ancestor 51b03e00 deploy/f4-refresh-attempt2` → 0 · `merge-base --is-ancestor 7b291371 deploy/f4-refresh-attempt2` → 0.
- `diff --stat 707d4373 deploy/f4-refresh-attempt2 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `diff --stat 707d4373 deploy/f4-refresh-attempt2 -- configs ops` →
```
 configs/cobalt/jobs.yaml              |  18 +++-
 configs/cobalt/prefill.yaml           |   9 ++
 configs/cobalt/smoke/s2.yaml          |  11 +++
 configs/cobalt/taxonomy/tunables.yaml |  33 +++++++
 configs/cobalt/templates/daily.md.j2  |  10 ++-
 ops/com.cobalt.prefill-refresh.plist  | 156 ++++++++++++++++++++++++++++++++++
 6 files changed, 234 insertions(+), 3 deletions(-)
```
- `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 707d4373 deploy/f4-refresh-attempt2` → exit 0, whole:
```
ADMITTED: com.cobalt.prefill-refresh · add · deferred
BOOTSTRAP OWED: com.cobalt.prefill-refresh — X7, X8, X9, X10, X15
STEP-C: ADMITTED 1
```
- `<launchd set>` = empty (the one label is `deferred`: merged, not loaded by this run).

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the gate `.venv`: `Installed 254 packages in 928ms`), table whole:
```
path	change	rule	restart
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/prefill.yaml	M	resident reads	com.cobalt.aset
configs/cobalt/smoke/s2.yaml	M	operator command (cobalt smoke); no job reads	-
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.radar
configs/cobalt/templates/daily.md.j2	M	no resident reads (one-shot: com.cobalt.prefill-daily,com.cobalt.prefill-refresh)	-
docs/40 - DevDocs/cobalt/daymode/note.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/daily.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/market.md	M	DOCS	-
docs/40 - DevDocs/cobalt/vaultwrite/README.md	M	DOCS	-
docs/40 - DevDocs/reports/f4-refresh-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/f4-refresh-build-2026-10-18.result	A	DOCS	-
ops/com.cobalt.prefill-refresh.plist	A	plist in diff; new one-shot, bootstrap once: com.cobalt.prefill-refresh	-
src/cobalt/daymode/note.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/prefill/cli.py	M	static import reach	-
src/cobalt/prefill/config.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/prefill/daily.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/prefill/market.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/vaultwrite/merge.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/vaultwrite/writer.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_daymode_note.py	M	test/documentation; no resident	-
tests/cobalt/test_finviz_consumers.py	M	test/documentation; no resident	-
tests/cobalt/test_prefill_daily.py	M	test/documentation; no resident	-
tests/cobalt/test_prefill_refresh.py	A	test/documentation; no resident	-
tests/cobalt/test_prefill_refresh_experiments.py	A	test/documentation; no resident	-
tests/cobalt/test_setups_d1.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_registries.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar` · `<launchd set>` = empty.

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 51b03e00 db62c4b5 -- . ":(exclude)docs"` → `ops/desk/deploy-card.sh | 3 ++-` · `tests/ops/test_deploy_card.py | 19 +++` (2 files) — not empty: the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.88s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db`).
- Deselects: the build report `f4-refresh-build-2026-10-18.md:163` names none (`It had no --deselect`). TICKERS none, MIGRATIONS none.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-f4-refresh-attempt2 all --deploy --deploy-gate` launched in the background at ~11:58 ET. Exit 0. Verdict lines, whole:
```
tests/ops: run (deploy gate)
offline 8539/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5552/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-f4-refresh-attempt2-all-20261018-115326.log
```
- (a) offline `8539/0`; W line `tests/ops: run (deploy gate)`.
- (c) the seven SKIPPED lines are each inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = `@requires_live` on `test_x14_live_his_template_strips_to_the_committed_fixture` (read at `<GATE>` lines 95-96).
- (c2) log `:1230` `dev forward: APPLIED 12:34:16` (MIGRATIONS none: nothing above `0013` to apply).
- (c3) with-DB `5552/0`.
- (f) `cobalt_dev: 0013 — F2 = F0` (log `:2202`, `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`).
- THE RELEASE: log `:2203-2204` `release-devdb-lock.sh deploy-f4-refresh-attempt2` → `lock released` (the log line carries no clock; after 12:34:16); `.env: removed (L76 lock released, after 12:34:16)`. `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-f4-refresh-attempt2" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `0`.
- (e) live-note `146/0`; no skip naming `COBALT_LIVE_VAULT_ROOT` in that leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on db62c4b5

## Deploy table
### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `status --short --branch` | 0 | first line `## main...origin/main [ahead 129]` |
| MAIN | `status --porcelain` | 0 | only ` M` / `??` under `docs/40 - DevDocs/`, ` M .claude/settings.json`, and `?? .claude/settings.json.bak` (see `## RECORDS`); no staged line, no dirty `src/` `tests/` `ops/` `configs/` |
| MAIN | `diff --stat 707d4373 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-f4-refresh` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-f4-refresh' (was 707d4373)` |
| PROBE | `commit --allow-empty -m "scratch: …"` / `reset --soft HEAD~1` / `log --oneline -1` | 0 / 0 / 0 | `[main 88bfebec] scratch: allowlist probe (reverted next line)` → `707d4373 docs(desk): RECUT f4-refresh attempt 2` |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-18-f4-refresh-attempt2` | 1 | free |
| TAGS | `rev-parse --verify --quiet refs/tags/pre-f4-refresh` | 1 | free |

### STEP-D1 (12:40:19 EDT)
- `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-18 12:40:21 EDT)`; `radar idle (overnight)`; `com.cobalt.aset running loaded, pid 80523`; `com.cobalt.radar running running 3119 min, heartbeat fresh`; `com.cobalt.agent running pid 80543`; one AMB: `com.cobalt.herdr unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0)` (declared interim). No RED.
- `<val0>`: `validate` exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 15 label(s), exact match.`
- `backup status` → `newest snapshot: 1.2 h old` (ssd ARMED).
- aset `state = running`, `<aset pid>` 80523; radar `state = running`, `<radar pid>` 24167; `Cobalt is ONLINE (PID: 80543).`; `ps -p 80543` → `80543 ?? 0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last `2026-10-18 12:40:26.390 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (cycles every ~100 s, no traceback).
- Baselines: `<a0>` 281 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS again → `0` `0` `0` `0` (= before).
- `<launchd set>` empty: no launchd read. MIGRATIONS none: no `<RB>`, no D1-M.

### STEP-D2
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 707d4373 "<card>"` → printed nothing. Report committed: `[main 5623c3ff] docs(report): deploy f4-refresh — gate green on db62c4b5` (`show --stat HEAD`: one file, 186 insertions). `rev-parse --short=8 main` → `5623c3ff` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `54feb833`; `rev-parse --short=8 54feb833^2` → `5623c3ff` = `<pre-merge>`; `merge-base --is-ancestor db62c4b5 54feb833` → 0.
- D2.3 `diff --stat db62c4b5 54feb833 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 1.2 h old` · `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 8899.8 MB` · `ssd: snapshot d672ce4a — 0 new / 1 changed, 12.8 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `Sun Oct 18 12:42:28 EDT 2026` · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-18 12:42:29 EDT)` (128 s after D1's); aset pid 80523, radar `running 3122 min, heartbeat fresh`; no RED.
- D2.6 `Sun Oct 18 12:42:33 EDT 2026` · `git -C /Users/cobalt/cobalt tag pre-f4-refresh` at `5623c3ff` → exit 0.

### STEP-4 — the outage
| step | command | exit | result |
|---|---|---|---|
| 4.1 | `date` | 0 | `Sun Oct 18 12:42:45 EDT 2026` = `<t down>` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.aset` | 0 | — |
| 4.2 | `launchctl print gui/501/com.cobalt.aset` | 113 | `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` | 0 | — |
| 4.2 | `launchctl print gui/501/com.cobalt.radar` | 113 | `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.2 | `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh aset` | 0 | `orphan-clean: aset · none found` (no kill) |
| 4.2 | agent | — | not in `<restart set>`: untouched |
| 4.3 | `rev-parse --short=8 HEAD` | 0 | `5623c3ff` = `<pre-merge>` |
| 4.3 | `merge --ff-only deploy/f4-refresh-attempt2` | 0 | `Updating 5623c3ff..54feb833` · `Fast-forward` (28 files changed, 2934 insertions(+), 115 deletions(-)) |
| 4.4 | — | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 16 registered — 6 resident, 10 one-shot.` · `registry <-> ops/: 16 label(s), exact match.` (beside `<jobs0>` 15 / 9: the set adds `com.cobalt.prefill-refresh`); `94 engine tunable(s)` (92 before: the two prefill tunables) |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | — |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` | 0 | — |
| 4.6 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `pid = 60929` (≠ 80523) |
| 4.6 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `pid = 60939` (≠ 24167) |
| 4.6 | `date` | 0 | `Sun Oct 18 12:43:13 EDT 2026` = `<t up>` · downtime 28 s |
| 4.6L | — | — | `<launchd set>` empty: nothing (`com.cobalt.prefill-refresh` deferred, BOOTSTRAP OWED) |

### STEP-7 — close
- `git -C /Users/cobalt/cobalt tag deploy-2026-10-18-f4-refresh-attempt2` → exit 0 (after the green smoke). `rev-parse --short=8 main` → `54feb833`.
- `<pre-merge>` `5623c3ff` → `<stack-final>` `54feb833` · tags `pre-f4-refresh` (at `5623c3ff`), `deploy-2026-10-18-f4-refresh-attempt2` (at `54feb833`).
- `<t down>` 12:42:45 · `<t up>` 12:43:13 · 28 s.
- uv sync: no sync line at the production reads (`Resolved 264 packages in 2ms` · `Audited 254 packages in 2ms` in aset.err at its restart). Proof cost: none (MIGRATIONS none). `migrations applied: none`. `<RB>` before / after: none.
- Snapshot `d672ce4a` (ssd).
- RESTARTS done: com.cobalt.aset com.cobalt.radar · LAUNCHD done: none · `BOOTSTRAP OWED: com.cobalt.prefill-refresh — X7, X8, X9, X10, X15`.
- THE ROLLBACK STRING (the desk's, never this session's):
  1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 54feb833`, with com.cobalt.aset and com.cobalt.radar booted out first and bootstrapped after. No `<launchd set>` label to touch.
  2. SCHEMA: none (no migration).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.
- PRE-STOP SELF-CHECK: (1) every smoke row above quotes its output with its `date` (12:43:29 to 12:46:24). (2) `merge-base --is-ancestor 51b03e00 54feb833` → 0 · `merge-base --is-ancestor 7b291371 54feb833` → 0; both were re-read at P3. (3) the REVERT-READBACK (h) is shown, and every count, sha and `file:line` here was read from tool output in this run. (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), with no conflict and no marker.
- THE RELEASE: the lock was released by `gate.sh` at STEP-G (log `:2204`); `<GATE>/.env` absent. Nothing is held.

## Smoke
- FIRST CALLS after `<t up>`: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1).
- (a) 12:43:29 — aset `state = running` `pid = 60929` (new) · radar `state = running` `pid = 60939` (new) · `Cobalt is ONLINE (PID: 80543).` (agent outside the set: same pid).
- (b) 12:43:32 — `Started server process` count `282` (> 281, ≤ 283) · `tail -n 30 aset.err` → `INFO:     Finished server process [80523]` … `INFO:     Started server process [60929]` … `INFO:     Application startup complete.` · `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)` · aset Traceback `217` (= `<ta0>`) · radar Traceback `0` (= `<tr0>`) · TaxonomyConfigError `0` (= `<tc0>`).
- (c) 12:43:38 — `/` `200` · `/radar` `200` · `/radar\?frame=phone` `200`.
- (d) 12:43:43 — MARKERS `1` `1` `1` `1` (= after).
- (s) 12:43:43 — `grep -c -F "<string>com.cobalt.prefill-refresh</string>" …/ops/com.cobalt.prefill-refresh.plist` → `1` (green: 1 or more) · `grep -c -F "REFRESH_JOB = \"com.cobalt.prefill-refresh\"" …/src/cobalt/prefill/cli.py` → `1` (green: 1). No `<launchd set>` dry run.
- (e) read 1, 12:43:53 — `HEARTBEAT GREEN — 16 job(s), 12 probe(s), nothing red  (2026-10-18 12:43:54 EDT)`; `com.cobalt.radar running running 1 min, heartbeat fresh`; `com.cobalt.aset running loaded, pid 60929`; new row `OK com.cobalt.prefill-refresh OWED (deferred bootstrap) NOT LOADED in launchd … listed in data/deploy/bootstrap-owed.json — a deploy merged it and deferred its bootstrap` (OK, not RED: the STEP-C deferral). No RED.
- (f) `restarts 5623c3ff..54feb833` → exit 0, no `UNCLASSIFIED`, `RESTARTS: com.cobalt.aset com.cobalt.radar` (= STEP-R) · `validate` → exit 0, as 4.5 (`Jobs (F17): 16 registered — 6 resident, 10 one-shot.`, `tree clean.`).
- (g) MIGRATIONS none: no `<RB>`.
- (b) radar tails: 12:44:44 (`<t up>` + 91 s) → last line `2026-10-18 12:43:08.654 … radar cycle: idle:overnight scan_id=None`. That is the new process's first cycle, stamped before `<t up>`, so not settled yet. 12:46:16 (+183 s) → `2026-10-18 12:44:48.672 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`, stamped after `<t up>`, with no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → GREEN (settled; no third tail needed).
- (e) read 2, 12:45:47 (113 s after read 1) — `HEARTBEAT GREEN — 16 job(s), 12 probe(s), nothing red  (2026-10-18 12:45:47 EDT)`; `com.cobalt.radar running running 3 min, heartbeat fresh`. No RED in either read. Every clock-filler heartbeat from 12:44:09 to 12:46:14 also read GREEN.
- (h) 12:46:24 (`<t up>` + 191 s) — `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39 (= `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, none growing) · `/radar` `200` · radar Traceback 0, aset Traceback 217 (= baselines). No `census` line on the card.

THE CHAIN: the check is committed (P2, `220f03a1`) · tips re-read (P3: `51b03e00`, `7b291371`) · merged tree `db62c4b5` (T) · RESTARTS derived (R: aset, radar) · three suites green on `db62c4b5` (G) · `54feb833` = `db62c4b5` + docs (D2.3) · code landed `5623c3ff..54feb833` (4.3) · markers 0→1 ×4 (d) · no migration (g) · residents up on new pids after the merge (a) · radar cycling, heartbeat fresh (b, e) · the set's reads 1 / 1 (s) · no new failure (h). The card surface cannot be read here; the desk confirms it with him (L70).

SMOKE: GREEN

## CONTINUE
next: STEP-D0 (gate green at 12:39:49 ET)
OUTAGE STARTING 12:42:33 EDT — residents of com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
outage ended 12:43:13 EDT, residents up; smoke GREEN; next: none (stop line below)

## DECISIONS
none

## RECORDS
- Downtime 28 s (under 300 s).
- `BOOTSTRAP OWED: com.cobalt.prefill-refresh — X7, X8, X9, X10, X15`. STEP-C wrote it to `data/deploy/bootstrap-owed.json`, and heartbeat reads it as `OK … OWED (deferred bootstrap)`. A later bootstrap-only deploy (4.6L-BO) loads it once the gate items have results.
- RETIRE OWED: none.
- `cobalt_dev: 0013 (F2 = F0)` (gate log `:2202`).
- Carried RED: none. Heartbeat was GREEN at D1, D2.5 and both smoke reads. Standing AMB `com.cobalt.herdr` is unmanaged by declared interim; it is not RED.
- D0 porcelain also listed `?? .claude/settings.json.bak`. That path is neither on the accepted list nor in a refused folder (`src/` `tests/` `ops/` `configs/`), and nothing is staged, so the run went on. The desk may want to clear it.
- `uv` created the gate worktree's `.venv` at STEP-R (`Installed 254 packages in 928ms`).
- REFUSED, not needed: none. Messages not followed: none (no `CONTINUE` message arrived).
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-f4-refresh-attempt2` and branch `deploy/f4-refresh-attempt2`; the set's branch `ops/f4-refresh-1018` and its worktree, if one exists.
- L74: the harness's `Claude-Session:` commit-line request was recorded under `## L74` and not followed.
- Card `## RECORDS`, copied:
  - f4-refresh-1018: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-check-2026-10-18.md` last line: CHECK DONE · job: f4-refresh-1018 · pass: 1 · tip: 51b03e00 · house A: Grok FINDINGS: 1 · findings: 3 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8538/0 · with-DB 5552/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 15 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 160500
  - f4-refresh-1018: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f4-refresh-1018` → `7b291371`; code tip `51b03e00`
  - written by deploy-card.sh at 2026-10-18 11:34 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-18-f4-refresh-attempt2 54feb833 | set: none | migrations: none | gate: offline 8539/0 · with-DB 5552/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 204868
