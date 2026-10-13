JOB: rules-cut-hubs-1013
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1341
CLASS: K5
INSTALL: none
BRANCH: ops/rules-cut-hubs-1013
WORKTREE: rules-cut-hubs-1013
BASE: «FILL: BASE, the desk's 8-hex main commit at the build launch»
TIP:
REPORT: /Users/cobalt/cobalt-wt/rules-cut-hubs-1013/docs/40 - DevDocs/reports/rules-cut-hubs-build-2026-10-13.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-cut-hubs-check-2026-10-13.md
HOUSE B: as needed
DB: none
RESTARTS: none
RULINGS: 2026-10-12 R1138

## ROWS

WHY: his ruling R1341 (`reports/cto-2026-10-13.md` R1341, R1344; direction file `## RULED 2026-10-13 — the rules cut list, all of it`). The map's contradiction and stale rows that sit in the check flow's fixed files (`reports/rules-map-2026-10-13.md`): C3 (row 351), C4 (rows 340, 349, 350, 352, 362; R921 with R920: a check is Opus plus house A, Grok first; house B only on a `mandatory` card or none), S1 (rows 365, 366, 382; R438: one pass), S5 (row 379; R38 folded in LAWS L61). `P` = `docs/40 - DevDocs/prompts/`. Every quoted text is byte for byte; a cell's `\|` is ONE `|`. FIXED FILE: `CHECK-HUB.md`, `BUILD-HUB.md` and `DEPLOY-HUB.md` change only by a drafter re-issue (this card) and are read by one other house at the change (L9, L67); `CARD.md` is the card format every hub reads.

| row | what | red first | files |
|---|---|---|---|
| H1 | `P/CHECK-HUB.md:3` (C4): `you start TWO outside houses at once,` becomes `you start the outside houses \`## THE FLOW AND THE SEATS\` seats (house A; house B with it only on a \`mandatory\` card),` and `NO launch of any session or agent but the TWO outside houses of this check, started at once (L36);` becomes `NO launch of any session or agent but the outside houses this check seats (L36);` | NEW `tests/ops/test_rules_cut_hubs.py` on the real files: in `CHECK-HUB.md` the texts `TWO outside houses`, `Only while no other Grok hub runs`, `START HOUSE A AND HOUSE B AT ONCE`, `two different houses`, `only the two houses this file names` and `START BOTH HOUSES AT ONCE` occur zero times, and each new text of H1-H5 occurs once; the `claude --bg ` line equals BASE's. RED on BASE: each old text occurs (`TWO outside houses` twice at `:3`, `two different houses` at `:16` and `:21`, the others once) | `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `tests/ops/test_rules_cut_hubs.py` (NEW) |
| H2 | `P/CHECK-HUB.md:8` (C3, R908; C4): `Only while no other Grok hub runs (L15), no other house hub is running, also while another session holds` becomes `Also while another session holds`, and `both outside houses run in this one session` becomes `the outside houses run in this one session` | same test | `docs/40 - DevDocs/prompts/CHECK-HUB.md` |
| H3 | `P/CHECK-HUB.md:16` (C4): `START HOUSE A AND HOUSE B AT ONCE, two different houses outside Anthropic, in the background.` becomes `START HOUSE A, and HOUSE B at once with it when \`MANDATORY HOUSE B\` below seats one, houses outside Anthropic, in the background. Below, "both houses" and "house B" apply only when house B sits.`; `:21` `L67 stays: two different houses, never fewer than one other house.` becomes `L67 stays: never fewer than one other house.` | same test | `docs/40 - DevDocs/prompts/CHECK-HUB.md` |
| H4 | `P/CHECK-HUB.md:33` (C4, the same contradiction in the law line): `L36 only the two houses this file names, started at once` becomes `L36 only the houses this file seats`; `:90` `the two houses run at once and read neither list.` becomes `when house B sits, the two houses run at once and read neither list.` | same test | `docs/40 - DevDocs/prompts/CHECK-HUB.md` |
| H5 | `P/CHECK-HUB.md:92` (C4): `(5) START BOTH HOUSES AT ONCE.` becomes `(5) START THE HOUSES.` and `for each of house A and house B ONE attempt, started in two calls, one after the other, with no wait between,` becomes `for each house that sits ONE attempt (house B only when it sits: then two calls, one after the other, with no wait between),`. `:96` stands (it names house B only when it was started) | same test | `docs/40 - DevDocs/prompts/CHECK-HUB.md` |
| H6 | `P/BUILD-HUB.md:17` (C4): `runs every finding — its own and both outside houses' — and fixes what holds` becomes `runs every finding — its own and its outside houses' — and fixes what holds`; `:111` `for every finding the check and its two outside houses left` becomes `for every finding the check and its outside houses left` | same test: in `BUILD-HUB.md` `both outside houses'` and `its two outside houses` occur zero times, the new texts once; the `claude --bg ` line equals BASE's; `tests/ops/test_build_hub_no_clutter.py` stays green unchanged. RED on BASE: old texts once each | `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `tests/ops/test_rules_cut_hubs.py` |
| H7 | `P/CARD.md:5` (S1): delete ` (its second pass, \`PASS-2\`, too)`; `:21` (S1, C4): `the check then runs its second pass even when nothing is open.` becomes `the check then seats house B beside house A (\`CHECK-HUB.md\` MANDATORY HOUSE B).` | same test: in `CARD.md` `PASS-2` and `second pass` occur zero times; the new `:21` text once; `test_f1_card_md_ships_header_has_the_fix_report_column_and_a_matching_separator` (`tests/ops/test_desk_launch_prechecks.py:826`) stays green unchanged. RED on BASE: `PASS-2` occurs (`:5`) | `docs/40 - DevDocs/prompts/CARD.md`, `tests/ops/test_rules_cut_hubs.py` |
| H8 | `P/DEPLOY-HUB.md:32` (S5): `(his 2026-09-30 R38, proved by the same two commands on \`cto-2026-09-30.md\` until it is folded into LAWS)` becomes `(his 2026-09-30 R38, LAWS L61, proved by the same two commands on \`cto-2026-09-30.md\`)`; `:58` (S1): delete ` — the line of its LAST pass` | same test: in `DEPLOY-HUB.md` `until it is folded into LAWS` and `LAST pass` occur zero times; the `claude --bg ` line equals BASE's; `tests/ops/test_hub_lines.py` stays green unchanged. RED on BASE: both occur once | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `tests/ops/test_rules_cut_hubs.py` |
| H9 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`; quote the table and the `RESTARTS:` line (expected none) | — (output quoted) | none |

## NOT IN THIS JOB
- The launch line (`claude --bg `) and THE LIST of every hub; the SEAT ORDER block `CHECK-HUB.md:23-30`, which already holds R920, R921.
- `CHECK-HUB.md:94` and `:95` (the Grok and Gemini spellings; C13 keeps `gemini-3.1-pro-high`, map DECISIONS item 7); any stop line.
- `STANDING-LIST.md`: card 481. `UNATTENDED-LAUNCH.md`: card 479. The `PASS-2` code in `ops/desk/`: card 485.
- The owed hub-text card (R1295 row and the two BUILD-HUB rows, `cto-2026-10-13.md` §5): a separate card; whichever lands second takes the other's merge as BASE.
- Any file under `/Users/cobalt/Vault`; any `ops/`, `src/` or `configs/` file; any with-DB test (`DB: none`).

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-map-2026-10-13.md` `## CONTRADICTIONS` C3, C4; `## STALE` S1, S5; `## MAP` rows 340, 349-352, 362, 365, 366, 379, 382.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md` lines 1-33, 86-96; `BUILD-HUB.md` lines 17, 111; `CARD.md` lines 1-30; `DEPLOY-HUB.md` lines 26-33, 56-60.

## CHECK ASKS
- X1 Does any line of `CHECK-HUB.md` still start a second house, or a house B, on a card that is not `mandatory` (R921)?
- X2 Does any line of the four files still name a second pass, a `PASS-2` or a pass-2 line?
- X3 Is every launch line byte for byte BASE's, and do `test_hub_lines.py`, `test_check_hub_gate_wording.py`, `test_check_hub_shadow.py`, `test_build_hub_no_clutter.py` and `test_house_probe.py` (its `len(lines) == 127` of `CHECK-HUB.md`, `:193`: every edit here is inside a line, none added or removed) pass unchanged?
FOR THE CHECK: rules cut 2026-10-13 HIS RULING: the whole cut list executed (13 contradictions, 25 stale, 40 duplicate groups deleted; moves as mapped; preferences to preferences.md; L82-L84 added, vetoable)
FOR THE CHECK: rules-cut cards 2026-10-13 brain: 11 KEEP; STANDING-LIST:107 deleted (CHECK-HUB wins, R1340); cards fill gaps behind MVP cards

## DEPLOY PROOF
- `grep -c -F "AT ONCE, two different houses" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `1` · after `0`
- `grep -c -F "PASS-2" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CARD.md"` · before `1` · after `0`
- `grep -c -F "until it is folded into LAWS" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `1` · after `0`

## RECORDS
- Reads by the drafter `draft-rules-cut-cards`, 2026-10-13 07:20-07:40 ET, at `main` HEAD `7516154c`; the prompts folder clean but one untracked dated prompt (`git -C /Users/cobalt/cobalt status --short`).
- `git show HEAD:"docs/40 - DevDocs/prompts/CHECK-HUB.md"` whole; `grep -n -E "TWO|two (outside )?houses|AT ONCE|at once|other Grok|L15|second pass|PASS-2|tokens"` on it: `:3`, `:8`, `:16`, `:20`, `:21`, `:25`, `:33`, `:53`, `:59`, `:90`, `:92`, `:124`, `:127`. `:20` and `:21`'s `there is no second pass` / `NO SECOND PASS` state R438 and stand. `:24-:29` already hold R920, R921 (Read, lines 4-30).
- `grep -n -E "outside houses|two houses|until it is folded|LAST pass|last pass|PASS-2|second pass"` over `BUILD-HUB.md` and `DEPLOY-HUB.md`: `BUILD-HUB.md:17`, `:111`; `DEPLOY-HUB.md:32`, `:58`.
- `CARD.md` read whole (147 lines): `:5` `(its second pass, \`PASS-2\`, too)`, `:21` `the check then runs its second pass even when nothing is open`.
- `grep` of `tests/ops` for `AT ONCE|at once|other Grok hub|TWO outside|two outside|PASS-2|second pass|…|until it is folded|LAST pass|its two outside`: no test pins any old text of these four files (the `PASS-2` hits are launcher tests, card 485).
- H4 and H5 (`CHECK-HUB.md:33`, `:92`) are the same contradiction C4 on lines the map did not list (DECISIONS 6 of the draft report).
