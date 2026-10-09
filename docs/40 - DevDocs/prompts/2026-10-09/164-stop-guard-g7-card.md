JOB: stop-guard-g7-1009
LADDER: OFF-LADDER — reports/desk-idle-answer-2026-10-09.md 2026-10-09 R724
BRANCH: ops/stop-guard-g7-1009
WORKTREE: stop-guard-g7-1009
BASE: 1458693d
TIP: b8047e79
REPORT: /Users/cobalt/cobalt-wt/stop-guard-g7-1009/docs/40 - DevDocs/reports/stop-guard-g7-build-2026-10-09.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/stop-guard-g7-check-2026-10-09.md
HOUSE B: as needed
DB: none
RULINGS: 2026-10-08 R685

## ROWS

| row | what | red first | files |
|---|---|---|---|
| T0 | Test fixture and two touched tests, before any red. `Desk.owed` (`tests/ops/test_stop_guard.py:306`) takes `rows: tuple[str, ...] = ()`: each row is written under the `| CTO desk |` row of the session table, inside `## §5 CURRENT`, before `## §5 HISTORY`. Two existing tests name a `waiting on Dejan` item with no `R<n>`; after G7 (b) that item is unsettled, so its text gains one: `:456` `OWED: a \| waiting on Dejan` → `OWED: a (asked R1) \| waiting on Dejan`; `:564` `OWED: w \| waiting on Dejan` → `OWED: w (asked R1) \| waiting on Dejan`. Their assertions are unchanged. `:409` (`fold R1`) and `:675` (fails open at parse) stay | none: green on BASE and after, unchanged assertions | `tests/ops/test_stop_guard.py` |
| G7a | A `## §5 CURRENT` table row whose first cell starts `QUEUE` is unsettled. Today the guard reads only the OWED block (`ops/desk/stop-guard.py:20-22`, `owed_block` `:198-241`, `unsettled` `:269-292`); the session table under it is never read. Add: after every OWED item is settled (`desk` `:313-317`), the first line under `## §5 CURRENT` and before the next line that starts `## ` that starts with `\|` and whose first cell, stripped, starts with `QUEUE` → `start it: <its third cell, stripped>` (the `prompt · tab` cell); a QUEUE row with fewer than three cells names the row, stripped. One read of the report. A missing block keeps the message at `:310`. Header comment `:20-26` names the rule (card 164 G7 (a), his 2026-10-09 R724) | RED (a) `test_g7a_a_queue_row_in_current_blocks`: `d.owed("owed: none", rows=("\| QUEUE \| — \| x card \| — \| x \|",))`; asserts `(r.returncode, r.stdout, r.stderr) == (2, "", "start it: x card\n")`. BASE: exit 0, `stderr ""` | `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py` |
| G7b | A `waiting on Dejan` item is settled only when its `<what>` holds `R<digits>` (regex `\bR\d+\b`). Today `if marker == WAITING: continue` (`:274-275`) settles every such item. Without `R<n>` → `start it: ask him: <what>`. `unsettled` returns the line's text after `start it: ` so the caller at `:317` prints it unchanged. Header `:22-23` and the docstring `:270` say it | RED (b) `test_g7b_waiting_on_him_without_a_row_blocks`: `d.owed("OWED: build 72 \| waiting on Dejan")`; asserts `(2, "", "start it: ask him: build 72\n")`. BASE: exit 0. NEGATIVE CONTROL (b) `test_g7b_waiting_on_him_with_a_row_lets_the_turn_end`: `d.owed("OWED: Finviz rate D2 (asked R722) \| waiting on Dejan")`; asserts `(0, "", "")`, BASE and after. MUTATION: `\bR\d+\b` → a pattern that matches nothing turns the control red | `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py` |
| G7c | A `live: <id>` that matches a `desk-list.sh` row named `brain` settles only an item whose `<what>` contains `brain`. Today any row not named `cto-desk` settles (`:288-289`). After: settled when some row with `i.startswith(sid)` has a name that is neither `cto-desk` nor `brain`, or is `brain` and `"brain" in what`; else unsettled, `start it: <what>`. The brain seat's session name is `brain` (`prompts/BRAIN-HUB.md:8` `--name brain`) | RED (c) `test_g7c_the_brains_id_on_a_desk_item_blocks`: `d.lister("f20cc306-0000 · brain · ~/cobalt · busy · working")`, `d.owed("OWED: launch https card \| live: f20cc306")`; asserts `(2, "", "start it: launch https card\n")`. BASE: exit 0. NEGATIVE CONTROL (c) `test_g7c_the_brains_id_on_a_brain_item_lets_the_turn_end`: same lister, `d.owed("OWED: brain checks card 134 draft \| live: f20cc306")`; asserts `(0, "", "")`, BASE and after. MUTATION: brain rows never settle → the control is red. `test_g3_a_live_session_id_lets_the_turn_end` (`:464`) and `test_g3_the_desks_own_row_is_not_live` (`:480`) stay green | `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py` |
| V | RUN — asserts nothing. `uv run pytest -q -p no:cacheprovider tests/ops/test_stop_guard.py` → `0 failed`; then the deploy gate. Quote both. Each red is shown exit 0 on BASE (the five new tests run against the BASE copy of `ops/desk/stop-guard.py`, with T0's fixture) and each mutation's red, with output | — | none |

## NOT IN THIS JOB
- The worker path (`worker` `:353`), the count and give-up (`:295-330`), the session-list failure (G2 of card 106), the watch form, `is_desk`, `owed_block`'s parse rules and fail-open lines.
- Any test beyond the three reds, two controls and T0's edits (L75: touched tests plus the deploy gate, no re-check).
- `desk-list.sh`, any other `ops/desk` script, any hub, any `settings.json`, any `src/` file.
- The desk's RULE NOW (1-4) in `reports/desk-idle-answer-2026-10-09.md`: the desk's record, not code.
- A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-idle-answer-2026-10-09.md` `## CARD ROW` (G7).
- `ops/desk/stop-guard.py` lines 15-34, 89-96, 198-241, 244-292, 295-330.
- `tests/ops/test_stop_guard.py` lines 262-334, 400-460, 464-486, 562-566, 672-682.
- `prompts/2026-10-06/66-desk-stop-guard-card.md` (the feature's card).

## CHECK ASKS
- X1 A desk stop is blocked by a §5 QUEUE row, by a `waiting on Dejan` item without R<n>, and by a desk item settled only by the brain's id (G7, desk-idle-answer-2026-10-09.md).

## RECORDS
- BASE `1458693dbde5371259a29c5d502d74e3878fee3b` (`git -C /Users/cobalt/cobalt rev-parse main`, 2026-10-09 11:37 ET); `git -C /Users/cobalt/cobalt diff --stat main -- ops/desk/stop-guard.py tests/ops/test_stop_guard.py ops/desk/desk-list.sh` prints nothing, so every `file:line` above is BASE's.
- `desk-list.sh` prints `id · name · cwd · status · state` (`ops/desk/desk-list.sh:3`, `:16`); `listed()` keeps `(id, name)` (`stop-guard.py:254-255`).
- Today's desk report holds three `QUEUE` rows in `## §5 CURRENT` (`reports/cto-2026-10-09.md:35-37`): after this deploy they block the desk's stop until the desk turns each into an `OWED:` line (RULE NOW 1).
- RESTARTS classes, one home per path (K10): `ops/desk/stop-guard.py` is an operator script (`grep -c -F "ops/desk" configs/cobalt/jobs.yaml` → `0`, 2026-10-09 11:37 ET); `tests/ops/test_stop_guard.py` is test; the report is DOCS. Expected `RESTARTS: none`; the build runs `uv run cobalt jobs restarts <BASE>..HEAD` and quotes it.
- WHERE IT RUNS: the Stop hook runs `python3 /Users/cobalt/cobalt/ops/desk/stop-guard.py` (the header's INSTALL, `stop-guard.py:47`), the main checkout's file, fresh on every stop: the change takes effect when the deploy merges to main.
- ORDER: this card builds after the https-only card (`prompts/2026-10-09/156-https-only-card.md`, JOB `https-only-1009`) deploys.
