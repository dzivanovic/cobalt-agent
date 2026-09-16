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
