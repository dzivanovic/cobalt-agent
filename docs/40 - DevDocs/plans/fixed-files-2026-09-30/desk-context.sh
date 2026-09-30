#!/bin/sh
# desk-context.sh <session-id-prefix> [threshold]
# Read-only. Prints the desk's CURRENT context size in tokens, read from the last recorded
# model usage in its own transcript (~/.claude/projects/-Users-cobalt-cobalt/<id>*.jsonl):
# input + cache_read + cache_creation. Prints REFRESH when >= threshold (default 400000,
# ruled 2026-09-23 R98). Writes nothing.
id="$1"; thr="${2:-400000}"
f=$(ls -t /Users/cobalt/.claude/projects/*/"$id"*.jsonl 2>/dev/null | head -1)
[ -z "$f" ] && { echo "no transcript for $id"; exit 2; }
tail -r "$f" | grep -m1 '"usage"' | python3 -c '
import json,sys
thr=int(sys.argv[1]); u=json.loads(sys.stdin.read())["message"]["usage"]
c=u.get("input_tokens",0)+u.get("cache_read_input_tokens",0)+u.get("cache_creation_input_tokens",0)
print(f"context {c} of {thr} — " + ("REFRESH" if c>=thr else "ok"))' "$thr"
