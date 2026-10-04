# Card 03d preflight — round 2 (2026-10-03)

Card: `prompts/2026-10-03/03d-adoption-port-card.md`

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `merge-base --is-ancestor a8d8a848 main`; `rev-parse --verify 9694a679^{commit}`; `… a09f0862^{commit}` | exit 0, no output; `9694a6793d02eabe612a9e224d592f0bc8c3e6f5`; `a09f08622ac8522adce99096f5af18faaed9e2ca` | OK |
| 2 | `rev-parse --verify ops/adoption-port-1003`; `ls /Users/cobalt/cobalt-wt/adoption-port-1003` | `fatal: Needed a single revision` (exit 128); `No such file or directory` | OK |
| 3 | `diff --name-only a09f0862 9694a679` (chain, 50 paths) and `… a09f0862 a8d8a848` (main, 66 paths); `--diff-filter=D` on the chain | Chain: 3 reports, `cobalt/db_migrations/cli.md`, `BUILD-HUB`, `CARD`, `CHECK-HUB`, `CTO-DESK-WAKEUP`, `DEPLOY-HUB`, `DEVFIX-HUB`, `STANDING-LIST`, 26 `ops/desk/*`, `src/cobalt/db_migrations/cli.py`, 2 `tests/cobalt/*` (`test_migrate_level.py`, `test_migrate_proof.py`), 17 `tests/ops/*`. Main: `restarts.md`, 2026-10-03 cards, reports, `CTO-DESK-WAKEUP`, `DEPLOY-HUB`, 3 `ops/desk/deploy-*.sh`, `restarts.py`, `tests/cobalt/test_jobs_restarts.py`, 5 `tests/ops/*` (`conftest.py`, `test_conftest_guard`, `test_deploy_*`). Intersection = `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` (P3), `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (P2). Deletions by the chain: none (empty output). | OK |
| 4 | `rev-parse --verify 9694a679:tests/cobalt/test_migrate_level.py`; `grep -n -E "test_db_only_selection\|conftest"` on the card | `4ecdc56180d82ae471555e138a090e4adebb2aea` (in check 3's chain list: yes). Grep: `16:WHY: … With-DB job (`cli.py`, `conftest.py` are in the chain): it takes the lock.` No `test_db_only_selection`. `tests/ops/conftest.py` is not in the chain list (it is a main file). | FAIL |
| 5 | decisions file items 5–8 vs the card's sentences; chain `DEPLOY-HUB.md` at `9694a679` | Items 5–8 exist (lines 11–14). 6: one TIP branch, docs-only diff from the check's code tip, with-DB count > 0, else gate whole → card (6) carries it. 7: empty restart set AND MIGRATIONS none, provisional at P1, SET re-read at STEP-R → card (7) carries it. 8: resend once as single calls, still blocked → STEP-5 → card (8) carries it. 5: the row only says T2 is cut and "the chain's sentence is 03d's" (no further ruled text); card (5) (release is gate.sh's trap on every exit; verify `.env` gone and lock dir absent, then the FAILED line) contradicts nothing. Chain clauses: l.102 `- THE GATE, ONE CALL: `ls -la <GATE>/.env` (No such file) · `sh /Users/cobalt/…` (exits 4/5/6 in that bullet); l.99 `THE EQUAL-TREE CLAUSE (before (a)): ONE branch in TIP, and `git -C /Users/cobalt/cobalt diff --st…`; l.57 `- **P1 DATE AND WINDOW**: `date`. Lawful when ONE of these holds; …` with (v) there, and l.93 `- P1 (v) RE-READ: when P1 named `(v) provisional`, the derived `<restart set>` …`; l.11 `claude --bg "Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md' and follow it exactly. CARD: '<card>'" …` (flag text ends "…resend it as single calls." after `--append-system-prompt`). | OK |
| 6 | `ls` of the four READ files; `grep -n "^## §0"` | all four exist; `3:## §0 Headline` | OK |
| 7 | `grep -n` R47, R154, R157 in `cto-2026-10-02.md`; R3 in `cto-2026-10-03.md` | R47 (l.54): `HIS RULING · APPROVED`; R154 (l.161): `HIS RULING · APPROVED`; R157 (l.164): `HIS RULING · APPROVED`; R3 (l.9): `HIS RULING · APPROVED — pending fold` | OK |
| 8 | `grep -n` of `restarts.py` at `main`; `## RESTARTS` of `03`'s build report at `9694a679` | `ops/desk/*` → `restarts.py:38 OPS_DESK_PREFIX = "ops/desk/"` holds. `tests/*` cite `:239` does NOT hold: l.239 is `continue` (META rule); the `test/documentation; no resident` rule is l.245–246. `docs/**` cite `:219` does NOT hold: l.219 is `restarts.update(matched)`; the DOCS rule is l.225–228 (`ROOT_DOCS` l.15). `cli.py` home: build report l.165 `…`src/cobalt/db_migrations/cli.py M static import reach com.cobalt.radar`. No `UNCLASSIFIED` row. Last line: `RESTARTS: com.cobalt.radar`.` | FAIL |
| 9 | `HOUSE B` line; `grep -c -F "«FILL"` | `HOUSE B: as needed` (filled); count `0` | OK |

## ISSUES
- Check 4: card line 16 still says "`cli.py`, `conftest.py` are in the chain"; `tests/ops/conftest.py` is a main file, not in `a09f0862..9694a679`. Drop `conftest.py` there.
- Check 8: the RESTARTS homes line cites `restarts.py:239` for tests (rule is at `:245`–`:246`) and `:219` for docs (rule is at `:225`–`:228`); both cites are wrong at `main`.

PREFLIGHT DONE · card: 03d · checks: 9 · fails: 2 · ready: NO
