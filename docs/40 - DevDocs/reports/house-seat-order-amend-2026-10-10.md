# House seat order card amend — 2026-10-10

## §0 Headline
- Card `prompts/2026-10-10/298-house-seat-order-card.md` amended: `authorize.sh` proves the `HOUSE A: OpenAI — his <date> R<n>` line, no hand proof by the hub.
- New row S4 (`ops/desk/authorize.sh` plus `tests/ops/test_authorize.py`); S1 and S2 text now cite AUTHORIZATION (`CHECK-HUB.md:41`) as the proof.
- Decisions 2 and 3 kept; header (BASE `«FILL»`, TIP, CHECK REPORT, HOUSE B, RULINGS) untouched. Nothing built, no git write.

## DECISIONS
1. `desk-launch.sh:871-880` stays out: it reads a HOUSE line only for `overruled` (`:874`) and refuses no other HOUSE A value (`HOUSE A` not in `need`, `:1020`). The check's gate is `authorize.sh`.
2. `authorize.sh` reads EVERY column-0 `HOUSE A: OpenAI…` line of the card, not `field`'s first `HOUSE A:` line (`:78-80`): a first `HOUSE A: none — overruled …` line could otherwise hide an OpenAI line from the proof while `house-probe.sh` still probes it. A value that starts `OpenAI` but is not exactly `OpenAI — his <date> R<n>` fails. A line under `## ROWS` is proved but never probed (safe side). Test A2 pins the hidden-line case.
3. `CHECK-HUB.md:41` is not edited: it quotes the output WHOLE, so the new `HOUSE A OpenAI` rows need no new word.
4. ASK DESK: the S2a/S1 NEW texts now say AUTHORIZATION proves the line; if the desk wants line 41 to name the new rows, that is a fifth hub fragment (X4's line-count rule would still hold if the edit is in place).
5. `uv run pytest` is UNPROVEN at drafting (no `uv` on the allow list); the build hub runs it.

## RECORDS
- Working files = `HEAD` `85d2cd62` for `ops/desk/authorize.sh` (214 lines) and `tests/ops/test_authorize.py` (241 lines): `git diff HEAD --stat` → nothing; both read whole via `git show HEAD:<file>`.
- `authorize.sh` at `HEAD`: `LC_ALL=C` `:28`, `field` `:78`, `prove` `:83`, HOUSE loop `:195-207`, `if [ -z "$failed" ]` `:209`; header comment HOUSE row `:16-17`. `test_authorize.py`: `card_text` `:46`, `desk` `:55`, `recommit` `:88`, overrule test `:214-224`.
- `desk-launch.sh` read at 862-890 and by `grep HOUSE [AB]` (`:150`, `:245`, `:871`, `:1020-1025`).
- `CHECK-HUB.md:41` read (the AUTHORIZATION call). `grep -rl authorize tests/` → `test_authorize.py`, `test_deploy_step0.py`. `grep -n -E "ops/desk|tests/ops" configs/cobalt/jobs.yaml` → no match: RESTARTS class home none.
- Edits to the card (Edit tool only): WHY paragraph (four rows, pytest line adds `test_authorize.py`), S1 row and S1 NEW line 1, S2 row, S2a NEW, new row S4, NOT IN THIS JOB, READ, CHECK ASKS (X4 reworded, X5 added), RECORDS (amend entry).

HOUSE SEAT ORDER CARD AMENDED · decisions: 5
