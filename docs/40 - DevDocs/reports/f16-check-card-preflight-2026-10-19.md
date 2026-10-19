# f16-close-1018 check card — preflight (2026-10-19)

Card: `prompts/2026-10-19/817-f16-close-check-card.md`. Read only; one file written (this one).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt merge-base s5/f16-close-1018 main` | `40e646edf7264b21191b2b63f5fbbb2dede793c7` (card `BASE: 40e646ed`) | OK |
| 2 | `git -C /Users/cobalt/cobalt log --oneline 40e646ed..s5/f16-close-1018` | `be0810ce` build report · `f44c4b52` feat · `81efedf3` wip red | OK |
| 3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 f44c4b52` | `f44c4b52` (card `TIP`, the feat commit; BASE is its ancestor, check 2) | OK |
| 4 | `git -C /Users/cobalt/cobalt rev-parse --short=8 s5/f16-close-1018` | `be0810ce` (the head named in the card's WHY) | OK |
| 5 | `git -C /Users/cobalt/cobalt diff --name-only --no-renames f44c4b52 s5/f16-close-1018` | `docs/40 - DevDocs/reports/f16-close-1018-build-2026-10-18.md`, `…build-2026-10-18.result` (report and its result only) | OK |
| 6 | `git -C /Users/cobalt/cobalt diff --stat f44c4b52 s5/f16-close-1018 -- . ":(exclude)docs"` | nothing (head adds docs only) | OK |
| 7 | `git -C /Users/cobalt/cobalt diff --name-only --no-renames 40e646ed f44c4b52` | `docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/cobalt/taxonomy/loader.md`, `src/cobalt/cli.py`, `src/cobalt/taxonomy/loader.py`, `tests/cobalt/test_f16_close_1018.py` (the five files of row S0) | OK |
| 8 | `ls "/Users/cobalt/cobalt-wt/f16-close-1018/docs/40 - DevDocs/reports/"` | lists `f16-close-1018-build-2026-10-18.md` and `.result`: the card's `REPORT` path exists | OK |
| 9 | `ls /Users/cobalt/cobalt/docs/40\ -\ DevDocs/reports/f16-close-1018-check-2026-10-19.md` | `No such file` (the CHECK REPORT is absent, as it must be before the check; parent folder `reports/` exists, check 8's sibling listing and this report's location) | OK |
| 10 | `git -C /Users/cobalt/cobalt diff HEAD -- "…/prompts/2026-10-19/817-f16-close-check-card.md"` | nothing | OK |
| 11 | `git -C /Users/cobalt/cobalt log --oneline -2 -- "…/817-f16-close-check-card.md"` | `b155c106 docs(desk): Close gate check card 817, preflight prompt 818, R1990` (committed; one commit) | OK |
| 12 | `grep -n -E "FILL\|«" card` | nothing (no placeholder token at all) | OK |
| 13 | `grep -n -E "claude --bg\|--allowedTools\|--add-dir\|--permission-mode" card` | nothing (no launch line, allow string, add-dir or mode; R411, R412) | OK |
| 14 | `grep -n -E "^(BAND\|RULINGS\|JOB\|LADDER\|BRANCH\|WORKTREE\|BASE\|DB\|INSTALL):" prompts/2026-10-18/790-f16-close-card.md` | `JOB f16-close-1018` · `LADDER S5 · F16 close` · `BRANCH s5/f16-close-1018` · `WORKTREE f16-close-1018` · `BASE 40e646ed` · `BAND MID` · `RULINGS 2026-10-18 R1841`; no `DB:` (matches the check card, which has none) | OK |
| 15 | `grep -n "ASK DESK" <build report>` | two tagged items: `:173` item 1 (head-range RESTARTS lists untracked `SHADOW-INSTRUCTIONS.md` UNCLASSIFIED, exit 1; committed range `com.cobalt.aset com.cobalt.radar`), `:174` item 2 (`validate --no-db` cannot run in the builder seat; proven in-process; CLI run is the deploy proof). Card X6 (1) and (2) match these | OK |
| 16 | `grep -n -i -E "self-check\|never run\|mutation" <build report>` | `:175` DECISIONS 3 (self-check (1) gap: the `pptx` assert and the C1 CONTROL never shown red; "left for the check"; `self-check: 2 of 3`). Card X6 (3), rows V1 and C1 carry it as the build took it | OK |
| 17 | `grep -n -E "^(CLASS\|INSTALL\|RESTARTS\|HOUSE A):"` over cards 731, 790, 648 | 731: `CLASS K2`, `INSTALL none`, `RESTARTS com.cobalt.aset com.cobalt.radar`; 790: none of the four; 648: `CLASS K5`, `INSTALL none`, `HOUSE A grok`, `RESTARTS none` | OK |
| 18 | read: card vs `CARD.md` and card 648 | header keys `JOB`…`RULINGS` in CARD.md order plus `CLASS`/`INSTALL`/`HOUSE A`/`RESTARTS` as 648; body order ROWS · NOT IN THIS JOB · READ · CHECK ASKS · DEPLOY PROOF · RECORDS, headings bare; ROWS table is the 4-column form; DEPLOY PROOF has three marker lines (`· before` `· after`) and one smoke line | OK |

## ISSUES

- NOTE · `CLASS: K2`: not in `CARD.md` or build card 790; the K2 precedent holds (card 731 carries `K2` with `INSTALL: none`, check 17). Not proven wrong.
- NOTE · `RESTARTS: com.cobalt.aset com.cobalt.radar`: the build's committed-range line; build card 790 `## RECORDS` named radar only. The card defers it to row R2 (L42), which re-derives it. Not proven wrong.
- NOTE · `BASE: 40e646ed`: equals `merge-base` (check 1); card 790 `## RECORDS` names `e7ef198a` as `main` at drafting, which the card's own `## RECORDS` already records. Not proven wrong.
- NOTE · "three build `ASK DESK` items": the build report tags two as `ASK DESK` (`:173`, `:174`); the third is its DECISIONS 3 (`:175`), untagged. The card's X6 carries all three as the build took them, so no fix is owed.
- NOTE · checks 9 and 12–13 were greps over the card as written; the card's rows hold command strings (`gate.sh`, `cobalt jobs restarts`) in ROW text, not on a launch line.
- NOTE · my first `rev-parse` call passed three revisions and exited 128 (`Needed a single revision`); rerun one revision per call (checks 3, 4); no change to the card.

PREFLIGHT DONE · card: f16-close-1018-check · checks: 18 · fails: 0 · ready: YES
