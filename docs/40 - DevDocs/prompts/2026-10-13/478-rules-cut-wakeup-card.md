JOB: rules-cut-wakeup-1013
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1341
CLASS: K5
INSTALL: none
BRANCH: ops/rules-cut-wakeup-1013
WORKTREE: rules-cut-wakeup-1013
BASE: «FILL: BASE, the desk's 8-hex main commit at the build launch»
TIP:
REPORT: /Users/cobalt/cobalt-wt/rules-cut-wakeup-1013/docs/40 - DevDocs/reports/rules-cut-wakeup-build-2026-10-13.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-cut-wakeup-check-2026-10-13.md
HOUSE B: as needed
DB: none
RESTARTS: none
RULINGS: 2026-10-12 R1138

## ROWS

WHY: his ruling R1341 (`reports/cto-2026-10-13.md` rows R1341, R1344; `reports/brain-direction-2026-10-02.md` `## RULED 2026-10-13 — the rules cut list, all of it`): the desk middle layer empties. Every line of `cto-desk-checklist.md` and `cto-desk-contract.md` that the map (`reports/rules-map-2026-10-13.md` `## MAP` rows 102-243) marks MOVE to `WAKE` goes into `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` under `## ON TRIGGER — <NAME>` headings; every line marked CUT goes nowhere. After this card deploys the desk retires both topic files (its own memory write, not this card's). `M` = `/Users/cobalt/Vault/Think/6 - Permanent/Memory`; `CL` = `M/topics/cto-desk-checklist.md` (23,526 bytes at the draft); `CT` = `M/topics/cto-desk-contract.md` (11,230 bytes at the draft). FIXED FILE: `CTO-DESK-WAKEUP.md` and `CLOSE-HUB.md` change only by a drafter re-issue (this card) and are read by one other house at the change (L9, L67).

HOW A LINE MOVES: the text is the source line byte for byte, with every `[stated …]` and `[desk lesson …]` tag removed (a ruling number that sits only in a removed tag is appended at the line's end as `(R<n>)`), its leading rule id kept (`- H2 …`), and the cut named in the table removed. A source line's `wc -c` that differs from the draft's figures above → `## DECISIONS` item `ASK DESK: source changed`, the safe default: build from the file as it reads then, every line named in the table.

| row | what | red first | files |
|---|---|---|---|
| W1 | THE POINTERS in `CTO-DESK-WAKEUP.md` (HEAD `:8`, `:22`, `:29`, `:36`, `:46-50`; card 458 moves the numbers, anchor on the text): (a) delete the whole line `- CONTRACT = \`M/topics/cto-desk-contract.md\` · CHECKLIST = \`M/topics/cto-desk-checklist.md\` (a section = its \`## <name>\` heading, read to the next \`## \`)` (`:8`); (b) in STEP 0 item 2 (`:22`) `record it in §5 and open CHECKLIST \`## handover\`.` becomes `record it in §5 and open \`## ON TRIGGER — HANDOVER\`.` and `(CHECKLIST H2)` becomes `(H2, \`## ON TRIGGER — HANDOVER\`)`; (c) READ item 1 (`:29`) `LAWS from its top down to \`## Reading\`, CONTRACT whole.` becomes `LAWS from its top down to \`## Reading\`.`; (d) READ item 8 (`:36`) `→ CHECKLIST W3 and L1;` becomes `→ LAWS L63: STOP it, fix the line, relaunch a new worker by \`desk-launch.sh\`;`; (e) the line `ON TRIGGER — open, then act (CONTRACT's \`## Checklist\` lists the CHECKLIST sections):` and its four bullets `- REFRESH → …`, `- A §4 row → …`, `- A launch → …`, `- A close → …` (`:46-50`) become the line `ON TRIGGER — open the section, then act (each is a \`## ON TRIGGER — <NAME>\` heading below, read to the next \`## \`):` and these bullets, in order: `- STEP 0 finds a HANDOVER naming you, or you REFRESH → HANDOVER.` · `- A reply, an approval request or an answer to ASK DESK → REPLIES.` · `- A ruling, launch or record to write → RULINGS.` · `- Planning the day or a queue item → PLANNING.` · `- A launch → LAUNCH and WATCH.` · `- A watch or timer created, restored, changed or answered → WATCH.` · `- A commit or a push → COMMIT.` · `- Reading a hub report, the DB or a config → READS.` · `- Drafting, filling or re-pointing a prompt or card, or a deploy launch → PROMPTS.` · `- A memory or LAWS edit (RECONCILE included) → MEMORY and WRITING.` · `- A close → CLOSE.` The three bullets after them (`- A law your task touches …`, `- The plate's sprint …`, `- Planning, or drafting …`) stand byte for byte. Measure `wc -c` before and after; name the growth in the report (writing rules) | NEW `tests/ops/test_rules_cut_wakeup.py` on the real file (read as `tests/ops/test_desk_wakeup_rule.py:17` reads it): `cto-desk-checklist`, `cto-desk-contract`, `CHECKLIST` and `CONTRACT` occur zero times; the eleven pointer bullets occur once each, in order, after the `ON TRIGGER — open the section` line; exactly one line starts `- LAUNCH ` and it equals `git show <BASE>:` of the same line; the `CLOSE WAIT (his 10-08 R658)` paragraph equals BASE's. RED on BASE: `CHECKLIST` occurs (`:8`, `:22`, `:36`, `:46-50`) | `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `tests/ops/test_rules_cut_wakeup.py` (NEW) |
| W2 | THE SECTIONS: appended at the file's end, after the last ON TRIGGER bullet, in this order, each a heading line then its lines in source order: `## ON TRIGGER — HANDOVER`, `## ON TRIGGER — RULINGS`, `## ON TRIGGER — PLANNING`, `## ON TRIGGER — LAUNCH`, `## ON TRIGGER — WATCH`, `## ON TRIGGER — COMMIT`, `## ON TRIGGER — READS`, `## ON TRIGGER — REPLIES`, `## ON TRIGGER — PROMPTS`, `## ON TRIGGER — MEMORY`, `## ON TRIGGER — CLOSE`. Each source line goes where `## THE LINE LIST` below says, with its cut; a line marked CUT or ELSEWHERE is not written. A heading carries no tag (writing rules) | same file: for each MOVE row of `## THE LINE LIST`, its id (or, for a `CT` line, its literal) starts or occurs in exactly one line, and that line sits inside its heading's section; each `CUT` id starts no line (`H1a`, `H3`, `H6`, `H7`, `H8`, `R1`, `L1`, `L2`, `L4`, `L5`, `L7`, `L12`, `L14`, `W3`, `C5`, `C3`, `P4`, `P6`, `K4`, `K10a`, `K10`, `K13`, `K14`, `K17`, `K19a`, `K22`, `K23`, `K24`, `K25`); `310k`, `Fable-grade`, `acceptEdits\` + allowlist`, `REQUIRES-three`, `hands him the command`, `goes to him`, `a trial, going forward` and `a brain he asked for stays open` occur zero times; the eleven headings occur once each, in order. RED on BASE: no `## ON TRIGGER — ` heading | `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `tests/ops/test_rules_cut_wakeup.py` |
| W3 | CLOSE-HUB's pointers to the checklist (`docs/40 - DevDocs/prompts/CLOSE-HUB.md`): (a) `:15` `LAWS, LAWS-HISTORY, the checklist and topics are the desk's` becomes `LAWS, LAWS-HISTORY, the wake-up's ON TRIGGER sections and topics are the desk's`; (b) `:16` `Row rule: \`<M>/topics/cto-desk-checklist.md\` \`## rulings\` R2 and \`## commit\` C6.` becomes `Row rule: \`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md\` \`## ON TRIGGER — RULINGS\` R2 and \`## ON TRIGGER — COMMIT\` C6.`; (c) `:44` `\`grep -c -F "<literal>"\` it in \`<M>/topics/cto-desk-checklist.md\` and in` becomes `\`grep -c -F "<literal>"\` it in \`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md\` and in`, and `Proposals only: the desk writes the checklist.` becomes `Proposals only: the desk writes the wake-up's ON TRIGGER sections.` (map DECISIONS item 5, brain KEEP R1337). Nothing else in the file changes | same test file: `cto-desk-checklist` occurs zero times in `CLOSE-HUB.md`; `CTO-DESK-WAKEUP.md` occurs at least twice; the `claude --bg ` line and the `CLOSE PUSHED` stop line equal BASE's. RED on BASE: `cto-desk-checklist` occurs twice (`:16`, `:44`) | `docs/40 - DevDocs/prompts/CLOSE-HUB.md`, `tests/ops/test_rules_cut_wakeup.py` |
| W4 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`; quote the table and the `RESTARTS:` line (expected none: `docs/` and `tests/`) | — (output quoted) | none |

## THE LINE LIST
`CL` lines by rule id, `CT` lines by line number and a literal. HEAD line numbers are the files' at the draft (`## RECORDS`). Map row in brackets.

| source | id / literal | verb | heading | cut from the text |
|---|---|---|---|---|
| CL:8 | H1 | MOVE [102] | HANDOVER | — |
| CL:9 | H1a | CUT [103, D1] | — | whole line: the limits stand in the wake-up's EVERY TURN; its R1323 clause is card 458's W1 text |
| CL:10 | H2 | MOVE [104] | HANDOVER | — |
| CL:11 | H2a | MOVE [105] | HANDOVER | — |
| CL:12 | H3 / H3a | CUT [106] | — | dup of the wake-up STEP 0 items 2 and 4 |
| CL:13 | H4 | MOVE [107] | HANDOVER | — |
| CL:14 | H5 | MOVE [108] | HANDOVER | — |
| CL:15 | H6 | CUT [109] | — | dup of the wake-up LAUNCH and STEP 0 |
| CL:16 | H7 | CUT [110] | — | state |
| CL:17 | REFRESH HOW | MOVE [111] | HANDOVER | — |
| CL:18 | H8 | CUT [112, D3] | — | dup of READ 7 |
| CL:19 | LAUNCH denied → | MOVE [113] | HANDOVER | — |
| CL:23 | Every ruling, launch or record → | MOVE [114] | RULINGS | — |
| CL:24 | R2 | MOVE [115] | RULINGS | — |
| CL:25 | R1 | CUT [116, D23] | — | LAWS L48 |
| CL:29 | L1 | CUT [117, D35] | — | `desk-launch.sh` |
| CL:30 | L2 | CUT [118] | — | pointer |
| CL:31 | L3 | MOVE [119] | LAUNCH | — |
| CL:32 | L4 | CUT [120, C12] | — | R45: the hubs run `dontAsk` |
| CL:33 | L5 | CUT [121] | — | `BUILD-HUB.md` UNATTENDED RULES |
| CL:34 | L6 | MOVE [122] | LAUNCH | — |
| CL:35 | L7 | CUT [123] | — | enforced by `desk-launch.sh` |
| CL:36 | L7a | MOVE [124] | LAUNCH | — |
| CL:37 | L8 | MOVE [125] | LAUNCH | — |
| CL:38 | L9 | MOVE [126, C7] | LAUNCH | `its allow list changes only with his approval; ` |
| CL:39 | L10 | MOVE [127] | LAUNCH | — |
| CL:40 | L11 | MOVE [128] | LAUNCH | — |
| CL:41 | L12 | CUT [129, S19] | — | R389 |
| CL:42 | L13 | MOVE [130] | LAUNCH | — |
| CL:43 | L14 | CUT [131, S3] | — | R920 |
| CL:44 | L15 | MOVE, soft cap only [132, D10] | LAUNCH | the line becomes exactly `- L15 Grok hubs: soft cap 3 at a time (desk meter practice by L47, not law); the rest of R908 is LAWS L67.` |
| CL:45 | L16 | MOVE [133] | LAUNCH | — |
| CL:46 | L17 | MOVE [134] | LAUNCH | — |
| CL:47 | L18 | MOVE [135] | LAUNCH | — |
| CL:48 | L20 | MOVE [136, C6] | LAUNCH | ` \`desk-launch.sh\` refuses at 310k tokens: REFRESH before a heavy launch turn.` |
| CL:49 | L19 | ELSEWHERE [137] | — | card 481 writes it into `STANDING-LIST.md` NEVER |
| CL:53 | WATCHES | MOVE [138] | WATCH | — |
| CL:54 | W1 | MOVE [139] | WATCH | — |
| CL:55 | W2 | MOVE [140] | WATCH | — |
| CL:56 | W3 | CUT [141, D36] | — | LAWS L63 |
| CL:57 | W5 | MOVE [142] | WATCH | — |
| CL:58 | W6 | MOVE [143] | WATCH | — |
| CL:59 | W7 | MOVE [144] | WATCH | — |
| CL:60 | W8 (R9 part, `"close a tab` … `it resumes only at \`STEP-D0\`.`) | MOVE [145] | WATCH | — |
| CL:60 | W8 (R76 part, `The one exception: a \`brain\` he asked for stays open after its report until he says stop.`) | CUT [146, D34] | — | `BRAIN-HUB.md:3` |
| CL:60 | W8 (R131, R188, R191 parts, `A brain restart` … `the desk replaces it.`) | ELSEWHERE [147, C5] | — | card 482 writes it into `BRAIN-HUB.md` |
| CL:60 | W8 (after R606 part, `A builder, checker or any worker` … `never stop it.`) | MOVE [148] as its own line `- W8a …` | WATCH | — |
| CL:60 | W8 (R613 part, `Worktree cleanup is the desk's` … end of line) | MOVE [149, D21] | CLOSE, joined to CL:136 as one line `- CLOSE2 …` | ` (card owed, no \`--force\`); until it ships the desk reports a broken tree and removes nothing` (salvage ships: `ops/desk/job-clean.sh:3`, `:12`; DECISIONS 3 of the draft report) |
| CL:62 | W9 | MOVE [150] | WATCH | items `(4) …;` and `(6) …` with their text (D23, D24) |
| CL:64 | W10 | MOVE [151] | WATCH | — |
| CL:68 | C1 | MOVE [152] | COMMIT | — |
| CL:69 | C5 | CUT [153, D14] | — | LAWS L55 |
| CL:70 | C2 | MOVE [154] | COMMIT | — |
| CL:71 | C3 | CUT [155] | — | each hub's UNATTENDED RULES |
| CL:72 | C6 | MOVE [156] | COMMIT | — |
| CL:76-81 | R2 (incident) R3 R4 R5 R6 R7 | MOVE [157-162] | READS | — |
| CL:85 | P1 | MOVE [163] | REPLIES | — |
| CL:86 | P2 | MOVE [164] | REPLIES | — |
| CL:87 | P3 | MOVE [165] | REPLIES | — |
| CL:88 | P4 | CUT [166, D28] | — | LAWS L78 |
| CL:89 | P5 | MOVE [167] | REPLIES | — |
| CL:90 | P6 | CUT [168] | — | LAWS L73 |
| CL:91 | P7 | MOVE [169] | REPLIES | — |
| CL:92 | P8 | MOVE [170] | REPLIES | — |
| CL:93 | P9 | MOVE [171] | REPLIES | — |
| CL:97 | K1 | MOVE [172] | PROMPTS | — |
| CL:98 | K2 | MOVE [173] | PROMPTS | — |
| CL:99 | K3 | MOVE [174] | PROMPTS | — |
| CL:100 | K4 | CUT [175, S7] | — | struck |
| CL:101 | K5 | MOVE [176] | PROMPTS | — |
| CL:102 | K6 | MOVE [177] | PROMPTS | — |
| CL:103 | K7 | MOVE [178] | PROMPTS | — |
| CL:104 | K8 | MOVE [179] | PROMPTS | — |
| CL:105 | K9 | MOVE [180] | PROMPTS | — |
| CL:106 | K10a | CUT [181, D5] | — | LAWS L61 |
| CL:107 | K10 | CUT [182] | — | `DEPLOY-HUB.md`, LAWS L42 |
| CL:108 | K11 | MOVE [183] | PROMPTS | — |
| CL:109 | K12 | MOVE [184] | PROMPTS | — |
| CL:110 | K13 | CUT [185] | — | `CHECK-HUB.md:94` |
| CL:111 | K14 | CUT [186, S7] | — | struck |
| CL:112 | K15 | MOVE [187] | PROMPTS | — |
| CL:113 | K16 | MOVE [188] | PROMPTS | — |
| CL:114 | K17 | CUT [189, S7] | — | struck |
| CL:115 | K18 | MOVE [190] | PROMPTS | — |
| CL:116 | K19a | CUT [191, D32] | — | LAWS L61 (the R1330 blocked-call rule is folded there, R1342) |
| CL:117 | K19 | MOVE [192] | PROMPTS | — |
| CL:118 | K20 | MOVE [193, S20] | PROMPTS | — (it reads the archiver clause only since R1342) |
| CL:119 | K21 | MOVE [194] | PROMPTS | — |
| CL:120 | K22 | CUT [195, S7] | — | struck |
| CL:121 | K23 | CUT [196, D38] | — | `ops/desk/authorize.sh` |
| CL:122 | K24 | CUT [197, D40] | — | LAWS L67, L70 |
| CL:123 | K25 | CUT [198, D39] | — | `BUILD-HUB.md` PRE-STOP SELF-CHECK |
| CL:127 | M1 | MOVE [199] | MEMORY | — |
| CL:128 | M2 | MOVE [200] | MEMORY | `+ that rule here` becomes `+ that rule in this file's \`## ON TRIGGER\` section` |
| CL:129 | M3 | MOVE [201] | MEMORY | — |
| CL:130 | M4 | MOVE [202] | MEMORY | `a section of this file` becomes `an \`## ON TRIGGER\` section of this file` |
| CL:134 | CLOSE: | CUT [203, D7] | — | LAWS L58 and the wake-up's CLOSE WAIT |
| CL:135 | A late close is not a fault | MOVE [204] as `- CLOSE1 …` | CLOSE | — |
| CL:136 | Worktree cleanup is the desk's, never his command | MOVE [205] | CLOSE, in `- CLOSE2 …` after the R613 part | — |
| CT:7 | The desk plans, rules, writes prompts | MOVE [206, S9] | PLANNING | `; Fable-grade work = a spawned agent, after he says yes` |
| CT:8 | It writes its own prompts too | MOVE [207] | PLANNING | — |
| CT:9 | One step at a time | MOVE [208] | PLANNING | — |
| CT:10 | He pastes nothing | CUT [209, D35] | — | LAWS L61, `desk-launch.sh` |
| CT:11 | Day: prefill, day-open | MOVE [210] | PLANNING | ` + this file` |
| CT:12 | Every plate or queue item names its ladder line | MOVE [211] | PLANNING | — |
| CT:13 | Pending sittings are nagged | MOVE [212] | PLANNING | — |
| CT:14 | Never re-ask a ruled item | CUT [213] | — | LAWS L73, L77 |
| CT:15 | METER STOP | MOVE [214] | PLANNING | — |
| CT:16 | A refused read, edit or command is tried ONCE more | CUT [215, D2] | — | wake-up STEP 0 item 6 |
| CT:17 | Plan every task from the approved allow list first | MOVE [216, C7] | PLANNING | `; permission settings are his to edit — the desk hands him the command` |
| CT:18 | is never cut. Every wake-up logs | CUT [217, D3] | — | READ 7 |
| CT:19 | REFRESH (replaces R56's | CUT [218, D1] | — | EVERY TURN |
| CT:20 | He rules only scope, dates and money | CUT [219, D4] | — | LAWS L78 |
| CT:21 | GOAL: first builds good enough | CUT [220, S11] | — | R438 |
| CT:22 | Each hub in its own tab | MOVE [221] | LAUNCH | — |
| CT:23 | Cards and prompts for builds, checks | MOVE [222] | PROMPTS | ` The brain judges and informs; it writes no card, card row or prompt, and a desk request that it write one is FAILED unless a \`HIS RULING · APPROVED\` row names that card.` (its home is `BRAIN-HUB.md:23`) |
| CT:24 | For a single-feature deploy the desk writes | CUT [223, D5] | — | LAWS L61 |
| CT:25 | The desk records a next step only in the turn it launches it | CUT [224] | — | wake-up OWED |
| CT:26 | A feature's small findings go as rows on its OWN card | CUT [225, D6] | — | LAWS L75 |
| CT:27 | The nightly close is a MUST | CUT [226, D7, D8] | — | LAWS L58 |
| CT:29 | ≤5 sentences, plain prose | MOVE [227] | REPLIES | — |
| CT:30 | Routine launches, clean stop lines | MOVE [228] | REPLIES | — |
| CT:31 | Phone push only | MOVE [229] | REPLIES | — |
| CT:32 | Before an A/B reaches him, grep | MOVE [230] | REPLIES | — |
| CT:34 | Fable-type seats run Opus 5.5 until his word | MOVE [231] | LAUNCH | — |
| CT:35 | A seat runs its family's highest model | MOVE [232, S10] | LAUNCH | ` [stated 2026-10-01 · Dejan, R34; desk model set aside by 10-05 R371 below] On his ask it opens a Fable or Opus tab as \`brain\` for a reasoning task and folds the answer — a trial, going forward.` |
| CT:36 | Every Grok seat runs `grok-4.7` | CUT [233, D33, C13] | — | `CHECK-HUB.md:94`, `:95`; `ops/desk/house-probe.sh` |
| CT:37 | Every CTO desk successor runs Sonnet 5.5 | CUT [234, D25] | — | wake-up MODEL |
| CT:38 | The desk asks the brain FIRST | CUT [235, D9] | — | wake-up MODEL |
| CT:39 | The brain is a standing seat | CUT [236] | — | `BRAIN-HUB.md:3` |
| CT:40 | A drafter copying an established precedent runs on Sonnet | MOVE [237] | LAUNCH | — |
| CT:42 | THE NEXT FLOW | MOVE, change 4 only [238, S8] | PROMPTS | the line becomes exactly `- Every drafter proves each \`file:line\` and count against BASE and records each read in \`## RECORDS\`; no fixed hub holds the drafter shape. Docs-only hub-text cards are checked with house A none under 2026-10-02 R47 until the staging includes \`docs/40 - DevDocs/prompts/\` (brain ruling, 2026-10-06 R488).` (both sentences are `CT:42`'s own text) |
| CT:43 | R412's "no outside-house reads" | CUT [239, S8] | — | history |
| CT:44 | Every drafter: a draft uses only the existing | MOVE [240, C7] | PROMPTS | ` and goes to him` |
| CT:45 | Order: tags (MODEL · SEAT · SESSION | MOVE [241] | PROMPTS | — |
| CT:46-56 | `## Checklist — open the section` and its ten bullets | CUT [242] | — | W1 (e) carries the trigger map |
| CT:58-59 | `## Retrieval` | CUT [243] | — | — |

## NOT IN THIS JOB
- Any file under `/Users/cobalt/Vault`: the topic files are read, never edited; the desk retires them after the deploy, folds `preferences.md` and L82-L84 (R1337, R1341).
- `UNATTENDED-LAUNCH.md` and its move into the wake-up: card 479. `STANDING-LIST.md`: card 481. `BRAIN-HUB.md`: card 482. The CLOSE-HUB stop line and launch line: card 483.
- The wake-up's `- LAUNCH ` line, MODEL line, SEAT PROFILE, CLOSE WAIT, OWED and EVERY TURN text; card 458's four texts (`STATE (card 458)`, `3a.`, `RECONCILE (card 458)`, the hook clauses at EVERY TURN) stand byte for byte.
- The READ item 3 `awk` read (`:31`, map row 313, C11): not this card's.
- Any `ops/`, `src/` or `configs/` file; any with-DB test (`DB: none`).

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-map-2026-10-13.md` `## MAP` rows 102-243, `## DUPLICATES`, `## DECISIONS`.
- `/Users/cobalt/Vault/Think/6 - Permanent/Memory/topics/cto-desk-checklist.md` whole (136 lines); `/Users/cobalt/Vault/Think/6 - Permanent/Memory/topics/cto-desk-contract.md` whole (59 lines).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` whole; `CLOSE-HUB.md` lines 14-16, 42-45.
- `/Users/cobalt/Vault/Think/6 - Permanent/Memory/topics/writing-rules.md` (read path, `wc -c` rule).
- Precedent card: `prompts/2026-10-13/458-desk-refresh-card.md` row W1 (hub text, a test on the real file).

## CHECK ASKS
- X1 Does every MOVE row of `## THE LINE LIST` stand in its heading with the source text byte for byte but for the named cut and the removed tags? Re-derive from the two topic files.
- X2 Does any CUT or ELSEWHERE line, or any named cut clause, still stand in the wake-up?
- X3 Is any line of the topic files neither in the table nor a heading, a tag line or front matter?
- X4 Do `test_hub_lines.py`, `test_desk_wakeup_rule.py`, `test_stop_guard.py` and card 458's `test_desk_refresh_wakeup.py` stay green unchanged?
- X5 Do CLOSE-HUB step 3's greps still find a lesson that the checklist carried (its ids now stand in the wake-up)?
FOR THE CHECK: rules cut 2026-10-13 HIS RULING: the whole cut list executed (13 contradictions, 25 stale, 40 duplicate groups deleted; moves as mapped; preferences to preferences.md; L82-L84 added, vetoable)
FOR THE CHECK: rules-cut cards 2026-10-13 brain: 11 KEEP; STANDING-LIST:107 deleted (CHECK-HUB wins, R1340); cards fill gaps behind MVP cards

## DEPLOY PROOF
- `grep -c -F "## ON TRIGGER — " "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` · before `0` · after `11`
- `grep -c -F "cto-desk-checklist" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` · before `1` · after `0`
- `grep -c -F "cto-desk-checklist" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CLOSE-HUB.md"` · before `2` · after `0`

## RECORDS
- Reads by the drafter `draft-rules-cut-cards`, 2026-10-13 07:20-07:40 ET, at `main` HEAD `7516154c` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`). `git -C /Users/cobalt/cobalt status --short -- ops tests "docs/40 - DevDocs/prompts"` printed one untracked dated prompt only: every repo `file:line` here is HEAD's.
- `git show HEAD:"docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` whole; `grep -n -E "CONTRACT|CHECKLIST|^ON TRIGGER|^- "` on it: `:8` CONTRACT/CHECKLIST paths, `:22` `open CHECKLIST \`## handover\`` and `(CHECKLIST H2)`, `:29` `CONTRACT whole`, `:36` `CHECKLIST W3 and L1`, `:46-50` the ON TRIGGER map, `:51-53` the three bullets that stand.
- `cat -n` of `CL` (136 lines) and `CT` (59 lines): every id and literal of `## THE LINE LIST` at the line named; `CL:9` already carries R1323, `CL:116` the R1330 rule, `CL:118` the archiver clause only (R1342 fold, 07:27). `wc -c`: `CL` 23,526, `CT` 11,230, wake-up 12,794.
- `grep -n -E "cto-desk-checklist|…|checklist"` over the fixed files: `CLOSE-HUB.md:15`, `:16`, `:44` (and `STANDING-LIST.md:184`, a never-touches cell, left); no `ops/`, `tests/`, `src/` or `configs/` file names either topic file (`grep -rln`, no output).
- `ops/desk/job-clean.sh:3` (`job-clean.sh salvage <worktree-name>`) and `:12` (`Salvage mode (worktree-salvage, R613)`): the R613 clause "until it ships" is stale.
- Card 458 (`458-desk-refresh-card.md` row W1) edits `CTO-DESK-WAKEUP.md` `:23`, `:36`, `:40`, `:42`: BASE is set after 458 merges; every anchor above is by text.
- Map DECISIONS item 3 (ON TRIGGER headings, the start READ list unchanged) and item 5 (CLOSE-HUB step 3 points at the wake-up): brain KEEP, `cto-2026-10-13.md` R1337.
