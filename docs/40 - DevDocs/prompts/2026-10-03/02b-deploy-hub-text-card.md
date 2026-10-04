JOB: deploy-hub-text
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/deploy-hub-text-1003
WORKTREE: deploy-hub-text-1003
BASE: 44b29c63
TIP: 69bf6082
REPORT: /Users/cobalt/cobalt-wt/deploy-hub-text-1003/docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-hub-text-check-2026-10-03-r3.md
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B: as needed
TREE STATE: unchanged
DB: none
RULINGS: 2026-10-02 R47, 2026-10-02 R154, 2026-10-02 R157

## ROWS

WHY: `DEPLOY-HUB.md` on `main` is the text every deploy runs under until a new text lands. P7 and STEP-T read any path under `src/cobalt/db_migrations/` as a migration, so the `03c` chain's `cli.py` (command code, no schema) cannot ship (`deploy-set2-1003.md` DECISIONS); and STEP-C refused a plist under `ops/desk/` (deploy set 2b, card `05`). This card is the P7 / STEP-T / STEP-C fix ONLY, on `main`'s `DEPLOY-HUB.md`. RE-ISSUE (judge, JUDGE ASK 16, `reports/deploy-hub-text-decisions-2026-10-03.md`): Grok's 8 findings on the first build (`reports/deploy-hub-02b-grok-read-2026-10-03.md`) all HOLD; T1 and T6 take the judge's sentences; the first issue's rows T2–T5 are CUT from this card (they describe the chain's text and are written by the port card `03d` against the chain's own clauses) — the build REMOVES the sentences it wrote for them. Docs only: one file, `DB: none`, no restart, deploys at any hour.

| row | what | red first | files |
|---|---|---|---|
| T1 | P7: "a MIGRATION is any file ending .sql under src/cobalt/db_migrations/ (whatever its name), or a changed line inside FORWARD = (…) of src/cobalt/db_migrations/__init__.py that adds, removes or reorders an entry; every .py under that folder (cli.py, placement.py, dev_rebuild.py), tests and docs are CODE and pass MIGRATIONS: none" (replaces the first build's `[0-9][0-9][0-9][0-9]_*.sql` sentence). STEP-T's FORWARD check: `grep -n -F 'MIGRATIONS_DIR / "' <GATE>/src/cobalt/db_migrations/__init__.py` (the `00` dropped) | no test: hub text; `grep -c -F "whatever its name"` → 1; `grep -c -F "[0-9][0-9][0-9][0-9]_*.sql"` → 0; `grep -c -F 'MIGRATIONS_DIR / \"00'` → 0 | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` |
| T6 | STEP-C: "a plist ADDED or MODIFIED anywhere under ops/ is refused, except one under ops/desk/ whose Label string (the <string> value on the <key>Label</key> line or the line after it) is not the label: value of any entry in configs/cobalt/jobs.yaml and whose path is not ops/<label>.plist; a Label the read cannot find is refused" (RE-ISSUE 2, JUDGE ASK 17: replaces the r2 sentence "whose Label (the line after <key>Label</key>, read by grep -A1 -F) is not a key of …") | hub text; `grep -c -F "a Label the read cannot find is refused"` → 1; `grep -c -F "is not a key of configs"` → 0 | the same file |
| C1 | CUT: remove every sentence the first build wrote for the old T2, T3, T4, T5 (STEP-G "trap on every exit" / "leftover lock after a FAILED gate"; "THE EQUAL-TREE CLAUSE, the rule for when it lands"; P1 "The rule for (v) when it lands"; the outage rule's "never a resend"); those places read as at BASE | hub text; `grep -c -F` of each of "trap on every exit", "leftover lock after a FAILED gate", "THE EQUAL-TREE CLAUSE", "The rule for (v) when it lands", "never a resend" → 0; `git diff 44b29c63 -- <file>` touches only P7, STEP-T and STEP-C | the same file |

## NOT IN THIS JOB
- Any file but `DEPLOY-HUB.md`; any allow string.
- The chain's sentences (old T2–T5): card `03d`.
- `BUILD-HUB.md`, `CHECK-HUB.md`: untouched.

## READ
- `reports/deploy-hub-text-decisions-2026-10-03.md` whole; `reports/deploy-hub-02b-grok-read-2026-10-03.md` findings 1–4; `reports/deploy-set2-1003.md` `## DECISIONS`.
- `DEPLOY-HUB.md` on `main` (P7, STEP-T, STEP-C) and at the branch head.

## CHECK ASKS
- X1 Can a real migration slip past T1 (a `.sql` under the folder by any name; a FORWARD entry added, removed or reordered)? Is any `.py`, test or doc under the folder still read as a migration?
- X2 Can a resident plist pass STEP-C (any path under `ops/` outside `ops/desk/`; an `ops/desk/` plist whose Label is a jobs.yaml key)?
- X3 Is `git diff 44b29c63` of the file limited to P7, STEP-T and STEP-C?

## RECORDS
- Judge, 10-03 20:04 (JUDGE ASK 17, check r2 O1/O2 HOLD): T6 as checked r2 O1/O2: labels are label: values in jobs.yaml, the Label string is read on its key line or the next, an unreadable Label is refused.
- Check r2 (`reports/deploy-hub-text-check-2026-10-03-r2.md`) at `69bf6082`: T1 and C1 as written, diff limited to P7, STEP-T, STEP-C; only T6 changes in this re-issue. Its sections sit at `<S>/opus-1-r2.md` (ASK DESK 3, kept); r3 writes `opus-1-r3.md`.
- Judge, 10-03 ~19:50 (JUDGE ASK 16): Grok's 8 findings answered (reports/deploy-hub-text-decisions-2026-10-03.md): 1–4 fixed in the P7, STEP-T and STEP-C sentences; T2–T5 cut from this card and carried to 03d; the card is the P7/T/C fix only.
- Judge (finding 2): no `.sql` test fixture exists under `src/cobalt/db_migrations/` (re-read by the check).
- Judge, 10-03 19:12 (JUDGE ASK 15, build decision T6): ADDED or MODIFIED kept; superseded in wording by JUDGE ASK 16's T6 sentence.
- First build `50bd02d8`, checked ready YES at `59ef8d48` (`reports/deploy-hub-text-check-2026-10-03.md`); this re-issue resumes at E3 on that branch.
- Judge, 10-03: this card ships alone, docs-only, before the `03c` chain and the ports; its other-house read (L67) is Grok on this one file, after the check.
- The `03c` chain (`9694a679`) is then PORTED onto this card's `main` by the brain's `03d` card (the chain's files re-applied; `DEPLOY-HUB.md` = this card's text plus the chain's adoption sentences and the old T2–T5 sentences written against the chain's clauses).
