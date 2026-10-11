## §0 Headline
- Wrote `prompts/2026-10-11/344-298-fixed-line.md`: four proofs, then one FIXED line, then one path-limited docs commit.
- One launch line; allow list is the BUILD-HUB subset plus `Edit(//…/house-seat-order-1010/**)`; no new command.
- The worker's own report lies outside the worktree, and no allowed tool creates a file there (decision 1).

## DECISIONS
- ASK DESK: the worker report `reports/fixed-line-298-2026-10-11.md` needs a new file outside the worktree; `Edit` is scoped to the worktree and `Write` is not on the BUILD-HUB line. Without a change the worker writes the commit but cannot write its report. [before launch] Default: add `"Write(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/fixed-line-298-2026-10-11.md)"` (that one path) to the launch line, or pre-create the file empty so Edit can fill it.

## RECORDS
- Read: `prompts/2026-10-11/343-draft-298-fixed-line.md` (task), `341-amend-launcher-324-r2.md` (launch-line shape), `339-fix-tribunal-triples.md` (layout), `Memory/topics/writing-rules.md`, `prompts/BUILD-HUB.md` line 12 (grep of its `--allowedTools`).
- Read: tail of the worktree build report: last non-blank line is `BUILT · job: house-seat-order-1010 · tip: 1b671292 | …`.
- `ls` of `reports/house-seat-order-check-2026-10-10.md`: exists.
- Grep `claude --bg` in 344: count 1.

DRAFTED · decisions: 1
