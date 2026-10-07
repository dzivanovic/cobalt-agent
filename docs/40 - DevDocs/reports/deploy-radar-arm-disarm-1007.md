# deploy radar-arm-disarm-1007 · set: none · migrations: none

## §0 Headline
Card 92 is live (radar card ARM / DISARM taps, R627): `main` 0e784e51 → a627c96b, tag `deploy-2026-10-07-radar-arm-disarm`.
Gate: the check's suites on the equal tree, offline 3991/0 · with-DB 4875/0 · live-note 146/0. No migration.
aset and radar restarted, 19 s down (15:59:11 → 15:59:30); smoke GREEN, no failure count grew.
Rollback: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 a627c96b`. The live tap is the desk's to confirm with him.

## L74
- A system reminder after a tool read asked commits to carry a `Claude-Session:` line. Recorded as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/102-deploy-radar-arm-disarm-card.md"` → exit 0, output WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/102-deploy-radar-arm-disarm-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-07/102-deploy-radar-arm-disarm-card.md" · 0 · e1f7808933d532015f082d5fb3ad8445a42025b5
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-07/102-deploy-radar-arm-disarm-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-07 R627 row · grep -n "^| R627 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 21:| R627 | 10:24 ET | HIS RULING (words: `cto-2026-10-07-words.md` R627, "yes"): card an ARM and a DISARM control on the radar card (none exists; the S3 smoke cannot reach FILLED without it). LAUNCHING a drafter, prompt `91`. | HIS RULING · APPROVED |
RULING 2026-10-07 R627 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R627 |" -- "docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 95e40f47c081f2a84ca4729118dd1a1260af94d5
RULING 2026-10-07 R627 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "<REPORT>"` | 1 | No such file or directory |
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| P1 DATE | `date` | 0 | Wed Oct  7 15:54:39 EDT 2026 |
| P2 check last line | `tail -n 3 "…/radar-arm-disarm-check-2026-10-07.md"` | 0 | `CHECK DONE · job: radar-arm-disarm · pass: 1 · tip: 0544f91d · … · held unfixed: 0 · … · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165017` — tip = code tip |
| P2 committed | `git log -1 --format=%H -- "docs/…/radar-arm-disarm-check-2026-10-07.md"` | 0 | 5c5301dd73c41f496233f24810eca2f3adb56a71 |
| P2 clean | `git diff --stat -- "docs/…/radar-arm-disarm-check-2026-10-07.md"` | 0 | (nothing) |
| P3 code tip | `rev-parse --short=8 0544f91d` | 0 | 0544f91d |
| P3 head | `rev-parse --short=8 ops/radar-arm-disarm-1007` | 0 | e9600951 (= TIP) |
| P3 ancestor | `merge-base --is-ancestor 0544f91d e9600951` | 0 | — |
| P3 docs only | `diff --stat 0544f91d e9600951 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — lock free |
| P5 status | `git -C <GATE> status --short --branch` | 0 | `## deploy/radar-arm-disarm-1007` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = e1f78089 |
| P5 on main | `merge-base --is-ancestor e1f78089 main` | 0 | — |
| P5 empty | `log --oneline main..deploy/radar-arm-disarm-1007` | 0 | (empty) |
| P6 marker ARM | `grep -c -F "/radar/card/{card_id}/arm" …/web.py` | 1 | 0 (before) |
| P6 marker DISARM | `grep -c -F "/radar/card/{card_id}/disarm" …/web.py` | 1 | 0 (before) |
| P6 marker test | `grep -c -F "def test_radar_arm_and_disarm_taps_render_on_watch_and_armed_only" …/test_radar_panel_cards.py` | 1 | 0 (before) |
| P7 migrations | `diff --stat main e9600951 -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 96145 |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 96165 |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit e9600951` → `Merge made by the 'ort' strategy.` (7 files: `radar_panel.py`, `web.py`, two test files, three docs; 489 insertions, 3 deletions).
- `<m1>` = `git -C <GATE> rev-parse --short=8 HEAD` → `5005ab4f`.
- `log --oneline --merges --first-parent e1f78089..deploy/radar-arm-disarm-1007` → `5005ab4f Merge commit 'e9600951' into deploy/radar-arm-disarm-1007` (one line, one head).
- `merge-base --is-ancestor 0544f91d deploy/radar-arm-disarm-1007` → exit 0; `… e9600951 …` → exit 0.
- `diff --stat e1f78089 deploy/radar-arm-disarm-1007 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `diff --stat e1f78089 deploy/radar-arm-disarm-1007 -- configs ops` → nothing. No plist added, changed or removed.

## RESTARTS
From `<GATE>`, `ls -la <GATE>/.env` → No such file; `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (first `uv` run in the worktree created `.venv`, 253 packages):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-arm-disarm-build-2026-10-07.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar`.

## L68 GATE
THE EQUAL-TREE CLAUSE holds: one branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat 0544f91d 5005ab4f -- . ":(exclude)docs"` → nothing; the check's stop line carries `with-DB 4875/0` (above 0). The check's suite lines are the gate's, quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-arm-disarm-check-2026-10-07.md` lines 137–154 (gate exit 0 at 15:53 EDT):
```
offline 3991/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4875/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-arm-disarm-1007-all-20261007-152528.log
```
SKIPPED read against the allowed set: all seven inside it (`test_s3_c4_experiments.py:95` is the `@requires_live` decorator of `test_x14_live_his_template_strips_to_the_committed_fixture`, read at `<GATE>/tests/cobalt/test_s3_c4_experiments.py:95-96`). (a)–(f) skipped by the clause.
(a0) THE EARLY READ, run anyway: `ls -la <GATE>/.env` → No such file; `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 163 skipped in 16.13s` (0 failed; the skips are with-DB tests with no Postgres env).
`cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed. `cobalt_dev` not touched by this run; no lock taken.

GATE GREEN on 5005ab4f

## Deploy table
STEP-D0:
| row | command | exit | result |
|---|---|---|---|
| main branch | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 90]` |
| main porcelain | `status --porcelain` | 0 | ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` under `docs/40 - DevDocs/` only, plus `?? .claude/settings.json.bak` (see DECISIONS); no staged line, no dirty `src/` `tests/` `ops/` `configs/` path |
| main moved | `diff --stat e1f78089 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | (nothing) |
| probe tag | `tag scratch-allow-probe-radar-arm-disarm-1007` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-radar-arm-disarm-1007' (was e1f78089)` |
| probe commit | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` / `reset --soft HEAD~1` / `log --oneline -1` | 0 / 0 / 0 | `[main 4af86e9e] …` → `e1f78089 docs(desk): card 92 CHECK DONE 0544f91d, deploy card 102, R649` |
| TAG free | `rev-parse --verify --quiet refs/tags/deploy-2026-10-07-radar-arm-disarm` | 1 | — |
| rollback tag free | `rev-parse --verify --quiet refs/tags/pre-radar-arm-disarm-1007` | 1 | — |

STEP-D1 (production baseline):
| row | command | result |
|---|---|---|
| time | `date` | Wed Oct  7 15:56:57 EDT 2026 |
| `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT RED — 1 probe(s)  (2026-10-07 15:56:58 EDT)`; every probe OK but `RED  radar                    failed_stage bars: poll failures: 1; poll RIBB stale since 2026-10-07T19:33:42.157760+00:00` (CARRIED FAMILY: radar `running 94 min, heartbeat fresh`, `radar cycle: scanning` at 15:56:45, no traceback) and `AMB com.cobalt.herdr unmanaged` (declared interim); `com.cobalt.aset running pid 96145`, `com.cobalt.agent running pid 22243` |
| `<val0>` | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Placement (docs/PLACEMENT.md): tree clean.` |
| `<jobs0>` | (validate) | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` |
| backup | `COBALT_ENV=production uv run cobalt backup status` | `newest snapshot: 1.6 h old` |
| aset | `launchctl print gui/501/com.cobalt.aset` (P8 read, 15:55) | `state = running`, `<aset pid>` = 96145 |
| radar | `launchctl print gui/501/com.cobalt.radar` (P8 read, 15:55) | `state = running`, `<radar pid>` = 96165 |
| agent | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 22243` | `Cobalt is ONLINE (PID: 22243).` · `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py` |
| radar tail | `tail -n 8 …/radar.err` | last line `2026-10-07 15:56:45.895 … radar cycle: scanning scan_id=1791402920505`; no traceback |
| `<a0>` | `grep -c "Started server process" …/aset.err` | 48 |
| `<ta0>` | `grep -c "Traceback" …/aset.err` | 2 |
| `<tr0>` | `grep -c "Traceback" …/radar.err` | 0 |
| `<tc0>` | `grep -c "TaxonomyConfigError" …/radar.err` | 0 |
| `<rp0>` | `grep -c "radar panel FAILED" …/aset.err` | 17 |
| `<rpr0>` | `grep -c "radar pool refresh FAILED" …/aset.err` | 58 |
| `<re0>` | `grep -c "radar S5 evaluate FAILED" …/radar.err` | 40 |
| `<lc0>` | `grep -c "lifecycle card read failed" …/radar.err` | 39 |
| /radar | `curl … http://127.0.0.1:5010/radar` | 200 |
| MARKERS | the three `## MARKERS` greps | 0 · 0 · 0 (before) |
| migration | MIGRATIONS: none | no `<RB>`, no proof-only |

STEP-D2:
| row | command | result |
|---|---|---|
| D2.0 | `add` + `commit … -- "docs/40 - DevDocs/reports/deploy-radar-arm-disarm-1007.md"` · `show --stat HEAD` | `[main 0e784e51] docs(report): deploy radar-arm-disarm-1007 — gate green on 5005ab4f`, one file · `<pre-merge>` = `rev-parse --short=8 main` → 0e784e51 |
| D2.1 | `git -C <GATE> merge --no-edit main` | `Merge made by the 'ort' strategy.` (the report, 1 file) |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` · `rev-parse --short=8 a627c96b^2` · `merge-base --is-ancestor 5005ab4f a627c96b` | `<stack-final>` = a627c96b · 0e784e51 (= `<pre-merge>`) · exit 0 |
| D2.3 | `diff --stat 5005ab4f a627c96b -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | (nothing) — docs only |
| D2.4 | `backup status` · `backup run` (foreground) · `backup status` | `newest snapshot: 1.6 h old` · `backup: cobalt_brain via pg_dump inside cobalt_memory — 5642.5 MB` · `ssd: snapshot 32fca157 — 0 new / 2 changed, 97.8 MB added, 1 pruned` · `newest snapshot: 0.0 h old` |
| D2.5 | `date` 15:58:50 · `heartbeat show` | `HEARTBEAT RED — 1 probe(s)  (2026-10-07 15:58:52 EDT)` — 114 s after D1's 15:56:58; only RED is the carried radar family, same text as `<hb0>`; aset pid 96145, radar `running 96 min, heartbeat fresh` |
| D2.6 | `date` · `tag pre-radar-arm-disarm-1007` | Wed Oct  7 15:58:57 EDT 2026 · rollback tag at 0e784e51 |

STEP-4 (the outage):
| row | command | result |
|---|---|---|
| 4.1 | `date` | `<t down>` = Wed Oct  7 15:59:11 EDT 2026 |
| 4.2 aset | `launchctl bootout gui/501/com.cobalt.aset` · `launchctl print …` | exit 0 · exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 radar | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print …` | exit 0 · exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.3 | `rev-parse --short=8 HEAD` · `merge --ff-only deploy/radar-arm-disarm-1007` | 0e784e51 (= `<pre-merge>`) · `Updating 0e784e51..a627c96b` / `Fast-forward`, 7 files, 489 insertions, 3 deletions |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` (= `<jobs0>`); `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.6 aset | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `launchctl print …` | exit 0 · `state = running`, pid 37788 (≠ 96145) |
| 4.6 radar | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `launchctl print …` | exit 0 · `state = running`, pid 37799 (≠ 96165) |
| 4.6 | `date` | `<t up>` = Wed Oct  7 15:59:30 EDT 2026 — downtime 19 s |

STEP-7 close:
- `<pre-merge>` 0e784e51 → `<stack-final>` a627c96b (`main` at a627c96b). Tags: `pre-radar-arm-disarm-1007` (0e784e51), `deploy-2026-10-07-radar-arm-disarm` (a627c96b, set after the green smoke).
- `<t down>` 15:59:11 / `<t up>` 15:59:30 / 19 s. uv sync line: none in production (the gate worktree's first `uv` call created its own `.venv`, 253 packages). Proof cost: none (no migration). `migrations applied: none`. `<RB>`: none.
- Snapshot: `ssd: snapshot 32fca157`.
- RESTARTS done: com.cobalt.aset com.cobalt.radar.
- THE ROLLBACK STRING (the desk's):
  1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 a627c96b` — aset and radar down first, up after.
  2. SCHEMA: none (no migration).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

THE CHAIN: check committed and clean, `ready: YES`, `held unfixed: 0` (P2) · tips 0544f91d / e9600951 re-read (P3) · merged tree 5005ab4f (T) · RESTARTS aset + radar, no UNCLASSIFIED (R) · three suites green on the equal tree, offline 3991/0 · with-DB 4875/0 · live-note 146/0 (G) · a627c96b = 5005ab4f + docs (D2.3) · landed by fast-forward (4.3) · markers 1/1/1 (d) · no migration (g) · residents up on new pids after the merge (a) · radar cycling at 16:00:52, heartbeat fresh (b, e) · the set's three reads green (s) · no failure count grew (h). The card surface (the ARM / DISARM taps on a live card) is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK: (1) every smoke row carries its `date` and quoted output (## Smoke). (2) `merge-base --is-ancestor 0544f91d a627c96b` → exit 0; `… e9600951 a627c96b` → exit 0; `rev-parse --short=8 main` → a627c96b. (3) REVERT-READBACK (h) shown at 16:02:35; every count and sha above was read this run. (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`); no conflict marker.
THE RELEASE: no lock taken this run; `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.

## Smoke
| row | date | command | result |
|---|---|---|---|
| first calls | after 15:59:30 | the four failure counts | `<rp_up>` 17 · `<rpr_up>` 58 · `<re_up>` 40 · `<lc_up>` 39 (= D1) |
| (a) | 15:59:42 | `launchctl print` aset / radar (4.6 reads) · `cobalt.sh status` | aset `state = running` pid 37788 (new) · radar `state = running` pid 37799 (new) · `Cobalt is ONLINE (PID: 22243).` (agent outside the set, same pid) |
| (b) | 15:59:42 | `grep -c "Started server process" …/aset.err` | 49 (`<a0>` 48 → +1) |
| (b) | 15:59:42 | `tail -n 30 …/aset.err` | `INFO:     Started server process [37794]` … `INFO:     Application startup complete.` / `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)` |
| (b) | 15:59:42 | Traceback aset · Traceback radar · TaxonomyConfigError radar | 2 · 0 · 0 (= baseline) |
| (c) | 15:59:49 | `curl … /` · `curl … /radar` · `curl … /radar\?frame=phone` | 200 · 200 · 200 |
| (d) | 15:59:49 | the three `## MARKERS` greps | 1 · 1 · 1 (after) |
| (s) | 15:59:49 | `## SMOKE READS`: ARM route · DISARM route · control test | exit 0, 1 · exit 0, 1 · exit 0, 1 — each a count of 1 or more: GREEN |
| (f) | 15:59:55 | `COBALT_ENV=production uv run cobalt jobs restarts 0e784e51..a627c96b` | exit 0; same 7 rows as STEP-R, no `UNCLASSIFIED`; `RESTARTS: com.cobalt.aset com.cobalt.radar` (= `<restart set>`) |
| (e) 1 | 15:59:57 | `heartbeat show` | `HEARTBEAT RED — 1 probe(s)  (2026-10-07 15:59:57 EDT)`; only RED = carried radar family, same text as `<hb0>`; `com.cobalt.aset running loaded, pid 37788`; `com.cobalt.radar running running 1 min, heartbeat fresh` |
| (f) | ~16:00 | `COBALT_ENV=production uv run cobalt validate` | exit 0; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` (= `<jobs0>`); `Placement (docs/PLACEMENT.md): tree clean.` |
| (g) | — | MIGRATIONS: none | no `<RB>` |
| (b) radar | 16:01:03 (`<t up>` + 93 s) | `tail -n 12 …/radar.err` | `2026-10-07 16:00:52.052 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791403166075` (after `<t up>`); the other 11 lines `cards.expire: falling back to the session close` INFO; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → GREEN, settled at the first tail |
| (h) | 16:02:35 (`<t up>` + 185 s) | the four failure counts · `curl … /radar` · `launchctl print` aset / radar | 17 · 58 · 40 · 39 (= `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, none growing) · 200 · aset `state = running` pid 37788, radar `state = running` pid 37799 → GREEN. No `census` read on the card |
| (e) 2 | 16:01:46 | `heartbeat show` | `HEARTBEAT RED — 1 probe(s)  (2026-10-07 16:01:48 EDT)` — 111 s after (e) 1; only RED = carried radar family, text unchanged from `<hb0>`; `com.cobalt.radar running running 2 min, heartbeat fresh`; aset pid 37788 → GREEN |

## CONTINUE
next: STEP-T
next: STEP-C
next: STEP-R
next: STEP-G
next: STEP-D0 (gate green at 15:56:21 EDT)
next: STEP-D2 (D0, D1 clean)
OUTAGE STARTING 15:58:57 EDT — residents of com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
next: STEP-4.7 smoke — residents UP at 15:59:30 on a627c96b; radar tails and (e) 2, (h) pending
next: STEP-7 — smoke GREEN at 16:02:35; tagged; closing

## DECISIONS
- ASK DESK: `git status --porcelain` on `main` shows `?? .claude/settings.json.bak` — not on D0's ACCEPTED list and not in its REFUSED classes (no staged line, not `src/` `tests/` `ops/` `configs/`); present at session start. Safe default taken: go on; it is untracked, outside every path the set touches, and the `--ff-only` merge does not read it. [15:57 EDT]

## RECORDS
- Downtime 19 s (15:59:11 → 15:59:30); under 300 s.
- REFUSED, not needed: none. No `CONTINUE` message arrived.
- `cobalt_dev`: not touched by this run (EQUAL-TREE CLAUSE); the check's gate recorded `cobalt_dev: 0013 — F2 = F0`.
- RETIRE OWED: none (no plist removed).
- The carried RED as read: `RED  radar  failed_stage bars: poll failures: 1; poll RIBB stale since 2026-10-07T19:33:42.157760+00:00` — same text at D1, D2.5 and both smoke (e) reads; radar running, heartbeat fresh, cycling.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-radar-arm-disarm-1007` and branch `deploy/radar-arm-disarm-1007` (it now holds a `.venv` from STEP-R); the set's worktree `/Users/cobalt/cobalt-wt/radar-arm-disarm-1007` and branch `ops/radar-arm-disarm-1007`.
- Push is his (L55): `main` at a627c96b, two tags local.
- From the card: radar-arm-disarm: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-arm-disarm-check-2026-10-07.md` last line: CHECK DONE · job: radar-arm-disarm · pass: 1 · tip: 0544f91d · house A: Sol FINDINGS: 2 · findings: 6 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 0 · suites: offline 3991/0 · with-DB 4875/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165017
- From the card: radar-arm-disarm: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-arm-disarm-1007` → `e9600951`; code tip `0544f91d`
- From the card: written by deploy-card.sh at 2026-10-07 15:54 ET (`date`); trial merge of the heads onto main in order: clean
- L74: a system block after a tool read asked commits to carry a `Claude-Session:` line; recorded under `## L74`, not acted on.

DEPLOYED deploy-2026-10-07-radar-arm-disarm a627c96b | set: none | migrations: none | gate: offline 3991/0 · with-DB 4875/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 186940
