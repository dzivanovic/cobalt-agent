# S3 exits C4 fix r1 — drafter report (2026-09-29)

Seat `s3-exits-c4-fix-r1-draft-0929` (Opus 5.5, auto), desk row R101 (`cto-2026-09-29.md:109`, authorization ✓). Start `date` → `Tue Sep 29 15:53:26 EDT 2026`. `<r1>` = `reports/s3-exits-c4-check-2026-09-29.md`; `<b>` = the C4 build report on `s3/exits-c4`; `<o>` / `<g>` = `opus-check.md` / `grok-check.md` in `agy-trial/scratch/tribunal-bars-0920/s3-exits-c4/`. Branch tip read 15:57: `cfd9f091` over `a0ac51c4` over `d05ae72d` (as expected). Code read at `d05ae72d` by `git show`.

## §0 Headline
- 2 FIX findings → ONE row, F1, tests only: a guard in `tests/cobalt/conftest.py` fails any test that resolves a trade-note path outside `tmp_path`, and C3's with-DB route fixture gets a `tmp_path` vault. No file under `src/` changes.
- 2 RUNS for the UNPROVEN: U1 posts NaN / −1 to the manual `/fill`; U2 prints a typed `exit_price: 5.10` line before and after a later write.
- X3 (human wins once) = OUT OF SCOPE, not an owner item: L28 and v3 §7 already rule "human wins"; the fix is in the shared vault writer, which `26` and v3 route outside C4. ESCALATE 1 asks the desk to route it.
- 12 NOT REAL · 3 OUT OF SCOPE · 0 OWNER ITEM. Written: `24-s3-exits-c4-fix-r1-build.md`, `25-s3-exits-c4-fix-r1-check.md` (Opus · Sol · Grok). No new rule string. ESCALATE 7.

## L74
Recorded once: a system-reminder block arrived appended to the first tool result (the read of this prompt file), asking for a `Claude-Session:` line in commits and PR bodies and naming a file-send tool. Not followed; I commit nothing and sent no file.

## Classification
Every class is taken from the hub's file-check column (`<r1>` `## Checked against the branch`, `:76-84`) or, where the hub walked nothing, from the seat's own line (L35 / L70).

| # | finding (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|
| 1 | C3's with-DB route tests fill through C4's note hook with no `tmp_path` vault; two C4 notes (`ZZPB`, `TEST`) sit in the dev vault, unreported (Opus (9) DOES NOT HOLD; hub HOLDS as a defect) | `<r1>:78`, `:54`, `:101`; `<o>:13` | FIX → **F1** | `26:75` "every vault write in a test goes to `tmp_path`"; `27:31` question (9) "every test write in a `tmp_path` vault"; L28; L1. Walked: `conftest.py:76` clears `COBALT_VAULT_PATH` → `configs/dev/vault.yaml:23` `~/dev-vault-cobalt`; `panel_world` (`test_s3_c3_panel_db.py:43-55`) patches no vault; `_filled` posts `/fill` at `:84`; the trade-note writer resolves every path through `resolve_target` (`trade_note.py:256`, `:422`); `_fill_note` / `_leg_note` swallow every exception (`web.py:1542-1573`) | (a) an autouse guard wraps `cobalt.prefill.trade_note.resolve_target`: a path outside `tmp_path_factory.getbasetemp()` is recorded and raises before any read or write, and the teardown `pytest.fail`s (the swallow is why a raise alone is not loud). (b) `panel_world` gets `make_vault(monkeypatch, tmp_path)`; `note_world` reuses it (a second `make_vault` in one `tmp_path` raises on `mkdir`). Red: the C3 fill tests ERROR at teardown naming the dev-vault path, even with the two notes present (the guard trips before the X16 existence check). Plus a with-DB "note lands in the tmp vault" test. |
| 2 | X3: after his hand edit, the next write of that unit replaces his line with no override row (builder ESCALATE 1; Grok's only exception; Opus ESCALATE 1) | `<r1>:81`, `:102`, `:60`; `<b>:221-226`, `:63`; `<o>:28`; `<g>:29` | OUT OF SCOPE | Real — hub HOLDS, measured offline and on the real `vault_writes` store (`<b>:85`). The RULE is settled: L28 ("a Cobalt line he changed → human wins, logged as override"), v3 §7 (`S3-EXITS-v3-2026-09-22.md:226`), `26` C4-3. So it fails the owner test (L67 OWNER ITEMS: a question the houses can settle, not his money, data, law or trading call) and is no owner item. The MECHANISM is `VaultWriter.upsert_unit`'s baseline (`writer.py:750`, `:766`: `unit_after` = the merged body, which is the next merge's base), shared by every Cobalt unit writer. v3's X3 row (`:306`) and `26:87` say a silent overwrite is design-changing and "C4 builds nothing to fix it" | Not built here (L75: the fix widens nothing; a shared seam is settled before a build, L72). The desk routes it (ESCALATE 1). R35 (3) is not touched (L77). |
| 3 | Manual `/fill` parse has no finite-and-positive guard (Opus ESCALATE 3) | `<r1>:80`, `:103`; `<o>:30` | UNPROVEN | L70; the hub: "HOLDS as a fact; effect NOT CHECKABLE FROM READS". Walked: `web.py:1110-1113` catches only `InvalidOperation` | RUN **U1** (E2, with-DB, `d05ae72d` src, in a `tmp_path` vault): NaN and −1 posted to `/fill` on a manual card; status, body, counts and the card row printed and quoted. A 500 or a stored NaN / negative → ESCALATE for round 2, never fixed here (C1's route). |
| 4 | A typed `5.10` is written back as `"5.1"` by the frontmatter merge (Opus (4), "older quirk") | `<r1>:49`; `<o>:8` | UNPROVEN | L70: no seat or the hub ran or walked it; it bears on R35 (3) "a value he typed … never overwritten", which C4's close write now exercises | RUN **U2** (E2, offline): the raw `exit_price` line before and after a later write, quoted. A changed byte → ESCALATE for round 2, never fixed here (`vaultwrite/frontmatter.py`). |
| 5 | No C3 route test asserts the note notice is absent or the vault is `tmp_path` (Opus (a)) | `<r1>:58`; `<o>:22` | FIX → **F1** | Same defect as row 1 (the reason it went unseen) | F1's guard is that check, suite-wide for the trade-note writer. |
| 6 | The X3 tests keep the silent overwrite green (Opus (a)) | `<r1>:58`; `<o>:21` | OUT OF SCOPE | Rides with row 2 | They measure X3; they change with X3's own fix. Untouched here. |
| 7 | The two dev-vault notes need removing by the desk (Opus ESCALATE 2; hub ESCALATE 1) | `<r1>:101`; `<o>:29` | OUT OF SCOPE | This prompt (`23`): "the desk removes nothing in any vault"; L28 (a vault edit is not a build row) | A RECORD in `24`'s report: `ls -la` of both at PREFLIGHT and CLOSE, equal. After F1 no test resolves the dev vault, so the X16 refusal they cause is moot. |
| 8 | `test_profit_loss_and_rvol_are_never_written` checks only the key set (Opus, Grok (a)) | `<r1>:82`, `:58`, `:104` | NOT REAL | Q(4) HOLDS in both seats (`<r1>:49`): `HIS_FILLED_KEYS` (`trade_note.py:68`) excludes both; no law makes a test fact a FIX | A test fact. Nothing tightened (L75). |
| 9 | The rollback test passed on base (Opus (a)) | `<r1>:83`, `:58`; `<b>:85` | NOT REAL | Q(2) HOLDS in both seats (`<r1>:47`: commit `store.py:326`, rollback `:327-329`, note after return `web.py:1182`, `:1640`) | Disclosed as a guard; base writes no fill note, so a red is impossible by construction. |
| 10 | The X16 test asserts the banner prefix only (Grok (a)) | `<r1>:84`, `:58` | NOT REAL | Q(6) HOLDS in both seats (`<r1>:51`); the hub: NOT CHECKABLE, not counted (L70). Read at `d05ae72d`: `test_s3_c4_trade_note_db.py:137-149` also asserts the retry command, `trade_note_path` NULL and the first note's bytes unchanged | A test fact. |
| 11 | The one-estimated-exit test does not assert `exit_time` (Grok (a)) | `<r1>:58`; `<g>:51` | NOT REAL | Q(4) HOLDS; `exit_time` is asserted in the close tests Q(4) cites (`offline.py:154-224`) | A test fact. |
| 12 | `Dejan` in comment prose (Grok (11)) | `<r1>:56`; `<g>:45` | NOT REAL | L31 governs identifiers; the prose is pre-existing (`diff.part1.md:336`) | Nothing widened. |
| 13 | Grok's (9) HOLDS covers the C4 tests only | `<r1>:79` | NOT REAL | Hub: "HOLDS for the C4 files only" (`trade_note_support.py:65-72`) | Not a finding; row 1 carries (9). |
| 14 | Astra did not check (METER, back 17:04) | `<r1>:105`, `:60` | NOT REAL | L67 floor met (Opus + Grok); R100 (ASK DESK 5 → NO) | A record. `25` seats Sol in Astra's place (K22). |
| 15 | The standing line (round 1 of ≤3; a HOLD → a fix round) | `<r1>:106` | NOT REAL | L39, L67, L75 | A record. `25` carries round 2's. |
| 16 | FC1 SCOPE: NOTHING WIDENED | `<r1>:95` | NOT REAL | Q(11) HOLDS; hub path union | A confirmation. |
| 17 | FC2 `prefill/drc.py`, `prefill/daily.py` untouched | `<r1>:96` | NOT REAL | Q(8) HOLDS; hub (i) EMPTY | A confirmation. |
| 18 | FC3 one note writer | `<r1>:97` | NOT REAL | Q(1) HOLDS; hub (iii) ONE | A confirmation. |
| 19 | FC4 `trade_note_path` through one store method | `<r1>:98` | NOT REAL | Q(3) HOLDS; hub (ii) | A confirmation. |

Each seat's CHECK line item: Opus `FIX (9)` = row 1; Grok `EXCEPT X3 human-wins-once` = row 2; Astra METER = row 14.

Totals: FIX 2 (→ 1 row, F1) · NOT REAL 12 · UNPROVEN 2 (→ 2 RUNS) · OUT OF SCOPE 3 · OWNER ITEM 0.

## RECORDS
- `<r1>` round 1: Opus FIX (9) · Astra METER · Grok BUILD STANDS EXCEPT X3; 2 of 3 checked, floor met (R99, R100).
- `<b>` ESCALATE 2–11 (owner defaults O4 A / O11 A / O12, R35 (3)'s narrower writes, the merge render, the leg line, `/size`'s card, the X16 residual, a failed retry NULLs the path, lock takes, E0's red, X14): no seat flagged any as a defect; they stay with the build report.
- The dev vault also holds two empty folders, `_f1-tests` and `_l28-tests` (Sep 29 14:16 / 14:22, `ls -la ~/dev-vault-cobalt/`) — not C4's; for the desk.
- `24` / `25` carry the `R__` row placeholder and `«FILL AT LAUNCH: …»` values; `25`'s `<packet ceiling>` is the desk's (K17).
- RULE STRINGS checked (16:00 ET): `24` line 5 equals `26` line 6 after the path and name substitutions (`cmp` identical); `comm -3` of the sorted quoted tokens prints only the two `Read '…'` paths (28 tokens each). `25`'s launch line against `27`'s (tokens from `claude --bg` to the last `--add-dir`): `comm -3` prints only the Astra / Sol `codex exec` pair and the two `Read '…'` paths (18 tokens each); the Sol string has `grep -c -F` = 1 in `04` line 1. `25`'s §2 SOL seat is `30-s3-exits-c1-fix-r1-check.md:43`, as `04` cites it.
- Sizes: `24` 26,998 B; `25` 16,438 B.

## OWNER ITEMS
NONE.

## FOR DEJAN
New rule strings: NONE.

## ESCALATE
1. **X3 routing — ASK DESK** [16:03 ET]: X3 is real and blocks nothing in this round's rows, but it touches his notes. It needs its own item: the vault writer's baseline rule (`writer.py:750`, `:766`) for every Cobalt unit writer, designed and checked by the houses (L67). Note: L28's sync-revert clause keys on "Cobalt's last 10 `unit_after` values". If the fix changes what `unit_after` holds, that clause's wording may need a fold, and a fold is his (L58). Also for the desk: whether the S3 deploy set waits for that item. Safe default taken: no owner item; nothing built; `25` asks each seat to say whether X3 decides its `ready` answer.
2. `24`'s stop line drops `26`'s `X: <k> of 4 run` field. A fix round runs no experiments (`03`'s precedent form); every other field is `26`'s, with `| FIX | RUNS | ESCALATE` appended.
3. F1's guard wraps only `cobalt.prefill.trade_note.resolve_target`, the C4 writer's one resolver. Other vault writers in tests are not guarded, so nothing outside C4 widens (L75). A pre-C4 test that reaches the trade-note writer unpatched (for example a `/size` route test) will trip it. `24`'s E2 offline run names each such test, and F1 fixes it with `make_vault` in its own fixture only. A trip first seen at W costs a third lock take, so it is an ESCALATE line in `24`.
4. `25`'s folder is `s3-exits-c4-fix-r1/`. The four R88 `cp` strings write only into round 1's `s3-exits-c4/files/`, so `25` refreshes and names those copies there. It also adds Opus's `--add-dir` for that folder (inside the standing `claude -p` string) and one sentence to Grok's prompt. No new rule string.
5. The DESK LINE: `24` launches only while `ls ~/cobalt-wt/*/.env` has no match and no with-DB run is in flight (L76). `21` (DRC D3 fix r2, `~/cobalt-wt/drc-d1`) takes the lock at its F3 / F8; the second taker waits. `## OWNER ITEMS` is empty.
6. `25`'s report goes to `reports/s3-exits-c4-fix-r1-check-<D>.md`, as `27`'s did (its Write there worked, R99). A refused Write falls back to `S/CHECK-REPORT.md`, named in §0.
7. L74: recorded once under `## L74`.

## CONTINUE
next: none. The desk verifies (L35) and commits `24`, `25` and this report. It writes `24`'s launch row (`<base>`, `no with-DB run in flight`) and launches it under the DESK LINE (ESCALATE 5).

S3 EXITS C4 FIX R1 DRAFTED · FIX: 2 · NOT REAL: 12 · UNPROVEN: 2 · OUT OF SCOPE: 3 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 7
