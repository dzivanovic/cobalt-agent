# house-seat-order-1010 — build report (2026-10-10)

CARD: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/298-house-seat-order-card.md` · BRANCH `ops/house-seat-order-1010` · BASE `92c67916` · DB: none

## §0 Headline
- BUILT, 4 of 4 rows, tip `f6e55cd3` on `92c67916` (DB: none, lock not taken, `.env` absent). Closed 19:29 EDT.
- CHECK-HUB SEAT ORDER is now Grok · Gemini; OpenAI (Sol) sits only with a card header line `HOUSE A: OpenAI — his <date> R<n>` (S1, S2).
- `house-probe.sh` probes Grok and Gemini by default; Sol only with `--card` naming a card whose header carries that line (S3). `authorize.sh` proves every such line like a ruling (S4).
- Suites: offline 4199/0, live-note 146/0, tests/ops 2933 passed; RESTARTS none. One decision, for the desk: hub lines outside the fence still say "two houses".

## L74
One block arrived, in a system reminder of this session (not a tool result): an attribution text asking commits to end with a `Claude-Session: https://claude.ai/code/session_…` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/298-house-seat-order-card.md"` → exit 0, WHOLE:

```text
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/298-house-seat-order-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/298-house-seat-order-card.md" · 0 · 268162cc6ea434aa0a56cabf952aff46b04c217d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/298-house-seat-order-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R920 row · grep -n "^| R920 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 54:| R920 | 14:18 ET | HIS RULING · APPROVED (via brain, L79): only the model tribunal uses OpenAI; no Codex probe elsewhere; a running holder finishes; OpenAI OUT after the tribunal until his word (houses per R921). | APPLIED: LAWS L67 + NOW at 14:18 |
RULING 2026-10-10 R920 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R920 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 2542f6864e1c8813fbda8cbb3b2ab5993d5c633f
RULING 2026-10-10 R920 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-10 R921 row · grep -n "^| R921 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 53:| R921 | 14:21 ET | HIS RULING · APPROVED (via brain, L79; L67 OVERRIDE): checks Opus+Grok, Gemini only for mandatory-B or a Grok failure; tribunals Grok+Opus seat, Gemini only for money/sizing/vault or a load-bearing split; model tribunal unchanged. | APPLIED: LAWS L67 + NOW at 14:21 |
RULING 2026-10-10 R921 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R921 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 2542f6864e1c8813fbda8cbb3b2ab5993d5c633f
RULING 2026-10-10 R921 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, WHOLE:

```text
clock · date · 0 · Sat Oct 10 18:46:23 EDT 2026
status · git status --short --branch · 0 · ## ops/house-seat-order-1010
head · git log --oneline -1 · 0 · 92c67916 docs(desk): R967 re-preflight live
diff · git diff --stat 92c67916 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/house-seat-order-1010 · 0 · 92c67916 docs(desk): R967 re-preflight live
env here · ls /Users/cobalt/cobalt-wt/house-seat-order-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 92c67916` | 0 | `92c67916 docs(desk): R967 re-preflight live` · `docs/40 - DevDocs/reports/cto-2026-10-10.md \| 2 +-` · `1 file changed, 1 insertion(+), 1 deletion(-)` |
| symbol: OpenAI in hub | `grep -n -F "OpenAI" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` | 0 | lines 23, 24, 25, 26, 90 (23 begins `SEAT ORDER, by the meter at launch (PREFLIGHT): OpenAI (Sol, `; 24 `- OpenAI up → A = OpenAI, B = Grok.`; 25 `- OpenAI out → A = Grok, B = Gemini.`; 26 `- OpenAI and Grok both out → A = Gemini, NO house B. …`; 90 `- **SOL:** \`codex exec …`) |
| symbol: `(all three` | `grep -n -F "(all three" …CHECK-HUB.md` | 0 | `65:- THE HOUSE GATES (AUTHORIZATION) · THE HOUSE PROBES, ONE call, \`run_in_background\`: \`sh /Users/cobalt/cobalt/ops/desk/house-probe.sh\` (all three: Sol, Grok, Gemini, …` |
| symbol: `**SOL` | `grep -n -F "**SOL" …CHECK-HUB.md` | 0 | `90:- **SOL:** \`codex exec --skip-git-repo-check -m gpt-5.6-sol …` |
| count | `grep -c -F -e "OpenAI up" …CHECK-HUB.md` | 0 | `1` |
| count | `grep -c -F -e "--card" ops/desk/house-probe.sh` | 1 | `0` |
| count | `grep -c -F -e "HOUSE A OpenAI" ops/desk/authorize.sh` | 1 | `0` |
| callers of house-probe | `grep -rn -F "house-probe" ops tests` | 0 | `ops/desk/order-open.sh:15` (comment), `:133` `if [ -f "$here/house-probe.sh" ]; then`, `:134` `sh "$here/house-probe.sh" 2>&1 \|\| echo "house-probe.sh exited non-zero"`; `ops/desk/preflight.sh:27` (comment); `ops/desk/bare-guard.py:11` (comment); `ops/desk/house-probe.sh:2`, `:53`; `tests/ops/test_order_open.py:7`, `:128`, `:231` (stubs); `tests/ops/test_house_probe.py:1`, `:21`; `tests/ops/test_bare_guard.py:1577` (comment) |
| callers of authorize.sh | `grep -rn -F "authorize.sh" ops tests` | 0 | `ops/desk/deploy-step0.sh:11`, `:190`, `:301`, `:305`, `:307` (`aout=$(LC_ALL=en_US.UTF-8 sh "$HERE/authorize.sh" deploy "$card" 2>&1)`); `ops/desk/authorize.sh:2`, `:42`; `tests/ops/test_deploy_step0.py:378`; `tests/ops/test_authorize.py:1`, `:17` |
| desk-launch | `grep -n -F "overruled" ops/desk/desk-launch.sh` | 0 | `150`, `245` (comments), `874:            *overruled*) ;;`, `877`, `878` |
| desk-launch | `grep -n -F "need TIP" ops/desk/desk-launch.sh` | 0 | `1020:    need TIP "CHECK REPORT" "HOUSE B"`, `1076:    need TIP TAG MIGRATIONS SET` |
| desk row R963 | `grep -n -F "\| R963 " …/reports/cto-2026-10-10.md` | 0 | `12:\| R963 \| 18:33 ET \| DESK RECORD (brain, L79): ONE card makes CHECK-HUB seat order and \`house-probe.sh\` Grok, Gemini (Sol only by header line, R920/R921); drafter prompt 297; … \| RECORD \|` |
| tail of READ report | `tail -n 3 …/reports/cto-2026-10-10.md` | 0 | last line `HANDOVER: predecessor e8778a8d → successor 092d855d at 18:15 · pane w2:pV1` |
| wc | `wc -l` of the five row files | 0 | `123 CHECK-HUB.md`, `109 house-probe.sh`, `156 test_house_probe.py`, `214 authorize.sh`, `241 test_authorize.py` |
| RESTARTS empty range | `uv run cobalt jobs restarts 92c67916..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` |

Files read whole: `house-probe.sh`, `test_house_probe.py`, `authorize.sh`, `test_authorize.py`, `CHECK-HUB.md`. At BASE the symbols the card names sit where it says: `house-probe.sh` usage `:2`, `refuse()` `:32-35`, house loop `:41-50`, unknown-house refusal `:44`, default set `:51`, `sol)` `:58-61`; `authorize.sh` `LC_ALL=C` `:28`, `field` `:78`, `prove` `:83`, `rulings` `:125`, HOUSE loop `:195-207`, `if [ -z "$failed" ]` `:209`; `test_authorize.py` `card_text` `:46`, `desk` `:55`, `recommit` `:88`, overrule test `:214-224`.

Card records copied: the card's `## RECORDS` (drafter at `8ba5a819`, amend at `85d2cd62`). Re-read here: the line counts (123/109/156/214/241, the table above), `OpenAI` on hub 23-26 and 90, `(all three` on 65, `- **SOL` on 90, `--card` 0 times in `house-probe.sh`, `HOUSE A OpenAI` 0 times in `authorize.sh`, the house-probe and authorize callers, `desk-launch.sh` `:874`, `:877`, `:1020`, and `grep -n -E "ops/desk|tests/ops" configs/cobalt/jobs.yaml` → no match (exit 1). RESTARTS: the empty range answers `RESTARTS: none`.

PROVEN BY FIRST REAL USE: class (a) `sh /Users/cobalt/cobalt/ops/desk/*` proven at AUTHORIZATION and PREFLIGHT (both ran); `uv run pytest *` at E0; `git add *` / `git commit *` at E2. No with-DB string is used (DB: none).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `92c67916` → exit 0: `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 644.39s (0:10:44)` — 0 failed, 0 errors (the offline skips are the with-DB and live-note skips; last one quoted: `SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → exit 0: `146 passed, 1 skipped, 15 warnings in 28.65s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests written (no `src/` edit; the card is DB: none, so no with-DB red and no lock take). `uv run pytest -q -p no:cacheprovider --color=no --tb=no -rfE tests/ops/test_house_probe.py tests/ops/test_authorize.py` on `92c67916` + the tests → `25 failed, 26 passed, 15 warnings in 10.83s`. Each red and its first line (from the `--tb=line` runs):

| row | test | red on BASE |
|---|---|---|
| S1 | `test_check_hub_seat_order_is_grok_gemini_and_openai_only_by_header` | `test_house_probe.py:190: assert 0 == 1 … where 0 = len([])` — no line starts the new `SEAT ORDER:` text |
| S2 | `test_check_hub_probe_step_calls_the_script_with_the_card` | `assert 'house-probe.sh --card "<card>"' in '- THE HOUSE GATES (AUTHORIZATION) · THE HOUSE PROBES, …'` (the line still holds `(all three`) |
| S3 T1 | `test_no_card_probes_grok_and_gemini_and_never_calls_codex` | `test_house_probe.py:94: AssertionError: assert [{'argv': ['e...-order-1010'}] == []` — `Left contains one more item: {'argv': ['exec', '--skip-git-repo-check', '-m', 'gpt-5.6-sol', …` |
| S3 T2 ×7 | `test_a_card_without_the_openai_line_makes_no_codex_call[plain, none-overruled, openai-alone, indented, overruled, tail, under-rows]` | each `test_house_probe.py:118: AssertionError: REFUSED: house '--card' is none of sol, grok, gemini` · `assert 1 == 0` |
| S3 T3 | `test_a_card_with_the_line_probes_sol_first_with_the_hub_spelling` | `test_house_probe.py:130: AssertionError: REFUSED: house '--card' is none of sol, grok, gemini` |
| S3 T4 | `test_naming_sol_without_the_line_is_refused[sol-alone]` | `test_house_probe.py:147: AssertionError: assert 0 == 1 … returncode=0, stdout='sol: UP\n'` |
| S3 T4 | `…[plain-card-sol]` | `test_house_probe.py:148: … "REFUSED: house '--card' is none of sol, grok, gemini\n".startswith("REFUSED: house 'sol' is probed only when the card header carries")` → False (red on the reason) |
| S3 T5 | `test_naming_sol_with_the_line_probes_only_sol` | `test_house_probe.py:158: AssertionError: REFUSED: house '--card' is none of sol, grok, gemini` · `assert 1 == 0` |
| S3 T6 ×3 | `test_a_bad_card_call_is_refused[no-path, missing, twice]` | each `test_house_probe.py:177: … "REFUSED: house '--card' is none of sol, grok, gemini\n".startswith('REFUSED: --card ')` → False (rc 1, red on the reason) |
| S3 (existing, now with `--card`) | `test_the_sol_stub_sees_the_hub_files_probe_exactly`, `test_a_house_that_says_nothing_is_out` | `assert [] == ['sol: UP']` (`:239`), `assert 1 == 0` with the unknown-house stderr (`:270`) |
| S4 A1 | `test_an_openai_house_line_with_its_approved_row_is_authorized` | rc 0 `AUTHORIZED`, then `AssertionError: ('row', …)` · `assert 'HOUSE A OpenAI 2026-01-02 R2 row · ' in '…AUTHORIZED\n'` |
| S4 A2 ×5 | `test_an_openai_house_line_without_its_row_fails[no-such-row, proposed, tail, openai-alone, second-house-a-line]` | each `test_authorize.py:262: … AUTHORIZED … assert 0 == 1` (rc 0 for every parameter: the line is unproved) |
| S4 A3 (pin) | `test_a_card_without_an_openai_line_prints_no_openai_row[plain, none-overruled]` | PASSES on BASE, as the row says |

Rewritten once: A3 `[plain]` first went red on `subprocess.CalledProcessError: Command '['git', '-c', 'core.hooksPath=/dev/null', 'commit', '-q', '-m', 'card']' returned non-zero exit status 1.` (the recommit of the fixture's unchanged card: nothing to commit), not on the row's reason; it now runs on the fixture's own committed card, and passes on BASE as a pin.
Commit: `d04e4291 wip(house-seat-order-1010): red` (2 files changed, 183 insertions(+), 8 deletions(-)).

## E3 THE ROWS
Built in card order, only the rows' files.
- **S1** `CHECK-HUB.md` lines 23-27 → TEXT S1 NEW, five whole lines, byte for byte from the card. `S1 test + tests/ops/test_hub_lines.py` → `20 passed, 15 warnings in 3.48s`.
- **S2** `CHECK-HUB.md` line 65 fragment → TEXT S2a NEW; line 90 label → TEXT S2b NEW; the rest of each line untouched. `S2 + S1 tests + test_hub_lines.py` → `21 passed, 15 warnings in 2.79s`.
- **S3** `ops/desk/house-probe.sh`: header (usage `house-probe.sh [--card <card>] [grok] [gemini] [sol]`, the header line spelled, the `sol` spelling note "only with the header line"); argument loop takes `--card <path>` (refusals `--card given twice`, `--card needs a path`, `--card <path> is not a readable file`); the header test `sed -n '/^## /q;p' "$card" | grep -q -x -e 'HOUSE A: OpenAI — his 20[0-9][0-9]-[0-9][0-9]-[0-9][0-9] R[0-9][0-9]*'` under the script's `LC_ALL=C`; a named `sol` without the line → `REFUSED: house 'sol' is probed only when the card header carries "HOUSE A: OpenAI — his <date> R<n>" (his 2026-10-10 R920)`; default set ` grok gemini`, or ` sol grok gemini` with the line. The `codex` / `grok` / `agy` calls, the limit and the output lines are unchanged. `test_house_probe.py test_order_open.py test_bare_guard.py test_hub_lines.py` → `1857 passed, 15 warnings in 95.10s (0:01:35)`.
- **S4** `ops/desk/authorize.sh`: two header-comment lines after `:17`, exactly the card's; after the HOUSE loop's `done`, a 15-line block (comment 2, code 13) reading every column-0 `HOUSE A: *OpenAI…` line of the whole card (`sed -n 's/^HOUSE A: *\(OpenAI.*\)$/\1/p'`, trailing blanks cut), each value matched against `^OpenAI — his <date> R<n>$` → `prove "HOUSE A OpenAI" <date> R<n>`, else `row "HOUSE A OpenAI" "field HOUSE A" 1 "no 'OpenAI — his <date> R<n>' alone on the line: <value>" 1`. `test_authorize.py test_deploy_step0.py` → `72 passed, 15 warnings in 31.90s`.

THE MUTATIONS (each made with Edit, run alone, undone with Edit):
| row | mutation | run | result, first failing line |
|---|---|---|---|
| S3 | default set always ` sol grok gemini` | `tests/ops/test_house_probe.py` | `8 failed, 18 passed` — T1 `test_house_probe.py:94: AssertionError: assert [{'argv': ['e...-order-1010'}] == []`; T2 ×7 `test_house_probe.py:119: AssertionError: assert ['sol: UP', '...UT — TIMEOUT'] == ['grok: OUT —...UT — TIMEOUT']` |
| S3 | the bare-`sol` refusal made `true \|\| refuse …` | `tests/ops/test_house_probe.py` | `2 failed, 24 passed` — T4 `[sol-alone]` and `[plain-card-sol]` `test_house_probe.py:147: AssertionError: assert 0 == 1 … stdout='sol: UP\n'` |
| S4 | block reads only the first `HOUSE A:` line (`set -- $(field "HOUSE A" \| sed -n 's/^\(OpenAI.*\)$/\1/p')`) | `tests/ops/test_authorize.py` | `1 failed, 24 passed` — `test_an_openai_house_line_without_its_row_fails[second-house-a-line]` `test_authorize.py:262: … AUTHORIZED … assert 0 == 1` |
| S4 | `prove` call skipped (`: prove …`) | `tests/ops/test_authorize.py` | `4 failed, 21 passed` — A1 `test_authorize.py:235: … assert 'HOUSE A OpenAI 2026-01-02 R2 row · ' in '…AUTHORIZED\n'`; A2 `[no-such-row]`, `[proposed]`, `[second-house-a-line]` `test_authorize.py:262: assert 0 == 1` |
| S1 | line 23 head back to `SEAT ORDER, by the meter at launch (PREFLIGHT): OpenAI (Sol, \`gpt-5.6-sol\`) · Grok …` | the S1 test | `1 failed` — `test_house_probe.py:190: assert 0 == 1 … where 0 = len([])` |
| S2 | `--card "<card>"` dropped from line 65 | the S2 test | `1 failed` — `test_house_probe.py:201: assert 'house-probe.sh --card "<card>"' in '- THE HOUSE GATES (AUTHORIZATION) · …'` |

After the undo: `git diff --stat` → `CHECK-HUB.md | 14 +++++-----`, `ops/desk/authorize.sh | 17 ++++++++++++`, `ops/desk/house-probe.sh | 49 +++++++++++++++++++++++++++++-----` (3 files changed, 67 insertions(+), 13 deletions(-)) = the fix; then `test_house_probe.py test_authorize.py test_hub_lines.py test_order_open.py test_bare_guard.py test_deploy_step0.py` → `1929 passed, 15 warnings in 122.02s (0:02:02)`. No named test stayed green under its mutation.

The card's counts at the fix: `wc -l` → `123 CHECK-HUB.md`, `231 authorize.sh`, `146 house-probe.sh`; `grep -c -F -e "OpenAI up"` hub → `0`; `grep -c -F -e 'house-probe.sh --card "<card>"'` hub → `1`; `grep -c -F -e "--card" ops/desk/house-probe.sh` → `6`; `grep -c -F -e "HOUSE A OpenAI" ops/desk/authorize.sh` → `3`; `git diff --numstat` → `7 7 CHECK-HUB.md`, `17 0 ops/desk/authorize.sh`, `43 6 ops/desk/house-probe.sh`.
DevDocs line: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` (Grep for `house-probe|authorize\.sh` over `docs/40 - DevDocs` outside `prompts/` and `reports/` → `No files found`); no page written (a new page is outside the rows' files) — `## RECORDS`.
Commit: `f6e55cd3 fix(house-seat-order-1010): check seat order Grok, Gemini; Sol only by a proved header line (S1-S4, L67, L72, L79)` (3 files changed, 67 insertions(+), 13 deletions(-)).

## RESTARTS
`uv run cobalt jobs restarts 92c67916..HEAD` (HEAD `f6e55cd3`) → WHOLE:

```text
path	change	rule	restart
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/house-seat-order-build-2026-10-10.md	A	DOCS	-
ops/desk/authorize.sh	M	operator script; no Cobalt reader	-
ops/desk/house-probe.sh	M	operator script; no Cobalt reader	-
tests/ops/test_authorize.py	M	test/documentation; no resident	-
tests/ops/test_house_probe.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row; nothing to classify.

## W THE THREE SUITES
`<tip>` = `f6e55cd3`. The card is "DB: none".
- (a0) `git diff --name-only --no-renames 92c67916` → WHOLE: `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `ops/desk/authorize.sh`, `ops/desk/house-probe.sh`, `tests/ops/test_authorize.py`, `tests/ops/test_house_probe.py` — every path under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 5 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh house-seat-order-1010 offline` → exit 0, verdict WHOLE: `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/house-seat-order-1010-offline-20261010-190748.log`. Executed (log line 2): `$ uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`; summary (log line 879): `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 670.91s (0:11:10)`. The tests this build adds live in `tests/ops` (the run below), not in this suite.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh house-seat-order-1010 livenote` → exit 0, verdict WHOLE: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/house-seat-order-1010-livenote-20261010-191917.log`. Executed (log line 2): `$ COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`; its one skip (log line 56): `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `2933 passed, 1 xfailed, 15 warnings in 551.37s (0:09:11)`; no SKIPPED line. The tests this build adds or changes are in it: `test_no_card_probes_grok_and_gemini_and_never_calls_codex`, `test_a_card_without_the_openai_line_makes_no_codex_call` ×7, `test_a_card_with_the_line_probes_sol_first_with_the_hub_spelling`, `test_naming_sol_without_the_line_is_refused` ×2, `test_naming_sol_with_the_line_probes_only_sol`, `test_a_bad_card_call_is_refused` ×3, `test_check_hub_seat_order_is_grok_gemini_and_openai_only_by_header`, `test_check_hub_probe_step_calls_the_script_with_the_card` (and the changed `test_the_sol_stub_sees_the_hub_files_probe_exactly`, `test_a_house_that_says_nothing_is_out`) in `tests/ops/test_house_probe.py`; `test_an_openai_house_line_with_its_approved_row_is_authorized`, `test_an_openai_house_line_without_its_row_fails` ×5, `test_a_card_without_an_openai_line_prints_no_openai_row` ×2 in `tests/ops/test_authorize.py`.
- (b)-(d), (f): not run (DB: none). `ls /Users/cobalt/cobalt-wt/house-seat-order-1010/.env` → `ls: /Users/cobalt/cobalt-wt/house-seat-order-1010/.env: No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red for its named reason: S1, S2, S3 T1-T6, the two changed sol tests, S4 A1 and A2 ×5 at E2 (the table in `## E2 RED`, quoted first lines); again under E3's mutations: T1 and T2 (default set mutation), T4 (refusal mutation), A2 `[second-house-a-line]` (first-line mutation), A1 and A2 `[no-such-row]`, `[proposed]`, `[second-house-a-line]` (skip-prove mutation), S1 and S2 (hub text mutations). A3 is the pin the row names: it passes on BASE and after. A2 `[tail]` and `[openai-alone]` go red at the strict-shape `row` call, which neither named mutation removes; their red on BASE is quoted at E2. One test was rewritten (A3 `[plain]`, for a git red, not the row's reason).
(2) Every entry path pinned: `house-probe.sh` callers from PREFLIGHT — `ops/desk/order-open.sh:134` (no argument) → pinned by T1 (no argument: grok, gemini, no codex call); CHECK-HUB line 65 (`--card "<card>"`) → pinned by the S2 test and T2/T3; `tests/ops/test_order_open.py:128`, `:231` (stubs, the fence) → green in the `tests/ops` run; the comments `preflight.sh:27`, `bare-guard.py:11`, `test_bare_guard.py:1577` carry no call. Flag combinations: no args (T1), `--card` alone with seven non-counting shapes (T2) and with the line (T3), `sol` alone / `--card <plain> sol` (T4), `--card <lined> sol` (T5), the three bad `--card` shapes (T6), the old bad calls (`test_a_bad_call_is_refused`). `authorize.sh` callers — `ops/desk/deploy-step0.sh:307` (deploy kind) → `test_deploy_step0.py` green and A3 (no line → no new row); CHECK-HUB line 41 (check kind) → A1-A3 run the `check` kind; the build kind runs the same block (AUTHORIZATION of this build: no OpenAI line, no row, `AUTHORIZED`).
(3) Re-read at the tip: `grep -n -F "SEAT ORDER"` hub → lines 23 and 65 as quoted; `grep -n -F "HOUSE A OpenAI" ops/desk/authorize.sh` → `18`, `220`, `222`; `grep -n -F "refuse" ops/desk/house-probe.sh` → `53`, `54`, `55`, `63`, `66`, `79` as quoted in E3; `git log --oneline 92c67916..HEAD` → the two commits below; the counts in E3 from the post-fix `wc -l`, `grep -c` and `git diff --numstat` calls.

## FOR THE CHECK
- Range `92c67916..f6e55cd3`: `d04e4291 wip(house-seat-order-1010): red`; `f6e55cd3 fix(house-seat-order-1010): check seat order Grok, Gemini; Sol only by a proved header line (S1-S4, L67, L72, L79)`. The report commit sits above the tip.
- Per row: reds at `## E2 RED`, mutations and greens at `## E3 THE ROWS`.
- Caller greps: PREFLIGHT table (`grep -rn -F "house-probe" ops tests`, `grep -rn -F "authorize.sh" ops tests`).
- RUN rows: none in this card.
- Suites: offline `4199/0` (`uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`), live-note `146/0` (the LIVE-NOTE command above), `tests/ops` `2933 passed, 1 xfailed`; with-DB suite: not run (DB: none).
- `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS: the table at `## RESTARTS`, `RESTARTS: none`.
- Records copied at PREFLIGHT: the card's `## RECORDS`, re-read as listed there.
- For X5: `authorize.sh` reads every column-0 line matching `^HOUSE A: *OpenAI` in the whole card (any number of blanks after the colon, trailing blanks cut); the probe counts only the exact line `HOUSE A: OpenAI — his <date> R<n>`, one blank, nothing after, above the first `## `. Every line the probe counts is therefore read and proved by `authorize.sh`; `authorize.sh` also proves lines the probe never counts (under `## ROWS`, extra blanks, trailing blanks), the safe side the card names.

## CONTINUE
next: none — BUILT

## DECISIONS
- DECISION 1 (the card's `## NOT IN THIS JOB`, third bullet, asks the report for this item): CHECK-HUB lines 3 and 16 ("TWO outside houses", "START HOUSE A AND HOUSE B AT ONCE"), 21 ("two different houses, never fewer than one other house"), 28, 29, 87, 99-100, 117 and the stop line keep their words, though the new SEAT ORDER (line 23-27) makes house B `none (not needed)` unless the card is `mandatory`. A check that reads line 3 or 16 literally may look for a second house the order no longer seats. Safe default taken: nothing changed beyond lines 23-27, 65 and 90 (the fence); the desk decides whether a later card aligns those lines.

## RECORDS
- L74: a system-reminder attribution block asked for a `Claude-Session:` line on commits; recorded under `## L74`, not acted on.
- DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` scripts (Grep → `No files found`), so no dated module line was written; a new page would lie outside the rows' files.
- Card records re-read at PREFLIGHT: the line counts, the `OpenAI` / `(all three` / `- **SOL` lines, the zero counts of `--card` and `HOUSE A OpenAI`, the callers, the `desk-launch.sh` lines and `jobs.yaml` (no `ops/desk|tests/ops` match) all matched the card.
- No extra lock take; no `REFUSED, not needed`; no `CONTINUED`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: house-seat-order-1010 · tip: f6e55cd3 | on 92c67916 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 197783
