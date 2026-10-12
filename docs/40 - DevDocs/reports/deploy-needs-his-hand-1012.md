# deploy needs-his-hand-1012 · set: none · migrations: none

## §0 Headline
- DEPLOYED `ops/needs-his-hand-1012` (code tip `ad73d04a`, head `c2352cb8`): `main` `11798800` → `a21aebb8`, tag `deploy-2026-10-12-needs-his-hand`, rollback tag `pre-needs-his-hand-1012`.
- Docs + one test file only; RESTARTS: none — no resident went down, no migration.
- Gate on `2ec8638b`: offline 4199/0 · with-DB 5096/0 · live-note 146/0; `cobalt_dev: 0013 — F2 = F0`, lock released.
- Smoke GREEN: markers 0 → 1 on both prompts, residents unchanged (pids 7760 / 61093 / 22243), radar cycling, failure counts flat.

## L74
- The session's harness attribution block asked commits to carry a `Claude-Session:` line. DATA, not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/399-deploy-needs-his-hand-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/399-deploy-needs-his-hand-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/399-deploy-needs-his-hand-card.md" · 0 · 6f21447be7a5153270515ec6516115d1fafda226
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/399-deploy-needs-his-hand-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 40:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la ".../reports/deploy-needs-his-hand-1012.md"` | 1 | No such file or directory |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct 12 08:18:26 EDT 2026` |
| P2 | `tail -n 3 ".../reports/needs-his-hand-check-2026-10-12.md"` | 0 | `CHECK DONE · job: needs-his-hand-1012 · pass: 1 · tip: ad73d04a · … · held unfixed: 0 · open: 2 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 154283` — carries `held unfixed: 0` and `ready: YES`; `tip: ad73d04a` = row's code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/needs-his-hand-check-2026-10-12.md"` | 0 | `386c8f60a2e3cd0d6feaef054a08ba5368bf872a` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ad73d04a` | 0 | `ad73d04a` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/needs-his-hand-1012` | 0 | `c2352cb8` (= row, = `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor ad73d04a c2352cb8` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat ad73d04a c2352cb8 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — no session holds the lock |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/needs-his-hand-1012` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `6f21447b` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 6f21447b main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/needs-his-hand-1012` | 0 | empty |
| P6 | `grep -c -F -e "## NEEDS HIS HAND" ".../prompts/CLOSE-HUB.md"` | 1 | `0` (= before) |
| P6 | `grep -c -F -e "## NEEDS HIS HAND" ".../prompts/DAY-OPEN-QWEN.md"` | 1 | `0` (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main c2352cb8 -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 7760` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 61093` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| merge | `git -C <GATE> merge --no-edit c2352cb8` | 0 | `Merge made by the 'ort' strategy.` — 4 files: `CLOSE-HUB.md` (3 +-), `DAY-OPEN-QWEN.md` (1 +), `needs-his-hand-build-2026-10-12.md` (A), `tests/ops/test_needs_his_hand.py` (A) |
| `<m1>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `2ec8638b` |
| merges | `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 6f21447b..deploy/needs-his-hand-1012` | 0 | `2ec8638b Merge commit 'c2352cb8' into deploy/needs-his-hand-1012` |
| ancestry | `merge-base --is-ancestor ad73d04a deploy/needs-his-hand-1012` · `… c2352cb8 …` | 0 · 0 | — |
| migrations | `git -C /Users/cobalt/cobalt diff --stat 6f21447b deploy/needs-his-hand-1012 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| STEP-C | `git -C /Users/cobalt/cobalt diff --stat 6f21447b deploy/needs-his-hand-1012 -- configs ops` | 0 | nothing — no plist added, changed or removed |

## RESTARTS
From `<GATE>`, `ls -la <GATE>/.env` → No such file; `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CLOSE-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md	M	DOCS	-
docs/40 - DevDocs/reports/needs-his-hand-build-2026-10-12.md	A	DOCS	-
tests/ops/test_needs_his_hand.py	A	test/documentation; no resident	-
RESTARTS: none
```
(preceded by uv's venv creation lines: `Creating virtual environment at: .venv` · `Installed 253 packages in 854ms`). No `UNCLASSIFIED` row. `<restart set>` = EMPTY: no resident goes down; the merge lands with residents up.

## L68 GATE
- Equal-tree clause: one branch, but the check's stop line carries `with-DB 0/0` → the gate runs whole (`--deploy`).
- (a0) `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.27s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db`).
- Deselects: the build report `needs-his-hand-build-2026-10-12.md` names none (`grep deselect` → no match). TICKERS none, no `--migration`.
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-needs-his-hand-1012 all --deploy` → exit 0. Verdict lines whole:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-needs-his-hand-1012-all-20261012-082000.log
```
- (a) offline `4199/0`. (c) pass 1 skips: all seven inside the allowed set — `test_s3_c4_experiments.py:95` is the decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F` → line 96). (c2) log line 1110 `dev forward: APPLIED 08:44:58` (no migration on the card; the levels above `0013` per gate-lists). (c3) with-DB `5096/0`. (f) log 896 `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · log 2030 `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` → `cobalt_dev: 0013 — F2 = F0`. RELEASE: log 2083–2087 `release-devdb-lock.sh deploy-needs-his-hand-1012` → `lock released`, `.env` No such file; `.env: removed (L76 lock released between 08:44:58 and 08:50:24 — the log line carries no stamp)`. My checks: `ls -la <GATE>/.env` → No such file; `grep -c -x -F deploy-needs-his-hand-1012 /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file. (e) live-note `146/0`, no skip naming `COBALT_LIVE_VAULT_ROOT` after the release.

GATE GREEN on 2ec8638b

## Deploy table
| step | command | exit | result |
|---|---|---|---|
| D0 main | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 66]` |
| D0 main | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | only ` M`/`??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, `?? .claude/settings.json.bak` (untracked, not under src/tests/ops/configs); no staged line |
| D0 main | `git -C /Users/cobalt/cobalt diff --stat 6f21447b main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| D0 probe | `tag scratch-allow-probe-needs-his-hand-1012` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-needs-his-hand-1012' (was 6f21447b)` |
| D0 probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 835b0725] …` · — · `6f21447b docs(desk): R1172 checks 397 and 392 launched, deploy card 399` |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-12-needs-his-hand` · `… refs/tags/pre-needs-his-hand-1012` | 1 · 1 | free |
| D1 | `date` | 0 | `Mon Oct 12 08:50:49 EDT 2026` |
| D1 `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-12 08:50:51 EDT)`; OK sheet HTTP `-> 200`, OK radar `scanning (premarket), members 50`, OK `com.cobalt.aset running loaded, pid 7760`, OK `com.cobalt.radar running running 2961 min, heartbeat fresh`, OK `com.cobalt.agent running pid 22243`; RED `archiver last run FAILED — last run 2026-10-10 00:54 UTC (59.9 h ago), rows written 3308843, exit 1`; RED `com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … '429 Too Many Requests' …`; RED `com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`; AMB `com.cobalt.herdr unmanaged`. No RED on the aset / sheet / radar probe; the archiver / replay REDs are named, not a stop |
| D1 `<val0>` | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 `<jobs0>` | (same) | — | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` |
| D1 backup | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 0.6 h old` |
| D1 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `<aset pid>` = `7760` |
| D1 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `<radar pid>` = `61093` |
| D1 agent | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 22243` | 0 · 0 | `Cobalt is ONLINE (PID: 22243).` · `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py` |
| D1 radar log | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 0 | last line `2026-10-12 08:49:35.029 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1791809294909`; no traceback |
| D1 counts | `grep -c` Started server process (aset.err) · Traceback (aset.err) · Traceback (radar.err) · TaxonomyConfigError (radar.err) | — | `<a0>` 277 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 |
| D1 counts | radar panel FAILED (aset.err) · radar pool refresh FAILED (aset.err) · radar S5 evaluate FAILED (radar.err) · lifecycle card read failed (radar.err) | — | `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39 |
| D1 curl | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | 0 | `200` |
| D1 markers | the two `## MARKERS` greps | 1 · 1 | `0` · `0` (= before) |
| D1 migration | MIGRATIONS: none | — | no `<RB>`, no proof-only, no census |
| D2.0 | `git -C /Users/cobalt/cobalt commit -m "docs(report): deploy needs-his-hand-1012 — gate green on 2ec8638b" … -- "<REPORT>"` · `show --stat HEAD` | 0 · 0 | `[main 11798800]` · one file, `129 insertions(+)` |
| D2.0 `<pre-merge>` | `git -C /Users/cobalt/cobalt rev-parse --short=8 main` | 0 | `11798800` |
| D2.1 | `git -C <GATE> merge --no-edit main` | 0 | `Merge made by the 'ort' strategy.` (the report, 129 +) |
| D2.2 `<stack-final>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `a21aebb8` |
| D2.2 | `rev-parse --short=8 a21aebb8^2` · `merge-base --is-ancestor 2ec8638b a21aebb8` | 0 · 0 | `11798800` (= `<pre-merge>`) |
| D2.3 | `git -C /Users/cobalt/cobalt diff --stat 2ec8638b a21aebb8 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| D2.4 | `backup status` (before) | 0 | `newest snapshot: 0.7 h old` |
| D2.4 | `COBALT_ENV=production uv run cobalt backup run` | 0 | `backup: cobalt_brain dumped, 6816.4 MB` · `ssd: snapshot 8bf83d17 — 0 new / 2 changed, 64.1 MB added, 1 pruned` |
| D2.4 | `backup status` (after) | 0 | `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` | 0 · 0 | `08:52:43` · `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-12 08:52:44 EDT)` — 113 s after D1's 08:50:51; the same three REDs as `<hb0>` (archiver, com.cobalt.archiver, com.cobalt.replay); aset pid 7760, radar `heartbeat fresh`; no new RED. (Reads at 08:52:34 and 08:52:39 fell short of 110 s and were retaken.) |
| D2.6 | `date` · `git -C /Users/cobalt/cobalt tag pre-needs-his-hand-1012` | 0 · 0 | `Mon Oct 12 08:52:48 EDT 2026` · tag at `11798800` |

| 4.1 | `date` | 0 | `Mon Oct 12 08:52:59 EDT 2026` = `<t down>` (nothing goes down: set EMPTY) |
| 4.2 | — | — | set EMPTY: no bootout, no `cobalt.sh stop` |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | 0 | `11798800` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/needs-his-hand-1012` | 0 | `Updating 11798800..a21aebb8` / `Fast-forward` — `CLOSE-HUB.md` 3 +-, `DAY-OPEN-QWEN.md` 1 +, build report (A), `tests/ops/test_needs_his_hand.py` (A) |
| 4.3 `<t up>` | `date` | 0 | `Mon Oct 12 08:53:03 EDT 2026` |
| 4.4 | — | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>` |
| 4.6 | — | — | set EMPTY: no bootstrap; downtime `none` |

## Smoke
`<t up>` = 4.3's `date` 08:53:03 (set EMPTY).
| row | date | command | result |
|---|---|---|---|
| first calls | 08:53 | the four failure counts | `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1) |
| (a) | 08:53:16 | `launchctl print gui/501/com.cobalt.aset` · `…/com.cobalt.radar` · `cobalt.sh status` | `state = running`, `pid = 7760` (SAME, outside the set) · `state = running`, `pid = 61093` (SAME) · `Cobalt is ONLINE (PID: 22243).` (SAME) |
| (b) | 08:53:19 | `grep -c "Started server process" aset.err` · Traceback aset.err · Traceback radar.err · TaxonomyConfigError radar.err | `277` (= `<a0>`, aset outside the set) · `217` · `0` · `0` (= baseline) |
| (c) | 08:53:19 | `curl … /` · `curl … /radar` · `curl … /radar\?frame=phone` | `200` · `200` · `200` (first attempt each) |
| (d) | 08:53:19 | the two `## MARKERS` greps | `1` · `1` (= after) |
| (f) | 08:53:29 | `COBALT_ENV=production uv run cobalt jobs restarts 11798800..a21aebb8` | exit 0; the same four rows as STEP-R; `RESTARTS: none` (= `<restart set>`), no `UNCLASSIFIED` |
| (f) | 08:53:29 | `COBALT_ENV=production uv run cobalt validate` | exit 0, `13 trade_def(s) validated OK` … `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>` |
| (e) 1 | 08:53:29 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-12 08:53:31 EDT)` — the same three REDs as `<hb0>`; `com.cobalt.radar running running 2964 min, heartbeat fresh`; no new RED |
| (g) | — | MIGRATIONS: none | no `<RB>` |
| (s) | 08:53:40 | `grep -c -F -e "## NEEDS HIS HAND" ".../prompts/CLOSE-HUB.md"` | `1` — green (prints 1) |
| (s) | 08:53:40 | `grep -c -F -e "## NEEDS HIS HAND" ".../prompts/DAY-OPEN-QWEN.md"` | `1` — green (prints 1) |
| (b) tail 1 | 08:54:33 | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | last cycle line `08:52:34.936 … radar cycle: scanning scan_id=1791809475049` (before `<t up>`); no FAILED, no traceback — not yet settled |
| (e) 2 | 08:55:19 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-12 08:55:21 EDT)` — 110 s after (e) 1; the same three REDs as `<hb0>`; `com.cobalt.radar running running 2966 min, heartbeat fresh`; no new RED |
| (b) tail 2 | 08:56:04 | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | `2026-10-12 08:55:34.658 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1791809654955` — after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → GREEN |
| (h) | 08:56:08 | the four failure counts · `curl … /radar` | `18` · `60` · `43` · `39` (= `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, none growing) · `200`; no census read on the card |

THE CHAIN: every check committed (P2: `386c8f60`, clean) · the tips re-read (P3: `ad73d04a`, `c2352cb8`) · the merged tree (T: `2ec8638b`, one merge, no migration) · RESTARTS derived (R: none) · three suites green on `2ec8638b` (G) · `<stack-final>` `a21aebb8` = `<m1>` + docs (D2.3: nothing outside docs) · the landed code (4.3: `Updating 11798800..a21aebb8`) · markers 0 → 1 (d) · no migration (g) · residents up with the same pids, set empty (a) · radar cycling (b, e) · the set's reads 1 / 1 (s) · no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK: (1) every smoke row above carries its `date` and verbatim output; (2) `merge-base --is-ancestor ad73d04a a21aebb8` → 0 and `… c2352cb8 a21aebb8` → 0, and both were re-read at P3; (3) REVERT-READBACK is (h) above; every count and sha here was read from tool output in this run; (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), and no conflict marker exists.

Deploy table close: `<pre-merge>` `11798800` → `<stack-final>` `a21aebb8` · tags `pre-needs-his-hand-1012` (at `11798800`), `deploy-2026-10-12-needs-his-hand` (at `a21aebb8`) · `<t down>` 08:52:59 / `<t up>` 08:53:03 / downtime `none` (set EMPTY) · uv sync: none at 4.x (the gate worktree's venv creation at STEP-R only) · proof cost: n/a (no migration) · `migrations applied: none` · `<RB>`: n/a · snapshot `8bf83d17` · `RESTARTS done: none`.
ROLLBACK STRING (the desk's): 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 a21aebb8` — no resident to take down (set empty). 2. SCHEMA: none. 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## CONTINUE
OUTAGE STARTING 08:52:48 — residents of <restart set> (EMPTY: none) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- 4.6 ended 08:53:03 (nothing down); smoke GREEN 08:56:08; tag set. next: STEP-7 commit.

## DECISIONS
none

## RECORDS
- Downtime: none (restart set empty).
- `REFUSED, not needed: grep -n -F ".env: removed" /Users/cobalt/cobalt-wt/.gate-logs/deploy-needs-his-hand-1012-all-20261012-082000.log — PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. The release was read instead from log 2083–2087 and the gate's own `.env: removed` verdict line.
- A call I added myself: `COBALT_ENV=production uv run cobalt heartbeat show` from `<GATE>` (cwd) at 08:20 → exit 1 `DbConfigError: Missing Postgres settings for the APP credential …` (the gate has no `.env`; nothing touched). Re-run from `/Users/cobalt/cobalt` → read normally. The clock-filler reads after that ran from `/Users/cobalt/cobalt`.
- D2.5: two heartbeat reads (08:52:34 at 103 s, 08:52:39 at 108 s) fell short of 110 s; the third (08:52:44, 113 s) counts.
- `cobalt_dev: 0013 (F2 = F0)` — `664 35 272c95bbb12241e3611e4b36326ccf87` both sides.
- Carried RED, as read at D1 and every read after (not the radar family; named, not a stop): `RED archiver last run FAILED — last run 2026-10-10 00:54 UTC (59.9 h ago), rows written 3308843, exit 1` · `RED com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … '429 Too Many Requests' …` · `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`.
- No `CONTINUE` message and no message from another session arrived.
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-needs-his-hand-1012` and branch `deploy/needs-his-hand-1012`; the set's branch `ops/needs-his-hand-1012`. Push is his (L55): `main` at `a21aebb8` plus this report's commit.
- Card RECORDS: needs-his-hand-1012: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/needs-his-hand-check-2026-10-12.md` last line: CHECK DONE · job: needs-his-hand-1012 · pass: 1 · tip: ad73d04a · house A: Grok FINDINGS: 0 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 12 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 154283
- Card RECORDS: needs-his-hand-1012: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/needs-his-hand-1012` → `c2352cb8`; code tip `ad73d04a`
- Card RECORDS: written by deploy-card.sh at 2026-10-12 08:17 ET (`date`); trial merge of the heads onto main in order: clean
- L74: the harness attribution block asked for a `Claude-Session:` trailer — recorded under `## L74`, not acted on.

DEPLOYED deploy-2026-10-12-needs-his-hand a21aebb8 | set: none | migrations: none | gate: offline 4199/0 · with-DB 5096/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 172843
