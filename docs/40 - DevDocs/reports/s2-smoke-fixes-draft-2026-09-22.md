# S2 SMOKE FIXES DRAFT 2026-09-22

Seat `s2-smoke-fixes-draft-0922` (Opus 5.5), reads + drafting, no code / DB / git write. Prompt: `docs/40 - DevDocs/prompts/2026-09-22/75-draft-s2-smoke-fixes.md`. Run 21:34–21:44 ET (`date`). Wrote: `prompts/2026-09-22/76-s2-smoke-fixes-build.md`, this report.

## §0 Headline

- **S2 CAN still close 09-23 — but only on this path:** `76` built + checked (Grok · Gemini · Opus 5.5) by the afternoon → deployed in the 20:00 pause with the setups stack → a green 21:10 replay → the smoke look **AT OR AFTER 21:40 ET, not 21:20** (the smoke's `last_trading_day` waits for 21:10 + the job's 1800 s timeout; a 21:20–21:39 look expects the PREVIOUS day and reads K7/K8.1/K9.2/K9.5 red on a green run).
- Movers bug: 14 never-traded rows at the tail of an 11,648-row export have an EMPTY `Change` cell; the parser reads every row before taking the top 20, so a row that would never be stored kills the night. Fix = those rows are counted and logged, not fatal (F1).
- K4.4's check was wrong at birth (the API's required `since` is ruled, 09-15); K3 counts a designed NULL (sticky name, no ranking that scan) as a defect — fix gated on one read-only desk query.
- Two owner items (09-21/09-22 miss-line gap; 5 `_inflight` files). ESCALATE: 4.

## CLASSIFICATION

Every red K row of `s2-smoke-2026-09-22.md` and every ESCALATE of `s2-smoke-look-2026-09-22.md` (L75).

| finding | class | evidence (quoted output · code) | row in `76` |
|---|---|---|---|
| ESC 1 · K7 · K8.1 — replay FAILED `movers: Change '' is not a percentage` | **FIX** | `logs/replay.err` `2026-09-22 21:10:05.839 … SourceFailure: movers: Change '' is not a percentage`. Retained export `data/radar-cache/2026-09-22/movers-gainers-211004.csv`: 11,648 data rows; 11,634 carry a `%` Change, **14 carry an EMPTY cell** (counted by two regex greps that sum to 11,648), all at export positions 11,635–11,648 — unit shells, new funds, one no-price stock; `Volume` present (often 0). `movers.py:125-128` raises on any non-`%` cell; `:183-193` parses EVERY row before `rows[:top_n]` (`:209`). Losers export never fetched (gainers failed first) — its blank placement is NOT KNOWN. **Design line:** `movers.py:24-32` "a COLUMN is never missing … Only a row's own CELL may be blank" (written for `Asset Type`; silent on `Change`). An empty `Change` = "no change reported" (never traded), a legitimate per-record blank → counted + loud per side (L9), not a dead night; a whole side of blanks still FAILS (L1). The fixtures missed it because they are the TOP 60 rows (`_cut_p4_fixtures.py:303-305`) — the L45 gap. | F1 + F1-FX |
| ESC 2 · K3 — 66 of 301 post-deploy admitted rows with NULL `rank_metric` | **FIX (check)**, gated | Output `post_deploy_admitted=301, metric_missing=66, value_null=66, rescanned_metric_missing=0`. The INSERT path always writes a metric (ADMIT → `value_of()` from `_ranked`, which always sets one, `pool.py:168-178`, `:386-391`; `store.py:145-161`). BUT a sticky RETAIN of an open member that is no longer a candidate gets `rank=None` and `(None, None)` (`pool.py:328-330`, `:366-378`) and `store.py:86-94` overwrites `last_rank`, `rank_metric`, `rank_value` with NULL — by design (`pool.py:50-54` "None where no ranking happened"). K3's first set grades rows FIRST SEEN after the cutoff by their CURRENT pair, so it reads that later RETAIN as an INSERT defect. P4 plan `:243` (Astra R1-19/R1-24): "a genuinely missing metric, is not a K3 failure; only a write-path defect is." Mechanism is from code reading → the desk's ONE read-only query (`76` STEP-D) proves it: `ranked_without_metric = 0` → F3 builds; `> 0` → a real defect, F3 skipped, brought back (L70). Radar deploy was 09-19 15:14 (Saturday, idle) → all 301 were written by P4 code (`deploy-p4-2026-09-19.md:810,823`); `pool.py`/`store.py` unchanged since. | F3 |
| ESC 3 · K4.4 — `/api/radar/pool` HTTP 422 `since is required` | **FIX (check)** | `web.py:870-875` + `radar_panel.py:370-373` are `ab28cb5` **2026-09-15** (S2-P3), RULED in `plan-s2-p3-2026-09-14.md:65` (Astra R2-1: missing `since` "rejected, not defaulted"). K4.4 written later (`f850dec`, 09-19) from `plan-s2-p4-2026-09-15.md:227`, which omits `since`. Not stale — wrong at birth; the endpoint is right. The smoke look's "landed 2026-09-21" is WRONG (L35). URL needs percent-encoding (an ISO `+` decodes as a space). | F2 |
| K9.2 · K9.3 · K9.5 · K9.6 | **NOT REAL** | `last_result.movers_by_side={}` — red by design until the first successful replay (`deploy-p4-2026-09-19.md` §6.5). Clear with F1 + a green run. | — |
| ESC 4 · K10.1 · K10.2 — 09-21 DRC miss line never written | **OWNER ITEM** | 09-21's run died on `radar.benchmark` before any step; 09-22's died in movers. **Not a blocker for the S2 close:** K10 reads `DRC-{last_trading_day}` — a look ≥21:40 on 09-23 reads `DRC-2026-09-23`. **No backfill exists by design:** `--date` needs a retained export for BOTH sides (`movers.py:372-394`, R1-20); 09-21 has none, 09-22 has gainers only. | — (FOR DEJAN 1) |
| ESC 5 · K17 — `cobalt validate` exit 1, 5 files in `docs/_inflight/` | **OWNER ITEM** | `placement/check.py:85,116`; `docs/PLACEMENT.md:28-33` (README-only, permanently). The 5 are gitignored working files (`git ls-files docs/_inflight` = README only) and are READ by live prompts (`33`, `40`, `41`, `51`, `05` among others). Moving them can break a running build. | — (FOR DEJAN 2) |
| NEW N1 — the smoke look's clock | **OUT OF SCOPE** (desk timer) | `smoke/checks.py:161-177`: `last_trading_day` = latest day whose 21:10 occurrence + `timeout_s` (1800) has passed. Tonight's look ran 21:28 → `last_trading_day: 2026-09-21` (`s2-smoke-2026-09-22.md:9`). Tomorrow's look must start ≥21:40:00 ET. | — (desk) |

Counts: FIX 3 build rows (covering K3, K4.4, K7, K8.1) · NOT REAL 4 · UNPROVEN 0 (K3's gate would turn it into a NEW finding, never carried as a defect) · OUT OF SCOPE 1 · OWNER ITEM 2.

## DIGEST FOR THE DESK

1. `76` = offline Opus 5.5 build, NEW worktree `~/cobalt-wt/s2-smoke-fix` on `s2/smoke-fix-0922` off `main`. Desk BEFORE launch: (a) his word on the ONE NEW USE (cutter string); (b) STEP-D — ONE read-only prod query, paste `K3 PROOF: metric_missing <a> · unranked_retained <b> · ranked_without_metric <c> [time]` into the launch row; (c) `worktree add`, fill BASE TIP + `R__`, commit, launch.
2. F1: blank `Change` → unranked, counted in `movers_by_side.<side>.unranked`, one WARNING per side; `expected = min(top_n, exported − unranked)`; non-blank junk still fails; zero ranked rows fails. Rank = position among ranked rows (covers an unknown losers placement).
3. F1-FX: new cutter mode `movers-blank` cuts header + top 25 + every blank row from tonight's retained export into `movers-gainers-blank-change.real-shape.csv` (L45).
4. F2: K4.4 `?since={cutoff}` + a percent-encoding `render_url` for http checks only.
5. F3 (gated): K3's graded counters add `last_rank IS NOT NULL`; `unranked_retained` printed as evidence.
6. Stop line: `S2 SMOKE FIX BUILT <tip> | on <base> | offline <p>/<f> | with-DB: OWED (68) | RESTARTS: <tool line> | F3: … | tests added: <n> | ESCALATE: <n>`.
7. RESTARTS: derived by `cobalt jobs restarts` at CLOSE (L42). Expected none — `com.cobalt.replay` is a one-shot and picks up merged code at 21:10; `cobalt smoke` is an operator command. The tool's line governs.
8. CHECK prompt owed (not drafted): `77`, `70`'s shape (`setups-check-r2r3`) re-pointed to `<base>..<tip>` of `s2/smoke-fix-0922`, Grok · Gemini · Opus 5.5 (Codex out until 09-26), read-only strings.
9. Deploy: joins tomorrow's ONE stacked set (L43/L68) with the setups branch if both are checked. Merge + residents inside 20:00–21:00; live before 21:10. The smoke look at ≥21:40.
10. Risk: the replay has NEVER got past movers live (`steps_done: []` both nights), so cards → miss line → movers i1 archive run live for the first time tomorrow. A third, different failure is possible. The first live losers export is also untested (F1 covers blank placement, not other shapes).

## RULE PROOF — `76`'s launch line vs the precedent

| part | `76` | precedent | verdict |
|---|---|---|---|
| 17 allow strings `uv run pytest *` … `COBALT_ENV=dev uv run pytest *` | present, in order | `33-setups-fix-r3.md` / `48-drc-d1-build.md` | `grep -c -F` of the joined 17-string run = 1 in `76`, 1 in `48` (21:4x) |
| 3 denies + `--add-dir` triplet | present | `33` | joined-run `grep -c -F` = 1 in `76`, 1 in `33` |
| `.env` pair | ABSENT (offline, nothing to re-point) | `48` / `72` carry a re-pointed pair | dropped, nothing added |
| `"Bash(uv run python tests/fixtures/replay/_cut_p4_fixtures.py*)"` | added | `prompts/2026-09-19/24b-p4-fund-rule.md` (byte for byte, `grep -o`) | NEW USE of a precedented string |
| `--model claude-opus-5-5 --permission-mode auto` | yes | `48`, `72` | same |
| worktree creation | desk runs `worktree add -b … main` before launch | `cto-2026-09-22.md` R31 (handicap-h1), `48` | same shape |
| differs | prompt path, `--remote-control s2-smoke-fix-0922`, cwd `~/cobalt-wt/s2-smoke-fix` | — | — |

NEW strings:
- `"Bash(uv run python tests/fixtures/replay/_cut_p4_fixtures.py*)"` — builder, NEW USE (precedent `prompts/2026-09-19/24b-p4-fund-rule.md`).
- Desk, read-only, STEP-D: `COBALT_ENV=production uv run cobalt db query --side system --prod --format json 'SELECT count(*) FILTER (WHERE rank_metric IS NULL) AS metric_missing, count(*) FILTER (WHERE rank_metric IS NULL AND last_rank IS NULL) AS unranked_retained, count(*) FILTER (WHERE rank_metric IS NULL AND last_rank IS NOT NULL) AS ranked_without_metric FROM system.radar_membership WHERE entered_at IS NOT NULL AND first_seen_at >= TIMESTAMPTZ '"'"'2026-09-19T15:11:42-04:00'"'"''` — the smoke seat's own command shape; listed in case the desk's allow set lacks it.
- Desk: `git -C /Users/cobalt/cobalt worktree add -b s2/smoke-fix-0922 /Users/cobalt/cobalt-wt/s2-smoke-fix main` — R31's shape re-pointed.

## FOR DEJAN

1. **The two nights with no miss line (09-21, 09-22).** The replay died before writing them, and they cannot be rebuilt: the rebuild needs both of that day's mover files, and neither night saved both. This does NOT block closing S2 — tomorrow's check looks at tomorrow's note. **A:** accept the two nights as recorded gaps (recommended). **B:** ask for a design that can rebuild a lost night from another source — its own design lane and tribunal, not before S2 closes.
2. **Five working files in `docs/_inflight/`** (DRC spec + values, setups assumed values, defs gap table, trading stats). The rules say that folder holds only its README, so `cobalt validate` — one of the S2 checks — fails. Live builds read those files where they are. **A:** leave them for now and run tomorrow's check with the rule's own "deliberate in-flight window" switch on; move them at the 09-23 close (recommended — nothing running breaks). **B:** move them into their proper folders now and re-point the prompts that read them; a build running tonight may fail on a missing file.

## ESCALATE

1. `ASK DESK:` the smoke look for the S2 close must start ≥21:40 ET on 09-23 (N1). The 75 prompt's "smoke look after 21:20" would read red on a green night. [21:44]
2. The smoke look's claim that `since` "landed 2026-09-21" is wrong: `ab28cb5`, 2026-09-15, ruled P3 plan R2-1 (L35 — corrected here, not carried).
3. K3's F3 depends on STEP-D. If `ranked_without_metric > 0`, K3 stays red, S2 cannot close 09-23, and it becomes a new finding for a radar-side fix (L70).
4. The replay's cards / miss-line / archive steps have never run live. A green movers step tomorrow is the first live test of the rest. No dry run is proposed here: a production dry run fetches Finviz and the 20:30–21:10 window belongs to the archiver (L53).

MEMORY: [stated 2026-09-22 · Code] The S2 smoke's `last_trading_day` waits for replay occurrence 21:10 + `timeout_s` 1800 → a smoke look before 21:40 ET grades the previous day; the S2-close look runs ≥21:40.
MEMORY: [stated 2026-09-22 · Code] Movers fixtures cut from the TOP of an export can never show tail-row shapes (blank `Change` on never-traded listings) — a cut that keeps only the head is not the whole real shape (L45).

## CONTINUE

Done. Next (desk): L35 read of `76`; his word on the NEW USE; STEP-D; worktree add; launch; then draft `77` (check).

S2 SMOKE FIXES DRAFTED · FIX: 3 · NOT REAL: 4 · UNPROVEN: 0 · OUT OF SCOPE: 1 · OWNER ITEM: 2 · new rule strings: 3 · S2 by 09-23: possible · ESCALATE: 4
