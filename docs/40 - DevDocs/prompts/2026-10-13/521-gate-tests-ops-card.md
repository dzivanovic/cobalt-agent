JOB: gate-tests-ops-1013
LADDER: OFF-LADDER — brain L79 2026-10-13 15:00 ET
CLASS: K5
INSTALL: none
BRANCH: ops/gate-tests-ops-1013
WORKTREE: gate-tests-ops-1013
BASE: 91ecb686
TIP:
REPORT: /Users/cobalt/cobalt-wt/gate-tests-ops-1013/docs/40 - DevDocs/reports/gate-tests-ops-build-2026-10-13.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/gate-tests-ops-check-2026-10-13.md
HOUSE B: as needed
DB: none
RESTARTS: none
RULINGS: 2026-10-13 R1436 (brain L79: the gate's offline leg runs tests/ops)

## ROWS

WHY: brain L79 (2026-10-13 15:00 ET: "the gate's offline leg must include tests/ops; K5 card, ahead of gap-fillers"). A red `tests/ops` test sat on main through several deploys because `ops/desk/gate-lists.md` `## OFFLINE` (line 18) runs only `tests/cobalt tests/taxonomy`; the sweep pin (`sweep-pin-1013`) then cost six touches. `gate.sh` reads that one file for the offline leg and nothing else (`ops/desk/gate.sh:156-159` the `OFFLINE` section read, `:182` `OFFLINE=$(cat "$tmp/offline")`, `:397-400` `do_offline` runs `suite "$OFFLINE"`), so one line moves the leg.

| row | what | red first | files |
|---|---|---|---|
| T1 | THE OFFLINE LEG RUNS `tests/ops`. `ops/desk/gate-lists.md` `## OFFLINE` line 18 becomes, byte for byte, `` `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy tests/ops` `` (one backticked line, as the header of that file requires). The one other text that holds the same command is `BUILD-HUB.md` `## E0` line 65 (the BASELINE run, `` `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (`run_in_background`) → …``); it takes the same added word and nothing else on that line changes (the LIVE-NOTE command on that line stays). `## PASS 1` (line 24, `… tests/cobalt tests/taxonomy --db-only …`), `## PASS 2`, `## LIVE-NOTE` and every other section of `gate-lists.md` stay as they are: `tests/ops` has no with-DB leg (the `--db-only` option is registered in `tests/cobalt/conftest.py:91-100` and keeps only tests that carry a `skipif` mark; `tests/ops` holds one `pytest.skip` (`test_fetch_voice_models.py:133`, a model absent from the dev model_dir, not a database) and no `skipif`), and `tests/ops/test_pass1_db_only.py:36` pins `" tests/cobalt tests/taxonomy --db-only "` in PASS 1, which the edit leaves true. Backed by brain L79, `gate.sh:156-159`, `:397-400` | In `tests/ops/test_gate.py` (helpers `list_commands()` `:106`, `HUB` `:29`): (1) `test_t1_the_offline_list_runs_tests_ops` — `list_commands()["offline"] == "uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy tests/ops"`. RED on `BASE`: the list ends `tests/taxonomy`. (2) `test_t1_the_e0_baseline_line_holds_the_offline_command_byte_for_byte` — the `## E0` section of `BUILD-HUB.md` holds `` `<list_commands()["offline"]>` `` as one backticked span. GREEN on `BASE` (the two texts are equal today) and after; it fails when only one of the two is edited. Pins, GREEN before and after, whole file: `uv run pytest -q tests/ops/test_gate.py tests/ops/test_pass1_db_only.py` → `0 failed` (`test_offline_*` through the stub `uv`, `test_the_hub_holds_no_gate_command_and_points_at_the_lists_file` (`:256`, `sorted(hub) == ["fp"]`: the E0 line is not read by `hub_commands()`) and `test_the_gate_lists_pass1_holds_db_only_once_after_the_two_suites` among them). THE PLANTED RED (a proof, never committed): in the worktree write `tests/ops/test_planted_t1.py` holding `def test_planted():` and one `assert False`; BEFORE the edit `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy -k planted_t1` → no test selected, exit 5 (the offline list does not see it); AFTER the edit `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy tests/ops -k planted_t1` → `1 failed`; then delete the file and `git status --short` shows no `test_planted_t1.py`. Then the whole new list once: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy tests/ops` (`run_in_background`), quoted whole, `0 failed`. Then `uv run cobalt jobs restarts <BASE>..HEAD`, table and `RESTARTS:` line quoted, expected `RESTARTS: none` | `ops/desk/gate-lists.md` (`## OFFLINE` line only), `docs/40 - DevDocs/prompts/BUILD-HUB.md` (`## E0` line 65 only), `tests/ops/test_gate.py` |

## NOT IN THIS JOB
- `## PASS 1`, `## PASS 2`, `## LIVE-NOTE` and every other section of `ops/desk/gate-lists.md`; `ops/desk/gate.sh` (it reads the list, it is not edited); the with-DB legs (`tests/ops` has none).
- Any other line of `BUILD-HUB.md`, `DEPLOY-HUB.md` (its `(a) OFFLINE` line `:102` names no command) and `CARD.md` (no hit for the command); the dated cards and prompts that quote the old line (`prompts/2026-*/`): history, not edited.
- Any test that fails when `tests/ops` runs offline: a red `tests/ops` test found by the new list is not fixed here; the build stops `FAILED: T1 — tests/ops red on BASE — <test ids>`. A `tests/ops` test that needs a resident, a database or the network stops as `ASK DESK` with its ids.
- Any `src/` or `configs/` file; any with-DB test (`DB: none`); a new command, option or seat (R411, R412).

## READ
- `/Users/cobalt/cobalt/ops/desk/gate-lists.md` lines 1-24; `ops/desk/gate.sh` lines 150-185 and 394-400.
- `/Users/cobalt/cobalt/tests/ops/test_gate.py` lines 98-157 (`LIST_KEYS`, `list_commands`, `hub_commands`), 256-276, 440-456; `tests/ops/test_pass1_db_only.py` whole.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md` lines 64-65 (`## E0`).
- Precedent cards: `prompts/2026-10-13/446-k5-gate-card.md` (shape), `516-sweep-pin-card.md`.

## CHECK ASKS
- X1 Is the OFFLINE line of `gate-lists.md` and the E0 line of `BUILD-HUB.md` the same command byte for byte, and does `git diff <BASE>..HEAD` on those two files show the one added word `tests/ops` and nothing else?
- X2 Do `## PASS 1`, `## PASS 2` and `## LIVE-NOTE` stand byte for byte (`git diff <BASE>..HEAD -- ops/desk/gate-lists.md` holds one changed line)?
- X3 Does the planted failing `tests/ops` test leave the BASE list green and the new list red, and is no `test_planted_t1.py` left on the branch?
- X4 Does the whole new list run `0 failed` in the build's own offline leg, and what is the count it quotes against BASE's `tests/ops` 3544 collected?

## DEPLOY PROOF
- `grep -c -F "tests/cobalt tests/taxonomy tests/ops" /Users/cobalt/cobalt/ops/desk/gate-lists.md` · before `0` · after `1`
- `grep -c -F "tests/cobalt tests/taxonomy tests/ops" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · before `0` · after `1`
- the next deploy gate's log: `grep -n -F "tests/ops" <log>` → the OFFLINE command with `tests/ops`, and `offline <p>/0` with `<p>` above `0`

## RECORDS
- Reads by the drafter `draft-gate-tests-ops`, 2026-10-13, at `main` HEAD `91ecb686` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`). `ops/` and `tests/` paths were read from the working tree; `git status` at the session start listed no modified file under `ops/` or `tests/`, only `.claude/settings.json`, `configs/cobalt/rules.yaml` and `docs/`.
- `tests/ops` exists at HEAD: `git -C /Users/cobalt/cobalt ls-tree --name-only HEAD tests/ops/conftest.py tests/ops/test_gate.py tests/conftest.py` → the three paths.
- `gate-lists.md` OFFLINE line, `git -C /Users/cobalt/cobalt grep -n -F "tests/cobalt tests/taxonomy" HEAD -- ops tests .claude CLAUDE.md`: `ops/desk/gate-lists.md:18` (OFFLINE), `:24` (PASS 1, stays), `tests/ops/test_pass1_db_only.py:5` (docstring) and `:36` (pins PASS 1, stays). No hit in `.claude/` or `CLAUDE.md`.
- `gate.sh` reads that file only: `ops/desk/gate.sh:156-159` (the `OFFLINE` title → key `offline` in the `for title, key` loop, `put(key, one(title))`), `:182` `OFFLINE=$(cat "$tmp/offline")`, `:397-400` `do_offline() { suite "$OFFLINE" || exit 1; say "offline $P/0"; }`, `:506` `offline) do_offline ;;`, `:509` `all) do_offline; do_withdb; do_livenote ;;`. `tests/ops/test_gate.py:443-446` proves the stub run: the call's argv equals `argv_of(list_commands()["offline"])[1]`, so the existing test follows the edited line.
- Texts outside `ops/` that hold the command, `grep -n -F "tests/cobalt tests/taxonomy"` under `docs/40 - DevDocs/prompts/` (undated files and `2026-10-*`): `BUILD-HUB.md:65` (`## E0`, the one live hub hit, the same OFFLINE command byte for byte, then the LIVE-NOTE command); `2026-10-02/25-deploy-scripts-card.md:79`, `2026-10-03/01-lock-relief-card.md:25` and `:57`, `2026-10-06/04-next-flow-card.md:92`: dated cards, not edited. Older dated cards under `2026-09-*` hold the line too (history). `DEPLOY-HUB.md` and `CARD.md` hold no hit for `tests/cobalt tests/taxonomy`; `DEPLOY-HUB.md:102` reads `(a) OFFLINE → offline <p>/0` with no command; `BUILD-HUB.md:82` the same.
- The byte-equal pin today: `tests/ops/test_gate.py` `hub_commands()` (`:124-157`) reads `- (a) OFFLINE` from `BUILD-HUB.md`, but `BUILD-HUB.md:82` holds no `uv run pytest` span, so the key `offline` is never put, and `test_the_hub_holds_no_gate_command_and_points_at_the_lists_file` (`:256-276`) asserts `sorted(hub) == ["fp"]`. The OFFLINE command and the E0 line are therefore pinned equal by nothing today; test (2) of row T1 adds that pin. The `gate-lists.md` header (`:6-8`) says the hub lines and the lists stay byte-equal (`tests/ops/test_gate.py`).
- No with-DB test in `tests/ops`: the `--db-only` option is registered in `tests/cobalt/conftest.py:91-100` and `db_only_split` keeps a test with a `skipif` mark (`:81-88`); `grep -rn -E "skipif|pytest.skip|importorskip" tests/ops` → one hit, `tests/ops/test_fetch_voice_models.py:133` `pytest.skip("speech-to-text model absent from the dev model_dir")` (a model file, no database). PASS 1 is not edited. Note: the G1 guard (`require_offline_skip`, `:75-78`) is that conftest's and does not cover `tests/ops`; a future with-DB test in `tests/ops` would not be refused by it (not this card's; ASK DESK 1).
- Offline count change, `uv run pytest -q tests/ops --collect-only` on `BASE` `91ecb686`: `3544 tests collected in 1.50s`. The offline leg therefore adds those 3544 tests, plus the two new `test_t1_*` of this card, to whatever `tests/cobalt tests/taxonomy` collect today (not counted here). The `tests/ops` full run on `BASE` is in the drafter report, `## RECORDS`.
- RESTARTS class homes, `src/cobalt/jobs/restarts.py` at HEAD: `ops/desk/gate-lists.md` → `OPS_DESK_PREFIX = "ops/desk/"` (`:38`) and the branch at `:230-232` → "operator script; no Cobalt reader"; `docs/40 - DevDocs/prompts/BUILD-HUB.md` → `docs/` → `DOCS` (`:225-228`, the append at `:228`); `tests/ops/test_gate.py` → `tests/` → "test/documentation; no resident" (`:246`). `RESTARTS: none`; the build's run is quoted (row T1, last step).
- INSTALL: none. No script is added; `ops/desk/gate.sh` is read from the merged tree by the deploy (`DEPLOY-HUB.md` G: "every command from the merged tree's `ops/desk/gate-lists.md`").
- No DevDocs page names the gate lists (`DEPLOY-HUB.md:98` and `BUILD-HUB.md` are the homes), so no dated page line is owed (BUILD-HUB E3), as card 446 recorded.
- `RULINGS: none`: the drafter found no R-row for L79 in the files read; the desk fills a ruling row if one exists (ASK DESK 2 of the drafter report). Ops script, hub line and ops test only: house A is Grok, `HOUSE B: as needed`, never OpenAI (R920). `BASE` is the desk's: `main` at the launch; `TIP` starts empty and is written after the build, before the check.
