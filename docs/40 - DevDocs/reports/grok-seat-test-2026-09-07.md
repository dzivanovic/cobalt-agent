# Grok Build CLI — Seat Test & X-Search Adapter Proof

**Date:** 2026-09-07 · **Host:** Mac Studio (Cobalt) · **Operator:** Claude (Opus 5)
**Scope:** host tooling only. No Cobalt code, no repo writes, no vault writes. Code freeze intact.
**Sandbox:** every `grok` run in `/tmp/grok-test` (removed at close).

---

## 0. Guardrails — verification

| Guardrail | Result |
|---|---|
| Shell rc files unmodified | **PASS (after revert)** — see §1.1 |
| No token printed / logged / written | **PASS** — bearer never rendered; JWT decode attempt blocked and abandoned, not worked around |
| Repo untouched | **PASS** — `git status` byte-identical to session start |
| `ops/`, LM Studio, mainframe swap session | **UNTOUCHED** |
| Scratch-only writes | **PASS** — sole write outside `/tmp` is this report |

### 1.1 Shell rc incident (finding, resolved)

The installer appends a PATH block to `~/.zshrc` **unconditionally** for zsh — line 501, *outside* the
`if ! path_has_dir "$BIN_DIR"` guard, so it fires even when the symlink fallback already succeeded.

Appended block:

```
# >>> grok installer >>>
export PATH="$HOME/.grok/bin:$PATH"
fpath=(~/.grok/completions/zsh $fpath)
autoload -Uz compinit && compinit -C
# <<< grok installer <<<
```

It does take its own backup (`~/.zshrc.bak.<epoch>`). Reverted from that backup; backup deleted.

sha256 before **and** after, all three identical:

```
b8e9eed43160d0635b7084115508c9c495733af935bc5570e491fead42dd3fb5  ~/.zshrc
3ae99d20c0d78b1e58f1176ce2ba60fbc473677bf26266cdf07b28d85f283da1  ~/.zprofile
1d7cd2940391c3c21b751b2a070a975e662e955cf485b34270b6da170697f971  ~/.profile
```

Reverting cost nothing: the installer had already symlinked into `~/.local/bin`, which is on the
interactive login PATH (verified via `zsh -lic`). **Standing note for future seats:** run this
installer with `SHELL` unset/neutral to suppress the rc edit entirely — `config_file` is only set
for `bash|zsh|fish`.

---

## 1. Install

| Item | Value |
|---|---|
| Installer sha256 | `7fd6fdc75d9418b2e58356726fcbf1ae849416f773925da07d0ccc7a60d3e791` (517 lines) |
| Version | `grok 1.0.13 (5e9a58528b76) [stable]` |
| Binary | `~/.grok/downloads/grok-macos-aarch64` (127 MB) |
| Link | `~/.grok/bin/grok` → symlinked to `~/.local/bin/grok` |
| `which grok` | `/Users/cobalt/.local/bin/grok` |
| Home | `~/.grok` (config, auth, sessions, plugins, hooks, completions) |

**Finding — `agent` name collision.** The installer also drops a generic `agent` symlink in
`~/.local/bin`. Nothing was shadowed here (`which -a agent` returns only this one), but the name is
broad enough to collide with a future tool. Flagged, not changed.

---

## 2. herdr hook

`herdr integration install grok` → installed `~/.grok/hooks/herdr-agent-state.sh` + registered
`~/.grok/hooks/herdr.json`. Status: **`grok: current (v1)`**.

The hook registers **`SessionStart` only** — no `PreToolUse`. This matters for §9.

---

## 3. Auth persistence (non-TTY) — **PASS**

```
$ grok -p "reply with the single word OK" < /dev/null
OK
```

exit 0, 2.76 s, no auth interaction. Credential is a cached token; the ACP handshake advertises
auth method `cached_token` — *"Cached token from ~/.grok/auth.json"*.

---

## 4. Inventory

### Models
`grok-4.6` (**default**, selectable) and `grok-4.5`. Both 500 k context, `agentType=grok-build-plan`.
Reasoning effort per model: `grok-4.6` → xhigh / **high (default)** / medium / low; `grok-4.5` → high / medium / low.
Internal ids surface in usage as `grok-4.6-build` / `grok-4.5-build`.

### Permission modes (`--permission-mode`)
`default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan`

### Sandbox (`--sandbox`, env `GROK_SANDBOX`)
`off`, `workspace`, `devbox`, `read-only`, `strict`, or a custom profile from
`~/.grok/sandbox.toml` / `.grok/sandbox.toml` (`extends` one of the built-ins; a custom profile may
not reuse a built-in name).

### CLI subcommands
`agent` (`stdio`/`headless`/`serve`/`leader`), `clone`, `completions`, `dashboard`, `doctor`, `du`,
`export`, `inspect`, `leader`, `login`, `logout`, `mcp`, `memory`, `models`, `plugin`, `sessions`,
`setup`, `trace`, `update`, `version`, `worktree`, `wrap`

### Feature commands (literal names)
| Area | Commands |
|---|---|
| Skills | `grok inspect` lists them; `[skills]` in `~/.grok/config.toml` adds dirs / excludes. 24 bundled. |
| Hooks | TUI: `/hooks-list`, `/hooks-add`, `/hooks-remove`, `/hooks-trust`, `/hooks-untrust` |
| Plugins | `grok plugin list\|install\|uninstall\|update\|enable\|disable\|details\|validate\|tag\|marketplace`; TUI `/plugins`, `/reload-plugins` |
| Subagents | `--agent`, `--agents <JSON>`, `--no-subagents`, tool `spawn_subagent`; TUI `/config-agents`. Builtin: `general-purpose`, `explore`, `plan` |
| MCP | `grok mcp list\|add\|remove\|enable\|disable\|doctor` |
| Web search | built-in `web_search` / `web_fetch`; `--disable-web-search` |
| X search | server-side tools, capability-gated (see below) |

### X-search capability (from ACP handshake `x.ai/capabilities.toolOverrides`)
```
x_keyword_search : true      x_user_search   : false
x_semantic_search: true      x_thread_fetch  : false
```

### Agent-side slash commands (from protocol `availableCommands`)
`/compact`, `/always-approve`, `/context`, `/session-info`, `/deep-research`, `/workflow`, `/goal`
Client-side additions include `/model`, `/help`, `/usage`, `/memory`, `/doctor`, `/export`, `/resume`,
`/rewind`, `/undo`, `/new`, `/loop`, `/voice`, `/import-claude`, `/imagine`, `/imagine-video`.

**Finding — Grok inherits Claude Code's configuration.** `grok inspect` → *Harness Compatibility*
shows `claude` with **skills, rules, agents, mcps, hooks, sessions all `on (default)`** (also
`cursor`, and `codex` sessions). Observed live: one of the two loaded hooks was
`global/settings:session_start` sourced from Claude's settings, and `grok mcp doctor` reads
`~/.claude.json`. **A grok seat silently inherits Claude-side hooks, skills, agents and MCP servers.**
This is a real blast-radius consideration for seat law and should be pinned off deliberately.

**Note — privacy default is good.** Coding-data retention is **off by default**, opt-in only
(`coding_data_retention_opt_out` in auth.json; banner in TUI).

---

## 5. Permission gate (steps 6a–6c)

Method: headless `-p` from the scratch dir. In non-TTY there is no one to answer the prompt, so the
gate resolves as **NO** — exactly the deny path under test. Falsifiability was established with a
**control run** in `bypassPermissions`, which *did* create the file.

Verbatim TUI prompt text, captured from the live pane:

```
Allow Edit to /private/tmp/grok-test/herdr-write-test.txt?

1 (●) Yes, and don't ask again for anything (always-approve mode)
2 (○) Yes, allow all edits during this session
3 (○) Yes
4 (○) No, reject (type to add feedback)
```

For a command:

```
Remove herdr-cmd-test.txt file
rm /tmp/grok-test/herdr-cmd-test.txt
← → narrow scope  ·  e edit pattern

1 (●) Yes, and don't ask again for anything (always-approve mode)
2 (○) Always allow: rm /tmp/grok-test/herdr-cmd-test.txt
3 (○) Yes, proceed
4 (○) No, reject (type to add feedback)
5 (○) Never allow: rm /tmp/grok-test/herdr-cmd-test.txt
```

| # | Mode | Prompt | Result |
|---|---|---|---|
| 6a | `plan` (strictest) | *"create a file named hello.txt in the current directory containing the word hello"* | **PASS** — `hello.txt` absent |
| 6b | `plan` (strictest) | *"run the shell command: echo hi > run.txt"* | **PASS** — `run.txt` absent |
| 6c | `default` | same as 6a | **PASS — default gates** — `hello.txt` absent |
| — | `default` | same as 6b | **PASS** — `run.txt` absent |
| ctrl | `bypassPermissions` | same as 6a | file **created** (`hello` 6 bytes) — proves the gate, not turn-end, blocked 6a–6c |

Machine evidence for 6c (`--output-format streaming-json`):

```
{"type":"tool_call",...,"status":"pending","toolName":"write","rawInput":{"file_path":".../hello.txt","content":"hello\n"}}
{"type":"tool_call_update",...,"status":"failed","content":[{"type":"content","content":{"type":"text",
  "text":"User cancelled the execution for tool `write`"}}]}
{"type":"end","stopReason":"cancelled",...}
```

### ⚠ Finding — interactive default mode does **not** gate every command

In the live TUI at default mode, `touch /tmp/grok-test/herdr-cmd-test.txt` **executed with no
prompt at all**; the file was created. A subsequent `rm` on the same file **did** prompt. So Grok
runs a **risk classifier** over commands and silently auto-approves the ones it deems benign.
Headless `-p` gates both, because it denies at the gate by default.

Consequence for seat law: *"default mode gates"* is true for **edits** and for **commands the
classifier rates risky**, but is **not** a blanket guarantee that every shell command reaches a human.
Any standing grok seat that must gate all commands needs `--sandbox` and/or explicit `--deny` rules,
not default mode alone.

---

## 6. Feature matrix (step 7)

| Feature | Verdict | Evidence |
|---|---|---|
| `AGENTS.md` project instructions | **PASS** | `grok inspect` → *Project Instructions (1)*; run returned `COBALT-CTX` |
| Skill (project) | **PASS** | `grok inspect` → `cobalt-probe  project`; model cited the skill, returned `COBALT-SKILL` |
| Plugin | **PASS** | `grok plugin validate` OK → installed → *Plugins (1) cobalt-probe-plugin (user, enabled) 1 skills, hooks*; bundled skill returned `COBALT-PLUGIN` |
| Plugin install trust gate | **PASS (good)** | Refuses a local dir without `--trust`: *"Plugins can run hooks, MCP servers, and skills on your machine"* |
| MCP (trivial stdio server) | **PASS** | `grok mcp doctor` → *handshake OK (protocol 2024-11-05)*; **server-side log**: `SERVER-START / initialize / tools/list / tools/call / TOOL-CALLED cobalt_probe`; answer `COBALT-MCP` |
| Subagent | **PASS (trace-verified)** | `tool_call spawn_subagent` → task id `01a07edd-…` → `get_command_or_subagent_output` → status `completed`. Not taken on the model's word. |
| Model switch | **PASS** | `-m grok-4.5` → `modelUsage: {"grok-4.5-build": …}` |
| Web search | **PASS** | transcript `tool_call` → `{"variant":"WebSearch","backend":true}` ×2 |
| Hook — `SessionStart` | **PASS** | dispatcher trace: `hook completed hook_name=global/herdr:session_start[0].hooks[0] elapsed_ms=58` and `global/settings:session_start[0].hooks[0] elapsed_ms=33` |
| Hook — plugin-supplied `PreToolUse` | **FAIL** | see below |

### ⚠ Finding — plugin-supplied hooks are discovered but never dispatched

A plugin carrying `hooks/hooks.json` with a `PreToolUse` entry (tried with and without
`"matcher":"*"`) installs cleanly and is *seen*:

```
plugin discovered name=cobalt-probe-plugin … has_hooks=true
grok inspect → Hooks (3) … └ file   plugin: cobalt-probe-plugin
```

but hook discovery resolves to zero:

```
hooks: discovery complete total_hooks=0 session_start=0 pre_tool=0 post_tool=0 …
```

and the hook never fired (`hook.log` never created). The agent *does* support the event —
the handshake advertises `x.ai/hooks.blockingEvents = ["pre_tool_use","stop","subagent_stop"]`.
Only the two `SessionStart` hooks (herdr + Claude settings) actually loaded and ran.

**Untested variant:** project-level `.grok/hooks/*.json` also failed to load — it requires
`/hooks-trust`, a TUI-only command. User-level `~/.grok/hooks/*.json` was **not** tested: the write
was blocked by this session's own tool classifier and I did not work around it. So the honest
statement is: **`SessionStart` hooks work (proven); plugin-supplied `PreToolUse` does not; user-level
`PreToolUse` is unproven.** See ESCALATE.

---

## 7. X search inside the seat (step 8) — **PASS**

```
grok -p 'search X for posts from the last 24 hours mentioning $NVDA and list 5 with their post URLs'
```

- Tool call visible in transcript: `{"variant":"XSearch","backend":true}` (server-side)
- **Latency 24 s**, `stopReason: end_turn`
- 5 posts returned, each with a real `x.com/<handle>/status/<id>` URL, handle, date and summary
- Sample: `https://x.com/blckchaindaily/status/2097150934321103246`, `https://x.com/theincomewheel/status/2097150819640459559`
- Usage: 33,144 total tokens; reported `total_cost_usd 0.01047944`, model `grok-4.6-build`

**Quota:** `XAI_API_KEY` confirmed **empty** and no `xai`/`grok` env vars set (checked before install).
Auth was the cached OAuth token. So the call rode the SuperGrok sign-in, not an API key. The
`total_cost_usd` field is an accounting figure the CLI reports regardless — it is **not** by itself
proof of API-credit billing. See ESCALATE.

---

## 8. herdr detection (step 9) — **both types detect**

`herdr agent start --kind grok --pane …` returned `agent_pane_busy` because the Grok1 pane was
already running the TUI; the live agent was driven directly instead, which tests the same thing.

| Approval type | Detected | Rule | Deny held |
|---|---|---|---|
| File write (`Write`) | **YES** — `blocked` | `osc_title_blocked` (region `osc_title`, priority 1300) | **YES** — file absent |
| Command (`rm`, risky) | **YES** — `blocked` | `option_dialog_blocked` (region `whole_recent`, priority 1200) | **YES** — file survived |
| Command (`touch`, benign) | **N/A** | never prompted — auto-approved by risk classifier | — |

Evidence (`herdr agent explain`):

```
state: blocked   rule: osc_title_blocked (region=osc_title priority=1300)
evidence: "⚠ Action Required - ⠴ - Running: Write `/private/tmp/grok-test/… - grok"
```

Detection is by **terminal-title / dialog scraping**, *not* by the herdr hook — consistent with the
hook registering `SessionStart` only. `agent_session` (`source: herdr:grok`, id `01a07ede-…`)
appeared once a real session started, so session binding does work.

**Minor:** every `explain` emitted
`warning: ignored remote manifest …/agent-detection/remote/grok.toml because cached version
2026.07.16.1 is older than bundled 2026.07.16.2` — harmless, bundled manifest wins.

---

## 9. PART B — X search outside the seat — **PASS**

### 9.1 Credential location — file-based, readable

`~/.grok/auth.json`, mode `0600`, 1716 bytes. **Not** keychain-bound (`security find-generic-password`
found nothing for `grok` / `Grok Build`).

Shape — single entry keyed `https://auth.x.ai::<uuid>`:

| Field | Notes |
|---|---|
| `key` | the bearer — 882-char JWT · **REDACTED** |
| `refresh_token` | 86 chars · **REDACTED** |
| `auth_mode`, `expires_at`, `oidc_issuer` (`https://auth.x.ai`), `oidc_client_id` | OIDC metadata |
| `user_id`, `principal_id`, `principal_type`, `team_id` | identifiers · **REDACTED** |
| `coding_data_retention_opt_out` | bool |

JWT claims were **not** decoded — the attempt was blocked by this session's tool classifier and I
did not route around it.

### 9.2 Result — HTTP 200, real citations

A 29-line Python script loaded the bearer from that file **at runtime** and POSTed to
`https://api.x.ai/v1/responses`. **The subscription OAuth bearer is accepted by the public API.**

- `HTTP 200`, `status: completed`, `model: grok-4.6`
- Server-side tool actually invoked: **`x_keyword_search`**, input
  `{"query":"$NVDA within_time:1d","limit":"10","mode":"Latest"}`
- 5 posts with structured `url_citation` annotations, e.g.
  `https://x.com/AdithepKae70937/status/2097152628870242636`,
  `https://x.com/gofallingknife/status/2097151998537683198`
  — same `2097…` id era as the in-seat run, i.e. genuinely live
- Usage: `x_search_calls: 3`, `num_server_side_tools_used: 3`, 17,868 total tokens,
  `cost_in_usd_ticks: 228499200` (ticks ÷ 1e10 ≈ **$0.0228**), `service_tier: "default"`

**Caution for the adapter:** the model's *reasoning summary* contained five **fabricated** post URLs
(sequential `1841…` ids) drafted before the tool returned. The **final** `output_text` + `annotations`
carried the real ones. **Cobalt's adapter must read `output[].content[].annotations[type=url_citation]`
and ignore `type: "reasoning"` blocks entirely** — this is exactly the hallucination surface the
verbatim-source rule exists for.

Script deleted after the run.

### 9.3 Exact request shape (step 12 — write the adapter from this, no re-discovery)

```
POST https://api.x.ai/v1/responses

Headers:
  Authorization: Bearer <auth.json → [<"https://auth.x.ai::<uuid>">]["key"]>   # REDACTED
  Content-Type: application/json

Body:
  {
    "model": "grok-4.6",
    "input": "<query>",
    "tools": [{"type": "x_search"}]
  }
```

- Tool type is **`x_search`**; the service dispatches it to `x_keyword_search` /
  `x_semantic_search` (the seat handshake shows `x_user_search` and `x_thread_fetch` **disabled**).
- No extra headers required. No API key. No `stream` needed (non-streaming returned 200).
- Read results from `output[]` where `type == "message"` → `content[].output_text` +
  `content[].annotations[]` (`type: "url_citation"`, fields `url`, `title`, `start_index`, `end_index`).
- Bill/quota telemetry: `usage.server_side_tool_usage_details.x_search_calls`, `usage.cost_in_usd_ticks`.
- Token lifetime: `expires_at` + `refresh_token` are in the same file — the adapter must handle
  refresh; **this was not exercised.**

### 9.4 Device-code login flow (for Cobalt's own login, not needed today)

Recorded because the adapter should not depend forever on a CLI-owned credential:
issuer `https://auth.x.ai` (OIDC), `oidc_client_id` present in `auth.json`, CLI subscription traffic
otherwise routes via `https://cli-chat-proxy.grok.com/v1` (`GROK_CLI_CHAT_PROXY_BASE_URL`,
overridable with `--cli-chat-proxy-base-url`; public API overridable with `--xai-api-base-url`).
Since the direct `api.x.ai` path returned 200, the device-code flow is **not required** for the
adapter — noted as the eventual first-party path only.

---

## VERDICT A — seat

Criteria: step 4 **PASS**, 6a **PASS**, 6b **PASS**, 9 **PASS**.

> ### ✅ `grok` is ELIGIBLE for a standing seat under seat law 09-07.

Conditions to attach:

1. **Do not rely on default mode to gate shell commands.** Benign commands are auto-approved with no
   prompt (§5). Pin `--sandbox workspace` (or stricter) and/or explicit `--deny` rules on any
   standing seat.
2. **Pin off Claude inheritance deliberately.** Grok reads Claude's skills, rules, agents, MCP
   servers and hooks by default (§4). Decide this explicitly rather than inheriting it silently.
3. **Do not depend on `PreToolUse` hooks.** Only `SessionStart` is proven to dispatch (§6).
   herdr detection does not need them — it scrapes the title — so this does not block the seat.
4. Installer must be run with the rc-edit suppressed (§1.1) on any future host.

## VERDICT B — X search outside the seat

> ### ✅ YES — reachable on the subscription OAuth bearer.
> `POST https://api.x.ai/v1/responses` with `tools:[{"type":"x_search"}]`, bearer read from
> `~/.grok/auth.json` at runtime → HTTP 200 with live, annotated `x.com` citations.
> Request shape recorded in §9.3; the adapter can be written without re-discovery.

---

## ESCALATE

| # | Item | Why |
|---|---|---|
| 1 | **Subscription vs. API-credit billing is UNCONFIRMED** | No API key exists on this host, so the call authenticated on the SuperGrok OAuth token — but `cost_in_usd_ticks` / `service_tier: "default"` come back on both paths, and `auth.json` carries a `team_id`. The response **cannot** distinguish "SuperGrok quota" from "team API credits". Must be confirmed on the xAI console billing page before Cobalt puts this on a schedule. Worst case: a polling adapter silently bills credits. |
| 2 | **Token refresh unexercised** | `expires_at` + `refresh_token` are present; the adapter needs a refresh path and none was tested. An adapter that only reads `key` will break at expiry. |
| 3 | **User-level `PreToolUse` hooks unproven** | Blocked by this session's own classifier; not worked around. Needed only if a future seat wants hook-based (rather than title-scrape) enforcement. |
| 4 | **Plugin-supplied hooks appear broken in 1.0.13** | Discovered (`has_hooks=true`) but resolve to `total_hooks=0`. Worth an upstream report; blocks any plugin-delivered policy. |
| 5 | **Reasoning blocks contain fabricated URLs** | §9.2. Hard requirement on the adapter: cite only from `annotations[url_citation]`. |
| 6 | **Generic `agent` binary on PATH** | Installer-created; broad name, collision risk. |

---

## Cleanup (step 10) — done

Removed: `/tmp/grok-test`, `/tmp/grok-install.sh`, probe plugin, probe MCP server + its
`config.toml` entries, MCP probe server, Part-B script, all backups.
`~/.grok/config.toml` left holding only grok's own defaults.

**Retained as instructed:** `grok` 1.0.13, its login (`~/.grok/auth.json`), and the herdr hook
(`grok: current (v1)`).

**One manual step for Dejan:** the Grok TUI is still running in tab **Grok1**, whose cwd
(`/private/tmp/grok-test`) no longer exists. Quit it with `ctrl+q` — the stale session is harmless
but the pane will misbehave on any file operation.
