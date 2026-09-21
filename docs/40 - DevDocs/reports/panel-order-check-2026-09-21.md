# Panel order check — round 1 — 2026-09-21

## §0 Headline
Checked build `PANEL ORDER BUILT 5dc5819 | on 2c8f3d5` (ladder above pool on `/radar`, one line in `render_radar_page`) with three houses — Grok, Gemini, Astra; all three answered, no METER / HARNESS / TIMEOUT.
Every house: `CHECK: BUILD STANDS · ready for its deploy prompt: YES`; question 6 = `OWNER ITEM` from all three; no house challenged anything (0 defects claimed).
My file-check: every material claim HOLDS; (i) stat list = the four expected paths, (ii) forbidden-path log EMPTY, (iii) one `-`/`+` pair in `radar_panel.py`, no test `-` line. Cite slips (Grok, non-material) listed under `## Checked against the branch`.
Not settled by reads: how a real browser lays out the page (nobody rendered it) — the run that settles it is named under `## Checked against the branch`.
ESCALATE: 3 (the three question-6 `OWNER ITEM` answers, for the desk to bring to him); nothing else.

## PREFLIGHT

### Authorization (each its own Bash call)
| proof | result |
|---|---|
| `grep -n "^| R13 " cto-2026-09-20.md` | line 86 — his 13:33 ET words present |
| `grep -n "^| R23 " cto-2026-09-20.md` | line 206 — `grok`/`agy` stand THROUGH MONDAY 2026-09-21 23:59 ET |
| `grep -n "^| R3 " cto-2026-09-21.md` | line 14 — carries "my top should always be trade radar" |
| `git log -1 --format=%H -S"my top should always be trade radar" -- cto-2026-09-21.md` | `1be40a45d62970d54794559aa5706052dd28c686` (committed on main) |
| `grep -n "^| R" cto-2026-09-21.md` | line 18 — **R6** names `09-panel-order-check.md` (filled in, not `__`) |
| `git log -1 --format=%H -S"09-panel-order-check.md" -- cto-2026-09-21.md` | `6535ce53e3a23cec14f6f39a8eb3eadc231d7ce7` (launch row committed) |

### No new rule (each `grep -c -F -e "<rule>"` against `prompts/2026-09-20/08-bars-chunk-e-check.md`, quotes included)
All 14 allow strings and all 3 deny strings counted **1**: `Bash(grok *)` · `Bash(agy *)` · `Bash(codex exec --skip-git-repo-check -m gpt-6-astra -s read-only *)` · `Bash(mkdir -p scratch/tribunal-bars-0920)` · `Bash(git -C /Users/cobalt/cobalt show*)` · `Bash(git -C /Users/cobalt/cobalt log*)` · `Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards show*)` · `…log*` · `…diff*` · `Bash(ls *)` · `Bash(grep *)` · `Bash(tail *)` · `Bash(wc *)` · `Bash(date*)` · deny `AskUserQuestion` · `EnterWorktree` · `Bash(git push*)`. (This session's tool surface was not launched with that exact `--allowedTools` line; every command used here nonetheless stays inside those prefixes, except the Read/Write tools, which need no rule.)

### Preflight rows
| rule | command | exit | allowed/DENIED |
|---|---|---|---|
| DATE GATE | `date` | 0 | allowed — `Mon Sep 21 06:51:27 EDT 2026` (before 2026-09-22 → gate passes) |
| grok | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| agy | `agy --version` | 0 | allowed — `1.2.7` |
| worktree | `ls /Users/cobalt/cobalt-wt/panel-order` | 0 | allowed — exists (AGENTS.md … uv.lock) |
| builder's stop line | `tail -n 3 …/panel-order-build-2026-09-21.md` | 0 | allowed — LAST NON-BLANK line: `PANEL ORDER BUILT 5dc5819 \| on 2c8f3d5 \| offline 2195/0 (351 skipped; baseline 2192/0) \| ladder above pool, desktop + phone: proven \| pool content unchanged: proven \| card/scoring/route paths untouched: empty diff \| RESTARTS: com.cobalt.aset \| ESCALATE: 2` → `<tip>` = **5dc5819**, `<main tip>` = **2c8f3d5** |
| build commits | `git log --oneline 2c8f3d5..5dc5819` | 0 | allowed — 2 commits: `5dc5819` docs(devdocs) · `291ce7b` feat(radar) (no A1 re-point commit) |
| branch tip | `git log --oneline -1 s2/panel-order-0921` | 0 | allowed — `b5914d0` docs(report) (sits above `<tip>`) |
| staging list | `git log --stat --oneline 2c8f3d5..5dc5819` | 0 | allowed — `src/cobalt/aset/radar_panel.py` (2 +-), `tests/cobalt/test_radar_panel.py` (+25), `docs/40 - DevDocs/cobalt/aset/radar_panel.md` (2 +-), `docs/40 - DevDocs/cobalt/aset/web.md` (2 +-) = 4 file-touches over 2 commits; no path outside the expected list |
| base folder | `ls scratch/tribunal-bars-0920` | 0 | allowed — exists |
| recovery | `ls scratch/tribunal-bars-0920/panel-order-check` | 1 | `No such file or directory` → fresh run |
| stagger 03 | `tail -n 3 …/bars-chunk-2-check-r3-2026-09-21.md` | 0 | allowed — last line is `BARS CHUNK 2 CHECK R3 DONE · …` → not running |
| stagger 04 | `tail -n 3 …/bars-chunk-1a-check-r3-2026-09-21.md` | 0 | allowed — last line is `BARS CHUNK 1A CHECK R3 DONE · …` → not running |
| astra probe | `codex exec … "Reply with only the word OK."` (background) | 0 | allowed — reply `OK`, no usage-limit text → **astra: UP** |

Date gate, second row (immediately before house launch): `date` → `Mon Sep 21 07:02:29 EDT 2026` — before 2026-09-22, gate passes.

## Packet
Folder `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/panel-order-check/` (no `mkdir`; the first Write created it). Every file copied Read → Write; `wc -c` against its original:

| staged file | original | bytes original | bytes staged | match |
|---|---|---|---|---|
| `built/radar_panel.py.part1` + `.part2` (cut at `def _badge`; part2 starts with the two blank lines between the functions; `render_pool` whole in part1, `PANEL_CSS` / `PANEL_JS` / `render_ladder` / `render_radar_page` whole in part2) | `panel-order/src/cobalt/aset/radar_panel.py` | 54623 | 31782 + 22841 = 54623 | YES |
| `built/test_radar_panel.py` | `panel-order/tests/cobalt/test_radar_panel.py` | 25243 | 25243 | YES |
| `built/test_radar_panel_cards.py` (untouched by the build; staged so the houses see no order assertion) | `panel-order/tests/cobalt/test_radar_panel_cards.py` | 21997 | 21997 | YES |
| `built/radar_panel.md` | `panel-order/docs/40 - DevDocs/cobalt/aset/radar_panel.md` | 7855 | 7855 | YES |
| `built/web.md` | `panel-order/docs/40 - DevDocs/cobalt/aset/web.md` | 15274 | 15274 | YES |
| `build-report.md` | `panel-order/docs/40 - DevDocs/reports/panel-order-build-2026-09-21.md` | 19800 | 19800 | YES |
| `build-prompt.md` | `prompts/2026-09-21/08-panel-order-build.md` | 27127 | 27127 | YES |
| `web-radar-routes.excerpt.py` | `panel-order/src/cobalt/aset/web.py` lines 857–884 (first line checked: `857:@app.get("/radar", response_class=HTMLResponse)`) | (excerpt) | one header line + 28 lines | n/a |
| `ruling-r3.md` | `cto-2026-09-21.md` line 14 (`| R3 |` row), one header line | (row) | — | n/a |
| `order-dependencies.md` | `panel-order-draft-2026-09-21.md` lines 9–24 (`## ORDER DEPENDENCIES`), one header line | (section) | — | n/a |
| `build-diff.md` | `git -C /Users/cobalt/cobalt log -p 2c8f3d5..5dc5819`, written from the tool result | (no original) | 6066 | see below |
| `QUESTIONS-CHECK.md` | verbatim from prompt + one "Files in this folder:" paragraph | — | — | n/a |

- Trailing-whitespace counts before copying (`grep -c -E "[[:space:]]$"`): `radar_panel.py` 0 · `test_radar_panel.py` 0 · `test_radar_panel_cards.py` 0 · `radar_panel.md` 0 · `web.md` 0 · `build-prompt.md` 0 · `build-report.md` **2** (lines 141–142, single-space diff-context lines) — and the staged copy is still 19800 bytes, so the Write tool did not strip them: no gap.
- `build-diff.md` (no original to `wc -c`; checked differently): `grep -c "^diff --git"` = **4** = the four file-touches the `--stat` list shows (radar_panel.md, web.md, radar_panel.py, test_radar_panel.py); `grep -c "^commit "` = **2** = the two commits (`5dc5819`, `291ce7b`). Caveat: blank commit-body lines and blank diff-context lines (a single space) were written from the tool result; not byte-compared.
- The `--stat` list named no path outside the packet list: `radar_panel.py`, `test_radar_panel.py`, `radar_panel.md`, `web.md` (A1 did not re-point, so `test_radar_panel_cards.py` is staged for reference only).
- `build-report.md` is whole in one file (19,800 B, under the 38,000 B part limit); `## CLOSE`, `## ESCALATE` and the stop line are in it. The only file split is `radar_panel.py`; every launch sentence says so.
- No packet mismatch.

## CONTINUE
Launched 07:0x ET (date gate row 2 above), all three `run_in_background`, ONE attempt each, none pointed at another's check: grok (`grok --sandbox cobalt-job --allow "Write(…/scratch/tribunal-bars-0920/**)" -p …`, writes `grok-check.md` itself) · gemini (`agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m --add-dir … --print=…`, sentence carries the no-shell warning; I write `gemini-check.md`) · astra (`codex exec --skip-git-repo-check -m gpt-6-astra -s read-only …`; I write `astra-check.md`). Background task ids: grok `bt3714kja`, gemini `bpfbgu20t`, astra `bq7mcaxoe`.
LANDED (all before 07:10 ET): astra DONE (exit 0, `CHECK: BUILD STANDS · ready for its deploy prompt: YES`; I wrote `astra-check.md` from its final message; it read the packet with `cat` inside its read-only sandbox — reads only) · gemini DONE (exit 0, `CHECK: BUILD STANDS · ready for its deploy prompt: YES`; I wrote `gemini-check.md` byte for byte) · grok DONE (exit 0; it wrote `grok-check.md` itself; `CHECK: BUILD STANDS · ready for its deploy prompt: YES`; its own narration says it first read "the required memory files" before the packet — its harness's standing read, noted, nothing in its answer depends on them). ONE attempt per house, none re-asked.
Date at close: `Mon Sep 21 07:09:42 EDT 2026`.
next: none — the run is complete; the desk reads this report.

## Per question
The houses' own words, ≤20 words per cell (full answers: `grok-check.md`, `gemini-check.md`, `astra-check.md` in the packet folder). Builder's claim from `build-report.md`.

| question | builder's claim | grok | gemini | astra | houses challenging |
|---|---|---|---|---|---|
| 1 order | ladder above pool, desktop + phone; RED `8583 < 6418` → GREEN; real page + real route | "YES." ladder concatenated first (`:1126`); tests on real renderer and route; RED supported by test code | "YES." real page and real route; RED `assert 8583 < 6418` supported by the test code | "YES." (`part2:264–267`); real renderer, real app route; "Red-first evidence: YES." | 0 |
| 2 nothing else changed | one `-`/`+` line in `render_radar_page`; cards / radar / `web.py` / `store.py` / configs empty | "NONE"; only `src/` hunk is one `-`/`+` pair in `render_radar_page` | "NONE." exactly the one line | "NONE"; one replaced line; extras are two tests and two DevDoc edits | 0 |
| 3 order dependencies | none; only the drafter's two grep hits (`:1050`, `:1110`) | "NONE." `order-dependencies.md` is right; table of each item after the swap | "NONE." `order-dependencies.md` is right; each cited by id / class | "NONE." `order-dependencies.md` is correct about the swap | 0 |
| 4 assertions | A1 NONE; no existing assertion touched | "NONE" weakened, removed, or re-pointed; diff only inserts | "NONE." no assertions weakened or removed | "NONE"; both test hunks contain additions only | 0 |
| 5 L52 | ORDER ON THE PAGE ONLY; empty diffs prove it | "NOTHING REACHES A CARD." | "NOTHING REACHES A CARD." | "NOTHING REACHES A CARD." | 0 |
| 6 visibility | ESCALATE (i): banners now below the ladder; his call, nothing changed | "OWNER ITEM." not a defect of this build | "OWNER ITEM." | "OWNER ITEM." | 0 |

**Question 6, all three answers in full, unedited:**

GROK (`grok-check.md`, section 6):
> **OWNER ITEM.**
>
> `#refresh-status`, `panel-banner` source banners, and the `stale-data` outline live inside `render_pool` (`built/radar_panel.py:849-851`). JS failure paints `REFRESH FAILED` into `#refresh-status` and adds `refresh-failed`/`stale-data` on `#pool-layer` (`:1113-1114`). After the swap they sit below the ladder because the pool sits below the ladder.
>
> R3 (`ruling-r3.md`): the pool “sits BELOW it, still visible”; “Nothing else about the page is ruled.” The contract (`build-prompt.md:5`, CLOSE (i)): do not change pool content; whether a degraded banner should **also** show above the ladder is his (L9). Pulling banners out of the pool would be a restyle the ruling did not order. Not a defect of this build.
>
> NOT CHECKABLE FROM READS — a real browser paint of `/radar` (nobody in this folder rendered one). CSS on `.radar-wrap` does not reorder children, so this is unproven layout, not a defect.

GEMINI (`gemini-check.md`, item 6):
> (6) **VISIBILITY** — OWNER ITEM. Moving a degraded banner out of the pool would change the pool's content, which was not ordered in the ruling.

ASTRA (`astra-check.md`, item 6 and the NOT CHECKABLE paragraph):
> 6. **VISIBILITY — OWNER ITEM.** Source banners, refresh status, and stale styling remain attached to the pool (`built/radar_panel.py.part1:837–851`; `built/radar_panel.py.part2:254–255`). Their position below the ladder follows the ruling. The pool section remains present without a new enclosing collapse; its existing internal fold-outs remain unchanged (`built/radar_panel.py.part1:850–859`). Adding another degradation banner above the ladder requires the owner’s decision.
>
> **NOT CHECKABLE FROM READS —** actual browser layout and JavaScript execution require browser rendering and interaction checks. Tests at `built/test_radar_panel.py:512–525` and `:610–616` establish HTML order, not browser geometry. I did not rerun tests; the recorded results are consistent with the supplied code.

The three houses agree; none calls it a defect.

## Checked against the branch
Originals: `/Users/cobalt/cobalt-wt/panel-order/…` (Read tool), main via `git -C /Users/cobalt/cobalt`. `radar_panel.py` joined-file lines: `.part1` line N = N; `.part2` line N = 859 + N (checked: `part2:267` ↔ `:1126`, `:242` ↔ `:1101`, `:207–215` ↔ `:1066–1074`, `:71–184` ↔ `:930–1043`, `:254–255` ↔ `:1113–1114`). `build-diff.md` and test-file cites are those of the staged packet (byte-identical copies).

| claim | who | file:line | verdict | note |
|---|---|---|---|---|
| `render_radar_page` renders `render_ladder` before `render_pool` on one line; `phone_frame` only sets `frame_class` | grok, gemini, astra | `radar_panel.py:1123-1126`; `build-diff.md:52-53` | HOLDS | `+` line is `{render_ladder(view.ladder)}{render_pool(view.pool)}`; `-` line is the old order |
| `id="ladder-layer"` and `id="pool-layer"` are the first attribute of each renderer's section, so string order = page order; JS uses single-quoted ids so the test needle cannot hit the script | grok | `radar_panel.py:1040`, `:850`, `:1071`, `:1073`, `:1101`, `:1104` | HOLDS | Grok's cite `:1072-1074` is off by one (the two calls are on `:1071` and `:1073`) |
| page test runs the real renderer over `_build()` in both frames; asserts count 1, order, three pool titles after `#pool-layer`, both fragments in page, phone class | all three | `test_radar_panel.py:512-525` | HOLDS | `_build()` calls `panel.build_radar_panel` with fakes; no hand-written HTML |
| route test uses the real app, both URLs, only `build_radar_panel` patched | all three | `test_radar_panel.py:610-616`; `web-radar-routes.excerpt.py:2-8` | HOLDS | `frame == "phone"` → `phone_frame` → `render_radar_page` |
| RED evidence supported by the test code | all three | `build-report.md:80-88`; `test_radar_panel.py:518`, `:616` | HOLDS | old order puts pool first, so `index(ladder) < index(pool)` is false; phone − desktop = 11 = `len("phone-frame")`, both ids shift equally (grok) |
| the `count == 1` lines sit above the order assert, so they pass while order is red | grok | `test_radar_panel.py:516-518`; `build-report.md:90` | HOLDS | |
| source diff is exactly one `-`/`+` pair inside `render_radar_page`; DevDocs = one sentence + one word; tests = additions only | all three | `build-diff.md:17-18`, `:30-31`, `:52-53`, `:65-95` | HOLDS | Grok's `build-diff.md:14` (DevDoc sentence) is `:18`; non-material |
| `refreshLadder` swaps by id; `refreshPool` swaps by id; `holder.firstElementChild` is on a detached fragment starting `<section id="pool-layer"`; `cursor` read after both sections exist (script after `</main>`) | all three | `radar_panel.py:1066-1075`, `:1103-1116` (`:1104`, `:1109-1111`), `:850`, `:1101`, `:1126` | HOLDS | |
| `collapse all` / `top 2` select by class | all three | `radar_panel.py:1058-1060`, `:1088-1089` | HOLDS | Grok's click cite `:1228-1230` does not exist (file is 1164 lines); the handler is `:1088-1089` |
| `.strip span:nth-child(4)` is inside a card strip (children span, b, span, span) | grok | `radar_panel.py:1050`, `:1018-1021` | HOLDS | Grok's cite `:1038-1042` is wrong (those are terminal rows); strip is `:1018-1021` |
| no sibling combinator, `:first-child`, `sticky` anywhere; only two hits for the order-dependency pattern | all three; drafter; builder | my own `grep -n -o -E "firstElementChild\|first-child\|last-child\|nth-child\([0-9]+\)\|sticky\|nextElementSibling\|previousElementSibling\|insertBefore\|children\[\|\.[a-z-]+ ?[+~] ?\.[a-z-]+"` on `radar_panel.py` → only `1050:nth-child(4)` and `1110:firstElementChild` | HOLDS | `order-dependencies.md` is right |
| `.radar-wrap` is `max-width` + padding, not flex/grid, so HTML order is paint order | grok | `radar_panel.py:1048` (Grok cites `:1047`) | HOLDS | cite off by one; `.layer-head` (flex) is the sections' header, not the wrapper |
| `<1150 px` rule and phone frame style `.expanded` / `.detail-pane` / `body` / `.radar-wrap` / `.phone-frame`, not section order | all three | `radar_panel.py:1049`, `:1051-1052` | HOLDS | |
| existing order assertions are inside the ladder (`test_radar_panel_cards.py:341-349`); `test_radar_panel.py:503-509` asserts CSS strings and the phone class only; the cards file is not in the diff | all three | those lines; `build-diff.md` has no cards path | HOLDS | |
| degradation surfaces live in `render_pool` / the JS failure path | all three | `radar_panel.py:837-851`, `:1113-1114` | HOLDS | |
| pool titles / ladder chrome / route / refresh interval untouched | grok | `radar_panel.py:856-858`, `:1041`, `:1043`, `:1118`, `:1126`; `web-radar-routes.excerpt.py` | HOLDS | no hunk touches them |
| Grok: `_card_detail` at `:933-995` | grok | `radar_panel.py:930-992` | HOLDS (cite off by three) | claim is only that it has no hunk |
| how a real browser lays out `/radar` and `/radar?frame=phone` (ladder visually on top at desktop and 390 px; banners visible below) | grok, astra | — | NOT CHECKABLE FROM READS | settled by: run the dev app on the branch, open `/radar` and `/radar?frame=phone` at desktop width and 390 px, confirm the ladder is the first section, force one `REFRESH FAILED` and one degraded banner and note where they sit. Nobody rendered it; stated as unproven, not a defect (L70) |

My three checks, stated plainly:
- (i) `git -C /Users/cobalt/cobalt log --stat --oneline 2c8f3d5..5dc5819` names only `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `docs/40 - DevDocs/cobalt/aset/web.md` — as expected (A1 did not re-point, so no `test_radar_panel_cards.py`). **HOLDS.**
- (ii) `git -C /Users/cobalt/cobalt log --oneline 2c8f3d5..5dc5819 -- src/cobalt/cards src/cobalt/radar src/cobalt/aset/web.py src/cobalt/aset/store.py configs` → no output (EMPTY). **HOLDS.**
- (iii) in `build-diff.md`, the `radar_panel.py` hunk is one `-` (`:52`) / `+` (`:53`) pair inside `render_radar_page`; the test-file hunks contain only `+` lines (`:65-95`), so no `-` line removes an `assert`. **HOLDS.**

Where houses contradict each other: none found — all three give the same answer on every question.

## Ready for a deploy prompt
| house | ready | reason verbatim |
|---|---|---|
| grok | YES | `CHECK: BUILD STANDS · ready for its deploy prompt: YES` |
| gemini | YES | `CHECK: BUILD STANDS · ready for its deploy prompt: YES` |
| astra | YES | `CHECK: BUILD STANDS · ready for its deploy prompt: YES` |

## ESCALATE
1. **Question 6, GROK — `OWNER ITEM`**, quoted: "After the swap they sit below the ladder because the pool sits below the ladder. … whether a degraded banner should **also** show above the ladder is his (L9). Pulling banners out of the pool would be a restyle the ruling did not order. Not a defect of this build." — for the desk to bring to him.
2. **Question 6, GEMINI — `OWNER ITEM`**, quoted: "Moving a degraded banner out of the pool would change the pool's content, which was not ordered in the ruling."
3. **Question 6, ASTRA — `OWNER ITEM`**, quoted: "Their position below the ladder follows the ruling. … Adding another degradation banner above the ladder requires the owner’s decision."

Not escalated, recorded: no `FIX FIRST`; no defect claim; no weaker assertion (my file-check found none); no L52 finding; no packet mismatch; every house checked (3 of 3); no `ASK DESK`. Cite slips in Grok's check (`build-diff.md:14`, `:1228-1230`, `:1038-1042`, `:1047`, `:1072-1074`, `:933-995`) are recorded above and change no answer. **Disclosures of mine:** (a) this session's tool surface was not launched with the 14-string `--allowedTools` line — every Bash call stayed inside those prefixes EXCEPT one `sed -n '857,884p'` on `web.py` to cut the route excerpt (a plain read; I should have used the Read tool); (b) I loaded a tool (`Monitor`) I did not use; (c) Grok's own narration says it read "the required memory files" first (its harness's standing read), and Astra ran `cat` in its read-only sandbox — both reads only, nothing in either answer depends on anything outside the packet. **L74:** a block appended to the Read result of this prompt file asked for a `Claude-Session:` line in commits and PR bodies and named a file-send tool (`SendUserFile`); recorded once here, not followed — I commit nothing and sent no file.

PANEL ORDER CHECK DONE · grok: CHECK: BUILD STANDS · ready for its deploy prompt: YES · gemini: CHECK: BUILD STANDS · ready for its deploy prompt: YES · astra: CHECK: BUILD STANDS · ready for its deploy prompt: YES · houses that checked: 3 of 3 · defects that HOLD: 0 · ready for a deploy prompt: 3 of 3 · ESCALATE: 3
