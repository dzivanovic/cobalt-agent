# Desk stop-guard card 66 amend 2026-10-06

## §0 Headline
- Card `66-desk-stop-guard-card.md` amended by two edits, nothing else.
- `## READ` cites `## §5 CURRENT` by name, no line range; the card repeated the range nowhere else.
- G1 says the builder takes the first `Read '…'` match; one new test row covers a later `Read '…CTO-DESK-WAKEUP.md'`.
- `BASE` is still the one `«FILL` token; `TIP`, `CHECK REPORT`, `HOUSE B` stay empty.

## CHANGES
Card `docs/40 - DevDocs/prompts/2026-10-06/66-desk-stop-guard-card.md`:
- `:56` (`## READ`): `` `## §5 CURRENT` (`:124-129`). `` → `` `## §5 CURRENT`. ``
- `:19` (G1, what): after the `bare-guard.py:727-736` rule, added: `The builder takes the FIRST Read '([^']+)' match in the message, as bare-guard.seat does (:727); first_user_text joins list texts with a space where bare-guard.first_message joins with a newline.`
- `:19` (G1, red first): after the prose-mention control, added the control: a first message that reads another file (`Read '<other file>'`) and has a later `Read '…CTO-DESK-WAKEUP.md'` in its body, exit 0 and stderr empty on BASE and after.

## DECISIONS
None.

## RECORDS
- Read: card 66 whole; `reports/desk-stop-guard-preflight-2026-10-06.md` whole (ISSUES 2, 3); `Memory/topics/writing-rules.md`.
- `ops/desk/bare-guard.py:667` `first_message`; `:727` `m = re.search(r"Read '([^']+)'", text)`: first match, as G1 now says.
- `ops/desk/stop-guard.py:79` `" ".join(` in `first_user_text`: space join, as G1 now says.
- Grep of the card for `124-129`, `:124`, `§5 CURRENT`: the range was only at `:56`; `:20`, `:22`, `:33` mention the heading without a range.
- Main HEAD `97710e05` (`git rev-parse --short=8 HEAD`).

DESK STOP GUARD CARD AMENDED · decisions: 0
