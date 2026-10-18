JOB: gemini-probe-id
LADDER: OFF-LADDER — reports/cto-2026-10-17.md R1736
CLASS: K5
INSTALL: none
BRANCH: ops/gemini-probe-id-1017
WORKTREE: gemini-probe-id-1017
BASE: f2140694
TIP: 744128d7
REPORT: /Users/cobalt/cobalt-wt/gemini-probe-id-1017/docs/40 - DevDocs/reports/gemini-probe-id-build-2026-10-17.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-probe-id-check-2026-10-17.md
HOUSE B: none
BAND: MID
DB: none
RESTARTS: none
RULINGS: 2026-10-17 R1736, 2026-10-17 R1738

## ROWS

The Gemini house-B id `gemini-3.1-pro-high` is rejected by the CLI (`reports/check-scratch-fr-check-2026-10-16.md:75`: `model gemini-3.1-pro-high is not recognized as a known model or custom model in settings`); his R1736 names `gemini-4-argon-high`. Class K5: an operator script, a fixed-file line, their test; no allow string changes (`Bash(agy *)` stands), no production command, no secret. Every `file:line` below was proved on `main` at the drafting (`## RECORDS`); re-read each by content before the edit (BUILD-HUB E3). The test rule (brain R1472): the pin finds its lines by content, holds no hash and no whole fixed-file line.

| row | what | red first | files |
|---|---|---|---|
| P0 | RUN — asserts nothing. THE ID PROOF, before any edit. (a) The CLI's own model list: `agy models` is not on the build line → `ASK DESK: agy models` under `## DECISIONS`, default taken: quote WHOLE the desk's `agy models` record of `## RECORDS` below (the line naming `gemini-4-argon-high`, with its time). That record does not name `gemini-4-argon-high` → the last line is `FAILED: id not listed — <the record's line>` (the arm is N/A, a record for the desk). (b) The probe with the old id, on the build line: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh gemini` → quote WHOLE (expected `gemini: OUT — error: invalid model selection …gemini-3.1-pro-high…`; any other answer is recorded, not a stop) | — (tool output quoted in the report) | none (read only) |
| G1 | The Gemini id in the probe and the hub becomes `gemini-4-argon-high`, nothing else on those lines. `ops/desk/house-probe.sh:24` (the header's spelling, `#           agy --model gemini-3.1-pro-high --mode accept-edits …`) and `:104` (`exec agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 3m …`); `docs/40 - DevDocs/prompts/CHECK-HUB.md:95` (the `- **GEMINI:**` line, `agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m …`); `docs/40 - DevDocs/prompts/STANDING-LIST.md:13` (THE HOUSE SPELLINGS, `agy --model gemini-3.1-pro-high …`). Each edit replaces the one token `gemini-3.1-pro-high` with `gemini-4-argon-high`; every other byte of the four files stands (CHECK-HUB stays 127 lines: `tests/ops/test_house_probe.py:193`). The existing pin `test_gemini_is_spelled_as_the_hub_launch_with_a_three_minute_print_timeout` (`tests/ops/test_house_probe.py:246-256`, its argv `"--model", "gemini-3.1-pro-high"` at `:253`) is the ONE existing test line edited: the id token only, no other assertion | In `tests/ops/test_house_probe.py` (appended): `test_k5_gemini_id_is_gemini_4_argon_high` — reads `PROBE` and `CHECK_HUB` (the module's constants, `:21-22`); the `PROBE` lines holding `agy --model` are exactly 2 and each holds `agy --model gemini-4-argon-high `; the `CHECK_HUB` lines starting `- **GEMINI:**` are exactly 1 and it holds `agy --model gemini-4-argon-high `; no line of either file holds `gemini-3.1-pro-high`. RED on `BASE`, quoted whole: `uv run pytest -q -p no:cacheprovider tests/ops/test_house_probe.py::test_k5_gemini_id_is_gemini_4_argon_high` → `1 failed`, on the first `gemini-4-argon-high` assertion. Then the edits, then the `:253` token, then `uv run pytest -q -p no:cacheprovider tests/ops/test_house_probe.py` → `0 failed`. MUTATION (PRE-STOP SELF-CHECK 1): `:104`'s id put back to `gemini-3.1-pro-high` by Edit → this test AND `test_gemini_is_spelled_…` red, quoted, undone | `ops/desk/house-probe.sh`, `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `tests/ops/test_house_probe.py` |
| P1 | RUN — asserts nothing. THE PROBE after the edit, through the worktree's script: `sh /Users/cobalt/cobalt-wt/gemini-probe-id-1017/ops/desk/house-probe.sh gemini` is not on the build line (the line's `sh` string is the repo path, which runs `main`'s old id) → `ASK DESK: the worktree probe` under `## DECISIONS`, default taken: not run here; the desk runs it before the check and records its line, and the deploy's smoke read (`## DEPLOY PROOF`) runs it on `main`. Then quote WHOLE: `grep -rn -F "gemini-3.1-pro-high" ops "docs/40 - DevDocs/prompts/CHECK-HUB.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md" tests/ops/test_house_probe.py` → nothing; `uv run pytest -q tests/ops` → `0 failed`; `uv run cobalt jobs restarts <BASE>..HEAD` and its `RESTARTS:` line | — (tool output quoted in the report) | none |

ORDER: P0; the new test on `BASE`, RED quoted; G1's four edits and the `:253` token; the file GREEN; P1.

## NOT IN THIS JOB
- `docs/40 - DevDocs/prompts/SHADOW-HUB.md` (`:88`, the Gemini `## BUILDERS` row) and `ops/desk/desk-launch.sh` (`:398`, the Gemini-id refusal) with its test `tests/ops/test_desk_launch_shadow.py:216-217`: card 671 owns them.
- Every dated prompt under `prompts/2026-*` and every report: history, never edited.
- `gemini-4-argon-medium` and `gemini-4-argon-low`: recorded, not used (R1736).
- Any other flag of the Gemini spelling (`--mode`, `--sandbox`, `--print-timeout`, `--add-dir`, the prompt text), the Grok and Sol spellings, the seat order, any allow string.
- `CHECK-HUB.md` lines 64 and 117 (card 583's, on `ops/band-routing-1015`); any `CHECK-HUB.md` line but `:95`.
- A real `agy`, `grok` or `codex` call in a test: `tests/ops/test_house_probe.py` stubs them.
- A red outside this fix: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here.

## READ
- `reports/check-scratch-fr-check-2026-10-16.md` lines 75 and 221 (the rejection).
- `reports/gemini-bakeoff-answer-2026-10-17.md` `## THE ARM` item 1.
- `ops/desk/house-probe.sh` lines 1-30 (the header) and 95-110 (`start()`).
- `tests/ops/test_house_probe.py` lines 1-60 (stubs, constants), 182-193 (the hub line count), 246-264 (the Gemini spelling tests).
- `docs/40 - DevDocs/prompts/CHECK-HUB.md` line 95; `docs/40 - DevDocs/prompts/STANDING-LIST.md` line 13.

## CHECK ASKS
- X1 Is `gemini-3.1-pro-high` replaced by `gemini-4-argon-high` at exactly `house-probe.sh` `:24`, `:104`, `CHECK-HUB.md:95`, `STANDING-LIST.md:13`, and is every other byte of those files unchanged (`git diff <BASE>..<TIP>`)?
- X2 Is the new pin red on `BASE` and on the mutation of `:104`, and is `:253` the only existing test line changed?
- X3 Does the desk's `agy models` record name `gemini-4-argon-high`, and does the worktree probe answer `gemini: UP`? A record missing is a finding, not a fix.

## DEPLOY PROOF
- `grep -c -F "agy --model gemini-4-argon-high" /Users/cobalt/cobalt/ops/desk/house-probe.sh` · before `0` · after `2`
- `grep -c -F "agy --model gemini-4-argon-high" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `0` · after `1`
- gemini probe · `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh gemini` · green: `gemini: UP`
- probe tests · `uv run pytest -q tests/ops/test_house_probe.py` · green: `0 failed`

## RECORDS
- THE CLI LIST (the desk, before launch): `agy models` → `gemini-4-argon-high	Gemini 4 Argon (High)` (listed with `gemini-4-argon-medium` and `gemini-4-argon-low`), Sat Oct 17 08:03:45 EDT 2026
- Drafter `draft-gemini-probe-id` (prompt 668), 2026-10-17 08:02 EDT. `git -C /Users/cobalt/cobalt status --short` on the four files and on `SHADOW-HUB.md`, `desk-launch.sh`, `test_desk_launch_shadow.py` printed nothing: the tree equals `main` for them. Occurrences of `gemini-3.1-pro-high` (`grep -rn` on `ops/`, `tests/`, `prompts/*.md`): `ops/desk/house-probe.sh:24`, `:104` (this card); `prompts/CHECK-HUB.md:95` (this card); `prompts/STANDING-LIST.md:13` (this card); `tests/ops/test_house_probe.py:253` (this card); `prompts/SHADOW-HUB.md:88` (card 671); `tests/ops/test_desk_launch_shadow.py:216-217` (card 671, the test of `desk-launch.sh:398`). No other top-level prompt holds it.
- Overlap: `git -C /Users/cobalt/cobalt diff main...ops/band-routing-1015 --stat` lists `docs/40 - DevDocs/prompts/CHECK-HUB.md | 4 +-` (card 583): its hunks are lines 64 and 117, one line replaced each; this card's is line 95. Text-disjoint; the line count stays 127 on both. Card 641 is deployed.
- RESTARTS (K10): `ops/desk/` → "operator script; no Cobalt reader" (`src/cobalt/jobs/restarts.py:38`, `:232`); `tests/` → `:245`; `docs/` → `:225`. Derived from the code; the builder's `cobalt jobs restarts` line is the record.
