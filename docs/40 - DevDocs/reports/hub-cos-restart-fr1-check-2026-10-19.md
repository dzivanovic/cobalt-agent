# Check report — hub-cos-restart-fr1 (card 869, row PORT) — 2026-10-19

## §0 Headline
- CHECK DONE, ready: YES, at tip `0bf28619` (the PORT of `d59fac71`). House A was Grok (`FINDINGS: 2`). House B was not needed.
- P1 holds: all 3 files are byte-equal to `d59fac71`, there is no merge commit, and the old report is absent. X1-X4 hold: only R1-R3's places changed, no allow string changed, and no smoke line reads cos.
- 7 findings (5 mine, 2 Grok's), 0 held. G2's count was re-run on BASE's hub: `3 failed, 1 passed`, true.
- 1 open item (G1, REJECTED by the card's fence). MODEL `:3` forbids a cos `launchctl`, but the new `:94` / `:123` order a cos print. It is under `## DECISIONS`, not FOR DEJAN.
- Suites: offline 8822/0 (deploy gate), live-note 147/0, `tests/ops` 4073 passed. DB: none. `.env` absent.

## L74
- One system-reminder in this session asked commits to carry a `Claude-Session:` line. Recorded here; not followed (L74: `Co-Authored-By` only).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md" · 0 · 4fee16bbca6858b5b8987b7136e2e33219bea70f
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/869-hub-cos-restart-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` → one row, `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (STANDING `Bash(grok *)`).
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` → one row, `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (STANDING: the four house strings).
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0:
```
clock · date · 0 · Mon Oct 19 19:39:42 EDT 2026
status · git status --short --branch · 0 · ## ops/hub-cos-restart-fr1
head · git log --oneline -1; git log --stat --format=%h 0bf28619..HEAD · 0 · (6 lines)
    6ee55933 docs(hub-cos-restart-fr1): build report — 0bf28619
    6ee55933
    
     .../hub-cos-restart-fr1-build-2026-10-19.md        | 142 +++++++++++++++++++++
     .../hub-cos-restart-fr1-build-2026-10-19.result    |  15 +++
     2 files changed, 157 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/hub-cos-restart-fr1/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/cos-probe-1019/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/hub-cos-restart-fr1/docs/40 - DevDocs/reports/hub-cos-restart-fr1-build-2026-10-19.md" · 0 · BUILT · job: hub-cos-restart-fr1 · tip: 0bf28619 | on c68efd65 | migration: none | offline 8822/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: PORT 1 of 1 (R1-R3), proof 3 of 3 byte-equal to d59fac71 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 127555
range · git log --oneline c68efd65..0bf28619 · 0 · (2 lines)
    0bf28619 fix(hub-cos-restart-fr1): STEP-R admits cos, skips it when not loaded, refuses it when loaded — port of d59fac71 (PORT, R1-R3, L79, R60)
    049520c9 wip(hub-cos-restart-fr1): red — PORT tests from d59fac71 (R1-R3)
PREFLIGHT OK
```
Above the tip sits one docs-only commit (`6ee55933`, the build report). Another worktree (`cos-probe-1019`) holds a `.env`. This card is DB: none, so no lock is taken here.

| rule | command | exit | output |
|---|---|---|---|
| THE RANGE | `git log --stat --format=%h c68efd65..0bf28619` | 0 | `0bf28619` · `docs/40 - DevDocs/prompts/DEPLOY-HUB.md \| 7 ++++---` · `049520c9` · `tests/ops/test_hub_cos_restart_1019.py \| 93 +++…` · `tests/ops/test_hub_deferred_1018.py \| 4 +-` |
| DB: none | `git diff --name-only --no-renames c68efd65..0bf28619` | 0 | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `tests/ops/test_hub_cos_restart_1019.py` · `tests/ops/test_hub_deferred_1018.py`. Every path is under `docs/` or `tests/ops/` |
| scratch | `ls <S>` | 1 | `No such file or directory`. Fresh run |
| house probe | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` | 0 | `grok: UP` · `gemini: UP` |
| seats | SEAT ORDER, no header line | — | house A: Grok · house B: none (not needed; `HOUSE B: as needed`) |

Path union for `## Scope`: the three paths above.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → exit 0:
```
28 <S>/STAGED-CARD
5261 <S>/diff.md
21134 <S>/files/869-hub-cos-restart-card.md
17867 <S>/files/hub-cos-restart-fr1-build-2026-10-19.md
68316 <S>/files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md
3534 <S>/files/wt/tests/ops/test_hub_cos_restart_1019.py
4102 <S>/files/wt/tests/ops/test_hub_deferred_1018.py
386 <S>/rulings.md
STAGED 8 files · 120628 bytes · commits 1
```
`commits 1` against PREFLIGHT's 2: the staged diff is the fixed `git log -p c68efd65..0bf28619 -- . ":(exclude)docs"`. `git log --oneline c68efd65..0bf28619 -- . ":(exclude)docs"` → `049520c9` alone. The other commit (`0bf28619`) touches only `DEPLOY-HUB.md` under `docs/`. So the count matches the staged command. The hub diff that `diff.md` leaves out was written by me to `<S>/diff-hub.md`, from `git diff c68efd65..0bf28619` (quoted in this session), and named in the instructions. The whole hub at the tip is also staged.
`stage-copy.sh`, one call each (the files the card's `## READ` names):
- `COPIED 10940 <S>/files/deploy-f16-close-fr2.md`
- `COPIED 154247 <S>/files/wt/ops/desk/desk-launch.sh`
- `COPIED 15452 <S>/files/wt/ops/desk/deploy-outage.sh`
- `COPIED 12334 <S>/files/wt/ops/desk/orphan-clean.sh`
- `COPIED 39628 <S>/files/wt/src/cobalt/heartbeat/probes.py`
- `COPIED 4207 <S>/files/wt/tests/ops/test_deploy_smoke_string_1014.py`
- `COPIED 25642 <S>/files/wt/configs/cobalt/jobs.yaml`. A row names it (`:206-214`); copied for X4.
Written: `<S>/HOUSE-INSTRUCTIONS.md`, the HOUSE TEXT verbatim, then the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS` and `## RECORDS` whole, then the Files paragraph.
`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/hub-cos-restart-fr1-check`.
House launch: `date` → `Mon Oct 19 19:42:43 EDT 2026`. Both house gates were re-run, each one row (R17 `:35`, R19 `:37`), and the `-S` log returned `5055151d…`. `ls -la <S>` → 6 entries. `cd <AGY>`, then Grok started in the background (task `bst6t81x5`). `cd <WT>`, then `git status --short --branch` → `## ops/hub-cos-restart-fr1`. House B: none (not needed).

## OWN FINDINGS
Written before any house list was opened. Read: the hub at the tip, `:50-99` and `:113-174`; the diff `c68efd65..0bf28619`, whole; both test files, through the diff; the build report; `cobalt.md` (the boundaries, and from `## Build rules` down); BUILD-HUB `## THE LOCK`, `## E2`, `## RESTARTS`, `## W`.

FINDING O1
ROW: PORT (P1)
CLAIM: The builder's PROOF line (`hub-cos-restart-fr1-build-2026-10-19.md:122`) is false for at least one of the three ported files: one of them differs from `d59fac71` at the tip.
RUN: COMMAND `git diff d59fac71 0bf28619 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" tests/ops/test_hub_cos_restart_1019.py tests/ops/test_hub_deferred_1018.py`
EXPECT: some diff output (a defect); empty output means the PROOF holds.

FINDING O2
ROW: PORT (P1)
CLAIM: The branch holds a merge commit, or the old build report `hub-cos-restart-1019-build-2026-10-19.md` was ported into the range.
RUN: COMMAND `git log --merges --oneline c68efd65..HEAD`, and `git diff --name-only c68efd65 HEAD`
EXPECT: a merge line, or the old report's path (a defect).

FINDING O3
ROW: X1
CLAIM: `DEPLOY-HUB.md` changes outside R1-R3's places (`:93`, the new `:94`, `:123`, `:155`), or the `Anything else (…)` sentence of `:93` is not byte-equal.
RUN: COMMAND `git diff --word-diff=porcelain c68efd65 0bf28619 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: a changed word outside the span `com.cobalt.cos`, the `(any of the four …)` parenthesis, the new NOT LOADED line, D1's cos clause and smoke (f)'s `and minus a label …` clause (a defect).

FINDING O4
ROW: X3
CLAIM: An allow string or one of its pins changed in the range: `ops/desk/`, `STANDING-LIST.md`, `test_deploy_smoke_string_1014.py` or `test_desk_launch_launchd.py`.
RUN: COMMAND `git diff c68efd65 HEAD -- ops/desk/ "docs/40 - DevDocs/prompts/STANDING-LIST.md" tests/ops/test_deploy_smoke_string_1014.py tests/ops/test_desk_launch_launchd.py`
EXPECT: any output (a defect).

FINDING O5
ROW: X2 / X4
CLAIM: A hub line outside STEP-R `:94` and D1 `:123` names `com.cobalt.cos`: a STEP-4 / STEP-5 / smoke `launchctl` call, or a smoke (e) cos read.
RUN: COMMAND `grep -n -F "com.cobalt.cos" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: a hit on a line other than `93`, `94`, `123` (a defect).

Read, no finding: the D1 clause `com.cobalt.cos in <restart set>: … <cos pid>` (`DEPLOY-HUB.md:123`) is unreachable text. `:94` takes cos out of `<restart set>` when it is not loaded, and stops the run when it is loaded. R2 (b) wrote the clause on purpose. It is harmless and the card names it.

## Findings
House A Grok finished at `date` → `Mon Oct 19 19:53:14 EDT 2026` (task `bst6t81x5`, exit 0). It wrote `<S>/house-a.md` (2371 bytes) and printed its path. Its last line is `FINDINGS: 2`. House B: none (not needed). The drop rule: both blocks carry a `RUN:` line followed by a test function or a command with an allowed start, so both are kept.

| id | house | row | claim | run |
|---|---|---|---|---|
| G1 | Grok | X2 | `:94` and `:123` order `launchctl print gui/501/com.cobalt.cos`, which MODEL `:3` forbids. If that print is skipped, a loaded cos is never stopped and 4.2 never names it | TEST |
| G2 | Grok | R3 | R3's required BASE quote of the new file (`3 failed, 1 passed`) is stated in the build report at `:71` with no command and no output | COMMAND |

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `git diff d59fac71 0bf28619 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" tests/ops/test_hub_cos_restart_1019.py tests/ops/test_hub_deferred_1018.py` | (empty). All 3 files are byte-equal to `d59fac71` | NOT HELD |
| O2 | own | `git log --merges --oneline c68efd65..HEAD` · `git diff --name-only c68efd65 HEAD` | (empty) · `DEPLOY-HUB.md`, `hub-cos-restart-fr1-build-2026-10-19.md`, `.result`, `test_hub_cos_restart_1019.py`, `test_hub_deferred_1018.py`. No merge commit, and the old `hub-cos-restart-1019-build-…` report is absent | NOT HELD |
| O3 | own | `git diff --word-diff=porcelain c68efd65 0bf28619 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | Changed words: `+com.cobalt.cos`; `-(one, two, all three,` → `+(any of the four,`; `-none)` → `+none; \`com.cobalt.cos\` then passes NOT LOADED below)`; the `+- NOT LOADED …` line; D1's `+\`com.cobalt.cos\` in \`<restart set>\`: … recuts\`;`; smoke (f)'s `+and minus a label … skipped\`` and `-it)` → `+them)`. The `Anything else (…)` sentence is an unchanged context run. Only R1-R3's places changed (X1) | NOT HELD |
| O4 | own | `git diff c68efd65 HEAD -- ops/desk/ "docs/40 - DevDocs/prompts/STANDING-LIST.md" tests/ops/test_deploy_smoke_string_1014.py tests/ops/test_desk_launch_launchd.py` | (empty). The `claude --bg` line `:11` sits outside every hunk (O3), so no allow string changed (X3) | NOT HELD |
| O5 | own | `grep -n -F "com.cobalt.cos" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | Hits on `93:`, `94:` and `123:` only. No STEP-4, STEP-5 or smoke line names cos, so smoke (e) gains no cos read (X2, X4) | NOT HELD |
| G1 | Grok | `test_x2_loaded_cos_reaches_step4_when_the_print_is_forbidden` pasted unchanged into `tests/ops/test_hub_cos_restart_1019.py`. `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_cos_restart_1019.py::test_x2_loaded_cos_reaches_step4_when_the_print_is_forbidden` | `1 failed, 15 warnings in 0.96s`. First line: `tests/ops/test_hub_cos_restart_1019.py:103: AssertionError: NOT LOADED orders launchctl print gui/501/com.cobalt.cos, MODEL names no com.cobalt.cos, and 4.2 bootout names no com.cobalt.cos` / `assert not (True and True and True)` | REJECTED — card R3 "No `launchctl` string for cos is added anywhere: `:3`, `:11`, … stand" and `## NOT IN THIS JOB` "MODEL `:3` … stand". Red for its stated reason: `:3` reads "NO `launchctl` on any label but `com.cobalt.aset` / `com.cobalt.radar` / `com.cobalt.agent` and the labels of `<launchd set>`", and `:94` / `:123` order a cos `launchctl print`. The only fix is a change to `:3`, which the card fences. The consequence Grok names (a loaded cos reaching STEP-4) needs a deploy session that skips the print, and no run can show that. Test removed again with the Edit tool; it stays OPEN |
| G2 | Grok | `grep -n -F -e "3 failed, 1 passed" -e "uv run pytest -q -p no:cacheprovider tests/ops/test_hub_cos_restart_1019.py" "docs/40 - DevDocs/reports/hub-cos-restart-fr1-build-2026-10-19.md"`. Then, to settle the number (L70): BASE's four places were put back into the tip's hub with the Edit tool (`git diff --stat c68efd65 -- DEPLOY-HUB.md` → empty), and `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_hub_cos_restart_1019.py` was run. The tip's text was restored with the Edit tool (`git status --short --branch` → `## ops/hub-cos-restart-fr1` alone; `git diff --stat 0bf28619` → the build report's two files only) | The grep prints exactly Grok's EXPECT: `71:New file alone: 3 failed, 1 passed, as the card's R3 states.`, `77:`, `111:` (both `4 passed`). The BASE run: `F.FF` · `3 failed, 1 passed, 15 warnings in 0.84s`. Failed: `test_r1_…` (`:54: assert False is True … admits({'com.cobalt.aset', 'com.cobalt.cos', 'com.cobalt.radar'})`), `test_r2_…` (`:71: no \`- NOT LOADED\` line`), `test_c3_…` (`:90: no \`- NOT LOADED\` line`). Passed: `test_c1_…` | NOT HELD — the form gap is real: the report states the BASE count without quoting that command's output. The count is true, though: my run on BASE's hub prints `3 failed, 1 passed`, each red for its row's reason, and the control passes. The report also quoted the two-file BASE run whole at `:65`. Nothing in the rows' files is wrong |

No finding held, so there is no `wip(hub-cos-restart-fr1): check red` commit.

## FIXES
none (held: 0)

## Suites
The tip is the build's `0bf28619` (no commit of mine). The card is DB: none, so W runs (a0), (a) and (e), with `--deploy-gate` added to the offline call.
- RESTARTS: `uv run cobalt jobs restarts c68efd65..HEAD` → `DEPLOY-HUB.md M DOCS -` · `hub-cos-restart-fr1-build-2026-10-19.md A DOCS -` · `….result A DOCS -` · `tests/ops/test_hub_cos_restart_1019.py A test/documentation; no resident -` · `tests/ops/test_hub_deferred_1018.py M test/documentation; no resident -` · `RESTARTS: none`. No UNCLASSIFIED row.
- (a0) `git diff --name-only --no-renames c68efd65` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/reports/hub-cos-restart-fr1-build-2026-10-19.md` · `docs/40 - DevDocs/reports/hub-cos-restart-fr1-build-2026-10-19.result` · `tests/ops/test_hub_cos_restart_1019.py` · `tests/ops/test_hub_deferred_1018.py`. Every path is under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 5 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-cos-restart-fr1 offline --deploy-gate` → exit 0:
  ```
  tests/ops: run (deploy gate)
  offline 8822/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/hub-cos-restart-fr1-offline-20261019-195508.log
  ```
  In the log: `947:4749 passed, 871 skipped, 4 xfailed, 36 warnings in 765.63s (0:12:45)` · `1021:4073 passed, 1 xfailed, 16 warnings in 905.75s (0:15:05)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-cos-restart-fr1 livenote` → exit 0: `live-note 147/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/hub-cos-restart-fr1-livenote-20261019-195509.log`. Its one SKIPPED line, `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, does not name `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `4073 passed, 1 xfailed, 16 warnings in 922.31s (0:15:22)`.
- `cobalt_dev`: not taken (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/hub-cos-restart-fr1/.env` → `No such file or directory` (before W and after).
- New tests in this check: none committed. Nothing held, so there was no red to show.

## Scope
PREFLIGHT's path union, `c68efd65..0bf28619`: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (R1-R3), `tests/ops/test_hub_cos_restart_1019.py` (R1-R3) and `tests/ops/test_hub_deferred_1018.py` (R1). Each path sits in a row's `files`. My commits: none. Above the tip: the build report only (docs).

## Checked against the branch
- (i) `git log --oneline 0bf28619..HEAD -- . ":(exclude)docs"` → (empty). No commits of mine. `<tip now>` = `0bf28619`.
- (ii) `git log --stat --format=%h 0bf28619..HEAD` → `6ee55933` only, touching `.../hub-cos-restart-fr1-build-2026-10-19.md` and `.result` (docs). No non-docs path, so no WIDENED line.
- (iii) Each fenced path, in one call: `git log --oneline c68efd65..HEAD -- ops/desk/desk-launch.sh ops/desk/deploy-step-c.sh ops/desk/deploy-step0.sh ops/desk/deploy-outage.sh ops/desk/orphan-clean.sh ops/desk/deploy-card.sh src/cobalt/jobs/restarts.py configs/cobalt/jobs.yaml ops/com.cobalt.cos.plist "docs/40 - DevDocs/prompts/CARD.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md" tests/ops/test_deploy_smoke_string_1014.py tests/ops/test_desk_launch_launchd.py` → (empty). The fenced lines of `DEPLOY-HUB.md` are untouched (O3, the word diff).
- (iv) No HELD finding, so there is no test to grep.
- (v) `ls /Users/cobalt/cobalt-wt/hub-cos-restart-fr1/.env` → `No such file or directory`. `git status --short --branch` → `## ops/hub-cos-restart-fr1` alone.
- (vi) `git log --stat --format=%h c68efd65..HEAD -- src/cobalt/db_migrations tests/cobalt` → (empty). No migration and no with-DB test, so `gate-lists.md` is not needed.
- (vii) The card's `## RECORDS` name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command (their commands are `rev-parse`, `show` and `git grep`, none of them on my list). I ran the card's `## DEPLOY PROOF` markers on the worktree hub instead: `grep -c -F "com.cobalt.cos: not loaded — skipped" …` → `2` · `grep -c -F "com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60)" …` → `1` · `grep -c -F "launchctl kickstart -k gui/501/com.cobalt.cos" …` → `0`. These are the card's `after` values, 2 / 1 / 0.
- (viii) L32: this report holds no ticker, price or date of his. The test values are constructed labels.

## OPEN
- G1 (Grok, X2): REJECTED, FOLLOW-UP. MODEL `DEPLOY-HUB.md:3` says "NO `launchctl` on any label but `com.cobalt.aset` / `com.cobalt.radar` / `com.cobalt.agent` and the labels of `<launchd set>`". R2's `:94` (NOT LOADED) and `:123` (D1) order `launchctl print gui/501/com.cobalt.cos`. The hub text contradicts itself. The test is red for this reason (`## RUNS`). The fix is a clause in `:3` (for example "and the `launchctl print` of `com.cobalt.cos` at STEP-R NOT LOADED and D1"). The card fences `:3` and R3 rules it stands, so this check does not change it. The allow string `Bash(launchctl print gui/501/*)` already admits the print. What would settle it: a ruling that the specific step (`:94`) governs over MODEL `:3` for this read-only print, or a fix-round line in `:3`.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
- G1: MODEL `:3` forbids a `launchctl` call on cos, but the new STEP-R NOT LOADED (`:94`) and D1 (`:123`) order a cos `launchctl print`. This lies outside the card's rows (`:3` is fenced), and every deploy of this hub reads both lines. Safe default taken: no change. Verdict REJECTED, and it stays OPEN for the builder's ONE fix round or a desk ruling (a `SETTLED: G1 — R<n>`). The print is read-only and on the allow list, and a session that refuses it stops loud (L1): neither branch of `:94` lets a loaded cos go on past STEP-R. Not FOR DEJAN: `:3` is a prose rule, not an allow string (R60).

## RECORDS
- L74: one system-reminder in this session asked for a `Claude-Session:` line on commits. Not followed. This check made no commit.
- Dropped findings: none.
- Every house produced a list: Grok `FINDINGS: 2`. House B: none (not needed; `HOUSE B: as needed`, and the probe showed `gemini: UP`).
- `REFUSED, not needed`: none. `CONTINUED`: none. Extra lock takes: none (DB: none).
- Staging: `stage-set.sh` printed `commits 1` against PREFLIGHT's 2. This is explained under `## Files copied`: the fixed diff excludes `docs/`. I wrote `<S>/diff-hub.md` so a house could read the hub diff.
- G2's BASE run edited the tip's `DEPLOY-HUB.md` back to BASE's four places for one test run, then restored it with the Edit tool. `git diff --stat c68efd65 -- DEPLOY-HUB.md` → empty during the run. Afterwards `git status --short --branch` → clean and `git diff --stat 0bf28619` → the build report only. G1's pasted test was removed the same way. The tree at the stop line is the build's tip, unchanged.
- The report is on `main` at `docs/40 - DevDocs/reports/`. The desk commits it with its `.result` file (LAUNCH). My list has no `git -C /Users/cobalt/cobalt add/commit` string.
- Session id `d83e98e0-3a9b-43ba-8786-da0f7941d724`. `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh d83e98e0-3a9b-43ba-8786-da0f7941d724` → `context 200556 of 400000 — ok` (read at 20:23).
- files opened: 10. `CHECK-HUB.md`, card 869, `BUILD-HUB.md` (`## THE LOCK` to `## W`), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), the build report, `DEPLOY-HUB.md` (tip), `tests/ops/test_hub_cos_restart_1019.py`, `<S>/diff.md` (head), `<S>/rulings.md`, `<S>/house-a.md`.
- Check of `hub-cos-restart-fr1`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: hub-cos-restart-fr1 · pass: 1 · tip: 0bf28619 · house A: Grok FINDINGS: 2 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8822/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 200556
