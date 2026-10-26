# deploy f4-probe · SET: f4-probe · MIGRATIONS: none

## §0 Headline
Deploy of `ops/f4-probe` (code tip `150296da`, head `07b507f9`) in progress.

## L74
- One block arrived in a system reminder asking that commits also carry a `Claude-Session: https://claude.ai/code/session_012k796qSQe5AsQ6ixF2ieEQ` line. Recorded as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1058-deploy-f4-probe-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1058-deploy-f4-probe-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-26/1058-deploy-f4-probe-card.md" · 0 · ab5555927348e4ec0b7255df3dd6717ca069946a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-26/1058-deploy-f4-probe-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
AUTHORIZED
```
RULINGS: none.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la ".../reports/deploy-f4-probe.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Mon Oct 26 10:53:38 EDT 2026` — outside 21:30-22:30 ET |
| P2 check last line | `tail -n 3 ".../reports/f4-probe-check-2026-10-26.md"` | 0 | `CHECK DONE · job: f4-probe · pass: 1 · tip: 150296da · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9131/0 · with-DB 5967/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 26 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 208781` — carries `held unfixed: 0`, `ready: YES`, `tip: 150296da` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/f4-probe-check-2026-10-26.md"` | 0 | `c06cf4d8efd49eb0d5db2ec7c41e07ff0be114c4` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/f4-probe-check-2026-10-26.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 150296da` | 0 | `150296da` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f4-probe` | 0 | `07b507f9` = TIP |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 150296da 07b507f9` | 0 | — |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 150296da 07b507f9 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-f4-probe status --short --branch` | 0 | `## deploy/f4-probe` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-f4-probe rev-parse --short=8 HEAD` | 0 | `ab555592` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor ab555592 main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/f4-probe` | 0 | empty |
| P6 marker 1 | `ls /Users/cobalt/cobalt/src/cobalt/prefill/refresh_probe.py` | 1 | `ls: /Users/cobalt/cobalt/src/cobalt/prefill/refresh_probe.py: No such file or directory` = before |
| P6 marker 2 | `grep -c -F "PROBE_ITEMS = (" /Users/cobalt/cobalt/src/cobalt/prefill/refresh_probe.py` | 2 | `grep: /Users/cobalt/cobalt/src/cobalt/prefill/refresh_probe.py: No such file or directory` — card's before `0`; the file is absent (marker 1), so production does not carry it. See `## DECISIONS` 1 |
| P6 marker 3 | `grep -c -F "test_x7_the_daymode_unit_still_starts_as_of_after_a_later_daymode_write" /Users/cobalt/cobalt/tests/cobalt/test_prefill_refresh.py` | 1 | `0` = before |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 07b507f9 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 36927` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 36944` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 retired | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1` — `com.cobalt.agent recorded retired` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` (retired: expected) |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-f4-probe merge --no-edit 07b507f9` → `Merge made by the 'ort' strategy.` (8 files changed, 1028 insertions; `src/cobalt/prefill/cli.py`, `src/cobalt/prefill/refresh_probe.py` (new), `tests/cobalt/test_prefill_refresh.py`, `tests/cobalt/test_refresh_probe.py` (new), 4 docs files)
- `git -C /Users/cobalt/cobalt-wt/deploy-f4-probe rev-parse --short=8 HEAD` → `285860b5` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent ab555592..deploy/f4-probe` → `285860b51 Merge commit '07b507f9' into deploy/f4-probe`
- `merge-base --is-ancestor 150296da deploy/f4-probe` → exit 0 · `merge-base --is-ancestor 07b507f9 deploy/f4-probe` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat ab555592 deploy/f4-probe -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat ab555592 deploy/f4-probe -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" ab555592 deploy/f4-probe` → exit 0, whole: `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-f4-probe` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0, whole (after the uv venv create lines `Using CPython 3.14.3 …`, `Creating virtual environment at: .venv`, `Built cobalt-agent …`, `Installed 257 packages in 795ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/prefill/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/daily.md	M	DOCS	-
docs/40 - DevDocs/reports/f4-probe-build-2026-10-26.md	A	DOCS	-
docs/40 - DevDocs/reports/f4-probe-build-2026-10-26.result	A	DOCS	-
src/cobalt/prefill/cli.py	M	static import reach	-
src/cobalt/prefill/refresh_probe.py	A	static import reach	-
tests/cobalt/test_prefill_refresh.py	M	test/documentation; no resident	-
tests/cobalt/test_refresh_probe.py	A	test/documentation; no resident	-
RESTARTS: none
```
- `<restart set>`: EMPTY — no resident goes down; the merge lands with the residents up.
- `<deferred set>`: empty · `<launchd set>`: empty
- com.cobalt.agent: recorded retired — not restarted
- No `UNCLASSIFIED` row.

## L68 GATE
THE EQUAL-TREE CLAUSE holds: ONE branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat 150296da 285860b5 -- . ":(exclude)docs"` → nothing; the check's stop line carries `with-DB 5967/0` (> 0). The check's suite lines are the gate's; (a)–(f) are not re-run. Quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-probe-check-2026-10-26.md:216-238`:
```
tests/ops: run (deploy gate)
offline 9131/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5967/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/f4-probe-all-20261026-095741.log
```
SKIPPED judgment (c): every line is inside the allowed set. `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262` by line; `test_playbook_live.py:31` is the decorator line of `test_live_vault_renders_six_decks` (`grep -n -F "def test_"` → `32:`) with reason `COBALT_LIVE_VAULT_ROOT not set`; `test_checkpoints_live.py:36` is the decorator line of `test_dry_run_finds_the_heading_in_real_notes` (`37:`) with reason `COBALT_LIVE_VAULT_ROOT not set`; `test_s3_c4_experiments.py:95` is the decorator line of `test_x14_live_his_template_strips_to_the_committed_fixture` (`96:`); `test_replay_line.py:266` reason names `COBALT_TEST_LIVE_DRC`.
`cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 285860b5

## Deploy table
STEP-D0 (10:55 ET):
- `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 75]`; `status --porcelain --untracked-files=no` → only ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml` and ` M` under `docs/40 - DevDocs/`; no staged line. Untracked: `??` under `docs/40 - DevDocs/` and `?? .claude/settings.json.bak` (not `src/`/`tests/`/`ops/`/`configs/`; recorded).
- `git -C /Users/cobalt/cobalt diff --stat ab555592 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-f4-probe` → ok; `tag -d` → `Deleted tag 'scratch-allow-probe-f4-probe' (was ab5555927)`; `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main e498d7942] scratch: allowlist probe (reverted next line)`; `reset --soft HEAD~1` → ok; `log --oneline -1` → `ab5555927 docs(desk): deploy card 1058 f4-probe` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-26-f4-probe` → exit 1; `refs/tags/pre-f4-probe` → exit 1.

STEP-D1 (10:56 ET), production baseline:
- `date` → `Mon Oct 26 10:56:10 EDT 2026`. `heartbeat show` → `<hb0>`: `HEARTBEAT RED — 2 job(s)  (2026-10-26 10:56:11 EDT)`. The two REDs, quoted: `RED  com.cobalt.agent             not loaded NOT LOADED in launchd — …` (recorded retired) and `RED  com.cobalt.replay            failed    StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings top_n Field required …`. Neither is an aset, sheet or radar probe → named, not a stop. `OK   sheet HTTP http://127.0.0.1:5010/ -> 200` · `OK   radar scanning (rth), members 50` · `OK   com.cobalt.aset running loaded, pid 36927` · `OK   com.cobalt.radar running running 2173 min, heartbeat fresh` · `OK   com.cobalt.cos running running 2173 min, heartbeat fresh`. Five labels `OWED (deferred bootstrap)` (prefill-refresh, checkpoint-0715/0745/0815/0845, playbook) are OK rows.
- `validate` → exit 0, `<val0>` ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 13.3 h old` (ssd ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 36927` = `<aset pid>`; `…/com.cobalt.radar` → `state = running`, `pid = 36944` = `<radar pid>`. cos not in `<restart set>`: not read. `cobalt.sh status` → `  Cobalt is OFFLINE.` (agent recorded retired; no `ps -p`).
- `tail -n 8 radar.err` → last line `2026-10-26 10:55:46.930 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1793026465683`, no traceback.
- LOG BASELINES: `<a0>` 298 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 31 · `<rpr0>` 60 · `<re0>` 750 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS again: marker 1 `No such file or directory` · marker 2 `grep: …refresh_probe.py: No such file or directory` (DECISIONS 1) · marker 3 `0` → before.
- THE LAUNCHD SET: empty, nothing. MIGRATION: none, no `<RB>`, no D1-M.

## Smoke

## CONTINUE
next: STEP-D2 (D0, D1 done; D2.0 `deploy-shipped.sh --moved ab555592 "<card>"` → nothing)

## DECISIONS
1. ASK DESK: P6 marker 2 (`grep -c -F "PROBE_ITEMS = ("` on `refresh_probe.py`) printed `No such file or directory` (exit 2), not the card's literal before `0`. The file's absence (marker 1) proves production does not carry the string. Safe default taken: read as the before state and go on; the after read at smoke (d) is `1` as written. [10:53 ET]

## RECORDS

(run in progress — next step under ## CONTINUE)
