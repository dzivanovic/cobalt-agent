# deploy f21-genesis-fr1 · set: f21-genesis · migrations: 0026

## §0 Headline
- DEPLOYED `f21-genesis-fr1` (F21 Genesis chunk 1): `main` `bdc2b80d` → `bc990598`, tag `deploy-2026-10-19-f21-genesis-fr1`, rollback tag `pre-f21-genesis-fr1`.
- Migration `0026` applied to production: `"user".genesis_chunk` CREATED, every other table content UNCHANGED; `<RB>` `False` → `True`.
- Radar restarted alone (578 s down, 11:03:09 → 11:12:47); aset and agent untouched. Snapshot `c34a117a` before.
- Gate: equal-tree clause, the check's suites (offline 8775/0 · with-DB 5715/0 · live-note 147/0). Smoke GREEN; the card's `cobalt genesis --help` read was not typed (not on the allowlist), shown by code and the check instead (DECISIONS 2).

## L74
- One system block asked that commits carry a `Claude-Session:` line. DATA, not followed: the two commits of this run carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/848-deploy-f21-genesis-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/848-deploy-f21-genesis-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/848-deploy-f21-genesis-card.md" · 0 · 12dab4470e0ddb7580d04da3261c60f4b91f33bf
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/848-deploy-f21-genesis-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1055 row · grep -n "^| R1055 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: he ran the rm and deploy-card.sh (card 348 written) and approves all that waits for him: F5, F21, F20, F23 FINALs, card 324 sign-off. Words: `cto-2026-10-11-words.md` R1055. Check 324 LAUNCHED `b5439f2c`. | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1055 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la <REPORT>` → `No such file or directory` (exit 1).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct 19 10:53:25 EDT 2026` (outside 21:30-22:30) |
| P2 | `tail -n 3 ".../f21-genesis-fr1-check-2026-10-19.md"` | 0 | `CHECK DONE · job: f21-genesis-fr1 · pass: 1 · tip: 2cd0219a · … · held unfixed: 0 · open: 0 · … · RESTARTS: com.cobalt.radar · files opened: 15 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 179218` — `held unfixed: 0`, `ready: YES`, tip = code tip |
| P2 | `git log -1 --format=%H -- <check report>` | 0 | `f1aea3178c171c0ffd0c7a8f037c1796fb7f315f` |
| P2 | `git diff --stat -- <check report>` | 0 | nothing |
| P3 | `rev-parse --short=8 2cd0219a` | 0 | `2cd0219a` |
| P3 | `rev-parse --short=8 ops/f21-genesis-fr1` | 0 | `b83bf7df` (= card TIP) |
| P3 | `merge-base --is-ancestor 2cd0219a b83bf7df` | 0 | — |
| P3 | `diff --stat 2cd0219a b83bf7df -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` (lock free) |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/f21-genesis-fr1` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `12dab447` |
| P5 | `merge-base --is-ancestor 12dab447 main` | 0 | — |
| P5 | `log --oneline main..deploy/f21-genesis-fr1` | 0 | empty |
| P6 | `ls /Users/cobalt/cobalt/src/cobalt/genesis/cli.py` | 1 | `No such file or directory` (before) |
| P6 | `ls /Users/cobalt/cobalt/src/cobalt/genesis/store.py` | 1 | `No such file or directory` (before) |
| P7 | `diff --stat main b83bf7df -- src/cobalt/db_migrations` | 0 | `0026_genesis_chunk.rollback.sql`, `0026_genesis_chunk.sql`, `__init__.py`, `placement.py` |
| P7 | `diff main b83bf7df -- .../__init__.py` | 0 | FORWARD `+ 0026_genesis_chunk.sql` (last); REVERSE `+ 0026_genesis_chunk.rollback.sql` (first); other lines docstring = code. Only the card's 0026 |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 35793 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 35818 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
- `git -C <GATE> merge --no-edit b83bf7df` → `Merge made by the 'ort' strategy.` (44 files, 1457+ / 75-).
- `<m1>` = `d87f9b82`.
- `log --oneline --merges --first-parent 12dab447..deploy/f21-genesis-fr1` → `d87f9b82 Merge commit 'b83bf7df' into deploy/f21-genesis-fr1` (one line, one head).
- `merge-base --is-ancestor 2cd0219a deploy/f21-genesis-fr1` → 0 · `merge-base --is-ancestor b83bf7df deploy/f21-genesis-fr1` → 0.
- `diff --stat 12dab447 deploy/f21-genesis-fr1 -- src/cobalt/db_migrations` → `0026_genesis_chunk.rollback.sql`, `0026_genesis_chunk.sql`, `__init__.py`, `placement.py` (placement.py = CODE). `__init__.py` diff: FORWARD `+ 0026_genesis_chunk.sql`, REVERSE `+ 0026_genesis_chunk.rollback.sql`; the rest docstring.
- `grep -n -F 'MIGRATIONS_DIR / "' <GATE>/src/cobalt/db_migrations/__init__.py` → FORWARD ends `180: 0026_genesis_chunk.sql`; REVERSE begins `185: 0026_genesis_chunk.rollback.sql`. = card's `0026`.
- STEP-C: `diff --stat 12dab447 deploy/f21-genesis-fr1 -- configs ops` → ` ops/desk/gate-lists.md | 4 ++--` (1 file). `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 12dab447 deploy/f21-genesis-fr1` → `STEP-C: ADMITTED 0` (exit 0). `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created `.venv`, 257 packages). Table whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/__init__.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/placement.md	M	DOCS	-
docs/40 - DevDocs/cobalt/genesis/__init__.md	A	DOCS	-
docs/40 - DevDocs/cobalt/genesis/chunk.md	A	DOCS	-
docs/40 - DevDocs/cobalt/genesis/cli.md	A	DOCS	-
docs/40 - DevDocs/cobalt/genesis/search.md	A	DOCS	-
docs/40 - DevDocs/cobalt/genesis/store.md	A	DOCS	-
docs/40 - DevDocs/reports/f21-genesis-fr1-build-2026-10-19.md	A	DOCS	-
docs/40 - DevDocs/reports/f21-genesis-fr1-build-2026-10-19.result	A	DOCS	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/0026_genesis_chunk.rollback.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0026_genesis_chunk.sql	A	non-Python src asset	-
src/cobalt/db_migrations/__init__.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/placement.py	M	static import reach	com.cobalt.radar
src/cobalt/genesis/__init__.py	A	static import reach	com.cobalt.radar
src/cobalt/genesis/chunk.py	A	static import reach	com.cobalt.radar
src/cobalt/genesis/cli.py	A	static import reach	com.cobalt.radar
src/cobalt/genesis/search.py	A	static import reach	com.cobalt.radar
src/cobalt/genesis/store.py	A	static import reach	com.cobalt.radar
tests/cobalt/fixtures/genesis/ledger-200.md	A	test/documentation; no resident	-
tests/cobalt/fixtures/genesis/structure.md	A	test/documentation; no resident	-
tests/cobalt/test_archiver_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_assumed_store.py	M	test/documentation; no resident	-
tests/cobalt/test_dml_roles_offline.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_d2_fix_r1_db.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_d3_experiments.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_k1_store.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_store.py	M	test/documentation; no resident	-
tests/cobalt/test_f15_p1_records_offline.py	M	test/documentation; no resident	-
tests/cobalt/test_genesis_db.py	A	test/documentation; no resident	-
tests/cobalt/test_genesis_experiments_db.py	A	test/documentation; no resident	-
tests/cobalt/test_genesis_offline.py	A	test/documentation; no resident	-
tests/cobalt/test_legs_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_p4_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_store.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_price_floor_db.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_score_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_seam_drc_s3_registry.py	M	test/documentation; no resident	-
tests/cobalt/test_stale_score_db.py	M	test/documentation; no resident	-
tests/cobalt/test_tenancy.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_store.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED`. `<restart set>` = `com.cobalt.radar` · `<deferred set>` = empty · `<launchd set>` = empty. Migration with a non-empty set (L66 holds).

## L68 GATE
THE EQUAL-TREE CLAUSE holds: one branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat 2cd0219a d87f9b82 -- . ":(exclude)docs"` → nothing; the check's stop line carries `with-DB 5715/0` (> 0). The check's suite lines are the gate's, quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f21-genesis-fr1-check-2026-10-19.md:161-188` (`gate.sh f21-genesis-fr1 all --deploy --deploy-gate --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py --migration` → exit 0):
```
tests/ops: run (deploy gate)
offline 8775/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
forward, back, forward, back — F = F0 twice
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5715/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f21-genesis-fr1-all-20261019-095934.log
```
- (c) judgment kept: the eight SKIPPED lines are each inside the allowed set (cards_picks :388 / :401, playbook_live `COBALT_LIVE_VAULT_ROOT not set`, radar_evaluate :695, replay_line `COBALT_TEST_LIVE_DRC`, s3_c4_experiments, catalyst :365, predicate :262). None outside.
- The check records `dev forward: APPLIED 10:42:40` (log :1261) and `cobalt_dev: 0013 — F2 = F0`, `.env: removed`.
- (a0) run here anyway (offline, `.env` absent): `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `264 passed, 163 skipped in 19.68s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db`).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on d87f9b82 — offline 8775/0 · with-DB 5715/0 · live-note 147/0 (equal-tree, from the check) · 10:55 EDT

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `status --short --branch` | 0 | `## main...origin/main [ahead 136]` |
| MAIN | `status --porcelain` | 0 | ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, `?? .claude/settings.json.bak` (not src/tests/ops/configs); no staged line |
| MAIN | `diff --stat 12dab447 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-f21-genesis-fr1` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-f21-genesis-fr1' (was 12dab447)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` / `reset --soft HEAD~1` / `log --oneline -1` | 0 / 0 / 0 | `[main 85612352] …` → `12dab447 docs(desk): Genesis deploy card READ-BACK` |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-19-f21-genesis-fr1` · `… refs/tags/pre-f21-genesis-fr1` | 1 · 1 | free |

### STEP-D1 (10:55:51 EDT)
- `<hb0>`: `HEARTBEAT GREEN — 18 job(s), 14 probe(s), nothing red  (2026-10-19 10:55:52 EDT)`; `radar scanning (rth), members 50`; `com.cobalt.radar running 272 min, heartbeat fresh`; `com.cobalt.aset running pid 35793`; `com.cobalt.agent running pid 35845`; AMB `com.cobalt.herdr` unmanaged (declared interim); OWED `com.cobalt.prefill-refresh`, `com.cobalt.playbook` (deferred bootstrap). No RED.
- `<val0>`: `validate` exit 0, `Placement (docs/PLACEMENT.md): tree clean.` · `<jobs0>`: `Jobs (F17): 18 registered — 7 resident, 11 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 3.1 h old` (ssd ARMED).
- aset `state = running`, `<aset pid>` 35793 · radar `state = running`, `<radar pid>` 35818 · `Cobalt is ONLINE (PID: 35845).` · `ps -p 35845` → `35845 ?? 0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last `2026-10-19 10:55:35.918 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792421654041`, no traceback.
- Baselines: `<a0>` 284 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS: both `No such file or directory` (before).
- THE LAUNCHD SET: empty, nothing read.
- `<RB>` → `m0026` / `False` (= the card's BEFORE `f`; see DECISIONS 1). No `census` read on the card.
- D1-M `db migrate --allow-prod --proof-only` → exit 0, 37 tables probed, no `CHANGED`, `Proof cost: total 295.1 s — and a migration pays it TWICE (before and after), inside the outage.`, `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`, `FINGERPRINT cols 908 · rels 45 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`, `TABLES 0024`.

### STEP-D2
- D2.0 `deploy-shipped.sh --moved 12dab447 "<card>"` → nothing. Commit `bdc2b80d docs(report): deploy f21-genesis-fr1 — gate green on d87f9b82`; `show --stat HEAD` → that one file (183+). `<pre-merge>` = `bdc2b80d`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `bc990598`; `rev-parse --short=8 bc990598^2` → `bdc2b80d` = `<pre-merge>`; `merge-base --is-ancestor d87f9b82 bc990598` → 0.
- D2.3 `diff --stat d87f9b82 bc990598 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 3.2 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 9103.5 MB` · `ssd: snapshot c34a117a — 12 new / 3 changed, 175.8 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `Mon Oct 19 11:02:54 EDT 2026` · `HEARTBEAT GREEN — 18 job(s), 14 probe(s), nothing red  (2026-10-19 11:02:55 EDT)` (423 s after D1's); radar `running 279 min, heartbeat fresh`. No new RED.
- D2.6 `Mon Oct 19 11:02:59 EDT 2026` · `tag pre-f21-genesis-fr1` at `bdc2b80d`.

### STEP-4 (the outage, `<restart set>` = com.cobalt.radar)
| step | command | result |
|---|---|---|
| 4.1 | `date` | `<t down>` = `Mon Oct 19 11:03:09 EDT 2026` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print …` | exit 0 · exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501`. aset and agent not in the set: no orphan-clean, no stop |
| 4.3 | `rev-parse --short=8 HEAD` · `merge --ff-only deploy/f21-genesis-fr1` | `bdc2b80d` = `<pre-merge>` · `Updating bdc2b80d..bc990598` / `Fast-forward` (44 files) |
| 4.4 | `COBALT_ENV=production uv run cobalt db migrate --allow-prod` | `-- applying 0026_genesis_chunk.sql`; table `genesis_chunk user - -> user - -> 0 … CREATED`, every other table `OK`; `38 table(s) proven; … content UNCHANGED on every table.`; `proof cost: BEFORE 280.6 s + AFTER 278.5 s = total 559.1 s`; no `CHANGED`; no uv sync line. `<RB>` → `m0026` / `True` (= AFTER `t`) |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 18 registered — 7 resident, 11 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `launchctl print …` | exit 0 · `state = running`, pid 57565 (≠ 35818) |
| 4.6 | `date` | `<t up>` = `Mon Oct 19 11:12:47 EDT 2026` · downtime 578 s |
| 4.6L | — | `<launchd set>` empty: nothing |

### CLOSE (STEP-7)
- `<pre-merge>` `bdc2b80d` → `<stack-final>` `bc990598` (`rev-parse --short=8 main` → `bc990598`).
- Tags: `pre-f21-genesis-fr1` at `bdc2b80d` · `deploy-2026-10-19-f21-genesis-fr1` at `bc990598` (after the green smoke).
- `<t down>` 11:03:09 · `<t up>` 11:12:47 · 578 s.
- uv sync line: none in the production calls (the gate worktree's `uv` created its own `.venv` at STEP-R).
- Proof cost: D1 `total 295.1 s`; 4.4 `BEFORE 280.6 s + AFTER 278.5 s = total 559.1 s`.
- migrations applied: all (`0026`). `<RB>` before `False` (`f`) / after `True` (`t`).
- Snapshot: `c34a117a` (ssd).
- RESTARTS done: com.cobalt.radar · LAUNCHD done: none · BOOTSTRAP OWED: none from this set.
- THE ROLLBACK STRING:
  1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 bc990598`, com.cobalt.radar booted out first and bootstrapped after; no launchd label.
  2. SCHEMA: only as a separate desk job on HIS word, after the code revert: `COBALT_ENV=production uv run cobalt db migrate --allow-prod --rollback --down-to 0025` (drops `"user".genesis_chunk` and every imported chunk; the old code runs on 0026, per the card's `MIGRATIONS` line).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
FIRST CALLS after `<t up>`: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1).

| row | date | command | result | verdict |
|---|---|---|---|---|
| (a) | 11:12:59 | `launchctl print` aset · radar · `cobalt.sh status` | aset `state = running` pid 35793 (SAME, outside the set) · radar `state = running` pid 57565 (NEW, ≠ 35818) · `Cobalt is ONLINE (PID: 35845).` (single line) | GREEN |
| (b) | 11:13:03 | `grep -c "Started server process" aset.err` · `tail -n 30 aset.err` · Traceback aset / radar · TaxonomyConfigError | `284` = `<a0>` (aset outside the set; tail shows no new start) · `217` = `<ta0>` · `0` = `<tr0>` · `0` = `<tc0>` | GREEN |
| (b) tails | 11:14:17 (`<t up>` + 90 s) | `tail -n 12 radar.err` | `2026-10-19 11:14:07.442 \| INFO \| cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792422765207` (after `<t up>`); no `radar S5 evaluate FAILED` (count 43), no `lifecycle card read failed` (count 39), no traceback (count 0) — settled at the first spaced tail | GREEN |
| (c) | 11:13:09 | `curl … /` · `/radar` · `/radar\?frame=phone` | `200` · `200` · `200` (first attempt each) | GREEN |
| (d) | 11:13:09 | `ls …/genesis/cli.py` · `ls …/genesis/store.py` | `/Users/cobalt/cobalt/src/cobalt/genesis/cli.py` · `/Users/cobalt/cobalt/src/cobalt/genesis/store.py` (after) | GREEN |
| (f) | 11:13:48 | `validate` · `jobs restarts bdc2b80d..bc990598` | exit 0, `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 18 registered — 7 resident, 11 one-shot.` = 4.5 · exit 0, no `UNCLASSIFIED`, `RESTARTS: com.cobalt.radar` = `<restart set>` | GREEN |
| (g) | 11:13:48 | `<RB>` | `m0026` / `True` (= AFTER `t`) | GREEN |
| (e) | 11:13:44 · 11:15:34 (110 s apart) | `heartbeat show` ×2 | 1st `HEARTBEAT GREEN — 18 job(s), 14 probe(s), nothing red  (2026-10-19 11:13:44 EDT)`, radar `running 1 min, heartbeat fresh`. 2nd `HEARTBEAT RED — 1 probe(s)  (2026-10-19 11:15:34 EDT)` with the one RED `RED  radar  failed_stage bars: poll failures: 1` — the CARRIED FAMILY (`failed_stage <stage>: poll failures: <n>`), with `com.cobalt.radar running running 3 min, heartbeat fresh`, a `radar cycle: scanning` line at 11:14:07 (tail 11:15:41, inside 5 min) and radar Traceback count 0. Not new (hub (e)); no other RED; aset / agent same pids | GREEN |
| (h) | 11:15:52 (`<t up>` + 185 s) | the four counts · `/radar` | `18` · `60` · `43` · `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew) · `200`. No `census` read on the card | GREEN |
| (s) genesis tests | — | `uv run pytest -q tests/cobalt/test_genesis_offline.py` | not run in production (hub (s): a test the gate ran is quoted from the gate). Gate = the check's run on the equal tree: offline 8775/0; the check's O9 row: `uv run pytest -q tests/cobalt/test_genesis_offline.py` → `19 passed in 0.42s` | GREEN (quoted from the gate) |
| (s) genesis CLI | — | `uv run cobalt genesis --help` | NOT TYPED: the string is not on this session's allowlist (`uv run cobalt …` without a listed verb; `.claude/settings.json` lists none either), and a refused step command ends the run (L62). Evidence instead: the check's O9 row on the equal tree → `usage: cobalt genesis [-h] {import,search} ...`; the landed `src/cobalt/cli.py:90` `from cobalt.genesis import cli as genesis_cli` and `:557` `genesis_cli.add_parser(sub)`; `src/cobalt/genesis/cli.py:23` `sub.add_parser("genesis", …)`, `:25` `"import"`, `:28` `"search"`; and production `uv run cobalt validate` (4.5, (f)) imports that `cli.py` and exits 0. See DECISIONS 2 | UNPROVEN in production (L70) |

THE CHAIN: the check committed and clean, `ready: YES`, `held unfixed: 0` (P2) → tips re-read `2cd0219a` / `b83bf7df` (P3) → the merged tree `d87f9b82`, migration paths = `0026` only (T) → `RESTARTS: com.cobalt.radar`, no UNCLASSIFIED (R) → three suites green on the equal tree (G) → `bc990598` = `d87f9b82` + docs (D2.3) → landed by fast-forward (4.3) → markers present (d) → `<RB>` `True` (4.4, g) → radar up on a new pid, aset / agent unchanged (a) → radar cycling (b, e) → the set's reads (s: tests from the gate; CLI by code and check, UNPROVEN in production) → no new failure count (h). The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK (K25): (1) every smoke row above carries its `date` and its output verbatim. (2) `merge-base --is-ancestor 2cd0219a bc990598` → 0; `merge-base --is-ancestor b83bf7df bc990598` → 0. (3) REVERT-READBACK (h): `18` `60` `43` `39` = the post-up counts; every count and sha in this report was read from tool output this run. (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`); `git -C <GATE> status --short --branch` → `## deploy/f21-genesis-fr1` alone; no conflict marker.

## CONTINUE
next: STEP-T
next: STEP-C
next: STEP-R
next: STEP-G
next: STEP-D0 (gate green at 10:55 EDT)
next: STEP-D2
OUTAGE STARTING 11:02:59 EDT — residents of com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
outage ended 11:12:47 EDT (radar up, pid 57565) · smoke GREEN · tagged · next: none (closed)

## DECISIONS
1. ASK DESK: `<RB>` prints the boolean as `False` / `True` (Python rendering) where the card writes `f` / `t`. Safe default taken: read as the same boolean (BEFORE `False` = `f`); at 4.4 / (g) `True` = `t`, anything else stops. Next card: write the READ-BACK answers as the tool prints them. [10:58 EDT]
2. ASK DESK: the card's SMOKE READ `uv run cobalt genesis --help` is not on the deploy line (no `uv run cobalt …` string but the listed verbs) and a refused step command ends the run with a rollback (L62). Safe default taken: not typed; shown by the landed code (`src/cobalt/cli.py:90`, `:557`; `src/cobalt/genesis/cli.py:23-28`), the check's O9 run on the equal tree (`usage: cobalt genesis [-h] {import,search} ...`) and production `validate` exiting 0 on the new tree; recorded UNPROVEN in production (L70), not a red. The desk may run it once by hand; a future card names only listed strings, or the hub's line gains one. [11:13 EDT]

## RECORDS
- Downtime over 300 s: radar 578 s (11:03:09 → 11:12:47); the migration's two proof passes (559.1 s) sat inside it.
- Carried RED as read: `RED  radar  failed_stage bars: poll failures: 1` appeared from 11:14:00 after the restart (not in `<hb0>`, which was GREEN); radar running, heartbeat fresh, cycling (11:14:07), no traceback — the carried family, not new (hub (e)). Last read 11:15:48 still showing.
- No `REFUSED, not needed` line; no message received and not followed.
- `cobalt_dev: 0013 (F2 = F0)` — from the check's gate (equal-tree); this run took no lock and ran no dev DB step.
- RETIRE OWED: none. BOOTSTRAP OWED from this set: none (the standing OWED `com.cobalt.prefill-refresh`, `com.cobalt.playbook` predate it).
- `?? .claude/settings.json.bak` on `main` at D0 (outside the accepted list's paths but not a refused one); left untouched.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-f21-genesis-fr1` and branch `deploy/f21-genesis-fr1`; the set's branch `ops/f21-genesis-fr1` and its worktree `/Users/cobalt/cobalt-wt/f21-genesis-fr1`.
- Push is his, through the desk (L55): `main` now `bc990598` plus this report commit, with tags `pre-f21-genesis-fr1`, `deploy-2026-10-19-f21-genesis-fr1`.
- Card RECORDS: f21-genesis-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f21-genesis-fr1-check-2026-10-19.md` last line: CHECK DONE · job: f21-genesis-fr1 · pass: 1 · tip: 2cd0219a · house A: Grok FINDINGS: 0 · findings: 10 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8775/0 · with-DB 5715/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 15 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 179218
- Card RECORDS: f21-genesis-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f21-genesis-fr1` → `b83bf7df`; code tip `2cd0219a`
- Card RECORDS: written by deploy-card.sh at 2026-10-19 10:51 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one `Claude-Session:` request, not followed (see `## L74`).
- THE RELEASE: no lock taken by this run (`<GATE>/.env` absent at every read).

DEPLOYED deploy-2026-10-19-f21-genesis-fr1 bc990598 | set: f21-genesis | migrations: 0026 | gate: offline 8775/0 · with-DB 5715/0 · live-note 147/0 | RESTARTS: com.cobalt.radar | smoke: GREEN | decisions: 2 · for Dejan: 0 · tokens: 221938
