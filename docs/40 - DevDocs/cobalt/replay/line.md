# `src/cobalt/replay/line.py`

The one miss line (S2-P4 STEP-7, R5, R1-18): unit `drc-misses/miss_line`
in that day's DRC note.

## `render_line`
```
Misses 2026-09-03: cards 3 (unarmed 2 · passed 0 · not_filled 0 · window 0 · rule_10 1) · cf-R Σ +0.5R, n=3 · avg: insufficient data (n<30) · movers ≥ 10%: 2 not in play — CTNT +165.0% not_in_any_source · SNYR −58.4% config_cap · formations: unavailable until S2-P2
```
- It is built only from the rows passed in. The runner passes the CURRENT
  reconciled set, so the line and `job.result` agree.
- **L8:** the cf-R sum always carries n. `avg ±x.xxR` appears only at
  `n >= MIN_N_FOR_AVERAGE` (30).
- **R1-12:** a nonzero `input_stale N` is printed after the card counts.
- Movers are ordered by |change| descending. The first `MOVERS_SHOWN` (3,
  from the ruled template) are listed, then `(+J more)`. Negatives use
  U+2212.
- `movers: unavailable` is printed when no benchmark settings were read.

## Writing (L28)
- `drc_note_path(day)`: `prefill.yaml` `review_dir` +
  `drc_filename_pattern` inside `resolve_vault_path()`. A missing file raises
  `DrcNoteAbsent`: "DRC note absent — prefill-drc owns creation".
- `write_miss_line(path, body, writer=)`: refuses an absent note, then
  calls `VaultWriter.upsert_unit(path, "drc-misses", "miss_line", body,
  placement=after_drc_rules())`. Replay never calls `create_if_absent`.
- `after_drc_rules()`: a zero-width placement at
  `find_section("drc-rules").close_line + 1`. If the anchor is missing the
  writer's own fallback applies (appended at the end, noted). A malformed
  marker raises from `find_section` and no byte is written.

Human edits winning, overrides, sync reverts, the mtime guard, the audit
row and the dry-run diff all belong to the writer (`vaultwrite/writer.md`).
The tests prove each one keeps every human byte outside the unit unchanged
(`tests/cobalt/test_replay_line.py`). The `requires_vault` test reads the
live DRC shape read-only: set `COBALT_TEST_LIVE_DRC` to a note path.
