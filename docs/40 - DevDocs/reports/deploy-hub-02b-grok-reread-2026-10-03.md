# DEPLOY-HUB.md card 02b — other-house RE-READ (Grok), 2026-10-03

Reader: Grok `grok-4.7`, read-only, prompt `prompts/2026-10-03/30-02b-grok-reread.md`; staged copies of `DEPLOY-HUB.md` at `2cc6330e` (check r3 ready YES), the same at BASE `44b29c63`, card `02b`, `jobs.yaml`. Source: `agy-trial/scratch/tribunal-bars-0920/deploy-hub-read-02b-r2/house-a.md`, verbatim below. The brain judges them (JUDGE ASK 18).

---

Re-read of the changed P7, STEP-T, and STEP-C sentences against the base, for a real migration shipping as code, code read as a migration, a missed FORWARD registration, a resident plist passing STEP-C, or a stalled deploy.

1. **Line 85** (against base line 85). "adds, removes or reorders an entry) EXACTLY the files of `MIGRATIONS` and the registry files they edit, or no migration path when `none`; every `.py`, test and doc under that folder is CODE and passes; when `__init__.py` is in that stat, `git -C /Users/cobalt/cobalt diff <m0> <BRANCH> -- src/cobalt/db_migrations/__init__.py` → a changed line inside `FORWARD = (…)` that adds, removes or reorders an entry is a migration and names only the card's files; with a migration, the FORWARD check: `grep -n -F 'MIGRATIONS_DIR / "' <GATE>/src/cobalt/db_migrations/__init__.py` → `FORWARD` ends with the card's numbers in order and `REVERSE` begins with them reversed."

The same sentence now calls a FORWARD remove or reorder a migration, and line 65 calls every `.sql` a migration whatever its name, but the only proof that follows is that FORWARD ends with the card's numbers and REVERSE begins with those numbers reversed. Removing an entry leaves that number absent, and a reorder that is not itself the new suffix leaves FORWARD ending with the old tail, so `Anything else → FAILED` stalls the deploy. A name with no digits (`backfill.sql`, the case the dropped `[0-9]…_*.sql` rule was rewritten to catch) has no "numbers" for that grep to prove: the run either stalls on a correct registration or, if an empty number list is treated as already satisfied, never checks that FORWARD gained the file.

`grep -n -F "ends with the card's numbers" files/DEPLOY-HUB.md`

2. **Line 65** (against base line 65). "or a changed line inside FORWARD = (…) of src/cobalt/db_migrations/__init__.py that adds, removes or reorders an entry; every .py under that folder (cli.py, placement.py, dev_rebuild.py), tests and docs are CODE and pass MIGRATIONS: none."

That registry file also has `REVERSE = (MIGRATIONS_DIR / "….rollback.sql", …)`, and rollback order is part of the migration. A changed line that adds, removes, or reorders a REVERSE entry is not inside `FORWARD = (…)`, and `__init__.py` is a `.py`, so the new sentence calls it CODE and passes `MIGRATIONS: none`. Base line 65 failed any `__init__.py` in the stat when the card said none; this wording lets the rollback registry change through. Line 85 runs `grep -n -F 'MIGRATIONS_DIR / "'` only "with a migration", so STEP-T never checks that registration.

`grep -n -F "inside FORWARD" files/DEPLOY-HUB.md`

READ DONE · findings: 2
