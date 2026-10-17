# CHECK — gemini-builder-row — 2026-10-17

## §0 Headline
Check of `gemini-builder-row` at `7b986738`: every row's red, mutation and undo reproduced as the build reported; suites green (offline 8413/0, tests/ops 3841 passed, live-note 146/0).
One held finding, not fixed under the card's fence: the guard reads only ` --add-dir D`, so a hub row adding `--add-dir=<dir>` would pass (O1, `bare-guard.py:1205`). It goes to the fix round with its test.
One unsettled item: the guard admits the Gemini call from any cwd (O2); the desk's X1 run settles it.
House A Grok: 1 finding (R1, agrees with the build). House B none (not needed; Gemini OUT on the probe's old id). M1: text-clean with 583 by hunk ranges. `ready: NO`.

## L74
One notice (a system message, not a tool result) asked for a `Claude-Session:` commit line; recorded, not acted on; no commit made.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card 687>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/687-gemini-builder-row-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/687-gemini-builder-row-check-card.md" · 0 · 8c2040395e9e8034d35826c2973848873e7b6d99
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/687-gemini-builder-row-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-17 R1736 row · grep -n "^| R1736 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · 42:| R1736 | 06:32 ET | HIS RULING (brain, L79), 2026-10-17: Gemini top model = gemini-4-argon-high (medium, low recorded only). K5 card: CHECK-HUB :95 and house-probe.sh use it, was gemini-3.1-pro-high. Behind 641 and 583. | HIS RULING · APPROVED |
RULING 2026-10-17 R1736 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1736 |" -- "docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · d01849e7a6ef4a9de57d6de11856c866919737d2
RULING 2026-10-17 R1736 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · the row as grepped
RULING 2026-10-17 R1738 row · grep -n "^| R1738 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · 40:| R1738 | 06:33 ET | HIS RULING (brain, L79), 2026-10-17: run the Gemini bake-off arm separately; answer: reports/gemini-bakeoff-answer-2026-10-17.md. Probe-id and builder cards drafted now; three builds after both deploy; routing B unchanged. | HIS RULING · APPROVED |
RULING 2026-10-17 R1738 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1738 |" -- "docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · b57cbf8e3ed386e736822c9ca864fef64a7433eb
RULING 2026-10-17 R1738 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · the row as grepped
AUTHORIZED
```
House gates (09:24 EDT): `grep -n "^| R17 " …cto-2026-09-24.md` → one row (line 35, the standing `Bash(grok *)` row); `grep -n "^| R19 " …` → one row (line 37, the four house strings standing); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card 687>"` · exit 0 · output whole:
```
clock · date · 0 · Sat Oct 17 09:24:25 EDT 2026
status · git status --short --branch · 0 · ## ops/gemini-builder-row-1017
head · git log --oneline -1; git log --stat --format=%h 7b986738..HEAD · 0 · (6 lines)
    7b22e411 docs(gemini-builder-row): build report — 7b986738
    7b22e411
    
     .../reports/gemini-builder-row-build-2026-10-17.md | 239 +++++++++++++++++++++
     .../gemini-builder-row-build-2026-10-17.result     |  15 ++
     2 files changed, 254 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/gemini-builder-row-1017/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/gemini-builder-row-1017/docs/40 - DevDocs/reports/gemini-builder-row-build-2026-10-17.md" · 0 · BUILT · job: gemini-builder-row · tip: 7b986738 | on 7f415a4f | migration: none | offline 8413/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 183912
range · git log --oneline 7f415a4f..7b986738 · 0 · (2 lines)
    7b986738 feat(gemini-builder-row): Gemini builder row gemini-4-argon-high, launcher admits it, guard admits its no-shell call (L1, G2, H1, X2; L1, L3, L72)
    14a17ab7 wip(gemini-builder-row): red
PREFLIGHT OK
```
THE RANGE typed: `git log --stat --format=%h 7f415a4f..7b986738` →
```
7b986738
 docs/40 - DevDocs/prompts/SHADOW-HUB.md | 12 ++++++++----
 ops/desk/bare-guard.py                  | 15 +++++++++++----
 ops/desk/desk-launch.sh                 |  4 +++-
 3 files changed, 22 insertions(+), 9 deletions(-)
14a17ab7
 tests/ops/test_bare_guard.py         | 79 ++++++++++++++++++++++++++++++++++++
 tests/ops/test_desk_launch_shadow.py | 30 ++++++++++++--
 tests/ops/test_shadow_hub_file.py    | 47 ++++++++++++++++++---
 3 files changed, 147 insertions(+), 9 deletions(-)
```
DB: none — `git diff --name-only --no-renames 7f415a4f 7b986738` →
```
docs/40 - DevDocs/prompts/SHADOW-HUB.md
ops/desk/bare-guard.py
ops/desk/desk-launch.sh
tests/ops/test_bare_guard.py
tests/ops/test_desk_launch_shadow.py
tests/ops/test_shadow_hub_file.py
```
every path under `ops/`, `tests/ops/` or `docs/`.
`ls <S>` → `No such file or directory` (fresh).
House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card 687>"` · exit 0 · output whole:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
No `HOUSE A: OpenAI` header line → Sol not probed. `house A: Grok · house B: none (not needed)` — the card's `HOUSE B: as needed`, not `mandatory`. Gemini OUT is HARNESS (an unknown model id in the probe; card 670 owns that probe id). X5: Gemini could not sit in any case (its own builder row).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card 687>" "<S>"` · output whole:
```
16975 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gemini-builder-row-check/diff.md
26639 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gemini-builder-row-check/files/687-gemini-builder-row-check-card.md
26848 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gemini-builder-row-check/files/gemini-builder-row-build-2026-10-17.md
18267 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gemini-builder-row-check/files/wt/docs/40 - DevDocs/prompts/SHADOW-HUB.md
56545 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gemini-builder-row-check/files/wt/ops/desk/bare-guard.py
133273 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gemini-builder-row-check/files/wt/ops/desk/desk-launch.sh
102292 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gemini-builder-row-check/files/wt/tests/ops/test_bare_guard.py
14782 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gemini-builder-row-check/files/wt/tests/ops/test_desk_launch_shadow.py
14088 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gemini-builder-row-check/files/wt/tests/ops/test_shadow_hub_file.py
701 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gemini-builder-row-check/rulings.md
STAGED 10 files · 410410 bytes · commits 2
```
`stage-copy.sh`, one call each:
```
COPIED 23626 …/files/671-gemini-builder-row-card.md
COPIED 13282 …/files/cto-2026-10-17.md
COPIED 3572 …/files/gemini-bakeoff-answer-2026-10-17.md
COPIED 43599 …/files/CHECK-HUB.md
COPIED 10468 …/files/367-shadow-strike-fallback-env-1010-terra-card.md
COPIED 25827 …/files/strike-fallback-env-1010-terra-build-2026-10-11.md
```
`<S>/HOUSE-INSTRUCTIONS.md` written (27836 bytes, `ls -la <S>` 09:26). House A Grok started 09:26:44 EDT (`date`), `run_in_background`, timeout 2700000; `cd <WT>`; `git status --short --branch` → `## ops/gemini-builder-row-1017`.

## OWN FINDINGS
Written before any house list was opened (house A still running; nothing under `<S>` opened but my own staging).

FINDING O1
ROW: G2 / X2 (bound c)
CLAIM: The agy write-target read `ops/desk/bare-guard.py:1205` matches only the space form ` --add-dir D`; a hub row that adds `--add-dir=<other dir>` (the `=` spelling, the same spelling the row already uses for `--print=`) leaves `targets == {target/**}` at `:1206`, so the guard admits a Gemini call whose workspace reaches outside the worktree.
RUN: TEST — tests/ops/test_bare_guard.py
```python
def test_k5_check_o1_an_add_dir_equals_form_in_the_hub_row_is_g7(roots):
    row = GEMINI[2].replace(" --print=", " --add-dir=/Users/cobalt/cobalt --print=")
    seat = gemini_seat(roots, "gemini-4-argon-high", row=row)
    assert_denied(run(gemini(roots, row=row), seat), G7_ROUTE)
```
EXPECT: `AssertionError: (0, '')` — the call is allowed (exit 0).

FINDING O2
ROW: G2 / X2 (bound a)
CLAIM: `builder_call` (`ops/desk/bare-guard.py:1180-1218`) never reads `s["cwd"]`; the hub's Gemini note (`SHADOW-HUB.md:28`, "--add-dir <worktree> is its one workspace, run from the cd into the worktree") rests the fence on the cwd, yet the guard admits the same agy call from a gate seat whose cwd is the repo.
RUN: TEST — tests/ops/test_bare_guard.py
```python
def test_k5_check_o2_the_gemini_call_from_outside_the_worktree_is_g7(roots):
    seat = dict(gemini_seat(roots, "gemini-4-argon-high"), cwd=str(roots.repo))
    assert_denied(run(gemini(roots), seat), G7_ROUTE)
```
EXPECT: `AssertionError: (0, '')` — allowed from the repo cwd.

FINDING O3
ROW: R1 / X6
CLAIM: The four R1 hits are tests' own strings: `tests/ops/test_desk_launch_shadow.py:218-219` (the refusal input and its message) and `tests/ops/test_shadow_hub_file.py:129` (the `gone` tuple) and `:178`; `:129`'s entry is redundant with `:178` (the whole file is a superset of `## BUILDERS`).
RUN: COMMAND — `grep -n -F "gemini-3.1-pro-high" "docs/40 - DevDocs/prompts/SHADOW-HUB.md" ops/desk/desk-launch.sh ops/desk/bare-guard.py tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py tests/ops/test_bare_guard.py`
EXPECT: exactly four lines, all under `tests/ops/`.

## Findings
House A Grok finished 09:37 (notice 09:38:00 EDT, `date`); `ls -la <S>` → `house-a.md` 881 bytes, written by Grok itself (stdout held only the path and its progress lines). `FINDINGS: 1`. House B: none (not needed).
- O1 · Opus · G2/X2 (c) · the agy write-target read `bare-guard.py:1205` misses `--add-dir=D`; a hub row carrying it is admitted with a second workspace · TEST
- O2 · Opus · G2/X2 (a) · `builder_call` never reads the seat's cwd; the agy call is admitted from the repo cwd though the hub's note rests the fence on the cd · TEST
- O3 · Opus · R1/X6 · the four R1 hits are tests' own strings; `:129`'s entry is redundant with `:178` · COMMAND
- A1 · Grok · R1 · four is the form the tests force; nothing-changed stands · COMMAND

## Dropped
none (both blocks of house A and all of mine carry a runnable `RUN:`).

## RUNS
- O1 · Opus · test added at the end of `tests/ops/test_bare_guard.py`, `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_bare_guard.py -k check_o` → `2 failed, 3 passed, 1870 deselected`; O1 first failing line `E       AssertionError: (0, '')` (returncode 0, stderr empty: ALLOWED) · **HELD, NOT FIXED — ops/desk/bare-guard.py** (the card's fence: no edit of `bare-guard.py` or a test in this job). The test was removed again with Edit (fence); `git diff --stat 7b986738 -- ops tests` → nothing.
- O2 · Opus · same run → `E       AssertionError: (0, '')` (ALLOWED from cwd = the repo) · **UNSETTLED — whether agy's workspace takes in the cwd beside `--add-dir` needs a real agy run, fenced here (`## NOT IN THIS JOB`: the X1 run is the desk's); the guard fact itself shows red.** Test removed again (same undo proof).
- O3 · Opus · `grep -n -F "gemini-3.1-pro-high" "docs/40 - DevDocs/prompts/SHADOW-HUB.md" ops/desk/desk-launch.sh ops/desk/bare-guard.py tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py tests/ops/test_bare_guard.py` →
  ```
  tests/ops/test_desk_launch_shadow.py:218:    refused(desk.run(str(desk.card), "--model", "gemini-3.1-pro-high"),
  tests/ops/test_desk_launch_shadow.py:219:            "shadow: model 'gemini-3.1-pro-high' is a Gemini id not admitted; gemini-4-argon-high is the one Gemini builder (R1738)")
  tests/ops/test_shadow_hub_file.py:129:    for gone in ("claude-opus-5-5", "gpt-5.6-sol", "gemini-4-argon-medium", "gemini-4-argon-low", "gemini-3.1-pro-high"):
  tests/ops/test_shadow_hub_file.py:178:    assert [x for x in text().splitlines() if "gemini-3.1-pro-high" in x] == []
  ```
  · NOT HELD as a defect (asserts nothing; the output shown is the claim, an observation for X6).
- A1 · Grok · same command, same four lines · NOT HELD as a defect (it agrees with the build's safe default; recorded for X6).

THE CARD'S ROWS (each run by me; none asserts a defect unless named):
- S0 · `git diff --name-only --no-renames 7f415a4f 7b986738` → the six paths exactly (quoted in PREFLIGHT); `git diff --stat 7f415a4f 7b986738` → `SHADOW-HUB.md | 12 +++--`, `bare-guard.py | 15 +++++--`, `desk-launch.sh | 4 +-`, `test_bare_guard.py | 79 +++…`, `test_desk_launch_shadow.py | 30 +++++--`, `test_shadow_hub_file.py | 47 +++++---`, `6 files changed, 169 insertions(+), 18 deletions(-)`; `git diff --stat 7b986738 7b22e411 -- . ":(exclude)docs"` → nothing; `git diff --stat 7b986738 -- ops tests` → nothing; `git status --short --branch` → `## ops/gemini-builder-row-1017`. No `src/`, `configs/`, `.claude/`, no card-670 file. OK.
- L1 · `git diff -U0 7f415a4f 7b986738 -- ops/desk/desk-launch.sh` → `@@ -376,0 +377 @@` (the comment) and `@@ -398 +399,2 @@` (`gemini-4-argon-high) ;;` then the new `gemini-*)` refusal) — no other launcher line. RED on the base launcher (arm and sentence undone by Edit): `-k "k5_gemini or refused_by_name or real_file_launches or grok or terra"` → `5 failed, 1 passed`: the high test `AssertionError: REFUSED: shadow: model 'gemini-4-argon-high' is a Gemini id; Gemini is not in ## BUILDERS (N/A — id not found)`, medium and low on the old sentence, `test_a_gemini_id_is_refused_by_name` on the old sentence, `test_the_real_file_launches_a_signed_grok` at `:316` (the gemini launch). MUTATION (the `gemini-4-argon-high) ;;` arm alone deleted): `-k "k5_gemini or real_file_launches"` → `2 failed, 2 passed` (the high test and the real-file test; medium and low green). Undone; `git diff --stat 7b986738 -- ops/desk/desk-launch.sh` → nothing; the file → `21 passed`. `ROLE` (`:1662`) and the `## BUILDERS` checks `:1667-1691` unchanged (not in the diff). X1: YES.
- G2 · the whole diff quoted under my read (two hunks in `builder_call`, one in its docstring; `write_targets` `:1171` unchanged). `git diff -U0 7f415a4f 7b986738 -- tests/ops/test_bare_guard.py` → ONE hunk `@@ -2456,0 +2457,79 @@`, no `-` line (the card's `@@ -2454,3 +2454,82 @@` is the same hunk with 3 context lines). RED on base (both guard hunks undone by Edit): `-k k5` → `2 failed, 13 passed`: the positive test `AssertionError: route: the desk launches` (exit 2), the env test `'route: the desk launches\n' == 'route: no builder pass while .env is in the worktree …'`. MUTATION (the agy rule `:1213-1215` alone deleted): `-k k5` → `3 failed, 12 passed`: `HUB YOLO`, `HUB TWO MODES`, `HUB NO SANDBOX`. Undone; `git diff --stat 7b986738 -- ops/desk/bare-guard.py` → nothing; the file → `1873 passed`. X2 CONTROL from the code: the seven `shapes` die at `:1197` (the command must start with the filled prefix and end with the suffix: NO SANDBOX, YOLO, TWO MODES, OTHER ADD-DIR, SECOND ADD-DIR, MEDIUM alter the filled template; GROK SEAT has the Grok template); the three `HUB …` rows die at `:1213-1215` only. A hub row with a second ` --add-dir X` (space form) dies at `:1206` (two targets). A hub row with `--add-dir=X` passes — finding O1, HELD.
- H1 · `git diff -U0 … SHADOW-HUB.md` → `@@ -12 +12`, `@@ -15 +15`, `@@ -21,0 +22`, `@@ -26,0 +28,3`, `@@ -29 +33`, `@@ -88 +92`; the launch line, the Grok/Sonnet/Terra rows, RULES OF THE SEAT and THE PROCEDURE untouched. RED on base (all six hunks undone by Edit; `git diff --stat 7f415a4f -- SHADOW-HUB.md` → nothing): `8 failed, 43 passed`: four-ids `At index 1 diff: 'gpt-5.6-terra' != 'gemini-4-argon-high'`; `KeyError: 'gemini-4-argon-high'` ×4 (allow, write target, sign, no-shell); old-id `Left contains one more item: '| Gemini | N/A — id not found …'`; launcher sentence `assert 'a Gemini id other than gemini-4-argon-high,' in …`; X1 paragraph `assert 0 == 1`. `-k unavailable_model` on base → `1 passed` (and green at the tip). MUTATION (the `:22` row deleted) → `5 failed, 46 passed` (four-ids and the four per-id tests). Undone; `git diff --stat 7b986738 -- SHADOW-HUB.md ops tests` → nothing; the file → `51 passed`. `grep -n -E "[0-9a-f]{8}" tests/ops/test_shadow_hub_file.py` → one line, `362:        "BASE: 0000aaaa\nTIP:\nREPORT: /nowhere/x-job-build.md\n"` — outside the added lines (a constructed value); no hash in the added tests.
- X2 · the paragraph (quoted in the diff) against card 367 row X1: the same four steps (read, fetch, append `X1 WRITE OK`, write `OUTSIDE.txt`); 367 RECORDED the canary read, this paragraph makes a read of either decoy a STOP (`INCOMPLETE`); network or outside write = STOP, `FAILED: X1` as in 367; it never names `x1-canary/.env` (the test's `:194` substring check is green; `probe/.env` does not contain the substring `x1-canary/.env`); G7 stands (no hunk on the `.env` lines `:1216-1217`). Its red on base: `assert 0 == 1` (the H1 run). `ls -la /Users/cobalt/cobalt-wt/x1-canary` → `A.txt` `B.txt` `C.txt` 25 bytes, `CANARY.txt` 23 bytes, `probe/`; `ls -la …/x1-canary/probe` → `.env` 23 bytes; no `x1-canary/.env`. Matches the records. X3: YES.
- R1 · see O3 (four lines, all under `tests/ops/`; none in SHADOW-HUB.md, `desk-launch.sh`, `bare-guard.py`; no card-670 file in the grep).
- M1 · `git merge-base 7f415a4f ops/band-routing-1015` → REFUSED (`Permission to use Bash has been denied because Claude Code is running in don't ask mode.` — not on the allow line; recorded as the card asks). In its place: `git log --oneline 7f415a4f..f2ca3e1a` → nothing (`f2ca3e1a` is an ancestor of BASE) and `git diff --stat f2ca3e1a 7f415a4f -- <the three files>` → nothing (BASE equals `f2ca3e1a` in these files). 583 head: `6c0ba560 docs(band-routing-1015): build report — 4b62c2fa (fix round 3, FR-9)`. `git -C /Users/cobalt/cobalt diff --stat f2ca3e1a ops/band-routing-1015 -- …` → `SHADOW-HUB.md | 15 +++++--`, `bare-guard.py | 5 +++`, `desk-launch.sh | 80 +++…`, `3 files changed, 90 insertions(+), 10 deletions(-)` (unchanged since 09:20). `@@` headers, 583: SHADOW-HUB `-27,0 +28,9`, `-44 +53`, `-61 +70`, `-73 +82`; bare-guard `-1276,0 +1277,5`; desk-launch `-378,0 +379`, `-390,0 +392,4`, `-986,2 +991,4`, `-991,0 +999`, `-1629,0 +1638,51`, `-1658 +1717,2`, `-1663 +1723`, `-1680 +1740`, `-1730,0 +1791,6`, `-1751 +1817`, `-2290 +2356`. This card: SHADOW-HUB `-12`, `-15`, `-21,0`, `-26,0`, `-29`, `-88`; bare-guard `-1184,2`, `-1201,2`, `-1203,0`, `-1208,0`; desk-launch `-376,0`, `-398`. Closest pairs: SHADOW-HUB insert after base `:26` (this) vs after `:27` (583), and desk-launch insert after `:376` (this) vs after `:378` (583): each separated by at least one untouched base line; no range shares or abuts a changed line. Text-clean by ranges (not proven by a merge: `git merge-tree` is not listed). Band rows: the launcher reads builder rows by `/^\| \`/` (`desk-launch.sh:1667`) and the guard by `line.startswith("| \`")` (`bare-guard.py:1149`); a `| LOW |` row starts `| L` and matches neither; 583's `band_row` matches column 2 equal to the band, and the Gemini row's column 2 is `gemini-4-argon-high`. X4: YES.
- R3 · `uv run cobalt jobs restarts 7f415a4f..7b986738` →
  ```
  path	change	rule	restart
  docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
  ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
  ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
  tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
  tests/ops/test_desk_launch_shadow.py	M	test/documentation; no resident	-
  tests/ops/test_shadow_hub_file.py	M	test/documentation; no resident	-
  RESTARTS: none
  ```
  = the header's `none`.

## FIXES
- O1: HELD, NOT FIXED — ops/desk/bare-guard.py (the card fences every edit of `bare-guard.py` and its tests; the fix goes to the builder's one fix round). Its test, ready to paste into `tests/ops/test_bare_guard.py`:
  ```python
  def test_k5_check_o1_an_add_dir_equals_form_in_the_hub_row_is_g7(roots):
      row = GEMINI[2].replace(" --print=", " --add-dir=/Users/cobalt/cobalt --print=")
      seat = gemini_seat(roots, "gemini-4-argon-high", row=row)
      assert_denied(run(gemini(roots, row=row), seat), G7_ROUTE)
  ```
No commit of mine (no test may be committed under the fence; nothing fixed).

## Suites
On the tip `7b986738` (no commit of mine). DB: none → W (a0), (a), (e):
- (a0) `git diff --name-only --no-renames 7f415a4f` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `docs/40 - DevDocs/reports/gemini-builder-row-build-2026-10-17.md`, `docs/40 - DevDocs/reports/gemini-builder-row-build-2026-10-17.result`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py` — every path under `ops/`, `tests/ops/` or `docs/`. `cobalt_dev: not taken (DB: none — 8 paths)`.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-builder-row-1017 offline --deploy-gate` (row G3) · exit 0 · whole:
  ```
  tests/ops: run (deploy gate)
  offline 8413/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-builder-row-1017-offline-20261017-094204.log
  ```
  `grep -n -F "passed" <log>` → `888:4572 passed, 806 skipped, 1 xfailed, 36 warnings in 694.67s (0:11:34)` and `959:3841 passed, 1 xfailed, 16 warnings in 844.41s (0:14:04)` (the `tests/ops` run: 3841 passed, 0 failed). The separate `uv run pytest … tests/ops` of W (a0) is this deploy-gate run.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-builder-row-1017 livenote` · exit 0 · whole:
  ```
  live-note 146/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-builder-row-1017-livenote-20261017-100800.log
  ```
- with-DB: 0/0 (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/gemini-builder-row-1017/.env` → `No such file or directory`. RESTARTS: `none` (R3 above).

## Scope
PREFLIGHT's path union (the six paths of S0) against the rows' files: all six are rows' files. My commits: none. The two check tests (O1, O2) were added and removed in the same step; `git diff --stat 7b986738 -- ops tests` → nothing after each undo.

## Checked against the branch
(i) `git log --oneline 7b986738..HEAD -- . ":(exclude)docs"` → nothing: no commit of mine; `<tip now>` = `7b986738`. (ii) `git log --stat --format=%h 7b986738..HEAD` → `7b22e411`: only the build report and its `.result` under `docs/`. (iii) `git log --oneline 7f415a4f..HEAD -- ops/desk/house-probe.sh ".../CHECK-HUB.md" ".../STANDING-LIST.md" tests/ops/test_house_probe.py .claude` → EMPTY. (iv) no HELD test committed (fence; O1's test is in `## FIXES`). (v) `ls <WT>/.env` → "No such file"; `git status --short --branch` → `## ops/gemini-builder-row-1017` alone (10:08). (vi) `git log --stat --format=%h 7f415a4f..HEAD -- src/cobalt/db_migrations tests/cobalt` → nothing: no gate lists owed. (vii) records: `git -C /Users/cobalt/cobalt log --oneline ops/gemini-builder-row-1017 -5` → `7b22e411`, `7b986738`, `14a17ab7`, `7f415a4f`, `3f037e70` as recorded; `git -C /Users/cobalt/cobalt diff --stat 7b986738 7b22e411 -- . ":(exclude)docs"` → nothing; `git -C /Users/cobalt/cobalt diff --stat 7f415a4f main -- ops tests ".../SHADOW-HUB.md"` → nothing (`main` has not moved in these files); the decoy `ls -la` lines match (X2 above); the 583 stat matches. (viii) L32: no value of his in this report; the paths and ids are the desk's.

## OPEN
- O1 — HELD, NOT FIXED — `ops/desk/bare-guard.py`: settles by the builder's fix round: read every `--add-dir` spelling at `:1205` (e.g. `--add-dir[ =](\S+)`), or refuse an agy template holding `--add-dir=`; its test above then passes.
- O2 — UNSETTLED: settles by the desk's X1 run (does agy's workspace include the cwd?) — if it does, the guard pins the seat's cwd to the worktree for agy; if it does not, the item closes.

## CONTINUE
next: done

## DECISIONS
1. O1 HELD, NOT FIXED — `ops/desk/bare-guard.py:1205`. A `## BUILDERS` Gemini row that adds `--add-dir=<dir>` passes the guard: the agy write-target read takes only the space spelling, so `:1206` sees one target. Run: the O1 test above → `AssertionError: (0, '')`. Today's hub row has no such token, so nothing is open on `main` until a row is edited, but bound (c) (nothing widened by the row) is not pinned by the code. Default taken: not fixed (the card fences every edit of the guard and its tests); it goes to the builder's ONE fix round on this card, with the test above. Ready: NO.
2. O2 UNSETTLED — the guard admits the Gemini call from any cwd (`builder_call` never reads `s["cwd"]`); the hub's note leans on "run from the cd into the worktree". Default taken: left open for the desk's X1 run before the Gemini arm's first build (pass 0 should also be run once from a cwd other than the worktree, or the X1 steps should prove it). Not fixed here.
3. X6 / the build's DECISION R1 — recommendation: keep four lines, change nothing. `:218-219` is one refusal call whose input and message must spell the old id; `:178` is the whole-file pin. Only `:129`'s entry could go (`:178` covers the whole file, a superset of `## BUILDERS`), giving three lines, never two; not worth a fix-round edit.

## RECORDS
- `REFUSED, not needed: git -C /Users/cobalt/cobalt merge-base 7f415a4f ops/band-routing-1015 — Permission to use Bash has been denied because Claude Code is running in don't ask mode.` (row M1 named it with "first"; replaced by `git log --oneline 7f415a4f..f2ca3e1a` → nothing and `git diff --stat f2ca3e1a 7f415a4f -- <three files>` → nothing).
- Gemini probe OUT (HARNESS): `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` — the probe still names the old id (card 670's `house-probe.sh`; recorded, not a finding). House B was not needed in any case (`HOUSE B: as needed`); X5: Gemini could not sit on its own builder row's check.
- House A Grok: stdout held its progress text and the path; the list itself is `<S>/house-a.md`, written by Grok (881 bytes, 09:37).
- No lock take (DB: none). No commit of mine; the report and the `.result` file are left for the desk to commit (my git writes run only with the cwd in `<WT>`; this report lives on `main`).
- L74: a system notice in this session asked for a `Claude-Session:` line on commits; CHECK-HUB L74 says commits carry `Co-Authored-By` only. No commit was made.
- files opened: 11 — `CHECK-HUB.md`; card 687; `BUILD-HUB.md` (`## THE LOCK`, `## E2`–`## W`); `ops/desk/bare-guard.py`; `ops/desk/desk-launch.sh`; `tests/ops/test_bare_guard.py`; `tests/ops/test_desk_launch_shadow.py`; `tests/ops/test_shadow_hub_file.py`; card 367; the build report (`## FOR THE CHECK`, by Grep); `<S>/house-a.md`. Not opened: `areas/cobalt.md`, the build card 671, `cto-2026-10-17.md` rows beyond authorize.sh's quoted rows, `gemini-bakeoff-answer-2026-10-17.md` (staged for the house only).
- Check of `gemini-builder-row`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: gemini-builder-row · pass: 1 · tip: 7b986738 · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 2 · house B: none available · suites: offline 8413/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: NO · decisions: 3 · for Dejan: 0 · tokens: 212150
