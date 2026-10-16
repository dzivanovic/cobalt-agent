# Card 622 jev-shadow-fr1 — preflight (read-only), 2026-10-16

Card `prompts/2026-10-16/622-jev-shadow-fr1-card.md`. Anchors proved on the working tree, which equals HEAD for every file cited (`git diff HEAD --stat` over `src/cobalt/classify` and `tests/cobalt/test_jev_shadow_1015.py` printed nothing). `main` moved during the run (`HEAD` ecc74af6, later `main` bd30d4d5).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat HEAD -- <622>` · `git log --oneline -2 -- <622>` | empty · `ecc74af6 docs(card): 622 …` (committed) | OK |
| 2 | `git diff --no-index -U0 <591> <622>` | hunks only in JOB, BRANCH, WORKTREE, BASE (now empty), REPORT, RULINGS (+R1620) and the added `## FIX ROUND` | OK |
| 3 | FR-O2 vs `621-draft-jev-shadow-fr1.md:6` | the card's `FR-O2:` line and prompt line 6 read identical | OK |
| 4 | `grep -c -F "«FILL"` · `grep -n -E "TODO\|TBD\|XXX\|<FILL\|PLACEHOLDER\|«"` | `0` · no hit | OK |
| 5 | anchor: day-batch routing, `route.py` `closed_cards` `:538-550`, `cmd_route` `:728-760` (`paths = … closed_cards(repo, args.day)` `:733`) | present at HEAD; it takes every `*-card.md` under `PROMPTS_DIR` (`:542-543`) | OK |
| 6 | anchor: `route --day`, `add_route_parsers` `:774-784` (`--day` `:778`) | present | OK |
| 7 | anchor: outcome rows reading CHECK DONE, `write_outcome` `:578-614` (`startswith("CHECK DONE")` `:589`), `_check_report` `:526-535`, `_last_line` `:521` | present | OK |
| 8 | anchor: build-launch detection, `launch_sha` `:319-327` (last commit whose `TIP:` is empty, else `ClassifyError`) | present; this is the content hook for "launch kind is build" | OK |
| 9 | red expressible with the card's fixtures: `_closed_card` `test_jev_shadow_1015.py:623`, `_card` `:137`, `_commit` `:127`, `_batch` `:734`, `DAY` `:47` | build card = `_closed_card`; check card = `_card(tip="abcd1234", check_report=<same report>)` committed the same day; today `closed_cards` returns both paths, so two decision rows (the check card gives a `launch_sha` ClassifyError row via `unloaded_row` `:753`); after the fix, one | OK |
| 10 | FR-O2 vs 591 F9 wording ("cards whose check CLOSED that day", `F9` row, ASK DESK 16) | conflict, see ISSUES 2 | NOTE |
| 11 | commands the card adds vs the BUILD-HUB `:12` allow line | none added: `uv run pytest`, `uv run cobalt jobs restarts`, `git diff/log/show`, `grep`, `ls`, `wc`. R1, ASK DESK 18 and 19 name commands the builder does not run | OK |
| 12 | RESTARTS vs derived class of `files` (`jobs.yaml:159` agent imports `cobalt_agent.main`; `:203` radar imports `cobalt.cli`; `route.yaml`, `trial.yaml` classified `jobs.yaml:345-359`) | `com.cobalt.agent com.cobalt.radar` is right for 591's full `files` set; FR-O2 alone touches `src/cobalt/classify/route.py` + tests = `com.cobalt.radar` only | NOTE |
| 13 | card header vs `CARD.md:20-21` | `CHECK REPORT:` is filled with the 10-15 check report; CARD.md says build = empty | NOTE |
| 14 | `ls /Users/cobalt/cobalt-wt` · `rev-parse feat/jev-shadow-fr1` | no `jev-shadow-fr1` worktree, no such branch (a clean cut) | OK |

## ISSUES

1. **FAIL-class, blocks the build: the card still carries 591's whole `## ROWS` (Z0, P0, D2, F13, F2, F3, J1 … R2), and every one is already on `main`.** `src/cobalt/classify/route.py` exists at HEAD, `grep -c -F "'openrouter_api_key': 'api_key'" src/cobalt_agent/config.py` is `0` (F13 landed), `test_jev_shadow_1015.py` exists. The BASE for the fix round is main HEAD, so P0 "port onto BASE", every `RED on BASE` and ORDER's "reds on the P0 port" cannot go red or be built. Nothing in the card says the rows stand as rules and only `## FIX ROUND` is built. The drafter was told to add nothing else (621). Needed from the desk: one line, in the card or the launch message, that the `## FIX ROUND` row is the only row built and every `## ROWS` row stands as its rule (the shape of card 603's WHY).
2. **FR-O2 against F9: FR-O2 wins, and the builder can reconcile by content.** F9 selects cards by "check CLOSED that day" (`closed_cards` `:548`, date of the check report's last commit). FR-O2 selects build cards "whose build launched that day". These are two different day keys. The card does not say which date FR-O2 uses. Default for the builder: keep F9's `CHECK DONE` closed gate and its day (outcome and decision rows stay keyed as built), add FR-O2's filter before it (skip a card whose `launch_sha` raises, i.e. a card with no empty-`TIP:` commit, and any card not a build card), and record the day choice under `## DECISIONS`. `FR-O2` itself says "launched that day": if the desk means the launch commit's date, F9's tests `test_f9_*` (`_closed_card`, `:623`) commit card and report in one commit, so they stay green either way.
3. NOTE: "launch kind is build" has no header key. The only content test in the code is `launch_sha` (empty `TIP:`), which also holds for a deploy or devfix card (no `TIP`). The builder must also exclude `CHECK REPORT:`-less and kind-marked cards by path or header; the card does not say how. Default: a build card is a `*-card.md` with an empty `TIP:` at some commit and a `## ROWS` section.
4. NOTE: RESTARTS lists `com.cobalt.agent` although FR-O2's only paths are in `src/cobalt/classify/` (radar). The builder's own `uv run cobalt jobs restarts <BASE>..HEAD` derives it (L42); the header value is a prediction.
5. NOTE: header `CHECK REPORT:` is non-empty on a build card (CARD.md says empty). `desk-launch.sh` checks only that keys its kind needs are non-empty, so it should not refuse; the desk confirms at launch.
6. BLOCKS THE BUILD LAUNCH: (a) issue 1's one-line scope statement; (b) `BASE:` is empty, the desk writes main HEAD and commits (CARD.md `:17`: build needs the 8-hex BASE; the card says "BASE (empty)" on purpose); (c) the card must be re-committed after (a) and (b) so `authorize.sh` finds it unchanged; (d) R1620 must be a committed `HIS RULING` + `APPROVED` row for the RULINGS proof (not read here).

PREFLIGHT DONE · card: jev-shadow-fr1 · checks: 14 · fails: 1 · ready: NO
