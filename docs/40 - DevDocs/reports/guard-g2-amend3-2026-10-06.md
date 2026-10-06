# guard-g2 amend 3 — 2026-10-06

## §0 Headline
- Card `prompts/2026-10-06/21-guard-g2-card.md` amended for preflight 2: 3d, 4c, 4d, 4e, 4g. R1, R2, reds (a)–(f) of the brain stand.
- 3d: the build adds `"first": text` to the `seat()` dict; G2 tests `s["first"]`.
- 4c: (a), (b), (e), (f) are CONTROLS; only (c), (d), (g) are red on BASE. 4d: uncommitted prompt = REFUSAL (d2). 4e: `|`/`;` controls G2 on BASE, G1 after.
- 4g: R1 refuses a launch line already holding `PROD-READ:` without the proving row; red (g), control (g2).
- Header unchanged: `BASE: 3c257bb9`, `RULINGS: 2026-10-06 R511`, no fill token.

## CARD
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/21-guard-g2-card.md`. Edits (row G2 and `## RECORDS`, `## CHECK ASKS`):
- 3d: BUILD NOTES: `seat()` (722-744) does not return the text; dict at 744 holds `kind`, `cwd`, `wt`, `cwd wt`, `card`; `bash_rules(command, s)` (846) gets only that dict; build adds `"first": text`; G2 (856-857) tests `s["first"]`.
- 4c: label CONTROLS (a), (b), (e), (f), green on BASE; red under mutations: marker test (a), leading-shape test (b), exactly-one-flag test (f).
- 4d: red (d) is the uncommitted row only; (d2) the uncommitted prompt is a REFUSAL at `desk-launch.sh:418` (exit 1, no launch line); "prompt committed" dropped from the mutations.
- 4e: the `| cat`, `; ls`, `| sh` controls: G2 on BASE, G1 after (`BLOCK_HEAD`/`BLOCK_TAIL`); removed from the `G2_ROUTE`-on-BASE-and-after list.
- 4g: R1 refusal, red (g), control (g2), mutation "drop the `PROD-READ:` refusal", X4, RECORDS line marking the desk reading.
- `words()` cite fixed: defined `bare-guard.py:283`, used at 848.

## DECISIONS
- ASK DESK: control (e) (`;`, `| sh`, `| cat`) is denied by G1 after the build, so no mutation of this row turns it red; keep it as a G1 control, or add a G1 mutation to the build? [next desk read] Default taken: G1 control, no mutation.
- ASK DESK: the R1 refusal passes a typed marker only when it equals the stamp the launcher would append for the prompt's RULINGS row (a marker for a different row is refused); his text said only "unless the row proof passes". [next desk read] Default taken: equality required.

## RECORDS
Reads at BASE `3c257bb9`; `git -C /Users/cobalt/cobalt log --oneline 3c257bb9..HEAD -- <bare-guard.py, desk-launch.sh, test_bare_guard.py, test_desk_launch_prechecks.py, db_query.py>` printed nothing (the five files equal BASE).
- `bare-guard.py`: 5 `It never runs a command.` · 20 `G2 production (not deploy)` · 80 `READ_FILTERS` (no `sh`, no `cat`) · 106 `PROD` · 283 `def words` · 611-612 `ws[0] not in READ_FILTERS` → pipe problem · 666-694 `first_message` · 725 `text = first_message(...)` · 744 `return {"kind", "cwd", "wt", "cwd wt", "card"}` (no text) · 846 `bash_rules(command, s)` · 848 `words(x)` · 856-857 G2 · 865-867 G1 · 968 `bash_rules(command, seat(event))` (only caller of `seat()` for Bash).
- `desk-launch.sh`: 176-180 `committed` · 238-265 `ruling_row` · 418 `committed "the prompt"` · 419-423 launch line · 435 reads-this-prompt check · 457-459 RULINGS · 499 `run_launch`.
- `test_bare_guard.py`: 20-21 `BLOCK_HEAD`/`BLOCK_TAIL` · 143 `G2_ROUTE` · 189 `transcript` · 223 `make_seat` · 272-273 `assert_allowed` · 405 the deploy/unknown-seat G2 test.
- `src/cobalt/db_query.py`: 158 `requires --prod` · 211 `--side` choices · 212 `--prod`.
- Ran no test, no command beyond reads, no git write; edited the card and this report only.

GUARD G2 CARD AMENDED 3 · card: 21 · decisions: 2
