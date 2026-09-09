# Seat-delegation spike — 2026-09-09 (outside the Ladder)

**Hub:** the Fable 5.1 architect session (Claude1). **Role delegated:** reviewer (read-only) to
four houses, one identical task each, headless. **Verification:** the hub computed ground truth
with Python `ast` + `hashlib` BEFORE spawning and compared field by field (L35 — trust the
artifact, never the report). **No hub spawner exists until F20 (S5)** — each spawn below is
recorded as the `cobalt_jobs` row it would have been (L34). Nothing in production was touched;
Codex1/Gemini1 panes were not needed.

## The task (verbatim, `task.txt`)

```
You are a read-only reviewer. Read the file src/cobalt/vaultwrite/merge.py (relative to the current directory) and reply with ONLY one JSON object, no prose, no markdown fences, with exactly these keys: "file" (the relative path as given), "line_count" (number of lines in the file as `wc -l` would count them), "top_level_functions" (names of module-level `def` functions in file order), "dataclasses" (names of classes decorated with @dataclass, in file order), "sha256" (hex sha256 of the file's bytes). Do not modify anything.
```

Variant `task-agy.txt` (used for the grok rerun and agy): same, plus "using ONLY your file-reading
tool (do not run any shell command)" and `"sha256": null` allowed with a `"note"` key — because
headless Grok and headless agy auto-deny shell commands (see findings).

## Ground truth (hub-computed)

```json
{
 "file": "src/cobalt/vaultwrite/merge.py",
 "line_count": 171,
 "top_level_functions": [
  "_human_view",
  "merge3",
  "merge_body"
 ],
 "dataclasses": [
  "Override",
  "MergeResult"
 ],
 "sha256": "c62d4e965e2f9c26d4b439cb30c8e9e80b1dd8fe9187359c2611b35563fad290"
}
```

## Manifests (the `cobalt_jobs` rows F20 will persist)

| house | role | model | launcher argv | exit | wall | verdict |
|---|---|---|---|---|---|---|
| codex | reviewer | `gpt-6-astra` | `codex exec -m gpt-6-astra -s read-only -C ~/cobalt --skip-git-repo-check "<task>"` | 0 | 15 s | **PASS** |
| grok | reviewer | `grok-4.6-build` | `grok --prompt-file task-agy.txt --sandbox readonly-safe --output-format json` | 0 | 35 s | **PARTIAL/FAIL** |
| qwen | worker | `mainframe` (Qwen3.8-27B-8bit) | `qwen -p "<task>" --approval-mode plan` | 1 | 90 s | **FAIL — server-side template error (see finding 1)** |
| agy | reviewer | `claude-sonnet-4-6` | `agy -p "<task-agy2>" --model claude-sonnet-4-6 --add-dir ~/cobalt --output-format json --log-file agy3.log` | 0 | 13 s | **PARTIAL/FAIL** |

## Artifacts, verbatim, and the field-by-field verdicts

### codex — `PASS`
```
{"file":"src/cobalt/vaultwrite/merge.py","line_count":171,"top_level_functions":["_human_view","merge3","merge_body"],"dataclasses":["Override","MergeResult"],"sha256":"c62d4e965e2f9c26d4b439cb30c8e9e80b1dd8fe9187359c2611b35563fad290"}
```
| `file` | match |
| `line_count` | match |
| `top_level_functions` | match |
| `dataclasses` | match |
| `sha256` | match |
Codex ran a `python3 -c` one-liner INSIDE the read-only sandbox (visible in stderr) — the sandbox
allowed a read-only command, so the sha256 came back. Tokens used: 4,102.

### grok — `PARTIAL/FAIL`
```
{"file": "src/cobalt/vaultwrite/merge.py", "line_count": 172, "top_level_functions": ["_human_view", "merge3", "merge_body"], "dataclasses": ["Override", "MergeResult"], "sha256": null, "note": "file is the given relative path; line_count is the Read tool’s last line number (172) taken as newline count assuming a trailing newline; top_level_functions and dataclasses were read in file order from module-level def and @dataclass names; sha256 is null because hashing the raw bytes is not possible without a shell."}
```
| `file` | match |
| `line_count` | MISMATCH (got 172) |
| `top_level_functions` | match |
| `dataclasses` | match |
| `sha256` | null (not computable headless) |
First two attempts (`--permission-mode plan`, then default) ended `stopReason: cancelled` after
one turn: the streaming trace shows `read_file` completed, then `run_terminal_command` →
`User cancelled the execution` — headless Grok auto-cancels shell commands in the sandbox. The
rerun with the file-tool-only task reached `end_turn` in 2 turns, 42,522 tokens, `$0.0106`
API-equivalent, and got `line_count` WRONG (172: it read the Read tool's last line number as the
newline count). functions and dataclasses correct.

### qwen — FAIL
```
[API Error: Error rendering prompt with jinja template: "Unknown StringValue filter: safe".
```
Turn 1 (the `read_file` tool call) succeeded; turn 2 — the request whose history carries that
tool call with a non-string argument value — failed in LM Studio's Jinja renderer. Root-caused
and reproduced by the hub with curl against production (finding 1).

### agy — `PARTIAL/FAIL`
```
{"file":"src/cobalt/vaultwrite/merge.py","line_count":171,"top_level_functions":["_human_view","merge3","merge_body"],"dataclasses":["Override","MergeResult"],"sha256":null,"note":"line_count is the number of newline characters, equal to total_lines minus 1 (172 lines displayed means 171 newline-separated line endings); top_level_functions identified by scanning every module-level `def` keyword (lines 73, 100, 167), excluding methods; dataclasses identified by @dataclass decorator immediately preceding class definitions (lines 43–44 and 63–64); sha256 is null because no shell command was used and arithmetic computation of SHA-256 from raw bytes is not possible with read-only file tools alone."}

```
| `file` | match |
| `line_count` | match |
| `top_level_functions` | match |
| `dataclasses` | match |
| `sha256` | null (not computable headless) |
First attempt (relative path, no `--add-dir`): SUCCESS status with an EMPTY response and
`denied_actions: [RunCommand]` — headless agy auto-denies shell commands. Second attempt: agy
resolved the relative path against its scratch workspace (`~/.gemini/antigravity-cli/scratch`)
and asked for an absolute path. Third attempt (`--add-dir ~/cobalt`, absolute path, file-tool-only
task): correct on every computable field; sha256 null, stated honestly in its note.

## agy: which model, which quota

* **Model served:** `claude-sonnet-4-6` (from `agy models`; the log's `model_resolver.go:93]
  Resolving model claude-sonnet-4-6` ×3 per run; `resolver.go:85] Model ID claude-sonnet-4-6 not
  in local config, defaulting to CCPA`).
* **Where the request went:** `https://daily-cloudcode-pa.googleapis.com/v1internal` (9 hits in
  `agy3.log`; the only model endpoint in the log). Auth: `server_oauth.go:192] applyAuthResult:
  email=<Dejan's Google account>, authMethod=consumer, quotaProject=` (empty) — the consumer OAuth
  path of Google's Cloud Code API, i.e. the **Google AI Pro entitlement**, no GCP project.
* **Not the Claude plan:** ccusage (`--offline`, today) before/after the spike shows no
  `claude-sonnet-4-6` model row appearing; the Claude rows that moved (`claude-fable-5-1`,
  `claude-opus-5`) are this architect session and the Opus subagents running in parallel. New
  rows `gpt-6-astra` and `grok-4.6-build` are the codex and grok spawns above.
* **Limit stated:** agy's `/usage` quota panel could not be captured over a scripted pty (the
  TUI did not render in a pseudo-terminal, 2 attempts); the Claude Max meter is not
  machine-readable. Dejan can read `/usage` in the Gemini1 pane for the remaining-quota number.
  Conclusion stands on the endpoint + auth-method evidence: **a Claude model on agy bills the
  Google AI Pro quota, not the Anthropic Max plan.**

## Findings

1. **PRODUCTION DEFECT (mainframe template): `| safe` is not a filter LM Studio's Jinja engine
   knows.** Upstream `chat_template.jinja` line 138 renders tool-call arguments with
   `args_value | tojson | safe` whenever an argument VALUE is not a string. Reproduced with
   curl against production: history tool_call arguments `{"path":"x.py"}` → OK;
   `{"path":"x.py","limit":5}` and `{"path":"x.py","flags":["a"]}` → `Error rendering prompt
   with jinja template: "Unknown StringValue filter: safe"`. Consequence: the Qwen seat dies on
   turn 2 of any tool workflow with a numeric/array argument (the 09-07 `glob` test passed only
   because its arguments were strings). **Fix folded into Prompt 5** (repo-owned template drops
   `| safe`; regression test; lands at Phase B).
2. **Headless = no shell, by construction, on Grok and agy.** Both auto-deny/cancel terminal
   commands; both READ files fine. A reviewer task must therefore be answerable from reads
   alone, or the launcher grants a specific command allow-rule (deterministic, not
   model-judged — L37). Codex's read-only sandbox let a read-only command through.
3. **agy needs `--add-dir` and absolute paths** headlessly; without a workspace it resolves
   relative paths against its own scratch dir and asks back (no error, exit 0 — a plausible
   empty artifact if the hub did not verify).
4. **Verification caught a wrong number.** Grok's `line_count` 172 vs 171 — plausible, wrong,
   and invisible without the hub's ground truth. This is the L35 case in one row.
5. **`codex exec` takes no `-a/--ask-for-approval`** (that flag is TUI-only); the seat rule
   "never bare" for `exec` means `-s read-only` (or `-s workspace-write` in a worktree) — the
   approval policy in exec is non-interactive by nature.

## Cost of the spike
codex 4,102 tokens · grok 42,522 tokens ($0.0106 API-equiv) · agy 19,534 tokens (Google quota)
· qwen 1 failed turn (local). Hub time ≈ 25 min including the root-cause repro.

## ESCALATE
* Prompt 5 Phase B must land the `| safe` fix before the Qwen seat is trusted for tool work.
* Role launcher profiles (L33) should encode finding 2: reviewer = reads only; a "sha/verify"
  step belongs to the hub, never to the worker.
* agy `/usage` remains a human read (Gemini1 pane) until a machine-readable quota source exists.
