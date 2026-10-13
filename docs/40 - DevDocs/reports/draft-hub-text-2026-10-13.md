# draft-hub-text — card 523 `hub-text-1013`

## §0 Headline
- Card written: `prompts/2026-10-13/523-hub-text-card.md` (rows H1-H4, R5; BASE `ce548f10`, DB none, RESTARTS none).
- H1 D2.4 → `DEPLOY-HUB.md:57`; H2 FIXED line → one new `BUILD-HUB.md` line 112; H3 no untracked file → `BUILD-HUB.md:105`, shadow exception stated.
- H4 (UNATTENDED `:6`, `:18`) overlaps card 479 U1, U2, U4, which retire the file; default: not built.
- H3 also repairs `tests/ops/test_build_hub_no_clutter.py::test_no_other_line_changes_from_base`, which the BUILD-HUB edits turn red.
- Nothing was run; every test is UNPROVEN until the builder's E2.

## DECISIONS
- ASK DESK 1: card 479 U1 (`UNATTENDED-LAUNCH.md:4-8`, edits `:4` and `:6`), U2 (`:17-19`, edits `:18`, cuts `:19`) and U4 (retires the file to 3 lines) hold the same lines as row H4. Both agree with L61, L62, L66 on `:6` and `:18` (the new texts are 479's, byte for byte); `:13`, `:14`, `:19` and the L66 check need no edit. Build H4 or let 479 carry it? [15:14] Default: H4 not built (the card builds it only on a desk line `ROW H4: BUILD` in `## RECORDS`); if 479 merges first, H4 is void.
- ASK DESK 2: row H2's FIXED-line text goes in as a new line 112 after `BUILD-HUB.md:111`, not inside `:111`, because card 480 H6 edits `:111` and card 483 copies its `tokens:` definition. [15:14] Default: new line 112.
- ASK DESK 3: R1295 also says "deploy outside 09:30-16:00 ET". No hub names it, and `DEPLOY-HUB.md:57` (L66, his R1324, R389) says a deploy runs at any hour; the row's one rule is 21:30-22:30 ET. [15:14] Default: 09:30-16:00 not added.
- ASK DESK 4: R1295 gives only the window. Row H1 also words the refusal `FAILED PREFLIGHT: P1 — backup window` (nothing changed yet at P1). [15:14] Default: include that wording.

## RECORDS
- Read at `main` HEAD `ce548f10`, 15:14 ET; `git diff --stat HEAD` over `BUILD-HUB.md`, `DEPLOY-HUB.md`, `UNATTENDED-LAUNCH.md`, `desk-launch.sh`, `test_hub_lines.py`, `restarts.py` → nothing, so every `file:line` is HEAD's.
- Rulings: R1295 `reports/cto-2026-10-12.md:18`; R1309 `reports/cto-2026-10-13.md:140` (grep `^| R1309 `). Both are brain `DESK RECORD` rows, so the card's `RULINGS` holds only his standing `2026-10-12 R1138` (as card 446).
- Already-there proof: `grep -c -F "FIXED" BUILD-HUB.md` → 0; `grep -n -F "untracked" BUILD-HUB.md` → no hit; `grep -n -F "21:30" DEPLOY-HUB.md` → no hit. No row is pin-only.
- Shadow exception: `desk-launch.sh:199`, `:1626-1628`. Restart class: `restarts.py:225-228` (`docs/` → DOCS), `:245-246` (`tests/`).
- Rules-cut cards 478-485, line ranges in these hubs: 480 H6 `BUILD-HUB.md:17`, `:111`; 480 H8 `DEPLOY-HUB.md:32`, `:58`; 483 copies `BUILD-HUB.md:111`; 479 U1-U4 `UNATTENDED-LAUNCH.md:4-8`, `:17-19`, `:22`, `:25-30`, whole file retired; 478, 481, 482, 484, 485: none. Overlap: H4 with 479 (ASK DESK 1) only; H1 (`:57`) and H2 (line 112) sit beside 480's lines, no shared byte.
- Pin found red by the card's edits: `tests/ops/test_build_hub_no_clutter.py:57-60` (BASE `5e5fab02`; `git diff --stat 5e5fab02 HEAD` → 2 insertions, the no-clutter pair). Repaired in row H3 (3).
- Law lines read: LAWS `### L61` (`:316`), `### L62` (`:319`), `### L66` (`:335`).

DRAFTED · decisions: 4
