# Gate run: F20 `com.cobalt.cos`, first pass (2026-10-19)

Seat `cos-gate-run`, prompt `prompts/2026-10-19/873-cos-gate-run.md`. Main `1c96c032`. Dev, no `COBALT_ENV`. `com.cobalt.cos` left unloaded. No launchctl, no keychain read, no DM, no service touched.

## RESULTS
```
GATE RESULT: com.cobalt.cos · D14 · NOT RUN — his decision, written from his ruling's R row by the desk
GATE RESULT: com.cobalt.cos · agent stopped · NOT RUN — his decision, written from his ruling's R row by the desk
GATE RESULT: com.cobalt.cos · X1 · OK (shell, not under a LaunchAgent)
GATE RESULT: com.cobalt.cos · X13 · FAIL — exit 0, but the output is not the word OK alone; the CLI's first line: "Permission deny rule (.claude/settings.local.json): Bash(git push*:*) mixes * with the trailing :* prefix syntax, so it is matched as a literal prefix (the * is not expanded) and matches only commands containing a literal * at that position. Use Bash(git push*) for wildcard matching."
GATE RESULT: com.cobalt.cos · X2 · NOT RUN — no allowed probe: a live scratch session told to run Bash, write and Read outside scratch needs a script
GATE RESULT: com.cobalt.cos · X10 · NOT RUN — no allowed probe: a real spawn with a planted user-config MCP server cannot be spelled without a script
GATE RESULT: com.cobalt.cos · X3 · OK (named tests, fake client and stub CLI; U4's real stream shape not recorded)
GATE RESULT: com.cobalt.cos · X14 · NOT RUN — no allowed probe: 20 real sessions on the cos.yaml model need a script; cos.max_turns 30 and cos.turn_timeout_s 900 stand unmeasured
GATE RESULT: com.cobalt.cos · X11 · NOT RUN — no allowed probe: a real spawn with a planted user-config MCP server cannot be spelled without a script
GATE RESULT: com.cobalt.cos · X12 · OK (named test, fake SDK client; the real CLI spawn not observed)
GATE RESULT: com.cobalt.cos · X15 · NOT RUN — waits for his word
GATE RESULT: com.cobalt.cos · X17 · NOT RUN — no allowed probe: the Sonnet/Opus comparison on 20 real sessions needs a script
GATE RESULT: com.cobalt.cos · X18 · OK — 3 deploy logs since 2026-10-15, no restart: median 23 s, max 43 s
GATE RESULT: com.cobalt.cos · X20 · NOT RUN — no allowed probe: no test on main runs redact() on a line carrying #k=<hex> (tests/cobalt/test_hitl_offline.py:141 asserts the fragment in the text BEFORE redaction only); a new test is a build card's
```

## DECISIONS
- ASK DESK (for Dejan): Today the old agent (com.cobalt.agent) runs your Mattermost DM listener, the scheduler, the Scribe and the memory layer; may it stop after your trading day, with each of those four moved to a named new-core job or retired (you name which), and will you tap one test link on your phone so we read that the page sees its #k= key?
- ASK DESK: X13 FAIL — the model replied `OK` (last line, exit 0), but the CLI printed a settings warning first: `.claude/settings.local.json` holds a deny rule `Bash(git push*:*)` the CLI says matches only a literal `*`, so that `git push` deny may not bite. Fix the rule to `Bash(git push*)` and re-run X13 under a probe that reads stdout only, or rule the warning out of the output? Default: cos stays unloaded; X13 does not count. [16:12]
- ASK DESK: X2 NOT RUN (no allowed probe). Default: cos stays unloaded. [16:12]
- ASK DESK: X10 NOT RUN (no allowed probe). Default: cos stays unloaded. [16:12]
- ASK DESK: X11 NOT RUN (no allowed probe). Default: cos stays unloaded. [16:12]
- ASK DESK: X14 NOT RUN (no allowed probe). Default: cos stays unloaded. [16:12]
- ASK DESK: X15 NOT RUN (waits for his phone read). Default: cos stays unloaded. [16:12]
- ASK DESK: X17 NOT RUN (no allowed probe). Default: cos stays unloaded. [16:12]
- ASK DESK: X20 NOT RUN (no test runs redact() on a `#k=<hex>` line). Default: cos stays unloaded. [16:12]
- ASK DESK: D14 and `agent stopped` NOT RUN (his decision). Default: cos stays unloaded. [16:12]
- ASK DESK: X1 `OK (shell, not under a LaunchAgent)` leaves unproven that the CLI is logged in when launchd runs it. Default: the line does not count for the bootstrap card. [16:12]
- ASK DESK: X3 `OK (named tests, …)` leaves unproven the real CLI's stream shape on timeout, max turns and no result (U4). Default: the line does not count for the bootstrap card. [16:12]
- ASK DESK: X12 `OK (named test, …)` leaves unproven the env a real CLI spawn receives. Default: the line does not count for the bootstrap card. [16:12]
- ASK DESK: X14 unmeasured beside `cos.max_turns` 30 and `cos.turn_timeout_s` 900: no real session sized them. Default: the shipped values stand until the desk rules. [16:12]
- Note: X18's spans are bootout `<t down>` to the report's own `<t up>` line (after bootstrap), not a first `/api/health` 200; none of the three reports states one for aset.

## RECORDS

### Step 0
- `date` → `Mon Oct 19 16:11:11 EDT 2026`
- `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `1c96c032`

### Step 1 — X20
Nothing run.

### Step 2 — X11, X10 (evidence only)
`uv run cobalt cos run --dry-run` (exit 0), whole:
```
{'tools': [], 'allowed_tools': ['mcp__cobalt__cards_open', 'mcp__cobalt__radar_pool', 'mcp__cobalt__jobs_status', 'mcp__cobalt__hitl_list', 'mcp__cobalt__agents_list', 'mcp__cobalt__request_action', 'mcp__cobalt__draft_agent'], 'disallowed_tools': ['Bash', 'BashOutput', 'KillShell', 'Write', 'Edit', 'MultiEdit', 'NotebookEdit', 'WebFetch', 'WebSearch', 'Task', 'Agent', 'Read', 'Grep', 'Glob', 'LS', 'TodoWrite', 'ExitPlanMode', 'Skill', 'SlashCommand', 'ListMcpResourcesTool', 'ReadMcpResourceTool'], 'setting_sources': [], 'strict_mcp_config': True, 'permission_mode': 'dontAsk', 'env': {'PATH': '/Users/cobalt/cobalt/.venv/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/Users/cobalt/.orbstack/bin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/Users/cobalt/.local/bin:/Users/cobalt/.lmstudio/bin:/Users/cobalt/.lmstudio/bin', 'HOME': '/Users/cobalt', 'USER': 'cobalt', 'LANG': 'en_US.UTF-8'}, 'cwd': '/Users/cobalt/cobalt/data/cos/scratch', 'model': '(cos.yaml)', 'max_turns': 0, 'resume': None, 'system_prompt': '(cos.yaml)'}
```
- `setting_sources`: `[]` · `strict_mcp_config`: `True` · `permission_mode`: `dontAsk`
- `allowed_tools`: the seven `mcp__cobalt__*` tools above · `disallowed_tools`: the 21 names above (Bash, Write, Edit, Read among them)
- `env` names: `PATH`, `HOME`, `USER`, `LANG`

`uv run pytest tests/cobalt/test_cos_offline.py::test_options_allowlist_disallowed_mode_settings`, whole:
```
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/cobalt/cobalt
configfile: pyproject.toml
plugins: anyio-4.12.1, asyncio-1.3.0, logfire-4.22.0
asyncio: mode=Mode.AUTO, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1 item

tests/cobalt/test_cos_offline.py .                                       [100%]

============================== 1 passed in 0.08s ===============================
```

### Step 3 — X12
`uv run pytest tests/cobalt/test_cos_offline.py::test_spawn_env_is_the_allowlist`, whole:
```
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/cobalt/cobalt
configfile: pyproject.toml
plugins: anyio-4.12.1, asyncio-1.3.0, logfire-4.22.0
asyncio: mode=Mode.AUTO, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1 item

tests/cobalt/test_cos_offline.py .                                       [100%]

============================== 1 passed in 0.04s ===============================
```

### Step 4 — X3
`uv run pytest tests/cobalt/test_cos_offline.py::test_hang_max_turns_no_result_each_fail_and_dm tests/cobalt/test_cos_offline.py::test_check_o6_a_hung_connect_is_inside_the_turn_timeout tests/cobalt/test_cos_offline.py::test_max_turns_leaves_no_descendant_alive_and_the_resident_stands tests/cobalt/test_cos_offline.py::test_max_turns_leaves_no_orphaned_descendant_alive`, whole:
```
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/cobalt/cobalt
configfile: pyproject.toml
plugins: anyio-4.12.1, asyncio-1.3.0, logfire-4.22.0
asyncio: mode=Mode.AUTO, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 4 items

tests/cobalt/test_cos_offline.py ....                                    [100%]

============================== 4 passed in 0.43s ===============================
```

### Steps 5, 6 — X14, X17
Nothing run.

### Step 7 — X1, X13
`claude auth status` · exit 0 · first non-empty line `{` · whole:
```
{
  "loggedIn": true,
  "authMethod": "claude.ai",
  "apiProvider": "firstParty",
  "analyticsDisabled": false,
  "projectsDirectory": "/Users/cobalt/.claude/projects",
  "configDirectory": "/Users/cobalt/.claude",
  "email": "dejan.kenkyukai@gmail.com",
  "orgId": "7520aad4-5b47-44d5-b69d-000abd60edc8",
  "orgName": "dejan.kenkyukai@gmail.com's Organization",
  "subscriptionType": "max"
}
```
`"loggedIn": true` → X1 logged in.

`claude -p --model claude-sonnet-5-5 'Reply with exactly the word OK'` · exit 0 · first non-empty line is the settings warning · whole:
```
Permission deny rule (.claude/settings.local.json): Bash(git push*:*) mixes * with the trailing :* prefix syntax, so it is matched as a literal prefix (the * is not expanded) and matches only commands containing a literal * at that position. Use Bash(git push*) for wildcard matching.
OK
```
The tool output merges stdout and stderr, so it cannot show which stream carried the warning.

### Step 8 — X2
Nothing run. Static evidence is step 2's options test; no result rests on it.

### Step 9 — X18
Read: Grep `bootout gui/501/com.cobalt.aset` in `reports/deploy-*.md` → 39 files. Dates read from titles, tags and `date` lines; three ran on or after 2026-10-15:
- `deploy-jev-shadow-1015.md` · 19 s · com.cobalt.aset — attempt 2 (the deploy): `:306` `<t down>` = Thu Oct 15 18:25:45 EDT 2026; `:311` `<t up>` = Thu Oct 15 18:26:04 EDT 2026, "Downtime 19 s" (`:334`). Attempt 1 also booted aset out, failed at 4.2 and brought it back on the old tree: `:229` "aset down 18:18:33 → up 18:19:05 (32 s)". Not counted, since only one span per report is listed.
- `deploy-f23-playbook.md` · 43 s · com.cobalt.aset — `:178` `Sun Oct 18 13:54:13 EDT 2026` = `<t down>`; `:188` `Sun Oct 18 13:54:56 EDT 2026` = `<t up>` · downtime 43 s.
- `deploy-f20-cos-attempt2.md` · 23 s · com.cobalt.aset — `:224` `<t down>` `Mon Oct 19 06:23:37 EDT 2026`; `:236` `<t up>` `Mon Oct 19 06:24:00 EDT 2026`. Downtime 23 s.

Spans 19, 23, 43 s → median 23 s, max 43 s. With jev attempt 1's 32 s counted too, the median would be 27.5 s and the max still 43 s.

### Times
- run start `date`: Mon Oct 19 16:11:11 EDT 2026 · report written after `date`: Mon Oct 19 16:12:09 EDT 2026

GATES DONE · ok: 4 · fail: 1 · not run: 9
