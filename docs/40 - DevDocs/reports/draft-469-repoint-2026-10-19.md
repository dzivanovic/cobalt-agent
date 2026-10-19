# draft-469-repoint — 2026-10-19

## §0 Headline
- Card 469 `f21-vectors` re-pointed onto main `1d9c0028` (Genesis port `bc990598`, Gemini grant `958ab78c`). One file edited: `prompts/2026-10-13/469-f21-vectors-card.md`.
- Changed: V4 migration number (`0028` default, `0027` if F5 does not deploy first), head-pin list (18 files), `gate-lists.md:33,39`, shipped store API, V5 `cli.md` seam-Edit note, READ line, one RECORDS line.
- Every modelaccess/voice/jobs `file:line` still holds on main; BASE, TIP, CHECK REPORT, HOUSE B, RULINGS, CLASS untouched. Nothing committed.

## DECISIONS
- ASK DESK: which migration number does 469 take, given F5 card 731 claims `0027_market_checkpoints` and is not yet deployed? Default: 469 takes `0028`, F5 deploys before it; whichever deploys second takes the seam row for the registry pins and `FORWARD`. [12:21 ET]

## RECORDS
- `date` → Mon Oct 19 12:21:15 EDT 2026.
- `git show main:src/cobalt/db_migrations/__init__.py` → `FORWARD` ends `0026_genesis_chunk.sql`, `REVERSE` starts `0026_genesis_chunk.rollback.sql`.
- `git show main:src/cobalt/genesis/store.py` → `GenesisStore` (`SIDE = Side.USER`, `_connect`, `replace`), `import_paths`; no embedding column.
- `git grep main -- src/cobalt/genesis/cli.py` → `add_parser` mounts `import`, `search` (`:22-28`).
- `git grep -n main -- ops/desk/gate-lists.md` → genesis ids at `:33` (PASS 1) and `:39` (PASS 2).
- `git grep main -- src/cobalt/cli.py` → `voice_cli` import `:84`, `genesis_cli` import `:90`, `add_parser` `:557`; `cli.md:141` the `f21-genesis-1013` section.
- `git grep main -- 731-f5-card.md` → K6 `0027`, DECISION 3.
- `git grep main -- tests` for `0026` → the pin files; the 18 names match the port build report `## E3 THE ROWS` (`reports/f21-genesis-fr1-build-2026-10-19.md:89`).
- `git show main:` for `config.py`, `adapters.py`, `client.py`, `modelaccess.yaml`; `git grep main` for `models.py`, `test_modelaccess_config.py`, `jobs.yaml`, `voice/*` → lines unchanged; `git diff --stat 279c99ce main` on modelaccess, `modelaccess.yaml`, the config test and `src/cobalt/voice` → empty.
- Not traced: none. (Not opened: `cli.md` tail, left unnamed by instruction.)

DRAFTED · decisions: 1
