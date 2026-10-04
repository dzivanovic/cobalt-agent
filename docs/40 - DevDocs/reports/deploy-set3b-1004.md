# deploy set3b-1004 — set: set3b — migrations: none

## §0 Headline
- Deploy hub `deploy-hub-set3b-1004`, card `prompts/2026-10-04/07-deploy-set3b-card.md`, gate `deploy/set3b-1004` at `/Users/cobalt/cobalt-wt/deploy-1004-2`.
- Preflight green at 16:04 ET Sunday 2026-10-04 (window (iii), a non-trading day).

## L74
- The launch's system context carried an attribution block asking commits to end with a `Claude-Session:` line (session_01UN9Qp4GAALtBx5vPVtHjE2). Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | result |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" DEPLOY-HUB.md` | 1 | nothing |
| card placeholder | `grep -n -E "«FIL[L]" <card>` | 1 | nothing |
| card committed | `git log -1 --format=%H -- <card>` | 0 | `31ea5d201d6ba63c87e68dc5ca4759d30b4cd71b` |
| card clean | `git diff --stat -- <card>` | 0 | nothing |
| standing list R60 (cto-2026-09-30.md:46) | grep · `log -S"\| R60 \|"` | 0 · 0 | `**HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|` · `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| string changes R62 (cto-2026-09-30.md:48) | grep · `log -S` | 0 · 0 | `**HIS RULING** … APPROVES the 7 deploy-line string changes … \| APPROVED \|` · `a45afae72bf2838c8e669e0d3d8dbb67dd892a8b` |
| standing deploy rule R38 (cto-2026-09-30.md:80) | grep · `log -S` | 0 · 0 | `**HIS RULINGS** … deploys self-launch on clean checks + green gate … \| APPROVED \|` · `65aa2b90a8e3eb2f7e94ef10ed40b60e1b2ce542` |
| RULINGS 2026-10-02 R157 (cto-2026-10-02.md:164) | grep · `log -S` | 0 · 0 | `HIS RULING (B): the brain's full process list for 10-03 runs this week … \| HIS RULING · APPROVED \|` · `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| RULINGS 2026-10-03 R216 (cto-2026-10-03.md:222) | grep · `log -S` | 0 · 0 | `HIS RULING: deploy set 3 whenever the desk is ready, Sunday, no window to wait for … \| HIS RULING · APPROVED \|` · `58094781af1a5b2397dda1827098b38b9d7fbb62` |
| RULINGS 2026-10-03 R230 (cto-2026-10-03.md:236) | grep · `log -S` | 0 · 0 | `HIS RULING: set 3 re-deploys whole with card 10 added … \| HIS RULING · APPROVED \|` · `e94e9275a692b0cd56e71e25a49f516a0a557a19` |
| first launch | `ls -la <REPORT>` | 1 | `No such file or directory` |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P1 | `date` | 0 | `Sun Oct  4 16:04:07 EDT 2026` — lawful under (iii): a Sunday, a non-trading day |
| P2 #1 | `tail -n 3 adoption-port-check-2026-10-03-r3.md` | 0 | `CHECK DONE · job: adoption-port · pass: 1 · tip: 685b88d6 · … · held unfixed: 0 · open: 0 · … · RESTARTS: com.cobalt.radar · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0`; committed `d41326ab…`; diff clean |
| P2 #2 | `tail -n 3 dev-rebuild-port-check-2026-10-03-r2.md` | 0 | `CHECK DONE · job: dev-rebuild-port · pass: 1 · tip: 396edb5a · … · held unfixed: 0 · open: 0 · … · RESTARTS: com.cobalt.radar · files opened: 6 · ready: YES · decisions: 1 · for Dejan: 0`; committed `23e558e2…`; diff clean |
| P2 #3 | `tail -n 3 desk-tools-port-check-2026-10-03.md` | 0 | `CHECK DONE · job: desk-tools-port · pass: 1 · tip: 5c1d629f · … · held unfixed: 0 · open: 0 · … · RESTARTS: none · files opened: 22 · ready: YES · decisions: 0 · for Dejan: 0`; committed `d41326ab…`; diff clean |
| P2 #4 | `tail -n 3 close-timer-check-2026-10-03.md` | 0 | `CHECK DONE · job: close-timer · pass: 1 · tip: 47a689a1 · … · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · … · RESTARTS: none · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0`; committed `903bf19a…`; diff clean |
| P2 #5 | `tail -n 3 cobalt-guard-check-2026-10-04.md` | 0 | `CHECK DONE · job: cobalt-guard · pass: 1 · tip: a2e19ceb · … · held: 4 · fixed: 4 · held unfixed: 0 · open: 2 · … · RESTARTS: none · files opened: 14 · ready: YES · decisions: 3 · for Dejan: 1`; committed `8564c35f…`; diff clean |
| P3 | `rev-parse --short=8` each tip / head | 0 | `685b88d6`/`15ba4b75` · `396edb5a`/`0452dc99` · `5c1d629f`/`525b5ae1` · `47a689a1`/`47a689a1` · `a2e19ceb`/`a2e19ceb` — all equal the card |
| P3 | `merge-base --is-ancestor <tip> <head>` ×5 | 0 ×5 | ancestors |
| P3 | `diff --stat <tip> <head> -- . ':(exclude)docs'` ×5 | 0 ×5 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` — the lock is free |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/set3b-1004` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `35a8e975` = `<m0>` |
| P5 | `merge-base --is-ancestor 35a8e975 main` | 0 | ancestor |
| P5 | `log --oneline main..deploy/set3b-1004` | 0 | empty |
| P6 | `grep -c -F "window (v) does not hold" DEPLOY-HUB.md` | 1 | `0` (before `0`) |
| P6 | `ls …/db_migrations/dev_rebuild.py` | 1 | `No such file or directory` |
| P6 | `grep -c -F "claude-fable-5-1" ops/desk/desk-launch.sh` | 1 | `0` |
| P6 | `ls ops/desk/close-timer.sh` | 1 | `No such file or directory` |
| P6 | `grep -c -F "route: production is the deploy hub" ops/desk/bare-guard.py` | 1 | `0` |
| P7 | `diff --stat main <head> -- src/cobalt/db_migrations` ×5 | 0 | 15ba4b75: `cli.py` · 0452dc99: `cli.py`, `dev_rebuild.py` · 525b5ae1: `cli.py` · 47a689a1: nothing · a2e19ceb: nothing — no `.sql`, no `__init__.py`: CODE, passes `MIGRATIONS: none` |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 13209 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 18818 |
| P8 | `ls ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
| head | `git -C <GATE> merge --no-edit <head>` |
|---|---|
| 15ba4b75 | `Merge made by the 'ort' strategy.` (57 files) |
| 0452dc99 | `Merge made by the 'ort' strategy.` (11 files) |
| 525b5ae1 | `Merge made by the 'ort' strategy.` (17 files) |
| 47a689a1 | `Merge made by the 'ort' strategy.` (4 files) |
| a2e19ceb | `Merge made by the 'ort' strategy.` (3 files) |

- `<m1>` = `ce213e11` (`git -C <GATE> rev-parse --short=8 HEAD`).
- `log --oneline --merges --first-parent 35a8e975..deploy/set3b-1004` → `ce213e11 Merge commit 'a2e19ceb'` · `7a9f4a0c Merge commit '47a689a1'` · `308c73e1 Merge commit '525b5ae1'` · `57844de1 Merge commit '0452dc99'` · `f362c306 Merge commit '15ba4b75'` — five lines, one per head.
- `merge-base --is-ancestor <x> deploy/set3b-1004` → exit 0 for 685b88d6, 15ba4b75, 396edb5a, 0452dc99, 5c1d629f, 525b5ae1, 47a689a1, a2e19ceb.
- `diff --stat 35a8e975 deploy/set3b-1004 -- src/cobalt/db_migrations` → `cli.py | 350`, `dev_rebuild.py | 879` — no `.sql`, no `__init__.py`: no migration path (MIGRATIONS: none).
- STEP-C `diff --stat 35a8e975 deploy/set3b-1004 -- configs ops` → 31 files, all under `ops/desk/` (`31 files changed, 1581 insertions(+), 154 deletions(-)`); nothing under `configs`. One plist ADDED: `ops/desk/com.cobalt.close-timer.plist`, Label `com.cobalt.close-timer` (line 6) — not a `label:` of `configs/cobalt/jobs.yaml` (15 labels read: aset, mainframe, obsidian, agent, herdr, radar, prefill-daily, archiver, replay, cards-expire, daymode-propose, backup, heartbeat, seat-usage, generated), path not `ops/com.cobalt.close-timer.plist`: admitted. No plist removed.

## RESTARTS
- `cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0. uv: `Creating virtual environment at: .venv` · `Installed 253 packages in 844ms`.
- Table (85 rows): every `docs/` row `DOCS -`; every `ops/desk/` row `operator script; no Cobalt reader -`; every `tests/` row `test/documentation; no resident -`; `src/cobalt/db_migrations/cli.py M static import reach com.cobalt.radar`; `src/cobalt/db_migrations/dev_rebuild.py A static import reach com.cobalt.radar`. No `UNCLASSIFIED` row.
- `RESTARTS: com.cobalt.radar` → `<restart set>` = `com.cobalt.radar`.

## L68 GATE
On `deploy/set3b-1004` at `<m1>` = `ce213e11`, in `<GATE>`.
- (a0) `ls -la <GATE>/.env` → No such file · the 17-file early read → **`261 passed, 157 skipped in 15.40s`**, 0 failed (every skip a with-DB `Postgres env settings not available` / `requires_db`).
- (a) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, exit 0) → **`3782 passed, 755 skipped, 1 xfailed, 36 warnings in 587.08s (0:09:47)`**. 0 failed, 0 errors; `grep -c -F "FAILED"` → `0`. No uv sync line (the venv was built at STEP-R). `<p>` = 3782.
- (e) `ls -la <GATE>/.env` → No such file · `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest … test_radar_evaluate.py test_replay_line.py test_catalyst.py test_predicate.py` → **`146 passed, 1 skipped, 15 warnings in 25.01s`**. The skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — in the allowed set; none names `COBALT_LIVE_VAULT_ROOT`. `<l>` = 146.
- (b) `sh /Users/cobalt/.claude/ops/take-devdb-lock.sh deploy-1004-2 90` (background, exit 0) → `lock taken: deploy-1004-2` (`date` 16:17:39). `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line: `-rw-------  1 cobalt  staff  2186 Oct  4 16:17 /Users/cobalt/cobalt-wt/deploy-1004-2/.env`. Lock held to the stop line.
- (d2) `COBALT_ENV=production uv run cobalt validate` → exit 0; `13 trade_def(s) validated OK`; `registry <-> ops/: 15 label(s), exact match`; `registry <-> plists: schedules and COBALT_ENV agree on every job`; `Placement (docs/PLACEMENT.md): tree clean.` `<jobsG>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot.`
- `<FP>` → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables probed (`drc_*`, `legs`, `prediction_records`, `voice_turns` read `-`); `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; no `CHANGED`; `SLOTS WARN user.aset_sizings max_attnum 1394 of 1600 · dropped 1340 · live 54 · fix: cobalt db dev-rebuild user.aset_sizings (dev only)`; `code: ce213e11 (clean)`; `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`; `TABLES 0011`. The level line this tool now prints is `TABLES <nnnn>` (the highest table-creating migration present, `cli.py:66-70`), not a bare number; `ops/desk/gate-lists.md:47-48` `## LEVEL 0013` = `TABLES 0011 · FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`, equal field for field → `cobalt_dev` at `0013`.
- (c) PASS 1: the hub's command byte for byte; no build of this set added a pass-1 deselect (adoption-port build `:125`, `:128` "no added deselect"; dev-rebuild-port build `:201`, `:229` "no deselect added"; close-timer build `:172`; desk-tools-port and cobalt-guard reports carry no `--deselect`). Background, exit 0 → **`4461 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings in 723.72s (0:12:03)`**. 0 failed, 0 errors. The two `FAILED` strings in the output are UserWarning texts from `tests/cobalt/test_drc_d2_fix_r1_runs.py:92` and `:125` (the tests' own constructed refusals), not test results. SKIPPED, all 7 in the allowed set: `test_cards_picks.py:388` (S2-P2's card_score column is present on cobalt_dev) · `test_cards_picks.py:401` (real S2-P2 0007 applied…) · `test_radar_evaluate.py:695` (COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof) · `test_replay_line.py:266` (COBALT_TEST_LIVE_DRC … not set) · `test_s3_c4_experiments.py:95` = `@requires_live` on `test_x14_live_his_template_strips_to_the_committed_fixture` (`:96`) · `test_catalyst.py:365` · `test_predicate.py:262`. `<d1>` = 4461.
- (c2) FORWARD: `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `-- applying` 0001 … 0011, 0013, 0014 … 0022 in FORWARD order; 36 tables proven, 28 `OK`, 8 `CREATED` (`drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns`); `content UNCHANGED on every table.`; no `CHANGED`; `proof cost: BEFORE 6.4 s + AFTER 6.2 s = total 12.6 s`; `SLOTS WARN user.aset_sizings max_attnum 1398 of 1600 · dropped 1340 · live 58`; `code: ce213e11 (clean)`. No migration in this set.
  **`dev forward: APPLIED 16:31`** (`date` → `Sun Oct  4 16:31:23 EDT 2026`).
  - `<FP>` → `<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c` (the builds' F1).
- (c3) PASS 2: the hub's command byte for byte (no pass-1 deselect to add), background, exit 0 → **`173 passed, 1 deselected, 5 warnings in 223.46s (0:03:43)`**; `grep -c -F "PASSED"` → `173`; `grep -c -F "SKIPPED"` → `0`. 0 failed, 0 errors. The 11 `FAILED` strings (`grep -n -F`, lines 66–150) are app log lines (`radar panel FAILED: … radar pool 'primary' is missing`) and page text echoed by `-rA` — the tests' own constructed refusals, not test results. `<d2>` = 173; `<d>` = 4461 + 173 = **4634**.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `-- applying` `0022_prediction_records.rollback.sql` … `0014_radar_handicap.rollback.sql`, newest first; 8 tables `DROPPED`, every other `OK`; `content UNCHANGED on every table.`; `SLOTS WARN user.aset_sizings max_attnum 1430 of 1600 · dropped 1376 · live 54`. `<FP>` → `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field. **`cobalt_dev: 0013 — F2 = F0`**. Lock and `<GATE>/.env` held to the stop line (L76).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on ce213e11 — offline 3782/0 · with-DB 4634/0 (4461 + 173) · live-note 146/0 (`date` 16:36:23).

## Deploy table
STEP-D0 (16:36):
- `git status --short --branch` → `## main...origin/main [ahead 286]`; `--porcelain` → ` M .claude/settings.json`, ` M`/`??` under `docs/40 - DevDocs/` only, plus `?? .claude/settings.json.bak` (untracked; not staged, not under `src/`, `tests/`, `ops/`, `configs/`). No staged line.
- `diff --stat 35a8e975 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- Allowlist probe: `tag scratch-allow-probe-set3b-1004` → ok; `tag -d` → `Deleted tag 'scratch-allow-probe-set3b-1004' (was 35a8e975)`; `commit --allow-empty` → `[main cf9e975f] scratch: allowlist probe (reverted next line)`; `reset --soft HEAD~1` → ok; `log --oneline -1` → `35a8e975 docs(desk): R259 set 3b preflight ready YES`.
- Tag names: `refs/tags/deploy-2026-10-04-2` → exit 1; `refs/tags/pre-set3b-1004` → exit 1.

STEP-D1 baseline (16:36:50):
- `<hb0>` = `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red (2026-10-04 16:36:51 EDT)`; `com.cobalt.radar running 1394 min, heartbeat fresh`; `radar idle (overnight)`; `com.cobalt.herdr` AMB unmanaged (declared interim). No RED.
- `<val0>`: validate exit 0, `13 trade_def(s) validated OK`, `registry <-> ops/: 15 label(s), exact match`, `Placement (docs/PLACEMENT.md): tree clean.` `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot.`
- `backup status` → `newest snapshot: 18.9 h old` (ssd ARMED).
- aset `state = running`, `<aset pid>` = 13209 · radar `state = running`, `<radar pid>` = 18818 · `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → listed.
- `tail -n 8 radar.err` → `radar cycle: idle:overnight scan_id=None` every 100 s, last 16:36:42; no traceback.
- `<a0>` 42 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 58 · `<re0>` 39 · `<lc0>` 39.
- `curl …/radar` → `200`. MARKERS again → `0` · No such file · `0` · No such file · `0` (each its `before`).
- MIGRATIONS none: no `<RB>`, no census, no D1-M.

## CONTINUE
next: STEP-D2.0 (commit the report)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
