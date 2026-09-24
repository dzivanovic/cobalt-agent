# Stale-score build check, round 1 — 2026-09-24

## §0 Headline
- Checked: nothing. The run stopped at PREFLIGHT. No packet was staged and no checker was launched.
- Two PREFLIGHT rows fail. In the prompt's order the first is "branch moved above `<tip>`": two `tests`-touching commits (`2bdc73df`, `358f1f75`) sit above the build's stop-line tip `01ee8bcd`. The second is THE STAGGER: R86 (`cto-2026-09-24.md:106`) names this file but lacks the literal `no other house hub is running`.
- Every gate before those passed.
- ESCALATE: 2. Nothing is built, run, merged or staged by this run.

## L74
none

## PREFLIGHT

`<D>` = 2026-09-24, 18:44 ET (`date` → `Thu Sep 24 18:44:16 EDT 2026`).

| rule | command | exit | result |
|---|---|---|---|
| placeholder gate | `grep -n -E "R_[_]"` on this prompt | 1 | allowed; prints nothing — PASS |
| grok gate, R17 row | `grep -n "^| R17 " cto-2026-09-24.md` | 0 | allowed; line 31 carries `Grok approved with no asking going forward` |
| grok gate, R17 committed | `git log -1 --format=%H -S"Grok approved with no asking going forward" -- cto-2026-09-24.md` | 0 | allowed; `1758fd78a572f47b613b2ca831dcfa636ed8f65a` |
| grok gate, R19 row | `grep -n "^| R19 " cto-2026-09-24.md` | 0 | allowed; line 33 carries `All 4 house models approved for use indefinlitly` |
| grok gate, R19 committed | `git log -1 --format=%H -S"All 4 house models approved" -- cto-2026-09-24.md` | 0 | allowed; `5055151dbf68899b82de5b11f99733ed2d03048c` |
| R45 row | `grep -n "^| R45 " cto-2026-09-22.md` | 0 | allowed; line 121 carries `recompute the FRESH-price tap race` |
| R40 row | `grep -n "^| R40 " cto-2026-09-22.md` | 0 | allowed; line 126 carries `EXCLUDED from the shadow agreement numbers` |
| R45 committed | `git log -1 --format=%H -S"recompute the FRESH-price tap race" -- cto-2026-09-22.md` | 0 | allowed; `1a3f5cf7003c03cb41a5158d601133b4c61a264b` |
| R58 row | `grep -n "^| R58 " cto-2026-09-23.md` | 0 | allowed; line 61 carries `"yes start both"` |
| R95 row | `grep -n "^| R95 " cto-2026-09-23.md` | 0 | allowed; line 103 carries `just Opus and Grok for code checks` |
| R97 row | `grep -n "^| R97 " cto-2026-09-23.md` | 0 | allowed; line 105 carries `take Gemini out of reading` |
| build's stop recorded | `grep -n -F "STALE SCORE BUILT"` on the three desk files | 2 | allowed; `cto-2026-09-25.md` and `cto-2026-09-26.md` do not exist (recorded, not fatal). `cto-2026-09-24.md` R84 (line 102) quotes the stop line — PASS |
| this launch's row | `grep -n "44-stale-score-check-r2.md"` on the three desk files | 2 | allowed; R86 at `cto-2026-09-24.md:106` (the other two files are absent, as above) |
| this launch's row committed | `git log -1 --format=%H -S"44-stale-score-check-r2.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | 0 | allowed; `f6643d4150ae2ce6f91a798a4498bf74df46840c` |
| the line is `15`'s | `grep -c -F -e "<rule>"` on `15-drc-d1-fix-r1-check.md`, for each of the 14 allow strings and 3 deny strings, quotes included | 0 | allowed; each counted 1 — PASS |
| Astra / agy / production string in the launch line | read of the launch line in line 1 of the prompt | — | none present — PASS |
| `grok --version` | `grok --version` | 0 | allowed; `grok 1.0.25 (f7e67d6988e2) [stable]` |
| worktree | `ls /Users/cobalt/cobalt-wt/stale-score` | 0 | allowed; present |
| THE BUILT LINE | `tail -n 3` of the build report | 0 | allowed. Last non-blank line, whole: `STALE SCORE BUILT 01ee8bcd \| on de48c19b \| rebased: yes \| red 7bffdbcb \| offline 2518/0 \| with-DB 2879/0 \| live-note 131/0 \| migration: 0015 rolled back \| cobalt_dev: 0013 \| .env: removed \| experiments 31/31/0 \| ESCALATE: 11`. It carries every required field; `cobalt_dev: UNPROVEN` is absent. |
| `main` is the base | `git log --oneline 01ee8bcd..de48c19b` | 0 | allowed; EMPTY — PASS |
| deploy tag under base | `git log --oneline de48c19b..a2d320b8` | 0 | allowed; EMPTY — PASS |
| the range | `git log --oneline de48c19b..01ee8bcd` | 0 | allowed; 6 commits: `f0798537`, `7bffdbcb` (= `<red>`), `f17814c6`, `d0274dc0`, `3894d1a1`, `01ee8bcd` |
| branch tip | `git log --oneline -1 cards/stale-score-0922` | 0 | allowed; `358f1f75` (report commit above `<tip>`) |
| branch moved above tip | `git log --oneline 01ee8bcd..cards/stale-score-0922 -- tests src configs` | 0 | allowed; NOT EMPTY — the rule's stop condition is met. Printed: `358f1f75 docs(report): stale score build r2 …` and `2bdc73df test(cards): stale score STEP-5 audit gate X4, restarts X17, rendering X29 …`. `git show --stat` of each: `2bdc73df` adds `tests/experiments/stale_score/test_x29_ladder_render.py` and `test_x4_audit_stale_card.py`; `358f1f75` adds `tests/experiments/stale_score/test_xl76_devdb_absence.py`; neither touches `src` or `configs`. Both also edit the build report. |
| stat list | `git log --stat --oneline de48c19b..01ee8bcd` | 0 | allowed; 6 commits, files as printed by the command (src: `scoring.py`, `audit_export.py`, `evaluate.py`, `formations.py`, `store.py`, `db_migrations/__init__.py`, `0015_*.sql` pair; tests: `test_stale_score.py`, `test_stale_score_db.py`, `tests/experiments/stale_score/`, `stale_db_support.py`, migration-registry re-points; docs: DevDocs + reports). Not judged (L37); not staged (run stopped). |
| `.env` | `ls /Users/cobalt/cobalt-wt/stale-score/.env` | 1 | allowed; `No such file or directory` — PASS |
| scratch folder | `ls scratch/tribunal-bars-0920` | 0 | allowed; present |
| recovery | `ls scratch/tribunal-bars-0920/stale-score-check` | 0 | allowed; holds only `60-production-x9-x25.md` (fresh run: nothing of mine staged) |
| production reads | `ls scratch/tribunal-bars-0920/stale-score-check/60-production-x9-x25.md` | 0 | allowed; present (the desk ran X9 / X25; R86 states both = 0). Not opened by me. |
| THE STAGGER | `grep -n -F "no other house hub is running" cto-2026-09-24.md`, then checked for a printed line that also names `44-stale-score-check-r2.md` | 0 | allowed. **FAIL.** 12 lines print (R5, R11, R18, R26, R31, R36, R37, R41, R48, R49, R70, R75). None names `44-stale-score-check-r2.md`. `grep -n -F "44-stale-score-check-r2.md"` prints only line 106 (R86), which is not among those 12. |
| THE PROBES (Opus, Sol) | — | — | NOT RUN: PREFLIGHT stopped at THE STAGGER row, before THE PROBES |

Order note: the "branch moved above `<tip>`" row precedes THE STAGGER in the prompt, so it is the stop line's rule. I ran the stagger checks in the same batch before re-reading that row's output; both fail. A relaunch fails on the tip row unless the desk re-points `<tip>`, and on the stagger row unless R86 is amended. See ESCALATE 1 and 2.

## Packet
Not staged. The run stopped before staging. `scratch/tribunal-bars-0920/stale-score-check/` holds only the desk's `60-production-x9-x25.md`, untouched.

## CONTINUE
next: none — the run ended at PREFLIGHT. A relaunch of this file first runs `ls scratch/tribunal-bars-0920/stale-score-check`, then re-runs PREFLIGHT from THE STAGGER row after the desk edits R86.

## Per question
Not run: no checker was launched.

## Suites
Not collated: the run stopped before staging. The build's own stop line is quoted under PREFLIGHT (`offline 2518/0`, `with-DB 2879/0`, `live-note 131/0`, `.env: removed`, `cobalt_dev: 0013`, `migration: 0015 rolled back`, `experiments 31/31/0`, `ESCALATE: 11`). These are the builder's claims, unverified by this run (L35).

## Checked against the branch
Not run.

## Ready for a deploy
opus: no CHECK line (not launched) · grok: no CHECK line (not launched) · sol: not probed (before 2026-09-26 06:47, `54`'s probe) · gemini: NOT SEATED (R96/R97). Ready for a deploy prompt: 0 of 0 answered. The floor is two (R95).

## FOR THE CLASSIFIER
none

## ESCALATE
1. **THE STAGGER row is unmet (second failing row).** R86 (`cto-2026-09-24.md:106`) names `44-stale-score-check-r2.md` and says "House lane: FREE since 18:06." It does not contain the literal `no other house hub is running`, which the prompt's gate requires on a line that also names this file. The desk edits R86 to say that sentence, with the pgrep basis it usually gives (R26, R31, R36), commits it, and relaunches the same launch line. I checked no process list, since I hold no `pgrep` string, so I state nothing about whether another house hub is running now.
2. **THE BRANCH-MOVED row is unmet (first failing row, the stop line's rule).** The build's stop line names `<tip>` = `01ee8bcd`, but two commits sit above it that touch `tests/`: `2bdc73df` (STEP-5 experiments X4, X29; the reported `experiments 31/31/0` and the stop line's hash predate it) and `358f1f75` (the `test_xl76_devdb_absence.py` module, plus the report). So the tree the suites' numbers were reported for (`01ee8bcd`) is not the tree that holds all the build's tests. ASK DESK: on a relaunch, is `<tip>` `01ee8bcd` (the stop line's hash, and the row stops on the two commits) or the branch tip `358f1f75`? Per the prompt the row stops the run unless the desk re-points it; I do not re-point it. [18:44 ET, from `date`]
3. The desk's X9 / X25 file exists (R86: X9 = 0, X25 = 0). It is unchecked by me: I did not open it.
4. Sol: not probed. It is before Sep 26th, 2026 6:47 AM (`54`'s probe), so the recorded line is `sol: METER — retry after Sep 26th, 2026 6:47 AM (54's probe)`.
5. The build's own ESCALATE count is 11 (from its stop line). It is not read by this run, since the run stopped.

FAILED PREFLIGHT: the branch moved above 01ee8bcd — 358f1f75 docs(report) and 2bdc73df test(cards) touch tests; (also: R86 lacks "no other house hub is running") — launch nothing
