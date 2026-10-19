# f21-vectors-fix-preflight (2026-10-19)

Card `f21-vectors-1013` (469) row F1. `date` → Mon Oct 19 19:33:13 EDT 2026. Read-only; no test run, no git write.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt diff --stat HEAD -- <469 card>` | empty | OK |
| 2 | `git -C /Users/cobalt/cobalt log --format=%h%x20%s -4 -- <469 card>` | newest `0a513165 docs(desk): 469 O1 fix-round row drafted…`: the card is committed with F1 in it | OK |
| 3 | `grep -c -F "«FILL" <469 card>` | `0` | OK |
| 4 | `git -C … diff 021100c7 HEAD -- <469 card>` (021100c7 = the commit that set TIP) | three hunks only: the F1 row (after V5), CHECK ASKS X4 and the G1/G2 line, one RECORDS bullet. No hunk touches lines 1-13: BASE `9436c975`, TIP `c772a516`, CHECK REPORT, HOUSE B `as needed` and the header all unchanged. BAND: the card has no BAND line, before or after (the card is dated 2026-10-13, so none is required by `CARD.md`) | OK |
| 5 | `git -C … rev-parse ops/f21-vectors-1013` | `c678dda0eae9222e82cd1d13f75074a4f13f9b3e`, equals the row's "code tip now `c678dda0`" | OK |
| 6 | `git show ops/f21-vectors-1013:src/cobalt/voice/registry.py` plus `grep -n` on the worktree | `:85` `def load_agent`, `:99` `from cobalt.modelaccess import load_routes` (lazy, inside the function), `:101` `routes = load_routes().routes`, `:102` `if spec.route not in routes:`. All four as the row states. The file has no `Route` import today | OK |
| 7 | `git show ops/f21-vectors-1013:src/cobalt/modelaccess/config.py` plus `grep -n` | `:43` `class Route`, `:47` `kind: Literal["openai_compatible"]`, `:99` `class EmbedRoute`, `:110` `kind: Literal["openai_embeddings"]`, `:178` `__all__` carries `Route` and `EmbedRoute`. `AnyRoute` is the discriminated union, so `routes[spec.route]` is a `Route` or an `EmbedRoute` instance and `isinstance(…, Route)` separates them | OK |
| 8 | `git show ops/f21-vectors-1013:src/cobalt/modelaccess/__init__.py` | exports `call`, `call_sync`, `embed_sync`, `load_routes`, `EmbedResult`, `ModelCallError`, `ModelMessage`, `ModelRequest`, `ModelResult`; no `Route`. So the import path `cobalt.modelaccess.config.Route` is the right one and is needed | OK |
| 9 | `git show ops/f21-vectors-1013:tests/cobalt/test_voice_config.py` plus `grep -n` | `:14` `import pytest` (used by `pytest.mark.parametrize` and `pytest.fixture` elsewhere), `:358` the `@pytest.mark.xfail(strict=True, reason="check O1 HELD, NOT FIXED — …")` line, `:359-361` the test (`def`, `with pytest.raises(vr.AgentConfigError):`, `vr.load_agent(_agent(tmp_path, route="local.embed"))`). The row's "one line" and "stays byte for byte" are right | OK |
| 10 | the O1 fix reaches the test | `_agent(tmp_path, route="local.embed")` builds a valid agent file, so `AgentSpec` passes and `local.embed` is in `routes` (modelaccess.yaml has it at the tip). Only the new `isinstance` guard can raise. The committed agent route is `local.plan` (a `Route`), so `test_committed_agent_is_the_v1_allowlist` stays green | OK |
| 11 | `grep -c -F "FIXED: O1 — tests/cobalt/test_voice_config.py::test_the_route_must_be_a_chat_route_not_the_embed_route" <469 card>` | `1`: one FIXED line, one held id (O1). G1 and G2 are REJECTED in the check's `## OPEN` / `## RUNS`, so no line for them. The id equals the check's `## OPEN` O1 test name | OK |
| 12 | underscores in the resume step text | F1 has no resume step; its last step is the stop line `BUILT`. The only underscores are in test ids, file names and symbol names | OK |
| 13 | `files` cell of F1 | `src/cobalt/voice/registry.py` (the guard after `:102`) and `tests/cobalt/test_voice_config.py` (the mark at `:358`). `registry.py` is in no other row's files (V1 names only `modelaccess/` files); F1 says so and adds it as a one-line addition | OK |
| 14 | order of F1 steps | (1) the guard, (2) drop the mark, FIXED line, then RUN only `tests/cobalt/test_voice_config.py tests/cobalt/test_modelaccess_config.py` and the deploy gate (L75), quote both, stop line `BUILT`, "No re-check; then the deploy" | OK |
| 15 | RED cell | red on the tip: `DID NOT RAISE <class 'cobalt.voice.registry.AgentConfigError'>` (check `## RUNS` O1, red commit `736beb73`); green after the guard with the mark gone; strict xfail goes red the moment the fix lands. Matches the check report | OK |
| 16 | `git log --format=%h%x20%s c772a516..ops/f21-vectors-1013 -- src` | empty: no `src` change on the branch past the build tip, so F1 builds on code equal to the build's | OK |
| 17 | CHECK ASKS X4 | present; asks the raise on `local.embed`, the committed agent on `local.plan`, the mark gone, the body unchanged, and the two files as the only F1 change | OK (NOTE 2) |
| 18 | RULINGS and RESTARTS | header RULINGS `2026-10-11 R1055` unchanged. F1 touches `voice/registry.py` (statically reached from `com.cobalt.radar` by `voice.cli` → `voice.turn` → `voice.agent` → `voice.registry`) and one test; the build's `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` (check `## Suites`) already covers it | OK |
| 19 | drafter decision 1 (no SETTLED line for G1 and G2; one CHECK ASKS line points at the drafter report) | Judged: ACCEPT. The check reports G1 and G2 as REJECTED, not held; the F1 scope is O1 only ("Nothing more than O1"); a SETTLED row is the desk's text, which the check did not supply | OK |
| 20 | drafter decision 2 (lazy import `from cobalt.modelaccess.config import Route` beside `:99`, message left to the builder) | Judged: ACCEPT. Same lazy placement keeps `registry.py` import-light as it is today; `Route` is not exported by the package, so the `config` path is the only one; the check asks only for `AgentConfigError` | OK |

## ISSUES
- NOTE 1: the row names "the original builder `aa4b75c7`" and "his R347"; neither is in a file I may open under this order (the build report's commit and the cto day file). Not checked; neither is read by the build or the deploy.
- NOTE 2: the G1/G2 line is placed under `## CHECK ASKS` without an `X` number, while `CARD.md` says `## CHECK ASKS` lines are numbered X1, X2 …. Harmless: the line is labelled and the check pass for F1 is not launched ("No re-check").
- NOTE 3: the card carries no `BAND` line. It is dated 2026-10-13, before the 2026-10-16 rule, so `desk-launch.sh` does not require one.
- Blocks the build: nothing found.

PREFLIGHT DONE · card: f21-vectors-1013 · checks: 20 · fails: 0 · ready: YES
