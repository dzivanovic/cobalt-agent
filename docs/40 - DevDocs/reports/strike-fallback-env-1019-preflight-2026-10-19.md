# strike-fallback-env-1019-gemini — preflight of card 855 (2026-10-19)

Card: `prompts/2026-10-19/855-shadow-strike-fallback-env-1019-gemini-card.md` (61 lines). main = `72a26b15`.

## CHECKS

| # | command · output | result |
|---|---|---|
| 1 | `grep -n "«\|FILL"` on the card · only `:5 BASE: «FILL: BASE, the desk's 8-hex main commit»` (`:56` matched `<BASE>..HEAD`, which is prose, not a token) | OK |
| 2 | `grep -n -i "0a\|0b\|x1-canary\|VERDICT\|PASSES\|two-leg\|leg "` · only `:20` (the one STEP 0 line, byte-equal to the prompt's) and `:27` (row B text `"legs"` in an unrelated sense: no old-leg text) ; no `x1-canary`, no VERDICT/PASSES rows left | OK |
| 3 | `git grep -n` of hub `:30` on main · `:30` is `X1 for Gemini … six legs, 0a to 0f … one agy launch per leg … x1-copy`; the VERDICT list (1)–(7) and the "`## PASSES` rows 0a to 0f" live in the hub line; the card now defers to it ("its verdict is the hub's") | OK |
| 4a | card `:2–:4` · JOB `strike-fallback-env-1019-gemini`, BRANCH `shadow/strike-fallback-env-1019-gemini-4-argon-high`, WORKTREE `strike-fallback-env-1019-gemini`: all 1019 names | OK |
| 4b | `git log --oneline -1 shadow/strike-fallback-env-1018-gemini-4-argon-high` · `0ae4e818 wip(strike-fallback-env-1018-gemini): PREFLIGHT — head 2eef34ac is a docs commit…`; the card names it only as kept evidence (`:60`) | OK |
| 5a | `git grep -n load_dotenv main -- src/cobalt/cli.py` · `:53 import`, `:60 load_dotenv(...parents[2]/".env")`; card says `cli.py:52–59` and `:50–59` | FAIL (shifted: now 53/60) |
| 5b | `git grep -n main -- src/cobalt/aset/__main__.py` · 66 lines (card: "57 lines"); `load_dotenv` already at `:24` import, `:30` call; `start_fallback_thread` import `:61`, call `:63`, `uvicorn.run` `:66` (card: `:52/:54/:57`) | FAIL (stale; fix already present) |
| 5c | `git grep -n main -- src/cobalt/db.py` · `DbConfigError :136`, `_open :160`, `POSTGRES_HOST :168`, `Credential.APP :103` | OK (4 refs) |
| 5d | `git grep -n main -- src/cobalt_agent/config.py` · `:21 load_dotenv()` | OK |
| 5e | `git grep -n main -- tests/conftest.py` · `:13 load_dotenv()` | OK |
| 5f | `git grep -n main -- tests/cobalt/test_strike_fallback.py` · `FakeStore :33`, `_tail :74`, thread test `:201` (card: `:68–78`, `:202–221`) | FAIL (shifted) |
| 5g | `git grep -n main -- src/cobalt/aset/strike.py` · `FallbackTail :469`, `pass_once :485`, `FallbackThread :527`, `__init__ :534` already has `monotonic`, `run :575`, `start_fallback_thread :581` (card: `:485 ok`, `:521–546`, `:535–546`, `:549`); `step()`/`REPEAT_ERROR_S`/`recovered`/`first pass OK` already present (6 hits) | FAIL (stale; row B already built) |
| 5h | `git ls-tree main …` · `215-strike-fallback-env-card.md`, `206-archiver-429-card.md` exist; `tests/cobalt/test_strike_fallback_env.py` ALREADY EXISTS on main (card row A: "NEW file") | FAIL |
| 5i | `grep R828 cto-2026-10-10.md` on main · `:183 R828` present (brain's read, DbConfigError) | OK |
| 6 | headers of 718/719 vs 855 · same set JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT, HOUSE B, RULINGS, SHADOW OF; 855 has `CHECK REPORT :8`, `HOUSE B: as needed`; no `MODEL`/band header in any of the three (consistent) | OK |
| 7 | rows A and B in card `:26–:27` · both carry a "red first" cell with RED lines (`RED on BASE: DbConfigError…`, `TypeError… 'monotonic'`) and a files cell | OK (present) — but see issue 1: not red on main |
| 8 | `git log -1 -- <card>` · `72a26b15`; `git diff --stat -- <card>` empty | OK (committed, clean) |

## ISSUES
- BLOCKS THE LAUNCH (FAIL 5b, 5g, 5h, 7): the work of rows A and B is already on main, merged as `b3d59b5f fix(strike-fallback-env-1010)`: `__main__.py:30` loads the repo env before `:63 start_fallback_thread()`, `strike.py` has `monotonic`, `REPEAT_ERROR_S` and the recovered / first-pass INFO lines, and `tests/cobalt/test_strike_fallback_env.py` exists. The card's header rule (the desk fills BASE with main HEAD `72a26b15`) makes the RED lines false: A1 and B1–B5 would be green on BASE, nothing to build, and the shadow grades nothing.
- FIX: the card's BASE must be the pre-fix commit the 1018 card used, `8f4bbe28` (`git grep -c` for `load_dotenv` in its `__main__.py` and for the new `strike.py` names prints nothing there: the fix is absent). The desk should fill BASE with `8f4bbe28`, not main HEAD, and the line numbers in the card are correct as of that BASE; re-prove 5a/5b/5f/5g against `8f4bbe28` (not done here) before the launch. A shadow of a merged card also needs its builder worktree cut from `8f4bbe28`, and the desk-launch BASE rule (`main HEAD`) overridden for this card.
- NOTE: line numbers in rows A/B, READ and RECORDS match `8f4bbe28`'s tree (the card says "main's"), not main now; the RECORDS line `:54` ("lines above are main's") is wrong today.
- NOTE: the old 1018 branch is intact at `0ae4e818` and untouched.
- NOTE: card 855 is committed (`72a26b15`) with the amend; STEP 0 and the placeholder checks pass.

PREFLIGHT DONE · card: strike-fallback-env-1019-gemini · checks: 17 · fails: 5 · ready: NO
