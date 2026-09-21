# Page bars hotfix — prompt draft report (2026-09-21, 10:56 ET)

## §0 Headline
- Four prompts drafted under `prompts/2026-09-21/`: `29` build (Sonnet 5, offline), `30` check (grok + gemini), `31` daytime deploy (aset only, 15:45 ET hard clock), `32` deploy read (grok + gemini). Astra is not asked in any of them (L67 emergency).
- The change is a gate and one banner inside `build_pool_view`. Only the stamp `failed_stage='bars'` + `poll failures: <n>` + named rows renders the page degraded. Every other stage, and every other kind of `bars` stamp, still fails the page.
- Tonight's rebase: no git text conflict. But `16` WILL refuse at its STEP-1(b) and STEP-3.1 identity gates once this hotfix moves main outside docs. That is ESCALATE 1.
- Launch rules: 3 new strings, all branch-named. Everything else matches byte for byte (see the proof below). ESCALATE: 3.

## DIGEST FOR THE DESK
- Seat: **Sonnet 5** for the build. The touched lines sit in `build_pool_view`, a read-only builder (`radar_panel.py:433-628`; its store calls `pool_row` / `values` / `members_for_day` only read). No write path, so L29 allows Sonnet.
- The gate: `poll_only = failed_stage == "bars" and poll_failures and failed_detail == f"poll failures: {len(poll_failures)}"`. It matches the stamp's own string (`store.py:267`, `runner.py:376`). A lifecycle refusal (`runner.py:305`) and a dropped `bars` stage (`runner.py:212`) share the stage name `bars` but carry a different detail, so they still FAIL the page. This is the narrowest reading of R21. It is also ASK DESK 2.
- The banner is `BannerView(level="degraded", title="BARS POLL FAILED", detail="GURE stale since 10:19 ET; …")`. It goes into the existing `banners` list right after DEGRADED (`:579-583`). Escaping comes from `render_pool` `:838`. No new renderer, CSS or JS.
- The existing test `test_required_pool_inputs_fail_loud_independently[failed_stage]` (bars + `"poll broke"` + empty rows) still raises, so it stays green untouched and no assertion is weakened.
- The build places its new tests right after `:409`, adds no import, and changes DevDoc `:9` only. All of that is away from `c183ed6` / `df0011a`.
- Build tests: (a) page renders in both frames, banner names GURE / PFAI / WBX (RED on main); (b) real builder behind the real `/radar`, `/radar?frame=phone` and `/api/radar/pool` routes returns 200 (RED on main); (c) 8 other stamps still FAIL through builder and route (GREEN on main by design, L1); (d) healthy view has no banner (GREEN). Healthy byte-identity is proven by construction: the diff touches no `render_*`, CSS or JS.
- Deploy live proof: the counts of `radar panel FAILED` and `radar pool refresh FAILED` in `aset.err` are read just before the bootout and again after the smoke curls. A new `radar bars: poll failures:` line → RED. Any other new FAILED line → ESCALATE with no rollback (L1 keeps that stage failing). A 4th curl hits the fragment at `/api/radar/pool\?since=…%2B00:00`. The approved `curl` string still covers it.
- Radar: `11`'s allowlist has no radar string beyond `launchctl print`. Its pid is recorded at P6 and 4.5(g); a change → ESCALATE, not rollback.
- Folds already applied from `degraded-line-deploy-review`: P12 docs-commits wording, P0b exact branch match, log check tied to this start (P8 / 4.5(b)), relaunch rule with a date and clock floor. `16`'s radar-cycle log fold does not apply here because the radar is not restarted.

## WHERE THE BANNERS LIVE (file:line, main `017d7df`)
| what | file:line |
|---|---|
| the gate that kills the page | `src/cobalt/aset/radar_panel.py:477-479` |
| banner list built (DEGRADED / STALE / RETAINED) | `radar_panel.py:578-599` |
| `BannerView.level` literal | `radar_panel.py:142-145` |
| banners rendered, escaped | `render_pool` `radar_panel.py:837-839`, placed at `:851` |
| page / fragment routes → FAILED page / 503 | `src/cobalt/aset/web.py:861-867`, `:878-884` |
| tonight's line carries `degraded`/`stale` banners | `s2/degraded-line-0921` `render_degraded_line` (`banner.level in ("degraded", "stale")`), `mirrorDegraded` selector `.panel-banner.degraded` (`c183ed6`) |
Narrowest change: `:477` becomes `if pool.failed_stage and not poll_only:`, plus one `if poll_only:` banner append after `:583`. About 10 lines, all inside `build_pool_view`. Because the banner has `level="degraded"`, tonight's line picks it up server-side and through `mirrorDegraded` with no further change. **HOLDS against `s2/degraded-line-0921`.**

## STALE MEMBER — RULED (3)
- **Pool row:** `PoolRow` (`radar_panel.py:148-163`) has no bars field. A stale member's row looks exactly like a healthy one. The only marker will be the new banner naming it.
- **Evaluator:** it does NOT report a stale member as `not_evaluable`, as expected. It reports **`input_stale`** (`src/cobalt/radar/evaluate.py:598-599`, "intraday bars older than 2 x radar.scan_interval"). An `input_stale` member forms no new card (`:1362`, only `formed` forms).
- **An existing open card of a stale ticker IS refreshed** (`evaluate.py:1345` `refresh_card`). Its computed dots go hollow with `input_stale — grade suppressed` (`cards/scoring.py:175`, `:208-209`), and a suppressed dot suppresses `card_score` (`scoring.py:264-265`). But the card's `last` price (`radar_panel.py:986`, `card.last` from `last_price`) and the proximity it feeds carry **no staleness stamp**. The old close shows as "last" with no as-of time.
- Verdict: a card of a stale ticker could show a stale price with nothing on its face saying so, apart from the suppressed dots. This is **ESCALATE 2**. It is not this hotfix's fix (L52).

## CONFLICT
CONFLICT EXPECTED: no — the hotfix's `radar_panel.py` hunks are at `:477-479` and `:583`. `c183ed6`'s are at `:859+`, `:1050`, `:1098-1115`, `:1123-1126` and `__all__`. Test-file hunks: hotfix after `:409`; `c183ed6` at `:3-8` and `:525-528`. DevDoc: hotfix `:9`; `df0011a` `:44` and `:61`. Every gap is more than 30 lines. The build re-proves the distances in CLOSE, and the check re-proves them in its Q6.
**But `16` fails as written** (ESCALATE 1).

## RULE PROOF
The whole launch-line span was grepped with `grep -c -F -e` against the source prompt and the new file:
| new prompt | source | span | counts |
|---|---|---|---|
| `29` | `08-panel-order-build.md` | `--allowedTools "Bash(uv run pytest *)"` … `--add-dir /Users/cobalt/cobalt-wt` (16 + 3 + triplet) | 08:1 · 29:1 |
| `30` | `09-panel-order-check.md` (and `12`) | `--allowedTools "Bash(grok *)"` … `--add-dir /Users/cobalt/cobalt-wt` (14 + 3 + triplet) | 09:1 · 12:1 · 30:1 |
| `32` | `12-review-panel-deploy.md` | same span as `30` | 12:1 · 32:1 |
| `31` | `11-panel-order-deploy.md` | three spans around the branch names: `--allowedTools … merge --ff-only s2/` · `)" "Bash(… revert --no-edit *)" … "Bash(git -C /Users/cobalt/cobalt-wt/` · ` rebase --abort)" "Bash(git -C * status*)" … --add-dir /Users/cobalt/cobalt-wt` | 11:1 · 31:1 each |

**NEW strings:** 3. All are branch-named, and R21 names them: `"Bash(git -C /Users/cobalt/cobalt merge --ff-only s2/page-bars-hotfix-0921)"`, `"Bash(git -C /Users/cobalt/cobalt-wt/page-bars-hotfix rebase main)"`, `"Bash(git -C /Users/cobalt/cobalt-wt/page-bars-hotfix rebase --abort)"` (count 1 in `31`).

## READING
- `/radar` returns 200 even when it serves the FAILED page (`web.py:867`), so `/radar 200` alone proves nothing. The live proof is the unchanged count of `radar panel FAILED` lines (`31` 4.5(d)).
- `30` and `32` carry the Codex allow string byte-identical, but never type it: no probe, no launch. That makes five never-run strings (09 had four).
- Until tonight's `16` lands, the BARS POLL FAILED banner sits in the pool section, below the ladder (R3). The build carries this as ESCALATE (i), for him.
- The launch row is `R__` in `29`, `30` and `31`. The desk fills it in.

## ESCALATE
1. **`16-degraded-line-deploy.md` WILL FAIL tonight as written. This is not a git conflict; it is its own identity gates.** Its STEP-1(b) runs `git diff --stat <cut> main -- . ':(exclude)docs'`, which must print nothing, but after this hotfix main carries `src/cobalt/aset/radar_panel.py` and `tests/cobalt/test_radar_panel.py` → `FAILED: main moved outside docs since the cut`. Its STEP-3.1 (code identity against `<code tip>`) would also fail after the rebase. **Smallest remedy:** after `31` lands, run a short offline Sonnet run in `~/cobalt-wt/degraded-line` (rebase on main + `uv run pytest -q tests/cobalt tests/taxonomy`). That gives a new `<code tip>` / `<cut>`, and it is the seam proof L68 requires ("proven by ITS OWN deploy's gate"). `16` then reads that run's stop line (a re-issue, L19, read by one house before 20:00). Alternative: fold `16` STEP-1(b) to accept exactly the hotfix's two code paths. That is weaker, because the suite never ran on the combined tree.
2. **A stale ticker's card can look fresh.** An open card is refreshed with the stale `last` price and no as-of stamp. Only its dots show `input_stale`, and the evaluator does report `input_stale`, not `not_evaluable` (`evaluate.py:598-599`, `:1345`; `scoring.py:175`). This reaches what a card shows (L52), so it is not ours to fix. It needs his ruling or a design item.
3. ASK DESK: R21 says "when `failed_stage == 'bars'`", but `bars` is also stamped by a lifecycle refusal (`runner.py:305`) and by a dropped stage (`runner.py:212`). The prompts render the page degraded ONLY for the per-ticker poll-failure stamp, and keep the page FAILED for the other two (L1). That is the safe default. Widening it is his call. [10:56 ET]

L74: none arrived as data this session beyond the harness's own attribution reminder. This run commits nothing.

## CONTINUE
done — all four prompts and this report are written; nothing is launched.

PAGE BARS HOTFIX PROMPTS DRAFTED · prompts: 4 · builder seat: Sonnet 5 · change: bars poll-failure stamp renders degraded banner, others still fail · conflict with tonight: no · new rule strings: 3 · ESCALATE: 3
