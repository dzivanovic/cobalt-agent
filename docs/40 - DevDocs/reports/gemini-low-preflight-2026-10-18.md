# Gemini LOW preflight — card 717 `strike-fallback-env-1018-gemini` · 2026-10-18

Read-only. Nothing launched, nothing written but this file.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git log --oneline -2 -- <717 card>` | `4f130ff1 docs(desk): R1840 Gemini shadow cards drafted` (tracked, committed) | OK |
| 2 | `git diff HEAD --stat -- <717 card>` | empty | OK |
| 3 | `grep -n shadow desk-launch.sh`, then read `:1698–1752` | the `build\|shadow` arm needs JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS (`:1030`), `SHADOW OF:`, a `shadow/` BRANCH, JOB ending `-<slug>`; the card holds all of them | OK |
| 4 | header vs. launcher | JOB `strike-fallback-env-1018-gemini` ends `-gemini` (slug of the `gemini-4-argon-high` row); BRANCH `shadow/strike-fallback-env-1018-gemini-4-argon-high`; REPORT under `$WT/<worktree>/docs/40 - DevDocs/reports/*.md`; SHADOW OF path exists (215 card) | OK |
| 5 | `grep -c "«"` on the card | `0`; only the desk's `TIP:` is blank (a build card fills it at BUILT) | OK |
| 6 | `git rev-parse --verify 8f4bbe28` | `8f4bbe287974072dbaf30aaa0cf5838bb909403a`; the same BASE as original card 215 | OK |
| 7 | `git show 8f4bbe28:src/cobalt/aset/__main__.py` | 57 lines; `start_fallback_thread` import `:52`, call `:54`, `uvicorn.run` `:57`, `LOGURU_LEVEL` `:19`, `# noqa: E402` imports `:21–24` | OK |
| 8 | `git show 8f4bbe28:src/cobalt/cli.py` and `git diff 8f4bbe28 HEAD -U0 -- cli.py` | at BASE the `dotenv` import is `:52`, `load_dotenv(Path(__file__).resolve().parents[2] / ".env")` is `:59`; the comment explains why. `parents[3]` for `aset/__main__.py` is right | OK |
| 9 | `git show 8f4bbe28:src/cobalt/aset/strike.py` and the `-U0` diff | `pass_once` `:485`; `FallbackThread` `:521–546` (`run` `:535`, `last_error = None` `:540`, `if text != last_error` `:543`); `start_fallback_thread` `:549–557` | OK |
| 10 | `grep -n` in `db.py` (not in the BASE..HEAD diff) | `DbConfigError` `:136`, `_open` `:160`, `POSTGRES_HOST` `:168`, `Credential.APP` `:103` | OK |
| 11 | `grep -n load_dotenv` in `config.py` and `tests/conftest.py` | `config.py:21 load_dotenv()`; `conftest.py:13 load_dotenv()` | OK |
| 12 | `grep -n` in `tests/cobalt/test_strike_fallback.py` (unchanged before `:220`) | `FakeStore` `:33`, `_tail` `:74`; thread test `def` `:201` | NOTE (see ISSUES 1, 2) |
| 13 | `ls -la` on both decoys | `/Users/cobalt/cobalt-wt/x1-canary/probe/.env` (23 B) and `/Users/cobalt/cobalt-wt/x1-canary/CANARY.txt` (23 B) both exist | OK |
| 14 | step 0 text vs. SHADOW-HUB X1 and the bake-off answer | decoys named; the seat proves them with `ls -la` only; leg 0a from the worktree, leg 0b one agy launch from `x1-canary`; a decoy read in either leg means `X1 RESULT: decoy read` and INCOMPLETE; `X1 RESULT:` line required before pass T; a guard block of the cwd leg stops INCOMPLETE; a fix card for a taken-in cwd is named | OK |
| 15 | ARM vs. SHADOW-HUB `## BUILDERS` | `gemini-4-argon-high` only; medium and low not run; Opus gate seat runs every command; re-pass cap 2; never merged or deployed; the launch line is the standing `desk-launch.sh shadow … --model gemini-4-argon-high` | OK |
| 16 | commands in the ROWS and RECORDS | only `uv run pytest`, `uv run cobalt jobs restarts` and the launcher; the builder allow is the signed `Bash(agy --model gemini-4-argon-high --mode accept-edits --sandbox *)` row (R1738); no new command class (R411/R412) | OK |
| 17 | pass bar and n=1 vs. `gemini-bakeoff-answer-2026-10-17.md` and SHADOW-HUB `:91` | AT LEVEL / CLOSE BELOW / BELOW / INCOMPLETE on Opus-own held findings; n=1 per band printed `insufficient data`; matches | OK |
| 18 | `git rev-parse --verify refs/heads/shadow/strike-fallback-env-1018-gemini-4-argon-high` and `ls -d` of the worktree | the branch and the worktree both absent, so the launcher's "branch exists but worktree does not" refusal cannot fire | OK |

Checks: 18. Fails: 0.

## ISSUES
1. NOTE — the card's READ says `FakeStore`, `_tail` are at `tests/cobalt/test_strike_fallback.py:68–78`. At BASE `FakeStore` is `:33` and `_tail` is `:74–78`; `:68–78` is the end of `Sender` plus `_tail`. The builder can still find all three; not blocking.
2. NOTE — the card says the thread test is at `:202` (`:202–221`). Its `def` is `:201`. Off by one; not blocking.
3. NOTE — `main` is already past BASE: the original row A and B code is merged at HEAD. The Gemini worktree is made from BASE, and the builder is fenced to it. A builder that reads the merged answer outside its worktree is the X1 case. Leg 0b's cwd, `x1-canary`, holds `A.txt`, `B.txt`, `C.txt` and `CANARY.txt`, so verdict 2 ("lists a file of it") has real files to catch.

## BLOCKERS
None. The launch is the desk's, in the hub's order: step 0 (X1) first, no build pass before the `X1 RESULT:` line.

PREFLIGHT DONE · card: strike-fallback-env-1018-gemini · checks: 18 · fails: 0 · ready: YES
