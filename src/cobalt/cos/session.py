"""The CoS session: the Agent SDK client wrapper (F20 FINAL §4, §5; F-16, F-19; spike D4, D5, U6; L41, L55).

THE SDK IS IMPORTED ONLY INSIDE `sdk_client_factory`, never at module top:
`import cobalt.cli` (the radar's import root) does not load it.

THE PERMISSION CLASS (§4). Allowed = the seven `cos/tools.py` tools only;
the built-in base set is empty (`tools=[]`) and every built-in is also on
the disallowed list (Bash, Write, Edit, NotebookEdit, WebFetch, WebSearch,
Task, Agent, Read, Grep, Glob, …). `setting_sources=[]` and
`strict_mcp_config=True` (D4): no user, project or connector config enters
the session. The mode is `dontAsk` — a call nothing pre-approved is refused,
no prompt — and never `bypassPermissions` (L55). No hook and no
`can_use_tool` callback (C7, U1). Whether an unlisted tool is refused with
no callback is UNPROVEN until T10 runs live (B0).

THE CHILD ENV (§4, L41). The SDK spawns the CLI with the parent's whole
`os.environ` merged under `options.env` (its transport, `connect`). So the
spawn runs with `os.environ` replaced by exactly PATH, HOME, USER, LANG and
COBALT_ENV, and the parent's env is put back the moment the spawn returns:
no API key, base URL, master key or DB credential reaches the child. X12
reads the real child's env at the gate.

FAILURE (§5). A turn fails on `is_error` or a `terminal_reason` other than
`completed`, never on the vendor `subtype` alone (D5). Cobalt counts rounds
and kills the CLI at `cos.max_turns`; each turn runs under `asyncio.wait_for`
of `cos.turn_timeout_s`; a stream that ends with no result fails. Every
failure DMs. A failed resume opens a fresh session and DMs (F-13).

PARALLEL TOOL USE (U6). Each request tool call is its own `request_action`,
which writes its own row and posts its own card, so a parallel turn posts
one card per request (pinned by a test).
"""

from __future__ import annotations

import asyncio
import os
import signal
import subprocess
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Optional

from loguru import logger

from . import tools as cos_tools

MAX_TURNS_KEY = "cos.max_turns"
TIMEOUT_KEY = "cos.turn_timeout_s"
POLL_KEY = "cos.poll_interval_s"

#: §4: the clean env passed to the CLI — these names and nothing else.
ALLOWED_ENV = ("PATH", "HOME", "USER", "LANG", "COBALT_ENV")

#: §4 / F-16 / U6: every built-in, disallowed by name as well as absent
#: from the (empty) base set.
DISALLOWED_BUILTINS = (
    "Bash", "BashOutput", "KillShell", "Write", "Edit", "MultiEdit", "NotebookEdit",
    "WebFetch", "WebSearch", "Task", "Agent", "Read", "Grep", "Glob", "LS", "TodoWrite",
    "ExitPlanMode", "Skill", "SlashCommand", "ListMcpResourcesTool", "ReadMcpResourceTool",
)

#: The in-process MCP server's name; the CLI sees `mcp__cobalt__<tool>`.
SERVER_NAME = "cobalt"
#: Never anything else: refuses what nothing pre-approved, with no prompt.
PERMISSION_MODE = "dontAsk"
#: The terminal reason of a clean turn; any other reported reason fails it.
CLEAN_TERMINAL = "completed"


class CosConfigError(RuntimeError):
    """A CoS tunable is missing or invalid — crash, never fall back (L1)."""


def tunable_int(key: str) -> int:
    """A positive integer tunable; missing, null, non-integer or <= 0 raises."""
    from cobalt.taxonomy.loader import load_tunables

    row = load_tunables().by_key.get(key)
    if row is None or row.value is None:
        raise CosConfigError(f"tunable {key!r} has no value in tunables.yaml — no built-in default (L1, F16)")
    if isinstance(row.value, bool) or not isinstance(row.value, int) or row.value <= 0:
        raise CosConfigError(f"tunable {key!r} must be a positive integer, got {row.value!r}")
    return row.value


def sdk_tool_name(name: str) -> str:
    """`cards.open` -> `mcp__cobalt__cards_open` (a tool name carries no dot)."""
    return f"mcp__{SERVER_NAME}__{name.replace('.', '_')}"


def child_env(parent: Optional[dict] = None) -> dict[str, str]:
    parent = os.environ if parent is None else parent
    return {k: parent[k] for k in ALLOWED_ENV if k in parent}


def build_options(*, model: str, cwd: Path, charter: str, max_turns: int,
                  resume: Optional[str]) -> dict[str, Any]:
    """The session's options as plain data (no SDK import)."""
    return {
        "tools": [],
        "allowed_tools": [sdk_tool_name(n) for n in cos_tools.TOOLS],
        "disallowed_tools": list(DISALLOWED_BUILTINS),
        "setting_sources": [],
        "strict_mcp_config": True,
        "permission_mode": PERMISSION_MODE,
        "env": child_env(),
        "cwd": str(cwd),
        "model": model,
        "max_turns": max_turns,
        "resume": resume,
        "system_prompt": charter,
    }


@contextmanager
def _scrubbed_environ(env: dict[str, str]):
    """`os.environ` is exactly `env` for the spawn, then restored."""
    saved = dict(os.environ)
    os.environ.clear()
    os.environ.update(env)
    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(saved)


def _kill_tree(pid: int) -> None:
    """SIGKILL the CLI and every descendant. The tree is walked first
    (orphaned tool children, spike Q4); then, when the CLI leads its own
    process group (`_SdkClient.connect` spawns it in a new session), the
    whole group goes too: a descendant whose parent already exited is
    reparented out of the tree but stays in the group (check r2 O1). The
    resident's own group is never signalled."""
    try:
        group = os.getpgid(pid)
    except ProcessLookupError:
        group = None
    seen: list[int] = []
    frontier = [pid]
    while frontier:
        current = frontier.pop()
        seen.append(current)
        out = subprocess.run(["pgrep", "-P", str(current)], capture_output=True, text=True).stdout
        frontier.extend(int(p) for p in out.split() if p.isdigit())
    for p in reversed(seen):
        try:
            os.kill(p, signal.SIGKILL)
        except ProcessLookupError:
            pass
    if group == pid and group != os.getpgrp():
        try:
            os.killpg(group, signal.SIGKILL)
        except ProcessLookupError:
            pass


@contextmanager
def _own_session_spawn():
    """Every process the SDK opens inside this block starts in a new session,
    so the CLI leads its own process group (row W (1); check r2 O1). The SDK
    spawns through `anyio.open_process`; it is wrapped for the open only and
    put back the moment it returns, as `_scrubbed_environ` does for the env."""
    import anyio

    real = anyio.open_process

    async def open_process(*args, **kwargs):
        kwargs.setdefault("start_new_session", True)
        return await real(*args, **kwargs)

    anyio.open_process = open_process
    try:
        yield
    finally:
        anyio.open_process = real


class _SdkClient:
    """The real client behind the four calls the session makes, plus `kill`."""

    def __init__(self, client):
        self._client = client

    async def connect(self):
        with _own_session_spawn():
            await self._client.connect()

    async def query(self, text: str):
        await self._client.query(text)

    def receive_response(self):
        return self._client.receive_response()

    async def disconnect(self):
        await self._client.disconnect()

    def kill(self):
        process = getattr(getattr(self._client, "_transport", None), "_process", None)
        if process is not None and process.returncode is None:
            _kill_tree(process.pid)


def sdk_client_factory(options: dict[str, Any], tool_call: Callable[[str, dict], str]) -> _SdkClient:
    """Build the SDK client with the in-process tool server. THE SDK IMPORT."""
    import claude_agent_sdk as sdk

    wrapped = []
    for name, tool_def in cos_tools.TOOLS.items():
        async def handler(args, _name=name):
            text = await asyncio.to_thread(tool_call, _name, dict(args or {}))
            return {"content": [{"type": "text", "text": text}]}

        wrapped.append(sdk.tool(name.replace(".", "_"), tool_def.description, tool_def.schema)(handler))
    server = sdk.create_sdk_mcp_server(name=SERVER_NAME, tools=wrapped)
    kwargs = {k: v for k, v in options.items() if v is not None}
    return _SdkClient(sdk.ClaudeSDKClient(options=sdk.ClaudeAgentOptions(
        **kwargs, mcp_servers={SERVER_NAME: server})))


@dataclass
class TurnOutcome:
    ok: bool
    reply: str = ""
    error: Optional[str] = None
    session_id: Optional[str] = None
    num_turns: Optional[int] = None
    result_subtype: Optional[str] = None
    is_error: Optional[bool] = None
    terminal_reason: Optional[str] = None


class _MaxTurns(Exception):
    """Carries the text streamed before the kill: the partial reply (FINAL §5)."""

    def __init__(self, partial: str):
        super().__init__(partial)
        self.partial = partial


class _ResumeFailed(Exception):
    pass


def _is_result(msg) -> bool:
    return all(hasattr(msg, a) for a in ("is_error", "num_turns", "subtype"))


def _texts(msg) -> list[str]:
    return [b.text for b in getattr(msg, "content", None) or [] if isinstance(getattr(b, "text", None), str)]


class CosSession:
    """One turn at a time, on the stored session id."""

    def __init__(
        self,
        *,
        model: str,
        scratch_dir: Path,
        charter: str,
        client_factory: Optional[Callable] = None,
        notify: Optional[Callable[[str], object]] = None,
        tool_call: Callable[[str, dict], str] = cos_tools.call,
        max_turns: Optional[int] = None,
        timeout_s: Optional[float] = None,
    ):
        self.model = model
        self.scratch_dir = Path(scratch_dir)
        self.charter = charter
        self.client_factory = client_factory or sdk_client_factory
        self.notify = notify or _dm
        self.tool_call = tool_call
        self.max_turns = max_turns if max_turns is not None else tunable_int(MAX_TURNS_KEY)
        self.timeout_s = timeout_s if timeout_s is not None else tunable_int(TIMEOUT_KEY)

    def _fail(self, reason: str, **fields) -> TurnOutcome:
        self.notify(f"CoS turn failed: {reason}")
        logger.error("CoS turn FAILED: {}", reason)
        return TurnOutcome(ok=False, error=reason, **fields)

    async def run_turn(self, text: str, *, resume: Optional[str]) -> TurnOutcome:
        try:
            return await self._attempt(text, resume)
        except _ResumeFailed as e:
            self.notify(f"CoS: resume of the stored session failed ({e}); opened a fresh session")
            try:
                return await self._attempt(text, None)
            except _ResumeFailed as again:  # pragma: no cover - resume is None here
                return self._fail(str(again))

    async def _attempt(self, text: str, resume: Optional[str]) -> TurnOutcome:
        options = build_options(model=self.model, cwd=self.scratch_dir, charter=self.charter,
                                max_turns=self.max_turns, resume=resume)
        try:
            client = self.client_factory(options, self.tool_call)
        except Exception as e:  # noqa: BLE001
            if resume:
                raise _ResumeFailed(f"{type(e).__name__}: {e}") from None
            return self._fail(f"the session did not open ({type(e).__name__}: {e})")
        # The open is part of the turn: it runs under the same timeout (C3c).
        try:
            with _scrubbed_environ(options["env"]):
                await asyncio.wait_for(client.connect(), self.timeout_s)
        except asyncio.TimeoutError:
            client.kill()
            return self._fail(f"timeout after {self.timeout_s}s opening the session; the CLI was killed")
        except Exception as e:  # noqa: BLE001
            if resume:
                raise _ResumeFailed(f"{type(e).__name__}: {e}") from None
            return self._fail(f"the session did not open ({type(e).__name__}: {e})")
        try:
            return await asyncio.wait_for(self._converse(client, text), self.timeout_s)
        except asyncio.TimeoutError:
            client.kill()
            return self._fail(f"timeout after {self.timeout_s}s; the CLI was killed")
        except _MaxTurns as stop:
            client.kill()
            return self._fail(f"turn stopped at max turns ({self.max_turns}); the CLI was killed",
                              reply=stop.partial)
        except Exception as e:  # noqa: BLE001 - a dead CLI is a failed turn, said out loud
            client.kill()
            return self._fail(f"the session died ({type(e).__name__}: {e})")
        finally:
            try:
                await asyncio.wait_for(client.disconnect(), 10)
            except Exception as e:  # noqa: BLE001
                logger.error("CoS: disconnect after the turn failed ({}: {})", type(e).__name__, e)

    async def _converse(self, client, text: str) -> TurnOutcome:
        await client.query(text)
        rounds, parts, result = 0, [], None
        async for msg in client.receive_response():
            if _is_result(msg):
                result = msg
                continue
            # A tool-result message answers a round; it is not one (the CLI's
            # own `max_turns` counts the same way).
            if type(msg).__name__ == "UserMessage":
                continue
            if getattr(msg, "content", None) is not None and isinstance(msg.content, list):
                rounds += 1
                parts.extend(_texts(msg))
                if rounds > self.max_turns:
                    raise _MaxTurns("\n".join(parts))
        if result is None:
            return self._fail("the stream ended with no result")
        fields = dict(session_id=getattr(result, "session_id", None), num_turns=result.num_turns,
                      result_subtype=result.subtype, is_error=bool(result.is_error),
                      terminal_reason=getattr(result, "terminal_reason", None))
        reply = getattr(result, "result", None) or "\n".join(parts)
        if result.is_error:
            return self._fail(f"the result is an error (subtype {result.subtype!r})", reply=reply, **fields)
        if fields["terminal_reason"] not in (None, CLEAN_TERMINAL):
            return self._fail(f"terminal reason {fields['terminal_reason']!r}", reply=reply, **fields)
        return TurnOutcome(ok=True, reply=reply, **fields)


def _dm(text: str) -> None:
    from cobalt.notify.mattermost import send_dm

    try:
        send_dm(text)
    except Exception as e:  # noqa: BLE001 - the failure is already logged loud
        logger.error("CoS: the failure DM could not be sent ({}: {})", type(e).__name__, e)


__all__ = [
    "ALLOWED_ENV", "CLEAN_TERMINAL", "CosConfigError", "CosSession", "DISALLOWED_BUILTINS",
    "PERMISSION_MODE", "SERVER_NAME", "TurnOutcome", "build_options", "child_env",
    "sdk_client_factory", "sdk_tool_name", "tunable_int",
]
