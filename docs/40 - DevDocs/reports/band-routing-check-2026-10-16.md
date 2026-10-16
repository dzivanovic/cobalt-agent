# band-routing-1015 — check report (2026-10-16)

## §0 Headline
- Every row's rule re-proved on the tip `bd9c24ac`, and every mutation of the build report reproduced and undone. T1, R3 and the deploy gate are green: offline 8409/0, `tests/ops` 3841 passed with 2 xfailed, live-note 146/0, RESTARTS: none.
- 9 findings (6 mine, 3 from Grok). 2 HELD, NOT FIXED: O2, where a card path through `/./` skips the BAND refusal and builds on Opus, and O4, where CHECK-HUB accepts the untracked SHADOW-INSTRUCTIONS.md on shadow cards only, not routed ones. Both fixes sit outside what this check may edit.
- 5 REJECTED and open (O1, O3, G1, G2, G3): each red or shown for its stated reason, but a card row or brain ruling says the behaviour is right. 2 NOT HELD (O5, O6).
- ready: NO (held unfixed 2). Six items for the desk under `## DECISIONS`; none is his.

## L74
One block arrived as a system reminder after the launch message: an attribution instruction asking commits to end with a `Claude-Session: https://claude.ai/code/session_…` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (CHECK-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/633-band-routing-check-card.md"` (08:51 EDT), output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/633-band-routing-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/633-band-routing-check-card.md" · 0 · b9858dadc5bfc753d37468942493ef5bbf3cb33d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/633-band-routing-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```

House gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` · 0 · `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (one row)
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` · 0 · `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (one row)
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` · 0 · `5055151dbf68899b82de5b11f99733ed2d03048c`

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"`, output whole:

```
clock · date · 0 · Fri Oct 16 08:51:26 EDT 2026
status · git status --short --branch · 0 · ## ops/band-routing-1015
head · git log --oneline -1; git log --stat --format=%h bd9c24ac..HEAD · 0 · (6 lines)
    115e1f37 docs(band-routing-1015): build report — bd9c24ac
    115e1f37

     .../reports/band-routing-build-2026-10-15.md       | 201 +++++++++++++++++++++
     .../reports/band-routing-build-2026-10-15.result   |  15 ++
     2 files changed, 216 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/band-routing-1015/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/band-routing-1015/docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md" · 0 · BUILT · job: band-routing-1015 · tip: bd9c24ac | on f2ca3e1a | migration: none | offline 8409/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 7 of 7 | self-check: 3 of 3 | decisions: 6 · for Dejan: 0 · tokens: 276778
range · git log --oneline f2ca3e1a..bd9c24ac · 0 · (2 lines)
    bd9c24ac feat(band-routing-1015): BAND header, band table, launcher routing, routed check and result-file fence (B1-B6, L27 L29 L72)
    1be72d81 wip(band-routing-1015): red
PREFLIGHT OK
```

- THE RANGE: `git log --stat --format=%h f2ca3e1a..bd9c24ac` → `bd9c24ac`: BUILD-HUB.md 2+, CARD.md 3+, SHADOW-HUB.md 11 (+/-), ops/desk/bare-guard.py 5+, ops/desk/desk-launch.sh 71 (+/-), ops/desk/preflight.sh 26 (+/-) — 6 files, 111 insertions, 7 deletions; `1be72d81`: tests/ops/test_band_routing_1015.py 567+. Path union: 7 paths.
- DB: none: `git diff --name-only --no-renames f2ca3e1a..bd9c24ac` → `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `ops/desk/preflight.sh`, `tests/ops/test_band_routing_1015.py` — every path under `ops/`, `tests/ops/` or `docs/`.
- `ls <S>` → `No such file or directory` (fresh).
- House probes (`house-probe.sh --card "<card>"`), output whole:
  - `grok: UP`
  - `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings`
- Seats: card header has no `HOUSE A: OpenAI` line → `house A: grok · house B: none (not needed)` (`HOUSE B: as needed`).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`, output whole:
```
36010 <S>/diff.md
24394 <S>/files/633-band-routing-check-card.md
25728 <S>/files/band-routing-build-2026-10-15.md
34998 <S>/files/wt/docs/40 - DevDocs/prompts/BUILD-HUB.md
20176 <S>/files/wt/docs/40 - DevDocs/prompts/CARD.md
16996 <S>/files/wt/docs/40 - DevDocs/prompts/SHADOW-HUB.md
56410 <S>/files/wt/ops/desk/bare-guard.py
136316 <S>/files/wt/ops/desk/desk-launch.sh
11676 <S>/files/wt/ops/desk/preflight.sh
25412 <S>/files/wt/tests/ops/test_band_routing_1015.py
363 <S>/rulings.md
STAGED 11 files · 388479 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/band-routing-1015-check`; commits 2 = PREFLIGHT's range count.)
`stage-copy.sh`, one call each:
- `COPIED 37695 <S>/files/583-band-routing-card.md`
- `COPIED 4651 <S>/files/band-routing-answer-2026-10-16.md`
- `COPIED 3869 <S>/files/routing-table-answer-2026-10-14.md`
- `COPIED 28538 <S>/files/cto-2026-10-15.md`
- `COPIED 2743 <S>/files/wt/ops/desk/result-read.sh`
- `COPIED 37206 <S>/files/wt/ops/desk/deploy-card.sh`
- `COPIED 46201 <S>/files/wt/ops/desk/deploy-step0.sh`
- `COPIED 3659 <S>/files/wt/tests/ops/test_hub_text_1013.py`
- `COPIED 24406 <S>/files/wt/tests/ops/test_preflight.py`
- `COPIED 12098 <S>/files/wt/src/cobalt/jobs/restarts.py`
`<S>/HOUSE-INSTRUCTIONS.md` written (25487 bytes): HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, the Files paragraph.
House A Grok started 08:54 EDT (`date` 08:54:07), `run_in_background`, timeout 2700000. House B: none (not needed). Return: `git status --short --branch` → `## ops/band-routing-1015`.

## OWN FINDINGS
Written before any house list was opened (`## 2`).

FINDING O1
ROW: B5 / X6
CLAIM: `desk-launch.sh:1790-1793` reads routedness from the card the check launches on, and `CARD.md:23` makes `BAND` optional on a check card, so a routed build checked on its own check card that carries no `BAND` (the shape of this check's own card, dated 2026-10-16, no `BAND` line) is refused "not clean" for its untracked SHADOW-INSTRUCTIONS.md (`desk-launch.sh:1814-1815`).
RUN: TEST — tests/ops/test_band_routing_1015.py
```python
def test_o1_a_routed_tree_checked_on_a_check_card_without_band_reaches_its_check(cdesk):
    """CARD.md: BAND is optional on a check card; the routed tree's untracked file is still there."""
    done = cdesk.check(cdesk.card(None))
    assert NOT_CLEAN not in done.stderr, done.stderr
```
EXPECT: `AssertionError: … is not clean (the check session commits there)`.

FINDING O2
ROW: B3 / X1
CLAIM: `desk-launch.sh:1644-1645` takes the card's day from the first folder after `$PROMPTS/`, and the path gates (`:990-997`) admit `$PROMPTS/./<date>/…`, so a card dated 2026-10-16 with no `BAND`, named through `/./`, is not dated and launches on the Opus line instead of `REFUSED: incomplete card: BAND must be LOW, MID or HIGH`.
RUN: TEST — tests/ops/test_band_routing_1015.py
```python
def test_o2_a_new_card_named_through_a_dot_folder_still_needs_its_band(desk):
    card = desk.card_for(None)
    odd = str(desk.prompts) + "/./" + str(card.relative_to(desk.prompts))
    done = desk.run("build", odd)
    assert done.returncode == 1, done.stdout + done.stderr
    assert BAND_REFUSAL in done.stderr, done.stderr
```
EXPECT: `assert 0 == 1` (exit 0, the Opus build line on stdout).

FINDING O3
ROW: X5
CLAIM: `SHADOW-HUB.md:28` says "the fix round goes to the same builder" and names when the backup is launched ("only when Grok's probe is OUT or a Grok build ends FAILED on a harness cause, never on a 429"); R1532 and the routing answer's conditions 1-4 name neither, and the brain answer's note 7 (`band-routing-answer-2026-10-16.md:15`) says a routed card's fix round is a fresh `BAND: HIGH` card.
RUN: COMMAND — `grep -n -F "the fix round goes to the same builder" "docs/40 - DevDocs/prompts/SHADOW-HUB.md"`
EXPECT: `28:BAND ROUTING (his 2026-10-15 R1532; …; the fix round goes to the same builder, …`.

FINDING O4
ROW: B5 / X6 (brain Q2: "shadow-shaped wherever the untracked SHADOW-INSTRUCTIONS.md is accepted as clean")
CLAIM: `CHECK-HUB.md:64` and `:117` accept `?? SHADOW-INSTRUCTIONS.md` as "expected and recorded, not a finding" only "on a shadow card", so the check seat of a routed card meets `## 7` (v) `git status --short --branch` → `## <BRANCH>` alone with the untracked file standing; the diff widens the two scripts only.
RUN: COMMAND — `grep -n -F "is expected and recorded, not a finding" "docs/40 - DevDocs/prompts/CHECK-HUB.md"`
EXPECT: two lines (`64:`, `117:`), each naming "on a shadow card" and neither naming a routed card.

FINDING O5
ROW: X10
CLAIM: if `routed=""` (`desk-launch.sh:379`) did not reset it, a `routed=1` inherited from the environment would skip the three shadow refusals on a plain `shadow` launch.
RUN: TEST — tests/ops/test_band_routing_1015.py
```python
def test_o5_an_inherited_routed_does_not_skip_the_shadow_refusals(desk):
    card = desk.card_for("LOW")
    env = dict(desk.env, DESK_LAUNCH_DRY="1", routed="1")
    done = subprocess.run(["sh", str(desk.launch), "shadow", str(card), "--model", "grok-4.7"],
                          env=env, cwd=desk.tmp, capture_output=True, text=True, timeout=120)
    refused(done, "shadow: the card's header has no 'SHADOW OF:' line")
```
EXPECT (claim true): the refusal is missing and exit 0.

FINDING O6
ROW: B3 / X11
CLAIM: an older card that carries `BAND: LOW` would route, or print a `BAND:` line, if `band_dated` (`desk-launch.sh:1646-1649`) did not gate it; no test pins an older card with a `BAND` line.
RUN: TEST — tests/ops/test_band_routing_1015.py
```python
def test_o6_an_old_card_with_a_band_line_builds_as_before_and_is_not_routed(desk):
    card = desk.card_for("LOW", day=OLD_DAY)
    done = desk.run("build", str(card))
    assert done.returncode == 0, done.stderr
    assert "--model claude-opus-5-5" in done.stdout and "MODEL:" not in done.stdout
    assert "BAND:" not in done.stderr
    refused(desk.run("shadow", str(card), "--model", "grok-4.7", "--routed"),
            "shadow: --routed needs a card with BAND LOW or MID and its builder or backup id")
```
EXPECT (claim true): `MODEL: grok-4.7` on stdout, or `BAND: LOW` on stderr.

## Findings
House A Grok: `<S>/house-a.md` (written by Grok, 2119 bytes, 09:12), last line `FINDINGS: 3`. Its stdout was its progress text and the path. House B: none (not needed). The DROP: each block's `RUN:` line (`:4`, `:15`, `:27`) is followed by a `def test_` or one `grep` line; none dropped.

| id | house | row | claim | run |
|---|---|---|---|---|
| G1 | grok | B3 | a dated LOW card launched `build … PASS-2` is refused by the old `PASS-2 is an option of kind check only` (`:968`), not the routed refusal `:1660`; no test calls PASS-2 | TEST |
| G2 | grok | B2 | SHADOW-HUB's procedure (`:53` SHADOW OF original, `:70` `SHADOW BUILT`) carries no routed exception, though `:28` says a routed stop line is `BUILT` | TEST |
| G3 | grok | X5 | the backup-cause clause of `SHADOW-HUB.md:28` (`probe is OUT`, harness `FAILED`, `never on a 429`) is in no ruling | COMMAND |

## Dropped
none (every block of house A carries a `def test_` or one `grep` line).

## RUNS
Each test was put in `tests/ops/test_band_routing_1015.py` with Edit and run alone (`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line <file>::<test>`); each command run from the worktree. No test's form or assertion was changed.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus | `::test_o1_a_routed_tree_checked_on_a_check_card_without_band_reaches_its_check` | `1 failed` · `:504: AssertionError: … REFUSED: …/wt/x-job is not clean (the check session commits there)` | REJECTED — card B5: "A non-routed `ops/` card (no `BAND`, …) with the same file is still refused" (the B5 control `[None-2026-10-16]` pins it). The test is removed again. OPEN |
| O2 | opus | `::test_o2_a_new_card_named_through_a_dot_folder_still_needs_its_band` | `1 failed` · `:387: assert 0 == 1`; stdout is the worktree add, the cd and `claude --bg "Read '…/BUILD-HUB.md' … CARD: '…/prompts/./2026-10-16/01-x-band-card.md'" --model claude-opus-5-5 …` | HELD, NOT FIXED — `ops/desk/desk-launch.sh` (the card's `## NOT IN THIS JOB` fences every edit of it from this check). Committed as a strict xfail (`ee21824d`) |
| O3 | opus | `grep -n -F "the fix round goes to the same builder" "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` | `28:BAND ROUTING (his 2026-10-15 R1532; … the fix round goes to the same builder, the backup is the desk's hand launch only when Grok's probe is OUT or a Grok build ends FAILED on a harness cause, never on a 429):` | REJECTED — build card 583 B2 gives this paragraph byte for byte (`583-band-routing-card.md:34`, `grep -n -F` hit). OPEN (it disagrees with brain note 7) |
| O4 | opus | `grep -n -F "is expected and recorded, not a finding" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` | `64:CHECK-HUB §7(v) and ## PREFLIGHT: on a shadow card, ?? SHADOW-INSTRUCTIONS.md at the worktree root is expected and recorded, not a finding.` · `117:` the same line | HELD, NOT FIXED — `docs/40 - DevDocs/prompts/CHECK-HUB.md` (in no row's files) |
| O5 | opus | `::test_o5_an_inherited_routed_does_not_skip_the_shadow_refusals` | `1 passed` | NOT HELD (X10: the inherited `routed=1` is reset at `:379`; the `SHADOW OF:` refusal stands). Removed |
| O6 | opus | `::test_o6_an_old_card_with_a_band_line_builds_as_before_and_is_not_routed` | `1 passed` | NOT HELD (X11: an older `BAND: LOW` card builds Opus, prints no `BAND:`, and `--routed` is refused). Removed |
| G1 | grok | `::test_b3_pass2_on_a_routed_card_is_refused_with_the_row_sentence` | `1 failed` · `:293: AssertionError: REFUSED: PASS-2 is an option of kind check only` | REJECTED — card B3 names "a resume step on a routed card is refused (`:1660`)", not PASS-2; PASS-2 on a build is refused at `:968` with exit 1 and no launch. Removed. OPEN |
| G2 | grok | `::test_b2_the_procedure_excepts_a_routed_card_from_the_shadow_stop_line` | `1 failed` · `:115: assert 'routed' in '1. AUTHORIZATION: …'` | REJECTED — card A1 / brain Q1 (`band-routing-answer-2026-10-16.md:9`): "The B2 hub clause already tells the routed seat which stop line to write". Removed. OPEN |
| G3 | grok | `grep -n -F -e "never on a 429" -e "probe is OUT" "docs/40 - DevDocs/prompts/SHADOW-HUB.md" "docs/40 - DevDocs/reports/routing-table-answer-2026-10-14.md" "docs/40 - DevDocs/reports/cto-2026-10-15.md"` | one hit: `docs/40 - DevDocs/prompts/SHADOW-HUB.md:28:BAND ROUTING (…never on a 429):` | REJECTED — build card 583 B2 text (as O3). OPEN |

Wip commit of the held test: `ee21824d wip(band-routing-1015): check red — O2 (strict xfail: HELD, NOT FIXED, fix fenced to the builder)`. The xfail is `strict=True`: when the builder's fix round makes the test pass, the run goes red until the marker is removed.

THE CARD'S RUN ROWS, on the tip (`bd9c24ac`; the check's one test commit adds only the xfail):
- S0: `git diff --name-only --no-renames f2ca3e1a..bd9c24ac` → the seven paths of the row exactly (quoted under `## PREFLIGHT`). `git diff --stat bd9c24ac 115e1f37 -- . ":(exclude)docs"` → nothing. `git diff --stat f2ca3e1a bd9c24ac -- tests/ops` → ` tests/ops/test_band_routing_1015.py | 567 +…` · `1 file changed, 567 insertions(+)`. No `src/`, `configs/`, `.claude/` path.
- B3 tail: `git diff -U0 f2ca3e1a bd9c24ac -- ops/desk/desk-launch.sh` → hunks at tip `:379`, `:392-395`, `:1635-1685`, `:1714-1715`, `:1720`, `:1737`, `:1788-1793`, `:1814`; the last hunk is `:1814` in the check arm. `install-ops` sits at `:926` (`grep -n -F "install-ops\" ]"`), the launch tail after `:1826`: no hunk in either.
- A1: test (8) asserts (`:349-353`): `returncode == 0`, `"worktree add -b ops/x-band " in done.stdout`, `"shadow/" not in done.stdout`, `report in printed`; no `BUILT · job:` / `tip:` assertion. Test (8) and `test_b3_control_shadow_without_routed_still_demands_its_own_header`: PASSED (T1 below). `SHADOW-HUB.md:28` holds `its stop line is BUILD-HUB's BUILT · job: <JOB> · tip: <tip> …, not SHADOW BUILT` (O3's grep output).
- A2: the diff holds no `rm ` of SHADOW-INSTRUCTIONS (the full diff read above; the only SHADOW-INSTRUCTIONS hunks are `desk-launch.sh:1814` and `preflight.sh:159`). RED with the widening undone (`1LOW|1MID) routed_tree="" ;;`): `2 failed, 3 passed` — `…reaches_its_check[LOW]`, `[MID]`, `:471: … is not clean (the check session commits there)`; the three check controls passed. Undone: `git diff --stat bd9c24ac -- ops/desk/desk-launch.sh` → nothing.
- A3: `grep -n -F ".result" ops/desk/result-read.sh ops/desk/deploy-card.sh ops/desk/deploy-step0.sh ops/desk/desk-launch.sh` → `result-read.sh:5` (`its name the report's with .md cut and .result added`), `deploy-card.sh:489` `resf="${creport%.md}.result"`, `:530` `${frel%.md}.result`, `deploy-step0.sh:681` `resf="${report%.md}.result"`, `:762`, `desk-launch.sh:1462` `resf="${crep%.md}.result"`, `:1514`. Every reader cuts `.md`; none reads `report.md.result` (X8). The B6 mutation red: see below.
- A4: `git diff f2ca3e1a bd9c24ac -- ".../BUILD-HUB.md"` → one hunk, the added `BAND (his 2026-10-15 R1532): …` paragraph and a blank line (read above). HIGH asserts (`:99-100`): `"Opus 5.5" in got["HIGH"]`, `"grok" not in got["HIGH"] and "terra" not in got["HIGH"]`. Mutation `| HIGH | Opus 5.5 claude-opus-5-5 (the` → `1 failed`: `test_b2_control_the_three_builder_rows_stand` `:117: assert 'claude-opus-5-5' not in …`. Undone: `git diff --stat bd9c24ac -- ".../SHADOW-HUB.md"` → nothing.
- T1: `uv run pytest -q -rA -p no:cacheprovider --color=no -W ignore::DeprecationWarning tests/ops/test_band_routing_1015.py` → `36 passed, 1 xfailed in 7.35s` (the 36 of the build plus the O2 xfail); the 14 controls PASSED: `test_b1_control_the_other_header_rows_stand`, `test_b2_control_the_three_builder_rows_stand`, `test_b4_control_the_launch_line_and_the_model_line_stand`, `test_b3_control_a_high_card_builds_on_the_build_hub_line`, `test_b3_control_an_old_card_with_no_band_builds_as_before`, `test_b3_control_shadow_without_routed_still_demands_its_own_header`, `test_b5_control_…_dirty_at_its_check[None-2026-10-16]`, `[HIGH-2026-10-16]`, `[LOW-2026-01-02]`, `test_b5_control_…_still_fails_preflight_status[None-2026-10-16]`, `[HIGH-2026-10-16]`, `[LOW-2026-01-02]`, `test_b6_control_the_report_passes_and_every_other_path_is_still_fenced`, `test_b6_control_a_link_named_as_the_result_file_is_fenced`. `git diff --stat f2ca3e1a bd9c24ac -- <the six files>` → nothing. `grep -n -E -e "git show" -e "subprocess" -e "[0-9a-f]{8}" tests/ops/test_band_routing_1015.py` → `18: import subprocess`, `195`, `272`, `274`, `285`, `449`, `451`, `454`, `456`, `536`, `542` (the tmp-repo git helper and the runs of the launcher, preflight.sh and bare-guard.py): no `git show`, no 8-hex hash (X4).

THE MUTATIONS, each made with Edit, run, undone with Edit, the undo proved by `git diff --stat bd9c24ac -- <file>` printing nothing:
- B1 `| \`BAND\` |` → `| \`BANDX\` |`: `-k b1` → `1 failed, 1 passed` · `:70: assert 0 == 1`.
- B2 the LOW row deleted and the RESULTS sentence back to `Routing takes effect only on his word on the result (L29).`: `-k b2` → `2 failed, 1 passed` · `:95: AssertionError: ('LOW', [])` · `:106: AssertionError: assert 'R1532' in 'The desk copies this shape …'`.
- B4 `BAND (his R1532)`: `-k b4` → `1 failed, 1 passed` · `:126: assert 0 == 1`.
- B3 (one at a time, `-k b3`): the `exec sh "$0" shadow` line removed → `4 failed, 12 passed` ((1)[LOW], (1)[MID], (5), (8); `:299: assert 'MODEL: grok-4.7' in …` with the Opus line). The dated-card refusal `*) ;;` → `4 failed` ((3)[None], [low], [LOWISH], []). The resume refusal → `true` → `1 failed` ((6)). The `SHADOW OF` skip removed → `5 failed` ((1)×2, (5), (7), (8)). The last three sum to the report's `10 failed`; the report's `7 failed` combined `rok=1` with the exec removal, which I ran apart (4 failed).
- B5 (`-k b5`): `1LOW|1MID` → `1LOWX|1MIDX` → `2 failed, 8 passed` (check [LOW], [MID]). `routed_tree` set for any band → `3 failed, 7 passed` (the three check controls). Preflight's date gate `-ge 0` → `1 failed, 9 passed` (`…still_fails_preflight_status[LOW-2026-01-02]`).
- B6 G5 compares `report + ".result"` → `2 failed, 1 passed` · `test_b6_the_gate_seat_writes_its_result_file` `:550: … assert 2 == 0` · `test_b6_control_the_report_passes_and_every_other_path_is_still_fenced` `:565: (…/x-band-build.md.result, '') assert 0 == 2`.
After the last undo: `git status --short --branch` → `## ops/band-routing-1015`.
- T1/B2/B3/B4/B6 neighbours, no edit: `uv run pytest -q -p no:cacheprovider --color=no -W ignore::DeprecationWarning tests/ops/test_shadow_hub_file.py tests/ops/test_desk_launch_shadow.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_build_hub_no_clutter.py tests/ops/test_hub_lines.py tests/ops/test_deploy_card.py tests/ops/test_bare_guard.py tests/ops/test_preflight.py tests/ops/test_hub_text_1013.py` → `2335 passed in 205.97s (0:03:25)`.
- R3: `uv run cobalt jobs restarts f2ca3e1a..bd9c24ac` → `BUILD-HUB.md`, `CARD.md`, `SHADOW-HUB.md` `M DOCS -`; `bare-guard.py`, `desk-launch.sh`, `preflight.sh` `M operator script; no Cobalt reader -`; `tests/ops/test_band_routing_1015.py` `A test/documentation; no resident -`; `RESTARTS: none` = the header.
- X12: the kept slug test checks the signed `## BUILDERS` row's slug cell (`desk-launch.sh:1730-1734`, `ship_cell "$brows" 3`), not the card; under `--routed` only the JOB-ends-in-slug test (`:1735-1737`) is skipped, so a real card's JOB (`x-band` in test (1)) passes.
- X13: `grep -rn -F "expected on a" ops tests/ops` → `preflight.sh:167` (the shadow text), `:169` (the routed text), `tests/ops/test_preflight.py:427` (`SHADOW_EXPECTED`, the shadow text byte for byte). No reader greps the routed text.

## FIXES
- O2: HELD, NOT FIXED — `ops/desk/desk-launch.sh`
- O4: HELD, NOT FIXED — `docs/40 - DevDocs/prompts/CHECK-HUB.md`
No fix commit: the card's `## NOT IN THIS JOB` fences every edit of `desk-launch.sh`, and `CHECK-HUB.md` is in no row's files. No DevDocs line (no module changed).

## Suites
On the tip now, `ee21824d` (the build's `bd9c24ac` plus the check's xfail test). DB: none card, so W is (a0), (a), (e).
- RESTARTS: `uv run cobalt jobs restarts f2ca3e1a..HEAD` → the seven paths of R3 plus the build report `.md` and `.result` (`A DOCS -`) → `RESTARTS: none`.
- (a0): `git diff --name-only --no-renames f2ca3e1a` → `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `CARD.md`, `SHADOW-HUB.md`, `docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md`, `band-routing-build-2026-10-15.result`, `ops/desk/bare-guard.py`, `desk-launch.sh`, `preflight.sh`, `tests/ops/test_band_routing_1015.py`. Every path is under `ops/`, `tests/ops/` or `docs/`. `cobalt_dev: not taken (DB: none — 9 paths)`.
- (a): `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 offline --deploy-gate`, whole output: `tests/ops: run (deploy gate)` · `offline 8409/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-offline-20261016-091750.log`. Log `:888` `4568 passed, 806 skipped, 1 xfailed, 36 warnings in 677.76s (0:11:17)` · `:959` `3841 passed, 2 xfailed, 16 warnings in 827.90s (0:13:47)` (the second xfail is O2's).
- `uv run pytest -q -rs -p no:cacheprovider --color=no -W ignore::DeprecationWarning tests/ops` → `3841 passed, 2 xfailed in 841.08s (0:14:01)`.
- (e): `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-livenote-20261016-094316.log`. The only skip, `:56` `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`, does not name `COBALT_LIVE_VAULT_ROOT`.
- With-DB: not run (DB: none). `.env`: never present. `ls /Users/cobalt/cobalt-wt/band-routing-1015/.env` → `No such file or directory`.

## Scope
PREFLIGHT's path union (7 paths: three hubs, three `ops/desk` scripts, one test file) matches S0 exactly. My one commit, `ee21824d`, touches only `tests/ops/test_band_routing_1015.py`, the rows' test file. The xfail was added and the other test functions are as built. No `src/`, `configs/` or `.claude/` path, and no fenced file was edited by the check (every mutation was undone; `git status` is clean).

## Checked against the branch
- (i) `git log --oneline bd9c24ac..HEAD -- . ":(exclude)docs"` → `ee21824d wip(band-routing-1015): check red — O2 (strict xfail: HELD, NOT FIXED, fix fenced to the builder)`; `<tip now>` = `ee21824d`.
- (ii) `git log --stat --format=%h bd9c24ac..HEAD` → `ee21824d` `tests/ops/test_band_routing_1015.py | 11 +` · `115e1f37` the build report `.md` and `.result` (docs). No other path.
- (iii) `git log --oneline f2ca3e1a..HEAD -- .claude/settings.json .claude/settings.json.bak src configs` → nothing.
- (iv) `grep -n -F "def test_o2_a_new_card_named_through_a_dot_folder_still_needs_its_band" tests/ops/test_band_routing_1015.py` → `380:` (one line). It is HELD, NOT FIXED, so it has no `fix(` commit; its `wip(…): check red` commit is `ee21824d`.
- (v) `ls …/.env` → `No such file or directory`; `git status --short --branch` → `## ops/band-routing-1015` alone.
- (vi) `git log --stat --format=%h f2ca3e1a..HEAD -- src/cobalt/db_migrations tests/cobalt` → nothing: no migration and no with-DB test. Gate lists not owed.
- (vii) Card records: `git log --oneline -4 bd9c24ac` → `bd9c24ac`, `1be72d81`, `f2ca3e1a`, `da345e0b` (the record's `115e1f37` head sits above them; `git -C /Users/cobalt/cobalt log --oneline -1 ops/band-routing-1015` → `ee21824d` now). `grep -n -F "BAND_FROM" ops/desk/desk-launch.sh` → `1636`, `1642`, `1648`, `1788` (4 lines, as recorded). `grep -c -F "def test_" tests/ops/test_band_routing_1015.py` → `25` (the record's 24 plus O2).
- (viii) L32: this report quotes no ticker, price or date of his. The dates are the card folder days, the ruling dates and constructed test days.

## OPEN
- O2 HELD, NOT FIXED — `ops/desk/desk-launch.sh`. Settled by the builder's fix round: the card path gates (`:990-997`) refuse `/./` and `//`, or the day is read from the path's real folder. Then remove the strict xfail and `test_o2_…` passes.
- O4 HELD, NOT FIXED — `docs/40 - DevDocs/prompts/CHECK-HUB.md`. Settled by one hub line: `:64` / `:117` read "on a shadow card or a routed card (BAND LOW or MID, dated 2026-10-16 or later)". This is outside every row's files, so it needs a card row.
- O1 REJECTED (card B5). Settled by the desk saying how a routed build's check card carries `BAND`. Either `CARD.md:23` makes `BAND` required on the check card of a routed build, or the check reuses the build card (CARD.md `:5`).
- O3, G3 REJECTED (card B2 text). Settled by the desk: brain note 7 says the fix round is a fresh `BAND: HIGH` card, and the hub says it goes to the same builder. Also, the backup clause (`probe is OUT`, harness `FAILED`, `never on a 429`) rests on no ruling it names.
- G1 REJECTED (card B3 names a resume step only). Settled by nothing: PASS-2 on a build is refused by the older rule, with no launch.
- G2 REJECTED (brain Q1). Settled by the follow-up row of brain note 7 (SHADOW-HUB's routed procedure text).

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
1. O2 HELD, NOT FIXED — `ops/desk/desk-launch.sh`. A card dated 2026-10-16 with no `BAND`, named as `$PROMPTS/./2026-10-16/…-card.md`, is not dated (`:1644-1649`). It launches the Opus line instead of `REFUSED: incomplete card: BAND must be LOW, MID or HIGH`. RUNS row O2; test `tests/ops/test_band_routing_1015.py::test_o2_a_new_card_named_through_a_dot_folder_still_needs_its_band` (strict xfail, `ee21824d`). Safe default taken: not fixed, because the card fences every check edit of `desk-launch.sh`. It goes to the builder's one fix round. The failure is the safe band (Opus), so no LOW/MID launch comes from it.
2. O4 HELD, NOT FIXED — `docs/40 - DevDocs/prompts/CHECK-HUB.md`. `:64` and `:117` excuse the untracked SHADOW-INSTRUCTIONS.md on a shadow card only. The first routed card's check meets `## 7` (v) `## <BRANCH>` alone with that file standing. Safe default taken: not fixed (in no row's files). It needs a desk card row, or the desk's word that the check seat records it as on a shadow card.
3. ASK DESK [09:57]: the held test of a HELD, NOT FIXED finding would turn every suite red. I committed it as `@pytest.mark.xfail(strict=True, reason="check O2: HELD, NOT FIXED — …")`, with its assertion unchanged, so the gate stays green and the fix round's pass shows up as a strict-xfail red until the marker goes. Safe default taken: that form. The other way is to leave the test uncommitted and only in this report.
4. O1 (REJECTED, open): `CARD.md:23` makes `BAND` optional on a check card. A routed build checked on its own check card without `BAND` (this check card's shape) is refused "not clean" at `desk-launch.sh check`. preflight.sh fails the same way: it reads the same card. Safe default taken: none built. The drafter of a routed build's check card copies the build card's `BAND` line, until a row says so.
5. O3 / G3 (REJECTED, open): `SHADOW-HUB.md:28` says "the fix round goes to the same builder", against brain note 7 (a fresh `BAND: HIGH` card). Its backup clause names no ruling. Safe default taken: the hub text stands as the card gave it, and the desk follows note 7 for a routed fix round.
6. G1 / G2 (REJECTED, open; Grok): PASS-2 on a routed build card is refused by the older `PASS-2 is an option of kind check only`, with no launch. SHADOW-HUB's procedure text has no routed exception (brain Q1 kept it so). Safe default taken: both go to the follow-up list (note 7's row).
House B: none available (`as needed`; Gemini OUT at the probe), so the open items above go to the follow-up list. None touches his notes, money or sizing: for Dejan 0.

## RECORDS
- Gemini probe OUT: `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (a HARNESS line). Gemini was not launched; the card's HOUSE B is `as needed`.
- Grok's stdout was progress text plus the path; it wrote `house-a.md` itself, and I read it only after `## OWN FINDINGS` was written (08:59; Grok done 09:12).
- Dropped findings: none. No REFUSED call, no CONTINUE, no lock take.
- L74: one system reminder after the launch message asked for a `Claude-Session:` trailer. It is recorded under `## L74`; the commit carries `Co-Authored-By` only.
- Removed again with Edit (not held, or rejected and red): `test_o1_…`, `test_o5_…`, `test_o6_…`, `test_b3_pass2_…`, `test_b2_the_procedure_…`.
- The report's B3 `7 failed` combined two edits (exec removed and `rok=1`); I ran the exec removal alone (4 failed). Its `10 failed` matches my three separate runs (4 + 1 + 5).
- The report and `band-routing-check-2026-10-16.result` sit on `main` uncommitted, for the desk to commit together (CHECK-HUB `## LAUNCH`). This session's git writes run in the worktree only.
- files opened: 13 — `CHECK-HUB.md`, the card `633-band-routing-check-card.md`, `BUILD-HUB.md`, the build report, `ops/desk/desk-launch.sh`, `CARD.md`, `tests/ops/test_band_routing_1015.py`, `ops/desk/preflight.sh`, `ops/desk/bare-guard.py`, `band-routing-answer-2026-10-16.md`, `routing-table-answer-2026-10-14.md`, `areas/cobalt.md` (the two named sections), `<S>/house-a.md`. Also the background task output files of the probe, Grok, the gate runs and the pytest runs.
- Check of `band-routing-1015`: house A `grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: band-routing-1015 · pass: 1 · tip: ee21824d · house A: grok FINDINGS: 3 · findings: 9 · dropped: 0 · held: 2 · fixed: 0 · held unfixed: 2 · open: 7 · house B: none available · suites: offline 8409/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 6 · for Dejan: 0 · tokens: 271773
