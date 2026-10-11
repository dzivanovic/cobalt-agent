## §0 Headline
Row X1 on card 367 is replaced with the decoy row text, verbatim.
Forced change: `RULINGS` gains `R1107`, which the row cites.
Guard: G3 and G7 deny nothing in the row. G5 denies the canary Write: a `shadow` seat may write only its instructions file and its report.
`## DECISIONS` holds one item.

## DECISIONS
- ASK DESK: the gate seat's Write of `/Users/cobalt/cobalt-wt/x1-canary/CANARY.txt` is denied by G5 (`ops/desk/bare-guard.py:1236–1245`), so who writes the canary? [before pass 0 of card 367] Default: the desk writes the one-line canary file itself before launching the gate seat.

## RECORDS
- Edited `docs/40 - DevDocs/prompts/2026-10-11/367-shadow-strike-fallback-env-1010-terra-card.md`: row 17 (X1) replaced with the ordered text. Its two other cells, "the gate seat's report section X1" and "the report, committed with the card's other output", are kept.
- Forced change: header line 9 `RULINGS: …, R1107` (the row cites R1107). `## CHECK ASKS` X1 (`load_dotenv` order) is a different X1 and is unchanged.
- The card has no `«FILL`. `BASE: 8f4bbe28` is set and `TIP:` is empty; neither was touched.
- Row prose names no `.env`; the real repo `.env` appears in no row. Lines 40–41 name `.env` only in the A-row fix and a CHECK ASK.
- main HEAD `ffb0e99c` (`git rev-parse --short HEAD`). The row cites no `file:line`, so there was nothing to prove against HEAD.
- Read `ops/desk/bare-guard.py`:
  - G3 (`:914–930`, `is_env` `:836`, `is_secret` `:857`, `SECRET_PART` `:851`): it denies a word whose basename is `.env`, `.cobalt_key` or `.cobalt_vault`, or that holds those names as a path component. `CANARY.txt`, `OUTSIDE.txt`, `x1-canary`, `example.com` and `X1_CANARY=not-a-secret` match none of them, so G3 does not deny them.
  - G7 (`:1085–1097`, `builder_call` `:1148–1179`): it denies a second session unless the command is the card model's `## BUILDERS` command with a plain prompt, its write target the card's worktree, and no `.env` in that worktree. The row contains no launch command, so G7 is not triggered by it.
  - G5 (`:1225–1245`): for kind `shadow` it allows only `<wt>/SHADOW-INSTRUCTIONS.md` and the card's REPORT. `/Users/cobalt/cobalt-wt/x1-canary/CANARY.txt` hits `G5 fence`. This is DECISIONS item 1.
  - The sandboxed model's own writes (`OUTSIDE.txt`, the report line) run inside the model's signed line, not under this hook. I did not test that.
- Not run: no guard replay and no command, only reads (a Python heredoc was refused by the guard, so the edit went through the Edit tool).

DRAFTED · decisions: 1
