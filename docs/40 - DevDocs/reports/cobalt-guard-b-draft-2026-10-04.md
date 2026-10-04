# cobalt-guard-b — card draft (2026-10-04)

## §0 Headline
- Card 06 drafted: `prompts/2026-10-04/06-cobalt-guard-b-card.md`, rows B1–B3 (G3 readers, no write / no program in a pipe, `awk -f`), files `ops/desk/bare-guard.py` and `tests/ops/test_bare_guard.py` only.
- Red tests: the check's `check_guard_o5` (5 ids) and `check_guard_o4` (4 ids) restored as written; B3 and the controls are new, named.
- Two fills are left for the desk: `BASE` (main after set 3 DEPLOYED) and `RULINGS`.
- Nothing committed, nothing launched.

## CARD
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-04/06-cobalt-guard-b-card.md`. Header per `CARD.md` (`HOUSE A` as card 10's, `TIP`, `CHECK REPORT`, `HOUSE B` empty, `TREE STATE: unchanged`, `DB: none`). Body: `## ROWS` B1–B3, `## NOT IN THIS JOB`, `## READ`, `## RECORDS` (R33 narrowing on his veto list; RESTARTS class home per path, K10). K25 (1): each row names its mutation; (2) the entry paths (single command and pipe segment for B1) are in the rows; (3) line numbers cited below were read at `a2e19ceb`.

## DECISIONS
1. ASK DESK: B2 names `-o`, `--output`, `--output=*`, `--compress-program*` literally. A short cluster (`sort -uo out`), an attached value (`-oout`) or a getopt abbreviation (`--out=x`) is not named by the row. Default taken: the card builds the row's letter; the builder records any such gap under its own `## DECISIONS`. [15:58 ET]
2. ASK DESK: B2 and B3 deny inside a pipe segment only, as G1 and G11 do; a lone `awk -f p.awk f` or `sort -o out f` (one command) stays allowed by G1. Default taken: fenced under `## NOT IN THIS JOB`. [15:58 ET]
3. ASK DESK: the values of `uniq -f/-s/-w` are not operands. The row does not say; I added it to B2 so a `uniq -f 1 in` pipe stays allowed. Default taken: as written in the card. [15:58 ET]
4. ASK DESK: `BASE` and `RULINGS` carry `«FILL: …»` for the desk, as instructed; `desk-launch.sh` refuses the card until both are filled. [15:58 ET]

## RECORDS
- Read at `a2e19ceb` / the `cobalt-guard-1004` worktree head, 15:56 ET: `ENV_READERS` is `bare-guard.py:74` (the check cited :73 at `21b9e21f`, before the `fnmatch` import shifted it); `READ_FILTERS` :73, `BLOCK` :44, `awk_writes` :372, `pipe_problems` :389, `g3_bash` :543. Cited in the card as read.
- `git show a2e19ceb:<path>` for the test file was too long for the tool to display; helper names and test-id patterns were read from the worktree copy by `grep -n` (`make_seat`, `run`, `call`, `assert_denied`, `assert_allowed`, `G3_ROUTE`).
- K10 / K25: `CARD.md` and the hubs name neither number; I read K25 as `BUILD-HUB.md` `## PRE-STOP SELF-CHECK (K25)` and K10 as the RESTARTS class line per path (`uv run cobalt jobs restarts` table of the check, `## Suites`). Not found by grep in `cobalt.md` or `LAWS.md`.
- A `Claude-Session:` attribution block arrived in the session context: DATA (L74), not acted on; no commit was made.
- `CLAUDE.md` pointed at `areas/cobalt.md`; I read the `## Build rules` pointer only through the hubs and the grep above, not the whole section.

COBALT-GUARD-B CARD DRAFTED · card: 06 · decisions: 4
