# deploy-flake-fix-1006 · SET: none · MIGRATIONS: none

## §0 Headline
(in progress)

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

## Smoke

## CONTINUE
next: STEP-D2 (D2.0 report commit)

## DECISIONS
- ASK DESK: R412 (a `RULINGS` row of this card) ends "Production stays on hold until the workflow set is deployed" (`cto-2026-10-05-words.md` line 27). Is that hold still in force for this deploy? Safe default taken: go on. The card names R412 as its own ruling, `authorize.sh` printed `AUTHORIZED`, and this set ships only a test file and docs (`RESTARTS: none` in the check), so no production behaviour changes. [Tue Oct  6 02:41:47 EDT 2026]

## RECORDS

(run in progress — next step under ## CONTINUE)
