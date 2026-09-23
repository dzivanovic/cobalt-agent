# Smoke-fix check round 2 — draft report (2026-09-23)

§0 Wrote `prompts/2026-09-23/17-s2-smoke-fix-check-r2.md`: ROUND 2 of the S2 smoke-fix check, F3 only (`b510b65`). Houses: Gemini (required, runs first), Grok and Opus 5.5 re-confirming F3. Sol is not seated (no ruling in round 1, so no round spent, L67 P-c). Launch line matches `06` byte for byte (checked by script at 07:52 ET; only the path and remote-control name differ). New rule strings: 0. Report path `reports/s2-smoke-fix-check-r2-2026-09-23.md`; the stop line keeps `06`'s DONE shape plus `round: 2`. ESCALATE: 3.

## What `17` carries
| item | value |
|---|---|
| hub | Sonnet 5, rc `s2-smoke-fix-check-r2-0923`, cwd `/Users/cobalt/cobalt-wt/agy-trial` |
| launch line | `06`'s, byte for byte: same 15 allow strings, 3 denies, `--add-dir` triplet. 5 of the 15 are never run (`mkdir`, three `s2-p2-cards`, `codex exec`) |
| authorization | `06`'s first paragraph (the `70` chain + DATE/EXTENSION gate at R30) and its first two PLUS gates, unchanged. New gates: round-1 report DONE with `DEFECT REMAINS F3` + `defects that HOLD: 0` and committed · R22 row carries `DOES NOT HOLD`, `models.py:92-97`, `16-draft-smoke-check-r2.md` and is committed (`b3f70f8` holds it) · launch row `R__` names `17-s2-smoke-fix-check-r2.md` and is committed |
| packet folder | `scratch/tribunal-bars-0920/s2-smoke-fix-check-r2/` (inside Grok's `--allow` and R49's wildcard) |
| packet | `f3-diff.md` (`git show b510b65 -- s2.yaml test_smoke_k3_sql.py`, 8,402 B, 2 `diff --git`) · `k3-at-tip.md` · `gemini-r1.md` (round-1 `gemini-check.md` whole, 1,704 B) · `hub-file-check.md` (round-1 report lines 62–68 + R22's desk-read clause) · `pool-at-tip.md` (`:109-212`, plus `:36-56`, `:323-398`) · `models-at-tip.md` (`:77-106`, `:21`) · `store-at-tip.md` (`:65-170`) · `QUESTIONS-S2FIX-R2.md`. Estimate ≈ 45 KB ≈ 11k tokens per house |
| questions | FIRST: Gemini's two round-1 sentences (S1 write defect nulls both, S2 designed NULL metric name), each HOLDS / DOES NOT HOLD / NOT CHECKABLE with file:line · SECOND: AGREE/DISAGREE per hub file-check row + desk read · THIRD: F3 CLOSED / NOT CLOSED / NEW DEFECT; ruling change stated · closing line: round 1's `CHECK S2 FIX:` shape, unchanged |
| stagger | `05` and `08`: `<nn> is not running` literal on a launch-row line naming `17` (`08`'s shape). Every other house hub (`03`, `06`, `13`, …): `no other house hub is running` |
| fail closed | Gemini not UP → FAILED PREFLIGHT, launch nothing. Fewer than 3 UP → FAILED PREFLIGHT |
| stop line | `S2 SMOKE FIX CHECK DONE · round: 2 · grok: <CHECK line> · gemini: <…> · opus: <…> · sol: NOT SEATED (round 1: METER — retry after Sep 26th, 2026 6:47 AM) · defects that HOLD: <n> · ESCALATE: <n>` |

## The `07` P6 change the desk must make (path only, L19 re-issue)
File `prompts/2026-09-23/07-stacked-deploy.md`, line 148 (the second P6 bullet). Two substitutions, nothing else:
- `prompts/2026-09-23/06-s2-smoke-fix-check.md` → `prompts/2026-09-23/17-s2-smoke-fix-check-r2.md`
- `reports/s2-smoke-fix-check-2026-09-23.md` → `reports/s2-smoke-fix-check-r2-2026-09-23.md`

The line after the change starts: ``  - `tail -n 3` of the smoke-fix check report that `prompts/2026-09-23/17-s2-smoke-fix-check-r2.md` names (the desk's R__L row quotes its path and stop line; expected `reports/s2-smoke-fix-check-r2-2026-09-23.md`). The LAST NON-BLANK line is `06`'s DONE shape, …`` Everything from there on stays unchanged. P6's opening commit gate (`git log -1 --format=%H -- "<path>"`) then applies to the round-2 report. No other line of `07` names `06` or the round-1 report (grep, 07:5x).

## ESCALATE
1. **I added packet files beyond the named list.** `16` named the F3 diff, Gemini's text, the file-check rows, `pool.py:109-212` and `models.py:92-97`. `17` also stages `k3-at-tip.md`, `pool.py:36-56` (`Transition`), `pool.py:323-398` (`decide`), `models.py:77-106` + `:21`, and `store.py:65-170`. Reason: the hub's file-check cites `store.py:86-94,132-142` and the RETAIN / ADMIT / EXCLUDE transitions, and `_ranked` reads `pool.rank_metric` and `pool.overrides` (`PoolOverride.rank_metric` is `… | None = None`, `models.py:80`). Without those lines a checker cannot verify the rows it is asked to rule on. These are packet contents, not rule strings. The desk can narrow the list with a path-only edit.
2. **The `round: 2` field.** It sits between `DONE` and `grok:`. `07` P6 reads "`06`'s DONE shape" and counts `ready … YES` fields; it does not name field positions, so I read it as passing unchanged. If the desk reads "`06`'s DONE shape" strictly, the edit to P6 is no longer path-only.
3. **What happens if Gemini says NO again with HOLD 0.** One round is left (round 3, the last; no fourth, L39), or his per-case override (L67 OVERRIDE / L73). Otherwise the branch drops from tonight's set (L43). `17` carries this as a standing line; the desk should set up the round-3 or override question in advance so it doesn't stall the deploy.

SMOKE CHECK R2 DRAFTED · houses: gemini, grok, opus 5.5 · new rule strings: 0 · ESCALATE: 3
