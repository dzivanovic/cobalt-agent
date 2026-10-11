## §0 Headline
- Card 317 now takes the CARRIED form (R998, L79): `CARRIED: <id> — <test id> — R<n>` satisfies a held id beside `FIXED:`.
- Edited: THE RULE (CARRIED LINES, COVER, REFUSED), rows H1, H2, H3 (tests and reads), row H4 (DEPLOY-HUB P2 and CARD.md text, greps). Header untouched, BASE stays.
- No script, test or other row touched; only `317-held-closed-card.md` changed.

## DECISIONS
- D1 CARRIED test check is a static read at the code tip: the `def` exists and a decorator in the contiguous `@…` lines above it holds `xfail` and `strict=True`; a `pytestmark` line does not satisfy it (the inverse of FIXED, where a `pytestmark` xfail refuses).
- D2 `R<n>` is read in `reports/cto-<date>.md`, `<date>` from the check report's file name; the row is a line starting `| R<n> |` carrying `DESK RECORD`. R993 and R998 of `cto-2026-10-10.md` match that shape (lines 13, 8).
- D3 H4's DEPLOY-HUB grep uses the full form `CARRIED: <finding id> — <test id> — R<n>` (0 on HEAD); the bare word `CARRIED` is already in DEPLOY-HUB (3 lines on HEAD), so it cannot be the count. CARD.md uses the bare word (0 on HEAD).
- D4 Card RECORDS line `why guard at :366` (amend reads, card 319) is `esac`; the `if [ -z "$why" ]` guard is `:367`. Not an H row, so left untouched; no H row cites it.

## RECORDS
- `git -C /Users/cobalt/cobalt diff --stat HEAD -- ops tests` → no output; `date` Sat Oct 10 21:46:09 EDT 2026. Every `ops/` and `tests/` line below is HEAD's.
- `git -C /Users/cobalt/cobalt show HEAD:ops/desk/deploy-card.sh` (21:46 ET): `:172-173` refusals, `:180` `frep=`, `:183` `fblob=`, `:201` SHIPS row, as the card cites.
- Grep of `ops/desk/desk-launch.sh` (`date` 21:46:23 ET): `clast=` `:946`, `ltip=` `:955`, `fixed_ok()` `:959`, `ltip` short-circuit `:973`, refusal `:974`; as the card cites.
- Grep and Read of `ops/desk/deploy-step0.sh` (`date` 21:46:23 ET): header `:24`, `lits=` `:337`, prefix `:340`, `esac` `:366`, `if [ -z "$why" ]` `:367`, `*"$lit"*` `:371`.
- Grep of `reports/cto-2026-10-10.md`: R998 line 8, R993 line 13, each `DESK RECORD (brain, L79)`.
- Grep of `DEPLOY-HUB.md`, `CARD.md` (`git status` shows both unmodified; `date` 21:47:02 ET): `CARRIED: <finding id>` in DEPLOY-HUB → 0; bare `CARRIED` in DEPLOY-HUB → 3 lines (`:32`, `:118`, `:119`), in CARD.md → 0.
- `git status --short -- "docs/40 - DevDocs/prompts"`: only `317-held-closed-card.md` modified.
- Reads by Grep on the working file, not `git show … | grep` (the bare-guard hook refuses a pipe with `git`); `git diff --stat HEAD` empty bounds them to HEAD.

HELD CLOSED CARD CARRIED · decisions: 4
