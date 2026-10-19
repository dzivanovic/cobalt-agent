# draft-cos-probe — 2026-10-19

## §0 Headline
- WROTE `prompts/2026-10-19/877-cos-probe-card.md`, job `cos-probe-1019`, BASE `07eb89a3`, BAND HIGH, RULINGS `2026-10-18 R1863`. Rows: P1 `cobalt cos probe <item>` (7 items), P2 the probe's stub tests plus the unknown-item control, A1 `claude auth status`, X20 the redaction test, R1 restarts, D0 docs.
- Auth subcommand: `claude auth status` (from `claude auth --help`, 16:11).
- X20: by reading, `redact()` leaves `#k=<hex>` intact today. The FINAL counts that as a pass, so the test is the CONTROL. The prompt's "removes the hex" is decision 1.
- RESTARTS was read from `classify`, not run: `com.cobalt.radar`. Committed nothing.

## DECISIONS
1. ASK DESK: the prompt says the X20 test checks that `redact()` "removes the hex". The FINAL says the opposite: "redacted → the link is broken in the DM; B's carrier changes" (`F20-FINAL-2026-10-11.md:82`). Default: the test asserts the key survives (`test_x20_redact_keeps_the_card_fragment_key`). By reading it is green today, so it is the control. [16:16]
2. ASK DESK: X2 and X10 share one design line (`:91`). The design does not say which of the four checks (Bash, write, Read outside scratch, planted MCP tool) belongs to which item. Default: both items run all four checks. [16:16]
3. ASK DESK: under X3 (`:86`), a dead child that goes unseen changes the design ("the timeout kill is the detection"). The design does not call it a deploy stop. Default: FAIL unless the killed-subprocess turn fails for a reason other than the timeout. [16:16]
4. ASK DESK: X14 (`:86`) is a measurement and has no pass rule. Default: OK iff all 20 constructed DMs end `ok` within the shipped `cos.max_turns` and `cos.turn_timeout_s`. The clause prints the measured maximums. [16:16]
5. ASK DESK: X17 (`:87`) says "a worse count for Sonnet" but does not define the count. Default: the number of the 20 DMs that end `ok`. OK iff Sonnet's count ≥ Opus's. [16:16]
6. ASK DESK: the probe runs with a scratch `HOME`. It is not proven that the CLI can see his subscription login (keychain or files) from there. Reading or copying his login is out of bounds. Default: row A1 runs `claude auth status` under the scratch HOME, and a non-zero exit gives `PROBE <item> FAIL auth`. If that is the result, the desk rules on the route (for example a `claude setup-token` token, which would add an env name beyond `ALLOWED_ENV`). [16:16]
7. ASK DESK: for X12 the probe reads the real child's env with `ps -E -ww -o command= -p <pid>` and parses names only. It is not proven that macOS `ps` shows another process's env. Default: an unreadable env → FAIL `env unreadable`. The probe's own env is cut to `ALLOWED_ENV` plus the two constructed dummies, so no real secret can reach the child or the reader. [16:16]
8. ASK DESK: the "browser-type MCP server" for X11 and X10 is a `sys.executable` stub named `browser` that only writes a marker in scratch. No real browser server is installed. Default: the stub. [16:16]
9. ASK DESK: the prompt asks for `cobalt jobs restarts` output. The drafter did not run it: it is not on this seat's list, and `uv run` in `/Users/cobalt/cobalt` may sync the production venv. The new files do not exist yet, so no range covers them. Default: the header `RESTARTS: com.cobalt.radar` comes from reading `classify`, and builder row R1 records the tool's line. [16:16]
10. ASK DESK: the prompt does not give these header values: BRANCH `ops/cos-probe-1019`, WORKTREE `cos-probe-1019`, REPORT, `CLASS: K2`, `INSTALL: none`, `HOUSE B: as needed`. Default: taken from the shape of card 730. No `DB:` key, because the rows touch `src/`. [16:16]

## RECORDS
- `date` 16:11:27 EDT at start, 16:14 card written, 16:16 report.
- `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `07eb89a3`.
- `git diff --stat main -- src/cobalt tests/cobalt configs/cobalt/redact.yaml "docs/30 - Design/F20-FINAL-2026-10-11.md"` plus the 808 and 873 cards → nothing.
- `claude --help` and `claude auth --help` at 16:11. Quoted in the card's `## RECORDS`.
- Read: prompt 876; `areas/cobalt.md`; `prompts/CARD.md`; card 730 whole; `topics/writing-rules.md`; `reports/draft-cos-gate-amend-2026-10-19.md`; `BUILD-HUB.md:14-79`.
- `git show main:` read: `808-deploy-f20-cos-card.md` (line 21); `F20-FINAL-2026-10-11.md` (`:60-104`); `src/cobalt/cos/cli.py`; `src/cobalt/cos/session.py`; `tests/cobalt/test_hitl_offline.py`; `src/cobalt/hitl/card.py`; `src/cobalt/redact/{guard,secrets,__init__}.py`; `configs/cobalt/redact.yaml`; `configs/cobalt/agents/cos.yaml`.
- On-disk reads, equal to main by the empty diff above: `src/cobalt/jobs/restarts.py:120-264`. Grep: `cli.py` cos lines (`:87-89`, `:554-556`, `:559`); `test_cos_offline.py` test lines; `#k=` sites; `jobs.yaml` resident `imports:`; `cos/run.py` imports; `jobs/cli.py` restarts args; `cto-2026-10-18.md:90` R1863.
- `reports/cos-gate-run-2026-10-19.md`: absent at 16:11 (`ls`).
- Wrote only `877-cos-probe-card.md` (Write, one Edit `:36`→`:34`) and this report. Nothing run but reads and the two help commands.

DRAFTED · decisions: 10
