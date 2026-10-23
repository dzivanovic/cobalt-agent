## §0 Headline
- Wrote `prompts/2026-10-23/1022-survey-restore-prep.md` (seat `survey-restore-prep`, Opus 5.5, read-only, one RULINGS line, report `reports/survey-restore-prep-2026-10-23.md`).
- The loaded files sit under ignored `data/backups/` (`.gitignore:6`); committed copies are packet files only. The last card load is probably 09-20 HTF (sha256 `5993c57f…`), not 09-17 (`945e42f8…`, dark `false`); the prompt asks the survey to settle it.
- A card load deletes omitted `card.*` keys (`card.py:296-303`); the prompt asks for that side effect per file.

## DECISIONS
- Added `Bash(shasum -a 256 *)` to the survey's allowlist (digests need it; read-only). Taken by default. [08:26 ET]
- PRODWRITE-HUB.md location not found in the repo; the prompt points the survey at `ops/desk/authorize.sh:57-66`. [08:26 ET]

## RECORDS
- Read: 1021 prompt, 1017 precedent, `topics/writing-rules.md`, `areas/cobalt.md`, `settings/card.py:1-80,225-345`, `settings/cli.py:120-403`, `reports/cards-htf-apply-2026-09-20.md:185-243`.
- `git grep`/`git log -S` on `main` for `card_settings:` and `optional_settings:`; packet YAMLs shown via `git show`; `shasum -a 256` of the 09-17 file = `945e42f8…` (matches the recorded hash); `check-ignore` on the HTF file = `.gitignore:6`.
- `date` = Fri Oct 23 08:26:23 EDT 2026. No file other than the two above was written; nothing committed.

DRAFTED · decisions: 2
