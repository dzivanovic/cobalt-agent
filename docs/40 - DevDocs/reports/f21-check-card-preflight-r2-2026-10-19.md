## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt merge-base ops/f21-genesis-1013 main` | `40e646edf7264b21191b2b63f5fbbb2dede793c7` = BASE `40e646ed` | OK |
| 2 | `git -C /Users/cobalt/cobalt log --oneline 40e646ed..ops/f21-genesis-1013` | `817a07c3` build report · `66439da6` feat · `9f742f73` wip red; TIP `66439da6` in range | OK |
| 3 | `git -C /Users/cobalt/cobalt rev-parse 66439da6` | `66439da62e25165d2a468466ef5d05474bee7381` | OK |
| 4 | `git -C /Users/cobalt/cobalt diff --name-only --no-renames 66439da6 ops/f21-genesis-1013` | build report `.md` and `.result` only (head adds docs only) | OK |
| 5 | `git -C /Users/cobalt/cobalt diff --name-only --no-renames 40e646ed 66439da6` (counted) vs card row S0 and `Range files` (FAIL 13 of round 1) | 42 paths: 8 DevDocs pages, `gate-lists.md`, `cli.py`, 4 `db_migrations`, 5 `genesis` modules, 2 fixtures, 3 genesis tests, 18 pin files (21 test files − 3 genesis). Card lines 22 and 77 both say 42; `grep -n -E "37\|42 paths"` finds no "37 paths"; the listed parts sum to 42 | OK |
| 6 | `git -C /Users/cobalt/cobalt diff HEAD -- <card 820>` | empty | OK |
| 7 | `git -C /Users/cobalt/cobalt log --oneline -4 -- <card 820>` | `daaf70cf` (count fix), `6aa42654` (card); the card is committed | OK |
| 8 | `grep -n -E "«\|FILL\|TODO\|TBD\|XXX\|<[A-Z_]+>"` on card 820 | no match; no placeholder token | OK |
| 9 | `grep -n -E "claude --bg\|--allowedTools\|--add-dir\|--permission-mode\|desk-launch"` on card 820 | no match; the card adds no command string to any launch line | OK |
| 10 | `grep -n "ASK DESK"` on the build report vs card X3 and CHECK ASK X6 | items 1 (rank 1, line 365, no figure), 2 (8 chunks, header row one, separator none), 3 (`test_dml_roles_offline.py` moved to `FORWARD[-2]` / `REVERSE[1]`, no REVERSE mutation) carried as the build took them; REVERSE mutation is in row X3 | OK |
| 11 | `git show ops/f21-genesis-1013:tests/cobalt/test_dml_roles_offline.py`; `grep -n -i GRANT` on `0025_dml_roles.sql` | tip lines 21-23 hold `FORWARD[-2]` / `REVERSE[1]` with the `# F21 genesis (0026)` comment (the card's `:21-22` is BASE numbering; its read of 15-30 covers it); 0025:49 grants on all tables, 0025:57-75 sets default privileges; 0026 has no `GRANT` line (as the card says), proven by G1b in W1 PASS 2 | OK |
| 12 | header vs build card 468 (round 1 check 6, unchanged by the amend) | CLASS K2, INSTALL none, RESTARTS `com.cobalt.radar`, RULINGS `2026-10-11 R1055` identical; TIP filled; no BAND owed | OK |

## ISSUES
- NOTE: round-1 FAIL 13 is fixed; no new FAIL.
- NOTE: R411 and R412 are not in `CARD.md` or `CHECK-HUB.md`; check 9 tested the plain reading (no launch string in the card).
- NOTE: the grant is not by precedent missing (0024 has none either); whether 0025's default privileges cover 0026 is G1b's, run in W1 PASS 2.

PREFLIGHT DONE · card: f21-genesis-1013-check · checks: 12 · fails: 0 · ready: YES
