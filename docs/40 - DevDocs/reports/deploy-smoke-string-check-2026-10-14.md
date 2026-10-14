# deploy-smoke-string-1014 — CHECK REPORT (2026-10-14)

## §0 Headline
- Card 537 checked on tip `f21900fc` by house A Grok (FINDINGS: 1) and me (6). Gemini was OUT at the probe, and house B was not needed (`as needed`).
- 7 findings · 0 held · 0 fixed · 1 open: O1 is REJECTED (T1's floor covers check reports only, so a build glob that finds nothing stays green) and goes on the follow-up list.
- X1–X3 answered: the string is byte-equal and appears once in each of the three files. No other launch line changed, and `--json` writes nothing.
- Suites on the tip: offline 4328/0 · live-note 146/0 · `tests/ops` 3604 passed / 0 failed. cobalt_dev not taken (DB: none). RESTARTS: none. ready: YES.

## L74
- A system notice in this session asked that git commits end with a `Claude-Session:` line. Recorded as data and not followed. This check made no commit.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/537-deploy-smoke-string-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/537-deploy-smoke-string-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-14/537-deploy-smoke-string-card.md" · 0 · eb797ddd985cd66f560a8f47214c03d1bd038745
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-14/537-deploy-smoke-string-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
House gates (13:25 EDT): `grep -n "^| R17 " …cto-2026-09-24.md` → one row (line 35); `grep -n "^| R19 " …cto-2026-09-24.md` → one row (line 37); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Wed Oct 14 13:25:45 EDT 2026
status · git status --short --branch · 0 · ## ops/deploy-smoke-string-1014
head · git log --oneline -1; git log --stat --format=%h f21900fc..HEAD · 0 · (5 lines)
    c9fcabfa docs(deploy-smoke-string-1014): build report — f21900fc
    c9fcabfa

     .../deploy-smoke-string-build-2026-10-14.md        | 55 ++++++++++++++++++----
     1 file changed, 45 insertions(+), 10 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/deploy-smoke-string-1014/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/deploy-smoke-string-1014/docs/40 - DevDocs/reports/deploy-smoke-string-build-2026-10-14.md" · 0 · BUILT · job: deploy-smoke-string-1014 · tip: f21900fc | on 7aa5d470 | migration: none | offline 4328/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 96124
range · git log --oneline 7aa5d470..f21900fc · 0 · (6 lines)
    f21900fc fix(deploy-smoke-string-1014): the rule sweep pins zero mismatches and a floor of 18 checks, not a count (T1; L1, L72)
    042630b7 wip(deploy-smoke-string-1014): W — desk resend recorded, not followed (BUILD-HUB (b))
    cfcb5a2b wip(deploy-smoke-string-1014): W — desk CONTINUE adding row T1 recorded, not followed (BUILD-HUB (b))
    4c3ae576 wip(deploy-smoke-string-1014): W — tests/ops red on BASE (test_the_rule_sweep pin 18, main has 21)
    9fb997bb feat(deploy-smoke-string-1014): deploy line and STANDING-LIST carry the read-only cobalt smoke string (S3, S1, S2; L1, L28, L72)
    4ea64dce wip(deploy-smoke-string-1014): red — S3 pin, S1/S2 tests
PREFLIGHT OK
```
- THE RANGE typed: `git log --stat --format=%h 7aa5d470..f21900fc` · exit 0 · paths: f21900fc `tests/ops/test_the_rule_sweep.py` (+7 −5); 042630b7, cfcb5a2b, 4c3ae576 the build report only; 9fb997bb `DEPLOY-HUB.md` (+1 −1), `STANDING-LIST.md` (+2 −1); 4ea64dce `tests/ops/test_deploy_smoke_string_1014.py` (+102), `tests/ops/test_hub_lines.py` (+1). Path union: the six paths below.
- DB: none: `git diff --name-only --no-renames 7aa5d470..f21900fc` · exit 0 · whole:
```
docs/40 - DevDocs/prompts/DEPLOY-HUB.md
docs/40 - DevDocs/prompts/STANDING-LIST.md
docs/40 - DevDocs/reports/deploy-smoke-string-build-2026-10-14.md
tests/ops/test_deploy_smoke_string_1014.py
tests/ops/test_hub_lines.py
tests/ops/test_the_rule_sweep.py
```
every path under `docs/` or `tests/ops/`.
- `ls <S>` · exit 1 · `No such file or directory` → fresh.
- House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0 · lines whole:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
No `HOUSE A: OpenAI` header line → Sol not probed. Gemini OUT → HARNESS (no return time named). **house A: Grok · house B: none (not needed)** — card `HOUSE B: as needed`, so the MANDATORY rule does not apply.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · output whole:
```
7035 <S>/diff.md
16434 <S>/files/537-deploy-smoke-string-card.md
27282 <S>/files/deploy-smoke-string-build-2026-10-14.md
65318 <S>/files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md
46345 <S>/files/wt/docs/40 - DevDocs/prompts/STANDING-LIST.md
20992 <S>/files/wt/docs/40 - DevDocs/reports/deploy-smoke-string-build-2026-10-14.md
4207 <S>/files/wt/tests/ops/test_deploy_smoke_string_1014.py
13611 <S>/files/wt/tests/ops/test_hub_lines.py
6770 <S>/files/wt/tests/ops/test_the_rule_sweep.py
356 <S>/rulings.md
STAGED 10 files · 208350 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/deploy-smoke-string-1014-check`.) `commits 2` = the commits of `git log -p 7aa5d470..f21900fc -- . ":(exclude)docs"` (4ea64dce, f21900fc); PREFLIGHT's range holds 6, the other 4 touching `docs/` only (see ASK DESK 1 under `## DECISIONS`).
`stage-copy.sh`, each its own call:
```
COPIED 27668 <S>/files/deploy-plist-step-c-1013.md
COPIED 66463 <S>/files/cto-2026-10-13.md
COPIED 17929 <S>/files/CARD.md
COPIED 18862 <S>/files/523-hub-text-card.md
COPIED 5493 <S>/files/516-sweep-pin-card.md
COPIED 127758 <S>/files/wt/ops/desk/desk-launch.sh
COPIED 4024 <S>/files/wt/src/cobalt/smoke/cli.py
COPIED 2135 <S>/files/wt/tests/ops/test_build_hub_no_clutter.py
COPIED 12098 <S>/files/wt/src/cobalt/jobs/restarts.py
```
Written by me under `<S>`: `HOUSE-INSTRUCTIONS.md` (17913 B; HOUSE TEXT verbatim, then the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, then "Files:"), and `diff-docs.md` (2494 B; the STANDING-LIST.md hunks of `git diff 7aa5d470..f21900fc -- "docs/40 - DevDocs/prompts"` and a description of the DEPLOY-HUB.md line-11 insertion, since `diff.md` excludes `docs/` and so holds no hunk of rows S1/S2).
House launch 13:28:05 EDT: gates R17 → 1 row, R19 → 1 row, R19 commit `5055151dbf68899b82de5b11f99733ed2d03048c`; `ls -la <S>` → diff-docs.md, diff.md, files/, HOUSE-INSTRUCTIONS.md, rulings.md; `cd <AGY>`; Grok started (`run_in_background`, task `bcgntcx08`); `cd <WT>`; `git status --short --branch` → `## ops/deploy-smoke-string-1014`. House B: none (not needed).

## OWN FINDINGS
Written before any house list was opened.

FINDING O1
ROW: T1
CLAIM: The floor guards the check glob only; the build glob (`tests/ops/test_the_rule_sweep.py:101`) lost its pin (`BUILDS_SWEPT`, removed at `:60-62`) and has no floor, so a build glob that finds nothing leaves `test_the_sweep_swept_what_it_pins` (`:148-152`) green — the row's "a broken glob that finds nothing still fails" holds for one of the sweep's two globs.
RUN: TEST — `tests/ops/test_the_rule_sweep.py`
```python
def test_o1_an_empty_build_glob_fails_the_sweep_pin(sweep):
    checks, _, _ = sweep
    with pytest.raises(AssertionError):
        test_the_sweep_swept_what_it_pins((checks, [], {}))
```
EXPECT: `Failed: DID NOT RAISE <class 'AssertionError'>`.

FINDING O2
ROW: X1 (S1)
CLAIM: `DEPLOY-HUB.md` changes outside line 11 between BASE and TIP.
RUN: COMMAND — `git diff -U0 7aa5d470..f21900fc -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: a hunk header other than `@@ -11 +11 @@`.

FINDING O3
ROW: X2
CLAIM: A launch line other than `DEPLOY-HUB.md:11` carries a `cobalt smoke` string at the tip.
RUN: COMMAND — `grep -rn -F "uv run cobalt smoke *)" "docs/40 - DevDocs/prompts"`
EXPECT: a hit in a file other than `DEPLOY-HUB.md` / `STANDING-LIST.md`.

FINDING O4
ROW: X3 (S2 "can touch" cell)
CLAIM: `cobalt smoke … --json` still writes the report file, so the cell's "the one smoke report … is written" understates nothing but the DEPLOY PROOF's "`--json` … writes no report file" is false (`src/cobalt/smoke/cli.py:71-80`).
RUN: COMMAND — `grep -n -F "write_report" src/cobalt/smoke/cli.py`
EXPECT: a `write_report` call outside the `else:` branch of `cmd_run` (any line other than `:76`).

FINDING O5
ROW: S1 (entry path: `desk-launch.sh` builds the deploy line)
CLAIM: The deploy line `desk-launch.sh` prints (`ops/desk/desk-launch.sh:2174-2189`, token fill) does not carry the smoke string once in its `--allowedTools` list; no test reads the launched line for it (`tests/ops/test_hub_lines.py:278-282` reads only the flag).
RUN: TEST — `tests/ops/test_hub_lines.py`
```python
def test_o5_the_deploy_launch_prints_the_smoke_string_once(desk):
    done = desk.launch("deploy", dry=True)
    assert done.returncode == 0, done.stderr
    (line,) = [ln for ln in done.stdout.splitlines() if ln.startswith("claude --bg ")]
    allow = tools(line, "--allowedTools")
    assert allow.count("Bash(COBALT_ENV=production uv run cobalt smoke *)") == 1, allow
```
EXPECT: `AssertionError` (count 0) or a non-zero return code.

FINDING O6
ROW: S2 (heading counts, ASK DESK 2)
CLAIM: The `## 3.` heading's `54 without a migration` (`STANDING-LIST.md:109`) is not the number of allow strings `DEPLOY-HUB.md:11` carries with one head, no migration and no `## LAUNCHD`; no test pins it (card RECORDS).
RUN: TEST — `tests/ops/test_deploy_smoke_string_1014.py`
```python
def test_o6_the_heading_counts_match_the_line():
    allow = tools(hub_line("DEPLOY-HUB.md"), "--allowedTools")
    tokens = {"<tip", "merges>", "<prod", "migrate", "strings>", "<launchd"}
    real = [s for s in allow if s not in tokens]
    heading = (HUBS / "STANDING-LIST.md").read_text(encoding="utf-8").split("\n## 3. ", 1)[1].splitlines()[0]
    assert f"{len(real) + 1 + 3} allow with one head and a migration ({len(real) + 1} without a migration" in heading, (len(real), heading)
```
EXPECT: `AssertionError` naming the computed count against the heading.

## Findings
House A Grok: task `bcgntcx08` exit 0 at 13:41:54 EDT (`date`); `ls -la <S>` → `house-a.md` 791 B, written by Grok; stdout was the path only. Its last line: `FINDINGS: 1`. House B: none (not needed; Gemini OUT at PREFLIGHT).
THE DROP: `grep -n -F "RUN:"` over `house-a.md` → `4:RUN: COMMAND`, followed by the line `grep -n "^FAILED: W" "docs/40 - DevDocs/reports/deploy-smoke-string-build-2026-10-14.md"` (allowed beginning) → kept.

| id | house | row | claim | run |
|---|---|---|---|---|
| G1 | Grok (A) | T1 | The build report at the tip still records T1 unbuilt and a `FAILED: W` line quoting the old pin (`:6`, `:107`, `:143`) while the test now holds `CHECKS_FLOOR` | COMMAND |

## Dropped
none

## RUNS
Each test was put in the file it names with Edit and run alone (`uv run pytest -q -rs -p no:cacheprovider --color=no <file>::<test>`); each was removed again with Edit (`git status --short --branch` after → `## ops/deploy-smoke-string-1014`, nothing else).

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `tests/ops/test_the_rule_sweep.py::test_o1_an_empty_build_glob_fails_the_sweep_pin` | `1 failed, 15 warnings in 1.28s` · `E       Failed: DID NOT RAISE <class 'AssertionError'>` (`tests/ops/test_the_rule_sweep.py:157`) | REJECTED — card row T1: "a floor (≥18 checks swept, so a broken glob that finds nothing still fails)" and "no longer pins the number of reports swept": the row defines the floor on check reports only. Red for its stated reason; OPEN. Test removed (a red test cannot stay in the suite). |
| O2 | own | `git diff -U0 7aa5d470..f21900fc -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | one hunk, `@@ -11 +11 @@`; the `+` line equals the `-` line with `"Bash(COBALT_ENV=production uv run cobalt smoke *)" ` inserted after `heartbeat show*)"` | NOT HELD |
| O3 | own | `grep -rn -F "uv run cobalt smoke *)" "docs/40 - DevDocs/prompts"` | hits: `DEPLOY-HUB.md:11`, `STANDING-LIST.md:140`; `2026-09-17/01-p4-build.md:27` and `2026-09-19/24-p4-fund-rule.md:10` (a September `claude -p` builder list, `Bash(uv run cobalt smoke *)` with no `COBALT_ENV=production`, not a launch line X2 names, untouched in the range: (iii) below); the 536/537/539 card and drafter texts | NOT HELD |
| O4 | own | `grep -n -F "write_report" src/cobalt/smoke/cli.py` | `76:        path = report_mod.write_report(rep, reports_dir=report_mod.REPORTS_DIR)` (only hit; `:73` `if args.json:` prints, `:75` `else:` writes) | NOT HELD |
| O5 | own | `tests/ops/test_hub_lines.py::test_o5_the_deploy_launch_prints_the_smoke_string_once` | `1 passed, 15 warnings in 1.22s` | NOT HELD (removed) |
| O6 | own | `tests/ops/test_deploy_smoke_string_1014.py::test_o6_the_heading_counts_match_the_line` | `1 passed, 15 warnings in 0.78s` | NOT HELD (removed) |
| G1 | Grok (A) | `grep -n "^FAILED: W" "docs/40 - DevDocs/reports/deploy-smoke-string-build-2026-10-14.md"` | exit 1, no output (the worktree at HEAD `c9fcabfa`, the docs-only report commit above `TIP`; Grok read the stage-set copy taken from git at `f21900fc`, before that report commit) | NOT HELD |

No test HELD: no `wip(deploy-smoke-string-1014): check red` commit.

## FIXES
none (nothing held).

## Suites
DB: none card. No commit of mine, so the tip is the build's `TIP` `f21900fc` (worktree HEAD `c9fcabfa`, docs only above it). RESTARTS, then W as `BUILD-HUB.md` gives it for this card: (a0), (a), (e), plus `tests/ops`.
- RESTARTS: `uv run cobalt jobs restarts 7aa5d470..HEAD` · exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/deploy-smoke-string-build-2026-10-14.md	A	DOCS	-
tests/ops/test_deploy_smoke_string_1014.py	A	test/documentation; no resident	-
tests/ops/test_hub_lines.py	M	test/documentation; no resident	-
tests/ops/test_the_rule_sweep.py	M	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames 7aa5d470` · exit 0 → the six paths of PREFLIGHT, each under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 6 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-smoke-string-1014 offline` · exit 0 → `offline 4328/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-smoke-string-1014-offline-20261014-134249.log`
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-smoke-string-1014 livenote` · exit 0 → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-smoke-string-1014-livenote-20261014-134250.log`
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` · exit 0 → `3604 passed, 1 xfailed, 16 warnings in 752.99s (0:12:32)`
- `.env`: `ls /Users/cobalt/cobalt-wt/deploy-smoke-string-1014/.env` → `No such file or directory` (13:55 EDT); never present; no lock taken.

## Scope
PREFLIGHT's path union (`7aa5d470..f21900fc`): `DEPLOY-HUB.md` (row S1), `STANDING-LIST.md` (S2), `tests/ops/test_hub_lines.py` (S3), `tests/ops/test_deploy_smoke_string_1014.py` (S1, S2), `tests/ops/test_the_rule_sweep.py` (T1), the build report (docs). Every path in a row's `files` or `docs/`. My commits: none.

## Checked against the branch
- (i) `git log --oneline f21900fc..HEAD -- . ":(exclude)docs"` → empty: no commit of mine; `<tip now>` = `f21900fc`.
- (ii) `git log --stat --format=%h f21900fc..HEAD` → `c9fcabfa` · `.../deploy-smoke-string-build-2026-10-14.md | 55 ++++++++++++++++++----` (docs only).
- (iii) fence: `git log --oneline 7aa5d470..HEAD -- ops src configs .claude` → empty; `git log --oneline 7aa5d470..HEAD -- <BUILD-HUB, CHECK-HUB, DEVFIX-HUB, SHADOW-HUB, CLOSE-HUB, BRAIN-HUB, OPS-HAND, PRODWRITE-HUB, SPIKE-HUB, CTO-DESK-WAKEUP .md under docs/40 - DevDocs/prompts>` → empty. `DEPLOY-HUB.md` text outside line 11: O2 (`@@ -11 +11 @@` only).
- (iv) no HELD finding.
- (v) after W: see `## Suites`.
- (vi) `git log --stat --format=%h 7aa5d470..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration, no with-DB test; gate lists not owed.
- (vii) card RECORDS: `grep -c "^claude --bg " "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → `1` (record: 1). `grep -c -F "cobalt smoke"` → `DEPLOY-HUB.md:1`, `STANDING-LIST.md:1`, `tests/ops/test_hub_lines.py:1` (record's BASE reads 0; the DEPLOY PROOF's after-counts 1, 1, 1 hold at the tip). `grep -rl "56 allow" tests ops` → empty (record: no test asserts the STANDING-LIST allow count; O6 counted it by hand: 53 strings + 1 head = 54, + 3 migrate = 57, as the heading says).
- (viii) L32: this report holds no ticker, price or date of his; the hosts and paths quoted are the files' own.
- CHECK ASKS: X1 — O2, O3, (vii): the string is byte-equal, once in `DEPLOY-HUB.md:11`, once in `STANDING-LIST.md` (`:140`, inside `## 3.`), once in the `test_hub_lines.py` pin; the one hunk of `DEPLOY-HUB.md` is line 11 and removing the string with its trailing space gives BASE's line (S1 (2), green in the suite). X2 — O3 and (iii): no other launch line gains a `cobalt smoke` string. X3 — O4: `cmd_run` writes the report only in the `else:` branch of `if args.json:` (`src/cobalt/smoke/cli.py:73-77`); `--json` writes nothing; with `--prod` it reads the production database (`:13-14`, `:89`). The new row's cell ("read only: … and the one smoke report … is written") is true.

## OPEN
- O1 (REJECTED — T1's row text sets the floor on check reports only): `test_the_sweep_swept_what_it_pins` has no floor on the build-report glob (`tests/ops/test_the_rule_sweep.py:101`); a build glob that finds nothing keeps it green. Would settle it: a `BUILDS_FLOOR` (the first run's 85) asserted beside `CHECKS_FLOOR`, by a card row that names it — or a ruling that the check floor alone is enough. FOLLOW-UP.

## CONTINUE
next: none (check done)

## DECISIONS
1. ASK DESK 1 [13:26 EDT]: `stage-set.sh` ended `STAGED 10 files · 208350 bytes · commits 2`, while PREFLIGHT's range holds 6 commits. `## 1` (1) asks for the diff's `^commit ` count to equal PREFLIGHT's commit count, and the diff it prescribes excludes `docs/`. The two counts differ because 4 of the 6 commits touch `docs/` only, and rows S1 and S2 live under `docs/`. Default I took: continued. I staged the two hub-doc hunks as `<S>/diff-docs.md` and named that file in the house instructions. Read O2 and the whole-file copies for the full before/after. Question for the desk: should the copy rule count only non-docs commits?
2. OPEN (house B none available; the open item ships to the follow-up list): O1 REJECTED. T1's floor guards the check-report glob only, so a build-report glob that finds nothing keeps `test_the_sweep_swept_what_it_pins` green (`tests/ops/test_the_rule_sweep.py:101`, `:148-152`). Default I took: no change. The row's own text scopes the floor to checks. It goes to the one fix round only if a card row names a build floor.

## RECORDS
- Dropped findings: none. Houses that produced nothing: Gemini, at the PREFLIGHT probe: `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS, not launched; house B was not needed).
- 13:25 EDT, a message from session `cto-desk`: "537 build decisions 2-4 KEEP as built (brain 0e848919, 10-14)". It is not a `CONTINUE`; it names no step and adds nothing. Recorded, nothing to act on (the build's DECISIONS 2-4 were not a check finding).
- `REFUSED, not needed`: none. `CONTINUED`: none. Lock takes: none (DB: none).
- The trial tests O1, O5, O6 were added and removed with Edit. The tree ended clean (`git status --short --branch` → `## ops/deploy-smoke-string-1014`).
- Grok read the build report as `stage-set.sh` copied it from git at `TIP` `f21900fc`. The report commit `c9fcabfa` (above `TIP`) rewrote it, so G1's quoted lines exist only in the older copy.
- files opened: 15 (Read): `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`); the build report; `tests/ops/test_the_rule_sweep.py`; `src/cobalt/smoke/cli.py`; `tests/ops/test_hub_lines.py` (:40-149); `areas/cobalt.md` (from `## What Cobalt is`); `<S>/diff.md`; `<S>/house-a.md`; five background-task outputs (probe, Grok, offline, live-note, `tests/ops`). Searched by Grep only: `STANDING-LIST.md` headings; `src/cobalt/smoke/`; `cto-2026-10-13.md` / `cto-2026-10-14.md` rows R1341, R1466, R1477; `tests/ops/test_hub_lines.py` (dry-launch test).
- Check of `deploy-smoke-string-1014`: house A `Grok`, house B `none`, and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: deploy-smoke-string-1014 · pass: 1 · tip: f21900fc · house A: Grok FINDINGS: 1 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 15 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 178351
