# Antigravity CLI (`agy`) — herdr seat validation

**Date:** 2026-09-07 · **Host:** Mac Studio (darwin 15.7.9, arm64) · **Operator:** Claude (Opus 5)
**Scope:** host tooling only. No Cobalt code touched, no repo commits, no vault writes. Code freeze intact.
**Test root:** `/tmp/agy-test` (== `/private/tmp/agy-test`), deleted at close.

---

## VERDICT

| Gate | Result |
| :-- | :-- |
| STEP 4 — auth persistence | **PASS** |
| STEP 6a — file-write gate | **PASS** |
| STEP 6b — shell-command gate | **PASS** |
| STEP 7 — herdr blocked detection | **PARTIAL — command approvals detected, file-write approvals NOT** |

**Ruling: agy is eligible for a standing seat (seat law 09-07) with one supervision caveat.**

Seat law requires 4 + 6a + 6b + 7. Three pass outright; STEP 7 passes only for *command* approvals.
The failure is a **supervision gap, not a safety gap** — the permission gate itself holds in every case
tested (nothing was created or executed without explicit approval). What fails is herdr's *visibility*:
when agy is waiting on a **file-edit approval**, `herdr agent list` reports `idle`, so the pane will not
surface as blocked and Dejan will not be pinged. Until herdr's agy detection manifest is updated,
**do not rely on the herdr status column to notice agy file-approval prompts.**

If seat law is read strictly (7 must pass unqualified), agy is scratch/worktree-eligible today and
becomes standing-seat-eligible the moment the manifest is fixed. That call is Dejan's.

---

## 1. Install

The URL in the task brief — `https://antigravity.google/install.sh` — **404s; no such file exists.**
The vendor-documented installer (via `antigravity.google/llms.txt` → `docs/cli/install`) is:

```
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

| Item | Value |
| :-- | :-- |
| Installer sha256 | `ee1ea43ce4e9e56356c4ab6dad907ef357ae4bdfcaadb682735909fb57c9c640` |
| Version | **1.1.27** |
| Install path | `/Users/cobalt/.local/bin/agy` (Mach-O arm64, 177 MB) |
| Config home | `~/.gemini/` (`config/` + `antigravity-cli/`) |

Installer reviewed in full before execution: it resolves a Google manifest, downloads from
`storage.googleapis.com/antigravity-public`, **verifies sha512 against the manifest** and aborts on
mismatch, then clears the macOS quarantine xattr. The shell script itself writes no shell profiles.

### ⚠ Shell-profile edits (made by the installer, reverted by me)

The script's native handoff (`agy install`) appended a PATH block to **three** files:

```
# Added by Antigravity CLI installer
export PATH="/Users/cobalt/.local/bin:$PATH"
```

…to `~/.zshrc`, `~/.zprofile` and `~/.profile`. The brief forbids editing `~/.zshrc`, and the block was
redundant — `~/.local/bin` was already on PATH via `~/.zshrc` line 2 (`. "$HOME/.local/bin/env"`).
All three were reverted. Proof: `~/.zshrc` sha256 = `b8e9eed43160d0635b7084115508c9c495733af935bc5570e491fead42dd3fb5`
both before and after; zero `Antigravity` lines remain in any of the three.

**For future installs:** `agy install --skip-path --skip-aliases` suppresses this. (Documented, but not
listed in the bootstrap script's own `--help`.)

---

## 2. herdr hook

```
antigravity-cli: current (v2) (/Users/cobalt/.gemini/config/hooks/herdr-agent-state.sh)
```

**Ordering note:** `herdr integration install antigravity-cli` fails with
`antigravity cli config directory not found at /Users/cobalt/.gemini/config` until agy has been run once.
Install order is therefore **agy → first run → herdr integration install**, not the order in the brief.

The hook registers as a global `PreInvocation` entry in `~/.gemini/config/hooks.json`. Its own comments
state it reports session identity only, and that **lifecycle state comes from herdr's screen detection** —
which is exactly where STEP 7 fails.

---

## 3. STEP 4 — auth persistence · **PASS**

Negative control first (pre-auth, same shell): `agy -p` printed `Authentication required`, an OAuth URL,
then `Error: authentication failed or timed out`. So the test can fail.

After Dejan's interactive sign-in, from this non-TTY shell:

```
$ agy -p "reply with the single word OK"
OK
[exit=0]   stderr: empty   auth prompts: 0
```

Credentials persist via the macOS Keychain. Headless runs reuse them silently.

---

## 4. STEP 5 — inventory (literal names)

### Permission / mode flags
| Flag | Meaning |
| :-- | :-- |
| `--mode` | `accept-edits`, `plan` (default when unset = `default`, internally `request-review`) |
| `--dangerously-skip-permissions` | auto-approve all tool permission requests (`permission_mode: always-proceed`) |
| `--sandbox` | run with terminal restrictions enabled |
| `--effort` | `low` / `medium` / `high` |
| `--add-dir`, `--model`, `--agent`, `--project`, `--new-project`, `--json-schema` | session/workspace scoping |
| `-p` / `--print` / `--prompt`, `-i` / `--prompt-interactive`, `-c` / `--continue`, `--conversation` | run modes |
| `--input-format` / `--output-format` (`text`, `json`, `stream-json`), `--print-timeout`, `--disable-slash-commands`, `--log-file` | headless plumbing |

**There is no mode stricter than `default`.** The cycle is `default → accept-edits → plan` (Shift+Tab).
Additional tightening is only via permission rules in `~/.gemini/antigravity-cli/settings.json`
(`deny` > `ask` > `allow`; actions `read_file`, `write_file`, `read_url`, `execute_url`, `command`,
`unsandboxed`, `mcp`, each with `(target)` or `(*)`).

### Subcommands
`agent`/`agents`, `changelog`, `help`, `install`, `mcp` (`add`/`remove`/`list`/`enable`/`disable`),
`mic-serve`, `models`, `plugin`/`plugins` (`list`/`import`/`install`/`uninstall`/`enable`/`disable`/`validate`/`link`),
`remote-control` (`start`/`status`/`stop`), `update`.

### Slash commands (46 total)
`/add-dir` `/agents` `/artifact` `/btw` `/changelog` `/clear` (`new`) `/codesearch` (`cs`,`search`)
`/config` (`settings`) `/context` `/copy` `/credits` `/diff` `/effort` `/exit` (`quit`) `/feedback`
`/fork` (`branch`) `/help` `/hooks` `/keybindings` `/logout` `/mcp` `/model` `/open` `/permissions`
`/rename` `/resume` (`switch`,`conversation`) `/rewind` (`undo`) `/skills` `/statusline` `/tasks`
`/title` `/usage` (`quota`) `/voice` (`record`) `/goal` `/schedule` `/browser` `/plan` `/grill-me`
`/teamwork-preview` `/learn` `/boost` — plus built-in skills surfaced as commands:
`/agy-customizations` `/antigravity-guide` `/migrate-workflows` `/permissioned-github` (+ `generative_ui`).

**Mapping to the brief's terms:** plan → `--mode=plan` / `/plan`; auto → `--mode=accept-edits`;
skip-permissions → `--dangerously-skip-permissions`; **review** → there is no `review` mode — the review
*is* `default` mode's inline diff card. `/diff` and `/artifact` cover after-the-fact review.

### Models (`agy models`, 15 ids / 7 families + effort slider)
`gemini-3.8-flash-{high,medium,low}`, `gemini-3.7-flash-{high,medium,low}`,
`gemini-3.6-flash-{high,medium,low}`, `gemini-3.1-pro-{high,low}`,
`claude-sonnet-4-6`, `claude-opus-4-6-thinking`, `gpt-oss-120b-medium`.
Account: `dejan.kenkyukai@gmail.com` (Google AI Pro). Default: Gemini 3.8 Flash (High).

### Customization commands & discovery paths
| Feature | Command | Workspace path | Global path |
| :-- | :-- | :-- | :-- |
| Skills | `/skills` | `.agents/skills/<n>/SKILL.md` | `~/.gemini/antigravity-cli/skills/`, `~/.gemini/skills/` |
| Hooks | `/hooks` | `.agents/hooks.json` | `~/.gemini/config/hooks.json` |
| Plugins | `agy plugin …` | `.agents/plugins/<n>/plugin.json` | — |
| Subagents | `/agents`, `agy agent` | `.agents/agents/<n>.md` | `~/.gemini/config/agents/` |
| MCP | `/mcp`, `agy mcp …` | **none** | `~/.gemini/config/mcp_config.json` |
| Rules | — | `GEMINI.md`, `AGENTS.md`, `.agents/rules/*.md` | — |

Hook events: `PreToolUse`, `PostToolUse`, `PreInvocation`, `PostInvocation`, `Stop`.
Workspace roots also accepted as `.agent/`, `_agents/`, `_agent/`. Precedence: workspace > declared > global.

---

## 5. STEP 6 — permission gate · **PASS**

Setup: `/tmp/agy-test` + `git init`. A first-run **workspace trust gate** appears per workspace
("Do you trust the contents of this project?" → *Yes, I trust this folder* / *No, exit*), recorded in
`settings.json:trustedWorkspaces`.

### 6a — file creation, default (most restrictive) mode · **PASS**
Prompt: *"Create a file named hello.txt in the current directory containing the text hello"*. Exact card:

```
● Create(/private/tmp/agy-test/hello.txt) (ctrl+o to expand)

Create file
──────────────────────────────────────────────────────────────────────
/private/tmp/agy-test/hello.txt  +1
   1 +  hello

Allow creation of this file?
> 1. Yes, allow creation
  2. No, deny creation

  ↑/↓ Navigate · tab Amend · f full diff
```

Answered **No** → `Create file  ⎿  User declined the tool call` → `hello.txt` absent. ✅

A path run *outside* the workspace root adds a third option and a reason line — worth knowing, because
`/tmp` symlinks to `/private/tmp` and a workspace opened as `/tmp/...` treats its own files as external:

```
Reason: outside workspace

Allow creation of this file?
> 1. Yes, allow creation
  2. Yes, and always allow non-workspace access
  3. No, deny creation
```

### 6b — shell command, same mode · **PASS**
Prompt: *"Run this exact shell command: echo hi > run.txt"*. Exact card:

```
● Bash(echo hi > run.txt) (ctrl+o to expand)

Command

Requesting permission for:
   echo hi > run.txt

Do you want to proceed?
> 1. Yes
  2. Yes, and always allow in this conversation for commands that start with 'echo hi > run.txt'
  3. Yes, and always allow for commands that start with 'echo hi > run.txt' (Persist to settings.json)
  4. No

  ↑/↓ Navigate · tab Amend · ctrl+g edit/expand command
```

Answered **No** (option 4) → `User declined the tool call` → `run.txt` absent. ✅
Note options 2/3: one is conversation-scoped, one **persists an allow-rule to `settings.json`**. Option 3
is the one to never press casually on a standing seat.

### 6c — default mode, no flags · **PASS (same configuration as 6a)**
`default` *is* the most restrictive mode, so 6a and 6c are the same run: **default gates.**

**Inverse control** (proving the gate is real, not incidental): the identical prompt under
`agy --mode=accept-edits` produced **no prompt at all** and wrote `accept.txt` immediately.
Gate present in `default`, absent in `accept-edits` — mode-sensitive and genuine.

---

## 6. STEP 6.5 — agent features

| # | Feature | Result | Evidence |
| :-- | :-- | :-- | :-- |
| a | SKILL | **PASS** | `.agents/skills/cobalt-test/SKILL.md` → agy ran `Read(/private/tmp/agy-test/.agents/skills/cobalt-test/SKILL.md)` and answered `COBALT-SKILL` |
| b | HOOK | **PASS (interactive)** | `.agents/hooks.json` `PreInvocation` → `hook.log`: `HOOK-FIRED 08:07:31 event=PreInvocation` |
| c | MCP | **PASS** | 20-line stdio server registered; `agy mcp list` showed it; server log: `recv method=tools/call` → `TOOL_CALLED ping -> pong` |
| d | SUBAGENT | **PASS** | `.agents/agents/sub-ok.md` → `Agent(sub-ok: Seat-Test Subagent)`, `1 subagent(s)`, `Delegating…` → replied `SUB-OK` |
| e | PLUGIN | **PASS** | `.agents/plugins/cobalt-kit/` → `agy plugin validate` `[ok] ✔ skills: 1 processed`; agy read the plugin's skill and answered `COBALT-PLUGIN` |
| f | MODELS | **PASS** | `/model` panel switched to `Claude Sonnet 4.6 (Thinking)` and back to `Gemini 3.8 Flash`; both answered `READY` headlessly |
| g | BACKGROUND | **PASS** | `/tasks`: `Agent Backgrounded ● [08:21:21] sleep 8 && echo bgshell > bg.txt` → **`completed (exit 0)`**, `bg.txt` written |

### Findings that matter for seat design

1. **Headless mode auto-denies.** Any tool needing permission is refused, not prompted:
   `jetski: no output produced — a tool required the "command" permission that headless mode cannot
   prompt for, so it was auto-denied.` This is a **safe default** — `agy -p` cannot be tricked into
   running an unapproved command. It also means headless agy is read-only-ish unless allow-rules or
   `--dangerously-skip-permissions` are added.
2. **Project-local hooks do NOT fire in headless mode; global hooks DO.** Verified both directions with
   the same probe script. herdr's hook is global, so herdr's session reporting is unaffected.
3. **`agy plugin list` only lists *imported* plugins** (from gemini/claude via `agy plugin import`).
   Workspace plugins are auto-discovered and work, but never appear in that listing —
   `agy plugin validate <path>` is the check that actually confirms them.
4. `agy agent` listed nothing for a subagent declared `mainAgent: false`; it still invoked correctly.
5. Docs are fetchable as markdown by appending `.md` to any docs URL — useful for future work.

---

## 7. STEP 7 — herdr detection · **PARTIAL**

Driven directly via herdr (no need to borrow tab 2): a scratch tab was created with
`herdr tab create --cwd /private/tmp/agy-test`, then `herdr agent start agy-seat --kind agy --pane w1:p5`.
herdr immediately classified it — `agent: agy`, `agent_status: idle` — and the hook reported session
identity (`agent_session.source: "herdr:antigravity_cli"`). agy was **never started in `~/cobalt`** by me.

### 6a-style prompt (file creation) → **FAIL**
The pane visibly showed `Allow creation of this file?` with the agent halted, yet:

```
agy      idle      pane=w1:p5  name=agy-seat  cwd=/private/tmp/agy-test
```

`herdr agent explain agy-seat`:

```
agent: agy
state: idle
manifest: remote:/Users/cobalt/.local/state/herdr/agent-detection/remote/agy.toml 2026.06.24.1
rule: none
fallback_reason: default_known_agent_idle_fallback
```

**Root cause.** The manifest's `permission_prompt` rule (state `blocked`, priority 300) has a hard
requirement: `contains = ["requesting permission for:"]`. agy 1.1.27 emits that line for **command**
approvals only. Its **file-write** card says `Create file` / `Allow creation of this file?` and never
contains that string, so no rule matches and herdr falls back to `idle`.

### 6b-style prompt (shell command) → **PASS**
```
$ herdr agent prompt agy-seat "Run this exact shell command: echo hi > run.txt"
t+  0s  agent=agy  agent_status=blocked
```
`herdr agent prompt … --wait --until blocked` also returned cleanly (`state_change_seq 24`).
After answering, status returned to **idle** in both cases, and neither `hello.txt` nor `run.txt` was created.

**Net:** the blocked→idle lifecycle works; the trigger set is incomplete. herdr's agy manifest
(`2026.06.24.1`, dated 2026-06-24) predates this CLI build.

---

## 8. Cleanup proof

| Item | State |
| :-- | :-- |
| `/tmp/agy-test`, `/tmp/agy-install.sh`, all temp captures | deleted (`/tmp/*agy*` → no matches) |
| `~/.zshrc`, `~/.zprofile`, `~/.profile` | restored; sha256 of `.zshrc` matches pre-install; 0 Antigravity lines |
| `~/.gemini/config/hooks.json` | restored — keys: `['herdr']` only |
| `~/.gemini/config/mcp_config.json` | restored to empty — `No MCP servers configured.` |
| `settings.json:trustedWorkspaces` | scratch entries **and** `/Users/cobalt/cobalt` removed → `[]` |
| herdr scratch tab `w1:t5` | closed (tabs remaining: `w1:t1`, `w1:t4`) |
| herdr integration | still `antigravity-cli: current (v2)` |
| Retained deliberately | `~/.local/bin/agy` (the seat) + `~/.gemini/` config home |

### Repo & vault

`git status` is **unchanged from session start except `configs/cobalt/rules.yaml`, which is not mine**:
its mtime is **05:15**, ~2h20m before this session began (07:33), and the only delta is
`generated_at: 2026-09-03… → 2026-09-07T09:15:00+00:00` with `source_sha256` **identical** — i.e. Cobalt's
own rules-prefill LaunchAgent regenerating from the vault. No rule content changed. Branch/HEAD untouched
(`ops/triage-2026-09-06` @ `8b1055b`). No commits made.

Two vault files carry today's mtime — `.obsidian/workspace.json` (Obsidian UI state) and
`1 - Trading/1- Daily Notes/2026-09-07.md` (Dejan's journal, header `2026-09-07 T 05:15`, sleep/readiness
entries). Neither is attributable to agy: every agy invocation's cwd is accounted for
(`/private/tmp/agy-test`, plus a handful of read-only `--version`/`--help`/`models` calls), and the vault
was never in `trustedWorkspaces`.

**One deviation to record:** a few informational calls (`agy --version`, `agy --help`, `agy models`)
inherited `~/cobalt` as cwd because the shell resets there between commands. They wrote nothing, but agy
registered `/Users/cobalt/cobalt` in `trustedWorkspaces`. That entry has been removed. No agy *session*
ever ran in the repo from this seat.

---

## 9. Escalations / could not test

1. **herdr agy detection manifest is stale** (`2026.06.24.1` vs agy 1.1.27) — the one blocking defect.
   Fix belongs upstream in herdr (add `Allow creation of this file?` / `Create file` to the
   `permission_prompt` rule's `any` list, or relax the `contains` requirement). Not fixed here per
   "report, don't fix". Worth checking `herdr channel set preview` / `herdr update` for a newer manifest.
2. **`--sandbox` not exercised.** Terminal-restriction sandboxing and the `unsandboxed(...)` permission
   action were read in docs only — testing them properly needs a container-isolation check beyond this brief.
3. **`/permissions`, `/hooks` interactive panels not driven.** Behaviour was verified through the
   underlying config files instead; the TUI panels themselves are untested.
4. **`ctrl+b` foreground→background handoff did not register** under pty automation (`/tasks` stayed
   empty). Background execution itself is proven two other ways (subagents; background shell process
   reaching `completed (exit 0)`), so this is most likely a limitation of my keystroke harness rather
   than an agy defect — but it is unproven either way.
5. **Not tested:** `remote-control` daemon, `mic-serve`/`/voice`, `/teamwork-preview`, `/boost`,
   `/schedule`, `/browser`, credits/quota behaviour under load.
6. **Cost/quota:** the seat runs on Dejan's Google AI Pro entitlement. Standing-seat usage will draw on
   it; `/usage` and `/credits` exist but no baseline was recorded.

---

## 10. Recommendation

Give agy a standing seat, with these operating rules until the herdr manifest is fixed:

- Run it in **`default` mode**. Never make `--dangerously-skip-permissions` or `--mode=accept-edits` the
  seat's default; both defeat the gate that this test just validated.
- **Do not trust the herdr status column for agy file edits.** A file-approval prompt reads as `idle`.
  Check the pane directly, or keep agy on command-heavy work where detection is reliable.
- Never press "(Persist to settings.json)" on an approval card without intent — it writes a durable
  allow-rule.
- Keep agy out of `~/cobalt` and the vault. Scratch dirs and worktrees only, per the freeze.
- Headless `agy -p` is the safest surface (auto-denies privileged tools) and is a good fit for
  read-only research passes.
