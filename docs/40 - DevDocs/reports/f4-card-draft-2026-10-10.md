# F4 card draft — 2026-10-10

## §0 Headline
- Card: `docs/40 - DevDocs/prompts/2026-10-10/304-f4-refresh-card.md`, JOB `f4-refresh-1010`, BASE `d78c66a2`, 15 rows (A1, C1, C2, M1, W1, O1, O2, S1, D1, G1, E1, U1, K1, R1, DOC; T1-T17 each on a row).
- Every FINAL cite re-proved at `d78c66a2`; 10 cites moved or did not hold, and the card uses the real lines (`## RECORDS`).
- Header `DB` is left out: the job needs `cobalt_dev` (D1).
- The build seat cannot run 5 writer-gate items; the plist bootstrap waits on them (D2).
- X16's hand-typed-table leg reads red from the code today (D4).

## DECISIONS
- D1 ASK DESK: the prompt says `DB: none`. CARD.md allows `none` only when every file sits under `ops/`, `tests/ops/` or `docs/`; with it, BUILD-HUB skips every with-DB step (`BUILD-HUB.md:39`). F4 changes `src/` and needs `cobalt_dev` for T1-T4, T7-T9, T11. The FINAL's `none` is its migration column; its `cobalt_dev` column says yes. Default: the key is left out (precedent `126-stt-model-fix-card.md` RECORDS). [18:58]
- D2 ASK DESK: X1-X16 must have results before the writer loads. The build cannot run X7's Obsidian render, X8 (live per-minute counts, 21 firings), X9 (launchd, Sync, a timed aset bounce), X10's real-note `--dry-run` or X15 (live transport). `cobalt jobs restarts` will print `new one-shot, bootstrap once: com.cobalt.prefill-refresh` (`restarts.py:198-206`). Default: the deploy ships the code and the plist file, and the bootstrap is held. The desk runs those five on the Mac after the deploy and bootstraps only when they pass. [18:58]
- D3 ASK DESK: RULINGS is `2026-10-10 R849, 2026-10-10 R969`, as the prompt set it. R931 (counted in the gate, L53) and R771 (form B) bind rows G1 and E1 too. Default: kept as written; R931 and R771 are cited in the rows through the FINAL. [18:58]
- D4 ASK DESK: X16's leg "a stub with a hand-typed `### Trading` table, bytes unchanged" reads red from the code. The absent-section arm wraps the located span as `seed` and runs `merge3(seed, seed, cobalt_lines)` (`writer.py:735`); base == human there, so Cobalt's body wins (`merge.py:15`). FINAL X16 says that result goes to him with the card, since there is no round 4. T17 (§4.6) has the same rule. Default: A1 (3) runs it on BASE first and quotes it. E1 builds [F-35] as folded, and a red X16 or T17 leg is reported, not fixed. The writer stays unloaded until he rules (D2). [18:58]

## RECORDS
- Prompt read: `prompts/2026-10-10/303-draft-f4-build.md`; `prompts/CARD.md`; `docs/30 - Design/F4-FINAL-2026-10-10.md` whole (321 lines); `areas/cobalt.md` `## What Cobalt is` and `## Build rules` down; `topics/writing-rules.md`; `BUILD-HUB.md` (grep: `:3`, `:17` test vaults `tmp_path` only; `:39` DB none); `ops/desk/gate-lists.md:1-46`.
- BASE: `git -C /Users/cobalt/cobalt log -1 --format="%H %cd" main` → `d78c66a274f2cd61cdab224c311024f1080db6a4 Sat Oct 10 18:54:43 2026 -0400`. `git status --short -- src configs ops tests` printed nothing, so the reads of the working tree equal HEAD. `git diff --stat d0a5fbb8 HEAD -- src configs ops tests` touches no F4 path.
- Cite proof (Explore agent, read-only, `grep -n` and line reads at `d78c66a2`, 18:57): 106 HOLD. MOVES: `daily.py:479`, `:574-577` (→ `:575-577`), `jobs/config.py:63-117` (`calendar_entries` `:198`), `radar/notes.py:357-362` (→ `:357-363`), `aset/web.py:35` (→ `:35-37`), `gate-lists.md:1-10` (→ `:5-8`). DO NOT HOLD: `prefill/config.py:37-48`, `rules_gen.py:156-158` (write at `:111-125`), `rules_gen.py:365-396` (→ `:128-159`), `store.py:91-98` (not stub-specific), `daymode/note.py:192` (stage at `:163`). Located: `SYNC_REVERT_WINDOW = 10` `writer.py:844`, `recent_afters` `store.py:111`, `overrides_for` `store.py:232`, `def merge3` `merge.py:100`, `PREFILL_CONFIG_PATH` `config.py:29`, the T14 test `test_finviz_consumers.py:65`, `radar.finviz_max_rpm` `tunables.yaml:702`, `seat_usage.*` `:1033`, `:1051`. No `prefill.refresh_` key, no `test_prefill_refresh.py`, no refresh plist. Highest migration `0024_strike_alerts.sql`.
- Drafter's own reads at `d78c66a2`: `daily.py:10-26` (stub-upgrade branch already DELETED), `:476-483`; `rules_gen.py:128-159`; `writer.py:181-211`, `:720-742`; `restarts.py:196-206`; `tests/cobalt/test_vaultwrite.py:30-99` (`dev_db_tx` at `:54`; its `dev_dir` writes the dev vault, so the card takes `tmp_path`).
- `vault_writes` level: `src/cobalt/db_migrations/0002_move_tables.sql:50` (≤ `0013`), so no gate-lists edit is needed.
- Precedent: `grep -l vault|plist` on `prompts/2026-10-0*/*card*.md` and `2026-10-10`. No card holds both a vault write path and a plist. The shape is taken from `2026-10-04/01-drc-k3-card.md`, with the RESTARTS paragraph of `2026-10-06/72-s4-p1-card.md`.
- LADDER: `areas/cobalt-sprints.md` has no S5 lane A line (`S5` hits only `:17`, `:42`), so the card uses `OFF-LADDER — reports/cto-2026-10-10.md R849`.
- The FINAL names two different tests T16 (the Opus seat's stamp edit, Grok's non-pipe line). The card splits them into T16a and T16b.
- No commit (no git write on this seat). The desk commits the card on `main` before launch.

F4 CARD DRAFTED · decisions: 4
