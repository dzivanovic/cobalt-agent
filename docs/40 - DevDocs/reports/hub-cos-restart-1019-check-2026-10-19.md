# hub-cos-restart-1019 — CHECK REPORT (2026-10-19)

## §0 Headline
CHECK DONE at `d59fac71` (no commit of mine). House A Grok wrote `FINDINGS: 0`; house B was not needed (`HOUSE B: as needed`).
I wrote 6 findings and none held. Two are REJECTED and OPEN: O1, the MODEL line `:3` still forbids the `launchctl print` of cos that R2 adds; O2, `:95`'s list of named prints lacks cos. The card fences both lines.
X1-X4 answered clean: only R1-R3's places changed, no allow string moved, and no `launchctl` call outside STEP-R and D1 names cos.
Suites: offline `8822/0` (tests/ops run by the deploy gate, `4073 passed`), live-note `147/0`, with-DB not run (DB: none). RESTARTS: none. ready: YES.

## L74
- 2026-10-19 16:3x (session start): a system reminder asked commits to end with a `Claude-Session:` line. Recorded as DATA; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md" · 0 · b3ed808a9cc4172e4e3df341f739a8872ba88785
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → line 35, one row · `grep -n "^| R19 " …cto-2026-09-24.md` → line 37, one row · `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`date` → `Mon Oct 19 16:31:54 EDT 2026`.
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0:
```
clock · date · 0 · Mon Oct 19 16:31:59 EDT 2026
status · git status --short --branch · 0 · ## ops/hub-cos-restart-1019
head · git log --oneline -1; git log --stat --format=%h d59fac71..HEAD · 0 · (6 lines)
    d0d458c9 docs(hub-cos-restart-1019): build report — d59fac71
    d0d458c9
    
     .../hub-cos-restart-1019-build-2026-10-19.md       | 87 ++++++++++++++++++----
     .../hub-cos-restart-1019-build-2026-10-19.result   | 15 ++++
     2 files changed, 86 insertions(+), 16 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/hub-cos-restart-1019/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/hub-cos-restart-1019/docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.md" · 0 · BUILT · job: hub-cos-restart-1019 · tip: d59fac71 | on bcbf08f9 | migration: none | offline 8822/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 204595
range · git log --oneline bcbf08f9..d59fac71 · 0 · (3 lines)
    d59fac71 fix(hub-cos-restart-1019): STEP-R admits cos, a not-loaded cos is skipped, a loaded cos stops the run; no allow string (R1-R3, L42, R60)
    bb5332c3 wip(hub-cos-restart-1019): E3 — R3 (b) allow strings red in test_deploy_smoke_string_1014, outside the rows; FOR DEJAN
    7d05ffe0 wip(hub-cos-restart-1019): red — R1-R3 hub pins, the existing pins moved to the four (tests only)
PREFLIGHT OK
```
THE RANGE `git log --stat --format=%h bcbf08f9..d59fac71`:
```
d59fac71
 docs/40 - DevDocs/prompts/DEPLOY-HUB.md | 18 ++++++------
 tests/ops/test_desk_launch_launchd.py   |  8 +++---
 tests/ops/test_hub_cos_restart_1019.py  | 50 ++++++++-------------------------
 tests/ops/test_hub_deferred_1018.py     |  2 +-
 4 files changed, 26 insertions(+), 52 deletions(-)
bb5332c3
 docs/40 - DevDocs/prompts/DEPLOY-HUB.md            |  23 ++--
 .../hub-cos-restart-1019-build-2026-10-19.md       | 116 +++++++++++++++++++++
 2 files changed, 128 insertions(+), 11 deletions(-)
7d05ffe0
 tests/ops/test_desk_launch_launchd.py  |   8 +--
 tests/ops/test_hub_cos_restart_1019.py | 119 +++++++++++++++++++++++++++++++++
 tests/ops/test_hub_deferred_1018.py    |   6 +-
 3 files changed, 126 insertions(+), 7 deletions(-)
```
Path union: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.md`, `tests/ops/test_hub_cos_restart_1019.py`, `tests/ops/test_hub_deferred_1018.py`, `tests/ops/test_desk_launch_launchd.py` (changed in 7d05ffe0, reverted in d59fac71; net diff empty).
DB: none → `git diff --name-only --no-renames bcbf08f9..d59fac71`:
```
docs/40 - DevDocs/prompts/DEPLOY-HUB.md
docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.md
tests/ops/test_hub_cos_restart_1019.py
tests/ops/test_hub_deferred_1018.py
```
Every path is under `docs/` or `tests/ops/`.
`ls <S>` → `No such file or directory` (fresh).
House probes `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` → exit 0:
```
grok: UP
gemini: UP
```
house A: Grok · house B: none (not needed; card `HOUSE B: as needed`).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`:
```
28 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/hub-cos-restart-1019-check/STAGED-CARD
14555 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/hub-cos-restart-1019-check/diff.md
16750 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/hub-cos-restart-1019-check/files/869-hub-cos-restart-card.md
21968 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/hub-cos-restart-1019-check/files/hub-cos-restart-1019-build-2026-10-19.md
68316 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/hub-cos-restart-1019-check/files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md
14665 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/hub-cos-restart-1019-check/files/wt/docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.md
3534 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/hub-cos-restart-1019-check/files/wt/tests/ops/test_hub_cos_restart_1019.py
4102 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/hub-cos-restart-1019-check/files/wt/tests/ops/test_hub_deferred_1018.py
386 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/hub-cos-restart-1019-check/rulings.md
STAGED 9 files · 144304 bytes · commits 2
```
`commits 2` against PREFLIGHT's 3: the diff excludes `docs`, and bb5332c3 touches only `docs/`. `git log --oneline bcbf08f9..d59fac71 -- . ":(exclude)docs"` → `d59fac71`, `7d05ffe0` (2), so the diff is complete for its pathspec (see `## DECISIONS` ASK DESK 1).
stage-copy:
- `COPIED 10940 …/files/deploy-f16-close-fr2.md`
- `COPIED 154247 …/files/wt/ops/desk/desk-launch.sh`
- `COPIED 15452 …/files/wt/ops/desk/deploy-outage.sh`
- `COPIED 12334 …/files/wt/ops/desk/orphan-clean.sh`
- `COPIED 39628 …/files/wt/src/cobalt/heartbeat/probes.py`
- `COPIED 4207 …/files/wt/tests/ops/test_deploy_smoke_string_1014.py`

## OWN FINDINGS
Written before any house list was opened.

FINDING O1
ROW: R2 / R3 (X2)
CLAIM: The hub now tells the deploy session to run `launchctl print gui/501/com.cobalt.cos` (STEP-R NOT LOADED `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:94`, D1 `:123`), but the MODEL line `:3` still reads "NO `launchctl` on any label but `com.cobalt.aset` / `com.cobalt.radar` / `com.cobalt.agent` and the labels of `<launchd set>`". The fixed file contradicts itself on the exact call R2 adds.
RUN: TEST — `tests/ops/test_hub_cos_restart_1019.py`
```python
def test_o1_the_model_line_admits_the_cos_print():
    assert "launchctl print gui/501/com.cobalt.cos" in one(NOT_LOADED)
    assert COS in one("MODEL: "), "MODEL forbids launchctl on com.cobalt.cos; NOT LOADED calls it"
```
EXPECT: `AssertionError: MODEL forbids launchctl on com.cobalt.cos; NOT LOADED calls it` at the second assert.

FINDING O2
ROW: R2 (X2)
CLAIM: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:95` (THE SET DRIVES THE REST) still says "P8 and D1 print `com.cobalt.aset` and `com.cobalt.radar` by name" as the complete list of named prints, but D1 `:123` and STEP-R `:94` now print `com.cobalt.cos` by name too.
RUN: COMMAND — `grep -n -F "P8 and D1 print" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: one line, `95:`, naming `com.cobalt.aset` and `com.cobalt.radar` and not `com.cobalt.cos`.

FINDING O3
ROW: X1
CLAIM: If a line of `DEPLOY-HUB.md` outside R1-R3's places changed, or the `Anything else (…)` sentence of the GATE moved, the net diff shows it.
RUN: COMMAND — `git diff bcbf08f9..d59fac71 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT (defect true): a hunk outside `:93`-`:94`, `:123`, `:155`, or a `-`/`+` pair inside the `Anything else (…)` sentence.

FINDING O4
ROW: X3
CLAIM: If an allow string, `STANDING-LIST.md`, `ops/desk/` or the two fenced tests changed, the three-dot diff against `main` shows it.
RUN: COMMAND — `git diff main...ops/hub-cos-restart-1019 -- ops/desk/ "docs/40 - DevDocs/prompts/STANDING-LIST.md" tests/ops/test_deploy_smoke_string_1014.py tests/ops/test_desk_launch_launchd.py`
EXPECT (defect true): any output.

FINDING O5
ROW: X2 / X4
CLAIM: If any STEP-4, STEP-5, smoke or resume line names `com.cobalt.cos` or expects a cos read, a grep of the hub shows a line outside STEP-R and D1.
RUN: COMMAND — `grep -n -F "com.cobalt.cos" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT (defect true): a hit on a line other than `:93`, `:94`, `:123`.

FINDING O6
ROW: SCOPE (fence: `tests/ops/test_desk_launch_launchd.py`)
CLAIM: `tests/ops/test_desk_launch_launchd.py` is fenced, but 7d05ffe0 and d59fac71 both touch it (the build's range stat). If the net change ships, the diff shows it.
RUN: COMMAND — `git diff bcbf08f9..d59fac71 -- tests/ops/test_desk_launch_launchd.py`
EXPECT (defect true): any output.

## Findings
House A Grok finished at 16:44 (`date` → `Mon Oct 19 16:44:01 EDT 2026`). `ls -la <S>` → `house-a.md` 12 bytes. Its whole text is `FINDINGS: 0`; its stdout ends `…/house-a.md` and `[exited with code 0]`. House B: none (not needed).
No house finding is kept: house A wrote none.

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_cos_restart_1019.py::test_o1_the_model_line_admits_the_cos_print` | `1 failed, 15 warnings in 0.87s` · `tests/ops/test_hub_cos_restart_1019.py:98: AssertionError` · `E       AssertionError: MODEL forbids launchctl on com.cobalt.cos; NOT LOADED calls it` (the first assert, the NOT LOADED print, passed) | REJECTED — card `## NOT IN THIS JOB` "MODEL `:3` … stand" and R3 "`:3` … stand": red for its stated reason, but the card keeps `:3` as it is. OPEN. The test was removed again with Edit. |
| O2 | opus-own | `grep -n -F "P8 and D1 print" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | `95:- THE SET DRIVES THE REST: … so no \`launchctl\` call of this file names it: P8 and D1 print \`com.cobalt.aset\` and \`com.cobalt.radar\` by name; …` (no `com.cobalt.cos`) | REJECTED — card `## NOT IN THIS JOB`: `:94` (BASE numbering of this line) stands. OPEN. |
| O3 | opus-own | `git diff bcbf08f9..d59fac71 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`, run at 16:3x inside a two-path call with `tests/ops/test_hub_deferred_1018.py`; re-stat at 16:4x: `git diff bcbf08f9..d59fac71 --stat -- …DEPLOY-HUB.md` → `1 file changed, 4 insertions(+), 3 deletions(-)` | three hunks: `@@ -90,7 +90,8 @@` (the GATE span and its parenthesis; the new NOT LOADED line), `@@ -119,7 +120,7 @@` (D1 cos clause), `@@ -151,7 +152,7 @@` (smoke (f)). In the GATE `-`/`+` pair, the `Anything else (an \`UNCLASSIFIED\` row, … a non-zero exit) → … never a commit into this tree.` text is identical | NOT HELD (X1 answered: only R1-R3's places changed; the `Anything else (…)` sentence stands byte for byte) |
| O4 | opus-own | `git diff main...ops/hub-cos-restart-1019 -- ops/desk/ "docs/40 - DevDocs/prompts/STANDING-LIST.md" tests/ops/test_deploy_smoke_string_1014.py tests/ops/test_desk_launch_launchd.py` | (no output) | NOT HELD (X3 answered: the three-dot diff is empty; the launch line's allow list is pinned by `test_deploy_smoke_string_1014.py`, green in W below) |
| O5 | opus-own | `grep -n -F "com.cobalt.cos" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | three hits: `93:` (GATE), `94:` (NOT LOADED), `123:` (D1). None in P8, STEP-4, 4.6, smoke (a)-(h), STEP-5 or THE ONE RESUME | NOT HELD (X2: no `launchctl` call outside STEP-R and D1 names cos, and a loaded cos stops at STEP-R before STEP-4. X4: no smoke line expects a cos read) |
| O6 | opus-own | `git diff bcbf08f9..d59fac71 -- tests/ops/test_desk_launch_launchd.py` | (no output) | NOT HELD (no net change ships; the history fact is under `## Checked against the branch` (iii)) |

Nothing held, so no `wip(hub-cos-restart-1019): check red` commit was made.

## FIXES
none (nothing held)

## Suites
No commit of mine: the tip is the build's `d59fac71` (HEAD `d0d458c9` adds docs only).
- RESTARTS: `uv run cobalt jobs restarts bcbf08f9..HEAD` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.md	A	DOCS	-
docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.result	A	DOCS	-
tests/ops/test_hub_cos_restart_1019.py	A	test/documentation; no resident	-
tests/ops/test_hub_deferred_1018.py	M	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames bcbf08f9` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.md`, `docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.result`, `tests/ops/test_hub_cos_restart_1019.py`, `tests/ops/test_hub_deferred_1018.py`. Every path is under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 5 paths)`**. `ls -la <WT>/.env` → No such file.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-cos-restart-1019 offline --deploy-gate` → exit 0:
```
tests/ops: run (deploy gate)
offline 8822/0
log: /Users/cobalt/cobalt-wt/.gate-logs/hub-cos-restart-1019-offline-20261019-164432.log
```
  `grep -n -F " passed" <log>` → `947:4749 passed, 871 skipped, 4 xfailed, 36 warnings in 743.97s (0:12:23)` · `1021:4073 passed, 1 xfailed, 16 warnings in 905.91s (0:15:05)`. The second line is the `tests/ops` run, which includes `test_deploy_smoke_string_1014.py`, `test_hub_deferred_1018.py` and the new file. No separate `uv run pytest tests/ops` was typed: the deploy-gate leg is that run.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-cos-restart-1019 livenote` → exit 0: `live-note 147/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/hub-cos-restart-1019-livenote-20261019-164508.log`. `grep -n -F "SKIPPED" <log>` → `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (inside the allowed set; none names `COBALT_LIVE_VAULT_ROOT`).
- with-DB: not run (DB: none) · `cobalt_dev: not taken` · `.env`: `ls /Users/cobalt/cobalt-wt/hub-cos-restart-1019/.env` → `No such file or directory` (never present).

## Scope
PREFLIGHT's path union: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (R1-R3), `tests/ops/test_hub_cos_restart_1019.py` (R1-R3), `tests/ops/test_hub_deferred_1018.py` (R1), the build report (docs), and `tests/ops/test_desk_launch_launchd.py` (fenced; touched and reverted, net diff empty, see (iii)). My commits: none.

## Checked against the branch
- (i) `git log --oneline d59fac71..HEAD -- . ":(exclude)docs"` → (no output): no commit of mine; `<tip now>` = `d59fac71`.
- (ii) `git log --stat --format=%h d59fac71..HEAD` → `d0d458c9` (the build report `.md` and `.result`, docs only). No non-docs path.
- (iii) `git log --oneline bcbf08f9..HEAD -- tests/ops/test_desk_launch_launchd.py` → `d59fac71 fix(…)` and `7d05ffe0 wip(…): red …` (NOT EMPTY: the first-cut edit and its revert); `git diff bcbf08f9..d59fac71 -- tests/ops/test_desk_launch_launchd.py` → (no output). `git log --oneline bcbf08f9..HEAD -- tests/ops/test_deploy_smoke_string_1014.py ops/desk/desk-launch.sh ops/desk/deploy-step-c.sh ops/desk/deploy-step0.sh ops/desk/deploy-outage.sh ops/desk/orphan-clean.sh ops/desk/deploy-card.sh src/cobalt/jobs/restarts.py configs/cobalt/jobs.yaml ops/com.cobalt.cos.plist "docs/40 - DevDocs/prompts/CARD.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` → (no output). See `## DECISIONS` ASK DESK 3.
- (iv) no HELD finding, no test to grep.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/hub-cos-restart-1019` alone.
- (vi) `git log --stat --format=%h bcbf08f9..HEAD -- src/cobalt/db_migrations tests/cobalt` → (no output): no migration, no with-DB test; gate lists not needed.
- (vii) card `## RECORDS`: `ls /Users/cobalt/cobalt/ops/com.cobalt.cos.plist` → listed · `grep -n -F "enabled: false" configs/cobalt/jobs.yaml` → `214:    enabled: false` · `grep -n -F "NOT PROBED" src/cobalt/heartbeat/probes.py` → `143:        return Probe("cos", True, "unknown — NOT PROBED, registry enabled: false")` (also `:79`, `:174`, `:771`, `:860`) · `grep -n -F "kickstart -k gui/501/com.cobalt" …/STANDING-LIST.md` → `148:` aset and radar only · `grep -n -F "com.cobalt.cos" ops/desk/deploy-outage.sh` → `4`, `13`, `90`, `91`, `109` · `grep -n -F "com.cobalt.cos" ops/desk/deploy-step0.sh` → `73:RESIDENTS="com.cobalt.aset com.cobalt.radar com.cobalt.agent com.cobalt.cos"` · `grep -n -F "deploy-outage"` and `grep -n -F "deploy-step0"` on the hub → no output (the hub calls neither) · `git -C /Users/cobalt/cobalt log --oneline -1 bcbf08f9` → `bcbf08f9 docs(desk): F16 deploy FAILED at STEP-R cos, K5 hub-cos-restart drafter 868 R2068 R2069`.
- (viii) L32: this report holds no ticker, price or date of his; its values are labels, paths, commits and counts.

## OPEN
- O1 REJECTED: `DEPLOY-HUB.md:3` MODEL says "NO `launchctl` on any label but `com.cobalt.aset` / `com.cobalt.radar` / `com.cobalt.agent` and the labels of `<launchd set>`", while `:94` and `:123` call `launchctl print gui/501/com.cobalt.cos`. The allow string `Bash(launchctl print gui/501/*)` admits the call, so it is not refused. But the deploy session reads two rules that disagree, at STEP-R of the F16 relaunch. What would settle it: a ruling that `:3` gains `launchctl print` of `com.cobalt.cos` (text only, no allow string), or that the newer STEP-R line governs. Its test is in `## OWN FINDINGS`, ready to paste.
- O2 REJECTED: `:95` "P8 and D1 print `com.cobalt.aset` and `com.cobalt.radar` by name" no longer lists every named print (STEP-R and D1 now print cos). What would settle it: the same ruling as O1, with one text edit to `:95`.

## CONTINUE
next: none — the stop line is below.

## DECISIONS
- ASK DESK 1: stage-set printed `commits 2` and PREFLIGHT counted 3. bb5332c3 changes only `docs/` (the hub and the build report), so `":(exclude)docs"` leaves it out, and with it the DEPLOY-HUB.md diff. The house reads the whole hub at TIP under `files/wt/`. Default taken: continue; the count gap is explained by the pathspec (16:3x).
- ASK DESK 2: the stop line's `house B:` field offers `<name> <line>` or `none available`. Neither fits: Gemini was UP, and house B was not seated because the card says `HOUSE B: as needed`. Default taken: `house B: none (not needed)`, the PREFLIGHT wording (17:12).
- ASK DESK 3: §7 (iii) wants `git log --oneline bcbf08f9..HEAD -- tests/ops/test_desk_launch_launchd.py` empty. It lists 7d05ffe0 and d59fac71: the first cut edited the fenced test and the re-cut reverted it. The net diff is empty, so nothing of it ships. Default taken: not a WIDENED line and not a held finding (O6 NOT HELD); `ready:` is not lowered for it (17:12).
- O1 / O2 (REJECTED, OPEN; outside the card's rows, its fence keeps `:3` and BASE `:94`): the deploy hub at the tip forbids, in MODEL `:3`, the `launchctl print` of `com.cobalt.cos` that STEP-R `:94` and D1 `:123` run. `:95` lists aset and radar as the only labels printed by name. Default taken: shipped as the card wrote it. The allow string admits the print, and a session that stops on the conflict stops before any change (STEP-R and D1 precede the outage). Text to a later hub card, or a ruling that the newer line governs. Not a command string, so not R60's; not FOR DEJAN.

## RECORDS
- Grok (house A) produced `FINDINGS: 0` in a 12-byte `house-a.md`; its stdout: `I'll read the house instructions first and follow them exactly.The instructions say I write each finding before opening the next file. I'll start with the build report.The rows, the hub, and the tests line up. I’ll write the finding list./Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/hub-cos-restart-1019-check/house-a.md` `[exited with code 0]`. Started 16:34, finished by 16:44.
- No finding dropped. No house produced nothing. No `REFUSED, not needed` line. No `CONTINUED`. No lock take (DB: none).
- The L74 line is under `## L74`.
- Test O1 was added to `tests/ops/test_hub_cos_restart_1019.py`, run red, and removed again with Edit. `git status --short --branch` → `## ops/hub-cos-restart-1019` (clean) after.
- Not run: a separate `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` beside the gate. The gate's `--deploy-gate` leg ran `tests/ops` whole (`4073 passed, 1 xfailed`, log line 1021).
- The report and its `.result` are left for the desk to commit (no `git -C /Users/cobalt/cobalt add/commit` string is on this line).
- files opened: 13 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK`, `## E2`–`## W`), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), the worktree's `DEPLOY-HUB.md`, `tests/ops/test_hub_cos_restart_1019.py`, `tests/ops/test_hub_deferred_1018.py`, the build report, `house-a.md`, and four task outputs (house probe, Grok, gate offline, gate livenote).
- Check of `hub-cos-restart-1019`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: hub-cos-restart-1019 · pass: 1 · tip: d59fac71 · house A: Grok FINDINGS: 0 · findings: 6 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none (not needed) · suites: offline 8822/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 190519
