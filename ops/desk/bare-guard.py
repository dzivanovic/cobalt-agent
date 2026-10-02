#!/usr/bin/env python3
# bare-guard.py — a Claude Code PreToolUse hook (his 2026-10-01 R45 part 1; card 17 A1).
# Reads the hook's JSON on stdin. A tool other than Bash -> exit 0. For Bash it scans
# tool_input.command with a quote-aware scanner (single quotes, double quotes, $'…' ANSI-C
# quotes, backslash escapes) and BLOCKS (exit 2, one line on stderr) when, OUTSIDE quotes, the command holds
# `&&`, `||`, a pipe `|`, `;`, a lone `&`, a newline, a `>` or `<` redirect, or -- outside
# quotes OR inside double quotes -- a backtick or `$(`. ONE exception: a command that ends
# with the exact text ` < /dev/null` (the house-probe shape) passes that redirect. Leading
# NAME=value words are part of the one command. Any error inside the guard -> exit 0: it
# never blocks work because it broke. Writes nothing.
import json
import sys

PROBE_TAIL = " < /dev/null"
BLOCK = (
    "NOT A REFUSAL. Dejan's rule: one bare command per call, and this call contains {found}. "
    "Resend the SAME commands now, one per call, in order. Do not report this to Dejan as a failure."
)


def scan(command):
    """Return (what was found, in order of first sight; the quote state at the end)."""
    found = []

    def see(what):
        if what not in found:
            found.append(what)

    quote = None
    i, n = 0, len(command)
    while i < n:
        c = command[i]
        nxt = command[i + 1] if i + 1 < n else ""
        if quote == "'":
            if c == "'":
                quote = None
        elif quote == "$'":
            # ANSI-C quoting: a backslash escapes, `\'` does not close
            if c == "\\":
                i += 2
                continue
            if c == "'":
                quote = None
        elif quote == '"':
            if c == "\\":
                i += 2
                continue
            if c == '"':
                quote = None
            elif c == "`":
                see("a backtick")
            elif c == "$" and nxt == "(":
                see("`$(`")
        elif c == "\\":
            i += 2
            continue
        elif c == "$" and nxt == "'":
            quote = "$'"
            i += 2
            continue
        elif c in "'\"":
            quote = c
        elif c == "`":
            see("a backtick")
        elif c == "$" and nxt == "(":
            see("`$(`")
        elif c == "&":
            if nxt == "&":
                see("`&&`")
                i += 2
                continue
            see("a background `&`")
        elif c == "|":
            if nxt == "|":
                see("`||`")
                i += 2
                continue
            see("a pipe `|`")
        elif c == ";":
            see("`;`")
        elif c == "\n":
            see("a newline")
        elif c in "<>":
            see("a redirect `%s`" % c)
        i += 1
    return found, quote


def main():
    try:
        event = json.loads(sys.stdin.read())
        if event.get("tool_name") != "Bash":
            return 0
        command = event["tool_input"]["command"]
        if not isinstance(command, str):
            return 0
        found, quote = [], None
        if command.endswith(PROBE_TAIL):
            found, quote = scan(command[: -len(PROBE_TAIL)])
        if not command.endswith(PROBE_TAIL) or quote is not None:
            found, quote = scan(command)
        if not found:
            return 0
        sys.stderr.write(BLOCK.format(found=", ".join(found)) + "\n")
        return 2
    except Exception:
        return 0


if __name__ == "__main__":
    sys.exit(main())
