JOB: rules-cut-stoplines-1013
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1341
CLASS: K5
INSTALL: none
BRANCH: ops/rules-cut-stoplines-1013
WORKTREE: rules-cut-stoplines-1013
BASE: «FILL: BASE, the desk's 8-hex main commit at the build launch»
TIP:
REPORT: /Users/cobalt/cobalt-wt/rules-cut-stoplines-1013/docs/40 - DevDocs/reports/rules-cut-stoplines-build-2026-10-13.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-cut-stoplines-check-2026-10-13.md
HOUSE B: as needed
DB: none
RESTARTS: none
RULINGS: 2026-10-12 R1138

## ROWS

WHY: his ruling R1341 (`reports/cto-2026-10-13.md` R1341, R1344; direction file `## RULED 2026-10-13 — the rules cut list, all of it`: "the stop-line token field is added"). Map C9 (rows 335, 374, 388, 389, 390): five stop lines carry no `tokens:`; L71 wins (every worker's stop line carries its MEASURE). The field and its one-line definition are copied from `BUILD-HUB.md:111`, byte for byte: THE TOKENS LINE = `` `tokens: <n>` = the figure `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh <your session id>` prints after `context` (your session id is the last part of the job directory your prompt names), read at your last step (L71). `` (the outer backticks are this card's quoting, not part of the line). `P` = `docs/40 - DevDocs/prompts/`. Every script that reads these lines matches a prefix (`desk-done.sh:29`, `desk-watch.sh:44`, `:46`, `close-timer.sh:99`, `card-fill.sh:74`, `preflight.sh:263`, `desk-launch.sh:1568`), so a field appended at the end changes no reader. FIXED FILE: `CLOSE-HUB.md` changes only by a drafter re-issue (this card) and is read by one other house at the change (L9, L67). BASE is set after cards 478 (`CLOSE-HUB.md`) and 479 (`JUDGE-HUB.md:3`) merge.

| row | what | red first | files |
|---|---|---|---|
| T1 | `P/CLOSE-HUB.md:65` (the `CLOSE PUSHED` line): ` · for Dejan: <n>\`` at its end becomes ` · for Dejan: <n> · tokens: <n>\``; THE TOKENS LINE as a new line directly after `:66` (`\`FAILED: <step> — <reason>\``). The close cannot run that command today: its launch line (`:10`) gets the string `"Bash(sh /Users/cobalt/cobalt/ops/desk/desk-context.sh *)"` directly after `"Bash(date*)"` (the PRODWRITE-HUB precedent string, `P/PRODWRITE-HUB.md:10`, `STANDING-LIST.md:245`; R1138 class K5: an allow string serving K1-K4 goes by card; DECISIONS 4 of the draft report), and `:12` `THE LIST: 21 allow, 11 deny;` becomes `THE LIST: 22 allow, 11 deny;` with ` NEW by card 483 (his 2026-10-12 R1138, class K5): \`Bash(sh /Users/cobalt/cobalt/ops/desk/desk-context.sh *)\`, the stop line's token figure.` appended after the sentence that names the push | NEW `tests/ops/test_rules_cut_stoplines.py` on the real files: the `CLOSE PUSHED` line ends ` · tokens: <n>\``; THE TOKENS LINE occurs once in `CLOSE-HUB.md`; the close's `claude --bg ` line's `--allowedTools` (split as `tests/ops/test_hub_lines.py` `tools()` splits it) equals BASE's plus that one string after `Bash(date*)`, and its `--disallowedTools` equals BASE's. RED on BASE: the line ends `for Dejan: <n>\`` and the string is absent. `tests/ops/test_needs_his_hand.py` `test_nothing_else_changed` pins the close at 66 lines and 21 allow strings (`:25`, `:85-88`): `LINE_COUNT`'s `"CLOSE-HUB.md": 66` becomes `67` and `== 21` becomes `== 22` (RED on BASE once changed: 66 lines, 21 strings); its other asserts stand | `docs/40 - DevDocs/prompts/CLOSE-HUB.md`, `tests/ops/test_rules_cut_stoplines.py` (NEW), `tests/ops/test_needs_his_hand.py` |
| T2 | `STANDING-LIST.md` §5 records T1's string: `:175` `21 allow, 11 deny` becomes `22 allow, 11 deny`; a NEW table row directly after `:188` (the `ls`/`grep`/`tail`/`wc`/`date` row): `\| \`Bash(sh /Users/cobalt/cobalt/ops/desk/desk-context.sh *)\` \| **NEW** (card 483, his 2026-10-12 R1138, K5): the stop line's token figure \| read only \| — \|` | same test: in `STANDING-LIST.md` the §5 heading reads `22 allow, 11 deny` and the new row occurs once between the `Bash(ls *)` row and the `Bash(git push origin main)` row. RED on BASE | `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `tests/ops/test_rules_cut_stoplines.py` |
| T3 | `P/DEVFIX-HUB.md:56` (the `REBUILT` line): ` · for Dejan: <n>\`` at its end becomes ` · for Dejan: <n> · tokens: <n>\``; THE TOKENS LINE as a new line directly after `:57`. Its line already holds CLASS (a) `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` (`:12`): no string changes | same test: the `REBUILT` line ends ` · tokens: <n>\``; THE TOKENS LINE once; the `claude --bg ` line equals BASE's. RED on BASE | `docs/40 - DevDocs/prompts/DEVFIX-HUB.md`, `tests/ops/test_rules_cut_stoplines.py` |
| T4 | `P/PRODWRITE-HUB.md:52`: `\`WRITTEN · job: <JOB> · rows: <n> · backup: <path>\`` becomes `\`WRITTEN · job: <JOB> · rows: <n> · backup: <path> · tokens: <n>\``; THE TOKENS LINE as a new line directly after `:53`. Its line holds `Bash(sh /Users/cobalt/cobalt/ops/desk/desk-context.sh *)` (`:10`): no string changes. `tests/ops/test_prodwrite_hub.py:129` (`test_the_stop_line_paragraph_names_both_endings`) asserts the old literal and is changed to the new one | the changed `:129` assertion: RED on BASE (the literal with ` · tokens: <n>` is absent); the rest of `test_prodwrite_hub.py` stays green unchanged | `docs/40 - DevDocs/prompts/PRODWRITE-HUB.md`, `tests/ops/test_prodwrite_hub.py` |
| T5 | `P/SHADOW-HUB.md:61` (the `SHADOW BUILT` line): ` · wall: <minutes>\`` at its end becomes ` · wall: <minutes> · tokens: <n>\`` (the gate seat's own; `builder tokens` stays the builder's); THE TOKENS LINE as a new line directly after `:61`. Its line holds CLASS (a) (`:10`): no string changes | same test: the `SHADOW BUILT` line ends ` · tokens: <n>\``; `card-fill.sh`'s and `preflight.sh`'s prefix reads accept a line so ended (`tests/ops/test_card_fill.py`, `tests/ops/test_preflight.py` green unchanged). RED on BASE | `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `tests/ops/test_rules_cut_stoplines.py` |
| T6 | `P/JUDGE-HUB.md`: `:10` `(\`<STOP> · answered: <n> of <total> · for Dejan: <n>\`)` and `:15` `last line \`<STOP> · answered: <n> of <total> · for Dejan: <n>\`` each become `… · for Dejan: <n> · tokens: <n>\``; THE TOKENS LINE appended to `:15` after a space. Its line (`:3`, a one-off `prompt` line, `auto`) gets `"Bash(sh /Users/cobalt/cobalt/ops/desk/desk-context.sh *)"` directly after `"Bash(date*)"` (DECISIONS 4) | same test: both stop texts end ` · tokens: <n>\``; the judge's line's `--allowedTools` equals BASE's plus that string after `Bash(date*)`; `sh /Users/cobalt/.claude/ops/desk-launch.sh prompt` with `DESK_LAUNCH_DRY=1` on a tmp copy of the repo (the shape of `tests/ops/test_desk_launch_prechecks.py`) prints the line and refuses nothing. RED on BASE | `docs/40 - DevDocs/prompts/JUDGE-HUB.md`, `tests/ops/test_rules_cut_stoplines.py` |
| T7 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`; quote the table and the `RESTARTS:` line (expected none) | — (output quoted) | none |

## NOT IN THIS JOB
- The `FAILED` stop lines (no field added); every other line of the six files; `CLOSE-HUB.md:15`, `:16`, `:44` (card 478); `JUDGE-HUB.md:3`'s pointer (card 479).
- `ops/desk/` scripts: no reader changes (all read a prefix); `bare-guard.py` is not touched (the close and judge are no guard kind, `bare-guard.py:95-103`).
- `STANDING-LIST.md` outside §5 (cards 481, 482; `:107` is card 481's row S7a).
- Any file under `/Users/cobalt/Vault`; any `src/` or `configs/` file; any with-DB test (`DB: none`).

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-map-2026-10-13.md` C9; rows 335, 374, 388-390.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md` line 111 (THE TOKENS LINE's source); `CLOSE-HUB.md` lines 10-12, 63-66; `DEVFIX-HUB.md` lines 12-14, 55-57; `PRODWRITE-HUB.md` lines 10-12, 51-53; `SHADOW-HUB.md` lines 10, 60-61; `JUDGE-HUB.md` whole; `STANDING-LIST.md` lines 175-191, 236-253.
- `tests/ops/test_prodwrite_hub.py` lines 118-131; `tests/ops/test_hub_lines.py` lines 50-120.

## CHECK ASKS
- X1 Does every stop line of the six fixed files (the five of C9 plus `BUILD-HUB.md`, `CHECK-HUB.md` as they stand) now carry `tokens: <n>`, and can each seat run the command its TOKENS LINE names on its own line?
- X2 Does any script, test or watch read one of the five lines past its prefix, so that the appended field changes what it reads?
- X3 Does the close or the judge launch (dry) still pass every refusal of `desk-launch.sh` with the added string?
FOR THE CHECK: rules cut 2026-10-13 HIS RULING: the whole cut list executed (13 contradictions, 25 stale, 40 duplicate groups deleted; moves as mapped; preferences to preferences.md; L82-L84 added, vetoable)
FOR THE CHECK: rules-cut cards 2026-10-13 brain: 11 KEEP; STANDING-LIST:107 deleted (CHECK-HUB wins, R1340); cards fill gaps behind MVP cards

## DEPLOY PROOF
- `grep -c -F "for Dejan: <n> · tokens: <n>" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CLOSE-HUB.md"` · before `0` · after `1`
- `grep -c -F "backup: <path> · tokens: <n>" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/PRODWRITE-HUB.md"` · before `0` · after `1`
- `grep -c -F "desk-context.sh *)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/JUDGE-HUB.md"` · before `0` · after `1`

## RECORDS
- Reads by the drafter `draft-rules-cut-cards`, 2026-10-13 07:20-07:45 ET, at `main` HEAD `7516154c`; `ops`, `tests` and the prompts folder clean but one untracked dated prompt.
- `git show HEAD:` of `CLOSE-HUB.md`, `JUDGE-HUB.md` whole; `grep -n -E "^\`?(REBUILT|WRITTEN|SHADOW BUILT|SHADOW ROLE|FAILED)|STOP LINE|desk-context|ops/desk/\*|tokens"` over DEVFIX, PRODWRITE, SHADOW: `DEVFIX-HUB.md:12` (CLASS (a) on the line), `:55-57`; `PRODWRITE-HUB.md:10` (`desk-context.sh *` on the line), `:51-53`; `SHADOW-HUB.md:10` (CLASS (a)), `:60-61`. `CLOSE-HUB.md:65` the `CLOSE PUSHED` line, `:66` the `FAILED` line, `:10` the line (no `sh` string), `:12` `THE LIST: 21 allow, 11 deny`. `JUDGE-HUB.md:3` the line (no `sh` string), `:10`, `:15` the stop text.
- `BUILD-HUB.md:111` holds THE TOKENS LINE byte for byte (`grep -n` output, 07:3x ET).
- Stop-line readers (`Grep` of `ops/desk`): `desk-done.sh:29` `done_re='^CLOSE PUSHED'`; `desk-watch.sh:44`, `:46` `^(SHADOW BUILT|…)`, `^(CLOSE PUSHED|FAILED)`; `close-timer.sh:99` `"CLOSE PUSHED "*`; `card-fill.sh:74` `SHADOW BUILT · job: (\S+) · tip: ([0-9a-f]{8})(?=\s|$)`; `preflight.sh:263`, `desk-launch.sh:1568` `"SHADOW BUILT · job: $job · tip: $tip "*`. No reader anchors at `for Dejan:` (`grep -rn` of `ops/desk`, no output).
- `tests/ops/test_prodwrite_hub.py:129` asserts `` `WRITTEN · job: <JOB> · rows: <n> · backup: <path>` `` in the STOP LINE section; `test_shadow_hub_file.py` pins no stop-line text; `tests/ops/test_needs_his_hand.py:25` pins `"CLOSE-HUB.md": 66` lines and `:85-88` 21 allow, 11 deny on the close's line (`sed -n 1,100p`); card 484 edits the same `LINE_COUNT` line, so the two build one after the other; `test_hub_lines.py` pins the close's production strings only (`PROD_ALLOW_TODAY`).
- `STANDING-LIST.md:175` `21 allow, 11 deny`; `:188` the `ls`/`grep`/`tail`/`wc`/`date` row; `:189` the push row; `:245` the PRODWRITE desk-context row (precedent).
