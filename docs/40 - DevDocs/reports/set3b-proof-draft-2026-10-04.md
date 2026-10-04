# set3b proof draft — 2026-10-04

## §0 Headline
- `07-deploy-set3b-card.md`: `MIGRATIONS`, `## MARKERS` and `## SMOKE READS` are filled; no `«FILL` is left (`grep -c -F "«FIL"` → 0).
- 4 lines carried from card 39 and re-checked on the new heads (`11b` at `0452dc99`); 1 new marker and 1 new smoke read for `10` cobalt-guard.
- `MIGRATIONS: none`: all five build stop lines say `migration: none`.
- Edits only to the card; header values, `## SHIPS` and `## RECORDS` untouched.

## FILLS
| line | kind | proof |
|---|---|---|
| `MIGRATIONS: none` | carried (39) | build stop lines: adoption-port `migration: none` · dev-rebuild-port `migration: none` · desk-tools-port `migration: none` · close-timer `migration: none` · cobalt-guard `migration: none` (`grep -n "migration:"` on its build report, line 313). `cli.py` and `dev_rebuild.py` are code, no `.sql`. |
| marker DEPLOY-HUB `window (v) does not hold` · 0 → 2 | carried, re-checked | main: `grep -c -F` → `0`; `git show 15ba4b75:"docs/40 - DevDocs/prompts/DEPLOY-HUB.md" \| grep -c -F "window (v) does not hold"` → `2` |
| marker `dev_rebuild.py` · absent → listed | carried, re-checked on `0452dc99` | main: `ls` → No such file; `git show 0452dc99:src/cobalt/db_migrations/dev_rebuild.py` prints the module (exists at the new head) |
| marker `claude-fable-5-1` in `desk-launch.sh` · 0 → 2 | carried, re-checked | main: `0`; `git show 525b5ae1:ops/desk/desk-launch.sh \| grep -c -F "claude-fable-5-1"` → `2` |
| marker `close-timer.sh` · absent → listed | carried, re-checked | main: `ls` → No such file; `git show 47a689a1:ops/desk/close-timer.sh` prints the script |
| smoke: hub-line tests | carried, re-checked | `git show 15ba4b75:tests/ops/test_hub_lines.py \| grep -c -F "def test_"` → `8` |
| smoke: dev-rebuild CLI tests | carried, re-checked on `0452dc99` | `git show 0452dc99:tests/cobalt/test_dev_rebuild_cli.py \| grep -c -F "def test_"` → `18` |
| smoke: desk-tools hooks | carried, re-checked | `git ls-tree --name-only 525b5ae1 ops/desk/stop-guard.py ops/desk/idle-wake.py` → both listed |
| smoke: close-timer plist | carried, re-checked | `git ls-tree --name-only 47a689a1 ops/desk/com.cobalt.close-timer.plist` → listed |
| marker cobalt-guard: `grep -c -F "route: production is the deploy hub" ops/desk/bare-guard.py` · 0 → 1 | new | main: `0`; `git show a2e19ceb:ops/desk/bare-guard.py \| grep -c -F ...` → `1` (G2's route sentence, card 10 row G2) |
| smoke cobalt-guard: `grep -c -F "route: a fixed file changes by a card row" ops/desk/bare-guard.py` · count 1 or more | new | main: `0`; `a2e19ceb` → `1` (G5's route sentence, card 10 row G5). Chosen over the test-file count because `tests/ops/test_bare_guard.py` already exists on main and would pass before the merge. |

## DECISIONS
- ASK DESK: the close-timer build stop line reads `tip: e4c0c4dd`; the check fixed one finding and moved the code tip to `47a689a1` (the card's value). I read `migration: none` from the build line and found nothing in the fix that changes it; the check line carries no migration field. Default taken: `MIGRATIONS: none`. [16:00 ET]

## RECORDS
- Files edited: `docs/40 - DevDocs/prompts/2026-10-04/07-deploy-set3b-card.md` only; this report written. No git write, no launch.
- Helper mistake: two `git show` calls printed whole files (`dev_rebuild.py`, `close-timer.sh`, DEPLOY-HUB) into tool output; read-only, no effect.
- Marker 1 and smoke 1 of 39 name `DEPLOY-HUB.md` and `desk-launch.sh` counts as of the heads; `main` itself was read, not a tree.

SET3B PROOF FILLED · placeholders left: 0 · decisions: 1
