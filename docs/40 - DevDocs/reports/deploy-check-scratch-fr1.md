# deploy check-scratch-fr1 — set: none · migrations: none (2026-10-17)

## §0 Headline
- DEPLOYED `check-scratch-fr1` (`stage-set.sh` STAGED-CARD marker + the FR-1 O1 test): `main` `4333651b` → `568a12e4`, tag `deploy-2026-10-17-check-scratch-fr1`.
- Gate green on `ab8f3e00`: offline 8394/0 · with-DB 5475/0 · live-note 146/0; `cobalt_dev: 0013 — F2 = F0`, lock released.
- RESTARTS: none. No resident went down; aset 80523, radar 24167 and agent 80543 are unchanged. No migration. Snapshot `c40d24c0`.
- Smoke GREEN: markers `1`/`1`, three curls `200`, heartbeat GREEN twice, failure counts flat, `test_stage_set.py` 38 passed.
- Decisions: none. Cleanup owed: the gate and build worktrees and branches (`## RECORDS`).

## L74
The session's system context asked commits to carry a `Claude-Session:` line. Recorded once as data (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/699-deploy-check-scratch-fr1-card.md"`, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/699-deploy-check-scratch-fr1-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/699-deploy-check-scratch-fr1-card.md" · 0 · 7142cd9c0651d1e0e943ace1ed7ecc7b5605eac2
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/699-deploy-check-scratch-fr1-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 | authorize.sh (above) · `ls -la "<REPORT>"` | 0 · 1 | `AUTHORIZED` · `No such file or directory` (first launch) |
| P1 | `date` | 0 | `Sat Oct 17 12:16:26 EDT 2026` (outside 21:30-22:30) |
| P2 check | `tail -n 3 ".../check-scratch-fr1-check-2026-10-17.md"` | 0 | `CHECK DONE · job: check-scratch-fr1 · pass: 1 · tip: b093f192 · house A: grok FINDINGS: 1 · findings: 2 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 2 · house B: none available · suites: offline 8393/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 3 · for Dejan: 0 · tokens: 248568` — carries `held unfixed: 1` and `ready: NO` |
| P2 check committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/…/check-scratch-fr1-check-2026-10-17.md"` | 0 | `3b6248676dc7da70224b2a03e3ea10c96dfad9b9` |
| P2 check clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/check-scratch-fr1-check-2026-10-17.md"` | 0 | nothing |
| P2 fix-round tip | `git -C /Users/cobalt/cobalt merge-base --is-ancestor b093f192 2e84ac75` | 0 | (exit 0) |
| P2 fix report | `tail -n 3` on main path | 1 | `No such file or directory` (the report lives on the branch; read at the head next row) |
| P2 fix report at head | `git -C /Users/cobalt/cobalt show "3879fdbb:docs/…/check-scratch-fr1-build-2026-10-17.md"` | 0 | last line `BUILT · job: check-scratch-fr1 · tip: 2e84ac75 \| on 79f6f2f3 \| migration: none \| offline 8394/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 1 of 1 \| self-check: 3 of 3 \| decisions: 1 · for Dejan: 0 · tokens: 108345`; holds `FIXED: O1 — tests/ops/test_stage_set.py::test_o1_legacy_a_higher_numbered_build_copy_is_not_the_prior_card` and `SETTLED: A1 — R1786` |
| P2 fix report committed | `git -C /Users/cobalt/cobalt log -1 --format=%H 3879fdbb -- "docs/…/check-scratch-fr1-build-2026-10-17.md"` | 0 | `3879fdbb89bb74a912d17bcdd4f9eafd01d97fde` |
| P2 fix report clean | `git -C /Users/cobalt/cobalt-wt/check-scratch-fr1 diff --stat -- "docs/…/check-scratch-fr1-build-2026-10-17.md"` · `git -C /Users/cobalt/cobalt-wt/check-scratch-fr1 status --short --branch` · `rev-parse --short=8 HEAD` | 0 · 0 · 0 | nothing · `## ops/check-scratch-fr1` · `3879fdbb` |
| P2 held ids | check `## RUNS` / `## FIXES` / `## OPEN` | — | `HELD, NOT FIXED`: `O1` only (`:193`, `:197`, `:216`); A1 is `REJECTED` (`:194`, `:217`), not held |
| P2 FIXED test at tip | `grep -n -F "test_o1_legacy_a_higher_numbered_build_copy_is_not_the_prior_card" /Users/cobalt/cobalt-wt/check-scratch-fr1/tests/ops/test_stage_set.py` | 0 | `665:def test_o1_legacy_a_higher_numbered_build_copy_is_not_the_prior_card(job):` |
| P2 not xfail | `grep -c -F "xfail" …/tests/ops/test_stage_set.py` | 1 | `0` |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 2e84ac75` | 0 | `2e84ac75` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/check-scratch-fr1` | 0 | `3879fdbb` (= `TIP`) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 2e84ac75 3879fdbb` | 0 | (exit 0) |
| P3 docs only | `git -C /Users/cobalt/cobalt diff --stat 2e84ac75 3879fdbb -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/check-scratch-fr1` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `7142cd9c` = `<m0>` |
| P5 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 7142cd9c main` | 0 | (exit 0) |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/check-scratch-fr1` | 0 | nothing |
| P6 marker 1 | `grep -c -F "STAGED-CARD write failed" /Users/cobalt/cobalt/ops/desk/stage-set.sh` | 1 | `0` (= before) |
| P6 marker 2 | `grep -c -F "test_mk1_staging_writes_the_marker_naming_the_card" /Users/cobalt/cobalt/tests/ops/test_stage_set.py` | 1 | `0` (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 3879fdbb -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 80523` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 24167` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is ONLINE (PID: 80543).` |

## THE TREE
- `git -C <GATE> merge --no-edit 3879fdbb` → `Merge made by the 'ort' strategy.` (`ops/desk/stage-set.sh | 70`, `tests/ops/test_stage_set.py | 159`, the two build-report docs; `4 files changed, 402 insertions(+), 34 deletions(-)`).
- `git -C <GATE> rev-parse --short=8 HEAD` → `ab8f3e00` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 7142cd9c..deploy/check-scratch-fr1` → `ab8f3e00 Merge commit '3879fdbb' into deploy/check-scratch-fr1` (one line, one head).
- `merge-base --is-ancestor 2e84ac75 deploy/check-scratch-fr1` → exit 0; `merge-base --is-ancestor 3879fdbb deploy/check-scratch-fr1` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 7142cd9c deploy/check-scratch-fr1 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 7142cd9c deploy/check-scratch-fr1 -- configs ops` → ` ops/desk/stage-set.sh | 70 +++++++++++++++++++++++++++++++++------------------` · ` 1 file changed, 46 insertions(+), 24 deletions(-)`. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 7142cd9c deploy/check-scratch-fr1` → `STEP-C: ADMITTED 0` (exit 0). `<launchd set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → (after the gate's first `uv` venv sync: `Creating virtual environment at: .venv` · `Installed 254 packages in 995ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/check-scratch-fr1-build-2026-10-17.md	A	DOCS	-
docs/40 - DevDocs/reports/check-scratch-fr1-build-2026-10-17.result	A	DOCS	-
ops/desk/stage-set.sh	M	operator script; no Cobalt reader	-
tests/ops/test_stage_set.py	M	test/documentation; no resident	-
RESTARTS: none
```
Exit 0, no `UNCLASSIFIED`. `<restart set>` = EMPTY (none): no resident goes down; the merge lands with residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold (the check's stop line carries `with-DB 0/0`, and `<m1>` differs from the check's tip `b093f192` by the FR-1 test): the gate runs whole.
- (a0) `ls -la <GATE>/.env` → `No such file or directory` · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.38s` (0 failed; every skip a `Postgres env settings not available` / `requires_db` skip).
- `ls -la <GATE>/.env` → `No such file or directory` · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-check-scratch-fr1 all --deploy --deploy-gate` (no `--deselect`: the build report names none; no `--tickers`: TICKERS none; no `--migration`: MIGRATIONS none) → exit 0, verdict whole:
```
tests/ops: run (deploy gate)
offline 8394/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5475/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-check-scratch-fr1-all-20261017-121849.log
```
- (c) every SKIPPED line inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = the decorator of `96:def test_x14_live_his_template_strips_to_the_committed_fixture():` (`grep -n -F` in `<GATE>`). `grep -n -F "OUTSIDE the allowed set" <log>` → nothing.
- (c2) FORWARD: no migration above `0013` on this set (MIGRATIONS: none); the gate's `LEVEL 0013`.
- (f) `cobalt_dev: 0013 — F2 = F0`: log `976:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `2115:F2: 664 35 272c95bbb12241e3611e4b36326ccf87`.
- THE RELEASE: `.env: removed (L76 lock released, log line 2169 `lock released`)`; `ls -la <GATE>/.env` → `No such file or directory`; `grep -c -x -F "deploy-check-scratch-fr1" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) live-note `146/0`; the only skip in it names `COBALT_TEST_LIVE_DRC` (inside the set).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on ab8f3e00 — offline 8394/0 · with-DB 5475/0 · live-note 146/0 (13:03:19 EDT)

## Deploy table
| step | command | result verbatim |
|---|---|---|
| D0 main | `git -C /Users/cobalt/cobalt status --short --branch` | first line `## main...origin/main [ahead 80]`; every line ` M` / `??` under `docs/40 - DevDocs/`, plus ` M .claude/settings.json` and `?? .claude/settings.json.bak` (untracked, not under src/tests/ops/configs; recorded); no staged line |
| D0 moved | `git -C /Users/cobalt/cobalt diff --stat 7142cd9c main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D0 probe | `tag scratch-allow-probe-check-scratch-fr1` · `tag -d …` · `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | (silent) · `Deleted tag 'scratch-allow-probe-check-scratch-fr1' (was 7142cd9c)` · `[main 1525dfac] scratch: allowlist probe (reverted next line)` · (silent) · `7142cd9c docs(desk): deploy card 699 check-scratch-fr1 (R1791)` |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-17-check-scratch-fr1` · `… refs/tags/pre-check-scratch-fr1` | exit 1 · exit 1 |
| D1 date | `date` | `Sat Oct 17 13:04:01 EDT 2026` |
| D1 `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-17 13:04:02 EDT)`; `OK   radar                    idle (overnight)`; `OK   com.cobalt.aset              running   loaded, pid 80523 [launchd probe]`; `OK   com.cobalt.agent             running   pid 80543 alive …`; `OK   com.cobalt.radar             running   running 1703 min, heartbeat fresh`; one `AMB  com.cobalt.herdr             unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) …` (declared interim, not RED) |
| D1 `<val0>` | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`; `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 backup | `COBALT_ENV=production uv run cobalt backup status` | `newest snapshot: 5.7 h old` |
| D1 aset | `launchctl print gui/501/com.cobalt.aset` | `state = running` · `pid = 80523` = `<aset pid>` |
| D1 radar | `launchctl print gui/501/com.cobalt.radar` | `state = running` · `pid = 24167` = `<radar pid>` |
| D1 agent | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 80543` | `  Cobalt is ONLINE (PID: 80543).` · `80543 ??         0:00.03 uv run src/cobalt_agent/main.py` |
| D1 radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | last `2026-10-17 13:03:28.966 \| INFO     \| cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (8 such lines, 100 s apart) |
| D1 counts | `grep -c` × 8 | `<a0>` 281 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39 |
| D1 curl | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | `200` |
| D1 markers | the two `## MARKERS` | `0` · `0` (= before) |
| D1 launchd / migration | — | `<launchd set>` empty; MIGRATIONS none: no `<RB>`, no proof-only |
| D2.0 | `deploy-shipped.sh --moved 7142cd9c "<card>"` · `add` · `commit … -- "<REPORT>"` · `show --stat HEAD` · `rev-parse --short=8 main` | nothing · (silent) · `[main 4333651b] docs(report): deploy check-scratch-fr1 — gate green on ab8f3e00` · the one file `.../reports/deploy-check-scratch-fr1.md \| 144 +++` · `4333651b` = `<pre-merge>` |
| D2.1 | `git -C <GATE> merge --no-edit main` | `Merge made by the 'ort' strategy.` (the report only) |
| D2.2 | `rev-parse --short=8 HEAD` · `rev-parse --short=8 568a12e4^2` · `merge-base --is-ancestor ab8f3e00 568a12e4` | `568a12e4` = `<stack-final>` · `4333651b` · exit 0 |
| D2.3 | `git -C /Users/cobalt/cobalt diff --stat ab8f3e00 568a12e4 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D2.4 | `backup status` · `backup run` · `backup status` | `newest snapshot: 5.7 h old` · `backup: cobalt_brain via pg_dump inside cobalt_memory — 8900.8 MB` · `ssd: snapshot c40d24c0 — 0 new / 2 changed, 21.8 MB added, 1 pruned` · `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` | `Sat Oct 17 13:06:07 EDT 2026` · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-17 13:06:08 EDT)` (126 s after D1's; aset pid 80523, agent 80543, radar `running 1705 min, heartbeat fresh`; no new RED) |
| D2.6 | `date` · `tag pre-check-scratch-fr1` · `rev-parse --short=8 pre-check-scratch-fr1` | `Sat Oct 17 13:06:13 EDT 2026` · (silent) · `4333651b` |
| 4.1 / 4.2 | — | empty `<restart set>`: no bootout, no orphan-clean, no agent stop |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` · `git -C /Users/cobalt/cobalt merge --ff-only deploy/check-scratch-fr1` · `date` | `4333651b` · `Updating 4333651b..568a12e4` / `Fast-forward` (`ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`, two build-report docs; `4 files changed, 402 insertions(+), 34 deletions(-)`) · `Sat Oct 17 13:06:32 EDT 2026` = `<t up>` |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` (= `<jobs0>`); `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.6 / 4.6L | — | nothing to bootstrap (empty `<restart set>`, empty `<launchd set>`); downtime: none |
| 7.1 | `git -C /Users/cobalt/cobalt tag deploy-2026-10-17-check-scratch-fr1` | (silent), after the green smoke |

CLOSE: `4333651b` (`<pre-merge>`) → `568a12e4` (`<stack-final>`) · tags `pre-check-scratch-fr1` at `4333651b`, `deploy-2026-10-17-check-scratch-fr1` at `568a12e4` · `<t down>` / `<t up>` / seconds: none (empty set; `<t up>` = 13:06:32) · uv sync: none on `main` · proof cost: none (no migration) · `migrations applied: none` · `<RB>`: none · snapshot `c40d24c0` · `RESTARTS done: none` · `LAUNCHD done: none` · BOOTSTRAP OWED: none.
ROLLBACK STRING (the desk's): 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 568a12e4` (no resident to take down: `<restart set>` empty; no `<launchd set>` label). 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
`<t up>` = 4.3's `date` `Sat Oct 17 13:06:32 EDT 2026` (empty set). First calls: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1).

| row | `date` | command | result verbatim |
|---|---|---|---|
| (a) | 13:06:46 | `launchctl print gui/501/com.cobalt.aset` · `…/com.cobalt.radar` · `/Users/cobalt/cobalt/cobalt.sh status` | `state = running` `pid = 80523` (SAME as D1, outside the set) · `state = running` `pid = 24167` (SAME) · `  Cobalt is ONLINE (PID: 80543).` (SAME) |
| (b) | 13:06:50 | `grep -c "Started server process" aset.err` · `tail -n 30 aset.err` · Traceback aset / radar · TaxonomyConfigError | `281` (= `<a0>`, aset outside the set) · last line `2026-10-16 11:24:51.365 \| INFO     \| cobalt.vaultwrite.writer:_purge_once:482 - vault_writes: purged 1 row(s) past 30-day retention` (no restart, as expected) · `217` / `0` (= baseline) · `0` (= baseline) |
| (c) | 13:06:56 | `curl … /` · `curl … /radar` · `curl … /radar\?frame=phone` | `200` · `200` · `200` |
| (d) | 13:06:56 | `grep -c -F "STAGED-CARD write failed" …/ops/desk/stage-set.sh` · `grep -c -F "test_mk1_staging_writes_the_marker_naming_the_card" …/tests/ops/test_stage_set.py` | `1` · `1` (= after) |
| (e) 1 | 13:07:01 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-17 13:07:01 EDT)`; `OK   com.cobalt.radar             running   running 1706 min, heartbeat fresh`; the same `AMB  com.cobalt.herdr` line as `<hb0>` |
| (f) | 13:07:06 | `COBALT_ENV=production uv run cobalt jobs restarts 4333651b..568a12e4` · `COBALT_ENV=production uv run cobalt validate` | the four rows of STEP-R, `RESTARTS: none` (= `<restart set>`), no `UNCLASSIFIED`, exit 0 · exit 0, `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` (as 4.5) |
| (g) | — | — | no migration |
| (b) radar | 13:08:03 | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` (`<t up>` + 91 s) | last `2026-10-17 13:06:49.003 \| INFO     \| cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`, stamped after `<t up>`; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback in the tail → GREEN, settled on the first tail |
| (e) 2 | 13:08:51 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-17 13:08:54 EDT)` (113 s after (e) 1); `OK   com.cobalt.radar             running   running 1708 min, heartbeat fresh`; no RED |
| (h) | 13:09:32 | the four counts · `curl … /radar` | `18` · `60` · `43` · `39` (= `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, none grew) · `200`; no `census` line on the card |
| (s) | 13:07:06 | `uv run pytest -q tests/ops/test_stage_set.py` (the card's `## SMOKE READS` line, on the merged `main` tree) | `38 passed, 15 warnings in 15.59s` → `0 failed` = green; exit 0. The gate's tests/ops pass also ran it (`tests/ops: run (deploy gate)`, `offline 8394/0`) |

THE CHAIN: every check committed (P2: check `3b624867…`, fix report at `3879fdbb`, O1 FIXED) → the tips re-read (P3: `2e84ac75`, `3879fdbb`) → the merged tree (T: `ab8f3e00`, one merge, no migration) → RESTARTS derived (R: none) → three suites green on `ab8f3e00` (G: offline 8394/0 · with-DB 5475/0 · live-note 146/0) → `<stack-final>` `568a12e4` = `<m1>` + docs (D2.3) → the landed code (4.3: `4333651b..568a12e4`) → markers `1` · `1` (d) → no migration (g) → residents unchanged after the merge (a) → radar cycling (b, e) → the set's read `38 passed` (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK: (1) every smoke row above is quoted with its `date`. (2) `2e84ac75` and `3879fdbb` re-read at P3; `merge-base --is-ancestor 2e84ac75 568a12e4` → exit 0, `merge-base --is-ancestor 3879fdbb 568a12e4` → exit 0. (3) REVERT-READBACK (h) shown; every count, sha and line number was re-read from tool output this run (`rev-parse --short=8 main` → `568a12e4`). (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`); `grep -c -F "<<<<<<<"` over `ops/desk/stage-set.sh` and `tests/ops/test_stage_set.py` on `main` → `0` · `0`. 4 of 4.

## CONTINUE
next: STEP-D2 (D0, D1 done; D2.0 `deploy-shipped.sh --moved 7142cd9c "<card>"` → printed nothing; this report commit is D2.0)
OUTAGE STARTING 13:06:13 EDT — residents of none (empty restart set) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
next: none (merged 13:06:32 with residents up; smoke GREEN 13:09:32; tagged)

## DECISIONS
none

## RECORDS
- L74: the session's system context asked commits to carry a `Claude-Session:` line; recorded under `## L74`, not acted on. Both commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- Downtime: none (empty `<restart set>`; no resident went down).
- `cobalt_dev: 0013 (F2 = F0)` — `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` = `F2`; lock released by the gate, `.env` gone, lock dir absent.
- RETIRE OWED: none. BOOTSTRAP OWED: none. Carried RED: none (`<hb0>` GREEN; the herdr AMBER is the declared `launchd_unmanaged` interim, present before and after).
- D0: `?? .claude/settings.json.bak` is on `main` untracked. It is not under src/, tests/, ops/ or configs/ and not staged, so it is not refused; recorded for the desk.
- P2: the fix report is not on `main` before the merge; it was read at the branch head `3879fdbb` (`git show`) and in the builder worktree `/Users/cobalt/cobalt-wt/check-scratch-fr1` (clean, HEAD `3879fdbb`).
- (s): the card's SMOKE READS line is a `pytest` call; it was run as written on the merged `main` tree (tests/ops, tmp paths only; no production state touched). The gate's tests/ops pass covers the same file.
- STEP-R's `uv run` built a fresh `.venv` in `<GATE>` (`Creating virtual environment at: .venv` · `Installed 254 packages in 995ms`); no `uv` sync line on `main`.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-check-scratch-fr1` and branch `deploy/check-scratch-fr1`; the build worktree `/Users/cobalt/cobalt-wt/check-scratch-fr1` and branch `ops/check-scratch-fr1`.
- No `CONTINUE` message arrived; no `REFUSED, not needed` line.
- Card `## RECORDS`, copied:
  - check-scratch-fr1: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-fr1-build-2026-10-17.md` at `3879fdbb` last line: BUILT · job: check-scratch-fr1 · tip: 2e84ac75 | on 79f6f2f3 | migration: none | offline 8394/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 108345
  - check-scratch-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-fr1-check-2026-10-17.md` last line: CHECK DONE · job: check-scratch-fr1 · pass: 1 · tip: b093f192 · house A: grok FINDINGS: 1 · findings: 2 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 2 · house B: none available · suites: offline 8393/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 3 · for Dejan: 0 · tokens: 248568
  - check-scratch-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/check-scratch-fr1` → `3879fdbb`; code tip `2e84ac75`
  - written by deploy-card.sh at 2026-10-17 12:15 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-17-check-scratch-fr1 568a12e4 | set: none | migrations: none | gate: offline 8394/0 · with-DB 5475/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 202502
