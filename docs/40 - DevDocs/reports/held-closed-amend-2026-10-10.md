## §0 Headline
Card 317 amended in place (header and BASE untouched), after preflight ready NO (2 fails, 6 notes).
FAIL 18: H2 happy path is a pin; red-first comes from the refusals.
FAIL 26: held path keyed on the check's last line, before the tip short-circuit; one red test each in H2 and H3.
Notes folded: unlisted-id and two-lines cases per suite, `open` parameter in three `check_line` helpers, `frep` moved before `:172`, exact `<n>` compare, H4 cites, RECORDS.

## DECISIONS
- D1 H2 happy path listed as a pin; the false BASE text is dropped.
- D2 THE RULE: the held path runs before the `ltip` short-circuit and outside step0's `$why` guard; two new red tests.
- D3 `held unfixed: 0` over `held unfixed: 1` is a pin in H2.
- D4 Unlisted-id in H2 and H3; two-lines in H3.
- D5 `open` parameter in the three `check_line` helpers; `--fix-report` lookup moves before `:172`.
- D6 Exact `<n>` compare; one test pins `held unfixed: 10` against n = 1.
- D7 H4 cites `:427-428`, `:588-589`; RECORDS adds the named reads.

## RECORDS
- Reads: `git -C /Users/cobalt/cobalt show HEAD:<file>` with `grep -n`/`sed -n`, 2026-10-10 21:41 ET (`date` in each call) for `deploy-card.sh`, `deploy-step0.sh`, `desk-launch.sh`, the three suites, `restarts.py`; `git diff --stat HEAD -- ops tests` printed nothing.
- Proven: `frep=` `:180` after `:172-173`; `*"$lit"*` `:371`; `ltip` short-circuit `:973-974`; `check_line` `:40`, `:78`, `:68` each `open: 0`; `CARD.md`/`DEPLOY-HUB.md` reads `:427-428`, `:588-589`; `fix_round` `:559`; `restarts.py:225-226`.
- Edited: `prompts/2026-10-10/317-held-closed-card.md` only. Not run: no test, no launch. `deploy-step0.sh:24-31` was read as a header by its first lines only.

HELD CLOSED CARD AMENDED · decisions: 7
