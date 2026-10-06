# guard-g2 card amend — 2026-10-06

## §0 Headline
- Card 21 amended: one row G2, the brain's R1 (`desk-launch.sh` appends the marker) and R2 (guard passes only a marked seat's leading db query), byte for byte.
- Files: `ops/desk/desk-launch.sh`, `ops/desk/bare-guard.py`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_bare_guard.py`. 3b, 3c, 4d fixed; header values kept.
- R2 as written never lets the query run: it refuses `--prod`, and `db_query.py:157-158` refuses production without it. Decision 1.

## CARD
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/21-guard-g2-card.md`

## DECISIONS
- ASK DESK: R2 allows no production string but the leading `COBALT_ENV=production uv run cobalt db query `, so `--prod` (matched by `PROD`, `bare-guard.py:106`) is refused; the query needs it (`db_query.py:157-158` raises `requires --prod`; `env.py` maps `production` to `cobalt_brain`). The default taken: the rules stay byte for byte; red (c) is the command without `--prod`; `--prod` is a control (denied). Allowing `--prod` for a marked seat needs the brain's word. [now]
- ASK DESK: R2 says "the read sides the prompt names"; the guard reads no prompt. The default taken: `--side` accepts `user` and `system` (`db_query.py:211`), anything else refused. [now]
- ASK DESK: the pipe and `;` controls: the card asks the builder to state whether G2 or G1 denies them today, not to pin one. [now]

## RECORDS
- BASE `3c257bb9`; HEAD at amend `55def42e`; `git diff --stat 3c257bb9 --` on `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_brain.py`, `tests/ops/test_desk_launch_prechecks.py` printed nothing, so each read below is BASE.
- Read `bare-guard.py`: 5 (never runs a command); 1-40 (header: G2 entry is line 20; 36-37 the `COBALT_WT_ROOT` comment); 106 `PROD`; 666-694 `first_message` (first non-meta `user` record, `if k > 500` break at 672); 697-744 `read_card`, `seat` (`first_message` called at 725, return dict 744); 846-868 `bash_rules` (G2 at 856-857).
- Read `desk-launch.sh`: 160-180 (`REPO`, `refuse`, `committed` 176-180); 209-227 (`run_launch`, `eval "$2"` at 223); 230-275 (`ruling_row` 238-265, `ruling_items` 267-275); 404-500 (prompt kind: `committed` 418, `line` 421-422, launch string check 435, RULINGS read 457-459, `run_launch` 499).
- Read `tests/ops/test_bare_guard.py`: 185-279 (`transcript` 189, `make_seat` 223, `call` 250, `run` 263, `assert_*` 267-274); 384-414 (G2 block 387-413, `G2_ROUTE` 143 by the card's read at BASE).
- Read `tests/ops/test_desk_launch_prechecks.py`: 770-802 (`survey_prompt` 775, `launch_prompt` 787, F5 tests 792+); grep found 22 RULINGS/prompt hits. Other `desk-launch` tests (`test_desk_launch_brain.py`, `_devfix.py`, `_recut.py`) not changed by the row.
- Read `src/cobalt/db_query.py` 143-168, 205-217 (157-158 `requires --prod`, 163 `BEGIN READ ONLY`, 211 `--side` choices, 212 `--prod`); `src/cobalt/env.py` grep (production → `cobalt_brain`).
- 3b: the header entry is `bare-guard.py:20` only; fixed in the card. 3c: `grep -n "^| R511 " reports/cto-2026-10-06.md` prints line 22 now; the card cites the command, no number. R508 (`| R508 |`, `HIS RULING`, `APPROVED`, names production reads) read.
- 4d: the card's proof is now the marker in the transcript's first user record, written only by `desk-launch.sh` from a committed row and prompt; the working tree is never read.
- K10 install: `ls -la /Users/cobalt/.claude/ops/desk-launch.sh` → symlink `-> /Users/cobalt/cobalt/ops/desk/desk-launch.sh`; `bare-guard.py` runs from the repo via `/Users/cobalt/.claude/settings.json:22`. No copy.
- Edited only the card and this report. No git write, no launch, no database, no production command.

GUARD G2 CARD AMENDED · card: 21 · decisions: 3
