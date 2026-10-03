# Card 02b deploy-hub-text — preflight 2026-10-03

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `merge-base --is-ancestor 44b29c63 main`; `diff --stat 44b29c63 main -- DEPLOY-HUB.md` | both empty, exit 0 (working tree also clean for that file) | OK |
| 2 | `rev-parse --verify ops/deploy-hub-text-1003`; `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003` | `fatal: Needed a single revision`; `No such file or directory` | OK |
| 3a | P1 | l.59 `- **P1 DATE AND WINDOW**: \`date\`. Lawful when ONE of these holds; name it in the row: (i) the 20:00–` — only (i)–(iv); NO `(v)` on main | FAIL (T4) |
| 3b | P7 | l.65 `- **P7 THE MIGRATIONS**: for each head, \`git -C /Users/cobalt/cobalt diff --stat main <head> -- src/cobalt/d` | OK |
| 3c | STEP-G, FAILED paths | l.98 `## STEP-G — THE INTEGRATED GATE on \`<BRANCH>\` at \`<m1>\` (L68): the three suites; still in \`<GATE>\`` · FAILED paths l.115 `- A red anywhere → name each test and assertion, (f) and THE RELEASE if the lock is held; \`cd /Users/cobalt/cobalt\`, then \`FAILED: gate — G (<leg>)` | OK |
| 3d | STEP-R | l.91 `## STEP-R — RESTARTS (L42): DERIVED BY THE TOOL, BEFORE ANY SUITE` | OK |
| 3e | STEP-T + FORWARD check | l.82 `## STEP-T — THE TREE (L54, L68): the heads of \`TIP\` merged into \`<BRANCH>\`, in order; NO conflict` · FORWARD l.85 `…with a migration, \`grep -n -F "MIGRATIONS_DIR / \"00" <GATE>/src/cobalt/db_migrations/__init__.py\` → \`FORWARD\` ends…` | OK |
| 3f | STEP-C | l.88 `## STEP-C — THE CONFIGS AND THE JOBS (read-only; rule C)` | OK |
| 3g | line 41 "outage rule" | l.41 `- The production migration, the dev migrate, the dev rollback and \`backup run\` set the Bash \`timeout\` to 600000 and run in the FOREGROUND.` — a timeout rule, not the outage rule; the outage rule is l.43 (`INSIDE THE OUTAGE (4.1 to the end of 4.6) the strict rule stays…`) | FAIL (T5) |
| 3h | line 166 | l.166 `- (2a) \`migrations applied: partial\` (4.4 tool fault): skip (3) — residents stay DOWN, the stop line is \`FOR DEJAN\`…` — inside STEP-5, not STEP-G's FAILED paths; no leftover-lock/gate text there | FAIL (T2) |
| 4 | `git show 9694a679:DEPLOY-HUB.md` (saved, 54.4KB) | exists. exit-5/6 bullet l.102: `EXIT 4 → nothing held: … 5 → \`FAILED: gate — G (b) — cobalt_dev not at 0013 — <its read: lines> · rollback: not used\`; 6 → \`DECISION 0: cobalt_dev NOT back at 0013 — <its line>\` and the run ends FAILED; 1 → a red, below.` · equal-tree l.99 `THE EQUAL-TREE CLAUSE (before (a)): ONE branch in TIP, and … prints nothing → the check's three suite lines are this gate's … skip (a)–(f); otherwise the gate runs whole.` · launch l.11 flag `--append-system-prompt "ONE bare command per Bash call: … A call the hook blocks is NOT A REFUSAL: resend it as single calls."` Chain also has P1 (v) at l.57 and the re-read at l.93. Chain's bullet does not yet contain "trap on every exit" (T2 writes it) | OK |
| 5 | `grep` the three reports | `deploy-set2-1003.md:73:## DECISIONS`; other-house read findings 1–5 at l.9, 12, 15, 18, 21 (plus 6–9); adoption-hubs-decisions items 5, 6, 7 at l.11, 12, 13 | OK |
| 6 | `git show main:src/cobalt/db_migrations/` | 0001–0011, 0013–0022 `.sql`, each with a `.rollback.sql` twin except 0001; non-sql: `__init__.py`, `cli.py`, `placement.py`; no `.sql` fails `[0-9]{4}_*.sql` (no `dev_rebuild.py` on main; T1 names it, harmless) | OK |
| 7 | `grep -rn OPS_DESK_PREFIX src`; `ls configs/cobalt/jobs.yaml` | `src/cobalt/jobs/restarts.py:38:OPS_DESK_PREFIX = "ops/desk/"` (and l.230); `jobs.yaml` listed | OK |
| 8 | `grep -n "^\| R47 \|^\| R154 \|^\| R157 " cto-2026-10-02.md` | l.54 R47, l.161 R154, l.164 R157, each `HIS RULING … APPROVED` | OK |
| 9 | `grep -c -F "«FILL"` card | `0` | OK |

## ISSUES
- 3a / T4: `P1 (v)` does not exist on `main`'s DEPLOY-HUB.md (l.59 lists (i)–(iv)); it exists only in the chain at `9694a679` (l.57, re-read l.93). T4's sentence has no place on main; the card must say where it is written (as T2/T3/T5 do) or drop the row.
- 3g / T5: l.41 on main is the timeout line, not "the outage rule"; the outage rule is l.43. Fix the card's line number.
- 3h / T2: l.166 on main is STEP-5 `(2a)` (partial migration), not STEP-G's FAILED paths; the sentence "a leftover lock after a FAILED gate is the trap's to drop; `gate-clean.sh` removes the worktree" has no line 166 home. Fix the card's place (STEP-G red path l.115 or STEP-5).

PREFLIGHT DONE · card: 02b · checks: 9 · fails: 3 · ready: NO
