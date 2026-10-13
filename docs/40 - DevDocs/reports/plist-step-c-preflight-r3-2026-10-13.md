# Preflight r3: card 496 `plist-step-c-1013` — 2026-10-13

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt diff HEAD --stat -- <card 496>`; `log --oneline -4 -- <card>`; `rev-parse --short HEAD` | diff empty; last card commit `74141579` (HEAD), then `17a1f68f`, `48d0dcc4`, `6b96c042` | OK |
| 2 | `grep -n -E "«\|TODO\|TBD\|XXX" <card>` | `:7` only: `BASE: «FILL: 8-hex main tip …»` (the desk's) | OK |
| 3 | FAIL 19: `grep -n -F` the R1379 body against card `:55` and `cto-2026-10-13.md:28` | both lines hold, from `D1 D2 D4 D5 KEEP;` to `run as K2 probes after.`, the same text with the same backticks; only the card's own label prefix `row-15 card 496 2026-10-13 brain:` differs | OK |
| 4 | FAIL 20: `grep -n -F` the R1395 body against card `:56` and `cto-2026-10-13.md:13` | same text, backticks, `no `--deploy-report` flag;` and the final period; prefix `k18-owed 2026-10-13 brain:` is the card's label | OK |
| 5 | FAIL 21: card DF1 `:31`; `grep -n -E "BOOTSTRAP\|LAUNCHD" ops/desk/deploy-card.sh` | DF1: "the desk writes 304's and each deferred card's `## LAUNCHD` line `BOOTSTRAP: deferred` by hand at the deploy card … `deploy-card.sh` stays outside this job"; `:38` bars it; grep prints nothing; no test builds on a copy | OK |
| 6 | FAIL 22: C1 `:25`, DF1 `:31`, BO1 `:32`, B1 `:27`, test (t) | C1: no git write, no `launchctl`, no merge, ONE named write `data/deploy/bootstrap-owed.json` (written at step C, removed by BO1's mode); "the hub types `launchctl bootstrap` at its step 4.6L from L1's generated strings, not this script"; B1 has 4.6L bootstrap; BO1 is a label-only run of 4.6L; (t) "pins the hub step's behaviour, not a string inside the script". C1, DF1, BO1, (t) agree | OK |
| 7 | NOTE 1: card `:33`, `:51` | the K18 case is `:450-463` in both | OK |
| 8 | R1400 line: `grep -n -F "preflight r2 2026-10-13 brain"` card; `cto-2026-10-13.md:8` | card `:57`: `C1 reworded (no git, no launchctl, no merge; one named write, the owed file); the hub types the bootstrap; FAILs 19-21 mechanical`. R1400: ``C1 reworded (no git, no launchctl, no merge; one write, the owed file); hub types `launchctl bootstrap` at 4.6L; FAILs 19-21 mechanical, desk fills `BOOTSTRAP: deferred`; gap-filler: `deploy-card.sh` copies it.`` Differs: `one named write` for `one write`; `the hub types the bootstrap` for ``hub types `launchctl bootstrap` at 4.6L``; the tail after `mechanical` (desk fills, gap-filler) is cut | FAIL |
| 9 | `git diff HEAD --stat` over `ops src/cobalt tests configs/cobalt/smoke configs/cobalt/jobs.yaml .gitignore` and the three prompts files; `git diff --stat 5cb4e8e9 HEAD` over the same | both print nothing: every anchor file equals `HEAD` and equals r2's, so r2 checks 5, 9, 10, 11, 12, 13, 14 (anchors and counts) stand | OK |
| 10 | `grep -n` `DEPLOY-HUB.md` headings; `STANDING-LIST.md`; `CARD.md` | `## STEP-C` `:87` (body `:88`), `## STEP-D1` `:117`, `4.6 ` `:141`, `## STEP-4.7` `:143`, `## STEP-5` `:157`; `STANDING-LIST.md:157` holds `NOT ON THIS LIST, by design: retiring or installing a launchd job`; `CARD.md:135` `## A DEPLOY CARD, IN SHORT` | OK |
| 11 | `grep -n -E "bootstrap-owed\|BOOTSTRAP OWED\|deploy-report"` `deploy-step0.sh`, `desk-launch.sh`, `deploy-card.sh` | nothing: the printer and the file are DF1's, new | OK |
| 12 | every test (a)-(z), card `:25-33` | each names its RED reason on `BASE` (script absent `sh` exit 127, no `4.6L ` line, bootstrap string absent, dry launch exits 0, `checks.py:431-434` detail, `watchdog.py:397` state) or is a PIN: (f), (k), (m), (w), (y), (z). (x) names the failing assertion | OK |
| 13 | allow strings: card against R411, R412 (`cto-2026-10-05.md:107`, `:109`) | the card adds no builder allow string and no new `ops/desk` command; L1's generated strings are per-label `bootout` and `bootstrap` plus an optional exact dry run, no `*` | OK |
| 14 | the card's own deploy: `cto-2026-10-13.md` rows R1381, R1385, R1398, R1401 | no deploy in flight (458 DEPLOYED `2370e58c`). Blocks it: the BASE fill by the desk; seams with card 485 (`desk-launch.sh`) and card 480 (`DEPLOY-HUB.md:32`, `:58`) at the BASE cut; the L68 gate on the merged hub text; one deploy at a time, so 304's recut and 503 wait; OW1 builds after DF1 | OK |

## ISSUES
1. FAIL 8: `## CHECK ASKS` `:57` is not R1400 byte for byte (`cto-2026-10-13.md:8`); put the R1400 body in as written, with the backticks, `hub types`, `one write` and the tail `desk fills `BOOTSTRAP: deferred`; gap-filler: `deploy-card.sh` copies it.`
2. NOTE 1: DF1 says `BOOTSTRAP: deferred` is "a deploy-card header value" and also a `## LAUNCHD` line mode (`add`, `change`, `deferred`, L1); test (o) expects `ADMITTED: … · add` with the deferred line. The builder reads one place; say which.
3. NOTE 2: `watchdog.py`'s reach to a resident is not read (RECORDS `:75`); the builder derives it, so no restart claim is made here.

PREFLIGHT DONE · card: plist-step-c-1013 · checks: 14 · fails: 1 · ready: NO
