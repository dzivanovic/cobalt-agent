# ops-hand install card 306 — amend, 2026-10-10

## §0 Headline
Card 306 amended per preflight 307: 2 FAILs and 3 NOTEs fixed, edits to the card only.
R969 is cited by row id (R969 / R971), not line number.
I2's red-first counts now match the text I2 writes.

## DECISIONS
1. `## READ` also cited `cto-2026-10-10.md:8` for R969; changed to rows R969, R971 (same FAIL 5 rule: no line cites). Default taken, no other row touched.
2. `RULINGS` carries R971 as its own item `2026-10-10 R971` (R971 has its own HIS RULING row, `APPLIED: R969 row`).

## RECORDS
- Read against `HEAD` `9d498807`: `git diff HEAD --stat` over `STANDING-LIST.md`, `OPS-HAND.md`, `reports/cto-2026-10-10.md` → empty, so working files equal `git show HEAD:`.
- `git show HEAD:` of `reports/cto-2026-10-10.md`: rows `R971` and `R969` both `HIS RULING · APPROVED` (R971 confirms R969). Lines moved from `:8` to `:9`/`:11` while the card was in flight; the card now cites ids.
- `wc -l`: `STANDING-LIST.md` 220, `OPS-HAND.md` 22.
- `grep -c -F -e '`Bash(sudo *)`'` on `STANDING-LIST.md` → 0 on `BASE`, so the red is 0 → 1 after the row. `grep -c -F -e '## 8. `OPS-HAND.md`'` → 0.
- `grep -n "cto-2026-10-10.md:[0-9]"` on the card after edit → no match.
- Edits: header `RULINGS`; I1 cite; I2 red (sudo pattern, single-quoted, `-c`; count "220 on `BASE`, 233 after the row"; single-quoted `## 8.` grep); READ cite; two RECORDS bullets (R969 cite rewritten, amend read added).

OPS HAND INSTALL CARD AMENDED · decisions: 2
