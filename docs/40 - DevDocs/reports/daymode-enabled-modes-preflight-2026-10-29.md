# Preflight — card 1081 (daymode enabled_modes, K3) — 2026-10-29

Seat: Sonnet 5.5, read-only. Clock from `date`: Thu Oct 29 19:04 ET. No shasum available to this seat (not on its allow list), so the four sha256 are the desk's pre-launch check.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | Read card + `CARD.md` "A PRODWRITE CARD" | Header has JOB, LADDER, CLASS K3, BRANCH main, WORKTREE none, BASE 1903c47f, REPORT, RULINGS, WRITE RULING. `grep -n "«FILL"` on the card: no hit. `git status --short` on card, CARD.md, PRODWRITE-HUB.md: clean | OK |
| 1b | `grep -n "^| R2563 " reports/cto-2026-10-29.md` | `:27 … HIS RULING · APPROVED ("enable everything I need to use. I want all enabled") … APPROVED — pending fold`. WRITE RULING and RULINGS cite `2026-10-29 R2563` | OK |
| 1c | `git diff --stat 1903c47f HEAD -- . ':(exclude)docs'`; `ls` of the REPORT path | prints nothing (no code past BASE); the report file is absent | OK |
| 2a | Read `## ROWS` | exactly ONE data row (P1), 7 cells; command is `COBALT_ENV=production uv run cobalt settings load --from …/forward --apply`; none of `" ' \ $` backtick `\| & ; < > * ? % #`; verb `settings`; table `user.trader_settings` | OK |
| 2b | backup cell | exactly `COBALT_ENV=production uv run cobalt backup run` | OK |
| 2c | count read vs `bare-guard.py:992-1018` `PROD_READ`/`prod_read` | opens `COBALT_ENV=production uv run cobalt db query`, one `--prod`, `--side user`; guard checks words and flags, not SQL; has no `%`/`$`/backtick; names the table as the literal `'user.trader_settings'`. The read-back (RECORDS step 5) is stated as the READ-line query plus `updated_at`, same words, so `prod_read` admits it | OK |
| 3 | Read `forward/daymode.yaml` vs `rollback/daymode.yaml` | the only value that differs is line 6: `enabled_modes: [reduced, half, full]` vs `[reduced]` (header comments lines 1–2 differ; comments only). The other keys and the 7 stepdown rows are line-for-line equal | OK |
| 3b | Read `forward/aset.yaml` vs `rollback/aset.yaml` | line-for-line identical (all 21 lines). The comment "the --dry-run must print …" (lines 3–4) is stale, harmless | OK |
| 4a | `git show main:src/cobalt/settings/cli.py` | `:283–284` `source_label = f"yaml:{args.from_dir}"`, `rows = TraderSettings.rows_from_yaml(Path(args.from_dir))`; `:317` `apply_settings(rows, source=source_label, store=store)` with no `delete`; `:320` `print(f"\napplied: {outcome}")` | OK |
| 4b | `git show main:src/cobalt/settings/models.py` | `rows_from_yaml` `:349`; the returned dict (`:376–386`) has exactly the seven `SETTING_KEYS` (`:45`) | OK |
| 4c | `git show main:src/cobalt/settings/store.py` | `put` `:89–108`: unchanged key skipped (`:90–92`), upsert for others, `DELETE` only for keys in `delete` (`:105–108`); `apply_settings` passes `delete` only when non-empty (`cli.py:102–104`). `--from --apply` writes only the seven keys and deletes nothing | OK |
| 5 | count logic | production `daymode.enabled_modes` is `[reduced]`, forward is `[reduced, half, full]`, the other six are equal, so only that key gets `source = yaml:<forward dir>`: before 0, after 1. The forward set validates (`config.py:284–289`: ladder `reduced < half < full` from `aset.sheet_modes.order [half, full]`; `reduced_sheet half` is on it). Count-before, count-after, read-back and updated_at list are stated in RECORDS "SEAT STEPS" and "THE COUNT" | OK (see I1) |
| 6a | no dry run, no `--sha256` | the card has no dry-run step; `--sha256` with `--from` is refused (`cli.py:268–270`); the row has none | OK |
| 6b | seat guard `bare-guard.py:1099–1105` | the seat is admitted the card's one command, the two backup strings and `prod_read`; the P1 command is byte-for-byte what the card holds | OK |
| 6c | `## ROLLBACK` | the backup path from `backup run`, plus the second one-command card (the P1 inverse cell, `--from …/rollback --apply`), "READY and NOT RUN" | OK |
| 7 | `cli.py:88–100`; `session/guard.py:123–150` | `apply_settings` calls `assert_writable(actor, target=TARGET)` at `cli.py:100`; `assert_writable` raises `SessionBlocked` when the session is `market_reset` (20:00–21:00 ET). The card names it (NOT IN THIS JOB). The card names no launch window (see I3) | OK (see I3) |
| 8 | spot-check, 20 more cites on main/HEAD | OK: `config.py:156–158` (`modes`), `:178`, `:181–182`, `:265–271`, `:284–289`, `:309–326` (reads `TraderSettings.from_db()` every call); `propose.py:58–61` (clamp text); `card.py:231` ("no cache"), `:296–303` (omitted-key delete is the `--card` route); `drc.py:151–160`; `.gitignore:6` (`data/`); `models.py:33–48`; `cto-2026-10-08.md:39` (R686); `cto-2026-10-29.md:13` (R2581) and `:15` (R2577); `bare-guard.py:996–1018`. FAIL: `deploy-2026-09-19.md:145` (see I2). Not found: row R2580 (see I2) | 1 FAIL |

## OPEN FILLS
none. (Desk-owed items before launch: the four `shasum -a 256` equal the four in RECORDS; no other `prodwrite-` or `deploy-hub-` session live.)

## ISSUES
- I1 (does not block). RECORDS "SEAT STEPS" (5) asks the seat for a read-back and an `updated_at` list. `PRODWRITE-HUB.md` has no such step: its VERIFY is the count only and step (6) says "Nothing else is run"; `CARD.md` "WHAT A CARD NEVER HOLDS" bars a card from holding steps. The guard would admit the read, but a seat following the hub strictly can skip it. The count (before 0, after 1, with only the changed key taking the new source) already proves that one key moved. Fix: the desk runs the read-back itself after `WRITTEN` (it holds the R686 read), or the seat does it and the report records it.
- I2 (does not block). Two stale cites: RECORDS says `trade_count_over_band` was added per `deploy-2026-09-19.md:145`; the row is at `:62`, and `:145` is the L28 trace. And "ruled R2580": `cto-2026-10-29.md` has no row R2580 as a `| R2580 |` row; route (b) is recorded at R2581 (`:13`). Neither affects the write.
- I3 (does not block). Time window: the apply is refused 20:00–21:00 ET. The clock read 19:04 ET at this check. `backup run` can take up to 600 s, so launch needs to start well before 20:00; else launch after 21:00. The card does not state this.
- I4 (note). The four sha256 were not recomputed here (no `shasum` on this seat's allow list). I confirmed line-for-line equality of forward and rollback `aset.yaml` and the single differing value in `daymode.yaml` by reading all four files.

Blocks the launch: nothing, besides the desk's own pre-launch `shasum` check and the 20:00–21:00 ET window.

PREFLIGHT DONE · cards: 1081 · checks: 17 · fails: 1 · ready: YES
