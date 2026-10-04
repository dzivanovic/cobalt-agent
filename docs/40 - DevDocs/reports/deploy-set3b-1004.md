# deploy set3b-1004 — set: set3b — migrations: none

## §0 Headline
- DEPLOYED set3b (adoption-port, dev-rebuild-port, desk-tools-port, close-timer, cobalt-guard): `main` `34d9af1d` → `979ec797`, tag `deploy-2026-10-04-2`, rollback tag `pre-set3b-1004`.
- Gate green on `ce213e11`: offline 3782/0 · with-DB 4634/0 (4461 + 173) · live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0); lock released 16:42:52.
- Outage: `com.cobalt.radar` only, 16:39:02 → 16:39:18 (16 s); aset and agent untouched. No migration. Snapshot `67b367e7`.
- Smoke GREEN on every row; heartbeat GREEN before and after. Window (iii): Sunday 2026-10-04.
- decisions: 0 · for Dejan: 0. Push is his; cleanup of the gate and the five set worktrees is owed.

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

STEP-D2:
- D2.0 `add` + `commit … -- <REPORT>` → `[main 34d9af1d] docs(report): deploy set3b-1004 — gate green on ce213e11` · `show --stat HEAD` → that one file (116 insertions). `<pre-merge>` = `34d9af1d`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `979ec797`; `979ec797^2` = `34d9af1d` = `<pre-merge>`; `merge-base --is-ancestor ce213e11 979ec797` → exit 0.
- D2.3 `diff --stat ce213e11 979ec797 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs only).
- D2.4 `backup status` → `newest snapshot: 19.0 h old` · `backup run` → `cobalt_brain via pg_dump inside cobalt_memory — 4460.3 MB` · `ssd: snapshot 67b367e7 — 0 new / 1 changed, 24.8 MB added, 0 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` 16:38:43 · heartbeat `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red (2026-10-04 16:38:45 EDT)` — 114 s after D1's 16:36:51; no RED. (A read at 16:38:15 came at 84 s and was not counted.)
- D2.6 `date` → `Sun Oct  4 16:38:51 EDT 2026` — window (iii), a Sunday, holds. `git tag pre-set3b-1004` → `rev-parse` `34d9af1d`.

STEP-4 (the outage, `com.cobalt.radar` only):
- 4.1 `date` → `Sun Oct  4 16:39:02 EDT 2026` = `<t down>`.
- 4.2 `launchctl bootout gui/501/com.cobalt.radar` → ok · `launchctl print gui/501/com.cobalt.radar` → exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501`. aset and agent not in the set: untouched.
- 4.3 `rev-parse --short=8 HEAD` → `34d9af1d` = `<pre-merge>` · `merge --ff-only deploy/set3b-1004` → `Updating 34d9af1d..979ec797` / `Fast-forward` (83 files changed, 10543 insertions(+), 372 deletions(-)).
- 4.4 `migrations applied: none` (MIGRATIONS: none).
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` (= `<jobs0>`); `registry <-> ops/: 15 label(s), exact match`; `Placement (docs/PLACEMENT.md): tree clean.`
- 4.6 `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` → ok · `launchctl print` → `state = running`, pid 36907 (≠ 18818). `date` → `Sun Oct  4 16:39:18 EDT 2026` = `<t up>`. Downtime 16 s.

STEP-7 summary:
| field | value |
|---|---|
| main | `34d9af1d` (`<pre-merge>`) → `979ec797` (`<stack-final>`) |
| tags | `pre-set3b-1004` → `34d9af1d` · `deploy-2026-10-04-2` → `979ec797` |
| outage | `<t down>` 16:39:02 · `<t up>` 16:39:18 · 16 s |
| uv sync | none at the merge (the gate's venv was built at STEP-R: `Installed 253 packages in 844ms`) |
| proof cost | n/a (no production migration) |
| migrations applied | none |
| `<RB>` before / after | n/a (MIGRATIONS: none) |
| snapshot | `67b367e7` (ssd, 16:38) |
| RESTARTS done | `com.cobalt.radar` |

THE ROLLBACK STRING (the desk's, never this session's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 979ec797` — ONE revert of the main-into-gate merge; `com.cobalt.radar` down first (`launchctl bootout gui/501/com.cobalt.radar`), up after (`launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`).
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` — `Reapply "Merge branch 'main' into deploy/set3b-1004"`.

## Smoke
<rp_up> 17 · <rpr_up> 58 · <re_up> 39 · <lc_up> 39 (read right after `<t up>`).

| row | `date` | command | result | verdict |
|---|---|---|---|---|
| (a) | 16:39:31 | `launchctl print` aset / radar · `cobalt.sh status` | aset `state = running` pid 13209 (= D1, outside the set) · radar `state = running` pid 36907 (≠ 18818, in the set) · `Cobalt is ONLINE (PID: 22243).` (= D1) | GREEN |
| (b) | 16:39:38 | `grep -c "Started server process" aset.err` · `tail -n 30 aset.err` · Traceback / TaxonomyConfigError counts | `42` (= `<a0>`, aset outside the set); tail ends `Started server process [13215]` … `Uvicorn running on http://0.0.0.0:5010` (the 10-02 start, no new start); aset Traceback `2` (= `<ta0>`), radar Traceback `0` (= `<tr0>`), TaxonomyConfigError `0` (= `<tc0>`) | GREEN |
| (b) tails | 16:40:51 (+93 s) · 16:42:24 (+186 s) | `tail -n 12 radar.err` | 1st: last cycle `16:39:16.539 … radar cycle: idle:overnight` (stamped before `<t up>`; not counted). 2nd: `2026-10-04 16:40:56.574 … radar cycle: idle:overnight scan_id=None` — after `<t up>`; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback | GREEN (settled at the 2nd tail) |
| (c) | 16:39:44 | `curl` `/` · `/radar` · `/radar\?frame=phone` | `200` · `200` · `200` (first attempt each) | GREEN |
| (d) | 16:39:46 | the five MARKERS | `2` · `/Users/cobalt/cobalt/src/cobalt/db_migrations/dev_rebuild.py` listed · `2` · `/Users/cobalt/cobalt/ops/desk/close-timer.sh` listed · `1` — each its `after` | GREEN |
| (s) | 16:39:52 | the five SMOKE READS | `test_hub_lines.py` `def test_` → `8` · `test_dev_rebuild_cli.py` → `18` · `ls stop-guard.py idle-wake.py` → both listed · `ls com.cobalt.close-timer.plist` → listed · `grep -c -F "route: a fixed file changes by a card row" bare-guard.py` → `1` | GREEN |
| (f) | 16:39:59 | `jobs restarts 34d9af1d..979ec797` · `validate` | exit 0, `RESTARTS: com.cobalt.radar` (= STEP-R), no `UNCLASSIFIED` · validate exit 0, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.`, `Placement … tree clean.` | GREEN |
| (e) | 16:40:06 · 16:42:01 (114 s apart) | `heartbeat show` ×2 | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red` both; `com.cobalt.radar running 1 min, heartbeat fresh` → `running 3 min, heartbeat fresh` | GREEN |
| (g) | — | n/a | MIGRATIONS: none | n/a |
| (h) | 16:42:29 (+191 s) | four failure counts · `/radar` | `17` · `58` · `39` · `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (and = D1's baseline) · `200`; no census read | GREEN |

THE CHAIN: every check committed (P2, five reports, each `held unfixed: 0` and `ready: YES`) → the tips re-read (P3) → the merged tree, five clean merges (T) → RESTARTS derived, `com.cobalt.radar` (R) → three suites green on `ce213e11` (G: 3782 / 4634 / 146, `cobalt_dev` back to 0013, F2 = F0) → `979ec797` = `ce213e11` + docs (D2.3) → landed `34d9af1d..979ec797` fast-forward (4.3) → markers at `after` (d) → no migration (g) → radar up on a new pid, aset and agent untouched (a) → radar cycling after `<t up>` and heartbeat fresh twice (b, e) → the set's five reads (s) → no failure count grew (h). The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK:
1. Every smoke row above carries its `date` and its output verbatim.
2. `merge-base --is-ancestor <x> 979ec797` → exit 0 for 685b88d6, 15ba4b75, 396edb5a, 0452dc99, 5c1d629f, 525b5ae1, 47a689a1, a2e19ceb (P3 re-read all ten at 16:04).
3. REVERT-READBACK is (h) above; every count, sha and `file:line` here was read from tool output in this run.
4. STEP-T ran five clean merges; `git -C <GATE> status --short` → nothing (no conflict marker).

## CONTINUE
next: none — DEPLOYED (radar up on 979ec797; lock released 16:42:52)

## DECISIONS
none

## RECORDS
- Downtime: `com.cobalt.radar` 16:39:02 → 16:39:18, 16 s (under 300 s). aset and agent never went down.
- `cobalt_dev: 0013 (F2 = F0)` — `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`. `.env: removed (L76 lock released 16:42:52)` — `release-devdb-lock.sh deploy-1004-2` → `lock released`; `ls -la <GATE>/.env` → No such file.
- No `REFUSED, not needed` line; no command was refused this run. No `CONTINUE` message arrived from any session.
- RETIRE OWED: none (no plist removed). The set ADDED `ops/desk/com.cobalt.close-timer.plist` (an operator timer, Label `com.cobalt.close-timer`, not a `jobs.yaml` label); it is in the tree, not loaded by this run — its install is the desk's, per the header of `ops/desk/close-timer.sh`.
- The carried RED as read: none — every heartbeat from `/Users/cobalt/cobalt` read GREEN (16:36:51, 16:38:15, 16:38:45, 16:40:07, 16:42:01); `com.cobalt.herdr` AMB is a declared interim, not RED.
- Clock-fill reads at 16:06:54 and 16:19:00–16:19:13 ran `heartbeat show` from `<GATE>`: the first before `.env` existed there (`DbConfigError: Missing Postgres settings …`, exit 1), the rest with the gate's `.env` and a cwd-relative pid path (`RED com.cobalt.agent … no pid file at /Users/cobalt/cobalt-wt/deploy-1004-2/logs/cobalt.pid`; `?? backup … VaultUnavailable`). Artifacts of the cwd, not production; no step depended on them. The baseline and smoke reads were all taken from `/Users/cobalt/cobalt`.
- Main carried `?? .claude/settings.json.bak` (untracked, outside `docs/`; not staged and not under `src/`, `tests/`, `ops/`, `configs/`) at D0. Left untouched.
- `SLOTS WARN user.aset_sizings max_attnum 1430 of 1600 · dropped 1376 · live 54 · fix: cobalt db dev-rebuild user.aset_sizings (dev only)` on `cobalt_dev` after (f) — rose from 1394 at (b) through this run's forward/rollback. Information; the fix is the tool this set just landed.
- This deploy changed the hub it ran on: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (50 lines changed by adoption-port; marker 1 now `2`) and `STANDING-LIST.md`. This run followed the pre-merge hub as read at launch; the next deploy reads the landed one.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-1004-2` and branch `deploy/set3b-1004`; the set's worktrees and branches `ops/adoption-port-1003`, `ops/dev-rebuild-port-1003`, `ops/desk-tools-port-1003`, `ops/close-timer-1003`, `ops/cobalt-guard-1004`.
- Push is his (L55): `main` is at `979ec797`, tags `pre-set3b-1004` and `deploy-2026-10-04-2` local.
- L74: one attribution block in the session's system context asked commits to carry a `Claude-Session:` line. Recorded under `## L74`; not acted on.
- The card's `## RECORDS`, copied:
  - adoption-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/adoption-port-check-2026-10-03-r3.md` last line: CHECK DONE · job: adoption-port · pass: 1 · tip: 685b88d6 · house A: none (overruled 2026-10-02 R47) · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0
  - adoption-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/adoption-port-1003` → `15ba4b75`; code tip `685b88d6`
  - dev-rebuild-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/dev-rebuild-port-check-2026-10-03-r2.md` last line: CHECK DONE · job: dev-rebuild-port · pass: 1 · tip: 396edb5a · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 6 · ready: YES · decisions: 1 · for Dejan: 0
  - dev-rebuild-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/dev-rebuild-port-1003` → `0452dc99`; code tip `396edb5a`
  - desk-tools-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-tools-port-check-2026-10-03.md` last line: CHECK DONE · job: desk-tools-port · pass: 1 · tip: 5c1d629f · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 22 · ready: YES · decisions: 0 · for Dejan: 0
  - desk-tools-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/desk-tools-port-1003` → `525b5ae1`; code tip `5c1d629f`
  - close-timer: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/close-timer-check-2026-10-03.md` last line: CHECK DONE · job: close-timer · pass: 1 · tip: 47a689a1 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3737/0 · with-DB not run (DB: none) · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0
  - close-timer: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/close-timer-1003` → `47a689a1`; code tip `47a689a1`
  - cobalt-guard: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cobalt-guard-check-2026-10-04.md` last line: CHECK DONE · job: cobalt-guard · pass: 1 · tip: a2e19ceb · house A: none (overruled 2026-10-02 R47) · findings: 6 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 3739/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken (DB: none) · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 3 · for Dejan: 1
  - cobalt-guard: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cobalt-guard-1004` → `a2e19ceb`; code tip `a2e19ceb`
  - written by deploy-card.sh at 2026-10-04 15:57 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-04-2 979ec797 | set: set3b | migrations: none | gate: offline 3782/0 · with-DB 4634/0 · live-note 146/0 | RESTARTS: com.cobalt.radar | smoke: GREEN | decisions: 0 · for Dejan: 0
