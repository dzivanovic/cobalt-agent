# ops-hand — card 231 amend, 2026-10-10

## §0 Headline
Card `prompts/2026-10-10/231-ops-hand-card.md` amended for preflight ISSUES 1-8, in place.
`BASE`, `TIP`, `CHECK REPORT`, `HOUSE B`, `RULINGS` untouched; no row added, class not widened.
Two decisions, both defaulted.

## CHANGES
1. H5 cites `:385-386` and `:405-406`.
2. H1 gets negative controls (c) another-prompt first message keeps kind `None`; (d) a later message naming `OPS-HAND.md` leaves a brain or worker unchanged.
3. H4 refusal tests each assert exit 1 and their own `REFUSED:` reason (red on `BASE`); the clean-fixture dry run is the positive control.
4. H3 `--disallowedTools` adds `Monitor`, `CronCreate`, `RemoteTrigger`, `ScheduleWakeup`, `Skill`, `WebFetch`, `mcp__*`, `Artifact*`; H3 and D3 state the non-Bash bound is his tap; H4 requires the whole H3 deny set (a `Monitor` refusal test added).
5. `## RECORDS` names the class home per file: `OPS_DESK_PREFIX` `:230`, `:245`, `DOCS` `:225-228`; any other label is a DECISIONS item.
6. H4 lists the three gates copied from kind `prompt` (`:441-444`, `:493`, `:541-544`) with a refusal test each.
7. H1, H2 and H4 tests use `roots.wt / ".ops-hand"`.
8. H4 says leave `:675` and header `:98` unchanged (first option taken).

## DECISIONS
- D-a. The new H4 reason strings (mode, `--name`, deny, allow, title, settings, live row, argument) are the builder's wording, one distinct string per case; the card pins no text (R411). The copied gates reuse the prompt kind's strings.
- D-b. H4 requires the full H3 deny set, so a name the harness rejects in a deny pattern must leave both H3's line and the check together. Default: as written.

Also added to `## RECORDS` (preflight NOTE 13, not one of the 8): the seat's first `Read` is itself a prompt. Preflight NOTES 9-12, 14, 15 left as they were.

## RECORDS
- Code proved at `d0a5fbb8` (`git diff --stat d0a5fbb8` on the four files below is empty, so the line reads are of the same text; `git show d0a5fbb8:<path>` read whole for `ops/desk/desk-launch.sh`, `ops/desk/stop-guard.py`, `src/cobalt/jobs/restarts.py`):
  - `stop-guard.py:112` `def worktree`; `:385` `if worktree(cwd) is not None:`; `:386` `return worker(event, cwd)`; `:405-406` `if text is not None and not CARD.search(text): return 0`.
  - `desk-launch.sh:441-444` Read-sentence case; `:493` `<`/`>` refusal; `:541-544` text-after case; `:675` kind refusal; `:98` header kind list.
  - `bare-guard.py:672` dot-name skip in `worktree_of`.
  - `restarts.py:38` `OPS_DESK_PREFIX`; `:225-228` DOCS; `:230` operator script; `:245` tests.
- Nothing run; no git write.

OPS HAND CARD AMENDED · issues fixed: 8 of 8 · decisions: 2
