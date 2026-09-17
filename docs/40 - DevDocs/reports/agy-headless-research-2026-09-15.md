---
name: agy-headless-research-2026-09-15
description: How to grant agy (Antigravity CLI) headless tool permissions via settings.json config, never --dangerously-skip-permissions
---

# Research: agy headless tool permissions by configuration — 2026-09-15

Prompt: `docs/40 - DevDocs/prompts/2026-09-15/07-agy-headless-research.md`. Followed
the trial in `docs/40 - DevDocs/reports/agy-trial-2026-09-15.md` (zero output,
every tool auto-denied headless). Read-only research; no writes to
`~/.gemini/antigravity-cli/settings.json`.

## §0 Headline
Config path exists and is real: settings.json takes a top-level `permissions`
object with `allow`/`deny`/`ask` arrays of `action(target)` strings —
`read_file(...)`, `write_file(...)`, `command(...)`, `mcp(...)`, confirmed by
the agy 1.2.3 binary's own error template, its log lines, and Google's official
docs (exact JSON example matches). `list_dir`/`glob` have **no separate rule
syntax anywhere in the binary** — they piggyback on `read_file` grants for the
same path (inferred, not spelled out in docs). One open upstream bug (GitHub
#548, Windows-reported) says headless mode sometimes ignores `permissions.allow`
and hangs past `--print-timeout` instead of denying cleanly; our own local
1.2.3 binary denies cleanly and fast (15–34s, per the 09-15 trial), so this may
not reproduce here, but the probe below should be watched for a hang as the
tell. ESCALATE: 1 (the probe result — config path is evidenced, not yet proven
live; needs Dejan to run it).

## 1. Local evidence
- `agy changelog` (1.2.3 back through history), grepped for permission/allow/rule/command(/unsandboxed/settings: line 9 — `unsandboxed` rules deprecated, migrate to `command()`; line 151 — "automatically granting workspace-scoped read access under the **default review mode**... within the workspace root" (this is the *default*, non-sandboxed case — does not describe `--sandbox` behavior, which is what the 09-15 trial used and where reads were still denied); line 139 — `always-proceed` permission mode auto-approves MCP calls and page reads too; line 153/69 — print mode now reports `denied_actions` in JSON output and no longer treats permission denials as fatal.
- `agy --help`: no `--permission-mode` flag; `--mode` only takes `accept-edits`/`plan`. `toolPermission` (the four-way policy: `always-proceed`/`request-review`/`strict`/`proceed-in-sandbox`) is a **settings.json key, not a CLI flag** — confirmed by both the binary log format string and the official CLI reference doc's example snippet (below).
- `~/.gemini/antigravity-cli/builtin/skills/antigravity_guide/references/app.md` — documents the GUI's Settings sidebar: Tool Execution Policy = `always-proceed`/`request-review`/`strict`/`proceed-in-sandbox`; Non-Workspace File Access = `allow`/`ask`/`deny`; "Permission Grants: Define global allow/deny rules for specific files, commands, and URLs"; Project-Level Settings section confirms **project-scoped** permission grants exist as a concept but gives no settings.json key shape for them.
- `~/.gemini/antigravity-cli/builtin/skills/antigravity_guide/references/cli.md` — confirms `~/.gemini/antigravity-cli/settings.json` is the config file; defers schema to the live docs (fetched below).
- `~/.gemini/antigravity-cli/builtin/skills/agy-customizations/docs/hooks.md` — a hook's `permissionOverrides` field uses the identical `["command(npm test)"]` string syntax, corroborating the rule grammar.
- `strings` on the agy binary (`/Users/cobalt/.local/bin/agy`, a real Mach-O executable, not a symlink) — read-only, no execution:
  - Exact denial template: `%s required the %s %s that headless mode cannot prompt for, so %s auto-denied. Add an allow-rule under permissions.allow in settings.json (e.g. %s)` — matches the 09-15 trial's `agy-err.log` verbatim.
  - `applyUserSettings: stored shared config permissions: allow=%d deny=%d ask=%d from %s` and `ApplyProjectPermissionGrants: stored %d allow, %d deny grants from project %q` — confirms three-list schema (`allow`/`deny`/`ask`) and that project-scoped grants are tracked separately by project name internally, but their on-disk key shape wasn't found (see §3).
  - `populatePermissionConfig(conv=%s): toolPermission=%v autoExecPolicy=%v enableTerminalSandbox=%t allowNonWorkspaceAccess=%t` — confirms settings.json field names `toolPermission`, `enableTerminalSandbox`, `allowNonWorkspaceAccess` (matches the official doc's example below field-for-field).
  - Rule-string literals found: `command()`, `command(*)`, `command(git status)`, `command(cat)`, `command(head)`, `command(tail)`, `command(tail -f)`, `command(npm test)`, `read_file(*)`, `read_file(/)`, `write_file(*)`, `write_file(/)`. **No** `list_dir(...)` or `glob(...)` rule string exists anywhere in the binary (checked both literal and regex search) — those two tool names appear only as internal proto/tool identifiers, never as a grantable permission target.
  - `Fix: replace "unsandboxed" with "command" ... Each token in the granted target is matched as a full word (internally treated as an anchored regular expression: ^(?:pattern)$).` and `Matches commands by prefix. e.g., 'git' matches 'git add', 'git commit', etc.` — command matching is prefix-by-token, anchored; official docs (below) also show a `regex:` form for tighter matching.
  - `Same as read_file. Also implicitly covers read_file for the same path.` — almost certainly the `write_file` description (write implies read), matching the official docs' explicit statement below.
- `~/.gemini/antigravity-cli/cli.log` (today's run, real): `cli_setting_manager.go:92` → `CLI settings initialized: permissions=<nil>, toolPermission=request-review` — confirms our current settings.json (no `permissions` key at all) is why every trial call was denied; `cli_setting_manager.go:156` → a **second** config location, `/Users/cobalt/.gemini/config/config.json` ("shared config"), can also carry a `permissions` block, merged in; `cli_setting_manager.go:218` → `ApplyProjectPermissionGrants: no grants for project "CLI Project", cleared project permissions` — project grants are a real, separate, currently-empty layer.
- Scanned all `log/*.log` back to 09-07 for a non-empty grant line: none found. **No interactive "always allow" grant has ever been made on this machine**, so source 3 (does an interactive grant persist, and in what shape) could not be answered from local history — see §3/GitHub #548.

## 2. Web evidence
- `https://antigravity.google/docs/permissions` — canonical action/target grammar, three lists (deny > ask > allow precedence): `read_file`, `write_file` (implies `read_file` on same target), `read_url`, `execute_url`, `command` (prefix or `regex:`), `unsandboxed` (deprecated), `mcp`. No `list_dir`/`glob` action listed — matches the binary's silence on them.
- `https://antigravity.google/docs/cli/reference` — settings.json keys: `toolPermission` (`request-review` default, `proceed-in-sandbox`, `always-proceed`, `strict`), `artifactReviewPolicy`, `enableTerminalSandbox`, `allowNonWorkspaceAccess`, plus display/editor keys. Example:
  ```json
  {
      "colorScheme": "tokyo night",
      "altScreenMode": "always",
      "toolPermission": "request-review",
      "notifications": true,
      "enableTerminalSandbox": true
  }
  ```
  Does not show `permissions.allow` in the same example, nor `trustedWorkspaces` (we confirmed that key exists and is live-used from our own settings.json + the binary's `TrustedWorkspaces` / `json:"trustedWorkspaces,omitempty"` struct tag).
- `https://antigravity.google/docs/cli/headless/` — the load-bearing page for the task. Direct quotes: "By default, the CLI respects the permission mode in your settings. A tool that requires approval it cannot obtain is soft-denied: the run continues, exits 0, and prints a notice to stderr." and "Reading and writing files inside your active workspace is auto-allowed" by default in headless contexts — this is the *non-sandboxed* default; it does not claim to cover `--sandbox`, which is exactly the gap the 09-15 trial hit (read_file denied under `--sandbox`). Canonical example, given verbatim by the doc for CI/non-interactive use:
  ```json
  {
    "permissions": {
      "allow": [
        "command(git)",
        "command(regex:npm run (build|lint|test))",
        "write_file(src/)"
      ]
    }
  }
  ```
  Also: `--dangerously-skip-permissions` is documented and explicitly discouraged in favor of scoped `permissions.allow` rules — this is the "config, not the banned flag" path the task requires.
- GitHub `google-antigravity/antigravity-cli#548` (open, filed 2026-07-06, Windows-labeled): "`--print` (headless) mode ignores permissions.allow entirely; 'persist to settings.json' approval option writes nothing." Reporter's five repro variants (including `toolPermission: always-proceed` set globally) all **hung indefinitely** past `--print-timeout` instead of denying — a materially different failure mode than our clean, fast (15–34s) denial in the 09-15 trial on this Mac. Two takeaways: (a) the interactive-grant-persists-to-settings.json path is confirmed broken upstream — directly answers source 3: don't rely on it, hand-edit instead; (b) if Dejan's probe below hangs rather than returning output or a clean denial, that is this bug, not a config mistake — kill it at `--print-timeout` and report back rather than waiting longer.

## 3. Interactive grant persistence (source 3)
Could not be verified live (never exercised on this machine, per §1 log scan) and is reported broken upstream (GitHub #548, §2). Do not rely on "approve once, it'll persist" — hand-write the JSON below instead.

## 4. Deliverable — JSON to merge into `~/.gemini/antigravity-cli/settings.json`

Scope: `read_file` (covers `list_dir`/`glob` too, per §1/§2 — no separate rule exists for either), `command(git diff *)`, `command(git log *)`, for the two worktrees only. Nothing that writes.

**Most likely (matches the official docs' own example syntax exactly):**
```json
{
  "permissions": {
    "allow": [
      "read_file(/Users/cobalt/cobalt-wt/s2-p3-radar-panel/)",
      "read_file(/Users/cobalt/cobalt-wt/agy-trial/)",
      "command(git diff *)",
      "command(git log *)"
    ]
  }
}
```
Caveat: `read_file(<dir>/)` scopes the read/list/glob grant to that directory by construction (path-prefix target). The two `command(...)` rules do **not** carry a path — `command` targets match the command string, not a working directory — so they are global to any agy session on this machine once written, not cryptographically confined to these two worktrees. In practice exposure stays bounded to whatever `--add-dir` was passed at launch, but this is a real gap between what the task asked for ("for the two worktrees ... only") and what the rule grammar can express. Flagging rather than overclaiming a directory-scoped command grant that doesn't exist in the schema.

**Second-most-likely (regex form, tighter anchoring, same semantics):**
```json
{
  "permissions": {
    "allow": [
      "read_file(regex:^/Users/cobalt/cobalt-wt/(s2-p3-radar-panel|agy-trial)/.*)",
      "command(regex:^git (diff|log) .*)"
    ]
  }
}
```

## 5. Backup-first merge command (Dejan runs this, not us)
```
python3 -c "import json,shutil,time; p='/Users/cobalt/.gemini/antigravity-cli/settings.json'; b=p+'.bak-'+time.strftime('%Y%m%d%H%M%S'); shutil.copy2(p,b); d=json.load(open(p)); perms=d.setdefault('permissions',{}); allow=perms.setdefault('allow',[]); new=['read_file(/Users/cobalt/cobalt-wt/s2-p3-radar-panel/)','read_file(/Users/cobalt/cobalt-wt/agy-trial/)','command(git diff *)','command(git log *)']; [allow.append(r) for r in new if r not in allow]; json.dump(d,open(p,'w'),indent=2); print('backed up to',b,'; allow now has',len(allow),'rules')"
```

## 6. Headless probes (Dejan runs after the merge)
```
agy --print="Read /Users/cobalt/cobalt-wt/agy-trial/README.md and reply with its first line only" --model gemini-3.1-pro-low --mode plan --sandbox --print-timeout 2m --add-dir /Users/cobalt/cobalt-wt/agy-trial
```
Expected: the file's first line, returned in well under 2m. If it hangs to the timeout instead, that's GitHub #548 (§2), not a JSON mistake — report back rather than re-running.
```
agy --print="Run git diff --stat main..HEAD and reply with just the output" --model gemini-3.1-pro-low --mode plan --sandbox --print-timeout 2m --add-dir /Users/cobalt/cobalt-wt/agy-trial
```
Expected: the `git diff --stat` output.

## 7. If config turns out not to work at all
Not established as true — the evidence above (official CI-grant doc page, binary's own error message pointing at `permissions.allow`, and our settings.json currently having zero rules explaining the clean denial) says config-granted headless tool use is the intended, documented mechanism. The one real risk is GitHub #548 (hangs, not denials, on some platform/version combos). If §6's probes both hang to timeout even with the JSON merged, the fallback is: (a) do a one-time **interactive** `agy` session in these two worktrees, grant `read_file`/`command(git diff *)`/`command(git log *)` via the TUI's approval prompt (not `--dangerously-skip-permissions`), and manually verify + hand-copy whatever it actually wrote to settings.json (since auto-persist is reported broken) — or (b) if even interactive grants don't stick, a wrapper driving `agy --prompt-interactive` (`-i`) via piped stdin, answering the approval prompts programmatically, with its own probe: `printf 'Read README.md and reply with its first line only\ny\n' | agy -i --model gemini-3.1-pro-low --add-dir /Users/cobalt/cobalt-wt/agy-trial`.

## Cost / escalation
Local reads + binary strings + 4 web fetches + 1 web search. ESCALATE: 1 — the JSON above is evidenced from three independent sources (binary error template, official docs example, hooks.md rule grammar) but has never been run; Dejan's §6 probes are the actual proof.

RESEARCH DONE 1a94ea9 · path: config
