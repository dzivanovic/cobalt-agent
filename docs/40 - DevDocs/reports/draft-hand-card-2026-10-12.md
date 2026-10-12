## §0 Headline
- Card `prompts/2026-10-12/393-needs-his-hand-card.md` written, class K5, one row N1, hub text only.
- Close prompt (`CLOSE-HUB.md`) and day-open prompt (`DAY-OPEN-QWEN.md`) each gain `## NEEDS HIS HAND`, entry shape byte for byte from his item 3, `none` when empty, by day only.
- Red test: new `tests/ops/test_needs_his_hand.py`, five tests (name once, shape once, four rules in one line, placement, line counts 65→66 and 29→30 plus launch line untouched). Nothing was run: no `uv` on this seat.

## DECISIONS
- ASK DESK: the day-open prompt is `DAY-OPEN-QWEN.md` (no `DAY-OPEN.md` exists); the card edits it. Confirm. [from `date`: 2026-10-12] Default: as written.
- ASK DESK: the day-open's S0 path has the `cobalt day-open` command write the report itself; the card has the seat append the section to that file. If the command's writer should own the section, that is a `src/` card, not this one. [2026-10-12] Default: seat appends.
- ASK DESK: the close prompt names the section once (in the shape chain) and spells it `NEEDS-HIS-HAND` in the rule line, so the exact string occurs once. [2026-10-12] Default: as written.
- ASK DESK: `BASE` is the placeholder `«FILL: BASE …»`; `TIP` empty; `HOUSE B: as needed` (CARD.md shows it empty on a build, card 361 fills it). [2026-10-12] Default: as written.

## RECORDS
- Read: `prompts/CARD.md` whole; `reports/hands-off-answer-2026-10-12.md` whole (item 3 `:13`, K5 `:24`, C4 `:33`); `prompts/CLOSE-HUB.md` whole (65 lines); `prompts/DAY-OPEN-QWEN.md` whole (29 lines); `tests/ops/test_hub_lines.py` whole; `prompts/2026-10-11/361-held-table-row-card.md` whole; `topics/writing-rules.md` whole. HEAD `6468fb5e` (`git rev-parse --short=8 HEAD`).
- `restarts.py:225-228` read: `docs/` → DOCS. `test_desk_size_guard.py:226-228` read. `cto-2026-10-12.md:12` is R1138, APPROVED.
- UNPROVEN: the five tests' red results (no test run); `tests/` restarts class (`:245-246`, from card 361); whether tests at `test_bare_guard.py:1365`, `test_stop_guard.py:406` read the real report shape (hit lines only).
- No git write, no launch, no production command.

DRAFTED · decisions: 4
