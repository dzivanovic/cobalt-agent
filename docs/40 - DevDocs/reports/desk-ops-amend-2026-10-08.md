# desk-ops-amend — report 2026-10-08

## §0 Headline
- Card `106-desk-ops-fixes-card.md` amended in place: rows G1-G5, G6 removed with every reference.
- G4 is unblocked (D1 = A): the timer sources `~/.cobalt_key` in a subshell and sends via `send_dm`.
- G1, G2, G3, G5 rows untouched. `BASE` is still the only fill token.
- Card 13954 → 13269 bytes. Not committed.

## CHANGES
- Header: `RULINGS` gains `2026-10-08 R660`.
- `WHY`: "Rows G1-G6" → "Rows G1-G5". The `HELD:` paragraph is removed.
- G4: "HELD on D1" → "(D1 = A, his 10-08 R660)"; "Under D1 option A:" dropped. Files and tests unchanged.
- G6 row removed.
- Deploy gate: the `test_day_open_desk_step.py` clause is removed.
- `NOT IN THIS JOB`: the `src/` line names the day-open desk check as its own card. `READ`: the `DAY-OPEN-QWEN.md` line is removed.
- `RECORDS`: one line on how the key stays out of logs and arguments (L4).

## DECISIONS
- C7 (G4, D1 = A): G4 stays on this card; the one new command is approved.
- C8 (D2 = B): the day-open desk check leaves this card. D3 stands.

## RECORDS
- Read: the card (whole), `reports/desk-ops-fixes-draft-2026-10-08.md` (whole), `Memory/topics/writing-rules.md`.
- `ops/run_backup.sh:26-32`: `KEY_FILE="$HOME/.cobalt_key"`, `source "$KEY_FILE"` (checked at main HEAD `c364bc43`).
- `ops/desk/close-timer.sh:42-45`: `refuse()` prints the line and `exit 1`.
- `~/.cobalt_key`: `grep -c '^export COBALT_MASTER_KEY='` → 1. The count only; the value was never read or printed.
- Key path (L4): the subshell environment and its `uv` child hold it. Argv carries only the REFUSED line. Nothing echoes it. The test stubs `COBALT_NOTIFY`.
- Final grep of the card for `G6|D2|HELD|DAY-OPEN`: no hit except the `D2 = B` ruling in C8. `«FILL` appears once (BASE).
- `wc -c`: before 13954 (draft report), after 13269 (after the C8 reword, a few bytes more).

DESK OPS CARD AMENDED · decisions: 2
