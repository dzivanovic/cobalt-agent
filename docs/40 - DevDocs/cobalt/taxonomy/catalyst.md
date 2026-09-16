# `src/cobalt/taxonomy/catalyst.py`

## What it does
Taxonomy v0.8's `catalyst` standard, moved into the trader's notes through ONE review file and ONE batch apply (S2-P2 STEP-9; ruling R10; Astra R1-17).

    cobalt taxonomy catalyst-review [--out <file>]
    cobalt taxonomy catalyst-apply --review <file> --sha256 <hash> (--dry-run | --apply)

## Key functions/classes
- `draft_review(vault_root, *, today) -> CatalystReview` — one `ReviewRow` per DEFINED note (drafts are skipped), sorted by note path: note path, slug, the Definition unit's sha256 as drafted, the proposed line (`- catalyst`, or `already present`), the note's existing `catalyst_*` factors, and `drop = []` (keep).
- `render_review` / `parse_review` — the markdown file. Instructions above; the machine part sits between `<!-- catalyst-review:v1 -->` markers: a `drafted:` line and a six-column table. The trader edits only the last cell: `keep`, `drop` (every listed `catalyst_*`), or `drop: <factor>, …`. A mark naming a factor the note does not carry, an empty `drop:`, any other word, a changed header or a wrong cell count is refused.
- `write_review(vault_root, out, *, today)` creates the file exclusively (never overwrites) and returns its path and sha256. The CLI default is `docs/40 - DevDocs/reports/catalyst-review-<ET date>.md`.
- `plan_apply(vault_root, review)` — the preflight, over EVERY row before any write:
  - a defined note missing from the review, or a reviewed note no longer defined, refuses (stale review);
  - unit sha256 == drafted → `write`, with the target body built and validated at schema 0.5 (`trade_def.schema_gate("0.5")`);
  - unit differs but already carries the reviewed change → `already_applied` (how an interrupted batch resumes);
  - otherwise the unit drifted → the whole batch is refused, nothing written.
- `apply_review(vault_root, review_path, *, expected_sha256, writer) -> ApplyReport`:
  1. sha256 of the file's bytes must equal `--sha256`;
  2. `plan_apply`;
  3. per pending unit, re-hash right before writing (a human edit that landed mid-batch stops the batch with "applied so far: n of m"), then `writer.upsert_unit` (L28: versioned, diffed, human-wins merge). A writer failure stops the batch the same way;
  4. with `--apply`, `verify_applied` re-reads every reviewed unit and requires the line present, the marked factors gone and validation at 0.5 — only then `gate_ready = True`. A dry run is never gate-ready.
- `target_body(body, row)` appends `- catalyst` when absent and removes the marked factors (`factor_lines`); `is_applied(body, row)` is its test.

## Config it reads
The vault (via `resolve_vault_path` in the CLI) and the engine tunables through `load_vault_trade_defs`. Writes go through `VaultWriter` with a `VaultWriteStore`.

## Gotchas
- The loader gate (`trade_def.LOADER_SCHEMA_GATE`) is NOT flipped here; STEP-D4 flips it in code after the apply reports gate-ready.
- Adding the line changes each def's md5. Open radar cards keep refreshing against their slug's new def and gain a `catalyst` dot once (`radar/evaluate.py`, Astra R2-4).
- The review file holds note paths and factor names — the trader's data. It is written for him, not committed by Cobalt.
