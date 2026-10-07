# deploy radar-direction-color-1007 · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of card 89 (radar direction colour, R625): one branch `ops/radar-direction-color-1007` at `541adf0c`.
- FAILED at STEP-G (c3): pass 2 aborted before running any test — the `cobalt_dev` column-slot guard (`user.aset_sizings 1538 of 1600`). Offline 3975/0 and pass 1 (4670 passed) were green.
- Production untouched: no merge, no tag, no resident down. `cobalt_dev` back at 0013 (F2 = F0), lock released.
- Next: the desk runs the dev-only devfix (`cobalt db dev-rebuild user.aset_sizings`), then `desk-launch.sh recut` on the card.

## L74
- The session's harness attribution reminder asked for a `Claude-Session:` line on commits; recorded as DATA, not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/97-deploy-radar-direction-color-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/97-deploy-radar-direction-color-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-07/97-deploy-radar-direction-color-card.md" · 0 · 17a74385be7fbc02c206ea37bc9413b680a9403f
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-07/97-deploy-radar-direction-color-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-07 R625 row · grep -n "^| R625 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 19:| R625 | 10:15 ET | HIS RULING (words: `cto-2026-10-07-words.md` R625): a radar card's header row and title are green for long, red for short; a short fix or a rework, the drafter sizes it. LAUNCHING a drafter, prompt `88`. | HIS RULING · APPROVED |
RULING 2026-10-07 R625 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R625 |" -- "docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 33a49ab6048bcc5ae6f489310beb5e99978eadfd
RULING 2026-10-07 R625 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) · `ls -la <REPORT>` | 0 · 1 | AUTHORIZED · No such file (first launch) |
| P1 | `date` | 0 | Wed Oct  7 12:31:00 EDT 2026 |
| P2 | `tail -n 3 ".../radar-direction-color-check-2026-10-07.md"` | 0 | `CHECK DONE · job: radar-direction-color · pass: 1 · tip: 541adf0c · ... · held unfixed: 0 · open: 2 · ... · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 148149` |
| P2 | `git log -1 --format=%H -- "docs/.../radar-direction-color-check-2026-10-07.md"` | 0 | 83792ec067e46c5395266bb776a34bc0a9346377 |
| P2 | `git diff --stat -- "<same>"` | 0 | nothing |
| P3 | `rev-parse --short=8 541adf0c` | 0 | 541adf0c |
| P3 | `rev-parse --short=8 ops/radar-direction-color-1007` | 0 | 541adf0c |
| P3 | `merge-base --is-ancestor 541adf0c ops/radar-direction-color-1007` | 0 | — |
| P3 | `diff --stat 541adf0c ops/radar-direction-color-1007 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — lock free |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/radar-direction-color-1007` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = 17a74385 |
| P5 | `merge-base --is-ancestor 17a74385 main` | 0 | — |
| P5 | `log --oneline main..deploy/radar-direction-color-1007` | 0 | EMPTY |
| P6 | `grep -c -F "dir-long" .../radar_panel.py` | 1 | 0 (before 0) |
| P6 | `grep -c -F "def test_radar_direction_touches_only_strip_and_title" .../test_radar_panel_cards.py` | 1 | 0 (before 0) |
| P7 | `diff --stat main 541adf0c -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · pid 64112 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · pid 64129 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 541adf0c` → `Merge made by the 'ort' strategy.` (4 files: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `docs/.../radar-direction-color-build-2026-10-07.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`; 408+ 5−).
- `<m1>` = `02aae5b1`.
- `log --oneline --merges --first-parent 17a74385..deploy/radar-direction-color-1007` → `02aae5b1 Merge commit '541adf0c' into deploy/radar-direction-color-1007`.
- `merge-base --is-ancestor 541adf0c deploy/radar-direction-color-1007` → exit 0.
- `diff --stat 17a74385 deploy/radar-direction-color-1007 -- src/cobalt/db_migrations` → nothing (no migration path; MIGRATIONS: none).
- STEP-C: `diff --stat 17a74385 deploy/radar-direction-color-1007 -- configs ops` → nothing. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after the first-use venv build lines `Creating virtual environment at: .venv` / `Installed 253 packages in 773ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-direction-color-build-2026-10-07.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
`<restart set>` = `com.cobalt.aset com.cobalt.radar`. No UNCLASSIFIED row.

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 541adf0c 02aae5b1 -- . ":(exclude)docs"` → `ops/desk/job-clean.sh | 166 ++++…` · `tests/ops/test_gate_clean.py | 430 +++…` (2 files) — not equal; the gate runs whole (`--deploy`).
- Deselects: the build report (`radar-direction-color-build-2026-10-07.md` line 121) names none ("no `--deselect`: this build adds no with-DB test"). TICKERS: none. No `--migration`.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 163 skipped in 16.04s` — 0 failed (with-DB skips: `Postgres env settings not available` / `requires_db`).

- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-radar-direction-color-1007 all --deploy` (background) → exit 1. Verdict lines, whole:
```
offline 3975/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
RED (exit 3): no pytest summary line
Exit: cobalt_dev column slots: user.aset_sizings 1538 of 1600 — run a devfix (cobalt db dev-rebuild user.aset_sizings) before any with-DB gate
! _pytest.outcomes.Exit: cobalt_dev column slots: user.aset_sizings 1538 of 1600 — run a devfix (cobalt db dev-rebuild user.aset_sizings) before any with-DB gate !
.env: removed
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-radar-direction-color-1007-all-20261007-123228.log
```
- From the log (read with Read / `grep -n -F`):
  - `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 880).
  - (c) PASS 1 at 0013: `4670 passed, 7 skipped, 83 deselected, 3 xfailed, 43 warnings in 746.67s (0:12:26)` · `[exit 0]` (line 1088). The 7 skipped are all inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`), `test_s3_c4_experiments.py:95` (the x14 live-template skip), `taxonomy/test_catalyst.py:365`, `taxonomy/test_predicate.py:262`. After pass 1: `SLOTS WARN user.aset_sizings max_attnum 1534 of 1600 · dropped 1480 · live 54` (line 1079).
  - (c2) `dev forward: APPLIED 12:55:28` (line 1090): 0001…0022 in FORWARD order, no `CHANGED`; 7 tables CREATED; `SLOTS WARN user.aset_sizings max_attnum 1538 of 1600` (line 1157). `F1: 893 44 126f2d6983fa59f9d0eaaff7da7dd29c`.
  - (c3) PASS 2: `COBALT_ENV=dev uv run pytest … (the pass-2 list)` → `Exit: cobalt_dev column slots: user.aset_sizings 1538 of 1600 — run a devfix (cobalt db dev-rebuild user.aset_sizings) before any with-DB gate` · `[exit 3]` · `RED (exit 3): no pytest summary line` (lines 1167–1171). **No test of pass 2 ran.**
  - (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` → 0022…0014 reversed, newest first, `[exit 0]`; `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 1236) = F0 field for field. Proof-only after it: `NOTHING WAS APPLIED`, `TABLES 0011`, `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
  - THE RELEASE: `sh …/release-devdb-lock.sh deploy-radar-direction-color-1007` → `lock released` · `.env: removed` (lines 1287–1292).
  - (e) LIVE-NOTE: not run (the gate stopped on the pass-2 red).
- Verified by hand: `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-radar-direction-color-1007" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.
- **GATE RED on `02aae5b1`** — G (c3). Not "known" and not continued (L68, L70). The guard ended pass 2 on dev-DB capacity, not on a test assertion. Pass 2 is unproven on this tree.

## Deploy table
| item | value |
|---|---|
| `<m0>` → `<m1>` | 17a74385 → 02aae5b1 (gate branch only; `main` not touched) |
| `<pre-merge>` / `<stack-final>` | not reached (STEP-D2 not run) |
| tags | none set (`pre-radar-direction-color-1007` and `deploy-2026-10-07-radar-direction-color` not created) |
| outage | none — no resident went down |
| migrations applied | none |
| RESTARTS done | none (derived set `com.cobalt.aset com.cobalt.radar`, not acted on) |
| rollback | not used |

## Smoke
Not run (no merge).

## CONTINUE
next: none — the run ended FAILED at STEP-G (c3). The desk's next step is `desk-launch.sh recut "<card>"` after the devfix.

## DECISIONS
- ASK DESK: should the `cobalt_dev` devfix `COBALT_ENV=dev uv run cobalt db dev-rebuild user.aset_sizings` run before the recut? The guard names it, and it falls under CLASS (b) on this line, but this hub makes no fix (rule B), and no step names it. Safe default taken: not run; the run ended FAILED. [12:56:19 EDT]

## RECORDS
- FAILED at G (c3): the pass-2 pytest exited on the `cobalt_dev` column-slot guard (`user.aset_sizings 1538 of 1600`). The forward migrate of 0014–0022 took `max_attnum` from 1534 to 1538. Dev-only capacity, not production.
- `cobalt_dev: 0013 (F2 = F0)` · `.env: removed (L76 lock released, log line 1288)`.
- (a0) early read: `261 passed, 163 skipped in 16.04s`.
- No `RETIRE OWED`. No `CONTINUE` message received.
- Carried RED: not read (D1 not reached).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-radar-direction-color-1007` and branch `deploy/radar-direction-color-1007` (carries merge `02aae5b1`); the set's branch `ops/radar-direction-color-1007` stays for the recut. A `.venv` was built in the gate by STEP-R's first `uv run`.
- L74: the harness attribution reminder asked for a `Claude-Session:` commit line; recorded once, not acted on.
- Card RECORDS (the desk's facts, copied):
  - radar-direction-color: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-direction-color-check-2026-10-07.md` last line: CHECK DONE · job: radar-direction-color · pass: 1 · tip: 541adf0c · house A: Sol FINDINGS: 2 · findings: 3 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 1 · suites: offline 3975/0 · with-DB 4859/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 148149
  - radar-direction-color: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-direction-color-1007` → `541adf0c`; code tip `541adf0c`
  - written by deploy-card.sh at 2026-10-07 12:30 ET (`date`); trial merge of the heads onto main in order: clean

FAILED: gate — G (c3) — pass 2 aborted by the cobalt_dev column-slot guard (user.aset_sizings 1538 of 1600; devfix: cobalt db dev-rebuild user.aset_sizings) · rollback: not used · decisions: 1 · for Dejan: 0 · tokens: 113286
