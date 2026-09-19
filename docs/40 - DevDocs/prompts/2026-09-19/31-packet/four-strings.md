# The four R20-approved rule strings, verbatim (`cto-2026-09-19.md` §4 R20, 11:57 ET)

(1) `Bash(COBALT_ENV=production uv run cobalt settings load --card /Users/cobalt/cobalt/data/backups/cards-live-2026-09-19/p2-live-settings.yaml --sha256 f3663399b1cbb5ba94edadc7b929900a09be02439c84ffc24f89c12ea81c65f0 --dry-run)`

(2) `Bash(COBALT_ENV=production uv run cobalt settings load --card /Users/cobalt/cobalt/data/backups/cards-live-2026-09-19/p2-live-settings.yaml --sha256 f3663399b1cbb5ba94edadc7b929900a09be02439c84ffc24f89c12ea81c65f0 --apply)`

(3) `Bash(COBALT_ENV=production uv run cobalt settings load --card /Users/cobalt/cobalt/data/backups/pre-s2-p2-2026-09-17/p2-dark-settings.yaml --sha256 945e42f86997559267b2e7c20783f2d023b9135ae4bb437ca25a4999ca7cd3ca --dry-run)`

(4) `Bash(COBALT_ENV=production uv run cobalt settings load --card /Users/cobalt/cobalt/data/backups/pre-s2-p2-2026-09-17/p2-dark-settings.yaml --sha256 945e42f86997559267b2e7c20783f2d023b9135ae4bb437ca25a4999ca7cd3ca --apply)` (ROLLBACK, only on a failed verification)

Note: strings (3) and (4) are IDENTICAL, byte for byte, to two strings already present in `02-deploy-stack-3.md`'s approved and already-executed launch line (see `02-settings-load-excerpt.md`) — they are the exact command that put the dark row into production on 2026-09-19 08:21:15 ET. Strings (1) and (2) are NEW — this is the first time the live multi-key card file has ever been loaded by any command, dry-run or apply.

CONDITIONS stated with R20: dry-run first, FAILED unless the parsed values are exactly his; no restart; today, outside 20:00–21:00 ET. NEVER: push, a deploy, any other settings file, `bypassPermissions`.
