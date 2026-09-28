# `src/cobalt/taxonomy/cli.py`

## What it does
`cobalt taxonomy …` — the vault-backed trade_def commands, mounted by `cobalt.cli`. (Page created 2026-09-16; the module predates it.)

| Command | Purpose |
|---|---|
| `load [--dry-run]` | read every strategy note (`vault_loader`) and sync `"user".trade_defs` / `"user".tunables` |
| `migrate-strategy-notes --dry-run \| --apply [--note] [--matrix-alias] [--tunable-alias]` | ONE-OFF ADR-0008 D3 note shape migration |
| `migrate-trade-notes --dry-run \| --apply [--note]` | ONE-OFF ADR-0008 D4 `trade_def:` on trade notes |
| `add-alias <slug> <alias> [--dry-run]` | one alias into a note's `aliases[]` through `VaultWriter` |
| `sync-frontmatter --dry-run \| --apply` | re-align each note's class/family with its loaded def |
| `catalyst-review [--out]` | S2-P2 STEP-9: draft the ONE catalyst review file; writes no note |
| `catalyst-apply --review --sha256 --dry-run \| --apply` | S2-P2 STEP-9: batch-apply the marked file, bound to its sha256 |

## Notes
- Every command that can write to the vault takes exactly one of `--dry-run` or `--apply`; there is no default (`_require_mode`).
- The two catalyst commands import `taxonomy.catalyst` lazily; see `catalyst.md` for the preflight, resume and gate-ready rules.

## 2026-09-21 — setups one build STEP-2: the assumed-defaults writer and dry-run
- `cobalt taxonomy assumed write --from <rows.yaml> --dry-run | --apply` (`write_assumed`) is the one writer of `1 - Trading/Assumed Defaults.md`. It is a Cobalt L28 command over the EXISTING `VaultWriter`: `create_if_absent`, with an empty unit (`assumed_note_text([])`), then `upsert_unit` of `tunables:assumed`. Writes are marker-bounded and three-way merged (a line he edited wins), audited in `vault_writes`, and each result carries its unified diff. The rows file is validated through `TunableRegistry` and must read `source` assumed or ruling. It was proven on a `tmp_path` vault only. X23 checked it: a hand-edited `source` line survived a second write of other values. The dev-vault proof and the production write are the deploy's.
- `cobalt taxonomy tunables --assumed` (`assumed_report`) is read-only (L10, FINAL §7 point 3). It lists every row whose resolved `source` is `assumed` and every engine hole still null, with key, unit, scope and consumers. The source-page column is EMPTY in the repo, because the page lives in his companion (L32).
