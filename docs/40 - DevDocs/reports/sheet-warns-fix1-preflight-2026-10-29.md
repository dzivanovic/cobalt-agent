# Preflight — card 1082 fix row S1 — 2026-10-29

Read: the card (whole), the drafter report, the check report (O1 lines), `BUILD-HUB.md:14,16`, LAWS L75/L76. Refs: BASE `78a6ab4a`, header TIP `01107570`, branch `ops/sheet-check-warns` = `d57714468` (rev-parse).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git show 49f60a963 -U0 -- <card>` | exactly one added line (`+| S1 | …`), after D1 and before R1; four columns like the other rows (what · red first · files); `files` = `scripts/smoke_s1.sh` | OK |
| 2a | `git show 01107570:scripts/smoke_s1.sh`, `grep -n` on the worktree | `:101` check line + needle `reload half.htk`; `:103` import and `:106` call of `assert_sheet_matches`; `:102-108` is the step; selector step `:109-112`; grade steps `:80-100` (card says `:80-98`) | OK (NOTE 3) |
| 2b | `git grep -n -E "assert_sheet_matches\|def sheet_warning\|reload half.htk" 01107570 -- src scripts tests ops` | `assert_sheet_matches` only in `smoke_s1.sh:103,106`; `match.py:84 def sheet_warning`; no `src/` or `tests/` use of the old name | OK |
| 2c | `git show d57714468:src/cobalt/daymode/match.py`, `grep -n "return None"` | `sheet_warning` `:84-117`, `assert_grade_allowed` `:120`; the full-on-reduced string holds `reload half.htk or overrule` (`:35` in the docstring, built at `:111-114`) | OK |
| 2d | `git diff 01107570 d57714468 --stat` | no change to `scripts/smoke_s1.sh` or `match.py` between the two refs (only tests and the build report) | OK |
| 3a | `BUILD-HUB.md:14` allow list vs the row's `uv run python -c` (old and new snippet) | `uv run python` is not on the list, and `BUILD-HUB.md:16` says "Never typed: `uv run python`". Under `dontAsk` the call is denied | FAIL |
| 3b | the row's `bash -n scripts/smoke_s1.sh` | not on the list (`bash`/`sh -n` absent; only `sh /Users/cobalt/cobalt/ops/desk/*`) | FAIL |
| 3c | the row's `grep -n -F "assert_sheet_matches" scripts/smoke_s1.sh`; no `git mv/rm`, `rm`, `mv`, `revert`, `cherry-pick` in the row | `grep *` is allowed; none of the banned verbs appear | OK |
| 4 | row's `files` column and text | only `scripts/smoke_s1.sh`; the row names no allow-line or guard change | OK |
| 5 | `git grep -n -E "smoke_s1\|_smoke_cards" d57714468 -- tests ops` | no output | OK |
| 6.1 | ASK DESK 1: `ORDER:` after D1, no DEPLOY PROOF line | `ORDER:` (card line 30) does not name `S1` yet; a script is not a deployed module, so no marker line | OK, but the card needs `S1` in `ORDER:` |
| 6.2 | ASK DESK 2: builder runs the two snippets under the lock, else `UNPROVEN (L70)` | the lock scripts are allowed (`sh …/ops/desk/*`) but the snippets cannot be run (3a), so the default always lands on `UNPROVEN` | FAIL |
| 6.3 | ASK DESK 3: RESTARTS stays; R1's table is the record | the header is the drafter's reading and R1 re-derives it; the row does not touch it | OK |
| 7 | `git show 49f60a963 -U0` on the card | diff is the one S1 line; `BASE`, `TIP`, `CHECK REPORT`, `HOUSE B`, `RULINGS` untouched | OK |

## ISSUES
- FAIL 3a/6.2: the row's RED (old snippet) and GREEN (new snippet) runs are `uv run python -c`, which the BUILD line does not allow (`BUILD-HUB.md:16` says it is never typed). The builder cannot produce either run. Fix on the card: drop the two snippet runs from "red first"; keep as proof `grep -n -F "assert_sheet_matches" scripts/smoke_s1.sh` printing nothing (exit 1) and `grep -n -F "sheet_warning" scripts/smoke_s1.sh` printing the import and call lines. State that the step's string is already pinned by T1 (a) (`tests/cobalt/test_daymode.py` returns the `reload half.htk` text). Name the snippet run `UNPROVEN (L70)` up front, or hand it to a step the desk runs.
- FAIL 3b: `bash -n scripts/smoke_s1.sh` is not allowed. Remove it, or mark it `UNPROVEN (L70)`.
- NOTE 1: `ORDER:` must name `S1` after D1 and before the commit (the drafter's default is right). This is a desk edit to the card.
- NOTE 2: header `TIP: 01107570` is behind the branch tip `d57714468` (the check's commit adds tests and the build report; it does not touch the script or `match.py`). The row cites `d57714468` correctly. The desk owns the header; it is unchanged by S1.
- NOTE 3: the row says the grade steps are `:80-98`; they end at `:100`. A wording slip; the row's logic is unaffected.

PREFLIGHT DONE · cards: 1082-S1 · checks: 13 · fails: 3 · ready: NO
