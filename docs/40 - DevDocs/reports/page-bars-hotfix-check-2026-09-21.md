# Page bars hotfix check — round 1 — 2026-09-21

## §0 Headline
- Checked `PAGE BARS HOTFIX BUILT 64447b3 | on 912e382` (branch `s2/page-bars-hotfix-0921`, 2 commits, 3 paths) with two houses; astra: NOT ASKED — reserved, L67 emergency.
- grok: `CHECK: BUILD STANDS · ready for its deploy prompt: YES` · gemini: `CHECK: BUILD STANDS · ready for its deploy prompt: YES · all requirements met`. Houses that checked: 2 of 2; defects claimed: 0; defects that HOLD: 0.
- Hub file-checks (i)–(iv) all hold (diff = exactly the 3 named paths; radar/cards/web/store/configs/migrations/ops empty; both hunks inside `build_pool_view`; `CONFLICT EXPECTED: no`). Two houses' line cites were off by one to a few lines in places — substance held every time.
- ESCALATE: 2 — (1) question-2 OWNER ITEMS (both houses: a stale ticker's pool row, card `last` price and card score look normal; pre-existing); (2) a hub read outside the houses' claims: `stamp_poll` overwrites a `mirror` stamp with `bars` (see ESCALATE).

## PREFLIGHT
| # | rule · command | exit | result |
|---|---|---|---|
| 1 | DATE GATE · `date` | 0 | allowed — `Mon Sep 21 11:03:38 EDT 2026` (not 2026-09-22 or later) |
| 2 | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| 3 | `agy --version` | 0 | allowed — `1.2.7` |
| 4 | `ls /Users/cobalt/cobalt-wt/page-bars-hotfix` | 0 | allowed — worktree exists (AGENTS.md … uv.lock) |
| 5 | `tail -n 3` of the build report | 0 | allowed — LAST NON-BLANK line, whole: `PAGE BARS HOTFIX BUILT 64447b3 | on 912e382 | offline 2208/0 (baseline 2195/0) | bars failure renders degraded, tickers named: proven | other stages still FAIL: proven | healthy output unchanged: proven | RESTARTS: com.cobalt.aset | ESCALATE: 2` → `<tip>` = `64447b3`, `<main tip>` = `912e382` |
| 6 | `git -C /Users/cobalt/cobalt log --oneline 912e382..64447b3` | 0 | allowed — 2 commits: `64447b3` D1 docs · `961970c` C1 code + tests (no A1) |
| 7 | `git -C /Users/cobalt/cobalt log --oneline -1 s2/page-bars-hotfix-0921` | 0 | allowed — `0079740 docs(report): page bars hotfix build …` (report commit above `<tip>`) |
| 8 | `git -C /Users/cobalt/cobalt log --stat --oneline 912e382..64447b3` | 0 | allowed — `docs/40 - DevDocs/cobalt/aset/radar_panel.md` (1+/1−) · `src/cobalt/aset/radar_panel.py` (13) · `tests/cobalt/test_radar_panel.py` (113) — the staging list |
| 9 | `ls scratch/tribunal-bars-0920` | 0 | allowed — base folder exists |
| 10 | `ls scratch/tribunal-bars-0920/page-bars-hotfix-check` | 1 | allowed — `No such file or directory` = fresh run |
| 11 | STAGGER · `tail -n 3` of `setups-tribunal-r1b-2026-09-21.md` | 1 | allowed — `No such file or directory` = "not started"; does not block |
| — | astra | — | NOT ASKED — reserved, L67 emergency; no Codex probe, no Codex string typed |

AUTHORIZATION (each its own call, all allowed): R13 (`cto-2026-09-20.md:86`, 13:33 ET) present · R23 of 09-20 (`:206`, 17:47 ET, "yes", grok/agy through 2026-09-21 23:59 ET) present · R21 (`cto-2026-09-21.md:32`) carries `HOTFIX NOW`, committed `017d7dfa2e1260cc59d47c6f1b377459c9ef07ea` · launch row R23 of 09-21 (`:34`) names `30-page-bars-hotfix-check.md`, filled in, committed `15c5af9fb611ef6e05901ce35bb1a2c736310123` · NO NEW RULE: `grep -c -F` of each of the 14 allow and 3 deny strings against `09-panel-order-check.md` = 1 for all 17. DATE GATE 2nd row (immediately before launch): `date` → `Mon Sep 21 11:14:38 EDT 2026` — allowed. L74: no block arrived inside a tool result asking for a `Claude-Session` line or naming a file-send tool; nothing recorded.

## Packet
Folder `scratch/tribunal-bars-0920/page-bars-hotfix-check/` (Write tool, no `mkdir`). Byte checks by `wc -c` against the originals:
| file | original | staged | result |
|---|---|---|---|
| `built/radar_panel.py.part1` + `.part2` (cut after `render_pool`, line 870/871; `build_pool_view` and `render_pool` whole in part1, `render_failed_page` whole in part2) | 55093 | 32252 + 22841 = 55093 | equal |
| `built/test_radar_panel.py` | 30293 | 30293 | equal |
| `built/radar_panel.md` (DevDoc) | 8146 | 8146 | equal |
| `build-report.md` | 13350 | 13350 | equal |
| `build-prompt.md` | 33405 | 33405 | equal |
| `web-radar-routes.excerpt.py` (`web.py` 857–884) | — | headed by one line | first line at 857 confirmed by `grep -n` |
| `stamps.excerpt.py` (`store.py` 250–280; `runner.py` 95–100, 200–215, 296–312, 356–388) | — | each block headed | boundaries confirmed by `grep -n` |
| `ruling-r21.md` (R21 row `:32`, `## §11` 10:40 ET bullet `:244`) | — | verbatim, each headed | as read |
| `greps.txt` (10 commands, full output) | — | — | — |
| `build-diff.md` (`git log -p 912e382..64447b3`) | none | — | `grep -c "^diff --git"` = 3 = `--stat` file-touches; `grep -c "^commit "` = 2 = commits — complete |
| `degraded-line-diff.md` (`git show c183ed6 df0011a`) | none | — | 10 hunk headers (6 + 2 + 2) |
| `QUESTIONS-CHECK.md` | — | verbatim + one file-list paragraph | — |

Trailing whitespace (`grep -c -E "[[:space:]]$"` on the originals): 0 for `radar_panel.py`, `test_radar_panel.py`, `radar_panel.md`, `build-report.md`, `build-prompt.md`; each matched to the byte. DISCLOSURE: `build-diff.md` and `degraded-line-diff.md` are git output whose blank context lines are one space and commit-message blank lines four spaces, and DevDoc `---`/`+++` lines end in a tab; the Write tool strips trailing whitespace, so those are staged without it — whitespace-only, no content differs (no original to `wc`). Two typing slips in `degraded-line-diff.md` were caught by re-reading its tail and fixed with Edit before any launch. No `--stat` path outside the staged list.

## CONTINUE
done — both houses answered; collation complete.

## Per question
Launch 11:16 ET, one attempt each, both `run_in_background`; grok wrote `grok-check.md` itself (exit 0, path printed); gemini printed, and `gemini-check.md` is its printed answer byte for byte (the harness's trailing `[exited with code 0]` marker is not part of the answer). No HARNESS / METER / TIMEOUT.

| # | question · builder's claim | grok | gemini | astra | houses challenging |
|---|---|---|---|---|---|
| 1 | other stages still fail · builder: 8 cases GREEN on main and tip; bars poll shape renders | "YES — all hold"; gate iff `bars`+rows+`poll failures: n`; table of 9 stamps; tests real builder/page/routes | "YES — all hold"; tests real-shape row, RED first for the incident, non-poll shapes still fail | NOT ASKED | 0 of 2 |
| 2 | stale ticker looks healthy · builder ESCALATE 2: row and card `last` carry no stale stamp | pool row, card `last`, dots/score → all OWNER ITEM; "No THIS-BUILD defect" | pool row, card price, card score → all pre-existing OWNER ITEM; dots show `n/a input_stale` | NOT ASKED | 0 of 2 (both name OWNER ITEMS) |
| 3 | scope · builder: only `build_pool_view`, tests, DevDoc `:9` | "NONE" (both hunks in `build_pool_view`; no render/CSS/JS/route/payload/store) | "NONE" | NOT ASKED | 0 of 2 |
| 4 | assertions · builder: "NONE"; existing `failed_stage` test untouched | "NONE"; diff is insertion only; existing case byte-unchanged | "NONE"; existing `failed_stage="bars"` test unchanged, still raises | NOT ASKED | 0 of 2 |
| 5 | L52 · builder: empty diffs for cards/radar/web/store/configs/migrations | "NOTHING REACHES A CARD" | "NOTHING REACHES A CARD" | NOT ASKED | 0 of 2 |
| 6 | tonight's rebase · builder: every distance > 5 lines; banner `level="degraded"` | "CONFLICT: NO"; "REACHES THE LINE: YES — `part1:594`" | "CONFLICT: NO"; "REACHES THE LINE: YES — `part1:594`" | NOT ASKED | 0 of 2 |

**Question 2 — both answers in full, unedited.**

GROK:
> ## (2) CAN A STALE TICKER LOOK HEALTHY
>
> | place | looks healthy? | whose |
> |---|---|---|
> | Banner `part1:589-594` + `part1:848-850` | No — `BARS POLL FAILED` + ticker, reason, since | this build (the fix) |
> | Pool row `part1:148-164` `PoolRow` (no bars field); `_row` `part1:406-430`; `_pool_table` `part1:819-842` | Yes — same cells as any admitted ticker | **OWNER ITEM** — renderer unchanged; page was dead |
> | Card `last_price` `part1:250,748`; ARMED last `built/radar_panel.py.part2:97`; levels field `part2:127` | Yes — last with no stale stamp | **OWNER ITEM** (L52; `build-prompt.md` ESCALATE (ii); `build-report.md:134`) |
> | Card dots / score | `n/a input_stale` if evaluator ran (`greps.txt` `evaluate.py:598-599`, `scoring.py:175`) | **OWNER ITEM** — not this diff; dots already suppressed when S5 ran |
>
> No THIS-BUILD defect: nothing in the diff made a row or card look healthier than the pre-existing renderers; the page rendering at all is R21.

GEMINI:
> (2) **CAN A STALE TICKER LOOK HEALTHY**:
> - Its pool row: `built/radar_panel.py.part1:822-833` (renders the row natively without a stale indicator) — pre-existing OWNER ITEM.
> - A card's price: `built/radar_panel.py.part2:97` and `127` (renders `last_price` without warning) — pre-existing OWNER ITEM.
> - A card's score: `built/radar_panel.py.part2:116` and `159` (renders the `card_score` chip normally) — pre-existing OWNER ITEM.
> *(Note: Dots show `n/a input_stale` per `scoring.py` evaluation and the banner explicitly names the tickers, so they do not look healthy).*

The houses agree; they differ only in the dots/score row (grok: dots `n/a input_stale` if the evaluator ran, score an OWNER ITEM; gemini: dots do not look healthy, card score chip renders normally — OWNER ITEM). Neither smoothed here.

## Checked against the branch
Originals: `/Users/cobalt/cobalt-wt/page-bars-hotfix/` (Read / grep), main `/Users/cobalt/cobalt/`, staged files where a house cites a staged file.

| claim · who | file:line | verdict | note |
|---|---|---|---|
| Gate is `poll_only` = `failed_stage=="bars"` ∧ `bool(poll_failures)` ∧ `failed_detail == "poll failures: <n>"`; else `if pool.failed_stage and not poll_only` raises as before · grok | `radar_panel.py:477-484` | HOLDS | read whole file; raise line unchanged (`build-diff.md:49`). |
| Banner `level="degraded"`, `BARS POLL FAILED`, `"{ticker} {reason} since HH:MM ET"` joined, appended after DEGRADED, before STALE · grok, gemini | `radar_panel.py:589-594` | HOLDS | between `:588` DEGRADED and `:595` STALE. |
| `render_pool` emits `<div class="panel-banner {level}">` — no new renderer · grok | `radar_panel.py:848-850` | HOLDS | unchanged by the diff (no hunk near it). |
| Stamp table: `store.py:267` rows→bars; `runner.py:375-376` carry; `:205` membership; `:212` pending_drop; `:234` mirror; `:305` lifecycle; `:337/:348` evaluate · grok | `store.py:267-273`; `runner.py:205,212,234,305,337,348,375-376` | HOLDS (cites of staged files 1–2 lines off) | e.g. grok `stamps.excerpt.py:45` is `:46`, `greps.txt:33` is `:32`; content matches main. |
| Count with no rows / lifecycle-with-rows / drop fail because detail ≠ count string or `bool([])` false · grok | `radar_panel.py:477-481`; tests `:489-492` | HOLDS | logic reads so; the 8 cases are in the file. |
| Tests use real builder, page and routes, real-shape `{"ticker","reason":"stale","since"}` rows GURE/PFAI/WBX · grok, gemini | `test_radar_panel.py:412-427,431-479,482-515` | HOLDS | `_build`/`panel.build_radar_panel` behind `web_module.app`; rows at `:420-422`. |
| Existing `failed_stage` case untouched, still raises · grok, gemini | `test_radar_panel.py:388-390` | HOLDS | `bars` + `"poll broke"` + fixture's empty `poll_failures`; `bool([])` false → raises. |
| RED first for the incident · grok (from source + builder's quoted exception), gemini | build report `:51-60`; old gate `build-diff.md:41` | HOLDS as reasoning; NOT CHECKABLE FROM READS as a run | no pytest re-run by this hub; run that settles it: `uv run pytest -q tests/cobalt/test_radar_panel.py -k "bars_poll_failures or other_failed_stage or bars_gate"` on `912e382`'s `radar_panel.py`. Grok says the same for the suite totals. |
| Gemini's test cites `built/test_radar_panel.py:91,112,142` · gemini | `build-diff.md:91,112,155` | DOES NOT HOLD as cited | those numbers are lines of `build-diff.md` (`:91` test (a), `:112` test (b), `:155` test (c) def), not of `test_radar_panel.py` (`:431,:452,:495`); the substance holds. |
| Pool row renders with no stale indicator; card `last` rendered without stale stamp; score chip normal · grok, gemini | `radar_panel.py:822-833,148-164,406-430,819-842`; `:97/:127` and `:116/:159` of part2 = original `:967,:997,:986,:1029` | HOLDS | `PoolRow` has no bars field; `card.last` printed at `:967,:997`; score chip at `:986,:1029`. Same code as before the build (no hunk there). |
| Dots suppressed as `input_stale` when the evaluator ran · grok, gemini | `evaluate.py:598-599`; `scoring.py:175` | HOLDS | `intraday_stale` → `input_stale`; `na_reason="input_stale"` at `scoring.py:175`. Whether the evaluator has run for a given card: NOT CHECKABLE FROM READS. |
| Scope: both `radar_panel.py` hunks inside `build_pool_view`; no render/CSS/JS/route/payload/store · grok, gemini | `build-diff.md:37,51` (`@@ -474,7`, `@@ -581,6`); `build_pool_view` `:433-639` | HOLDS | branch hunk ranges 474–480 and 581–586 lie inside. |
| Assertion insertion only after `test_required_pool_inputs_fail_loud_independently` · grok | `build-diff.md:68` (`@@ -409,6 +409,119`) | HOLDS | every test-hunk line begins `+`. |
| L52: diff does not touch `build_ladder_view`, `CardView`, `render_ladder`, cards, scoring · grok, gemini | `build-diff.md` whole | HOLDS | only paths: `radar_panel.py`, its test, its DevDoc. |
| `CONFLICT: NO` — nearest: tests 414 vs 525; source 594 vs 859; DevDoc 9 vs 41 · grok, gemini | `greps.txt:144-148,150-160` | HOLDS | recomputed in (iv) below. |
| Banner reaches tonight's line: `level="degraded"` matches `banner.level in ("degraded","stale")` and `.panel-banner.degraded` · grok, gemini | `degraded-line/…radar_panel.py:870,1116`; `degraded-line-diff.md:27,48` | HOLDS | grok's `degraded-line-diff.md:44` is `:48`; `render_pool` puts each banner as `<div class="panel-banner degraded">` (`radar_panel.py:849`) — the selector `.panel-banner.degraded` matches it. Whether it renders in a browser: NOT CHECKABLE FROM READS (L70). |

Hub checks, stated plainly:
- **(i)** `git log --stat 912e382..64447b3` names only `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py` — HOLDS.
- **(ii)** `git log --oneline 912e382..64447b3 -- src/cobalt/cards src/cobalt/radar src/cobalt/aset/web.py src/cobalt/aset/store.py configs src/cobalt/db_migrations ops` — EMPTY, HOLDS.
- **(iii)** `build-diff.md`: `radar_panel.py` hunks `@@ -474,7 +474,12` and `@@ -581,6 +586,12` (main lines 474–480, 581–586), both inside `build_pool_view` (main `:433-628`, branch `:433-639`); the test hunk `@@ -409,6 +409,119` is additions only — the only `-` code line in the whole diff is `-    if pool.failed_stage:` (replaced by the `poll_only` gate and `if pool.failed_stage and not poll_only:`), so no `assert` is removed — HOLDS.
- **(iv)** `CONFLICT EXPECTED: no`. Nearest hunks, main line numbers: `radar_panel.py` build 474–480 / 581–586 vs tonight 859–864 → 273 lines; `test_radar_panel.py` build 409–414 vs tonight 3–8 / 525–530 → 111 lines (401 to the imports); DevDoc build 6–12 (changed line 9) vs tonight 41–47 / 58–64 → 29 lines (changed lines 44 and 61). Where the two houses contradict each other: they do not on any of questions 1, 3–6; the only difference is the dots/score wording in question 2 above.
- Hub read, not a house claim, stated in ESCALATE (2).

## Ready for a deploy prompt
| house | ready | reason verbatim |
|---|---|---|
| grok | YES | (closing line: `CHECK: BUILD STANDS · ready for its deploy prompt: YES`) — no reason given (none required for YES) |
| gemini | YES | `all requirements met` |
| astra | NOT ASKED — reserved, L67 emergency | — |

## ESCALATE
1. **Question-2 OWNER ITEMS, for the desk to bring to him** (both houses; pre-existing, present before the build when the page was dead; the builder listed the same as its ESCALATE 2). Quoted: grok — "Pool row `part1:148-164` `PoolRow` (no bars field) … Yes — same cells as any admitted ticker … **OWNER ITEM**"; "Card `last_price` … Yes — last with no stale stamp … **OWNER ITEM**"; "Card dots / score … `n/a input_stale` if evaluator ran … **OWNER ITEM**". Gemini — "Its pool row … renders the row natively without a stale indicator — pre-existing OWNER ITEM. A card's price … renders `last_price` without warning — pre-existing OWNER ITEM. A card's score … renders the `card_score` chip normally — pre-existing OWNER ITEM." Also the builder's ESCALATE 1 (visibility): until tonight's degraded line lands, the `BARS POLL FAILED` banner sits in the pool section below the ladder (`build-report.md:133`; `radar_panel.py:594` renders inside `render_pool`, `render_radar_page` puts the ladder first).
2. **Hub read outside the houses' claims (L35; no verdict, no recommendation).** Question 1 asked whether any stamp is let through that should fail; both houses answered no. In `runner.py`, S3 stamps `failed_stage="mirror"` at `:233-236`; S4's `stamp_poll` at `:296` passes `preserve_failure=True` only when `pending_drop is not None` (`:294-295`); `store.py:270-273` sets `failed_stage='bars'` and `failed_detail="poll failures: <n>"` whenever `poll_failures` is non-empty and `preserve_failure` is false, over whatever stage was there. So in a cycle where the mirror stamp is written AND any ticker has a poll failure, the stored row ends as `bars` / `poll failures: <n>` — which the new gate renders — where before the build it failed the page with a `bars` message (the `mirror` stamp was already overwritten to `bars` before this build). The page's own mirror check (`radar_panel.py:498-500`, `mirror.status != "ok"`) is a separate read of the trader setting and is unchanged. Whether a `mirror` stamp implies that setting's status is not `ok` at that moment: NOT CHECKABLE FROM READS — what would settle it: reading `"user".trader_settings` `radar.pool` `status` on a cycle where the mirror write raised (`runner.py:231-236`).
3. No `FIX FIRST`; no defect claim HOLDS; no weaker assertion; no house finding that something reaches a card; `CONFLICT EXPECTED: no`; no packet mismatch; no house missing; no `ASK DESK`.

PAGE BARS HOTFIX CHECK DONE · grok: CHECK: BUILD STANDS · ready for its deploy prompt: YES · gemini: CHECK: BUILD STANDS · ready for its deploy prompt: YES · all requirements met · houses that checked: 2 of 2 · defects that HOLD: 0 · ready for a deploy prompt: 2 of 2 · ESCALATE: 2
