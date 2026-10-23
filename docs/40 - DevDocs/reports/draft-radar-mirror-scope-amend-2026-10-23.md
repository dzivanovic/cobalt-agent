# draft-radar-mirror-scope-amend — card 1020 amended after preflight FAIL

## §0 Headline
- Card 1020 amended in place, three edits: deploy-proof marker 1 now holds no quote, backslash, `$` or backtick; the ticker is gone from WHY; M1's unknown-source test counts one warning line per `mirror_sources` call.
- Marker 1 proved against `main`: `MIRROR_SOURCE_PREFIX = ` occurs 0 times in `notes.py` (before `0`), and after M1 it occurs once.
- Nothing run beyond reads and greps, nothing committed.

## DECISIONS
1. Marker 1 is now `grep -c -F "MIRROR_SOURCE_PREFIX = " /Users/cobalt/cobalt/src/cobalt/radar/notes.py` · before `0` · after `1`. `ops/desk/deploy-smoke.sh:122-129` cuts a pattern at the first `"` and `:127` refuses a backslash, so the old `\"` pattern would have gone RED on a correct deploy.
2. To make "after 1" unambiguous I added a parenthesis to M1's constants sentence. The definition `MIRROR_SOURCE_PREFIX = "vault:radar-notes@"` is ONE line, assigned once, and no other line of `notes.py` may hold the text `MIRROR_SOURCE_PREFIX = `. The prompt asked me to state how the card makes the single line, and M1 is where the card defines it. This is the only wording I added beyond the three listed items.
3. WHY now says "the 10-21 edit" in place of the ticker. The brain's verbatim `## RECORDS` line is untouched, byte for byte, and still holds the ticker, as the prompt required.
4. M1's unknown-source test now says "One line" is PER `mirror_sources` call. The sink wraps each call alone, and the assertion counts one warning line for the first call and one for the second.
5. BASE, TIP, BAND and every other row are unchanged.

## RECORDS
- Start 2026-10-23 08:36 EDT (`date`).
- Read: prompt 1025; card 1020 (whole); `reports/radar-mirror-scope-preflight-2026-10-23.md` (whole, check 25 and NOTES 6 and 9).
- `git -C /Users/cobalt/cobalt grep -c -F "MIRROR_SOURCE_PREFIX = " main -- src/cobalt/radar/notes.py` → no output (zero matches). Before is `0`.
- `git -C /Users/cobalt/cobalt grep -n -F "MIRROR_SOURCE_PREFIX" main -- src tests ops` → no output. The name occurs nowhere on `main`, so no other line of `notes.py` holds the pattern.
- After M1: the pattern `MIRROR_SOURCE_PREFIX = ` matches only the one definition line the card specifies. The uses at the `:749` label and in the ownership test are references, not assignments, and carry no ` = `. The builder reads the marker on the tree (card ORDER).
- Ticker occurrences in the card, by Grep: line 17 (WHY, replaced) and line 65 (the brain's verbatim line, kept).
- Edited only `docs/40 - DevDocs/prompts/2026-10-23/1020-radar-mirror-scope-card.md`. Git write: none.

DRAFTED · decisions: 5
