# cos-outage-1018 — CHECK (pass 1) — 2026-10-18

## §0 Headline
- Check of K1 and K2 at tip `de3e15c8`: house A Grok `FINDINGS: 0`; house B none (card `HOUSE B: as needed`).
- My own findings: O1 and O2 test the X3 entry paths the build left unpinned (the trap, and the `Bootstrap failed: 5` retry for cos). Both passed on the tip: NOT HELD. Every cos bootstrap uses `$REPO/ops/com.cobalt.cos.plist`.
- X1 and X2 hold: only the K1 and K2 lines changed, and no existing test was edited. Held 0, fixed 0, open 0. I made no commit.
- Suites on `de3e15c8`: offline 8612/0 (tests/ops run, deploy gate) · live-note 147/0 · `tests/ops` 3966 passed · `cobalt_dev` not taken (DB: none) · `.env` absent · RESTARTS: none.

## L74
- A system reminder in this session asks for a `Claude-Session:` line on commits. Per L74 and CHECK-HUB UNATTENDED RULES, recorded here once and not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/784-cos-outage-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/784-cos-outage-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/784-cos-outage-card.md" · 0 · 454a23083ccacc45dcf7032c241aef0b13046009
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/784-cos-outage-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 65:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → line 35, one row (`Bash(grok *)` PRE-APPROVED, standing); `grep -n "^| R19 "` → line 37, one row (four house strings pre-approved indefinitely); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Sun Oct 18 17:48:10 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/cos-outage-1018
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a routed card)
head · git log --oneline -1; git log --stat --format=%h de3e15c8..HEAD · 0 · (6 lines)
    b5d62f17 docs(cos-outage-1018): build report — de3e15c8
    b5d62f17
    
     .../reports/cos-outage-1018-build-2026-10-18.md    | 169 +++++++++++++++++++++
     .../cos-outage-1018-build-2026-10-18.result        |  15 ++
     2 files changed, 184 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/cos-outage-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/f20-cos-1018/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/cos-outage-1018/docs/40 - DevDocs/reports/cos-outage-1018-build-2026-10-18.md" · 0 · BUILT · job: cos-outage-1018 · tip: de3e15c8 | on 0bdb7089 | migration: none | offline 8612/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 2 of 3 | decisions: 2 · for Dejan: 0 · tokens: 167789
report: self-check 2 of 3 (recorded)
range · git log --oneline 0bdb7089..de3e15c8 · 0 · (2 lines)
    de3e15c8 feat(cos-outage-1018): rows
    1b11f128 wip(cos-outage-1018): red
PREFLIGHT OK
```
- `?? SHADOW-INSTRUCTIONS.md`: routed card (BAND LOW), expected and recorded, not a finding.
- self-check `2 of 3`: recorded; passed to the house as a fact (it is in the build report the house reads).
- THE RANGE, `git log --stat --format=%h 0bdb7089..de3e15c8`:
```
de3e15c8
 ops/desk/deploy-outage.sh | 11 ++++++-----
 ops/desk/deploy-step0.sh  |  4 ++--
 2 files changed, 8 insertions(+), 7 deletions(-)
1b11f128
 tests/ops/test_deploy_outage.py | 116 ++++++++++++++++++++++++++++++++++++++++
 tests/ops/test_deploy_step0.py  | 108 +++++++++++++++++++++++++++++++++++++
 2 files changed, 224 insertions(+)
```
  Path union: `ops/desk/deploy-outage.sh`, `ops/desk/deploy-step0.sh`, `tests/ops/test_deploy_outage.py`, `tests/ops/test_deploy_step0.py`.
- DB: none — `git diff --name-only --no-renames 0bdb7089..de3e15c8` → the four paths above, all under `ops/` or `tests/ops/`.
- `ls <S>` → `No such file or directory` (fresh).
- House probe `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0: `grok: UP` · `gemini: UP`.
- house A: Grok · house B: none (not needed) — card `HOUSE B: as needed`, no `HOUSE A:` header line.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`:
```
23 <S>/STAGED-CARD
15054 <S>/diff.md
11269 <S>/files/784-cos-outage-card.md
19457 <S>/files/cos-outage-1018-build-2026-10-18.md
15452 <S>/files/wt/ops/desk/deploy-outage.sh
46221 <S>/files/wt/ops/desk/deploy-step0.sh
24912 <S>/files/wt/tests/ops/test_deploy_outage.py
49801 <S>/files/wt/tests/ops/test_deploy_step0.py
386 <S>/rulings.md
STAGED 9 files · 182575 bytes · commits 2
```
`stage-copy.sh`: `COPIED 42491 <S>/files/730-f20-card.md` (READ: row C4a, D8) · `COPIED 6475 <S>/files/f20-fix-preflight-2026-10-18.md` (ROWS scope).

## OWN FINDINGS
Written before either house's list was opened. Read: CHECK-HUB, BUILD-HUB `## THE LOCK` `## E2` `## RESTARTS` `## W`, the card, `git diff 0bdb7089..de3e15c8` (scripts and tests), `ops/desk/deploy-outage.sh` at the tip whole and at BASE (`git show`), `ops/desk/deploy-step0.sh` `:96-127`, `:860-909`, `tests/ops/test_deploy_outage.py:1-300`, `tests/ops/test_deploy_step0.py:210-239`, the build report whole, `areas/cobalt.md` `## What Cobalt is` and from `## Build rules` down, 730 card C4a and D8 by grep.

Reading notes (not findings): X1 — `git diff 0bdb7089..de3e15c8 -- ops/desk` holds exactly K1 (a) `:90`, (b) `:91`, (c) `:109`, (d) `:4`, `:11`, `:13` and K2 (a) `:73`, (b) `:41`; each line with the label holds it once. X2 — `git diff 0bdb7089..de3e15c8 -- tests/ops` is additions only (one `import textwrap`, the K1/K2 blocks): no existing test edited. X3 — `plist_of` (`deploy-outage.sh:105-111`) is the only source of a cos plist path; its callers are the dry run `:141`, rule E `:237`, `up_one` `:285` (step 2 `:410`, step 3 `:426`, the trap `:335`). The builder's tests pin the dry run, rule E and step 2 for cos; the trap and the `Bootstrap failed: 5` retry are not pinned for cos (build report self-check (2) says so). O1 and O2 make that runnable.

FINDING O1
ROW: X3 (K1)
CLAIM: the trap's restore of `com.cobalt.cos` (`ops/desk/deploy-outage.sh:333-341` → `up_one` `:285-286`) is pinned by no test; if it bootstrapped cos from a plist other than `$REPO/ops/com.cobalt.cos.plist`, or did not restore cos, no test would fail.
RUN: TEST — `tests/ops/test_deploy_outage.py`
```python
def test_k1_check_o1_the_trap_brings_cos_up_from_the_repo_plist(box):
    """Check O1: cos booted out, a later label stuck → the trap bootstraps cos from <repo>/ops."""
    plist = load_cos(box)
    done = box.run(labels=f"{COS},{ASET}", STUB_STUCK=ASET)
    assert done.returncode == 1
    assert last_line(done).startswith(f"FAILED OUTAGE: {ASET} — "), done.stdout
    boots = [a for a in box.launchctl_calls() if a[0] == "bootstrap" and COS in a[-1]]
    assert boots == [["bootstrap", "gui/501", str(plist)]], boots
    st = box.launchd()["labels"]
    assert COS in st and st[COS]["path"] == str(plist) and st[COS]["pid"] != 504, st
    assert "RESIDENTS UP (trap)" in done.stdout, done.stdout
```
EXPECT: on the tip, if the claim is true, an assertion on `boots` or on `st[COS]` fails.

FINDING O2
ROW: X3 (K1)
CLAIM: the `Bootstrap failed: 5` retry and the trap's second try for `com.cobalt.cos` (`ops/desk/deploy-outage.sh:286-296`) are pinned by no test; a retry or trap call naming any plist but `$REPO/ops/com.cobalt.cos.plist` would pass the suite.
RUN: TEST — `tests/ops/test_deploy_outage.py`
```python
def test_k1_check_o2_every_cos_bootstrap_names_the_repo_plist(box):
    """Check O2: cos's bootstrap fails → the retry and the trap each name <repo>/ops's plist."""
    plist = load_cos(box)
    done = box.run(labels=COS, STUB_FAIL_BOOTSTRAP=COS)
    assert done.returncode == 1
    assert last_line(done).startswith(f"FAILED OUTAGE: {COS} — "), done.stdout
    assert f"down: {COS}" in last_line(done), done.stdout
    boots = [a for a in box.launchctl_calls() if a[0] == "bootstrap"]
    assert len(boots) >= 3, boots
    assert all(a == ["bootstrap", "gui/501", str(plist)] for a in boots), boots
```
EXPECT: on the tip, if the claim is true, the `all(...)` assertion fails, or fewer than three bootstraps are made.

## Findings
House A Grok (grok-4.7), finished 17:58:57 EDT (`date` at the notice). `<S>/house-a.md` (written by Grok, 12 bytes) whole: `FINDINGS: 0`. Grok's stdout: "The two scripts and their tests match the rows. No defect meets the finding bar." then the path. House B: none (not needed).
No house finding to keep.

## Dropped
none (house A wrote no FINDING block).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_outage.py::test_k1_check_o1_the_trap_brings_cos_up_from_the_repo_plist` (pasted as written in `## OWN FINDINGS`) | `1 passed, 15 warnings in 1.73s` | NOT HELD — the trap bootstraps cos once, from `<repo>/ops/com.cobalt.cos.plist`; X3 holds for the trap. Test removed with Edit. |
| O2 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_outage.py::test_k1_check_o2_every_cos_bootstrap_names_the_repo_plist` | `1 passed, 15 warnings in 1.41s` | NOT HELD — every cos bootstrap (main, retry, trap) names the repo plist; X3 holds for the retry. Test removed with Edit. |
After removal: `git status --short --branch` → `## ops/cos-outage-1018` · `?? SHADOW-INSTRUCTIONS.md` (tree at the tip). No `wip(cos-outage-1018): check red` commit (nothing held).

## FIXES
none (nothing held).

## Suites
DB: none card, no commit of mine: on the tip `de3e15c8` (HEAD `b5d62f17` above it is docs only). RESTARTS first, then W (a0), (a), (e) per `BUILD-HUB.md` `## W`, with `--deploy-gate` on (a).
- RESTARTS: `uv run cobalt jobs restarts 0bdb7089..de3e15c8` → exit 0:
```
path	change	rule	restart
ops/desk/deploy-outage.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_outage.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames 0bdb7089` → `docs/40 - DevDocs/reports/cos-outage-1018-build-2026-10-18.md` · `docs/40 - DevDocs/reports/cos-outage-1018-build-2026-10-18.result` · `ops/desk/deploy-outage.sh` · `ops/desk/deploy-step0.sh` · `tests/ops/test_deploy_outage.py` · `tests/ops/test_deploy_step0.py`. Every path is under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 6 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-outage-1018 offline --deploy-gate` → exit 0: `tests/ops: run (deploy gate)` · `offline 8612/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/cos-outage-1018-offline-20261018-175939.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-outage-1018 livenote` → exit 0: `live-note 147/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/cos-outage-1018-livenote-20261018-182816.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3966 passed, 1 xfailed, 16 warnings in 882.35s (0:14:42)`.
- with-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/cos-outage-1018/.env` → `No such file or directory` (never present in this check).

## Scope
PREFLIGHT's path union: `ops/desk/deploy-outage.sh`, `tests/ops/test_deploy_outage.py` (K1 files) and `ops/desk/deploy-step0.sh`, `tests/ops/test_deploy_step0.py` (K2 files). No path falls outside the rows' files. My commits: none.

## Checked against the branch
- (i) `git log --oneline de3e15c8..HEAD -- . ":(exclude)docs"` → empty: no commit of mine; `<tip now>` = `de3e15c8`.
- (ii) `git log --stat --format=%h de3e15c8..HEAD` → `b5d62f17` only: `.../reports/cos-outage-1018-build-2026-10-18.md | 169`, `.../cos-outage-1018-build-2026-10-18.result | 15` (docs only). No WIDENED path.
- (iii) `git log --oneline 0bdb7089..HEAD -- prompts/DEPLOY-HUB.md ops/desk/desk-launch.sh ops/desk/deploy-step-c.sh ops/desk/orphan-clean.sh src/cobalt/jobs/restarts.py data/deploy/bootstrap-owed.json "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → empty. Fenced script lines: X1 (`## OWN FINDINGS` reading notes): only the K1/K2 lines changed; `:15-30` untouched.
- (iv) no HELD finding: nothing to check.
- (v) `ls /Users/cobalt/cobalt-wt/cos-outage-1018/.env` → `No such file or directory`; `git status --short --branch` → `## ops/cos-outage-1018` · `?? SHADOW-INSTRUCTIONS.md` (routed card, BAND LOW: expected, not a finding).
- (vi) `git log --stat --format=%h 0bdb7089..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration, no with-DB test; gate lists not needed.
- (vii) the card's `## RECORDS` name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command (they name `git -C … rev-parse`, `git -C … diff --stat` and `git show`): nothing to run.
- (viii) L32: this report holds no ticker, price or date of his; the pids and paths are the tests' constructed values.

## OPEN
none. Counts: findings 2 (opus-own 2 · house 0) · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 0.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
none.

## RECORDS
- Dropped findings: none. No house produced nothing (Grok closed with `FINDINGS: 0`). No `REFUSED, not needed` line, no `CONTINUE` message, no lock take (DB: none).
- L74: one system reminder asked for a `Claude-Session:` commit line. It is recorded under `## L74` and was not acted on. I made no commit.
- The build report's DECISION 2 stands: CONTROL 3 of K1 and CONTROL 2 of K2 were never shown red under a mutation. That is the desk's item, and I did not reopen it here. O1 and O2 pinned the cos paths that were left unpinned, and both ran green.
- `deploy-outage.sh:9` still says "a label outside the three". The fence keeps that line, since K1 (d) names only `:4`, `:11` and `:13`. It is not a red and is recorded for a later card.
- The result file is written beside this report. The desk commits both: my write path to `/Users/cobalt/cobalt` is the Edit tool only, and the hub lists no `git -C` add or commit for it.
- Clock: preflight 17:48:10 · Grok started 17:49:35 · Grok done 17:58:57 · close 18:43:51 EDT.
- files opened: 13 — `prompts/CHECK-HUB.md`, `prompts/2026-10-18/784-cos-outage-card.md`, `prompts/BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`), `reports/cos-outage-1018-build-2026-10-18.md`, `ops/desk/deploy-outage.sh`, `ops/desk/deploy-step0.sh`, `tests/ops/test_deploy_outage.py`, `tests/ops/test_deploy_step0.py`, `areas/cobalt.md` (the two sections), `prompts/2026-10-18/730-f20-card.md` (grep C4a, D8), `prompts/DEPLOY-HUB.md` (grep), `reports/cto-2026-09-24.md` (R17/R19 grep), `<S>/house-a.md`.
- Check of `cos-outage-1018`: house A `Grok`, house B `none`, and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: cos-outage-1018 · pass: 1 · tip: de3e15c8 · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8612/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165134
