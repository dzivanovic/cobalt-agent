# ops-hand install card — draft, 2026-10-10

## §0 Headline
Card `prompts/2026-10-10/306-ops-hand-install-card.md` written: three rows, BASE `936c9b1e`, `DB: none`, `RULINGS: 2026-10-10 R969`.
I1 replaces `«INSTALL: his row»` in `OPS-HAND.md` line 1 with `HIS RULING · APPROVED 2026-10-10 R969`; H4 (`desk-launch.sh:633-634`) refuses only while `«INSTALL` is present, so the string passes.
I2 appends a 13-line `## 8.` to `STANDING-LIST.md` (the launch line's 4 allow, 17 deny, mode `default`).
I3 renames two tests that pin the token (`test_desk_launch_ops_hand.py:296-315`); they go red with I1.
Two decisions for the desk, below. Not run: `uv run pytest`, `uv run cobalt jobs restarts` (no `uv` on this seat).

## DECISIONS
1. Title form. Your prompt gave `HIS RULING · APPROVED 2026-10-10 R969`; I used it. The hubs' `authorize.sh` reads titles of the form `INSTALL: <date> R<n>` (`authorize.sh:173-183`), but it names no `OPS-HAND` and H4 reads only the token, so the prompt's form is accepted. If the desk wants the hub form for uniformity, change I1's NEW line to `… INSTALL: 2026-10-10 R969`; H4 passes either (it has no `«`).
2. Scope beyond docs. The prompt says docs-only. Two tests of `tests/ops/test_desk_launch_ops_hand.py` (`:296-300`, `:303-315`) assert the real file still carries the token and would fail the build's suite, so row I3 edits that one test file. `DB: none` still holds (`tests/ops/`). Alternative: drop I3 and leave the suite red; I do not recommend it.

## RECORDS
- Read 2026-10-10 against `HEAD` `936c9b1e`: `git diff HEAD --stat` over `OPS-HAND.md`, `STANDING-LIST.md`, `desk-launch.sh`, `test_desk_launch_ops_hand.py`, `test_desk_launch_brain.py`, `cto-2026-10-10.md`, `CARD.md` → nothing (working files = `HEAD`). `git show HEAD:` of `OPS-HAND.md` whole and of `cto-2026-10-10.md` (R969 row present).
- `wc -l`: `OPS-HAND.md` 22, `STANDING-LIST.md` 220, `CARD.md` 139. `«INSTALL` count in `OPS-HAND.md`: 1 (line 1).
- Files read whole: `prompts/OPS-HAND.md`, `prompts/STANDING-LIST.md`, `prompts/CARD.md`, `2026-10-10/298-house-seat-order-card.md` (precedent), `2026-10-10/305-…md`. Read in part: `desk-launch.sh` 600-722, `test_desk_launch_ops_hand.py` 1-40 and 280-320, `test_desk_launch_brain.py` 485-502, `284-kill-hub-card.md` 1-30, `cto-2026-10-10-words.md` 12-14. Grep: `«INSTALL` over `ops/` and `prompts/`; `STANDING-LIST|OPS-HAND` over `tests/` and `bare-guard.py`; `INSTAL|OPS-HAND` in `authorize.sh` (no `OPS-HAND` match); `R969` in the day report (line 8, `HIS RULING · APPROVED`) and the words file (line 12).
- Interaction with card `284` (K3 adds one line to `STANDING-LIST.md` after `:148`): different lines; I2 states its count as "13 more lines", not an absolute total.
- No file written but the card and this report; no git write, no launch.

OPS HAND INSTALL CARD DRAFTED · decisions: 2
