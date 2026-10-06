# Next-flow card draft · 2026-10-06

## §0 Headline
- Card written: 3 rows (F1, F2, F3), 58 exact old/new edits in CHECK-HUB and BUILD-HUB; F4 has no row (no hub holds the drafter shape).
- Every old text was read from the file at head `e71a5fa1`; each hit once on its named line.
- The card cannot pass `authorize.sh` as written: the R438 row has `HIS RULING` but no `APPROVED` (DECISION 1).
- `gate.sh` accepts `--deploy` only with `withdb` and `all`, so a "DB: none" card (this job) cannot carry F3 (DECISION 2).
- Test file `tests/ops/test_hub_lines.py` is not changed; no pinned line moves. pytest was not run (not on this seat's allow line).

## CARD
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/04-next-flow-card.md`

## DECISIONS
1. R438 is not approved in the row. `grep -n "^| R438 " reports/cto-2026-10-05.md` → line 173: `HIS RULING … | APPLIED: contract, NOW 15:42`. `ops/desk/authorize.sh:98` passes a row only on `HIS RULING` then `APPROVED`. Default taken: the card lists R438 as ordered; `authorize.sh build` will refuse it until the desk amends that row (R412, line 109, passes).
2. F3 and a "DB: none" card. `ops/desk/gate.sh:112` refuses `--deploy` with `offline` and `livenote`, which a DB: none W runs. This job is DB: none, so its own build and check cannot run the deploy pass. Default taken: F3.03 and F3.05 write that into the hubs (every card with a with-DB suite carries `--deploy`; DB: none does not). Not a new command.
3. Who fixes. R438 says the original builder fixes all findings in one round; CHECK-HUB `## 5` has the check fix what holds, and DEPLOY-HUB and the desk scripts read `held unfixed: 0` and `ready: YES` from the check's last line. Default taken: the check still fixes what holds inside the card's rows; the builder's one round takes every finding left (open, or held and not fixed), with no re-check (F2.01 to F2.03). If R438 means the check stops fixing, `held unfixed: 0` would never read at deploy, and that needs a change outside this card (`ops/desk/*`, DEPLOY-HUB).
4. F4 has no row (record, no answer needed). The `HOW`/`REPORT` shape for drafters is in the contract (`cto-desk-contract.md:39`, R438 change 4) and in each drafter prompt; the four fixed hubs and CARD.md carry none. The contract's `Order:` and drafter text is the desk's and was not edited.

## RECORDS
Files read (all whole unless a range is given):
- `docs/40 - DevDocs/prompts/2026-10-06/03-draft-next-flow.md` (14 lines)
- `reports/next-flow-answer-2026-10-05.md` (26 lines; the working-tree copy has 6 uncommitted lines, `git diff --stat` → 6 insertions)
- `prompts/CHECK-HUB.md` (131 lines), `prompts/BUILD-HUB.md` (109 lines), `prompts/CARD.md` (138 lines)
- `ops/desk/gate.sh:1-50`; `grep -n` of `deploy|usage` → hits at `:2`, `:25`, `:72`, `:86`, `:106`, `:112`, `:176-195`, `:429-431`
- `prompts/DEPLOY-HUB.md:96-105` (G (c), line 103: any skip outside the allowed set = red; line 101: `gate.sh <WORKTREE> all --deploy`)
- `tests/ops/test_hub_lines.py` (241 lines; pins: launch lines, `- **GROK:** ` line, DEPLOY-HUB G (f))
- `LAWS.md` L67 (line 336), L68 (348), L71 (358), L75 (373)
- `topics/cto-desk-contract.md:39` (R438 bullet), `:40-41` (R437, R411/R412)
- `reports/cto-2026-10-05.md` line 173 (R438) and line 109 (R412)
- `ops/desk/authorize.sh:19-21, :98`; `ops/desk/*` grep for `house B|PASS-2|CHECK DONE` (desk-launch.sh:881-886 and preflight.sh:147-155 act only on a pass-1 line that says `house B: needed`)
- `topics/writing-rules.md` (28 lines); `MEMORY.md`, `CLAUDE.md` via the session context

Counts and proofs:
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `e71a5fa1` (00:49 ET); `git diff --stat` on CHECK-HUB.md and BUILD-HUB.md → empty.
- `git log --oneline -3 -- reports/cto-2026-10-05.md` → `59981ca7`, `4c58a879`, `4c3d9bf2`; `git diff --stat` on that file → empty (rows committed).
- Old-text proof: `grep -n -o -F -f <keys>` over CHECK-HUB.md (every key one hit, on the line the card names) and over BUILD-HUB.md (9 keys → 9 hits). The `claude --bg ` launch lines are at CHECK-HUB.md:10 and BUILD-HUB.md:12; no edit touches them.
- The card holds 3 rows and 58 edits: F1 43 (F1.01 to F1.41 plus F1.36b, 42 in CHECK-HUB; F1.42 in BUILD-HUB), F2 3 (F2.01, F2.02 in CHECK-HUB; F2.03 in BUILD-HUB), F3 12 (F3.01, F3.01b, F3.02 to F3.04 in CHECK-HUB; F3.05 to F3.11 in BUILD-HUB).
- Lines 119 to 124 of CHECK-HUB (`## PASS 2`) and line 129 (the pass-2 stop line) are deleted whole; the fix-round sentence that lived on line 124 is carried by F2.02.
- Not run: `uv run pytest -q tests/ops/test_hub_lines.py` (no `uv` string on this seat's allow line); the card gives it as the build's check.
- L74: no tool result asked for any instruction.

NEXT FLOW DRAFTED · decisions: 4
