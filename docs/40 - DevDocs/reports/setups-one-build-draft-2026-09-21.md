# SETUPS ONE BUILD — draft of build + check prompts (2026-09-21)

Seat `setups-one-build-draft-0921` · Opus 5 · 17:53–18:2x ET · reads only; wrote `65`, `66` and this report; nothing launched, nothing committed. Three desk additions were folded in mid-run, each checked against its committed desk row: R45 (17:57, ADDING-A-SETUP), R46 (18:05, code checks seat Sol + Opus) and R49 (18:14, his "Approved" for the two seat strings, used byte for byte). R47 (18:09, one stacked deploy per evening) was read from the desk file.

## §0 Headline

- **Drafted:** `65-setups-one-build.md` (Opus 5, no auto mode, ONE branch `setups/seven-0921` in `~/cobalt-wt/setups-c1`, 9 steps in the FINAL's code order C1→C2→C3a→C3b→C4→C5→C6→C7→Lego) and `66-setups-one-check.md` (Sonnet 5 hub; Grok + Gemini + Sol + Opus 5, three required, per R46).
- **On/off dial: NO per-setup switch exists** (only the global `radar.cards_enabled`). No pure use of an existing mechanism gives one → OWNER / TRIBUNAL item; the build ships without it and says so.
- **R2-4: B (Fable) is the only text with no failed claim and no withdrawn sentence.** A carries the withdrawn "kept in the receipt" sentence; Astra's carries the withdrawn state order (K22 HOLDS against it). The desk's launch row picks. **R2-3:** the two reads B rests on HOLD on main, so A cannot be built as the radar is wired; X20 decides only whether B needs its migration.
- **Two blockers for production defaults:** the three `per_indicator` holes (F1) keep fashionably-late and vwap-continuation from forming, and every numeric assumed hole stays null until `Assumed Defaults.md` is written after the deploy. So on deploy night **only Rubberband can form in production.**
- **Estimates:** build ≈ 30 h of Opus, 6–10 relaunches, 3–4 calendar days. Check ≈ 3 h. **NEW approvals: 1**, a date extension of grok/agy for the check. `65` reuses `56`'s line; `66`'s seat strings are his R49. New rule strings: 0. ESCALATE: 10.

## (A) THE DIALS, and the on / off finding

Default source: **engine** = a committed row in `configs/cobalt/taxonomy/tunables.yaml` (system side; value ruled or null). **HIS** = his own per-trade row in the note's `tunables:<slug>` unit. **ASSUMED `A-nn`** = a row in the future `1 - Trading/Assumed Defaults.md` unit `tunables:assumed`. An assumed row starts `source: assumed`, becomes `ruling` when he rules it, and its number never enters committed config ([R2F-07], [R2F-09]). **conv.** = a convention: a `label` row, value = the rule the code implements. Cheat-sheet pages come from the gitignored companion. **No value appears here** (L32).

| setup | dials (key · source · where he changes it) | inside the standard routine after this build? |
|---|---|---|
| rubberband | `bars_cleared` · HIS (`Rubberband.md:48`, unit `:111-136`) · his note · `stop.buffer` · engine (`tunables.yaml:32`) · engine row by ruling · `extension.path_b_atr`, `extension.path_a_volume_ma_bars`, `extension.path_a_volume_sigma`, `extension.leg_base` · engine (`:91-128`) · `range_break.htf_range` · engine (`:130`) · **A-01** conv. ASSUMED (`the_rubberband_scalp_cheat_sheet.pdf` p.1) · assumed note | **YES** — `bar_break` + `structural_extreme` re-registered; the direction line is generic (A-01) |
| hitchhiker | range-duration band · HIS (`Hitchhiker.md:37`, unit `:88-105`) · **A-02** `range.wick_ratio_max` engine hole, global (`:73-80`; hitchhiker sheet p.2) · `range.micro.touches_per_side`, `pivot.n` · engine · `stop.buffer` · **A-03**, **A-04** new null engine rows (A-04: hitchhiker p.1; A-03: no sheet) · **A-05** conv. (`9 EMA.pdf` p.2, visual) · **A-06** conv. (hitchhiker p.1) · **A-07** new null row (hitchhiker p.1) | **YES** — `range_break`, `consolidation_low`, D1–D3 atoms, all generic |
| backside | HIS row (unit `Backside Scalp.md:144-161`) · `extension.backside_hh_min` / `_hl_min` · engine (`:139`, `:148`) · `stop.buffer` · **A-01** (`back$ide_cheat_sheet.pdf` p.1) · **A-03**, **A-04**, **A-05** · **A-08** new null row (rubberband sheet p.1) · **A-11** new null row (no sheet) | **YES**, if X10 passes. If it fails, the FINAL offers two fixes and picks neither → ASK DESK at that point |
| fashionably-late | no `tunables:` unit in the note · **A-09** `flat_threshold.ema9`, **A-10** `flat_threshold.vwap` — engine holes, **`per_indicator`** (`:185-201`; FL sheet p.2 / p.1) · **A-01**, **A-05**, **A-08**, **A-11**, **A-12** conv. (`First VWAP Pullback.pdf` p.2, visual) · stop from the note (`Fashionably Late.md:47-51`) | **YES as bricks; BLOCKED at defaults by F1** — the settled reader cannot fill `per_indicator` holes |
| nine-ema-scalp | HIS row (unit `9 EMA Scalp.md:98-115`) · **A-05** · **A-13** conv. (`9 EMA.pdf` p.2) · **A-14** conv. (p.1) · **A-15** conv. (p.1; reuses `extension.path_b_atr`) · `stop.buffer` | **NO — ONE NAMED SPECIAL CASE:** `catalyst_ref` is served by the `A-13` resolver, which stands in for catalyst data Cobalt does not have (FINAL §6). It is registered in `ATOMS` by atom name, never by trade name, and `ADDING-A-SETUP.md` must name it. The rest is generic |
| vwap-continuation | HIS row (unit `VWAP Continuation.md:99-116`) · `trendline.min_pivots` · engine (`:60`) · **A-16** `dist.k.vwap` engine hole, **`per_indicator`** (`:203-210`; VWAP Continuation p.1) · **A-03**, **A-05**, **A-12** · **A-17** conv. (second-chance p.1, hitchhiker p.2) · **A-18** conv. (VWAP Continuation p.1) · `stop.buffer` | **YES as bricks; BLOCKED at defaults by F1** |
| second-chance | HIS row (unit `Second Chance Scalp.md:170-189`) · **A-19** `range_break.failed_trap_bars` engine hole, **global**, fillable (`:157-164`; SC p.2) · **A-03**, **A-17** · **A-20** new null row (SC p.1) · **A-21**, **A-22** conv. (SC p.2) · **A-23** conv. (SC p.1) · `stop.buffer` | **YES** — `sequence`, `turn_candle`, RangeBreak lifecycle, events |
| all | `radar.cards_enabled` (`settings/card.py:63`, `:151`) · `card.curves`, `card.proposed_key` · `"user".trader_settings` via `cobalt settings load` (his hand) | global, not per setup |

**Per-setup "discoverable or not": NONE exists today.**

Evidence:
- The only switch is global: `radar.cards_enabled` (`settings/card.py:4`, `:63`, `:151`).
- `TradeDef` has no enabled or status field (`trade_def.py:739-768`).
- A note's frontmatter `status:` is DERIVED and never trusted. A `draft` on a finished def is a warning, not a switch (`vault_loader.py:51-57`, `:238-254`).
- The stage evaluates every loaded def (`evaluate.py:1285-1291`). The store loads every `trade_defs` row (`taxonomy/store.py:126-131`). The registry has no flag (`registry.py`).

The only existing way to take a setup off the radar is to empty or break its Definition unit. It then becomes a DRAFT (`vault_loader.py:379-429`) and `sync` deletes it (`store.py:14-21`). That is an edit of his note (L65) and destroys the def in place, so it is not a dial.

**Smallest lawful candidate, NOT a pure use.** A per-trade row in the def's own `tunables:<slug>` unit would travel through the existing reader (`vault_loader.py:257-284`) and the existing sync. But the stage would need new code to read a new key convention. It would also need a meaning chosen: skip the evaluation entirely, or evaluate and publish the seam row but form no card ("dark", the `cards_enabled` idea per setup). That choice is design. → `## OWNER / TRIBUNAL` + ASK DESK. `65` builds nothing for it, and says so in its ESCALATE (viii) and in `ADDING-A-SETUP.md`.

## (B) R2-3 and R2-4, laid out

**R2-3 (FINAL §8; gates C2's store). B rests on three reads the hubs never checked. I re-read them on main `75e65d0` (a drafter's read, not a hub check):**

| read | file:line | on main |
|---|---|---|
| R1: the radar merges engine rows with user rows read back from the DATABASE (bare `TunableRow`, no reader identity) | `evaluate.py:1185-1187`; `taxonomy/store.py:114-132` | HOLDS |
| R2: that table has ONE writer, `sync`, which DELETEs absent keys | `taxonomy/store.py:140-213` (DELETE `:200-204`) | HOLDS |
| R3: `tunables.slug TEXT NOT NULL REFERENCES trade_defs(slug)` | `taxonomy/migrations/0001_trade_defs.sql:63` | HOLDS as DDL; runtime = X20 |

So A's predicate ("a row from `load_assumed_tunables` may supply…") has nothing to test at the radar's merge site. Reader identity is not stored. As worded, A either never delivers the rows to the radar or becomes B without B's field-only predicate. X20 (sync with a NULL-slug row) decides only whether B carries its migration.

`65` STEP-2 runs X20 first, quotes R1–R3 on the branch, and applies this table:
- R1 and R2 hold, X20 = violation → **B with the migration**.
- R1 and R2 hold, X20 = accepted → **B without it** (X20's own row: "the migration leaves C2").
- R1 or R2 fails → **A**.

Both texts are quoted whole in `65`.

The migration's home is `db_migrations/` (FORWARD + REVERSE, with a rollback), NOT `taxonomy/migrations/`. `TradeDefStore.ensure_schema` runs every `*.sql` in that folder on each load (`taxonomy/store.py:82`), so a rollback file there would run forward. Its number must be above `bars/chunk-2-0920`'s unmerged `0012_bars_partitioned_parent` → expect `0013`.

**R2-4 (FINAL §2.1; gates C2's frame publication).** Only the hub tables' file-checked rows are used (`setups-tribunal-r2-2026-09-21.md` `## Checked against the files`; Fable R2 `## Withdrawn from round 1`):

| text | rows that HOLD | DOES NOT HOLD | WITHDRAWN sentence in it | verdict |
|---|---|---|---|---|
| **A — Grok** (louder of two, `not_evaluable > input_stale > avoided > not_formed`, tie → long; both frames kept in the receipt; observations per frame) | K22 (against Fable's order, not Grok's), K23a, K24; G23 / A19 describe Grok's round-1 O2 having no publication rule | none | **yes** — "Both frames' evaluations are kept in the receipt" is the content of Fable R2 withdrawn #11 ("the other frame's evaluation is kept in the receipt", defeated by `evaluate.py:917-930`, `:1061-1065`). The FINAL excluded Gemini's R2-4.1 text for carrying that sentence. My read: the receipt holds inputs and snapshots, no evaluations (`evaluate.py:917-930`) | no failed claim; carries a withdrawn sentence |
| **B — Fable** (`by_side` internal; per-card decisions read the card's own side; neither forms → long frame always; observations once on real bars) | C9, G22 (one detail per evaluation); K22 (against the order B dropped); G25 (rvol and `atrs_from_open` are direction-agnostic; `htf_level_proximity` not addressed) | none | **none** — #10 and #11 are its round-1 sentences, replaced. Its round-2 cites were checked by no hub. My read confirms `evaluate.py:1329` (open-card lookup by `(member, md5)` alone) and `:1342` (the avoid that expires a card) | **no failed claim, no withdrawn sentence** |
| **ASTRA** (order `formed > avoided > input_stale > not_formed > not_evaluable`, tie → long; typed receipt artifact in the detail JSON) | A18 (the detail model is closed and has no frame identity, so this text needs a seam-model change), A19, A20a, A21; A20b UNVERIFIABLE | none of Astra's own | **yes** — the selection order is Fable's withdrawn #10, and K22 HOLDS against it (it publishes a formed long card when both frames form, which F-19 refuses) | carries a withdrawn sentence and a HOLDS row against it |

**The text with no failed claim and no withdrawn sentence: B.** `65` takes `R2-4 = <A|B|ASTRA>` from the desk's launch row and REFUSES to start without exactly one. It builds the named text plus the lines all texts agree on: exactly one side forms → that side; both form → `both_sides`; daily series and levels are mirrored. Where the chosen text conflicts with an agreed line, the agreed line is built and the conflict is escalated. A named test pins the `:1329` / `:1342` case under whichever text is built. Both R2-3 and R2-4 are the FIRST two questions of `66`.

## (C) FIXTURES

**Committed real-shape days: ONE trade date, two tickers.** FTFT forms; BGFI is stale by design (`tests/fixtures/radar/_cut_p2_fixtures.py:36-38`; `bars-rubberband.real-shape.json`, `daily-bars.real-shape.csv`).

| def | committed day on which it forms? | what `65` proves instead | expected pin |
|---|---|---|---|
| rubberband | relation path: YES, FTFT, 71 scans (proof test A/B). Full shape: NO — the day-1 HTF avoid covers FTFT (proof ESCALATE 2) | all four values on the relation path; full shape `avoided` on exactly the control's scans | `AWAITING_A_DAY` (full shape) |
| hitchhiker | unknown until D2/D3 exist; no read can say | if FTFT forms it, the four values; if not, `test_<slug>_path_*` on definition-written constructed series + `evaluable` | likely pinned |
| backside | unknown (D4) | same; X10 first | likely pinned |
| fashionably-late | only with a test-constructed config; F1 blocks production defaults | same, on the constructed config (L69) | `AWAITING_A_RULING: F1` (+ day) |
| nine-ema-scalp | unknown (D3 roles, A-13) | same | likely pinned |
| vwap-continuation | same as fashionably-late (F1) | same | `AWAITING_A_RULING: F1` (+ day) |
| second-chance | unknown (D6) | same | likely pinned |
| eighth (synthetic) | constructed series by design (Lego (iii)) | forms, and does not form when one precondition is False | never pinned |

`65`'s stop line prints the pins. **What the DB-backed fixture-cut job needs from the built branch** (not drafted here):
1. Each def's neutral real-shape note: the tests' constants in `tests/cobalt/test_rubberband_forms.py` / `test_setups_lego.py`, plus the final `AWAITING_A_DAY` set.
2. A way to find, on stored sessions, the (ticker, day) pairs where the DEFINITION forms. Two options: `cobalt radar evaluate --replay <day> --trade-def <slug> --expect-formed` from `~/cobalt` (gate 4, built in STEP-1), or the build's `tests/experiments/setups_one/` scan helper on `cobalt_dev`. The day is never chosen because he traded it (R24).
3. The `_cut_p2_fixtures.py` pattern extended to more tickers or days. It needs raw reads saved to a file, and no approved string produces one today (`db_query.py` has no output file — c1 draft ESCALATE 1).
4. A BLIND expected-values seat. Inputs: the bars excerpt, the neutral def, and the FINAL's resolver tables (§2.2, §2.3, §3, §4). Each checker writes side, formed bar, trigger and stop. A small follow-up then replaces each pin with a formed test.

Both close before the ONE deploy (F-16 (1), F-21).

## Step list (`65`)

| step | FINAL tags | files (expected) | tests | experiments | needs cobalt_dev |
|---|---|---|---|---|---|
| 0 | — | report | baseline offline + with-DB | — | reachability |
| 1 C1 | §1, A-01, F-01, F-07, R2F-01, §2.3+§9(5) F-16·X17, §9 gates 1–5, R2-2 B | `radar/evaluate.py`, `cards/scoring.py`, `cards/store.py`, `radar/audit_export.py`, `radar/evaluate_cli.py`, `radar/cli.py`, `replay/formations.py` | `test_rubberband_forms.py` (T1–T6), `test_setups_lego.py` (pin), re-points | X9, X17, X24, X27, X8 tap half; X3 → deploy; X28 n/a | yes |
| 2 C2 | §2.1 F-04, R2F-12, F-06·X4/X6, R2-4 per row, §2.2–2.5, §4, §7 B (full closure), §8 R2F-07/R2F-09, R2-3 by X20 | new `radar/formation/{triggers,stops}.py`, ATOMS/RELATIONS module, `anatomy/frame.py`; `anatomy/registry.py`, `evaluate.py`, `taxonomy/{tunables,loader,vault_loader,store,cli}.py`, `tunables.yaml` (convention rows, null), migration pair (B + X20), `seam.py` only under ASTRA | frame property, byte-identity pins, registry⇔interpreter, truth table, writer on `tmp_path`, dry-run | **X20 first**, X19, X22, X23 (tmp), X8 source half, X21, X25, X18, X12, X4, X6, X5 (offline) | yes |
| 3 C3a | §3 D1, §5, F-10, F-11, F-14·X11 | `anatomy/indicators.py`, `frame.py`, D1 detectors, `evaluate.py`, `seam.py` if X11 | F-10 / F-11 as tests, pins | X1 (before), X11, X14, X5 | yes (X1) |
| 4 C3b | §3 D2–D3, F-12·X15/X16 | Range(micro)+pivots, leg roles (`leg.py` untouched), `range_break`, `consolidation_low`, `IN cfg(band) min` | hitchhiker acceptance | X13, X15 (before), X16, X7, X11, X5 | yes |
| 5 C4 | §3 D4, F-03·X10 | `extension.py` lifecycle, `indicator_cross`, `measured_fraction`, `recent_higher_low`, `flat` / `between`, Arith | backside, fashionably-late | **X10 before**, X7×2, X11, X5 | stored-session parts |
| 6 C5 | §3 D3 roles, §6 F-13, R2-2.4 | roles, `touched`, `indicator_rejection`, `indicator` stop, **A-13 resolver (special case)**, Extension on Leg | nine-ema-scalp | **X26 before**, X1 re-read, X7, X11, X5 | stored-session parts |
| 7 C6 | §3 D5 (+ D6 level set) | trendline, `trendline_break`, `dist`, level set A-17, `rejected` A-18 | vwap-continuation | X7, X11, X5 | stored-session parts |
| 8 C7 | §3 D6 | RangeBreak lifecycle, events, Range(prior), anaphora, `sequence`, `turn_candle` | second-chance | X7, X11, X5 | stored-session parts |
| 9 Lego | R44 (i)–(iv), R45 (v) | tests + `ADDING-A-SETUP.md` ONLY | no-name-in-src, registries, eighth def, evaluability×8, doc drift | X22 (all), frame property (all), X5 final | no |

## Honest duration

**Build.** The FINAL sizes the chunks: C1 S+M, C2 M (plus the store, writer, closure and migration), C3a M, C3b L, C4 M, C5 M, C6 M, C7 M–L, plus the Lego step. `56`, the C1 slice alone, was metered MEDIUM (≈2–3 h). Estimate per step: STEP-1 ≈3 h · STEP-2 ≈6–7 h · STEP-3 ≈2.5 h · STEP-4 ≈4–5 h · STEP-5 ≈3.5 h · STEP-6 ≈3 h · STEP-7 ≈3 h · STEP-8 ≈4 h · STEP-9 ≈1.5 h · CLOSE ≈1 h. **Total ≈ 30 h of Opus run time (range 25–38).**

**Relaunches.** Expect 6–10: the Anthropic usage limit resets, plus any crash. Context compaction continues inside one session; a relaunch is needed only on a stop. **Calendar: 3–4 days.** A deploy on TUE 09-22 or WED 09-23 is not possible.

**Check.** Staging ≈ 40 min for 30–60 parts. Checkers run in parallel under a 45 min clock, Sol and Opus possibly in two runs each. File-checks ≈ 1–1.5 h. **≈ 3 h of hub time.**

## RULE PROOF (per string; `grep -c -F`, run by this seat 18:1x ET)

| prompt | strings | against | count |
|---|---|---|---|
| 65 | the whole `--allowedTools` … `--add-dir /Users/cobalt/cobalt-wt` span (16 + 1 + 2 allow, 3 deny, triplet) | `2026-09-21/56-setups-c1-build.md` | 1 — **byte-identical to `56`**; only `--remote-control` and the prompt path differ |
| 65 | the 14 middle allow strings as one span | `2026-09-21/02-bars-chunk-2-fix-r3.md` | 1 (09-20 R25); `56`'s drafter proved the other two + denies + triplet against `02` = 1 each |
| 65 | `"Bash(COBALT_ENV=dev uv run pytest *)"` | `2026-09-19/44-archiver-db-rerun.md` | present (09-19 R18 "approve env") |
| 65 | `cp` / `rm` `.env` for `setups-c1` | `cto-2026-09-21.md` R41 | quoted with "Approved"; R44 keeps them valid for this path |
| 66 | `"Bash(grok *)" "Bash(agy *)"` | `2026-09-20/08-bars-chunk-e-check.md` | 1 |
| 66 | the 11 strings `mkdir -p scratch/…` → `date*` as one span | `08-bars-chunk-e-check.md` and `66` | 1 and 1 — 13 of `08`'s 14. The Astra string is LEFT OUT (R46) |
| 66 | 3 deny + triplet span | `08-bars-chunk-e-check.md` | 1 |
| 66 | `"Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only *)"` + `"Bash(claude -p --model claude-opus-5 *)"` | `cto-2026-09-21.md` R49 ("Approved", 18:14) | 1 line (R49's row carries both); byte for byte in `66`'s line. `-c model_reasoning_effort="high"` and the Opus flags ride inside the wildcards |
| 66 | grok / agy date literal | `cto-2026-09-21.md` R39 (`through 2026-09-22`) | covers only through 09-22; the check runs later → an extension row is needed |
| — | `Bash(COBALT_ENV=dev uv run cobalt db migrate*)` (considered for R2-3 B) | 09-19 R18 (reused from 13's line) | **NOT needed**: the migration is proven inside the suite's rollback transaction (`test_radar_score_migration.py` applies `FORWARD`); `65` never migrates `cobalt_dev` |
| — | `Bash(uv run cobalt radar evaluate *)` (X3) | `2026-09-16/01-p2-build.md` | **NOT used**: the worktree has no `data/radar-cache`; X3 and gate 4 move to the deploy |

**NEW approvals:**
1. `Bash(grok *) and Bash(agy *) through <the check's launch date>` — for `66` only. It extends R39 (through 2026-09-22) for the same sandboxed, headless, read-only use. The one build finishes ≈ 09-24/25, so the date must be the check's actual launch date. `66`'s DATE + EXTENSION GATE requires a committed row of his carrying that exact literal.

Nothing else is needed:
- `65`'s line is `56`'s: R41's two `.env` strings, R25's 16 + 3, and 09-19 R18's env string.
- `66`'s two seat strings are his R49, "Approved" at 18:14.

What the desk can show him, verbatim: *"The seven-setup build needs no new permission. The one check of it needs Grok and Gemini extended to the day it runs, which I expect Thursday or Friday. Approve extending them through that date? No production, no push."*

## L68 — shared files

| branch | status | files shared with the one build |
|---|---|---|
| `s2/degraded-line-0921` | lands tonight (`deploy-2026-09-21b`), under the build by PREFLIGHT | none |
| `s2/stale-marker-0921` | built tonight, deploys TUE 09-22 (`53`) | `tests/cobalt/test_radar_panel_cards.py` (and `aset/radar_panel.py`) ONLY if X24 fails |
| `ops/2026-09-21` | offline done, unmerged | none (`.gitignore`, `configs/cobalt/backup.yaml`, backup test, DevDocs, BACKLOG) |
| `bars/chunk-1a-0920` | unmerged | **`configs/cobalt/taxonomy/tunables.yaml`**; `tests/cobalt/test_tenancy.py` if A1 re-points it |
| `bars/chunk-2-0920` | unmerged | **`configs/cobalt/taxonomy/tunables.yaml`**; **`src/cobalt/db_migrations/__init__.py`** (+ numbering: its `0012`) when R2-3 B ships a migration; migration-list tests (`test_radar_score_migration.py`, `test_p4_migrations.py`, `test_tenancy.py`) if re-pointed |
| `bars/chunk-e-0920` | unmerged | `tests/experiments/` (it adds `tests/experiments/__init__.py`; `65` uses its own `setups_one/conftest.py` and does not add that file) |
| `s2/rubberband-proof-0921` | proof, never merging | none (`test_rubberband_forms.py` ≠ the proof's filename) |
| queued stale-score design (`61`, no branch) | tribunal | the same `evaluate.py` / `scoring.py` / `store.py` functions; whichever lands second rebases |

## What the ONE deploy will need (facts; the desk decides)

- **His chat "approve"** (L7 / L61). It is a trading-logic change for eight defs, and every card of the seven has no score for its life until he rules its rows.
- **RESTARTS**, derived at CLOSE. Expected: `com.cobalt.radar`, `com.cobalt.aset` (via `aset/web.py` importing `cobalt.cards`), every resident importing the taxonomy loader, and the one-shot `com.cobalt.replay` on its next run. L66: residents down before the merge, inside the 20:00–21:00 pause.
- **Migration:** none, or `0013_…` (tunables.slug nullable) with its bounded rollback under R2-3 B + X20. Then `cobalt db migrate --allow-prod` joins the allowlist (L61), after the residents are down.
- **The assumed note, AFTER the reader ships ([F-09]).**
  - The writer is proven on the DEV vault with a diff (L28). `65` proves it on `tmp_path` only.
  - Then `cobalt taxonomy assumed write --from <yaml the desk prepares from the companion>` runs against the production vault, then `cobalt taxonomy load`.
  - Both are new production strings plus his approve. Until then only Rubberband can form in production.
- **Acceptance the build cannot run**, from `~/cobalt`:
  - X3 + gate 4 over the stored sessions. The deploy must say whether X3's "zero is allowed" or gate 4's "non-zero on zero" governs.
  - The live-note test with `COBALT_LIVE_VAULT_ROOT` set; a SKIP is RED.
  - The stored-day X5.
  - The daily legs of X7 / X18.
  - The NN#16 smoke.
- **Before the deploy:** the fixture-cut job + blind seat (C), and the owner / tribunal items (F1, on/off) if he wants them in the same evening.
- **EVALUATOR_VERSION bump:** older receipts are refused by replay / audit export; `replay/formations.py:81` gets the new version inside the build.
- **Stacking (his R47, 18:09):** every built and checked branch ships in ONE stacked deploy per evening, gated on the combined tree (L68). `53` is superseded by TUE's stacked set. The one build cannot be ready TUE or WED (≈ 09-24/25), so it joins the first evening's set after its check. It then stacks with whatever else is checked by then; the bars branches share `tunables.yaml` with it, so the combined tree's offline + with-DB suites are that set's gate.

## READING

- `64-draft-setups-one-build.md` (brief).
- `LAWS.md` 1–405 in full.
- FINAL `SETUPS-AT-DEFAULTS-FINAL-2026-09-21.md` 1–496 in full (110,651 B, not the brief's 67 KB).
- `setups-tribunal-derive-r2-2026-09-21.md` in full.
- `setups-tribunal-fable-r2-2026-09-21.md` 106–239 (plus grep).
- `setups-tribunal-r2-2026-09-21.md` 97–150, 490–617.
- `56-setups-c1-build.md` in full; `57-setups-c1-check.md` in full; `setups-c1-draft-2026-09-21.md` in full.
- `cto-2026-09-21.md` rows R13, R15, R17, R18, R23, R24, R25, R39, R40–R46 (grep).
- `cto-2026-09-20.md` R13, R23, R25, R39; `cto-2026-09-19.md` R18.
- Code on main `75e65d0`:
  - `radar/evaluate.py` 1–700, 905–964, 1150–1399
  - `radar/anatomy/registry.py` in full
  - `taxonomy/vault_loader.py` in full; `taxonomy/store.py` in full; `taxonomy/tunables.py` in full
  - `taxonomy/loader.py` 1–180
  - `taxonomy/trade_def.py` 120–380, 700–918
  - `db_migrations/__init__.py` 1–66
  - by grep: `predicate.py`, `vaultwrite/writer.py`, `settings/card.py`, `replay/formations.py`, `migrations/0001_trade_defs.sql`, `db_migrations/placement.py`, `tunables.yaml`
- Tests: `test_taxonomy_store.py` 60–91, `conftest.py` (grep), `test_radar_score_migration.py` (grep), the proof test (grep), `_cut_p2_fixtures.py` in full, `ls tests/fixtures/radar`.
- His seven notes: by `grep -n "cobalt:unit\|cfg("` and the `- key:` count only; nothing copied. Companion `setups-assumed-values-2026-09-21.md` in full: key NAMES, pages and units used; values never copied.
- Git: `git branch --no-merged main`; `log --name-only main..<branch>` for `ops/2026-09-21`, `bars/chunk-1a/2/e`, `s2/degraded-line-0921`; `deploy-2026-09-21b` (absent at 17:5x, expected tonight).
- Precedent greps: `Bash(claude -p *)`, `gpt-5.6-sol`, `cobalt db migrate`, `radar evaluate --replay`.

## ESCALATE

1. **R2-4 is the desk's to fill on the launch row, and `65` refuses without it.**
   - Only B has no failed claim and no withdrawn sentence.
   - A carries withdrawn #11 ("kept in the receipt"); the receipt has no evaluations today (`evaluate.py:917-930`).
   - ASTRA carries withdrawn #10 (the order) and K22 HOLDS against it.
   - Whichever text is chosen, `65` pins the `:1329` / `:1342` case (an open short card expired by the long side's avoid) in a named test.
   - `ASK DESK: which R2-4 goes on the launch row? [18:1x]` — no safe default; the prompt stops without it.
2. **R2-3: A cannot be built as the radar is wired** (reads R1 and R2 HOLD on main). X20 decides only B's migration. The migration lives in `db_migrations/` as `0013`, because a rollback cannot live in `taxonomy/migrations/`. It is an L68 seam with `bars/chunk-2-0920`'s `0012`.
3. **F1 — the three `per_indicator` holes** (derive ESCALATE 4). fashionably-late and vwap-continuation cannot form at production defaults under the settled reader. `ASK DESK: may load_assumed_tunables accept per_indicator(<ind>) rows under scope equality? That widens settled wording [R2F-07], so it needs a house's wording or his ruling. [18:1x]` Safe default in `65`: NOT widened; both defs listed `AWAITING_A_RULING: F1`.
4. **No per-setup ON / OFF exists (R44 (c)).** No pure use of an existing mechanism gives one. → `## OWNER / TRIBUNAL`. The build ships without it and says so, including in `ADDING-A-SETUP.md`.
5. **Until `Assumed Defaults.md` is written, every numeric assumed hole is null. Only Rubberband (convention `A-01`) can form in production.**
   - The writer, a Cobalt L28 command over the existing `VaultWriter` (`create_if_absent` `:559`, `upsert_unit` `:644`), is built and proven on `tmp_path` only.
   - The dev-vault proof and the production write are deploy-time work: new strings plus his approve.
   - `ASK DESK: does the note write ride the deploy evening, or follow it? [18:1x]`
6. **Convention rows before the note exists — a reading of R2-2.2 B, not new design.**
   - Each convention key gets an ENGINE row: `label`, `value: null`, `status: proposed`. This way "a declared convention with no row is a loud load error" can never break a production load.
   - A null convention row counts as assumed unconditionally (the C1 rule carried forward). It over-marks, which is the safe side.
   - `ASK DESK: intended reading? [18:1x]` Safe default: as written.
7. **FIXTURES.** Expect most of the eight in `AWAITING_A_DAY` (one committed trade date).
   - A DB-backed fixture-cut job and a blind expected-values seat close the pins before the deploy, as listed in (C). Neither is drafted here.
   - The cut needs a DB read into a committed file, which no approved string does today.
8. **The check cannot run on 2026-09-22.** grok/agy expire with R39. `66` needs his extension to its launch date (NEW approval 1).
9. **R46 and R49 arrived mid-draft (18:05, 18:14) and were folded.**
   - `66` seats Grok + Gemini + Sol + Opus 5; three are required.
   - Its line = 13 of `08`'s 14 strings (Astra left out) + R49's two strings byte for byte.
   - `-c model_reasoning_effort="high"` and the Opus `--permission-mode plan` / `--add-dir` / tool lists ride inside the wildcards.
   - The hub proves no write with `ls -la` of the packet folder and the build worktree before and after each checker, plus the quoted launch line.
   - The brief's two-astra-run split is replaced by a two-run split for Sol and for Opus, each one attempt, triggered only when the MANDATORY set with source diffs is over 1.2 MB. Evidence is never shrunk.
   - Windows: I do not know Sol's or Opus 5's exact context size. Opus reads with its Read tool and Sol with `cat`/`rg`, so neither has to hold the whole packet; the split is the fallback.
10. **Stored-session experiments and the daily cache.**
    - X1, X7, X13, X15, X16 and X18 run as with-DB pytests under `tests/experiments/setups_one/`, only if `cobalt_dev` holds stored sessions (X2's neutral coverage question runs first).
    - The worktree has no `data/radar-cache` (`configs/cobalt/radar.yaml:31`), so their daily/HTF legs are UNPROVEN in the build and move to the deploy.
    - X5 runs offline as a proxy; the stored-day X5 is at the deploy.

## OWNER / TRIBUNAL

- **Per-setup "discoverable or not" (his R44 (c)).**
  - Candidate, for a design round, not built: a per-trade row in the def's own `tunables:<slug>` unit. It uses the existing reader and sync, is absent = on, and is set in his note.
  - Open question: what "off" means — (a) the def is not evaluated at all, no seam row; or (b) the def is evaluated and published on the board but forms no card, a per-setup `cards_enabled`.
  - Needs a tribunal or his word; L65 governs any edit to his notes.
- **F1**: whether the dedicated reader also accepts `per_indicator(<ind>)` rows. It widens [R2F-07]'s settled wording.

L74: no instruction block was observed inside a tool result this run. The two desk additions arrived as cross-session messages from the desk session. Both are verified against committed desk rows R45 and R46 (and L67's 18:05 amendment) and folded as the desk's direction, not as rulings of mine. This seat committed nothing and sent nothing.

MEMORY: [stated 2026-09-21 · setups one-build drafter] A migration for a table created by a feature module's own `migrations/` folder cannot carry a rollback there: `ensure_schema()` executes every `*.sql` in that folder on each load (`taxonomy/store.py:82`), so a `*.rollback.sql` would run forward. Such migrations go to the database-wide `db_migrations/` registry.

## CONTINUE

None. The run is complete. Next steps are not mine:
- The desk fills `65`'s launch row with `R2-4 = <A|B|ASTRA>` and answers ESCALATE 3, 5 and 6 (safe defaults stand if it does not).
- It launches `65` after `DEGRADED LINE DEPLOY DONE … deploy-2026-09-21b`, then gets approval 1 (the grok/agy date) before `66`, and fills `66`'s launch row.

## DIGEST FOR THE DESK

- **Two prompts, nothing launched.**
  - `65-setups-one-build.md` (106 KB): Opus 5, no auto mode, `setups/seven-0921` in `~/cobalt-wt/setups-c1`, 9 steps (C1 → C2 → C3a → C3b → C4 → C5 → C6 → C7 → Lego), one commit per step, one stop line.
  - `66-setups-one-check.md` (44 KB): Sonnet 5 hub; Grok + Gemini + Sol + Opus 5 (R46), three required, 45-min clock, a reading-order packet with MANDATORY and OPEN-AS-NEEDED parts.
- **`65` needs NO new string.** Its line is `56`'s byte for byte, except the rc name and prompt path.
- **Its launch row must carry exactly one of `R2-4 = A|B|ASTRA`.** Only **B** has no failed claim and no withdrawn sentence. A holds withdrawn #11, ASTRA holds withdrawn #10 plus K22.
- **R2-3:** the reads B rests on HOLD on main, so A cannot be built. X20 inside STEP-2 decides only B's migration (`db_migrations/0013`, bounded rollback; L68 seam with bars chunk-2's 0012).
- **On/off dial: does not exist.** Only global `radar.cards_enabled`. It is an owner/tribunal item (what does "off" mean: not evaluated, or evaluated but no card). The build ships without it, and `ADDING-A-SETUP.md` says so.
- **Standard routine:** 6 of 7 setups fit entirely. **nine-ema-scalp** has ONE named special case, the `A-13` catalyst stand-in resolver. fashionably-late and vwap-continuation fit as bricks but are **blocked at defaults by F1** (three `per_indicator` holes the settled reader cannot fill).
- **In production on deploy night, only Rubberband can form** until `Assumed Defaults.md` is written after the reader ships. That write is a production vault write with its own approvals.
- **Fixtures:** one committed trade date. Expect most defs pinned `AWAITING_A_DAY`. A DB fixture-cut job plus a blind seat close them before the deploy (needs listed in C).
- **Estimates:** build ≈ 30 h of Opus (25–38), 6–10 relaunches, 3–4 days. Check ≈ 3 h. Not ready for TUE or WED; it joins the first evening's stacked set after its check (R47).
- **NEW approvals: 1** — grok/agy extended to the check's launch date (R39 ends 09-22).
  - `66`'s seat strings are R49's, byte for byte (Sol `… -m gpt-5.6-sol -s read-only *`, Opus `claude -p --model claude-opus-5 *`). Astra is out of the line.
- **ASK DESK:** R2-4 row (no default) · F1 widen? (default no) · note write same evening? · null convention row = assumed? (default yes).
- **L68 seams:** `tunables.yaml` with bars chunk-1a/2 · `db_migrations/__init__.py` with chunk-2 · `tests/experiments/` with chunk-e · panel test with stale-marker only if X24 fails · stale-score design on the same functions.
- **DO NOT EXIT** does not apply; this seat hosts no child.

SETUPS ONE BUILD PROMPTS DRAFTED · prompts: 2 · steps: 9 · on/off dial exists: no · R2-4 text with no failed claim: B · build estimate: 30 h · new rule strings: 0 · ESCALATE: 10
