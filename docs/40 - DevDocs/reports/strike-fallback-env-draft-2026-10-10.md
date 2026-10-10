# strike-fallback-env draft — 2026-10-10

## §0 Headline
- Card written: `prompts/2026-10-09/215-strike-fallback-env-card.md`, rows A (ORDER) and B (LOUD), one feature.
- Every file:line proved at `975345f3`; `git diff --stat 975345f3 HEAD -- src tests ops` printed nothing.
- `BASE` is `«FILL»` for the desk; `TIP`, `CHECK REPORT`, `HOUSE B` empty; `DB` omitted.
- Nothing launched, no git write, no database touched.

## CHANGES
- NEW `docs/40 - DevDocs/prompts/2026-10-09/215-strike-fallback-env-card.md`.
- NEW this report.
- Row A: explicit `load_dotenv(Path(__file__).resolve().parents[3] / ".env")` in `aset/__main__.py` before `start_fallback_thread()`; red test through `runpy` with stubs; negative control still fails loud.
- Row B: repeating ERROR (`REPEAT_ERROR_S = 60.0`, with count), one `recovered after <n> failed passes` INFO, one `first pass OK` INFO; `FallbackThread` gets a `monotonic` keyword and a `step()` method so tests need no thread.

## DECISIONS
1. Order: explicit `.env` load in `__main__.py`, not starting the thread from the app's startup after `cobalt.aset.web` imports. Default taken. The alternative works but moves thread lifetime into uvicorn's lifespan.
2. `override` stays `False` (as `cli.py:59`): a variable already in the environment wins over `.env`.
3. The repeat period is a code constant `REPEAT_ERROR_S = 60.0`, not config (the card fences config out).
4. A failure text that differs from the last logs at once, regardless of the 60 s.
5. `first pass OK` logs only when the first pass succeeds; a first pass that fails gets its `recovered` line instead.
6. A missing `.env` file adds no log line of its own: the loud failure is the first pass's ERROR from row B (negative control A2).
7. The thread seam is a new `step()` method plus a `monotonic` keyword; existing `test_the_thread_logs_a_failed_pass_and_goes_on` stays green unchanged.

## RECORDS
- Read `CARD.md`, `206-archiver-429-card.md` and `writing-rules.md` whole (2026-10-10).
- `git -C /Users/cobalt/cobalt show 975345f3:` read whole: `src/cobalt/aset/__main__.py`, `src/cobalt/aset/strike.py`, `src/cobalt/cli.py`, `src/cobalt/db.py`, `tests/cobalt/test_strike_fallback.py`, `tests/conftest.py`.
- `git -C /Users/cobalt/cobalt grep -n` at `975345f3`: `__main__.py:52` import, `:54` call, `:57` `uvicorn.run`; `strike.py:485` `pass_once`, `:521` `FallbackThread`, `:535–546` `run` (`:543` the new-message test, `:545` `last_error = text`), `:549` `start_fallback_thread`; `cli.py:52` import, `:59` the load (`parents[2]`); `cobalt_agent/config.py:21` `load_dotenv()`; `db.py:136` `DbConfigError`, `:160` `_open`, `:168` `POSTGRES_HOST`, `:103` `Credential.APP`.
- `parents[3]` for `src/cobalt/aset/__main__.py` is the repo root (aset, cobalt, src, root).
- `tests/conftest.py:13` runs `load_dotenv()`, so the red test clears the three variables itself.
- No test references `cobalt.aset.__main__` at `975345f3` (`git grep`), so row A's test is new and uses `runpy`.
- `reports/cto-2026-10-10.md` R828 exists (line 7). `aset.err` line 10373 is the brain's read; not opened.
- `jobs.yaml:39` carries `com.cobalt.aset`; RESTARTS expectation in the card is from the prompt, the builder runs the command.
- The `runpy` test of row A has not been run; the builder confirms `load_config()` works offline there.

STRIKE FALLBACK CARD DRAFTED · decisions: 7
