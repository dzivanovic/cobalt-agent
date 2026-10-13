# deploy k5-gate-1013 · SET: radar · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/k5-gate-1013` (code tip `5b3c525b`, head `56472a30`) through DEPLOY-HUB. In progress.

## L74
- One attribution reminder in this session asked commits to carry a `Claude-Session:` line. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (DEPLOY-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/473-deploy-k5-gate-card.md"` → exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/473-deploy-k5-gate-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/473-deploy-k5-gate-card.md" · 0 · e0adf140c8d8d602e53a7304f84dbb486c439013
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/473-deploy-k5-gate-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT

| rule | command | exit | result verbatim |
|---|---|---|---|
| first launch | `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-k5-gate-1013.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Tue Oct 13 07:33:57 EDT 2026` |
| P2 check line | `tail -n 3 ".../reports/k5-gate-check-2026-10-13.md"` | 0 | `CHECK DONE · job: k5-gate-1013 · pass: 1 · tip: 5b3c525b · house A: Grok FINDINGS: 1 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 3 · house B: none available · suites: offline 4317/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 228916` — carries `held unfixed: 0`, `ready: YES`, `tip: 5b3c525b` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/k5-gate-check-2026-10-13.md"` | 0 | `1a93a59cc4b1179bd3f432186b5bab0330f4d101` |
| P2 unchanged | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/k5-gate-check-2026-10-13.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 5b3c525b` | 0 | `5b3c525b` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/k5-gate-1013` | 0 | `56472a30` (= TIP) |
| P3 ancestry | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5b3c525b 56472a30` | 0 | — |
| P3 head adds docs only | `git -C /Users/cobalt/cobalt diff --stat 5b3c525b 56472a30 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate status | `git -C /Users/cobalt/cobalt-wt/deploy-k5-gate-1013 status --short --branch` | 0 | `## deploy/k5-gate-1013` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-k5-gate-1013 rev-parse --short=8 HEAD` | 0 | `e0adf140` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor e0adf140 main` | 0 | — |
| P5 gate holds nothing | `git -C /Users/cobalt/cobalt log --oneline main..deploy/k5-gate-1013` | 0 | empty |
| P6 marker 1 | `grep -c -F "card 446" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` | 1 | `0` (before) |
| P6 marker 2 | `grep -c -F "card 446" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` | 1 | `0` (before) |
| P6 marker 3 | `grep -c -F "card 446" /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` | 1 | `0` (before) |
| P6 marker 4 | `ls /Users/cobalt/cobalt/tests/ops/test_the_rule_sweep.py` | 1 | `No such file or directory` (absent = before) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 56472a30 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 40377` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 22724` |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 14763).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-k5-gate-1013 merge --no-edit 56472a30` → `Merge made by the 'ort' strategy.` — 8 files changed, 878 insertions(+), 48 deletions(-) (`ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_card.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_the_rule_sweep.py` (new), `docs/40 - DevDocs/reports/k5-gate-build-2026-10-13.md` (new)).
- `<m1>` = `035bbb0f` (`rev-parse --short=8 HEAD`).
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent e0adf140..deploy/k5-gate-1013` → `035bbb0f Merge commit '56472a30' into deploy/k5-gate-1013`.
- `merge-base --is-ancestor 5b3c525b deploy/k5-gate-1013` → exit 0 · `merge-base --is-ancestor 56472a30 deploy/k5-gate-1013` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat e0adf140 deploy/k5-gate-1013 -- src/cobalt/db_migrations` → nothing (no migration; MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat e0adf140 deploy/k5-gate-1013 -- configs ops` →
  ```
   ops/desk/deploy-card.sh  | 80 ++++++++++++++++++++++++++++++++++++++----------
   ops/desk/deploy-step0.sh | 80 ++++++++++++++++++++++++++++++++++++++----------
   ops/desk/desk-launch.sh  | 80 ++++++++++++++++++++++++++++++++++++++----------
   3 files changed, 192 insertions(+), 48 deletions(-)
  ```
  No plist added, modified or removed.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-k5-gate-1013` · `ls -la .../deploy-k5-gate-1013/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the worktree `.venv`: `Installed 254 packages in 846ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/k5-gate-build-2026-10-13.md	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_card.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
tests/ops/test_the_rule_sweep.py	A	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = EMPTY (none). No UNCLASSIFIED row. MIGRATIONS: none, so an empty set is consistent.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold — the check's stop line carries `with-DB 0/0`; the gate runs whole (`--deploy`).
- (a0) `ls -la .../.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.10s` (0 failed; every skip a with-DB skip: `Postgres env settings not available` / `requires_db`).
- Deselects: none — the build report `k5-gate-build-2026-10-13.md` names no with-DB pass-1 deselect (its three `deselected` mentions are `-k` filter counts). TICKERS: none. No `--migration`.
- `ls -la .../.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-k5-gate-1013 all --deploy` (background) → exit 0. Verdict lines whole:
  ```
  offline 4317/0
  lock: waited 0 min
  proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
  LEVEL 0013
  pass 1: whole (deploy)
  stray rows: not read (no --tickers given)
  cobalt_dev: 0013 — F2 = F0
  .env: removed
  with-DB 5220/0
  SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
  SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
  SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
  SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
  SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
  SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
  SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
  live-note 146/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-k5-gate-1013-all-20261013-073542.log
  ```
- (a) offline `4317/0`. (c)+(c3) with-DB `5220/0`. (e) live-note `146/0`.
- SKIPPED lines: all seven inside the allowed set. `test_s3_c4_experiments.py:95` is the skip of `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F` → `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`, decorator at 95). The replay_line skip names `COBALT_TEST_LIVE_DRC` (allowed).
- (c2) `dev forward: APPLIED 08:01:02` (log line 1117).
- (f) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log 902) · `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log 2037) → `cobalt_dev: 0013 — F2 = F0` (log 2089).
- THE RELEASE: log 2090–2095 `release-devdb-lock.sh deploy-k5-gate-1013` → `lock released`, `.env: removed` (the log stamps no clock time; released before 08:06:19, my `date` after the completion notice). `ls -la .../deploy-k5-gate-1013/.env` → No such file · `grep -c -x -F "deploy-k5-gate-1013" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 035bbb0f

## Deploy table

### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| main branch | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 103]` |
| main porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M` = `.claude/settings.json`, `configs/cobalt/rules.yaml`, seven `docs/40 - DevDocs/reports/*` files; `??` = `docs/40 - DevDocs/…` paths plus `.claude/settings.json.bak` and `docs/30 - Design/f20-f23-lock-seam-2026-10-13.md` (see DECISIONS 1); no dirty `src/`, `tests/`, `ops/`, `configs/` path beyond `rules.yaml` |
| main moved outside docs | `git -C /Users/cobalt/cobalt diff --stat e0adf140 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe tag | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-k5-gate-1013` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-k5-gate-1013' (was e0adf140)` |
| probe commit | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 5ede27b2] scratch: …` · — · `e0adf140 docs(desk): R1349 R1350 desk takeover d508104f, 446 deploy card 473, wake-up row` (HEAD back) |
| TAG free | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-13-k5-gate` | 1 | — |
| pre-tag free | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-k5-gate-1013` | 1 | — |

### STEP-D1 (baseline)
- `date` → `Tue Oct 13 08:06:53 EDT 2026` · `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-13 08:06:54 EDT)`; `OK   com.cobalt.aset              running   loaded, pid 40377 [launchd probe]`; `OK   com.cobalt.radar             running   running 499 min, heartbeat fresh`; `OK   com.cobalt.agent             running   pid 14763 alive …`; `OK   radar                    scanning (premarket), members 50`; one AMB: `com.cobalt.herdr unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) …; runs outside launchd by declared interim`. No RED.
- `COBALT_ENV=production uv run cobalt validate` → exit 0, `<val0>` ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 7.7 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 40377` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 22724` · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 14763).` · `ps -p 14763` → `14763 ??         0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → last cycle `2026-10-13 08:04:53.773 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1791893014688`, price-floor lines to 08:06:44, no traceback.
- LOG BASELINES: `<a0>` 279 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` → `200`.
- MARKERS again: `0` · `0` · `0` · `ls … test_the_rule_sweep.py` → No such file (absent). All `before`.
- MIGRATIONS: none → no `<RB>`, no D1-M proof-only.

## Smoke

## CONTINUE
next: STEP-D2 (D2.0 commit of this report)

## DECISIONS
- 1. ASK DESK: `git status --porcelain` on `main` shows two untracked paths outside D0's ACCEPTED list and outside its REFUSED list: `?? .claude/settings.json.bak` and `?? "docs/30 - Design/f20-f23-lock-seam-2026-10-13.md"`. Neither is staged, neither is under `src/`, `tests/`, `ops/`, `configs/`, and an untracked file is not in the tree that lands. Safe default taken: go on (the hub's refusal names only staged and `src/` `tests/` `ops/` `configs/` paths). [08:07 EDT]
- 2. ASK DESK: the card's one `## SMOKE READS` line (304 passes THE RULE, census) is, in the card's own words, "the desk's next step after this deploy and after row CR, not a gate of this set"; it runs `sh /Users/cobalt/.claude/ops/deploy-card.sh` with "the desk's own" `--job`/`--set`/`--worktree`/`--tag`/`--out` and writes a card. That string is not on this run's line (CLASS (a) is `/Users/cobalt/cobalt/ops/desk/*` only) and the values are the desk's. Safe default taken: not run at D1 or smoke (s); recorded `UNPROVEN (L70)` — the desk runs it. [08:07 EDT]

## RECORDS

(run in progress — next step under ## CONTINUE)
