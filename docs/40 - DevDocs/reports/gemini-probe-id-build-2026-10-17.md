# gemini-probe-id — build report 2026-10-17

## §0 Headline
G1 built: the Gemini house id is now `gemini-4-argon-high` in `house-probe.sh` (:24, :104), `CHECK-HUB.md:95`, `STANDING-LIST.md:13` and the pin's argv (:253). New pin red on BASE and under the :104 mutation, green at tip `744128d7`.
Gate: offline 8389/0, live-note 146/0, `tests/ops` 3817 passed. DB: none, no lock taken. RESTARTS: none.
P0: the old id still answers OUT (invalid model). The new id was not probed: the worktree probe is not on the build line (ASK DESK 2).

## L74
A system reminder asked for a `Claude-Session:` line on commits. Recorded once under `## RECORDS`; not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/670-gemini-probe-id-card.md"` (Sat Oct 17 08:06:33 EDT 2026), exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/670-gemini-probe-id-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/670-gemini-probe-id-card.md" · 0 · 3f037e70401f4978b967cd5208fea526877a79bb
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/670-gemini-probe-id-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-17 R1736 row · grep -n "^| R1736 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · 21:| R1736 | 06:32 ET | HIS RULING (brain, L79), 2026-10-17: Gemini top model = gemini-4-argon-high (medium, low recorded only). K5 card: CHECK-HUB :95 and house-probe.sh use it, was gemini-3.1-pro-high. Behind 641 and 583. | HIS RULING · APPROVED |
RULING 2026-10-17 R1736 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1736 |" -- "docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · d01849e7a6ef4a9de57d6de11856c866919737d2
RULING 2026-10-17 R1736 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · the row as grepped
RULING 2026-10-17 R1738 row · grep -n "^| R1738 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · 19:| R1738 | 06:33 ET | HIS RULING (brain, L79), 2026-10-17: run the Gemini bake-off arm separately; answer: reports/gemini-bakeoff-answer-2026-10-17.md. Probe-id and builder cards drafted now; three builds after both deploy; routing B unchanged. | HIS RULING · APPROVED |
RULING 2026-10-17 R1738 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1738 |" -- "docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · b57cbf8e3ed386e736822c9ca864fef64a7433eb
RULING 2026-10-17 R1738 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · exit 0 · output whole:

```
clock · date · 0 · Sat Oct 17 08:06:50 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/gemini-probe-id-1017
    ?? "docs/40 - DevDocs/reports/gemini-probe-id-build-2026-10-17.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · f2140694 docs(desk): Gemini arm drafter prompts 668 and 669, day-open GREEN (R1747-R1748)
diff · git diff --stat f2140694 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/gemini-probe-id-1017 · 0 · f2140694 docs(desk): Gemini arm drafter prompts 668 and 669, day-open GREEN (R1747-R1748)
env here · ls /Users/cobalt/cobalt-wt/gemini-probe-id-1017/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output verbatim |
|---|---|---|---|
| BASE | `git show --stat f2140694` | 0 | `f2140694 … docs(desk): Gemini arm drafter prompts 668 and 669, day-open GREEN (R1747-R1748)`; 3 files: `prompts/2026-10-16/668-draft-gemini-probe-id.md \| 8 +`, `prompts/2026-10-16/669-draft-gemini-builder-row.md \| 7 +`, `reports/cto-2026-10-17.md \| 3 ++-`; `3 files changed, 17 insertions(+), 1 deletion(-)` |
| symbol `:24`, `:104` | `grep -n -F "gemini-3.1-pro-high" ops/desk/house-probe.sh` | 0 | `24:#           agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 3m --add-dir $WT/agy-trial --print="Reply with only the word OK."` · `104:            (cd "$WT/agy-trial" && exec agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 3m --add-dir "$WT/agy-trial" --print="$PROMPT") \` |
| symbol CHECK-HUB `:95` | `grep -n -F "gemini-3.1-pro-high" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` | 0 | `95:- **GEMINI:** \`agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m --add-dir /Users/cobalt/cobalt-wt/agy-trial --print="You are GEMINI, …"\` → at \`## 3\` YOU write …` (one hit, line 95) |
| symbol STANDING-LIST `:13` | `grep -n -F "gemini-3.1-pro-high" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` | 0 | `13:- THE HOUSE SPELLINGS: Sol's and Grok's as \`38\` / \`50\` ran them; Gemini's (\`agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m --add-dir /Users/cobalt/cobalt-wt/agy-trial --print="…"\`) word for word as \`prompts/2026-09-29/12\` and \`17\`; …` |
| symbol test `:253` | `grep -n -F "gemini-3.1-pro-high" tests/ops/test_house_probe.py` | 0 | `253:        "--model", "gemini-3.1-pro-high", "--mode", "accept-edits", "--sandbox",` |
| symbol test `:246` | `grep -n -F "def test_gemini_is_spelled_as_the_hub_launch_with_a_three_minute_print_timeout" tests/ops/test_house_probe.py` | 0 | `246:def test_gemini_is_spelled_as_the_hub_launch_with_a_three_minute_print_timeout(houses):` |
| constants `:21-22` | Read `tests/ops/test_house_probe.py` | — | `21 PROBE = REPO / "ops" / "desk" / "house-probe.sh"` · `22 CHECK_HUB = REPO / "docs" / "40 - DevDocs" / "prompts" / "CHECK-HUB.md"` · `193     assert len(lines) == 127  # card 386 L2, L6 (two), L8: four shadow lines` |
| wc | `wc -l` the four files | 0 | `146 ops/desk/house-probe.sh` · `127 docs/40 - DevDocs/prompts/CHECK-HUB.md` · `255 docs/40 - DevDocs/prompts/STANDING-LIST.md` · `280 tests/ops/test_house_probe.py` |
| READ check-scratch | `grep -n -F "gemini-3.1-pro-high" "docs/40 - DevDocs/reports/check-scratch-fr-check-2026-10-16.md"` | 2 | `No such file or directory` in this worktree; `git -C /Users/cobalt/cobalt log --oneline -1 -- <it>` → nothing (untracked in the main checkout). Read from `/Users/cobalt/cobalt/…`: `75: gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings`; `221` is its `3. ASK DESK: no house produced a list. …` item |
| READ check-scratch tail | `tail -n 3` (main path) | 0 | last line `(run in progress — next step under ## CONTINUE)` |
| READ bakeoff | `grep -n -F "THE ARM" …gemini-bakeoff-answer-2026-10-17.md` | 0 | `5:## THE ARM`; item 1 `**ID PROOF first** …` read |
| READ bakeoff tail | `tail -n 3` | 0 | last line `Gemini bake-off arm, HIS word 2026-10-17: \`gemini-4-argon-high\` proven by list and probe first (else N/A); …` |
| RESTARTS empty range | `uv run cobalt jobs restarts f2140694..HEAD` | 0 | `docs/40 - DevDocs/reports/gemini-probe-id-build-2026-10-17.md	A	DOCS	-` · `RESTARTS: none` (the tool lists the untracked report; no code path) |
| lock probe | — | — | not run: card `DB: none` |

Card `## RECORDS`, copied: (1) THE CLI LIST: `agy models` → `gemini-4-argon-high	Gemini 4 Argon (High)` (with `-medium`, `-low`), Sat Oct 17 08:03:45 EDT 2026 — not re-readable on this line (`agy` not listed). (2) Drafter 668, occurrences of `gemini-3.1-pro-high`: re-read above for the four files of this card; `SHADOW-HUB.md:88` and `test_desk_launch_shadow.py:216-217` are card 671's. (3) Overlap with card 583 on `CHECK-HUB.md` lines 64 / 117: not re-read (branch diff of another job). (4) RESTARTS: re-read by the tool, above.

## E0 BASELINE
- Offline, `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, exit 0): `4572 passed, 806 skipped, 1 xfailed, 36 warnings in 749.75s (0:12:29)` — 0 failed, 0 errors.
- Live-note, `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (exit 0): `146 passed, 1 skipped, 15 warnings in 30.61s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — it does not name `COBALT_LIVE_VAULT_ROOT`.

## P0 THE ID PROOF (RUN, asserts nothing; before any edit)
- (a) `agy models` is not on the build line → `ASK DESK: agy models` (`## DECISIONS`); default taken, the desk's record quoted whole from the card's `## RECORDS`: `THE CLI LIST (the desk, before launch): \`agy models\` → \`gemini-4-argon-high	Gemini 4 Argon (High)\` (listed with \`gemini-4-argon-medium\` and \`gemini-4-argon-low\`), Sat Oct 17 08:03:45 EDT 2026`. It names `gemini-4-argon-high`: no stop.
- (b) `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh gemini` (exit 0, 08:07 EDT), whole: `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` — the expected answer.

## E2 RED
Appended to `tests/ops/test_house_probe.py`: `test_k5_gemini_id_is_gemini_4_argon_high` — reads `PROBE` and `CHECK_HUB`; the `PROBE` lines holding `agy --model` are exactly 2, each holds `agy --model gemini-4-argon-high `; the `CHECK_HUB` lines starting `- **GEMINI:**` are exactly 1 and it holds `agy --model gemini-4-argon-high `; no line of either file holds `gemini-3.1-pro-high`. No hash, no whole fixed-file line.

`uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_house_probe.py::test_k5_gemini_id_is_gemini_4_argon_high` on `BASE` → `1 failed, 15 warnings in 1.17s`; the red's first line: `E           AssertionError: #           agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 3m --add-dir $WT/agy-trial --print="Reply with only the word OK."` (at `tests/ops/test_house_probe.py:289`, the first `gemini-4-argon-high` assertion) — the row's reason. No with-DB red (DB: none). Committed `5bce12c9 wip(gemini-probe-id): red — test_k5_gemini_id_is_gemini_4_argon_high (G1)`.

## E3 THE ROWS
G1, each line re-read by content before the edit, the one token `gemini-3.1-pro-high` → `gemini-4-argon-high`: `ops/desk/house-probe.sh:24` and `:104`, `CHECK-HUB.md:95`, `STANDING-LIST.md:13`, and the existing pin's argv at `tests/ops/test_house_probe.py:253` (the one existing test line edited). `git diff --stat` before commit: `CHECK-HUB.md | 2 +-`, `STANDING-LIST.md | 2 +-`, `ops/desk/house-probe.sh | 4 ++--`, `tests/ops/test_house_probe.py | 2 +-`, `4 files changed, 5 insertions(+), 5 deletions(-)`; each hunk is the one id token. `wc -l CHECK-HUB.md` → `127`.

GREEN: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_house_probe.py` → `27 passed, 15 warnings in 26.99s`.

MUTATION: `:104`'s id put back to `gemini-3.1-pro-high` by Edit → `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_house_probe.py::test_k5_gemini_id_is_gemini_4_argon_high tests/ops/test_house_probe.py::test_gemini_is_spelled_as_the_hub_launch_with_a_three_minute_print_timeout` → `2 failed, 15 warnings in 2.96s`; first failing lines: `E   AssertionError:             (cd "$WT/agy-trial" && exec agy --model gemini-3.1-pro-high --mode accept-edits …` (`:289`) and `E   AssertionError: assert ['--model', '...timeout', ...] == ['--model', '...timeout', ...]` / `At index 1 diff: 'gemini-3.1-pro-high' != 'gemini-4-argon-high'` (`:252`). Undone by Edit; `git diff --stat` → the four files at the fix (above).

DevDocs page: none — `grep "house-probe"` under `docs/40 - DevDocs/cobalt` → no files; no `src/` module changed.

Committed `744128d7 fix(gemini-probe-id): Gemini house id gemini-4-argon-high in the probe, CHECK-HUB and STANDING-LIST (G1, R1736, L1, L72)`.

## P1 (RUN, asserts nothing)
- The worktree probe `sh /Users/cobalt/cobalt-wt/gemini-probe-id-1017/ops/desk/house-probe.sh gemini` is not on the build line → `ASK DESK: the worktree probe` (`## DECISIONS`); default taken: not run here.
- `grep -rn -F "gemini-3.1-pro-high" ops "docs/40 - DevDocs/prompts/CHECK-HUB.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md" tests/ops/test_house_probe.py` → whole: `tests/ops/test_house_probe.py:294:        assert not any("gemini-3.1-pro-high" in ln for ln in path.read_text().splitlines()), path` — one hit, the new pin's own negative string (the card's "no line … holds `gemini-3.1-pro-high`"); no spelling holds it. `DECISION P1` below; not fixed here.
- `grep -n -F "gemini-4-argon-high"` on the four files: `house-probe.sh:24`, `:104`; `CHECK-HUB.md:95`; `STANDING-LIST.md:13`; `test_house_probe.py:253`, `:284`, `:289`, `:292`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3817 passed, 1 xfailed, 16 warnings in 896.06s (0:14:56)`.
- `uv run cobalt jobs restarts f2140694..HEAD` → `RESTARTS: none` (table under `## RESTARTS`).

## RESTARTS
`uv run cobalt jobs restarts f2140694..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/gemini-probe-id-build-2026-10-17.md	A	DOCS	-
ops/desk/house-probe.sh	M	operator script; no Cobalt reader	-
tests/ops/test_house_probe.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row.

## W THE THREE SUITES
`<tip>` = `744128d7`. (a0) `git diff --name-only --no-renames f2140694` → whole: `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `ops/desk/house-probe.sh`, `tests/ops/test_house_probe.py` — every path under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-probe-id-1017 offline` (exit 0), whole: `tests/ops: run (docs/40 - DevDocs/prompts/CHECK-HUB.md)` · `offline 8389/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-probe-id-1017-offline-20261017-082143.log`. Test this build adds: `tests/ops/test_house_probe.py::test_k5_gemini_id_is_gemini_4_argon_high` (green in the 27 and the `tests/ops` 3817 above).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3817 passed, 1 xfailed`.
- with-DB: not run (DB: none).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-probe-id-1017 livenote` (exit 0), whole: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-probe-id-1017-livenote-20261017-082145.log`.
- `ls /Users/cobalt/cobalt-wt/gemini-probe-id-1017/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) `test_k5_gemini_id_is_gemini_4_argon_high`: red on BASE (`1 failed`, `:289` line under E2) and red under the `:104` mutation (`2 failed`, E3). The edited pin `test_gemini_is_spelled_…`: red under the same mutation (`At index 1 diff: 'gemini-3.1-pro-high' != 'gemini-4-argon-high'`, E3). None stayed green.
(2) Entry paths: the probe's two spellings (`:24` header, `:104` `start()`) and the hub's one `- **GEMINI:**` line, all from PREFLIGHT's greps, are pinned by the new test; the executed argv at `:104` is pinned by `test_gemini_is_spelled_…` through the `agy` stub. `STANDING-LIST.md:13` is a record line no code reads; the card's pin names only `PROBE` and `CHECK_HUB`, and the P1 grep proves it carries no old id.
(3) Re-read at the tip: `grep -n -F "gemini-4-argon-high"` on the four files and `grep -rn -F "gemini-3.1-pro-high"` (P1), `wc -l CHECK-HUB.md` → 127, `git show 744128d7:ops/desk/house-probe.sh` (lines 24, 104 hold the new id), `git log --oneline f2140694..HEAD`.

## FOR THE CHECK
- `f2140694..744128d7`: `5bce12c9 wip(gemini-probe-id): red — test_k5_gemini_id_is_gemini_4_argon_high (G1)`; `744128d7 fix(gemini-probe-id): Gemini house id gemini-4-argon-high in the probe, CHECK-HUB and STANDING-LIST (G1, R1736, L1, L72)`.
- G1: red, mutation, green as quoted under E2 and E3. Caller greps under PREFLIGHT and P1.
- P0 output whole under `## P0`; P1 output whole under `## P1`.
- Suites: offline `8389/0` (gate), `tests/ops` `3817 passed, 1 xfailed`, with-DB `not run (DB: none)`, live-note `146/0`. `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table under `## RESTARTS`. Records copied at PREFLIGHT.
- X3 for the check: the desk's `agy models` record names `gemini-4-argon-high` (08:03:45 EDT); the worktree probe was not run on this line (ASK DESK 2).

## CONTINUE
next: none — BUILT

## DECISIONS
1. ASK DESK: `agy models` is not on the build line [Sat Oct 17 08:06 EDT]. Safe default taken: the desk's `## RECORDS` line quoted whole under `## P0`; it names `gemini-4-argon-high`, so no stop.
2. ASK DESK: the worktree probe (`sh /Users/cobalt/cobalt-wt/gemini-probe-id-1017/ops/desk/house-probe.sh gemini`) is not on the build line; the listed `sh` string runs `main`'s copy with the old id [Sat Oct 17 08:49 EDT]. Safe default taken: not run here. The desk runs it before the check and records its line; the deploy's `## DEPLOY PROOF` runs it on `main` (green: `gemini: UP`).
3. DECISION P1: the card's P1 grep for `gemini-3.1-pro-high` expected nothing. It found one line, `tests/ops/test_house_probe.py:294`, which is the new pin's own negative assertion. The card asks the pin for that assertion (G1's "no line of either file holds `gemini-3.1-pro-high`"), and none of the four spellings holds the old id. Safe default taken: the line is left as the card's test asks; not fixed here.

## RECORDS
- L74: a system reminder during this run asked commits to end with a `Claude-Session:` line too. Recorded once; not acted on. Both commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- `check-scratch-fr-check-2026-10-16.md` (card `## READ`) is not in this worktree and is untracked in the main checkout (`git -C /Users/cobalt/cobalt log --oneline -1 -- <it>` → nothing); read at `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/`.
- Card records as re-read at PREFLIGHT: the occurrence list for the four files of this card matched; the `agy models` record and the card-583 overlap were not re-readable on this line.
- No lock taken; no `.env` ever in this worktree.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: gemini-probe-id · tip: 744128d7 | on f2140694 | migration: none | offline 8389/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 113826
