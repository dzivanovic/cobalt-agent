# deploy-p2-1005 · set: s3 · migrations: none

## §0 Headline
- Deploy of `f15/p2-replay-1004` (code tip `437c7299`, head `6269f05e`) on gate `deploy/deploy-p2-1005-attempt2`. Running.

## L74
- The session's harness attribution reminder offered a `Claude-Session:` trailer for commits. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/61-deploy-p2-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/61-deploy-p2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/61-deploy-p2-card.md" · 0 · 618d85f0a6e17db4eccaacba04eba1ee3d2763bc
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/61-deploy-p2-card.md" · 0 · nothing
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

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P0 first launch | `ls -la "…/reports/deploy-deploy-p2-1005-attempt2.md"` | 1 | `No such file or directory` |
| P1 | `date` | 0 | `Tue Oct  6 00:06:21 EDT 2026` |
| P2 | `tail -n 3 "…/reports/f15-p2-check-2026-10-05.md"` | 0 | `CHECK DONE · job: f15-p2 · pass: 1 · tip: 437c7299 · … · held unfixed: 0 · … · ready: YES · decisions: 0 · for Dejan: 0` (tip = code tip) |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/f15-p2-check-2026-10-05.md"` | 0 | `4e8795dc5d93751a628be63bcce5b445e71957f9` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/f15-p2-check-2026-10-05.md"` | 0 | (nothing) |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 437c7299` | 0 | `437c7299` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 f15/p2-replay-1004` | 0 | `6269f05e` (= TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 437c7299 6269f05e` | 0 | (nothing) |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 437c7299 6269f05e -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-p2-1005-attempt2` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `11d96acf` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 11d96acf main` | 0 | (nothing) |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-p2-1005-attempt2` | 0 | (empty) |
| P6 | `grep -c -F "def corpus(" …/cards/predictions.py` | 1 | `0` (before 0) |
| P6 | `grep -c -F "def replay(" …/cards/predictions.py` | 1 | `0` (before 0) |
| P6 | `grep -c -F "def cmd_replay" …/cards/cli.py` | 1 | `0` (before 0) |
| P6 | `ls …/tests/cobalt/test_f15_p2_replay.py` | 1 | `No such file or directory` |
| P6 | `ls …/tests/experiments/f15_p2/conftest.py` | 1 | `No such file or directory` |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 6269f05e -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 47333` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 47343` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 6269f05e` → `Merge made by the 'ort' strategy.` (10 files changed, 1822 insertions(+), 4 deletions(-)).
- `git -C <GATE> rev-parse --short=8 HEAD` → `18112f89` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 11d96acf..deploy/deploy-p2-1005-attempt2` → `18112f89 Merge commit '6269f05e' into deploy/deploy-p2-1005-attempt2` (one line, one head).
- `merge-base --is-ancestor 437c7299 deploy/deploy-p2-1005-attempt2` → exit 0; `… 6269f05e …` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 11d96acf deploy/deploy-p2-1005-attempt2 -- src/cobalt/db_migrations` → (nothing): no migration path, as MIGRATIONS: none.
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 11d96acf deploy/deploy-p2-1005-attempt2 -- configs ops` → ` ops/desk/gate-lists.md | 4 ++--` / ` 1 file changed, 2 insertions(+), 2 deletions(-)`. No plist added, modified or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after the venv build lines):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cards/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cards/predictions.md	M	DOCS	-
docs/40 - DevDocs/reports/f15-p2-build-2026-10-04.md	A	DOCS	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
src/cobalt/cards/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/cards/predictions.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_f15_p2_replay.py	A	test/documentation; no resident	-
tests/cobalt/test_f15_p2_replay_db.py	A	test/documentation; no resident	-
tests/experiments/f15_p2/conftest.py	A	test/documentation; no resident	-
tests/experiments/f15_p2/test_x7_x10_x11_db.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
`<restart set>` = `com.cobalt.aset com.cobalt.radar`. No `UNCLASSIFIED` row.

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 437c7299 18112f89 -- . ":(exclude)docs"` → 18 files (configs/cobalt/rules.yaml, ops/desk/*, src/cobalt/cli.py, src/cobalt/drc/*, tests/…; `18 files changed, 1680 insertions(+), 206 deletions(-)`), so the clause does not hold and the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 157 skipped in 15.83s`; 0 failed (all skips are `Postgres env settings not available` / `requires_db`).
- Deselect from the build report (`f15-p2-build-2026-10-04.md:155`): `--deselect tests/cobalt/test_f15_p2_replay_db.py`.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-p2-1005-attempt2 all --deploy --deselect tests/cobalt/test_f15_p2_replay_db.py` (background) → exit 0, verdict lines whole:
```
offline 3932/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4809/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-p2-1005-attempt2-all-20261006-000811.log
```
- Skips: every one is inside the allowed set. `test_s3_c4_experiments.py:95` is the decorator of `def test_x14_live_his_template_strips_to_the_committed_fixture():` at `:96` (grep of the gate tree).
- Log reads: `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (:872) · `dev forward: APPLIED 00:30:54` (:1081) · `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (:1830) · `cobalt_dev: 0013 — F2 = F0` (:1881) · `lock released` (:1883) · `.env: removed` (:1887).
- THE RELEASE verified: `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-p2-1005-attempt2" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.
- GATE GREEN on 18112f89 — offline 3932/0 · with-DB 4809/0 · live-note 146/0 · `date` `Tue Oct  6 00:35:52 EDT 2026`.

## Deploy table
### D0
| check | command | exit | result |
|---|---|---|---|
| main | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 37]` |
| main | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; ` M` ×5 and `??` ×10 under `docs/40 - DevDocs/`; `?? .claude/settings.json.bak` (see DECISIONS 1). No staged line, no dirty `src/` `tests/` `ops/` `configs/` path |
| main moved | `git -C /Users/cobalt/cobalt diff --stat 11d96acf main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | (nothing) |
| probe | `tag scratch-allow-probe-deploy-p2-1005` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-deploy-p2-1005' (was 11d96acf)` |
| probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` | 0 | `[main d2c7e165] scratch: allowlist probe (reverted next line)` |
| probe | `reset --soft HEAD~1` → `log --oneline -1` | 0 / 0 | `11d96acf docs(desk): open cto-2026-10-06.md (night continues; R481)` |
| tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-05-p2-attempt2` | 1 | free |
| tags | `rev-parse --verify --quiet refs/tags/pre-deploy-p2-1005` | 1 | free |

### D1 baseline
- `date` → `Tue Oct  6 00:36:21 EDT 2026`.
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 1 job(s)  (2026-10-06 00:36:22 EDT)`. Every probe OK except `AMB  com.cobalt.herdr  unmanaged AMBER …` and `RED  com.cobalt.generated  failed  GeneratedCommitRefused: \`git commit -m\` failed (exit 1): pre-commit: a deploy hub is live — no desk commit on main until its stop line: 9f093747 deploy-hub-deploy-p2-1005 …`. Aset, sheet and radar probes are OK: `OK sheet HTTP http://127.0.0.1:5010/ -> 200`, `OK radar idle (overnight)`, `OK com.cobalt.aset running loaded, pid 47333`, `OK com.cobalt.radar running running 74 min, heartbeat fresh`, `OK com.cobalt.agent running pid 22243 alive`. The RED is not on the aset, sheet or radar probe, so it is named here and is not a stop.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `13 trade_def(s) validated OK from the vault.` · `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 1.3 h old` (ssd ARMED).
- `launchctl print` aset → `state = running`, `pid = 47333` · radar → `state = running`, `pid = 47343` · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last `2026-10-06 00:35:21.186 | INFO | cobalt.radar.runner:resident:467 - radar cycle: idle:overnight scan_id=None` (one line every 100 s, no traceback).
- Counts: `<a0>` 44 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 58 · `<re0>` 40 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS again → `0`, `0`, `0`, `No such file or directory` ×2 (all at before).
- MIGRATIONS: none → no `<RB>`, census or D1-M.

## Smoke

## CONTINUE
next: STEP-D2

## DECISIONS
1. ASK DESK: `git status --porcelain` on `main` shows `?? .claude/settings.json.bak`. That path is not on D0's accepted list and not in its refused classes (staged, or dirty `src/` `tests/` `ops/` `configs/`). Safe default taken: it is untracked, outside the tree that merges, and not refused, so the run continued. [00:36 EDT]
2. ASK DESK: the card gives no `--tickers`, so the gate ran without it and printed `stray rows: not read (no --tickers given)`; the build's own gate used `--tickers ZZPB,TEST`. Safe default taken: follow the card; F2 = F0 holds. [00:35 EDT]

## RECORDS

(run in progress — next step under ## CONTINUE)
