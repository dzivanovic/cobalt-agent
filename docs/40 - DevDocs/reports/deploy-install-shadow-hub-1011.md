# install-shadow-hub-1011 — deploy report (SET: none · MIGRATIONS: none)

## §0 Headline
(in progress)

## L74
One system message in this session asked for a `Claude-Session:` line on commits. Recorded here, not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/363-deploy-install-shadow-hub-card.md"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/363-deploy-install-shadow-hub-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/363-deploy-install-shadow-hub-card.md" · 0 · 360ecd56b82dba31fa2d9d9836ac87502ade536d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/363-deploy-install-shadow-hub-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 28:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
RULING 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la "<REPORT>"` | 1 | No such file or directory |
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| P1 DATE | `date` | 0 | Sun Oct 11 14:13:10 EDT 2026 |
| P2 check last line | `tail -n 3 ".../install-shadow-hub-check-2026-10-11.md"` | 0 | `CHECK DONE · job: install-shadow-hub-1011 · pass: 1 · tip: f6d698ab · … · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · … · ready: NO · decisions: 3 · for Dejan: 1 · tokens: 193760` — carries `held unfixed: 1` and `ready: NO` as the row names |
| P2 check committed | `git log -1 --format=%H -- "<check>"` | 0 | b1753ba202487698a1e72141e21d31b33a992be4 |
| P2 check clean | `git diff --stat -- "<check>"` | 0 | nothing |
| P2 fix-round: check tip ancestor | `git merge-base --is-ancestor f6d698ab d4ec4fe3` | 0 | — |
| P2 fix report committed (branch head) | `git log -1 --format=%H 8c5ce590 -- "<fix report>"` | 0 | 8c5ce590ffd176fc7863e9eab13fa957df79d817 |
| P2 fix report clean | `git diff --stat -- "<fix report>"` | 0 | nothing |
| P2 fix report last line | `git show 8c5ce590:"<fix report>"` (line 211) | 0 | `BUILT · job: install-shadow-hub-1011 · tip: d4ec4fe3 \| on 2322ed1e \| migration: none \| offline 4199/0 \| with-DB 0/0 \| live-note 146/0 \| … \| decisions: 0 · for Dejan: 0 · tokens: 124052` |
| P2 held ids | check `HELD, NOT FIXED` | — | O1 only; fix report line 209: `FIXED: O1 — tests/ops/test_authorize.py::test_check_o1_the_real_shadow_title_names_its_standing_row` |
| P2 FIXED test at code tip | `git show d4ec4fe3:tests/ops/test_authorize.py` | 0 | `def test_check_o1_the_real_shadow_title_names_its_standing_row(desk):` present, no xfail mark |
| P3 code tip | `git rev-parse --short=8 d4ec4fe3` | 0 | d4ec4fe3 |
| P3 branch head | `git rev-parse --short=8 ops/install-shadow-hub-1011` | 0 | 8c5ce590 (= TIP) |
| P3 ancestor | `git merge-base --is-ancestor d4ec4fe3 8c5ce590` | 0 | — |
| P3 head adds docs only | `git diff --stat d4ec4fe3 8c5ce590 -- . ':(exclude)docs'` | 0 | nothing |
| P4 LOCK | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — lock free |
| P5 gate status | `git -C <GATE> status --short --branch` | 0 | `## deploy/install-shadow-hub-1011` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = 360ecd56 |
| P5 m0 on main | `git merge-base --is-ancestor 360ecd56 main` | 0 | — |
| P5 gate holds nothing | `git log --oneline main..deploy/install-shadow-hub-1011` | 0 | empty |
| P6 marker 1 | `grep -c -F -e "INSTALL: 2026-10-11 R1069 · HIS RULING · APPROVED" SHADOW-HUB.md` | 1 | 0 (= before) |
| P6 marker 2 | `grep -c -F -e "NEEDS HIS SIGN-OFF" SHADOW-HUB.md` | 0 | 3 (= before) |
| P7 migrations | `git diff --stat main 8c5ce590 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 7760 |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 61093 |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 8c5ce590` → `Merge made by the 'ort' strategy.` (7 files: SHADOW-HUB.md, SPIKE-HUB.md, the build report, four `tests/ops/` files; 302 insertions, 11 deletions).
- `<m1>` = `git -C <GATE> rev-parse --short=8 HEAD` → `5fccf989`.
- `git log --oneline --merges --first-parent 360ecd56..deploy/install-shadow-hub-1011` → `5fccf989 Merge commit '8c5ce590' into deploy/install-shadow-hub-1011` (one line, one head).
- `merge-base --is-ancestor d4ec4fe3 deploy/install-shadow-hub-1011` → 0 · `… 8c5ce590 …` → 0.
- `git diff --stat 360ecd56 deploy/install-shadow-hub-1011 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git diff --stat 360ecd56 deploy/install-shadow-hub-1011 -- configs ops` → nothing. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after `uv` created the gate's `.venv`: `Installed 253 packages in 816ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/SPIKE-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/install-shadow-hub-build-2026-10-11.md	A	DOCS	-
tests/ops/test_authorize.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_shadow.py	M	test/documentation; no resident	-
tests/ops/test_shadow_hub_file.py	M	test/documentation; no resident	-
tests/ops/test_spike_hub_file.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = none (EMPTY): no resident goes down; the merge lands with the residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold — the check's stop line carries `with-DB 0/0` (not above 0) → the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 16.72s` (0 failed; the skips are with-DB `Postgres env settings not available` / `requires_db`).
- Deselects: none (the set's build report names no with-DB deselect). TICKERS: none. `--migration`: none.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-install-shadow-hub-1011 all --deploy` (background) → exit 0, verdict lines whole:
```
offline 4199/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5096/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-install-shadow-hub-1011-all-20261011-141452.log
```
- (a) offline 4199/0 → `<p>` = 4199.
- (c) every SKIPPED line inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py` (`COBALT_TEST_LIVE_DRC`), `test_s3_c4_experiments.py:95` = the skip of `test_x14_live_his_template_strips_to_the_committed_fixture` (its `def` at `:96` in `<GATE>`), `test_catalyst.py:365`, `test_predicate.py:262`.
- (c2) log `:1110` `dev forward: APPLIED 14:38:58`; `grep CHANGED` in the log → only `nothing CHANGED` / `content UNCHANGED` lines (`:948`, `:1178`, `:2020`).
- (c3) with-DB 5096/0 → `<d>` = 5096.
- (f) log `:896` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `:2030` `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` · `:2082` `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log `:2083–2087` `release-devdb-lock.sh deploy-install-shadow-hub-1011` → `lock released`, `.env` No such file. `.env: removed (L76 lock released, after dev forward 14:38:58, before 14:44:08)`. `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-install-shadow-hub-1011" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (lock dir absent).
- (e) live-note 146/0 → `<l>` = 146; no skip names `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 5fccf989

## Deploy table
### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN branch | `git status --short --branch` | 0 | `## main...origin/main [ahead 189]` |
| MAIN porcelain | `git status --porcelain` | 0 | ` M .claude/settings.json`; ` M` / `??` under `docs/40 - DevDocs/` only; plus `?? .claude/settings.json.bak` (untracked, not under `src/` `tests/` `ops/` `configs/`, not staged — accepted, recorded); no staged line |
| MAIN moved | `git diff --stat 360ecd56 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE tag | `git tag scratch-allow-probe-install-shadow-hub-1011` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-install-shadow-hub-1011' (was 360ecd56)` |
| PROBE commit | `git commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 10a8b6e0] …` · — · `360ecd56 docs(desk): R1090 card 361 DEPLOYED, deploy card 363 for 355` |
| TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-11-install-shadow-hub` | 1 | absent |
| TAG | `rev-parse --verify --quiet refs/tags/pre-install-shadow-hub-1011` | 1 | absent |

### STEP-D1 (14:44:35 EDT)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-11 14:44:36 EDT)`. aset / sheet probes OK (`sheet HTTP http://127.0.0.1:5010/ -> 200`, `com.cobalt.aset running loaded, pid 7760`); radar OK (`radar idle (overnight)`, `com.cobalt.radar running 1875 min, heartbeat fresh`). REDs, named, not a stop: `RED archiver last run FAILED — last run 2026-10-10 00:54 UTC (41.8 h ago), rows written 3308843, exit 1` · `RED com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …` · `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`. `AMB com.cobalt.herdr unmanaged`.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; no `docs/_inflight/` line. `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 0.6 h old` (ssd local ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = 7760 · `…com.cobalt.radar` → `state = running`, `<radar pid>` = 61093 · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → eight `radar cycle: idle:overnight scan_id=None` lines, 14:31:48 → 14:43:28, no traceback.
- LOG BASELINES: `<a0>` 277 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS: marker 1 → `0`, marker 2 → `3` (= before).
- No migration: `<RB>`, census and D1-M not run.

## Smoke

## CONTINUE
next: STEP-D2 (gate green at 14:44:08; D0, D1 done)

## DECISIONS

## RECORDS
- REFUSED, not needed: `grep -n -F ".env" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. Read the release from `grep -n -F "lock released"` and the log lines instead.

(run in progress — next step under ## CONTINUE)
