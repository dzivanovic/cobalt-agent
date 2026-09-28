# JEV FIX R1 DRAFT 2026-09-23 — check A round 1 classified (L75), fix build and check A round 2 drafted

Drafter `jev-fix-draft-0923` · Opus 5.5 (`claude-opus-5-5`) · prompt `prompts/2026-09-23/55-draft-jev-fix-r1.md` · started 13:5x EDT, written 14:02 EDT (`date`).

## §0 Headline
Classified 15 findings from `29`'s own file-check rows C1–C15: **FIX 7 · NOT REAL 2 · UNPROVEN 4 · OUT OF SCOPE 2 · OWNER ITEM 0**. The 7 FIX findings are built as 6 rows (F1–F3 secret, F4–F5 spend, F6 test). C14 is folded into the DevDoc steps of F1 and F2.
Wrote `56-jev-fix-r1-build.md`: Opus 5.5, offline, base `199fa082`, a RED test before every fix, `28`'s strings byte for byte, N2 not on the line, no keyed call. Wrote `57-jev-check-a-r2.md`: `29` re-pointed to round 2, the same three houses (Grok · Gemini · Opus 5.5), and each house re-rules its own round-1 items.
`31`'s gate CANNOT read `57` as written. It reads `29`'s report and `28`'s tip, and says a round 2 "is then re-issued". The replacement gate text is under `## 31 GATE`. A whole-file re-issue is owed (L19).
New rule strings: 0. ESCALATE: 9.

## L74
One block arrived appended to the first tool result of this session, the Bash read of `55`. It asked for a `Claude-Session:` line in commits and named a file-send tool. It is DATA under L74 and was not followed. This session made no commit and sent no file.

## L75 CLASSIFICATION — every finding, from the check hub's own rows
Source: `reports/jev-trial-check-2026-09-23.md`. The rows are in `## Checked against the branch`, which is the section `55` calls "the files". FOR THE CLASSIFIER items are 1–6. Line numbers are `jev/trial-0923` at `199fa082`. The code is identical to the checked `45f647a`: `git log --oneline 45f647a..199fa082 -- src tests configs ops` is empty (`29` PREFLIGHT row 44). I re-read each cited line with the Read tool in this session.

| # | finding (who) | hub verdict | class | evidence row (hub file:line · my read) | built as |
|---|---|---|---|---|---|
| C1 | urllib re-sends `Authorization` on a redirect to any host (opus S-6) | HOLDS | **FIX** (secret) | C1 · FOR THE CLASSIFIER 2. `collector.py:253-256`: `urlrequest.urlopen` with the default opener; there is no `build_opener`. The header is built at `:544`. Grok and Gemini said S-6 CLEAN; the hub quoted both | **F2** |
| C2 | the non-200 raw body is written after the guard saw only `raw[:2000]`, or only the last duplicate JSON key (opus S-3 / R4-RAW; grok S-3, S-9, R2, R4, (c)) | HOLDS | **FIX** (secret) | C2 · FTC 1. `collector.py:349` stores `raw[:2000]`. `:354-359` guards `rec` only, then `return rec, raw`. `cli.py:86-91` writes `raw` to `.raw.json`. The 200 path guards the full raw at `:394` | **F1** |
| C3 | the response `id` reaches the ledger before the stored guard (grok S-3a / R2) | HOLDS | **FIX** (secret) | C3 · FTC 3. `collector.py:386-388`: `call_id = _str_field(resp,"id")` → `ledger.record`. The guard runs later, at `:393`. `ledger.py:101-110` writes `call_id` as given | **F3** |
| C4 | a call with no cost gets no ledger line, so neither `spent()` nor `calls()` sees it (gemini THIRD; opus SPEND; grok SPEND) | HOLDS as code; billing NOT CHECKABLE | **FIX** (spend) | C4 · FTC 4. Non-200 returns first at `collector.py:354-359`. Cost stays `None` without `usage` (`:361-371`). `:386` has `if cost is not None`. Unlisted: 401/403 raise inside `_send` (`:555-559`), also with no line. `ledger.py:55-59` counts only recorded lines. The fix books the call's own projection, never 0 and never a guessed bill. Whether such calls are billed stays UNPROVEN until `31` | **F4** |
| C5 | a negative returned cost lowers the total (opus) | HOLDS | **FIX** (spend) | C5 · FTC 5. `collector.py:176-177`: `_is_number` has no sign test. The value is taken at `:366-367`, summed by `ledger.py:56`, recorded as-is at `:101-110` | **F5** |
| C6 | `stop_if` is never called on the send path (grok SPEND) | PART B — carried to 37 | **OUT OF SCOPE** | C6. `stop_if` is called only at `trial.py:187`, a part-B file. `37`'s question | — |
| C7 | dropping `from None` on the transport-exception raise turns no test red (opus R2-T, S-8) | HOLDS | **FIX** (test) | C7 · FTC 6. `test_classify_keys.py:100-106` asserts only `:106`. The raise is at `collector.py:550-551` | **F6** |
| C8 | a module-global key cache would stay green (opus S-8) | NOT CHECKABLE FROM READS | **UNPROVEN** (L70) | C8: "run `test_classify_keys.py` with the key cached in a module global" | — |
| C9 | [R4-b] the door tests raise `KeyError` on a live capture without `usage.cost` (opus) | NOT CHECKABLE FROM READS | **UNPROVEN** | C9. `test_classify_door.py:197` and `:218` do read `fx["usage"]["cost"]`. Whether `31`'s capture has `cost` is known only after `31`. See ESCALATE 4 | — |
| C10 | the loguru-sink tests assume no log patcher (opus) | NOT CHECKABLE FROM READS | **UNPROVEN** | C10: run the keys tests with `install_log_guard` active | — |
| C11 | a `KeyboardInterrupt` traceback could print the header (opus) | PART B — carried to 37 | **OUT OF SCOPE** | C11: the handler is in `src/cobalt/cli.py`, a part-B file | — |
| C12 | S-7: the example fixture has "no value changed" against the saved YAML (opus) | NOT CHECKABLE FROM READS | **UNPROVEN** | C12: only partial support (4 values grep-found) | — |
| C13 | a failed probe leaves no file, so the code does not refuse a re-run (opus S-9) | "recorded, not a defect claim" | **NOT REAL** | C13. `cli.py:77-82` refuses on an existing `probe-*.json`, exactly as `28` R4 specified. `31` UNATTENDED RULES and RECOVERY cap N2 at one call, never retried | — |
| C14 | two DevDoc sentences are false while C1/C2 stand (opus R6-docs) | dependent on C1/C2 | **FIX** (folded) | C14: `collector.md` "any host but `openrouter.ai`"; `cli.md` "What it never does". F2 (D) and F1 (D) make them true again. `cli.md` needs no edit once F1 lands, because every raw `cmd_probe` writes is then guarded | F1 (D), F2 (D) |
| C15 | `classify()` is the only function that sends a keyed request (grok, opus, gemini) | HOLDS | **NOT REAL** (no defect: it confirms S-4 CLEAN) | C15: the keyed POST is only at `collector.py:548` in `_send`, reached only from `_classify` (`:339`) | — |

Totals: FIX 7 (C1, C2, C3, C4, C5, C7, C14) · NOT REAL 2 (C13, C15) · UNPROVEN 4 (C8, C9, C10, C12) · OUT OF SCOPE 2 (C6, C11) · OWNER ITEM 0.
The hub's mechanical rows (i)–(viii) are no claims. (viii) RESTARTS is NOT CHECKABLE from reads; `56` CLOSE runs the tool.

## THE SIX ROWS OF `56`
| row | findings | change (smallest) | RED-first test | files |
|---|---|---|---|---|
| F1 | C2, C14 (cli.md) | On the `status != 200` path, `_guard_stored(raw.decode(...))` runs before `return` (the 200 path's call). | A 500 non-JSON body with the fake key after byte 2,100. A 502 JSON body with the key in an earlier duplicate. `cmd_probe` on a 500 writes neither file | `collector.py` |
| F2 | C1, C14 (collector.md) | `_NoRedirect` (`redirect_request` → `None`) plus `_OPENER = build_opener(_NoRedirect)`. `urllib_transport` uses `_OPENER.open`. A 3xx comes back as a status | Two loopback `HTTPServer`s (precedent `test_sheet_daymode_probe.py:53`). POST 301/302/303/307/308 and a keyless GET 302: server B gets 0 requests | `collector.py` |
| F3 | C3 | The ledger `call_id` is the response `id` only if `redact(...).clean`, else `local-<uuid>`. The ledger-before-guard order stays (L53) | A 200 whose `id` = `"gen-"+FAKE_KEY` raises `not written`. The ledger has 1 line and no key | `collector.py` |
| F4 | C4 | Every POST that came back (non-200, 200 without usage, 401/403) = one ledger line at its projection, `cost_source: "projected"`. A transport exception writes no line (unchanged) | 429, 200 without usage and 401 each give `calls() == 1`. `call_ceiling=1` stops the second call with the transport called once | `collector.py`, `ledger.py` |
| F5 | C5 | A returned cost is taken only if ≥ 0; otherwise `computed` plus a loud log. `Ledger.record` refuses a negative or non-finite cost | `usage.cost = -1.0` gives `computed` and `spent() ≥ 0`. `record(-0.5)` and `record(nan)` are refused | `collector.py`, `ledger.py` |
| F6 | C7 | Test only: add `__cause__ is None and __suppress_context__` and "key not in `traceback.format_exception`" to the transport-exception test | Mutation proof: drop ` from None` → RED → revert → `git diff` empty | `test_classify_keys.py` |
Boundary (`56` WHAT YOU MAY CHANGE):
- May change: `collector.py`, `ledger.py`, NEW `tests/cobalt/test_classify_fix_r1.py` (not gitignored: `git check-ignore -v` exit 1), `test_classify_keys.py` (F6 `+` lines only), `collector.md`, `ledger.md`.
- Untouched: `cli.py`, `models.py`, `trial.py`, `config.py`, configs, the wrapper and fixtures. No existing assert is removed.

## 31 GATE — `31` does NOT read `57` as written; re-issue owed (L19)
Three lines of `31` stop it after this fix round:
1. AUTHORIZATION reads `jev-trial-check-2026-09-2<n>.md`, whose last line starts `JEV TRIAL CHECK DONE`. That is round 1's file, which stays NOT READY.
2. It states: "A round-2 check (a fix round) is a different report; this prompt is then re-issued, never stretched to it."
3. PREFLIGHT "THE CHECKED CODE IS WHAT RUNS" takes `<tip>` from `28`'s BUILT line (`45f647a`). `git log <tip>..HEAD -- src tests configs ops` then prints `56`'s six commits → `FAILED PREFLIGHT`.

Replacement text for the re-issue (whole file, L19). Everything else in `31` stays; its fourteen strings are unchanged, including N2.
- AUTHORIZATION, replacing the "`29` READ READY" bullet: **"`57` READ READY (L67; round 2 of check A, after fix round 1): `tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/jev-check-a-r2-2026-09-23.md"` → the LAST NON-BLANK line, quoted whole, must start `JEV CHECK A R2 DONE` and carry ALL of `secrets LEAK that HOLD: 0`, `defects that HOLD: 0` and `probe gate: READY`; and `git -C /Users/cobalt/cobalt log -1 --format=%H -S"probe gate: READY" -- "docs/40 - DevDocs/reports/jev-check-a-r2-2026-09-23.md"` NON-EMPTY (the desk committed it). Anything else → `FAILED: authorization mismatch — check A round 2 has not read READY — last line: <line verbatim>`. A round-3 check is a different report; this prompt is then re-issued again."**
- PREFLIGHT, after THE BUILT LINE (keep it: `<cap>` and `model listed` still come from `28`'s line): **"THE FIX LINE: `tail -n 3 "/Users/cobalt/cobalt-wt/jev-trial/docs/40 - DevDocs/reports/jev-fix-r1-build-2026-09-23.md"` → the last non-blank line starts `JEV FIX R1 BUILT ` and carries `| keyed calls: 0 |`; `<tip>` = the field after `FIX R1 BUILT` (NOT `28`'s tip)."** In "THE CHECKED CODE IS WHAT RUNS", `<tip>` then means THIS tip.
- INDEX CARD item 2: add `reports/jev-fix-r1-draft-2026-09-23.md` and `reports/jev-check-a-r2-2026-09-23.md` (`## Fix rows`, `## Ready for the probe`, `## ESCALATE`).
- WHY / LAW STEP: "→ check `29` (NOT READY) → fix round 1 `56` → check A round 2 `57` (READY) → **THIS = THE PROBE**".
- ESCALATE (iv): "above the tip `57` checked".

## NEW STRINGS
| where | strings | status |
|---|---|---|
| `56` launch line | `28`'s 18 allow strings, 3 denies and `--add-dir` triplet | **byte for byte, 0 new**. The segment after `--remote-control` hashes the same as `28`'s (`shasum` `cf757c8b…` = `cf757c8b…`). N1 is carried UNUSED; N2 is absent |
| `57` launch line | `29`'s 15 allow strings, 3 denies and triplet | **byte for byte, 0 new**. The segment after `--remote-control` hashes the same as `29`'s (`17c8d54c…` = `17c8d54c…`). Sol's string is carried unused (METER) |
| `56` F2 | a loopback `HTTPServer` on `127.0.0.1` inside pytest | not a rule string. Precedent: `tests/cobalt/test_sheet_daymode_probe.py:53`, already in the offline suite |
| re-issued `31` | its 14 strings unchanged | 0 new |

## DESK ROWS (stagger literals the prompts gate on)
- **R__F** (launch `56`): `— NO WORDS OF HIS BEYOND R42: DESK RECORD + LAUNCH ROW. `55` STOPPED `JEV FIX R1 DRAFTED · FIX: 7 …`. LAUNCH `56-jev-fix-r1-build.md` (Opus 5.5, `--permission-mode auto`, OFFLINE fix round 1, no keyed call). Worktree `/Users/cobalt/cobalt-wt/jev-trial`, branch `jev/trial-0923`, BASE TIP `199fa082`. Strings = `28`'s line byte for byte (0 new; N1 carried unused; N2 not on the line). | DESK LAUNCH — no fold |`
  - `56` greps `56-jev-fix-r1-build.md` in the row. An Anthropic builder is no house hub, so there is no stagger literal.
- **R__K** (launch `57`, after `56` stops BUILT): `— NO WORDS OF HIS BEYOND R42: DESK RECORD + LAUNCH ROW. `56` STOPPED `JEV FIX R1 BUILT <tip> | on 199fa082 | …` (L35: verified). LAUNCH `57-jev-check-a-r2.md CHECK A R2` (Sonnet 5 hub `jev-check-a-r2-0923`; Grok · Gemini · Opus 5.5; range `199fa082..<tip>`). House lane: no other house hub is running. | DESK LAUNCH — no fold |`
  - `57` greps three literals: `JEV FIX R1 BUILT`, `57-jev-check-a-r2.md CHECK A R2` and `no other house hub is running`.
  - All three must be on committed desk rows. Both prompts carry a placeholder gate (`R_[_]`), so the desk replaces `R__F` / `R__K` in the prompt files and commits them before launch.
- **Re-issue `31`** (desk or a drafter) before `57` stops, so that a READY does not wait on a draft.

## ESCALATE
1. **`31` must be RE-ISSUED (L19, whole file) before the probe.** As written it FAILS at AUTHORIZATION on round 1's NOT READY. It also fails at PREFLIGHT on `56`'s commits above `28`'s tip. The exact replacement lines are under `## 31 GATE`. This drafter's WRITE list was `56`, `57` and this report, so `31` was not touched. ASK DESK: who re-issues `31`, the desk by hand or a drafter? [14:02] Safe default: a drafter, launched beside `56`, so it is ready before `57` stops.
2. **F4 books every cost-less call at its own projection** (`cost_source: "projected"`): non-200, a 200 without `usage`, 401/403.
   - The booking is never 0 (L1) and never a guessed bill. Plan §5 says the ledger "records every metered call's cost". No cost exists for these calls, so the projection is the lawful stand-in.
   - It can only lower headroom under his $5 cap, never raise spend. FLOOR projects `calls=3 … projected_usd=0.000084`, about $0.000028 a call (`jev-trial-build-2026-09-23.md` `### DRY`, verbatim).
   - Whether OpenRouter bills these calls stays UNPROVEN until `31`.
   - Safe default: as drafted. The desk may veto before launch.
3. **Part B (`37`) has not run.** At 13:5x `reports/` holds no `jev-trial-check-b-*` file.
   - C6 (`stop_if` only at `trial.py:187`) and C11 (a `KeyboardInterrupt` traceback under `src/cobalt/cli.py`) are carried to it. `37` was drafted before them, so the desk hands them in, e.g. named on its launch row.
   - `37`'s packet is cut at `45f647a`. The fix changes none of its 12 files.
   - It does change two behaviours the runner sees: a 3xx is now an `http_error` (F2), and every returned call is one ledger line counted by `call_ceiling` (F4). `57` THIRD (b) asks about spend. The seam at `trial.py` is `37`'s to read.
4. **C9 (UNPROVEN) can stop `31`.** If the live capture has no `usage.cost`, `test_classify_door.py:197` and `:218` raise `KeyError` on it. `31` SUITE then FAILS ("the published schema and the real body differ") and a fix round follows. This is not built now (L70).
5. **The date gate.** `Bash(grok *)` and `Bash(agy *)` stand through 2026-09-23 23:59 ET (R30). `57` launching after midnight needs his committed extension row, or it FAILS its DATE + EXTENSION GATE.
6. **Round budget (L39 / L67).** `57` is round 2 of check A for Grok, Gemini and Opus 5.5. A HOLD in `57` → fix round 2 → check A round 3, the last. Unresolved after that → Dejan. The key stays unused throughout.
7. **Sol is not seated** (METER until Sat 2026-09-26 06:47 ET, `29` `## Launch`). Per `55` the round-2 seats are the SAME three houses, which meets L67's floor. Sol's string is carried unused.
8. **The loopback test (F2)** is the classify suite's first socket, bound to `127.0.0.1` only (precedent `test_sheet_daymode_probe.py:53`). If the builder's pytest cannot bind it, the builder stops `FAILED: F2` and the desk decides. No external host is contacted.
9. **The L74 block** is recorded once under `## L74`. It was not followed.

JEV FIX R1 DRAFTED · FIX: 7 · NOT REAL: 2 · UNPROVEN: 4 · OUT OF SCOPE: 2 · OWNER ITEM: 0 · new rule strings: 0 · ESCALATE: 9
