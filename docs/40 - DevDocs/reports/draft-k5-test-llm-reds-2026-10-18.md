## §0 Headline
- Card written: `prompts/2026-10-18/723-test-llm-reds-card.md`, BASE `279c99ce` (= `main` HEAD, `git rev-parse --short=8 main`), RULINGS `2026-10-18 R1833`, JOB `test-llm-reds-1018`.
- The 9 reds are one STALE TEST cause: `tests/test_llm.py` patches `cobalt_agent.config.load_config`, which does not exist; the code reads `get_config` (`llm.py:47`, `:85`; `config.py:664`). No code defect proved.
- Rows: T1 (patch target, 9 lines, recorded red), T2 and T3 (predicted from the code, built only on a proved red), Z1 (run).
- Nothing run, nothing committed.

## DECISIONS
1. `ASK DESK: T2 (patch("cobalt_agent.llm.completion") is not the function called, llm.py:163 imports completion locally; 4 tests) and T3 (expected api base lacks the /v1 that llm.py:81 builds; 1 test) are read from the code, not from a recorded failure. [06:25 EDT]` Default: the card builds each only if its red is proved after T1, else reports NOT NEEDED.
2. `ASK DESK: BAND set to MID (one test file, but T2 and T3 are unproven; when unsure, the higher band). [06:25 EDT]` Default: MID; LOW is fine if he wants it.
3. `ASK DESK: the fix edits an old-tree test (strangler rule: old tree untouched). jev-shadow-1015 already edited src/cobalt_agent. [06:25 EDT]` Default: fix the test; no retirement.

## RECORDS
- Evidence: `reports/jev-shadow-build-2026-10-15.md:85`, `:203` (9 failed, all `AttributeError … 'load_config'`); `reports/cto-2026-10-15.md:36` (R1598); `reports/brain-direction-2026-10-02.md:299`; `reports/jev-check-card-preflight-2026-10-15.md:44`. Grep of the 10-15, 10-16 and 10-17 reports found no per-test failure list, so the 9 tests are named from the 9 `load_config` lines of `tests/test_llm.py` (`:38 :59 :69 :97 :119 :151 :194 :203 :219`), a match of the recorded count.
- `git status --short` on the three files printed nothing; `date` → 2026-10-18 06:21 EDT.

DRAFTED · decisions: 3
