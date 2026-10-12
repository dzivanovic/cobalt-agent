JOB: needs-his-hand-1012
CLASS: K5
LADDER: OFF-LADDER — reports/cto-2026-10-12.md R1138
BRANCH: ops/needs-his-hand-1012
WORKTREE: needs-his-hand-1012
BASE: 6468fb5e
TIP: ad73d04a
REPORT: /Users/cobalt/cobalt-wt/needs-his-hand-1012/docs/40 - DevDocs/reports/needs-his-hand-build-2026-10-12.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/needs-his-hand-check-2026-10-12.md
HOUSE B: as needed
DB: none
RESTARTS: none
RULINGS: 2026-10-12 R1138

## ROWS

WHY: his standing item 3 (`reports/hands-off-answer-2026-10-12.md:13`, LAWS L81, row R1138 of `reports/cto-2026-10-12.md:12`) and class K5, HARNESS UPKEEP (`:24`: hub lines that serve K1–K4, changed by card). The two prompts that write a morning or night report carry no place for an item only he can do. Hub text only: the item goes into one named section of the report, never into a relay or a wait.

THE TEXT, one fact per line, byte for byte as quoted (the section name appears ONCE in each file):

ENTRY SHAPE (his item 3, byte for byte): `what was blocked · by which rule or tool · why no seat could do it · the exact line he types · what it unblocks`

`prompts/CLOSE-HUB.md`:
- `## REPORT (L48)`, line 34, the shape chain `… → ## DECISIONS → ## RECORDS → the stop line` becomes `… → ## DECISIONS → ## NEEDS HIS HAND → ## RECORDS → the stop line`. That is the only edit of an existing line.
- ONE new line directly after line 34 (the paragraph's own last line), no heading:
  `The NEEDS-HIS-HAND section: `none` when nothing is owed; else one entry per item: what was blocked · by which rule or tool · why no seat could do it · the exact line he types · what it unblocks. Work around the blocked ITEM, never around a permission check. An item for his hand is raised by day only; at night it waits in this section and the rest runs.`
  (the heading name is NOT repeated in that line: it is spelled `NEEDS-HIS-HAND` there, so the exact string `## NEEDS HIS HAND` occurs once in the file.)

`prompts/DAY-OPEN-QWEN.md`:
- ONE new line directly after line 28 (the `Table:` line, which ends `Last line: NEXT: …`) and before the final `/no_think`:
  `Above that last line the report carries `## NEEDS HIS HAND` (on the S0 path too: append it to the file the command wrote): `none` when nothing is owed; else one entry per item: what was blocked · by which rule or tool · why no seat could do it · the exact line he types · what it unblocks. Work around the blocked ITEM, never around a permission check. An item for his hand is raised by day only; at night it waits in this section and the rest runs.`

| row | what | red first | files |
|---|---|---|---|
| N1 | The close prompt's report shape names `## NEEDS HIS HAND` once, between `## DECISIONS` and `## RECORDS`, and carries the entry shape, the `none` rule, the work-around-the-item rule and the by-day-only rule in ONE new line after `CLOSE-HUB.md:34`. The day-open prompt carries the same four rules in ONE new line after `DAY-OPEN-QWEN.md:28`, naming the section once. Nothing else in either file changes: not the launch line (`CLOSE-HUB.md:10`), not an allow or deny string, not a guard, not a step. Backed by `hands-off-answer-2026-10-12.md:13` (item 3) and `:33` (card C4) | A new file `tests/ops/test_needs_his_hand.py`, in the style of `tests/ops/test_hub_lines.py` (`HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"`, a file read by `(HUBS / name).read_text(encoding="utf-8").splitlines()`, `pytest.mark.parametrize` over the two names, no tmp repo, nothing run). Five tests. (1) `test_the_section_is_named_once_in_each_file` — `text.count("## NEEDS HIS HAND") == 1` for `CLOSE-HUB.md` and `DAY-OPEN-QWEN.md`. RED on `BASE`: the count is 0. (2) `test_the_entry_shape_is_written_once_byte_for_byte` — `text.count(SHAPE) == 1`, `SHAPE` the five-part string of THE TEXT above; RED on `BASE`: 0. (3) `test_the_four_rules_stand_in_the_one_line` — the one line holding `SHAPE` also holds ``none`` (backticked), `never around a permission check`, `by day only` and `at night it waits in this section and the rest runs`; RED on `BASE`: no line holds `SHAPE`. (4) `test_the_section_sits_where_the_text_puts_it` — `CLOSE-HUB.md`: the line starting `` `<REPORT>`, shaped: `` holds `## DECISIONS → ## NEEDS HIS HAND → ## RECORDS`, and the `SHAPE` line is the very next line; `DAY-OPEN-QWEN.md`: the `SHAPE` line is the line after the one starting `Table: check | verdict`, and the last line of the file is `/no_think`. RED on `BASE`: the chain lacks the name; no `SHAPE` line. (5) `test_nothing_else_changed` — the line count of `CLOSE-HUB.md` is 66 and of `DAY-OPEN-QWEN.md` is 30 (`BASE`: 65 and 29, `grep -c ""` each); `CLOSE-HUB.md` still holds exactly one line starting `claude --bg `, whose `--allowedTools` strings number 21 and `--disallowedTools` strings number 11 (parsed with the `tools` helper of `test_hub_lines.py`, copied into the new file, not imported), carries `--permission-mode dontAsk` and no `NEEDS`; `DAY-OPEN-QWEN.md` still holds `COBALT_ENV=production uv run cobalt day-open verdict` once. GREEN on `BASE` for the launch-line parts, RED for the two line counts (65 ≠ 66, 29 ≠ 30). The row ends with `uv run pytest -q tests/ops/test_needs_his_hand.py tests/ops/test_hub_lines.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_bare_guard.py tests/ops/test_stop_guard.py tests/ops/test_desk_size_guard.py` → `0 failed`, and `wc -c` of each prompt before and after is quoted in the report (the growth is the one line; writing-rules.md: the growth is named) | `docs/40 - DevDocs/prompts/CLOSE-HUB.md`, `docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md`, `tests/ops/test_needs_his_hand.py` |

## NOT IN THIS JOB
- Any launch line, allow string, deny string, `--add-dir`, model, permission mode or guard: `CLOSE-HUB.md:10`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `ops/desk/authorize.sh`, `ops/desk/install-fixed.sh`, `.claude/settings.json`.
- Any other prompt: `BUILD-HUB.md`, `CHECK-HUB.md`, `DEPLOY-HUB.md`, `DEVFIX-HUB.md`, `CTO-DESK-WAKEUP.md`, `BRAIN-HUB.md`, `CARD.md`. The morning plate and the desk's own report are the desk's.
- A step, a stop line, a refusal, a report section other than the one new section and the one new line; `ops/` and `src/cobalt/` code; any with-DB test.
- The day-open command's own report writer (`cobalt day-open`): its output is not edited here; the seat appends the section.
- Cards C1, C2, C3, C5 and their rows (`hands-off-answer-2026-10-12.md:30-34`).

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hands-off-answer-2026-10-12.md` `:13` (item 3), `:24` (K5), `:33` (C4).
- `prompts/CLOSE-HUB.md` `:33-34` (`## REPORT (L48)`), `:63-65` (`## STOP LINE`), `:10` (the launch line, read only).
- `prompts/DAY-OPEN-QWEN.md` `:27-29` (`## VERDICT`), `:9` (S0).
- `tests/ops/test_hub_lines.py` `:54-70` (`hub_line`, `tools`), `:76-98` (the parametrized pins).
- Precedent: `prompts/2026-10-11/361-held-table-row-card.md`.

## CHECK ASKS
- X1 Is the exact string `## NEEDS HIS HAND` in each of the two files once, and is `SHAPE` there byte for byte (the ` · ` separators, no change of word)?
- X2 `git diff <BASE>..<TIP> -- "docs/40 - DevDocs/prompts/CLOSE-HUB.md"` and the same for `DAY-OPEN-QWEN.md`: is every changed line the one named in THE TEXT, and is the launch line `CLOSE-HUB.md:10` byte for byte as on `BASE`?
- X3 Does any sentence the build added permit a seat to bypass a permission check, ask him for a command at night, or end its turn to wait for him?
- X4 Does any existing test or script read the `## REPORT (L48)` shape chain of the close or the `Table:` line of the day-open (a `grep -rn` over `tests/` and `ops/`)? Name each hit.

## RECORDS
- Read by the drafter `draft-hand-card`, 2026-10-12, against `HEAD` `6468fb5e` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`). `git -C /Users/cobalt/cobalt status --short -- ops tests "docs/40 - DevDocs/prompts/CLOSE-HUB.md" "docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md"` prints nothing, so every `file:line` here is HEAD's.
- The two prompts: `grep -rn` over `docs/40 - DevDocs/prompts/` for `DAY-OPEN` and `CLOSE-HUB` finds the day-open prompt at `DAY-OPEN-QWEN.md` (title `# DAY-OPEN`, `:3`; no file named `DAY-OPEN.md` exists: `ls` of the folder) and the close prompt at `CLOSE-HUB.md` (title `:1`). Each read whole.
- Line counts at `HEAD`: `CLOSE-HUB.md` 65, `DAY-OPEN-QWEN.md` 29 (`wc -l` and `grep -c ""` agree).
- The close's launch line is `CLOSE-HUB.md:10`, its list is 21 allow and 11 deny (`:12`); the report shape chain is `:34`. The day-open's `Table:` line is `:28` and `/no_think` is `:29`.
- `grep -rn "NEEDS HIS HAND"` over `/Users/cobalt/cobalt` finds only prompt 391, `reports/cto-2026-10-12.md` and `reports/hands-off-answer-2026-10-12.md`: no prompt carries the section yet.
- His approval: row R1138 (`reports/cto-2026-10-12.md:12`, `HIS RULING · APPROVED`, K1–K5 and the four standing items) and LAWS L81; this card is class K5 and is built and checked with no further word of his.
- Pattern of the test: `tests/ops/test_hub_lines.py` reads a hub as `(HUBS / name).read_text(encoding="utf-8").splitlines()` (`:55`), keeps the line starting `claude --bg ` (`:55-57`) and splits it with `shlex.split` after each `--allowedTools` or `--disallowedTools` (`:60-70`); its parametrized names are in `KINDS` (`:30`), which holds no `CLOSE-HUB.md` and no `DAY-OPEN-QWEN.md`, so the new test names them itself.
- Other tests that name `CLOSE-HUB`: `tests/ops/test_bare_guard.py:1365`, `tests/ops/test_desk_launch_prechecks.py:46` and `:86`, `tests/ops/test_stop_guard.py:406`, `tests/ops/test_desk_size_guard.py:226`. The first, second and fourth quote the launch line or write a constructed close prompt; the fifth writes a one-line fixture (`test_desk_size_guard.py:226-228`, read). The bodies of the other tests were not read beyond their hit lines: whether any reads the real report shape is UNPROVEN, X4 asks the check to prove it.
- RESTARTS: none. A path under `docs/` derives `DOCS` (`src/cobalt/jobs/restarts.py:225-228`: `path.startswith("docs/")` → `Classification(path, item.change, "DOCS", ())`, read by the drafter). `tests/` derives `test/documentation; no resident` (`:245-246` per card 361's record, not re-read here). The build hub runs `uv run cobalt jobs restarts <BASE>..HEAD` and quotes `RESTARTS: none`.
- `uv run pytest` is not on the drafter's allow list: no test was run. Each red test above is a prediction from the file text at `HEAD` (UNPROVEN until the build's red-first run).
- No preflight ran. `BASE` is the desk's placeholder, filled at the launch; `TIP` is empty (build).
