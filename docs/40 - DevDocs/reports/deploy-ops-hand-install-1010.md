# deploy ops-hand-install-1010 · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/ops-hand-install-1010` at `680eca0e` (OPS-HAND.md installed title, STANDING-LIST §8, one test). Running.

## L74
- none arrived in a tool result.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/313-deploy-ops-hand-install-card.md"` → exit 0, verbatim:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/313-deploy-ops-hand-install-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/313-deploy-ops-hand-install-card.md" · 0 · 02447573773952253cf2aad13c24ae9dd2e1cb33
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/313-deploy-ops-hand-install-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R969 row · grep -n "^| R969 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 20:| R969 | 18:51 ET | HIS RULING · APPROVED: "Approved" to the plate: F4 FINAL (`docs/30 - Design/F4-FINAL-2026-10-10.md`) and ops-hand D1-D5; words: `cto-2026-10-10-words.md` R969. Next: F4 card, F5 F20 F21 F23 re-point, ops-hand install. | APPLIED: LAWS.md L63, NOW at wake-up 18:55 |
RULING 2026-10-10 R969 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R969 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 8f5586abab5f095375e2759a2377d91fc0f54d5c
RULING 2026-10-10 R969 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-10 R971 row · grep -n "^| R971 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 18:| R971 | 18:54 ET | HIS RULING · APPROVED: "Yes both" confirms R969 covered F4 FINAL and ops-hand D1-D5; words `cto-2026-10-10-words.md` R971. | APPLIED: R969 row (no new text) |
RULING 2026-10-10 R971 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R971 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · d78c66a274f2cd61cdab224c311024f1080db6a4
RULING 2026-10-10 R971 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P0 first launch | `ls -la ".../reports/deploy-ops-hand-install-1010.md"` | 1 | No such file or directory |
| P1 | `date` | 0 | `Sat Oct 10 19:56:57 EDT 2026` |
| P2 | `tail -n 3 ".../ops-hand-install-check-2026-10-10.md"` | 0 | `CHECK DONE · job: ops-hand-install-1010 · pass: 1 · tip: 680eca0e · … · held unfixed: 0 · open: 0 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 161299` — carries `held unfixed: 0`, `ready: YES`, `tip: 680eca0e` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/ops-hand-install-check-2026-10-10.md"` | 0 | `f2aadad3c857f4f6e8aa30d12d6b6d14b3595270` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 680eca0e` | 0 | `680eca0e` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/ops-hand-install-1010` | 0 | `680eca0e` (= TIP) |
| P3 | `merge-base --is-ancestor 680eca0e ops/ops-hand-install-1010` | 0 | — |
| P3 | `diff --stat 680eca0e ops/ops-hand-install-1010 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/ops-hand-install-1010` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `02447573` = `<m0>` |
| P5 | `merge-base --is-ancestor 02447573 main` | 0 | — |
| P5 | `log --oneline main..deploy/ops-hand-install-1010` | 0 | empty |
| P6 | `grep -c -F "HIS RULING · APPROVED 2026-10-10 R969" ".../prompts/OPS-HAND.md"` | 0 | `0` (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 680eca0e -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 7760` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 61093` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 680eca0e` → `Merge made by the 'ort' strategy.` (OPS-HAND.md 2 ±, STANDING-LIST.md +13, build report +203, tests/ops/test_desk_launch_ops_hand.py 26 ±).
- `<m1>` = `04a3e70e`.
- `log --oneline --merges --first-parent 02447573..deploy/ops-hand-install-1010` → `04a3e70e Merge commit '680eca0e' into deploy/ops-hand-install-1010`.
- `merge-base --is-ancestor 680eca0e deploy/ops-hand-install-1010` → exit 0.
- `diff --stat 02447573 deploy/ops-hand-install-1010 -- src/cobalt/db_migrations` → nothing (no migration).
- STEP-C: `diff --stat 02447573 deploy/ops-hand-install-1010 -- configs ops` → nothing; no plist added, changed or removed.

## RESTARTS
From `<GATE>`, `ls -la <GATE>/.env` → No such file; `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/OPS-HAND.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/ops-hand-install-build-2026-10-10.md	A	DOCS	-
tests/ops/test_desk_launch_ops_hand.py	M	test/documentation; no resident	-
RESTARTS: none
```
(preceded by uv creating the gate `.venv`: `Installed 253 packages in 872ms`). `<restart set>` = EMPTY: no resident goes down; the merge lands with residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied — the check's stop line carries `with-DB 0/0`; the gate runs whole (`--deploy`).
- (a0) `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.32s` (0 failed; skips are with-DB, `.env` absent).
- Build report `ops-hand-install-build-2026-10-10.md`: `grep -c -F "deselect"` → `0`; no `--deselect`. TICKERS none, migration none.
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-ops-hand-install-1010 all --deploy` → exit 0, verdict lines WHOLE:
```
offline 4199/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5096/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-ops-hand-install-1010-all-20261010-195828.log
```
- Log reads (`grep -n -F "passed" <log>`): `879:4199 passed, 800 skipped, 1 xfailed` (offline) · `1108:4891 passed, 7 skipped, 99 deselected, 3 xfailed` (pass 1) · `1962:205 passed, 1 deselected` (pass 2; 4891 + 205 = 5096) · `2153:146 passed, 1 skipped` (live-note).
- (c) the 7 pass-1 skips are each in the allowed set; `test_s3_c4_experiments.py:95` is the decorator of `def test_x14_live_his_template_strips_to_the_committed_fixture` (line 96). (e) live-note's one skip (log 2152) is `test_replay_line.py:266` naming `COBALT_TEST_LIVE_DRC` — allowed; none names `COBALT_LIVE_VAULT_ROOT`.
- (c2) FORWARD: no migration above `0013` in the set; `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: `.env: removed` (L76 lock released, log line 2084 `lock released`); `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-ops-hand-install-1010" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (lock dir absent).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed. `date` → `Sat Oct 10 20:28:12 EDT 2026`.

GATE GREEN on 04a3e70e

## Deploy table
| step | command | result |
|---|---|---|
| D0 | `git -C /Users/cobalt/cobalt status --short --branch` | `## main...origin/main [ahead 370]`; ` M` lines under `docs/40 - DevDocs/` and ` M .claude/settings.json`; `??` lines under `docs/40 - DevDocs/` and `?? .claude/settings.json.bak` (see DECISIONS); no staged line, no dirty src/tests/ops/configs |
| D0 | `diff --stat 02447573 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D0 probe | `tag scratch-allow-probe-ops-hand-install-1010` · `tag -d …` | ok · `Deleted tag 'scratch-allow-probe-ops-hand-install-1010' (was 02447573)` |
| D0 probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | `[main 0d344d25] scratch: …` · ok · `02447573 docs(desk): deploy card 313 ops-hand install` |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-10-ops-hand-install` · `…refs/tags/pre-ops-hand-install-1010` | exit 1 · exit 1 |
| D1 | `date` | `Sat Oct 10 20:28:38 EDT 2026` |
| D1 `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 20:28:39 EDT)`; RED: `archiver last run FAILED — last run 2026-10-10 00:54 UTC (23.6 h ago), rows written 3308843, exit 1`, `com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …`, `com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`; OK: sheet HTTP 200, `radar idle (overnight)`, `com.cobalt.aset running pid 7760`, `com.cobalt.agent running pid 22243`, `com.cobalt.radar running 779 min, heartbeat fresh`. No RED on aset / sheet / radar — the archiver/replay REDs are named, not a stop |
| D1 `<val0>` | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 `<jobs0>` | (same) | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 15 label(s), exact match.` |
| D1 | `COBALT_ENV=production uv run cobalt backup status` | `newest snapshot: 2.4 h old` |
| D1 | `launchctl print gui/501/com.cobalt.aset` · `…/com.cobalt.radar` | `state = running`, `pid = 7760` · `state = running`, `pid = 61093` |
| D1 | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 22243` | `Cobalt is ONLINE (PID: 22243).` · `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py` |
| D1 | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 8 × `radar cycle: idle:overnight scan_id=None`, last `2026-10-10 20:28:11.337`; no traceback |
| D1 counts | `<a0>` `<ta0>` `<tr0>` `<tc0>` `<rp0>` `<rpr0>` `<re0>` `<lc0>` | 277 · 217 · 0 · 0 · 18 · 60 · 43 · 39 |
| D1 | `curl … /radar` | `200` |
| D1 | MARKER `grep -c -F "HIS RULING · APPROVED 2026-10-10 R969" ".../OPS-HAND.md"` | `0` (before) |
| D1-M | MIGRATIONS: none | not run |

## Smoke

## CONTINUE
next: STEP-D2 (gate green at 20:28:12 EDT; D0, D1 done)

## DECISIONS
- ASK DESK: D0's porcelain carries `?? .claude/settings.json.bak` — an untracked file outside `docs/40 - DevDocs/`, in neither the ACCEPTED nor the REFUSED class (not staged, not under src/tests/ops/configs). Default taken: go on; it is untracked, the ff-merge does not touch it, and it was already present in this session's start snapshot. [20:28 EDT]

## RECORDS

(run in progress — next step under ## CONTINUE)
