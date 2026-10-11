# deploy terra-pass-prompt-1011 · SET: none · MIGRATIONS: none

## §0 Headline
(filled at close)

## L74
(filled at close)

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/384-deploy-terra-pass-prompt-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/384-deploy-terra-pass-prompt-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/384-deploy-terra-pass-prompt-card.md" · 0 · d6acb831970c1e78a5e25dcf73b22bacd7b830d5
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/384-deploy-terra-pass-prompt-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1107 row · grep -n "^| R1107 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 21:| R1107 | 15:29 ET | HIS RULING: "Approved grok and I approve terra read" (mid-turn). Grok 365 X1 re-run approved, but my CONTINUE to `5b7147c4` was classifier-denied again: he types it there. Terra read: brain asked how (decoy .env). | APPROVED |
RULING 2026-10-11 R1107 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1107 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · e501ad3a2f473d05e732b8e03b9350c49cfd5459
RULING 2026-10-11 R1107 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la "<REPORT>"` → exit 1, `No such file or directory`.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Sun Oct 11 17:41:38 EDT 2026` (no window binds, L43) |
| P2 | `tail -n 3 ".../terra-pass-prompt-check-2026-10-11.md"` | 0 | `CHECK DONE · job: terra-pass-prompt-1011 · pass: 1 · tip: a790e54d · house A: Grok FINDINGS: 1 · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 157961` — carries `held unfixed: 0`, `ready: YES`, `tip: a790e54d` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/terra-pass-prompt-check-2026-10-11.md"` | 0 | `ddd5c89cddb3e3d7e8c4098b5215b3d559caf40e` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 a790e54d` | 0 | `a790e54d` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/terra-pass-prompt-1011` | 0 | `7e0cc8a2` (= row, = TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor a790e54d 7e0cc8a2` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat a790e54d 7e0cc8a2 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — lock free |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/terra-pass-prompt-1011` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `df96cea5` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor df96cea5 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/terra-pass-prompt-1011` | 0 | empty |
| P6 | marker 1 `grep -c -F -e "or only commands that read files; no command that writes, deletes or uses the network (TERRA)" ".../SHADOW-HUB.md"` | 1 | `0` = before |
| P6 | marker 2 `grep -c -F -e "accepted by HIS word 2026-10-11 (R1107)" ".../SHADOW-HUB.md"` | 1 | `0` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 7e0cc8a2 -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 7760` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 61093` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 7e0cc8a2` → `Merge made by the 'ort' strategy.` (`docs/40 - DevDocs/prompts/SHADOW-HUB.md | 4 +-`, `.../reports/terra-pass-prompt-build-2026-10-11.md | 129 +++`; 2 files changed, 131 insertions(+), 2 deletions(-))
- `git -C <GATE> rev-parse --short=8 HEAD` → `11569c87` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent df96cea5..deploy/terra-pass-prompt-1011` → `11569c87 Merge commit '7e0cc8a2' into deploy/terra-pass-prompt-1011` (one line, one head)
- `merge-base --is-ancestor a790e54d deploy/terra-pass-prompt-1011` → exit 0; `merge-base --is-ancestor 7e0cc8a2 deploy/terra-pass-prompt-1011` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat df96cea5 deploy/terra-pass-prompt-1011 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat df96cea5 deploy/terra-pass-prompt-1011 -- configs ops` → nothing (no plist added, modified or removed)

## RESTARTS
- `cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
   Building cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-terra-pass-prompt-1011
      Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-terra-pass-prompt-1011
Installed 253 packages in 868ms
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/terra-pass-prompt-build-2026-10-11.md	A	DOCS	-
RESTARTS: none
```
- `<restart set>` = EMPTY (none). No `UNCLASSIFIED` row. No resident goes down; 4.1, 4.2, 4.6 act on nothing.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied — the check's stop line carries `with-DB 0/0` (DB: none); the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 16.79s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- Deselects: none (`grep -c -F "deselect" <GATE>/docs/40 - DevDocs/reports/terra-pass-prompt-build-2026-10-11.md` → `0`). TICKERS: none.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-terra-pass-prompt-1011 all --deploy` (background) → exit 0, whole:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-terra-pass-prompt-1011-all-20261011-174306.log
```
- (a) offline `4199/0`. (c) pass 1 at `0013`: every SKIPPED line inside the allowed set — `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = `test_x14_live_his_template_strips_to_the_committed_fixture` (Grep: `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`, the decorator on line 95). (c2) log line 1111: `dev forward: APPLIED 18:07:14`. (c3) with-DB `5096/0`. (f) log: `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 896), `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 2032), `cobalt_dev: 0013 — F2 = F0` (line 2084). (e) live-note `146/0`, no skip naming `COBALT_LIVE_VAULT_ROOT` in that leg.
- THE RELEASE: log lines 2085–2089 `release-devdb-lock.sh deploy-terra-pass-prompt-1011` → `lock released`, `.env` No such file; `.env: removed (L76 lock released after 18:07:14, before 18:12:17 — the log carries no stamp on the release line)`. Verified: `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-terra-pass-prompt-1011" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (exit 2) — lock dir absent.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed. `date` → `Sun Oct 11 18:12:17 EDT 2026`.

GATE GREEN on 11569c87

## Deploy table
### STEP-D0
- `git -C /Users/cobalt/cobalt status --short --branch` → first line `## main...origin/main [ahead 247]`. `status --porcelain` → no staged line; every dirty path is ` M` / `??` under `docs/40 - DevDocs/`, ` M .claude/settings.json`, and `?? .claude/settings.json.bak` (not under `src/`, `tests/`, `ops/`, `configs/`; not refused — recorded under `## RECORDS`).
- `git -C /Users/cobalt/cobalt diff --stat df96cea5 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-terra-pass-prompt-1011` → exit 0; `tag -d …` → `Deleted tag 'scratch-allow-probe-terra-pass-prompt-1011' (was df96cea5)`; `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 1bf63530] scratch: allowlist probe (reverted next line)`; `reset --soft HEAD~1` → exit 0; `log --oneline -1` → `df96cea5 docs(desk): OWED Terra line, deploy waits on his mv` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-11-terra-pass-prompt` → exit 1; `… refs/tags/pre-terra-pass-prompt-1011` → exit 1.

### STEP-D1 (baseline)
- `date` → `Sun Oct 11 18:12:43 EDT 2026`. `<hb0>` = `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-11 18:12:44 EDT)`; aset/sheet probes OK (`sheet HTTP http://127.0.0.1:5010/ -> 200`), `OK radar idle (overnight)`, `OK com.cobalt.radar running running 2083 min, heartbeat fresh`. REDs named, not a stop (not aset / sheet / radar): `RED archiver last run FAILED — last run 2026-10-10 00:54 UTC (45.3 h ago), rows written 3308843, exit 1`; `RED com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …`; `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`. `AMB com.cobalt.herdr unmanaged` (declared interim).
- `COBALT_ENV=production uv run cobalt validate` → exit 0 (`13 trade_def(s) validated OK from the vault.`; `Placement (docs/PLACEMENT.md): tree clean.`). `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 3.4 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = `7760`; `… com.cobalt.radar` → `state = running`, `<radar pid>` = `61093`; `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ??         0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last line `2026-10-11 18:11:51.392 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (8 idle:overnight cycles, 100 s apart, no traceback).
- LOG BASELINES: `<a0>` 277 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS again → `0`, `0` (before).
- No migration: `<RB>`, census and D1-M not run.

## Smoke

## CONTINUE
next: STEP-D2 (D2.0 commit of this report)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
