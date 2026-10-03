JOB: deploy-steps
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/deploy-steps-1003
WORKTREE: deploy-steps-1003
BASE: a09f0862
TIP: 735f5ed8
REPORT: /Users/cobalt/cobalt-wt/deploy-steps-1003/docs/40 - DevDocs/reports/deploy-steps-build-2026-10-03.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-steps-check-2026-10-03.md
HOUSE A: Grok
HOUSE B: as needed
TREE STATE: unchanged
DB: none
RULINGS: 2026-10-02 R47, 2026-10-02 R157

## ROWS

WHY: a deploy's STEP-0 is about 45 typed worker turns, and on 09-30 a session stopped INSIDE the outage with the residents down for 11 minutes. `reports/brain-unattended-2026-10-02.md` E 22: three scripts, one per deploy phase; the outage one brings the residents back on EVERY exit path by a `trap`. His one exception to "no outside house" (direction row 10): this is the script that touches production, so its check has house A = Grok, and it is dry-run once before its first real use. NO fixed file calls these scripts in this job; `DEPLOY-HUB.md` adopts them after the dry run (a later card, the judge's). Every script is POSIX `sh`, `export LC_ALL=C` first, header comment = usage; tested in `tests/ops/` with stubs (`launchctl`, `git`, `curl`, `uv`) on `PATH` that record arguments and answer from a per-test script; NO test touches production, launchd, the real repo or the network.

| row | what | red first | files |
|---|---|---|---|
| D1 | `ops/desk/deploy-step0.sh "<card>"`: STEP-0 of `DEPLOY-HUB.md` as ONE table (`rule · command · exit · output`), read-only: the card's keys and `## SHIPS` rows, each head's check report stop line (`held unfixed: 0`, `ready: YES`, the code tip), `RULINGS` rows proved as `authorize.sh deploy` proves them, `MIGRATIONS` against `git show <head>:src/cobalt/db_migrations/` listings, the window read (P1 (i)–(v) by `date`, naming which holds), the production `launchctl print` census of the residents (pid per label, recorded, not a gate), the free-disk and the `git status` of `/Users/cobalt/cobalt`. Last line `STEP-0 OK — window: <which>` (exit 0) or `FAILED STEP-0: <rule>` (exit 1). It writes nothing but its log | `tests/ops/test_deploy_step0.py`: a tmp repo with a deploy card, two check reports, stub `launchctl` and `date` (via `FAKE_NOW`) → the table and `STEP-0 OK — window: (iii)`; a `ready: NO` report, a `MIGRATIONS` mismatch, a `RULINGS` row without `APPROVED`, a weekday 14:00 with no override → `FAILED STEP-0` naming the rule. RED on `BASE`: no such file | `ops/desk/deploy-step0.sh`, `tests/ops/test_deploy_step0.py` |
| D2 | `ops/desk/deploy-outage.sh "<card>" <restart set, comma-separated labels>`: the outage as ONE script. In order: `date` inside the window again (else `REFUSED`, nothing down); each label in the set goes down and up the way `DEPLOY-HUB.md` 4.2 / 4.6 does it today: `com.cobalt.agent` by `cobalt.sh stop` and `launchctl kickstart gui/<uid>/com.cobalt.agent`; every other label by `launchctl bootout` and `launchctl bootstrap`; the trap brings each back by its own way (each down recorded); the merge is NOT here (the hub merged before the outage: L54 as the hub orders it — the script is given the state `MERGED` or `NOT MERGED` as its third argument and refuses `NOT MERGED`); `cobalt.sh status` → ONLINE. A `trap` on EXIT, INT, TERM, HUP: every label taken down and not yet back is brought back by its own way, then the trap reports `RESIDENTS UP (trap)`. Prints one line per label with its pid before and after, the outage's length in seconds, `OUTAGE DONE <seconds>s` or `FAILED OUTAGE: <label> — <reason> · residents: <up or down list>`. Never touches a label outside the set | `tests/ops/test_deploy_outage.py`, stub `launchctl` recording calls and answering pids: the happy path's order (bootout all, bootstrap all, status); a `bootstrap` that fails for one label → `FAILED OUTAGE` and the trap still bootstraps the rest; a `kill -TERM` of the script between bootout and bootstrap (the test sends it) → every label bootstrapped by the trap, `RESIDENTS UP (trap)`; `NOT MERGED` → `REFUSED`, no `launchctl` call; a label outside the set never appears in the call log; a set holding `com.cobalt.agent` → the stub log shows `cobalt.sh stop` and a `kickstart` for it, `bootout`/`bootstrap` for the others, in order. RED on `BASE`: no such file | `ops/desk/deploy-outage.sh`, `tests/ops/test_deploy_outage.py` |
| D3 | `ops/desk/deploy-smoke.sh "<card>"`: the `## SMOKE READS` and `## MARKERS` rows of the card, each run as typed (`ls`, `grep -c -F`, `curl` with three tries, the census reads), `before` / `after` compared where the card gives both; one line per row `<label> · <command> · <output> · GREEN|RED|census`; last line `SMOKE GREEN` or `SMOKE RED: <labels>`. A production `db query` row runs only when the card's `MIGRATIONS` is not `none` and carries no `%` | `tests/ops/test_deploy_smoke.py`: a card with four smoke rows and two markers, stubs for `curl` (200 on the third try) and files on a tmp root → `SMOKE GREEN` with every line; a marker whose `after` differs → `SMOKE RED`; a `db query` row on a `MIGRATIONS: none` card → the row is skipped and said. RED on `BASE`: no such file | `ops/desk/deploy-smoke.sh`, `tests/ops/test_deploy_smoke.py` |
| D4 | THE DRY RUN, documented: each script accepts `--dry-run` and prints every command it WOULD run, in order, running none (`launchctl`, `git`, `curl` never called). The header of each names the dry-run line the desk types once before the first real use. RUN — asserts nothing beyond the tests: quote the three `--dry-run` outputs on `prompts/2026-10-02/25-deploy-scripts-card.md` (the real card of the 10-02 night deploy, read-only, no production call is made by a dry run) | in each test file: `--dry-run` → no stub called, the would-run lines printed | the three scripts, their tests |
| D5 | NO TEST REACHES THE REAL LAUNCHD OR A HOUSE. New `tests/ops/conftest.py` with an autouse fixture that prepends to `PATH` a tmp bin holding stand-ins named `launchctl`, `codex`, `grok`, `agy`, `curl`, each printing `REAL <name> REACHED BY A TEST` on stderr and exiting 127; a test that needs a stub of its own prepends it ahead, as today. Every existing `tests/ops` test still passes (the stubs they place take precedence) | `tests/ops/test_conftest_guard.py`: a test that calls `launchctl` through a script with no stub → exit 127 and the sentence; the whole `tests/ops` run green. RED on `BASE`: `/bin/launchctl` answers | `tests/ops/conftest.py`, `tests/ops/test_conftest_guard.py` |

## NOT IN THIS JOB
- `DEPLOY-HUB.md`: not edited; the hub keeps typing its steps until a later card adopts the scripts after the desk's dry run.
- A real run of any script: `launchctl`, `curl` and production strings are not on your line; the scripts run only through their tests and `--dry-run`.
- The merge, the revert, the tag: the hub's (L54, L55); `deploy-card.sh` (card `18`).
- Any resident outside the derived restart set; the window law itself (P1's text is card `02`'s).

## READ
- `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` whole: STEP-0, P1, STEP-D (the outage steps D2.x), STEP-5, the smoke rows; every rule the scripts mirror is there, and nothing else may be mirrored.
- `reports/deploy-2026-09-30-1-attempt1.md` … `-attempt3.md` and `reports/deploy-2026-10-01-1.md`: what a stopped outage and a failed gate looked like.
- `reports/brain-unattended-2026-10-02.md` E 22; `## THE STANDARD` 6, 9.
- `prompts/2026-10-02/25-deploy-scripts-card.md`: a real deploy card for D4's dry run.
- `ops/desk/authorize.sh`, `ops/desk/gate-clean.sh`, `ops/desk/deploy-card.sh` headers at `BASE`.

## CHECK ASKS
- X1 Is there ANY exit path of `deploy-outage.sh` — a signal, a failed command, a missing stub, a bad argument after the first bootout — that leaves a resident of the set down? Write the test.
- X2 Can a script run a production-touching command in `--dry-run`? Can one touch a label not in the set, or run when the state is `NOT MERGED`?
- X3 Does `deploy-step0.sh` mirror a rule DEPLOY-HUB.md does not have, or miss one it has (read both side by side)?
- X4 Is any rule of the window (P1 (i)–(v)) read differently by the script than by the hub text at this tip?

## RECORDS
- `DB: none`: every file is under `ops/` or `tests/ops/`.
- House A = Grok by his word (direction row 10 and `## HIS WORDS`: "We should run an outside Grok check for only one that touches production as well"); one Grok hub at a time (L15): the desk serialises this check with the other-house read of card `02`'s `DEPLOY-HUB.md` part.
- The dry run before first use is the desk's step after DEPLOYED, recorded in the desk report; the adoption of the three scripts into `DEPLOY-HUB.md` is a later card the judge writes after reading the dry run.
- FOR THE CHECK: Build decisions 1–6 answered by the judge: D1 closed on the desk's launchctl read and recorded for Dejan at DONE; rows D5 and D2-amended added (no test reaches the real launchd or a house; the agent label goes down and up as the hub does it); D2, D3, D4, D5, D6 KEEP; the inner-step argument is the adoption card's. Desk reading: in D2 the merge clause between the down and up steps stands unchanged.
