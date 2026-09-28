# S3 EXITS — BUILD + CHECK PROMPTS DRAFTED (2026-09-28)

Drafter `s3-exits-build-draft-0928` (Opus 5.5), prompt `prompts/2026-09-28/07-draft-s3-exits-build.md`, launch row `cto-2026-09-28.md` R28. Writing rules: `topics/writing-rules.md`.

## §0
- 4 chunks, 8 prompts (`prompts/2026-09-28/20`–`27`): C1 legs + one fill transaction (M1 `0021`) → C2 exits / running / corrections / held count / CLOSED / realized R / FILLED stop edit → C3 panel → C4 trade note. Strictly sequential: each stacks on the previous CHECKED tip. C5 (DM) HELD on O8; C6 folded.
- All four builds are with-DB: each waits for the `cobalt_dev` lock the F14 chain holds (L76). The four checks touch no DB and run beside any F14 build.
- NEW rule strings: 8 (a `.env` cp / rm pair per worktree). Check lines: 0 new.
- Hours: 27 builder seat-h (C1 8 · C2 7 · C3 7 · C4 5) + 4 checks ≈ 1 h each; ≈ 38 h with one fix round each (v3's 0.4× pattern, unmeasured).
- 7 seams with the DRC stack, each settled by the S3 build that lands first (C1 for 5, C2 for 1, C4 for 1); `## SEAMS`.

## CHUNKS
| chunk | feature | prompts | files | migration | WITH-DB | depends on |
|---|---|---|---|---|---|---|
| C1 | F11: `legs` + view, `card_stop_edits.kind`, `trade_note_path`, drift columns; `SizingResult.from_card`; ONE fill transaction; drift P setting | `20` build · `21` check | `db_migrations/0021_legs{,.rollback}.sql`, `__init__.py`, `placement.py`, `cards/legs.py` (new), `cards/store.py`, `cards/cli.py`, `aset/store.py`, `aset/engine.py`, `aset/web.py` (`/fill`, `/card/{id}/move` bodies), `settings/fills.py` (new) | **`0021`** — the next free after `main` (ends `0017`; `0012` on `bars/chunk-2-0920`) and `drc/d1-trading-log` (`0016`, `0018`; `0019` D2 fix, `0020` D3 claimed) | yes (forward to `0021` and rollback to `0013`, F2 = F0) | `main` at launch (`1ba082e9` when drafted); the lock |
| C2 | F11: running (one read), exit legs + stale-tap refusal, corrections, held count (R67), CLOSED at 0, `realized_r.1`, the FILLED stop edit (live defect), `cobalt cards legs` | `22` · `23` | `cards/legs.py`, `cards/store.py`, `cards/cli.py`, `aset/engine.py` (if needed) | none | yes | C1 CHECKED; the lock |
| C3 | F11 + S3-P2 stop half: panel routes + TRIGGERED / IN-TRADE render, held field, corrections, stop YOURS / Cobalt / ↺ | `24` · `25` | `aset/web.py` (one block after `/radar/card/{id}/release`), `aset/radar_panel.py`, sheet render | none | yes | C2 CHECKED; the lock |
| C4 | F22: one note writer (card row), note at the fill after commit, `trade_note_path`, `cobalt-legs` units, retry CLI | `26` · `27` | `prefill/trade_note.py`, `aset/web.py` (fill + C3 route bodies), `aset/store.py`, `cards/cli.py` | none | yes | C3 CHECKED; the lock |
| C5 | F11 DM line: `com.cobalt.dmlisten`, `dm_inbound` (M2 = `0022`) | NOT DRAFTED | — | `0022` if drafted | yes | **O8 = A (his)**; C2 |
| C6 | smoke, DevDocs, ADR | FOLDED | DevDocs ride in each chunk's last row; the S3 smoke is the ladder's S3-P3 line; the ADR is docs-only (desk lane) | — | no | — |

Cut: v3 §10's C1–C4 as drawn. C2 gains R67's held count (+≈1 h). C3 → C4 sequential (O17 A: C4 adds its note calls inside C3's routes, after their DB call). Worktree per chunk `~/cobalt-wt/s3-exits-c<n>`, branch `s3/exits-c<n>`; C1 cut from `main`, C2–C4 from the previous chunk's checked tip (they cannot build off `main` — each calls the one before). Checks: Sonnet 5 hub, Opus 5.5 (Fable seat, R109) · Astra · Grok (L67 new build; R95 / R97), no packet (R40 → R42 shape of `02-shrink-tribunal.md`): one `CHECK-INSTRUCTIONS.md`, originals read by Opus / Astra, copies for Grok only, the build diff as the one staged command output.

## SEAMS
Every file or table S3 shares with the DRC stack (`drc/d1-trading-log`, tip `10163d51`) or `main`, and the build that settles it first (K3). The texts live in `20` `## THE SEAMS` (S-LEGS, S-HELD, S-FILL, S-WEB, S-MIG), `22` (S-C2) and `26` (S-NOTE). This section is offered as the L72 document both lanes cite; the desk settles it before C1 or DRC D5 launches.
| seam | shared with | what | settled first by |
|---|---|---|---|
| S-LEGS | DRC D3 (`drc-trades/reconcile` reads `legs_current_v`), DRC D5 (writes through C2) | v3 §3 DDL as R67 rules it (N): `running_before`, no `running_after` / `direction`; plus DRC v2 §96 S-C1 (`source` and `price_source` gain `trading_log` — L31's rename of `das`; nullable `source_import_id`, NO FK, CHECK paired with `trading_log`); plus `held_stated` (S-HELD) | C1 (`0021`) |
| S-C2 | DRC D5 (`drc/reconcile.py`) | C2's `record_exit` / `record_correction` are the ONLY leg writers; `trading_log` rows need `source_import_id`; append-only; running may stay > 0 across days; CLOSED only at 0; refusals raised by name (R90: DRC resolves, never forced) | C2 |
| S-FILL | DRC D3 card match (`AsetStore.for_date`, v2 `[F-19]` snapshot columns) | `mark_filled` is the one fill; `for_date`'s SELECT list and column meanings unchanged (append only, named) | C1 |
| S-NOTE | DRC D3 (retires `find_trade_note_for_card` from the DRC path) | `aset_sizings.trade_note_path` = the fill note's path, NULL = missing; C4 never edits `prefill/drc.py` or `prefill/daily.py` | C4 (column by C1) |
| S-WEB | DRC D4 (block after `/attest`), DRC D2 (block at END of `aset/web.py`) | S3 edits existing S3 route bodies; new S3 routes contiguous directly after `/radar/card/{card_id}/release` | C1 (C3 adds the block) |
| S-MIG | DRC `0016`–`0020` in `db_migrations/__init__.py` FORWARD / REVERSE and `placement.py` | `0021` last in FORWARD, first in REVERSE; the stacked gate orders the lists at merge (L68) | C1 |
| S-SETTINGS | DRC D4 (`settings/models.py`, `SETTING_KEYS`, `settings/drc.py`) | C1 reads `fills.drift_warning_pct` through a NEW `settings/fills.py`; `models.py` untouched; X-S tests whether `cobalt settings load` accepts the key without a `models.py` edit | C1 (X-S) |
| S-HELD | S3-internal (C1 column, C2 writer); DRC D5 reads held rows as history | "holding X" = an entry-leg correction with `held_stated = X`, `shares = X + Σ current exits` | C1 / C2 |

## RULINGS USED
Found by `grep -n -F "EXITS"` on `cto-2026-09-21.md`, `-22`, `-23`, `-24`, `-25`, `-27`, `-28` (`-26` does not exist; `-23`, `-24`, `-25`, `-27` have no hit), `grep -n -F "stop-override"` on the same set plus `cto-2026-09-20.md` and the ladder, and `grep -n -i -F "S3 exits"` on `-22`.
- `cto-2026-09-22.md` **R67** (15:48) — R2-2 = the Fable seat's N + his four additions (held count wins; partial exit = his shares + price; the trading-log import reconciles as correction rows naming the source; open position carries). Governs S-LEGS, S-HELD, S-C2, C2, C3.
- `cto-2026-09-20.md` **R38** (18:38, "B with your addition") — the stop override. Governs `card_stop_edits.kind` (C1), C2-6, C3's stop render. Ladder `SPRINT-LADDER-v0_1.md:517`, `:593` carry it.
- `cto-2026-09-22.md` **R62** (round 2 on the three items) · **R13** (Astra reads the FINAL) · **R36** / **R109** (every Anthropic seat on `claude-opus-5-5`).
- `cto-2026-09-22.md` **R90** (DRC O20: a CLOSED card the export shows open stays open with a RESOLVE line) — why S-C2 refuses, never forces.
- `cto-2026-09-23.md` **R95** / **R97** — new-build checkers Opus (Fable seat) · Astra · Grok; no Gemini on code.
- `cto-2026-09-24.md` **R17** / **R19** — the house strings standing; **R22** — the `.env` pair shape this report re-paths.
- `cto-2026-09-25.md` **R74** — his approval of `48`'s strings (the four `COBALT_ENV=dev uv run cobalt db …` strings reused).
- `cto-2026-09-28.md` **R26** (development continues) · **R28** (this launch) · **R29** (Astra's read, parallel).
- `cto-2026-09-21.md` **R57** and the 09-21 / 09-22 launch rows (R34, R35, R63): context only; no build rule taken from them.
- Ladder `SPRINT-LADDER-v0_1.md` S3 section (`:639`–`:658`): F11 / F22 acceptance and "S3-P1 / S3-P2 · Opus 5 · fresh".
- Owner items O1–O22 (v3 §12): UNRULED — no row in `cto-2026-09-2[2-8].md` rules one. Every build takes the default its prompt names; `## ESCALATE` 3.

## ASTRA-SENSITIVE
Every `[R2F-nn]` item a chunk rests on (v3 carries `ASTRA PENDING (R13)` on each). An Astra DOES-NOT-HOLD on an item re-issues the named prompt rows only. R2-2's items (R2F-04, -07, -18–-21) are also ruled by his R67: Astra's objection there is recorded, never a reopening (L77).
| item | what | chunk | prompt line |
|---|---|---|---|
| R2F-01 | one fill transaction (R2-1 converged) | C1 | `20:36` (C1-4) |
| R2F-03 | `autocommit = False` on the fill connection | C1, C2 | `20:36`; `22:30`, `22:34` |
| R2F-04 | R2-2: running column, index, current-row view, `direction` source | C1, C2 | `20:24` (S-LEGS); `22:29`–`22:32` |
| R2F-07 | the FILLED stop-edit share read | C2 | `22:34` (C2-6) |
| R2F-09, -10, -11 | M1 = one `db_migrations` file + `.rollback.sql`, carrying `card_stop_edits.kind` | C1 | `20:28` (S-MIG), `20:33` (C1-1) |
| R2F-12, -13, -15, -16 | X20–X22 added; X4 / X7 merged | C1, C2 | X22 `20:98`; X4 `20:99`; X21 `22:63`; X7 `22:69` |
| R2F-14 | per-share risk from the planned entry (X20) | C2 | `22:34`, `22:64` |
| R2F-17 | O16: `fills` kept declared | C1 | `20:24` |
| R2F-18 | O21: pre-C1 card's share count | C2 | `22:29` |
| R2F-19 | O22: a correction to 0 closes | C2 | `22:31`, `22:32` |
| R2F-20 | the concurrent-tap expectation | C2 | `22:69` |
| R2F-21 | Q3 → R2-2 | C1 | `20:24` |
| R2F-02, R2F-22 | dissent records | none | — |
R2F-05, -06, -08 appear in the derive's fold table only, not in v3's text; not read, no chunk cites them.

## NEW strings
8, each on one build line only; his approval word for the pair goes on that build's launch row:
- `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s3-exits-c1/.env)` · `Bash(rm /Users/cobalt/cobalt-wt/s3-exits-c1/.env)` — `20`
- `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s3-exits-c2/.env)` · `Bash(rm /Users/cobalt/cobalt-wt/s3-exits-c2/.env)` — `22`
- `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s3-exits-c3/.env)` · `Bash(rm /Users/cobalt/cobalt-wt/s3-exits-c3/.env)` — `24`
- `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s3-exits-c4/.env)` · `Bash(rm /Users/cobalt/cobalt-wt/s3-exits-c4/.env)` — `26`
Reused, not new: the 18 non-`.env` strings of `prompts/2026-09-25/07-drc-d2-build.md` line 1; the four `COBALT_ENV=dev uv run cobalt db …` strings of `prompts/2026-09-27/48-stack-seam-fix-r2-build.md` line 5 (R74); on the check lines, the seven read-only strings (09-20 R13) + the three standing house strings (L62, R17 / R19).
Desk's `worktree add` (step (0) of each build) is the desk's own command, on no builder line.

## ESCALATE
1. **S-HELD is the drafter's cut of R67 (1)** — v3 has no row form for "I'm holding X". Taken: an entry-leg correction carrying `held_stated` (C1 column, C2 writer). The desk confirms before `20` launches (C1 carries the column). Safe default: built as written.
2. **S-LEGS widens v3 §3's DDL** by DRC v2 §96's S-C1 (`trading_log` on `source` / `price_source`, `source_import_id` without FK) and by `held_stated`. The desk records `## SEAMS` as the L72 document before C1 or DRC D5 launches; DRC D5's prompt cites the same text.
3. **Owner items O1–O22 unruled.** Defaults taken, each named in its prompt: O1 A · O3 A · O4 A · O7 A · O11 A · O14 A · O15 A · O16 A · O17 A · O18 A · O19 A · O20 A · O21 A · O22 A. **O5 / O6: v3 §7 creates his keys blank; the derive's `## FOR DEJAN` calls "Cobalt fills while blank" the A default** — contradiction; C4 takes blank (writes nothing of his). **O2**: P and the comparator are his; C1 takes the Charter's `>` and no value.
4. **O8 → C5 NOT DRAFTED.** The DM listener (new resident, plist, heartbeat probe, M2 `0022`, the bot credential's first read) waits on his O8. If A, a C5 build + check are drafted then (new strings: the resident's proofs).
5. **C6 folded**: DevDocs in each chunk; the S3 smoke is S3-P3's; the F11 / F22 ADR is docs-only and unassigned.
6. **Eight new strings vs two.** The drafting prompt names a worktree per chunk; one stacked worktree `s3-exits` would need one pair. Taken: per chunk, C2–C4 cut from the prior checked tip (the prompt's "branched from main" read as C1's base).
7. **`cobalt_dev` at `0013` assumed** (`48`'s F2 = F0 on 09-27). Each build's W (b) fails loud at any other level; the desk then re-issues the `--down-to` token (a new string).
8. **X-S (C1)**: `fills.drift_warning_pct` may need a `settings/models.py` edit to load — a seam with DRC D4; the desk settles which lands first if X-S is `design-changing: yes`.
9. **The check line carries grok + Astra + Opus together** for the first time; each string is standing (L62, R17 / R19). Zero new by rule; the desk may show him the combination once.
10. **The CLI fill is refused** (`cobalt cards move <id> FILLED`), not routed through `mark_filled` — v3 allows either; refusal needs no `cli` source value.
11. **Critical path**: C1 → check → C2 → check → C3 → check → C4 → check, each build behind the F14 chain's lock. S3 stops 2026-10-07; ≈ 38 h of seats before a deploy.
12. **Carried for the builds, UNPROVEN (L70)**: X5 (TRIGGERED past `expires_at` may not expire — C3 records, does not fix; the ladder's "EXPIRED timer"); X-UR (`used_risk` stale after an exit — C2 lists, C3 renders only what it allows); X-OPEN (a FILLED card across a session boundary).
13. **Astra's read (R29) runs in parallel**; a DOES-NOT-HOLD maps through `## ASTRA-SENSITIVE` to prompt rows.
14. **L74**: a block inside a tool result asked for a `Claude-Session:` line in commits and named a file-send tool; recorded once here; this seat committed nothing and did not follow it.

## EVIDENCE
- 08:46 `grep -n -F "| R28 |" …/cto-2026-09-28.md` → line 36, the R28 row naming `07-draft-s3-exits-build.md`; `git -C /Users/cobalt/cobalt log --oneline -3 -- …/cto-2026-09-28.md` → `e77b08a1 docs(desk): 09-28 R27–R29 …` on main.
- 08:50 `git -C /Users/cobalt/cobalt log --oneline -1 main` → `1ba082e9`. `ls src/cobalt/db_migrations/` on main → highest `0017`. `git log --all --diff-filter=A` on `db_migrations/` → `0012` (`02d67a6e`), `0016` (`d583f6fd`), `0018` (`9a0fc900`); `0019` / `0020` claimed by the DRC prompts (ladder `:691`).
- Code read on main: `cards/store.py:429` `fill` (own connection, `:494` autocommit False), `:643` `record_stop_edit` (autocommit connection, `:720` `in_trade_shares=shares`, `:730` writes `shares`); `aset/store.py:185` `mark_filled` (second connection `:230`); `aset/engine.py:43` `FILL_DISTANCE_WARNING_PCT = 25`; `db.py:199` `autocommit=True`; `aset/web.py:1057` `/fill`, `:1192` `/card/{card_id}/move`, `:1394` `/radar/card/{card_id}/release`; `cards/cli.py:83` `store.fill(`. v3 §1's facts hold on `1ba082e9`.
- DRC branch vs main, S3's files: `git diff --stat main...drc/d1-trading-log` → `aset/web.py`, `aset/drc_page.py`, `cli.py`, `db_migrations/{0016,0018,__init__,placement}`, `prefill/daily.py`, `vaultwrite/writer.py`, `settings/{card,cli,drc,models}.py`.
- Prompt sizes (`wc -c`, 09:03): `20` 31,263 · `21` 18,796 · `22` 19,856 · `23` 9,276 · `24` 16,853 · `25` 8,216 · `26` 16,768 · `27` 8,337.

## CONTINUE
Done. Next is the desk's: settle `## SEAMS` (L72) and ESCALATE 1–2; bring him the 8 new strings as ONE list; launch `20` when the lock is free.

S3 EXITS BUILD PROMPTS DRAFTED · chunks: 4 · prompts: 8 · with-DB chunks: 4 · seams with DRC: 7 · new rule strings: 8 · ESCALATE: 14
