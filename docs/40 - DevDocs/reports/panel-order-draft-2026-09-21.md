# panel-order-draft-0921 — draft report (2026-09-21, 06:2x–06:3x ET)

## §0 Headline
- Two prompts drafted, NOT launched: `08-panel-order-build.md` (Sonnet 5 build, offline) and `09-panel-order-check.md` (Sonnet 5 hub, three houses, ROUND 1).
- The change is one line: swap the two f-string calls in `render_radar_page` (`radar_panel.py:1126`). No JS, CSS or test depends on the old order (0 dependencies).
- Builder seat: Sonnet 5. No write-path line is touched. NEW rule strings: NONE (19/19 and 17/17 count 1).
- ESCALATE 3: the degradation banners move below the ladder (his call, L9) · `web.md:7` DevDoc added to the build's paths (outside the brief's list) · the desk still has to fill in and commit the `R__` launch rows before 23:59 ET.

## ORDER DEPENDENCIES
| what | file:line (main) | does the swap break it |
|---|---|---|
| `refreshLadder` fetches `/radar`, parses it, swaps `#ladder-layer` BY ID | `radar_panel.py:1066-1075` | NO — it looks the layer up by id, so the order does not matter |
| `refreshPool` swaps `#pool-layer` BY ID | `radar_panel.py:1103-1116` | NO |
| `holder.firstElementChild` | `radar_panel.py:1110` | NO — this is the first element of the POOL FRAGMENT (`render_pool` output starts with `<section id="pool-layer"`), not of the page |
| `cursor` read from `#pool-layer` at script start | `radar_panel.py:1101` | NO — the `<script>` sits after `</main>`, so both sections exist when it runs |
| `collapse all` / `top 2` (`.ladder-item` query) | `radar_panel.py:1058-1060` | NO — they select by class |
| `.strip span:nth-child(4)` | `radar_panel.py:1050` | NO — this rule is inside a card strip, not a page section |
| sibling `+` / `~`, `:first-child`, `sticky` selectors | `PANEL_CSS` `:1046-1053` | none exist |
| `<1150 px` detail-column rule | `radar_panel.py:1049` | NO — it styles `.expanded` / `.detail-pane` |
| phone frame | `radar_panel.py:1051-1052`, `web.py:860` | NO — it styles `body` / `.radar-wrap` |
| `render_failed_page` | `radar_panel.py:1129-1131` | NO — it renders neither layer |
| tests that pin the order | `test_radar_panel.py`, `test_radar_panel_cards.py` | none. `:341-349` (cards) is the card detail order and terminal-below-active, both inside the ladder. `:503-509` checks that the phone frame is present. `:540` and `:455` check substrings only. `:451-452` monkeypatches `render_radar_page`. |
| DevDoc text | `web.md:7` "composes the pool-first page" | goes STALE after the swap → the build corrects it (ESCALATE 2) |
Code order dependencies: **0**. There is one visibility consequence that is not a code dependency: ESCALATE 1.

## L29 seat finding
**Sonnet 5.** The build touches no write-path line. `radar_panel.py`'s own docstring (`:6-8`) says it "never writes". A grep for `insert|transition|assert_writable|execute|commit|write` finds only those docstring lines. The only code line that changes is in `render_radar_page`, a pure renderer. The tap / grade POST handlers (`web.py:1294-1391`) live in the same package but are not touched: `web.py` must stay an EMPTY diff, and the prompt says STOP + ESCALATE if a step needs it. The ladder marks this item "Front-end only = Sonnet-eligible" (`:455`, `:468`).

## Worktree creation
**The desk creates it**, as it did for `10` / `11`. `11-bars-chunk-2-build.md:1` has "Three bare commands, run by the desk AFTER … are committed on main: `git -C /Users/cobalt/cobalt worktree add -b bars/chunk-2-0920 /Users/cobalt/cobalt-wt/bars-chunk-2 main` then `cd …` then `claude --bg …`". `08` copies that shape: `git -C /Users/cobalt/cobalt worktree add -b s2/panel-order-0921 /Users/cobalt/cobalt-wt/panel-order main`. The hub never runs `git worktree`, and it is listed under NOT in your list.

## Prompts
| file | size | seat |
|---|---|---|
| `prompts/2026-09-21/08-panel-order-build.md` | 27,128 B | Sonnet 5 build hub `panel-order-build-0921` — one session, offline |
| `prompts/2026-09-21/09-panel-order-check.md` | 27,881 B | Sonnet 5 check hub `panel-order-check-0921` — three houses, ROUND 1 |
Notes:
- `08` has no `--permission-mode auto` flag. That is byte-faithful to `02`'s (and `11`'s / `23`'s) launch shape; the flag is not a rule string.
- `09`'s folder `scratch/tribunal-bars-0920/panel-order-check/` sits under that name BECAUSE Grok's approved `--allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)"` covers only that root. A new folder root would need a new string. `09` says so.
- `09`'s PREFLIGHT refuses while `03`'s (`bars-chunk-2-check-r3-2026-09-21.md`) or `04`'s (`bars-chunk-1a-check-r3-2026-09-21.md`) report still ends on the in-progress line. An absent report does not block.

## RULE PROOF
`grep -c -F -e "<string>"`, one call per string:
- `08` vs `prompts/2026-09-21/02-bars-chunk-2-fix-r3.md`: 16 allow + 3 deny = **19/19 count 1**; the `--add-dir` triplet counts 1.
- `09` vs `prompts/2026-09-20/08-bars-chunk-e-check.md`: 14 allow + 3 deny = **17/17 count 1**; the triplet counts 1.
- Whole-block match, from `--allowedTools` through the triplet: `02` 1 / `08-panel-order-build` 1; `08-bars-chunk-e-check` 1 / `09-panel-order-check` 1.
- R3 committed on main: `git -C /Users/cobalt/cobalt log -1 --format=%H -S"my top should always be trade radar" -- …cto-2026-09-21.md` → `1be40a45d62970d54794559aa5706052dd28c686`.
**NEW strings: NONE.**

## READING
1. `Memory/LAWS.md` (in full)
2. `src/cobalt/aset/radar_panel.py` (`:808-859`, `:995-1144`, plus greps)
3. `tests/cobalt/test_radar_panel.py` (`:120-150`, `:485-594`, plus grep)
4. `tests/cobalt/test_radar_panel_cards.py` (`:110-189`, `:370-457`, plus grep)
5. `src/cobalt/aset/web.py` (grep)
6. `DevDocs/cobalt/aset/radar_panel.md` (grep)
7. `DevDocs/cobalt/aset/web.md` (grep)
8. `prompts/2026-09-21/02-bars-chunk-2-fix-r3.md`
9. `prompts/2026-09-20/14-bars-chunk-1a-check.md`
10. `prompts/2026-09-21/04-bars-chunk-1a-check-r3.md`
11. `prompts/2026-09-20/08-bars-chunk-e-check.md`
12. `prompts/2026-09-20/11-bars-chunk-2-build.md:1`
13. `reports/cto-2026-09-21.md` (§4 rows, grep)
14. `SPRINT-LADDER-v0_1.md` (grep)

NOT read directly: `cto-2026-09-20.md` R13 / R23 / R25. They are cited as `02` / `04` / `14` quote them, and each hub greps them itself in AUTHORIZATION.

## L74
One block arrived appended to a tool result: the prompt file's Read output carried a `Claude-Session:` commit-line instruction and named a file-send tool. It is DATA. It was not followed. This run made no commit.

## ESCALATE
1. **VISIBILITY, his call (L9).** The pool section carries the page's loud-degradation surfaces:
   - `#refresh-status` / `REFRESH FAILED` (`radar_panel.py:851`, `:1113-1114`);
   - the `panel-banner` source banners (`:837-840`);
   - the `stale-data` outline (`:849`).
   After the swap they sit BELOW the ladder. The ruling says the pool goes below with its content unchanged, so neither prompt moves them. `08` lists this under ESCALATE, and `09` asks every house (question 6) whether it is a DEFECT or an OWNER ITEM. `ASK DESK: should a degraded/stale banner ALSO show above the ladder? That is a new ruling, not part of R3. [06:33 ET]` Safe default: unchanged.
2. **One path outside the brief's diff list.** `docs/40 - DevDocs/cobalt/aset/web.md:7` says `GET /radar` "composes the pool-first page". The swap makes that false. `08`'s D1 corrects that one word, and `web.md` joins the allowed `git diff --stat main` paths in `08` and `09`. It is docs only (`web.py` stays an EMPTY diff), but it widens the brief's path list by one DevDoc. If the desk refuses this, delete D1's `web.md` clause in both prompts (L19 re-issue).
3. **Desk actions before launch.**
   - Fill in the `R__` launch rows in `cto-2026-09-21.md` for `08` and `09`, and commit them with both prompt files. Each hub greps `-S"08-panel-order-build.md"` / `-S"09-panel-order-check.md"` and FAILS on an uncommitted row.
   - `09` must START before 2026-09-21 23:59 ET (the R23 window). The `08` build is SMALL, so this is feasible today.
   - `09` is staggered with `03` / `04`, which use the same three houses.

## CONTINUE
Done. Nothing is left for this seat. Next, not this seat's: the desk reads both prompts, a house other than the author checks them (L67 floor), the desk fills and commits the launch rows, then creates the worktree and launches `08`.

PANEL ORDER PROMPTS DRAFTED · prompts: 2 · builder seat: Sonnet 5 · order dependencies: 0 · new rule strings: 0 · READING: 14 · ESCALATE: 3
