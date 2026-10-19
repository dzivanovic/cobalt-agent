## §0 Headline
Card 790 amended in place, three edits, nothing committed.
X6, the C1 control and RECORDS now say `100` rows (proven on main).
Stale cites re-found: `tunables.yaml:1148`, `:1160`, `cli.py:150`.
Old PORT row carries "(context only, superseded by PORT2)". BASE untouched.

## DECISIONS
- RECORDS also holds the "consumers" counts line; its `94` and `94` became `100` and `100` (same rows, edit 1).
- main HEAD at the run is `21fb3fa6`; the proven files are unchanged against main (`git diff --stat main` empty), so the counts and lines hold on main.

## RECORDS
- Read: prompt 861; card `prompts/2026-10-18/790-f16-close-card.md`; `reports/f16-port2-preflight-2026-10-19.md`; `Vault/Think/6 - Permanent/Memory/topics/writing-rules.md`.
- `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `21fb3fa6`.
- `git -C /Users/cobalt/cobalt diff --stat main -- configs/cobalt/taxonomy/tunables.yaml src/cobalt/cli.py` → empty (working files equal main). A piped `git show main:<file> | grep` was refused by the bare-command hook, so the counts were read with Grep on those equal files.
- Grep `^  - key:` on `tunables.yaml` → `100`; Grep `^    consumers:` → `100` (the preflight's check 8g, `grep -c`, gave the same).
- Grep `key: prefill\.refresh_` → `1148: - key: prefill.refresh_window`, `1160: - key: prefill.refresh_interval_min`.
- Grep `load_tunables` on `src/cobalt/cli.py` → `150: from cobalt.taxonomy.loader import load_tunables`, `250`.
- Edits (Edit tool, card only): `94`→`100` at the C1 control, live ask X6, RECORDS loaders line; `:1084`/`:1096`→`:1148`/`:1160` in the scope text and the F4 RECORDS line; `cli.py:146`→`cli.py:150`; old PORT row gets "(context only, superseded by PORT2)" after "(header: 6452f70e)".
- Grep `\b94\b|1084|1096|cli\.py:146` on the card → no match after the edits.
- BASE (`cb4e42ce`) left as it stands. No git write.

DRAFTED · decisions: 2
