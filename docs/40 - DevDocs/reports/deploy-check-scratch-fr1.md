# deploy check-scratch-fr1 — set: none · migrations: none (2026-10-17)

## §0 Headline
- (filled at close)

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

## Smoke

## CONTINUE
next: STEP-D2 (D0, D1 done; D2.0 `deploy-shipped.sh --moved 7142cd9c "<card>"` → printed nothing; this report commit is D2.0)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
