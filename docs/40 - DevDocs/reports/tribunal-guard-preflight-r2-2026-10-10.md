# tribunal-guard — card 251 preflight round 2, 2026-10-10 (read-only)

Card `prompts/2026-10-10/251-tribunal-guard-card.md` (commit `e61b4d69`), round 1 `reports/tribunal-guard-preflight-2026-10-10.md`, amend `reports/tribunal-guard-amend-2026-10-10.md`. Code read by `git show d0a5fbb8:ops/desk/bare-guard.py`. Not run (read-only seat): `uv run cobalt jobs restarts`, pytest; red/green claims are read from the guard's code.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| R2-1 | `git show d0a5fbb8:ops/desk/bare-guard.py` `:1033-1038` against card test (5) | `:1036` `if kind in WORKERS and launches:` → G7; `:1038` `deny = g1(command)` → G1. G7 precedes G1, so `grok --version && ls` from a `worker` seat is G7 on BASE. Card says the `&&` case is RED on BASE (G7 `:1036` before G1 `:1038`, G7 hides G1), `git push` GREEN on both, and "Only (1) and the `&&` case of (5) are red on `BASE`" | OK |
| R2-2 | round 1's 22 checks re-run against the amended card | rows 1-22 below | see below |
| R2-3 | `git diff --stat HEAD -- <card> ops/desk tests/ops`; `git diff 9b03f5eb HEAD -U0 -- <card>` | first: empty. second: row T test (5) text changed, the last-sentence change, and three added lines X4, X5, X6; nothing else. Amend report CHANGES (test (5), last sentence, X4-X6) match | OK |
| R2-4 | `grep -c -F "«FILL" <card>`; card header lines 5, 11 | 0; `BASE: fccbb258`, `RULINGS: 2026-10-08 R685` | OK |

Round 1's checks re-run on the amended card:

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | header fields JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS | all present, REPORT under `$WT/tribunal-guard-1010/docs/40 - DevDocs/reports/`; unchanged by the amend | OK |
| 2 | `fccbb258` real main commit, no code change past `d0a5fbb8` | card header unchanged; the amend touched no code (`git diff --stat HEAD -- ops/desk tests/ops` empty) | OK |
| 3 | R685 row | header unchanged | OK |
| 4 | `«FILL` count | 0 | OK |
| 5 | card committed, guard and tests unchanged | card in `e61b4d69`, working tree clean for card, `ops/desk`, `tests/ops` | OK |
| 6 | `:83`, `:88` | `WORKERS = ("build", "check", "devfix", "deploy", "worker")`; `LAUNCHERS = ("claude", "codex", "grok", "agy")` | OK |
| 7 | `:124-125` | G9 comment and `HOUSE` as the card says | OK |
| 8 | `:731-753` `seat()` | `:736` `prompt = m.group(1)`, `:746-747` brain, `:748-749` worker, `:753` the one return | OK |
| 9 | `:1015-1041` `bash_rules` | `:1015` def, `:1021` `kind = s["kind"]`, `:1033` launches, `:1034-1035` G9, `:1036-1037` G7, `:1038` G1 | OK |
| 10 | worktree cwd gives `worker` | `agy-trial` under the worktree root, not `REPO_ROOT`; `:748` | OK |
| 11 | name pattern over `ls -d prompts/20*/*tribunal*` (76 files) | matches every `NN-<x>-tribunal[-rN].md` hub incl. `237-f4-tribunal.md`, `12-f15-tribunal.md`, `17-f15-tribunal-r2.md`, `63-routing-tribunal.md`; no match for `236-draft-…`, `238-…-opus-seat`, `239-…-derive`, `249-…-preflight`, `13-…-anthropic-seat`, `250-draft-…`, `251-…-card`, `252-…-preflight` | OK |
| 12 | 237 lines 1, 9, 39, 41, 43 | unchanged by the amend; shapes match the card | OK |
| 13 | `CHECK-HUB.md:10` | three `HOUSE` prefixes; no new string | OK |
| 14 | tests file anchors `:28 :223 :250-264 :1187-1218 :1221-1273 :1223 :1240` | unchanged (tests file untouched) | OK |
| 15 | red (1) on BASE | worker seat → G7 `route: the desk launches` | OK |
| 16 | negative controls (2), (3), (4) green on BASE | unchanged | OK |
| 17 | green (2) after change | unchanged | OK |
| 18 | X3 reach beyond the prefix | gate `launches == [0]` and `HOUSE.match(command)` then G1; unchanged | OK |
| 19 | test (5) red/green | now stated: `&&` RED on BASE (G7 `:1036` before G1 `:1038`), green after; `git push` G4 GREEN on both (`:1031`); the "Only (1) and the `&&` case of (5)" sentence agrees with the code | OK |
| 20 | header comment `:22-23` G9 clause | present at `:22-23` | OK |
| 21 | no new allow line, setting or command | NOT IN THIS JOB unchanged | OK |
| 22 | `restarts.py` classes for the two files | unchanged; both files have a class home | OK |

## ISSUES
1. NOTE (11): the pattern still misses older hub names (`2026-09-19/08-tribunal-archiver*.md`, `2026-09-21/27-setups-tribunal-r1b.md`, `41-reissue-handicap-tribunal-q17.md`); no live hub is among them; the card now asks this as X5.
2. NOTE: not run here: `uv run cobalt jobs restarts <BASE>..HEAD` and all pytest; the builder quotes `RESTARTS: none`.

PREFLIGHT DONE · card: tribunal-guard-1010 · checks: 26 · fails: 0 · ready: YES
