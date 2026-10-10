# deploy https-only-1009 (attempt 2) — SET: none · MIGRATIONS: none

## §0 Headline
- FAILED at 4.6, then rolled back. Gate GREEN on `da0ee609` (offline 4203/0 · with-DB 5100/0 · live-note 146/0); merged 1a13bd1d → 86f8e308 at 07:28; reverted by one `revert -m 2` → `7f6b63fd`; the tree equals `<pre-merge>` outside docs.
- The new aset never started: `ScratchLocked` — the OLD aset's python child (pid 39280, `python -m cobalt.aset`) outlived the bootout (the plist has `abandon process group`) and holds `/Users/cobalt/.cobalt/voice-scratch`. The reverted code hits the same lock.
- NOW: **aset DOWN** (every https page 502, sheet probe RED); radar UP on the reverted tree; agent ONLINE. launchd retries aset every ~10 s; it comes up on its own once pid 39280 is stopped (DECISIONS 2, FOR DEJAN).
- The https code is not proven wrong (L70): the failure is the orphan, and every deploy that restarts aset will hit it until that is fixed (DECISIONS 3).

## L74
- A system reminder arriving mid-session asked commits to end with a `Claude-Session:` line. Recorded once; not acted on (L74). Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/208-deploy-https-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/208-deploy-https-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/208-deploy-https-card.md" · 0 · 9e0954a99c0d624408ef766ee40073202aa661e1
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/208-deploy-https-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-09 R718 row · grep -n "^| R718 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · 11:| R718 | 07:14 ET | Relayed by brain (L79), then his words 07:20 ET: "yes https only please". Widens R717 to every page: https via `tailscale serve`; http binds 127.0.0.1; probes read https. APPLIED: LAWS L80, NOW at 07:20 ET. | HIS RULING · APPROVED · APPLIED |
RULING 2026-10-09 R718 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R718 |" -- "docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · 1458693dbde5371259a29c5d502d74e3878fee3b
RULING 2026-10-09 R718 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la "…/reports/deploy-https-only-1009-attempt2.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Sat Oct 10 06:52:43 EDT 2026` (no restart window binds, L43) |
| P2 check | `tail -n 3 "…/reports/https-only-check-2026-10-09.md"` | 0 | `CHECK DONE · job: https-only-1009 · pass: 1 · tip: 6e1ccd3d · … · held unfixed: 0 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 180198` |
| P2 check committed | `git log -1 --format=%H -- "docs/…/https-only-check-2026-10-09.md"` | 0 | `5fc1e9a48018383697ec040f1bf85d17eb1d4441` |
| P2 check clean | `git diff --stat -- "docs/…/https-only-check-2026-10-09.md"` | 0 | nothing |
| P2 fix round: tip ancestor | `git merge-base --is-ancestor 6e1ccd3d a1b99495` | 0 | — |
| P2 fix report | `tail -n 3 "…/https-only-build-2026-10-09.md"` (main checkout) | 1 | `No such file or directory` — the fix report lives on the branch (card RECORDS: "read at `16559ba4`") |
| P2 fix report committed | `git log -1 --format=%H 16559ba4 -- "docs/…/https-only-build-2026-10-09.md"` | 0 | `16559ba4c6f5edf22477c392a4fafe1352c78e45` (in a commit: unmodified) |
| P2 fix report last line | `git show "16559ba4:docs/…/https-only-build-2026-10-09.md"` (last line) | 0 | `BUILT · job: https-only-1009 · tip: a1b99495 \| on e4586978 \| migration: none \| offline 4061/0 \| with-DB 4948/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: com.cobalt.aset com.cobalt.radar \| rows: 6 of 6 \| self-check: 3 of 3 \| decisions: 2 · for Dejan: 0 · tokens: 97831` |
| P3 code tip | `git rev-parse --short=8 a1b99495` | 0 | `a1b99495` |
| P3 branch head | `git rev-parse --short=8 ops/https-only-1009` | 0 | `16559ba4` (= TIP) |
| P3 ancestor | `git merge-base --is-ancestor a1b99495 16559ba4` | 0 | — |
| P3 docs only | `git diff --stat a1b99495 16559ba4 -- . ":(exclude)docs"` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` (no holder) |
| P5 gate status | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-2026-10-09-https-only-attempt2` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `9e0954a9` = `<m0>` |
| P5 m0 on main | `git merge-base --is-ancestor 9e0954a9 main` | 0 | — |
| P5 gate empty | `git log --oneline main..deploy/deploy-2026-10-09-https-only-attempt2` | 0 | EMPTY |
| P6 marker 1 | `grep -c -F "bind: lan" …/configs/dev/aset.local.yaml` | 1 | `0` = before (M5 done) |
| P6 marker 2 | `grep -c -F "https_url" …/configs/cobalt/voice.yaml` | 1 | `0` = before |
| P6 marker 3 | `grep -c -F "isSecureContext" …/src/cobalt/voice/web.py` | 1 | `0` = before |
| P6 marker 4 | `grep -c -F "L80" …/src/cobalt/aset/config.py` | 1 | `0` = before |
| P6 marker 5 | `grep -c -F "cobalt.taild24291.ts.net" …/configs/cobalt/smoke/s2.yaml` | 1 | `0` = before |
| P6 marker 6 | `grep -c -F "cobalt.taild24291.ts.net" …/src/cobalt/heartbeat/probes.py` | 1 | `0` = before |
| P6 marker 7 | `grep -c -F "cobalt.taild24291.ts.net" …/ops/desk/deploy-smoke.sh` | 1 | `0` = before |
| P7 two-dot | `git diff --stat main 16559ba4 -- src/cobalt/db_migrations` | 0 | `0024_strike_alerts.rollback.sql \| 5 ----` · `0024_strike_alerts.sql \| 32 ---` · `__init__.py \| 6 ----` · `placement.py \| 3 --` · `4 files changed, 46 deletions(-)` — all deletions: main's 0024, newer than the branch's base (DECISIONS 1) |
| P7 the head's own | `git diff --stat main...16559ba4 -- src/cobalt/db_migrations` | 0 | nothing: the set adds no migration (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 39274` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 25666` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 16559ba4` → `Merge made by the 'ort' strategy.` (`22 files changed, 635 insertions(+), 86 deletions(-)`; auto-merged `aset/__main__.md`, `voice/web.md`, `src/cobalt/aset/__main__.py`, `src/cobalt/voice/web.py`, `tests/cobalt/test_jobs_restarts.py`, `tests/cobalt/test_voice_web.py`; no conflict).
- `git -C <GATE> rev-parse --short=8 HEAD` → `da0ee609` = `<m1>`.
- `git log --oneline --merges --first-parent 9e0954a9..deploy/deploy-2026-10-09-https-only-attempt2` → `da0ee609 Merge commit '16559ba4' into deploy/deploy-2026-10-09-https-only-attempt2` (one line, one head).
- `git merge-base --is-ancestor a1b99495 <BRANCH>` → exit 0 · `… 16559ba4 <BRANCH>` → exit 0.
- `git diff --stat 9e0954a9 <BRANCH> -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none holds).
- STEP-C: `git diff --stat 9e0954a9 <BRANCH> -- configs ops` → `configs/cobalt/smoke/s2.yaml | 8 ++++----` · `configs/cobalt/voice.yaml | 2 ++` · `configs/dev/aset.yaml | 11 ++++-------` · `ops/desk/deploy-smoke.sh | 6 +++---` · `4 files changed, 13 insertions(+), 14 deletions(-)`. No plist added, modified or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the gate's `.venv`: `Installed 253 packages in 889ms`), the table whole:
```
path	change	rule	restart
configs/cobalt/smoke/s2.yaml	M	operator command (cobalt smoke); no job reads	-
configs/cobalt/voice.yaml	M	resident reads	com.cobalt.aset
configs/dev/aset.yaml	M	resident reads	com.cobalt.aset
docs/40 - DevDocs/cobalt/aset/__main__.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/heartbeat/probes.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/web.md	M	DOCS	-
docs/40 - DevDocs/reports/https-only-build-2026-10-09.md	A	DOCS	-
ops/desk/deploy-smoke.sh	M	operator script; no Cobalt reader	-
src/cobalt/aset/__main__.py	M	static import reach	com.cobalt.aset
src/cobalt/aset/config.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/heartbeat/probes.py	M	static import reach	com.cobalt.radar
src/cobalt/voice/config.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_aset_config.py	M	test/documentation; no resident	-
tests/cobalt/test_https_only.py	A	test/documentation; no resident	-
tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
tests/cobalt/test_smoke.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_config.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_web.py	M	test/documentation; no resident	-
tests/ops/test_deploy_smoke.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar` (= the card's and the check's).

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold — `git diff --stat 6e1ccd3d da0ee609 -- . ":(exclude)docs"` prints 72 files (`5022 insertions(+), 116 deletions(-)`: the fix round and main's strike / archiver / voice work since the check). The gate runs whole (`--deploy`). No `--deselect` (the build report: "No `--deselect` (no with-DB test added)"), no `--tickers` (TICKERS: none), no `--migration`.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_archiver_migrations.py … tests/cobalt/test_jobs_restarts.py` (the hub's 17 files) → `263 passed, 163 skipped in 16.93s` — 0 failed (with-DB tests skip offline).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-https-only-1009-attempt2 all --deploy` launched in the background → exit 0. Verdict lines, WHOLE:
```
offline 4203/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5100/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-https-only-1009-attempt2-all-20261010-065521.log
```
- (a) OFFLINE: log :879 `4203 passed, 800 skipped, 1 xfailed, 36 warnings in 654.23s` → `offline 4203/0`.
- (b) lock taken (`waited 0 min`), `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :896), proof-only at `0013` with nothing `CHANGED` (log :948).
- (c) PASS 1 whole: log :1108 `4895 passed, 7 skipped, 99 deselected, 3 xfailed, 43 warnings in 785.09s` → `<d1>` 4895. The seven SKIPPED lines above are each inside the allowed set by test and reason: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = the skip of `test_x14_live_his_template_strips_to_the_committed_fixture` (`def` at :96 of the gate tree).
- (c2) FORWARD: `dev forward: APPLIED 07:19:46` (log :1110); 0014 → 0024 in `FORWARD` order; the forward proof `content UNCHANGED on every table` (log :1178); `grep -c -F "CHANGED"` = 3 lines, all three read: :948 "nothing CHANGED", :1178 and :2020 "content UNCHANGED" — no `CHANGED` verdict.
- (c3) PASS 2: log :1962 `205 passed, 1 deselected, 5 warnings in 230.32s` → `<d2>` 205; 4895 + 205 = 5100 = `with-DB 5100/0`.
- (f) rollback `--down-to 0013` reversed 0024 → 0014 newest first (log :1966–:1979), `content UNCHANGED on every table` (:2020); `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (:2030) = F0 → `cobalt_dev: 0013 — F2 = F0` (:2082).
- THE RELEASE: `release-devdb-lock.sh` → `lock released` (:2084), `.env: removed` (:2088) — the log carries no clock on these lines; between `dev forward: APPLIED 07:19:46` and my `date` `Sat Oct 10 07:25:03 EDT 2026`. `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-https-only-1009-attempt2" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (no lock dir).
- (e) LIVE-NOTE, `.env` absent: log :2153 `146 passed, 1 skipped, 15 warnings in 25.23s`; the one skip (:2152) names `COBALT_TEST_LIVE_DRC` (inside the set); none names `COBALT_LIVE_VAULT_ROOT` → `live-note 146/0`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on da0ee609

## Deploy table
STEP-D0 (nothing in production changes):
- `git status --short --branch` → `## main...origin/main [ahead 118]`; `git status --porcelain` → ` M .claude/settings.json`, ` M` × 7 and `??` × 22 under `docs/40 - DevDocs/` (this report among them), and `?? .claude/settings.json.bak` (RECORDS); no staged line, no dirty `src/` `tests/` `ops/` `configs/` path.
- `git diff --stat 9e0954a9 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-https-only-1009` → ok; `tag -d …` → `Deleted tag 'scratch-allow-probe-https-only-1009' (was 9e0954a9)`; `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 36539f20] scratch: allowlist probe (reverted next line)`; `reset --soft HEAD~1` → ok; `log --oneline -1` → `9e0954a9 docs(desk): RECUT https-only-1009 attempt 2` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-09-https-only-attempt2` → exit 1; `… refs/tags/pre-https-only-1009` → exit 1.

STEP-D1 (baseline, read-only):
- `date` → `Sat Oct 10 07:25:48 EDT 2026`. `<hb0>` = `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 07:25:49 EDT)`: `OK sheet HTTP http://127.0.0.1:5010/ -> 200` · `OK radar idle (overnight)` · `OK com.cobalt.aset running loaded, pid 39274` · `OK com.cobalt.radar running running 130 min, heartbeat fresh` · `OK com.cobalt.agent running pid 22243 alive`. The REDs, named (not aset / sheet / radar, not a stop): `RED archiver last run FAILED — last run 2026-10-10 00:54 UTC (10.5 h ago), rows written 3308843, exit 1`; `RED com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …`; `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`. `AMB com.cobalt.herdr unmanaged` (declared interim).
- `<val0>`: `validate` exit 0, `13 trade_def(s) validated OK from the vault.`, `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 2.2 h old` (ssd ARMED, b2 off).
- aset `state = running`, `<aset pid>` 39274; radar `state = running`, `<radar pid>` 25666; `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- DEPLOY ORDER (M5), read: `grep -n -F "bind:" …/configs/dev/aset.local.yaml` → `25:  bind: loopback`.
- `tail -n 8 radar.err` → `radar cycle: idle:overnight scan_id=None` every 100 s, last `2026-10-10 07:25:40.346`; no traceback.
- LOG BASELINES: `<a0>` 60 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … https://cobalt.taild24291.ts.net/radar` → `200`. MARKERS again → 0 · 0 · 0 · 0 · 0 · 0 · 0 (each its `before`).
- MIGRATIONS: none → no `<RB>`, no census, no D1-M.

STEP-D2:
- D2.0 `add` + `commit -m "docs(report): deploy https-only-1009 — gate green on da0ee609"` → `[main 1a13bd1d] … 1 file changed, 164 insertions(+)`; `show --stat HEAD` → that one file. `<pre-merge>` = `1a13bd1d`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `86f8e308`; `rev-parse --short=8 86f8e308^2` → `1a13bd1d` = `<pre-merge>`; `merge-base --is-ancestor da0ee609 86f8e308` → exit 0.
- D2.3 `git diff --stat da0ee609 86f8e308 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 2.2 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 6694.3 MB` · `ssd: snapshot e871251e — 0 new / 2 changed, 27.4 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `Sat Oct 10 07:27:46 EDT 2026`; `heartbeat show` (07:27:50, 121 s after D1's 07:25:49) → same three REDs as `<hb0>` (archiver ×2, replay), aset `pid 39274`, radar `running 132 min, heartbeat fresh`, sheet HTTP 200; no new RED.
- D2.6 `date` → `Sat Oct 10 07:27:55 EDT 2026`; `git tag pre-https-only-1009` at `1a13bd1d`.

STEP-4 (the outage):
- 4.1 `date` → `Sat Oct 10 07:28:12 EDT 2026` = `<t down>`.
- 4.2 `launchctl bootout gui/501/com.cobalt.aset` → ok; `print` → still loaded, `state = SIGTERMed`, `pid = 39274`; `date` → `07:28:19`; `print` → exit 113 `Could not find service "com.cobalt.aset"`. `bootout gui/501/com.cobalt.radar` → ok; `print` → exit 113 `Could not find service "com.cobalt.radar"`.
- 4.3 `rev-parse --short=8 HEAD` → `1a13bd1d` = `<pre-merge>`; `merge --ff-only deploy/deploy-2026-10-09-https-only-attempt2` → `Updating 1a13bd1d..86f8e308` · `Fast-forward` (22 files, 635 insertions, 86 deletions).
- 4.4 `migrations applied: none` (MIGRATIONS: none).
- 4.5 `validate` → exit 0, `13 trade_def(s) validated OK`, `Placement … tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`.
- 4.6 `bootstrap … com.cobalt.aset.plist` → ok; `bootstrap … com.cobalt.radar.plist` → ok. `print` aset → `state = spawn scheduled`, `last exit code = 3` (loaded, not running); radar → `state = running`, `pid = 60803`. `tail -n 30 aset.err` → `RED voice scratch dir /Users/cobalt/.cobalt/voice-scratch locked by pid 39280 — start sweep deleted nothing` · `cobalt.voice.scratch.ScratchLocked: voice scratch dir /Users/cobalt/.cobalt/voice-scratch is locked by pid 39280 — the start sweep deleted NOTHING. A process still owns this directory (X-X22: an orphan can outlive its job); find it and stop it before this process may serve voice turns.` · `ERROR:    Application startup failed. Exiting.` `ps -p 39280` → `39280 ?? 1:42.81 …/Python -m cobalt.aset` — the OLD aset's python child, alive after the bootout (the aset plist carries `abandon process group`; the bootout signalled `start_aset.sh` pid 39274 only). `kickstart -k gui/501/com.cobalt.aset` once → `print` → `state = spawn scheduled`, `runs = 4`, `last exit code = 3`. Still not running → STEP-5.

STEP-5 (rollback):
- (0) `date` → `Sat Oct 10 07:29:19 EDT 2026`.
- (1) `bootout gui/501/com.cobalt.aset` → ok, `print` → exit 113 `Could not find service`; `bootout gui/501/com.cobalt.radar` → ok, `print` → exit 113. Agent not in the set (untouched). Counts: `<rp5>` 18 · `<rpr5>` 60 · `<re5>` 43 · `<lc5>` 39 (= D1's baselines).
- (2) `log --oneline -1` → `86f8e308 Merge branch 'main' into deploy/deploy-2026-10-09-https-only-attempt2` = `<stack-final>`. `revert --no-edit -m 2 86f8e308` → `[main 7f6b63fd] Revert "Merge branch 'main' into deploy/deploy-2026-10-09-https-only-attempt2"` · `22 files changed, 86 insertions(+), 635 deletions(-)`. PROOF: `git diff --stat 1a13bd1d HEAD -- . ":(exclude)docs"` → nothing: the tree is `<pre-merge>`'s.
- (3) `bootstrap … com.cobalt.aset.plist` → ok; `bootstrap … com.cobalt.radar.plist` → ok. aset → `state = spawn scheduled`, `last exit code = 3` (the same lock: the old code runs the same voice startup); `kickstart -k gui/501/com.cobalt.aset` once → `state = spawn scheduled`, `runs = 3`, `last exit code = 3`; `ps -p 39280` → alive (`1:45.51`). radar → `state = running`, `pid = 61093`. `date` → `Sat Oct 10 07:30:02 EDT 2026`.
- (4) re-reads on the reverted tree:
  - (a) aset NOT running (`spawn scheduled`, exit 3); radar running, pid 61093 (new); `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (agent outside the set, same pid).
  - (b) `Started server process` 65 (> `<a0>` 60: five failed starts) · aset `Traceback` 7 (`<ta0>` 2: the five ScratchLocked startups) · radar `Traceback` 0 · `TaxonomyConfigError` 0. `tail -n 12 radar.err` → `2026-10-10 07:29:40.454 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`, after the restore, no traceback, no S5 / lifecycle failure → radar GREEN.
  - (c) `curl … https://cobalt.taild24291.ts.net/` → `502`, `502` · `/radar` → `502` · `/radar\?frame=phone` → `502`. RED (aset down).
  - (e) `date` `07:30:17` · `heartbeat show` (07:30:18) → `HEARTBEAT RED — 3 job(s) and 3 probe(s)`: NEW against `<hb0>`: `RED sheet HTTP http://127.0.0.1:5010/ unreachable: URLError: <urlopen error [Errno 61] Connection refused>`, `?? sheet daymode … unreachable`, `RED com.cobalt.aset failed loaded, not running (last exit 3)`; carried: archiver ×2, replay. `OK com.cobalt.radar running running 1 min, heartbeat fresh`.
  - (f) `validate` → exit 0 (`13 trade_def(s) validated OK`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.`, `Placement … tree clean.`); `jobs restarts 1a13bd1d..86f8e308` → exit 0, `RESTARTS: com.cobalt.aset com.cobalt.radar`, no `UNCLASSIFIED`.
  - (g) no migration.
  - (c) again, three attempts per URL: `/` `502` ×3 · `/radar` `502` ×3 · `/radar\?frame=phone` `502` ×3.
  - (e) second read: `date` `07:32:09` · `heartbeat show` (07:32:12, 114 s after 07:30:18) → same as the first: sheet HTTP RED (connection refused), `com.cobalt.aset failed loaded, not running (last exit 3)`, carried archiver ×2 / replay; `com.cobalt.radar running running 3 min, heartbeat fresh`. `tail -n 12 radar.err` → `07:31:20.482 … radar cycle: idle:overnight scan_id=None`.
  - Between the reads: `print` aset → `state = spawn scheduled`, `runs = 10`, `last exit code = 3` (KeepAlive retries); `ps -p 39274` → header only (the old `start_aset.sh` is gone); `ps -p 39280` → alive at `1:48.95` CPU (07:31); `Started server process` 75, aset `Traceback` 17 at 07:31:50 (each a ScratchLocked start).
  - REVERT-READBACK: after the settled radar tail, `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39 = `<rp5>` `<rpr5>` `<re5>` `<lc5>`; no count grew.

THE ROLLBACK STRING (L54):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 86f8e308` — DONE by this run at STEP-5 (2) → `7f6b63fd`.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit 7f6b63fd` — git titles it `Reapply "Merge branch 'main' into deploy/deploy-2026-10-09-https-only-attempt2"` — only after the orphan pid 39280 is stopped (DECISIONS 2).

TABLE: `<pre-merge>` `1a13bd1d` → `<stack-final>` `86f8e308` → reverted `7f6b63fd` · tags: `pre-https-only-1009` at `1a13bd1d`; `deploy-2026-10-09-https-only-attempt2` NOT set (no green smoke) · `<t down>` 07:28:12 · `<t up>` none for aset (still down at 07:32:12); radar up 07:28:40-ish (4.6) and again from 07:29:40 (STEP-5 (3), first cycle line) · uv sync: none in production · proof cost: none (no migration) · `migrations applied: none` · `<RB>` none · snapshot `e871251e` · RESTARTS attempted: `com.cobalt.aset com.cobalt.radar`.

## Smoke
4.7 was never reached: 4.6 failed (aset not running after one `kickstart -k`) and sent the run to STEP-5. STEP-5 (4)'s reads are under `## Deploy table`.
THE CHAIN, as far as it holds: every check committed (P2) ✓ · the tips (P3) ✓ · the merged tree (T) ✓ · RESTARTS derived (R) ✓ · three suites green on `da0ee609` (G) ✓ · `86f8e308` = `da0ee609` + docs (D2.3) ✓ · the landed code (4.3) ✓ · residents up after the merge ✗ (aset: ScratchLocked by orphan pid 39280) → rolled back; the reverted tree proven equal to `<pre-merge>` (STEP-5 (2)); radar cycling on it; no failure count grew; aset still down for the same orphan.

## CONTINUE
next: none — the run ended FAILED with rollback used. The desk's next steps: stop pid 39280 (DECISIONS 2); confirm aset comes up on `7f6b63fd`; fix the orphan in a build (DECISIONS 3); then RE-LAND by a new deploy.
OUTAGE STARTING 07:27:55 EDT — residents of com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
OUTAGE ENDED by STEP-5 at 07:30:02 EDT — radar UP, aset DOWN (orphan lock); STEP-5 is never entered twice.

## DECISIONS
1. P7's two-dot `git diff --stat main <head>` lists main's `0024_strike_alerts` files as DELETIONS (main moved past the branch's base). Read as: the head adds no migration — the three-dot `main...16559ba4` prints nothing, and STEP-T's `<m0>..<BRANCH>` stat is the decisive check. Safe default taken: go on; STEP-T fails the run if any migration path enters. (STEP-T's stat printed nothing.)
2. **DECISION 0 · FOR DEJAN — production aset is DOWN now.** Every https page returns 502; the sheet probe is RED. The cause is pid 39280 (`…/Python -m cobalt.aset`), the old aset's python child. It is still alive after the bootout and holds the voice scratch lock `/Users/cobalt/.cobalt/voice-scratch`. Neither tree can start while it lives. This line has no kill string. The fix is to stop pid 39280 (SIGTERM, then SIGKILL if it hangs). launchd KeepAlive is retrying (`runs = 10` at 07:31), so aset should come up on the reverted tree `7f6b63fd` by itself within ~10 s of the kill; then `launchctl print gui/501/com.cobalt.aset` should show `state = running`, and `curl … /radar` should return `200`. Safe default taken: residents left as STEP-5 (3) left them, and nothing outside the line was touched. Market closed (Saturday).
3. **The root cause belongs to a build, before any re-land.** The aset plist carries `abandon process group`, so `launchctl bootout` signals only `start_aset.sh`; the `python -m cobalt.aset` child is orphaned. Since voice fix 193's `DirectoryLock` (X-X22), that orphan blocks the next aset start. Every deploy with aset in `<restart set>` will fail at 4.6 the same way until one of these is in place: `start_aset.sh` `exec`s python, the plist drops `AbandonProcessGroup`, or the hub stops the child. A plist change goes on strings he approves (STEP-C). Safe default: no re-land from this run. The ROLLBACK STRING's RE-LAND waits for this fix.

## RECORDS
- D0: `?? .claude/settings.json.bak` is untracked on main — not in D0's accepted list and not a refused `src/` `tests/` `ops/` `configs/` path; recorded, not a stop. Cleanup is the desk's.
- DOWNTIME: aset down from `<t down>` 07:28:12 and STILL DOWN at the stop line (≥ 240 s at 07:32:12; over 300 s by the time this is read) — DECISIONS 2. radar down 07:28:12 → ~07:28:40 (4.6) and 07:29:19 → 07:29:40 (STEP-5). Agent untouched (ONLINE, pid 22243 throughout).
- ORPHAN: pid 39280 `python -m cobalt.aset` (old code) alive after bootout; parent `start_aset.sh` pid 39274 gone. aset.err at 07:31:50: `Started server process` 75 (`<a0>` 60), `Traceback` 17 (`<ta0>` 2) — every one a `ScratchLocked` start.
- `cobalt_dev: 0013 (F2 = F0)` — the gate's (log :2082); lock released (`lock released`, :2084), `.env: removed`.
- CARRIED RED, as read at D1, D2.5 and STEP-5 (4): `RED archiver last run FAILED — … exit 1`, `RED com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … '429 Too Many Requests' …`, `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`. Not this deploy's.
- No `RETIRE OWED` (no plist removed). No `REFUSED` call. No message from another session.
- CLEANUP OWED (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-https-only-1009-attempt2` and branch `deploy/deploy-2026-10-09-https-only-attempt2` (holds `86f8e308`, needed for the RE-LAND or a recut); the gate's `.venv`; tag `pre-https-only-1009` stays at `1a13bd1d`.
- L74: one system reminder mid-session asked for a `Claude-Session:` commit line; recorded under `## L74`, not acted on.
- The card's `## RECORDS`, copied:
  - https-only-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/https-only-check-2026-10-09.md` last line: CHECK DONE · job: https-only-1009 · pass: 1 · tip: 6e1ccd3d · house A: Sol FINDINGS: 4 · findings: 10 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 2 · suites: offline 4061/0 · with-DB 4948/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 17 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 180198
  - https-only-1009: head `ops/https-only-1009` → `16559ba4`; code tip `a1b99495`; check tip `6e1ccd3d` is an ancestor of `a1b99495`; `git diff --stat a1b99495 16559ba4 -- . ':(exclude)docs'` prints nothing (the head adds docs only).
  - FIX ROUND (his R376, L75; no new check): the check passed at `6e1ccd3d`; the build's first attempt was gated on `4dfe6114`; the fix round `a1b99495` moved the card's hunks off the lines voice fix 193 (main `2041a53f`) changed, after S4-P1. The fix report (read at `16559ba4`) ends with `BUILT · job: https-only-1009 · tip: a1b99495 …`. No deploy attempt of this job had run.
  - RULINGS `2026-10-09 R718` (card 156, L80 HTTPS only). The deploy runs when READY at any hour (L43, R389).
  - Shipped files, `git diff --stat main...16559ba4` (22 files, 635 insertions, 86 deletions) — listed in the card.
  - MACHINE STEPS (card 156): M0–M3 done 2026-10-09; M5 his, before this deploy (read done: `25:  bind: loopback`); M6, M7 follow. The deploy hub's STEP rewrites the pinned `Uvicorn running on http://0.0.0.0:5010` line to `http://127.0.0.1:5010`.
  - Marker counts: BEFORE read on main, AFTER at `a1b99495`; no `## DEPLOY PROOF` section in card 156.
  - Written by hand by the drafter `https-deploy-fixround` on the fix-round path; trial merge not run by the drafter.

PRE-STOP SELF-CHECK: (1) every smoke row reached is quoted verbatim with its `date` (STEP-5 (4) under `## Deploy table`); 4.7 itself was not reached. (2) `a1b99495` and `16559ba4` re-read at P3 and ancestors of `<BRANCH>` (STEP-T) and so of `86f8e308` (D2.2). (3) REVERT-READBACK shown at STEP-5 (4): 18 · 60 · 43 · 39 = `<rp5>` `<rpr5>` `<re5>` `<lc5>`; every count and sha above was read from tool output this run. (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`); no conflict marker. THE RELEASE: the lock was released by the gate at STEP-G; `<GATE>/.env` absent.

FAILED: 4.6 — aset not running after one kickstart: ScratchLocked, the voice scratch dir held by orphan pid 39280 (the old aset's python child, left by the bootout) · rollback: used — migrations applied: none — aset: DOWN — radar: UP · decisions: 3 · for Dejan: 1 · tokens: 188560
