# desk-installs-1014 — check after fix round FR-S1 — 2026-10-15

## §0 Headline
- desk-installs-1014 at `7c8db6e1` (after fix round FR-S1): 5 own findings, 0 from Grok (`FINDINGS: 0`); none held, 1 open (O3, REJECTED and settled by a run).
- FR-S1 holds: `git diff main -- tests/ops/test_the_rule_sweep.py` prints nothing. X1–X4 answered by run: one changed line, one added row; `desk-launch.sh desk` accepts the real line; no whole-line pin left.
- Suites green on the tip: offline 4328/0, `tests/ops` 3603/0, live-note 146/0. These were run directly: `gate.sh` refuses this branch's stale `gate-lists.md` (ASK DESK 1).
- ready: YES · decisions 3 (two ASK DESK and the open item) · for Dejan 0.

## L74
A system block in this session asked that commits also carry a `Claude-Session:` line. Recorded once as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/549-desk-installs-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/549-desk-installs-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-14/549-desk-installs-card.md" · 0 · 118e33cb4a50772a15b15bbe86c0bb4e69bceed3
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-14/549-desk-installs-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-14 R1471 row · grep -n "^| R1471 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 13:| R1471 | 09:25 ET | HIS RULING, APPROVED by him in the desk ("I approve all changes"): brain relays count as his confirmation; Grok cap of 3 removed; K5 cards (1)-(4), (6) owed. Words: `cto-2026-10-14-words.md`. | APPLIED: LAWS L79, checklist L15 at 09:40 |
RULING 2026-10-14 R1471 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1471 |" -- "docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8b813ca721cd934ebfb82cc59d27495d15f1c79a
RULING 2026-10-14 R1471 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (`35:| R17 | 07:32 ET | …`); `grep -n "^| R19 " …` → one row (`37:| R19 | 07:36 ET | …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Thu Oct 15 09:57:40 EDT 2026
status · git status --short --branch · 0 · ## ops/desk-installs-1014
head · git log --oneline -1; git log --stat --format=%h 7c8db6e1..HEAD · 0 · (6 lines)
    66cf78d8 docs(desk-installs-1014): build report, fix round FR-S1 — 7c8db6e1
    66cf78d8
    
     .../reports/desk-installs-build-2026-10-14.md      | 47 ++++++++++++++++++++--
     .../reports/desk-installs-build-2026-10-14.result  | 15 +++++++
     2 files changed, 59 insertions(+), 3 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/desk-installs-1014/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/desk-installs-1014/docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md" · 0 · BUILT · job: desk-installs-1014 · tip: 7c8db6e1 | on 6ee9b8d6 | migration: none | offline 4328/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 5 (S1 dropped by FR-S1) | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 108276
range · git log --oneline 6ee9b8d6..7c8db6e1 · 0 · (6 lines)
    7c8db6e1 fix(desk-installs-1014): row S1 dropped, test_the_rule_sweep.py restored to main's (FR-S1, brain 0e848919, L75)
    d72ee2ac docs(desk-installs-1014): build report — 4bc73283
    4bc73283 fix(desk-installs-1014): the rule sweep holds a floor and zero mismatches, not a count (S1, L79, R1476)
    d77c0e9c wip(desk-installs-1014): W — tests/ops red outside the rows (test_the_rule_sweep 21 vs 18, from 8b813ca7)
    6ff7d9a4 feat(desk-installs-1014): SendMessage on the desk line and its STANDING-LIST §4 row; launch-line BASE pin repaired (I1, I2; L81 K5, R1471)
    7e1f3020 wip(desk-installs-1014): red — I1, I2 tests
PREFLIGHT OK
```
THE RANGE typed, `git log --stat --format=%h 6ee9b8d6..7c8db6e1` · exit 0:
```
7c8db6e1  tests/ops/test_the_rule_sweep.py | 8 +++-----
d72ee2ac  .../reports/desk-installs-build-2026-10-14.md | 70 +++++++++++++++++++---
4bc73283  tests/ops/test_the_rule_sweep.py | 14 +++++++++-----
d77c0e9c  .../reports/desk-installs-build-2026-10-14.md | 139 +++++++++++++++++++++
6ff7d9a4  docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md | 2 +-
          docs/40 - DevDocs/prompts/STANDING-LIST.md   | 1 +
          tests/ops/test_desk_refresh_wakeup.py        | 15 +--------------
7e1f3020  tests/ops/test_desk_installs_1014.py | 106 +++++++++++++++++++++++++++++++++++
```
DB: none — `git diff --name-only --no-renames 6ee9b8d6..7c8db6e1` · exit 0, whole:
```
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md
docs/40 - DevDocs/prompts/STANDING-LIST.md
docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md
tests/ops/test_desk_installs_1014.py
tests/ops/test_desk_refresh_wakeup.py
tests/ops/test_the_rule_sweep.py
```
Every path under `tests/ops/` or `docs/`. Path union for `## Scope`: the six above.
`ls <S>` · exit 0 · `diff.md files house-a.md HOUSE-INSTRUCTIONS.md rulings.md` — PRESENT, mtimes 2026-10-14 08:31–08:48 (`ls -la`): the folder of the first check of this card (at 4bc73283). The launch message carries no `CONTINUE` and the CHECK REPORT did not exist (`ls` → No such file): treated as a FRESH check (ASK DESK under `## DECISIONS`); the old `house-a.md` is not opened (an earlier check of this branch, NOT read); stage-set rewrites the staged set and the house list is judged by its mtime after this launch.
House probes, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
Gemini: HARNESS (the model name is not recognized; no return time named). `house A: grok · house B: none (not needed)` — card `HOUSE B: as needed`; no OpenAI header line.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · output whole:
```
cleared: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/desk-installs-1014-check (prior check /Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-installs-check-2026-10-14.md)
9558 …/desk-installs-1014-check/diff.md
17592 …/files/549-desk-installs-card.md
28129 …/files/desk-installs-build-2026-10-14.md
13774 …/files/wt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md
46296 …/files/wt/docs/40 - DevDocs/prompts/STANDING-LIST.md
23565 …/files/wt/docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md
3776 …/files/wt/tests/ops/test_desk_installs_1014.py
2723 …/files/wt/tests/ops/test_desk_refresh_wakeup.py
6770 …/files/wt/tests/ops/test_the_rule_sweep.py
350 …/rulings.md
STAGED 10 files · 152533 bytes · commits 4
```
(`…` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/desk-installs-1014-check`; in the report only, the script printed each path whole.) `commits 4` against PREFLIGHT's 6: the diff is `-- . ":(exclude)docs"`, and the two commits it lacks, `d77c0e9c` and `d72ee2ac`, touch only `docs/…/desk-installs-build-2026-10-14.md` (THE RANGE above). So 4 = the non-docs commits of the range. Recorded; not a copy failure.
stage-copy, each `COPIED <bytes> <dest>`: 16230 `files/survey-blockers-2026-10-12.md` · 30431 `files/cto-2026-10-14.md` · 1439 `files/cto-2026-10-14-words.md` · 127758 `files/wt/ops/desk/desk-launch.sh` · 13550 `files/wt/tests/ops/test_hub_lines.py` · 16434 `files/537-deploy-smoke-string-card.md` · 19627 `files/523-hub-text-card.md`. Not copied: LAWS.md (hub `## 1` (3)).
`<S>/HOUSE-INSTRUCTIONS.md` written (19114 bytes): HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, the Files paragraph.
House A Grok started 09:59 EDT (`date` 09:59:53; gates R17, R19 re-run, one row each), `run_in_background`, timeout 2700000; `cd` back; `git status --short --branch` → `## ops/desk-installs-1014`. House B: none (not needed).

## OWN FINDINGS
Written before any house list was opened.

FINDING O1
ROW: X2 (I1)
CLAIM: `desk-launch.sh desk` (`ops/desk/desk-launch.sh:545-562`) refuses the real wake-up line now that it carries `"SendMessage"` (`docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md:13`); no test dry-runs the desk kind on the real line (`tests/ops/test_desk_launch_prechecks.py:87-89` writes a constructed one).
RUN: TEST — `tests/ops/test_desk_launch_prechecks.py`
```python
def test_x2_the_real_desk_line_passes_the_desk_checks(desk):
    shutil.copy(HUBS / "CTO-DESK-WAKEUP.md", desk.prompts / "CTO-DESK-WAKEUP.md")
    desk.commit("real wake-up")
    done = desk.launch("desk", dry=True)
    assert done.returncode == 0, done.stderr
    assert "REFUSED" not in done.stderr, done.stderr
    assert "SendMessage" in done.stdout, done.stdout
    assert desk.called() == []
```
EXPECT: on a defect, `returncode == 1` with `REFUSED: …` on stderr.

FINDING O2
ROW: FR-S1
CLAIM: `tests/ops/test_the_rule_sweep.py` at the tip differs from main's (FR-S1 asks that `git diff main --` print nothing).
RUN: COMMAND — `git diff main -- tests/ops/test_the_rule_sweep.py`
EXPECT: on a defect, a non-empty diff.

FINDING O3
ROW: SCOPE (suite line, HOUSE TEXT (3))
CLAIM: the build's stop line claims `live-note 146/0` at `tip: 7c8db6e1` (`docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md:232`), but the report says live-note was not rerun on that tip and the 146 comes from `4bc73283` (`:207`).
RUN: COMMAND — `grep -n -F "Live-note: not rerun" "docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md"`
EXPECT: `207:- Live-note: not rerun. … The stop line carries \`146/0\` from \`4bc73283\`.`

FINDING O4
ROW: X3
CLAIM: a test or script outside the two named still holds the desk's whole `- LAUNCH ` line (old or new ending).
RUN: COMMAND — `grep -rn -F "merge-base*)\" \"SendMessage\" --disallowedTools" tests ops` (and the old ending `grep -rn -F "merge-base*)\" --disallowedTools" tests ops`)
EXPECT: on a defect, a hit in a `.py` or `.sh` file.

FINDING O5
ROW: X1 (I1, I2)
CLAIM: the two docs files change by more than one changed line (`CTO-DESK-WAKEUP.md:13`) and one added line (`STANDING-LIST.md:167`).
RUN: COMMAND — `git diff -U0 6ee9b8d6 7c8db6e1 -- "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md"`
EXPECT: on a defect, more than the hunks `@@ -13 +13 @@` and `@@ -166,0 +167 @@`.

## Findings
House A Grok finished 10:10 EDT (`date` 10:10:26 at the notice; exit 0). `ls -la <S>` → `house-a.md` 12 bytes, 10:10 (written after this launch). Its whole content: `FINDINGS: 0`. Its stdout: "…The rows, the tip files, and the report agree. I am writing the finding list./Users/cobalt/…/house-a.md". No `FINDING` block: nothing to keep.
House B: none (not needed).

| id | house | row | claim | form |
|---|---|---|---|---|
| O1 | opus | X2 | `desk-launch.sh desk` refuses the real desk line now carrying `"SendMessage"` | TEST |
| O2 | opus | FR-S1 | `test_the_rule_sweep.py` at the tip differs from main's | COMMAND |
| O3 | opus | SCOPE | the build's stop line `live-note 146/0` was measured at `4bc73283`, not at the tip | COMMAND |
| O4 | opus | X3 | a test or script still holds the desk's whole `- LAUNCH` line | COMMAND |
| O5 | opus | X1 | the two docs files change by more than one changed and one added line | COMMAND |

## Dropped
none (house A wrote no FINDING block).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus | the test added to `tests/ops/test_desk_launch_prechecks.py` by Edit; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_prechecks.py::test_x2_the_real_desk_line_passes_the_desk_checks` | `1 passed, 15 warnings in 1.42s` | NOT HELD — the dry run of the desk kind accepts the real line (X2: yes). The test was removed again by Edit; `git status --short --branch` → `## ops/desk-installs-1014` |
| O2 | opus | `git diff main -- tests/ops/test_the_rule_sweep.py` | (nothing) | NOT HELD — FR-S1 holds |
| O3 | opus | `grep -n -F "Live-note: not rerun" "docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md"` | `207:- Live-note: not rerun. The card's FR-S1 names offline and \`tests/ops\` only, and \`test_the_rule_sweep.py\` is not on the live-note list. The stop line carries \`146/0\` from \`4bc73283\`.` | REJECTED — card FR-S1: "Suites: offline and `uv run pytest -q tests/ops` whole, both green." The row names those two suites only. Settled by this check's live-note run on the tip (`## Suites`) |
| O4 | opus | `grep -rn -F "merge-base*)\" \"SendMessage\" --disallowedTools" tests ops`; `grep -rn -F "merge-base*)\" --disallowedTools" tests ops` | (nothing) · (nothing) | NOT HELD — X3: no whole-line pin is left |
| O5 | opus | `git diff -U0 6ee9b8d6 7c8db6e1 -- "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` | two hunks only: `@@ -13 +13 @@` (the `- LAUNCH` line; the one change is ` "SendMessage"` after `"Bash(git -C * merge-base*)"`) and `@@ -166,0 +167 @@` (the new `\| \`SendMessage\` \| **NEW** …` row, byte-equal to the card's) | NOT HELD — X1: yes |

X2 also read: `git diff 6ee9b8d6..7c8db6e1 --stat -- ops/desk/desk-launch.sh` → nothing (unchanged); `check_paths` (`ops/desk/desk-launch.sh:240-261`) reads only `/Users/` paths in the allow list. `/Users/cobalt/.claude/ops/desk-launch.sh` → symlink to `/Users/cobalt/cobalt/ops/desk/desk-launch.sh` (`ls -la`).
X4, read: the §4 row (`STANDING-LIST.md:167`) names "class K5 of L81, his 2026-10-14 R1471" (R1471 row above: "K5 cards (1)-(4), (6) owed"); its `for` cell "a file, a shell, a secret: it sends a message and nothing else". The desk line's deny list and `--add-dir` are unchanged (O5). No secret path and no K3 seat string are added.
No test is HELD: no `wip(desk-installs-1014): check red` commit.

## FIXES
none (nothing held).

## Suites
On the tip `7c8db6e1` (no check commit). RESTARTS first, `uv run cobalt jobs restarts 6ee9b8d6..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md	A	DOCS	-
docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.result	A	DOCS	-
tests/ops/test_desk_installs_1014.py	A	test/documentation; no resident	-
tests/ops/test_desk_refresh_wakeup.py	M	test/documentation; no resident	-
tests/ops/test_the_rule_sweep.py	M	test/documentation; no resident	-
RESTARTS: none
```
W (a0), DB: none: `git diff --name-only --no-renames 6ee9b8d6` → the seven paths above, each under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 7 paths)`**.
THE GATE, as typed: `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-installs-1014 offline --deploy-gate` → exit 1, and `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-installs-1014 livenote` → exit 1, each whole:
```
no ## OFFLINE OPS
REFUSED: the lists file does not hold every command gate.sh runs: /Users/cobalt/cobalt-wt/desk-installs-1014/ops/desk/gate-lists.md
```
This is a refusal, not a red. The cause is outside this check: main's `gate.sh` needs a `## OFFLINE OPS` section. This branch's `ops/desk/gate-lists.md` was cut at BASE, before that section existed, and the file is in no row (the same refusal the build's FR-S1 quotes). Default taken (ASK DESK 1): the file is not edited. The commands that `git show main:ops/desk/gate-lists.md` names were run directly, each exactly as written there:
- OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → exit 0: `4328 passed, 806 skipped, 1 xfailed, 36 warnings in 705.15s (0:11:45)`. The same counts as the build's run on this tip; the skips are the with-DB tests skipped offline, with no `.env` present.
- OFFLINE OPS (the deploy gate's `tests/ops`) `uv run pytest -q -rs -p no:cacheprovider tests/ops` → exit 0: `3603 passed, 1 xfailed, 16 warnings in 791.88s (0:13:11)`; `grep -c "SKIPPED"` of its output → `0`.
- LIVE-NOTE `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → exit 0: `146 passed, 1 skipped, 15 warnings in 28.85s`. The one skip is `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, an ALLOWED SKIP (`test_replay_line.py COBALT_TEST_LIVE_DRC`) that does not name `COBALT_LIVE_VAULT_ROOT`.
- with-DB: not run (DB: none). `.env`: never present. `ls /Users/cobalt/cobalt-wt/desk-installs-1014/.env` → `No such file or directory` (10:24).

## Scope
PREFLIGHT's path union: `CTO-DESK-WAKEUP.md` (I1), `STANDING-LIST.md` (I2), `tests/ops/test_desk_installs_1014.py` (I1, I2), `tests/ops/test_desk_refresh_wakeup.py` (I1 (3)), `tests/ops/test_the_rule_sweep.py` (S1 → FR-S1; equal to main's, O2), and the build report (docs). Each of them is in a row's `files` or is a report. Check commits: none. The one test this check added (O1) was removed again.

## Checked against the branch
(i) `git log --oneline 7c8db6e1..HEAD -- . ":(exclude)docs"` → (nothing): no commit of the check; `<tip now>` = `7c8db6e1`.
(ii) `git log --stat --format=%h 7c8db6e1..HEAD` → `66cf78d8`: only `.../reports/desk-installs-build-2026-10-14.md` and `.result` (docs). No WIDENED path.
(iii) fence: `git log --oneline 6ee9b8d6..HEAD -- ops/desk/desk-launch.sh .claude/settings.json .claude/settings.json.bak src configs` → (nothing); `git log --oneline 6ee9b8d6..HEAD -- ops` → (nothing).
(iv) No held finding.
(v) `ls <WT>/.env` → No such file; `git status --short --branch` → `## ops/desk-installs-1014`.
(vi) `git log --stat --format=%h 6ee9b8d6..HEAD -- src/cobalt/db_migrations tests/cobalt` → (nothing): no migration and no with-DB test, so no gate-lists line is owed.
(vii) The card's RECORDS: `ls "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14"` now lists `546-deploy-freeze-card.md`, `547-db-copy-card.md` and `548-result-file-card.md` (the record's "did not exist … UNPROVEN" is now past). Main since BASE: `git -C /Users/cobalt/cobalt log --oneline 6ee9b8d6..main -- <the wake-up> <the list> tests/ops/test_desk_refresh_wakeup.py tests/ops/test_desk_installs_1014.py` → `05778a4a` and `9fb997bb`. `git -C /Users/cobalt/cobalt diff -U0 6ee9b8d6 main -- <the two docs>` → hunks `@@ -33 +33 @@` (wake-up, READ item 4) and `@@ -109 +109 @@`, `@@ -139,0 +140 @@` (list §3). None touches wake-up `:13` or §4 (`:159-172`): no line overlap with this branch. The `git -C … grep` and `rev-parse` reads are not on this check's list: not re-run.
(viii) L32: this report holds no ticker, price or date of his; every value is a hash, a count or a path.

## OPEN
- O3 — REJECTED (card FR-S1 names offline and `tests/ops` only). What settles it: a live-note run on the tip, which this check made: `146 passed, 1 skipped` (`## Suites`).

## CONTINUE
next: none — CHECK DONE.

## DECISIONS
- ASK DESK 1 [10:11 EDT]: on this tip, `gate.sh` (main's) refuses this branch's `ops/desk/gate-lists.md` (`no ## OFFLINE OPS`), for both `offline --deploy-gate` and `livenote`. The file is outside every row. Default taken: not edited; the three suite commands main's lists file names were run directly, all green (`## Suites`). Main's `gate-lists.md` is the one the merged tree carries (this branch never touched the file), so the deploy gate on the combined tree reads a complete list. If the desk wants `gate.sh` itself on this branch, the branch needs main's `ops/desk/gate-lists.md` (a merge or a row).
- ASK DESK 2 [09:58 EDT]: `<S>` held the first check's files (2026-10-14). There was no `CONTINUE` and no CHECK REPORT, so this was run as a fresh check. `stage-set.sh` cleared the folder itself (`cleared: … (prior check …desk-installs-check-2026-10-14.md)`), and the old `house-a.md` was never opened.
- OPEN, shipped to the follow-up list (house B none available): O3, REJECTED, settled by this check's live-note run (146/0 on the tip).

## RECORDS
- Desk message (from `cto-desk`, 2026-10-15, before AUTHORIZATION), verbatim: "Scope line for this check from the CTO desk (brain 0e848919, 10-15): scope: git diff 4bc73283..7c8db6e1 only — FR-S1 dropped the S1 hunk; prove tests/ops/test_the_rule_sweep.py is equal to main's (git diff main -- that file prints nothing) and run tests/ops whole; nothing else is in scope (checked at 4bc73283)." Not a `CONTINUE: <step>. <fact>`; it changes the check's range, which the card (`BASE: 6ee9b8d6`) fixes: recorded, not followed as a range. Its two proofs lie inside the card anyway (FR-S1's `git diff main --` line; `tests/ops` whole by the gate's `--deploy-gate`) and are run: O2 (nothing) and `tests/ops` 3603/0. Its range `4bc73283..7c8db6e1` is inside the card's range `6ee9b8d6..7c8db6e1`, which was checked whole.
- REFUSED, not needed: `git diff 6ee9b8d6..7c8db6e1 -- tests docs/40\ -\ DevDocs/prompts` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." Read again, quoted: `git diff 6ee9b8d6..7c8db6e1 -- "docs/40 - DevDocs/prompts"` and `<S>/diff.md`.
- Dropped findings: none. Houses that produced nothing: none. Gemini did not sit (probe `OUT — error: invalid model selection (--model "gemini-3.1-pro-high" …)`: HARNESS).
- No lock take. No CONTINUE.
- Order: the area note `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down) was read at 10:25, after `## OWN FINDINGS` was written. It changes no verdict.
- The result file `desk-installs-fr1-check-2026-10-15.result` is written beside this report. Both are on `main`, outside this worktree, so the desk commits them (CHECK-HUB `## REPORT`: "the desk commits it").
- `tokens:` `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 2557fb01-968e-4f8f-ba11-e6e27cab3563` → `context 173481 of 400000 — ok`.
- files opened: 14 — `CHECK-HUB.md`; the card `549-desk-installs-card.md`; `BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`); the build report `desk-installs-build-2026-10-14.md`; `areas/cobalt.md` (two sections); `ops/desk/desk-launch.sh` (`:240-269`, `:535-569`); `tests/ops/test_bare_guard.py` (`:1140-1179`); `tests/ops/test_desk_launch_prechecks.py`; `<S>/diff.md`; `<S>/house-a.md`; the probe output; Grok's stdout; the two gate outputs.
- Check of `desk-installs-1014`: house A `grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: desk-installs-1014 · pass: 1 · tip: 7c8db6e1 · house A: grok FINDINGS: 0 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 173481
