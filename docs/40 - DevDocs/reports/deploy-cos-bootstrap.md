# deploy cos-bootstrap — SET: cos — MIGRATIONS: none

Card: `docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md` (committed `971dd96f`). Bootstrap-only deploy (DEPLOY-HUB 4.6L-BO): no branch, no worktree, no merge, no outage. Seat: deploy-hub-cos-bootstrap. Started `Wed Oct 21 17:19:59 EDT 2026`.

## §0 Headline
- FAILED at smoke (s). `com.cobalt.cos` bootstrapped at 17:23 ET from `ops/com.cobalt.cos.plist`, then exited 1 at start: `cobalt.db.DbConfigError: Missing Postgres settings for the APP credential: POSTGRES_HOST, COBALT_DB_USER, COBALT_DB_PASSWORD`.
- Cause: `src/cobalt/cos/run.py` never loads the repo `.env`. aset (`src/cobalt/aset/__main__.py:30`) and the CLI (`src/cobalt/cli.py:60`) do. The fix needs a build.
- STEP-5 ran: cos booted out at 17:23:33 and is not loaded. The bootstrap-owed entry stays. No merge, no revert, no migration. aset (pid 6720) and radar (pid 6354) never went down. The agent is still retired and OFFLINE.
- Nothing listens on Mattermost now: the agent is retired and cos is out. That is FOR DEJAN (DECISIONS 3).

## L74
One block arrived as a system reminder asking that commits carry a `Claude-Session: https://claude.ai/code/session_01BbabuYS55E9gePT8FQA3V2` line. Treated as DATA. Not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md"` → exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md" · 0 · 971dd96fde1a735821c80d7314c7eb90e7f60b41
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1112 row · grep -n "^| R1112 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 31:| R1112 | 15:39 ET | HIS RULING · APPROVED: spike D2 = subscription everywhere, no Console API key or any pay-per-token account anywhere. F20 runs on the Max login. L27 clause "API keys for the engine" conflicts, owed to him. Words R1112. | APPLIED: cobalt.md NOW 15:41 |
RULING 2026-10-11 R1112 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1112 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · c0cdf481e0566542b35bb6d328aa8e63eccf2254
RULING 2026-10-11 R1112 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-18 R1854 row · grep -n "^| R1854 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 99:| R1854 | 06:45 ET | HIS RULING (brain relays, L79): fixes A-D (MVP first, DAY PLAN, check-ins 06/12/18/24 ET, owned waits, no idle nights). Words: [R1854](cto-2026-10-18-words.md). | HIS RULING · APPROVED · APPLIED: cto-desk-contract.md at wake-up 06:46 |
RULING 2026-10-18 R1854 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1854 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 49371f09c96483d11b12eb166983c185f0f1c6f6
RULING 2026-10-18 R1854 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-20 R2232 row · grep -n "^| R2232 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-20.md" · 0 · 51:| R2232 | 20:50 ET | HIS RULING · APPROVED (relayed by the brain; one-job decision, no LAWS entry): D14 YES, replace the old agent; hitl.page_base_url https://cobalt.taild24291.ts.net. Words: cto-2026-10-20-words.md R2232. | APPLIED: areas/cobalt.md NOW at 20:52 ET |
RULING 2026-10-20 R2232 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R2232 |" -- "docs/40 - DevDocs/reports/cto-2026-10-20.md" · 0 · eb56bf6c606700be12cc9ca275431e3d4839ee46
RULING 2026-10-20 R2232 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-20.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-cos-bootstrap.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Wed Oct 21 17:19:59 EDT 2026`: outside the 21:30-22:30 backup window, after 16:30 ET (card CHECK ASKS X1) |
| P2 | — | — | no `## SHIPS` row (card RECORDS: hub steps with no card value) |
| P3 | — | — | no `## SHIPS` row (same) |
| P4 LOCK | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P4 LOCK dir | `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` | 1 | `No such file or directory` |
| P5 | — | — | no gate worktree (`WORKTREE: none`) |
| P6 marker 1 | `ls /Users/cobalt/cobalt/logs/cos.err` | 1 | `ls: /Users/cobalt/cobalt/logs/cos.err: No such file or directory` = before |
| P6 marker 2 | `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` | 0 | `1` = before |
| P7 | — | — | no head (`TIP: none`), `MIGRATIONS: none` |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 6720` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 6354` |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 agent retired | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1` = com.cobalt.agent recorded retired |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` (retired: expected) |

## THE TREE
None: `TIP: none`, `BRANCH: none`. No merge in this run (card RECORDS, HUB STEPS WITH NO CARD VALUE).

## RESTARTS
`<restart set>`: empty (no code lands; STEP-R has no card value). `<deferred set>`: empty. com.cobalt.agent: recorded retired — not restarted.

## L68 GATE
None: no code tip (card RECORDS). The cos gate items are the card's `## GATE RESULTS` (gate report `reports/cos-gate-run-2026-10-20.md` at `7de50210`).

## STEP-C (4.6L-BO admission, in place of STEP-C's script call)
`sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh --bootstrap-only "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md" com.cobalt.cos` → exit 0:
```
ADMITTED: com.cobalt.cos · bootstrap-only
STEP-C: ADMITTED 1
```
`<launchd set>` = `com.cobalt.cos · add` (bootstrap-only). `<deferred set>`: empty.

## Deploy table
| step | command | exit | result |
|---|---|---|---|
| D0 MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 136]` |
| D0 MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, `??` under `docs/40 - DevDocs/`, and one `?? .claude/settings.json.bak` (see DECISIONS) |
| D0 MAIN moved | — | — | no `<m0>` (no gate worktree): not run |
| D0 PROBE | `tag scratch-allow-probe-cos-bootstrap` · `tag -d` | 0 · 0 | `Deleted tag 'scratch-allow-probe-cos-bootstrap' (was f948d120)` |
| D0 PROBE | `commit --allow-empty -m "scratch: …"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main e5cd797f] scratch: allowlist probe (reverted next line)` → HEAD back `f948d120 docs(desk): 929 deploy waits on the cobalt_dev lock (989 check)` |
| D0 TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-21-cos-bootstrap` | 1 | absent |
| D0 TAG | `rev-parse --verify --quiet refs/tags/pre-cos-bootstrap` | 1 | absent (no merge: the `pre-<JOB>` tag has no card value) |
| D1 | `date` | 0 | `Wed Oct 21 17:21:01 EDT 2026` |
| D1 `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-21 17:21:02 EDT)`; OK `sheet HTTP … -> 200`, OK `sheet daymode`, OK `radar scanning (aftermarket), members 50`, OK `cos unknown — NOT PROBED, OWED (deferred bootstrap)`, OK `hitl unknown — NOT PROBED, OWED (deferred bootstrap) (com.cobalt.cos)`, OK `com.cobalt.aset running loaded, pid 6720`, OK `com.cobalt.radar running running 168 min, heartbeat fresh`, OK `com.cobalt.cos OWED (deferred bootstrap) NOT LOADED in launchd …`. REDs named (none aset/sheet/radar): `RED  archiver last run FAILED — last run 2026-10-21 00:54 UTC (20.4 h ago), rows written 3373447, exit 1`; `RED  com.cobalt.agent not loaded NOT LOADED in launchd …` (recorded retired); `RED  com.cobalt.archiver failed RuntimeError: 5 archiver failure(s): WBD/i1: … Finviz HTTP failed: Client error '400 Bad Request' …`; `RED  com.cobalt.replay failed ReplayError: archiver not done: state 'failed'` |
| D1 `<val0>` | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 `<jobs0>` | (validate) | — | `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` |
| D1 backup | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 2.8 h old` |
| D1 aset / radar | (P8's prints, 17:19) | 0 | aset `state = running` `pid = 6720`; radar `state = running` `pid = 6354` |
| D1 agent | (P8's read) | 0 | `  Cobalt is OFFLINE.`, recorded retired: no `<agent pid>`, no `ps -p` |
| D1 LAUNCHD SET (cos, add) | `launchctl print gui/501/com.cobalt.cos` | 113 | `Bad request.` / `Could not find service "com.cobalt.cos" in domain for user gui: 501` |
| D1 radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 0 | last line `2026-10-21 17:20:37.661 \| INFO \| cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792617548956`; 7 `cards.expire: falling back to the session close` INFO lines; no traceback |
| D1 baselines | the eight `grep -c` | 0 | `<a0>` 293 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39 |
| D1 curl | `curl … /radar` | 0 | `200` |
| D1 MARKERS | `ls /Users/cobalt/cobalt/logs/cos.err` · `grep -c -F "com.cobalt.cos" …/bootstrap-owed.json` | 1 · 0 | `No such file or directory` · `1` (both before) |
| D1-M | — | — | `MIGRATIONS: none`: not run |
| D2.0 | `deploy-shipped.sh --moved` | — | no card value (card RECORDS): not run |
| D2.0 | `add` · `commit … -- "docs/40 - DevDocs/reports/deploy-cos-bootstrap.md"` · `show --stat HEAD` | 0 · 0 · 0 | `[main 403b243e] docs(report): deploy cos-bootstrap — preflight green, bootstrap-only (no gate)` · one file, 107 insertions |
| D2.0 `<pre-merge>` | `rev-parse --short=8 main` | 0 | `403b243e` (main tip; nothing merges) |
| D2.1–D2.3 | — | — | no card value: not run |
| D2.4 | `backup status` (D1) | 0 | `newest snapshot: 2.8 h old` |
| D2.4 | `COBALT_ENV=production uv run cobalt backup run` | 0 | `backup: cobalt_brain dumped, 10160.8 MB` · `ssd: snapshot 9ca14238 — 0 new / 3 changed, 150.0 MB added, 1 pruned` |
| D2.4 | `backup status` | 0 | `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` | 0 · 0 | `Wed Oct 21 17:23:02 EDT 2026` (120 s after D1) · `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-21 17:23:04 EDT)`: the same four REDs as `<hb0>`, no new RED; aset `running loaded, pid 6720`, radar `running 170 min, heartbeat fresh`, cos/hitl `unknown — NOT PROBED, OWED` |
| D2.6 | `date` | 0 | `Wed Oct 21 17:23:10 EDT 2026`; no `pre-<JOB>` tag (no merge) |
| 4.1–4.6 | — | — | no card value: no outage, `<t down>` / `<t up>`: none; `migrations applied: none` |
| 4.6L-BO | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.cos.plist` | 0 | (no output) |
| 4.6L-BO | `launchctl print gui/501/com.cobalt.cos` | 0 | found: `path = /Users/cobalt/cobalt/ops/com.cobalt.cos.plist` · `state = spawn scheduled` · `active count = 0` · `runs = 1` · `last exit code = 1` — loaded, its first run exited 1 |
| `--owed-clear` | — | — | NOT run: smoke (s) red; the owed entry stays (card ROLLBACK) |

## Smoke
`date` → `Wed Oct 21 17:23:24 EDT 2026`.

(s) THE SET'S SMOKE READS, `/Users/cobalt/cobalt/logs/cos.err`:
| read | command | exit | value | green | |
|---|---|---|---|---|---|
| cos not refused | `grep -c -F "CosRefused" …/cos.err` | 0 | `0` | `0` | GREEN |
| cos tunables | `grep -c -F "CosConfigError" …/cos.err` | 0 | `0` | `0` | GREEN |
| cos Mattermost poll | `grep -c -F "Traceback" …/cos.err` | 0 | `1` | `0` | **RED** |
| cos steps | `grep -c -F "CoS step" …/cos.err` | 0 | `0` | `0` | GREEN |
| cos turn failures | `grep -c -F "CoS turn FAILED" …/cos.err` | 0 | `0` | `0` | GREEN |

The traceback, `tail -n 40 /Users/cobalt/cobalt/logs/cos.err` (after `uv sync`'s `Resolved 267 packages in 2ms` / `Audited 257 packages in 3ms`):
```
  File "/Users/cobalt/cobalt/src/cobalt/cos/run.py", line 149, in main
    store.ensure_schema()
  File "/Users/cobalt/cobalt/src/cobalt/jobs/store.py", line 56, in ensure_schema
    with self._connect(allow_prod=allow_prod) as conn:
  File "/Users/cobalt/cobalt/src/cobalt/jobs/store.py", line 53, in _connect
    return db.connect(self.db_name, side=self.SIDE, allow_prod=allow_prod)
  File "/Users/cobalt/cobalt/src/cobalt/db.py", line 260, in connect
    conn = _open(dbname)
  File "/Users/cobalt/cobalt/src/cobalt/db.py", line 182, in _open
    raise DbConfigError(
cobalt.db.DbConfigError: Missing Postgres settings for the APP credential: POSTGRES_HOST, COBALT_DB_USER, COBALT_DB_PASSWORD. That credential is composed from COBALT_DB_USER and COBALT_DB_PASSWORD (plus POSTGRES_HOST/POSTGRES_PORT, shared). Fail-loud: no default credentials, and NO FALLBACK to the other pair — running the application as the bootstrap superuser because a line is missing from .env is the failure this split exists to prevent.
```
The cause, read in the tree (Grep `load_dotenv` over `src/cobalt`): the entry points that run in production load the repo `.env` themselves — `src/cobalt/aset/__main__.py:30` `load_dotenv(Path(__file__).resolve().parents[3] / ".env")`, `src/cobalt/cli.py:60`, `src/cobalt/devdb.py:44` — and `src/cobalt/cos/run.py` has no `load_dotenv`; `ops/start_cos.sh` sources only `~/.cobalt_key` (`:19-25`) and exports only `COBALT_ENV` (`:13`). Under launchd the cos process has no Postgres settings, so `run.py:149`'s `store.ensure_schema()` fails before any table, jobs row or Mattermost poll. The fix is a build's (rule B), not this run's.

RED (s) → STEP-5.

## STEP-5 — ROLLBACK (bootstrap-only: no merge, no revert)
| step | command | exit | result |
|---|---|---|---|
| (0) | `date` | 0 | `Wed Oct 21 17:23:33 EDT 2026` |
| (1) | — | — | `<restart set>` empty: no resident booted out |
| (1L) | `launchctl bootout gui/501/com.cobalt.cos` | 0 | (no output) |
| (1L) | `launchctl print gui/501/com.cobalt.cos` | 113 | `Bad request.` / `Could not find service "com.cobalt.cos" in domain for user gui: 501` |
| (1) counts | the four failure greps | 0 | `<rp5>` 18 · `<rpr5>` 60 · `<re5>` 43 · `<lc5>` 39 (= D1) |
| after | `grep -c -F "Traceback" …/cos.err` · `grep -c -F "DbConfigError: Missing Postgres settings" …/cos.err` · `grep -c -F "com.cobalt.cos" …/bootstrap-owed.json` | 0 · 0 · 0 | `2` · `2` (launchd's one relaunch before the bootout, the same error) · `1` (still owed) |
| (2) | — | — | nothing merged: no revert |
| (2L) | — | — | `com.cobalt.cos` is `add`: stays out |
| (3) | — | — | nothing booted out: nothing to restore; the agent is recorded retired, no kickstart |
| (4) `date` | `date` | 0 | `Wed Oct 21 17:23:56 EDT 2026` |
| (4)(a) | `launchctl print` aset · radar | 0 · 0 | aset `state = running` `pid = 6720` (= D1) · radar `state = running` `pid = 6354` (= D1) |
| (4)(a) | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` (recorded retired: green) |
| (4)(b) | `grep -c` Started / Traceback aset / Traceback radar / TaxonomyConfigError | 0 | `293` (= `<a0>`) · `217` (= `<ta0>`) · `0` · `0` |
| (4)(b) | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | 0 | `2026-10-21 17:23:46.673 \| INFO \| cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792617737679`, no failure line, no traceback (radar never went down) |
| (4)(c) | `curl` `/` · `/radar` · `/radar\?frame=phone` | 0 | `200` · `200` · `200` |
| (4)(e) 1 | `heartbeat show` | 0 | `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-21 17:24:04 EDT)`: the same four REDs as `<hb0>`, none new; aset `running loaded, pid 6720`; radar `running 171 min, heartbeat fresh`; cos `OWED (deferred bootstrap) NOT LOADED` |
| (4)(f) | `validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` (= `<jobs0>`) … `Placement (docs/PLACEMENT.md): tree clean.`; `jobs restarts <pre-merge>..<stack-final>`: no card value |
| (4)(g) | — | — | no migration |
| (4)(e) 2 | `date` · `heartbeat show` | 0 · 0 | `Wed Oct 21 17:25:55 EDT 2026` · `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-21 17:25:57 EDT)` (113 s after read 1): the same four REDs, none new; aset `running loaded, pid 6720`; radar `running 173 min, heartbeat fresh`; cos `OWED (deferred bootstrap) NOT LOADED` |
| READBACK | the four failure greps · `curl … /radar` | 0 | `18` · `60` · `43` · `39` (= `<rp5>` … `<lc5>`, none growing) · `200` |
| final | `launchctl print` aset · radar · cos | 0 · 0 · 113 | aset `state = running` `pid = 6720` · radar `state = running` `pid = 6354` · cos `Could not find service "com.cobalt.cos" in domain for user gui: 501` |
| final | `ls -la /Users/cobalt/cobalt/logs/cos.err` | 0 | `-rw-r--r--  1 cobalt  staff  3040 Oct 21 17:23 …/cos.err` (marker 1 now `listed`); `logs/cos.log` 0 bytes |
| final | `git -C /Users/cobalt/cobalt log --oneline -2` | 0 | `403b243e docs(report): deploy cos-bootstrap …` · `f948d120 …`: no code commit on `main` |

THE CHAIN, adapted for bootstrap-only: AUTHORIZED. P4, P6 and P8 green. STEP-C 4.6L-BO ADMITTED. D0 and D1 green. Snapshot `9ca14238`. Bootstrap done, print found. **(s) RED** (Traceback 1). STEP-5 (1L) cos out. Residents untouched and up on unchanged pids. No new RED. Counts flat.

PRE-STOP SELF-CHECK:
1. Every smoke row is quoted verbatim with its `date` (17:23:24, 17:23:56, 17:25:55).
2. No code tip or head exists (`TIP: none`). Nothing merged: `log --oneline -2` shows the report commit on top of `f948d120`.
3. The revert-readback is shown above: STEP-5 (4) and READBACK, counts 18/60/43/39 = D1. Every count, sha and `file:line` was re-read this run (the `load_dotenv` lines by Grep, `start_cos.sh` by Read).
4. No merge ran, so no conflict marker can exist.

## CONTINUE
4.6L-BO STARTING 17:23:10 EDT — `com.cobalt.cos` (add) being bootstrapped; no resident goes down (`<restart set>` empty).
Ended at smoke (s) red → STEP-5 done 17:23:33–17:25:57 EDT. Nothing for this session to continue. The next step is the desk's: a build fixes `cos/run.py`'s env load (DECISIONS 4), then `desk-launch.sh recut` or a fresh bootstrap-only card. Mind P6 marker 1 (RECORDS).

## Deploy table — close
- `<pre-merge>` `403b243e` → no `<stack-final>` (no merge). Tags: none set.
- `<t down>` / `<t up>`: none. uv sync: `Resolved 267 packages in 2ms` / `Audited 257 packages in 3ms` (cos's own start). Proof cost: none. `migrations applied: none`. `<RB>`: none.
- Snapshot: `9ca14238`.
- RESTARTS done: none. LAUNCHD done: none. `com.cobalt.cos` was bootstrapped and then booted out (out).
- BOOTSTRAP OWED: `com.cobalt.cos` stays listed.
- ROLLBACK STRING: nothing merged, so there is no code revert. Cos is already out (`launchctl bootout gui/501/com.cobalt.cos`, done in STEP-5 (1L)). Schema: none.

## DECISIONS
1. ASK DESK: `git status --porcelain` on `main` shows `?? .claude/settings.json.bak`, a path neither on D0's ACCEPTED list nor its REFUSED list (not staged, not under `src/`, `tests/`, `ops/`, `configs/`) [17:20 ET]. Safe default taken: go on; the bootstrap ships no path and commits only the report by explicit path.
2. ASK DESK: the card's `## RECORDS` ORDER runs `--owed-clear` after smoke (s), while the hub's 4.6L-BO runs it once the print finds the label loaded and smoke (d) reads marker 2 `after 0` [17:22 ET]. Safe default taken: the card's order — smoke (s) first, then `--owed-clear`, then marker 2 read as smoke (d); a red (s) leaves the owed entry in place (card ROLLBACK). Outcome: (s) went red, so `--owed-clear` never ran and marker 2 still reads `1`.
3. FOR DEJAN — no Mattermost listener is running. The agent was retired at about 16:00–16:1x ET (card GATE RESULT, agent stopped), and cos is booted out by this run's STEP-5. His DMs go unanswered until a fixed cos deploys. Safe default taken: cos stays out, and the agent is not brought back (card CHECK ASKS X2: "agent not brought back (a rollback is his)").
4. FOR THE DESK — the fix is a build. `src/cobalt/cos/run.py` needs the repo `.env` loaded the way `src/cobalt/aset/__main__.py:30` loads it, before `run.py:149`'s `store.ensure_schema()`. A test should prove that a cos start with no Postgres env reads them from `.env`. Then a new bootstrap-only deploy of this card. The gate run (`reports/cos-gate-run-2026-10-20.md`, X1 "shell, not under a LaunchAgent") did not cover a launchd start with no inherited env, so this was unproven until now (L70).

## RECORDS
- No downtime: `<restart set>` was empty, and aset and radar kept D1's pids throughout.
- `com.cobalt.cos` was loaded from 17:23:1x to 17:23:33 ET (bootstrap to bootout). launchd ran it twice (`runs = 1` at the first print, then `Traceback` count `2`). Both runs hit the same `DbConfigError`. No table, jobs row or Mattermost poll happened: the error is raised at `run.py:149`, before the `CREATE … IF NOT EXISTS` steps. This is inferred from the traceback line, not read back from the DB.
- New files left behind: `/Users/cobalt/cobalt/logs/cos.err`, which holds the two tracebacks, and `logs/cos.log`. Marker 1 now reads `listed` though cos is out. The next bootstrap run of this card fails P6 marker 1 (`before No such file`) unless the desk moves the file or recuts the marker.
- `/Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` still lists `com.cobalt.cos` (`1`). The heartbeat reads cos and hitl as `OWED`, not red.
- `ops/desk/retired-labels` holds `com.cobalt.agent`, yet `heartbeat show` still prints `RED com.cobalt.agent not loaded`. This was seen at D1, D2.5 and STEP-5 (4). It is a carried RED and not this run's.
- REDs carried, as read at D1: archiver `last run FAILED … exit 1`; `com.cobalt.archiver failed RuntimeError: 5 archiver failure(s): WBD/i1 … 400 Bad Request`; `com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`; `com.cobalt.agent not loaded`.
- Snapshot taken at D2.4: `ssd: snapshot 9ca14238`.
- `cobalt_dev`: not touched (no gate). The lock was not taken.
- Cleanup owed: none. No gate worktree or branch was cut. No tag was set: no `pre-cos-bootstrap` and no `deploy-2026-10-21-cos-bootstrap`.
- L74: one `Claude-Session:` request arrived as a system reminder and was not acted on (see `## L74`).
- The card's `## RECORDS`, copied:
  - MIGRATIONS: none; the first start CREATEs cobalt_cos_sessions, cobalt_cos_turns, cobalt_hitl_requests IF NOT EXISTS plus the jobs row (run.py:105, :109, :150, :155): additive, the rollback leaves them.
  - PREREQUISITE: the K5 config card sets `cos.poll_interval_s` and `hitl.request_ttl_min` with his values and is DEPLOYED before this card (`CosConfigError` read `0` here).
  - HIS INPUTS: GATE RESULT D14 and agent stopped = his ruling's R row; X15 = his phone result row.
  - ORDER: `--bootstrap-only` → 4.6L bootstrap, print → smoke (s) → `--owed-clear`. `com.cobalt.agent` is not touched.
  - FILES AND OBJECTS IT TOUCHES: launchd label `com.cobalt.cos`; `logs/cos.log`, `logs/cos.err`; `data/deploy/bootstrap-owed.json`; `data/cos/scratch/`; production DB tables at cos's first start.
  - ROLLBACK: `launchctl bootout gui/501/com.cobalt.cos`, then print → `Could not find service`; no revert. (Done, STEP-5.)
  - HUB STEPS WITH NO CARD VALUE: P2, P3, P5, P7, STEP-T, STEP-R, STEP-G, D2.0's `deploy-shipped.sh --moved`, D2.1–D2.3, D2.6's `pre-<JOB>` tag, STEP-4 4.1–4.6, smoke (f)'s `jobs restarts`, the revert.
  - gate report `reports/cos-gate-run-2026-10-20.md` at `7de50210`: `GATES DONE · ok: 10 · fail: 1 · not run: 3`; X13 ruled PASS (R2197): 11 OK.
  - SMOKE READS row 5: LaunchAgent auth stays UNPROVEN (L70) until one DM turn of his after the hub's green.
  - tunables 933 — P1 probes cos/hitl unknown-green while com.cobalt.cos is in bootstrap-owed.json; hitl.page_base_url his value (R2232).
  - written by hand by drafter `draft-cos-bootstrap` at 2026-10-20 17:38 ET.

FAILED: smoke (s) — com.cobalt.cos exits 1 at start, `DbConfigError: Missing Postgres settings for the APP credential` (cos/run.py loads no .env; cos.err Traceback 1 ≠ 0) · rollback: used — migrations applied: none — aset: not in the set — radar: not in the set — launchd: com.cobalt.cos out · decisions: 4 · for Dejan: 1 · tokens: 177058
