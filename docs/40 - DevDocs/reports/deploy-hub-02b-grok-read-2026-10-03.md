# DEPLOY-HUB.md card 02b — other-house read (Grok), 2026-10-03

Reader: Grok `grok-4.7` (`grok --sandbox cobalt-job --disallowed-tools run_terminal_command --allow Read/Write(scratch) -p`), a house other than the author (Opus). Read-only. Prompt `prompts/2026-10-03/28-02b-grok-read.md`. Files: byte-identical `stage-copy.sh` copies of `DEPLOY-HUB.md` at `59ef8d48` (card `02b` checked tip), the same file at BASE `44b29c63` (main), card `02b`, and the chain's file at `9694a679`. Source: `agy-trial/scratch/tribunal-bars-0920/deploy-hub-read-02b/house-a.md`, output verbatim below. First run stopped after one line; the second, with `--allow Read(...)`, finished. No finding has a failing test or command the checker ran (K24); the brain judges them (JUDGE ASK 16).

---

Other-house read of the changed DEPLOY-HUB.md text against base and card 02b, looking for a stalled deploy, residents left down, a held cobalt_dev lock, a migration shipped as code, a resident plist passing STEP-C, or a row the card contradicts.

1. **Line 65** (against base line 65): "a MIGRATION is a file matching `src/cobalt/db_migrations/[0-9][0-9][0-9][0-9]_*.sql` (its `.rollback.sql` twin included) or a change of the `FORWARD` registry in `src/cobalt/db_migrations/__init__.py`; any other path under that folder (`cli.py`, `placement.py`, `dev_rebuild.py`, tests, docs) is CODE and passes `MIGRATIONS: none`."
A `.sql` that misses that glob is "any other path" and passes on a `MIGRATIONS: none` card. `0014.sql`, `014_add.sql`, `0014-add.sql`, and any other file the migrator would apply that lacks four digits and an underscore therefore ship as code: P7 does not fail, STEP-R's "migration with no resident down" does not fire, and 4.4 does not run. A registry edit that is not a changed line inside `FORWARD = (…)` in `__init__.py` slips the same way — `REVERSE` only, `FORWARD +=`, an annotated `FORWARD: … = (`, or a registry module other than `__init__.py`.
`grep -n "any other path under that folder" files/DEPLOY-HUB.md`

2. **Line 65** (against base line 65): "a changed line inside `FORWARD = (…)` is a migration and names only the card's files."
The same P7 rule reads code as a migration. Any path matching `NNNN_*.sql` is a MIGRATION, so a test, fixture, or doc at `src/cobalt/db_migrations/0014_example.sql` does not get the CODE pass the sentence gives "tests, docs". Any changed line inside the tuple, including a comment or a rewrap, is a migration; on a `MIGRATIONS: none` card that line fails P7 and the deploy stalls before STEP-T.
`grep -n "a changed line inside" files/DEPLOY-HUB.md`

3. **Line 85** (against base line 85): "with a migration, the FORWARD check reads only the matching files: `grep -n -F \"MIGRATIONS_DIR / \\\"00\" <GATE>/src/cobalt/db_migrations/__init__.py`"
The new pattern calls every four-digit `NNNN_*.sql` a migration, but this check greps `__init__.py` for the fixed substring `MIGRATIONS_DIR / "00` and never opens those files. A registration of `0100` or any number that does not start with `00` is absent from the only output the sentence accepts, so a card that lawfully names `0100_*.sql` cannot be shown to end `FORWARD` and STEP-T goes `FAILED: T`. A hub that treats a missing hit as "not a migration line" lets that migration's order go unproved.
`grep -n "FORWARD check reads only the matching files" files/DEPLOY-HUB.md`

4. **Line 89** (against base line 89): "STEP-C refuses only a plist under `ops/` ADDED or MODIFIED whose label is in `configs/cobalt/jobs.yaml` or whose path is `ops/<label>.plist`"
Every other added or modified plist under `ops/` passes, not only `ops/desk/`. A new resident plist at `ops/<some other directory>/<file>.plist` whose label is not already in `jobs.yaml` therefore passes STEP-C, which contradicts the card record that only a plist under `ops/desk/` passes. The only named command is `diff --stat`, which does not show the plist `Label`; an `ops/desk/` file whose stem is not a jobs.yaml key also passes when the label inside is a resident such as `com.cobalt.aset`.
`grep -n "STEP-C refuses only a plist" files/DEPLOY-HUB.md`

5. **Line 115** (against base line 115): "When STEP-G runs as one `gate.sh` call (its exit-5 / exit-6 ends included): the release is `gate.sh`'s own trap on every exit; verify `<GATE>/.env` gone and the lock dir absent, then the FAILED line; and a leftover lock after a FAILED gate is the trap's to drop; `gate-clean.sh` removes the worktree."
This file's STEP-G never calls `gate.sh`. The chain's exit 5 is `FAILED: gate — G (b) — cobalt_dev not at 0013`, exit 6 is `DECISION 0: cobalt_dev NOT back at 0013`, a leftover lock is the desk's `DECISION 0`, and the cleaner is `desk-launch.sh recut`, not `gate-clean.sh`. The new clauses put the FAILED line behind a verify that the trap has already dropped `<GATE>/.env` and the lock dir, and they say a leftover lock is not the hub's to drop. On a red gate there is no trap, `gate-clean.sh` is not on this launch line, and the FAILED line cannot be written while the lock dir is still there, so the run stalls with the `cobalt_dev` lock held.
`grep -n "leftover lock after a FAILED gate" files/DEPLOY-HUB.md`

6. **Line 116** (against base line 115, inserted; base has no equal-tree line): "THE EQUAL-TREE CLAUSE, the rule for when it lands (this text has no clause yet): it applies only when the check's three suite lines came from a whole pass 1 (no `--db-only`); otherwise the gate runs whole."
The chain's clause does not say that. It skips (a)–(f) only when there is one TIP branch, the diff from the check's code tip to `<m1>` is docs-only, and the check's stop line has a with-DB count above 0; a `DB: none` branch runs the gate whole. The chain's `--deploy` gate already runs pass 1 without `--db-only`, so "no `--db-only`" is true of every normal chain gate, not the skip condition. Copied onto that clause, the skip fires for a tree that is not equal, and the port is not a copy of the chain sentence.
`grep -n "THE EQUAL-TREE CLAUSE" files/DEPLOY-HUB.md`

7. **Line 59** (against base line 59): "The rule for (v) when it lands (this P1 has (i)–(iv) only): (v) is re-read at STEP-R with `date` then; a non-empty derived set means (v) does not hold, and D2.6's clock rule binds as under (i) or (ii)."
The chain's (v) is an empty restart set and `MIGRATIONS: none`, any hour, provisional; STEP-R re-reads that set and fails only when P1 was already outside (i)–(iv). This sentence never requires `MIGRATIONS: none`, re-reads `date` instead of the set, and rebinds D2.6 to the (i)/(ii) 04:00 ET cutoff for every non-empty set. A Saturday or override deploy that P1 named (iii) or (iv), with any resident in the set, then dies at D2.6 after the gate has taken the lock, and this file's STEP-R has no (v) re-read for that sentence to land on.
`grep -n "re-read at STEP-R" files/DEPLOY-HUB.md`

8. **Line 43** (against base line 43): "Inside the outage (4.1–4.6) a blocked call goes to STEP-5, never a resend."
The chain's launch flag says the opposite: a call the hook blocks is not a refusal and is resent as single calls. This sentence forbids that resend from 4.1 through 4.6, which is while residents are down, and it breaks 4.6's one retry of the same bootstrap (`Bootstrap failed: 5` → retry that one once). A blocked bootstrap is not resent, so the resident is still down when 4.6 is left; the wording is not the chain flag's, so the port is not a copy.
`grep -n "never a resend" files/DEPLOY-HUB.md`

READ DONE · findings: 8
