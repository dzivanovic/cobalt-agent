# deploy-launcher-fixround-1005 · SET: workflow2 · MIGRATIONS: none

## §0 Headline
- DEPLOYED `deploy-2026-10-05-launcher-fixround` at 19:00:58: `main` ef3e40ec → 21a06ce3, fast-forward. The launcher fix round (`ops/launcher-fixround-1005` @ a545a4d8) is live.
- Gate GREEN on 1ee33bcf: offline 3786/0 · with-DB 4639/0 · live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0); lock released.
- RESTARTS: none. No resident went down (aset 13209, radar 28249, agent 22243 unchanged); downtime none; migrations none.
- Smoke GREEN: four markers 0 → 1, curls 200, radar cycled at 19:03:38, failure counts flat, heartbeat GREEN twice.

## L74
none arrived inside a tool result. A harness system note in this session asked for a `Claude-Session:` trailer on commits; per L74 / this hub, the commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/47-deploy-launcher-fixround-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/47-deploy-launcher-fixround-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/47-deploy-launcher-fixround-card.md" · 0 · ea8906451c597946ccf2704bd1d85e6e78b96ab0
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/47-deploy-launcher-fixround-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
R412's "production HOLD", read in `cto-2026-10-05-words.md:27`: "Production stays on hold until the workflow set is deployed." This card is part of the workflow set (LADDER: R387), so the hold does not bar it.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| P1 | `date` | 0 | Mon Oct  5 18:29:30 EDT 2026 |
| first launch | `ls -la "<REPORT>"` | 1 | No such file or directory |
| P2 | `tail -n 3 ".../launcher-checks-check-2026-10-05-r2.md"` | 0 | `CHECK DONE · job: launcher-checks · pass: 1 · tip: a545a4d8 · … · held unfixed: 0 · open: 0 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 152813` |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "<check>"` | 0 | 6bf0b815c86ac3ae11567bf32f890efea7dc37bd |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<check>"` | 0 | nothing |
| P3 | `rev-parse --short=8 a545a4d8` | 0 | a545a4d8 |
| P3 | `rev-parse --short=8 ops/launcher-fixround-1005` | 0 | a545a4d8 |
| P3 | `merge-base --is-ancestor a545a4d8 ops/launcher-fixround-1005` | 0 | — |
| P3 | `diff --stat a545a4d8 ops/launcher-fixround-1005 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` (lock free) |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-launcher-fixround-1005` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = 59d271c9 |
| P5 | `merge-base --is-ancestor 59d271c9 main` | 0 | — |
| P5 | `log --oneline main..deploy/deploy-launcher-fixround-1005` | 0 | empty |
| P6 | marker 1 `grep -c -F "is not committed and unmodified" …/deploy-step0.sh` | 1 | 0 (before 0) |
| P6 | marker 2 `grep -c -F "Fix-round row" …/DEPLOY-HUB.md` | 1 | 0 (before 0) |
| P6 | marker 3 `grep -c -F "On a fix-round row (a small fix after the check, his R376, L75)" …/CARD.md` | 1 | 0 (before 0) |
| P6 | marker 4 `grep -c -F "\| fix report \|" …/deploy-card.sh` | 1 | 0 (before 0) |
| P7 | `diff --stat main a545a4d8 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 13209 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 28249 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit a545a4d8` → `Auto-merging docs/40 - DevDocs/prompts/DEPLOY-HUB.md` / `Merge made by the 'ort' strategy.` (8 files, 586 insertions, 11 deletions)
- `<m1>` = `git -C <GATE> rev-parse --short=8 HEAD` → 1ee33bcf
- `log --oneline --merges --first-parent 59d271c9..deploy/deploy-launcher-fixround-1005` → `1ee33bcf Merge commit 'a545a4d8' into deploy/deploy-launcher-fixround-1005`
- `merge-base --is-ancestor a545a4d8 deploy/deploy-launcher-fixround-1005` → exit 0
- `diff --stat 59d271c9 deploy/deploy-launcher-fixround-1005 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C `diff --stat 59d271c9 deploy/deploy-launcher-fixround-1005 -- configs ops` → `ops/desk/deploy-card.sh | 6 +++---` · `ops/desk/deploy-step0.sh | 22 ++++` · `ops/desk/desk-launch.sh | 22 +++-` · `3 files changed, 46 insertions(+), 4 deletions(-)`. No plist added, modified or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after a fresh `.venv` create, `Installed 253 packages in 919ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = none (EMPTY: no resident goes down; the merge lands with residents up).

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat a545a4d8 1ee33bcf -- . ":(exclude)docs"` → `ops/desk/preflight.sh | 54`, `tests/ops/test_desk_launch_brain.py | 2`, `tests/ops/test_preflight.py | 78` (main moved since the check's base) → the clause does not hold; the gate runs whole (`--deploy`).
- Deselects: none (build report line 216: "no `--deselect`: this build adds no with-DB test"); no `--tickers`, no `--migration`.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 157 skipped in 15.47s` (0 failed; every skip is a with-DB skip: "Postgres env settings not available" / "requires_db").
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-launcher-fixround-1005 all --deploy` (background) → exit 0. Verdict lines, whole:
```
offline 3786/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4639/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-launcher-fixround-1005-all-20261005-183114.log
```
- (a) offline: log :829 `3786 passed, 756 skipped, 1 xfailed` → `<p>` = 3786.
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :846); proof-only at 0013, nothing CHANGED.
- (c) PASS 1 whole: log :1051 `4466 passed, 7 skipped, 67 deselected, 3 xfailed` → `<d1>` = 4466. The 7 SKIPPED lines above are each inside the allowed set: test_cards_picks.py:388, :401; test_radar_evaluate.py:695; test_replay_line.py (reason names `COBALT_TEST_LIVE_DRC`); test_s3_c4_experiments.py:95 = `test_x14_live_his_template_strips_to_the_committed_fixture` (read at `<GATE>/tests/cobalt/test_s3_c4_experiments.py:95-96`); test_catalyst.py:365; test_predicate.py:262.
- (c2) `dev forward: APPLIED 18:53:20` (log :1053).
- (c3) PASS 2: log :1610 `173 passed, 1 deselected` → `<d2>` = 173; `with-DB 4639/0` = 4466 + 173.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :1675) = F0 · `cobalt_dev: 0013 — F2 = F0` (log :1726).
- THE RELEASE: log :1727–1731 `release-devdb-lock.sh deploy-launcher-fixround-1005` → `lock released`, `.env` No such file. `.env: removed (L76 lock released, log :1728; gate ended before 18:58:18)`. Verified: `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-launcher-fixround-1005" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (lock dir absent).
- (e) LIVE-NOTE: log :1797 `146 passed, 1 skipped` → `<l>` = 146; the one skip is the `COBALT_TEST_LIVE_DRC` replay_line skip (allowed); none names `COBALT_LIVE_VAULT_ROOT`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 1ee33bcf

## Deploy table
| step | command | result |
|---|---|---|
| D0 | `git -C /Users/cobalt/cobalt status --short --branch` | `## main...origin/main [ahead 169]`; ` M` lines: `.claude/settings.json` and five under `docs/40 - DevDocs/reports/`; `??` lines under `docs/40 - DevDocs/` plus `.claude/settings.json.bak` (see RECORDS); no staged line; no dirty `src/` `tests/` `ops/` `configs/` |
| D0 | `diff --stat 59d271c9 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D0 probe | `tag scratch-allow-probe-deploy-launcher-fixround-1005` · `tag -d …` | `Deleted tag 'scratch-allow-probe-deploy-launcher-fixround-1005' (was 59d271c9)` |
| D0 probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | `[main aa6c8e11] scratch: …` → `59d271c9 docs(desk): R452 deploy card 47 preflight r2 READY YES` |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-05-launcher-fixround` · `…/pre-deploy-launcher-fixround-1005` | exit 1 · exit 1 |
| D1 | `date` | Mon Oct  5 18:58:47 EDT 2026 |
| D1 `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 18:58:48 EDT)`; `OK radar scanning (aftermarket), members 50`; `OK com.cobalt.radar running 392 min, heartbeat fresh`; one `AMB com.cobalt.herdr unmanaged` (declared interim). No RED. |
| D1 `<val0>` | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK`; `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 `<jobs0>` | (validate) | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` |
| D1 | `COBALT_ENV=production uv run cobalt backup status` | `newest snapshot: 2.7 h old` |
| D1 | `launchctl print gui/501/com.cobalt.aset` | `state = running`, `<aset pid>` 13209 |
| D1 | `launchctl print gui/501/com.cobalt.radar` | `state = running`, `<radar pid>` 28249 |
| D1 | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 22243` | `Cobalt is ONLINE (PID: 22243).` · listed (`uv run src/cobalt_agent/main.py`) |
| D1 | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | last line `2026-10-05 18:57:21.254 \| INFO \| cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791240952793`; no traceback |
| D1 counts | `grep -c` × 8 | `<a0>` 42 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 58 · `<re0>` 39 · `<lc0>` 39 |
| D1 | `curl … http://127.0.0.1:5010/radar` | 200 |
| D1 markers | the four `## MARKERS` greps | 0 · 0 · 0 · 0 (each its `before`) |
| D1 migration | — | MIGRATIONS: none; no `<RB>`, no census, no proof-only |
| D2.0 | `add` + `commit -m "docs(report): deploy deploy-launcher-fixround-1005 — gate green on 1ee33bcf"` · `show --stat HEAD` | `[main ef3e40ec]`; one file, 146 insertions |
| D2.0 | `rev-parse --short=8 main` | `<pre-merge>` = ef3e40ec |
| D2.1 | `git -C <GATE> merge --no-edit main` | `Merge made by the 'ort' strategy.` (the report only) |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` · `rev-parse --short=8 21a06ce3^2` · `merge-base --is-ancestor 1ee33bcf 21a06ce3` | `<stack-final>` = 21a06ce3 · ef3e40ec · exit 0 |
| D2.3 | `diff --stat 1ee33bcf 21a06ce3 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D2.4 | `backup status` · `backup run` · `backup status` | `newest snapshot: 2.7 h old` → `backup: cobalt_brain dumped, 4846.8 MB` · `ssd: snapshot bb74760d — 0 new / 3 changed, 90.3 MB added, 1 pruned` → `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` | 19:00:37 · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 19:00:39 EDT)` (111 s after D1's 18:58:48; clock filled with four date + heartbeat pairs 19:00:14–19:00:34, each GREEN) |
| D2.6 | `date` · `tag pre-deploy-launcher-fixround-1005` | 19:00:43 · set at ef3e40ec |
| 4.1 | `date` | `<t down>` 19:00:58 (no resident goes down: `<restart set>` none) |
| 4.2 | — | nothing: empty set |
| 4.3 | `rev-parse --short=8 HEAD` · `merge --ff-only deploy/deploy-launcher-fixround-1005` | ef3e40ec = `<pre-merge>` · `Updating ef3e40ec..21a06ce3` / `Fast-forward` (8 files, 586 insertions, 11 deletions) |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`; `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.6 | — | nothing: empty set; `<t up>` = 4.3's `date` 19:00:58; downtime: none |
| 7.1 | `git -C /Users/cobalt/cobalt tag deploy-2026-10-05-launcher-fixround` | set at 21a06ce3, after green smoke |

CLOSE: `<pre-merge>` ef3e40ec → `<stack-final>` 21a06ce3 · tags `pre-deploy-launcher-fixround-1005` (ef3e40ec), `deploy-2026-10-05-launcher-fixround` (21a06ce3) · `<t down>` / `<t up>` none / none / 0 s (empty set) · uv sync: none in production (the gate worktree created its own `.venv` at STEP-R, `Installed 253 packages in 919ms`) · proof cost: none (no migration) · `migrations applied: none` · `<RB>` none · snapshot `bb74760d` (ssd) · `RESTARTS done: none`.

THE ROLLBACK STRING (the desk's; L54):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 21a06ce3`. No residents to take down: the set is empty (no Cobalt reader of these files).
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
| row | date | command | result |
|---|---|---|---|
| first | 19:00:58+ | the four failure counts | `<rp_up>` 17 · `<rpr_up>` 58 · `<re_up>` 39 · `<lc_up>` 39 (= D1) |
| (a) | 19:01:08 | `launchctl print` aset · radar · `cobalt.sh status` | aset `state = running` pid 13209 (SAME, outside the set) · radar `state = running` pid 28249 (SAME) · `Cobalt is ONLINE (PID: 22243).` (same; agent outside the set) — GREEN |
| (b) | 19:01:11 | `grep -c` Started / Traceback ×2 / TaxonomyConfigError | 42 = `<a0>` (aset outside the set) · 2 = `<ta0>` · 0 = `<tr0>` · 0 = `<tc0>` |
| (b) | 19:01:11 | `tail -n 30 /Users/cobalt/cobalt/logs/aset.err` | last line written 2026-10-05 09:44:31 (`cobalt.aset.daily_note:_write_unit:189 - [WRITE] updated …`); no new start (aset not in the set), no traceback |
| (c) | 19:01:11 | `curl` `/` · `/radar` · `/radar\?frame=phone` | 200 · 200 · 200 — GREEN |
| (d)/(s) | 19:01:18 | the four `## MARKERS` / `## SMOKE READS` greps | `deploy-step0.sh` 1 · `DEPLOY-HUB.md` 1 · `CARD.md` 1 · `deploy-card.sh` 1 — each exit 0, its `after` value / "a count of 1 or more" — GREEN |
| (f) | 19:01:18 | `COBALT_ENV=production uv run cobalt jobs restarts ef3e40ec..21a06ce3` | exit 0; same eight rows as STEP-R; `RESTARTS: none` = `<restart set>`; no `UNCLASSIFIED`. Validate as 4.5 (exit 0) — GREEN |
| (g) | — | — | no migration |
| (b) tail 1 | 19:02:31 | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` (`<t up>` + 93 s) | last line `2026-10-05 19:00:29.638 \| INFO \| cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791241141286` — before `<t up>`; not settled; no failure, no traceback |
| (e) 1 | 19:01:42 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 19:01:42 EDT)`; `com.cobalt.radar running 395 min, heartbeat fresh` |
| (e) 2 | 19:03:34 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 19:03:37 EDT)` (115 s after the first); `com.cobalt.radar running 396 min, heartbeat fresh`; no RED — GREEN. The clock between them was filled with date + heartbeat pairs, each GREEN. |
| (b) tail 2 | 19:03:59 | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` (`<t up>` + 181 s) | `2026-10-05 19:03:38.187 \| INFO \| cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791241329670` — stamped after `<t up>`; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → (b) settled GREEN (the third tail is not needed) |
| (h) | 19:04:07 | the four failure counts · radar Traceback · `curl /radar` | 17 · 58 · 39 · 39 = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew) · 0 = `<tr0>` · 200 — GREEN; no census reads (none on the card) |

THE CHAIN: every check committed (P2: `launcher-checks-check-2026-10-05-r2.md` at 6bf0b815, `held unfixed: 0`, `ready: YES`) → the tip re-read (P3: a545a4d8 = branch head) → the merged tree (T: 1ee33bcf, clean) → RESTARTS derived (R: none) → three suites green on 1ee33bcf (G: offline 3786/0, with-DB 4639/0, live-note 146/0) → `<stack-final>` 21a06ce3 = 1ee33bcf + the report only (D2.3) → the landed code (4.3: `Fast-forward` ef3e40ec..21a06ce3) → markers 0 → 1 (d) → no migration (g) → residents unchanged and up after the merge (a) → radar cycling (b, e) → the set's reads (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

## CONTINUE
OUTAGE STARTING 19:00:43 — residents of none going down (`<restart set>` EMPTY: no resident goes down; the merge lands with residents up); if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- 4.1–4.6 done; merged ef3e40ec..21a06ce3 at 19:00:58.
- 4.7 smoke GREEN 19:04:07; STEP-7 closed. next: none (the desk's cleanup and push, below).

## DECISIONS
none

## RECORDS
- Downtime: none (empty restart set); no line over 300 s.
- REFUSED, not needed: none. No `CONTINUE` message and no other session's message arrived.
- `cobalt_dev: 0013 (F2 = F0)`: F0 = F2 = `664 35 272c95bbb12241e3611e4b36326ccf87` (gate log :846, :1675).
- RETIRE OWED: none (no plist removed).
- Carried RED: none. Every heartbeat this run was GREEN; the one standing `AMB com.cobalt.herdr unmanaged` is a declared interim, not RED.
- D0: `?? .claude/settings.json.bak` is untracked on `main`. It is not on the accepted list (` M .claude/settings.json` is) and not on the refused list (staged, or dirty `src/` `tests/` `ops/` `configs/`), so it was not a stop. Recorded for the desk.
- D0: `## main...origin/main [ahead 169]` before this run; push is his (L55).
- CLEANUP OWED (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-launcher-fixround-1005` and branch `deploy/deploy-launcher-fixround-1005`; the set's branch `ops/launcher-fixround-1005` and its worktree if one exists. The gate worktree holds a `.venv` created at STEP-R.
- Desk RECORDS (copied from the card):
  - launcher-fixround: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-checks-check-2026-10-05-r2.md` last line: CHECK DONE · job: launcher-checks · pass: 1 · tip: a545a4d8 · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3786/0 · with-DB 857/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 152813
  - launcher-fixround: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-fixround-1005` → `a545a4d8`; code tip `a545a4d8` (the check's own fix on top of the build's `dc2a80b4`; BASE `5fb0ddf5`)
  - G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
  - `DEPLOY-HUB.md` is among the shipped files (one inserted line after P2, the F3 hub line). Card 41 deployed first (`1ff72b72`), so main's `DEPLOY-HUB.md` differs from this branch's merge base `5fb0ddf5`. The deploy merges main into the tree and that merge is clean, proved by reading, not running. — This run confirms it by running: STEP-T printed `Auto-merging docs/40 - DevDocs/prompts/DEPLOY-HUB.md` / `Merge made by the 'ort' strategy.`, no conflict.
  - The fix-round column (`fix report`) is added by this deploy, so `## SHIPS` carries main's six columns; the row needs no fix report because the check's `tip:` equals the code tip `a545a4d8`.
  - OWED, a later card, not part of this deploy (the check's DECISIONS 1): `DEPLOY-HUB.md:58` (P2) says the literals are those "the row's last column names"; on the seven-column `## SHIPS` shape the last column is `fix report`, and the literals are in `its stop line must carry`, the column before it (`CARD.md:47` and the scripts read that column). One-phrase hub fix: "the `its stop line must carry` column".
- PRE-STOP SELF-CHECK (K25): (1) every smoke row above carries its `date` and its output verbatim; (2) a545a4d8 re-read at P3 (= branch head), and `merge-base --is-ancestor a545a4d8 21a06ce3` → exit 0; (3) REVERT-READBACK (h) is shown: 17 · 58 · 39 · 39 at 19:04:07, and every count, sha and `file:line` here was read from this run's tool output; (4) no conflict marker: STEP-T and D2.1 each printed `Merge made by the 'ort' strategy.`
- THE RELEASE: done by the gate at STEP-G (log :1728 `lock released`); `<GATE>/.env` absent, lock dir absent.
- Tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 09038999-57b4-4c75-8aae-81f0fedb89b4` → `context 198021 of 400000 — ok`.

DEPLOYED deploy-2026-10-05-launcher-fixround 21a06ce3 | set: workflow2 | migrations: none | gate: offline 3786/0 · with-DB 4639/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 198021
