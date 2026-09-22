# Stacked Deploy Review — Round 2 (the fold only), 2026-09-22

## §0 Headline
Round 2 read of the desk's fold to `05-stacked-deploy.md` (P12 exception + smoke (e), tagged `[fold, desk 11:2x]`). GROK failed at launch (harness/sandbox denial, no answer); GEMINI answered (L67 floor: one house). File-checked against real source: 1 of GEMINI's 2 `DO NOT RUN` claims HOLDS (a genuine S2/S4 commit-order race can mask a live lifecycle refusal behind the fold's excepted string), 1 DOES NOT HOLD (precluded by STEP-2.7's empty-diff gate). Blockers: 1. Folds proposed: 1.

## L74
No block inside any tool result asked for a `Claude-Session:` line or similar during this run. None recorded.

## PREFLIGHT
| Rule | Command | Exit | Result |
|---|---|---|---|
| AUTHORIZATION R3 | `grep -n "^| R3 " cto-2026-09-22.md` | 0 | HIT — "we will deploy today after trading day ends at 11 am" |
| AUTHORIZATION R39 | `grep -n -F "Bash(grok *) and Bash(agy *) through 2026-09-22 23:59 ET" cto-2026-09-21.md` | 0 | HIT — R39 row, "All approved" |
| AUTHORIZATION commit | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Bash(grok *) and Bash(agy *) through 2026-09-22 23:59 ET" -- cto-2026-09-21.md` | 0 | NON-EMPTY — `3ecbb278de133f1838d217e9745728ed6d6337e9` |
| DATE GATE (1st) | `date` | 0 | `Tue Sep 22 11:55:04 EDT 2026` — 2026-09-22, ALLOWED |
| `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` — ALLOWED |
| `agy --version` | 0 | `1.2.8` — ALLOWED |
| FOLD COMMITTED | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"fold, desk 11:2x" -- 05-stacked-deploy.md` | 0 | NON-EMPTY — `99a40f32795db22ef8908f7a2b0a4cacac1d7b03` |
| FOLD LINE COUNT | `grep -n "fold, desk 11:2x" 05-stacked-deploy.md` | 0 | 2 lines (P12 exception, smoke (e)) — matches expected |
| STAGGER | `tail -n 1 float-handicap-tribunal-r2-2026-09-22.md` | 0 | `FLOAT HANDICAP TRIBUNAL R2 DONE · … houses that ruled: 2 of 3 · …` — `19` not running, PASS |
| STAGING FOLDER | `ls scratch/tribunal-bars-0920/stacked-deploy-0922/r2` | 1 | "No such file or directory" — RECOVERY: fresh run |
| DATE GATE (2nd, pre-launch) | `date` | 0 | `Tue Sep 22 12:00:04 EDT 2026` — 2026-09-22, ALLOWED |

## Packet
Staged in `scratch/tribunal-bars-0920/stacked-deploy-0922/r2/`:
- `fold.md` — 14,881 B, 0 trailing-whitespace lines. Fold line 1 (`05:205`, ±6 lines = `05:199-211`), fold line 2 (`05:361`, ±6 lines = `05:355-367`), P12 PRODUCTION BASELINE whole (`05:201-221`), STEP-4.5 SMOKE whole (`05:344-380`).
- `evidence.md` — 12,154 B. `runner.py:290-315`, `runner.py:355-380`, `store.py:245-290`, `poller.py:55-90`, `probes.py:85-125`, `tunables.yaml:504-510`, `deploy-2026-09-22.md:38-59` (P12 rows), `cto-2026-09-22.md:114` (ILAG quote).
- `rulings.md` — 7,756 B. `cto-2026-09-22.md` R3/R10/R11; `cto-2026-09-21.md` R21/R25/R39.
- `greps.txt` — 13,262 B. All 5 required searches run, full output captured.
- `QUESTIONS.md` — 3,730 B. Verbatim + appended file-list paragraph.
Byte counts verified with `wc -c`; verbatim excerpts spot-checked against source with `grep -c -F` (all hits = 1).

## CONTINUE
Both houses launched 2026-09-22 12:00 ET. GROK (bg `b1vwqsw5o`, launched 12:00:09 ET) FAILED at 12:00:44 ET — HARNESS: `Error: Operation not permitted (os error 1)`, exit 1 (sandbox denial at launch, before any read; `grok-review.md` holds only that one error line, no `REVIEW:` line — recorded NO REVIEW LINE / HARNESS, not retried per one-attempt-per-house). GEMINI (bg `blcc49786`, launched 12:00:16 ET) completed 12:03:40 ET, well inside the 15-minute timeout — full answer captured and written to `gemini-review.md` byte for byte. Collation and file-check below; L67's one-house floor is met by GEMINI alone.

## Per question
| Q | grok | gemini |
|---|---|---|
| Q1 — P12 exception safe? | HARNESS FAILURE — no answer (`Error: Operation not permitted (os error 1)`, exit 1 at launch) | `DO NOT RUN` — S2 overwrites `failed_stage` to `bars` during its ~70s gap, hiding the previous cycle's lifecycle refusal behind `poll failures: <n>` (`evidence.md:55`) |
| Q2 — smoke (e) still real? | HARNESS FAILURE — no answer | `DO NOT RUN` — deploy breaks all bars fetching → S4 fails all members → `<n>` spikes → fold at (e) explicitly ignores the higher `<n>` and passes it as baseline (`fold.md:28`) |
| Q3 — fold changes strings/order/window? | HARNESS FAILURE — no answer | `RUN IT` |

OTHER-SENTENCES (fold.md lines mentioning the radar probe/heartbeat):
| line | gemini |
|---|---|
| 10 | CONSISTENT — the fold defines how to interpret the baseline |
| 12 | CONSISTENT — the fold provides the exact named exception |
| 28 | CONSISTENT — the fold clarifies how P12's baseline applies to the post-deploy check |
| 39 | CONSISTENT — the fold defines how to interpret the baseline (P12 duplicate of line 10's context) |
| 41 | CONSISTENT — the fold provides the exact named exception (P12 duplicate of line 12's context) |
| 81 | CONSISTENT — the fold clarifies how P12's baseline applies to the post-deploy check (STEP-4.5 duplicate of line 28's context) |
| 97 | INCONSISTENT — a spike in `<n>` creates a textually NEW RED string, but the fold explicitly overrides and ignores it |

## Checked against the files
| claim | who | file:line | verdict | blocks? | why |
|---|---|---|---|---|---|
| Q1 `DO NOT RUN` — S2 commits carried `poll failures: <n>` before this cycle's lifecycle check runs | gemini | `runner.py:209-218` (S2 `_pool_row`/`put_pool`, commits immediately), `runner.py:251-269` (lifecycle_refusal computed AFTER S2 has already committed), `runner.py:302-311` (lifecycle stamp lands LAST in the cycle), `runner.py:375-376`/`store.py:267,270-273` (the carried-count string) | HOLDS | yes | S2 writes `failed_stage='bars', failed_detail='poll failures: N'` from the PRIOR cycle's carried list before this cycle even checks for a lifecycle refusal; a beat sampling in that window reads exactly the fold's excepted string during a cycle that is mid-way through, or about to re-flag, a live refusal. The code's own comment (`runner.py:357-359`) documents this S2/S4 gap as a known "flap" source (`cto-2026-09-15 §1.2`) — distinct from the two escalates the desk already folded (final-text distinctness, per-record aging), which don't cover this transient-read race. |
| Q2 `DO NOT RUN` — a deploy-caused break in bars fetching hides behind a spiking `<n>` | gemini | `05-stacked-deploy.md:294-296` and `:382` (STEP-2.7: empty diff over `src/cobalt/radar` and other reachable paths, checked BEFORE STEP-3/4/4.5; any output → `FAILED: 2.7 …`, deploy stops pre-merge) | DOES NOT HOLD | no | The scenario requires this deploy's own code to break bars fetching, but STEP-2.7 proves `src/cobalt/radar` is byte-identical between `<main-at-gate>` and `<stack>` and fails the whole deploy pre-merge on any diff — smoke (e) never runs against a radar carrying this deploy's code changes, because there are none. QUESTIONS.md's own preamble states this ("STEP-2.7 proves the radar's paths have an empty diff") and gemini's answer does not address it. |
| line 97 "NEW RED" — INCONSISTENT flag (not a Q1-3 claim, not counted as a blocker) | gemini | `05-stacked-deploy.md:379` (`a NEW RED on the aset/sheet or radar probe in (e)`) | UNVERIFIABLE FROM READS | no | `05` does not define "NEW RED" (a new finding KIND vs. any RED reading textually different from P12's exact string) anywhere in the packet or in STEP-4.5 itself. Related to the Q1 finding but not itself one of the three fixed answers, so not tallied as a blocker. |

Houses did not contradict each other on any question — GROK produced no content to compare.

## Folds proposed
- `4.5 (e)`: `is still baseline here whatever \`<n>\` now reads` → `is still baseline here whatever \`<n>\` now reads, PROVIDED a second heartbeat show ≥100 s later shows the same finding kind — a reading taken while S2's carried snapshot is live but this cycle's lifecycle check has not yet completed is not proof (runner.py:209-218 vs :251-311)`

## Blockers
- Q1 `DO NOT RUN` (GEMINI) HOLDS: the S2/S4 commit-order gap (`runner.py:209-218` vs `:251-311`) lets a heartbeat beat read the fold's excepted string `failed_stage bars: poll failures: <n>` during a live lifecycle refusal the fold does not distinguish from a genuine carried per-ticker failure.

## ESCALATE
- ASK DESK: GROK's sandboxed launch was denied before any read (`Error: Operation not permitted (os error 1)`, exit 1, `--sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)"`) — a harness/environment failure, not a content refusal or a finding about the fold. Safe default taken: proceeded on GEMINI alone per L67's one-house floor; not retried (one attempt per house). Worth the desk's look before the next house round needs GROK. [2026-09-22 12:00 ET]

STACKED DEPLOY REVIEW R2 DONE · houses: 1 of 2 · blockers: 1 · folds: 1
