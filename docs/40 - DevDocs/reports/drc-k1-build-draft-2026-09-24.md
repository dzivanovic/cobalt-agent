# DRC K1 build draft — 2026-09-24

Seat `drc-k1-build-draft-0924` (Opus 5.5), from `prompts/2026-09-24/38-draft-drc-k1-build.md`. Authorization: `cto-2026-09-24.md` R61 (`:72`, names `38`) and R51 / R52 (`:62`, `:63`) printed. Times from `date` (16:03–16:10 ET).

## §0 Headline
- WROTE `prompts/2026-09-24/39-drc-k1-build.md` (K1 build, 54,585 B) and `prompts/2026-09-24/40-drc-k1-check.md` (new-build check round 1, 32,035 B).
- K1 builds on `drc/d1-trading-log` at `38a70947` in `drc-d1`, with migration `0018_drc_stated_books`. X1–X6 run first (gate on built code, then pass on K1). The `[F-17]` contract is stated verbatim for D2.
- The two launch lines equal `14` / `15` byte for byte except path and remote-control (a `diff` after normalising them: identical). New strings: 0. Owner items: 0.
- ESCALATE: 9 (desk readings and drafter pins; none blocks launch).

## L74
A `Claude-Session:` commit-attribution line arrived in this session's system reminders. This seat made no commit (NO git write), so it was never used. Recorded once.

## DECISIONS
| # | Decision | Source |
|---|---|---|
| 1 | **Branch:** K1 continues `drc/d1-trading-log` in `/Users/cobalt/cobalt-wt/drc-d1` at tip `38a70947` (code `d1342595`). No new worktree, so no desk `worktree add` line. v3 §6's "D1 merged" (`:247` Depends on) is the DEPLOY order, not a branch rule; `:254` makes K1 + K2 land with D2 + D3. One branch carries the DRC stack. | `git -C ~/cobalt log -1 --format=%h drc/d1-trading-log` = `38a70947`; v3 `:247`, `:254`, `:256`; L46 SCOPE; L68 |
| 2 | **Migration `0018_drc_stated_books`**, a NEW file. `0016` is never edited: X5 runs, and either result keeps the new file, which is `[F-02]`'s default. | `## MIGRATION NUMBER`; v3 `:196`, `:316`, `:344` |
| 3 | **Scope** = v3 §6 row K1 (`:247`) + `[F-10]`'s CLI (`:256`) + R52's `cli` literal and dry-run / `--apply --sha256` shape (side B of R2-2(c), v3 `:158`) + R51's history (append-only `drc_stated_books`; `seed_for` FAILS loud on stated-vs-recorded until K2 builds R51's rebuild). **[F-04] is included:** X3 gates K1, and K1's `seed_for` turns a stated book (cost / time may be null) into a seed. NOT built: K2 (empty-day record, forward re-pair, RESOLVE's effect), K3 (unit, `/drc`), K4 (widget). B8's pin test is replaced by "a first import without a stated book does not pair" (v3 `:118`). `FN_VERSION` → `drc.pairing/2` (v3 `:163`). | v3 `:118`, `:163`, `:192`, `:247`, `:256`, `:314`; R51; R52; `39` "THE K1 CONTRACT" C1–C7 |
| 4 | **Seam `[F-17]`:** stated as a CONTRACT in `39` `## SEAM FOR D2`, written verbatim into the build report. It gives the call order `seed_for` → `build_day(seed=…)` → `record_day(…, seed)`, `seed_for`'s raises, the `None` = not-stated path, the in-store `market_reset` refusal, and `pair_day` holding no policy. D3's `cobalt drc build` joins K1's `drc` parser group. No D2 / D3 file is touched (39 S6 asserts it). | v3 `:258`; L72 P-b |
| 5 | **Experiments X1–X6 run FIRST (S2), each with v3's words quoted.** Each X gets a GATE test on built code: X1 trade_id through a jsonb round trip; X4 three-way hash (in-memory / jsonb / second process); X5 edited-`0016` insert; X6 `assert_writable` at a constructed 20:15 ET clock. It also gets a PASS test of v3's condition against K1, red before the code and green at S8 / S9. X2 and X3 have no gate that can run on built code: their conditions are K1's own behaviour, so the gate records the as-built lines and the pass runs post-code (ESCALATE 5). A failing gate → `FAILED: X<n> — <v3's words>`, and the build stops. | v3 `:308-317`; L70 |
| 6 | **Check seats:** a NEW BUILD → Fable-seat as Opus 5.5 (09-22 R109) + Grok. Astra is METER until Sep 26th, 2026 6:47 AM and not on `15`'s line, so the desk seats it on its return. NO Sol (new build), NO Gemini (09-23 R97). Fail closed below TWO. | L67 as amended 2026-09-24; v3 `:10`; `15` line |

## MIGRATION NUMBER
Read with `git -C /Users/cobalt/cobalt ls-tree --name-only <branch> src/cobalt/db_migrations/` over EVERY local branch (37, `git branch | wc -l`), plus the two prompts:
| Branch / source | Highest number |
|---|---|
| `main`, `cards/stale-score-0922`, `deploy/stacked-0923`, `setups/seven-0921` | `0013_tunables_slug_nullable` |
| `bars/chunk-2-0920` | `0012_bars_partitioned_parent` |
| `radar/handicap-h1-0922` | `0011` on the branch; `0014_radar_handicap` claimed by `prompts/2026-09-23/47-handicap-h1-build.md:76`, `:96` |
| `cards/stale-score-0922` (conditional) | `0015_shadow_agreement_stale` claimed by `prompts/2026-09-23/46-stale-score-build.md:20`, `:80` (X30 (A) only) |
| `drc/d1-trading-log` | `0016_drc` |
| `voice/v1-0923` | `0017_voice_turns` |
| every other branch (ops/*, s2/*, sprint-2/*, archiver, heartbeat, jev, replay, bars chunk-1a / e) | ≤ `0011` |
| `0018` anywhere | no branch holds a `0018*` file. `prompts/2026-09-24/41-reissue-devdb-builds-r2.md` (R62) pins "K1's `0018` untouched". |
**Pinned: `0018`.** `39` S0 re-proves it with `git -C /Users/cobalt/cobalt log --all --oneline -- "src/cobalt/db_migrations/0018*"` EMPTY. The desk renumbers at the L68 gate if a sibling changes.

## SEAM
`[F-17]` as `39` states it (verbatim for D2's drafter; the build fills `file:line`): (1) `DrcStore().seed_for(D)` → `Optional[SeedBook]`. It raises `PairingError` on a broken chain, an uncomputed prior, a pre-lane prior (`rebuild <P>`), a hash mismatch, a stated-vs-recorded conflict (R51, K2) and a stored unapplied resolve (K2), never caught into a flat book. (2) `None` → `build_day(trading, stats, seed=None)` → `not computed — opening book not stated`, and the page asks for the book (K3; the CLI until then, R52). (3) Otherwise `build_day(…, seed=book.positions)` then `record_day(pairing, import_ids, book)` (seed REQUIRED). (4) Every statement goes through `record_stated_book(day, kind, positions, via=…, now=…)`, which refuses inside `market_reset` itself. (5) `pair_day` holds no book policy; a route never calls it directly. (6) D3's `cobalt drc build` joins K1's `drc` group.

## OWNER ITEMS
NONE. v3 §8 (`:278`) and R51 / R52 settle the lane. Every open shape `39` pins is a design question for `40`'s houses (ESCALATE 2), not his.

## FOR DEJAN
New rule strings: **0**. Both launch lines are their precedents byte for byte. The `drc-d1` `.env` pair is his R22 (`cto-2026-09-24.md:33`, "approved"); its reading for `39` is the desk's (ESCALATE 1).

## ESCALATE
1. **R22 scope — desk reading, not his words.** R22 approves the `.env` pair "the launch line of `14`". `39` uses it on the desk's R61 reading ("the `drc-d1` `.env` pair is his R22"). `39`'s gate records `R22 scope: read as the drc-d1 pair for this worktree (desk reading, R61)`. If the desk wants his word, it is one line on his list.
2. **Drafter pins where v3 names no shape (for `40`'s houses to rule, carried in `39` CLOSE):**
   - stated `trade_id` = `<symbol>-<direction>-stated-<day>`;
   - a stated position's `opened_on` = the stated day, so a later "days held" undercounts a swing opened before the chain;
   - the hash encoding: `json.dumps(sort_keys=True, separators=(",", ":"), ensure_ascii=False)` over `model_dump(mode="json")` sorted by `trade_id`, proven by X4;
   - `reason` derived by the store, not the caller (L3);
   - `seed_for` FAILS loud on (a) a stated opening beside a recorded prior close (R51 is K2's) and (b) a stored unapplied `resolve` (`[F-06]` is K2's), instead of silently ignoring his statement.
3. **`book_sha256` binds positions only** (v3 `:135`). Every flat `opening` and every `no_trade` row hashes to `sha256(b"[]")`, so R52's `--apply --sha256` binds the positions, not the day or kind. The printed row (day, kind, reason) must ride in the approval message (R52 / R47 ESC 2). Built as ruled; recorded in `39` CLOSE and `40`'s packet. A hash over the whole row would be his amendment of R52.
4. **Mode:** `39` copies `14`'s `acceptEdits` as `38` directs. L63's state note keeps it INTERIM PRACTICE for a write path, and any unlisted Bash is a dialog = FAILED. So the CLI is proven through pytest only (`uv run cobalt drc …` is not on the line), and X4's second process is spawned inside a test.
5. **X2 / X3 "run first":** their v3 conditions are K1's own behaviour (the not-computed first import; a null-cost stated seed). Before the code, only the as-built lines can be recorded (`test_drc_pairing.py:265-272`; `models.py:98`, `:110`) and the PASS tests red as absent. The stop line's `X: 6 of 6 run` counts the gate plus the post-code pass. That is this seat's reading of L70 for a chunk-internal experiment.
6. **L68 seams the gate will meet:**
   - K1 must re-pin `REVERSE` in `test_p4_migrations.py`, `test_radar_migration.py`, `test_archiver_migrations.py`, `test_radar_score_migration.py` and `test_tenancy.py`, or offline goes red. Those files are also touched by `setups/seven-0921` / `deploy/stacked-0923` / H1 / stale-score.
   - K1 adds one import and one `add_parser` line to `src/cobalt/cli.py`.
   - Both are named in `39` S5 / S6.
7. **L76 stagger:** `39` takes the `cobalt_dev` lock THREE times (S2, S4, S9). Its DESK LINE bars a launch while `36`, `42` / `43` or a deploy gate holds the lane. R61 says `36` or `39` goes first, never both with-DB. METER ≈ 90–120 min, longer than `14`.
8. **`cobalt_dev` head:** `39` S2 proves `cobalt_dev` at production's head with the `migrate_proof` probe (`assert 28 == 31`, `14`'s D7). S9 expects `28 == 32`, short by 4 with `drc_stated_books`. A different shape is recorded and escalated, not fatal. If `36` / `43` leave a table behind, the counts move.
9. **Astra:** `40` carries `15`'s line byte for byte, which has no Astra string. On Astra's return (Sep 26th, 2026 6:47 AM) the desk seats it in its own launch. Until then K1's check stands at two houses under L67's shrink-to-two clause, and `40`'s standing line says so.

DRC K1 BUILD DRAFTED · branch: drc/d1-trading-log · migration: 0018 · experiments: 6 · prompts: 2 · new rule strings: 0 · owner items: 0 · ESCALATE: 9
