# Preflight — card 723 `test-llm-reds-1018` (read-only, 2026-10-18)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt log --oneline -2 -- "docs/40 - DevDocs/prompts/2026-10-18/723-test-llm-reds-card.md"` | `75dcdb5f docs(desk): R1839 cards 721 and 723 and preflight prompts` (committed) | OK |
| 2 | `git -C /Users/cobalt/cobalt diff HEAD --stat -- <card>` and `git status --short -- <card>` | both empty (card unchanged vs HEAD) | OK |
| 3 | header vs `CARD.md` build column | JOB, LADDER, BRANCH, WORKTREE, BASE `279c99ce` (8 hex), TIP empty, REPORT absolute in worktree, CHECK REPORT empty, HOUSE B empty, BAND `MID` (card dated 10-18), RULINGS `2026-10-18 R1833` all present, plus CLASS K5, INSTALL none, RESTARTS none | OK |
| 4 | `grep -n "«FILL\|TBD\|TODO\|XXX\|<FILL\|«" <card>` | no output (only BASE set, TIP empty by design) | OK |
| 5 | `git -C /Users/cobalt/cobalt rev-parse --short=8 279c99ce` and `git diff 279c99ce HEAD --stat -- tests/test_llm.py src/cobalt_agent/config.py src/cobalt_agent/llm.py` | `279c99ce`; diff empty (HEAD is now `4f130ff1`, 3 desk doc commits past BASE, no code) | OK |
| 6 | `grep -n "load_config" tests/test_llm.py` | 9 lines: 38 59 69 97 119 151 194 203 219, all `patch("cobalt_agent.config.load_config")`; each sits in the card's named test (defs at 36 46 67 95 117 143 170 201 210) | OK |
| 7 | `grep -n "def _load_config\|def get_config\|def load_config" src/cobalt_agent/config.py` | `525 _load_config`, `664 get_config`, no `load_config` | OK |
| 8 | `grep -n "get_config\|import completion\|/v1\|..." src/cobalt_agent/llm.py` | `:47` and `:85` `from cobalt_agent.config import get_config` (local, call-time); `:81` `f"{protocol}://{ip}:{port}/v1"`; `:163` local `from litellm import completion`; `:12` also a module-level `from litellm import completion` (the `cobalt_agent.llm.completion` attribute exists, so the patch applies but is not the name `:164` calls) | OK |
| 9 | `grep -n "llm.completion\|_api_base" tests/test_llm.py` | patches at `:102 :124 :156 :227`; `:199` `assert llm._api_base == "http://192.168.1.100:11434"`; `:208` `is None` | OK |
| 10 | `git diff d601b1f6 HEAD -U0 -- src/cobalt_agent/config.py` | two hunks, `openrouter_api_key` mapping and a vault-loop skip; no `load_config` line (matches jev-shadow-build `:85`) | OK |
| 11 | report anchors: `grep -n` of `jev-shadow-build-2026-10-15.md` (`:85`, `:203`), `cto-2026-10-15.md:36` (R1598), `brain-direction-2026-10-02.md:299`, `jev-check-card-preflight-2026-10-15.md:44` | all carry the cited text (9 failed / `load_config`; R1598; defect card; N6). `jev-shadow-build:92` named in READ not read here | OK |
| 12 | red-first per row (read against `llm.py` and the test bodies) | T1 red = 9 `AttributeError` ids, named, command given. T2 and T3 are PREDICTED and the card builds each only after a proved red, else `NOT NEEDED` with the run quoted (card rows T2, T3, L70). Code agrees with both predictions: `:163` rebinds `completion` from `litellm` at call time; `:81` adds `/v1`. Z1 says `RUN — asserts nothing` | OK |
| 13 | test-pin rule (CARD.md `HOW A CARD CITES AND PINS`) | edits existing tests by content (`patch(` lines, one string); no whole-file pin, no BASE hash in any row; DEPLOY PROOF counts are `grep -c` of the changed lines (9/0), the suite gate is `0 failed`. `d601b1f6` appears in the T1 prose as a cited commit of the recorded diff, not as a pin | OK |
| 14 | `grep -c "claude \|--allowedTools\|desk-launch" <card>`; read of the 4 `uv run` hits | the 4 `uv run` hits are the test and `cobalt jobs restarts` commands inside rows T1/Z1/DEPLOY PROOF; no launch line, allow string, model or permission mode (R411, R412) | OK |
| 15 | K10 RESTARTS class home: `src/cobalt/jobs/restarts.py:245-246` | every file the rows touch is `tests/test_llm.py` → `tests/` prefix → `test/documentation; no resident`; the build report is under `docs/` → `DOCS` (`:225-229`); no `src/` file → `RESTARTS: none` as the header says. `readers_of` has no registry entry for a test file | OK |
| 16 | overlap: `grep -ln "tests/test_llm.py\|src/cobalt_agent/llm.py\|src/cobalt_agent/config.py" prompts/2026-10-18` and branch/worktree names of 717, 718, 719, 721 | only 717 names `src/cobalt_agent/config.py`, as "untouched"; no card edits `tests/test_llm.py`; branches and worktrees all distinct; worktree `test-llm-reds-1018` and branch `test/test-llm-reds-1018` do not exist yet (the builder creates them) | OK |
| 17 | deploy readiness: `## DEPLOY PROOF` against `deploy-card.sh:29-30,534-543` | two marker lines (`· before 0 · after 9`, `· before 9 · after 0`, `grep -c -F … <absolute path>`) and one smoke line (label · command · green) | OK |

## ISSUES
- NOTE 1: the grep markers read `/Users/cobalt/cobalt/tests/test_llm.py` on main; they differ before/after only once the merge lands, as intended (before: 0 and 9 on main now, verified by check 6).
- NOTE 2: `K10`, `R411`, `R412` are not defined in `ops/desk` text I could grep; check 14 and 15 rest on the rule as the prompt states it and on `restarts.py`, not on the rule's own file.
- NOTE 3: T2 and T3 are predictions; the card handles a miss (`NOT NEEDED`). Any red after T1 outside T2/T3 goes to `## DECISIONS`, UNPROVEN.
- NOTE 4: what blocks this card's own deploy: nothing in the card. It needs its build, then its check (`CHECK REPORT`, `HOUSE B` and `TIP` are the desk's to fill), then a deploy card; no desk commit on main while a deploy hub runs.

PREFLIGHT DONE · card: test-llm-reds-1018 · checks: 17 · fails: 0 · ready: YES
