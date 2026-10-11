# deploy ops-hand-install-1010 · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED: `ops/ops-hand-install-1010` at `680eca0e` landed on `main` as `0d0f90f5..3ecac752` (fast-forward), tag `deploy-2026-10-10-ops-hand-install`, rollback tag `pre-ops-hand-install-1010` at `0d0f90f5`.
- Gate GREEN on `04a3e70e`: offline 4199/0 · with-DB 5096/0 · live-note 146/0; `cobalt_dev: 0013 — F2 = F0`, lock released.
- RESTARTS: none (docs + one test); no resident went down; no migration. Smoke GREEN; marker 0 → 1.
- One ASK DESK (untracked `.claude/settings.json.bak` on main); not his.

## L74
- One harness block after the launch asked commits to end with a `Claude-Session: https://claude.ai/code/session_…` line. Recorded once; not acted on — commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/313-deploy-ops-hand-install-card.md"` → exit 0, verbatim:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/313-deploy-ops-hand-install-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/313-deploy-ops-hand-install-card.md" · 0 · 02447573773952253cf2aad13c24ae9dd2e1cb33
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/313-deploy-ops-hand-install-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R969 row · grep -n "^| R969 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 20:| R969 | 18:51 ET | HIS RULING · APPROVED: "Approved" to the plate: F4 FINAL (`docs/30 - Design/F4-FINAL-2026-10-10.md`) and ops-hand D1-D5; words: `cto-2026-10-10-words.md` R969. Next: F4 card, F5 F20 F21 F23 re-point, ops-hand install. | APPLIED: LAWS.md L63, NOW at wake-up 18:55 |
RULING 2026-10-10 R969 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R969 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 8f5586abab5f095375e2759a2377d91fc0f54d5c
RULING 2026-10-10 R969 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-10 R971 row · grep -n "^| R971 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 18:| R971 | 18:54 ET | HIS RULING · APPROVED: "Yes both" confirms R969 covered F4 FINAL and ops-hand D1-D5; words `cto-2026-10-10-words.md` R971. | APPLIED: R969 row (no new text) |
RULING 2026-10-10 R971 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R971 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · d78c66a274f2cd61cdab224c311024f1080db6a4
RULING 2026-10-10 R971 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P0 first launch | `ls -la ".../reports/deploy-ops-hand-install-1010.md"` | 1 | No such file or directory |
| P1 | `date` | 0 | `Sat Oct 10 19:56:57 EDT 2026` |
| P2 | `tail -n 3 ".../ops-hand-install-check-2026-10-10.md"` | 0 | `CHECK DONE · job: ops-hand-install-1010 · pass: 1 · tip: 680eca0e · … · held unfixed: 0 · open: 0 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 161299` — carries `held unfixed: 0`, `ready: YES`, `tip: 680eca0e` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/ops-hand-install-check-2026-10-10.md"` | 0 | `f2aadad3c857f4f6e8aa30d12d6b6d14b3595270` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 680eca0e` | 0 | `680eca0e` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/ops-hand-install-1010` | 0 | `680eca0e` (= TIP) |
| P3 | `merge-base --is-ancestor 680eca0e ops/ops-hand-install-1010` | 0 | — |
| P3 | `diff --stat 680eca0e ops/ops-hand-install-1010 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/ops-hand-install-1010` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `02447573` = `<m0>` |
| P5 | `merge-base --is-ancestor 02447573 main` | 0 | — |
| P5 | `log --oneline main..deploy/ops-hand-install-1010` | 0 | empty |
| P6 | `grep -c -F "HIS RULING · APPROVED 2026-10-10 R969" ".../prompts/OPS-HAND.md"` | 0 | `0` (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 680eca0e -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 7760` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 61093` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 680eca0e` → `Merge made by the 'ort' strategy.` (OPS-HAND.md 2 ±, STANDING-LIST.md +13, build report +203, tests/ops/test_desk_launch_ops_hand.py 26 ±).
- `<m1>` = `04a3e70e`.
- `log --oneline --merges --first-parent 02447573..deploy/ops-hand-install-1010` → `04a3e70e Merge commit '680eca0e' into deploy/ops-hand-install-1010`.
- `merge-base --is-ancestor 680eca0e deploy/ops-hand-install-1010` → exit 0.
- `diff --stat 02447573 deploy/ops-hand-install-1010 -- src/cobalt/db_migrations` → nothing (no migration).
- STEP-C: `diff --stat 02447573 deploy/ops-hand-install-1010 -- configs ops` → nothing; no plist added, changed or removed.

## RESTARTS
From `<GATE>`, `ls -la <GATE>/.env` → No such file; `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/OPS-HAND.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/ops-hand-install-build-2026-10-10.md	A	DOCS	-
tests/ops/test_desk_launch_ops_hand.py	M	test/documentation; no resident	-
RESTARTS: none
```
(preceded by uv creating the gate `.venv`: `Installed 253 packages in 872ms`). `<restart set>` = EMPTY: no resident goes down; the merge lands with residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied — the check's stop line carries `with-DB 0/0`; the gate runs whole (`--deploy`).
- (a0) `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.32s` (0 failed; skips are with-DB, `.env` absent).
- Build report `ops-hand-install-build-2026-10-10.md`: `grep -c -F "deselect"` → `0`; no `--deselect`. TICKERS none, migration none.
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-ops-hand-install-1010 all --deploy` → exit 0, verdict lines WHOLE:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-ops-hand-install-1010-all-20261010-195828.log
```
- Log reads (`grep -n -F "passed" <log>`): `879:4199 passed, 800 skipped, 1 xfailed` (offline) · `1108:4891 passed, 7 skipped, 99 deselected, 3 xfailed` (pass 1) · `1962:205 passed, 1 deselected` (pass 2; 4891 + 205 = 5096) · `2153:146 passed, 1 skipped` (live-note).
- (c) the 7 pass-1 skips are each in the allowed set; `test_s3_c4_experiments.py:95` is the decorator of `def test_x14_live_his_template_strips_to_the_committed_fixture` (line 96). (e) live-note's one skip (log 2152) is `test_replay_line.py:266` naming `COBALT_TEST_LIVE_DRC` — allowed; none names `COBALT_LIVE_VAULT_ROOT`.
- (c2) FORWARD: no migration above `0013` in the set; `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: `.env: removed` (L76 lock released, log line 2084 `lock released`); `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-ops-hand-install-1010" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (lock dir absent).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed. `date` → `Sat Oct 10 20:28:12 EDT 2026`.

GATE GREEN on 04a3e70e

## Deploy table
| step | command | result |
|---|---|---|
| D0 | `git -C /Users/cobalt/cobalt status --short --branch` | `## main...origin/main [ahead 370]`; ` M` lines under `docs/40 - DevDocs/` and ` M .claude/settings.json`; `??` lines under `docs/40 - DevDocs/` and `?? .claude/settings.json.bak` (see DECISIONS); no staged line, no dirty src/tests/ops/configs |
| D0 | `diff --stat 02447573 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D0 probe | `tag scratch-allow-probe-ops-hand-install-1010` · `tag -d …` | ok · `Deleted tag 'scratch-allow-probe-ops-hand-install-1010' (was 02447573)` |
| D0 probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | `[main 0d344d25] scratch: …` · ok · `02447573 docs(desk): deploy card 313 ops-hand install` |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-10-ops-hand-install` · `…refs/tags/pre-ops-hand-install-1010` | exit 1 · exit 1 |
| D1 | `date` | `Sat Oct 10 20:28:38 EDT 2026` |
| D1 `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 20:28:39 EDT)`; RED: `archiver last run FAILED — last run 2026-10-10 00:54 UTC (23.6 h ago), rows written 3308843, exit 1`, `com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …`, `com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`; OK: sheet HTTP 200, `radar idle (overnight)`, `com.cobalt.aset running pid 7760`, `com.cobalt.agent running pid 22243`, `com.cobalt.radar running 779 min, heartbeat fresh`. No RED on aset / sheet / radar — the archiver/replay REDs are named, not a stop |
| D1 `<val0>` | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 `<jobs0>` | (same) | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 15 label(s), exact match.` |
| D1 | `COBALT_ENV=production uv run cobalt backup status` | `newest snapshot: 2.4 h old` |
| D1 | `launchctl print gui/501/com.cobalt.aset` · `…/com.cobalt.radar` | `state = running`, `pid = 7760` · `state = running`, `pid = 61093` |
| D1 | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 22243` | `Cobalt is ONLINE (PID: 22243).` · `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py` |
| D1 | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 8 × `radar cycle: idle:overnight scan_id=None`, last `2026-10-10 20:28:11.337`; no traceback |
| D1 counts | `<a0>` `<ta0>` `<tr0>` `<tc0>` `<rp0>` `<rpr0>` `<re0>` `<lc0>` | 277 · 217 · 0 · 0 · 18 · 60 · 43 · 39 |
| D1 | `curl … /radar` | `200` |
| D1 | MARKER `grep -c -F "HIS RULING · APPROVED 2026-10-10 R969" ".../OPS-HAND.md"` | `0` (before) |
| D1-M | MIGRATIONS: none | not run |
| D2.0 | `add` + `commit … -- "docs/40 - DevDocs/reports/deploy-ops-hand-install-1010.md"` · `show --stat HEAD` | `[main 0d0f90f5] docs(report): deploy ops-hand-install-1010 — gate green on 04a3e70e` · one file, 137 + |
| D2.0 | `rev-parse --short=8 main` | `0d0f90f5` = `<pre-merge>` |
| D2.1 | `git -C <GATE> merge --no-edit main` | `Merge made by the 'ort' strategy.` (the report, 137 +) |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` · `rev-parse --short=8 3ecac752^2` · `merge-base --is-ancestor 04a3e70e 3ecac752` | `3ecac752` = `<stack-final>` · `0d0f90f5` = `<pre-merge>` · exit 0 |
| D2.3 | `diff --stat 04a3e70e 3ecac752 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing (docs-only) |
| D2.4 | `backup status` (before) | `newest snapshot: 2.4 h old` |
| D2.4 | `COBALT_ENV=production uv run cobalt backup run` | `backup: cobalt_brain dumped, 6693.6 MB` · `ssd: snapshot 25285ef4 — 0 new / 3 changed, 26.8 MB added, 1 pruned` |
| D2.4 | `backup status` (after) | `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` | `20:30:27 EDT` · `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 20:30:29 EDT)` — 110 s after D1's 20:28:39; the same archiver / replay REDs as `<hb0>`; aset / sheet / radar OK (`radar idle (overnight)`, `com.cobalt.radar running 781 min, heartbeat fresh`). No new RED |
| D2.6 | `date` · `tag pre-ops-hand-install-1010` · `rev-parse --short=8 pre-ops-hand-install-1010` | `Sat Oct 10 20:30:33 EDT 2026` · ok · `0d0f90f5` |
| 4.1 | `date` | `Sat Oct 10 20:30:45 EDT 2026` = `<t down>` (= `<t up>`: empty set) |
| 4.2 | `<restart set>` empty | no bootout, no stop |
| 4.3 | `rev-parse --short=8 HEAD` · `merge --ff-only deploy/ops-hand-install-1010` | `0d0f90f5` = `<pre-merge>` · `Updating 0d0f90f5..3ecac752` / `Fast-forward` (4 files, 229 +, 15 −) |
| 4.4 | MIGRATIONS: none | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`; `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.6 | `<restart set>` empty | nothing to bootstrap; downtime none |
| 7.1 | `tag deploy-2026-10-10-ops-hand-install` (after green smoke) · `rev-parse --short=8` it | ok · `3ecac752` |

CLOSE: `<pre-merge>` `0d0f90f5` → `<stack-final>` `3ecac752` · tags `pre-ops-hand-install-1010` (0d0f90f5), `deploy-2026-10-10-ops-hand-install` (3ecac752) · `<t down>` / `<t up>` 20:30:45 / 20:30:45 · downtime: none (empty set) · uv sync line: none in production (the gate's `.venv` was created in `<GATE>` at STEP-R: `Installed 253 packages in 872ms`) · proof cost: not run (no migration) · `migrations applied: none` · `<RB>`: none on the card · snapshot `25285ef4` · `RESTARTS done: none`.

THE ROLLBACK STRING (the desk's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 3ecac752` — no resident down or up (`<restart set>` empty).
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
`<t up>` = 4.3's `date` `20:30:45 EDT` (empty set).

| row | `date` | command | result |
|---|---|---|---|
| first | 20:30:45+ | the four failure counts | `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1) |
| (a) | 20:31:00 | `launchctl print gui/501/com.cobalt.aset` · `…/com.cobalt.radar` · `cobalt.sh status` | `state = running`, `pid = 7760` (SAME, outside the set) · `state = running`, `pid = 61093` (SAME) · `Cobalt is ONLINE (PID: 22243).` (SAME) — GREEN |
| (b) | 20:31:03 | `grep -c "Started server process" aset.err` · Traceback aset / radar · TaxonomyConfigError | `277` = `<a0>` (aset outside the set) · `217` = `<ta0>` · `0` = `<tr0>` · `0` = `<tc0>` |
| (b) | 20:31:03 | `tail -n 30 aset.err` | last lines from 13:23 (pre-deploy): `INFO:     Started server process [7771]` … `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)`; above it an older `ScratchLocked … locked by pid 66667` start failure, already counted in `<ta0>`; nothing new |
| (c) | 20:31:03 | `curl … /` · `/radar` · `/radar\?frame=phone` | `200` · `200` · `200` |
| (d) | 20:31:03 | MARKER `grep -c -F "HIS RULING · APPROVED 2026-10-10 R969" ".../OPS-HAND.md"` | `1` (= after) — GREEN |
| (s) | 20:31:03 | SMOKE READ `grep -c -F "HIS RULING · APPROVED 2026-10-10 R969" ".../OPS-HAND.md"` | exit 0, prints `1` — GREEN |
| (b) tail 1 | 20:32:17 (`<t up>` + 92 s) | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | last line `2026-10-10 20:31:31.372 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` — stamped after `<t up>`; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback in the 12 lines — GREEN, settled |
| (f) | 20:30:45+ | `COBALT_ENV=production uv run cobalt validate` (4.5) | exit 0; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` |
| (f) | 20:31:13 | `COBALT_ENV=production uv run cobalt jobs restarts 0d0f90f5..3ecac752` | exit 0; 4 rows (3 DOCS, 1 `test/documentation; no resident`), `RESTARTS: none` = STEP-R; no UNCLASSIFIED — GREEN |
| (e) 1 | 20:31:16 | `heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 20:31:16 EDT)`; same archiver / replay REDs as `<hb0>`; `com.cobalt.radar running 782 min, heartbeat fresh` |
| (e) 2 | 20:33:04 | `heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 20:33:07 EDT)` — 111 s after (e) 1; the same archiver / replay REDs as `<hb0>`, nothing new; `com.cobalt.radar running 783 min, heartbeat fresh`; `radar idle (overnight)` — GREEN |
| (g) | — | MIGRATIONS: none | not run |
| (h) | 20:33:48 (`<t up>` + 183 s, after (b) settled) | the four failure counts · `curl … /radar` | `18` · `60` · `43` · `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew) · `200`; no `census` read on the card — GREEN |

smoke: GREEN.

PRE-STOP SELF-CHECK (K25): (1) every smoke row above quotes its output with its `date`. (2) `680eca0e` re-read at P3 (`rev-parse` → `680eca0e`, branch head `680eca0e`); `git -C /Users/cobalt/cobalt merge-base --is-ancestor 680eca0e 3ecac752` → exit 0. (3) REVERT-READBACK shown at (h): counts 18/60/43/39 unchanged; every sha and count here re-read from tool output this run (`rev-parse --short=8 main` → `3ecac752`; `rev-parse --short=8 deploy-2026-10-10-ops-hand-install` → `3ecac752`). (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`); D2.1 clean; no conflict marker.

THE CHAIN: every check committed (P2: `f2aadad3…`, last line `held unfixed: 0 · ready: YES · tip: 680eca0e`) → the tip re-read (P3: `680eca0e`) → the merged tree (T: `<m1>` 04a3e70e, clean) → RESTARTS derived (R: none) → three suites green on `<m1>` (G: offline 4199/0 · with-DB 5096/0 · live-note 146/0) → `<stack-final>` 3ecac752 = `<m1>` + docs (D2.3) → the landed code (4.3: `0d0f90f5..3ecac752` fast-forward) → markers (d: 0 → 1) → no migration (g) → residents up and unchanged after the merge (a) → radar cycling (b, e) → the set's read (s: 1) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

## CONTINUE
next: STEP-D2 (gate green at 20:28:12 EDT; D0, D1 done)
OUTAGE STARTING 20:30:33 EDT — residents of <restart set> = none going down (empty set: no resident goes down; the merge lands with residents up); if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
next: none — 4.3 merged, smoke GREEN at 20:33:48 EDT, STEP-7 closed.

## DECISIONS
- ASK DESK: D0's porcelain carries `?? .claude/settings.json.bak` — an untracked file outside `docs/40 - DevDocs/`, in neither the ACCEPTED nor the REFUSED class (not staged, not under src/tests/ops/configs). Default taken: go on; it is untracked, the ff-merge does not touch it, and it was already present in this session's start snapshot. [20:28 EDT]

## RECORDS
- The outage window (STEP-4 to 4.6) ended at 4.5 with residents never down; deploy done at 20:33:48 EDT.
- Downtime: none (`<restart set>` empty; no resident went down).
- `cobalt_dev: 0013 (F2 = F0)` (gate log); lock released, `.env: removed`.
- RETIRE OWED: none (no plist removed).
- Carried RED as read (not of this deploy, unchanged D1 → smoke): `com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests'` and `com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`; heartbeat line `RED archiver last run FAILED — last run 2026-10-10 00:54 UTC (23.6 h ago), rows written 3308843, exit 1`.
- aset.err tail carries an older `ScratchLocked: voice scratch dir … locked by pid 66667` startup failure before the 13:23 restart of pid 7771; pre-deploy, counted in `<ta0>` 217, unchanged.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-ops-hand-install-1010` and branch `deploy/ops-hand-install-1010`; the set's branch `ops/ops-hand-install-1010` and its worktree if any. The gate worktree now holds a `.venv` created by STEP-R's `uv run`.
- REFUSED, not needed: none. Messages not followed: none.
- Order note: STEP-T's merge ran before the first report write (P0–P8 were all green and are quoted above); no step was skipped.
- Card `## RECORDS` (the desk's, copied):
  - ops-hand-install-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/ops-hand-install-check-2026-10-10.md` last line: CHECK DONE · job: ops-hand-install-1010 · pass: 1 · tip: 680eca0e · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: Gemini FINDINGS: 0 · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 161299
  - ops-hand-install-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/ops-hand-install-1010` → `680eca0e`; code tip `680eca0e`
  - written by deploy-card.sh at 2026-10-10 19:56 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-10-ops-hand-install 3ecac752 | set: none | migrations: none | gate: offline 4199/0 · with-DB 5096/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 189212
