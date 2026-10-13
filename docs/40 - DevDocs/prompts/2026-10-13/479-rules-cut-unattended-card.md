JOB: rules-cut-unattended-1013
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1341
CLASS: K5
INSTALL: none
BRANCH: ops/rules-cut-unattended-1013
WORKTREE: rules-cut-unattended-1013
BASE: «FILL: BASE, the desk's 8-hex main commit at the build launch»
TIP:
REPORT: /Users/cobalt/cobalt-wt/rules-cut-unattended-1013/docs/40 - DevDocs/reports/rules-cut-unattended-build-2026-10-13.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-cut-unattended-check-2026-10-13.md
HOUSE B: as needed
DB: none
RESTARTS: none
RULINGS: 2026-10-12 R1138

## ROWS

WHY: his ruling R1341 (`reports/cto-2026-10-13.md` R1341, R1344; direction file `## RULED 2026-10-13 — the rules cut list, all of it` and `## RULED 2026-10-13 — blocker survey decisions`, rows 11 and 31). Map rows 330-334 (`reports/rules-map-2026-10-13.md`): the desk's side of `UNATTENDED-LAUNCH.md` (§1, §3, §4, §5) moves to `CTO-DESK-WAKEUP.md`; §2 (the blocks inside every prompt) is cut, each fixed file carrying its own (L19; D13, D38). Survey row 11 (L62 gains `unless a card inside an approved class of L81 adds it`) and row 31 (the three-step blocked-call rule) land in the moved text. `U` = `docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md` at HEAD; every text below is byte for byte. FIXED FILE: `CTO-DESK-WAKEUP.md` changes only by a drafter re-issue (this card) and is read by one other house at the change (L9, L67). Card 478 creates `## ON TRIGGER — LAUNCH`; BASE is set after 478 merges.

| row | what | red first | files |
|---|---|---|---|
| U1 | §1 MOVES: at the end of the wake-up's `## ON TRIGGER — LAUNCH` section (after its last line), the line `THE LAUNCH STANDARD (was UNATTENDED-LAUNCH.md):`, then `U:4`-`U:8` as five lines, each `- ` plus the source text without its leading `<n>. `, with two edits: (a) in `U:4` delete ` (a check's second pass adds \`PASS-2\`; a deploy resume adds \`STEP-D0\`)` and put ` (a deploy resume adds \`STEP-D0\`)` in its place (S1, R438), and `a string not on it is new and is asked for by itself.` becomes `a string not on it is new and is asked for by itself, unless a card inside an approved class of L81 adds it.` (survey row 11, C7, R1138); (b) in `U:6` `A list whose every string is standing (L62) or already approved for the same job shape is never brought again.` becomes `A list whose every string is standing (L62), added by a card inside an approved class of L81, or already approved for the same job shape is never brought again.` (row 11 follows L62 at `:6`). `U:5`, `U:7`, `U:8` unchanged | NEW `tests/ops/test_rules_cut_unattended.py` on the real files: in the wake-up, `unless a card inside an approved class of L81 adds it.` and `added by a card inside an approved class of L81, or already approved` occur once each, inside the `## ON TRIGGER — LAUNCH` section; `PASS-2` occurs zero times in the wake-up; `U:5`'s and `U:7`'s texts (from `git show <BASE>:`) occur once each in the wake-up. RED on BASE: the two new texts are absent | `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `tests/ops/test_rules_cut_unattended.py` (NEW) |
| U2 | §3 MOVES, row 31 applied: after U1's lines, `U:17` as a line; then `U:18` with `fix it, bring him only a NEW string, relaunch a new worker.` replaced by `follow the blocked-call rule: (1) was each call one bare command? If not, resend it as single bare calls (the guard's NOT A REFUSAL route, never a workaround); (2) a script or string the seat already holds that does the job (\`scratch-clean.sh\`, \`job-clean.sh\`, the R686 read) → use it; (3) still denied → that ONE item stops and goes to \`## NEEDS HIS HAND\` with the full why, and everything else keeps running. Never the same action disguised (a file pointer, a rename, another seat, another tool) (LAWS L61; R1330, R1341). A line that must change → fix it, relaunch a new worker.`; `U:19` (THE ONE DIALOG RULE) is CUT (D36: LAWS L63 holds it) | same file: the rule text occurs once in the wake-up; `bring him only a NEW string` and `THE ONE DIALOG RULE` occur zero times. RED on BASE: the rule text is absent | `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `tests/ops/test_rules_cut_unattended.py` |
| U3 | §4 and §5 MOVE: after U2's lines, `U:22` as a line with `A build or check that ended \`FAILED\` is not closed: §3.` replaced by `A build or check that ended \`FAILED\` is not closed: see \`FAILED\` above.`; then the line `LAUNCH FACTS:` and `U:25`-`U:30` byte for byte. In the wake-up's `- L13 ` line (moved there by card 478) `(\`UNATTENDED-LAUNCH.md\` §5)` becomes `(LAUNCH FACTS below)` | same file: `LAUNCH FACTS:` occurs once, followed by the six `U:25`-`U:30` lines; `UNATTENDED-LAUNCH` occurs zero times in the wake-up. RED on BASE: `LAUNCH FACTS:` absent | `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `tests/ops/test_rules_cut_unattended.py` |
| U4 | THE FILE RETIRES (nothing under `docs/` is deleted): `UNATTENDED-LAUNCH.md` becomes three lines, its title line `# UNATTENDED LAUNCH — the standard for every session the desk starts (L62)` byte for byte, a blank line, and `Retired 2026-10-13 (his R1341; \`reports/rules-map-2026-10-13.md\` rows 330-334): the desk's launch standard is \`CTO-DESK-WAKEUP.md\` \`## ON TRIGGER — LAUNCH\`; each fixed file carries its own AUTHORIZATION, UNATTENDED, PREFLIGHT and CONTINUE blocks (L19).` §2 (`U:10`-`U:14`) goes nowhere (row 331, D13, D38) | same file: `UNATTENDED-LAUNCH.md` has exactly 3 lines, line 1 equals BASE's line 1, line 3 is the text above. RED on BASE: 30 lines | `docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md`, `tests/ops/test_rules_cut_unattended.py` |
| U5 | THE ONE LIVE POINTER: `JUDGE-HUB.md:3` `(\`UNATTENDED-LAUNCH.md\` §4)` becomes `(\`CTO-DESK-WAKEUP.md\` \`## ON TRIGGER — LAUNCH\`)`; nothing else on the line changes (its launch span stands byte for byte; card 483 adds its string after this card merges) | same file: `UNATTENDED-LAUNCH.md` occurs zero times in `JUDGE-HUB.md`; the backticked launch span of `:3` from `claude --bg` to `--add-dir /Users/cobalt/cobalt-wt` equals BASE's. RED on BASE: one occurrence | `docs/40 - DevDocs/prompts/JUDGE-HUB.md`, `tests/ops/test_rules_cut_unattended.py` |
| U6 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`; quote the table and the `RESTARTS:` line (expected none) | — (output quoted) | none |

## NOT IN THIS JOB
- Any file under `/Users/cobalt/Vault` (LAWS L61, L62 carry rows 11 and 31 already: R1342).
- Any line of the wake-up but the U1-U3 insertions and the `- L13 ` pointer; card 478's sections and card 458's texts stand.
- `BRAIN-HUB.md:23` (its write fence names `UNATTENDED-LAUNCH.md`; the stub stays a fixed file): left.
- Dated prompts under `prompts/20*/` that name the file: frozen records, never edited.
- `JUDGE-HUB.md` but `:3`'s pointer; the judge stop line is card 483's.
- Any `ops/`, `src/` or `configs/` file; any with-DB test (`DB: none`).

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md` whole (30 lines).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/brain-direction-2026-10-02.md` `## RULED 2026-10-13 — blocker survey decisions` (rows 11, 31).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-map-2026-10-13.md` rows 330-334, D13, D36, D38.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/478-rules-cut-wakeup-card.md` (the LAUNCH section it creates).

## CHECK ASKS
- X1 Is every line of `U:4`-`U:8`, `U:17`, `U:18`, `U:22`, `U:25`-`U:30` in the wake-up, byte for byte but for the named edits?
- X2 Does the row 31 text match the direction file's three steps and its "Never" clause, and does nothing in the moved text still ask him for a string a K5 card may add?
- X3 Does any fixed file, script or test (not a dated prompt) still point at `UNATTENDED-LAUNCH.md` § anything?
FOR THE CHECK: rules cut 2026-10-13 HIS RULING: the whole cut list executed (13 contradictions, 25 stale, 40 duplicate groups deleted; moves as mapped; preferences to preferences.md; L82-L84 added, vetoable)
FOR THE CHECK: rules-cut cards 2026-10-13 brain: 11 KEEP; STANDING-LIST:107 deleted (CHECK-HUB wins, R1340); cards fill gaps behind MVP cards

## DEPLOY PROOF
- `grep -c -F "LAUNCH FACTS:" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` · before `0` · after `1`
- `grep -c -F "Retired 2026-10-13" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md"` · before `0` · after `1`

## RECORDS
- Reads by the drafter `draft-rules-cut-cards`, 2026-10-13 07:20-07:40 ET, at `main` HEAD `7516154c`; the prompts folder clean but one untracked dated prompt (`git -C /Users/cobalt/cobalt status --short`).
- `git show HEAD:"docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md"` whole and `grep -n -E "^## |^[0-9]\. |^[A-Z ,]+:|^- "` on it: `:3` §1, `:4`-`:8` items 1-5 (`:4` holds `PASS-2` and `asked for by itself`; `:6` `A list whose every string is standing (L62)`), `:10` §2, `:11` AUTHORIZATION, `:12` UNATTENDED RULES, `:13` PREFLIGHT, `:14` CONTINUE, `:16` §3, `:17`-`:19`, `:21` §4, `:22`, `:24` §5, `:25`-`:30`. `wc -c` 9,515.
- `grep -rln -F "UNATTENDED-LAUNCH"` over `ops`, `tests`, `docs/40 - DevDocs/prompts`: no `ops/` or `tests/` file; fixed files `JUDGE-HUB.md` (`:3`) and `BRAIN-HUB.md` (`:23`, the fence); the rest are dated prompts.
- The survey cites row 11 at `:6`; the literal `asked for by itself` stands at `:4`: both lines get the L81 clause.
