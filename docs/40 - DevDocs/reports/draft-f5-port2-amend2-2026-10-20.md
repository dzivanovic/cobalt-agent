## §0 Headline

Card 731 amended in place for preflight r2 FAIL 22.
PORT (7) no longer orders "the f5 offline line and the readers line of ## DEPLOY PROOF"; the `## OFFLINE` gate line of `ops/desk/gate-lists.md` that PORT (7) already names stays (heading proven at `HEAD:ops/desk/gate-lists.md:23`).
No other PORT, DONE WHEN or CHECK ASKS reference to the dropped lines was found; PORT1 (:43) and FIX2 (:44) context rows untouched. K0 and the other NOTEs left. Nothing committed.

## DECISIONS

None.

## RECORDS

2026-10-20 07:17 (`date`)
- Read: `prompts/2026-10-20/907-draft-f5-port2-amend2.md`; `reports/f5-port2-preflight-r2-2026-10-20.md` (`## ISSUES`, FAIL 22); `prompts/2026-10-18/731-f5-card.md` (grep for `offline line|readers line|DEPLOY PROOF`: hits at :43 PORT1, :44 FIX2, :45 PORT, heading :96; count of the two clause phrases = 3 lines).
- Proved: `git grep -n "^## OFFLINE" HEAD -- ops/desk/gate-lists.md` → `:23 ## OFFLINE`.
- Edited: card :45 PORT (7), clause deleted only.

DRAFTED · decisions: 0
