# Card 670 `gemini-probe-id` — preflight (read-only), Sat Oct 17 08:05 EDT 2026

Card: `docs/40 - DevDocs/prompts/2026-10-16/670-gemini-probe-id-card.md`. Spec: `prompts/CARD.md`, `prompts/BUILD-HUB.md`. Precedent: card 641.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | Read card 670 header | JOB `gemini-probe-id`, LADDER `OFF-LADDER — reports/cto-2026-10-17.md R1736`, CLASS `K5`, INSTALL `none`, BRANCH `ops/gemini-probe-id-1017`, WORKTREE `gemini-probe-id-1017`, REPORT inside that worktree, BAND `MID`, DB `none`, RESTARTS `none`, RULINGS `2026-10-17 R1736, 2026-10-17 R1738`; every CARD.md build-required key is present | OK |
| 2 | `git -C /Users/cobalt/cobalt log --oneline main..f2140694` | empty: BASE `f2140694` is an ancestor of `main` (`main` = HEAD = `3f037e70`, one commit past BASE; that commit is the card and prompt) | OK |
| 3 | `git -C /Users/cobalt/cobalt diff --stat f2140694 main -- ops tests CHECK-HUB.md STANDING-LIST.md SHADOW-HUB.md` | empty: the card's files are the same at BASE and on `main`, so BASE-based line numbers hold | OK |
| 4 | header TIP, CHECK REPORT, HOUSE B | `TIP:` empty (the desk fills it at launch); `CHECK REPORT:` and `HOUSE B:` empty, as CARD.md says for a build | OK |
| 5 | R1736 and R1738 are committed | `git log -1 -S"\| R1736 \|"` → `d01849e7`; `-S"\| R1738 \|"` → `b57cbf8e`; `reports/cto-2026-10-17.md:18` and `:20` are both `HIS RULING · APPROVED`, R1736 text names `gemini-4-argon-high` and the K5 card (file shows `M` in the tree for later rows; the two rows are in commits) | OK |
| 6 | `## RECORDS` `agy models` line | card line 57: `gemini-4-argon-high	Gemini 4 Argon (High)`, listed with `-medium` and `-low`, `Sat Oct 17 08:03:45 EDT 2026`; filled and names the id (a desk record, not re-run here: `agy` is not on this seat's list) | OK |
| 7 | `git -C /Users/cobalt/cobalt grep -n gemini-3.1-pro-high main -- ops tests CHECK-HUB.md STANDING-LIST.md SHADOW-HUB.md` | 9 lines: `house-probe.sh:24`, `:104`; `CHECK-HUB.md:95`; `STANDING-LIST.md:13`; `test_house_probe.py:253` (all card 670); `SHADOW-HUB.md:88`; `test_desk_launch_shadow.py:216`, `:217` (card 671, NOT IN THIS JOB). Plain `git grep` on `main` of `prompts/` paths needs the `docs/40 - DevDocs/` prefix; the card's paths are shorthand for it. | OK |
| 8 | every hit of 7 assigned once | 670 owns 5 lines in 4 files; 671 owns 3 lines in 2 files (`SHADOW-HUB.md:88`, the test `:216-217`); `desk-launch.sh:398` holds `gemini-*` (a glob, not the old id) and is 671's by the card; none left over, none claimed twice (670's NOT IN THIS JOB names exactly 671's three) | OK |
| 9 | sample `house-probe.sh:24` and `:104` on `main` | `:24` header `agy --model gemini-3.1-pro-high … --print-timeout 3m …`; `:104` `exec agy --model gemini-3.1-pro-high … --print-timeout 3m …`; `grep -n agy` finds no other `agy --model` line, so "exactly 2" holds | OK |
| 10 | sample `CHECK-HUB.md:95` and `STANDING-LIST.md:13` on `main` | `:95` starts `- **GEMINI:** \`agy --model gemini-3.1-pro-high --mode accept-edits …`; `:13` `THE HOUSE SPELLINGS … agy --model gemini-3.1-pro-high --mode …`; both carry the token once; `CHECK-HUB.md` has 127 lines (`grep -c ""`) | OK |
| 11 | sample `tests/ops/test_house_probe.py` | `:20-22` `REPO`, `PROBE`, `CHECK_HUB` (card says `:21-22`, right); `:193` `assert len(lines) == 127`; `:246-256` the Gemini spelling test, `:253` holds `"--model", "gemini-3.1-pro-high", …` | OK |
| 12 | sample `reports/check-scratch-fr-check-2026-10-16.md:75` | the `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" …)` line (also `:159`, `:226`) | OK |
| 13 | RED/GREEN pin specified | `test_k5_gemini_id_is_gemini_4_argon_high` appended; uses `PROBE`/`CHECK_HUB`; counts 2 `agy --model` lines in `PROBE`, 1 `- **GEMINI:**` line in `CHECK_HUB`, none holding the old id; RED on BASE quoted (`1 failed`), edits, `:253` token, whole file `0 failed`; mutation of `:104` makes this test and `test_gemini_is_spelled_…` red (that test's argv at `:253` compares what the stub received, so it does fail); no hash, no whole fixed-file line (brain R1472) | OK |
| 14 | P0 stops on a missing id | row P0 (a): a record not naming `gemini-4-argon-high` → last line `FAILED: id not listed — <the record's line>`; `agy models` handled as `ASK DESK` with the record quoted whole | OK |
| 15 | no command beyond the build line's allow list | `BUILD-HUB.md:12` allows `sh /Users/cobalt/cobalt/ops/desk/*` (P0 b probe), `grep *` (P1 `grep -rn -F`), `uv run pytest *` (incl. `-p no:cacheprovider`), `uv run cobalt jobs restarts *`, `git add/commit/diff/status/log/show`, `Edit(//Users/cobalt/cobalt-wt/**)`. Not listed and handled as `ASK DESK`: `agy models` (P0 a), the worktree probe `sh /Users/cobalt/cobalt-wt/…/house-probe.sh gemini` (P1). `DB: none`, no `.env`, no `COBALT_ENV`. No new command. | OK |
| 16 | overlap with card 583 | `git diff main...ops/band-routing-1015 -U0 -- CHECK-HUB.md` changes only lines 64 and 117 (one line each); card 670 changes line 95; text-disjoint, line count stays 127 on both | OK |
| 17 | `git diff HEAD --stat -- 670-gemini-probe-id-card.md` and `git log -1 -- 670-…` | empty diff; last commit `3f037e70` — card is committed and unchanged against HEAD (found as it stands) | OK |
| 18 | worktree and `CARD.md` keys | `/Users/cobalt/cobalt-wt/gemini-probe-id-1017` does not exist yet (`ls /Users/cobalt/cobalt-wt`); `CLASS` and `BAND` are not documented in `CARD.md` on `main` (`grep` finds only the prodwrite `CLASS`), but other K5 cards carry them and the card's RECORDS says the same of `BAND` | OK (NOTE 3, 4) |

## ISSUES

- NOTE 1 · `STANDING-LIST.md:13` is edited by G1 but no test and no DEPLOY PROOF `grep -c` line covers it (the new pin reads `PROBE` and `CHECK_HUB` only; `P1`'s `grep -rn` after the edit does cover it once). Acceptable per the card; the check reads it by `git diff`.
- NOTE 2 · `reports/check-scratch-fr-check-2026-10-16.md` (cited in `## READ`) is untracked on `main` (`git ls-files` → not known); readable in `/Users/cobalt/cobalt` for the builder, not in its worktree. The rejection string is also in the card itself.
- NOTE 3 · The worktree and branch `ops/gemini-probe-id-1017` do not exist; the desk's launch creates them (not verified here, no launch).
- NOTE 4 · `SHADOW-HUB.md:88` cites `CHECK-HUB.md:92` (stale; the line is `:95`): card 671's text, not this card's.
- NOTE 5 · Blocks on `desk-launch.sh build "<card>"`: nothing found on the card. The desk's steps remain: create the worktree and branch from `f2140694`, and keep `cto-2026-10-17.md` rulings committed (R1736 and R1738 are, in `d01849e7` and `b57cbf8e`; the file also shows later uncommitted rows). Card 583's `CHECK-HUB.md` merge is text-disjoint, so order does not matter. Card 671 shares no file.

PREFLIGHT DONE · card: gemini-probe-id · checks: 18 · fails: 0 · ready: YES
