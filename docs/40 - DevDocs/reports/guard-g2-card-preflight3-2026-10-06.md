# guard-g2 card preflight 3 — 2026-10-06

Card `21-guard-g2-card.md` (amend 3), BASE `3c257bb9`. Read only; I ran no test, no production command. `git log --oneline 3c257bb9..HEAD` on the five files prints nothing and `git diff --stat 3c257bb9 --` on them is empty, so every read is BASE. The six checks are those of preflight 2.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3c257bb9 main` | exit 0, no output | OK |
| 1b | `git -C /Users/cobalt/cobalt rev-parse --verify ops/guard-g2-1006` | `fatal: Needed a single revision` | OK |
| 1c | `ls /Users/cobalt/cobalt-wt/guard-g2-1006` | `No such file or directory` | OK |
| 1d | card lines 1-11 | `BRANCH ops/guard-g2-1006` · `WORKTREE guard-g2-1006` · `BASE 3c257bb9` · `TIP:` `CHECK REPORT:` `HOUSE B:` empty · `DB: none` · `RULINGS: 2026-10-06 R511` | OK |
| 2a | `grep -n "^| R511 " reports/cto-2026-10-06.md` | `28:\| R511 \| 06:37 ET \| HIS RULING: add the G2 row … \| APPROVED — pending fold \|` (card: "22 … re-run, never cite": it moved to 28) | OK |
| 2b | the same row | holds `HIS RULING` and `APPROVED` | OK |
| 2c | `git log -1 --format=%h -S"\| R511 \|" -- reports/cto-2026-10-06.md` | `720c98b8` | OK |
| 3a | `bare-guard.py` 5, 20, 56, 80, 106, 283, 666, 722, 725, 744, 846, 857, 968 | 5 `It never runs a command.` · 20 `G2 production (not deploy)` · 56 `"G2": "route: production is the deploy hub's…"` · 80 `READ_FILTERS = ("grep", "sed", "cut", "sort", "uniq", "head", "tail", "wc")` · 106 `PROD = re.compile(r"COBALT_ENV=production\|(?<![\w-])--prod(?![\w-])\|cobalt_brain")` · 283 `def words(segment)` · 666 `def first_message` · 722 `def seat` · 725 `text = first_message(…)` · 744 `return {"kind": kind, "cwd": cwd, "wt": …, "cwd wt": wt, "card": card}` · 846 `def bash_rules(command, s)` · 857 `return "G2", ROUTE["G2"]` · 968 `bash_rules(command, seat(event))` | OK |
| 3b | `desk-launch.sh` 176, 212, 238, 266-267, 418, 435, 457-459, 499 | 176 `committed()` · 212 `run_launch()` · 238 `ruling_row()` · 267 `ruling_items()` · 418 `committed "the prompt" "$pfile"` · 435 `*"Read '$pfile' and follow it exactly."*) ;;` · 457 `prulings=$(sed -n 's/^RULINGS:…` · 459 `( ruling_items "$prulings" ) 2>/dev/null && ruled=1` · 499 `run_launch "$dir" "$line" …` · `grep PROD-READ` prints nothing | OK |
| 3c | `test_bare_guard.py` 20-21, 143, 189, 223, 272, 405 | `BLOCK_HEAD` 20 · `BLOCK_TAIL` 21 · `G2_ROUTE` 143 · `def transcript` 189 · `def make_seat(…, first=None)` 223 · `def assert_allowed` 272 · `test_g2_the_deploy_hub_and_an_unknown_seat_are_allowed` 405 | OK |
| 3d | `db_query.py` 157-158, 211-212 | not re-read (the repo guard blocked my own `grep` for `--prod`, G2); equals BASE and preflight 2 read 158 `requires --prod`, 211 `--side choices`, 212 `--prod` | OK |
| 3e | `git diff --stat 3c257bb9 -- <5 files>`; `git log --oneline 3c257bb9..HEAD -- <5 files>` | both empty | OK |
| 4a | card R1, R2 vs the brain's text (preflight 2 prompt line 8) and R517 (`cto-2026-10-06.md:22`) | R1 stamp ` PROD-READ: <date> R<n>`, row committed + `HIS RULING` + `APPROVED` + names production reads, prompt committed and clean · R2 `first_message` marker, leading `COBALT_ENV=production uv run cobalt db query`, exactly one `--prod`, none `--prod=`, `--side` `user`/`system`, no other PROD match, tree never read: same. R1's refusal is the desk's amend-3 reading, flagged in the card `## RECORDS` and the amend report `## DECISIONS` | OK |
| 4b | red (c) on BASE | marked seat `…db query --prod --side user "SELECT 1"`: `PROD.search` hits at 857 → `G2`, exit 2; `assert_allowed` needs `returncode == 0`. Red for the stated reason | OK |
| 4c | reds (a), (b), (e), (f) (preflight 2 fail) | CLOSED. Card: `Only (c), (d) and (g) are red on BASE. CONTROLS (a), (b), (e), (f) are green on BASE (G2 refuses every PROD string for every non-deploy seat, bare-guard.py:856-857) and stay denied after the change; each is shown red under a named MUTATION`. Mutations named: marker test (a), leading-shape test (b), exactly-one-`--prod` test (f). (e) has none, said so | OK |
| 4d | uncommitted prompt (preflight 2 fail) | CLOSED. Card: `RED (d): an uncommitted row gets no marker … REFUSAL (d2), not a red: an uncommitted prompt is refused by committed "the prompt" (desk-launch.sh:418; refuse 177-179): exit 1, no launch line, green on BASE`. Mutations: `The prompt committed test is not a mutation` | OK |
| 4e | `\|` and `;` controls (preflight 2 fail) | CLOSED. Card: `CONTROL (e): … refused: by G2 on BASE; after the build R2 does not forbid ; or \|, G2 passes them and G1 denies (BLOCK text, BLOCK_HEAD / BLOCK_TAIL, test lines 20-21; sh is not in READ_FILTERS, bare-guard.py:80, 611-612); the test asserts the G1 text after` and `(never G2_ROUTE after)`. The `G2_ROUTE`-on-BASE-and-after list holds none of `\|`, `;` | OK |
| 4f | `seat()` returns no text (preflight 2 3d) | CLOSED. Card: `seat() (722-744) does NOT return that text: its dict at 744 holds kind, cwd, wt, cwd wt, card … the build adds the key "first": text to the dict at 744, and G2 (856-857) tests s["first"] (no second read of the transcript)`. Matches 725 and 744 above | OK |
| 4g | typed marker in a prompt's launch line (preflight 2 fail) | CLOSED in text. Card R1: `REFUSES a prompt whose launch line already holds PROD-READ: unless the row proof above passes and the line holds exactly the stamp the launcher would append for that RULINGS row`; `RED (g)`: prompt with the typed marker and no proving row refused (exit 1, no launch line; BASE launches, since 435 accepts any text after `follow it exactly.`); `CONTROL (g2)`: same prompt with the proving row passes, marker once; mutation `drop … the PROD-READ: refusal (red g)`; X4 and a RECORDS line. Gap: next row | OK |
| 4h | R1's equality clause (`exactly the stamp the launcher would append`) has a red or control | FAIL. (g) covers no proving row; (g2) covers the equal marker with the proving row. Nothing covers a typed marker naming a DIFFERENT `<date> R<n>` than the prompt's RULINGS row while the RULINGS row proves (the case the amend report's DECISIONS says is refused). No mutation `drop the equality test` is listed, so the equality can be removed with every named test still green | FAIL |
| 4i | the proof comes from `first_message`, never the tree; the guard runs no command | R2 reads `s["first"]` only; later-record and body-only markers are controls; header line 5 stands, card RECORDS repeats it | OK |
| 5a | the build's commands vs `BUILD-HUB.md` line 12 allow line | card runs `uv run pytest -q -p no:cacheprovider …` and `uv run cobalt jobs restarts <BASE>..HEAD`: `Bash(uv run pytest *)`, `Bash(uv run cobalt jobs restarts *)` both on line 12; `DESK_LAUNCH_DRY=1` runs inside tests; no production command typed | OK |
| 5b | RESTARTS class home, install (`## RECORDS`) | `grep -n -F "ops/desk" configs/cobalt/jobs.yaml` prints nothing (operator scripts) · `settings.json:22 "command": "python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py"` · `desk-launch.sh -> /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · `RESTARTS: none` expected | OK |
| 6a | `grep -c -F "«FILL" <card>` | `0` | OK |
| 6b | `git diff --stat -- <card>` | empty | OK |
| 6c | `git log -1 --format=%h -- <card>` | `e78ac1c5` | OK |

## ISSUES
- 4h FAIL: R1's equality clause (a typed marker passes only when it equals the stamp for the prompt's own RULINGS row) has no red or control and no mutation: add a control (a prompt typing a marker for another `<date> R<n>` with its own row proven is refused, exit 1) and the mutation `drop the equality test`.

Not counted: `ruling_items` takes a comma list (`desk-launch.sh:267`) while the card's R1 says "cites `<date> R<n>`" (singular); which item the stamp names for a RULINGS line with several is unsaid (the survey prompt cites one). Carried from preflight 1: an unquoted `$VAR`, brace or glob positional is one word to `words()`; argparse still takes only exact option words.

PREFLIGHT DONE · card: guard-g2-21 · checks: 27 · fails: 1 · ready: NO
