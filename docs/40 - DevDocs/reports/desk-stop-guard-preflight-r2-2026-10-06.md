# Desk stop-guard card 66 preflight r2 2026-10-06

Main HEAD `556cd58b`. Round 1 checks 1-19 re-run on the amended card; the card diff since `ddf6f4b3` is the two amend edits only.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt diff ddf6f4b3 HEAD -- <card 66>` | two hunks only: G1 row (`:19`: the FIRST `Read '([^']+)'` sentence added to "what", one control added to "red first") and `## READ` (`:56`: `` (`:124-129`) `` removed). Nothing else moved | OK |
| 2 | Card header `:1-12` (unchanged by diff) | `BRANCH: ops/desk-stop-guard-1006`, `WORKTREE: desk-stop-guard-1006`, `BASE: «FILL: main HEAD at launch, 8 hex»` (the one fill), `TIP:` `CHECK REPORT:` `HOUSE B:` empty, `DB: none`, `RULINGS: 2026-10-06 R590` | OK |
| 3 | RULINGS R590 (round 1 NOTE 1) | unchanged: `HIS ORDER` + `APPLIED` in `cto-2026-10-06.md`; his direct order, committed (`becf04a2`) | OK (NOTE) |
| 4 | `git diff --stat HEAD -- prompts/2026-10-06 amend report` | empty: card, prompts and amend report committed, none modified | OK |
| 5 | `git diff --stat ddf6f4b3 HEAD -- ops tests/ops src/cobalt/jobs/restarts.py CTO-DESK-WAKEUP.md` | empty: every code, test, restarts and wake-up cite of round 1 checks 4-11 still matches (round 1 quotes stand) | OK |
| 6 | Round 1 FAIL 2 fix: `grep -n "124-129" <card>` | no output; `## READ` (`:56`) now cites `` `## §5 CURRENT` `` by name, no range. Heading exists: `grep -n "^## §5 CURRENT"` → `cto-2026-10-06.md:127` | OK |
| 7 | Round 1 NOTE 3 fix: `grep -n "Read '" ops/desk/bare-guard.py` | `:727 m = re.search(r"Read '([^']+)'", text)` is a first-match `re.search`, as G1 now states; `:736 … hub == "CTO-DESK-WAKEUP.md"`; `stop-guard.py:79 return " ".join(` is the space join G1 states | OK |
| 8 | New G1 control red/green on BASE: first message `Read '<other file>'` with a later `Read '…CTO-DESK-WAKEUP.md'` | on BASE `stop-guard.py:122 if worktree(cwd) is None` → exit 0 (stderr empty); after the build the first match is the other file, not the desk → exit 0. Green on both, a control as stated | OK |
| 9 | G1-G6 vs R590, new commands/args (R411, R412), RESTARTS class homes, red-first of the other tests, X4 | unchanged from round 1 checks 14-19 (card text outside the two hunks identical) | OK |

## ISSUES
1. NOTE — RULINGS `2026-10-06 R590` is `HIS ORDER` / `APPLIED`, not the literal `HIS RULING` / `APPROVED`; his direct order, committed. Stands as a NOTE.
2. NOTE — card `## RECORDS` says citations proven at `d2f651ce`; code files are unchanged through `556cd58b`. (Round 1 NOTE 4.)
3. Round 1 FAIL 2 and NOTE 3 are fixed (checks 6, 7).

PREFLIGHT DONE · card: desk-stop-guard-66 · checks: 9 · fails: 0 · ready: YES
