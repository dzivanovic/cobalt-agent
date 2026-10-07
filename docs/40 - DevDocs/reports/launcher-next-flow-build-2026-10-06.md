# launcher-next-flow — build report 2026-10-06

## §0 Headline
- N6: `desk-launch.sh` and `deploy-step0.sh` read the fix report with `git show <row's branch head>:<path>`. A copy on `main` is never read. An absent blob refuses.
- N7: `desk-launch.sh recut` cuts a too-long failed line to desk-row.sh's 300. It keeps the head through the first ` — ` and the tail from ` · rollback:`, and marks the cut `…`.
- N8: `deploy-card.sh --tickers` (default `none`) writes `TICKERS:` after `SET:`. CARD.md has one new row and DEPLOY-HUB.md:101 one new phrase (+44 bytes).
- Tip `055018c0` on `8e33fdc4`. Offline 3963/0, live-note 146/0, `tests/ops` 1476 passed. DB: none, so no lock was taken. RESTARTS: none. One DECISION (a fixture follow-up, not for Dejan).

## L74
- One system reminder, after the launch message, asked commits to end with a `Claude-Session:` line. Recorded as data and not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/63-launcher-next-flow-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/63-launcher-next-flow-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/63-launcher-next-flow-card.md" · 0 · be9f880c691ae170fb5f89a9c9e6891125abcdea
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/63-launcher-next-flow-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-06 R588 row · grep -n "^| R588 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 86:| R588 | 19:30 ET | HIS RULING (L79, via brain) ([words](cto-2026-10-06-words.md) `## R588`): build next-flow changes 6, 7, 8 (`next-flow-answer-2026-10-05.md`) tonight, as card `63`. | HIS RULING · APPROVED |
RULING 2026-10-06 R588 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R588 |" -- "docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · be9f880c691ae170fb5f89a9c9e6891125abcdea
RULING 2026-10-06 R588 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
- `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, whole:
```
clock · date · 0 · Tue Oct  6 19:30:48 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/launcher-next-flow-1006
    ?? "docs/40 - DevDocs/reports/launcher-next-flow-build-2026-10-06.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 8e33fdc4 docs(desk): his R587 single-feature deploy cards by the desk, applied to contract, L61, K10a
diff · git diff --stat 8e33fdc4 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/launcher-next-flow-1006 · 0 · 8e33fdc4 docs(desk): his R587 single-feature deploy cards by the desk, applied to contract, L61, K10a
env here · ls /Users/cobalt/cobalt-wt/launcher-next-flow-1006/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- `git show --stat 8e33fdc4` → `docs(desk): his R587 single-feature deploy cards by the desk, applied to contract, L61, K10a`; `docs/40 - DevDocs/reports/cto-2026-10-06-words.md | 3 +++`, `docs/40 - DevDocs/reports/cto-2026-10-06.md | 1 +`, `2 files changed, 4 insertions(+)`.
- THE CARD'S SYMBOLS (BASE `8e33fdc4`; the card cites main `3053fb9c`, and every line below matched):
  - `grep -n -E "frep|fix report|fixed_ok" ops/desk/desk-launch.sh ops/desk/deploy-step0.sh` (the N6 proof list, BEFORE):
```
ops/desk/desk-launch.sh:806:        frep=$(ship_cell "$srow" 8)
ops/desk/desk-launch.sh:840:        # code tip, and the row's `fix report` is committed and ends `BUILT · … tip: <code tip>`
ops/desk/desk-launch.sh:841:        fixed_ok() {
ops/desk/desk-launch.sh:842:            [ -n "$frep" ] || return 1
ops/desk/desk-launch.sh:843:            case "$frep" in
ops/desk/desk-launch.sh:847:            [ -f "$frep" ] || return 1
ops/desk/desk-launch.sh:848:            [ -n "$(git -C "$REPO" log -1 --format=%H -- "$frep")" ] \
ops/desk/desk-launch.sh:849:                && git -C "$REPO" diff --quiet -- "$frep" \
ops/desk/desk-launch.sh:850:                && git -C "$REPO" diff --cached --quiet -- "$frep" || return 1
ops/desk/desk-launch.sh:852:            flast=$(grep -v '^[[:space:]]*$' "$frep" | tail -n 1)
ops/desk/desk-launch.sh:858:        [ -n "$ltip" ] && { [ "$ltip" = "$ctip" ] || [ "$ltip" = "$shead" ] || fixed_ok; } \
ops/desk/desk-launch.sh:1042:    [ -n "$step" ] || [ ! -e "$report" ] || refuse "the devfix report already exists: $report (a new worker names its CONTINUE step)"
ops/desk/deploy-step0.sh:338:    frep=$(printf '%s\n' "$line" | awk -F'|' '{print $8}' | tr -d '`' | sed -e 's/^ *//' -e 's/ *$//')
ops/desk/deploy-step0.sh:385:            # a fix round (his R376, L75): the row's `fix report` ends `BUILT · … tip: <code tip>` and
ops/desk/deploy-step0.sh:387:            if [ -n "$why" ] && [ -n "$t" ] && [ -n "$frep" ]; then
ops/desk/deploy-step0.sh:389:                [ -f "$frep" ] && flast=$(grep -v '^[[:space:]]*$' "$frep" | tail -n 1)
ops/desk/deploy-step0.sh:392:                        # the hub's P2 fix-round line: the fix report committed and unmodified
ops/desk/deploy-step0.sh:393:                        frel=$(rel "$frep")
ops/desk/deploy-step0.sh:397:                            why="$why; the fix report $frep is not committed and unmodified (commit '${flog:-none}')"
ops/desk/deploy-step0.sh:401:                            why="$why, nor its ancestor (fix report $frep)"
ops/desk/deploy-step0.sh:403:                    *) why="$why; the fix report $frep does not end 'BUILT · … tip: $ctip': ${flast:-absent}" ;;
```
  (`:1042` is the devfix report, not the fix report.)
  - callers: `grep -rn -F "fixed_ok" ops` → `desk-launch.sh:841` (def), `:858` (its one call). `grep -rn -F "ships_checked" ops` → `desk-launch.sh:790` (def), `:997` (its one call). `grep -rn -F "deploy-card.sh" ops` → `deploy-card.sh:2`, `:43`, `:215` (its own lines only).
  - Read: `desk-launch.sh:790-872` (`ships_checked`, `:806` `frep=…`, `:841-857` `fixed_ok`, `:858-859` the `neither the code tip` refuse); `:1054-1127` (`recut`; `:1066` `last=`, `:1071-1074` the `rollback: used` / bar refusals, `:1106-1108` `text` / `rlen` / the 300 refuse, `:1124` `desk-row.sh RECORD "$text"`); `deploy-step0.sh:129-134` (`rel`), `:335` (`head=`), `:338`, `:385-404`; `desk-row.sh:52` (`if size(row) > 300:`); `deploy-card.sh:2`, `:43`, `:44-57`, `:193-203` (`SET: $set` at `:203`); `gate.sh:100` (`""|,*|*,|*,,*|*[!A-Z0-9.,]*) refuse …`); `CARD.md:26` (the `SET` row), `:135`; `DEPLOY-HUB.md:101` holds the phrase `the set's \`--tickers\` and \`--migration\` as the card gives them` (Read).
  - `grep -n -i -F "tickers" ops/desk/gate.sh ops/desk/deploy-card.sh ops/desk/card-fill.sh CARD.md` → only `gate.sh` lines `2, 19, 72, 84, 97, 98, 100, 102, 112, 160, 161, 163, 187, 463, 466, 467, 473, 476`; none in `deploy-card.sh`, `card-fill.sh` or `CARD.md`.
  - `wc -l`: `desk-launch.sh` 1197 · `deploy-step0.sh` 526 · `deploy-card.sh` 218 · `test_desk_launch_prechecks.py` 1118 · `test_deploy_step0.py` 647 · `test_desk_launch_recut.py` 285 · `test_deploy_card.py` 390 · `CARD.md` 138 · `DEPLOY-HUB.md` 181. `wc -c DEPLOY-HUB.md` → `57017`.
  - Test counts BEFORE (`uv run pytest -qq --collect-only … `): `test_deploy_card.py: 27`, `test_deploy_step0.py: 44`, `test_desk_launch_prechecks.py: 124`, `test_desk_launch_recut.py: 10`.
  - `tail -n 3` of the `## READ` reports: `next-flow-answer-2026-10-05.md` → last line `Send changes 1–4 to a drafter as rows for CHECK-HUB, BUILD-HUB and the drafter prompt shape, in one card. …`; `deploy-deploy-drc-d5-o1-b2-1006.md` → last line `FAILED: resume — (b) no \`GATE GREEN on <m1>\` and no \`<restart set>\`: the earlier run failed at STEP-T before the gate; the desk recuts · rollback: not used · decisions: 3 · for Dejan: 0 · tokens: 83489`. Its lines 75, 95, 105 were read: the add/add cause on the hand copy, DECISION 2, and the fix report row.
- Card `## RECORDS` copied: (1) citations proven at main HEAD `3053fb9c` by Read / Grep (drafter); re-read here at BASE `8e33fdc4`, and every cited line matched (above). (2) His R438 approves `next-flow-answer-2026-10-05.md`; changes 6-8 were read there (lines 15, 17, 19).
- `uv run cobalt jobs restarts 8e33fdc4..HEAD` → `docs/40 - DevDocs/reports/launcher-next-flow-build-2026-10-06.md	A	DOCS	-` / `RESTARTS: none`. The range has no commit; the one row is this report, untracked.
- DB: none. No lock probe was run and nothing was proven by a first with-DB use.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3963 passed, 787 skipped, 1 xfailed, 36 warnings in 616.83s (0:10:16)`, exit 0. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.00s`. The one skip is `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which names no `COBALT_LIVE_VAULT_ROOT`.
- The four row files on BASE: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_prechecks.py tests/ops/test_deploy_step0.py tests/ops/test_desk_launch_recut.py tests/ops/test_deploy_card.py` → `205 passed, 15 warnings in 81.80s`.

## E2 RED
Commit `2bf4a37b wip(launcher-next-flow): red — N6 fix report at the branch head, N7 recut fits its row, N8 deploy card TICKERS` (4 test files only; no `src/`, no script). DB: none, so no with-DB red and no lock.
`uv run pytest -q -p no:cacheprovider --color=no --tb=no -rf <the four files>` → `13 failed, 206 passed, 15 warnings in 86.22s`. The 13:
```
  FAILED tests/ops/test_desk_launch_prechecks.py::test_f1_a_fix_round_past_the_checked_tip_launches
  FAILED tests/ops/test_desk_launch_prechecks.py::test_n6_the_branch_heads_copy_decides_never_a_copy_on_main[wrong last line]
  FAILED tests/ops/test_desk_launch_prechecks.py::test_n6_the_branch_heads_copy_decides_never_a_copy_on_main[right last line]
  FAILED tests/ops/test_deploy_step0.py::test_o1_a_fix_round_row_the_launcher_accepts_passes_p2
  FAILED tests/ops/test_deploy_step0.py::test_f2_a_fix_round_row_passes_p2_and_step0
  FAILED tests/ops/test_deploy_step0.py::test_o1r2_a_fix_report_absent_at_the_branch_head_fails_p2[absent at the branch head]
  FAILED tests/ops/test_deploy_step0.py::test_o1r2_a_fix_report_absent_at_the_branch_head_fails_p2[cell path never committed]
  FAILED tests/ops/test_deploy_step0.py::test_n6_the_branch_heads_copy_decides_never_a_copy_on_main[wrong last line]
  FAILED tests/ops/test_deploy_step0.py::test_n6_the_branch_heads_copy_decides_never_a_copy_on_main[right last line]
  FAILED tests/ops/test_desk_launch_recut.py::test_n7_a_long_failed_line_is_cut_to_fit_the_desk_row
  FAILED tests/ops/test_deploy_card.py::test_n8_tickers_are_written_directly_after_set
  FAILED tests/ops/test_deploy_card.py::test_n8_no_tickers_given_writes_none - ...
  FAILED tests/ops/test_deploy_card.py::test_n8_card_md_row_and_deploy_hub_phrase
```
First lines of the reds (quoted from `--tb=line` / `--tb=short` runs):
- N6 launcher: `REFUSED: deploy ops/x-job: the check's tip 'b0ad8674' is neither the code tip 29b589ee nor the branch head 61d1dd70 — the check is not clean: …` (`test_f1_a_fix_round_past_the_checked_tip_launches`, `assert 1 == 0`). The cell's file is absent on `main`. `[wrong last line]`: the same refusal (the main copy is read). `[right last line]`: `assert 0 == 1`, because the launch went through on the main copy (`RUN: git -C … worktree add -b deploy/x-deploy …`).
- N6 step-0: `FAILED STEP-0: P2 check 1 — …/alpha-check.md — its tip f493ebff is not the row's code tip 42c3d5bb; the fix report …/alpha-fix-build.md does not end 'BUILT · … tip: 42c3d5bb': absent` (`test_o1_a…`). The cell's file is absent on `main`. `[absent at the branch head]`: `… alpha-fix-build-2.md is not committed and unmodified (commit 'none')` against the new `is absent at the branch head a49563b4` text.
- N7: `REFUSED: recut: the desk row would be 509 characters, over desk-row.sh's 300: RECUT x-deploy attempt 2 — FAILED: gate — G (c) — tests/cobalt/test_x.py::test_y …`
- N8: `REFUSED: unknown option '--tickers'; usage: deploy-card.sh …` (`assert 1 == 0`); `KeyError: 'TICKERS'`; `assert 0 == 1 … grep_c(…CARD.md, "| \`TICKERS\` | — | — | optional | …")`.
NEGATIVE CONTROLS green on BASE (among the 206 passed): launcher `test_f1_a_fix_round_missing_one_proof_still_refuses` (a) empty cell, (b) ×2, (c) report not at the branch head, (d) not an ancestor; `test_f1_a_fix_report_outside_the_reports_folder_still_refuses`; `test_f1_a_card_of_todays_shape_passes_as_today` ×2. Step-0 `test_f2_a_fix_round_missing_one_proof_still_fails_p2` (a), (b), (c) fix report not at the branch head, (d) not an ancestor. Recut `test_a_failed_deploy_is_recut_and_its_launch_printed_in_order` (a); `test_n7_a_long_line_the_cut_does_not_reach_still_refuses` (b) no rollback field and (c) rollback used. Deploy card `test_n8_tickers_outside_the_gates_pattern_are_refused` ×4 (`zz`, `A,,B`, `A,B,`, `A'B`) and every existing test of the file.
Re-pointed fixtures (N6): launcher `fix_round` and step-0 `fix_round` / `test_o1_a…` write the report on the branch head (a docs-only commit past the fix; the row's head cell is that commit). `(c) report uncommitted` becomes `(c) report not at the branch head`. `test_f1_a_fix_report_edited_after_its_commit_still_refuses` is replaced by `test_n6_the_branch_heads_copy_decides_never_a_copy_on_main` (launcher). `test_o1r2_…` becomes `test_o1r2_a_fix_report_absent_at_the_branch_head_fails_p2` (`edited after its commit` is replaced by step-0's `test_n6_…`; `never committed` becomes `absent at the branch head`). The helper `neither()` now names the row's real branch head (`desk.fix_head`), not the code tip. Two lines of `test_f1_a_fix_report_outside_the_reports_folder_still_refuses` follow the fixture (DECISION N6-1).
Test counts AFTER E2 (`--collect-only -qq`): `test_desk_launch_prechecks.py` 124 → 125 · `test_deploy_step0.py` 44 → 47 · `test_desk_launch_recut.py` 10 → 13 · `test_deploy_card.py` 27 → 34.

## E3 THE ROWS
Commit `055018c0 feat(launcher-next-flow): fix report read at the branch head, recut fits its desk row, deploy card carries TICKERS (N6, N7, N8, L1, L3)`: 5 files, `50 insertions(+), 29 deletions(-)`.

**N6.** `desk-launch.sh` `fixed_ok`: `:847-850` (`[ -f ]`, `git log -1`, `git diff --quiet`, `git diff --cached --quiet`) are replaced by `fblob=$(git -C "$REPO" show "$shead:${frep#"$REPO"/}" 2>/dev/null) || return 1`. `flast` is read from `$fblob`. The cell read, the `$REPORTS/*.md` test, the ancestor test and the `BUILT ·`…`tip: $ctip` test stay, and the comment is reworded. `deploy-step0.sh` P2 check 1: `[ -f "$frep" ]`, `frel`, `flog`, `fdiff` and the `is not committed and unmodified` refusal are gone. `if fblob=$(git -C "$REPO" show "$head:$(rel "$frep")" 2>/dev/null)` reads the blob. An absent blob refuses `the fix report $frep is absent at the branch head $head`. The `BUILT ·` test, the ancestor test and the `does not end` refusal stay, and the comment is reworded. The proof list AFTER (`grep -n -E "frep|fix report|fixed_ok" ops/desk/desk-launch.sh ops/desk/deploy-step0.sh`):
```
ops/desk/desk-launch.sh:806:        frep=$(ship_cell "$srow" 8)
ops/desk/desk-launch.sh:840:        # code tip, and the row's `fix report`, read at the row's branch head (`git show`, card 63
ops/desk/desk-launch.sh:842:        fixed_ok() {
ops/desk/desk-launch.sh:843:            [ -n "$frep" ] || return 1
ops/desk/desk-launch.sh:844:            case "$frep" in
ops/desk/desk-launch.sh:848:            fblob=$(git -C "$REPO" show "$shead:${frep#"$REPO"/}" 2>/dev/null) || return 1
ops/desk/desk-launch.sh:856:        [ -n "$ltip" ] && { [ "$ltip" = "$ctip" ] || [ "$ltip" = "$shead" ] || fixed_ok; } \
ops/desk/desk-launch.sh:1040:    [ -n "$step" ] || [ ! -e "$report" ] || refuse "the devfix report already exists: $report (a new worker names its CONTINUE step)"
ops/desk/deploy-step0.sh:338:    frep=$(printf '%s\n' "$line" | awk -F'|' '{print $8}' | tr -d '`' | sed -e 's/^ *//' -e 's/ *$//')
ops/desk/deploy-step0.sh:385:            # a fix round (his R376, L75): the row's `fix report`, read at the row's branch head
ops/desk/deploy-step0.sh:389:            if [ -n "$why" ] && [ -n "$t" ] && [ -n "$frep" ]; then
ops/desk/deploy-step0.sh:391:                if fblob=$(git -C "$REPO" show "$head:$(rel "$frep")" 2>/dev/null); then
ops/desk/deploy-step0.sh:398:                                why="$why, nor its ancestor (fix report $frep)"
ops/desk/deploy-step0.sh:400:                        *) why="$why; the fix report $frep does not end 'BUILT · … tip: $ctip': ${flast:-absent}" ;;
ops/desk/deploy-step0.sh:403:                    why="$why; the fix report $frep is absent at the branch head $head"
```
No line reads the fix report from the main checkout. The same grep re-run at the tip `055018c0` gives these lines unchanged; every hit lies above N7's insertion at `:1104`.
After N6: `uv run pytest … tests/ops/test_desk_launch_prechecks.py tests/ops/test_deploy_step0.py` → `172 passed, 15 warnings in 72.61s`.

**N7.** `desk-launch.sh` `recut`: before `text=` (old `:1106`), ONE fitting step (now `:1104-1118`). A `python3 -c` measures `| R0000 | 00:00 ET | RECUT <job> attempt <n> — <last> | RECORD |`, the same measure as `rlen`. When that is over 300, `last` holds a ` — ` and a ` · rollback:` after it, and the head plus `…` plus the tail fit, `last` becomes: the head through the FIRST ` — `, then `mid[:room]`, then `…`, then the tail from the LAST ` · rollback:`. Otherwise `last` is unchanged. A failed or empty fit refuses `recut: the failed line could not be fitted to desk-row.sh's 300 (python3)` (L1). `:1119-1121` (`text`, `rlen`, the 300 refuse) are as before. The row `desk-row.sh` writes is the same `text`.
After N7: `uv run pytest … tests/ops/test_desk_launch_recut.py` → `13 passed, 15 warnings in 6.64s`.

**N8.** `deploy-card.sh`: `:2` and `:43` name `[--tickers "<A,B,…>"]`. The default is `tickers="none"`. A `--tickers)` option, and a refusal `--tickers '<v>' must be none or A,B,… of [A-Z0-9.]` unless the value is `none` or passes gate.sh's `""|,*|*,|*,,*|*[!A-Z0-9.,]*` (`:100`). The header line `TICKERS: $tickers` follows `SET: $set`. `CARD.md`: ONE row after the `SET` row (the card's text verbatim), and `` `SET`, `TICKERS`. `` on the deploy-card line (old `:135`). `DEPLOY-HUB.md:101`: the one phrase replaced; `git diff --stat` → `DEPLOY-HUB.md | 2 +-`; `wc -c` 57017 → 57061 (**+44 bytes**).
After N8: `uv run pytest … tests/ops/test_deploy_card.py` → `34 passed, 15 warnings in 9.84s`.

THE DEPLOY GATE of the card (on the fix, before commit): the four files → `219 passed, 15 warnings in 91.40s`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1476 passed, 1 xfailed, 15 warnings in 378.01s`.

THE MUTATIONS (each made with Edit, run alone, undone with Edit):
| # | row | mutation | run | result |
|---|---|---|---|---|
| 1 | N6 launcher, undo | `fblob=$(cat "$frep" 2>/dev/null)` (the main checkout's file) | `-k "f1 or n6"` prechecks | `3 failed, 10 passed`: `test_f1_a_fix_round_past_the_checked_tip_launches`, `test_n6_…[wrong last line]`, `test_n6_…[right last line]` |
| 2 | N6 launcher, control (d) | ancestor test `\|\| true` | same | `1 failed, 12 passed`: `test_f1_a_fix_round_missing_one_proof_still_refuses[(d) checked tip not an ancestor]` |
| 3 | N6 launcher, control (c) | `git show … \|\| cat "$WT/x-job/<rel>"` (a worktree copy in no commit) | same | `1 failed, 12 passed`: `…[(c) report not at the branch head]` |
| 4 | N6 step-0, undo | `fblob=$(cat "$frep" 2>/dev/null)` | `-k "o1 or f2 or n6"` step-0 | `7 failed, 3 passed`: `test_o1_a…`, `test_f2_a_fix_round_row_passes_p2_and_step0`, `test_f2_…[(c) fix report not at the branch head]`, `test_o1r2_…[absent at the branch head]`, `test_o1r2_…[cell path never committed]`, `test_n6_…[wrong last line]`, `test_n6_…[right last line]` |
| 5 | N6 step-0, control (d) | ancestor test → `if true` | same | `1 failed, 9 passed`: `test_f2_…[(d) checked tip not an ancestor]` |
| 6 | N7, undo | the cut → `pass` | `-k n7` recut | `1 failed, 2 passed`: `test_n7_a_long_failed_line_is_cut_to_fit_the_desk_row`, first line `REFUSED: recut: the desk row would be 509 characters, over desk-row.sh's 300: …` |
| 7 | N7, control (b) | a cut with no ` · rollback:` too (`elif … last[:i+3] + … + "…"`) | recut file | `1 failed, 12 passed`: `test_n7_a_long_line_the_cut_does_not_reach_still_refuses[(b) no rollback field]` |
| 8 | N8, undo | no `TICKERS: $tickers` line | `-k n8` card | `2 failed, 5 passed`: `test_n8_tickers_are_written_directly_after_set`, `test_n8_no_tickers_given_writes_none` (`KeyError: 'TICKERS'`) |
| 9 | N8, controls | the pattern → `"")` only | same | `4 failed, 3 passed`: `test_n8_tickers_outside_the_gates_pattern_are_refused[zz]`, `[A,,B]`, `[A,B,]`, `[A'B]` |
After every undo, `git diff --stat` showed the tree back at the fix (`git diff ops/desk/desk-launch.sh` read whole after mutation 3). The commit is the tree the four files ran green on. `test_n8_card_md_row_and_deploy_hub_phrase` reads the two docs. Its red is the E2 red (`assert 0 == 1`), and no mutation of a script reaches it.
DevDocs line: none written. No page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/`: `grep -rl -F "desk-launch.sh" "docs/40 - DevDocs/cobalt"` → only `jobs/restarts.md`, the RESTARTS rule of another module; Grep `deploy-step0.sh|deploy-card.sh` across DevDocs outside `reports/` and `prompts/` → `No files found`. Earlier builds on `ops/desk/` did the same (`close-timer-build-2026-10-03.md:89`, `worker-steps-build-2026-10-02.md:157`).

## RESTARTS
`uv run cobalt jobs restarts 8e33fdc4..HEAD` (HEAD `055018c0`) → whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/launcher-next-flow-build-2026-10-06.md	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_card.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_recut.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row. The table matches the card's expectation (`RESTARTS: none`).

## W THE THREE SUITES
`<tip>` = `055018c0`. The card says DB: none, so W is (a0), (a) and (e).
- (a0) `git diff --name-only --no-renames 8e33fdc4` → whole: `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_card.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_desk_launch_recut.py`. Every path starts with `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 9 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-next-flow-1006 offline` → exit 0: `offline 3963/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-next-flow-1006-offline-20261006-200350.log`. In the log (`grep -n -F " passed"`): `862: 3963 passed, 787 skipped, 1 xfailed, 36 warnings in 607.98s (0:10:07)`. This build adds no test under `tests/cobalt` or `tests/taxonomy`. Its tests are in `tests/ops`, below.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-next-flow-1006 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-next-flow-1006-livenote-20261006-201412.log`. Its one SKIPPED line (`grep -n -F "SKIPPED"`): `56: SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which names no `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` at the tip → `1476 passed, 1 xfailed, 15 warnings in 379.09s (0:06:19)`. That is 0 failed, 0 errors, and no skip. The tests this build adds or re-points, all in it: launcher `test_f1_a_fix_round_past_the_checked_tip_launches`, `test_f1_a_fix_round_missing_one_proof_still_refuses[(c) report not at the branch head]`, `test_n6_the_branch_heads_copy_decides_never_a_copy_on_main` ×2. Step-0 `test_o1_a_fix_round_row_the_launcher_accepts_passes_p2`, `test_f2_a_fix_round_row_passes_p2_and_step0`, `test_f2_a_fix_round_missing_one_proof_still_fails_p2[(c) fix report not at the branch head]` / `[(d) …]`, `test_o1r2_a_fix_report_absent_at_the_branch_head_fails_p2` ×2, `test_n6_the_branch_heads_copy_decides_never_a_copy_on_main` ×2. Recut `test_n7_a_long_failed_line_is_cut_to_fit_the_desk_row`, `test_n7_a_long_line_the_cut_does_not_reach_still_refuses` ×2. Card `test_n8_tickers_are_written_directly_after_set`, `test_n8_no_tickers_given_writes_none`, `test_n8_tickers_outside_the_gates_pattern_are_refused` ×4, `test_n8_card_md_row_and_deploy_hub_phrase`.
- No migration, no lock, no `.env`: `ls /Users/cobalt/cobalt-wt/launcher-next-flow-1006/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED for its named reason against a mutation or negative control. The E2 reds are quoted under `## E2 RED`. Each N6 / N7 / N8 test is red under mutations 1-9 (`## E3`, the table). The negative controls are pinned by mutations 2, 3, 5, 7 and 9. `test_n8_card_md_row_and_deploy_hub_phrase` is pinned by its E2 red (`assert 0 == 1`). No test stayed green under its mutation, so none was rewritten. Two tests were re-pointed during E2 for a wrong-reason red (`neither()` named the code tip as the head): they were rewritten to name the row's real head, and said so in `## E2`.
(2) Every entry path of each rule is pinned by a test. `fixed_ok` has one caller (`desk-launch.sh:856`, the deploy kind via `ships_checked` `:997`): pinned by `test_f1_*` / `test_n6_*` (launcher). Step-0 P2 check 1 is reached per SHIPS row: pinned by the step-0 `test_o1_*` / `test_f2_*` / `test_o1r2_*` / `test_n6_*`. The row with no fix report is pinned by `test_f1_a_card_of_todays_shape_passes_as_today` ×2 and `test_a_check_report_whose_tip_is_not_the_row_s_code_tip_fails`. The `recut` kind has one entry (`desk-launch.sh recut <card>`): pinned by the N7 tests and the 10 existing recut tests. `deploy-card.sh` has no caller in `ops` but its own lines (`grep -rn -F "deploy-card.sh" ops`): pinned through its CLI by `test_deploy_card.py` and `test_f1_deploy_card_writes_the_fix_report_column_and_its_empty_cell`.
(3) Every `file:line`, count and quote was re-read from tool output at the tip `055018c0`. Re-run there: `grep -n -E "frep|fix report|fixed_ok"` on both scripts (identical to `## E3`); `grep -n -F "TICKERS"` → `deploy-card.sh:210`, `CARD.md:27`, `CARD.md:136`, `DEPLOY-HUB.md:101`; `grep -n -F "card 63 N7" ops/desk/desk-launch.sh` → `1104`; `git log --oneline 8e33fdc4..HEAD` → `055018c0`, `2bf4a37b`; the test counts (`--collect-only -qq`) after E2, which E3 left unchanged; `wc -c DEPLOY-HUB.md` → `57061`.

## FOR THE CHECK
- Range `8e33fdc4..055018c0`: `2bf4a37b wip(launcher-next-flow): red — N6 fix report at the branch head, N7 recut fits its row, N8 deploy card TICKERS`, then `055018c0 feat(launcher-next-flow): fix report read at the branch head, recut fits its desk row, deploy card carries TICKERS (N6, N7, N8, L1, L3)`.
- Per row, the reds, mutation runs and greens: `## E2 RED` and `## E3 THE ROWS`. Caller greps: `## PREFLIGHT` and self-check (2). No RUN row on this card.
- Suites: offline `3963/0` (log above), with-DB `not run (DB: none)`, live-note `146/0`, `tests/ops` `1476 passed, 1 xfailed`. `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: `## RESTARTS` (`RESTARTS: none`).
- Records copied at PREFLIGHT: `## PREFLIGHT`, last bullet but two.
- On the CHECK ASKS, from what the build did (not a verdict):
  - X1: the after-grep is in `## E3`. No path reads `$frep` from the main checkout.
  - X2: both scripts read only the row's own cell path. In the launcher it must also match `$REPORTS/*.md`. Step-0 does not test the `$REPORTS` prefix, before or after (the card keeps `:387` as it is); a path outside `$REPO` is passed to `git show` as is and is absent at any head. The launcher reads `$shead` before P3 (`:858-866`) has proven it is the branch's head. A blob read at an unproven head can only end in P3's refusal (`the branch head is …, the row says …`). Step-0 reads at `$head`, the row's cell, which its own P3 then checks.
  - X3: the fit keeps the head through the FIRST ` — ` and the tail from the LAST ` · rollback:` (`rfind`). A second ` — ` (the red's `G (c) — `) falls in the cut middle. A ` · rollback:` inside the middle falls in the middle too, because the tail starts at the last one. No test pins a middle ` · rollback:`. The row is measured as `rlen` measures it (`R0000`, `00:00`), and `desk-row.sh` refuses a bar or a newline, which `:1071-1074` and a one-line `last` already exclude.
  - X4: the launcher and `deploy-step0.sh` are untouched by N8. Every existing launcher / step-0 deploy-card fixture carries no `TICKERS` line and still launches / passes (`tests/ops` green). The `none` → `--tickers` omitted rule lives in `DEPLOY-HUB.md:101` text, read by the deploy hub. No script reads `TICKERS`.

## CONTINUE
next: CLOSE (W done 20:21:22 EDT)

## DECISIONS
- DECISION N6-1 (not for Dejan): the card says `test_f1_a_fix_report_outside_the_reports_folder_still_refuses` "stays as it is". Its body reads the fix report from `desk.reports` on `main` and writes the row with `head=fixed`. After N6's re-pointed fixture there is no main copy, and the head is the docs commit past the fix. Two lines were changed so it can run: the stray copy's text is read from the branch copy (`desk.job_wt / FIX_REL`), and `head=desk.fix_head`. Its case, its stray path outside `$REPORTS`, its refusal (`neither the code tip … nor the branch head …`) and its assertions are unchanged. Safe default taken: the minimal fixture follow-up, recorded here. The other choice was to leave the test broken against the card's own re-pointed fixture.

## RECORDS
- L74: one `Claude-Session:` request (a system reminder after the launch message). Not followed. Commits carry the `Co-Authored-By` line only.
- Card `## RECORDS`, as re-read at PREFLIGHT: (1) drafter citations at `3053fb9c`; every cited line was re-read at BASE `8e33fdc4` and matched. (2) His R438 approves `next-flow-answer-2026-10-05.md`; changes 6-8 were read there.
- No extra lock take (DB: none). No `REFUSED, not needed` line. No `CONTINUE` received.
- DevDocs: no dated line, because no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` (`## E3`).
- Tokens at the last step: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh b43daef9` → `context 273122 of 400000 — ok`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: launcher-next-flow · tip: 055018c0 | on 8e33fdc4 | migration: none | offline 3963/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 273122
