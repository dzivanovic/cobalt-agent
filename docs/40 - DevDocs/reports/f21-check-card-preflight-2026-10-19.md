## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt merge-base ops/f21-genesis-1013 main` | `40e646edf7264b21191b2b63f5fbbb2dede793c7` = BASE `40e646ed` | OK |
| 2 | `git -C /Users/cobalt/cobalt log --oneline 40e646ed..ops/f21-genesis-1013` | `817a07c3` build report · `66439da6` feat · `9f742f73` wip red; TIP `66439da6` is in the range | OK |
| 3 | `git -C /Users/cobalt/cobalt rev-parse 66439da6` | `66439da62e25165d2a468466ef5d05474bee7381` (resolves, 8-hex prefix matches) | OK |
| 4 | `git -C /Users/cobalt/cobalt diff --name-only --no-renames 66439da6 ops/f21-genesis-1013` | `reports/f21-genesis-build-2026-10-13.md` and `.result`, nothing else (head adds the report only) | OK |
| 5 | `ls` of `/Users/cobalt/cobalt-wt/f21-genesis-1013/docs/40 - DevDocs/reports/`; `ls` of the CHECK REPORT path | build report `f21-genesis-build-2026-10-13.md` present at the card's REPORT path; CHECK REPORT path is under `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/`, file absent (expected, check not run yet) | OK |
| 6 | `grep -n -E "^(JOB\|LADDER\|CLASS\|…\|RULINGS):"` on build card 468 vs the check card header | JOB, LADDER, CLASS K2, INSTALL none, BRANCH, WORKTREE, BASE, REPORT, CHECK REPORT, HOUSE B, RESTARTS `com.cobalt.radar`, RULINGS `2026-10-11 R1055` identical; TIP filled; 468 has no BAND, so none owed (CARD.md BAND row); HOUSE A added from precedent 817 | OK |
| 7 | `grep -n "ASK DESK"` on the build report (lines 218-220) vs card X3 and CHECK ASK X6 | item 1 (G6 question without the figure, rank 1, line 365), item 2 (8 chunks, header row one, separator none), item 3 (`test_dml_roles_offline.py` moved to `FORWARD[-2]` / `REVERSE[1]`, no REVERSE mutation) all carried as the build took them; the REVERSE mutation is in row X3 | OK |
| 8 | `git show ops/f21-genesis-1013:…/0026_genesis_chunk.sql`; `grep -n -i GRANT` on `0025_dml_roles.sql` and `0024_strike_alerts.sql` | 0026 has no `GRANT`; 0024 (the shape 0026 copies) has none either; 0025:48-50 grants on all tables, 0025:57-75 sets `ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_user…`. The card asks it (row G1, CHECK ASK X4) | OK |
| 9 | read card rows G1, X3, X4 and CHECK ASKS X4, X7 | X4 grant ask present (G1 + ask X4); REVERSE mutation present (X3, names six test files); F5 `0027` renumber present (row X4, ask X7); `grep -c -F 0027` on card 731 → `4` | OK |
| 10 | `git -C /Users/cobalt/cobalt diff HEAD --stat -- <card 820>`; `git log --oneline -2 -- <card 820>` | diff empty; committed in `6aa42654` | OK |
| 11 | `grep -n -E "«FILL"` on card 820 | no match | OK |
| 12 | `grep -n -E "claude --bg\|--allowedTools\|--add-dir\|--permission-mode\|desk-launch"` on card 820 | no match; the card holds no launch line and no launch command string (R411, R412) | OK |
| 13 | `git diff --name-only --no-renames 40e646ed 66439da6` (counted) vs the card's "37 paths" (card lines 22 and 77) | 42 paths: 8 DevDocs pages, `gate-lists.md`, `cli.py`, 4 `db_migrations` files, 5 `genesis` modules, 2 fixtures, 3 genesis tests, 18 pin files. The card's listed groups sum to 42, its stated total says 37 | FAIL |
| 14 | `git show ops/f21-genesis-1013:tests/cobalt/test_dml_roles_offline.py` | `FORWARD[-2]` / `REVERSE[1]` with the `# F21 genesis (0026)` comment (tip lines 21-23; the card's `:21-22` is BASE's numbering); the card reads lines 15-30, which covers it | OK |

## ISSUES
- FAIL 13: card `820-f21-genesis-check-card.md` lines 22 and 77 say "37 paths"; the diff lists 42 and the card's own list sums to 42. Change `37` to `42` in both places, commit, then launch. The checker would otherwise stop at S0 on a count the card got wrong.
- NOTE: draft decisions 1-5 are NOTES; none is proven wrong. 1 (HOUSE A grok from precedent 817) and 2 (no BAND, 468 has none) agree with CARD.md; 4 (F5 at `0027`) agrees with card 731 (4 hits of `0027`); 5 (six test files in X3) is the check's to widen.
- NOTE: the grant (decision 3) is not missing by precedent: 0024 has no `GRANT` either, and 0025's default privileges name `cobalt_user`. Whether that covers 0026 is proven by `test_dml_roles_db.py` (G1b) in W1 PASS 2, as the card asks.
- NOTE: R411 and R412 are not in `CARD.md` or `CHECK-HUB.md`; check 12 tested the plain reading (no launch string in the card).

PREFLIGHT DONE · card: f21-genesis-1013-check · checks: 14 · fails: 1 · ready: NO
