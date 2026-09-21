# Setups tribunal — round 2 (hub `setups-tribunal-r2-0921`) — 2026-09-21

## §0 Headline

- **All 3 houses ruled** (grok `TRIBUNAL R2: BUILD` · gemini `BUILD AFTER applying the NEITHER replacements` · astra `BUILD AFTER incorporating these replacements and assigning their chunk gates.`); astra launched with ` < /dev/null` (accepted) and its reads started: `astra stdin experiment: reads started`.
- **R2-2 = SPLIT**: R2-2.1 grok NEITHER · gemini FABLE'S · astra GROK'S (no two alike); R2-2.2 split; R2-2.3 and R2-2.4 two NEITHER (different wording) + one FABLE'S; R2-2.5 two GROK'S + one FABLE'S. **Items settled: 1 of 4** (R2-1, 3-0 FABLE'S).
- **Fable R1 claims file-checked: 9 HOLD of 10** (C7b, "the existing pattern" across resolvers, DOES NOT HOLD). Packet 90,028 B (13 files). Redactions of user data: 0.
- **ESCALATE: 3.** No `DO NOT BUILD`; no house failed; no independence breach.

## AUTHORIZATION

All proofs run as separate Bash calls, 15:56–16:00 ET, 2026-09-21.

| proof | result |
|---|---|
| `date` row 1 | `Mon Sep 21 15:56:36 EDT 2026` — before 2026-09-22, outside 19:25–20:45 and before 23:20: passes |
| R13 (`cto-2026-09-20.md:86`) | present |
| R23 (`cto-2026-09-20.md:206`) | present — `Bash(grok *)` / `Bash(agy *)` stand through Monday 2026-09-21 23:59 ET |
| R15 (`cto-2026-09-21.md:27`) | present; carries "I don't want to rule on anything" |
| R32 (`cto-2026-09-21.md:43`) | present; carries "derive without astra: yes" |
| derive stop line committed | `git log -1 -S"SETUPS DERIVED v2"` → `fd33ab58fe5202705027f64018f9f796bbc84ae8` |
| v2 committed | `git log -1 -- SETUPS-AT-DEFAULTS-v2-2026-09-21.md` → `fd33ab58fe5202705027f64018f9f796bbc84ae8` |
| derive last non-blank line | `SETUPS DERIVED v2 · folds: 21 · verbatim: 9 · needs round 2: 4 · owner items: 12 · ESCALATE: 5` |
| no new rule (`grep -c -F` in `08-bars-chunk-e-check.md`) | 11 allow strings + 3 denies count **1**; `Bash(grok *)` and `Bash(agy *)` count **2** each (matching LINES, not occurrences: line 1 = the approved launch line, line 5 = its authorization prose; located with `grep -n -o -F`). None counts 0, so the "any 0 → FAILED" rule does not fire; disclosed for the desk. |
| `date` row 2 (immediately before launch) | `Mon Sep 21 16:04:32 EDT 2026` — passes |

## PREFLIGHT

| rule · command | exit | allowed / DENIED |
|---|---|---|
| `date` | 0 | allowed — `Mon Sep 21 15:56:36 EDT 2026` |
| `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| `agy --version` | 0 | allowed — `1.2.7` |
| `ls scratch/tribunal-bars-0920/setups-tribunal` | 0 | allowed — lists `r1` |
| `ls scratch/tribunal-bars-0920/setups-tribunal/r2` | 1 | allowed — `No such file or directory` = fresh run |
| STAGGER s1 `ls …degraded-line-deploy-review-r2-2026-09-21.md` + `tail -n 3` | 0 | allowed — last non-blank line starts `DEGRADED LINE DEPLOY REVIEW R2 DONE ` |
| STAGGER s2 `ls …float-handicap-tribunal-2026-09-21.md` | 1 | allowed — `38: no report — not running`, continue |
| CODEX PROBE (`run_in_background`, `codex exec … "Reply with only the word OK."`) | 0 | allowed — answered `OK`, no usage-limit text; output BEGAN with `Reading additional input from stdin...` → **astra: UP** (finished 15:57 ET, under a minute) |

Extra (not in the plan, harmless read): `grok --help` was run once at 16:02 ET to confirm the single-turn flag (`-p`); allowed. Two Write calls to `/Users/cobalt-wt/...` (a typo of the worktree path) were REFUSED by the OS (`EACCES: permission denied, mkdir '/Users/cobalt-wt'`) and created nothing; the files were then written to the correct path. Two `Edit` calls at a nonexistent path also failed and changed nothing.

## Packet

Folder `scratch/tribunal-bars-0920/setups-tribunal/r2/` (gitignored; created by the first Write). Every file Read → Write; the Write tool strips trailing whitespace (not counted separately). `wc -c` after staging:

| file | bytes | note |
|---|---|---|
| `NEEDS-ROUND-2.md` | 10,102 | derive lines 71–105 verbatim, header line naming path and range |
| `v2-sections.excerpt.md` | 29,265 | ranges :1-37, :61-88, :93-107, :139-141, :215-265, §10 header + rows C1/C2/C5 (:297, :298, :302) + evenings (:306), L52 rows (a)(b)(c) (:331-333, with :325-327 header), X-table header (:340) + rows X8 (:349), X12 (:353). The `|---|` separator lines of two tables are omitted. |
| `hub-checks.md` | 4,895 | R1 rows 6, 17, 18, 19, 26 + `Also hub-noted` + ESCALATE 3; R1B rows 8, 9, 14, 17b + ESCALATE 3; the two table header lines |
| `seam.excerpt.py` | 2,119 | `radar/seam.py` :95–156 |
| `scoring.excerpt.py` | 6,396 | `cards/scoring.py` :60–**111** (spec :60–110; extended by ONE line so the `computed` property body is whole) and :236–345 |
| `evaluate.excerpt.py` | 8,575 | `radar/evaluate.py` :128–140, :415–430, :584–625, :630–660, :755–805 |
| `extension.excerpt.py` | 2,615 | `radar/anatomy/extension.py` :36–64, :94–104, :136–146; head note says the "existing pattern" is the uppercase module constant `TUNABLE_KEYS` |
| `vault_loader.excerpt.py` | 5,031 | `taxonomy/vault_loader.py` :257–285, :317–366, :457–485 |
| `loader.excerpt.py` | 2,159 | `taxonomy/loader.py` :88–135 |
| `tunables.excerpt.py` | 1,117 | `taxonomy/tunables.py` :60–100 |
| `store.excerpt.py` | 1,526 | `cards/store.py` :1030–1050 |
| `greps.txt` **[USER DATA]** | 8,354 | 15 searches (7 counts + 2 line lists + 6 repo/v2 searches); its header states that this shell's `grep` honours `.gitignore`; note paths shortened to `…/4 - Strategies/` in the printed command lines. Three output lines were mis-typed on first write and corrected against the tool results before launch; the mirror grep matches only the S3 note-mirror stage (`mirror_sources`) — no price frame exists. |
| `QUESTIONS-R2.md` | 7,874 | verbatim question text + the appended "Files in this folder" paragraph |
| **total (13 files)** | **90,028** | ≤ 100 KB (target ≤ 90 KB: 90,028 B ≈ 90.0 KB — at the line; nothing dropped) |

All anchors checked with `grep -n` before staging; every one sat at the line the prompt named (`seam.py` :100/:111/:141; `scoring.py` :72/:247/:264/:319; `evaluate.py` :134/:419/:593/:759/:800 and `"Setup(relation)"` :643, `catalyst_ref_unknown` :620; `extension.py` :40/:143; `vault_loader.py` :271/:317/:476; `loader.py` :90/:115; `tunables.py` :63/:85; `store.py` score_suppressed UPDATE :1039-1047).

Disclosed packet facts: (1) `../r1/` (44 files) also holds `grok-ruling.md` and `gemini-ruling.md` (round 1) — the houses were told not to open any file whose name contains `-ruling`; and `trade-tags.txt`, `assumed-values.md` (user data, round 1's packet). (2) `refresh_dots` (the function that carries a dot set across a refresh) is NOT in the round-2 excerpts; it is in `../r1/cards-scoring.py`, which a house may open by a line range.

## CONTINUE

RUN COMPLETE at 16:28 ET — nothing is running. (A relaunch of this file would find all three `*-ruling-r2.md` files and re-ask no house; the report below is final.)

History (kept for the desk): next-step breadcrumb while running was "wait for grok, then run §3 and close".

Final status: gemini DONE 16:08:00 (`BUILD AFTER applying the NEITHER replacements`, `gemini-ruling-r2.md`); astra DONE ≈16:10:30 (exit 0, 46,391 tokens, `astra-ruling-r2.md`); grok DONE 16:23:53 ET, ≈ 19.4 min after its 16:04:32-16:04:52 launch, i.e. inside the 16:24:32 deadline (exit 0, wrote `grok-ruling-r2.md` itself, final line `TRIBUNAL R2: BUILD`). No TIMEOUT, no METER, no HARNESS.

## Clock

| time (ET) | trigger | minutes since launch | action |
|---|---|---|---|
| 16:04:32 | DATE GATE row 2 | — | passes; launch all three in one message |
| 16:04:52 | after launch | ≈ 0 | grok, gemini, astra running |
| 16:05:30 | after writing the report skeleton | ≈ 1 | all three running; began Fable-claim file-check |
| 16:06:32 | astra output check (≥ 3 min rule: read at ≈ 2 min) | ≈ 2 | astra output already past the stdin line: `cat` of `QUESTIONS-R2.md`, `NEEDS-ROUND-2.md` … and its first `ITEM R2-2.1` printed → **reads started** |
| 16:07:14, 16:07:19, 16:07:28 | between file-check rows | ≈ 3 | grok output 373 B (progress text, no file yet), gemini 0 B, astra printing ITEMs (9 of 12 by 16:07:14) |
| 16:08:00 / 16:08:03 | completion notice (gemini) | ≈ 3.5 | gemini done, exit 0, full ruling; wrote `gemini-ruling-r2.md` byte for byte |
| 16:08:29, 16:08:56 | between file-check rows | ≈ 4 | astra all 12 ITEMs printed; grok still writing nothing |
| 16:10:26 / 16:10:30 | completion notice (astra) | ≈ 6 | astra done, exit 0; final message captured to `astra-ruling-r2.md` |
| 16:11:27, 16:11:47, 16:12:44 | between file-checks | ≈ 7–8 | grok only; no `grok-ruling-r2.md` |
| 16:13:07, 16:14:02, 16:14:08, 16:14:47 | between file-checks / before ending the turn | ≈ 9–10 | grok only; no `grok-ruling-r2.md`; deadline 16:24:32 written in `## CONTINUE`; turn ended to wait |
| 16:23:53 | completion notice (grok) | ≈ 19.4 | grok done inside the deadline; `grok-ruling-r2.md` exists (122 lines); read it and its raw output |
| 16:24:59, 16:27:14 | collate steps (checking Grok's claims against the excerpts, notes, `cards/radar.py`, `cards/store.py`, ADR-0009, `../r1/`) | ≈ 20–22 | nothing running; no house past 20 min at any check |
| 16:28:09 | close | — | report finalised; last line replaced |

## Astra stdin experiment

Launched with ` < /dev/null` appended after the closing quote of its sentence. The Bash call was NOT denied (the permission layer accepted the redirect under `Bash(codex exec --skip-git-repo-check -m gpt-6-astra -s read-only *)`). (i) `Reading additional input from stdin...` **appears** (line 1 of astra's output). (ii) **READS STARTED**: at the first check (16:06:32 ET, ≈ 2 min after launch) the output already held the `cat` of `QUESTIONS-R2.md` and the first printed `ITEM R2-2.1`; it went on to read 8 more files by `cat` / `rg` / `sed` in the r2 folder only (`QUESTIONS-R2.md`, `NEEDS-ROUND-2.md`, `hub-checks.md`, `scoring.excerpt.py` + `evaluate.excerpt.py` + `seam.excerpt.py`, `extension.excerpt.py`, `v2-sections.excerpt.md` by `rg` and `sed -n 73,87p`, `store.excerpt.py`, `greps.txt` by `rg` and `sed -n 1,26p`, `vault_loader.excerpt.py` + `tunables.excerpt.py`, `loader.excerpt.py`). (iii) **final outcome**: exit 0 at ≈ 16:10:30 ET (≈ 6 min), 46,391 tokens used, final message ends `TRIBUNAL R2: BUILD AFTER …`, all 12 questions ruled. Experiment field: **reads started**. (The redirect and the hang are not proven causally related: the 11:46 run hung with no redirect, this run did not hang with one — one launch each; L70 keeps the cause UNPROVEN.)

## Fable round-1 claims, file-checked

Done while the houses ran (each row: the real file opened with Read or `grep -n` on main at HEAD; the claim's line is in `reports/setups-tribunal-fable-r1-2026-09-21.md`). No wording from his notes is copied; notes are cited by `note:line`.

| # | claim (Fable R1 report line) | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| C1 | WF5: `AtomOutcome` is a closed model, `extra="forbid"` (:89, :184) | `seam.py:99-100`, `:111-117` | HOLDS | `_Closed` sets `extra="forbid", frozen=True` (:100); `AtomOutcome(_Closed)` (:111) inherits it; its slots are atom, value_kind, boolean, number, symbol, unavailable — no field for a mark. |
| C2 | `NaReason` is a closed Literal, no `ASSUMED` (:61) | `scoring.py:72`, `:104` | HOLDS | Six members: curve_unset, MANUAL, input_stale, input_unavailable, DESK_NA, DEFAULT_UNRULED. `Dot.na_reason: NaReason \| None` validates against it. DB column `na_reason` is `TEXT` (`0006_radar_score.sql:169`, `0007_radar_cards.sql:132`), no CHECK by that name. |
| C3 | `suppression()` is dots-only; would suppress while an N/A dot is untapped; a tap lifts it (:61, :181) | `scoring.py:109-111`, `:238-244`, `:247-251`, `:264-267`, `:319-336` | HOLDS | A `cobalt-degraded`/`deterministic` dot outside DESK_FACTORS is `computed`; with `na_reason` set and `trader_grade` None it blocks; a tap sets `trader_grade`, the blocker goes, `conviction` averages it. |
| C3b | (not a Fable claim — a read fact bearing on C3) | `evaluate.py:774-777`; `scoring.py:201-235`; `store.py:1049-1050` | READ FACT, no verdict | `refresh_card` builds `fresh` from `ld.definition.quality_factors`; `refresh_dots` returns only dots present in `fresh`; `score_card` sees that returned list. Fable's text says "appended after `compute_dots`" without naming create and refresh call sites. |
| C4 | `Hitchhiker.md:33-38` and `Second Chance Scalp.md:106-108` name neither an Extension nor `trade_direction` (:43) | `Hitchhiker.md:33-38`; `Second Chance Scalp.md:106-108`; greps.txt counts | HOLDS | `trade_direction` counts: 0 in both (also 0 in Rubberband, Backside, Fashionably Late; 1 in 9 EMA Scalp; 2 in VWAP Continuation). Hitchhiker:35 names a `Leg(...)` atom; Second Chance:106-108 names no Extension/Leg. |
| C5 | loader refuses a tunables row whose scope ≠ `per_trade(<own slug>)` (:70, :180) | `vault_loader.py:271-280` | HOLDS | `_read_tunables_unit` raises `VaultTaxonomyError` when `row.scope != per_trade_scope(slug)` of the note the unit sits in. |
| C6 | every `*.md` in the Strategies folder is read; a note without def frontmatter / `name:` / definition section / def unit RAISES (:70, :180, :204) | `vault_loader.py:476`; `:327-331`, `:338-344`, `:352-356`, `:359-365` | HOLDS | `glob("*.md")` feeds `_read_note`; each of the four absences raises. The module docstring (:43-49) makes an EMPTY or partial def unit a skipped DRAFT, but an ABSENT unit id still raises (:359-365). Folder holds 22 notes today. |
| C7a | a declared-key constant exists at `extension.py:40-44` (:118) | `extension.py:40-44`, `:56` | HOLDS | It is `TUNABLE_KEYS` (uppercase module constant of the Extension detector), read by `ExtensionParams.from_tunables`; not spelled `tunable_keys`. |
| C7b | "the existing pattern": atom resolvers, detectors, trigger/stop/relation resolvers declare their keys (:118) | `grep -rn TUNABLE_KEYS\|tunable_keys src/cobalt`; `grep -rl -i tunable src/cobalt/radar`; `evaluate.py:528`, `:653`, `:656` | DOES NOT HOLD | Only `extension.py` declares keys. Lowercase `tunable_keys` occurs only in `taxonomy/store.py` (DB counters, unrelated). Trigger and stop read `cfg(...)` strings through `_cfg_value` with no declaration. |
| C8 | Extension path B keeps `catalyst_ref_unknown` (`extension.py:140-144`, `evaluate.py:620-622`) (:87) | `extension.py:140-144`; `evaluate.py:620-622` | HOLDS | Path B returns `path="B_only"`, `unavailable="catalyst_ref_unknown"`; `evaluate_member` returns `not_evaluable` for it. "Untouched by the design" is a promise, not a read. |
| C9 | `evaluate.py:593-596` publishes one `RadarScoreDetail` per evaluation (:50) | `evaluate.py:514-515`, `:583-596`; `seam.py:141-150` | HOLDS | `detail()` builds one `RadarScoreDetail` (one `extension_path`, one `formed_bar_ts`); `result()` wraps one detail into one `MemberEvaluation`. No two-frame carrier exists in the excerpts. |

`Fable R1 claims checked: 9 HOLD of 10` (C1–C6, C7a, C7b, C8, C9 = 10 rows; C7 is split in two because one half HOLDS and one DOES NOT; C3b is a read fact, not counted).

## Rulings table

Same packet for all three houses (L44). A shared label (`NEITHER`) is NOT a shared wording: the wording gists differ and are in the next section. astra: full (all 12 ruled). No house was PARTIAL.

| question | grok | gemini | astra | agreement | NEITHER wording gist (≤25 words per house) |
|---|---|---|---|---|---|
| R2-2.1 | NEITHER | FABLE'S | GROK'S | **split (1 NEITHER, 1 FABLE'S, 1 GROK'S)** | grok: `score_suppressed=assumed_formation` at create, kept by every writer incl. `store.py:1222`; tap, ruling, live tunables do not clear it; no column/migration |
| R2-2.2 | NEITHER | FABLE'S | NEITHER | **split (2 NEITHER, 1 FABLE'S)** | grok: runtime record via one wrapper on the three reads + the convention line's row; no `tunable_keys`. astra: static transitive closure incl. literal `cfg` and implicit deps (A-01), snapshot to `Formation.assumed_keys`, one provenance migration |
| R2-2.3 | NEITHER | FABLE'S | NEITHER | **split (2 NEITHER, 1 FABLE'S)** | grok: C1 sets the string at create (existing column); chip + `assumed_keys` in C2; C2 deletes the direct write. astra: same string in C1 plus an `ASSUMED · A-01` chip in C1; C2 migration maps C1 cards to `{A-01}` |
| R2-2.4 | NEITHER | FABLE'S | NEITHER | **split (2 NEITHER, 1 FABLE'S)** | grok: no atom field; mark = card string recorded when the `catalyst_ref` resolver reads `A-13` through the wrapper; C5. astra: resolver declares `A-13` in its closure; permanent chip; stays suppressed; C5 S |
| R2-2.5 | GROK'S | FABLE'S | GROK'S | **split 2 GROK'S – 1 FABLE'S** | — |
| R2-1 | FABLE'S | FABLE'S | FABLE'S | **3-0 FABLE'S** | — |
| R2-3.1 | FABLE'S | NEITHER | FABLE'S | **split 2 FABLE'S – 1 NEITHER** | gemini: Fable's location (`1 - Trading/Assumed Defaults.md`) and `load_assumed_tunables` reader, restated as its own wording |
| R2-3.2 | NEITHER | NEITHER | NEITHER | **3-0 NEITHER (wordings differ)** | grok: reader-supplied row fills only if engine value null, keys, units and scopes equal. gemini: value None, dedicated reader, scopes equal. astra: same plus non-null value, source ∈ {assumed, ruling}, duplicate/strategy collisions fail, supplier still present after engine non-null fails |
| R2-3.3 | FABLE'S | NEITHER | FABLE'S | **split 2 FABLE'S – 1 NEITHER** | gemini: `source` rule kept, but a ruled engine key MUST move into committed `tunables.yaml` |
| R2-4.1 | NEITHER | NEITHER | NEITHER | **3-0 NEITHER (wordings differ)** | grok: both frames form → `not_formed`/`both_sides`; else louder of two (`not_evaluable` first); tie long. gemini: Fable's order, ties long, other in receipt. astra: Fable's order + typed receipt (`selected_frame`, both evaluations) in detail JSON |
| R2-4.2 | NEITHER | NEITHER | NEITHER | **3-0 NEITHER (wordings OPPOSE)** | grok: seam observations per frame, factor observations of the published frame; volume-only once. gemini: once on real bars, never per frame. astra: source measurements once; formation atoms/seam obs per frame; factors once after selection |
| R2-4.3 | FABLE'S | NEITHER | FABLE'S | **split 2 FABLE'S – 1 NEITHER** | gemini: frame negates prices before `Formation`/`RadarCardSpec`; intraday bars, daily series and level sets NEVER mirrored |

Notes on completeness (facts, not verdicts): gemini's R2-2.3 answer names no chunk for the `A-01` mark (the question asks which chunk and with what); astra's R2-2.3 and grok's R2-2.3 name C1 and differ on whether the chip is C1 (astra) or C2 (grok).

**closing line** — grok: `TRIBUNAL R2: BUILD` · gemini: `TRIBUNAL R2: BUILD AFTER applying the NEITHER replacements` · astra: `TRIBUNAL R2: BUILD AFTER incorporating these replacements and assigning their chunk gates.`

Per-item summary (SETTLED = every house that ruled chose the same label on every question of the item AND no house's supporting claim DOES NOT HOLD):

| item | verdict | SETTLED? |
|---|---|---|
| R2-1 | 3-0 FABLE'S | **SETTLED** (supporting claims HOLD; gemini's `evaluate.py:643-650` cite is off, the code fact holds at :635-639) |
| R2-2 | **SPLIT** (R2-2.1 has three different labels) | no |
| R2-3 | R2-3.1 and R2-3.3 split; R2-3.2 3-0 NEITHER | no |
| R2-4 | R2-4.1, R2-4.2 3-0 NEITHER (opposed wording on 4.2); R2-4.3 split | no |

Items settled: **1 of 4**.

## Wording offered, verbatim

Unedited, house by house; each file as saved in `scratch/tribunal-bars-0920/setups-tribunal/r2/`. Redactions of user-data spans: **0** (no value, quote or wording from his notes, the companion or the gap table appears; notes are cited by `note:line`, assumed values by key).

### GROK (`grok-ruling-r2.md`, written by grok itself; exit 0, 16:23:53)

~~~~
# GROK — setups tribunal, round 2

## R2-2.1

NEITHER — A formation that consumed an assumed input sets `score_suppressed = assumed_formation` on the card row at create. Consumed means a row returned by `resolve_cfg`, `_cfg_value` or `from_tunables` whose `source` is `assumed`, or a convention the forming line names (C1: the rubberband direction line, key `A-01`). `refresh_card` and every other writer of that column, including the UPDATE at `cards/store.py:1222`, keep the string. Live tunables, `suppression(dots)`, a tap, and a later `source: ruling` do not clear it on the open card. While it is set, `card_score` is null. Proximity stays computed from entry and stop and is shown. `card_score` remains the only ranking authority (ADR-0009 D4); nulls sort last under the existing WATCH tie policy. No new column and no migration.

A tap must not lift the mark: `suppression` drops a computed dot once `trader_grade` is set (`scoring.py:247-248`) and `card_score` then returns conviction × proximity (`scoring.py:86-88`). `refresh_dots` rebuilds only quality-factor dots (`cards/scoring.py:216-235`), so an appended `assumed_formation` dot is gone on the next scan. Grok's trigger ("assumed cfg key or assumed resolver, A-01 included") does not fire for `A-01` (neither a cfg key nor a resolver — hub ESCALATE 3), which contradicts his own C1 sentence. Fable's D4 objection does not hold: WATCH is `card_score desc nulls last`, then `pool_position` (`evaluate.py:134-136`, `cards/radar.py:179-182`); `pool_position` is pool `last_rank` (`evaluate.py` part3:129). ADR-0009:43 already nulls `trail_fit` until tap; that tie-break is not a second authority.

Fable, failing: a hitchhiker card formed on assumed `A-02`. Tap the dot, grade 8. The next refresh that does not take the `taps_moved` branch writes a numeric `card_score`. Proximity still uses the assumed stop. L52(a) fails. Same card, no tap: the second scan drops the dot and publishes a score anyway.
Grok, failing: implement only the first sentence. Rubberband direction is the anatomy line, no cfg read. `score_suppressed` stays null. The card is scored on `A-01`. L52(a) fails.

## R2-2.2

NEITHER — Which keys a formation consumed is a runtime record, not a static closure. One wrapper records a key when `resolve_cfg`, `_cfg_value` or `ExtensionParams.from_tunables` returns a row whose `source` is `assumed`, and when the single line that implements a convention reads that convention's row through the same wrapper (`A-01` at the direction line). The record is keys actually read, not a union of declared keys. Resolvers do not grow `tunable_keys`. There is no label vocabulary and no `not_evaluable` on an unrecognised label. `extension.py:40-44` (`TUNABLE_KEYS`) stays Extension's param list. C1 writes the rubberband string directly (R2-2.3). C2 deletes that direct write once the wrapper covers `A-01`, so there is one marker.

`_cfg_value` and `from_tunables` read tunables outside the interpreter `cfg` (hub R1 row 26 HOLDS; `evaluate.py:419-426`, `extension.py:24-31`). A wrapper on those three is the whole fix for cfg rows. It never sees `A-01`, because that convention is not one of those reads (hub ESCALATE 3). Fable's closure is not an existing seam: `TUNABLE_KEYS` occurs on Extension only (`greps.txt:29-38`). The union "preconditions, avoids, trigger and stop" does not name `A-01`, so "one mechanism marks all 23" is false for the key that gates C1.

Grok, failing: wrap only `resolve_cfg` / `_cfg_value` / `from_tunables`. Rubberband forms with direction from `A-01` and an empty recorded set. The card is scored unmarked.
Fable, failing: declare `tunable_keys` on every resolver and take the static union. The direction line is none of those resolvers and the rubberband exprs do not name `A-01`. The closure is empty of `A-01`. Same unmarked card. A path that declares three Extension keys also marks a key this scan's branch did not use, if the union is taken without a read.

## R2-2.3

NEITHER — C1 marks the Rubberband card by setting `score_suppressed = assumed_formation` at create, because the direction line consumed `A-01`. The column already exists (`cards/store.py:1041-1044`, `cards/radar.py:61`). No `assumed_keys` column, no closure, no migration, no vault write. The chip and the `assumed_keys` view column land in C2, and C2 deletes the C1 direct write when the R2-2.2 wrapper records `A-01`.

C1's file list has no schema change, and v2 §1 states the card is scored on `A-01` unmarked until this mark exists (`v2-sections` F-08; C1 row). Grok's chunk is right and his column deferral is right; his text leaves the direct write in place after C2, a second marker beside the recorder (one-path). Fable's dot is fed by the closure, and C1 has neither the column nor the closure (`v2-sections` §1, C1 row), so that text marks nothing on the first card.

Grok, failing: leave "rubberband sets the string because A-01 is assumed" standing in C2 next to the wrapper. A rubberband scan records `A-01` twice, and a ruling that stops the wrapper still leaves the hardcode marking new cards.
Fable, failing: ship C1 with no closure. Rubberband forms, direction from `A-01`, no dot, `card_score` set. L52(a) fails on the chunk this item gates.

## R2-2.4

NEITHER — `A-13` is not a field on `AtomOutcome`. The model is closed (`seam.py:100`, `AtomOutcome` at `:111`, `extra="forbid"`). The `catalyst_ref` atom stays `value_kind=boolean` with `boolean=true` and no assumed slot. The mark is the card string from R2-2.1, recorded when the `catalyst_ref` resolver reads key `A-13` through the R2-2.2 wrapper. Extension path B is untouched: `unavailable="catalyst_ref_unknown"` (`extension.py:143`) still returns `not_evaluable` and never a card (`evaluate.py:620-622` in the excerpt's `:72-74`). `A-13` does not satisfy path B. No seam change, no migration. Chunk C5.

An undeclared `assumed` argument fails validation, so Grok's "mark A-13 on the atom" does not fit the seam that exists, and his sentence does not add a field. Fable is right that the model gains no field and that path B stays `catalyst_ref_unknown`. The rest of that sentence is the declared-key closure and the tappable dot, both rejected above: the mark would not be on the card in C5 either, for the same two refresh and tap failures as R2-2.1.

Grok, failing: `AtomOutcome(atom="catalyst_ref", value_kind="boolean", boolean=True, assumed="A-13")` raises. The seam row stores a plain true. The card has no mark. Nine-ema shows a score built on `A-13`.
Fable, failing: the resolver declares `A-13` and the evaluator appends the dot. The trader taps it, or the next `refresh_card` drops it (`cards/scoring.py:216-235`). `card_score` publishes. Path B correctly still forms nothing; the nine-ema card still loses the degradation.

## R2-2.5

GROK'S

The winner is the R2-2.1 string, so X8 passes: form on an assumed key, set that row's `source` to `ruling`, and the open card still has `score_suppressed=assumed_formation` and a null `card_score` (`v2-sections` row X8; refresh must not revive it — R1 row 17 HOLDS at `evaluate.py:800`, `store.py:1041-1044`). WATCH stays ordered by `card_score` (`evaluate.py:134-136`: desc, nulls last, then `pool_position`, ticker, `card_id`). Fable's closure fails X8: after `source` becomes `ruling` the key leaves the closure, the dot is not rebuilt, and the open card gains a score.

Fable, failing: she says a mark that never lifts leaves WATCH ordered by `pool_position` against ADR-0009 D4. Three rubberband cards, all `card_score` null, sort nulls-last together and only then by `pool_position` (`cards/radar.py:179-182`). Any card with a non-null `card_score` ranks above them. `pool_position` does not become the authority. ADR-0009:28 and :43 already describe this ladder.

## R2-1

FABLE'S

With the frame, none of the seven stays unbound. `trade_direction` in a frame is that frame's side (`v2-sections` §2.1, F-04). Hitchhiker and second-chance name neither an Extension nor `trade_direction` (`greps.txt:5-6`, `:19-24`; `note:hitchhiker.md:33-38`, `note:second-chance.md:106-108`) and still form, because the frame binds the side. The other five name an Extension or `trade_direction` (`note:rubberband.md:45`, `note:backside.md:98`, `note:fashionably-late.md:40`, `note:nine-ema-scalp.md:45`, `note:vwap-continuation.md:40-41`). No `Direction(unbound)` refusal is built. The proposal sentence that refuses a def which names neither an oriented object nor the token (`PROPOSAL.md` part1:36) is the one that would kill those two after C3 / C7.

Grok, failing: keep his sentence and implement "bindable" as a note-token check, which is all the sentence specifies. Hitchhiker's count is 0 and second-chance's count is 0, and neither names Extension. The registry reports `not_evaluable: Direction(unbound)`. Two of the seven never form, while §2.1 has already given both frames a side.

## R2-3.1

FABLE'S

The note is `1 - Trading/Assumed Defaults.md`, outside `1 - Trading/4 - Strategies/`, read only by `load_assumed_tunables`. `load_vault_trade_defs` globs every `*.md` in `STRATEGIES_DIR` (`vault_loader.py:476`) and `_read_note` raises when frontmatter, `name:`, the definition section or the def unit is missing (`:44-82`). A row whose scope is not `per_trade(<slug>)` of that note raises (`:271-280`). Grok's path sits in that folder, so the load raises before any card. The dedicated reader validates through `TunableRegistry` (the same call the strategy unit uses at `:14-16`), accepts `global` and `per_trade(<slug>)`, and allows only `source ∈ {assumed, ruling}`. `TunableSource` gains `ASSUMED` (`tunables.py:63-66`). Who writes the note is not ruled here.

Grok, failing: write `1 - Trading/4 - Strategies/Assumed Defaults.md` with a global row and no def frontmatter. The next taxonomy load raises at `_read_note` (`:44-48`). Add frontmatter to get past that, and the global row raises at `:271-280`. The seven notes do not load. No scan.

## R2-3.2

NEITHER — `merge_tunables` hole-fill: a row from `load_assumed_tunables` may supply `value` and `source` for an engine row only when the engine `value` is null, the keys are equal, the units are equal, and the scopes are equal. Every other collision stays loud, including a strategy-note row on an engine key, a row whose scope differs from the engine row, and an assumed row whose engine value is no longer null. Engine null becoming non-null in the same load as deleting that assumed row is the quiet path; otherwise the merge raises. A per-trade row never fills a global key. Open cards keep the assumed keys they formed with. No migration. C2, `taxonomy/loader.py` only.

Grok requires `source == assumed` and matching scope, but any user row may fill, so a strategy note can fill a matching per-trade engine hole. Once `source` becomes `ruling` and the row stays in the note (R2-3.3), his predicate no longer qualifies and the key collides loud (`loader.py:18-25`). Fable limits the fill to her reader and keeps the engine's scope, so a per-trade assumed row fills a global null (`range.wick_ratio_max`, hub R1 row 18) for every def. `resolve_cfg` returns `row.value` by key only (`loader.py:40-42`); the widened value is what every def sees.

Grok, failing: `Rubberband.md`'s own tunables unit carries an engine key, `source: assumed`, scope equal to that engine row, engine value null. The merge fills from the strategy note. The assumed number never passed through the dedicated note.
Fable, failing: the assumed note has `range.wick_ratio_max` at `per_trade(rubberband)`, engine row global and null. Her fill keeps the engine scope. Hitchhiker's next `cfg` read gets rubberband's number.

## R2-3.3

FABLE'S

A row stops being assumed only when its `source` reads `ruling`. An edited value left at `source: assumed` keeps the mark. A ruled number for one of these keys stays in the note and does not move into committed `tunables.yaml`. That is the new-formation rule. The open card keeps `score_suppressed=assumed_formation` (R2-2.1, X8) either way.

The mark has to follow `source`, not "the value changed", or an edit clears L52(a) without a ruling. Keeping the number in the note is what lets R2-3.2 keep filling a null engine row after the ruling; moving it into `tunables.yaml` is the L32/L53 leak the sentence forbids. Deleting the row is not a third way to un-assume: the key then has no row, and `resolve_cfg` raises (`loader.py:47-49`).

Failing if this is rejected: edit the assumed note's value for `A-02`, leave `source: assumed`. The next hitchhiker card forms on the new number with no `assumed_formation` mark and a live `card_score`. The modelled stop buffer no longer degrades the score.

## R2-4.1

NEITHER — One `RadarScoreDetail` per (member, def) (`evaluate.py:593`). Both frames' evaluations are kept in the receipt. The published row is: if both frames would form, `not_formed` with note `both_sides` (v2 §1, F-19), not a card; if exactly one forms, that frame; if neither forms, the louder of the two — `not_evaluable` > `input_stale` > `avoided` > `not_formed` — and a tie publishes the long frame. C2. No migration. No new seam field.

Fable's order (`formed > avoided > input_stale > not_formed > not_evaluable`, ties to long) publishes a formed long card when both frames form, which §1 already refuses, and it hides `not_evaluable` whenever the other frame is anything else. Grok's O2 does not say which frame the one seam row carries.

Fable, failing: both frames' preconditions are true on the same scan. Her rule ties two `formed` results to the long frame and publishes a card. The scan was `both_sides`. A side was guessed.
Same rule, second scan: the long frame is `not_evaluable` (missing atom) and the short frame is `not_formed`. The seam row says `not_formed`. The missing atom is not on the published row.

## R2-4.2

NEITHER — Seam observations are computed per frame, on that frame's bars. The published `RadarScoreDetail` carries the published frame's observations; the other frame's stay in the receipt. Factor observations that the published frame consumed are that frame's, not a copy of the long frame's measurements onto a short card. Volume is unchanged by the mirror, so a volume-only factor may be computed once on the real bars. Price and direction factors are not. No `unmirror()` on every type (labels stay X12). C2, inside the frame evaluation. No migration.

The detail stores one evaluation's observations (`evaluate.py:45-47` in the excerpt, anchor `:593`). Computing them once on the real bars and attaching them to a short-frame trigger makes the receipt's inputs not the inputs that trigger used (L57). Grok's O2 does not mention observations. The factor formulas are not in the excerpts; X18 says which named factors actually change under the mirror.

Fable, failing: the short frame forms. `Extension.leg_count` and the seam observations were taken on the real bars. The trigger was resolved on mirrored bars. `replay` of the published detail cannot rebuild that trigger. The short card shows the long frame's price factor.
Grok, failing: no rule. A short card ships with whatever observations the long pass left in the one detail.

## R2-4.3

FABLE'S

The frame mirrors the daily series and the level set with the intraday bars. The same price map as the intraday bars (negate price, swap high and low; volume and time unchanged). Level labels are not this question; they stay X12. A daily level left in real price space is compared with a negated intraday price, and the short frame's level predicates are numeric nonsense.

Grok's O2 mirrors "bars" and negates prices before `Formation`. It does not mirror the daily series or the level set. That is the whole of his text, and it is not sufficient for a def whose precondition reads a daily level.

Grok, failing: short frame, hitchhiker. Intraday prices are negated; the daily level that precondition names is left on the real scale (`note:hitchhiker.md:38`). The comparison is across two price spaces. The short side does not form, for arithmetic, on a day the long side would. No short card.

## OWNER (after cards):

- Each assumed key is ruled, after cards on it exist, by setting that row's `source` to `ruling` in `1 - Trading/Assumed Defaults.md`; the number stays in the note. Not a precondition for C1 or for showing the card.
- Nothing else is asked of him before a card. Who writes the note is not an owner question in this round.

## EXPERIMENTS:

- X8: unchanged. Form a card on an assumed key, set that row's `source` to `ruling`, refresh. The open card still has `score_suppressed=assumed_formation` and null `card_score`. If the open card gains a score, the preserve in R2-2.1 was not actually on every writer.
- X12: unchanged, not ruled here. Labels and `why` strings.
- X18: on one stored day, compute `atrs_from_open`, `Extension.leg_count` and `htf_level_proximity` on the real bars and on the mirrored frame. If a factor differs, it stays per frame in the published row. If all three match, they may be computed once on the real bars.

TRIBUNAL R2: BUILD
~~~~

### GEMINI (`gemini-ruling-r2.md`, printed; hub wrote it byte for byte without the harness's `[exited with code 0]`; done 16:08:00)

~~~~
**R2-2.1**
`FABLE'S`
Reasoning: Grok's persistent `score_suppressed = assumed_formation` string is overwritten on the very next refresh because `refresh_card` (`evaluate.py:800`) recomputes suppression solely from dots (`scoring.py:247-251`). Failing scenario (objection to Grok): a Hitchhiker card formed on assumed `A-02` shows a score after one refresh, leaking an assumed score. Furthermore, Grok's permanent null score causes `WATCH` to order by `pool_position` (due to `nulls last` in `TIE_POLICY`, `evaluate.py:134`), violating ADR-0009 D4. Fable's tappable dot utilizes existing suppression flawlessly.

**R2-2.2**
`FABLE'S`
Reasoning: Grok's runtime recorder wrapped around the interpreter `cfg` misses direct reads from `_cfg_value` and `from_tunables` (`evaluate.py:653, 528`), as hub check R1 row 26 confirms. Failing scenario (objection to Grok): a Fashionably Late card reading `bars_cleared` forms silently without the assumed mark. Fable's static declared-key closure accurately captures all dependencies by following the existing `TUNABLE_KEYS` pattern (`extension.py:40-44`) with no runtime gaps.

**R2-2.3**
`FABLE'S`
Reasoning: Rubberband relies on convention `A-01`. Because `A-01` is not a `cfg` key, Grok's recorder ignores it. Failing scenario (objection to Grok): a Rubberband card evaluates `A-01` but receives no assumed mark, leaking the number. Fable correctly handles this by converting all 23 conventions into `label` rows; the relation resolver declares `A-01` in its `tunable_keys`, seamlessly propagating the `assumed_formation` dot to the card.

**R2-2.4**
`FABLE'S`
Reasoning: Grok's attempt to attach `A-13` directly to `AtomOutcome` fails because the model strictly inherits `extra="forbid"` from `BaseModel` (`seam.py:100`). Failing scenario (objection to Grok): evaluating a card with `A-13` crashes the scan instantly with a Pydantic `ValidationError`. Fable correctly lets the resolver declare `A-13` in its static closure, passing the mark to the card via the `assumed_formation` dot without mutating the atom.

**R2-2.5**
`FABLE'S`
Reasoning: Fable passes X8 by successfully marking `A-13`. Because Fable's dot is tappable, the trader can tap to lift the suppression, which immediately restores the `card_score`. Consequently, `WATCH` stays correctly ordered by `card_score desc` per the `TIE_POLICY` (`evaluate.py:134`), completely honoring ADR-0009 D4. Failing scenario (objection to Grok): Grok's permanent null score sinks the card to `pool_position` sorting, destroying `card_score` ranking.

**R2-1**
`FABLE'S`
Reasoning: The v2 mirrored frame inherently binds `trade_direction` via `ext.direction` and the `valid_setups` relation (`evaluate.py:643-650`). No definition stays unbound. Failing scenario (objection to Grok): Hitchhiker and Second Chance Scalp lack any `trade_direction` strings (`greps.txt:4-11`). Under Grok's `Direction(unbound)` refusal, these valid setups would be incorrectly rejected in every scan as `not_evaluable`.

**R2-3.1**
`NEITHER — The assumed rows live in ONE vault note OUTSIDE 1 - Trading/4 - Strategies/ — 1 - Trading/Assumed Defaults.md. A dedicated reader, load_assumed_tunables(vault_root), validates the unit.`
Reasoning: Grok's design places the note in `1 - Trading/4 - Strategies/`. Failing scenario (objection to Grok): `vault_loader.py:476` globs all `*.md` there, and `:317-366` instantly crashes the taxonomy load with a `VaultTaxonomyError` because the defaults note lacks `trade_def:` frontmatter and a `DEFINITION_SECTION`. Fable's placement outside with a dedicated reader completely avoids this crash.

**R2-3.2**
`NEITHER — In merge_tunables, an assumed row may fill an engine row iff the engine row's value is None, the assumed row comes strictly from the dedicated assumed reader, and their scopes match exactly.`
Reasoning: Grok allows a per-trade row to fill a global key (R1 row 18). Failing scenario (objection to Grok): a trader adds a global tunable to a strategy note, silently redefining an engine parameter. Fable allows a strategy note to fill an engine hole. Failing scenario (objection to Fable): an assumed unit inside a strategy note fills an engine hole, silently affecting all cards. Matching scopes strictly closes both holes.

**R2-3.3**
`NEITHER — A row stops being assumed only when its source reads ruling. Once ruled, an engine key MUST move into committed tunables.yaml; it does not stay in the note.`
Reasoning: Fable's (e) correctly uses `source`, but incorrectly claims a ruled engine key stays in the note. Failing scenario (objection to Fable): an owner rules on a global engine key, keeping it in `Assumed Defaults.md`; a second Cobalt install syncing the repo runs on a `null` value, causing divergent engine behavior. Grok incorrectly lets an owner edit drop the mark. Failing scenario (objection to Grok): a trader edits a value to test, silently dropping the mark for an unruled number.

**R2-4.1**
`NEITHER — One evaluation is published per (member, def): the better of the two frames by formed > avoided > input_stale > not_formed > not_evaluable (ties to the long frame). The other is kept in the receipt.`
Reasoning: `evaluate.py:593` dictates exactly one `RadarScoreDetail` per evaluation. Grok completely omits how to merge two frames. Failing scenario (objection to Grok): when one frame evaluates to `not_formed` and the other to `input_stale`, lacking Fable's strict precedence hierarchy causes the seam row to publish one randomly, destroying determinism.

**R2-4.2**
`NEITHER — Factor observations and seam observations are computed ONCE on the real bars, never per frame.`
Reasoning: Factors like `rvol` and `atrs_from_open` (`evaluate.py:33`) are direction-agnostic. Grok implies observations might run per frame. Failing scenario (objection to Grok): computing direction-agnostic factors twice per scan redundantly wastes CPU cycles across the long and short frames on identical data.

**R2-4.3**
`NEITHER — The frame negates prices before Formation and RadarCardSpec, and keeps labels frame-local. Intraday bars, daily series, and level sets are NEVER mirrored.`
Reasoning: Fable hallucinates `unmirror()` and repurposes `mirror`. Failing scenario (objection to Fable): `grep unmirror` is empty, and `mirror` strictly runs the S3 user-side note sync (`runner.py:223`, `notes.py:686`). Attempting to "unmirror" daily series crashes the evaluator with a missing function. Grok is correct to limit adjustments to negating prices.

OWNER (after cards):
None

EXPERIMENTS:
None

TRIBUNAL R2: BUILD AFTER applying the NEITHER replacements
~~~~

### ASTRA (`astra-ruling-r2.md`, the final message once; exit 0, ≈16:10:30; `[PARTIAL]` marks: none — all 12 questions ruled in full)

~~~~
ITEM R2-2.1

**GROK'S**

- Persist formation suppression permanently; a tap does not verify assumed formation inputs.
- Fable fails when a hitchhiker card formed using A-02 receives a grade on its assumption dot: the blocker disappears and a numeric score becomes possible (`cards/scoring.py:247–267`).
- Null-score ties do not introduce another ranking authority: WATCH explicitly orders by `card_score` first, then its tie breakers (`radar/evaluate.py:134–138`).
- All-assumed cards consequently lack score differentiation. Disclose that limitation.
- Preserve the formation blocker through refresh and tap-triggered scoring; current refresh does not preserve it (`radar/evaluate.py:777–800`).

ITEM R2-2.2

**NEITHER — replacement wording:**

> C2 uses a static, transitive dependency closure. Every atom, detector, trigger, stop, relation resolver and frame/orientation convention declares its tunable dependencies, including literal `cfg` references in the definition. Conventions are label-valued rows; unsupported labels produce a named `not_evaluable` result. The closure includes implicit evaluator dependencies, including A-01, and all dependencies reachable through declared components. At formation, snapshot the resolved rows with `source: assumed` as `Formation.assumed_keys`; persist those keys with the card and apply the permanent formation suppression. This is conservative dependency provenance, not a claim that every listed branch executed. A registry check rejects undeclared or unresolved dependencies.

- Fable’s detector precedent holds: `TUNABLE_KEYS` enumerates `from_tunables` dependencies (`radar/anatomy/extension.py:40–63`).
- Its closure over what definitions name can miss Rubberband’s implicit A-01 convention; Grok’s read wrappers also miss a convention executed without a tunable read (`v2-sections.excerpt.md:49–53`).
- Include literal cfg references and implicit dependencies to cover interpreter, trigger and stop paths (`radar/evaluate.py:419–422,601–602,653–657`).
- Cost: C2, M; registry/resolver declarations, evaluator/Formation, card models/store/view and panel; one provenance-column/view migration, no runtime recorder.

ITEM R2-2.3

**NEITHER — replacement wording:**

> C1 marks every newly formed Rubberband card with persisted `score_suppressed = assumed_formation` and `card_score = null`, because its orientation uses A-01. C1 displays `ASSUMED · A-01` from that persisted formation marker; it does not wait for C2’s generic chip. Refresh and tap score paths preserve the marker and null score while continuing to calculate proximity. C1 needs no assumed-key closure or new database column. C2 adds the generic provenance storage and chip; its migration maps C1-marked Rubberband cards to `{A-01}` without clearing their suppression.

- Grok postpones the chip until C2, leaving the first Rubberband card without a visible A-01 explanation; C1 already depends on that assumption (`v2-sections.excerpt.md:49–53,155–156`).
- Fable depends on a closure absent from C1; tapping its dot also removes degradation (`cards/scoring.py:247–267`).
- Setting only the create-time string fails on refresh: the UPDATE writes both score and suppression (`cards/store.py:1039–1047`; `radar/evaluate.py:777–800`).
- Cost: C1, S additional logic plus lifecycle checks; evaluator, scoring callers/store guard and panel; no C1 migration. Generic provenance uses C2’s migration.

ITEM R2-2.4

**NEITHER — replacement wording:**

> A-13 applies only to the definition’s `catalyst_ref` precondition resolver. That resolver declares A-13 in its dependency closure. `AtomOutcome` remains unchanged; the ordinary boolean outcome and the persisted formation-key snapshot together identify the assumed result. The card displays A-13 in its permanent assumption chip and remains suppressed under R2-2.1. Extension path B retains `catalyst_ref_unknown`; A-13 does not make that path evaluable.

- Grok’s proposed nine-ema-scalp atom with `assumed=A-13` violates the declared closed schema: that field does not exist (`radar/seam.py:99–117`).
- Fable correctly avoids a schema addition, but its tappable dot lets an A-13 card regain a score (`cards/scoring.py:247–267`).
- Path B’s existing refusal remains explicit (`radar/anatomy/extension.py:140–144`; `radar/evaluate.py:620–622`).
- Cost: C5, S resolver declaration using C2’s artifacts; no additional seam field or migration.

ITEM R2-2.5

**GROK'S**

- Immutable formation suppression meets X8’s specified assertion after the source becomes `ruling` (`v2-sections.excerpt.md:180`).
- Fable fails when that sequence is followed by an assumption-dot tap (`cards/scoring.py:247–267`).
- WATCH stays ordered by `card_score DESC NULLS LAST`, followed by existing tie breakers; suppressed cards tie at null (`radar/evaluate.py:134–138`).
- This is design compliance, not an executed test pass. X8 must cover persistence, reload, refresh and tapping; current refresh fails the required preservation (`radar/evaluate.py:777–800`).

ITEM R2-1

**FABLE'S**

- From C2, the frame binds direction; none of the seven remains unbound merely because its note lacks an orientation token (`v2-sections.excerpt.md:77–83`).
- The supplied counts establish absent `trade_direction` references for hitchhiker and second-chance; their cited anatomy does not require an unqualified Extension (`greps.txt:6–11,19–24`; `Hitchhiker.md:35,68`; `Second Chance Scalp.md:106–108`).
- A note-based Grok refusal could reject second-chance before an otherwise valid frame evaluation.
- If Grok’s “bindable” includes the frame, its condition is unreachable for these seven; prefer the smaller mechanism.
- C1 remains Rubberband-only (`v2-sections.excerpt.md:49–51`).

ITEM R2-3.1

**FABLE'S**

- Use the note outside Strategies and the dedicated `load_assumed_tunables(vault_root)` reader.
- Grok’s defaults-only Markdown note is enumerated as a strategy and rejected for lacking its required definition structure (`taxonomy/vault_loader.py:317–366,476–477`).
- Adding strategy frontmatter would still leave global rows incompatible with the strategy reader’s per-trade scope restriction (`taxonomy/vault_loader.py:271–280`).
- C2 must add `TunableSource.ASSUMED` before validating those rows (`taxonomy/tunables.py:63–66`; `v2-sections.excerpt.md:156`).
- This selects the location/reader clause. Merge semantics follow below; note authorship is outside this round.

ITEM R2-3.2

**NEITHER — replacement wording:**

> Keep strategy-note rows and dedicated-default-reader rows in separate, provenance-bearing inputs. A dedicated-reader row may fill an engine hole if and only if its key equals the engine key, its scope equals the engine scope, its unit equals the engine unit, the committed engine value is null, its supplied value is non-null, and its source is `assumed` or `ruling`. Copy only value and source into the effective engine row; retain its structural metadata and receipt provenance. Strategy-note collisions, duplicate suppliers and every other collision fail loudly. A row cannot obtain dedicated-reader provenance by declaring a source field. An engine row becoming non-null while its supplier remains present fails the load.

- Grok lacks reader provenance and unit equality: a strategy-note row with matching key/scope and `source: assumed` could fill an engine hole (`taxonomy/loader.py:90–112`, current collision boundary).
- Fable lacks scope equality: a per-trade supplier could populate a global key subsequently returned for other setups (`taxonomy/loader.py:115–128`).
- Grok’s assumed-only predicate also rejects the next load when a valid supplier changes to `source: ruling`.
- Cost: C2, S within store work; loader, dedicated reader result type and collision tests; no database migration.

ITEM R2-3.3

**FABLE'S**

- In this store, editing a value with `source: assumed` preserves its assumption status; an actual ruling is represented by `source: ruling` (`v2-sections.excerpt.md:125`).
- The ruled value stays in the note; R2-3.2 accepts that supplier while the committed engine value remains null.
- Grok’s engine-transfer sequence would move the private ruled value into committed configuration, contrary to the supplied store constraint (`NEEDS-ROUND-2.md`, Fable (e), quoting the derive’s source range :71–105).
- Existing cards retain their formation provenance and suppression; subsequent formations use the newly resolved source (`v2-sections.excerpt.md:125,180`).

ITEM R2-4.1

**NEITHER — replacement wording:**

> C2 publishes one evaluation per `(member, definition)` per scan. Select the frame by `formed > avoided > input_stale > not_formed > not_evaluable`, with ties selecting the long frame. Publish that frame’s state, atoms, missing atoms, extension path and formation timestamp together; never combine them with the other frame’s outcome. Add a typed receipt artifact containing `selected_frame` and both frame evaluations, normalized to real-world coordinates. Persist it in the evaluation’s detail JSON, with backward-compatible optional fields for older receipts. Each frame evaluation includes its state, reasons and existing `RadarScoreDetail` payload, without recursive nesting.

- Fable supplies selection but no concrete artifact for the other evaluation; the closed detail model lacks frame identity and a second outcome (`radar/seam.py:141–155`).
- Concrete failure: long is `not_formed`, mirrored is `not_evaluable`; the current single payload cannot retain both states and reasons.
- Grok leaves that same scan’s selection unspecified (`v2-sections.excerpt.md:77–79`).
- Select complete results, preserving their associated evidence (`radar/evaluate.py:593–596,609–623`).
- Cost: C2, S–M; evaluator orchestration, seam receipt models and consumers; no relational migration if stored in existing detail JSON.

ITEM R2-4.2

**NEITHER — replacement wording:**

> Frame-independent source measurements may be computed once on real bars and shared. Formation atoms and their consumed seam observations are evaluated per frame, retained with that frame’s result and normalized for publication. After selecting the frame, compute the card’s factor observations once using real bars and the selected formation’s direction and anchor where required. Do not publish a real-bars observation as evidence of a different frame computation. Reuse an observation across frames only where its definition establishes that it is frame-independent.

- Fable’s blanket once-only seam rule fails when a mirrored slope predicate consumes a signed measurement different from the long frame’s measurement (`v2-sections.excerpt.md:81–83`).
- The resulting receipt could pair a passing mirrored predicate with the untransformed long-frame slope.
- Grok leaves unspecified which of two frame observation sets supports the single card (`v2-sections.excerpt.md:77–85`; `radar/evaluate.py:593–596`).
- Current observations have no frame identity; R2-4.1 supplies that association (`radar/seam.py:103–108`).
- Cost: C2, S–M within frame/receipt work; evaluator and observation adapters; no additional migration.

ITEM R2-4.3

**FABLE'S**

- Mirror daily series and levels alongside intraday inputs; restore typed prices, signed directions and paired labels before publication.
- Grok’s intraday price wording leaves a concrete mixed-coordinate failure: a mirrored intraday price compared against an unmirrored daily level (`v2-sections.excerpt.md:77–83`).
- Fable explicitly includes daily series and levels and renders prose after unmirroring (`NEEDS-ROUND-2.md`, O2, quoting the derive’s source range :71–105).
- This establishes the coordinate contract; detector equivalence, rounding and label correctness remain experiments (`v2-sections.excerpt.md:87,181`).

OWNER (after cards): Review the displayed assumed keys; any rulings affect new formations, without rehabilitating historical formation evidence.

OWNER (after cards): Assess the usefulness of null-score WATCH ties after seeing cards; no assumption-dot tap lifts degradation.

EXPERIMENTS:

X8: On synthetic or definition-written fixtures, form an assumed card, persist/reload it, change its supplier to `ruling`, then refresh and tap. The original card must retain its assumption provenance, `score_suppressed=assumed_formation` and null score. Any loss requires fixing lifecycle persistence before deployment.

X12: Form a mirrored-frame card on a fixture independent of the owner’s trades. Inspect `why`, `extreme`, `raw`, `rounded`, `inputs`, daily levels and labels. Leaked mirrored prices or incorrect directional labels require correcting typed normalization before publication.

X18: Exercise the dedicated loader with matching suppliers, mismatched units/scopes, strategy-origin collisions, duplicates and engine-null transitions. Acceptance outside R2-3.2’s predicate requires revising merge validation.

X19: Evaluate fixtures covering each pair of non-formed frame states and frame-dependent observations. Assert deterministic selection and round-trip retention of both results. Lost or mismatched evidence requires revising the receipt artifact.

X20: Compare declared closures against instrumented reads in fixtures covering cfg, trigger, stop, detector and convention paths. Missing dependencies require repairing declarations; this instrumentation is a verification tool, not a production recorder.

No experiments were executed; this round was read-only.

TRIBUNAL R2: BUILD AFTER incorporating these replacements and assigning their chunk gates.
~~~~

## Checked against the files

Every claim below was checked by opening the real file on main at HEAD (Read, or `grep -n` / `grep -rl`), the notes under `/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies/`, LAWS.md, ADR-0009, `cards/radar.py`, `cards/store.py`, `configs/cobalt/taxonomy/tunables.yaml`, or the staged packet. Note: several house cites resolve inside the packet's excerpt files (`*.excerpt.py`, `v2-sections.excerpt.md`, `greps.txt`), not in the real files at that number — marked `(excerpt line)`. Notes cited by `note:line` only; no wording copied. `= C<n>` / `= R1 row n` = same fact as the Fable-claims table above / `hub-checks.md`.

READ FACTS the checks turned up (unclaimed by any house; no verdict): **(F1)** the six engine rows with `value: null` (`tunables.yaml:74, 83, 158, 186, 195, 204`) carry scopes `global` ×3 (`:76, :85, :160`) and `per_indicator(ema9)` / `per_indicator(vwap)` ×3 (`:188, :197, :206`); no engine row is `per_trade(...)` (`grep -n "scope: per_trade"` finds none). v2 §8 says assumed rows carry `global` or `per_trade(<slug>)`. **(F2)** `store.py:1215-1224`: the tap path re-reads dots from the DB (`_dots_for`) and recomputes `suppression(dots)`, then UPDATEs `score_suppressed`; `store.py:1049-1050` upserts dots in `update.dots` (no delete in the excerpt). **(F3)** `evaluate.py:565-577`: the seam-observation list holds two price-valued entries (`session_open`, `last_close`) and magnitudes/counts/rvol; `extension.py:115` computes `distance_from_open_atr` with `abs()`. **(F4)** `evaluate.py:547-550`: `htf_range_break` is called with the daily series AND the intraday run's session high/low. **(F5)** `DayRange` / `upper_third` appear in no file under `src/cobalt` (`grep -rl` empty). **(F6)** `bars_cleared` occurs in one of the 22 notes in the Strategies folder (`Rubberband.md`); `Fashionably Late.md` has 0. **(F7)** `ADR-0009:28` "`card_score` is the only number that orders WATCH cards; pool `last_rank` only admits"; `:43` "`trail_fit` is N/A and suppresses the score until tapped or re-sourced by the trader". **(F8)** `cards/radar.py:179-183`: WATCH sort key = (`card_score` desc nulls-last, `pool_position` asc nulls-last, ticker, card_id). **(F9)** unqualified `Extension` appears at `Rubberband.md:45`, `Backside Scalp.md:98`, `Fashionably Late.md:40`; `9 EMA Scalp.md:78` names `Extension … on Leg(pre_test)`; `trade_direction` at `9 EMA Scalp.md:45` and `VWAP Continuation.md:40-41`.

| # | claim · who | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| G1 | R2-2.1: `refresh_card` recomputes suppression solely from dots · gemini | `evaluate.py:774-800`; `scoring.py:247-251` | HOLDS | = R1 row 17; = R1B row 8. |
| G2a | R2-2.1/2.5: `nulls last` in `TIE_POLICY` sends all-null WATCH cards to `pool_position` order · gemini | `evaluate.py:134-138`; `cards/radar.py:179-183` | HOLDS | Sort key is card_score desc nulls-last, then pool_position, ticker, card_id (F8). |
| G2b | … "violating ADR-0009 D4" · gemini | `ADR-0009:28` | UNVERIFIABLE FROM READS | D4 says card_score is the only number that orders WATCH cards and `last_rank` only admits; whether a tie-break is "ordering" is a reading. Both texts quoted (F7, F8). |
| G3 | R2-2.2: recorder on `cfg` misses `_cfg_value` / `from_tunables` reads (`evaluate.py:653, 528`) · gemini | `evaluate.py:419-422,528,601-602,653,656` | HOLDS | = R1 row 26; = R1B row 9. |
| G4 | R2-2.2 scenario: a Fashionably Late card reading `bars_cleared` · gemini | `evaluate.py:653`; `Fashionably Late.md` (`grep -c` 0); `grep -rl` over Strategies | DOES NOT HOLD | `bars_cleared` is read from trigger params at :653; only Rubberband.md carries it (F6); Fashionably Late has none. |
| G5a | R2-2.2: "the existing `TUNABLE_KEYS` pattern (`extension.py:40-44`)" across resolvers · gemini | `extension.py:40-44`; greps.txt | DOES NOT HOLD | = C7b: one detector module declares keys; nothing else does. The constant itself exists (= C7a). |
| G5b | … "no runtime gaps" · gemini | — | UNVERIFIABLE FROM READS | Nothing built; astra's X20 (declared closure vs instrumented reads) is the run. |
| G6 | R2-2.3: Fable converts "all 23 conventions" into `label` rows · gemini | `NEEDS-ROUND-2.md` Fable (d) | DOES NOT HOLD | Fable's text lists 12 convention keys as rows (`A-01, A-05, A-06, A-12, A-13, A-14, A-15, A-17, A-18, A-21, A-22, A-23`); "One mechanism marks all 23" is Fable's wording. |
| G7 | … "the relation resolver declares `A-01` in its `tunable_keys`" · gemini | `evaluate.py:635-639`; greps.txt `TUNABLE_KEYS` | UNVERIFIABLE FROM READS | No relation resolver exists at HEAD: direction is inline at :635-639; only `extension.py` declares keys. |
| G8 | R2-2.4: `AtomOutcome` inherits `extra="forbid"` (from `BaseModel`) · gemini | `seam.py:99-100`, `:111` | HOLDS | = C1. It inherits from `_Closed(BaseModel)`, not `BaseModel` directly. |
| G9 | … evaluating a card with `A-13` on the atom "crashes the scan instantly" · gemini (grok K11 same) | `seam.py:100`; `evaluate.py:588-592` | UNVERIFIABLE FROM READS | Construction with an unknown kwarg is refused by the model config; nobody ran it, nor read whether the caller of `detail()` catches it. Run: E1 below. |
| G10 | R2-2.5: "Fable passes X8 by successfully marking `A-13`" · gemini | `v2-sections.excerpt.md:180` (X8 row) | DOES NOT HOLD | X8 is: change a row's `source` to `ruling`, assert the open card still has `score_suppressed=assumed_formation`. It does not mention `A-13`. |
| G11 | … a tap lifts the suppression and restores `card_score` · gemini | `scoring.py:238-267`; `store.py:1215-1224` | HOLDS | = C3; the tap path recomputes score from the dots (F2). |
| G12a | R2-1: direction bound via `ext.direction` and the `valid_setups` relation (`evaluate.py:643-650`) · gemini | `evaluate.py:635-639` | HOLDS | Code binds it at :635-639; :643-650 is the `not_evaluable` return and setup label — a mis-cite. |
| G12b | … "the v2 mirrored frame inherently binds `trade_direction`" · gemini | greps.txt (`unmirror`/`mirror`) | UNVERIFIABLE FROM READS | No frame code exists; the only `mirror` hits are the S3 note mirror. |
| G13 | R2-1: Hitchhiker, Second Chance have no `trade_direction` (`greps.txt:4-11`) · gemini | `greps.txt:6-7, 10-11`; notes | HOLDS | = C4. Counts 0 and 0. |
| G14 | R2-3.1: `:476` globs all `*.md`; `:317-366` crashes without `trade_def:` frontmatter / definition section · gemini | `vault_loader.py:476`, `:327-331`, `:352-356` | HOLDS | = C6. |
| G15 | R2-3.2: "Grok allows a per-trade row to fill a global key (R1 row 18)" · gemini | `NEEDS-ROUND-2.md` Grok (O5) | DOES NOT HOLD | Grok's O5 requires `user scope == engine scope`; R1 row 18 is about the PROPOSAL's key-only hole-fill. (`QUESTIONS-R2.md`, from the derive, also attributes that hole to Grok — both quoted, neither smoothed.) |
| G16 | … "Fable allows a strategy note to fill an engine hole" · gemini | `NEEDS-ROUND-2.md` Fable (O5) | DOES NOT HOLD | Fable's text: only "a row from THAT reader" (`load_assumed_tunables`) fills; a strategy-note row is not read by it. The derive's R2-3.2 question phrases the strategy-note hole as Fable's. |
| G17 | … "matching scopes strictly closes both holes" · gemini | `tunables.yaml:74-206` (F1) | UNVERIFIABLE FROM READS | Design not built. F1: the six null engine rows are global ×3 / per_indicator ×3, none per_trade; Fable's reader accepts global and per_trade only. |
| G18 | R2-3.3: Fable (e) says a ruled number stays in the note · gemini | `NEEDS-ROUND-2.md` Fable (e) | HOLDS | Fable (e): "it stays in the note". |
| G19 | … "Once ruled, an engine key MUST move into committed `tunables.yaml`" · gemini | `LAWS.md:178` (L32), `:279` (L53) | DOES NOT HOLD | Conflicts with the TEXT of L32 (user data = strategies/settings, cheat-sheet-derived) and L53 (committed config carries engine tunables only). The hub reads no law; it is his/the desk's (L73). |
| G20 | … a second install "runs on a `null`" (divergent behaviour) · gemini | — | UNVERIFIABLE FROM READS | Nothing built; the engine rows are `null` by design (`tunables.yaml:26-27`). |
| G21 | … "Grok incorrectly lets an owner edit drop the mark" · gemini | `NEEDS-ROUND-2.md` Grok (O5) | DOES NOT HOLD | Grok's O5 has no such sentence; its "Owner edit of the unit: human wins (L28)" is about which write prevails. |
| G22 | R2-4.1: `evaluate.py:593` gives one `RadarScoreDetail` per evaluation · gemini | `evaluate.py:514-515,583-596` | HOLDS | = C9. |
| G23 | … "Grok completely omits how to merge two frames" · gemini | `v2-sections.excerpt.md:77-79` | HOLDS | Grok's O2 text (F-04) has no publication rule. |
| G24 | … "publish one randomly" · gemini | — | UNVERIFIABLE FROM READS | No code publishes two frames. |
| G25 | R2-4.2: `rvol`, `atrs_from_open` direction-agnostic (`evaluate.py:33`) · gemini | `evaluate.py:429`; `extension.py:115` | HOLDS | :429 lists `FACTOR_COMPUTERS`; distance uses `abs()`; volume unchanged in F-04. Cite :33 is a docstring (DIRECTION, :34-37). `htf_level_proximity` not addressed. |
| G26 | R2-4.3: `unmirror` is absent; `mirror` = S3 note sync (`runner.py:223`, `notes.py:686`) · gemini | greps.txt; `runner.py:221-230`; `notes.py:686,724` | HOLDS | Only `mirror_sources` / `_mirror_rows` (note mirror). `unmirror()` is a proposal (Fable O2), not claimed to exist. |
| G27 | … "Intraday bars … are NEVER mirrored" · gemini | `v2-sections.excerpt.md:79` | DOES NOT HOLD | F-04 (Grok's O2, which gemini calls correct): "Short = the same detectors on mirrored bars (price → −price, high ↔ low …)". |
| G28 | … unmirroring "crashes the evaluator with a missing function" · gemini | — | UNVERIFIABLE FROM READS | Nothing built. |
| A1 | R2-2.1: after a tap on its dot the blocker disappears and a score becomes possible · astra (grok K1) | `scoring.py:247-251,264-267` | HOLDS | `suppression()` needs `trader_grade is None`; `card_score` returns an int with conviction, proximity and no suppression. |
| A2 | WATCH orders by `card_score` first (`evaluate.py:134-138`) · astra | `evaluate.py:134-138`; `cards/radar.py:179-183` | HOLDS | (F8). |
| A3 | current refresh does not preserve a create-time blocker (`:777-800`) · astra | `evaluate.py:777-800` | HOLDS | = R1 row 17. |
| A4 | R2-2.2: `TUNABLE_KEYS` enumerates `from_tunables` dependencies · astra | `extension.py:40-63` | HOLDS | = C7a. |
| A5a | … Grok's read wrappers miss a convention executed without a tunable read · astra | R1 hub ESCALATE 3; `evaluate.py:636-637` | HOLDS | `A-01` is applied in evaluator code (:636-637), neither a cfg key nor a resolver. |
| A5b | … Fable's closure over what definitions name can miss Rubberband's implicit `A-01` · astra | `extension.py:40-44`; `evaluate.py:635-639` | UNVERIFIABLE FROM READS | Fable's text puts `A-01` in convention rows read by a "relation resolver"; no such resolver exists at HEAD (G7). |
| A6 | R2-2.3: C1 depends on `A-01` (`v2-sections.excerpt.md:49-53,155-156`) · astra | those excerpt lines | HOLDS | :53 F-08; :155 C1 row. |
| A7 | … a create-time string alone fails on refresh: the UPDATE writes both (`store.py:1039-1047`) · astra | `store.py:1039-1047`; `evaluate.py:777-800` | HOLDS | = R1 row 17. |
| A8 | … C1 needs no new database column · astra | `store.py:1041-1044`; `cards/radar.py:61` | HOLDS | `score_suppressed` is an existing column and badge (COBALT). Whether the panel can render a C1 chip from it is design (not read). |
| A9 | R2-2.4: `AtomOutcome` is closed; Fable's dot lets an `A-13` card regain a score; path B refusal explicit · astra | `seam.py:99-117`; `scoring.py:247-267`; `extension.py:140-144`; `evaluate.py:620-622` | HOLDS | = C1, C3, C8. |
| A10 | R2-2.5: X8's assertion is specified (`:180`); refresh currently fails preservation · astra | `v2-sections.excerpt.md:180`; `evaluate.py:777-800` | HOLDS | (excerpt line). |
| A11 | R2-1: counts and lines (`greps.txt:6-11,19-24`; `Hitchhiker.md:35,68`; `Second Chance Scalp.md:106-108`); C1 Rubberband-only (`:49-51`) · astra | greps.txt; notes; `v2-sections.excerpt.md:51` | HOLDS | = C4. `Hitchhiker.md:35,68` are `Leg(...)` lines. |
| A12 | R2-3.1: strategy-folder note raises; global rows refused; `TunableSource` needs `ASSUMED` · astra | `vault_loader.py:317-366,476-477,271-280`; `tunables.py:63-66` | HOLDS | = C5, C6; the enum has RULING, SHEET, DWV and `TunableRow.source` is typed to it. |
| A13 | R2-3.2: Grok has no reader provenance / unit equality, so a strategy-note row with matching key/scope and `source: assumed` could fill · astra | `NEEDS-ROUND-2.md` Grok (O5); `loader.py:90-112` | HOLDS | A reading of Grok's text (no provenance or unit clause). Reachable today only if an engine null row were `per_trade` — none is (F1). |
| A14 | … Fable lacks scope equality; a per-trade supplier could populate a global key (`loader.py:115-128`) · astra | `loader.py:115-136`; `tunables.yaml:73-80` | HOLDS | = R1 row 18; `resolve_cfg` returns `row.value` by key. |
| A15 | … Grok's assumed-only predicate rejects the next load once a supplier is `ruling` · astra (grok K19) | `loader.py:104-111` | HOLDS | Grok's O5 lets only `source == assumed` fill; any other same-key row is a collision, which raises. |
| A16 | R2-3.3: edits with `source: assumed` keep the mark; ruling = `source: ruling` (`:125`) · astra | `v2-sections.excerpt.md:125` | HOLDS | v2 §7 "How a value stops being assumed". |
| A17 | … Grok's engine-transfer sequence would move the private ruled value into committed config · astra | `NEEDS-ROUND-2.md` Grok (O5) | UNVERIFIABLE FROM READS | Grok says "Engine null → non-null in the same load as dropping the assumed row" and does not say where the non-null value comes from. |
| A18 | R2-4.1: the closed detail model has no frame identity or second outcome (`seam.py:141-155`) · astra | `seam.py:141-156` | HOLDS | Fields: atoms, missing_atoms, observations, extension_path, formed_bar_ts; `extra="forbid"`. |
| A19 | … Grok leaves selection unspecified (`:77-79`) · astra | `v2-sections.excerpt.md:77-79` | HOLDS | = G23. |
| A20a | R2-4.2: observations have no frame identity (`seam.py:103-108`) · astra | `seam.py:103-108` | HOLDS | `SeamObservation`: name, value, bar_ts. |
| A20b | … a mirrored slope predicate consumes a signed measurement that differs from the long frame's · astra | `v2-sections.excerpt.md:83`; `evaluate.py:565-577` | UNVERIFIABLE FROM READS | `EMA9.slope` is a predicate atom named in v2; the seam-observation list holds two prices and magnitudes (F3). Nothing built. |
| A21 | R2-4.3: a mirrored intraday price could meet an unmirrored daily level · astra (grok K25 same) | `evaluate.py:547-550` | HOLDS | (F4) the daily series and the intraday session high/low are passed together to `htf_range_break`; what a mirrored run gives it is unrun (X12). |
| K1 | R2-2.1: a computed dot stops blocking once `trader_grade` is set; `card_score` = conviction × proximity (`scoring.py:247-248`, `:86-88`) · grok | `scoring.py:247-251,264-267` | HOLDS | = A1. `:86-88` is the excerpt line; real file :264-267. |
| K2a | … `refresh_dots` rebuilds only quality-factor dots (`:216-235`) · grok | `scoring.py:201-235`; `evaluate.py:774-777` | HOLDS | = C3b: it returns only dots present in `fresh`. |
| K2b | … "so an appended `assumed_formation` dot is gone on the next scan" · grok | `evaluate.py:774-777` | UNVERIFIABLE FROM READS | True of `refresh_dots` as written; whether a not-yet-built append also runs at refresh is Fable's unwritten detail. Run: E2. |
| K3 | … Grok's O4 trigger ("assumed cfg key or assumed resolver, `A-01` included") does not fire for `A-01`; contradicts his own C1 sentence · grok | R1 hub ESCALATE 3; `NEEDS-ROUND-2.md` Grok (O4) | HOLDS | `A-01` is neither a cfg key nor a resolver. |
| K4 | … WATCH is `card_score desc nulls last` then `pool_position` (`evaluate.py:134-136`, `cards/radar.py:179-182`); `pool_position` is pool `last_rank` (`evaluate.py` part3:129) · grok | `evaluate.py:134-138`; `cards/radar.py:179-183`; `../r1/evaluate.py.part3:129` | HOLDS | Line 129: `pool_position=raw.get("last_rank")`. |
| K5 | … ADR-0009:43 "already nulls `trail_fit` until tap"; `:28` describes the ladder · grok | `ADR-0009:28,43` | HOLDS | :43 says `trail_fit` suppresses the score "until tapped or re-sourced by the trader" — the same line also describes a suppression that lifts (F7). |
| K6 | … the UPDATE at `cards/store.py:1222` is another writer of `score_suppressed` · grok | `store.py:1215-1224` | HOLDS | The tap path recomputes it from dots (F2). |
| K7 | R2-2.2: `_cfg_value` and `from_tunables` read outside the interpreter `cfg` (`evaluate.py:419-426`, `extension.py:24-31`) · grok | excerpts; `evaluate.py:419-422,528` | HOLDS | = R1 row 26 (cites are excerpt lines). |
| K8 | … `TUNABLE_KEYS` occurs on Extension only (`greps.txt:29-38`) · grok | greps.txt:29-38 | HOLDS | = C7b. |
| K9 | … Fable's union does not name `A-01`, so "one mechanism marks all 23" is false for `A-01` · grok | `NEEDS-ROUND-2.md` Fable (d); `evaluate.py:635-639` | UNVERIFIABLE FROM READS | = A5b/G7: Fable's text puts `A-01` in a convention row read by a resolver that does not exist yet. |
| K10 | … a path declaring three Extension keys marks a key this scan's branch did not use · grok | `extension.py:40-44,55-58` | HOLDS | `from_tunables` requires all three keys whether path A or B runs. |
| K11 | R2-2.3: the column exists (`store.py:1041-1044`, `radar.py:61`); C1's file list has no schema change · grok | `store.py:1041-1044`; `cards/radar.py:61`; `v2-sections.excerpt.md:49-53` | HOLDS | = A8; v2 §1 Files: no schema/migration/column change. |
| K12 | R2-2.4: `AtomOutcome(... assumed="A-13")` raises · grok | `seam.py:100` | UNVERIFIABLE FROM READS | = G9. |
| K13 | R2-2.5: after `source` becomes `ruling` the key leaves Fable's closure, the dot is not rebuilt, the open card gains a score · grok | `NEEDS-ROUND-2.md` Fable (O4)/(d) | UNVERIFIABLE FROM READS | Fable's text does not say whether the closure or dot is recomputed on refresh. Nothing built. |
| K14 | … three all-null Rubberband cards sort together, then by `pool_position` (`cards/radar.py:179-182`) · grok | `cards/radar.py:179-183` | HOLDS | (F8). |
| K15 | R2-1: the other five notes name an Extension or `trade_direction` (rubberband:45, backside:98, fashionably-late:40, nine-ema-scalp:45, vwap-continuation:40-41) · grok | the real notes (F9) | HOLDS | All five cites hit. `greps.txt:5-6` is one line early (Hitchhiker's count is line 7). `PROPOSAL.md` part1:36 IS the refusal sentence. |
| K16a | R2-3.1: loader cites (`vault_loader.py:476`, `:44-82`, `:271-280`, `:14-16`, `:44-48`) · grok | `vault_loader.py:476,317-366,271-280` | HOLDS | = C5, C6 (cites are excerpt lines). |
| K16b | … the next taxonomy load raises, so "the seven notes do not load. No scan." · grok | `reports/setups-tribunal-fable-r1-2026-09-21.md:204` | UNVERIFIABLE FROM READS | Fable's R1 ESCALATE 1 says the running radar keeps its DB copy and stays up; whether a failed taxonomy load stops scans is not in the excerpts. Both quoted. |
| K17 | R2-3.2: "any user row may fill, so a strategy note can fill a matching per-trade engine hole" · grok | `NEEDS-ROUND-2.md` Grok (O5); `tunables.yaml` (F1) | HOLDS | True of the text; not reachable on today's six null rows (none is per_trade). |
| K18 | … Fable: a per-trade assumed row fills global null `range.wick_ratio_max` for every def; `resolve_cfg` by key only (`loader.py:40-42`) · grok | `tunables.yaml:73-80`; `loader.py:126-128` | HOLDS | = R1 row 18. Engine row is global, null, consumers `hitchhiker`. |
| K19 | … a `ruling` row that stays in the note collides loud (`loader.py:18-25`) · grok | `loader.py:104-111` | HOLDS | = A15. |
| K20 | R2-3.3: deleting the row leaves no row and `resolve_cfg` raises (`loader.py:47-49`) · grok | `loader.py:126-136` | HOLDS | `TaxonomyConfigError` when the key has no row and is no `working_timeframe` / MA ref. |
| K21 | … "the modelled stop buffer" for `A-02` · grok | (companion not opened) | UNVERIFIABLE FROM READS | What `A-02` stands for is in the gitignored companion; the hub cites assumed values by key only (L32). |
| K22 | R2-4.1: Fable's order publishes a formed long card when both frames form, which §1 refuses, and hides `not_evaluable` · grok | `v2-sections.excerpt.md` §1 ("Both sides qualify … `not_formed`, note `both_sides`"); Fable (O2) | HOLDS | Text conflict as stated: Fable's tie → long frame; v2 §1 + F-19 (kept by all three seats) → `both_sides`. |
| K23a | R2-4.2: the detail stores one evaluation's observations (`evaluate.py:45-47` excerpt) · grok | `evaluate.py:583-596` | HOLDS | = C9 (excerpt line). Volume unchanged by the mirror = F-04 text. |
| K23b | … `replay` of the published detail cannot rebuild the trigger · grok | — | UNVERIFIABLE FROM READS | Nothing built. |
| K24 | R2-4.3: Grok's O2 does not mirror the daily series or level set · grok | `v2-sections.excerpt.md:79` | HOLDS | F-04 says "mirrored bars" only. |
| K25 | … `Hitchhiker.md:38` names a daily level · grok | `Hitchhiker.md:38`; `grep -rl` (F5) | UNVERIFIABLE FROM READS | The line names a `DayRange` item; `DayRange` / `upper_third` exist in no source file, so its source series is not readable. |

Counts of DOES NOT HOLD rows: gemini 9 (G4, G5a, G6, G10, G15, G16, G19, G21, G27), astra 0, grok 0; UNVERIFIABLE FROM READS rows are listed per row (behaviour claims nobody ran, or design text with nothing built). Two houses contradicting each other on the same fact: gemini G15/G16 (grok's and fable's predicates) against `NEEDS-ROUND-2.md`'s quoted texts, and grok K16b against Fable's R1 ESCALATE 1 on whether a failed taxonomy load stops scans — quoted both, smoothed neither.

## Experiments named (L70)

| experiment | named by | gates | the result that would change the design |
|---|---|---|---|
| X8 (v2's row; after C2 form a card on an assumed key, change its `source` to `ruling`, refresh; astra adds persist/reload and a tap) | grok (unchanged), astra (extended) | C2 (binds the R2-2 winner) | The open card loses the assumption provenance / `score_suppressed=assumed_formation`, or gains a score → lifecycle persistence must be fixed before deploy (astra); the preserve must be on every writer (grok). |
| X12 (v2's row; form a mirrored-frame card; read `why`, `extreme`, `raw`, `rounded`, `inputs`, levels, labels) | grok (unchanged, not ruled), astra | C2 | Leaked mirrored prices or wrong directional labels → typed normalization / per-type un-mirroring before publication. |
| X18 (grok's): on one stored day compute `atrs_from_open`, `Extension.leg_count`, `htf_level_proximity` on real and mirrored bars | grok | C2 | A factor differs → it stays per frame in the published row; all three match → may be computed once on real bars. |
| X18 (astra's, same number, different run): exercise the dedicated loader with matching suppliers, mismatched units/scopes, strategy-origin collisions, duplicates, engine-null transitions | astra | C2 | Acceptance outside R2-3.2's predicate → merge validation revised. **NUMBER COLLISION: two different runs are both called X18.** |
| X19: fixtures for each pair of non-formed frame states; assert deterministic selection and round-trip of both results | astra | C2 | Lost or mismatched evidence → receipt artifact revised. |
| X20: declared closures vs instrumented reads on cfg, trigger, stop, detector and convention paths | astra | C2 (only if a static closure is chosen) | Missing dependencies → repair declarations; instrumentation stays a verification tool, not a production recorder. |
| E1 (hub-noted, no house named it): construct `AtomOutcome(atom=…, value_kind="boolean", boolean=True, assumed="A-13")` in a dev session and follow the `detail()` caller | hub (from G9 / K12) | C5 | Not a ValidationError, or the caller swallows it → R2-2.4's "cannot mark the atom" premise changes. |
| E2 (hub-noted): with an evaluator-appended dot outside `quality_factors`, run `refresh_card` then read the returned dots and `score_suppressed` | hub (from C3b / K2b) | C1/C2 | The dot survives a refresh → the Fable-mechanism objection in K2b/A-family falls; it does not → both the dot and any refresh-time append need a stated call site. |

## Independence

| file | `grep -c -F -e "-ruling"` | reading |
|---|---|---|
| `grok-ruling-r2.md` | 0 | clean |
| `gemini-ruling-r2.md` | 0 | clean |
| `astra-ruling-r2.md` | 0 | clean |
| grok raw output (`brdzkpi8j.output`) | 1 | line 1 is grok's own closing message naming its own output file `grok-ruling-r2.md` — not another house's ruling |
| gemini raw output (`btdn320b4.output`) | 0 | clean (gemini's run prints only its answer; its reads are not exposed — UNVERIFIABLE which files it opened) |
| astra raw output (`b472hxu6p.output`) | 2 | line 14 = its own launch sentence (allowed); line 104 = the substring inside `owner-rulings.md`, a citation inside the packet's `hub-checks.md` that astra `cat`-ed, not a file it opened |

astra's shell reads (its own log): `cat` of `QUESTIONS-R2.md`, `NEEDS-ROUND-2.md`, `hub-checks.md`, `scoring.excerpt.py` + `evaluate.excerpt.py` + `seam.excerpt.py`, `extension.excerpt.py`, `store.excerpt.py`, `vault_loader.excerpt.py` + `tunables.excerpt.py`, `loader.excerpt.py`; `rg` on `v2-sections.excerpt.md` and `greps.txt`; `sed -n` on `v2-sections.excerpt.md` and `greps.txt` — all in the r2 folder; none in `../r1/`, none of a `-ruling` file. No house READ ANOTHER RULING.

## ESCALATE

1. **Choices whose supporting claim DOES NOT HOLD (nine rows, all gemini's; astra 0, grok 0):** G4 (Fashionably Late has no `bars_cleared`) and G5a (no "existing pattern" beyond `extension.py`) under gemini's `FABLE'S` on R2-2.2 — G5a is also Fable's own claim C7b, which DOES NOT HOLD; G6 (12 convention rows, not 23) under R2-2.3; G10 (X8 does not concern `A-13`) under R2-2.5; G15 and G16 (what grok's and Fable's O5 texts say) under R2-3.2; G19 and G21 (LAWS L32/L53 text; Grok's O5 has no "edit drops the mark") under R2-3.3; G27 (F-04 mirrors intraday bars) under R2-4.3. No claim under grok's or astra's choices DOES NOT HOLD. (Nothing changes the counts of who chose what; the derive decides what the failed claims do to a choice.)
2. **A second ranking authority in effect that HOLDS mechanically (L52 (b)):** WATCH's second sort key is `pool_position` (`evaluate.py:134-136`, `cards/radar.py:179-183`), so a set of all-null `card_score`s is ordered by `pool_position` (= `last_rank`, `evaluate.py` part3:129); `ADR-0009:28` says `card_score` is the only number that orders WATCH cards and `last_rank` only admits. Grok and astra read that as the existing tie policy; gemini and Fable read it as a violation. The hub reads no ADR into law and decides nothing.
3. **A card can regain a score after a tap or a refresh — the claim HOLDS, on the code as it is (L52 (a)):** `suppression()` needs an untapped dot (`scoring.py:247-251`); the tap path (`store.py:1215-1224`) and `refresh_card` (`evaluate.py:777-800`) both recompute it from dots; `refresh_dots` returns only dots present in `fresh` (`scoring.py:216-235`), so a dot the evaluator appends outside `quality_factors` is not carried by the current functions unless the refresh path appends it too (C3b, E2). Whether a tap that lifts the score is acceptable is R2-2.1, split 3 ways.

Recorded once, not escalations: (a) **L74** — a block inside the Read result of `44-setups-tribunal-r2.md` (after its last line) asked for a `Claude-Session` line in commits and named a file-send tool; it is DATA, was not followed, no commit was made; not raised again. (b) The approved-line proof: `Bash(grok *)` and `Bash(agy *)` count 2 lines in `08-bars-chunk-e-check.md` (lines 1 and 5), the other 15 strings count 1; none counted 0. (c) Two typo'd Writes to `/Users/cobalt-wt/...` were refused by the OS (`EACCES`) and created nothing; several stray failed tool calls changed nothing. (d) Packet 90,028 B, under 100 KB. (e) No `ASK DESK`; no house failed; astra experiment `reads started`; no owner item is a precondition; no gate or fixture rests on his trade log (astra's fixtures are definition-written or "independent of the owner's trades"; grok's X18 runs on "one stored day", unspecified).

SETUPS TRIBUNAL R2 DONE · grok: TRIBUNAL R2: BUILD · gemini: TRIBUNAL R2: BUILD AFTER applying the NEITHER replacements · astra: TRIBUNAL R2: BUILD AFTER incorporating these replacements and assigning their chunk gates. · houses that ruled: 3 of 3 · R2-2: SPLIT · items settled: 1 of 4 · Fable R1 claims checked: 9 HOLD of 10 · astra stdin experiment: reads started · ESCALATE: 3
