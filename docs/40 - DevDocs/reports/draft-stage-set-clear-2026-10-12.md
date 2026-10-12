# Draft — stage-set clears its own staging (card 413, K5)

## §0 Headline
- Card `prompts/2026-10-12/413-stage-set-clear-card.md` written: row T1 (the clear, tests C1-C12), row T2 (RESTARTS RUN). BASE is the one placeholder.
- The prior check report is read from the prior card copy `<dest>/files/<card name>`, not by name: 392's is `prodwrite-seat-check-2026-10-12.md`, committed `dc8d290e`.
- The clear needs no new command: the seat types only `sh …/ops/desk/stage-set.sh` (`CHECK-HUB.md:10`), and the script already runs `rm -rf "$dest"` (`stage-set.sh:103`).
- No file is shared with card 392. 413 deploys first, then 392 is re-checked on 1012b.

## DECISIONS
1. ASK DESK: the brain's list is wider than "entries stage-set itself writes". The script writes only `diff.md`, `rulings.md` and `files/` (`stage-set.sh:108`, `:122`, `:142`, `:144-153`). `HOUSE-INSTRUCTIONS.md` is written by the hub (`CHECK-HUB.md:78`) and `house-*.md` by a house or the hub (`:93-95`). 392's leftover holds both. Default: the card takes the brain's list as named. `CHECK-REPORT.md` (`:59`) is not on it, so a dest holding one is refused. [11:29 EDT]
2. ASK DESK: one test the row does not name: the prior report must differ from the card's current `CHECK REPORT`, so a check's own staging, kept for RECOVERY, is never cleared (test C9). This only refuses more. Default: kept. [11:29 EDT]
3. ASK DESK: the refusal keeps today's text as its prefix and adds `— not cleared: <test missed>` on the same line. Default: append. [11:29 EDT]

## RECORDS
- Read at `main` HEAD `8732e0ad`, 11:29 EDT: `CARD.md`; `cto-2026-10-12.md` R1209-R1214 (`:7-12`) and R1138 (`:81`); `ops/desk/stage-set.sh` whole (168 lines); `stage-copy.sh` whole (38); `scratch-clean.sh` whole; `tests/ops/test_stage_set.py` whole (185); `CHECK-HUB.md` `:1-122`; card 389 header `:1-17` and rows C1/R1 (`:19`, `:21`); card 392 at `HEAD` and at `7aedae07~1`; `bare-guard.py:162`, `:1250-1262`; `desk-launch.sh` grep (`:888`, `:1697-1699`); `restarts.py` `:38`, `:228`, `:230-234`, `:246`.
- `ls -la` of the leftover `agy-trial/scratch/tribunal-bars-0920/prodwrite-seat-1012-check` and its `files/`: entries as the card's RECORDS lists.
- `git log` of card 392 and of `prodwrite-seat-check-2026-10-12.md` (→ `dc8d290e`).
- Not run (not on this seat's line): `git hash-object` of the prior card copy and `git --version` (for `log --find-object`). The build proves both through C1 and C8.
- `grep` with a pipe was blocked by the guard and re-sent as Glob.

DRAFTED · decisions: 3
