# deploy check-scratch-1016 — SET: none — MIGRATIONS: none

## §0 Headline
- Deploy of `ops/check-scratch-1016` (code tip `dd4d968d`, head `949cb071`), card 664, off-ladder (R1532), carried held G1 shipped on R1731 (HIS RULING A).
- DEPLOYED: `main` `a0c192cd` → `9c36df59` (fast-forward), tag `deploy-2026-10-17-check-scratch-1016`, rollback tag `pre-check-scratch-1016`.
- Gate green on `1c4f84ae`: offline 8388/0 · with-DB 5475/0 · live-note 146/0. RESTARTS: none — no resident went down. MIGRATIONS: none.
- Smoke GREEN; markers `1`/`1`; `tests/ops/test_stage_set.py` on `main` `32 passed`. FR-1/FR-2 red-green quoted under `## Smoke` (R1731).

## L74
- A harness attribution block arrived mid-session asking commits to end with a `Claude-Session:` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/664-deploy-check-scratch-1016-card.md"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/664-deploy-check-scratch-1016-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/664-deploy-check-scratch-1016-card.md" · 0 · d01849e7a6ef4a9de57d6de11856c866919737d2
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/664-deploy-check-scratch-1016-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-17 R1731 row · grep -n "^| R1731 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · 13:| R1731 | 06:24 ET | Card 641 deployed before its fix-round check, HIS RULING A, 2026-10-16 (brain: "Dejan said: A", L79 + R1471). Deploy 641 now with the builder's FR red-green quoted; then relaunch check 662 once (live proof); then the 583 check. | HIS RULING · APPROVED |
RULING 2026-10-17 R1731 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1731 |" -- "docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · aa404a3b943f1f0cac48a796ed44dfa695c52b57
RULING 2026-10-17 R1731 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la "…/reports/deploy-check-scratch-1016.md"` | 1 | `No such file or directory` |
| P0 | `authorize.sh deploy "<card>"` | 0 | `AUTHORIZED` (above) |
| P1 DATE | `date` | 0 | `Sat Oct 17 06:30:58 EDT 2026` — outside 21:30-22:30 |
| P2 check line | `tail -n 3 "…/reports/check-scratch-check-2026-10-16.md"` | 0 | `CHECK DONE · job: check-scratch-1016 · pass: 1 · tip: 85eade55 · house A: grok FINDINGS: 1 · findings: 2 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 8384/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 7 · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 185748` — carries `held unfixed: 1` and `ready: NO` (the row's cell); carried on R1731 |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/…/check-scratch-check-2026-10-16.md"` | 0 | `764c097c84a540e0b82c856fc7c56df70b59a4f5` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/check-scratch-check-2026-10-16.md"` | 0 | nothing |
| P2 fix-round tip | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 85eade55 dd4d968d` | 0 | ancestor |
| P2 fix report | `git -C /Users/cobalt/cobalt show "949cb071:docs/…/check-scratch-build-2026-10-16.md"` | 0 | last line `BUILT · job: check-scratch-1016 · tip: dd4d968d \| on b84cca9a \| migration: none \| offline 8388/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 2 of 2 \| self-check: 3 of 3 \| decisions: 1 · for Dejan: 0 · tokens: 152910`; held id G1 (check `## RUNS` `- G1: HELD, NOT FIXED — tests/ops/test_stage_set.py (fence)`) → `FIXED: G1 — tests/ops/test_stage_set.py::test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob` |
| P2 fix report committed | `git -C /Users/cobalt/cobalt log -1 --format=%H 949cb071 -- "docs/…/check-scratch-build-2026-10-16.md"` | 0 | `949cb071bb36873618973c8ef106e2f0959c9fa8` |
| P2 fix report clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/check-scratch-build-2026-10-16.md"` | 0 | nothing |
| P2 FIXED test at tip | `git -C /Users/cobalt/cobalt show dd4d968d:tests/ops/test_stage_set.py` | 0 | `def test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob(job):` present; no `xfail` in the file |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 dd4d968d` | 0 | `dd4d968d` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/check-scratch-1016` | 0 | `949cb071` = row = `TIP` |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor dd4d968d 949cb071` | 0 | ancestor |
| P3 docs only | `git -C /Users/cobalt/cobalt diff --stat dd4d968d 949cb071 -- . ":(exclude)docs"` | 0 | nothing |
| P4 LOCK | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate | `git -C <GATE> status --short --branch` | 0 | `## deploy/check-scratch-1016` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `d01849e7` = `<m0>` |
| P5 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor d01849e7 main` | 0 | ancestor |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/check-scratch-1016` | 0 | empty |
| P6 marker 1 | `grep -c -F "more than one prior card copy" /Users/cobalt/cobalt/ops/desk/stage-set.sh` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "test_cs1_a_fix_rounds_check_clears_the_first_passes_folder" /Users/cobalt/cobalt/tests/ops/test_stage_set.py` | 1 | `0` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 949cb071 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 80523` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 24167` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 80543).` |

## THE TREE
- `git -C <GATE> merge --no-edit 949cb071` → `Merge made by the 'ort' strategy.` (`4 files changed, 533 insertions(+), 6 deletions(-)`: `check-scratch-build-2026-10-16.md`, `.result`, `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`).
- `git -C <GATE> rev-parse --short=8 HEAD` → `1c4f84ae` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent d01849e7..deploy/check-scratch-1016` → `1c4f84ae Merge commit '949cb071' into deploy/check-scratch-1016` (one head, one line).
- `merge-base --is-ancestor dd4d968d deploy/check-scratch-1016` → exit 0; `merge-base --is-ancestor 949cb071 deploy/check-scratch-1016` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat d01849e7 deploy/check-scratch-1016 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat d01849e7 deploy/check-scratch-1016 -- configs ops` →
```
 ops/desk/stage-set.sh | 34 +++++++++++++++++++++++++++++-----
 1 file changed, 29 insertions(+), 5 deletions(-)
```
- `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" d01849e7 deploy/check-scratch-1016` → exit 0, whole: `STEP-C: ADMITTED 0`. `<launchd set>` = empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv lines: `Creating virtual environment at: .venv`, `Installed 254 packages in 827ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md	A	DOCS	-
docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.result	A	DOCS	-
ops/desk/stage-set.sh	M	operator script; no Cobalt reader	-
tests/ops/test_stage_set.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = EMPTY: no resident goes down; the merge lands with the residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold (check tip `85eade55` ≠ fix-round code tip `dd4d968d`; check with-DB 0) → the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.49s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db`).

- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-check-scratch-1016 all --deploy --deploy-gate` (no `--deselect`: the build deselected none, with-DB 0/0; TICKERS none; MIGRATIONS none) → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8388/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-check-scratch-1016-all-20261017-063313.log
```
- (c) every SKIPPED line inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = `@requires_live` on `test_x14_live_his_template_strips_to_the_committed_fixture` (`:96`, read in `<GATE>`).- log reads: `grep -n -F "F0: "` → `976:F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; `grep -n -F "dev forward"` → `1195:dev forward: APPLIED 07:12:48`; `:2164` `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`, `:2167` `cobalt_dev: 0013 — F2 = F0`, `:2169` `lock released`, `:2173` `.env: removed`.
- THE RELEASE verified: `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-check-scratch-1016" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent). `.env: removed (L76 lock released; the log stamps no time, read by 07:18:22 EDT)`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed. `date` → `Sat Oct 17 07:18:22 EDT 2026`.

GATE GREEN on 1c4f84ae

## Deploy table
### STEP-D0 (07:18 EDT)
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 7]`; then the `--porcelain` lines |
| MAIN porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; 10 ` M` under `docs/40 - DevDocs/`; `??` under `docs/40 - DevDocs/` (incl. this report); `?? .claude/settings.json.bak` (see `## DECISIONS` 1). No staged line; no dirty `src/` `tests/` `ops/` `configs/` path |
| MAIN moved | `git -C /Users/cobalt/cobalt diff --stat d01849e7 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE tag | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-check-scratch-1016` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-check-scratch-1016' (was d01849e7)` |
| PROBE commit | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main f26c61a4] scratch: allowlist probe (reverted next line)` · nothing · `d01849e7 docs(desk): desk 80e82f59 seated, 641 deploy card 664 written, R1735-R1736 Gemini K5 ruling` |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-17-check-scratch-1016` | 1 | absent |
| TAG pre | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-check-scratch-1016` | 1 | absent |

### STEP-D1 (07:19 EDT)
- `date` → `Sat Oct 17 07:19:09 EDT 2026`. `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-17 07:19:10 EDT)`; `OK   radar                    idle (overnight)`; `OK   com.cobalt.aset              running   loaded, pid 80523 [launchd probe]`; `OK   com.cobalt.agent             running   pid 80543 alive …`; `AMB  com.cobalt.herdr             unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) …`; `OK   com.cobalt.radar             running   running 1358 min, heartbeat fresh`. No RED.
- `COBALT_ENV=production uv run cobalt validate` → exit 0; `<val0>` ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 9.6 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 80523` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 24167` · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 80543).` · `ps -p 80543` → `80543 ??         0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → last `2026-10-17 07:18:24.788 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (8 idle:overnight cycle lines 07:06:44–07:18:24, no traceback).
- LOG BASELINES: `<a0>` 281 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` → `200`. MARKERS again → `0`, `0` (before).
- THE LAUNCHD SET: empty. MIGRATIONS: none → no `<RB>`, no census, no D1-M.

### STEP-D2
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved d01849e7 "<card>"` → nothing. `git add` + `git commit … -- "docs/40 - DevDocs/reports/deploy-check-scratch-1016.md"` → `[main a0c192cd] docs(report): deploy check-scratch-1016 — gate green on 1c4f84ae` · `1 file changed, 150 insertions(+)`; `git show --stat HEAD` → that one file. `git rev-parse --short=8 main` → `a0c192cd` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (`deploy-check-scratch-1016.md | 150 +++`).
- D2.2 `git -C <GATE> rev-parse --short=8 HEAD` → `9c36df59` = `<stack-final>`; `rev-parse --short=8 9c36df59^2` → `a0c192cd` = `<pre-merge>`; `merge-base --is-ancestor 1c4f84ae 9c36df59` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 1c4f84ae 9c36df59 -- . ":(exclude)docs" ":(exclude)configs/cobalt/rules.yaml"` → nothing.
- D2.4 `backup status` → `newest snapshot: 9.7 h old`; `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 8901.2 MB` · `ssd: snapshot 686c6be3 — 0 new / 3 changed, 30.6 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `Sat Oct 17 07:21:16 EDT 2026` (126 s after D1's 07:19:10); `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-17 07:21:16 EDT)`; aset pid 80523, radar `running 1360 min, heartbeat fresh`. No new RED.
- D2.6 `date` → `Sat Oct 17 07:21:21 EDT 2026`; `git -C /Users/cobalt/cobalt tag pre-check-scratch-1016` (at `a0c192cd`) → exit 0.

### STEP-4 (empty `<restart set>`: no resident down)
- 4.1 `date` → `Sat Oct 17 07:21:35 EDT 2026` = `<t down>` = `<t up>` (set empty). 4.2: no call.
- 4.3 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `a0c192cd` = `<pre-merge>`; `git -C /Users/cobalt/cobalt merge --ff-only deploy/check-scratch-1016` → `Updating a0c192cd..9c36df59` / `Fast-forward` (`4 files changed, 533 insertions(+), 6 deletions(-)`).
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 / 4.6L: no call (both sets empty).

### CLOSE
| item | value |
|---|---|
| merge | `<pre-merge>` `a0c192cd` → `<stack-final>` `9c36df59` |
| tags | rollback `pre-check-scratch-1016` at `a0c192cd`; deploy `deploy-2026-10-17-check-scratch-1016` (set after the green smoke) |
| downtime | `<t down>` / `<t up>` none (empty set) · 0 s |
| uv sync | gate worktree only (`Creating virtual environment at: .venv`, `Installed 254 packages in 827ms`); none on `main` |
| proof cost | none (no migration; dev proof-only in the gate log `:2160` `Proof cost: total 5.6 s`) |
| migrations applied | none · `<RB>` none |
| snapshot | `686c6be3` (ssd) |
| RESTARTS done | none |
| LAUNCHD done | none · BOOTSTRAP OWED: none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 9c36df59` (no resident down: the set is empty; no launchd label). 2. SCHEMA: none. 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`. The desk's, never this session's. |

## Smoke
- FIRST CALLS: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1).
- (a) `date` 07:21:49 · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 80523` (SAME, outside the set) · `…/com.cobalt.radar` → `state = running`, `pid = 24167` (SAME) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 80543).` (one line; same pid). GREEN.
- (b) `date` 07:21:54 · `grep -c "Started server process" …/aset.err` → `281` = `<a0>` (aset outside the set) · `tail -n 30 …/aset.err` → last line `2026-10-16 11:24:51.365 | INFO     | cobalt.vaultwrite.writer:_purge_once:482 - vault_writes: purged 1 row(s) past 30-day retention` (no new start, nothing since) · Traceback aset `217` = `<ta0>`, radar `0` = `<tr0>`, TaxonomyConfigError `0` = `<tc0>`.
- (c) `curl … https://cobalt.taild24291.ts.net/` → `200` · `…/radar` → `200` · `…/radar\?frame=phone` → `200`. GREEN.
- (d) MARKERS: `grep -c -F "more than one prior card copy" …/ops/desk/stage-set.sh` → `1` (after) · `grep -c -F "test_cs1_a_fix_rounds_check_clears_the_first_passes_folder" …/tests/ops/test_stage_set.py` → `1` (after). GREEN.
- (f) validate → as 4.5 · `COBALT_ENV=production uv run cobalt jobs restarts a0c192cd..9c36df59` → exit 0, the same four rows, `RESTARTS: none` = STEP-R's set, no `UNCLASSIFIED`. GREEN.
- (g) no migration.
- (s) `ls -la <GATE>/.env` → No such file · `uv run pytest -q tests/ops/test_stage_set.py` (in `/Users/cobalt/cobalt`, on the landed `main`) → exit 0, `32 passed, 15 warnings in 12.65s` — `0 failed` = green. The gate also ran it inside `tests/ops` (offline 8388/0).
- (s) EXTRA READ (R1731), quoted from the build report `check-scratch-build-2026-10-16.md` (at `949cb071`, now on `main`):
  - FR-1 red (tip `0605334f`, code `85eade55`): `uv run pytest -q -p no:cacheprovider --color=no -rA --tb=line tests/ops/test_stage_set.py` → exit 1, `2 failed, 29 passed, 15 warnings in 11.74s`; `E   AssertionError: REFUSED: the dest is not empty: …/test_fr1_a_build_card_read_cop0/wt/agy-trial/scratch/tribunal-bars-0920/x-job-check — not cleared: more than one prior card copy in …/x-job-check/files` (`tests/ops/test_stage_set.py:476`) and the same for `test_fr1_control_this_jobs_own0` (`:508`). Commit `a370ecce wip(check-scratch-1016): FR-1 red`.
  - FR-1 green: "After the edit: the same command → `32 passed, 15 warnings in 12.19s`". Mutations F1 (`^HOUSE A:` filter removed → `2 failed, 29 passed`), F2 (JOB split → `if true; then` → `1 failed, 30 passed`), F3 (THE FALLBACK removed → `1 failed, 31 passed`).
  - FR-2: `test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob` green with the JOB line in place: `32 passed, 15 warnings in 12.36s`; the JOB line removed alone → `1 failed, 31 passed, 15 warnings in 12.35s`, `FAILED tests/ops/test_stage_set.py::test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob` · `E   AssertionError: cleared: …` (`:531`). Commit `dd4d968d`.
  - Guard test `test_fr1_a_build_card_read_copy_does_not_block_the_clear`: present at `dd4d968d` (read by `git show dd4d968d:tests/ops/test_stage_set.py`), named in the build report `- BUILT: FR-1 — … — tests/ops/test_stage_set.py::test_fr1_a_build_card_read_copy_does_not_block_the_clear`; red at `:476` before FR-1, green after; inside the (s) run's `32 passed`.
- (e) `date` 07:22:29 · `heartbeat show` #1 → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-17 07:22:30 EDT)`; `com.cobalt.radar             running   running 1362 min, heartbeat fresh`. `date` 07:24:21 · #2 → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-17 07:24:23 EDT)` (113 s later); `com.cobalt.radar             running   running 1363 min, heartbeat fresh`. No RED. GREEN.
- (b) radar tail: `date` 07:23:05 (`<t up>` + 90 s) · `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` → last `2026-10-17 07:21:44.835 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` — a cycle line stamped after `<t up>` 07:21:35, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback in the 12 lines: settled GREEN at the first tail.
- (h) REVERT-READBACK: `date` 07:24:35 (`<t up>` + 180 s) · counts `18` `60` `43` `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew) · `/radar` curl → `200`. No census read (no migration). GREEN.
- Clock fillers between (b), (e) and (h): `date` + `heartbeat show` pairs, each `HEARTBEAT GREEN … nothing red`.

THE CHAIN: every check committed (P2: check `764c097c`, fix report at `949cb071`) → the tips re-read (P3: `dd4d968d`, `949cb071`) → the merged tree `1c4f84ae` (T) → RESTARTS derived `none` (R) → three suites green on `1c4f84ae` (G: offline 8388/0 · with-DB 5475/0 · live-note 146/0) → `<stack-final>` `9c36df59` = `<m1>` + docs (D2.3) → the landed code `a0c192cd..9c36df59` (4.3) → markers `1`/`1` (d) → no migration (g) → residents up, same pids (a) → radar cycling (b, e) → the set's read `32 passed` (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

## PRE-STOP SELF-CHECK
1. Every smoke row's evidence is quoted verbatim with its `date`: (a) 07:21:49, (b) 07:21:54 and 07:23:05, (c)/(d)/(f)/(s) after 07:21:54, (e) 07:22:29 and 07:24:21, (h) 07:24:35 — `## Smoke` above.
2. Every code tip and head re-read (P3 `dd4d968d`, `949cb071`) and ancestors of `<BRANCH>` (STEP-T `merge-base --is-ancestor` exit 0 each); `<stack-final>` `9c36df59` has `1c4f84ae` as ancestor (D2.2 exit 0), so both tips are in it.
3. REVERT-READBACK shown at (h): counts `18 60 43 39` unchanged from D1. Every count, sha and `file:line` here re-read from this run's tool output.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.`, D2.1 the same, 4.3 `Fast-forward`.

## CONTINUE
OUTAGE STARTING 07:21:21 EDT — residents of <restart set> (EMPTY: none) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
next: none — deployed; STEP-7 closed 07:24 EDT.

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` on `main` is neither on D0's ACCEPTED list nor on its REFUSED list (not staged, not under `src/` `tests/` `ops/` `configs/`). Safe default taken: not a refusal; untracked, the fast-forward merge does not touch it; left as found. [07:18 EDT]

## RECORDS
- Downtime: none (empty `<restart set>`; no resident went down).
- `cobalt_dev: 0013 (F2 = F0)` (gate log `:2167`); lock released, `.env: removed`.
- RETIRE OWED: none. BOOTSTRAP OWED: none. Carried RED: none read (heartbeat GREEN at D1, D2.5 and smoke).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-check-scratch-1016` and branch `deploy/check-scratch-1016`; the set's worktree and branch `ops/check-scratch-1016`.
- Carried held defect G1 (check `HELD, NOT FIXED`) shipped on R1731 (HIS RULING A); the fix round's `FIXED: G1` test is in `tests/ops/test_stage_set.py` and green on `main`; the fix-round check (card 662) runs after this deploy per R1731.
- Card `## RECORDS`, copied:
  - check-scratch-1016: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md` at `949cb071` last line: BUILT · job: check-scratch-1016 · tip: dd4d968d | on b84cca9a | migration: none | offline 8388/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 152910
  - check-scratch-1016: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-check-2026-10-16.md` last line: CHECK DONE · job: check-scratch-1016 · pass: 1 · tip: 85eade55 · house A: grok FINDINGS: 1 · findings: 2 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 8384/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 7 · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 185748
  - check-scratch-1016: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/check-scratch-1016` → `949cb071`; code tip `dd4d968d`
  - written by deploy-card.sh at 2026-10-17 06:29 ET (`date`); trial merge of the heads onto main in order: clean
- L74: the `Claude-Session:` attribution block (system reminder) recorded under `## L74`, not acted on.
- The harness showed a "do not cd to the original repository root" note on entering `<GATE>`; this file's CWD rule governs (`cd /Users/cobalt/cobalt` after the suites), recorded, not followed.
- REFUSED, not needed: `git -C /Users/cobalt/cobalt grep -n -F -e "def test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob" -e "xfail" dd4d968d -- tests/ops/test_stage_set.py` — Permission to use Bash has been denied because Claude Code is running in don't ask mode. (read instead by the listed `git -C * show*`)

DEPLOYED deploy-2026-10-17-check-scratch-1016 9c36df59 | set: none | migrations: none | gate: offline 8388/0 · with-DB 5475/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 193201
