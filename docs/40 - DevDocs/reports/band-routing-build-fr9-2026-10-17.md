# band-routing-1015 — fix round 3, FR-9, build report (2026-10-17)

## §0 Headline
- Fix round 3 (FR-9) is built on `8b142c56..4b62c2fa`. The close step's `unclean()` in `desk-watch.sh` now lets through exactly one status line, `?? SHADOW-INSTRUCTIONS.md`, and only for kinds `shadow` and `routed`. A routed or shadow gate seat whose tree holds only that file now closes through `desk-done.sh`.
- A `build`-kind tree holding that file is still KEPT "tree not clean". So is a routed tree with any other untracked or modified line. The strict xfail of `test_check_o1_…` is gone and the test passes.
- Offline 8439/0 (tests/ops 3871 passed, 1 xfailed, pre-existing), live-note 146/0. With-DB not run (DB: none). RESTARTS: none.
- 0 decisions.

FIXED: O1 — tests/ops/test_band_routing_1015.py::test_check_o1_a_routed_closeout_on_a_gate_seat_tree_hands_build_to_desk_done
FIXED: O1 — tests/ops/test_band_routing_1015.py::test_fr9_a_shadow_card_tree_holding_only_the_instructions_file_closes

## L74
- A system-reminder block in this session asked for a `Claude-Session:` trailer on commits. Recorded here once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md"` (09:02 EDT), exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md" · 0 · caebf4574fa588f3a4edbc1357331e34f5930888
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
RECOVERY first rows (09:01 EDT): `git status --short --branch` → `## ops/band-routing-1015`; `git log --oneline -3` → `8b142c56 wip(band-routing-1015): check red — O1 (strict xfail: HELD, NOT FIXED, desk-watch.sh fenced)`, `4fc9b9da docs(band-routing-1015): build report — fda2300b (fix round 2, FR-6 to FR-8)`, `fda2300b fix(band-routing-1015): …`; `ls -la …/band-routing-1015/.env` → `No such file or directory`.

This report's first write was committed before the script ran (`da95e8c7 wip(band-routing-1015): fix round 3 report opened (FR-9)`), as in round 2, so the status row stays clean. `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, exit 0, output whole:
```
clock · date · 0 · Sat Oct 17 09:02:20 EDT 2026
status · git status --short --branch · 0 · ## ops/band-routing-1015
head · git log --oneline -1 · 0 · da95e8c7 wip(band-routing-1015): fix round 3 report opened (FR-9)
diff · git diff --stat f2ca3e1a · 0 · (18 lines)
     docs/40 - DevDocs/prompts/BUILD-HUB.md             |   2 +
     docs/40 - DevDocs/prompts/CARD.md                  |   3 +
     docs/40 - DevDocs/prompts/CHECK-HUB.md             |   4 +-
     docs/40 - DevDocs/prompts/SHADOW-HUB.md            |  15 +-
     .../reports/band-routing-build-2026-10-15.md       | 201 +++++
     .../reports/band-routing-build-2026-10-15.result   |  15 +
     .../reports/band-routing-build-fr1-2026-10-16.md   | 152 ++++
     .../band-routing-build-fr1-2026-10-16.result       |  15 +
     .../reports/band-routing-build-fr6-2026-10-16.md   | 177 +++++
     .../band-routing-build-fr6-2026-10-16.result       |  15 +
     .../reports/band-routing-build-fr9-2026-10-17.md   |  36 +
     ops/desk/bare-guard.py                             |   5 +
     ops/desk/desk-launch.sh                            |  80 +-
     ops/desk/desk-watch.sh                             |   4 +-
     ops/desk/preflight.sh                              |  26 +-
     tests/ops/test_band_routing_1015.py                | 860 +++++++++++++++++++++
     tests/ops/test_check_hub_shadow.py                 |   3 +-
     17 files changed, 1597 insertions(+), 16 deletions(-)
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/band-routing-1015 · 0 · da95e8c7 wip(band-routing-1015): fix round 3 report opened (FR-9)
env here · ls /Users/cobalt/cobalt-wt/band-routing-1015/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

THE CARD'S SYMBOLS on the tip `8b142c56`, read in this worktree (Read and Grep; `wc -l`: desk-watch.sh 230, test_band_routing_1015.py 860):
- `desk-watch.sh`: `unclean() {` `:97`, its closing `}` `:108`, the worktree status read `:99` `[ -z "$(git -C "/Users/cobalt/cobalt-wt/$wt" status --short 2>&1)" ] || { echo "tree not clean"; return; }`. Its caller is `close_worker` (`why=$(unclean)` at `:126` and `:135`).
- The model: `preflight.sh:159` `if [ "$ok" -ne 0 ] && { [ -n "$shadow" ] || [ -n "$routed" ]; } && [ "$other" = "?? SHADOW-INSTRUCTIONS.md" ]; then`, and `desk-launch.sh:1817` `{ [ -z "$shadow" ] && [ -z "$routed_tree" ]; } || [ "$dirt" != "?? SHADOW-INSTRUCTIONS.md" ] || dirt=""`.
- `test_band_routing_1015.py`: `ROUTED_STOP` `:494`, `IDLE_GATE` `:496`, `class RWatch` `:500`, `def run` `:539`, `def logged` `:545`; one xfail decorator, `:649` (`reason="check fr2 O1: HELD, NOT FIXED — ops/desk/desk-watch.sh (fenced)"`), its `def` `:650`, and the line above it is blank.
- Every anchor is where the card's `## RECORDS` (fix round 3, drafter 680) puts it. The card's records are copied by reference.

## E0 BASELINE
Not re-run. The B rows' E0 on `f2ca3e1a` stands in `band-routing-build-2026-10-15.md`. A fix round reruns only the tests that touch the fixed part, then the gate.

## E2 RED
On the tip, in `tests/ops/test_band_routing_1015.py` only: three new tests (four cases), after `test_check_o1_…`, using the `RWatch` helper as it stands. The marker stayed in place for E2. The build-kind control rewrites its card's `BAND: LOW` to `BAND: HIGH` and lists `IDLE_JOB_BUILD`. The modified-file control commits a `tracked.txt` in the tmp worktree and then changes it.

`uv run pytest -q -p no:cacheprovider --color=no --tb=line --runxfail tests/ops/test_band_routing_1015.py` → `2 failed, 64 passed, 15 warnings in 25.87s`. Each red, first line:
- O1 `test_check_o1_a_routed_closeout_on_a_gate_seat_tree_hands_build_to_desk_done` → `:657: AssertionError: BUILT · job: x · tip: tip-x | on base-x | rows: 1 of 1` / `KEPT sess-x01: tree not clean` / `assert [] == ['sess-x01 /p...ild.md build']`.
- FR-9 `test_fr9_a_shadow_card_tree_holding_only_the_instructions_file_closes` → `:671: AssertionError: SHADOW BUILT · job: x · tip: tip-x | on base-x` / `KEPT sess-x01: tree not clean` / `assert [] == ['sess-x01 /p...ld.md shadow']`.

CONTROLS GREEN on the tip, inside the 64 passed: `test_fr9_control_a_build_kind_tree_holding_that_file_is_still_kept`, `test_fr9_control_a_routed_tree_with_any_other_untracked_line_is_still_kept[untracked]`, `[modified]`. No RUN row and no with-DB red; no lock. Commit `9bd05618 wip(band-routing-1015): fix round 3 red (FR-9)`.

## E3 THE ROWS
FR-9, `desk-watch.sh` `unclean()`, re-read by content before the edit (`## PREFLIGHT`). The one status read became three lines and a comment:
```
    dirt=$(git -C "/Users/cobalt/cobalt-wt/$wt" status --short 2>&1)
    # card 583 FR-9: a shadow or routed seat's ONE untracked SHADOW-INSTRUCTIONS.md is not dirt
    case "$kind" in shadow|routed) [ "$dirt" != "?? SHADOW-INSTRUCTIONS.md" ] || dirt="" ;; esac
    [ -z "$dirt" ] || { echo "tree not clean"; return; }
```
The whole status output must equal the one line, as at `desk-launch.sh:1817`. A second line of any kind keeps the tree "not clean". `unclean` runs in `$(…)`, so `dirt` stays in its subshell. Nothing else of `desk-watch.sh` changed (`git diff`: one line out, four in). The decorator above `test_check_o1_…` is out, and its body is unchanged.

THE MUTATIONS (Edit tool, `-k "check_o1 or fr9"` run alone, each undone with Edit):
- The fix undone (`case "$kind" in MUTATED) …`) → `2 failed, 3 passed`: `test_check_o1_…` `:656` and `test_fr9_a_shadow_…` `:670`, each `KEPT sess-x01: tree not clean` with the stub never called.
- The controls: the exception as a glob over any kind (`case "$dirt" in *SHADOW-INSTRUCTIONS.md*) dirt="" ;; esac`) → `3 failed, 2 passed`: `test_fr9_control_a_build_kind_…` `:681`, `…[untracked]` and `…[modified]` `:700`, each `assert 'CLOSED sess-x01' == 'KEPT sess-x0...ree not clean'`.
- After the undo, `git diff` showed the fix only (2 files, the four lines above and the decorator out).

GREEN:
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py` (no `--runxfail`) → `66 passed, 15 warnings in 21.85s`. No `xfailed`.
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_watch.py tests/ops/test_close_automation_1015.py tests/ops/test_shadow_hub_file.py tests/ops/test_desk_launch_shadow.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_check_hub_shadow.py tests/ops/test_card_template_1014.py tests/ops/test_preflight.py` → `373 passed, 16 warnings in 181.77s (0:03:01)`. `git diff --stat 8b142c56 -- <those eight>` → nothing.
- `grep -n -E -e "git show" -e "[0-9a-f]{8}" tests/ops/test_band_routing_1015.py` → no output (exit 1).

DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` (B rows' report, `## E3`), so there is no dated line.

Commit `4b62c2fa fix(band-routing-1015): close step excepts a shadow or routed seat's one untracked SHADOW-INSTRUCTIONS.md (FR-9, L1 L72)`.

## RESTARTS
`uv run cobalt jobs restarts 8b142c56..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/reports/band-routing-build-fr9-2026-10-17.md	A	DOCS	-
ops/desk/desk-watch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_band_routing_1015.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `4b62c2fa`. (a0): `git diff --name-only --no-renames f2ca3e1a` → `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `…/CARD.md`, `…/CHECK-HUB.md`, `…/SHADOW-HUB.md`, `docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md`, `….result`, `band-routing-build-fr1-2026-10-16.md`, `….result`, `band-routing-build-fr6-2026-10-16.md`, `….result`, `band-routing-build-fr9-2026-10-17.md`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `ops/desk/desk-watch.sh`, `ops/desk/preflight.sh`, `tests/ops/test_band_routing_1015.py`, `tests/ops/test_check_hub_shadow.py`. Every path is under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 17 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 offline` → `tests/ops: run (docs/40 - DevDocs/prompts/BUILD-HUB.md)` · `offline 8439/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-offline-20261017-090832.log`. Its two runs were `:888` `4568 passed, 806 skipped, 1 xfailed, 36 warnings in 739.82s (0:12:19)` and `:959` (tests/ops whole) `3871 passed, 1 xfailed, 16 warnings in 895.32s (0:14:55)`. The 3871 is round 2's 3866, plus the four cases this round adds, plus the strict xfail of `8b142c56`, which now passes. The one xfail is the same as at every earlier W.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-livenote-20261017-093615.log`. The only SKIPPED is `:56` `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.
- `ls /Users/cobalt/cobalt-wt/band-routing-1015/.env` → `No such file or directory`.
- The card's `uv run pytest -q tests/ops` whole is the gate's `:959` run on the same tip. I did not type it a second time.
- With-DB: not run (DB: none).

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red. `test_check_o1_…` and `test_fr9_a_shadow_…` were red on the tip (`## E2 RED`) and again under the undo mutation. The three control cases were red under the control mutation (any kind, glob match): `assert 'CLOSED sess-x01' == 'KEPT …tree not clean'` (`## E3`).
(2) Entry paths: `unclean()` has one caller, `close_worker` (`why=$(unclean)`, the first call and the close-wait loop). It runs for every kind with a worktree (`wt != -`: build, check, devfix, shadow, routed). `routed` is pinned by `test_check_o1_…` and the two `[untracked]`/`[modified]` controls. `shadow` is pinned by `test_fr9_a_shadow_…`, and `build` by `test_fr9_control_a_build_kind_…`. `check` and `devfix` take the same non-excepted path as `build`, and the green `test_desk_watch.py` and `test_close_automation_1015.py` (373 passed with their neighbours) keep them as before. A clean tree with no file is pinned by `test_fr6_a_routed_closeout_…` and `test_fr6_control_a_shadow_…`, both green.
(3) Re-read at the tip: `grep -n -F "SHADOW-INSTRUCTIONS.md" ops/desk/desk-watch.sh` → `100:` (the comment) and `101:` (the `case`); `grep -n -F "xfail" tests/ops/test_band_routing_1015.py` → no output; `git log --oneline 8b142c56..HEAD` → the three commits below; `ls …/.env` → No such file.

## FOR THE CHECK
- Range `8b142c56..4b62c2fa` (on BASE `f2ca3e1a`): `da95e8c7 wip(band-routing-1015): fix round 3 report opened (FR-9)` · `9bd05618 wip(band-routing-1015): fix round 3 red (FR-9)` · `4b62c2fa fix(band-routing-1015): close step excepts a shadow or routed seat's one untracked SHADOW-INSTRUCTIONS.md (FR-9, L1 L72)`.
- Per row: the reds are in `## E2 RED`, and the mutations and greens are in `## E3 THE ROWS`.
- This round has no RUN row. The RESTARTS table is in `## RESTARTS`, whole.
- Suites: `## W`. With-DB: not run (DB: none). F0/F1/F2: not run (DB: none). Lock taken/released: not run (DB: none).
- X16: `desk-watch.sh` changed only inside the body of `unclean()` in this round (one line out, four in, including one comment line). FR-6's two `routed` arms and its mapping line stand as built. `desk-done.sh` was not touched. The strict xfail of `test_check_o1_…` is gone, and its body is unchanged (`git diff`, the decorator line only).
- Records copied at PREFLIGHT: the card's `## RECORDS` (drafter 680). Every anchor they name matched (`## PREFLIGHT`).

## CONTINUE
next: none (BUILT)

## DECISIONS
none

## RECORDS
- CONTINUED at FIX ROUND row FR-9 09:01 EDT (a new session; RECOVERY rows under `## PREFLIGHT`).
- L74: one session system reminder asked for a `Claude-Session:` trailer. It is recorded under `## L74`. Commits carry `Co-Authored-By` only.
- I committed the report's first write as a wip commit before `preflight.sh`, so the status row ran clean (round 2's lesson).
- I edited this report (uncommitted) while the offline gate ran on `4b62c2fa`. No test reads this file. The gate's tip is the fix commit.
- The header comment of `desk-watch.sh` (`:16-23`, "any other is CLEAN when the worktree … is clean") does not name the exception. FR-9 fences the file to the body of `unclean()`, so I left the comment as is. The usage lines `:2` and `:49` are as round 2 left them.
- E0 not re-run (fix round). No lock take (DB: none). `.env`: never present.
- ORDER (card, binding): the check after this round is scoped to FR-9 and waits for job `check-scratch-fr1` DEPLOYED. That is not this builder's step.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: band-routing-1015 · tip: 4b62c2fa | on f2ca3e1a | migration: none | offline 8439/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 171440
