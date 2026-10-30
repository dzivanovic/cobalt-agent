# deploy launcher-tip-prefix — set: launcher-tip-prefix · migrations: none

## §0 Headline
- (in progress)

## L74
- 22:35 ET: this session's system reminder asked commits to carry a `Claude-Session:` line. Recorded as data (L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-29/1097-deploy-launcher-tip-prefix-card.md"` (22:35 ET), exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-29/1097-deploy-launcher-tip-prefix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-29/1097-deploy-launcher-tip-prefix-card.md" · 0 · 34f5d0bdd1ae9f8b89db8e52ed1a33e17e2a5f79
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-29/1097-deploy-launcher-tip-prefix-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
First launch: `ls -la "<REPORT>"` → `No such file or directory`.

| rule | command | exit | result |
|---|---|---|---|
| P0 | `authorize.sh deploy "<card>"` | 0 | `AUTHORIZED` (above) |
| P1 | `date` | 0 | `Thu Oct 29 22:35:18 EDT 2026` — outside 21:30-22:30 |
| P2 check | `tail -n 3 ".../launcher-tip-prefix-check-2026-10-29.md"` | 0 | `CHECK DONE · job: launcher-tip-prefix · pass: 1 · tip: 5babf712 · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 9181/1 · with-DB 0/0 · live-note 148/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 163970` — carries `held unfixed: 1` and `ready: NO` |
| P2 check committed | `git log -1 --format=%H -- "<check>"` | 0 | `79186d4c3c9e0aa57ad3ceb75cfaa0398f25feef` |
| P2 check clean | `git diff --stat -- "<check>"` | 0 | nothing |
| P2 fix-round tip | `merge-base --is-ancestor 5babf712 2da6759e` | 0 | — |
| P2 fix report committed | `git log -1 --format=%H ops/launcher-tip-prefix -- "<fix report>"` | 0 | `3a6c1bfa9cd99eb33dc9ecef767c124199e69e19` (on main: `git log -1 -- "<fix report>"` → empty, file not on main; `diff --stat` → nothing) |
| P2 fix report last line | `git show "3a6c1bfa:<fix report>"` | 0 | `BUILT · job: launcher-tip-prefix · tip: 2da6759e \| on 4f1c991f \| migration: none \| offline 9185/0 \| with-DB 0/0 \| live-note 148/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 4 of 4 \| self-check: 3 of 3 \| decisions: 2 · for Dejan: 0 · tokens: 106862` |
| P2 held ids | `grep -n -F "HELD, NOT FIXED" "<check>"` | 0 | one id: `O1` (`:5`, `:133`, `:140`, `:166`, `:172`) |
| P2 FIXED line | same `git show` | 0 | `FIXED: O1 — tests/ops/test_card_fill.py::test_1085_check_o1_a_nine_hex_built_line_fills_the_eight_hex_tip` |
| P2 FIXED test at tip | `git show 2da6759e:tests/ops/test_card_fill.py` | 0 | `def test_1085_check_o1_a_nine_hex_built_line_fills_the_eight_hex_tip(desk):` present, no xfail mark |
| P3 code tip | `rev-parse --short=8 2da6759e` | 0 | `2da6759e` |
| P3 head | `rev-parse --short=8 ops/launcher-tip-prefix` | 0 | `3a6c1bfa` (= `TIP`) |
| P3 ancestor | `merge-base --is-ancestor 2da6759e 3a6c1bfa` | 0 | — |
| P3 docs only | `diff --stat 2da6759e 3a6c1bfa -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 status | `git -C <GATE> status --short --branch` | 0 | `## deploy/launcher-tip-prefix` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `34f5d0bd` = `<m0>` |
| P5 ancestor | `merge-base --is-ancestor 34f5d0bd main` | 0 | — |
| P5 empty | `log --oneline main..deploy/launcher-tip-prefix` | 0 | empty |
| P6 | `grep -c -F "card 1085" .../desk-launch.sh` | 1 | `0` (before) |
| P6 | `grep -c -F "card 1085" .../preflight.sh` | 1 | `0` (before) |
| P6 | `grep -c -F "test_1085" .../test_desk_launch_prechecks.py` | 1 | `0` (before) |
| P6 | `grep -c -F "test_1085" .../test_preflight.py` | 1 | `0` (before) |
| P7 | `diff --stat main 3a6c1bfa -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 68013` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 68034` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 retired | `grep -c -x -F "com.cobalt.agent" .../retired-labels` | 0 | `1` — `com.cobalt.agent recorded retired` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` |

## THE TREE
- `git -C <GATE> merge --no-edit 3a6c1bfa` → `Merge made by the 'ort' strategy.` (8 files changed, 319 insertions(+), 14 deletions(-)).
- `git -C <GATE> rev-parse --short=8 HEAD` → `2b57dabe` = `<m1>`.
- `log --oneline --merges --first-parent 34f5d0bd..deploy/launcher-tip-prefix` → `2b57dabea Merge commit '3a6c1bfa' into deploy/launcher-tip-prefix` (one line, one head).
- `merge-base --is-ancestor 2da6759e deploy/launcher-tip-prefix` → exit 0; `… 3a6c1bfa …` → exit 0.
- `diff --stat 34f5d0bd deploy/launcher-tip-prefix -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `diff --stat 34f5d0bd deploy/launcher-tip-prefix -- configs ops` →
```
 ops/desk/card-fill.sh   |  7 ++++---
 ops/desk/desk-launch.sh | 14 ++++++++++++--
 ops/desk/preflight.sh   | 18 +++++++++++++-----
 3 files changed, 29 insertions(+), 10 deletions(-)
```
  `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 34f5d0bd deploy/launcher-tip-prefix`, exit 0 → `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD`, exit 0 (uv created `.venv`, `Installed 257 packages in 1.00s`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/launcher-tip-prefix-build-2026-10-29.md	A	DOCS	-
docs/40 - DevDocs/reports/launcher-tip-prefix-build-2026-10-29.result	A	DOCS	-
ops/desk/card-fill.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/preflight.sh	M	operator script; no Cobalt reader	-
tests/ops/test_card_fill.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
tests/ops/test_preflight.py	M	test/documentation; no resident	-
RESTARTS: none
```
- No UNCLASSIFIED row. `<restart set>`: EMPTY (no resident goes down). `<deferred set>`: empty. `<launchd set>`: empty.
- `com.cobalt.agent: recorded retired — not restarted`.

## L68 GATE
- EQUAL-TREE CLAUSE: one branch, but the check's stop line carries `with-DB 0/0` (and the check tip `5babf712` ≠ code tip) → the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_archiver_migrations.py … tests/cobalt/test_jobs_restarts.py` (the 17 files), exit 0 → `265 passed, 163 skipped in 19.88s` — 0 failed.
- Gate launched: `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-launcher-tip-prefix all --deploy --deploy-gate` (no `--deselect`: the build deselected none, with-DB 0/0; `TICKERS: none`; `MIGRATIONS: none`). Exit 0. Verdict lines WHOLE:
```
tests/ops: run (deploy gate)
offline 9189/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 6014/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-launcher-tip-prefix-all-20261029-223746.log
```
- (a) offline `9189/0`; W line `tests/ops: run (deploy gate)`.
- (c) pass 1 whole at `0013`: the nine SKIPPED lines are each inside the allowed set (cards_picks :388, :401; checkpoints_live and playbook_live naming `COBALT_LIVE_VAULT_ROOT not set`; radar_evaluate :695; replay_line `COBALT_TEST_LIVE_DRC`; s3_c4_experiments; catalyst :365; predicate :262).
- (c2)/(c3): MIGRATIONS: none — no forward applied; `with-DB 6014/0`.
- (f) `cobalt_dev: 0013 — F2 = F0`; log `:1050` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`, `:2334` `F2: 664 35 272c95bbb12241e3611e4b36326ccf87`.
- THE RELEASE: log `:2389-2394` `release-devdb-lock.sh deploy-launcher-tip-prefix` → `lock released`, `.env: removed` (the log prints no time at that line; log stamped 22:37:46 start, verdict read 23:28 ET). `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-launcher-tip-prefix" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) live-note `148/0`; the one skip names `COBALT_TEST_LIVE_DRC` (allowed); none names `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 2b57dabe

## Deploy table
STEP-D0 (23:28 ET):
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 1]` |
| MAIN porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M` lines: `.claude/settings.json` and 14 under `docs/40 - DevDocs/`; `??` lines: all under `docs/40 - DevDocs/` but `?? .claude/settings.json.bak` (neither accepted nor a refused `src/` / `tests/` / `ops/` / `configs/` path; recorded). No staged line. |
| MAIN moved | `diff --stat 34f5d0bd main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-launcher-tip-prefix` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-launcher-tip-prefix' (was 34f5d0bdd)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 6140336a0] scratch: …` · — · `34f5d0bdd docs(desk): 1097 deploy card for launcher-tip-prefix (1085)` |
| TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-29-launcher-tip-prefix` | 1 | absent |
| TAG | `rev-parse --verify --quiet refs/tags/pre-launcher-tip-prefix` | 1 | absent |

STEP-D1 (23:29 ET):
| read | result |
|---|---|
| `date` | `Thu Oct 29 23:29:17 EDT 2026` |
| `<hb0>` `heartbeat show` | `HEARTBEAT RED — 1 job(s)  (2026-10-29 23:29:18 EDT)`; the one RED: `RED  com.cobalt.agent             not loaded NOT LOADED in launchd — …` (agent recorded retired; not the aset / sheet / radar probe → named, not a stop). `OK   sheet HTTP … -> 200`, `OK   radar                    idle (overnight)`, `OK   com.cobalt.aset              running   loaded, pid 68013`, `OK   com.cobalt.radar             running   running 95 min, heartbeat fresh`, `OK   com.cobalt.cos               running   running 95 min, heartbeat fresh`; `AMB  com.cobalt.herdr unmanaged`; OWED (deferred bootstrap): prefill-refresh, checkpoint-0715/0745/0815/0845, playbook. |
| `<val0>` `validate` | exit 0; `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`; `Placement (docs/PLACEMENT.md): tree clean.` |
| `backup status` | `newest snapshot: 1.6 h old` (ssd ARMED) |
| aset | `state = running`, `pid = 68013` |
| radar | `state = running`, `pid = 68034` |
| cos | not in `<restart set>` — not read |
| agent | `  Cobalt is OFFLINE.` (recorded retired; no `ps -p`) |
| `tail -n 8 radar.err` | last: `2026-10-29 23:29:17.912 | INFO | cobalt.radar.runner:resident:645 - radar cycle: idle:overnight scan_id=None` |
| `<a0>` `<ta0>` `<tr0>` `<tc0>` | `303` · `217` · `1` · `0` |
| `<rp0>` `<rpr0>` `<re0>` `<lc0>` | `31` · `60` · `750` · `39` |
| `curl …/radar` | `200` |
| MARKERS | `0` · `0` · `0` · `0` (before) |
| LAUNCHD SET | empty — nothing |
| MIGRATION | none — no `<RB>`, no D1-M |

D2.0: `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 34f5d0bd "<card>"` → printed nothing, exit 0.

## Smoke

## CONTINUE
next: STEP-D2.1 (report committed at D2.0; gate green at 23:28 ET)

## DECISIONS

## RECORDS
- REFUSED, not needed: `git -C /Users/cobalt/cobalt grep -n -F "def test_1085_check_o1_…" 2da6759e -- tests/ops/test_card_fill.py` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." Read instead with the listed `git -C * show*`.

(run in progress — next step under ## CONTINUE)
