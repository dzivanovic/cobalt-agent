# draft-f20-fix-round — 2026-10-18

## §0 Headline
- Added ONE row `W` (fix round, three parts G5 a, G7 a, G6 yes) to card 730, same card, original builder, BAND HIGH; ORDER ends `…, D0, W`, then the check scoped to the fix round, then the deploy.
- Files: the two test files, and `src/cobalt/cos/{session,run,cli}.py` only if a test finds a real defect. No `jobs/wrapper.py`. BASE, TIP, CHECK REPORT, HOUSE B untouched.
- Every `file:line` read on `fae30bbd` (tree clean); recorded in the card's `## RECORDS` and below.
- 2 decisions: red lines that may be green on the tip as built.

## DECISIONS
1. ASK DESK: the G5 and G6 new tests may be GREEN on the tip as built (the tree kill and the non-dry-run path both exist), so "red against the tip" cannot hold literally. [14:00 EDT]
   Default taken in row W: red is shown by a named cut (`_kill_tree` cut to the CLI pid alone; `_run` forced to `["--dry-run"]`), and a test green on the tip is said so, not a fault. Only G7 is expected red on the tip as built (the `allow_prod` keyword and `result` value differ).
2. ASK DESK: how strict is G7's "same rows, compared by field"? [14:00 EDT]
   Default taken: compare method, label, `exit_code`, `error` first line, and keywords with `allow_prod=False` filled in; `result` only present-or-None; a differing field is fixed in `cos/run.py`, never in the wrapper.

## RECORDS
- `date` → Sun Oct 18 14:00:11 EDT 2026.
- `git -C /Users/cobalt/cobalt rev-parse fae30bbd` → `fae30bbd960066970094fb7c45399532349f5a91`; `git -C /Users/cobalt/cobalt-wt/f20-cos-1018 rev-parse HEAD` → same; `status --short` → empty.
- Read: `git show fae30bbd:` `src/cobalt/cos/session.py`, `cos/run.py`, `cos/cli.py`, `jobs/wrapper.py`; line numbers from the same clean tree for `jobs/store.py`, `configs/cobalt/jobs.yaml:206-227`, `tests/cobalt/test_cos_offline.py:121,310,375-386`, `tests/cobalt/test_cos_listener.py:244-249`. The full list is in the card's `## RECORDS`.
- Edited: the card, row `W` after `D0`, ORDER line, one RECORDS line. Committed nothing; no launch, no DB, no production command.
- Nothing I could not trace is left outside the two decisions.

DRAFTED · decisions: 2
