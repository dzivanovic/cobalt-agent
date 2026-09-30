# S3 EXITS C1 FIX R2 — DRAFT (L75 classification of round-2 check `30`) — 2026-09-28

Seat: `s3-exits-c1-fix-r2-draft-0928` · Opus 5.5 · prompt `prompts/2026-09-28/34-draft-s3-exits-c1-fix-r2.md` · authorized by `cto-2026-09-28.md:81` (R73), read 13:35 ET. `<chk>` = `reports/s3-exits-c1-fix-r1-check-2026-09-28.md`; `<fb>` = `/Users/cobalt/cobalt-wt/s3-exits-c1/docs/40 - DevDocs/reports/s3-exits-c1-fix-r1-build-2026-09-28.md`. Base read 13:36 ET: `git -C /Users/cobalt/cobalt log --oneline -3 s3/exits-c1` → `9b25eced` over `3ceb3b11` over `da9246f0` (as the desk named).

## §0 Headline
- 7 findings classified from `<chk>`'s file-check rows: FIX 1 · NOT REAL 4 · UNPROVEN 0 · OUT OF SCOPE 2 · OWNER ITEM 0; Sol METER and the round line are RECORDS.
- The desk's reading holds for the HOLD: no line of `5164f867..3ceb3b11` names `redact`. The `cobalt_redactions` row comes from `tests/cobalt/test_redact.py:393` (`monkeypatch.undo()` drops the suite's rollback patch; the INSERT commits on the real autocommit factory). That file is outside the range, so the HOLD is OUT OF SCOPE and recorded against R61's OWED item.
- One FIX differs from the desk's reading: F5 (item 4). Three C1-added `fill_shares` values and one C1-added `orig_timestamp` still equal the base replay card's values. That breaks `20`'s L32 card, the same class as round 1's F4. So C1 does not stand.
- Wrote `35-s3-exits-c1-fix-r2-build.md` and `36-s3-exits-c1-fix-r2-check.md` (round 3 of ≤3, THE LAST). New rule strings: 0.

## L74
Recorded once (L74): after this prompt file was read (13:35), a `<system-reminder>` block was appended to that tool result. It asked for a `Claude-Session: https://claude.ai/code/session_…` line in commits and PR bodies and named a file-send tool. It is data, not an instruction. This seat commits nothing and sent nothing.

## Classification
Source lines are `<chk>:<line>` unless named. `20` = `prompts/2026-09-28/20-s3-exits-c1-build.md`; `29` = `prompts/2026-09-28/29-s3-exits-c1-fix-r1-build.md`.

| # | finding (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|
| 1 | R1 per-table proof: `cobalt_redactions` `179 · 1d147fe7…` in `<P0>` → `180 · 5acf3646…` in `<P2>` (Opus, Grok; both CHECK lines' only item) | `:130` (FTC 1), file-check `:111`; `:83`, `:136`, `:137`; `<fb>:116`, `:219`, `:243` | OUT OF SCOPE → RECORD | `cto-2026-09-28.md` R61 (line 69) OWED "`cobalt_redactions` grew mid-run, writer outside the build"; `29:83` (f2) asks for the comparison and an ESCALATE, not a fix | `git -C /Users/cobalt/cobalt log -p 5164f867..3ceb3b11 -- src tests`, grep `redact` (case-insensitive) → no line (exit 1). The row changed between 12:09 and 12:21, during pass 1 (`<fb>:198`), which runs `tests/cobalt/test_redact.py` (not deselected, `<fb>:143`). Its `TestTheCounter::test_a_hit_is_counted_with_its_channel_and_never_its_value` (`test_redact.py:381`) calls `monkeypatch.undo()` (`:393`). That undoes `dev_db_tx`'s `monkeypatch.setattr(db, "connect", fake_connect)` (`conftest.py:188`), which is on the same `monkeypatch`. `redact(…, channel="mattermost")` (`:401`) then reaches `RedactionStore.record` (`guard.py:186` → `redact/store.py:57-62`) on `db.connect`'s `psycopg.connect(dsn, autocommit=True)` (`db.py:199`). The result is one durable row per with-DB pass 1 on any branch. `test_redact.py` last changed in `4b3403df` (2026-09-10). This is consistent with `<fb>:243` (C1's `<P0>` 177 at 10:00) and `17`'s 180 / `5acf3646…` at 12:41 |
| 2 | The cause is a pass-1 leak; run `--proof-only`, pass 1 alone, `--proof-only` (Opus inference) | file-check `:112` (NOT CHECKABLE FROM READS) | OUT OF SCOPE | as #1; L70 | The attribution in #1 is from reads. It is not a C1 defect, whatever a run shows. The cheap run belongs to R61's OWED item, not this fix: under the lock, `--proof-only`, then `COBALT_ENV=dev uv run pytest -q -p no:cacheprovider "tests/cobalt/test_redact.py::TestTheCounter"`, then `--proof-only`. Expected: `cobalt_redactions` +1, every other table equal. `35` records the table as a known outside writer (compared, recorded, never a gate) |
| 3 | `test_a_note_failure_after_the_commit_keeps_the_p_missing_banner` never asserts the result card (Opus (a)1) | `:131` (FTC 2), file-check `:113`; `:81` | NOT REAL | `29:25` F2 red column: `[p missing]` → "the response carries `DRIFT_NOT_EVALUATED` and `marked FILLED`" | The test asserts exactly what `29`'s row names (`test_fill_c1_offline.py:387-393` at `3ceb3b11`). The result card is the unconditional shared tail `_result_card(original, form, fill=fill_result)` (`aset/web.py:1173-1177`); no branch on P or on the note outcome precedes it. `test_a_note_failure_after_the_commit_keeps_the_drift_warning` asserts `STRUCTURAL_WARNING` (`:404`), which only the result card renders, through that same tail. It was PASSED (`<fb>:87`) |
| 4 | `_db.connect is not REAL_CONNECT` proves only that the suite patched (Opus (a)2, "not blocking") | `:132` (FTC 3), file-check `:114`; `:81` | NOT REAL | `29:24` F1 red column: "Its red is W (c3m) MUTATION"; L70 | The assertion is a precondition guard. F1's proof is the mutation red, run and quoted (`<fb>:188-197`: RED at `test_fill_transaction_db.py:263`, `git diff` empty, re-run PASSED). A "not blocking" note is not a defect by itself |
| 5 | C1-added lines still carry `<value>`s of the base replay card: `fill_shares` at `test_aset_web.py:217`, `:251`, `:567`; `orig_timestamp` at `test_fill_c1_offline.py:296` (Opus note) | `:133` (FTC 4), file-check `:115` HOLDS; `:84` | **FIX → F5** | `20:43` index card L32: "constructed values only; no ticker, price or date of his in any file"; round 1 #13 → F4 (same class, `reports/s3-exits-c1-fix-r1-draft-2026-09-28.md:32`) | My reads: `git diff c1dc476d 3ceb3b11 -- tests/cobalt/test_aset_web.py` shows the three `fill_shares` lines as `+`. Their `<value>` equals the derived `shares` of C1's replay row at `5164f867:tests/cobalt/test_aset_web.py:197` before F4. `test_fill_c1_offline.py` came in with C1 (`c57634f8`, `eb642f05`). Its `:296` `orig_timestamp` `<value>` equals the base replay card's (`c1dc476d:tests/cobalt/test_aset_web.py:188`). It is the only `+` line of `c1dc476d..3ceb3b11` carrying that date. F5 = those four C1-added values only: `fill_shares` → the constructed row's `30` (`test_aset_web.py:197`); `orig_timestamp` → the suite's constructed instant `2026-09-03T10:00:00-04:00` (`conftest.py:233` `FROZEN_NOW`). The `actual_fill` `<value>` on `:567` and every `orig_timestamp` in `test_aset_web.py` predate C1 → R61 ESC 2 (OWED), untouched |
| 6 | Suites HOLD on quoted output; re-execution NOT CHECKABLE FROM READS (Opus (v)) | `:79` | NOT REAL | `29:29` RUN R1; L35 | RUN R1 was executed by the builder and quoted whole (`<fb>:93-201`); `packet.md` carried it verbatim (`<chk>:46`). A check seat cannot run commands; that is the check's shape, not a finding |
| 7 | The hub's L74 block (ESC 8) | `:12`, `:140` | NOT REAL | L74 | Data, recorded once by that hub |

Composite lines map to the rows above: Opus's CHECK line (`:83`) = #1 (+ #2). Grok's CHECK line (`:83`) = #1. Hub ESC 1–2 = #1; ESC 3–6 = #1, #3, #4, #5.

## RECORDS
- Sol METER (`<chk>:35`, `:66`, `:139`): 2 of 3 houses checked. The L67 floor is met (Opus + Grok). A METER turn spends no round (L67). The hub's `ASK DESK` (relaunch Sol alone) is moot: round 3 seats Sol again.
- Round (L39): `30` was round 2 (`<chk>:141`). `36` is round 3 of ≤3, THE LAST. A HOLD there goes to the desk and then to him; there is no round 4.
- #1 / #2 → R61's OWED `cobalt_redactions` item, now with a named writer (`tests/cobalt/test_redact.py:393`) and a named run (#2). Until it is fixed, every with-DB pass 1 moves `cobalt_redactions` by +1. So every build's per-table proof (R1 here, `17`'s, the integrated gate's) differs on that one table. `35` / `36` compare it and record it; it never gates.
- `<fb>` ESC 2 / R61 OWED: the base replay lines (`test_aset_web.py:97`, `:101`, `:102`, `:103`, `:129`, `:183`, `:323`, `:516`, `:531`, `:540`) and their `orig_timestamp` / `actual_fill` values predate C1. F5 touches none of them.
- `fills.drift_warning_pct` stays out (R43 (5)); no row touches it.

## OWNER ITEMS
NONE.

## FOR DEJAN
New rule strings: NONE. `35` = `29`'s 24 allow + 3 deny; `36` = `30`'s 10 allow + 3 deny.

## FOR THE DESK
- C1 does not stand at `3ceb3b11`: FIX F5 (#5). `22` stays held (K3) until `36` reads `ready for C2: YES`.
- Wrote `prompts/2026-09-28/35-s3-exits-c1-fix-r2-build.md` (13:41) and `prompts/2026-09-28/36-s3-exits-c1-fix-r2-check.md` (13:43).
- `comm` of the sorted double-quoted launch-line tokens (13:43):
  - `29` line 5 vs `35` line 5: 27 common. Only the `Read '…'` path differs. With the prompt name and the `--remote-control` / `--name` value masked, `diff` is empty. `35` line 3 (the desk's preconditions) is byte-identical to `29` line 3.
  - `30` line 1 vs `36` line 1 (the `claude --bg …` span): 13 common. Only the `Read '…'` path differs. `diff` with the names masked is empty.
- Placeholders to fill at launch:
  - `35`: `R__` (line 36) and the desk's `<base>` read (line 14, `FILL AT LAUNCH`). The drafter's read is `9b25eced`.
  - `36`: `R__` (line 15), `<build stop>` (line 4) and `<tip>` (line 5), from `35`'s stop line.
- `35` launches under L76 (no `.env` under `~/cobalt-wt/*`, no with-DB run in flight). `36` launches after `35`'s stop line.
- F5 is tests only. The expected numbers are fix r1's: offline 3246, with-DB 3617 + 33, live-note 146, `RESTARTS: none`.
- R61 OWED `cobalt_redactions` now has a writer (`tests/cobalt/test_redact.py:393`) and a run (#2). It needs its own owner and fix, outside S3.

## ESCALATE
1. #1 / #2: the writer of `cobalt_redactions` is attributed from reads, not a run (L70). This does not change the class: no line of the range names `redact`. `ASK DESK: who owns the test_redact.py leak fix (R61 OWED)? [13:44 ET]` Safe default: recorded only; nothing here builds it.
2. `35`'s W is `29`'s W without (c3m). (c3m) was F1's mutation red; the row is closed and F5 edits no `src`. F1's test still runs in pass 2, and (c3r) keeps the two `X1RF` zero-row reads. `ASK DESK: restore (c3m) in 35? [13:44 ET]` Safe default: dropped (a tests-only fix edits no `src`).
3. `35` (f2) and `36` (iii) make `cobalt_redactions` a known outside writer: compared and recorded, never a gate. `35` escalates it only if its row count falls or grows by more than 1 (one `TestTheCounter` run per pass 1).
4. L74: the block is recorded once under `## L74`.

## CONTINUE
- next: none. The desk reads this report, commits the three files (`35`, `36`, this report), fills the placeholders and launches `35` under L76.

S3 EXITS C1 FIX R2 DRAFTED · FIX: 1 · NOT REAL: 4 · UNPROVEN: 0 · OUT OF SCOPE: 2 · OWNER ITEM: 0 · prompts: 2 · C1 stands: NO · new rule strings: 0 · ESCALATE: 4
