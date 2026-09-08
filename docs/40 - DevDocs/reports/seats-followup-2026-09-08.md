# Seats follow-up — 2026-09-08

**Laws in force:** L29 (no vault/DB write path, no Cobalt `src/` changes) · L15 · L31 · fail-loud.
**Date:** 2026-09-08, a trading day. No service/launchd restarts or reloads were performed
(`com.cobalt.mainframe`, `com.cobalt.agent`, herdr server, or any other launchd job). No git
commits were made by this session. Every file this session modified outside a repo commit is
listed with a backup path in its own section.

---

## STEP 0 — Git state (read-only)

**Snapshot taken at task start**, before any of my own edits:

| Branch | Ahead/behind `main` | Pushed | Last commit |
|---|---|---|---|
| `main` (local) | 0 behind / 17 ahead of `origin/main` | tracked, 17 unpushed | 2026-08-31 `79943f6` |
| `ops/backup-arm` | 90 ahead of main | yes, in sync | 2026-09-05 `1aa2220` |
| `ops/mattermost-role` | 95 ahead | yes, in sync | 2026-09-05 `998a177` |
| `ops/mattermost-split` | 89 ahead | yes, in sync | 2026-09-04 `d56d239` |
| `ops/triage-2026-09-06` (current) | 97 ahead | yes, in sync | 2026-09-06 `8b1055b` |
| `sprint-1/foundation` | 85 ahead | yes, in sync | 2026-09-04 `3fd08ec` |
| `taxonomy/trade-defs-v0_3` | 45 ahead, 4 ahead of its own `origin` | yes, 4 unpushed | 2026-09-04 `b0fd2e4` |

**These six branches were not six independent efforts.** `git merge-base --is-ancestor`, checked
pairwise, showed one **linear stack**, each branch built directly on the previous one's tip, all
sharing identical commit hashes for the common prefix:

```
main (79943f6)
  -> taxonomy/trade-defs-v0_3   (45 commits, tip b0fd2e4, 09-04)
  -> sprint-1/foundation        (85 commits, tip 3fd08ec, 09-04)
  -> ops/mattermost-split       (89 commits, tip d56d239, 09-04)
  -> ops/backup-arm             (90 commits, tip 1aa2220, 09-05)
  -> ops/mattermost-role        (95 commits, tip 998a177, 09-05)
  -> ops/triage-2026-09-06      (97 commits, tip 8b1055b, 09-06)  [was current]
```

`main` was itself a direct ancestor of `ops/triage-2026-09-06`, so the whole stack was a clean
fast-forward. `git branch --merged main` showed only `main` (none of the six had been merged yet
at snapshot time). Working tree on `ops/triage-2026-09-06` carried pre-existing uncommitted
changes from before this session (`configs/cobalt/rules.yaml`, `configs/config.yaml`,
`docs/00 - Project/MVP-CHARTER-v0_2.md`, `docs/00 - Project/PROJECT-LEDGER.md`,
`docs/30 - Design/archiver-runs.md`, `ops/start_mainframe.sh`, plus four untracked
paths) — untouched by me.

**Recommendation given at the time (not executed by me):** push local `main`'s 17 older commits,
then fast-forward `main` to `ops/triage-2026-09-06` in one shot (it's the superset tip — no
separate merge needed for the five intermediate branches, and they become deletable once it's
in).

**What actually happened, mid-session, not by me:** `git reflog` shows Dejan (`dzivanovic`)
committed the pending working-tree changes as `fdf79d0` ("ops+docs: mainframe swap…") at
**08:07:50 -0400**, checked out `main`, fast-forward-merged `ops/triage-2026-09-06` into it, and
pushed. **Current state:** only `main` remains (all six branch refs are gone — deleted, not just
merged), `main` is `fdf79d0`, and `origin/main`...`main` shows 0/0 — fully in sync with the
remote. This is exactly the merge order recommended above, self-resolved by Dejan while this
report was in progress. Nothing here was a git action taken by this session — see the verbatim
`git status --porcelain` at the very end of this report for the current tree.

---

## STEP 1 — Morning briefing triage (read-only, old tree)

### a. Which job

Not a separate launchd entry. `com.cobalt.agent.plist` runs `cobalt.sh start` →
`nohup uv run src/cobalt_agent/main.py`. Inside that process, `CobaltScheduler`
(`src/cobalt_agent/services/scheduler.py:_setup_jobs`) registers exactly one APScheduler cron
job: `id='morning_briefing'`, `day_of_week='mon-fri'`, `hour=8`, `minute=0`. Started from
`main.py`'s `__main__` block, before `agent.start_mattermost_interface()`.

### b. Full code path

Prompt template (`configs/prompts.yaml`, `scheduler.morning_briefing`), quoted verbatim:

```
You are an expert intraday daytrader and financial analyst. Summarize the US pre-market for {today_str}.

*** CRITICAL SYSTEM DIRECTIVE ***
You MUST use the `googleSearch` tool to retrieve live, real-time market data BEFORE generating this report.
1. Search for the current live VIX level and today's macroeconomic backdrop/catalysts.
2. Search for today's top pre-market movers (gappers) and their specific news catalysts.
3. DO NOT simulate, guess, or predict any tickers, prices, or volume data. If you cannot find live data via search, state that data is unavailable. Ground your entire response strictly in the live data retrieved.
[... formatting spec ...]
```

`{today_str}` is the **only** date token, and it is filled by Python before the model ever sees
the prompt: `datetime.now().strftime("%B %d, %Y")` in `scheduler.py:generate_morning_briefing`.
**The code injects the date; the model does not supply it for that line.** The model call is
`BriefingAgent(role="researcher").run(...)` → `LLM.generate_response(tools=[{"googleSearch":{}}])`
→ `litellm.completion` with native Gemini grounding (not the custom `ACTION:` tool loop — no
`ACTION:` line appeared in the 09-08 log, confirming grounding is native, not the ReAct path).
The raw model output is written to file **verbatim**, with **no header prepended** by this code
path (a separate, unused `MorningBriefing` class in `skills/productivity/briefing.py` *does*
prepend a `# Morning Briefing: {date}` header, but it is wired only to the interactive
CLI/Cortex path, never to this cron job).

**Delivery:** file → `docs/60 - Agent Output/Morning_Briefing_YYYY-MM-DD.md` (resolves inside the
repo: `.env` sets `OBSIDIAN_VAULT_PATH=/Users/cobalt/cobalt/docs` and
`BRIEFING_INBOX_DIR="60 - Agent Output"` — not the real vault). Mattermost → `town-square` channel,
team `cobalt-bridge`, message `"☀️ Morning Briefing Ready! ... pre-market analysis for
{today_str} ..."`.

### Cause of the wrong date — NOT REPRODUCED

I could not find a wrong date in any artifact this job produced today. Evidence gathered:

- **Today's file** (`Morning_Briefing_2026-09-08.md`) has **zero date-string references** anywhere
  in its body (checked for day names, "current date", "today is", "2026", "September" — no
  hits).
- **Today's Mattermost delivery message** (`agent_2026-09-08.log:50-51`, 08:00:23) reads
  `"...pre-market analysis for September 08, 2026..."` — **correct**.
- **Yesterday's file** (09-07) *does* open with a date line — `"RSThe current date is Monday,
  September 7, 2026."` — the date itself is **correct** (2026-09-07 is in fact a Monday,
  confirmed via `date -j`), but the leading `"RS"` looks like a truncated word fragment (e.g. a
  clipped "RESULTS"/"SOURCES" heading) — a distinct formatting defect, not a wrong date.
- No stale or duplicate copies exist elsewhere on disk (broad `find ~` for
  `Morning_Briefing_*.md` found nothing outside `docs/60 - Agent Output/`).
- System clock/timezone are correct: `date` → `Tue Sep 8 08:08 EDT 2026`; `/etc/localtime` →
  `America/New_York`. No drift.
- **Unconfirmed hypothesis, not a claim:** today's grounding call completed in ~22s with a single
  `generate_response` call and the output text includes the hedge *"Granular live data for
  RVOL > 4, ATR > 0.4, and exact pre-market volume > 100K is currently unavailable via live search
  results for today's session"* — suggesting partial/failed grounding. If grounding silently
  degrades, the model could fall back to non-live (effectively stale-dated) data without ever
  printing a date string. I did not call the paid API to test this further, per instruction.

**I cannot pin down what was actually seen as "wrong."** Neither delivery artifact I examined
(file, Mattermost message) shows an incorrect date string. **ESCALATE: ask Dejan for the exact
screenshot/message he flagged** so this can be traced to its real source.

### c. Routing/model, cost evidence

`researcher` role → `active_profile.researcher: "cloud_gemini_3_1_pro_preview"` →
`provider: "gemini"`, `model_name: "gemini-3.1-pro-preview"`, `env_key_ref: "gemini"` →
`configs/config.yaml keys.gemini = "GEMINI_API_KEY"` (name only — value never inspected or
printed). `llm.py:_call_provider`'s key-resolution has what looks like a dict-shape bug (looks up
`keys_dict[target_key_name]` against a dict whose keys are role names, not env-var names — this
will always miss) but falls through to `os.getenv("GEMINI_API_KEY")`, which is not a literal line
in `.env` — the credential is supplied some other way (VaultManager or process env), not traced
further (secrets boundary). **No usage/cost/token telemetry exists anywhere in this codebase** —
`llm.py` and the logs never record `prompt_tokens`/`completion_tokens`/cost. Only call-**count**
evidence is available: exactly one `morning_briefing` run per weekday in the retained 7-day log
window (09-02, 03, 04, 07, 08 — 09-05/06 correctly skipped, weekend). No paid API call was made to
test this, per instruction.

### d. Everything else `com.cobalt.agent` provides

From `main.py`'s `__main__`: (1) `CobaltScheduler` — **only one** registered job,
`morning_briefing` Mon-Fri 08:00 (no other cron jobs anywhere in `scheduler.py`). (2)
`MattermostInterface` websocket listener (`start_mattermost_interface`, blocking) — the live
chat/command surface. (3) `ProposalEngine` (HITL approval workflow), attached to that Mattermost
interface. (4) `Cortex` brain routing, also attached, for chat-command handling. The interactive
CLI path (`agent.main()` / `Prompt.ask` loop) is a **separate** entrypoint, not used by the
daemon launch.

### e. Recommendation (no fix applied)

**No clean lever exists to disable `morning_briefing` alone.** `scheduler.py` hardcodes the cron
registration with no config/env gate — unusual for this codebase, which CLAUDE.md documents as
otherwise config-driven. Disabling it cleanly needs a small `src/` change (barred today by L29).
Options: **(i)** disable job alone — blocked today, needs a future code change; **(ii)** leave
running until the old tree retires — no code touched, Mattermost listener + HITL stay up;
**(iii)** stop `com.cobalt.agent` entirely — also kills the Mattermost listener and HITL proposal
engine, and is a service restart/stop, explicitly forbidden today. **Recommendation: (ii).**
Revisit with a proper config gate in a future sprint.

### f. Provider console

Gemini calls route through provider `"gemini"` (litellm) using the credential named
`GEMINI_API_KEY` (`env_key_ref: "gemini"`). Check whichever project issued that key in
VaultManager, in **Google AI Studio** (aistudio.google.com) or the matching **Google Cloud
Console** project — no project ID string is present in the repo or `.env` to name it more
precisely (not guessed).

---

## STEP 2 — Grok sandbox

**Reproduced exactly.** `grok --sandbox read-only -p "echo hi"` (and any custom profile
`extends`ing `"read-only"`, even freshly defined) fails with:

```
warning: sandbox could not be applied: runtime-socket deny resolution failed: could not resolve runtime-socket deny path /var/run/docker.sock: endpoint is a symlink
error: could not apply the 'read-only' sandbox profile; see the warning above for the cause. Refusing to start with its protections missing.
```

**Cause:** OrbStack symlinks `/var/run/docker.sock -> /Users/cobalt/.orbstack/run/docker.sock`
(confirmed via `readlink`). The built-in `read-only`/`strict` profiles carry an **undocumented**
internal "runtime-socket deny" pre-flight check (not exposed as a `sandbox.toml` field anywhere in
`~/.grok/docs/user-guide/18-sandbox.md` or `26-config-reference.md`) that tries to canonicalize
known container-runtime socket paths and refuses to start if one is a symlink it can't resolve.
This is a Grok 1.0.13 bug on OrbStack-based macOS hosts.

**Mechanism, discovered empirically (not guessed):** a custom profile `extends`ing `"read-only"`
still hits the identical error — `extends` inherits the same internal check. Adding
`restrict_network = false` to the custom profile **bypasses the runtime-socket check entirely**
and the profile starts cleanly. Since the docs state plainly that `restrict_network` is **already
a no-op on macOS** for actual network blocking, this workaround costs nothing on this platform —
nothing that was ever actually enforced gets relaxed.

**Important caveat:** literal `grok --sandbox read-only` (the built-in name) **cannot** be fixed
via `sandbox.toml` — "a custom profile can't reuse a built-in name" (docs), and the bug lives in
the built-in's own hardcoded check. The only usable fix is an equivalent custom profile under a
different name.

**File written:** `~/.grok/sandbox.toml` (was empty; backed up to `~/.grok/sandbox.toml.pre-p4`,
also empty). New content:
```toml
[profiles.readonly-safe]
extends = "read-only"
restrict_network = false
```

**Proof** (via `--sandbox readonly-safe`, headless `-p`, `--always-approve` to isolate kernel
enforcement from Grok's own permission-prompt layer):

- Starts cleanly, no error.
- `~/.grok/sandbox-events.jsonl` `ProfileApplied` event: `enforced:true`, `restrict_network:false`,
  `read_write_paths` = exactly `~/.grok`, `/tmp`, `/var/tmp`, `/private/tmp`, `/private/var/tmp`,
  `/private/var/folders`, per-run T dir — **matches the documented `read-only` grant exactly**
  (not CWD, unlike `workspace`).
- Scratch file edit (Grok's own file-edit tool) outside the granted zone
  (`~/grok-sandbox-test-p4`, deliberately **not** under `/tmp`): **refused** —
  `failed to write testfile.txt: IO Error: Operation not permitted (os error 1)`. File unchanged.
- Scratch shell `touch newfile.txt` in the same dir: **refused** —
  `touch: newfile.txt: Operation not permitted`, exit 1, file not created.
- `rm testfile.txt`: **refused** — `rm: testfile.txt: Operation not permitted`, exit 1, file still
  present.
- Network state: `curl https://example.com` → HTTP 200 (succeeds) — confirms `restrict_network:
  false` changes nothing actually enforced on macOS (matches the docs' stated no-op).
- Test debris cleaned up.

**ESCALATE candidate:** worth filing upstream with Grok (OrbStack docker.sock symlink breaks
`read-only`/`strict` startup) — similar in shape to the agy/herdr issue in Step 8. Not filed by
me.

---

## STEP 3 — Claude-config inheritance: coexist, never disable

Harness Compatibility toggles were **not touched**; all `claude` cells remain `on (default)` in
`grok inspect`, confirmed before and after my edits.

### a. Inventory (docs + live `grok inspect` in `/Users/cobalt/cobalt`)

| What | Paths | Live in this project |
|---|---|---|
| Project instructions | `CLAUDE.md`/`CLAUDE.local.md`, project + `~/.claude/` home-level + `<dir>/.claude/CLAUDE*.md` | `/Users/cobalt/cobalt/Claude.md` loaded (~3409 tokens; display casing differs from `CLAUDE.md` only because of case-insensitive-fs dedup — same file) |
| Permissions | `.claude/settings.local.json` (project), `~/.claude/settings.json`+`.local.json` (global) | `/Users/cobalt/cobalt/.claude/settings.local.json`, 5 rules loaded |
| Skills | `~/.claude/skills/`, `~/.claude/commands/` (lowest precedence, configurable) | none present beyond Grok's own 24 bundled |
| MCP servers | Claude's project + user MCP config sources | 0 loaded (none configured) |
| Hooks | `~/.claude/settings.json`(+`.local.json`) always; `<project>/.claude/settings.json`(+`.local.json`) requires folder trust | 1 fired, tagged `[claude]`, `matcher=*`, `SessionStart` — see 3b |
| Sessions | Read access gated by the `sessions` cell + the `resume-claude` skill | see 3d |

### b. The hook that fired in the 09-07 Grok run

`~/.claude/hooks/herdr-agent-state.sh` — **installed and managed by herdr**; its own header
warns: *"reinstalling or updating the integration overwrites this file... add custom hooks beside
this file instead of editing it."* Wired via `~/.claude/settings.json`'s `hooks.SessionStart`
(`matcher: "*"`). It is **unconditionally hardcoded** `source="herdr:claude"`, `agent="claude"` —
**no harness detection at all**.

`grok inspect` shows 2 `SessionStart` hooks discovered under Grok: 1 native ("user") + 1 inherited
("[claude]"). Grok **also** has its own correctly-labeled native hook
(`~/.grok/hooks/herdr-agent-state.sh`, `agent="grok"`, reads `GROK_SESSION_ID`). **So every Grok
session double-fires: one correct report and one incorrect one** — the exact 09-07 bug.

Checked the other harnesses in scope:
- **Codex** has its own fully separate native hook (`~/.codex/hooks.json` +
  `~/.codex/herdr-agent-state.sh`, `HERDR_INTEGRATION_ID=codex`), no evidence of Claude-config
  inheritance — not affected.
- **agy**: initially found no `~/.agy` config and no Claude-compat flag in `agy --help`. A later
  live probe in Step 8 (spinning up a scratch agy session) showed it actually reports to herdr as
  `source: "herdr:antigravity_cli"` with its own session id — **agy does have a working native
  herdr integration**, just not stored where I first looked (its home-dir/config location was not
  pinned down; not investigated further as it was outside this step's scope). No evidence agy
  inherits or fires *Claude's* hook file specifically. The fix below stays defensive for it
  regardless (never mislabels an unrecognized invoker as `claude`).

**Fix** — deliberately **not** editing the herdr-managed file itself (honoring its own "edit
beside it, not it" instruction, so a herdr reinstall/update won't silently revert this). Added:

- **New file** `~/.claude/hooks/herdr-harness-guard.sh` (not herdr-managed), which gates on env
  vars set directly by each vendor's own binary — the most robust signal available (more robust
  than argv or parent-process sniffing, which are fragile and unrelated to actually-invoking
  process identity):
  - `CLAUDECODE` or `CLAUDE_CODE_SESSION_ID` present, **and** no `GROK_SESSION_ID` → genuinely
    Claude Code → `exec`s the real herdr script unchanged (stdin preserved via `exec`).
  - `GROK_SESSION_ID` present (Grok sets this on every hook process it runs — confirmed in
    `~/.grok/docs/user-guide/10-hooks.md`'s "Environment Variables" table) → this is Grok firing
    the inherited hook → exits 0 silently (Grok's own native hook already reports correctly in
    parallel).
  - Neither signal present (unknown harness) → exits 0 silently rather than guess/mislabel as
    `claude`. Documented in-file as a gap to close once that harness's real hook-process env is
    observed.
- **Edited** `~/.claude/settings.json`'s `hooks.SessionStart` command to point at the guard
  instead of the herdr script directly.

**Backups:** `~/.claude/settings.json.pre-p4` (original, 243 bytes, intact). The herdr-managed
`.sh` file itself was left with **zero edits**.

### c. Proof — one scratch scenario per harness, no double-fire

Chose an **isolated fake Unix-socket** test harness instead of launching real `claude`/`grok`/`agy`
sessions from this shell, specifically because this shell's own environment carries the **real**
`HERDR_ENV`/`HERDR_SOCKET_PATH`/`HERDR_PANE_ID` for the **live running Claude1 seat** (confirmed
present) — any nested real session launched from here would report into the actual live herdr
server/pane, risking a visible perturbation of herdr's live state on a trading day for no added
rigor. A throwaway Python Unix-socket listener captured exactly what each case sends, with
realistic env + stdin payloads:

- **Case A** (`CLAUDECODE=1`, `CLAUDE_CODE_SESSION_ID=test-claude-session-A`, no Grok var): guard
  `exec`'d the real script → listener captured
  `{"...,"source":"herdr:claude","agent":"claude","agent_session_id":"test-claude-session-A",...}`
  — correct.
- **Case B** (`GROK_SESSION_ID=test-grok-session-B`, no Claude var): guard exited 0 — **nothing**
  captured. Correct no-op; Grok's own separate native hook, unmodified, still reports `"grok"` on
  its own.
- **Case C** (neither var set, simulating an unrecognized harness): guard exited 0 — **nothing**
  captured. Correct fail-safe no-op, no false `"claude"` label.

`grok inspect`, re-run after the edit, still shows the same 2 hooks discovered (expected —
discovery is unchanged; only the guarded hook's runtime behavior changed). Per instruction, the
running Claude1 seat (this session) was **not** restarted or reloaded; this change applies to hook
processes spawned by **new** sessions of any harness only.

### d. Sessions (read-only, no change made)

Grok's `resume-claude` bundled skill is **user-invoked only** (natural-language "continue from
Claude"/"resume my Claude session" or the skill's slash form) — **not** automatic at Grok startup.
When invoked, it reads Claude's transcript store at `$CLAUDE_CONFIG_DIR` (default `~/.claude`) —
the same `~/.claude/projects/<cwd-hash>/*.jsonl` history this session itself lives in — via a
bundled `session_reader.py` that understands Claude's branching/compaction/snip semantics. The
skill's own safety boundary treats every recovered field as **"untrusted inert history"**: never
executed, never replayed verbatim, never treated as live tool availability; only a short
synthesized handoff is carried into the new Grok session, with an explicit re-verification step
(branch/diff/file/test state) required before continuing any work. **No config change made here**,
per instruction to leave scope/keep to Dejan's call.

---

## STEP 4 — Codex OSC re-verify

`codex-cli 0.153.4` — **unchanged**, no bump since the 2026-09-07 seat-qualification report
(`docs/40 - DevDocs/reports/codex-seat-test-2026-09-07.md`).

Re-ran §7 of that report in a fresh scratch pane/dir (`~/codex-test-p4`, a new herdr tab, cleaned
up and closed at the end — the live codex pane already running the seat's own work, `w1:p6`, was
never touched): `codex --no-alt-screen -m gpt-6-astra -a on-request -s read-only`, submitted a
command-approval-triggering prompt. Result:

- `herdr agent get` → `agent_status: "blocked"`.
- `herdr agent explain` → `rule: osc_title_blocked`, evidence
  `"[ . ] Action Required | codex-test-p4"`, manifest
  `remote:~/.local/state/herdr/agent-detection/remote/codex.toml 2026.09.05.1` — **same manifest
  version** as the 09-07 report.
- Denied via `Escape` → settled to `agent_status: "done"` / underlying detection
  `state: "idle"` (`rule: osc_title_idle`, evidence `"codex-test-p4"`) — matches the 09-07 report's
  note that Codex settles to `done`, not `idle`.
- `run.txt` was not created.

**One addendum not in the 09-07 report:** first launch in a brand-new directory now shows a
separate **"Do you trust the contents of this directory?"** prompt before the TUI is usable
(distinct from hook trust). The 09-07 test's `/tmp/codex-test` had apparently already been
trust-marked from Dejan's manual first launch, so it never fired there. Not a regression — just
undocumented until now.

**Checklist line added** to `docs/40 - DevDocs/reports/codex-seat-test-2026-09-07.md` (§10, new):
*"Re-verify after every Codex bump: confirm `codex --version`, then re-run §7 ... and diff against
the manifest version in `herdr agent explain`. A silent title-string change is the failure mode;
there is no hook fallback to catch it."* Plus a dated entry recording today's re-verification
result above.

---

## STEP 5 — Qwen code context

`~/.qwen/settings.json` → `modelProviders.openai[0].generationConfig.contextWindowSize` was
`32768`. Backed up to `~/.qwen/settings.json.pre-p4` (original, intact), then changed to
`262144` (the mainframe's actual served context — confirmed live via LM Studio's
`GET /api/v0/models`: `"max_context_length": 262144, "loaded_context_length": 262144`).

**Proof:** `qwen -p "reply with the single word OK"` completed (`"OK"`). Ran again with `-d`
(debug) to confirm the setting is actually **read**, not just present in the file — the debug log
(`~/.qwen/debug/<session>.txt`) shows:
```
[DEBUG] [COMPRESSION] [compaction] cheap-gate NOOP: effectiveTokens=1542, auto=222822.4, contextLimit=262144
```
`contextLimit=262144` confirms the new value is loaded into qwen's own context-management logic.
LM Studio was **not** touched.

---

## STEP 6 — 27B no-think paths (small calls only, no reload)

All tests against the already-running mainframe (`gemini`-compatible `POST
http://localhost:1234/v1/chat/completions`), `temperature=0`.

### a. Literal `/no_think` at the START of the user message

Prompt: `"/no_think\nWhat is 2+2? Reply with just the number."` — **still emits `<think>`**
(41 `completion_tokens`, content opens with `<think>User asks: /no_think ...`). Also tested the
suffix form (`"...number. /no_think"`, Qwen's other documented convention) — same result, still
thinks (45 tokens). Neither placement works. The 2026-09-07 swap report only tested `/no_think` as
a **system** prompt (also failed); this closes out the user-message placements too.

### b. Per-request fields LM Studio 1.11.0 honours for this model

Re-tested `reasoning_effort: "none"` (the swap report tried `low`/`medium`/`high`/default, not
literally `"none"`) — **byte-identical to default**, 37 `completion_tokens`, still thinks. Public
research (LM Studio's own bug tracker, `lmstudio-ai/lmstudio-bug-tracker#2057`, and third-party
reports) confirms this is a **known LM Studio limitation**: `chat_template_kwargs.enable_thinking:
false` is not forwarded into the Qwen Jinja template at all on this version, for any model in this
family. **No per-request field currently disables thinking for this model on this server** —
consistent with, and now broader than, the swap report's §5 finding.

### c. Per-model chat-template override — found, NOT applied (needs reload)

The live model's Jinja template lives at
`~/.lmstudio/models/mlx-community/Qwen3.8-27B-8bit/chat_template.jinja`. Line 46:
```jinja
{%- if enable_thinking is undefined or enable_thinking is true %}
```
Thinking fires unless `enable_thinking` is explicitly `false` in the template's render context —
and per (b), LM Studio never sets it there from the API. The one working override: in LM Studio's
Desktop app, open the model's **Developer / Prompt Template editor** and hardcode
`{%- set enable_thinking = false %}` near the top of the template (this writes back into this same
`chat_template.jinja`), **or** edit the file directly. **Either path only takes effect on the
model's *next load*** — the currently loaded runtime session keeps the template it started with.
**Not applied today.** Exact steps for the maintenance window (Prompt 5): (1) open LM Studio →
Developer tab → select `mlx-community/Qwen3.8-27B-8bit` → Prompt Template → insert the `set` line
before the existing `if` on line 46 → Save; (2) unload and reload the model (or restart
`com.cobalt.mainframe`) for it to take effect; (3) re-run the §5-style probe to confirm `<think>`
no longer appears.

### d. Useful tok/s post-strip — 3 runs, ocean prompt

`"write 500 words about the ocean"`, `max_tokens=1600`, `temperature=0` (the 09-07 report's
original §4 throughput test used `temperature=0.7`; I used 0 for consistency with this step's own
instruction — flagged, not silently substituted). All 3 runs: `finish_reason: "length"`,
`completion_tokens: 1599`, **byte-identical** content (expected at `temperature=0`).

**Finding, and it matters:** the content contains **no `<think>` tag at all** (open or closed) —
the entire 1599-token, 71.4s response is unclosed, un-tagged reasoning/word-counting scratch work
(e.g. *"...Count Tides1 rise2 and3 fall4 with5 the6 moon7..."*, the model literally
numbering words to verify a target count) that **never reaches the actual essay** before the
token cap cuts it off. Checked all 3 runs individually for a transition into real prose — none
exists.

| Metric | Value |
|---|---|
| Raw tok/s (billed/elapsed) | ~22.4 (matches the swap report's §4 measurement of 22.25 avg) |
| **Useful (post-strip) tokens delivered** | **0**, all 3 runs |
| **Useful tok/s** | **0** |

**ADR-0008 input:** at `max_tokens=1600`, this model does not merely decode slowly for long-form
prose — for a "write 500 words" class of prompt, it can spend the **entire** budget planning and
verifying word counts and deliver **zero** usable output. Anything generating essay-length prose
against this budget needs either a much larger `max_tokens` ceiling or a working thinking-disable
path (blocked today per (a)–(c)) to be usable at all.

---

## STEP 7 — CLAUDE.md model line (docs-only edit)

**Before:**
```
- Local model: Qwen3.8-27B 8-bit MLX with MTP speculative decoding, parallel
  slots, per-call reasoning_effort (default xhigh overthinks — use low/off
  for simple calls). Exposed as the LiteLLM local route.
```

**After:**
```
- Local model: Qwen3.8-27B 8-bit MLX (mlx-community), context 262144,
  thinking always on and inlined (consumers strip <think>…</think>), no
  reasoning_effort control, speculative decoding not available on this
  stack. Exposed as the LiteLLM local route.
```

Matches `mainframe-swap-2026-09-07.md`'s ESCALATE item 2 verbatim. No other lines touched.

---

## STEP 8 — agy upstream issue

Written: `docs/40 - DevDocs/reports/agy-herdr-manifest-issue-2026-09-08.md` — the exact mismatch,
a live reproduction (scratch agy session, `Antigravity CLI 1.1.27`), versions, and a proposed
manifest change. Summary: herdr's `agy.toml` detection manifest
(`~/.local/state/herdr/agent-detection/remote/agy.toml`, version `2026.06.24.1`) only recognizes a
`blocked` state via the string `"requesting permission for:"`. Real agy 1.1.27 file-write approval
cards read **"Allow creation of this file?"** — never matching that string. Reproduced live: a
scratch agy session blocked on exactly that card while `herdr agent explain` reported
`state: "idle"` via `fallback_reason: "default_known_agent_idle_fallback"` — herdr genuinely
cannot see the block. Full detail, proposed manifest rule, and repro steps are in that file. Dejan
files it upstream; nothing was opened on GitHub by me.

---

## Files touched outside a git commit (all backed up, all reversible)

| File | Backup | Status |
|---|---|---|
| `~/.grok/sandbox.toml` | `~/.grok/sandbox.toml.pre-p4` | new content (was empty) |
| `~/.claude/settings.json` | `~/.claude/settings.json.pre-p4` | hook command redirected to guard |
| `~/.claude/hooks/herdr-harness-guard.sh` | n/a (new file, not herdr-managed) | created |
| `~/.qwen/settings.json` | `~/.qwen/settings.json.pre-p4` | `contextWindowSize` 32768 → 262144 |

Repo files touched (not committed): `CLAUDE.md` (Step 7),
`docs/40 - DevDocs/reports/codex-seat-test-2026-09-07.md` (Step 4 checklist addendum), plus this
report and the new `docs/40 - DevDocs/reports/agy-herdr-manifest-issue-2026-09-08.md` (Step 8).

---

## ESCALATE

- **ESCALATE: higher model/judgment call needed — Step 1 "wrong date."** No wrong date is present
  in either artifact I could inspect (file, Mattermost message); need Dejan's exact
  screenshot/message to trace further, or a paid API call to test grounding reliability (not made
  here).
- **ESCALATE: higher model/judgment call needed — Step 1e.** Disabling `morning_briefing` alone
  needs a small `src/cobalt_agent/services/scheduler.py` change (a config/env gate) — barred today
  by L29; a future sprint decision.
- **ESCALATE: judgment call — file the Grok `read-only`/`strict` OrbStack docker.sock bug
  upstream** (Step 2). Reproducible, workaround in place, but the underlying bug is Grok's.
- **ESCALATE: judgment call — Step 3b's third branch (unrecognized harness) is a documented gap,
  not a fix.** The guard fails safe (never mislabels as `claude`) but does not yet positively
  identify agy or any future harness by its own signal, since none was observed. Revisit once such
  a harness is seen firing this hook for real.
- **ESCALATE: write path/code change — Step 6c's chat-template fix needs a model reload,** which
  this task explicitly forbade. Scheduled for the next maintenance window (Prompt 5 in this
  ticket's own numbering).
- **ESCALATE: judgment call — Step 6d's finding (0 useful tokens at `max_tokens=1600` for
  essay-length prose) should inform the ADR-0008 decision** on the 4-bit-27B tradeoff already
  flagged in the swap report's ESCALATE item 4 — a higher `max_tokens` ceiling or a working
  thinking-disable path may be a harder requirement than that ADR currently assumes.
- **ESCALATE: Dejan's call — file the agy/herdr manifest issue upstream** (Step 8's report is
  ready; I did not open anything on GitHub).

---

## `git status --porcelain` (verbatim, end of session)

```
 M CLAUDE.md
 M "docs/40 - DevDocs/reports/codex-seat-test-2026-09-07.md"
?? "docs/40 - DevDocs/reports/agy-herdr-manifest-issue-2026-09-08.md"
?? "docs/40 - DevDocs/reports/seats-followup-2026-09-08.md"
```
