# deploy-flake-fix-1006 · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED `deploy-2026-10-06-flake-fix`. `main` went `ac2e9371` → `433e1c7e` (fast-forward). It ships `ops/flake-fix-1006` at `f520debb`: a test-side retry in the `migrated` fixture of `tests/cobalt/test_drc_store.py`, plus docs.
- Gate: the check's gate on `f520debb` stands under the equal-tree clause (offline 3932/0 · with-DB 886/0 · live-note 146/0).
- `RESTARTS: none`: no resident went down and there was no downtime. `migrations applied: none`. Snapshot `925d4c7d`.
- Smoke GREEN: markers at their `after` values, residents unchanged, curls 200, radar cycling, failure counts flat.
- 1 decision (an ASK DESK on R412's "production on hold" wording, default: go on); 0 for Dejan.

## L74
- A system reminder in this session added a `Claude-Session:` line to the commit attribution. It is recorded here as data and not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/11-deploy-flake-fix-card.md"`, the output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/11-deploy-flake-fix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/11-deploy-flake-fix-card.md" · 0 · 04b8974302845b523bc0929c4a9a92dc454c41e1
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/11-deploy-flake-fix-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-03 R326 row · grep -n "^| R326 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · 332:| R326 | 10-05 06:19 ET | HIS RULING: A on all three — D5 ships at `c96b5118` with O1 pinned (follow-up card: items' store + B2 wording); second-writer survey gets its 5 read strings, this seat only; F15 P2 X11 → follow-up card. Words: `cto-2026-10-05-words.md` R326–R327. | HIS RULING · APPROVED |
RULING 2026-10-03 R326 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R326 |" -- "docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · b133743171ec855e164c445ceef03e657eb50eeb
RULING 2026-10-03 R326 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-flake-fix-1006.md"` → exit 1, `No such file or directory`.

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (above) |
| P1 | `date` | 0 | `Tue Oct  6 02:41:47 EDT 2026` |
| P2 | `tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/flake-fix-check-2026-10-06.md"` | 0 | last line: `CHECK DONE · job: flake-fix · pass: 2 · tip: f520debb · house B: Grok FINDINGS: 3 · findings: 3 · dropped: 0 · held: 3 · fixed: 0 · held unfixed: 0 · open: 0 · suites: offline 3932/0 · with-DB 886/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 135367` — carries `held unfixed: 0` and `ready: YES`; `tip: f520debb` = the row's code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/flake-fix-check-2026-10-06.md"` | 0 | `7f18ca5f1a518f38da168d7329aa8d7ce389dcc1` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/flake-fix-check-2026-10-06.md"` | 0 | (nothing) |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 f520debb` | 0 | `f520debb` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/flake-fix-1006` | 0 | `f520debb` (= the row and `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor f520debb ops/flake-fix-1006` | 0 | (nothing) |
| P3 | `git -C /Users/cobalt/cobalt diff --stat f520debb ops/flake-fix-1006 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no worktree holds the lock |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-flake-fix-1006 status --short --branch` | 0 | `## deploy/deploy-flake-fix-1006` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-flake-fix-1006 rev-parse --short=8 HEAD` | 0 | `1714ff1a` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 1714ff1a main` | 0 | (nothing) |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-flake-fix-1006` | 0 | (empty) |
| P6 | the eight `## MARKERS` `grep -c -F` reads on main's tree | 1 each | `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0` = every `before` |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main ops/flake-fix-1006 -- src/cobalt/db_migrations` | 0 | (nothing) — no migration; `MIGRATIONS: none` holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 79583` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 79594` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-flake-fix-1006 merge --no-edit f520debb` → `Merge made by the 'ort' strategy.` (`docs/40 - DevDocs/cobalt/drc/store.md | 5 +`, `.../reports/flake-fix-build-2026-10-06.md | 223 +++`, `tests/cobalt/test_drc_store.py | 159 ++++++++++++++-`, `3 files changed, 383 insertions(+), 4 deletions(-)`).
- `git -C /Users/cobalt/cobalt-wt/deploy-flake-fix-1006 rev-parse --short=8 HEAD` → `a041c3ad` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 1714ff1a..deploy/deploy-flake-fix-1006` → `a041c3ad Merge commit 'f520debb' into deploy/deploy-flake-fix-1006` (one head, one merge).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor f520debb deploy/deploy-flake-fix-1006` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 1714ff1a deploy/deploy-flake-fix-1006 -- src/cobalt/db_migrations` → (nothing): no migration path, as `MIGRATIONS: none` requires.
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 1714ff1a deploy/deploy-flake-fix-1006 -- configs ops` → (nothing). No plist added, changed or removed.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-flake-fix-1006` · `ls -la /Users/cobalt/cobalt-wt/deploy-flake-fix-1006/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD`, exit 0. Before the table, uv printed a sync: `Creating virtual environment at: .venv` · `Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-flake-fix-1006` · `Installed 253 packages in 922ms`.
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/drc/store.md	M	DOCS	-
docs/40 - DevDocs/reports/flake-fix-build-2026-10-06.md	A	DOCS	-
tests/cobalt/test_drc_store.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row. `<restart set>` = EMPTY (none). No resident goes down; the merge lands with the residents up.

## L68 GATE
THE EQUAL-TREE CLAUSE holds:
- `TIP` has ONE branch.
- `git -C /Users/cobalt/cobalt diff --stat f520debb a041c3ad -- . ":(exclude)docs"` → (nothing).
- The check's stop line carries `with-DB 886/0`, a count above 0.

So the check's three suite lines are the gate's, and (a0) and (a)–(f) were not run here. They are quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/flake-fix-check-2026-10-06.md` lines 204–226 (gate log `/Users/cobalt/cobalt-wt/.gate-logs/flake-fix-1006-all-20261006-015751.log`, line 345):
```
offline 3932/0
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 886/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
```
- (c) SKIPPED lines read against the allowed set. All seven are inside it:
  - `test_cards_picks.py:388` and `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365` and `test_predicate.py:262` are named in the set.
  - The `test_replay_line.py` skip names `COBALT_TEST_LIVE_DRC`.
  - `test_s3_c4_experiments.py:95` is the skip decorator of `test_x14_live_his_template_strips_to_the_committed_fixture`. `grep` of the gate tree shows `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`, and the decorator's reason sits at line 35.
- with-DB: `698 passed, 7 skipped` (pass 1) + `188 passed` (pass 2) = 886. `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` = `F2: 664 35 272c95bbb12241e3611e4b36326ccf87`. The check records `lock released` (log `:1804`).
- (e) live-note: `146 passed, 1 skipped`. The one skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.
- This run took no lock. `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed (cwd back).

GATE GREEN on a041c3ad (offline 3932/0 · with-DB 886/0 · live-note 146/0, the check's gate on f520debb, equal tree) at Tue Oct  6 02:43:20 EDT 2026

## Deploy table
STEP-D0:
- `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 69]`.
- `status --porcelain` lists only ` M`/`??` paths under `docs/40 - DevDocs/`, plus ` M .claude/settings.json` and `?? .claude/settings.json.bak`. There is no staged line and no dirty `src/`, `tests/`, `ops/` or `configs/` path. `.claude/settings.json.bak` is in neither the hub's ACCEPTED nor its REFUSED list; it is recorded under `## RECORDS`.
- `git -C /Users/cobalt/cobalt diff --stat 1714ff1a main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing).
- ALLOWLIST PROBE:
  - `tag scratch-allow-probe-deploy-flake-fix-1006` → (ok).
  - `tag -d …` → `Deleted tag 'scratch-allow-probe-deploy-flake-fix-1006' (was 1714ff1a)`.
  - `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 86bcbc73] scratch: allowlist probe (reverted next line)`.
  - `reset --soft HEAD~1` → (ok).
  - `log --oneline -1` → `1714ff1a docs(report): flake-fix deploy card preflight — 20 checks, 0 fails, ready YES; R496` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-06-flake-fix` → exit 1; `… refs/tags/pre-deploy-flake-fix-1006` → exit 1.

STEP-D1 (production baseline, read-only):
- `date` → `Tue Oct  6 02:43:58 EDT 2026`.
- `<hb0>`: `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 1 job(s)  (2026-10-06 02:43:59 EDT)`.
  - `OK sheet HTTP http://127.0.0.1:5010/ -> 200` · `OK radar idle (overnight)` · `OK com.cobalt.aset running loaded, pid 79583` · `OK com.cobalt.agent running pid 22243 alive` · `OK com.cobalt.radar running running 125 min, heartbeat fresh` · `AMB com.cobalt.herdr unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) …; runs outside launchd by declared interim`.
  - The one RED: `RED com.cobalt.generated failed GeneratedCommitRefused: \`git commit -m\` failed (exit 1): pre-commit: a deploy hub is live — no desk commit on main until its stop line: 9f093747 deploy-hub-deploy-p2-1005 …`.
  - That RED is not on the aset, sheet or radar probe, so it is named here and is not a stop.
- `<val0>`: `COBALT_ENV=production uv run cobalt validate` → exit 0, ending `Placement (docs/PLACEMENT.md): tree clean.`. `<jobs0>`: `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 2.1 h old`.
- Residents:
  - `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 79583`.
  - `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 79594`.
  - `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → eight `radar cycle: idle:overnight scan_id=None` lines, the last `2026-10-06 02:43:46.799`. No traceback.
- LOG BASELINES: `<a0>`=45 · `<ta0>`=2 · `<tr0>`=0 · `<tc0>`=0 · `<rp0>`=17 · `<rpr0>`=58 · `<re0>`=40 · `<lc0>`=39.
- `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` → `200`.
- MARKERS again: `0` ×8 = every `before`.
- No migration on the card: `<RB>`, census and D1-M are not run.

STEP-D2:
- D2.0: report committed as `ac2e9371 docs(report): deploy deploy-flake-fix-1006 — gate green on a041c3ad`. `show --stat HEAD` lists the one file (`.../reports/deploy-deploy-flake-fix-1006.md | 144 +++`). `<pre-merge>` = `ac2e9371`.
- D2.1: `git -C /Users/cobalt/cobalt-wt/deploy-flake-fix-1006 merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2:
  - `<stack-final>` = `433e1c7e`.
  - `rev-parse --short=8 433e1c7e^2` → `ac2e9371` = `<pre-merge>`.
  - `merge-base --is-ancestor a041c3ad 433e1c7e` → exit 0.
- D2.3: `git -C /Users/cobalt/cobalt diff --stat a041c3ad 433e1c7e -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing). The tree that lands is the gated tree plus docs.
- D2.4 snapshot:
  - Before: `backup status` → `newest snapshot: 2.1 h old`.
  - `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 4889.5 MB` · `ssd: snapshot 925d4c7d — 0 new / 2 changed, 12.8 MB added, 1 pruned` · `F17: com.cobalt.backup DONE`.
  - After: `backup status` → `newest snapshot: 0.0 h old`. Snapshot id `925d4c7d`.
- D2.5: `date` → `Tue Oct  6 02:45:34 EDT 2026` with a heartbeat at `02:45:35`, which was only 96 s after D1. The clock was filled with `date`+heartbeat pairs (02:45:39/42, 02:45:46/48, 02:45:51/53). The counted read is `date` `Tue Oct  6 02:45:57 EDT 2026`, heartbeat `HEARTBEAT RED — 1 job(s)  (2026-10-06 02:46:00 EDT)`, 121 s after D1's.
  - The same single RED, `com.cobalt.generated`.
  - aset `running loaded, pid 79583`; radar `running running 127 min, heartbeat fresh`; `radar idle (overnight)`. No new RED.
- D2.6: `date` → `Tue Oct  6 02:46:04 EDT 2026`. `git -C /Users/cobalt/cobalt tag pre-deploy-flake-fix-1006` at `ac2e9371` → (ok).

STEP-4 (`<restart set>` empty):
- 4.1: `date` → `Tue Oct  6 02:46:16 EDT 2026`. This is `<t down>`, and also `<t up>` because no resident went down.
- 4.2: nothing booted out; the agent was not stopped.
- 4.3: `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `ac2e9371` = `<pre-merge>`. `git -C /Users/cobalt/cobalt merge --ff-only deploy/deploy-flake-fix-1006` → `Updating ac2e9371..433e1c7e` / `Fast-forward` (`3 files changed, 383 insertions(+), 4 deletions(-)`).
- 4.4: `migrations applied: none`.
- 4.5: `COBALT_ENV=production uv run cobalt validate` → exit 0, the same output as `<val0>`, ending `Placement (docs/PLACEMENT.md): tree clean.`. `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`.
- 4.6: nothing to bootstrap. `date` → `Tue Oct  6 02:46:24 EDT 2026`. Downtime: none.

STEP-7 summary:
| item | value |
|---|---|
| merge | `<pre-merge>` `ac2e9371` → `<stack-final>` `433e1c7e` (`<m0>` `1714ff1a`, `<m1>` `a041c3ad`) |
| tags | `pre-deploy-flake-fix-1006` at `ac2e9371`; `deploy-2026-10-06-flake-fix` at `433e1c7e` (after green smoke) |
| `<t down>` / `<t up>` / seconds | none (empty set; `02:46:16` both) / 0 |
| uv sync line | STEP-R, gate tree only: `Creating virtual environment at: .venv` … `Installed 253 packages in 922ms`. No sync line on the production calls. |
| proof cost | none (no migration) |
| migrations applied | none |
| `<RB>` before / after | not applicable (no migration) |
| snapshot | `925d4c7d` (ssd, `0 new / 2 changed, 12.8 MB added, 1 pruned`; dump 4889.5 MB) |
| RESTARTS done | none |

THE ROLLBACK STRING (the desk's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 433e1c7e`. ONE revert of the main-into-gate merge. The restart set is empty, so no resident goes down or up.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
`<t up>` = `Tue Oct  6 02:46:16 EDT 2026` (the empty set; 4.1's `date`, the call before 4.3).
- FIRST CALLS: `<rp_up>`=17 · `<rpr_up>`=58 · `<re_up>`=40 · `<lc_up>`=39. These equal D1's `<rp0>` `<rpr0>` `<re0>` `<lc0>`.
- (a) `date` `Tue Oct  6 02:46:36 EDT 2026`. Same pids as D1, as the empty set requires:
  - `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 79583`.
  - `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 79594`.
  - `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`. GREEN.
- (b) counts:
  - `grep -c "Started server process" …/aset.err` → `45` = `<a0>` (aset not in the set).
  - Traceback aset `2` = `<ta0>` · Traceback radar `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`.
  - `tail -n 30 …/aset.err` → last `INFO:     Started server process [79589]` … `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)`, from 2026-10-06 00:38. No restart, as expected.
- (c) `date` `Tue Oct  6 02:46:43 EDT 2026` → `/` `200` · `/radar` `200` · `/radar\?frame=phone` `200`. GREEN.
- (d) MARKERS (`date` `02:46:43`), each its `after`:
  - `migration retry` `8` · `conn = None` `1`.
  - `…retries_once_when_the_first_migration_attempt_deadlocks` `1` · `…fails_on_a_third_deadlock_after_two_retries` `1` · `…does_not_retry_another_error` `1`.
  - `…retries_when_opening_the_first_attempt_deadlocks` `1` · `…closes_a_failed_attempt_when_rollback_fails` `1`.
  - `flake-fix` in `store.md` `2`.
  - GREEN.
- (f) `date` `Tue Oct  6 02:46:56 EDT 2026`:
  - validate as 4.5 (exit 0, `= <val0>`).
  - `COBALT_ENV=production uv run cobalt jobs restarts ac2e9371..433e1c7e` → exit 0, the same three rows as STEP-R, `RESTARTS: none` = `<restart set>`, no `UNCLASSIFIED`. GREEN.
- (g) no migration: not run.
- (s) THE SET'S SMOKE READS (the same `grep -c -F` strings as markers 3, 6, 7, read at `02:46:43`), each exit 0 with a count ≥ 1:
  - retry test (F1) `1`.
  - open-deadlock test (H2) `1`.
  - rollback-failure test (H3) `1`.
  - The tests themselves ran in the gate (with-DB 886/0, quoted under `## L68 GATE`); no test runs in production.
- (b) radar tails:
  - `date` `Tue Oct  6 02:47:47 EDT 2026` (`<t up>` + 91 s): `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` → last line `2026-10-06 02:47:06.855 | INFO | cobalt.radar.runner:resident:467 - radar cycle: idle:overnight scan_id=None`. That cycle line is stamped after `<t up>`, and the tail has no `radar S5 evaluate FAILED`, no `lifecycle card read failed` and no traceback. That settles (b) GREEN.
  - A later read at `02:49:16` (`<t up>` + 180 s) shows `2026-10-06 02:48:46.885 … radar cycle: idle:overnight scan_id=None` as well, same clean tail.
- (e) heartbeat twice, 111 s apart. The single RED (`com.cobalt.generated`) is the one in `<hb0>`; no new RED. GREEN.
  - `HEARTBEAT RED — 1 job(s)  (2026-10-06 02:46:58 EDT)`.
  - `HEARTBEAT RED — 1 job(s)  (2026-10-06 02:48:49 EDT)` (`date` `02:48:47`).
  - Both reads: `OK com.cobalt.radar running running 128 min, heartbeat fresh` / `… 130 min, heartbeat fresh` · `OK com.cobalt.aset running loaded, pid 79583` · `OK sheet HTTP http://127.0.0.1:5010/ -> 200`.
  - Between them, `date`+heartbeat clock-fill pairs at 02:47:04 – 02:49:13 (`L38`) all read the same.
- (h) REVERT-READBACK, `date` `Tue Oct  6 02:49:16 EDT 2026` (`<t up>` + 180 s), after (b) settled. GREEN:
  - The four counts `17` / `58` / `40` / `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`; none grew.
  - `curl … /radar` → `200`.
  - No `census` line on the card.

THE CHAIN: every link holds.
- Every check committed (P2: `7f18ca5f…`, `ready: YES`, `held unfixed: 0`).
- The tips re-read (P3: `f520debb` = code tip = head).
- The merged tree (T: one merge `a041c3ad`, no migration, no configs/ops change).
- RESTARTS derived (R: none).
- Three suites green on `<m1>` (G: equal tree with the check's `f520debb` gate, 3932/886/146).
- `<stack-final>` = `<m1>` + docs (D2.3: empty diff).
- The landed code (4.3: `ac2e9371..433e1c7e`).
- Markers (d: all at `after`).
- No migration (g).
- Residents unchanged after the merge (a: same pids, as the empty set requires).
- Radar cycling (b, e).
- The set's reads (s: 1/1/1).
- No new failure (h: flat).

The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK:
1. Every smoke row above is quoted with its `date`.
2. `f520debb` (code tip and head) was re-read at P3, and `git -C /Users/cobalt/cobalt merge-base --is-ancestor f520debb 433e1c7e` → exit 0.
3. REVERT-READBACK is shown at (h). Every count, sha and `file:line` here was read from tool output this run. One exception: `## L68 GATE`'s suite lines and log line numbers are quoted from the check report, with its path, under the equal-tree clause.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.` and D2.1 the same; there was no conflict.

## CONTINUE
OUTAGE STARTING Tue Oct  6 02:46:04 EDT 2026 — residents of none (empty restart set) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
next: none — deployed. The desk's: cleanup (L46, `## RECORDS`); push is his (L55).

## DECISIONS
- ASK DESK: R412 (a `RULINGS` row of this card) ends "Production stays on hold until the workflow set is deployed" (`cto-2026-10-05-words.md` line 27). Is that hold still in force for this deploy? Safe default taken: go on. The card names R412 as its own ruling, `authorize.sh` printed `AUTHORIZED`, and this set ships only a test file and docs (`RESTARTS: none` in the check), so no production behaviour changes. [Tue Oct  6 02:41:47 EDT 2026]

## RECORDS
- Downtime: none. The restart set was empty and no resident went down; aset `79583`, radar `79594` and agent `22243` were the same before and after.
- `cobalt_dev`: this run took no lock and ran no dev migrate. The check's gate on `f520debb` stands under the equal-tree clause: `cobalt_dev: 0013 — F2 = F0`, `.env: removed`.
- No `REFUSED, not needed` line. No `CONTINUE` message arrived. No `RETIRE OWED` (no plist changed).
- The carried heartbeat RED, as read at D1, D2.5 and smoke (e), is unchanged throughout:
  - `RED com.cobalt.generated failed GeneratedCommitRefused: \`git commit -m\` failed (exit 1): pre-commit: a deploy hub is live — no desk commit on main until its stop line: 9f093747 deploy-hub-deploy-p2-1005 …`.
  - It is not on the aset, sheet or radar probe and is not of this deploy. The pre-commit guard it quotes names an earlier hub, `deploy-hub-deploy-p2-1005`; the desk should check whether that hub marker is stale.
- `?? .claude/settings.json.bak` on `main` is in neither D0 list; it was recorded and is not a stop.
- Cleanup owed (L46):
  - the gate worktree `/Users/cobalt/cobalt-wt/deploy-flake-fix-1006` and branch `deploy/deploy-flake-fix-1006`;
  - the set's worktree `/Users/cobalt/cobalt-wt/flake-fix-1006` and branch `ops/flake-fix-1006`;
  - the gate tree's new `.venv` (created by `uv` at STEP-R).
- Tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 015zRNjoQEPxUXvWW6QtDr5D` → `no transcript for 015zRNjoQEPxUXvWW6QtDr5D` (exit 2). That id is the remote bridge id. The local session id `077bc28a-9a90-4d33-aad6-4bfdcc0b3828` (from the job's `state.json`) is the one used for the stop line.
- L74: as under `## L74`.
- The card's `## RECORDS`, copied:
  - flake-fix: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/flake-fix-check-2026-10-06.md` last line: CHECK DONE · job: flake-fix · pass: 2 · tip: f520debb · house B: Grok FINDINGS: 3 · findings: 3 · dropped: 0 · held: 3 · fixed: 0 · held unfixed: 0 · open: 0 · suites: offline 3932/0 · with-DB 886/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 135367
  - flake-fix: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/flake-fix-1006` → `f520debb` (also the head of `git -C /Users/cobalt/cobalt log --oneline main..ops/flake-fix-1006`); code tip `f520debb` (the check's fix commit, H2 H3; its red tests are `814f56fd`); the job card's own TIP header reads `d1fee872` (the build tip); the build report commit `0ff56462` sits between them (docs only). Pass 1 house A was Sol, pass 2 house B was Grok. The gate on `f520debb` (pass 1, stands for pass 2): offline 3932/0, with-DB 886/0, live-note 146/0, `cobalt_dev: 0013 — F2 = F0`, `.env: removed`.
  - G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
  - Autovacuum (R479): a `DeadlockDetected` in the gate is an autovacuum worker, not a second writer; rerun once via recut. The fix here covers the `migrated` fixture of `tests/cobalt/test_drc_store.py` only.
  - FOLLOW-UP for him, NOT part of this deploy: the build's DECISION W. The other tests that open `db.connect_migration` and run `_apply(conn, FORWARD)` themselves (`test_p4_migrations.py`, `test_voice_store.py`, `test_archiver_migrations.py`, `radar_migrated_support.py`, `test_drc_d2_fix_r1_db.py` and others) keep no retry; a card of their own if one deadlocks (job card `## NOT IN THIS JOB`).
  - AFTER values above were read from the checked-out worktree `/Users/cobalt/cobalt-wt/flake-fix-1006` (HEAD `f520debb`, verified), BEFORE values from main's working tree, at drafting time 2026-10-06 02:38 EDT; the deploy re-proves each with `git -C /Users/cobalt/cobalt show f520debb:<path>`.
  - Absent today: `git rev-parse --verify` of `deploy/deploy-flake-fix-1006` and of `deploy-2026-10-06-flake-fix` both failed; `ls` of `/Users/cobalt/cobalt-wt/deploy-flake-fix-1006` and of the REPORT path both failed.
  - one feature per deploy (his R390).

DEPLOYED deploy-2026-10-06-flake-fix 433e1c7e | set: none | migrations: none | gate: offline 3932/0 · with-DB 886/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 178413
