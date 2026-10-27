# deploy f4-strike-reserve · SET: f4-strike-reserve · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/f4-strike-reserve` (code tip `a79fca72`, head `48d45bed`) on DEPLOY-HUB, card 1076. In progress.

## L74
- The session's harness attribution reminder asked commits to carry a `Claude-Session:` line. DATA (L74): recorded once, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1076-deploy-f4-strike-reserve-card.md"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1076-deploy-f4-strike-reserve-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-26/1076-deploy-f4-strike-reserve-card.md" · 0 · 67fbab4e4e5ef52f5499311939f9608ba9fc88ea
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-26/1076-deploy-f4-strike-reserve-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
AUTHORIZED
```
RULINGS: none.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above); `ls -la <REPORT>` | 0 · 1 | AUTHORIZED; report `No such file or directory` (first launch) |
| P1 | `date` | 0 | `Mon Oct 26 23:31:26 EDT 2026` — outside 21:30-22:30 ET |
| P2 | `tail -n 3 ".../f4-strike-reserve-check-2026-10-26.md"` | 0 | `CHECK DONE · job: f4-strike-reserve · pass: 1 · tip: a79fca72 · ... · held unfixed: 0 · open: 0 · ... · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 232103` — `held unfixed: 0`, `ready: YES`, `tip: a79fca72` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/f4-strike-reserve-check-2026-10-26.md"` | 0 | `bf5aaaf7b4fe361e2760053627cc3278fc59152c` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 a79fca72` | 0 | `a79fca72` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f4-strike-reserve` | 0 | `48d45bed` = TIP |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor a79fca72 48d45bed` | 0 | ancestor |
| P3 | `git -C /Users/cobalt/cobalt diff --stat a79fca72 48d45bed -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no lock held |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/f4-strike-reserve` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `67fbab4e` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 67fbab4e main` | 0 | ancestor |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/f4-strike-reserve` | 0 | empty |
| P6 | the five `## MARKERS` greps | 0/1 | `0` · `0` · `0` · `0` · `0` = every `before` |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 48d45bed -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 76357 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 76377 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1` — com.cobalt.agent recorded retired |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is OFFLINE.` (retired: expected) |

## THE TREE
- `git -C <GATE> merge --no-edit 48d45bed` → `Merge made by the 'ort' strategy.` (23 files, 698+, 44-).
- `git -C <GATE> rev-parse --short=8 HEAD` → `<m1>` = `708e60ba`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 67fbab4e..deploy/f4-strike-reserve` → `708e60ba1 Merge commit '48d45bed' into deploy/f4-strike-reserve` (one line, one head).
- `merge-base --is-ancestor a79fca72 deploy/f4-strike-reserve` → exit 0; `merge-base --is-ancestor 48d45bed deploy/f4-strike-reserve` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 67fbab4e deploy/f4-strike-reserve -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 67fbab4e deploy/f4-strike-reserve -- configs ops` → ` configs/cobalt/taxonomy/tunables.yaml | 9 +++++++++` / ` 1 file changed, 9 insertions(+)`. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 67fbab4e deploy/f4-strike-reserve` → exit 0, whole: `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (first lines: uv created the gate's `.venv`, `Installed 257 packages in 862ms`), table WHOLE:
```
path	change	rule	restart
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
docs/30 - Design/F4-FINAL-2026-10-10.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/daily.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/collector.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/runner.md	M	DOCS	-
docs/40 - DevDocs/cobalt/strike/detector.md	M	DOCS	-
docs/40 - DevDocs/reports/f4-strike-reserve-build-2026-10-26.md	A	DOCS	-
docs/40 - DevDocs/reports/f4-strike-reserve-build-2026-10-26.result	A	DOCS	-
src/cobalt/prefill/daily.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/prefill/refresh_probe.py	M	static import reach	-
src/cobalt/radar/collector.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/radar/config.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/strike/detector.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_prefill_refresh.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_collector.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_config.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_price_floor.py	M	test/documentation; no resident	-
tests/cobalt/test_refresh_probe.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_d1.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_registries.py	M	test/documentation; no resident	-
tests/cobalt/test_strike_detector.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row. NOT LOADED read: `launchctl print gui/501/com.cobalt.cos` → exit 0, `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.cos.plist`, pid 76369 → kept.
- `<restart set>` = `com.cobalt.aset com.cobalt.cos com.cobalt.radar`
- `<deferred set>` = empty · `<launchd set>` = empty
- com.cobalt.agent: recorded retired — not restarted (not in the derived set either)

## L68 GATE
EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat a79fca72 708e60ba -- . ":(exclude)docs"` → ` configs/cobalt/rules.yaml | 2 +-` → not equal; the gate runs whole.
- (a0) `ls -la <GATE>/.env` → No such file · the 17-file early read → `265 passed, 163 skipped in 19.52s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db`).
- Build report deselects: none (`f4-strike-reserve-build-2026-10-26.md:165` "no `--deselect`, no `--tickers`"). TICKERS: none. No migration.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-f4-strike-reserve all --deploy --deploy-gate` (background) → exit 0, verdict WHOLE:
```
tests/ops: run (deploy gate)
offline 9174/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 6010/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-f4-strike-reserve-all-20261026-233311.log
```
- (a) offline `<p>` = 9174 (log `:958` `5038 passed, 878 skipped, 4 xfailed …`; `:1033` `4136 passed, 1 xfailed …` = tests/ops, deploy gate); `tests/ops: run (deploy gate)`.
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:1050`); LEVEL 0013; proof-only nothing CHANGED.
- (c) PASS 1 `<d1>` = 5766 (log `:1278` `5766 passed, 9 skipped, 138 deselected, 7 xfailed, 43 warnings in 946.56s`). All nine SKIPPED lines inside the allowed set (`test_cards_picks.py:388`, `:401`, `test_checkpoints_live.py` dry-run test / `COBALT_LIVE_VAULT_ROOT not set`, `test_playbook_live.py` / same, `test_radar_evaluate.py:695`, `test_replay_line.py` / `COBALT_TEST_LIVE_DRC`, `test_s3_c4_experiments.py` / x14, `test_catalyst.py:365`, `test_predicate.py:262`).
- (c2) `dev forward: APPLIED 00:17:38` (log `:1280`).
- (c3) PASS 2 `<d2>` = 244 (log `:2260` `244 passed, 1 deselected, 5 warnings in 245.28s`) → `with-DB 6010/0`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:2334`) = F0 → `cobalt_dev: 0013 — F2 = F0`.
- RELEASE: `.env: removed (L76 lock released, log :2390, before 00:23:13)`; `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-f4-strike-reserve" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) live-note `<l>` = 148 (log `:2461` `148 passed, 1 skipped`; the one skip is `COBALT_TEST_LIVE_DRC`).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 708e60ba

## Deploy table
| step | command | result |
|---|---|---|
| D0 MAIN | `git -C /Users/cobalt/cobalt status --short --branch` / porcelain | `## main...origin/main [ahead 14]`; only ` M .claude/settings.json`, ` M`/`??` under `docs/40 - DevDocs/`, `?? .claude/settings.json.bak` (see RECORDS); no staged line |
| D0 MAIN | `git -C /Users/cobalt/cobalt diff --stat 67fbab4e main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D0 PROBE | `tag scratch-allow-probe-f4-strike-reserve` · `tag -d …` · `commit --allow-empty …` · `reset --soft HEAD~1` · `log --oneline -1` | `Deleted tag 'scratch-allow-probe-f4-strike-reserve' (was c8a4626e6)` · `[main 4b21d5c98] scratch: …` · HEAD back `c8a4626e6 chore(generated): nightly rewrite 2026-10-26` |
| D0 TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-26-f4-strike-reserve` · `refs/tags/pre-f4-strike-reserve` | exit 1 · exit 1 |
| D1 | `date` · `heartbeat show` → `<hb0>` | `Tue Oct 27 00:23:41 EDT 2026` · `HEARTBEAT RED — 1 job(s)`: the one RED `com.cobalt.agent not loaded` (recorded retired; not aset/sheet/radar — named, not a stop). `OK sheet HTTP … 200`, `OK radar idle (overnight)`, `OK cos loop stamping`, `OK com.cobalt.aset running pid 76357`, `OK com.cobalt.radar running 221 min, heartbeat fresh`, `OK com.cobalt.cos running 221 min, heartbeat fresh`; `com.cobalt.prefill-refresh`, `checkpoint-0715/0745/0815/0845`, `playbook` OWED (deferred bootstrap) |
| D1 | `validate` → `<val0>` | exit 0; `<jobs0>` = `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`; `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 | `backup status` | `newest snapshot: 2.7 h old` |
| D1 | `launchctl print` aset · radar · cos | `state = running` · pids aset 76357, radar 76377, cos 76369 |
| D1 | `cobalt.sh status` | `Cobalt is OFFLINE.` (agent recorded retired; no `ps -p`) |
| D1 | `tail -n 8 radar.err` | last `2026-10-27 00:22:33.268 … radar cycle: idle:overnight scan_id=None`, no traceback |
| D1 | log baselines | `<a0>` 301 · `<ta0>` 217 · `<tr0>` 1 · `<tc0>` 0 · `<rp0>` 31 · `<rpr0>` 60 · `<re0>` 750 · `<lc0>` 39 |
| D1 | `curl … /radar` | `200` |
| D1 | `## MARKERS` again | `0` `0` `0` `0` `0` = before |
| D1 | THE LAUNCHD SET · migration reads | empty · none (MIGRATIONS: none) |

## CONTINUE
next: STEP-D2 (D2.0 commit)

## DECISIONS

## RECORDS
- REFUSED, not needed: `grep -n -F ".env: removed" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it` (the release was read instead from `grep -n -F "lock released" <log>` → `:2390`).
- `?? .claude/settings.json.bak` on `main` (untracked, outside the D0 accepted list's wording; not under `src/`, `tests/`, `ops/`, `configs/`, so not a refused path) — recorded, not a stop.

(run in progress — next step under ## CONTINUE)
