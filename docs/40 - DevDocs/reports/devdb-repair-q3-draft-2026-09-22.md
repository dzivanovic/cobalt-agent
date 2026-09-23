# DEV-DB REPAIR Q3 RE-ISSUE — draft report, 2026-09-22 (seat `devdb-q3-draft-0922`, prompt `77-draft-devdb-repair-q3.md`)

## §0
- `68-devdb-repair.md` re-issued in place (22:16 EDT, uncommitted). Option (i): `pg_database_size` moved out of Q3 into a new in-container probe **D0** ("Q3 size probe"). Q3 keeps `db` + `has_head`.
- Launch line: **1 string added, 0 changed**. Every other string, step, gate and R8 rollback is unchanged byte for byte (word-diff below). Launch row is back to `R__`.
- Other preflight queries checked: none fails the same way, so **0 other fixes**. Cause: `db.py:216` `SET ROLE cobalt_system` (NOINHERIT, `db.py:249`), and `pg_database_size` checks that role's CONNECT on the database.
- Before launch: his word on D0 plus a new launch row, and one other house reads the diff (L67). ESCALATE: 5.

## CHANGES
| # | where (68) | old | new |
|---|---|---|---|
| 1 | line 1, SEAT prose | `after the launch row **R124**` | `after the launch row **R__**` |
| 2 | line 1, launch line, after D2's string | — | `"Bash(docker exec cobalt_memory sh -c 'psql -U \"\$POSTGRES_USER\" -d postgres -v ON_ERROR_STOP=1 -Atc \"SELECT pg_database_size('\"'\"'cobalt_dev'\"'\"')\"')"` (ADDED) |
| 3 | AUTHORIZATION, new bullet after "His approval of this list" | — | `**His approval of the Q3 size probe**`: `grep -n -F "Q3 size probe"` over `cto-2026-09-22.md` / `cto-2026-09-23.md` → a `\| R` row quoting his approve for D0's string, plus `git … log -1 --format=%H -S"Q3 size probe" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` NON-EMPTY. Otherwise `FAILED: authorization mismatch — the Q3 size probe is not approved on a committed row` |
| 4 | AUTHORIZATION, launch bullet | `row **R124**` | `row **R__**` |
| 5 | COMMANDS Q3 (typed text; the allow rule is the existing `db query … *` wildcard, unchanged) | `"SELECT current_database() AS db, pg_database_size(current_database()) AS bytes, to_regclass('system.archive_incidents') IS NOT NULL AS has_head"` | `"SELECT current_database() AS db, to_regclass('system.archive_incidents') IS NOT NULL AS has_head"` |
| 6 | COMMANDS, new line after Q3 | — | `- D0 (the Q3 size probe …) docker exec cobalt_memory sh -c 'psql -U "$POSTGRES_USER" -d postgres -v ON_ERROR_STOP=1 -Atc "SELECT pg_database_size('"'"'cobalt_dev'"'"')"'` — read-only. MUST print one integer, recorded as `bytes`. Otherwise `FAILED: D0 — <output verbatim>`, stop, nothing changed |
| 7 | D3 gate | `3 × Q3's \`bytes\`` | `3 × D0's \`bytes\`` |
| 8 | Steps 1 order | `Q1 → Q2 → Q3 → D1 → D2 → D3` | `Q1 → Q2 → Q3 → D0 → D1 → D2 → D3` |
| 9 | REPORT ESCALATE list | `its size from Q3's \`bytes\`` | `its size from D0's \`bytes\`` |

`git diff --stat`: `1 file changed, 8 insertions(+), 6 deletions(-)`. Edit tool used, not Write, to keep every untouched byte exact.

Other preflight queries, checked against the app role (`cobalt_system` via `SET ROLE`, NOINHERIT) on `cobalt_dev`:
| query | reaches it? | evidence |
|---|---|---|
| Q1 (`pg_catalog.pg_attribute/pg_class/pg_namespace`) | yes | ran exit 0 at 22:1x (`devdb-repair-2026-09-22.md` PREFLIGHT). Catalogs are PUBLIC-readable, and the restored DB has the same ACL (`--create`), so PROOF's Q1 works too. |
| Q2 (`pg_catalog.pg_tables`) | yes | ran exit 0 at 22:1x. Same reasoning as Q1. |
| Q3 new (`current_database()`, `to_regclass`) | yes, reasoned | no database-ACL-gated function. The 22:13 error text is "permission denied for **database**" (the `pg_database_size` CONNECT check), not "for schema". `to_regclass` on `system.` needs USAGE on `system` only when that schema exists, and `system` is `cobalt_system`'s own side. UNPROVEN until run (L70). |
| D1 / D2 / D3 | yes | container superuser. All three ran exit 0 at 22:1x. |
| PROOF Q1–Q3 | yes | same role and same statements as above. The old Q3 would have failed in PROOF too, and the new one fixes both places. |

## RULE PROOF
The new launch line vs `HEAD` (`git -C /Users/cobalt/cobalt diff --word-diff=plain`, 22:16 EDT). The only difference inside the `claude --bg …` command is one inserted token:
`"Bash(docker exec cobalt_memory {+sh -c 'psql -U \"\$POSTGRES_USER\" -d postgres -v ON_ERROR_STOP=1 -Atc \"SELECT pg_database_size('\"'\"'cobalt_dev'\"'\"')\"')" "Bash(docker exec cobalt_memory+} df -k …`
In words: one new string inserted between D2's string and D3's string. Everything else is unchanged: the other 20 allow strings, the 6 deny/tool strings, `--model`, `--permission-mode acceptEdits`, `--remote-control devdb-repair-0922` and the `--add-dir`s. The `R124 → R__` change sits in the SEAT prose before the command, not in the command. Expected differences = the listed strings only: **HOLDS**.
Escape proof, run by this seat:
- `printf '%s\n' "<launch spelling>"` printed `Bash(docker exec cobalt_memory sh -c 'psql -U "$POSTGRES_USER" -d postgres -v ON_ERROR_STOP=1 -Atc "SELECT pg_database_size('"'"'cobalt_dev'"'"')"')`, which is the D0 typed command exactly.
- `sh -c` simulation of the container side printed `SELECT pg_database_size('cobalt_dev')`, with `$POSTGRES_USER` left for the container's shell (empty on the host). No credential appears on the host line (L4).
- `grep -rl -F "Q3 size probe"` over `reports/` + `prompts/` found only `68` and `77`. No desk file carries the literal yet, so the gate cannot pass before his row.

## NEW strings:
Launch-line spelling (zsh, verbatim):
`"Bash(docker exec cobalt_memory sh -c 'psql -U \"\$POSTGRES_USER\" -d postgres -v ON_ERROR_STOP=1 -Atc \"SELECT pg_database_size('\"'\"'cobalt_dev'\"'\"')\"')"`
Typed by the hub (D0):
`docker exec cobalt_memory sh -c 'psql -U "$POSTGRES_USER" -d postgres -v ON_ERROR_STOP=1 -Atc "SELECT pg_database_size('"'"'cobalt_dev'"'"')"'`
Grep literal his approval row must carry: `Q3 size probe`.

## ESCALATE
1. **His word is needed on the one NEW string** (D0 above). His R122 does not cover it. The desk needs a committed `| R` row in `cto-2026-09-22.md` that carries `Q3 size probe` and his "approve", plus a NEW launch row (fills `R__`). For transparency, Q3's typed SQL also shrank (CHANGES 5). It stays under the already-approved `db query … *` wildcard, so it is not counted as a string change.
2. **House read needed (L67): yes.** This re-issue changes a DB-recovery prompt, so at least one other house must read it before it runs. Named, not drafted: one round in which Gemini reads `68`'s word-diff vs `4830d80` and D0's quoting, with verdict `RUN IT` / `HOLD`.
3. **The failed run's report is untracked** (`?? docs/40 - DevDocs/reports/devdb-repair-2026-09-22.md` in git status at seat start). The relaunch's first Write overwrites that path, which is kept byte for byte. The desk commits the FAILED report before the relaunch, or its evidence is lost.
4. **The launch-row gate is ambiguous.** It is kept byte for byte as instructed: `grep -n "68-devdb-repair.md"` / `git log -S"68-devdb-repair.md"` are already satisfied by the committed R124 row. The hub must match the filled-in `R<n>`, not just any row. The desk may want a distinct literal in the new launch row. That would be a gate change, so it was not made here.
5. `ASK DESK: D0 nests '"'"' quoting; whether acceptEdits' allowlist matcher matches it verbatim is UNPROVEN — switch to the no-nested-quote shape 'psql -U "$POSTGRES_USER" -d cobalt_dev -v ON_ERROR_STOP=1 -Atc "SELECT pg_database_size(current_database())"' (D1's proven shape, still names cobalt_dev literally via -d)? [22:16 EDT]`. Safe default: drafted as instructed (`-d postgres`, literal `'cobalt_dev'`). A matcher miss asks → the run FAILED at D0 under L62, and nothing has changed by then.
- L74: a block arrived beside this seat's tool results asking for a `Claude-Session` commit trailer and naming a file-send tool (`SendUserFile`). Recorded once as DATA and not followed. This seat makes no commit and sends no file.

## CONTINUE
next: none. Draft complete. The desk takes ESCALATE 1–5: commit the FAILED report, get the L67 read, get his approval row + launch row, commit `68` + rows, then launch.

DEVDB REPAIR RE-ISSUED · strings changed: 0 · strings added: 1 · other preflight fixes: 0 · house read needed: yes · ESCALATE: 5
