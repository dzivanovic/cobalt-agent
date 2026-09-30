# CARD — the job card (FIXED FORMAT · INSTALLED 2026-09-30 · R60)

One format for every kind (`build`, `check`, `deploy`). A card holds the job's VALUES and nothing else: the fixed file of its kind (`BUILD-HUB.md`, `CHECK-HUB.md`, `DEPLOY-HUB.md`) holds the launch line, the procedure, the authorization steps and the stop line. A card carries no launch line, no procedure, no authorization block and no read of a words file.

WHERE: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/<date>/<nn>-<job>-card.md`, committed on `main` before the launch. ONE card per job: the build launches on it; the desk then fills `TIP`, `CHECK REPORT` and `HOUSE B`, commits, and the check launches on the same file (its second pass, `PASS-2`, too). A deploy has its own card. A relaunch, a `CONTINUE` and a second pass need no card edit: the hub proves only that the card is committed and unchanged; the desk still writes its own §4 row for every launch (L34).

WHO FILLS IT: the desk (or a drafter it launches). A card that builds a check's `held unfixed` finding is written from that check report: each of its rows is a FIX row backed by the `## RUNS` row that is `HELD`. A value not yet known is written `«FILL: <what>»`; `desk-launch.sh` refuses a card that still holds one in a field its kind needs, and every hub's first gate greps for it.

## THE HEADER — one `KEY: value` per line, from column 0, plain text (no backtick, no bold); read by `desk-launch.sh` and by the hub

| key | build | check | deploy | value |
|---|---|---|---|---|
| `JOB` | required | required | required | short name, `[a-z0-9-]` only. The session is named `<JOB>-build`, `<JOB>-check` or `deploy-hub-<JOB>` |
| `LADDER` | required | required | required | the ladder line (`S3-P2 · F22`) or `OFF-LADDER — <report> <date> R<n>` |
| `BRANCH` | required | required | required | build / check: the job's branch. deploy: the gate branch |
| `WORKTREE` | required | required | required | ONE directory name under `/Users/cobalt/cobalt-wt/` (`[A-Za-z0-9._-]`, no `/`). build: where the builder works. check: the build's worktree (read only). deploy: the gate worktree |
| `BASE` | required | required | `main` | build / check: the 8-hex commit the branch stood at before this job's first commit. deploy: the literal `main` (the hub records the cut itself) |
| `TIP` | empty | required | required | check: the 8-hex code tip the suites ran on. deploy: every branch HEAD the gate merges (8-hex, space-separated, in merge order); `## SHIPS` gives each head's code tip |
| `REPORT` | required | required | required | build / check: the BUILD report, absolute path inside the worktree. deploy: `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-<…>.md` |
| `CHECK REPORT` | empty | required | — | absolute path under `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/` |
| `HOUSE B` | empty | required | — | `as needed`, or `mandatory — vault notes` / `mandatory — sizing` for a build that writes his vault notes or changes sizing (his 2026-09-30 R38): the check then runs its second pass even when nothing is open. His per-case overrule of the wait is appended: ` · overruled <date> R<n>` |
| `TREE STATE` | required | required | — | `unchanged`, or `row <id>` when the build adds a with-DB test or a migration: that row of `## ROWS` edits the pass-1 / pass-2 commands, the allowed-skip list and the level in `docs/40 - DevDocs/prompts/BUILD-HUB.md` and `DEPLOY-HUB.md`, and names both files in its `files` |
| `RULINGS` | required | required | required | his rulings that bind the job: `<date> R<n>`, comma-separated (`2026-09-30 R3, 2026-09-30 R9`). Row numbers only; never his words. deploy: `none` when no held defect is carried and he has not overruled the window for this one deploy (L73; the deploy's approval is the standing rule, `DEPLOY-HUB.md` `## AUTHORIZATION`) |
| `TAG` | — | — | required | the deploy tag; the rollback tag is `pre-<JOB>` |
| `MIGRATIONS` | — | — | required | `none`, or the numbers in `FORWARD` order, then ` · production at <level> · creates: <objects> · old code on the new schema: <why a code revert alone is safe>` |
| `SET` | — | — | required | one word naming the set in the stop line |

## THE BODY — sections in this order; a section with nothing to say is left out

A HEADING IS A BARE LINE: `## <name>` from column 0, no backtick, no bold, nothing after the name (`desk-launch.sh` greps `^## <name>`; a backticked heading reads as a missing section and the launch is refused). The names below are backticked only because they are named here; the examples print them as they go in a card.

`## ROWS` (build, check) — the work, in order, nothing else:

| row | what | red first | files |
|---|---|---|---|
| `<id>` | the rule the row builds, with the `file:line` and the report row that backs it (a fix row is backed by a check `## RUNS` row that is `HELD`) | the test that fails on `BASE` for this row's reason, named, with the assertion it fails on. A row that only runs something (L70) says `RUN — asserts nothing` and names the command's output to quote | every file the row may touch |

`## SHIPS` (deploy) — one row per branch of the set:

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|

The code tip is the `tip:` of the check's stop line (a fresh Opus pass may have moved it past the build's). The last column is `held unfixed: 0` and `ready: YES` for a check run on `CHECK-HUB.md`; a report of the old shape keeps its own literals.

`## NOT IN THIS JOB` — the fence: what the job must not build, touch or re-decide (seams settled elsewhere, rulings that stand, files out of bounds). One line each.

`## READ` — the job's own reading, by path and section or by symbol: the design section, the report rows behind a fix row, the code symbols. The fixed file already names the laws and the rules; never repeat them here.

`## CHECK ASKS` (check; optional) — questions beyond the rows, one line each, numbered X1, X2 …; the fixed HOUSE TEXT carries them to the houses verbatim.

`## RECORDS` (optional) — facts the desk read at launch that the hub copies into its report and re-reads where it can (a listing, the answer to a `## DECISIONS` item, an item carried as OUT OF SCOPE with its owed row). Each with its command and time.

`## MARKERS` (deploy) — reads that prove production does NOT carry the set before and DOES after. One line each: `<command>` · before `<value>` · after `<value>`. Commands: `ls <absolute path under /Users/cobalt/cobalt>` or `grep -c -F "<fixed string>" <absolute path>` only.

`## READ-BACK` (deploy; only when `MIGRATIONS` is not `none`) — ONE `COBALT_ENV=production uv run cobalt db query --side user --prod "<SQL>"`, typed whole, reading `pg_catalog` (L35), with its BEFORE and AFTER answers. No `%` anywhere in it.

`## SMOKE READS` (deploy) — the set's own reads after the merge, one line each: label · the command typed whole · what a green answer looks like. A line marked `census` is a count read before the outage (D1) and again after it, recorded, never a gate. A production `db query` read carries no `%` and is listed only when `MIGRATIONS` is not `none` (a deploy with no migration has no production `db query` string on its line).

## WHAT A CARD NEVER HOLDS
- A launch line, an allow string, a `--add-dir`, a model or a permission mode: the fixed file's.
- A step, an order of steps, a suite command, a lock rule, a recovery rule, a report section list, a stop-line shape: the fixed file's.
- An authorization block or a gate literal: the fixed file proves `RULINGS` by row number and commit (K23), and the card itself by its commit.
- The row of a launch: the desk's §4 row (L34) is the desk's record; no card field names it and no hub greps it (his 2026-09-30 R38).
- His words. A read of `cto-<date>-words.md`.
- A count the hub must reach ("expected 3320 passed"): the gate is `0 failed`, `0 errors`; a count is what the hub reports.
- State of the desk (a meter that is out, a tab id, a watch id).

## EXAMPLE 1 — the E1 fix, at its BUILD launch (values of `prompts/2026-09-30/47-e1-fix-build.md`)

```
JOB: e1-fix
LADDER: S3-P2 · F22
BRANCH: s3/e1-fix-0930
WORKTREE: e1-fix-0930
BASE: d37e8bc0
TIP:
REPORT: /Users/cobalt/cobalt-wt/e1-fix-0930/docs/40 - DevDocs/reports/e1-fix-build-2026-09-30.md
CHECK REPORT:
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-09-30 R3, 2026-09-30 R9
```

## ROWS

| row | what | red first | files |
|---|---|---|---|
| A1 | RUN — asserts nothing. Can any value `_render_value` renders carry an indented `#` line (a block scalar, a list item's text)? `grep -n` every caller of `_render_value` and every shape it produces; quote the output. If one can, row E1's fix keeps only the lines that are not the old value's own, or the input goes under `## DECISIONS` as `DECISION A1` | — (tool output quoted in the report) | none (read only) |
| E1 | `_merge_frontmatter_lines` keeps an indented `#` comment he typed under a Cobalt-replaced or filled entry. Today `src/cobalt/prefill/trade_note.py` line ~345 keeps only a blank line or a column-0 `#`; the helper's docstring (~302–303) and L28 say his comment is kept. Backed by `reports/s3-exits-c4-fix-r2-check-2026-09-29.md` lines 93 and 117 (HOLDS). The check's fix: `line.lstrip().startswith("#")` for `line.startswith("#")` | ONE new test in the file that already pins the helper: a note whose replaced entry has `  # typed at close` and a blank line under it; asserts the comment and the blank survive and the entry's value is replaced. RED on `BASE`: the comment line is missing from the written block | `src/cobalt/prefill/trade_note.py` (the one line; the docstring if it misstates the rule), `tests/cobalt/test_s3_c4_trade_note_offline.py` |

## NOT IN THIS JOB
- Any `src/` file but `src/cobalt/prefill/trade_note.py`; anything under `src/cobalt/vaultwrite/` or `src/cobalt/db_migrations/`.
- X3 (human wins once, the vault writer's merge baseline): owed as its own item (2026-09-29 R104).
- A red outside this fix: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/s3-exits-c4-fix-r2-check-2026-09-29.md` lines 90–120.
- `src/cobalt/prefill/trade_note.py` lines 289–350: `_merge_frontmatter_lines`, `_render_value`, `upsert_trade_note`.

## RECORDS
- Both deploys of the day are live; E1 is live (the desk, 2026-09-30 R30).

## EXAMPLE 2 — the same card at its CHECK launch (values of `prompts/2026-09-30/50-e1-fix-check.md`)

The header lines that changed; `## ROWS`, `## NOT IN THIS JOB` and `## READ` stand as in example 1.

```
JOB: e1-fix
LADDER: S3-P2 · F22
BRANCH: s3/e1-fix-0930
WORKTREE: e1-fix-0930
BASE: d37e8bc0
TIP: 5c92b589
REPORT: /Users/cobalt/cobalt-wt/e1-fix-0930/docs/40 - DevDocs/reports/e1-fix-build-2026-09-30.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/e1-fix-check-2026-09-30.md
HOUSE B: mandatory — vault notes
TREE STATE: unchanged
RULINGS: 2026-09-30 R3, 2026-09-30 R9
```

## CHECK ASKS
- X1 Is the one-line change what the round-3 check asked for (`s3-exits-c4-fix-r2-check-2026-09-29.md` lines 93 and 117), and is it the only `src/` line changed?
- X2 Re-derive row A1 from the code, not from the report: the inputs of `fresh` and of `his_fills`. If a rendered value can carry an indented `#` line, name the input.
- X3 The KEEP record below: is any of his text deleted anywhere else in `_merge_frontmatter_lines` (a column-0 comment, a blank line, an extra key, a list shape, a line before the first entry)?
- X4 Does any caller or test depend on the old drop of an indented `#` line?
- X5 The vault writer's "human wins once" is out of scope (2026-09-29 R104). Write no finding that rests on it alone.

## RECORDS
- The build's report commit `8953224c` sits on the tip; `git -C /Users/cobalt/cobalt diff --stat 5c92b589 8953224c -- . ":(exclude)docs"` prints nothing (the desk, 10:40 ET).
- The build's `## DECISIONS` item 1 was answered KEEP: a `#` line of a multi-line value he retyped stays under the refreshed entry as a comment; none of his text is deleted (2026-09-30 R32).

## A DEPLOY CARD, IN SHORT (the values `DEPLOY-HUB.md` reads; no example is filled here)
Header: `JOB`, `LADDER`, `BRANCH` (gate branch), `WORKTREE` (gate worktree), `BASE: main`, `TIP` (the code tips), `REPORT`, `RULINGS`, `TAG`, `MIGRATIONS`, `SET`. Body: `## SHIPS`, `## MARKERS`, `## READ-BACK` (with a migration), `## SMOKE READS`, `## RECORDS` (facts the hub copies into its report's `## RECORDS`).
