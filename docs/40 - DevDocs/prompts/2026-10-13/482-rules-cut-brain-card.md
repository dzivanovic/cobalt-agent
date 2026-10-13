JOB: rules-cut-brain-1013
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1341
CLASS: K5
INSTALL: none
BRANCH: ops/rules-cut-brain-1013
WORKTREE: rules-cut-brain-1013
BASE: «FILL: BASE, the desk's 8-hex main commit at the build launch»
TIP:
REPORT: /Users/cobalt/cobalt-wt/rules-cut-brain-1013/docs/40 - DevDocs/reports/rules-cut-brain-build-2026-10-13.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-cut-brain-check-2026-10-13.md
HOUSE B: as needed
DB: none
RESTARTS: none
RULINGS: 2026-10-12 R1138

## ROWS

WHY: his ruling R1341 (`reports/cto-2026-10-13.md` R1341, R1344; direction file `## RULED 2026-10-13 — the rules cut list, all of it`: "The brain-restart rule goes to BRAIN-HUB"). Map C5 (rows 147, 321, 322, 328, 407; D11, D34): R188 wins over R76 — past 500k the brain asks for its own restart and the desk replaces it. Card 462 (`prompts/2026-10-13/462-brain-replace-card.md`, R1331) makes the scripts do it: `desk-done.sh <id> "<desk report>" brain` and `desk-launch.sh brain` replace a brain whose ask is a DESK RECORD row; a brain that has not asked is still stopped only on his word (R76). This card states the same in the brain's fixed file and the standing list. BASE is set after card 462 is DEPLOYED (the text describes what its scripts do). `B` = `docs/40 - DevDocs/prompts/BRAIN-HUB.md` at HEAD. Every quoted text is byte for byte.

| row | what | red first | files |
|---|---|---|---|
| B1 | `B:3` (C5, row 321): `you are stopped only when he says so (his 2026-09-30 R76).` becomes `you are stopped on his word (his 2026-09-30 R76), or replaced by the desk once you have asked for your replacement and the desk has recorded the ask as a DESK RECORD row (his 2026-10-02 R131, 2026-10-04 R188, R191; card 462).` | NEW `tests/ops/test_rules_cut_brain.py` on the real file: `stopped only when he says so`, `after he has stopped the brain before you` and `Once he has stopped you` occur zero times in `BRAIN-HUB.md`; each new text of B1-B3 occurs once; the one `claude --bg ` line equals BASE's (`tests/ops/test_desk_launch_brain.py` compares it with `23-brain-judge.md`). RED on BASE: the three old texts occur once each | `docs/40 - DevDocs/prompts/BRAIN-HUB.md`, `tests/ops/test_rules_cut_brain.py` (NEW) |
| B2 | `B:6` (C5, row 322): `The desk types ONE bare command, after he has stopped the brain before you (a brain is never launched beside a live one):` becomes `The desk types ONE bare command once the brain before you is stopped, on his word or, after its recorded ask, by the script itself (a brain is never launched beside a live one):`; and `and refuses while a session named \`brain\` is live;` becomes `and refuses while a session named \`brain\` is live and has not asked for its replacement in a DESK RECORD row of today's or yesterday's desk report (one that asked is stopped and removed by \`desk-done.sh\` first, card 462);` | same test | same files |
| B3 | `B:33` (C5, row 328; the move of checklist W8's brain-restart rule, row 147, D11): the paragraph's first sentence gets in front of it `A restart ordered by him or by you is approved, no ask (his 2026-10-02 R131).` and a space; `Once he has stopped you, the desk launches your successor on it with \`desk-launch.sh brain\`, adding \`--fable\` only when you named Fable.` becomes `The desk records your ask as a DESK RECORD row and launches your successor on it with \`desk-launch.sh brain\`, which stops and removes you first (card 462), adding \`--fable\` only when you named Fable.` | same test; `test_p5_the_hubs_measure_asks_the_desk_for_a_successor_and_names_its_model` (`tests/ops/test_desk_launch_brain.py`) stays green unchanged | same files |
| B4 | `STANDING-LIST.md:221` (§7, row 407, C5): `and any live session named \`brain\` (his 2026-09-30 R76: a brain is stopped only on his word, so the successor launches after he has stopped it).` becomes `and any live session named \`brain\` that has not asked for its replacement in a DESK RECORD row (card 462: one that asked is stopped and removed by \`desk-done.sh\` first; one that has not is stopped only on his word, his 2026-09-30 R76).` | same test: on the line starting `Deny: \`AskUserQuestion\`, \`EnterWorktree\`, \`Bash(git push*)\` (standing). \`desk-launch.sh brain\` refuses`, `so the successor launches after he has stopped it` occurs zero times and `that has not asked for its replacement in a DESK RECORD row` once. RED on BASE | `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `tests/ops/test_rules_cut_brain.py` |
| B5 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`; quote the table and the `RESTARTS:` line (expected none) | — (output quoted) | none |

## NOT IN THIS JOB
- `ops/desk/desk-done.sh`, `ops/desk/desk-launch.sh` (the brain guards and their comments): card 462. A brain that has not asked: still his (R76); no text here lets the desk stop it.
- `B:8` (the launch line), `B:10`, `B:23` (the write fence), `## HANDOVER SHAPE`; every other line of `STANDING-LIST.md` (cards 481, 483).
- Any file under `/Users/cobalt/Vault` (checklist W8 retires with card 478; the desk folds the ASK ROW wording, card 462 `## NOT IN THIS JOB`).
- Any `src/` or `configs/` file; any with-DB test (`DB: none`).

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BRAIN-HUB.md` whole (43 lines).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/462-brain-replace-card.md` (THE ASK ROW, rows D1, L1).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/STANDING-LIST.md` lines 210-221.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-map-2026-10-13.md` C5; rows 147, 321, 322, 328, 407.

## CHECK ASKS
- X1 Does the text say what card 462's scripts do at the deployed `main` (the ask row, today's or yesterday's report, an unasked brain refused)?
- X2 Does any line of `BRAIN-HUB.md` or `STANDING-LIST.md` §7 still say a brain is stopped ONLY on his word?
- X3 Is the brain's launch line byte for byte BASE's?
FOR THE CHECK: rules cut 2026-10-13 HIS RULING: the whole cut list executed (13 contradictions, 25 stale, 40 duplicate groups deleted; moves as mapped; preferences to preferences.md; L82-L84 added, vetoable)
FOR THE CHECK: rules-cut cards 2026-10-13 brain: 11 KEEP; STANDING-LIST:107 deleted (CHECK-HUB wins, R1340); cards fill gaps behind MVP cards

## DEPLOY PROOF
- `grep -c -F "stopped only when he says so" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BRAIN-HUB.md"` · before `1` · after `0`
- `grep -c -F "card 462" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BRAIN-HUB.md"` · before `0` · after `3`

## RECORDS
- Reads by the drafter `draft-rules-cut-cards`, 2026-10-13 07:20-07:45 ET, at `main` HEAD `7516154c`; the prompts folder clean but one untracked dated prompt.
- `git show HEAD:"docs/40 - DevDocs/prompts/BRAIN-HUB.md"` whole; `grep -n -E "stopped only|after he has stopped|Once he has stopped|UNATTENDED-LAUNCH|^## "`: `:3` `you are stopped only when he says so (his 2026-09-30 R76)`, `:6` `after he has stopped the brain before you` and `refuses while a session named \`brain\` is live`, `:33` `Once he has stopped you, the desk launches your successor`.
- `STANDING-LIST.md:221` (Read of the persisted `git show`): `(his 2026-09-30 R76: a brain is stopped only on his word, so the successor launches after he has stopped it)`.
- Checklist `cto-desk-checklist.md:60` W8 (`cat -n`): R131 `A brain restart (replace with a fresh brain) ordered by him OR by the brain itself is approved, no ask.`; R7, R188, R191 `past 500,000 tokens it asks the desk by message for its own restart, no word of his; the desk replaces it.` (the latter already at `B:33`).
- Card 462 (`462-brain-replace-card.md`): `desk-done.sh <id> "<desk report>" brain`, today's or yesterday's `cto-<D>.md`, the refusal of an unasked brain names R76; its `## NOT IN THIS JOB` leaves `BRAIN-HUB.md` to another card.
