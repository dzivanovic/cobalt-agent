# Draft: K5 card, the card template (2026-10-14)

## §0 Headline
- Card `prompts/2026-10-14/550-card-template-card.md` written: job `card-template-1014`, K5, `RULINGS: 2026-10-14 R1471`, `BASE` and `TIP` empty.
- Rows C1 (`## DEPLOY PROOF` required in `CARD.md`), C2 (a "how a card cites and pins" section: rulings by R number, anchors by `file:line` on `git show`, tests pin only their card's lines, no hash or `BASE` literal), R3 (restarts run). Red first: a new `tests/ops/test_card_template_1014.py`; a negative control keeps the four tests that already pin `CARD.md` green.
- Source of truth: `CARD.md` (format), `deploy-card.sh:534-543` (how `## DEPLOY PROOF` is read). Nothing was run (no `uv run`): every RED is UNPROVEN.
- 5 decisions, all defaults taken.

## DECISIONS
1. ASK DESK: the survey (`reports/survey-blockers-2026-10-12.md`) holds no card-template row (`grep -i template` → no hit); the wording comes from his R1471 and brain R1472 only, as the prompt owes. Default: any sentence beyond those two rows would be `ASK DESK`; none was added, so the card stands as written. [07:37]
2. ASK DESK: "DEPLOY PROOF required" bites today only through `deploy-card.sh:534-543` (a missing section leaves a `«FILL`, so the deploy card cannot launch); `desk-launch.sh` does not refuse a BUILD card without it. Default: docs rule and test only, no launcher change (outside this card's files). [07:37]
3. ASK DESK: card 537 rows S1 (2) and S2 (2) tell the builder to write `BASE` into the test as an 8-hex literal and to read `git show <BASE>`, which the new rule (his R1471: no `BASE` literal in a test) forbids. Default: card 550 does not touch 537; amend 537 before its build if the rule is to bind it. [07:37]
4. ASK DESK: the header table of `CARD.md` (`:11-29`) has no `CLASS`, `INSTALL` or `RESTARTS` key, though every K5 card carries them. No ruling traces to adding them. Default: not added. [07:37]
5. ASK DESK: cards 546-549 are not written, so their `CARD.md` line ranges cannot be compared; 521, 523 and 537 edit no `CARD.md` line. Default: this card edits only one new line after `CARD.md:55` and one new section after `:73`; the desk compares when 546-549 land. [07:37]

## RECORDS
- 2026-10-14 07:37 ET, `main` HEAD `0ffb6949`. Read: prompt 545; `prompts/CARD.md` (`git show HEAD:`, whole); cards 523 and 516, 537 (shape); `ops/desk/deploy-card.sh:24-37`, `:505-550`; `reports/cto-2026-10-14.md` rows R1471, R1472 and `-words.md` R1471; `reports/deploy-hub-text-1013.md` tail; `survey-blockers-2026-10-12.md` rows 1-33; tests that read `CARD.md` (`grep -n "CARD.md" tests/ops`); `git status --short` on `CARD.md`, the four pinning tests and `deploy-card.sh` → nothing (HEAD's).
- Pins on `CARD.md`: `test_deploy_card.py:426-434`, `test_prodwrite_hub.py:145-150` and `:187-191`, `test_deploy_step_c.py:332-334`, `test_desk_launch_prechecks.py:826-832`; none reads a line the two insertions touch.
- No drafter-prompt shape file exists among the fixed prompts (`grep -l -i "drafter prompt"` over `prompts/*.md` → none). Cards 546-549 were not on disk.
- No test was run, nothing launched, no git write.

DRAFTED · decisions: 5
