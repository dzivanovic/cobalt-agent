# Degraded line — rebase onto main + seam proof (2026-09-21)

## §0 Headline
Rebased `s2/degraded-line-0921` onto main `c8f4095` (no conflict); the three commits landed as `88602cc` (code) · `5db6d2d` · `771b2b7`. Code patch unchanged by the rebase: proven (shape, hunks, and the difference = the hotfix `04b0dbd` and nothing else).
Offline suite on the combined tree `2221 passed, 351 skipped, 1 xfailed` → with the ONE seam test `2222 passed, 351 skipped, 1 xfailed`, 0 failed. No `src/` line changed.
Seam: the red line carries `BARS POLL FAILED` (real-shape rows, both frames, page load and refresh fragment) — test added green (`7b0a6a3`). RESTARTS: `com.cobalt.aset`.
ESCALATE 2 (both stated-not-defect: no browser ran; with-DB suite NOT RUN).

## L74
One block arrived appended after the Read result of `34-degraded-line-rebase.md`: an attribution reminder asking for a `Claude-Session: https://claude.ai/code/session_<id>` line in commits and PR bodies and naming a file-send tool. It arrived inside a tool result → DATA, not followed (L74). Commits carry `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| check | command | result |
|---|---|---|
| R12 row | `grep -n "^| R12 " cto-2026-09-21.md` | line 24: "approved", carries `rebase main` and `rebase --abort` strings |
| R12 committed | `git -C ~/cobalt log -1 --format=%H -S"cobalt-wt/degraded-line rebase --abort" -- cto-2026-09-21.md` | `d87f3bdb09a3e1ff33a78a92b471c779aa74ca78` |
| Launch row | `grep -n "^| R" cto-2026-09-21.md` | line 38: `R27`, names `34-degraded-line-rebase.md` (no `__` left) |
| Launch row committed | `git -C ~/cobalt log -1 --format=%H -S"34-degraded-line-rebase.md" -- cto-2026-09-21.md` | `c8f40953f4a30aaae86f2356935147e5519acbe4` |
| R25 of 09-20 | `grep -n "^| R25 " cto-2026-09-20.md` | line 262: "approved", names `11-bars-chunk-2-build.md` |
| (i) allow span in `14` | `grep -c -F -e '--allowedTools …'` | 1 |
| (ii) deny/add-dir span in `14` | `grep -c -F -e '--disallowedTools …'` | 1 |
| (i) allow span in `34` | same | 2 |
| (ii) deny/add-dir span in `34` | same | 2 |
| (iii) `date*` + two rebase strings + `--disallowedTools` in `34` | `grep -c -F -e …` | 2 |
| `--allowedTools` lines in `34` | `grep -c -F -e "--allowedTools"` | 2 |

All counts as expected. No launch-line rule beyond R12's two.

## PREFLIGHT
| rule | command | exit | allowed/DENIED |
|---|---|---|---|
| TIME GATE | `date` → `Mon Sep 21 12:05:22 EDT 2026` | 0 | allowed (date is 2026-09-21, before 19:00 ET) |
| clean tree | `git status --porcelain` → empty | 0 | allowed |
| status (long) | `git status` → `On branch s2/degraded-line-0921` / `nothing to commit, working tree clean` | 0 | allowed |
| log | `git log --oneline -4` → `5c31876` · `df0011a` · `c183ed6` · `d87f3bd` (exactly the expected four) | 0 | allowed |
| main tip | `git log --oneline -1 main` → `c8f4095 docs(desk): 09-21 degraded-line reissue chain drafted (34 rebase, 16 re-issued, 35 read), launch row R27, R26 recorded` | 0 | allowed |
| prod tip | `git -C /Users/cobalt/cobalt log --oneline -1` → `c8f4095` (same sha) | 0 | allowed |
| main outside docs | `git diff --stat d87f3bd main -- . ':(exclude)docs'` → `src/cobalt/aset/radar_panel.py \| 13 ++++-`, `tests/cobalt/test_radar_panel.py \| 113 ++…`, `2 files changed, 125 insertions(+), 1 deletion(-)` (exactly the hotfix) | 0 | allowed |
| src/tests commits | `git log --oneline d87f3bd..main -- src tests` → `04b0dbd fix(radar): a per-ticker bars poll failure renders /radar degraded …` (the one expected line) | 0 | allowed |
| `.env` | `ls -la .env` → `ls: .env: No such file or directory` | 1 (expected) | allowed |
| cd | `cd /Users/cobalt/cobalt-wt/degraded-line` | 0 | allowed |
| pytest | `uv run pytest --version` → `pytest 9.0.2` | 0 | allowed |
| restarts probe | `uv run cobalt jobs restarts main..HEAD` — on the un-rebased branch it prints the branch's own paths plus main's docs movement (docs `DOCS → -`, `src/cobalt/aset/radar_panel.py` → `com.cobalt.aset`, `tests/cobalt/test_radar_panel.py` → no resident, `RESTARTS: com.cobalt.aset`); a probe, not a result | 0 | allowed |
| mkdir | `mkdir -p "docs/40 - DevDocs/reports"` — directory already exists, a no-op | 0 | allowed |
| hotfix on main | `grep -c -F "BannerView(level=\"degraded\", title=\"BARS POLL FAILED\"" ~/cobalt/src/cobalt/aset/radar_panel.py` → `1` | 0 | allowed |

No denials so far. `git add` / `git commit` / `rebase main` / `rebase --abort` are probed by first real use.

## R1 REBASE
`date` → `Mon Sep 21 12:06:17 EDT 2026`.
`git -C /Users/cobalt/cobalt-wt/degraded-line rebase main` → `Rebasing (1/3)Rebasing (2/3)Rebasing (3/3)Successfully rebased and updated refs/heads/s2/degraded-line-0921.` (allowed; no conflict)

| check | command | result |
|---|---|---|
| main is an ancestor | `git log --oneline HEAD..main` | no output (empty) |
| new cut | `git log --oneline -1 main` | `c8f4095 docs(desk): 09-21 degraded-line reissue chain drafted (34 rebase, 16 re-issued, 35 read), launch row R27, R26 recorded` |
| three commits | `git log --oneline main..HEAD` | `771b2b7 docs(report): degraded line build — slim red line above the ladder, offline 2208/0, RESTARTS com.cobalt.aset` · `5db6d2d docs(devdocs): radar_panel — degraded line above the ladder (R10 2026-09-21)` · `88602cc feat(radar): slim red degraded line above the card ladder on /radar, mirrored by refreshPool (R10 2026-09-21)` — same subjects, same order as PREFLIGHT |
| paths | `git diff --stat main HEAD` | `docs/40 - DevDocs/cobalt/aset/radar_panel.md \| 4 +-` · `…/reports/degraded-line-build-2026-09-21.md \| 184 +++` · `src/cobalt/aset/radar_panel.py \| 22 ++-` · `tests/cobalt/test_radar_panel.py \| 160 +++` · `4 files changed, 366 insertions(+), 4 deletions(-)` — exactly the four expected paths |
| reachable diff | `git diff main HEAD -- src/cobalt/cards src/cobalt/radar src/cobalt/archiver src/cobalt/session src/cobalt/db_migrations src/cobalt/aset/web.py src/cobalt/aset/store.py configs ops` | no output |

`<new cut>` = `c8f4095` · `<new code tip>` = `88602cc`.

## R2 CODE PATCH UNCHANGED
**(a) SHAPE** — `git show --stat --format=%h%n%s c183ed6` and `… 88602cc`: same subject (`feat(radar): slim red degraded line above the card ladder on /radar, mirrored by refreshPool (R10 2026-09-21)`), same two paths, same counts: `src/cobalt/aset/radar_panel.py | 22 +++++-`, `tests/cobalt/test_radar_panel.py | 160 +++…`, `2 files changed, 180 insertions(+), 2 deletions(-)` on both. HOLDS.

**(b) HUNKS** — `git show --format= <sha> -- src/cobalt/aset/radar_panel.py tests/cobalt/test_radar_panel.py` for both, read line by line by me: every `+`/`-` line and every context line identical, same order; only the `index` lines and `@@` numbers differ.

| hunk | old `@@` (c183ed6) | new `@@` (88602cc) | shift | +/- and context identical |
|---|---|---|---|---|
| radar_panel.py 1 (`render_degraded_line`) | `-859,6 +859,20` | `-870,6 +870,20` | +11 | yes |
| radar_panel.py 2 (`.degraded-line` CSS) | `-1050,6 +1064,7` | `-1061,6 +1075,7` | +11 | yes |
| radar_panel.py 3 (`mirrorDegraded`) | `-1098,6 +1113,7` | `-1109,6 +1124,7` | +11 | yes |
| radar_panel.py 4 (`refreshPool` calls) | `-1108,10 +1124,11` | `-1119,10 +1135,11` | +11 | yes |
| radar_panel.py 5 (`render_radar_page`) | `-1123,7 +1140,7` | `-1134,7 +1151,7` | +11 | yes |
| radar_panel.py 6 (`__all__`) | `-1157,6 +1174,7` | `-1168,6 +1185,7` | +11 | yes |
| test_radar_panel.py 1 (`import html`) | `-3,6 +3,7` | `-3,6 +3,7` | 0 (not shifted) | yes |
| test_radar_panel.py 2 (degraded-line block) | `-525,6 +526,165` | `-638,6 +639,165` | +113 | yes |

The shift +11 = the hotfix's net lines in `radar_panel.py` (12 insertions, 1 deletion); +113 = the hotfix's test block above the branch's block.

**(c) THE DIFFERENCE IS THE HOTFIX** — `git diff --stat c183ed6 88602cc -- src tests` → `radar_panel.py | 13 ++++-`, `test_radar_panel.py | 113 +++…`, `2 files changed, 125 insertions(+), 1 deletion(-)`; `git diff --stat d87f3bd c8f4095 -- src tests` → the same two paths, same counts (13 / 113, `125 insertions(+), 1 deletion(-)`). HOLDS.

code patch unchanged by the rebase: **proven**.

## R3 SUITE + SEAM
1. `date` → `Mon Sep 21 12:06:52 EDT 2026`. `uv run pytest -q tests/cobalt tests/taxonomy` (background, offline, no `.env`) → `2221 passed, 351 skipped, 1 xfailed, 15 warnings in 63.42s (0:01:03)`. 0 failed; matches EXPECTED (2195 + 13 + 13 = 2221; skipped 351 unchanged).
2. `uv run pytest -q tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py` → `103 passed, 1 skipped in 0.90s` (expected 77 + 13 + 13).
3. SEAM VERIFIED before adding — `grep -n "BARS POLL FAILED\|def render_degraded_line\|carried = \|panel-banner {banner.level}\|querySelectorAll('.refresh-failure" src/cobalt/aset/radar_panel.py`:
   - `594: banners.append(BannerView(level="degraded", title="BARS POLL FAILED", detail=failed))`
   - `849: f'<div class="panel-banner {banner.level}"><b>{e(banner.title)}</b> · {e(banner.detail)}</div>'`
   - `873: def render_degraded_line(view: PoolView) -> str:`
   - `881: carried = [banner for banner in view.banners if banner.level in ("degraded", "stale")]`
   - `1127: function mirrorDegraded(layer){… querySelectorAll('.refresh-failure,.panel-banner.degraded,.panel-banner.stale') …}`
   All four links present as the drafter read them → the red line carries `BARS POLL FAILED` with no source change. The helper `_bars_poll_failed_pool()` exists at `tests/cobalt/test_radar_panel.py:413` (production row shape at 10:42, L45).
   Added `test_degraded_line_carries_the_bars_poll_failure` directly after `test_degraded_line_never_carries_retained`, exactly the prompt's text, no new fixture. `uv run pytest -q tests/cobalt/test_radar_panel.py -k "bars_poll_failure"` → `4 passed, 76 deselected in 0.22s` (the new test plus the hotfix's three `bars_poll_failure` cases the `-k` also selects). GREEN at once, as expected. `git add tests/cobalt/test_radar_panel.py` → `git commit` → `[s2/degraded-line-0921 7b0a6a3] test(radar): degraded line carries the bars poll failure (seam, L68)` · `1 file changed, 21 insertions(+)`; `git show --stat HEAD` lists only `tests/cobalt/test_radar_panel.py`. → seam test: **added green**.
4. `date` → `Mon Sep 21 12:08:18 EDT 2026`. `git log --oneline -1` → `7b0a6a3 test(radar): degraded line carries the bars poll failure (seam, L68)` = `<tip>`. Final suite `uv run pytest -q tests/cobalt tests/taxonomy` (background) → `2222 passed, 351 skipped, 1 xfailed, 15 warnings in 64.31s (0:01:04)`. 0 failed; matches EXPECTED for the seam test added (2221 + 1).

## CLOSE
`uv run cobalt jobs restarts main..HEAD` (L42, rebased range), VERBATIM:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/degraded-line-build-2026-09-21.md	A	DOCS	-
docs/40 - DevDocs/reports/degraded-line-rebase-2026-09-21.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset
```
As expected: `radar_panel.py` → `com.cobalt.aset`; the test file → no resident; docs `DOCS → -`; no `com.cobalt.radar`, no `UNCLASSIFIED`. (The tool also lists this report file, still uncommitted at that moment, as a docs `A` row — `DOCS → -`, no effect.)

`git diff --stat main HEAD` (before this report's commit):
```
 docs/40 - DevDocs/cobalt/aset/radar_panel.md       |   4 +-
 .../reports/degraded-line-build-2026-09-21.md      | 184 +++++++++++++++++++++
 src/cobalt/aset/radar_panel.py                     |  22 ++-
 tests/cobalt/test_radar_panel.py                   | 181 ++++++++++++++++++++
 4 files changed, 387 insertions(+), 4 deletions(-)
```
The same four R1 paths; the test file's count now includes the seam test (160 + 21).

`git diff --stat 88602cc HEAD -- . ':(exclude)docs'` → `tests/cobalt/test_radar_panel.py | 21 +++++++++++++++++++++` · `1 file changed, 21 insertions(+)` — EXACTLY the test file (seam test added); `src/` is byte-identical between the rebased code tip and HEAD. This is the identity the re-issued `16` checks tonight.

`git log --oneline main..HEAD` (before this report's commit):
```
7b0a6a3 test(radar): degraded line carries the bars poll failure (seam, L68)
771b2b7 docs(report): degraded line build — slim red line above the ladder, offline 2208/0, RESTARTS com.cobalt.aset
5db6d2d docs(devdocs): radar_panel — degraded line above the ladder (R10 2026-09-21)
88602cc feat(radar): slim red degraded line above the card ladder on /radar, mirrored by refreshPool (R10 2026-09-21)
```

## ESCALATE
1. NO BROWSER RAN. The live line is confirmed by the desk with Dejan on the real page after the deploy (L70) — the build's ESCALATE (ii), carried. Not a defect.
2. The with-DB suite: NOT RUN — the same scope as `14` and `29` (OFFLINE by design, `.env` absent; DB tests SKIP, `351 skipped`). Stated, not a defect (L70).

No `ASK DESK` items. No `MEMORY:` / `RULING:` lines. Both items above are the always-carried notes the prompt requires; neither is a defect, and nothing in R1–R3 failed, stopped or diverged. Preflight, R1 and R2 held exactly as EXPECTED; no permission was denied.

## CONTINUE
done — nothing left. The desk verifies (L35) and launches `35-review-degraded-line-deploy-r2.md`.

DEGRADED LINE REBASED 7b0a6a3 | on c8f4095 | cut c8f4095 | code tip 88602cc | offline 2222/0 (baselines main 2208/0, branch 2208/0) | code patch unchanged by the rebase: proven | seam test: added green | RESTARTS: com.cobalt.aset | ESCALATE: 2
