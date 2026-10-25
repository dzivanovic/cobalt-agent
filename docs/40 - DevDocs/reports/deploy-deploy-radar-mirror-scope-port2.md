# deploy-deploy-radar-mirror-scope-port2 — SET: radar-mirror-scope-port — MIGRATIONS: none

## §0 Headline
- Deploy of `ops/radar-mirror-scope-port` (code tip `283389ff`, head `50116c45`), card `prompts/2026-10-23/1036-deploy-radar-mirror-scope-port2-card.md`. In progress.

## L74
- The session's system reminder asked commits to also carry a `Claude-Session:` line. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-23/1036-deploy-radar-mirror-scope-port2-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-23/1036-deploy-radar-mirror-scope-port2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-23/1036-deploy-radar-mirror-scope-port2-card.md" · 0 · 6bf2f290600f519b019a50049e1c5d2685939d17
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-23/1036-deploy-radar-mirror-scope-port2-card.md" · 0 · nothing
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
| first launch | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P0 | `authorize.sh deploy` | 0 | `AUTHORIZED` (above) |
| P1 DATE | `date` | 0 | `Sat Oct 24 22:32:57 EDT 2026` — outside the 21:30–22:30 ET backup window |
| P2 check last line | `tail -n 3 ".../radar-mirror-scope-port-check-2026-10-24.md"` | 0 | `CHECK DONE · job: radar-mirror-scope-port · pass: 1 · tip: 283389ff · house A: Gemini FINDINGS: 0 · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 9120/0 · with-DB 5956/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 167121` — carries `held unfixed: 0`, `ready: YES`, `tip: 283389ff` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/.../radar-mirror-scope-port-check-2026-10-24.md"` | 0 | `89b1260326f2073c0636cc4bec74888dbe9983ea` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../radar-mirror-scope-port-check-2026-10-24.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 283389ff` | 0 | `283389ff` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-mirror-scope-port` | 0 | `50116c45` = card row and `TIP` |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 283389ff 50116c45` | 0 | — |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 283389ff 50116c45 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no session holds the lock |
| P5 gate status | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-radar-mirror-scope-port2` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `6bf2f290` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 6bf2f290 main` | 0 | — |
| P5 gate empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-radar-mirror-scope-port2` | 0 | empty |
| P6 marker 1 | `grep -c -F "MIRROR_SOURCE_PREFIX = " /Users/cobalt/cobalt/src/cobalt/radar/notes.py` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` | 2 | `grep: ...test_radar_mirror_scope.py: No such file or directory` — the file is new on the branch (`git diff --stat main 283389ff -- tests/cobalt/test_radar_mirror_scope.py` → `201 ++++` insertions only); production does not carry it (see DECISIONS 1) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 50116c45 -- src/cobalt/db_migrations` | 0 | nothing — `MIGRATIONS: none` holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 51019` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 51036` |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent retired | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1` — `com.cobalt.agent recorded retired` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` (expected: recorded retired) |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| merge head | `git -C <GATE> merge --no-edit 50116c45` | 0 | `Merge made by the 'ort' strategy.` — 9 files, 559 insertions, 16 deletions (src/cobalt/radar/notes.py, 5 test files, 3 docs) |
| m1 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `9bcc7868` = `<m1>` |
| merges | `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 6bf2f290..deploy/deploy-radar-mirror-scope-port2` | 0 | `9bcc7868 Merge commit '50116c45' into deploy/deploy-radar-mirror-scope-port2` |
| code tip in | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 283389ff deploy/deploy-radar-mirror-scope-port2` | 0 | — |
| head in | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 50116c45 deploy/deploy-radar-mirror-scope-port2` | 0 | — |
| migrations | `git -C /Users/cobalt/cobalt diff --stat 6bf2f290 deploy/deploy-radar-mirror-scope-port2 -- src/cobalt/db_migrations` | 0 | nothing (`MIGRATIONS: none`) |
| STEP-C diff | `git -C /Users/cobalt/cobalt diff --stat 6bf2f290 deploy/deploy-radar-mirror-scope-port2 -- configs ops` | 0 | nothing |
| STEP-C | `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 6bf2f290 deploy/deploy-radar-mirror-scope-port2` | 0 | `STEP-C: ADMITTED 0` |

`<launchd set>`: empty · `<deferred set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (first run created the gate `.venv`: `Using CPython 3.14.3 … Installed 257 packages in 884ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/radar/notes.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-port-build-2026-10-24.md	A	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-port-build-2026-10-24.result	A	DOCS	-
src/cobalt/radar/notes.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_mirror_scope.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_notes.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
- No `UNCLASSIFIED` row. `launchctl print gui/501/com.cobalt.cos` → exit 0, `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.cos.plist`, `pid = 51030` — kept.
- `<restart set>`: `com.cobalt.aset com.cobalt.cos com.cobalt.radar`
- `<deferred set>`: empty
- `<launchd set>`: empty
- com.cobalt.agent: recorded retired — not restarted (not in the derived set either)

## L68 GATE
THE EQUAL-TREE CLAUSE holds: ONE branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat 283389ff 9bcc7868 -- . ":(exclude)docs"` → exit 0, prints nothing; the check's stop line carries `with-DB 5956/0` (> 0). The check's suite lines are the gate's, quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-mirror-scope-port-check-2026-10-24.md` lines 187–213 (its W: `sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-mirror-scope-port all --deploy --deploy-gate` on `283389ff`, exit 0):
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
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-mirror-scope-port-all-20261024-210338.log
```
- Check report: offline `4984 passed, 878 skipped, 4 xfailed` + tests/ops `4136 passed, 1 xfailed` = 9120; with-DB pass 1 `5712 passed, 9 skipped, 138 deselected, 7 xfailed`, pass 2 `244 passed, 1 deselected` = 5956; `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` = `F2`; live-note `148 passed, 1 skipped` (skip names `COBALT_TEST_LIVE_DRC`).
- SKIPPED judgment (c): all nine lines are inside the allowed set (cards_picks :388, :401; checkpoints_live and playbook_live with `COBALT_LIVE_VAULT_ROOT not set`; radar_evaluate :695; replay_line `COBALT_TEST_LIVE_DRC`; s3_c4_experiments; catalyst :365; predicate :262). The clause stands; (a)–(f) not re-run; this run held no lock and touched no `cobalt_dev`.
- (a0) THE EARLY READ, run in `<GATE>`: `ls -la <GATE>/.env` → No such file; `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → exit 0, `265 passed, 163 skipped in 19.44s` (every skip `Postgres env settings not available` / `requires_db`) — `0 failed`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 9bcc7868

## Deploy table
| step | command | exit | result |
|---|---|---|---|
| D0 date | `date` | 0 | `Sat Oct 24 22:35:38 EDT 2026` |
| D0 main | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 10]`; every line ` M` / `??` under `docs/40 - DevDocs/`, plus ` M .claude/settings.json` and `?? .claude/settings.json.bak` |
| D0 code paths | `git -C /Users/cobalt/cobalt status --porcelain -- src tests ops configs .claude` | 0 | ` M .claude/settings.json` · `?? .claude/settings.json.bak` — no staged line, no dirty `src/` `tests/` `ops/` `configs/` path (see RECORDS on the `.bak`) |
| D0 main moved | `git -C /Users/cobalt/cobalt diff --stat 6bf2f290 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| D0 probe | `tag scratch-allow-probe-…` · `tag -d …` · `commit --allow-empty …` · `reset --soft HEAD~1` · `log --oneline -1` | 0 each | `Deleted tag 'scratch-allow-probe-deploy-radar-mirror-scope-port2' (was 6bf2f290)` · `[main 36fb8ec6] scratch: allowlist probe (reverted next line)` · HEAD back `6bf2f290 docs(desk): R2429 deploy card 1036 radar-mirror-scope-port2 (fresh report path)` |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-24-radar-mirror-scope-port2` · `… refs/tags/pre-deploy-radar-mirror-scope-port2` | 1 · 1 | both free |
| D1 date | `date` | 0 | `Sat Oct 24 22:36:00 EDT 2026` |
| D1 `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | `HEARTBEAT RED — 2 job(s)  (2026-10-24 22:36:01 EDT)`; aset/sheet OK (`sheet HTTP http://127.0.0.1:5010/ -> 200`, `com.cobalt.aset running loaded, pid 51019`); `OK radar idle (overnight)`; `OK com.cobalt.radar running running 167 min, heartbeat fresh`; `OK com.cobalt.cos running running 167 min, heartbeat fresh`. The two REDs, named, not a stop: `RED com.cobalt.agent not loaded NOT LOADED in launchd …` (recorded retired) and `RED com.cobalt.replay failed StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings top_n Field required …`. OWED (deferred bootstrap): prefill-refresh, checkpoint-0715/0745/0815/0845, playbook |
| D1 `<val0>` | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 `<jobs0>` | (validate) | — | `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 22 label(s), exact match.` |
| D1 backup | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 0.9 h old` |
| D1 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `<aset pid>` = `51019` |
| D1 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `<radar pid>` = `51036` |
| D1 cos | `launchctl print gui/501/com.cobalt.cos` | 0 | `state = running`, `<cos pid>` = `51030` |
| D1 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` (recorded retired; no `ps -p`) |
| D1 radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 0 | last `2026-10-24 22:34:33.909 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`; eight cycle lines, no traceback |
| D1 baselines | the eight `grep -c` reads | — | `<a0>` 296 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 26 · `<rpr0>` 60 · `<re0>` 750 · `<lc0>` 39 |
| D1 curl | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | 0 | `200` |
| D1 markers | the two `## MARKERS` reads | 1 · 2 | `0` · `No such file or directory` (as P6) |
| D1 launchd set | — | — | empty: nothing |
| D1 migration | — | — | `MIGRATIONS: none`: no `<RB>`, no proof-only |
| D2.0 shipped | `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 6bf2f290 "<card>"` | 0 | nothing |

## Smoke

## CONTINUE
next: STEP-D2 (D2.0 report commit)

## DECISIONS
1. P6 marker 2: the card's `before 0` command exits 2 `No such file` because the test file is new on the branch; read as "production does not carry the marker" (the purpose of P6). Default taken: go on. The desk may write `before: No such file` on future cards for a new file.

## RECORDS
- Card `## RECORDS` (desk's facts, copied):
  - radar-mirror-scope-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-mirror-scope-port-check-2026-10-24.md` last line: CHECK DONE · job: radar-mirror-scope-port · pass: 1 · tip: 283389ff · house A: Gemini FINDINGS: 0 · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 9120/0 · with-DB 5956/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 167121
  - radar-mirror-scope-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-mirror-scope-port` → `50116c45`; code tip `283389ff`
  - written by deploy-card.sh at 2026-10-24 22:32 ET (`date`); trial merge of the heads onto main in order: clean
- `?? .claude/settings.json.bak` is untracked on `main`: outside D0's accepted list and outside its refused list (not `src/`, `tests/`, `ops/`, `configs/`, not staged). Read as no refusal; the desk may clean it.

(run in progress — next step under ## CONTINUE)
