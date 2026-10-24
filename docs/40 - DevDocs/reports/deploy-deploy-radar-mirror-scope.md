# deploy-radar-mirror-scope — SET: radar-mirror-scope — MIGRATIONS: none

## §0 Headline
- FAILED at smoke (h): the `radar panel FAILED` count grew 21 → 23 after `<t up>`. ROLLED BACK by one revert, `41bb2402`; the code is proven equal to `e41b9420`; residents UP on the old tree.
- Cause, as read: a CardSettingsError (`radar.cards_enabled: Input should be a valid boolean`) that predates this deploy. Every `/radar` hit logs one line, and the smoke's own curls are those hits. The OLD code did the same at 19:43:10 (D1's curl) and on the reverted tree at 19:49:43 / 19:49:44. The set changes only `src/cobalt/radar/notes.py`, which never reads `cards_enabled`.
- Gate was green on `0d6765aa`: offline 9120/0 · with-DB 5956/0 · live-note 148/0. The landed tree passed (a)–(g) and (s). Downtime: 31 s (deploy) + 26 s (rollback).
- DECISION 0: production DEGRADED on the reverted tree. The count grows on old code too, so the desk decides whether to re-land (ROLLBACK STRING 3) once the settings fault, or the (h) rule, is ruled on.

## L74
- One block, outside any tool result: a system notice asked commit messages to carry a `Claude-Session:` line. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-23/1027-deploy-radar-mirror-scope-card.md"` → exit 0, output WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-23/1027-deploy-radar-mirror-scope-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-23/1027-deploy-radar-mirror-scope-card.md" · 0 · 172351fed149777638c24a4d5c90f124a4ed3bda
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-23/1027-deploy-radar-mirror-scope-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| FIRST LAUNCH | `ls -la "…/reports/deploy-deploy-radar-mirror-scope.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Sat Oct 24 18:51:38 EDT 2026`: outside 21:30-22:30 |
| P2 check last line | `tail -n 3 "…/reports/radar-mirror-scope-check-2026-10-23.md"` | 0 | `CHECK DONE · job: radar-mirror-scope · pass: 1 · tip: 25994142 · … · held unfixed: 0 · open: 1 · … · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 164093`: carries `held unfixed: 0` and `ready: YES`; `tip: 25994142` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/radar-mirror-scope-check-2026-10-23.md"` | 0 | `d9ec36a888c178603fa09663c2d9951d92933371` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "<check>"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 25994142` | 0 | `25994142` |
| P3 branch head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-mirror-scope` | 0 | `25994142` (= card, = TIP) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 25994142 ops/radar-mirror-scope` | 0 | — |
| P3 docs only | `git -C /Users/cobalt/cobalt diff --stat 25994142 ops/radar-mirror-scope -- . ':(exclude)docs'` | 0 | nothing |
| P4 LOCK | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`: no session holds the lock |
| P5 status | `git -C /Users/cobalt/cobalt-wt/deploy-radar-mirror-scope status --short --branch` | 0 | `## deploy/deploy-radar-mirror-scope` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-radar-mirror-scope rev-parse --short=8 HEAD` | 0 | `172351fe` = `<m0>` |
| P5 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 172351fe main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-radar-mirror-scope` | 0 | empty |
| P6 marker 1 | `grep -c -F "MIRROR_SOURCE_PREFIX = " /Users/cobalt/cobalt/src/cobalt/radar/notes.py` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "def test_m2_a_lists_edit_…_byte_identical" /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` | 2 | `grep: /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py: No such file or directory`: the file is absent on main, so production does not carry the marker (zero occurrences); see `## DECISIONS` 1 |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 25994142 -- src/cobalt/db_migrations` | 0 | nothing: no migration, matches `MIGRATIONS: none` |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 53218` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 53248` |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent retired | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1`: `com.cobalt.agent recorded retired` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is OFFLINE.` (as expected when retired) |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-radar-mirror-scope merge --no-edit 25994142` → `Merge made by the 'ort' strategy.` (9 files, 561 insertions, 16 deletions: notes.py, notes.md, the build report and result, and five test files incl. new `tests/cobalt/test_radar_mirror_scope.py`)
- `rev-parse --short=8 HEAD` → `0d6765aa` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 172351fe..deploy/deploy-radar-mirror-scope` → `0d6765aa Merge commit '25994142' into deploy/deploy-radar-mirror-scope` (one line, one head)
- `merge-base --is-ancestor 25994142 deploy/deploy-radar-mirror-scope` → exit 0
- `diff --stat 172351fe deploy/deploy-radar-mirror-scope -- src/cobalt/db_migrations` → nothing (no migration, = `MIGRATIONS: none`)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 172351fe deploy/deploy-radar-mirror-scope -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 172351fe deploy/deploy-radar-mirror-scope` → exit 0, output WHOLE: `STEP-C: ADMITTED 0`. `<launchd set>`: empty · `<deferred set>`: empty.

## RESTARTS
- `cd /Users/cobalt/cobalt-wt/deploy-radar-mirror-scope` · `ls -la <GATE>/.env` → `No such file or directory`
- `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0, table WHOLE (after uv lines `Creating virtual environment at: .venv` · `Installed 257 packages in 897ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/radar/notes.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-build-2026-10-23.md	A	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-build-2026-10-23.result	A	DOCS	-
src/cobalt/radar/notes.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_mirror_scope.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_notes.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
- No `UNCLASSIFIED` row. cos loaded: `launchctl print gui/501/com.cobalt.cos` → exit 0, `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.cos.plist`, `pid = 53231`, so it stays in the set.
- `<restart set>`: **com.cobalt.aset com.cobalt.cos com.cobalt.radar**
- `<deferred set>`: empty · `<launchd set>`: empty
- com.cobalt.agent: recorded retired — not restarted (not derived anyway)

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 25994142 0d6765aa -- . ":(exclude)docs"` → ` configs/cobalt/rules.yaml | 2 +-`. Not empty, so the gate runs whole (`--deploy`).
- Deselects: none. The build report's gate run is `gate.sh radar-mirror-scope all --deploy` with "no `--deselect`"; its `--deselect` lines are gate.sh's own pass-1 command.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `265 passed, 163 skipped in 19.47s` (0 failed; every skip is `Postgres env settings not available` / `requires_db`)
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-radar-mirror-scope all --deploy --deploy-gate` (no `--deselect`, `TICKERS: none`, no `--migration`) → exit 0, verdict lines WHOLE:
```
tests/ops: run (deploy gate)
offline 9120/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5956/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-radar-mirror-scope-all-20261024-185355.log
```
- (a) offline `9120/0`; W line `tests/ops: run (deploy gate)`.
- (b) lock waited 0 min; proof-only at `0013`, nothing CHANGED; `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log:1049).
- (c) pass 1 whole at `0013`. All nine SKIPPED lines fall inside the allowed set by file and reason: cards_picks :388 / :401, checkpoints_live and playbook_live (`COBALT_LIVE_VAULT_ROOT not set`), radar_evaluate :695, replay_line (`COBALT_TEST_LIVE_DRC`), s3_c4_experiments, catalyst :365, predicate :262.
- (c2)/(c3): no migration on the card, so no forward and no pass 2. `with-DB 5956/0`.
- (f) `cobalt_dev: 0013 — F2 = F0` (log:2388 `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`).
- RELEASE: log:2389-2394 `release-devdb-lock.sh deploy-radar-mirror-scope` → `lock released` · `.env: removed` (L76 lock released; the log carries no clock stamp there, and the gate ended before 19:42:19 EDT). `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file (lock dir absent).
- (e) live-note `148/0`; no skip names `COBALT_LIVE_VAULT_ROOT` in the live leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 0d6765aa

## Deploy table
**STEP-D0** (Sat Oct 24 19:42 EDT 2026)
| row | command | result |
|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | `## main...origin/main [ahead 3]` |
| MAIN porcelain | `status --porcelain` | ` M .claude/settings.json`; every other line is ` M` / `??` under `docs/40 - DevDocs/`, except `?? .claude/settings.json.bak` (untracked; neither staged nor under src/tests/ops/configs, so not refused; see RECORDS). No staged line. |
| MAIN moved | `git -C /Users/cobalt/cobalt diff --stat 172351fe main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| PROBE | `tag scratch-allow-probe-deploy-radar-mirror-scope` · `tag -d …` | `Deleted tag 'scratch-allow-probe-deploy-radar-mirror-scope' (was 172351fe)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | `[main 3da032d1] …` → `172351fe docs(desk): deploy card 1027 radar-mirror-scope tip 25994142` (HEAD back) |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-24-radar-mirror-scope` · `…/pre-deploy-radar-mirror-scope` | exit 1 · exit 1 |

**STEP-D1** baseline (`date` → `Sat Oct 24 19:42:52 EDT 2026`)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s)  (2026-10-24 19:42:53 EDT)`. Aset / sheet probes OK (`sheet HTTP http://127.0.0.1:5010/ -> 200`), `radar idle (overnight)` OK, `cos loop stamping (4s ago)` OK, `com.cobalt.aset running loaded, pid 53218`, `com.cobalt.radar running 3863 min, heartbeat fresh`, `com.cobalt.cos running 3863 min, heartbeat fresh`. The two REDs, named and not a stop:
  - `RED  com.cobalt.agent             not loaded NOT LOADED in launchd — …` (agent recorded retired)
  - `RED  com.cobalt.replay            failed    StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings top_n Field required …`
  - OWED (deferred bootstrap), listed OK: prefill-refresh, checkpoint-0715/0745/0815/0845, playbook.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 22.0 h old` (ssd local ARMED)
- `<aset pid>` 53218 · `<radar pid>` 53248 · `<cos pid>` 53231 (each `state = running`). `cobalt.sh status` → `  Cobalt is OFFLINE.` (recorded retired: no `<agent pid>`, no `ps -p`)
- `tail -n 8 radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, last `2026-10-24 19:41:23.068`; no traceback.
- LOG BASELINES: `<a0>` 294 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 20 · `<rpr0>` 60 · `<re0>` 750 · `<lc0>` 39
- `curl … /radar` → `200`. MARKERS: marker 1 `0`; marker 2 `No such file or directory` (as P6, DECISIONS 1).
- THE LAUNCHD SET: empty, nothing read. No migration: no `<RB>`, no D1-M.

**STEP-D2**
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 172351fe "<card>"` → nothing. Report committed `e41b9420 docs(report): deploy deploy-radar-mirror-scope — gate green on 0d6765aa` (`show --stat HEAD`: the one file, 155 insertions). `<pre-merge>` = `e41b9420`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only)
- D2.2 `<stack-final>` = `4f35be8f`; `rev-parse --short=8 4f35be8f^2` → `e41b9420` = `<pre-merge>`; `merge-base --is-ancestor 0d6765aa 4f35be8f` → exit 0
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 0d6765aa 4f35be8f -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs only)
- D2.4 `backup status` before → `newest snapshot: 22.0 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 10246.9 MB` · `ssd: snapshot 4f50ea50 — 0 new / 2 changed, 28.8 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`. Snapshot id **4f50ea50**.
- D2.5 `Sat Oct 24 19:45:03 EDT 2026` heartbeat → `HEARTBEAT RED — 2 job(s)  (2026-10-24 19:45:03 EDT)`, the same two REDs as `<hb0>` (agent, replay); aset / sheet / radar / cos OK. 130 s after D1's read. No new RED.
- D2.6 `date` → `Sat Oct 24 19:45:08 EDT 2026`; `git -C /Users/cobalt/cobalt tag pre-deploy-radar-mirror-scope` at `e41b9420`.

**STEP-4 OUTAGE**
| step | command | result |
|---|---|---|
| 4.1 | `date` | `<t down>` = `Sat Oct 24 19:45:20 EDT 2026` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.aset` · print | no output · exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.cos` · print | no output · exit 113 `Could not find service "com.cobalt.cos" …` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` · print | no output · exit 113 `Could not find service "com.cobalt.radar" …` |
| 4.2 ORPHAN | `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh aset` | `orphan-clean: aset · none found`: clean, no kill. Agent not in the set. |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | `e41b9420` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/deploy-radar-mirror-scope` | `Updating e41b9420..4f35be8f` · `Fast-forward` (9 files, 561+/16-) |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · print | no output · `state = running`, `pid = 49777` (≠ 53218) |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.cos.plist` · print | no output · `state = running`, `pid = 49789` (≠ 53231) |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · print | no output · `state = running`, `pid = 49795` (≠ 53248) |
| 4.6 | `date` | `<t up>` = `Sat Oct 24 19:45:51 EDT 2026`, so downtime is 31 s |
| 4.6L | — | `<launchd set>` empty: nothing |

**STEP-5 ROLLBACK** (entered from smoke (h) RED)
| step | command | result |
|---|---|---|
| (0) | `date` | `Sat Oct 24 19:49:06 EDT 2026` |
| (1) | `launchctl bootout gui/501/com.cobalt.aset` / `.cos` / `.radar`, each with a print | no output; each print exit 113 `Could not find service …` |
| (1) | four counts | `<rp5>` 24 · `<rpr5>` 60 · `<re5>` 750 · `<lc5>` 39 |
| (1L) | — | `<launchd set>` empty |
| (2) | `git -C /Users/cobalt/cobalt log --oneline -1` | `4f35be8f Merge branch 'main' into deploy/deploy-radar-mirror-scope` |
| (2) | `git -C /Users/cobalt/cobalt revert --no-edit -m 2 4f35be8f` | `[main 41bb2402] Revert "Merge branch 'main' into deploy/deploy-radar-mirror-scope"` (9 files, 16+/561-) |
| (2) PROOF | `git -C /Users/cobalt/cobalt diff --stat e41b9420 HEAD -- . ':(exclude)docs'` | nothing: the code equals `<pre-merge>` |
| (2L) | — | none |
| (3) | `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh aset` | `orphan-clean: aset · none found` |
| (3) | `launchctl bootstrap` aset / cos / radar | no output each |
| (3) | `date` | `Sat Oct 24 19:49:32 EDT 2026`, so rollback downtime is 26 s |
| (4a) | prints | aset `state = running` pid 51019 · cos running pid 51030 · radar running pid 51036 (all new) · `cobalt.sh status` → `  Cobalt is OFFLINE.` (recorded retired) |
| (4b) | `grep -c "Started server process" aset.err` · tail | `296` · `Started server process [51019]` … `Uvicorn running on http://127.0.0.1:5010`. Traceback aset 217 / radar 0, TaxonomyConfigError 0 (= baseline). Radar tail last line `2026-10-24 19:49:31.861 … radar cycle: idle:overnight scan_id=None`; a later read is in `## Smoke` |
| (4c) | `Sat Oct 24 19:49:41 EDT 2026` curls `/` · `/radar` · `/radar\?frame=phone` | `200` · `200` · `200` |
| (4e) | `Sat Oct 24 19:49:49 EDT 2026` heartbeat | `HEARTBEAT RED — 2 job(s)`: the same agent and replay REDs as `<hb0>`; aset pid 51019 OK; radar / cos `running 0 min, heartbeat fresh` |
| (4f) | validate · `jobs restarts e41b9420..4f35be8f` | exit 0, `Jobs (F17): 22 registered — 7 resident, 15 one-shot.`, `tree clean.` · `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`, no UNCLASSIFIED |
| (4g) | — | no migration |
| (4e) 2 | `Sat Oct 24 19:51:06 EDT 2026` heartbeat (`19:51:09`, 140 s after read 1) | the same two REDs only; aset pid 51019 OK; `com.cobalt.radar running 2 min, heartbeat fresh`; `com.cobalt.cos running 2 min, heartbeat fresh` |
| (4b) radar | `tail -n 2 radar.err` | `2026-10-24 19:51:11.887 … radar cycle: idle:overnight scan_id=None`, stamped after 19:49:32: radar cycling on the old tree, no traceback |
| (4) READBACK | `grep -c "radar panel FAILED" aset.err` after (4c) | **26**, up from `<rp5>` 24. New lines `2026-10-24 19:49:43.255` and `19:49:44.010`, both `radar panel FAILED: FAILED: radar evaluate: CardSettingsError: invalid card settings: radar.cards_enabled: Input should be a valid boolean`. The count grows on the OLD code too, so this is terminal: DECISION 0 |

| field | value |
|---|---|
| `<pre-merge>` → `<stack-final>` | `e41b9420` → `4f35be8f`; reverted by `41bb2402` |
| tags | `pre-deploy-radar-mirror-scope` at `e41b9420` (set). `deploy-2026-10-24-radar-mirror-scope` NOT set (not green) |
| outage | `<t down>` 19:45:20 / `<t up>` 19:45:51 / 31 s; rollback 19:49:06 / 19:49:32 / 26 s |
| uv sync | none in production (the gate worktree created its own `.venv`: `Installed 257 packages in 897ms`) |
| proof cost | n/a (no migration) |
| migrations applied | none |
| `<RB>` | n/a |
| snapshot | `4f50ea50` (ssd) |
| RESTARTS done | com.cobalt.aset com.cobalt.cos com.cobalt.radar (twice: deploy and rollback) |
| LAUNCHD done | none |
| BOOTSTRAP OWED | none from this set |

THE ROLLBACK STRING (stack-final `4f35be8f`):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 4f35be8f`, already run by STEP-5 as `41bb2402`. Residents of `com.cobalt.aset com.cobalt.cos com.cobalt.radar` were taken down first and brought up after.
2. SCHEMA: none (no migration).
3. RE-LAND (the desk's, on his word): `git -C /Users/cobalt/cobalt revert --no-edit 41bb2402`, which git titles `Reapply "Merge branch 'main' into deploy/deploy-radar-mirror-scope"`, with the same three residents down first and up after.

## Smoke
- FIRST CALLS after `<t up>`: `<rp_up>` **21** · `<rpr_up>` 60 · `<re_up>` 750 · `<lc_up>` 39. `<rp_up>` (21) is one above `<rp0>` (20); that line is `2026-10-24 19:43:10.377 … radar panel FAILED: FAILED: radar evaluate: CardSettingsError: invalid card settings: radar.cards_enabled: Input should be a valid boolean`, written BEFORE the outage by the OLD aset (pid 53218, shut down at 19:45). It came from D1's own `/radar` curl, so the fault predates this set.
- (a) `Sat Oct 24 19:46:11 EDT 2026`: aset `state = running` pid 49777 (new) · cos running pid 49789 (new) · radar running pid 49795 (new) · `cobalt.sh status` → `  Cobalt is OFFLINE.` (recorded retired, so this is GREEN)
- (b) `grep -c "Started server process" aset.err` → `295` (= `<a0>`+1) · `tail -n 30 aset.err` → `INFO:     Started server process [49777]` … `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)` · Traceback aset `217` = `<ta0>` · Traceback radar `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`
- (c) `Sat Oct 24 19:46:23 EDT 2026`: `/` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200`
- (d) `Sat Oct 24 19:46:26 EDT 2026`: marker 1 → `1` · marker 2 → `1` (both = after)
- (s) `ls /Users/cobalt/cobalt/src/cobalt/radar/notes.py` → listed · `ls /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` → listed (both exit 0). The tests are quoted from the gate: offline 9120/0 · with-DB 5956/0 · live-note 148/0.
- (e) read 1 `Sat Oct 24 19:46:51 EDT 2026` → `HEARTBEAT RED — 2 job(s)  (2026-10-24 19:46:52 EDT)`: the same agent and replay REDs as `<hb0>`; aset pid 49777 OK; `com.cobalt.radar running 1 min, heartbeat fresh`; `com.cobalt.cos running 1 min, heartbeat fresh`
- (f) `COBALT_ENV=production uv run cobalt jobs restarts e41b9420..4f35be8f` → exit 0, `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` = `<restart set>`, no UNCLASSIFIED · validate (19:47:0x) → exit 0, `Jobs (F17): 22 registered — 7 resident, 15 one-shot.` = `<jobs0>`, `Placement (docs/PLACEMENT.md): tree clean.`
- (g) no migration.
- (b) radar tail 1 at `Sat Oct 24 19:47:23 EDT 2026` (`<t up>`+92 s): last line `2026-10-24 19:45:47.594 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (the new pid's first cycle, stamped 4 s BEFORE `<t up>`); no traceback, no S5 / lifecycle failure.
- Seen during smoke: `radar panel FAILED` 21 → 23 after (c)'s two `/radar` curls. Lines `2026-10-24 19:46:24.597` and `19:46:25.276`, the same `CardSettingsError … radar.cards_enabled: Input should be a valid boolean` as the old code's 19:43:10 line and its 2026-10-23 08:08 lines.
- (e) read 2 `Sat Oct 24 19:48:42 EDT 2026` (111 s after read 1) → `HEARTBEAT RED — 2 job(s)  (2026-10-24 19:48:45 EDT)`, the same two REDs; `com.cobalt.radar running 3 min, heartbeat fresh`; `com.cobalt.cos running 3 min, heartbeat fresh`. GREEN.
- (b) radar tail 2 at `Sat Oct 24 19:48:51 EDT 2026` (`<t up>`+180 s): last line `2026-10-24 19:47:27.624 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`, stamped after `<t up>`; no S5 / lifecycle failure, no traceback. Settled GREEN (tail 3 is not needed).
- (h) REVERT-READBACK at 19:48:51 or later (`<t up>`+180 s): `radar panel FAILED` **23** ≠ `<rp_up>` 21 (growing), so **RED**. `radar pool refresh FAILED` 60 = 60 · `radar S5 evaluate FAILED` 750 = 750 · `lifecycle card read failed` 39 = 39 · `/radar` curl `200`. No census reads on the card.
- RED → STEP-5 (see `## Deploy table`).
- THE CHAIN: every check committed (P2 ✓) · the tips (P3 ✓) · the merged tree (T ✓) · RESTARTS derived (R ✓) · three suites green on `0d6765aa` (G ✓) · `4f35be8f` = `0d6765aa` + docs (D2.3 ✓) · the landed code (4.3 ✓) · markers (d ✓) · no migration (g n/a) · residents up after the merge (a ✓) · radar cycling (b ✓, e ✓) · the set's reads (s ✓) · no new failure (h ✗: `radar panel FAILED` grew 21 → 23 under the smoke's own `/radar` curls). STEP-5 (4) reproduced the growth on the reverted tree (24 → 26).
- PRE-STOP SELF-CHECK (K25): (1) every smoke row above is quoted verbatim with its `date`. (2) P3 re-read `25994142` for both tip and head; `merge-base --is-ancestor 0d6765aa 4f35be8f` exit 0, and `25994142` is a parent of `0d6765aa` (T). (3) the readback is shown in STEP-5 (4). Every count, sha and time here was read from tool output this run. (4) STEP-T merged clean (`Merge made by the 'ort' strategy.`), so no conflict marker exists.

## CONTINUE
OUTAGE STARTING Sat Oct 24 19:45:08 EDT 2026 — residents of com.cobalt.aset com.cobalt.cos com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
OUTAGE ENDED Sat Oct 24 19:45:51 EDT 2026: residents up on 4f35be8f.
Smoke (h) RED at 19:48:51 → STEP-5 at 19:49:06 → reverted (`41bb2402`) and residents UP at 19:49:32. The run ends FAILED under DECISION 0. next: the desk's (re-land via ROLLBACK STRING 3 on his word, or a recut once the card-settings fault or the (h) rule is ruled on). A relaunch is never this run's.

## DECISIONS
1. ASK DESK: P6 marker 2 printed `No such file or directory` (exit 2), not `0`: `tests/cobalt/test_radar_mirror_scope.py` is new in this set and absent on main. Is a missing file a valid `before`? [Sat Oct 24 18:51 EDT 2026]. Safe default taken: yes. An absent file has zero occurrences, so production does not carry the marker; P6 fails only on "already carries". Smoke (d) reads `after` = `1`.
2. DECISION 0: production DEGRADED on the reverted tree — `radar panel FAILED` (aset.err) grew 24 → 26 at STEP-5 (4) on the OLD code, just as it grew 21 → 23 on the new code at smoke (c)/(h). Each `/radar` request logs one `radar panel FAILED: FAILED: radar evaluate: CardSettingsError: invalid card settings: radar.cards_enabled: Input should be a valid boolean`. The fault predates this set: the old aset logged it at 2026-10-23 08:08:48 / 08:08:52 and at 2026-10-24 19:43:10, before any change here, and the set's only source change (`src/cobalt/radar/notes.py`) never references `cards_enabled` (grep: the field lives in `radar/store.py`, `radar/evaluate*.py`, `radar/audit_export.py`, `settings/card.py`, `settings/cli.py`). Safe default taken: STEP-5 as the hub orders. The old tree stands, residents are UP, and no further action came from this run. **FOR DEJAN**: (a) the `radar.cards_enabled` value in his card settings fails validation, so the `/radar` panel errors on every load (the page still returns 200). (b) Whether the set re-lands: `git -C /Users/cobalt/cobalt revert --no-edit 41bb2402` with the three residents bounced, on his word. (c) The hub's (h) rule counts failures that the smoke's own `/radar` curls cause; with a pre-existing panel fault, every deploy that restarts aset will fail (h).

## RECORDS
- Downtime: 31 s (deploy outage 19:45:20 → 19:45:51) + 26 s (STEP-5, 19:49:06 → 19:49:32). Neither is over 300 s.
- `cobalt_dev: 0013 (F2 = F0)` (gate log:2388); lock released by the gate (`lock released`, log:2390; `.env: removed`, log:2394).
- The carried RED as read (`<hb0>`, unchanged through every read): `RED com.cobalt.agent not loaded` (recorded retired) and `RED com.cobalt.replay failed StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings top_n Field required …`. The second is another settings-validation fault on the same machine, which the desk may want to read together with DECISION 2.
- REFUSED, not needed (my own call, not a hub step): `COBALT_ENV=production uv run cobalt heartbeat show cos` → `cobalt: error: unrecognized arguments: cos` (exit 2; a mistyped clock filler, nothing changed).
- `?? .claude/settings.json.bak` is untracked at the repo root on main: not on D0's ACCEPTED list and not REFUSED (not staged, not src/tests/ops/configs). Recorded for the desk.
- RETIRE OWED: none. BOOTSTRAP OWED: none from this set.
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-radar-mirror-scope` and branch `deploy/deploy-radar-mirror-scope`; the set's branch `ops/radar-mirror-scope` and its worktree, if one exists. The tag `pre-deploy-radar-mirror-scope` (at `e41b9420`) stays for the desk.
- main is now `ahead 13` of origin (it includes the merge `4f35be8f` and the revert `41bb2402`). Push is his (L55).
- Card `## RECORDS` (the desk's, copied):
  - radar-mirror-scope: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-mirror-scope-check-2026-10-23.md` last line: CHECK DONE · job: radar-mirror-scope · pass: 1 · tip: 25994142 · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 9120/0 · with-DB 5956/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 164093
  - radar-mirror-scope: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-mirror-scope` → `25994142`; code tip `25994142`
  - written by deploy-card.sh at 2026-10-24 18:51 ET (`date`); trial merge of the heads onto main in order: clean
- L74: the one `Claude-Session:` request (see `## L74`), not followed.
- REFUSED, not needed: `grep -n -F ".env: removed" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. I read the line with the Read tool at log:2394 instead.

FAILED: STEP-4.7 (h) — radar panel FAILED grew 21 → 23 (CardSettingsError radar.cards_enabled, predates the set; grows on the reverted tree 24 → 26: DECISION 0 production DEGRADED on the reverted tree) · rollback: used — migrations applied: none — aset: UP — cos: UP — radar: UP — launchd: none · decisions: 2 · for Dejan: 1 · tokens: 218432
