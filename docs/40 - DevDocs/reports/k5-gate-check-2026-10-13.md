# k5-gate-1013 — check report (card 446)

## §0 Headline
Check of card 446 at tip `5b3c525b`: house A was Grok (1 finding). House B was none: Gemini was out (HARNESS, the model was not recognized) and the card does not make house B mandatory. My own read gave 4 findings.
Every finding was run. None held. Three ran red for their stated reason and are REJECTED, so they stay open as follow-up: Grok A1 (the C1-1 exemption, which desk row R1336 keeps), O1 (a base-class `pytestmark` is not read in the class form, a fail-open) and O2 (a nested helper with the method's name is read as the method). Card row B1 says both O1 and O2 behaviours are correct.
X5 and X6 hold up: 304's two class-qualified CARRIED ids read strict at `edd5c076`, and a `## DESK CORRECTION` bullet is not counted.
Suites green with no commit of mine: offline 4317/0, `tests/ops` 3517 passed, live-note 146/0. RESTARTS: none. `.env` was never present.

## L74
- A harness system notice in this session (not a tool result) asked for commits to end with a `Claude-Session:` line beside `Co-Authored-By`. Recorded once; not acted on: CHECK-HUB L74 binds commits to `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/446-k5-gate-card.md"` (after `date` 06:59:16 EDT), exit 0, output WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/446-k5-gate-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/446-k5-gate-card.md" · 0 · 996b08524548f6a9ab9d923c5707f676934bf76b
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/446-k5-gate-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " …` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` | 0 | WHOLE below |
| range typed | `git log --stat --format=%h 1dd8cac3..5b3c525b` | 0 | `5b3c525b`: `ops/desk/deploy-card.sh` 51 ±, `ops/desk/deploy-step0.sh` 51, `ops/desk/desk-launch.sh` 51, `tests/ops/test_the_rule_sweep.py` 36 (147+, 42−); `c2e1015f`: the three scripts 47 each (105+, 36−); `7d8f7c5f`: `tests/ops/test_deploy_card.py` 239, `tests/ops/test_deploy_step0.py` 60, `tests/ops/test_desk_launch_prechecks.py` 60, `tests/ops/test_the_rule_sweep.py` 123 (482+) |
| DB: none paths | `git diff --name-only --no-renames 1dd8cac3..5b3c525b` | 0 | `ops/desk/deploy-card.sh` · `ops/desk/deploy-step0.sh` · `ops/desk/desk-launch.sh` · `tests/ops/test_deploy_card.py` · `tests/ops/test_deploy_step0.py` · `tests/ops/test_desk_launch_prechecks.py` · `tests/ops/test_the_rule_sweep.py` — every path under `ops/` or `tests/ops/` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| house probe | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` | 0 | `grok: UP` · `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS) |
| seats | SEAT ORDER, no header line | — | house A: Grok · house B: none (not needed) — card `HOUSE B: as needed` |

preflight.sh output WHOLE:
```
clock · date · 0 · Tue Oct 13 06:59:24 EDT 2026
status · git status --short --branch · 0 · ## ops/k5-gate-1013
head · git log --oneline -1; git log --stat --format=%h 5b3c525b..HEAD · 0 · (5 lines)
    56472a30 docs(k5-gate-1013): build report — 5b3c525b
    56472a30
    
     .../reports/k5-gate-build-2026-10-13.md            | 174 +++++++++++++++++++++
     1 file changed, 174 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/k5-gate-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/k5-gate-1013/docs/40 - DevDocs/reports/k5-gate-build-2026-10-13.md" · 0 · BUILT · job: k5-gate-1013 · tip: 5b3c525b | on 1dd8cac3 | migration: none | offline 4317/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 309362
range · git log --oneline 1dd8cac3..5b3c525b · 0 · (3 lines)
    5b3c525b fix(k5-gate-1013): THE RULE reads a HELD, NOT FIXED table row, a class-qualified test id, the lowercase mark and a several-id line; the sweep pinned at zero (A1 B1 C1 C2, L1 L3 L72)
    c2e1015f feat(k5-gate-1013): THE RULE's readers are four seams, no behavior change (RF, L3 L72)
    7d8f7c5f wip(k5-gate-1013): red — RF A1 B1 C1 C2 tests (card 446)
PREFLIGHT OK
```

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → output WHOLE:
```
70523 <S>/diff.md
35856 <S>/files/446-k5-gate-card.md
28341 <S>/files/k5-gate-build-2026-10-13.md
34408 <S>/files/wt/ops/desk/deploy-card.sh
42648 <S>/files/wt/ops/desk/deploy-step0.sh
122871 <S>/files/wt/ops/desk/desk-launch.sh
71460 <S>/files/wt/tests/ops/test_deploy_card.py
45801 <S>/files/wt/tests/ops/test_deploy_step0.py
76069 <S>/files/wt/tests/ops/test_desk_launch_prechecks.py
6898 <S>/files/wt/tests/ops/test_the_rule_sweep.py
356 <S>/rulings.md
STAGED 11 files · 535231 bytes · commits 3
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/k5-gate-1013-check`; commits 3 = PREFLIGHT's range.) `stage-copy.sh`, each `COPIED <bytes> <dest>`: `cto-2026-10-13.md` 15715 · `f4-refresh-check-2026-10-10.md` 33600 · `f4-refresh-build-2026-10-10.md` 49332 · `397-gate-alignment-card.md` 17309 · `361-held-table-row-card.md` 12847 · `wt/tests/ops/test_check_hub_gate_wording.py` 2691 · `desk-ops-fixes-check-2026-10-08.md` 30194 · `launcher-checks-check-2026-10-05.md` 25635 · `drc-d5-o1-b2-check-2026-10-06.md` 25188 · `radar-display-fix-1008-grok-check-2026-10-11.md` 25461 · `drc-d5-check-2026-10-04.md` 54147 · `radar-display-fix-1008-sonnet-check-2026-10-11.md` 26879 · `archiver-429-grok-check-2026-10-11.md` 30499 · `shadow-hub-build-2026-10-11.md` 32258 · `kill-hub-row-check-2026-10-10.md` 28674 · `radar-display-fix-1008-terra-check-2026-10-11.md` 22085. `HOUSE-INSTRUCTIONS.md` written (36957 bytes).
House A Grok started 07:02:36 (`date`; gates R17, R19 re-grepped, one row each), `run_in_background`, timeout 2700000; house B none (not needed). `cd` back → `git status --short --branch` → `## ops/k5-gate-1013`.

## OWN FINDINGS
Finished 07:06:05 (`date`); `ls -la <S>` then: no house file yet. Written before any house list was opened. Read: the card, the diff `1dd8cac3..5b3c525b` (`git diff` of the three scripts and the four test files), `deploy-card.sh:135-442` at the tip, `test_the_rule_sweep.py` whole, `test_deploy_card.py:560-669`, the build report whole, and `git show edd5c076:tests/cobalt/test_prefill_refresh.py` (lines 1058-1182 read: `class TestCheckFindings` `:1061`, the strict decorators `:1062-1066`, `:1152-1156`, the defs `:1067`, `:1157`, next column-0 line `:1180` `@requires_db`, no `pytestmark`).

FINDING O1
ROW: B1 (X4)
CLAIM: The class form reads a `pytestmark` only at column 0 or inside `<Class>`'s own block (`ops/desk/deploy-card.sh:350`), so a `pytestmark = pytest.mark.xfail` on a base class in the same file, which pytest applies to the subclass's methods, is not read: a FIXED line on `TestB(Base)::test_o1` passes although pytest runs that test as xfail (the plain form, reading any `pytestmark` of the file, refused it).
RUN: TEST — `tests/ops/test_deploy_card.py`:
```python
def test_check_o1_a_base_class_pytestmark_marks_the_subclass_method(tmp_path):
    import sys
    src = ("import pytest\n\n\nclass Base:\n    pytestmark = pytest.mark.xfail\n\n\n"
           "class TestB(Base):\n    def test_o1(self):\n        assert True\n")
    probe = tmp_path / "probe" / "test_probe.py"
    probe.parent.mkdir()
    probe.write_text(src)
    ran = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", str(probe)],
                         capture_output=True, text=True, timeout=120)
    assert "1 xpassed" in ran.stdout, ran.stdout
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, lines=["FIXED: O1 — tests/x.py::TestB::test_o1"],
                                     tests={"tests/x.py": src})
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 "alpha: FIXED test tests/x.py::TestB::test_o1 of O1 is marked xfail")
```
EXPECT: pytest reports the subclass method `1 xpassed` (the base `pytestmark` applies), then `_fix_refused` fails: deploy-card exits 0 and writes the card.

FINDING O2
ROW: B1 (X4)
CLAIM: The class form's def is the first `^[ \t]+def <name>\(` anywhere in the class block (`ops/desk/deploy-card.sh:355`), so a nested helper of the same name inside an earlier method is read in place of the class's own strict-xfail method: a FIXED line passes for a test pytest runs as xfail.
RUN: TEST — `tests/ops/test_deploy_card.py`:
```python
def test_check_o2_a_nested_helper_of_the_same_name_is_not_the_method(tmp_path):
    src = ("import pytest\n\n\nclass TestC:\n    def test_x(self):\n        def test_o1():\n"
           "            return 1\n        assert test_o1() == 1\n\n"
           '    @pytest.mark.xfail(strict=True, reason="carried")\n    def test_o1(self):\n        assert False\n')
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, lines=["FIXED: O1 — tests/x.py::TestC::test_o1"],
                                     tests={"tests/x.py": src})
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 "alpha: FIXED test tests/x.py::TestC::test_o1 of O1 is marked xfail")
```
EXPECT: `_fix_refused` fails: exit 0, the card written (the helper at 8 spaces is read as the method).

FINDING O3
ROW: X6 (B1)
CLAIM: The two class-qualified CARRIED ids of card 304 (`f4-refresh-build-2026-10-10.md:262`) do not read as strict xfail against the real file at the 304 fix tip `edd5c076` (`tests/cobalt/test_prefill_refresh.py:1061-1177`).
RUN: TEST — `tests/ops/test_deploy_card.py`:
```python
def test_check_o3_the_304_class_qualified_carried_ids_read_strict_at_edd5c076(tmp_path):
    src = git(REPO, "show", "edd5c076:tests/cobalt/test_prefill_refresh.py") + "\n"
    rows = (TABLE_HEAD + "| O1 | own | `x` | `1 failed` | HELD, NOT FIXED — x |\n"
            + "| A3 | own | `x` | `1 failed` | HELD, NOT FIXED — x |\n")
    lines = ["CARRIED: O1 — tests/x.py::TestCheckFindings::"
             "test_check_o1_degraded_age_is_the_last_success_when_his_stamp_owns_the_line — R7",
             "CARRIED: A3 — tests/x.py::TestCheckFindings::"
             "test_t5_a_human_stamp_still_retains_the_last_success_time_after_ten_writes — R7"]
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, runs_text=rows, held="2", lines=lines, tests={"tests/x.py": src})
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
```
EXPECT (if the claim is true): exit 1, `CARRIED test … is not a strict xfail` or `… is absent`. (A check of X6: I expect it green, NOT HELD.)

FINDING O4
ROW: X5 (A1, C2)
CLAIM: A bullet `- <id> · … HELD, NOT FIXED` under a section other than `## RUNS` / `## FIXES` (a `## DESK CORRECTION`) is now counted as a held id (`ops/desk/deploy-card.sh:189-198`).
RUN: TEST — `tests/ops/test_deploy_card.py`:
```python
def test_check_o4_a_desk_correction_bullet_is_no_held_id(tmp_path):
    rows = (HELD_RUN.format(id="O1") + "\n\n## DESK CORRECTION\n" + HELD_RUN.format(id="O2") + "\n"
            + TABLE_HEAD + "| O3 | own | `x` | `1 failed` | HELD, not fixed — x |\n")
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, runs_text=rows, lines=[FIXED_O1])
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
```
EXPECT (if the claim is true): exit 1, `lists 2 HELD, NOT FIXED row(s)` or `lists 3`. (A check of X5: I expect it green, NOT HELD.)

## Findings
House A Grok finished 07:14:33 (`date`); stdout `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/k5-gate-1013-check/house-a.md`; Grok wrote `house-a.md` itself (782 bytes), last line `FINDINGS: 1`. House B: none (not needed; card `HOUSE B: as needed`).
| id | house | row | claim | form |
|---|---|---|---|---|
| A1 | Grok | C1 | `SWEEP_EXEMPT` names `dev-rebuild-port-build-2026-10-03.md` (`test_the_rule_sweep.py:58-60`, reason `DECISION C1-1`), which is none of the ASK DESK 1, 2 or 4 shapes the card allows | TEST |
| O1 | own | B1 X4 | a base-class `pytestmark` that pytest applies to the subclass method is not read by the class form | TEST |
| O2 | own | B1 X4 | a nested helper of the same name earlier in the class block is read as the method | TEST |
| O3 | own | X6 | 304's two class-qualified CARRIED ids do not read strict at `edd5c076` | TEST |
| O4 | own | X5 | a `## DESK CORRECTION` bullet is counted as a held id | TEST |

## Dropped
none (Grok's one block carries `RUN: TEST` and a `def test_`).

## RUNS
Each test placed with the Edit tool (own ones in `tests/ops/test_deploy_card.py`, A1 in `tests/ops/test_the_rule_sweep.py`), run alone with `uv run pytest -q -rs -p no:cacheprovider --color=no <file>::<test>`; no form repair needed.
| id | source | run | output | verdict |
|---|---|---|---|---|
| A1 | Grok | `tests/ops/test_the_rule_sweep.py::test_c1_sweep_exempt_holds_only_ask_desk_shapes` | `1 failed` · `AssertionError: ['dev-rebuild-port-build-2026-10-03.md']` | REJECTED — `cto-2026-10-13.md` R1336 (`grep -n "^| R1336 "` → `8:| R1336 | 07:01 ET | DESK RECORD, brain (L79) on card 446 build: C1-1 (named SWEEP_EXEMPT for the two \`- SETTLED <path> by Edit\` lines) and B1-1 (nested class shape, recorded only) KEEP. …`): red for its stated reason, the exemption kept by the brain |
| O1 | own | `tests/ops/test_deploy_card.py::test_check_o1_a_base_class_pytestmark_marks_the_subclass_method` | `1 failed` · the probe's pytest printed `1 xpassed` (the assert before it passed), then `_fix_refused`: `deploy-card: …/03-deploy-x-set-card.md written (2 job(s), TIP 8d97dc27 f5e656fa)` · `assert 0 == 1` | REJECTED — card row B1: "a `pytestmark` counts only when it sits at module level (indent 0) or inside THAT class's block": red for its stated reason (a fail-open the plain form did not have: pytest marks `TestB(Base)::test_o1` xfail, the gate reads it plain) |
| O2 | own | `tests/ops/test_deploy_card.py::test_check_o2_a_nested_helper_of_the_same_name_is_not_the_method` | `1 failed` · `deploy-card: …/03-deploy-x-set-card.md written (2 job(s), TIP f31108f7 4c6e51e7)` · `assert 0 == 1` | REJECTED — card row B1: "the def = the first `^[ \t]+def <name>\(` inside that block"; R1336 B1-1 (nested shape, recorded only): red for its stated reason |
| O3 | own | `tests/ops/test_deploy_card.py::test_check_o3_the_304_class_qualified_carried_ids_read_strict_at_edd5c076` | `1 passed` | NOT HELD (X6: both real ids read `strict` at `edd5c076`) |
| O4 | own | `tests/ops/test_deploy_card.py::test_check_o4_a_desk_correction_bullet_is_no_held_id` | `1 passed` | NOT HELD (X5: a `## DESK CORRECTION` bullet and table row are not counted) |
All five tests removed again with the Edit tool (REJECTED and NOT HELD alike; none is committed); `git status --short --branch` → `## ops/k5-gate-1013` (clean). No HELD finding, so no `wip(k5-gate-1013): check red` commit.

## FIXES
none — no finding held.

## Suites
No commit of mine; the tip is the build's `5b3c525b`. A `DB: none` card, so W is (a0), (a), (e) and `tests/ops` (`BUILD-HUB.md` W (a0)).
- RESTARTS: `uv run cobalt jobs restarts 1dd8cac3..HEAD` → WHOLE: `docs/40 - DevDocs/reports/k5-gate-build-2026-10-13.md A DOCS -` · `ops/desk/deploy-card.sh M operator script; no Cobalt reader -` · `ops/desk/deploy-step0.sh M operator script; no Cobalt reader -` · `ops/desk/desk-launch.sh M operator script; no Cobalt reader -` · `tests/ops/test_deploy_card.py M test/documentation; no resident -` · `tests/ops/test_deploy_step0.py M test/documentation; no resident -` · `tests/ops/test_desk_launch_prechecks.py M test/documentation; no resident -` · `tests/ops/test_the_rule_sweep.py A test/documentation; no resident -` · `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames 1dd8cac3` → `docs/40 - DevDocs/reports/k5-gate-build-2026-10-13.md`, `ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_card.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_the_rule_sweep.py`: every path under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 8 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh k5-gate-1013 offline` → exit 0: `offline 4317/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/k5-gate-1013-offline-20261013-071536.log` (`:885` `4317 passed, 806 skipped, 1 xfailed, 36 warnings in 679.70s (0:11:19)`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3517 passed, 1 xfailed, 16 warnings in 720.36s (0:12:00)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh k5-gate-1013 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/k5-gate-1013-livenote-20261013-072719.log`. `grep -n -F "COBALT_LIVE_VAULT_ROOT" <log>` → only `:2` (the command line), so no skip names it.
- with-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/k5-gate-1013/.env` → `No such file or directory` (07:27, never present).

## Scope
PREFLIGHT's union: `ops/desk/deploy-card.sh`, `ops/desk/desk-launch.sh`, `ops/desk/deploy-step0.sh` (rows RF A1 B1 C2), `tests/ops/test_deploy_card.py`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_the_rule_sweep.py` (rows' tests); the build report under `docs/`. My commits: none. Every script hunk lies inside THE RULE block: `git diff -U0 1dd8cac3..5b3c525b -- ops/desk/desk-launch.sh ops/desk/deploy-step0.sh` shows hunks at `desk-launch.sh` 1124-1375 and `deploy-step0.sh` 163-414, and `deploy-card.sh` changes sit at 159-410 inside `:135`-`:442`. `grep -rn -F "held_runs" ops/desk` → hits only in those blocks (`deploy-card.sh:160,187,188,202,219`, `desk-launch.sh:1125,1152,1153,1167,1184`, `deploy-step0.sh:164,191,192,206,223`). No path to a score, rank, grade or size: the change is in operator scripts and ops tests only.
CHECK ASKS: X1, the one-text pin `test_h1_the_rule_is_one_text_in_the_three_scripts` and the existing h1/g1/g2/t1 tests are green inside `tests/ops` 3517 passed. X2, the builder's mutation table (build report `## E3`, its claim, not re-run here): with the A1 branch removed, `adoption-hubs-check-2026-10-03-r2.md`, `adoption-hubs-check-2026-10-03.md`, `drc-d5-o1-b2-check-2026-10-06.md`, `f4-refresh-check-2026-10-10.md` and `launcher-checks-check-2026-10-05.md` turn red; with the class branch removed, no report does (the only real class-form claim, `f4-refresh-build-2026-10-10.md:262`, is exempt). X3: Grok's A1 (REJECTED, R1336). X4: O1 and O2 (REJECTED, card B1). X5: O4 (NOT HELD). X6: O3 (NOT HELD).

## Checked against the branch
(i) `git log --oneline 5b3c525b..HEAD -- . ":(exclude)docs"` → empty (no commit of mine; `<tip now>` = `5b3c525b`). (ii) `git log --stat --format=%h 5b3c525b..HEAD` → `56472a30` · `.../reports/k5-gate-build-2026-10-13.md | 174` (docs only). (iii) `git log --oneline 1dd8cac3..HEAD -- src configs ops/desk/authorize.sh ops/desk/bare-guard.py ops/desk/install-fixed.sh "docs/40 - DevDocs/prompts"` → empty. (iv) no HELD finding. (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/k5-gate-1013`. (vi) `git log --stat --format=%h 1dd8cac3..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration and no with-DB test, so no gate lists are owed. (vii) the card's records: `git -C /Users/cobalt/cobalt log --oneline -1 -- ".../f4-refresh-check-2026-10-10.md"` → `71a84c1a docs(desk): card 304 check report, ready NO`; `… f4-refresh-build-2026-10-10.md` → `70108697 docs(desk): R1309 brain queue 10-13, 304 fix report on main, deploy-card refusal asked of the brain` (both as recorded). `ls -la /Users/cobalt/.claude/ops/{deploy-card,deploy-step0,desk-launch}.sh` → three symlinks to `/Users/cobalt/cobalt/ops/desk/…` (as recorded). `grep -c -F "card 446"` → `1` in each of the three scripts (DEPLOY PROOF after-value in the worktree). (viii) L32: this report quotes no ticker, price or date of his; the 304 test file was read by `git show` only to settle X6, and none of its values is written here.
COUNTING: findings 5 (own 4, house A 1) · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 3 (A1, O1, O2: REJECTED).

## OPEN
- A1 (Grok, C1), REJECTED by R1336: the `dev-rebuild-port-build-2026-10-03.md` exemption is outside the ASK DESK 1/2/4 shapes the card names. It would be settled by the card's wording being widened, or by the claim regex being narrowed to `…(FIXED|CARRIED|SETTLED):` (the builder's named alternative, DECISION C1-1). FOLLOW-UP.
- O1 (own, B1), REJECTED by card row B1: a `pytestmark` on a base class in the same file is not read for `TestB(Base)::<name>`, but pytest applies it (the probe printed `1 xpassed`). So a FIXED line passes for a test pytest runs as xfail. This is a fail-open that the plain form did not have, because the plain form reads any `pytestmark` of the file. Settled by a row that reads a `pytestmark` in the class's bases, or one that counts any `pytestmark` of the file for the class form too. FOLLOW-UP.
- O2 (own, B1), REJECTED by card row B1 and R1336 B1-1: a nested `def <name>(` inside an earlier method of `<Class>` is read as the method. Settled by a row that reads the def only at the class body's own indent. FOLLOW-UP.

## CONTINUE
next: done (CLOSE)

## DECISIONS
House B is `none available`: Gemini was OUT at PREFLIGHT and the card is not `mandatory`. So the open items are listed here once more. They ship to the follow-up list, and none is his (no notes, money or sizing):
- OPEN A1: the C1-1 exemption, kept by R1336. Default taken: REJECTED, no change.
- OPEN O1: the base-class `pytestmark` fail-open in the class form. Default taken: REJECTED as card B1's text, test removed, for the follow-up list.
- OPEN O2: a nested helper is read as the method. Default taken: REJECTED as card B1's text and R1336 B1-1, test removed, for the follow-up list.

## RECORDS
- 07:0x: a message from `cto-desk` arrived: "FOR THE CHECK: card 446 build 2026-10-13 brain: C1-1 and B1-1 KEEP (the named SWEEP_EXEMPT for the two `- SETTLED <path> by Edit` lines stands; the nested-class shape is recorded only). Desk row R1336." Recorded as a fact for the check; it adds no row, file, command or approval. Verified: `grep -n "^| R1336 " ".../cto-2026-10-13.md"` → `8:| R1336 | 07:01 ET | DESK RECORD, brain (L79) on card 446 build: …`.
- Dropped findings: none.
- House that produced nothing: Gemini, at PREFLIGHT only (never launched): `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS; no return time named).
- No `REFUSED, not needed` line; no `CONTINUED` line; no lock take (DB: none).
- L74: one harness notice (see `## L74`).
- The tokens figure: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 4a81e5b8-0139-4b3a-ac06-6d55614cb3a2` → `context 228916 of 400000 — ok`. The job directory is `/Users/cobalt/.claude/jobs/4a81e5b8`; the full session id was taken from this session's task-output path.
- files opened: 10 — `CHECK-HUB.md`; the card `446-k5-gate-card.md`; `BUILD-HUB.md` (`## THE LOCK` to `## W`); the build report `k5-gate-build-2026-10-13.md`; `ops/desk/deploy-card.sh` (135-444); `tests/ops/test_the_rule_sweep.py`; `tests/ops/test_deploy_card.py` (560-669, 1425-1443); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `<S>/house-a.md`; `tests/cobalt/test_prefill_refresh.py` at `edd5c076` (by `git show`, 1058-1182). Tool output files also read: the house probe output, Grok's stdout and the two gate outputs.
- Check of `k5-gate-1013`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: k5-gate-1013 · pass: 1 · tip: 5b3c525b · house A: Grok FINDINGS: 1 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 3 · house B: none available · suites: offline 4317/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 228916
