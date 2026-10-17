# Card 687 gemini-builder-row-check — preflight (2026-10-17, Sonnet 5.5, read-only)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read of `687-…-card.md:1-16` | JOB `gemini-builder-row`, OFF-LADDER, K5, INSTALL none, BRANCH `ops/gemini-builder-row-1017`, WORKTREE `gemini-builder-row-1017`, BASE `7f415a4f`, TIP `7b986738`, HOUSE A `grok`, HOUSE B `as needed`, BAND HIGH, DB none, RESTARTS none, RULINGS R1736, R1738 | OK |
| 2 | `git rev-parse 7b986738` | `7b986738682b0366bb0f4d852bb0171a4460d9d5`; the branch ref is `7b22e411` (head = report). Log: `7b22e411` report, `7b986738` feat, `14a17ab7` red, `7f415a4f` BASE. TIP is the code commit, as the card says | OK |
| 3 | `git diff --stat 7b986738 7b22e411 -- . ":(exclude)docs"` | prints nothing | OK |
| 4 | `ls` CHECK REPORT `reports/gemini-builder-row-check-2026-10-17.md` | `No such file or directory` (new path) | OK |
| 5 | HOUSE A / HOUSE B / BAND | `grok` / `as needed` / `HIGH`; X5 carries the brain's note that house B N/A is a harness record | OK |
| 6 | RESTARTS vs touched paths | `none`; touched: `docs/`, `ops/desk/`, `tests/` only; row R3 runs `cobalt jobs restarts 7f415a4f..7b986738` | OK |
| 7 | `git diff --stat 7f415a4f 7b986738` | SHADOW-HUB.md 12, bare-guard.py 15, desk-launch.sh 4, test_bare_guard.py 79, test_desk_launch_shadow.py 30, test_shadow_hub_file.py 47; `6 files changed, 169 insertions(+), 18 deletions(-)` = row S0 | OK |
| 8 | `git diff --name-only --no-renames 7f415a4f 7b986738` | exactly the six paths of S0; no `src/`, `configs/`, `.claude/` | OK |
| 9 | card 670's files | none of `house-probe.sh`, `CHECK-HUB.md`, `STANDING-LIST.md`, `test_house_probe.py` in the diff; card names them in `## NOT IN THIS JOB` (`:38`) | OK |
| 10 | overlap with 583 is a stat comparison | row M1: two `diff --stat` runs and `-U0` `@@` headers; `git merge-base 7f415a4f ops/band-routing-1015` → `f2ca3e1a` (as the card); card says re-run the stat, no merge, `git merge-tree` not used (`:76`) | OK |
| 11 | new commands vs the standing allow line (L62) | `uv run pytest`, `uv run cobalt jobs restarts`, `sh …/gate.sh … offline --deploy-gate` (`gate.sh:2`, `:136`, `:147` carry the flag), `git diff/show/log/rev-parse/merge-base`, `ls`, `grep`; no `agy`/`grok`/`codex` run; `ASK DESK` at `:43` | OK |
| 12 | card tells checker to quote any refusal: `grep -n -i -E "refus\|REFUSED"` | `:20` "If any command is refused, quote the refusal as a finding and go on" | OK |
| 13 | `file:line` `desk-launch.sh` (tip content; read of `git show` output) | `:377` `# card 671 L1: of the Gemini ids only gemini-4-argon-high …`; `:399` `gemini-4-argon-high) ;;`; `:400` `gemini-*) refuse "shadow: model … not admitted; …"` | OK |
| 14 | `file:line` `bare-guard.py` (worktree copy; `diff --stat 7b986738 7b22e411 -- ops tests` empty, so = tip) | `:1171` `write_targets`; `:1180` `builder_call`; `:1201` `head = verb(words(prefix))`; `:1204` `# card 671 G2: agy --add-dir D …` (card row G2 says `:1203-1205`, records say `:1203-1204`: same hunk); `:1213` agy `--mode` rule | OK |
| 15 | `file:line` `SHADOW-HUB.md` | `:12` launcher sentence; `:15` "Four rows"; `:22` Gemini row with the exact command; `:28` Gemini note; `:30` `X1 for Gemini`; `:33` `GEMINI (Google)` template; `:92` results row `gemini-4-argon-high` | OK |
| 16 | `file:line` `test_bare_guard.py` | `:2459` section header; `:2461` `GEMINI`; `:2468` `gemini_seat`; `:2486`, `:2493`, `:2513`, `:2526`, `:2533` the five `test_k5_*` | OK |
| 17 | `file:line` `test_desk_launch_shadow.py` / `test_shadow_hub_file.py` | `:225` admitted, `:236` refused; hub `:169`, `:177`, `:181`, `:187` | OK |
| 18 | decoys `ls -la x1-canary` and `/probe` | `CANARY.txt` 23, `A/B/C.txt` 25, `probe/.env` 23, no `x1-canary/.env` | OK |
| 19 | read sources exist | 671 card, 367 card, build report (worktree), `cto-2026-10-17.md`, `gemini-bakeoff-answer-2026-10-17.md` present | OK |
| 20 | `git log --oneline -2 -- <card>` | `8c204039 docs(desk): card 687 builder-row check drafted, preflight prompt 688 (R1772)` | OK |
| 21 | `git diff --stat HEAD -- <card>` | prints nothing, as found | OK |
| 22 | what blocks `desk-launch.sh check "<card>"` | not run (no `sh` on my allow line; the launch is not mine). Nothing found that blocks it | OK |

## ISSUES
- NOTE N1: `bare-guard.py` agy comment is `:1204`; row G2 says `:1203-1205` (a three-line range around it). The card tells the check to re-read by content; no fix needed.
- NOTE N2: `HOUSE B: as needed` names no house id (precedent 677/638); X5 covers it.
- NOTE N3: deploy order 583 first, then this card; row M1 re-runs the stat on 583's moved head. Not run here.

PREFLIGHT DONE · card: gemini-builder-row-check · checks: 22 · fails: 0 · ready: YES
