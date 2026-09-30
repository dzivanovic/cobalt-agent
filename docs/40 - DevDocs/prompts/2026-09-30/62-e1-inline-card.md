JOB: e1-inline
LADDER: S3-P2 · F22
BRANCH: s3/e1-inline-0930
WORKTREE: e1-inline-0930
BASE: 1a8827e0
TIP:
REPORT: /Users/cobalt/cobalt-wt/e1-inline-0930/docs/40 - DevDocs/reports/e1-inline-build-2026-09-30.md
CHECK REPORT:
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-09-30 R74

## ROWS

| row | what | red first | files |
|---|---|---|---|
| A1 | RUN — asserts nothing. `_merge_frontmatter_lines` (`src/cobalt/prefill/trade_note.py:~308-350`) replaces a Cobalt-owned or filled entry's own line with `_render_value(...)` (line ~346: `out.extend([rendered, *tail])`), so an inline comment he typed on that same line (`status: open  # mine`) is dropped, although the docstring (~302-303) and L28 say his comment is kept. `grep -n` every caller of `_render_value` and quote the output; say whether `_render_value` can return one line or several for any key, and whether a value a user can type can contain ` #` inside quotes | RUN — asserts nothing; quote the grep output and the answer | none (read only) |
| E1 | Keep the trailing inline comment of the replaced entry's FIRST line: after the new value, append his ` #…` text (spacing as he typed it) when the rendered value is a single line and the ` #` is outside quotes in his original line. When the rendered value is several lines, or the ` #` position cannot be told from a quoted one, do NOT guess: keep the current behaviour and write the case under `## DECISIONS` as `DECISION E1` with the input | ONE new test in `tests/cobalt/test_s3_c4_trade_note_offline.py`, beside the E1 (indented comment) test: a note with `key: old  # typed by him` where the key is Cobalt-owned; asserts the written line is the new value followed by `  # typed by him`. RED on `BASE`: the written line has no comment. A second assertion, same test or its own: a value with `#` inside quotes keeps its whole quoted text and gains no comment | `src/cobalt/prefill/trade_note.py` (the merge helper only; the docstring if it misstates the rule), `tests/cobalt/test_s3_c4_trade_note_offline.py` |

## NOT IN THIS JOB
- Any `src/` file but `src/cobalt/prefill/trade_note.py`; anything under `src/cobalt/vaultwrite/` or `src/cobalt/db_migrations/`.
- The indented-comment and blank-line rule (E1, live; `5c92b589`); X3 (human wins once) stays owed (2026-09-29 R104).
- F15 P1 (branch `f15/p1-records`, worktree `f15-p1-0930`) and every file it touches (`cards/store.py`, `radar/evaluate.py`, `aset/web.py`, `db_migrations/`, `cards/scoring.py`): this job touches none.
- A red outside this fix: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here.

## READ
- `src/cobalt/prefill/trade_note.py` lines 289-350: `_merge_frontmatter_lines`, `_render_value`.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/e1-fix-check-2026-09-30.md` (the E1 check; the owed item is its follow-up).
- `tests/cobalt/test_s3_c4_trade_note_offline.py`: the E1 test and its fixtures.

## RECORDS
- The owed item: "an inline comment on a replaced entry's own line is lost (`trade_note.py:346`)", recorded by the desk at the E1 deploy (`reports/cto-2026-09-30.md` §5 OWED, 17:08 ET). The job is offline: no database, no migration, no lock (L76); it runs beside the F15 P1 build.
