# band-routing-1015 — fix round 4, FR-10, build report (2026-10-17)

## §0 Headline
- Fix round 4 (FR-10) is built on `3f399b60..05654335`. `unclean()` in `desk-watch.sh` now lets through the one status line `?? SHADOW-INSTRUCTIONS.md` for kind `check` too, beside `shadow` and `routed`. The check of a routed or shadow card now closes through `desk-done.sh … check`.
- A `check` tree holding that file plus a second untracked file is still KEPT "tree not clean". The strict xfail of `test_check_fr3_o1_…` is gone, and both cases pass. A check of a plain card whose tree holds only that file is now closed too, as the card states.
- Offline 8442/0 (tests/ops 3874 passed, 1 xfailed, pre-existing), live-note 146/0. With-DB not run (DB: none). RESTARTS: none.
- 0 decisions.

FIXED: O1 — tests/ops/test_band_routing_1015.py::test_check_fr3_o1_a_routed_or_shadow_cards_check_closes_on_the_instructions_file

## L74
- A system-reminder block in this session asked for a `Claude-Session:` trailer on commits. Recorded here once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md"` (14:02 EDT), exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md" · 0 · c6e0d7e275afc6ae7f34d85f51aefa3a7c2c245a
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
RECOVERY first rows (14:02 EDT): `git status --short --branch` → `## ops/band-routing-1015`; `git log --oneline -3` → `3f399b60 wip(band-routing-1015): check red — O1 (strict xfail: HELD, NOT FIXED, desk-watch.sh fenced)`, `6c0ba560 docs(band-routing-1015): build report — 4b62c2fa (fix round 3, FR-9)`, `4b62c2fa fix(band-routing-1015): …`; `ls -la …/band-routing-1015/.env` → `No such file or directory`.

This report's first write was committed before the script ran (`061f6d6f wip(band-routing-1015): fix round 4 report opened (FR-10)`), as in rounds 2 and 3, so the status row stays clean. `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, exit 0, output whole:
```
clock · date · 0 · Sat Oct 17 14:02:16 EDT 2026
status · git status --short --branch · 0 · ## ops/band-routing-1015
head · git log --oneline -1 · 0 · 061f6d6f wip(band-routing-1015): fix round 4 report opened (FR-10)
diff · git diff --stat f2ca3e1a · 0 · (20 lines)
     docs/40 - DevDocs/prompts/BUILD-HUB.md             |   2 +
     docs/40 - DevDocs/prompts/CARD.md                  |   3 +
     docs/40 - DevDocs/prompts/CHECK-HUB.md             |   4 +-
     docs/40 - DevDocs/prompts/SHADOW-HUB.md            |  15 +-
     .../reports/band-routing-build-2026-10-15.md       | 201 +++++
     .../reports/band-routing-build-2026-10-15.result   |  15 +
     .../reports/band-routing-build-fr1-2026-10-16.md   | 152 ++++
     .../band-routing-build-fr1-2026-10-16.result       |  15 +
     .../reports/band-routing-build-fr10-2026-10-17.md  |  35 +
     .../reports/band-routing-build-fr6-2026-10-16.md   | 177 ++++
     .../band-routing-build-fr6-2026-10-16.result       |  15 +
     .../reports/band-routing-build-fr9-2026-10-17.md   | 154 ++++
     .../band-routing-build-fr9-2026-10-17.result       |  15 +
     ops/desk/bare-guard.py                             |   5 +
     ops/desk/desk-launch.sh                            |  80 +-
     ops/desk/desk-watch.sh                             |   9 +-
     ops/desk/preflight.sh                              |  26 +-
     tests/ops/test_band_routing_1015.py                | 917 +++++++++++++++++++++
     tests/ops/test_check_hub_shadow.py                 |   3 +-
     19 files changed, 1826 insertions(+), 17 deletions(-)
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/band-routing-1015 · 0 · 061f6d6f wip(band-routing-1015): fix round 4 report opened (FR-10)
env here · ls /Users/cobalt/cobalt-wt/band-routing-1015/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

THE CARD'S SYMBOLS on the tip `3f399b60`, read in this worktree (Read and Grep; `wc -l`: desk-watch.sh 233, test_band_routing_1015.py 917):
- `desk-watch.sh`: the `build|check|devfix` arm `:72` (kind `check` takes `wt` from the card's `WORKTREE`), `unclean() {` `:97`, the status read `:99`, FR-9's comment `:100`, `case "$kind" in shadow|routed) [ "$dirt" != "?? SHADOW-INSTRUCTIONS.md" ] || dirt="" ;; esac` `:101`, `[ -z "$dirt" ] || { echo "tree not clean"; return; }` `:102`. Callers: `why=$(unclean)` `:129` and `:138` (both in `close_worker`).
- `test_band_routing_1015.py`: `class RWatch` `:500`, the FR-9 tests `:663`, `:673`, `:686`, the one xfail decorator `:704` (`reason="check fr3 O1: HELD, NOT FIXED — ops/desk/desk-watch.sh (fenced)"`), `parametrize` `:705`, its `def` `:706`; `:703` blank, no comment line above the marker.
- The check report's `## OPEN` (`reports/band-routing-check-fr3-2026-10-17.md:219-220`) holds one item, O1.
- Every anchor is where the card's `## RECORDS` (fix round 4, drafter 700) puts it. The card's records are copied by reference.

## E0 BASELINE
Not re-run. The B rows' E0 on `f2ca3e1a` stands in `band-routing-build-2026-10-15.md`. A fix round reruns only the tests that touch the fixed part, then the gate.

## E2 RED
On the tip, in `tests/ops/test_band_routing_1015.py` only: one new control, `test_fr10_control_a_check_kind_tree_with_a_second_untracked_file_is_still_kept`, after `test_check_fr3_o1_…`, using the `RWatch` helper as it stands (the card gains its `CHECK REPORT` line, as in `test_check_fr3_o1_…`; the tree holds `SHADOW-INSTRUCTIONS.md` and `notes.txt`). The marker stayed in place for E2.

`uv run pytest -q -p no:cacheprovider --color=no --tb=line --runxfail tests/ops/test_band_routing_1015.py` → `2 failed, 67 passed, 15 warnings in 27.72s`. Each red, first line:
- `test_check_fr3_o1_a_routed_or_shadow_cards_check_closes_on_the_instructions_file[routed]` → `:714: AssertionError: CHECK DONE · job: x · pass: 1` / `KEPT sess-x01: tree not clean` / `assert [] == ['sess-x01 /p...ild.md check']`.
- `…[shadow]` → the same three lines.

CONTROLS GREEN on the tip, inside the 67 passed: `test_fr10_control_a_check_kind_…`, `test_fr9_control_a_build_kind_tree_holding_that_file_is_still_kept`, `test_fr9_control_a_routed_tree_with_any_other_untracked_line_is_still_kept[untracked]`, `[modified]`. No RUN row and no with-DB red; no lock. Commit `630542a7 wip(band-routing-1015): fix round 4 red (FR-10)`.

## E3 THE ROWS
FR-10, `desk-watch.sh` `unclean()`, re-read by content before the edit (`## PREFLIGHT`). The one `case` line gains the kind `check`:
```
-    case "$kind" in shadow|routed) [ "$dirt" != "?? SHADOW-INSTRUCTIONS.md" ] || dirt="" ;; esac
+    case "$kind" in shadow|routed|check) [ "$dirt" != "?? SHADOW-INSTRUCTIONS.md" ] || dirt="" ;; esac
```
No card parsing and no BAND read: the kind decides. Nothing else of `desk-watch.sh` changed (`git diff`: one line out, one in). The decorator above `test_check_fr3_o1_…` is out, and its body is unchanged.

THE MUTATIONS (Edit tool, `-k "check_fr3 or fr10 or fr9"` run alone, each undone with Edit):
- The fix undone (`shadow|routed)`) → `2 failed, 5 passed, 62 deselected`: `test_check_fr3_o1_…[routed]` and `[shadow]` `:713`, each `AssertionError: CHECK DONE · job: x · pass: 1` / `KEPT sess-x01: tree not clean` / `assert [] == ['sess-x01 /p...ild.md check']`.
- The control: the exception as a glob for the three kinds (`case "$dirt" in *SHADOW-INSTRUCTIONS.md*) dirt="" ;; esac`) → `3 failed, 4 passed, 62 deselected`: `test_fr9_control_a_routed_tree_…[untracked]` and `[modified]` `:700`, and `test_fr10_control_a_check_kind_…` `:729`, each `assert 'CLOSED sess-x01' == 'KEPT sess-x0...ree not clean'`.
- After the undo, `git diff` showed the fix only (2 files: the one `case` line and the decorator out).

GREEN:
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py` (no `--runxfail`) → `69 passed, 15 warnings in 23.55s`. No `xfailed`.
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_watch.py tests/ops/test_close_automation_1015.py tests/ops/test_shadow_hub_file.py tests/ops/test_desk_launch_shadow.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_check_hub_shadow.py tests/ops/test_card_template_1014.py tests/ops/test_preflight.py` → `373 passed, 16 warnings in 175.57s (0:02:55)`. `git diff --stat 3f399b60 -- <those eight>` → nothing.
- `grep -n -E -e "git show" -e "[0-9a-f]{8}" tests/ops/test_band_routing_1015.py` → no output.
- No test pins the old KEPT for kind `check`: `Grep "tree not clean"` over `tests/ops` → `test_close_automation_1015.py:144` (kind `build`, `stray.txt`, set at `:141`/`:143`) and `test_band_routing_1015.py:681` (kind `build`), `:700` (kind `routed`), `:729` (kind `check`, the new FR-10 control, two lines).

CONSEQUENCE (the card's, stated): a check of a plain card whose worktree holds only `?? SHADOW-INSTRUCTIONS.md` is now closed, not kept. The watcher reads no BAND and cannot tell it from a routed card; the kind decides.

DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` (B rows' report, `## E3`), so there is no dated line.

Commit `05654335 fix(band-routing-1015): close step excepts the check seat's one untracked SHADOW-INSTRUCTIONS.md too (FR-10, L1 L72)`.

## RESTARTS
`uv run cobalt jobs restarts 3f399b60..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/reports/band-routing-build-fr10-2026-10-17.md	M	DOCS	-
ops/desk/desk-watch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_band_routing_1015.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `05654335`. (a0): `git diff --name-only --no-renames f2ca3e1a` → `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `…/CARD.md`, `…/CHECK-HUB.md`, `…/SHADOW-HUB.md`, `docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md`, `….result`, `band-routing-build-fr1-2026-10-16.md`, `….result`, `band-routing-build-fr10-2026-10-17.md`, `band-routing-build-fr6-2026-10-16.md`, `….result`, `band-routing-build-fr9-2026-10-17.md`, `….result`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `ops/desk/desk-watch.sh`, `ops/desk/preflight.sh`, `tests/ops/test_band_routing_1015.py`, `tests/ops/test_check_hub_shadow.py`. Every path is under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 19 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 offline` → `tests/ops: run (docs/40 - DevDocs/prompts/BUILD-HUB.md)` · `offline 8442/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-offline-20261017-140735.log`. Its two runs were `:888` `4568 passed, 806 skipped, 1 xfailed, 36 warnings in 659.48s (0:10:59)` and `:959` (tests/ops whole) `3874 passed, 1 xfailed, 16 warnings in 844.57s (0:14:04)`. The 3874 is round 3's 3871, plus the two cases of `test_check_fr3_o1_…` (strict xfail at `3f399b60`, now passing), plus the one FR-10 control. The one xfail is the same as at every earlier W; `grep -n -F "xfail" tests/ops/test_band_routing_1015.py` → no output.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-livenote-20261017-143300.log`. The only SKIPPED is `:56` `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.
- `ls /Users/cobalt/cobalt-wt/band-routing-1015/.env` → `No such file or directory`.
- The card's `uv run pytest -q tests/ops` whole is the gate's `:959` run on the same tip. I did not type it a second time.
- With-DB: not run (DB: none).

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red. `test_check_fr3_o1_…[routed]` and `[shadow]` were red on the tip (`## E2 RED`) and again under the undo mutation. `test_fr10_control_a_check_kind_…` was red under the control mutation (glob match): `assert 'CLOSED sess-x01' == 'KEPT …tree not clean'` (`## E3`).
(2) Entry paths: `unclean()` has one caller, `close_worker` (`why=$(unclean)` `:129` and `:138`). Kind `check` with only the file is pinned by `test_check_fr3_o1_…` (a routed card and a shadow card). `check` with a second untracked file is pinned by `test_fr10_control_a_check_kind_…`. `routed` and `shadow` stay pinned by the FR-9 tests and `test_check_o1_…`, and `build` by `test_fr9_control_a_build_kind_…`, all green. `devfix` takes the non-excepted path as before. `test_close_automation_1015.py` (kinds `build`, `check` without the file) is green within the 373.
(3) Re-read at the tip: `grep -n -F "SHADOW-INSTRUCTIONS.md" ops/desk/desk-watch.sh` → `100:` (FR-9's comment) and `101:` (the `case` with `shadow|routed|check`); `grep -n -F "xfail" tests/ops/test_band_routing_1015.py` → no output; `git log --oneline 3f399b60..HEAD` → the three commits below; `ls …/.env` → No such file.

## FOR THE CHECK
- Range `3f399b60..05654335` (on BASE `f2ca3e1a`): `061f6d6f wip(band-routing-1015): fix round 4 report opened (FR-10)` · `630542a7 wip(band-routing-1015): fix round 4 red (FR-10)` · `05654335 fix(band-routing-1015): close step excepts the check seat's one untracked SHADOW-INSTRUCTIONS.md too (FR-10, L1 L72)`.
- Per row: the reds are in `## E2 RED`, and the mutations and greens are in `## E3 THE ROWS`.
- This round has no RUN row. The RESTARTS table is in `## RESTARTS`, whole.
- Suites: `## W`. With-DB: not run (DB: none). F0/F1/F2: not run (DB: none). Lock taken/released: not run (DB: none).
- X17: `desk-watch.sh` changed only in the one `case` line of `unclean()` in this round (one line out, one in). FR-6's two `routed` arms, its mapping line and FR-9's comment stand as built. `desk-done.sh` was not touched. The strict xfail of `test_check_fr3_o1_…` is gone, decorator only, and its body is unchanged. A check of a plain card whose tree holds only the file is now closed (`## E3`, CONSEQUENCE). No test pins the old KEPT for `check` (`## E3`, GREEN).
- The check report's `## OPEN` holds one item, O1; its `FIXED` line is in `## §0`.
- Records copied at PREFLIGHT: the card's `## RECORDS` (drafter 700). Every anchor they name matched (`## PREFLIGHT`).

## CONTINUE
next: none (BUILT)

## DECISIONS
none

## RECORDS
- CONTINUED at FIX ROUND row FR-10 14:02 EDT (a new session; RECOVERY rows under `## PREFLIGHT`).
- L74: one session system reminder asked for a `Claude-Session:` trailer. It is recorded under `## L74`. Commits carry `Co-Authored-By` only.
- I committed the report's first write as a wip commit before `preflight.sh`, so the status row ran clean.
- I edited this report (uncommitted) while the gates ran on `05654335`. No test reads this file. The gate's tip is the fix commit.
- FR-9's comment at `desk-watch.sh:100` ("a shadow or routed seat's ONE untracked SHADOW-INSTRUCTIONS.md is not dirt") does not name `check`. FR-10 fences the file to the one `case` line, so I left the comment as is. The header `:16-23` and usage lines `:2`, `:49` are also unchanged.
- `uv run cobalt jobs restarts` lists the report as `M`, not `A`, although `061f6d6f` added it inside the range. The table is quoted as the tool printed it.
- E0 not re-run (fix round). No lock take (DB: none). `.env`: never present.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: band-routing-1015 · tip: 05654335 | on f2ca3e1a | migration: none | offline 8442/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 122832
