JOB: rules-cut-standing-1013
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1341
CLASS: K5
INSTALL: none
BRANCH: ops/rules-cut-standing-1013
WORKTREE: rules-cut-standing-1013
BASE: «FILL: BASE, the desk's 8-hex main commit at the build launch»
TIP:
REPORT: /Users/cobalt/cobalt-wt/rules-cut-standing-1013/docs/40 - DevDocs/reports/rules-cut-standing-build-2026-10-13.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-cut-standing-check-2026-10-13.md
HOUSE B: as needed
DB: none
RESTARTS: none
RULINGS: 2026-10-12 R1138

## ROWS

WHY: his ruling R1341 (`reports/cto-2026-10-13.md` R1341, R1344; direction file `## RULED 2026-10-13 — the rules cut list, all of it`: "no-awk to the STANDING-LIST NEVER block"). The map's rows in `STANDING-LIST.md` (`reports/rules-map-2026-10-13.md`): C7 (row 398; R1138: strings serving K1-K4 go by card in class K5), S1 (rows 397, 402; R438), S2 (rows 396, 402; R920, R921), the move of checklist L19 (row 137, D12). `S` = `docs/40 - DevDocs/prompts/STANDING-LIST.md` at HEAD. No string of any launch line changes. Every quoted text is byte for byte; a cell's `\|` is ONE `|`.

| row | what | red first | files |
|---|---|---|---|
| S1 | C7, the approval sentences: `S:3` `A string that is not in this file is NEW and is asked for by itself.` becomes `A string that is not in this file is NEW and is asked for by itself, unless a card inside an approved class of L81 adds it.`; `S:32` `a string outside every class is NEW and is asked for by itself.` becomes `a string outside every class is NEW and is asked for by itself, unless a card inside an approved class of L81 adds it.` (survey row 11's L62 wording, R1342) | NEW `tests/ops/test_rules_cut_standing.py` on the real file: `unless a card inside an approved class of L81 adds it.` occurs exactly twice, on the lines starting `WHAT HE APPROVES, ONCE:` and `His permission by class.`. RED on BASE: zero occurrences | `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `tests/ops/test_rules_cut_standing.py` (NEW) |
| S2 | S2: `S:11` delete the last two sentences ` \`Bash(agy *)\` on a code check also goes against L67 as it reads today ("Gemini … reads no code check"): \`RULE-CHANGES.md\` row 1 changes that text.` (from the space before `` `Bash(agy *)` on a code check `` to the line's end) | same test: `goes against L67` occurs zero times; the line starting `- THE THREE HOUSE STRINGS ON A WRITE-PATH LINE.` still ends `**NEW COMBINATION**, for his eyes.` RED on BASE: once | same files |
| S3 | C7: `S:24` `\`.claude/settings.json\` and \`.git/hooks\` (his script, his order).` becomes `\`.claude/settings.json\` and \`.git/hooks\`.` | same test: `his script, his order` occurs zero times. RED on BASE: once | same files |
| S4 | S1 / C4: `S:28` ` A check starts ONE outside house per pass and nothing else.` becomes ` A check starts house A, and house B with it only on a \`mandatory\` card, and nothing else (R920, R921).` | same test: `ONE outside house per pass` zero times, the new sentence once. RED on BASE | same files |
| S5 | L19 MOVES (row 137, D12; checklist `cto-desk-checklist.md:49`): a NEW line directly after `S:29` (the last NEVER bullet, `- A write-path launch from a one-off prompt: …`): `- \`Bash(awk *)\` on any line, ever (his 2026-10-04 R283; amends 10-03 R33): the read strings are \`Bash(cut *)\`, \`Bash(sort *)\`, \`Bash(uniq *)\`.` | same test: the line occurs once, inside the `## NEVER` section (between that heading and `## CLASSES`). RED on BASE: absent | same files |
| S6 | S1, §2: `S:87` `ONE LINE, for pass 1 and for pass 2 (\`desk-launch.sh check <card> PASS-2\` runs the same line; only its message starts \`PASS-2. \`).` becomes `ONE LINE, one pass (his 2026-10-05 R438).`; `S:93` `; one house is started per pass, in the background,` becomes `; house A, and house B at once with it only on a \`mandatory\` card, in the background,`; `S:105` (`THE SEAT ORDER AND THE SECOND PASS change no string: pass 2 starts house B with the same three strings.`) and the blank line after it are deleted | same test: `PASS-2`, `pass 2` and `SECOND PASS` occur zero times in the file. RED on BASE: they occur (`PASS-2` twice and `pass 2` at `:87`; `SECOND PASS` and `pass 2` at `:105`) | same files |
| S7 | S2, the house roles (R920, R921; `CHECK-HUB.md:24-28`): the `for` cell of `S:97` becomes `the OpenAI house (Sol): house A only when the card header carries \`HOUSE A: OpenAI — his <date> R<n>\` (R920); and its METER PROBE`; of `S:98` `the Grok house: house A; house B when OpenAI sits on that header line; and \`grok --version\``; of `S:99` `the Gemini house: house B on a \`mandatory\` card; house A when Grok is out; and \`agy --version\``. The other cells of the three rows stand | same test: the three cells read as above; `A when OpenAI is out` and `B when OpenAI is out` occur zero times. RED on BASE: the old cells | same files |
| S7a | C9-type contradiction (brain answer to the draft's DECISIONS 7, his R1340: every contradiction deleted): `S:107` loses its first sentence, `THE TOKEN TOTAL of a check is not the session's to report: the desk measures it at the stop line (\`sh /Users/cobalt/.claude/ops/desk-context.sh <id>\`, a command already on the desk's side) and writes it beside the stop line's \`files opened\`. ` (through the space after `files opened\`.`); `CHECK-HUB.md:59` and `:124` win (the check's stop line carries `tokens: <n>`, L71). The line then reads `\`desk-launch.sh\` launches a check while the lock is held (R20); the check takes the lock at its with-DB step and waits there.` | same test: `is not the session's to report` occurs zero times; the lock sentence occurs once. RED on BASE: once | same files |
| S8 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`; quote the table and the `RESTARTS:` line (expected none) | — (output quoted) | none |

## NOT IN THIS JOB
- `S:175-191` (§5, the close): card 483 adds its desk-context row. `S:221` (§7, the brain): card 482.
- `S:103` (THE METER PROBES).
- `S:184`'s never-touches cell naming `the checklist`: left.
- Every launch line of every fixed file; `.claude/settings.json` (his, R1324).
- Any file under `/Users/cobalt/Vault`; any `ops/`, `src/` or `configs/` file; any with-DB test (`DB: none`).

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/STANDING-LIST.md` lines 1-35, 85-107.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-map-2026-10-13.md` rows 137, 395-402; C7; S1, S2; D12.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md` lines 23-30 (the seat order the S7 cells copy).

## CHECK ASKS
- X1 Does any line of `STANDING-LIST.md` still say a K5 card's string is asked of him, or name a second pass?
- X2 Do the S7 cells match `CHECK-HUB.md:24-28` for every meter state (Grok up, Grok out, the OpenAI header line)?
- X3 Is every allow and deny string in the file byte for byte BASE's (`git diff <BASE> -- <file>` shows no string cell changed but S7's `for` cells)?
FOR THE CHECK: rules cut 2026-10-13 HIS RULING: the whole cut list executed (13 contradictions, 25 stale, 40 duplicate groups deleted; moves as mapped; preferences to preferences.md; L82-L84 added, vetoable)
FOR THE CHECK: rules-cut cards 2026-10-13 brain: 11 KEEP; STANDING-LIST:107 deleted (CHECK-HUB wins, R1340); cards fill gaps behind MVP cards

## DEPLOY PROOF
- `grep -c -F "Bash(awk *)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/STANDING-LIST.md"` · before `0` · after `1`
- `grep -c -F "PASS-2" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/STANDING-LIST.md"` · before `1` · after `0`

## RECORDS
- Reads by the drafter `draft-rules-cut-cards`, 2026-10-13 07:20-07:40 ET, at `main` HEAD `7516154c`; the prompts folder clean but one untracked dated prompt.
- `git show HEAD:"docs/40 - DevDocs/prompts/STANDING-LIST.md"` whole (persisted output); `grep -n -E "is NEW and is asked|asked for by itself|agy|against L67|his script, his order|ONE outside house per pass|second|PASS-2|pass 2|OpenAI|stopped only|his word|NEVER|awk|desk-context|^## "` on it: `:3`, `:11`, `:16` (`## NEVER`), `:24`, `:28`, `:31-32` (`## CLASSES`), `:87`, `:93`, `:97-99`, `:105`, `:175`, `:221`, `:245`; Read `:16-31`, `:86-106`, `:175-191`.
- `grep -c -F "Bash(awk *)"` of the file: 0 at HEAD (the guard holds it: `ops/desk/bare-guard.py:35`).
- Checklist `cto-desk-checklist.md:49`: `L19 No line carries \`Bash(awk *)\`, ever (amends 10-03 R33); after guard-b ships, the read strings are \`Bash(cut *)\`, \`Bash(sort *)\`, \`Bash(uniq *)\` only.` (`cat -n`).
- `S:107` (Read of the persisted `git show`): `THE TOKEN TOTAL of a check is not the session's to report: …`; `CHECK-HUB.md:59` (`tokens: <n>` = the figure `desk-context.sh` prints, read at your last step, L71) and `:124` (the stop line ends `· tokens: <n>`). Row S7a: the desk's CONTINUE 2026-10-13, brain answer to DECISIONS 7 (R1340).
- S1 at `:32` is the same C7 sentence on a line the map did not list (DECISIONS 6 of the draft report).
