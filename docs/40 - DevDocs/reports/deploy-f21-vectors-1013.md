# deploy f21-vectors-1013 — set: f21-vectors — migrations: 0028

## §0 Headline
- In progress.

## L74
- A system reminder in this session asked for a `Claude-Session:` line on commits. Recorded here as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/892-deploy-f21-vectors-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/892-deploy-f21-vectors-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/892-deploy-f21-vectors-card.md" · 0 · 6d9a497808d20e311ed06d72a3b8847e6d05bfd7
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/892-deploy-f21-vectors-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
AUTHORIZED
```
RULINGS: none.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| FIRST LAUNCH | `ls -la ".../reports/deploy-f21-vectors-1013.md"` | 1 | No such file or directory |
| P1 | `date` | 0 | Tue Oct 20 00:46:53 EDT 2026 (outside 21:30-22:30) |
| P2 | `tail -n 3 ".../f21-vectors-check-r2-2026-10-19.md"` | 0 | `CHECK DONE · job: f21-vectors-1013 · pass: 1 · tip: c56817ec · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8852/0 · with-DB 5751/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 19 · ready: YES · decisions: 5 · for Dejan: 1 · tokens: 207817` — carries `held unfixed: 0`, `ready: YES`, tip c56817ec |
| P2 | `git log -1 --format=%H -- <check>` | 0 | 10fe28b57b6a17d48d828c721d0435d410dbfcae |
| P2 | `git diff --stat -- <check>` | 0 | nothing |
| P3 | `rev-parse --short=8 c56817ec` | 0 | c56817ec |
| P3 | `rev-parse --short=8 ops/f21-vectors-1013` | 0 | c56817ec |
| P3 | `merge-base --is-ancestor c56817ec ops/f21-vectors-1013` | 0 | — |
| P3 | `diff --stat c56817ec ops/f21-vectors-1013 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no holder) |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/f21-vectors-1013` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `6d9a4978` = `<m0>` |
| P5 | `merge-base --is-ancestor 6d9a4978 main` | 0 | — |
| P5 | `log --oneline main..deploy/f21-vectors-1013` | 0 | EMPTY |
| P6 | `grep -c -F "openai_embeddings" .../modelaccess.yaml` | 1 | `0` (before `0`) |
| P6 | `ls /Users/cobalt/cobalt/src/cobalt/genesis/embed.py` | 1 | `No such file or directory` (before) |
| P7 | `diff --stat main c56817ec -- src/cobalt/db_migrations` | 0 | `0028_genesis_vectors.rollback.sql` 11+, `0028_genesis_vectors.sql` 24+, `__init__.py` 14+ — 3 files, 49 insertions |
| P7 | `diff main c56817ec -- .../__init__.py` | 0 | FORWARD adds `0028_genesis_vectors.sql` last; REVERSE adds `0028_genesis_vectors.rollback.sql` first; the rest is docstring — the card's 0028 only |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 3518 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 3536 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
- `git -C <GATE> merge --no-edit c56817ec` → `Merge made by the 'ort' strategy.` (49 files changed, 1370 insertions(+), 118 deletions(-))
- `rev-parse --short=8 HEAD` → `<m1>` = `434ebb42`
- `log --oneline --merges --first-parent 6d9a4978..deploy/f21-vectors-1013` → `434ebb42 Merge commit 'c56817ec' into deploy/f21-vectors-1013`
- `merge-base --is-ancestor c56817ec deploy/f21-vectors-1013` → exit 0
- `diff --stat 6d9a4978 deploy/f21-vectors-1013 -- src/cobalt/db_migrations` → `0028_genesis_vectors.rollback.sql` 11+, `0028_genesis_vectors.sql` 24+, `__init__.py` 14+ (3 files, 49 insertions) — exactly 0028 and its registry
- `__init__.py` diff: FORWARD gains `0028_genesis_vectors.sql` last; REVERSE gains `0028_genesis_vectors.rollback.sql` first
- `grep -n -F 'MIGRATIONS_DIR / "' <GATE>/.../__init__.py` → `193:    MIGRATIONS_DIR / "0028_genesis_vectors.sql",` last of FORWARD; `198:    MIGRATIONS_DIR / "0028_genesis_vectors.rollback.sql",` first of REVERSE
- STEP-C: `git diff --stat 6d9a4978 deploy/f21-vectors-1013 -- configs ops` → `configs/cobalt/modelaccess.yaml | 22 ++++` · `ops/desk/gate-lists.md | 4 ++--` · `2 files changed, 24 insertions(+), 2 deletions(-)`
- STEP-C: `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 6d9a4978 deploy/f21-vectors-1013` → `STEP-C: ADMITTED 0` (exit 0)

## RESTARTS
`COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` (in `<GATE>`, `.env` absent) → exit 0, no UNCLASSIFIED row. Rows outside DOCS/tests, verbatim:
```
configs/cobalt/modelaccess.yaml	M	resident reads	com.cobalt.aset
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
src/cobalt/db_migrations/0028_genesis_vectors.rollback.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0028_genesis_vectors.sql	A	non-Python src asset	-
src/cobalt/db_migrations/__init__.py	M	static import reach	com.cobalt.radar
src/cobalt/genesis/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/genesis/embed.py	A	static import reach	com.cobalt.radar
src/cobalt/genesis/store.py	M	static import reach	com.cobalt.radar
src/cobalt/modelaccess/__init__.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/modelaccess/adapters.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/modelaccess/client.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/modelaccess/config.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/modelaccess/models.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/voice/registry.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
(the 11 docs rows are DOCS `-`; the 24 tests rows are `test/documentation; no resident` `-`.) First run in the fresh gate created `.venv` (`Installed 257 packages in 950ms`).
- `launchctl print gui/501/com.cobalt.cos` → exit 113, `Could not find service "com.cobalt.cos" in domain for user gui: 501`
- com.cobalt.cos: not loaded — skipped
- `<restart set>` = `com.cobalt.aset com.cobalt.radar` · `<deferred set>` = empty · `<launchd set>` = empty
- MIGRATIONS 0028 with a non-empty set: OK (L66).

## L68 GATE
- EQUAL-TREE CLAUSE: `git diff --stat c56817ec 434ebb42 -- . ":(exclude)docs"` → `configs/cobalt/rules.yaml | 2 +-` · `tests/ops/test_hub_cos_restart_1019.py | 93 +++` · `tests/ops/test_hub_deferred_1018.py | 4 +-` (3 files) → not equal; the gate runs whole.
- Deselect named by the build report (`f21-vectors-build-2026-10-13.md:156`, `:220`): `tests/cobalt/test_genesis_vectors_db.py`. `--migration` (card MIGRATIONS 0028). TICKERS none.
- (a0) `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` (`.env` absent) → `264 passed, 163 skipped in 18.90s`; 0 failed (every skip a with-DB skip: `Postgres env settings not available` / `requires_db`).
- THE GATE: `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-f21-vectors-1013 all --deploy --deploy-gate --deselect tests/cobalt/test_genesis_vectors_db.py --migration` → exit 0. Verdict lines, whole:
```
tests/ops: run (deploy gate)
offline 8856/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
forward, back, forward, back — F = F0 twice
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5751/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-f21-vectors-1013-all-20261020-004848.log
```
- (a) offline 8856/0; W line `tests/ops: run (deploy gate)`.
- (c) every SKIPPED line inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`; `test_playbook_live.py:31` = the decorator of `32:def test_live_vault_renders_six_decks`, reason `COBALT_LIVE_VAULT_ROOT not set`; `test_s3_c4_experiments.py:95` = decorator of `96:def test_x14_live_his_template_strips_to_the_committed_fixture`; `test_replay_line.py:266` reason names `COBALT_TEST_LIVE_DRC`.
- (c2) `dev forward: APPLIED 01:30:36` (log `:1265`); no CHANGED (log `:1093`, and `content UNCHANGED on every table` at `:1337`, `:2290`, `:2424`, `:2488`).
- (c3) with-DB 5751/0.
- (f) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:1040`) = `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:2300`) → `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: `.env: removed`; log `:2502` `lock released`; `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-f21-vectors-1013" .../.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) live-note 147/0; log tail `147 passed, 1 skipped, 15 warnings in 26.05s` (the one skip names `COBALT_TEST_LIVE_DRC`, inside the set).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 434ebb42

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `status --short --branch` | 0 | first line `## main...origin/main [ahead 45]` |
| MAIN | `status --porcelain` | 0 | ` M .claude/settings.json`; ` M` / `??` under `docs/40 - DevDocs/` only; plus `?? .claude/settings.json.bak` (untracked, outside src/tests/ops/configs — not a refused line; recorded); no staged line |
| MAIN | `diff --stat 6d9a4978 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-f21-vectors-1013` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-f21-vectors-1013' (was 6d9a4978)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main c2c59e18] …` → `6d9a4978 docs(prompts): 892 read-back for 0028` |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-20-f21-vectors-1013` · `…/pre-f21-vectors-1013` | 1 · 1 | free |

### STEP-D1 (01:36:53 EDT)
- `<hb0>` `heartbeat show` (01:36:54): `HEARTBEAT RED — 3 job(s) and 1 probe(s)`. aset / sheet / radar probes OK: `OK   sheet HTTP http://127.0.0.1:5010/ -> 200`, `OK   radar idle (overnight)`, `OK   com.cobalt.aset running loaded, pid 3518`, `OK   com.cobalt.radar running running 56 min, heartbeat fresh`, `OK   com.cobalt.agent running pid 35845 alive`. REDs named, not a stop: `RED  archiver last run FAILED — last run 2026-10-20 00:54 UTC (4.7 h ago), rows written 3369418, exit 1` · `RED  com.cobalt.archiver failed RuntimeError: 5 archiver failure(s): WBD/i1: Fetch failed … Finviz HTTP failed: Client error '400 Bad Request' …` · `RED  com.cobalt.replay failed ReplayError: archiver not done: state 'failed'` · `RED  com.cobalt.generated failed GeneratedCommitRefused: … pre-commit: a deploy hub is live — no desk commit on main until its stop line: 79a459de deploy-hub-hub-cos-restart-fr1 …`. OWED (deferred bootstrap): `com.cobalt.prefill-refresh`, `com.cobalt.playbook`.
- `<val0>` `validate` → exit 0; ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` `Jobs (F17): 18 registered — 7 resident, 11 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 1.0 h old` (ssd ARMED).
- aset `state = running`, pid 3518; radar `state = running`, pid 3536; `launchctl print gui/501/com.cobalt.cos` → exit 113 `Could not find service` (still not loaded); `cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).`; `ps -p 35845` → `35845 ?? 0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, last `2026-10-20 01:35:57.972`.
- baselines: `<a0>` 286 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS: `openai_embeddings` → `0`; `embed.py` → `No such file or directory`.
- `<launchd set>` empty: nothing.
- `<RB>` → `m0028` / `0` = BEFORE `0`. No `census` smoke read on the card.
- D1-M `db migrate --allow-prod --proof-only` → exit 0; 38 tables probed, no CHANGED; `Proof cost: total 302.8 s — and a migration pays it TWICE (before and after), inside the outage.`; `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `SLOTS ok · highest user.aset_sizings 60 of 1600`; `FINGERPRINT cols 926 · rels 46 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`; `TABLES 0026`.

## Smoke

## CONTINUE
next: STEP-D2 (D0, D1 done; gate green at 01:36:28)

## DECISIONS

## RECORDS
- f21-vectors-1013: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f21-vectors-check-r2-2026-10-19.md` last line: CHECK DONE · job: f21-vectors-1013 · pass: 1 · tip: c56817ec · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8852/0 · with-DB 5751/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 19 · ready: YES · decisions: 5 · for Dejan: 1 · tokens: 207817
- f21-vectors-1013: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f21-vectors-1013` → `c56817ec`; code tip `c56817ec`
- written by deploy-card.sh at 2026-10-20 00:45 ET (`date`); trial merge of the heads onto main in order: clean

(run in progress — next step under ## CONTINUE)
