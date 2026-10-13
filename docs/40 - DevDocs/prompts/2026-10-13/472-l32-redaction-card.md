JOB: l32-redaction-1013
CLASS: K2
LADDER: OFF-LADDER — reports/f23-tribunal-2026-10-11.md 2026-10-13 R1343
BRANCH: docs/l32-redaction-1013
WORKTREE: l32-redaction-1013
BASE: «FILL: 8-hex commit on main the branch stands at — the desk's placeholder»
TIP:
REPORT: /Users/cobalt/cobalt-wt/l32-redaction-1013/docs/40 - DevDocs/reports/l32-redaction-build-2026-10-13.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/l32-redaction-check-2026-10-13.md
HOUSE B:
DB: none
RULINGS: 2026-10-12 R1138

## ROWS

DOCS ONLY: every file sits under `docs/`. Each row names its span by file, line and section only (L32: this card quotes no count). The builder reads the span in place on BASE, replaces exactly that span with `[user data]`, and changes no other character. Lines proven against `git -C /Users/cobalt/cobalt show HEAD:<file>` at HEAD `0e3590dc`.

| row | what | red first | files |
|---|---|---|---|
| L1 | `f23-design-proposal-2026-10-10.md:19`, `## 2.1`, the last bullet (the live-vault count of strategy notes with a `family:` and the per-family deck sizes). Span = the bullet text after `- `; the line becomes `- [user data]`. Backed by `reports/f23-tribunal-2026-10-11.md` :60 and item 8 :298 | RUN — asserts nothing. `grep -c -E "[0-9]+ non-empty" "<file>"` prints 1 on BASE; quote it, then 0 after | `docs/40 - DevDocs/reports/f23-design-proposal-2026-10-10.md` |
| L2 | `f23-design-proposal-2026-10-10.md:76`, `## 5`, the live-note suite line. Span = the tail that gives the per-family deck setup counts and its parenthetical about the build day's counts (from `deck setup counts` to the closing parenthesis); the line keeps its opening and its final period, so it ends `, [user data].` | RUN — asserts nothing. `grep -c -E "[0-9]/[0-9]/[0-9]/[0-9]/[0-9]" "<file>"` prints 1 on BASE; quote it, then 0 after | same file as L1 |
| L3 | `f23-design-2026-10-10.md:50`, `## RECORDS`, the vault grep-count line (the F23 drafter report; the tribunal calls it `12-drafter-report` `:50`). Span = the bullet text after `- `; the line becomes `- [user data]` | RUN — asserts nothing. `grep -c -E "[0-9]+ non-empty" "<file>"` prints 1 on BASE; quote it, then 0 after | `docs/40 - DevDocs/reports/f23-design-2026-10-10.md` |
| L4 | `prompts/2026-10-11/338-f23-tribunal.md:16`, section `## 1.`, in the KNOWN SPANS paragraph: the parenthetical after "its `## 5` live-note line" holds the per-family counts as a five-number literal. Span = that literal only (inside its backticks); the parenthesis then reads `(the `[user data]` counts)` | RUN — asserts nothing. `grep -c -E "[0-9]/[0-9]/[0-9]/[0-9]/[0-9]" "<file>"` prints 1 on BASE; quote it, then 0 after | `docs/40 - DevDocs/prompts/2026-10-11/338-f23-tribunal.md` |
| V1 | RUN — asserts nothing. After L1-L4: `git diff --stat BASE` lists exactly the three files and 4 changed lines; the two `grep -c -E` patterns above print 0 on all three files, and `grep -c -E "time_window [0-9]"` prints 0 on the two f23 reports; quote the output | — (tool output quoted in the report) | none (read only) |

## NOT IN THIS JOB
- Git history: it still holds the old text; rewriting it is NOT in scope and is his word alone.
- Any span beyond L1-L4 (the desk's further-span list is in `reports/draft-l32-redaction-2026-10-13.md` `## RECORDS`; each needs its own card row).
- `docs/30 - Design/F23-FINAL-2026-10-11.md` (untouched) and the staged tribunal copies.
- Any `src/`, `configs/`, `tests/` or `ops/` file.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f23-tribunal-2026-10-11.md` :60 and :298 (the three known spans).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/draft-l32-redaction-2026-10-13.md` `## RECORDS`.

## RECORDS
- `git -C /Users/cobalt/cobalt grep -n` of the two count patterns on HEAD `0e3590dc` printed `:19`, `:76` (proposal), `:50` (drafter report) and `:16` (`338-f23-tribunal.md`) (the drafter, 2026-10-13). Neither f23 report is modified in the working tree.
- R1138 is his row `HIS RULING · APPROVED` of `reports/cto-2026-10-12.md` :173.
