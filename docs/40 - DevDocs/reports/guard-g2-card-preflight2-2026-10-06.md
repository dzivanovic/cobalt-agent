# guard-g2 card preflight 2 — 2026-10-06

Card `21-guard-g2-card.md`, BASE `3c257bb9`. Read only; I ran no test, no production command. The five files equal BASE (`git diff --stat 3c257bb9 -- <5 files>` prints nothing), so each read below is BASE.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3c257bb9 main` | exit 0, no output | OK |
| 1b | `git -C /Users/cobalt/cobalt rev-parse --verify ops/guard-g2-1006` | `fatal: Needed a single revision` | OK |
| 1c | `ls /Users/cobalt/cobalt-wt/guard-g2-1006` | `No such file or directory` | OK |
| 1d | card lines 1-11 | `JOB: guard-g2` · `LADDER: OFF-LADDER — cto-2026-10-06.md R511` (the launcher only needs LADDER non-empty, `desk-launch.sh:666`) · `TIP:` `CHECK REPORT:` `HOUSE B:` empty · `DB: none` · `RULINGS: 2026-10-06 R511` | OK |
| 2a | `grep -n "^| R511 " reports/cto-2026-10-06.md` | `26:\| R511 \| 06:37 ET \| HIS RULING: add the G2 row … \| APPROVED — pending fold \|` (card says 22 and says to re-run, not cite) | OK |
| 2b | the same row | holds `HIS RULING` and `APPROVED` | OK |
| 2c | `git log -1 --format=%h -S"\| R511 \|" -- reports/cto-2026-10-06.md` | `720c98b8` | OK |
| 3a | `bare-guard.py` 5, 20, 36-37 | 5: `ONE line on stderr naming the route. It never runs a command.` · 20: `# THE RULES, first hit wins. Bash: G3 .env read · G2 production (not deploy) · G4 git shape` · 36-37: the `COBALT_WT_ROOT` comment. Previous 3b fixed | OK |
| 3b | `bare-guard.py` 106 | `PROD = re.compile(r"COBALT_ENV=production\|(?<![\w-])--prod(?![\w-])\|cobalt_brain")` | OK |
| 3c | `bare-guard.py` 666-694 | `def first_message(transcript)` … first non-meta `user` record, `return ""` at 694 | OK |
| 3d | `bare-guard.py` 722-744, 725, 744 | 725 `text = first_message(event.get("transcript_path"))` OK; 744 `return {"kind": kind, "cwd": cwd, "wt": card["worktree"] or wt, "cwd wt": wt, "card": card}`: the dict holds NO first-message text; `text` is a local. The card says "`seat()` returns that text in its dict (line 744) and G2 tests it" | FAIL |
| 3e | `bare-guard.py` 846-868, 848, 856-857 | 848 `segs = [words(x) for x in segments(command, cuts)]` · 856-857 `if kind is not None and kind != "deploy" and PROD.search(command): return "G2", ROUTE["G2"]`; `bash_rules(command, s)` gets only the seat dict `s` | OK |
| 3f | `src/cobalt/db_query.py` 154-159, 209-216 | 157-158 `if dbname == db.PROD_DB_NAME and not prod: raise QueryRefused(f"database {db.PROD_DB_NAME} requires --prod")` · 211 `--side choices=[s.value for s in Side]` · 212 `--prod` store_true; `Side` is imported from `cobalt.db` (line 17); I did not open it, so `user`/`system` rests on R517 | OK |
| 3g | `tests/ops/test_bare_guard.py` 143, 189-274, 272-274, 387-413, 403-406 | 143 `G2_ROUTE = "route: production is the deploy hub's; a dev read uses COBALT_ENV=dev"` · `transcript` 189, `make_seat(…, first=…)` 223-247, `assert_allowed` 272-274 (`returncode == 0`) · G2 block 387-413 · 403-406 `test_g2_the_deploy_hub_and_an_unknown_seat_are_allowed` | OK |
| 3h | `tests/ops/test_desk_launch_prechecks.py` 52, 775-850 | 52 `RULINGS_HEAD = …` · 775 `survey_prompt` · 787 `launch_prompt` · 792-850 the F5 tests | OK |
| 3i | `desk-launch.sh` 176-180, 212-227, 238-265 | `committed()` 176-180 · `run_launch` 212-228 · `ruling_row` 238-265: row text 257-261 (`*"HIS RULING"*APPROVED*`), commit proof 262-264 | OK |
| 3j | `desk-launch.sh` 404-500 | 418 `committed "the prompt" "$pfile"` · 421-422 `line=$(sed …)` · 435 `*"Read '$pfile' and follow it exactly."*` · 457-459 `prulings=…; … ( ruling_items "$prulings" ) 2>/dev/null && ruled=1` · 499 `run_launch "$dir" "$line" …` | OK |
| 3k | `git diff --stat 3c257bb9 -- <the 4 files + db_query.py>` | empty | OK |
| 3l | `grep -n -E "^\| R508 " reports/cto-2026-10-06.md`; R511 row | R508 (line 29) `HIS RULING … production read included … \| APPROVED \|`; R511 holds `production read-only`; both hold the `production read` text the card tests | OK |
| 3m | RECORDS: `grep -n -F "ops/desk" configs/cobalt/jobs.yaml` · `grep -n "bare-guard.py" /Users/cobalt/.claude/settings.json` · `ls -la /Users/cobalt/.claude/ops/desk-launch.sh` | no output · `22: "command": "python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py"` · `… desk-launch.sh -> /Users/cobalt/cobalt/ops/desk/desk-launch.sh` | OK |
| 3n | previous 3c (R511 line number) | card now says "22 at 2026-10-06; it moves: re-run, never cite the number"; the file has it at 26 | OK |
| 4a | card R1, R2 vs the brain's text (prompt line 8) and R517 | R1 stamp ` PROD-READ: <date> R<n>`, row committed + `HIS RULING` + `APPROVED` + names production reads, prompt committed and clean · R2 first_message marker, exactly one `--prod`, `--side` `user`/`system`, no other PROD match, tree never read: same. The card adds the leading shape `COBALT_ENV=production uv run cobalt db query` (stricter, in the card's own R2(ii) text); `none starts with --prod followed by =` is in the card | OK |
| 4b | red (c) on BASE | `…db query --prod --side user "SELECT 1"` on a marked seat: `PROD.search` hits at 856 → `G2`, exit 2; `assert_allowed` fails on `returncode == 0`. Red for the stated reason | OK |
| 4c | reds (a), (b), (e), (f) on BASE | each asserts a refusal. BASE's G2 refuses every `PROD` string for every non-deploy kind (856-857), so all four are GREEN on BASE (a: no marker → G2; b: `db migrate` carries `COBALT_ENV=production` → G2; e: `; ls`, `\| sh` → G2 first; f: two `--prod` → G2). The card calls them RED; they are controls, red only under a mutation. Only (c) and (d) fail on BASE | FAIL |
| 4d | red (d): "an uncommitted row, or an uncommitted prompt, gets no marker; the launch line printed under `DESK_LAUNCH_DRY=1` has no `PROD-READ`" | an uncommitted prompt never reaches a launch line: `desk-launch.sh:418` `committed "the prompt"` → `refuse "…is not committed on main"`, exit 1, nothing printed. The prompt-committed condition of R1 is already the launcher's gate, so "launch as today" for it is a refusal, and the mutation "drop the prompt committed test" has no new test to drop. An uncommitted row: `ruling_items` fails inside `2>/dev/null`, `ruled=0`; it prints a line only when the line holds no write string | FAIL |
| 4e | controls "each run on the same seat … denied with `G2_ROUTE` on BASE and after" | `…"SELECT 1" \| cat` after the build: R2 does not forbid `\|`, so G2 passes; `g1` returns the BLOCK text (`cat` is not in `READ_FILTERS`, `bare-guard.py:611-612`), not `G2_ROUTE`. A test asserting `G2_ROUTE` for it fails after. The card's parenthesis ("state which rule returns each") contradicts the sentence. The other controls (`migrate`, `dev-rebuild`, `--side` out of range, second `COBALT_ENV`, no `--prod`, `--prod=x`, `NAME=x`, `env`, `SELECT cobalt_brain`, `SELECT '--prod'`, `psql cobalt_brain`, later-record marker, body-only marker, no marker) hit G2 on BASE (PROD or kind) and, for a marked seat, R2 | FAIL |
| 4f | where the proof comes from (previous 4d) | R2 reads only `first_message` (the first non-meta `user` record, `bare-guard.py:666-694`); R1's commit proof is the launcher's; the guard reads no file for it; reds (a) and the "later record" and "body only" controls pin it. A brain seat that writes its own prompt or a `cto` row (`G5`) no longer matters: neither is read | OK |
| 4g | can the marker be authored rather than stamped (X2) | R1 appends the marker but nothing refuses a launch line that already holds ` PROD-READ: <date> R<n>`: line 435 accepts any text after `follow it exactly.`, and a prompt's launch line (`desk-launch.sh:421-422`) is whatever the prompt file holds. A brain seat may write prompts under `prompts/20*/` (G5); once the desk commits and launches that prompt, its first message carries the marker with no row. No red or control covers a marker already in the prompt's launch line | FAIL |
| 4h | the guard runs no command (previous 4d) | R2 uses `words()`, `PROD`, the marker regex only; header line 5 stands; the card's RECORDS repeats it | OK |
| 5a | the build's commands vs `BUILD-HUB.md` line 12 allow line (R411, R412 rows: `cto-2026-10-05.md:107, 109`) | `uv run pytest -q -p no:cacheprovider …` and `uv run cobalt jobs restarts <BASE>..HEAD` are `Bash(uv run pytest *)` and `Bash(uv run cobalt jobs restarts *)`; `DESK_LAUNCH_DRY=1` runs inside the tests; no production command; no new command | OK |
| 5b | RESTARTS class home, launcher/hook install | in the card's `## RECORDS`: both scripts operator (no `ops/desk` in `jobs.yaml`), tests no resident, report DOCS, `RESTARTS: none`; hook = `settings.json:22` on the main checkout; launcher = symlink; no install step (3m) | OK |
| 6a | `grep -c -F "«FILL" <card>` | `0` | OK |
| 6b | `git diff --stat -- <card>` | empty | OK |
| 6c | `git log -1 --format=%h -- <card>` | `1503d5b6` | OK |

## ISSUES
- 3d FAIL: `seat()` (`bare-guard.py:744`) does not return the first message; the card says it does. The build must add a key to the dict (or re-read the message in `bash_rules`); name it in the row.
- 4c FAIL: reds (a), (b), (e), (f) are green on BASE (G2 refuses every `PROD` string today); only (c) and (d) are red. Call (a), (b), (e), (f) controls, or say they go red only under a mutation.
- 4d FAIL: an uncommitted prompt is refused at `desk-launch.sh:418` (exit 1, no launch line), so no `PROD-READ`-free line prints; test it as a refusal, and drop "prompt committed" from the launcher mutations (it is not a new test).
- 4e FAIL: the control `…"SELECT 1" \| cat` is denied by G1 (BLOCK text) after the build, not `G2_ROUTE`; the sentence "denied with `G2_ROUTE` on BASE and after" is wrong for it, and the `;` and `\| sh` reds likewise return G1. Say G2 on BASE, G1 after.
- 4g FAIL: a marker typed into a prompt's own launch line is not refused by R1 and satisfies R2. Add a launcher refusal (a launch line already holding `PROD-READ:` without the proven row) and a control.

Not counted: an unquoted `$VAR`, brace or glob positional is one word to `words()` and may expand in the shell (carried from the first preflight); argparse still takes only the exact option words, so no wider verb is reachable.

PREFLIGHT DONE · card: guard-g2-21 · checks: 34 · fails: 5 · ready: NO
