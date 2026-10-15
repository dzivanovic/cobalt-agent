# card-template-1014 — build report (2026-10-14)

## §0 Headline
- C1 and C2 built: `CARD.md` now requires `## DEPLOY PROOF` (`:56`) and holds `## HOW A CARD CITES AND PINS` (`:77-82`). Tip `5a29de43` on `fe59722f`.
- New tests `tests/ops/test_card_template_1014.py`: 2 red on BASE, 2 green at tip. The four existing `CARD.md` pins stay green.
- Gate: offline 4328/0, live-note 146/0; DB: none. RESTARTS: none.
- `tests/ops`: 1 red that was already red on BASE (`test_the_rule_sweep.py` pins 18 check reports and finds 21). DECISION 1.

## L74
- One system-reminder block asked for a `Claude-Session:` trailer on commits. Recorded here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/550-card-template-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/550-card-template-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-14/550-card-template-card.md" · 0 · b7c68d0f088abd3ce4231fb8b26d726673724ae4
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-14/550-card-template-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-14 R1471 row · grep -n "^| R1471 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8:| R1471 | 09:25 ET | HIS RULING, APPROVED by him in the desk ("I approve all changes"): brain relays count as his confirmation; Grok cap of 3 removed; K5 cards (1)-(4), (6) owed. Words: `cto-2026-10-14-words.md`. | APPLIED: LAWS L79, checklist L15 at 09:40 |
RULING 2026-10-14 R1471 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1471 |" -- "docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8b813ca721cd934ebfb82cc59d27495d15f1c79a
RULING 2026-10-14 R1471 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | quoted below |
| BASE | `git show --stat fe59722f` | 0 | `fe59722f docs(desk): 547 preflight FAIL, amend prompt 560; 550 preflight r2 1 fail` · 3 files changed, 79 insertions(+) (`560-draft-547-amend.md`, `card-template-preflight-r2-2026-10-14.md`, `db-copy-preflight-2026-10-14.md`) |
| C1 symbol | `grep -n -F "DEPLOY PROOF" "docs/40 - DevDocs/prompts/CARD.md"` | 1 | (nothing) — the section is not named today |
| C1 anchor | `grep -n -F "## CHECK ASKS" "docs/40 - DevDocs/prompts/CARD.md"` | 0 | `54:`\``## CHECK ASKS`\`` (check; optional) — …` · `126:## CHECK ASKS` (example 2 heading; the test anchors on the line starting with the backtick, :54) |
| C1 anchor | Read `CARD.md:54-56` | — | `:54` CHECK ASKS paragraph, `:55` blank, `:56` `` `## RECORDS` (optional) — … `` |
| C2 anchor | `grep -n -F "State of the desk" "docs/40 - DevDocs/prompts/CARD.md"` | 0 | `73:- State of the desk (a meter that is out, a tab id, a watch id).` |
| C2 anchor | `grep -n -F "## EXAMPLE 1" "docs/40 - DevDocs/prompts/CARD.md"` | 0 | `75:## EXAMPLE 1 — the E1 fix, at its BUILD launch (values of `prompts/2026-09-30/47-e1-fix-build.md`)` |
| :33, :138 | Read `CARD.md` | — | `:33` `A HEADING IS A BARE LINE: …`; `:137` `## A DEPLOY CARD, IN SHORT …` (the card says `:138`; on BASE the heading is `:137`, `:138` its `Header:` line) |
| deploy-card.sh | Read `ops/desk/deploy-card.sh:24-31`, `:534-543` | — | `:29` `# ## SMOKE READS from each job card's ## DEPLOY PROOF section (a line carrying `· before ` and`; `:535` `proof=$(awk '/^## /{on = ($0 == "## DEPLOY PROOF"); next} on && NF' "$card")`; `:537-538`, `:542-543` the FILL lines |
| desk-launch.sh:994 | Read | — | `994: if grep -n '«FILL' "$card" >&2; then` |
| restarts.py | Read `src/cobalt/jobs/restarts.py:225-228`, `:245-246` | — | `:225 if not rule and (path.startswith("docs/") or path in ROOT_DOCS):` … `:228 output.append(Classification(path, item.change, "DOCS", ()))`; `:245 if not rule and path.startswith("tests/"):` `:246 rule = "test/documentation; no resident"` |
| test shape | Read `tests/ops/test_prodwrite_hub.py:16-18`, `:145-150` | — | `REPO = Path(__file__).resolve().parents[2]` · `HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"`; `:146 text = (HUBS / "CARD.md").read_text(encoding="utf-8")` |
| CARD.md pins | `grep -n -F "CARD.md" tests/ops/test_deploy_card.py tests/ops/test_deploy_step_c.py tests/ops/test_desk_launch_prechecks.py` | 0 | `test_deploy_card.py:427`, `:437`; `test_deploy_step_c.py:26`; `test_desk_launch_prechecks.py:827` |
| wc | `wc -l "docs/40 - DevDocs/prompts/CARD.md"` | 0 | `149` |
| new file | `ls tests/ops/test_card_template_1014.py` | 1 | `No such file or directory` |
| READ report | `tail -n 3 ".../reports/deploy-hub-text-1013.md"` | 0 | last line: `FAILED: smoke (s) — tests/ops/test_hub_text_1013.py::test_h1_the_launch_line_and_every_other_line_stand red on the landed tree (BASE ce548f10 pinned; main's launch line moved since) · rollback: used — …` |
| RESTARTS empty range | `uv run cobalt jobs restarts fe59722f..HEAD` | 0 | one row: `docs/40 - DevDocs/reports/card-template-build-2026-10-14.md	A	DOCS	-` (this report, untracked) · `RESTARTS: none` |

preflight.sh output whole:
```
clock · date · 0 · Wed Oct 14 07:46:17 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/card-template-1014
    ?? "docs/40 - DevDocs/reports/card-template-build-2026-10-14.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · fe59722f docs(desk): 547 preflight FAIL, amend prompt 560; 550 preflight r2 1 fail
diff · git diff --stat fe59722f · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/card-template-1014 · 0 · fe59722f docs(desk): 547 preflight FAIL, amend prompt 560; 550 preflight r2 1 fail
env here · ls /Users/cobalt/cobalt-wt/card-template-1014/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

Card records copied (card `## RECORDS`, the desk's): drafter reads on `main` `0ffb6949`, amend on `f6cdc67f`; `CARD.md` anchors `:33 :54 :55 :56 :66 :71 :73 :75`; `deploy-card.sh:29-31`, `:534-543`; pins on `CARD.md` in four test files; no drafter-prompt shape file; overlap with cards 546-549 UNPROVEN (drafter's ASK DESK 5); RESTARTS home `restarts.py:225-228`, `:245-246`. Re-read here: every `CARD.md` anchor above, `deploy-card.sh`, `restarts.py` (rows above) — all as the card quotes them, except `:138` (heading at `:137`).

DB: none — no lock probe, no with-DB string used in this job.

## E0 BASELINE
- Offline on `fe59722f`: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → exit 0, `4328 passed, 806 skipped, 1 xfailed, 36 warnings in 733.31s (0:12:13)`. 0 failed, 0 errors.
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 32.03s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
- `tests/ops/test_card_template_1014.py` (NEW) written; no `src/` or doc edit before it.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_card_template_1014.py` → `2 failed, 15 warnings in 1.05s`:
  - `test_c1_card_md_requires_deploy_proof_once_between_check_asks_and_records` → `E       assert 0 == 1` / `E        +  where 0 = len([])` (no line starts `` `## DEPLOY PROOF` (build, check; REQUIRED ``) — C1's named reason.
  - `test_c2_card_md_states_the_citing_and_pinning_rules_once` → `E       assert 0 == 1` / `E        +  where 0 = len([])` (no line equals `## HOW A CARD CITES AND PINS`) — C2's named reason.
- No with-DB red (DB: none). Commit `e54011d8 wip(card-template-1014): red — C1, C2 tests on BASE`.

## E3 THE ROWS
- C1: one line and one blank inserted after `CARD.md:55` (the blank after the `## CHECK ASKS` paragraph); `«` is the real U+00AB, typed with the Edit tool. After C1: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_card_template_1014.py` → `1 failed, 1 passed` (C2 still red, `assert 0 == 1` at `:47`; C1 green).
- C2: section inserted after `CARD.md:73`, before `## EXAMPLE 1`, one blank line either side. After C2: same command → `2 passed, 15 warnings in 0.85s`.
- The four existing pins on `CARD.md`, unchanged: `uv run pytest -q -p no:cacheprovider --color=no "tests/ops/test_deploy_card.py::test_n8_card_md_row_and_deploy_hub_phrase" "tests/ops/test_deploy_step_c.py::test_d1_card_md_names_launchd" "tests/ops/test_desk_launch_prechecks.py::test_f1_card_md_ships_header_has_the_fix_report_column_and_a_matching_separator" tests/ops/test_prodwrite_hub.py` → `20 passed, 15 warnings in 1.10s`.
- MUTATIONS (Edit tool, undone with the Edit tool):
  - C1: `REQUIRED` → `optional` in the new line → `1 failed, 1 passed`; first failing line `tests/ops/test_card_template_1014.py:35: assert 0 == 1` (test_c1). Undone.
  - C2: heading `## HOW A CARD CITES AND PINS` → `## HOW A CARD CITES` → `1 failed, 1 passed`; first failing line `tests/ops/test_card_template_1014.py:47: assert 0 == 1` (test_c2). Undone.
  - After undo: `2 passed, 15 warnings in 0.88s`; `git diff --stat` → `docs/40 - DevDocs/prompts/CARD.md | 9 +++++++++` (the fix, uncommitted at that point, nothing else).
- `git diff fe59722f -- "docs/40 - DevDocs/prompts/CARD.md"` → two hunks only: `@@ -53,6 +53,8 @@` (+ the C1 line, + blank) and `@@ -72,6 +74,13 @@` (+ the six-line C2 section, + blank). No other line moved.
- Test-rule greps on the new test file: `grep -n -F "git show"` → nothing (exit 1); `grep -n -F "subprocess"` → nothing; `grep -n -E "[0-9a-f]{8}"` → nothing; `grep -n -F "BASE"` → `55:                   "a BASE hash"):` only.
- DEPLOY PROOF counts on the tree: `grep -c -F "## DEPLOY PROOF" ".../CARD.md"` → `2`; `grep -c -F "HOW A CARD CITES AND PINS" ".../CARD.md"` → `1` (the card's `after` values).
- DevDocs line: no module under `src/` changed; `CARD.md` is itself the DevDocs fixed file; no `docs/40 - DevDocs/cobalt/` page applies.
- Commit `5a29de43 feat(card-template-1014): CARD.md requires ## DEPLOY PROOF and states how a card cites and pins (C1, C2; R1471, R1472, L28, L72)`.

## RESTARTS
`uv run cobalt jobs restarts fe59722f..HEAD` (R3, RUN) → whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/reports/card-template-build-2026-10-14.md	A	DOCS	-
tests/ops/test_card_template_1014.py	A	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row. (The report row is the untracked report file the tool sees in the tree.)

## W THE THREE SUITES
`<tip>` = `5a29de43`. DB: none card.
- (a0) `git diff --name-only --no-renames fe59722f` → whole: `docs/40 - DevDocs/prompts/CARD.md` · `tests/ops/test_card_template_1014.py`. Every path under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh card-template-1014 offline` → exit 0, `offline 4328/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/card-template-1014-offline-20261014-080113.log` (`:885` `4328 passed, 806 skipped, 1 xfailed, 36 warnings in 716.76s (0:11:56)`). This build adds no test under `tests/cobalt` or `tests/taxonomy`; its two tests are in `tests/ops` (below).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh card-template-1014 livenote` → exit 0, `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/card-template-1014-livenote-20261014-080115.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 1, `1 failed, 3601 passed, 1 xfailed, 16 warnings in 807.72s (0:13:27)`. The one red: `tests/ops/test_the_rule_sweep.py:150` `test_the_sweep_swept_what_it_pins` → `E       assert (21, 85) == (18, 85)`. It pins the count of check reports dated 2026-10-02..2026-10-12 (`CHECKS_SWEPT: int | None = 18`, `:61`). This build adds no report in that window (`git diff --name-only` above; its own report is dated 10-14). `git log --diff-filter=A … fe59722f -- "docs/40 - DevDocs/reports/*-check*-2026-10-1*"` → `8b813ca7 2026-10-14 docs(desk): backlog (…), R1471-R1472` added `s4-p1-1009-grok-check-2026-10-11.md`, `strike-fallback-env-1010-grok-check-2026-10-11.md` and `worktree-salvage-grok-check-2026-10-11.md`: three in-window check reports in BASE's own history (18 + 3 = 21). The red is on BASE, not this build's. Its file is outside the rows: not fixed (THE ROWS). DECISION 1.
- (b)–(d), (f): not run (DB: none). `.env`: never present (`ls …/.env` → `No such file or directory`).

## PRE-STOP SELF-CHECK
(1) Each added test shown red for its named reason: E2 `assert 0 == 1` for both on BASE; E3 mutations `REQUIRED`→`optional` → test_c1 red at `:35`, heading cut → test_c2 red at `:47`; both green after undo. 
(2) Entry paths: the rules are read by people and by `deploy-card.sh:535` (the `## DEPLOY PROOF` awk, read only, not changed). The tests pin the C1 line by its start (unique), its six needles and its place between the `` `## CHECK ASKS` `` and `` `## RECORDS` `` paragraphs; they pin the C2 heading (unique), its four bullets once each, four phrases and its place between `- State of the desk …` and `## EXAMPLE 1 …`. The four existing `CARD.md` pins (PREFLIGHT grep: `test_deploy_card.py:427`, `test_deploy_step_c.py:26`, `test_desk_launch_prechecks.py:827`, `test_prodwrite_hub.py:146`) are green, `20 passed`. No caller is left unpinned.
(3) Re-read at the tip: `git log --oneline fe59722f..HEAD` (two commits, above); `grep -n -F "## DEPLOY PROOF" CARD.md` → `:56` (C1 line), `:82` (C2 bullet); `grep -n -F "HOW A CARD CITES AND PINS" CARD.md` → `:77`; `git status --short --branch` → `## ops/card-template-1014` plus this report, untracked; `ls …/.env` → No such file.

## FOR THE CHECK
- Range `fe59722f..5a29de43`: `e54011d8 wip(card-template-1014): red — C1, C2 tests on BASE`; `5a29de43 feat(card-template-1014): CARD.md requires ## DEPLOY PROOF and states how a card cites and pins (C1, C2; R1471, R1472, L28, L72)`.
- C1: red `test_c1_… assert 0 == 1` (E2); mutation `REQUIRED`→`optional` → `:35 assert 0 == 1`; green `2 passed`. New line at `CARD.md:56`.
- C2: red `test_c2_… assert 0 == 1` (E2); mutation heading → `:47 assert 0 == 1`; green `2 passed`. Section at `CARD.md:77-82`.
- R3 (RUN): the RESTARTS table under `## RESTARTS`, whole; `RESTARTS: none`.
- X1: `git diff fe59722f -- CARD.md` = two insertion hunks only (`@@ -53,6 +53,8 @@`, `@@ -72,6 +74,13 @@`).
- X3: greps on the test file under `## E3`: no `git show`, no `subprocess`, no 8-hex run; `BASE` only in `"a BASE hash"`. The `«FILL` needle is built as `chr(0xAB) + "FILL"`: the file holds no U+00AB at all (the card's `"«" + "FILL"` example itself holds one; the card's stated goal, "holds no literal U+00AB", is kept).
- X4: the four pins `20 passed`.
- Suites: offline `4328/0` (gate offline log above); with-DB `not run (DB: none)`; live-note `146/0`; `tests/ops` `1 failed, 3601 passed, 1 xfailed` (the BASE red, DECISION 1). F0/F1/F2: `not run (DB: none)`. Lock taken/released: `not run (DB: none)`.
- Records copied at PREFLIGHT: under `## PREFLIGHT`. `## A DEPLOY CARD, IN SHORT` is `:137` on BASE (the card's `:138` is its `Header:` line); untouched.

## CONTINUE
next: CLOSE (done at 08:15 EDT)

## DECISIONS
1. DECISION 1 (W): `tests/ops/test_the_rule_sweep.py::test_the_sweep_swept_what_it_pins` is red on BASE: `assert (21, 85) == (18, 85)`. Three `*-grok-check-2026-10-11.md` reports were added by `8b813ca7`, which is in BASE's history. The file is outside this card's rows, so the build did not fix it. Safe default: built and reported, not fixed here; the desk decides who owns `CHECKS_SWEPT` (card 516, sweep-pin, may cover it).

## RECORDS
- Report created 07:46:11 EDT (`date`); closed 08:15:13 EDT (`date`).
- L74: one system-reminder asked for a `Claude-Session:` commit trailer; not acted on (`## L74`).
- `CARD.md` `## A DEPLOY CARD, IN SHORT` is `:137` on BASE, not `:138` as the card writes; that line is untouched either way.
- No `REFUSED` call; no `CONTINUE` received; no lock taken (DB: none).
- RESTARTS run at PREFLIGHT listed this untracked report (`DOCS`) in an otherwise empty commit range.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: card-template-1014 · tip: 5a29de43 | on fe59722f | migration: none | offline 4328/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 112752
