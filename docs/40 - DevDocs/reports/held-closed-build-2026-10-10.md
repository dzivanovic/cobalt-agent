# held-closed-1010 — build report (card 317, 2026-10-10)

## §0 Headline
- H1–H4 built on `26327808`, tip `ca5c11aa`. A held check now ships on its fix round when the fix report names each held id once, in a FIXED line or a CARRIED line.
- One rule text, `held_n` plus `held_rule`, sits byte for byte in `deploy-card.sh`, `desk-launch.sh` and `deploy-step0.sh`; a test pins the three copies equal. n = 0 rows take today's code.
- Suites: offline 4199/0, live-note 146/0, `tests/ops` 2969 passed, 1 xfailed. DB: none. RESTARTS: none.
- One decision: the card misstates one H3 red on BASE (below). Nothing for Dejan.

## L74
- The session's system reminder (21:50 ET) asked for a `Claude-Session:` line on commits. Recorded once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/317-held-closed-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/317-held-closed-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/317-held-closed-card.md" · 0 · b7c86cd8f84f0c519d497d563814dcf1f117e3e5
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/317-held-closed-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R438 row · grep -n "^| R438 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 173:| R438 | 10-05 15:42 ET | HIS RULING: next flow (`next-flow-answer-2026-10-05.md`) only for features drafted after K3, P2, D5 DEPLOYED; after D5 a drafter writes changes 1-4 into the hubs (applied: contract, NOW 15:42; [words](cto-2026-10-05-words.md#r438)). | HIS RULING · APPROVED |
RULING 2026-10-05 R438 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R438 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 8e5b72b05c0c2566b49eb4b46d42969b4c4e5453
RULING 2026-10-05 R438 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Sat Oct 10 21:50:03 EDT 2026
status · git status --short --branch · 0 · ## ops/held-closed-1010
head · git log --oneline -1 · 0 · 26327808 docs(desk): R993 brain direction card 298 deploy, drafter 316
diff · git diff --stat 26327808 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/held-closed-1010 · 0 · 26327808 docs(desk): R993 brain direction card 298 deploy, drafter 316
env here · ls /Users/cobalt/cobalt-wt/held-closed-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/f4-refresh-1010/.env
PREFLIGHT OK
```
- `git show --stat 26327808` → `docs(desk): R993 brain direction card 298 deploy, drafter 316`; `316-draft-held-closed-row.md | 6 ++++++`, `cto-2026-10-10.md | 1 +`; 2 files, 7 insertions.
- DB: none: no lock probe, no with-DB string used.

| rule | command | exit | output |
|---|---|---|---|
| symbols | `grep -n -F "held unfixed: 0" ops/desk/deploy-card.sh ops/desk/deploy-step0.sh` | 0 | `deploy-card.sh:172` refusal; `:201` SHIPS row; `deploy-step0.sh:340` `lits=$(printf 'held unfixed: 0\nready: YES\n%s\n' "$lits")` (also comments `:9`, `:24`) |
| symbols | `grep -n -F "fixed_ok" ops/desk/desk-launch.sh` | 0 | `959: fixed_ok() {`; `973: [ -n "$ltip" ] && { [ "$ltip" = "$ctip" ] \|\| [ "$ltip" = "$shead" ] \|\| fixed_ok; }` |
| symbols | `grep -n -E "^def (check_line\|fix_round\|…)" tests/ops/…` | 0 | `test_deploy_card.py:40 check_line`, `:239 test_a_check_line_with_a_held_defect_is_refused`, `:442 fix_round`, `:487 test_no_fix_report_leaves_every_cell_empty`, `:581 test_a_fix_report_round_trips_through_the_launchers_ships_checked`; `test_deploy_step0.py:78 check_line`, `:546 test_o1_…`, `:578 fix_round`, `:619 test_f2_a_fix_round_row_passes_p2_and_step0`, `:637 test_f2_a_fix_round_missing_one_proof_still_fails_p2`; `test_desk_launch_prechecks.py:68 check_line`, `:559 fix_round`, `:589 test_f1_a_fix_round_past_the_checked_tip_launches` |
| symbols | `grep -n -E "^set \|held_\|hr_\|…"` the three scripts | 0 | `set -u` in all three, `set -f` in step0; no `held_`/`hr_` name taken; `rn=` only at `desk-launch.sh:250` |
| READ | `grep -n -F "HELD, NOT FIXED" …/house-seat-order-check-2026-10-10.md`; `grep -n "^## " …` | 0 | under `## RUNS` (`:68`–`:72`) exactly one row: `:69` `- O1 · own · …HELD, NOT FIXED…`; other hits at `:5` (§0), `:99` (`## OPEN`), `:106` (`## DECISIONS`) |
| READ | `tail -n 3 …/house-seat-order-check-2026-10-10.md` | 0 | last line `CHECK DONE · job: house-seat-order-1010 · pass: 1 · tip: ed48d80d · … · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · … · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 153447` |
| wc | `wc -l` of the rows' files | 0 | deploy-card.sh 285 · desk-launch.sh 1327 · deploy-step0.sh 526 · test_deploy_card.py 616 · test_deploy_step0.py 687 · test_desk_launch_prechecks.py 1144 · DEPLOY-HUB.md 181 · CARD.md 139 |
| RESTARTS | `uv run cobalt jobs restarts 26327808..HEAD` | 0 | `path change rule restart` / `RESTARTS: none` (empty range) |

Card `## RECORDS`, copied: the R993 brain direction (row H, R438); the symlink `~/.claude/ops/desk-launch.sh` → `/Users/cobalt/cobalt/ops/desk/desk-launch.sh` (edit the repo file only); the HEAD reads of the cited lines; the check report's last line and one held id O1 at `:69`; RESTARTS none for `ops/desk/`. Re-read here: the check report lines (table above) and every cited line of the three scripts (Read of each file, lines as the card gives them).

## E0 BASELINE
- Offline on `26327808`: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 662.27s (0:11:02)`; 0 failed, 0 errors.
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.88s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Commit `cdb84761` `wip(held-closed-1010): red — H1 H2 H3 held-check tests` (test files only). Run on BASE code: `uv run pytest -q -p no:cacheprovider --color=no --tb=no -rfp tests/ops/test_deploy_card.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_deploy_step0.py -k "h1 or h2 or h3"` → `55 failed, 5 passed, 222 deselected, 15 warnings in 33.26s`.
- H1 (26 red): every held test's first failing line is `REFUSED: alpha: the check's last line lacks 'held unfixed: 0': CHECK DONE · job: x · pass: 2 · tip: … · held unfixed: 1 · open: 1 · ready: NO · …` (the row's named reason; seen for the writes, the FIXED refusals and the CARRIED refusals). `test_h1_the_rule_is_one_text_in_the_three_scripts` red: no script holds `# ---- THE RULE (card 317`.
- H2 (12 red): each refusal's first failing line `assert 0 == 1` with the dry launch lines printed (the launch runs, the row's named reason), including `test_h2_a_held_check_at_the_code_tip_without_a_fix_report_is_refused`.
- H3 (17 red): `FAILED STEP-0: P2 check 1 — …/alpha-check-2026-01-02.md — the last line lacks 'held unfixed: 0': CHECK DONE · job: x · pass: 1 · tip: … · held unfixed: 1 · open: 1 · ready: NO · …` (quoted for `test_h3_a_held_row_with_a_fixed_line_per_id_passes_p2` and `test_h3_a_held_check_at_the_code_tip_without_a_fix_report_fails_p2`).
- PASSED on BASE (pins, as the card says): `test_h1_held_check_without_a_fix_report_is_still_refused`, `test_h2_a_held_row_with_a_fixed_line_per_id_launches`, `test_h2_a_carried_line_with_a_strict_xfail_test_and_a_desk_record_row_launches`, `test_h2_a_mix_of_one_fixed_and_one_carried_id_launches`, `test_h2_a_clean_cell_over_a_held_check_line_is_refused_by_the_literal_loop`.
- One red differs from the card's text: the card says `test_h3_a_held_check_at_the_code_tip_without_a_fix_report_fails_p2` is "RED on BASE: P2 passes"; on BASE P2 fails on `lacks 'held unfixed: 0'` (`:340` prefixes the clean pair), so the test is red because the id is not named. DECISION H3 below.

## E3 THE ROWS
Commit `ca5c11aa` `feat(held-closed-1010): a held check ships on its fix round — one FIXED or CARRIED line per held id, read the same by deploy-card.sh, desk-launch.sh and deploy-step0.sh (H1 H2 H3 H4, L3 L67 L75)`.

| row | change (at the tip) | greens |
|---|---|---|
| THE RULE | `# ---- THE RULE (card 317 …` to `# ---- end of THE RULE`: `deploy-card.sh:135-302`, `desk-launch.sh:905-1072`, `deploy-step0.sh:139-306`; `held_n` (`:150` / `:920` / `:154`), `held_rule` (`:154` / `:924` / `:158`) | `test_h1_the_rule_is_one_text_in_the_three_scripts` |
| H1 | `deploy-card.sh:344-352`: `frep` moved before the check line's refusals, and with a fix report `hn=$(held_n "$last")` (`:348`); `:172-173`'s two refusals run only when `hn` is empty. `:373`: `held_rule "$job" … "$fixtip" "$head" "$frep" \|\| refuse`. The SHIPS row writes `held unfixed: $hn` and `ready: NO` for a held row; otherwise today's line. Header comment `:16-19` | `tests/ops/test_deploy_card.py` 76 passed (after H1) |
| H2 | `desk-launch.sh:1142-1147`: `hn=$(held_n "$clast")`; held → `held_rule "deploy $sbranch" "$crep" "$clast" "$ctip" "$shead" "$frep" \|\| refuse "$held_why"`, before the `:973` tip short-circuit. The literal loop and `fixed_ok` are unchanged | prechecks + deploy-card: 217 passed |
| H3 | `deploy-step0.sh:511-518`: a row whose literals name `held unfixed: <n>` (n ≥ 1) and `ready: NO` drops the clean-pair prefix (`hrn`). `:559` makes the exact n compare. `:562-563` runs `held_rule "$branch" "$report" "$last" "$ctip" "$head" "$frep"` on any held line before the tip test. The dry-run list is unchanged. Header `:27-30` | step0 + deploy-card: 141 passed |
| H4 | `DEPLOY-HUB.md:59` and `CARD.md:48`: one sentence each, joined to the existing line | `grep -c -F -e "FIXED: <finding id> — <test id>"` → DEPLOY-HUB 1, CARD 1; `"CARRIED: <finding id> — <test id> — R<n>"` DEPLOY-HUB → 1; `"CARRIED"` CARD → 1; `"has no FIXED line"` DEPLOY-HUB → 1; `wc -l` 181 / 139 (unchanged); `tests/ops/test_hub_lines.py tests/ops/test_deploy_card.py` → `96 passed`. On BASE, the CARD.md line 48 shown by `git show 26327808:…CARD.md` and the DEPLOY-HUB line 59 read before the edit hold no such text |

All four test files together at the fix: `301 passed, 15 warnings in 124.57s`.

MUTATIONS (each made with Edit, run, then undone with Edit; `git diff --stat` after all of them showed only the fix's 5 files, `558 insertions(+), 9 deletions(-)`):
- H1 (a) `deploy-card.sh` `hn=$(held_n "$last")` → `hn=""`: `-k h1` → `25 failed, 2 passed`. All writes and refusals are red; the two that pass are the pin and the one-text test.
- H1 (b) `held_rule … || refuse "$held_why"` → `|| :`: `22 failed, 5 passed`. Every refusal is red; the three writes, the pin and the one-text test stay green.
- H2 `desk-launch.sh` `|| refuse "$held_why"` → `|| :`: `-k h2` → `12 failed, 4 passed`. All 11 refusals and the code-tip test are red. The 4 that pass are pins, green on BASE by the card's design.
- H3 (a) `|| why=$held_why` → `|| :` plus the exact compare off (`false &&`): `-k h3` → `14 failed, 3 passed`. The refusals and the code-tip test are red.
- H3 (b) the exact compare alone off: `…[held unfixed 10 against n = 1]` → `1 failed`.
- H3 (c) the prefix forced (`if true || …`): the three pass tests → `3 failed`.
- One text: one copy's `lines` → `line(s)`: `test_h1_the_rule_is_one_text_in_the_three_scripts` → `1 failed`, diff `- RRIED line(s) in the fix report $hr_frep"`.
No named test stayed green under its mutation.

DevDocs: `ops/desk/` has no page under `docs/40 - DevDocs/cobalt/`. The only hit for the three script names there is `jobs/restarts.md`, which is not their page. No line written (RECORDS).

## RESTARTS
`uv run cobalt jobs restarts 26327808..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/held-closed-build-2026-10-10.md	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_card.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
RESTARTS: none
```

## W THE THREE SUITES
- (a0) `git diff --name-only --no-renames 26327808` → `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_card.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py`. Each path starts with `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 8 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh held-closed-1010 offline` → `offline 4199/0`; `log: /Users/cobalt/cobalt-wt/.gate-logs/held-closed-1010-offline-20261010-222101.log`.
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops` → `2969 passed, 1 xfailed, 15 warnings in 558.37s (0:09:18)`. Tests this build adds: H1 `test_h1_*` (27 cases), H2 `test_h2_*` (16), H3 `test_h3_*` (17).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh held-closed-1010 livenote` → `live-note 146/0`; `log: /Users/cobalt/cobalt-wt/.gate-logs/held-closed-1010-livenote-20261010-223201.log`. `grep -n -F "COBALT_LIVE_VAULT_ROOT"` on the log matches only `:2`, the command line, so no skip names it.
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/held-closed-1010/.env` → `No such file or directory` (22:32 ET).

## PRE-STOP SELF-CHECK
1. Every added or changed test was shown red for its named reason against BASE or a mutation, as quoted in E2 and the E3 MUTATIONS. The 5 pins are green on BASE by the card's design. The changed `check_line` helpers (an `open` parameter, default `0`) are covered by the existing tests, which stay green.
2. Callers by `grep` at the tip: `held_rule` is called at `deploy-card.sh:373`, `desk-launch.sh:1146` and `deploy-step0.sh:563`. H1, H2 and H3 respectively pin each call. `held_n` sites: `deploy-card.sh:348` (H1, with and without `--fix-report`: `test_h1_held_check_without_a_fix_report_is_still_refused`), `desk-launch.sh:1144` (H2, including the code-tip case), `deploy-step0.sh:559`/`:562` (H3, exact n and the code-tip case). The n = 0 paths are pinned by today's tests: `test_no_fix_report_leaves_every_cell_empty`, `test_a_check_line_with_a_held_defect_is_refused`, `test_a_fix_report_round_trips_through_the_launchers_ships_checked`, `test_f1_a_fix_round_past_the_checked_tip_launches`, `test_f2_a_fix_round_row_passes_p2_and_step0` and the four `test_f2_a_fix_round_missing_one_proof_still_fails_p2` cases, all in the 301 / 2969 passed.
3. Line numbers re-read at the tip with `grep -n -E "held_n|held_rule|THE RULE"` on the three scripts (22:32 ET), `git log --oneline 26327808..HEAD`, and the H4 `grep -c` / `grep -n` and `wc -l` above.

## FOR THE CHECK
- Range `26327808..ca5c11aa`: `cdb84761 wip(held-closed-1010): red — H1 H2 H3 held-check tests`, `ca5c11aa feat(held-closed-1010): a held check ships on its fix round — … (H1 H2 H3 H4, L3 L67 L75)`.
- Per row: reds in E2; mutations and greens in E3; suites in W.
- with-DB: not run (DB: none). F0 / F1 / F2: not run (DB: none). Lock taken and released: not run (DB: none).
- X1, n = 0: `deploy-card.sh` runs `:172-173` and today's SHIPS line whenever `hn` is empty, which covers no `--fix-report` or a line without `held unfixed: <n≥1>`. In `desk-launch.sh` and `deploy-step0.sh` the new code runs only when `held_n` finds n ≥ 1; step0's prefix line is unchanged in the else branch.
- X2: every `held_why` begins `<who>:` (job, `deploy <branch>`, or the ship's branch) and names the id. The count, `open:` and `ready:` refusals name the listed ids in parentheses. `_fix_refused` asserts `--out` unwritten and `desk.state()` unchanged.
- X3: covered by `test_h1_a_held_check_missing_one_proof_is_refused` cases: an ASCII hyphen, an indented line, an id with a space, `held unfixed: 10` against one row, `open:` not n, and an unlisted id.
- X4: one text in all three scripts (pinned). The callers differ in two ways, by design. deploy-card takes the held path only with a `--fix-report` (card: "n ≥ 1 with no fix report is refused as today"). step0 also compares the row's n with the line's n exactly.
- X5: on BASE, P2 refuses the row H1 writes. E2's H3 reds show `the last line lacks 'held unfixed: 0'`.
- Limits of the static read, for the check to weigh:
  - the decorator block is the contiguous non-blank, non-comment lines above the `def`;
  - a class-level decorator or a class-level `pytestmark` holding xfail is not seen;
  - `pytest.param(..., marks=xfail)` and `pytest.xfail()` in a body are not seen.
  The gate still runs every named test.
- The desk report for a CARRIED row is read at the repo's `HEAD` (`git show HEAD:…cto-<date>.md`), as `authorize.sh` reads rulings.
- Records copied at PREFLIGHT: see `## PREFLIGHT`.

## CONTINUE
next: none — BUILT

## DECISIONS
- DECISION H3: the card says `test_h3_a_held_check_at_the_code_tip_without_a_fix_report_fails_p2` is "RED on BASE: P2 passes". On BASE, P2 fails instead, because `:340` prefixes `held unfixed: 0`. The test is still red on BASE: it asserts the id-naming text, which BASE never prints. Safe default taken: the test stands as written, and the red is recorded as observed in E2. No code depends on this.

## RECORDS
- L74: the `Claude-Session:` request in the session reminder was not acted on (see `## L74`).
- DevDocs: no page for `ops/desk/` exists under `docs/40 - DevDocs/cobalt/`; none written. Precedent: launcher-1010, ops-hand-1010 and orphan-clean-1010 changed `ops/desk/` with no DevDocs line.
- No lock taken; `.env` never present in this worktree. A sibling `.env` sat in `f4-refresh-1010` at PREFLIGHT, not this job's.
- The card's records were re-read at PREFLIGHT: the check report's `## RUNS` O1 row is at `:69`, and its last line carries `held unfixed: 1 · open: 1 · … ready: NO`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: held-closed-1010 · tip: ca5c11aa | on 26327808 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 301182
