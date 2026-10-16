# draft-641-fixround — 2026-10-16

## §0 Headline
- Card 641 now has `## CONTINUE FIX ROUND`, rows FR-1 (O1) and FR-2 (G1), a FIX ROUND ORDER, checks X5 and X6, READ and RECORDS lines, and a new 2nd bullet of `## NOT IN THIS JOB`. CS-1 and R2 are untouched.
- Two orders cannot both hold as worded; I took a default for each (ASK DESK 1, 2 below).
- Only the card was edited. Nothing was run but reads.

## DECISIONS
1. ASK DESK: FR-1 and FR-2 contradict. FR-1 ignores check cards of another JOB, so the JOB test (`stage-set.sh:115`) could never fail, and FR-2 needs it to fail on a lone other-JOB card. Default taken: FR-1 gets a fallback. With no this-JOB check card and exactly one other-JOB check card, that card is handed to `:115`, which refuses it. Outcomes are the same as FR-1's (refuse, nothing deleted) and FR-2's test stays red for `:115` alone. Alternative: drop `:115` as dead code. [13:54 EDT]
2. ASK DESK: FR-1's discriminator ("header carries `CHECK REPORT:`") does not separate a build card from a check card. Build cards carry it too (`641-check-scratch-card.md:10`, `583-band-routing-card.md:10`). Then control (ii) fails: the READ copy 641 has this JOB and the pair with 648, so two cards refuse. Default taken: `HOUSE A:` must sit beside `CHECK REPORT:`. 648 and 638 have it (line 11); 641 has none. [13:54 EDT]
3. ASK DESK: the order's "count sentence in `## NOT IN THIS JOB` / `## WHY`" is only in `## NOT IN THIS JOB`, the 2nd bullet (the check report calls it the 3rd). `## WHY` holds none. Default: replaced the 2nd bullet. CS-1's row text (a) keeps its old words as history, with the precedence stated in the new section. [13:54 EDT]
4. ASK DESK: the card has no SELF-CHECK section; the self-check lives in the build report. Default: the FIX ROUND ORDER ends with a self-check line naming FR-1 and FR-2. The M5 correction is in FR-2 and adds the build report to the files. [13:54 EDT]
5. ASK DESK: 583 has no heading `CONTINUE FIX ROUND`. I used the order's heading and 583's launch phrase, `build` at `FIX ROUND row FR-1`. Default: this. [13:54 EDT]

## RECORDS
- `git -C /Users/cobalt/cobalt show 85eade55:ops/desk/stage-set.sh` whole: `clearable()` `:92`, find `:109`, none `:110`, count `:111`, version `:112-114`, JOB `:115`, prior `:116`, `rm -rf` `:151` `:158`. `git show 85eade55:tests/ops/test_stage_set.py` whole. `git diff --stat 85eade55 ops/check-scratch-1016 -- ops tests` printed nothing.
- Read whole: card 641, the check report, 583 (rows FR-1..FR-8, orders), headers of 648 and 638. Build report M5: `check-scratch-build-2026-10-16.md:150`.
- The test shapes (the FR-1 test and its two controls) are unrun; the card says so (L70).

DRAFTED · decisions: 5
