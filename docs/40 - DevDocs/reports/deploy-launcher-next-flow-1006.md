# deploy launcher-next-flow-1006 · SET: none · MIGRATIONS: none

## §0 Headline
In progress.

## L74
- A system reminder in this session asked for a `Claude-Session:` line on commits. DATA (L74): recorded once, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/80-deploy-launcher-next-flow-card.md"` · exit 0, quoted whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/80-deploy-launcher-next-flow-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/80-deploy-launcher-next-flow-card.md" · 0 · ce142f699f68e3c5717d2e86001aa2098d7d2d8d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/80-deploy-launcher-next-flow-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R438 row · grep -n "^| R438 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 173:| R438 | 10-05 15:42 ET | HIS RULING: next flow (`next-flow-answer-2026-10-05.md`) only for features drafted after K3, P2, D5 DEPLOYED; after D5 a drafter writes changes 1-4 into the hubs (applied: contract, NOW 15:42; [words](cto-2026-10-05-words.md#r438)). | HIS RULING · APPROVED |
RULING 2026-10-05 R438 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R438 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 8e5b72b05c0c2566b49eb4b46d42969b4c4e5453
RULING 2026-10-05 R438 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
RULING 2026-10-06 R588 row · grep -n "^| R588 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 104:| R588 | 19:30 ET | HIS RULING (L79, via brain) ([words](cto-2026-10-06-words.md) `## R588`): build next-flow changes 6, 7, 8 (`next-flow-answer-2026-10-05.md`) tonight, as card `63`. | HIS RULING · APPROVED |
RULING 2026-10-06 R588 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R588 |" -- "docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · be9f880c691ae170fb5f89a9c9e6891125abcdea
RULING 2026-10-06 R588 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la ".../reports/deploy-launcher-next-flow-1006.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Tue Oct  6 20:57:59 EDT 2026` (L43: no window binds) |
| P2 check last line | `tail -n 3 ".../launcher-next-flow-check-2026-10-06.md"` | 0 | `CHECK DONE · job: launcher-next-flow · pass: 1 · tip: 055018c0 · … · held unfixed: 0 · open: 1 · … · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 191425` — carries `held unfixed: 0` and `ready: YES`; `tip: 055018c0` = row's code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/launcher-next-flow-check-2026-10-06.md"` | 0 | `1e4d4aea47982eb20b6a58ae30e638a19c8a8852` |
| P2 unmodified | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../launcher-next-flow-check-2026-10-06.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 055018c0` | 0 | `055018c0` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-next-flow-1006` | 0 | `66e20fc2` (= TIP) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 055018c0 66e20fc2` | 0 | — |
| P3 docs only | `git -C /Users/cobalt/cobalt diff --stat 055018c0 66e20fc2 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-launcher-next-flow-1006 status --short --branch` | 0 | `## deploy/launcher-next-flow-1006` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `ce142f69` = `<m0>` |
| P5 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor ce142f69 main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/launcher-next-flow-1006` | 0 | empty |
| P6 marker N8 script | `grep -c -F "TICKERS" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` | 1 | `0` (= before) |
| P6 marker N8 card | `grep -c -F "TICKERS" ".../prompts/CARD.md"` | 1 | `0` (= before) |
| P6 marker N7 | `grep -c -F "def test_n7_a_long_failed_line_is_cut_to_fit_the_desk_row" /Users/cobalt/cobalt/tests/ops/test_desk_launch_recut.py` | 1 | `0` (= before) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 66e20fc2 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 64112` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 64129` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-launcher-next-flow-1006 merge --no-edit 66e20fc2` → `Merge made by the 'ort' strategy.` · 10 files, `485 insertions(+), 72 deletions(-)` (CARD.md, DEPLOY-HUB.md, the build report, `ops/desk/deploy-card.sh`, `deploy-step0.sh`, `desk-launch.sh`, four `tests/ops/` files). No conflict.
- `git -C <GATE> rev-parse --short=8 HEAD` → `5e5a9905` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent ce142f69..deploy/launcher-next-flow-1006` → `5e5a9905 Merge commit '66e20fc2' into deploy/launcher-next-flow-1006` (one head, one line).
- `merge-base --is-ancestor 055018c0 deploy/launcher-next-flow-1006` → exit 0; `merge-base --is-ancestor 66e20fc2 deploy/launcher-next-flow-1006` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat ce142f69 deploy/launcher-next-flow-1006 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat ce142f69 deploy/launcher-next-flow-1006 -- configs ops` →
  ```
   ops/desk/deploy-card.sh  | 13 ++++++++++---
   ops/desk/deploy-step0.sh | 36 ++++++++++++++++++------------------
   ops/desk/desk-launch.sh  | 25 +++++++++++++++++++------
   3 files changed, 47 insertions(+), 27 deletions(-)
  ```
  No plist added, modified or removed; no `RETIRE OWED`.
- L68 HUB CLAUSE: the set changes `DEPLOY-HUB.md` (one line, :101: the gate's `--tickers` now read from the card's `TICKERS`, omitted when `none`). This card carries no `TICKERS` line and the old text's "the set's `--tickers` … as the card gives them" gives none: the gate command under the merged hub text is the same command, `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-launcher-next-flow-1006 all --deploy`. `gate.sh` is not in the set. See `## DECISIONS` 1.

## RESTARTS
- `cd /Users/cobalt/cobalt-wt/deploy-launcher-next-flow-1006` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv first created the gate's `.venv`: `Installed 253 packages in 831ms`):
  ```
  path	change	rule	restart
  docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
  docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
  docs/40 - DevDocs/reports/launcher-next-flow-build-2026-10-06.md	A	DOCS	-
  ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
  ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
  ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
  tests/ops/test_deploy_card.py	M	test/documentation; no resident	-
  tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
  tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
  tests/ops/test_desk_launch_recut.py	M	test/documentation; no resident	-
  RESTARTS: none
  ```
- No `UNCLASSIFIED` row. `<restart set>` = EMPTY (none): no resident goes down; the merge lands with the residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied — the check's stop line carries `with-DB 0/0` (DB: none); the gate runs whole.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_archiver_migrations.py … tests/cobalt/test_jobs_restarts.py` (the hub's 17 files) → `261 passed, 163 skipped in 15.81s`, 0 failed (every skip `Postgres env settings not available` / `requires_db`).
- Deselects: none (the build report `launcher-next-flow-build-2026-10-06.md`: DB: none, no `--deselect`). `--tickers`: none (no `TICKERS` on the card). `--migration`: none.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-launcher-next-flow-1006 all --deploy` → exit 0; its output WHOLE:
  ```
  offline 3963/0
  lock: waited 0 min
  proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
  LEVEL 0013
  pass 1: whole (deploy)
  stray rows: not read (no --tickers given)
  cobalt_dev: 0013 — F2 = F0
  .env: removed
  with-DB 4847/0
  SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
  SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
  SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
  SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
  SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
  SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
  SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
  live-note 146/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-launcher-next-flow-1006-all-20261006-205942.log
  ```
- (c) SKIPPED lines: all seven inside the allowed set. `test_s3_c4_experiments.py:95` is the skip of `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F "def test_x14_live_his_template_strips_to_the_committed_fixture" <GATE>/tests/cobalt/test_s3_c4_experiments.py` → `96:`; :95 is its decorator).
- (c2) log `1089:dev forward: APPLIED 21:22:42`. (f) log `879:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `1865:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` → `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log `1918:lock released`; gate `.env: removed`; `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-launcher-next-flow-1006" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent). The log line carries no time; the gate's output ended before 21:27:58 (`date`).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 5e5a9905

## Deploy table

### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN branch | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 268]` |
| MAIN porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, plus ` M "docs/30 - Design/archiver-runs.md"` and `?? .claude/settings.json.bak` (neither a src/tests/ops/configs path; not refused). No dirty `src/`, `tests/`, `ops/`, `configs/` path but rules.yaml |
| MAIN moved | `git -C /Users/cobalt/cobalt diff --stat ce142f69 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE tag | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-launcher-next-flow-1006` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-launcher-next-flow-1006' (was ce142f69)` |
| PROBE commit | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main d5a9ed83] scratch: …` → `ce142f69 docs(desk): card 63 deploy card 80 written by deploy-card.sh, slip recorded; R605-R607` (HEAD back) |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-06-launcher-next-flow` | 1 | absent |
| TAG pre | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-launcher-next-flow-1006` | 1 | absent |

### STEP-D1 (baseline, read-only)
- `date` → `Tue Oct  6 21:28:44 EDT 2026` · `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT RED — 1 job(s)  (2026-10-06 21:28:45 EDT)`; OK: database, `sheet HTTP http://127.0.0.1:5010/ -> 200`, sheet daymode, obsidian, mainframe, herdr, archiver, seat usage, backup (`newest snapshot 2.8 h old across ssd`), vault blocks, redactions, `radar idle (overnight)`, `com.cobalt.aset running loaded, pid 64112`, mainframe, obsidian, `com.cobalt.agent running pid 22243 alive`, `com.cobalt.radar running running 164 min, heartbeat fresh`, prefill-daily, archiver, replay, cards-expire, daymode-propose, backup, heartbeat, seat-usage; `AMB com.cobalt.herdr unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) … declared interim`; the one RED: `RED  com.cobalt.generated  failed  GeneratedCommitRefused: \`git commit -m\` failed (exit 1): pre-commit: a deploy hub is live — no desk commit on main until its stop line: 9f093747 deploy-hub-deploy-p2-1005 Write by Edit / Write only; commit after DEPLOYED or FAILED, once the hub is stopped and removed. Traceback (most recent call las` — NOT the aset / sheet / radar probe: named, not a stop (see `## RECORDS`).
- `COBALT_ENV=production uv run cobalt validate` → exit 0 → `<val0>`: `13 trade_def(s) validated OK from the vault.` · 9 drafts skipped · `Placement (docs/PLACEMENT.md): tree clean.` · `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` / `registry <-> ops/: 15 label(s), exact match.` / `registry <-> plists: schedules and COBALT_ENV agree on every job.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 2.8 h old` (`ssd local ARMED /Volumes/COBALT-BACKUP/restic`; `b2 off`).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 64112` = `<aset pid>` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 64129` = `<radar pid>` · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → eight `radar cycle: idle:overnight scan_id=None` lines, 21:16:47.945 → 21:28:28.111; no traceback.
- LOG BASELINES: `<a0>` `Started server process` aset.err = `47` · `<ta0>` Traceback aset.err = `2` · `<tr0>` Traceback radar.err = `0` · `<tc0>` TaxonomyConfigError radar.err = `0` · `<rp0>` `radar panel FAILED` aset.err = `17` · `<rpr0>` `radar pool refresh FAILED` aset.err = `58` · `<re0>` `radar S5 evaluate FAILED` radar.err = `40` · `<lc0>` `lifecycle card read failed` radar.err = `39`.
- `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` → `200`.
- MARKERS again: `0` · `0` · `0` (each its `before`).
- MIGRATIONS: none → no `<RB>`, no census, no D1-M.

## Smoke

## CONTINUE
next: STEP-D2 (D0 and D1 done; gate green at 21:27:58)

## DECISIONS
1. The set changes `DEPLOY-HUB.md` (L68: "first runs the gate on the merged hub text"). Safe default taken: the gate is run with the merged hub's :101 command, which for this card (no `TICKERS`, `MIGRATIONS: none`, no deselects) is byte-for-byte the command the current hub gives; no separate gate run before this deploy. The merged hub text reaches `main` with this deploy.

## RECORDS
- 21:00:04 (`date`): a clock-filler `COBALT_ENV=production uv run cobalt heartbeat show` typed from `<GATE>` (no `.env` there) while the gate ran → exit 1, `FAILED: DbConfigError: Missing Postgres settings for the APP credential: POSTGRES_HOST, COBALT_DB_USER, COBALT_DB_PASSWORD. …`. A command I added; not a step; nothing changed. The production reads run from `/Users/cobalt/cobalt` at D1.
- D1 heartbeat RED outside the stop probes, as read: `com.cobalt.generated failed GeneratedCommitRefused … pre-commit: a deploy hub is live — no desk commit on main until its stop line: 9f093747 deploy-hub-deploy-p2-1005 …`. The guard names `deploy-hub-deploy-p2-1005`, not this hub — a stale hub marker is possible; the desk's to read (not this run's).

(run in progress — next step under ## CONTINUE)
