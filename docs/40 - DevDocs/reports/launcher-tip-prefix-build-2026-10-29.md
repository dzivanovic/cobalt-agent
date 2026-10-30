# launcher-tip-prefix — build report 2026-10-29

## §0 Headline
- The check launcher (`desk-launch.sh` check kind) and the check PREFLIGHT's SHADOW arm (`preflight.sh`) now admit a stop line whose tip is the card TIP plus hex (git's 9-hex form); other tips, shorter tips and non-hex tails still refuse.
- Rows T1, A1, A2 built; tip `2edcf295` on `4f1c991f`; offline 9181/0, live-note 148/0, `tests/ops` 4143 passed; DB: none; RESTARTS: none.
- Two decisions, none for Dejan: T1 (f)'s `tipz` case moved to its own test so a pinned 386 case count holds; `preflight.sh:273` left loose as the card fences.

## L74
- 19:02 ET: a system reminder in this session asked commits to end with a `Claude-Session:` line. Recorded as data (L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-29/1085-launcher-tip-prefix-card.md"` (19:02 ET), exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-29/1085-launcher-tip-prefix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-29/1085-launcher-tip-prefix-card.md" · 0 · c2054e15e3e90d72d2f4898172702c7699481a2e
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-29/1085-launcher-tip-prefix-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
DB: none card: no lock, no `<FP>`.

`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, exit 0:
```
clock · date · 0 · Thu Oct 29 19:03:00 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/launcher-tip-prefix
    ?? "docs/40 - DevDocs/reports/launcher-tip-prefix-build-2026-10-29.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 4f1c991f3 docs(desk): R2581-R2582 route (b), amend drafter r2 and card 1085 preflight launched
diff · git diff --stat 4f1c991f · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/launcher-tip-prefix · 0 · 4f1c991f3 docs(desk): R2581-R2582 route (b), amend drafter r2 and card 1085 preflight launched
env here · ls /Users/cobalt/cobalt-wt/launcher-tip-prefix/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat 4f1c991f` | 0 | `4f1c991f3 … docs(desk): R2581-R2582 route (b), amend drafter r2 and card 1085 preflight launched` · `docs/40 - DevDocs/reports/cto-2026-10-29.md \| 8 +++++---` · `1 file changed, 5 insertions(+), 3 deletions(-)` |
| symbol: hex8 TIP | Read `ops/desk/desk-launch.sh:2091` | 0 | `    hex8 TIP "$tip"` |
| symbol: the two case arms | Grep `tip: \$` in `ops/desk` | 0 | `desk-launch.sh:2133: "BUILT · job: $job · tip: $tip"\|"BUILT · job: $job · tip: $tip "*) ;;` · `desk-launch.sh:2134: "SHADOW BUILT · job: $job · tip: $tip"\|"SHADOW BUILT · job: $job · tip: $tip "*)` · `:2135 [ -n "$shadow" ] \|\| refuse "not built — $last" ;;` · `:2136 *) refuse "not built — $last" ;;` |
| symbol: not-changed sites | same Grep | 0 | `desk-launch.sh:1523: "BUILT ·"*"tip: $hr_tip"*) ;;` · `desk-launch.sh:1810: "BUILT ·"*"tip: $ctip"*) return 0 ;;` · `deploy-step0.sh:783: "BUILT ·"*"tip: $ctip"*)` · `deploy-card.sh:264: "BUILT ·"*"tip: $hr_tip"*) ;;` |
| symbol: `:1773` | Read `desk-launch.sh:1773-1774` | 0 | `# check H1: the tip is a commit, compared in its 8-hex short form as deploy-step0.sh reads it` · `ltip=$(git -C "$REPO" rev-parse --verify --quiet --short=8 "$ltip^{commit}")` |
| symbol: preflight arms | same Grep | 0 | `preflight.sh:273: "BUILT · job: $job · tip: $tip"*"self-check: "[0-3]" of 3"*)` · `preflight.sh:285: "SHADOW BUILT · job: $job · tip: $tip"\|"SHADOW BUILT · job: $job · tip: $tip "*)` |
| symbol: tests | Read | 0 | `test_desk_launch_prechecks.py:53 OTHER_TIP = "0000beef"` · `:103 self.tip = short(self.job_wt)` · `:141 def built_line` · `:145 def write_build_report` · `:195 def launch` · `:203 def called` · `:342 "BUILT · job: x-job · tip: TIP9 \| on x",` · `:391 def shadow_built` · `:411 ("tip9", False),` · `:420 "tip9": shadow_built(desk, tip=desk.tip + "9"),`; `test_preflight.py:423 SHADOW_LAST = (` · `:430 def write_shadow_card` · `:443 def test_386_c1_a_shadow_check_whose_report_ends_shadow_built_passes` · `:462 (SHADOW_LAST.replace("tip: {tip}", "tip: {tip}9"), "shadow/x-job", True),` |
| wc | `wc -l …` | 0 | `2820 ops/desk/desk-launch.sh` · `310 ops/desk/preflight.sh` · `1585 tests/ops/test_desk_launch_prechecks.py` · `558 tests/ops/test_preflight.py` |
| READ report | `tail -n 3 ".../cto-2026-10-29.md"` | 0 | last line: `HANDOVER: predecessor dfaeff87 → successor 877b6a4f at 17:48 · pane w2:pV1`; `grep -n -F "\| R2571 "` → `19:\| R2571 \| 18:05 ET \| DESK RECORD (brain, L79): 1082 check refused, 9-hex tip (4th). …` |
| restarts | `uv run cobalt jobs restarts 4f1c991f..HEAD` | 0 | `docs/40 - DevDocs/reports/launcher-tip-prefix-build-2026-10-29.md A DOCS -` · `RESTARTS: none` (the untracked report only; no code path) |

Card records copied: (1) drafter `draft-launcher-tip-prefix`, main HEAD `c29d13e9`, file:lines read with `git grep` — re-read here at BASE: `desk-launch.sh:2133-2134`, `:1523`, `:1810`, `preflight.sh:273`, `:285`, `deploy-step0.sh:783`, `deploy-card.sh:264` all at the named lines (Grep above). (2) `/Users/cobalt/.claude/ops/*.sh` symlinks: not re-read (no `ls -l` string on the list). (3) `install-ops` links by name: not re-read.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `4f1c991f`, exit 0: `5038 passed, 878 skipped, 4 xfailed, 36 warnings in 827.76s (0:13:47)` — 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`, exit 0: `146 passed, 1 skipped, 15 warnings in 29.60s`; the skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests only, on BASE's `ops/` (19:18 ET). No with-DB red (DB: none).

T1 RUN `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_launch_prechecks.py -k "1085 or test_386_a2"`, exit 1: `2 failed, 9 passed, 177 deselected, 15 warnings in 5.82s`
- RED (a) `test_1085_t1_a_nine_hex_tip_on_the_built_line_launches`: `REFUSED: not built — BUILT · job: x-job · tip: 6c5223599 | on 7143a15e | migration: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0` · `assert 1 == 0` — the row's reason.
- RED (f) `test_386_a2_job_and_tip_are_exact_as_for_built[tip9-True]`: `REFUSED: not built — SHADOW BUILT · job: x-job · tip: 9abb5d229 | on dd6529f8 | …` · `assert 1 == 0` — the row's reason.
- GREEN boundary controls: (b) `test_1085_t1_a_different_eight_hex_prefix_refuses`, (c) `test_1085_t1_a_nine_char_tip_with_a_non_hex_tail_refuses[z]` and `[9z]`, (d) `test_1085_t1_a_shorter_tip_refuses`, `test_386_a2_…[tipz-False]`, and the other `test_386_a2` cases (9 passed).
- (e) `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_launch_prechecks.py -k test_l2`, exit 0: `9 passed, 179 deselected` (the `TIPz` row refuses on BASE).

A2 RUN `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_preflight.py -k "1085 or test_386_c"`, exit 1: `1 failed, 10 passed, 40 deselected, 15 warnings in 3.17s`
- RED `test_1085_a2_a_shadow_check_with_a_nine_hex_tip_passes`: `report · … · 0 · SHADOW BUILT · job: x-job · tip: 8c8b29139 | on base | …` then `FAILED PREFLIGHT: report` · `assert 1 == 0` — the row's reason.
- GREEN: the `{tip}z` row of `test_386_c2_…` and every other `test_386_c` case.

## E3 THE ROWS
Lines re-read before the edit: `desk-launch.sh:2129-2138`, `preflight.sh:268-292` (Read).

| row | change | tests at the fix |
|---|---|---|
| T1 | `tests/ops/test_desk_launch_prechecks.py`: new `test_1085_t1_a_nine_hex_tip_on_the_built_line_launches`, `test_1085_t1_a_different_eight_hex_prefix_refuses`, `test_1085_t1_a_nine_char_tip_with_a_non_hex_tail_refuses[z,9z]`, `test_1085_t1_a_shorter_tip_refuses`; `test_l2_…` row `TIP9` → `TIPz`; `test_386_a2_…` `("tip9", True)` and new `("tipz", False)` | (with A1) `188 passed` |
| A1 | `ops/desk/desk-launch.sh:2132-2147`: `tiptail` = what follows the literal `BUILT · job: $job · tip: $tip` (or `SHADOW BUILT · …`); its first word holding any `[!0-9a-f]` → `refuse "not built — $last"`; then the two arms as prefix globs, the shadow arm still gated on `$shadow`, `*) refuse` unchanged; comment `card 1085` | `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_launch_prechecks.py` → `188 passed, 15 warnings in 75.49s` |
| A2 | `ops/desk/preflight.sh:285-298`: the SHADOW arm as a prefix glob, `ok=0` only when the tip's tail is hex and `$shadow`; BUILT arm `:273` untouched; comment `card 1085`; `tests/ops/test_preflight.py`: new `test_1085_a2_a_shadow_check_with_a_nine_hex_tip_passes`, `test_386_c2_…` row `{tip}9` → `{tip}z` | `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_preflight.py` → `51 passed, 15 warnings in 9.63s` |

Both files together at the fix: `239 passed, 15 warnings in 86.43s`.

MUTATIONS (Edit tool, undone with the Edit tool):
- A1 undo (`*[!0-9a-f]*)` → `?*)`: any tail refused), `-k "1085 or test_386_a2 or test_l2"` → `2 failed, 18 passed`: `FAILED …::test_1085_t1_a_nine_hex_tip_on_the_built_line_launches`, `FAILED …::test_386_a2_job_and_tip_are_exact_as_for_built[tip9-True]`; first line `REFUSED: not built — BUILT · job: x-job · tip: 0d7e97879 | …`.
- A1 control break (`*[!0-9a-f]*)` → `*[!0-9a-z]*)`), same `-k` → `4 failed, 16 passed`: `test_l2_a_report_not_ending_in_its_built_line_refuses[BUILT · job: x-job · tip: TIPz | on x]`, `test_1085_t1_a_nine_char_tip_with_a_non_hex_tail_refuses[z]`, `[9z]`, `test_386_a2_…[tipz-False]`; first line `assert 0 == 1` (the launcher launched).
- A2 undo (`*[!0-9a-f]*) ;;` → `?*) ;;`), `-k "1085 or test_386_c"` → `1 failed, 10 passed`: `FAILED tests/ops/test_preflight.py::test_1085_a2_a_shadow_check_with_a_nine_hex_tip_passes`; first line `FAILED PREFLIGHT: report` · `assert 1 == 0`.
- A2 control break (`*[!0-9a-f]*) ;;` → `*[!0-9a-z]*) ;;`), same `-k` → `1 failed, 10 passed`: `FAILED …::test_386_c2_…[SHADOW BUILT · job: x-job · tip: {tip}z | … -shadow/x-job-True]`.
- After each undo: `git diff --stat` → `ops/desk/desk-launch.sh | 14 ++++++++++++--` · `ops/desk/preflight.sh | 18 +++++++++++++-----` (the fix only), then committed.
- (b) `different_eight_hex_prefix` and (d) `shorter_tip` stay green under these mutations: they are the card's GREEN-before-and-after boundary controls of the unchanged literal prefix (green on BASE, E2; green at the fix).

Commit `79f14e9e8 fix(launcher-tip-prefix): check launcher and check preflight admit the card TIP plus hex on the stop line (T1, A1, A2, L1, L72)`.

DevDocs line: no page under `docs/40 - DevDocs/cobalt/` holds `ops/desk/desk-launch.sh` or `preflight.sh` (Grep `desk-launch|preflight\.sh` there → only `cobalt/jobs/restarts.md`, a different module); none written (RECORDS).

## RESTARTS
`uv run cobalt jobs restarts 4f1c991f..HEAD`, exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/reports/launcher-tip-prefix-build-2026-10-29.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/preflight.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
tests/ops/test_preflight.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
(a0) `git diff --name-only --no-renames 4f1c991f`, exit 0: `ops/desk/desk-launch.sh` · `ops/desk/preflight.sh` · `tests/ops/test_desk_launch_prechecks.py` · `tests/ops/test_preflight.py` — every path under `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**.

FIRST ROUND at `79f14e9e` — a red E2 / E3 did not show:
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops`, exit 1: `1 failed, 4142 passed, 1 xfailed, 16 warnings in 952.97s (0:15:52)`. The red: `tests/ops/test_check_hub_shadow.py:118` `test_build_report_case_count_matches_collection` · `AssertionError: assert 59 == 58` — it pins the `-k 386` case count (`58`) stated in `launcher-shadow-check-build-2026-10-11.md:140`; T1 (f)'s added `test_386_a2_…[tipz-False]` made it 59.
- The offline gate call started at `79f14e9e` was stopped before its verdict (its tip was superseded); no verdict is claimed from it.
- FIX inside the rows' files only: the `tipz` case left `test_386_a2_…` and became `test_1085_t1_f_a_shadow_tip_with_a_non_hex_tail_refuses` (same `shadow_built(desk, tip=desk.tip + "z")` line, same `refused(… "not built — <line>")`). `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_check_hub_shadow.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_preflight.py` → `244 passed, 16 warnings in 91.62s`. Its mutation (A1 `*[!0-9a-f]*)` → `*[!0-9a-z]*)`): `FAILED tests/ops/test_desk_launch_prechecks.py::test_1085_t1_f_a_shadow_tip_with_a_non_hex_tail_refuses` · `1 failed, 187 deselected`; undone, `git diff --stat` → the test move only. Commit `2edcf295e fix(launcher-tip-prefix): the shadow tipz control as its own test_1085 test, the 386 case count stays 58 (T1, L1)`. DECISION T1-f below.
- RESTARTS again at `2edcf295`: the same five rows, `RESTARTS: none`. `git diff --name-only --no-renames 4f1c991f` again: the same 4 paths.

`<tip>` = `2edcf295`.

THE SUITES at `2edcf295`:
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-tip-prefix offline`, exit 0: `tests/ops: run (ops/desk/desk-launch.sh)` · `offline 9181/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-tip-prefix-offline-20261029-194229.log` (log `:958` `5038 passed, 878 skipped, 4 xfailed, 36 warnings in 821.73s`; `:1033` `4143 passed, 1 xfailed, 16 warnings in 913.67s`). This build adds: `test_1085_t1_a_nine_hex_tip_on_the_built_line_launches`, `test_1085_t1_a_different_eight_hex_prefix_refuses`, `test_1085_t1_a_nine_char_tip_with_a_non_hex_tail_refuses[z]`, `[9z]`, `test_1085_t1_a_shorter_tip_refuses`, `test_1085_t1_f_a_shadow_tip_with_a_non_hex_tail_refuses`, `test_1085_a2_a_shadow_check_with_a_nine_hex_tip_passes`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-tip-prefix livenote`, exit 0: `live-note 148/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-tip-prefix-livenote-20261029-201147.log` (`:57` `148 passed, 1 skipped, 15 warnings in 28.92s`; `:56` the one skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops`, exit 0: `4143 passed, 1 xfailed, 16 warnings in 922.80s (0:15:22)`.
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/launcher-tip-prefix/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown red against a mutation or negative control: (a) E2 red + A1 undo red; (f) `tip9` E2 red + A1 undo red; `test_1085_a2_…` E2 red + A2 undo red; (c) `[z]`, `[9z]` and (e) `TIPz` red under the A1 control break; `test_1085_t1_f_…` red under the A1 control break (W first round); the `{tip}z` row of `test_386_c2_…` red under the A2 control break; (b) and (d) are the card's GREEN-before-and-after controls of the unchanged literal prefix (green at BASE, E2, and at the fix) — they are not reds of this fix by the card's own row. 3 of 3 held as the card defines.
(2) Every entry path pinned: the launcher's check kind is reached only by `desk-launch.sh check <card> [PASS-2|<step>]` (`grep -rn -F "desk-launch.sh check" ops/desk` → `desk-launch.sh:18`, `:19`, the usage lines); the read under change runs when `$pass2` is empty — first launch (T1 tests) and a step resume (`test_l2_a_check_resume_still_needs_the_built_line`, green); PASS-2 bypasses it (`test_l2_a_pass_2_launch_keeps_the_test_it_has`, green). BUILT and SHADOW BUILT, shadow and non-shadow cards (`test_386_a3_a4_…`, `test_386_a5_…`, green); edge inputs: 9-hex, other 8-hex, 7-hex, `z`, `9z`, bare SHADOW line (`bare-True`). `preflight.sh check`: shadow 9-hex (`test_1085_a2_…`), `{tip}z`, off-card shadow lines (`test_386_c2_…`).
(3) Re-read at the tip: `grep -n -F "card 1085"` → `desk-launch.sh:2132`, `preflight.sh:285`; `grep -n -F "def test_1085"` → `test_desk_launch_prechecks.py:354`, `:361`, `:368`, `:374`, `:462`, `test_preflight.py:454`; `git log --oneline 4f1c991f..HEAD` (below); the gate logs by `grep -n -F`.

## FOR THE CHECK
- Range `4f1c991f..2edcf295`: `e6bed1797 wip(launcher-tip-prefix): red` · `79f14e9e8 fix(launcher-tip-prefix): check launcher and check preflight admit the card TIP plus hex on the stop line (T1, A1, A2, L1, L72)` · `2edcf295e fix(launcher-tip-prefix): the shadow tipz control as its own test_1085 test, the 386 case count stays 58 (T1, L1)`.
- Per row reds, mutations and greens: `## E2 RED`, `## E3 THE ROWS`, `## W` first round (quoted there).
- Caller greps: `## PRE-STOP SELF-CHECK` (2); sites not changed: `## PREFLIGHT`.
- RUN rows' output: `## E2 RED` (the two RUN commands, summaries and every red's first line).
- Suites: `## W` — offline `9181/0`, live-note `148/0`, `tests/ops` `4143 passed`; with-DB `not run (DB: none)`. `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: `## RESTARTS` (`RESTARTS: none`, the same at `2edcf295`).
- DEPLOY PROOF counts at the tip: `card 1085` — 1 line in `desk-launch.sh`, 1 in `preflight.sh`; `test_1085` defs — 5 in `test_desk_launch_prechecks.py`, 1 in `test_preflight.py` (the grep above).
- Records copied at PREFLIGHT: `## PREFLIGHT`.

## CONTINUE
next: none (BUILT)

## DECISIONS
- DECISION T1-f: card T1 (f) says to add a `("tipz", False)` case to `test_386_a2_job_and_tip_are_exact_as_for_built`. Doing so made `tests/ops/test_check_hub_shadow.py:118` red (`assert 59 == 58`: it pins the `-k 386` count of `launcher-shadow-check-build-2026-10-11.md:140`), a file outside the rows. Safe default taken, inside the rows' files only: the same `tipz` assertion lives in its own `test_1085_t1_f_a_shadow_tip_with_a_non_hex_tail_refuses` (shown red under mutation), the `tip9` case flipped as the card says, the 386 count stays 58. If the desk wants the case inside `test_386_a2_…`, the pinned count (an old report and its test) is a separate item.
- DECISION NOT-IN-JOB: `ops/desk/preflight.sh:273`, the BUILT arm, still admits any tail after `tip: $tip` before `self-check: ` (hex or not); the card fences it out (`## NOT IN THIS JOB`), so it is a separate item; untouched.

## RECORDS
- L74: one system reminder asked commits to carry a `Claude-Session:` line; recorded under `## L74`, not followed.
- The offline gate call started at `79f14e9e` (task stopped before its verdict, its tip superseded); a second offline gate call ran at `2edcf295`. A `tests/ops` run at `79f14e9e` (red, `## W`) and one at `2edcf295` (green).
- DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/desk-launch.sh` or `ops/desk/preflight.sh`; no dated line written.
- The card's records as re-read at PREFLIGHT: the file:lines matched at BASE; the `~/.claude/ops` symlinks and `install-ops` behaviour not re-read (no listed string reads them).
- No lock taken (DB: none); `.env` never present.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: launcher-tip-prefix · tip: 2edcf295 | on 4f1c991f | migration: none | offline 9181/0 | with-DB 0/0 | live-note 148/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 163769
