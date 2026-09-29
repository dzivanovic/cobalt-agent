# S3 EXITS C2 CHECK, ROUND 1 — 2026-09-28

Hub `s3-exits-c2-check` (Sonnet 5.5), desk row R147. `<D>` = 2026-09-28. First `date`: `Mon Sep 28 19:48:58 EDT 2026`. Range `bbf25412..77cf18fd` on `s3/exits-c2`. Builder's report `/Users/cobalt/cobalt-wt/s3-exits-c2/docs/40 - DevDocs/reports/s3-exits-c2-build-2026-09-28.md`. I give no verdict (L37); the checkers' words are theirs.

## §0 Headline
- Round 1 of ≤3: Opus 5.5 `BUILD STANDS EXCEPT` three items (`ready for C3: YES`); Grok `BUILD STANDS` (`YES`); Astra METER at 20:12, back at 8:58 PM — 2 of 3 houses checked, floor met (Grok).
- I walked every Opus `DOES NOT HOLD` in the real files: 3 of 3 HOLD as claims (sheet/CLI CLOSE at running above 0 · a second fill-cache writer · ✓ confirm refused on a pre-C1 closed card). Grok's four weak-assertion and path items are facts, none a defect.
- My own checks (i)–(v): all as expected. No route, migration or `radar/` `prefill/` `drc/` `settings/` change.
- `defects that HOLD: 3` → `ready for C3: NO` by the stop line's own rule; the desk classifies first (L75).
- ESCALATE 6.

## L74
None arrived in a tool result during this run.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | `Mon Sep 28 19:48:58 EDT 2026` |
| placeholder `R_[_]` | `grep -n -E "R_[_]" …/23-s3-exits-c2-check.md` | 1 | (nothing) |
| placeholder `FILL AT LAUNCH` | `grep -n -F "FILL AT LAUNCH" …/23-s3-exits-c2-check.md` | 1 | (nothing — `23` carries no gate line of its own; no hit) |
| R17 | `grep -n "^| R17 " …/cto-2026-09-24.md` | 0 | line 35, carries `Grok approved with no asking going forward` |
| R19 | `grep -n "^| R19 " …/cto-2026-09-24.md` | 0 | line 37, carries `All 4 house models approved` |
| R19 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"All 4 house models approved" -- …/cto-2026-09-24.md` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |
| house gates again, right before launch (20:10:53) | the R17 and R19 greps, `-c` | 0 | 1 and 1 |
| seats | `grep -n "^| R95 " …/cto-2026-09-23.md` · `grep -n "^| R109 " …/cto-2026-09-22.md` | 0 · 0 | R95 line 103 (CHECKER SEATS); R109 carries `Make all Opus` |
| launch row R147 | `grep -n -F "23-s3-exits-c2-check.md" …/cto-2026-09-28.md` | 0 | line 156, `| R147 | 19:48 ET | …` names this file, carries the build stop and the literal `no other house hub is running` |
| R147 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"23-s3-exits-c2-check.md" -- …/cto-2026-09-28.md` | 0 | `e7d35a213603eaddbafbfaac35c7c40e1d8c9191` |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| report tail | `tail -n 3 "<report>"` | 0 | last non-blank line EQUALS `<build stop>` and starts `S3 EXITS C2 BUILT ` |
| commits | `git -C /Users/cobalt/cobalt log --oneline bbf25412..77cf18fd` | 0 | `77cf18fd feat(s3): C2 — exit legs, running, corrections, held count, CLOSED, realized R, the FILLED stop edit (v3 §2–§3 / §5, R67, R38)` · `8c4f116f wip(s3-c2): red` · `80e0c8a2 wip(s3-c2): E1 experiments` |
| stat | `git -C /Users/cobalt/cobalt log --stat --format=%h bbf25412..77cf18fd` | 0 | `77cf18fd`: `docs/40 - DevDocs/cobalt/cards/{cli,legs,store}.md`, `src/cobalt/cards/{cli,legs,store}.py`, `tests/cobalt/test_legs_c2_db.py` · `8c4f116f`: `tests/cobalt/test_legs_c2_db.py`, `test_realized_r.py`, `test_s3_c2_experiments.py` · `80e0c8a2`: `tests/cobalt/test_s3_c2_experiments.py` |
| `.env` | `ls /Users/cobalt/cobalt-wt/s3-exits-c2/.env` | 1 | `No such file or directory` (never read) |
| scratch | `ls scratch/tribunal-bars-0920/s3-exits-c2` | 1 | absent = fresh |
| stagger | `grep -n -F "no other house hub is running" …/cto-2026-09-28.md` | 0 | the R147 line also names `23-s3-exits-c2-check.md` |
| probe OPUS | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` | 0 | `OK` (UP; stderr note: `Permission deny rule (../../cobalt/.claude/settings.local.json): Bash(git push*:*) mixes * with the trailing :* prefix syntax…`) |
| probe ASTRA | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` | 0 | `OK` (UP at 19:5x; it hit its meter at 20:12, below) |
| probe GROK | `grok --version` | 0 | UP |

## Files copied
`S` = `scratch/tribunal-bars-0920/s3-exits-c2/`. The diff was saved to the job tmp folder (92,150 B, 3 commits) and written in 4 parts; each part headed with its git command (100 B header).
| copy | bytes (copy − 100 B header where a diff part) | original | match |
|---|---|---|---|
| `S/diff.part1.md` … `part4.md` | 36,605 + 14,691 + 24,369 + 16,485 = 92,150; `grep -c "^commit "` = 1+0+1+1 = 3 | `git log -p bbf25412..77cf18fd -- . ":(exclude)docs"` 92,150 B, 3 commits | yes |
| `S/rulings.md` | 3,179 | R67 (`cto-2026-09-22.md:99`) and R38 (`cto-2026-09-20.md:275`), each under its command | — |
| `S/files/s3-exits-c2-build-2026-09-28.md.part1/.part2` | 14,193 + 24,527 = 38,720 | the report, 38,720 | yes |
| `S/files/22-s3-exits-c2-build.md` | 19,994 | 19,994 | yes |
| `S/files/20-s3-exits-c1-build.md` | 31,610 | 31,610 | yes |
| `S/files/s3-exits-c1-build-2026-09-28.md.part1/.part2` (C1's report on `s3/exits-c1`) | 14,271 + 29,237 = 43,508 | 43,508 (worktree and `git show s3/exits-c1:…` agree) | yes |
| `S/files/S3-EXITS-v3-2026-09-22.md.part1/.part2/.part3` | 35,192 + 30,038 + 13,730 = 78,960 | 78,960 | yes |
| `S/files/LAWS.md.part1/.part2` | 34,611 + 26,400 = 61,011 | 61,011 | yes |
| `S/files/wt/src/cobalt/cards/legs.py` | 30,944 | 30,944 | yes |
| `S/files/wt/src/cobalt/cards/cli.py` | 11,330 | 11,330 | yes |
| `S/files/wt/src/cobalt/cards/store.py.part1/.part2/.part3` | 29,483 + 9,112 + 29,357 = 67,952 | 67,952 | yes |
| `S/files/wt/tests/cobalt/test_legs_c2_db.py` | 23,683 | 23,683 | yes |
| `S/files/wt/tests/cobalt/test_realized_r.py` | 2,744 | 2,744 | yes |
| `S/files/wt/tests/cobalt/test_s3_c2_experiments.py` | 9,519 | 9,519 | yes |
The worktree HEAD is `0d591041` (the report commit); `git diff --stat 77cf18fd 0d591041` touches only the report, so the source copies equal the tip. `S/CHECK-INSTRUCTIONS.md` = the QUESTIONS verbatim + the "Files:" paragraph. `ls -la S` before launch (20:10:53) held 10 lines and no seat output; after: `astra-check.partial.md`, `grok-check.md` appeared, both seats' own or mine from stdout (`opus-check.md` written by me from stdout).

## CONTINUE
next: none. The desk classifies (L75) and decides C3.

## Clock
| event | `date` |
|---|---|
| seats launched (all three, one message) | ~20:11 (`date` 20:10:53 just before) |
| ASTRA stopped: METER | 20:12:29 (its output read then) |
| OPUS answer read | 20:14:39 (`opus-check.md` present, exit 0) |
| GROK answer read | 20:24:40 (task completed, exit 0) |
No seat neared the 45-minute clock.

## Per question
| Q | opus | astra | grok |
|---|---|---|---|
| (1) | HOLDS. `legs.py:285-336` only read, lock `:300-304`, five callers all locked; basis `:317-322`. Edge: a pre-C1 CLOSED card has no basis, so ✓ confirm is refused (`:323-327`). | METER | HOLDS. `legs.py:285`; lock `:300-303`; callers `:417 :552 :644 :725`, `store.py:787`; basis `:317-322`. |
| (2) | HOLDS. Exit `:403-437`, correction, held, stop edit `store.py:733-827`; X7 `test_legs_c2_db.py:545-565`; X21 before-fix report line 74. | METER | HOLDS. Same lines; X7 `:485-565`; X21 report `:74`, red `:89`, after-fix `test_s3_c2_experiments.py:172-176`. |
| (3) | HOLDS. Table of nine refusals with `legs.py` lines, all raised before any INSERT; tests `test_legs_c2_db.py:119-408`. | METER | HOLDS. Each refusal cited with its line and test; `SessionBlocked` on all four writers `:391-408`. |
| (4) | HOLDS for C2's writers (`_close_if_zero` `legs.py:228-238`). DOES NOT HOLD for "nowhere else": `web.py:1236-1258` and `cli.py:75-96` still move FILLED → CLOSED at running above 0. | METER | HOLDS. `_close_if_zero`; `cli.py:89` is "the pre-existing generic `cards move`, not the running-to-0 path". |
| (5) | HOLDS. `legs.py:651`, `:659-667`; test `:310-324` (84 shares, running 50). | METER | HOLDS. `record_held` `:607-668`; same test. |
| (6) | Append-only HOLDS. One writer DOES NOT HOLD: `_rewrite_fill_cache` `legs.py:468-481` is a second writer of the fill cache (L3, L40); `aset/store.py:361-362` says "written only by `mark_filled`". | METER | HOLDS. No UPDATE of `legs`; `:576`, `:588-589`; test `:266-284`. |
| (7) | HOLDS. `legs.py:683-711`; `realized_r.1` `:65`; never stored `:733`; tests `test_realized_r.py:25-72`. | METER | HOLDS. Same lines; long 1.5, short 2, provisional, zero unit. |
| (8) | HOLDS. `store.py:786-804`, `:752-763`, `:849-861`; X20 tests `test_s3_c2_experiments.py:184-207`. | METER | HOLDS. `store.py:787-805`, `:753-764`, `:850-862`; same X20 values. |
| (9) | HOLDS. `expire.py:71`, `:182`; X-OPEN `:232-242`; next-day leg `test_legs_c2_db.py:411-419`. | METER | HOLDS. `expire.py:71`, `:182-183`; X-OPEN and next-day leg. |
| (10) | HOLDS from the report (counts not re-derivable by reading): 3252 / 3621 + 63 / 146; re-run needed to confirm. | METER | HOLDS as quoted; deselects named; 63 = 33 + 30; `.env` removed before the stop line. |
| (11) | NOTHING WIDENED. L31: one prose mention, `legs.py:5` docstring. | METER | NOTHING WIDENED. Prose word at `legs.py:5` and `cobalt/cards/legs.md:4`, not an identifier. |
| (a) | (1) `test_legs_c2_db.py:245-251` no nothing-written assert; (2) `:330-331` same; (3) `:372-383`, `:391-408` no `card_stop_edits` count; (4) no test of the plan-at-fill cache branch; (5) no test of a pre-C1 closing-exit correction. | METER | (1) `:245-251` refusal text only; (2) `:326-328` holding 0 does not assert `evidence["leg_id"]`; (3) `:438` asserts the prefix `realized R: `, not the figure. |
| (b) | `legs.py:468-481` DOES: an entry-price correction rewrites `recomputed_shares` / `share_delta` through `compute_fill_recompute`; `store.py:813-823` DOES: WATCH stop edit writes `shares` (already there). No score, rank or grade. | METER | `legs.py:465-480` DOES write a share count (the cache, not planned `shares`, grade, rank or score); the FILLED edit writes no `shares`. |
| closing line | `CHECK S3 C2: BUILD STANDS EXCEPT (4) sheet/CLI CLOSE at running>0, (6) second fill-cache writer (L3), (1) pre-C1 CLOSED correction refused · ready for C3: YES` | METER (`astra-check.partial.md`: `PARTIAL — METER`, "try again at 8:58 PM") | `CHECK S3 C2: BUILD STANDS · ready for C3: YES` |

## Suites
From the report, not re-run by me (`<report>` line numbers as in the file):
- Offline (`:114`): `3252 passed, 438 skipped, 1 xfailed, 20 warnings in 559.92s`, exit 0, 0 failed, 0 errors.
- With-DB pass 1 at `0013` (`:120`): `3621 passed, 6 skipped, 63 deselected, 1 xfailed, 20 warnings in 649.34s`, exit 0. Deselected (`:118`, named): `test_tenancy.py::TestMigrationRoundTrip` · `test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default` · `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` · `test_voice_store.py` ×3 (`test_store_round_trip_and_single_flight_in_the_suite_transaction`, `test_the_reaper_fails_stale_rows_and_never_retries`, `test_single_flight_under_two_real_connections`) · `test_voice_confirm.py::test_x13_with_db_…` · `test_voice_lifecycle.py::test_e7_kill_mid_turn_…` · `test_legs_db.py` · `test_fill_transaction_db.py` · `test_legs_c2_db.py` · `test_s3_c2_experiments.py` · `test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled` · `test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk` (63 in all).
- Forward (`:121`): `dev forward: APPLIED 16:44:15`; pass 2 at `0021` (`:126`): `63 passed, 5 warnings in 137.64s`, exit 0, no skip, no fail line. Total with-DB 3621 + 63 = 3684.
- Live-note (`:129`): `146 passed, 1 skipped, 15 warnings in 26.11s`; the one skip is `test_replay_line.py:256 … COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, none names `COBALT_LIVE_VAULT_ROOT`.
- Fingerprints: `F0` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`; `F1` = `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`; `F2` = `F0` (16:47:40, `cobalt_dev` at `0013`).
- `.env` (`:131`): `rm`, `ls` → `No such file or directory`, `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`, released 16:47:44, before the stop line (`:214`). X22 not repeated (C2 adds no migration).

## Scope
- Opus (11): NOTHING WIDENED (src only in `cards/legs.py`, `cards/store.py`, `cards/cli.py`; L31 one docstring word). Grok (11): NOTHING WIDENED (same; the word "Fable" in prose only). Astra: METER.
- My PREFLIGHT path union: `src/cobalt/cards/{cli,legs,store}.py`, `tests/cobalt/{test_legs_c2_db,test_realized_r,test_s3_c2_experiments}.py`, `docs/40 - DevDocs/cobalt/cards/{cli,legs,store}.md`. No route, render, note, migration; `git log … -- src/cobalt/radar src/cobalt/prefill src/cobalt/drc src/cobalt/settings src/cobalt/db_migrations src/cobalt/aset/web.py` is empty (check (i) below).

## Checked against the branch
Real files are `/Users/cobalt/cobalt-wt/s3-exits-c2/…` at `77cf18fd` (its tree equals HEAD `0d591041` outside the report).
| claim | who | file:line | result | note |
|---|---|---|---|---|
| FILLED → CLOSED at running above 0 is still written by the sheet move route | opus | `src/cobalt/aset/web.py:1236-1258` | HOLDS | Route refuses only `FILL_TARGET` (`:1236-1245`), then `store.transition(card_id, to_state, evidence={"via": "aset.sheet"})` (`:1250-1258`); edge FILLED → CLOSED is legal (`cards/models.py:105`). Not touched by C2 (`git log … web.py` empty). |
| the same through `cobalt cards move <id> --to CLOSED` | opus | `src/cobalt/cards/cli.py:75-96` | HOLDS | Only `FILL_TARGET` is refused (`:76-86`); `store.transition(…)` follows (`:89-95`). |
| `_rewrite_fill_cache` is a second UPDATE of the fill cache | opus | `src/cobalt/cards/legs.py:468-481` vs `src/cobalt/aset/store.py:360-386` | HOLDS | `legs.py` UPDATEs 6 of the 8 columns `_update_fill_cache` writes (all but `filled_at`, `drift_warning_pct`); its docstring `aset/store.py:361-362` says "written only by `mark_filled`". The builder named this (report ESCALATE 4). |
| ✓ confirm (a correction) of a closing exit is refused on a card filled before C1 | opus | `src/cobalt/cards/legs.py:552`, `:317-327`; `cli.py:104-109` | HOLDS | No entry leg + state CLOSED → neither FILLED branch matches → `LegRefused("no_position")`; `record_correction` calls `running_shares` at `:552`; `cmd_legs` exits on it. Loud, not silent. |
| weak: over-entry test asserts refusal only | opus, grok | `tests/cobalt/test_legs_c2_db.py:245-251` | HOLDS | Body: `pytest.raises(...)`, no assert after. |
| weak: held-on-CLOSED test asserts nothing written | opus | `test_legs_c2_db.py:330-331` | HOLDS | Only `pytest.raises` on `record_held`. |
| weak: holding 0 does not assert `evidence["leg_id"]` | grok | `test_legs_c2_db.py:326-328` | HOLDS | Asserts `zero.closed`, state CLOSED, shares, running — not the transition evidence. |
| weak: `cobalt cards legs` test asserts the prefix `realized R: ` | grok | `test_legs_c2_db.py:438` | HOLDS | `assert "realized R: " in out and "provisional" in out …`. |
| paths to a size: entry-price correction writes `recomputed_shares`; WATCH stop edit writes `shares` | opus, grok | `legs.py:468-481`; `store.py:813-823` | HOLDS | Both true; neither writes a score, rank, grade or planned `shares` on FILLED (`store.py:801-804`). |
Not checkable from reads: the suite counts (need the report's commands re-run). "No test of the plan-at-fill cache branch" and "no test of a pre-C1 closing-exit correction" are absences claimed by one seat from a read of the test files I copied, not from `grep` of the whole tree — stated as "not visible to this read" (L35).

Own checks:
- (i) `git -C /Users/cobalt/cobalt log --oneline bbf25412..77cf18fd -- src/cobalt/radar src/cobalt/prefill src/cobalt/drc src/cobalt/settings src/cobalt/db_migrations src/cobalt/aset/web.py` → EMPTY (exit 0).
- (ii) `grep -rn -F "INSERT INTO" …/src/cobalt/cards/legs.py` → one hit, `legs.py:203` (`INSERT INTO legs (`); `grep -rn -F "legs" …/src/cobalt/aset` → `aset/store.py:43, :224, :244, :308` — the call `legs.insert_entry_leg(`; every `legs` write is inside `cards/legs.py`.
- (iii) `grep -rn "def running_shares" …/src` → ONE, `legs.py:285`.
- (iv) `grep -rn "shares = %s" …/src/cobalt/cards/store.py` → `store.py:814` (the sized non-FILLED branch of `record_stop_edit`) and `:1300` (radar `tap_key`, WATCH); the FILLED branch UPDATE at `:801-804` names `stop`, `per_share_risk`, `used_risk` only. No FILLED path writes `shares`.
- (v) L32: this report holds only the constructed test values the builder used (`TEST`, `X7CT`, `X21LK`; 10.00, 9.90, 10.05, 10.02, 9.95, 100, 66) and no ticker or figure of his.

## FOR THE CLASSIFIER
- "`running_shares` is the only place running is computed, called only under the card lock, and its `basis` … `recomputed_shares`, else `shares`" — opus, grok — Q(1) — `legs.py:285-336`, `:300-304`, `:317-322` — HOLDS (the pre-C1 CLOSED edge is under ESCALATE 3).
- "Every writer opens ONE connection with `autocommit = False`, locks before reading running, commits once; X7 real connections; X21 before-fix in the report" — opus, grok — Q(2) — `legs.py:403-437`, `:528-596`, `:633-672`; `store.py:733-827`; `test_legs_c2_db.py:545-565`; report `:74` — HOLDS.
- "The nine refusals are loud and write nothing" — opus, grok — Q(3) — `legs.py:160-166`, `:360-371`, `:411-419`, `:542-571`, `:636-637`, `store.py:720` — HOLDS.
- "A leg, correction or held count that reaches 0 writes FILLED → CLOSED through `transition()` in the same transaction with the leg id as evidence" (C2's own writers) — opus, grok — Q(4) — `legs.py:228-238`, `:433`, `:591-592`, `:668` — HOLDS (the "nowhere else" half is ESCALATE 1).
- "The held count is an entry correction with `held_stated = X`, `shares = X + Σ exits`, price copied, `confirmed`" — opus, grok — Q(5) — `legs.py:651`, `:659-667` — HOLDS.
- "Corrections are append-only; `seq`/`kind` copied; entry-price correction rewrites the cache in the same transaction and leaves the fill transition's evidence alone" — opus (append-only half), grok — Q(6) — `legs.py:576`, `:588-589`; `test_legs_c2_db.py:266-284` — HOLDS (the L3 half is ESCALATE 2).
- "`realized_r.1` is pure, on the actual unit, provisional while any leg is estimated, never divides a zero unit, never stored" — opus, grok — Q(7) — `legs.py:683-711`, `:733` — HOLDS.
- "The FILLED stop edit prices from the running shares at the entry-leg price, never writes `shares`, resets only to `structural_stop`, `stop_owner` derived" — opus, grok — Q(8) — `store.py:752-804`, `:849-861` — HOLDS.
- "A FILLED card with running above 0 stays FILLED across a session boundary and an expiry cycle" — opus, grok — Q(9) — `expire.py:71`, `:182`; `test_s3_c2_experiments.py:232-242`; `test_legs_c2_db.py:411-419` — HOLDS.
- "NOTHING WIDENED; no vendor or person name in an identifier" — opus, grok — Q(11) — `legs.py:5` prose only — HOLDS; my checks (i)–(iv) agree.

## ESCALATE
1. **Opus — FIX (4) — my verdict beside it: none (L37); file-check HOLDS.** FILLED → CLOSED is still writable at running above 0 with no leg through the sheet move route (`aset/web.py:1236-1258`) and `cobalt cards move <id> --to CLOSED` (`cards/cli.py:75-96`); both predate C2, C2 widened neither. Opus: C3 (the route) and the desk (the CLI) must refuse CLOSED there as C1 refused FILLED. Grok does not raise it (it reads `cli.py:89` as pre-existing). For the classifier: FIX, OUT OF SCOPE for C2, or OWNER ITEM.
2. **Opus — FIX (6) — file-check HOLDS.** `_rewrite_fill_cache` (`legs.py:468-481`) is a second writer of the fill cache under L3/L40; `aset/store.py:361-362` still says "written only by `mark_filled`". The builder raised the same (its ESCALATE 4) and the desk's cross-session message told it to leave the question to this check under L3. Opus: the fix (a mode of the one writer that keeps `filled_at`) edits `aset/store.py`, outside C2's files. Grok read it as "not a second copy of the arithmetic" (`engine.py:266`) and does not call it a defect.
3. **Opus — item (1) edge — file-check HOLDS.** On a card filled before C1 (no entry leg), the ✓ confirm (`record_correction`) and `cobalt cards legs` are refused with `no_position` once the card is CLOSED (`legs.py:317-327`, `:552`). Loud. The builder's SEAM FOR C3 says ✓ confirm is a correction. Grok's basis reading (Q1) does not raise it.
4. **Astra did not check — METER.** Stopped 20:12 ET with the OpenAI usage-limit message; return time it names: 8:58 PM (2026-09-28). No round spent (L67). `ASK DESK: Astra did not check (METER, back 8:58 PM) — relaunch it alone at 20:58 or later? [20:12 ET, from date]` Safe default taken: not relaunched, never a retry.
5. **The builder's ASK DESK items 2–4** (actor `you` on a trading-log CLOSED row; `at` copied on a correction and held count; `_rewrite_fill_cache` as built) were answered by the desk as TAKEN; item 4 is judged under L3 by this check (ESCALATE 2). The three weak-assertion lists (Opus 5, Grok 3) are facts under `## Checked against the branch`; each HOLDS as stated.
6. **Round 1 of ≤3 (L39) of S3 C2: Opus 5.5 (Fable seat, R109) · Astra · Grok (L67, R95). A HOLD → a fix round classified first (L75). `ready for C3: YES` → `24-s3-exits-c3-build.md` stacks on `77cf18fd`.** Stop line below: `ready for C3: NO` only because three claims HOLD (Opus said YES with its exceptions, Grok YES).

S3 EXITS C2 CHECK DONE · round: 1 · opus: CHECK S3 C2: BUILD STANDS EXCEPT (4) sheet/CLI CLOSE at running>0, (6) second fill-cache writer (L3), (1) pre-C1 CLOSED correction refused · ready for C3: YES · astra: METER · grok: CHECK S3 C2: BUILD STANDS · ready for C3: YES · houses that checked: 2 of 3 · defects that HOLD: 3 · ready for C3: NO · ESCALATE: 6
