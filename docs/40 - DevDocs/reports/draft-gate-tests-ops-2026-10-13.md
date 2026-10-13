## §0 Headline
Card `gate-tests-ops-1013` drafted: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/521-gate-tests-ops-card.md` (520 was taken; the desk's message moved it to 521). BASE `91ecb686`, one row T1, three files.
`## OFFLINE` gets `tests/ops` and the same word on `BUILD-HUB.md` `## E0` line 65; a new pin ties the two together.
`tests/ops` is 3544 tests on BASE and ran green here (3543 passed, 1 xfailed, 849 s), so the offline leg grows by about 14 minutes.
Four decisions for the desk.

## DECISIONS
- ASK DESK 1: the G1 guard (`tests/cobalt/conftest.py:75-78`) and `--db-only` live in `tests/cobalt/conftest.py`, so a with-DB test added to `tests/ops` is neither refused nor reached by PASS 1. Default: not this card; the card says a with-DB `tests/ops` test stops as `ASK DESK`. [before the build launches]
- ASK DESK 2: no R-row for L79 was found in the files read, so the card says `RULINGS: none`. Default: `none`; the desk writes the row if one exists. [before the build launches]
- ASK DESK 3: `BUILD-HUB.md:65` (`## E0`) holds the same OFFLINE command and is pinned equal by nothing today (`BUILD-HUB.md:82` holds no command, so `hub_commands()` never reads it). Default: the card edits that one line and adds the pin, so the hub is a file of the row. [before the build launches]
- ASK DESK 4: every gate, build W and deploy, now spends about 14 minutes more in the offline leg (849 s for `tests/ops` alone, 2026-10-13). Default: accept; `gate.sh` runs it under `run_in_background` with `timeout` 7200000. [before the first deploy after this card]

## RECORDS
- Reads: HEAD `91ecb686`, `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`. Shape from `446-k5-gate-card.md` (header, ROWS, NOT IN THIS JOB, READ, CHECK ASKS, DEPLOY PROOF, RECORDS) and the header table of `CARD.md:9-29`.
- `tests/ops` exists at HEAD: `git ls-tree --name-only HEAD tests/ops/conftest.py tests/ops/test_gate.py tests/conftest.py` → all three.
- `gate.sh` reads `gate-lists.md` only: `ops/desk/gate.sh:156-159`, `:182`, `:397-400`, `:506`, `:509`; stub proof `tests/ops/test_gate.py:443-446`.
- Texts holding the command: `gate-lists.md:18` (edit), `:24` PASS 1 (stays), `BUILD-HUB.md:65` (edit), `tests/ops/test_pass1_db_only.py:5` and `:36` (stay; `:36` pins PASS 1). No hit in `DEPLOY-HUB.md`, `CARD.md`, `.claude/`, `CLAUDE.md`. Dated cards (`2026-09-*`, `2026-10-02/25`, `2026-10-03/01`, `2026-10-06/04`) hold it too: history, not edited.
- `--db-only`: registered `tests/cobalt/conftest.py:91-100`, keep rule `:81-88`. `grep -rn -E "skipif|pytest.skip|importorskip" tests/ops` → one hit, `test_fetch_voice_models.py:133` (a model file, not a database). PASS 1 and LIVE-NOTE unchanged.
- BASE count: `uv run pytest -q tests/ops --collect-only` → `3544 tests collected in 1.50s`.
- Full run on BASE working tree: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3543 passed, 1 xfailed, 16 warnings in 849.08s (0:14:09)`, exit 0. No test failed, so no resident or network test needed an `ASK DESK`; the offline and live paths were not separately classified beyond that. The run was on the working tree (docs, `.claude/settings.json`, `configs/cobalt/rules.yaml` modified; nothing under `ops/` or `tests/`).
- RESTARTS homes: `ops/desk/` → `src/cobalt/jobs/restarts.py:38`, `:230-232`; `docs/` → `:225-228`; `tests/` → `:246`. Expected `RESTARTS: none`.
- Not proven: the planted-red steps and the `restarts` run are the build's (the drafter wrote and deleted no test file; no git write).

DRAFTED · decisions: 4
