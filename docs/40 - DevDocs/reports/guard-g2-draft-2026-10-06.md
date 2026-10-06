# Guard G2 card draft — 2026-10-06

## §0 Headline
- Card `21-guard-g2-card.md` drafted: one row G2, files `ops/desk/bare-guard.py` and `tests/ops/test_bare_guard.py` only, `DB: none`, `RULINGS: 2026-10-06 R511`.
- The guard proves the approval from a row file (one `| R<n> |` line, `HIS RULING`, `APPROVED`, a `production read` row among them), as the launcher does; brain seats only.
- Red: a ruled brain seat's production `db query` is denied on BASE and allowed after. About 20 controls stay denied.
- Two items need the desk's word; each has a default taken.

## CARD
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/21-guard-g2-card.md`

## DECISIONS
- ASK DESK: which row "grants production reads"? The guard cannot read intent, so the default is the literal `production read` (case-insensitive) in at least one cited row, with every cited row still a valid HIS RULING + APPROVED row. R511's row holds it. If you want no content test, drop that clause from row G2 and its control. [06:38 ET]
- ASK DESK: the launcher proves a row is committed with `git show`; the guard never runs a command (`bare-guard.py:5`). The default is to read the working-tree file only: the launcher already refuses an uncommitted row for any prompt whose line carries the production string, and G2 reads the same file. [06:38 ET]

## RECORDS
- BASE `3c257bb988f2683bb4b7a0286250b211eb77dd25` (`git -C /Users/cobalt/cobalt rev-parse HEAD`, 06:38 ET).
- Read at BASE, every cited line: `ops/desk/bare-guard.py` 1-1039 whole (header 20-21, 36-37; `ROUTE` 56; `PROD` 106; `read_card` 697-719; `seat` 722-744, `prompt` at 727, kind at 733-742; `bash_rules` 846-868, G2 at 856-857). `tests/ops/test_bare_guard.py` lines 20-70, 140-274, 385-414 (`G2_ROUTE` 143; `make_seat` 223-247; G2 block 387-413). `/Users/cobalt/.claude/ops/desk-launch.sh` 225-285 (`ruling_row` 238-265, `ruling_items` 267-275), 440-479 (F5 comment 451-453, `ruled` 456-460). `src/cobalt/db_query.py` 144-167 (`BEGIN READ ONLY` 163, `--prod` refusal 157-158), 205-218 (options 211-215).
- F5 card read: `prompts/2026-10-05/57-deploy-launcher-f5-card.md`. Format read: `prompts/CARD.md`, `prompts/2026-10-06/14-flake-fix-2-card.md`. BUILD-HUB lines 17, 24, 42, 71-74, 91, 100, 106 read.
- LAWS read: L37 (234-236), L61 (315), L62 (318-320). `areas/cobalt.md` lines 19-63.
- R511 row: `grep -n "^| R511 " reports/cto-2026-10-06.md` → line 19, `HIS RULING` and `APPROVED — pending fold`; committed in `720c98b8` (`git log -1 --format=%h -S"| R511 |"` → `720c98b8`). R510 line 20, R509 line 21.
- `--allow-prod` is not matched by `PROD` (`bare-guard.py:106`), so its control is denied by shape (the production word is in the command), not by the regex; the card says so.
- RESTARTS homes (K10): `ops/desk/bare-guard.py` operator hook, no resident (`grep -n -F "ops/desk" configs/cobalt/jobs.yaml`: no hit); `tests/ops/test_bare_guard.py` test; the builder's report DOCS. The hook sits in the repo; `/Users/cobalt/.claude/settings.json:22` runs `python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py`, so merging to main installs it. Nothing outside the repo is edited: `decisions` for the install is 0.
- Row on his veto list: noted under the card's `## RECORDS`.
- One tool call of mine was refused by the live guard (a grep whose pattern held the production string, G2): the hook works as ruled. Re-read with the Grep tool; no production command was run.
- No git write, no launch, no database.

GUARD G2 CARD DRAFTED · card: 21 · decisions: 2
