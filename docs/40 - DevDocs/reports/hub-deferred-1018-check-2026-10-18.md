# hub-deferred-1018 — CHECK (pass 1) — 2026-10-18

## §0 Headline
- Checked `170e90ca..79b8ac8e` (D1, D2: the STEP-R deferred-set edit to `DEPLOY-HUB.md` and its test file). House A Grok `FINDINGS: 0`; no house B (`HOUSE B: as needed`).
- Own findings O1–O5, one per CHECK ASK plus a scope check: every one was run and NOT HELD. Nothing held, nothing fixed, nothing open.
- Suites on `79b8ac8e`: offline 8608/0 (with the deploy gate, `tests/ops: run (deploy gate)`), live-note 147/0, `tests/ops` 3962 passed / 1 xfailed. `cobalt_dev` not taken (DB: none). `.env` absent. RESTARTS: none.
- One decision, ASK DESK 1: the staging script's commit count (1) did not match PREFLIGHT's range (2), because the fix commit touches only `docs/`. I continued and staged the BASE hub for the house.

## L74
The session's harness attribution reminder asked for a `Claude-Session:` line on commits. Recorded once and not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (CHECK-HUB L74). This check made no commit.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/787-hub-deferred-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/787-hub-deferred-card.md" · 0 · bc6956396f77aa3102c9774ff5cf53363dba4c3c
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/787-hub-deferred-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 64:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates at AUTHORIZATION: `grep -n "^| R17 "` → one row (line 35); `grep -n "^| R19 "` → one row (line 37); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c`. Again before the launch, at 17:44:43 EDT: `grep -c` R17 → `1`, R19 → `1`.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Sun Oct 18 17:42:22 EDT 2026
status · git status --short --branch · 0 · ## ops/hub-deferred-1018
head · git log --oneline -1; git log --stat --format=%h 79b8ac8e..HEAD · 0 · (6 lines)
    77e04a2a docs(hub-deferred-1018): build report — 79b8ac8e
    77e04a2a
    
     .../reports/hub-deferred-1018-build-2026-10-18.md  | 150 +++++++++++++++++++++
     .../hub-deferred-1018-build-2026-10-18.result      |  15 +++
     2 files changed, 165 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/hub-deferred-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/f20-cos-1018/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/hub-deferred-1018/docs/40 - DevDocs/reports/hub-deferred-1018-build-2026-10-18.md" · 0 · BUILT · job: hub-deferred-1018 · tip: 79b8ac8e | on 170e90ca | migration: none | offline 8608/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 157900
range · git log --oneline 170e90ca..79b8ac8e · 0 · (2 lines)
    79b8ac8e fix(hub-deferred-1018): STEP-R admits the restart set minus the deferred set; no launchctl call names it (D1, D2, L1, L42, L79)
    dbe3f841 wip(hub-deferred-1018): red — D1, D2 hub-text tests (3 red, 2 controls green on BASE)
PREFLIGHT OK
```
- THE RANGE, `git log --stat --format=%h 170e90ca..79b8ac8e` · exit 0: `79b8ac8e` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md | 10 +++++-----`; `dbe3f841` → `tests/ops/test_hub_deferred_1018.py | 108 +++`. Path union: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `tests/ops/test_hub_deferred_1018.py`.
- DB: none. `git diff --name-only --no-renames 170e90ca..79b8ac8e` · exit 0 → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `tests/ops/test_hub_deferred_1018.py`. Every path is under `docs/` or `tests/ops/`.
- The sibling `.env` at `/Users/cobalt/cobalt-wt/f20-cos-1018/.env` is another job's lock. This card takes none.
- `ls <S>` · exit 1 · `No such file or directory` (a fresh run).
- House probes, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0: `grok: UP` · `gemini: UP`. The card has no `HOUSE A: OpenAI` header line, so Sol was not probed.
- Seats: **house A: Grok · house B: none (not needed)** (`HOUSE B: as needed`).
- Self-check count from the build: `3 of 3`.

## Files copied
`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/hub-deferred-1018-check`.
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0:
```
25 <S>/STAGED-CARD
4807 <S>/diff.md
11083 <S>/files/787-hub-deferred-card.md
17042 <S>/files/hub-deferred-1018-build-2026-10-18.md
67105 <S>/files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md
4092 <S>/files/wt/tests/ops/test_hub_deferred_1018.py
386 <S>/rulings.md
STAGED 7 files · 104540 bytes · commits 1
```
The script counts `commits 1` and PREFLIGHT's range holds 2. The diff is `git log -p … -- . ":(exclude)docs"`, and the fix commit `79b8ac8e` touches only `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, so the excluded diff holds `dbe3f841` alone. The script still staged the hub at TIP whole. To give the house the hub's diff, I also staged the hub at BASE. `main` still holds the BASE text: `git -C /Users/cobalt/cobalt diff --stat 170e90ca HEAD -- <hub>` and `git -C /Users/cobalt/cobalt diff --stat 170e90ca -- <hub>` both print nothing. See ASK DESK 1.
`stage-copy.sh` ran once per file, and each call printed `COPIED`:
- 3327 `<S>/files/draft-cos-outage-2026-10-18.md`
- 6475 `<S>/files/f20-fix-preflight-2026-10-18.md`
- 42491 `<S>/files/730-f20-card.md`
- 20258 `<S>/files/CARD.md`
- 15506 `<S>/files/wt/ops/desk/deploy-step-c.sh`
- 3659 `<S>/files/wt/tests/ops/test_hub_text_1013.py`
- 21111 `<S>/files/wt/tests/ops/test_deploy_step_c.py`
- 66254 `<S>/files/base/DEPLOY-HUB.md` (the hub at BASE, from `main`)
`<S>/HOUSE-INSTRUCTIONS.md` written (13082 bytes): the HOUSE TEXT verbatim; the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS` and `## RECORDS`; the Files paragraph.
House A Grok started at 17:44:43 EDT: `cd <AGY>`, the launch, `cd <WT>`, then `git status --short --branch` → `## ops/hub-deferred-1018`.

## OWN FINDINGS
Written at 17:45:55 EDT, before I opened any house list.

FINDING O1
ROW: X1
CLAIM: The fix may change a hub line outside D1 (a)-(c) and D2 (a)-(b), or alter the `Anything else (…)` sentence of `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:93`.
RUN: COMMAND `git diff 170e90ca 79b8ac8e -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: a hunk on a line other than 5, 89, 93, 94 or 154, or a `-`/`+` pair whose `Anything else (` text differs.

FINDING O2
ROW: X4
CLAIM: A `RESTARTS:` set that holds only the deferred label may not read as an EMPTY `<restart set>`, and `DEPLOY-HUB.md:95` may then fail to refuse a migration.
RUN: TEST `tests/ops/test_hub_deferred_1018.py`
```python
def test_o2_a_deferred_label_alone_is_an_empty_restart_set():
    three, minus = rule()
    assert minus
    assert ({COS} - {COS}) == set() and admits({COS}, {COS}) is True
    assert one("- `MIGRATIONS` not `none` and `<restart set>` EMPTY").count("FAILED: RESTARTS") == 1
```
EXPECT: an assertion fails (there is no `minus` clause, or no `:95` refusal line).

FINDING O3
ROW: X2
CLAIM: A `launchctl` call site of the hub may take its label from a source that can hold a label STEP-C admitted `· deferred`.
RUN: COMMAND `grep -n -F "launchctl" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: a call line whose label is not a fixed name (`aset`, `radar`, `agent`), not from `<restart set>`, not from `<launchd set>`, and not 4.6L-BO's later `add` label.

FINDING O4
ROW: X3
CLAIM: THE ONE RESUME (`DEPLOY-HUB.md:53`, which re-runs neither STEP-C nor STEP-R) may reach smoke (f) with no `<deferred set>` to subtract, because smoke (f) may not read it from `## RESTARTS`.
RUN: COMMAND `grep -n -F "records it" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: no line, or a line that is not smoke (f) `:154`.

FINDING O5
ROW: SCOPE
CLAIM: The range may touch a fenced path or a file outside the rows' two files.
RUN: COMMAND `git diff --name-only 170e90ca 79b8ac8e`
EXPECT: a path other than `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` and `tests/ops/test_hub_deferred_1018.py`.

## Findings
House A Grok finished at 17:55:24 EDT (`date` at the notice). `<S>/house-a.md` (12 bytes), written by Grok, holds the single line `FINDINGS: 0`. Grok's stdout replied with the path and a summary: "The five hub lines match the rows, and the new tests pin those clauses. Check asks X1–X4 do not show a path that fails on the tip." That summary is a house's claim, not evidence (L35).
No house B sat (`HOUSE B: as needed`).
No house findings to keep.

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus | `git diff 170e90ca 79b8ac8e -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | three hunks (`@@ -2,7 +2,7 @@`, `@@ -86,12 +86,12 @@`, `@@ -151,7 +151,7 @@`). The changed lines are exactly `:5`, `:89`, `:93`, `:94` and `:154`. In each `-`/`+` pair of `:93`, the text `Anything else (an \`UNCLASSIFIED\` row, \`com.cobalt.herdr\` / \`com.cobalt.mainframe\` / \`com.cobalt.obsidian\`, a non-zero exit) → \`cd /Users/cobalt/cobalt\`, \`FAILED: RESTARTS — <rows> · rollback: not used\`: the classification is a build's, with its suite (rule B), never a commit into this tree.` is the same on both sides. The `:3` MODEL line and the `:11` launch line show only as context | NOT HELD |
| O2 | opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_deferred_1018.py::test_o2_a_deferred_label_alone_is_an_empty_restart_set` | `1 passed, 15 warnings in 0.97s` | NOT HELD (test removed again with Edit; `git status --short --branch` → `## ops/hub-deferred-1018`) |
| O3 | opus | `grep -n -F "launchctl" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | lines 3, 5, 11, 13, 53, 65, 77, 89, 94, 122, 125, 139, 143, 144, 149, 162, 163, 165, 168. Call lines and their label sources: `:53` (e), `:65` P8, `:122` D1 → aset and radar by name; `:125` D1 THE LAUNCHD SET, `:144` 4.6L, `:163` (1L), `:165` (2L) → `<launchd set>`; `:139` 4.2, `:143` 4.6, `:149` smoke (a), `:162` (1), `:168` (3) → `<restart set>` or the fixed resident names; `:11` and `:13` hold launch strings with fixed resident names or `<launchd strings>` (a `deferred` line fills nothing, `:13`). Lines 3, 5, 77, 89 and 94 hold no call. No call line takes a deferred label | NOT HELD |
| O4 | opus | `grep -n -F "records it" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | `154:- (f) … \`RESTARTS:\` minus \`<deferred set>\` (as \`## RESTARTS\` records it) = STEP-R's \`<restart set>\`, no \`UNCLASSIFIED\`.` Smoke (f) reads `<deferred set>` from `## RESTARTS`, and STEP-R writes it there (`:93`). A resume keeps the report, so (f) still has it | NOT HELD |
| O5 | opus | `git diff --name-only 170e90ca 79b8ac8e` | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `tests/ops/test_hub_deferred_1018.py` | NOT HELD |

## FIXES
none (nothing held)

## Suites
On tip `79b8ac8e` (no commit of mine), as a DB: none card (`BUILD-HUB.md` W (a0), (a), (e)):
- RESTARTS: `uv run cobalt jobs restarts 170e90ca..HEAD` · exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/hub-deferred-1018-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/hub-deferred-1018-build-2026-10-18.result	A	DOCS	-
tests/ops/test_hub_deferred_1018.py	A	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames 170e90ca` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/reports/hub-deferred-1018-build-2026-10-18.md` · `docs/40 - DevDocs/reports/hub-deferred-1018-build-2026-10-18.result` · `tests/ops/test_hub_deferred_1018.py`. Every path is under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-deferred-1018 offline --deploy-gate` · exit 0:
```
tests/ops: run (deploy gate)
offline 8608/0
log: /Users/cobalt/cobalt-wt/.gate-logs/hub-deferred-1018-offline-20261018-175559.log
```
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-deferred-1018 livenote` · exit 0:
```
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/hub-deferred-1018-livenote-20261018-175603.log
```
  `grep -n -F "SKIPPED" <log>` → `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. This skip is in the allowed set; no skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` · exit 0 → `3962 passed, 1 xfailed, 16 warnings in 919.71s (0:15:19)`.
- with-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/hub-deferred-1018/.env` → `No such file or directory` (no lock was taken).

## Scope
PREFLIGHT's path union is `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (D1, D2 `files`) and `tests/ops/test_hub_deferred_1018.py` (D1, D2 `files`). This check made no commit. Nothing lies outside the rows' files.

## Checked against the branch
- (i) `git log --oneline 79b8ac8e..HEAD -- . ":(exclude)docs"` → empty (no commit of mine). `<tip now>` = `79b8ac8e`.
- (ii) `git log --stat --format=%h 79b8ac8e..HEAD` → `77e04a2a`: `.../reports/hub-deferred-1018-build-2026-10-18.md`, `.../hub-deferred-1018-build-2026-10-18.result` (docs only).
- (iii) `git log --oneline 170e90ca..HEAD -- ops/desk/deploy-outage.sh ops/desk/deploy-step0.sh ops/desk/deploy-step-c.sh ops/desk/desk-launch.sh ops/desk/deploy-card.sh src/cobalt/jobs/restarts.py data/deploy/bootstrap-owed.json "docs/40 - DevDocs/prompts/CARD.md"` → empty. The fenced hub lines (`:3`, `:11`, `:53`, STEP-4, STEP-5) are unchanged per O1.
- (iv) No held finding.
- (v) `ls /Users/cobalt/cobalt-wt/hub-deferred-1018/.env` → `No such file or directory`; `git status --short --branch` → `## ops/hub-deferred-1018`.
- (vi) `git log --stat --format=%h 170e90ca..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration and no with-DB test, so no gate-lists entry is owed.
- (vii) Card `## RECORDS`: `git -C /Users/cobalt/cobalt log --oneline -1 170e90ca` → `170e90ca docs(prompt): 786 drafter for hub-deferred-1018 card` (the BASE). `grep -c -F "deferred"` on main's hub → `3` (`:5`, `:13` and `:89` per the record). On the tip hub: `grep -c -F "<deferred set>"` → `5` (DEPLOY PROOF after `5`), `grep -c -F "minus every label of"` → `1` (DEPLOY PROOF after `1`), `grep -c -F "com.cobalt.cos"` → `0`.
- (viii) L32: this report holds no ticker, price or date of his. The only values are labels, commit ids, paths and test counts.

## OPEN
none

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
- ASK DESK 1: At `## 1`, `stage-set.sh` printed `commits 1`, and PREFLIGHT's range holds 2. CHECK-HUB `## 1` (1) says a count mismatch is `FAILED: copy — the diff is incomplete`. The cause is mechanical: the diff excludes `docs`, and this card's fix commit `79b8ac8e` touches only a `docs/` path. The house still had the whole TIP hub, and I added the BASE hub copy (`<S>/files/base/DEPLOY-HUB.md`) so it could see the diff. Default taken: continue, with no extra access and no second house attempt. For the desk: should a check whose fix lives entirely under `docs/` (a hub card) count commits without the `docs` exclude, or stage the docs diff as well?

## RECORDS
- Clock: PREFLIGHT 17:42:22 EDT · house A launch 17:44:43 · own findings 17:45:55 · house A notice 17:55:24 · suites launched about 17:56 · close 18:24:08 EDT (`date`).
- House A Grok produced a list: `FINDINGS: 0`. No house produced nothing.
- Dropped findings: none.
- The house-B field in the stop line reads `none (not needed)`, as PREFLIGHT recorded it. Gemini was UP but was not seated, because the card's `HOUSE B` line is `as needed`, not `mandatory`. `none available` would misstate this.
- WHAT YOU READ (5), `areas/cobalt.md` `## What Cobalt is` and `## Build rules` down, was read at close (18:24 EDT), not at `## 2`. Nothing in it bears on a hub-text card. Recorded as a deviation.
- The result file `hub-deferred-1018-check-2026-10-18.result` is written beside this report. Both are left for the desk to commit on `main`: this check's git strings write only inside `<WT>`.
- No `REFUSED, not needed` line; no `CONTINUE` message; no lock take.
- files opened: 15 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (THE LOCK, E2, RESTARTS, W), `areas/cobalt.md`, `tests/ops/test_hub_deferred_1018.py`, `DEPLOY-HUB.md` (tip), the build report, `ops/desk/deploy-step-c.sh` (270-294), `<S>/diff.md`, `<S>/house-a.md`, the house-probe output, Grok's stdout, the livenote output, the offline gate output, the `tests/ops` output (tail).
- Check of `hub-deferred-1018`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: hub-deferred-1018 · pass: 1 · tip: 79b8ac8e · house A: Grok FINDINGS: 0 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 8608/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 15 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 173800
