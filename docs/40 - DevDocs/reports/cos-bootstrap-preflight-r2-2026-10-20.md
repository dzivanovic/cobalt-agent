# Card 929 (cos bootstrap, 4.6L-BO) — preflight round 2, 2026-10-20

Read-only. Card `prompts/2026-10-20/929-deploy-cos-bootstrap-card.md` as committed at HEAD (no working-tree diff). Both round-1 FAILs are fixed; no new FAIL.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | header values (read card) | `JOB cos-bootstrap`, `LADDER S5-P3 · F20`, `BRANCH/WORKTREE/TIP none`, `BASE main`, `SET cos`, `TICKERS none`, `MIGRATIONS none`; `TAG`/`RULINGS` carry `«FILL»` (his/desk, round-1 note 1 stands) | OK |
| 2 | `git diff HEAD --stat -- <card>` | empty: the card is committed as read | OK |
| 3 | `git diff 22ac1970 HEAD -- <card>` | exactly three hunks: WAITS gains `, hitl.page_base_url set`; SMOKE READS row 5 trimmed to `` `0` ``; RECORDS: R2197/R2198 cited by row id, the row-5 note moved to a RECORDS line, one 933 P1 line added. Nothing else changed. | OK |
| 4 | `git grep -n main: run.py` | `:99 poll_s = tunable_int`, `:103 SCRATCH_DIR.mkdir`, `:105 turns.ensure_schema`, `:109 hitl.ensure_schema`, `:147 refuse_if_agent_alive()`, `:150 store.register`, `:155 store.mark_running`; `:44 def refuse_if_agent_alive`, `:52 raise CosRefused` | OK |
| 5 | `git grep -n main: session.py actions.py` | `session.py:76 def tunable_int`, `:82`/`:84` raise `CosConfigError`, `:85` return; `actions.py:62-71` `request_ttl_min` null raise (`:68`) | OK |
| 6 | `git grep -n main: tunables.yaml` | `:1008-1009 cos.poll_interval_s` `value: null`; `:1026-1027 hitl.request_ttl_min` `value: null`; `:1038 hitl.page_base_url` exists | OK |
| 7 | `git grep -n main: jobs.yaml, plist, migrations` | `jobs.yaml:206` label, `:214 enabled: false`; plist `:33 cos.log`, `:35 cos.err`; `0001_cobalt_cos.sql:14`, `:28` and `0001_cobalt_hitl.sql:20` are `CREATE TABLE IF NOT EXISTS` | OK |
| 8 | `grep -n R219[6-8] reports/cto-2026-10-20.md` | rows R2198, R2197 exist (R2197 = X13 PASS; R2198 = bootstrap brief). The card now cites them by id, so line drift cannot break it. (Round-1 FAIL 6 closed.) | OK |
| 9 | `grep -n R1112 / R1854` in `cto-2026-10-11.md`, `cto-2026-10-18.md` | `cto-2026-10-11.md:31` R1112 `HIS RULING · APPROVED`; `cto-2026-10-18.md:99` R1854 `HIS RULING · APPROVED` | OK |
| 10 | `grep -n C4a prompts/2026-10-18/730-f20-card.md` | row `C4a` at `:37` (jobs row, plist, `start_cos.sh`) | OK |
| 11 | `tail -n 3 reports/cos-gate-run-2026-10-20.md` | `GATES DONE · ok: 10 · fail: 1 · not run: 3`, as the card says | OK |
| 12 | SMOKE READS row 5 vs `git show main:ops/desk/deploy-smoke.sh`: row form | line is `- cos turn failures · \`grep -c -F "CoS turn FAILED" /Users/cobalt/cobalt/logs/cos.err\` · \`0\``; matches `"- "*" · \`"*`, so it is a smoke-read row. Label `cos turn failures`, not `census`. | OK |
| 13 | row 5: expectation up to the first `;` | `exp=${after_tick#*\`}` then `${exp# · }` then `${exp%%;*}`: the text after the command is ` · \`0\``, and there is no `;` left in the row. The expectation is `` `0` ``, which hits the `` "`"*"`" `` case → `value_is "`0`"`: the last output line must be `0`. A clean file with no match prints `0` (grep -c exits 1, but the `` "`"*"`" `` case does not read `rc`). (Round-1 FAIL 10 closed.) | OK |
| 14 | row 5: command shape | `grep -c -F "CoS turn FAILED" <path>` matches the grep shape: pattern has no `$`, backtick or backslash (spaces are fine inside the quotes); path is unquoted, no blank, none of ``"$`;&|<>()*?\``. | OK |
| 15 | rows 1-4 and both markers vs the same script | rows 1-4: `grep -c -F "<s>" <path>` with `` `0` ``, same form as row 5. Markers: `ls <path>` (before `No such file or directory`, after `listed`) and `grep -c -F … bootstrap-owed.json` (before `1`, after `0`), both in marker form `- \`cmd\` · before … · after …`. Every smoke row is of a mapped form. `--dry-run` not run (no permission); the desk runs it once before first use (script header). | OK |
| 16 | production markers now: `ls …/logs/cos.err`; `grep -c -F "com.cobalt.cos" …/bootstrap-owed.json` | `No such file or directory`; `1`. Both equal the card's `before`. | OK |
| 17 | `deploy-step-c.sh --bootstrap-only` conditions (`:171-198`) | `## LAUNCHD` line `com.cobalt.cos · add · prompts/2026-10-18/730-f20-card.md:C4a · dry run: none` passes the shape awk (`:105-106`); mode is `add`; `ops/com.cobalt.cos.plist` on main carries the Label (`:33,:35` file; plist read by `plist_label`); owed file lists the label | OK |
| 18 | gate items vs `bootstrap-owed.json` (`com.cobalt.cos`, 14 items) | D14, agent stopped, X1, X13, X2, X10, X3, X14, X11, X12, X15, X17, X18, X20. The card has 14 column-0 `GATE RESULT: com.cobalt.cos · <item> · <non-empty>` lines (`grep -c` = 14), item names match; the three `«FILL»` rows are non-empty text, so they admit (his rows, round-1 note stands). | OK |
| 19 | `WAITS:` line | `cos-cutover-tooling DEPLOYED, cos-tunables DEPLOYED, agent retired, hitl.page_base_url set`: names all four. Unmet today (`tunables.yaml` values null, `jobs.yaml:214 enabled: false`); not a fail while unmet. | OK |
| 20 | F-14 listener overlap | `run.py:44-57` refuses while the agent pidfile is live, called at `:147` before `store.register`; the card never touches `com.cobalt.agent` | OK |
| 21 | what blocks the card's own launch beyond WAITS | nothing found (see NOTE 2 for a non-blocking observation) | OK |

## ISSUES

- NOTE 1: BASE `main` trails by desk commits only; not a fail. Round-1 notes 1–4 (TAG/RULINGS `«FILL»`, BASE, `WAITS:` not in `CARD.md`, no restart homes) stand as non-defects.
- NOTE 2: `bootstrap-owed.json` stores the card path `prompts/2026-10-19/808-deploy-f20-cos-card.md` for `com.cobalt.cos`, not 929. `deploy-step-c.sh --bootstrap-only` and `--owed-clear` take the card as an argument and never compare it to that stored path, so it does not block; it is stale metadata.
- NOTE 3: the WAITS items are still unmet (cutover-tooling, tunables, agent retired, `hitl.page_base_url`); the card is ready as written, not yet launchable.

PREFLIGHT DONE · card: cos-bootstrap · checks: 21 · fails: 0 · ready: YES
