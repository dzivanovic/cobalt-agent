# hub-text-1013-fr1 — build report (fix round, row FR-P1) — 2026-10-14

## §0 Headline
FR-P1: card 523's change (H1-H3 with FR-T1, as at `65951179`) is re-applied by Edit on `main` `4a7b221f`, tip `e82cdcc7`. There was no merge, no cherry-pick and no revert-of-revert.
BUILD-HUB.md and the two test files are byte-equal to `65951179`. DEPLOY-HUB.md differs from BASE by 523's one P1 hunk only.
Results: `test_hub_text_1013.py` 4 passed; tests/ops 3608 passed, 1 xfailed; offline 4328/0; live-note 146/0. DB: none. RESTARTS: none.

## L74
A system message in this session asked for a `Claude-Session:` line on commits. Recorded once here; not acted on. Every commit carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/523-hub-text-card.md"`, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/523-hub-text-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/523-hub-text-card.md" · 0 · 0456a7536347c51281355cccea14dfc2d919d588
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/523-hub-text-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, output whole:
```
clock · date · 0 · Wed Oct 14 15:12:45 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/hub-text-1013-fr1
    ?? "docs/40 - DevDocs/reports/hub-text-build-fr1-2026-10-14.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 4a7b221f docs(desk): card 537 deployed, R1484
diff · git diff --stat 4a7b221f · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/hub-text-1013-fr1 · 0 · 4a7b221f docs(desk): card 537 deployed, R1484
env here · ls /Users/cobalt/cobalt-wt/hub-text-1013-fr1/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- `git show --stat 4a7b221f` → `docs(desk): card 537 deployed, R1484`; `docs/40 - DevDocs/reports/cto-2026-10-14.md | 17 +++++++++--------`, 1 file.
- THE SOURCE OF THE PORT. `git log --oneline --boundary 4a7b221f..65951179` →
  ```
  65951179 docs(hub-text-1013): fix-round report FR-T1 — 7f2f9637
  7f2f9637 fix(hub-text-1013): tests pin only the lines this card changes, by their own text (FR-T1; L75, L28)
  e4bd85db wip(hub-text-1013): PREFLIGHT — fix round, head 0f4a49c5 is the build report commit, preflight.sh build has no fix-round case
  07421d11 wip(hub-text-1013): PREFLIGHT — head is the build report commit, no fix-round mode (FR-T1)
  - 0f4a49c5 docs(hub-text-1013): build report — 3894a878
  ```
  The merge-base with main is `0f4a49c5` (merged into main by `1bdc32b8`, then taken out by the revert `cdf2233c`). `git log --oneline -14 --first-parent 65951179` shows 523's own commits start after `ce548f10` (`73fe909b` red, `3894a878` fix, `0f4a49c5` report, then the FR-T1 commits). Since the revert undid 523 on main, the change ported is 523's whole code change, `git diff ce548f10 65951179` over the files the rows name.
- `git diff --stat ce548f10 65951179` → `BUILD-HUB.md | 3 +-`, `DEPLOY-HUB.md | 2 +-`, `reports/hub-text-build-2026-10-13.md | 251 +++`, `tests/ops/test_build_hub_no_clutter.py | 13 +-`, `tests/ops/test_hub_text_1013.py | 85 +++`.
- WHAT MAIN TOUCHED. `git diff --stat ce548f10 4a7b221f -- <the four row files>` → `DEPLOY-HUB.md | 26 ++++++++++++++++----------` only. So BUILD-HUB.md and the two test files are, net, untouched by main since 523's base. DEPLOY-HUB.md was touched by main (`9fb997bb` and others); its P1 line at BASE is unchanged: `grep "P1 DATE"` → `57:- **P1 DATE**: \`date\`, recorded in the row. No restart window binds a deploy (L43, his R389): it runs at any hour, day or night.`
- RESTARTS on the empty range: not run before the first change; the range's table is under `## RESTARTS`.
- Card `## RECORDS` (desk facts, drafted at `ce548f10`): re-read where they bear on the port. `BUILD-HUB.md:105` and `:111` at BASE read as the card quotes (Read of lines 105-111). The P1 line is `DEPLOY-HUB.md:57`, as quoted.

## E0 BASELINE
Not run as a separate step. This is a fix round (L75): the card's FR-P1 names the tests to run (`tests/ops/test_hub_text_1013.py` and the gate's tests/ops). The full offline suite and the live-note suite run at W through `gate.sh`.

## E2 RED
`tests/ops/test_hub_text_1013.py` was written by Write as the `65951179` text, before any hub edit. `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_text_1013.py tests/ops/test_build_hub_no_clutter.py` on BASE → `3 failed, 6 passed`:
- `test_h1_p1_names_the_backup_window_once_in_its_own_line` → `assert 0 == 1` (`t.count("21:30-22:30 ET")`): the window is absent. Row H1's reason.
- `test_h2_the_build_hub_states_the_fixed_line_per_held_id` → `AssertionError: []` / `assert 0 == 1`: no `FIX-ROUND REPORT (brain R1309):` line. Row H2's reason.
- `test_h3_the_build_hub_stop_line_step_names_no_untracked_file` → `AssertionError: []` / `assert 0 == 1`: no `no untracked file at the stop line`. Row H3's reason.
- `test_h3_the_launcher_still_carries_the_shadow_exception` (negative control) PASSED.
Commit `12dd14fd wip(hub-text-1013-fr1): red — H1-H3 tests ported from 65951179 (FR-P1)`.

## E3 THE ROWS
FR-P1, by Edit only (no merge, no cherry-pick, no revert-of-revert):
- `DEPLOY-HUB.md:57`: the P1 tail replaced (H1).
- `BUILD-HUB.md:105`: the CLOSE `git status` clause (H3); new line 112, the FIX-ROUND REPORT line (H2).
- `tests/ops/test_build_hub_no_clutter.py::test_no_other_line_changes_from_base`: the filter (H3 (3)).

PROOF PER FILE:
- Files main has not touched since 523's base: `git diff 65951179 -- "docs/40 - DevDocs/prompts/BUILD-HUB.md" tests/ops/test_build_hub_no_clutter.py tests/ops/test_hub_text_1013.py` → printed nothing (byte-equal to `65951179`).
- File main has touched: `git diff 4a7b221f -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → ONE hunk, `@@ -54,7 +54,7 @@`, the P1 line only, `-…it runs at any hour, day or night.` / `+…it runs at any hour, day or night, but it never starts within the nightly backup window 21:30-22:30 ET (brain R1295; D2.4's \`backup run\` stays off it): a \`date\` inside the window → \`FAILED PREFLIGHT: P1 — backup window\`, nothing changed.` That equals 523's own DEPLOY-HUB hunk in `git diff ce548f10 65951179` (same `-`/`+` lines). Every other line of main stands.
- `git diff --stat 4a7b221f` → `BUILD-HUB.md | 3 +-`, `DEPLOY-HUB.md | 2 +-`, `tests/ops/test_build_hub_no_clutter.py | 13 ++++-`, `tests/ops/test_hub_text_1013.py | 85 +++`; `4 files changed, 100 insertions(+), 3 deletions(-)`. That's the same per-file count as 523's change minus its old report.

GREEN: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_hub_text_1013.py tests/ops/test_build_hub_no_clutter.py tests/ops/test_hub_lines.py` → `39 passed, 15 warnings in 2.85s`. `tests/ops/test_hub_lines.py` is unchanged: it is not in `git diff --stat 4a7b221f`.

MUTATIONS: For H1-H3, the fix undone is BASE itself; their reds are the E2 lines above. For the no-clutter repair, an Edit mutation dropped `close_last` from the `now` filter. `uv run pytest -q … --tb=line tests/ops/test_build_hub_no_clutter.py` → `1 failed, 4 passed`, `FAILED tests/ops/test_build_hub_no_clutter.py::test_no_other_line_changes_from_base`, first line `E   assert ['# BUILD-HUB...…\`.', '', ...] == ['# BUILD-HUB...…\`.', '', ...]` (`At index 102 diff: '- \`## §0 Headline\`…'`). Undone by Edit; `git diff 65951179 -- <the three files>` → nothing (tree back at the fix).

No DevDocs module page line: the change touches no module under `src/`.
Commit `e82cdcc7 fix(hub-text-1013-fr1): port of 523 at 65951179 onto main — P1 backup window, FIXED line per held id, no untracked file at stop (FR-P1, H1-H3, FR-T1; L28, L71, L75)`.

## RESTARTS
`uv run cobalt jobs restarts 4a7b221f..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/hub-text-build-fr1-2026-10-14.md	A	DOCS	-
tests/ops/test_build_hub_no_clutter.py	M	test/documentation; no resident	-
tests/ops/test_hub_text_1013.py	A	test/documentation; no resident	-
RESTARTS: none
```

## W THE THREE SUITES
(a0) `git diff --name-only --no-renames 4a7b221f` →
```
docs/40 - DevDocs/prompts/BUILD-HUB.md
docs/40 - DevDocs/prompts/DEPLOY-HUB.md
tests/ops/test_build_hub_no_clutter.py
tests/ops/test_hub_text_1013.py
```
Every path starts with `docs/` or `tests/ops/`. **cobalt_dev: not taken (DB: none — 4 paths)**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-text-1013-fr1 offline` → exit 0: `offline 4328/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/hub-text-1013-fr1-offline-20261014-151418.log`. Tests this build adds: the 4 in `tests/ops/test_hub_text_1013.py`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-text-1013-fr1 livenote` → exit 0: `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/hub-text-1013-fr1-livenote-20261014-152606.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `3608 passed, 1 xfailed, 16 warnings in 759.01s (0:12:39)`. No SKIPPED line.
- with-DB: not run (DB: none). `.env`: never present (`ls` → "No such file or directory" at RECOVERY and PREFLIGHT).

## PRE-STOP SELF-CHECK
(1) Each test was shown red. The H1, H2 and H3 tests are red on BASE (E2: `assert 0 == 1`, `AssertionError: []` ×2). The negative control `test_h3_the_launcher_still_carries_the_shadow_exception` was green on BASE. The no-clutter repair is red under its Edit mutation (E3: `FAILED …::test_no_other_line_changes_from_base`, `At index 102 diff`). No test stayed green.
(2) Each changed line is pinned: P1 (`DEPLOY-HUB.md:57`) by the H1 test; `BUILD-HUB.md:105` by the H3 test and the no-clutter filter; `BUILD-HUB.md:112` by the H2 test and the no-clutter count. The launch lines are pinned by `tests/ops/test_hub_lines.py`, which is unchanged and passes (39 passed with the touched set). The shadow exception in `desk-launch.sh` is pinned by the H3 control. The hub lines are read by agents, not code: no caller in `src`.
(3) Re-read at the tip with these calls: `grep -n -F "brain R1309" BUILD-HUB.md` → `:105`, `:112`; `grep -n -F "21:30-22:30 ET" DEPLOY-HUB.md` → `:57` only; `grep -n -F` of `BASE`, `git show` and `subprocess` in `tests/ops/test_hub_text_1013.py` → no hit, each; `git log --oneline 4a7b221f..HEAD` → the two commits below; `git diff 65951179 -- <the three files>` → nothing.

## FOR THE CHECK
- Range `4a7b221f..e82cdcc7`: `12dd14fd wip(hub-text-1013-fr1): red — H1-H3 tests ported from 65951179 (FR-P1)`; `e82cdcc7 fix(hub-text-1013-fr1): port of 523 at 65951179 onto main — P1 backup window, FIXED line per held id, no untracked file at stop (FR-P1, H1-H3, FR-T1; L28, L71, L75)`.
- Reds, mutation and greens: see E2 and E3.
- The checked tip `3894a878` is an ancestor of BASE (`git log --oneline 4a7b221f..3894a878` → nothing), so DEPLOY-HUB P2's fix-round ancestor test holds at `e82cdcc7`. The check's last line: `held: 0 · held unfixed: 0 · ready: YES`, so no `FIXED:` line is owed.
- Suites: offline 4328/0, live-note 146/0, tests/ops 3608 passed / 1 xfailed; with-DB not run (DB: none); F0/F1/F2 not run (DB: none); lock not run (DB: none).
- RESTARTS table: see `## RESTARTS` (`RESTARTS: none`).
- Records copied at PREFLIGHT: see `## PREFLIGHT`.

## CONTINUE
next: none (BUILT)

## DECISIONS
none

## RECORDS
- Launch message: `CONTINUE: FIX ROUND row FR-P1`. RECOVERY reads at 15:12:32 EDT: `git status --short --branch` → `## ops/hub-text-1013-fr1`; `git log --oneline -3` → `4a7b221f docs(desk): card 537 deployed, R1484` at the top (= BASE, no wip commit); `ls -la …/hub-text-1013-fr1/.env` → "No such file or directory". No report existed at REPORT; this is its first write.
- CONTINUED at FR-P1 15:12:32 EDT (new session; the branch was freshly cut at BASE, so AUTHORIZATION and PREFLIGHT ran first).
- 523's old build report `reports/hub-text-build-2026-10-13.md` (in `ce548f10..65951179`, removed from main by the revert) is not ported: it is not a file the rows name. This report is the fix round's record.
- Row H4: not built. `## RECORDS` of the card carries no `ROW H4: BUILD` line (the card's default). R5's RUN is the `## RESTARTS` table.
- **The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.**

BUILT · job: hub-text-1013-fr1 · tip: e82cdcc7 | on 4a7b221f | migration: none | offline 4328/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 114989
