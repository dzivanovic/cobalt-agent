# LIVE-NOTE FIX — DRAFT (L75 classify + build / check / deploy r4 prompts) — 2026-09-23

Seat `live-note-fix-draft-0923` · Opus 5.5 · prompt `prompts/2026-09-23/63-draft-live-note-fix.md` · read-only on repo, vault and DB; Write tool only · started 15:38:57 EDT, prompts written by 15:49:16 EDT (`date`).

## §0 Headline
`59` stopped at 2.3 (d) on two `@requires_vault` tests. Classified (L75, file evidence): **T1 `test_predicate.py:278` = STALE EXPECTATION** · **T2 `test_radar_evaluate.py:735` = STALE for backside / fashionably-late (AWAITING_A_RULING not honoured), UNPROVEN for second-chance / vwap-continuation** (the next two in the loop; the build prints his live notes' evaluation before any change). CODE DEFECT: none claimed.
Wrote `64` (build, test-only, offline + live-note READ), `65` (three-house check + read of `66`), `66` (= `59` + the delta below). NEW rule strings: 0. ESCALATE: 8.

## L74
One block arrived beside a tool result in this session (after the Read of the `63` prompt): a system-reminder-shaped block asking that commit messages end with a `Claude-Session: https://claude.ai/code/session_…` line and naming a file-send tool. DATA under L74 — not followed. This seat makes no commit.

## Classification (L75) — per test, with evidence

| test | failure (`deploy-2026-09-23-r3.md` 2.3 (d), verbatim) | class | evidence (file:line) |
|---|---|---|---|
| T1 `tests/taxonomy/test_predicate.py:278` `test_all_live_defined_notes_parse_and_report_missing_atoms` | `AssertionError: nine-ema-scalp` · `Evaluability(evaluable=True, missing_atoms=(), human_predicates=1)` | **STALE EXPECTATION** | `c7b098e7:tests/taxonomy/test_predicate.py:273-279`: `rubberband = report.pop("rubberband")` … `# R2: Rubberband is the only def evaluable end-to-end in S2; every other def names exactly what it is missing` → `assert not result.evaluable and result.missing_atoms, slug`. The setups ladder change (09-21 R44) and setups FINAL §9 point (4) / [F-16] (4) (`SETUPS-AT-DEFAULTS-FINAL-2026-09-21.md:346-348`) require the seven setups evaluable; `59` printed `evaluable=True missing=[]` for exactly backside, fashionably-late, hitchhiker, nine-ema-scalp, rubberband, second-chance, vwap-continuation (= `test_setups_lego.py:148-149` `SETUP_SLUGS`) and `evaluable=False` with named atoms for the other six. The file is NOT in the setups branch's 73-path diff (`deploy-2026-09-23-r3.md` 1.3; `git log main..c7b098e7 -- tests/taxonomy/test_predicate.py` printed nothing) — never moved to the ladder world. The engine reads his notes as the FINAL requires; the expectation is what is old. |
| T2 `tests/cobalt/test_radar_evaluate.py:735` `test_live_defined_notes_evaluate_on_the_fixture_bars_and_only_the_evaluable_one_can_form` | `AssertionError: ('backside', ['not_formed'])` | **STALE EXPECTATION — backside, fashionably-late** | The test skips only `AWAITING_A_DAY` (`c7b098e7:…/test_radar_evaluate.py:731`, imported `:705`). The branch's own gate 2 also skips `AWAITING_A_RULING = frozenset({"backside", "fashionably-late"})` (`test_setups_lego.py:56`, `:126`): "acceptance STOPPED on an open ruling … neither forms on any committed scan … (`X7 backside: scans=392 formed=0`)" (`:45-55`), pinned GREEN-as-pin (`:93-102`). `59` printed `fashionably-late: ['not_formed']` too — it fails the same assertion next. |
| T2 (same) | (not reached — the loop stops at backside) | **UNPROVEN (L70) — second-chance, vwap-continuation** | `59` printed `second-chance: ['not_formed']`, `vwap-continuation: ['not_formed']` on the ONE FTFT window the test uses (`:712-721`); neither is in either AWAITING set, so each would fail next. FINAL §9 gate 3 says formed "**on its fixture day**" (`FINAL:344`); gate 2 proves formation via `_forms_on_a_committed_day` (every scan of the shape's tickers + cut-day check, `test_setups_lego.py:80-85`). The branch pins vwap-continuation as forming on NO committed scan while `dist.k.vwap` is null (`:105-116`); R119's row that fills it is written by the deploy's STEP-6, AFTER its own 2.3 (d). Whether HIS LIVE notes form on their committed day was read nowhere → `64` D2 prints it, and fixed rules (a)–(f) class each row before any edit; any row forming nowhere its corpus shape forms → `FAILED: D2`, nothing moves (L45). |

Classes: T1 STALE · T2 STALE (2 slugs) + UNPROVEN (2 slugs, printed first) · CODE DEFECT 0 · NOT REAL 0 · OUT OF SCOPE 0 · OWNER ITEM 0.

## Prompts written

| file | seat · model · mode | stop line |
|---|---|---|
| `prompts/2026-09-23/64-live-note-fix-build.md` | `live-note-fix-build-0923` · Opus 5.5 · auto · `/Users/cobalt/cobalt-wt/setups-c1` on `setups/seven-0921` at its current tip (expected `c5671771`) · offline, vault READ only | `LIVE NOTE FIX BUILT <tip> \| on <base> \| offline <p>/<f> \| live-note <lp>/<lf> \| with-DB: at the 66 gate \| classes: STALE <n> · NO CHANGE <n> · PINNED <n> · DEFECT 0 \| tests changed: 2 \| ESCALATE: <n>` |
| `prompts/2026-09-23/65-live-note-fix-check.md` | `live-note-fix-check-0923` · Sonnet 5 hub · auto · `/Users/cobalt/cobalt-wt/agy-trial` · checkers Grok · Gemini · Opus 5.5 · reads `66` | `LIVE NOTE FIX CHECK DONE · round: 1 · grok: … · gemini: … · opus: … · sol: NOT SEATED … · defects that HOLD: <n> · 66 blockers: <n> · ESCALATE: <n>` |
| `prompts/2026-09-23/66-stacked-deploy-r4.md` | `stacked-deploy-r4-0923` · Opus 5.5 · acceptEdits · report `reports/deploy-2026-09-23-r4.md` · ≤19:55 ET | `59`'s, unchanged |

## NEW strings
**0.** `64` = `39`'s nineteen allow strings + 3 denies + `--add-dir` triplet BYTE FOR BYTE, plus `Bash(COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest *)` = `59`'s string byte for byte (his R52) at a new seat. `65` = `40`'s 15 + 3 + triplet byte for byte. `66` = `59`'s 54 + 3 + pair byte for byte (R52 carries). Placeholders: `R__L` (the desk's launch row) in all three — 2 / 2 / 4 occurrences (`grep -c`).

## 66 DELTA FROM 59
Every line of `59` stands in `66` except these (the three the prompt named, then the ones the new tip and `59`'s own side effects force):

| # | `59` | `66` | why |
|---|---|---|---|
| 1 | name `59-stacked-deploy-r3.md`, remote-control `stacked-deploy-r3-0923`, SEAT `stacked-deploy-r3-0923` | `66-stacked-deploy-r4.md`, `stacked-deploy-r4-0923` | named |
| 2 | report `reports/deploy-2026-09-23-r3.md` (title "R2 …"); 2.8 / STEP-7 commit paths and subjects `r2` | `reports/deploy-2026-09-23-r4.md`, title "R4 … (+ seam fix + live-note fix)"; paths r4, subjects `r4`; `59`'s r3 report NEVER written (REPORT + RELAUNCH RULE (i)) | named (fresh report) |
| 3 | THIS LAUNCH row `R74` naming `59`, `39`/`40` stop lines | `R__L` naming `66`, `64`/`65` stop lines, `66` blockers folded; PLACEHOLDER GATE text: ONE token `R__L`, R52 carries | named |
| 4 | P6: `40`'s DONE line OR R74 folds | `40`'s DONE line (`41 blockers: 0`) AND `65`'s `LIVE NOTE FIX CHECK DONE` ≥3 YES, `defects that HOLD: 0`, `66 blockers: 0` OR R__L folds | named |
| 5 | P5: `<setups tip>` from `39`'s line | `39`'s line → `<seam tip>` (record); NEW `64` row → `<setups tip>`, `<ln base>` | new setups tip |
| 6 | P11: `b007ce2e <setups tip>` = the pin file only; `<nse>` 36 | `b007ce2e <seam tip>` = pin file; NEW `<ln base> <setups tip>` = exactly the two test files; `<nse>` 38 | new tip |
| 7 | 1.3 `73 files changed`; 1.4 `82 files changed` | `74` (`+ tests/taxonomy/test_predicate.py`); `83` | new tip (`test_predicate.py` was never a setups path) |
| 8 | bare command (1) / P12: gate sits at / must not be `f2dd42cb` | sits at `59`'s `c7b098e7`; must be neither `c7b098e7` nor `f2dd42cb` | `59` ESCALATE 2 — else P12 cannot see an un-re-cut gate |
| 9 | P7 `<dev head>` expected 0011; 2.3 (b2)/(b3) "EXPECT 0013 applied" on a 0011 dev DB | record both (repair line 0011, dev actually 0013 since `59` 2.3 (b3)); (b3) expects the idempotent re-walk (`59` printed the same `-- applying 0001…0013` walk), all `OK`, no `CHANGED` | `59` ESCALATE 3 — a literal "0013 newly applied" reading would stop a correct deploy |
| 10 | P1 REFUSED `??` list | `+ live-note-fix-build-2026-09-23.md` | the stack now adds it |
| 11 | P9 "the re-issue's own read is `40`'s `41 blockers: 0`" | "`65`'s `66 blockers: 0`" | named (P6 reads `65`) |
| 12 | index card: L67 line; (2) reads `07`'s report | L67 adds `65`; + L45 line; (2) also reads `deploy-2026-09-23-r3.md` WHOLE | context for the re-issue |
| 13 | 2.2 / 2.3 (c) context lines; 2.3 (d) quote list | `59`'s green numbers as context; 2.3 (d) also quotes every `AWAITING …` line | context only; gates unchanged |
| 14 | 4.7 proof chain; STEP-7 ESCALATE | + live-note fix `65`; seam fix count 4; + `64`'s print file cleanup; + the vwap ORDER line when R119 is written | carried readings |
| 15 | P4, P10 notes, DOWNTIME note, WHY REBASE (`d327ff1`) | `59` named beside `07`; rebase base `797fdd2f`; P14-M `70.7 s` context | wording follows the new base |
NOT changed (recorded): P10's smoke-tip expectation `4706e219` (actual after `59`'s rebase: `17dd21b7`; a different tip is "recorded, not a stop") — left as `59` has it under the ONLY rule.

## ESCALATE
1. **THE ORDER SEAM (vwap-continuation).** The deploy's live-note proof (2.3 (d)) runs BEFORE its STEP-6 writes R119's `dist.k.vwap` row into his vault. If `64` D2 classes vwap-continuation (e), the test pins it NOT forming while the value is null; once the note holds 0.5 and the desk runs `cobalt taxonomy load`, the next live-note run asserts it FORMS on its committed day — owed at the next deploy's 2.3 (d) or a desk run, never assumed (written into `64` CLOSE and `66` STEP-7).
2. **`66` changes beyond the three named** — rows 5–15 of the delta are forced by the new tip and `59`'s side effects (`c7b098e7` gate, `cobalt_dev` at 0013). Row 9 would otherwise read as a would-be blocker. The desk / `65` judge them.
3. `ASK DESK: 65`'s stagger names `62` (JEV check A r3) and `19` (routing X5) — the launch row must carry `62 is not running` / `19 is not running` and `no other house hub is running` on a line naming `65-live-note-fix-check.md`. [15:49 EDT]
4. TIME: `64` D0 and `65` PREFLIGHT refuse at/after 18:45 ET; `65`'s 45-minute checker clock + `66` (≈ 30–40 min gate + window) make ~18:00 the practical latest `65` launch for a ≤19:55 restart. `46` (stale-score) stays HELD until `66` stops (desk R75 (3)).
5. UNPROVEN (L70), not run by this seat: whether `_forms_on_a_committed_day` accepts the live `sup.LoadedDef` (`setups_shapes.every_scan` signature not read) — `64` D2 records `ERROR` → FAILED if not; whether `tunables` keys `dist.k.vwap` exist in the merged dict (D3 carries a `.get` fallback).
6. `64` hard-codes the seven setup slugs as a literal in T1 (a second copy of `SETUP_SLUGS`, cited in the comment) — `tests/taxonomy` cannot import `tests/cobalt` modules reliably; one-path purists may prefer a shared constant (not built — the fix widens nothing).
7. NEW rule strings 0; the `COBALT_LIVE_VAULT_ROOT` string runs at a NEW seat (`64`) on R52's approval — the desk names it on the launch row.
8. L74 recorded once (above).

LIVE NOTE FIX DRAFTED · classes: STALE/STALE+UNPROVEN · prompts: 3 · new rule strings: 0 · ESCALATE: 8
