# draft-recut-archive-amend 2026-10-12 — card 434

## §0 Headline
Card 434 amended in place after preflight round 1 (2 FAILs, notes). Five anchors re-proved at HEAD `75c39896` and fixed; a seventh test RA7 (archive name present) and a lock-directory case RA3 (g) added; the card now says SEVEN tests. The brain's row text, BASE `0990393f` and every other row are untouched.

## DECISIONS
1. RA3 (g) is the lock-directory case and keeps (f) as `.env` only, so the preflight's "beside RA3 (f)" holds.
2. Test (a)'s miss text is pinned: `DEPLOYED: tag <name> exists` for the tag case, `DEPLOYED: <report file> holds a DEPLOYED line` for the report case; RA2 asserts `DEPLOYED` on both.
3. RA7 fixes the stamp by stubbing `date` on `PATH` (`20261012-1930`), two cases: archive tag present, archive branch present.
4. Anchors beyond the five named, cited with the card's own wording: OWED in `## READ` and the "F4 card 304" line now `:155` (the deploy-queue row; `:153-154` are other OWED rows), so I wrote `:155`, not the preflight's `:153-154`.
5. RA6: comment lines (first non-blank character `#`) are dropped before counting calls.

## RECORDS
- Reads at `main` HEAD `75c39896` (`git diff --stat 0990393f HEAD -- ops src tests` is empty): `ops/desk/desk-launch.sh` `:1847` (`recut)`), `:1853` and `:1861` (nested `;;`), `:1873` `bw=`, `:1874` `bt=`, `:1875` `br=`, `:1917` (comment naming `gate-clean.sh`), `:1935` (the arm's own `    ;;`) — `git grep -n`.
- `reports/cto-2026-10-12.md` at HEAD: R1279 `:9`, R1278 `:10`, R1277 `:11`, R1138 `:148`, OWED deploy queue `:155` — `git grep -n`.
- Card 434, `preflight` report `recut-archive-preflight-2026-10-12.md` `## CHECKS` and `## ISSUES`, read whole.
- RESTARTS classes written into the card's `## RECORDS`: `desk-launch.sh` "operator script; no Cobalt reader", the test file "test/documentation; no resident", reports `DOCS` (`restarts.py:38`, `:225-233`, `:246`, as the card's R2 row cites them; not re-read by me, taken from the preflight check 14).
- Not touched: the NOTE on directory/file clash (the card already words the `archive stopped at` refusal); the uncommitted files on main (the desk's).

DRAFTED · decisions: 5
