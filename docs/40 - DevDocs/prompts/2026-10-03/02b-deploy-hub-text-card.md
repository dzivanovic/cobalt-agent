JOB: deploy-hub-text
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/deploy-hub-text-1003
WORKTREE: deploy-hub-text-1003
BASE: 44b29c63
TIP: 50bd02d8
REPORT: /Users/cobalt/cobalt-wt/deploy-hub-text-1003/docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-hub-text-check-2026-10-03.md
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B: as needed
TREE STATE: unchanged
DB: none
RULINGS: 2026-10-02 R47, 2026-10-02 R154, 2026-10-02 R157

## ROWS

WHY: `DEPLOY-HUB.md` on `main` is the text every deploy runs under until a new text lands. Two things block the next sets: P7 and STEP-T read any path under `src/cobalt/db_migrations/` as a migration, so the `03c` chain's `cli.py` (command code, no schema) cannot ship (`deploy-set2-1003.md` DECISIONS); and Grok's read of the chain's new text (`deploy-hub-other-house-read-2026-10-03.md`) holds five text findings the judge upheld. This card edits `main`'s `DEPLOY-HUB.md` only; the chain's version of the file (card `02`) gets the same five sentences when `03c` is ported onto this card's `main` — the port carries them. Docs only: one file, `DB: none`, no restart, deploys at any hour; its deploy runs under the text it replaces, which is fine for a docs-only set.

| row | what | red first | files |
|---|---|---|---|
| T1 | P7 and STEP-T: a MIGRATION is a file matching `src/cobalt/db_migrations/[0-9][0-9][0-9][0-9]_*.sql` (its `.rollback.sql` twin included) or a change of the FORWARD registry in `src/cobalt/db_migrations/__init__.py`; any other path under that folder (`cli.py`, `placement.py`, `dev_rebuild.py`, tests, docs) is CODE and passes `MIGRATIONS: none`. The two sentences name the pattern; STEP-T's FORWARD check reads only the matching files | no test: hub text; `grep -n -F` of the pattern → two hits (P7, STEP-T) | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` |
| T2 | Grok finding 1 and 3: the STEP-G exit-5 / exit-6 bullet ends "the release is `gate.sh`'s own trap on every exit; verify `<GATE>/.env` gone and the lock dir absent, then the FAILED line"; and "a leftover lock after a FAILED gate is the trap's to drop; `gate-clean.sh` removes the worktree". (The bullet exists only in the chain's text; on `main`'s text this row writes both sentences at STEP-G's red path, the bullet starting "A red anywhere" (line 115 at BASE), so the port has nothing to invent) | hub text; `grep -c -F "trap on every exit"` → 1 | the same file |
| T3 | Grok finding 2: the equal-tree clause (where present) reads "applies only when the check's three suite lines came from a whole pass 1 (no `--db-only`); otherwise the gate runs whole". On `main`'s text, which has no clause yet, the sentence is written under STEP-G as the rule for when the clause lands | hub text; one hit | the same file |
| T4 | Grok finding 4: P1 (v) — "re-read at STEP-R with `date` then; a non-empty derived set means (v) does not hold, and D2.6's clock rule binds as under (i) or (ii)". On `main`'s text, whose P1 has (i)–(iv) only (line 59 at BASE), the sentence is written at the end of P1 as the rule for when (v) lands, as T3 does | hub text; one hit | the same file |
| T6 | STEP-C: a plist added under `ops/desk/` is a FILE of the tree, not a resident (nothing loads it but his install by hand; `restarts.py`'s `OPS_DESK_PREFIX` classes it as an operator script); STEP-C refuses only a plist added under `ops/` whose label is in `configs/cobalt/jobs.yaml` or whose path is `ops/<label>.plist` (the launchd install path). The sentence names the rule (deploy set 2b FAILED STEP-C, card `05`) | hub text; one hit | the same file |
| T5 | Grok finding 5: the deploy launch line's flag text gains "Inside the outage (4.1–4.6) a blocked call goes to STEP-5, never a resend." (the flag exists only on the chain's line; on `main`'s line, which has no flag yet, the sentence goes into the outage rule, the bullet starting "INSIDE THE OUTAGE" (line 43 at BASE), so the port keeps it) | hub text; one hit | the same file |

## NOT IN THIS JOB
- Any file but `DEPLOY-HUB.md`; any allow string (Grok's 6–9 are his class strings and pre-existing strings; the Sunday guard narrows by hook).
- `BUILD-HUB.md`, `CHECK-HUB.md`: untouched.

## READ
- `reports/deploy-set2-1003.md` `## DECISIONS`; `reports/deploy-hub-other-house-read-2026-10-03.md` findings 1–5; `reports/adoption-hubs-decisions-2026-10-03.md` items 5, 6, 7.
- `DEPLOY-HUB.md` on `main` (P1, P7, STEP-G, STEP-R, STEP-T, STEP-C, the outage rule at line 43) and the chain's version at `9694a679` (so the five sentences read the same in both).

## CHECK ASKS
- X1 Can a real migration file slip past T1's pattern (a `.sql` without the four digits, a registry change outside `__init__.py`)? Can code under the folder still be read as a migration?
- X2 Does each of T2–T5 say the same thing as the chain's version will, so the port is a copy?

## RECORDS
- Judge, 10-03 19:12 (JUDGE ASK 15, build decision T6): T6 keeps main's ADDED or MODIFIED for a plist under ops/<label>.plist or a jobs.yaml label; only a plist under ops/desk/ passes STEP-C as a tree file.
- Judge, 10-03 (deploy set 2 FAILED PREFLIGHT; Grok read): this card ships alone, docs-only, before the `03c` chain and the ports; its other-house read (L67) is Grok on this one file, after the check.
- The `03c` chain (`9694a679`) is then PORTED onto this card's `main` by the brain's `03d` card (the chain's files re-applied; `DEPLOY-HUB.md` = this card's text plus the chain's adoption sentences).
