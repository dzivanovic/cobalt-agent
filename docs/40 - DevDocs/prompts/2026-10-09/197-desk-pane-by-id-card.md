JOB: desk-pane-by-id-1009
LADDER: OFF-LADDER — reports/cto-2026-10-09.md R779
BRANCH: ops/desk-pane-by-id-1009
WORKTREE: desk-pane-by-id-1009
BASE: 044f58b5
TIP:
REPORT: /Users/cobalt/cobalt-wt/desk-pane-by-id-1009/docs/40 - DevDocs/reports/desk-pane-by-id-build-2026-10-09.md
CHECK REPORT:
HOUSE B:
DB: none
RULINGS: 2026-10-08 R685

## ROWS

All four rows change `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` and nothing else. `grep -c -F` of each old sentence on that file is 1 on `BASE`.

| row | what | red first | files |
|---|---|---|---|
| P1 | VIEW line (`CTO-DESK-WAKEUP.md:14`): the desk has ONE pane, by the id in §5 CURRENT, never by label. The label "CTO" is used only when that id is gone from `herdr pane list`; then `herdr tab create … --label "CTO"` and the new id goes into §5. Replaces the clause `no id there → `herdr tab list` (find the "CTO" tab)` and drops "never `herdr pane list`" (the id-gone test reads that list). Backed by the brain's FIX 1 and 4, `reports/desk-tab-answer-2026-10-09.md` lines 10 and 13 | RUN — `grep -c -F 'no id there → `herdr tab list` (find the "CTO" tab)' "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` prints 1 on `BASE`, 0 after. Quote both | `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` |
| P2 | STEP 0 item 2 (`:22`): the successor, right after `claude stop <p>` and `claude rm <p>` (the predecessor's attach has ended), runs `herdr pane run <pane id from the HANDOVER line> "claude attach <own id>"`; an exit box first takes `send-keys Enter`; alive = `pgrep -fl "claude attach <own id>"`. The sentence `A pane → leave it, name it in the plate as closable.` is replaced by this re-attach. Backed by FIX 2 and 3, `desk-tab-answer-2026-10-09.md` lines 11 and 12; checklist H3a and H4 carry the same | RUN — `grep -c -F 'A pane → leave it, name it in the plate as closable.' "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` prints 1 on `BASE`, 0 after | `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` |
| P3 | STEP 0 item 4 (`:24`): no seat creates, renames or labels a desk tab while the desk pane exists; a new tab only when its id is gone from `herdr pane list`, labelled "CTO" once, recorded in §5; any other desk tab is closed the same turn (`herdr tab close`). Replaces `One herdr tab "CTO" with a live VIEW of you; create or re-attach as needed; close any other desk tab.` Backed by FIX 1 and 4, `desk-tab-answer-2026-10-09.md` lines 10 and 13 | RUN — `grep -c -F 'One herdr tab "CTO" with a live VIEW of you; create or re-attach as needed; close any other desk tab.' "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` prints 1 on `BASE`, 0 after | `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` |
| P4 | HANDOVER shape in STEP 0 item 2 (`:22`) reads `HANDOVER: predecessor <p> → successor <s> at <time> · pane <id>`; item 1 (`:21`) names no shape and stays. The successor reads the pane id from this line. The `(stuck; ended by successor)` variant in item 2 keeps its own shape (no predecessor pane was handed over; the successor takes the pane id from §5 CURRENT). Backed by FIX 2, `desk-tab-answer-2026-10-09.md` line 11 | RUN — `grep -c -F '· pane <id>' "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` prints 0 on `BASE`, 1 after | `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` |

The brain's red `grep -c 'VIEW it in the "CTO" tab'` is in the checklist (memory, already changed by the desk), not in this file; the four greps above are this file's red.

## NOT IN THIS JOB
- `topics/cto-desk-checklist.md` (REFRESH HOW steps 5–6, H3a) and every other memory file: the desk already changed them; this job does not touch them.
- Any file but `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`: no `ops/desk/` script and no `stop-guard.py` change; none parses the new `· pane` tail (`## RECORDS`).
- The NOW step of the brain's answer (FIX 5: the live desk re-attaches in one tab and closes stale tabs): the desk does it by hand, once.
- Any new command or script (R411, R412); only `herdr pane run`, `herdr pane list`, `herdr tab create`, `herdr tab close`, `pgrep` and `claude stop` / `claude rm` / `claude attach`, which the file already names.
- Any other line of the wake-up: the PATHS block, the LAUNCH line, STEP 0 items 1, 3, 5, 6, READ, OWED, CLOSE WAIT, ON TRIGGER.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-tab-answer-2026-10-09.md`: `## FIX` items 1–4 (the rows) and the "Red for the card" line.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` lines 14, 21–24 (the lines the rows change).
- `/Users/cobalt/Vault/Think/6 - Permanent/Memory/topics/cto-desk-checklist.md` lines 12 (H3a, H4) and 17 (REFRESH HOW 5–6): already changed memory; the wake-up text must say what they say. Read only.
- `/Users/cobalt/Vault/Think/6 - Permanent/Memory/topics/writing-rules.md` `## How`: the file is on the read path (imperative, one fact per line, no quotes, no history); `wc -c` before and after, the after smaller or the growth named in the report.
- `ops/desk/desk-wake.sh:75`: the only reader of the HANDOVER line.

## CHECK ASKS
- X1 Brain 10-09 (desk-tab-answer-2026-10-09.md): one desk pane by id, never by label; the successor re-attaches in the predecessor's pane after stop+rm; no REFRESH creates a tab while that pane exists.
- X2 Does any sentence left in `CTO-DESK-WAKEUP.md` still say the desk finds its pane by the label "CTO", or that a pane is left open, other than the id-gone case?
- X3 Is the file's diff limited to lines 14, 22 and 24 and the length named in the report?

## RECORDS
- BASE reads, all against main HEAD `a82d8b6f` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`; `git -C /Users/cobalt/cobalt diff --stat a82d8b6f -- "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` prints nothing, so the working file is the HEAD file); the drafter at 2026-10-09 evening.
- `grep -c -F` of the old sentences in `CTO-DESK-WAKEUP.md`: P1 clause 1, P2 sentence 1, P3 sentence 1; `grep -c -F '· pane <id>'` 0.
- `grep -n "pane\|HANDOVER" ops/desk/*`: `desk-wake.sh:75` reads `^HANDOVER: .* at ([0-9]{2}:[0-9]{2})`, which still matches with a `· pane <id>` tail; `desk-handover.sh:6,37,39` and `desk-launch.sh:407` name only the word or the env var, `gate-lists.md:30` is unrelated. No script breaks, so no extra row. `stop-guard.py` has no `HANDOVER` match.
- RESTARTS: none expected (a docs file; no process reads it between sessions).
