# band-routing-1015 — check after fix round 2 (FR-6 to FR-8), 2026-10-17

## §0 Headline
FR-6, FR-7 and FR-8 hold on the tip. Each shows its named red under a mutation that was undone afterwards, and its controls stay green. S0, E1, T1 and R3 hold. The suites are green: offline 8434/0, live-note 146/0.
House A Grok: `FINDINGS: 0`. House B: none (not needed). I found three things. O2 and O3 ran green, so they are NOT HELD.
O1 HELD, NOT FIXED. On a real routed gate-seat tree, `desk-watch.sh`'s close step reads the untracked `SHADOW-INSTRUCTIONS.md` as "tree not clean" and prints `KEPT`, so `desk-done.sh … build` never runs. The fix is in `desk-watch.sh`, which the card fences. It goes to the builder's fix round. ready: NO.

## L74
A system reminder in this session asked that commits end with a `Claude-Session:` line beside `Co-Authored-By`. Recorded once here as data (L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/666-band-routing-fr2-check-card.md"` (07:44:42 EDT):
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/666-band-routing-fr2-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/666-band-routing-fr2-check-card.md" · 0 · b5d62588f5960f3cbc1aa704a9e66aa5b737c7bd
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/666-band-routing-fr2-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → line 35, one row (standing `Bash(grok *)`); `grep -n "^| R19 " …cto-2026-09-24.md` → line 37, one row (the four house strings, indefinitely); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"`:
```
clock · date · 0 · Sat Oct 17 07:44:47 EDT 2026
status · git status --short --branch · 0 · ## ops/band-routing-1015
head · git log --oneline -1; git log --stat --format=%h fda2300b..HEAD · 0 · (6 lines)
    4fc9b9da docs(band-routing-1015): build report — fda2300b (fix round 2, FR-6 to FR-8)
    4fc9b9da
    
     .../reports/band-routing-build-fr6-2026-10-16.md   | 147 ++++++++++++++++++++-
     .../band-routing-build-fr6-2026-10-16.result       |  15 +++
     2 files changed, 159 insertions(+), 3 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/band-routing-1015/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/band-routing-1015/docs/40 - DevDocs/reports/band-routing-build-fr6-2026-10-16.md" · 0 · BUILT · job: band-routing-1015 · tip: fda2300b | on f2ca3e1a | migration: none | offline 8434/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 271499
range · git log --oneline f2ca3e1a..fda2300b · 0 · (11 lines)
    fda2300b fix(band-routing-1015): routed launch watched as kind routed on <job>-gate; card outside a dated folder refused; 429 clause cited as the brain's reading (FR-6 to FR-8, L1 L72)
    45b9d8c7 wip(band-routing-1015): fix round 2 red (FR-6 to FR-8)
    ac172ab9 wip(band-routing-1015): fix round 2 report opened (FR-6 to FR-8)
    7bf43c2b wip(band-routing-1015): check red — O1 O3 G1 (strict xfail: HELD, NOT FIXED, desk-launch.sh fenced)
    3ac61a2f docs(band-routing-1015): build report — c8c5ca90 (fix round FR-1 to FR-5)
    c8c5ca90 fix(band-routing-1015): card paths with /./ or // refused; routed card in CHECK-HUB, CARD.md check cell, SHADOW-HUB fix round and routed exception (FR-1 to FR-5, L1 L72)
    01b10bdd wip(band-routing-1015): fix round red (FR-1 to FR-5)
    ee21824d wip(band-routing-1015): check red — O2 (strict xfail: HELD, NOT FIXED, fix fenced to the builder)
    115e1f37 docs(band-routing-1015): build report — bd9c24ac
    bd9c24ac feat(band-routing-1015): BAND header, band table, launcher routing, routed check and result-file fence (B1-B6, L27 L29 L72)
    1be72d81 wip(band-routing-1015): red
PREFLIGHT OK
```
THE RANGE typed, `git log --stat --format=%h f2ca3e1a..fda2300b`: 11 commits; path union (DB: none, `git diff --name-only --no-renames f2ca3e1a..fda2300b`, quoted whole):
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
ops/desk/bare-guard.py
ops/desk/desk-launch.sh
ops/desk/desk-watch.sh
ops/desk/preflight.sh
tests/ops/test_band_routing_1015.py
tests/ops/test_check_hub_shadow.py
```
Every path under `ops/`, `tests/ops/` or `docs/`: DB: none holds.
`ls <S>` → `diff.md files house-a.md HOUSE-INSTRUCTIONS.md rulings.md` — present, but every file dated Oct 16 11:50–12:01 (`ls -la <S>`): the folder of the previous check of this job (same `<JOB>-check` name), not a recovery of this one (no `CONTINUE` in the launch message, no `CHECK REPORT` on disk). Treated as fresh; the stale `house-a.md` is not opened (see `## DECISIONS`).
House probe `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"`:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
house A: Grok · house B: none (not needed — the card's `HOUSE B: as needed`). Gemini OUT is a HARNESS record (X7), not a finding.
Write and with-DB strings: DB: none; no with-DB string is used.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → `cleared: <S> (prior check …/band-routing-check-fr1-r2-2026-10-16.md)`, then 19 lines (`63730 diff.md`, `28509 files/666-band-routing-fr2-check-card.md`, `24427 files/band-routing-build-fr6-2026-10-16.md`, `34998 files/wt/…/BUILD-HUB.md`, `20258 …/CARD.md`, `43727 …/CHECK-HUB.md`, `17407 …/SHADOW-HUB.md`, `25728 …/band-routing-build-2026-10-15.md`, `220 ….result`, `20584 …/band-routing-build-fr1-2026-10-16.md`, `220 ….result`, `1101 …/band-routing-build-fr6-2026-10-16.md` (as at `fda2300b`), `56410 …/bare-guard.py`, `136683 …/desk-launch.sh`, `12269 …/desk-watch.sh`, `11676 …/preflight.sh`, `37993 …/test_band_routing_1015.py`, `4899 …/test_check_hub_shadow.py`, `363 rulings.md`), last line `STAGED 19 files · 541202 bytes · commits 8`. The 8 are the non-docs commits of the 11 (the docs-only `ac172ab9`, `3ac61a2f`, `115e1f37` are excluded by `":(exclude)docs"`; brain decisions row 4 KEEP).
`stage-copy.sh`, each `COPIED <bytes> <dest>`: `79380 files/583-band-routing-card.md`, `40137 files/band-routing-check-fr1-r2-2026-10-16.md`, `301 ….result`, `4107 files/band-routing-check-fr1-decisions-2026-10-16.md`, `35110 files/band-routing-check-2026-10-16.md`, `4651 files/band-routing-answer-2026-10-16.md`, `1439 files/cto-2026-10-14-words.md`, `28538 files/cto-2026-10-15.md`, `7293 files/wt/ops/desk/desk-done.sh`, `37206 files/wt/ops/desk/deploy-card.sh`, `4347 files/645-draft-583-fr6.md`, `4252 files/646-draft-583-fr6-routed.md`, `4090 files/651-draft-583-fr6-closeout.md`, `23403 files/wt/tests/ops/test_desk_watch.py`, `20877 …/test_close_automation_1015.py`, `13261 …/test_desk_launch_shadow.py`, `76069 …/test_desk_launch_prechecks.py`, `12470 …/test_shadow_hub_file.py`. `HOUSE-INSTRUCTIONS.md` (29751 bytes) written: the HOUSE TEXT, the card's four sections, the Files paragraph.

## OWN FINDINGS
Written before any house list was opened.

FINDING O1
ROW: FR-6 (X1, X4)
CLAIM: a routed seat's worktree always holds the untracked `SHADOW-INSTRUCTIONS.md` (`docs/40 - DevDocs/prompts/SHADOW-HUB.md:55` "never committed"; not in `.gitignore`), and `ops/desk/desk-watch.sh:99` `unclean()` reads any `git status --short` output as "tree not clean", so the routed closeout of `:153` never reaches `desk-done.sh … build` on a real routed worktree; FR-6's closeout test (`tests/ops/test_band_routing_1015.py:570`) runs on a tree without that file.
RUN: TEST — tests/ops/test_band_routing_1015.py
```python
def test_check_o1_a_routed_closeout_on_a_gate_seat_tree_hands_build_to_desk_done(tmp_path):
    w = RWatch(tmp_path / "w", done=True, last=ROUTED_STOP)
    (w.wt / "SHADOW-INSTRUCTIONS.md").write_text("constructed\n")
    w.rows(IDLE_GATE)
    done = w.run("routed")
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines()[0] == ROUTED_STOP, done.stdout
    assert w.logged() == [f"sess-x01 {w.report} build"], done.stdout
```
EXPECT: `assert [] == ['sess-x01 … build']`, stdout ending `KEPT sess-x01: tree not clean`.

FINDING O2
ROW: FR-6 (X1)
CLAIM: the Terra backup is the desk's hand launch `shadow <card> --model gpt-5.6-terra --routed` (`ops/desk/desk-launch.sh:393`, `:1674-1686`); its WATCH line (`:2356`) is pinned by no test (`test_b3_the_backup_is_a_hand_launch`, `tests/ops/test_band_routing_1015.py:335`, reads no WATCH line).
RUN: TEST — tests/ops/test_band_routing_1015.py
```python
def test_check_o2_the_backup_hand_launch_is_watched_as_routed(desk):
    card = desk.card_for("MID")
    done = desk.run("shadow", str(card), "--model", "gpt-5.6-terra", "--routed")
    assert done.returncode == 0, done.stderr
    assert [ln for ln in done.stderr.splitlines() if ln.startswith("WATCH:")] == [
        f'WATCH: sh {desk.launch.parent}/desk-watch.sh routed "{card}"']
```
EXPECT: if the claim of a gap is true in behaviour, the WATCH line differs; a pin probe (expected green if `:2356` holds for the hand launch).

FINDING O3
ROW: FR-7 (X2)
CLAIM: FR-7 (i) says the three odd paths are refused by `build`, `check` and `shadow`; `test_fr7_a_card_outside_a_date_folder_is_refused_naming_it` (`tests/ops/test_band_routing_1015.py:607`) runs `build` only; the `check` and `shadow` (`--routed`) entries to `ops/desk/desk-launch.sh:990-995` are pinned by no test.
RUN: TEST — tests/ops/test_band_routing_1015.py
```python
@pytest.mark.parametrize("kind", ["check", "shadow"])
@pytest.mark.parametrize("where", ["01-x-band-card.md", "drafts/01-x-band-card.md",
                                   f"{NEW_DAY}/sub/01-x-band-card.md"])
def test_check_o3_check_and_shadow_refuse_a_card_outside_a_date_folder(desk, kind, where):
    (desk.prompts / "CHECK-HUB.md").write_text("# CHECK-HUB (constructed, installed)\n\nconstructed\n")
    card = desk.card_for("LOW")
    odd = desk.prompts / where
    odd.parent.mkdir(parents=True, exist_ok=True)
    odd.write_text(card.read_text())
    desk.commit("odd card")
    args = ("shadow", str(odd), "--model", "grok-4.7", "--routed") if kind == "shadow" else ("check", str(odd))
    done = desk.run(*args, dry=False)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: the card must be" in done.stderr, done.stderr
    assert str(odd) in done.stderr, done.stderr
    assert not desk.calls.exists()
```
EXPECT: a pin probe: green if the first card `case` binds every kind; a red names the kind that slips past it.

Records of my read (not findings): `test_x5_routed_build_watch_does_not_wait_on_built` (`:419-423`) passes on an empty WATCH list (the list comprehension compares a list with its own filter); the WATCH line itself is pinned by `test_fr6_the_routed_watcher_admits_built_and_watches_the_gate_session` (`:549`). A routed FAILED is `KEPT … until CONTINUE` (`desk-watch.sh:116`) while a routed build refuses a resume step (`desk-launch.sh:1663`): a message CONTINUE only, B3's design, not this round's.

## Findings
House A Grok (`grok-4.7`), started 07:47:55 EDT, notice 08:00:17 EDT; `<S>/house-a.md` (12 bytes, 08:00) reads whole: `FINDINGS: 0`. Its stdout: `…The tip matches the three fix rows: the watch line, the dated-card refusal, and the citation. No failing check to hand off./Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/band-routing-1015-check/house-a.md` · `[exited with code 0]`. House B: none (not needed).
- O1 · opus · FR-6 (X1, X4) · routed closeout KEPT `tree not clean` on a real gate-seat tree (untracked `SHADOW-INSTRUCTIONS.md`); never reaches `desk-done.sh … build` · TEST
- O2 · opus · FR-6 (X1) · the Terra backup hand launch's WATCH line pinned by no test · TEST
- O3 · opus · FR-7 (X2) · `check` and `shadow` entries to the dated-folder gate pinned by no test · TEST

## Dropped
none (Grok wrote no block; mine all carry a test)

## RUNS
### The card's rows (each a RUN; every mutation undone with the Edit tool and the undo proved)
- S0 · `git diff --name-only --no-renames 7bf43c2b fda2300b` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `docs/40 - DevDocs/reports/band-routing-build-fr6-2026-10-16.md`, `ops/desk/desk-launch.sh`, `ops/desk/desk-watch.sh`, `tests/ops/test_band_routing_1015.py` (exactly the five) · `git diff --stat fda2300b 4fc9b9da -- . ":(exclude)docs"` → nothing · `git diff --name-only --no-renames f2ca3e1a..fda2300b` → the 15 paths quoted under PREFLIGHT (no `src/`, `configs/`, `.claude/`; `ops/desk/desk-done.sh` absent; `git log --oneline f2ca3e1a..fda2300b -- ops/desk/desk-done.sh` → nothing) · `git diff ac172ab9 fda2300b -- ops/desk/desk-watch.sh` → three hunks, one changed line each: `+  routed) report=$(header REPORT) || exit 1; re='^(BUILT ·|FAILED)' ;;`, `+  routed) job=$(header JOB) || exit 1; wt=$(header WORKTREE) || exit 1; session="$job-gate" ;;`, and `-    out=$(sh "$here/desk-done.sh" "$rid" "$report" "$kind")` → `+    out=$(sh "$here/desk-done.sh" "$rid" "$report" "$([ "$kind" = routed ] && echo build || echo "$kind")")` · `git diff --stat 45b9d8c7 fda2300b -- ops/desk/desk-launch.sh` → `1 file changed, 5 insertions(+), 3 deletions(-)`: two hunks, the first card `case` (`@@ -988,8 +988,10 @@`) and the `watch=` line (`@@ -2351,7 +2353,7 @@`), no other tail hunk · `git diff --stat 7bf43c2b fda2300b -- "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` → `1 file changed, 1 insertion(+), 1 deletion(-)` (`:28`) · `git status --short --branch` → `## ops/band-routing-1015`.
- FR-6 · read: `desk-launch.sh:379` `routed=""`, `:393-394` `--routed) routed=1` inside the `shadow` argument loop only; `:1669` a LOW/MID `build` re-enters as `exec sh "$0" shadow "$card" --model "$bid" --routed`; `:2356` the `watch=` line; the other `watch_line` caller `:546` (`close`) unchanged. `desk-watch.sh:65` regex `^(BUILT ·|FAILED)` (admits `BUILT ·`, `FAILED`; `SHADOW BUILT` does not start `BUILT`), `:74` session `$job-gate`, `:153` the mapping. `desk-done.sh:47` `build) done_re='^BUILT'`, `:54` `shadow) … kind=build`, `:61-63` a FAILED build is refused (kept for CONTINUE). `test_x5_…` hunk of `git diff 7bf43c2b fda2300b -- tests/ops/test_band_routing_1015.py`: `-    assert watch == [ln for ln in watch if "desk-watch.sh build " in ln], watch` / `+    assert watch == [ln for ln in watch if "desk-watch.sh routed " in ln], watch` plus the decorator line removed; `test_o1_…` loses its decorator only. `grep -n -F -e "xfail" -e "runxfail" tests/ops/test_band_routing_1015.py` → nothing.
  GREEN on the tip (T1 run below): `PASSED …::test_o1_a_routed_builds_watch_line_waits_on_the_build_stop_line`, `…::test_x5_routed_build_watch_does_not_wait_on_built`, `…::test_fr6_the_routed_watcher_admits_built_and_watches_the_gate_session`, `…::test_fr6_a_routed_closeout_hands_build_to_desk_done`, `…::test_fr6_control_a_shadow_card_closeout_still_passes_shadow`, `…::test_fr6_control_a_high_card_and_a_real_shadow_keep_their_watch` (the HIGH `build` → `desk-watch.sh build`, the real shadow → `desk-watch.sh shadow`, asserted whole). The `check`/`deploy`/`devfix` WATCH lines: `test_desk_watch.py`, `test_close_automation_1015.py`, `test_desk_launch_shadow.py` inside the eight-file run, `373 passed`.
  (a) `:2356` back to `watch=$(watch_line "$kind" "$card")` → `3 failed, 3 passed`: `test_o1_…` `assert 'desk-watch.sh shadow ' not in …` (printed `WATCH: sh …/desk-watch.sh shadow "…/2026-10-16/01-x-band-card.md"`), `test_x5_…` `assert ['WATCH: sh /...and-card.md"'] == []`, `test_fr6_the_routed_watcher…` `assert 'desk-watch.sh routed "…"' in …`; the controls passed. Undone: `git diff --stat fda2300b -- ops/desk/desk-launch.sh` → nothing.
  (b) the two `routed` arms removed → `2 failed, 2 passed`, both `AssertionError: REFUSED: unknown kind: routed` (the parent's reason, the builder's DECISION FR-6). (b') the arms kept, regex set to `^(SHADOW BUILT|SHADOW ROLE|FAILED)` and session to `$job-build` → `2 failed, 2 passed`, both `assert 3 == 0` with stdout `GONE: x-job-build\n# x-job build\nbody\nBUILT · job: x · tip: tip-x | on base-x | rows: 1 of 1` (the card's named reason: the gate session not watched, `BUILT ·` not matched); controls passed. Undone: `git diff --stat fda2300b -- ops/desk/desk-watch.sh` → nothing.
  (c) `:153` back to `"$kind"` → `1 failed, 3 passed`: `test_fr6_a_routed_closeout_hands_build_to_desk_done` `assert ['sess-x01 /p...ld.md routed'] == ['sess-x01 /p...ild.md build']`. Undone: `git diff --stat fda2300b -- ops/desk/desk-watch.sh` → nothing.
  The usage line `desk-watch.sh:2` and `:49` name no `routed`: a record (fenced), not a finding.
- FR-7 · read: `desk-launch.sh:971-979` every kind of the fixed-file `case` (build, check, deploy, recut, devfix, shadow, prodwrite) reaches `:990`; `:991` pass-through, `:992` deep path refused, `:993` the date arm, `:994` the closing refusal; the FR-1 arm is `:999`. Mutation 1, the first `case` back to the parent's `"$PROMPTS"/*-card.md) ;;` / `*) refuse "the card must be $PROMPTS/<date>/<nn>-<job>-card.md" ;;` → `4 failed, 1 passed`: `test_o3_…` `assert 0 == 1` (printed the Opus `BUILD-HUB.md` line, `desk-watch.sh build`), `test_fr7_…[01-x-band-card.md]` and `[drafts/01-x-band-card.md]` `assert 0 == 1` (the Opus line), `[2026-10-16/sub/01-x-band-card.md]` `assert 0 == 1` with `BAND: LOW → grok-4.7 (backup gpt-5.6-terra)` and the gate seat `--remote-control x-band-gate` launched; the control `test_fr7_control_a_dated_card_still_launches` passed. Mutation 2, the pass-through line alone removed → `2 failed, 5 passed`: `test_o2_…` and `test_fr1_…` read `REFUSED: the card must be …/prompts/<YYYY-MM-DD>/<nn>-<job>-card.md: …/prompts/./2026-10-16/01-x-band-card.md` (and `…prompts//2026-10-16/…`) in place of `the card path holds '/./' or '//'`. Undone: `git diff --stat fda2300b -- ops/desk/desk-launch.sh` → nothing. Survey (main repo, Glob): `docs/40 - DevDocs/prompts/*-card.md` → No files found; `docs/40 - DevDocs/prompts/*/*/**/*-card.md` → No files found; `ls "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts"` → 31 dated folders `2026-09-15` … `2026-10-16` and hub files only (no non-date folder). Desk callers: `Grep "-card\.md|PROMPTS"` over `ops/desk/` (desk-launch.sh aside) → `deploy-step-c.sh:105` admits `prompts/[A-Za-z0-9._/-]+-card.md` (a deploy row reference, not a launch path), `deploy-shipped.sh:65-69` refuses a path outside `$PROMPTS`, `desk-wake.sh:129` lists `$PROMPTS/<today>/`; none builds a card path outside a dated folder. Every live card in the open pipeline (this card 666) sits in `prompts/2026-10-16/`.
- FR-8 · `git diff 7bf43c2b fda2300b -- "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` → one hunk `@@ -25,7 +25,7 @@`, one line: `(R1532: Terra backup; 2026-10-14 item 7: a 429 is retried, never a backup)` → `(brain 2026-10-16, reading R1532's 'Terra backup': a backup is for a probe OUT or a harness FAILED; a 429 is recorded and retried, never a backup, as the Grok-cap removal of 2026-10-14 R1471 (7) is recorded in the direction file)`. Sources: `reports/cto-2026-10-14-words.md:9` `Relayed by the brain (quoted): "I want all, including 5, and I want to remove Grok's limit of 3." Items: … (7) Grok cap of 3 removed; …`; `reports/cto-2026-10-15.md:102` `LOW/MID Grok 4.7 + Terra backup`; `reports/band-routing-check-fr1-decisions-2026-10-16.md:11` the clause byte for byte as the hub has it. No word of the clause is presented as his: "a backup is for a probe OUT or a harness FAILED" and "a 429 is recorded and retried, never a backup" are the brain's reading, and the clause names itself so. `Grep "item 7"` over the worktree's `docs/40 - DevDocs/prompts` → no hit in `BUILD-HUB.md`, `CHECK-HUB.md`, `SHADOW-HUB.md` or `CARD.md` (the hits are dated cards). Card 583 on main: `grep -n -o -F -e "R1471 item 7" -e "(brain 2026-10-16, reading R1532's 'Terra backup'"` → `:22` `R1471 item 7` (the amend's own history sentence: "the words … that cited R1471 item 7 (those two are re-worded by this amend)"), and the citation at `:43`, `:55` (×3), `:70`; the card is the desk's, not edited. Mutation: `:28`'s clause restored to the parent's → `2 failed, 2 passed`: `test_fr4_…` and `test_fr8_…` `AssertionError: brain 2026-10-16, reading R1532's 'Terra backup'`; `test_fr8_control_…` and `test_fr4_control_…` passed. Undone: `git diff --stat fda2300b -- "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` → nothing. `test_shadow_hub_file.py` inside the eight-file run (`373 passed`).
- E1 · `grep -c -F "on a shadow card or a routed card (BAND LOW or MID, dated on or after BAND_FROM)" CHECK-HUB.md` → `2`; `tests/ops/test_check_hub_shadow.py` → `5 passed`; `grep -c -F "BAND" CARD.md` → `2`; `CARD.md:23` holds `required when the build card carries BAND: LOW or MID (copied from it); optional otherwise`; `desk-launch.sh:1645` `BAND_FROM=20261016`, `:1654` `band_row()`; `git diff f2ca3e1a fda2300b -- BUILD-HUB.md` → one added paragraph `BAND (his 2026-10-15 R1532): …`, the `claude --bg` line unchanged; SHADOW-HUB `:53`, `:70` each hold `(a routed card: no `SHADOW OF`; stop line `BUILT ·` as `:28`)` (`test_fr5_…` PASSED). The band-routing file: `61 passed` (no xfailed); PASSED lines of every `test_b*`, `test_fr*_control_*`, `test_*_control_*` as quoted in the T1 run. Routed path end to end (X4): hub stop line `BUILT ·` (`SHADOW-HUB.md:28`, `:70`) → watcher `routed` on `<job>-gate` admitting `^(BUILT ·|FAILED)` → closeout `build` → `preflight.sh:273` (`BUILT · job: … self-check:`) and `deploy-card.sh:264`, `:536` (`BUILT ·`) read the same line: consistent, except the close step O1 shows (KEPT on the untracked `SHADOW-INSTRUCTIONS.md`).
- T1 · `uv run pytest -q -rA -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py` → `61 passed, 15 warnings in 15.17s` (no xfailed); the eight files → `373 passed, 16 warnings in 175.23s (0:02:55)`; `git diff --stat 7bf43c2b fda2300b -- <the eight files>` → nothing; `grep -n -E -e "git show" -e "subprocess" -e "[0-9a-f]{8}" tests/ops/test_band_routing_1015.py` → `18:import subprocess`, `195`, `272`, `274`, `285`, `539`, `540`, `710`, `712`, `715`, `717`, `761`, `807`, `813` (each `subprocess` use on a tmp desk); no `git show`, no 8-hex hash.
- R3 · `uv run cobalt jobs restarts 7bf43c2b..fda2300b` → `SHADOW-HUB.md M DOCS -` · `band-routing-build-fr6-2026-10-16.md A DOCS -` · `ops/desk/desk-launch.sh M operator script; no Cobalt reader -` · `ops/desk/desk-watch.sh M operator script; no Cobalt reader -` · `tests/ops/test_band_routing_1015.py M test/documentation; no resident -` · `RESTARTS: none`. `… f2ca3e1a..fda2300b` → the 15 paths, DOCS / operator script / test rules, `RESTARTS: none`. Header `RESTARTS: none` holds.
- D1 · FR-6: confirmed; the parent's red is `unknown kind: routed` (mutation (b)); the card's named reasons show under (a), (b') and (c). Keep. FR-7: the pass-through is needed (mutation 2 turns FR-1's named refusal into the generic one) and the deep-path arm is needed because a `case` `*` matches `/` (mutation 1's `sub/` case launches); three arms is the smallest form that keeps both texts; it refuses no real path (survey above). Keep. FR-7-survey: re-run on main by Glob and `ls`, none outside a dated folder. Keep.
- G1 · see `## Suites`.

### The findings
- O1 · opus · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py::test_check_o1_a_routed_closeout_on_a_gate_seat_tree_hands_build_to_desk_done` · `1 failed`: `AssertionError: BUILT · job: x · tip: tip-x | on base-x | rows: 1 of 1 / KEPT sess-x01: tree not clean` · `assert [] == ['sess-x01 /p...ild.md build']` · HELD, NOT FIXED — ops/desk/desk-watch.sh (the fix is `unclean()`, `desk-watch.sh:97-108`, outside FR-6's three lines; `## NOT IN THIS JOB` fences any edit of `desk-watch.sh`). Committed as a strict xfail (the earlier checks' form, brain decisions row 5 KEEP; the assertion unchanged): `8b142c56`; with it the file reads `61 passed, 1 xfailed`, `XFAIL …::test_check_o1_… - check fr2 O1: HELD, NOT FIXED — ops/desk/desk-watch.sh (fenced)`. By the code, the same `unclean()` (`:123-126`) runs for kind `shadow`: a shadow seat's tree carries the same file, so the shadow closeout is KEPT the same way (card 580 C2's rule, not this branch's).
- O2 · opus · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py::test_check_o2_the_backup_hand_launch_is_watched_as_routed` · `1 passed` · NOT HELD (the backup hand launch prints `desk-watch.sh routed "<card>"`); test removed with the Edit tool.
- O3 · opus · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py -k test_check_o3_` · `6 passed, 63 deselected` · NOT HELD (check and shadow refuse all three paths, naming them, no `claude` call); tests removed with the Edit tool.

## FIXES
- O1: HELD, NOT FIXED — ops/desk/desk-watch.sh (fenced by `## NOT IN THIS JOB`; it goes to the original builder's one fix round, `## DECISIONS`)
No `fix(band-routing-1015):` commit; no DevDocs line (no module changed).

## Suites
On the tip `8b142c56` (DB: none; W (a0), (a), (e)):
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 offline --deploy-gate` → `tests/ops: run (deploy gate)` · `offline 8434/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-offline-20261017-080138.log` · exit 0. In the log: `4568 passed, 806 skipped, 1 xfailed, 36 warnings in 711.28s (0:11:51)` and the tests/ops pass `3866 passed, 2 xfailed, 16 warnings in 895.24s (0:14:55)` (the pre-existing xfail plus O1's strict xfail).
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-livenote-20261017-082914.log` · exit 0.
- with-DB: not run (DB: none). cobalt_dev: not taken. `.env`: `ls /Users/cobalt/cobalt-wt/band-routing-1015/.env` → `No such file or directory` (never created).
- RESTARTS: `uv run cobalt jobs restarts f2ca3e1a..8b142c56` → the 16 paths DOCS / operator script / test rules, `RESTARTS: none`.

## Scope
PREFLIGHT's path union (15 paths, all `ops/`, `tests/ops/`, `docs/`) plus the check's one commit `8b142c56`: `tests/ops/test_band_routing_1015.py` (the card's rows' test file). No row file edited; every mutation undone (`git diff --stat fda2300b -- <file>` → nothing, each).

## Checked against the branch
(i) `git log --oneline fda2300b..HEAD -- . ":(exclude)docs"` → `8b142c56 wip(band-routing-1015): check red — O1 (strict xfail: HELD, NOT FIXED, desk-watch.sh fenced)`; tip now `8b142c56`. (ii) `git log --stat --format=%h fda2300b..HEAD` → `8b142c56` `tests/ops/test_band_routing_1015.py | 11 +++`; `4fc9b9da` the two report files under `docs/`. (iii) `git log --oneline f2ca3e1a..HEAD -- ops/desk/desk-done.sh .claude/settings.json .claude/settings.json.bak src configs` → nothing. (iv) `grep -n -F "def test_check_o1_a_routed_closeout_on_a_gate_seat_tree_hands_build_to_desk_done" tests/ops/test_band_routing_1015.py` → `650:` one line; no fix commit (HELD, NOT FIXED). (v) `.env` → No such file; `git status --short --branch` → `## ops/band-routing-1015`. (vi) `git log --stat --format=%h f2ca3e1a..HEAD -- src/cobalt/db_migrations tests/cobalt` → nothing: no gate-list change needed. (vii) card RECORDS: `git log --oneline -4 ops/band-routing-1015` → `8b142c56`, `4fc9b9da`, `fda2300b`, `45b9d8c7` (the record's four plus this check's commit on top; `ac172ab9` now fifth); main HEAD now `f2140694` (`git -C /Users/cobalt/cobalt log --oneline -1`; the record's `d8bdf960` was the drafter's time). (viii) L32: this report holds constructed test values and repo ids only.
COUNT: findings 3 (opus 3, Grok 0) · dropped 0 · held 1 · fixed 0 · held unfixed 1 · open 1.

## OPEN
- O1: HELD, NOT FIXED — ops/desk/desk-watch.sh. Settled by a builder's fix in `desk-watch.sh` `unclean()` (or by the seat's tree carrying no untracked file at its stop line) that turns `tests/ops/test_band_routing_1015.py::test_check_o1_a_routed_closeout_on_a_gate_seat_tree_hands_build_to_desk_done` green with its strict xfail removed.
OUT OF SCOPE (records): `desk-watch.sh:2`, `:49` name no `routed` (`## NOT IN THIS JOB`); the shadow closeout is KEPT on the same file by the same `unclean()` (card 580 C2's code, not this branch's); `test_x5_…` passes on an empty WATCH list (the routed WATCH line is pinned by `test_fr6_the_routed_watcher…`).

## CONTINUE
next: done

## DECISIONS
1. O1 HELD, NOT FIXED — ops/desk/desk-watch.sh. A routed gate seat leaves the untracked `SHADOW-INSTRUCTIONS.md` at the worktree root (`SHADOW-HUB.md:55` "never committed"; not in `.gitignore`), and `desk-watch.sh:97-108` `unclean()` reads any `git status --short` line as "tree not clean". After the routed stop line, then, the watcher prints `KEPT <id>: tree not clean` after its close-wait and never calls `desk-done.sh … build`. The run is in `## RUNS` (O1). FR-6's own closeout test runs on a tree without the file. The desk does see the stop line (printed, exit 0), but the worker is not closed automatically, the gap the brain's row 1 named for the interim. By the code the shadow kind behaves the same. Safe default taken: no edit of the fenced `desk-watch.sh`; the test is committed as a strict xfail (`8b142c56`); `ready: NO`. It goes to the original builder's one fix round on card 583 (his R438). The likely form: `unclean()` excepts the one `?? SHADOW-INSTRUCTIONS.md` line for kinds `shadow` and `routed`, as `preflight.sh:159` and `desk-launch.sh:1817` already do. That would also change the shadow close, so the desk decides whether it widens `files`.
Recommendations on the builder's decisions (D1, X6): keep FR-6, FR-7 and FR-7-survey as built (`## RUNS` D1).

## RECORDS
- `<S>` held the previous check's files (2026-10-16 11:50–12:01) at the start; this launch carried no `CONTINUE`, so the run was fresh. `stage-set.sh` cleared the folder (`cleared: …`) before staging, and the old `house-a.md` was never opened.
- Gemini probe: `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS; X7, the K5 card pending); not seated (house B not needed).
- Grok produced a list: `FINDINGS: 0`.
- L74: one system reminder asked for a `Claude-Session:` commit line; recorded under `## L74`, not acted on.
- No lock take; no `.env`; no `REFUSED, not needed`; no `CONTINUED`.
- Not read, from WHAT YOU READ: the `BUILD-HUB.md` sections (beyond the grep of its stop line and its diff), the build report's sections, and `areas/cobalt.md`. The rows' runs did not need them; the gate scripts carry W.
- files opened: 16 — CHECK-HUB.md, card 666, the house-probe output, desk-watch.sh, desk-done.sh, desk-launch.sh (three ranges), test_band_routing_1015.py (two ranges), preflight.sh, SHADOW-HUB.md, band-routing-check-fr1-decisions-2026-10-16.md, cto-2026-10-14-words.md, card 583 (one line), the Grok task output, house-a.md, the two gate outputs.
- Check of `band-routing-1015`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: band-routing-1015 · pass: 1 · tip: 8b142c56 · house A: grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 8434/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 16 · ready: NO · decisions: 1 · for Dejan: 0 · tokens: 246068
