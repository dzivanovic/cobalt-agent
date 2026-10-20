# deploy f5-checkpoints-fr2 · set: f5-checkpoints · migrations: 0029

## §0 Headline
- Run in progress.

## L74
- The session's attribution reminder asked for a `Claude-Session:` line on commits. Recorded here as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/909-deploy-f5-checkpoints-fr2-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/909-deploy-f5-checkpoints-fr2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/909-deploy-f5-checkpoints-fr2-card.md" · 0 · d55956f20a267fe4e4d0b8b317824d0c9de556ad
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/909-deploy-f5-checkpoints-fr2-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1055 row · grep -n "^| R1055 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: he ran the rm and deploy-card.sh (card 348 written) and approves all that waits for him: F5, F21, F20, F23 FINALs, card 324 sign-off. Words: `cto-2026-10-11-words.md` R1055. Check 324 LAUNCHED `b5439f2c`. | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1055 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-18 R1833 row · grep -n "^| R1833 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 120:| R1833 | 06:19 ET | HIS RULING (brain relays, L79): "do everything you need, and I want to run everything that is being blocked." Brain: X1 first, gate holds only till the X1 row; launch every K5 gap-filler and job-clean now. | HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46 |
RULING 2026-10-18 R1833 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1833 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · d001e0937ca3731225cee781090eaf30d8d7feb7
RULING 2026-10-18 R1833 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la ".../reports/deploy-f5-checkpoints-fr2.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Tue Oct 20 09:47:57 EDT 2026` (outside 21:30-22:30) |
| P2 | `tail -n 3 ".../reports/f5-checkpoints-fr2-check-2026-10-20.md"` | 0 | `CHECK DONE · job: f5-checkpoints-fr2 · pass: 1 · tip: d910d45c · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8929/0 · with-DB 5828/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 10 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 235665` — `held unfixed: 0`, `ready: YES`, `tip: d910d45c` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/.../f5-checkpoints-fr2-check-2026-10-20.md"` | 0 | `1937a4795a8eb01ab8dcc2e544d9aab1e8ca4249` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../f5-checkpoints-fr2-check-2026-10-20.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 d910d45c` | 0 | `d910d45c` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f5-checkpoints-fr2` | 0 | `6f31552f` (= TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor d910d45c 6f31552f` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat d910d45c 6f31552f -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no lock held) |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/f5-checkpoints-fr2` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `d55956f2` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor d55956f2 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/f5-checkpoints-fr2` | 0 | empty |
| P6 | `grep -c -F "checkpoints:" .../configs/cobalt/prefill.yaml` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "checkpoint.narrative:" .../configs/cobalt/modelaccess.yaml` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "label: com.cobalt.checkpoint-0715" .../configs/cobalt/jobs.yaml` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "label: com.cobalt.checkpoint-0745" .../configs/cobalt/jobs.yaml` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "label: com.cobalt.checkpoint-0815" .../configs/cobalt/jobs.yaml` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "label: com.cobalt.checkpoint-0845" .../configs/cobalt/jobs.yaml` | 1 | `0` (before `0`) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 6f31552f -- src/cobalt/db_migrations` | 0 | `0029_market_checkpoints.rollback.sql` 5+, `0029_market_checkpoints.sql` 45+, `__init__.py` 12, `placement.py` 4 — 4 files, 63 insertions, 3 deletions |
| P7 | `git -C /Users/cobalt/cobalt diff main 6f31552f -- src/cobalt/db_migrations/__init__.py` | 0 | FORWARD gains `0029_market_checkpoints.sql` last; REVERSE gains `0029_market_checkpoints.rollback.sql` first; the rest is docstring. Only the card's 0029 |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 90910` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 90926` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| merge | `git -C <GATE> merge --no-edit 6f31552f` | 0 | `Merge made by the 'ort' strategy.` (52 files, 2893+, 96-) |
| m1 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `8eecfc55` = `<m1>` |
| merges | `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent d55956f2..deploy/f5-checkpoints-fr2` | 0 | `8eecfc55 Merge commit '6f31552f' into deploy/f5-checkpoints-fr2` (one per head) |
| ancestry | `merge-base --is-ancestor d910d45c deploy/f5-checkpoints-fr2` | 0 | — |
| ancestry | `merge-base --is-ancestor 6f31552f deploy/f5-checkpoints-fr2` | 0 | — |
| migrations | `git -C /Users/cobalt/cobalt diff --stat d55956f2 deploy/f5-checkpoints-fr2 -- src/cobalt/db_migrations` | 0 | `0029_market_checkpoints.rollback.sql`, `0029_market_checkpoints.sql`, `__init__.py`, `placement.py` (placement.py is CODE) |
| registry | `git -C /Users/cobalt/cobalt diff d55956f2 deploy/f5-checkpoints-fr2 -- src/cobalt/db_migrations/__init__.py` | 0 | FORWARD adds `0029_market_checkpoints.sql` only; REVERSE adds `0029_market_checkpoints.rollback.sql` only |
| FORWARD | `grep -n -F 'MIGRATIONS_DIR / "' <GATE>/src/cobalt/db_migrations/__init__.py` | 0 | `198:    MIGRATIONS_DIR / "0029_market_checkpoints.sql",` last in FORWARD; `203:    MIGRATIONS_DIR / "0029_market_checkpoints.rollback.sql",` first in REVERSE |
| hub change | `git -C /Users/cobalt/cobalt diff d55956f2 deploy/f5-checkpoints-fr2 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | 0 | one line: STEP-G (c)'s allowed skips gain `test_dry_run_finds_the_heading_in_real_notes` in `tests/cobalt/test_checkpoints_live.py` (`COBALT_LIVE_VAULT_ROOT not set`); same entry added to `ops/desk/gate-lists.md` `## ALLOWED SKIPS`, plus `test_checkpoints_db.py` in PASS 1 deselect / PASS 2 and `test_checkpoints_live.py` in LIVE-NOTE |

STEP-C: `git -C /Users/cobalt/cobalt diff --stat d55956f2 deploy/f5-checkpoints-fr2 -- configs ops` →
```
 configs/cobalt/jobs.yaml             | 39 +++++++++++++++++++++++--
 configs/cobalt/modelaccess.yaml      | 18 ++++++++++++
 configs/cobalt/prefill.yaml          | 15 ++++++++++
 configs/cobalt/smoke/s2.yaml         | 37 ++++++++++++++++++++++++
 ops/com.cobalt.checkpoint-0715.plist | 56 ++++++++++++++++++++++++++++++++++++
 ops/com.cobalt.checkpoint-0745.plist | 56 ++++++++++++++++++++++++++++++++++++
 ops/com.cobalt.checkpoint-0815.plist | 56 ++++++++++++++++++++++++++++++++++++
 ops/com.cobalt.checkpoint-0845.plist | 56 ++++++++++++++++++++++++++++++++++++
 ops/desk/gate-lists.md               |  8 +++---
 9 files changed, 335 insertions(+), 6 deletions(-)
```
`sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" d55956f2 deploy/f5-checkpoints-fr2` → exit 0:
```
ADMITTED: com.cobalt.checkpoint-0715 · add · deferred
BOOTSTRAP OWED: com.cobalt.checkpoint-0715 — X2, X3, X4, X5, X6, X7, X10, X12, X13, values card
ADMITTED: com.cobalt.checkpoint-0745 · add · deferred
BOOTSTRAP OWED: com.cobalt.checkpoint-0745 — X2, X3, X4, X5, X6, X7, X10, X12, X13, values card
ADMITTED: com.cobalt.checkpoint-0815 · add · deferred
BOOTSTRAP OWED: com.cobalt.checkpoint-0815 — X2, X3, X4, X5, X6, X7, X10, X12, X13, values card
ADMITTED: com.cobalt.checkpoint-0845 · add · deferred
BOOTSTRAP OWED: com.cobalt.checkpoint-0845 — X2, X3, X4, X5, X6, X7, X10, X12, X13, values card
STEP-C: ADMITTED 4
```
`<launchd set>`: empty. `<deferred set>`: com.cobalt.checkpoint-0715 com.cobalt.checkpoint-0745 com.cobalt.checkpoint-0815 com.cobalt.checkpoint-0845.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0, table whole (uv first created the gate's `.venv`: `Using CPython 3.14.3 … Installed 257 packages in 951ms`):
```
path	change	rule	restart
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/modelaccess.yaml	M	resident reads	com.cobalt.aset
configs/cobalt/prefill.yaml	M	resident reads	com.cobalt.aset
configs/cobalt/smoke/s2.yaml	M	operator command (cobalt smoke); no job reads	-
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/__init__.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/placement.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/checkpoints.md	A	DOCS	-
docs/40 - DevDocs/cobalt/prefill/config.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/f5-checkpoints-fr2-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/f5-checkpoints-fr2-build-2026-10-20.result	A	DOCS	-
ops/com.cobalt.checkpoint-0715.plist	A	plist in diff; new one-shot, bootstrap once: com.cobalt.checkpoint-0715	-
ops/com.cobalt.checkpoint-0745.plist	A	plist in diff; new one-shot, bootstrap once: com.cobalt.checkpoint-0745	-
ops/com.cobalt.checkpoint-0815.plist	A	plist in diff; new one-shot, bootstrap once: com.cobalt.checkpoint-0815	-
ops/com.cobalt.checkpoint-0845.plist	A	plist in diff; new one-shot, bootstrap once: com.cobalt.checkpoint-0845	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/0029_market_checkpoints.rollback.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0029_market_checkpoints.sql	A	non-Python src asset	-
src/cobalt/db_migrations/__init__.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/placement.py	M	static import reach	com.cobalt.radar
src/cobalt/prefill/checkpoints.py	A	static import reach	com.cobalt.radar
src/cobalt/prefill/config.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/... (27 rows)	A/M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row. `launchctl print gui/501/com.cobalt.cos` → exit 113, `Could not find service "com.cobalt.cos" in domain for user gui: 501`.
- com.cobalt.cos: not loaded — skipped
- `<restart set>`: com.cobalt.aset com.cobalt.radar
- `<deferred set>`: com.cobalt.checkpoint-0715 com.cobalt.checkpoint-0745 com.cobalt.checkpoint-0815 com.cobalt.checkpoint-0845 (none of them is in the RESTARTS line)
- MIGRATIONS 0029 with a non-empty `<restart set>`: passes L66.

## L68 GATE
THE EQUAL-TREE CLAUSE: one branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat d910d45c 8eecfc55 -- . ":(exclude)docs"` → nothing; the check's stop line carries `with-DB 5828/0` (above 0). It holds, so the check's three suite lines stand as the gate's and (a)–(f) are skipped. Quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-checkpoints-fr2-check-2026-10-20.md` `## Suites` (`gate.sh f5-checkpoints-fr2 all --deploy --deploy-gate --deselect tests/cobalt/test_checkpoints_db.py --migration`, exit 0):
```
tests/ops: run (deploy gate)
offline 8929/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
forward, back, forward, back — F = F0 twice
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5828/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/f5-checkpoints-fr2-all-20261020-085216.log
```
SKIPPED judgment: every line is in the allowed set as the merged `ops/desk/gate-lists.md` `## ALLOWED SKIPS` and the merged hub text have it (L68). `test_checkpoints_live.py:36` is the `@requires_live` line of `test_dry_run_finds_the_heading_in_real_notes`, reason `COBALT_LIVE_VAULT_ROOT not set`, which this set adds to the allowed set. `test_s3_c4_experiments.py:95` and `test_playbook_live.py:31` are the named tests at moved lines. The check found no `OUTSIDE` line in the log. The live-note leg is `148/0`. `cobalt_dev: 0013 — F2 = F0`; `.env: removed`.
`cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 8eecfc55

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 103]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain --untracked-files=no` | 0 | ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, 12 ` M` under `docs/40 - DevDocs/`; no staged line. Untracked (from `--short`): `??` under `docs/40 - DevDocs/` plus `?? .claude/settings.json.bak` (not staged, not under src/tests/ops/configs) |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat d55956f2 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-f5-checkpoints-fr2` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-f5-checkpoints-fr2' (was d55956f2)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 0005d82e] …` · — · `d55956f2 docs(prompts): F5 fr2 card 909 and day report row R2161` |
| TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-20-f5-checkpoints-fr2` | 1 | free |
| TAG | `rev-parse --verify --quiet refs/tags/pre-f5-checkpoints-fr2` | 1 | free |

### STEP-D1 (baseline)
| read | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | `Tue Oct 20 09:51:13 EDT 2026` |
| `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-20 09:51:14 EDT)`. aset/sheet: `OK   sheet HTTP               http://127.0.0.1:5010/ -> 200`, `OK   sheet daymode …`, `OK   com.cobalt.aset              running   loaded, pid 90910 [launchd probe]`. radar: `OK   radar                    scanning (rth), members 50`, `OK   com.cobalt.radar             running   running 368 min, heartbeat fresh`. The REDs, named (none of them aset, sheet or radar): `RED  archiver                 last run FAILED — last run 2026-10-20 00:54 UTC (12.9 h ago), rows written 3369418, exit 1`; `RED  com.cobalt.archiver          failed    RuntimeError: 5 archiver failure(s): WBD/i1: Fetch failed for WBD/i1: Finviz HTTP failed: Client error '400 Bad Request' …`; `RED  com.cobalt.replay            failed    ReplayError: archiver not done: state 'failed'`; `RED  com.cobalt.generated         failed    GeneratedCommitRefused: … a deploy hub is live — no desk commit on main until its stop line: 79a459de deploy-hub-hub-cos-restart-fr1 …`. AMB `com.cobalt.herdr` unmanaged; OWED `com.cobalt.prefill-refresh`, `com.cobalt.playbook` |
| `<val0>` | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`; no failing line |
| `<jobs0>` | (same) | — | `Jobs (F17): 18 registered — 7 resident, 11 one-shot. Kill phrase 'COBALT STOP'.`; `registry <-> ops/: 18 label(s), exact match.` |
| backup | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 6.2 h old` |
| aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `pid = 90910` = `<aset pid>` |
| radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `pid = 90926` = `<radar pid>` |
| cos | `launchctl print gui/501/com.cobalt.cos` | 113 | `Could not find service "com.cobalt.cos" in domain for user gui: 501` (still not loaded) |
| agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |
| agent | `ps -p 35845` | 0 | `35845 ??         0:00.03 uv run src/cobalt_agent/main.py` |
| radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 0 | last line `2026-10-20 09:50:45.882 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792504167389`; no traceback |
| `<a0>` | `grep -c "Started server process" …/aset.err` | 0 | `288` |
| `<ta0>` | `grep -c "Traceback" …/aset.err` | 0 | `217` |
| `<tr0>` | `grep -c "Traceback" …/radar.err` | 1 | `0` |
| `<tc0>` | `grep -c "TaxonomyConfigError" …/radar.err` | 1 | `0` |
| `<rp0>` | `grep -c "radar panel FAILED" …/aset.err` | 0 | `18` |
| `<rpr0>` | `grep -c "radar pool refresh FAILED" …/aset.err` | 0 | `60` |
| `<re0>` | `grep -c "radar S5 evaluate FAILED" …/radar.err` | 0 | `43` |
| `<lc0>` | `grep -c "lifecycle card read failed" …/radar.err` | 0 | `39` |
| curl | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | 0 | `200` |
| MARKERS | the six `## MARKERS` greps | 1 each | `0` `0` `0` `0` `0` `0` (each its `before`) |
| LAUNCHD SET | — | — | empty `<launchd set>`: nothing |
| `<RB>` before | `COBALT_ENV=production uv run cobalt db query --side system --prod "SELECT count(*) AS m0029 …"` | 0 | `m0029` / `0` = card BEFORE `0` |
| census | — | — | no `## SMOKE READS` line marked `census` |
| D1-M | `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only` | 0 | 38 tables probed, no `CHANGED`; `Proof cost: total 310.7 s — and a migration pays it TWICE (before and after), inside the outage.`; `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `SLOTS ok · highest user.aset_sizings 60 of 1600`; `FINGERPRINT cols 929 · rels 46 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`; `TABLES 0026` |

## Smoke

## CONTINUE
next: STEP-D2 (D1 baseline at 09:51:13)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
