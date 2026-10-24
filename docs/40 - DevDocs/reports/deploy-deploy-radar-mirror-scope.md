# deploy-radar-mirror-scope — SET: radar-mirror-scope — MIGRATIONS: none

## §0 Headline
- (filled at the end)

## L74
- none so far.

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

## Smoke

## CONTINUE
next: STEP-D2 (D2.0 report commit; D0 and D1 done, nothing in production changed)

## DECISIONS
1. ASK DESK: P6 marker 2 printed `No such file or directory` (exit 2), not `0`: `tests/cobalt/test_radar_mirror_scope.py` is new in this set and absent on main. Is a missing file a valid `before`? [Sat Oct 24 18:51 EDT 2026]. Safe default taken: yes. An absent file has zero occurrences, so production does not carry the marker; P6 fails only on "already carries". Smoke (d) reads `after` = `1`.

## RECORDS
- REFUSED, not needed: `grep -n -F ".env: removed" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. I read the line with the Read tool at log:2394 instead.

(run in progress — next step under ## CONTINUE)
