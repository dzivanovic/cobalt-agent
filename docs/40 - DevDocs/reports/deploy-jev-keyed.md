# deploy — jev-keyed · SET: none · MIGRATIONS: none

## §0 Headline
(in progress)

## L74
- A harness block during this run asked that commits end with a `Claude-Session:` line. Recorded as data (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/776-deploy-jev-keyed-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/776-deploy-jev-keyed-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/776-deploy-jev-keyed-card.md" · 0 · 43b0dc152dfa77ada5bd872da1587556494c3abe
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/776-deploy-jev-keyed-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1830 row · grep -n "^| R1830 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 95:| R1830 | 06:14 ET | HIS RULING: yes to JEV F12 (keyed wrapper allow string); "no card needed, run tribunal and JEV build". Words: [cto-2026-10-18-words.md#R1830](cto-2026-10-18-words.md). Asked brain what remains and what "no card" covers. | HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46 |
RULING 2026-10-18 R1830 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1830 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 15af08b4218bdb9fb80c52ab7fa7784c9f14bf86
RULING 2026-10-18 R1830 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-jev-keyed.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Sun Oct 18 15:29:15 EDT 2026` — outside 21:30-22:30 |
| P2 | `tail -n 3 ".../reports/jev-keyed-check-2026-10-18.md"` | 0 | `CHECK DONE · job: jev-keyed-1018 · pass: 1 · tip: 9780e4eb · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8514/0 · with-DB 5476/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 16 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 178753` — carries `held unfixed: 0`, `ready: YES`, `tip: 9780e4eb` = row's code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/.../jev-keyed-check-2026-10-18.md"` | 0 | `13ccb79b4e088ef9a5be31095b529f8e799222ab` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../jev-keyed-check-2026-10-18.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 9780e4eb` | 0 | `9780e4eb` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 feat/jev-keyed-1018` | 0 | `df6a000f` = row's head = `TIP` |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 9780e4eb df6a000f` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 9780e4eb df6a000f -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no lock held |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-jev-keyed status --short --branch` | 0 | `## deploy/jev-keyed` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-jev-keyed rev-parse --short=8 HEAD` | 0 | `11e4334d` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 11e4334d main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/jev-keyed` | 0 | empty |
| P6 | `ls /Users/cobalt/cobalt/ops/jev-route.sh` | 1 | `ls: /Users/cobalt/cobalt/ops/jev-route.sh: No such file or directory` = before |
| P6 | `grep -c -F "Bash(sh /Users/cobalt/cobalt/ops/jev-route.sh --day *)" ".../prompts/CLOSE-HUB.md"` | 1 | `0` = before |
| P6 | `grep -c -F "## 7b. JEV SHADOW BATCH" ".../prompts/CLOSE-HUB.md"` | 1 | `0` = before |
| P6 | `grep -c -F "ops/jev-route.sh" /Users/cobalt/cobalt/src/cobalt/jobs/restarts.py` | 1 | `0` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main df6a000f -- src/cobalt/db_migrations` | 0 | nothing — `MIGRATIONS: none` holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 89330` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 89340` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 89351).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| T merge | `git -C /Users/cobalt/cobalt-wt/deploy-jev-keyed merge --no-edit df6a000f` | 0 | `Merge made by the 'ort' strategy.` — 10 files changed, 649 insertions(+), 7 deletions(-): `docs/40 - DevDocs/cobalt/jobs/restarts.md`, `docs/40 - DevDocs/prompts/CLOSE-HUB.md`, `.../reports/jev-keyed-build-2026-10-18.md`, `.../reports/jev-keyed-build-2026-10-18.result`, `ops/jev-route.sh`, `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jev_shadow_1015.py`, `tests/cobalt/test_jobs_restarts.py`, `tests/ops/test_jev_route_1018.py`, `tests/ops/test_needs_his_hand.py` |
| `<m1>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `c95e7241` |
| merges | `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 11e4334d..deploy/jev-keyed` | 0 | `c95e7241 Merge commit 'df6a000f' into deploy/jev-keyed` |
| ancestry | `merge-base --is-ancestor 9780e4eb deploy/jev-keyed` · `… df6a000f deploy/jev-keyed` | 0 · 0 | — |
| migrations | `git -C /Users/cobalt/cobalt diff --stat 11e4334d deploy/jev-keyed -- src/cobalt/db_migrations` | 0 | nothing — `MIGRATIONS: none` |
| C configs/ops | `git -C /Users/cobalt/cobalt diff --stat 11e4334d deploy/jev-keyed -- configs ops` | 0 | ` ops/jev-route.sh | 26 ++++++++++++++++++++++++++` / ` 1 file changed, 26 insertions(+)` |
| C script | `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 11e4334d deploy/jev-keyed` | 0 | `STEP-C: ADMITTED 0` → `<launchd set>` empty |

## RESTARTS
`COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` (in `<GATE>`, `.env` absent) → exit 0 (after a first-use `uv` venv build: `Installed 256 packages in 926ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/jobs/restarts.md	M	DOCS	-
docs/40 - DevDocs/prompts/CLOSE-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/jev-keyed-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/jev-keyed-build-2026-10-18.result	A	DOCS	-
ops/jev-route.sh	A	operator script; no Cobalt reader	-
src/cobalt/jobs/restarts.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_jev_shadow_1015.py	M	test/documentation; no resident	-
tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
tests/ops/test_jev_route_1018.py	A	test/documentation; no resident	-
tests/ops/test_needs_his_hand.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.radar` · `<launchd set>` = none.

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 9780e4eb c95e7241 -- . ":(exclude)docs"` → 40 files changed, 4190 insertions(+), 84 deletions(-) (`main` moved since the check tip) → the clause does not hold; the gate runs whole.
- (a0) `uv run pytest -q -rs -p no:cacheprovider <17 files>` → `264 passed, 163 skipped in 18.55s` (0 failed; the skips are with-DB tests without Postgres env).
- Gate: `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-jev-keyed all --deploy --deploy-gate` (no `--deselect`: the build report says "this build deselects nothing"; no `--tickers`, no `--migration`) → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8603/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5582/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-jev-keyed-all-20261018-153113.log
```
- SKIPPED lines: all inside the allowed set. `test_playbook_live.py:31` is the decorator of `test_live_vault_renders_six_decks` (`:32`); `test_s3_c4_experiments.py:95` is the decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (`:96`); the others are the set's listed lines.
- Log reads: `1014:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `1235:dev forward: APPLIED 16:12:27` · `2237:lock released` · `cobalt_dev: 0013 — F2 = F0`.
- RELEASE: `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file. `.env: removed (L76 lock released, log :2237)`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on c95e7241 — offline 8603/0 · with-DB 5582/0 · live-note 147/0

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 161]`; ` M .claude/settings.json`, ` M` / `??` under `docs/40 - DevDocs/`, and `?? .claude/settings.json.bak` (see `## RECORDS`); no staged line, no dirty `src/` `tests/` `ops/` `configs/` path |
| MAIN moved | `git -C /Users/cobalt/cobalt diff --stat 11e4334d main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe | `tag scratch-allow-probe-jev-keyed` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-jev-keyed' (was 11e4334d)` |
| probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 24eae6b2] scratch: …` · — · `11e4334d docs(desk): R1914-R1917 agy-read deployed, …` (HEAD back) |
| tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-18-jev-keyed` · `… refs/tags/pre-jev-keyed` | 1 · 1 | both free |

### STEP-D1 (baseline, `date` → `Sun Oct 18 16:18:39 EDT 2026`)
- `<hb0>`: `HEARTBEAT GREEN — 17 job(s), 12 probe(s), nothing red  (2026-10-18 16:18:40 EDT)`; `OK   radar                    idle (overnight)`; `OK   com.cobalt.radar             running   running 144 min, heartbeat fresh`; `AMB  com.cobalt.herdr …unmanaged…` (declared interim); `com.cobalt.prefill-refresh` and `com.cobalt.playbook` `OWED (deferred bootstrap)` (listed in `bootstrap-owed.json`, not red). No RED.
- `<val0>`: `cobalt validate` → exit 0, `13 trade_def(s) validated OK from the vault.`, `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 17 registered — 6 resident, 11 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 0.9 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 89330` (`<aset pid>`); `… com.cobalt.radar` → `state = running`, `pid = 89340` (`<radar pid>`); `cobalt.sh status` → `Cobalt is ONLINE (PID: 89351).`; `ps -p 89351` → `89351 ??         0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last `2026-10-18 16:18:14.084 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (one per ~100 s, no traceback).
- Log baselines: `<a0>` 283 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS → `No such file or directory` · `0` · `0` · `0` (each its before).
- `<launchd set>` empty: nothing. `MIGRATIONS: none`: no `<RB>`, no proof-only.

## Smoke

## CONTINUE
next: STEP-D2 (D1 baseline at 16:18:39)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
