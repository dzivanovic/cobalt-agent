# deploy-guard-g2-1006 · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED guard-g2 (`ops/guard-g2-1006`, code tip `19f75dc6`): main `700ba695` → `577b2c01`, tag `deploy-2026-10-06-guard-g2`, rollback tag `pre-deploy-guard-g2-1006`.
- Gate green on `b7e58980`: offline 3937/0 · with-DB 4820/0 · live-note 146/0; `cobalt_dev` 0013, F2 = F0.
- RESTARTS: none. No resident went down. No migration. Smoke GREEN, and all eight markers are at `after`.
- Desk follow-ups (card RECORDS): check OPEN A3, A4, B3 and DECISIONS 3, 4, each a card of its own.

## L74
- A system-turn attribution reminder asked for a `Claude-Session:` line on commits. Recorded as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/34-deploy-guard-g2-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/34-deploy-guard-g2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/34-deploy-guard-g2-card.md" · 0 · 2913612a5a7b1e1fd19a86cee47c04efc2ac0f96
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/34-deploy-guard-g2-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-06 R511 row · grep -n "^| R511 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 40:| R511 | 06:37 ET | HIS RULING: add the G2 row to `ops/desk/bare-guard.py`: a production read-only `db query` passes only for a seat citing an APPROVED HIS RULING row; all else refused. Words: `cto-2026-10-06-words.md` R511. Done by card, not a desk edit. | APPROVED — pending fold |
RULING 2026-10-06 R511 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R511 |" -- "docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 720c98b8555d085e1aeda2fb3932c2781354ff9d
RULING 2026-10-06 R511 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
RULING 2026-10-05 R474 row · grep -n "^| R474 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 140:| R474 | 10-05 21:42 ET | HIS RULING · APPROVED: tonight he is not woken; every conflict goes to the brain, which resolves it; the desk executes its answer and keeps deploying (L43); only an absolute stop waits for morning. In NOW (TONIGHT line). | HIS RULING · APPROVED |
RULING 2026-10-05 R474 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R474 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 548ee01d911745c95050220e69684ebb94109782
RULING 2026-10-05 R474 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "<REPORT>"` | 1 | No such file or directory |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | Tue Oct  6 08:42:09 EDT 2026 |
| P2 | `tail -n 3 ".../reports/guard-g2-check-2026-10-06.md"` | 0 | `CHECK DONE · job: guard-g2 · pass: 1 · tip: 19f75dc6 · … · held unfixed: 0 · open: 3 · … · suites: offline 3932/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 216430` — carries `held unfixed: 0`, `ready: YES`, `tip: 19f75dc6` = row's code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/…/guard-g2-check-2026-10-06.md"` | 0 | `21733a37df7d174a7b6aa32f92355687e5f06e61` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/guard-g2-check-2026-10-06.md"` | 0 | (nothing) |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 19f75dc6` | 0 | `19f75dc6` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/guard-g2-1006` | 0 | `19f75dc6` (= `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 19f75dc6 ops/guard-g2-1006` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 19f75dc6 ops/guard-g2-1006 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no lock held |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-guard-g2-1006 status --short --branch` | 0 | `## deploy/deploy-guard-g2-1006` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `21733a37` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 21733a37 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-guard-g2-1006` | 0 | (empty) |
| P6 | the eight `## MARKERS` greps on main's tree | 1 each | `0` each = every `before` |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 19f75dc6 -- src/cobalt/db_migrations` | 0 | (nothing) — no migration, matches `MIGRATIONS: none` |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 79583` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 79594` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 19f75dc6` → `Merge made by the 'ort' strategy.` (5 files changed, 624 insertions(+), 3 deletions(-)).
- `git -C <GATE> rev-parse --short=8 HEAD` → `b7e58980` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 21733a37..deploy/deploy-guard-g2-1006` → `b7e58980 Merge commit '19f75dc6' into deploy/deploy-guard-g2-1006` (one line, one head).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 19f75dc6 deploy/deploy-guard-g2-1006` → exit 0 (code tip = branch head).
- `git -C /Users/cobalt/cobalt diff --stat 21733a37 deploy/deploy-guard-g2-1006 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 21733a37 deploy/deploy-guard-g2-1006 -- configs ops` → `ops/desk/bare-guard.py | 54 +++…---` · `ops/desk/desk-launch.sh | 42 ++++…` · `2 files changed, 93 insertions(+), 3 deletions(-)`. No plist added, modified or removed.

## RESTARTS
- `cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (first `uv` in the gate: `Creating virtual environment at: .venv` · `Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-guard-g2-1006` · `Installed 253 packages in 797ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/guard-g2-build-2026-10-06.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
RESTARTS: none
```
- `<restart set>` = EMPTY. No UNCLASSIFIED row. MIGRATIONS none, so L66 does not apply. No resident goes down.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied. The check's stop line carries `with-DB 0/0`, so the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 163 skipped in 15.90s`, 0 failed (with-DB skips only).
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-guard-g2-1006 all --deploy`: no `--deselect` (the set's build ran `DB: none` and deselected nothing), and the card gives no `--tickers` or `--migration`. Exit 0. Verdict lines, whole:
```
offline 3937/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4820/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-guard-g2-1006-all-20261006-084346.log
```
- (a) offline `3937/0` (log:861 `3937 passed, 786 skipped, 2 xfailed`).
- (b) lock taken, waited 0 min. `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log:878). Proof-only at 0013: `NOTHING WAS APPLIED`, no `CHANGED` (log:923, 929).
- (c) PASS 1 has 7 skips, each inside the allowed set. `test_s3_c4_experiments.py:95` is the `@requires_live` decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (`tests/cobalt/test_s3_c4_experiments.py:95-96`).
- (c2) `dev forward: APPLIED 09:06:38` (log:1087). The FORWARD ran 0001…0022 in order, and the proof table reads `content UNCHANGED on every table` (log:1152). No `CHANGED`.
- (c3) log:1085 `4632 passed, 7 skipped, 82 deselected, 4 xfailed`. Combined with pass 1 → `with-DB 4820/0`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log:1836) = F0 → `cobalt_dev: 0013 — F2 = F0` (log:1887).
- THE RELEASE: `lock released` (log:1889) · `.env: removed` (log:1893). `ls -la <GATE>/.env` → No such file. `grep -c -x -F "deploy-guard-g2-1006" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent). The log carries no clock time for the release; it lies between 09:06:38 and the gate's exit (read 09:11:40).
- (e) live-note `146/0`. No skip names `COBALT_LIVE_VAULT_ROOT` in that leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on b7e58980

## Deploy table
STEP-D0:
- `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 137]`. `status --porcelain` shows no staged line. Every dirty path is ` M`/`??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml` or ` M .claude/settings.json`, except `?? .claude/settings.json.bak`. That path is outside `src/ tests/ ops/ configs/`, so it is not refused (RECORDS).
- `git -C /Users/cobalt/cobalt diff --stat 21733a37 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-deploy-guard-g2-1006` ok · `tag -d …` → `Deleted tag 'scratch-allow-probe-deploy-guard-g2-1006' (was 21733a37)` · `commit --allow-empty …` → `[main a30f7a4c] scratch: allowlist probe (reverted next line)` · `reset --soft HEAD~1` ok · `log --oneline -1` → `21733a37 docs(report): guard-g2 check report, preflight report` (HEAD back).
- TAGS: `rev-parse --verify --quiet refs/tags/deploy-2026-10-06-guard-g2` → exit 1 · `…refs/tags/pre-deploy-guard-g2-1006` → exit 1.

STEP-D1 (baseline, `date` → Tue Oct  6 09:12:08 EDT 2026):
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 1 job(s)  (2026-10-06 09:12:09 EDT)`. Every probe is OK except two:
  - `AMB com.cobalt.herdr unmanaged … declared interim`
  - `RED  com.cobalt.generated  failed  GeneratedCommitRefused: \`git commit -m\` failed (exit 1): pre-commit: a deploy hub is live — no desk commit on main until its stop line: 9f093747 deploy-hub-deploy-p2-1005 …`
  
  That RED is not the aset, sheet or radar probe, so it is named and is not a stop (RECORDS). Also read: `OK sheet HTTP … 200` · `OK radar scanning (premarket), members 50` · `OK com.cobalt.aset running loaded, pid 79583` · `OK com.cobalt.agent running pid 22243` · `OK com.cobalt.radar running running 513 min, heartbeat fresh`.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.` · `<jobs0>` `Jobs (F17): 15 registered — 6 resident, 9 one-shot.`
- `backup status` → `newest snapshot: 1.3 h old` (ssd ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 79583` · `…com.cobalt.radar` → `state = running`, `pid = 79594` · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 logs/radar.err` → `radar cycle: scanning` every ~3 min, last `2026-10-06 09:11:06.389`. No traceback.
- Log baselines: `<a0>` 45 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 58 · `<re0>` 40 · `<lc0>` 39.
- `curl … /radar` → `200`. The eight `## MARKERS` again → `0` each (= before).
- No migration: `<RB>`, census and D1-M are not run.

STEP-D2:
- D2.0 commit `700ba695 docs(report): deploy deploy-guard-g2-1006 — gate green on b7e58980`. `show --stat HEAD` → one file, 143 insertions. `<pre-merge>` = `700ba695`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `577b2c01` · `rev-parse --short=8 577b2c01^2` → `700ba695` = `<pre-merge>` · `merge-base --is-ancestor b7e58980 577b2c01` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat b7e58980 577b2c01 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` before → `newest snapshot: 1.3 h old`. `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 5015.7 MB` · `ssd: snapshot b839df9a — 0 new / 3 changed, 61.2 MB added, 1 pruned`. `backup status` after → `newest snapshot: 0.0 h old`.
- D2.5 `date` 09:13:59 · `heartbeat show` → `(2026-10-06 09:14:01 EDT)`, 112 s after D1's 09:12:09. Same probes as `<hb0>`: only `RED com.cobalt.generated` (the same text) and `AMB com.cobalt.herdr`. aset pid 79583, radar `running 515 min, heartbeat fresh`. No new RED.
- D2.6 `date` → Tue Oct  6 09:14:06 EDT 2026 · `git -C /Users/cobalt/cobalt tag pre-deploy-guard-g2-1006` at `700ba695`.

STEP-4 (`<restart set>` empty):
- 4.1 `date` → Tue Oct  6 09:14:17 EDT 2026 = `<t down>` = `<t up>` (empty set).
- 4.2 nothing goes down.
- 4.3 `rev-parse --short=8 HEAD` → `700ba695` = `<pre-merge>`. `git -C /Users/cobalt/cobalt merge --ff-only deploy/deploy-guard-g2-1006` → `Updating 700ba695..577b2c01` / `Fast-forward` (5 files changed, 624 insertions(+), 3 deletions(-)).
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.` · `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`.
- 4.6 nothing to restore. Downtime: none.

STEP-7 summary:
| field | value |
|---|---|
| main | `700ba695` (`<pre-merge>`) → `577b2c01` (`<stack-final>`) |
| tags | `pre-deploy-guard-g2-1006` at `700ba695` · `deploy-2026-10-06-guard-g2` at `577b2c01` (after green smoke) |
| `<t down>` / `<t up>` / seconds | none (empty set; merge at 09:14:17) |
| uv sync line | gate worktree only: `Installed 253 packages in 797ms` (main's env unchanged; no `uv` sync line in production calls) |
| proof cost | n/a (no migration; no D1-M) |
| migrations applied | none |
| `<RB>` before / after | n/a (MIGRATIONS: none) |
| snapshot | `b839df9a` (ssd, 09:13:35) |
| RESTARTS done | none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 577b2c01` (no resident to take down: RESTARTS none). 2. SCHEMA: none. 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` |

## Smoke
- FIRST CALLS after `<t up>` (09:14:17): `<rp_up>` 17 · `<rpr_up>` 58 · `<re_up>` 40 · `<lc_up>` 39 (= D1 baselines).
- (a) 09:14:27 · aset `state = running`, `pid = 79583` (SAME, outside the set) · radar `state = running`, `pid = 79594` (SAME) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (same).
- (b) 09:14:31 · `Started server process` 45 = `<a0>` (aset outside the set) · Traceback aset 2 = `<ta0>` · Traceback radar 0 = `<tr0>` · TaxonomyConfigError 0 = `<tc0>`.
- (c) 09:14:31 · `/` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200`.
- (d) 09:14:37 · markers: `def marked_read(command, s)` 1 · `MARKER = re.compile` 1 · `and not marked_read(command, s)` 1 · `PROD-READ:` 8 · `production reads?([^[:alpha:]]|\$)` 1 · `MARKED_KINDS` 3 · `def test_g2_a_marked_seat_is_denied_a_production_word_in_a_brace_word` 1 · `def test_r1_a_disapproved_row_stamps_nothing` 1. Each = its `after`.
- (f) `validate` as 4.5 (exit 0) · `COBALT_ENV=production uv run cobalt jobs restarts 700ba695..577b2c01` → exit 0, the same five rows (DOCS / operator script; no Cobalt reader ×2 / test/documentation; no resident ×2), `RESTARTS: none` = STEP-R's set, no UNCLASSIFIED.
- (e) read 1 at 09:14:49: `HEARTBEAT RED — 1 job(s)`, the same probe set as `<hb0>` (only `RED com.cobalt.generated`, same text; `AMB com.cobalt.herdr`). `com.cobalt.radar running running 516 min, heartbeat fresh`.
- (s) 09:15:08 · each exit 0:
  - the G2 pass (R2): `def marked_read(command, s)` → `1`
  - the G2 row in the rule: `and not marked_read(command, s)` → `1`
  - the launcher stamp (R1): `PROD-READ:` → `8`
  - the check's A1 fix: `production reads?([^[:alpha:]]|\$)` → `1`
  
  Each is a count of 1 or more = GREEN. The tests behind them ran in the gate (`tests/ops` inside offline 3937/0).
- (b) radar tails:
  - 09:15:52 (+95 s): last line `09:14:03.202 radar cycle: scanning`, none after `<t up>` yet.
  - 09:17:17 (+180 s): `2026-10-06 09:17:00.182 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791292543219`. This is after `<t up>`, with no `radar S5 evaluate FAILED`, no `lifecycle card read failed` and no traceback in the 12 lines. Settled GREEN, so no third tail is needed.
- (e) read 2 at 09:16:42, 113 s after read 1: the same probe set as `<hb0>` (only `RED com.cobalt.generated`, unchanged; `AMB com.cobalt.herdr`). `com.cobalt.radar running running 518 min, heartbeat fresh`. No new RED.
- (g) no migration.
- (h) 09:17:21 (+184 s): `radar panel FAILED` 17 · `radar pool refresh FAILED` 58 · `radar S5 evaluate FAILED` 40 · `lifecycle card read failed` 39, each = its `<…_up>`. `/radar` → `200`. No census read on the card. Traceback radar 0, aset 2 (= baseline).

THE CHAIN:
- every check committed (P2: `21733a37…`, clean)
- the tips re-read (P3: `19f75dc6` = head)
- the merged tree (T: `b7e58980`, one merge, no migration)
- RESTARTS derived (R: none)
- three suites green on `b7e58980` (G: 3937/0 · 4820/0 · 146/0)
- `577b2c01` = `b7e58980` + docs (D2.3: nothing outside docs)
- the landed code (4.3: `Updating 700ba695..577b2c01`)
- markers at `after` (d: 1, 1, 1, 8, 1, 3, 1, 1)
- no migration (g)
- residents up, same pids (a)
- radar cycling (b: 09:17:00; e: fresh)
- the set's reads (s: 1, 1, 8, 1)
- no new failure (h: 17/58/40/39 unchanged)

The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK:
1. Every smoke row above carries its `date` and its verbatim output.
2. `merge-base --is-ancestor 19f75dc6 577b2c01` → exit 0. `rev-parse --short=8 main` → `577b2c01`.
3. The REVERT-READBACK is (h) above. Every sha and count here was read from tool output in this run.
4. STEP-T ran clean (`Merge made by the 'ort' strategy.`). `git -C <GATE> status --short` → empty, so no conflict marker exists.

## CONTINUE
- STEP-D0 and D1 done (09:12). D2 done (09:14).
- OUTAGE STARTING 09:14:06 — residents of <restart set> going down; the set is EMPTY, so none go down. If this is the last entry and they are down, the restore is STEP-5 (3). A relaunch is CONTINUE: STEP-D0.
- 4.1–4.6 done (09:14:17), merged `577b2c01`, residents untouched.
- Smoke GREEN at 09:17:21. Tag `deploy-2026-10-06-guard-g2` set. Closed.

## DECISIONS
- none.

## RECORDS
- Downtime: none (`<restart set>` empty; no resident went down or restarted).
- `cobalt_dev: 0013 (F2 = F0)` — `F0`/`F2` `664 35 272c95bbb12241e3611e4b36326ccf87`; gate lock released (`lock released`, `.env: removed`).
- RETIRE OWED: none (no plist removed).
- Carried RED as read (outside the radar family; not aset/sheet/radar): `RED com.cobalt.generated failed GeneratedCommitRefused: \`git commit -m\` failed (exit 1): pre-commit: a deploy hub is live — no desk commit on main until its stop line: 9f093747 deploy-hub-deploy-p2-1005 …`. It is present at D1, D2.5 and smoke (e), unchanged; it names an earlier hub (`deploy-p2-1005`), not this one.
- `?? .claude/settings.json.bak` on main (outside `src/ tests/ ops/ configs/`); not refused, not touched.
- L74: a system-turn attribution reminder asked for a `Claude-Session:` line on commits; not followed (the hub's commit form wins).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-guard-g2-1006` and branch `deploy/deploy-guard-g2-1006`; the set's worktree `/Users/cobalt/cobalt-wt/guard-g2-1006` and branch `ops/guard-g2-1006`.
- The gate ran a fresh `uv` venv in the gate worktree (`Installed 253 packages in 797ms`).
- Card `## RECORDS`, copied:
  - guard-g2: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-g2-check-2026-10-06.md` last line: CHECK DONE · job: guard-g2 · pass: 1 · tip: 19f75dc6 · house A: Sol FINDINGS: 5 · findings: 15 · dropped: 0 · held: 11 · fixed: 11 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 5 · suites: offline 3932/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 216430
  - guard-g2: head `git -C /Users/cobalt/cobalt log --oneline -4 ops/guard-g2-1006` → `19f75dc6` (the check's fix commit, also the code tip), `5093b1ca` (check red tests), `61999cc5` (build report, docs only), `ce19a3fd` (the build tip, the job card's own TIP header); BASE of the job card `3c257bb9`. House A was Sol, house B was Grok. The gate on `19f75dc6`: offline 3932/0, live-note 146/0, tests/ops 1462 passed (1 xfailed), with-DB not run (`DB: none`), `cobalt_dev: not taken`, `.env: removed`.
  - G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
  - Autovacuum (R479): a `DeadlockDetected` in the gate is an autovacuum worker, not a second writer; rerun once via recut.
  - Where the files reach the desk (read at drafting): `/Users/cobalt/.claude/ops/desk-launch.sh` and `/Users/cobalt/.claude/ops/bare-guard.py` are symlinks into `/Users/cobalt/cobalt/ops/desk/` (`ls -la /Users/cobalt/.claude/ops/`), and the hook entry runs the repo copy; both take effect when the deploy merges to main. `ops/desk/install-fixed.sh` installs a prompt-title token (`«INSTALL`) and copies no desk script, so the deploy hub does not run it; it is an existing script but `DEPLOY-HUB.md` does not name it (`grep -n -F "install-fixed"` → nothing). No new command.
  - FOLLOW-UP for him, NOT part of this deploy: the check's `## OPEN`. A3: CONTROL (b) as typed cannot go red under the leading-shape mutation (the build's `db migrate --prod` case carries it). A4: CONTROL (e) is red on BASE on its G1 deny text only. B3: a marked `db query … "DELETE FROM t"` passes the guard (R2(ii) reads no SQL; `guard_select` and `BEGIN READ ONLY` in `src/cobalt/db_query.py` refuse it at run time); the desk rules whether "a write verb" covers SQL text.
  - FOLLOW-UP for him, NOT part of this deploy: the check's DECISIONS 3 and 4. (3) `ruling_row` (`ops/desk/desk-launch.sh`, `*"HIS RULING"*APPROVED*`) also accepts a `DISAPPROVED` status for every kind that calls it; only the prompt stamp was fixed. (4) UNPROVEN: the `desk` kind launches the wake-up file's typed line with no `PROD-READ:` test while the guard counts a marked desk seat (`MARKED_KINDS`). Each is a card of its own.
  - R511 on main reads `APPROVED — pending fold` (`reports/cto-2026-10-06.md` line 38 at drafting; the line number moves). R412 reads `APPROVED (in cto-desk-contract.md …)` and R474 reads `HIS RULING · APPROVED` (`reports/cto-2026-10-05.md` lines 109, 140).
  - AFTER values above were read from the checked-out worktree `/Users/cobalt/cobalt-wt/guard-g2-1006` (the branch `ops/guard-g2-1006`, head `19f75dc6` verified by `rev-parse`), BEFORE values from main's working tree, at drafting time 2026-10-06 08:39 EDT; the deploy re-proves each with `git -C /Users/cobalt/cobalt show 19f75dc6:<path>`.
  - Absent today: `git rev-parse --verify` of `deploy/deploy-guard-g2-1006` and of `deploy-2026-10-06-guard-g2` both failed; `ls` of `/Users/cobalt/cobalt-wt/deploy-guard-g2-1006` and of the REPORT path both failed.
  - one feature per deploy (his R390).

DEPLOYED deploy-2026-10-06-guard-g2 577b2c01 | set: none | migrations: none | gate: offline 3937/0 · with-DB 4820/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 194389
