# Qwen Code upstream issue — draft for Dejan to file (2026-09-09)

Repo: QwenLM/qwen-code (GitHub). Dejan files; Cobalt keeps the workaround until it lands.

---

**Title:** `cron_list` and `list_agents` tool schemas omit `parameters.properties`, rejected by
OpenAI-compatible servers (LM Studio 400 on every turn)

**Version:** Qwen Code 0.23.x (observed on 0.23.0 and 0.23.2, npm), macOS arm64, Node 26.

**Setup:** `security.auth.selectedType = openai`, base URL = LM Studio's OpenAI-compatible
endpoint (`http://localhost:1234/v1`), a local model served under a custom identifier.

**What happens:** every request fails with HTTP 400 from the server. LM Studio's request log
shows the rejected members are `tools[5]` (`cron_list`) and `tools[15]` (`list_agents`): both
are sent with `"parameters": {"type": "object"}` and no `properties` key. Servers that
validate tool schemas against the OpenAI function-calling shape (LM Studio does) require
`properties` to be present — an empty object is fine, a missing key is not. Every other tool
Qwen Code sends carries `properties`, and the request succeeds once those two are removed.

**Expected:** tools with no arguments are emitted as
`"parameters": {"type": "object", "properties": {}}` (optionally `"required": []`).

**Repro:**
1. Configure the OpenAI auth type against LM Studio (any loaded model).
2. `qwen -p "reply with the single word OK"` → 400 on the first turn.
3. Add to `~/.qwen/settings.json`: `{"tools": {"exclude": ["cron_list", "list_agents"]}}`.
4. Same command → `OK`. The request no longer carries either tool.

**Workaround in use:** the `tools.exclude` above. It costs the two tools; a `properties: {}`
in their declarations would restore them.

**Environment note:** the same endpoint serves Claude Code, Grok Build CLI and Codex CLI
sessions without this error; the schema difference is specific to these two Qwen Code tools.
