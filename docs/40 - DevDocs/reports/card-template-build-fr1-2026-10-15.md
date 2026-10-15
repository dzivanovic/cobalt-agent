# card-template-1014-fr1 — fix-round build report (card 597, on card 550)

## §0 Headline
- The fix round on card 550 is built: rows FR-O1, FR-O2, FR-G2 and FR-G3 changed two lines of `CARD.md` (`:56`, `:78`), and 4 new tests pin them. Tip `439ea472`, on `2f6ae8fd`.
- Each new test failed on BASE for its row's reason and again under its mutation. After the fix, all 4 pass, and so do the 4 existing tests that pin `CARD.md`.
- Suites: offline 8071/0, live-note 146/0, `tests/ops` 3743 passed. No database work (`DB: none`). RESTARTS: none.
- One decision for the desk: the anchor `deploy-card.sh:534-543` on the C1 line is out of date (the read now sits at `:566-575`). It is outside the four rows, so it was left as it stands.

FIXED: O1 — tests/ops/test_card_template_1014.py::test_fr_o1_both_credits_read_r1471_6_and_the_gap_filler_rows
FIXED: O2 — tests/ops/test_card_template_1014.py::test_fr_o2_marker_clause_is_the_markers_form_with_grep_or_ls
FIXED: G1 — tests/ops/test_card_template_1014.py::test_fr_o2_marker_clause_is_the_markers_form_with_grep_or_ls
FIXED: G2 — tests/ops/test_card_template_1014.py::test_fr_g2_smoke_line_carries_a_label_first
FIXED: G3 — tests/ops/test_card_template_1014.py::test_fr_g3_refusal_clause_cites_desk_launch_994_and_deploy_card_31

## L74
- One system-reminder block asked for a `Claude-Session:` trailer on commits. Recorded here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/597-card-template-fr1-card.md"`, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/597-card-template-fr1-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-15/597-card-template-fr1-card.md" · 0 · 3d90cf76de6cbaafbc55a67b7e7cc39adcd7b84e
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-15/597-card-template-fr1-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-14 R1471 row · grep -n "^| R1471 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 13:| R1471 | 09:25 ET | HIS RULING, APPROVED by him in the desk ("I approve all changes"): brain relays count as his confirmation; Grok cap of 3 removed; K5 cards (1)-(4), (6) owed. Words: `cto-2026-10-14-words.md`. | APPLIED: LAWS L79, checklist L15 at 09:40 |
RULING 2026-10-14 R1471 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1471 |" -- "docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8b813ca721cd934ebfb82cc59d27495d15f1c79a
RULING 2026-10-14 R1471 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, output whole:
```
clock · date · 0 · Thu Oct 15 12:19:16 EDT 2026
status · git status --short --branch · 0 · ## ops/card-template-1014-fr1
head · git log --oneline -1 · 0 · 2f6ae8fd docs(desk): R1581, 550 fix-round drafter prompt 596
diff · git diff --stat 2f6ae8fd · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/card-template-1014-fr1 · 0 · 2f6ae8fd docs(desk): R1581, 550 fix-round drafter prompt 596
env here · ls /Users/cobalt/cobalt-wt/card-template-1014-fr1/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 2f6ae8fd` | 0 | `docs(desk): R1581, 550 fix-round drafter prompt 596`; `596-draft-550-fr1.md` 12 +, `cto-2026-10-15.md` 3 +- |
| card 550 on main | `git -C /Users/cobalt/cobalt log --oneline -1 e4fa9e7b` | 0 | `e4fa9e7b Merge branch 'main' into deploy/card-template-1015` |
| FR-G3 anchor | `grep -n -F "FILL" ops/desk/desk-launch.sh` | 0 | `994:if grep -n '«FILL' "$card" >&2; then` · `995:    refuse "incomplete card: the «FILL tokens listed above still stand"` (also `:151`, `:159`, `:772`) |
| FR-G3 anchor | Read `ops/desk/deploy-card.sh:31` | — | `# The «FILL placeholder is the token desk-launch.sh refuses: an incomplete card cannot launch.` |
| C1 read anchor | `grep -n -F "## DEPLOY PROOF" ops/desk/deploy-card.sh` | 0 | `29:` (comment), `566:    # ## DEPLOY PROOF: its non-blank lines up to the next "## " heading`, `567:    proof=$(awk …`, `569`, `570`, `574`, `575` (the `«FILL` lines). `:534-543` at BASE now holds the fix-report tip read, not the proof read: DECISIONS 1 |
| FR-G2 anchor | Read `CARD.md:64` | — | `` `## SMOKE READS` (deploy) — the set's own reads after the merge, one line each: label · the command typed whole · what a green answer looks like. `` … |
| FR-O1 source | Grep `brain-direction-2026-10-02.md` | 0 | `257:## RULED 2026-10-14 — remove the blockers …` · `263:6. Cards are written from a template: rulings cited by R number, no HEAD hashes, anchors by file:line.` |
| CARD.md credit lines | Read `CARD.md` | — | `:56` `` `## DEPLOY PROOF` (build, check; REQUIRED, his R1471 item 6) — … `` · `:78` `Owed by his R1471 (item 6); the test rule is brain R1472.` |
| wc | `wc -l "docs/40 - DevDocs/prompts/CARD.md" tests/ops/test_card_template_1014.py` | 0 | `158` · `59` |
| check report | `tail -n 3 …/card-template-check-2026-10-14.md` | 0 | `CHECK DONE · job: card-template-1014 · pass: 1 · tip: 5a29de43 · … · open: 5 · … · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 153702` |
| deploy report | `tail -n 3 …/deploy-hub-text-1013.md` | 0 | `FAILED: smoke (s) — tests/ops/test_hub_text_1013.py::test_h1_the_launch_line_and_every_other_line_stand red on the landed tree (BASE ce548f10 pinned; main's launch line moved since) · …` |
| RESTARTS | `uv run cobalt jobs restarts 2f6ae8fd..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` |

Card `## RECORDS` copied (the drafter's reads on `0ffb6949`/`f6cdc67f`, the CARD.md and deploy-card.sh anchors, the four existing pins, the restart class homes). Re-read: the `CARD.md` anchors moved (C1 and C2 have landed, card 550 deployed at `e4fa9e7b`); `deploy-card.sh:534-543` moved to `:566-575` (above). DB: none — no lock probe.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4328 passed, 806 skipped, 1 xfailed, 36 warnings in 665.43s (0:11:05)`; 0 failed, 0 errors. (Its one skip that names `COBALT_LIVE_VAULT_ROOT` is the offline run's own: `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`.)
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 29.16s`; skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Four tests appended to `tests/ops/test_card_template_1014.py`; the C1 and C2 tests stand unchanged. `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_card_template_1014.py` → `4 failed, 2 passed, 15 warnings in 0.84s`. Each red's first line:
- `test_fr_o1_both_credits_read_r1471_6_and_the_gap_filler_rows`: `assert "his R1471 (6): rulings by R number, … DESK RECORD)" in '`## DEPLOY PROOF` (build, check; REQUIRED, his R1471 item 6) — …'` (the credit has the old wording)
- `test_fr_o2_marker_clause_is_the_markers_form_with_grep_or_ls`: `assert 'marker lines in the form of `## MARKERS` (grep -c -F or ls)' in '…'` (the clause is still "one per file", grep only)
- `test_fr_g2_smoke_line_carries_a_label_first`: `assert 'label · the command typed whole · what a green answer looks like' in '…'` (no label)
- `test_fr_g3_refusal_clause_cites_desk_launch_994_and_deploy_card_31`: `assert 'does not launch (`desk-launch.sh:994`, `deploy-card.sh:31`)' in '…'` (no anchor on the refusal)
Commit `386af50d wip(card-template-1014-fr1): red — FR-O1, FR-O2, FR-G2, FR-G3 pins`.

## E3 THE ROWS
Three Edit calls on `CARD.md`: the `:56` credit (FR-O1), the `:56` refusal anchor, marker clause and smoke form (FR-G3, FR-O2, FR-G2), and the `:78` credit (FR-O1). `git diff 2f6ae8fd -- "docs/40 - DevDocs/prompts/CARD.md"` → 2 lines changed (`@@ -53,7 +53,7 @@` and `@@ -75,7 +75,7 @@`), nothing else.
GREEN: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_card_template_1014.py "tests/ops/test_deploy_card.py::test_n8_card_md_row_and_deploy_hub_phrase" "tests/ops/test_deploy_step_c.py::test_d1_card_md_names_launchd" "tests/ops/test_desk_launch_prechecks.py::test_f1_card_md_ships_header_has_the_fix_report_column_and_a_matching_separator" tests/ops/test_prodwrite_hub.py` → `26 passed, 15 warnings in 0.96s`. The four existing pins pass with no edit.
MUTATIONS: each mutation was one Edit, followed by `--tb=line` on the test file, then the Edit undone:
- M-O1: `:78` back to `Owed by his R1471 (item 6); the test rule` → `1 failed, 5 passed`; `FAILED …::test_fr_o1_both_credits_read_r1471_6_and_the_gap_filler_rows`, `…:83: assert "his R1471 (6): …" in "Owed by his R1471 (item 6); …"`.
- M-O2: marker clause back to `One marker line per file the set changes, in the form of `## MARKERS`: `grep -c -F "<fixed string>" <absolute path>`` → `1 failed, 5 passed`; `FAILED …::test_fr_o2_marker_clause_is_the_markers_form_with_grep_or_ls`, `…:90`.
- M-G2: `label · ` removed → `1 failed, 5 passed`; `FAILED …::test_fr_g2_smoke_line_carries_a_label_first`, `…:96`.
- M-G3: refusal anchor removed → `1 failed, 5 passed`; `FAILED …::test_fr_g3_refusal_clause_cites_desk_launch_994_and_deploy_card_31`, `…:101`.
After all undos, the same 26-test command → `26 passed`. The diff above is the fixed tree.
Test rule (ORDER): `grep -n -E -e "git show" -e "subprocess" -e "[0-9a-f]{8}" tests/ops/test_card_template_1014.py` → no output; `grep -n -F "BASE" tests/ops/test_card_template_1014.py` → `55:                   "a BASE hash"):` only.
DevDocs page line: no module changed (a fixed doc and a test only); no `docs/40 - DevDocs/cobalt/` page applies.
Commit `439ea472 fix(card-template-1014-fr1): DEPLOY PROOF credit, marker form, smoke label, refusal anchor (FR-O1, FR-O2, FR-G2, FR-G3; L35, L72)`.

## RESTARTS
`uv run cobalt jobs restarts 2f6ae8fd..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/reports/card-template-build-fr1-2026-10-15.md	A	DOCS	-
tests/ops/test_card_template_1014.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
- (a0) `git diff --name-only --no-renames 2f6ae8fd` → `docs/40 - DevDocs/prompts/CARD.md` · `tests/ops/test_card_template_1014.py`: every path starts with `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh card-template-1014-fr1 offline` → `tests/ops: run (docs/40 - DevDocs/prompts/CARD.md)` · `offline 8071/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/card-template-1014-fr1-offline-20261015-123252.log`. The new tests are the 4 `test_fr_*` tests in `tests/ops/test_card_template_1014.py`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh card-template-1014-fr1 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/card-template-1014-fr1-livenote-20261015-125838.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3743 passed, 1 xfailed, 16 warnings in 858.80s (0:14:18)`; `grep -n -F "SKIPPED"` on its output → none.
- with-DB: not run (DB: none). `.env`: never present (PREFLIGHT `env here` exit 1); no lock taken.

## PRE-STOP SELF-CHECK
(1) All 4 new tests failed in E2 for their rows' reasons, and each failed alone under its own mutation (M-O1, M-O2, M-G2, M-G3, quoted in E3). None stayed green, so none was rewritten. C1 and C2 are not part of this round; they were not changed.
(2) Entry paths: the one reader of these lines is the text of `CARD.md` (it is a doc, not code). `deploy-card.sh:567` reads only a job card's `## DEPLOY PROOF`, never `CARD.md`. Each of the 2 changed lines is pinned by content: `:56` by FR-O1, FR-O2, FR-G2, FR-G3 and C1; `:78` by FR-O1 and C2.
(3) Re-read at the tip: `grep -n -F "his R1471 (6)" CARD.md` → `56:` and `78:` (both lines as quoted); `grep -c -F "## DEPLOY PROOF" CARD.md` → `2` (the card's DEPLOY PROOF `after 2` holds); `git log --oneline 2f6ae8fd..HEAD` → `439ea472`, `386af50d`.

## FOR THE CHECK
- Range `2f6ae8fd..439ea472`: `386af50d wip(card-template-1014-fr1): red — FR-O1, FR-O2, FR-G2, FR-G3 pins` · `439ea472 fix(card-template-1014-fr1): DEPLOY PROOF credit, marker form, smoke label, refusal anchor (FR-O1, FR-O2, FR-G2, FR-G3; L35, L72)`.
- Reds, mutations, greens: E2 and E3 above. Caller greps: PREFLIGHT (`desk-launch.sh:994`, `deploy-card.sh:31`, `:566-575`).
- RUN row R3: the RESTARTS table above (`RESTARTS: none`).
- Suites: offline 8071/0, live-note 146/0, tests/ops 3743 passed; with-DB not run (DB: none); F0/F1/F2 not run (DB: none); lock not run (DB: none).
- No re-check follows this round (L75, the desk's message).

## CONTINUE
next: none — BUILT

## DECISIONS
1. ASK DESK: `CARD.md:56` still cites `deploy-card.sh:534-543` for how `## DEPLOY PROOF` is read. On BASE that read sits at `ops/desk/deploy-card.sh:566-575` (`:567` `proof=$(awk …`), and `:534-543` holds the fix-report tip read. Card 550's C1 test pins the needle `deploy-card.sh:534-543`. No FR row names this anchor, so changing it would go beyond the four rows. Safe default taken: left as it stands; a later card can re-anchor it and its C1 needle. [13:13]

## RECORDS
- The desk (`cto-desk`) sent at AUTHORIZATION: "this is a FIX ROUND on card 550 (already deployed at e4fa9e7b, now on main) … do only rows FR-O1, FR-O2, FR-G2, FR-G3 against main's CARD.md and its tests, anchoring by content; do not redo the card's original rows. No re-check follows (L75)." It names the card's own `## FIX ROUND` rows and adds no row, file, command or approval. Followed as the card's scope.
- The check's open items O2 and G1 are one clause (check report `:162`); FR-O2 settles both, so G1's FIXED line names the FR-O2 test.
- FR-O1's credit text is copied from the card row verbatim; its source line is `brain-direction-2026-10-02.md:263`.
- No lock was taken; `.env` never present.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: card-template-1014-fr1 · tip: 439ea472 | on 2f6ae8fd | migration: none | offline 8071/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 119323
