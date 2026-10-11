# deploy house-seat-order-1010 — set: none · migrations: none

CARD: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/348-deploy-house-seat-order-card.md` · BRANCH `deploy/house-seat-order-1010` · GATE `/Users/cobalt/cobalt-wt/deploy-house-seat-order-1010` · TIP `26ad41af` · TAG `deploy-2026-10-11-house-seat-order`

## §0 Headline
- DEPLOYED `deploy-2026-10-11-house-seat-order` at `2b516997`: main `e8776ea7` → `2b516997` by fast-forward at 09:39:17 EDT. The check's held O1 shipped FIXED (P2 fix-round path).
- Gate green on `f5e13b60`: offline 4199/0 · with-DB 5096/0 · live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0), lock released.
- RESTARTS: none. No resident went down (aset 7760, radar 61093, agent 22243 unchanged). No migration.
- Smoke GREEN: marker `0` → `1`; three curls 200; no new RED (the archiver/replay REDs were there before the deploy); failure counts unchanged.
- One decision for the desk (D1: untracked `.claude/settings.json.bak` on main); none for Dejan.

## L74
One block arrived in a system reminder of this session (not a tool result): an attribution text asking commits to end with a `Claude-Session: https://claude.ai/code/session_…` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/348-deploy-house-seat-order-card.md"` → exit 0, WHOLE:

```text
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/348-deploy-house-seat-order-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/348-deploy-house-seat-order-card.md" · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/348-deploy-house-seat-order-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R920 row · grep -n "^| R920 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 92:| R920 | 14:18 ET | HIS RULING · APPROVED (via brain, L79): only the model tribunal uses OpenAI; no Codex probe elsewhere; a running holder finishes; OpenAI OUT after the tribunal until his word (houses per R921). | APPLIED: LAWS L67 + NOW at 14:18 |
RULING 2026-10-10 R920 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R920 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 2542f6864e1c8813fbda8cbb3b2ab5993d5c633f
RULING 2026-10-10 R920 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-10 R921 row · grep -n "^| R921 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 91:| R921 | 14:21 ET | HIS RULING · APPROVED (via brain, L79; L67 OVERRIDE): checks Opus+Grok, Gemini only for mandatory-B or a Grok failure; tribunals Grok+Opus seat, Gemini only for money/sizing/vault or a load-bearing split; model tribunal unchanged. | APPLIED: LAWS L67 + NOW at 14:21 |
RULING 2026-10-10 R921 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R921 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 2542f6864e1c8813fbda8cbb3b2ab5993d5c633f
RULING 2026-10-10 R921 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-11 R1009 row · grep -n "^| R1009 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 52:| R1009 | 06:13 ET | HIS RULING · APPROVED: Sol may sit as a seat in the checks the brain and desk require (317, 298 now); every build and every deploy waiting on his word is approved. Words `cto-2026-10-11-words.md` R1009. | APPLIED: LAWS L67 + NOW at 06:31 |
RULING 2026-10-11 R1009 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1009 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · aebcf44974dfbfd3e7eb7815b8a583c4f86e9e1c
RULING 2026-10-11 R1009 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Sun Oct 11 09:05:03 EDT 2026` |
| P2 check stop line | `tail -n 3 "…/house-seat-order-check-2026-10-10.md"` | 0 | `CHECK DONE · job: house-seat-order-1010 · pass: 1 · tip: ed48d80d · … · held unfixed: 1 · open: 1 · … · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 153447` — carries `held unfixed: 1` and `ready: NO` (the row's literals) |
| P2 check committed | `git log -1 --format=%H -- "docs/40 - DevDocs/reports/house-seat-order-check-2026-10-10.md"` | 0 | `22a4301f66a71c13f83d14c06aea2f44e7263341` |
| P2 check clean | `git diff --stat -- "<check>"` | 0 | nothing |
| P2 fix-round: check tip ancestor of code tip | `git merge-base --is-ancestor ed48d80d 1b671292` | 0 | — |
| P2 fix report (at branch head) | `git show "26ad41af:docs/40 - DevDocs/reports/house-seat-order-build-2026-10-10.md"` | 0 | last line `BUILT · job: house-seat-order-1010 · tip: 1b671292 \| on 92c67916 \| … \| decisions: 2 · for Dejan: 0 · tokens: 96904`; line 208 `FIXED: O1 — tests/ops/test_authorize.py::test_check_o1_a_first_openai_line_does_not_hide_a_later_overrule` |
| P2 held ids | Grep `HELD, NOT FIXED` in the check report | 0 | one id, `O1` (line 99: `O1 · HELD, NOT FIXED — ops/desk/authorize.sh:197-209`) |
| P2 FIXED test at code tip | `git show 1b671292:tests/ops/test_authorize.py` | 0 | `def test_check_o1_a_first_openai_line_does_not_hide_a_later_overrule(desk):` present, no xfail mark |
| P3 code tip | `git rev-parse --short=8 1b671292` | 0 | `1b671292` |
| P3 branch head | `git rev-parse --short=8 ops/house-seat-order-1010` | 0 | `26ad41af` (= TIP) |
| P3 ancestry | `git merge-base --is-ancestor 1b671292 26ad41af` | 0 | — |
| P3 head adds docs only | `git diff --stat 1b671292 26ad41af -- . ':(exclude)docs'` | 0 | nothing |
| P4 LOCK | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate status | `git -C <GATE> status --short --branch` | 0 | `## deploy/house-seat-order-1010` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `0a1951ef` = `<m0>` |
| P5 m0 on main | `git merge-base --is-ancestor 0a1951ef main` | 0 | — |
| P5 nothing main lacks | `git log --oneline main..deploy/house-seat-order-1010` | 0 | empty |
| P6 MARKER | `grep -c -F -e "every column-0 HOUSE line" "/Users/cobalt/cobalt/ops/desk/authorize.sh"` | 1 | `0` (= before) |
| P7 MIGRATIONS | `git diff --stat main 26ad41af -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 7760` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 61093` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 26ad41af` → `Merge made by the 'ort' strategy.` (6 files: CHECK-HUB.md, house-seat-order-build-2026-10-10.md, ops/desk/authorize.sh, ops/desk/house-probe.sh, tests/ops/test_authorize.py, tests/ops/test_house_probe.py; 487+, 33−)
- `git -C <GATE> rev-parse --short=8 HEAD` → `f5e13b60` = `<m1>`
- `git log --oneline --merges --first-parent 0a1951ef..deploy/house-seat-order-1010` → `f5e13b60 Merge commit '26ad41af' into deploy/house-seat-order-1010` (one line, one head)
- `merge-base --is-ancestor 1b671292 deploy/house-seat-order-1010` → exit 0; `… 26ad41af …` → exit 0
- `git diff --stat 0a1951ef deploy/house-seat-order-1010 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C `git diff --stat 0a1951ef deploy/house-seat-order-1010 -- configs ops` → WHOLE:
```text
 ops/desk/authorize.sh   | 48 ++++++++++++++++++++++++++++++++++++------------
 ops/desk/house-probe.sh | 49 +++++++++++++++++++++++++++++++++++++++++++------
 2 files changed, 79 insertions(+), 18 deletions(-)
```
  No plist added, modified or removed.
- The set changes `CHECK-HUB.md`, not `DEPLOY-HUB.md` or `gate.sh`: L68's hub-text gate clause does not apply.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after uv created `.venv`: `Installed 253 packages in 884ms`), WHOLE:
```text
path	change	rule	restart
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/house-seat-order-build-2026-10-10.md	A	DOCS	-
ops/desk/authorize.sh	M	operator script; no Cobalt reader	-
ops/desk/house-probe.sh	M	operator script; no Cobalt reader	-
tests/ops/test_authorize.py	M	test/documentation; no resident	-
tests/ops/test_house_probe.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = EMPTY (none). No UNCLASSIFIED row. MIGRATIONS: none, so an empty set is consistent.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold — the check's stop line carries `with-DB 0/0` (count not above 0). The gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.02s` (0 failed; the skips are with-DB: `Postgres env settings not available` / `requires_db`).
- Deselects: none (the build report names no `--deselect`; the build was DB: none).
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-house-seat-order-1010 all --deploy` (background) → exit 0, verdict lines WHOLE:
```text
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-house-seat-order-1010-all-20261011-090702.log
```
- (a) offline `4199/0`.
- (c) PASS 1: the seven SKIPPED lines are each inside the allowed set by test and reason; `test_s3_c4_experiments.py:95` is the skip of `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F "def test_x14_live_his_template_strips_to_the_committed_fixture" <GATE>/tests/cobalt/test_s3_c4_experiments.py` → `96:`).
- (b)/(c2)/(f): log `896:F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; `1110:dev forward: APPLIED 09:31:22`; `2030:F2: 664 35 272c95bbb12241e3611e4b36326ccf87`; `2082:cobalt_dev: 0013 — F2 = F0`.
- (c3) with-DB `5096/0`.
- THE RELEASE: log `2084:lock released`, `2088:.env: removed` (L76 lock released at the gate's end, before 09:36:41). `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.
- (e) LIVE-NOTE `146/0` (log tail: `146 passed, 1 skipped`; the one skip is the `COBALT_TEST_LIVE_DRC` one, inside the set; none names `COBALT_LIVE_VAULT_ROOT`).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on f5e13b60

## Deploy table

### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git status --short --branch` | 0 | first line `## main...origin/main [ahead 113]` |
| MAIN porcelain | `git status --porcelain` | 0 | no staged line; ` M` / `??` under `docs/40 - DevDocs/` and ` M .claude/settings.json` (accepted); one other line `?? .claude/settings.json.bak` (neither accepted nor refused — see `## DECISIONS` D1); no dirty `src/`, `tests/`, `ops/`, `configs/` path |
| main moved | `git diff --stat 0a1951ef main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE tag | `git tag scratch-allow-probe-house-seat-order-1010` · `tag -d` | 0 · 0 | `Deleted tag 'scratch-allow-probe-house-seat-order-1010' (was 0a1951ef)` |
| PROBE commit | `git commit --allow-empty -m "scratch: …"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main b314c9d1] scratch: allowlist probe (reverted next line)` · — · `0a1951ef docs(desk): R1055 his approval, deploy card 348, check 324 launched` (HEAD back) |
| TAG | `git rev-parse --verify --quiet refs/tags/deploy-2026-10-11-house-seat-order` | 1 | absent |
| TAG pre | `git rev-parse --verify --quiet refs/tags/pre-house-seat-order-1010` | 1 | absent |

### STEP-D1 (baseline, 09:37:07 EDT)
| read | result |
|---|---|
| `<hb0>` `heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-11 09:37:08 EDT)`; OK: database, sheet HTTP (`http://127.0.0.1:5010/ -> 200`), sheet daymode, obsidian, mainframe, herdr, seat usage, backup, vault blocks, redactions, radar (`idle (overnight)`), aset running pid 7760, agent pid 22243 alive, `com.cobalt.radar running 1567 min, heartbeat fresh`. RED (named, not a stop — none is aset / sheet / radar): `RED  archiver  last run FAILED — last run 2026-10-10 00:54 UTC (36.7 h ago), rows written 3308843, exit 1`; `RED  com.cobalt.archiver  failed  RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …`; `RED  com.cobalt.replay  failed  ReplayError: archiver not done: state 'failed'`. AMB: `com.cobalt.herdr unmanaged`. |
| `<val0>` `validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Placement (docs/PLACEMENT.md): tree clean.` |
| `<jobs0>` | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` |
| `backup status` | `newest snapshot: 2.2 h old` (ssd local ARMED; b2 off) |
| aset | `state = running`, `pid = 7760` = `<aset pid>` |
| radar | `state = running`, `pid = 61093` = `<radar pid>` |
| agent | `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py` |
| `tail -n 8 radar.err` | last: `2026-10-11 09:36:44.011 \| INFO \| cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (eight `idle:overnight` cycles 09:25–09:36) |
| counts | `<a0>` 277 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39 |
| `/radar` curl | `200` |
| MARKER | `0` (= before) |
| migration reads | not run (MIGRATIONS: none) |

### STEP-D2
| step | command | result |
|---|---|---|
| D2.0 | `git add` · `git commit … -- "docs/40 - DevDocs/reports/deploy-house-seat-order-1010.md"` · `show --stat HEAD` | `[main e8776ea7] docs(report): deploy house-seat-order-1010 — gate green on f5e13b60` · one file, 167+ |
| `<pre-merge>` | `git rev-parse --short=8 main` | `e8776ea7` |
| D2.1 | `git -C <GATE> merge --no-edit main` | `Merge made by the 'ort' strategy.` (the report only) |
| D2.2 | `rev-parse --short=8 HEAD` · `rev-parse 2b516997^2` · `merge-base --is-ancestor f5e13b60 2b516997` | `<stack-final>` = `2b516997` · `e8776ea7` (= `<pre-merge>`) · exit 0 |
| D2.3 | `git diff --stat f5e13b60 2b516997 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D2.4 | `backup status` · `backup run` · `backup status` | `newest snapshot: 2.3 h old` · `backup: cobalt_brain via pg_dump inside cobalt_memory — 6693.3 MB` / `ssd: snapshot 8d614980 — 0 new / 3 changed, 26.4 MB added, 1 pruned` · `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` | `09:38:59` · `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-11 09:39:01 EDT)` — 113 s after D1's 09:37:08; the same three REDs as `<hb0>` (archiver probe, com.cobalt.archiver, com.cobalt.replay), no new RED; aset pid 7760, radar `heartbeat fresh` |
| D2.6 | `date` · `git tag pre-house-seat-order-1010` · `rev-parse` | `Sun Oct 11 09:39:06 EDT 2026` · tag at `e8776ea7` |

### STEP-4 (restart set EMPTY)
| step | command | result |
|---|---|---|
| 4.1 | `date` | `Sun Oct 11 09:39:17 EDT 2026` = `<t down>` (no resident goes down) |
| 4.2 | — | nothing (empty set) |
| 4.3 | `git rev-parse --short=8 HEAD` · `git merge --ff-only deploy/house-seat-order-1010` | `e8776ea7` (= `<pre-merge>`) · `Updating e8776ea7..2b516997` / `Fast-forward` (6 files, 487+, 33−) |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` (= `<jobs0>`); `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.6 | — | nothing to bootstrap; `<t up>` = 4.3's time `09:39:17`; downtime: none |

### CLOSE
| item | value |
|---|---|
| landing | `<pre-merge>` `e8776ea7` → `<stack-final>` `2b516997` (main tip `2b516997`) |
| tags | `pre-house-seat-order-1010` at `e8776ea7`; `deploy-2026-10-11-house-seat-order` at `2b516997` (set after the green smoke) |
| `<t down>` / `<t up>` / seconds | none (empty restart set; 4.1 `date` 09:39:17, merge at 09:39:17) |
| uv sync line | none at 4.4 (no migration). The gate's first `uv run` in `<GATE>` created `.venv`: `Installed 253 packages in 884ms` |
| proof cost | none in production (no migration); the gate's dev proof-only: `Proof cost: total 5.2 s` (log line 2075) |
| migrations applied | none |
| `<RB>` before / after | n/a (no READ-BACK on the card) |
| snapshot | `ssd: snapshot 8d614980` (D2.4) |
| RESTARTS done | none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 2b516997` — no resident to take down (restart set empty). 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` |

## Smoke
`<t up>` = 09:39:17 (4.3's `date`; empty set). FIRST CALLS: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1's).

| row | date | command | result | verdict |
|---|---|---|---|---|
| (a) | 09:39:31 | `launchctl print` aset · radar · `cobalt.sh status` | aset `state = running`, `pid = 7760` (SAME as D1, outside the set) · radar `state = running`, `pid = 61093` (SAME) · `Cobalt is ONLINE (PID: 22243).` (one line; same pid) | GREEN |
| (b) | 09:39:35 | `grep -c "Started server process" aset.err` · `tail -n 30 aset.err` · Traceback / TaxonomyConfigError counts | `277` (= `<a0>`, aset outside the set) · last lines `2026-10-10 13:23:12 … INFO: Started server process [7771]` … `INFO: Uvicorn running on http://127.0.0.1:5010` (yesterday's start; no new line) · aset Traceback `217` (= `<ta0>`) · radar Traceback `0` · TaxonomyConfigError `0` | GREEN (radar tails below) |
| (b) radar tail 1 | 09:40:49 (`<t up>` + 92 s) | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | last line `2026-10-11 09:40:04.052 \| INFO \| cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` — a cycle after `<t up>`; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback in the 12 lines | GREEN (settled; tails 2 and 3 not needed) |
| (c) | 09:39:39 | three curls | `/` `200` · `/radar` `200` · `/radar\?frame=phone` `200` | GREEN |
| (d) | 09:39:42 | `grep -c -F -e "every column-0 HOUSE line" "/Users/cobalt/cobalt/ops/desk/authorize.sh"` | `1` (after = 1) | GREEN |
| (e) 1 | 09:39:47 | `heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-11 09:39:48 EDT)` — the same three REDs as `<hb0>`; `com.cobalt.radar running 1570 min, heartbeat fresh`; aset pid 7760; agent pid 22243 | no new RED |
| (e) 2 | 09:41:40 | `heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-11 09:41:41 EDT)` — 113 s after (e) 1; the same three REDs as `<hb0>`; `com.cobalt.radar running 1572 min, heartbeat fresh` | GREEN (no new RED) |
| (f) | 09:39:50 | `validate` · `jobs restarts e8776ea7..2b516997` | exit 0, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` (= `<jobs0>`) · exit 0, the same six rows as STEP-R, `RESTARTS: none` (= `<restart set>`), no UNCLASSIFIED | GREEN |
| (g) | — | — | no migration | n/a |
| (s) | 09:39:53 | the O1 fix is on main · `grep -c -F -e "every column-0 HOUSE line" "/Users/cobalt/cobalt/ops/desk/authorize.sh"` | `1` (card: prints 1) | GREEN |
| (h) | 09:42:17 (`<t up>` + 180 s) | the four failure counts · `/radar` curl | `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39 (= `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, none growing) · `200`; no `census` read on the card | GREEN |

SMOKE: GREEN.

THE CHAIN: every check committed (P2: check `22a4301f`, fix report at `26ad41af` with `FIXED: O1`) → the tips re-read (P3: `1b671292`, `26ad41af`) → the merged tree `f5e13b60` (T) → RESTARTS derived `none` (R) → three suites green on `f5e13b60` (G: offline 4199/0, with-DB 5096/0, live-note 146/0) → `<stack-final>` `2b516997` = `<m1>` + docs (D2.3 empty) → landed by `--ff-only` `e8776ea7..2b516997` (4.3) → marker `1` (d) → no migration (g) → residents up, unchanged pids (a) → radar cycling at 09:40:04 and heartbeat fresh (b, e) → the set's read `1` (s) → no growing count (h). The card surface is not readable here; the desk confirms it with him (L70).

## CONTINUE
next: STEP-D0 (gate green at 09:36:41)
OUTAGE STARTING 09:39:06 — residents of none (empty restart set) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
next: none — 4.6 ended at 09:39:17 (nothing down); smoke GREEN at 09:42:17; STEP-7 closed.

### PRE-STOP SELF-CHECK
1. Every smoke row's evidence is quoted verbatim with its `date` (`## Smoke`: 09:39:31, 09:39:35, 09:40:49, 09:39:39, 09:39:42, 09:39:47, 09:41:40, 09:39:50, 09:39:53, 09:42:17). YES.
2. Every code tip and head was re-read (P3: `1b671292`, `26ad41af`) and is an ancestor of `<stack-final>`: `git merge-base --is-ancestor 1b671292 2b516997` → exit 0; `… 26ad41af 2b516997` → exit 0. YES.
3. REVERT-READBACK shown at (h): the four counts 18 / 60 / 43 / 39 = the first calls after `<t up>`; every count, sha and line number above was read from tool output in this run. YES.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.`; D2.1 the same; `--ff-only` landed. YES.
THE RELEASE: nothing held — the gate released the lock (`lock released`, `.env: removed`); `ls -la <GATE>/.env` and the lock dir → No such file.

## DECISIONS
- D1 · ASK DESK: `git status --porcelain` on main shows `?? .claude/settings.json.bak`, a line D0's ACCEPTED list does not name and its REFUSED list does not name (not staged, not under `src/`, `tests/`, `ops/`, `configs/`). Safe default taken: not a refusal; went on. It is untracked, outside the gate's tree, and the `--ff-only` merge does not touch it. [09:36:41 EDT]

## RECORDS
- Downtime: none (restart set empty; no resident went down).
- `cobalt_dev: 0013 (F2 = F0)` — gate log `2082:cobalt_dev: 0013 — F2 = F0`; lock released, `.env: removed`.
- RETIRE OWED: none (no plist removed).
- The carried RED as read (not of this set; named at D1, D2.5 and smoke (e), not a stop): `RED  archiver  last run FAILED — last run 2026-10-10 00:54 UTC …, exit 1`; `RED  com.cobalt.archiver  failed  RuntimeError: 18 archiver failure(s): DKNG/i2: … '429 Too Many Requests' …`; `RED  com.cobalt.replay  failed  ReplayError: archiver not done: state 'failed'`.
- The aset.err tail at smoke (b) ends on yesterday's (2026-10-10 13:23) `ScratchLocked` startup failure and the start that followed it (`Started server process [7771]` → `Uvicorn running on http://127.0.0.1:5010`); counts unchanged by this deploy (Traceback 217 = 217).
- Not a refusal, a cwd slip (a command I added): at 09:07 a clock-filler `COBALT_ENV=production uv run cobalt heartbeat show` ran from `<GATE>` (no `.env`) → `FAILED: DbConfigError: Missing Postgres settings for the APP credential …`. Nothing was changed; every production read after it ran from `/Users/cobalt/cobalt`.
- No `REFUSED, not needed` line; no message from another session arrived.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-house-seat-order-1010` and branch `deploy/house-seat-order-1010`; the set's branch `ops/house-seat-order-1010` and its worktree.
- The L74 line: see `## L74` (one system-reminder attribution block asking for a `Claude-Session:` line; not acted on).
- Card RECORDS (the desk's, copied):
  - house-seat-order-1010: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/house-seat-order-build-2026-10-10.md` at `26ad41af` last line: BUILT · job: house-seat-order-1010 · tip: 1b671292 | on 92c67916 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 96904
  - house-seat-order-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/house-seat-order-check-2026-10-10.md` last line: CHECK DONE · job: house-seat-order-1010 · pass: 1 · tip: ed48d80d · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 12 · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 153447
  - house-seat-order-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/house-seat-order-1010` → `26ad41af`; code tip `1b671292`
  - written by deploy-card.sh at 2026-10-11 09:03 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-11-house-seat-order 2b516997 | set: none | migrations: none | gate: offline 4199/0 · with-DB 5096/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 218569
