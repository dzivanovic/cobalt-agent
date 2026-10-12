# deploy launcher-shadow-check-1011 — set: none · migrations: none

## §0 Headline
- DEPLOYED at 10:12 ET: `ops/launcher-shadow-check-1011` (code tip `66c4fefc`, head `ef754d0b`) is on `main` at `1966c239`, tag `deploy-2026-10-12-launcher-shadow-check`.
- The gate ran green on `c09a532f`: offline 4199/0 · with-DB 5096/0 · live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0).
- RESTARTS: none, so no resident went down. Smoke GREEN: both markers 0 → 1, radar cycled at 10:13:54, and no failure count grew.
- The check's one held finding (G3) passed P2 as FIXED in the fix round. No decision is open.

## L74
- A system notice in this session asked that commits end with a `Claude-Session:` line. Recorded as data (L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/401-deploy-launcher-shadow-check-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/401-deploy-launcher-shadow-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/401-deploy-launcher-shadow-check-card.md" · 0 · 012e38aa46a5acffd69c1e150eeb901ee44bba16
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/401-deploy-launcher-shadow-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 49:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | `ls -la "<REPORT>"` (first launch) | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct 12 09:38:02 EDT 2026` |
| P2 | `tail -n 3 ".../launcher-shadow-check-check-2026-10-11.md"` | 0 | last line: `CHECK DONE · job: launcher-shadow-check-1011 · pass: 1 · tip: a8c18242 · house A: Grok FINDINGS: 5 · findings: 6 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none (not needed) · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 3 · for Dejan: 0 · tokens: 236094` — carries `held unfixed: 1` and `ready: NO` (the row's literals) |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/launcher-shadow-check-check-2026-10-11.md"` | 0 | `86b9daa537c060633ba2a771fdc835adf40d9670` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<check report>"` | 0 | nothing |
| P2 fix-round | `git -C /Users/cobalt/cobalt merge-base --is-ancestor a8c18242 66c4fefc` | 0 | check tip is an ancestor of the code tip |
| P2 fix-round | `git -C /Users/cobalt/cobalt log -1 --format=%H ef754d0b -- "docs/40 - DevDocs/reports/launcher-shadow-check-build-2026-10-11.md"` | 0 | `ef754d0bf7f000f57bcc39317b75852bbbc7da90` (the fix report lives on the branch; `log -1` on `main` → empty, `diff --stat` → nothing) |
| P2 fix-round | `git -C /Users/cobalt/cobalt show "ef754d0b:<fix report>"` | 0 | last non-blank line `BUILT · job: launcher-shadow-check-1011 · tip: 66c4fefc | on a76d8855 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 10 of 10 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 115749`; holds `FIXED: G3 — tests/ops/test_check_hub_shadow.py::test_build_report_case_count_matches_collection` |
| P2 fix-round | Grep `HELD, NOT FIXED` in the check report | 0 | one held id: G3 (`:173`, `:199`, `:209`, `:229`) |
| P2 fix-round | `git -C /Users/cobalt/cobalt show 66c4fefc:tests/ops/test_check_hub_shadow.py` | 0 | `def test_build_report_case_count_matches_collection():` present, no xfail marker |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 66c4fefc` | 0 | `66c4fefc` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-shadow-check-1011` | 0 | `ef754d0b` = TIP |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 66c4fefc ef754d0b` | 0 | ancestor |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 66c4fefc ef754d0b -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — no holder |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/launcher-shadow-check-1011` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `012e38aa` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 012e38aa main` | 0 | ancestor |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/launcher-shadow-check-1011` | 0 | empty |
| P6 | marker 1 `grep -c -F -e "On a shadow card the check counts and holds findings exactly as on any card" ".../CHECK-HUB.md"` | 1 | `0` = before |
| P6 | marker 2 `grep -c -F -e "SHADOW BUILT · job:" "/Users/cobalt/cobalt/ops/desk/preflight.sh"` | 1 | `0` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main ef754d0b -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 7760` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 61093` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit ef754d0b` → `Merge made by the 'ort' strategy.` (12 files, 768 insertions, 13 deletions; auto-merged CHECK-HUB.md, desk-launch.sh, test_desk_launch_prechecks.py with no conflict).
- `<m1>` = `c09a532f`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 012e38aa..deploy/launcher-shadow-check-1011` → `c09a532f Merge commit 'ef754d0b' into deploy/launcher-shadow-check-1011` (one line, one head).
- `merge-base --is-ancestor 66c4fefc deploy/launcher-shadow-check-1011` → exit 0; `… ef754d0b …` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 012e38aa deploy/launcher-shadow-check-1011 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 012e38aa deploy/launcher-shadow-check-1011 -- configs ops` →
```
 ops/desk/card-fill.sh   | 11 +++++++++--
 ops/desk/desk-done.sh   | 14 ++++++++------
 ops/desk/desk-launch.sh | 26 ++++++++++++++++++++++----
 ops/desk/preflight.sh   | 25 +++++++++++++++++++++++++
 4 files changed, 64 insertions(+), 12 deletions(-)
```
  No plist added, modified or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created `.venv` in the gate: `Installed 253 packages in 966ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/launcher-shadow-check-build-2026-10-11.md	A	DOCS	-
ops/desk/card-fill.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-done.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/preflight.sh	M	operator script; no Cobalt reader	-
tests/ops/test_card_fill.py	M	test/documentation; no resident	-
tests/ops/test_check_hub_shadow.py	A	test/documentation; no resident	-
tests/ops/test_desk_done.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
tests/ops/test_house_probe.py	M	test/documentation; no resident	-
tests/ops/test_preflight.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = none (EMPTY): no resident goes down; the merge lands with the residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied — one branch in TIP, but the check's stop line carries `with-DB 0/0` (a DB: none branch runs the gate whole).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.15s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-launcher-shadow-check-1011 all --deploy` (no `--deselect`: the build was DB: none; no `--tickers`: TICKERS none; no `--migration`: MIGRATIONS none) → exit 0. Verdict lines WHOLE:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-launcher-shadow-check-1011-all-20261012-094007.log
```
- (a) offline `4199/0`. (c) every SKIPPED line inside the allowed set: `test_s3_c4_experiments.py:95` is the decorator of `:96 def test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F` at the gate). (c2) no migration above `0013` (MIGRATIONS none, no `--migration`). (c3) with-DB `5096/0`.
- (f) `cobalt_dev: 0013 — F2 = F0`: log `:896 F0: 664 35 272c95bbb12241e3611e4b36326ccf87`, `:2030 F2: 664 35 272c95bbb12241e3611e4b36326ccf87`.
- THE RELEASE: log `:2083 $ sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh deploy-launcher-shadow-check-1011` · `:2084 lock released` · `:2088 .env: removed` (L76 lock released; the log line carries no clock — the gate ran 09:40–10:09 ET). `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-launcher-shadow-check-1011" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (exit 2): lock dir absent.
- (e) live-note `146/0`: log `:2152` the one skip `COBALT_TEST_LIVE_DRC` (allowed), `:2153 146 passed, 1 skipped`; no skip names `COBALT_LIVE_VAULT_ROOT`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on c09a532f

## Deploy table
### STEP-D0
- `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 87]`. `status --porcelain` → ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M` / `??` under `docs/40 - DevDocs/` (cto-2026-10-08, cto-2026-10-12, harness-mods-review, house-seat-order-preflight2, lock-relief-decisions, next-flow-answer, seat-usage; the untracked reports and plans listed in the session's git status; this report), and `?? .claude/settings.json.bak`. No staged line; no dirty `src/`, `tests/`, `ops/` or `configs/` path beyond the accepted `rules.yaml`.
- `git -C /Users/cobalt/cobalt diff --stat 012e38aa main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-launcher-shadow-check-1011` → ok; `tag -d …` → `Deleted tag 'scratch-allow-probe-launcher-shadow-check-1011' (was 012e38aa)`; `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 26b3c146] scratch: allowlist probe (reverted next line)`; `reset --soft HEAD~1` → ok; `log --oneline -1` → `012e38aa docs(desk): R1181 deploy cards 401 and 402` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-12-launcher-shadow-check` → exit 1; `… refs/tags/pre-launcher-shadow-check-1011` → exit 1.

### STEP-D1 (baseline, 10:09:58 ET)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s) and 2 probe(s)  (2026-10-12 10:09:59 EDT)`. REDs, named (not aset / sheet; radar inside the carried family):
  - `RED  archiver                 last run FAILED — last run 2026-10-10 00:54 UTC (61.3 h ago), rows written 3308843, exit 1`
  - `RED  radar                    failed_stage bars: poll failures: 1` — CARRIED FAMILY: `com.cobalt.radar running 3040 min, heartbeat fresh`; radar.err `10:07:52.655 … radar cycle: scanning scan_id=1791813991678` (inside 5 min), no traceback in the tail.
  - `RED  com.cobalt.archiver          failed    RuntimeError: 18 archiver failure(s): DKNG/i2: Fetch failed for DKNG/i2: Finviz HTTP failed: Client error '429 Too Many Requests' …`
  - `RED  com.cobalt.replay            failed    ReplayError: archiver not done: state 'failed'`
  - OK: database, sheet HTTP (`http://127.0.0.1:5010/ -> 200`), sheet daymode, obsidian, mainframe, herdr, seat usage, backup, vault blocks, redactions, aset (`pid 7760`), mainframe, obsidian, agent (`pid 22243`), radar; AMB herdr (declared interim).
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, `13 trade_def(s) validated OK from the vault.`, `Placement (docs/PLACEMENT.md): tree clean.` `<jobs0>`: `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 0.6 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = `7760`; `… com.cobalt.radar` → `state = running`, `<radar pid>` = `61093`; `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ??         0:00.04 uv run src/cobalt_agent/main.py`.
- LOG BASELINES: `<a0>` = 277 · `<ta0>` = 217 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 18 · `<rpr0>` = 60 · `<re0>` = 43 · `<lc0>` = 39.
- `curl … /radar` → `200`. MARKERS again: `0`, `0` (before).
- No migration: `<RB>`, census and D1-M not run.

### STEP-D2
- D2.0 `git -C /Users/cobalt/cobalt add "<REPORT>"` · `commit -m "docs(report): deploy launcher-shadow-check-1011 — gate green on c09a532f" …` → `[main 96e163ee] … 1 file changed, 158 insertions(+)`; `show --stat HEAD` lists that one file. `<pre-merge>` = `96e163ee`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `1966c239`; `rev-parse --short=8 1966c239^2` → `96e163ee` = `<pre-merge>`; `merge-base --is-ancestor c09a532f 1966c239` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat c09a532f 1966c239 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 0.7 h old`; `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 6858.8 MB` · `ssd: snapshot b8e63b49 — 11 new / 2 changed, 133.9 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` 10:11:43 → heartbeat at 105 s; a second pair `date` 10:11:49 → `HEARTBEAT RED — 2 job(s) and 2 probe(s)  (2026-10-12 10:11:50 EDT)` at 111 s after D1: the same REDs as `<hb0>` — archiver, `RED  radar                    failed_stage bars: poll failures: 2` (carried family; `com.cobalt.radar running 3042 min, heartbeat fresh`), com.cobalt.archiver, com.cobalt.replay. No new RED; aset `pid 7760`, sheet HTTP 200.
- D2.6 `date` → `Mon Oct 12 10:11:55 EDT 2026`. `git -C /Users/cobalt/cobalt tag pre-launcher-shadow-check-1011` at `96e163ee`.

### STEP-4 (restart set EMPTY)
- 4.1 `date` → `<t down>` = `Mon Oct 12 10:12:06 EDT 2026`.
- 4.2 nothing booted out (empty set).
- 4.3 `rev-parse --short=8 HEAD` → `96e163ee` = `<pre-merge>`; `git -C /Users/cobalt/cobalt merge --ff-only deploy/launcher-shadow-check-1011` → `Updating 96e163ee..1966c239` / `Fast-forward` (12 files, 768 insertions, 13 deletions).
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 nothing to bootstrap. `<t up>` = 4.3's `date` 10:12:06 ET; downtime: none.

## Smoke
- FIRST CALLS after `<t up>` (10:12:06): `<rp_up>` = 18 · `<rpr_up>` = 60 · `<re_up>` = 43 · `<lc_up>` = 39 (= D1).
- (a) `date` 10:12:22 · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 7760` (SAME, outside the set) · `… com.cobalt.radar` → `state = running`, `pid = 61093` (SAME) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (SAME). GREEN.
- (b) `date` 10:12:25 · `grep -c "Started server process" aset.err` → `277` = `<a0>` (aset outside the set) · `Traceback` aset.err → `217` = `<ta0>` · `Traceback` radar.err → `0` = `<tr0>` · `TaxonomyConfigError` radar.err → `0` = `<tc0>`.
- (c) `curl … https://cobalt.taild24291.ts.net/` → `200` · `…/radar` → `200` · `…/radar\?frame=phone` → `200`. GREEN.
- (d) MARKERS: marker 1 → `1`, marker 2 → `1` (after values). GREEN.
- (s) SMOKE READS: `The shadow check wording is on main` → `grep -c -F -e "On a shadow card the check counts and holds findings exactly as on any card" ".../CHECK-HUB.md"` → `1` (exit 0; green = prints 1) · `The preflight takes a shadow stop line on main` → `grep -c -F -e "SHADOW BUILT · job:" "/Users/cobalt/cobalt/ops/desk/preflight.sh"` → `1` (exit 0). GREEN. The tests behind them ran in the gate: `offline 4199/0`, `with-DB 5096/0`, `live-note 146/0` (`## L68 GATE`).
- (f) validate → as 4.5 (exit 0) · `COBALT_ENV=production uv run cobalt jobs restarts 96e163ee..1966c239` → exit 0, the same 12 rows as STEP-R, `RESTARTS: none` = `<restart set>`, no `UNCLASSIFIED`. GREEN.
- (g) no migration.
- (e) first read `date` 10:12:37 → `HEARTBEAT RED — 2 job(s) and 2 probe(s)  (2026-10-12 10:12:38 EDT)`; `RED  radar                    failed_stage bars: poll failures: 2; poll WFF stale since 2026-10-12T14:06:31.678942+00:00` (carried family); `com.cobalt.radar running 3043 min, heartbeat fresh`; the other REDs as `<hb0>`.

- (e) second read `date` 10:14:32 → `HEARTBEAT RED — 2 job(s) and 2 probe(s)  (2026-10-12 10:14:35 EDT)` (117 s after the first): `RED  radar                    failed_stage bars: poll failures: 1; poll WFF stale since 2026-10-12T14:06:31.678942+00:00` (carried family); `com.cobalt.radar running 3045 min, heartbeat fresh`; archiver, com.cobalt.archiver, com.cobalt.replay as `<hb0>`. No new RED. GREEN.
- (b) THE SPACED TAILS: `date` 10:13:36 (+90 s) · `tail -n 12 radar.err` → last cycle line `10:10:53.311 … radar cycle: scanning scan_id=1791814172671` (before `<t up>`), no failure line; `date` 10:15:06 (+180 s) · `tail -n 12 radar.err` → `2026-10-12 10:13:54.139 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1791814353333` (after `<t up>`), no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → SETTLED GREEN; the third tail is not needed. Traceback counts re-read 10:15:12: radar.err `0`, aset.err `217` (= baseline).
- (h) REVERT-READBACK `date` 10:15:12 (`<t up>` + 186 s): `radar panel FAILED` `18` · `radar pool refresh FAILED` `60` · `radar S5 evaluate FAILED` `43` · `lifecycle card read failed` `39` — each = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, none growing; `curl …/radar` → `200`; no census read on the card. GREEN.
- THE CHAIN: every check committed (P2: check `86b9daa5`, fix report on `ef754d0b`, G3 FIXED) → the tips re-read (P3: `66c4fefc`, `ef754d0b`) → the merged tree `c09a532f` (T) → RESTARTS derived: none (R) → three suites green on `c09a532f`: offline 4199/0 · with-DB 5096/0 · live-note 146/0 (G) → `<stack-final>` `1966c239` = `<m1>` + docs (D2.3) → the landed code `96e163ee..1966c239` (4.3) → markers 0 → 1 (d) → no migration (g) → residents up, same pids (a) → radar cycling at 10:13:54 (b, e) → the set's reads print 1 (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

### CLOSE
- `<pre-merge>` `96e163ee` → `<stack-final>` `1966c239`. Tags: `pre-launcher-shadow-check-1011` (at `96e163ee`), `deploy-2026-10-12-launcher-shadow-check` (at `1966c239`, after the green smoke).
- `<t down>` / `<t up>` / seconds: none (the restart set is EMPTY; 4.3's `date` 10:12:06 ET).
- uv sync: none in production; the gate's `.venv` was created in the gate worktree at STEP-R (`Installed 253 packages in 966ms`).
- proof cost: none (no migration). `migrations applied: none`. `<RB>`: none before / none after.
- Snapshot: `ssd: snapshot b8e63b49` (D2.4).
- `RESTARTS done: none`.
- THE ROLLBACK STRING (the desk's):
  1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 1966c239` — ONE revert of the main-into-gate merge (it carries the set's merge with it); no resident to take down (restart set none).
  2. SCHEMA: none (no migration).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` — git titles it `Reapply "Merge branch 'main' into deploy/launcher-shadow-check-1011"`.

### PRE-STOP SELF-CHECK
1. Every smoke row's evidence is quoted verbatim with its `date` (10:12:22, 10:12:25, 10:12:37, 10:13:36, 10:14:32, 10:15:06, 10:15:12) — `## Smoke`.
2. Code tip and head re-read at P3 (`rev-parse` → `66c4fefc`, `ef754d0b`); `merge-base --is-ancestor 66c4fefc 1966c239` → exit 0; `merge-base --is-ancestor ef754d0b 1966c239` → exit 0.
3. REVERT-READBACK shown at (h): the four counts `18` `60` `43` `39` = the `<t up>` counts. Every count, sha and `file:line` in this report was read from tool output this run (main tip `rev-parse --short=8 main` → `1966c239`).
4. No conflict marker: STEP-T ran clean (`Merge made by the 'ort' strategy.`, no `UU`/`AA` path), D2.1 likewise.

## CONTINUE
next: none (DEPLOYED)

## DECISIONS
none

## RECORDS
- Downtime: none (restart set EMPTY; every resident kept its pid: aset 7760, radar 61093, agent 22243).
- `cobalt_dev: 0013 (F2 = F0)` — `664 35 272c95bbb12241e3611e4b36326ccf87` both; the lock released by `gate.sh`.
- RETIRE OWED: none (no plist removed).
- The carried RED as read: `RED  radar                    failed_stage bars: poll failures: <1|2>`, from 10:12:38 with `; poll WFF stale since 2026-10-12T14:06:31.678942+00:00` — the carried family at D1, D2.5 and (e). Also standing, outside this deploy: `RED  archiver` / `com.cobalt.archiver` (Finviz `429 Too Many Requests`, last run 2026-10-10 00:54 UTC) and `com.cobalt.replay` (`archiver not done: state 'failed'`).
- Cleanup owed (L46, the desk's): the gate worktree `/Users/cobalt/cobalt-wt/deploy-launcher-shadow-check-1011` (it now holds a `.venv`) and branch `deploy/launcher-shadow-check-1011`; the set's branch `ops/launcher-shadow-check-1011` and its worktree.
- P2 reading: the fix report lives on the branch only, so `git log -1 -- <fix report>` on `main` prints nothing; it was read committed at the branch head (`log -1 ef754d0b -- <fix report>` → `ef754d0bf7f0…`) as P2 says the fix report is read there. It reaches `main` with this merge.
- `?? .claude/settings.json.bak` on `main` at D0: outside the accepted and the refused paths of D0; recorded, not touched.
- The allowlist probe's commit `26b3c146` was reset away at once (`reset --soft HEAD~1`, HEAD back to `012e38aa`).
- REFUSED, not needed: `grep -n -F ".env: removed" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. The line was read with the Read tool instead (`:2088`).
- (card) launcher-shadow-check-1011: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-shadow-check-build-2026-10-11.md` at `ef754d0b` last line: BUILT · job: launcher-shadow-check-1011 · tip: 66c4fefc | on a76d8855 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 10 of 10 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 115749
- (card) launcher-shadow-check-1011: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-shadow-check-check-2026-10-11.md` last line: CHECK DONE · job: launcher-shadow-check-1011 · pass: 1 · tip: a8c18242 · house A: Grok FINDINGS: 5 · findings: 6 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none (not needed) · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 3 · for Dejan: 0 · tokens: 236094
- (card) launcher-shadow-check-1011: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-shadow-check-1011` → `ef754d0b`; code tip `66c4fefc`
- (card) written by deploy-card.sh at 2026-10-12 09:36 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-12-launcher-shadow-check 1966c239 | set: none | migrations: none | gate: offline 4199/0 · with-DB 5096/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 205807
