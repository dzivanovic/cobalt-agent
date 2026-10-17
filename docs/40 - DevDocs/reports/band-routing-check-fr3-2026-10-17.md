# band-routing-1015 — CHECK after fix round 3 (FR-9) — 2026-10-17

## §0 Headline
- FR-9 holds for the BUILD seats. A routed or shadow gate seat whose tree holds only `?? SHADOW-INSTRUCTIONS.md` now closes through `desk-done.sh`. The three mutations each went red for their named reason, and every undo was proven.
- One own finding is HELD, NOT FIXED (O1): the CHECK of a routed or shadow card is still KEPT on the same file, because the watcher's `check` kind has no exception. `desk-watch.sh` is fenced, so the test is committed as a strict xfail (`3f399b60`).
- House A Grok `FINDINGS: 0`; house B none (as needed). The suites are green on `3f399b60`: offline 8439/0 (tests/ops 3871 passed, 3 xfailed), live-note 146/0. DB: none.
- M1: `SHADOW-HUB.md` will conflict when 671 merges after 583, and `desk-launch.sh:374-379` sits adjacent. That falls to 671's fix round.
- `ready: NO` (held unfixed 1).

## L74
The session's harness attribution reminder asks for a `Claude-Session:` line in commits. Recorded once as DATA (L74). Commits here carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"`, exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/692-band-routing-fr3-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/692-band-routing-fr3-check-card.md" · 0 · 573e96fd422a73dbe5a2bad8ab56cb35395d4e7c
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/692-band-routing-fr3-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → row 35 (one row); `grep -n "^| R19 "` → row 37 (one row); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"`, exit 0, whole:
```
clock · date · 0 · Sat Oct 17 13:11:00 EDT 2026
status · git status --short --branch · 0 · ## ops/band-routing-1015
head · git log --oneline -1; git log --stat --format=%h 4b62c2fa..HEAD · 0 · (6 lines)
    6c0ba560 docs(band-routing-1015): build report — 4b62c2fa (fix round 3, FR-9)
    6c0ba560

     .../reports/band-routing-build-fr9-2026-10-17.md   | 124 ++++++++++++++++++++-
     .../band-routing-build-fr9-2026-10-17.result       |  15 +++
     2 files changed, 136 insertions(+), 3 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/band-routing-1015/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 ".../band-routing-build-fr9-2026-10-17.md" · 0 · BUILT · job: band-routing-1015 · tip: 4b62c2fa | on f2ca3e1a | migration: none | offline 8439/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 171440
range · git log --oneline f2ca3e1a..4b62c2fa · 0 · (16 lines)
    4b62c2fa fix(band-routing-1015): close step excepts a shadow or routed seat's one untracked SHADOW-INSTRUCTIONS.md (FR-9, L1 L72)
    9bd05618 wip(band-routing-1015): fix round 3 red (FR-9)
    da95e8c7 wip(band-routing-1015): fix round 3 report opened (FR-9)
    8b142c56 wip(band-routing-1015): check red — O1 (strict xfail: HELD, NOT FIXED, desk-watch.sh fenced)
    4fc9b9da docs(band-routing-1015): build report — fda2300b (fix round 2, FR-6 to FR-8)
    fda2300b fix(band-routing-1015): routed launch watched as kind routed on <job>-gate; ...
    45b9d8c7 wip(band-routing-1015): fix round 2 red (FR-6 to FR-8)
    ac172ab9 wip(band-routing-1015): fix round 2 report opened (FR-6 to FR-8)
    7bf43c2b wip(band-routing-1015): check red — O1 O3 G1 (strict xfail: HELD, NOT FIXED, desk-launch.sh fenced)
    3ac61a2f docs(band-routing-1015): build report — c8c5ca90 (fix round FR-1 to FR-5)
    c8c5ca90 fix(band-routing-1015): card paths with /./ or // refused; ...
    01b10bdd wip(band-routing-1015): fix round red (FR-1 to FR-5)
    ee21824d wip(band-routing-1015): check red — O2 (strict xfail: HELD, NOT FIXED, fix fenced to the builder)
    115e1f37 docs(band-routing-1015): build report — bd9c24ac
    bd9c24ac feat(band-routing-1015): BAND header, band table, launcher routing, routed check and result-file fence (B1-B6, L27 L29 L72)
    1be72d81 wip(band-routing-1015): red
PREFLIGHT OK
```
(two long commit subjects shortened with `...` here; the tool output carries them whole.)
- THE RANGE typed, `git log --stat --format=%h f2ca3e1a..4b62c2fa`: 16 commits. Path union: `docs/40 - DevDocs/prompts/{BUILD-HUB,CARD,CHECK-HUB,SHADOW-HUB}.md`, the four build reports and three `.result` files, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `ops/desk/desk-watch.sh`, `ops/desk/preflight.sh`, `tests/ops/test_band_routing_1015.py`, `tests/ops/test_check_hub_shadow.py`.
- DB: none — `git diff --name-only --no-renames f2ca3e1a..4b62c2fa`, whole:
```
docs/40 - DevDocs/prompts/BUILD-HUB.md
docs/40 - DevDocs/prompts/CARD.md
docs/40 - DevDocs/prompts/CHECK-HUB.md
docs/40 - DevDocs/prompts/SHADOW-HUB.md
docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md
docs/40 - DevDocs/reports/band-routing-build-2026-10-15.result
docs/40 - DevDocs/reports/band-routing-build-fr1-2026-10-16.md
docs/40 - DevDocs/reports/band-routing-build-fr1-2026-10-16.result
docs/40 - DevDocs/reports/band-routing-build-fr6-2026-10-16.md
docs/40 - DevDocs/reports/band-routing-build-fr6-2026-10-16.result
docs/40 - DevDocs/reports/band-routing-build-fr9-2026-10-17.md
ops/desk/bare-guard.py
ops/desk/desk-launch.sh
ops/desk/desk-watch.sh
ops/desk/preflight.sh
tests/ops/test_band_routing_1015.py
tests/ops/test_check_hub_shadow.py
```
Every path under `ops/`, `tests/ops/` or `docs/`.
- `ls <S>` → `diff.md files house-a.md HOUSE-INSTRUCTIONS.md rulings.md`: present, left by the earlier checks of this JOB (cards 638, 666; mtimes 07:45-08:00 today), no `STAGED-CARD`. This is a fresh launch, not a `CONTINUE`; `stage-set.sh` on `main` carries the `STAGED-CARD` marker and its legacy fallback (`git -C /Users/cobalt/cobalt log --oneline -3 -- ops/desk/stage-set.sh` → `b093f192 fix(check-scratch-fr1): stage-set records STAGED-CARD …`): the card's ORDER dependency is deployed, and the staging clears the folder.
- House probes, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (background, exit 0), whole:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
No `HOUSE A: OpenAI` header line: Sol not probed. **house A: Grok · house B: none (not needed)** — the card reads `HOUSE B: as needed`; Gemini OUT is a HARNESS record (CHECK ASK X6), not a finding.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`, whole:
```
cleared: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/band-routing-1015-check (prior check /Users/cobalt/cobalt/docs/40 - DevDocs/reports/band-routing-check-fr2-2026-10-17.md)
35 <S>/STAGED-CARD
69931 <S>/diff.md
23601 <S>/files/692-band-routing-fr3-check-card.md
17413 <S>/files/band-routing-build-fr9-2026-10-17.md
34998 <S>/files/wt/docs/40 - DevDocs/prompts/BUILD-HUB.md
20258 <S>/files/wt/docs/40 - DevDocs/prompts/CARD.md
43727 <S>/files/wt/docs/40 - DevDocs/prompts/CHECK-HUB.md
17407 <S>/files/wt/docs/40 - DevDocs/prompts/SHADOW-HUB.md
25728 <S>/files/wt/docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md
220 <S>/files/wt/docs/40 - DevDocs/reports/band-routing-build-2026-10-15.result
20584 <S>/files/wt/docs/40 - DevDocs/reports/band-routing-build-fr1-2026-10-16.md
220 <S>/files/wt/docs/40 - DevDocs/reports/band-routing-build-fr1-2026-10-16.result
24427 <S>/files/wt/docs/40 - DevDocs/reports/band-routing-build-fr6-2026-10-16.md
220 <S>/files/wt/docs/40 - DevDocs/reports/band-routing-build-fr6-2026-10-16.result
1091 <S>/files/wt/docs/40 - DevDocs/reports/band-routing-build-fr9-2026-10-17.md
56410 <S>/files/wt/ops/desk/bare-guard.py
136683 <S>/files/wt/ops/desk/desk-launch.sh
12477 <S>/files/wt/ops/desk/desk-watch.sh
11676 <S>/files/wt/ops/desk/preflight.sh
40557 <S>/files/wt/tests/ops/test_band_routing_1015.py
4899 <S>/files/wt/tests/ops/test_check_hub_shadow.py
363 <S>/rulings.md
STAGED 22 files · 562925 bytes · commits 11
```
(`<S>` written for `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/band-routing-1015-check`.) `commits 11` against PREFLIGHT's 16: the diff is `-- . ":(exclude)docs"`; `git log --oneline f2ca3e1a..4b62c2fa -- . ":(exclude)docs"` → 11 commits (`4b62c2fa 9bd05618 8b142c56 fda2300b 45b9d8c7 7bf43c2b c8c5ca90 01b10bdd ee21824d bd9c24ac 1be72d81`); the other 5 (`da95e8c7 4fc9b9da ac172ab9 3ac61a2f 115e1f37`) are docs-only report commits. `grep -c "^commit " <S>/diff.md` → `11`. The diff is complete.
`stage-copy.sh`, one call each:
```
COPIED 89125 <S>/files/583-band-routing-card.md
COPIED 34776 <S>/files/band-routing-check-fr2-2026-10-17.md
COPIED 4606 <S>/files/check-662-and-583-fr2-decisions-2026-10-17.md
COPIED 28466 <S>/files/671-gemini-builder-row-card.md
COPIED 8725 <S>/files/670-gemini-probe-id-card.md
COPIED 12098 <S>/files/wt/src/cobalt/jobs/restarts.py
COPIED 7293 <S>/files/wt/ops/desk/desk-done.sh
```
`<S>/HOUSE-INSTRUCTIONS.md` written (24222 bytes): HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, and the Files paragraph.
House A Grok started 13:13 EDT (`date` 13:13:25; gates R17 row 35, R19 row 37, R19 commit `5055151d…` re-run first), background, timeout 2700000; `cd` back, `git status --short --branch` → `## ops/band-routing-1015`.

## OWN FINDINGS
Written before any house list was opened. Read: `desk-watch.sh` whole at the tip, `git diff 8b142c56 4b62c2fa -- ops/desk/desk-watch.sh tests/ops/test_band_routing_1015.py`, `preflight.sh:110-179`, `desk-launch.sh:282-289`, `:1795-1824`, `:2356`, `test_band_routing_1015.py:480-739`, the build report `:70-154`, BUILD-HUB `:33-94`, cobalt.md `:21-65`, `grep` of `deploy-card.sh` for `BUILT`, `grep` of the prompts for `routed|SHADOW-INSTRUCTIONS`.

FINDING O1
ROW: FR-9 (X2, X3)
CLAIM: FR-9 excepts the file for the kinds `shadow` and `routed` only (`ops/desk/desk-watch.sh:101`). But the CHECK of a routed or shadow card runs in the same worktree, and that worktree still holds the untracked `SHADOW-INSTRUCTIONS.md`. The launcher accepts the file for that check (`ops/desk/desk-launch.sh:1817`), and so do `ops/desk/preflight.sh:159` and CHECK-HUB `:64`/`:117`. The launcher prints `desk-watch.sh check "<card>"` for it (`desk-launch.sh:2356`). At `CHECK DONE`, `unclean()` therefore reads the file as dirt, and the close prints `KEPT <id>: tree not clean` instead of handing `check` to `desk-done.sh`. This is the O1 hang of the fr2 check, moved one seat down.
RUN: TEST — `tests/ops/test_band_routing_1015.py`
```python
@pytest.mark.parametrize("shadow", [False, True], ids=["routed", "shadow"])
def test_check_fr3_o1_a_routed_or_shadow_cards_check_closes_on_the_instructions_file(tmp_path, shadow):
    w = RWatch(tmp_path / "w", done=True, last="CHECK DONE · job: x · pass: 1", shadow=shadow)
    w.card.write_text(w.card.read_text().replace("RULINGS:", f"CHECK REPORT: {w.report}\nRULINGS:"))
    (w.wt / "SHADOW-INSTRUCTIONS.md").write_text("constructed\n")
    w.rows("sess-x01 · x-job-check · ~/cobalt-wt/x-job · idle · idle")
    done = w.run("check")
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines()[0] == "CHECK DONE · job: x · pass: 1", done.stdout
    assert w.logged() == [f"sess-x01 {w.report} check"], done.stdout
```
EXPECT: both cases red: `AssertionError: CHECK DONE · job: x · pass: 1` / `KEPT sess-x01: tree not clean` / `assert [] == ['sess-x01 … check']`.

## Findings
House A Grok finished at 13:23 EDT (`date` 13:23:20; background exit 0). `ls -la <S>` → `house-a.md` 12 bytes. `<S>/house-a.md`, whole: `FINDINGS: 0`. Grok's stdout ended with the path and the line "The fix matches the row: the exception is only the one status line, only for those two kinds, and the tests pin that. No defect to hand over." House B: none (not needed; `HOUSE B: as needed`).
No house finding to keep.

## Dropped
none (Grok wrote no `FINDING` block)

## RUNS
### The findings
- O1 · opus · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py -k test_check_fr3_o1` → `2 failed, 66 deselected`: `[routed]` and `[shadow]` both `AssertionError: CHECK DONE · job: x · pass: 1` / `KEPT sess-x01: tree not clean` / `assert [] == ['sess-x01 /p...ild.md check']` (`:713`). Control: the same test with the `SHADOW-INSTRUCTIONS.md` write removed → `2 passed`, so the file is the only cause; the line was restored by Edit. Verdict: **HELD, NOT FIXED — ops/desk/desk-watch.sh** (`## NOT IN THIS JOB`: no edit of `desk-watch.sh`). Committed as a strict xfail (the form of `8b142c56`), the assertion unchanged: `3f399b60 wip(band-routing-1015): check red — O1 (strict xfail: HELD, NOT FIXED, desk-watch.sh fenced)`. With it the file reads `66 passed, 2 xfailed`, each `XFAIL …[routed]` / `[shadow]` `- check fr3 O1: HELD, NOT FIXED — ops/desk/desk-watch.sh (fenced)`.

### The card's rows
- S0 · `git diff --name-only --no-renames 8b142c56 4b62c2fa` → `docs/40 - DevDocs/reports/band-routing-build-fr9-2026-10-17.md`, `ops/desk/desk-watch.sh`, `tests/ops/test_band_routing_1015.py` (exactly the three). `git diff --stat 4b62c2fa 6c0ba560 -- . ":(exclude)docs"` → nothing. `git diff --name-only --no-renames f2ca3e1a..4b62c2fa` → the 17 paths under PREFLIGHT: no `src/`, `configs/` or `.claude/` path, and no `desk-done.sh`. `git diff --stat 8b142c56 4b62c2fa` → `desk-watch.sh | 5 ++-`, `test_band_routing_1015.py | 46 ++-`, the report `| 36 +`. `git diff 8b142c56 4b62c2fa -- ops/desk/desk-watch.sh` → one hunk `@@ -96,7 +96,10 @@ listed()`, one line out (`[ -z "$(git -C … status --short 2>&1)" ] || { echo "tree not clean"; return; }`) and four in (the `dirt=` read, the `# card 583 FR-9` comment, the `case`, the `[ -z "$dirt" ]` test), all inside `unclean()`. The FR-6 arms `:65`, `:74` and the mapping `:156` are untouched. Test diff: `@@ -646,7 +646,6 @@` removes only the strict-xfail decorator above `test_check_o1_…`, and `@@ -657,6 +656,51 @@` adds the FR-9 block (three tests, four cases). No other body changed. `git status --short --branch` → `## ops/band-routing-1015`.
- FR-9 · read at the tip: `desk-watch.sh:97` `unclean() {`, `:99` the `dirt=` read, `:100` the comment, `:101` `case "$kind" in shadow|routed) [ "$dirt" != "?? SHADOW-INSTRUCTIONS.md" ] || dirt="" ;; esac`, `:102` `[ -z "$dirt" ] || { echo "tree not clean"; return; }`, `:103-110` (report committed, session busy) unchanged. Callers: `close_worker` `:129` and `:138`, both `why=$(unclean)`, so `dirt` lives in the `$(…)` subshell. `prodwrite` and `close` skip `unclean` (`:126`). It is an exact string compare of the whole output, so any second line, a modified file or a nested path keeps "tree not clean". **The three places, compared:** `preflight.sh:159` (`check` of a shadow or routed card, the one status line under the branch line), `desk-launch.sh:1817` (`check` of a shadow card or a routed tree, `--porcelain`), and `desk-watch.sh:101` (the watcher's `shadow` and `routed` kinds, `--short`). All three use the same exact one-line equality, but their kinds do not match: the launcher and preflight except the file for the CHECK of such a card, and the watcher does not (`check` is not in `:101`). That gap is O1. **Kinds that still read the file as dirt:** `build`, `check` and `devfix` (`:72`, `wt` set, through `close_worker` `:129`/`:138`). `deploy` has `wt=-` (`:75`), so it never reads the tree. A first-wave `build` of a HIGH card has no such file, so `build` is right. `devfix` of a routed card is its own fresh HIGH card (SHADOW-HUB `:28`), so it is right too. `check` is wrong for a routed or shadow card (O1). The strict xfail at the tip: the stage copy of `test_band_routing_1015.py` from blob `4b62c2fa` (Grep `xfail`) → 0 matches; in the worktree now the one hit is this check's `:704`. GREEN, `uv run pytest -q -rA -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py -k "check_o1 or fr9"` → `5 passed, 63 deselected`: `PASSED …::test_check_o1_a_routed_closeout_on_a_gate_seat_tree_hands_build_to_desk_done`, `…::test_fr9_a_shadow_card_tree_holding_only_the_instructions_file_closes`, `…::test_fr9_control_a_build_kind_tree_holding_that_file_is_still_kept`, `…[untracked]`, `…[modified]`. The helpers (`:494-546`): the build control rewrites `BAND: LOW` to `BAND: HIGH` (the watcher reads no BAND; the kind decides) and lists `IDLE_JOB_BUILD` (`x-job-build`). The modified control commits `tracked.txt`, then changes it. Each control tests its named case.
  MUTATIONS (Edit; each undone, `git diff --stat 4b62c2fa -- ops/desk/desk-watch.sh` → nothing after each):
  (a) `:99-102` back to the single read of `9bd05618` (`git diff 9bd05618 -- ops/desk/desk-watch.sh` → nothing while mutated) → `--runxfail` `2 failed, 3 passed`: `:656` `AssertionError: BUILT · job: x · tip: tip-x | on base-x | rows: 1 of 1 / KEPT sess-x01: tree not clean` / `assert [] == ['sess-x01 /p...ild.md build']` and `:670` `SHADOW BUILT … / KEPT sess-x01: tree not clean` / `assert [] == ['sess-x01 /p...ld.md shadow']`. The three controls passed.
  (b) `case "$kind" in shadow|routed|build)` → `1 failed, 4 passed`: `:681` `test_fr9_control_a_build_kind_…` `assert 'CLOSED sess-x01' == 'KEPT sess-x0...ree not clean'`.
  (c) equality loosened to `case "$dirt" in *SHADOW-INSTRUCTIONS.md*) dirt="" ;; esac` → `2 failed, 3 passed`: `[untracked]` and `[modified]` `:700` `assert 'CLOSED sess-x01' == 'KEPT sess-x0...ree not clean'`.
  Hand run: not needed. The `[untracked]` control is exactly the routed tree with `?? SHADOW-INSTRUCTIONS.md` plus `?? notes.txt`, and it is KEPT. The controls were green before and after (the GREEN run above, and the `66 passed` E1 run after every undo).
- D1 · build report `:141-142` `## DECISIONS` / `none`; stop line `:154` `… decisions: 0 · for Dejan: 0 · tokens: 171440`. Both are confirmed. The design choice: the exception is the whole-output equality inside `unclean()` in the `$(…)` subshell, the shape of `desk-launch.sh:1817`. Keep. The header comment `:16-23` does not name it (a record by the fence). Grep of the worktree for `any other is CLEAN` → `ops/desk/desk-watch.sh` and the build report only, so no test or hub reads it. **Shadow gains the same close as routed:** yes. `test_fr9_a_shadow_…` shows `desk-done.sh <id> <report> shadow` called once, and mutation (a) turns it KEPT. Tests that pin a KEPT on "tree not clean": `tests/ops/test_close_automation_1015.py:144` (kind `build`, `stray.txt`, not the instructions file) and this file's `:681`, `:700` (the FR-9 controls). None pins the old shadow KEPT on the file.
- M1 · merge bases: `git merge-base ops/gemini-builder-row-1017 main` → `7f415a4f…`; `git merge-base ops/gemini-probe-id-1017 main` → `f2140694…`. Stats: 583 `git diff --stat f2ca3e1a ops/band-routing-1015 -- <three>` → `SHADOW-HUB.md | 15`, `bare-guard.py | 5`, `desk-launch.sh | 80` (90+, 10-). 671 `git diff --stat 7f415a4f ops/gemini-builder-row-1017 -- <three>` → `SHADOW-HUB.md | 12`, `bare-guard.py | 15`, `desk-launch.sh | 4` (22+, 9-), head now `8ba22eaf`. 670 `git diff --stat f2140694 ops/gemini-probe-id-1017 -- <three>` → nothing; its whole stat → `CHECK-HUB.md`, `STANDING-LIST.md`, its report and `.result`, `ops/desk/house-probe.sh`, `tests/ops/test_house_probe.py`. So 670 touches none of the three. Both diffs start from the same pre-image blobs (`SHADOW-HUB.md` `1b63a76d`, `bare-guard.py` `0a486be5`, `desk-launch.sh` `f3d3f3b4`), so the hunk lines compare directly. Hunk headers:
  - `SHADOW-HUB.md`: 583 `@@ -25,6 +25,15 @@` (the `BAND ROUTING (` paragraph and band table, inserted after the Terra note `:26` and its blank line, just before the `<pass prompt>` line), `@@ -41,7 +50,7 @@` (`:53`), `@@ -58,7 +67,7 @@` (`:70`), `@@ -70,7 +79,7 @@` (RESULTS TABLE). 671 `@@ -9,24 +9,28 @@` (the refusal line, the `## BUILDERS` intro, a Gemini table row, a Gemini note and the X1 paragraph inserted after the same Terra note, and the `<pass prompt>` line rewritten), `@@ -85,7 +89,7 @@` (the Gemini results row). **Overlap: 583's `-25,6` sits inside 671's `-9,24`. Both insert at the same point, after the Terra note, and 671 also rewrites the `<pass prompt>` line that follows 583's insert. A textual conflict is certain.** 583's `-70,7` and 671's `-85,7` are disjoint.
  - `bare-guard.py`: 583 `@@ -1274,6 +1274,11 @@` (`g5`, the B6 `.result` admit); 671 `@@ -1181,8 +1181,8 @@`, `@@ -1198,14 +1198,21 @@` (`builder_call`). Disjoint by more than 70 lines: no conflict.
  - `desk-launch.sh`: 583 `@@ -376,6 +376,7 @@` (`routed=""` after `builder=""`, old `:378`) and 671 `@@ -374,6 +374,7 @@` (a comment after old `:376`, before `model=""`). Two unchanged lines lie between them (`model=""`, `builder=""`): adjacent, not overlapping, so a conflict is possible but not certain. 583 `@@ -388,6 +389,10 @@` (`--routed` arm after old `:390`) and 671 `@@ -395,7 +396,8 @@` (the `gemini-*` line, old `:398`): about 7 lines apart, likely clean. 583's other hunks (`-983`, `-1627`, `-1655`, `-1677`, `-1728`, `-1748`, `-2287`) are untouched by 671.
  In deploy order 583, 671, 670, any conflict falls on the second deploy (671 onto a main carrying 583): certainly `SHADOW-HUB.md`, possibly `desk-launch.sh:374-379`. That is 671's fix round's to resolve (the fence; not resolved here). 670 merges with no overlap on these three files. (`git merge-tree` is not on the list; this is read from the hunks.)
- E1 · one mutation per row where the second check named one, each undone, the undo proved by `git diff --stat 4b62c2fa -- <file>` → nothing:
  FR-6 (c): `desk-watch.sh:156` mapping back to `"$kind"` → `2 failed, 3 passed` (`-k "fr6 or check_o1"`): `test_fr6_a_routed_closeout_…` `:576` and `test_check_o1_…` `:656`, both `assert ['sess-x01 /p...ld.md routed'] == ['sess-x01 /p...ild.md build']`.
  FR-7 mutation 2: the pass-through `*/./*|*//*) ;;` line removed (`desk-launch.sh:991`) → `2 failed, 6 passed` (`-k "fr7 or o3 or o2 or fr1"`): `test_o2_…` `:382` and `test_fr1_…` `:393`, each `REFUSED: the card must be …/prompts/<YYYY-MM-DD>/<nn>-<job>-card.md: …/prompts/./2026-10-16/…` (and `prompts//2026-10-16/…`) in place of `the card path holds '/./' or '//'`.
  FR-8: `SHADOW-HUB.md:28`'s clause restored to the parent's `(R1532: Terra backup; 2026-10-14 item 7: a 429 is retried, never a backup)` → `2 failed, 2 passed` (`-k "fr8 or fr4"`): `test_fr4_…` `:464` and `test_fr8_…` `:634`, `AssertionError: brain 2026-10-16, reading R1532's 'Terra backup'`. The controls passed.
  Reads: `desk-watch.sh:65` `routed) report=$(header REPORT) || exit 1; re='^(BUILT ·|FAILED)' ;;`, `:74` `routed) … session="$job-gate" ;;`, `:156` the mapping; `desk-launch.sh:990-995` the first card `case` (`the card must be` at `:992`, `:994`); SHADOW-HUB `:28` ends `… R1471 (7) is recorded in the direction file)):`. FR-1 to FR-5 and B1-B6 through their tests in the whole-file run.
  Pins: `uv run pytest -q -rA -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py` → `66 passed, 2 xfailed, 15 warnings in 25.48s`. The 66 are the build's 66, all PASSED. The 2 xfailed are this check's O1 (`3f399b60`). PASSED lines include every `test_b1_…`, `test_b2_…` (3), `test_b3_…` (16 cases), `test_b4_…` (2), `test_b5_…` (10 cases), `test_b6_…` (3), and the controls `test_b1_control_…`, `test_b2_control_…`, `test_b4_control_…`, `test_b3_control_…` (3), `test_fr1_control_…`, `test_fr2_control_…`, `test_fr4_control_…`, `test_fr5_control_…`, `test_fr6_control_…` (2), `test_fr7_control_…`, `test_fr8_control_…`, `test_fr9_control_…` (3 cases), `test_fr3_control_…` (2 cases), `test_b5_control_…` (6 cases), `test_b6_control_…` (2). The eight files: see `## Suites`. `git diff --stat 8b142c56 4b62c2fa -- <the eight>` → nothing. `grep -n -E -e "git show" -e "[0-9a-f]{8}" tests/ops/test_band_routing_1015.py` → no output (exit 1).
- R3 · `uv run cobalt jobs restarts 8b142c56..4b62c2fa` → `band-routing-build-fr9-2026-10-17.md A DOCS -` · `ops/desk/desk-watch.sh M operator script; no Cobalt reader -` · `tests/ops/test_band_routing_1015.py M test/documentation; no resident -` · `RESTARTS: none`. `… f2ca3e1a..4b62c2fa` → 17 rows: the 11 `docs/` paths `DOCS`; `bare-guard.py`, `desk-launch.sh`, `desk-watch.sh`, `preflight.sh` `operator script; no Cobalt reader`; the two tests `test/documentation; no resident`; `RESTARTS: none`. The header's `none` holds.
- G1 · see `## Suites`.
- X4 · FR-9 changes no hub: `git diff --name-only 8b142c56 4b62c2fa` holds no `docs/40 - DevDocs/prompts/` path. X6: Grok ran from the staged copies, wrote `FINDINGS: 0`, and made no keyed call that this check can see. House B: N/A (Gemini OUT on the CLI's model id), a harness record.

## FIXES
- O1: HELD, NOT FIXED — ops/desk/desk-watch.sh (fenced by `## NOT IN THIS JOB`; it goes to the original builder's one fix round, `## DECISIONS`)
No `fix(band-routing-1015):` commit; no DevDocs line (no module changed).

## Suites
On the tip `3f399b60` (the build's `4b62c2fa` plus this check's red commit; DB: none, W (a0), (a), (e)):
- RESTARTS: `uv run cobalt jobs restarts f2ca3e1a..HEAD` → the 18 paths (the 17 above plus the fr9 `.result`), DOCS / operator script / test rules, `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames f2ca3e1a` → 18 paths, each under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 18 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 offline --deploy-gate` (background, exit 0), whole:
```
tests/ops: run (deploy gate)
offline 8439/0
log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-offline-20261017-132732.log
```
  In the log: `:888` `4568 passed, 806 skipped, 1 xfailed, 36 warnings in 664.36s (0:11:04)`; `:959` (tests/ops whole) `3871 passed, 3 xfailed, 16 warnings in 845.68s (0:14:05)` (the build's 3871 plus 1 pre-existing xfail, and O1's two strict xfails).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 livenote` (background, exit 0), whole: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-livenote-20261017-135258.log`. One SKIPPED, `:56` `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`; it does not name `COBALT_LIVE_VAULT_ROOT`.
- The eight launcher and hub files (E1): `uv run pytest -q tests/ops/test_shadow_hub_file.py … tests/ops/test_preflight.py` → `373 passed, 16 warnings in 173.44s (0:02:53)`.
- with-DB: not run (DB: none). cobalt_dev: not taken. `.env`: `ls /Users/cobalt/cobalt-wt/band-routing-1015/.env` → `No such file or directory` (never created).

## Scope
PREFLIGHT's path union (17 paths, all `ops/`, `tests/ops/`, `docs/`), plus the build's `.result` at `6c0ba560`, plus this check's one commit `3f399b60`: `tests/ops/test_band_routing_1015.py` (the rows' test file, 13 insertions). No row file is edited, and every mutation was undone (`git diff --stat 4b62c2fa -- <file>` → nothing, each; `git status --short --branch` → `## ops/band-routing-1015`).

## Checked against the branch
(i) `git log --oneline 4b62c2fa..HEAD -- . ":(exclude)docs"` → `3f399b60 wip(band-routing-1015): check red — O1 (strict xfail: HELD, NOT FIXED, desk-watch.sh fenced)`; tip now `3f399b60`. (ii) `git log --stat --format=%h 4b62c2fa..HEAD` → `3f399b60` `tests/ops/test_band_routing_1015.py | 13 +`; `6c0ba560` the two report files under `docs/`. (iii) `git log --oneline f2ca3e1a..HEAD -- ops/desk/desk-done.sh .claude/settings.json .claude/settings.json.bak src configs LAWS.md` → nothing. `git log --oneline 4b62c2fa..HEAD -- <desk-launch.sh, desk-watch.sh, preflight.sh, bare-guard.py, the prompts folder, the eight test files>` → nothing. (iv) `grep -n -F "def test_check_fr3_o1_a_routed_or_shadow_cards_check_closes_on_the_instructions_file" tests/ops/test_band_routing_1015.py` → `706:` one line; no fix commit (HELD, NOT FIXED). (v) `.env` → No such file; `git status --short --branch` → `## ops/band-routing-1015`. (vi) `git log --stat --format=%h f2ca3e1a..HEAD -- src/cobalt/db_migrations tests/cobalt` → nothing: no gate-list change needed. (vii) card RECORDS: `git log --oneline ops/band-routing-1015 -6` → `3f399b60` (this check), `6c0ba560`, `4b62c2fa`, `9bd05618`, `da95e8c7`, `8b142c56` (the record's five under this check's commit). Merge bases `f2ca3e1a` (PREFLIGHT), `7f415a4f`, `f2140694` (M1) match. `ls` of the fr9 report on main → `No such file or directory`, as recorded. `ops/gemini-builder-row-1017` head is now `8ba22eaf` (the record's `7b22e411` came before its fix round report); the three-file stat is the record's. `ops/gemini-probe-id-1017` head `9f281a6a`, as recorded. `git -C /Users/cobalt/cobalt log --oneline -3 -- ops/desk/stage-set.sh` → `b093f192` newest (the record's "not yet deployed" was 10:08; the dependency is now on main). (viii) L32: this report holds constructed test values and repo ids only.
COUNT: findings 1 (opus 1, Grok 0) · dropped 0 · held 1 · fixed 0 · held unfixed 1 · open 1.

## OPEN
- O1: HELD, NOT FIXED — ops/desk/desk-watch.sh. It is settled by a builder's fix in `desk-watch.sh` `unclean()` `:101` that adds the `check` of a routed or shadow card to the exception, by the rule `desk-launch.sh:1817` uses (`shadow` or `routed_tree` from the card), and that turns `tests/ops/test_band_routing_1015.py::test_check_fr3_o1_a_routed_or_shadow_cards_check_closes_on_the_instructions_file` (both cases) green with its strict xfail removed.
OUT OF SCOPE (records, by `## NOT IN THIS JOB`): `desk-watch.sh:2`, `:49` and the header `:16-23` do not name `routed` or the FR-9 exception. The M1 textual conflict is the later deploy's own fix round.

## CONTINUE
next: done

## DECISIONS
1. O1 HELD, NOT FIXED — ops/desk/desk-watch.sh. FR-9 closes the routed and shadow BUILD seats (proven: the 5 tests, the three mutations). But the CHECK of such a card runs in the same worktree, which still holds the untracked `SHADOW-INSTRUCTIONS.md`. The launcher (`desk-launch.sh:1817`), `preflight.sh:159` and CHECK-HUB `:64`/`:117` all accept the file for that check. The watcher's `check` kind (`desk-watch.sh:72`, `unclean()` `:101`) does not, so after `CHECK DONE` it prints `KEPT <id>: tree not clean` and never calls `desk-done.sh … check`. The run is in `## RUNS` (O1: red for routed and shadow, green with the file removed). Safe default taken: no edit of the fenced `desk-watch.sh`; the test is committed as a strict xfail (`3f399b60`); `ready: NO`. It goes to the original builder's one fix round on card 583 (his R438). The likely form: in `unclean()`, for kind `check`, derive shadow or routed from the card as `desk-launch.sh:1785-1796` does, and except the same one line. The desk decides whether the fix round widens FR-9's rows.
2. M1, for the desk's deploy sequencing (not this branch's to fix): `SHADOW-HUB.md` will conflict textually when 671 merges onto a main that carries 583. Both insert after the Terra note (583 `@@ -25,6 +25,15 @@`, 671 `@@ -9,24 +9,28 @@`), and 671 rewrites the `<pass prompt>` line right after 583's insert. `desk-launch.sh:374-379` is adjacent (two unchanged lines between the hunks) and may conflict. `bare-guard.py` is disjoint. 670 touches none of the three. Safe default: nothing resolved here; it falls on the second deploy (671), and that deploy's fix round resolves it.

## RECORDS
- No house list was dropped. House A Grok `FINDINGS: 0`. House B: none (not needed; `HOUSE B: as needed`). Gemini probe OUT: `error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS; card 670's id, X6).
- `<S>` was left by the earlier checks of this JOB (no `STAGED-CARD`). `stage-set.sh` cleared it by its legacy fallback (`cleared: … (prior check …/band-routing-check-fr2-2026-10-17.md)`) and wrote `STAGED-CARD`.
- `stage-set.sh` printed `commits 11` against PREFLIGHT's 16: the diff excludes `docs`, and the 5 other commits are docs-only (`## Files copied`).
- L74: the session's harness attribution reminder asked for a `Claude-Session:` trailer; recorded under `## L74`; not followed.
- No REFUSED call; no CONTINUE; no lock take (DB: none).
- The eight-file pin run and the offline gate ran at the same time on the same tip, after every mutation was undone (`git status` clean before both started).
- files opened: 12 — `CHECK-HUB.md`; the card `692-band-routing-fr3-check-card.md`; `ops/desk/desk-watch.sh`; `ops/desk/preflight.sh` (`:110-179`); `ops/desk/desk-launch.sh` (`:282-293`, `:986-1000`, `:1795-1824`); `tests/ops/test_band_routing_1015.py` (`:480-739`); `BUILD-HUB.md` (`:33-94`); the build report `band-routing-build-fr9-2026-10-17.md` (`:70-155`); `areas/cobalt.md` (`:21-65`); `band-routing-check-fr2-2026-10-17.md` (`:157-208`); `<S>/house-a.md`; `tests/ops/test_close_automation_1015.py` (`:125-154`). Plus the background task outputs (the house probe, Grok, the eight-file run, the two gate calls).
- Check of `band-routing-1015`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: band-routing-1015 · pass: 1 · tip: 3f399b60 · house A: grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 8439/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 12 · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 239385
