# Card 03d adoption-port — preflight (2026-10-03, seat 03d-preflight, read-only)

Card: `prompts/2026-10-03/03d-adoption-port-card.md`

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor a8d8a848 main` | exit 0, no output | OK |
| 1 | `rev-parse --verify 9694a679^{commit}` / `a09f0862^{commit}` | `9694a6793d02eabe612a9e224d592f0bc8c3e6f5` / `a09f08622ac8522adce99096f5af18faaed9e2ca` | OK |
| 2 | `rev-parse --verify ops/adoption-port-1003` | `fatal: Needed a single revision` (exit 128) — branch absent | OK |
| 2 | `ls /Users/cobalt/cobalt-wt/adoption-port-1003` | `No such file or directory` | OK |
| 3 | `diff --name-only a09f0862 9694a679` (chain, 49 paths) | `cobalt/db_migrations/cli.md`; `prompts/{BUILD-HUB,CARD,CHECK-HUB,CTO-DESK-WAKEUP,DEPLOY-HUB,DEVFIX-HUB,STANDING-LIST}.md`; 3 `reports/adoption-*-build` files; 26 `ops/desk/*` (authorize.sh … wait-stop-line.sh, gate-lists.md); `src/cobalt/db_migrations/cli.py`; `tests/cobalt/test_migrate_{level,proof}.py`; 17 `tests/ops/test_*.py` | — |
| 3 | `diff --name-only a09f0862 a8d8a848` (main, 56 paths) | restarts.md, 02b/… cards, reports, `ops/desk/deploy-{outage,smoke,step0}.sh`, `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py`, `tests/ops/conftest.py`, 5 deploy tests, plus `prompts/CTO-DESK-WAKEUP.md`, `prompts/DEPLOY-HUB.md` | — |
| 3 | intersection (merge-base of the two is `a09f0862`) | **`docs/40 - DevDocs/prompts/DEPLOY-HUB.md` AND `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`**. Card says DEPLOY-HUB.md only | **FAIL** (CTO-DESK-WAKEUP.md) |
| 3 | `diff --diff-filter=D --name-only a09f0862 9694a679` | empty — the chain deletes no path | OK |
| 4 | `ls-tree -r 9694a679 tests`; `diff --stat a09f0862 9694a679 -- tests/cobalt/conftest.py tests/cobalt/test_db_only_selection.py` | `tests/cobalt/test_migrate_level.py` and `tests/cobalt/test_db_only_selection.py` both exist at `9694a679`. `test_migrate_level.py` is in the chain diff. `test_db_only_selection.py` and `tests/cobalt/conftest.py` are NOT (empty diff: identical at `a09f0862`, hence at BASE). The card's WHY says `conftest.py` is in the chain; it is not | **FAIL** (card claims, see ISSUES) |
| 5 | decisions file items 5–8 (lines 11–14) vs the card's four sentences | the file's items 5–8 hold only CUT notes and paraphrases, not the card's sentences. Item 5: `removed from 02b; the chain's sentence is 03d's` (no sentence). Item 6: `one TIP branch, docs-only diff from the check's code tip, with-DB count above 0, else the gate whole` (paraphrase). Item 7: `(v) = empty restart set AND MIGRATIONS none, provisional at P1, the SET re-read at STEP-R`. Item 8: `inside the outage a blocked call is resent once as single calls; still blocked → STEP-5` vs card `Inside the outage (4.1–4.6) a blocked call is resent once as single calls; still blocked → STEP-5.` — words differ (`(4.1–4.6)`, capital I) | **FAIL** items 5, 6, 7, 8 |
| 5 | chain `DEPLOY-HUB.md` at `9694a679`, lines | l.102 the gate-call bullet `- THE GATE, ONE CALL: \`ls -la <GATE>/.env\` (No such file) · \`sh /Users/cobalt/cob…` holds the exit text inline `EXIT 4 → … 5 → \`FAILED: gate — G (b) — cobalt_dev not at 0013 … 6 → \`DECISION 0: cobalt_dev NOT back at 0013 …` (exits 5 and 6 are two different outcomes, there is no "exit-5/6 bullet" ending the sentence the card replaces); l.99 `THE EQUAL-TREE CLAUSE (before (a)): ONE branch in TIP, and \`git -C /Users/cobalt/cobalt diff --stat <its ch…` (ends with the with-DB count above 0 sentence — already present); l.57 `(v) a set whose MIGRATIONS is none and whose derived restart se…`; l.11 launch line `claude --bg "Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md' and follow…`, its flag text ends `A call the hook blocks is NOT A REFUSAL: resend it as single calls.` | OK (all four anchors exist; mismatches noted above) |
| 5 | `grep -n -F 'MIGRATIONS_DIR / "00' DEPLOY-HUB.md` on `main` | no hit (already `MIGRATIONS_DIR / "` from 02b) | OK |
| 6 | `ls` of the four READ files; `grep -n "^## §0"` in `adoption-scripts-b-check-2026-10-03.md` | all four exist; `3:## §0 Headline` | OK |
| 7 | R47 (cto-2026-10-02 l.54) | `HIS RULING · APPROVED` | OK |
| 7 | R154 (l.161) | `HIS RULING · APPROVED` | OK |
| 7 | R157 (l.164) | `HIS RULING · APPROVED` | OK |
| 7 | R3 (cto-2026-10-03 l.9) | `HIS RULING · APPROVED — pending fold` | OK |
| 8 | `grep -n -E "ops/desk\|db_migrations\|\"tests/" configs/cobalt/jobs.yaml`; card `## RECORDS` | no hit in jobs.yaml for `ops/desk/*`, `src/cobalt/db_migrations/cli.py` or `tests/*`; the card's `## RECORDS` names no restart class home for any of them | **FAIL** (all non-docs chain paths: `ops/desk/*` ×26, `src/cobalt/db_migrations/cli.py`, `tests/cobalt/test_migrate_*.py`, `tests/ops/test_*.py` ×17) |
| 9 | `grep -n -E "^HOUSE B"` on the card | `10:HOUSE B:` — EMPTY (the launch script refused an empty HOUSE B on 10-03 07:40) | FAIL |
| 9 | `grep -c -F "«FILL"` on the card | `0` | OK |

Checks run: 9 (checks 3, 4, 5, 8, 9 fail; the issues below).

## ISSUES

- FAIL 3: `prompts/CTO-DESK-WAKEUP.md` is touched by both the chain and main (besides `DEPLOY-HUB.md`); needs a hand merge the card does not give.
- FAIL 4: `test_db_only_selection.py` and `tests/cobalt/conftest.py` are not chain files (identical at `a09f0862`/BASE), so the card's "chain files incl. `conftest.py`" and red-on-BASE for that test do not hold as stated; only `test_migrate_level.py` is a chain test.
- FAIL 5: the decisions file items 5–8 carry no sentence word-for-word; item 8 differs from the card's flag text (`(4.1–4.6)`, capital `Inside`). Item 5's "exit-5/6 bullet" is not one bullet in the chain text (exits 5 and 6 have separate outcomes in the l.102 bullet).
- FAIL 8: no restart class home (jobs.yaml or card `## RECORDS`) for any non-docs chain path (`ops/desk/*`, `cli.py`, tests).
- FAIL 9: `HOUSE B` is empty; the launch script will refuse it.

PREFLIGHT DONE · card: 03d · checks: 9 · fails: 5 · ready: NO
