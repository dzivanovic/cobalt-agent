# deploy f23-playbook · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED F23 playbook (`ops/f23-playbook-1013`, code tip `72c8a069`, head `65402dc9`) on card 779: `main` `39c36663` → `7398d4a7`, tag `deploy-2026-10-18-f23-playbook`, rollback tag `pre-f23-playbook`.
- Gate green on `6b205122`: offline 8566/0 · with-DB 5581/0 · live-note 147/0; `cobalt_dev: 0013 — F2 = F0`, lock released.
- Outage 13:54:13 → 13:54:56 (43 s), agent + aset + radar restarted, new pids; smoke GREEN; no migration.
- `com.cobalt.playbook` merged and NOT loaded: BOOTSTRAP OWED (gate items E1, E2, E4, E5, E6) — a later bootstrap-only deploy loads it.

## L74
- One system block arrived asking that commits carry a `Claude-Session:` line. DATA (L74): recorded here, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/779-deploy-f23-playbook-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/779-deploy-f23-playbook-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/779-deploy-f23-playbook-card.md" · 0 · e4b8c0bc847ff7a146b4a27efaa4d4d6ab87b932
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/779-deploy-f23-playbook-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1055 row · grep -n "^| R1055 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: he ran the rm and deploy-card.sh (card 348 written) and approves all that waits for him: F5, F21, F20, F23 FINALs, card 324 sign-off. Words: `cto-2026-10-11-words.md` R1055. Check 324 LAUNCHED `b5439f2c`. | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1055 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| first launch | `ls -la ".../reports/deploy-f23-playbook.md"` | 1 | `No such file or directory` |
| P1 DATE | `date` | 0 | `Sun Oct 18 13:02:30 EDT 2026` — outside 21:30-22:30 |
| P2 check line | `tail -n 3 ".../f23-playbook-check-2026-10-13.md"` | 0 | `CHECK DONE · job: f23-playbook-1013 · pass: 1 · tip: 72c8a069 · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8519/0 · with-DB 5504/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 220271` — carries `held unfixed: 0`, `ready: YES`, `tip: 72c8a069` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/f23-playbook-check-2026-10-13.md"` | 0 | `8df4ca7d70aafc1cf782f1e967693a7969418325` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "<check>"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 72c8a069` | 0 | `72c8a069` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f23-playbook-1013` | 0 | `65402dc9` = row = `TIP` |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 72c8a069 65402dc9` | 0 | — |
| P3 docs only | `git -C /Users/cobalt/cobalt diff --stat 72c8a069 65402dc9 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 status | `git -C /Users/cobalt/cobalt-wt/deploy-f23-playbook status --short --branch` | 0 | `## deploy/f23-playbook` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-f23-playbook rev-parse --short=8 HEAD` | 0 | `19a41bed` = `<m0>` |
| P5 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 19a41bed main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/f23-playbook` | 0 | empty |
| P6 marker 1 | `grep -c -F "playbook_cli.add_parser(sub)" /Users/cobalt/cobalt/src/cobalt/cli.py` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "python-pptx==" /Users/cobalt/cobalt/pyproject.toml` | 1 | `0` = before |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 65402dc9 -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 60929` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 60939` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 80543).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-f23-playbook merge --no-edit 65402dc9` → `Auto-merging configs/cobalt/jobs.yaml` · `Merge made by the 'ort' strategy.` · `21 files changed, 1744 insertions(+), 5 deletions(-)`
- `rev-parse --short=8 HEAD` → `6b205122` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 19a41bed..deploy/f23-playbook` → `6b205122 Merge commit '65402dc9' into deploy/f23-playbook` (one line, one head)
- `merge-base --is-ancestor 72c8a069 deploy/f23-playbook` → exit 0 · `merge-base --is-ancestor 65402dc9 deploy/f23-playbook` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 19a41bed deploy/f23-playbook -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none holds)
- The set changes `DEPLOY-HUB.md` (one line: STEP-G (c)'s allowed skips add `test_live_vault_renders_six_decks` in `tests/cobalt/test_playbook_live.py`, reason `COBALT_LIVE_VAULT_ROOT not set`) and `ops/desk/gate-lists.md` (PASS 1 deselect / PASS 2 add `tests/cobalt/test_playbook_db.py`, LIVE-NOTE adds `tests/cobalt/test_playbook_live.py`, the same allowed skip). Not `gate.sh`. Per L68 the gate below is judged on the merged hub text: the merged allowed-skip set applies.

### STEP-C
- `git -C /Users/cobalt/cobalt diff --stat 19a41bed deploy/f23-playbook -- configs ops` →
```
 configs/cobalt/jobs.yaml      | 21 ++++++++++++++++++
 configs/cobalt/playbook.yaml  | 16 ++++++++++++++
 ops/com.cobalt.playbook.plist | 51 +++++++++++++++++++++++++++++++++++++++++++
 ops/desk/gate-lists.md        |  8 +++----
 4 files changed, 92 insertions(+), 4 deletions(-)
```
- `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 19a41bed deploy/f23-playbook` → exit 0:
```
ADMITTED: com.cobalt.playbook · add · deferred
BOOTSTRAP OWED: com.cobalt.playbook — E1, E2, E4, E5, E6
STEP-C: ADMITTED 1
```
- `<launchd set>` = empty (the one label is `deferred`: merged, not loaded by this run).

## RESTARTS
- `cd /Users/cobalt/cobalt-wt/deploy-f23-playbook` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the gate venv: `Installed 256 packages in 848ms`):
```
path	change	rule	restart
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/playbook.yaml	A	no resident reads (one-shot: com.cobalt.playbook)	-
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/playbook/README.md	A	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/f23-playbook-build-2026-10-13.md	A	DOCS	-
docs/40 - DevDocs/reports/f23-playbook-build-2026-10-13.result	A	DOCS	-
ops/com.cobalt.playbook.plist	A	plist in diff; new one-shot, bootstrap once: com.cobalt.playbook	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
pyproject.toml	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/playbook/__init__.py	A	static import reach	com.cobalt.radar
src/cobalt/playbook/cli.py	A	static import reach	com.cobalt.radar
src/cobalt/playbook/config.py	A	static import reach	com.cobalt.radar
src/cobalt/playbook/data.py	A	static import reach	com.cobalt.radar
src/cobalt/playbook/deck.py	A	static import reach	com.cobalt.radar
tests/cobalt/test_playbook_db.py	A	test/documentation; no resident	-
tests/cobalt/test_playbook_live.py	A	test/documentation; no resident	-
tests/cobalt/test_playbook_offline.py	A	test/documentation; no resident	-
tests/cobalt/test_playbook_registry.py	A	test/documentation; no resident	-
uv.lock	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar
```
- No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.agent com.cobalt.aset com.cobalt.radar` · `<launchd set>` = empty.

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 72c8a069 6b205122 -- . ":(exclude)docs"` → 22 files (main's prefill-refresh work since the check) → the clause does not hold; the gate runs whole.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_archiver_migrations.py … tests/cobalt/test_jobs_restarts.py` (the hub's 17 files) → `263 passed, 163 skipped in 17.82s` — 0 failed (every skip `Postgres env settings not available` / `requires_db`).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-f23-playbook all --deploy --deploy-gate` (no `--deselect`: the build's PASS 1 deselect and PASS 2 id are in the merged `gate-lists.md`, build report row P7; TICKERS none; no `--migration`) → exit 0. Verdict lines WHOLE:
```
tests/ops: run (deploy gate)
offline 8566/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-f23-playbook-all-20261018-130502.log
```
- (a) offline `8566/0`; W line `tests/ops: run (deploy gate)`.
- (c) pass 1 skips, each inside the merged allowed set by test and reason: `test_playbook_live.py:31` is `test_live_vault_renders_six_decks` (Grep `:32 def test_live_vault_renders_six_decks`), reason `COBALT_LIVE_VAULT_ROOT not set` — the set's own addition to the hub/`gate-lists.md`; `test_s3_c4_experiments.py:95` is the decorator of `:96 def test_x14_live_his_template_strips_to_the_committed_fixture`; the rest are the hub's named lines.
- (c2) `dev forward: APPLIED 13:45:24` (log `:1235`).
- (c3)/(f) `with-DB 5581/0` · `cobalt_dev: 0013 — F2 = F0` (log `:2235`, `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = LEVEL 0013).
- RELEASE: log `:2236` `release-devdb-lock.sh deploy-f23-playbook` → `:2237 lock released` · `.env: removed` · `ls -la <GATE>/.env` → No such file · `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.
- (e) live-note `147 passed, 1 skipped` — the one skip `test_replay_line.py:266 … COBALT_TEST_LIVE_DRC`, inside the set; no skip naming `COBALT_LIVE_VAULT_ROOT`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 6b205122

## Deploy table
### STEP-D0 (`date` → `Sun Oct 18 13:51:16 EDT 2026`)
| check | command | exit | result |
|---|---|---|---|
| main branch | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 138]` |
| main dirty | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M .claude/settings.json`; ` M`/`??` under `docs/40 - DevDocs/` only; plus `?? .claude/settings.json.bak` (see DECISIONS 1); no dirty `src/`, `tests/`, `ops/`, `configs/` path |
| main moved | `git -C /Users/cobalt/cobalt diff --stat 19a41bed main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe tag | `tag scratch-allow-probe-f23-playbook` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-f23-playbook' (was 19a41bed)` |
| probe commit | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 5735c279] …` · — · `19a41bed docs(desk): F20 cos check report, CHECK DONE ready NO (2 held unfixed)` |
| TAG free | `rev-parse --verify --quiet refs/tags/deploy-2026-10-18-f23-playbook` | 1 | — |
| pre-tag free | `rev-parse --verify --quiet refs/tags/pre-f23-playbook` | 1 | — |

### STEP-D1 (`date` → `Sun Oct 18 13:51:41 EDT 2026`)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT GREEN — 16 job(s), 12 probe(s), nothing red  (2026-10-18 13:51:42 EDT)`; `OK   radar                    idle (overnight)`; `OK   com.cobalt.aset running loaded, pid 60929`; `OK   com.cobalt.agent running pid 80543 alive`; `OK   com.cobalt.radar running running 69 min, heartbeat fresh`; `AMB  com.cobalt.herdr unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) … declared interim`; `OK   com.cobalt.prefill-refresh   OWED (deferred bootstrap) …`. No RED.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.` · `<jobs0>` `Jobs (F17): 16 registered — 6 resident, 10 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 16 label(s), exact match.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 1.2 h old` (ssd ARMED)
- `launchctl print gui/501/com.cobalt.aset` → `state = running` · `<aset pid>` `60929` · `launchctl print gui/501/com.cobalt.radar` → `state = running` · `<radar pid>` `60939` · `cobalt.sh status` → `Cobalt is ONLINE (PID: 80543).` · `ps -p 80543` → `80543 ??         0:00.03 uv run src/cobalt_agent/main.py`
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → last `2026-10-18 13:51:29.364 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (eight `idle:overnight` lines, 100 s apart, no traceback)
- LOG BASELINES: `<a0>` 282 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39
- `curl … /radar` → `200` · MARKERS: `playbook_cli.add_parser(sub)` → `0` (before) · `python-pptx==` → `0` (before)
- THE LAUNCHD SET: empty — nothing read. MIGRATIONS: none — no `<RB>`, no census, no D1-M.

### STEP-D2
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 19a41bed "<card>"` → nothing · `add` + `commit … -- "<REPORT>"` → `[main 39c36663] docs(report): deploy f23-playbook — gate green on 6b205122` · `1 file changed, 173 insertions(+)` · `show --stat HEAD` → the one file · `<pre-merge>` = `39c36663`
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only)
- D2.2 `<stack-final>` = `7398d4a7` · `rev-parse --short=8 7398d4a7^2` → `39c36663` = `<pre-merge>` · `merge-base --is-ancestor 6b205122 7398d4a7` → exit 0
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 6b205122 7398d4a7 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs only)
- D2.4 `backup status` → `newest snapshot: 1.2 h old` · `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain dumped, 8899.8 MB` · `ssd: snapshot 2b843746 — 0 new / 1 changed, 12.8 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`
- D2.5 `date` → `Sun Oct 18 13:53:52 EDT 2026` · `heartbeat show` → `HEARTBEAT GREEN — 16 job(s), 12 probe(s), nothing red  (2026-10-18 13:53:53 EDT)` (131 s after D1's) · aset pid 60929, agent pid 80543, radar `running 71 min, heartbeat fresh` · no RED
- D2.6 `date` → `Sun Oct 18 13:53:58 EDT 2026` · `git -C /Users/cobalt/cobalt tag pre-f23-playbook` → `rev-parse --short=8 pre-f23-playbook` → `39c36663`

### STEP-4 (the outage)
| step | command | result |
|---|---|---|
| 4.1 | `date` | `Sun Oct 18 13:54:13 EDT 2026` = `<t down>` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.aset` · `print` | exit 0 · exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` · `print` | exit 0 · exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.2 orphan | `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh aset` | `orphan-clean: aset · none found` — clean, no kill |
| 4.2 agent | `/Users/cobalt/cobalt/cobalt.sh stop` · `ps -p 80543` | `Cobalt stopped safely.` · header only |
| 4.3 | `rev-parse --short=8 HEAD` · `merge --ff-only deploy/f23-playbook` | `39c36663` = `<pre-merge>` · `Updating 39c36663..7398d4a7` `Fast-forward` (21 files, 1744+/5−) |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0; uv sync: `Built cobalt-agent @ file:///Users/cobalt/cobalt` · `Uninstalled 1 package in 1ms` · `Installed 3 packages in 3ms`; `Jobs (F17): 17 registered — 6 resident, 11 one-shot.` (was 16 / 10: + `com.cobalt.playbook`) · `registry <-> ops/: 17 label(s), exact match.` · `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.6 | `bootstrap … com.cobalt.aset.plist` · `bootstrap … com.cobalt.radar.plist` · `kickstart gui/501/com.cobalt.agent` | exit 0 · exit 0 · exit 0 |
| 4.6 | `launchctl print` aset · radar · `cobalt.sh status` | `state = running` pid `89330` (≠ 60929) · `state = running` pid `89340` (≠ 60939) · `Cobalt is ONLINE (PID: 89351).` (≠ 80543) |
| 4.6 | `date` | `Sun Oct 18 13:54:56 EDT 2026` = `<t up>` · downtime 43 s |
| 4.6L | — | `<launchd set>` empty: nothing (`com.cobalt.playbook` deferred) |

### STEP-7 close
| item | value |
|---|---|
| main | `<pre-merge>` `39c36663` → `<stack-final>` `7398d4a7` |
| tags | `pre-f23-playbook` → `39c36663` · `deploy-2026-10-18-f23-playbook` → `7398d4a7` (`rev-parse --short=8` read back) |
| outage | `<t down>` 13:54:13 · `<t up>` 13:54:56 · 43 s |
| uv sync | `Built cobalt-agent @ file:///Users/cobalt/cobalt` · `Uninstalled 1 package in 1ms` · `Installed 3 packages in 3ms` (4.5, first production `uv run` on the new tree) |
| proof cost | none (no migration) |
| migrations applied | none · `<RB>` before / after: none |
| snapshot | `2b843746` (ssd), `cobalt_brain` 8899.8 MB |
| RESTARTS done | `com.cobalt.agent com.cobalt.aset com.cobalt.radar` |
| LAUNCHD done | none |
| BOOTSTRAP OWED | `BOOTSTRAP OWED: com.cobalt.playbook — E1, E2, E4, E5, E6` |

THE ROLLBACK STRING (the desk's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 7398d4a7` — one revert of the main-into-gate merge; agent, aset and radar down first, up after. No `<launchd set>` label was loaded by this run (`com.cobalt.playbook` stays out).
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` — git titles it `Reapply "Merge branch 'main' into deploy/f23-playbook"`.

## Smoke
- FIRST CALLS after `<t up>` 13:54:56: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1)
- (a) [13:55:13] `cobalt.sh status` → `Cobalt is ONLINE (PID: 89351).` (new; was 80543) · [13:55:43] `launchctl print` aset → `state = running` `pid = 89330` (new) · radar → `state = running` `pid = 89340` (new)
- (b) [13:55:13] `grep -c "Started server process" aset.err` → `283` (`<a0>` 282 +1) · `tail -n 30 aset.err` → `INFO:     Started server process [89330]` … `INFO:     Application startup complete.` · `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)` · Traceback aset `217` (= `<ta0>`) · Traceback radar `0` (= `<tr0>`) · TaxonomyConfigError `0` (= `<tc0>`)
- (b) radar tail 1 [13:56:28, `<t up>`+92 s] `tail -n 12 radar.err` → last `2026-10-18 13:54:52.425 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (stamped 4 s before `<t up>`: not yet settling) preceded by vault-unlock / finviz token lines; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback
- (b) radar tail 2 [13:57:56, `<t up>`+180 s] `tail -n 12 radar.err` → last `2026-10-18 13:56:32.451 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` — a cycle line stamped after `<t up>`, no S5 / lifecycle failure, no traceback → (b) settled GREEN (third tail not needed)
- (c) [13:55:13+] `/` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200`
- (d) [13:55:13+] `playbook_cli.add_parser(sub)` → `1` (after) · `python-pptx==` → `1` (after)
- (e) #1 [13:55:24] `heartbeat show` → `HEARTBEAT GREEN — 17 job(s), 12 probe(s), nothing red  (2026-10-18 13:55:26 EDT)` · `com.cobalt.radar running running 1 min, heartbeat fresh` · new row `OK   com.cobalt.playbook          OWED (deferred bootstrap) NOT LOADED in launchd … listed in data/deploy/bootstrap-owed.json — a deploy merged it and deferred its bootstrap` (OWED, not red — STEP-C's deferred label) · #2 [13:57:18] `heartbeat show` → `HEARTBEAT GREEN — 17 job(s), 12 probe(s), nothing red  (2026-10-18 13:57:21 EDT)` (115 s after #1) · aset pid 89330, agent pid 89351, `com.cobalt.radar running running 2 min, heartbeat fresh` · no RED; no RED in `<hb0>` either
- (f) [13:55:24+] `validate` → as 4.5 (exit 0, `Jobs (F17): 17 registered`, tree clean) · `COBALT_ENV=production uv run cobalt jobs restarts 39c36663..7398d4a7` → exit 0, no `UNCLASSIFIED`, `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar` = STEP-R
- (g) no migration
- (s) playbook tests: quoted from the gate (no test runs in production) — the gate's offline legs over `tests/cobalt` (which hold `test_playbook_offline.py`, `test_playbook_registry.py`) → `offline 8566/0` (log `:925` `4645 passed, 841 skipped, 4 xfailed …`, `:997` `3921 passed, 1 xfailed …`) — `0 failed` · playbook mount: `uv run cobalt playbook render --help` → exit 0, `usage: cobalt playbook render [-h] [--date DATE] [--out OUT] [--dry-run]` — names `--date`, `--out`, `--dry-run`. No `<launchd set>` dry run.
- (h) REVERT-READBACK [13:57:56+, `<t up>`+180 s, after (b) settled]: `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39 — each = `<…_up>` (no growth) · `/radar` → `200` · `cobalt.sh status` → `Cobalt is ONLINE (PID: 89351).` · no census reads (no migration).
- THE CHAIN: every check committed (P2 `8df4ca7d`) → the tips re-read (P3 `72c8a069` / `65402dc9`) → the merged tree `6b205122` (T) → RESTARTS derived `com.cobalt.agent com.cobalt.aset com.cobalt.radar` (R) → three suites green on `6b205122` (G) → `7398d4a7` = `6b205122` + docs (D2.3) → the landed code `Fast-forward 39c36663..7398d4a7` (4.3) → markers `1` / `1` (d) → no migration (g) → residents up on new pids after the merge (a) → radar cycling `13:56:32`, heartbeat fresh (b, e) → the set's reads green (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).
- SMOKE: GREEN

## CONTINUE
- STEP-D0 done (gate green; gate log `dev forward: APPLIED 13:45:24`, finished before 13:51:16).
- OUTAGE STARTING 13:53:58 — residents of com.cobalt.agent com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- 4.6 ended 13:54:56: residents up on new pids (aset 89330, radar 89340, agent 89351). Smoke GREEN 13:57:56+. STEP-7 closed; nothing next for this session.

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` on `main` is untracked, outside `docs/40 - DevDocs/`, and not in D0's accepted list; it is also not a `src/`/`tests/`/`ops/`/`configs/` path nor staged, so D0's refusal rules do not name it, and the set ships no such path (the `--ff-only` merge cannot touch it). Safe default taken: not a refusal; went on. [13:51:16]

No `DECISION 0`. Nothing `FOR DEJAN`.

## RECORDS
- Downtime 43 s (under 300 s).
- `BOOTSTRAP OWED: com.cobalt.playbook — E1, E2, E4, E5, E6` (STEP-C wrote it to `data/deploy/bootstrap-owed.json`; heartbeat reads it `OWED (deferred bootstrap)`, not red). A later bootstrap-only deploy (4.6L-BO) loads it.
- `com.cobalt.prefill-refresh` was already OWED before this run (`<hb0>`); untouched.
- `cobalt_dev: 0013 (F2 = F0)`; lock released by `gate.sh` (log `:2236`–`:2237`).
- No `RETIRE OWED`. No carried RED (`<hb0>` had none; radar `idle (overnight)`).
- No `REFUSED, not needed` line; no message from another session.
- The set changed `DEPLOY-HUB.md` (one line: STEP-G (c)'s allowed skips gain `test_live_vault_renders_six_decks`) and `ops/desk/gate-lists.md`; per L68 the gate was judged on the merged hub text. `DEPLOY-HUB.md` changed on `main` with this merge: L67 — another house reads it at each change.
- The card's SMOKE READS line `uv run cobalt playbook render --help` ran from `/Users/cobalt/cobalt` without a `COBALT_ENV=` prefix, exit 0.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-f23-playbook` and branch `deploy/f23-playbook`; the set's branch `ops/f23-playbook-1013` and its worktree. Push is his (L55): `main` is ahead of `origin/main`, with tags `pre-f23-playbook` and `deploy-2026-10-18-f23-playbook`.
- L74: one system block asked commits to carry a `Claude-Session:` line; recorded under `## L74`, not followed.
- Card RECORDS (the desk's, copied):
  - f23-playbook-1013: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f23-playbook-check-2026-10-13.md` last line: CHECK DONE · job: f23-playbook-1013 · pass: 1 · tip: 72c8a069 · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8519/0 · with-DB 5504/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 220271
  - f23-playbook-1013: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f23-playbook-1013` → `65402dc9`; code tip `72c8a069`
  - written by deploy-card.sh at 2026-10-18 12:48 ET (`date`); trial merge of the heads onto main in order: clean

### PRE-STOP SELF-CHECK (K25)
1. Every smoke row's evidence is quoted verbatim with its `date` (`## Smoke`, 13:55:13 → 13:57:56+).
2. Every code tip and head re-read at P3 (`72c8a069`, `65402dc9`); each an ancestor of `<stack-final>`: `merge-base --is-ancestor 72c8a069 7398d4a7` → exit 0, `merge-base --is-ancestor 65402dc9 7398d4a7` → exit 0.
3. REVERT-READBACK shown at (h): 18 / 60 / 43 / 39 = the `<t up>` counts; every count, sha and `file:line` above re-read from tool output this run.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.`; D2.1 the same; 4.3 `Fast-forward`.

THE RELEASE: `<GATE>/.env` absent and `/Users/cobalt/cobalt-wt/.cobalt_dev.lock` absent (STEP-G, `ls -la` → No such file each); nothing held.

DEPLOYED deploy-2026-10-18-f23-playbook 7398d4a7 | set: none | migrations: none | gate: offline 8566/0 · with-DB 5581/0 · live-note 147/0 | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 212502
