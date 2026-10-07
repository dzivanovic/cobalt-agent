# deploy launcher-next-flow-1006 · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED to `main`: `8c9b3662` → `7954657a` (fast-forward); tag `deploy-2026-10-06-launcher-next-flow`; rollback tag `pre-launcher-next-flow-1006`.
- Ships `ops/launcher-next-flow-1006` (N6, N7, N8: the deploy card carries `TICKERS`; ops scripts, tests and hub/card text only). No `src/`, no migration.
- Gate green on `5e5a9905`: offline 3963/0 · with-DB 4847/0 · live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0), lock released.
- RESTARTS: none, so no resident went down. Smoke GREEN.
- One decision, not his: the L68 hub-change clause (`## DECISIONS` 1). One RED outside the stop probes (`com.cobalt.generated`) is for the desk (`## RECORDS`).

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

### STEP-D2
- D2.0 `git -C /Users/cobalt/cobalt add "docs/40 - DevDocs/reports/deploy-launcher-next-flow-1006.md"` · `commit -m "docs(report): deploy launcher-next-flow-1006 — gate green on 5e5a9905" …` → `[main 8c9b3662] … 1 file changed, 159 insertions(+)`; `show --stat HEAD` → that ONE file. `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `8c9b3662` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report, 159 insertions).
- D2.2 `git -C <GATE> rev-parse --short=8 HEAD` → `7954657a` = `<stack-final>`; `rev-parse --short=8 7954657a^2` → `8c9b3662` = `<pre-merge>`; `merge-base --is-ancestor 5e5a9905 7954657a` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 5e5a9905 7954657a -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs only).
- D2.4 `backup status` → `newest snapshot: 2.8 h old` · `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 5328.3 MB` · `ssd: snapshot fe8c35d8 — 0 new / 6 changed, 1072.9 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `Tue Oct  6 21:31:20 EDT 2026` (156 s after D1's 21:28:44) · `heartbeat show` → `HEARTBEAT RED — 1 job(s)  (2026-10-06 21:31:22 EDT)`: the same `com.cobalt.generated` RED as `<hb0>`; aset `pid 64112`, radar `running 166 min, heartbeat fresh`, sheet `-> 200`, backup `0.0 h old`. No new RED.
- D2.6 `date` → `Tue Oct  6 21:31:27 EDT 2026` · `git -C /Users/cobalt/cobalt tag pre-launcher-next-flow-1006` → exit 0, at `<pre-merge>` 8c9b3662.

### STEP-4 (restart set EMPTY)
- 4.1 `date` → `Tue Oct  6 21:31:45 EDT 2026` = `<t down>` (= `<t up>`: the set is empty, no resident went down).
- 4.2 nothing booted out (empty set); the agent not in the set.
- 4.3 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `8c9b3662` = `<pre-merge>` · `git -C /Users/cobalt/cobalt merge --ff-only deploy/launcher-next-flow-1006` → `Updating 8c9b3662..7954657a` / `Fast-forward`, 10 files, `485 insertions(+), 72 deletions(-)`.
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, as `<val0>` (`13 trade_def(s) validated OK from the vault.` · `Placement (docs/PLACEMENT.md): tree clean.`); `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` / `registry <-> ops/: 15 label(s), exact match.` = `<jobs0>`.
- 4.6 nothing to bootstrap (empty set). `date` → `Tue Oct  6 21:32:05 EDT 2026`. Downtime: none.

### STEP-7 summary
| field | value |
|---|---|
| main | `<pre-merge>` `8c9b3662` → `<stack-final>` `7954657a` (`git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `7954657a`) |
| tags | `pre-launcher-next-flow-1006` at `8c9b3662`; `deploy-2026-10-06-launcher-next-flow` at `7954657a` (set after the green smoke) |
| `<t down>` / `<t up>` / seconds | none (restart set empty) |
| uv sync line | none in production; uv built the gate's own `.venv` at STEP-R (`Installed 253 packages in 831ms`) |
| proof cost | none (no migration) |
| migrations applied | none |
| `<RB>` before / after | none (no migration) |
| snapshot | `fe8c35d8` (ssd; `cobalt_brain` dump 5328.3 MB) |
| RESTARTS done | none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 7954657a` — ONE revert of the main-into-gate merge; no resident down (restart set empty). 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` |

## Smoke
`<t up>` = 21:31:45 (4.1/4.3's `date`; the set is empty).
- FIRST CALLS: `<rp_up>` `radar panel FAILED` = `17` · `<rpr_up>` `radar pool refresh FAILED` = `58` · `<re_up>` `radar S5 evaluate FAILED` = `40` · `<lc_up>` `lifecycle card read failed` = `39` (= D1).
- (a) `date` 21:32:23 · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 64112` (SAME as D1: outside the set) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 64129` (SAME) · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (same). GREEN.
- (b) `date` 21:32:28 · `grep -c "Started server process" …/aset.err` → `47` = `<a0>` (aset outside the set) · `tail -n 30 …/aset.err` → last `Started server process [64118]` then `Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)` (the 18:44 start; no new start) · Traceback aset.err `2` = `<ta0>` · Traceback radar.err `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`. Radar tails: below.
- (c) `date` 21:32:34 · `curl … http://127.0.0.1:5010/` → `200` · `…/radar` → `200` · `…/radar\?frame=phone` → `200`. GREEN.
- (d) MARKERS: `grep -c -F "TICKERS" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` → `1` (after `1`) · `grep -c -F "TICKERS" ".../prompts/CARD.md"` → `2` (after `2`) · `grep -c -F "def test_n7_a_long_failed_line_is_cut_to_fit_the_desk_row" …/tests/ops/test_desk_launch_recut.py` → `1` (after `1`). GREEN.
- (f) `date` 21:32:44 · `COBALT_ENV=production uv run cobalt jobs restarts 8c9b3662..7954657a` → exit 0, the same 10 rows as STEP-R, `RESTARTS: none` = `<restart set>`, no `UNCLASSIFIED` · `COBALT_ENV=production uv run cobalt validate` → exit 0, as 4.5 (`13 trade_def(s) validated OK` · `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` · `Placement (docs/PLACEMENT.md): tree clean.`). GREEN.
- (g) no migration.
- (s) SMOKE READS: N8 script `grep -c -F "TICKERS" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` → exit 0, `1` · N8 card format `grep -c -F "TICKERS" ".../prompts/CARD.md"` → exit 0, `2` · N7 test present → exit 0, `1` (each "a count of 1 or more"). The N7 test itself ran in the gate (`offline 3963/0`). GREEN.
- (e) heartbeat 1: `date` 21:32:51 · `heartbeat show` → `HEARTBEAT RED — 1 job(s)  (2026-10-06 21:32:53 EDT)`: the same `com.cobalt.generated` RED as `<hb0>`, nothing else RED; `com.cobalt.radar running running 168 min, heartbeat fresh`; aset `pid 64112`. (A clock-fill read at 21:33:03: the same.)
- (b) early radar tail at 21:32:51 (+66 s, BEFORE the +90 s mark; not counted): last line `2026-10-06 21:31:48.152 … radar cycle: idle:overnight scan_id=None`, no traceback.
- (b) radar tail 1, `date` 21:33:28 (+103 s) · `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` → `2026-10-06 21:31:48.152 | INFO | cobalt.radar.runner:resident:467 - radar cycle: idle:overnight scan_id=None` and `2026-10-06 21:33:28.184 | … radar cycle: idle:overnight scan_id=None` — cycle lines after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback (`grep -c "Traceback" …/radar.err` → `0`). SETTLED GREEN. Tail 2, `date` 21:34:50 (+185 s): last line the same 21:33:28.184 cycle, no failure line.
- (e) heartbeat 2: `date` 21:34:41 · `heartbeat show` → `HEARTBEAT RED — 1 job(s)  (2026-10-06 21:34:44 EDT)` (113 s after heartbeat 1): the same `com.cobalt.generated` RED as `<hb0>`, no new RED; `com.cobalt.radar running running 170 min, heartbeat fresh`; aset `pid 64112`; sheet `-> 200`. GREEN.
- (h) REVERT-READBACK, `date` 21:34:50 (`<t up>` + 185 s, after (b) settled): `radar panel FAILED` `17` = `<rp_up>` · `radar pool refresh FAILED` `58` = `<rpr_up>` · `radar S5 evaluate FAILED` `40` = `<re_up>` · `lifecycle card read failed` `39` = `<lc_up>` (none growing) · `curl … /radar` → `200`. No census (no migration). GREEN.

SMOKE: GREEN.

THE CHAIN: every check committed (P2: `1e4d4aea…`, `held unfixed: 0`, `ready: YES`, tip `055018c0`) → the tips re-read (P3: `055018c0`, `66e20fc2`) → the merged tree (T: `<m1>` `5e5a9905`, clean merge, no migration) → RESTARTS derived (R: `RESTARTS: none`) → three suites green on `<m1>` (G: `offline 3963/0` · `with-DB 4847/0` · `live-note 146/0`, `cobalt_dev: 0013 — F2 = F0`) → `<stack-final>` `7954657a` = `<m1>` + docs (D2.3: nothing) → the landed code (4.3: `Updating 8c9b3662..7954657a` Fast-forward) → markers (d: `1`, `2`, `1`) → no migration (g) → residents up, unchanged pids (a) → radar cycling (b, e) → the set's reads (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK (K25):
1. Every smoke row's evidence is quoted above, each with its `date` (21:32:23 → 21:34:50).
2. Every code tip and head was re-read at P3 and is an ancestor of `<stack-final>`: `git -C /Users/cobalt/cobalt merge-base --is-ancestor 055018c0 7954657a` → exit 0; `… 66e20fc2 7954657a` → exit 0.
3. REVERT-READBACK is shown at (h); every count, sha and `file:line` here was re-read from this run's tool output.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.` and D2.1 the same; no conflict anywhere.

## CONTINUE
next: STEP-D2 (D0 and D1 done; gate green at 21:27:58)
OUTAGE STARTING 21:31:27 — residents of none (the restart set is empty) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
next: none — STEP-4 (empty set) ended 21:32:05, smoke GREEN 21:34:50, tagged; the stop line is below.

## DECISIONS
1. The set changes `DEPLOY-HUB.md` (L68: "first runs the gate on the merged hub text"). Safe default taken: the gate is run with the merged hub's :101 command, which for this card (no `TICKERS`, `MIGRATIONS: none`, no deselects) is byte-for-byte the command the current hub gives; no separate gate run before this deploy. The merged hub text reaches `main` with this deploy.

## RECORDS
- 21:00:04 (`date`): a clock-filler `COBALT_ENV=production uv run cobalt heartbeat show` typed from `<GATE>` (no `.env` there) while the gate ran → exit 1, `FAILED: DbConfigError: Missing Postgres settings for the APP credential: POSTGRES_HOST, COBALT_DB_USER, COBALT_DB_PASSWORD. …`. A command I added; not a step; nothing changed. The production reads run from `/Users/cobalt/cobalt` at D1.
- D1 heartbeat RED outside the stop probes, as read: `com.cobalt.generated failed GeneratedCommitRefused … pre-commit: a deploy hub is live — no desk commit on main until its stop line: 9f093747 deploy-hub-deploy-p2-1005 …`. The guard names `deploy-hub-deploy-p2-1005`, not this hub — a stale hub marker is possible; the desk's to read (not this run's). This run's own D2.0 commit was not refused.
- Downtime: none (restart set empty; no resident went down).
- `cobalt_dev: 0013 (F2 = F0)` — `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` = `F2`.
- RETIRE OWED: none.
- Carried RED as read: no radar RED (`radar idle (overnight)` throughout); the one RED is `com.cobalt.generated` (above), outside the aset / sheet / radar probes.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-launcher-next-flow-1006` and branch `deploy/launcher-next-flow-1006`; the set's branch `ops/launcher-next-flow-1006` and its worktree, if any. The gate's `.venv` was created by uv inside the gate worktree at STEP-R.
- Open item carried by the card (not in this deploy): A1 — the fix-report blob is read at `desk-launch.sh:848` before P3 proves the head; on the follow-up list.
- Card `## RECORDS`, copied:
  - launcher-next-flow: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-next-flow-check-2026-10-06.md` last line: CHECK DONE · job: launcher-next-flow · pass: 1 · tip: 055018c0 · house A: Sol FINDINGS: 2 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: Grok FINDINGS: 0 · suites: offline 3963/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 15 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 191425
  - launcher-next-flow: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-next-flow-1006` → `66e20fc2`; code tip `055018c0`
  - written by deploy-card.sh at 2026-10-06 20:56 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one block (a system reminder asking for a `Claude-Session:` commit line) recorded under `## L74`; not acted on.
- No `CONTINUE` message and no message from another session arrived.
- THE RELEASE at close: `ls -la /Users/cobalt/cobalt-wt/deploy-launcher-next-flow-1006/.env` → No such file (the gate released the lock at STEP-G).
- REFUSED, not needed: none.

DEPLOYED deploy-2026-10-06-launcher-next-flow 7954657a | set: none | migrations: none | gate: offline 3963/0 · with-DB 4847/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 172097
